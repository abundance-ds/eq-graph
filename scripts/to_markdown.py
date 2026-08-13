#!/usr/bin/env python3
"""Convert the harvested full texts to Markdown, ready for stage-2 extraction.

Offline and deterministic: reads `input/projects/*/papers/*.{xml,pdf}`, writes
`corpus/<project id>/<same stem>.md` plus `corpus/index.json`. Rerunning is cheap --
a paper is reconverted only when its source bytes, this script, or the converting
tool changed.

Two sources, two toolchains. Europe PMC JATS XML goes through pandoc, below.
Publisher PDFs go through poppler, in `pdf_markdown.py`; they carry no structural
markup at all, so what comes back is thinner -- no author list, no keywords, and
tables flattened into loose lines. Prefer the XML wherever a paper is held as both.

    python3 scripts/to_markdown.py              # convert what changed
    python3 scripts/to_markdown.py --force      # reconvert everything
    python3 scripts/to_markdown.py 20170600     # just these projects
    python3 scripts/to_markdown.py --beside 341-RA   # write next to the sources

What pandoc alone does not give us, and this script adds:

* **The abstract.** The JATS reader files it under document metadata, and every
  Markdown writer drops it, so a plain `pandoc -f jats -t gfm` silently loses the
  single most information-dense section of the paper.
* **The reference list.** The reader moves `<ref-list>` into citeproc metadata and
  leaves an empty `<div id="refs">` behind. Running `--citeproc` does not rescue it:
  Europe PMC's `<mixed-citation>` refs carry no fields citeproc understands, so every
  entry renders as "n.d.-a" *and* the numeric markers in the body are rewritten to
  match. So citations stay as pandoc leaves them without citeproc -- the original
  `[1]`, `[4-7]` labels -- and the reference list is read straight out of the XML and
  written back into that empty div, keyed by the same labels.
* **Front matter.** Ids, journal, date, authors with ORCIDs, affiliations, keywords
  and licence, none of which survive into the body, plus the provenance recorded for
  the file by the `fulltext` stage.

Headings are shifted down one level so the article title is the only `#`, and the
abstract's internal sections sit under `## Abstract` rather than colliding with the
body's own `## Methods`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import pdf_markdown

REPO = Path(__file__).resolve().parent.parent
PROJECTS_DIR = REPO / "input" / "projects"
OUT_DIR = REPO / "corpus"

# Bump when a change here alters the Markdown produced, so the next run picks the
# change up without --force. Mirrors match.EXTRACTOR_VERSION.
CONVERTER_VERSION = 1

XLINK_HREF = "{http://www.w3.org/1999/xlink}href"

# gfm rather than pandoc's own markdown: the grid tables the latter emits pad every
# cell to the widest column, inflating this corpus by a fifth for no added meaning.
# gfm writes pipe tables where the shape allows and falls back to HTML where it does
# not, which is what the source was anyway.
PANDOC_TO = "gfm"

TEMPLATE = """# $title$

$if(abstract)$
## Abstract

$abstract$

$endif$
$body$
"""

# Header runs over the metadata as well as the body, so the abstract's own sections
# are already demoted once by the time Meta sees them; the second pass puts them
# under `## Abstract` instead of beside it.
LUA_FILTER = """-- Markdown has no h7: past six hashes the line stops being a heading and
-- renders as literal text, so deeply nested JATS sections clamp instead.
local function demote(h)
  h.level = math.min(h.level + 1, 6)
  return h
end

function Header(h)
  return demote(h)
end

function Meta(m)
  if m.abstract then
    m.abstract = pandoc.walk_block(pandoc.Div(m.abstract), {Header = demote}).content
  end
  return m
end
"""

EMPTY_REFS_RE = re.compile(r'<div id="refs">\s*</div>')
STAMP_RE = re.compile(
    r'^(source_sha256|converter_version|pandoc|poppler): (.+)$', re.MULTILINE
)


def rel(path: Path) -> str:
    """Repository-relative where possible -- `--out` may point outside it."""
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def run(cmd: list[str]) -> str:
    return subprocess.run(
        cmd, check=True, capture_output=True, text=True, encoding="utf-8"
    ).stdout


def pandoc_version() -> str:
    try:
        first = run(["pandoc", "--version"]).splitlines()[0]
    except FileNotFoundError:
        sys.exit(
            "pandoc not found. Install it (brew install pandoc) and rerun; "
            "this script is a wrapper around its JATS reader."
        )
    return first.split()[1]


# --------------------------------------------------------------------------- XML


def text_of(el) -> str:
    """All descendant text of an element, whitespace collapsed."""
    if el is None:
        return ""
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def first(root, *paths):
    for path in paths:
        el = root.find(path)
        if el is not None:
            return el
    return None


def article_ids(meta) -> dict[str, str]:
    ids = {}
    for el in meta.findall("article-id"):
        kind = el.get("pub-id-type")
        if kind:
            ids[kind] = text_of(el)
    return ids


def publication_date(meta) -> str | None:
    """The earliest complete date on offer, preferring electronic publication.

    JATS carries several `<pub-date>`s -- epub, ppub, a collection year -- and they
    disagree by months. Preference order is fixed so the same file always yields the
    same date.
    """
    dates = meta.findall("pub-date")
    ordered = []
    for wanted in ("epub", "ppub", "collection", None):
        for el in dates:
            kind = el.get("pub-type") or el.get("date-type")
            if kind == wanted or (wanted is None and el not in ordered):
                ordered.append(el)
    for el in ordered:
        year = text_of(el.find("year"))
        if not year:
            continue
        month = text_of(el.find("month"))
        day = text_of(el.find("day"))
        if month and day:
            return f"{year}-{int(month):02d}-{int(day):02d}"
        if month:
            return f"{year}-{int(month):02d}"
        return year
    return None


def affiliations(meta) -> list[dict]:
    """Every `<aff>` in the article, keyed by the id its authors point at.

    Affiliations are the only institution evidence in the file and pandoc emits them
    nowhere in the body, so they are lifted into the front matter instead of lost.
    """
    out = []
    for el in meta.iter("aff"):
        label = text_of(el.find("label"))
        text = text_of(el)
        if label and text.startswith(label):
            text = text[len(label) :].strip()
        if text:
            out.append({"id": el.get("id"), "name": text})
    return out


def authors(meta) -> list[dict]:
    out = []
    for contrib in meta.iter("contrib"):
        kind = contrib.get("contrib-type")
        if kind not in (None, "author"):
            continue
        name_el = contrib.find("name")
        if name_el is not None:
            surname = text_of(name_el.find("surname"))
            given = text_of(name_el.find("given-names"))
            name = " ".join(part for part in (given, surname) if part)
        else:
            name = text_of(first(contrib, "string-name", "collab"))
        if not name:
            continue
        entry = {"name": name}
        orcid = contrib.find('contrib-id[@contrib-id-type="orcid"]')
        if orcid is not None:
            entry["orcid"] = text_of(orcid)
        refs = [
            xref.get("rid")
            for xref in contrib.findall('xref[@ref-type="aff"]')
            if xref.get("rid")
        ]
        if refs:
            entry["affiliation_ids"] = refs
        out.append(entry)
    return out


def element_citation_text(el) -> str:
    """Assemble a citation string from a structured `<element-citation>`."""
    parts = []
    names = []
    for group in el.findall("person-group"):
        for name in group.findall("name"):
            surname = text_of(name.find("surname"))
            given = text_of(name.find("given-names"))
            joined = " ".join(part for part in (surname, given) if part)
            if joined:
                names.append(joined)
        for collab in group.findall("collab"):
            names.append(text_of(collab))
    if names:
        # Initials already carry their own full stop -- "Cella D.F." not "Cella D.F..".
        joined = ", ".join(names)
        parts.append(joined if joined.endswith(".") else joined + ".")
    for tag in ("article-title", "chapter-title"):
        title = text_of(el.find(tag))
        if title:
            parts.append(title.rstrip(".") + ".")
    source = text_of(el.find("source"))
    if source:
        parts.append(source.rstrip(".") + ".")

    year = text_of(el.find("year"))
    volume = text_of(el.find("volume"))
    issue = text_of(el.find("issue"))
    fpage = text_of(el.find("fpage"))
    lpage = text_of(el.find("lpage"))
    pages = f"{fpage}–{lpage}" if fpage and lpage else fpage
    locator = year
    if volume:
        locator = f"{locator};{volume}" if locator else volume
    if issue:
        locator += f"({issue})"
    if pages:
        locator = f"{locator}:{pages}" if locator else pages
    if locator:
        parts.append(locator + ".")

    publisher = text_of(el.find("publisher-name"))
    location = text_of(el.find("publisher-loc"))
    if publisher:
        parts.append(", ".join(p for p in (location, publisher) if p) + ".")
    return " ".join(parts)


def references(root) -> list[str]:
    """The reference list as `<label>. <citation>` lines, in document order.

    Three shapes occur across this corpus: a Springer-style `<named-content
    content-type="citation-string">`, a free-text `<mixed-citation>`, and a
    structured `<element-citation>`; `<citation-alternatives>` wraps more than one of
    them, and the `.//` lookups pick the richest available.
    """
    out = []
    for index, ref in enumerate(root.findall(".//ref-list/ref"), start=1):
        source = first(
            ref,
            './/named-content[@content-type="citation-string"]',
            ".//mixed-citation",
        )
        if source is not None:
            text = text_of(source)
        else:
            element = ref.find(".//element-citation")
            text = element_citation_text(element) if element is not None else ""
        if not text:
            continue

        doi = ""
        for el in ref.iter():
            if el.tag == "pub-id" and el.get("pub-id-type") == "doi":
                doi = text_of(el)
            elif el.tag == "ext-link" and el.get("ext-link-type") == "doi":
                doi = doi or (el.get(XLINK_HREF) or text_of(el))
            if doi:
                break
        if doi and doi.lower() not in text.lower():
            text = f"{text.rstrip('.')}. doi:{doi}"

        label = text_of(ref.find("label")).rstrip(".") or str(index)
        out.append(f"{label}. {text}")
    return out


# ------------------------------------------------------------------ front matter


def front_matter(root, provenance: dict) -> dict:
    meta = first(root, ".//article-meta")
    if meta is None:
        meta = ET.Element("article-meta")
    journal = first(
        root,
        ".//journal-meta/journal-title-group/journal-title",
        ".//journal-meta/journal-title",
    )
    licence_el = first(root, ".//permissions/license")
    keywords = [text_of(kwd) for kwd in root.iter("kwd")]
    ids = article_ids(meta)
    pmcid = ids.get("pmc") or ids.get("pmcid")
    if pmcid and not pmcid.upper().startswith("PMC"):
        pmcid = f"PMC{pmcid}"

    return {
        "project_id": provenance.get("project_id"),
        "work_id": provenance.get("work_id"),
        "doi": ids.get("doi") or provenance.get("doi"),
        "pmid": ids.get("pmid"),
        "pmcid": pmcid,
        "title": text_of(first(meta, "title-group/article-title"))
        or provenance.get("title"),
        "journal": text_of(journal) or None,
        "publication_date": publication_date(meta),
        "volume": text_of(first(meta, "volume")) or None,
        "issue": text_of(first(meta, "issue")) or None,
        "authors": authors(meta),
        "affiliations": affiliations(meta),
        "keywords": sorted({kwd for kwd in keywords if kwd}),
        "licence": provenance.get("licence"),
        "licence_url": (licence_el.get(XLINK_HREF) if licence_el is not None else None),
        "source_file": provenance.get("source_file"),
        "source_url": provenance.get("source_url"),
        "source_method": provenance.get("method"),
        "source_sha256": provenance.get("sha256"),
        "converter": "scripts/to_markdown.py",
        "converter_version": CONVERTER_VERSION,
        "pandoc": provenance.get("pandoc"),
    }


def pdf_front_matter(provenance: dict, stats: dict) -> dict:
    """Front matter for a paper held only as PDF.

    Thinner than the JATS equivalent by necessity. A publisher PDF carries no author
    list, keywords or affiliations in any form a converter can trust -- they are
    drawn on the page like everything else -- so the identifiers come from the
    manifest the `fulltext` stage wrote, and the fields JATS would have supplied are
    simply absent rather than guessed at.
    """
    return {
        "project_id": provenance.get("project_id"),
        "work_id": provenance.get("work_id"),
        "doi": provenance.get("doi"),
        "title": provenance.get("title"),
        "licence": provenance.get("licence"),
        "source_file": provenance.get("source_file"),
        "source_url": provenance.get("source_url"),
        "source_method": provenance.get("method"),
        "source_sha256": provenance.get("sha256"),
        "source_format": "pdf",
        "pages": stats.get("pages"),
        "cover_sheet_pages_dropped": stats.get("cover_sheet_pages_dropped"),
        "running_heads_dropped": stats.get("running_heads_dropped"),
        "symbol_runs_repaired": stats.get("symbol_runs_repaired"),
        "converter": "scripts/pdf_markdown.py",
        "converter_version": pdf_markdown.PDF_CONVERTER_VERSION,
        "poppler": provenance.get("poppler"),
    }


def yaml_block(data: dict, indent: int = 0) -> list[str]:
    """Minimal YAML emitter -- JSON scalars are valid YAML, so quoting is free.

    PyYAML is deliberately not imported: `requests` is the repository's only
    third-party dependency and this does not warrant a second.
    """
    pad = " " * indent
    lines = []
    for key, value in data.items():
        if value is None or value == [] or value == {} or value == "":
            continue
        if isinstance(value, dict):
            lines.append(f"{pad}{key}:")
            lines.extend(yaml_block(value, indent + 2))
        elif isinstance(value, list):
            lines.append(f"{pad}{key}:")
            for item in value:
                if isinstance(item, dict):
                    nested = yaml_block(item, indent + 4)
                    nested[0] = f"{pad}  - {nested[0].lstrip()}"
                    lines.extend(nested)
                else:
                    lines.append(f"{pad}  - {json.dumps(item, ensure_ascii=False)}")
        elif isinstance(value, (bool, int)):
            lines.append(f"{pad}{key}: {json.dumps(value)}")
        else:
            lines.append(f"{pad}{key}: {json.dumps(str(value), ensure_ascii=False)}")
    return lines


# -------------------------------------------------------------------- conversion


def convert_body(xml_path: Path, template: Path, lua: Path) -> str:
    return run(
        [
            "pandoc",
            "--from=jats",
            f"--to={PANDOC_TO}",
            "--wrap=none",
            "--standalone",
            f"--template={template}",
            f"--lua-filter={lua}",
            str(xml_path),
        ]
    )


def ref_list_titled(root) -> bool:
    """Does the reference list carry its own heading in the source?

    Most do -- "References", "REFERENCES", "Reference" -- and pandoc emits it as a
    header above the empty div. Where the `<ref-list>` has no `<title>`, nothing
    separates the bibliography from the section before it, so one is supplied.
    """
    ref_list = first(root, ".//ref-list")
    return ref_list is not None and bool(text_of(ref_list.find("title")))


def insert_references(body: str, refs: list[str], titled: bool = True) -> tuple[str, bool]:
    """Fill the empty `<div id="refs">` pandoc leaves where the reference list was."""
    if not refs:
        return body, False
    block = "\n\n".join(refs)
    if not titled:
        block = f"## References\n\n{block}"
    # A callable replacement, because citation strings contain backslashes that
    # re.sub would otherwise read as escapes ("\c" raises, "\1" would silently
    # substitute a group).
    replaced = EMPTY_REFS_RE.subn(lambda _: block, body, count=1)
    if replaced[1]:
        return replaced[0], True
    return f"{body.rstrip()}\n\n## References\n\n{block}\n", True


def existing_stamp(path: Path) -> dict[str, str]:
    """The provenance stamp of an already-converted file, from its front matter.

    Read from the Markdown itself rather than from `index.json`, so deleting an
    output file is enough to force it to be rebuilt.
    """
    if not path.exists():
        return {}
    lines = []
    with path.open(encoding="utf-8") as handle:
        if handle.readline().rstrip("\n") != "---":
            return {}
        for line in handle:
            if line.rstrip("\n") == "---":
                break
            lines.append(line)
    head = "".join(lines)
    return {m.group(1): m.group(2).strip('"') for m in STAMP_RE.finditer(head)}


def manifest_provenance(project_dir: Path) -> dict[str, dict]:
    """Provenance per paper file, as recorded by the `fulltext` stage.

    `manifest.json` is the only record of where a held file came from -- the ledger's
    `query` column is a settle key over the whole candidate list, not a source URL.
    """
    path = project_dir / "papers" / "manifest.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    out = {}
    for entry in data.get("entries", []):
        name = entry.get("file")
        if name:
            out[Path(name).name] = entry
    return out


def output_path(project_dir: Path, source: Path, beside: bool) -> Path:
    """Where the Markdown for `source` goes."""
    if beside:
        return source.with_suffix(".md")
    return OUT_DIR / project_dir.name / f"{source.stem}.md"


def convert(
    project_dirs: list[Path], force: bool, pandoc: str, poppler: str, beside: bool
) -> dict:
    documents, skipped, failures = [], 0, []

    with tempfile.TemporaryDirectory() as tmp:
        template = Path(tmp) / "paper.md"
        template.write_text(TEMPLATE, encoding="utf-8")
        lua = Path(tmp) / "demote.lua"
        lua.write_text(LUA_FILTER, encoding="utf-8")

        for project_dir in project_dirs:
            papers = project_dir / "papers"
            if not papers.is_dir():
                continue
            recorded = manifest_provenance(project_dir)

            for source in sorted(papers.glob("*.xml")) + sorted(papers.glob("*.pdf")):
                is_pdf = source.suffix == ".pdf"
                out_path = output_path(project_dir, source, beside)
                digest = hashlib.sha256(source.read_bytes()).hexdigest()
                version = (
                    pdf_markdown.PDF_CONVERTER_VERSION if is_pdf else CONVERTER_VERSION
                )
                tool_key, tool = ("poppler", poppler) if is_pdf else ("pandoc", pandoc)
                stamp = existing_stamp(out_path)
                if (
                    not force
                    and stamp.get("source_sha256") == digest
                    and stamp.get("converter_version") == str(version)
                    and stamp.get(tool_key) == tool
                ):
                    skipped += 1
                    documents.append(index_entry(project_dir, source, out_path, digest))
                    continue

                entry = dict(recorded.get(source.name, {}))
                entry.update(
                    {
                        "project_id": project_dir.name,
                        "source_file": rel(source),
                        "sha256": digest,
                        tool_key: tool,
                    }
                )
                try:
                    if is_pdf:
                        body, stats = pdf_markdown.convert(source, entry.get("title"))
                        meta = pdf_front_matter(entry, stats)
                        has_refs = None
                    else:
                        root = ET.parse(source).getroot()
                        body = convert_body(source, template, lua)
                        body, has_refs = insert_references(
                            body, references(root), ref_list_titled(root)
                        )
                        meta = front_matter(root, entry)
                except (
                    ET.ParseError,
                    subprocess.CalledProcessError,
                    RuntimeError,
                ) as error:
                    detail = getattr(error, "stderr", "") or str(error)
                    failures.append(
                        {
                            "file": rel(source),
                            "error": detail.strip().splitlines()[-1][:200],
                        }
                    )
                    continue

                if is_pdf:
                    # The PDF has no title element; the manifest is the only source.
                    title = entry.get("title")
                    body = f"# {title}\n\n{body.lstrip()}" if title else body.lstrip()
                text = "---\n" + "\n".join(yaml_block(meta)) + "\n---\n\n" + body.lstrip()

                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(text, encoding="utf-8")
                documents.append(
                    index_entry(
                        project_dir, source, out_path, digest, references=has_refs
                    )
                )

    return {"documents": documents, "skipped": skipped, "failures": failures}


def index_entry(
    project_dir: Path, source: Path, out_path: Path, digest: str, references=None
) -> dict:
    entry = {
        "project_id": project_dir.name,
        "source": rel(source),
        "source_format": source.suffix.lstrip("."),
        "markdown": rel(out_path),
        "source_sha256": digest,
        "bytes": out_path.stat().st_size,
    }
    if references is not None:
        entry["references"] = references
    return entry


def main() -> int:
    global OUT_DIR

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("projects", nargs="*", help="project ids; default is all")
    parser.add_argument(
        "--force", action="store_true", help="reconvert even when nothing changed"
    )
    parser.add_argument(
        "--out", type=Path, default=OUT_DIR, help="output directory (default: corpus/)"
    )
    parser.add_argument(
        "--beside",
        action="store_true",
        help="write each Markdown next to its source instead of under --out",
    )
    args = parser.parse_args()
    OUT_DIR = args.out.resolve()

    if args.projects:
        project_dirs = [PROJECTS_DIR / pid for pid in sorted(set(args.projects))]
        missing = [d.name for d in project_dirs if not d.is_dir()]
        if missing:
            return f"no such project: {', '.join(missing)}"
    else:
        project_dirs = sorted(d for d in PROJECTS_DIR.iterdir() if d.is_dir())

    pandoc = pandoc_version()
    poppler = pdf_markdown.poppler_version()
    result = convert(project_dirs, args.force, pandoc, poppler, args.beside)

    documents = sorted(result["documents"], key=lambda d: (d["project_id"], d["source"]))
    # In --beside mode the outputs are scattered across the project tree and each one
    # carries its own provenance in its front matter, so there is nowhere an index
    # would belong and nothing it would be the only record of.
    if not args.beside:
        index = {
            "converter_version": CONVERTER_VERSION,
            "pdf_converter_version": pdf_markdown.PDF_CONVERTER_VERSION,
            "pandoc": pandoc,
            "poppler": poppler,
            "format": PANDOC_TO,
            "documents": documents,
        }
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / "index.json").write_text(
            json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    written = len(documents) - result["skipped"]
    total = sum(d["bytes"] for d in documents)
    pdfs = sum(1 for d in documents if d["source_format"] == "pdf")
    print(
        f"{len(documents)} documents ({written} written, {result['skipped']} unchanged), "
        f"{len(documents) - pdfs} from XML, {pdfs} from PDF, {total / 1_000_000:.1f} MB"
    )
    without_refs = [d for d in documents if d.get("references") is False]
    if without_refs:
        print(f"{len(without_refs)} without a reference list")
    for failure in result["failures"]:
        print(f"FAILED {failure['file']}: {failure['error']}", file=sys.stderr)
    return 1 if result["failures"] else 0


if __name__ == "__main__":
    sys.exit(main())

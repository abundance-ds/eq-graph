#!/usr/bin/env python3
"""Prepare verified scale full texts for semantic assessment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
PIPELINE = ROOT / "pipeline"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(PIPELINE))

import pdf_markdown  # noqa: E402
import to_markdown  # noqa: E402
from jats_metadata import parse_jats  # noqa: E402
from scale_publication_metadata import load_publications  # noqa: E402


PREPARATION_VERSION = 1
DEFAULT_RESULTS = ROOT / "scale/protocol-2.0/fulltext-retrieval-v2/RESULTS.tsv"
DEFAULT_OUTPUT = ROOT / "scale/protocol-2.0/fulltext-preparation-v2"
DEFAULT_CORPUS = ROOT / "scale/protocol-2.0/article-corpus.jsonl"
DEFAULT_CANONICAL = ROOT / "scale/protocol-2.0/source-union.jsonl"
YEAR_OVERRIDES = ROOT / "pipeline/data/publication_year_overrides.tsv"
EMPTY_REFS_RE = re.compile(r'<div id="refs">\s*</div>')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def apply_year_overrides(publications: dict[str, dict[str, Any]]) -> None:
    with YEAR_OVERRIDES.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            record = publications.get(row["record_id"])
            if record is not None and not isinstance(record.get("year"), int):
                record["year"] = int(row["year"])
                record["year_source"] = "reviewed_override"


def pdf_metadata(row: dict[str, str], publication: dict[str, Any]) -> dict[str, Any]:
    """Use discovery metadata when the source has no structured JATS metadata."""
    return {
        "publication": {
            "publication_id": f"doi:{row['doi'].casefold()}" if row["doi"] else row["record_id"],
            "record_id": row["record_id"],
            "doi": row["doi"] or publication.get("doi"),
            "pmid": row["pmid"] or publication.get("pmid"),
            "title": row["title"],
            "year": int(row["year"]) if row["year"].isdigit() else publication.get("year"),
            "journal": publication.get("venue"),
            "document_types": publication.get("document_types", []),
            "canonical_url": row["doi_url"] or row["landing_url"],
            "metadata_status": "bibliographic_metadata_only",
        },
        "authors": publication.get("authors", []),
        "funders": publication.get("funders", []),
        "euroqol_award_ids": publication.get("euroqol_award_ids", []),
        "references": [],
        "metadata_note": (
            "The PDF has no trusted structured metadata layer. These fields come "
            "from the canonical discovery record. References are not reconstructed."
        ),
    }


def convert_pdf_for_preparation(pdf: Path, title: str) -> tuple[str, dict[str, Any]]:
    """Use the approved converter, with Poppler only after a strict glyph failure."""
    try:
        body, stats = pdf_markdown.convert(pdf, title)
        stats["fallback_parser"] = None
        stats["unreadable_glyph_markers"] = 0
        return body, stats
    except RuntimeError as exc:
        if not any(
            marker in str(exc)
            for marker in ("replacement character", "unhandled detached accent")
        ):
            raise
    completed = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        check=True,
        capture_output=True,
    )
    raw = completed.stdout.decode("utf-8", errors="replace").replace("\r\n", "\n")
    pages = raw.split("\f")
    unreadable = raw.count("\ufffd")
    control_re = re.compile(r"[\x00-\x08\x0b\x0e-\x1f\x7f]")
    unreadable += len(control_re.findall(raw))
    rendered_pages = []
    for number, page in enumerate(pages, 1):
        page = control_re.sub("[unreadable glyph]", page)
        page = page.replace("\ufffd", "[unreadable glyph]").strip()
        if page:
            rendered_pages.append(f"<!-- source-page: {number} -->\n\n{page}")
    body = "\n\n".join(rendered_pages).rstrip() + "\n"
    if len(body.strip()) < 500:
        raise RuntimeError("the Poppler fallback returned too little text")
    stats = {
        "source_pages": len([page for page in pages if page.strip()]),
        "pages": len(rendered_pages),
        "cover_sheet_pages_dropped": 0,
        "font_objects_repaired": 0,
        "font_codes_repaired": 0,
        "tables": 0,
        "headings": 0,
        "formulas": 0,
        "unread_formulas": 0,
        "replacement_characters": 0,
        "unreadable_glyph_markers": unreadable,
        "fallback_parser": "pdftotext-layout",
    }
    return body, stats


def tool_fingerprint(source_format: str) -> str:
    paths: list[Path] = []
    versions = [f"preparation:{PREPARATION_VERSION}"]
    if source_format == "xml":
        paths.extend((SCRIPTS / "to_markdown.py", PIPELINE / "jats_metadata.py"))
        versions.append(f"pandoc:{to_markdown.pandoc_version()}")
    else:
        paths.append(SCRIPTS / "pdf_markdown.py")
        versions.extend(
            (
                f"pdf_markdown:{pdf_markdown.PDF_CONVERTER_VERSION}",
                pdf_markdown.parser_version(),
            )
        )
    material = "\n".join(versions + [digest(path) for path in paths])
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def existing_result(
    row: dict[str, str], output: Path, fingerprint: str
) -> dict[str, str] | None:
    state_path = output / "state" / f"{row['record_id']}.json"
    if not state_path.is_file():
        return None
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        result = state["manifest_row"]
        markdown = ROOT / result["markdown_path"]
        metadata = ROOT / result["metadata_path"]
        if (
            state["source_sha256"] == row["sha256"]
            and state["tool_fingerprint"] == fingerprint
            and markdown.is_file()
            and metadata.is_file()
            and digest(markdown) == result["markdown_sha256"]
            and digest(metadata) == result["metadata_sha256"]
        ):
            return result
    except (KeyError, ValueError, json.JSONDecodeError):
        return None
    return None


def prepare_one(
    row: dict[str, str],
    publication: dict[str, Any],
    output: Path,
    template: Path,
    lua: Path,
    fingerprints: dict[str, str],
    force: bool,
) -> tuple[dict[str, str], bool]:
    source_format = row["format"].casefold()
    if source_format not in {"xml", "pdf"}:
        raise ValueError(f"Unsupported source format: {source_format}")
    fingerprint = fingerprints[source_format]
    if not force:
        prior = existing_result(row, output, fingerprint)
        if prior is not None:
            return prior, True

    source = ROOT / row["source_path"]
    if not source.is_file():
        raise ValueError(f"Missing source: {source}")
    if source.stat().st_size != int(row["bytes"]) or digest(source) != row["sha256"]:
        raise ValueError("Source byte or SHA-256 verification failed.")

    if source_format == "xml":
        metadata = parse_jats(source)
        metadata["publication"]["source_path"] = relative(source)
        metadata["publication"]["record_id"] = row["record_id"]
        metadata["publication"]["retrieval_doi"] = row["doi"]
        source_doi = str(metadata["publication"].get("doi") or "").casefold()
        metadata["publication"]["doi_matches_retrieval_record"] = source_doi == row["doi"].casefold()
        body = to_markdown.convert_body(source, template, lua)
        text = EMPTY_REFS_RE.sub("", body).strip() + "\n"
        stats = {
            "headings": len(re.findall(r"^#{1,6} ", text, re.MULTILINE)),
            "structured_references": len(metadata.get("references", [])),
            "bibliography_in_ai_text": False,
        }
        converter = f"jats-pandoc:{to_markdown.pandoc_version()}"
    else:
        metadata = pdf_metadata(row, publication)
        body, stats = convert_pdf_for_preparation(source, row["title"])
        text = f"# {row['title']}\n\n{body.lstrip()}".rstrip() + "\n"
        stats["bibliography_in_ai_text"] = True
        converter = (
            f"pdf_markdown:{pdf_markdown.PDF_CONVERTER_VERSION};"
            f"{pdf_markdown.parser_version()}"
        )
        if stats.get("fallback_parser"):
            converter += f";fallback:{stats['fallback_parser']}"

    if len(text.strip()) < 500:
        raise ValueError("Prepared Markdown is shorter than 500 characters.")
    if "\ufffd" in text:
        raise ValueError("Prepared Markdown contains Unicode replacement characters.")

    markdown_path = output / "markdown" / f"{row['record_id']}.md"
    metadata_path = output / "metadata" / f"{row['record_id']}.json"
    markdown_path.write_text(text, encoding="utf-8")
    metadata_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    result = {
        "record_id": row["record_id"],
        "source_format": source_format,
        "source_method": row["source_method"],
        "source_url": row["source_url"],
        "source_path": relative(source),
        "source_sha256": row["sha256"],
        "source_bytes": row["bytes"],
        "identity_method": row["identity_method"],
        "identity_reason": row["identity_reason"],
        "markdown_path": relative(markdown_path),
        "markdown_sha256": digest(markdown_path),
        "markdown_bytes": str(markdown_path.stat().st_size),
        "metadata_path": relative(metadata_path),
        "metadata_sha256": digest(metadata_path),
        "converter": converter,
        "tool_fingerprint": fingerprint,
        "stats_json": json.dumps(stats, ensure_ascii=False, separators=(",", ":")),
    }
    state_path = output / "state" / f"{row['record_id']}.json"
    state_path.write_text(
        json.dumps(
            {
                "source_sha256": row["sha256"],
                "tool_fingerprint": fingerprint,
                "manifest_row": result,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return result, False


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--canonical-metadata", type=Path, default=DEFAULT_CANONICAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.workers < 1:
        raise ValueError("--workers must be at least 1.")
    rows = [row for row in read_tsv(args.results) if row["status"] == "VERIFIED"]
    publications = load_publications(args.corpus, args.canonical_metadata)
    apply_year_overrides(publications)
    missing = sorted({row["record_id"] for row in rows} - publications.keys())
    if missing:
        raise ValueError(f"Missing publication metadata: {', '.join(missing[:5])}")

    for folder in ("markdown", "metadata", "state"):
        (args.output / folder).mkdir(parents=True, exist_ok=True)
    fingerprints = {kind: tool_fingerprint(kind) for kind in ("xml", "pdf")}
    completed: dict[str, dict[str, str]] = {}
    failures: list[dict[str, str]] = []
    reused = 0

    with tempfile.TemporaryDirectory() as temporary:
        template = Path(temporary) / "paper.md"
        template.write_text(to_markdown.TEMPLATE, encoding="utf-8")
        lua = Path(temporary) / "demote.lua"
        lua.write_text(to_markdown.LUA_FILTER, encoding="utf-8")
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    prepare_one,
                    row,
                    publications[row["record_id"]],
                    args.output,
                    template,
                    lua,
                    fingerprints,
                    args.force,
                ): row
                for row in rows
            }
            for index, future in enumerate(as_completed(futures), 1):
                row = futures[future]
                try:
                    result, was_reused = future.result()
                    completed[row["record_id"]] = result
                    reused += int(was_reused)
                except Exception as exc:
                    failures.append(
                        {
                            "record_id": row["record_id"],
                            "source_path": row["source_path"],
                            "source_sha256": row["sha256"],
                            "error": f"{type(exc).__name__}: {str(exc)[:500]}",
                        }
                    )
                if index % 100 == 0 or index == len(rows):
                    print(f"processed={index}/{len(rows)} failures={len(failures)}", flush=True)

    ordered = [completed[row["record_id"]] for row in rows if row["record_id"] in completed]
    manifest = args.output / "MANIFEST.tsv"
    fields = list(ordered[0]) if ordered else ["record_id"]
    write_tsv(manifest, ordered, fields)
    write_tsv(
        args.output / "FAILURES.tsv",
        sorted(failures, key=lambda item: item["record_id"]),
        ["record_id", "source_path", "source_sha256", "error"],
    )
    summary = {
        "preparation_version": PREPARATION_VERSION,
        "verified_sources": len(rows),
        "prepared": len(ordered),
        "reused": reused,
        "failed": len(failures),
        "formats": {
            kind: sum(item["source_format"] == kind for item in ordered)
            for kind in ("xml", "pdf")
        },
        "manifest_sha256": digest(manifest),
        "boundary": (
            "Markdown is the AI reading copy. The verified PDF or JATS file is the "
            "source of record. Structured JATS metadata and references stay outside "
            "the AI text. PDF references remain in the reading copy but the semantic "
            "agent must not reconstruct them."
        ),
    }
    (args.output / "SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit("One or more full texts failed preparation.")


if __name__ == "__main__":
    main()

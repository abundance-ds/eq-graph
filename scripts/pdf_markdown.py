#!/usr/bin/env python3
"""Convert a publisher PDF to Markdown, for the papers held only as PDF.

Pandoc has no PDF reader, so this uses poppler. Not `pdftotext`, though: its output
is already-flattened text, and two things this corpus needs are only recoverable
while the font of each glyph is still known.

**The symbol font.** Elsevier's Value in Health PDFs draw −, <, >, ≥ and ≤ from a
separate Mathematical Pi font whose glyphs carry no usable ToUnicode mapping, so
every text extractor reads them as `2`, `,`, `.`, `$` and `#`. "Values ranged from
−0.654" comes out as "from 20.654", and `P < .001` as `P , .001` -- silent, and
exactly the kind of damage that survives into an extracted fact. The substitution is
fixed per font, so it is repaired by font identity rather than by guessing at
context: only glyphs actually drawn from those fonts are touched, and a real `2`
elsewhere on the line is left alone. See SYMBOL_FONTS.

**The headings.** Section structure survives in this layout only as a font size --
there is no other marker -- so heading levels are assigned by ranking the sizes that
sit above the body size.

`pdftohtml -xml` keeps both, and its runs come out already in reading order, columns
included, so this reassembles lines from those runs rather than re-deriving layout.

Multi-column pages, running heads and hyphenation across line breaks are handled;
tables are not. A table's cells arrive as ordinary positioned runs with nothing to
mark them apart, so they land in the output as loose lines in reading order.
"""

from __future__ import annotations

import collections
import re
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

# Bump when a change here alters the Markdown produced.
PDF_CONVERTER_VERSION = 1

# Glyphs whose meaning is knowable from the font they were drawn with, because the
# embedded font maps them to nothing usable. Keyed by the stable part of the family
# name -- poppler prefixes a random per-file subset tag ("RGDYHB+AdvOT8817665d").
#
# Confirmed against the surrounding prose in all seven Value in Health PDFs held
# here: "censored at ⟦2⟧1.0", "P⟦,⟧.001", "eigenvalue⟦.⟧1 were retained",
# "correlations ⟦$⟧0.5", "benchmark values: ⟦#⟧0.32 (unacceptable)".
SYMBOL_FONTS = {
    "AdvOT8817665d": {"2": "−", ",": "<", ".": ">", "$": "≥", "#": "≤"},
    "MathematicalPi-One": {
        "2": "−", ",": "<", ".": ">", "$": "≥", "#": "≤",
    },
    # Elsevier's inline-formula font: "310 ¼ 0:" is "310 = 0.".
    "AdvP4C4E74": {"\xbc": "=", "\xf0": "(", "\xde": ")", ":": "."},
    "AdvPSSym": {"\xaa": "©"},
    "PSSymbol": {"\xaa": "©"},
}

# A line this far into the top or bottom of the page is a running head or foot, not
# body text -- but only if it also repeats across pages (REPEAT_PAGES).
MARGIN_BAND = 0.07
REPEAT_PAGES = 3

# A line ending this far short of its column's right edge ends a paragraph.
RAGGED_RIGHT = 14
# A line starting this far right of its column's left edge is an indented first line.
INDENT = 5

WORD_RE = re.compile(r"[A-Za-zÀ-ɏ][\wÀ-ɏ'’-]*")
HYPHEN_BREAK_RE = re.compile(r"(\S*\w)-$")


def run_pdftohtml(pdf: Path, out: Path) -> None:
    """`-i` drops images, `-hidden` keeps the text layer of scanned-then-OCRed pages."""
    proc = subprocess.run(
        ["pdftohtml", "-xml", "-i", "-hidden", "-nodrm", str(pdf), str(out)],
        capture_output=True,
        text=True,
    )
    if not out.exists():
        raise RuntimeError(
            (proc.stderr or proc.stdout or "pdftohtml produced no output").strip()
        )


def poppler_version() -> str:
    try:
        proc = subprocess.run(
            ["pdftohtml", "-v"], capture_output=True, text=True, check=False
        )
    except FileNotFoundError:
        sys.exit(
            "pdftohtml not found. Install poppler (brew install poppler) and rerun; "
            "this module is a wrapper around it."
        )
    text = (proc.stderr or "") + (proc.stdout or "")
    match = re.search(r"version\s+([\d.]+)", text)
    return match.group(1) if match else "unknown"


def repair(text: str, family: str) -> str:
    for stable, table in SYMBOL_FONTS.items():
        if stable in family:
            return "".join(table.get(char, char) for char in text)
    return text


# ------------------------------------------------------------------------- layout


def read_pages(xml_path: Path) -> list[dict]:
    """Runs per page, with the font resolved and its broken glyphs repaired.

    `<fontspec>` ids are assigned once and reused by later pages, so the table has to
    accumulate across the document rather than reset per page.
    """
    root = ET.parse(xml_path).getroot()
    fonts: dict[str, tuple[float, str]] = {}
    pages = []
    for page in root.findall("page"):
        for spec in page.findall("fontspec"):
            try:
                size = float(spec.get("size") or 0)
            except ValueError:
                size = 0.0
            fonts[spec.get("id")] = (size, spec.get("family") or "")
        runs = []
        for element in page.findall("text"):
            size, family = fonts.get(element.get("font"), (0.0, ""))
            text = repair("".join(element.itertext()), family)
            if not text.strip():
                continue
            runs.append(
                {
                    "top": int(element.get("top") or 0),
                    "left": int(element.get("left") or 0),
                    "width": int(element.get("width") or 0),
                    "height": int(element.get("height") or 0),
                    "size": size,
                    "family": family,
                    "text": text,
                }
            )
        pages.append(
            {
                "number": int(page.get("number") or 0),
                "width": int(page.get("width") or 0),
                "height": int(page.get("height") or 0),
                "runs": runs,
            }
        )
    return pages


def drop_cover_sheets(pages: list[dict]) -> tuple[list[dict], int]:
    """Discard the deposit banner a repository staples in front of the article.

    White Rose and Erasmus both prepend one, and it is not part of the paper: it
    restates the citation and the licence in the repository's own house font. That
    font is the signal -- the sheet was typeset by different software, so it shares
    no font family with the article, which is what separates it from a genuine first
    page. Only leading pages are considered, so a body page that happens to be
    typographically odd is safe.
    """
    weights: collections.Counter = collections.Counter()
    for page in pages:
        for run in page["runs"]:
            weights[run["family"].split("+")[-1]] += len(run["text"])
    if not weights:
        return pages, 0
    dominant = weights.most_common(1)[0][0]

    index = 0
    while index < len(pages) - 1:
        families = {run["family"].split("+")[-1] for run in pages[index]["runs"]}
        if dominant in families:
            break
        index += 1
    return pages[index:], index


def assemble_lines(page: dict) -> list[dict]:
    """Merge runs sharing a baseline into lines, keeping poppler's reading order.

    A line is broken by a vertical step or by a run that starts back to the left of
    where the previous one did, which is what a column or paragraph change looks
    like. Superscript citation markers sit a couple of pixels high and stay on the
    line they annotate, which is where they belong: "similar construct.9 However".
    """
    groups: list[dict] = []
    for run in page["runs"]:
        if groups:
            current = groups[-1]
            aligned = abs(run["top"] - current["top"]) <= max(3, 0.45 * current["height"])
            forward = run["left"] >= current["runs"][-1]["left"] - 2
            if aligned and forward:
                current["runs"].append(run)
                current["top"] = min(current["top"], run["top"])
                continue
        groups.append({"top": run["top"], "height": run["height"], "runs": [run]})

    lines = []
    for group in groups:
        parts: list[str] = []
        previous_end = None
        for run in group["runs"]:
            if previous_end is not None and run["left"] - previous_end > 1.5:
                parts.append(" ")
            parts.append(run["text"])
            previous_end = run["left"] + run["width"]
        # NFKC folds the ﬁ/ﬂ ligatures the fonts emit as single code points.
        text = unicodedata.normalize("NFKC", "".join(parts))
        text = re.sub(r"[ \t]+", " ", text).strip()
        if not text:
            continue

        weights: collections.Counter = collections.Counter()
        for run in group["runs"]:
            weights[run["size"]] += len(run["text"])
        size = weights.most_common(1)[0][0]
        first, last = group["runs"][0], group["runs"][-1]
        lines.append(
            {
                "text": text,
                "page": page["number"],
                "top": group["top"],
                "left": first["left"],
                "right": last["left"] + last["width"],
                "size": size,
                "column": 0 if first["left"] < page["width"] / 2 else 1,
                "page_height": page["height"],
            }
        )
    return lines


def drop_running_heads(lines: list[dict]) -> tuple[list[dict], int]:
    """Remove the journal furniture that repeats in the margins of every page.

    Repetition alone would take out a recurring table header; the margin band alone
    would take out the first heading on a page. Both together is what a running head
    is. Bare page numbers are dropped on the margin test alone -- they never repeat,
    being different on every page.
    """
    pages_by_text: dict[str, set[int]] = collections.defaultdict(set)
    for line in lines:
        pages_by_text[line["text"].strip().lower()].add(line["page"])

    kept, dropped = [], 0
    for line in lines:
        height = line["page_height"] or 1
        in_margin = (
            line["top"] < MARGIN_BAND * height
            or line["top"] > (1 - MARGIN_BAND) * height
        )
        repeats = len(pages_by_text[line["text"].strip().lower()]) >= REPEAT_PAGES
        # Folio marks, and not only digits: Value in Health draws its page numbers
        # from a font that resolves to nothing, so they arrive as a bare "-".
        stripped = line["text"].strip()
        folio = len(stripped) <= 8 and not any(char.isalpha() for char in stripped)
        if in_margin and (repeats or folio):
            dropped += 1
            continue
        kept.append(line)
    return kept, dropped


LEFT_BUCKET = 8


def measure_block(line: dict) -> tuple[int, int, int]:
    """The text block a line belongs to, for the purpose of measuring its width.

    Page and column are not enough. An article's first page runs a full-width
    abstract above a two-column body, so both share a column while ending in
    different places; keying on where the line starts as well separates them.
    """
    return (line["page"], line["column"], line["left"] // LEFT_BUCKET)


def column_extents(lines: list[dict]) -> dict[tuple[int, int, int], int]:
    """The right edge a full-width line reaches, per block.

    The most common edge, not the widest: body text is justified, so the modal edge
    is the block's own, and the occasional line that overshoots it -- or a footer
    spanning the whole page -- does not drag it out.
    """
    edges: dict[tuple[int, int, int], collections.Counter] = collections.defaultdict(
        collections.Counter
    )
    for line in lines:
        edges[measure_block(line)][line["right"]] += 1
    return {key: counter.most_common(1)[0][0] for key, counter in edges.items()}


# ----------------------------------------------------------------------- headings


def body_size(lines: list[dict]) -> float:
    weights: collections.Counter = collections.Counter()
    for line in lines:
        weights[line["size"]] += len(line["text"])
    return weights.most_common(1)[0][0] if weights else 0.0


def heading_levels(lines: list[dict], body: float) -> dict[float, int]:
    """Font sizes above the body size, ranked into heading levels.

    Sizes carrying almost no text are decoration -- a drop cap, a masthead rule --
    and would otherwise claim the top level and push the real headings down.
    """
    weights: collections.Counter = collections.Counter()
    for line in lines:
        if line["size"] > body:
            weights[line["size"]] += len(line["text"])
    sizes = sorted((s for s, n in weights.items() if n >= 25), reverse=True)
    # h1 is the article title, supplied from the manifest, so these start at h2.
    return {size: min(index + 2, 6) for index, size in enumerate(sizes)}


# ------------------------------------------------------------------- de-hyphenation


def vocabulary(lines: list[dict]) -> set[str]:
    words = set()
    for line in lines:
        for match in WORD_RE.finditer(line["text"]):
            words.add(match.group(0).lower())
    return words


def join_hyphenated(head: str, tail: str, vocab: set[str]) -> str:
    """Join a word broken across two lines, deciding whether its hyphen was real.

    "compara-" + "bility" is one word; "EQ-5D-" + "5L" and "long-" + "term" are two
    with a hyphen of their own. The document is its own dictionary: whichever form
    occurs elsewhere in the paper wins, and only when neither does is the shape of
    the fragments used -- keeping the hyphen unless both sides are plainly lowercase
    prose, because a wrongly kept hyphen is a wart while a wrongly dropped one
    rewrites an instrument's name.
    """
    match = HYPHEN_BREAK_RE.search(head)
    if not match:
        return f"{head} {tail}"
    stem = match.group(1)
    following = WORD_RE.match(tail)
    if not following:
        return f"{head} {tail}"
    word = following.group(0)

    hyphenated = f"{stem}-{word}".lower()
    fused = f"{stem}{word}".lower()
    if hyphenated in vocab:
        keep = True
    elif fused in vocab:
        keep = False
    else:
        keep = not (stem[-1:].islower() and word[:1].islower())
    # `head` still carries the trailing hyphen, so keeping it is a plain join.
    return head + tail if keep else head[:-1] + tail


# ---------------------------------------------------------------------- conversion


def to_blocks(lines: list[dict], body: float, levels: dict[float, int]) -> list[str]:
    """Group lines into headings and reflowed paragraphs.

    A paragraph ends where the layout says it does: a heading, a change of column or
    page, a change of font size, a line that stops short of the column's right edge,
    or a line indented past it.
    """
    extents = column_extents(lines)
    vocab = vocabulary(lines)

    blocks: list[str] = []
    paragraph: list[dict] = []

    def flush() -> None:
        if not paragraph:
            return
        text = paragraph[0]["text"]
        for line in paragraph[1:]:
            text = join_hyphenated(text, line["text"], vocab)
        blocks.append(text)
        paragraph.clear()

    for line in lines:
        # Size alone, never boldness. Bold at body size does mark the odd real
        # subheading, but it also marks every column header in every table, and in
        # this corpus that is the overwhelming majority: 216 of the 218 lines the
        # boldness test caught were table headers, arriving as a run of one-word
        # "headings" where a table should be.
        level = levels.get(line["size"]) if line["size"] > body else None
        if level is not None:
            flush()
            blocks.append("#" * level + " " + line["text"])
            continue

        if paragraph:
            previous = paragraph[-1]
            edge = extents.get(measure_block(previous), previous["right"])
            # Deliberately not broken by a column or page change: body text flows
            # across both, and a paragraph that really does end at the foot of a
            # column leaves its last line short, which the ragged-right test catches.
            broke = (
                line["size"] != previous["size"]
                or previous["right"] < edge - RAGGED_RIGHT
                or line["left"] > previous["left"] + INDENT
            )
            if broke:
                flush()
        paragraph.append(line)
    flush()
    return blocks


def normalise(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


# How far into the document the drawn title can still be. Masthead, article type
# and the title itself; the abstract follows well inside this.
TITLE_WINDOW = 12


def drop_title_headings(blocks: list[str], title: str | None) -> list[str]:
    """Remove the headings that restate the article title.

    The caller writes the title as the `#` of the document, taken from the manifest,
    and the page draws it too -- usually across two lines, so it arrives as two
    headings that would otherwise sit directly under it saying the same thing. Only
    the opening blocks are considered, so a later section whose name happens to
    appear in the title survives.
    """
    if not title:
        return blocks
    wanted = normalise(title)
    out = []
    for index, block in enumerate(blocks):
        if index < TITLE_WINDOW and block.startswith("#"):
            body = normalise(block.lstrip("# "))
            if body and body in wanted:
                continue
        out.append(block)
    return out


def convert(pdf: Path, title: str | None = None) -> tuple[str, dict]:
    """Markdown body for `pdf`, plus what the conversion had to decide or discard."""
    with tempfile.TemporaryDirectory() as tmp:
        xml_path = Path(tmp) / "paper.xml"
        run_pdftohtml(pdf, xml_path)
        pages = read_pages(xml_path)

    pages, cover_pages = drop_cover_sheets(pages)
    lines = [line for page in pages for line in assemble_lines(page)]
    if not lines:
        raise RuntimeError("no text layer: the PDF holds page images only")

    lines, dropped = drop_running_heads(lines)
    body = body_size(lines)
    levels = heading_levels(lines, body)
    blocks = drop_title_headings(to_blocks(lines, body, levels), title)

    repaired = sum(
        1
        for page in pages
        for run in page["runs"]
        if any(stable in run["family"] for stable in SYMBOL_FONTS)
    )
    stats = {
        "pages": len(pages),
        "lines": len(lines),
        "blocks": len(blocks),
        "cover_sheet_pages_dropped": cover_pages,
        "running_heads_dropped": dropped,
        "symbol_runs_repaired": repaired,
        "body_font_size": body,
        "heading_sizes": sorted(levels, reverse=True),
    }
    return "\n\n".join(blocks) + "\n", stats


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    text, stats = convert(args.pdf)
    print(text)
    print(stats, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

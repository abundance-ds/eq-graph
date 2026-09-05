#!/usr/bin/env python3
"""Repair known PDF font maps, then convert the PDF to structured Markdown.

Some publisher PDFs have correct visible glyphs but incorrect or missing
``/ToUnicode`` maps. A normal parser then reads comparison signs as digits or
punctuation. This module repairs the verified font maps in a temporary PDF before
PyMuPDF4LLM reads it. The repair does not change page content or page geometry.

PyMuPDF4LLM then makes one structural pass. It supplies headings, reading order,
and Markdown tables from the same repaired text. There is no second table view to
merge and no numerical output from another parser.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import sys
import tempfile
import unicodedata
from pathlib import Path

import pikepdf
import pymupdf
import pymupdf4llm

# Bump this value when a change alters the Markdown.
PDF_CONVERTER_VERSION = 3

# These mappings come from visible source checks in this corpus. Use a stable font
# family and a glyph name when the PDF supplies one. Use a raw code only when the
# font has no useful glyph name and the code has a stable meaning in that family.
CODE_REPAIRS: dict[str, dict[int, str]] = {
    "AdvOT8817665d": {
        0x23: "≤",
        0x24: "≥",
        0x2C: "<",
        0x2E: ">",
        0x32: "−",
    },
    # This formula font uses a colon code to draw a full stop.
    "AdvP4C4E74": {0x3A: "."},
    "AdvP41CBCA": {0x31: "ł"},
    "AdvPSSym": {0xAA: "©"},
    "PSSymbol": {0xAA: "©"},
    "AdvPSMP4": {0x5C: "<"},
    # The accent is a separate positioned glyph before the letter c. Keep a private
    # marker until the layout pass has joined the glyphs.
    "TeX_CM_Roman": {0x14: "\uE000"},
}

GLYPH_REPAIRS: dict[str, dict[str, str]] = {
    "AdvP4C4E74": {
        "/C0": "−",
        "/C15": "•",
        "/C20": "≤",
        "/C21": "≥",
        "/C138": "]",
        "/onequarter": "=",
        "/Thorn": ")",
        "/eth": "(",
    },
    "AdvP4C4E46": {
        "/C16": "(",
        "/C17": ")",
        "/C18": "(",
        "/C19": ")",
        "/X": "∑",
    },
    "AdvP4C4E59": {"/C19": "\uE000"},
    "AdvMacMthSyN": {"/C15": "•"},
    "AdvPSSym": {"/C211": "©"},
    "Calibri-Bold": {
        "/g415": "t",
        "/g332": "f",
    },
    "Calibri": {
        "/g415": "ti",
        "/g427": "tti",
        "/g425": "tt",
        "/g332": "f",
    },
    "MathematicalPi-One": {
        "/H11002": "−",
        "/H11021": "<",
        "/H11022": ">",
        "/H11349": "≤",
        "/H11350": "≥",
    },
    "SymbolMT": {
        "/g11": "(",
        "/g12": ")",
        "/g13": "*",
        "/g14": "+",
        "/g16": "−",
        "/g32": "=",
        "/g69": "β",
        "/g72": "ε",
        "/g74": "γ",
        "/g80": "μ",
        "/g86": "σ",
        "/g120": "•",
    },
}

COVER_SHEET_MARKERS = {
    "eur research information portal",
    "white rose research online",
}

DETACHED_ACUTE = "\uE000"
INVISIBLE_GLYPH = "\uE001"
TABLE_RULE_RE = re.compile(r"^\|(?:\s*:?-+:?\s*\|)+\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+")
TITLE_WINDOW = 40


def parser_version() -> str:
    """Return the two tool versions that determine PDF output."""
    return f"pymupdf4llm {pymupdf4llm.__version__}; pikepdf {pikepdf.__version__}"


def stable_family(font: pikepdf.Object) -> str | None:
    """Get the verified family name without the per-file subset prefix."""
    base = str(font.get("/BaseFont", ""))
    families = set(CODE_REPAIRS) | set(GLYPH_REPAIRS)
    for family in sorted(families, key=len, reverse=True):
        if family in base:
            return family
    return None


def encoding_differences(font: pikepdf.Object) -> dict[int, str]:
    """Read the code-to-glyph-name entries from a simple PDF font."""
    encoding = font.get("/Encoding")
    if not isinstance(encoding, pikepdf.Dictionary):
        return {}

    differences: dict[int, str] = {}
    code: int | None = None
    for item in encoding.get("/Differences", []):
        if isinstance(item, int):
            code = item
        elif code is not None:
            differences[code] = str(item)
            code += 1
    return differences


def _unicode_target(value: str) -> str | None:
    """Decode one hexadecimal UTF-16BE target from a ToUnicode CMap."""
    if len(value) % 2:
        return None
    try:
        return bytes.fromhex(value).decode("utf-16-be")
    except (UnicodeDecodeError, ValueError):
        return None


def existing_mapping(font: pikepdf.Object) -> dict[int, str]:
    """Read bfchar and bfrange entries from an existing ToUnicode CMap."""
    stream = font.get("/ToUnicode")
    if not isinstance(stream, pikepdf.Stream):
        return {}

    source = stream.read_bytes().decode("latin1", errors="replace")
    mapping: dict[int, str] = {}

    for block in re.findall(r"beginbfchar(.*?)endbfchar", source, re.S):
        for raw_code, raw_target in re.findall(
            r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block
        ):
            target = _unicode_target(raw_target)
            if target is not None:
                mapping[int(raw_code, 16)] = target

    for block in re.findall(r"beginbfrange(.*?)endbfrange", source, re.S):
        entries = re.findall(
            r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*"
            r"(\[(?:\s*<[0-9A-Fa-f]+>\s*)+\]|<[0-9A-Fa-f]+>)",
            block,
            re.S,
        )
        for raw_first, raw_last, raw_targets in entries:
            first = int(raw_first, 16)
            last = int(raw_last, 16)
            if raw_targets.startswith("["):
                targets = re.findall(r"<([0-9A-Fa-f]+)>", raw_targets)
                for code, raw_target in zip(range(first, last + 1), targets):
                    target = _unicode_target(raw_target)
                    if target is not None:
                        mapping[code] = target
                continue

            raw_target = raw_targets[1:-1]
            base = int(raw_target, 16)
            width = len(raw_target)
            for offset, code in enumerate(range(first, last + 1)):
                encoded = f"{base + offset:0{width}X}"
                if len(encoded) != width:
                    continue
                target = _unicode_target(encoded)
                if target is not None:
                    mapping[code] = target

    return mapping


def font_code_width(font: pikepdf.Object) -> int:
    """Get the byte width of one character code in this font."""
    if str(font.get("/Subtype", "")) != "/Type0":
        return 1
    stream = font.get("/ToUnicode")
    if isinstance(stream, pikepdf.Stream):
        source = stream.read_bytes().decode("latin1", errors="replace")
        match = re.search(
            r"begincodespacerange\s*<([0-9A-Fa-f]+)>", source, re.S
        )
        if match:
            return max(1, len(match.group(1)) // 2)
    return 2


def build_tounicode(
    mapping: dict[int, str], name: str, code_width: int = 1
) -> bytes:
    """Build a ToUnicode CMap with one fixed source-code width."""
    source_width = code_width * 2
    entries = [
        f"<{code:0{source_width}X}> <{value.encode('utf-16-be').hex().upper()}>"
        for code, value in sorted(mapping.items())
    ]
    blocks: list[str] = []
    for start in range(0, len(entries), 100):
        group = entries[start : start + 100]
        blocks.extend([f"{len(group)} beginbfchar", *group, "endbfchar"])

    lines = [
        "/CIDInit /ProcSet findresource begin",
        "12 dict begin",
        "begincmap",
        f"/CMapName /{name} def",
        "/CMapType 2 def",
        "1 begincodespacerange",
        f"<{0:0{source_width}X}> <{(1 << (8 * code_width)) - 1:0{source_width}X}>",
        "endcodespacerange",
        *blocks,
        "endcmap",
        "CMapName currentdict /CMap defineresource pop",
        "end",
        "end",
        "",
    ]
    return "\n".join(lines).encode("ascii")


def repairs_for_font(font: pikepdf.Object) -> tuple[str | None, dict[int, str]]:
    """Get only the verified repairs that this font object can use."""
    family = stable_family(font)
    if family is None:
        return None, {}

    repairs = dict(CODE_REPAIRS.get(family, {}))
    glyph_repairs = GLYPH_REPAIRS.get(family, {})
    first = int(font.get("/FirstChar", 0))
    last = int(font.get("/LastChar", 255))
    for code, glyph in encoding_differences(font).items():
        if glyph in glyph_repairs:
            # This family also occurs in a larger symbol font where C19 is not an
            # accent. The verified accent subset contains only that one glyph.
            if family == "AdvP4C4E59" and first != last:
                repairs[code] = INVISIBLE_GLYPH
            else:
                repairs[code] = glyph_repairs[glyph]

    return family, {
        code: value for code, value in repairs.items() if first <= code <= last
    }


def _shown_bytes(operands: pikepdf.Object, operator: str) -> bytes:
    """Get the encoded string from a text-showing PDF instruction."""
    if operator in {"Tj", "'", '"'}:
        value = operands[-1]
        return bytes(value) if isinstance(value, pikepdf.String) else b""
    if operator != "TJ" or not operands:
        return b""
    return b"".join(
        bytes(item) for item in operands[0] if isinstance(item, pikepdf.String)
    )


def actual_text_repairs(pdf: pikepdf.Pdf) -> dict[tuple[int, int], dict[int, str]]:
    """Promote unambiguous ActualText glyph values into their font CMaps.

    Some generated PDFs put ligature text in marked content but map the glyph to
    NUL. The layout engine intentionally ignores marked-content text. Promote only
    a single-glyph, printable value that is identical at every use of that code.
    """
    candidates: dict[tuple[int, int], dict[int, set[str]]] = {}
    seen_forms: set[tuple[int, int]] = set()

    def scan(container: pikepdf.Object, resources: pikepdf.Object) -> None:
        font_name = None
        font_stack: list[pikepdf.Object | None] = []
        actual = None
        actual_stack: list[str | None] = []
        try:
            instructions = pikepdf.parse_content_stream(container)
        except (pikepdf.PdfError, TypeError):
            return

        for operands, raw_operator in instructions:
            operator = str(raw_operator)
            if operator == "q":
                font_stack.append(font_name)
                continue
            if operator == "Q":
                font_name = font_stack.pop() if font_stack else None
                continue
            if operator == "Tf":
                font_name = operands[0]
                continue
            if operator == "BDC":
                actual_stack.append(actual)
                if len(operands) > 1 and isinstance(operands[1], pikepdf.Dictionary):
                    value = operands[1].get("/ActualText")
                    if value is not None:
                        actual = str(value)
                continue
            if operator == "EMC":
                actual = actual_stack.pop() if actual_stack else None
                continue
            if operator == "Do":
                xobjects = resources.get("/XObject", {})
                form = (
                    xobjects.get(operands[0])
                    if isinstance(xobjects, pikepdf.Dictionary)
                    else None
                )
                if (
                    isinstance(form, pikepdf.Stream)
                    and str(form.get("/Subtype")) == "/Form"
                ):
                    key = form.objgen
                    if key == (0, 0) or key not in seen_forms:
                        if key != (0, 0):
                            seen_forms.add(key)
                        scan(form, form.get("/Resources", resources))
                continue
            if operator not in {"Tj", "TJ", "'", '"'} or actual is None:
                continue
            if (
                not actual
                or len(actual) > 8
                or not all(char.isprintable() for char in actual)
            ):
                continue

            fonts = resources.get("/Font", {})
            font = fonts.get(font_name) if isinstance(fonts, pikepdf.Dictionary) else None
            if not isinstance(font, pikepdf.Dictionary):
                continue
            raw = _shown_bytes(operands, operator)
            width = font_code_width(font)
            if len(raw) != width:
                continue
            code = int.from_bytes(raw, "big")
            by_code = candidates.setdefault(font.objgen, {})
            by_code.setdefault(code, set()).add(actual)

    for page in pdf.pages:
        scan(page, page.get("/Resources", {}))

    repairs: dict[tuple[int, int], dict[int, str]] = {}
    for key, by_code in candidates.items():
        resolved = {
            code: next(iter(values))
            for code, values in by_code.items()
            if len(values) == 1
        }
        if resolved:
            repairs[key] = resolved
    return repairs


def _fonts_in_resources(
    resources: pikepdf.Object,
    seen_xobjects: set[tuple[int, int]],
):
    """Yield fonts from page resources and nested form XObjects."""
    if not isinstance(resources, pikepdf.Dictionary):
        return
    fonts = resources.get("/Font", {})
    if isinstance(fonts, pikepdf.Dictionary):
        yield from fonts.values()

    xobjects = resources.get("/XObject", {})
    if not isinstance(xobjects, pikepdf.Dictionary):
        return
    for xobject in xobjects.values():
        if not isinstance(xobject, pikepdf.Stream):
            continue
        key = xobject.objgen
        if key != (0, 0) and key in seen_xobjects:
            continue
        if key != (0, 0):
            seen_xobjects.add(key)
        yield from _fonts_in_resources(xobject.get("/Resources", {}), seen_xobjects)


def repair_pdf(source: Path, target: Path) -> list[dict]:
    """Write a temporary PDF with corrected ToUnicode maps."""
    changes: list[dict] = []
    with pikepdf.open(source) as pdf:
        marked_content_repairs = actual_text_repairs(pdf)
        seen_fonts: set[tuple[int, int]] = set()
        seen_xobjects: set[tuple[int, int]] = set()
        for page_number, page in enumerate(pdf.pages, 1):
            resources = page.get("/Resources", {})
            for font in _fonts_in_resources(resources, seen_xobjects):
                key = font.objgen
                if key != (0, 0) and key in seen_fonts:
                    continue
                if key != (0, 0):
                    seen_fonts.add(key)

                family, verified_repairs = repairs_for_font(font)
                repairs = dict(marked_content_repairs.get(key, {}))
                repairs.update(verified_repairs)
                if not repairs:
                    continue

                width = font_code_width(font)
                first = int(font.get("/FirstChar", 0))
                last = int(font.get("/LastChar", (1 << (8 * width)) - 1))
                mapping = {
                    code: value
                    for code, value in existing_mapping(font).items()
                    if first <= code <= last and code < (1 << (8 * width))
                }
                mapping.update(repairs)
                object_number = key[0] if key != (0, 0) else len(changes) + 1
                font["/ToUnicode"] = pdf.make_stream(
                    build_tounicode(mapping, f"EQGraph{object_number}", width)
                )
                label = family or f"{str(font.get('/BaseFont', 'unknown'))}:ActualText"
                changes.append(
                    {
                        "page": page_number,
                        "object": list(key),
                        "family": label,
                        "codes": sorted(repairs),
                    }
                )

        if changes:
            pdf.save(
                target,
                compress_streams=True,
                object_stream_mode=pikepdf.ObjectStreamMode.preserve,
                deterministic_id=True,
            )
    if not changes:
        shutil.copyfile(source, target)
    return changes


def normalise(text: str) -> str:
    """Make text suitable for a conservative title or cover comparison."""
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def drop_cover_chunks(chunks: list[dict]) -> tuple[list[dict], int]:
    """Drop only leading pages with verified repository cover text."""
    index = 0
    while index < len(chunks) - 1:
        text = normalise(chunks[index].get("text", ""))
        if not any(marker in text for marker in COVER_SHEET_MARKERS):
            break
        index += 1
    return chunks[index:], index


def drop_title_headings(markdown: str, title: str | None) -> str:
    """Remove a drawn title when the caller will add the manifest title."""
    if not title:
        return markdown

    wanted = normalise(title)
    seen = 0
    output: list[str] = []
    for line in markdown.splitlines():
        if line.strip():
            seen += 1
        match = HEADING_RE.match(line)
        if match and seen <= TITLE_WINDOW:
            candidate = normalise(line[match.end() :])
            if len(candidate) >= 20 and candidate in wanted:
                continue
        output.append(line)
    return "\n".join(output)


def fix_detached_accents(markdown: str) -> str:
    """Join the verified positioned acute accent with its following letter."""
    pattern = re.compile(
        rf"(?:<sup>\s*)?{re.escape(DETACHED_ACUTE)}(?:\s*</sup>)?\s*c"
    )
    markdown = pattern.sub("ć", markdown)
    invisible = re.compile(
        rf"(?:<sup>\s*)?{re.escape(INVISIBLE_GLYPH)}(?:\s*</sup>)?"
    )
    markdown = invisible.sub("", markdown)
    if DETACHED_ACUTE in markdown:
        raise RuntimeError("an unhandled detached accent remains in the PDF text")
    return unicodedata.normalize("NFC", markdown)


def _page_number(chunk: dict, fallback: int) -> int:
    metadata = chunk.get("metadata") or {}
    value = metadata.get("page_number", fallback)
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


def inject_formula_text(chunks: list[dict], pdf: Path) -> tuple[list[dict], int, int]:
    """Insert native text where the layout model marks a formula region.

    The layout model returns an exact output position and page rectangle for each
    formula, but it writes an empty slot unless image export is enabled. Read that
    rectangle from the same repaired PDF and put its visual text at the supplied
    position. A fenced text block preserves line placement without claiming that
    the result is LaTeX.
    """
    output: list[dict] = []
    inserted = 0
    unread = 0
    with pymupdf.open(pdf) as document:
        for fallback, original in enumerate(chunks, 1):
            chunk = dict(original)
            text = chunk.get("text", "")
            page_number = _page_number(chunk, fallback)
            page = document[page_number - 1]
            formula_boxes = [
                box
                for box in chunk.get("page_boxes", [])
                if box.get("class") == "formula"
            ]
            for box in sorted(
                formula_boxes, key=lambda item: item.get("pos", (0, 0))[0], reverse=True
            ):
                start, stop = box.get("pos", (0, 0))
                rectangle = pymupdf.Rect(box["bbox"])
                formula = page.get_text("text", clip=rectangle, sort=True).strip()
                formula = "".join(
                    char
                    if ord(char) >= 32 or char in "\n\t"
                    else "\N{REPLACEMENT CHARACTER}"
                    for char in formula
                )
                if formula:
                    block = f"\n\n```text\n{formula}\n```\n\n"
                    text = text[:start] + block + text[stop:]
                    inserted += 1
                else:
                    unread += 1
            chunk["text"] = text
            output.append(chunk)
    return output, inserted, unread


def chunks_to_markdown(chunks: list[dict], title: str | None) -> str:
    """Join page chunks while keeping the source page number for verification."""
    pages = []
    for fallback, chunk in enumerate(chunks, 1):
        text = chunk.get("text", "").strip()
        if not text:
            continue
        number = _page_number(chunk, fallback)
        pages.append(f"<!-- source-page: {number} -->\n\n{text}")

    markdown = "\n\n".join(pages)
    markdown = fix_detached_accents(markdown)
    markdown = drop_title_headings(markdown, title)
    # The manifest title is the only level-one heading in the final document.
    markdown = re.sub(r"^#\s+", "## ", markdown, flags=re.MULTILINE)
    return markdown.rstrip() + "\n"


def convert(pdf: Path, title: str | None = None) -> tuple[str, dict]:
    """Return structured Markdown and conversion statistics for one PDF."""
    with tempfile.TemporaryDirectory() as tmp:
        repaired_pdf = Path(tmp) / "repaired.pdf"
        repairs = repair_pdf(pdf, repaired_pdf)
        chunks = pymupdf4llm.to_markdown(
            repaired_pdf,
            page_chunks=True,
            show_progress=False,
            use_ocr=False,
            header=False,
            footer=False,
        )
        chunks, formulas, unread_formulas = inject_formula_text(chunks, repaired_pdf)

    if not isinstance(chunks, list) or not chunks:
        raise RuntimeError("the PDF parser returned no pages")
    if not any(chunk.get("text", "").strip() for chunk in chunks):
        raise RuntimeError("no text layer: the PDF holds page images only")

    source_pages = len(chunks)
    chunks, cover_pages = drop_cover_chunks(chunks)
    body = chunks_to_markdown(chunks, title)
    replacement_characters = body.count("\ufffd")
    if unread_formulas:
        raise RuntimeError(
            f"{unread_formulas} formula region(s) have no readable native text"
        )
    if replacement_characters:
        raise RuntimeError(
            f"the PDF text contains {replacement_characters} replacement character(s)"
        )
    lines = body.splitlines()
    stats = {
        "source_pages": source_pages,
        "pages": len(chunks),
        "cover_sheet_pages_dropped": cover_pages,
        "font_objects_repaired": len(repairs),
        "font_codes_repaired": sum(len(item["codes"]) for item in repairs),
        "tables": sum(bool(TABLE_RULE_RE.match(line)) for line in lines),
        "headings": sum(bool(HEADING_RE.match(line)) for line in lines),
        "formulas": formulas,
        "unread_formulas": unread_formulas,
        "replacement_characters": replacement_characters,
    }
    return body, stats


def main() -> int:
    """Run the converter for one PDF."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--title")
    args = parser.parse_args()
    text, stats = convert(args.pdf, args.title)
    print(text)
    print(json.dumps(stats, ensure_ascii=False, sort_keys=True), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

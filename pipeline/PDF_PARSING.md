# PDF parsing

## Converter

[`scripts/pdf_markdown.py`](../scripts/pdf_markdown.py) version 3 is the project PDF converter.
It writes a temporary PDF with corrected `/ToUnicode` font maps, runs one PyMuPDF4LLM structural pass, and outputs one Markdown document with headings, tables, formula text, and source-page markers.
The font repair is upstream of the parser; the source PDF is unchanged.

## Rejected tools

| Tool | Reason |
|---|---|
| Docling 2.120.3 | Reads the same wrong source font maps; adds an unnecessary pipeline. |
| GROBID 0.9.1 CRF | Header extraction made author errors; does not produce the required Markdown. |
| pdf-inspector 1.15.0 | Corrupted tested signs; layout errors. |
| Marker | The local PDF set has text layers and does not need a vision model. |

## Rules

- No OCR. An image-only PDF fails with a clear error.
- Never claim LaTeX for formula regions; insert native text in a fenced `text` block.
- Repair `/ToUnicode` by verified font family and glyph name or code. Do not repair extracted numbers by context.
- Promote an unambiguous single-glyph `/ActualText` value into the temporary font map.
- Use Poppler layout text as a bounded fallback for PDFs whose font maps leave unreadable glyphs. Mark every unresolved position with `[unreadable glyph]`.
- Remove a leading page only when its text has known repository branding.
- Count title authors only in the header, not from bibliography entries.

## Fallback

Fallback and failure counts are in [docs/RESULTS.md](../docs/RESULTS.md).
Text near an `[unreadable glyph]` marker is not authoritative; the source audit must check facts near a marker against the PDF.

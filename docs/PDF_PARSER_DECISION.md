# PDF parser decision

Date: 2026-08-20

## Decision

Adopt [`scripts/pdf_markdown.py`](../scripts/pdf_markdown.py) version 3 as the
project PDF converter.

The converter uses this fixed sequence for every PDF:

1. It writes a temporary PDF with corrected `/ToUnicode` font maps.
2. PyMuPDF4LLM makes one structural pass over all pages of that repaired PDF.
3. The converter writes headings, tables, formula text, and source-page markers
   to one Markdown document.

There is no table trigger and no second table output to merge. PyMuPDF4LLM
handles prose, headings, and tables in the same pass. If its layout result marks
a formula region, the converter inserts the native text from that region at the
position that the same layout result gives. It puts formula text in a fenced
`text` block and does not claim that it is LaTeX.

The font repair is upstream of the structural parser. This is why PyMuPDF4LLM
can now read the affected numbers and signs correctly. The earlier failures did
not mean that its table logic was unreliable. They meant that the source PDFs
gave all text extractors wrong Unicode values for some visible glyphs.

## Font repair

The source PDFs can draw the correct visible sign while their font map gives a
different character. For example, a visible minus sign can extract as `2`, and
`P < .001` can extract as `P , .001`. These errors are silent and can change a
result.

Version 3 fixes this at PDF level:

- It promotes unambiguous `/ActualText` values that the PDF already supplies.
- It applies corpus mappings only when the font family and glyph name or code
  match a rendered source check.
- It keeps the original PDF unchanged and uses the repaired copy only during
  conversion.

This method is not tied to Poppler or PyMuPDF4LLM. Another parser can also read
the repaired temporary PDF. The production path uses PyMuPDF4LLM because its
single output keeps useful heading and table structure.

## Validation result

The final run covered all 67 project PDFs, including the 7 current pilot PDFs
and the 60 pending PDF-only papers.

| Check | Result |
| --- | ---: |
| PDFs completed | 67 of 67 |
| Source pages read | 1,207 |
| Output pages | 1,196 |
| Verified repository cover pages removed | 11 |
| Font objects repaired | 120 |
| Font codes repaired | 282 |
| Markdown tables | 512 |
| Formula regions inserted | 31 |
| Unread formula regions | 0 |
| Unicode replacement characters | 0 |
| Conversion failures | 0 |

All 67 PDFs have text layers, so OCR is disabled. An image-only PDF fails with
a clear error instead of producing an empty document.

The source regression suite checks Elsevier, Value in Health Regional Issues,
SAGE, F1000, and repository PDFs. It checks inequality signs, minus signs,
letters with diacritics, copyright signs, formula symbols, tables, cover-page
handling, source-page markers, and one-byte and two-byte font maps. The final
suite has 14 passing tests.

The final render regression compared 13 selected original and repaired page
pairs. The PNG files were byte-identical. The selection included the large
compendium formula pages, a font-object special case in an author name, text in
a diagram, and Research Square ligatures. Earlier prototype checks also found
no visual page change.

## Tool assessment

The earlier comparison remains useful as a failure record:

| Tool | Decision |
| --- | --- |
| Previous Poppler converter | Remove. It repaired some symbols, but it flattened tables and used weak custom layout rules. |
| PyMuPDF4LLM 1.28.2 on unmodified PDFs | Do not use directly on this corpus. Wrong source font maps caused silent character errors. |
| PyMuPDF4LLM 1.28.2 after PDF-level repair | Adopt. It gives one structured Markdown output with correct tested symbols. |
| Docling 2.120.3 | Do not use. It read the same wrong source font maps and adds an unnecessary pipeline. |
| GROBID 0.9.1 CRF | Do not use as the paper converter. Its header extraction made author errors, and it does not produce the required Markdown. |
| `pdf-inspector` 1.15.0 | Do not use. It corrupted tested signs and had layout errors. |
| Marker | Do not add now. The local PDF set has text layers and does not need a vision model. |

Poppler is not a production parser dependency. `pdftoppm` remains useful only
for an optional visual regression check.

## Install and reproduce

Pandoc is still required for JATS XML. Install the PDF packages in the same
Python environment that runs the converter:

```sh
brew install pandoc
python3 -m venv .venv
.venv/bin/pip install -r requirements-pdf.txt
PYTHONPATH=scripts .venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/to_markdown.py --out tmp/pdfs/pdf-pilot 1455-RA 442-RA 1883-RA 1508-RA 20180080 361-RA
```

The Markdown keeps `<!-- source-page: N -->` before each page. Semantic
extraction must keep the existing source-page verification gate for claims and
numbers. The table markup is now part of the canonical Markdown, not a separate
review view.

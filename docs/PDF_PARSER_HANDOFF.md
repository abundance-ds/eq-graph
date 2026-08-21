# PDF parser handoff

Status: implemented and validated on 2026-08-20. See the
[`PDF parser decision`](PDF_PARSER_DECISION.md).

Use [`scripts/pdf_markdown.py`](../scripts/pdf_markdown.py) version 3 for all
project PDFs. Do not run a second parser for tables. The converter always does
one PyMuPDF4LLM structural pass and writes tables in the same Markdown as the
article text.

Before that pass, the converter repairs wrong or missing PDF font maps in a
temporary copy. This makes the corrected characters available to the complete
parser. It does not patch numbers after extraction, and it does not change the
source PDF.

## Run

```sh
brew install pandoc
python3 -m venv .venv
.venv/bin/pip install -r requirements-pdf.txt
PYTHONPATH=scripts .venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/to_markdown.py
```

For each PDF, front matter records the parser version, source and output page
counts, font repairs, table and heading counts, formula counts, and replacement
character count. Page comments keep the source page number.

The full test run completed all 67 project PDFs and 1,207 source pages. It found
512 tables and 31 formula regions. It had no unread formula, replacement
character, or conversion failure.

## New PDF behavior

- A PDF with no text layer fails clearly. Add an OCR path only when such a source
  enters the corpus.
- A new wrong font map needs a rendered source check before a mapping is added.
- A repository cover is removed only when its text has known repository
  branding.
- Formula regions remain visual text blocks. They are not converted to LaTeX.

The parser selection task is complete. The next PDF task is semantic processing
of the 60 pending papers with the existing source-page audit gate.

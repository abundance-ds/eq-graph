# PDF parser handoff

Evaluate a mature, maintained academic PDF-to-Markdown system for the 60 local PDF-only papers. Prefer Docling, GROBID, or another established library. Do not build a new parser. Use `scripts/pdf_markdown.py` only as the baseline: its layout logic is general, but it was calibrated on seven Value in Health PDFs and contains Elsevier-specific font repairs. `pdf-inspector` 1.15.0 is not a valid default because it silently corrupted minus and inequality signs in the six-paper test.

Use exactly the same six calibration PDFs recorded in
`../pilot/ontology-development-v3/pdf-calibration/PARSER_COMPARISON.md`, so the
new result is directly comparable with the rejected `pdf-inspector` run. Do not
add papers to the adoption test. Compare source-page renders with each result.
Check reading order, headings, tables, minus and inequality signs, missing
text, and separation of the bibliography from the article body. Preserve the
PDF as the source. Do not reconstruct JATS XML from PDF. Do not ask the
semantic extraction agent to reproduce references; bibliography parsing is an
optional, separate process.

Return one concise Markdown decision record. State the tools and versions tested, exact failures, the recommended default and fallback, install and reproduction commands, and a clear adopt-or-reject decision. Prefer the simplest reliable off-the-shelf pipeline. Do not change the production converter until the selected system passes the test.

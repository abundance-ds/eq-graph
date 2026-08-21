# corpus

The full texts as Markdown, ready for stage-2 extraction.
Generated from `input/projects/*/papers/*.{xml,pdf}` by [`scripts/to_markdown.py`](../scripts/to_markdown.py); nothing here is edited by hand.

```sh
python3 scripts/to_markdown.py          # convert what changed
python3 scripts/to_markdown.py --force  # reconvert everything
```

Rerunning is cheap and safe: a paper is reconverted only when its source bytes, the converter, or the version of the tool that read it changed, and the output is byte-identical across runs.
Deleting a `.md` file is enough to have it rebuilt — the provenance stamp lives in the file's own front matter, not in a side ledger.

## Layout

    corpus/index.json                       every converted document
    corpus/<project id>/<work id>.md        one paper, front matter + body

The stem matches the source XML exactly, so `corpus/20170600/doi_10.1007_s40273-022-01172-4.md` came from `input/projects/20170600/papers/doi_10.1007_s40273-022-01172-4.xml`.
A paper funded by two projects appears under both, as it does in `input/`.

## What a document contains

YAML front matter carries the identifiers, the bibliographic metadata, and the provenance of the source — `project_id`, `doi`, `pmid`, `pmcid`, journal, date, authors, affiliations, keywords, licence, and the source SHA-256 where they are available.
Extraction can therefore attribute a paper to its grant without a second lookup.

The raw JATS XML remains the canonical source for structured metadata.
The Markdown is a readable article representation for semantic work; it is not a reason to ask an AI to reconstruct metadata that the XML already supplies.

The body is the article: `#` is the title, `## Abstract` holds the abstract with its own subsections beneath it, and the paper's sections follow at `##`.
The reference list is rendered as numbered entries matching the `[1]`, `[4–7]` markers in the text.

## Coverage and limits

- **227 of the 287 held full texts**: all 220 JATS XML files and the 7 PDF files used in the ontology pilot.
  `to_markdown.py` converts PDFs with [`pdf_markdown.py`](../scripts/pdf_markdown.py).
  It repairs verified font maps before one PyMuPDF4LLM structural pass.
  The converter passed all 67 local PDFs. The other 60 remain outside this
  audited corpus until their semantic processing run.
  PDF Markdown includes headings, pipe tables, formula text blocks, and source-page markers.
  Publisher PDFs can still lack structured authors, keywords, and affiliations.
  Prefer the XML wherever a paper is held as both.
- **Tables** are pipe tables where the shape allows and raw HTML where it does not — rowspans and nested tables have no Markdown form.
  This is where the value-set coefficients and sample characteristics live, so it matters that they survive at all; both forms are readable, neither is tidy.
- **Figures** keep their captions, but the `![](…jpg)` links point at image files that were never downloaded.
- **Licence values are inconsistent** — `cc-by` and `cc by` both occur, and one record holds a bare URL.
  They are passed through from Unpaywall via `manifest.json` rather than normalised, so the front matter says what was recorded.
- **Not every document is a research paper.**
  `2016440/doi_10.1371_journal.pone.0305983.md` is a 3 KB correction notice, not a study; the corpus is what the pipeline resolved, so stage 2 should expect a few of these.
- Every converted paper is Creative Commons except one recorded as `other-oa`.
  The publisher TDM licences the [root README](../README.md#conventions-and-constraints) flags as blocking publication are all on PDFs, so none of them are here — but that is a fact about today's corpus, not a guarantee, and `licence` in the front matter is the field to check.

## Why the conversion is not just a pandoc call

Pandoc does the document conversion; the script exists for the two things pandoc's JATS reader discards before any template, filter or `--citeproc` can reach them.

The reference list is the sharp one: the reader collapses each `<ref>` to `{"id": "CR1"}` and drops the citation text at read time, leaving an empty `<div id="refs">` where the bibliography was — 9,890 references across this corpus.
The abstract is the quieter one: it is filed under document metadata, which every Markdown writer drops unless a template asks for it.
Both are read back out of the JATS by the script.
See the module docstring for the detail, and [`CLAUDE.md`](../CLAUDE.md) for the traps found along the way.

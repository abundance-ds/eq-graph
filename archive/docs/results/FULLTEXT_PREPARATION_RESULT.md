# Full-text preparation result

All 1,607 verified sources have extraction-ready Markdown and deterministic
metadata, and all 1,607 have a paper package. There were no failures.

| | records |
|---|---|
| verified sources prepared | 1,607 — 885 JATS, 722 PDF |
| paper packages built | 1,607 |
| packages with nominated project rows | 1,397 |
| packages with none | 210 |
| failures | 0 |

The 72 routed records without a full text are not prepared and have no package.
Each carries a disposition in
[`../data/fulltext-not-retrieved.csv`](../../../data/fulltext-not-retrieved.csv); see
[`FULLTEXT_RETRIEVAL_RESULT.md`](FULLTEXT_RETRIEVAL_RESULT.md).

## What the converters did

JATS supplied structured publication metadata and reference records for 885
sources. Those references stay outside the AI reading text.

The approved PDF converter (`pymupdf4llm` with `pikepdf` font repair) processed
722 PDFs. Facts a source audit must know about that text:

- **315 PDFs needed font-map repair**, covering 1,208 character codes. Publisher
  PDFs draw `−`, `<`, `>`, `≥` and `≤` from symbol fonts with no usable
  `/ToUnicode` map, so an unrepaired extractor silently reads `−0.654` as
  `20.654` and `P < .001` as `P , .001`. Repair happens in a temporary copy, by
  verified font and glyph identity. Numbers are never repaired by context.
- **163 PDFs fell back to a bounded Poppler layout pass** because their glyph
  maps stayed unsupported after repair. Those files carry **4,861 explicit
  unreadable-glyph markers**. The runner did not guess their meaning. The source
  audit must check any fact near a marker against the PDF itself.
- **33 repository cover-sheet pages were dropped**, only where the leading page
  carried known repository branding.

PDF references remain in the reading copy, but the semantic agent must not
reconstruct them.

## Boundary

Markdown is the AI reading copy. The verified PDF or JATS file is the source of
record.

## Outputs and hashes

Local outputs, both git-ignored:

- `scale/protocol-2.0/fulltext-preparation-v2/`
- `scale/protocol-2.0/fulltext-paper-packages-v2/`

- preparation manifest SHA-256 `216cd750c3ce2ba5ddb713f3506560855a55a9a5f1b0d03818f794540551dcb4`
- package manifest SHA-256 `51ecd8d2d4e06475d56114094ceca1a716107818797d22851e92ece34d73e2a4`

Rebuild with:

```sh
.venv/bin/python pipeline/prepare_scale_fulltexts.py --workers 4
python3 pipeline/build_fulltext_paper_packages.py \
  --fulltext-manifest scale/protocol-2.0/fulltext-preparation-v2/MANIFEST.tsv \
  --output scale/protocol-2.0/fulltext-paper-packages-v2
```

Both steps reuse completed work; this run reused 1,153 and prepared 454 new.

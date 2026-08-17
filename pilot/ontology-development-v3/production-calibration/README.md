# One-pass production calibration

## Purpose

Use one AI pass to make the full-text decision and, only when applicable,
extract the research record. Do not use separate filter, extraction, and
normalization agents.

```text
JATS or PDF
    |
    +-- deterministic metadata and text preparation
    |
    +-- one AI assessment and conditional extraction
    |
    +-- deterministic validation, flat indexing, and SQLite load
             |
             +-- targeted repair only for a failed check
```

## Agent input

- `ONTOLOGY_GRAPH.md`: one-page domain graph;
- `EXTRACTION_TASK_V2.md`: exact task used for the 50-paper run;
- `EXTRACTION_TASK_V3.md`: current task, with one fixed source-locator syntax;
- `INDEX_TASK.md`: flat typed search index, not JSON;
- deterministic JATS metadata and candidate project context;
- full article text.

The long ontology document is not the extraction prompt. The agent does not
receive source-checked reference records.

## Calibration evidence

The initial calibration used 30 source-checked papers:

- 30/30 structurally valid records;
- 29/30 initial disposition decisions;
- 86.2% high-value term coverage for extracted studies;
- 99.8% source locators on substantive bullets;
- 21/22 initial critical safety checks;
- mean record length 1,143 words.

The one failure treated unrelated EuroQol grants in competing interests as
support for the paper and treated DALY use as measurement research. Two short
rules corrected both errors. Targeted reruns then excluded the paper correctly.

A seven-paper lower-cost-model stress test passed 7/7 dispositions and 12/12
critical safety checks. Included records retained 87.5% of source-checked terms.
This supports the lower-cost model for the first pass.

The final task was then rerun on all 30 source-checked papers. After two
targeted repairs, it passed 30/30 expected dispositions, 30/30 structural
checks, and 22/22 critical safety checks. Exact reference-term recall was
84.6%. This is a demanding phrase-match test, not a general accuracy score.

The source-conflict check found the known contradictions in two test papers and
one additional table-versus-text conflict. A JATS parser correction now keeps
the complete funding statement, not only the funder and award ID. The 220-file
JATS audit still passes with zero parse and determinism failures.

## Machine-readable layer

The AI record remains Markdown. Its final flat index uses simple lines such as
`Instrument: EQ-5D-5L`, `Method: cTTO`, and `Model: hybrid model 3b`.
`index_terms.py` parses this block. `load_production.py` loads publication
metadata, authors, funding, Markdown sections, fact bullets, and index terms
into SQLite. It also creates full-text search. No second AI pass is required.

## Full local JATS production pass

- Scope: all 209 unique papers with JATS full text in the repository.
- First-pass model: `gpt-5.6-luna`.
- Final result: 209/209 records pass the deterministic record checks.
- Disposition: 206 included studies, two exclusions, and one correction notice
  kept as publication context.
- Connection: 182 `direct_eq`, 16 `application_only`, and 11
  `adjacent_measurement` records.
- Support: 201 records have explicit EuroQol support; eight state no support.
- SQLite: 209 publications, 3,731 normalized terms, 5,786 record-term links,
  16,471 fact bullets, and full-text search.
- Database tests: 9/9 pass, including record counts, unique DOI values,
  metadata, index terms, fact loading, full-text search, and integrity.

The first 50 records use several valid source-locator styles, for an automatic
recognition rate of 87.2%. Later records use the exact `Source:` form and reach
at least 99.8%. Combined recognition is 96.7%. The raw term index also contains
type variation. The loader applies only small, documented normalization rules
and retains each source term.

The combined local database is `production-local-jats-209.sqlite`. The full
record trees and database remain ignored local artefacts. The tracked workspace
manifests preserve their file names, sizes, and hashes. `FINAL_RESULT.md` is the
compact result record.

## Next input-format calibration

Convert and test the 60 local PDF-only files. Compare their text and extraction
quality with the JATS baseline. If PDF quality passes, use this same one-pass
process for later lawful retrieval. If a check fails, rebuild and rerun only
that record. Use `--overlay-run` when validation and database loading include a
repair.

This work uses only full texts already in the repository. It does not start
new full-text retrieval or change the frozen Protocol 2.0 abstract screen.

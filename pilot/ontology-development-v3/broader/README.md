# Broader semantic extraction test

Status: complete.

## Purpose

Test the ontology on 20 papers that were not in the 100-paper design set or the
first holdout set.

## Deliberate stress cases

- Verified EuroQol-supported outputs with no EQ instrument.
- Translation and cultural adaptation of a non-EQ instrument.
- Proxy perspective and recall-period interpretation.
- Systematic review and meta-analysis.
- Longitudinal responsiveness and clinical prediction.
- Remote compared with in-person valuation.
- Recall bias and experienced-health valuation.
- Routine PROM implementation and decision-aid usability.
- Methodological, reporting-checklist, and protocol papers.
- Retracted and correction publications.

## Process

1. Verify every Markdown and JATS source against `BATCH.tsv`.
2. Parse publication metadata from JATS.
3. Extract semantic records from the full Markdown articles.
4. Load the records into the relational pilot.
5. Test exact terms and the assigned competency questions.
6. Check each record against the source.
7. Record ontology fit, missing distinctions, and unnecessary fields.

## Result

- 20 source-checked semantic records.
- Zero overlap with the 100-paper design set or first holdout.
- 40 of 40 article and JATS files match the frozen hashes.
- 20 of 20 JATS DOI values match the manifest.
- 23 of 23 executable competency checks pass.
- 98 findings and 76 limitations loaded with study-dependent depth.
- One retracted article remains visible with a safety warning.
- One correction notice amends its parent and does not create a second study.

See `SOURCE_QA.md`, `ONTOLOGY_FIT.md`, and `QUERY_EVALUATION.md`.

The extraction rules are in `../validation/EXTRACTION_TASK.md`. The same rules
apply here. The database schema remains provisional during this test.

# Version-3 holdout validation

Status: complete.

## Purpose

- Test the final ontology proposal on papers that were not in the 100-paper design set.
- Inspect concrete extraction records before database design.
- Test representative user questions against the extracted records.
- Record missing, unnatural, or excessive ontology distinctions.

## Holdout

- Ten papers.
- Ten unique DOIs.
- No DOI occurs in `pilot/ontology-development-v3/papers.tsv`.
- Coverage includes valuation, DCE task design, OPUF, instrument development, qualitative proxy use, population health, systematic review, language-version psychometrics, cost-of-illness, and implementation.

## Files

- `holdout.tsv`: frozen source manifest.
- `EXTRACTION_TASK.md`: compact extraction instruction.
- `records/`: one extracted record per paper.
- `qa/`: source checks and extraction-fit review.
- `QUESTION_TEST.md`: question tests and answers.
- `RESULT.md`: pilot assessment and next decision.

## Result

- Ten of ten records completed and source-checked.
- Twelve question tests: ten pass, one partial, one funding-boundary test, and zero fail.
- The partial result identified a review evidence unit. The economic-analysis profile is deferred because the H09 project link is not verified.
- Other evidence-based refinements cover research-purpose versus study-design labels, source-dataset lineage, instrument-data reuse, and family-specific controlled detail.
- No database schema was designed in this phase.

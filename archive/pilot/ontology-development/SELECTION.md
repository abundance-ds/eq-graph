# Paper selection

Date: 2026-08-16.

## Development set

The 30 prepared ontology-pilot papers are the development set.
They contain 30 unique works: 23 JATS XML sources and 7 PDF sources.

- Batch 1: ten papers selected earlier for broad portfolio coverage.
- Batch 2: ten papers selected earlier to extend research-type coverage.
- Batch 3: ten companion papers in the same project folders.

The agent manifests contain no prior research-type or ontology labels.
All lineages receive the same batches in the same order.

## Holdout

Ten unique JATS works were selected from converted papers outside the development set.
Selection used Python's deterministic shuffle with seed `20260816` after reading the corpus index in stored order and deduplicating by Markdown file name.
The first ten results were accepted without replacement.

The holdout stays hidden until comparison and harmonization finish.

## Input limits

The three development batches contain approximately 2.19 MB of Markdown with references and 1.86 MB before reference sections.
Agents read papers from files and can skip reference sections unless they need them.

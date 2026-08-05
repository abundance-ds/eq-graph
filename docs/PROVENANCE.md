# Protocol 2.0 provenance

This file identifies the evidence trail from source data to the current results. The
scripts and `REPRODUCE.md` make each mechanical step repeatable. Validators check the
counts, identifiers, required fields, and allowed decisions.

## Governing records

| Record | Purpose |
|---|---|
| `../protocol-2.0.md` | Canonical method, fixed rules, and current counts |
| `METHOD_SIMPLE.md` | Short method without implementation detail |
| `../LOG.md` | Chronological decisions, failures, revisions, and results |
| `../pilot/protocol-2.0/REPRODUCE.md` | Commands that reproduce the pilot and scale preparation |
| `../scale/protocol-2.0/SCALE_STATUS.md` | Current scale funnel and work queue |
| `../scale/protocol-2.0/PAUSE_2026-08-05.md` | Dated pause state and restart order |

`../PROTOCOL.md` is a summary. `METHOD.md` and the July pipeline in `../README.md` are
retained design history. They do not govern Protocol 2.0 screening.

## Source-to-result trail

| Stage | Source or input | Evidence retained |
|---|---|---|
| Project portfolio | EuroQol public export | `../data/funded-projects-canonical.csv` |
| People | Project leaders and current EuroQol members | `../artefacts/01_people.csv` and `../artefacts/00_euroqol_members.csv` |
| Profile identity | OpenAlex profiles, ORCID IDs, affiliations, fields, coauthors, and works | `../scale/protocol-2.0/profile-qa-v1/`, `profile-scale-readiness.csv`, and `profile-review-queue-final.csv` |
| OpenAlex discovery | Accepted author IDs and the independent EuroQol funder route | `../artefacts/03_works/`, `openalex-discovery.jsonl`, and `openalex-discovery-summary.json` |
| ORCID and PubMed discovery | Accepted ORCID IDs; exact ORCID PubMed queries | `../scale/protocol-2.0/identifier-sources/` and `identifier-source-summary.json` |
| Source union | OpenAlex, ORCID, and PubMed records | `source-union.jsonl`, its summary and validator, and `source-union-title-year-identifier-variants.csv` |
| Abstract enrichment | Exact DOI or PMID queries to Europe PMC | `abstract-enrichment-selection.json`, the summary and validator, and cached responses under `raw/abstract-enrichment/` |
| Screening input | Article gate plus abstract-length gate | `article-corpus.jsonl`, `abstract-unavailable-or-short.csv`, and `screening-v1/selection.json` |
| AI screening | Frozen prompt and full title and abstract | `screening-v1/SYSTEM.md`; each completed batch retains `batch.json`, `input.md`, `decisions.jsonl`, and run metadata |
| Screening result | Validated complete decisions | `screening-v1/results.csv`, `retained.csv`, `excluded.csv`, `results-summary.json`, `progress.json`, `PRODUCTION_CHECK.md`, and `FINAL_SCREEN.md` |
| Exclusion audits | Two nonoverlapping blinded simple random samples of completed exclusions | `exclusion-audit-v1/` and `exclusion-audit-v2/`: selections, batch inputs and decisions, comparisons, adjudications, and evaluations |
| Pilot full text | Retrieved article files and source metadata | `../pilot/protocol-2.0/fulltext/manifest.csv` and `fulltext/summary.json` |
| Pilot assessment | Frozen prompts, selections, decisions, and summaries | `../pilot/protocol-2.0/fulltext-assessment-v1-final/`, `paper-assessment-v2/`, `funding-audit-v1/`, and `project-assessment-v3/` |
| Pilot result | Integrated evidence and evaluation | `../pilot/protocol-2.0/paper-assessment.csv`, `article-project-links.csv`, and `pilot-evaluation.json` |

All scale paths in the table are relative to `../scale/protocol-2.0/` unless the path
starts with `../`.

## AI run provenance

The screening folders retain the exact system prompt and the exact title and full
stored abstract supplied to the model. Each completed batch run records the model,
Codex CLI version, command, UTC start and end times, structured decisions, trace output,
and errors. Prompt-selection files record the prompt hash. Invalid and superseded
attempts remain labeled in their original folders.

## Known limits

- This directory is not a Git repository. It has file-level and run-level provenance,
  but it has no commit history or signed release tag.
- The pilot and first scale checks used operator reference labels. They were not an
  independent human validation.
- The 100-record scale exclusion audit used a separate AI subagent and primary-agent
  adjudication. It was blinded to production decisions, but it was not human review.
- The second 100-record exclusion audit used a fresh AI subagent and a nonoverlapping
  sample. It was also blinded, but it was not human review.
- Ninety-four people remain outside the author route pending identity review.
- A total of 4,827 scale article or review records have no usable abstract and remain
  outside AI screening.
- Seventy-eight retained pilot articles have no retrieved full text. Their funding and
  project links remain unassessed.
- Scale full-text retrieval has not started. The pause record prevents the pilot
  full-text artifacts from being mistaken for scale retrieval.

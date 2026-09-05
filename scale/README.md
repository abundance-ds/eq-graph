# Scale-run records

Working records of the protocol-2.0 scale run: discovery, abstract screen, full-text retrieval, preparation, and processing.

## Tracked files

The Git-tracked files under `protocol-2.0/` are summaries, selections, and audits.

| File or directory | Content |
|---|---|
| `identifier-source-summary.json` | ORCID and PubMed discovery counts per accepted profile |
| `openalex-discovery-summary.json` | OpenAlex author-route and funder-metadata counts |
| `source-union-summary.json`, `source-union-validation.json` | Deduplication result and validation |
| `source-union-title-year-identifier-variants.csv` | Merged title-year identifier groups |
| `abstract-enrichment-summary.json`, `abstract-enrichment-validation.json`, `abstract-enrichment-selection.json` | Europe PMC abstract enrichment |
| `abstract-unavailable-or-short.csv` | Records that failed the 80-character abstract gate |
| `scale-input-summary.json` | Funding-metadata discovery counts |
| `funding-metadata-discovery.csv`, `funding-metadata-pilot-evaluation.*` | Funder-metadata route records |
| `profile-qa-v1/` | Binary profile QA: system prompt, results, evaluation |
| `profile-scale-readiness.csv`, `profile-review-queue-final.csv` | Profile readiness and review queue |
| `fulltext-pilot-v1/MANIFEST.tsv` | Two-agent full-text pilot manifest |

## Local run folders

Run folders under `protocol-2.0/` are not in Git.
They hold prompts, per-record decisions, and compiled results.
Current local folders: `abstract-screen-v2-codex-r5`, `fulltext-retrieval-v2`, `fulltext-preparation-v2`, `fulltext-paper-packages-v2`, `fulltext-single-agent-v1`, `fulltext-sql-scale-v1`, and `fulltext-release-v1`, plus the discovery inputs `openalex-discovery.jsonl`, `source-union.jsonl`, `article-corpus.jsonl`, `raw/`, and `identifier-sources/`.

## Superseded records

Superseded scale records are in [`archive/scale/`](../archive/scale/): the topic screen validation, both exclusion audits, the full-text pilot results, and the 2026-08-05 pause record.

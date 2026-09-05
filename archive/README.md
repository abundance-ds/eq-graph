# Archive

This folder holds records that the release does not govern, kept as evidence of the approaches tried.

## LOG.md

| Path | What it is | Dates | Replaced by |
|---|---|---|---|
| `LOG.md` | Day-by-day build log | 2026-07-28 to 2026-08-31 | [docs/HISTORY.md](../docs/HISTORY.md) |

## docs/

| Path | What it is | Dates | Replaced by |
|---|---|---|---|
| `docs/2026-07-29-grant-mining-pipeline-assessment.md` | Assessment of the project-first pipeline at commit `68ebeab` | 2026-07-29 | [docs/HISTORY.md](../docs/HISTORY.md) |
| `docs/2026-07-29-scrape-pipeline.md` | Architecture of the scrape pipeline | 2026-07-29 | [docs/HISTORY.md](../docs/HISTORY.md) |
| `docs/2026-07-30-method-draft.md` | Two-pipeline method draft with evidence model | 2026-07-30 | [docs/METHOD.md](../docs/METHOD.md) |
| `docs/2026-08-05-topic-screen-and-pilot-results.md` | 10-person pilot result and topic-based scope | 2026-08-05 | [docs/RESULTS.md](../docs/RESULTS.md) |
| `docs/2026-08-24-scope-repair-plan.md` | Scope repair after the topic-screen invalidation | 2026-08-24 | [docs/METHOD.md](../docs/METHOD.md) |
| `docs/2026-08-27-pipeline-recap.md` | Pipeline recap at the end of full-text processing | 2026-08-27 | [docs/RESULTS.md](../docs/RESULTS.md) |
| `docs/neo4j-pilot/` | Neo4j Aura graph model, Cypher schema, and type declarations | 2026-07-31 to 2026-08-05 | SQLite model in the release |
| `docs/results/` | Five stage-result records: abstract screen, scope screen, retrieval, preparation, processing | 2026-08-24 to 2026-08-27 | [docs/RESULTS.md](../docs/RESULTS.md) |

## pilot/

| Path | What it is | Dates | Replaced by |
|---|---|---|---|
| `pilot/ontology-development/` | Version-1 ontology experiment: open architecture, 3 lineages, 30 papers | 2026-08-16 | Version 2 |
| `pilot/ontology-development-v2/` | Version-2 ontology experiment: paper-first task, granularity test | 2026-08-16 | Version 3 |
| `pilot/ontology-development-v3/` | Version-3 ontology: question-driven, 100 papers, production calibration | 2026-08-16 to 2026-08-20 | Version 4, ontology 0.13 |
| `pilot/ontology-development-v4/production/DECISION.md` | Production calibration decision for the 273-publication database | 2026-08-22 | [docs/DATA_RELEASE.md](../docs/DATA_RELEASE.md) |
| `pilot/ontology-development-v4/` round-01 to round-04, `regression-*`, `*_TASK.md`, `PROTOCOL.md` | Ontology 0.1 to 0.5 development: builder rounds, blind regressions, task prompts | 2026-08-17 to 08-21 | Ontology 0.13 |
| `pilot/ontology-development-v4/aggregate-validity-v2/` to `v4/` | Competency-question tests of the interim database | 2026-08-21 to 08-22 | [aggregate-validity-v5](../pilot/ontology-development-v4/aggregate-validity-v5/RESULT.md) |
| `pilot/ontology-development-v4/production/scale-pilot-01/RESULTS.md`, `normalization-v1/RESULT.md` | 20-paper pilot result and the registry normalization result | 2026-08-22 to 08-26 | [docs/RESULTS.md](../docs/RESULTS.md) |
| `pilot/protocol-2.0/` | 10-person pilot: screening, full-text assessment, project linkage | 2026-08-01 to 2026-08-05 | [docs/RESULTS.md](../docs/RESULTS.md) |

## scale/

| Path | What it is | Dates | Replaced by |
|---|---|---|---|
| `scale/protocol-2.0/screening-v1/` | Topic-based scale title-and-abstract screen (3,148 retained, 15,200 excluded) | 2026-08-04 to 2026-08-05 | Corrected abstract screen in [docs/RESULTS.md](../docs/RESULTS.md) |
| `scale/protocol-2.0/screening-v1-validation/` | Screening-v1 prompt validation (86 records) | 2026-08-04 | — |
| `scale/protocol-2.0/exclusion-audit-v1/` | First blinded 100-record exclusion audit | 2026-08-05 | — |
| `scale/protocol-2.0/exclusion-audit-v2/` | Second blinded 100-record exclusion audit | 2026-08-05 | — |
| `scale/protocol-2.0/fulltext-pilot-v1/` | 40-paper full-text eligibility pilot | 2026-08-22 | Full-text processing in [docs/RESULTS.md](../docs/RESULTS.md) |
| `scale/protocol-2.0/PAUSE_2026-08-05.md` | Pause point between screening and retrieval | 2026-08-05 | Resumed; see [docs/HISTORY.md](../docs/HISTORY.md) |

## pipeline/

| Path | What it is | Dates | Replaced by |
|---|---|---|---|
| `pipeline/` | 18 superseded pipeline scripts | 2026-08-01 to 2026-08-22 | Current scripts in `pipeline/` at the repository root |

These scripts are kept as records. Several import modules that stayed in `pipeline/` at the root and will not run from this location.

## Files deleted on 2026-09-03

The files listed below are in Git history.

- Gradle scaffolding
- `data/graph.json`, `data/extractions.json`, `data/funded-projects.csv`
- `corpus/`
- `scripts/scrape/`
- Per-batch traces and raw CSVs of superseded scale runs: profile-qa-v1 batches, screening-v1 raw results, screening-v1-validation batches, exclusion-audit batches, fulltext-pilot-v1 eligibility records
- Iteration snapshots of the interim database under `pilot/ontology-development-v4/production/`: rebuild-v2-\*, run-\*, pdf-tranche-\*
- Interim-pipeline scripts, prompts, repair queues, build manifests, and pilot records under `pilot/ontology-development-v4/production/`; the version-3 pilot code under `pilot/ontology-development-v3/` except `jats_metadata.py`, now `pipeline/jats_metadata.py` (removed 2026-09-04)
- 30 pipeline scripts of the 10-person pilot and superseded calibrations
- Two tests

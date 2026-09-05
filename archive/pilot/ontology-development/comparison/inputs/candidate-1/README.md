# Candidate 1 ontology record

This directory contains the Candidate 1 state after round 3.

- [`ontology.md`](ontology.md) gives the current ontology and its use rules.
- [`applications-round-01.md`](applications-round-01.md) applies the ontology to all ten papers in batch 01.
- [`applications-round-02.md`](applications-round-02.md) applies the revised ontology to all ten papers in batch 02.
- [`applications-round-03.md`](applications-round-03.md) applies the revised ontology to all ten papers in batch 03.
- [`decisions-and-open-cases.md`](decisions-and-open-cases.md) records origin decisions, difficult cases, and metadata issues.

## Round 3 run note

- Lineage: C
- Round: 3
- Task version: 1, frozen 2026-08-16
- Batch: `batch-03.tsv`
- Run date: 2026-08-16
- Agent: fresh round-3 Codex agent
- Input: the ten allowlisted full-text Markdown files, their supplied structured records, and the inherited Candidate 1 round-1 and round-2 Markdown record
- Completion: all ten papers were read and applied
- Mechanical check: every article SHA-256 value and byte count matched the batch manifest
- Branch and commit: not checked because the allowed research context did not include repository metadata

Round 3 retained the measurement-chain structure. It added research-data lineage, separate response-data integrity, task-frame and scale assumptions for valuation, explicit inferential aims, and provenance for population, inequality, burden, and cost outcomes. These changes prevent duplicate evidence counts and keep derived outcomes distinct from direct observations.

The source packet limits this work. Supplementary files, cited papers, external registries, and external metadata were not available as research inputs. The ontology describes what the supplied papers report and does not independently verify the studies or their conclusions.

## Round 2 run note

- Lineage: C
- Round: 2
- Task version: 1, frozen 2026-08-16
- Batch: `batch-02.tsv`
- Run date: 2026-08-16
- Agent: fresh round-2 Codex agent
- Input: the ten allowlisted full-text Markdown files, their supplied structured records, and the inherited Candidate 1 round-1 Markdown record
- Completion: all ten papers were read and applied
- Mechanical check: every article SHA-256 value and byte count matched the batch manifest
- Branch and commit: not checked because the allowed research context did not include repository metadata

Round 2 retained the measurement-chain structure. It added outcome derivation provenance, operational implementation properties, explicit respondent and referent facets, language-version artifacts, and more precise comparison alignment. The source packet limits this work. Supplementary files, cited papers, external registries, and external metadata were not available as research inputs. The ontology describes what the supplied papers report and does not independently verify the studies or their conclusions.

## Round 1 run note

- Lineage: C
- Round: 1
- Task version: 1, frozen 2026-08-16
- Batch: `batch-01.tsv`
- Input: the ten allowlisted full-text Markdown files and their supplied structured records
- Prior lineage state: none
- Completion: all ten papers were read and applied
- Mechanical check: every article SHA-256 value matched the batch manifest

The source packet limits this work. Supplementary files, cited papers, external registries, and external metadata were not available as research inputs. The ontology therefore describes what the supplied papers report. It does not independently verify the studies or their conclusions.

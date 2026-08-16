# Paper-first EuroQol ontology experiment

Status: valid rounds one to three complete; round-four calibration in progress, 2026-08-16.

## Why version 2 exists

Version 1 tested open ontology architecture.
It produced a stable common core and three internally coherent structures.
Human review selected a paper-first structure but found that the task did not specify the EuroQol research use clearly enough.
The agents therefore produced method descriptions that were often too broad.

Version 2 fixes the outer architecture and tests domain granularity.
It does not start from a proposed ontology schema.

## Research question

Given a paper-first EuroQol research record, which distinctions must be structured, tagged or summarized so that researchers can find relevant studies and understand what they did and found?

## Process

```text
fixed paper-first purpose + focused user questions + frozen papers
  -> three isolated lineages
  -> four rounds of ten papers
  -> one consolidation pass per lineage
  -> anonymous granularity comparison
  -> independent harmonization
  -> unchanged holdout application
  -> human review
```

## Research record

- [`PURPOSE.md`](PURPOSE.md): intended users, boundaries and data layers.
- [`USER_QUESTIONS.md`](USER_QUESTIONS.md): focused requirements, not a schema.
- [`TASK.md`](TASK.md): common agent task.
- [`PROTOCOL.md`](PROTOCOL.md): experimental controls.
- [`FREEZE.md`](FREEZE.md): frozen inputs, controls and file hashes.
- [`RUNS.md`](RUNS.md): valid rounds, branches and commits.
- [`SELECTION.md`](SELECTION.md): operator paper-selection record.
- [`PROBES.md`](PROBES.md): frozen operator tests kept from development agents.
- `batches/`: frozen development, calibration and holdout manifests.
- Each lineage: current ontology, paper applications, granularity decisions, rejected distinctions, unresolved cases and run notes.

Version-1 ontologies, comparisons, graph models and legacy extractions remain outside all version-2 agent contexts.

# Ontology development pilot

Status: development and anonymous comparison complete; harmonization awaits human review, 2026-08-16.

## Purpose

Develop a practical meta-research ontology from papers through repeated AI-assisted analysis.
Do not define the ontology before the experiment.

## Process

```text
frozen task + frozen paper batches + common base
  -> three isolated ontology lineages
  -> three rounds of ten new papers per lineage
  -> semantic comparison of structures, applications, changes and unresolved cases
  -> independent harmonization
  -> held-out paper test
  -> human review
```

Each round uses a fresh agent.
The agent receives only its lineage state and the next paper batch.
Agents do not see other lineages before the comparison.

## Principles

- Treat agents as research collaborators, not form-filling tools.
- Use a short task and flexible Markdown output.
- Do not prescribe ontology classes or a nested JSON schema.
- Do not force papers into the current ontology.
- Record changes, difficult cases and the papers that caused them.
- Compare meaning, not file shape or exact names.
- Use agent agreement as evidence, not as an automatic decision.
- Extract structured JATS metadata deterministically before semantic AI work.
- Design the database only after the ontology stabilizes.

## Research record

- [`PROTOCOL.md`](PROTOCOL.md): experiment controls and sequence.
- [`TASK.md`](TASK.md): common agent task.
- `batches/`: frozen development and holdout manifests.
- Each lineage: current ontology, paper applications, changes, open questions and run note.
- [`RUNS.md`](RUNS.md): round, batch, branch and commit record.
- `comparison/`: semantic crosswalk, disagreements, harmonization and holdout report.
- Root [`LOG.md`](../../LOG.md): dated milestones and main findings.

The record must let a researcher understand what was done, what changed and why.
It does not need to reproduce an agent's internal reasoning.

## Next

1. Review the material architecture and boundary alternatives in the semantic comparison.
2. Run independent harmonization, then apply the frozen candidate to held-out papers.

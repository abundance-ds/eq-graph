# Ontology development protocol

Status: frozen version 1, 2026-08-16, before the first run.

## Design

- Three independent lineages: A, B and C.
- Same task, paper batches, paper order, model configuration and base commit.
- Three rounds per lineage; ten new papers per round.
- Fresh agent for each round; prior lineage files provide continuity.
- Fresh agent context with no inherited conversation or prior ontology discussion.
- No cross-lineage access before all development rounds finish.
- Each agent receives an allowlisted worktree with only its task, lineage state, structured paper records and assigned full texts.
- Separate held-out papers for validation.

This first experiment tests agent convergence under controlled inputs.
A later paper-order test is optional if the lineages differ substantially.
It does not test model independence or order independence.

## Round

The agent reads the current lineage state and the new papers.
It applies, tests and revises the ontology.
It records:

- the current ontology in an intelligible form;
- its application to every new paper;
- important changes and their reasons;
- unresolved or poorly fitting cases;
- a short run note.

Markdown is the default.
The agent can add another useful representation.
No fixed ontology schema is required.

When a revision affects prior applications, the agent updates them or explains the remaining work.

## Controls

- Freeze manifests and SHA-256 values before the first run.
- Record branch, commit, agent, task version, batch and time.
- Keep prior graph schemas, legacy extractions and other lineage work out of the agent context.
- Confirm that each ten-paper packet and the inherited lineage state fit the agent workflow before the first run.
- Check only mechanical completeness with scripts.
- Keep semantic evaluation with capable agents and human review.
- Do not expose comparison results to development agents.
- Freeze the task before round one.
  If the task causes a material failure, label all affected runs invalid and restart every lineage with a new task version.

## Comparison

After round three, an independent agent compares anonymous lineage copies in a randomized order.
It maps equivalent, overlapping, conflicting and unique elements.
It examines application consistency, stability, coverage, redundancy, clarity and unresolved cases.
It cites the papers and lineage records that support each observation.

No majority rule decides ontology content.
No element count or combined numerical score decides ontology content.
Material alternatives remain explicit for human review.

## Harmonization and validation

An independent agent proposes a harmonized candidate from the three lineages and the comparison.
A fresh agent then applies the unchanged candidate to held-out papers and records fit and failure before it proposes any revision.

Stop for human input when a decision changes the ontology's purpose, retains materially different alternatives, or follows no clear evidence from the papers.

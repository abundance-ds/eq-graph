# Paper-first ontology development protocol

Status: frozen version 2, 2026-08-16, before the first run.

## Experimental question

Given a paper-first EuroQol research record, which distinctions must be structured, tagged or summarized so that researchers can find relevant studies and understand what they did and found?

Version 1 tested ontology architecture.
Version 2 fixes the paper-first architecture and tests granularity.
It does not harmonize or seed from version-1 ontology content.

## Design

- Three independent lineages: A, B and C.
- Same frozen purpose, user questions, task, papers, order, model configuration and base commit.
- Four rounds per lineage; ten new papers per round.
- Rounds one to three reuse the 30 version-1 papers for direct comparison.
- Round four is a purpose-selected granularity calibration batch.
- A fresh agent runs each round with no inherited conversation.
- Each agent sees only its lineage state and papers available through the current round.
- A separate fresh agent consolidates each lineage after round four against all 40 applications.
- No lineage sees another lineage, version-1 ontology work or comparison results during development.
- A separate purpose-stratified holdout remains hidden until one candidate is frozen.

The experiment tests convergence under one model configuration and one paper order.
It does not test model independence or order independence.

## Agent inputs and outputs

Each development agent receives `PURPOSE.md`, `USER_QUESTIONS.md`, `TASK.md`, this protocol, the current lineage record, one batch manifest and the available full texts.

The record must provide these functions in a clear form:

- current ontology and extraction guidance;
- application to every assigned paper;
- granularity decisions and paper or user-question evidence;
- important changes and rejected distinctions;
- unresolved cases;
- a short run note.

Markdown is the default.
No fixed file layout, nested schema or JSON contract is required.

## Consolidation

After round four, a fresh agent reviews the final ontology and all 40 applications.
It checks whether concepts added late also work for papers from earlier rounds.
It updates an earlier application only when needed or records why no change is needed.
It does not add new papers or see another lineage.

## Controls

- Freeze all documents, manifests and SHA-256 values before the first run.
- Record branch, commit, agent, task version, batch and time.
- Use isolated allowlisted worktrees and fresh contexts.
- Keep prior graph models, version-1 ontologies, legacy extractions and other lineage work out of agent context.
- Use paper-selection labels only in the operator record, not in agent manifests.
- Freeze representative retrieval and comparison probes before the first run.
  Keep them from development agents.
- Record the anonymous candidate mapping and its randomization seed outside the comparator context.
- Check source identity, paper coverage, allowed paths and Markdown integrity mechanically.
- Keep semantic evaluation with independent agents and human review.
- Do not change the task after development starts.
  If it causes a material failure, invalidate and restart all affected lineages with a new version.

The full texts test semantic ontology development.
They do not replace deterministic JATS extraction.
Raw JATS remains canonical for source metadata.

## Anonymous comparison

After consolidation, a fresh agent compares randomized anonymous lineage copies.
It evaluates:

- support for the focused user questions;
- distinctions that enable useful retrieval;
- distinctions that change interpretation;
- consistent use across paper applications;
- broad labels that hide important differences;
- fine labels that add no retrieval or interpretation value;
- choices between controlled terms, structured values, relations and narrative;
- findings, interpretation, implication and gap boundaries;
- unstable or unresolved boundaries.

Each disagreement must state its paper evidence and concrete user-query consequence.
For each frozen probe, trace which paper applications the candidate would retrieve or distinguish and why.
Record missed, ambiguous and false matches without combining them into a score.
No majority rule, ontology size, element count, nesting depth or combined numerical score decides content.

## Harmonization and holdout

A separate fresh agent uses the comparison, anonymous records and fixed purpose to propose one concise candidate.
It must resolve duplicate or overlapping terms instead of concatenating all lineage elements.
Material alternatives remain explicit for human review.

After the candidate is frozen, another fresh agent applies it unchanged to every held-out paper.
It records natural fit, ambiguity, forced fit, missing concepts and unnecessary detail before it proposes any revision.
It uses the held-out applications to test the frozen probes before any candidate revision.
No numeric pass threshold is used.

Stop for human input if a decision changes the ontology purpose, retains materially different alternatives or lacks clear paper and user-question evidence.

# Unchanged holdout application task

## Objective

Test the frozen paper-first EuroQol ontology on ten new papers.
Apply the candidate unchanged to every paper before you propose a revision.

This is a validation exercise, not another development round.
Do not edit `candidate/CANDIDATE.md`.
Do not add a concept during application to make a paper fit.
When the candidate does not fit, record the problem.

Do not use a numerical score or a pass threshold.

## Inputs

Read these files in full:

- `context/PURPOSE.md`
- `context/USER_QUESTIONS.md`
- `context/PROBES.md`
- `candidate/CANDIDATE.md`
- `batches/holdout.tsv`
- all ten article files listed in the manifest.

Verify each article SHA-256 value and byte count before application.

Do not use development papers, lineage records, comparison or harmonization records, selection labels, version-1 work, the Internet, Git history, external ontology guidance, or database-modeling skills.

## Sequence

Complete these stages in order:

1. Apply the unchanged candidate to all ten papers in manifest order.
2. Review the ten completed applications for fit and cross-paper retrieval.
3. Test the focused user questions and frozen probes with the holdout applications.
4. Only then write revision proposals, if the evidence justifies them.

Do not revise an earlier application to hide a fit problem.
You can correct a factual or transcription error, but record the correction in the run note.

## Stage 1: applications

Write `output/APPLICATIONS.md`.
For each paper, make a concise but complete semantic application of the candidate.
Use the candidate's terms and boundaries.
Cover the applicable purpose, components, evidence and population roles, instruments, administration, exact domain methods, analytic methods, outcomes, products, findings, interpretation, limits, implications, use or effect, future work, reuse and source uncertainty.
Omit concepts that do not apply.

Keep principal findings concise.
Do not copy every estimate and do not build claim-evidence-finding triples.
Keep deterministic bibliographic metadata outside the semantic application, apart from the manifest DOI used as the paper identifier.

End the file with an application-stage run note that confirms that the candidate was unchanged and that no later fit decision changed the applications.

## Stage 2: fit review

Write `output/FIT_REVIEW.md` after all ten applications are complete.

For each paper, record:

- natural fit;
- ambiguity in the candidate;
- forced fit or term misuse;
- missing concept or relation;
- unnecessary structured detail;
- source conflict or not-reported fact that is not an ontology failure.

State `none found` where applicable.
Each problem must state its effect on one focused user question or a concrete retrieval or interpretation result.

Then review cross-paper consistency.
Check whether the same concept receives the same meaning across valuation, mapping, psychometric, translation, qualitative, implementation, longitudinal outcome, administration-method, instrument-development, and evidence-synthesis work.

## Stage 3: question and probe checks

In `FIT_REVIEW.md`, check all 27 focused user questions against the ten populated applications.
Use `supported`, `ambiguous`, `unsupported`, or `not testable in this holdout` with a short reason.

Check all 14 frozen probes by their semantic purpose, not only by their development-paper examples.
Use holdout papers when they provide an equivalent test.
When the holdout has no relevant case, record `not testable`.
Also record false matches that the candidate would create.

For the corpus-gap probe, derive only a holdout-bounded result and label it with the ten-paper scope.

## Stage 4: revision proposals

Write `output/REVISION_PROPOSALS.md` only after the first three stages are complete.

For each proposed revision, state:

- the exact problem;
- the holdout paper evidence;
- the user question or probe consequence;
- the smallest change that fixes it;
- the development concept that it changes or extends;
- whether earlier applications need a backward check;
- the cost in complexity or extraction consistency.

Separate:

- required revisions that fix a missing or forced distinction;
- useful clarifications that do not change the ontology;
- ideas rejected because one paper detail does not justify a stable distinction.

If no ontology revision is justified, say so and still record useful wording clarifications or rejected ideas.
Do not edit or restate the full candidate.

## Final validation

Before completion, verify:

- ten manifest papers and ten applications;
- exact manifest DOI coverage;
- all 27 question checks;
- all 14 probe checks;
- three output files only;
- the candidate file hash is still `d97d07070b75c8a5fe831285205c27821b9df6de27ec04ef4b3a678ca98720dc`;
- no trailing whitespace and a final newline in each output;
- a run note lists all inputs and mechanical issues.

Make no commit.

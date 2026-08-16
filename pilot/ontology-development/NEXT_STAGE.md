# Harmonization and holdout procedure

Status: prepared but not started.

## Harmonization

1. Record the human architecture direction in `comparison/HARMONIZATION_DECISION.md`.
2. Freeze a short harmonization task.
3. Give a fresh agent the anonymous lineage records, semantic comparison and human direction.
4. Keep all holdout papers outside this workspace.
5. Ask the agent for one practical candidate, a concise decision record and explicit unresolved alternatives.
6. Do not concatenate all lineage elements. Retain a distinction only when it has repeated paper support or a clear meta-research use.
7. Use flexible Markdown. Do not require JSON or a detailed claim-evidence model.
8. Check links and source citations, then freeze the candidate and its SHA-256 value.

## Holdout

1. Give a new agent only the frozen candidate, the holdout task and the ten held-out papers.
2. Apply the candidate unchanged to every paper before proposing a revision.
3. For each paper, record natural fit, ambiguity, forced fit, missing concepts and unnecessary detail.
4. After all applications, summarize repeated failures and proposed changes in a separate section.
5. Do not use a combined numerical score or a pass threshold.
6. Preserve the unchanged applications, revision proposal and source hashes.
7. Stop for human review if a revision changes the ontology purpose or introduces a material alternative.

The final review compares the frozen candidate, holdout evidence and any proposed revision.
Database design starts only after this review.

# What happens after the architecture decision

## Harmonization

1. A fresh agent receives the three anonymous ontology records, their paper applications, the semantic comparison and the selected architecture.
2. It produces one concise ontology. It must resolve duplicate terms instead of combining every lineage element.
3. It explains important choices with examples from the 30 development papers.
4. I check that the result stays practical, uses clear Markdown and does not introduce a detailed claim-evidence model.
5. I freeze the candidate and record its exact version.

## Unseen-paper test

1. A different fresh agent receives the frozen ontology and ten papers that no development agent saw.
2. It applies the ontology without changing it.
3. It records what fits, what is unclear, what is missing and what appears unnecessary.
4. Only after all ten applications can it propose changes.
5. I bring the frozen candidate, test evidence and proposed changes to the human reviewer.

No numerical pass score is used.
The paper evidence and the nature of any failures determine whether a change is justified.
Database design starts after this review.

## Input needed now

Select option A, B or C in `comparison/HARMONIZATION_DECISION.md`.
No other decision is required before harmonization.

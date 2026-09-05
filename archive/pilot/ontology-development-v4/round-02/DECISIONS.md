# Round 2 decisions

## Result

- Two independent agents applied ontology version 0.1 to the same 15 papers.
- Primary-family agreement: 15/15.
- Both agents left the same two health-outcome papers unmapped.
- A fresh reviewer checked all material differences against the articles.
- The reviewed family partition covers all 30 cumulative studies without a
  round-1 family change.

## Accepted changes

- Add `HEALTH_OUTCOME_RESEARCH` for primary empirical outcome and determinant
  research in patient or condition-defined populations.
- Add bounded `TaskDesign` records for reusable elicitation and assessment
  tasks.
- Add bounded `StudyFactor` records with six initial analytic roles.
- Add `StakeholderInvolvement`, but keep its activity and role terms open.
- Add `PARTICIPATORY_DESIGN` as a method function.
- Let a product-state assertion identify the person or organization that made
  the assertion. Keep its normal evidence locator; do not add a duplicate
  evidence field.

## Still open

- Intervention roles for study factors.
- Controlled stakeholder-involvement roles.
- The G160 interviewer-score construction and weighting structure.
- Source-specific missing information and the nine round-2 source conflicts.

## Next gate

Reapply version 0.2 to all 30 papers, then use it unchanged on one more diverse
15-paper batch. Increase the cumulative batch size only if the next gaps are
mainly registry identities, aliases, or open concepts.

Full evidence and adjudication: [`review.md`](review.md).

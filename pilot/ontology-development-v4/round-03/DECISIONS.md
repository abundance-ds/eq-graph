# Round 3 decisions

## Result

- Blind version-0.2 regression agreement with the reviewed 30-paper partition:
  27/30.
- The regression correctly exposed two forced preference-research mappings,
  one part-level co-design gap, and one weak population-reference boundary.
- Two fresh agents then agreed on all 15 primary-family mappings in the
  confirmation batch.
- A fresh reviewer checked the material differences against 19 papers.
- The reviewed exact-one partition covers 45 studies.

## Accepted changes

- Add `HEALTH_PREFERENCE_RESEARCH`.
- Add `ECONOMIC_BURDEN_RESEARCH` and purpose
  `ECONOMIC_BURDEN_ESTIMATION`.
- Add part-level `PARTICIPATORY_DESIGN`; retain the separate method function.
- Add source-dated `PublicationStatusAssertion`, initially with `RETRACTED`.
- Add health behavior to `HEALTH_OUTCOME_RESEARCH` and add the
  `HEALTH_BEHAVIOR` outcome family.
- Restrict population-reference research to papers where norms or reference
  data are the stated main aim or principal output.
- Keep task randomization separate from study allocation.

## Corrected earlier mappings

- G101 and S031: `METHODS_RESEARCH` to `HEALTH_PREFERENCE_RESEARCH`.
- S099: `POPULATION_REFERENCE_DESCRIPTION` to
  `HEALTH_OUTCOME_RESEARCH`.

## Next gate

Reapply version 0.3 to all 45 papers, then use it unchanged on one final
15-paper confirmation batch. Consider a freeze only if that batch adds no
family, key, record, or controlled design value and changes no earlier family.

Full evidence and adjudication: [`review.md`](review.md).

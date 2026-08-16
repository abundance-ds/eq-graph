# Final candidate record

Status: ready for human review, 2026-08-16.

## Identity

- Frozen holdout input: [`harmonization/CANDIDATE.md`](harmonization/CANDIDATE.md)
- Frozen input commit: `b5ebdf5`
- Frozen input SHA-256: `d97d07070b75c8a5fe831285205c27821b9df6de27ec04ef4b3a678ca98720dc`
- Human-review candidate: [`FINAL_CANDIDATE.md`](FINAL_CANDIDATE.md)
- Human-review candidate SHA-256: `5256ab9406c49807239b227464e172bd6c60e5d5ca8b0c1d02d30be52bdd6960`

The unchanged holdout found no required structural revision.
The human-review candidate adds four wording clarifications and no new controlled term, relation, study family or product type.

## Holdout clarifications applied

1. **Valuation-scale transformation:** The mapping boundary now requires the exact task-to-scale path and prevents an instrument-mapping or economic-use false match.
2. **Response-process targets:** The measurement-property guidance now names response behavior, recall interpretation and instruction or perspective adherence as possible exact targets without forcing them into content validity.
3. **Proxy perspectives:** The guide now defines both numbered proxy perspectives in plain language and keeps requested perspective separate from observed response behavior.
4. **Documented effects:** The guide now requires the evidence provider and outcome level and separates staff-reported practice, observed workflow and measured participant or service outcomes.

## Backward check

The 40-paper harmonization table and ten holdout applications were checked for these four changes.

- Existing mapping, anchoring, scoring, QALY and economic-evaluation paths already use exact sources and outputs. No application needs a family change.
- Existing cognitive, qualitative, content-validity and proxy applications already keep exact targets. No result needs a forced property label.
- Existing proxy applications already separate respondent, referent and reported or missing perspective. No missing perspective receives an inferred value.
- Existing implementation applications already separate implication, pilot or routine use and observed effects. No reported impact changes level.

The clarifications improve extraction consistency and false-match control without changing the fit result for any of the 50 papers.

## Review package

- [`FINAL_CANDIDATE.md`](FINAL_CANDIDATE.md): ontology and extraction guide for human review.
- [`harmonization/HARMONIZATION.md`](harmonization/HARMONIZATION.md): 40-paper decisions and validation.
- [`holdout/APPLICATIONS.md`](holdout/APPLICATIONS.md): unchanged applications to ten new papers.
- [`holdout/FIT_REVIEW.md`](holdout/FIT_REVIEW.md): fit, question and probe checks.
- [`holdout/REVISION_PROPOSALS.md`](holdout/REVISION_PROPOSALS.md): clarifications and rejected additions.
- [`comparison/COMPARISON.md`](comparison/COMPARISON.md): anonymous three-lineage comparison.

Database design remains outside this experiment.
The next technical stage can translate the reviewed semantic guide and deterministic JATS metadata into a simple relational model.

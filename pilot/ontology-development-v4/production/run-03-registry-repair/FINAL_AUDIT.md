# Final repair audit

## Scope

This audit checks only the requested corrections for the 16 affected records. It uses this record precedence: `run-03-registry-repair`, then `run-02-repair`, then `run-01`. Each check uses the source article. Unrelated fields are outside this audit.

| Record | Final overlay | Verdict | Source check and confirmed repair | Remaining defect |
|---|---|---|---|---|
| `C50-P032` | run-02 | PASS | The protocol says that the two samples **will** include 400 and 1,000 respondents. Both are now `PLANNED_TARGET`. The 13 EQ-5D bolt-on questions are present with the exact source label and no inferred registry ID. | None. |
| `C50-P045` | run-03 | PASS | The stated aims support value-set development and health-state valuation. The extra method-evaluation purpose is gone. The four cTTO quality controls from Methods are separate uses. The Taiwan traditional-Chinese instrument version has no false base mapping. | None. |
| `R129-P001` | run-02 | PASS | The cTTO profiles, correction variants, and loss-aversion reference points remain in task design. No such item is a studied condition. Only retained analysis alternatives are comparators; interview mode is a stratifier. | None. |
| `R129-P106` | run-03 | PASS | Methods support a service-outcome study, not an implementation study. The implementation purpose, object, and outcome are gone. The source cohort (2,285), same-day exclusions (107), and three-of-14 service restriction are present. Parts are flat and inherit one complete study-wide design. The anxiety/depression dimension is separate and null-mapped. | None. |
| `R129-P038` | run-03 | PASS | The part is flat. The source flow is present: 248 left before allocation, 1,742 failed the quiz, 422 left later, and 2,577 of 4,989 entered analysis. The dimension-, construct-, and instrument-level multivariate models are separate uses. | None. |
| `R129-P018` | run-02 | PASS | The paper develops selection criteria; it does not assess protocol quality. The false purpose is gone. Translatability and cultural context are present as an extra consideration, not as checklist criterion 23. | None. |
| `R129-P014` | run-02 | PASS | The harmonization part has complete temporal, comparison, and allocation axes. The false implementation purpose is gone. The limitation records difficult clinical recruitment and the UK use of schoolchildren because separate NHS approval would cause delay. | None. |
| `CAL-B12` | run-03 | PASS | The source supports the five-patient pilot, follow-up times of 5.8 and 11.6 weeks, and communalities of 0.436 and 0.380. All are present. The administration conflict remains. CFA is now a `ModelUse`. | None. |
| `R129-P129` | run-03 | PASS | The parts are flat, and translation is a secondary purpose. The translation target, protocol, forward/back translation, and cognitive interviews are current-study work. The isiXhosa version has no false base mapping. Response distribution, ceiling/floor effects, and missingness are separate methods. The duplicate VAS regression method is gone; its model remains. | None. |
| `R129-P127` | run-02 | PASS | The title, stated aim, main analyses, and conclusion concern caregiver HRQoL, burden, and determinants. The prior MAJOR error is corrected: the family is `HEALTH_OUTCOME_RESEARCH`, with `OUTCOME_DESCRIPTION` first and measurement-property evaluation second. | None. |
| `R129-P064` | run-03 | PASS | The source uses paired 3L/5L data at baseline and follow-up in two cohorts. Each flat part now has complete effective design axes. Level-sum score is no longer a method; it is a `ScoringUse` for each instrument use. | None. |
| `C50-P049` | run-02 | PASS | Methods support one quantitative longitudinal part and one qualitative interview part. Both `StudyPart` records are flat, and the existing item links to these parts remain valid. | None. |
| `CAL-B03` | run-02 | PASS | Methods name an experimental Australian proxy EQ-HWB-9 (2022), version 1. That exact use is now null-mapped. The separate use of three items from the longer EQ-HWB keeps its valid base identity. | None. |
| `R129-P049` | run-03 | PASS | Methods specify separate univariate and multivariable censored linear regression models. Both remain as `ModelUse` records, and the duplicate compound method is gone. The adapted translated EQ-VT has no false standard-protocol mapping. | None. |
| `R129-P090` | run-03 | PASS | The article discusses better-than-dead as a scale and task concept. It is now a `Concept`, not a `MethodUse`. The separate TTO, DCE, SG, and VAS method uses remain. | None. |
| `R129-P110` | run-03 | PASS | Methods state that Welch's t-test was used for binary groups and Welch's ANOVA for other groups. They are now two separate, queryable method uses. | None. |

## Totals

- PASS: 16
- MINOR: 0
- MAJOR: 0

## Readiness

The 16 repaired overlays are ready for the next production gate. All requested planned-sample, purpose, sample-flow, flat-part/design, context, compound-split, type-repair, and version-mapping corrections are present and source-faithful. This result applies only to these repairs; it does not resolve unrelated registry queue items.

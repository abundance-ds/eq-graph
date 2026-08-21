# Source audit A

| Record | Verdict | Checked source locations | Material corrections | Missing important facts |
|---|---|---|---|---|
| C50-P032 | MINOR | Abstract; **Aims**; **Survey instrument**; **Data collection**; **Analysis** | `sam1` and `sam2` are planned targets, not `COMPLETED` samples. Remove the false completion state and use a gap for the planned sample stage if the record must keep these targets. | Add the planned use of 13 unnamed EQ-5D bolt-on questions. Keep the exact source label and do not infer their identities. |
| R129-P117 | PASS | Abstract; **Sampling and data collection**; **Instruments**; **Test-retest reliability**; **EQ-5D-5L population norms**; **WHOQOL-BREF population norm**; Discussion and limitations | None. | None. The record also preserves the source difference between 1,056 questionnaire completers and the 1,046 WHOQOL-BREF analysis sample. |
| C50-P045 | MINOR | Abstract; §2.2.2 **Valuation procedures**; §2.4 **Statistical analysis**; §3.3 **Modelling results**; Discussion and conclusions | Remove `VALUATION_METHOD_EVALUATION` as a separate purpose. The stated purpose is value-set development. Comparison and selection of estimation models are procedures for that purpose and are already recorded as `ModelUse` items. | None. The record captures the cTTO and DCE tasks, candidate models, selected hybrid model, product, sample flow, main values, and source-reported limitations. |
| C50-P028 | PASS | Abstract; **Literature Search**; **Study Selection, Data Extraction and Synthesis**; **Psychometric Properties**; **Quality Assessment/Risk of Bias**; Results; Discussion and conclusions | None. | None. The record preserves the source conflict between seven EQ-5D-5L studies in the abstract and eight in the main Results. |
| R129-P001 | MINOR | Abstract; **Experiment** subsections for cTTO, loss aversion, discounting, and validation; Results, Table 4; Discussion and limitations | Do not use `STUDIED_CONDITION` for EQ-5D profiles, correction variants, or loss-aversion reference points. Keep profiles and reference points in `TaskDesign`; use `COMPARATOR` for retained analysed alternatives. | None. The record captures both correction approaches, the validation task, interview mode, principal results, and the two Table 4 source conflicts. |
| CAL-B03 | PASS | Abstract; **Study design**; **Participants**; **Data collection**; **Analysis**; Results for recall and proxy perspective; Limitations and conclusions | None. | None. The record captures recruitment flow, exact EQ-HWB-9 version, three extra EQ-HWB items, administration, lived-experience review, main themes, and all stated limitations. |
| R129-P106 | MINOR | Background, final paragraph; **Data source**; **Measures**; **Statistical analysis**; three program Results sections; Tables 2–3; Discussion and conclusions | Keep study parts flat. `part2`–`part4` cannot be children of `part1`, and each part needs an effective design. Remove `IMPLEMENTATION_EVALUATION`, the implementation-object use, and the implementation outcome: the study uses routine PROM data for service evaluation but does not evaluate implementation. | Add the 2,285-record source cohort, the 107 same-day records excluded, and the restriction from 14 service types to the three with sufficient samples. |
| R129-P110 | PASS | Abstract; **Data collection**; **Analysis**; **The sample**; **Inequality**; **Comparison of 2022–2023 to 2012**; Discussion, limitations, and conclusions | None. | None. The record captures all three current surveys, the 611 DCE exclusions, the 2012 comparator, rescoring, inequality methods, principal values, and both source conflicts. |
| R129-P038 | MINOR | Abstract; **Data**; **Survey instrument**; all statistical-analysis subsections; Results; Discussion, limitations, and conclusions | Set the `StudyPart` object's `part_id` to null. | Add the reported attrition: 248 left before arm assignment, 1,742 failed the comprehension quiz, and 422 left during preference tasks or follow-up. This selection flow is important because only 2,577 of 4,989 recruits entered the psychometric analysis. |
| R129-P018 | MINOR | Abstract; Background; **Item selection criteria...** and Table 1; **Other considerations**; Conclusions; structured funding metadata | Remove `METHOD_OR_PROTOCOL_QUALITY` as a purpose. The paper develops a checklist but does not apply it to evaluate a method or protocol. | Add translatability and cultural context as an important additional item-selection consideration. Do not count it as a twenty-third checklist criterion. |

## Totals

- PASS: 4
- MINOR: 6
- MAJOR: 0

## Recurring patterns

- Three records promote a procedure or discussion topic to a separate research purpose or outcome.
- Two records use an invalid `StudyPart.part_id`; one also loses the effective design for three substantive parts.
- Two empirical records omit important participant-flow details.
- One protocol maps planned sample targets to completed samples because the sample-stage list has no planned state.
- One methods record uses `STUDIED_CONDITION` for task profiles and experimental alternatives rather than clinical study conditions.

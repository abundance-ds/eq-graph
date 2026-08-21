# Production calibration report

- Records: 20/20.
- Studies: 21.
- Unmapped registry labels: 2.
- Ontology gaps: 3.
- Source conflicts: 17.
- Deterministically valid records: 20/20.

## Dispositions

- `include-study`: 20.

## Primary research families

- `APPLIED_USE_RESEARCH`: 3.
- `EVIDENCE_SYNTHESIS`: 1.
- `HEALTH_OUTCOME_RESEARCH`: 3.
- `MEASUREMENT_PROPERTY_EVALUATION`: 7.
- `METHODS_RESEARCH`: 5.
- `POPULATION_REFERENCE_DESCRIPTION`: 1.
- `VALUE_SET_DEVELOPMENT`: 1.

## Ontology gaps

- `UNMODELED_ASPECT` `multi-Study finding relation`: Findings f1/f6, f2/f7, f3/f8, and f5/f12 use pooled data from Study 1 and Study 2. The schema permits only one study_id for each Finding, so each pooled finding is repeated under both studies.
- `UNMAPPED_VALUE` `comparison_structure`: The study compares frequency and severity response-scale formats. The controlled comparison-structure vocabulary has no value for a response-scale-format comparison.
- `UNMAPPED_VALUE` `function`: The paper proposes graphical reporting of health utility alongside mortality on Kaplan-Meier curves, but the method-function vocabulary has no reporting or visualization value.

## Source conflicts

- Denominator for the Study-2-only TTOown versus DTA analysis
- Reported MDC95 values for the EQ-5D index and EQ VAS
- Named EORTC QLQ-C30 domain associated with correlations of 0.70 and 0.64
- Whether the current study generated or analyzed data
- Model 2 refugee-versus-control coefficient
- Planned qualitative-sample allocation
- Adjusted association between education and EQ-5D-5L LSS
- Unadjusted EQ VAS difference by work status in Sweden
- Age distribution in the analyzed sample
- Designation of the referent and focal response-scale groups in the DIF analysis
- Meaning of the graded-response-model parameter a
- Standard deviation of the total-sample mean EQ-5D-5L index value
- Mean EQ VAS value reported for men
- Adjusted knee-register EQ VAS estimates at 1-year follow-up in table 4
- Adjusted spine-register EQ VAS change estimates in table 4
- Full-scale Hs values for the healthy, hearing-problems, and Norway subgroups
- Subgroup with the lowest reported full-scale HT value

## Registry review queue

- `CNF-P010` `ModelUse`: regression techniques
- `CNF-P018` `InstrumentUse`: EQ-5D proxy versions

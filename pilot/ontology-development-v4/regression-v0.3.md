# Version 0.3 blind regression across 45 papers

## Result

The compact ontology gives one primary family to each of the 45 studies.

No study needs a family gap.

The family partition is complete: 45 mapped studies, 0 duplicate family
assignments, and 0 unmapped studies.

The difficult boundaries remain stable after part-level application of
approach, allocation, time, comparison, and data axes.

All controlled values below are exact values from `VOCABULARY.tsv`.

## Family table

| Record | Primary family | First-ranked purpose |
|---|---|---|
| G109 | `VALUE_SET_DEVELOPMENT` | `VALUE_SET_DEVELOPMENT` |
| G101 | `HEALTH_PREFERENCE_RESEARCH` | `PREFERENCE_COMPARISON` |
| G125 | `POPULATION_REFERENCE_DESCRIPTION` | `POPULATION_NORMS` |
| G160 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| G195 | `MEASUREMENT_PROPERTY_EVALUATION` | `MEASUREMENT_PROPERTY_EVALUATION` |
| G010 | `APPLIED_USE_RESEARCH` | `DECISION_SUPPORT_DEVELOPMENT` |
| G196 | `INSTRUMENT_VERSION_DEVELOPMENT` | `TRANSLATION_AND_CULTURAL_ADAPTATION` |
| G116 | `INSTRUMENT_VERSION_DEVELOPMENT` | `CONTENT_VALIDITY_EVALUATION` |
| G131 | `APPLIED_USE_RESEARCH` | `IMPLEMENTATION_EVALUATION` |
| G014 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` |
| G083 | `HEALTH_ECONOMIC_EVALUATION` | `ECONOMIC_EVALUATION` |
| G015 | `MEASUREMENT_PROPERTY_EVALUATION` | `MEASUREMENT_PROPERTY_EVALUATION` |
| G168 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| G154 | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` |
| G146 | `VALUE_SET_DEVELOPMENT` | `VALUE_SET_DEVELOPMENT` |
| S002 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| S017 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| S024 | `METHODS_RESEARCH` | `MAPPING_OR_CROSSWALK` |
| S031 | `HEALTH_PREFERENCE_RESEARCH` | `PREFERENCE_COMPARISON` |
| S040 | `HEALTH_OUTCOME_RESEARCH` | `OUTCOME_DESCRIPTION` |
| S052 | `MEASUREMENT_PROPERTY_EVALUATION` | `CONTENT_VALIDITY_EVALUATION` |
| S057 | `APPLIED_USE_RESEARCH` | `DECISION_SUPPORT_DEVELOPMENT` |
| S058 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| S062 | `INSTRUMENT_VERSION_DEVELOPMENT` | `TRANSLATION_AND_CULTURAL_ADAPTATION` |
| S071 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` |
| S084 | `HEALTH_PREFERENCE_RESEARCH` | `PREFERENCE_COMPARISON` |
| S089 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| S091 | `HEALTH_OUTCOME_RESEARCH` | `OUTCOME_DESCRIPTION` |
| S099 | `HEALTH_OUTCOME_RESEARCH` | `OUTCOME_DESCRIPTION` |
| S100 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` |
| C001 | `VALUE_SET_DEVELOPMENT` | `VALUE_SET_DEVELOPMENT` |
| C002 | `INSTRUMENT_VERSION_DEVELOPMENT` | `INSTRUMENT_DEVELOPMENT` |
| C003 | `MEASUREMENT_PROPERTY_EVALUATION` | `CONTENT_VALIDITY_EVALUATION` |
| C004 | `HEALTH_OUTCOME_RESEARCH` | `OUTCOME_DESCRIPTION` |
| C005 | `ECONOMIC_BURDEN_RESEARCH` | `ECONOMIC_BURDEN_ESTIMATION` |
| C006 | `APPLIED_USE_RESEARCH` | `IMPLEMENTATION_EVALUATION` |
| C007 | `APPLIED_USE_RESEARCH` | `IMPLEMENTATION_EVALUATION` |
| C008 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| C009 | `METHODS_RESEARCH` | `METHOD_OR_PROTOCOL_QUALITY` |
| C010 | `VALUE_SET_DEVELOPMENT` | `VALUE_SET_DEVELOPMENT` |
| C011 | `HEALTH_PREFERENCE_RESEARCH` | `PREFERENCE_COMPARISON` |
| C012 | `INSTRUMENT_VERSION_DEVELOPMENT` | `INSTRUMENT_DEVELOPMENT` |
| C013 | `HEALTH_OUTCOME_RESEARCH` | `OUTCOME_DESCRIPTION` |
| C014 | `EVIDENCE_SYNTHESIS` | `EVIDENCE_SYNTHESIS` |
| C015 | `HEALTH_OUTCOME_RESEARCH` | `OUTCOME_DESCRIPTION` |

## Complete partition

Counting unit: distinct mapped study. Denominator: 45 studies.

| Primary family | Count |
|---|---:|
| `VALUE_SET_DEVELOPMENT` | 4 |
| `MEASUREMENT_PROPERTY_EVALUATION` | 4 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | 5 |
| `POPULATION_REFERENCE_DESCRIPTION` | 1 |
| `METHODS_RESEARCH` | 9 |
| `APPLIED_USE_RESEARCH` | 5 |
| `EVIDENCE_SYNTHESIS` | 4 |
| `HEALTH_ECONOMIC_EVALUATION` | 1 |
| `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` | 1 |
| `HEALTH_OUTCOME_RESEARCH` | 6 |
| `HEALTH_PREFERENCE_RESEARCH` | 4 |
| `ECONOMIC_BURDEN_RESEARCH` | 1 |
| Family gap | 0 |
| **Total** | **45** |

## Part-level axes

Each line gives: approach; allocation; time; comparison; and data
origin/data level. A plus sign joins supported multi-value axes. A semicolon
separates study parts.

- **G109:** valuation and modeling — `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Abstract; Methods).

- **G101:** secondary cross-country DCE analysis — `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_CONTEXT`; `PRIOR_RESEARCH_COLLECTION`/`PARTICIPANT_RESPONSE` (Abstract; Methods, Data collection and Analysis).

- **G125:** Italian norms — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/ `PARTICIPANT_RESPONSE`; country comparison — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_CONTEXT`; `DOCUMENTARY_SOURCE`/`AGGREGATE_ESTIMATE` (Methods; Data Analysis).

- **G160:** pattern development — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `PRIOR_RESEARCH_COLLECTION`/ `QUALITATIVE_MATERIAL`; interviewer scoring — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON` + `BETWEEN_METHOD`; `PRIOR_RESEARCH_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods; Data Collection and Study Population).

- **G195:** dyad measurement study — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `WITHIN_DYAD` + `WITHIN_PERSON` + `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/ `PARTICIPANT_RESPONSE` + `ROUTINE_SERVICE_COLLECTION`/`DOCUMENT` (Methods; Study design and setting; Data collection).

- **G010:** pre-surgery and post-surgery visualization parts — each uses `QUANTITATIVE_EMPIRICAL` + `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `WITHIN_PERSON` + `BETWEEN_INSTRUMENT`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` + `QUALITATIVE_MATERIAL` (Methods; Results, Parts 1 and 2).

- **G196:** translation workflow — `TRANSLATION_ADAPTATION_WORKFLOW`; `NOT_APPLICABLE`; `NOT_APPLICABLE`; `BETWEEN_INSTRUMENT`; `DOCUMENTARY_SOURCE`/`DOCUMENT`; cognitive debriefing — `TRANSLATION_ADAPTATION_WORKFLOW` + `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_INSTRUMENT`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods).

- **G116:** expert consultation — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/ `QUALITATIVE_MATERIAL` (Abstract; Methods, Procedure).

- **G131:** workshops and interviews — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Aim and Methods; Workshop and Interview procedures).

- **G014:** systematic review and meta-analysis — `EVIDENCE_SYNTHESIS` + `MODEL_BASED`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_GROUP` + `BETWEEN_INSTRUMENT` + `BETWEEN_CONTEXT`; `REVIEW_EXTRACTED_EVIDENCE`/`AGGREGATE_ESTIMATE` (Materials and methods; Statistical analysis).

- **G083:** non-diabetic and diabetic Markov parts — each uses `MODEL_BASED`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `BETWEEN_GROUP` + `BETWEEN_INSTRUMENT` + `BETWEEN_METHOD`; `PUBLISHED_MODEL_INPUT`/ `MODEL_PARAMETER` + `PRIOR_RESEARCH_COLLECTION`/`AGGREGATE_ESTIMATE` + `SIMULATED_DATA`/`SIMULATED_UNIT` (Decision analytic models; Analysis).

- **G015:** routine PROM cohort — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON` + `BETWEEN_INSTRUMENT` + `BETWEEN_GROUP`; `ROUTINE_SERVICE_COLLECTION`/ `PARTICIPANT_RESPONSE` + `DOCUMENT` (Materials and Methods, 2.1-2.4).

- **G168:** quantitative DCE-feasibility part — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE`; focus-group part — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL`; integration is `CONVERGENT_PARALLEL` (Methods and analysis).

- **G154:** taxonomy development — `CONCEPTUAL`; `NOT_APPLICABLE`; `NOT_APPLICABLE`; `NONCOMPARATIVE`; `CONCEPTUAL_MATERIAL`/`DOCUMENT` (Abstract; Conclusions).

- **G146:** DCE and cTTO samples — each uses `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Data Collection; Analysis).

- **S002:** protocol comparison — `CONCEPTUAL`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_METHOD`; `DOCUMENTARY_SOURCE`/`DOCUMENT` + `CONCEPTUAL_MATERIAL`/`DOCUMENT` (The EuroQol Valuation Protocols).

- **S017:** personal utility function pilot — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Sample and administration of survey).

- **S024:** crosswalk analysis — `MODEL_BASED`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_METHOD` + `BETWEEN_INSTRUMENT` + `BETWEEN_CONTEXT`; `PRIOR_RESEARCH_COLLECTION`/`AGGREGATE_ESTIMATE` (Methods).

- **S031:** think-aloud PTO study — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP` + `BETWEEN_CONTEXT`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods, 2.1-2.4).

- **S040:** cancer utility analysis — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Materials and Methods, 2.1-2.3).

- **S052:** concept elicitation and cognitive debriefing — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP` + `BETWEEN_INSTRUMENT`; `CURRENT_STUDY_COLLECTION`/ `QUALITATIVE_MATERIAL` (Methods; Study design; Procedures).

- **S057:** co-design process — `PARTICIPATORY_DESIGN`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `NONCOMPARATIVE`; `CURRENT_STUDY_COLLECTION`/ `QUALITATIVE_MATERIAL` (Methods; Data collection; Final prototype).

- **S058:** domain-selection method — `CONCEPTUAL`; `NOT_APPLICABLE`; `NOT_APPLICABLE`; `BETWEEN_METHOD`; `CONCEPTUAL_MATERIAL`/`DOCUMENT` + `DOCUMENTARY_SOURCE`/`DOCUMENT` (Abstract; Options; Adopted approach).

- **S062:** cultural-adaptation part — `TRANSLATION_ADAPTATION_WORKFLOW`; `NOT_APPLICABLE`; `NOT_APPLICABLE`; `BETWEEN_INSTRUMENT`; `DOCUMENTARY_SOURCE`/`DOCUMENT` + `CURRENT_STUDY_COLLECTION`/ `QUALITATIVE_MATERIAL`; content-validity part — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods; Procedures).

- **S071:** systematic review — `EVIDENCE_SYNTHESIS`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_INSTRUMENT`; `REVIEW_EXTRACTED_EVIDENCE`/`AGGREGATE_ESTIMATE` (Methods; Data Sources and Study Selection).

- **S084:** bolt-on face-validity part — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_INSTRUMENT`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL`; choice-survey part — `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `WITHIN_PERSON` + `BETWEEN_INSTRUMENT`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods).

- **S089:** UK pilot — `QUANTITATIVE_EMPIRICAL`; `RANDOMIZED`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; `CURRENT_STUDY_COLLECTION`/ `PARTICIPANT_RESPONSE`; 15-country rollout — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_CONTEXT`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods).

- **S091:** POPCORN cohort — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON` + `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Materials and methods; Study design and population).

- **S099:** two survey waves — each uses `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Study Design and Data Collection).

- **S100:** systematic review — `EVIDENCE_SYNTHESIS`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_METHOD`; `REVIEW_EXTRACTED_EVIDENCE`/ `DOCUMENT` (Methods, Trial Identification through Data Synthesis).

- **C001:** valuation and modeling — `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods).

- **C002:** short-form development — `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_INSTRUMENT`; `PRIOR_RESEARCH_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Sources of data; Statistical methods).

- **C003:** proxy appropriateness interviews — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods; Sample and Recruitment; Procedure).

- **C004:** adolescent health analysis — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `PRIOR_RESEARCH_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Study design).

- **C005:** NESTT input part — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `PRIOR_RESEARCH_COLLECTION`/`PARTICIPANT_RESPONSE` + `DOCUMENT`; burden model — `MODEL_BASED`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `PRIOR_RESEARCH_COLLECTION`/`AGGREGATE_ESTIMATE` + `PUBLISHED_MODEL_INPUT`/`MODEL_PARAMETER` (Methods; Statistical methods).

- **C006:** hip and knee cohorts — each uses `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `BETWEEN_GROUP`; `ROUTINE_SERVICE_COLLECTION`/`DOCUMENT` (Methods; Inclusion criteria).

- **C007:** implementation interviews — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods; Study design; Data collection).

- **C008:** planned PTO survey — `QUANTITATIVE_EMPIRICAL`; `RANDOMIZED`; `CROSS_SECTIONAL`; `WITHIN_PERSON` + `BETWEEN_GROUP` + `BETWEEN_CONTEXT`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE`; planned interviews and focus groups — `QUALITATIVE_INQUIRY`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_GROUP` + `BETWEEN_CONTEXT`; `CURRENT_STUDY_COLLECTION`/`QUALITATIVE_MATERIAL` (Methods, 2.3-2.10).

- **C009:** evidence foundation — `EVIDENCE_SYNTHESIS`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `NONCOMPARATIVE`; `REVIEW_EXTRACTED_EVIDENCE`/ `DOCUMENT`; Delphi and survey — `PARTICIPATORY_DESIGN` + `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `NONCOMPARATIVE`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods, CREATE Development).

- **C010:** valuation and modeling — `QUANTITATIVE_EMPIRICAL` + `MODEL_BASED`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_METHOD`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods).

- **C011:** perspective experiment — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `WITHIN_PERSON` + `BETWEEN_METHOD` + `BETWEEN_CONTEXT`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Experimental procedure and design).

- **C012:** bolt-on development — `CONCEPTUAL` + `PARTICIPATORY_DESIGN`; `NOT_APPLICABLE`; `NOT_APPLICABLE`; `BETWEEN_INSTRUMENT`; `DOCUMENTARY_SOURCE`/`DOCUMENT` + `CURRENT_STUDY_COLLECTION`/ `QUALITATIVE_MATERIAL`; psychometric survey — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `CROSS_SECTIONAL`; `BETWEEN_INSTRUMENT` + `BETWEEN_GROUP`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Development and selection; Cross-sectional survey).

- **C013:** ESMI and EUROSCA cohort parts — each uses `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON` + `BETWEEN_GROUP` + `BETWEEN_CONTEXT`; `PRIOR_RESEARCH_COLLECTION`/`PARTICIPANT_RESPONSE` (Methods; Study Design, Recruitment, and Sample).

- **C014:** systematic review — `EVIDENCE_SYNTHESIS`; `NOT_APPLICABLE`; `VARIABLE_SOURCE_TIME`; `BETWEEN_CONTEXT` + `BETWEEN_METHOD`; `REVIEW_EXTRACTED_EVIDENCE`/`DOCUMENT` (Methods; Data sources; Analysis).

- **C015:** POPCORN cohort — `QUANTITATIVE_EMPIRICAL`; `NOT_APPLICABLE`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON` + `BETWEEN_GROUP` + `BETWEEN_CONTEXT`; `CURRENT_STUDY_COLLECTION`/`PARTICIPANT_RESPONSE` (Material and Methods, 2.1-2.3).

## Focused checks of version 0.3

### Part structure and data origin

- Separate parts prevent mixed-origin values in G125, G160, G196, G146, S062, S084, S089, C005, C008, C009, C012, and C013.
- G015 uses routine PROM and clinical-record data. It does not use `CURRENT_STUDY_COLLECTION` or `PRIOR_RESEARCH_COLLECTION` for that part.
- C006 uses Medicare claims as `ROUTINE_SERVICE_COLLECTION`/`DOCUMENT`.
- G083 keeps prior estimates, published parameters, and simulated units as three DataUse records.
- Review papers use `REVIEW_EXTRACTED_EVIDENCE`. They do not inherit the current-study context of the reviewed studies.

### Allocation and task design

- C008 has `RANDOMIZED` allocation because people are assigned to the forced or unforced study arms.
- The S089 pilot has `RANDOMIZED` allocation because people are assigned to survey versions that the study compares.
- Random health-state order, left/right order, or valuation blocks in G109, G101, G146, S084, C001, C010, and C011 remain in TaskDesign. They do not create `RANDOMIZED` study allocation.
- Observed treatment or practice groups in G015 and C006 do not create `NONRANDOMIZED` allocation because the studies do not assign those groups.

### Participatory design and stakeholder involvement

- S057 supports `PARTICIPATORY_DESIGN`: service users and providers jointly create and refine the P-PROM ROCK Program through workshops and later optimization sessions.
- C009 supports `PARTICIPATORY_DESIGN`: the Delphi panel and survey refine and select CREATE checklist items.
- C012 supports `PARTICIPATORY_DESIGN` only for the bolt-on development part. Its psychometric survey remains `QUANTITATIVE_EMPIRICAL`.
- G116 reports expert consultation, but it does not show that the experts made the final content decision. It remains `QUALITATIVE_INQUIRY`.
- Ordinary patients, respondents, and interviewees do not become stakeholder involvement records without a reported activity and influence.

### Factors and comparisons

- G195 uses `WITHIN_DYAD` for child/caregiver reports and `WITHIN_PERSON` for admission/discharge. These axes do not collapse into one comparison value.
- S099 uses `TARGET_STAGE` for pregnancy and postpartum stage. Its two survey waves remain `CROSS_SECTIONAL` because the same people are not followed.
- C004 supports StudyFactor records for sex, age, comorbidity, mental distress, and parent occupational status. These factors do not turn the paper into a measurement-property study.
- C006 supports determinants of PNB use and PNB use as a studied practice. The observed practice group remains a `BETWEEN_GROUP` comparison.
- C011 keeps valuation perspective, target age, health-state severity, and valuation method on separate factor, administration, and comparison axes.
- C013 and C015 support longitudinal determinants without adding new family values.

### State and product separation

- G168 is a `PROTOCOL_ARTICLE`. At the source date, data collection is complete but analysis has not begun. Use `DATA_COLLECTION_COMPLETE` and `NO_RESULTS_YET`.
- C008 is a `PROTOCOL_ARTICLE` with `PLANNED` execution and `NO_RESULTS_YET`.
- C010 is an `ORIGINAL_RESEARCH_ARTICLE` with `COMPLETED` execution and `RESULTS_REPORTED`. Add the separate `RETRACTED` publication assertion.
- Retraction of C010 does not prove withdrawal or invalidity of its value-set product. The source gives no product-state assertion of that type.
- C009 produces a `CHECKLIST_OR_TOOL`. S057 produces implementation and decision-support resources. C002 and C012 produce `INSTRUMENT_VERSION` products.

### Family boundaries

- G125 states norms as the main output and maps to `POPULATION_REFERENCE_DESCRIPTION`.
- C004 presents population health by factors but does not state norms or reference data as its main output. It maps to `HEALTH_OUTCOME_RESEARCH`.
- C006 studies use and provision of PNBs first, with complications and stay as secondary outcomes. It maps to `APPLIED_USE_RESEARCH`.
- G083 compares costs and consequences of dialysis alternatives. It remains `HEALTH_ECONOMIC_EVALUATION` despite its mapping-method emphasis.
- C005 estimates attributable burden without decision alternatives. It maps to `ECONOMIC_BURDEN_RESEARCH`.
- C015 has a health-behavior outcome and maps to `HEALTH_OUTCOME_RESEARCH`. It does not need a health-behavior primary family.

## Material close calls

- **G010:** `METHODS_RESEARCH` is plausible because the paper tests data displays. `APPLIED_USE_RESEARCH` is stronger because the main output is a presentation within a patient decision aid for routine care.
- **G116:** `MEASUREMENT_PROPERTY_EVALUATION` is plausible because experts assess content validity. `INSTRUMENT_VERSION_DEVELOPMENT` is stronger because the stated development work and proposed content changes define the paper.
- **G083:** `METHODS_RESEARCH` is plausible because mapped utilities are the methodological focus. `HEALTH_ECONOMIC_EVALUATION` is stronger because two dialysis alternatives have costs, QALYs, and ICERs.
- **S024:** `HEALTH_PREFERENCE_RESEARCH` is plausible because value sets are compared. `METHODS_RESEARCH` is stronger because interchangeability and method choice are the main decision.
- **S058:** `INSTRUMENT_VERSION_DEVELOPMENT` is plausible because EQ-HWB is the application. `METHODS_RESEARCH` is stronger because the stated aim is to choose an approach for domain identification.
- **C004:** `POPULATION_REFERENCE_DESCRIPTION` is plausible because the sample is population based. The stated output is health status by determinants, not norms or reference data, so `HEALTH_OUTCOME_RESEARCH` is stronger.
- **C008:** `HEALTH_PREFERENCE_RESEARCH` is plausible for the planned empirical study. `METHODS_RESEARCH` is stronger for this publication because its main output is a tested PTO protocol and task design.
- **C012:** `MEASUREMENT_PROPERTY_EVALUATION` is plausible because the survey tests psychometric performance. `INSTRUMENT_VERSION_DEVELOPMENT` is stronger because new dining and gastrointestinal bolt-ons are explicit main outputs.
- **S100:** `METHODS_RESEARCH` is plausible because the subject is analysis methods. `EVIDENCE_SYNTHESIS` is stronger because systematic combination of 2,125 prior trials is the paper's main output.

None of these close calls requires `UNCERTAIN_MAPPING`. The stated aim, main
decision, product, and conclusion give one stronger family in each case.

## Source conflicts

- **G109, Methods, Valuation techniques:** the text calls the DCE design “196 health states” but also gives 28 blocks of seven choice pairs. The latter arithmetic gives 196 pairs. Preserve both statements and do not repair the TaskDesign count.
- **G195, Abstract Results versus full Results:** the abstract says 957 dyads participated. The full Results says 985 dyads participated and 957 were analyzed. Preserve both sample-stage statements.
- **G116, Results, Sample characteristics:** the paper reports 44 invited experts, but the three reported invited group counts are 21, 13, and 9, which sum to 43. Preserve the total and group counts.
- **S057, Abstract Results versus Results, Participants:** the abstract reports nine service providers. The full Results reports 11 service providers. Preserve both participation counts.
- **C006, Abstract Methods versus full Methods and Results:** the abstract gives 52,926 hip and 94,795 knee cases, and the full Methods gives 147,721 patients. The Results gives 52,000 hip and 93,448 knee cases. Preserve all counts and locators.
- **C013, Abstract Methods and Sample Selection:** the cohort counts are 525 and 310, which sum to 835. Sample Selection calls the same group 842 patients. Preserve the stated total and component counts.
- **C014, Results versus Source of preference data:** the paper repeatedly reports 4,052 HSUs, but Source of preference data uses 4,025 as the denominator. Preserve both denominators.

## New gaps

No new controlled-value or structural gap occurred.

The seven contradictions above are `SourceConflict` records, not gaps.
Ordinary absence on a required field can still use `NOT_REPORTED`, but no such
absence changes a family or a version-0.3 boundary in this regression.

## Stability verdict

**Stable for the 45-paper regression.**

Version 0.3 gives a complete primary-family partition and supports all observed
part-level approach, allocation, time, comparison, and data-origin patterns.
The additions for participatory design, StudyFactor, within-dyad comparison,
publication status, study/result state, product state, health behavior, and
economic burden work without expansion.

The next confirmation batch can use version 0.3 without an ontology change.
The seven source conflicts must remain explicit during later extraction.

## Exact input verification

Verification recomputed SHA-256 over the article bytes. Each actual byte count
and digest matches its manifest value.

| Record | Bytes | SHA-256 | Match |
|---|---:|---|---|
| G109 | 73318 | `06cd47ce7b8c4e8d26327e3407a25539e756606d602863d3d907f73fd8c71dc7` | yes |
| G101 | 57070 | `b74d1da3c908098efdcdb1f163991e4cc891ea8737c285ddf5b5ea1c3665186b` | yes |
| G125 | 132749 | `a7845f657f23302e62c6915868cbcf0c8530bab59d535c2ddd02031a21b3d02f` | yes |
| G160 | 62604 | `dd0eab4abc6332fc9965a9e57ff912ee12fa04bd7b6f6e9f6836cb54f1a8094f` | yes |
| G195 | 95266 | `544b05d801a8cf385f60d4784e189a2bd1bb54e8148c9072199907de1e38775c` | yes |
| G010 | 57114 | `866438ce4bdc844c0cc7a3929828e48acfe2aab09c5d6b7461a5fec9219f4997` | yes |
| G196 | 49236 | `975b85316c338820d1694979d7df6a5fde53cfa68dc0bfab4a9609330c958d7f` | yes |
| G116 | 101717 | `84b48b2cb480dfcce2baff045168cea58615e2e013c0c9a5d31243c1c6e472be` | yes |
| G131 | 70997 | `fb4d743f9a0e75d57decc78b76c41075602e60ef190ae1c99d2df742b6f455ec` | yes |
| G014 | 219415 | `4537712ebff158ad24bb9a223e9000698a6355d4538599d3bb44287adc91f7e5` | yes |
| G083 | 39487 | `fc488afa7b1a983ed266cae605368061b0e9fb85c5648b5e2a1ee89cec5aa645` | yes |
| G015 | 92054 | `988ed7c0fbcde3d5739aa46e55f11b691a9cf0cfc7adaa248e24427f931a764a` | yes |
| G168 | 48411 | `21f3eb92df6f2e28b4fa4d44f0559ef20deb1192ab09cfe164c764142621f53d` | yes |
| G154 | 43713 | `5458440de4fda7b5d6a24520f6806e84f8655377b767d63a053525ddced5fe11` | yes |
| G146 | 61466 | `2d9a0b8e02c0f5c456e661027b22c536aed26c1a76529ec00e1001cb8fd003f2` | yes |
| S002 | 56286 | `467cb82e557941064c134149dbaf410ed7cffd108084fcd2507a051db5c532c9` | yes |
| S017 | 80616 | `9a859cd03aa3256bbd52a6fac01749ca85e7d878770f3d212d83ce3ec304a741` | yes |
| S024 | 68428 | `de0405964ea0d43d90d3fa0acc825ce046c65bff84aef08a44942b8040365452` | yes |
| S031 | 163225 | `87a2c313ac7b1cdde3152331e303e0015897a8f79614135163db1d1f16701e70` | yes |
| S040 | 58691 | `c56fde022f3c5b0ab1a9fe9a206c95f38c6f711c734b82bb98778c78058e1ba4` | yes |
| S052 | 64852 | `f8d32a59a6e392759fc0c38accaee1b28f75699d4ff172abdcc62c41f4c4719f` | yes |
| S057 | 69560 | `5e7dd427dd3e9ecb19ee3957b0623b7b932aa6d983274de82d67e97340ed5464` | yes |
| S058 | 92752 | `3fd5eca21b9429c79f5c0947e286ee07919dea027a79fd7f4a03fd45cd902b0b` | yes |
| S062 | 52978 | `9ee7dfff9c287e3c6dd4abab83be9d2f3d32ca4212aa8fae20b4b93c39a717f0` | yes |
| S071 | 84553 | `2db101c7ed9e576690145c64ba93fbb06f684053fb8ed9af2058f27508d0b6fa` | yes |
| S084 | 65568 | `3ae3da8629d8b0716d2e0a96569796b3bf81b1eb5c5c13fe54038d2d46676d99` | yes |
| S089 | 90076 | `228dc3ca0c53db29e5f6de64f2702c80bcdf1e110f3a67319d213c77b3859e02` | yes |
| S091 | 82786 | `5f3bd0b79e50eb3cc64cc38855dc6166f24d0376f5cf183e648cb1d8459485c3` | yes |
| S099 | 50592 | `a3b76abaf1369572ffe8c9a3fd3d132e04aef1abb93c8730546f5020fc85320b` | yes |
| S100 | 50386 | `45d9c8ae457cb963d4fb0be5882c72526e7fbcff050b234d29f5bbe94719f2ac` | yes |
| C001 | 48419 | `ce4008f8960d9f27e76693f2f31fd1b2b043c3b86ccef599e799a745c444849f` | yes |
| C002 | 49434 | `5266d9a9ea95e329ff9e5e1e46f124ffe129051b75fd16ce030459f108d798fe` | yes |
| C003 | 62053 | `19259d3a21512fdd2c1e447fe6e44febcbd2388f57eabe3431d298282c222d05` | yes |
| C004 | 71162 | `363625c754d379c479f786321eb244e48678aacfa36d92fe001dd38ac3247539` | yes |
| C005 | 71413 | `6a27dd1b66faeb7e4095b044a2f9b8df67dc165bf02ff8811dbcc59b536643d6` | yes |
| C006 | 93921 | `46894a0a2caf783ddeed15e6c822abcc1444a18dc7b1ad824a631c826f233f5a` | yes |
| C007 | 77245 | `171009067ec3beb38d0342b099ed4a4172530dea123ad3a96a6a5907bfd95ba1` | yes |
| C008 | 188611 | `9420b24805f77c45e43b06a4d79dde1108b29b495b94d16550687f99631dcbb5` | yes |
| C009 | 55363 | `183a6da25535bfd5f18299dc5aa2c40eea8e4b804bf42793efda1eb3a62ae76c` | yes |
| C010 | 94816 | `f16bf7a38694b56920da191a401bb044d65a40b646a083e7fd2139a5fca87322` | yes |
| C011 | 63193 | `57250a97f739fa5d4c81b213313ae376cc98f670ef1f80444769917babf91e0d` | yes |
| C012 | 101030 | `7ca37497aa5ba3a9bab94fe0156583e85bd35a99d4934ff5af8381837dda5394` | yes |
| C013 | 64795 | `ba3549249f6cd84bf6aea4d81fd2cf43e6024a192e0c9ede4d0451c2ffb36a93` | yes |
| C014 | 50150 | `b2083bc30a6caf142e5ea44beb9a49f3d4bfb500e10f6c8158ee2dfdc88eee01` | yes |
| C015 | 82631 | `8b7cca005d2c1fa9631f3981fddf0945e20dfa67678fc845fd73f939bddb73a9` | yes |

Aggregate verification: 45 files, 3,510,202 bytes, 45 byte-count
matches, and 45 SHA-256 matches.

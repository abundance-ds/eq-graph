# Round 04 application A

Ontology version 0.3 and `VOCABULARY.tsv` were applied without additions or changes. The counting unit for the partition is the distinct study, and the denominator is 15.

- Family partition: `VALUE_SET_DEVELOPMENT` D005; `MEASUREMENT_PROPERTY_EVALUATION` D008; `INSTRUMENT_VERSION_DEVELOPMENT` D003; `METHODS_RESEARCH` D001, D004, D010, and D013; `APPLIED_USE_RESEARCH` D006 and D014; `EVIDENCE_SYNTHESIS` D002; `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` D007, D011, and D012; `HEALTH_OUTCOME_RESEARCH` D015; `HEALTH_PREFERENCE_RESEARCH` D009.
- Zero-count families are `POPULATION_REFERENCE_DESCRIPTION`, `HEALTH_ECONOMIC_EVALUATION`, and `ECONOMIC_BURDEN_RESEARCH`; no study has a family gap. All 15 article byte counts and SHA-256 values agree with `round-04.tsv`, and each paper record gives the exact check.

## D001 — Test-retest reliability of the Online Elicitation of Personal Utility Functions (OPUF) approach for valuing the EQ-HWB-S

### Assessment and classification

- Primary family: `METHODS_RESEARCH`. Purposes: `VALUATION_METHOD_EVALUATION`, `METHOD_OR_PROTOCOL_QUALITY`, and `HEALTH_STATE_VALUATION`. The main decision is the test-retest reliability of OPUF, not the development of the EQ-HWB-S. (Abstract—Introduction; Conclusion)
- Design: `QUANTITATIVE_EMPIRICAL`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Materials and methods—Sample; Test-retest)
- Input verification: `corpus/1508-RA/doi_10.1007_s10198-025-01769-4.md`; 78,866 bytes; SHA-256 `5aeb8d6b2307857d7cfd092368a992685d86ab149249d8db3b4d03dc4468c324`.

### Study structure and typed uses

- One study has test and retest time points two weeks apart. It enrolled 330 people, 257 completed the retest, and 220 were analyzed: 73 general-population participants and 147 patients with diabetes or rheumatic disease. (Materials and methods—Sample; Results—Sample characteristics)
- Data use: `CURRENT_STUDY_COLLECTION` at `PARTICIPANT_RESPONSE` level. Study factors are sample group, age, and gender; their roles are `STRATIFIER` or `EXPOSURE_OR_DETERMINANT` as analyzed. (Materials and methods—Sample; Impact of other factors on test-retest)
- Instrument use: exact label `EQ-HWB-S`, context `DIRECT_CURRENT_ACTIVITY`, functions `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`; exact label `adapted version of the EQ-VAS`, function `CURRENT_HEALTH_MEASUREMENT`. (Materials and methods—Preference elicitation survey)
- Method uses: exact labels `Online elicitation of Personal Utility Functions (OPUF)`, `intraclass correlation coefficient (ICC)`, `Spearman’s rank correlation coefficient`, `unweighted kappa statistic`, `paired t-test`, and `two-sample Kolmogorov-Smirnov test`; OPUF has `PREFERENCE_ELICITATION`, and the other methods have `QUANTITATIVE_ANALYSIS`. (Materials and methods—Preference elicitation survey; Data analysis)

### Findings, limitations, products, and concepts

- Outcome families are `METHOD_PERFORMANCE_OR_DATA_QUALITY` and `PREFERENCE_OR_UTILITY`. Individual task agreement was mainly poor to moderate, while the pairwise anchoring choice had kappa about 0.6 and about 83% agreement. (Abstract—Results; Discussion)
- Aggregate utility decrements were similar across test and retest, but individual utility decrements and final health-state ranks were not stable. The final rank correlation was 0.26. (Results—Utility decrements and value set; Discussion)
- Reported limitations include exclusion of illogical or indifferent responses, VAS response bias, online-panel digital-literacy selection, limited generalizability from Germany, and poor comparability with conventional reliability tests. Two analytical OPUF EQ-HWB-S value sets map to `VALUE_SET`; no approval or deployment is reported. Concepts include individual and aggregate reliability, anchoring, digital literacy, and respondent engagement. (Materials and methods—Utility decrements and value set; Discussion)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. Keep the initial, retest, and analyzed sample stages separate; 220 is not the enrollment count. (Results—Sample characteristics)

### High-value canonical terms

- Controlled: `METHODS_RESEARCH`, `VALUATION_METHOD_EVALUATION`, `METHOD_OR_PROTOCOL_QUALITY`, `LONGITUDINAL_REPEATED`, `WITHIN_PERSON`, and `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Registry: `Online elicitation of Personal Utility Functions (OPUF)`, `EQ-HWB-S`, `adapted version of the EQ-VAS`, `intraclass correlation coefficient (ICC)`, and `Spearman’s rank correlation coefficient`.

## D002 — Measurement Properties of Commonly Used Generic Preference-Based Measures in East and South-East Asia: A Systematic Review

### Assessment and classification

- Primary family: `EVIDENCE_SYNTHESIS`. Purposes: `EVIDENCE_SYNTHESIS` and `MEASUREMENT_PROPERTY_EVALUATION`. The paper systematically combines evidence about construct validity, test-retest reliability, and responsiveness. (Abstract—Objectives; Conclusions)
- Design: component approach `EVIDENCE_SYNTHESIS`; synthesis designs `SYSTEMATIC_REVIEW` and `NARRATIVE_SYNTHESIS`; temporal structure `VARIABLE_SOURCE_TIME`; allocation `NOT_APPLICABLE`. Publication form is `REVIEW_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods)
- Input verification: `corpus/2016230/doi_10.1007_s40273-019-00854-w.md`; 113,530 bytes; SHA-256 `68f45ea10e7e3e77cad9ebad14637b5c1f2f2109e34b67f380cce6c050127b6c`.

### Study structure and typed uses

- One review includes 79 papers and 1,504 COSMIN-defined study units. A unit is one tested hypothesis, ICC, or standardized effect-size result, so it is not a publication count. (Methods—Data Extraction; Results)
- Data use: `REVIEW_EXTRACTED_EVIDENCE` at `DOCUMENT` and `AGGREGATE_ESTIMATE` levels. Sample stage is `INCLUDED_EVIDENCE`. (Methods—Identification and Selection of Studies; Data Extraction)
- Instrument uses, all in `CURRENT_STUDY_OBJECT` context with `EVIDENCE_SYNTHESIS_TARGET`, have exact labels `EQ-5D-3L`, `EQ-5D-5L`, `EQ-VAS`, `SF-6D`, `HUI2`, `HUI3`, `QWB`, `15D`, and `AQOL`. (Methods—Identification and Selection of Studies; Assessment of the PBMs)
- Protocol use: exact label `COnsensus-based Standards for the selection of health Measurement Instruments (COSMIN) guideline`, context `DIRECT_CURRENT_ACTIVITY`, functions `GOVERNING_STUDY_PROTOCOL` and `CRITICAL_APPRAISAL_PROTOCOL`. Methods include database searching, hypothesis testing, risk-of-bias assessment, and modified GRADE assessment. (Methods)

### Findings, limitations, products, and concepts

- The review found `EQ-5D` to have sufficient construct validity and responsiveness in many populations. It found its test-retest reliability inconsistent or insufficient in almost all assessed populations. (Abstract—Results; Discussion)
- Evidence for `SF-6D` and `EQ-VAS` construct validity was inconsistent in some populations. Evidence for HUI and QWB was scarce, although available evidence supported HUI use. (Abstract—Results; Conclusions)
- Reported limitations were modifications to COSMIN methods, exclusion of non-English journal papers, and aggregation across language versions. No explicit reusable product is reported. Concepts include construct validity, test-retest reliability, responsiveness, methodological quality, and population-specific measurement performance. (Discussion; Methods—Assessment of the PBMs)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. Aggregation must retain the source-defined distinction between 79 papers and 1,504 study units. (Methods—Data Extraction)

### High-value canonical terms

- Controlled: `EVIDENCE_SYNTHESIS`, `SYSTEMATIC_REVIEW`, `REVIEW_EXTRACTED_EVIDENCE`, `INCLUDED_EVIDENCE`, and `MEASUREMENT_PROPERTY`. Registry: `COnsensus-based Standards for the selection of health Measurement Instruments (COSMIN) guideline`, `EQ-5D-3L`, `EQ-5D-5L`, `EQ-VAS`, `SF-6D`, `HUI2`, `HUI3`, `QWB`, `15D`, and `AQOL`.

## D003 — Cross-cultural adaptation and psychometric validation of the Chichewa (Malawi) PedsQL 4.0 Generic Core Scales

### Assessment and classification

- Primary family: `INSTRUMENT_VERSION_DEVELOPMENT`. Purposes: `TRANSLATION_AND_CULTURAL_ADAPTATION`, `INSTRUMENT_DEVELOPMENT`, `CONTENT_VALIDITY_EVALUATION`, and `MEASUREMENT_PROPERTY_EVALUATION`. The new Chichewa versions are the principal output. (Abstract—Background; Conclusion)
- Design: two sequential parts, `TRANSLATION_ADAPTATION_WORKFLOW` with `QUALITATIVE_INQUIRY`, then `QUANTITATIVE_EMPIRICAL`; mixed-method integration `SEQUENTIAL`; temporal structure `CROSS_SECTIONAL`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods)
- Input verification: `corpus/20190200/doi_10.1186_s41687-024-00761-5.md`; 72,470 bytes; SHA-256 `b8f909cd41f6e78a60f33357e8ead8d5b7e5956785ab9364a33cd4c0a446d693`.

### Study structure and typed uses

- The adaptation part used translation, back translation, and cognitive interviews with ten healthy participants. The psychometric part used a separate convenience sample of 289 healthy or sick children and adolescents aged 8–17 years. (Methods—Translation process; Cognitive interviews; Participants)
- Data uses are `CURRENT_STUDY_COLLECTION` at `QUALITATIVE_MATERIAL` level for cognitive interviews and at `PARTICIPANT_RESPONSE` level for psychometric testing. (Methods—Cognitive interviews; self-completion)
- Instrument uses: exact labels `PedsQL™ 4.0 GCS child self-report` and `PedsQL™ 4.0 GCS teen self-report`. The US English versions have `TRANSLATION_SOURCE` and `DEVELOPMENT_OBJECT`; the Chichewa versions have `TRANSLATION_TARGET`, `CONTENT_TEST_OBJECT`, and `OUTCOME_MEASURE`. (Methods—The instruments; Translation process)
- Protocol use: exact labels `standard PedsQL™ 4.0 GCS translation protocol (forward and backward)` and `cognitive interview protocols`, context `DIRECT_CURRENT_ACTIVITY`, functions `TRANSLATION_PROTOCOL` and `GOVERNING_STUDY_PROTOCOL`. Methods include cognitive interviewing, item analysis, Cronbach's alpha, correlation, t-test, ANOVA, and a modified multitrait-multimethod approach. (Methods)

### Findings, limitations, products, and concepts

- Six items needed cultural adaptation. Cognitive interviews identified the unintended menstrual-cycle meaning of `kusamba`, and adding `m’thupi` resolved it. (Results—Translation process; Cognitive interviews)
- Internal consistency and convergent validity were promising, but results were mixed for missing data, adjacent endorsement, discriminant validity, and known-groups validity. The authors recommend cautious use. (Abstract—Results; Discussion; Conclusion)
- Reported limitations were cognitive adaptation with healthy participants only and one-time psychometric data collection, which prevented assessment of test-retest reliability and responsiveness. The Chichewa child and teen self-report versions map to `INSTRUMENT_VERSION`; pre-final versions went to Mapi Research Trust for approval before administration. Concepts include linguistic and conceptual equivalence, literacy, self-completion, and cultural connotation. (Discussion; Methods—Cognitive interviews; Conclusion)

### Gaps and source conflicts

- `SourceConflict`: the abstract states that missing data below 5% were problematic, but Methods define 5% or more as problematic and Results report 16 of 23 child items failed that criterion. Preserve both threshold statements. (Abstract—Results; Methods—Item analysis; Results—Item analyses)
- `SourceConflict`: the abstract uses abbreviation `GSC` once, while the title and body use `GCS` for Generic Core Scales. Preserve the exact source labels; do not silently normalize the abstract label. (Abstract—Background; Methods—The instruments)

### High-value canonical terms

- Controlled: `INSTRUMENT_VERSION_DEVELOPMENT`, `TRANSLATION_AND_CULTURAL_ADAPTATION`, `SEQUENTIAL`, `TRANSLATION_SOURCE`, `TRANSLATION_TARGET`, `CONTENT_VALIDITY`, and `INSTRUMENT_VERSION`. Registry: `PedsQL™ 4.0 GCS child self-report`, `PedsQL™ 4.0 GCS teen self-report`, `standard PedsQL™ 4.0 GCS translation protocol (forward and backward)`, and `cognitive interview protocols`.

## D004 — Exploring the Comparability of Face-to-Face Versus Video Conference-Based Composite Time Trade-Off Interviews

### Assessment and classification

- Primary family: `METHODS_RESEARCH`. Purposes: `METHOD_OR_PROTOCOL_QUALITY`, `VALUATION_METHOD_EVALUATION`, and `IMPLEMENTATION_EVALUATION`. The main decision concerns administration-mode effects on cTTO data quality. (Abstract—Background; Conclusions)
- Design: `QUANTITATIVE_EMPIRICAL`; `VARIABLE_SOURCE_TIME`; comparison `BETWEEN_CONTEXT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods—Sampling and Data Collection; Statistical Comparison)
- Input verification: `corpus/20180510/doi_10.1007_s40271-022-00573-z.md`; 89,014 bytes; SHA-256 `87546967999f6c5a21fc8bd2b7a96493080b09695f502b89787aedec94405c7d`.

### Study structure and typed uses

- Two country parts have separate samples and data sources. Belgium contributed 218 interviews: 120 face-to-face and 98 video. Spain contributed 184 analyzed interviews: 123 face-to-face and 61 video; 16 video interviews by one interviewer were excluded. (Methods—Sampling and Data Collection; Results—Descriptive Statistics)
- Data use: `PRIOR_RESEARCH_COLLECTION` at `PARTICIPANT_RESPONSE` level from national Belgium and Spain EQ-5D-Y-3L valuation studies. The nonrandom, sequential administration modes are a study factor with role `STUDIED_CONDITION`. (Methods—The EQ-5D-Y-3L Valuation Protocol; Statistical Comparison)
- Method use: exact label `composite time trade-off (cTTO)`, context `CURRENT_STUDY_OBJECT`, function `PREFERENCE_ELICITATION`. Instrument use: exact label `EQ-5D-Y-3L`, context `SOURCE_STUDY_ACTIVITY`, functions `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. (Methods—Valuation Protocol; Interview Structure)
- Protocol use: exact label `international EQ-5D-Y-3L valuation protocol`, context `SOURCE_STUDY_ACTIVITY`, function `VALUATION_PROTOCOL`; exact label `standard quality control procedure of the EuroQol Group`, function `QUALITY_CONTROL_PROTOCOL`. Task order randomization remains in `TaskDesign`, not allocation. (Methods—Valuation Protocol; Sampling and Data Collection)

### Findings, limitations, products, and concepts

- Outcome family is `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Interviewer and respondent engagement measures did not show worse results for video than for later face-to-face interviews in either country. (Abstract—Results; Discussion)
- Video interviews had longer observed total duration in both countries, significantly so only in Spain. Differences in inconsistent respondents and worse-than-dead values were not significant. (Results—Respondent Engagement; Face Validity)
- Reported limitations were nonrandom administration, time and pandemic confounding, interviewer learning, subgroup demographic imbalance, IT-skill selection, reduced power, and small samples for subgroup analysis. No explicit reusable product is reported. Concepts include video and face-to-face administration, engagement, learning effects, and data quality. (Discussion; Methods—Metrics Definition)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. The current paper examines source-study activities; it does not repeat the national valuation collections. (Methods—The EQ-5D-Y-3L Valuation Protocol)

### High-value canonical terms

- Controlled: `METHODS_RESEARCH`, `IMPLEMENTATION_EVALUATION`, `PRIOR_RESEARCH_COLLECTION`, `BETWEEN_CONTEXT`, `CURRENT_STUDY_OBJECT`, and `SOURCE_STUDY_ACTIVITY`. Registry: `composite time trade-off (cTTO)`, `EQ-5D-Y-3L`, `international EQ-5D-Y-3L valuation protocol`, `standard quality control procedure of the EuroQol Group`, and `EuroQol Valuation Technology (EQ-VT)`.

## D005 — Measuring Effectiveness Based on Patient Experience (Instead of QALYs) in US Value Assessments

### Assessment and classification

- Primary family: `VALUE_SET_DEVELOPMENT`. Purposes: `HEALTH_STATE_VALUATION`, `VALUE_SET_DEVELOPMENT`, and `PREFERENCE_COMPARISON`. The principal outputs are preference-based experience-scale values for three parent perspectives. (Abstract—Methods and Results; Results; Conclusions)
- Design: `QUANTITATIVE_EMPIRICAL` and `MODEL_BASED`; `CROSS_SECTIONAL`; comparisons `BETWEEN_GROUP` and `BETWEEN_CONTEXT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods)
- Input verification: `corpus/304-PHD/doi_10.1007_s40273-024-01444-1.md`; 32,807 bytes; SHA-256 `e27029b44386f096dd26fc2f449114b07773a788ad1181b4378639882a3f53d2`.

### Study structure and typed uses

- One secondary-analysis part uses 179 parents from a 631-person US adult survey. It reports nested mother and father subgroups of 99 and 80. Data use is `PRIOR_RESEARCH_COLLECTION` at `PARTICIPANT_RESPONSE` level. (Methods)
- Instrument use: exact label `EQ-5D-Y-3L`, context `INPUT_DATA_PROVENANCE`, functions `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. (Methods)
- Method uses: exact labels `discrete choice experiment (DCE)`, `kaizen tasks`, `paired comparisons`, and `experience scale`; context `SOURCE_STUDY_ACTIVITY` for the elicitation tasks and `DIRECT_CURRENT_ACTIVITY` for experience-scale derivation; functions `PREFERENCE_ELICITATION` and `MAPPING_OR_DERIVATION`. (Methods)
- Model uses: three exact-label `conditional logit models`, function `CHOICE_MODELING`; parent, mother, and father models have analytic role `SUBGROUP`. Cluster bootstrap has `QUANTITATIVE_ANALYSIS`. (Methods)

### Findings, limitations, products, and concepts

- Outcome family is `PREFERENCE_OR_UTILITY`. Mothers valued relief in a child's feelings more highly than fathers; other reported perspective differences were not statistically significant. (Results; Conclusions)
- For parents, the worst state 33333 had experience value -0.294 and was worse than no experience, stated as being in a coma. The source explicitly says these are not standard Y-3L value sets. (Results)
- Reported limitations are that experience scaling excludes life expectancy, may not support comparison across conditions, permits perspective selection, lacks open-source access, and needs development for other ages, durations, countries, and groups. Parent, mother, and father products each map to `VALUE_SET`; no approval or deployment is reported. Concepts include experience scaling, no experience, stakeholder perspective, and separation of HRQoL from life expectancy. (Results; Discussion)

### Gaps and source conflicts

- `SourceConflict`: the Abstract and Results call other mother-father differences not statistically significant but give “p-values < .05.” Preserve the significance statement and the reported inequality; do not repair it to `> .05`. (Abstract—Results; Results)

### High-value canonical terms

- Controlled: `VALUE_SET_DEVELOPMENT`, `HEALTH_STATE_VALUATION`, `PREFERENCE_COMPARISON`, `PRIOR_RESEARCH_COLLECTION`, `PREFERENCE_OR_UTILITY`, and `VALUE_SET`. Registry: `EQ-5D-Y-3L`, `discrete choice experiment (DCE)`, `kaizen tasks`, `paired comparisons`, `experience scale`, and `conditional logit models`.

## D006 — Can Patient-Reported Outcome Measures Help Predict Unplanned Hospital Readmission?

### Assessment and classification

- Primary family: `APPLIED_USE_RESEARCH`. Purposes: `DECISION_SUPPORT_DEVELOPMENT`, `IMPLEMENTATION_EVALUATION`, and `OUTCOME_DESCRIPTION`. The primary question is whether routine PROM use adds value to postdischarge risk prediction and care management. (Abstract—Objectives; Conclusions)
- Design: `QUANTITATIVE_EMPIRICAL` and `MODEL_BASED`; `LONGITUDINAL_REPEATED`; comparison `BETWEEN_INSTRUMENT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods—Study Design; Model Derivation)
- Input verification: `corpus/1787-RA/doi_10.1097_mlr.0000000000002315.md`; 55,617 bytes; SHA-256 `1357ec5e1968fa90e5d089d20bce9aa717a605af481776e7fdac726471b62dad`.

### Study structure and typed uses

- One linked cohort contains 11,177 analyzed adults discharged from acute care; 6,253 had complete predictor data. Sample stages are `ANALYZED` for the full cohort and complete-case sensitivity subset. (Methods—Study Population; Results—Participants)
- Data uses are `ROUTINE_SERVICE_COLLECTION` at `PARTICIPANT_RESPONSE` level for the Acute Inpatient Survey and at `DOCUMENT` level for linked NACRS, DAD, and demographic records. (Methods—Study Design and Data Sources)
- Instrument uses: exact labels `EQ-5D-5L` and `Veterans RAND 12-Item Health Survey (VR-12)`, context `INPUT_DATA_PROVENANCE`, function `PREDICTOR_MEASURE`. Their enhanced-model comparison function is `COMPARATOR`. (Methods—Predictors)
- Model uses: exact labels `Cox Landmark Supermodel` with analytic role `PRIMARY_REPORTED`, `Cox model with time-dependent PROM covariates` and `logistic regression` with role `SENSITIVITY`; all have function `STATISTICAL_ESTIMATION`. (Methods—Model Derivation; Sensitivity Analyses)

### Findings, limitations, products, and concepts

- Outcome families are `IMPLEMENTATION`, `METHOD_PERFORMANCE_OR_DATA_QUALITY`, and `HEALTH_STATUS_OR_EQ_VAS`. PROM-enhanced models improved discrimination modestly at all horizons. (Abstract—Results; Results—Model Performance)
- At 180 days, the C-index increased from 0.762 for administrative data to 0.774 with EQ-5D-5L and 0.782 with VR-12. In the ACSC subgroup, VR-12 improved discrimination by 2.4%–3.0%. (Abstract—Results; Results—Subgroup Analysis)
- Reported limitations are response-selection bias, PROM collection weeks after discharge, omission of early readmissions, one PROM observation carried forward, and need for external validation and economic evaluation. No explicit reusable product is reported. Concepts include PROM-enhanced prediction, landmark time, readmission horizon, calibration, discrimination, and postdischarge monitoring. (Discussion—Strengths and Limitations; Methods—Model Performance Evaluation)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. The readmission is a health event, but predictive use and care support are primary; do not force `HEALTH_OUTCOME_RESEARCH`. (Abstract—Objectives; Conclusions)

### High-value canonical terms

- Controlled: `APPLIED_USE_RESEARCH`, `DECISION_SUPPORT_DEVELOPMENT`, `ROUTINE_SERVICE_COLLECTION`, `PREDICTOR_MEASURE`, `STATISTICAL_ESTIMATION`, and `IMPLEMENTATION`. Registry: `EQ-5D-5L`, `Veterans RAND 12-Item Health Survey (VR-12)`, `Cox Landmark Supermodel`, `Cox model with time-dependent PROM covariates`, and `TRIPOD guidelines`.

## D007 — Uncertainty around Health State Values Used in Cost-Effectiveness Analysis: How It Arises and How to Deal with It

### Assessment and classification

- Primary family: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. Purpose: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. The main output is a classification of uncertainty types, sources, pathways, and responses. (Abstract; What Do We Mean by Uncertainty?; Conclusions)
- Design: `CONCEPTUAL`; temporal structure `NOT_APPLICABLE`; comparison `NONCOMPARATIVE`; allocation `NOT_APPLICABLE`. Publication form is `CONCEPTUAL_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Abstract; article structure)
- Input verification: `corpus/399-RA/doi_10.1177_0272989x251380556.md`; 59,876 bytes; SHA-256 `91d4c02e7b1d5b43b84e82c49838fbe2ba6ba78ac4449304a1a9504b078b3ae4`.

### Study structure and typed uses

- One conceptual study uses `CONCEPTUAL_MATERIAL` at `DOCUMENT` level. No empirical sample is reported. (Abstract; What Do We Mean by Uncertainty?)
- Instrument labels `EQ-5D-3L`, `EQ-5D-5L`, `SF-6D`, and `HUI` have context `DISCUSSION_ONLY` and function `REFERENCE_ONLY`. (How Uncertainty Combines; Discussion)
- Method labels `valuation study`, `mapping`, `meta-analysis`, `cost-effectiveness modeling`, and `sensitivity analysis` have context `DISCUSSION_ONLY` and retain their source labels. (How Uncertainty Combines; Figure 1)
- The framework distinguishes variability, heterogeneity, statistical uncertainty, and methodological variation, then traces uncertainty through valuation, profile data, mapping, disease-state studies, meta-analysis, and cost-effectiveness modeling. (What Do We Mean by Uncertainty?; Figure 1)

### Findings, limitations, products, and concepts

- Outcome family is `CONCEPTUAL_CLASSIFICATION`. Uncertainty accumulates across linked studies and is not adequately represented in QALY or cost-effectiveness estimates. (Abstract; Conclusions)
- The paper recommends health-state-level standard errors or variance-covariance matrices, fuller reporting, and explicit treatment of HSV uncertainty in decision models. (Discussion)
- The source states that its source list is not exhaustive and that some aspects remain hard to conceptualize and measure. The uncertainty account and flow map to `TAXONOMY_OR_FRAMEWORK`. Concepts include variability, heterogeneity, statistical and methodological uncertainty, inherited uncertainty, and model misspecification. (Sources of Uncertainty within Valuation Studies; Discussion; Figure 1; Table 1)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. The cited scoping review is background evidence, not the current study design. (Introduction)

### High-value canonical terms

- Controlled: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`, `CONCEPTUAL`, `CONCEPTUAL_MATERIAL`, `CONCEPTUAL_CLASSIFICATION`, and `TAXONOMY_OR_FRAMEWORK`. Registry: `EQ-5D-3L`, `EQ-5D-5L`, `SF-6D`, `HUI`, `mapping`, `meta-analysis`, `cost-effectiveness modeling`, and `sensitivity analysis`.

## D008 — Perceptions of the General Public About Health-related Quality of Life and the EQ-5D Questionnaire: A Qualitative Study in Korea

### Assessment and classification

- Primary family: `MEASUREMENT_PROPERTY_EVALUATION`. Purposes: `CONTENT_VALIDITY_EVALUATION` and `OUTCOME_DESCRIPTION`. The main decision concerns the relevance, comprehensibility, and coverage of EQ-5D-5L and EQ-VAS in Korea. (Abstract—Objectives; Discussion; Conclusion)
- Design: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; comparison `NONCOMPARATIVE`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods)
- Input verification: `corpus/2016290/doi_10.3961_jpmph.22.151.md`; 58,582 bytes; SHA-256 `85bc7bba2624710564b9b3dc97c953f6f5d533bc9381b4390a897dce7d41f6f2`.

### Study structure and typed uses

- One study recruited 22 people; two helped to develop the guide, and 20 completed the analyzed interviews. Data use is `CURRENT_STUDY_COLLECTION` at `QUALITATIVE_MATERIAL` level; sample stage is `ANALYZED` for 20. (Methods—Research Participants)
- Instrument uses: exact labels `EuroQoL 5-Dimension 5-Level (EQ-5D-5L)` and `EuroQoL visual analogue scale (EQ-VAS)`, context `CURRENT_STUDY_OBJECT`, function `CONTENT_TEST_OBJECT`. (Methods—In-depth Interview Procedure)
- Method uses: exact labels `face-to-face, in-depth interviews`, `semi-structured interview guide`, and `directive content analysis`; functions `QUALITATIVE_DATA_COLLECTION` and `QUALITATIVE_ANALYSIS`. (Abstract—Methods; Methods—Analysis)
- Protocol use: exact label `Consolidated Criteria for Reporting Qualitative Research (COREQ) checklist`, context `DIRECT_CURRENT_ACTIVITY`, function `REPORTING_GUIDELINE`. (Methods)

### Findings, limitations, products, and concepts

- Outcome families are `CONTENT_VALIDITY` and `CONCEPTUAL_CLASSIFICATION`. The analysis produced 734 codes in four categories. Participants emphasized physical health but also identified mental and social health as important. (Abstract—Results; Results—Identified Concepts)
- Participants found EQ-5D-5L simple and broadly relevant, but some wanted more mental-health and social-health content. They liked EQ-VAS presentation but questioned score comparability and a single health score. (Results—Perceptions and opinions; Discussion)
- The reported limitation is limited generalizability from a qualitative sample; the authors call for hypothesis testing and international qualitative comparisons. No explicit reusable product is reported. Concepts include multidimensional, physical, mental, and social health, vitality, usual activities, scale anchors, and response comparability. (Results; Discussion)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. Suggestions for added dimensions and EQ-VAS labels are findings about instrument content, not approved instrument versions. (Discussion; Conclusion)

### High-value canonical terms

- Controlled: `MEASUREMENT_PROPERTY_EVALUATION`, `CONTENT_VALIDITY_EVALUATION`, `QUALITATIVE_INQUIRY`, `CONTENT_TEST_OBJECT`, and `CONTENT_VALIDITY`. Registry: `EuroQoL 5-Dimension 5-Level (EQ-5D-5L)`, `EuroQoL visual analogue scale (EQ-VAS)`, `directive content analysis`, and `Consolidated Criteria for Reporting Qualitative Research (COREQ) checklist`.

## D009 — Experience-based health state valuation using the EQ VAS among nine patient groups in Sweden

### Assessment and classification

- Primary family: `HEALTH_PREFERENCE_RESEARCH`. Purposes: `HEALTH_STATE_VALUATION` and `PREFERENCE_COMPARISON`. The study reports empirical patient valuations and does not make a new value set its principal output. (Abstract—Objective; Conclusions)
- Design: `QUANTITATIVE_EMPIRICAL` and `MODEL_BASED`; patient parts `LONGITUDINAL_REPEATED`, general-population part `CROSS_SECTIONAL`; comparisons `WITHIN_PERSON` and `BETWEEN_CONTEXT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods—Study design; Data analysis)
- Input verification: `corpus/2016480/doi_10.1186_s12955-023-02115-z.md`; 110,575 bytes; SHA-256 `7af13a637ee2fdaaa6015f33bf75811e8838652bb8eec73539e501c32d572762`.

### Study structure and typed uses

- Ten parts represent nine National Quality Registers and one general-population comparison source. The patient data have baseline and one-year follow-up; the comparison surveys were from 2004 and 2006. (Methods—Study design; Data)
- Data uses: `ROUTINE_SERVICE_COLLECTION` for the nine registers and `PRIOR_RESEARCH_COLLECTION` for the general-population surveys, both at `PARTICIPANT_RESPONSE` level. Sample sizes are reported as 172,070 patient records and 41,761 general-population participants. (Abstract—Methods; Methods—Data; Sample size)
- Instrument uses: exact labels `EQ-5D-3L` and `EQ VAS`, context `INPUT_DATA_PROVENANCE`; functions `HEALTH_STATE_DESCRIPTION`, `CURRENT_HEALTH_MEASUREMENT`, and `SCORING_INPUT`. Scoring use has exact label `Swedish experience-based EQ-5D-3L VAS value set`. (Methods—Data; Data analysis)
- Method and model uses: `EQ VAS` as an experience-based valuation method has `PREFERENCE_ELICITATION`; exact labels `ordinary least squares (OLS) models` and `two-level random slope and random intercept models` have `STATISTICAL_ESTIMATION` with roles `PRIMARY_REPORTED` and `SENSITIVITY`. (Methods—Data analysis)

### Findings, limitations, products, and concepts

- Outcome family is `PREFERENCE_OR_UTILITY`. EQ VAS scores were generally ordered by health-state severity at baseline and follow-up, and correlations with the EQ-5D-3L index were moderate to strong. (Abstract—Results; Discussion)
- Anxiety/depression had the largest decrement in most patient groups and the general population. Self-care level 3 was the main source of model inconsistency. (Abstract—Results; Conclusions)
- Reported limitations include different procedures across registers, no dead anchor, no explicit choice or trade-off in EQ VAS, end aversion, and discrepancy between EQ VAS and EQ-5D-3L. No present value set is claimed; the data have potential to provide one. Concepts include own-health valuation, patient perspective, severity consistency, timing, and adaptation. (Discussion; Conclusions)

### Gaps and source conflicts

- `SourceConflict`: the Abstract calls the 172,070 units “patients,” while Methods calls them “patient records.” Preserve both terms because the denominator and distinct-person count can differ. (Abstract—Methods; Methods—Sample size)

### High-value canonical terms

- Controlled: `HEALTH_PREFERENCE_RESEARCH`, `HEALTH_STATE_VALUATION`, `ROUTINE_SERVICE_COLLECTION`, `PRIOR_RESEARCH_COLLECTION`, `WITHIN_PERSON`, and `PREFERENCE_OR_UTILITY`. Registry: `EQ-5D-3L`, `EQ VAS`, `Swedish experience-based EQ-5D-3L VAS value set`, `ordinary least squares (OLS) models`, and `two-level random slope and random intercept models`.

## D010 — The effect of duration and time preference on the gap between adult and child health state valuations in time trade-off

### Assessment and classification

- Primary family: `METHODS_RESEARCH`. Purposes: `VALUATION_METHOD_EVALUATION`, `PREFERENCE_COMPARISON`, and `HEALTH_STATE_VALUATION`. The main decision concerns duration and time-preference effects on cTTO utilities. (Abstract; Introduction—Aims; Conclusion)
- Design: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; comparison `WITHIN_PERSON`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Experiment—Design and participants; TTO operationalization)
- Input verification: `corpus/237-RA/doi_10.1007_s10198-023-01612-8.md`; 80,820 bytes; SHA-256 `06d4f20b17ef523a1b289e2113a5f8f395a30a6eed56a88a55f6d51442f47185`.

### Study structure and typed uses

- One study used video interviews with 151 UK adults. All participants completed adult and 10-year-old-child perspectives, 10- and 20-year cTTO durations, and time-preference tasks. (Abstract; Experiment—Design and participants)
- Data use is `CURRENT_STUDY_COLLECTION` at `PARTICIPANT_RESPONSE` level. TaskDesign records four cTTO blocks, four states, two durations, two perspectives, a 10-year lead time, block and state order randomization, and the bisection/titration rule. Task randomization is not study allocation. (Experiment—TTO operationalization)
- Instrument use: exact label `EQ-5D-Y-3L`, context `DIRECT_CURRENT_ACTIVITY`, functions `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`; `EQVAS Own health today` has `CURRENT_HEALTH_MEASUREMENT`. (Introduction; Experiment—Interview procedure; Table 5)
- Method uses: exact labels `composite time trade-off (cTTO)` and `Direct Method`, both with `PREFERENCE_ELICITATION`; exact label `mixed-effects regressions` has `QUANTITATIVE_ANALYSIS`. Protocol use: `EQ-VT protocol`, function `VALUATION_PROTOCOL`. (Method; Experiment; Analysis)

### Findings, limitations, products, and concepts

- Outcome families are `PREFERENCE_OR_UTILITY` and `METHOD_PERFORMANCE_OR_DATA_QUALITY`. The child-perspective coefficient was 0.028 in the uncorrected mixed-effects model and was no longer significant after time-preference correction. (Results—Regression results)
- The 10- and 20-year durations did not differ materially. Average time preference was near zero, with substantial individual heterogeneity. (Results—Time preference; TTO utilities; Discussion)
- Reported limitations include sequence effects and other Direct Method interpretations, no time-preference validity checks, video interviews, unequal lower bounds, and partial explanation of the perspective difference. No reusable product is reported. Concepts include perspective, gauge duration, lead time, time preference, constant proportional trade-off, and sequence effect. (Method; Discussion)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. Random block and task order belongs to `TaskDesign`; it must not cause `RANDOMIZED` allocation. (Experiment—TTO operationalization)

### High-value canonical terms

- Controlled: `METHODS_RESEARCH`, `VALUATION_METHOD_EVALUATION`, `PREFERENCE_COMPARISON`, `WITHIN_PERSON`, `PREFERENCE_ELICITATION`, and `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Registry: `EQ-5D-Y-3L`, `composite time trade-off (cTTO)`, `Direct Method`, `EQ-VT protocol`, and `mixed-effects regressions`.

## D011 — Nothing about us, without us? A reflection on and call for involving children in valuing child health

### Assessment and classification

- Primary family: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. Purpose: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. The paper classifies 13 public-involvement arguments and applies them to children's involvement in health-state valuation. (Abstract; Public involvement; Nothing about us without us)
- Design: `CONCEPTUAL`; temporal structure `NOT_APPLICABLE`; comparison `NONCOMPARATIVE`; allocation `NOT_APPLICABLE`. Publication form is `OPINION_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Abstract; article structure)
- Input verification: `corpus/1462-PHD/doi_10.1007_s10198-025-01823-1.md`; 48,411 bytes; SHA-256 `949690fcd6808e4d6dd65cd7417fd63e83f446e6ede0a3fce9fdfadf605ffe91`.

### Study structure and typed uses

- One conceptual study uses `DOCUMENTARY_SOURCE` at `DOCUMENT` level. Sources were found through search engines and snowballing; this is not reported as a systematic review. (Public involvement in decisions on health(care))
- Instrument labels `EQ-5D-Y` and `EQ-5D-Y-3L` have context `DISCUSSION_ONLY` and function `REFERENCE_ONLY`. (Valuing child health; Involving children)
- Method labels `Time Trade-Off (TTO)`, `Discrete Choice Experiments (DCEs)`, ranking, deliberative groups, and qualitative approaches have context `DISCUSSION_ONLY`; some are also `PLANNED_ACTIVITY` recommendations. (Valuing child health; Nothing about us without us)
- Stakeholder involvement is reported: an advisory group of EuroQol members gave feedback on an earlier version. The activity and its influence were feedback on the manuscript. (Acknowledgements)

### Findings, limitations, products, and concepts

- Outcome family is `CONCEPTUAL_CLASSIFICATION`. The framework groups 13 arguments as input, process, or outcome arguments and finds most relevant to child involvement in the valuation process. (Table 1; Table 2)
- The principal interpretation is a shift from whether children should be involved to how they can be involved, including activities beyond direct valuation tasks. (Abstract; Nothing about us without us)
- Source-reported bounds are that the argument list is non-exhaustive, it does not distinguish child age groups, relevance can vary by age, and proposed approaches have ethical and cognitive challenges. The classification maps to `TAXONOMY_OR_FRAMEWORK`. Concepts include child involvement, valuation process and task, legitimacy, accuracy, public involvement, and paternalism. (Public involvement; Tables 1–2; Conclusion)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. The `OPINION_ARTICLE` publication form does not change the conceptual primary family. (Abstract; article structure)

### High-value canonical terms

- Controlled: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`, `CONCEPTUAL`, `DOCUMENTARY_SOURCE`, `DISCUSSION_ONLY`, `PLANNED_ACTIVITY`, and `TAXONOMY_OR_FRAMEWORK`. Registry: `EQ-5D-Y`, `EQ-5D-Y-3L`, `Time Trade-Off (TTO)`, `Discrete Choice Experiments (DCEs)`, `ranking`, and `deliberative groups`.

## D012 — Developing a quality of life framework from the perspective of laypeople: a qualitative comparison with the EQ-HWB framework

### Assessment and classification

- Primary family: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. Purposes: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` and `CONTENT_VALIDITY_EVALUATION`. Framework development is the first stated aim and the principal reusable output; content-validity comparison is secondary. (Introduction—Aims; Abstract—Conclusion)
- Design: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; comparison `BETWEEN_CONTEXT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods—Study design; Participant selection)
- Input verification: `corpus/1485-RA/doi_10.1007_s11136-025-04038-2.md`; 76,716 bytes; SHA-256 `168d53aed9f5436771a17e2560de98f312835ceea2df0b76cf64f31f8de92608`.

### Study structure and typed uses

- One study used 30 Chinese lay participants: ten healthy people, ten patients, and ten informal caregivers. Data use is `CURRENT_STUDY_COLLECTION` at `QUALITATIVE_MATERIAL` level. (Methods—Participant selection; Results—Participants)
- Instrument use: exact label `EQ-HWB`, context `CURRENT_STUDY_OBJECT`, function `CONTENT_TEST_OBJECT`; the 96 candidate EQ-HWB items also supplied the deductive codebook. (Introduction; Methods—Familiarization and coding)
- Method uses: exact labels `individual semi-structured interviews`, `thematic analysis`, and `thematic framework approach`; functions `QUALITATIVE_DATA_COLLECTION` and `QUALITATIVE_ANALYSIS`. (Abstract—Methods; Methods—Study design; Analysis)
- Protocol uses: exact labels `consolidated criteria for reporting qualitative research (COREQ)` and `COSMIN guideline on assessing content validity`, functions `REPORTING_GUIDELINE` and `GOVERNING_STUDY_PROTOCOL`. (Methods—Study design; Participant selection)

### Findings, limitations, products, and concepts

- Outcome families are `CONCEPTUAL_CLASSIFICATION` and `CONTENT_VALIDITY`. The 187 retained codes formed eight themes: feeling and emotion, cognition, self-identity, coping, physical sensation, relationship, activity, and mindset. (Abstract—Results; Results—QoL framework)
- Seven of eight themes aligned with EQ-HWB; mindset was additional. The paper concludes that EQ-HWB comprehensiveness is supported in the Chinese context. (Results—Comparison with the EQ-HWB; Conclusion)
- Reported limitations concern sample diversity, absence of severe hospitalized patients, difficult concept translation, no preset saturation criteria, and subjective saturation judgment. The Chinese QoL framework maps to `TAXONOMY_OR_FRAMEWORK`. Concepts include mindset, coping, cultural framing, comprehensiveness, positive or negative energy, autonomy, and dependence. (Limitation; Results—QoL framework)

### Gaps and source conflicts

- `SourceConflict`: the source reports a sub-theme alignment rate of 68% and gives the fraction 18/57, which equals about 31.6%. Preserve the percentage and fraction as separate source statements. (Results—Comparison with the EQ-HWB)

### High-value canonical terms

- Controlled: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`, `CONTENT_VALIDITY_EVALUATION`, `QUALITATIVE_INQUIRY`, `CONTENT_TEST_OBJECT`, `CONCEPTUAL_CLASSIFICATION`, and `TAXONOMY_OR_FRAMEWORK`. Registry: `EQ-HWB`, `individual semi-structured interviews`, `thematic analysis`, `thematic framework approach`, `consolidated criteria for reporting qualitative research (COREQ)`, and `COSMIN guideline on assessing content validity`.

## D013 — The Performance of Kaizen Tasks Across Three Online Discrete Choice Experiment Surveys: An Evidence Synthesis

### Assessment and classification

- Primary family: `METHODS_RESEARCH`. Purposes: `METHOD_OR_PROTOCOL_QUALITY`, `VALUATION_METHOD_EVALUATION`, and `EVIDENCE_SYNTHESIS`. The principal decision is how kaizen-task design affects performance and future method choice. (Abstract—Objective and Methods; Conclusions)
- Design: `QUANTITATIVE_EMPIRICAL`, `MODEL_BASED`, and `EVIDENCE_SYNTHESIS`; temporal structure `VARIABLE_SOURCE_TIME`; comparisons `BETWEEN_METHOD` and `BETWEEN_CONTEXT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods—Secondary Datasets; Primary Analyses)
- Input verification: `corpus/304-PHD/doi_10.1007_s40271-024-00708-4.md`; 53,929 bytes; SHA-256 `88a8fbfa8c75bcf902b77e17a48a32df69935d546d0db120706f518d4569bf76`.

### Study structure and typed uses

- Three parts reuse the 2020 US COVID-19 vaccination study, 2021 UK Children’s Surgery Outcome Reporting study, and 2023 US EQ-5D-Y-3L valuation study. Reported analysis samples are 652, 807, and 631. (Methods—Secondary Datasets; Table 1)
- Data use is `PRIOR_RESEARCH_COLLECTION` at `PARTICIPANT_RESPONSE` level. Instrument label `EQ-5D-Y-3L` has `INPUT_DATA_PROVENANCE` and functions `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. (Methods—Secondary Datasets)
- Method uses: exact labels `kaizen task`, `paired-comparison tasks`, and `discrete choice experiment (DCE)`, context `CURRENT_STUDY_OBJECT`, function `PREFERENCE_ELICITATION`; bootstrap and response-behavior analyses have `QUANTITATIVE_ANALYSIS`. (What is a Kaizen Task?; Methods)
- Model uses: exact labels `conditional logit` and `Zermelo–Bradley–Terry (ZBT) models`, function `CHOICE_MODELING`, roles `COMPARATOR` and `PRIMARY_REPORTED`. Task order and attribute order stay in `TaskDesign`, not allocation. (Methods—Primary Analyses)

### Findings, limitations, products, and concepts

- Outcome family is `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Hold-outs appeared to halve positional behavior; lack of multi-level improvements prevented direct logit main-effect estimation; fixed attribute order may explain weak CSOR estimates. (Abstract—Results; Discussion)
- All Y-3L estimates were positive and significant. Kaizen predictions had high correlation and strong agreement with paired-comparison probabilities, and simulated results suggested smaller samples can be sufficient. (Abstract—Results; Results—Standard Errors)
- Source-reported limits are that designs differ, comparisons support inference rather than random assignment, and current evidence does not support nominal attributes or interactions. A planned open-source suite maps to `SOFTWARE_OR_DECISION_SUPPORT` with a “preparing” state. Concepts include preference path, hold-out, positional behavior, multi-level improvement, predictive validity, and sample efficiency. (Discussion)

### Gaps and source conflicts

- `SourceConflict`: Table 1 says 1,026 of 1,357 CSOR respondents equal 69%, but that fraction is about 75.6%; it also says 230 additional exclusions yield an analysis sample of 807, while 1,026 minus 230 is 796. Preserve all reported counts and percentages. (Methods—Secondary Datasets; Table 1)

### High-value canonical terms

- Controlled: `METHODS_RESEARCH`, `METHOD_OR_PROTOCOL_QUALITY`, `EVIDENCE_SYNTHESIS`, `PRIOR_RESEARCH_COLLECTION`, `BETWEEN_METHOD`, and `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Registry: `kaizen task`, `paired-comparison tasks`, `discrete choice experiment (DCE)`, `conditional logit`, `Zermelo–Bradley–Terry (ZBT) models`, and `EQ-5D-Y-3L`.

## D014 — What do HTA agencies need for generating health-related quality of life evidence? Findings from a global survey

### Assessment and classification

- Primary family: `APPLIED_USE_RESEARCH`. Purposes: `IMPLEMENTATION_EVALUATION` and `OUTCOME_DESCRIPTION`. The paper describes use, practice, quality problems, and evidence needs in HTA agencies. (Abstract—Objectives; Conclusions)
- Design: `QUANTITATIVE_EMPIRICAL` and `QUALITATIVE_INQUIRY` with `CONVERGENT_PARALLEL` integration; `CROSS_SECTIONAL`; comparison `BETWEEN_CONTEXT`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods; Statistical analysis)
- Input verification: `corpus/1505-RA/doi_10.1017_s0266462326103602.md`; 101,826 bytes; SHA-256 `4f26cab992adb34e099c71814ee81c54b02de2bffc8ad03c5f824627b93901be`.

### Study structure and typed uses

- One global online survey has 238 completed respondents from 45 countries and 65 HTA agencies. Sixty countries were approached, and the survey was distributed in 49. Data use is `CURRENT_STUDY_COLLECTION` at `PARTICIPANT_RESPONSE` and `QUALITATIVE_MATERIAL` levels. (Methods; Results—Sample characteristics)
- The six regions are comparison contexts. Instrument labels `EQ-5D`, `SF-6D`, and `EQ-5D-Y` have context `CURRENT_STUDY_OBJECT` and function `IMPLEMENTATION_OBJECT`, because the survey examines their use rather than measuring respondent health. (Abstract—Results; Results—Use and importance)
- Method labels `time trade-off`, `visual analogue scale`, `standard gamble`, `discrete choice experiment`, `best-worst scaling`, and `person trade-off` have context `CURRENT_STUDY_OBJECT` and retain `PREFERENCE_ELICITATION` as their scientific function. (Results—Use and importance of preference elicitation methods)
- Current methods include `online survey`, descriptive analysis, regional pooling, forward-backward translation, and structured content analysis. Functions are `QUANTITATIVE_DATA_COLLECTION`, `QUANTITATIVE_ANALYSIS`, `QUALITATIVE_ANALYSIS`, and `QUALITY_CONTROL`. HTA personnel pilot-tested and influenced iterative form development. (Methods—Survey form; Statistical analysis)

### Findings, limitations, products, and concepts

- Outcome family is `IMPLEMENTATION`. The most used instruments were EQ-5D, SF-6D, and EQ-5D-Y; the most used elicitation methods were time trade-off, visual analogue scale, and standard gamble. (Abstract—Results)
- Foreign general-public preferences were used more often than local public preferences. Common quality problems were poor representativeness, small samples, data-model mismatch, and mixed instruments or methods. (Results—Data sources; Data quality)
- Global priorities were recent utility values, child instruments, and instruments that cover healthcare and social care. Limitations include few responses in 12 countries, uncertain agency representation, network recruitment that can favor EuroQol familiarity, no agency identifiers, no reliable subgroup analysis, and inability to verify eligibility. No reusable product is reported. (Results—Research priorities; Discussion)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. Survey participants are ordinary respondents; the paper does not report that they influenced study decisions. Pilot testers informed iterative survey-form development and can be retained as involvement evidence if that activity is extracted. (Methods—Survey form)

### High-value canonical terms

- Controlled: `APPLIED_USE_RESEARCH`, `IMPLEMENTATION_EVALUATION`, `CONVERGENT_PARALLEL`, `CURRENT_STUDY_OBJECT`, `IMPLEMENTATION_OBJECT`, and `IMPLEMENTATION`. Registry: `EQ-5D`, `SF-6D`, `EQ-5D-Y`, `time trade-off`, `visual analogue scale`, `standard gamble`, `discrete choice experiment`, `best-worst scaling`, and `person trade-off`.

## D015 — Living in uncertainty due to floods and pollution: health and quality of life on an unhealthy riverbank

### Assessment and classification

- Primary family: `HEALTH_OUTCOME_RESEARCH`. Purpose: `OUTCOME_DESCRIPTION`. Health status, quality of life, happiness, and life satisfaction under riverbank exposure are the primary outcomes. (Abstract—Background; Objectives in Background; Conclusion)
- Design: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; comparison `BETWEEN_GROUP`; allocation `NOT_APPLICABLE`. Publication form is `ORIGINAL_RESEARCH_ARTICLE`; execution is `COMPLETED`; results are `RESULTS_REPORTED`. (Methods; Analysis)
- Input verification: `corpus/2013240/doi_10.1186_s12889-018-5706-0.md`; 67,215 bytes; SHA-256 `a87301d2f9843a690a82156a6439327902948364a5d42df83c2150818f23262f`.

### Study structure and typed uses

- Two data-source parts separate current Ciliwung collection from prior comparison data. Samples are 204 Ciliwung residents, 204 matched controls, 305 Jakarta residents, and 1,041 general-population respondents; the comparison subsets overlap the larger prior study and must not be added as independent samples. (Abstract—Methods; Methods—Respondents)
- Data uses: `CURRENT_STUDY_COLLECTION` for Ciliwung and `PRIOR_RESEARCH_COLLECTION` for the three comparison samples, all at `PARTICIPANT_RESPONSE` level. (Methods—Respondents; Procedure)
- Instrument uses, context `DIRECT_CURRENT_ACTIVITY` for Ciliwung and `INPUT_DATA_PROVENANCE` for comparisons, functions `OUTCOME_MEASURE` and `CURRENT_HEALTH_MEASUREMENT`: exact labels `EQ-5D-5L`, `EQ Visual Analogue Scale (EQ-VAS)`, `WHOQOL-BREF`, `Happiness Thermometer`, and `Cantril’s Self-Anchoring Striving Scale`. (Methods—Measures)
- Scoring use has exact label `Indonesian value set`. Study factors include riverbank residence, flood and pollution exposure, and comparison group; roles are `STUDIED_CONDITION` and `COMPARATOR`. Methods include MANOVA and multiple linear regression with `QUANTITATIVE_ANALYSIS`. (Methods—Analysis)

### Findings, limitations, products, and concepts

- Outcome family is `HEALTH_STATUS_OR_EQ_VAS`. Ciliwung residents reported lower physical WHOQOL-BREF quality of life and less happiness, but better EQ-5D-5L health, life satisfaction, and perceived financial situation than matched controls. (Abstract—Results; Results—Comparison between groups)
- Similar patterns occurred against Jakarta and general-population comparisons. Most differences were small; the physical quality-of-life difference was moderate. (Results—Comparison between groups; Discussion)
- Reported limitations are uncertain effects from imminent relocation and possible selection or dependence bias from recruitment through a local organization. No reusable product is reported. Concepts include pollution, flooding, relocation, adaptation, relative comparison, social capital, community resilience, happiness, and life satisfaction. (Discussion; Implications)

### Gaps and source conflicts

- No controlled-value gap or source conflict is required. Do not infer post-relocation outcomes: the source describes them as future-study questions. (Implications; Conclusion)

### High-value canonical terms

- Controlled: `HEALTH_OUTCOME_RESEARCH`, `OUTCOME_DESCRIPTION`, `BETWEEN_GROUP`, `CURRENT_STUDY_COLLECTION`, `PRIOR_RESEARCH_COLLECTION`, and `HEALTH_STATUS_OR_EQ_VAS`. Registry: `EQ-5D-5L`, `EQ Visual Analogue Scale (EQ-VAS)`, `WHOQOL-BREF`, `Happiness Thermometer`, `Cantril’s Self-Anchoring Striving Scale`, and `Indonesian value set`.

## Cross-paper gap, conflict, and rule-risk check

- Gap count is zero. All controlled fields use version 0.3 values, and no proposed addition is approved. Source conflicts occur in five papers: D003, D005, D009, D012, and D013.
- Family-boundary risk: explicit value sets make D005 `VALUE_SET_DEVELOPMENT`; routine PROM use for care support makes D006 `APPLIED_USE_RESEARCH`; a content-validity decision makes D008 `MEASUREMENT_PROPERTY_EVALUATION`; and the first aim and reusable framework make D012 `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. (D005 Conclusions; D006 Objectives; D008 Objectives; D012 Aims)
- Family-boundary risk: D011 publication form does not change its conceptual family. D013 calls itself a synthesis, but its main decision is kaizen-task performance and choice, so `METHODS_RESEARCH` applies. (D011 Tables 1–2; D013 Conclusions)
- Use and allocation risks: D002 uses current review objects; D004 uses source-study activities; D009 uses data provenance; D014 uses implementation objects; D015 separates direct and provenance uses. Random task order in D010 and D013 stays in `TaskDesign`, and allocation is `NOT_APPLICABLE`.
- Part and product risks: parts occur only for distinct samples or sources in D003, D004, D009, D013, and D015. Absence of a product-state statement is not a negative assertion; D013 software is planned, not deployed.

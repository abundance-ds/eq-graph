# Round 4 application B: ontology version 0.3

This application uses only ontology version 0.3 and the current controlled vocabulary. Each source locator names a section, table, or figure in the stated article file.
## Exact input verification

All 15 article files matched the path, SHA-256 digest, and byte count in `round-04.tsv`.

- D001 — `corpus/1508-RA/doi_10.1007_s10198-025-01769-4.md`; `5aeb8d6b2307857d7cfd092368a992685d86ab149249d8db3b4d03dc4468c324`; 78,866 bytes.
- D002 — `corpus/2016230/doi_10.1007_s40273-019-00854-w.md`; `68f45ea10e7e3e77cad9ebad14637b5c1f2f2109e34b67f380cce6c050127b6c`; 113,530 bytes.
- D003 — `corpus/20190200/doi_10.1186_s41687-024-00761-5.md`; `b8f909cd41f6e78a60f33357e8ead8d5b7e5956785ab9364a33cd4c0a446d693`; 72,470 bytes.
- D004 — `corpus/20180510/doi_10.1007_s40271-022-00573-z.md`; `87546967999f6c5a21fc8bd2b7a96493080b09695f502b89787aedec94405c7d`; 89,014 bytes.
- D005 — `corpus/304-PHD/doi_10.1007_s40273-024-01444-1.md`; `e27029b44386f096dd26fc2f449114b07773a788ad1181b4378639882a3f53d2`; 32,807 bytes.
- D006 — `corpus/1787-RA/doi_10.1097_mlr.0000000000002315.md`; `1357ec5e1968fa90e5d089d20bce9aa717a605af481776e7fdac726471b62dad`; 55,617 bytes.
- D007 — `corpus/399-RA/doi_10.1177_0272989x251380556.md`; `91d4c02e7b1d5b43b84e82c49838fbe2ba6ba78ac4449304a1a9504b078b3ae4`; 59,876 bytes.
- D008 — `corpus/2016290/doi_10.3961_jpmph.22.151.md`; `85bc7bba2624710564b9b3dc97c953f6f5d533bc9381b4390a897dce7d41f6f2`; 58,582 bytes.
- D009 — `corpus/2016480/doi_10.1186_s12955-023-02115-z.md`; `7af13a637ee2fdaaa6015f33bf75811e8838652bb8eec73539e501c32d572762`; 110,575 bytes.
- D010 — `corpus/237-RA/doi_10.1007_s10198-023-01612-8.md`; `06d4f20b17ef523a1b289e2113a5f8f395a30a6eed56a88a55f6d51442f47185`; 80,820 bytes.
- D011 — `corpus/1462-PHD/doi_10.1007_s10198-025-01823-1.md`; `949690fcd6808e4d6dd65cd7417fd63e83f446e6ede0a3fce9fdfadf605ffe91`; 48,411 bytes.
- D012 — `corpus/1485-RA/doi_10.1007_s11136-025-04038-2.md`; `168d53aed9f5436771a17e2560de98f312835ceea2df0b76cf64f31f8de92608`; 76,716 bytes.
- D013 — `corpus/304-PHD/doi_10.1007_s40271-024-00708-4.md`; `88a8fbfa8c75bcf902b77e17a48a32df69935d546d0db120706f518d4569bf76`; 53,929 bytes.
- D014 — `corpus/1505-RA/doi_10.1017_s0266462326103602.md`; `4f26cab992adb34e099c71814ee81c54b02de2bffc8ad03c5f824627b93901be`; 101,826 bytes.
- D015 — `corpus/2013240/doi_10.1186_s12889-018-5706-0.md`; `a87301d2f9843a690a82156a6439327902948364a5d42df83c2150818f23262f`; 67,215 bytes.
## Complete primary-family partition

- `METHODS_RESEARCH` (4): D001, D004, D005, D010.
- `APPLIED_USE_RESEARCH` (2): D006, D014.
- `EVIDENCE_SYNTHESIS` (2): D002, D013.
- `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` (3): D007, D011, D012.
- `INSTRUMENT_VERSION_DEVELOPMENT` (1): D003.
- `MEASUREMENT_PROPERTY_EVALUATION` (1): D008.
- `HEALTH_PREFERENCE_RESEARCH` (1): D009.
- `HEALTH_OUTCOME_RESEARCH` (1): D015.

Counting unit: distinct study. Denominator: 15 studies. The partition count is 15. No study occurs in more than one primary family.
## Cross-paper rule risks

- D001, D010, D013, and D014 examine a method as a study object. `use_context` supports `CURRENT_STUDY_OBJECT`, but `method_function` has no evaluation-object or implementation-object value. The applications keep `UNMAPPED_VALUE` and do not misuse `QUALITY_CONTROL`.
- D006 has unplanned hospital readmission as its main clinical event. No `outcome_family` value covers health-service use or a clinical event. The application keeps `UNMAPPED_VALUE`.
- D003 and D015 contain inconsistent source labels. The applications preserve both statements as `SourceConflict` records.
## D001 — 10.1007/s10198-025-01769-4

### Assessment and classification

- Title: “Test-retest reliability of the Online Elicitation of Personal Utility Functions (OPUF) approach for valuing the EQ-HWB-S.” The aim is method reliability, so `primary_research_family` is `METHODS_RESEARCH`. (Abstract, Introduction)
- Ranked `research_purpose`: `VALUATION_METHOD_EVALUATION`, `METHOD_OR_PROTOCOL_QUALITY`, and `HEALTH_STATE_VALUATION`. (Introduction; Materials and methods, “Preference elicitation survey”)
- Design: `QUANTITATIVE_EMPIRICAL`; `LONGITUDINAL_REPEATED`; `WITHIN_PERSON` and `BETWEEN_GROUP`; `NOT_APPLICABLE` allocation. (Materials and methods, “Sample” and “Test-retest”) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Results, Conclusion)
### Study structure and typed uses

- One Study has a matched test-retest sample of 220 German adults: 73 general-population respondents and 147 patients with diabetes or rheumatic disease. Sample stage is `ANALYZED`. (Abstract, Methods; Results, “Sample characteristics”)
- One DataUse has `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. Collection occurred twice, two weeks apart. (Materials and methods, “Sample”)
- InstrumentUse: “EQ-HWB-S” has `DIRECT_CURRENT_ACTIVITY` with `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. “adapted version of the EQ-VAS” has `DIRECT_CURRENT_ACTIVITY` with `CURRENT_HEALTH_MEASUREMENT`. (Materials and methods, “Preference elicitation survey”)
- MethodUse: “Online elicitation of Personal Utility Functions (OPUF) approach” has `DIRECT_CURRENT_ACTIVITY` with `PREFERENCE_ELICITATION`. Its separate `CURRENT_STUDY_OBJECT` function is gap G-D001-01. (Introduction; Materials and methods)
- ModelUse: “additive model” has `SCORING` and `PRIMARY_REPORTED`. Other exact analysis labels include “intraclass correlation coefficient,” “Spearman’s rank correlation coefficient,” and “linear regression.” (Materials and methods, “Data analysis”)
### Findings, limitations, products, and concepts

- Outcome families are `METHOD_PERFORMANCE_OR_DATA_QUALITY` and `PREFERENCE_OR_UTILITY`. Individual tasks usually had poor or moderate agreement, but aggregate utility decrements were similar. (Abstract, Results; Discussion)
- Only 42.27% chose the same top dimension. The pairwise task had about 83% agreement, while the individual anchoring factor had poor agreement. (Discussion)
- Product: test and retest aggregate “value set” outputs map to `VALUE_SET`. The paper reports development, not external approval or deployment. (Materials and methods, “Utility decrements and value set”; Conclusion)
- Reported limitations include exclusion of illogical or unusable responses, possible VAS response spreading, online-panel selection, one German setting, and weak comparability with standard TTO or DCE reliability tests. (Discussion)
- Concepts: individual reliability, aggregate reliability, response shift, digital literacy, task complexity, and anchoring consistency. (Discussion)
### Gaps and source conflicts

- G-D001-01 — `UNMAPPED_VALUE`; affected key: `method_function`; evidence: OPUF is the object of the test-retest assessment; importance: direct use and evaluation-object use must remain separate; proposed resolution: review a method-function value such as `METHOD_EVALUATION_OBJECT`. (Abstract; Discussion)
- No source contradiction was found after the distinct individual and aggregate results were kept separate.
### High-value canonical terms

- Registry labels: “EQ-HWB-S,” “adapted version of the EQ-VAS,” “Online elicitation of Personal Utility Functions (OPUF) approach,” “intraclass correlation coefficient,” “Spearman’s rank correlation coefficient,” “additive model,” and “R version 4.3.1.” (Materials and methods) Discovery concepts: test-retest reliability, dimension ranks, swing weights, level ratings, anchoring factor, utility decrement, and personal utility function. (Materials and methods, “Test-retest”)
## D002 — 10.1007/s40273-019-00854-w

### Assessment and classification

- Title: “Measurement Properties of Commonly Used Generic Preference-Based Measures in East and South-East Asia: A Systematic Review.” The systematic combination of prior evidence is primary, so the family is `EVIDENCE_SYNTHESIS`. (Abstract)
- Ranked purposes: `EVIDENCE_SYNTHESIS` and `MEASUREMENT_PROPERTY_EVALUATION`. (Abstract, Objectives)
- Design: `EVIDENCE_SYNTHESIS`; `VARIABLE_SOURCE_TIME`; `BETWEEN_INSTRUMENT` and `BETWEEN_CONTEXT`; `NOT_APPLICABLE` allocation; synthesis designs `SYSTEMATIC_REVIEW` and `NARRATIVE_SYNTHESIS`. (Methods) Status: `REVIEW_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusions)
### Study structure and typed uses

- One review Study includes 79 papers and 1,504 paper-defined studies. Evidence-unit sample stage is `INCLUDED_EVIDENCE`. (Abstract, Results)
- One review DataUse has `REVIEW_EXTRACTED_EVIDENCE` and `DOCUMENT`. Searches covered MEDLINE, EMBASE, PsycINFO, and PubMed through August 2019. (Methods, “Identification and Selection of Studies”)
- InstrumentUse records use `CURRENT_STUDY_OBJECT` and `EVIDENCE_SYNTHESIS_TARGET` for “EQ-5D-3L,” “EQ-5D-5L,” “EQ-VAS,” “SF-6D,” “HUI2,” “HUI3,” “QWB,” “15D,” and “AQOL.” (Methods)
- ProtocolUse: “COSMIN guideline” has `DIRECT_CURRENT_ACTIVITY` and `CRITICAL_APPRAISAL_PROTOCOL`. The “Risk of Bias” assessment tool and “COSMIN Grading of Recommendation Assessment, Development, and Evaluation (GRADE)” retain exact source labels. (Methods)
- MethodUse: the database search has `EVIDENCE_IDENTIFICATION`; the cross-study assessment has `EVIDENCE_SYNTHESIS`. (Methods)
### Findings, limitations, products, and concepts

- Outcome family is `MEASUREMENT_PROPERTY`. EQ-5D had sufficient construct validity and responsiveness in many populations. Its test-retest reliability was inconsistent or insufficient in almost all assessed populations. (Abstract, Results; Discussion)
- SF-6D and EQ-VAS had inconsistent construct validity in some populations. Evidence for HUI and QWB was scarce, and no relevant studies were found for AQOL or 15D. (Abstract; Results)
- Reported limitations are modified COSMIN methods, exclusion of non-English papers, and no separation of language versions. (Discussion)
- Concepts: construct validity, known-groups validity, convergent validity, test-retest reliability, responsiveness, methodological quality, and regional measurement performance. (Introduction; Methods)
### Gaps and source conflicts

- The current controlled values fit the review. No required controlled-field gap or internal source contradiction was found.
### High-value canonical terms

- Registry labels: “COnsensus-based Standards for the selection of health Measurement Instruments (COSMIN) guideline,” “International Classification of Diseases, 11th Revision (ICD-11),” and the nine instrument labels listed above. (Methods) Discovery concepts: generic preference-based measure, population-specific measurement property, risk of bias, quality of evidence, and Asian population. (Methods, “Assessment of the Preference-Based Measures”)
## D003 — 10.1186/s41687-024-00761-5

### Assessment and classification

- Title: “Cross-cultural adaptation and psychometric validation of the Chichewa (Malawi) PedsQL™ 4.0 Generic Core Scales child self-report and PedsQL™ 4.0 GCS teen self-report.” A new language version is the main output, so the family is `INSTRUMENT_VERSION_DEVELOPMENT`. (Title, Abstract)
- Ranked purposes: `TRANSLATION_AND_CULTURAL_ADAPTATION`, `INSTRUMENT_DEVELOPMENT`, `MEASUREMENT_PROPERTY_EVALUATION`, and `CONTENT_VALIDITY_EVALUATION`. (Abstract; Methods)
- Two StudyParts are present: `TRANSLATION_ADAPTATION_WORKFLOW` plus `QUALITATIVE_INQUIRY` for adaptation, and `QUANTITATIVE_EMPIRICAL` for psychometric validation. Both are `CROSS_SECTIONAL`; comparison is `BETWEEN_GROUP`; allocation is `NOT_APPLICABLE`. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusion)
### Study structure and typed uses

- Adaptation part: ten healthy participants completed cognitive interviews. Validation part: 289 literate children aged 8–17 years from schools and a hospital in Blantyre. Both sample stages are `ANALYZED`. (Methods, “Cognitive interviews” and “Participants”)
- Both DataUses have `CURRENT_STUDY_COLLECTION`; the levels are `QUALITATIVE_MATERIAL` and `PARTICIPANT_RESPONSE`, respectively. (Methods)
- InstrumentUse: the English (US) child and teen versions have `DIRECT_CURRENT_ACTIVITY` with `TRANSLATION_SOURCE`; the Chichewa versions have `DIRECT_CURRENT_ACTIVITY` with `TRANSLATION_TARGET`, `DEVELOPMENT_OBJECT`, and `CONTENT_TEST_OBJECT`. Separate uses preserve each function. (Methods, “The instruments” and “Translation process”)
- ProtocolUse: “standard PedsQL™ 4.0 GCS translation protocol (forward and backward)” has `TRANSLATION_PROTOCOL`; “cognitive interview protocols” has `QUALITY_CONTROL_PROTOCOL`. (Methods, “Translation process”)
- MethodUse labels include “cognitive interviews,” `QUALITATIVE_DATA_COLLECTION`, and “Classical psychometrics,” `MEASUREMENT_PROPERTY_ANALYSIS`. (Abstract; Methods)
### Findings, limitations, products, and concepts

- Outcome families are `CONTENT_VALIDITY` and `MEASUREMENT_PROPERTY`. Six items needed cultural adaptation. One key change disambiguated the Chichewa word “kusamba.” (Abstract; Results, “Translation process” and “Cognitive interviews”)
- Internal consistency was acceptable. Convergent validity was generally strong. Other validity results were mixed, and self-completion was difficult for some younger children. (Abstract; Discussion)
- Product: “Chichewa (Malawi) PedsQL™ 4.0 GCS child self-report and teen self-report” maps to `INSTRUMENT_VERSION`. The source reports that Mapi Research Trust approved the pre-final versions before administration. (Methods, “Cognitive interviews”; Conclusion)
- Reported limitations are cognitive adaptation with healthy participants only and one-time psychometric data, which prevented tests of reliability and responsiveness. (Discussion)
- Concepts: linguistic equivalence, conceptual equivalence, cultural connotation, literacy, response-option use, and interviewer assistance. (Results; Discussion)
### Gaps and source conflicts

- SourceConflict SC-D003-01: the Abstract first uses “Generic Core Scales (GSC),” while the title, Methods, and later text use “Generic Core Scales (GCS).” Preserve both labels and use no silent correction. (Title; Abstract, Background; Methods)
### High-value canonical terms

- Registry labels: “PedsQL™ 4.0 Generic Core Scales,” “PedsQL™ 4.0 GCS child self-report,” “PedsQL™ 4.0 GCS teen self-report,” “standard PedsQL™ 4.0 GCS translation protocol (forward and backward),” and “IBM SPSS 26.0.0 for Mac.” (Methods) Discovery concepts: Chichewa, Malawi, cross-cultural adaptation, item redundancy, adjacent endorsement frequency, known-groups validity, and item convergent/discriminant validity. (Methods)
## D004 — 10.1007/s40271-022-00573-z

### Assessment and classification

- Title: “Exploring the Comparability of Face-to-Face Versus Video Conference-Based Composite Time Trade-Off Interviews.” The main decision concerns administration-mode performance, so the family is `METHODS_RESEARCH`. (Title, Abstract)
- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `METHOD_OR_PROTOCOL_QUALITY`, and `IMPLEMENTATION_EVALUATION`. (Abstract, Background and Methods)
- Design: `QUANTITATIVE_EMPIRICAL`; `VARIABLE_SOURCE_TIME`; `BETWEEN_CONTEXT`; `NONRANDOMIZED` allocation to interview mode. (Methods, “Sampling and Data Collection” and “Statistical Comparison”) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusion)
### Study structure and typed uses

- Two country StudyParts preserve the Belgium and Spain samples, interviewers, collection dates, and source studies. Each part has face-to-face and videoconference administration records. (Methods, “Sampling and Data Collection”)
- DataUse has `PRIOR_RESEARCH_COLLECTION` and `PARTICIPANT_RESPONSE` for the two national valuation studies. (Methods, “The EQ-5D-Y-3L Valuation Protocol”)
- InstrumentUse: “EQ-5D-Y-3L” has `SOURCE_STUDY_ACTIVITY` with `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`; its self-report warm-up use has `CURRENT_HEALTH_MEASUREMENT`. (Methods, “Interview Structure”)
- MethodUse: “composite time trade-off (cTTO)” has `SOURCE_STUDY_ACTIVITY` and `PREFERENCE_ELICITATION`. ProtocolUse: “international EQ-5D-Y-3L valuation protocol” has `SOURCE_STUDY_ACTIVITY` and `VALUATION_PROTOCOL`. (Methods)
- Administration preserves “face-to-face,” “Skype,” and “Zoom,” with interviewer operation, verbal response, audio/video connection, and screen sharing. TaskDesign keeps ten states, random state order, and the child perspective. (Methods)
### Findings, limitations, products, and concepts

- Outcome family is `METHOD_PERFORMANCE_OR_DATA_QUALITY`. No engagement outcome showed worse results for videoconference interviews than for later face-to-face interviews. (Abstract; Discussion)
- Interviewer and respondent engagement, response distributions, and face-validity results were similar. The conclusion found no evidence of reduced cTTO data quality. (Results; Conclusion)
- Reported limitations are nonrandom mode assignment, learning effects, different collection periods and samples, COVID-19 effects, IT-skill selection, and reduced power after subgroup splits. (Discussion)
- Concepts: interviewer engagement, respondent engagement, mode of administration, face validity, learning effect, and feedback module. (Methods, “Metrics Definition”)
### Gaps and source conflicts

- The Administration structure carries the studied mode, so no new method-function value is necessary. No internal source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-Y-3L,” “composite time trade-off (cTTO),” “international EQ-5D-Y-3L valuation protocol,” “EuroQol Valuation Technology (EQ-VT),” “Skype,” and “Zoom.” (Methods) Discovery concepts: better-than-dead, worse-than-dead, half-year unit, negative value, interviewer effect, and Bonferroni correction. (Methods)
## D005 — 10.1007/s40273-024-01444-1

### Assessment and classification

- Title: “Measuring Effectiveness Based on Patient Experience (Instead of QALYs) in US Value Assessments.” Method feasibility and choice are the main decision, so the family is `METHODS_RESEARCH`. (Abstract; Conclusions)
- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `HEALTH_STATE_VALUATION`, and `PREFERENCE_COMPARISON`. (Introduction; Methods)
- Design: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE` allocation. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Results)
### Study structure and typed uses

- One secondary-analysis Study uses 179 parents from a 2023 US child-health valuation survey, with overlapping mother and father subgroups of 99 and 80. Sample stage is `ANALYZED`. (Introduction; Methods)
- DataUse has `PRIOR_RESEARCH_COLLECTION` and `PARTICIPANT_RESPONSE`. (Introduction, final paragraphs; Methods)
- InstrumentUse: “EQ-5D-Y-3L” has `DIRECT_CURRENT_ACTIVITY` with `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. (Methods)
- MethodUse: “discrete choice experiment (DCE) with kaizen tasks” and “paired comparisons” have `SOURCE_STUDY_ACTIVITY` with `PREFERENCE_ELICITATION`; the current analysis uses “conditional logit models” and “cluster bootstrap technique.” (Methods)
- TaskDesign preserves ten kaizen tasks, five coma comparisons, a 10-year-old child, one-week health duration, and parent, mother, and father perspectives. (Methods)
### Findings, limitations, products, and concepts

- Outcome families are `PREFERENCE_OR_UTILITY` and `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Nearly all estimated child HRQoL gains were positive. Mothers valued the child’s feelings more than fathers. (Results, Table 1)
- From the parent perspective, state 33333 had an experience-scale value of −0.294 and was worse than “being in a coma.” (Results)
- Product: “values on an experience scale” maps to `VALUE_SET`. The source says these are not standard Y-3L value sets. (Results; Discussion)
- Reported limitations are exclusion of life expectancy, weak comparability across patient perspectives, possible perspective selection, adult valuation of child health, specialized methods, and no open-source software. (Discussion)
- Concepts: experience scaling, no experience, stakeholder perspective, anti-discrimination, and separation of HRQoL from life expectancy. (Discussion)
### Gaps and source conflicts

- Existing values distinguish method research from value-set development. No controlled-field gap or source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-Y-3L,” “discrete choice experiment (DCE) with kaizen tasks,” “paired comparisons,” “conditional logit models,” and “cluster bootstrap technique.” (Methods) Discovery concepts: experience scale, patient experience, parent perspective, mother perspective, father perspective, QALY, and “being in a coma.” (Introduction; Results)
## D006 — 10.1097/mlr.0000000000002315

### Assessment and classification

- Title: “Can Patient-Reported Outcome Measures Help Predict Unplanned Hospital Readmission?” The primary use is prediction for follow-up care, so the family is `APPLIED_USE_RESEARCH`. (Abstract, Objectives and Conclusions)
- Ranked purposes: `DECISION_SUPPORT_DEVELOPMENT`, `IMPLEMENTATION_EVALUATION`, and `OUTCOME_DESCRIPTION`. (Abstract; Discussion)
- Design: `QUANTITATIVE_EMPIRICAL` and `MODEL_BASED`; `LONGITUDINAL_REPEATED`; `BETWEEN_INSTRUMENT`; `NOT_APPLICABLE` allocation. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusions)
### Study structure and typed uses

- One linked retrospective cohort has 11,177 adults discharged from acute care in British Columbia. Sample stage is `ANALYZED`. (Methods, “Study Population”)
- DataUses have `ROUTINE_SERVICE_COLLECTION` and `PARTICIPANT_RESPONSE` for the Acute Inpatient Survey, and `ROUTINE_SERVICE_COLLECTION` and `DOCUMENT` for linked administrative records. (Methods, “Study Design and Data Sources”)
- InstrumentUse: “EQ-5D-5L” and “Veterans RAND 12-Item Health Survey (VR-12)” have `INPUT_DATA_PROVENANCE` and `PREDICTOR_MEASURE`. Their collection context is the source survey. (Methods, “Study Design and Data Sources” and “Predictors”)
- ModelUse: “Cox Landmark Supermodel” has `STATISTICAL_ESTIMATION` and `PRIMARY_REPORTED`; “Base” is `COMPARATOR`; “EQ-5D-5L-enhanced” and “VR-12-enhanced” are `CANDIDATE`. (Methods, “Model Derivation”)
- ProtocolUse: “Transparent Reporting of a Multivariable Prediction Model for Individual Prognosis or Diagnosis (TRIPOD) guidelines” has `REPORTING_GUIDELINE`. (Methods)
### Findings, limitations, products, and concepts

- Model-performance outcomes map to `METHOD_PERFORMANCE_OR_DATA_QUALITY`. PROMs gave modest and consistent discrimination gains, with larger gains for Ambulatory Care Sensitive Conditions. (Abstract; Discussion)
- At the 180-day horizon, the C-index rose from 0.762 for Base to 0.774 with EQ-5D-5L and 0.782 with VR-12. All models had adequate calibration. (Abstract, Results)
- Reported limitations include response selection, PROM collection weeks after discharge, missed early readmissions, one PROM observation carried forward, and need for external validation. (Discussion, “Strengths and Limitations”)
- Concepts: postdischarge monitoring, ongoing care management, landmark time, discrimination, calibration, and Ambulatory Care Sensitive Conditions. (Methods; Discussion)
### Gaps and source conflicts

- G-D006-01 — `UNMAPPED_VALUE`; affected key: `outcome_family`; evidence: the primary event is unplanned emergency-department use or acute-care readmission; importance: it is not health status, implementation, economic burden, or method performance; proposed resolution: review a distinct value such as `HEALTH_SERVICE_USE_OR_CLINICAL_EVENT`. (Methods, “Outcome”)
- No source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-5L,” “Veterans RAND 12-Item Health Survey (VR-12),” “Acute Inpatient Survey,” “Cox Landmark Supermodel,” “National Ambulatory Care Reporting System,” and “Discharge Abstract Database.” (Methods) Discovery concepts: unplanned readmission, PROM-enhanced prediction, administrative-data baseline, immortal time bias, and postdischarge risk. (Methods; Discussion)
## D007 — 10.1177/0272989X251380556

### Assessment and classification

- Title: “Uncertainty around Health State Values Used in Cost-Effectiveness Analysis: How It Arises and How to Deal with It.” Its taxonomy and process account are the main output, so the family is `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. (Abstract; Conclusions)
- Research purpose is `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. (Abstract)
- Design: `CONCEPTUAL`; `NOT_APPLICABLE` time; `NONCOMPARATIVE`; `NOT_APPLICABLE` allocation. Data origins are `CONCEPTUAL_MATERIAL` and `DOCUMENTARY_SOURCE`. (Abstract; “What Do We Mean by Uncertainty?”) Status: `CONCEPTUAL_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusions)
### Study structure and typed uses

- One conceptual Study has no participant sample. Its source materials are prior methodological and policy literature. (Introduction; Discussion)
- The paper defines four uncertainty types and traces them through valuation studies, profile data, mapping, disease-state studies, meta-analysis, and cost-effectiveness modeling. (Sections “What Do We Mean by Uncertainty?” and “How Uncertainty … Combines”)
- InstrumentUse records for “EQ-5D,” “SF-6D,” “HUI,” “EQ-5D-5L,” and “EQ-5D-3L” have `DISCUSSION_ONLY` and `REFERENCE_ONLY`. (Section “How Uncertainty … Combines”; Discussion)
- Methods such as mapping, meta-analysis, and sensitivity analysis are discussion concepts, not direct MethodUses. (Sections “Mapping,” “Meta-Analysis,” and “Cost-Effectiveness Modeling”)
### Findings, limitations, products, and concepts

- Outcome family is `CONCEPTUAL_CLASSIFICATION`. The four types are “variability,” “heterogeneity,” “statistical uncertainty,” and “methodological variation.” (Section “What Do We Mean by Uncertainty?”)
- Uncertainty accumulates through linked study stages and is not adequately carried into QALY and cost-effectiveness estimates. (Abstract; Conclusions)
- Product: “Sources of uncertainty in health state values” in Figure 1 and Table 1 maps to `TAXONOMY_OR_FRAMEWORK`. (Figure 1; Table 1)
- Source-reported scope limits are that the list is not exhaustive, the article has little empirical evidence on relative importance, and it focuses on valuation studies instead of all sources. (Introduction; “Sources of Uncertainty within Valuation Studies”)
- Concepts: health state value, HDS-V, inherited uncertainty, point estimate, variance/covariance matrix, QALY, and ICER. (Abstract; Discussion)
### Gaps and source conflicts

- Open Concept records carry the uncertainty types without new controlled values. No controlled-field gap or source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-5L,” “EQ-5D-3L,” “SF-6D,” “HUI,” and “Measurement and Valuation of Health study.” (Sections “How Uncertainty … Combines” and Discussion) Discovery concepts: variability, heterogeneity, statistical uncertainty, methodological variation, parameter uncertainty, model specification, and value-set reporting. (Table 1; Discussion)
## D008 — 10.3961/jpmph.22.151

### Assessment and classification

- Title: “Perceptions of the General Public About Health-related Quality of Life and the EQ-5D Questionnaire: A Qualitative Study in Korea.” The main decision concerns EQ-5D content adequacy, so the family is `MEASUREMENT_PROPERTY_EVALUATION`. (Abstract; Discussion)
- Ranked purposes: `CONTENT_VALIDITY_EVALUATION` and `OUTCOME_DESCRIPTION`. (Introduction; Discussion)
- Design: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `NONCOMPARATIVE`; `NOT_APPLICABLE` allocation. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusion)
### Study structure and typed uses

- One Study has 20 Korean general-public participants selected by purposive sampling. Sample stage is `ANALYZED`. (Methods, “Research Participants”; Results)
- DataUse has `CURRENT_STUDY_COLLECTION` and `QUALITATIVE_MATERIAL` from transcripts and field notes. (Methods, “In-depth Interview Procedure” and “Analysis”)
- InstrumentUse: “EQ-5D-5L” and “EQ-VAS” have `CURRENT_STUDY_OBJECT` and `CONTENT_TEST_OBJECT`. They were shown for comment, not used to measure participant health. (Methods, “In-depth Interview Procedure”)
- MethodUse: “face-to-face, in-depth interviews” has `QUALITATIVE_DATA_COLLECTION`; “directive content analysis” has `QUALITATIVE_ANALYSIS`. (Abstract; Methods)
- ProtocolUse: “Consolidated Criteria for Reporting Qualitative Research (COREQ) checklist” has `REPORTING_GUIDELINE`. (Methods)
### Findings, limitations, products, and concepts

- Outcome family is `CONTENT_VALIDITY`. The analysis produced 734 codes in four categories. Physical health was basic, but mental and social health were also important. (Abstract; Results, “Identified Concepts”)
- Participants valued the simplicity of EQ-5D-5L but asked for more mental and social content. They liked EQ-VAS presentation but questioned score comparability. (Abstract; Discussion)
- The source reports limited generalizability because of the qualitative design. It calls for tests of the generated hypotheses and comparisons with other countries. (Discussion)
- Concepts: multidimensional health, social relationships, positive health, usual activities, cross-person EQ-VAS comparability, and cultural adaptation. (Discussion; Conclusion)
### Gaps and source conflicts

- Existing content-validity structures fit the study. No controlled-field gap or source contradiction was found.
### High-value canonical terms

- Registry labels: “EuroQoL 5-Dimension 5-Level (EQ-5D-5L),” “EuroQoL visual analogue scale (EQ-VAS),” “Consolidated Criteria for Reporting Qualitative Research (COREQ) checklist,” and “directive content analysis.” (Methods) Discovery concepts: health definition and recognition, significant factors in health, mental health, social health, usual activities, and reference points. (Results; Discussion)
## D009 — 10.1186/s12955-023-02115-z

### Assessment and classification

- Title: “Experience-based health state valuation using the EQ VAS: a register-based study of the EQ-5D-3L among nine patient groups in Sweden.” Empirical preferences are primary without current value-set development, so the family is `HEALTH_PREFERENCE_RESEARCH`. (Abstract; Conclusions)
- Ranked purposes: `HEALTH_STATE_VALUATION` and `PREFERENCE_COMPARISON`. (Background; Methods)
- Patient parts are `QUANTITATIVE_EMPIRICAL`, `LONGITUDINAL_REPEATED`, `WITHIN_PERSON`, and `BETWEEN_GROUP`. The population comparator is `CROSS_SECTIONAL`. Allocation is `NOT_APPLICABLE`. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusions)
### Study structure and typed uses

- Ten StudyParts preserve nine Swedish National Quality Register patient groups and one general-population comparator. Patient records total 172,070; the comparator has 41,761 participants. Sample stage is `ANALYZED`. (Methods, “Data” and “Sample size”)
- Register DataUses have `ROUTINE_SERVICE_COLLECTION` and `PARTICIPANT_RESPONSE`. The Scania 2004 and Stockholm 2006 survey data have `PRIOR_RESEARCH_COLLECTION`. The Swedish value set has `PUBLISHED_MODEL_INPUT`. (Methods, “Data”)
- InstrumentUse: “EQ-5D-3L” has `INPUT_DATA_PROVENANCE` with `CURRENT_HEALTH_MEASUREMENT` and `HEALTH_STATE_DESCRIPTION`; “EQ VAS” has source-study `CURRENT_HEALTH_MEASUREMENT` and current-study `VALUATION_TARGET` uses. (Methods)
- ScoringUse links EQ-5D-3L responses to the “Swedish experience-based EQ-5D-3L VAS value set.” (Methods, “Data”)
- ModelUse: “ordinary least squares (OLS) models” and “two-level random slope and random intercept models” have `STATISTICAL_ESTIMATION`; OLS is `PRIMARY_REPORTED` and multilevel models are `SENSITIVITY`. (Methods, “Data analysis”)
### Findings, limitations, products, and concepts

- Outcome families are `PREFERENCE_OR_UTILITY` and `HEALTH_STATUS_OR_EQ_VAS`. Values were generally ordered by severity at baseline and one year. Anxiety/depression had the largest decrement in most groups. (Abstract; Discussion)
- Values for the same states changed over time and differed by patient group. Self-care level 3 was the main source of inconsistent decrements. (Abstract; Conclusions)
- Reported limitations include collection differences between registers, no dead anchor, no choice or trade-off in EQ VAS, end-aversion bias, and residual disagreement between EQ VAS and EQ-5D-3L. (Discussion)
- Concepts: experience-based valuation, patient value, disease stage, severity consistency, own-health perspective, and broader EQ VAS construct. (Discussion; Conclusions)
### Gaps and source conflicts

- The source proposes only the potential for future experience-based value sets. It does not report a current reusable Product. No controlled-field gap or contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-3L,” “EQ VAS,” “Swedish experience-based EQ-5D-3L VAS value set,” “ordinary least squares (OLS) models,” “Spearman’s rank correlation,” “R version 3.5.0/3.5.1,” and “SAS version 9.4.” (Methods) Discovery concepts: National Quality Register, baseline, one-year follow-up, experience-based value, hypothetical perspective, and patient valuation. (Background; Methods)
## D010 — 10.1007/s10198-023-01612-8

### Assessment and classification

- Title: “The effect of duration and time preference on the gap between adult and child health state valuations in time trade-off.” The main decision is about valuation-method assumptions, so the family is `METHODS_RESEARCH`. (Abstract; Introduction)
- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `PREFERENCE_COMPARISON`, and `HEALTH_STATE_VALUATION`. (Introduction)
- Design: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `WITHIN_PERSON`; `NOT_APPLICABLE` allocation. Task-order randomization stays in TaskDesign. (Experiment, “Design and participants” and “TTO operationalization”) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusion)
### Study structure and typed uses

- One Study has 151 UK adults who completed all perspective and duration conditions in interviewer-led video calls. Sample stage is `ANALYZED`. (Abstract; Experiment)
- DataUse has `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. (Experiment)
- InstrumentUse: “EQ-5D-Y-3L” has `DIRECT_CURRENT_ACTIVITY` with `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. (Introduction; Experiment)
- MethodUse: “composite time trade-off (cTTO)” and “Direct Method” have `DIRECT_CURRENT_ACTIVITY` with `PREFERENCE_ELICITATION`. The cTTO evaluation-object use is gap G-D010-01. (Method; Experiment)
- ProtocolUse: “EQ-VT protocol” has `VALUATION_PROTOCOL`. ModelUse: “general QALY model” and “mixed effects regressions” have `SCORING` and `STATISTICAL_ESTIMATION`, respectively. (Method; Analysis)
- TaskDesign preserves adult and 10-year-old child perspectives, four health states, 10- and 20-year durations, a 10-year lead time, and randomized block, task, and state order. (Experiment)
### Findings, limitations, products, and concepts

- Outcome family is `PREFERENCE_OR_UTILITY`. Child-perspective utilities were higher only after covariate control. The effect disappeared after adjustment for perspective-specific time preference. (Abstract; Discussion)
- The 10- and 20-year duration conditions did not differ. The authors infer that time preference partly drives the child-adult gap. (Abstract; Conclusion)
- Reported limitations include video interviews, different lower utility bounds by duration, possible sequence effects, no validity checks for the time-preference task, and only a partial explanation of perspective effects. (Discussion)
- Concepts: gauge duration, time preference, child perspective, adult perspective, lead time, constant proportional trade-off, and discount function. (Introduction; Method)
### Gaps and source conflicts

- G-D010-01 — `UNMAPPED_VALUE`; affected key: `method_function`; evidence: cTTO duration and correction are evaluated as method features; importance: `PREFERENCE_ELICITATION` describes direct use, not the evaluation-object role; proposed resolution: review `METHOD_EVALUATION_OBJECT`. (Introduction; Discussion)
- No source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-Y-3L,” “composite time trade-off (cTTO),” “Direct Method,” “EQ-VT protocol,” “general QALY model,” “mixed effects regressions,” “Zoom,” “Google Meet,” and “Shiny.” (Method; Experiment) Discovery concepts: child-adult valuation gap, perspective-specific time preference, worse than dead, discounting, dominance violation, and duration effect. (Method; Discussion)
## D011 — 10.1007/s10198-025-01823-1

### Assessment and classification

- Title: “Nothing about us, without us? A reflection on and call for involving children in the process of valuing child health.” The classified argument framework is the main output, so the family is `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. (Abstract; “Nothing about us without us”)
- Research purpose is `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. (Abstract)
- Design: `CONCEPTUAL`; `NOT_APPLICABLE` time; `NONCOMPARATIVE`; `NOT_APPLICABLE` allocation. Data origins are `DOCUMENTARY_SOURCE` and `CONCEPTUAL_MATERIAL`. (Section “Public involvement in decisions on health(care)”) Status: `OPINION_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Title; Abstract)
### Study structure and typed uses

- One conceptual Study has no participant sample. The authors used search engines and snowballing to identify arguments in academic and policy documents. (Section “Public involvement in decisions on health(care)”)
- The paper classifies 13 arguments as input, process, or outcome arguments and assesses their relevance to child involvement in health-state valuation. (Table 1; Table 2)
- InstrumentUse: “EQ-5D-Y” and “EQ-5D-Y-3L” have `DISCUSSION_ONLY` and `REFERENCE_ONLY`. (Sections “Valuing child health” and “Involving children”)
- Method labels “Time Trade-Off (TTO)” and “Discrete Choice Experiments (DCEs)” are discussion terms, not current MethodUses. (Section “Valuing child health”)
### Findings, limitations, products, and concepts

- Outcome family is `CONCEPTUAL_CLASSIFICATION`. Most broader public-involvement arguments also apply to child involvement in the valuation process. (Table 2; “Arguments for involving children”)
- The authors call for a change from whether children must be involved to how they can be involved, including approaches outside direct valuation tasks. (Abstract; final section)
- Product: the 13-argument input/process/outcome classification and its child-HSV applicability table map to `TAXONOMY_OR_FRAMEWORK`. (Tables 1 and 2)
- Reported scope limits are a non-exhaustive argument list, no separation by child age, and unresolved ethical, cognitive, consensus, and method-quality questions. (Tables 1 and 2; final section)
- Concepts: child involvement, health-state valuation process, health-state valuation task, legitimacy, lived expertise, paternalism, and deliberative group. (Final section)
### Gaps and source conflicts

- Open Concept and Product records can carry the proposed participation forms. No controlled-field gap or source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D-Y,” “EQ-5D-Y-3L valuation protocol,” “Time Trade-Off (TTO),” “Discrete Choice Experiments (DCEs),” and “Youth Advisory Network.” (Sections “Valuing child health” and “Involving children”) Discovery concepts: intrinsic value, democratic participation, consumer voice, taxpayer role, decision legitimacy, decision quality, and health-system responsiveness. (Tables 1 and 2)
## D012 — 10.1007/s11136-025-04038-2

### Assessment and classification

- Title: “Developing a quality of life framework from the perspective of laypeople: a qualitative comparison with the EQ-HWB framework.” The new framework is primary, so the family is `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`. (Abstract)
- Ranked purposes: `CONCEPTUAL_FRAMEWORK_DEVELOPMENT` and `CONTENT_VALIDITY_EVALUATION`. (Introduction)
- Design: `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `BETWEEN_INSTRUMENT`; `NOT_APPLICABLE` allocation. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusion)
### Study structure and typed uses

- One Study has 30 Chinese lay participants: ten healthy people, ten patients, and ten informal caregivers. Sample stage is `ANALYZED`. (Methods, “Participant selection and setting”; Results)
- DataUse has `CURRENT_STUDY_COLLECTION` and `QUALITATIVE_MATERIAL` from verbatim interviews. (Methods, “Data collection” and “Analysis”)
- InstrumentUse: “EQ-HWB” has `CURRENT_STUDY_OBJECT` with `CONTENT_TEST_OBJECT`; its 96 candidate items supplied the deductive codebook. (Methods, “Familiarization and coding”)
- MethodUse: “individual semi-structured interviews” has `QUALITATIVE_DATA_COLLECTION`; “thematic analysis” and “thematic framework approach” have `QUALITATIVE_ANALYSIS`. (Abstract; Methods)
- ProtocolUse: “consolidated criteria for reporting qualitative research (COREQ)” has `REPORTING_GUIDELINE`. (Methods)
### Findings, limitations, products, and concepts

- Outcome families are `CONCEPTUAL_CLASSIFICATION` and `CONTENT_VALIDITY`. The 187 retained codes formed eight themes: feeling and emotion, cognition, self-identity, coping, physical sensation, relationship, activity, and mindset. (Abstract; Results)
- Seven of eight themes aligned with the EQ-HWB framework. “Mindset” was additional. Theme alignment was 88%, and sub-theme alignment was 68%. (Abstract; Results, “Comparison with the EQ-HWB”)
- Product: the “Chinese QoL conceptual framework” maps to `TAXONOMY_OR_FRAMEWORK`. (Abstract; Results)
- Reported limitations are limited sample diversity in Harbin, no hospitalized severe cases, hard translation of some terms, no prespecified saturation rule, and subjective saturation assessment. (Limitation)
- Concepts: mindset, coping, positive/negative energy, autonomy, dependence, sleep, and holistic quality of life. (Discussion)
### Gaps and source conflicts

- Existing Concept and Product structures preserve “mindset” as an open concept. No new controlled value or source contradiction is necessary.
### High-value canonical terms

- Registry labels: “EuroQol Health and Wellbeing (EQ-HWB),” “Consensus-based Standard for the selection of health Measurement Instruments (COSMIN),” “COREQ,” “NVivo 14,” and “Gale’s thematic analysis methodology.” (Introduction; Methods) Discovery concepts: Chinese QoL conceptual framework, comprehensiveness, mindset, coping, physical sensation, relationship, activity, and cultural meaning. (Results; Discussion)
## D013 — 10.1007/s40271-024-00708-4

### Assessment and classification

- Title: “The Performance of Kaizen Tasks Across Three Online Discrete Choice Experiment Surveys: An Evidence Synthesis.” Combination of prior evidence is primary, so the family is `EVIDENCE_SYNTHESIS`. (Title, Abstract)
- Ranked purposes: `EVIDENCE_SYNTHESIS`, `VALUATION_METHOD_EVALUATION`, and `METHOD_OR_PROTOCOL_QUALITY`. (Abstract; Introduction)
- Design: `EVIDENCE_SYNTHESIS` and `QUANTITATIVE_EMPIRICAL`; source parts are `CROSS_SECTIONAL`; comparisons are `BETWEEN_METHOD` and `BETWEEN_CONTEXT`; allocation is `NOT_APPLICABLE`; synthesis design is `NARRATIVE_SYNTHESIS`. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusions)
### Study structure and typed uses

- Three StudyParts preserve the 2020 US COVID-19 vaccination study, 2021 UK Children’s Surgery Outcome Reporting study, and 2023 US EQ-5D-Y-3L valuation study. (Methods, “Secondary Datasets”)
- DataUses have `PRIOR_RESEARCH_COLLECTION` and `PARTICIPANT_RESPONSE`. Analyzed samples are 652, 807, and 631, respectively. (Table 1)
- InstrumentUse: “EQ-5D-Y-3L” has `SOURCE_STUDY_ACTIVITY` with `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET`. Other source descriptive systems remain source-faithful open labels. (Methods; Table 1)
- MethodUse: “kaizen task” and “paired comparisons” have `SOURCE_STUDY_ACTIVITY` with `PREFERENCE_ELICITATION`. The current kaizen evaluation-object use is gap G-D013-01. (Introduction; Methods)
- ModelUse: “conditional logit” and “Zermelo–Bradley–Terry (ZBT) models” have `STATISTICAL_ESTIMATION` and `PRIMARY_REPORTED`. (Methods, “Primary Analyses”)
- TaskDesign preserves warm-up tasks, hold-outs, multi-level improvements, attribute order, blocks, and randomized task order. (Methods; Table 1)
### Findings, limitations, products, and concepts

- Outcome family is `METHOD_PERFORMANCE_OR_DATA_QUALITY`. Hold-outs appeared to halve positional behavior. All Y-3L main effects were positive and had strong predictive validity against paired comparisons. (Abstract; Results)
- CVP lacked multi-level improvements, and CSOR used fixed attribute order. These design features limited or confounded their estimates. (Results; Discussion)
- Product: the reusable Kaizen DCE design recommendations map to `IMPLEMENTATION_GUIDANCE`: use warm-ups, hold-outs, multi-level improvements, randomized attribute order, and smaller samples. (Abstract, Conclusions)
- Reported limits are the three available studies, confounding from the fixed CSOR order, no direct CVP logit main effects, and insufficient support for nominal attributes or interactions. (Methods; Discussion)
- Concepts: preference path, positional behavior, predictive validity, hold-out, multi-level improvement, and small-sample performance. (Introduction; Discussion)
### Gaps and source conflicts

- G-D013-01 — `UNMAPPED_VALUE`; affected key: `method_function`; evidence: kaizen-task performance is the current study object; importance: source-study elicitation must remain separate from current evaluation; proposed resolution: review `METHOD_EVALUATION_OBJECT`. (Abstract; Discussion)
- No source contradiction was found.
### High-value canonical terms

- Registry labels: “kaizen task,” “discrete choice experiment (DCE),” “paired comparisons,” “conditional logit,” “Zermelo–Bradley–Terry (ZBT) models,” “EQ-5D-Y-3L,” and “LimeSurvey.” (Introduction; Methods) Discovery concepts: continuous improvement, preference path, pick-one task, hold-out, attribute-order randomization, main effect, and positional behavior. (Introduction; Methods)
## D014 — 10.1017/S0266462326103602

### Assessment and classification

- Title: “What do HTA agencies need for generating health-related quality of life evidence? Findings from a global survey.” Current use and needs are primary, so the family is `APPLIED_USE_RESEARCH`. (Abstract; Introduction)
- Ranked purposes: `IMPLEMENTATION_EVALUATION` and `OUTCOME_DESCRIPTION`. (Abstract, Objectives)
- Design: `QUANTITATIVE_EMPIRICAL` and `QUALITATIVE_INQUIRY`; `CROSS_SECTIONAL`; `BETWEEN_CONTEXT`; `NOT_APPLICABLE` allocation; mixed-method integration is `CONVERGENT_PARALLEL`. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusions)
### Study structure and typed uses

- One Study has 238 HTA practitioners from 45 countries and 65 agencies. Sample stage is `COMPLETED`. Regional results use six region groups. (Results, “Sample characteristics”)
- DataUse has `CURRENT_STUDY_COLLECTION` with `PARTICIPANT_RESPONSE` for closed questions and `QUALITATIVE_MATERIAL` for open responses. (Methods, “Survey form” and “Statistical analysis”)
- InstrumentUse records use `CURRENT_STUDY_OBJECT` and `IMPLEMENTATION_OBJECT` for “EQ-5D,” “SF-6D,” and “EQ-5D-Y,” with other survey-named instruments kept in the same registry. (Results, “Use and importance of utility instruments”)
- MethodUse records for “time trade-off,” “visual analogue scale,” “standard gamble,” and “discrete choice experiment” use `CURRENT_STUDY_OBJECT`; their function is gap G-D014-01. (Results, “Use and importance of preference elicitation methods”)
- MethodUse: “descriptive analyses” has `QUANTITATIVE_ANALYSIS`; “structured content analysis” has `QUALITATIVE_ANALYSIS`; “forward-backward approach” has `QUALITY_CONTROL`. (Methods, “Statistical analysis”)
- Administration is anonymous online self-completion in Qualtrics, with open responses allowed in the participant’s language. (Methods, “Survey form”)
### Findings, limitations, products, and concepts

- Outcome family is `IMPLEMENTATION`. The most used instruments were EQ-5D, SF-6D, and EQ-5D-Y. The most used elicitation methods were time trade-off, visual analogue scale, and standard gamble. (Abstract; Results)
- Foreign general-public values were used more often than local values. Common problems were poor representativeness, small samples, model-data mismatch, and mixed methods or instruments. (Abstract; Results)
- The top global priorities were recent utility values, child and adolescent instruments, and instruments that cover health and social care. (Results, Table 4)
- Reported limitations include low country counts, uncertain respondent authority, EuroQol-network recruitment bias, no agency identifier, no reliable subgroup analysis, and unverified eligibility. (Discussion)
- Concepts: HTA practice, utility-data need, data quality, research priority, local preference, and foreign preference. (Discussion)
### Gaps and source conflicts

- G-D014-01 — `UNMAPPED_VALUE`; affected key: `method_function`; evidence: the survey examines method use and fitness without performing valuation; importance: `PREFERENCE_ELICITATION` would falsely state direct current use; proposed resolution: review a value such as `IMPLEMENTATION_OBJECT` for MethodUse. (Survey form; Results)
- No source contradiction was found.
### High-value canonical terms

- Registry labels: “EQ-5D,” “SF-6D,” “EQ-5D-Y,” “time trade-off,” “visual analogue scale,” “standard gamble,” “discrete choice experiment,” “Qualtrics,” and “STATA v14.” (Methods; Results) Discovery concepts: HTA agency, QALY evidence, multi-attribute utility instrument, local public preference, data representativeness, recent tariff, and research priority. (Introduction; Results)
## D015 — 10.1186/s12889-018-5706-0

### Assessment and classification

- Title: “Living in uncertainty due to floods and pollution: the health status and quality of life of people living on an unhealthy riverbank.” Health and well-being outcomes are primary, so the family is `HEALTH_OUTCOME_RESEARCH`. (Abstract)
- Research purpose is `OUTCOME_DESCRIPTION`. (Background, final paragraph)
- Design: `QUANTITATIVE_EMPIRICAL`; `CROSS_SECTIONAL`; `BETWEEN_GROUP`; `NOT_APPLICABLE` allocation. (Methods) Status: `ORIGINAL_RESEARCH_ARTICLE`; `COMPLETED`; `RESULTS_REPORTED`. (Abstract, Conclusion)
### Study structure and typed uses

- Four StudyParts preserve the Ciliwung sample, matched control, Jakarta sample, and Indonesian general population. Sample stages are `ANALYZED`; sizes are 204, 204, 305, and 1,041. (Abstract; Methods, “Respondents”)
- The Ciliwung DataUse has `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. Comparator DataUses have `PRIOR_RESEARCH_COLLECTION` and `PARTICIPANT_RESPONSE`. (Methods, “Respondents”)
- InstrumentUse labels are “EQ-5D-5L,” “WHOQOL-BREF,” “Happiness Thermometer,” and “Cantril’s Self-Anchoring Striving Scale,” each with `CURRENT_HEALTH_MEASUREMENT` for the applicable source or current part. (Methods, “Measures”)
- ScoringUse links EQ-5D-5L responses to the “Indonesian value set.” (Methods, “Analysis”)
- MethodUse: “one-way MANOVA,” “multiple linear regression analysis,” “t-tests,” and “Wilcoxon rank-sum test” have `QUANTITATIVE_ANALYSIS`. (Methods, “Analysis”)
- Administration preserves paper self-completion at home with interviewer reading assistance for literacy or eyesight problems. (Methods, “Procedure” and “Measures”)
### Findings, limitations, products, and concepts

- Outcome family is `HEALTH_STATUS_OR_EQ_VAS`. Ciliwung respondents had lower physical QoL and happiness, but higher EQ-VAS health, life satisfaction, and perceived financial status than comparison groups. Differences were small overall. (Abstract; Discussion; Conclusion)
- The authors discuss adaptation, local comparison, social capital, and resilience as possible explanations for the unexpected positive self-ratings. These are interpretations, not Findings. (Discussion)
- Reported limitations are possible effects from imminent relocation and possible recruitment bias from introduction by a non-governmental organization. (Discussion)
- Concepts: river pollution, annual flooding, relocation uncertainty, adaptation, social capital, community resilience, happiness, and life satisfaction. (Background; Discussion)
### Gaps and source conflicts

- SourceConflict SC-D015-01: the Abstract says “Life Satisfaction Index,” while Methods name “Cantril’s Self-Anchoring Striving Scale.” Preserve both source labels and do not merge them without registry review. (Abstract, Methods; Methods, “Measures”)
### High-value canonical terms

- Registry labels: “official EQ-5D-5L Bahasa Indonesia version,” “EQ Visual Analogue Scale (EQ-VAS),” “Indonesian version of WHOQOL-BREF,” “Happiness Thermometer,” “Cantril’s Self-Anchoring Striving Scale,” and “Indonesian value set.” (Methods, “Measures” and “Analysis”) Discovery concepts: unhealthy riverbank, flood exposure, pollution exposure, relocation, physical quality of life, perceived financial situation, social capital, and resilience. (Background; Discussion)

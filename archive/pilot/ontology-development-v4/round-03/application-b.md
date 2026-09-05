# Round 03 ontology v0.2 application B

## Inputs and verification

I read only `AGENTS.md`, `ROUND3_APPLICATION_TASK.md`, `PROTOCOL.md`,
`ONTOLOGY.md`, `EXTRACTION_TASK.md`, `round-03.tsv`, and the 15 article files
listed below. I did not use an earlier application, candidate, review,
decision, graph record, extraction, old ontology version, or Neo4j guidance.

| Record | Article file | Bytes | SHA-256 | Result |
|---|---|---:|---|---|
| C001 | `corpus/2012020/doi_10.1007_s40273-018-0615-8.md` | 48419 | `ce4008f8960d9f27e76693f2f31fd1b2b043c3b86ccef599e799a745c444849f` | match |
| C002 | `corpus/429-RA/doi_10.1007_s11136-026-04223-x.md` | 49434 | `5266d9a9ea95e329ff9e5e1e46f124ffe129051b75fd16ce030459f108d798fe` | match |
| C003 | `corpus/150-RA/doi_10.1007_s40271-024-00715-5.md` | 62053 | `19259d3a21512fdd2c1e447fe6e44febcbd2388f57eabe3431d298282c222d05` | match |
| C004 | `corpus/2015400/doi_10.1007_s11136-018-1985-2.md` | 71162 | `363625c754d379c479f786321eb244e48678aacfa36d92fe001dd38ac3247539` | match |
| C005 | `corpus/341-RA/doi_10.1038_s41433-023-02860-x.md` | 71413 | `6a27dd1b66faeb7e4095b044a2f9b8df67dc165bf02ff8811dbcc59b536643d6` | match |
| C006 | `corpus/1483-TVG/doi_10.1213_ane.0000000000007107.md` | 93921 | `46894a0a2caf783ddeed15e6c822abcc1444a18dc7b1ad824a631c826f233f5a` | match |
| C007 | `corpus/330-PHD/doi_10.1007_s11136-025-03990-3.md` | 77245 | `171009067ec3beb38d0342b099ed4a4172530dea123ad3a96a6a5907bfd95ba1` | match |
| C008 | `corpus/348-PHD/doi_10.1371_journal.pone.0302886.md` | 188611 | `9420b24805f77c45e43b06a4d79dde1108b29b495b94d16550687f99631dcbb5` | match |
| C009 | `corpus/2013230/doi_10.1007_s40273-015-0292-9.md` | 55363 | `183a6da25535bfd5f18299dc5aa2c40eea8e4b804bf42793efda1eb3a62ae76c` | match |
| C010 | `corpus/20180130/doi_10.1007_s40273-021-01002-z.md` | 94816 | `f16bf7a38694b56920da191a401bb044d65a40b646a083e7fd2139a5fca87322` | match |
| C011 | `corpus/20190890/doi_10.1007_s10198-021-01377-y.md` | 63193 | `57250a97f739fa5d4c81b213313ae376cc98f670ef1f80444769917babf91e0d` | match |
| C012 | `corpus/238-RA/doi_10.1007_s10198-024-01719-6.md` | 101030 | `7ca37497aa5ba3a9bab94fe0156583e85bd35a99d4934ff5af8381837dda5394` | match |
| C013 | `corpus/349-RA/doi_10.1007_s12311-024-01657-2.md` | 64795 | `ba3549249f6cd84bf6aea4d81fd2cf43e6024a192e0c9ede4d0451c2ffb36a93` | match |
| C014 | `corpus/2016230/doi_10.1186_s12955-023-02131-z.md` | 50150 | `b2083bc30a6caf142e5ea44beb9a49f3d4bfb500e10f6c8158ee2dfdc88eee01` | match |
| C015 | `corpus/460-RA/doi_10.3390_nu16162591.md` | 82631 | `8b7cca005d2c1fa9631f3981fddf0945e20dfa67678fc845fd73f939bddb73a9` | match |

## C001 — German EQ-5D-5L value set

### Assessment

- Complete application. The source supports a national value-set study and no controlled-key gap.
### Study identity and primary family

- One study; primary family `VALUE_SET_DEVELOPMENT`. The objective and principal output are a German EQ-5D-5L value set (Abstract; Introduction; Preferred Model).
### Purposes, status, and publication form

- Ranked purposes: `VALUE_SET_DEVELOPMENT`, `HEALTH_STATE_VALUATION`, `VALUATION_METHOD_EVALUATION`, `METHOD_OR_PROTOCOL_QUALITY`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE` (Results; Conclusions).
### Study parts, design, and data origin

- cTTO part and DCE part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_METHOD`, `NOT_APPLICABLE` allocation. Both use `CURRENT_STUDY_COLLECTION` at `PARTICIPANT_RESPONSE` level (Methods, Study Design and Valuation Interview).
### Populations and sample stages

- Population: German general population aged over 18 years. Sample: target at least 1000; `COMPLETED` 1158 interviews; cTTO analysis used 10,867 observations after 713 respondent-flagged observations were removed (Methods; Results).
### Instrument uses and administration

- “EQ-5D-5L”: `DIRECT_CURRENT_ACTIVITY` as `CURRENT_HEALTH_MEASUREMENT`, `HEALTH_STATE_DESCRIPTION`, and `VALUATION_TARGET`; “EQ VAS”: `DIRECT_CURRENT_ACTIVITY` as `CURRENT_HEALTH_MEASUREMENT` (Valuation Interview; Table 1); Administration: adult self-report and societal valuation perspective; computer-assisted personal interview; public venue or home; six German areas (Study Design).
### Method, protocol, scoring, and model uses

- Exact methods: “composite time trade-off (cTTO)” and “discrete choice experiment (DCE)” as `PREFERENCE_ELICITATION`; quota-based sampling as `SAMPLING`; EQ-VT QC software process as `QUALITY_CONTROL` (Methods); `TaskDesign`: ten cTTO target states per block with 10-year impaired-health profiles, and seven forced-choice DCE pairs per block, with respondent-level block randomization (Valuation Interview); “EQ-VT 2.0” has `GOVERNING_STUDY_PROTOCOL`, `VALUATION_PROTOCOL`, and `QUALITY_CONTROL_PROTOCOL` uses in `DIRECT_CURRENT_ACTIVITY`; Model 1 censored Tobit and Model 2 conditional logit are `COMPARATOR`; hybrid Model 3a is `COMPARATOR`; heteroskedastic hybrid Model 3b is `PRIMARY_REPORTED`. Functions are `STATISTICAL_ESTIMATION` or `CHOICE_MODELING` as applicable (Data Analysis; Preferred Model).
### Outcomes and principal findings

- Preference/utility: predicted values range from −0.661 to 1; pain/discomfort was most important, then anxiety/depression, self-care, mobility, and usual activities (Preferred Model; Comparison); Model result: Model 3b was selected for logical consistency, heteroskedasticity handling, precision, and fit. Of cTTO values, 17.3% were negative; the feedback module reduced inconsistency (Data Characteristics; Modeling).
### Interpretations and limitations

- Interpretation: the hybrid value set is recommended as the preferred German set and can support clinical studies and cost-utility analysis (Discussion; Conclusions); Source-reported limitations: the sample clustered in six regions and had a small middle-class bias; practical discrimination in patient groups needs more research (Discussion).
### Products and concepts

- Product `VALUE_SET`: “German EQ-5D-5L value set.” Development assertion: “resulting”/“provided”; assertion date `NOT_REPORTED`. Recommendation as “preferred” is preserved and is not converted to approval, validation, or deployment (Key Points; Conclusions); Concepts: states worse than dead, hybrid valuation, respondent feedback, valuation quality control.
### Gaps and source conflicts

- No mapping gap or source conflict identified. Task-block randomization does not change study allocation from `NOT_APPLICABLE` (Valuation Interview).
### High-value canonical terms

- EQ-5D-5L; EQ VAS; EQ-VT 2.0; composite time trade-off (cTTO); discrete choice experiment (DCE); censored Tobit model; conditional logit model; heteroskedastic hybrid Model 3b.

## C002 — QID-12 short-form development

### Assessment

- Complete application. The paper develops new instrument content and evaluates its measurement performance.
### Study identity and primary family

- One study; primary family `INSTRUMENT_VERSION_DEVELOPMENT` because the principal output is QID-12, a 12-item short form (Abstract; Conclusions).
### Purposes, status, and publication form

- Ranked purposes: `INSTRUMENT_DEVELOPMENT`, `MEASUREMENT_PROPERTY_EVALUATION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- Scale-reduction and psychometric-evaluation parts: `QUANTITATIVE_EMPIRICAL`, `VARIABLE_SOURCE_TIME`, `BETWEEN_INSTRUMENT`, `NOT_APPLICABLE` allocation. Data are `PRIOR_RESEARCH_COLLECTION`, `PARTICIPANT_RESPONSE` (Sources of data; Statistical methods).
### Populations and sample stages

- Population: children aged 3–18 years with mild-to-profound intellectual disability. `ANALYZED`: 1,699 unique complete proxy measures from several datasets; source groups include Simons Searchlight 953, The Kids 603, and Inchstone 143 (Sources of data; Results).
### Instrument uses and administration

- “QI-Disability”: `INPUT_DATA_PROVENANCE` as `DEVELOPMENT_OBJECT` and comparator; “QID-12”: `CURRENT_STUDY_OBJECT` as `DEVELOPMENT_OBJECT` and `COMPARATOR` (Variables; Results); Parent/caregiver proxy reports used a five-point response scale. Source modes and settings vary by dataset and are not fully reported (Variables; Sources of data).
### Method, protocol, scoring, and model uses

- “Genetic Algorithm (GA)” with R package “GAabbreviate” is `MAPPING_OR_DERIVATION`; Pearson correlation, Cronbach’s Alpha, item-fit statistics, person separation reliability, and Martin-Loef test are `MEASUREMENT_PROPERTY_ANALYSIS` (Statistical methods); “partial credit model” Rasch analysis is `MEASUREMENT_PROPERTY_ANALYSIS`, `PRIMARY_REPORTED` (Statistical methods; Results).
### Outcomes and principal findings

- Measurement properties: QID-12 retained all six domains; correlation with QI-Disability was 0.970; item fit was satisfactory; person separation reliability was 0.84; targeting covered the ability range but was better at the lower-QOL end (Results); Three items had disordered thresholds between “Never,” “Rarely,” and “Sometimes” categories (Results).
### Interpretations and limitations

- Interpretation: QID-12 can reduce burden for surveys, registries, and clinical monitoring, but it is not a replacement when domain-level detail is needed (Discussion); Limitations: same-sample development can inflate correlation; common descriptors were limited; three thresholds were disordered; independent and diverse-cohort validation is needed (Discussion).
### Products and concepts

- Product `INSTRUMENT_VERSION`: “QID-12.” Development and validation assertions use the exact source terms “developed” and “validated”; assertion dates are `NOT_REPORTED` (Abstract; Discussion); `StudyFactor`: diagnosis/source cohort is `STRATIFIER` for separately reported score patterns (Table 1; Discussion); Concepts: child quality of life, intellectual disability, proxy report, respondent burden, short-form measurement.
### Gaps and source conflicts

- `SourceConflict`: Cronbach’s alpha is 0.85 in the Abstract and Discussion but 0.84 in Results. Do not select one value without source checking; `SourceConflict`: the Martin-Loef result is *p* > 0.99 in the Abstract but *p* = 0.12 in Results. Both statements claim the same unidimensionality test.
### High-value canonical terms

- Quality of Life Inventory – Disability (QI-Disability); QID-12; Genetic Algorithm (GA); GAabbreviate; Rasch analysis; partial credit model; Martin-Loef test.

## C003 — EQ-HWB proxy appropriateness in aged care

### Assessment

- Complete qualitative content and proxy-use evaluation.
### Study identity and primary family

- One study; primary family `MEASUREMENT_PROPERTY_EVALUATION`. The main contribution is qualitative appropriateness and content/face-validity evidence (Abstract; Discussion).
### Purposes, status, and publication form

- Ranked purposes: `CONTENT_VALIDITY_EVALUATION`, `MEASUREMENT_PROPERTY_EVALUATION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- One qualitative part: `QUALITATIVE_INQUIRY`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NOT_APPLICABLE` allocation; `CURRENT_STUDY_COLLECTION`, `QUALITATIVE_MATERIAL` (Methods).
### Populations and sample stages

- Population: family and staff proxies for residents of three not-for-profit aged-care facilities in Melbourne. `ANALYZED`: 29 proxies, including nine family members and 20 staff (Sample and Recruitment; Results).
### Instrument uses and administration

- “25-item EQ-HWB English version for Australia, proxy version 2”: `CURRENT_STUDY_OBJECT` as `CONTENT_TEST_OBJECT` (Procedure); Respondent is a family or staff proxy; perspective is proxy-person; completion was in person except one Zoom interview; instrument recall is last 7 days; interview language was English (Procedure; Recall Period).
### Method, protocol, scoring, and model uses

- Convenience sampling is `SAMPLING`; “cognitive think-aloud interviews” and “semi-structured questions” are `QUALITATIVE_DATA_COLLECTION`; combined deductive and inductive “thematic analysis” is `QUALITATIVE_ANALYSIS` (Methods); No `PARTICIPATORY_DESIGN` use: participants commented on content but did not jointly create or select a product in this study.
### Outcomes and principal findings

- Content validity and feasibility: two themes covered accurate proxy report and instrument appropriateness. Problems included perspective adherence, limited knowledge, disagreement, heuristics, ambiguity, double-barrelled items, examples, repetition, response options, recall, and layout (Results, Themes 1–2); Proxies generally endorsed domain coverage, but psycho-social items were harder to assess; central response choices could hide uncertainty (Discussion).
### Interpretations and limitations

- Interpretation: revise wording and examples; self-report remains preferred, but proxy report can be necessary in severe impairment (Conclusions); Limitations: convenience sample, no resident self-report comparison, problem-focused questioning could bias views, and no head-to-head measure comparison (Discussion).
### Products and concepts

- Concepts: proxy-person perspective, proxy reporting, residential aged care, content validity, recall period, central-tendency bias.
### Gaps and source conflicts

- Rule check: mapping these interviews to `PARTICIPATORY_DESIGN` would weaken the joint-creation rule. Preserve them as qualitative evidence only. No source conflict identified.
### High-value canonical terms

- EQ Health and Wellbeing (EQ-HWB); EQ-HWB proxy version 2; cognitive think-aloud interviews; semi-structured interviews; thematic analysis; NVivo.

## C004 — Swedish adolescent EQ-5D-Y-3L population data

### Assessment

- Complete population-reference application with condition and socioeconomic strata.
### Study identity and primary family

- One study; primary family `POPULATION_REFERENCE_DESCRIPTION` because the aim is adolescent population health and reference data (Abstract; Introduction).
### Purposes, status, and publication form

- Ranked purposes: `POPULATION_NORMS`, `OUTCOME_DESCRIPTION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- One part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NOT_APPLICABLE` allocation; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (Study design; Data analyses).
### Populations and sample stages

- Population: students aged 13–18 years in Orebro County, Sweden, in 2014. `COMPLETED`: 7,399 survey respondents; `ANALYZED`: 6,574 complete EQ-5D-Y-3L profiles; 231 profiles were excluded for dimension missingness (Response rate).
### Instrument uses and administration

- “Swedish version of the EQ-5D-Y-3L” and its VAS: `DIRECT_CURRENT_ACTIVITY` as `CURRENT_HEALTH_MEASUREMENT` and `OUTCOME_MEASURE` (Measures); Adolescent self-report; self-administered paper-and-pencil; classroom during school hours; EQ-5D-Y-3L time point “today” (Study design; EQ-5D-Y-3L).
### Method, protocol, scoring, and model uses

- Total school survey is `SAMPLING` and `QUANTITATIVE_DATA_COLLECTION`; chi-square, Fisher exact, Mann-Whitney U, multiple logistic regression, and multiple linear regression are `QUANTITATIVE_ANALYSIS` (Data analyses).
### Outcomes and principal findings

- Health status and EQ VAS: 44.9% reported 11111. Girls had more usual-activity, pain/discomfort, and mood problems and lower VAS scores; unemployment of one or both parents and comorbidity were associated with poorer health (Results); The largest adjusted sex association was for mood problems, OR 3.44 for girls versus boys. Always feeling depressed had the largest VAS impact (Regression analyses; Abstract).
### Interpretations and limitations

- Interpretation: the instrument distinguished important population groups and can guide prioritization (Conclusions); Source-reported limitation: adolescent-reported parental occupation might be an imperfect socioeconomic proxy. School-based collection can also exclude adolescents who cannot attend (Discussion).
### Products and concepts

- Product `POPULATION_REFERENCE_DATA`: Swedish adolescent EQ-5D-Y-3L results by sex, age, parental occupation, and comorbidity. The source gives 2014 as the data-collection year; no product-state date, approval, validation, or deployment is inferred; `StudyFactor`: sex, age, parent occupation, disease, impairment, distress, and BMI are `STRATIFIER`, and regression-tested terms are also `EXPOSURE_OR_DETERMINANT` in their analytic uses (Data analyses; Results); Concepts: adolescent health, population norms, mental distress, socioeconomic inequality, comorbidity.
### Gaps and source conflicts

- No controlled-key gap or source conflict identified.
### High-value canonical terms

- EQ-5D-Y-3L; visual analogue scale (VAS); Life & Health—young people; multiple logistic regression; multiple linear regression.

## C005 — Societal cost of vision impairment

### Assessment

- Complete application with a primary-family gap. This is a cost-of-illness study, not an intervention decision analysis.
### Study identity and primary family

- Primary family `UNMAPPED_VALUE`. `HEALTH_ECONOMIC_EVALUATION` requires costs and health consequences used for a decision; this study estimates prevalent burden without comparing decision options (Abstract; Methods; Discussion).
### Purposes, status, and publication form

- `OUTCOME_DESCRIPTION` applies to cost and well-being burden. Main economic-burden purpose is `UNMAPPED_VALUE` (Gap G1); Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- Survey part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (Methods); Cost-estimation part: `MODEL_BASED`, `NOT_APPLICABLE` time, `NONCOMPARATIVE`, `NOT_APPLICABLE`; separate uses of survey data, contemporaneous eye-system data, and `PUBLISHED_MODEL_INPUT` at `MODEL_PARAMETER` level (Classification; Intangible effects).
### Populations and sample stages

- Population: Trinidad and Tobago adults aged at least 40 years in 2014. Eligible survey sample 4,263; visual-acuity responders 3,589; medical/ophthalmic questionnaire 2,792; socioeconomic questionnaire 2,516 (Methods; Results).
### Instrument uses and administration

- No EQ instrument was used. Socioeconomic and medical/ophthalmic questionnaires were interviewer-administered with Epi Info during clinic assessment (Methods).
### Method, protocol, scoring, and model uses

- Multi-stage probability-proportional cluster sampling is `SAMPLING`; standardized visual-acuity assessment and questionnaires are `QUANTITATIVE_DATA_COLLECTION`; survey weighting and mixed-effects logistic regression are `QUANTITATIVE_ANALYSIS` (Methods); Bottom-up cost-of-illness estimation is `ECONOMIC_EVALUATION`; one-way sensitivity analysis is `QUANTITATIVE_ANALYSIS`. “Cost of Vision Loss Consensus Guidelines (2010)” has `GOVERNING_STUDY_PROTOCOL` use (Introduction; Methods).
### Outcomes and principal findings

- Cost and well-being loss: total societal cost was TT$3.842 billion, or UK£365.650 million; well-being loss was 73.3%. Without it, cost was TT$1.025 billion; indirect costs were 70.5% (Table 2); Estimated distance-VI cases were 64,431, of which 86.1% were potentially avoidable; disability-weight choices caused a fourfold range in monetized well-being loss (Estimation of cases; Sensitivity analyses).
### Interpretations and limitations

- Interpretation: individuals and families bore most cost; direct health-sector costs alone would understate the resource case for vision care (Discussion; Conclusion); Limitations: age 40+ only; institutionalized people and long-term care omitted; 59–66% response; blind people underrepresented; recall bias; several cost types omitted; DALY monetization has conceptual and ethical limits (Discussion).
### Products and concepts

- `StudyFactor`: presenting vision level is `STUDIED_CONDITION` and `STRATIFIER` for level-specific costs and access; normal vision is the reported `COMPARATOR` where used (Differential impacts); Concepts: vision impairment, cost of illness, societal perspective, informal care, productivity loss, DALY, avoidable vision loss.
### Gaps and source conflicts

- Gap G1: family and main purpose are `UNMAPPED_VALUE`; evidence and proposal are in the aggregate gap log. No source conflict identified.
### High-value canonical terms

- National Eye Survey of Trinidad and Tobago (NESTT); cost-of-illness study; societal perspective; years lived with disability (YLD); disability-adjusted life year (DALY); one-way deterministic sensitivity analysis.

## C006 — Peripheral nerve block use in arthroplasty

### Assessment

- Complete applied-use study with separate hip and knee parts. No EQ instrument is present.
### Study identity and primary family

- One study; primary family `APPLIED_USE_RESEARCH`. The main decision concerns variation and standardization of PNB use in routine care; clinical outcomes are secondary (Abstract; Main Findings).
### Purposes, status, and publication form

- Ranked purposes: `IMPLEMENTATION_EVALUATION`, `OUTCOME_DESCRIPTION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- THA and TKA parts: `QUANTITATIVE_EMPIRICAL`, `LONGITUDINAL_REPEATED`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `ROUTINE_SERVICE_COLLECTION`, `PARTICIPANT_RESPONSE` (Data; Outcomes; Statistical Analysis).
### Populations and sample stages

- Population: Medicare-insured primary THA/TKA patients aged at least 66 years, 2012–2021. Initial cohort 241,326; complete-case final count is internally conflicting (Inclusion; Results; Gap section).
### Instrument uses and administration

- No EQ instrument or participant questionnaire was used. Claims codes and linked hospital and neighborhood records supplied the measures (Data; Variables).
### Method, protocol, scoring, and model uses

- Claims extraction is `QUANTITATIVE_DATA_COLLECTION`; mixed-effects logistic regression and adjusted population-attributable risk are `QUANTITATIVE_ANALYSIS` (Statistical Analysis); Mixed-effects logistic models are `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; sensitivity variants are `SENSITIVITY`. STROBE has `REPORTING_GUIDELINE` use (Data).
### Outcomes and principal findings

- Implementation: clinical factors explained 46% of THA and 34% of TKA PNB variation; hospital factors explained 31% and 22%; demographic and socioeconomic factors had small contributions (Population Attributable Risks); Outcomes: in TKA, PNB use was associated with fewer CMS complications, OR 0.82, and less stay over 3 days, OR 0.90; readmission was null. All THA outcome associations were null (Secondary Outcomes).
### Interpretations and limitations

- Interpretation: practice variation, more than socioeconomic status, drove PNB use; more standard provision is warranted (Conclusions); Limitations: observational associations are not causal; residual confounding; Medicare-only generalizability; area deprivation can differ from individual status; PAR is a theoretical maximum (Strengths and Limitations).
### Products and concepts

- `StudyFactor`: PNB receipt is `STUDIED_CONDITION` with nonreceipt as `COMPARATOR`; clinical, hospital, demographic, and socioeconomic variables are `EXPOSURE_OR_DETERMINANT`; THA/TKA is `STRATIFIER` (Statistical Analysis; Results); Concepts: routine PNB use, practice variation, socioeconomic disparity, arthroplasty, care standardization.
### Gaps and source conflicts

- `SourceConflict`: Abstract reports 52,926 THA and 94,795 TKA cases, total 147,721; Results reports 52,000 THA and 93,448 TKA cases, total 145,448. The Inclusion section also calls 147,721 the final sample.
### High-value canonical terms

- peripheral nerve blocks (PNBs); Medicare Limited Dataset; Social Deprivation Index; population-attributable risk (PAR); mixed-effects logistic regression; CMS-defined complication.

## C007 — P-PROM ROCK phase 1

### Assessment

- Complete qualitative pre-implementation study. Stakeholder influence is explicit, but joint product creation is not.
### Study identity and primary family

- One study; primary family `APPLIED_USE_RESEARCH` because it examines routine PROM implementation and future workflow design (Abstract; Conclusions).
### Purposes, status, and publication form

- Ranked purposes: `IMPLEMENTATION_EVALUATION`, `CONTENT_VALIDITY_EVALUATION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- One qualitative part: `QUALITATIVE_INQUIRY`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION`, `QUALITATIVE_MATERIAL` (Methods).
### Populations and sample stages

- Population: Royal Children’s Hospital adolescent outpatients, caregivers, and outpatient service providers. Seventeen eligible people registered; 14 were selected and interviewed: six providers, five caregivers, three adolescents (Participants; Results).
### Instrument uses and administration

- “EQ-5D-Y-5L”: separate `CURRENT_STUDY_OBJECT` uses as `IMPLEMENTATION_OBJECT` and `CONTENT_TEST_OBJECT`; it was shown and discussed, not used to measure participant health (Data collection); Interviews were individual, online video sessions of about 30 minutes. Respondents were adolescent patients, caregivers, or providers (Data collection).
### Method, protocol, scoring, and model uses

- Purposive and snowball recruitment is `SAMPLING`; semi-structured interviews are `QUALITATIVE_DATA_COLLECTION`; framework analysis and post-coding mapping to the Theoretical Framework of Acceptability are `QUALITATIVE_ANALYSIS` (Methods); COREQ has `REPORTING_GUIDELINE` use. No `PARTICIPATORY_DESIGN` use is assigned because Phase 1 gathered views; the joint design work is Phase 2 (Study design; Conclusions).
### Outcomes and principal findings

- Implementation and acceptability: participants supported use only if clinicians respond to results; family support, clinician education, resources, and IT integration are needed (Key themes; Discussion); Most preferred item-level and longitudinal displays, not one score. Concerns included short recall, negative framing, missing context, and broad items (Scoring and displaying results; Instrument characteristics).
### Interpretations and limitations

- Interpretation: advance to co-design and then test prototypes for feasibility, acceptability, and effect (Conclusions); Limitations: one parent dominated an adolescent interview; no younger-child, father, or non-English voice; three adolescents; clinic selection limits transfer; only EQ-5D-Y-5L was offered (Discussion).
### Products and concepts

- `StakeholderInvolvement`: adolescents, caregivers, and providers gave views at the pre-design stage; influence statement: findings informed Phase 2 co-design and its focus areas (Abstract; RQ3; Conclusions); Concepts: routine paediatric PROM implementation, acceptability, clinical workflow, item display, co-design.
### Gaps and source conflicts

- Rule risk: classifying stakeholder consultation as `PARTICIPATORY_DESIGN` would erase the stated boundary between Phase 1 interviews and planned Phase 2 joint design. No source conflict identified.
### High-value canonical terms

- EQ-5D-Y-5L; P-PROM ROCK; semi-structured interviews; framework analysis; Theoretical Framework of Acceptability (TFA); COREQ.

## C008 — Mixed-method Person Trade Off protocol

### Assessment

- Complete protocol application with planned uses, reusable task design, completed pilot work, and documented consumer influence.
### Study identity and primary family

- One study; primary family `METHODS_RESEARCH`. The paper gives a detailed PTO protocol and tests forced choice against an equivalence option (Abstract; Box 1; Discussion).
### Purposes, status, and publication form

- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `PREFERENCE_COMPARISON`, `METHOD_OR_PROTOCOL_QUALITY`, `DECISION_SUPPORT_DEVELOPMENT`; Main execution `PLANNED`; results `NO_RESULTS_YET`; form `PROTOCOL_ARTICLE`. Completed pilots do not change the main state (Data Availability; Pilot testing).
### Study parts, design, and data origin

- Online PTO survey: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `RANDOMIZED`; planned `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE`; Think-aloud interviews and focus groups: `QUALITATIVE_INQUIRY`, `CROSS_SECTIONAL`, `BETWEEN_CONTEXT`, `NOT_APPLICABLE`; planned `CURRENT_STUDY_COLLECTION`, `QUALITATIVE_MATERIAL`. Integration is `SEQUENTIAL` (Sections 2.3–2.7); Consumer and pilot development part: `QUALITATIVE_INQUIRY`, completed current collection (Section 2.9).
### Populations and sample stages

- Population: Australian public aged at least 16 years, with parent and non-parent subgroups. Planned survey `ENROLLED` target 2,000; interviews about 40; about four focus groups of at most five (Sample size); Completed pilots: three CAG survey pilots plus at least 14 convenience survey pilots; two convenience qualitative interview pilots, with six recruited pilots planned (Pilot testing).
### Instrument uses and administration

- No EQ instrument is directly administered. Planned respondents use a social decision-maker perspective; the PTO survey is self-completed online. Qualitative interviews and focus groups are facilitated and recorded (Perspective; Mode; Qualitative component).
### Method, protocol, scoring, and model uses

- “Person Trade Off (PTO) choice-experiment” is planned `PREFERENCE_ELICITATION`; `TaskDesign`: programs A/B, 100-patient start, iterative equivalence, 13 youth ages versus age 40/55, 2- or 5-year life extension or 2-year quality gain, and randomized forced/equivalence option, age screen-side, and question order (Section 2.3); patient age, health-gain type/domain, and forced/equivalence option are `STUDIED_CONDITION` factors; online survey is `QUANTITATIVE_DATA_COLLECTION`; think-aloud, semi-structured interviews, and focus groups are `QUALITATIVE_DATA_COLLECTION`; thematic framework analysis is `QUALITATIVE_ANALYSIS`; CAG refinement is `PARTICIPATORY_DESIGN`, `DIRECT_CURRENT_ACTIVITY`. Bootstrap intervals and planned regressions are `QUANTITATIVE_ANALYSIS` (Sections 2.7 and 2.9).
### Outcomes and principal findings

- Planned outcomes: relative child-versus-adult health-gain weights, preference heterogeneity, task consistency, forced-versus-unforced differences, and qualitative reasons (Box 1); Pilot process finding: CAG input simplified participant material and task wording and moved sensitive personal-priority discussion out of focus groups (Section 2.9.1).
### Interpretations and limitations

- Interpretation: results can inform Australian age weighting and PTO best practice (Abstract; Conclusion); Planned limitations: unattended online engagement, incomplete social-group coverage, PTO design biases, Australia-only generalizability (Section 3.3).
### Products and concepts

- Product `PROTOCOL`: mixed-method PTO and qualitative protocol. Exact state “resultant protocol”/“protocol outlined”; the University of Melbourne ethics committee “granted ethical approval.” No dates are inferred (Title; Section 2.11.2); `StakeholderInvolvement`: QUOKKA Consumer Advisory Group refined plain-language material, PTO tasks, and safe focus-group scope (Section 2.9.1).
### Gaps and source conflicts

- No controlled-key gap or source conflict identified. Do not assign `HEALTH_STATE_VALUATION`: the principal preference collection is planned and the article reports no substantive valuation results.
### High-value canonical terms

- Person Trade Off (PTO) choice-experiment; think aloud; semi-structured interview; focus group; framework analysis; Online Research Unit (ORU); QUOKKA Consumer Advisory Group.

## C009 — CREATE reporting checklist

### Assessment

- Complete methods and checklist-development application.
### Study identity and primary family

- One study; primary family `METHODS_RESEARCH` because its contribution is reporting-quality guidance for valuation studies (Abstract; Conclusion).
### Purposes, status, and publication form

- Ranked purpose: `METHOD_OR_PROTOCOL_QUALITY`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- Expert-panel and member-survey parts: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `NONCOMPARATIVE`, `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (CREATE Development); The initial 35 items use `PRIOR_RESEARCH_COLLECTION` from a reported systematic review (CREATE Development).
### Populations and sample stages

- Expert panel: five named utility-measurement experts. EuroQol email survey: `COMPLETED` 16 respondents from eight countries; the source does not support one combined unique-person count (Expert Panel; Results).
### Instrument uses and administration

- MAUIs, including EQ-5D, SF-6D, HUI, and AQoL, are `DISCUSSION_ONLY` with `REFERENCE_ONLY` function. No instrument response is collected in this study (Introduction; Discussion).
### Method, protocol, scoring, and model uses

- “modified Delphi panel approach” and “email survey” are `QUANTITATIVE_DATA_COLLECTION`; `TaskDesign`: 26 candidate items rated “required,” “recommended,” or “optional,” with a greater-than-50% “required” threshold before final deliberation (CREATE Development); item rating and majority rule are `QUANTITATIVE_ANALYSIS`; expert and intended-user refinement is `PARTICIPATORY_DESIGN` (Methods); “international reporting guideline development framework” has `GOVERNING_STUDY_PROTOCOL` use.
### Outcomes and principal findings

- Method-quality outcome: 22 items exceeded the survey threshold; final CREATE has 21 items in seven sections after deliberation removed one item (Results); The sections are descriptive system, health states valued, sampling, preference data collection, study sample, modeling, and scoring algorithm (Results, Table 1).
### Interpretations and limitations

- Interpretation: CREATE supports transparent reporting, critical appraisal, reproducibility, and valuation-study design (Discussion; Conclusion); Limitations: small survey, all participants were EuroQol members, categorical ratings and a majority threshold were used, and methods can require later updates (Discussion).
### Products and concepts

- Product `CHECKLIST_OR_TOOL`: “21-item Checklist for REporting VAluaTion StudiEs (CREATE).” Development assertion is undated; approval, validation, and deployment are not reported; `StakeholderInvolvement`: five experts and 16 member respondents reviewed content, completeness, wording, importance, and item changes (Methods).
### Gaps and source conflicts

- No controlled-key gap or source conflict identified.
### High-value canonical terms

- Checklist for REporting VAluaTion StudiEs (CREATE); multi-attribute utility-based instruments (MAUIs); modified Delphi panel approach; email survey; international reporting guideline development framework.

## C010 — Retracted Egyptian EQ-5D-5L valuation article

### Assessment

- The reported study is extractable, but publication retraction is not modeled in ontology v0.2. Product usability must not be inferred from the original body text.
### Study identity and primary family

- One reported study; primary family `VALUE_SET_DEVELOPMENT` based on the stated objective and output (Abstract; Preferred Model). Retraction is a publication fact, not a different research family.
### Purposes, status, and publication form

- Ranked purposes: `VALUE_SET_DEVELOPMENT`, `HEALTH_STATE_VALUATION`, `VALUATION_METHOD_EVALUATION`, `METHOD_OR_PROTOCOL_QUALITY`; Reported execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. Title publication status is unmodeled (Gap G2).
### Study parts, design, and data origin

- Pilot, cTTO, and DCE parts: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_METHOD`, `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (Methods).
### Populations and sample stages

- Population: adult Egyptian public selected by age, sex, and geography quotas. `COMPLETED` 1,378 interviews; `EXCLUDED` 113 poor-protocol interviewer cases and 75 incomplete cases; pilot 216; `ANALYZED` 974 (Data Cleaning).
### Instrument uses and administration

- “EQ-5D-5L” and “visual analogue scale (VAS)”: `DIRECT_CURRENT_ACTIVITY` as current-health measures; EQ-5D-5L states also have `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET` uses (Interview Process); Interviewer-administered Egyptian Arabic EQ-VT; visual aids and read-aloud assistance supported illiterate respondents (Pilot Phase; Interview Process).
### Method, protocol, scoring, and model uses

- “composite time trade-off (cTTO)” and “discrete-choice experiments (DCEs)” are `PREFERENCE_ELICITATION`; `TaskDesign`: five cTTO practice tasks, ten hypothetical-state cTTO tasks with feedback, and seven randomly ordered forced-pair DCE tasks; health-state cards and read-aloud support were assistance, not a proxy response (Interview Process); quota sampling is `SAMPLING`; QC tool is `QUALITY_CONTROL`; “EQ-VT software (2.1)” has direct `GOVERNING_STUDY_PROTOCOL`, `VALUATION_PROTOCOL`, and `QUALITY_CONTROL_PROTOCOL` uses; GLS, Tobit, heteroskedastic, conditional-logit, and hybrid models are `STATISTICAL_ESTIMATION` or `CHOICE_MODELING`; heteroskedastic Model 4 is `PRIMARY_REPORTED`, others `CANDIDATE` or `COMPARATOR` (Data Analysis; Preferred Model).
### Outcomes and principal findings

- Reported utility range: −0.933 for 55555 to 1 for full health; 1,136 predicted states, 36.3%, were worse than dead; mobility had the largest decrement (Preferred Model); Model 4 was selected for consistency, error variability, MAE, and fit. Forty-one percent of observed cTTO responses were worse than dead (Results; Discussion).
### Interpretations and limitations

- Original-body interpretation: the tariff could support Egyptian economic evaluation and HTA. This statement is preserved as historical source text, not as current guidance (Discussion; Conclusion; title); Limitations: rural, illiterate, and older people were underrepresented; visual aids were not fully validated; COVID-19 stopped quota completion; marital and insurance distributions differed (Discussion).
### Products and concepts

- Product `VALUE_SET`: “Egyptian tariff”/“first value set for EQ-5D-5L” with exact development term “generated.” No approval, validation, deployment, or current usability is inferred (Discussion; Conclusion); Concepts: Egyptian social preferences, cultural adaptation, illiterate respondent assistance, states worse than dead, retracted publication.
### Gaps and source conflicts

- Gap G2 `UNMODELED_ASPECT`: retracted publication status and its dated provenance have no key. The file title gives “RETRACTED ARTICLE,” but the file gives no retraction notice, date, or reason (`NOT_REPORTED`); This is a chronological publication-status tension, not a `SourceConflict`: a later retraction can coexist with the original article’s claims. Treating retraction as product validation failure would violate the product-state rule.
### High-value canonical terms

- EQ-5D-5L; EQ-VT 2.1; composite time trade-off (cTTO); discrete-choice experiment (DCE); generalized least square (GLS); heteroskedastic Model 4; Egyptian tariff.

## C011 — Valuation-perspective experiment

### Assessment

- Complete valuation-method experiment with direct task and factor records.
### Study identity and primary family

- One study; primary family `METHODS_RESEARCH` because the main contribution is the effect of valuation perspective on method outcomes, precision, and quality (Objectives; Discussion).
### Purposes, status, and publication form

- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `HEALTH_STATE_VALUATION`, `PREFERENCE_COMPARISON`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- VAS and TTO parts: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `WITHIN_PERSON`, `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (Experimental procedure).
### Populations and sample stages

- Population: bachelor students; `ANALYZED` 205, mean age 19.48 years, 106 female (Methods).
### Instrument uses and administration

- “EQ-5D-Y-3L”: `DIRECT_CURRENT_ACTIVITY` as familiarization `CURRENT_HEALTH_MEASUREMENT`, then `HEALTH_STATE_DESCRIPTION` and `VALUATION_TARGET` (Experimental procedure; Health states); Respondents self-completed in individual cubicles after video instruction; a researcher was present. Perspectives were self-adult, other-adult, self-child, and other-child (Methods).
### Method, protocol, scoring, and model uses

- “visual analogue scale (VAS)” and “composite TTO procedure” are `PREFERENCE_ELICITATION`; `TaskDesign`: five assigned states, VAS 0–100, 10-year cTTO with five bisection choices and worse-than-dead branch, crossed with four randomly ordered perspectives (Health states; Valuation methods); task randomization and researcher support are `QUALITY_CONTROL`; regressions and Bayesian variance analysis are `QUANTITATIVE_ANALYSIS`; EQ-5D-Y-3L valuation protocol has `VALUATION_PROTOCOL` use. Reported regressions are `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED` (Methods; Results).
### Outcomes and principal findings

- Preference/method performance: TTO valuations for others were higher overall and less variable; perspective effects were small and heterogeneous by state and respondent. VAS child/adult effects occurred in both directions (Results; Discussion); Quality: child perspectives had more dominance violations; deciding for self had more TTO non-trading (Valuation quality).
### Interpretations and limitations

- Interpretation: even small perspective effects can affect QALY gains; the empirical and normative implications remain uncertain (Discussion); Limitations: self-completion instead of one-to-one interview, student sample, bisection method difference, possible block-randomization error, order/anchoring effects (Discussion).
### Products and concepts

- `StudyFactor`: “valuation perspective,” role `STUDIED_CONDITION`, levels self-adult, other-adult, self-child, other-child. “Health-state severity” is `EFFECT_MODIFIER` where interactions are reported. VAS versus TTO is represented by method uses and `BETWEEN_METHOD`, not a combined factor (Methods; Results); Concepts: valuation perspective, child health, self-other decision, states worse than dead, dominance violation.
### Gaps and source conflicts

- `SourceConflict`: Abstract says VAS variance was higher with child perspectives; Results says VAS variance was larger for adult perspectives. Preserve both until source checking resolves direction.
### High-value canonical terms

- EQ-5D-Y-3L; self-adult (SA); other-adult (OA); self-child (SC); other-child (OC); visual analogue scale (VAS); composite TTO procedure; bisection elicitation.

## C012 — EQ-5D-5L coeliac-disease bolt-ons

### Assessment

- Complete instrument-content development and psychometric evaluation with supported patient participation.
### Study identity and primary family

- One study; primary family `INSTRUMENT_VERSION_DEVELOPMENT`. It creates two bolt-on items and evaluates five bolt-ons; final wording remains future work (Objectives; Development; Discussion).
### Purposes, status, and publication form

- Ranked purposes: `INSTRUMENT_DEVELOPMENT`, `MEASUREMENT_PROPERTY_EVALUATION`, `CONTENT_VALIDITY_EVALUATION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- Development part: `QUALITATIVE_INQUIRY`, `VARIABLE_SOURCE_TIME`, `BETWEEN_INSTRUMENT`, `NOT_APPLICABLE`; literature, prior expert interviews, and current panel input have separate documentary/qualitative data uses (Development); Survey part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_INSTRUMENT`, `NOT_APPLICABLE`; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (Survey; Analyses).
### Populations and sample stages

- Population: Hungarian adults with confirmed coeliac disease. `ANALYZED`: 312 convenience-sampled patients in an online survey, December 2020 to January 2021 (Cross-sectional survey).
### Instrument uses and administration

- “EQ-5D-5L,” dining, gastrointestinal problems, cognition, sleep, and tiredness bolt-ons: `DIRECT_CURRENT_ACTIVITY` as `CURRENT_HEALTH_MEASUREMENT`, `DEVELOPMENT_OBJECT`, and `COMPARATOR` in separate uses (Outcome measures); “Gastrointestinal Symptom Rating Scale (GSRS)” and “Satisfaction with Life Scale (SWLS)” are direct comparator/outcome measures. Adult self-report, Qualtrics web channel, Hungarian context (Survey; Outcome measures).
### Method, protocol, scoring, and model uses

- Literature and expert/patient input are `PARTICIPATORY_DESIGN` for the two new items; online survey is `QUANTITATIVE_DATA_COLLECTION`; ceiling, Shannon indices, correlations, known groups, regressions, PCA, and CFA are `MEASUREMENT_PROPERTY_ANALYSIS` (Methods); PCA and CFA are `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; adjusted and unadjusted regressions are reported comparators (Analyses).
### Outcomes and principal findings

- Measurement properties: each bolt-on reduced the 39% EQ-5D-5L ceiling; tiredness reduced it to 17%, sleep 23%, GI 24%, dining 26%, cognition 37% (Abstract); GI correlated 0.71 with GSRS, improved all known-group tests, and alone loaded on a factor separate from core dimensions; cognition added little (Results; Discussion).
### Interpretations and limitations

- Interpretation: dining, GI, sleep, and tiredness can improve measurement, especially GI; utility effects still need study (Conclusion; Discussion); Limitations: self-reported unverified disease, unrepresentative all-GFD volunteer sample, cross-sectional design, pandemic timing, no final item wording, and no utility assessment (Discussion).
### Products and concepts

- Product `INSTRUMENT_VERSION`: candidate EQ-5D-5L bolt-on content, including newly developed “dining (DI)” and “gastrointestinal problems (GI).” Exact state is “newly-developed”; no finalization, approval, validation, or deployment is inferred; `StakeholderInvolvement`: one coeliac-disease patient helped select and finalize candidate wording with a gastroenterologist and two health economists (Development).
### Gaps and source conflicts

- No mapping gap or source conflict identified. Patient and expert joint refinement meets `PARTICIPATORY_DESIGN`; survey completion alone does not.
### High-value canonical terms

- EQ-5D-5L; dining (DI); gastrointestinal problems (GI); cognition (CO); sleep (SL); tiredness (TI); GSRS; SWLS; principal component analysis; confirmatory factor analysis.

## C013 — Longitudinal HRQoL in spinocerebellar ataxia

### Assessment

- Complete health-outcome reanalysis of two longitudinal cohorts.
### Study identity and primary family

- One study; primary family `HEALTH_OUTCOME_RESEARCH` because it follows HRQoL and its determinants in SCA patients (Objectives; Summary).
### Purposes, status, and publication form

- Ranked purpose: `OUTCOME_DESCRIPTION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- EUROSCA and ESMI parts: `QUANTITATIVE_EMPIRICAL`, `LONGITUDINAL_REPEATED`, `BETWEEN_GROUP`, `NONRANDOMIZED`; two `PRIOR_RESEARCH_COLLECTION` uses at `PARTICIPANT_RESPONSE` level (Study Design; Sample Selection).
### Populations and sample stages

- Population: manifest SCA1, SCA2, SCA3, or SCA6 patients in European and US centers. Source baseline counts conflict; the main panel model reports `ANALYZED` 344 and up to four observations per patient (Sample; Table 3).
### Instrument uses and administration

- “EQ-5D-3L” is `INPUT_DATA_PROVENANCE` as `OUTCOME_MEASURE`; “PHQ-9” is input provenance as `PREDICTOR_MEASURE`; “SARA” and “INAS” are input clinical predictor measures (Data Assessment); The “European value set” has `SCORING` use that links EQ-5D-3L profiles to utility indices (EQ-5D-3L section).
### Method, protocol, scoring, and model uses

- MICE, Spearman correlation, paired tests, panel regression, and sensitivity regressions are `QUANTITATIVE_ANALYSIS` (Statistical Analyses); Panel random-effects regression is `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; time-specific linear regressions are `SENSITIVITY` (Multivariable and Sensitivity Analyses).
### Outcomes and principal findings

- HRQoL declined from 0.665 to 0.633 over three years, average −0.011 per year. SARA and PHQ-9 correlated strongly with HRQoL (Results); Higher BMI, male sex, earlier onset, increasing ataxia, and increasing depression predicted greater decline; INAS, SCA6, and restless-legs terms were null in the panel model (Table 3).
### Interpretations and limitations

- Interpretation: mental-health and weight management are potentially modifiable clinical targets, but intervention effects need evaluation (Discussion; Summary); Limitations: merged cohorts restricted shared variables; baseline-only BMI; differing RLS measures; SCA6/time-period heterogeneity; cognition and duration unavailable; European weights and populations limit precision/generalization (Strengths and Limitations).
### Products and concepts

- `StudyFactor`: SCA type is `STUDIED_CONDITION`; BMI, PHQ-9 depression, SARA ataxia, sex, and age at onset are `EXPOSURE_OR_DETERMINANT`; baseline and years 1–3 are `TARGET_STAGE` (Methods; Results); Concepts: spinocerebellar ataxia, HRQoL progression, depression, weight, independence.
### Gaps and source conflicts

- `SourceConflict`: Sample Selection gives 1,140 total minus 298 controls = 842 manifest patients, but also gives EUROSCA 525 plus ESMI 310 = 835. Abstract repeats 525 and 310. Do not combine these as one verified baseline count.
### High-value canonical terms

- EQ-5D-3L; European value set; Scale for Assessment and Rating of Ataxia (SARA); Inventory of Non-Ataxia Signs (INAS); Patient Health Questionnaire (PHQ-9); MICE; panel regression.

## C014 — Asian CUA health-state utility review

### Assessment

- Complete systematic review with explicit evidence and reporting-quality targets.
### Study identity and primary family

- One study; primary family `EVIDENCE_SYNTHESIS` (Title; Methods; Conclusion).
### Purposes, status, and publication form

- Ranked purposes: `EVIDENCE_SYNTHESIS`, `METHOD_OR_PROTOCOL_QUALITY`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `REVIEW_ARTICLE`.
### Study parts, design, and data origin

- One review part: `EVIDENCE_SYNTHESIS`, `VARIABLE_SOURCE_TIME`, `NONCOMPARATIVE`, `NOT_APPLICABLE`; synthesis `SYSTEMATIC_REVIEW` and `NARRATIVE_SYNTHESIS`; Data uses are `REVIEW_EXTRACTED_EVIDENCE` at `DOCUMENT` and `AGGREGATE_ESTIMATE` levels (Methods).
### Populations and sample stages

- Evidence population: English-language published QALY-based CUAs for Asian populations. `APPROACHED`: 3,379 records; 1,958 after duplicates; `INCLUDED_EVIDENCE`: 789 studies and 4,052 base-case HSUs (Study selection; HSU characteristics).
### Instrument uses and administration

- “EQ-5D” is `CURRENT_STUDY_OBJECT` as `EVIDENCE_SYNTHESIS_TARGET`; source studies also used it to estimate HSUs. SF-6D, HUI, QWB, TTO, SG, VAS, and mapping are preserved as exact observed methods (HSU characteristics).
### Method, protocol, scoring, and model uses

- Four-database systematic search is `EVIDENCE_IDENTIFICATION`; duplicate independent selection and standardized Excel extraction are `QUALITY_CONTROL`; categorical descriptive comparison is `EVIDENCE_SYNTHESIS` (Methods); CHEERS is `DISCUSSION_ONLY` as `REPORTING_GUIDELINE`; it was not the direct appraisal protocol (Discussion).
### Outcomes and principal findings

- Reporting quality: nonreporting was 65.4% for estimation method, 76.9% for HRQoL sample source, 84.3% for sample size, and 91.0% for preference source (Nonreporting); Among reported methods, EQ-5D was most frequent, 781 of 1,349, or 55.7%. Reported HRQoL and preference sources were mostly Asian and usually matched the target country (Results).
### Interpretations and limitations

- Interpretation: HSU methods improved over time, but missing detail prevents quality and appropriateness assessment; future CUAs need better search and reporting (Discussion; Conclusion); Limitations: English-only studies, severe source nonreporting, unpublished CUAs absent, and appropriateness of HSU reuse not tested (Discussion).
### Products and concepts

- `StudyFactor`: publication period before/after 2010 is `STRATIFIER` for reporting and method trends (Data analysis; Results); Concepts: health-state utility, cost-utility analysis, reporting quality, Asian HTA, local preference data, evidence synthesis.
### Gaps and source conflicts

- `SourceConflict`: Abstract gives comparison periods 1990–2010 and 2011–2020; Methods and included-study results give 1999–2010 and 2011–2019; `SourceConflict`: Source of preference data says 365 of 4,025 HSUs, while the study total and Table 2 are 4,052 HSUs.
### High-value canonical terms

- health-state utility (HSU); cost-utility analysis (CUA); EQ-5D; SF-6D; Health Utilities Index (HUI); Quality of Well-Being (QWB); time trade-off (TTO); standard gamble (SG); CHEERS.

## C015 — Alcohol-consumption change during COVID-19

### Assessment

- Complete longitudinal health-outcome study without an EQ instrument.
### Study identity and primary family

- One study; primary family `HEALTH_OUTCOME_RESEARCH`. It follows a health-behavior outcome and determinants in a population defined by the COVID-19 pandemic context (Abstract; Introduction; Conclusions).
### Purposes, status, and publication form

- Ranked purpose: `OUTCOME_DESCRIPTION`; Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`.
### Study parts, design, and data origin

- One part: `QUANTITATIVE_EMPIRICAL`, `LONGITUDINAL_REPEATED`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `CURRENT_STUDY_COLLECTION`, `PARTICIPANT_RESPONSE` (Study Design; Data Collection).
### Populations and sample stages

- Population: adults aged 18–75 years from general-population internet panels in Greece, Italy, Netherlands, Sweden, UK, and US. `ENROLLED` T1 19,902; `COMPLETED` all three waves and `ANALYZED` 4,999 (Data Collection; Study Sample).
### Instrument uses and administration

- “Patient Health Questionnaire-9 (PHQ-9)” and “Generalized Anxiety Disorder Questionnaire (GAD-7)” are `DIRECT_CURRENT_ACTIVITY` as `PREDICTOR_MEASURE` (Socio-Demographics and Health); Adult self-report by web at T1–T3; translated and back-translated country-language surveys; PHQ-9/GAD-7 recall two weeks; pre-pandemic alcohol was recalled at T3 (Data Collection; measures).
### Method, protocol, scoring, and model uses

- Internet-panel quota recruitment is `SAMPLING`; three web surveys are `QUANTITATIVE_DATA_COLLECTION`; tests, Sankey plots, and multinomial logistic regression are `QUANTITATIVE_ANALYSIS` (Statistical Analyses); Multinomial logistic regression is `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; country-stratified models are `SUBGROUP` (Results).
### Outcomes and principal findings

- Alcohol-consumption change: 82.3% no change, 12.6% decrease, and 5.1% increase (Results); Increased and decreased use shared male sex, depression, prior excessive drinking, and job loss as predictors; associations were stronger for increase. Anxiety was not an independent predictor (Predictive Factors; Discussion).
### Interpretations and limitations

- Interpretation: results can identify groups for post-pandemic alcohol and mental-health support; more follow-up and country-policy research are needed (Conclusions); Limitations: 25% three-wave response and differential attrition; social-desirability, internet-panel, extreme-drinker selection, and recall bias; country policy confounding not measured (Strengths and Limitations).
### Products and concepts

- `StudyFactor`: alcohol-change group is `STUDIED_CONDITION`; age, sex, education, PHQ-9 depression, previous excessive drinking, chronic disease, general-health change, and job loss are `EXPOSURE_OR_DETERMINANT`; country is `STRATIFIER`; T1, T2, T3 are `TARGET_STAGE` (Methods; Results); Concepts: COVID-19 pandemic, alcohol consumption, depression, job loss, health behavior.
### Gaps and source conflicts

- Family-rule risk: this mapping treats alcohol consumption as a health outcome and pandemic exposure as the defining condition. If `HEALTH_OUTCOME_RESEARCH` is intended only for patient disease outcomes, the current definition needs clarification; do not create a new value during extraction; No source conflict identified.
### High-value canonical terms

- POPulation health impact of the CORoNavirus disease 2019 pandemic (POPCORN); PHQ-9; GAD-7; multinomial logistic regression; Sankey plot.

## Complete primary-family partition

Counting unit is one distinct study. The partition contains all 15 studies once.

| Primary family or gap | Studies | Count |
|---|---|---:|
| `VALUE_SET_DEVELOPMENT` | C001, C010 | 2 |
| `MEASUREMENT_PROPERTY_EVALUATION` | C003 | 1 |
| `INSTRUMENT_VERSION_DEVELOPMENT` | C002, C012 | 2 |
| `POPULATION_REFERENCE_DESCRIPTION` | C004 | 1 |
| `METHODS_RESEARCH` | C008, C009, C011 | 3 |
| `APPLIED_USE_RESEARCH` | C006, C007 | 2 |
| `EVIDENCE_SYNTHESIS` | C014 | 1 |
| `HEALTH_OUTCOME_RESEARCH` | C013, C015 | 2 |
| `UNMAPPED_VALUE` | C005 | 1 |
| **Total** | **C001–C015** | **15** |

No study maps to `MAPPING_OR_CROSSWALK`, `HEALTH_ECONOMIC_EVALUATION`,
`CONCEPTUAL_FRAMEWORK_DEVELOPMENT`, or another family in this round.

## Aggregate gap log
### G1 — Cost-of-illness family and purpose

- State: `UNMAPPED_VALUE`; Affected fields: C005 `primary_research_family` and main `research_purpose`; Evidence: the study estimates 2014 prevalent societal costs, productivity losses, and monetized DALYs for vision impairment; it does not compare intervention costs and consequences for a decision (Abstract; Classification; Discussion); Importance: forcing `HEALTH_ECONOMIC_EVALUATION` would remove its explicit decision requirement. `OUTCOME_DESCRIPTION` captures a secondary descriptive purpose but not the main economic-burden aim; **PROPOSAL ONLY:** add family `ECONOMIC_BURDEN_RESEARCH`, defined as estimation of the total costs and non-cost burden attributable to a condition without comparative decision analysis. Add purpose `ECONOMIC_BURDEN_ESTIMATION`, with the same boundary. Review can instead decide to broaden `HEALTH_ECONOMIC_EVALUATION`, but it must change the current definition explicitly.
### G2 — Retraction status and provenance

- State: `UNMODELED_ASPECT`; retraction date and reason are `NOT_REPORTED` in the supplied file; Affected field: C010 publication status; Evidence: the title is “RETRACTED ARTICLE: The EQ-5D-5L Valuation Study in Egypt,” while ontology v0.2 models publication form but not retraction (title; Status and publication facts in ontology); Importance: users must be able to exclude or flag retracted reports without changing study execution, results availability, or product validation state; **PROPOSAL ONLY:** add a source-dated `PublicationStatusAssertion` with controlled status `RETRACTED`, exact source term, assertion date, asserted-by organization, notice identifier, reason text, and evidence locator. Missing notice facts must remain `NOT_REPORTED`.

## Source-conflict register

| ID | Study | Conflict |
|---|---|---|
| SC1 | C002 | Cronbach’s alpha 0.85 in Abstract/Discussion versus 0.84 in Results. |
| SC2 | C002 | Martin-Loef *p* > 0.99 in Abstract versus *p* = 0.12 in Results. |
| SC3 | C006 | Final samples 52,926/94,795 and total 147,721 versus 52,000/93,448 and total 145,448. |
| SC4 | C011 | Abstract says higher VAS variance for child perspectives; Results says higher variance for adult perspectives. |
| SC5 | C013 | Manifest baseline total 842 versus component totals 525 + 310 = 835. |
| SC6 | C014 | Review periods 1990–2010/2011–2020 versus 1999–2010/2011–2019. |
| SC7 | C014 | Preference-source denominator 4,025 versus total 4,052 HSUs. |

## Risks to current rules

- `PARTICIPATORY_DESIGN`: C007 shows that stakeholder interviews can inform later co-design without being joint design. C008, C009, and C012 do report direct joint refinement and fit the value. Keep the current threshold; Product state: C010 shows that publication retraction must not be converted into value-set validation failure or withdrawal. Publication status and product state need separate assertions; `HEALTH_OUTCOME_RESEARCH`: C015 fits only if health behavior and a pandemic-defined general population are inside “health outcome” and “condition-defined population.” Clarify this wording before broader aggregation; `HEALTH_ECONOMIC_EVALUATION`: C005 shows that its decision requirement excludes descriptive cost-of-illness research. Do not force the mapping; Study allocation: C001 and C010 randomize task blocks, and C011 randomizes task order. These are task-design facts, not randomized study allocation. C008 separately randomizes people to forced versus unforced task versions, so `RANDOMIZED` applies there.

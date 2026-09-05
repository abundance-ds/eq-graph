# Round 03 application A

## Exact inputs and verification

I used only `AGENTS.md`,
`pilot/ontology-development-v4/ROUND3_APPLICATION_TASK.md`,
`pilot/ontology-development-v4/PROTOCOL.md`,
`pilot/ontology-development-v4/ONTOLOGY.md`,
`pilot/ontology-development-v4/EXTRACTION_TASK.md`,
`pilot/ontology-development-v4/round-03.tsv`, and the 15 article files listed
below. I did not use an earlier application, review, decision, graph record,
old ontology, prior extraction, or Neo4j guidance.

All checks used the file bytes. All 15 checks match `round-03.tsv`.

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

### 1. Assessment

- Complete value-set study with direct German general-population valuation and a selected hybrid scoring model. (Abstract; Methods; Preferred Model)
### 2. Study identity and primary family

- Study: German EQ-5D-5L valuation study. Primary family: `VALUE_SET_DEVELOPMENT`. (Objectives; Conclusions)
### 3. Purposes, status, and publication form

- Ranked purposes: `VALUE_SET_DEVELOPMENT`, `HEALTH_STATE_VALUATION`, `VALUATION_METHOD_EVALUATION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Objectives; Results; Conclusions)
### 4. Study parts, design, and data origin

- One quantitative valuation part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_METHOD`, `NONRANDOMIZED`; `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. cTTO and DCE blocks were task-randomized, not study allocation. (Study Design; Valuation Interview)
### 5. Populations and sample stages

- Population: German residents aged over 18 years; quota targets were age, sex, education, and employment. `COMPLETED` and `ANALYZED`: 1,158 interviews; 83 interviews were quality-flagged but respondents were retained. (Study Design; Results; Data Analysis)
### 6. Instrument uses and administration

- EQ-5D-5L: `CURRENT_HEALTH_MEASUREMENT` and `VALUATION_TARGET`, both `DIRECT_CURRENT_ACTIVITY`; German version. CAPI was face-to-face and interviewer-administered in six German areas. Current health was self-reported; valuation used societal preferences. (Study Design; Valuation Interview)
### 7. Method, protocol, scoring, and model uses

- Exact methods: “composite time trade-off (cTTO)” and “discrete choice experiment (DCE) without duration”, `PREFERENCE_ELICITATION`; “EQ-VT QC software”, `QUALITY_CONTROL`. “EQ-VT 2.0” is a `VALUATION_PROTOCOL`. (Valuation Interview; Quality Control)
- TaskDesign: cTTO used 86 target states in ten blocks of ten; DCE used 196 A/B pairs in 28 blocks of seven. Each respondent received one random block of each. cTTO used 10 years, conventional/lead-time paths, and an indifference point; DCE was forced choice. (Valuation Interview)
- Models: “censored at −1 Tobit model”, “conditional logit model”, and “hybrid model … accommodating heteroskedasticity”, `STATISTICAL_ESTIMATION`; Model 3b is `PRIMARY_REPORTED`, others `CANDIDATE`; sensitivity exclusions are `SENSITIVITY`. (Data Analysis; Preferred Model)
### 8. Outcomes and principal findings

- Outcome family: preference or utility. Model 3b was selected because it handled heteroskedasticity and had the highest coefficient precision and fit. Predicted values ranged from −0.661 to 1. (Preferred Model; Abstract Results)
- All selected-model coefficients were logical and significant. Dimension order was pain/discomfort, anxiety/depression, self-care, mobility, usual activities. Observed negative cTTO values were 17.3%. (Modeling; Data Characteristics)
### 9. Interpretations and limitations

- Interpretation: the authors recommend this value set as the preferred German set and state that EQ-VT 2.0 with quality control is a sound national valuation basis. (Conclusions)
- Limitation: the sample was clustered in six regions and had a small middle-class bias. (Discussion)
### 10. Products and concepts

- Product: German EQ-5D-5L value set, `VALUE_SET`, with source term “recommended as the preferred value set for Germany”. This recommendation is not a formal-approval assertion. Concepts: states worse than dead; respondent feedback; national societal preferences. (Key Points; Conclusions)
### 11. Gaps and source conflicts

- SC5: Cronbach's alpha is 0.85 in the Abstract and Discussion but 0.84 in Results. SC6: the Martin-Loef p-value is greater than 0.99 in the Abstract but 0.12 in Results. The qualitative conclusions agree, but the exact values conflict. (Abstract Results; Results; Discussion)
### 12. High-value canonical terms

- EQ-5D-5L; EQ-VT 2.0; composite time trade-off (cTTO); discrete choice experiment (DCE) without duration; censored Tobit model; conditional logit model; heteroskedastic hybrid model.
## C002 — QID-12 short-form development

### 1. Assessment

- Short-form instrument development and same-sample psychometric validation from six prior datasets. (Abstract; Sources of data)
### 2. Study identity and primary family

- Study: development of QID-12 from QI-Disability. Primary family: `INSTRUMENT_VERSION_DEVELOPMENT`. (Purpose; Conclusions)
### 3. Purposes, status, and publication form

- Ranked purposes: `INSTRUMENT_DEVELOPMENT`, `MEASUREMENT_PROPERTY_EVALUATION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One reanalysis part: `QUANTITATIVE_EMPIRICAL`, `VARIABLE_SOURCE_TIME`, `BETWEEN_INSTRUMENT`, `NOT_APPLICABLE`; one `PRIOR_RESEARCH_COLLECTION` DataUse for each named dataset, all at `PARTICIPANT_RESPONSE` level. Collections span 2016–2023. (Sources of data)
### 5. Populations and sample stages

- Population: children aged 3–18 years with mild-to-profound intellectual disability. `ANALYZED`: 1,699 unique complete proxy measures: Kids datasets 603, Simons Searchlight 953, and Inchstone 143. (Sources of data; Results)
### 6. Instrument uses and administration

- QI-Disability, exact source label “Quality of Life Inventory – Disability (QI-Disability)”: `DEVELOPMENT_OBJECT` and `COMPARATOR`, `DIRECT_CURRENT_ACTIVITY`; parent/caregiver proxy report. QID-12: `CONTENT_TEST_OBJECT`, `DIRECT_CURRENT_ACTIVITY`. EQ-5D-Y-5 L only has `INPUT_DATA_PROVENANCE` for one source dataset. (Variables; Sources of data)
### 7. Method, protocol, scoring, and model uses

- Exact methods: “Genetic algorithm (GA)” with R package `GAabbreviate`, `MAPPING_OR_DERIVATION`; Pearson correlation and Cronbach’s Alpha, `MEASUREMENT_PROPERTY_ANALYSIS`. (Statistical methods)
- Exact model: “partial credit model” in Rasch analysis, `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; Martin-Loef test and person-item mapping assessed dimensionality and targeting. (Statistical methods)
### 8. Outcomes and principal findings

- Outcome family: measurement property. QID-12 covered all six domains; correlation with QI-Disability was 0.970; alpha was 0.84/0.85; person separation reliability was 0.84. Items fit the partial credit model and the Martin-Loef test did not reject unidimensionality. (Results; Abstract)
- Three items had disordered category thresholds. Item targeting was reasonable but was better at the lower QOL range. (Results)
### 9. Interpretations and limitations

- Interpretation: QID-12 is suitable where burden is important, but it is not a replacement for domain-level use of the full measure. (Discussion)
- Limitations: derivation and validation used the same sample; common descriptive variables were limited; three item thresholds were disordered; independent and diverse-cohort validation is still needed. (Discussion)
### 10. Products and concepts

- Product: QID-12, `INSTRUMENT_VERSION`; source assertions are “developed and validated” and “valid and reliable”, without an inferred date or formal approval. Concepts: child QOL; proxy reporting; respondent burden; intellectual disability. (Discussion; Conclusions)
### 11. Gaps and source conflicts

- All controlled mappings above use version 0.2 values.
### 12. High-value canonical terms

- Quality of Life Inventory – Disability (QI-Disability); QID-12; Genetic algorithm (GA); GAabbreviate; Cronbach’s Alpha; Rasch analysis; partial credit model; Martin-Loef test.
## C003 — EQ-HWB proxy appropriateness in aged care

### 1. Assessment

- Qualitative content and proxy-response assessment of an experimental EQ-HWB version in residential aged care. (Abstract; Procedure)
### 2. Study identity and primary family

- Study: appropriateness of EQ-HWB proxy version 2 in residential aged care. Primary family: `MEASUREMENT_PROPERTY_EVALUATION`. (Objective; Conclusions)
### 3. Purposes, status, and publication form

- Ranked purposes: `CONTENT_VALIDITY_EVALUATION`, `MEASUREMENT_PROPERTY_EVALUATION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One part: `QUALITATIVE_INQUIRY`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `CURRENT_STUDY_COLLECTION` and `QUALITATIVE_MATERIAL`. Family and staff proxy groups were compared in interpretation, but not as a formal effect test. (Sample and Recruitment; Analysis)
### 5. Populations and sample stages

- Population: adult family and staff proxies for residents in three not-for-profit aged-care facilities in Melbourne. `COMPLETED` and `ANALYZED`: 29 proxies, nine family members and 20 staff. (Sample and Recruitment; Results)
### 6. Instrument uses and administration

- “25-item EQ-HWB proxy version 2”, English version for Australia: `CONTENT_TEST_OBJECT`, `DIRECT_CURRENT_ACTIVITY`. Perspective was proxy-person. Interviews were interviewer-administered, mainly face-to-face; one used Zoom. Instrument recall was the last 7 days. (Procedure; Results, Recall Period)
### 7. Method, protocol, scoring, and model uses

- “Cognitive think-aloud interviews” and “semi-structured questions”, `QUALITATIVE_DATA_COLLECTION`; “thematic analysis” with deductive and inductive coding, `QUALITATIVE_ANALYSIS`. (Procedure; Analysis)
### 8. Outcomes and principal findings

- Outcome families: content validity; feasibility; usability and acceptability. Theme 1 concerned accurate proxy reporting: perspective adherence, proxy-resident disagreement, limited knowledge, proxy type, and evidence or heuristics. (Results, Theme 1)
- Theme 2 concerned EQ-HWB suitability: relevant coverage but ambiguous or double-barrelled items, poor aged-care examples, repetition, response-scale issues, recall-period concerns, and layout or instruction issues. (Results, Theme 2)
### 9. Interpretations and limitations

- Interpretation: self-report must remain the default; proxy use can be necessary, but proxy type, perspective adherence, and central-tendency bias need attention. Item wording and examples need changes. (Discussion; Conclusions)
- Limitations: convenience sampling; no resident self-report comparison; problem-focused interviewing can understate positive comments; no head-to-head instrument comparison. (Discussion)
### 10. Products and concepts

- Concepts: proxy reporting; proxy-person perspective; residential aged care; cognitive impairment; central-tendency bias; content validity. (Discussion)
### 11. Gaps and source conflicts

- Ordinary interview participation was not coded as `StakeholderInvolvement`, because the source does not state joint design influence in this study.
### 12. High-value canonical terms

- EQ Health and Wellbeing (EQ-HWB); 25-item EQ-HWB proxy version 2; cognitive think-aloud interviews; semi-structured interviews; thematic analysis; NVivo.
## C004 — Swedish adolescent EQ-5D-Y-3L population data

### 1. Assessment

- General-population adolescent health description with subgroup reference data. (Purpose; Introduction)
### 2. Study identity and primary family

- Study: Life & Health—young people 2014 EQ-5D-Y-3L analysis. Primary family: `POPULATION_REFERENCE_DESCRIPTION`. (Study design; Purpose)
### 3. Purposes, status, and publication form

- Ranked purposes: `POPULATION_NORMS`, `OUTCOME_DESCRIPTION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `ROUTINE_SERVICE_COLLECTION` and `PARTICIPANT_RESPONSE`. The county survey supports health decisions and school health promotion. (Study design; Discussion)
### 5. Populations and sample stages

- Population: students aged 13–18 years in Örebro County, Sweden. `COMPLETED`: 7,399, response rate 79.7%; 6,805 remained after age/sex eligibility; 231 incomplete EQ-5D-Y-3L cases were `EXCLUDED`; 6,574 were `ANALYZED`. (Response rate)
### 6. Instrument uses and administration

- Swedish EQ-5D-Y-3L: `CURRENT_HEALTH_MEASUREMENT` and `OUTCOME_MEASURE`, `DIRECT_CURRENT_ACTIVITY`; self-report, self-completed paper and pencil, classroom setting, “today” recall. EQ VAS was part of the same use. (Study design; EQ-5D-Y-3L)
- Self-rated health question, mental-distress questions, disease and impairment questions, and self-reported BMI inputs were `PREDICTOR_MEASURE`. (Measures)
### 7. Method, protocol, scoring, and model uses

- Chi-square/Fisher tests, Mann–Whitney U, multiple logistic regression, and multiple linear regression are `QUANTITATIVE_ANALYSIS`. No value set was applied. (Data analyses; Discussion)
- StudyFactors: sex, age group, parental occupational status, disease, impairment, mental distress, self-rated health, and BMI are `EXPOSURE_OR_DETERMINANT`; their reported levels remain source-faithful. (Measures; Data analyses)
### 8. Outcomes and principal findings

- Outcome family: health status and EQ VAS. Profile 11111 occurred in 44.9%. Girls reported more usual-activity, pain/discomfort, and mood problems and lower VAS than boys. (Health profiles; Sex and age)
- One or both parents unemployed, disease, impairment, mental distress, and obesity were associated with worse reported health. Always feeling depressed had the largest reported VAS impact; the mood-problem prevalence was 90.7% in that group. (Results; Regression analyses)
### 9. Interpretations and limitations

- Interpretation: these population data can guide prioritization and comparisons with patient groups. (Conclusions)
- Source-reported limitation: adolescents’ reports of parental occupation can be unreliable as a socioeconomic proxy. (Discussion)
### 10. Products and concepts

- Product: Swedish adolescent EQ-5D-Y-3L population data, `POPULATION_REFERENCE_DATA`; no approval or validation state is inferred. Concepts: adolescent health; health inequality; mental distress; socioeconomic status. (Introduction; Discussion)
### 11. Gaps and source conflicts

- All controlled mappings above use version 0.2 values.
### 12. High-value canonical terms

- EQ-5D-Y-3L; EQ VAS; Life & Health—young people; self-rated health; parents’ occupational status; mental distress.
## C005 — Societal cost of vision impairment

### 1. Assessment

- Bottom-up, prevalent cost-of-illness and wellbeing-burden study. It has no intervention comparison. (Introduction; Methods; Discussion)
### 2. Study identity and primary family

- Study: 2014 societal economic impact of presenting vision impairment in Trinidad and Tobago. Primary family: `UNMAPPED_VALUE`, gap G1. `HEALTH_ECONOMIC_EVALUATION` does not fit because the paper does not compare costs and consequences of decision alternatives. (Aim; Classification of economic impact)
### 3. Purposes, status, and publication form

- Supported purpose: `OUTCOME_DESCRIPTION`; cost-of-illness purpose is `UNMAPPED_VALUE`, gap G2. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Aim; Results)
### 4. Study parts, design, and data origin

- Survey/cost part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `PRIOR_RESEARCH_COLLECTION` participant responses from NESTT and `PUBLISHED_MODEL_INPUT` model parameters. A contemporaneous eye-system survey is a second `PRIOR_RESEARCH_COLLECTION` source. (Methods; Classification of economic impact)
- Burden calculation part: `MODEL_BASED`, `NOT_APPLICABLE`, `BETWEEN_CONTEXT`, `NOT_APPLICABLE`; inputs include census population, unit costs, disability weights, and value-of-statistical-life assumptions at `MODEL_PARAMETER` level. (Statistical methods; Intangible effects)
### 5. Populations and sample stages

- Population: Trinidad and Tobago adults aged at least 40 years in 2014. NESTT had 4,263 eligible adults; 3,589 responded to visual assessment; utilization data were available for 2,792 and cost data for 2,516. (Methods; Abstract Results)
### 6. Instrument uses and administration

- No EQ instrument use. Clinic-based questionnaires measured utilization, costs, socioeconomic facts, and access. The paper uses disability weights from published sources, not direct preference elicitation. (Methods; Intangible effects)
### 7. Method, protocol, scoring, and model uses

- “bottom-up cost” and “cost-of-illness” estimation are `ECONOMIC_EVALUATION`; the “simple human capital approach” and prevalent DALY calculation are `DECISION_ANALYSIS`, `PRIMARY_REPORTED`. One-way deterministic sensitivity analysis is `SENSITIVITY`. (Abstract; Classification; Sensitivity analyses)
- “Cost of Vision Loss Consensus Guidelines (2010)” is `GOVERNING_STUDY_PROTOCOL`, `DIRECT_CURRENT_ACTIVITY`. (Introduction; Methods)
### 8. Outcomes and principal findings

- Outcome families: cost, QALY, and ICER; health status and EQ VAS, limited here to cost and DALY burden. Total societal cost was TT$3.842 billion/UK£365.650 million; wellbeing loss was 73.3%. Excluding it, cost was TT$1.025 billion/UK£97.547 million, with 70.5% indirect cost. (Abstract Results; Table 2)
- Affected persons and families bore 97.6% of cost. Estimated distance-VI cases were 64,431, of which 86.1% were potentially avoidable. Alternative disability weights changed wellbeing-cost estimates about fourfold. (Discussion; Sensitivity analyses)
### 9. Interpretations and limitations

- Interpretation: direct health-sector cost alone understates the societal burden and can misdirect resource decisions. (Conclusion)
- Limitations: age 40+ only; institutionalized people and long-term care omitted; 59–66% response creates nonresponse risk; 12-month recall; transfer payments, dead-weight loss, carer opportunity cost, and several downstream health costs omitted; DALY monetization is conceptually and ethically limited. (Discussion)
### 10. Products and concepts

- Concepts: vision impairment; cost of illness; productivity loss; informal care; wellbeing loss; DALY; avoidable vision impairment. (Methods; Discussion)
### 11. Gaps and source conflicts

- G1 and G2 apply; the source statements used for the record are mutually consistent.
### 12. High-value canonical terms

- National Eye Survey of Trinidad and Tobago (NESTT, 2014); Cost of Vision Loss Consensus Guidelines (2010); societal perspective; bottom-up cost; human capital approach; Disability Adjusted Life Year (DALY).
## C006 — Determinants of peripheral nerve block use

### 1. Assessment

- Observational implementation/utilization study with clinical outcomes; it has no EQ instrument use. (Abstract; Data)
### 2. Study identity and primary family

- Study: determinants of PNB use in Medicare THA and TKA cases. Primary family: `APPLIED_USE_RESEARCH`. (Background; Conclusions)
### 3. Purposes, status, and publication form

- Ranked purposes: `IMPLEMENTATION_EVALUATION`, `OUTCOME_DESCRIPTION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- THA and TKA are separate parts because each has its own sample and analysis. Each is `QUANTITATIVE_EMPIRICAL`, `VARIABLE_SOURCE_TIME`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `ROUTINE_SERVICE_COLLECTION` and `PARTICIPANT_RESPONSE` from 2012–2021 Medicare claims. (Data; Statistical Analysis)
### 5. Populations and sample stages

- Population: US Medicare patients aged at least 66 years with primary THA or TKA. Initial cases: 241,326; eligible after clinical exclusions: 153,322; complete-case `ANALYZED`: 147,721, comprising 52,926/52,000 THA and 94,795/93,448 TKA before/after missing-data exclusion. (Abstract Methods; Inclusion; Results)
### 6. Instrument uses and administration

- No EQ or PROM use. CPT and ICD claims define arthroplasty, PNB use, comorbidity, and outcomes. (Data; Outcomes)
### 7. Method, protocol, scoring, and model uses

- Mixed-effects logistic regression is `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; confounder-adjusted population-attributable risk is `QUANTITATIVE_ANALYSIS`; county and dual-eligibility models are `SENSITIVITY`. (Statistical Analysis)
- STROBE is a `REPORTING_GUIDELINE`, `DIRECT_CURRENT_ACTIVITY`. (Data)
- StudyFactors: diagnosis, prior hospitalizations, care setting, hospital ownership, region, rurality, teaching intensity, race/ethnicity, and Social Deprivation Index are `EXPOSURE_OR_DETERMINANT`; PNB use is an exposure with comparator “no PNB”; THA/TKA is a `STRATIFIER`. No effect modifier is asserted. (Variables; Results)
### 8. Outcomes and principal findings

- Outcome families: implementation and health status. Clinical and hospital factors explained most PNB-use variation; demographic and socioeconomic factors explained little. (Abstract Results; Main Findings)
- For TKA, PNB use was associated with fewer CMS complications, OR 0.82, and less stay over 3 days, OR 0.90, but not readmission. THA associations were not significant. (Association with Secondary Outcomes)
### 9. Interpretations and limitations

- Interpretation: practice variation supports more standardized PNB provision, especially in TKA. (Conclusions)
- Limitations: associations are not causal; residual confounding is possible; Medicare limits generalizability; area deprivation can differ from individual deprivation; PAR is a maximum attainable reduction. (Strengths and Limitations)
### 10. Products and concepts

- Concepts: clinical practice variation; health inequality; peripheral nerve block utilization; total joint arthroplasty. (Discussion)
### 11. Gaps and source conflicts

- All controlled mappings above use version 0.2 values.
### 12. High-value canonical terms

- peripheral nerve block (PNB); total hip arthroplasty (THA); total knee arthroplasty (TKA); Medicare Limited Dataset; Social Deprivation Index; population-attributable risk; mixed-effects logistic regression; STROBE.
## C007 — P-PROM ROCK Phase 1

### 1. Assessment

- Qualitative pre-implementation and co-design input from adolescents, caregivers, and service providers. (Purpose; Study design)
### 2. Study identity and primary family

- Study: P-PROM ROCK Phase 1. Primary family: `APPLIED_USE_RESEARCH`. (Title; Conclusions)
### 3. Purposes, status, and publication form

- Ranked purposes: `IMPLEMENTATION_EVALUATION`, `CONTENT_VALIDITY_EVALUATION`, `DECISION_SUPPORT_DEVELOPMENT`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Purpose; Research questions)
### 4. Study parts, design, and data origin

- One part: `QUALITATIVE_INQUIRY`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `CURRENT_STUDY_COLLECTION` and `QUALITATIVE_MATERIAL`. The three stakeholder groups supplied distinct views. (Participants; Data collection)
### 5. Populations and sample stages

- Population: Royal Children’s Hospital outpatient adolescents, caregivers, and providers. Seventeen registered interest; 14 were selected, `COMPLETED`, and `ANALYZED`: three adolescents, five caregivers, six providers. (Participants; Participant characteristics)
### 6. Instrument uses and administration

- EQ-5D-Y-5L: `IMPLEMENTATION_OBJECT` and `VISUALIZATION_OBJECT`, `CURRENT_STUDY_OBJECT`; participants were shown the instrument and scoring/display options, but did not use it as a health measure. (Data collection; Results)
- Planned future clinical use is `PLANNED_ACTIVITY`, with `CURRENT_HEALTH_MEASUREMENT` and routine implementation functions. (Conclusions)
### 7. Method, protocol, scoring, and model uses

- “individual online semi-structured interviews”, `QUALITATIVE_DATA_COLLECTION`; “qualitative framework analysis”, `QUALITATIVE_ANALYSIS`; mapping to “Theoretical Framework of Acceptability”, `QUALITATIVE_ANALYSIS`. (Data collection; Data analysis)
- “co-design framework for public service design” is `PARTICIPATORY_DESIGN`, `DIRECT_CURRENT_ACTIVITY`, because Phase 1 recruited intended users and their findings influenced the program. Later co-design steps are `PLANNED_ACTIVITY`. (Study design; Conclusions)
### 8. Outcomes and principal findings

- Outcome families: implementation; usability and acceptability; content validity. Participants accepted generic P-PROM use only if clinicians use and respond to the data. Key needs were IT integration, pre-visit completion, family support, clinician training, and adequate resources. (Key themes; Discussion)
- EQ-5D-Y-5L was broadly supported, but concerns covered a short recall, negative framing, missing context, and broad items. Item-level display over time was preferred over one summary score. (Scoring and displaying results; Conclusions)
### 9. Interpretations and limitations

- Interpretation: further design and trial work is warranted, with meaningful clinical response central to implementation. (Conclusions)
- Limitations: one parent dominated one adolescent interview; younger children, fathers, and non-English speakers were absent; clinic prioritization limits transfer; only three adolescents participated; stakeholders did not choose among multiple P-PROMs. (Discussion)
### 10. Products and concepts

- StakeholderInvolvement: adolescents, caregivers, and service providers gave implementation and display input; source influence: “Results have informed co-design of the P-PROM ROCK Program.” (Abstract Conclusions)
- Concepts: routine PROM implementation; co-design; paediatric outpatient care; respondent support; clinical workflow. (Discussion)
### 11. Gaps and source conflicts

- Stakeholder roles remain source-faithful because the ontology has no controlled role list.
### 12. High-value canonical terms

- EQ-5D-Y-5L; Paediatric Patient Reported Outcome Measure (P-PROM); P-PROM ROCK; qualitative framework analysis; Theoretical Framework of Acceptability; co-design framework for public service design.
## C008 — Mixed-method PTO protocol

### 1. Assessment

- Protocol for a planned mixed-method PTO study, with completed consumer input and pilots but no main-study results. (Abstract; Data Availability; Pilot testing)
### 2. Study identity and primary family

- Study: Australian child-versus-adult social-value PTO study. Primary family: `METHODS_RESEARCH`, based on the explicit method test and detailed protocol contribution. (Box 1; Discussion)
### 3. Purposes, status, and publication form

- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `PREFERENCE_COMPARISON`, `METHOD_OR_PROTOCOL_QUALITY`. `HEALTH_STATE_VALUATION` is not assigned because main preference elicitation is planned, not current. Execution `PLANNED`; results `NO_RESULTS_YET`; form `PROTOCOL_ARTICLE`. (Abstract; Data Availability)
### 4. Study parts, design, and data origin

- Planned online PTO part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_METHOD`, `RANDOMIZED`; planned `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. Forced/unforced equivalence arms are study allocation; task order and screen side are task randomization. (Survey structure; Sample size plan)
- Planned think-aloud interview and focus-group parts: each `QUALITATIVE_INQUIRY`, `CROSS_SECTIONAL`, `BETWEEN_GROUP`, `NONRANDOMIZED`; planned qualitative material. Mixed integration is `SEQUENTIAL`, with interviews before and after survey analysis and findings used together. (Qualitative component)
### 5. Populations and sample stages

- Planned population: Australian public aged 16+, including parents and nonparents. Targets: 2,000 online surveys, about 40 one-to-one interviews, and about four focus groups of at most five. Pilot samples are 17 survey/CAG pilots, two completed convenience interviews, and planned additional pilots. (Sample size; Recruitment; Pilot testing)
### 6. Instrument uses and administration

- No EQ instrument is directly used. Planned administration is self-completed online for the survey and interviewer-administered online/in person for qualitative work. Respondents use a social-decision-maker perspective. (Perspective; Mode of administration)
### 7. Method, protocol, scoring, and model uses

- “Person Trade Off (PTO) choice experiment”, `PREFERENCE_ELICITATION`, `PLANNED_ACTIVITY`; think-aloud interview and focus group, `QUALITATIVE_DATA_COLLECTION`, `PLANNED_ACTIVITY`; framework thematic analysis, `QUALITATIVE_ANALYSIS`, `PLANNED_ACTIVITY`. (Abstract; Qualitative component; Analysis plan)
- Planned models include ratio of means, median of individual ratios, bootstrapping, multinomial logistic regression, and chaining tests. Exact task protocol is the study `PROTOCOL`, `GOVERNING_STUDY_PROTOCOL`. (PTO data analysis)
### 8. Outcomes and principal findings

- Planned outcome families: preference or utility; method performance and data quality. No main findings are reported. Planned outputs are age-relative social-value weights, forced/unforced method effects, consistency, and public reasoning. (Box 1; Discussion)
- TaskDesign: seven PTO contexts; ages 1 month through 24 years versus 40 or 55; gains of 2 or 5 life-years and relief of distress, mobility problems, or pain; Programs A/B; initial groups 100/100; bisection with three or four follow-ons; equivalence option randomized; task order and younger-group screen side randomized; midpoint inference when indifference is not observed. (PTO survey design; PTO analysis)
- StudyFactors: patient age, health-gain type, gain duration, health domain, and equivalence-option arm are `EXPOSURE_OR_DETERMINANT`; the alternative age/group is `COMPARATOR`; target stage includes survey, interview, and focus-group phases. (Box 1; Survey structure)
### 9. Interpretations and limitations

- Interpretation: the planned study can inform Australian age weighting and PTO best practice. (Abstract Discussion)
- Limitations: unsupervised online engagement; commercial panels can miss social groups; PTO focusing, aggregation, and extreme-value issues; Australia-only data. (Limitations)
### 10. Products and concepts

- Product: detailed PTO mixed-method study protocol, `PROTOCOL`, source state “protocol outlined in this paper”; ethics approval is not formal product approval. Planned anonymized survey data are not a current `DATASET` product. (Purpose; Ethics; Data access)
- StakeholderInvolvement: QUOKKA Consumer Advisory Group members simplified participant text and task wording, changed focus groups to reduce sensitive personal discussion, and piloted the survey. Method function: `PARTICIPATORY_DESIGN`. (CAG input)
- Concepts: child-health priority; social value of a QALY; age weighting; equivalence; deliberation; healthcare prioritization. (Introduction)
### 11. Gaps and source conflicts

- The statement that no dataset was generated refers to the main study; completed pilot work is separately reported and excluded.
### 12. High-value canonical terms

- Person Trade Off (PTO); bisection; ratio of means (ROM); median of individual ratios (MOIR); chaining test; QUOKKA Consumer Advisory Group; framework analysis.
## C009 — CREATE reporting checklist

### 1. Assessment

- Empirical expert-consensus development of a reporting checklist for valuation studies. (Abstract; Methods)
### 2. Study identity and primary family

- Study: Checklist for REporting VAluaTion StudiEs development. Primary family: `METHODS_RESEARCH`. (Objective; Conclusion)
### 3. Purposes, status, and publication form

- Ranked purposes: `METHOD_OR_PROTOCOL_QUALITY`, `DECISION_SUPPORT_DEVELOPMENT`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract; Conclusion)
### 4. Study parts, design, and data origin

- Expert-panel part: `QUALITATIVE_INQUIRY`, `LONGITUDINAL_REPEATED`, `NONCOMPARATIVE`, `NONRANDOMIZED`; current qualitative material across two Delphi rounds. Email-survey part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `NONCOMPARATIVE`, `NONRANDOMIZED`; current participant responses. Integration is `SEQUENTIAL`. (CREATE Development)
### 5. Populations and sample stages

- Stakeholder population: valuation-study experts and EuroQol Research Foundation members. Expert panel `ENROLLED`: five. Email survey `ANALYZED`: 16 respondents from eight countries. (Expert Panel; Results)
### 6. Instrument uses and administration

- EQ-5D, SF-6D, 15D, HUI, Quality of Well-Being, and AQoL are source-study subjects, not direct measures. Use context is `SOURCE_STUDY_ACTIVITY`; function is `EVIDENCE_SYNTHESIS_TARGET` where the prior EQ-5D review supplied items. (Introduction; CREATE Development)
### 7. Method, protocol, scoring, and model uses

- “international reporting guideline development framework” is `GOVERNING_STUDY_PROTOCOL`; “systematic literature review”, `EVIDENCE_IDENTIFICATION`; “modified Delphi panel approach”, email survey, and deliberation are `PARTICIPATORY_DESIGN` plus quantitative/qualitative collection. (CREATE Development)
- TaskDesign: the email assessment presented 26 candidate checklist items with levels “required”, “recommended”, and “optional”; greater than 50% “required” was the stated inclusion threshold before deliberation. (CREATE Development)
### 8. Outcomes and principal findings

- Outcome families: method performance and data quality; content validity. The process reduced 35 initial items to 26 candidates and then a final 21-item checklist in seven sections. (Results)
- Sixteen respondents assessed candidates; 22 items passed the greater-than-50% required threshold, and one was removed in final deliberation. (Results)
### 9. Interpretations and limitations

- Interpretation: CREATE can improve transparent reporting, appraisal, and valuation-study design. (Discussion; Conclusion)
- Limitations: few survey participants, all were EuroQol members; majority rule was arbitrary; measurement-method advances will require updates. (Discussion)
### 10. Products and concepts

- Product: CREATE, `CHECKLIST_OR_TOOL`; exact source state “final CREATE” and “finalizing the checklist”, without inferred formal approval. (Results; Methods)
- StakeholderInvolvement: five experts refined items; 16 members rated importance and suggested wording; final deliberation selected content. (Methods)
- Concepts: reporting quality; reproducibility; valuation-study appraisal; health utility measurement. (Discussion)
### 11. Gaps and source conflicts

- SourceIssue S1: Results says seven items were required by “more than 100%” of respondents, which is mathematically impossible and is probably a source error. It is not used in the extraction. (Results)
### 12. High-value canonical terms

- Checklist for REporting VAluaTion StudiEs (CREATE); multi-attribute utility-based instruments (MAUIs); modified two-round Delphi panel approach; international reporting guideline development framework.
## C010 — Retracted Egyptian EQ-5D-5L valuation article

### 1. Assessment

- Completed value-set study in an article whose title is explicitly marked “RETRACTED ARTICLE”. The source does not include the retraction notice or reason. (Title; Abstract)
### 2. Study identity and primary family

- Study: Egyptian EQ-5D-5L valuation study. Primary family: `VALUE_SET_DEVELOPMENT`. Retraction is a publication fact and does not change the study-family assignment. (Objective; Title)
### 3. Purposes, status, and publication form

- Ranked purposes: `VALUE_SET_DEVELOPMENT`, `HEALTH_STATE_VALUATION`, `VALUATION_METHOD_EVALUATION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. Retraction status is gap G3. (Abstract; Results; Title)
### 4. Study parts, design, and data origin

- One valuation part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_METHOD`, `NONRANDOMIZED`; `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. Task blocks and DCE order were randomized; study allocation was not. (Study Design; Interview Process)
### 5. Populations and sample stages

- Population: Egyptian adults, quota-sampled by age, sex, and geography. `COMPLETED`: 1,378 interviews; `EXCLUDED`: 113 protocol-poor, 75 incomplete, and 216 pilot interviews; `ANALYZED`: 974. Rural, illiterate, and age 65+ participants were underrepresented. (Data Cleaning; Participants)
### 6. Instrument uses and administration

- EQ-5D-5L: `CURRENT_HEALTH_MEASUREMENT` and `VALUATION_TARGET`, `DIRECT_CURRENT_ACTIVITY`. Egyptian Arabic EQ-VT 2.1; face-to-face interviewer administration. Illiterate participants received read-aloud assistance and graphic/colored-card aids. (Study Design; Pilot Phase; Interview Process)
### 7. Method, protocol, scoring, and model uses

- “composite time trade-off (cTTO)” and “discrete-choice experiments (DCEs)”, `PREFERENCE_ELICITATION`; EQ-VT quality-control tool, `QUALITY_CONTROL`; EQ-VT-2.1, `VALUATION_PROTOCOL`; CREATE, `REPORTING_GUIDELINE`. (Methods)
- TaskDesign: each main interview had five cTTO practice tasks, ten cTTO target states, a feedback review, and seven forced DCE pairs in random order. The cTTO design drew from 86 states in ten blocks; the DCE design drew from 196 pairs in 28 blocks. (Preference-Elicitation Techniques; Interview Process)
- GLS, Tobit, heteroskedastic, conditional logit, and hybrid models are `STATISTICAL_ESTIMATION`, `CANDIDATE`; heteroskedastic model 4 is `PRIMARY_REPORTED`; flagged-state re-inclusion is `SENSITIVITY`. (Data Analysis; Preferred Model)
### 8. Outcomes and principal findings

- Outcome family: preference or utility. Model 4 used cTTO data and was selected for logical consistency, fit, accuracy, and handling variable error. Predicted values ranged from −0.933 to 1; 1,136/3,125 states were worse than dead. Mobility had the largest decrement. (Preferred Model; Abstract)
- Current data included 8,842 unflagged cTTO values; 41% were worse than dead. The feedback module reduced respondents with an inconsistency from 26% to 12.5%. (cTTO and DCE Data)
### 9. Interpretations and limitations

- Source interpretation: the authors state that the tariff can support Egyptian CUA and HTA. This claim is retained as source text, not as current endorsement. (Discussion; Conclusion)
- Limitations: rural and illiterate participants were underrepresented; visual aids were not fully validated; COVID-19 stopped recruitment before 1,000 final interviews; marital status and insurance differed from population values. (Discussion)
### 10. Products and concepts

- Product: Egyptian EQ-5D-5L value set, `VALUE_SET`; source state “generated” and “can be used”. No approval, validation, deployment, withdrawal, or invalidation assertion is inferred. (Discussion; Conclusion)
- Concepts: states worse than dead; cultural adaptation; Arabic valuation; illiterate-participant accessibility; retraction. (Pilot Phase; Discussion; Title)
### 11. Gaps and source conflicts

- G3 applies. The retracted title and positive body claims are retained as separate source facts. They do not establish a product-state assertion or a reason for retraction.
### 12. High-value canonical terms

- EQ-5D-5L; EQ-VT-2.1; composite time trade-off (cTTO); discrete-choice experiments (DCEs); heteroskedastic model; CREATE checklist; Egyptian tariff.
## C011 — Valuation-perspective experiment

### 1. Assessment

- Direct within-person method experiment that separates child/adult and self/other valuation perspectives. (Objectives; Methods)
### 2. Study identity and primary family

- Study: experimental comparison of EQ-5D-Y-3L valuation perspectives. Primary family: `METHODS_RESEARCH`. (Objectives; Discussion)
### 3. Purposes, status, and publication form

- Ranked purposes: `VALUATION_METHOD_EVALUATION`, `HEALTH_STATE_VALUATION`, `PREFERENCE_COMPARISON`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `WITHIN_PERSON`, `RANDOMIZED`; `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE`. Perspective and health-state order and health-state block were randomized. VAS always preceded TTO. (Experimental procedure)
### 5. Populations and sample stages

- Population: bachelor Business Administration students. `ENROLLED`, `COMPLETED`, and `ANALYZED`: 205; mean age 19.48, 106 female. (Methods)
### 6. Instrument uses and administration

- EQ-5D-Y-3L: `CURRENT_HEALTH_MEASUREMENT` for familiarization and `VALUATION_TARGET` for five states, both `DIRECT_CURRENT_ACTIVITY`. Administration was self-completed in individual cubicles after video instruction, with a researcher present. (Experimental procedure)
- Perspectives: self-adult, other-adult, self-child as age 10, and other-child age 10. (Table 2)
### 7. Method, protocol, scoring, and model uses

- Exact methods “visual analogue scale (VAS)” and “composite TTO procedure”, `PREFERENCE_ELICITATION`; five-choice bisection task. (Valuation methods)
- TaskDesign: two five-state blocks; each state valued under four perspectives; VAS levels 0–100; cTTO target duration 10 years with better/worse-than-dead paths and five bisection choices. State and perspective order were randomized. (Health states; Valuation methods)
- Linear mixed-effects regression and Bayesian random-parameters/JAGS variance model are `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`. (Statistical analyses)
- StudyFactors: adult/child and self/other perspective are `EXPOSURE_OR_DETERMINANT`; health-state severity is `EFFECT_MODIFIER` for VAS because the source states that perspective effects depended on severity; health-state block is `STRATIFIER`. (Abstract Results; Valuation outcomes)
### 8. Outcomes and principal findings

- Outcome families: preference or utility; method performance and data quality. Perspective effects were small, systematic, and heterogeneous by state and respondent. TTO valuations for others were higher and less variable. (Abstract; Discussion)
- Child perspectives had more dominance violations; self-perspectives had more nontrading. The VAS variance direction is left unresolved because of source conflict SC1. (Valuation quality; Valuation precision)
### 9. Interpretations and limitations

- Interpretation: perspective can affect QALY inputs; the separate self/other and child/adult mechanisms need more work. (Discussion)
- Limitations: self-completed task instead of one-to-one interview; student sample; bisection differs from recommended elicitation; possible block randomization error; within-person anchoring/order effects. (Discussion)
### 10. Products and concepts

- Concepts: child health; valuation perspective; self-other decision; states worse than dead; dominance violation; nontrading. (Methods; Discussion)
### 11. Gaps and source conflicts

- SC1: Abstract Results says VAS variance was higher for child perspectives. Results and Discussion say VAS variance was higher for adult perspectives, with VSF-AC 1.053, 95% CrI 1.008–1.101. Both cannot be correct. (Abstract Results; Valuation precision; Discussion)
### 12. High-value canonical terms

- EQ-5D-Y-3L; visual analogue scale (VAS); composite TTO procedure; self-adult; other-adult; self-child; other-child; linear mixed-effects regression; Bayesian random-parameters model; JAGS.
## C012 — Coeliac-disease EQ-5D-5L bolt-ons

### 1. Assessment

- Development of two new bolt-ons and psychometric comparison of five bolt-ons for coeliac disease. (Objectives; Methods)
### 2. Study identity and primary family

- Study: EQ-5D-5L bolt-on development and testing in coeliac disease. Primary family: `INSTRUMENT_VERSION_DEVELOPMENT`. (Objectives; Conclusion)
### 3. Purposes, status, and publication form

- Ranked purposes: `INSTRUMENT_DEVELOPMENT`, `MEASUREMENT_PROPERTY_EVALUATION`, `CONTENT_VALIDITY_EVALUATION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- Development part: `CONCEPTUAL`, `NOT_APPLICABLE`, `NONCOMPARATIVE`, `NOT_APPLICABLE`; documentary and conceptual material from literature, prior item content, expert and patient input. Survey part: `QUANTITATIVE_EMPIRICAL`, `CROSS_SECTIONAL`, `BETWEEN_INSTRUMENT`, `NONRANDOMIZED`; current participant responses. Integration is `SEQUENTIAL`. (Development and selection; Survey)
### 5. Populations and sample stages

- Development stakeholders: one coeliac-disease patient, one gastroenterologist, and two health economists. Survey population: Hungarian adults with confirmed coeliac disease. `COMPLETED` and `ANALYZED`: 312, with mandatory complete items. (Development; Survey; Results)
### 6. Instrument uses and administration

- EQ-5D-5L: `COMPARATOR` and `CURRENT_HEALTH_MEASUREMENT`; dining (DI) and gastrointestinal problems (GI) bolt-ons: `DEVELOPMENT_OBJECT` and `CONTENT_TEST_OBJECT`; cognition, sleep, and tiredness bolt-ons: `CONTENT_TEST_OBJECT`; all `DIRECT_CURRENT_ACTIVITY`. (Outcome measures)
- GSRS and SWLS are `COMPARATOR` measures; EQ VAS is an `OUTCOME_MEASURE`. Administration was self-completed online. (Outcome measures; Survey)
### 7. Method, protocol, scoring, and model uses

- Ceiling, Shannon informativity, Spearman correlation, known-group relative efficiency, and regression are `MEASUREMENT_PROPERTY_ANALYSIS`. PCA and CFA/DWLS are `STATISTICAL_ESTIMATION`; the four-factor CFA is `PRIMARY_REPORTED`. (Analyses)
- `PARTICIPATORY_DESIGN`: the patient and expert panel selected content and finalized DI/GI wording for this test. (Development and selection)
- StudyFactors: self-perceived health, GSRS tertile, and symptom presence are `STRATIFIER` for known-group results. (Known-group validity)
### 8. Outcomes and principal findings

- Outcome families: measurement property; content validity. Any bolt-on reduced the 38.8% EQ-5D-5L ceiling; all five reduced it to 7.4%. (Distributional characteristics)
- GI correlated strongly with GSRS, r=0.712, and improved all known-group tests, relative efficiency 1.30–1.84. GI alone loaded on a factor distinct from all five core EQ-5D items. DI, GI, SL, and TI improved performance; CO added little. (Validity; Dimensionality; Discussion)
### 9. Interpretations and limitations

- Interpretation: GI has the clearest added value, but overlap with pain/discomfort and utility effects need more study. (Discussion)
- Limitations: unverified self-reported diagnoses; nonrepresentative voluntary sample in which all used a gluten-free diet; no reliability or responsiveness test; COVID-19 timing; final item wording was outside scope; utility effects were not tested. (Discussion)
### 10. Products and concepts

- Products: “dining (DI)” and “gastrointestinal problems (GI)” bolt-on items, each `INSTRUMENT_VERSION`; exact state is “newly-developed”. No finalized, approval, or validation assertion is inferred. (Abstract Methods; Discussion)
- StakeholderInvolvement: the coeliac-disease patient and experts selected concepts and finalized tested wording. Concepts: coeliac disease; bolt-ons; gastrointestinal problems; dining; ceiling effect; gluten-free diet. (Development and selection)
### 11. Gaps and source conflicts

- All controlled mappings above use version 0.2 values.
### 12. High-value canonical terms

- EQ-5D-5L; dining (DI); gastrointestinal problems (GI); cognition (CO); sleep (SL); tiredness (TI); Gastrointestinal Symptom Rating Scale (GSRS); Satisfaction with Life Scale (SWLS); PCA; CFA; DWLS.
## C013 — Longitudinal HRQoL in spinocerebellar ataxia

### 1. Assessment

- Secondary longitudinal analysis of two natural-history cohorts, with conflicting sample and correlation statements retained. (Abstract; Methods; Results)
### 2. Study identity and primary family

- Study: three-year HRQoL progression and determinants in SCA. Primary family: `HEALTH_OUTCOME_RESEARCH`. (Objectives; Summary)
### 3. Purposes, status, and publication form

- Ranked purpose: `OUTCOME_DESCRIPTION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One pooled analysis part: `QUANTITATIVE_EMPIRICAL`, `LONGITUDINAL_REPEATED`, `NONCOMPARATIVE`, `NONRANDOMIZED`; two `PRIOR_RESEARCH_COLLECTION` DataUses at `PARTICIPANT_RESPONSE` level, EUROSCA and ESMI. (Study Design; Sample Selection)
### 5. Populations and sample stages

- Population: adults with SCA1, SCA2, SCA3, or SCA6 in European and US centers. Source cohort stages conflict under SC2. Definite `ANALYZED` sample is 344 complete-baseline patients with imputed follow-up values. (Sample Selection; Results Table 1)
### 6. Instrument uses and administration

- EQ-5D-3L and EQ VAS: `OUTCOME_MEASURE`, `DIRECT_CURRENT_ACTIVITY` in this analysis and `SOURCE_STUDY_ACTIVITY` in cohorts; self-report at baseline and yearly. PHQ-9: `PREDICTOR_MEASURE`; SARA and INAS: clinician-rated `PREDICTOR_MEASURE`. (Data Assessment)
- ScoringUse: EQ-5D-3L responses scored with the exact source label “European value set”; national English and German sets were tested but not selected. (EQ-5D-3L)
### 7. Method, protocol, scoring, and model uses

- MICE, Spearman correlation, paired tests, and linear sensitivity regressions are `QUANTITATIVE_ANALYSIS`. “panel random effects (variable time) regression model” is `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`. (Statistical Analyses; Table 3)
- StudyFactors: BMI, sex, age of onset, changes in SARA and PHQ-9 are `EXPOSURE_OR_DETERMINANT`; SCA type and country/site are `STRATIFIER`; baseline and 1-, 2-, and 3-year follow-ups are `TARGET_STAGE`. No interaction claim supports `EFFECT_MODIFIER`. (Multivariable Analyses; Results)
### 8. Outcomes and principal findings

- Outcome family: health status and EQ VAS. EQ-5D-3L index fell from 0.665 to 0.633 over three years, mean −0.032, p=0.002. Self-care deteriorated most. (HRQoL Over Time)
- Higher BMI, male sex, rising SARA, and rising PHQ-9 predicted larger HRQoL decline. Age of onset was marginal, p=0.058. Correlation signs are unresolved under SC3. (Factors Influencing HRQoL)
### 9. Interpretations and limitations

- Interpretation: depression and weight are potentially modifiable care targets, but the observational models do not prove treatment effects. (Discussion)
- Limitations: pooled cohorts restricted common variables; baseline BMI only; different RLS measures; mixed SCA types and cohort periods; cognitive status and disease duration unavailable; no population weights; European focus; European value set can reduce national precision. (Strengths and Limitations)
### 10. Products and concepts

- Concepts: spinocerebellar ataxia; HRQoL progression; depression; ataxia severity; body mass index; rare disease. (Discussion)
### 11. Gaps and source conflicts

- SC2: Abstract gives ESMI 310 plus EUROSCA 525, total 835. Sample Selection states 842 manifest patients at baseline while repeating the 310 and 525 component counts. (Abstract; Sample Selection)
- SC3: Abstract reports SARA/PHQ-9 correlations of −0.589/−0.507. Results reports +0.569/+0.507 while describing inverse trends. (Abstract Results; Correlation of HRQoL)
- SourceIssue S2: Abstract calls the one-year −0.014 change “significant” but gives p=0.095. The extraction does not call it significant. (Abstract Results)
### 12. High-value canonical terms

- EQ-5D-3L; EQ VAS; European value set; Scale for Assessment and Rating of Ataxia (SARA); Inventory of Non-Ataxia Signs (INAS); Patient Health Questionnaire 9 (PHQ-9); MICE; panel random-effects regression.
## C014 — Asian CUA health-state utility review

### 1. Assessment

- Systematic review of health-state utility use and reporting in Asian cost-utility analyses. (Aim; Methods)
### 2. Study identity and primary family

- Study: review of HSU characteristics in Asian CUAs. Primary family: `EVIDENCE_SYNTHESIS`. (Title; Methods)
### 3. Purposes, status, and publication form

- Ranked purposes: `EVIDENCE_SYNTHESIS`, `METHOD_OR_PROTOCOL_QUALITY`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `REVIEW_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One part: `EVIDENCE_SYNTHESIS`, `VARIABLE_SOURCE_TIME`, `BETWEEN_CONTEXT`, `NOT_APPLICABLE`; synthesis design `SYSTEMATIC_REVIEW`. Data origin `REVIEW_EXTRACTED_EVIDENCE`, level `DOCUMENT`, with HSU-level aggregate extraction. (Methods)
### 5. Populations and sample stages

- Evidence population: English-language QALY-based CUAs for Asian populations. `APPROACHED`: 3,379 records; 1,958 after duplicates; 1,026 full texts; `INCLUDED_EVIDENCE`: 789 studies and 4,052 HSU records. (Study selection; HSU characteristics)
### 6. Instrument uses and administration

- EQ-5D, SF-6D, HUI, and QWB are `EVIDENCE_SYNTHESIS_TARGET`, `SOURCE_STUDY_ACTIVITY`; none is directly administered. EQ-5D was 781/1,349 reported-method HSUs. (Table 2; Estimation method)
### 7. Method, protocol, scoring, and model uses

- “systematic literature search”, `EVIDENCE_IDENTIFICATION`; dual independent selection/extraction and descriptive categorization, `EVIDENCE_SYNTHESIS`. TTO, SG, VAS, and mapping are source-study methods with `SOURCE_STUDY_ACTIVITY`. (Methods)
- No meta-analysis or current decision model. CHEERS is `DISCUSSION_ONLY`, not the governing protocol. (Discussion)
- StudyFactors: target country and publication period are `STRATIFIER`; the before/after period levels remain unresolved under SC7. (Data analysis)
### 8. Outcomes and principal findings

- Outcome family: method performance and data quality. Nonreporting was 65.4% for estimation method, 76.9% for HRQoL sample source, 84.3% for sample size, and 91.0% for preference source. Reporting improved after 2010. (Nonreporting)
- Of reported cases, EQ-5D was 55.7%; Asian HRQoL data 91.9%; Asian preference data 87.7%; samples at least 100 were 45.7%. Only 5% of studies reported a literature review to identify HSU values. (Study characteristics; Results)
### 9. Interpretations and limitations

- Interpretation: poor HSU reporting prevents assessment of utility appropriateness and can weaken CUA conclusions. (Discussion; Conclusion)
- Limitations: English-only studies; source nonreporting can bias observed characteristics; unpublished CUAs were absent; appropriate application of published HSUs was not assessed. (Discussion)
### 10. Products and concepts

- Concepts: health-state utility; cost-utility analysis; reporting quality; local preference data; Asian HTA. (Background; Discussion)
### 11. Gaps and source conflicts

- SC4: the paper consistently reports 4,052 HSUs, but “Source of preference data” uses denominator 4,025. The 4,052 denominator is retained and the mismatch remains unresolved. (Abstract; Table 2; Source of preference data)
- SC7: Abstract Methods gives comparison periods 1990–2010 and 2011–2020. Main Methods gives 1999–2010 and 2011–2019, which agree with the reported publication range. The exact period labels conflict. (Abstract Methods; Data analysis; Study characteristics)
### 12. High-value canonical terms

- health-state utility (HSU); cost-utility analysis (CUA); EQ-5D; SF-6D; Health Utilities Index (HUI); Quality of Well-Being (QWB); time trade-off (TTO); standard gamble (SG); visual analogue scale (VAS); mapping.
## C015 — Alcohol-consumption change during COVID-19

### 1. Assessment

- Multi-country longitudinal health-behavior outcome study with predictors and no EQ instrument use. (Abstract; Study Design)
### 2. Study identity and primary family

- Study: POPCORN alcohol-consumption change analysis. Primary family: `HEALTH_OUTCOME_RESEARCH`. (Aims; Conclusions)
### 3. Purposes, status, and publication form

- Ranked purpose: `OUTCOME_DESCRIPTION`. Execution `COMPLETED`; results `RESULTS_REPORTED`; form `ORIGINAL_RESEARCH_ARTICLE`. (Abstract)
### 4. Study parts, design, and data origin

- One part: `QUANTITATIVE_EMPIRICAL`, `LONGITUDINAL_REPEATED`, `BETWEEN_GROUP`, `NONRANDOMIZED`; `CURRENT_STUDY_COLLECTION` and `PARTICIPANT_RESPONSE` across T1–T3. (Study Design; Data Collection)
### 5. Populations and sample stages

- Population: general-population internet-panel members aged 18–75 in Greece, Italy, Netherlands, Sweden, UK, and US. T1 `COMPLETED`: 19,902; all three waves `COMPLETED` and `ANALYZED`: 4,999; longitudinal retention 25%. (Study Sample)
### 6. Instrument uses and administration

- No EQ instrument use. PHQ-9 and GAD-7 are `PREDICTOR_MEASURE`, `DIRECT_CURRENT_ACTIVITY`. Alcohol, health, disease, work, and life-event questions are current outcome/predictor measures. (Data Collection)
- Surveys were web-based and self-completed in each country’s main language after translation/back-translation; PHQ-9 and GAD-7 used a two-week recall. Alcohol change was reported retrospectively at T3. (Data Collection)
### 7. Method, protocol, scoring, and model uses

- Descriptive analysis, Sankey plots, Wilcoxon signed-rank, Kruskal–Wallis, and group tests are `QUANTITATIVE_ANALYSIS`. Multinomial logistic regression is `STATISTICAL_ESTIMATION`, `PRIMARY_REPORTED`; country models are `SUBGROUP`. (Statistical Analyses)
- StudyFactors: age, sex, country, education, chronic disease, PHQ-9 category, prior excessive drinking, health change, and job loss are `EXPOSURE_OR_DETERMINANT`; no-change drinking is `COMPARATOR`; country is also `STRATIFIER`; T1, T2, and T3 are `TARGET_STAGE`. (Statistical Analyses; Results)
### 8. Outcomes and principal findings

- Outcome family: `UNMAPPED_VALUE`, gap G4, because the assessed property is alcohol-consumption behavior. No change was 82.3%, decrease 12.6%, and increase 5.1%. (Change in Alcohol Consumption)
- Excessive prior drinking, depression symptoms, male sex, and job loss predicted both increase and decrease, with stronger association for increase. Age 35–54 and high education predicted increase; age 18–34 and chronic disease predicted decrease. (Predictive Factors)
### 9. Interpretations and limitations

- Interpretation: tailored post-pandemic alcohol and mental-health support should focus on vulnerable groups. (Conclusions)
- Limitations: low follow-up and differential attrition; social-desirability, selection, and recall bias; internet-panel sampling can miss extreme drinking; country-level policy confounding was not measured. (Strengths and Limitations)
### 10. Products and concepts

- Concepts: alcohol consumption; COVID-19; longitudinal behavior change; depression; job loss; population mental health. (Discussion)
### 11. Gaps and source conflicts

- G4 applies. The study is mapped to `HEALTH_OUTCOME_RESEARCH` because its main contribution is a longitudinal health-behavior outcome and its determinants, not population norms.
### 12. High-value canonical terms

- POPulation health impact of the CORoNavirus disease 2019 pandemic (POPCORN); Patient Health Questionnaire-9 (PHQ-9); Generalized Anxiety Disorder Questionnaire (GAD-7); multinomial logistic regression; Sankey plots.
## Complete primary-family partition

Counting unit: distinct studies, denominator 15. Each study occurs once.

| Primary family | Records | Count |
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

No study maps to `HEALTH_ECONOMIC_EVALUATION`, `CONCEPTUAL_FRAMEWORK_DEVELOPMENT`, or another current family in this batch.
## Consolidated gap log and proposals

These are proposals only. They are not ontology additions.
### G1 — Cost-of-illness primary family

- State/key: `UNMAPPED_VALUE` for `primary_research_family`, C005.
- Evidence: the aim is to estimate total prevalent societal cost of vision impairment, including direct, indirect, and intangible burden; there is no intervention comparator. (C005, Aim; Methods)
- Importance: forcing `HEALTH_ECONOMIC_EVALUATION` would merge burden estimation with comparative economic decisions and would weaken the family partition.
- Proposed resolution: add `BURDEN_OF_ILLNESS_RESEARCH`, defined as estimation of disease or condition burden in cost, disability, wellbeing, utilization, or productivity without comparison of intervention alternatives. Review can instead `MERGE` it if the economic-evaluation family definition is intentionally broadened.
### G2 — Cost-of-illness purpose

- State/key: `UNMAPPED_VALUE` for `research_purpose`, C005.
- Evidence: the stated purpose is total societal economic cost and wellbeing burden. `ECONOMIC_EVALUATION` implies a comparative decision, while `OUTCOME_DESCRIPTION` captures only part of the purpose. (C005, Aim; Classification of economic impact)
- Importance: purpose queries must distinguish burden-of-illness estimates from intervention CUAs.
- Proposed resolution: add `BURDEN_OF_ILLNESS_ESTIMATION`, with the same noncomparative boundary as G1.
### G3 — Retraction and editorial publication state

- State/key: `UNMODELED_ASPECT` for publication editorial status, C010.
- Evidence: the structured title says “RETRACTED ARTICLE”, but no controlled publication field can store retraction, its source, date, reason, or relation to the original article. (C010, title)
- Importance: retraction must be queryable and must not be misrepresented as study execution, result availability, or value-set product validity.
- Proposed resolution: add source-dated `PublicationStatusAssertion` with exact editorial state, notice identifier, notice date, reason text, and asserting organization. Keep it separate from all `Product` state assertions.
### G4 — Health-behavior outcome family

- State/key: `UNMAPPED_VALUE` for `outcome_family`, C015.
- Evidence: the primary outcome is self-reported increase, decrease, or no change in alcohol consumption during the COVID-19 pandemic. (C015, Primary Outcome Measure)
- Importance: mapping alcohol use to “health status and EQ VAS” would mix a health behavior with measured health status.
- Proposed resolution: add an outcome family such as `HEALTH_BEHAVIOR`, defined for behaviors that affect health, including alcohol use, smoking, diet, and physical activity. This proposal does not change the study's `HEALTH_OUTCOME_RESEARCH` primary family.
## Consolidated source conflicts and source issues

- SC1, C011: Abstract says VAS variance is higher for child perspectives; Results and Discussion say it is higher for adult perspectives.
- SC2, C013: 310 ESMI plus 525 EUROSCA equals 835, but Methods states 842 baseline patients.
- SC3, C013: Abstract gives negative SARA/PHQ-9 correlations; Results gives positive values while it describes inverse trends.
- SC4, C014: the overall HSU count is 4,052, but one Results subsection uses 4,025 as denominator.
- SC5, C002: Cronbach's alpha is 0.85 in Abstract/Discussion and 0.84 in Results.
- SC6, C002: the Martin-Loef p-value is greater than 0.99 in Abstract and 0.12 in Results.
- SC7, C014: Abstract and main Methods give different before/after period bounds.
- SourceIssue S1, C009: “more than 100%” is impossible.
- SourceIssue S2, C013: a one-year change with p=0.095 is called significant.
- SourceIssue S3, C015: GAD-7 is stated to range from 0 to 21, but the upper classification is written as 10–27.

No conflict was silently reconciled. The applicable record states the value used or leaves the value unresolved.
## Risks to existing rules

- G1 is a direct risk to the exact-one primary-family partition. It is one gap in 15 studies. A forced mapping would hide the scientific difference between cost-of-illness and comparative economic evaluation.
- C010 confirms the need to keep publication status separate from study status and product state. Retraction does not by itself assert that a value set is unapproved, invalid, withdrawn, or not deployed.
- C007, C008, C009, and C012 confirm that ordinary study participation and reported design influence are different. `StakeholderInvolvement` and `PARTICIPATORY_DESIGN` were used only where the source states an influence on a program, task, checklist, or item wording.
- C008 confirms that task randomization and randomized study allocation must stay separate. C001, C010, and C011 also use randomized task order or blocks without converting all such features into study allocation.
- C006, C011, C013, and C015 confirm the factor-role boundary. `EFFECT_MODIFIER` was used only for C011, where the source reports dependence on severity. Separate subgroup results alone remained `STRATIFIER`.
- C001, C002, C008, C009, C010, and C012 confirm that “preferred”, “valid”, ethics-approved, “final”, “can be used”, and “newly-developed” are different source assertions. They were not collapsed into one product maturity sequence.

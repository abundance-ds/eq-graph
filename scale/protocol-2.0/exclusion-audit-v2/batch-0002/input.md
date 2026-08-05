# EuroQol title and abstract screen scale v1

## Purpose

You are screening journal articles for an impact study of research funded by the
EuroQol Research Foundation.

The input corpus contains publications by verified funded-project leaders and
EuroQol members. A linked person is retrieval provenance only. It is not evidence
that an article is relevant or funded.

This is a recall-focused title and abstract screen. Its purpose is to remove articles
that are clearly outside EuroQol measurement and valuation research before full-text
retrieval. A later stage will assess full text, funding evidence, and project links.
Do not infer funding or match an article to a project.

## Central-object test

Retain an article only when at least one of these statements is true:

1. An EQ instrument or EuroQol method is a primary object of the research. Examples
   include development, valuation, value sets, descriptive systems, bolt-ons,
   psychometrics, translations, mapping, comparisons, population norms, and
   implementation research about the instrument itself.
2. Health or wellbeing measurement is the primary object of the research. The work
   develops or evaluates an instrument, descriptive system, preference-based score,
   mapping method, or other measurement method that could require a EuroQol funding
   check at full text.
3. Health-state valuation is the primary object of the research. The work develops,
   evaluates, or compares TTO, standard-gamble, DCE, utility-elicitation, value-set,
   or QALY methods rather than merely using their outputs.

The central object is what the article tries to learn or change. A measure that is
only used to learn about a disease, treatment, service, population, or policy is not
the central object.

## Exclusion rules

Exclude the article when any of these statements describes its main contribution:

- It reports clinical outcomes, disease burden, population differences, or treatment
  effects. EQ, HRQoL, QoL, a PROM, or a utility is only an outcome or covariate.
- It is a cost-effectiveness, cost-utility, budget-impact, reimbursement, resource-use,
  or policy study. Utilities or QALYs are only model inputs or results.
- It uses a DCE, willingness-to-pay task, or other preference method to study treatment,
  service, product, or policy preferences. It does not study measurement or
  health-state valuation.
- It evaluates a generic statistical or econometric method without a direct health
  measurement or health-state valuation purpose.
- It is about patient experience, satisfaction, decision-making, or shared decisions
  without developing or evaluating a health measurement instrument.
- It is clinically, economically, or topically unrelated to measurement and valuation.
- The record shows an ineligible format such as a conference abstract, editorial,
  letter, protocol-only conference item, correction, or retraction.

Mere mention or use of EQ-5D, EuroQol, HRQoL, QoL, a PROM, a utility, a QALY, a DCE,
TTO, mapping, validation, or preference is insufficient. Judge the aim and methods,
not keywords.

## Boundary rules

- Absence of `EuroQol` or `EQ-5D` is not by itself a reason to exclude an article.
- A non-EQ instrument-development or measurement-method article can qualify only when
  measurement is the central research contribution.
- A TTO or DCE article can qualify only when it values health states or studies the
  valuation method. Treatment and service preferences do not qualify.
- A QALY article can qualify when it studies the QALY concept or method. An economic
  evaluation that only calculates QALYs does not qualify.
- If the supplied abstract leaves genuine uncertainty about the central object, retain
  the article for full-text review.
- If the supplied text is not a usable article abstract, exclude it with E5. Examples include an author list, citation list, database placeholder, publisher boilerplate, or incomplete fragment. Do not infer relevance from the title alone.
- Use only the supplied metadata. Do not search the web or inspect other files.

## Decision codes

Start every reason with exactly one code:

- `[R1]`: An EQ instrument or EuroQol method is the primary research object.
- `[R2]`: Health measurement or health-state valuation is the primary research object.
- `[RU]`: The abstract is genuinely ambiguous, so full text is necessary.
- `[E1]`: EQ, HRQoL, QoL, a PROM, or a utility is only an outcome or covariate.
- `[E2]`: Utilities or QALYs are only inputs or results in an economic or policy study.
- `[E3]`: A DCE or preference method concerns a treatment, service, product, or policy.
- `[E4]`: The article is clinical, economic, statistical, or otherwise outside scope.
- `[E5]`: The publication format or supplied abstract field is ineligible.

Use `retain` with R1, R2, or RU. Use `exclude` with E1, E2, E3, E4, or E5.

## Boundary examples

- Retain `[R1]`: A study derives an EQ-5D-5L value set with TTO data.
- Retain `[R1]`: A study maps a cancer measure to EQ-5D utilities.
- Retain `[R1]`: A study tests responsiveness or content validity of EQ-HWB.
- Retain `[R2]`: A study develops a preference-based measure and its scoring system.
- Retain `[R2]`: A study compares TTO and DCE methods for valuing health states.
- Exclude `[E1]`: A cancer cohort compares EQ-5D scores between patient groups.
- Exclude `[E2]`: A treatment model reports cost per QALY with published utilities.
- Exclude `[E3]`: A DCE elicits preferred attributes of a clinical service.
- Exclude `[E4]`: A simulation studies mixed-logit estimation without a health-state
  valuation or measurement application.
- Exclude `[E4]`: A paper discusses reimbursement policy without studying a health
  measure or valuation method.

## Submission tool

The only task tool is:

`./submit_screening RECORD_ID retain|exclude "[CODE] SHORT EVIDENCE-BASED REASON"`

Call it exactly once for every supplied record. Each reason must be one concise
record-specific sentence of at most 240 characters. After all records are submitted,
run `./submit_screening status` and finish.


# Batch records

## P33d251169632

- Year: 2021
- Linked people: Juanita Haagsma
- Title: Can Fall Risk Screening and Fall Prevention Advice in Hospital Settings Motivate Older Adult Patients to Take Action to Reduce Fall Risk?

Abstract:

OBJECTIVE: We investigated whether an in-hospital intervention consisting of fall risk screening and tailored advice could prompt patients to take preventive action. METHOD: Patients (≥70) attending the emergency department and nephrology outpatient clinic in a Dutch hospital were screened. Patients at high risk received tailored advice based on their individual risk factors. Three months after screening, preventive steps taken by patients were surveyed. RESULTS: = 20), 70% took action. Patients most often adhered to advice on improving muscle strength and undergoing vision checkups (20%). Tailored advice and a reported low quality of life were associated with consulting a health care provider. DISCUSSION: Patients at risk in these settings are inclined to take action after screening. However, they do not always adhere to the tailored prevention advice.

## P0629cc52b6e3

- Year: 2022
- Linked people: Gerard De Pouvourville
- Title: Facilitating More Efficient Negotiations for Innovative Therapies: A Value-Based Negotiation Framework – Corrigendum

Abstract:

An abstract is not available for this content. As you have access to this content, full HTML content is provided on this page. A PDF of this content is also available in through the ‘Save PDF’ action button.

## P1d2b2c9c8eed

- Year: 2021
- Linked people: Sander van Kuijk
- Title: Development of a prognostic risk model for clear cell renal cell carcinoma by systematic evaluation of DNA methylation markers

Abstract:

BACKGROUND: Current risk models for renal cell carcinoma (RCC) based on clinicopathological factors are sub-optimal in accurately identifying high-risk patients. Here, we perform a head-to-head comparison of previously published DNA methylation markers and propose a potential prognostic model for clear cell RCC (ccRCC). PATIENTS AND METHODS: Promoter methylation of PCDH8, BNC1, SCUBE3, GREM1, LAD1, NEFH, RASSF1A, GATA5, SFRP1, CDO1, and NEURL was determined by nested methylation-specific PCR. To identify clinically relevant methylated regions, The Cancer Genome Atlas (TCGA) was used to guide primer design. Formalin-fixed paraffin-embedded (FFPE) tissue samples from 336 non-metastatic ccRCC patients from the prospective Netherlands Cohort Study (NLCS) were used to develop a Cox proportional hazards model using stepwise backward elimination and bootstrapping to correct for optimism. For validation purposes, FFPE ccRCC tissue of 64 patients from the University Hospitals Leuven and a series of 232 cases from The Cancer Genome Atlas (TCGA) were used. RESULTS: Methylation of GREM1, GATA5, LAD1, NEFH, NEURL, and SFRP1 was associated with poor ccRCC-specific survival, independent of age, sex, tumor size, TNM stage or tumor grade. Moreover, the association between GREM1, NEFH, and NEURL methylation and outcome was shown to be dependent on the genomic region. A prognostic biomarker model containing GREM1, GATA5, LAD1, NEFH and NEURL methylation in combination with clinicopathological characteristics, performed better compared to the model with clinicopathological characteristics only (clinical model), in both the NLCS and the validation population with a c-statistic of 0.71 versus 0.65 and a c-statistic of 0.95 versus 0.86 consecutively. However, the biomarker model had limited added prognostic value in the TCGA series with a c-statistic of 0.76 versus 0.75 for the clinical model. CONCLUSION: In this study we performed a head-to-head comparison of potential prognostic methylation markers for ccRCC using a novel approach to guide primers design which utilizes the optimal location for measuring DNA methylation. Using this approach, we identified five methylation markers that potentially show prognostic value in addition to currently known clinicopathological factors.

## P3f5801c0b23b

- Year: 2021
- Linked people: Iwan van der Horst
- Title: Metrology part 2: Procedures for the validation of major measurement quality criteria and measuring instrument properties.

Abstract:

A measurement is always afflicted with some degree of uncertainty. A correct understanding of the different types of uncertainty, their naming, and their definition is of crucial importance for an appropriate use of the measuring instruments. However, in perioperative and intensive care medicine, the metrological requirements for measuring instruments are poorly defined and often used spuriously. The correct use of metrological terms is also of crucial importance in validation studies. The European Union published a new directive on medical devices, mentioning that in the case of devices with a measuring function, the notified body is involved in all aspects relating to the conformity of the device with the metrological requirements. It is therefore the task of scientific societies to establish the standards in their area of expertise. After adopting the same understandings and definitions (part 1), the different procedures for the validation of major quality criteria of measuring devices must be consensually established. In this metrologic review (part 2), we review the terms and definitions of validation, some basic processes leading to the display of an indication from a physiologic signal, and procedures for the validation of measuring instrument properties, with specific focus on perioperative and intensive care medicine including appropriate examples.

## Pd2ac262eca91

- Year: 2025
- Linked people: Abdulmuminu Isah
- Title: HIV-themed escape room and perceived impact on learning among undergraduate pharmacy students in a game-naïve university: A cross-sectional study

Abstract:

Objectives This study aims to evaluate the acceptability of an HIV-themed escape room activity and the perceived impact on the learning outcomes, and knowledge of HIV management, among pharmacy students at the University of Nigeria, Nsukka. Methods The study was conducted in three different HIV-themed escape rooms designed at the Faculty of Pharmaceutical Sciences, University of Nigeria, Nsukka (UNN), involving 36 final-year pharmacy students. The escape room activity was carried out in groups of six students, and data were collected from the participants after the activity using a 14-item questionnaire. The questionnaire was divided into three sections: socio-demographics, perception and acceptability, and feedback. Descriptive and inferential statistics were used to analyse the data. Results More than half of the participants (n = 20, 55.6 %) were between the ages of 20-24 years out of which a larger percentage (n = 22, 61.1 %) were females. Female participants were more likely to recommend the activity, and students with higher academic performance reported greater improvement in critical thinking skills. All teams were able to escape the room with the shortest and longest escape times recorded as 9.51 and 19.56 min, respectively. The majority of the participants (n = 34, 94.4 %) agreed or strongly agreed that the escape room activity impacted their learning. Conclusion Overall, the participants reported a positive perception of the escape room activity, which also had a self-reported positive impact on their learning of HIV pharmacotherapy. This suggests that escape rooms hold promise as an innovative teaching approach in pharmacy education.

## P72b0042dafd5

- Year: 2023
- Linked people: Sander van Kuijk
- Title: Type A aortic dissection: optimal annual case volume for surgery

Abstract:

BACKGROUND AND AIMS: The current study proposes a novel volume-outcome (V-O) meta-analytical approach to determine the optimal annual hospital case volume threshold for cardiovascular interventions in need of centralization. This novel method is applied to surgery for acute type A aortic dissection (ATAAD) as an illustrative example. METHODS: A systematic search was applied to three electronic databases (1 January 2012 to 29 March 2023). The primary outcome was early mortality in relation to annual hospital case volume. Data were presented by volume quartiles (Qs). Restricted cubic splines were used to demonstrate the V-O relation, and the elbow method was applied to determine the optimal case volume. For clinical interpretation, numbers needed to treat (NNTs) were calculated. RESULTS: One hundred and forty studies were included, comprising 38 276 patients. A significant non-linear V-O effect was observed (P < .001), with a notable between-quartile difference in early mortality rate [10.3% (Q4) vs. 16.2% (Q1)]. The optimal annual case volume was determined at 38 cases/year [95% confidence interval (CI) 37-40 cases/year, NNT to save a life in a centre with the optimal volume vs. 10 cases/year = 21]. More pronounced between-quartile survival differences were observed for long-term survival [10-year survival (Q4) 69% vs. (Q1) 51%, P < .01, adjusted hazard ratio 0.83, 95% CI 0.75-0.91 per quartile, NNT to save a life in a high-volume (Q4) vs. low-volume centre (Q1) = 6]. CONCLUSIONS: Using this novel approach, the optimal hospital case volume threshold was statistically determined. Centralization of ATAAD care to high-volume centres may lead to improved outcomes. This method can be applied to various other cardiovascular procedures requiring centralization.

## P2d4bd1968a8b

- Year: 2026
- Linked people: Vivian Reckers-Droog
- Title: “They Are Not Going to Be Happy”: An Ethnographic Study of the Prioritization of Patients Awaiting Elective Surgery in an Academic Hospital in the Netherlands

Abstract:

BackgroundTo reduce variation in waiting time for elective surgery, a Dutch academic hospital introduced a classification system based on urgency scores to standardize decision making. Physicians, however, retain clinical discretion in assigning urgency scores. This facilitates the provision of personalized and efficient care but may also create variation between patients and lack of transparency. The aim of this study was to describe the prioritization of patients awaiting elective surgery, including the use of urgency scores, and to explore explanations for discrepancies between assigned scores and actual waiting times.MethodsWe conducted an ethnographic study combining interviews with physicians and observations of elective surgery planners in the academic hospital. Data were analyzed thematically, guided by 3 sensitizing concepts: professional autonomy, emotions, and traditions.ResultsThe prioritization of patients awaiting elective surgery begins with physicians' assessment of urgency and concludes with planners drafting the schedule. The assessment is guided by clinical parameters, patient- and physician-related factors, and logistical constraints. Importantly, the prioritization of patients for elective surgery is shaped by subjective and affective considerations, customary decision-making practices, as well as the considerable professional autonomy of physicians and planners.ConclusionsStandardized prioritization tools, such as urgency scores, may reduce unjustified variation in waiting times, but initial resistance to their implementation can hamper their use in decision-making practice. Moreover, such tools alone may fail to capture the complexity of clinical practice and the importance of the expertise and experience of physicians and planners therein. Rather than relying solely on stricter adherence to urgency scores, prioritization processes may be strengthened by facilitating communication and feedback exchanges to support a more integrated and context-specific approach that considers the complexity of clinical practice.HighlightsStandardized decision-making tools are implemented to standardize and support the prioritization of patients awaiting elective surgery.Prioritization decisions are made by different professionals, and nonclinical factors that include subjective perceptions and logistic constraints may guide these decisions.Standardized tools inadequately capture the complexity of clinical decision making and the professional autonomy physicians and planners.

## P7481844e62b4

- Year: 2025
- Linked people: Min-Woo Jo
- Title: Factors Associated with Health Related Quality of Life in Self-employed 2nd Baby Boomers

Abstract:

본 연구는 2차 베이비붐 세대 자영업자의 건강관련 삶의 질(Health Related Quality of Life, HRQoL) 수준을 파악하고, 이에 영향을 미치는 요인을 규명하고자 수행되었다. 연구 자료는 한국보건사회연구원과 국민건강보험공단이 2022년 3월부터 7월까지 수집한 한국의료패널(KHP) version 2.3 연간데이터를 활용하였으며, 최종적으로 239명의 응답자가 분석에 포함되었다. 자료 분석은 SPSS WIN 26.0 프로그램을 사용하여 t-test, ANOVA 및 다중회귀분석(multiple regression)을 실시하였다. 연구 결과, 2차 베이비붐 세대 자영업자의 HRQoL 평균은 0.97±0.16으로 나타났다. HRQoL에 유의한 영향을 미친 요인은 주관적 건강상태(β=-.29, p<.001)와 자살생각(β=-.27, p<.001)으로 확인되었으며, 이들 변인의 설명력은 23.6%였다. 따라서 2차 베이비붐 세대 자영업자의 HRQoL 향상을 위해서는 주관적 건강상태와 자살생각을 주요 고려 요인으로 반영한 맞춤형 건강증진 프로그램의 개발이 필요하다. 본 연구는 보건의료 전문가들이 해당 세대를 대상으로 효과적인 중재 전략을 설계하는 데 기초자료로 활용될 수 있을 것이다.

## P71228404da25

- Year: 2022
- Linked people: Koonal Shah
- Title: Spotlight environmental sustainability: a strategic priority for NICE

Abstract:

This article provides the context for the ambition outlined in the the National Institute for Health and Care Excellence (NICE) 2021-2026 strategy to 'lead globally on the potential to include environmental impact data in its guidance to reduce the carbon footprint of health and care'. Anthropogenic environmental changes pose a catastrophic risk to human health, with potential to widen national and global health inequalities. Recognising the fact that NICE guidance influences the way health and care is delivered and its consequent environmental impact, NICE has included environmental sustainability among its strategic priorities. This article outlines the work underway to meet this sustainability agenda at NICE.

## P3dcf7b04845b

- Year: 2023
- Linked people: Erica Lubetkin, Gouke Bonsel, Juanita Haagsma
- Title: Cross-sectional and longitudinal comparison of health-related quality of life and mental well-being between persons with and without post COVID-19 condition

Abstract:

Background Still little is known about the impact of post COVID-19 condition (PC) on health-related quality of life (HRQOL) and mental well-being. We compared participants with PC with three groups: an acute COVID-19 infection (AC) only, at least one chronic condition (CC) but no COVID-19, or no condition at all, healthy (PH). Between these disease groups, we also estimated and compared HRQOL and mental well-being change over time. Methods Participants from six countries (Greece, Italy, Netherlands, Sweden, United Kingdom and United States) completed two web-based questionnaires (T1 = April–May 2020 and T2 = April–June 2022). Primary outcomes were HRQOL, measured by EQ-5D-5L and EQ VAS, and mental well-being (measured by World Health Organisation-Five (WHO-5) Well-Being Index, Patient Health Questionnaire (PHQ)-9 and General Anxiety Disorder (GAD)-7). All analyses were stratified by the disease groups. Results In total, 4,999 participants filled out both surveys: 240 were in PC, 107 in AC, 1798 in CC and 2,854 in PH. At T2, the mean EQ-5D-5L index values for the PC, AC, CC and PH groups were 0.70, 0.73, 0.75 and 0.92 ( p &amp;lt; .001), respectively. Mean EQ VAS scores were 66, 65, 68 and 81 ( p &amp;lt; .001), respectively. Poor mental well-being, depression and anxiety mean values were highest in the PC group (47.7; 9.1; 7.4), followed by the AC group (51.1; 7.7; 5.7), CC group (56.1; 5.2; 4.2) and the PH group (65.6; 2.8; 2.5), respectively ( p &amp;lt; .001 between groups). Over time, HRQOL deteriorated in all groups, apart from the PH group. We observed the largest deterioration in the CC (EQ-5D-5L index: Δ0.03, p &amp;lt; .001) and AC group (EQ VAS: Δ6.3, p &amp;lt; .001). For the mental well-being outcomes, deterioration for WHO-5 and PHQ-9 were largest in the AC group (Δ4.8, p = .016; Δ-1.3, p = .012). Rates for GAD-7 improved for the PH and CC groups (PH: Δ1.27, CC: Δ0.56, p &amp;lt; .001). Conclusions In the cross-sectional analysis, participants with PC had the worst HRQOL and mental well-being compared to the other groups. In terms of change since the start of the COVID-19 pandemic, HRQOL and mental well-being deterioration was highest among AC participants and had a lower impact among PC participants, most likely due to pre-existing chronic disease.

## P75ff7ec10680

- Year: 2022
- Linked people: Hesam Ghiasvand
- Title: A Systematic Review on the Economic Evaluations Evidence of Enhanced External Counter-Pulsation (EECP) for Managing Chronic Stable Angina

Abstract:

Background: Chronic Stable Angina (CSA) does not respond to clinical interventions always. Therefore, enhanced external counter pulsation (EECP) has been approved by the Food and Administration Drug (FDA) as an effective technology. This study aimed to synthesize evidence on the economic evaluation of EECP in managing CSA through a systematic approach.

## P3a0bdca77a16

- Year: 2024
- Linked people: Shankar Prinja
- Title: Economic Evaluation of Targeted Therapies for Anaplastic Lymphoma Kinase- and ROS1 Fusion-Positive Non-Small Cell Lung Cancer in India.

Abstract:

PURPOSE Targeted therapies, such as crizotinib and ceritinib, have shown promising results in treating non–small cell lung cancer (NSCLC) with specific oncogenic drivers like anaplastic lymphoma kinase ( ALK), c-ros ( ROS1) oncogene, etc. This study aims to assess the cost-effectiveness of these therapies for patients with NSCLC in India. METHODS The Markov model consisted of three health states: progression-free survival, progressive disease, and death. Lifetime costs and consequences were estimated for three treatment arms: crizotinib, ceritinib, and chemotherapy for patients with ALK- and ROS1-positive NSCLC. Incremental cost per quality-adjusted life-year (QALY) gained with crizotinib and ceritinib was compared to chemotherapy and assessed using a willingness-to-pay threshold of one-time per capita gross domestic product in India. RESULTS The total lifetime cost per patient for ALK-positive NSCLC was ₹332,456 ($4,054 US dollars [USD]), ₹1,284,100 ($15,659 USD), and ₹2,337,779 ($28,509 USD) in the chemotherapy, crizotinib, and ceritinib arms, respectively. The mean QALYs lived per patient were 1.20, 2.21, and 3.34, respectively. For patients with ROS1-positive NSCLC, the total cost was ₹323,011 ($3,939 USD) and ₹1,763,541 ($21,507 USD) for chemotherapy and crizotinib, with mean QALYs lived per patient of 1.16 and 2.73, respectively. Nearly 92% and 81% reduction in the price of ceritinib and crizotinib is required to make it a cost-effective treatment option for ALK- and ROS1-positive NSCLC, respectively. CONCLUSION Our study findings suggest that the prices of ceritinib and crizotinib need to be reduced significantly to justify their value for inclusion in India's publicly financed health insurance scheme for treatment of patients with locally advanced/metastatic ALK- and ROS1-positive NSCLC, respectively.

## P199181929267

- Year: 2024
- Linked people: Eleanor Pullenayegum
- Title: Hemagglutination-Inhibition Antibodies and Protection against Influenza Elicited by Inactivated and Live Attenuated Vaccines in Children

Abstract:

BACKGROUND: Hemagglutinin (HA)-inhibiting antibodies contribute to the immune defense against influenza infection. However, there are insufficient data on the extent of correlation between vaccine-elicited HA antibodies and protection in children against different influenza strains, particularly when comparing live attenuated influenza vaccines (LAIV) versus inactivated influenza vaccines (IIV). METHODS: We measured postvaccination hemagglutination-inhibition (HAI) titers in 3-15-year-old participants of a cluster-randomized controlled trial of trivalent LAIV(3) versus IIV(3) in Canadian Hutterite colonies. We assessed HAI titers as predictors of symptomatic, reverse transcription polymerase chain reaction (RT-PCR)-confirmed influenza over 3 influenza seasons using Cox proportional hazards regression models with vaccine type as a covariate. RESULTS: For each log2 unit increase in postvaccination HAI against A/H1N1 in 2013-2014, A/H3N2 2014-2015, and B/Yamagata in 2013-2014 (each the predominant circulating strain for the respective influenza season), the reduction in the risk of confirmed influenza was equal to 29.6% (95% confidence interval [CI], 17.1%-39.5%), 34.8% (95% CI, 17.2%-47.9%), and 31.8% (95% CI, 23.8%-38.5%), respectively. No reduction in the risk of influenza was observed with B/Yamagata-specific HAI titers in 2012-2013, which was dominated by a mixture of Yamagata and Victoria strains. Despite the overall lower HAI titers in the LAIV3 group, both H1N1 and H3N2 HAI titers were associated with protection against subtype matched influenza. CONCLUSIONS: Both LAIV3- and IIV3-elicited HA antibodies are associated with protection against influenza infection in seasons when the vaccine strains match the circulating influenza strain subtypes, supporting the use of HAI as a correlate of protection for both vaccine types in children.

## Pe7d870568231

- Year: 2023
- Linked people: Brigitte Essers
- Title: A systematic review of economic evaluations for the interventions of superficial basal cell carcinoma

Abstract:

The rising incidence of superficial basal cell carcinoma (sBCC) puts a large burden on healthcare budgets worldwide. There are several treatment options for sBCC with difference in terms of effectiveness and costs. A few studies examined the cost-effectiveness of treatments for sBCC. We performed a systematic review following the PRISMA guidelines to determine the number and quality of the existing economic evaluations of treatment options for sBCC from a healthcare perspective. Our search of OVID Medline, Embase, Cochrane, and the NHS Economic Evaluation Database included all economic evaluations of any treatment for sBCC. Non-original articles, articles on high-risk BCC, and articles concerning Mohs surgery, radiotherapy, or systemic treatment were excluded. Risk of bias was evaluated using the extended version of the Consensus on Health Economic Criteria. The search was performed in February 2023, yielded 710 records and resulted in the inclusion of 4 economic evaluations. Two were trial-based economic evaluations and two were decision analytical models. Costs and effects were compared for imiquimod and 5FU versus MAL-PDT, imiquimod versus surgery, and MAL-PDT versus surgery. Due to heterogeneity, the results could not be pooled. The quality of the studies was moderate to high. One of the issues was that uncertainty around the given Incremental Costs and Effects Ratios was not or insufficiently addressed. The conclusions of the authors could not be corroborated in all cases. In the end, we conclude that treatment of sBCC with imiquimod as well as surgery seemed to provide value for money. Compared to treatment with imiquimod, MAL-PDT did not provide value for money.

## Pc9152ee952f0

- Year: 2024
- Linked people: Juanita Haagsma
- Title: Association between stringency of lockdown measures and emergency department visits during the COVID-19 pandemic: A Dutch multicentre study

Abstract:

INTRODUCTION: The COVID-19 outbreak disrupted regular health care, including the Emergency Department (ED), and resulted in insufficient ICU capacity. Lockdown measures were taken to prevent disease spread and hospital overcrowding. Little is known about the relationship of stringency of lockdown measures on ED utilization. OBJECTIVE: This study aimed to compare the frequency and characteristics of ED visits during the COVID-19 outbreak in 2020 to 2019, and their relation to stringency of lockdown measures. MATERIAL AND METHODS: A retrospective multicentre study among five Dutch hospitals was performed. The primary outcome was the absolute number of ED visits (year 2018 and 2019 compared to 2020). Secondary outcomes were age, sex, triage category, way of transportation, referral, disposition, and treating medical specialty. The relation between stringency of lockdown measures, measured with the Oxford Stringency Index (OSI) and number and characteristics of ED visits was analysed. RESULTS: The total number of ED visits in the five hospitals in 2019 was 165,894, whereas the total number of visits in 2020 was 135,762, which was a decrease of 18.2% (range per hospital: 10.5%-30.7%). The reduction in ED visits was greater during periods of high stringency lockdown measures, as indicated by OSI. CONCLUSION: The number of ED visits in the Netherlands has significantly dropped during the first year of the COVID-19 pandemic, with a clear association between decreasing ED visits and increasing lockdown measures. The OSI could be used as an indicator in the management of ED visits during a future pandemic.

## Ped41b260bf89

- Year: 2023
- Linked people: Sarah Dewilde
- Title: Patient-reported burden of myasthenia gravis: baseline results of the international prospective, observational, longitudinal real-world digital study MyRealWorld-MG.

Abstract:

OBJECTIVES: Myasthenia gravis (MG) is a rare, chronic, autoimmune neuromuscular disease which can affect functional and mental aspects of health and health-related quality of life (HRQoL). This study aims to obtain detailed knowledge of the impact of MG on HRQoL in a broad population from the perspective of the patient. DESIGN: Prospective, observational, digital, longitudinal real-world study. SETTING: Adult patients with MG from seven countries (USA, Japan, Germany, UK, Italy, Spain and Canada) downloaded a mobile application onto their phones and entered data about themselves and their MG. OUTCOME MEASURES: Data was collected using the following general and disease-specific patient-reported outcome measurements: EuroQol 5 Domains Health-Related Quality of Life Questionnaire (EQ-5D-5L), Myasthenia Gravis Activities of Daily Living (MG-ADL), Myasthenia Gravis Quality of Life 15-item revised scale (MG-QoL-15r), Hospital Anxiety and Depression Scale (HADS) and Health Utilities Index III (HUI3). Patients were categorised by their self-assessed Myasthenia Gravis Foundation of America (MGFA) class (I-V). RESULTS: Baseline results of 841 participants (mean age 47 years, 70% women) are reported . The distribution across the MGFA classes was: 13.9%, 31.0%, 38.1%, 15.5% and 1.6% for classes I-V. The MGFA class was a strong predictor of all aspects of HRQoL, measured with disease-specific and with generic instruments. The domains in which patients with MG most frequently mentioned problems were usual activities, anxiety and depression, tiredness, breathing and vision. The mean total MG-ADL Score was positively associated with increasing MGFA classes: 2.7, 4.4, 6.3 and 8.4 for MGFA classes I-IV. Mean baseline EQ-5D-5L utility was also associated with MGFA classes and was 0.817, 0.766, 0.648 and 0.530 for MGFA class I-IV. CONCLUSIONS: MG has a large impact on key aspects of health and HRQoL. The impact of this disease increases substantially with increasing disease severity.

## P1dd2f4d52020

- Year: 2023
- Linked people: Sayem Ahmed
- Title: Conducting epidemiological studies on snakebite in nomadic populations: A methodological paper

Abstract:

INTRODUCTION: Research on snakebite has mostly been conducted on settled populations and current risk factors and potential interventions are therefore most suited for these populations. There is limited epidemiological data on mobile and nomadic populations, who may have a higher risk of snakebite. METHODS AND RESULTS: We conducted a scoping review to gather evidence on survey methods used in nomadic populations and compared them with contemporary survey methods used for snakebite research. Only 16 (10.5%) of 154 articles reportedly conducted on pastoralist nomadic populations actually involved mobile pastoralists. All articles describing snakebite surveys (n = 18) used multistage cluster designs on population census sampling frames, which would not be appropriate for nomadic populations. We used geospatial techniques and open-source high-resolution satellite images to create a digital sampling frame of 50,707 households and used a multistage sampling strategy to survey nomadic and semi-nomadic populations in Samburu County, Kenya. From a sample of 900 geo-located households, we correctly identified and collected data from 573 (65.4%) households, of which 409 were in their original locations and 164 had moved within 5km of their original locations. We randomly sampled 302 (34.6%) households to replace completely abandoned and untraceable households. CONCLUSION: Highly mobile populations require specific considerations in selecting or creating sampling frames and sampling units for epidemiological research. Snakebite risk has a strong spatial component and using census-based sampling frames would be inappropriate in nomadic populations. We propose using open-source satellite imaging and geographic information systems to improve the conduct of epidemiological research in these populations.

## Pde03d4b16ce8

- Year: 2024
- Linked people: Fernando Argento
- Title: Safety and Effectiveness of COVID-19 Vaccines During Pregnancy: A Living Systematic Review and Meta-analysis

Abstract:

BACKGROUND: Pregnant persons are susceptible to significant complications following COVID-19, even death. However, worldwide COVID-19 vaccination coverage during pregnancy remains suboptimal. OBJECTIVE: This study assessed the safety and effectiveness of COVID-19 vaccines administered to pregnant persons and shared this evidence via an interactive online website. METHODS: We followed Cochrane methods to conduct this living systematic review. We included studies assessing the effects of COVID-19 vaccines in pregnant persons. We conducted searches every other week for studies until October 2023, without restrictions on language or publication status, in ten databases, guidelines, preprint servers, and COVID-19 websites. The reference lists of eligible studies were hand searched to identify additional relevant studies. Pairs of review authors independently selected eligible studies using the web-based software COVIDENCE. Data extraction and risk of bias assessment were performed independently by pairs of authors. Disagreements were resolved by consensus. We performed random-effects meta-analyses of adjusted relative effects for relevant confounders of comparative studies and proportional meta-analyses to summarize frequencies from one-sample studies using R statistical software. We present the GRADE certainty of evidence from comparative studies. Findings are available on an interactive living systematic review webpage, including an updated evidence map and real-time meta-analyses customizable by subgroups and filters. RESULTS: We included 177 studies involving 638,791 participants from 41 countries. Among the 11 types of COVID-19 vaccines identified, the most frequently used platforms were mRNA (154 studies), viral vector (51), and inactivated virus vaccines (17). Low to very low-certainty evidence suggests that vaccination may result in minimal to no important differences compared to no vaccination in all assessed maternal and infant safety outcomes from 26 fewer to 17 more events per 1000 pregnant persons, and 13 fewer to 9 more events per 1000 neonates, respectively. We found statistically significant reductions in emergency cesarean deliveries (9%) with mRNA vaccines, and in stillbirth (75-83%) with mRNA/viral vector vaccines. Low to very low-certainty evidence suggests that vaccination during pregnancy with mRNA vaccines may reduce severe cases or hospitalizations in pregnant persons with COVID-19 (72%; 95% confidence interval [CI] 42-86), symptomatic COVID-19 (78%; 95% CI 21-94), and virologically confirmed SARS-CoV-2 infection (82%; 95% CI 39-95). Reductions were lower with other vaccine types and during Omicron variant dominance than Alpha and Delta dominance. Infants also presented with fewer severe cases or hospitalizations due to COVID-19 and laboratory-confirmed SARS-CoV-2 infection (64%; 95% CI 37-80 and 66%; 95% CI 37-81, respectively). CONCLUSIONS: We found a large body of evidence supporting the safety and effectiveness of COVID-19 vaccines during pregnancy. While the certainty of evidence is not high, it stands as the most reliable option available, given the current absence of pregnant individuals in clinical trials. Results are shared in near real time in an accessible and interactive format for scientists, decision makers, clinicians, and the general public. This living systematic review highlights the relevance of continuous vaccine safety and effectiveness monitoring, particularly in at-risk populations for COVID-19 impact such as pregnant persons, during the introduction of new vaccines. CLINICAL TRIAL REGISTRATION: PROSPERO: CRD42021281290.

## P169bf51d6948

- Year: 2024
- Linked people: Julie Ratcliffe, Nancy Devlin, Richard Norman, Rosalie Viney, Tessa Peasgood
- Title: Systematic Review of the Relative Social Value of Child and Adult Health.

Abstract:

OBJECTIVES: We aimed to synthesise knowledge on the relative social value of child and adult health. METHODS: Quantitative and qualitative studies that evaluated the willingness of the public to prioritise treatments for children over adults were included. A search to September 2023 was undertaken. Completeness of reporting was assessed using a checklist derived from Johnston et al. Findings were tabulated by study type (matching/person trade-off, discrete choice experiment, willingness to pay, opinion survey or qualitative). Evidence in favour of children was considered in total, by length or quality of life, methodology and respondent characteristics. RESULTS: Eighty-eight studies were included; willingness to pay (n = 9), matching/person trade-off (n = 12), discrete choice experiments (n = 29), opinion surveys (n = 22) and qualitative (n = 16), with one study simultaneously included as an opinion survey. From 88 studies, 81 results could be ascertained. Across all studies irrespective of method or other characteristics, 42 findings supported prioritising children, while 12 provided evidence favouring adults in preference to children. The remainder supported equal prioritisation or found diverse or unclear views. Of those studies considering prioritisation within the under 18 years of age group, nine findings favoured older children over younger children (including for life saving interventions), six favoured younger children and five found diverse views. CONCLUSIONS: The balance of evidence suggests the general public favours prioritising children over adults, but this view was not found across all studies. There are research gaps in understanding the public's views on the value of health gains to very young children and the motivation behind the public's views on the value of child relative to adult health gains. CLINICAL TRIAL REGISTRATION: The review is registered at PROSPERO number: CRD42021244593. There were two amendments to the protocol: (1) some additional search terms were added to the search strategy prior to screening to ensure coverage and (2) a more formal quality assessment was added to the process at the data extraction stage. This assessment had not been identified at the protocol writing stage.

## Pd61d9e6b3dce

- Year: 2026
- Linked people: Piyameth Dilokthornsakul
- Title: Budget Impact of Secukinumab in Psoriatic Arthritis Patients with Contraindication to TNF-Alpha Inhibitors.

Abstract:

Background: Secukinumab, an IL-17A inhibitor, has been recommended for psoriatic arthritis (PsA) patients with contraindications to TNF-alpha inhibitors (TNFi). However, its budgetary implications in Thailand remain unclear. Objective: To estimate the 5-year budget impact of introducing secukinumab 150 mg for PsA patients contraindicated to TNFi therapy from the perspective of the Thai healthcare system. Methods: A budget impact analysis (BIA) was developed following the Thai HTA Guideline. Two treatment scenarios were compared: the current standard of care using csDMARDs and a new scenario incorporating secukinumab 150 mg (auto-injector). The model estimated eligible patients based on national demographics and clinical data. Costs included direct medical costs for medications, administration, monitoring, and complications. Net budget impact (NBI) was estimated. Deterministic sensitivity analyses were conducted to evaluate the impact of varying uptake rates and treatment durations. Results: Under the base-case scenario over five years, secukinumab use resulted in the NBI of 15.14 million THB (434,965 USD), with an average annual net budget impact of 3.03 million THB (86,993 USD). Drug acquisition accounted for 97.16% of the total budget impact. Sensitivity analyses revealed a higher financial burden with increased uptake or lifetime treatment but remained within a manageable range (up to 18.34 million THB or 526,849 USD). Conclusion: Introducing secukinumab for PsA patients contraindicated to TNFi is associated with a moderate increase in healthcare expenditure. These findings suggest that inclusion of secukinumab in the National List of Essential Medicines for this specific population may be feasible, conditional on successful price negotiation and/or managed entry arrangements to ensure budgetary sustainability and equitable access. Plain Language Summary: This study evaluated the 5-year budget impact of introducing secukinumab, an interleukin-17A inhibitor, for psoriatic arthritis (PsA) patients contraindicated to TNF-alpha inhibitors (TNFi) in Thailand. A budget impact analysis was developed in accordance with the Thai Health Technology Assessment (HTA) Guideline, comparing the current standard of care with conventional DMARDs (csDMARDs) against a new scenario incorporating secukinumab 150 mg (auto-injector). Eligible patient numbers were estimated using national demographic and clinical data, while direct medical costs included medications, administration, monitoring, and treatment of complications. Results showed that introducing secukinumab led to a net budget impact (NBI) of 15.14 million THB (434,965 USD) over five years, averaging 3.03 million THB (86,993 USD) annually. Drug acquisition accounted for 97% of the increased expenditure. Sensitivity analyses indicated that higher uptake rates or lifetime treatment duration moderately increased costs but remained within a manageable range (up to 18.34 million THB or 526,849 USD). The findings suggest that while secukinumab adoption modestly increases healthcare costs, it provides a valuable therapeutic alternative for PsA patients who cannot use TNFi. Policy implications include supporting its inclusion in Thailand’s National List of Essential Medicines with price negotiation strategies to ensure affordability and access. Keywords: psoriatic arthritis, secukinumab, TNF-alpha inhibitor, budget impact analysis, Thailand, pharmacoeconomics, health technology assessment

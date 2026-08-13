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

## P8a2908082f99

- Year: 2025
- Linked people: Aki Tsuchiya
- Title: Equality of opportunity and the intergenerational transmission of lifestyles: some normative implications

Abstract:

Abstract The Equality of Opportunity framework assumes that a given distribution of outcomes is a function of factors for which the individuals should be held accountable (referred to as effort) and factors that are beyond the individuals’ responsibility (referred to as circumstances). Circumstances can influence effort by shaping: i) the return to effort (interaction effect) or ii) the distribution of effort (indirect effect). The theoretical literature has mainly focused on the former. This study explores different allocation strategies to mitigate health inequalities due to the unfair indirect effects of circumstances and their alignment with principles of fair allocation. A questionnaire-experimental study is conducted, adapting these concepts to explore public attitudes toward health inequalities resulting from the intergenerational transmission of smoking habits.

## P008d40a1acd0

- Year: 2025
- Linked people: Maureen Rutten-van Molken
- Title: Preparing for the EU HTA Regulation: Insights from the Dutch Perspective.

Abstract:

The European Health Technology Assessment (HTA) regulation (HTAR) came into effect in January 2025 and impacts the HTA process in all European Member States. Member States must give due consideration to the joint clinical assessment (JCA) report. This may require adaptations at the national level. This paper describes the anticipated changes to the Dutch national HTA process and how the Dutch National Health Care Institute (Zorginstituut Nederland, ZIN) prepared for this, because sharing experience between Member States can be of general interest for future expansion of the EU HTAR. ZIN's implementation activities were facilitated by a project-governance structure and by a continuous gap analysis of the current national assessment and appraisal process of medicinal products, resulting in a concrete action plan. The implementation of the HTAR has two major implications for ZIN's HTA process, namely that the scoping phase starts much earlier and that the JCA report is the starting point for the national assessment. Gaps, challenges and issues were identified in the categories: information and knowledge, IT and template, communication and stakeholder engagement, capacity and resources, and financial aspects. Based on a thorough and well-defined implementation plan, ZIN is ready to implement the HTAR in national HTA processes and to take on (co-)assessor roles for JCA of medicinal products in 2025.

## Pc104991b8d09

- Year: 2025
- Linked people: María Belizán
- Title: Acceptability and perceived barriers to adoption of the core outcome set for maternal and neonatal health research and surveillance during emerging and ongoing epidemic threats (MNH-EPI-COS). An online survey

Abstract:

The Maternal and Newborn Health Core Outcome Set during Epidemics (MNH-EPI-COS) is a standardized set of outcomes developed to harmonize outcome selection in maternal and neonatal health research conducted during outbreaks and epidemics. It was developed through a four-stage modified Delphi process involving a large group of international stakeholders who assessed outcomes relevance through online surveys, followed by consensus meetings with a subgroup of stakeholders to finalize the COS. The objective of this study is to evaluate the acceptability of the full MNH-EPI-COS among key stakeholders who participated in the first two round of the Delphi process, to identify anticipated barriers to its adoption, and to assess agreement on the inclusion of individual outcomes, their definitions, and the perceived feasibility of data collection. An online consultation was conducted using an electronic semi-structured survey targeting senior clinical and public health experts and civil society representatives who had contributed to earlier phases of MNH-EPI-COS development but did not participate in the final consensus meetings. Of the 118 invited stakeholders, 100 completed the survey. The majority (95%) agreed that the MNH-EPI-COS captures the most important outcomes, is likely acceptable to key stakeholders (94%), and facilitates timely evidence generation (92%). Additionally, 75% expressed intent to use it. Over 80% of participants agreed with the individual outcomes and their definitions, except for "skin-to-skin contact" and "breastfeeding," which were acceptable to 67% and 74%, respectively. Concerns were raised about the feasibility of measuring specific outcomes across diverse settings due to the substantial effort and resources required. Key barriers to adoption include knowledge, skills, and understanding gaps and the lack of practical resources. The MNH-EPI-COS, including its outcomes and definitions, was highly acceptable to the larger group of stakeholders involved in the early stages of its development. However, feasibility concerns remain. Successful implementation will require effective dissemination, targeted training, data collection resources, and real-world evaluation.

## P0bb73be96421

- Year: 2024
- Linked people: Matthijs Versteegh
- Title: The Cost-Effectiveness of Seizure Dogs for Persons Living With Severe Refractory Epilepsy: Results From the EPISODE Study

Abstract:

OBJECTIVES: The Epilepsy Support Dog Evaluation study was commissioned by the Dutch Ministry of Health, Welfare and Sports to inform a reimbursement decision on seizure dogs. The randomized trial found that seizure dogs reduce seizure frequency and improve health-related quality of life of persons with severe refractory epilepsy (PSREs). This article examined the cost-effectiveness (CE) of adding seizure dogs to usual care for PSREs in The Netherlands. METHODS: A microsimulation model was developed, informed by generalized linear mixed models using patient-level trial data from the Epilepsy Support Dog Evaluation study. The model adopted a 10-year time horizon and took a societal perspective. Seizure frequency was predicted as a function of time with the seizure dog. Patient utilities, caregiver utilities, and costs were predicted as a function of seizure frequency and time with the seizure dog. RESULTS: Quality-adjusted life-years (QALYs) of PSREs with a seizure dog and usual care alone were estimated at 6.28 and 5.65, respectively (Δ 0.63). For caregivers, estimated QALYs were 6.94 and 6.52, respectively (Δ 0.42). Total costs were respectively €228 691 and €226 261 (Δ €2430). Intervention costs were largely offset by savings in informal care and healthcare. The incremental CE ratio was €2314/QALY. Probabilistic sensitivity analysis indicated a 91% probability of seizure dogs being cost-effective at the €50 000/QALY threshold. The incremental CE ratio fell well below this threshold in scenario analyses. CONCLUSIONS: Seizure dogs are likely to be a cost-effective addition to usual care for PSREs in The Netherlands.

## P4fa63c527cad

- Year: 2025
- Linked people: Mina Bahrampour
- Title: Impoverishing Health Expenditure in Iran Before and After the COVID-19 Pandemic: A National Cross-sectional Study

Abstract:

Background: The COVID-19 pandemic has altered healthcare service utilization patterns and, consequently, the financial protection indicators. Objectives: This study aims to examine the impoverishment caused by health expenditures before and during the COVID-19 pandemic in Iran. Methods: This retrospective-descriptive study was conducted using six years of national income and expenditure data (2016 - 2021) from 228,910 households. We measured the occurrence and intensity indices of impoverishing health expenditure, such as the poverty headcount (PH), normalized poverty gap (NPG), and normalized mean positive poverty gap (NMPG), at the rural and urban levels separately. Results: The PH increased from 2016 to 2018, decreased in 2019, and rose again in 2020 and 2021. Moreover, the occurrence of impoverishment health expenditure was at its lowest level in 2016 compared to previous years. PH was consistently higher in rural areas. NPG increased from 2016 to 2018, decreased in 2019, and increased again in 2020 and 2021. The NMPG index ranged from 0.11% to 0.62% in rural areas, and from 0.34% to 1.18% in urban areas. Conclusion: Impoverishing health expenditure in Iran was significant, especially for rural residents. The COVID-19 pandemic did not change this trend. Reforming economic policies and providing targeted financial support for vulnerable populations are crucial.

## P0255202c8797

- Year: 2024
- Linked people: Ciaran O'Neill
- Title: An investigation into patterns of Alcohol drinking in Scotland after the introduction of minimum unit pricing

Abstract:

BACKGROUND: In 2018, Scotland became the second country to implement minimum unit pricing (MUP) for all types of alcoholic beverages. The aim of this study was to examine the effect of the policy. METHOD: Three national household-level surveys were used: Scottish Health Surveys (2008-2021), Health Surveys in England (2011-2019), and Northern Ireland Continuous Household Survey (2011-2015). First, a generalized ordered logistic model examined patterns of drinking solely in Scotland from 2008-2021 covering current drinking, drinking categories and the weekly consumption (in alcohol units). Secondly, difference-in-difference (DID) analysis was employed to examine changes in "social drinking" behaviours in Scotland after the announcement in 2012 (2011-2015, Northern Ireland and England as comparators) and after the adoption of the policy in 2018 (England as a comparator, with two timeframes 2016-2019 and 2013-2019). RESULTS: Overall, drinking in Scotland began to decline prior to 2012 and dropped further with the enactment of MUP in 2018. In response to MUP, the likelihood of abstention increased along with a slight decrease in the prevalence of heavy drinking. The overall amount of drinking fell by about 8% after 2012 and 12% after 2018 (as compared to 2008-2011 level), with a significant decline seen in moderate drinkers but not of those who drank at hazardous or harmful levels. The DID analyses confirmed the reduction in current drinking in Scotland starting since 2012 and continued post-MUP in 2018. CONCLUSION: This study points to the impact of MUP in Scotland with a potential role for 'policy signalling' by the Scottish Government's with a multiple-buy discount ban and MUP's announcement since 2011-2012. Indications of impact include a clear decline in alcohol consumption levels and a small but noteworthy change in prevalence of overall drinking and heavy drinking.

## Ped8da1e938e5

- Year: 2025
- Linked people: Martin Härter
- Title: Efficacy of Psychodynamic Psychotherapy in Serious Physical Illness: Systematic Review and Meta‐Analysis

Abstract:

Objective Prevalence rates of depression and anxiety in patients with a serious physical illness are high. Psychodynamic psychotherapies show potential in mitigating such psychological distress because they address hindering relational experiences and unconscious conflicts that may impair patients’ capacity to cope with illness‐related distress. We investigated the efficacy of psychodynamic psychotherapy for symptoms of depression and anxiety in patients with serious physical illness. Methods We conducted a systematic literature search to identify randomized controlled trials and quasi‐experiments of psychodynamic psychotherapies in adults with serious physical illness. We conducted random‐effects meta‐analyses and narrative summaries. Results We identified 15,112 records and included 5 RCTs ( n = 648, mean age: 52.4 years, 69% female). Meta‐analyses showed no significant differences between psychodynamic and standard treatment for the reduction of depressive symptoms in serious physical illness (SMD = −0.24, 95% CI: −0.87 to 0.39). No meta‐analysis was calculated for anxiety symptoms due to the small number of studies investigating this outcome. Conclusion Quantitative evidence for the efficacy of psychodynamic psychotherapy in this population is inconclusive. More research is needed with regard to effective intervention length and adequate outcome measures, especially in patients with incurable illness.

## P02438f1ef16f

- Year: 2024
- Linked people: Carlos Wong
- Title: Comparison of Bivalent and Monovalent mRNA Vaccine Boosters.

Abstract:

In this cohort study conducted in Hong Kong where both bivalent and monovalent formulations of BNT162b2 were available, there were no significant differences in the mortality or hospitalization between those who received bivalent and monovalent mRNA as second boosters. Bivalent and monovalent mRNA boosters appear equally protective against clinical outcomes.

## P2cecfd5365b4

- Year: 2025
- Linked people: Fredrick Purba
- Title: Determinants of Middle and High School Teachers' Well-Being: A Systematic Review.

Abstract:

Purpose: In this review, the determinant of teachers' well-being in middle and high school teachers and to identify potential avenues for future investigation was evaluated. Patients and Methods: The systematic review of this study was conducted using the Preferred Reporting Items for System Reviews and Meta-Analysis (PRISMA) methodology. We looked through a range of scholarly research on teachers' well-being that had been published in English and included in Scopus, EBSCO host, Science Direct, and Springer Link. There were 465 publications found throughout the literature search. The final analysis contained 12 publications after duplicates were eliminated and titles, abstracts, and full texts were screened. Articles unrelated to the topic and did not concentrate on TWB in middle and high school were excluded. The findings were checked and verified. A risk-of-bias assessment tool designed for systematic reviews of mixed research (ie, reviews that combine qualitative, quantitative, and/or mixed methods studies) was the Mixed Methods Appraisal Tool (MMAT). Results: There were fourth determinants of middle and high school TWB. The most powerful determinants were physical health, mental and emotional health, social support, professional development and autonomy. Meanwhile, the areas that required further investigation included TWB intervention programs, influential cultural and social factors, research methodology, and measurement procedures. Conclusion: Key determinants of teacher well-being (TWB) in middle and high school, such as physical and mental health, social support, professional development and autonomy, suggest several clinical applications. Targeted mental health resources, wellness initiatives, and strong support networks could significantly enhance TWB. Additionally, empowering teachers through skill development and autonomy may improve their job satisfaction and reduce burnout. Future intervention should consider cultural and social nuances to maximize TWB support.

## Pbef6e623447a

- Year: 2026
- Linked people: Oriana Ciani
- Title: Methods for Evaluation of Surrogate Endpoints for HTA Decision Making: A Good Practices Report of an ISPOR Task Force

Abstract:

Surrogate endpoints are frequently used as primary outcomes in clinical trials. This is appropriate when they are validated for their ability to predict clinical benefit measured on patient-relevant target outcome(s). Such validation is often lacking, thus increasing uncertainty in the decision-making process of regulatory bodies, health technology assessment agencies and payers. This ISPOR Task Force Report provides recommendations on best practices for surrogate endpoint evaluation for health technology assessment decision making. It covers methods that address the 3 levels of evidence for surrogate endpoint validation described in several methodological guidelines: (1) association between treatment effects on the surrogate and the target outcome, (2) association between the surrogate and the target outcome, and (3) biological plausibility. Statistical methods for surrogate endpoint evaluation include meta-analytic approaches using individual participant data or aggregate data. Multivariate meta-analytic models are recommended because they account for the within-study correlation and estimation errors. Issues with limited data and generalizability might be addressed through Bayesian approaches for information sharing from different treatments, treatment classes or indications. Real-world data can complement randomized controlled trial data, especially in rare diseases, but require careful consideration of underlying bias. For plausibility of health economic modeling, the surrogacy analysis and the health economic model should be aligned. The modeled time course of surrogate and target outcomes per treatment arm, as well as the modeled relative effects, should be reported to assess plausibility. Parameter and structural uncertainty in surrogate relationships can be explored through scenario analyses, probabilistic sensitivity analyses, value of information analyses, and threshold analysis techniques.

## P29fa78335431

- Year: 2025
- Linked people: Shankar Prinja
- Title: Comprehensive primary health care for cost-effective scale-up of depression screening in India: an economic modelling study

Abstract:

Background: The Government of India envisions integrating population-based depression screening within the framework of comprehensive primary health care. This study assesses the economic impact and cost-utility of implementing universal depression screening for different age groups (≥30 years and ≥20 years) compared to the current practice of opportunistic diagnosis and management of symptomatic patients. Methods: A hybrid model comprising of a decision tree and Markov model was developed for economic evaluation. The input parameters were acquired through comprehensive literature search, stakeholder consultations, analysis of the data from National Mental Health Survey, and the National Sample Survey, besides primary data collected from 259 patients for quality of life. The analysis was performed from both abridged societal (consideration of direct costs) and societal perspective (consideration of direct as well as indirect costs). In line with Indian economic evaluation standards, a screening strategy was deemed cost-effective if its incremental cost-utility ratio (ICUR) was below the per capita gross domestic product (GDP) threshold of ₹1,71,498 ($2182). Findings: The gain in QALYs per person from universal screening ranged from 0·0273 (0·0265-0·0281) to 0·0295 (0·0287-0·0303), depending on the target age group. The program is expected to generate net savings of ₹291 billion ($3·7 billion) to ₹482 billion ($6·1 billion), equivalent to 0·19% to 0·32% of GDP. Furthermore, the ICURs were below the threshold, with ≥20 years aged cohort screening (₹43,995, $620) being more cost-effective than the screening in ≥30 years aged population (₹48,746, $560) from the abridged societal perspective. However, the program ceases to yield positive net health benefits if the sensitivity of the PHQ-2 decreases to 26%, or if the combined sensitivity of the sequential PHQ-2 and PHQ-9 approach falls below 35%. The intervention is likely to result in cost savings if at least 60% of patients seeking treatment after screening use public health facilities. Interpretation: Integrating depression screening and management into the government primary healthcare system provides substantial public health and economic benefits, supporting the case for a PHC-oriented health system. Expanding coverage to individuals aged 20 years and above, along with ensuring high diagnostic accuracy through quality training and supportive supervision, will be key to sustaining and maximizing the programme's impact. Funding: The study was supported by funding from the Department of Health Research, Ministry of Health and Family Welfare, Government of India.

## P46ef5634c035

- Year: 2025
- Linked people: Maja Kuharic
- Title: Web-Based Cancer Symptom Self-Management System

Abstract:

Importance: Patients with cancer and cancer survivors frequently experience symptoms that increase the need for health care services and impair quality of life. Effective symptom management is critical for comprehensive patient-centered cancer care. Objective: To evaluate the effectiveness of adding a bilingual (English and Spanish), web-based self-management program to an electronic health record (EHR)-integrated patient-reported outcome for cancer (cPRO) assessment in reducing symptom burden and health care resource use (HCRU). Design, Setting, and Participants: This patient-level randomized clinical trial was performed at the Northwestern Memorial HealthCare system in Chicago, Illinois. Participants included 1614 adult patients with cancer or cancer survivors in 30 clinics who were enrolled between April 1, 2020, and April 8, 2023, and followed up for 12 months until May 8, 2024. Interventions: Usual care (UC) consisting of an EHR-integrated cPRO assessment or enhanced care (EC), which offered an additional tailored web-based self-management program. Main Outcomes and Measures: Patient-Reported Outcomes Measurement Information System measures of anxiety, depression, fatigue, pain interference, and physical function collected at baseline and monthly for 12 months. Secondary outcomes included HCRU measures (inpatient and/or observation visits and days, emergency department and/or urgent care visits, and days of hospital stay). Results: A total of 1614 patients were included in the analysis, with 804 randomized to EC and 810 to UC. The mean (SD) age was 61 (13) years; 1095 patients (67.8%) were female. Only 419 EC participants (52.1%) accessed the website, with only 197 (47%) returning; the median time per visit was 45 seconds (IQR, 45-105 seconds). There were no statistically significant differences between EC and UC across the cPRO outcomes over 12 months. The mean change from baseline at each assessment time point for treatment effects (EC vs UC) ranged from -0.19 (95% CI, -0.86 to 0.33; P = .64) for physical function to 0.11 (95% CI, -0.75 to 0.79; P = .87) for fatigue. Zero-inflated negative binomial and logistic regression models showed no significant differences in HCRU outcomes: inpatient and/or observation visits (incidence rate ratio [IRR], 0.90; 95% CI, 0.72-1.12), emergency department and/or urgent care visits (IRR, 0.99; 95% CI, 0.84-1.16), and days of hospital stay (IRR, 1.05; 95% CI, 0.83-1.33). Conclusions and Relevance: In this randomized clinical trial, adding a bilingual web-based self-management program to EHR-integrated cPRO did not reduce symptom burden or HCRU compared with cPRO alone. Low engagement with the web-based program highlights the need for strategies to enhance engagement and tailor interventions to those who would benefit most. Trial Registration: ClinicalTrials.gov Identifier: NCT03988543.

## Pe8a33f1b5e19

- Year: 2025
- Linked people: David Whitehurst
- Title: Did a digital quality of life (QOL) assessment and practice support system in home health care improve the QOL of older adults living with life-limiting conditions and of their family caregivers? A mixed-methods pragmatic randomized controlled trial

Abstract:

We aimed to improve the quality of life (QOL) of homecare patients (≥ 55 years of age) who had chronic life-limiting conditions and that of their family caregivers by making QOL assessment data available via a digital QOL and practice support system (QPSS). We hypothesized that access to QPSS data in home health care would result in improved QOL for patients or their family caregivers. We further sought to understand how to integrate the use of QOL information into home health care. Our mixed-methods study, including a pragmatic randomized controlled trial (PrCT; registered at ClinicalTrials.gov #NCT02940951), was conducted with nine home healthcare teams in Canadian urban areas. The qualitative research included focus groups and interviews with home healthcare teams (N = 118) to determine how to integrate the QPSS into their practice. Participating homecare patients were assigned to an intervention group (N = 166), where home healthcare teams had access to patients' and their family caregivers' QOL data via the QPSS, or a usual care group (N = 165). Where possible, one family caregiver per patient was recruited (intervention N = 62; usual care N = 51). Primary outcomes, measured every two months for one year, were patients' and family caregivers' QOL trajectories. Longitudinal structural equation models were used to compare the trajectories. The home healthcare teams preferred to have QOL scores presented as tables and graphs, with family caregivers' data linked to each patient. Despite the enthusiasm expressed by the home healthcare teams, and efforts to satisfy their preferences, they infrequently accessed the QOL information. While we observed substantial individual-level variability in patients' and family caregivers' QOL trajectories, the average trajectories for the PrCT groups were similar. Making QOL assessment data available via a digital platform may not be sufficient to achieve measurable improvements for patients and family caregivers.

## P53d0dd9db9a1

- Year: 2025
- Linked people: Irina Kinchin
- Title: From Fragmentation to Reform: Mapping the Lived Experience of Lewy Body Dementia Care in Ireland

Abstract:

Abstract Background Lewy Body Dementia (LBD) is the second most common form of dementia, yet it remains under-recognised and under-diagnosed, particularly in Ireland, where no national clinical guidelines or care pathways exist. This study represents the first comprehensive exploration of LBD diagnostic and post-diagnostic pathways in Ireland, drawing on the lived experiences of LBD patients, care partners, and healthcare professionals (HCPs) to identify systemic gaps and opportunities for reform. Methods A qualitative interpretive phenomenological approach was employed to conduct semi-structured interviews with 12 LBD patients, 17 care partners, and 23 healthcare professionals, from both urban and rural areas, across various disciplines, including neurology, psychiatry, geriatric medicine, nursing, allied health, and general practice. Thematic analysis was conducted using Colaizzi’s method, with a focus on diagnosis, post-diagnostic support, and service navigation. Results Five key themes emerged: (1) Recognition and Diagnosis – delays, misdiagnoses, and unclear referral routes were prevalent; (2) Systemic Fragmentation and Informal Anchors – families often coordinated care in the absence of structured support; (3) Emotional and Practical Burden of Care – care partners reported significant exhaustion, isolation, and financial strain; (4) Inequitable Access and Training Gaps – rural, young-onset, and under-65 cases faced substantial access barriers, compounded by inconsistent LBD-specific training; and (5) Call for Awareness and Structural Change – participants emphasised the need for standardised care pathways, specialist roles, and integrated, age-inclusive services. Conclusion This study highlights the distinct challenges faced by LBD patients and their care partners in Ireland, underscoring the need for systemic reform to address inequities in diagnosis and care. It highlights the critical importance of LBD-specific training for healthcare professionals, developing coordinated care models, and implementing policy changes to better support patients and frontline professionals. By centering the lived experiences of patients and care partners, these findings provide a foundation for the design of more inclusive, responsive, and person-centered dementia services in Ireland.

## P4500da701a6f

- Year: 2025
- Linked people: Erwin Birnie
- Title: Cosmetic outcome and patient satisfaction following percutaneous thermal ablation of early-stage breast cancer; results of an open label randomized phase 2 trial

Abstract:

Purpose The aim of the present study is to assess patient reported cosmetic outcome and satisfaction following percutaneous thermal ablation and subsequent breast-conserving surgery. Methods Cosmetic outcome and patient satisfaction were assessed in postmenopausal women diagnosed with unilateral invasive cT1N0M0 breast cancer who participated in a randomized phase 2 treat-and-resect trial comparing the efficacy of radiofrequency ablation (RFA), microwave ablation (MWA) and cryoablation (CA). Cosmetic outcome was measured subjectively with the BCTOS-13 and the Beast-Q questionnaires (0-100 score), and objectively with BCCT.core software at baseline, after thermal ablation and after surgery. Patient satisfaction was defined as satisfaction with the technique (4 point scale), recommendation of the technique to others (yes/no), and the preference for surgery of thermal ablation after completion of both treatments. Results Forty-one patients were included in the study. The overall median cosmetic outcome was good after thermal ablation, and intermediate after surgery (1.6 vs 1.8; P = 0.07). Most domains of the BREAST-Q were scored higher after thermal ablation, 95 % of patients were very satisfied or satisfied with the technique, and 91 % would prefer thermal ablation over surgery. Differences between the different techniques were limited On the BCCT.core, 94 % of cases were rated as good or excellent after thermal ablation, compared to 80 % after surgery. Conclusion The present study demonstrates that patient reported and objectivated cosmetic outcomes are good both after thermal ablation and breast-conserving surgery. Patient satisfaction was outstanding following thermal ablation, with a preference for thermal ablation observed in a group of patients who underwent both treatment options.

## P6ed5991396e4

- Year: 2025
- Linked people: Julie Ratcliffe
- Title: Process Evaluation of a Dementia Prevention Program for Aboriginal Australians (DAMPAA) Using a Theory of Change Framework

Abstract:

A co-designed, Aboriginal health practitioner-led dementia risk management program (DAMPAA) was implemented from 2021 to 2024 to address the growing concern of dementia among Aboriginal and Torres Strait Islander peoples in Western Australia. Key features of DAMPAA included group walking and yarning sessions incorporating health and well-being education twice a week, alongside a six-month home program. A theory of change framework guided a parallel process evaluation, co-developed with Aboriginal Community-Controlled Health Services and an Elders Governance Group. The evaluation involved two distinct groups: Elders who participated in the program and staff involved in its design and delivery. Qualitative data were collected through yarning interviews, focusing on the program's implementation and impact. A brain health program for Elders was highly valued. Through group walking and yarning, the program supported a deeper connection to Country and strengthened community connection enhancing social and emotional well-being for Elders as well as program staff. A key learning was the significance of an Elders-informed health program, delivered by local Aboriginal people at an Aboriginal Community Controlled Health Service, creating a space that strengthens connection and a sense of belonging for Elders. The process evaluation validated the importance of the DAMPAA program. The DAMPAA program and resources have since been integrated into Elders' health programs across all service partners, demonstrating its relevance and potential for broader application.

## Pfc0faf9453e2

- Year: 2026
- Linked people: Joshua Bonsel, Juanita Haagsma, You-Shan Feng
- Title: Socioeconomic inequalities in health-related quality of life during the COVID-19 pandemic: a six-country comparison using the EQ-5D-5 L.

Abstract:

PURPOSE: Despite the growing attention to health inequalities, there is no global consensus on how to measure socio-economic status. This study examined inequalities in health-related quality of life (HRQoL) during the early phase of the COVID-19 pandemic across six countries-China, Italy, the Netherlands, Sweden, the United Kingdom (UK), and the United States (US)-using three SES indicators: education level, income, and work status. METHODS: Between April and June 2020, individuals aged 18-75 years old completed a web-based survey. HRQoL was measured using the EQ-5D-5L Level Sum Score (LSS), where higher scores indicate poorer health. Country-specific differences in LSS across SES groups were assessed using Kruskal-Wallis and Mann-Whitney U tests. Multiple linear regression models, adjusted for age, gender, and chronic conditions, were used to explore associations between SES indicators and HRQoL. No formal correction for multiple testing was applied. RESULTS: Data from 17,607 respondents were analyzed. In all countries except Italy, individuals with lower education levels reported significantly higher LSS scores. The largest disparity was observed in the UK. In the Netherlands, Sweden, the UK, and the US, lower-income groups also had higher LSS scores, while no such differences were observed in China or Italy. Across all countries, unemployed individuals consistently reported worse HRQoL. Regression analyses confirmed that younger age, chronic conditions, and unemployment were strongly associated with poorer HRQoL. CONCLUSIONS: Substantial SES-related health inequalities in HRQoL were observed during the COVID-19 pandemic, especially in the UK. Work status emerged as a particularly strong and consistent predictor across countries.

## P844a23f9b837

- Year: 2026
- Linked people: Janine van Til
- Title: Comprehension of and preferences for visualization of patient-reported outcome data to support clinical decision making: A systematic review

Abstract:

OBJECTIVES: As Patient-Reported Outcome Measures (PROMs) become integrated into clinical care, interest grows in identifying effective visualization formats. Evidence on formats supporting user preference and comprehension remains limited. Moreover, communication of uncertainty around predicted PROMs remains underexplored. This review evaluates quantitative studies on PROM visualization across clinical domains, focusing on observed past and current scores as well as predicted scores at individual and group levels. METHODS: This review followed PRISMA guidelines and was registered in PROSPERO (CRD42024505034). Systematic searches of PubMed, Scopus, and Web of Science were conducted for quantitative studies published between 2014 and 2024, assessing user preferences and comprehension for the visualization of PROMs. Two independent reviewers screened articles, extracted data, and assessed study quality using the Mixed Methods Appraisal Tool (MMAT). Data were synthesized descriptively according to outcome and visualization type. RESULTS: Thirteen of the 7973 identified studies met inclusion and quality criteria. Seven studies assessed preferences, and seven studies assessed comprehension of visualization formats. For individual-level data, bar charts were preferred over line graphs in three studies, and heat maps in one study; for group-level data, two studies found pie charts preferred over bar charts and icon arrays. For comprehension, bar charts and line graphs were generally well understood, with accuracy ranging from 49 to 100% among patients and 90-100% among clinicians for individual-level data. For group-level data, pie charts were correctly interpreted by 52-95% of the population. One study assessed visualization of predicted PROMs, which patients found difficult to interpret. CONCLUSIONS: Preferences and comprehension of PROM visualizations vary by format, data type, and users. While bar charts, line graphs, and pie charts are preferred, no one-size-fits-all approach exists. Visualization of predicted outcomes remains underexplored. PRACTICE IMPLICATIONS: Future research should study preferences for and comprehension of predicted PROM visualizations and apply user-centered design to support clinical decision-making.

## P14fb3aac8baa

- Year: 2025
- Linked people: Fernando Argento
- Title: Immunogenicity of COVID-19 Vaccines During Pregnancy: A Systematic Review and Comparison of Pregnant Versus Nonpregnant Persons.

Abstract:

BACKGROUND: The COVID-19 pandemic induced the rapid deployment of novel vaccines with pregnant persons identified as an at-risk population due to their increased risk of severe outcomes. Limited data on the immunogenicity of COVID-19 vaccines in pregnant persons were available at the time of implementation. To address this data gap, we developed a living systematic review summarizing emerging evidence on vaccine immunogenicity in pregnancy. METHODS: Following Cochrane, World Health Organization, and Preferred Reporting Items for Systematic reviews and Meta-Analyses guidelines, we included studies on COVID-19 vaccines during pregnancy. We carried out comprehensive biweekly literature searches from March 2022 to October 2023, covering multiple databases. Study selection, data extraction and risk of bias assessment were conducted by pairs of authors independently. Immunogenicity outcomes, primarily post-vaccination neutralizing or binding antibody concentrations, were analyzed descriptively. Post-vaccination antibody ratios in pregnant versus nonpregnant individuals were calculated for the subset of studies that included nonpregnant comparators. RESULTS: By October 2023, our review encompassed 62 studies predominantly analyzing maternal sera (87%), with limited investigation regarding cord, neonatal and infant sera. Most studies investigated mRNA vaccines (97%) and focused on primary vaccination (82%), with some investigating booster doses (15%). Immunogenicity end points included spike-specific IgG (84%) and neutralizing antibodies (24%), with limited data on T-cell responses (3%). Antibodies were detectable after primary vaccination in most pregnant individuals, with similar or modestly attenuated concentrations compared to nonpregnant individuals (ratios > 0.7 for 5/6 estimates of spike-specific IgG), albeit with modest differences in antibody quality and kinetics. Long-term antibody-waning trajectories were similar between pregnant and nonpregnant individuals for up to 8 months after vaccination. CONCLUSIONS: mRNA COVID-19 vaccines induce a robust antibody response during pregnancy comparable (or modestly attenuated) relative to nonpregnant individuals. Immunogenicity data on non-mRNA vaccines are notably underrepresented in the existing literature.

## P99c6e0107b77

- Year: 2026
- Linked people: Birol Yetim
- Title: OECD Ülkelerinde Sağlık Sistem Performansı: Türkiye’nin Konumu Üzerine Çok Kriterli Bir İnceleme

Abstract:

Bu çalışmanın temel amacı, OECD ülkelerinin sağlık sistemi başarısını çok kriterli karar verme yöntemleri ile karşılaştırmalı olarak değerlendirmek, Türkiye’nin OECD ülkeleri arasındaki konumunu ortaya koymak ve farklı yöntemlerden elde edilen skorları karşılaştırmaktır. Çalışmada doğumda beklenen yaşam süresi, bulaşıcı ve kronik hastalıklara bağlı ölüm oranları, karşılanamayan sağlık ihtiyaçları, sağlık hizmetlerinden memnuniyet düzeyi ve algılanan sağlık statüsü olmak üzere altı gösterge dikkate alınmıştır. Veriler; IHME, Eurostat ve OECD gibi uluslararası kurumların düzenli yayınladıkları istatistiklerden elde edilmiştir. Analiz sürecinde TOPSIS, PROMETHEE II ve ELECTRE III yöntemleri birlikte kullanılmıştır. Bulgular; Lüksemburg, İsviçre, Hollanda ve Belçika gibi sosyo-ekonomik düzeyi gelişmiş bazı ülkelerin sağlık sistemi performansında üst sıralarda yer aldığını ancak Letonya, Polonya ve Türkiye gibi düşük gelirli ülkelerin ise alt grupta konumlandığını ortaya koymuştur. Türkiye, bazı göstergelerde görece daha iyi bir performans sergilese de genel başarı düzeyi açısından OECD ülkelerinin gerisinde kalmıştır. Bu çalışma, çok kriterli karar verme yöntemlerinin sağlık sistemi performansını değerlendirmede güçlü ve bütüncül bir yaklaşım sunduğunu ortaya koymakta ve politika yapıcılar ve sağlık yöneticileri için sistem başarısını artırmaya yönelik çok boyutlu öneriler sunmaktadır.

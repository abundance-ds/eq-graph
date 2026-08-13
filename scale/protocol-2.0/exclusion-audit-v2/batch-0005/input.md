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

## P4e77e750ee92

- Year: 2023
- Linked people: Sarah Derrett
- Title: Implementing patient-public engagement for improved health: Lessons from three Ghanaian community-based programmes.

Abstract:

BACKGROUND: Community-based health interventions have been implemented as a key strategy for achieving improved health outcomes in Ghana. Effectiveness, however, largely depends on the successful implementation of patient-public engagement (PPE). Although several PPE studies have been conducted in Ghana, little research has been done to understand the specific role of PPE in the context of implementing community-based health programmes. This paper, therefore, examines the extent of PPE implementation in three selected community-based health programmes (Community-based Health Planning and Service [CHPS], Community-based Maternal and Child Health and Buruli Ulcer) to understand their specific effects on health outcomes. METHODS: Three focus groups, involving 26 participants, were held in three districts of the Ashanti region of Ghana. Participants were mainly health service users involving community health committee members/volunteers, residents and health professionals. They were invited to participate based on their roles in the design and implementation of the programmes. Participants focused on each of Rifkin's spider-gram components. Data were transcribed and analysed descriptively using NVIVO 12 Plus. RESULTS: PPE implementation was found to be extensive across the three programmes in specific areas such as organisation and resource mobilisation. PPE was more restricted in relation to community needs assessment, leadership and management, particularly for the CHPS and Buruli Ulcer programmes. CONCLUSION: Findings suggest that benefits from community-based health interventions are likely to be greater if PPE can be widely implemented across all dimensions of the spider-gram framework.

## P7b922d85c148

- Year: 2022
- Linked people: Sayem Ahmed
- Title: Digital Health Policy and Programs for Hospital Care in Vietnam: Scoping Review

Abstract:

Background There are a host of emergent technologies with the potential to improve hospital care in low- and middle-income countries such as Vietnam. Wearable monitors and artificial intelligence-based decision support systems could be integrated with hospital-based digital health systems such as electronic health records (EHRs) to provide higher level care at a relatively low cost. However, the appropriate and sustainable application of these innovations in low- and middle-income countries requires an understanding of the local government's requirements and regulations such as technology specifications, cybersecurity, data-sharing protocols, and interoperability. Objective This scoping review aims to explore the current state of digital health research and the policies that govern the adoption of digital health systems in Vietnamese hospitals. Methods We conducted a scoping review using a modification of the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses Extension for Scoping Reviews) guidelines. PubMed and Web of Science were searched for academic publications, and Thư Viện Pháp Luật, a proprietary database of Vietnamese government documents, and the Vietnam Electronic Health Administration website were searched for government documents. Google Scholar and Google Search were used for snowballing searches. The sources were assessed against predefined eligibility criteria through title, abstract, and full-text screening. Relevant information from the included sources was charted and summarized. The review process was primarily undertaken by one researcher and reviewed by another researcher during each step. Results In total, 11 academic publications and 20 government documents were included in this review. Among the academic studies, 5 reported engineering solutions for information systems in hospitals, 2 assessed readiness for EHR implementation, 1 tested physicians' performance before and after using clinical decision support software, 1 reported a national laboratory information management system, and 2 reviewed the health system's capability to implement eHealth and artificial intelligence. Of the 20 government documents, 19 were promulgated from 2013 to 2020. These regulations and guidance cover a wide range of digital health domains, including hospital information management systems, general and interoperability standards, cybersecurity in health organizations, conditions for the provision of health information technology (HIT), electronic health insurance claims, laboratory information systems, HIT maturity, digital health strategies, electronic medical records, EHRs, and eHealth architectural frameworks. Conclusions Research about hospital-based digital health systems in Vietnam is very limited, particularly implementation studies. Government regulations and guidance for HIT in health care organizations have been released with increasing frequency since 2013, targeting a variety of information systems such as electronic medical records, EHRs, and laboratory information systems. In general, these policies were focused on the basic specifications and standards that digital health systems need to meet. More research is needed in the future to guide the implementation of digital health care systems in the Vietnam hospital setting.

## P0913e04e4ad1

- Year: 2025
- Linked people: Jenny Downs
- Title: Effectiveness of current digital cognitive behavioural therapy for insomnia interventions for adolescents with insomnia symptoms: A systematic review and meta‐analysis

Abstract:

Sleep problems occur in up to 20%-45% of adolescents. This systematic review and meta-analysis examined the effectiveness of digital sleep interventions, based on cognitive behavioural therapy for insomnia, for adolescents with insomnia symptoms. The objective was to synthesise and quantify, through meta-analyses, changes in sleep following completion of a digital sleep-based intervention. MEDLINE, PubMed, PsycINFO, Scopus, EMBASE, CENTRAL, and Web of Science databases were searched from January 2012 to March 2024. Within-subject studies or randomized-controlled trials reporting the effects of digital cognitive behavioural therapy for insomnia were included. Risk of bias was assessed using the integrated quality criteria for the review of multiple study designs. Random-effects meta-analyses estimated pooled standardised within-subject mean differences to assess effectiveness. Nine studies involving 486 adolescents were included. Digital cognitive behavioural therapy for insomnia interventions were effective in reducing insomnia symptoms (Hedges' g = 1.40), subjective sleep-onset latency (Hedges' g = 0.72) and waking after sleep onset (Hedges' g = 0.47), and increasing subjective and objective total sleep time (Hedges' g = -0.29 and -0.23, respectively). Other objective measures of sleep did not improve. All studies met the minimum ICROMS score and were considered to be of sufficient quality. Seven within-subject studies failed to satisfy all mandatory criteria. These results suggest that digital cognitive behavioural therapy for insomnia interventions are effective in improving adolescent's perceptions of their sleep, but are less effective at improving some objective measures of sleep. To achieve a clear understanding of how digital cognitive behavioural therapy for insomnia interventions compare with other behavioural interventions, additional high-quality randomized-controlled trials comparing digital cognitive behavioural therapy for insomnia interventions with traditional in-person modalities are needed. (PROSPERO;CRD42021287479).

## P17b3e5b48cc7

- Year: 2025
- Linked people: Eliza Wong
- Title: Health Coaching Enhanced Older Adults’ Self-Efficacy in Managing Their Chronic Diseases: A Randomized Controlled Trial

Abstract:

Although health coaching is a well-known self-management intervention for individuals with chronic diseases, the research on its effect on older adults is limited. A total of 414 older Hong Kong adults were randomly assigned to the intervention group, which received 12-week health coaching sessions, and the control group without intervention. Participants in the intervention group completed assessments at three time points (baseline, postintervention, and three-month follow-up), and those in the control group completed baseline and three-month follow-up assessments. Generalized estimating equations first revealed a significant improvement in self-efficacy and blood pressures among the intervention group participants, and such improvements were maintained at follow-up. In addition, the self-efficacy of the intervention group significantly increased while that of the control group significantly decreased from baseline to follow-up. Thus, the overall results demonstrate the effectiveness of the health coaching intervention in improving the self-efficacy of older adults in managing their chronic diseases and health risks.

## Pc5e868c58ef6

- Year: 2026
- Linked people: Ciaran O'Neill
- Title: Using Role Substitution to Improve Oral Health of Dependent Older People Residing in Care Homes and Assisted Living Settings in the United Kingdom.

Abstract:

OBJECTIVES: To determine whether Dental Therapists and Dental Nurses could reduce plaque levels of dependent older adults residing in care homes and assisted living settings, when compared to 'treatment as usual'. METHODS: A two-arm pragmatic cluster randomised controlled trial over a 6-month period was undertaken based on an a priori assumption of superiority. Forty-eight dependent settings across Wales, North-West England, London and Northern Ireland were recruited. Dependent settings were excluded if they solely focused on end-of-life or palliative care or were already participating in an oral health prevention programme. Residents were excluded if they were below 65 years of age or if they were receiving end-of-life or palliative care. Dependent settings were randomised using an adaptive algorithm, which generated the randomisation sequence. After allocation, the Chief Investigator, Principal Investigators and the trial statistician were blinded until the trial was completed and the analysis was complete. Due to the nature of the intervention, outcome assessors, those delivering the intervention and the residents were not blinded. Dental Therapists provided routine dental care according to their Scope of Practice. Dental Nurses administered fluoride varnish, oversaw the use of high-strength fluoride toothpaste, and sought to improve the level of day-to-day prevention offered by the formal carers. Current practice formed the control arm. In the United Kingdom, this is often ad hoc and relies on dentists, if available, visiting residents presenting with clinical symptoms. The intervention period lasted for 6 months. The primary outcome measure was the proportion of residents that demonstrated a 50% reduction in the Silness and Löe plaque index. Secondary outcome measures were the number of new carious lesions (coronal and root caries), bleeding on probing, Oral Impacts on Daily Performances, EuroQol five dimensions questionnaire (quality of life measure), oral symptoms, episodes of pain, and episodes of unscheduled care, and the number of onward referrals to dentists. RESULTS: Twenty-four dependent settings were allocated to receive the intervention and 24 continued with 'treatment as usual'. 41.7% of the settings were in London, 33.3% were in Wales or the Northwest of England, and 25.0% of the settings were in Northern Ireland. One hundred and twenty-two residents were allocated to the control arm and 142 residents in the intervention arm. The mean age was 85 years and 67.2% were female. Levels of cognitive impairment were high in both arms (mean score 13.7 on the Six Item Cognitive Impairment Test). No statistically significant differences were found in the primary or secondary outcome measures at 6-months. No differences were apparent in the number of adverse events related to the trial by group. CONCLUSIONS: A 6-month intervention using Dental Therapists and Dental Nurses did not produce any measurable improvements in oral health within dependent settings when compared to treatment as usual. High levels of cognitive impairment may have contributed to the lack of any effect seen. TRIAL REGISTRATION: The study was registered with ISRCTN: ISRCTN16332897 (https://doi.org/10.1186/ISRCTN16332897) on 3 December 2021 and the protocol was published in 2022 (https://doi.org/10.1186/s13063-022-06487-3).

## P4271639c4273

- Year: 2024
- Linked people: Aaron Winn
- Title: Urinary Incontinence Medications: Patient-Initiated Concerns in Primary Care

Abstract:

IMPORTANCE: Guideline-recommended medications for overactive bladder and urge urinary incontinence (OAB/UUI) are effective but have high costs and side effects. Little is known about patient concerns regarding these medications when prescribed by their primary care providers (PCPs). OBJECTIVE: The aim of the study was to describe PCP-patient interactions when prescribing medications for OAB/UUI, specifically clinical concerns, cost and authorization issues, and mode of communication for these interactions. STUDY DESIGN: Using electronic health records, we identified a retrospective cohort of women aged 18-89 years who were prescribed a medication for OAB/UUI during a primary care office visit from 2017 to 2018. We examined the electronic health record from initial prescription through 15 subsequent months for documentation of prior authorization requests and patient concerns about cost, side effects, or ineffectiveness. The association of patient demographics, comorbidity, and medication class with these concerns was examined with logistic regression models. RESULTS: Overall, 46.2% of patients (n = 123) had 1 or more OAB/UUI medication concerns, and 52 reported outside an office visit. Only higher comorbidity was associated with reduced concern of any type. Although the overall percent age of patients reporting concerns was similar by medication type, the patterns of concern type varied. Compared with those taking short-acting antimuscarinics, patients taking long-acting antimuscarinics other than oxybutynin were less likely to have side effect concerns (adjusted odds ratio 0.35, 95% CI 0.16-0.78) and more likely to have cost concerns (adjusted odds ratio 5.10, 95% CI 1.53-17.03). CONCLUSIONS: Patient concerns regarding OAB/UUI medications were common in primary care practices and frequently reported outside of office visits. However, the patterns of concerns (cost vs side effects) varied between medication classes.

## P58076867c137

- Year: 2021
- Linked people: David Whitehurst
- Title: Assessment of an Interactive Digital Health–Based Self-management Program to Reduce Hospitalizations Among Patients With Multiple Chronic Diseases

Abstract:

Importance: Digital health programs may have the potential to prevent hospitalizations among patients with chronic diseases by supporting patient self-management, symptom monitoring, and coordinated care. Objective: To compare the effect of an internet-based self-management and symptom monitoring program targeted to patients with 2 or more chronic diseases (internet chronic disease management [CDM]) with usual care on hospitalizations over a 2-year period. Design, Setting, and Participants: This single-blinded randomized clinical trial included patients with multiple chronic diseases from 71 primary care clinics in small urban and rural areas throughout British Columbia, Canada. Recruitment occurred between October 1, 2011, and March 23, 2015. A volunteer sample of 456 patients was screened for eligibility. Inclusion criteria included daily internet access, age older than 19 years, fluency in English, and the presence of 2 or more of the following 5 conditions: diabetes, heart failure, ischemic heart disease, chronic kidney disease, or chronic obstructive pulmonary disease. A total of 230 patients consented to participate and were randomized to receive either the internet CDM intervention (n = 117) or usual care (n = 113). One participant in the internet CDM group withdrew from the study after randomization, resulting in 229 participants for whom data on the primary outcome were available. Interventions: Internet-based self-management program using telephone nursing supports and integration within primary care compared with usual care over a 2-year period. Main Outcomes and Measures: The primary outcome was all-cause hospitalizations at 2 years. Secondary outcomes included hospital length of stay, quality of life, self-management, and social support. Additional outcomes included the number of participants with at least 1 hospitalization, the number of participants who experienced a composite outcome of all-cause hospitalization or death, the time to first hospitalization, and the number of in-hospital days. Results: Among 229 participants included in the analysis, the mean (SD) age was 70.5 (9.1) years, and 141 participants (61.6%) were male; data on race and ethnicity were not collected because there was no planned analysis of these variables. The internet CDM group had 25 fewer hospitalizations compared with the usual care group (56 hospitalizations vs 81 hospitalizations, respectively [30.9% reduction]; relative risk [RR], 0.68; 95% CI, 0.43-1.10; P = .12). The intervention group also had 229 fewer in-hospital days compared with the usual care group (282 days vs 511 days, respectively; RR, 0.52; 95% CI, 0.24-1.10; P = .09). Components of self-management and social support improved in the intervention group. Fewer participants in the internet CDM vs usual care group had at least 1 hospitalization (32 of 116 individuals [27.6%] vs 46 of 113 individuals [40.7%]; odds ratio [OR], 0.55; 95% CI, 0.31-0.96; P = .03) or experienced the composite outcome of all-cause hospitalization or death (37 of 116 individuals [31.9%] vs 51 of 113 individuals [45.1%]; OR, 0.57; 95% CI, 0.33-0.98; P = .04). Participants in the internet CDM group had a lower risk of time to first hospitalization (hazard ratio, 0.62; 95% CI, 0.39-0.97; P = .04) than those in the usual care group. Conclusions and Relevance: In this study, an internet-based self-management program did not result in a significant reduction in hospitalization. However, fewer participants in the intervention group were admitted to the hospital or experienced the composite outcome of all-cause hospitalization or death. These findings suggest the internet CDM program has the potential to augment primary care among patients with multiple chronic diseases. Trial Registration: ClinicalTrials.gov Identifier: NCT01342263.

## P931f521df456

- Year: 2023
- Linked people: Nick Bansback
- Title: The Association of Rheumatologist Supply and Multidisciplinary Care With Timely Patient Access to Rheumatologists: Evidence From British Columbia, Canada

Abstract:

OBJECTIVE: The objective was to understand how the expansion of rheumatology supply and the introduction of multidisciplinary care was associated with access to rheumatology services. METHODS: We accessed Population Data BC, a longitudinal database with de-identified individual-level health data on all residents of British Columbia, Canada, to analyze physician visits and prescribing from 2010-2011 to 2019-2020. We calculated access as the time from referral to first rheumatologist visit and, for people with rheumatoid arthritis (RA), time to first disease-modifying antirheumatic drug (DMARD). Associations between lag time, patient characteristics, and system variables were explored using quantile regression. RESULTS: Over the study period, there were 149,902 new rheumatologist visits, with 31% more visits in 2019-2020 than in 2010-2011. The proportion of first visits for patients with inflammatory arthritis increased from 28% to 51%. The median time from referral to first visit decreased by 22 days (35%) from 63 days (interquartile range 21-120 days) in 2010-2011. For people with RA, time from referral to DMARD decreased by 4 days (6%) to 62 days. Male sex, living in metropolitan areas, and having a rheumatologist who used a multidisciplinary care assessment code were associated with shorter times from referral to first DMARD. CONCLUSION: Access to rheumatology care improved, and the increased proportion of patients with IA in the first visits case-mix indicates that rheumatologist supply and incentives for multidisciplinary care may have improved referral patterns. However, time to DMARDs for people with RA remained long, and we found signals of unequal access for female patients and people living outside of metropolitan areas.

## Pcccdb7744deb

- Year: 2022
- Linked people: Harri Sintonen
- Title: Long-term health-related quality of life in patients with ruptured arteriovenous malformations treated in childhood

Abstract:

OBJECTIVE: The aim of this study was to reveal the long-term health-related quality of life (HRQOL), educational level, and impact on occupation in 55 patients who experienced ruptured brain arteriovenous malformations (AVMs) that were treated during childhood. METHODS: In 2016, questionnaires including the 15D instrument were sent to all living patients older than 18 years (n = 432) in the Helsinki AVM database. The cohort was further specified to include only patients with ruptured AVMs who were younger than 20 years at the time of diagnosis (n = 55). Educational level was compared with the age-matched general population of Finland. The mean 15D scores were calculated for independent variables (Spetzler-Ponce classification, admission age, symptomatic epilepsy, and multiple bleeding episodes) and tested using the independent-samples t-test or ANCOVA. Linear regression was used to create a multivariate model. Bonferroni correction was used with multiple comparisons. RESULTS: The mean follow-up time from diagnosis to survey was 24.2 (SD 14.7) years. The difference in the mean 15D scores between Spetzler-Ponce classes did not reach statistical significance. The youngest age group (< 10 years at the time of diagnosis) performed less well on the dimension of usual activities than the older patients. Symptomatic epilepsy significantly reduced the long-term HRQOL. Multiple hemorrhages significantly reduced the scores on three dimensions: mobility, speech, and sexual activity. In the regression model, symptomatic epilepsy was the only significant predictor for a lower 15D score. The educational level of the cohort was for the most part comparable to that of the general population in the same age group. AVM was the reason for early retirement in 11% of the patients, while lowered performance because of the AVM was reported by 37% of the patients. CONCLUSIONS: Patients with ruptured AVMs treated in childhood can live an independent and meaningful life, even in the case of the highest-grade lesions. Symptomatic epilepsy significantly reduced the long-term HRQOL, highlighting the need for continuing support for these patients.

## P8cd861528f6c

- Year: 2023
- Linked people: Stirling Bryan
- Title: Concordance between 8-1-1 HealthLink BC Emergency iDoctor-in-assistance (HEiDi) virtual physician advice and subsequent health service utilization for callers to a nurse-managed provincial health information telephone service

Abstract:

BACKGROUND: British Columbia 8-1-1 callers who are advised by a nurse to seek urgent medical care can be referred to virtual physicians (VPs) for supplemental assessment and advice. Prior research indicates callers' subsequent health service use may diverge from VP advice. We sought to 1) estimate concordance between VP advice and subsequent health service use, and 2) identify factors associated with concordance to understand potential drivers of discordant cases. METHODS: We linked relevant provincial administrative databases to obtain inpatient, outpatient, and emergency service use by callers. We developed operational definitions of concordance collaboratively with researcher, patient, VP, and management perspectives. We used Kaplan-Meier curves to describe health service use post-VP consultation and Cox regression to estimate the association of caller factors (rurality, demography, attachment to primary care) and call factors (reason, triage level, time of day) with concordance as hazard ratios. RESULTS: We analyzed 17,188 calls from November 16, 2020 to April 30, 2021. Callers advised to attend an emergency department (ED) immediately were the most concordant (73%) while concordance was lowest for those advised to seek Family Physician (FP) care either immediately (41%) or within 7 days (47%). Callers unattached to FPs were less likely to schedule an FP visit (hazard ratio = 0.76 [95%CI: 0.68-0.85]). Rural callers were less likely to attend an ED within 48 h when advised to go immediately (0.53 [95%CI:0.46-0.61]) compared to urban callers. Rural callers advised to see an FP, either immediately (1.28 [95%CI:1.01-1.62]) or within 7 days (1.23 [95%CI: 1.11-1.37]), were more likely to do so than urban callers. INTERPRETATION: Concordance between VP advice and subsequent caller health service use varies substantially by category of advice and caller rurality. Concordance with advice to "Go to ED" is high overall but to access primary care is below 50%, suggesting potential issues with timely access to FP care. Future research from a patient/caller centered perspective may reveal additional barriers and facilitators to concordance.

## Pb59643240712

- Year: 2024
- Linked people: Brigitte Essers, Iwan van der Horst
- Title: Health-related quality of life one year after refractory cardiac arrest treated with conventional or extracorporeal CPR; a secondary analysis of the INCEPTION-trial

Abstract:

Background: Prospective, trial-based data comparing health-related quality of life (HRQoL) in patients surviving out-of-hospital cardiac arrest (OHCA) through extracorporeal cardiopulmonary resuscitation (ECPR) or conventional CPR (CCPR) are scarce. We aimed to determine HRQoL during 1-year after refractory OHCA in patients treated with ECPR and CCPR. Methods: We present a secondary analysis of the multicenter INCEPTION-trial, which studied the effectiveness of ECPR versus CCPR in patients with refractory OHCA. HRQoL was prospectively assessed using the EQ-5D-5L questionnaire. Poor HRQoL was pragmatically defined as an EQ-5D-5L health utility index (HUI) > 1 SD below the age-adjusted norm. We used mixed linear models to assess the difference in HRQoL over time and univariable analyses to assess factors potentially associated with poor HRQoL. Results: A total of 134 patients were enrolled, and hospital survival was 20% (27 patients). EQ-5D-5L data were available for 25 patients (5 ECPR and 20 CCPR). One year after OHCA, the estimated mean HUI was 0.73 (0.05) in all patients, 0.84 (0.12) in ECPR survivors, and 0.71 (0.05) in CCPR survivors (p-value 0.31). Eight (32%) survivors had a poor HRQoL. HRQoL was good in 17 (68%) patients, with 100% in ECPR survivors versus 60% in CCPR survivors (p-value 0.14). Conclusion: One year after refractory OHCA, 68% of the survivors had a good HRQoL. We found no statistically significant difference in HRQoL one year after OHCA in patients treated with ECPR compared to CCPR. However, numerical differences may be clinically relevant in favor of ECPR.

## Pcd0da3956cfa

- Year: 2022
- Linked people: Claire Gudex
- Title: Compensation Claims in Danish Emergency Care: Identifying Hot Spots and Blind Spots in the Quality of Care

Abstract:

BACKGROUND: The Healthcare Complaints Analysis Tool (HCAT) offers a validated way of systematically extracting content from patient complaints for further analysis of complaint hot spots with harm or near misses, and blind spots with, for example, systemic problems or quality problems arising during discharge. This study analyzed a Danish national sample of compensations claims about emergency care using the HCAT. METHODS: Through use of the HCAT, compensation claims about Danish emergency care from 2013 to 2017 (N = 712) were coded and then grouped to identify and highlight hot spot problem areas (harm and near misses) and blind spot problem areas (admission/discharge, systemic problems, errors of omission). Two assessors coded the compensation claims by entering data into a database. RESULTS: The HCAT analyses of the sample resulted in coding of 1,305 problems. Most problems concerned quality and safety issues at the examination/diagnosis stage of care (63.9%). In 91.2% of the cases, the level of harm was moderate or major. Harm hot spots most often involved diagnostic errors (189 problems). Eighty-nine problems related to errors of omission, all causing moderate or major harm. For systemic blind spots, patient harm significantly increased in cases of multiple problem types in the compensation claim (odds ratio = 1.6, 95% confidence interval = 1.3-2.0). CONCLUSION: Systematic coding and analytic approach to the HCAT can highlight potential quality problems in emergency care and point to areas for further consideration. From the perspective of future health care harm prevention, there seems to be a strong incentive for further analysis of the amount, nature, and prevention of diagnostic errors in emergency care.

## P8db138ae7287

- Year: 2025
- Linked people: Kim Dalziel
- Title: Intervention overuse in paediatric care in Australian metropolitan general practice

Abstract:

CHILD, to which Australia is a signatory, states that 'children and young people have the right to the highest attainable standard of healthcare' emphasising 'the development of primary health care' for children. 1,2The Royal Australasian College of General Practitioners' (RACGP) 'First do no harm' initiative and the Royal Australasian College of Physicians' (RACP) EVOLVE initiative (led by RACP members to drive high-value, high-quality care in Australia and Aotearoa New Zealand) provide guidance for physicians on the avoidance of intervention overuse paediatric or low-value care (LVC). 3,4LVC is defined as the delivery of health services where no or a disproportionately low benefit is obtained relative to financial cost. 5To date, the paediatric LVC literature has placed greater emphasis on hospital-delivered care rather than primary healthcare, yet the larger volume of care is delivered in primary care settings. 6,7n Australia, the last large-scale analysis of paediatric care quality was conducted through the CareTrack Kids study (2012-13). 8Adherence to clinical practice guideline recommendations for 17 common childhood conditions was 59.8% (95% confidence interval [CI]: 57.5 to 62.0) among clinicians across primary, secondary and tertiary healthcare.For example, for asthma, the adherence to guideline-concordant care was lower among primary care providers (54.4%; 95% CI: 46.0 to 62.5) compared with paediatricians (77.7%; 95% CI: 40.5 to 97.0), emergency departments (ED; 79.9%; 95% CI: 70.6 to 87.3) and inpatient care (85.1%; 95% CI: 76.7 to 91.5). 9 Whether healthcare quality for children provided by general practitioners (GPs) has changed over the past decade is unknown.The aim of the current study was to analyse the prevalence of LVC across five common paediatric conditions.Associated GP practice and individual GP characteristics, as well as the financial cost of LVC care, were evaluated.

## P17ff6529c08a

- Year: 2022
- Linked people: Federico Augustovski
- Title: Consolidated Health Economic Evaluation Reporting Standards (CHEERS) 2022 Explanation and Elaboration: A Report of the ISPOR CHEERS II Good Practices Task Force

Abstract:

Health economic evaluations are comparative analyses of alternative courses of action in terms of their costs and consequences. The Consolidated Health Economic Evaluation Reporting Standards (CHEERS) statement, published in 2013, was created to ensure health economic evaluations are identifiable, interpretable, and useful for decision making. It was intended as guidance to help authors report accurately which health interventions were being compared and in what context, how the evaluation was undertaken, what the findings were, and other details that may aid readers and reviewers in interpretation and use of the study. The new CHEERS 2022 statement replaces the previous CHEERS reporting guidance. It reflects the need for guidance that can be more easily applied to all types of health economic evaluation, new methods and developments in the field, and the increased role of stakeholder involvement including patients and the public. It is also broadly applicable to any form of intervention intended to improve the health of individuals or the population, whether simple or complex, and without regard to context (such as healthcare, public health, education, and social care). This Explanation and Elaboration Report presents the new CHEERS 2022 28-item checklist with recommendations and explanation and examples for each item. The CHEERS 2022 statement is primarily intended for researchers reporting economic evaluations for peer-reviewed journals and the peer reviewers and editors assessing them for publication. Nevertheless, we anticipate familiarity with reporting requirements will be useful for analysts when planning studies. It may also be useful for health technology assessment bodies seeking guidance on reporting, given that there is an increasing emphasis on transparency in decision making.

## Pe47b2987967d

- Year: 2023
- Linked people: Shankar Prinja
- Title: Evaluating efficiency and equity of prevention and control strategies for rheumatic fever and rheumatic heart disease in India: an extended cost-effectiveness analysis

Abstract:

BACKGROUND: There is a dearth of evidence on the cost-effectiveness of a combination of population-based primary, secondary, and tertiary prevention and control strategies for rheumatic fever and rheumatic heart disease. The present analysis evaluated the cost-effectiveness and distributional effect of primary, secondary, and tertiary interventions and their combinations for the prevention and control of rheumatic fever and rheumatic heart disease in India. METHODS: A Markov model was constructed to estimate the lifetime costs and consequences among a hypothetical cohort of 5-year-old healthy children. Both health system costs and out-of-pocket expenditure (OOPE) were included. OOPE and health-related quality-of-life were assessed by interviewing 702 patients enrolled in a population-based rheumatic fever and rheumatic heart disease registry in India. Health consequences were measured in terms of life-years and quality-adjusted life-years (QALY) gained. Furthermore, an extended cost-effectiveness analysis was undertaken to assess the costs and outcomes across different wealth quartiles. All future costs and consequences were discounted at an annual rate of 3%. FINDINGS: A combination of secondary and tertiary prevention strategies, which had an incremental cost of ₹23 051 (US$30) per QALY gained, was the most cost-effective strategy for the prevention and control of rheumatic fever and rheumatic heart disease in India. The number of rheumatic heart disease cases prevented among the population belonging to the poorest quartile (four cases per 1000) was four times higher than the richest quartile (one per 1000). Similarly, the reduction in OOPE after the intervention was higher among the poorest income group (29·8%) than among the richest income group (27·0%). INTERPRETATION: The combined secondary and tertiary prevention and control strategy is the most cost-effective option for the management of rheumatic fever and rheumatic heart disease in India, and the benefits of public spending are likely to be accrued much more by those in the lowest income groups. The quantification of non-health gains provides strong evidence for informing policy decisions by efficient resource allocation on rheumatic fever and rheumatic heart disease prevention and control in India. FUNDING: Department of Health Research, Ministry of Health and Family Welfare, New Delhi.

## Pc621a892a765

- Year: 2024
- Linked people: Ilias Goranitis
- Title: A micro-costing study of mass-spectrometry based quantitative proteomics testing applied to the diagnostic pipeline of mitochondrial and other rare disorders

Abstract:

BACKGROUND: Mass spectrometry-based quantitative proteomics has a demonstrated utility in increasing the diagnostic yield of mitochondrial disorders (MDs) and other rare diseases. However, for this technology to be widely adopted in routine clinical practice, it is crucial to accurately estimate delivery costs. Resource use and unit costs required to undertake a proteomics test were measured and categorized into consumables, equipment, and labor. Unit costs were aggregated to obtain a total cost per patient, reported in 2023 Australian dollars (AUD). Probabilistic and deterministic sensitivity analysis were conducted to evaluate parameter uncertainty and identify key cost drivers. RESULTS: The mean cost of a proteomics test was $897 (US$ 607) per patient (95% CI: $734-$1,111). Labor comprised 53% of the total costs. At $342 (US$ 228) per patient, liquid chromatography coupled tandem mass spectrometry (LC-MS/MS) was the most expensive non-salary component. An integrated analysis pipeline where all the standard analysis are performed automatically, as well as discounts or subsidized LC-MS/MS equipment or consumables can lower the cost per test. CONCLUSIONS: Proteomics testing provide a lower-cost option and wider application compared to respiratory chain enzymology for mitochondrial disorders and potentially other functional assays in Australia. Our analysis suggests that streamlining and automating workflows can reduce labor costs. Using PBMC samples may be a cheaper and more efficient alternative to generating fibroblasts, although their use has not been extensively tested yet. Use of fibroblasts could potentially lower costs when fibroblasts are already available by avoiding the expense of isolating PBMCs. A joint evaluation of the health and economic implications of proteomics is now needed to support its introduction to routine clinical care.

## P4322a2ea9dd4

- Year: 2024
- Linked people: Narcis Gusi
- Title: 116 Expert Agreement on definitions for compensatory protective step strategies: Delphi method study

Abstract:

Abstract Purpose The older adults have a high probability of suffering an unexpected fall during activities of daily living, this can generate fear of fall, changes in gait patterns, decreased mobility, reduced social contact and impaired ability to perform different activities. Previous studies of gait in the presence of a perturbance identified and analyzed several protective gait strategies to prevent a fall. But there was a lack of common wording and definitions for the same strategy that limits the comparison and scientific synergic advance among researchers and professionals. Objective to elaborate and clarify the definitions of compensatory protective step strategies to create a single common terminology to be used by all related-professionals (e.g., physical educators, physiotherapists, occupational therapists, doctors and researchers). Methods the study followed the Conducting and Reporting of Delphi Studies guideline (CREDES) and a chronological order 1) review of the literature (scoping review), 2) step-by-step creating a quantitative questionnaire (Likert-type scale from 1 to 5) and qualitative assessment of degree the pertinence, wording and identification of each of the definitions (items=14), 3) same number of experts selection from different professional backgrounds (N = 14), 4) Aike's V coefficient was used to determine content validity. Results showed demanding levels of validity (V ≥ 0.68) and none of the strategy definitions were eliminated, all of them passed Aiken’s V critical value. Conclusion: the definitions of 14 compensatory protective step strategies (13 strategies mentioned in the scoping review and one added by the panel of experts) have been elaborated and clarified. The limb collisions were not included by the consensus of the panel of experts because it was considered as an isolated action and information about its protective function is lacking. These identifications could be used as innovative specific targets to include in health enhancing physical activity programs Funding The Spanish National R + D + i Plan co-funded by the Spanish Ministry of Sciences and Innovation (reference PID2019-107191RB I00/AEI/10.13039/501100011033). The author J.L.L.-L. was supported by a grant from the Spanish Ministry of Education, Culture and Sport (FPU18/05655).

## P55eba2713984

- Year: 2025
- Linked people: Julie Ratcliffe
- Title: New Horizons? Assessing General Public Preferences for a Wellbeing Economy in the Post-COVID-19 World.

Abstract:

OBJECTIVE: As societies emerge from the COVID-19 pandemic, governments are increasingly moving away from a focus on economic growth at any cost towards the principles of a wellbeing economy, focused on achieving a more equitable distribution of wealth and wellbeing. This study aimed to assess the relative importance to the Australian general public of the key principles of a wellbeing economy and to investigate heterogeneity in preferences between demographic subgroups. METHODS: An online survey was developed and delivered to a general public sample of 2042 Australian adults (aged 18 years and above). Respondents were invited to rank the key principles of a wellbeing economy (dignity, nature and climate, social connection, fairness and participation) plus two additional traditional economic indicators of societal success ('economic growth' and 'economic prosperity') in order of their relative importance for informing future policy directions. Data analysis was conducted using simple summative scoring, which involved the use of a point system allocated to rankings as a dependent variable. In addition, a rank-ordered logit model was used to explore preferences for the entire sample and subgroups defined by key socio-demographic characteristics. RESULTS: 'Dignity' (people have enough to live in comfort, safety and happiness) and 'fairness' (equal opportunity for all Australians and the gap between richest and poorest greatly reduced) were ranked as the most important priorities for the total sample and for key socio-demographic subgroups differentiated by age, level of education and level of socio-economic advantage. Traditional economic indicators of societal success including 'economic prosperity' and 'economic growth' were considered important but generally ranked below the principles of 'dignity' and 'fairness'. CONCLUSIONS: The findings indicate that government movements away from traditional economic indicators and towards new broader wellbeing economy measures of societal success are likely to be supported by the general public.

## P973e628a1874

- Year: 2022
- Linked people: Nancy Devlin, Tianxin Pan
- Title: The impact of depression and physical multimorbidity on health-related quality of life in China: a national longitudinal quantile regression study.

Abstract:

The co-occurrence of mental and physical chronic conditions is a growing concern and a largely unaddressed challenge in low-and-middle-income countries. This study aimed to investigate the independent and multiplicative effects of depression and physical chronic conditions on health-related quality of life (HRQoL) in China, and how it varies by age and gender. We used two waves of the China Health and Retirement Longitudinal Study (2011, 2015), including 9227 participants aged ≥ 45 years, 12 physical chronic conditions and depressive symptoms. We used mixed-effects linear regression to assess the effects of depression and physical multimorbidity on HRQoL, which was measured using a proxy measure of Physical Component Scores (PCS) and Mental Component Scores (MCS) of the matched SF-36 measure. We found that each increased number of physical chronic conditions, and the presence of depression were independently associated with lower proxy PCS and MCS scores. There were multiplicative effects of depression and physical chronic conditions on PCS (- 0.83 points, 95% CI - 1.06, - 0.60) and MCS scores (- 0.50 points, 95% CI - 0.73, - 0.27). The results showed that HRQoL decreased markedly with multimorbidity and was exacerbated by the presence of co-existing physical and mental chronic conditions.

## Pcda1b48db064

- Year: 2023
- Linked people: Mark Sculpher
- Title: Randomised trial of stable chest pain investigation: 3-year clinical and quality of life results from CE-MARC 2

Abstract:

AIMS: Guidelines for suspected cardiac chest pain have used historical risk stratification tools, advocating invasive coronary angiography (ICA) first-line in those at highest risk. We aimed to determine whether different strategies to manage suspected stable angina affected medium-term cardiovascular event rates and patient-reported quality of life (QoL) measures. METHODS: CE-MARC 2, a three-arm parallel group trial, randomised patients with suspected stable cardiac chest pain and a Duke Clinical pretest likelihood of coronary artery disease between 10% and 90%. Patients were randomised to either first-line cardiovascular magnetic resonance (CMR), single-photon emission computed tomography (SPECT) or the UK National Institute for Health and Care Excellence (NICE) CG95 (2010) guidelines-directed care. For the three arms, 1-year and 3-year first major adverse cardiovascular event (MACE) rates and QoL assessed by the Seattle Angina Questionnaire, Short Form 12 (V.12) Questionnaire and EuroQol-5 Dimension Questionnaire were recorded. RESULTS: 1202 patients were randomised to CMR (n=481), SPECT (n=481) and NICE (n=240). Forty-two patients (18 CMR, 18 SPECT, 6 NICE) experienced one or more MACEs. The percentage rates (95% CIs) of MACE in the CMR, SPECT and NICE groups at 3 years were 3.7% (2.4%, 5.8%), 3.7% (2.4%, 5.8%) and 2.1% (0.9%, 4.8%), respectively. QoL scores did not significantly differ across domains. CONCLUSION: Despite a fourfold increase in referrals for ICA, the NICE CG95 (2010) guidelines risk-stratified care strategy did not significantly reduce 3-year MACE or improve QoL, as compared with functional imaging with CMR or SPECT. TRIAL REGISTRATION NUMBER: ClinicalTrials.gov Registry (NCT01664858).

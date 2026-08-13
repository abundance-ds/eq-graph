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

## Pc0cc1bb04e40

- Year: 2024
- Linked people: Elly Stolk
- Title: Headpulse measurement can reliably identify large-vessel occlusion stroke in prehospital suspected stroke patients: Results from the EPISODE-PS-COVID study.

Abstract:

Background Large-vessel occlusion (LVO) stroke represents one-third of acute ischemic stroke (AIS) in the United States but causes two-thirds of poststroke dependence and >90% of poststroke mortality. Prehospital LVO stroke detection permits efficient emergency medical systems (EMS) transport to an endovascular thrombectomy (EVT)-capable center. Our primary objective was to determine the feasibility of using a cranial accelerometry (CA) headset device for prehospital LVO stroke detection. Our secondary objective was development of an algorithm capable of distinguishing LVO stroke from other conditions. Methods We prospectively enrolled consecutive adult patients suspected of acute stroke from 11 study hospitals in four different U.S. geographical regions over a 21-month period. Patients received device placement by prehospital EMS personnel. Headset data were matched with clinical data following informed consent. LVO stroke diagnosis was determined by medical chart review. The device was trained using device data and Los Angeles Motor Scale (LAMS) examination components. A binary threshold was selected for comparison of device performance to LAMS scores. Results A total of 594 subjects were enrolled, including 183 subjects who received the second-generation device. Usable data were captured in 158 patients (86.3%). Study subjects were 53% female and 56% Black/African American, with median age 69 years. Twenty-six (16.4%) patients had LVO and 132 (83.6%) were not LVO (not-LVO AIS, 33; intracerebral hemorrhage, nine; stroke mimics, 90). COVID-19 testing and positivity rates (10.6%) were not different between groups. We found a sensitivity of 38.5% and specificity of 82.7% for LAMS ≥ 4 in detecting LVO stroke versus a sensitivity of 84.6% (p Conclusions Obtaining adequate recordings with a CA headset is highly feasible in the prehospital environment. Use of the device algorithm incorporating both CA and LAMS data for LVO detection resulted in significantly higher sensitivity without reduced specificity when compared to the use of LAMS alone.

## Pcf05ac2edd07

- Year: 1993
- Linked people: Ben Van Hout
- Title: Effects of ACE inhibitors on heart failure in The Netherlands: a pharmacoeconomic model

Abstract:

A modelling approach is used to analyse the cost effectiveness of prescribing angiotensin converting enzyme (ACE) inhibitors, compared with standard practice, as first-line therapeutic agents in the treatment of heart failure in The Netherlands. Data concerning costs, incidence, prevalence and survival are used to construct an age-dependent semi-Markov-chain model. Two scenarios are compared. The first reflects the continuation of common practice. The second, containing assumptions made on the basis of results from randomised clinical trials, reflects the situation in which ACE inhibitors are given as first-line pharmacotherapy. Conditional on the estimates and assumptions made, it is shown that prescribing ACE inhibitors as first-line pharmacotherapy will improve survival by about 4% over the first 10 years, and will save about 17% in costs over the first 10 years. Sensitivity analysis shows the robustness of the conclusions to all major parameters.

## P26410cf35508

- Year: 2005
- Linked people: Elly Stolk
- Title: Values for resource allocation should expose the adaptation process, not the outcome

Abstract:

Menzel P, Dolan O, Richardson J, Olsen JA. The role of adaptation to disability and disease in health state valuation: a preliminary normative analysis. Soc Sci Med. 2002;55(12):2149-2158. Ubel PA, Loewenstein G, Jepson C. Whose quality of life? A commentary exploring discrepancies between health state evaluations of patients and the general public. Qual Life Res. 2003;12(6):599-607.

## P111b14fc8d2b

- Year: 1998
- Linked people: Ben Van Hout
- Title: Sample size calculation in economic evaluations

Abstract:

A simulation method is presented for sample size calculation in economic evaluations. As input the method requires: the expected difference and variance of costs and effects, their correlation, the significance level (alpha) and the power of the testing method and the maximum acceptable ratio of incremental effectiveness to incremental costs. The method is illustrated with data from two trials. The first compares primary coronary angioplasty with streptokinase in the treatment of acute myocardial infarction, in the second trial, lansoprazole is compared with omeprazole in the treatment of reflux oesophagitis. These case studies show how the various parameters influence the sample size. Given the large number of parameters that have to be specified in advance, the lack of knowledge about costs and their standard deviation, and the difficulty of specifying the maximum acceptable ratio of incremental effectiveness to incremental costs, the conclusion of the study is that from a technical point of view it is possible to perform a sample size calculation for an economic evaluation, but one should wonder how useful it is.

## Pb8f868bd311b

- Year: 2009
- Linked people: Gerard De Pouvourville
- Title: La convergence tarifaire entre hôpitaux publics et privés : mission impossible ?

Abstract:

Article disponible en ligne l'adresse https://shs.cairn.info/revue-regards-croises-sur-l-economie-2009-1-page-181?lang=fr Dcouvrir le sommaire de ce numro, suivre la revue par email, s'abonner... Scannez ce QR Code pour accder la page de ce numro sur Cairn.info. Distribution lectronique Cairn.info pour La Dcouverte.Vous avez l'autorisation de reproduire cet article dans les limites des conditions d'utilisation de Cairn.infoou, le cas chant, des conditions gnrales de la licence souscrite par votre tablissement.Dtails et conditions sur cairn.info/copyright.Sauf dispositions lgales contraires, les usages numriques des fins pdagogiques des prsentes ressources sont soumises l'autorisation de l'diteur ou, le cas chant, de l'organisme de gestion collective habilit cet effet.Il en est ainsi notamment en France avec le CFC qui est l'organisme agr en la matire.

## P1141bb655825

- Year: 2012
- Linked people: Ben Van Hout
- Title: Estimating Preference-Based EQ-5D Health State Utilities or Item Responses from Neuropathic Pain Scores

Abstract:

Preference-based health state utilities are required for many health economic evaluations. When the direct evidence of such is lacking and only condition-specific scores are available, establishing a 'mapping' relationship between instruments can be useful. Our objective was to map the 11-point Pain Intensity Numerical Rating Scale (PI-NRS-11), a pain-specific instrument ranging from 0 ('no pain') to 10 ('pain as bad as you can imagine'), to the EQ-5D, a preference-based generic instrument. We used web survey data collected from adult US respondents who (i) had ≥ 3 months of neuropathic pain (NP), either painful diabetic peripheral neuropathy (pDPN) or post-herpetic neuralgia (PHN); (ii) were receiving medications treating NP; and (iii) had completed the EQ-5D and PI-NRS-11. We explored indirect and direct mapping approaches. The indirect method took a probabilistic approach using ordered logistic models (OLMs) predicting response levels for each EQ-5D item via repeated Monte Carlo simulations before computing utilities. The direct approach simply predicted EQ-5D utilities directly using ordinary least squares (OLS). Categorical scores of PI-NRS-11 were used as the predictors. Patient age, gender, and pain duration were additionally controlled in the full model specification. Seventy percent of the data were used for estimation and 30% for prediction. Mean square errors (MSEs) and 95% confidence intervals (CIs) of prediction errors were reported. A total of 2719 respondents were included. Mean (SD) age was 55.48 (10.65) years and 56.23% were female. Average NP duration was 61 months and 58% gave scores ≥ 6 on the PI-NRS-11. The clinical pain scores were significantly associated with all EQ-5D items, especially with the 'pain/discomfort' item (p 0.2. Findings suggest that EQ-5D utilities or item responses could be estimated on the basis of NP scores. Independent testing of the external validity of the mapping algorithms developed herein is encouraged.

## P099b4bfedca4

- Year: 2014
- Linked people: Ciaran O'Neill
- Title: Evaluating Direct Medical Expenditures Estimation Methods of Adults Using the Medical Expenditure Panel Survey: An Example Focusing on Head and Neck Cancer

Abstract:

Objective To inform policymakers of the importance of evaluating various methods for estimating the direct medical expenditures for a low-incidence condition, head and neck cancer (HNC). Methods Four methods of estimation have been identified: 1) summing all health care expenditures, 2) estimating disease-specific expenditures consistent with an attribution approach, 3) estimating disease-specific expenditures by matching, and 4) estimating disease-specific expenditures by using a regression-based approach. A literature review of studies (2005-2012) that used the Medical Expenditure Panel Survey (MEPS) was undertaken to establish the most popular expenditure estimation methods. These methods were then applied to a sample of 120 respondents with HNC, derived from pooled data (2003-2008). Results The literature review shows that varying expenditure estimation methods have been used with MEPS but no study compared and contrasted all four methods. Our estimates are reflective of the national treated prevalence of HNC. The upper-bound estimate of annual direct medical expenditures of adult respondents with HNC between 2003 and 2008 was $3.18 billion (in 2008 dollars). Comparable estimates arising from methods focusing on disease-specific and incremental expenditures were all lower in magnitude. Attribution yielded annual expenditures of $1.41 billion, matching method of $1.56 billion, and regression method of $1.09 billion. Conclusions This research demonstrates that variation exists across and within expenditure estimation methods applied to MEPS data. Despite concerns regarding aspects of reliability and consistency, reporting a combination of the four methods offers a degree of transparency and validity to estimating the likely range of annual direct medical expenditures of a condition.

## P75339c6d635f

- Year: 2026
- Linked people: Fredrick Purba
- Title: The EQ-5D-5L valuation study in Nigeria

Abstract:

PURPOSE: A country-specific EQ-5D-5L value set ensures that health utility estimates reflect national preferences, enabling contextually appropriate health technology assessment (HTA) to inform efficient resource allocation decisions. This study aimed to develop the first EQ-5D-5L value set for Nigeria. METHODS: Adult Nigerians were recruited from 12 states using multi-stage stratified quota sampling based on age, sex, and education. Face-to-face interviews were conducted through Computer-Assisted Personal Interviews using the EQ-PVT protocol. The interview comprises 2 main parts: composite time-trade-off (cTTO) and discrete choice experiment (DCE) tasks. The cTTO data were modelled using random intercept, Tobit, linear (heteroskedasticity-corrected), and Tobit (heteroskedasticity-corrected) models. DCE data were analyzed using Mixed Logit Model (MLM). Hybrid models combining the cTTO and DCE data were also estimated. RESULTS: A total of 1,200 interviews were conducted. The Hybrid Tobit model with intercept, corrected for heteroscedasticity, and excluded flagged responses was considered the preferred model. The utility values of the best (11,111), 2nd best (21,111), worst (55,555), and 2nd worst (54,555) health states are 1, 0.963, - 0.733, and - 0.653, respectively. The most important dimension is Pain/Discomfort followed by Anxiety/Depression, Mobility, Usual Activity, and Self-care, respectively. CONCLUSION: This study provides the first EQ-5D-5L value set for Nigeria, derived from a representative adult population. This value set provides a strong foundation for HTA, supporting evidence-informed policy decisions and advancing progress towards Universal Health Coverage (UHC) in Nigeria and the wider West African region.

## P4bbb249162d3

- Year: 2012
- Linked people: Ben Van Hout
- Title: A COMPARISON OF ALTERNATIVE VARIANTS OF THE LEAD AND LAG TIME TTO

Abstract:

'Lead Time' TTO improves upon conventional TTO by providing a uniform method for eliciting positive and negative values. This research investigates (i) the values generated from different combinations of time in poor health and in full health; and the order in which these appear (lead vs. lag); (ii) whether values concur with participants' views about states; (iii) methods for handling extreme preferences. n = 208 participants valued five EQ-5D states, using two of four variants. Combinations of lead time and health state duration were: 10 years and 20 years; 5 years and 1 year; 5 years and 10 years; and a health state duration of 5 years with a lag time of 10 years. Longer lead times capture more preferences, but may involve a framing effect. Lag time results in less non-trading for mild states, and less time being traded for severe states. Negative values broadly agree with participants' stated opinion that the state is worse than dead. The values are sensitive to the ratio of lead time to duration of poor health, and the order in which these appear (lead vs. lag). It is feasible to handle extreme preferences though challenges remain.

## P4512f87b33d2

- Year: 2021
- Linked people: Ciaran O'Neill
- Title: A Review to Populate A Proposed Cost-Effectiveness Analysis of Glaucoma Screening in Sub-Saharan Africa

Abstract:

To populate a proposed cost-effectiveness analysis of glaucoma screening in Sub-Saharan Africa (SSA).A complete search was conducted on PubMed, Medline and African Journals Online (AJOL) to obtain relevant published articles, which were included in this review. All relevant articles on prevalence of glaucoma in SSA and among other African-derived populations, severity of glaucoma, cost of diagnosis and management, clinical effectiveness of glaucoma screening and treatment and the different glaucoma screening strategies in SSA were reviewed.Population screening interventions for glaucoma may be considered as follows: standalone screening for glaucoma, screening for glaucoma during cataract outreach, and screening incorporated with diabetic retinopathy image review using tele-ophthalmology. Our review suggests that cost of glaucoma treatment is relatively low with cost of medical treatment ranging from USD 273 to USD 480 per year/patient and surgical treatment cost of USD 283 per patient as with other developing countries. Compliance with medication is moderate to good in about 50% of glaucoma patients. Prevalence of glaucoma is much higher in SSA and almost 50% of glaucoma patients are blind in at least one eye at presentation in clinics (without outreach screening). Our review suggests a moderate sensitivity and specificity in identifying glaucoma with basic equipment (direct ophthalmoscope, contact tonometer and frequency doubling technology) during outreach screening although about a third or fewer take up glaucoma services in clinics.Our review provides the necessary information to conduct a cost-effective analysis of glaucoma screening in SSA using the decision Markov model.

## P80d13ed3ef16

- Year: 2018
- Linked people: Ciaran O'Neill
- Title: The health of the residents of Ireland: Population norms for Ireland based on the EQ-5D-5L descriptive system – a cross sectional study

Abstract:

Background: The EQ-5D descriptive system has become a widely used generic instrument to measure population health. In this study we use the EQ-5D-5L system to describe the health of residents in Ireland in 2015/16 and examine relationships between health and a range of socio-demographic characteristics. Methods: A representative sample of residents in Ireland was established in a two-stage random sampling exercise in 2015/16. Self-reported health, together with a range of socio-demographic characteristics, were collected using a computer-assisted-personal-interview survey. Self-reported health was captured using the EQ-5D-5L descriptive system including a visual analogue scale. Data were presented as descriptive statistics and analysed using a general linear regression model and ordered logistic regression models in the case of specific health domains. Socio-economic gradients in health were also examined using concentration curves and indices. Results : A usable sample of 1,131 individuals provided responses to all questions in the survey. The population in general reported good health across the five domains with roughly 78%, 94%, 81%, 60% and 78% reporting no problems with mobility, self-care, usual activities, pain/discomfort and anxiety/depression respectively. Differences in health with respect to age, and socio-economic status were evident; those who were older, less well-educated of lower income and without private health insurance reported poorer health. Differences in health between groups differentiated by socio-economic status varied across domains of health, and were dependent on the measure of socio-economic status used. Conclusion: Residents of Ireland appear to rate their health as relatively good across the various domains captured by the EQ-5D-5L system. A pro-affluent gradient in self-reported health is evident though the sharpness of that gradient varies between domains of health and the measures of socio-economic status used. The study provides baseline data against which the health of the population can be measured in the future as demography and economic conditions change.

## P01a1f791f782

- Year: 2019
- Linked people: Ben Van Hout
- Title: Health-related quality of life and mortality in patients with pulmonary embolism: a prospective cohort study in seven European countries

Abstract:

PURPOSE: Little is known about the quality of life following pulmonary embolism (PE). The aim of the study was to assess the 12-month illness burden in terms of health-related quality of life (HrQoL) and mortality, in relation to differences in patient characteristics. METHODS: The PREFER in VTE registry, a prospective, observational study conducted in seven European countries, was used. Within 2 weeks following an acute symptomatic PE, patients were recruited and followed up for 12 months. Associations between patient characteristics and HrQoL (EQ-5D-5L) and mortality were examined using a regression approach. RESULTS: Among 1399 PE patients, the EQ-5D-5L index score at baseline was 0.712 (SD 0.265), which among survivors gradually improved to 0.835 (0.212) at 12 months. For those patients with and without active cancer, the average index score at baseline was 0.658 (0.275) and 0.717 (0.264), respectively. Age and previous stroke were significant factors for predicting index scores in those with/without active cancer. Bleeding events but not recurrences had a noticeable impact on the HrQoL of patients without active cancer. The 12-month mortality rate post-acute period was 8.1%, ranging from 1.4% in Germany, Switzerland, and Austria to 16.8% in Italy. Mortality differed between patients with active cancer and those without (42.7% vs. 4.7%). CONCLUSION: PE is associated with a substantial decrease in HrQoL at baseline which normalizes following treatment. PE is associated with a high mortality rate especially in patients with cancer, with significant country variation. Bleeding events, in particular, impact the burden of PE.

## P3e2170e62c8b

- Year: 2022
- Linked people: Elly Stolk
- Title: Modifying the Composite Time Trade-Off Method to Improve Its Discriminatory Power.

Abstract:

In cost-effectiveness analysis of health technologies, health state utilities are needed. They are often elicited with a composite time trade-off (cTTO) method, particularly for the widely used EQ-5D-5L. Unfortunately, cTTO discriminatory power is hindered by (1) respondents' nontrading (NT) of time for quality, (2) censoring of utilities at -1, and (3) poor correlation of negative utilities with state severity. We investigated whether modifying cTTO can mitigate these effects. We interviewed online 478 students (February to April, 2021) who each valued the same 10 EQ-5D-5L health states in 1 of 3 arms. Arm A used a standard cTTO, expanded with 2 questions to explore reasons for NT and censoring. Arms B and C used a time trade-off with modified alternatives offered to overcome loss aversion, to unify the tasks for positive and negative utilities, and to enable eliciting utilities < -1. In arms B and C, we observed less NT than in A (respectively, 4% and 4% vs 10%), more strictly negative utilities (38% and 40% vs 25%), and more utilities ≤ -1 (18% and 30% vs 10%). The average utility of state 55555 dropped to -2.15 and -2.52 from -0.53. Enabling finer trades in arm A reduced NT by 70%. Arms B and C yielded an intuitive association between negative utilities and state severity. These arms were considered more difficult and resulted in more inconsistencies. The discriminatory power of cTTO can be improved, but it may require increasing the difficulty of the task. The standard cTTO may overestimate the utilities, especially of severe states.

## Pf03eadc4f6ab

- Year: 2023
- Linked people: Gerard De Pouvourville
- Title: Population norms in France with EQ-5D-5L: health states, value indexes, and VAS

Abstract:

To provide EuroQoL EQ-5D-5L French population norms based on a sample of 15,000 responders. Based on the National Health and Wellness Survey, an international, annual, selfadministered Internet-based survey, this study extracted data from France for 2018 involving a sample of 15,000 respondents stratified by age and gender. Responses to the EQ-5D-5L questionnaire and the Visual Analog Scale (VAS) score, together with sociodemographic, health behavior, and disease status variables were collected. VAS, value indexes, the level sum score, and the distribution of levels per dimension were described. Multivariate regression analyses were performed to identify covariates with a statistically significant effect on the five dimensions and the three scores. The mean [standard deviation (SD)] VAS was 73.4 (22.2) for the entire sample (male 74.8 vs female 72.2, p < 0.0001). The Mean SD value index was 0.905 (0.158) (male 0.915 vs female 0.895, p < 0.0001). The mean SD level sum score was 7.6 (3.0) (7.4 for males vs. 7.9 for females p < 0.0001). Health state 11,111 (no problem in any dimension) represented 25.1% of all responses. "No problem" responses' proportions were Self Care (91.3%), Usual Activities (74.2%), Mobility (72.4%), Anxiety/Depression (52.6%) and Pain/Discomfort (37.7%). Multivariate regressions revealed a significant relationship for health states, value indexes, and VAS with age, income, employment, marital status, smoking and alcohol consumption, obesity, and the presence of one or more health problems. Based on a large sample, this study is the first to report EQ-5D-5L population norms for France.

## Pa27a1d67c33b

- Year: 2021
- Linked people: Philip Powell
- Title: Deriving a Preference-Based Measure for People With Duchenne Muscular Dystrophy From the DMD-QoL

Abstract:

OBJECTIVES: This study generates a preference-based measure for capturing the quality of life of people with Duchenne muscular dystrophy (DMD) from a new measure of quality of life, DMD-QoL. METHODS: A health state classification system was derived from the DMD-QoL based on psychometric performance of items, factor analysis, and item response theory analysis. Preferences for health states described by the classification system were elicited using an online discrete choice experiment survey with life years as an additional attribute, from members of the UK general population (n = 1043). Discrete choice experiment data was modeled using a conditional fixed-effects logit model and utility estimates were directly anchored on the 1 to 0 full health-dead scale. RESULTS: The health state classification system has 8 dimensions: mobility, difficulty using hands, difficulty breathing, pain, tiredness, worry, participation, and feeling good about yourself. The standard model had mostly statistically significant coefficients and reflected the instrument's monotonic structure. However, 2 dimensions had inconsistent coefficients (where utility increased as health worsened) and a consistent model was estimated that merged adjacent inconsistent severity levels. The best state defined by the classification system has a value of 1 and the worst state has a value of -0.559. CONCLUSION: The modeled results enable DMD-QoL-8D utility values to be generated using DMD-QoL or DMD-QoL-8D data to generate QALYs for people with DMD. QALYs can then be used to inform economic models of the cost-effectiveness of interventions in DMD. Future research comparing the psychometric performance of DMD-QoL-8D to existing generic preference-based measures, including EQ-5D-5L, is recommended.

## Pb599996d5562

- Year: 2013
- Linked people: Elly Stolk
- Title: The effects of lead time and visual aids in TTO valuation: A study of the EQ-VT framework

Abstract:

BACKGROUND: The effect of lead time in time trade-off (TTO) valuation is not well understood. The purpose of this study was to investigate the effects on health-state valuation of the length of lead time and the way the lead-time TTO task is displayed visually. METHODS: Using two general population samples, we compared three lead-time TTO variants: 10 years of lead time in full health preceding 5 years of unhealthy time (standard); 5 years of lead time preceding 5 years of unhealthy time (experimental); and 10 years of lead time and 5 years of unhealthy time, presented with a visual aid to highlight the point where the lead time ends (experimental). Participants were randomized to receive one of the lead-time variants, as administered by a computer software program. RESULTS: Health-state values generated by TTO valuation tasks using a longer lead time were slightly lower than those generated by tasks using a shorter lead time. When lead time and unhealthy time were presented with visual aids highlighting the difference between the lead time and unhealthy time, respondents spent more time considering health states with a value close to 0. CONCLUSIONS: Different lead-time time trade-off variants should be carefully studied in order to achieve the best measurement of health-state values using this new method.

## Pe58cce429ea9

- Year: 2017
- Linked people: Margreet Franken
- Title: Cost-effectiveness of capecitabine and bevacizumab maintenance treatment after first-line induction treatment in metastatic colorectal cancer.

Abstract:

Capecitabine and bevacizumab (CAP-B) maintenance therapy has shown to be more effective compared with observation in metastatic colorectal cancer patients achieving stable disease or better after six cycles of first-line capecitabine, oxaliplatin, bevacizumab treatment in terms of progression-free survival. We evaluated the cost-effectiveness of CAP-B maintenance treatment. Decision analysis with Markov modelling to evaluate the cost-effectiveness of CAP-B maintenance compared with observation was performed based on CAIRO3 study results (n = 558). An additional analysis was performed in patients with complete or partial response. The primary outcomes were the incremental cost-effectiveness ratio (ICER) defined as the additional cost per life year (LY) and quality-adjusted life years (QALY) gained, calculated from EQ-5D questionnaires and literature and LYs gained. Univariable sensitivity analysis was performed to assess the influence of input parameters on the ICER, and a probabilistic sensitivity analysis represents uncertainty in model parameters. CAP-B maintenance compared with observation resulted in 0.21 QALYs (0.18LYs) gained at a mean cost increase of €36,845, yielding an ICER of €175,452 per QALY (€204,694 per LY). Varying the difference in health-related quality of life between CAP-B maintenance and observation influenced the ICER most. For patients achieving complete or partial response on capecitabine, oxaliplatin, bevacizumab induction treatment, an ICER of €149,300 per QALY was calculated. CAP-B maintenance results in improved health outcomes measured in QALYs and LYs compared with observation, but also in a relevant increase in costs. Despite the fact that there is no consensus on cost-effectiveness thresholds in cancer treatment, CAP-B maintenance may not be considered cost-effective.

## P9f850f38893d

- Year: 2017
- Linked people: Piyameth Dilokthornsakul
- Title: Cost-effectiveness of dipeptidyl peptidase-4 inhibitor monotherapy versus sulfonylurea monotherapy for people with type 2 diabetes and chronic kidney disease in Thailand

Abstract:

OBJECTIVE: With a high prevalence of chronic kidney disease (CKD) in type 2 diabetes (T2DM) in Thailand, the appropriate treatment for the patients has become a major concern. This study aimed to evaluate long-term cost-effective of dipeptidyl peptidase-4 (DPP-4) inhibitor monothearpy vs sulfonylurea (SFU) monotherapy in people with T2DM and CKD. METHODS: A validated IMS CORE Diabetes Model was used to estimate the long-term costs and outcomes. The efficacy parameters were identified and synthesized using a systematic review and meta-analysis. Baseline characteristics and cost parameters were obtained from published studies and hospital databases in Thailand. Costs were expressed in 2014 US Dollars. Outcomes were presented as an incremental cost-effectiveness ratio (ICER). One-way and probabilistic sensitivity analyses were performed to estimate parameter uncertainty. RESULTS: From a societal perspective, treatment with DPP-4 inhibitors yielded more quality-adjusted life years (QALYs) (0.024) at a higher cost (>66,000 Thai baht (THB) or >1,829.27 USD) per person than SFU, resulting in the ICER of >2.7 million THB/QALY (>74,833.70 USD/QALY). The cost-effectiveness results were mainly driven by differences in HbA1c reduction, hypoglycemic events, and drug acquisition cost of DPP-4 inhibitors. At the ceiling ratio of 160,000 THB/QALY (4,434.59 USD/QALY), the probability that DPP-4 inhibitors are cost-effective compared to SFU was less than 10%. CONCLUSIONS: Compared to SFU, DPP-4 inhibitor monotherapy is not a cost-effective treatment for people with T2DM and CKD in Thailand.

## Pe8f86ffb599b

- Year: 2022
- Linked people: Elly Stolk
- Title: Reliability and validity of using EQ-5D-5L among healthy and adolescents with major mental health disorders in Ethiopia.

Abstract:

The EQ-5D is a validated and widely used generic measure of health-related quality of life (HRQoL) in both healthy individuals and those with various medical conditions. The objective of this study was to test whether EQ-5D-5L is reliable and valid for use among school sample adolescents and those with major mental health disorders in Ethiopia. Participants were recruited from ten sub-districts comprising the Butajira Rural Health Programme (BRHP) and Butajira major mental health disorders center. Data were collected using an Amharic (Ethiopia) EQ-5D-5L self-complete-paper and the questionnaire was administered 10 days after the first completion for test-retest procedures. Two-way mixed-effects models absolute intraclass correlation coefficient (ICC) was used to test reliability of the instrument while Kruskal-Wallis rank test with pairwise comparison was used to assess the known group validity of the instrument. There were 501 (201 school sample and 300 adolescents with major mental health disorders) participants recruited and 497 were included in the sample for analysis. The ICC was high (ICC > 0.7, p < 0.001) for all EQ-5D-5L dimensions, EQ-5D-5L utility index and EQ-VAS scores. The findings revealed that the Amharic EQ-5D-5L has significant known group validity as shown by the difference in scores among various disease group (depression, schizophrenia, and bipolar) and experience of chronic illness. The results shows that the Amharic EQ-5D-5L is reliable and valid instrument for the measurement of HRQoL among adolescent populations in Ethiopia.

## Pd7fdee484959

- Year: 2019
- Linked people: Ciaran O'Neill
- Title: A pilot study of the duration of GP consultations in Ireland

Abstract:

BACKGROUND: General practitioner (GP)-led primary care is the linchpin of health care in Ireland. Reflecting international trends, there are increasing concerns about the sustainability of the current Irish GP service due to an increasing workload. Objective data on the duration of GP consultations are currently not available in Ireland. The objective of this pilot study is to demonstrate how the duration of consultations can be collected, using readily available administrative data. METHODS: = 3) comprising 15 GPs were recruited from a university-affiliated research network. A retrospective analysis of GP consultations with patients with diabetes for the 9 years between 2010 and 2018 was used to assess the feasibility of using this system to measure the duration of consultations. RESULTS: The average duration of a consultation was 14.1 min for the 9 years spanning 2010 to 2018. Patients had an average time between consultations of 99 days. CONCLUSIONS: This pilot study confirms that an administrative data set can be utilised at negligible cost to monitor GP practice consultation workload over time. Our preliminary pilot data show that GP consultation durations among participating practices were longer than the 5-11.7 min reported in the UK and show an increase over the period. Clearly, a larger number of practices and patients are required to substantiate this finding.

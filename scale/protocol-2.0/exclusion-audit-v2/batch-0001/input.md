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

## Pecf17c687687

- Year: 2022
- Linked people: Deborah Marshall
- Title: Rural-Urban Differences in Non-Local Primary Care Utilization among People with Osteoarthritis: The Role of Area-Level Factors.

Abstract:

The utilization of non-local primary care physicians (PCP) is a key primary care indicator identified by Alberta Health to support evidence-based healthcare planning. This study aims to identify area-level factors that are significantly associated with non-local PCP utilization and to examine if these associations vary between rural and urban areas. We examined rural-urban differences in the associations between non-local PCP utilization and area-level factors using multivariate linear regression and geographically weighted regression (GWR) models. Global Moran's I and Gi* hot spot analyses were applied to identify spatial autocorrelation and hot spots/cold spots of non-local PCP utilization. We observed significant rural-urban differences in the non-local PCP utilization. Both GWR and multivariate linear regression model identified two significant factors (median travel time and percentage of low-income families) with non-local PCP utilization in both rural and urban areas. Discontinuity of care was significantly associated with non-local PCP in the southwest, while the percentage of people having university degree was significant in the north of Alberta. This research will help identify gaps in the utilization of local primary care and provide evidence for health care planning by targeting policies at associated factors to reduce gaps in OA primary care provision.

## Pefe012857ece

- Year: 2023
- Linked people: Matthijs Versteegh, Maureen Rutten-van Molken
- Title: Lessons learned from the application of the HEcoPerMed guidance to three modeling case studies.

Abstract:

Background: The HEcoPerMed consortium developed a methodological guidance for the harmonization and improvement of economic evaluations in personalized medicine. Materials & methods: In three therapeutic areas, health economic models were developed to scrutinize the recommendations of the guidance. Results: Altogether, 20 of the 23 recommendations of the guidance were addressed by the models. Seven recommendations were applied in all studies, six in two of the studies and seven in one of the studies. Recommendations with an essential role on the final conclusions of the analyses were identified in each study. Conclusion: The guidance was found to be best used as a tool to identify and prioritize issues, verify solutions and justify decisions during the economic analysis of personalized interventions.

## P710cc558ee3d

- Year: 2024
- Linked people: Zhuxin Mao
- Title: Invasive‐plant traits, native‐plant traits, and their divergences as invasion factors

Abstract:

Abstract Invasive plants exert significant ecological impacts on native plants, communities, and ecosystems. However, consistent conclusions regarding how traits of invasive plants, native plants, and their divergences affect invasion dynamics are still lacking. Here, we conducted a pairwise common garden experiment to investigate how invasion was influenced not only by invasive plants but also by native plants, aiming to elucidate the role of invasive‐plant traits, native‐plant traits, and their divergences in invasion processes. Our findings revealed variations in invasive stage depending on the combinations of invasive and native plants. Specifically, native plants such as A. argyi , A. lavandulifolia , and C. album exhibited competitive superiority when co‐occurring with the three invasive plants. S. viridis , A. vestita , and A. annua had competitive superiority when they co‐occurred with E. canadensis , G. quadriradiata , and E. annuus respectively. Furthermore, our results demonstrated that the competitive abilities of invasive plants were primarily influenced by factors such as height, diameter, and biomass allocation, while native plants' competitive abilities were mainly affected by diameter, biomass allocation, and function group differences. Moreover, our analysis revealed that invasive‐plant traits, native‐plant traits, their divergences, and their interactions together explained 36.88% of the variation in invasion dynamics, with invasive‐plant traits and the native‐plant traits explaining 10.19% and 6.88%, respectively. In conclusion, the traits of invasive and native plants, along with their divergences, significantly influence interspecific relationships, and influencing the invasive stages. Divergences in competitive strategies between the native plants and invasive plants facilitated invasion processes. Our study not only contributes to understanding the mechanisms underlying invasion, but also provides a scientific foundation for predicting and managing the negative effects of invasive plants.

## P0341e97c1654

- Year: 2021
- Linked people: Kim Dalziel
- Title: Protocol for a randomised clinical trial of multimodal postconcussion symptom treatment and recovery: the Concussion Essentials study

Abstract:

INTRODUCTION: While most children recover from a concussion shortly after injury, approximately 30% experience persistent postconcussive symptoms (pPCS) beyond 1-month postinjury. Existing research into the treatment of pPCS have evaluated unimodal approaches, despite evidence suggesting that pPCS likely represent an interaction across various symptom clusters. The primary aim of this study is to evaluate the effectiveness of a multimodal, symptom-tailored intervention to accelerate symptom recovery and increase the proportion of children with resolved symptoms at 3 months postconcussion. METHODS AND ANALYSIS: In this open-label, assessor-blinded, randomised clinical trial, children with concussion aged 8-18 years will be recruited from The Royal Children's Hospital (The RCH) emergency department, or referred by a clinician, within 17 days of initial injury. Based on parent ratings of their child's PCS at ~10 days postinjury, symptomatic children (≥2 symptoms at least 1-point above those endorsed preinjury) will undergo a baseline assessment at 3 weeks postinjury and randomised into either Concussion Essentials (CE, n=108), a multimodal, interdisciplinary delivered, symptom-tailored treatment involving physiotherapy, psychology and education, or usual care (UC, n=108) study arms. CE participants will receive 1 hour of intervention each week, for up to 8 weeks or until pPCS resolve. A postprogramme assessment will be conducted at 3 months postinjury for all participants. Effectiveness of the CE intervention will be determined by the proportion of participants for whom pPCS have resolved at the postprogramme assessment (primary outcome) relative to the UC group. Secondary outcome analyses will examine whether children receiving CE are more likely to demonstrate resolution of pPCS, earlier return to normal activity, higher quality of life and a lower rate of utilisation of health services, compared with the UC group. ETHICS AND DISSEMINATION: Ethics were approved by The RCH Human Research Ethics Committee (HREC: 37100). Parent, and for mature minors, participant consent, will be obtained prior to commencement of the trial. Study results will be disseminated at international conferences and international peer-reviewed journals. TRIAL REGISTRATION NUMBER: ACTRN12617000418370; pre-results.

## P36b7c6aa1f68

- Year: 2022
- Linked people: Nyantara Wickramasekera
- Title: Surgeon preference for treatment allocation in older people facing major gastrointestinal surgery: an application of the discrete choice experiment methodology

Abstract:

AIM: Variation in major gastrointestinal surgery rates in the older population suggests heterogeneity in surgical management. A higher prevalence of comorbidities, frailty and cognitive impairments in the older population may account for some variation. The aim of this study was to determine surgeon preference for major surgery versus conservative management in hypothetical patient scenarios based on key attributes. METHOD: A survey was designed according to the discrete choice methodology guided by a separate qualitative study. Questions were designed to test for associations between key attributes (age, comorbidity, urgency of presentation, pathology, functional and cognitive status) and treatment preference for major gastrointestinal surgery versus conservative management. The survey consisting of 18 hypothetical scenarios was disseminated electronically to UK gastrointestinal surgeons. Binomial logistic regression was used to identify associations between the attributes and treatment preference. RESULTS: In total, 103 responses were received after 256 visits to the questionnaire site (response rate 40.2%). Participants answered 1847 out of the 1854 scenarios (99.6%). There was a preference for major surgery in 1112/1847 (60.2%) of all scenarios. Severe comorbidities (OR 0.001, 95% CI 0.000-0.030; P = 0.000), severe cognitive impairment (OR 0.001, 95% CI 0.000-0.033; P = 0.000) and age 85 years and above (OR 0.028, 95% CI 0.005-0.168; P = 0.000) were all significant in the decision not to offer major gastrointestinal surgery. CONCLUSION: This study has demonstrated variation in surgical treatment preference according to key attributes in hypothetical scenarios. The development of fitness-stratified guidelines may help to reduce variation in surgical practice in the older population.

## P3d924237bc9a

- Year: 2021
- Linked people: Gerard De Pouvourville
- Title: Cost-Effectiveness Analysis of SAPIEN 3 Transcatheter Aortic Valve Implantation Procedure Compared With Surgery in Patients With Severe Aortic Stenosis at Low Risk of Surgical Mortality in France

Abstract:

OBJECTIVES: The clinical and cost-saving benefits of transcatheter aortic valve implantation (TAVI) over surgical aortic valve replacement (SAVR) in patients with severe aortic stenosis who are at high or intermediate risk of surgical mortality are supported by a growing evidence base. The PARTNER 3 trial (Placement of AoRTic TraNscathetER Valve Trial) demonstrated clinical benefits with SAPIEN 3 TAVI compared with SAVR in selected patients at low risk of surgical mortality. This study uses PARTNER 3 outcomes in combination with a French national hospital claim database to inform a cost-utility model and examine the cost implications of TAVI over SAVR in a low-risk population. METHODS: A 2-stage cost-utility analysis was developed to estimate changes in both direct healthcare costs and health-related quality of life using TAVI with SAPIEN 3 compared with SAVR. Early adverse events associated with TAVI were captured using the PARTNER 3 data set. These data fed into a Markov model that captured longer-term outcomes of patients, after TAVI or SAVR intervention. RESULTS: TAVI with SAPIEN 3 offers meaningful benefits over SAVR in providing both cost saving (€12 742 per patient) and generating greater quality-adjusted life-years (0.89 per patient). These results are robust with TAVI with SAPIEN 3 remaining dominant across several scenarios and deterministic and probabilistic sensitivity analyses. CONCLUSIONS: This model demonstrated that TAVI with SAPIEN 3 was dominant compared with SAVR in the treatment of patients with severe symptomatic aortic stenosis who are at low risk of surgical mortality. These findings should help policy makers in developing informed approaches to intervention selection for this patient population.

## P6268eed3ad97

- Year: 2022
- Linked people: Nyantara Wickramasekera
- Title: Patient preferences for treatment in steroid resistant ulcerative colitis - a discrete-choice experiment.

Abstract:

BACKGROUND AND AIM: Understanding treatment preferences in those patients who are not responding to corticosteroids for ulcerative colitis is important in informing treatment choices. This study aimed to assess the relative importance of treatment characteristics to patients by conducting a discrete-choice experiment. METHODS: Patients completed the questionnaire online. All data were collected between September and December 2020. Participants were shown 13 discrete-choice experiment tasks - a series of side-by-side comparisons of competing, hypothetical treatment characteristics and asked to select a preferred treatment. Survey responses were analysed using descriptive statistics and regression analyses. RESULTS: 115 patients completed the study. Patient preferences were strongest for treatments with a lower chance of side effects, this attribute had the most influence on the choice of treatment patients preferred. The second most important attribute was an improvement in maintaining remission. Conversely, route and frequency of administration were least important on the choice of treatment patients preferred. Respondents were willing to make trade offs and accept treatment benefits to compensate them for receiving a treatment with a less desirable attribute level. Participants were willing to accept a larger benefit of 45% improvement in maintenance of remission to accept a treatment with a higher probability of side effects. The benefit required was smaller with a 10% improvement in remission required to accept a treatment with a lower probability of side effects. CONCLUSION: Quantifying preferences helps to identify and prioritise treatment characteristics that are important to patients. The results highlight the importance of careful discussion of side effects, including the magnitude of risk, using visualisation tools during a patient consultation to support decisions.

## Pd92df6e63616

- Year: 2026
- Linked people: Wolfgang Greiner
- Title: Development Process of a Clinical Decision Support System for Empiric Antibiotic Therapies in Patients With Sepsis: Case Study.

Abstract:

Background: Antibiotic therapies are the main treatment for bacterial infections, but growing antibiotic resistance is a major global health threat, severely impacting patients with sepsis. Rapid selection of the most effective antibiotic therapy is critical for survival and for preventing further resistance. Physicians must consider numerous factors for proper empiric treatment selection. A clinical decision support system (CDSS) aims to support physicians in this process, facilitating rapid and targeted therapy. Objective: The purpose of this work is to explore the extent to which the realization of a CDSS is possible based on the data available to us and to document insights gained during the development of a foundational model designed to assist physicians in determining empiric treatment options for patients with sepsis. In this regard, rather than aiming to develop a CDSS for clinical application, we highlight the importance of close interprofessional collaboration between scientists from various disciplines and analyze the effects of data quality and quantity on the performance of our statistical models. Methods: Empirical scientists conducted interviews with medical practitioners to acquire the medical knowledge required to develop sound statistical models. We developed and applied 2-step cross-sectional, as well as time-series classification models, to carefully preprocessed data of patients with sepsis admitted to the intensive care unit of a German hospital. Results: We identified several factors as crucial information for valid decisions on empiric therapy for treating patients with sepsis. These include the patients' core data, especially the infection focus. To prevent further resistance, individual risk factors such as travel history and professional background should be considered. The evaluation of a therapy's effectiveness is mainly based on the patient's general condition and blood values such as procalcitonin and interleukin 6. One key factor in the acceptance of a CDSS is the explainability of the results produced by the applied methods. Our models demonstrated mainly weak predictive ability for all considered empiric antibiotic therapies. However, they are not yet suitable for use in clinical practice, especially as they are based on prescribing habits rather than on optimal treatment decisions. Conclusions: This work highlights the importance of interprofessional collaboration between medical experts and model developers, ensuring that data quality and clinical relevance are central to the process. It emphasizes the urgent need for high-quality, comprehensive data to overcome challenges such as data discontinuity and improve model performance, particularly through enhanced digitization in health care. This feasibility study will facilitate future efforts to develop a CDSS for treating patients with sepsis and to translate it into clinical use.

## P89369eea67bd

- Year: 2025
- Linked people: Elske van den Akker-van Marle
- Title: Cost analysis of intrauterine balloon tamponade versus uterine artery embolization in the management of persistent postpartum hemorrhage

Abstract:

OBJECTIVE: The aim of this study was to compare the cost of a strategy initially resorting to intrauterine balloon tamponade versus a strategy initially resorting to uterine artery embolization in the management pathway of persistent postpartum hemorrhage. METHODS: This was a propensity score-matched cohort study including women who were subsequently treated with (scenario 1) versus uterine artery embolization (scenario 2) in order to control PPH, defined as postpartum bleeding that was resistant to first-line treatment. We compared these two scenarios in terms of cost. These were based on costs of intervention, blood products transfused, and intensive care unit admission. We calculated the mean cost difference between the scenarios per woman. RESULTS: The propensity score-matched cohort comprised 50 women per scenario. In scenario 1, intrauterine balloon tamponade was successful in 29 women (58%), with a mean cost per patient of €7060 (standard deviation [SD], €2846). In scenario 2, uterine artery embolization was successful in 42 women (84%), with mean cost per patient of €7122 (SD, €2918). In each scenario, six women (12%) underwent a peripartum hysterectomy. The difference in mean cost per woman between the two scenarios was €62 in favor of scenario 1. CONCLUSION: There is a negligible difference in cost between scenarios in which women with PPH are initially managed with intrauterine balloon tamponade versus uterine artery embolization. Given the comparable cost and maternal outcomes, intrauterine balloon tamponade is a favorable treatment, considering its less invasive nature, practical considerations, and lower risk of complications.

## Pde0b680a6a59

- Year: 2023
- Linked people: Zhuxin Mao
- Title: What is the relationship between health-related quality of life among scoliosis patients and their caregiver burden? A cross-sectional study in China

Abstract:

BACKGROUND: Caregivers play a vital role in the recovery of scoliosis patients, but limited studies evaluate the caregivers' HRQoL and burden in health care. This study aimed to explore the health-related quality of life (HRQoL) of scoliosis patients and their caregivers, and identify the factors influencing caregiver burden in Eastern China. METHODS: This cross-sectional study was conducted from August 2018 to January 2019 at the Shandong Provincial Hospital, Jinan, China. The HRQoL of scoliosis patients was measured by the Scoliosis Research Society-22r (SRS-22r), five-level EQ-5D (EQ-5D-5L) and Child Health Utility 9D (CHU9D). The caregivers' questionnaires consist of the EQ-5D-5L, WHO-five wellbeing index (WHO-5), 22-item Zarit Caregiver Burden Interview (ZBI-22) and Social Support Rating Scale (SSRS). Spearman correlation coefficients were used to estimate the relationship among caregivers' burden, social support, HRQoL, and SWB. Cohen's effect size (Cohen's d) was used to assess the ZBI-22 total score between different groups. Multiple stepwise hierarchical linear regression models were conducted to assess the associated factors of caregiver burden. RESULTS: There were 59 scoliosis patients and their caregivers (n = 59) included in the analysis. The mean health state utility of adolescent scoliosis patients (n = 39) was 0.718 (95%CI: 0.654, 0.782) based on CHU9D and adult scoliosis patients (n = 20) was 0.663 (95%CI: 0.471, 0.855) based on EQ-5D-5L. The mean health state utility of male scoliosis patients (0.792/0.667) was higher than females (0.681/0.662) based on CHU9D and EQ-5D-5L (p > 0.05), respectively. The ZBI-22 total score of scoliosis patients' caregivers was 27.86 (SD: 20.59). Scoliosis patients' HRQoL was significantly inversely correlated with caregiver burden, and the HRQoL and subjective wellbeing (SWB) of caregivers were moderately and inversely correlated with caregiver burden. The regression results showed that the patients' age and caregivers' SWB were key characteristics associated with caregiver burden. CONCLUSIONS: The caregiver burden of adolescent patients was higher than that of adult patients, and the satisfaction rate of adolescent scoliosis patients was higher than that of adult scoliosis patients. Improving the functional state of scoliosis patients and providing appropriate nursing practice education from health professionals would be necessary to effectively improve caregivers SWB and alleviate caregiver burden.

## Pd91927ef1914

- Year: 2023
- Linked people: Takeru Shiroiwa
- Title: Cost-effectiveness analysis of lifestyle interventions for preventing kidney disease in patients with type 2 diabetes

Abstract:

Background Lifestyle interventions in patients with type-2 diabetes contribute to reducing the incidence of chronic kidney disease. The cost-effectiveness of lifestyle interventions to prevent kidney disease in patients with type-2 diabetes remains undetermined. We aimed to develop a Markov model from a Japanese healthcare payer's perspective focusing on the development of kidney disease in patients with type-2 diabetes and examine the cost-effectiveness of lifestyle interventions. Methods To develop the model, the parameters, including lifestyle intervention effect, were derived from results of the Look AHEAD trial and previously published literature. Incremental cost-effectiveness ratios (ICER) were calculated from the difference in cost and quality-adjusted life years (QALY) between lifestyle intervention and diabetes support education groups. We estimated lifetime costs and effectiveness assuming patient's life span to be 100 years. Costs and effectiveness were discounted by 2% annually. Results ICER for lifestyle intervention compared to diabetes support education was JPY 1,510,838 (USD 13,031) per QALY. Cost-effectiveness acceptability curve showed that the probability that lifestyle intervention is cost-effective at the threshold of JPY 5,000,000 (USD 43,084) per QALY gained, compared to diabetes support education, is 93.6%. Conclusions Using a newly-developed Markov model, we illustrated that lifestyle interventions for preventing kidney disease in patients with diabetes would be more cost-effective from a Japanese healthcare payer's perspective compared to diabetes support education. The model parameters in the Markov model must be updated to adapt to the Japanese setting.

## Pfa5c33517852

- Year: 2025
- Linked people: Zhuxin Mao
- Title: Identifying indicators of “success” in managing the COVID-19 pandemic in Europe: insights from an interdisciplinary expert consultation

Abstract:

BACKGROUND: Reflecting on what we have been through and learned during the COVID-19 pandemic can help prepare for similar challenges in the future. A quintessential question is what may indicate “success” in pandemic management. We aimed to establish a workable set of indicators for success over different distinct pandemic stages, as well as cumulatively from pandemic emergence to epidemic control. METHODS: First, using an iterative brainstorm and a pilot survey process, we developed a set of indicators of success for the entire pandemic (from late 2019 to date) and for six distinct COVID-19 pandemic stages: (1) pre-pandemic, (2) rising virus prevalence outside Europe, (3) rising virus prevalence in other countries or regions within Europe, (4) within-country first wave of virus, (5) subsequent virus waves pre-vaccination, (6) post-vaccination. Secondly, these indicators were validated by COVID-19 experts from different fields through an online survey. Experts were asked to rank the proposed indicators according to importance, along with answering two open-ended questions and five background questions. RESULTS: The developed indicator lists differed according to the pandemic stages. A total number of 45 experts completed the survey (29% response rate). All 50 indicators were ranked by at least 70% of the respondents as important. Notably, experts from all disciplines agreed that mortality was the most important indicator over the entire pandemic, during the first wave and subsequent waves pre-vaccination, while vaccination coverage was considered the most important indicator post-vaccination. Experts had different ranking preferences for the remaining indicators. CONCLUSION: Reflecting on the COVID-19 pandemic, this list could serve as a valuable resource to point towards which indicators are most crucial to monitor, informing future pandemic response strategies. Meanwhile, as this study currently only relied on input from European experts, it could serve as a validation set for experts outside Europe as well as the general public.

## P9d6e991b8600

- Year: 2025
- Linked people: Ciaran O'Neill
- Title: A Theoretically Informed Process Evaluation in Parallel to a Feasibility Study of a Complex Oral Health Intervention Using NICE Guidelines in a Care Home Setting.

Abstract:

BACKGROUND: A theoretically informed process evaluation was undertaken in parallel to a study examining the feasibility of an oral health intervention based on an existing guideline for care homes. The objectives were to explore the factors that influenced the implementation of the intervention in order to understand the potential pathway to impact. The research team initially utilised Pfadenhauer et al.'s framework, which focuses on a number of different implementation factors: intervention characteristics, context, theory, process, strategy, agents, outcomes and setting. METHODS: Nine semi-structured interviews were undertaken with care home managers and staff, predominantly within the intervention arm of the study. Interview schedules were originally based on Pfadenhauer et al.'s framework. These were coded and analysed using thematic analysis. Given the range of themes that emerged, the research team ran a reflexive workshop to determine whether Pfadenhauer et al.'s framework was able to capture and frame the authentic voice of those interviewed. RESULTS: The research team found that a systems lens approach better fitted the data from the interviews, capturing the idiosyncrasy of the different settings and the importance of values and beliefs of the key stakeholders. It was clear that unlike the structure proposed by Pfaednhauer et al., many of the factors were interdependent and hierarchical in nature, that is, paradigm and goals within the care home had a direct impact on the system structure, which fed into how the care home was maintained, which led onto how the different actors (care home managers and staff) behaved. The process also highlighted key factors for intervention delivery: time poverty, competing needs, staff turnover, differences between shift patterns and between permanent and agency staff. Cognitive capacity of the residents and staff attitudes were also key. CONCLUSIONS: Adding a reflexive workshop enabled the research to critically review the Pfadenhauer et al.'s framework and change to a systems lens approach, which better explained the interdependent and hierarchical nature of the findings. It also highlighted a number of key factors that could influence the pathway to impact for the intervention. TRIAL REGISTRATION: ISRCTN10276613.

## P91f1bbd286c9

- Year: 2026
- Linked people: Darshini Govindasamy
- Title: The correlates and experiences of HIV-related intersectional stigma among caregivers of adolescents living with HIV during COVID-19 in KwaZulu-Natal, South Africa: Results from a mixed method study.

Abstract:

Caregivers play a critical role in promoting HIV adherence and positive mental health among adolescents living with HIV (ALHIV). However, the health and wellbeing of caregivers are often compromised by HIV-related stigma. Furthermore, in sub-Saharan Africa, the effects of HIV-related stigma are amplified by intersecting forms of stigma, such as poverty and gender. If we can identify the key drivers of HIV-related intersectional stigma, then we can develop targeted strategies to improve caregiver wellbeing. We used a mixed-method study design, utilising quantitative and qualitative baseline data from an economic incentive trial with n = 100 caregivers of ALHIV sampled from peri-urban clinics in Durban, KwaZulu-Natal, South Africa between November and December 2021. We drew on the trial's survey dataset that examined socio-demographics, mental health and wellbeing, and stigma. We conducted descriptive statistics and fitted a linear regression model to assess correlates of HIV-related intersectional stigma using STATA (V18). In-depth interview data (n = 16 caregivers) were analysed guided by the Health Stigma and Discrimination Framework in NVivo. Of the 100 caregivers in the analysis, 86% were female, with a median age of 43 years (IQR:34-50) and 75% living with HIV. Seventy-eight caregivers reported experiencing HIV-related intersectional stigma. More than half (52%) were experiencing depressive symptoms, 51% were living in severely food-insecure households, and 59% were experiencing a high caregiver burden. Caregiver burden and total direct cost of caregiving were correlated with HIV-related intersectional stigma. Key domains from the qualitative data suggest that HIV-related intersectional stigma increased caregiver burden, diminished psychological well-being, and was linked to the cost associated with caregiving. Results highlight the need for multi-sectoral HIV-related intersectional stigma programmes that focus on economic empowerment and mental health coping strategies to equip carers with the skills needed to manage HIV-related intersectional stigma.

## P1ed293c242c7

- Year: 2024
- Linked people: Lidia Engel
- Title: Exploring important service characteristics of telephone cancer information and support services for callers: protocol for a systematic review of qualitative research.

Abstract:

INTRODUCTION: As cancer incidence continues to rise, challenges remain in how to communicate accurate, timely information to people with cancer, their families and healthcare professionals. One option is to provide support and comprehensive, tailored information via a telephone cancer information and support service (CISS). This systematic review aims to summarise the service characteristics of telephone CISS and identify what aspects of services are important from callers' perspectives. METHODS AND ANALYSIS: A comprehensive literature search will be conducted for articles published from database inception to 30 March 2023 (OVID MEDLINE, EMBASE, CINAHL, PsycINFO and SocINDEX). Published, peer-reviewed, articles reporting qualitative research on the service characteristics of telephone CISS important to callers in any language will be included. One researcher will complete the searches, two researchers will independently screen results for eligible studies and a third researcher will resolve any disagreement. A narrative and thematic synthesis of studies will be provided. Study characteristics will be independently extracted by one researcher and checked by a second. Included studies' methodological quality will be evaluated independently by two researchers using the 2022 Critical Appraisal Skills Programme Qualitative Studies Checklist. Grading of Recommendations Assessment, Development and Evaluation-Confidence in the Evidence from Reviews of Qualitative research tool will assess the confidence of the review findings. ETHICS AND DISSEMINATION: Ethics approval is not required for this research as it is a planned systematic review of published literature. Findings will be presented at leading cancer, health economic and supportive care conferences, published in a peer-reviewed journal, and disseminated via websites and social media. PROSPERO REGISTRATION NUMBER: CRD42023413897.

## Paa0180e69d60

- Year: 2024
- Linked people: Ciaran O'Neill
- Title: Inequality in green space distribution and its association with preventable deaths across urban neighbourhoods in the UK, stratified by Index of Multiple Deprivation

Abstract:

BACKGROUND: This study investigated inequalities in the distribution of green space (GS) and the association between inequalities in amounts of GS and preventable deaths across urban neighbourhoods with different Index of Multiple Deprivation (IMD) scores in the UK. METHODS: Data on preventable deaths, IMD, percentage of grassland and woodland, urban/rural, population size, and density were sourced for each of 6791 middle-layer super output areas (MSOAs) in England, 410 MSOAs in Wales, 1279 intermediate zones (IZs) in Scotland, and 890 super output areas (SOAs) in Northern Ireland (NI). While appreciating the potential for ecological fallacy we related area-based measures of deprivation to deaths. Concentration curves, Lorenz dominance tests, and negative binomial regression models were used to analyse the data. RESULTS: In urban areas of England, Scotland, and NI, the percentage of grassland was significantly lower among the more deprived neighbourhoods (Lorenz test, p<0.0001). In England, a 1% increase in grassland area was associated with a 37% reduction in annual preventable deaths among the most deprived urban MSOAs (incidence rate ratio (IRR) 0.63, 95% CI 0.52 to 0.76). In NI and Scotland, a 1% increase in grassland area was associated with a 37% (IRR 0.63, 95% CI 0.43 to 0.91) and 41% (IRR 0.59, 95% CI 0.42 to 0.81) reduction in 5-year accumulated preventable deaths in the most deprived urban SOAs/IZs, respectively. CONCLUSIONS: Results suggest that investment in GS in urban areas may be an important public health prevention strategy. There is evidence that investments in the most deprived urban neighbourhoods where the highest inequality currently exists would see the largest effect on preventable deaths.

## P40eca2d6a982

- Year: 2024
- Linked people: Annette Regan
- Title: Perinatal Outcomes After RSV Vaccination During Pregnancy—Addressing Emerging Concerns

Abstract:

Moeun Son, MD, MSCI; Laura E. Riley, MD; Anna P. Staniczenko, MD, MSc; Julia Cron, MD; Steven Yen, MS; Charlene Thomas, MS; Evan Sholle, MS; Lauren M. Osborne, MD; Heather S. Lipkind, MD, MS

## Pcdd6a95206cc

- Year: 2025
- Linked people: Abdulmuminu Isah
- Title: Mental health literacy on postpartum depression among university staff in Nigeria

Abstract:

Postpartum depression (PPD) is an important public health problem which often goes unrecognized and untreated, especially in low-income settings. Poor mental health literacy of community members has been shown to create barriers to help-seeking for PPD. The study assessed the mental health literacy of postpartum depression (PPD) among staff members in a Nigerian university. This was a cross-sectional survey that employed a case vignette format. A questionnaire, consisting of a socio-demographic form and a case vignette, was distributed to a convenient sample of 400 staff members in the faculties of pharmaceutical sciences, veterinary medicine, and agricultural sciences. Data were analysed using the IBM SPSS Statistics (version − 20). Descriptive analysis (frequencies, percentages, mean, and standard deviations) were used to summarize the findings. The relationship between socio-demographic characteristics and knowledge score of PPD was assessed using chi-square analysis. Statistical significance was set at p-value ˂0.05. The majority of the respondents were females 195 (54.0%) and were between 18 and 30 years of age (35.5%). Only 16.3% of respondents correctly identified PPD and nearly half (44.9%) of the respondents opined that the condition is ‘very serious. Poor knowledge of PPD was statistically significant associated with age [X 2 (4) = 18.252, p = 0.001], marital status [X 2 (3) = 16.888, p = 0.001], and educational qualification [X 2 (3) = 59.729, p = < 0.001], while medical help- seeking of PPD was statistically significant associated with age [X 2 (4) = 13.982, p = < 0.007], and educational qualification [X 2 (3) = 10.716, p = < 0.013]. The overall knowledge of postpartum depression among the staff members of the university was relatively poor and more female staff members than male staff members could identify postpartum depression. The study findings highlight the need to create awareness and improve knowledge of PPD through campaign-specific mental health programmes, educational programmes, integration of mental health programmes for university staff development to aid in early identification, intervention, media, and other targeted strategies such as creating a culture that encourages open discussions about mental health and provides accessible support services and, developing and implementing policies that address mental health in the university and the country at large.

## P4b440be249bb

- Year: 2021
- Linked people: Harri Sintonen
- Title: The health-related quality of life of patients with a benign gynecological condition: a 2-year follow-up.

Abstract:

Aim: To assess health-related quality of life (HRQoL) of patients with benign gynecological disorders. Materials &amp; methods: Prospective 2-year follow-up with the 15D HRQoL-instrument of 311 women treated in Helsinki-area hospitals in 2012–2013. Results: The initially impaired HRQoL regarding excretion, discomfort and symptoms, and vitality and sexual activity improved after treatment. However, only sexual activity reached similar levels as in the general population. Treatment of endometriosis, fibroids and polyps resulted in best and that of unspecific pelvic pain and bleeding disorders in worst HRQoL scores. Results were independent of hospital size. Conclusion: The impaired HRQoL dimensions were improved by treatment but HRQoL still remained poorer than in the general female population. Treatment of unspecific pelvic pain and bleeding disorders needs further evaluation.

## Pd5442979d930

- Year: 2022
- Linked people: Iwan van der Horst
- Title: External Validation of Mortality Prediction Models for Critical Illness Reveals Preserved Discrimination but Poor Calibration

Abstract:

OBJECTIVES: In a recent scoping review, we identified 43 mortality prediction models for critically ill patients. We aimed to assess the performances of these models through external validation. DESIGN: Multicenter study. SETTING: External validation of models was performed in the Simple Intensive Care Studies-I (SICS-I) and the Finnish Acute Kidney Injury (FINNAKI) study. PATIENTS: The SICS-I study consisted of 1,075 patients, and the FINNAKI study consisted of 2,901 critically ill patients. MEASUREMENTS AND MAIN RESULTS: For each model, we assessed: 1) the original publications for the data needed for model reconstruction, 2) availability of the variables, 3) model performance in two independent cohorts, and 4) the effects of recalibration on model performance. The models were recalibrated using data of the SICS-I and subsequently validated using data of the FINNAKI study. We evaluated overall model performance using various indexes, including the (scaled) Brier score, discrimination (area under the curve of the receiver operating characteristics), calibration (intercepts and slopes), and decision curves. Eleven models (26%) could be externally validated. The Acute Physiology And Chronic Health Evaluation (APACHE) II, APACHE IV, Simplified Acute Physiology Score (SAPS)-Reduced (SAPS-R)' and Simplified Mortality Score for the ICU models showed the best scaled Brier scores of 0.11' 0.10' 0.10' and 0.06' respectively. SAPS II, APACHE II, and APACHE IV discriminated best; overall discrimination of models ranged from area under the curve of the receiver operating characteristics of 0.63 (0.61-0.66) to 0.83 (0.81-0.85). We observed poor calibration in most models, which improved to at least moderate after recalibration of intercepts and slopes. The decision curve showed a positive net benefit in the 0-60% threshold probability range for APACHE IV and SAPS-R. CONCLUSIONS: In only 11 out of 43 available mortality prediction models, the performance could be studied using two cohorts of critically ill patients. External validation showed that the discriminative ability of APACHE II, APACHE IV, and SAPS II was acceptable to excellent, whereas calibration was poor.

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

## Pa7d4b1c07001

- Year: 2026
- Linked people: Mark Sculpher
- Title: What is the Value of Developing an HTA Process?

Abstract:

Health technology assessment (HTA) processes are becoming increasingly established and embedded in healthcare decision making around the world. Yet, there is limited evidence on whether HTA processes at the system level offer value for money to those presiding over their creation, such as governments and ministries of health. That is, whether the value of improvements in the health system exceed the costs. To address this issue, we outline the approaches adopted in a sample of recent evaluations of HTA systems and propose a set of considerations for measuring and valuing HTA processes. The scale and remit of the process can help identify the relevant system-level impacts of HTA such as those on productive efficiency and population health, health equity, guiding innovation and care pathways, and broader impacts. We further describe the methodological challenges and potential approaches to evaluating HTA including the appropriateness of approaches. The considerations discussed can reveal the potential for ill-designed HTA processes to generate less social value than intended.

## Pfb2736b92351

- Year: 2025
- Linked people: Kristina Secnik Boye
- Title: Therapeutic Inertia in an Insured Population with Type 2 Diabetes in the United States: A Retrospective Cohort Study.

Abstract:

INTRODUCTION: This study examines the characteristics of adults with type 2 diabetes (T2D) who were not initially treated with an antihyperglycemic agent (AHA). METHODS: The analyses used Optum de-identified Market Clarity data from January 2013 through September 2023. The US study included nonpregnant adults with T2D who were continuously insured from 1 year prior through 5 years post diagnosis and did not fill a prescription for an AHA in the year after their initial T2D diagnosis. Differences between those treated in years 2-5 with an AHA (delayed treatment) and those untreated with an AHA for 5 years post diagnosis (untreated) were examined descriptively and using multivariable analyses. RESULTS: Out of 186,259 adults with T2D, 56.7% (N = 105,533) did not fill a prescription for an AHA in the year after diagnosis and were included in the study. Of these 105,533 adults (mean age 59.6 years; 51.4% female), 75.0% were untreated for the entire 5 years post diagnosis. In the delayed treatment group, metformin was the most common first-line therapy (72.9%), and 83.0% of those who initiated monotherapy never received additional classes of AHAs. Compared to the delayed treatment group, the untreated group had significantly higher rates of incident cardiovascular outcomes and all-cause direct total costs ($118,191 vs $108,687; P < 0.05). CONCLUSION: Over 50% of adults diagnosed with T2D were untreated with an AHA in the first year post diagnosis, and most of those who went untreated the first year remained untreated after 5 years. Among the delayed treatment patients, the majority did not use additional AHA classes besides their index therapy in the post-period. These findings suggest that therapeutic inertia affects a significant percentage of individuals with T2D. Given the untreated group's significantly worse cardiovascular outcomes and higher medical costs, these findings highlight a potential unmet need in the years immediately following T2D diagnosis.

## P20b4604aa789

- Year: 2024
- Linked people: Maja Kuharic
- Title: Shared decision-making and disease management in advanced cancer and chronic kidney disease using patient-reported outcome dashboards.

Abstract:

OBJECTIVES: To assess the use of a co-designed patient-reported outcome (PRO) clinical dashboard and estimate its impact on shared decision-making (SDM) and symptomatology in adults with advanced cancer or chronic kidney disease (CKD). MATERIALS AND METHODS: We developed a clinical PRO dashboard within the Northwestern Medicine Patient-Reported Outcomes system, enhanced through co-design involving 20 diverse constituents. Using a single-group, pretest-posttest design, we evaluated the dashboard's use among patients with advanced cancer or CKD between June 2020 and January 2022. Eligible patients had a visit with a participating clinician, completed at least two dashboard-eligible visits, and consented to follow-up surveys. PROs were collected 72 h prior to visits, including measures for chronic condition management self-efficacy, health-related quality of life (PROMIS measures), and SDM (collaboRATE). Responses were integrated into the EHR dashboard and accessible to clinicians and patients. RESULTS: We recruited 157 participants: 66 with advanced cancer and 91 with CKD. There were significant improvements in SDM from baseline, as assessed by collaboRATE scores. The proportion of participants reporting the highest level of SDM on every collaboRATE item increased by 15 percentage points from baseline to 3 months, and 17 points between baseline and 6-month follow-up. Additionally, there was a clinically meaningful decrease in anxiety levels over study period (T-score baseline: 53; 3-month: 52; 6-month: 50; P < .001), with a standardized response mean (SRM) of -0.38 at 6 months. DISCUSSION: PRO clinical dashboards, developed and shared with patients, may enhance SDM and reduce anxiety among patients with advanced cancer and CKD.

## Pffe3eca4dc88

- Year: 2025
- Linked people: Deborah Marshall
- Title: Stated-Preference Survey Design and Testing in Health Applications.

Abstract:

Following the conceptualization of a well-formulated and relevant research question, selection of an appropriate stated-preference method, and related methodological issues, researchers are tasked with developing a survey instrument. A major goal of designing a stated-preference survey for health applications is to elicit high-quality data that reflect thoughtful responses from well-informed respondents. Achieving this goal requires researchers to design engaging surveys that maximize response rates, minimize hypothetical bias, and collect all the necessary information needed to answer the research question. Designing such a survey requires researchers to make numerous interrelated decisions that build upon the decision context, selection of attributes, and experimental design. Such decisions include considering the setting(s) and study population in which the survey will be administered, the format and mode of administration, and types of contextual information to collect. Development of a survey is an interactive process in which feedback from respondents should be collected and documented through qualitative pre-test interviews and pilot testing. This paper describes important issues to consider across all major steps required to design and test a stated-choice survey to elicit patient preferences for health preference research.

## P29a6757f6d9a

- Year: 2025
- Linked people: Nils Gutacker
- Title: Activity outcomes after hip arthroplasty: an information tool based on patients’ experience captured in a hospital registry

Abstract:

BACKGROUND AND PURPOSE: Patients receiving total hip arthroplasty (THA) have different expectations and concerns about their health outcomes after surgery. In this study we developed a tool based on registry data to inform patients and their clinicians about activity outcomes after THA. METHODS: We used data from the Geneva Arthroplasty Registry (GAR) on patients receiving a primary elective THA between 1996 and 2019. The information tool was developed around five activity outcomes: getting in/out of the car, getting dressed autonomously, independence in weekly tasks, interference in social activities, and activity levels. Based on baseline predictors, conditional inference trees (CITs) were used to create clusters of patients with homogeneous activity outcomes at one, five and 10 years after surgery, rather than to predict individual probabilities. RESULTS: In total, 14 CITs were generated based on 6,836 operations included in the tool. Overall, activity outcomes substantially improved at all three times points after surgery, with 1-year values mostly being the highest. While before surgery only about 10% of patients had none/slight limitations in activities of daily living, about 70% did one year after surgery. The SF12 mental component score (MCS), SF12 self-rated health (SRH), BMI, ASA score, and comorbidity count were the most recurring predictors of activity outcomes. Predictors and their relative importance changed at different time points for the same outcome. For example, for ability to get in/out the car, whilst clusters at year 1 were generated based on WOMAC function, SRH, mental health, WOMAC difficulty walking, and SF12 physical interference, at year 5, ASA score, BMI, SF12 physical & mental health, activity level, and socio-economic status were significant. Outcome profiles varied by clusters. CONCLUSION: Distinct activity outcomes clusters based on baseline patient characteristics were identified and knowing this can help inform patients' expectation and meaningful discussions with clinicians about treatment decisions.

## Pb5669f9b0e3c

- Year: 2025
- Linked people: Deborah Marshall
- Title: Measuring Patient Preferences to Inform Clinical Trial Design: An Example in Rheumatoid Arthritis.

Abstract:

Allogeneic bone marrow transplantation (BMT) may be a curative treatment for patients with rheumatoid arthritis (RA), but it has serious risks, including death. It is uncertain whether patients would accept the risks and benefits of BMT and participate in clinical trials. We conducted a discrete choice experiment (DCE) to quantify risk tolerance and benefit-risk trade-offs to inform the design of a clinical trial for BMT.
We conducted a DCE with three attributes (three levels each): chance of stopping disease progression (50-90%), increased chance of death in year after transplant (3-15%), and chance of chronic graft-versus-host disease (cGVHD) (3-15%). An orthogonal main effects design of nine binary choice tasks were presented for two scenarios: one considering their current situation and a second scenario where the patient has failed seven anti-rheumatic drugs. Participants were recruited from the Rheum4U inflammatory arthritis registry. Choice data were analyzed using a logit model accounting for multiple responses per participant.
Sixty patients participated. Most (82%) had severe disease, and the median number of anti-rheumatic drugs previously taken was 6 (range 0-18). As expected, an increased chance of stopping disease progression increases the probability of choosing BMT, while increased chance of both risks decreases the probability. Patients were willing to accept a 3% increase in risk of death or 6% increase in chance of chronic GVHD for a 10% increase in the chance of stopping disease progression. For the most clinically likely BMT risk-benefit profiles, and the likely initial target population of patients who have failed multiple biologics, between 72% and 91% of patients would choose BMT.
Patients with RA are willing to accept substantial risks for a chance to stop disease progression with BMT, suggesting that a pilot trial of BMT for RA could successfully recruit patients. Preference studies have an important role in informing patient-centered clinical trial planning and design.

## P9144d0cff881

- Year: 2026
- Linked people: Maureen Rutten-van Molken
- Title: Organisational interventions in nursing care: A scoping review and descriptive system to support comparison

Abstract:

Background The nursing profession across developed countries faces significant pressures, particularly due to nursing shortages, highlighting the need for effective organisational interventions of nursing care at hospital level, e.g. new nursing roles, experimenting with different types of nurses and differentiated practices of nursing, and the expansion of the nursing profession within the hospital. However, it is difficult to learn from those experiences, partly because of the absence of a standardised description of these interventions. We benefited from a window of opportunity that occurred after failed reorganisation attempts at national level in the Netherlands, leading to a wide range of local initiatives to experiment and organise nursing care differently. Objective To develop a comprehensive descriptive system to systematically describe the diversity of interventions to reorganise nursing care in different hospital settings. Methods A scoping review of Dutch grey literature on these initiatives was conducted to identify interventions to (re)organise nursing care in Dutch hospitals between 2015 and 2021. The results were analysed thematically and synthesised into a descriptive system, consisting of a checklist and a matrix, embedded in international literature to capture the diversity in the (re)organisation of hospital nursing care. We applied the descriptive system on two cases of interventions of (re)organising nursing care in Dutch hospitals. Results Initially, 1102 records were identified, of which 27 were included in the review. Three main themes were determined: the organisation of different types of nurses, the organisation of different types of nursing work, and the organisation based on terms of employment. The three themes formed the basis for the descriptive system, each outlined with three dimensions describing each theme in more detail. Nine dimensions were identified within these three themes: (1) educational degree, competences, and subjective professional requirements, (2) patient care, indirect operational patient tasks, and quality and research, and (3) positions and embedding, quantity and ratios, and valuation. Additionally, the context was added to the descriptive system in order to take into account contextual factors not captured by the dimensions. All themes and dimensions proved valuable when applying the descriptive system to the two existing interventions. Conclusions We propose a system of interventions of (re)organising nursing care to enable a systematic and comprehensive description of such interventions as the basis for evaluation.

## P56a0db896a2c

- Year: 2025
- Linked people: Elske van den Akker-van Marle
- Title: Patient preferences for analgesia in lung surgery: an observational cohort study

Abstract:

BACKGROUND: Optimal analgesia following thoracoscopic lung surgery is crucial for patient comfort and effective recovery. Despite the lack of high quality evidence in guidelines, experts favour locoregional analgesic techniques above thoracic epidural analgesia (TEA), without considering patient preferences. This study investigates patient choices to aid in shared-decision making and incorporation in guidelines. METHODS: Through adaptive conjoint analysis (ACA) concerning attributes (characteristics) related to analgesic techniques and treatment trade-off methods (TTM) comparing scenarios with locoregional analgesia against TEA, 200 patients planned for thoracoscopic lung resection in five Dutch hospitals received online questionnaires. In the TTM, patients were repeatedly asked to choose between two scenarios: one describing thoracic epidural analgesia with fixed low levels of pain and the other representing locoregional analgesia with varying pain levels, to assess trade-off thresholds. For the ACA, Relative Importance (RI) of the characteristics was calculated with 95%-confidence intervals (CI). RESULTS: Response rates of ACA and TTM questionnaires were 72% (144/200) and 71% (141/200) respectively. The most important characteristics were state of consciousness (‘awake or under general anaesthesia’) while receiving the analgesic technique (RI 20.45; 95%-CI 19.12–21.75) and mobilisation (RI 19.42; 95%-CI 18.45–20.38). In the TTM, 10 patients (7.1%) consistently chose the TEA scenario, irrespective of the benefits of locoregional analgesia. In contrast, 131 patients (92.9%) preferred experiencing more moments of pain as trade-off for the potential advantages associated with locoregional analgesia. CONCLUSION: Regarding analgesia following thoracoscopic lung surgery, patients considered the state of consciousness while receiving the analgesic technique (awake or under general anaesthesia) and postoperative mobility as the most important characteristics. Over 92% of patients are willing to accept more moments of pain as trade-off for the potential benefits of locoregional analgesia. These findings are aligned with current guideline recommendations and support the inclusion of patient preferences in shared decision-making.

## Pf4f842632739

- Year: 2025
- Linked people: Ciaran O'Neill
- Title: Age-period-cohort analysis of different mental wellbeing measures in Scotland from 2008 to 2021: The U-shaped curve of mental wellbeing over the life course

Abstract:

Common mental disorders are increasingly recognized as a serious public health concern globally. This study reports an age-period-cohort (APC) analysis of mental wellbeing to help identify high-risk groups. Data from Scottish Health Survey from 2008 to 2021 for adults aged 16+ was used with mental wellbeing measured with three different tools: the General Health Questionnaire-12 (GHQ-12), the Warwick-Edinburgh Mental Wellbeing Scale (WEMWBS) and the Revised Clinical Interview Schedule (CIS-R). A graphical analysis was performed using hexamap and Intrinsic Estimator models were employed to estimate the separate effects for age, period and birth cohorts on mental wellbeing. Age evidenced the most pronounced pattern with a U-shape curve indicative of a deterioration of mental health as individuals enter adulthood, reaching a nadir in their late 50s/ early 60s before gradually improving thereafter. Mental health trends across cohorts were largely stable, although there was a noticeable, albeit non-significant, increase in mental health issues among people born in late 1990s-to mid-2000s. After adjusting for APC effects, better mental health was found for males, people with higher incomes, employed and those currently married. Medium to high level of physical activity were also associated with better mental wellbeing. The study supports arguments for greater attention to mental health among those are working-age adults and for younger generations born after the 1980s. Associations with sex, socio-economic factors may help guide targeting of public health measures while associations with a healthy physical lifestyle support arguments at measures intended to promote a mental health through physical activity. • GHQ-12, WEMWBS and CIS-R tool were used to measure mental wellbeing • Three measures provided similar patterns by age, time period and birth cohorts. • Age effect was most pronounced with a U-shaped curve of happiness over the life course • Cohort effect: a noticeable raise in mental health issues among Millennials and Gen Z. • After controlled for age and cohort effect, secular trend from 2008 to 2021 were relatively stable

## P2beceff25e7c

- Year: 2025
- Linked people: Stirling Bryan
- Title: The BC SUPPORT Unit: bringing patient-oriented research to bridge research and practice in health care

Abstract:

This is the introductory paper in a collection of five papers on the BC SUPPORT Unit, a component of the pan-Canadian Strategy for Patient-Oriented Research (SPOR), and is match funded by the Canadian Institutes of Health Research and the provincial government of British Columbia since 2016. In this introductory paper, we offer a brief overview of the Strategy, describe the ambition underlying the creation of the SUPPORT Unit in British Columbia, provide information on the Unit’s mandate and approach, and identify areas of ongoing priority focus for the Unit.

## Pf0c76e8230a1

- Year: 2025
- Linked people: Kelly de Ligt
- Title: Exploring the role of health-related quality of life measures in predictive modelling for oncology: a systematic review.

Abstract:

Health related quality of life (HRQoL) is increasingly assessed in oncology research and routine care, which has led to the inclusion of HRQoL in prediction models. This review aims to describe the current state of oncological prediction models incorporating HRQoL. A systematic literature search for the inclusion of HRQoL in prediction models in oncology was conducted. Selection criteria were a longitudinal study design and inclusion of HRQoL data in prediction models as predictor, outcome, or both. Risk of bias was assessed using the PROBAST tool and quality of reporting was scored with an adapted TRIPOD reporting guideline. From 4747 abstracts, 98 records were included in this review. High risk of bias was found in 71% of the publications. HRQoL was mainly incorporated as predictor (78% (55% predictor only, 23% both predictor and outcome)), with physical functioning and symptom domains selected most frequently as predictor. Few models (23%) predicted HRQoL domains by other or baseline HRQoL domains. HRQoL was used as outcome in 21% of the publications, with a focus on predicting symptoms. There were no difference between AI-based (16%) and classical methods (84%) in model type selection or model performance when using HRQoL data. This review highlights the role of HRQoL as a tool in predicting disease outcomes. Prediction of and with HRQoL is still in its infancy as most of the models are not fully developed. Current models focus mostly on the physical aspects of HRQoL to predict clinical outcomes, and few utilize AI-based methods.

## P1141d34456d2

- Year: 2025
- Linked people: Lidia Engel
- Title: Implementability of a co-designed programme to increase tailored exercise to reduce falls in older people from culturally and linguistically diverse communities: protocol for a pilot randomised controlled trial.

Abstract:

Introduction Falls are a critical problem for older people, including those from ethnically diverse communities, who are under-represented in research. The aim of this pilot trial is to evaluate (1) the implementability of a co-designed intervention developed to support the sustained uptake of tailored exercise to reduce falls ( MOVE Together: Reduce Falls ) and (2) the feasibility of conducting a randomised controlled trial (RCT) in older people from Italian, Arabic, Cantonese or Mandarin-speaking communities. Methods and analysis Investigator and assessor-blinded pilot two-arm parallel RCT. 60 older people at risk of falls from Italian, Arabic, Cantonese or Mandarin speaking communities will be recruited, with the option to enrol on their own or with another participant (dyad). Participants or dyads will be randomly assigned to the experimental or control arm. The experimental arm will receive MOVE Together: Reduce Falls , which provides up to 12 sessions with a physiotherapist over 12 months and supports participants to engage in individualised exercises. Both arms will receive educational resources in the participant’s preferred language. The primary outcome is implementability of the co-designed intervention, MOVE Together: Reduce Falls; operationalised as fidelity (&gt;70% of intended sessions delivered), feasibility (&gt; 95% of sessions delivered with no serious adverse events related or likely related to the intervention) and acceptability (&gt;50% acceptability score). The secondary outcome is feasibility of the RCT protocol, which will be evaluated quantitatively (eg, recruitment and retention rates, completion of clinical outcome data including prospective collection of falls data for 12 months via falls calendars) and qualitatively (eg, barriers and enablers to data collection). Ethics and dissemination Ethical approval has been granted for this study (HREC/106010/MH-2024). Study findings will be published in peer-reviewed journals and presented at relevant conferences and community forums. Trial registration number ACTRN12624000658516.

## Pc31cae779c4c

- Year: 2026
- Linked people: Deborah Marshall
- Title: Balancing safety and effectiveness: parent preferences for fecal microbiota transplant and established therapies in pediatric inflammatory bowel disease-results of a multicenter Canadian study.

Abstract:

Treatment decision-making in pediatric inflammatory bowel disease (IBD) is complex, with many existing and emerging options. However, little is known about parent preferences for these therapies. This multi-center Canadian study provides the first quantitative data on parent preferences for pediatric IBD treatments and explores characteristics associated with differing preferences.
We conducted a cross-sectional survey including a discrete choice experiment (DCE) with Canadian parents (n = 159) of children diagnosed with UC/IBD-U, recruited from four pediatric IBD clinics. The DCE assessed preferences across four treatment attributes: chance of clinical remission, severity and chance of known side effects, severity of rare unknown side effects, and mode of treatment delivery. Latent class modeling was used to explore preference heterogeneity.
Parents prioritized safety, particularly the risk of rare unknown side effects, followed by likelihood of remission. Latent class analysis identified two distinct groups: one most concerned about rare unknown side effects, and another prioritizing treatment effectiveness. Thirty-eight percent of parents were open to fecal microbiota transplant (FMT), an emerging therapy that uses donor stool to help restore gut microbiome health. Younger parents and those with children experiencing more severe disease and on multiple medications were more likely to accept FMT. Across the cohort, many parents were willing to trade off less desirable delivery modes or increased risk in exchange for better treatment outcomes.
Parents value both safety and effectiveness in IBD treatment decisions. Recognizing these preferences may support shared decision-making, particularly when discussing novel therapies like FMT.

## P8e8d3be1c8da

- Year: 2025
- Linked people: Deborah Marshall
- Title: Economic Evaluation of Including Biomarker Testing in the Biologic Therapy Withdrawal Decision-Making Process in Non-Systemic Juvenile Idiopathic Arthritis: The International UCAN CAN-DU and CURE Study

Abstract:

Objectives To assess the cost-effectiveness of including biomarker testing in the decision-making process of withdrawing biologic therapy for patients with non-systemic JIA compared to usual care. Methods A health economic model was developed to assess 3 different scenarios reflecting decision-making in response to biomarker information and what percentage of patients start biologic therapy withdrawal early (within 2 years after reaching inactive disease) including 20%, 46% and 75%, compared to usual care (74%). A 1-month cycle length and ten-year time horizon were used. Transition probabilities, costs and effects were based on data from the UCAN CAN-DU cohorts (in The Netherlands and Canada), and the Wilhelmina Children’s Hospital (Utrecht, the Netherlands), plus clinical expert opinion and the literature. Costs include drugs, biomarker testings, pediatric rheumatology visits and other hospital related costs, such as radiology investigations, laboratory testing and hospitalization. Effects were measured in quality-adjusted life years (QALYs). A probabilistic analysis was performed to reflect uncertainty Results In the analysis we compared usual care to each individual scenario. The percentage of flare-ups within the 1st year of stopping biologics are 62% for usual care, compared to 43%, 50% and 57% respectively. In usual care, the average time in active disease per patient is 25 months (21%), where the scenarios show 23 months (19%), 24 months (20%) and 25 months (21%). The average time off biologics in usual care is 26 months (22%), where the scenarios show 26 months (22%), 29 months (24%), 30 months (25%). The absolute costs are €79,051 for usual care, compared to €78,315, €77,354, and €76,745 respectively, resulting in incremental costs of €−737, €−1,697, and €−2,306. The absolute QALYs are 7.470 for usual care, compared to 7.535, 7.521, and 7.490 respectively, resulting in incremental QALYs of 0.065, 0.051 and 0.020. The incremental cost-effectiveness ratio for each scenario is €−11,254/QALY, €−33,301/QALY and €−117,145/QALY. The Net Health Benefit, for a willingness-to-pay (WTP) threshold of €50,000/QALY, is 0.080, 0.085 and 0.066. For this WTP, the probabilistic analysis shows that the probability of biomarker testing being cost-effective was 100% for all scenarios. Conclusion The inclusion of biomarker testing in the decision-making process of withdrawing biologic therapy in JIA is likely to be cost-effective. The benefits of biomarker-guided therapy withdrawal are preference sensitive and will depend on the balance between how patients/families and physicians tradeoff between time off biologics (and consequently cost savings) and the (avoidable) risk of flare-up due to early withdrawal.

## P72cba429f618

- Year: 2026
- Linked people: Wolfgang Greiner
- Title: Epidemiology and economic burden of medically attended influenza and influenza-like illness in Germany, 2016-2019.

Abstract:

AIMS: Older adults and individuals with certain underlying conditions are at elevated risk of severe influenza complications. This study quantifies the burden of influenza and influenza-like illness (ILI) in Germany focusing on these high-risk groups. METHODS: This cohort study is based on claims data of a large statutory health insurance fund. Influenza/ILI was identified through International Classification of Diseases version 10 (ICD-10) codes J09-J11. Among insured individuals, the incidence of medically attended influenza/ILI, hospitalizations, complications, and direct healthcare costs were estimated for three consecutive influenza seasons from 2016-2017 to 2018-2019. Healthcare resource use, complications, and costs attributable to influenza were estimated through comparison with a matched control group. Analyses were stratified by age and prevalence of underlying conditions. RESULTS: Approximately 7 million individuals were included in each season. Influenza/ILI incidence decreased with age, but hospitalizations were most common among older adults. One in five cases aged 80+ years was hospitalized. In all age groups, individuals with underlying conditions had a higher incidence of influenza/ILI and of complications than those without underlying conditions. Direct costs per influenza/ILI case ranged from €133.28 (2016-2017) to €218.99 (2018-2019) and were higher in older adults and in individuals with underlying conditions. LIMITATIONS: Underdiagnosis and misclassification of influenza in administrative claims may occur, particularly in the outpatient setting. Only selected complications were examined; exclusion of cardiovascular and neurological consequences likely results in an underestimation of the influenza/ILI burden. Indirect costs, e.g. through productivity losses are not considered. CONCLUSIONS: Influenza/ILI significantly impacts the German healthcare system, with older adults and individuals with underlying conditions contributing disproportionately to the observed burden. Risks of severe outcomes and direct costs are highest in older adults, particularly those aged 80+ years, while children with underlying conditions also contribute substantially to the observed burden. These groups are important targets for preventive interventions.

## Pd0b5ec0069a5

- Year: 2025
- Linked people: Zhuxin Mao
- Title: Distribution Patterns and Assembly Mechanisms of Rhizosphere Soil Microbial Communities in Schisandra sphenanthera Across Altitudinal Gradients

Abstract:

To investigate the characteristics of rhizosphere soil microbial communities associated with Schisandra sphenanthera across different altitudinal gradients and to reveal the driving factors of microbial community dynamics, this study collected rhizosphere soil samples at four elevations: 900 m (HB1), 1100 m (HB2), 1300 m (HB3), and 1500 m (HB4). High-throughput sequencing and molecular ecological network analysis were employed to analyze the microbial community composition and species interactions. A null model was applied to elucidate community assembly mechanisms. The results demonstrated that bacterial communities were dominated by Proteobacteria, Acidobacteriota, Actinobacteriota, and Chloroflexi. The relative abundance of Proteobacteria increased with elevation, while that of Acidobacteriota and Actinobacteriota declined. Fungal communities were primarily composed of Ascomycota and Basidiomycota, with both showing elevated relative abundances at higher altitudes. Diversity indices revealed that HB2 exhibited the highest bacterial Chao, Ace, and Shannon indices but the lowest Simpson index. For fungi, HB3 displayed the highest Chao and Ace indices, whereas HB4 showed the highest Shannon index and the lowest Simpson index. Ecological network analysis indicated stronger bacterial competition at lower elevations and enhanced cooperation at higher elevations, contrasting with fungal communities that exhibited increased competition at higher altitudes. Altitude and soil nutrients were negatively correlated with soil carbon content, while plant nutrients and fungal diversity positively correlated with soil carbon. Null model analysis suggested that deterministic processes dominated bacterial community assembly, whereas stochastic processes governed fungal assembly. These findings highlight significant altitudinal shifts in the microbial community structure and assembly mechanisms in S. sphenanthera rhizosphere soils, driven by the synergistic effects of soil nutrients, plant growth, and fungal diversity. This study provides critical insights into microbial ecology and carbon cycling in alpine ecosystems, offering a scientific basis for ecosystem management and conservation.

## P7e0c4874b507

- Year: 2026
- Linked people: Oriana Ciani
- Title: ESG Performance, Debt Financing, and R&amp;D Output: Evidence From the Healthcare Sector

Abstract:

ABSTRACT Amid growing calls for sustainability in the healthcare sector, this study examines how and under what conditions environmental, social, and governance (ESG) performance influences research and development (R&amp;D) output. Although existing studies suggest that ESG performance enhances R&amp;D output, the financial mechanisms that enable or constrain this relationship remain underexplored. We address this gap by theorizing and testing the dual role of debt financing as both a mediator and a moderator in the ESG performance and R&amp;D output relationship within the healthcare sector, where innovation is highly capital‐intensive and socially consequential. Integrating stakeholder theory and agency theory, we argue that ESG performance promotes R&amp;D output through improved access to reputational and financial resources, whereas high debt levels weaken this effect due to agency conflicts. Using panel data from 2016 to 2022 on healthcare firms in Europe and the United States, we estimate our main models using OLS and applying instrumental variable and system GMM techniques as robustness checks to address endogeneity. Our findings show that debt financing partially mediates the ESG–R&amp;D link and negatively moderates it, revealing its ambivalent role. Compared to existing studies, our findings indicate that the effects of ESG performance on R&amp;D output are conditional and context specific, with stronger impacts observed in Europe than in the United States, reflecting institutional conditions such as stricter European Union sustainability reporting frameworks, notably the Corporate Sustainability Reporting Directive (CSRD), along with robust policy incentives and longer term investment horizons. We also find pronounced effects in the biotechnology and pharmaceutical subsectors. This study contributes to theory by bridging competing views on ESG performance and offering a more nuanced understanding of how debt financing shapes the ESG–R&amp;D output relationship.

## P0cfe6556573a

- Year: 2024
- Linked people: Hesam Ghiasvand
- Title: Translating potential improvement in the precision and accuracy of lung nodule measurements on computed tomography scans by software derived from artificial intelligence into impact on clinical practice—a simulation study

Abstract:

Objectives: Accurate measurement of lung nodules is pivotal to lung cancer detection and management. Nodule size forms the main basis of risk categorization in existing guidelines. However, measurements can be highly variable between manual readers. This article explores the impact of potentially improved nodule size measurement assisted by generic artificial intelligence (AI)-derived software on clinical management compared with manual measurement. Methods: The simulation study created a baseline cohort of people with lung nodules, guided by nodule size distributions reported in the literature. Precision and accuracy were simulated to emulate measurement of nodule size by radiologists with and without the assistance of AI-derived software and by the software alone. Nodule growth was modelled over a 4-year time frame, allowing evaluation of management strategies based on existing clinical guidelines. Results: Measurement assisted by AI-derived software increased cancer detection compared to an unassisted radiologist for a combined solid and sub-solid nodule population (62.5% vs 61.4%). AI-assisted measurement also correctly identified more benign nodules (95.8% vs 95.4%); however, it was associated with over an additional month of surveillance on average (5.12 vs 3.95 months). On average, with AI assistance people with cancer are diagnosed faster, and people without cancer are monitored longer. Conclusions: In this simulation, the potential benefits of improved accuracy and precision associated with AI-based diameter measurement is associated with additional monitoring of non-cancerous nodules. AI may offer additional benefits not captured in this simulation, and it is important to generate data supporting these, and adjust guidelines as necessary. Advances in knowledge: This article shows the effects of greater measurement accuracy associated with AI assistance compared with unassisted measurement.

## P064e7fbc3f47

- Year: 2025
- Linked people: Shankar Prinja
- Title: Seizing the silent vision loss: cost-utility analysis of population-based glaucoma screening in India.

Abstract:

OBJECTIVES: Glaucoma is a major cause of irreversible blindness in India; however, if detected early, its progression can be either prevented or stabilised through appropriate medical or surgical treatment. We aim to evaluate the cost-utility of various models for population-based glaucoma screening at primary health centres in India. We also assess the potential impact of the implementation of a population-based screening programme on overall costs of care for glaucoma. DESIGN: Cost-utility analysis using a mathematical model comprising a decision tree and Markov model was conducted to simulate relevant costs and health outcomes over a lifetime horizon. SETTING: Screening services were assumed to be delivered at primary health centres in India. PARTICIPANTS: A hypothetical cohort of different target population groups in terms of age groups and risk of glaucoma (age group 40-75 years, 50-75 years, 40-75 years age group at high risk of glaucoma, 50-75 years age group at high risk of glaucoma) were included in comparative screening strategies. INTERVENTIONS: The exclusive intervention scenarios were 12 screening strategies based on different target population groups (age group 40-75 years, 50-75 years, 40-75 years age group at high risk of glaucoma, 50-75 years age group at high risk of glaucoma), screening methods (face-to-face screening and artificial intelligence-supported face-to-face screening) and screening frequencies for 40-75 years aged population (annual vs once every 5 years screening), in comparison to usual care scenario. The usual care scenario (current practice) implied opportunistic diagnosis by the ophthalmologists at higher levels of care. PRIMARY AND SECONDARY OUTCOMES: The primary outcome was the incremental cost-utility ratio for each of the screening strategies in comparison to usual care. The secondary outcomes were per person lifetime costs, lifetime out-of-pocket expenditures, life years and quality-adjusted life-years (QALYs) in all screening scenarios and usual care. FINDINGS: Depending on the type of screening strategy, the gain in QALY per person ranged from 0.006 to 0.046 relative to usual care. However, the screening strategies, whether adjusted for specific age groups, patient risk profiles, screening methods or frequency, were not found to be cost-effective. Nonetheless, annual face-to-face screening strategies for individuals aged 40-75 years could become cost-effective in a scenario of strengthened public financing and provisioning, such that at least 67% of those seeking care for confirmatory diagnosis and treatment use government-funded facilities, in conjunction with 60% availability of medications at government hospitals. CONCLUSIONS: Enhancing continuity of care following screening through either strengthening of public provisioning or strategic purchasing of care could make glaucoma screening interventions not only cost-effective, but also potentially cost-saving.

## Pc21e7607529b

- Year: 2025
- Linked people: Lidia Engel
- Title: Health Utility Decrements Associated With Social Isolation and Loneliness: Evidence From Australian Longitudinal Data

Abstract:

OBJECTIVES: This study estimates health utility decrements associated with social isolation and loneliness (SIL) using nationally representative longitudinal data from Australia. METHODS: Four waves of the Household, Income and Labour Dynamics in Australia survey were analyzed. Health utility was measured using the Short Form 6-Dimension with the Australian weighting algorithm. Social isolation was defined as living alone with infrequent social contact, and loneliness as a score ≥5 on a 1 to 7 scale. Respondents were classified as neither, socially isolated only, lonely only, or both. Individual fixed-effects panel regressions were applied to estimate within-person associations, with adjustment for time-varying health and sociodemographic factors. RESULTS: A total of 53 108 observations from 21 965 individuals (mean age 44.9; 53% male) were included, with 20% experiencing SIL (3% socially isolated only, 15% lonely only, 2% both). Compared with no SIL, adjusted models showed utility decrements of 0.020 for social isolation, 0.061 for loneliness, and 0.102 for both (all P < .001). The combined decrements significantly exceeded the sum of individual estimates (P < .05), suggesting interaction effects. Loneliness had the greatest impact on young adults (15-24 years), whereas social isolation affected middle-aged females (25-44 years) the most. Results were robust across sensitivity analyses, except that applying the UK weighting algorithm yielded smaller estimates and no significant interaction effects. CONCLUSIONS: SIL is independently associated with reduced health utility, with some variation by age and sex. Potential interaction effects of SIL on health utility should be considered in economic evaluation, while recognizing their sensitivity to the choice of weighting algorithm.

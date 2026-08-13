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

## Pac8b8a0f9570

- Year: 2024
- Linked people: Chris Sampson
- Title: Marginal cost per QALY estimates: What are they good for?

Abstract:

Estimates of the marginal cost per quality-adjusted life year (MCPQ) are available for health care systems worldwide. Researchers routinely make claims about these estimates and how they should inform policymaking. This commentary considers these claims by taking a recent article from Health Policy as a case study. Claims are made about the past performance of the health service and about future decisions and relate to such considerations as productivity, the impact of technology approvals, cost-effectiveness thresholds, and budget allocation. We argue that the evidence does not justify these claims and MCPQ estimates should instead inform questions about the consequences of changes in expenditure.

## Pbc1436a73cd1

- Year: 2023
- Linked people: Nick Bansback
- Title: Canadian Rheumatology Association Living Guidelines for Rheumatoid Arthritis: Update #1.

Abstract:

We have updated the Canadian Rheumatology Association (CRA) guidelines for rheumatoid arthritis, with a series of best practice statements and a recommendation for the choice of disease-modifying antirheumatic drug therapy after an inadequate response to tumor necrosis factor inhibitors (TNFi).These add to our prior recommendation for tapering of advanced therapy. 1 The full list of best practice statements and treatment recommendations is summarized (Table ).Readers should always consult the online version of the guideline, 2 which will always be the latest version with all recommendations, and include important contextual information for each recommendation, along with supporting evidence summaries.The online version is available via an interactive web-based platform for guideline authoring and publication (MAGICapp) and can be accessed directly (https://app.magicapp.org/#/guideline/jNxw7n)or through the CRA website (www.rheum.ca).The recommendations and statements were developed using the Grading of Recommendations, Assessment, Development and Evaluation (GRADE) approach. 3Consistent with CRA processes, a full evidence-to-decision framework that summarizes the evidence and rationale for the recommendation is available for each treatment recommendation in the online version of the guideline.For the best practice statements, we present an explicit rationale for each statement following GRADE guidance, 4 also available in the online version of the guideline.We will continue to develop recommendations over time, and these will be added to the online version of the guideline on MAGICapp as they are developed.

## P362be7fa8a06

- Year: 2024
- Linked people: 
- Title: A Collection of Components to Design Clinical Dashboards Incorporating Patient-Reported Outcome Measures: Qualitative Study

Abstract:

BACKGROUND: A clinical dashboard is a data-driven clinical decision support tool visualizing multiple key performance indicators in a single report while minimizing time and effort for data gathering. Studies have shown that including patient-reported outcome measures (PROMs) in clinical dashboards supports the clinician's understanding of how treatments impact patients' health status, helps identify changes in health-related quality of life at an early stage, and strengthens patient-physician communication. OBJECTIVE: This study aims to determine design components for clinical dashboards incorporating PROMs to inform software producers and users (ie, physicians). METHODS: We conducted interviews with software producers and users to test preselected design components. Furthermore, the interviews allowed us to derive additional components that are not outlined in existing literature. Finally, we used inductive and deductive coding to derive a guide on which design components need to be considered when building a clinical dashboard incorporating PROMs. RESULTS: A total of 25 design components were identified, of which 16 were already surfaced during the literature search. Furthermore, 9 additional components were derived inductively during our interviews. The design components are clustered in a generic dashboard, PROM-related, adjacent information, and requirements for adoption components. Both software producers and users agreed on the primary purpose of a clinical dashboard incorporating PROMs to enhance patient communication in outpatient settings. Dashboard benefits include enhanced data visualization and improved workflow efficiency, while interoperability and data collection were named as adoption challenges. Consistency in dashboard design components is preferred across different episodes of care, with adaptations only for disease-specific PROMs. CONCLUSIONS: Clinical dashboards have the potential to facilitate informed treatment decisions if certain design components are followed. This study establishes a comprehensive framework of design components to guide the development of effective clinical dashboards incorporating PROMs in health care practice.

## P86fc5ae55eaa

- Year: 2023
- Linked people: Sander van Kuijk
- Title: Picking Up the Threads: Long-Term Outcomes of the Sutured Haemorrhoidopexy: A Retrospective Single-Centre Cohort Study

Abstract:

BACKGROUND: This study aimed to assess the short- and long-term safety and efficacy of the sutured haemorrhoidopexy (SH) in patients with haemorrhoidal disease (HD). METHODS: A retrospective study was performed, assessing the following treatment characteristics: number of sutures needed; operation time; perioperative complications; postoperative pain; hospital stay. The short- and long-term postoperative complications, HD recurrence and data on current HD symptoms were assessed according to the Core Outcome Set for HD. RESULTS: Between January 2009 and December 2021, 149 patients with HD underwent a SH. One-hundred and forty-five patients were included, with a mean age of 61 years (±12.8), of which 70 were women (48.3%). Patients were predominantly diagnosed with grade III (37.2%) HD and the median follow-up was nine years (5-11). Perioperative complications occurred in four cases (2.8%). In two patients (1.4%), short-term postoperative complications were reported, and in seven patients (6.2%), long-term complications were reported. The cumulative efficacy in terms of freedom of recurrence was 88.3% (95% CI, 83.1-93.5) at six months, 80.0% (95% CI, 73.5-86.5) at one year, and 67.7% (95% CI, 59.7-75.7) at five years. CONCLUSIONS: Sutured haemorrhoidopexy is a safe treatment for patients with HD and can be proposed as a minimally invasive surgical treatment if basic and outpatient procedures fail.

## P7f4a68e7c1da

- Year: 2024
- Linked people: Nick Bansback
- Title: A scoping review of triage approaches for the referral of patients with suspected inflammatory arthritis, from primary to rheumatology care.

Abstract:

We aimed to (1) identify existing triage approaches for referral of patients with suspected inflammatory arthritis (IA) from primary care physicians (PCP) to rheumatologists, (2) describe their characteristics and methodologies for clinical use, and (3) report their level of validation for use in a publicly funded healthcare system. The comprehensive search strategy of multiple databases up to October 2023 identified relevant literature and focussed on approaches applied at the PCP-Rheumatologist referral stage. Primary, quantitative studies, reported in English were included. Triage approaches were grouped into patient conditions as defined by the authors of the reports, including IA, its subtypes and combinations. 13952 records were identified, 425 full text reviewed and 55 reports of 53 unique studies were included. Heterogeneity in disease nomenclature and study sample pretest probability was found. The number of published studies rapidly increased after 2012. Studies were mostly from Europe and North America, in IA and Axial Spondyloarthritis (AxSpa). We found tools ranging the continuum of development with those best performing, indicated by the area under the receiver operating curve (AUC) >0.8), requiring only patient-reported questions. There were AUCs for some tools reported from multiple studies, these were in the outstanding to excellent range for the Early IA Questionnaire (EIAQ) (0.88 to 0.92), acceptable for the Case Finding AxSpa (CaFaSpa) (0.70 to 0.75), and poor to outstanding for the Psoriasis Epidemiology Screening Tool (PEST) (0.61 to 0.91). Given the clinical urgency to improve rheumatology referrals and considering the good.

## Pc1c0ce199b1a

- Year: 2022
- Linked people: Eliza Wong
- Title: The association between healthcare needs, socioeconomic status, and life satisfaction from a Chinese rural population cohort, 2012–2018

Abstract:

This study aimed to examine the prevalence of unmet healthcare needs and clarify its impact on socioeconomic status (SES) and life satisfaction in a longitudinal cohort of the Chinese rural population. Data used in this study were obtained from a nationally representative sample of 1387 eligible rural residents from the Chinese Family Panel Studies. Generalized estimating equation (GEE) logistic regression models were used to examine the factors associated with unmet healthcare needs and the impact of unmet healthcare needs on respondents' perceived SES and life satisfaction. Approximately 34.6% of respondents were male, 18.2% were ≤ 40 years, and 66.7% had completed primary education or below. Around 19% and 32.6% of individuals who healthcare needs were met reported an above average socioeconomic status and life satisfaction, respectively in the baseline survey. GEE models demonstrated that unmet healthcare needs were significantly associated with low perceived SES (Odds ratio = 1.57, p < 0.001) and life satisfaction (Odds ratio = 1.23, p = 0.03) adjusted by covariates. Respondents who were older, reported moderate or severe illness, and with chronic conditions were more likely to report the unmet healthcare needs.Unmet healthcare needs are longitudinally associated with low SES and life satisfaction among the Chinese rural population, the disparity in access to healthcare exists among this population.

## Pf3416aaac89f

- Year: 2023
- Linked people: Ilias Goranitis
- Title: Determining the utility of diagnostic genomics: a conceptual framework

Abstract:

BACKGROUND: Diagnostic efficacy is now well established for diagnostic genomic testing in rare disease. Assessment of overall utility is emerging as a key next step, however ambiguity in the conceptualisation and measurement of utility has impeded its assessment in a comprehensive manner. We propose a conceptual framework to approach determining the broader utility of diagnostic genomics encompassing patients, families, clinicians, health services and health systems to assist future evidence generation and funding decisions. BODY: Building upon previous work, our framework posits that utility of diagnostic genomics consists of three dimensions: the domain or type and extent of utility (what), the relationship and perspective of utility (who), and the time horizon of utility (when). Across the description, assessment, and summation of these three proposed dimensions of utility, one could potentially triangulate a singular point of utility axes of type, relationship, and time. Collectively, the multiple different points of individual utility might be inferred to relate to a concept of aggregate utility. CONCLUSION: This ontological framework requires retrospective and prospective application to enable refinement and validation. Moving forward our framework, and others which have preceded it, promote a better characterisation and description of genomic utility to inform decision-making and optimise the benefits of genomic diagnostic testing.

## Pd91db5851d8b

- Year: 2022
- Linked people: Elske van den Akker-van Marle
- Title: Physiological-based cord clamping in very preterm infants: the Aeration, Breathing, Clamping 3 (ABC3) trial—study protocol for a multicentre randomised controlled trial

Abstract:

BACKGROUND: International guidelines recommend delayed umbilical cord clamping (DCC) up to 1 min in preterm infants, unless the condition of the infant requires immediate resuscitation. However, clamping the cord prior to lung aeration may severely limit circulatory adaptation resulting in a reduction in cardiac output and hypoxia. Delaying cord clamping until lung aeration and ventilation have been established (physiological-based cord clamping, PBCC) allows for an adequately established pulmonary circulation and results in a more stable circulatory transition. The decline in cardiac output following time-based delayed cord clamping (TBCC) may thus be avoided. We hypothesise that PBCC, compared to TBCC, results in a more stable transition in very preterm infants, leading to improved clinical outcomes. The primary objective is to compare the effect of PBCC on intact survival with TBCC. METHODS: > 85% while using supplemental oxygen < 40%. In the control TBCC group, cord clamping is time based at 30-60 s. The primary outcome is survival without major cerebral and/or intestinal injury. Preterm infants born before 30 weeks of gestation are included after prenatal parental informed consent. The required sample size is 660 infants. DISCUSSION: The findings of this trial will provide evidence for future clinical guidelines on optimal cord clamping management in very preterm infants at birth. TRIAL REGISTRATION: ClinicalTrials.gov NCT03808051. First registered on January 17, 2019.

## P89a9bfcf586f

- Year: 2023
- Linked people: Jan Abel Olsen
- Title: The relative importance of education and health behaviour for health and wellbeing.

Abstract:

BACKGROUND: Indicators of socioeconomic position (SEP) and health behaviours (HB) are widely used predictors of health variations. Their relative importance is hard to establish, because HB takes a mediating role in the link between SEP and health. We aim to provide new knowledge on how SEP and HB are related to health and wellbeing. METHODS: The analysis considered 14,713 Norwegians aged 40-63. Separate regressions were performed using two outcomes for health-related quality of life (EQ-5D-5 L; EQ-VAS), and one for subjective wellbeing (Satisfaction with Life Scale). As predictors, we used educational attainment and a composite measure of HB - both categorized into four levels. We adjusted for differences in childhood financial circumstances, sex and age. We estimated the percentage share of each predictor in total explained variation, and the relative contributions of HB in the education-health association. RESULTS: The reference case model, excluding HB, suggests consistent stepwise education gradients in health-related quality of life. The gap between the lowest and highest education was 0.042 on the EQ-5D-5 L, and 0.062 on the EQ-VAS. When including HB, the education effects were much attenuated, making HB take the lion share of the explained health variance. HB contributes 29% of the education-health gradient when health is measured by EQ-5D-5 L, and 40% when measured by EQ-VAS. For subjective wellbeing, we observed a strong HB-gradient, but no education gradient. CONCLUSION: In the institutional context of a rich egalitarian country, variations in health and wellbeing are to a larger extent explained by health behaviours than educational attainment.

## P115a17da0ba1

- Year: 2023
- Linked people: Oriana Ciani
- Title: An accelerated access pathway for innovative high-risk medical devices under the new European Union Medical Devices and health technology assessment regulations? Analysis and recommendations.

Abstract:

INTRODUCTION: The new European Union (EU) Regulations for medical devices (MDs) and health technology assessment (HTA) are welcome developments that should increase the quality of clinical evidence for MDs and reduce fragmentation in the EU market access process. To fully exploit anticipated benefits, their respective assessment processes should be closely coordinated, particularly for promising, highly innovative MDs. Accelerated approval is worth exploring for certain categories of high-risk MDs to keep the EU regulatory process competitive compared to accelerated MD approval programs elsewhere (e.g. US). AREAS COVERED: Problems observed in worldwide accelerated drug and MD regulatory approval programs are reviewed, including greater uncertainty in premarket clinical evidence generation and lack of oversight for post approval evidence requirements. Implications for MD approval, HTA and coverage are explored. EXPERT OPINION: Through analysis of two decades of drug and MD accelerated approval programs worldwide, recommendations for an Accelerated Access Pathway for select innovative, high-risk MDs are proposed to fit the EU context, leverage the two new regulations, increase opportunities for Expert Panels to provide timely advice regarding manufacturers' evidence generation plans along the MD lifecycle (pre, postmarket), and safely speed patient access while promoting increased collaboration among Member States on coverage decisions.

## P3f004c444d24

- Year: 2026
- Linked people: Emelie Heintz
- Title: Informing decisions in light of parameter uncertainty - an economic evaluation of the adjuvanted recombinant herpes zoster vaccine in Sweden.

Abstract:

BACKGROUND: Many studies of the adjuvanted recombinant zoster vaccine (RZV) consider it cost-effective using efficacy estimates from randomized trials (RCTs). However, the effect magnitude differs between RCTs and observational studies, in addition to other input parameters that have shown to greatly impact cost-effectiveness. The aim of the current study is to assess the economic case of the RZV in Sweden and assess at which price the vaccine would be considered cost-effective. METHODS: A decision-analytic model was used to estimate the health economic impact of introducing RZV in Sweden. Five-year age-cohorts were modelled between ages 65 to 100+, comparing the cost-effectiveness of two-dose RZV to no vaccination from a health care perspective, using efficacy data from RCTs and observational estimates. The model was run over a lifetime time horizon with quality adjusted life years (QALYs) as the outcome. Multiple one-way and probabilistic sensitivity analyses were conducted to analyze the impact of parameter uncertainty. RESULTS: At a willingness-to-pay of 80,000 Euro per QALY, the RZV was cost-effective across cohorts at a price per dose of 80 to 105 Euro in basecase analyses, in contrast to the current market price at 176 Euro. However, due to parameter uncertainty, the price per dose at which the RZV may be considered cost-effective varies between as high as the current market price to less than 10% of that price, depending on which input variables are used. CONCLUSION: The price at which the RZV would be considered cost-effective varies greatly, highlighting the need to explore and consider parameter uncertainty in both analyses and procurement negotiations.

## P0447e9fa39b4

- Year: 2023
- Linked people: Jan Busschbach
- Title: Patients’ Preferences Towards Decision Counseling for Active Surveillance After Neoadjuvant Chemoradiotherapy for Esophageal Cancer

Abstract:

BACKGROUND: Decision counseling (DC) is offered to enable patients to reflect on their treatment preferences and to think through the consequences of alternative treatment options. However, the timing of DC is debatable. In this study, patients who underwent DC at different times were interviewed about their experiences, specifically focusing on the timing of DC. METHODS: Patients with locally advanced esophageal cancer eligible for participation in a prospective cohort study on active surveillance (SANO-2 study) were offered DC either before or after neoadjuvant chemoradiotherapy (nCRT). Structured interviews were conducted by phone 1 week after DC, and responses were analyzed using frequency counts for the answers to set response categories. The primary outcome was the preferred time to receive DC, while the secondary outcome was the overall experience of patients with DC. RESULTS: Overall, 40 patients were offered DC between 2021 and 2023. Patients who had counseling before the start of nCRT (n = 20) were satisfied with the timing of DC. Of the 20 patients who had DC after nCRT, 6 would have preferred counseling at an earlier time point. Patients who had DC both before or after the completion of nCRT reflected positively on DC. CONCLUSION: It is recommended to introduce the option of DC as early as possible and discuss with the patient at which moment during the decision-making process they prefer to discuss all treatment options more extensively.

## Pcb62a9a5c75e

- Year: 2026
- Linked people: Iwan van der Horst
- Title: Cerebral monitoring responses to bedside physiological challenges in comatose post-cardiac arrest patients.

Abstract:

To evaluate the effects of three simple bedside challenges on cerebral oxygenation and brain activity, measured non-invasively using near-infrared spectroscopy (NIRS) and frontal single-channel electroencephalography (EEG), in comatose post-cardiac arrest patients, and to examine whether these responses differ according to cerebral autoregulation status and intensive care unit (ICU) outcome and could aid early prognostication. Three bedside physiological challenges were conducted: (1) increasing the fraction of inspired oxygen (FiO₂) to 100%, (2) lowering the head-of-bed (HOB) to 0°, and (3) elevating end-tidal carbon dioxide (etCO₂) by 1.0 kPa. Tissue oxygen saturation (StO₂) and EEG amplitude were hypothesized to increase, by enhancing oxygen delivery (FiO₂), augmenting cerebral perfusion pressure (HOB), and inducing cerebral vasodilation (etCO₂). Furthermore, we examined the associations between signal responses, cerebral autoregulation status, and ICU outcome. Of the 48 monitored patients, FiO2, HOB, and etCO₂ challenges were successfully completed in 41 (85%), 33 (69%), and 32 (67%) patients, respectively. The StO₂ increased on average by 0.3% (95%-CI 0.2-0.5, p < 0.001) for every 10% rise in FiO2, and 1.94% (95%-CI 0.9-3.0, p < 0.001) for each 15º lowering of the HOB. The etCO₂ challenge did not affect the StO₂. EEG amplitude remained unchanged during all three challenges. No significant differences were found in the responses between patients with intact versus impaired autoregulation or between the ICU outcome groups. Brief physiological challenges simulating common ICU scenarios elicited only modest increases in StO₂, and no measurable response in EEG amplitude. Response patterns were not associated with cerebral autoregulation status or ICU outcome.

## P31c4ebd69352

- Year: 2021
- Linked people: Martin Härter
- Title: Profiles of patients’ self-reported health after acute stroke

Abstract:

BACKGROUND: We aimed to identify groups of patients with similar health status after stroke, assessed by patient reported outcome measures (PROMs), to improve initial risk stratification. METHODS: In a prospective study, inpatients were recruited during acute stroke treatment. Demographics, history, and cardio-vascular risk factors were assessed at baseline. Self-reported functional status, physical and mental health as well as anxiety and depressive symptoms were assessed 3 and 12 months after stroke and used to identify latent classes. The association of patient characteristics with latent class membership was investigated with multinomial logistic regression. RESULTS: Of the 650 patients included with a mean age of 75 years and 48% female, 70% had ischemic, 6% hemorrhagic strokes, and 24% transient ischemic attacks. Median NIHSS on admission was 2 (IQR:0,5). Values of PROMs remained comparable at 3 and 12 months. A three-class model was developed, differentiating between patients with mildly (75%), moderately (17%), and severely (8%) impaired self-reported health status. Adjusted for univariately significant baseline characteristics, initial NIHSS distinguished mild- from moderate-, and moderate- from severe-class-membership (p < 0.001). Length of inpatient stay (p < 0.001;OR = 1.1), diabetes (p = 0.021;OR = 1.91), and atrial fibrillation (p = 0.004;OR = 2.20) predicted allocation to the moderately vs. mildly affected class. CONCLUSIONS: Grading stroke patients by a standard set of PROMs up to 1 year after stroke allows to distinguish the diverse impact of baseline characteristics on differently affected groups. In addition to initial stroke severity, longer inpatient stay, presence of diabetes and atrial fibrillation correlate with greater impairment of self-reported health in the less affected groups. TRIAL REGISTRATION: http://www.ClinicalTrials.gov ; Unique identifier: NCT03795948 .

## P2502afb0c8f0

- Year: 2021
- Linked people: Matthijs Versteegh, Maureen Rutten-van Molken
- Title: Guidance for the Harmonisation and Improvement of Economic Evaluations of Personalised Medicine.

Abstract:

OBJECTIVE: The objective of this study was to develop guidance contributing to improved consistency and quality in economic evaluations of personalised medicine (PM), given current ambiguity about how to measure the value of PM as well as considerable variation in the methodology and reporting in economic evaluations of PM. METHODS: A targeted literature review of methodological papers was performed for an overview of modelling challenges in PM. Expert interviews were held to discuss best modelling practice. A systematic literature review of economic evaluations of PM was conducted to gain insight into current modelling practice. The findings were synthesised and used to develop a set of draft recommendations. The draft recommendations were discussed at a stakeholder workshop and subsequently finalised. RESULTS: Twenty-two methodological papers were identified. Some argued that the challenges in modelling PM can be addressed within existing methodological frameworks, others disagreed. Eighteen experts were interviewed. They believed large uncertainty to be a key concern. Out of 195 economic evaluations of PM identified, 56% addressed none of the identified modelling challenges. A set of 23 recommendations was developed. Eight recommendations focus on the modelling of test-treatment pathways. The use of non-randomised controlled trial data is discouraged but several recommendations are provided in case randomised controlled trial data are unavailable. The parameterisation of structural uncertainty is recommended. Other recommendations consider perspective and discounting; premature survival data; additional value elements; patient and clinician compliance; and managed entry agreements. CONCLUSIONS: This study provides a comprehensive list of recommendations to modellers of PM and to evaluators and reviewers of PM models.

## P41d6b7a96d0f

- Year: 2025
- Linked people: Sander van Kuijk
- Title: Defining centres of expertise for minimally invasive mitral valve surgery: a systematic review and volume–outcome meta-analysis

Abstract:

BACKGROUND: Minimally invasive mitral valve surgery (MIMVS) is increasingly performed, but outcomes such as repair rate, mortality and survival likely depend on expertise. Still, the definition of a high-volume centre varies in the literature and lacks an evidence-based substantiation. Consequently, this study aims to determine the volume-outcome relation in MIMVS in conjunction with a volume threshold, in order to define 'high-volume centres', applying a novel statistical concept. METHODS: The study was preregistered in PROSPERO (CRD42022376293, registered 26 November 2022). A systematic search was applied to three databases, including consecutive patients undergoing MIMVS. Studies describing patients undergoing transcatheter procedures were excluded. Restricted cubic spline analyses were applied and the elbow method was used to retrieve the threshold volume. Long-term outcomes were analysed using reconstructed Kaplan-Meier curves and a novel statistical concept to assess the volume-outcome relation for time-to-event outcomes was applied. The primary outcome was early mortality, secondary outcomes were repair rate, stroke, and long-term survival, freedom from reoperation, and freedom from more than moderate mitral regurgitation. Leave-one-out analyses were performed for sensitivity purposes. RESULTS: Data from 68 unique centres were included (n=23 495 patients). Early mortality was 1.3% (95% CI 1.1% to 1.6%), without a statistically significant non-linear relation for this endpoint, nor for stroke. There was a statistically significant volume-outcome relation for mitral valve repair rate (p=0.018). Based on the repair rate, the threshold to define a high-volume centre was 60 cases/year (number needed to treat to prevent a replacement ≤7). A significant volume-outcome relation was observed for long-term outcomes as well, with a threshold of 53 and 54 cases/year for long-term survival and freedom from reoperation, respectively. These results were robust across the sensitivity analyses for the various endpoints. CONCLUSIONS: The threshold to define a high-volume centre ranges between 53 and 60 cases/year based on repair rate, long-term survival and freedom-from reoperation. These findings have the potential to facilitate centralisation of MIMVS.PROSPERO registration numberCRD42022376293.

## P0713cd99c86e

- Year: 2025
- Linked people: Caitlyn Solem
- Title: Patient and Physician Preferences for Maintenance Treatment in Advanced Non-Small Cell Lung Cancer: Insights into Treatment Selection

Abstract:

Introduction Advanced/metastatic non-small cell lung cancer (a/mNSCLC) is associated with a poor prognosis. Although maintenance therapy after first-line (1L) induction treatment can extend survival, it may also present with drawbacks like risk of certain adverse events (AEs), underscoring the need for shared decision-making between patients and their treating physicians. This study aimed to quantify the extent to which maintenance treatment attributes impact the preferences of patients and physicians after 1L induction therapy for a/mNSCLC. Methods Eligible patients (aged ≥ 18 years in the UK and US) were diagnosed with a/mNSCLC and had stable disease with or responded to 1L induction therapy. Eligible physicians were licensed oncologists with ≥ 5 years' experience in a/mNSCLC treatment who had treated ≥ 20 such patients in the past year. Surveys assessed the patients' and physicians' perspectives regarding the current treatment landscape of a/mNSCLC, and a discrete choice experiment assessed their preferences regarding treatment characteristics. Data were collected using choice cards, designed to capture treatment attribute preferences including efficacy (progression-free survival [PFS] and overall survival [OS]), chance (risk) of new brain metastasis (BM), and selected AEs. Results Among 34 UK and 48 US patients, the three most important treatment attributes (in order) were chance of new BM, OS, and risk of severe neutropenia. Among 51 UK and 50 US treating physicians, the 3 most important treatment attributes (in order) were OS, chance of new BM, and PFS. Conclusion In this real-world survey, OS and chance of new BM were the two most important maintenance treatment attributes for patients with a/mNSCLC and treating physicians. However, the risk of severe neutropenia carried greater relative importance, while PFS carried lesser relative importance, for patients than physicians. These results highlight the differing emphasis placed on attributes by patients and physicians when selecting maintenance treatment.

## Pfd374421886a

- Year: 2022
- Linked people: Kelly de Ligt
- Title: Opportunities and obstacles in linking large health care registries: the primary secondary cancer care registry - breast cancer

Abstract:

BACKGROUND: The growing volume of health data provides new opportunities for medical research. By using existing registries, large populations can be studied over a long period of time. Patient-level linkage of registries leads to even more detailed and extended information per patient, but brings challenges regarding responsibilities, privacy and security, and quality of data linkage. In this paper we describe how we dealt with these challenges when creating the Primary Secondary Cancer Care Registry (PSCCR)- Breast Cancer. METHODS: The PSCCR - Breast Cancer was created by linking two existing registries containing data on 1) diagnosis, tumour and treatment characteristics of all Dutch breast cancer patients (NCR), and 2) consultations and diagnoses from primary care electronic health records of about 10% of Dutch GP practices (Nivel-PCD). The existing registry governance structures and privacy regulations were incorporated in those of the new registry. Privacy and security risks were reassessed. Data were restricted to females and linked using postal code and date of birth. The breast cancer diagnosis was verified in both registries and for a subsample of 44 patients with the GP as well. RESULTS: A collaboration agreement was signed in which the organisations retained data responsibility and accountability for 'their' registry. A Trusted Third Party performed the record linkage. Ten percent of the patients with breast cancer could be linked to the primary care registry, as was expected based on the coverage of Nivel-PCD, and finally 7 % could be included. The breast cancer diagnosis was verified by the GP in 42 of the 44 patients. CONCLUSIONS: We developed and validated a procedure for patient-level linkage of health data registries without a unique identifier, while preserving the integrity and privacy of the original registries. The method described may help researchers wishing to link existing health data registries.

## P18cabf5bdd52

- Year: 2022
- Linked people: Ciaran O'Neill
- Title: Survival of cancer patients with pre-existing heart disease

Abstract:

BACKGROUND: While cancer outcomes have improved over time, in Northern Ireland they continue to lag behind those of many other developed economies. The role of comorbid conditions has been suggested as a potential contributory factor in this but issues of data comparability across jurisdictions has inhibited efforts to explore relationships. We use data from a single jurisdiction of the UK using data from - the Northern Ireland Cancer Registry (NICR), to examine the association between mortality (all-cause and cancer specific) and pre-existing cardiovascular diseases among patients with cancer. MATERIALS AND METHODS: All patients diagnosed with cancer (excluding non-melanoma skin cancer) between 2011 and 2014 were identified from Registry records. Those with a pre-existing diagnosis of cardiovascular diseases were identified by record linkage with patient hospital discharge data using ICD10 codes. Survival following diagnosis was examined using descriptive statistics and Cox proportional hazards regression analyses. Analyses examined all-cause mortality and cancer specific mortality for lung, colorectal, breast and prostate cancer. As well as cardiovascular diseases, regression models controlled for age, gender (where appropriate), deprivation (as quintiles), stage at diagnosis and other comorbidities. RESULTS: Almost 35,000 incident cancer cases were diagnosed during the study period of which approximately 23% had a prior heart condition. The pan-cancer hazard ratio for death in the presence of pre-existing cardiovascular diseases was 1.28 (95% CI: 1.18-1.40). All-cause and cancer specific mortality was higher for patients with cardiovascular diseases across lung, female breast, prostate and colorectal cancer groups after controlling for age, gender (where appropriate), deprivation (as quintiles), stage at diagnosis and other comorbidities. CONCLUSION: Pre-existing morbidity may restrict the treatment of cancer for many patients. In this cohort, cancer patients with pre-existing cardiovascular diseases had poorer outcomes than those without cardiovascular diseases. A high prevalence of cardiovascular diseases may contribute to poorer cancer outcomes at a national level.

## P78fc39bb9422

- Year: 2023
- Linked people: Ilias Goranitis, Kim Dalziel
- Title: Uptake of funded genomic testing for syndromic and non-syndromic intellectual disability in Australia.

Abstract:

Lack of reimbursement for genomic testing in rare diseases is recognized as one of the principal barriers to wider implementation within healthcare systems [ 1 ]. Multiple studies have provided evidence for diagnostic and clinical utility and for the cost-effectiveness of genomic testing in rare diseases, leading to testing being funded across a range of public and private healthcare systems worldwide [ 2 ].

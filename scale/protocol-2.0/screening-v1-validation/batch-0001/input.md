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

## P346af7659df3

- Year: 2024
- Linked people: Gerard De Pouvourville
- Title: Generalized pustular psoriasis: A nationwide population-based study using the National Health Data System in France

Abstract:

BACKGROUND: GPP is a rare, chronic, neutrophilic skin disease, with limited real-world data characterizing patients with flares and the impact of flares on disease progression and morbidity. OBJECTIVE: Describe the clinical characteristics of patients with GPP, comorbidities, disease epidemiology and frequency and severity of flares, and compare patients with GPP with a matched severe psoriasis population. METHODS: In this population-based real-world cohort study an algorithm was developed to identify patients with GPP flares. Three cohorts were identified using the Système National des Données de Santé (SNDS) database covering almost the entire French population; a prevalent cohort (2010-2018), an incident cohort (2012-2015). A severe psoriasis cohort was compared with the GPP incident cohort using propensity score matching. RESULTS: The prevalent and incident cohorts comprised 4195 and 1842 patients, respectively. In both cohorts, mean age was 58 years; 53% were male. Comorbidities were significantly more common in the incident cohort versus matched psoriasis cohort, respectively, including hypertension (44% vs. 26%), ischaemic heart disease (26% vs. 18%) and hyperlipidaemia (25% vs. 15%). In the incident cohort, the flare rate was 0.1 flares/person-year and 0.4 flares/person-year among the 569 out of 1842 patients hospitalized with flares. These patients had a mean (±SD) stay of 11.6 ± 10.4 days; 25% were admitted to the intensive care unit. In 2017, the cumulative incidence and cumulative GPP age-sex standardized prevalence were 7.1 and 45.2 per million, respectively. CONCLUSIONS: Patients with GPP had a distinct comorbidity profile compared to patients with severe psoriasis, and GPP flares were associated with long hospitalizations.

## P3c2a48f0eb38

- Year: 2016
- Linked people: Piyameth Dilokthornsakul
- Title: Healthcare utilization and cost of Stevens-Johnson syndrome and toxic epidermal necrolysis management in Thailand

Abstract:

BACKGROUND: Stevens-Johnson syndrome (SJS) and Toxic Epidermal Necrolysis (TEN) are life-threatening dermatologic conditions. Although, the incidence of SJS/TEN in Thailand is high, information on cost of care for SJS/TEN is limited. This study aims to estimate healthcare resource utilization and cost of SJS/TEN in Thailand, using hospital perspective. METHODS: A retrospective study using an electronic health database from a university-affiliated hospital in Thailand was undertaken. Patients admitted with SJS/TEN from 2002 to 2007 were included. Direct medical cost was estimated by the cost-to-charge ratio. Cost was converted to 2013 value by consumer price index, and converted to $US using 31 Baht/ 1 $US. The healthcare resource utilization was also estimated. RESULTS: A total of 157 patients were included with average age of 45.3±23.0 years. About 146 patients (93.0%) were diagnosed as SJS and the remaining (7.0%) were diagnosed as TEN. Most of the patients (83.4%) were treated with systemic corticosteroids. Overall, mortality rate was 8.3%, while the average length of stay (LOS) was 10.1±13.2 days. The average cost of managing SJS/TEN for all patients was $1,064±$2,558. The average cost for SJS patients was $1,019±$2,601 while that for TEN patients was $1,660±$1,887. CONCLUSIONS: Healthcare resource utilization and cost of care for SJS/TEN in Thailand were tremendous. The findings are important for policy makers to allocate healthcare resources and develop strategies to prevent SJS/TEN which could decrease length of stay and cost of care.

## Pd85947fcb4e8

- Year: 2022
- Linked people: Ciaran O'Neill
- Title: Examining the transnational preventive healthcare utilisation of a group of Eastern European migrants living full-time in another European state

Abstract:

Migrants in Europe are shown to have consistently lower uptake of preventive healthcare compared to European host populations. This paper examines how the transnational preventive care use of Eastern European migrants in their country of origin may be associated with preventive care uptake in their European host country. Preventive care use data in Ireland was collected on 119 Polish migrants and 123 native Irish from June 2018 to September 2019. Preventive care use data was also collected on the Polish migrant group in Poland during the same period. Preventive care use was captured by examining general practitioner visits, blood or urine test uptake, and cancer screening uptake. Probit models were first estimated to examine whether the Polish migrants were more or less likely to have used each service in Ireland than the native Irish. Second, three bivariate probit models were estimated to examine the use of each service by the Polish migrants only in Ireland and Poland as the two dependant variables. The Polish migrants are less likely to have GP visits, blood or urine test uptake, and cancer screening uptake in Ireland compared to the native Irish. The Polish migrants from this study are also shown to potentially substitute blood or urine test uptake in Ireland for uptake in Poland. Transnational ties can determine the preventive care utilisation of migrants in Europe.

## P9b77a57aa69d

- Year: 1990
- Linked people: Ben Van Hout
- Title: EuroQol-a new facility for the measurement of health-related quality of life

Abstract:

In the course of developing a standardised, non-disease-specific instrument for describing and valuing health states (based on the items in Table 1), the EuroQol Group (whose members are listed in the Appendix) conducted postal surveys in England, The Netherlands and Sweden which indicate a striking similarity in the relative valuations attached to 14 different health states. The data were collected using a visual analogue scale similar to a thermometer. The EuroQol instrument is intended to complement other quality-of-life measures and to facilitate the collection of a common data set for reference purposes. Others interested in participating in the extension of this work are invited to contact the EuroQol Group.

## P5a10aa051f45

- Year: 2019
- Linked people: Ben Van Hout
- Title: Comparison of quality of life measurements: EQ-5D-5L versus disease/treatment-specific measures in pulmonary embolism and deep vein thrombosis

Abstract:

There is a lack of performance comparisons of the generic quality of life tool EQ-5D-5L against disease- and treatment-specific measures in venous thromboembolism (VTE). The aim of this study was to compare EQ-5D-5L against the pulmonary embolism (PE)-specific PEmb-QoL and the deep vein thrombosis (DVT)-specific VEINES-QOL/Sym, and PACT-Q2 (treatment-specific) questionnaires in five language settings. PREFER in VTE was a non-interventional disease registry conducted between 2013 and 2014 in primary and secondary care across seven European countries with five languages, including English, French, German, Italian and Spanish. Consecutive patients with acute PE/DVT were enrolled and followed over 12 months. Only patients who completed all three questionnaires at baseline were included in the study sample. The psychometric properties examined included acceptability (missing, ceiling and floor effects), validity (convergent and known-groups validity), and responsiveness. Known groups validity and responsiveness were assessed using both effect size (Cohen's d) and relative efficiency (F-statistic). All analyses were conducted in each language version and the total sample across all languages. A total of 1054 PE and 1537 DVT patients were included. 14% of PE and 10% of DVT patients had the maximum EQ-5D-5L index score. EQ-5D-5L was low to moderately correlated with other measures (r < 0.5). EQ-5D-5L was associated with larger effect size/relative efficiency in most of known group comparisons in both VTE groups. Similar results were observed for responsiveness. EQ-5D-5L performed relatively better in French, Italian and Spanish language versions. Overall EQ-5D-5L is comparable to PEmb-QoL, VEINES-QOL/Sym and PACT-Q2 in terms of acceptability, validity and responsiveness in both PE and DVT populations in English, French, German, Italian and Spanish language version. Nevertheless, it should be noted that each measure is designed to capture different aspects of health-related quality of life.

## P46000c7cbbe8

- Year: 2024
- Linked people: Gerard De Pouvourville
- Title: The Determination of Diabetes Utilities, Costs, and Effects Model: A Cost-Utility Tool Using Patient-Level Microsimulation to Evaluate Sensor-Based Glucose Monitoring Systems in Type 1 and Type 2 Diabetes: Comparative Validation

Abstract:

To assess the accuracy and validity of the Determination of Diabetes Utilities, Costs, and Effects (DEDUCE) model, a Microsoft-Excel-based tool for evaluating diabetes interventions for type 1 and type 2 diabetes. The DEDUCE model is a patient-level microsimulation, with complications predicted based on the Sheffield and Risk Equations for Complications Of type 2 diabetes models for type 1 and type 2 diabetes, respectively. For this tool to be useful, it must be validated to ensure that its complication predictions are accurate. Internal, external, and cross-validation was assessed by populating the DEDUCE model with the baseline characteristics and treatment effects reported in clinical trials used in the Fourth, Fifth, and Ninth Mount Hood Diabetes Challenges. Results from the DEDUCE model were evaluated against clinical results and previously validated models via mean absolute percentage error or percentage error. The DEDUCE model performed favorably, predicting key outcomes, including cardiovascular disease in type 1 diabetes and all-cause mortality in type 2 diabetes. The model performed well against other models. In the Mount Hood 9 Challenge comparison, error was below the mean reported from comparator models for several outcomes, particularly for hazard ratios. The DEDUCE model predicts diabetes-related complications from trials and studies well when compared with previously validated models. The model may serve as a useful tool for evaluating the cost-effectiveness of diabetes technologies.

## Pfdcafb278bd0

- Year: 2020
- Linked people: Gerard De Pouvourville
- Title: Current challenges for assessing the long-term clinical benefit of cancer immunotherapy: A multi-stakeholder perspective

Abstract:

Immuno-oncologics (IOs) differ from chemotherapies as they prime the patient's immune system to attack the tumor, rather than directly destroying cancer cells. The IO mechanism of action leads to durable responses and prolonged survival in some patients. However, providing robust evidence of the long-term benefits of IOs at health technology assessment (HTA) submission presents several challenges for manufacturers. The aim of this article was to identify, analyze, categorize, and further explore the key challenges that regulators, HTA agencies, and payers commonly encounter when assessing the long-term benefits of IO therapies. Insights were obtained from an international, multi-stakeholder steering committee (SC) and expert panels comprising of payers, economists, and clinicians. The selected individuals were tasked with developing a summary of challenges specific to IOs in demonstrating their long-term benefits at HTA submission. The SC and expert panels agreed that standard methods used to assess the long-term benefit of anticancer drugs may have limitations for IO therapies. Three key areas of challenges were identified: (1) lack of a disease model that fully captures the mechanism of action and subsequent patient responses; (2) estimation of longer-term outcomes, including a lack of agreement on ideal methods of survival analyses and extrapolation of survival curves; and (3) data limitations at the time of HTA submission, for which surrogate survival end points and real-world evidence could prove useful. A summary of the key challenges facing manufacturers when submitting evidence at HTA submission was developed, along with further recommendations for manufacturers in what evidence to produce. Despite almost a decade of use, there remain significant challenges around how best to demonstrate the long-term benefit of checkpoint inhibitor-based IOs to HTA agencies, clinicians, and payers. Manufacturers can potentially meet or mitigate these challenges with a focus on strengthening survival analysis methodology. Approaches to doing this include identifying reliable biomarkers, intermediate and surrogate end points, and the use of real-world data to inform and validate long-term survival projections. Wider education across all stakeholders-manufacturers, payers, and clinicians-in considering the long-term survival benefit with IOs is also important.

## P3ddd769fbcb7

- Year: 2016
- Linked people: Piyameth Dilokthornsakul
- Title: Long-Term Cost-Effectiveness of Insulin Glargine Versus Neutral Protamine Hagedorn Insulin for Type 2 Diabetes in Thailand

Abstract:

Even though Insulin glargine (IGlar) has been available and used in other countries for more than a decade, it has not been adopted into Thai national formulary. This study aimed to evaluate the long-term cost effectiveness of IGlar versus neutral protamine Hagedorn (NPH) insulin in type 2 diabetes from the perspective of Thai Health Care System. A validated computer simulation model (the IMS CORE Diabetes Model) was used to estimate the long-term projection of costs and clinical outcomes. The model was populated with published characteristics of Thai patients with type 2 diabetes. Baseline risk factors were obtained from Thai cohort studies, while relative risk reduction was derived from a meta-analysis study conducted by the Canadian Agency for Drugs and Technology in Health. Only direct costs were taken into account. Costs of diabetes management and complications were obtained from hospital databases in Thailand. Both costs and outcomes were discounted at 3 % per annum and presented in US dollars in terms of 2014 dollar value. Incremental cost-effectiveness ratio (ICER) was calculated. One-way and probabilistic sensitivity analyses were also performed. IGlar is associated with a slight gain in quality-adjusted life years (0.488 QALYs), an additional life expectancy (0.677 life years), and an incremental cost of THB119,543 (US$3522.19) compared with NPH insulin. The ICERs were THB244,915/QALY (US$7216.12/QALY) and THB176,525/life-year gained (LYG) (US$5201.09/LYG). The ICER was sensitive to discount rates and IGlar cost. At the acceptable willingness to pay of THB160,000/QALY (US$4714.20/QALY), the probability that IGlar was cost effective was less than 20 %. Compared to treatment with NPH insulin, treatment with IGlar in type 2 diabetes patients who had uncontrolled blood glucose with oral anti-diabetic drugs did not represent good value for money at the acceptable threshold in Thailand.

## Pd690862e6d04

- Year: 2000
- Linked people: Ciaran O'Neill
- Title: Do GPs working in practice with high or low prescribing costs have different views on prescribing cost issues?

Abstract:

BACKGROUND: In a previous study we found that a minority of general practitioners (GPs) had different views to health authority advisers on a number of prescribing cost issues. However, there were few differences between subgroups of GPs. We hypothesised that subgroups that might show differences were GPs from practices with either high or low prescribing costs. AIM: To assess differences in views on prescribing cost issues between GPs working in practices with either high or low prescribing costs. METHOD: Using PACTLINE data, prescribing costs were obtained for general practices within the Trent Region for the financial year 1996 to 1997. A questionnaire was sent anonymously to 340 GPs working in those practices with high prescribing costs, and to 322 GPs working in practices with the lowest prescribing costs. RESULTS: A total of 216 (63.5%) GPs from high-cost practices and 194 (60.2%) from low-cost practices responded. There were statistically significant differences between the two groups on seven out of 22 statements. However, when the confounding effect of fundholding was taken into account, significant differences were found for just three statements and each of these related to substitution with comparable but cheaper drugs. CONCLUSIONS: GPs working in practices with either high or low prescribing costs had different views on a number of statements concerning substitution with comparable but cheaper drugs. When encouraging GPs to control their prescribing costs, a different approach may be required for doctors in some high-cost practices.

## Pbf3bbda3b907

- Year: 2025
- Linked people: Ciaran O'Neill
- Title: An International Study of Variation in Attitudes to Kidney Biopsy Practice

Abstract:

Key Points Attitudes on kidney biopsy practice vary significantly across the world. Male clinicians, younger clinicians, and individuals who perform biopsies more frequently had an increased propensity to recommend a kidney biopsy. Kidney biopsy was most often recommended in the setting of higher proteinuria levels and preserved kidney function. Background A kidney biopsy is an essential investigation for diagnosis but is invasive and associated with complications. Delaying or missing the opportunity to diagnose kidney disease could result in adverse patient outcomes. The aim of this study was to examine attitudes to kidney biopsy across the world. Methods An online questionnaire for nephrologists was designed on the basis of the existing literature with input from patients. Anonymized data were collected on individual and institutional demographics, indications and contraindications for biopsy, and attitudes and barriers to access. A propensity-to-biopsy score was generated from responses, which allowed clinicians to compare their practice with international colleagues. A higher score was associated with an increased likelihood of recommending biopsy. The questionnaire was disseminated through international nephrology societies, including the National Kidney Foundation, and by social media. Results Participants responding to the questionnaire included 1181 clinicians from 83 countries, making it the largest international study in this area to date. The propensity-to-biopsy scores were significantly different between the 13 countries with over 20 clinicians participating ( P < 0.001) and was highest in Mexico and lowest in the Philippines. Kidney biopsy was most often recommended in patients with higher proteinuria levels and most often avoided in patients with small kidneys. An adjusted linear regression model demonstrated that a significantly higher propensity-to-biopsy score was found in male clinicians, younger clinicians, frequent performers of kidney biopsy, increased job seniority, and larger institution size ( P = 0.05). Conclusions Kidney biopsy practice is varied internationally and is subject to human and systemic factors. Further research is required to understand the variances behind clinical decision making.

## P9a49bb749c53

- Year: 1994
- Linked people: Ben Van Hout
- Title: Assessing the benefits of transplant services.

Abstract:

This chapter presents some methods for the assessment of transplant benefits, using the example of liver transplantation. An independent assessment of the benefits of medical technology is especially important for evaluation of the balance between the costs and benefits involved. To enable comparison with other health-care facilities, benefits are defined in terms of a combination of life-years gained and quality of life. The number of life-years gained can be calculated by comparing the survival expected with and without transplantation. Survival with transplantation is estimated on the basis of observed survival, acknowledging that the probability of survival may have changed over time, owing to changes in therapy and selection criteria. To estimate survival without transplantation, several techniques are available. Prognostic models, correcting for stage of disease, are often used. Pitfalls in the use of these models are discussed. The number of life-years gained can be corrected for quality of life by weighing survival with and without transplantation with an index representing quality of life. A method for the calculation of such an index is given. Finally, some cost estimates are presented and the results are discussed.

## P1ebd0d6a1783

- Year: 2021
- Linked people: Piyameth Dilokthornsakul
- Title: Budget Impact of Sequential Treatment with Biologics, Biosimilars, and Targeted Synthetic Disease-Modifying Antirheumatic Drugs in Thai Patients with Rheumatoid Arthritis

Abstract:

Background Targeted treatment of rheumatoid arthritis (RA) includes biological DMARDs (bDMARDs) and JAK inhibitors (JAKi). These agents are recommended at the same level on the basis of their efficacy and safety data. However, no local evidence of the impact of RA treatment regimens on total budget spending is available to date. This study aimed to explore the budget impact of different sequential targeted treatments in Thai patients with RA who failed at least three conventional synthetic DMARDs. Methods We used the adapted model to evaluate the budget impact of adding tofacitinib in different order to RA targeted treatment regimens. The Thai RA population eligible for treatment was assessed on the basis of local prevalence and experts' opinion. Cost-impact analysis was evaluated for the treatment sequences of four different lines of targeted therapies using inputs like clinical efficacy, safety, and costs. The model used a decision tree structure with treatment nodes corresponding to treatment response outcomes for a cohort of patients. The comparisons included five bDMARDs [etanercept (ETN), infliximab (IFX), golimumab (GOL), rituximab (RTX), tocilizumab (TCZ) intravenous formulation], two JAKi [tofacitinib (TOF) and baricitinib (BAR)], and two IFX biosimilars (PF-06438179/GP1111 and CT-P13). A total of 80 treatment sequences within each containing four sequential first-, second-, third-, and fourth-line options were generated. Results The findings of the base case scenario indicated the treatment sequence with RTX as first-line, followed by IFX biosimilar (PF-06438179/GP1111), TOF, and TCZ, respectively, produced the lowest budget impact of US $693.54 million. Sensitivity analyses confirmed the robustness of our findings. Conclusion The order of targeted therapy starting with RTX, then IFX biosimilar, TOF, and finally TCZ incurred the lowest budget impact over a 5-year time horizon for treating moderate to severe RA. Our findings may help payers and policy makers consider appropriate budget allocation on chronic non-communicable diseases, especially RA.

## Pafe86f287f9e

- Year: 2025
- Linked people: Piyameth Dilokthornsakul
- Title: Impact of gout flare on health-related quality of life: a multi-center cross-sectional study in Thailand

Abstract:

Although the 5-level EQ-5D version (EQ-5D-5L) instrument has been used to determine health-related quality of life and health utility in gout, it is used in comparing health utility among gout flare (GF) and non-gout flare (non-GF) patients is still limited. This study aimed to compare health utility among GF and non-GF patients in Thailand. In this multi-center cross-sectional study, patients with GF and non-GF were interviewed for the EQ-5D5L and EQ-Visual Analog Scale (VAS) instruments by rheumatologists or trained research staffs. Patients with GF were subdivided into 2 subgroups (those who received no treatment and those who received treatment less than 48 h after GF episode). Two hundred and sixteen patients (108 GF and 108 non-GF patients), males in 90.28%, were included. The gout disease duration was significantly longer in the non-GF than in the GF groups (median, 10 vs 5 years; p = 0.004). There was no difference in the tophi present between the two groups. When compared with the non-GF group, the GF patients significantly had low health utility (0.34 ± 0.36 vs. 0.89 ± 0.15, p < 0.001) and EQ-VAS score (54.73 ± 25.14 vs. 84.06 ± 13.38, p < 0.001). In the subgroup analysis of the non-GF group, there was insignificant health utility and EQ-VAS score between those with tophi and those without tophi (0.87 ± 0.14 vs. 0.90 ± 0.15, p = 0.124 and 83.36 ± 14.92 vs. 84.33 ± 12.83, p = 0.938, respectively). This study found that GF clearly had a substantial impact on patients' quality of life. Targeted interventions in managing GF patients to improve their health outcomes are needed. Key Points • Patients with gout flare had lower health utility than those without gout flare. • The clinical significance of the utility and EQ-VAS was evaluated by the EQ-5D-5L instrument between gout flare and non-gout flare groups in Thai gouty patients. • Regarding the presence of tophi or disease duration, no significant differences in health utility and EQ-VAS were observed in the gout flare or non-gout flare group. • Targeted interventions for management of gout flare are needed to improve the health outcomes of gout flare patients.

## Pbfdb0b0dc9b2

- Year: 2024
- Linked people: Margreet Franken
- Title: Applying a cost-based pricing model for innovative cancer treatments subject to indication expansion: A case study for pembrolizumab and daratumumab

Abstract:

BACKGROUND: Expanding the indication of already approved immuno-oncology drugs presents treatment opportunities for patients but also strains healthcare systems. Cost-based pricing models are discussed as a possibility for cost containment. This study focuses on two drugs, pembrolizumab (Keytruda) and daratumumab (Darzalex), to explore the potential effect of indication broadening on the estimated price when using the cost-based pricing (CBP) model proposed by Uyl-de Groot and Löwenberg (2018). METHODS: The model was used to calculate cumulative yearly prices, cumulative prices per indication, and non-cumulative indication-based prices using inputs such as research and development (R&D) costs, manufacturing costs, eligible patient population, and a profit margin. A deterministic stepwise analysis and scenario analysis were conducted to examine how sensitive the estimated price is to the different input assumptions. RESULTS: The yearly cumulative cost-based prices (CBPs) ranged from €52 to €885 for pembrolizumab per vial and €823 to €31,941 for daratumumab per vial. Prices were higher in initial years or indications due to smaller patient populations, decreased over time or after additional indications. Sensitivity analysis showed that the number of eligible patients had the most significant impact on the estimated price. In the scenario analysis the profit margin contributed most to a higher CBPs for both drugs. Lower estimates resulted from assumed lower R&D costs. DISCUSSION: The estimated CBPs are consistently lower than Dutch list prices for pembrolizumab (€2,861), mainly resulting from larger patient populations in registered indications. However, daratumumab's list prices fall within the range of modeled CBPs depending on the year or indication (€4,766). Both CBPs decrease over time or with additional indications. The number of eligible patients and initial R&D costs have the most significant influence on the CBPs. These findings contribute to the ongoing discussions on pharmaceutical pricing, especially concerning cancer drugs with expanding indications.

## P7fe7cb86ffa4

- Year: 2025
- Linked people: Nyantara Wickramasekera
- Title: OP23 Developing A Personalized Decision Aid Incorporating A Discrete Choice Experiment: A Case Study In Ulcerative Colitis

Abstract:

Introduction Choosing the optimal ulcerative colitis treatment is complex, given the range of medical and surgical options with varying side effects and effectiveness. Decision aids can improve patient choices, but current tools lack personalization. To address this, we developed a personalized decision tool using a discrete choice experiment (DCE) to help patients make informed decisions about medical or surgical treatments. Methods An online DCE survey was developed containing competing treatment profiles described using all important aspects of the treatment (effectiveness, side effects, family planning). Patients (n=300) with ulcerative colitis were asked to consider the benefits and disadvantages of each treatment profile and select the treatment that they would choose. The DCE data were analyzed using mixed logit and latent class models. The model results were integrated into an online decision aid using a Shiny application. Results R Shiny was successfully used to enable the real-time personalization of DCE results. The developed decision aid contained two aspects of personalization. First, attribute importance scores showed the treatment characteristics that mattered most to patients based on their DCE choices. Second, a “best-match” treatment that aligned with their preferences was provided from uptake rate calculations. User testing of the developed decision aid is ongoing. However, initial feedback from patients has been positive. Conclusions A key challenge in developing personalized decision aids is providing real-time, tailored recommendations based on individual preferences. This study demonstrated the feasibility of integrating DCE methods into personalized decision aids for ulcerative colitis. By tailoring treatment recommendations to individual patient preferences, this tool has the potential to empower patients, reduce decisional conflict, and enhance shared decision-making between patients and clinicians.

## P269beaa55182

- Year: 2019
- Linked people: Fredrick Purba
- Title: Sociodemographic determinants of self-reporting mental health problems in Indonesian urban population

Abstract:

Studies have found that mental health problems are more prevalent in urban areas compared to rural ones, including in Indonesia. About 6% of Indonesian people report having mental health problems, and 1.7 out of every thousand residents are diagnosed with a psychiatric problem. This study examines the sociodemographic determinants of reporting mental health problems among Indonesia’s general population living in urban areas. One thousand forty participants aged 17 years and over answered sociodemographic questions (i.e., residence, gender, age, education level, income, marital status) and completed the EQ-5D-5L. Their responses to the Anxiety/Depression item of the EQ-5D-5L (no problem vs. any level of problem) were the dependent variable sociodemographic factors were the explanatory variables. About one-third (35.37%) of the participants reported experiencing problems with anxiety/depression. Logistic regression found that marital status was significantly associated with reporting any problems of anxiety/depression in the EQ-5D-5L: single/divorced participants were 58% more likely to report that they suffered from anxiety/depression in comparison to their married counterparts. These results highlight the importance of social support; that is, having a spouse or extended family member whom one can count on for help when facing a problem is essential, regardless of one’s gender, age, educational level, or income.

## P5659f0d1c6ef

- Year: 2023
- Linked people: Piyameth Dilokthornsakul
- Title: Risk prediction algorithms in guiding antiviral therapy initiation among patients with chronic hepatitis B in Thailand: an economic evaluation and budget impact analysis

Abstract:

OBJECTIVE: Several risk prediction algorithms have been developed to guide antiviral therapy initiation among patients with chronic hepatitis B (CHB). This study assessed the cost-effectiveness and budget impact of three risk prediction algorithms among patients with CHB in Thailand. METHODS: A decision tree with a Markov model was constructed. Three risk prediction algorithms were compared with current practices including HePAA, TREAT-B and REACH-B. PubMed was searched from its inception to December 2022 to identify inputs. Tenofovir alafenamide and best supportive care were selected for antiviral-eligible patients, and incremental cost-effectiveness ratios per quality-adjusted life year (QALY) were calculated. RESULTS: Our base case analysis showed that HePAA and REACH-B could provide better QALY (0.098 for HePAA and 0.921 for REACH-B) with decreased total healthcare costs (-10909 THB for HePAA and -8,637 THB for REACH-B). TREAT-B provided worse QALY (-0.144) with increased total healthcare costs (10,435 THB). The budget impacts for HePAA and REACH-B were 387 million THB and 3,653 million THB, respectively. CONCLUSION: HePAA and REACH-B algorithms are cost-effective in guiding antiviral therapy initiation. REACH-B is the most cost-effective option, but has a high budget impact. Policymakers should consider both cost-effectiveness and budget impact findings when deciding which algorithm should be implemented.

## Pc811e48f0b5c

- Year: 2014
- Linked people: Ciaran O'Neill
- Title: Reasons for participation and non-participation in a diabetes prevention trial among women with prior gestational diabetes mellitus (GDM)

Abstract:

BACKGROUND: Gestational diabetes mellitus (GDM) is a risk factor for the development of type 2 diabetes. Lifestyle intervention can prevent progression to type 2 diabetes in high risk populations. We designed a randomised controlled trial (RCT) to evaluate the effectiveness of an established lifestyle intervention compared to standard care for delaying diabetes onset in European women with recent GDM. Recruitment into the RCT was more challenging than anticipated with only 89 of 410 (22%) women agreeing to participate. This paper identifies factors that could enhance participation of the target population in future interventions. METHODS: We hypothesised that women who agreed to participate would have higher diabetes risk profiles than those who declined, and secondly that it would be possible to predict participation on the bases of those risk factors. To test our hypothesis, we identified the subset of women for whom we had comprehensive data on diabetes risks factors 3-5 years following GDM, reducing the sample to 43 participants and 73 decliners. We considered established diabetes risk factors: smoking, daily fruit and vegetable intake, participation in exercise, family history of diabetes, glucose values and BMI scores on post-partum re-screens, use of insulin during pregnancy, and age at delivery. We also analysed narrative data from 156 decliners to further understand barriers to and facilitators of participation. RESULTS: Two factors differentiated participants and decliners: age at delivery (with women older than 34 years being more likely to participate) and insulin use during pregnancy (with women requiring the use of insulin in pregnancy less likely to participate). Binary logistic regression confirmed that insulin use negatively affected the odds of participation. The most significant barriers to participation included the accessibility, affordability and practicality of the intervention. CONCLUSIONS: Women with recent GDM face multiple barriers to lifestyle change. Intervention designers should consider: (i) the practicalities of participation for this population, (ii) research designs that capitalise on motivational differences between participants, (iii) alleviating concerns about long-term diabetes management. We hope this work will support future researchers in developing interventions that are more relevant, effective and successful in recruiting the desired population. TRIAL REGISTRATION: Current Controlled Trials ISRCTN41202110.

## Pcba4c36af786

- Year: 1992
- Linked people: Gerard De Pouvourville
- Title: Issues in the cross-national assessment of health technology

Abstract:

With the growing international literature in economic evaluation and the rapid spread of new health technologies, there is a need to undertake, or at least interpret, economic evaluations on the international level. However, the ways in which cross-national differences affect the cost-effectiveness of health technologies or their evaluations have never been studied. This paper explores these issues by taking advantage of a unique situation in which the same economic evaluation of a new indication for a health technology was conducted simultaneously in four countries using an identical methodology. The study showed that if prior agreement on methods can be reached and local data applied, economic evaluations can be undertaken in a way that facilitates the extrapolation of results from country to country.

## P9562cbd1e70a

- Year: 2020
- Linked people: Elly Stolk
- Title: International Valuation Protocol for the EQ-5D-Y-3L

Abstract:

The EQ-5D-Y-3L is a generic, health-related, quality-of-life instrument for use in younger populations. Some methodological studies have explored the valuation of children's EQ-5D-Y-3L health states. There are currently no published value sets available for the EQ-5D-Y-3L that are appropriate for use in a cost-utility analysis. The aim of this article was to describe the development of the valuation protocol for the EQ-5D-Y-3L instrument. There were several research questions that needed to be answered to develop a valuation protocol for EQ-5D-Y-3L health states. Most important of these were: (1) Do we need to obtain separate values for the EQ-5D-Y-3L, or can we use the ones from the EQ-5D-3L? (2) Whose values should we elicit: children or adults? (3) Which valuation methods should be used to obtain values for child's health states that are anchored in Full health = 1 and Dead = 0? The EuroQol Research Foundation has pursued a research programme to provide insight into these questions. In this article, we summarized the results of the research programme concluding with the description of the features of the EQ-5D-Y-3L valuation protocol. The tasks included in the protocol for valuing EQ-5D-Y-3L health states are discrete choice experiments for obtaining the relative importance of dimensions/levels and composite time-trade-off for anchoring the discrete choice experiment values on 1 = Full Health and 0 = Dead. This protocol is now available for use by research teams to generate EQ-5D-Y-3L value sets for their countries allowing the implementation of a cost-utility analysis for younger populations.

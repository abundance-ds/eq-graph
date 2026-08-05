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

## P458a78612ea9

- Year: 2021
- Linked people: Márta Péntek
- Title: Outcomes of Digital Biomarker-Based Interventions: Protocol for a Systematic Review of Systematic Reviews.

Abstract:

BACKGROUND: Digital biomarkers are defined as objective, quantifiable, physiological, and behavioral data that are collected and measured using digital devices such as portables, wearables, implantables, or digestibles. For their widespread adoption in publicly financed health care systems, it is important to understand how their benefits translate into improved patient outcomes, which is essential for demonstrating their value. OBJECTIVE: The paper presents the protocol for a systematic review that aims to assess the quality and strength of the evidence reported in systematic reviews regarding the impact of digital biomarkers on clinical outcomes compared to interventions without digital biomarkers. METHODS: A comprehensive search for reviews from 2019 to 2020 will be conducted in PubMed and the Cochrane Library using keywords related to digital biomarkers and a filter for systematic reviews. Original full-text English publications of systematic reviews comparing clinical outcomes of interventions with and without digital biomarkers via meta-analysis will be included. The AMSTAR-2 tool will be used to assess the methodological quality of these reviews. To assess the quality of evidence, we will evaluate the systematic reviews using the Grading of Recommendations, Assessment, Development and Evaluation (GRADE) tool. To detect the possible presence of reporting bias, we will determine whether a protocol was published prior to the start of the studies. A qualitative summary of the results by digital biomarker technology and outcomes will be provided. RESULTS: This protocol was submitted before data collection. Search, screening, and data extraction will commence in December 2021 in accordance with the published protocol. CONCLUSIONS: Our study will provide a comprehensive summary of the highest level of evidence available on digital biomarker interventions, providing practical guidance for health care providers. Our results will help identify clinical areas in which the use of digital biomarkers has led to favorable clinical outcomes. In addition, our findings will highlight areas of evidence gaps where the clinical benefits of digital biomarkers have not yet been demonstrated. INTERNATIONAL REGISTERED REPORT IDENTIFIER (IRRID): PRR1-10.2196/28204.

## Pfd062eea3822

- Year: 2023
- Linked people: Annette Regan
- Title: Association of arsenic exposure with measles antibody titers in US children: Influence of sex and serum folate levels

Abstract:

Exposure to arsenic during childhood is associated with various adverse health conditions. However, little is known about the effect of arsenic exposure on vaccine-related humoral immunity in children. We analyzed data from the National Health and Nutrition Examination Survey (2003-2004 and 2009-2010) to study the relationship between urinary arsenic and measles antibody levels in 476 US children aged 6-11. Multivariable linear regression was used to evaluate the association, adjusting for cycle, age, race, body mass index (BMI), serum cotinine, poverty index ratio, and vitamin B12 and selenium intakes. Stratified analyses were conducted by sex and serum folate levels using the median as cutoff (18.7 ng/mL). The measles antibody concentrations in the 3rd and 4th quartiles were found to have significantly decreased by 28.5 % (95 % Confidence Interval (CI) -47.6, -2.28) and 36.8 % (95 % CI -50.2, -19.5), compared to the lowest quartile among boys with serum folate levels lower than 18.7 ng/ml. The serum measles antibody titers significantly decreased by 16.7 % (95 %CI -25.0, -7.61) for each doubling of creatinine-corrected urinary total inorganic arsenic concentrations in the same group. No associations were found in boys with high serum folate levels or in girls. Further prospective studies are needed to validate these findings and develop interventions to protect children from infectious diseases.

## P76f437ec5a22

- Year: 2022
- Linked people: Fanni Rencz
- Title: Immunohistochemical Study of the PD-1/PD-L1 Pathway in Cutaneous Lupus Erythematosus

Abstract:

The pathomechanism of various autoimmune diseases is known to be associated with the altered function of programmed cell death 1/programmed cell death ligand 1 (PD-1/PD-L1) axis. We aimed to investigate the role of this pathway and inflammatory cell markers in subtypes of cutaneous lupus erythematosus (CLE): discoid lupus erythematosus (DLE), subacute CLE (SCLE) and toxic epidermal necrolysis (TEN)-like lupus, a hyperacute form of acute CLE (ACLE). Ten skin biopsy samples from 9 patients were analyzed with immunohistochemistry regarding the following markers: CD3, CD4, CD8, Granzyme B, CD123, CD163, PD-1, PD-L1. Our group consisted of 4 SCLE (2 idiopathic (I-SCLE) and 2 PD-1 inhibitor-induced (DI-SCLE)), 4 DLE and 1 TEN-like lupus cases. From the latter patient two consecutive biopsies were obtained 1 week apart. Marker expression patterns were compared through descriptive analysis. Higher median keratinocyte (KC) PD-L1 expression was observed in the SCLE group compared to the DLE group (65% and 5%, respectively). Medians of dermal CD4, Granzyme B (GB), PD-1 positive cell numbers and GB+/CD8 + ratio were higher in the DLE group than in the SCLE group. The I-SCLE and DI-SCLE cases showed many similarities, however KC PD-L1 expression and dermal GB positive cell number was higher in the former. The consecutive samples of the TEN-like lupus patient showed an increase by time within the number of infiltrating GB+ cytotoxic T-cells and KC PD-L1 expression (from 22 to 43 and 30%–70%, respectively). Alterations of the PD-1/PD-L1 axis seems to play a role in the pathogenesis of CLE.

## P7dd9603872c5

- Year: 2025
- Linked people: Erica Lubetkin
- Title: Health-Related Quality of Life for Persons Treated or Monitored for Anal High-Grade Squamous Intraepithelial Lesions (AMC-A01)

Abstract:

PURPOSE The Anal Cancer/High-grade squamous intraepithelial lesions Outcomes Research (ANCHOR) trial demonstrated that treating precancerous anal HSIL reduces the incidence of anal cancer by 57% in people with HIV. It remains unclear how HSIL treatment or monitoring without treatment affects patient-reported health-related quality of life (HRQoL). We evaluated differences in HRQoL for individuals who were randomly assigned to active monitoring (AM) or treatment for anal HSIL. METHODS Using an index designed and validated for use in ANCHOR, HRQoL was assessed before random assignment (T1), 2-7 days (+3 days) after random assignment/treatment (T2), and 28 days (±7 days) after random assignment/treatment (T3). RESULTS ANCHOR participants living with HIV (N = 124; mean [standard deviation, SD] age, 52.6 years [10.3]; n = 101 [81.5%] men; n = 65 [52.4%] White; n = 95 [76.6%] non-Hispanic; treatment n = 70 [56.4%]; and AM n = 54 [43.6%]) were included. Treatment arm participants had significant mean worsening from T1-T2 in physical symptoms (mean [SD] difference, 0.31 [0.51]; P = .0001) and impact on psychological functioning (mean [SD] difference, 0.25 [0.64]; P = .022) that significantly improved to T1 levels from T2-T3 (ie, mean [SD] difference, –0.25 [0.52]; P = .003; and mean [SD] difference, –0.07 [0.23]; P = .039, respectively). AM arm participants experienced significant mean improvement in impact on psychological functioning from T1-T3 (mean [SD], difference, –0.20 [0.50]; P = .017). After adjusting for T1, treatment arm participants had a larger mean improvement than AM arm participants in physical symptoms from T2-T3 (mean [SD] difference, –0.25 [0.52]; P = .024); no between-arm differences were observed for impact on physical or psychological functioning. CONCLUSION Treatment arm participants experienced significant worsening in physical symptoms and impact on psychological functioning from T1-T2 but returned to prerandomization levels by T3, indicating that any immediate anal HSIL treatment-related impacts to HRQoL are temporary. Further research is needed to determine long-term impacts of anal HSIL treatment on HRQoL.

## P389b718badbc

- Year: 2025
- Linked people: Abdelghafour MARFAK
- Title: External generalizability and internal accuracy of predictive models for perinatal mortality: a systematic review and meta-analysis

Abstract:

Objective To systematically review and meta-analyze predictive models for perinatal mortality, including stillbirths from 28 weeks gestation and early neonatal deaths within six days, focusing on calibration and discrimination metrics. Methods We conducted a comprehensive search across databases like PubMed and Scopus from inception to April 1, 2025, targeting observational studies that developed or validated predictive models for perinatal mortality reporting at least one discrimination metric, such as the Area Under the Curve (AUC) or C-statistic. Two reviewers independently screened studies and assessed bias using the PROBAST tool. Meta-analyses were performed utilizing a random-effects model with heterogeneity assessed via the I 2 statistic. Results Sixteen studies were included, representing 8 553 805 neonates. Eight studies focused on stillbirths, five on early neonatal deaths, and three on both. Pooled AUC estimates ranged from 0.78 to 0.86, with higher discrimination in internally validated models. Calibration was reported in 11 studies, but varied in quality, with one study rated high risk of bias. Conclusion This meta-analysis is the first to synthesize predictive models specific to stillbirths and early neonatal mortality. While internal performance metrics are promising, significant shortfalls in external validation and generalizability remain. Standardized methodologies and thorough external validations are crucial for reliable perinatal risk prediction. PROSPERO registration number CRD42025638383

## P66d351fee2bd

- Year: 2025
- Linked people: Oriana Ciani
- Title: A Strategic Roadmap to Support Communication on and Acceptance of Surrogate Endpoints: The REnal Surrogacy accEpTance in Chronic Kidney Disease (RESET CKD) Collaboration.

Abstract:

INTRODUCTION: Developing effective treatments in chronic, progressive diseases like chronic kidney disease (CKD) is challenging because patients may only experience relevant outcomes such as kidney failure after long periods of disease progression. Surrogate endpoints provide a valuable alternative to definitive final patient-relevant outcomes, which may accelerate clinical development processes. However, optimal utilization of surrogate endpoints for reimbursement decisions requires alignment across multiple stakeholders, including health technology assessment (HTA) bodies and reimbursement agencies, who are generally more cautious than regulatory bodies in their acceptance of surrogate endpoint evidence. The aim of this paper is to propose a strategic roadmap to facilitate cross-stakeholder collaboration and support the consideration of surrogate endpoints in regulatory and reimbursement decisions. METHODS: An international group of experts in surrogate endpoints, reimbursement decisions, and kidney disease formed The REnal Surrogacy accEpTance in Chronic Kidney Disease (RESET CKD) Collaboration. This scientific steering committee held several meetings to develop a roadmap of activities with the aim of enabling the appropriate consideration of surrogate endpoints through structured multi-stakeholder engagement involving regulators, clinicians, HTA bodies, payers, industry, and patients. RESULTS: The strategic roadmap focuses on four areas: identifying the need for evidence; engaging stakeholders; collaborating in regulatory and reimbursement processes; and disseminating evidence. The RESET CKD collaboration is currently implementing the roadmap in the field of CKD through collating relevant evidence for a CKD-relevant surrogate endpoint in a scientific playbook, conducting economic evaluations, developing a position paper, and engaging patient groups. CONCLUSIONS: Disparities between regulatory and reimbursement processes and decisions underscore the need for a structured approach to enhancing transparency, consistency, and timeliness in the use of surrogate endpoint evidence in healthcare decision-making. The roadmap developed through the RESET CKD Collaboration addresses this need and is already demonstrating practical value in its implementation. Although initially focused on CKD, the framework is designed to be transferable to other therapeutic areas. Key challenges remain, including the integration of surrogate endpoints into adaptive pricing models and performance-based agreements.

## Pa2330e89e7dc

- Year: 2023
- Linked people: Simon Pickard
- Title: A qualitative assessment of key considerations for drug checking service implementation

Abstract:

BACKGROUND: With many drug-related deaths driven by potent synthetic opioids tainting the illicit drug supply, drug checking services are becoming a key harm reduction strategy. Many drug checking technologies are available, ranging from fentanyl test strips to mass spectrometry. This study aimed to identify key considerations when implementing drug checking technologies and services to support harm reduction initiatives. METHODS: Key informant interviews were conducted with harm reduction stakeholders throughout Illinois. Participants included members of existing drug checking services and recovery centers. Interviews were recorded, transcribed, and coded by two researchers using the framework method. Findings were contextualized according to micro (client)-, meso (organization)-, and macro (policy)-level themes. RESULTS: Seven interviews were conducted with ten participants. Fourier transform infrared spectroscopy was consistently identified as a technology of choice given its accuracy, range of substance detection, portability, and usability. Recommendations included the use of confirmatory testing, which can help address the limitations of technologies and provide a mechanism to train technicians. Locations of drug checking services should maximize public health outreach and leverage existing harm reduction agencies and staff with lived experience, who are critical to developing trust and rapport with clients. Criminalization and loss of privacy were major concerns for clients using drug checking services. Additional issues included the need to raise awareness of the legitimacy of services through public support from governing bodies, and funding to ensure the sustainability of drug checking services. CONCLUSIONS: This research facilitated the identification of issues and recommendations from stakeholders around key considerations for the adoption of drug checking technologies, which not only included the cost and technical specifications of instrumentation, but also broader issues such as accessibility, privacy, and well-trained personnel trusted by clients of the service. Successful implementation of drug checking services requires knowledge of local needs and capacity and an in-depth understanding of the target population.

## P278ebdbd9b85

- Year: 2022
- Linked people: Henry Bailey
- Title: Evaluating Health Inequality in Five Caribbean Basin Countries Using EQ-5D-5L.

Abstract:

BACKGROUND: EQ-5D-5L is a standardized health outcomes instrument that can be added to national surveys to measure inequality in health outcomes. The aim of this study was to produce baseline values of health inequality using EQ-5D-5L for five countries in the Caribbean Basin region based on national surveys in 2012-2014. METHODS: The EQ-5D-5L questionnaire was included in adult population surveys of Barbados, Belize, Colombia, Jamaica and Trinidad and Tobago. EQ-5D-5L measures were calculated for demographic groups using stratifiers from the World Health Organization's PROGRESS-Plus framework, and generalized linear models were used to test for association between EQ-5D-5L and the PROGRESS-Plus variables. Ordered logit models were used to obtain odds ratios for the effect of the PROGRESS-Plus variables on reporting problems on the EQ-5D-5L dimensions. The Kakwani index was calculated for each country. RESULTS: Data were obtained for representative samples in each country, giving a combined total of 11,284 respondents. Different patterns of inequality were observed among the five countries. The biggest drivers of inequality were age and gender, and the biggest EQ-5D factors were self-care in Belize and pain/discomfort in the other four countries. CONCLUSION: This study demonstrated that the EQ-5D-5L instrument can easily be added to national surveys. Inequality measures from this study can be used as baseline values for comparisons with future similar surveys in these five countries to infer changes in health inequality as measured by EQ-5D outcomes. These can be used to track the performance of policy initiatives aimed at specific demographic groups.

## P2bedf2477c52

- Year: 2022
- Linked people: Ciaran O'Neill
- Title: Hospital Costs and Fatality Rates of Traumatic Assaults by Mechanism in the US, 2016-2018

Abstract:

Importance: Estimates of the total economic cost of firearm violence are important in drawing attention to this public health issue; however, studies that consider violence more broadly are needed to further the understanding of the extent to which such costs can be avoided. Objectives: To estimate the association of firearm assaults with US hospital costs and deaths compared with other assault types. Design, Setting, and Participants: The 2016-2018 US Nationwide Emergency Department Sample and National Inpatient Sample, Healthcare Cost and Utilization Project were used in this cross-sectional study of emergency department (ED) and inpatient admissions for assaults involving a firearm, sharp object, blunt object, or bodily force identified using International Statistical Classification of Diseases, Tenth Revision, Clinical Modification codes. Differences in ED and inpatient costs (2020 US dollars) across mechanisms were estimated using ordinary least-squares regression with and without adjustments for year and hospital, patient, and injury characteristics. The Centers for Disease Control and Prevention underlying cause of death data were used to estimate national death rates and hospital case-fatality rates across mechanisms. Cost analysis used a weighted sample. National death rates and hospital case-fatality rates used US resident death certificates, covering 976 million person-years. Hospital case-fatality rates also used nationally weighted ED records covering 2.7 million admissions. Data analysis was conducted from March 1, 2021, to March 31, 2022. Exposure: The primary exposure was the mechanism used in the assault. Main Outcomes and Measures: Emergency department and inpatient costs per record. National death rates and hospital case-fatality rates. Results: Overall, 2.4 million ED visits and 184 040 inpatient admissions for assault were included. Across all mechanisms, the mean age of the population was 32.7 (95% CI, 32.6-32.9) years in the ED and 36.4 (95% CI, 36.2-36.7) years in the inpatient setting; 41.9% (95% CI, 41.2%-42.5%) were female in the ED, and 19.1% (95% CI, 18.6%-19.6%) of inpatients were female. Most assaults recorded in the ED involved publicly insured or uninsured patients and hospitals in the Southern US. Emergency department costs were $678 (95% CI, $657-$699) for bodily force, $861 (95% CI, $813-$910) for blunt object, $996 (95% CI, $925-$1067) for sharp object, and $1388 (95% CI, $1254-$1522) for firearm assaults. Corresponding inpatient costs were $14 702 (95% CI, $14 178-$15 227) for bodily force, $17 906 (95% CI, $16 888-$18 923) for blunt object, $19 265 (95% CI, $18 475-$20 055) for sharp object, and $34 949 (95% CI, $33 654-$36 244) for firearm assaults. National death rates per 100 000 were 0.04 (95% CI, 0.03-0.04) for bodily force, 0.03 (95% CI, 0.03-0.03) for blunt object, 0.54 (95% CI, 0.52-0.55) for sharp object, and 4.40 (95% CI, 4.36-4.44) for firearm assaults. Hospital case fatality rates were 0.01% (95% CI, 0.009%-0.012%) for bodily force, 0.05% (95% CI, 0.04%-0.06%) for blunt object, 1.05% (95% CI, 1.00%-1.09%) for sharp object, and 15.26% (95% CI, 15.04%-15.49%) for firearm assaults. In regression analysis, ED costs for firearm assaults were 59% to 99% higher than costs for nonfirearm assaults, and inpatient costs were 67% to 118% higher. Conclusions and Relevance: The findings of this study suggest that it may be useful for policies aimed at reducing the costs of firearm violence to consider violence more broadly to understand the extent to which costs can be avoided.

## Pcb33275303c9

- Year: 2023
- Linked people: Jan Busschbach
- Title: The Effect of Tailored Short Message Service (SMS) on Physical Activity: Results from a Three-Component Randomized Controlled Lifestyle Intervention in Women with PCOS

Abstract:

This analysis of secondary outcome measures of a randomized controlled trial was conducted to study the effect of a one-year three-component (cognitive behavioural therapy, diet, exercise) lifestyle intervention (LSI), with or without additional Short Message Service (SMS) support, on physical activity and aerobic capacity in overweight or obese women with polycystic ovary syndrome (PCOS). Women diagnosed with PCOS and a BMI &gt; 25 kg/m2 were randomly assigned to LSI with SMS support (SMS+, n = 60), LSI without SMS support (SMS−, n = 63) or care as usual (CAU, n = 60) in order to lose weight. Based on results from the International Physical Activity Questionnaire (IPAQ), we found a significant within-group increase after one year for SMS+ in the high physical activity category (+31%, p &lt; 0.01) and sitting behaviour decreased (Δ −871 min/week, p &lt; 0.01). Moreover, the peak cycle ergometer workload increased within SMS+ (Δ +10 watts, p &lt; 0.01). The SMS+ group also demonstrated a significantly different increase in walking metabolic equivalent of task minutes (METmin)/week compared with CAU after one year (Δ 1106 METmin/week, p &lt; 0.05). Apart from this increase in walking activity, no other between-group differences were found in this trial. Overall, based on within-group results, SMS support seemed to help with improving physical activity and aerobic capacity and decreasing sedentary behaviour.

## P768b84afb833

- Year: 2023
- Linked people: Deborah Marshall
- Title: Persuasive Messages for Improving Adherence to COVID-19 Prevention Behaviors: Randomized Online Experiment.

Abstract:

BACKGROUND: Adherence to nonpharmaceutical interventions for COVID-19, including physical distancing, masking, staying home while sick, and avoiding crowded indoor spaces, remains critical for limiting the spread of COVID-19. OBJECTIVE: The aim of this study was to test the effectiveness of using various persuasive appeals (deontological moral frame, empathy, identifiable victim, goal proximity, and reciprocity) at improving intentions to adhere to prevention behaviors. METHODS: A randomized online experiment using a representative sample of adult Canadian residents with respect to age, ethnicity, and province of residence was performed from March 3 to March 6, 2021. Participants indicated their intentions to follow public health guidelines, saw one of six flyers featuring a persuasive appeal or no appeal, and then rated their intentions a second time. Known correlates of attitudes toward public health measures were also measured. RESULTS: Intentions to adhere to public health measures increased in all appeal conditions. The message featuring an empathy appeal resulted in a greater increase in intentions than the control (no appeal) message. Moreover, the effectiveness of persuasive appeals was moderated by baseline intentions. Deontological, empathy, identifiable victim, and reciprocity appeals improved intentions more than the control message, but only for people with lower baseline intentions to adhere to nonpharmaceutical interventions. CONCLUSIONS: Public health marketing campaigns aiming to increase adherence to COVID-19 protective behaviors could achieve modest gains by employing a range of persuasive appeals. However, to maximize impact, it is important that these campaigns be targeted to the right individuals. TRIAL REGISTRATION: ClinicalTrials.gov NCT05722106; https://clinicaltrials.gov/ct2/show/NCT05722106.

## Pf29fba37de4f

- Year: 2022
- Linked people: Nick Bansback
- Title: Adoption des médicaments biosimilaires au Canada : analyse des politiques provinciales et données sur leur utilisation

Abstract:

[Voir la version anglaise de l’article ici : www.cmaj.ca/lookup/doi/10.1503/cmaj.211478][1] Points clés Les agents biologiques représentent un segment important des dépenses en médicaments au Canada : alors qu’ils ne constituaient que 1,5 % du volume des ordonnances, les agents biologiques

## P87a0b8d01ebc

- Year: 2022
- Linked people: Eleanor Pullenayegum
- Title: Applying the Clinician-reported Genetic testing Utility InDEx (C-GUIDE) to genome sequencing: further evidence of validity

Abstract:

Genome sequencing (GS) outperforms other rare disease diagnostics, but standardized approaches to assessing its clinical utility are limited. This study assessed the validity of the Clinician-reported Genetic testing Utility InDEx (C-GUIDE), a novel tool for assessing the utility of genetic testing from a clinician's perspective, for GS. C-GUIDE ratings were completed for patients who received GS results. For each patient, total C-GUIDE and single item global scores were calculated. Construct validity was assessed using linear regression to determine the association between C-GUIDE total and global item scores and measure the effects of potential explanatory variables. Ratings were completed for 67 pediatric and 36 adult patients. GS indications were neurological for 70.9% and results were diagnostic for 28.2%. When the C-GUIDE assessed primary (PV), secondary (SV), and pharmacogenomic (PGx) variants, on average, a one unit increase in the global item score was associated with an increase of 7.3 in the C-GUIDE score (p < 0.05). Diagnostic results were associated with an increase in C-GUIDE score of 5.0 compared to non-diagnostic results (p < 0.05) and an increase of one SV was associated with an increase of 2.5 (p < 0.05). For children, decreased age of one year was associated with an increase in C-GUIDE score of 0.3 (p < 0.05). Findings provide evidence that C-GUIDE measures the construct of clinical utility in pediatric and adult rare disease populations and is sensitive to changes in utility related to variant type. Quantifying the clinical utility of GS using C-GUIDE can inform efforts to optimize its use in patient care.

## P6f7cf057e867

- Year: 2022
- Linked people: Arjun Bhadhuri
- Title: Cost-effectiveness of a structured medication review approach for multimorbid older adults: Within-trial analysis of the OPERAM study

Abstract:

BACKGROUND: Inappropriate polypharmacy has been linked with adverse outcomes in older, multimorbid adults. OPERAM is a European cluster-randomized trial aimed at testing the effect of a structured pharmacotherapy optimization intervention on preventable drug-related hospital admissions in multimorbid adults with polypharmacy aged 70 years or older. Clinical results of the trial showed a pattern of reduced drug-related hospital admissions, but without statistical significance. In this study we assessed the cost-effectiveness of the pharmacotherapy optimisation intervention. METHODS: We performed a pre-planned within-trial cost-effectiveness analysis (CEA) of the OPERAM intervention, from a healthcare system perspective. All data were collected within the trial apart from unit costs. QALYs were computed by applying the crosswalk German valuation algorithm to EQ-5D-5L-based quality of life data. Considering the clustered structure of the data and between-country heterogeneity, we applied Generalized Structural Equation Models (GSEMs) on a multiple imputed sample to estimate costs and QALYs. We also performed analyses by country and subgroup analyses by patient and morbidity characteristics. RESULTS: Trial-wide, the intervention was numerically dominant, with a potential cost-saving of CHF 3'588 (95% confidence interval (CI): -7'716; 540) and gain of 0.025 QALYs (CI: -0.002; 0.052) per patient. Robustness analyses confirmed the validity of the GSEM model. Subgroup analyses suggested stronger effects in people at higher risk. CONCLUSION: We observed a pattern towards dominance, potentially resulting from an accumulation of multiple small positive intervention effects. Our methodological approaches may inform other CEAs of multi-country, cluster-randomized trials facing presence of missing values and heterogeneity between centres/countries.

## P8b40a6014853

- Year: 2026
- Linked people: Girma Tekle Gebremariam
- Title: Health-related quality of life and associated factors among patients with chronic obstructive pulmonary disease in Addis Ababa, Ethiopia: a multicentre cross-sectional study

Abstract:

OBJECTIVE: This study aimed to assess health-related quality of life (HRQoL) and identify associated factors among patients with chronic obstructive pulmonary disease (COPD) attending selected hospitals in Addis Ababa, Ethiopia. DESIGN AND SETTING: A hospital-based multicentre cross-sectional study was conducted among 205 patients with COPD attending the chest clinics of selected hospitals in Addis Ababa, Ethiopia, from June 2023 to December 2023. PARTICIPANTS: A total of 205 patients with COPD who had follow-up at outpatient departments of the chest clinic of the selected hospitals were included in the study. MAIN OUTCOME MEASURES: The main outcome of this study was HRQoL, which was assessed using the validated COPD Assessment Test-Amharic version (CAT-Am). Data analysis was performed using Stata version.17, and multivariable linear regression was employed to examine the relationship between HRQoL and independent variables. Variables with p-values <0.05 at a 95% CI were considered statistically significant. RESULTS: The mean score of the overall CAT-Am was 20.24±8.13. Older age (β=0.11, 95% CI: 0.04 to 0.17), poor social support (β=2.49, 95% CI: 0.74 to 4.24), biomass fuel exposure (β=4.57, 95% CI:3.17 to 5.97), Global Initiative for Chronic Obstructive Lung Disease (GOLD) stages 2, 3 and 4 (β=2.12, 95% CI: 0.23 to 4.01; β=3.38, 95% CI: 1.11 to 5.66; β=5.20, 95% CI: 2.37 to 8.05, respectively), presence of comorbidity (β=4.03, 95% CI: 2.48 to 5.59), increased number of hospitalisations in the past year (β=2.78, 95% CI: 1.68 to 3.88), increased number of prescribed medications (β=0.40, 95% CI: 0.10 to 0.70), low medication adherence (β=2.79, 95% CI: 1.13 to 4.46), and moderate medication adherence (β=3.38, 95% CI: 1.65 to 5.11) were negatively associated with HRQoL. CONCLUSION AND RECOMMENDATIONS: In this study, patients with COPD had poor HRQoL, which indicates that patients need multidisciplinary interventions. Older age, poor social support, an increased number of prescribed medications, an increased number of hospitalisations in the past year, biomass fuel exposure, low and moderate medication adherence, GOLD severity stages 2, 3 and 4, and the presence of comorbidities require close follow-up to improve HRQoL. Further research should evaluate targeted strategies to address these determinants.

## P855bbe175bf1

- Year: 2024
- Linked people: Andrew Lloyd, Philip Powell
- Title: The Association Between Physical Distancing Behaviors to Avoid COVID-19 and Health-Related Quality of Life in Immunocompromised and Nonimmunocompromised Individuals: Patient-Informed Protocol for the Observational, Cross-Sectional EAGLE Study.

Abstract:

BACKGROUND: Immunocompromised individuals are known to respond inadequately to SARS-CoV-2 vaccines, placing them at high risk of severe or fatal COVID-19. Thus, immunocompromised individuals and their caregivers may still practice varying degrees of social or physical distancing to avoid COVID-19. However, the association between physical distancing to avoid COVID-19 and quality of life has not been comprehensively evaluated in any study. OBJECTIVE: We aim to measure physical distancing behaviors among immunocompromised individuals and the association between those behaviors and person-centric outcomes, including health-related quality of life (HRQoL) measures, health state utilities, anxiety and depression, and work and school productivity impairment. METHODS: A patient-informed protocol was developed to conduct the EAGLE Study, a large cross-sectional, observational study, and this paper describes that protocol. EAGLE is designed to measure distancing behaviors and outcomes in immunocompromised individuals, including children (aged ≥6 mo) and their caregivers, and nonimmunocompromised adults in the United States and United Kingdom who report no receipt of passive immunization against COVID-19. We previously developed a novel self- and observer-reported instrument, the Physical Distancing Scale for COVID-19 Avoidance (PDS-C19), to measure physical distancing behavior levels cross-sectionally and retrospectively. Using an interim or a randomly selected subset of the study population, the PDS-C19 psychometric properties will be assessed, including structural validity, internal consistency, known-group validity, and convergent validity. Associations (correlations) will be assessed between the PDS-C19 and validated HRQoL-related measures and utilities. Structural equation modeling and regression will be used to assess these associations, adjusting for potential confounders. Participant recruitment and data collection took place from December 2022 to June 2023 using direct-to-patient channels, including panels, clinician referral, patient advocacy groups, and social media, with immunocompromising diagnosis confirmation collected and assessed for a randomly selected 25% of immunocompromised participants. The planned total sample size is 3718 participants and participant-caregiver pairs. Results will be reported by immunocompromised status, immunocompromising condition category, country, age group, and other subgroups. RESULTS: All data analyses and reporting were planned to be completed by December 2023. Results are planned to be submitted for publication in peer-reviewed journals in 2024-2025. CONCLUSIONS: This study will quantify immunocompromised individuals' physical distancing behaviors to avoid COVID-19 and their association with HRQoL as well as health state utilities. INTERNATIONAL REGISTERED REPORT IDENTIFIER (IRRID): RR1-10.2196/52643.

## P5635ed4eb93d

- Year: 2025
- Linked people: Richard Norman
- Title: Patient preferences for Remote cochlear implant management: A discrete choice experiment

Abstract:

BACKGROUND: The opportunity to assess cochlear implant outcomes remotely provides the potential to streamline delivery of care for cochlear implant users. However, the conditions required for its implementation into clinic systems must be fully understood to ensure success and sustainability. The objectives of this study were to (i) use a discrete choice experiment quantify the preferences of cochlear implant users when considering use of Cochlear Remote CheckTM, a remote assessment service, and (ii) explore the perceptions, insights and attitudes of CI users that may influence utilisation of a remote service. DESIGN: A discrete choice experiment was administrated to Australian adult cochlear implant users via an online survey. Participants chose between pairs of hypothetical clinical service options for three different clinical scenarios (acute care, troubleshooting and long-term review). Participants answered a series of questions focusing on how and when remote services should be discussed and offered within their hearing journey. RESULTS: A total of 124 adult cochlear implant users completed the survey. Conditional logit analysis revealed the strongest participant preference was clinician continuity for assessment review, followed by low service costs. They preferred to receive assessment results within one week of completion, but not by videoconference/call in the acute care scenario. Only 12% of participants preferred in-clinic visits for all scenarios. Notably, 100% of participants felt that cochlear implant users should be made aware of remote service opportunities available to them. CONCLUSION: Study participants placed high importance on clinician continuity, but preferences for timing and delivery of results were less pronounced. This information can help to inform customisation of remote services by individual clinics. Costs and payment infrastructure for providing remote care require careful consideration. Whilst there is an appetite for use of Remote CheckTM alongside clinic visits, it is not suitable for, nor preferred by, all cochlear implant users.

## Pcadbf90fab6e

- Year: 2025
- Linked people: Bernhard Michalowsky
- Title: Informal care for people with dementia in Europe.

Abstract:

Introduction Informal care estimates for use in health-economic models are lacking. We aimed to estimate the association between informal care time and dementia symptoms across Europe. Methods A secondary analysis was performed on 13,529 observations in 5,369 persons from 9 European pooled cohort or trial studies in community-dwelling persons with dementia. A mixed regression model was fitted to time spent on instrumental or basic activities of daily living using disease severity and demographic characteristics. Results Daily informal care time was 0.5 hours higher in moderate compared to mild and 1.3h higher in severe compared to mild cognitive impairment. Likewise, this was 1.2h and 2.7h for functional disability and 0.3h and 0.6h for behavioral symptoms in the same directions. Discussion Estimates can be used in both single- and multi-domain health-economic models for dementia in European settings.

## Pd036c8e6253f

- Year: 2023
- Linked people: You-Shan Feng
- Title: Definitions of Abnormal Breast Size and Asymmetry: A Cohort Study of 400 Women

Abstract:

Background Macromastia, micromastia and breast asymmetry have an impact on health and quality of life. However, there is scarce information addressing breast size and asymmetry frequency distribution in reference populations. Objective The current study aims to identify factors that influence breast size and symmetry and classifies abnormal breast sizes and breast asymmetries in an adult German population. Methods Breast base dimensions, breast volume, symmetry, and other breast anthropometric parameters of 400 German female patients were determined in a retrospective review of the MRI archives at our institution. Professional medical MRI-segmentation software was used for volume measurement. Results A total of 400 Patients were retrospectively enrolled. The patients had a mean age of 50 ± 12 years (min: 24; max: 82), mean BMI of 25.0 ± 5.0 (min: 14.7, max: 45.6), and a mean total breast volume of 976 ml (right: 973 ml, min: 64, max: 4777; left: 979 ml, min: 55, max: 4670). The strongest correlation of breast volume was observed with BMI (r = 0.834, p 2 , micromastia is defined by breast volumes below 250 ml (5th percentile) and macromastia by volumes above 1250 ml (95th percentile). Abnormal breast volume asymmetry ( 95th percentile) is equivalent to an absolute difference of approximately 25% relative to the smallest side (bidirectional asymmetry ratio 5th percentile - 19%; 95th percentile 26%). Conclusion This study provides normative data of German women, as well as selected size-for-BMI percentiles and asymmetry ratio percentiles. The normative data may help to establish transparent and objective coverage criteria for health insurances. Level of evidence iv This journal requires that authors assign a level of evidence to each article. For a full description of these Evidence-Based Medicine ratings, please refer to the Table of Contents or the online Instructions to Authors www.springer.com/00266 .

## P42b6963f9495

- Year: 2025
- Linked people: Stirling Bryan
- Title: Characterizing models for delivery of pharmacogenomic testing: a scoping review

Abstract:

Pharmacogenomic (PGx) testing can help guide medication prescribing for a wide range of health indications. The objective of this scoping review was to understand how PGx testing has been clinically implemented and learn from these experiences. Research questions guiding this work were: (1) what different models for delivery of PGx testing have been employed? (2) what are the characteristics of each delivery model? and (3) what are the reported facilitators and barriers associated with each delivery model? A total of 134 articles reported on 125 PGx initiatives spanning 19 countries. Four unique delivery models were identified: sole prescriber-led (n = 45), prescriber-led within an interdisciplinary care team (n = 34), community pharmacist-led (n = 16), and PGx consultation service (n = 30). The unique combination of characteristics, and reported facilitators and barriers yielded distinct strengths and challenges for each identified delivery model. Findings from this review can help inform future implementation planning or expansion of PGx initiatives by presenting different delivery models that may be employed and the corresponding considerations for each approach. This information can help inform future implementers in the selection of one or more approaches that may be most suitable based on their unique contextual needs, and available infrastructures or resources.

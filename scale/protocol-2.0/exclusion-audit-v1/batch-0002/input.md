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

## Pe5090fcec6ca

- Year: 2025
- Linked people: Sayem Ahmed
- Title: Cost-Effectiveness of Community-Based Interventions for Hypertension Prevention and Management: A Protocol

Abstract:

Introduction: Hypertension presents a global health challenge, contributing significantly to household and health system costs. While clinical effectiveness of hypertension interventions is well documented, evidence on the cost-effectiveness of community-based interventions remains limited. This review aims to evaluate the economic evidence of community-based interventions for hypertension prevention and management and compare cost-effectiveness estimates across diverse geographical and implementation settings. Methods: A systematic search will be conducted across databases such as Scopus, Web of Science, Cumulative Index to Nursing and Allied Health Literature Plus, American Psychological Association PsyclNFO, National Health Service Economic Evaluation Database, and Cochrane Central, covering literature up to January 2025. Grey literature and preprints will also be included. Eligible Judies will be full economic evaluations comparing two or more community-based interventions, in any language. Two reviewers will independently screen Judies using RAYYAN software. Quality assessment will be performed using validated checkMs. A meta-analysis will be undertaken contingent upon the presence of adequate homogeneity in outcomes and methodologies. Discussion: This review will highlight cost-effectiveness estimates and identify methodological and subject-specific gaps in the literature which can provide comprehensive insights to inform policy decision on CBIs for HTN. While focusing on adult populations may introduce publication bias, this will be considered during interpretation. Systematic review registration: This review is registered under PROSPERO, Indentifier: CRD420246129.

## P678376fbdea1

- Year: 2026
- Linked people: Wolfgang Greiner
- Title: Enhancing Continuous Medication Safety Through e-Prescription and Clinical Decision Support Systems in Outpatient Practices and Pharmacies: Protocol for a Multiperspective Study (eRIKA Study).

Abstract:

Increased life expectancy is associated with increasing multimorbidity and polypharmacy, leading to a heightened risk of drug-drug interactions and adverse events, especially when multiple health care providers are involved. To address the urgent need for safer medication management in this population, tools such as medication plans (MP), electronic prescriptions (e-prescriptions), and clinical decision support systems (CDSS) offer valuable support. These instruments have the potential to enhance medication safety by providing physicians and pharmacists with a comprehensive overview of a patient's overall medication regimen and by assisting health care professionals in making informed prescribing decisions.
This study aims to improve medication therapy safety by combining e-prescriptions, the use of claims data, MPs, CDSS, and interprofessional communication. To comprehensively evaluate this complex intervention, a holistic multiphase study will be conducted, examining (1) the effectiveness of the intervention and (2) health-economic and (3) implementation-related aspects.
A multiphase study design is used. In the first phase, the intervention is implemented in selected outpatient practices (n=10) and pharmacies (n=10) in 2 regions in Germany as part of a cluster-randomized controlled trial to assess process-related outcomes. The primary outcome is the congruence between the MP and claims data. In phase 2, the intervention is scaled up in 3 regions and evaluated in a quasi-experimental study. The required sample size for the intervention group is 3528 patients, with a synthetic control group matched from existing claims data. The primary outcome is a combined end point of all-cause mortality and hospitalization within 3 months of an index prescription. Quantitative methods (descriptive, regression-based methods using claims data, calculation of the incremental cost-effectiveness ratio, and survey-based analyses of implementation-related aspects) and qualitative methods (interviews and focus groups to capture experiences of health care professionals and patients) are used.
In phase 1, a total of 187 patients were recruited (74 in the intervention group and 113 in the control group) by June 2025. Phase 2 is currently ongoing, with data collection continuing through December 31, 2025. Final analyses are planned by March 2027.
Medication safety in polypharmacy remains a critical challenge in Germany. This study provides multiperspective evidence supporting the nationwide implementation of the eRIKA (e-prescription as an element of interprofessional care pathways for continuous medication therapy management [eRezept als Element interprofessioneller Versorgungspfade für kontinuierliche AMTS]) intervention.

## Pebd4ed8d0226

- Year: 2025
- Linked people: Hsiang-Wen Lin
- Title: Charting the path to better diabetes outcomes: Revealing psychosocial influences on medication adherence through the information-motivation-behavioral skills model among adults with type 2 diabetes

Abstract:

Background Psychosocial factors like beliefs, distress, and behavioral skills affect medication adherence. The Information-Motivation-Behavioral Skills (IMB) model addresses these through integrated knowledge, motivation, and skills to support adherence. Objective This study applied the IMB model to identify salient factors associated with medication adherence and glycemic control among adults with type 2 diabetes (T2D), aiming to clarify mechanisms underlying non-adherence. Methods A cross-sectional survey was conducted from June 2023 to May 2024 at five community pharmacies in Taiwan using convenience sampling. Eligible participants were adults diagnosed with T2D, currently prescribed at least one oral diabetes medication, and able to read Traditional Chinese. Data were collected via a structured questionnaire covering demographics, clinical characteristics, and four IMB-based constructs. Specifically, eHealth literacy represented the information component; medication-related beliefs (i.e., perceived concerns and necessity of medications) reflected the motivation construct; and self-efficacy captured behavioral skills. Medication adherence was assessed in two domains: medication-taking and medication refill behaviors. Path analysis was used to examine relationships among psychosocial variables, adherence behaviors, and glycemic control. Results A total of 273 participants completed the questionnaire. Higher self-reported medication-taking behavior was significantly associated with better glycemic control (β = 0.198, p Conclusions The IMB model offers a useful framework for understanding adherence behaviors in T2D. Self-efficacy emerged as a central influence, mediating the effects of eHealth literacy and beliefs about medicines.

## P5ef1ae01f406

- Year: 2025
- Linked people: thomas kohlmann
- Title: How does an intervention work?—English Version

Abstract:

In addition to the usual evaluation approach (usually a clinical randomized trial in the sense of the question: does an intervention work), complex interventions require further systematic investigations to prove their effectiveness. The role of the context in which the intervention is delivered is essential here, as is consideration of the question of why an intervention works (or does not work). Detailed recommendations exist for the planning and implementation of effectiveness studies on complex interventions, to which interdisciplinary multimodal pain therapy undoubtedly belongs. In an effectiveness model, concrete, verifiable assumptions are formulated as to how an intervention produces changes that are reflected in the endpoint. This article provides a brief introduction to methodological approaches to effectiveness research on complex interventions and uses the PAIN 2.0 project (01NVF20023) to describe in concrete terms what an effectiveness model for interdisciplinary multimodal pain therapy for the prevention of chronic pain in an outpatient setting might look like.

## P240c0e07412d

- Year: 2024
- Linked people: Eleanor Pullenayegum
- Title: Disease activity trajectories in juvenile dermatomyositis from childhood to adulthood

Abstract:

OBJECTIVES: To assess whether there are identifiable subgroups of disease activity trajectory in a population of JDM patients-followed throughout childhood and into adulthood-and determine factors that predict those trajectory groupings. METHODS: This is a retrospective, longitudinal inception cohort of patients with idiopathic inflammatory myopathies, largely JDM. We sought to identify baseline factors that predict membership into different groups (latent classes) of disease activity trajectory. RESULTS: A total of 172 patients (64% females), with median age at diagnosis of 7.7 years, were analysed. We studied 4725 visits (1471 patient-years). We identified three latent classes of longitudinal disease activity, as measured by the modified DAS (DASm), with distinct class trajectories predicted by DASm at baseline, and by the changes of DASm from either baseline to 3 months or baseline to 6 months (early response to therapy). In the analysis in which DASm at baseline and the changes of DASm from baseline to 6 months are included as predictors, Class 1 (10%) has persistently high disease activity, Class 2 (34%) is characterized by moderate disease activity and Class 3 (56%) is characterized by individuals with a high early disease activity but an apparently good response to treatment and long-term low disease activity. CONCLUSION: High early disease activity, and treatment resistance in the first few months, predict a more chronic longitudinal course of JDM.

## Pec33a491c709

- Year: 2025
- Linked people: Carlos Wong
- Title: Single and combined anti-COVID-19 drugs among hospitalised patients: abridged secondary publication.

Abstract:

Single and combined anti-COVID-19 drugs among hospitalised patients: abridged secondary publication

## Pa33c02db507d

- Year: 2025
- Linked people: Jermaine Dambi
- Title: Predictors of physical activity among pregnant women in Harare, Zimbabwe

Abstract:

The extensive benefits of physical activity (PA) are well known. However, PA participation among pregnant women remains low. This study evaluated PA levels and associated factors, including barriers and facilitators in pregnant women in Harare, Zimbabwe. This cross-sectional study recruited 517 pregnant women receiving antenatal care across ten primary healthcare clinics. Data were collected using the Pregnancy Physical Activity Questionnaire (PPAQ), Exercise Benefits and Barriers Scale (EBBS) and EQ-5D-5L. We used descriptive statistics and binary logistic regression for analyses. The mean age of the study participants was 26.1 (±5.9) years. 89% of the pregnant women did not meet the WHO recommendations of 150 minutes of moderate-intensity PA. For women who were active, most engaged in moderate intensity (41.9%) PA and household activity (51.1%). The most perceived barriers and facilitators to PA were reported as exercise environment and life enhancement, respectively. Lower education (AOR 5.24 [1.69: 16.19]), multigravida (AOR .47 [.31: .42]), not exercising pre-pregnancy (AOR 2.02 [1.30: 3.13]), perceived decreased current PA level (AOR 2.04 [1.22: 3.43]) and not being advised by a doctor on exercise (AOR 2.05 [1.04: 4.04]) were associated with physical inactivity. Physical inactivity is endemic among Zimbabwean pregnant women, there is a need for bespoke and contextualized interventions. Implementing supervised and group-based antenatal exercise classes must be considered.

## P066d33efcffd

- Year: 2024
- Linked people: Jan Verhaar
- Title: Lower Extremity Tendinopathies are Associated with Metabolic and Chronic Diseases: A Systematic Review

Abstract:

Background. Recent narrative reviews suggest an association between lower extremity tendinopathies and metabolic and chronic diseases. This association might lead to early recognition and change in clinical management, but it has, however, never been assessed systematically. Objective. To analyze the association between lower extremity tendinopathies and metabolic and chronic diseases in a systematic review. We searched studies in Embase, Medline Ovid, Web of Science, Cochrane library and Google Scholar. Articles were eligible if the association between clinically diagnosed lower extremity tendinopathies and a metabolic or chronic disease in adult patients was reported. Results. From 4,287 eligible studies, we included 10 cohort studies and 10 case-control studies, involving 83,948 participants. Almost all (90%) included studies were assessed as having a high risk of bias. These studies had moderate evidence for an association between lower extremity tendinopathies and obesity, ankylosing spondylitis, psoriatic arthritis, and reactive arthritis. There was limited evidence for an association between lower extremity tendinopathies and heterozygous familial hypercholesterolemia, and Systemic Lupus Erythematosus. Conclusions. We found multiple associations between lower extremity tendinopathies and metabolic and chronic diseases. These results suggest that medical professionals should screen for these specific metabolic and chronic diseases in patients with lower extremity tendinopathies. Study registration. The review has been prospectively registered in the international PROSPERO database. Protocol details were submitted in June 2019 and registered in September 2019 (registration number: CRD42019140317).

## P15dc10ceedc2

- Year: 2025
- Linked people: Fredrick Purba
- Title: Exploring the impact of virtual reality-based mathematics learning on students' motivation: Protocol for a systematic review and meta-analysis.

Abstract:

It has been extensively documented that motivation plays a pivotal role in both the learning and performance of mathematics, often intersecting with various antecedents of mathematical competence, such as math anxiety and self-esteem. These factors, in turn, significantly influence the well-being of students. Therefore, it is necessary to provide learning situations that may impact students' motivation in learning mathematics. During the digital era, studies have examined the use of technology, particularly, virtual reality-based mathematics learning in explaining the variance of students' motivation in mathematics learning. However, the results seem to be various and a comprehensive review about the impact of virtual reality mathematics learning on students' motivation does not seem to exist yet. This review aims to fill this knowledge gap by examining the impact of mathematics learning using virtual reality-based learning materials on students' motivation. The literature search will be conducted across multiple bibliographic databases, including Cambridge, Oxford, PubMed, Science Direct, Scopus, SpringerLink. Only studies published in English, German, or Indonesian within the past seven years will be eligible for inclusion in the review. The risk of bias inherent in this review will be evaluated by two independent reviewers utilizing the Joanna Briggs Institute (JBI) critical assessment tool. Any discrepancies between the reviewers will be resolved through the third reviewer. Further, quality of evidence will be examined using The Grading of Recommendations, Assessment, Development, and Evaluations (GRADE). A review exploring the correlation between mathematics education utilizing virtual reality and student motivation will offer educational practitioners and stakeholder's valuable insights into the effective integration of technology-based learning resources, particularly virtual reality. The findings of this study aim to elucidate the advantages and potential drawbacks associated with the adoption of virtual reality in mathematics education, as well as identify the student and instructional material characteristics that may be associated with specific increases in motivation. This protocol has been registered in PROSPERO with registration number: CRD42023463974.

## Pe6ce40f447b0

- Year: 2025
- Linked people: Kim Dalziel
- Title: Polysomnographic titration of non-invasive ventilation in motor neurone disease (3TLA): study protocol for a randomised controlled trial

Abstract:

BACKGROUND: Non-invasive ventilation (NIV) uses positive pressure to assist people with respiratory muscle weakness or severe respiratory compromise to breathe. Most people use this treatment during sleep when breathing is most susceptible to instability. The benefits of using NIV in motor neurone disease (MND) are well-established. However, uptake and usage are low (~ 19%) and there is no consensus on how to best implement NIV in MND in Australia. Consequently, clinical practice models are highly variable. Our team has recently provided evidence that specific and individualised NIV titration using a sleep study (polysomnography; PSG) leads to better outcomes in people with MND. However, for this clinical practice model to result in sustained benefits, evidence of effectiveness across multiple sites, as well as culture and practice change, must occur. METHODS: A two-arm, assessor-blinded, individual participant randomised controlled trial in MND care centres across Australia will be undertaken. Two-hundred and forty-four participants will be randomised (1:1) to either the intervention group (PSG-assisted commencement of NIV settings; PSG) or a control group (sham PSG). Participants will be asked to use their NIV device for 7 weeks and will then return for follow-up assessments. Respiratory, sleep and patient-reported outcome measures will be collected at baseline and follow-up. The primary aim is to determine if the proportion of participants using NIV for > 4 h/day during the intervention period is higher in the PSG than the control group. A process evaluation, health economic evaluation and 12-month cohort follow-up will be undertaken and reported separately. DISCUSSION: The results of this trial will demonstrate the effects of PSG-assisted titration of NIV on usage of NIV in people with MND. We hypothesise that the PSG intervention will improve synchrony between the user and the machine, which will lead to greater NIV usage compared to the control group. TRIAL REGISTRATION: ClinicalTrials.gov NCT05136222. Registered on November 25, 2021.

## P4e46e06eccbf

- Year: 2026
- Linked people: Philip Powell
- Title: Assessing the association of physical distancing to avoid COVID-19 with health-related quality of life in immunocompromised adolescents: results from the cross-sectional observational EAGLE study

Abstract:

Objective We describe physical distancing behaviors to avoid coronavirus disease 2019 (COVID-19) and their associations with health-related quality of life (HRQoL) and related outcomes, among immunocompromised adolescents (aged 13–17 years). Methods EAGLE was a cross-sectional, observational study of immunocompromised adults, adolescents, and children in the United States and United Kingdom. Adolescents and their caregivers were enrolled between February and June 2023 and completed a web-based survey that was designed to capture the following outcomes: physical distancing behaviors in the past 4 weeks, measured using the Physical Distancing Scale for COVID-19 Avoidance (PDS-C19®); HRQoL (Pediatric Quality of Life Inventory™ [PedsQL™] Generic Core Scales); loneliness (Direct Measure of Loneliness [DMOL] scale); health-state utility (EQ-5D-5L); mental health (Hospital Anxiety and Depression Scale; HADS®); and school and activity impairment (Work Productivity and Activity Impairment plus Classroom Impairment Questions: Specific Health Problem questionnaire; WPAI-CIQ:SHP). Results Among 405 immunocompromised adolescents, the PDS-C19 mean T-score was 49.1, indicative of moderate physical distancing intensity. Most participants reported moderate (60.1%) or high/very high (16.3%) physical distancing intensity; fewer reported low (10.0%) or very low (13.7%) physical distancing intensity. The PedsQL™ Generic Core Scales mean total score was 58.0 (scale range: 0–100, where higher scores indicate better HRQoL). Most outcomes moderately correlated with PDS-C19 (| r | = 0.4–0.5), with stronger correlations (| r |&amp;gt;0.6) shown for WPAI-CIQ:SHP activity impairment, school presenteeism, and overall school impairment. Linear regression models adjusting for confounders showed similar associations. Conclusions Two years after national lockdowns ended, most immunocompromised adolescents practiced moderate-to-high intensities of physical distancing to avoid COVID-19. Higher intensities of physical distancing were associated with worse HRQoL and greater school and activity impairment, emphasizing the prolonged burden of COVID-19 avoidance in this population.

## Pbd748226e344

- Year: 2025
- Linked people: Irina Kinchin
- Title: Feasibility Study for Implementing Disease‐Modifying Therapies in Alzheimer's Disease: Process Measures and Patient Pathways across Ireland

Abstract:

BACKGROUND: Alzheimer's disease (AD) is a leading cause of cognitive decline, and the recent European approval of disease-modifying therapies (DMTs) like Donanemab and Lecanemab offers new hope for slowing its progression. However, healthcare systems across Europe, including Ireland, are unprepared for their real-world implementation. Challenges include equitable access, infrastructure readiness, and treatment logistics. This study aims to evaluate the feasibility of implementing DMTs across public and private healthcare sectors in Ireland, positioning it as a stepping stone toward broader European readiness. METHOD: This multi-center observational feasibility study will assess DMT implementation readiness across Irish centers (Dublin, Waterford, Cork, Galway). The study employs patient journey mapping using retrospective and hypothetical data, alongside evaluations of key process measures, including referral timelines, biomarker verification, infusion readiness, and follow-up protocols. Graph-theory modeling will visualize patient pathways and highlight system inefficiencies. RESULTS: The study is expected to reveal disparities in DMT access, logistical bottlenecks, and enablers for scalable implementation. Graph-based modeling will provide actionable insights to optimize patient pathways and healthcare delivery frameworks. Stakeholder feedback will inform patient-centered approaches and address equity challenges. CONCLUSION: This feasibility study addresses the critical need for preparedness in integrating DMTs for AD, which were recently approved in Europe but remain underutilized due to systemic barriers. By generating actionable insights and laying the groundwork for national guidelines, this project not only advances Ireland's readiness but also serves as a model for other European countries seeking to adopt transformative therapies for Alzheimer's disease.

## Pb55941750683

- Year: 2025
- Linked people: Prudence Cheung
- Title: Exploring the potential relationships between idiopathic scoliosis and various multifactorial diseases: a systematic scoping review.

Abstract:

Although the etiology of adolescent idiopathic scoliosis (AIS) remains largely elusive, it is widely recognized as a multifactorial condition shaped by both genetic predispositions and environmental influences. This review seeks to explore the intricate relationships between idiopathic scoliosis and its associated comorbidities, with the goal of advancing our understanding of this multifaceted disorder.
Primary studies involving human subjects diagnosed with idiopathic scoliosis and presenting comorbid conditions were included. Six online databases (AMED, CENTRAL, CINAHL, EMBASE, MEDLINE, and WOS) were systematically searched. Two reviewers independently screened citations and extracted data. Studies were categorized based on commonly examined diagnoses, and outcome measures were descriptively reported.
Our search yielded 1185 citations, with 9 studies meeting the eligibility after screening. These studies examined comorbidities involving conditions like malocclusion, central precocious puberty (CPP), gingival diseases, malignant hematopoietic neoplasms (MHN), temporomandibular joint disorders (TMD), and functional gastrointestinal disorders (FGD). Significant associations were found between AIS and these multifactorial disorders, including dental anomalies (i.e., asymmetrical canine, midline deviations, crossbites, overbite, multiple malocclusion, gingivitis, distocclusion, asymmetric molar occlusion, maxillary overjet, crowding, and reverse chewing cycles), digestive issues (i.e., FGD), endocrine disruptions (i.e., CPP), musculoskeletal imbalances (i.e., reduced masseter muscle volume, higher Fonseca Anamnestic Index score, and greater Helkimo Clinical Dysfunction Index score), and oncological conditions (i.e., MHN).
We have presented the multifactorial and potential systemic nature of AIS by revealing its associations with comorbid conditions. These relationships may indicate shared genetic, hormonal, neuromuscular, and immunological pathways.

## P937fa69f768e

- Year: 2026
- Linked people: Ilias Goranitis
- Title: Australian parents' perspectives on extended genomic screening: what information to return and when?

Abstract:

Genomic newborn screening (gNBS) has the potential to generate information that remains relevant across the lifespan, yet little is known about how families who have directly experienced gNBS, understand its long-term role and value. This study analysed the results of eight focus groups with 32 parents whose children had received findings from gNBS (through the BabyScreen+ study, a population-based Australian gNBS pilot programme), to explore how they conceptualise the use of genomic information beyond infancy (which we refer to as extended genomic sequencing, or eGS). Parents described a complex interplay of factors including treatability, severity, certainty, and personal capacity to manage information that shaped their desire to receive results. Using the Health Belief Model as a lens, we show how parental reflections mapped to constructs such as perceived benefits, barriers, severity, susceptibility, self-efficacy, and cues to action. However, parents' reasoning was dynamic rather than static, illustrating how shifts in clinical options or family circumstances influence decision making over time. Overall, our findings demonstrate that families view gNBS data as a potential lifetime resource and support the need for flexible consent pathways, ongoing counselling, and governance frameworks that anticipate both the benefits and burdens of genomic information. This work offers timely insights to inform ethical implementation of eGS in Australia and contributes to international discussions about integrating genomic sequencing into population-level screening.

## Pc87f361243fb

- Year: 2025
- Linked people: Begashaw Melaku Gebresillassie
- Title: Development and Validation of a Risk Prediction Model to Identify Women With Chronic Obstructive Pulmonary Disease for Proactive Palliative Care.

Abstract:

BACKGROUND AND OBJECTIVE: Proactive palliative interventions can improve symptom control and quality of life in individuals with chronic obstructive pulmonary disease (COPD); however, they are often underutilised. This study aimed to develop and validate a prediction model to identify women with COPD in their last year of life to facilitate timely palliative care referrals and interventions. METHODS: Data from 1236 women diagnosed with COPD from the 1921-1926 Australian Longitudinal Study on Women's Health cohort, linked to administrative health records, were analysed. We employed Lasso regression and multivariable logistic regression to select predictors. To assess the predictive performance of the model, we used the area under the receiver operating characteristic (AUROC) curve, calibration plot, and calibration metrics. The Youden index was used to establish the optimal cutoff point for risk classification. The clinical utility of the model was evaluated using decision curve analysis (DCA). RESULTS: The final model to predict 1-year all-cause mortality included six predictors: smoking status, body mass index, needing regular assistance with daily activities, number of supplied medications, duration of illness, and number of hospital admissions. The model performed well, with AUROC of 0.82 (95% CI: 0.80-0.85) and showed excellent calibration. Using a cutoff of 56.6% predicted risk, the model achieved a sensitivity of 72.3%, specificity of 77.7%, and accuracy of 75.0%. The DCA indicated that the model provided a greater net benefit for clinical decision-making. CONCLUSION: Our prediction model for identifying women with COPD who may benefit from palliative care has shown robust predictive performance and can be easily applied, but requires external validation.

## P0949b2a72add

- Year: 2024
- Linked people: Márta Péntek
- Title: The Reporting Quality of Machine Learning Studies on Pediatric Diabetes Mellitus: Systematic Review.

Abstract:

BACKGROUND: Diabetes mellitus (DM) is a major health concern among children with the widespread adoption of advanced technologies. However, concerns are growing about the transparency, replicability, biasedness, and overall validity of artificial intelligence studies in medicine. OBJECTIVE: We aimed to systematically review the reporting quality of machine learning (ML) studies of pediatric DM using the Minimum Information About Clinical Artificial Intelligence Modelling (MI-CLAIM) checklist, a general reporting guideline for medical artificial intelligence studies. METHODS: We searched the PubMed and Web of Science databases from 2016 to 2020. Studies were included if the use of ML was reported in children with DM aged 2 to 18 years, including studies on complications, screening studies, and in silico samples. In studies following the ML workflow of training, validation, and testing of results, reporting quality was assessed via MI-CLAIM by consensus judgments of independent reviewer pairs. Positive answers to the 17 binary items regarding sufficient reporting were qualitatively summarized and counted as a proxy measure of reporting quality. The synthesis of results included testing the association of reporting quality with publication and data type, participants (human or in silico), research goals, level of code sharing, and the scientific field of publication (medical or engineering), as well as with expert judgments of clinical impact and reproducibility. RESULTS: After screening 1043 records, 28 studies were included. The sample size of the training cohort ranged from 5 to 561. Six studies featured only in silico patients. The reporting quality was low, with great variation among the 21 studies assessed using MI-CLAIM. The number of items with sufficient reporting ranged from 4 to 12 (mean 7.43, SD 2.62). The items on research questions and data characterization were reported adequately most often, whereas items on patient characteristics and model examination were reported adequately least often. The representativeness of the training and test cohorts to real-world settings and the adequacy of model performance evaluation were the most difficult to judge. Reporting quality improved over time (r=0.50; P=.02); it was higher than average in prognostic biomarker and risk factor studies (P=.04) and lower in noninvasive hypoglycemia detection studies (P=.006), higher in studies published in medical versus engineering journals (P=.004), and higher in studies sharing any code of the ML pipeline versus not sharing (P=.003). The association between expert judgments and MI-CLAIM ratings was not significant. CONCLUSIONS: The reporting quality of ML studies in the pediatric population with DM was generally low. Important details for clinicians, such as patient characteristics; comparison with the state-of-the-art solution; and model examination for valid, unbiased, and robust results, were often the weak points of reporting. To assess their clinical utility, the reporting standards of ML studies must evolve, and algorithms for this challenging population must become more transparent and replicable.

## P741e46b11a50

- Year: 2025
- Linked people: Sander van Kuijk
- Title: Heterogeneity in clinical judgment of septal lead position and capture type in left bundle branch area pacing

Abstract:

BACKGROUND: Determining capture type and septal lead location during left bundle branch area pacing (LBBAP) relies on criteria obtained during implantation. However, during follow-up, the interpretation of left bundle branch (LBB) capture largely depends on QRS morphology, which is not so straightforward in LBBAP. OBJECTIVE: This study aimed to investigate the inter- and intraobserver agreement, as well as the accuracy of clinical judgment of the electrocardiogram (ECG) in determining LBB-capture and septal lead position in patients undergoing LBBAP implantation. In addition, the role of vectorcardiographic QRS-area in determining LBB-capture was evaluated. METHODS: Unipolar paced ECGs during LBBAP implantation from 50 patients with baseline narrow QRS were collected. LBB-capture was attempted in all patients and assessed using MELOS (Multicentre European Left Bundle Branch Area Pacing Outcomes Study) criteria and the European Heart Rhythm Association (EHRA) consensus statement. Eight blinded cardiologists classified 100 ECGs for capture type and septal location. RESULTS: The interobserver and intraobserver agreement for capture type had a Light's kappa of 0.43 and 0.62, respectively. Concordance between clinical judgment and intraprocedural confirmation averaged 72%. Interobserver and intraobserver agreement for septal lead position had a Light's kappa of 0.43 and 0.77 respectively. QRS-area was significantly higher for left ventricular septal pacing (LVSP) than nsLBBP, whereas QRS duration was not. A QRS-area cutoff of 26 mV.ms had 77% accuracy in distinguishing LVSP from nsLBBP. Clinical judgment accuracy averaged 72%. CONCLUSION: Interobserver agreement and correlation with intraprocedural confirmation (gold standard) are only moderate, whereas intraobserver agreement on ECG-based differentiation of capture type and septal lead location is substantial. Vectorcardiographic QRS-area slightly outperforms clinical judgment in distinguishing capture types and may be a useful objective alternative.

## P03721db290e9

- Year: 2024
- Linked people: Hesam Ghiasvand
- Title: Optimising the diagnostic accuracy of First post-contrAst SubtracTed breast MRI (FAST MRI) through interpretation-training: a multicentre e-learning study, mapping the learning curve of NHS Breast Screening Programme (NHSBSP) mammogram readers using an enriched dataset

Abstract:

BACKGROUND: Abbreviated breast MRI (FAST MRI) is being introduced into clinical practice to screen women with mammographically dense breasts or with a personal history of breast cancer. This study aimed to optimise diagnostic accuracy through the adaptation of interpretation-training. METHODS: A FAST MRI interpretation-training programme (short presentations and guided hands-on workstation teaching) was adapted to provide additional training during the assessment task (interpretation of an enriched dataset of 125 FAST MRI scans) by giving readers feedback about the true outcome of each scan immediately after each scan was interpreted (formative assessment). Reader interaction with the FAST MRI scans used developed software (RiViewer) that recorded reader opinions and reading times for each scan. The training programme was additionally adapted for remote e-learning delivery. STUDY DESIGN: Prospective, blinded interpretation of an enriched dataset by multiple readers. RESULTS: 43 mammogram readers completed the training, 22 who interpreted breast MRI in their clinical role (Group 1) and 21 who did not (Group 2). Overall sensitivity was 83% (95%CI 81-84%; 1994/2408), specificity 94% (95%CI 93-94%; 7806/8338), readers' agreement with the true outcome kappa = 0.75 (95%CI 0.74-0.77) and diagnostic odds ratio = 70.67 (95%CI 61.59-81.09). Group 1 readers showed similar sensitivity (84%) to Group 2 (82% p = 0.14), but slightly higher specificity (94% v. 93%, p = 0.001). Concordance with the ground truth increased significantly with the number of FAST MRI scans read through the formative assessment task (p = 0.002) but by differing amounts depending on whether or not a reader had previously attended FAST MRI training (interaction p = 0.02). Concordance with the ground truth was significantly associated with reading batch size (p = 0.02), tending to worsen when more than 50 scans were read per batch. Group 1 took a median of 56 seconds (range 8-47,466) to interpret each FAST MRI scan compared with 78 (14-22,830, p < 0.0001) for Group 2. CONCLUSIONS: Provision of immediate feedback to mammogram readers during the assessment test set reading task increased specificity for FAST MRI interpretation and achieved high diagnostic accuracy. Optimal reading-batch size for FAST MRI was 50 reads per batch. Trial registration (25/09/2019): ISRCTN16624917.

## Pa531f68e6efc

- Year: 2026
- Linked people: Harri Sintonen
- Title: The Effect of Age on Improvement in Health‐Related Quality of Life After Percutaneous Coronary Intervention

Abstract:

INTRODUCTION: Percutaneous coronary intervention (PCI) is the first-line therapy in patients scheduled for coronary revascularization, aiming to relieve symptoms of coronary artery disease (CAD) and improve health-related quality of life (HRQoL) and prognosis. Particularly, in older adults, symptom alleviation and HRQoL are emphasized. However, it is not known whether older patients benefit from PCI equally to their younger peers. We used disease-specific and generic instruments to evaluate the improvement in HRQoL after PCI, comparing changes in three age groups. METHODS: Altogether 300 patients undergoing PCI were divided into three age groups: ≥ 75 years (n = 89), 66-74 years (n = 117), and ≤ 65 years (n = 94). HRQoL was measured using the disease-specific Seattle Angina Questionnaire (SAQ-7) and the generic 15D instrument at baseline, one, and 12 months. RESULTS: Statistically and clinically significant improvements in the SAQ-7 and 15D scores were observed after one- and 12-month follow-up in all age groups. There were no differences in the 12-month improvements in the SAQ-7 and 15D scores between the groups. The 15D score started to decline after 1 month, particularly in the oldest group. The decline was associated with age-related rather than CAD-related 15D dimensions. CONCLUSIONS: Our findings on comparable improvement in disease-specific and generic HRQoL after PCI in older and younger patients are encouraging, particularly considering that the aims of PCI in older adults are predominantly symptom alleviation and improvement of daily activities. In addition, to overcome age-related changes in HRQoL, a disease-specific instrument should be incorporated in the evaluation of PCI on HRQoL. CLINICAL TRIAL REGISTRATION: 5101114.

## P8d3a3c95b73c

- Year: 2025
- Linked people: Aaron Winn
- Title: Effects of urban greenspace on time to major adverse cardiovascular events among women with breast cancer in the US: Insights from the Greater Milwaukee, WI Area

Abstract:

Background Cardiovascular (CV) disease (CVD) remains a significant concern among breast cancer (BC) survivors, particularly following potentially cardiotoxic treatments, such as anthracyclines and anti-HER2 drugs, which increase the risk of major adverse CV events (MACE). Social determinants of health (SDOH) and environmental factors influence health outcomes, including those related to CVD. Urban greenspace has been associated with CV and cancer-related health benefits, yet its specific impact on MACE among BC survivors remains unknown. Objective This study aims to investigate the association between urban greenspace and time to first MACE incidence among individuals with BC after being treated with cardiotoxic therapies in the greater Milwaukee, WI area. Methods A retrospective cohort study was conducted using electronic medical records from the Froedtert Health System, linked to the National Death Index. Cox proportional hazards regression models were used to assess the association between percent tree canopy cover and MACE-specific hazards, adjusting for sociodemographic, clinical, and neighborhood-level factors. Results Among the 849 women included, 44.6 % experienced a MACE. Adjusted models indicated an 18 % reduction in MACE-specific hazard (HR: 0.82, 95 % CI: 0.70, 0.96) and a 20 % reduction in MACE-specific hazard (HR: 0.80, 95 % CI: 0.67, 0.97) for women in the second and third quartiles of percent tree canopy cover, respectively, compared to the women in the first (lowest) quartile. However, we did not observe a risk difference for women living in the fourth quartile of tree canopy. Racial/ethnic disparities in greenspace exposure and MACE incidence were evident, with Non-Hispanic Black (NHB) women having a lower proportion living in areas with the highest tree canopy cover and a higher MACE incidence (61.9 %) compared to Non-Hispanic White (NHW) women (41.6 %), who had the highest proportion residing in areas within the 4th quartile of tree canopy cover. Discussion Our findings suggest that urban tree canopy is associated with time to incident MACE among BC survivors receiving cardiotoxic treatments. These results underscore the importance of considering socioenvironmental factors in CardioOncology care and highlight the benefits of greenspace in mitigating CV complications among individuals with BC. Future research should delve into individual lifestyle and behavioral factors, environmental factors, and biological mechanisms that may underlie these associations. Additionally, longitudinal studies should be conducted to evaluate greenspace-based interventions for BC survivors, aiming to advance precision CardioOncology interventions. Observed racial/ethnic disparities in MACE incidence underscore the urgent need for equity-focused interventions addressing greenspace access and MACE-related disparities.

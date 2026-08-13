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

## P28a27cc6411d

- Year: 2020
- Linked people: Piyameth Dilokthornsakul
- Title: Glossary for systematic reviews and meta-analyses

Abstract:

A systematic review aims to answer a focussed research question through a structured review of the evidence, using a predefined methodology, which often includes a meta-analysis. A meta-analysis is a statistical method used to combine the effect estimates from the individual studies included in a systematic review. Systematic reviews and meta-analyses are positioned at the highest level in the hierarchy of clinical evidence. The Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) statement was introduced in 2009 to help authors improve the quality and reliability of systematic reviews and meta-analyses. Recently, the volume of systematic reviews and meta-analyses in the field of Endodontology has increased; however, the quality of the published manuscripts has been reported to be sub-optimal, which does not take account of the systematic reviews that were rejected because of more obvious deficiencies. The aim of this paper is to present a comprehensive glossary of terminology commonly used in systematic reviews and meta-analyses in an attempt to provide easily understood definitions and explanations to assist authors when reporting systematic reviews and meta-analyses and to allow those wishing to read them to become better informed.

## Pd89954f39a01

- Year: 2002
- Linked people: Ciaran O'Neill
- Title: Attitudes to physician and family assisted suicide: results from a study of public attitudes in Britain

Abstract:

TEST 02 - Elsevier's Scopus, the largest abstract and citation database of peer-reviewed literature. Search and access research from the science, technology, medicine, social sciences and arts and humanities fields.

## Pc18022692a61

- Year: 1996
- Linked people: Ciaran O'Neill
- Title: Cost effectiveness of personal health education in primary care for people with angina in the greater Belfast area of Northern Ireland.

Abstract:

STUDY OBJECTIVE: To investigate the cost effectiveness of personal health education for angina patients being treated in general practice. DESIGN: A randomised controlled trial in which people were randomised to intervention and control groups. All were assessed at the start and end of the study, with details recorded of disease status, coronary heart disease risk factors, and self assessed quality of life. A note was taken of their current use of drugs and over the course of the study their use of all health services. Those in the intervention group had three visits per year from a health visitor, whose brief was discuss ways of living more easily with their disease and in which risks of further events might be reduced. PATIENTS: Altogether 688 patents in the Greater Belfast area aged less than 75 years and known to have angina for at least six months. MAIN RESULTS: Significant improvements in survival and self assessed quality of life were found between the study and control groups. The intervention was associated with a reduction in drug usage and there was no significant difference between the intervention and control groups in terms of their use of other health services. CONCLUSION: Given the improvement in survival and self assessed quality of life and no significant differences in costs to the health service between the two groups, the intervention was deemed to be cost effective.

## P68ac5e9c9736

- Year: 2018
- Linked people: Ben Van Hout
- Title: The impact of co-morbidity on the disease burden of VTE

Abstract:

Venous thromboembolism (VTE) is often accompanied by co-morbidities, which complicate and confound data interpretation concerning VTE-related mortality, costs and quality of life. We aimed to assess the contribution of co-morbidities to the burden of VTE. The PREFER in VTE registry, across seven European countries, documented and followed acute VTE patients over 12 months. Patients with co-morbidities were grouped in major co-morbidity groups: cancer, cardiovascular (CV) comorbidity (other than VTE), CV risks, venous, renal, liver, respiratory, bone and joint diseases, and lower extremity paralysis. Mortality rates and health-related quality of life (HrQoL) utility values grouped per co-morbidity were compared to the UK general population. Regression analyses were performed to determine the impact of co-morbidities on mortality and HrQoL. VTE were analyzed together and separately as pulmonary embolism (PE) and deep vein thrombosis (DVT). In total, 3455 patients were included, 40.5% with PE and 59.5% with DVT. 13% and 16% of the PE and DVT patients had no co-morbidities and had a 12-month mortality rate of 1.8% and 1.7%, respectively. Frequency and severity of co-morbidities increased mortality rates up to 30%. The EQ-5D-5L index in patients without co-morbidities were 0.826 and 0.838 for PE and DVT. These scores decreased to 0.638 and 0.555 in the presence of co-morbidities. Co-morbidities in VTE patients are common. VTE had an impact on mortality and HrQoL, and additional impact of co-morbidities was seen. Awareness of the presence of co-morbidities is important when making VTE-related treatment decisions. The presence of co-morbidities in PE and DVT patients is common and their frequency and severity in VTE patients have a substantial impact on mortality rates and HrQoL. When adjusting for co-morbidities, the impact of VTE on mortality as well as health-related quality of life remains present. Assessing patients without consideration of co-morbidities might lead to misinterpretations of the disease burden of PE and DVT.

## Pc1019d8075e6

- Year: 2026
- Linked people: Fredrick Purba
- Title: Cost-effectiveness and budget impact analyses of Typhoid Vi capsular polysaccharide vaccination in Indonesia

Abstract:

Typhoid fever has a substantial economic impact in developing countries, including in Indonesia. As the most cost-effective intervention to prevent typhoid fever, vaccination has not yet been introduced in the country. This study aimed to analyse the cost-effectiveness and budget impact of typhoid vaccination strategies, focusing on high-burden regions in Indonesia. This study applied a top-down cost analysis method by collecting costs from various sources to estimate incremental cost-effectiveness ratio and to analyse the impact of this new program in a time horizon of six years within the scenario. In the first five years, the typhoid vaccine will be introduced only in high-risk areas, with nationwide vaccination starting in the sixth year. The results showed that vaccination can prevent 158,276 cases and 352 deaths in six years. It also could save treatment costs up to $10,655,063, resulting in a cost-saving intervention. Compared with the routine immunization budget, the total budget for typhoid vaccination would be 0.11%, 0.15%, 0.18%, 0.86%, 1.21% and 2.11%. To conclude, the nationwide typhoid vaccination in Indonesia is a cost-saving and affordable intervention since the required budget was only 2.11% of Indonesia’s total routine immunization budget.

## P4c344cefa6d9

- Year: 2001
- Linked people: Ben Van Hout
- Title: Clinical and Economic Impact of Diabetes Mellitus on Percutaneous and Surgical Treatment of Multivessel Coronary Disease Patients

Abstract:

BACKGROUND: Our aims were to compare coronary artery bypass grafting (CABG) and stenting for the treatment of diabetic patients with multivessel coronary disease enrolled in the Arterial Revascularization Therapy Study (ARTS) trial and to determine the costs of these 2 treatment strategies. METHODS AND RESULTS: Patients (n=1205) were randomly assigned to stent implantation (n=600; diabetic, 112) or CABG (n=605; diabetic, 96). Costs per patient were calculated as the product of each patient's use of resources and the corresponding unit costs. Baseline characteristics were similar between the groups. At 1 year, diabetic patients treated with stenting had the lowest event-free survival rate (63.4%) because of a higher incidence of repeat revascularization compared with both diabetic patients treated with CABG (84.4%, P<0.001) and nondiabetic patients treated with stents (76.2%, P=0.04). Conversely, diabetic and nondiabetic patients experienced similar 1-year event-free survival rates when treated with CABG (84.4% and 88.4%). The total 1-year costs for stenting and CABG in diabetic patients were $12 855 and $16 585 (P<0.001) and in the nondiabetic groups, $10 164 for stenting and $13 082 for surgery. CONCLUSIONS: Multivessel diabetic patients treated with stenting had a worse 1-year outcome than patients assigned to CABG or nondiabetics treated with stenting. The strategy of stenting was less costly than CABG, however, regardless of diabetic status.

## P8f2bc31ce40a

- Year: 2009
- Linked people: Gerard De Pouvourville
- Title: Étude Polychrome : Une méthode d'expertise pour optimiser des ordonnances de polyprescription en médecine générale

Abstract:

Résumé Objectif : Déterminer si un programme d’optimisation d’ordonnances de polyprescription par une équipe médicale multidisciplinaire permettrait d’améliorer la qualité des ordonnances. Méthodes : Sélection de 16 vignettes présentant chacune un patient différent avec son association de pathologies chroniques et ses prescriptions à partir d’une base de données issue de l’observatoire de la médecine générale. Analyse des prescriptions par une équipe de pharmacologues à l’aide du Vidal électronique, puis optimisation des prescriptions par une équipe multidisciplinaire de six médecins et d’un pharmacologue, en deux temps : une évaluation individuelle de leur caractère approprié à l’aide de la grille MAI (Medication appropriateness index) , puis une réunion du groupe d’experts avec des propositions de changement des prescriptions. Résultats : Parmi les 11 vignettes traitées au cours de la réunion de synthèse, la réduction du nombre de médicaments prescrits est de 29 %. Cette réduction est liée à un arrêt de prescription dans 2/3 des cas (soit une médiane de réduction de trois médicaments par ordonnance). L’effet de l’optimisation sur les contre-indications est une amélioration de 46 %, et sur les interactions médicamenteuses, une amélioration de 66 %. Les quatre causes principales de non optimisation (sur 11 proposées) sont : l’indication thérapeutique, l’efficacité, le dosage et la répartition sur 24 heures. Conclusion : Il s’agit d’une étude expérimentale, sur de véritables prescriptions de médecine générale, dont l’objectif était de montrer la possibilité théorique d’améliorer les ordonnances de polyprescription chronique. Les limites de ce travail sont l’incomplétude du dossier médical proposé aux experts, l’absence des arguments du prescripteur, et la quantité de travail nécessaire aux experts pour obtenir ce résultat. Prat Organ Soins 2009;40(3):167-175

## Pa06ed50f6556

- Year: 2025
- Linked people: Fredrick Purba
- Title: Comparisons of Preferences Toward EQ-5D-Y-3L Health States Between Adult Own and Child Perspectives

Abstract:

The international valuation protocol for EQ-5D-Y-3L recommends elicitation of utilities using adults' preference for a hypothetical 10-year-old child. Published studies have reported preference difference in adults when valuing for a child and valuing for themselves. This study aimed to obtain EQ-5D-Y-3L preferences in Hong Kong and understand the preference difference between the adult own perspective and the child perspective. We recruited 1000 and 200 adults in Hong Kong to value EQ-5D-Y-3L health states using discrete choice experiment and composite time trade-off (cTTO), respectively. Discrete choice experiment respondents were randomized to complete tasks from either adult own perspective or child perspective. cTTO respondents completed valuation from the child perspective. Relative attribute importance scores were compared between perspectives. Utility values were obtained by anchoring on the worst health state for both perspectives. Both perspectives had similar relative attribute importance scores, rankings of dimensions, rescaled coefficients, and elicited values. Rank order of 5 dimensions, from highest to lowest importance, was "having pain or discomfort," "doing usual activities," "feeling worried, sad, or unhappy," "mobility," and "looking after myself" for both perspectives. The most important and least important dimensions were consistent with published EQ-5D-Y-3L value sets. This study revealed no remarkable difference in the relative preference for EQ-5D-Y-3L health states between the adult own and child perspectives in Hong Kong, offering insights to the development of the EQ-5D-Y-5L valuation protocol. Future research may explore the effect of perspectives on preferences elicited by cTTO in Asia.

## P87313758ece1

- Year: 2018
- Linked people: Fredrick Purba
- Title: Quality of life and health status of Indonesian women with breast cancer symptoms before the definitive diagnosis: A comparison with Indonesian women in general

Abstract:

OBJECTIVES: Breast cancer (BC) is prevalent in low and middle-income countries (LMICs) where the majority of cases are diagnosed in late stages. The aims of this study were: (1) to assess quality of life (QOL) and health status of Indonesian women with BC symptoms before definitive diagnosis; (2) to compare QOL and health status between women with BC symptoms before definitive diagnosis and Indonesian women in general; (3) to evaluate the association between demographic variables (age, residence, social economic status and education level) and QOL within the Indonesian women with BC symptoms before definitive diagnosis. METHODS: We used WHOQOL-BREF to measure QOL and EQ-5D-5L for health status. Multivariate analysis of covariance (MANCOVA) was used to compare QOL and health status between women with BC symptoms and women from the general Indonesian population in order to control for confounders. Regression analyses were used for testing the association between the demographic variables, QOL, and health status. RESULTS: In comparison with the data from the women from the general population (n = 471), the women with BC symptoms (n = 132) reported lower QOL, especially in physical and psychological domains. They also reported more problems in all dimensions of health status. Higher education and monthly income were positively associated with QOL and health status among the women with BC symptoms. CONCLUSION: Before receiving a definitive diagnosis, women who visit hospitals with symptoms of BC, report a lower QOL and health status than women in general. Our results suggest that healthcare providers should provide targeted strategies for women with BC symptoms to improve their QOL.

## P33e2c0446f8e

- Year: 2025
- Linked people: Ciaran O'Neill
- Title: Investigating the long-term public health and co-benefit impacts of an urban greenway intervention in the UK: a natural experiment evaluation – study protocol

Abstract:

INTRODUCTION: Urban green and blue space (UGBS) interventions, such as the development of an urban greenway, have the potential to provide public health benefits and multiple co-benefits in the realms of the environment, economy and society. This paper presents the protocol for a 5-year follow-up evaluation of the public health benefits and co-benefits of an urban greenway in Belfast, UK. METHODS AND ANALYSIS: The natural experiment evaluation uses a range of systems-oriented and mixed-method approaches. First, using group model building methods, we codeveloped a causal loop diagram with stakeholders to inform the evaluation framework. We will use other systems methods including viable systems modelling and soft systems methodology to understand the context of the system (ie, the intervention) and the stakeholders involved in the development, implementation and maintenance phases. The effectiveness evaluation includes a repeat cross-sectional household survey with a random sample of 1200 local residents (adults aged ≥16 years old) who live within 1 mile of the greenway. The survey is complemented with administrative data from the National Health Service. For the household survey, outcomes include physical activity, mental well-being, quality of life, social capital, perceptions of environment and biodiversity. From the administrative data, outcomes include prescription medications for a range of non-communicable diseases such as cardiovascular disease, type II diabetes mellitus, chronic respiratory and mental health conditions. We also investigate changes in infectious disease rates, including COVID-19, and maternal and child health outcomes such as birth weight and gestational diabetes. A range of economic evaluation methods, including a cost-effectiveness analysis and social return on investment (SROI), will be employed. Findings from the household survey and administrative data analysis will be further explored in focus groups with a subsample of those who complete the household survey and the local community to explore possible mechanistic pathways and other impacts beyond those measured. Process evaluation methods include intercept surveys and direct observation of the number and type of greenway visitors using the Systems for Observing Play and Recreation in Communities tool. Finally, we will use methods such as weight of evidence, simulation and group model building, each embedding participatory engagement with stakeholders to help us interpret, triangulate and synthesise the findings. ETHICS AND DISSEMINATION: To our knowledge, this is one of the first natural experiments with a 5-year follow-up evaluation of an UGBS intervention. The findings will help inform future policy and practice on UGBS interventions intended to bring a range of public health benefits and co-benefits. Ethics approval was obtained from the Medicine, Health and Life Sciences Research Ethics Committee prior to the commencement of the study. All participants in the household survey and focus group workshops will provide written informed consent before taking part in the study. Findings will be reported to (1) participants and stakeholders; (2) funding bodies supporting the research; (3) local, regional and national governments to inform policy; (4) presented at local, national and international conferences and (5) disseminated by peer-review publications.

## P448cdf743747

- Year: 2021
- Linked people: Piyameth Dilokthornsakul
- Title: Mid- to long-term outcomes of contemporary total knee arthroplasty in Charcot neuroarthropathy: a systematic review and meta-analysis

Abstract:

Abstract Total knee arthroplasty (TKA) is an effective procedure to treat many patients with end-stage knee arthropathy. However, the extension of TKA for patients with Charcot neuroarthropathy (CNA) is controversial, with relatively limited evidence defining optimal reconstruction techniques. This systematic review of relevant studies that were published from January 2000 to June 2020 aimed to define survivorship, complications, reoperation, and component revision rates of contemporary TKA performed for CNA. We identified 127 TKA performed for CNA in five studies that comprised ≥ 7 knees with ≥ 5 years of follow-up. Overall implant survivorship was 85.4%. The overall complication rate was 26.4%, with the most common complications including instability (24.0%), periprosthetic fracture (17.4%), infection (13.0%), ligament injury (10.9%) and aseptic loosening (10.9%). The aetiology of CNA and prosthesis type had no influence on clinical outcomes, whereas the effect of staging of disease and ataxia status was still inconclusive. Understanding the potential determinants, survivorship and risk of complications related to TKA performed in CNA may help surgeons to deal with patient expectations. Cite this article: EFORT Open Rev 2021;6:556-564. DOI: 10.1302/2058-5241.6.200103

## P68d4e63216b4

- Year: 2002
- Linked people: Ciaran O'Neill
- Title: Addressing clinical governance in paediatric cochlear implantation

Abstract:

The protracted and multidisciplinary nature of paediatric cochlear implantation presents particular challenges in addressing issues of clinical governance. The implantation process is one that involves many disciplines in acute and community settings over several years. Reviews the difficulties presented by a protracted, multidisciplinary intervention for addressing issues of clinical governance within the context of paediatric cochlear implantation. Discusses the activities of the Nottingham Paediatric Cochlear Implant Programme in tackling these problems and gives some details of its progress and success in these areas.

## Pf19b6a946d16

- Year: 2022
- Linked people: Ciaran O'Neill
- Title: Implementation of a colorectal cancer screening intervention in Malaysia (CRC-SIM) in the context of a pandemic: study protocol

Abstract:

INTRODUCTION: Colorectal cancer (CRC) is the second most common cancer in Malaysia and cases are often detected late. Improving screening uptake is key in down-staging cancer and improving patient outcomes. The aim of this study is to develop, implement and evaluate an intervention to improve CRC screening uptake in Malaysia in the context of the COVID-19 pandemic. The evaluation will include ascertaining the budgetary impact of implementing and delivering the intervention. METHODS AND ANALYSIS: The implementation research logic model guided the development of the study and implementation outcome measures were informed by the 'Reach, Effectiveness, Adoption, Implementation and Maintenance' (RE-AIM) framework. This CRC screening intervention for Malaysia uses home-testing and digital, small media, communication to improve CRC screening uptake. A sample of 780 people aged 50-75 years living in Segamat district, Malaysia, will be selected randomly from the South East Asia Community Observatory (SEACO) database. Participants will receive a screening pack as well as a WhatsApp video of a local doctor to undertake a stool test safely and to send a photo of the test result to a confidential mobile number. SEACO staff will inform participants of their result. Quantitative data about follow-up clinic attendance, subsequent hospital tests and outcomes will be collected. Logistic regression will be used to investigate variables that influence screening completion and we will conduct a budget impact-analysis of the intervention and its implementation. Qualitative data about intervention implementation from the perspective of participants and stakeholders will be analysed thematically. ETHICS AND DISSEMINATION: Ethics approval has been granted by Monash University Human Research Ethics Committee (MUHREC ID: 29107) and the Medical Review and Ethics Committee (Reference: 21-02045-O7G(2)). Results will be disseminated through publications, conferences and community engagement activities. TRIAL REGISTRATION NUMBER: National Medical Research Register Malaysia: 21-02045-O7G(2).

## Pae9a1ef61183

- Year: 2016
- Linked people: Gerard De Pouvourville
- Title: CAPECO: Cost evaluation of community acquired pneumonia managed in primary care

Abstract:

Background Estimating the economic burden of community acquired pneumonia (CAP) managed in ambulatory setting is needed in France since no data are available. Method A retrospective study (CAPECO) was conducted based on a prospective French study describing patients with suspected CAP managed in primary care (CAPA). The aim of the CAPECO study was to estimate and explain medical costs of a disease episode in CAP patients only followed in ambulatory care and in hospitalised patients. Primary endpoints were the direct medical costs, impact on productivity and costs of incident CAP over one year. Secondary endpoint was to describe predictive factors of costs, hospital admission and stay length. Results In this cohort of 886 patients, resulting in an incidence of CAP of 400 per 100,000 inhabitants per year, the mean direct medical cost of a disease episode of CAP was € 118.8 for strictly ambulatory patients with an equal weight for medical time, drugs, diagnostic procedures and tests. This direct cost was € 102.1 before admission for patients who were finally hospitalised. The mean cost of hospital admissions was € 3522.9. Main predictive factors of hospital admission and stay length were respectively a history of chronic respiratory disease and older age. Factors of direct medical cost were prescribing X-ray examination and having a positive X-ray. The impact of a disease episode on productivity was € 1980 (sd 1400) per ambulatory episode and € 5425 (sd 4760) per episode leading to hospital admission. Conclusion Costs per ambulatory episode were modest but increased substantially in hospitalised patients, who were more numerous when chronic respiratory disorders were present and in the elderly. Indirect costs were significant. Deciders should thus consider both direct and indirect costs when assessing preventive interventions in the context of this disease.

## P0640f26e484e

- Year: 2024
- Linked people: Fredrick Purba
- Title: Validity, test-retest reliability, and responsiveness of the Indonesian version of FACIT-COST measure for subjective financial toxicity

Abstract:

BACKGROUND: Financial toxicity describes the impairment of financial wellbeing in patients due to the burden of cancer diagnosis and care. The COST: A Functional Assessment of Chronic Illness Therapy Measure of Financial Toxicity (FACIT-COST) is the most widely used cancer-specific measure of subjective financial toxicity, having been validated in multiple languages, but not in Indonesian. This study aimed to validate the Indonesian version of FACIT-COST in a breast cancer sample. METHODS: A single-center prospective cohort study was performed in Indonesia. Female breast cancer patients aged ≥ 18 undergoing treatment at baseline were invited to participate and followed for up to six months. The survey included the official Indonesian version of FACIT-COST (v2) which was administered to the patients by interviewers. Clinical information (e.g., metastasis status, disease duration) was provided based on medical records. The following measurement properties of FACIT-COST were tested: distributional characteristics, structural validity (principal component [PCA] and confirmatory factor analyses [CFA]), internal consistency reliability (Cronbach's alpha and McDonald's omega), known-groups validity (Mann-Whitney U or Kruskal-Wallis H test), test-retest reliability, and responsiveness to change. RESULTS: Overall, 300 female patients participated at baseline. No patients reported the best or worst possible FACIT-COST total scores. The PCA proposed a two-factor model structure for the instrument, which was confirmed by the CFA (RMSEA = 0.042, SRMR = 0.049, CFI = 0.99, TLI = 0.99). The internal consistency reliability of the two factors was considered adequate (Cronbach's alpha = 0.774-0.882, McDonald's omega = 0.786-0.888). The FACIT-COST total score significantly discriminated across the following known-groups: age, education, residential setting, income, employment, metastasis status, number of symptoms, and financial coping strategies. The FACIT-COST demonstrated excellent test-retest reliability (intraclass correlation coefficient = 0.96) and satisfactory responsiveness to change (standardized response mean and effect size ranges=|0.39| to |0.92|). CONCLUSIONS: This is the first study to validate the FACIT-COST in patients with breast cancer and to present the measurement properties of the Indonesian version of FACIT-COST. The Indonesian FACIT-COST demonstrates acceptable psychometric performance and shows potential as a valid measure of subjective financial toxicity. The instrument may serve as a valuable tool for informing health policies that focus on providing resource support to improve cancer care in Indonesia.

## Pad10a097038a

- Year: 2025
- Linked people: Gerard De Pouvourville
- Title: Real-world evidence to support health technology assessment and payer decision making: is it now or never?

Abstract:

OBJECTIVES: The aim of this policy article is twofold: (i) to provide a summary and update of recent important policy developments, in particular relevant guidance on the use of real-world data/real-world evidence (RWD/RWE) by health technology assessment (HTA) bodies and (ii) to set out our policy recommendations on how the different elements of an "RWE framework" we have previously developed could support, further enhance and facilitate the use of RWE for HTA purposes and by HTA bodies and payers. METHODS: We undertook a targeted review and analysis of recent important policy developments. The aim was to build on our recommendations from previous work on the "RWE Framework," and consider how the relevant tools from our Framework can further enhance and facilitate the use of RWE for HTA purposes and by HTA bodies/payers. RESULTS: We provide eight conditions that we argue would, in combination, constitute the optimal use and acceptance of RWD/RWE for HTA. We believe that, should the eight conditions hold, RWD/RWE would enable more efficient access to medicines and healthcare technologies for patients. CONCLUSIONS: High-quality, fit-for-purpose RWD/RWE can and should be used more frequently in HTA. Multi-stakeholder and cross-geography collaborative partnerships are needed to align on best practices to optimize the evidence that needs to be generated to satisfy all stakeholders' needs.

## P060e13fe92fe

- Year: 2023
- Linked people: Ben Van Hout, Elly Stolk
- Title: Using Age-Specific Values for Pediatric HRQoL in Cost-Effectiveness Analysis: Is There a Problem to Be Solved? If So, How?

Abstract:

Value sets for the EQ-5D-Y-3L published to date appear to have distinctive characteristics compared with value sets for corresponding adult instruments: in many cases, the value for the worst health state is higher and there are fewer values < 0. The aim of this paper is to consider how and why values for child and adult health differ; and what the implications of that are for the use of EQ-5D-Y-3L values in economic evaluations to inform healthcare resource allocation decisions. We posit four potential explanations for the differences in values: (a) The wording of severity labels may mean the worst problems on the EQ-5D-Y-3L are descriptively less severe than those on the EQ-5D-5L; (b) Adults may genuinely consider that children are less badly affected than adults by descriptively similar health issues. That is, for any given health problem, adult respondents in valuation studies consider children's overall health-related quality of life (HRQoL) on average to be higher than that for adults; (c) Values are being sought by eliciting adults' stated preferences for HRQoL in another person, rather than in themselves (regardless of whether the 'other person' concerned is a child); and (d) The need to elicit preferences for child HRQoL that are anchored at dead = 0 invokes special considerations regarding children's survival. Existing evidence does not rule out the possibility that (c) and (d) exert an upward bias in values. We consider the implications of that for the interpretation and use of values for pediatric HRQoL. Alternative methods for valuing children's HRQoL in a manner that is not 'age specific' are possible and may help to avoid issues of non-comparability. Use of these methods would place the onus on health technology assessment bodies to reflect any special considerations regarding child quality-adjusted life-year gains.

## P142ea3b82df7

- Year: 2010
- Linked people: Ciaran O'Neill
- Title: 073 Variations in the use of publicly funded oral care in Northern Ireland: results from an analysis of adolescents in the Northern Ireland Longitudinal Study

Abstract:

Background A socio-economic gradient in use of health care has been observed in a number of situations. These have been used to assess the performance of systems as well as frame discussion on system design. Examination of patterns at an aggregate level may mask important differences between types of care that could lead to different policy advice. Aims To identify whether differences in registration and use related to socio-demographic characteristics exist in respect of publicly funded oral health care in Northern Ireland and if so to identify the nature of differences in care. Methods NHS reimbursement data were linked to census and vital statistics data within the Northern Ireland Longitudinal Study. Data cover 28% of the population in Northern Ireland and in this study cover a period from 2003 to 2008. Data for individuals aged 11 or 12 in April 2003 that include registration status, reimbursement on a per item basis, gender, community background, siblings and also the social class and education of household reference person (HRP) were extracted. A series of multivariate analyses were used to examine the relationship between registration and use of care as a function of socio-demographic characteristics. Results A clear socio-economic gradient was evident in respect of registration status. Adolescents whose HRP was long term unemployed or never worked were registered for 6 months (from a maximum of 54) less and consumed 8.3% less expenditure than those whose HRP was professional. While those from lower social backgrounds consumed 24.4% less expenditure on orthodontic services, with respect to extractions and conservative treatment, adolescents whose HRP was long term unemployed or never worked consumed 35.6% and 25.8%, respectively, more expenditure than those whose HRP was professional, other variables controlled for. Conclusions A publicly funded demand led service can produce a pattern of service provision that disproportionately reflects the preferences of the affluent at the expense of the needs of the less affluent. This might be masked by analysis of data at an aggregate level. The pattern of service provision that results may from a societal perspective be neither efficient (cost effective) nor equitable. The disaggregated analysis of registration and utilisation patterns in this study highlights the potential for such distortion where public funds support demand led provision by for profit providers.

## P957118f6e6d6

- Year: 2015
- Linked people: Piyameth Dilokthornsakul
- Title: Databases in the Asia-pacific region: The potential for a distributed network approach

Abstract:

BACKGROUND: This study describes the availability and characteristics of databases in Asian-Pacific countries and assesses the feasibility of a distributed network approach in the region. METHODS: A web-based survey was conducted among investigators using healthcare databases in the Asia-Pacific countries. Potential survey participants were identified through the Asian Pharmacoepidemiology Network. RESULTS: Investigators from a total of 11 databases participated in the survey. Database sources included four nationwide claims databases from Japan, South Korea, and Taiwan; two nationwide electronic health records from Hong Kong and Singapore; a regional electronic health record from western China; two electronic health records from Thailand; and cancer and stroke registries from Taiwan. CONCLUSIONS: We identified 11 databases with capabilities for distributed network approaches. Many country-specific coding systems and terminologies have been already converted to international coding systems. The harmonization of health expenditure data is a major obstacle for future investigations attempting to evaluate issues related to medical costs.

## P9439f6a84eb1

- Year: 2020
- Linked people: Ciaran O'Neill
- Title: Developing composite indices of geographical access and need for nursing home care in Ireland using multiple criteria decision analysis

Abstract:

Background: Spatial accessibility has consistently been shown to influence utilisation of care and health outcomes, compared against local population needs. We sought to identify how appropriately nursing homes (NHs) are distributed in Ireland, as its NH market lacks central planning. Methods: We used multiple criteria decision analysis (MCDA) approaches to develop composite indices of both access (incorporating measures of availability, choice, quality and affordability) and local NH need for over 65s (relating to the proportion living alone, with cognitive disabilities or with low self-rated health, estimated scores for activities of daily living and instrumental activities of daily living, the average number of disabilities per person and the average age of this group). Data for need were derived from census data. Results were mapped to better understand underlying geographical patterns. Results: By comparing local accessibility and need, underserved areas could be identified, which were clustered particularly in the country’s northwest. Suburbs, particularly around Dublin, were by this measure relatively overserved. Conclusions: We have developed multi-dimensional indices of both accessibility to, and need for, nursing home care. This was carried out by combining granular, open data sources and elicited expert/stakeholder opinion from practitioners. Mapping these data helped to highlight clear evidence of inequitable variation in nursing home distribution.

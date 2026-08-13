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

## P194d15e1ded5

- Year: 2025
- Linked people: Fredrick Purba
- Title: Health belief model of parents’ COVID-19 vaccination intentions for children: perceived benefits and barriers in Indonesia

Abstract:

Introduction: The uptake of vaccines against COVID-19 remains low. Some barriers to childhood vaccination uptake persist, such as parents' assumption that children are at lower risk of severe COVID-19 and tend to be asymptomatic carriers. This study aims to develop guidance for in-depth interviews for a future qualitative study based on a cross-sectional quantitative study of parents with school-age children. Methods: This study adopted a cross-sectional design. The study population comprised parents of 6-11-year-old children in the Centra Java province who had received the COVID-19 vaccine or not. The data were collected from August 2023 by filling in an online questionnaire. The sample size was calculated using formulation in OpenEpi for 95% confidence levels, with a statistical power of 80%. Results: Our study finds that perceived benefit and perceived barriers are the two domains that most significantly influenced the parents' intention to vaccinate their children. In our study, there was no significant association between parent gender and the intention to vaccinate their children. Our study shows that parents' acceptance of vaccinating their children is high. We emphasized questions related to benefits and barriers in the interview. The questions on perceived benefits explored the advantages of COVID-19 vaccination. The content on perceived barriers examined the concerns of parents, the information influencing their decision to vaccinate their child, the procedure vaccination and the effect after vaccination. Discussion: The significant association between parents' intention to vaccinate their children and the perceived benefits and perceived barriers to vaccination generated guidance for in-depth interviews in the qualitative study. The health belief model should be further explored in Indonesia because of the potential external factors that may influence parents' intention to vaccinate their children.

## P400a9a39db25

- Year: 2019
- Linked people: Piyameth Dilokthornsakul
- Title: Incorporating adherence in cost-effectiveness analyses of asthma: a systematic review

Abstract:

Aims: Non-adherence is associated with poor clinical outcomes among patients with asthma. While cost-effectiveness analysis (CEA) is increasingly used to inform value assessment of the interventions, most do not take into account adherence in the analyses. This study aims to: (1) Understand the extent of studies considering adherence as part of the economic analyses, and (2) summarize the methods of incorporating adherence in the economic models.Materials and methods: A literature search was performed from the inception to February 2018 using four databases: PubMed, EMBASE, NHS EED, and the Tufts CEA registry. Decision model-based CEA of asthma were identified. Outcomes of interest were the number of studies incorporating adherence in the economic models, and the incorporating methods. All data were extracted using a standardized data collection form.Results: From 1,587 articles, 23 studies were decision model-based CEA of asthma, of which four CEA (17.4%) incorporated adherence in the analyses. Only the method of incorporating adherence by adjusting treatment effectiveness according to adherence levels was demonstrated in this review. Two approaches were used to derive the associations between adherence and effectiveness. The first approach was to apply a mathematical formula, developed by an expert panel, and the second was to extrapolate the associations from previous published studies. The adherence-adjusted effectiveness was then incorporated in the economic models.Conclusions: A very low number of CEA of asthma incorporated adherence in the analyses. All the CEA adjusted treatment effectiveness according to adherence levels, applied to the economic models.

## P5adb70ae1f53

- Year: 2014
- Linked people: Ben Van Hout
- Title: A Comparison of Methods for Converting DCE Values onto the Full Health-Dead QALY Scale

Abstract:

BACKGROUND: Preference elicitation techniques such as time trade-off (TTO) and standard gamble (SG) receive criticism for their complexity and difficulties of use. Ordinal techniques such as discrete choice experiment (DCE) are arguably easier to understand but generate values that are not anchored onto the full health-dead 1-0 quality-adjusted life-year (QALY) scale required for use in economic evaluation. METHODS: This article compares existing methods for converting modeled DCE latent values onto the full health-dead QALY scale: 1) anchoring DCE values using dead as valued in the DCE and 2) anchoring DCE values using TTO value for worst state to 2 new methods: 3) mapping DCE values onto TTO and 4) combining DCE and TTO data in a hybrid model. Models are compared using their ability to predict mean TTO health state values. DATA: We use postal DCE data (n = 263) and TTO data (n = 307) collected by interview in a general population valuation study of an asthma condition-specific measure (AQL-5D). RESULTS: New methods 3 and 4 using mapping and hybrid models are better able to predict mean TTO health state values (mean absolute difference [MAD], 0.052-0.084) than the anchor-based methods (MAD, 0.075-0.093) and were better able to predict mean TTO health state values even when using in their estimation a subsample of the available TTO data. CONCLUSIONS: These new mapping and hybrid methods have a potentially useful role for producing values on the QALY scale from data elicited using ordinal techniques such as DCE for use in economic evaluation that makes best use of the desirable properties of each elicitation technique and elicited data. Further research is encouraged.

## Ped09f2dc0688

- Year: 2024
- Linked people: Ben Van Hout
- Title: 691 - Understanding patient and physician preferences when choosing between biologic and oral systemic treatment options for moderate-to-severe atopic dermatitis: a discrete choice experiment

Abstract:

Abstract Background A growing number of treatment options are becoming available for moderate-to-severe atopic dermatitis (AD), including biologic therapies. As these treatments have different efficacy, safety, and tolerability profiles, it is important to understand patient and physician preferences for informed treatment decision making. Objective To discover the importance of different attributes, including efficacy, safety, and mode of administration, and to provide insights into whether patient preferences concur or conflict with those of physicians. Methods We conducted a cross-sectional, online discrete choice experiment involving 306 patients with AD and 206 physicians in the UK and Germany. Qualitative interviews identified key attributes influencing treatment preferences, including efficacy (itch relief, sleep disturbance, time-to-itch relief, and total body surface area affected by eczema), safety (special warnings and risks of eye problems and shingles), and treatment administration. Data were analyzed using a random parameters logit model to calculate the conditional relative importance of each attribute. Results Both groups placed significant emphasis on efficacy, with reducing sleep disturbance ranking first for patients and second for physicians and itch ranking first for physicians and second for patients. Time to itch relief was the third most important efficacy attribute for both groups, although it was more important for patients. For both groups, the risk of eye problems was the most important safety concern. The mode of administration was not considered of great importance when compared with efficacy and safety attributes. Conclusions Our findings suggest patients prioritize sleep disturbance, an attribute not captured in other preference studies in AD, and itch. This emphasizes the importance of addressing sleep-related issues and itching to enhance patients’ well-being. The findings offer insights for prioritization strategies among healthcare providers, aiming to improve patient outcomes amidst a growing number of AD treatments.

## P31ff012c0beb

- Year: 2024
- Linked people: Fredrick Purba
- Title: Content validity of the EQ-HWB and EQ-HWB-S in a sample of Italian patients, informal caregivers and members of the general public

Abstract:

BACKGROUND: The EuroQol Group recently developed two new instruments, the EQ Health and Wellbeing (EQ-HWB) and the EQ Health and Wellbeing short version (EQ-HWB-S). The EQ-HWB and EQ-HWB-S are intended to capture a broad range of health and broader quality of life aspects, which may be relevant to general public members, patients, their families, social care users and informal carers. This study assesses the content validity of the Italian version of the two instruments in a sample of Italian patients, social care users and informal carers. METHODS: Participants were recruited using a convenience sampling approach. One-on-one interviews were carried out using video-conferencing interviews. A semi-structured topic guide was used to guide the interview procedures, with open-ended questions supplemented by probes. Participants were asked to explain important aspects of their health and quality of life, to complete the questionnaires and verbalize their thoughts. RESULTS: Twenty participants comprising of patients (n = 9), informal carers (n = 6), and members of the general public (n = 5) participated to the study. Content validity was summarized into six main themes: comprehension, interpretation, acceptability, relevance, response options and recall period. All participants found the instruments easy or quite easy to understand and to respond to. Items were relevant for all three groups of participants, and response options appropriate. CONCLUSIONS: The Italian version of the EQ-HWB showed content validity in measuring health and wellbeing in a mixed Italian population.

## P9cab91ca50fd

- Year: 2025
- Linked people: Fredrick Purba
- Title: Initial comparison of psychometric properties of the Japanese Parenting Style Scale (JPSS) in Indonesia and Japan

Abstract:

Parenting style is crucial in shaping children's development, particularly during early childhood. Therefore, this study aims to investigate the psychometric properties of the Japanese Parenting Style Scale (JPSS) and its applicability in cross-cultural contexts, specifically among Indonesian and Japanese mothers. JPSS, comprising four dimensions, namely warmth, hostility, permissiveness, and harsh control, was administered to 1095 female participants across the countries. Using Rasch analysis with the Rating Scale Model (RSM), key measurement assumptions, including unidimensionality, local independence, monotonicity, and differential item functioning (DIF) were examined. The results confirmed the unidimensionality and local independence of all subscales. Item and person statistics met acceptable thresholds, and reliability, as well as separation indices, ranged from good to excellent. However, some disparities in rating scale functionality were observed between the two cultural groups, with Indonesian participants showing a tendency to select extreme response options. DIF analysis identified cross-cultural differences in item functioning, particularly in warmth and harsh control subscales. These results affirm the importance of cultural adaptation when applying parenting measurement tools developed across diverse contexts. JPSS shows robust psychometric properties, but cultural nuances need to be considered for accurate interpretation and use in diverse populations.

## Pbe9b7dc732f5

- Year: 2017
- Linked people: Piyameth Dilokthornsakul
- Title: Economic Evaluation and Budget Impact Analysis of Vaccination against Haemophilus influenzae Type b Infection in Thailand

Abstract:

Current study aimed to estimate clinical and economic outcomes of providing the Haemophilus influenzae type b (Hib) vaccination as a national vaccine immunization program in Thailand. A decision tree combined with Markov model was developed to simulate relevant costs and health outcomes covering lifetime horizon in societal and health care payer perspectives. This analysis considered children aged under 5 years old whom preventive vaccine of Hib infection are indicated. Two combined Hib vaccination schedules were considered: three-dose series (3 + 0) and three-dose series plus a booster does (3 + 1) compared with no vaccination. Budget impact analysis was also performed under Thai government perspective. The outcomes were reported as Hib-infected cases averted and incremental cost-effectiveness ratios (ICERs) in 2014 Thai baht (THB) ($) per quality-adjusted life year (QALY) gained. In base-case scenario, the model estimates that 3,960 infected cases, 59 disability cases, and 97 deaths can be prevented by national Hib vaccination program. The ICER for 3 + 0 schedule was THB 1,099 ($34) per QALY gained under societal perspective. The model was sensitive to pneumonia incidence among aged under 5 years old and direct non-medical care cost per episode of Hib pneumonia. Hib vaccination is very cost-effective in the Thai context. The budget impact analysis showed that Thai government needed to invest an additional budget of 110 ($3.4) million to implement Hib vaccination program. Policy makers should consider our findings for adopting this vaccine into national immunization program.

## Pdbef0c2452ff

- Year: 2022
- Linked people: Ciaran O'Neill
- Title: Explaining spatial accessibility to high-quality nursing home care in the US using machine learning

Abstract:

In this study we measure and map the system-wide spatial accessibility to good quality nursing home care for all counties in the contiguous United States, and use an 'imputed post-lasso' machine learning technique to systematically examine this accessibility measure's associations with a broad range of county-level socio-demographic variables. Both steps were carried out using publicly available datasets. Analyses found clear evidence of spatial patterning in accessibility, particularly by population density, state and the populations of specific racial minorities. This has implications for outcomes that extend beyond the care homes and we highlight a number of policy measures that may help to address these shortcomings. The 'out-of-sample' predictive performance of the machine learning approach highlights the method's usefulness in identifying systematic differences in accessibility to services.

## P319a919037f5

- Year: 2019
- Linked people: Philip Powell
- Title: Producing a preference-based quality of life measure for people with Duchenne muscular dystrophy: a mixed-methods study protocol

Abstract:

INTRODUCTION: Preference-based measures (PBMs) of health-related quality of life (HRQoL) are used to generate quality-adjusted life years, which are necessary for cost-effectiveness evaluations of health interventions via cost-utility analysis. These measures of health can be generic (ie, pandiagnostic) or condition specific. No condition-specific PBM of HRQoL in Duchenne muscular dystrophy (DMD) exists, yet there are concerns that standard generic measures lack the specificity to assess aspects of HRQoL that are especially important to people with DMD. This study has been designed to produce a condition-specific PBM of HRQoL in DMD. METHODS AND ANALYSIS: This mixed-methods study proceeds through three stages. In the first stage (concept elicitation), semistructured interviews will be conducted with boys and men diagnosed with DMD, and analysed with framework to produce a draft health state descriptive system for HRQoL in DMD. In the second stage (refining the descriptive system), patients, clinicians and primary caregivers of people with DMD will assess the face validity of the descriptive system. This will be followed by a quantitative survey on a larger sample of patients, which will be analysed with psychometric analyses to produce a refined descriptive system. In the third stage (valuation and econometric modelling), an online discrete choice experiment with duration will be administered to a general public sample to generate utility values for the new measure. ETHICS AND DISSEMINATION: This study has received ethical approval from the National Health Service (REC reference: 18/SW/0055). The primary output of this research will be a condition-specific PBM (or 'bolt-on' to an existing generic PBM) in people with DMD and an associated value set. Results will be disseminated through international conferences and open-access journals.

## P595e0df3a2cf

- Year: 2021
- Linked people: Ciaran O'Neill
- Title: An Exploration on Attribute Non-attendance Using Discrete Choice Experiment Data from the Irish EQ-5D-5L National Valuation Study

Abstract:

BACKGROUND: Generic measures of health-related quality of life (HRQoL) permit comparisons of competing demands for healthcare resources using outcomes that reflect the preferences of tax payers. EQ-5D instruments are the most commonly used generic, preference-based measures of HRQoL. The EQ-5D-5L enables respondents to describe their health state using five dimensions of health, each with five response levels. The standardised protocol for the valuation of EQ-5D-5L health states comprises use of the composite time trade-off valuation technique, supplemented by a discrete choice experiment (DCE). OBJECTIVE: This paper presents the first exploration on attribute non-attendance (ANA) to the dimensions of the EQ-5D-5L using DCE data collected following the standardised protocol. METHOD: This paper uses the equality constrained latent class model and the endogenous attribute attendance model to examine ANA to the dimensions of the EQ-5D-5L. RESULTS: The results suggest that respondents are less likely to consider the physical dimensions of the EQ-5D-5L (such as self-care and usual activities) when evaluating the health states. The effects of ANA on utility scores depends on the interpretation of the underlying reasons for ANA. CONCLUSIONS: We recommend that future value sets based in whole or in part on DCE data examine the impact of and reasons for non-attendance in national valuation studies.

## Pd40392956b2d

- Year: 2013
- Linked people: Ciaran O'Neill
- Title: ATLANTIC DIP: simplifying the follow-up of women with previous gestational diabetes

Abstract:

OBJECTIVE: Previous gestational diabetes (GDM) is associated with a significant lifetime risk of type 2 diabetes. In this study, we assessed the performance of HbA1c and fasting plasma glucose (FPG) measurements against that of 75 g oral glucose tolerance testing (OGTT) for the follow-up screening of women with previous GDM. METHODS: Two hundred and sixty-six women with previous GDM underwent the follow-up testing (mean of 2.6 years (s.d. 1.0) post-index pregnancy) using HbA1c (100%), and 75 g OGTT (89%) or FPG (11%). American Diabetes Association (ADA) criteria for abnormal glucose tolerance were used. DESIGN, COHORT STUDY, AND RESULTS: The ADA HbA1c high-risk cut-off of 39 mmol/mol yielded sensitivity of 45% (95% CI 32, 59), specificity of 84% (95% CI 78, 88), negative predictive value (NPV) of 87% (95% CI 82, 91) and positive predictive value (PPV) of 39% (95% CI 27, 52) for detecting abnormal glucose tolerance. ADA high-risk criterion for FPG of 5.6 mmol/l showed sensitivity of 80% (95% CI 66, 89), specificity of 100% (95% CI 98, 100), NPV of 96% (95% CI 92, 98) and PPV of 100% (95% CI 91, 100). Combining HbA1c ≥39 mmol/mol with FPG ≥5.6 mmol/l yielded sensitivity of 90% (95% CI 78, 96), specificity of 84% (95% CI 78, 88), NPV of 97% (95% CI 94, 99) and PPV of 56% (95% CI 45, 66). CONCLUSIONS: Combining test cut-offs of 5.6 mmol/l and HbA1c 39 mmol/mol identifies 90% of women with abnormal glucose tolerance post-GDM (mean 2.6 years (s.d.1.0) post-index pregnancy). Applying this follow-up strategy will reduce the number of OGTT tests required by 70%, will be more convenient for women and their practitioners, and is likely to lead to increased uptake of long-term retesting by these women whose risk for type 2 diabetes is substantially increased.

## Pd7ce056308c8

- Year: 2018
- Linked people: Piyameth Dilokthornsakul
- Title: The protective effect of lycopene-rich products on skin photodamage: A systematic review and meta-analysis of randomized controlled trials

Abstract:

Background: Ultraviolet (UV) radiation has known as a major cause of photodamage, photoaging and skin cancer as it involves in reactive oxygen species generation. Several natural antioxidants including lycopene has been suggested for photoprotection. How.

## Pc77ab47251bf

- Year: 1995
- Linked people: Gerard De Pouvourville
- Title: Information médicale et régulation de la médecine générale : une approche comparative

Abstract:

Medical Information and Regulation of General Practice Medicine : A Comparative Approach Most industrialised countries recently came to realise that an efficient regulation of health care services was no longer possible without an evaluation of the precise content of medical activity, particularly through the gathering of medical data. A comparative analysis has been carried out conceming the measures for controlling medical practices in the non-hospital sector in three countries : Germany, the United Kingdom and the United States of America. The study shows that the question of control over medical practices has arisen very differently in these three countries and that the response to this question depends upon the general organisation of the System of health care and particularly the mechanisms of macro-economic regulation of health expenditure as well as the mechanisms of micro-economic regulation of the medical profession.

## P13a50c7a151d

- Year: 2018
- Linked people: Ben Van Hout
- Title: Comparing the UK EQ-5D-3L and English EQ-5D-5L Value Sets

Abstract:

BACKGROUND: Three EQ-5D value sets (EQ-5D-3L, crosswalk, and EQ-5D-5L) are now available for cost-utility analysis in the UK and/or England. The value sets' characteristics differ, and it is important to assess the implications of these differences. OBJECTIVE: The aim of this paper is to compare the three value sets. METHODS: We carried out analysis comparing the predicted values from each value set, and investigated how differences in health on the descriptive system is reflected in the utility score by assessing the value of adjacent states. We also assessed differences in values using data from patients who completed both EQ-5D-3L and EQ-5D-5L. RESULTS: The distribution of the value sets systematically differed. EQ-5D-5L values were higher than EQ-5D-3L/crosswalk values. The overall range and difference between adjacent states was smaller. In the patient data, the EQ-5D-5L produced higher values across all conditions and there was some evidence that the value sets rank different health conditions in a similar severity order. CONCLUSIONS: There are important differences between the value sets. Due to the smaller range of EQ-5D-5L values, the possible change in quality-adjusted life years (QALYs) might be reduced, but they will apply to both control and intervention groups, and will depend on whether the gain is in quality of life, survival, or both. The increased sensitivity of EQ-5D-5L may also favour QALY gains even if the changes in utility are smaller. Further work should assess the impact of the different value sets on cost effectiveness by repeating the analysis on clinical trial data.

## Pa494ae4c9bea

- Year: 2025
- Linked people: Ciaran O'Neill
- Title: Improving the Oral Health of Older People in Care Homes: Results From a Randomised Feasibility Study

Abstract:

OBJECTIVES: Poor oral health is a considerable burden for older adults in care homes. The National Institute for Health and Care Excellence (NICE) issued guideline NG48 on "Improving oral health in care homes". However, empirical evidence for oral health interventions among care home residents is weak, and the feasibility of the NG48 recommended interventions is not established. This study aimed to determine the feasibility of delivering a co-designed oral health intervention, based on NG48 recommendations, in care homes in two sites in the UK. METHODS: This was a pragmatic cluster randomised controlled feasibility study with a 12-month follow-up, undertaken in 22 care homes across two sites (11 each in London and Northern Ireland). Care homes were randomised to an intervention arm (n = 11), and a control arm (n = 11) that continued with usual routine practice. The complex intervention contained materials were co-designed with care home staff and consisted of: care home staff training package; Oral Health Assessment Tool (OHAT) administered by trained care home staff; and a support worker assisted twice daily tooth-brushing regimen with 1500 ppm fluoride toothpaste. Rates of recruitment and retention, data completion, and intervention fidelity were recorded to determine feasibility. RESULTS: One-hundred-and-nineteen residents from 22 care homes were recruited and 82 residents from 19 care homes completed the study (retention: 86% for care homes and 69% for residents). Twenty residents were lost to follow-up and another 17 withdrew throughout the study. Data completion rates ranged between 88% and 97% at baseline and between 91% and 96% at the 12-month follow-up. Intervention fidelity records showed high completion rates for oral care plans (90%), and lower rates for weekly oral hygiene records (73%) and the OHAT (61%). CONCLUSIONS: This study documented the feasibility of an oral health intervention in care homes, while also highlighting issues to consider for a definitive trial to assess the effectiveness of the co-designed intervention. TRIAL REGISTRATION: Clinical Trial Registration: ISRCTN10276613.

## Pcfb895e0b381

- Year: 1999
- Linked people: Ben Van Hout
- Title: The ARTS study (Arterial Revascularization Therapies Study).

Abstract:

The rising costs of health care have forced policy makers to make choices, and new treatments are increasingly assessed in terms of the balance between additional costs and additional effects. The recent recognition that stenting has a major and long-lasting effect enhancing balloon PTCA procedure has made it imperative to compare in patients with multivessel disease the standard surgical procedure with multiple stenting in a large scale multinational and multicentre approach (19 countries, 68 sites). Selection and inclusion of patients is based on a consensus of the cardiac surgeon and interventional cardiologist on equal 'treatability' of patients by both techniques with analysis of clinical follow-up (event-free survival) on the short (30 day), medium (1 year), and long-term (3 and 5 year) with analysis of cost-effectiveness and quality of life (EuroQol and SF-36). Of the entire trial, the primary null hypothesis which needs to be rejected is that there will be no difference in event-free survival or effectiveness (E), at 1 year and also that the direct and indirect costs (C) per event-free year are not different between surgery or stenting. For this to become significant with a power of 90% one needs 1200 patients. Between April 97 and June 98, 1205 patients have been randomized with a monthly recruitment of 83 patients. Expected costs, effects and cost-effectiveness ratio (CE ratio) are: Stent high costs 2 VDStent high costs 3 VDStent low costs 2 VDStent low costs 3 VDCABG costs (C)$19.297$24.566$16.638$20.456$21.350 effects (E)81%81%81%81%88% CE ratio$23.876$30.397$20.586$25.322$24.348 Clinically, stenting is not expected to be more effective than CABG, but should be cost effective in both the 2- and 3-VD group when using the lower cost estimate and in the 2 VD group when using the higher cost assumptions.

## P5e758f731736

- Year: 2023
- Linked people: Elly Stolk, Fredrick Purba
- Title: Evaluation of EuroQol Valuation Technology (EQ-VT) Designs to Generate National Value Sets: Learnings from the Development of an EQ-5D Value Set for India Using an Extended Design (DEVINE) Study.

Abstract:

INTRODUCTION: Countries develop their EQ-5D-5L value sets using the EuroQol Valuation Technology (EQ-VT) protocol. This study aims to assess if extension in the conventional EQ-VT design can lead to development of value sets with improved precision. METHODS: A cross-sectional survey was undertaken in a representative sample of 3,548 adult respondents, selected from 5 different states of India using a multistage stratified random sampling technique. A novel extended EQ-VT design was created that included 18 blocks of 10 health states, comprising 150 unique health states and 135 observations per health state. In addition to the standard EQ-VT design, which is based on 86 health states and 100 observations per health state, 3 extended designs were assessed for their predictive performance. The extended designs were created by 1) increasing the number of observations per health state in the design, 2) increasing the number of health states in the design, and 3) implementing both 1) and 2) at the same time. Subsamples of the data set were created for separate designs. The root mean squared error (RMSE) and mean absolute error (MAE) were used to measure the predictive accuracy of the conventional and extended designs. RESULTS: The average RMSE and MAE for the standard EQ-VT design were 0.055 and 0.041, respectively, for the 150 health states. All 3 types of design extensions showed lower RMSE and MAE values as compared with the standard design and hence yielded better predictive performance. RMSE and MAE were lowest (0.051 and 0.039, respectively) for the designs that use a greater number of health states. Extending the design with inclusion of more health states was shown to improve the predictive performance even when the sample size was fixed at 1,000. CONCLUSION: Although the standard EQ-VT design performs well, its prediction accuracy can be further improved by extending its design. The addition of more health states in EQ-VT is more beneficial than increasing the number of observations per health state. HIGHLIGHTS: The EQ-5D-5L value sets are developed using the standardized EuroQol Valuation Technology (EQ-VT) protocol. This is the first study to empirically assess how much can be gained from extending the standard EQ-VT design in terms of sample size and/or health states. It not only presents useful insights into the performance of the standard design of the EQ-VT but also tests the potential extensions in the standard EQ-VT design in terms of increasing the health states to be directly valued as well as the number of observations recorded to predict the utility value of each of these health states.The study demonstrates that the standard EQ-VT design performs good, and an extension in the design of the standard EQ-VT can lead to further improvement in its performance. The addition of more health states in EQ-VT is more beneficial than increasing the number of observations per health state. Extending the design with inclusion of more health states marginally improves the predictive performance even when the sample size was fixed at 1,000.The findings of the study will streamline the systematic process for generating precise EQ-5D-5L value sets, thus facilitating the conduct of credible, transparent, and robust outcome valuation in health technology assessments.

## P197b91cd88a6

- Year: 2022
- Linked people: Piyameth Dilokthornsakul
- Title: Determinants of COVID-19 self-protection behavior of Thai people: a cross-sectional survey

Abstract:

Coronavirus disease 2019 (COVID-19) is firstly discovered in China since December 2019 and the pandemic of COVID-19 has been rapidly occurred and recognized as the important global health problem in 2020 1-2 . Most infected people develops mild to moderate respiratory symptoms including fever, dry cough, headache, sore throat, and weakness 3-4 . However, serious acute respiratory distress syndrome and multiple organ failures could develop especially in elderly who have medical conditions such as cancer, chronic kidney disease, diabetes mellitus and cardiovascular disease 5 .

## P139d8058a935

- Year: 2019
- Linked people: Ciaran O'Neill
- Title: Direct healthcare costs of sedentary behaviour in the UK

Abstract:

BACKGROUND: Growing evidence indicates that prolonged sedentary behaviour increases the risk of several chronic health conditions and all-cause mortality. Sedentary behaviour is prevalent among adults in the UK. Quantifying the costs associated with sedentary behaviour is an important step in the development of public health policy. METHODS: National Health Service (NHS) costs associated with prolonged sedentary behaviour (≥6 hours/day) were estimated over a 1-year period in 2016-2017 costs. We calculated a population attributable fraction (PAF) for five health outcomes (type 2 diabetes, cardiovascular disease [CVD], colon cancer, endometrial cancer and lung cancer). Adjustments were made for potential double-counting due to comorbidities. We also calculated the avoidable deaths due to prolonged sedentary behaviour using the PAF for all-cause mortality. RESULTS: The total NHS costs attributable to prolonged sedentary behaviour in the UK in 2016-2017 were £0.8 billion, which included expenditure on CVD (£424 million), type 2 diabetes (£281 million), colon cancer (£30 million), lung cancer (£19 million) and endometrial cancer (£7 million). After adjustment for potential double-counting, the estimated total was £0.7 billion. If prolonged sedentary behaviour was eliminated, 69 276 UK deaths might have been avoided in 2016. CONCLUSIONS: In this conservative estimate of direct healthcare costs, prolonged sedentary behaviour causes a considerable burden to the NHS in the UK. This estimate may be used by decision makers when prioritising healthcare resources and investing in preventative public health programmes.

## P8ece1bb2377a

- Year: 2012
- Linked people: Ben Van Hout
- Title: Quality of Life After PCI With Drug-Eluting Stents in Coronary Artery Bypass Surgery

Abstract:

Cohen, David J.; Van Hout, Ben; Serruys, Patrick W.; Mohr, Friedrich W.; Macaya, Carlos; Den Heijer, Peter; Vrakking, M.M.; Wang, Kaijun; Mahoney, Elizabeth M.; Audi, Salma; Leadley, Katrin; Dawkins, Keith D.; Kappetein, A. Pieter for the Synergy Between PCI With Taxus and Cardiac Surgery (SYNTAX) Investigators Author Information

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

## Pea6dd44cb509

- Year: 2025
- Linked people: Maureen Rutten-van Molken
- Title: Characterizing a heterogeneous chronic patient population for redesigning person-centred bundled payment models using risk-mitigating measures

Abstract:

Since 2010, most Dutch patients with diabetes mellitus type 2 (DM2), an increased risk of cardiovascular diseases (CVR), and chronic obstructive pulmonary disease (COPD), have been treated in single-disease management programs (SDMPs) provided by primary care cooperatives (PCCs). These SDMPs are funded through bundled payments. However, given the prevalence of multimorbidity among patients, there is a growing need for care that is more person-centred. We have previously published an alternative payment model that stimulates the integration of care required for a person-centred approach and in this paper, we demonstrate an operationalization of this model. We performed cluster analysis on claims data to distinguish between different subgroups of patients, predicted cluster probabilities with data available to general practitioners, designed different care packages and investigated the expected financial risk for PCCs of different sizes. We showed that mainly the size of the PCC and the content of the care package influenced the predicted losses or profits for the PCC. Two risk-mitigating measures-risk-adjustment and cost-capping-resulted generally in predicted losses or profits closer to 0, and therefore a reduced risk for the PCC.

## Pf8200bda174d

- Year: 2025
- Linked people: Sander van Kuijk
- Title: The impact of high versus standard enteral protein provision on functional recovery following intensive care admission: A pre-planned Bayesian analysis of the PRECISe trial

Abstract:

BACKGROUND AND AIMS: High protein nutrition may improve outcomes after critical illness. We recently published the primary frequentist analysis of the PRECISe trial, showing that high (2.0 g/kg/day) compared with standard (1.3 g/kg/day) protein provision led to statistically significant worse health-related quality of life. The study, however, was not powered to draw definitive conclusions about clinical and other functional outcomes under a frequentist framework. We present a pre-planned and pre-specified Bayesian analysis to facilitate the clinical interpretation of these paramount endpoints. METHODS: The trial enrolled 935 patients and used the EQ-5D-5L health utility score as the primary endpoint. We performed Bayesian analyses of the primary and selected secondary endpoints, and relevant subgroups, under weakly informative priors. Sensitivity analyses were performed using skeptical and enthusiastic priors, and informed priors (when available) based on existing literature. Thresholds for clinically relevant differences were predefined. RESULTS: The posterior probability of benefit from high (2.0 g/kg/day) protein targets with respect to the EQ-5D-5L health utility score was 0 %. Concerning 60-day mortality, the posterior probability of any benefit from high protein provision was 8 %, with a posterior probability of clinically important harm (>5 % absolute risk difference) of 47 %, which varied between 1 and 21 % across various sensitivity analyses under reference or literature-based priors. CONCLUSIONS: This pre-planned Bayesian re-analysis of the PRECISe trial shows that high (2.0 g/kg/day) compared to standard (1.3 g/kg/day) protein provision in critically ill patients has a low probability to yield any benefit and results in a high probability of an increase of 60-day mortality. REGISTRATION NUMBER OF CLINICAL TRIAL: NCT04633421.

## P900e90c06829

- Year: 2026
- Linked people: Ciaran O'Neill
- Title: Improving the Oral Health of Older People In Care Homes: the TOPIC randomised feasibility study.

Abstract:

The National Institute for Health and Care Excellence guideline NG48 aims to maintain and improve the oral health of care home residents. However, evidence on oral health interventions among care home residents is weak. A co-design process with residents and care home staff refined National Institute for Health and Care Excellence guidance NG48 aspects to facilitate implementation. This study aimed to assess the feasibility of undertaking a large-scale definitive trial on this intervention. A parallel theoretically informed process evaluation explored factors affecting implementation. The feasibility of collecting data to inform a cost-consequence model was also explored.
A pragmatic cluster randomised feasibility study with 12-month follow-up was undertaken in 22 care homes across two sites (London, Northern Ireland). Care homes were randomised into an intervention arm (n = 11) that received the National Institute for Health and Care Excellence guidance NG48-based complex oral health intervention, and a control arm (n = 11) that continued with routine practice. The complex intervention included a training package for care home staff in oral health promotion knowledge and skills; using the Oral Health Assessment Tool to assess residents' oral health needs; and a 'support worker assisted' daily toothbrushing regime with 1500 ppm fluoride toothpaste. Dentate residents aged 65 years or over without severe cognitive impairment were recruited, resulting in a sample of 119 participants. Assessments were undertaken at baseline and 12 months through clinical dental examination and questionnaires. A parallel process evaluation involved semistructured interviews to explore how the intervention could be embedded in standard practice. Rates of recruitment and retention and intervention fidelity were also recorded. Economic evaluation or cost-consequence indicators were collected through interviews with stakeholders, survey and questionnaire data.
Eighty-four per cent of care homes and 88% of residents agreed to participate; 86% of care homes and 69% of residents were retained at 12-month follow-up. Researcher-collected data on clinical and subjective measures had successful completion rates, but completion rates were very low for the weekly symptoms checklist collected by care home staff. The process evaluation highlighted that most care homes were keen to participate, as accessing oral care provision was challenging. The values and beliefs of managers and staff within each care home were key to intervention adoption. Collecting outcomes relevant for cost-consequence modelling is feasible, therefore, supporting an economic evaluation alongside the definite trial. Residents' quality of life was identified as a key outcome for stakeholders, including care home managers.
As ethical approval was granted for care home residents without or with mild cognitive impairment, the inclusion criteria excluded a considerable proportion of residents that had severe cognitive impairment, meaning that the findings are less generalisable to the wider population of care home residents. Attrition rates were high, and recruitment was affected by the coronavirus disease pandemic.
The study documented the feasibility of undertaking a National Institute for Health and Care Excellence guidance NG48-based intervention in care homes. Recruitment and retention were feasible but challenging. A definitive trial should accommodate these challenges.
A definitive trial should assess the effectiveness of the co-designed intervention, with more inclusive recruitment, improving retention, minimising missing data and outcome selection being important issues to consider.
This synopsis presents independent research funded by the National Institute for Health and Care Research (NIHR) Public Health Research programme as award number 17/03/11.

## P7eabf252e699

- Year: 2026
- Linked people: Narcis Gusi
- Title: Latent profiles of movement behaviour compositions and their associations with adiposity and health-related quality of life in Australian children: a cross-sectional and 12-month longitudinal study

Abstract:

Objectives To identify profiles of compositional movement behaviour patterns among children and examine cross-sectional and 12-month associations with adiposity markers and health-related quality of life (HRQoL). Design Secondary analysis of data from the TransformUs cluster randomised controlled trial with cross-sectional and 12-month follow-up analyses. Setting Primary schools in metropolitan and regional areas of Victoria, Australia. Participants Children aged 7–11 years with valid accelerometer at baseline, regardless of demographic, adiposity and HRQoL data available (n=792), were included in the analytical sample for the latent profile analysis. Measures Sedentary time, light-intensity physical activity (LPA) and moderate- to vigorous-intensity physical activity (MVPA) along with their respective mean bout lengths were derived from raw acceleration data. Latent profile analysis used these measures (total times, as isometric log ratios and mean bout lengths) as input variables to classify distinct profiles for us as a categorical exposure variable in regression models. Primary outcomes were age- and sex-standardised body mass index, waist circumference and parent-reported HRQoL at baseline. Secondary outcomes were the same measures assessed at 12-month follow-up. Results Four distinct profiles were identified. The high MVPA-short sedentary bout profile (n=184) was characterised by the highest levels of MVPA, moderate sedentary time and the shortest mean sedentary bout duration. The low sedentary-high LPA profile (n=54) had the lowest sedentary time, the highest LPA and the longest mean LPA bout duration. Two profiles were characterised by high sedentary time: the high sedentary-long sedentary bout profile (n=149), which had the longest mean sedentary bout durations, and the high sedentary-shorter bouts profile (n=405), which also had high sedentary time but shorter bout durations for all intensities. While the omnibus Wald test for differences across profiles indicated uncertainty in the overall profile effect, the high MVPA-short sedentary bout profile had favourable adiposity levels cross-sectionally compared with the high sedentary-long sedentary bout reference profile in pairwise comparisons. No longitudinal associations were detected. Conclusions Four distinct movement profiles were identified. Few pairwise differences between health outcomes were observed. While MVPA remains a key factor for promoting healthy body weight, our findings suggest that a variety of movement patterns - including those characterised by lower sedentary time and higher LPA - may also support health in children. Trial registration This study is a secondary analysis of the TransformUs effectiveness-implementation trial, registered with the Australian Clinical Trials Registry (ACTRN12617000204347; 1 April 2017).

## P73eaa4b74ad5

- Year: 2025
- Linked people: Sander van Kuijk
- Title: Risk Factors for Postoperative Stem Revision in Patients with Periprosthetic Femoral Fractures after Primary Total Hip Arthroplasty: Nationwide Outcomes Based on the Dutch Arthroplasty Registry.

Abstract:

This study aimed to determine the incidence of postoperative primary total hip arthroplasty (THA) stem revision due to periprosthetic fractures (PPF) and analyze related patient and surgical factors.
Utilizing the Kaplan-Meier analysis and Cox regression method to identify risk factors for stem revision due to PPF, this study analyzed 331,009 primary THA procedures from the Dutch Arthroplasty Register between 2007 and 2021.
At 10-year follow-up, the incidence rate was 0.7%. Patient specific factors with significant incidence probabilities were higher age (hazard ratio [HR] 1.29 per 10 years, 95% confidence interval [CI] 1.22-1.36), female sex (HR 1.30, 95% CI 1.16-1.45), American Society of Anesthesiologists (ASA) class II (HR 1.56, 95% CI 1.27-1.93) and ASA class III-IV (HR 2.07, 95% CI 1.59-2.71), Charnley score B2 (HR 1.46, 95% CI 1.23-1.72) and Charnley score C (HR 1.81, 95% CI 1.26-2.59), and higher body mass index (BMI) (HR 1.02 per kg/m2, 95% CI 1.00-1.03). Surgery specific factors with significant incidence probabilities were interventions with an uncemented stem (HR 4.55, 95% CI 3.85-5.26), and anterior approach compared to posterolateral approach (HR 1.25, 95% CI 1.03-1.52).
The highest risk of PPF in THA requiring stem revision was found in older female patients with high ASA class, Charnley score and BMI as well as uncemented implants. This result may prompt surgeons to strive for cemented stem fixation in patients with declining bone stock when feasible. Furthermore, care should be taken when using anterior approaches for patients with specific risk factors.

## P10211b8d057c

- Year: 2025
- Linked people: Federico Augustovski, Fernando Argento
- Title: A Delphi study on valuing DNA sequencing in oncology: a European stakeholder developed framework for assessing next generation sequencing and comprehensive genomic profiling diagnostics

Abstract:

BACKGROUND: Advanced genomic technologies like Next Generation Sequencing and Comprehensive Genomic Profiling are pivotal for the prevention, management and treatment of cancer by identifying crucial genetic markers. However, their adoption in Europe is inconsistent, partly due to the lack of a validated approach to assessing their value. METHODS: A multi-phase mixed-methods approach was implemented, integrating a systematic review and multi-stakeholder consensus-generating Delphi exercise to derive a comprehensive set of value criteria and arrive at a value assessment framework. This value assessment framework adapted an existing Latin American-focused diagnostic framework to the European context. The Delphi included representatives from the broader stakeholder community (patient advocacy, industry, decision-makers, health technology assessment, regulators, academia, and physicians). Over four rounds, participants refined and rated the significance of these criteria in the context of the assessment of the specified technologies in oncology, particularly for reimbursement decisions. Responses were analysed in terms of stability and level of consensus in order to generate a final value assessment framework. FINDINGS: 34 individuals participated in all rounds of the Delphi exercise. The final value assessment framework includes 8 distinct value criteria, including: clinical impact; test performance and quality; quality of scientific evidence; non-clinical impact; impact on health system integration, organisation and delivery of care; economic aspects; ethical and governance concerns; and health system priorities. Within these criteria, a total of 27 distinct sub-criteria were identified, 23 of which had consensus as 'important' or 'very important' in assessing value. INTERPRETATION: The resultant value assessment framework is validated by a wide range of key European stakeholders and enables systematic assessment of Next Generation Sequencing and Comprehensive Genomic Profiling technologies used in oncology diagnostics within the European setting. The framework includes aspects that are not adequately considered in current health technology assessment and goes beyond existing value assessment frameworks through the inclusion of newer criteria such as data governance concerns. FUNDING: Funding was provided by the Precision Cancer Consortium with an unrestricted educational grant.

## P060aa0a07a76

- Year: 2024
- Linked people: Lidia Engel
- Title: Model-Based Economic Evaluations of Interventions for Dementia: An Updated Systematic Review and Quality Assessment

Abstract:

BACKGROUND: There has been an increase in model-based economic evaluations of interventions for dementia. The most recent systematic review of economic evaluations for dementia highlighted weaknesses in studies, including lack of justification for model assumptions and data inputs. OBJECTIVE: This study aimed to update the last published systematic review of model-based economic evaluations of interventions for dementia, including Alzheimer's disease, with a focus on any methodological improvements and quality assessment of the studies. METHODS: Systematic searches in eight databases, including PubMed, Cochrane, Embase, CINAHL, PsycINFO, EconLit, international HTA database, and the Tufts Cost-Effectiveness Analysis Registry were undertaken from February 2018 until August 2022. The quality of the included studies was assessed using the Philips checklist and the Consolidated Health Economic Evaluation Reporting Standards (CHEERS) 2022 checklist. The findings were summarized through narrative analysis. RESULTS: This review included 23 studies, comprising cost-utility analyses (87%), cost-benefit analyses (9%) and cost-effectiveness analyses (4%). The studies covered various interventions, including pharmacological (n = 10, 43%), non-pharmacological (n = 4, 17%), prevention (n = 4, 17%), diagnostic (n = 4, 17%) and integrated (n = 1, 4%) [diagnostics-pharmacologic] strategies. Markov transition models were commonly employed (65%), followed by decision trees (13%) and discrete-event simulation (9%). Several interventions from all categories were reported as being cost effective. The quality of reporting was suboptimal for the Methods and Results sections in almost all studies, although the majority of studies adequately addressed the decision problem, scope, and model-type selection in their economic evaluations. Regarding the quality of methodology, only a minority of studies addressed competing theories or clearly explained the rationale for model structure. Furthermore, few studies systematically identified key parameters or assessed data quality, and uncertainty was mostly addressed partially. CONCLUSIONS: This review informs future research and resource allocation by providing insights into model-based economic evaluations for dementia interventions and highlighting areas for improvement.

## P7b334e4336f3

- Year: 2025
- Linked people: Eleanor Pullenayegum
- Title: Screen Time and Standardized Academic Achievement Tests in Elementary School

Abstract:

Importance: Few studies have investigated the longitudinal associations between different types of screen time in young children and academic achievement in elementary school. Objective: To examine whether there is an association between screen time in young children and standardized academic achievement tests in grades 3 and 6. Design, Setting, and Participants: This prospective cohort study was conducted among children participating in the TARGet Kids! primary care cohort in Ontario, Canada, between July 2008 and June 2023. Participant data were linked to annual grades 3 and 6 provincial standardized academic achievement test results. Exposures: Parent-reported child total screen time, TV and digital media time, and video gaming time. The screen time measurement closest before the outcome was used. Main Outcomes and Measures: Academic achievement levels on standardized tests in reading, writing, and math for grades 3 and 6 were classified as below, at, or above the Ontario provincial standard. Results: This study included 3322 grade 3 children (mean [SD] age at test, 8.86 [0.28] years; 1714 [51.6%] male students) and 2084 grade 6 children (mean [SD] age at test, 11.86 [0.28] years; 1070 [51.3%] male students). Screen time was measured at mean (SD) age of 5.54 (2.36) years for grade 3 children and 7.54 (2.90) years for grade 6 children. From adjusted proportional odds models, each additional hour of total screen time was associated with 9% to 10% lower odds of achieving a higher academic level in grade 3 reading (odds ratio [OR], 0.91; 95% CI, 0.86-0.96; P = .001), grade 3 math (OR, 0.91; 95% CI, 0.86-0.96; P < .001), and grade 6 math (OR, 0.90; 95% CI, 0.84-0.96; P = .002). Similarly, higher TV and digital media time was associated with lower achievement levels in grade 3 reading and math and grade 6 math. Video game use was associated with lower achievement level in grade 3 reading (OR, 0.77; 95% CI, 0.62-0.94; P = .01). In the sex-stratified analysis, video game use among female students was associated with lower grade 3 reading and math achievement. Conclusions and Relevance: In this prospective cohort study of Canadian children recruited from primary care settings, high levels of total screen time and TV and digital media in young children were associated with lower achievement levels in reading and math on standardized tests in elementary school. Early interventions to reduce screen time exposure should be developed and tested to enhance academic achievement in elementary school.

## Pe43bed937331

- Year: 2025
- Linked people: Eleanor Pullenayegum
- Title: Systemic reactogenicity is a correlate of MF59 adjuvant-moderated immunogenicity in influenza vaccinated children

Abstract:

Adjuvanted influenza vaccine induces more robust antibody responses, but is associated with more adverse events following vaccination. Prior work has examined the link between vaccine reactions and immunogenicity in adults, but little is known about the association between reactogenicity and postvaccination antibody responses in children, particularly regarding adjuvanted influenza vaccine. This study examines the relationship between reactogenicity and immunogenicity in children vaccinated against influenza, and the immunomodulatory effects of the adjuvant. We conducted a secondary analysis of data from a cluster-randomized trial of children aged 6 to 72 months from Canadian Hutterite colonies. Participants received either a trivalent MF59-adjuvanted vaccine (aTIV) or a quadrivalent non-adjuvanted vaccine (QIV). Reactogenicity was measured using a composite score based on local, systemic, and respiratory reactions recorded within five days post-vaccination. Immunogenicity was assessed by measuring hemagglutination inhibition (HAI) titers before and four weeks after vaccination. Linear mixed models were used to evaluate associations between reactogenicity scores and post-vaccination log-transformed HAI titers. In adjuvanted vaccinees, higher systemic reactogenicity scores were associated with increased antibody titers for A/H1N1 and B/Victoria, relative to nonadjuvanted vaccinees (β: 0.38, 95% CI: 0.17 to 0.60; and (β: 0.44, 95% CI: 0.24 to 0.64 respectively). Higher systemic reactogenicity in nonadjuvanted vaccinees correlated with reduced post-vaccination antibody titers for A/H1N1 (β: -0.36, 95% CI: -0.54 to -0.18) and B/Victoria (β: -0.37, 95% CI: -0.54 to -0.20). Respiratory reactogenicity was positively correlated with immunogenicity in responses to A/H3N2 in the adjuvanted group (β: 0.78, 95% CI: 0.13 to 1.43). Local reactogenicity was associated with A/H1N1 immunogenicity, but showed no significant interaction with vaccine formulation (β: 0.25, 95% CI: 0.04 to 0.47). Systemic reactogenicity in adjuvanted vaccinees showed positive correlations with immunogenicity, whereas reactogenicity contributed to blunting of antibody responses in nonadjuvanted vaccinees. We found that stronger systemic reactions correlate with improved immune responses in the adjuvanted group against all vaccine strains save A/H3N2, which warrants further investigation. Our study finds that reactogenicity is a modest biomarker for vaccine immunogenicity, and that the increased reactogenicity of the adjuvanted vaccine is associated with enhanced immune responsiveness, which may predict greater vaccine effectiveness.

## Pa04ae3701053

- Year: 2025
- Linked people: Donna Rowen, Nyantara Wickramasekera
- Title: Embedding a Choice Experiment in an Online Decision Aid or Tool: Scoping Review.

Abstract:

BACKGROUND: Decision aids empower patients to understand how treatment options match their preferences. Choice experiments, a method to clarify values used within decision aids, present patients with hypothetical scenarios to reveal their preferences for treatment characteristics. Given the rise in research embedding choice experiments in decision tools and the emergence of novel developments in embedding methodology, a scoping review is warranted. OBJECTIVE: This scoping review examines how choice experiments are embedded into decision tools and how these tools are evaluated, to identify best practices. METHODS: This scoping review followed the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) guidelines. Searches were conducted on MEDLINE, PsycInfo, and Web of Science. The methodology, development and evaluation details of decision aids were extracted and summarized using narrative synthesis. RESULTS: Overall, 33 papers reporting 22 tools were included in the scoping review. These tools were developed for various health conditions, including musculoskeletal (7/22, 32%), oncological (8/22, 36%), and chronic conditions (7/22, 32%). Most decision tools (17/22, 77%) were developed in the United States, with the remaining tools originating in the Netherlands, United Kingdom, Canada, and Australia. The number of publications increased, with 73% (16/22) published since 2015, peaking at 4 publications in 2019. The primary purpose of these tools (20/22, 91%) was to help patients compare or choose treatments. Adaptive conjoint analysis was the most frequently used design type (10/22, 45%), followed by conjoint analysis and discrete choice experiments (DCEs; both 4/22, 18%), modified adaptive conjoint analysis (3/22, 14%), and adaptive best-worst conjoint analysis (1/22, 5%). The number of tasks varied depending on the design (6-12 for DCEs and adaptive conjoint vs 16-20 for conjoint analysis designs). Sawtooth software was commonly used (14/22, 64%) to embed choice tasks. Four proof-of-concept embedding methods were identified: scenario analysis, known preference phenotypes, Bayesian collaborative filtering, and penalized multinomial logit model. After completing the choice tasks patients received tailored information, 73% (16/22) of tools provided attribute importance scores, and 23% (5/22) presented a "best match" treatment ranking. To convey probabilistic attributes, most tools (13/22, 59%) used a combination of approaches, including percentages, natural frequencies, icon arrays, narratives, and videos. The tools were evaluated across diverse study designs (randomized controlled trials, mixed methods, and cohort studies), with sample sizes ranging from 23 to 743 participants. Over 40 different outcomes were included in the evaluations, with the decisional conflict scale being the most frequently used in 6 tools. CONCLUSIONS: This scoping review provides an overview of how choice experiments are embedded into decision tools. It highlights the lack of established best practices for embedding methods, with only 4 proof-of-concept methods identified. Furthermore, the review reveals a lack of consensus on outcome measures, emphasizing the need for standardized outcome selection for future evaluations.

## P59e5f1b652fa

- Year: 2025
- Linked people: 
- Title: A microcosting and cost consequence analysis from a randomized controlled trial comparing genome sequencing with exome sequencing for genetic diagnosis

Abstract:

PURPOSE: Diagnosing rare diseases is costly. The objectives were to microcost exome (ES) and genome sequencing (GS) trios and estimate the incremental costs of GS per additional diagnosis from an institutional payer perspective. METHODS: Trios (proband plus biological parents) that are referred for sequencing were randomly assigned to ES or GS. Laboratory workflow and sequencing were microcosted. Total and category cost per trio were estimated probabilistically. Effectiveness was expressed as diagnostic yield (rates of diagnostic or partially diagnostic variants detected). Incremental costs and effectiveness were calculated. RESULTS: The mean total cost per trio was CAD 2888.79 (95% CI 2567.72, 3492.72) for ES (n = 329) and 4364.02 (95% CI 3984.94, 5013.67) for GS (n = 324). Reagents accounted for 34% and 61% of total costs for ES and GS, respectively. The incremental cost of GS was 1475.23. The diagnostic yield was 35.9% for ES and 32.7% for GS with a difference of 0.032 (95% CI: -0.041, 0.104, P value .397). CONCLUSION: GS demonstrated higher costs and a similar diagnostic yield to ES but was limited by technical capabilities at the time of the study. The study provides comprehensive costs for the economic evaluation comparing alternative diagnostic pathways and impetus for further evaluating variants uniquely detectable by GS.

## Pb1f8adca5f68

- Year: 2025
- Linked people: Tianxin Pan
- Title: Discrete choice experiment on the preferences for continuing medical education training programs among primary health care physicians in China

Abstract:

BACKGROUND: Improving primary health care (PHC) physician's capacity has been identified as an important area in the healthcare reform. The continuing medical education (CME) training programs are conducive to enhancing competence of PHC physicians. But few studies have explored PHC physicians' needs and preferences for CME training programs. This study aimed to explore the preferences for CME training programs from the perspective of PHC physicians, and to understand the willingness, tendency, and needs in CME. METHODS: A Discrete Choice Experiment (DCE) was developed based on literature review and semi-structured interviews with 4 general practitioners to identify key attributes of CME programs. The DCE survey was administered to 360 PHC physicians in Jiangsu Province, China, in August 2023, to elicit preferences for: training frequency, training time, training duration, training location, training content of basic medical services, and training content of basic public health services. A total of 281 valid responses were included after the quality control test, which involved checking completion time and consistency in repeated choice tasks. DCE data were analyzed using Mixed Logit, and Latent Class Models to explore preference heterogeneity and class membership. RESULTS: PHC physicians showed strong preference for CME training programs that were conducted during working hours on weekdays, once a year, at a local meeting place and training on health management of patients with multiple chronic diseases. Latent class analysis identified 2 preference classes, with half (51.2%) of the respondents focused only on training frequency and time while the rest considered training logistic arrangement as well as training content. These preferences could be explained by some observed characteristics of PHC physicians such as age and professional level. CONCLUSIONS: Overall, PHC physicians valued the convenience of participation in CME training programs and training on health management of patients with multiple chronic disease. Our findings can be used to inform the design of CME training programs for PHC physicians in China.

## Pdbf650c4d161

- Year: 2026
- Linked people: Katie Spencer
- Title: Influence of stage at cancer diagnosis on NHS hospital care costs in England: a national, retrospective, population-based cohort study using individual patient-level data

Abstract:

Background Estimates of the cost of cancer care are crucial for the economic evaluation of screening interventions and other early cancer diagnosis initiatives. However, data on the cost of cancer is scarce. This study estimated National Health Service (NHS) hospital care costs for eight cancer types by stage at diagnosis in England. Methods This national, retrospective, population-based cohort study used individual patient-level data collated by the National Disease Registration Service, NHS England. We included patients aged 50-79 years who were diagnosed with a colorectal, head and neck, liver and bile duct, lung, lymphoma, oesophageal, ovarian, or pancreatic cancer in England between Jan 1, 2014, and Dec 31, 2017. For each patient, we obtained linked national health-care records, incorporating all inpatient hospital care, outpatient activity, and accident and emergency department attendances, and costed these using a payer perspective. Patients were excluded if registration was death certificate only, records related only to a secondary metastatic site, sex and cancer type were incompatible, death status or date were uncertain, or there were zero health-care costs from 6 months before diagnosis to end of follow-up. Net, cancer-related, regression-adjusted hospital care costs were reported for each cancer type and stage overall, annually, and by phase of care. Within each annual period and phase, mean monthly costs were also estimated. Findings Of 359 106 cancer records registered, 345 629 cancers were available for analysis, and 333 657 cancers were included in the analysis (147 334 [44·2%] occurred in female patients and 186 323 [55·8%] in male patients; 303 227 [90·9%] among participants of White ethnicity, 4452 [1·3%] among participants of mixed or other ethnicity, 7870 [2·3%] among participants of Asian ethnicity, 4179 [1·3%] among participants of Black ethnicity, and 13 929 [4·2%] among participants of unknown ethnicity). Overall costs were higher at later stages for colorectal, head and neck, lymphoma, and ovarian cancers with mean stage IV costs of £37 838, £36 657, £42 667, and £45 871, respectively. Costs for liver and bile duct, lung, oesophageal, and pancreatic cancers were highest for those diagnosed at stage II (£28 356, £29 553, £33 640, and £39 351, respectively), and slightly lower at stages I, III, and IV. Health-care costs were highest in the initial treatment and the end-of-life phases of care. Within each phase, mean cost per month increased with stage for most cancer types studied, though fewer months of follow-up were observed in each phase for liver and bile duct, lung, oesophageal, and pancreatic cancers. Interpretation Cancer-related NHS hospital care costs by stage at diagnosis differed between cancer types; this heterogeneous pattern could inform detailed and nuanced economic evaluations of early detection initiatives. Funding GRAIL Bio UK.

## P1ce08d1431d4

- Year: 2025
- Linked people: Vincent Lau
- Title: Society of Critical Care Medicine 2024 Guidelines on Adult ICU Design: Executive Summary

Abstract:

Advances in technology, challenges in infection control—such as the severe acute respiratory syndrome coronavirus 2 pandemic, and evolutions in patient- and family-centered care highlight ideal aspects of ICU design present opportunities for enhancement (1,2). For example, prior Society of Critical Care Medicine (SCCM) ICU design guidelines (1995–2012) did not envision remote manipulation of ventilator settings or infusion pumps (3,4) or the unique aspects of pandemic care. Design elements spanning square footage, air handling, airborne isolation, linkage to electronic and digital local or remote systems, as well as ICU organization and layout may be addressed during new construction, revision of existing critical care spaces, or conversion of previously noncritical care space to render ICU care. Ensuring proximity to key destinations helps enable safe, quality care for all ICU subspecialties. ICU design may influence safety and security for patients, visitors, and staff (5). Due to substantial shifts in healthcare and intervening research, SCCM sought to update the 2012 ICU design guidelines to provide expert guidance for clinicians, administrators, and healthcare architects considering constructing a new ICU or renovating one. ICU DESIGN POPULATION, INTERVENTION, COMPARISON, AND OUTCOMES QUESTIONS A summary of Good Practice Statements (GPSs) and Strong Recommendations for selected Population, Intervention, Comparison, and Outcomes (PICO) questions are presented in Table 1 along with panel generated design themes. PICO questions in “bold italics” represent the most impactful areas determined by the panel and are presented herein. Figure 1 provides a Visual Summary of the certainty of evidence and strength of recommendations for each PICO question. Evidence summaries and recommendation justifications for all 15 questions are located within the supporting materials. Overall, the panel articulated 17 recommendations (PICO questions 2.1. and 5.2. each yielded two recommendations), including five GPS. TABLE 1. - Complete Summary of ICU Design Themes and Related Population, Intervention, Comparison, and Outcomes Questionsa Theme Population, Intervention, Comparison, and Outcomes Question 1. ICU layout 1.1. Should high-visibility layouts vs. low-visibility layouts be used in ICUs? 1.2. Should centralized charting areas vs. decentralized charting areas be used in intensive care? 1.3. Should single-bed rooms vs. open bay layouts be used in ICUs? 1.4. Should designs with close proximity to key destinations vs. without close proximity to key destinations be used for ICUs? 2. Room design 2.1. Should rooms with environmental features to enhance sleep and recovery vs. standard rooms be used in ICUs 2.2. Should in-room supplies vs. centralized supply rooms be used in ICUs? 3. Infection control 3.1. Should advanced HVAC designs vs. standard HVAC designs be used in ICUs? 3.2. Should advanced infection prevention features vs. no advanced infection prevention features be used in ICUs? 4. Infrastructure 4.1. Should outside-room monitoring and control of devices vs. inside-room only monitoring and control of devices be used in ICUs? 4.2. Should advanced remote monitoring (e.g., telemedicine) vs. usual care be used in ICUs? 4.3. Should flexible surge capacity vs. no specific design for surge capacity be used in ICUs? 4.4. Should nonwall-based life support utility access vs. wall-based life support utility access be used in ICUs? 5. Staff space 5.1. Should ergonomic features vs. usual designs be used for ICUs? 5.2. Should integrated break/respite space vs. nonintegrated break/respite spaces be used in ICUs? 5.3. Should mobile workstations, or combination workstations vs. fixed workstations, be used in ICUs? HVAC = heating, ventilation, and air conditioning.aItems in “bold italics” represent the one Population, Intervention, Comparison, and Outcomes question in each theme that have been selected for presentation within the Executive Summary; all others are fully reviewed in the complete article (6). Figure 1.: Society of Critical Care Medicine (SCCM) ICU design guidelines, all Population, Intervention, Comparison, and Outcomes—visual summary. GRADE = Grading of Recommendations, Assessment, Development and Evaluation, HVAC = heating, ventilation, and air conditioning.High Level Summary of PICO Questions With Strong Recommendations and GPS Theme 1: ICU Layout 1.1. Should high-visibility vs. low-visibility layouts be used in ICUs? One primary determinant of patient visibility is ICU layout. Visibility of patients at risk of deterioration is a high priority and complements existing monitoring devices, as the sickest patients benefit from early problem detection (7–10). Caring for patients in more visible areas may allow staff to more rapidly intervene and to recognize when colleagues require assistance. The panel noted that “visibility” specifically refers to the patient including their face, monitors, and bedside alarms—as opposed to the room entryway or nonpatient-care design elements. A Strong Recommendation was made in favor of high visibility, despite a low certainty of evidence that evaluated patient safety during critical illness. Although the certainty of evidence is low, this is a fundamental aspect of ICU care. The undesirable effects of high-visibility rooms (e.g., reduced privacy) are believed to be minimal by comparison to the anticipated benefits and may be easily mitigated (11). ICU design for optimum patient visibility from staff workstations is a priority. Theme 2. Room Design 2.1. Should rooms with environmental features that enhance sleep and recovery (light and noise mitigation, natural lighting) vs. standard rooms be used in ICUs? These aspects are priorities as ICU environments commonly disrupt natural sleep cycles, promote delirium, and impede recovery. Incorporation of natural lighting, dynamic lighting, and noise mitigation could reduce sleep disruption. While early studies of windows suggested an impact upon mortality and delirium, effects remain unclear. Due to confounding risks in observational studies, as well as effect estimate imprecision, the panel assigned a low certainty of evidence for window and natural lighting effects on mortality, delirium, as well as ventilator or ICU length of stay. Windows are inherently desirable as they humanize the critical care setting, reflect current patient, family, and staff expectations and are encoded in existing ICU standards. A strong recommendation was made supporting windows in patient rooms. Studies of specific design-related features to address ICU noise mitigation were not identified. Noise canceling ceiling tiles may enhance patient rest and staff communication (12). Common ICU noise sources include staff activity and conversation, furniture movement, other patients, visitors, and device alarms. Because alarms often exceed the World Health Organization decibel standards, they are associated with impaired sleep hygiene (13–16). The panel agreed that the effect of ICU design noise mitigation strategies warranted a very low certainty of evidence assessment due to limited study data. Theme 3. Infection Control 3.2. Should advanced infection prevention features vs. no advanced infection prevention features be used in ICUs? Nosocomial infection is a challenging source of morbidity and mortality in the ICUs and localized outbreaks are well described (17). There is no strong evidence supporting the efficacy of any single infection prevention/control measure to address nosocomial infection. Many measures may reduce microbe prevalence on surfaces, in air, and in water. It is less clear that these measures result in reduced colonization and subsequent infection, but they offer interventions designed to reduce the likelihood of nosocomial pathogen acquisition and subsequent infection, especially in those with immune compromise. Studied interventions included: 1) reducing or clearing pathogen bioburden (18–20); 2) improving hand hygiene compliance (21–25); 3) concerns regarding sink location, splash guard use, and water filter emplacement (26–33); 4) appropriate space for personal protective equipment storage and use (34); 5) pathogen-reducing or surface-cleaning enabling surface materials (35–46); and 6) the impact of push-plate door handles (47). Most interventions demonstrate face validity and appear to reduce microbe counts on surfaces as well as patient colonization by antimicrobial-resistant or multidrug-resistant organism pathogens. While it is unclear which single advanced infection prevention and control feature is most effective, the cumulative effect of multiple simultaneous interventions to mitigate nosocomial colonization, infection, and localized outbreaks is anticipated to be large. A GPS recommendation to incorporate design features to prevent airborne, water-borne, and surface transmission. Theme 4. Infrastructure 4.3. Should flexible surge capacity vs. no specific design for surge capacity be used in ICUs? The COVID-19 pandemic highlighted the unpredictability of critical care needs and the importance of being able to rapidly augment bed capacity to address patient volume surges. Surge capacity includes equipment, staff, and the ICU physical infrastructure (i.e., beds or care locations). While comparison studies of surge capacity were not identified, strategies to rapidly increase capacity included: 1) cohorting multiple patients within a single room (48,49); 2) using novel spaces for patient care (50,51); 3) leveraging resources across health systems such as load balancing across sites (52); 4) deploying infant monitors to increase observation capability (50,53); and 5) emplacing portable high-efficiency particulate air filters to improve airborne isolation room complement (50). Designs that accommodate large patient volume surges may support continued access to routine as well as emergency care despite system stress. Additionally, staff augmentation may occur using a tiered-staffing structure where ICU clinicians guide teams of non-ICU clinicians to provide critical care during surges (54). Theme 5. Staff Space 5.2. Should integrated break/respite space vs. nonintegrated break/respite spaces be used in ICUs? Staff satisfaction, burnout, and clinical performance may be influenced by the design, usability, and impact provided by nonworkspaces such as break rooms and respite areas. Break rooms are often multifunctional, providing space for nourishment, team education, as well as team bonding and mentoring. Such spaces may promote staff well-being. Since critical care environments are often high-stress environments, individual spaces devoted to recovery and well-being complement breakroom functionality. The panel made two recommendations. First, including dedicated staff break rooms that provided storage lockers, washrooms with showers, and nutrition areas was embraced as a GPS. An additional consideration is to locate the break room within the ICU, in a space with windows for natural light. Second, a conditional recommendation was crafted for less essential “wellness rooms” or “respite spaces” as promising complements to break rooms, noting that there is limited evidence to support this as a routine practice (55,56). CONCLUSIONS This executive summary and associated article are SCCM evidence-based guidelines, including 15 PICO questions that update SCCMs 2012 guidelines. The guidelines panel considered five themes—layout of ICU rooms, room design, infrastructure, infection control and prevention, and space for staff—as domains related to ICU design. This summary presents five of the 17 recommendations that if implemented will result in ICU designs that are patient, family, and clinician centered. Strong Recommendations were made for: 1) high patient visibility and 2) room environmental features that enhance sleep and recovery. Other recommendations were conditional along with GPSs including: 1) integrated staff break/respite spaces, 2) advanced infection prevention features, and 3) flexible surge capacity design. While the underpinning evidence was of low certainty, these guidelines provides a unique and comprehensive summary of evidence-based design data informed by practice-based expertise.

## P1c148ff9a6fa

- Year: 2024
- Linked people: Zhuxin Mao
- Title: COVID-19-related health utility values and changes in COVID-19 patients and the general population: a scoping review

Abstract:

Purpose To summarise the diverse literature reporting the impact of COVID-19 on health utility in COVID-19 patients as well as in general populations being affected by COVID-19 control policies. Methods A literature search up to April 2023 was conducted to identify papers reporting health utility in COVID-19 patients or in COVID-19-affected general populations. We present a narrative synthesis of the health utility values/losses of the retained studies to show the mean health utility values/losses with 95% confidence intervals. Mean utility values/losses for categories defined by medical attendance and data collection time were calculated using random-effects models. Results In total, 98 studies-68 studies on COVID-19 patients and 30 studies on general populations-were retained for detailed review. Mean (95% CI) health utility values were 0.83 (0.81, 0.86), 0.78 (0.73, 0.83), 0.82 (0.78, 0.86) and 0.71 (0.65, 0.78) for general populations, non-hospitalised, hospitalised and ICU patients, respectively, irrespective of the data collection time. Mean utility losses in patients and general populations ranged from 0.03 to 0.34 and from 0.02 to 0.18, respectively. Conclusions This scoping review provides a summary of the health utility impact of COVID-19 and COVID-19 control policies. COVID-19-affected populations were reported to have poor health utility, while a high degree of heterogeneity was observed across studies. Population- and/or country-specific health utility is recommended for use in future economic evaluation on COVID-19-related interventions.

## Pe58589b32a4f

- Year: 2026
- Linked people: Lucky Ngwira
- Title: Uncertainty in Economic Evaluation: A Pragmatic Guide for Health Technology Assessment (HTA) Agencies in Resource-Constrained Settings.

Abstract:

Understanding the financial and health consequences if economic evaluation assumptions prove incorrect is essential for managing the risk associated with benefit package decisions, particularly in resource-constrained and overburdened healthcare systems. Yet these are also the settings that face the greatest challenges in conducting comprehensive uncertainty analysis, owing to a range of factors including limited skilled staff, data constraints, and short timelines to generate evidence in time to influence policy. This paper takes a pragmatic approach to support health technology assessment agencies in these settings to generate policy-relevant uncertainty analysis, drawing on good practice literature and the authors' collective experience conducting economic evaluation for policy across resource-constrained settings. For each step of the economic evaluation process, we outline the main sources of uncertainty, principles for deciding which uncertainty analysis to prioritise, and approaches to overcome some of the common challenges faced when dealing with constrained timelines, data, and skilled staff. The overarching goal is to support better-informed decisions, by targeting uncertainty analysis to factors that actually affect decisions and by effectively communicating this decision-relevant uncertainty to policymakers.

## P470669829dcb

- Year: 2026
- Linked people: Juanita Haagsma
- Title: The effect of feedback on the diagnostic process of physicians at the emergency department: a systematic review

Abstract:

In the emergency department (ED), the diagnostic process is complex. Discrepancies between the initial diagnosis in the ED and the final discharge diagnosis occur in 12-15%. Emergency physicians are often unaware of these discrepancies. Systematic feedback could serve as a valuable tool to enhance the diagnostic process. The potential methods and impact of such feedback remain poorly understood. This systematic review (PROSPERO: CRD42024491077) aimed to obtain insight into the types and timing of feedback provided to ED physicians about the diagnostic process and examined the effect on ED physicians' performance and confidence. Studies were included if they examined feedback on the diagnostic process to physicians in the ED. Five large international databases (MEDLINE, EMBASE, Cochrane libraries, Google Scholar, and Web of Science) were searched. Quality assessment was performed using Grading of Recommendations Assessment, Development and Evaluation. In total 1897 articles were screened, of which 11 were included in this review. Most of them were qualified as low-grade evidence. Feedback was given through in-person sessions, monthly group meetings, rapid diagnostic discussions, and computer-based feedback. Six studies reported feedback methods to improve diagnostic accuracy. Furthermore, reduction of adverse outcomes after feedback introduction was reported by two articles. Confidence was reported in one study. This review showed that - although there were few studies and generally of low quality - structured feedback may positively influence the diagnostic performance of ED physicians. The feedback strategies identified in this review could be used for future studies on their effectiveness. Furthermore, rigorous study designs, standardized outcome measures, and scalable feedback methods are needed.

## P4906d51ea7bd

- Year: 2025
- Linked people: Sander van Kuijk
- Title: CT Perfusion Imaging After Selection for Late-Window Endovascular Stroke Treatment

Abstract:

Importance: MR CLEAN-LATE (Multicenter Randomized Clinical Trial of Endovascular Treatment of Acute Ischemic Stroke in the Netherlands for Late Arrivals) showed efficacy of endovascular treatment (EVT) in the late window (6-24 hours after stroke symptom onset or time last seen well) among patients with ischemic stroke selected based on collateral flow. Therefore, the future role of computed tomography perfusion (CTP) imaging in patient selection for late-window EVT may change. Objective: To investigate the interaction among CTP parameters (core volumes, penumbra volumes, and mismatch ratio) and the association of EVT with functional outcomes among patients in the late window after ischemic stroke selected based on collateral flow. Design, Setting, and Participants: This is a post hoc secondary analysis of MR CLEAN-LATE, a multicenter randomized clinical trial, with open-label treatment and blinded end point, conducted from February 2, 2018, to January 27, 2022, in 18 Dutch stroke intervention centers. Participants included 502 patients with anterior circulation large vessel occlusion and present collateral flow on results of computed tomographic angiography in the late window after stroke, who gave deferred consent and were included in MR CLEAN-LATE. All patients had completed follow-up at 90 days. This secondary analysis included 313 patients (62%) with available CTP results. Statistical analysis was performed in September 2023. Intervention: Patients were randomized to receive EVT (EVT group) and best medical management vs best medical management alone (no EVT group). Main Outcomes and Measures: The primary outcome was functional outcome at 90 days measured by the modified Rankin Scale score. The treatment effect was analyzed in subgroups of core volumes, penumbra volume, and mismatch ratios using ordinal regression analysis. An interaction analysis was performed to assess whether CTP parameters modified the EVT effect on the modified Rankin Scale score at 90 days. All analyses were adjusted for relevant prognostic factors. Results: Among the 313 patients (158 women [50%]) in the study, the median age was 73 years (IQR, 63-80 years), and the EVT group had fewer male participants than the no EVT group (73 of 168 [43%] vs 82 of 145 [57%]). Penumbra volumes significantly modified the association of EVT with outcomes (P < .001 for interaction), with the largest effect size among patients with penumbras of 120 mL or more (adjusted common odds ratio [ACOR], 6.89 [95% CI, 2.96-16.04]) and the smallest effect size among patients with penumbras of 72 mL or less (ACOR, 0.49 [95% CI, 0.22-1.08]). Core volume and mismatch ratio did not modify the EVT effect. Conclusions and Relevance: Based on results from this secondary analysis of the MR CLEAN-LATE randomized clinical trial, there was a direct interaction between penumbra volume and treatment effect, and a trend toward potential harm of EVT was seen among patients with the smallest penumbras, which warrants further research. However, core volume and mismatch ratio did not seem to have additional value in patient selection. Trial Registration: isrctn.org Identifier: ISRCTN19922220.

## Pabef64274879

- Year: 2025
- Linked people: Richard Norman
- Title: The role of women's empowerment in the uptake of maternal health services in low- and middle-income countries: a propensity score-matched analysis

Abstract:

Background: Women's empowerment directly influences the quality and timeliness of the maternal health care they receive; a lack thereof, particularly in low- and middle-income countries (LMICs), is likely to contribute to poor uptake of maternal healthcare. We aimed to evaluate the role of women's empowerment in maternal healthcare in LMICs. Methods: We used the recent Demographic and Health Survey (DHS) data on 71 077 married/partnered women from 35 LMICs. We categorised women as empowered if they participated in all decision-making activities and were able to disagree that a husband is justified in hitting or beating his wife for any reason. We used logit propensity score matching (PSM) analysis to estimate the effect of women's empowerment on maternal health services. Result: Only one-third (33.8%) of reproductive-age women in LMICs (95% confidence interval = 27.7-40.8) were estimated to be empowered. Women's empowerment was associated with an 11.2 percentage point increase in having adequate antenatal care (ANC) visits (average treatment effects on the treated (ATT) = 0.112, standard error (SE) = 0.026) and an 8.0 percentage point increase in the likelihood of health facility childbirth (ATT = 0.078, SE = 0.039). However, there was insufficient evidence for early postnatal care visits. Conclusions: Empowering women has a positive association with the utilisation of adequate ANC visits and health facility childbirth in LMICs. These findings underscore the necessity for public health programmes to empower women and enhance their decision-making abilities to improve maternal healthcare uptake, such as health facility childbirth and ANC visits.

## P3c3cb82a8a4a

- Year: 2026
- Linked people: Jan Faller
- Title: Consumers' experiences with and outcomes from Better Access: Results from a national survey.

Abstract:

We sought consumers' views about Better Access, which funds sessions of care with eligible providers via the Medicare Benefits Schedule (MBS).
We surveyed a stratified random sample of consumers who saw a clinical psychologist, psychologist, social worker or occupational therapist (OT) via Better Access during 2021. The survey focussed on consumers' experiences with receiving treatment through Better Access, and the outcomes of this treatment. Survey data were linked to MBS claims data for consenting participants.
In total, 2013 individuals completed the survey; linked MBS data were available for 1317 (65.4%). The majority (85.2%) were satisfied with their care, although they raised some issues, particularly around affordability. When asked to rate their mental health before and after treatment, 91.9% indicated it had significantly improved. Overall, 77.5% attributed this improvement to treatment by the mental health professional. For the full sample, baseline self-rated mental health was predictive of improvement, as was the number of sessions. For the sub-sample with linked data, these factors also predicted improvement, as did whether they paid a co-payment.
In general, consumers who use Better Access appear to appreciate the programme and benefit from the care it provides. However, affordability remains an issue.

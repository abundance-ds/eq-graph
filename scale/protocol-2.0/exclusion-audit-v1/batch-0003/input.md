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

## Pd10a6328658f

- Year: 2025
- Linked people: Kompal Sinha
- Title: Household indebtedness and multidimensional poverty: evidence from China

Abstract:

Household indebtedness has risen sharply and reached unprecedented levels globally. Low-income households disproportionately bear the burden of this debt, making them particularly vulnerable to over-indebtedness and financial vulnerabilities. This article examines the complex relationship between household indebtedness and multidimensional poverty, accounting for household heterogeneity. Using data from the China Household Financial Survey, we employ both traditional linear regression models and semi-parametric Generalized Additive Models (GAM) to uncover a non-linear relationship between household indebtedness and multidimensional poverty. The analysis finds a dual-threshold impairing effect of household indebtedness on multidimensional poverty. Furthermore, the impact of indebtedness varies significantly across households based on financial and demographic characteristics. Households with solvency-strain, those with credit-constraints, minority households, female-household heads, and those without government subsidies, are disproportionately affected by these dual-threshold effects. Notably, these adverse effects are consistent across both rural and urban households. Robustness checks and endogeneity analyses, conducted using a two-step generalized additive model (2SGAM), validate the findings and reinforce the reliability of the results. Our findings provide new insights into the non-linear relationship between household indebtedness and multidimensional poverty and offer evidence for policymakers to guide accessibility of household credit facilities.

## Pcb5b70fbb68f

- Year: 2025
- Linked people: Hilton Lam
- Title: Number of people treated for hepatitis C virus infection in 2014-2023 and applicable lessons for new HBV and HDV therapies

Abstract:

BACKGROUND & AIMS: The year 2023 marked the 10-year anniversary of the launch of direct-acting antivirals (DAAs) for the treatment of hepatitis C virus (HCV). Monitoring HCV treatment trends by country, region, and globally is important to assess progress toward the World Health Organization's 2030 elimination targets. Additionally, historical patterns can help predict the uptake of future therapies for other liver diseases. METHODS: The number of people living with HCV (PLHCV) treated between 2014-2023 across 119 countries was estimated using national HCV registries, reported DAA sales data, pharmaceutical companies' reports, and estimates provided by national experts. For the countries with no available data, the average estimate of the corresponding Global Burden of Disease region was used. RESULTS: An estimated 13,816,000 (95% uncertainty intervals: 13,221,000-16,415,000) PLHCV were treated, of whom 12,748,000 (12,226,000-15,231,000) were treated with DAAs, of which 11,081,000 (10,542,000-13,338,000) were sofosbuvir-based DAA regimens. Country-level data accounted for 97% of these estimates. In high-income countries, there was a 41% drop in treatment from its peak, and reimbursement was a large predictor of treatment. In low- and middle-income countries, price played an important role in expanding treatment access through the public and private markets, and treatment continues to increase slowly after a sharp drop at the end of the Egyptian national program. CONCLUSIONS: In the last 10 years, 21% of all HCV infections were treated with DAAs. Regional and temporal variations highlight the importance of active screening strategies. Without program enhancements, the number of treated PLHCV stalled in every country/region, which may not reflect a lower prevalence but may instead reflect the diminishing returns of existing strategies. IMPACT AND IMPLICATIONS: Long-term hepatitis C virus (HCV) infection can lead to cirrhosis and liver cancer. Since 2014, these infections can be effectively treated with 8-12 weeks of oral therapies. In 2015, the World Health Organization established targets to eliminate HCV by 2030, which included treatment targets for member countries. The current study examines HCV treatment patterns across 119 countries and regions from 2014 to 2023 to assess the impact of national programs. This study can assist physicians and policymakers in understanding treatment patterns within similar regions or income groups and in utilizing historical data to refine their strategies in the future.

## P93fe1ea78431

- Year: 2025
- Linked people: Trudy Sullivan
- Title: Facilitators and barriers of public–private partnerships for universal health coverage in sub-Saharan Africa: a scoping review

Abstract:

Universal health coverage (UHC) provides a platform for attaining 'Health for All'. Attaining UHC requires substantial investment and resources in the health sector. This can be challenging for many sub-Saharan African (SSA) countries. Public-private partnerships (PPPs) could be a potential solution. The implementation of healthcare PPPs for developing health system capacities for UHC presents both significant opportunities and notable challenges. This scoping review, part of a broader review on PPPs, examines the facilitators and barriers of healthcare PPPs and their impact on UHC. The review was guided by Arksey and O'Malley's guidelines for conducting a scoping review. PubMed, Medline (Ovid), Global Health (Ovid), Web of Science, Scopus, and EconLit were searched for peer-reviewed English language publications from January 2013 to December 2023. Nineteen studies were eligible for the final analysis following screening of 944 studies. Identified key facilitators of PPPs for UHC included well-established institutional structures, robust accreditation systems, accountability mechanisms, and political will and support. These factors contributed to improving primary healthcare delivery, which is a critical dimension for UHC. Key barriers identified were limited capacity of implementing partners, regulatory inadequacies, and insufficient funds. These barriers negatively affected the performance of healthcare PPPs, which translates into systemic inequities in access to essential health services, impeding progress towards achieving UHC. Considering contract management capacity of implementers, sources and flow of funds, and regulatory frameworks are highly recommended for UHC to be realized using PPPs.

## P05638f3c10a4

- Year: 2024
- Linked people: Federico Augustovski
- Title: Exploring gender disparities in the disease and economic tobacco-attributable burden in Latin America

Abstract:

Introduction: Tobacco use has significant health consequences in Latin America, and while studies have examined the overall impact, the gender-specific effects have not been thoroughly researched. Understanding these differences is crucial for effective tobacco control policies. The objective of this study was to explore the differences in tobacco-attributable disease and economic burden between men and women in Argentina, Brazil, Chile, Colombia, Costa Rica, Ecuador, Mexico, and Peru. Methods: We used a previously validated economic model to quantify the impact of tobacco-related illnesses, including morbidity, mortality, healthcare costs, productivity losses, informal care expenses, and DALYs, by gender and age. We utilized data from national surveys, records, studies, and expert opinions to populate the model. Results: In 2020, there were 351,000 smoking-attributable deaths. Men accounted for 69% and women 31%. Ecuador and Mexico had the highest male-to-female death ratio, while Peru and Chile had the smallest disparities. 2.3 million tobacco-related disease events occurred, with 65% in men and 35% in women. Ecuador and Mexico had higher disease rates among men, while Peru had a more balanced ratio. Regarding DALYs, men lost 6.3 million due to tobacco, while women lost 3.3 million, primarily from COPD, cardiovascular disease, and cancer. Brazil and Mexico had the highest DALY losses for both genders. Costa Rica had a lower male-to-female tobacco use prevalence ratio but ranked second in deaths, disease events, and DALYs attributed to tobacco. Colombia had a unique pattern with a male-to-female death ratio of 2.08 but a higher ratio for disease events. The health systems spent $22.8 billion to treat tobacco-attributable diseases, with a male-to-female cost ratio 2.15. Ecuador showed the greatest gender cost difference, while Peru had the lowest. Productivity loss due to tobacco was $16.2 billion, with Ecuador and Mexico exhibiting the highest gender disparities and Peru the lowest. Informal care costs amounted to $10.8 billion, with men incurring higher costs in Ecuador, Costa Rica, and Mexico. Discussion: Tobacco causes significant health and economic burdens in Latin America, with gender-based differences. There is a need for gender-disaggregated data to improve tobacco control policies.

## Pbe7905bdbb52

- Year: 2025
- Linked people: Deborah Street, Rosalie Viney
- Title: Artificial intelligence in radiation therapy treatment planning: A discrete choice experiment.

Abstract:

INTRODUCTION: The application of artificial intelligence (AI) in radiation therapy holds promise for addressing challenges, such as healthcare staff shortages, increased efficiency and treatment planning variations. Increased AI adoption has the potential to standardise treatment protocols, enhance quality, improve patient outcomes, and reduce costs. However, drawbacks include impacts on employment and algorithmic biases, making it crucial to navigate trade-offs. A discrete choice experiment (DCE) was undertaken to examine the AI-related characteristics radiation oncology professionals think are most important for adoption in radiation therapy treatment planning. METHODS: Radiation oncology professionals completed an online discrete choice experiment to express their preferences about AI systems for radiation therapy planning which were described by five attributes, each with 2-4 levels: accuracy, automation, exploratory ability, compatibility with other systems and impact on workload. The survey also included questions about attitudes to AI. Choices were modelled using mixed logit regression. RESULTS: The survey was completed by 82 respondents. The results showed they preferred AI systems that offer the largest time saving, and that provide explanations of the AI reasoning (both in-depth and basic). They also favoured systems that provide improved contouring precision compared with manual systems. Respondents emphasised the importance of AI systems being cost-effective, while also recognising AI's impact on professional roles, responsibilities, and service delivery. CONCLUSIONS: This study provides important information about radiation oncology professionals' priorities for AI in treatment planning. The findings from this study can be used to inform future research on economic evaluations and management perspectives of AI-driven technologies in radiation therapy.

## P2c95c3f7fed2

- Year: 2025
- Linked people: Abdulmuminu Isah
- Title: Core drug use indicators in Nigerian health facilities: a systematic review (1994–2024)

Abstract:

Objectives We systematically reviewed the rational use of medicines using the World Health Organization/International Network of Rational Use of Drugs (WHO/INRUD) core drug use indicators. We also assessed the impact of the coronavirus disease 2019 pandemic and the National Drug Policy (NDP) 2005 on the rational use of medicines. Methods Searches were conducted in PubMed, Scopus, and Google Scholar databases to identify studies that met our eligibility criteria. Assessment of the quality of studies was conducted using the Joanna Briggs Institute criteria for analytical studies. We reported and compared the median values of WHO/INRUD core drug use indicators with standard thresholds. Data were presented with median, interquartile range (IQR), and percentages. Mann-Whitney and Kruskal-Wallis tests were conducted to assess for statistical significance ( P < 0.05) across variables. Results Thirty-one studies were included in the review, comprising 50,931 patient encounters across 268 health facilities. Within prescribing indicators, average number of medicines per patient encountered [3.4 (IQR: 3.0 to 4.0)], percentage of medicines prescribed by generic [50.4 % (IQR: 47.4 % to 65.0 %)], percentage of encounters with antibiotic prescribed [40.2 % (IQR: 30.5 % to 52.7 %)], percentage of encounters with injection prescribed [18 % (IQR: 3.2 % to 30.0 %)] and the percentage of medicines prescribed from essential medicines list [82.0 % (IQR: 66.4 % to 89.3 %)]. The median percentage of encounters with antibiotics ( P = 0.04) and the median percentage of medicines prescribed by generics ( P = 0.03) increased during and after the COVID-19 pandemic. Prescribing indicators were worse in primary and secondary health facilities, with significant differences in the median percentage of encounters with antibiotics ( P = 0.007) and injections ( P = 0.0002) across primary, secondary, and tertiary health facilities. There were improvements across all prescribing indicators after the implementation of NDP 2005. Conclusions Core drug use indicators in Nigerian health facilities deviated from the WHO/INRUD thresholds, with noticeable improvement after the implementation of NDP 2005. More efforts are needed to improve rational drug use in Nigerian hospitals.

## P3dce4f0ff57a

- Year: 2025
- Linked people: Deborah Marshall
- Title: Usability testing of an individualized decision aid for total knee arthroplasty

Abstract:

Osteoarthritis (OA) is a leading cause of total knee arthroplasty (TKA), affecting over 15 % of Canadians. With an aging population and suboptimal use of non-surgical options, TKA rates and wait times are rising. Although TKA is effective, 30 % of patients are dissatisfied due to unmet expectations, suggesting some surgeries may be inappropriate. Patient decision aids can set realistic expectations, improve decision quality, and enhance satisfaction. We developed an individualized online patient decision aid allowing patients to compare treatment outcomes based on similar characteristics (age, sex and body mass index) and evaluated its usability before clinical implementation. Participants were recruited from a high-volume urban hip and knee clinic. Eligible adults diagnosed with knee OA completed the decision aid online and subsequently filled out demographics and survey forms, including the Preparation for Decision Making Scale (PDMS), System Usability Scale (SUS), and Acceptability Scale. Data were analyzed using descriptive statistics and content analysis of open-ended responses. There were 20 participants (mean age 68 years, 65 % female). The average PDMS score was 66.4, indicating above-average preparedness for decision-making. The SUS score averaged 63.4, suggesting marginal usability. Females and participants under 70 years reported higher PDMS and SUS scores. Most participants rated the information presentation as “good” or “excellent,” with 75 % finding the decision aid's length appropriate and information balanced. Feedback highlighted the need to simplify content, reduce variables, and offer the aid earlier in treatment. The decision aid demonstrated reasonable usability, acceptability, and usefulness for routine practice. Future research should explore its impact on long-term patient outcomes and satisfaction, including among non-surgical populations. Incorporating this decision aid into routine practice can help patients set realistic expectations and make informed decisions, reducing dissatisfaction. Offering it earlier in the patient journey may enhance its impact, especially for non-surgical options. • Osteoarthritis (OA) is a leading cause of total knee arthroplasty (TKA). • Some patients are dissatisfied with TKA due to unmet expectations. • Patient decision aids can set realistic expectations, improve decision quality, and enhance satisfaction. • An individualized decision aid shows reasonable usefulness, acceptability, and usability. • Offering the decision aid earlier may boost impact, especially for non-surgical options.

## P191009c59a97

- Year: 2024
- Linked people: Marufa Sultana
- Title: Mapping gaps and exploring impairment and disability prevalence in South Asian (SAARC) countries: a scoping review

Abstract:

Despite the considerable health and economic burden of disability in the South Asian (SA) region, there is limited evidence of impairments and disabilities prevalence and the need for Assistive Technologies (ATs). This scoping review aims to synthesise the evidence of the impairments and disabilities in SA countries. This review followed Arksey and O'Malley's methodological framework. EBSCOhost, EMBASE, PubMed, and Web of Science databases were searched for original research articles from SA countries. In this study, impairment and disability refer to functional limitations restricting individuals from performing activities, including visual, hearing, speaking, cognitive, mobility, and self-care difficulties. The review included full-text, English-language articles addressing any impairment and disability, without restrictions on publication date. This review identified 105 articles distributed over the six impairment and disability domains: visual, hearing, mobility, self-care, speaking, and cognitive. Most evidence originated from India (50.5%) and focused on visual impairments (53.3%). The review identified that heterogeneity in methodologies, case identification definitions, and study settings contributed to variations in prevalence estimation and restricted the comparability within and across countries. Besides, the uneven distribution of studies across countries suggests varying inclinations of countries toward specific impairment and disability domains. The review identified variations in prevalence due to differences in methodologies, definitions, and contexts. The review also identified the uneven distribution of studies, limited evidence on ATs, reliance on self-reported data, and lack of nationally representative research. Future research should use standardised case identification and evidence-based approaches to enhance comparability and minimise response biases.

## P0041e193c954

- Year: 2024
- Linked people: Rebecca Addo
- Title: PP76 “It Is Better For Me To Die Than To Be Disgraced”: Perceptions Of Worse-Than-Death Health States In Ghana

Abstract:

Introduction Many cultures across the world have varying conceptions about death and dying. Perceptions about health states considered “worse than death” also vary based on sociocultural norms as well as health system capacity. We explore worse-than-death health states in Ghana as well as reasons for opting for death in those health states. Methods We interviewed 28 participants from three regions in Ghana to understand the contextual “value of life” in Ghana and factors influencing respondents’ decision to opt to die rather than live in a particular health state. Written consents were sought from all participants to partake in the study. Interviews were conducted in either Twi or English based on each participant’s preference and lasted for an average of 30 to 35 minutes. Interviews were transcribed verbatim and stored in NVivo software. Data were analyzed thematically. Results We identified that health states perceived as worse than death were those associated with impairment in mobility, anxiety/depression, and pain/discomfort. Participants preferred death under these circumstances because they wanted to avoid the financial burden on themselves and family, time spent in caregiving by family, loss of personhood, and loss of social status. Decisions regarding health states worse than death hold considerable importance, particularly in a context where culture and societal norms play a role in shaping how quality of life is assessed. Conclusions An understanding of the value Ghanaians attach to health states perceived as worse than death provides useful information for patient-centered care. Findings from the study can provide evidence on healthcare resource allocation and aid policymakers and clinicians in making informed decisions on which treatments to prioritize, and how to maximize the overall health and well-being of individuals.

## P7fe7cb86ffa4

- Year: 2025
- Linked people: Nyantara Wickramasekera
- Title: OP23 Developing A Personalized Decision Aid Incorporating A Discrete Choice Experiment: A Case Study In Ulcerative Colitis

Abstract:

Introduction Choosing the optimal ulcerative colitis treatment is complex, given the range of medical and surgical options with varying side effects and effectiveness. Decision aids can improve patient choices, but current tools lack personalization. To address this, we developed a personalized decision tool using a discrete choice experiment (DCE) to help patients make informed decisions about medical or surgical treatments. Methods An online DCE survey was developed containing competing treatment profiles described using all important aspects of the treatment (effectiveness, side effects, family planning). Patients (n=300) with ulcerative colitis were asked to consider the benefits and disadvantages of each treatment profile and select the treatment that they would choose. The DCE data were analyzed using mixed logit and latent class models. The model results were integrated into an online decision aid using a Shiny application. Results R Shiny was successfully used to enable the real-time personalization of DCE results. The developed decision aid contained two aspects of personalization. First, attribute importance scores showed the treatment characteristics that mattered most to patients based on their DCE choices. Second, a “best-match” treatment that aligned with their preferences was provided from uptake rate calculations. User testing of the developed decision aid is ongoing. However, initial feedback from patients has been positive. Conclusions A key challenge in developing personalized decision aids is providing real-time, tailored recommendations based on individual preferences. This study demonstrated the feasibility of integrating DCE methods into personalized decision aids for ulcerative colitis. By tailoring treatment recommendations to individual patient preferences, this tool has the potential to empower patients, reduce decisional conflict, and enhance shared decision-making between patients and clinicians.

## Pe43e1bf41b84

- Year: 2025
- Linked people: Nick Bansback
- Title: Patient Perceptions of Medication Therapy for Prevention of Posttraumatic Osteoarthritis Following Anterior Cruciate Ligament Injury: A Qualitative Content Analysis

Abstract:

OBJECTIVE: Posttraumatic osteoarthritis (PTOA) accounts for nearly 12% of osteoarthritis incidences and often occurs after anterior cruciate ligament (ACL) tear. Ensuring the uptake of preventive treatments for PTOA requires that investigators and clinicians understand factors influencing patients to seek preventive therapies. This qualitative, descriptive study aimed to assess individuals' willingness to adopt a medication therapy for PTOA prevention following ACL injury. METHODS: We enrolled participants who had an ACL tear within two years of enrollment. Study individuals participated in a semistructured interview or focus group. We reviewed audio transcriptions for accuracy, and then organized the data inductively, beginning with open coding of audio transcriptions using NVivo 12. Finally, using a qualitative content analysis approach, we identified, revised, and constructed themes and subthemes. RESULTS: Twenty-five individuals (mean age 25 years, 60% women) participated. Participants were an average of 10 months after injury (mean 310 days, 95% confidence interval [CI] 249-371) and reported a mean Knee Injury and Osteoarthritis Outcome Score pain score of 80.3 (95% CI 74.5-86.2). We identified three main themes related to general treatment for PTOA (eg, unwanted side effects), medication treatment for PTOA (eg, concern about pill size and dose frequency), and clinical trial attributes (eg, time commitment). CONCLUSION: Although participants expressed great interest in trying medication therapy for PTOA prevention, there was variability in which components of treatment mattered to them. Our results stress the importance of using qualitative approaches such as this one to inform the design of trials and treatments that real-world patients will pursue with enthusiasm.

## P434558e1c87f

- Year: 2025
- Linked people: Shitong Xie, Xuejing Jin
- Title: Health utility book: A systematic review and meta-analysis of health utilities in gastric cancer

Abstract:

Purpose The treatment landscape in gastric cancer has changed drastically over the last 15 years with surgical advancements and the introduction of new therapeutic agents and combinations. Despite the potential for improved survival, these new interventions can impact health-related quality of life (HRQoL). Our objective was to identify and synthesize health utility data for gastric cancer patients as part of the Health Utility Book (HUB) project. Methods We searched MEDLINE, EMBASE, EconLit, and CINAHL from inception to March 2023 for original studies that reported health utility data for gastric cancer. Records were screened independently and in duplicate by two reviewers. Data on study design, patient characteristics, and health utilities were extracted using a standardized form. A random effects meta-analysis was conducted to synthesize health utilities by cancer stage. Heterogeneity was evaluated using the I 2 statistic. Results 600 health utilities from 3,405 respondents were identified across 19 studies. All studies were published between 2018 and 2022 and most were conducted in Asia (n = 12, 63.2%). The EQ-5D was the most common method of preference elicitation (n = 17, 89.5%), and health utilities ranged from 0.298 (SD 0.088) to 0.920 (SD 0.130). Mean health utilities from random effects models were 0.82 (95% Confidence Interval [CI] 0.76-0.88), 0.76 (95% CI 0.68-0.85), and 0.67 (95% CI 0.46-0.87) for early stage, advanced stage, and metastatic gastric cancer, respectively. Conclusion This systematic review provides a reference set of health utilities for gastric cancer, which can help understand HRQoL and facilitate the retrieval and selection of health utilities for economic evaluations.

## P3b0355854b5d

- Year: 2025
- Linked people: Annette Regan
- Title: Intention to Use RSVpreF Vaccine or Nirsevimab to Prevent Infant RSV Among Pregnant Individuals

Abstract:

BACKGROUND: Respiratory syncytial virus (RSV) is the leading cause of hospitalization among infants in the United States. While 2 new immunization products have been developed to prevent RSV in infants-RSVpreF vaccine (a prefusion F protein-based vaccine for pregnant individuals) and nirsevimab (a monoclonal antibody for infants)-intended uptake of these products is unclear. Our objective was to evaluate intended uptake of each product and their correlates among pregnant individuals. METHODS: We conducted a nationally representative survey of pregnant individuals weighted to the US population of births between September 20 and October 3, 2023. Primary outcomes included whether each participant intended to receive RSVpreF vaccine during pregnancy or immunize their infant with nirsevimab; beliefs about product safety, effectiveness and importance; and reasons for hesitancy. We used logistic regression to identify correlates of intent and product support, controlling for sociodemographic characteristics, political orientation and psychological dispositions. RESULTS: Nearly 45% of participants intended to receive RSVpreF vaccine during their pregnancy, and 51% of participants intended to give their infants nirsevimab; 41% did not intend to use either product. Intention to use RSVpreF vaccine or nirsevimab was higher among those who were previously aware of the products and who viewed each product as safe, effective and important. Common reasons for hesitancy included concerns about side effects, impacts on infants and the immunizations being too new. CONCLUSIONS: Health communication interventions that increase awareness about RSV immunizations and highlight their safety, effectiveness and importance are needed to increase intended uptake.

## Pd3d12a4bc76e

- Year: 2025
- Linked people: Mark Sculpher
- Title: Development of the natural history component of an early economic model for primary sclerosing cholangitis

Abstract:

BACKGROUND: Primary sclerosing cholangitis (PSC) is a rare, chronic cholestatic disease that can progress to cirrhosis and liver failure. The natural history of PSC is variable as liver enzymes and liver symptoms fluctuate over time. Several drugs for PSC are under investigation, but there are currently no economic models to evaluate the cost-effectiveness and value of new treatments. The objective of this study was to develop an early economic model for PSC and validate the natural history component. METHODS: A lifetime horizon Markov cohort model was developed to track the progression of adults with PSC with or without inflammatory bowel disease. Based on relevant literature and clinical expert advice, fibrosis staging was used to model disease progression. Evidence on disease progression, mortality, PSC-related complications, and secondary cancers was identified by literature searches and validated by interviews with clinical and cost-effectiveness modelling experts. Model outcomes were overall survival and transplant-free survival years, and the proportions of patients receiving liver transplants, 2nd liver transplants after recurrent PSC (rPSC), and developing rPSC after liver transplantation during their lifetime. Cumulative incidence of secondary cancers and quality-adjusted life-years (QALYs) were also tracked. RESULTS: Model outcomes are in line with estimates reported in literature recommended by clinical experts. Overall survival (95% uncertainty interval [UI]) was estimated to be 25.0 (23.2-26.3) years and transplant-free survival was estimated to be 22.0 (20.2-23.6) years. The estimated proportion (95% UI) of patients receiving first liver transplants was 14.5% (11.6-17.1%), while the proportion of patients developing rPSC and receiving 2nd liver transplants after rPSC was 24.2% (20.4-28.0%) and 21.6% (12.9-29.7%), respectively. The cumulative incidence (95% UI) of cholangiocarcinoma, colorectal cancer, and gallbladder cancer were estimated at 5.2% (2.1-10.0%), 3.6% (1.4-5.4%), and 3.3% (1.2-7.6%), respectively. Discounted lifetime QALYs per patient (95% UI) were estimated at 16.4 (15.6-17.1). CONCLUSIONS: We have developed a model framework to simulate the progression of PSC with estimates of overall and transplant-free survival. This model, which calibrates well with existing estimates of disease progression, may be useful to evaluate the clinical and economic benefits of future treatments.

## P2d765b514b57

- Year: 2026
- Linked people: Katie Spencer
- Title: Patient perspectives on reirradiation for recurrent cancer, to inform future clinical trial design

Abstract:

Aims There is increasing interest in the potential benefits of reirradiation for recurrent or new primary cancers close to or within a previously irradiated region, but there is a need for high-quality studies to evaluate this approach. This study aimed to understand patient and carer perspectives regarding reirradiation, future clinical trial design, and the potential role of advanced technologies. Materials and methods Semi-structured interviews were conducted with patients who underwent reirradiation, and their carers. Patients were in follow-up and were approached about the study by their oncologist. Analysis was informed by principles of thematic analysis. Results Interviews involving 11 patients and 5 carers were conducted and analysed. Five themes were developed: 1. Considerable psychological impact from a diagnosis of recurrent cancer; 2. Influences on decision making for reirradiation; 3. Experience of reirradiation; 4. Considerations for future clinical trial design; 5. Considerations regarding advanced technologies in reirradiation. Patients and carers described the impact they had experienced from a recurrent cancer diagnosis, the strong influence of their treating oncologists on decision making regarding reirradiation, and absence of decision regret. In terms of future clinical trial design, study arms without reirradiation, especially if these contain no active treatment, may be less acceptable to patients. Some patients would be prepared to travel or temporarily relocate for reirradiation using advanced technologies such as proton beam therapy, but for others the family/social/financial impact would make this challenging. Conclusion This study has provided important insights from patients and their carers regarding reirradiation for recurrent cancer. Perspectives regarding clinical trials and advanced technologies will help to shape future study design.

## P3f6782a1b90d

- Year: 2025
- Linked people: Ernest Law
- Title: Timing of Initial Hair Regrowth and Clinical Trial-Defined Response Following Ritlecitinib Treatment in Patients With Alopecia Areata

Abstract:

Introduction: Ritlecitinib is an oral, selective, dual inhibitor of JAK3 and the TEC family kinases that was approved for treatment of severe alopecia areata (AA) in adults and adolescents aged ≥12 years in June 2023. With the recent approval of ritlecitinib, it is important to understand when patients receiving ritlecitinib can expect therapeutic benefit after initial hair regrowth. Methods: This post-hoc analysis of an integrated ALLEGRO dataset evaluated the time to clinical trial-defined scalp hair regrowth following initial signs of hair regrowth while receiving ritlecitinib. Among trial participants receiving active ritlecitinib doses (ritlecitinib 50 mg or 30 mg once daily with or without a 4-week 200 mg loading dose), we evaluated the time from initial hair regrowth, defined as Severity of Alopecia Tool change-from-baseline of 30% (SALT30) to the primary clinical trial endpoint of an absolute score of SALT ≤20. We calculated the proportion of patients who achieved SALT30 and SALT ≤20 and evaluated the time between them using Kaplan-Meier-estimated median survival time. Results were analyzed overall and by the time SALT30 was achieved: early (≤24 weeks), middle (25 to ≤48 weeks), and late (&gt;48 weeks). Results: Among 831 patients included in the analysis, 607 (73%) achieved SALT30, of whom 66% achieved SALT30 before SALT ≤20, 17% achieved both simultaneously, and 17% achieved SALT30, but not SALT ≤20. Most patients achieved SALT30 early (67%), while 19% and 14% achieved middle and late SALT30 response, respectively. Overall, the median time to SALT ≤20 after SALT30 response was 93 days. The median time to SALT ≤20 after SALT30 response was shorter in early SALT30 responders (87 days) compared with middle (170 days) or late (267 days) SALT30 responders. Conclusions: We observed a substantial amount of time passes from initial hair regrowth until trial-defined clinical response is achieved, even among patients who experienced earlier SALT30 response. These results can help inform treatment expectations and goal setting between patients and their clinicians considering ritlecitinib therapy.

## Pe3d3cca151f2

- Year: 2025
- Linked people: Sander van Kuijk
- Title: Routine mid-gestational prediction of later preeclampsia

Abstract:

Preeclampsia is thought to be superimposed upon cardiovascular and cardiometabolic risk factors, predominantly consistent with the metabolic syndrome. In this study, we developed and internally validated a prediction model for the development of later preeclampsia in pregnant women at routine second-trimester oral glucose tolerance testing. Data were collected during a prospective clinical cohort study, including pregnant women undergoing routine gestational diabetes mellitus (GDM) screening. Routine clinical data during the GDM screening (e.g., oral glucose tolerance test) were considered as potential predictors. Univariable and multivariable logistic regression with Backward Wald elimination were performed to develop the prediction model. Internal validation was performed using bootstrapping. Predictive performance of the final model was evaluated in terms of discrimination and calibration, both before and after adjusting for overfitting. Of 3227 pregnant women undergoing GDM screening, 137 (4.2 %) subsequently developed preeclampsia. The final prediction model included obstetric history of preeclampsia (yes/no), history of large for gestational age (yes/no), current antihypertensive drug use (yes/no), diastolic blood pressure (mmHg), fasting serum creatinine (μmol/l), fasting serum triglycerides (mmol/l), and urinary protein-creatinine ratio (g/mol creatinine). The area under the receiver operating characteristic curve of the model was 0.79 before and after internal validation, with good model calibration. Upon external validation and impact analysis, the proposed second-trimester preeclampsia prediction model enables accurate estimation of individuals risk on predominantly later third trimester development of preeclampsia. The model could facilitate timely, tailored monitoring and early intervention among pregnant women at risk to improve pregnancy outcomes.

## P9d3cd8716be4

- Year: 2025
- Linked people: Carlos Wong
- Title: Parental depression in the relationship between parental stress and child health among low-income families in Hong Kong

Abstract:

INTRODUCTION: Low-income families face increased exposure to stressors, including material hardship and limited social support, which contribute to poor health outcomes. The poor health and behavioural problems in children from these families may exacerbate parental stress. This study explored the bidirectional relationship between parental stress and child health, along with its mediators and moderators, among low-income families in Hong Kong. METHODS: In total, 217 families were recruited from two less affluent communities between 2016 and 2017; they were followed up at 12 and 24 months. Each parent-child pair was assessed using parent-completed questionnaires on socio-demographics, medical history, parental stress, health-related quality of life, child health and behaviour, family harmony, parenting style, and neighbourhood cohesion. RESULTS: Thirty-eight parents (17.5%) reported significantly higher levels of stress than the control group. These individuals were more likely to be single parents (41.2% vs 18.5%), victims of intimate partner abuse (23.7% vs 10.9%), have a household income below 50% of the Hong Kong population median (50.0% vs 29.9%), and be diagnosed with mental illnesses (23.7% vs 5.1%). A bidirectional inverse relationship was observed between parental stress and child health at respective time points, with cross-effects from baseline child health to later parental stress, and from baseline parental stress to later child health. The relationship was mediated by the level of parental depression. CONCLUSION: Parental stress both precedes and results from child health and behavioural problems, with reciprocal short-term and long-term effects. Screening and intervention for parental depression are needed to mitigate the impacts of stress on health among parents and children.

## P4c11d924c70f

- Year: 2026
- Linked people: Ilias Goranitis, Tianxin Pan
- Title: Public Preferences and Willingness to Pay for a Multidisciplinary Colorectal and Pelvic Reconstruction Service.

Abstract:

Children with congenital colorectal conditions require care from multiple health professionals. However, evidence on the value of a multidisciplinary care model is lacking. This study aimed to elicit public preferences and willingness to pay for a multidisciplinary care model for children with congenital colorectal conditions.
We developed a discrete choice experiment (DCE) that was administered to 807 members of the Australian public online. A Bayesian D-efficient design consisting of 20 choice tasks was split into 2 blocks of 10 choice tasks per respondent. Five attributes elicited through mixed methods included make-up of the multidisciplinary team; responsibility for care coordination; duration of access; provision of educational information; and cost. Choice data were analysed with a panel error component mixed logit model. Willingness to pay for each DCE attribute and level was estimated using the unconditional population moments estimates.
The Australian public demonstrated preference for a multidisciplinary care model. They showed preference for long-term access, having a care coordinator and provision of additional information. The public was willing to pay Australian dollars (AU) $64,275 for a multidisciplinary care model comprising an essential multidisciplinary team (including a surgeon, clinical nurse consultants, a psychologist, a social worker, stomal therapists, a child life therapist and a dietitian) with care coordination and information booklets and ongoing care until the child reached adulthood. We observed preference heterogeneity associated with gender, parenthood status and household income.
The Australian public valued the multidisciplinary care model for children with complex colorectal conditions. Our findings can be used to inform the design of a multidisciplinary care model and to inform cost-benefit analyses as part of broader healthcare system implementation.

## Pf9cffda8a842

- Year: 2025
- Linked people: Irina Kinchin
- Title: Healthcare pathways and social experiences of Lewy body dementia and Alzheimer's disease in Ireland

Abstract:

OBJECTIVE: This study examines how social and healthcare structures in Ireland shape the experiences of individuals diagnosed with Lewy body dementia (LBD) and Alzheimer's disease (AD), with particular attention to diagnostic pathways, care access, and social constructions of dementia. METHODS: Twenty-three participants with mild to moderate dementia resulting from LBD (n = 12) and AD (n = 11) participated in in-depth interviews between September 2022 and February 2023. Using a descriptive phenomenological approach informed by social constructivist perspectives, interviews were analysed to understand how institutional, geographical, and social factors influence experiences of diagnosis, post-diagnostic support, and public awareness. RESULTS: Healthcare structures and social understanding of dementia created divergent experiences for individuals with LBD and AD. While AD participants generally encountered established diagnostic pathways aligned with dominant cultural understanding of dementia as memory loss, LBD participants faced structural barriers due to complex symptomatology and limited specialist knowledge. Geographic inequalities in accessing specialised diagnostic services particularly affected rural LBD participants. Post-diagnosis, LBD participants encountered greater institutional barriers in accessing appropriate support, reflecting systemic gaps in service provision. Both groups highlighted how societal misconceptions about dementia shaped their lived experiences, with LBD participants particularly affected by the cultural dominance of the Alzheimer's narrative. CONCLUSION: This study demonstrates how social structures, healthcare systems, and cultural understandings of dementia create inequitable experiences for individuals with different forms of dementia in Ireland. Findings highlight the need for structural changes in healthcare delivery, increased professional education about LBD, and broader societal awareness to address these disparities.

---
project_id: "1719-RA"
work_id: "doi:10.1007/s11136-026-04226-8"
doi: "10.1007/s11136-026-04226-8"
pmid: "41920383"
pmcid: "PMC13043573"
title: "Psychometric validation of a cognition and social participation bolt-on for the EQ-5D-5L in SARS-CoV-2 infected German healthcare workers"
journal: "Quality of Life Research"
publication_date: "2026-04-01"
volume: "35"
issue: "5"
authors:
  - name: "Ines Buchholz"
    affiliation_ids:
      - "Aff1"
  - name: "Laura Lüdtke"
    affiliation_ids:
      - "Aff1"
  - name: "Martin Härter"
    affiliation_ids:
      - "Aff1"
  - name: "M F Bas Janssen"
    affiliation_ids:
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "Department of Medical Psychology, Institute for Psychotherapy, University Medical Center Hamburg-Eppendorf, Hamburg, Germany"
  - id: "Aff2"
    name: "Maths in Health, Klimmen, The Netherlands"
licence: "cc-by"
source_file: "input/projects/1719-RA/papers/doi_10.1007_s11136-026-04226-8.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13043573/fullTextXML"
source_method: "epmc_xml"
source_sha256: "b3f88161972ef2982cb616a02b9371aeae870735038571402fdc3b6bd96df936"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Psychometric validation of a cognition and social participation bolt-on for the EQ-5D-5L in SARS-CoV-2 infected German healthcare workers

## Abstract

### Purpose

COVID-19 can result in long-term impairments, including cognitive difficulties and restrictions in social participation, which may not be fully captured by EQ-5D-5L. This study examined whether adding cognition (CO) and social participation (SP) bolt-ons improves EQ-5D-5L’s measurement properties in German healthcare workers (HCW) with SARS-CoV-2 infection.

### Methods

N = 3335 HCW with self-reported occupational COVID-19 completed an online survey including EQ-5D-5L, two candidate bolt-ons (CO, SP), and validated self-report instruments (e.g., Post-COVID Syndrome PCS-Score, PHQ-4, PTSD screening, SSD-12, WAI, WHODAS). Psychometric analyses covered distributional characteristics (response pattern, missing values, ceiling), construct (convergent and divergent) validity, known-groups validity, and explanatory power.

### Results

Both bolt-ons showed acceptable distributional properties; adding CO modestly reduced overall ceiling effect, while adding SP resulted in negligible change (‘11111’ = 18.8% vs. ‘111111’<sub>CO</sub> = 14.8% and ‘111111’<sub>SP</sub> = 17.8%). Construct validity was supported by expected correlation patterns, i.e. r<sub>CO,PCS-Score</sub> = 0.63, r<sub>SP, WHODAS</sub> = 0.71. Known-groups validity improved with the inclusion of bolt-ons, as reflected by higher or comparable relative efficiency (RE) compared with EQ-5D-5L in most group comparisons for CO (11/13, RE = 0.94–1.22), whereas this was observed in approximately half of group comparisons for SP (6/13, RE = 0.89–1.18). In multivariate models, adding CO to the EQ-5D-5L resulted in a small to moderate increase in explained variance for PCS symptom severity (Δ adj. R<sup>2</sup><sub>CO</sub> = 0.04–0.07), whereas adding SP had a negligible impact (Δ adj. R<sup>2</sup><sub>SP</sub> ≤ 0.01).

### Conclusion

While CO improved ceiling, construct, and known-groups validity of the EQ-5D-5L in SARS-CoV-2 infected HCW, the added value of SP appeared limited.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-026-04226-8.

**Keywords:** Quality of life, Healthcare workers, EQ-5D-5L, Psychometrics, Cognition, Social participation, Germany

Received 2025 Jun 15; Accepted 2026 Mar 9; Issue date 2026.

## Introduction

The EQ-5D-5L is a widely used instrument for measuring health-related quality of life (HRQoL). It assesses five domains on a five-level severity-scale, providing a standardized and simple approach to compare health status across populations and diseases \[1\]. Its brevity and generic nature have contributed to its extensive use in health technology assessment and outcome research.

Despite these strengths, the EQ-5D-5L may incompletely capture condition-specific aspects of health, such as cognitive and psychosocial functioning \[2–10\]. To address these limitations, supplementary "bolt-on" dimensions have been proposed and increasingly studied, targeting health aspects not covered by the core domains \[11–17\].

The COVID-19 pandemic has highlighted the relevance of such extensions. Many individuals experience ongoing symptoms after acute infection, referred to as Long COVID (4–12 weeks) or Post-COVID-Syndrome (PCS, \> 12 weeks) \[18, 19\], including symptoms like fatigue, cognitive difficulties, respiratory problems, and sequelae liked reduced social and occupational functioning \[20–23\]. Cognitive problems—such as memory issues, attention deficits, and slowed processing—are prominent among persons with PCS and can negatively affect mental health, work performance, and social participation \[24, 25\]. Emerging longitudinal evidence from the Norwegian adult population indicate that individuals who had COVID-19 reported poorer social participation on PROMIS-29 compared with pre-pandemic levels, exceeding minimal important change thresholds. Interestingly, respondents whose family or partner had COVID-19 also reported poorer outcomes in anxiety and social participation, suggesting broader social and relational impacts of the pandemic \[25\]. About 9 months into the pandemic, EQ-5D-5L and PROMIS-29 scores showed slightly poorer overall health compared with 1 year earlier, highlighting that even in general population samples social participation may be particularly affected. These findings underscore the relevance of including social participation alongside cognition as bolt-ons to capture the broader functional impact of PCS.

During the COVID-19 pandemic, the EQ-5D-5L was extensively used to monitor population health, evaluate health inequalities, and generate utility values for economic evaluations \[20, 25–33\]. However, most studies focused on general population samples or non-COVID-specific cohorts. A systematic review and meta-analysis of nearly 200 EQ-5D studies demonstrated a substantial reduction in HRQoL among COVID-19 patients, with pain/discomfort and anxiety/depression as the most affected domains \[34\]. Risk factors for lower HRQoL included older or younger age, female gender, disease severity, comorbidities, and post-COVID symptoms \[25, 34\].

Longitudinal evidence from the CORona Follow-Up study shows that a substantial proportion of former COVID-19 patients reported persistent symptoms 24 months post-infection, accompanied by reduced HRQoL, as reflected by lower EQ-5D-5L, EQ VAS and health utility scores compared with non-infected controls \[20\]. Janols et al. (2024) demonstrated in Swedish post-COVID patients that the EQ-5D-5L partly captures fatigue and memory/concentration problems but poorly reflects dyspnea, and that adding symptom-specific bolt-ons enhances the explained variance of overall HRQoL \[35\].

Healthcare workers (HCW) are a particularly relevant group. High occupational exposure, sustained workload, and psychosocial stress during the pandemic increase the risk of SARS-CoV-2 and post-COVID sequelae \[36, 37\]. In Germany, approximately 6.1 million individuals—around 13% of the workforce—are employed in the healthcare sector \[38\]. Alongside high infection rates \[39\], European studies report persistent psychological, cognitive and functional burden among HCW during and after the pandemic, including elevated levels of depression, anxiety, stress, and reduced work functioning \[40–43\]. In the context of post-COVID conditions, these sustained demands may translate into persistent cognitive impairments and restrictions in social participation with direct implications for daily functioning and work ability, and direct relevance for HRQoL assessment. These characteristics make HCW a key population for evaluating whether extended HRQoL instruments better capture post-COVID–related health deficits.

Against this background, this study aimed to evaluate the psychometric properties of the EQ-5D-5L with and without a cognition and a social participation bolt-on in a randomly selected cohort of German HCW who acquired SARS-CoV-2 infection at work.

## Methods

### Data collection and study population

This secondary data analysis used cross-sectional data from an online survey (REDCap) funded by the Federal Ministry of Education and Research (funding code: 01EP2110A). The original study aimed to examine the prevalence of COVID-19 symptoms and Post-COVID Syndrome (PCS) in German HCW. More information about the study design can be found in the study protocol \[44, 45\].

The initial study sample included 20,000 HCW in Germany with confirmed SARS-CoV-2 infection during occupational exposure, randomly selected from a population of approximately 120,000 HCW by the employer’s liability insurance association (German statutory accident insurance provider for non-state institutions within the health and welfare service sectors, Berufsgenossenschaft für Gesundheitsdienst und Wohlfahrtspflege, BGW). Inclusion criteria required participants to be HCW in regular contact with patients, insured by the BGW, with a confirmed SARS-CoV-2 infection (positive PCR test) before February 14, 2023. The present analyses are based exclusively on data collected at baseline from subjects with a confirmed SARS-CoV-2-infection (positive PCR-Test).

### Outcome measures

Data was collected using validated German self-report measures (for the entire survey instrument please see \[45\]). Questionnaires were presented in a fixed order. For sample characterization, sociodemographic information, such as age, sex, marital status, education, employment, occupation, course and intensity of symptoms were assessed. This study used the data collected with the following questionnaires:

### Brief resilience scale

The Brief Resilience Scale (BRS) is a validated 6-item self-report measure designed to assess an individual's ability to recover from stress. Items are rated on a 5-point Likert scale, with higher scores indicating greater resilience.

### EQ-5D-5L and bolt-ons

The EQ-5D-5L includes a descriptive system comprising five health dimensions (mobility (MO), self-care (SC), usual activities (UA), pain/discomfort (PD), anxiety/depression (AD)) each rated on a 5-point severity scale ranging from *no problems* (1) to *extreme problems/unable to* (5), and a vertical visual analogue scale (EQ VAS), on which respondents rate their overall health from 0 (*the worst health you can imagine*) to 100 (*the best health you can imagine*). Responses from the five dimensions can be combined into a 5-digit health string, where ‘11111’ represents the best possible health profile, and ‘55555’ represents the worst.

The EQ-5D-5L was administered last, followed by two bolt-ons—cognition (CO) and social participation (SP)—and the EQ VAS.

The bolt-ons are not formally part of the EQ-5D descriptive system; their use and translation from English into German were approved by EuroQol Research Foundation. The English and German item wordings are provided in Supplementary Material <a href="#MOESM1" data-ref-type="supplementary-material">1</a>.

Bolt-ons were selected using a symptom-guided, literature-based approach in line with current EQ-5D bolt-on recommendations \[11\].

Cognition was included because cognitive problems are among the most common long-term sequelae of COVID-19 \[20\] and seem to be insufficiently captured by the core EQ-5D-5L \[35\]. It is also the earliest \[10\] and most frequently tested bolt-on in empirical EQ-5D research, with applications targeting diverse item formulations (e.g., concentration, memory, and thinking ability) across diverse populations \[16\].

SP was selected to capture pandemic-related social and occupational limitations, which have been shown to affect HRQoL, and to be associated with psychological distress and fatigue \[46\]. Among the various social domain bolt-ons described in the literature \[6, 7, 17, 47, 48\], this item focuses on participation in social life rather than interpersonal relationships alone \[30\], aligning with functional impairments commonly reported after COVID-19.

Both bolt-ons were previously applied in the POPCORN study, one of the first studies employing EQ-5D bolt-ons in a COVID-19 context \[30\]. They had a single-item format with a recall period of 3 months; the response format followed the structure of the EQ-5D-5L descriptive system. As the term ‘cognition’ is more used in a scientific context than in everyday German language, examples and explanations from the POPCORN study \[30\] and Finch et al. (2021) were provided in parenthesis following the dimension title to enhance comprehension and completion \[11\].

To avoid redundancy and respondent burden, no additional EQ-5D-5L bolt-ons addressing other key post-COVID symptoms such as fatigue or respiratory problems were included, as these were assessed using the Post-COVID Syndrome (PCS) severity score.

### PCS – severity of post COVID syndrome

The Post-COVID Syndrome PCS-Score is a symptom-based severity classification tool designed to quantify the extent of long-term symptoms following COVID-19 infection \[49\]. It comprises 12 symptom complexes, including fatigue, neurological issues, sleep disturbances, and musculoskeletal pain, among others. Each symptom complex is assessed through binary items and weighted (2–7 points) based on clinical relevance. As respondents first indicate the presence of a symptom (no/yes, corresponding to EQ-5D-5L level 1 vs. ≥ 2), followed by severity levels that are conceptually aligned with EQ-5D-5L levels 2–5, the items can be considered “bolt-on-like” measures tailored to the post-COVID population.

### German version of the moral injury symptom and support scale for health professionals (G-MISS-HP)

The G-MISS-HP is a German version of the MISS-HP, measuring moral injury and related impairment in healthcare professionals, capturing distress from perceived moral value violations at work with 11 items on a 10-point Likert scale \[50, 51\].

### PHQ-4 – anxiety and depression

The Patient Health Questionnaire-4 (PHQ-4) is a brief screening tool consisting of four items to assess symptoms of depression and anxiety \[52\]. Each symptom is rated on a 4-point frequency scale (*0* = *not at all, 1* = *several days, 2* = *more than half the days, 3* = *nearly every day*). The total score ranges from 0 to 12, with a score of 5 or higher indicating the potential presence of clinical anxiety or depression \[53\].

### SSD-12 – symptom-related thoughts, feelings, and behaviours

The Somatic Symptom Disorder–B Criteria Scale (SSD-12) \[54–56\] is a 12 item self-report instrument based on DSM-5 criteria, assessing cognitive, emotional, and behavioural aspects of somatic symptom disorder on a 5-point frequency scale from 0 (“*never*”) to 4 (“*very often*”), yielding a total score from 0 to 48.

### Short screening scale for DSM IV posttraumatic stress disorder

The Short Screening Scale for DSM-IV Posttraumatic Stress Disorder (PTSD) is a brief diagnostic tool designed to identify individuals with PTSD based on DSM-IV criteria, with scores ≥ 4 indicating probable PTSD \[57\].

### WHODAS 2.0

The WHO Disability Assessment Schedule 2.0 (WHODAS 2.0), assesses functioning and disability over the past 30 days across six domains using a 5-point Likert scale \[58\]. Based on the International Classification of Functioning, Disability and Health (ICF), it enables cross-cultural comparisons of health and disability. This study used the 12-item short version.

### Work ability index (WAI)

The Work Ability Index is a 24-item self-assessment tool designed to evaluate a person’s capacity to meet current and future work demands across seven dimensions \[59, 60\]: current work ability compared with lifetime best, work ability in relation to job demands, number of diseases (assessed using a 14-category disease list indicating physician- or self-diagnosed conditions and whether they existed prior to the first SARS-CoV-2 infection), work impairment due to diseases, sickness absence during the past year, own prognosis of work ability in 2 years, and mental resources. It is widely used to identify risks for reduced work ability and to guide preventive measures in occupational health.

### Statistical analysis

We followed the analytical framework used in previous studies to test the distributional properties, convergent and divergent validity, known-groups validity, and explanatory power of bolt-ons \[12\]. Psychometric properties were first assessed for the EQ-5D-5L, followed by the EQ-5D-5L with added bolt-on(s). Socio-demographic, occupational, and health-related characteristics of the baseline population are presented. All analyses were performed using Stata 18.5.

### Distributional properties

For each EQ-5D-5L item and bolt-on, we analysed the number and proportion of missing values (feasibility) and the response distribution across the five levels to confirm relevance and endorsement of all levels. Stratified analyses were also conducted by PCS severity. Missing values were not imputed for subsequent analyses. To ensure that the EQ-5D-5L items and the bolt-ons were able to detect differences at the upper end of the scale, we examined (i) the proportion of respondents reporting *"no problems"* (level 1) on each EQ-5D-5L dimension and bolt-on item separately (item-level ceiling), and (ii) the proportion reporting *"no problems"* across all dimensions of the EQ-5D-5L (‘11111’) and the EQ-5D-5L + each bolt-on item (‘111111’) combined (profile-level ceiling). The frequency of persons reporting “*no problems*” on each EQ-5D-5L item but any problems on the bolt-on was examined using cross-tabulations.

### Convergent and divergent validity

To investigate construct validity, Spearman’s correlation coefficients were calculated between bolt-on items and the EQ-5D-5L items, the EQ VAS, and relevant scores or items of other measures, including BRS, G-MISS-HP, PCS-Score, PHQ-4, Short Screening Scale for PTSD, SSD-12, WAI and WHODAS. For scores and items targeting related constructs (convergent) such as EQ-5D-5L dimension anxiety/depression and PHQ-4, we expected at least moderate correlations (r = 0.40–0.59); for those who measure unrelated constructs (divergent validity) such as EQ-5D-5L dimension mobility and PHQ-4 weak (r=0.2– \< 0.4) to no correlations according to available guidelines \[61\].

### Discriminative (known groups) validity

Known-groups validity was examined using an anchor-based approach, comparing mean level sum scores (LSS; transformed to a 0–100 scale \[62\]) for the EQ-5D-5L alone and with bolt-ons across externally defined subgroups based on clinical and other indicators (e.g., physician-diagnosed post-COVID condition, number of sick leave days, PHQ-4). Clinically meaningful groups were defined using established cut-offs from the literature. Symptoms of anxiety and depression were categorized using the PHQ-4 \[52\] as normal (0–2), mild (3–5), moderate (6–8), and severe (9–12). Somatic symptom burden was assessed with the SSD-12 \[63–65\]; in the face of lacking recommended thresholds, previously applied cut-offs derived from primary care and population-based studies were used (SSD-12 \< 13 vs. ≥ 13). These cut-offs were analyzed both alone and in combination with PHQ-4 severity (PHQ-4 \< 8 and SSD-12 \< 13 vs. PHQ-4 ≥ 8 and SSD-12 ≥ 13). Post-COVID symptom severity was defined using the PCS-Score \[49\] as no (0 points), mild (0.01–10.75), moderate (10.76–26.25), and severe (\> 26.25). A positive screen for post-traumatic stress disorder was defined as a score ≥ 4 on the short Screening Scale for DSM IV PTSD \[57\]. Work ability, assessed with the WAI, was categorized as excellent (44–49), good (37–43), moderate (28–36), or low (7–27) \[66\].

We hypothesized that adding bolt-ons would improve the EQ-5D-5L's ability to distinguish between groups expected to differ on relevant constructs. Known-group validity was evaluated using relative efficiency (RE), defined as the ratio of F-statistics for multi-group comparisons or squared t-statistics for binary comparisons, with the EQ-5D-5L without bolt-ons as the reference. Statistical significance of changes in discriminatory ability was assessed using 95% bootstrap confidence intervals based on 3000 replications, following \[67\].

### Explanatory power

Linear regression models were used to assess the explanatory power of EQ-5D-5L dimensions with and without bolt-ons in explaining variance in the severity of self-reported post-COVID symptoms with the baseline PCS-Score and the baseline EQ VAS score as dependent variables and the EQ-5D-5L and bolt-on items as predictors.

Explanatory power refers to how well the EQ-5D-5L dimensions and bolt-ons account for variability in the respective outcome measure in a multivariable context. Analyses were run using the total sample and subsamples of the most prevalent health conditions, defined as more than n = 200 cases self-reporting a diagnosis in WAI.

The same modelling approach was applied using EQ VAS, PHQ-4, SSD-12, and WAI as dependent variables in the total sample to investigate whether EQ-5D-5L dimensions with and without bolt-ons capture constructs beyond overall self-rated health as measured by EQ VAS.

Univariable models were estimated for descriptive purposes only. The primary analyses focused on multivariable models including all EQ-5D-5L dimensions, with adjusted R<sup>2</sup> and incremental R<sup>2</sup> (Δ adjusted R<sup>2</sup>) used to quantify the additional explanatory value of bolt-ons beyond the core EQ-5D-5L.

## Results

### Study population

A total of n = 3335 individuals (mean age: 50.8 years; 85.6% female) completed the assessment (Table <a href="#Tab1" data-ref-type="table">1</a>). About one-third (33.3%) of participants were in the age group of 50–59 years. Most participants were care staff/nurses (73.3%), with 44.6% working full-time and 46% part-time. The majority had no migration experience (87.4%), 40% held a German high school or university of applied sciences entrance qualification, and 58.9% reported two or more infections.

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of the patient population

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variables<sup>1</sup></th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Total sample</td>
<td style="text-align: left;">3335</td>
<td style="text-align: center;">100.0</td>
</tr>
<tr>
<td style="text-align: left;">Female sex</td>
<td style="text-align: left;">2852</td>
<td style="text-align: center;">85.6</td>
</tr>
<tr>
<td style="text-align: left;">Age (years), mean ± sd (min–max)</td>
<td colspan="2" style="text-align: left;">50.8 ± 11.4 (19–83)</td>
</tr>
<tr>
<td style="text-align: left;">  20–29</td>
<td style="text-align: left;">192</td>
<td style="text-align: center;">5.8</td>
</tr>
<tr>
<td style="text-align: left;">  30–39</td>
<td style="text-align: left;">430</td>
<td style="text-align: center;">12.9</td>
</tr>
<tr>
<td style="text-align: left;">  40–49</td>
<td style="text-align: left;">706</td>
<td style="text-align: center;">21.3</td>
</tr>
<tr>
<td style="text-align: left;">  50–59</td>
<td style="text-align: left;">1114</td>
<td style="text-align: center;">33.6</td>
</tr>
<tr>
<td style="text-align: left;">  60 + </td>
<td style="text-align: left;">876</td>
<td style="text-align: center;">26.4</td>
</tr>
<tr>
<td style="text-align: left;">Occupation (professional group)</td>
<td colspan="2" style="text-align: left;">3333</td>
</tr>
<tr>
<td style="text-align: left;">  Care staff/nurse</td>
<td style="text-align: left;">2442</td>
<td style="text-align: center;">73.3</td>
</tr>
<tr>
<td style="text-align: left;">  Physician</td>
<td style="text-align: left;">315</td>
<td style="text-align: center;">9.5</td>
</tr>
<tr>
<td style="text-align: left;">  Therapeutical staff/therapist</td>
<td style="text-align: left;">203</td>
<td style="text-align: center;">6.1</td>
</tr>
<tr>
<td style="text-align: left;">  Advisor</td>
<td style="text-align: left;">20</td>
<td style="text-align: center;">0.6</td>
</tr>
<tr>
<td style="text-align: left;">  Other</td>
<td style="text-align: left;">353</td>
<td style="text-align: center;">10.6</td>
</tr>
<tr>
<td style="text-align: left;">Current working situation</td>
<td colspan="2" style="text-align: left;">2969</td>
</tr>
<tr>
<td style="text-align: left;">  Full-time employed</td>
<td style="text-align: left;">1323</td>
<td style="text-align: center;">44.6</td>
</tr>
<tr>
<td style="text-align: left;">  Part-time employed</td>
<td style="text-align: left;">1365</td>
<td style="text-align: center;">46.0</td>
</tr>
<tr>
<td style="text-align: left;">  Working in marginal employment/on an hourly basis</td>
<td style="text-align: left;">56</td>
<td style="text-align: center;">1.9</td>
</tr>
<tr>
<td style="text-align: left;">  In reintegration</td>
<td style="text-align: left;">34</td>
<td style="text-align: center;">1.2</td>
</tr>
<tr>
<td style="text-align: left;">  Unemployed</td>
<td style="text-align: left;">72</td>
<td style="text-align: center;">2.4</td>
</tr>
<tr>
<td style="text-align: left;">  Retired</td>
<td style="text-align: left;">119</td>
<td style="text-align: center;">4.0</td>
</tr>
<tr>
<td style="text-align: left;">Living situation</td>
<td colspan="2" style="text-align: left;">2969</td>
</tr>
<tr>
<td style="text-align: left;">  Alone</td>
<td style="text-align: left;">474</td>
<td style="text-align: center;">16.0</td>
</tr>
<tr>
<td style="text-align: left;">  With others</td>
<td style="text-align: left;">2495</td>
<td style="text-align: center;">84.0</td>
</tr>
<tr>
<td style="text-align: left;">Migration experience</td>
<td colspan="2" style="text-align: left;">2971</td>
</tr>
<tr>
<td style="text-align: left;">  No</td>
<td style="text-align: left;">2607</td>
<td style="text-align: center;">87.4</td>
</tr>
<tr>
<td style="text-align: left;">  Yes, I myself (1<sup>rst</sup> generation)</td>
<td style="text-align: left;">276</td>
<td style="text-align: center;">9.3</td>
</tr>
<tr>
<td style="text-align: left;">  Yes, at least one parent has migration experience</td>
<td style="text-align: left;">99</td>
<td style="text-align: center;">3.3</td>
</tr>
<tr>
<td style="text-align: left;">Highest level of education</td>
<td colspan="2" style="text-align: left;">3000</td>
</tr>
<tr>
<td style="text-align: left;">  Higher education entrance qualification</td>
<td style="text-align: left;">1198</td>
<td style="text-align: center;">40.0</td>
</tr>
<tr>
<td style="text-align: left;">  German intermediate school certificate</td>
<td style="text-align: left;">1426</td>
<td style="text-align: center;">47.5</td>
</tr>
<tr>
<td style="text-align: left;">  Other</td>
<td style="text-align: left;">376</td>
<td style="text-align: center;">12.5</td>
</tr>
<tr>
<td style="text-align: left;">Size of residence</td>
<td colspan="2" style="text-align: left;">2.959</td>
</tr>
<tr>
<td style="text-align: left;">   &lt; 1.000 inhabitants</td>
<td style="text-align: left;">430</td>
<td style="text-align: center;">14.5</td>
</tr>
<tr>
<td style="text-align: left;">  Up to 10.000</td>
<td style="text-align: left;">963</td>
<td style="text-align: center;">32.5</td>
</tr>
<tr>
<td style="text-align: left;">  Up to 35.000</td>
<td style="text-align: left;">613</td>
<td style="text-align: center;">20.7</td>
</tr>
<tr>
<td style="text-align: left;">  Up to 100.000</td>
<td style="text-align: left;">396</td>
<td style="text-align: center;">13.4</td>
</tr>
<tr>
<td style="text-align: left;">   &gt; 100.000</td>
<td style="text-align: left;">557</td>
<td style="text-align: center;">18.8</td>
</tr>
<tr>
<td style="text-align: left;">Number of infections</td>
<td colspan="2" style="text-align: left;">3331</td>
</tr>
<tr>
<td style="text-align: left;">  1</td>
<td style="text-align: left;">1368</td>
<td style="text-align: center;">41.1</td>
</tr>
<tr>
<td style="text-align: left;">  2</td>
<td style="text-align: left;">1581</td>
<td style="text-align: center;">47.5</td>
</tr>
<tr>
<td style="text-align: left;">   ≥ 3</td>
<td style="text-align: left;">382</td>
<td style="text-align: center;">11.5</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS (0–100), mean ± sd</td>
<td style="text-align: left;">n = 2934, 71.1 ± 20.0</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

<sup>1</sup>n (number of cases) and % (percent), otherwise reported; sd, standard deviation

</div>

### Feasibility and distribution properties

Table <a href="#Tab2" data-ref-type="table">2</a> presents the response distribution and proportion of missing values for the EQ-5D-5L dimensions and bolt-on items. Respondents without any item responses (n = 234) were excluded from analyses, assuming survey break-off. Among the remaining respondents, missing values ranged from 0.4% to 0.6% for the EQ-5D-5L dimensions and bolt-ons. Missing values for the EQ VAS were approximately 5% (n = 167). Regarding the response distribution, the proportion of respondents reporting *no problems* ranged from 27.4% for PD to 92.7% for SC. The proportion reporting *severe* or *extreme problems* was generally low (\< 10%), with the highest rates observed for CO (9.3%), followed by PD (8.6%).

<div id="Tab2" class="table-wrap">

<div class="caption">

Feasibility and distribution of EQ-5D-5L and bolt-on item responses in the total sample

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Missing values<sup>1</sup></th>
<th colspan="2" style="text-align: left;">No problems</th>
<th colspan="2" style="text-align: left;">Slight problems</th>
<th colspan="2" style="text-align: left;">Moderate problems</th>
<th colspan="2" style="text-align: left;">Severe problems</th>
<th colspan="2" style="text-align: left;">Extreme problems/unable to</th>
<th colspan="2" style="text-align: left;">Full health<sup>2</sup></th>
</tr>
<tr>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="15" style="text-align: left;">EQ-5D items</td>
</tr>
<tr>
<td style="text-align: left;">  Mobility</td>
<td style="text-align: left;">12</td>
<td style="text-align: center;">0.4</td>
<td style="text-align: left;">1.718</td>
<td style="text-align: center;">55.6</td>
<td style="text-align: left;">712</td>
<td style="text-align: center;">23.1</td>
<td style="text-align: left;">477</td>
<td style="text-align: center;">15.4</td>
<td style="text-align: left;">176</td>
<td style="text-align: center;">5.7</td>
<td style="text-align: left;">6</td>
<td style="text-align: center;">0.2</td>
<td rowspan="5" style="text-align: left;">571</td>
<td rowspan="5" style="text-align: left;">18.8</td>
</tr>
<tr>
<td style="text-align: left;">  Self-care</td>
<td style="text-align: left;">12</td>
<td style="text-align: center;">0.4</td>
<td style="text-align: left;">2.862</td>
<td style="text-align: center;">92.7</td>
<td style="text-align: left;">151</td>
<td style="text-align: center;">4.9</td>
<td style="text-align: left;">52</td>
<td style="text-align: center;">1.7</td>
<td style="text-align: left;">16</td>
<td style="text-align: center;">0.5</td>
<td style="text-align: left;">8</td>
<td style="text-align: center;">0.3</td>
</tr>
<tr>
<td style="text-align: left;">  Usual activities</td>
<td style="text-align: left;">14</td>
<td style="text-align: center;">0.4</td>
<td style="text-align: left;">1.640</td>
<td style="text-align: center;">53.1</td>
<td style="text-align: left;">834</td>
<td style="text-align: center;">27.0</td>
<td style="text-align: left;">434</td>
<td style="text-align: center;">14.0</td>
<td style="text-align: left;">161</td>
<td style="text-align: center;">5.2</td>
<td style="text-align: left;">18</td>
<td style="text-align: center;">0.6</td>
</tr>
<tr>
<td style="text-align: left;">  Pain/discomfort</td>
<td style="text-align: left;">20</td>
<td style="text-align: center;">0.6</td>
<td style="text-align: left;">845</td>
<td style="text-align: center;">27.4</td>
<td style="text-align: left;">845</td>
<td style="text-align: center;">37.7</td>
<td style="text-align: left;">811</td>
<td style="text-align: center;">26.3</td>
<td style="text-align: left;">230</td>
<td style="text-align: center;">7.5</td>
<td style="text-align: left;">33</td>
<td style="text-align: center;">1.1</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression</td>
<td style="text-align: left;">18</td>
<td style="text-align: center;">0.5</td>
<td style="text-align: left;">1519</td>
<td style="text-align: center;">49.3</td>
<td style="text-align: left;">1519</td>
<td style="text-align: center;">29.1</td>
<td style="text-align: left;">488</td>
<td style="text-align: center;">15.8</td>
<td style="text-align: left;">153</td>
<td style="text-align: center;">5.0</td>
<td style="text-align: left;">25</td>
<td style="text-align: center;">0.8</td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Bolt-ons</td>
</tr>
<tr>
<td style="text-align: left;">  Cognition</td>
<td style="text-align: left;">19</td>
<td style="text-align: center;">0.6</td>
<td style="text-align: left;">1088</td>
<td style="text-align: center;">35.3</td>
<td style="text-align: left;">1170</td>
<td style="text-align: center;">37.9</td>
<td style="text-align: left;">538</td>
<td style="text-align: center;">17.5</td>
<td style="text-align: left;">234</td>
<td style="text-align: center;">7.6</td>
<td style="text-align: left;">52</td>
<td style="text-align: center;">1.7</td>
<td style="text-align: left;">450</td>
<td style="text-align: left;">14.8</td>
</tr>
<tr>
<td style="text-align: left;">  Social participation</td>
<td style="text-align: left;">17</td>
<td style="text-align: center;">0.5</td>
<td style="text-align: left;">1780</td>
<td style="text-align: center;">57.7</td>
<td style="text-align: left;">694</td>
<td style="text-align: center;">22.5</td>
<td style="text-align: left;">381</td>
<td style="text-align: center;">12.4</td>
<td style="text-align: left;">185</td>
<td style="text-align: center;">6.0</td>
<td style="text-align: left;">44</td>
<td style="text-align: center;">1.4</td>
<td style="text-align: left;">540</td>
<td style="text-align: left;">17.8</td>
</tr>
<tr>
<td style="text-align: left;">  EQ VAS</td>
<td style="text-align: left;">167</td>
<td style="text-align: center;">5.0</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">1.7</td>
</tr>
</tbody>
</table>

<sup>1</sup>Individuals who did not answer any of the EQ-5D-5L items (n = 234) were excluded from missingness analysis

<sup>2</sup>EQ-5D-5L (‘11111’) (+ bolt-on) or EQ VAS = 100, respectively

</div>

Among respondents reporting *no problems* with MO, 14.8% reported *moderate* to *extreme* cognitive problems (Table <a href="#Tab3" data-ref-type="table">3</a>). Similarly, 23.4% of those without self-care limitations reported cognitive difficulties, and 16.3% reported at least moderate problems with SP. Stratified analysis by symptom severity revealed the added value of both bolt-ons, which becomes especially apparent with increasing severity of post-COVID symptomatology (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<div id="Tab3" class="table-wrap">

<div class="caption">

Number and proportion of patients reporting “*no problems*” on the EQ-5D-5L dimension by bolt-ons (T<sub>1</sub>)

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="2" style="text-align: left;">Bolt-on</th>
<th colspan="6" style="text-align: left;">Number and proportion of patients reporting “<em>no problems</em>” with…</th>
</tr>
<tr>
<th style="text-align: left;">Mobility</th>
<th style="text-align: left;">Self-care</th>
<th style="text-align: left;">Usual activities</th>
<th style="text-align: left;">Pain/discomfort</th>
<th style="text-align: left;">Anxiety/depression</th>
<th style="text-align: left;">’11111’</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6" style="text-align: left;">Cognition</td>
<td style="text-align: left;">No problems</td>
<td style="text-align: left;">835 (48.9)</td>
<td style="text-align: left;">1065 (37.5)</td>
<td style="text-align: left;">920 (56.4)</td>
<td style="text-align: left;">533 (63.2)</td>
<td style="text-align: left;">856 (56.5)</td>
<td style="text-align: left;">450 (78.8)</td>
</tr>
<tr>
<td style="text-align: left;">Slight problems</td>
<td style="text-align: left;">621 (36.3)</td>
<td style="text-align: left;">1116 (39.2)</td>
<td style="text-align: left;">583 (35.7)</td>
<td style="text-align: left;">237 (28.1)</td>
<td style="text-align: left;">492 (32.5)</td>
<td style="text-align: left;">111 (19.4)</td>
</tr>
<tr>
<td style="text-align: left;">Moderate problems</td>
<td style="text-align: left;">188 (11.0)</td>
<td style="text-align: left;">458 (16.1)</td>
<td style="text-align: left;">110 (6.7)</td>
<td style="text-align: left;">60 (7.1)</td>
<td style="text-align: left;">121 (8.0)</td>
<td style="text-align: left;">9 (1.6)</td>
</tr>
<tr>
<td style="text-align: left;">Severe problems</td>
<td style="text-align: left;">58 (3.4)</td>
<td style="text-align: left;">175 (6.2)</td>
<td style="text-align: left;">16 (1.0)</td>
<td style="text-align: left;">12 (1.4)</td>
<td style="text-align: left;">41 (2.7)</td>
<td style="text-align: left;">1 (0.0)</td>
</tr>
<tr>
<td style="text-align: left;">Extreme problems</td>
<td style="text-align: left;">7 (0.4)</td>
<td style="text-align: left;">30 (1.1)</td>
<td style="text-align: left;">2 (0.1)</td>
<td style="text-align: left;">2 (0.1)</td>
<td style="text-align: left;">4 (0.3)</td>
<td style="text-align: left;">0 (0.0)</td>
</tr>
<tr>
<td style="text-align: left;">Total<sup>1</sup></td>
<td style="text-align: left;">1709 (100)</td>
<td style="text-align: left;">2844 (100)</td>
<td style="text-align: left;">1631 (100)</td>
<td style="text-align: left;">844 (100)</td>
<td style="text-align: left;">1514 (100)</td>
<td style="text-align: left;">571 (100)</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Social participation</td>
<td style="text-align: left;">No problems</td>
<td style="text-align: left;">1252 (73.2)</td>
<td style="text-align: left;">1746 (61.4)</td>
<td style="text-align: left;">1352 (82.9)</td>
<td style="text-align: left;">684 (81.3)</td>
<td style="text-align: left;">1265 (83.6)</td>
<td style="text-align: left;">540 (94.9)</td>
</tr>
<tr>
<td style="text-align: left;">Slight problems</td>
<td style="text-align: left;">293 (17.1)</td>
<td style="text-align: left;">637 (22.4)</td>
<td style="text-align: left;">221 (13.6)</td>
<td style="text-align: left;">108 (12.8)</td>
<td style="text-align: left;">172 (11.4)</td>
<td style="text-align: left;">26 (4.6)</td>
</tr>
<tr>
<td style="text-align: left;">Moderate problems</td>
<td style="text-align: left;">118 (6.9)</td>
<td style="text-align: left;">328 (11.5)</td>
<td style="text-align: left;">45 (2.8)</td>
<td style="text-align: left;">35 (4.2)</td>
<td style="text-align: left;">52 (3.4)</td>
<td style="text-align: left;">2 (0.4)</td>
</tr>
<tr>
<td style="text-align: left;">Severe problems</td>
<td style="text-align: left;">39 (2.3)</td>
<td style="text-align: left;">119 (4.2)</td>
<td style="text-align: left;">13 (0.8)</td>
<td style="text-align: left;">10 (1.2)</td>
<td style="text-align: left;">22 (1.5)</td>
<td style="text-align: left;">1 (0.2)</td>
</tr>
<tr>
<td style="text-align: left;">Extreme problems</td>
<td style="text-align: left;">8 (0.5)</td>
<td style="text-align: left;">16 (0.6)</td>
<td style="text-align: left;">0 (0.0)</td>
<td style="text-align: left;">4 (0.5)</td>
<td style="text-align: left;">3 (0.2)</td>
<td style="text-align: left;">0 (0.0)</td>
</tr>
<tr>
<td style="text-align: left;">Total<sup>1</sup></td>
<td style="text-align: left;">170 (100)</td>
<td style="text-align: left;">2846 (100)</td>
<td style="text-align: left;">1631 (100)</td>
<td style="text-align: left;">841 (100)</td>
<td style="text-align: left;">1514 (100)</td>
<td style="text-align: left;">569 (100)</td>
</tr>
</tbody>
</table>

<sup>1</sup>Corresponds to ceiling in EQ-5D-5L items

</div>

<figure id="Fig1">
<p><img src="11136_2026_4226_Fig1_HTML.jpg" id="d33e1525" /></p>
<p><img src="11136_2026_4226_Fig1_HTML.gif" /></p>
<figcaption>Distribution of responses based on self-rated PCS severity (PCS-Score T<sub>1</sub>): no or mild (0–10.75), moderate (10.76–26.25), severe (&gt; 26.25) PCS</figcaption>
</figure>

#### Convergent and divergent validity

CO and SP show moderate to high correlations with all EQ-5D-5L dimensions (e.g., r<sub>CO,UA</sub> = 0.63, r<sub>SP,UA</sub> = −0.65, r<sub>SP,PD</sub> = −0.63) except SC (r<sub>CO,SC</sub> = 0.27, r<sub>SP,SC</sub> = 0.33). Except for moral injury (G-MISS-HP) and resilience (BRS), which show weak correlations of r \< 0.27, correlations with other measures are generally moderate to high, particularly with broader constructs of functioning, (dis)ability and health (WHODAS: r<sub>CO,WHODAS</sub> = 0.69, r<sub>SP,WHODAS</sub> = 0.71, WAI: r<sub>CO,WAI</sub> = −0.63, r<sub>SP,WAI</sub> = −0.60, EQ VAS: r<sub>CO,VAS</sub> = r<sub>SP,VAS</sub> = −0.58, Table <a href="#Tab4" data-ref-type="table">4</a>).

<div id="Tab4" class="table-wrap">

<div class="caption">

Spearman's rank correlation coefficients; pairwise; T<sub>1</sub>: EQ-5D-5L items, bolt-on items and other measures

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variables*</th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">CO</th>
<th style="text-align: left;">SP</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8" style="text-align: left;">EQ-5D-5L items</td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">0.354</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">0.570</td>
<td style="text-align: center;">0.381</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">0.603</td>
<td style="text-align: center;">0.316</td>
<td style="text-align: center;">0.587</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">0.377</td>
<td style="text-align: center;">0.266</td>
<td style="text-align: center;">0.507</td>
<td style="text-align: center;">0.451</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Bolt-ons</td>
</tr>
<tr>
<td style="text-align: left;">CO</td>
<td style="text-align: center;">0.405</td>
<td style="text-align: center;">0.271</td>
<td style="text-align: center;">0.587</td>
<td style="text-align: center;">0.478</td>
<td style="text-align: center;">0.513</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">SP</td>
<td style="text-align: center;">0.425</td>
<td style="text-align: center;">0.329</td>
<td style="text-align: center;">0.626</td>
<td style="text-align: center;">0.445</td>
<td style="text-align: center;">0.586</td>
<td style="text-align: center;">0.552</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: center;"> − 0.541</td>
<td style="text-align: center;"> − 0.319</td>
<td style="text-align: center;"> − 0.654</td>
<td style="text-align: center;"> − 0.633</td>
<td style="text-align: center;"> − 0.542</td>
<td style="text-align: center;"> − 0.583</td>
<td style="text-align: left;"> − 0.575</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Other measures</td>
</tr>
<tr>
<td style="text-align: left;">SSD-12</td>
<td style="text-align: center;">0.484</td>
<td style="text-align: center;">0.280</td>
<td style="text-align: center;">0.601</td>
<td style="text-align: center;">0.566</td>
<td style="text-align: center;">0.583</td>
<td style="text-align: center;">0.574</td>
<td style="text-align: left;">0.554</td>
</tr>
<tr>
<td style="text-align: left;">PHQ-4</td>
<td style="text-align: center;">0.422</td>
<td style="text-align: center;">0.249</td>
<td style="text-align: center;">0.547</td>
<td style="text-align: center;">0.482</td>
<td style="text-align: center;">0.727</td>
<td style="text-align: center;">0.561</td>
<td style="text-align: left;">0.574</td>
</tr>
<tr>
<td style="text-align: left;">PTSD</td>
<td style="text-align: center;">0.412</td>
<td style="text-align: center;">0.266</td>
<td style="text-align: center;">0.555</td>
<td style="text-align: center;">0.470</td>
<td style="text-align: center;">0.581</td>
<td style="text-align: center;">0.562</td>
<td style="text-align: left;">0.589</td>
</tr>
<tr>
<td style="text-align: left;">BRS</td>
<td style="text-align: center;"> − <em>0.029</em></td>
<td style="text-align: center;"><em>0.006</em></td>
<td style="text-align: center;"> − <em>0.002</em></td>
<td style="text-align: center;"> − <em>0.002</em></td>
<td style="text-align: center;">0.114</td>
<td style="text-align: center;"><em>0.027</em></td>
<td style="text-align: left;"><em>0.037</em></td>
</tr>
<tr>
<td style="text-align: left;">G-MISS-HP</td>
<td style="text-align: center;">0.170</td>
<td style="text-align: center;">0.104</td>
<td style="text-align: center;">0.211</td>
<td style="text-align: center;">0.171</td>
<td style="text-align: center;">0.272</td>
<td style="text-align: center;">0.214</td>
<td style="text-align: left;">0.207</td>
</tr>
<tr>
<td style="text-align: left;">WAI</td>
<td style="text-align: center;"> − 0.538</td>
<td style="text-align: center;"> − 0.289</td>
<td style="text-align: center;"> − 0.693</td>
<td style="text-align: center;"> − 0.641</td>
<td style="text-align: center;"> − 0.573</td>
<td style="text-align: center;"> − 0.632</td>
<td style="text-align: left;"> − 0.604</td>
</tr>
<tr>
<td style="text-align: left;">WHODAS</td>
<td style="text-align: center;">0.614</td>
<td style="text-align: center;">0.366</td>
<td style="text-align: center;">0.749</td>
<td style="text-align: center;">0.628</td>
<td style="text-align: center;">0.633</td>
<td style="text-align: center;">0.687</td>
<td style="text-align: left;">0.706</td>
</tr>
<tr>
<td style="text-align: left;">PCS total score</td>
<td style="text-align: center;">0.514</td>
<td style="text-align: center;">0.287</td>
<td style="text-align: center;">0.603</td>
<td style="text-align: center;">0.609</td>
<td style="text-align: center;">0.498</td>
<td style="text-align: center;">0.631</td>
<td style="text-align: left;">0.508</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">PCS items<sup>1</sup></td>
</tr>
<tr>
<td style="text-align: left;">1 Smell or taste disorders</td>
<td style="text-align: center;">0.201</td>
<td style="text-align: center;">0.103</td>
<td style="text-align: center;">0.201</td>
<td style="text-align: center;">0.208</td>
<td style="text-align: center;">0.156</td>
<td style="text-align: center;">0.231</td>
<td style="text-align: left;">0.160</td>
</tr>
<tr>
<td style="text-align: left;">2 Fatigue (chronic exhaustion, tiredness)</td>
<td style="text-align: center;">0.463</td>
<td style="text-align: center;">0.268</td>
<td style="text-align: center;">0.575</td>
<td style="text-align: center;">0.530</td>
<td style="text-align: center;">0.484</td>
<td style="text-align: center;">0.573</td>
<td style="text-align: left;">0.479</td>
</tr>
<tr>
<td style="text-align: left;">3 Lack of physical resilience (e.g., full capacity not regained, shortness of breath)</td>
<td style="text-align: center;">0.494</td>
<td style="text-align: center;">0.268</td>
<td style="text-align: center;">0.588</td>
<td style="text-align: center;">0.538</td>
<td style="text-align: center;">0.426</td>
<td style="text-align: center;">0.540</td>
<td style="text-align: left;">0.449</td>
</tr>
<tr>
<td style="text-align: left;">4 Joint or muscle pain</td>
<td style="text-align: center;">0.503</td>
<td style="text-align: center;">0.260</td>
<td style="text-align: center;">0.470</td>
<td style="text-align: center;">0.625</td>
<td style="text-align: center;">0.364</td>
<td style="text-align: center;">0.409</td>
<td style="text-align: left;">0.356</td>
</tr>
<tr>
<td style="text-align: left;">5 Complaints in the throat, nose or ear area (e.g., hoarseness, pain or scatchiness)</td>
<td style="text-align: center;">0.251</td>
<td style="text-align: center;">0.146</td>
<td style="text-align: center;">0.286</td>
<td style="text-align: center;">0.306</td>
<td style="text-align: center;">0.245</td>
<td style="text-align: center;">0.289</td>
<td style="text-align: left;">0.247</td>
</tr>
<tr>
<td style="text-align: left;">6 Lung or breathing difficulties (e.g., coughing, whistling or wheezing)</td>
<td style="text-align: center;">0.348</td>
<td style="text-align: center;">0.211</td>
<td style="text-align: center;">0.377</td>
<td style="text-align: center;">0.344</td>
<td style="text-align: center;">0.283</td>
<td style="text-align: center;">0.330</td>
<td style="text-align: left;">0.290</td>
</tr>
<tr>
<td style="text-align: left;">7 Heart complaints (e.g., extrasystoles, palpitations, chest pain)</td>
<td style="text-align: center;">0.293</td>
<td style="text-align: center;">0.194</td>
<td style="text-align: center;">0.338</td>
<td style="text-align: center;">0.348</td>
<td style="text-align: center;">0.311</td>
<td style="text-align: center;">0.350</td>
<td style="text-align: left;">0.295</td>
</tr>
<tr>
<td style="text-align: left;">8 Gastrointestinal complaints (e.g., abdominal pain, diarrhea, vomiting, nausea)</td>
<td style="text-align: center;">0.284</td>
<td style="text-align: center;">0.233</td>
<td style="text-align: center;">0.314</td>
<td style="text-align: center;">0.318</td>
<td style="text-align: center;">0.275</td>
<td style="text-align: center;">0.294</td>
<td style="text-align: left;">0.318</td>
</tr>
<tr>
<td style="text-align: left;">9 Complaints or abnormalities of the nervous system or memory (e.g., concentration problems)</td>
<td style="text-align: center;">0.395</td>
<td style="text-align: center;">0.222</td>
<td style="text-align: center;">0.545</td>
<td style="text-align: center;">0.491</td>
<td style="text-align: center;">0.471</td>
<td style="text-align: center;">0.734</td>
<td style="text-align: left;">0.469</td>
</tr>
<tr>
<td style="text-align: left;">10 Skin complaints (e.g., hair loss, rash, itching)</td>
<td style="text-align: center;">0.196</td>
<td style="text-align: center;">0.111</td>
<td style="text-align: center;">0.239</td>
<td style="text-align: center;">0.250</td>
<td style="text-align: center;">0.213</td>
<td style="text-align: center;">0.236</td>
<td style="text-align: left;">0.203</td>
</tr>
<tr>
<td style="text-align: left;">11 Signs of infection (e.g., chills, fever, flu-like feeling)</td>
<td style="text-align: center;">0.262</td>
<td style="text-align: center;">0.203</td>
<td style="text-align: center;">0.261</td>
<td style="text-align: center;">0.243</td>
<td style="text-align: center;">0.216</td>
<td style="text-align: center;">0.253</td>
<td style="text-align: left;">0.226</td>
</tr>
<tr>
<td style="text-align: left;">12 Sleep disorders (e.g., difficulties falling asleep or sleeping through the night)</td>
<td style="text-align: center;">0.398</td>
<td style="text-align: center;">0.242</td>
<td style="text-align: center;">0.469</td>
<td style="text-align: center;">0.472</td>
<td style="text-align: center;">0.443</td>
<td style="text-align: center;">0.474</td>
<td style="text-align: left;">0.404</td>
</tr>
<tr>
<td style="text-align: left;">13 Other health restrictions</td>
<td style="text-align: center;">0.270</td>
<td style="text-align: center;">0.188</td>
<td style="text-align: center;">0.302</td>
<td style="text-align: center;">0.282</td>
<td style="text-align: center;">0.216</td>
<td style="text-align: center;">0.249</td>
<td style="text-align: left;">0.242</td>
</tr>
<tr>
<td style="text-align: left;">14 Sexual complaints (e.g., loss of libido, erectile dysfunction, pain during sexual)</td>
<td style="text-align: center;">0.240</td>
<td style="text-align: center;">0.163</td>
<td style="text-align: center;">0.302</td>
<td style="text-align: center;">0.255</td>
<td style="text-align: center;">0.265</td>
<td style="text-align: center;">0.309</td>
<td style="text-align: left;">0.295</td>
</tr>
</tbody>
</table>

All *p* \< 0.01 except those in italic letters. \*n<sub>min</sub> = 1819, n<sub>avg</sub> = 2758, n<sub>max</sub> = 3153. <sup>1</sup>n<sub>min</sub> = 2804, n<sub>avg</sub> = 3100, n<sub>max</sub> = 3301

G-MISS-HP, Moral Injury Symptom and Support scale for Health Professionals, German version; PCS-Score, Post-COVID syndrome PCS-Score; PHQ-4, Patient Health Questionnaire; SSD-12, Somatic Symptom Disorder-B criteria scale; PTSD, Short screening scale for DSM-IV posttraumatic stress disorder; WAI, Work Ability Index; WHODAS, WHO Disability Assessment Schedule 2.0

</div>

EQ-5D-5L items display convergent validity, with moderate to high correlations with corresponding measures, such as anxiety/depression (r<sub>AD,PHQ-4</sub> = 0.73) and posttraumatic stress (r<sub>AD,PTSD</sub> = 0.58). Conversely, correlations with instruments measuring different constructs are weak (e.g., r<sub>BRS</sub> = −0.03–0.04, r<sub>G-MISS-HP</sub> = 0.10–0.27), demonstrating the divergent validity of the EQ-5D-5L.

SC stands out as the only dimension with minimal correlation to other instruments, suggesting that it either captures a unique aspect of health or exhibits limited variance, which may reduce the power to estimate its associations properly. Excluding SC, correlations with the EQ VAS are moderate to strong, ranging from r = −0.54 (MO, AD) to r = −0.65 (UA), reinforcing the validity of the EQ-5D-5L in assessing overall health.

### Known-groups validity

Inclusion of CO significantly improved discrimination in 10 of 13 comparisons compared to the EQ-5D-5L alone, with relative efficiencies (REs) ranging from 1.10 (95% CI 1.06–1.14) to 1.22 (95% CI 1.16–1.28, Table <a href="#Tab5" data-ref-type="table">5</a>). EQ-5D-5L + SP improved discrimination in 6 of 13 comparisons, with REs of 1.06 (95% CI 1.01–1.10) to 1.18 (95% CI 1.13–1.24).

<div id="Tab5" class="table-wrap">

<div class="caption">

Known groups validity of the EQ-5D-5L (+ bolt-ons): baseline mean LSS ± SD with RE (ref: EQ-5D-5L) with Bootstrap SE and 95% CI

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Known groups</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">EQ-5D-5L</th>
<th style="text-align: left;">EQ-5D-5L + CO</th>
<th style="text-align: left;">EQ-5D-5L + SP</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">PCS diagnosed by physician<sup>1</sup></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td style="text-align: left;">765</td>
<td style="text-align: left;">23.3</td>
<td style="text-align: center;">71.5 ± 17.9</td>
<td style="text-align: center;">68.9 ± 17.9</td>
<td style="text-align: left;">70.9 ± 18.7</td>
</tr>
<tr>
<td style="text-align: left;">  No</td>
<td style="text-align: left;">2159</td>
<td style="text-align: left;">76.7</td>
<td style="text-align: center;">85.8 ± 14.1</td>
<td style="text-align: center;">84.8 ± 14.1</td>
<td style="text-align: left;">85.9 ± 18.7</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.22 ± 0.03</p>
<p>(1.16–1.28)</p></td>
<td style="text-align: center;"><p>1.06 ± 0.02</p>
<p>(1.01 1.10)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Full days absent from work due to post-COVID symptoms</td>
</tr>
<tr>
<td style="text-align: left;">  0 days</td>
<td style="text-align: left;">216</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: center;">90.5 ± 11.3</td>
<td style="text-align: center;">89.2 ± 11.5</td>
<td style="text-align: left;">90.5 ± 11.4</td>
</tr>
<tr>
<td style="text-align: left;">   &lt; 10</td>
<td style="text-align: left;">220</td>
<td style="text-align: left;">7.2</td>
<td style="text-align: center;">90.5 ± 12.3</td>
<td style="text-align: center;">89.9 ± 12.1</td>
<td style="text-align: left;">91.0 ± 11.8</td>
</tr>
<tr>
<td style="text-align: left;">  10–24</td>
<td style="text-align: left;">1167</td>
<td style="text-align: left;">38.2</td>
<td style="text-align: center;">86.1 ± 14.2</td>
<td style="text-align: center;">85.1 ± 14.3</td>
<td style="text-align: left;">86.3 ± 14.4</td>
</tr>
<tr>
<td style="text-align: left;">  25–99</td>
<td style="text-align: left;">1185</td>
<td style="text-align: left;">38.7</td>
<td style="text-align: center;">80.1 ± 15.5</td>
<td style="text-align: center;">78.7 ± 15.4</td>
<td style="text-align: left;">80.3 ± 15.6</td>
</tr>
<tr>
<td style="text-align: left;">   ≥ 100 days</td>
<td style="text-align: left;">271</td>
<td style="text-align: left;">8.9</td>
<td style="text-align: center;">67.0 ± 18.6</td>
<td style="text-align: center;">64.3 ± 18.5</td>
<td style="text-align: left;">65.5 ± 19.4</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.17 ± 0.03</p>
<p>(1.11–1.22)</p></td>
<td style="text-align: center;"><p>1.10 ± 0.25</p>
<p>(1.05–1.15)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Current incapacity for work due to COVID-illness<sup>2</sup></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td style="text-align: left;">212</td>
<td style="text-align: left;">6.4</td>
<td style="text-align: center;">58.2 ± 17.4</td>
<td style="text-align: center;">55.4 ± 17.2</td>
<td style="text-align: left;">55.7 ± 17.6</td>
</tr>
<tr>
<td style="text-align: left;">  No</td>
<td style="text-align: left;">3095</td>
<td style="text-align: left;">93.6</td>
<td style="text-align: center;">84.2 ± 14.8</td>
<td style="text-align: center;">82.9 ± 14.9</td>
<td style="text-align: left;">84.3 ± 14.9</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.11 ± 0.03</p>
<p>(1.05–1.16)</p></td>
<td style="text-align: center;"><p>1.18 ± 0.03</p>
<p>(1.13–1.24)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Work ability according to WAI</td>
</tr>
<tr>
<td style="text-align: left;">  Very good (44–49)</td>
<td style="text-align: left;">265</td>
<td style="text-align: left;">10.9</td>
<td style="text-align: center;">97.5 ± 4.0</td>
<td style="text-align: center;">97.2 ± 4.1</td>
<td style="text-align: left;">97.7 ± 3.6</td>
</tr>
<tr>
<td style="text-align: left;">  Good (37–43)</td>
<td style="text-align: left;">703</td>
<td style="text-align: left;">29.0</td>
<td style="text-align: center;">92.8 ± 7.9</td>
<td style="text-align: center;">91.9 ± 7.8</td>
<td style="text-align: left;">93.2 ± 7.3</td>
</tr>
<tr>
<td style="text-align: left;">  Moderate (28–36)</td>
<td style="text-align: left;">830</td>
<td style="text-align: left;">34.3</td>
<td style="text-align: center;">82.9 ± 11.2</td>
<td style="text-align: center;">81.4 ± 10.9</td>
<td style="text-align: left;">83.1 ± 11.1</td>
</tr>
<tr>
<td style="text-align: left;">  Poor (7–27)</td>
<td style="text-align: left;">625</td>
<td style="text-align: left;">25.8</td>
<td style="text-align: center;">66.3 ± 15.3</td>
<td style="text-align: center;">64.1 ± 14.8</td>
<td style="text-align: left;">65.5 ± 15.8</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.18 ± 0.02</p>
<p>(1.13–1.22)</p></td>
<td style="text-align: center;"><p>1.08 ± 0.02</p>
<p>(1.04–1.11)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">PHQ-4</td>
</tr>
<tr>
<td style="text-align: left;">  Normal (0–2)</td>
<td style="text-align: left;">1525</td>
<td style="text-align: left;">50.2</td>
<td style="text-align: center;">90.6 ± 10.8</td>
<td style="text-align: center;">89.6 ± 11.1</td>
<td style="text-align: left;">90.9 ± 10.6</td>
</tr>
<tr>
<td style="text-align: left;">  Mild (3–5)</td>
<td style="text-align: left;">985</td>
<td style="text-align: left;">32.4</td>
<td style="text-align: center;">78.3 ± 13.7</td>
<td style="text-align: center;">76.7 ± 13.3</td>
<td style="text-align: left;">78.4 ± 13.6</td>
</tr>
<tr>
<td style="text-align: left;">  Moderate (6–8)</td>
<td style="text-align: left;">340</td>
<td style="text-align: left;">11.2</td>
<td style="text-align: center;">67.3 ± 15.1</td>
<td style="text-align: center;">65.1 ± 14.7</td>
<td style="text-align: left;">66.2 ± 15.4</td>
</tr>
<tr>
<td style="text-align: left;">  Severe (9–12)</td>
<td style="text-align: left;">186</td>
<td style="text-align: left;">6.1</td>
<td style="text-align: center;">55.7 ± 16.9</td>
<td style="text-align: center;">53.7 ± 16.2</td>
<td style="text-align: left;">53.6 ± 17.2</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.12 ± 0.02</p>
<p>(1.08–1.16)</p></td>
<td style="text-align: center;"><p>1.03 ± 0.02</p>
<p>(0.99–1.06)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">SSD-12</td>
</tr>
<tr>
<td style="text-align: left;">  No impairment (&lt; 13)</td>
<td style="text-align: left;">1182</td>
<td style="text-align: left;">41.4</td>
<td style="text-align: center;">91.4 ± 9.4</td>
<td style="text-align: center;">90.5 ± 9.6</td>
<td style="text-align: left;">91.8 ± 9.1</td>
</tr>
<tr>
<td style="text-align: left;">  Impairment (≥ 13)</td>
<td style="text-align: left;">1671</td>
<td style="text-align: left;">58.6</td>
<td style="text-align: center;">73.3 ± 16.3</td>
<td style="text-align: center;">71.4 ± 16.1</td>
<td style="text-align: left;">72.9 ± 16.9</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.12 ± 0.02</p>
<p>(1.08–1.16)</p></td>
<td style="text-align: center;"><p>1.03 ± 0.02</p>
<p>(0.99–1.06)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Combination of PHQ-4 and SSD-12</td>
</tr>
<tr>
<td style="text-align: left;">  SSD-12 &lt; 13</td>
<td style="text-align: left;">1182</td>
<td style="text-align: left;">35.4</td>
<td style="text-align: center;">91.4 ± 9.4</td>
<td style="text-align: center;">90.5 ± 9.6</td>
<td style="text-align: left;">91.8 ± 9.1</td>
</tr>
<tr>
<td style="text-align: left;">  SSD-12 ≥ 13 AND PHQ-4 &lt; 8</td>
<td style="text-align: left;">1637</td>
<td style="text-align: left;">49.1</td>
<td style="text-align: center;">79.3 ± 15.1</td>
<td style="text-align: center;">77.8 ± 15.1</td>
<td style="text-align: left;">79.4 ± 15.3</td>
</tr>
<tr>
<td style="text-align: left;">  SSD-12 ≥ 13 AND PHQ-4 ≥ 8</td>
<td style="text-align: left;">516</td>
<td style="text-align: left;">15.5</td>
<td style="text-align: center;">70.7 ± 21.7</td>
<td style="text-align: center;">68.9 ± 21.9</td>
<td style="text-align: left;">69.4 ± 22.6</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.10 ± 0.02</p>
<p>(1.06–1.14)</p></td>
<td style="text-align: center;"><p>1.13 ± 0.02</p>
<p>(1.09–1.17)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Before first infection</td>
</tr>
<tr>
<td style="text-align: left;">  No (0)</td>
<td style="text-align: left;">1321</td>
<td style="text-align: left;">43.9</td>
<td style="text-align: center;">85.8 ± 15.7</td>
<td style="text-align: center;">84.4 ± 16.8</td>
<td style="text-align: left;">85.6 ± 16.3</td>
</tr>
<tr>
<td style="text-align: left;">  Mild (&gt; 0 and ≤ 10.75)</td>
<td style="text-align: left;">839</td>
<td style="text-align: left;">27.9</td>
<td style="text-align: center;">81.9 ± 15.5</td>
<td style="text-align: center;">80.4 ± 15.7</td>
<td style="text-align: left;">81.9 ± 15.9</td>
</tr>
<tr>
<td style="text-align: left;">  Moderate (&gt; 10.75- ≤ 26.25)</td>
<td style="text-align: left;">627</td>
<td style="text-align: left;">20.8</td>
<td style="text-align: center;">79.4 ± 15.9</td>
<td style="text-align: center;">78.3 ± 15.9</td>
<td style="text-align: left;">79.5 ± 16.1</td>
</tr>
<tr>
<td style="text-align: left;">  Severe/relevant (&gt; 26.25)</td>
<td style="text-align: left;">222</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: center;">74.2 ± 17.3</td>
<td style="text-align: center;">72.9 ± 16.8</td>
<td style="text-align: left;">74.3 ± 17.7</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>0.94 ± 0.04</p>
<p>(0.86–1.01)</p></td>
<td style="text-align: center;"><p>0.89 ± 0.03</p>
<p>(0.82–0.95)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Baseline (T<sub>1</sub>)</td>
</tr>
<tr>
<td style="text-align: left;">  No or mild (0 to ≤ 10.75)</td>
<td style="text-align: left;">865</td>
<td style="text-align: left;">28.5</td>
<td style="text-align: center;">94.7 ± 7.4</td>
<td style="text-align: center;">94.4 ± 7.1</td>
<td style="text-align: left;">94.9 ± 7.1</td>
</tr>
<tr>
<td style="text-align: left;">  Moderate (&gt; 10.75 to ≤ 26.25)</td>
<td style="text-align: left;">687</td>
<td style="text-align: left;">22.6</td>
<td style="text-align: center;">88.0 ± 10.3</td>
<td style="text-align: center;">86.9 ± 10.0</td>
<td style="text-align: left;">88.2 ± 10.5</td>
</tr>
<tr>
<td style="text-align: left;">  Severe/relevant (&gt; 26.25)</td>
<td style="text-align: left;">1482</td>
<td style="text-align: left;">48.9</td>
<td style="text-align: center;">72.7 ± 16.5</td>
<td style="text-align: center;">70.7 ± 16.1</td>
<td style="text-align: left;">72.5 ± 16.9</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.21 ± 0.02</p>
<p>(1.17–1.24)</p></td>
<td style="text-align: center;"><p>0.99 ± 0.01</p>
<p>(0.97–1.02)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">During most severe infection</td>
</tr>
<tr>
<td style="text-align: left;">  No or mild (0 to ≤ 10.75)</td>
<td style="text-align: left;">214</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: center;">95.4 ± 7.4</td>
<td style="text-align: center;">95.5 ± 6.9</td>
<td style="text-align: left;">95.8 ± 6.9</td>
</tr>
<tr>
<td style="text-align: left;">  Moderate (&gt; 10.75- ≤ 26.25)</td>
<td style="text-align: left;">500</td>
<td style="text-align: left;">16.6</td>
<td style="text-align: center;">91.3 ± 10.3</td>
<td style="text-align: center;">90.7 ± 10.2</td>
<td style="text-align: left;">91.4 ± 10.5</td>
</tr>
<tr>
<td style="text-align: left;">  Severe/relevant (&gt; 26.25)</td>
<td style="text-align: left;">2301</td>
<td style="text-align: left;">76.3</td>
<td style="text-align: center;">79.1 ± 16.6</td>
<td style="text-align: center;">77.4 ± 16.6</td>
<td style="text-align: left;">79.0 16.9</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.21 ± 0.02</p>
<p>(1.16–1.25)</p></td>
<td style="text-align: center;"><p>1.00 ± 0.02</p>
<p>(0.97–1.03)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Short screening scale for DSM-IV PTSD</td>
</tr>
<tr>
<td style="text-align: left;">  No PTSD (&lt; 4)</td>
<td style="text-align: left;">1618</td>
<td style="text-align: left;">53.9</td>
<td style="text-align: center;">90.3 ± 10.6</td>
<td style="text-align: center;">89.5 ± 10.7</td>
<td style="text-align: left;">90.8 ± 10.3</td>
</tr>
<tr>
<td style="text-align: left;">  PTSD (≥ 4)</td>
<td style="text-align: left;">1381</td>
<td style="text-align: left;">46.1</td>
<td style="text-align: center;">73.4 ± 16.7</td>
<td style="text-align: center;">71.5 ± 16.4</td>
<td style="text-align: left;">72.8 ± 17.1</td>
</tr>
<tr>
<td style="text-align: left;">RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.16 ± 0.02</p>
<p>(1.11–1.19)</p></td>
<td style="text-align: center;"><p>1.13 ± 0.02</p>
<p>(1.09–1.16)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Number of pre-existing conditions<sup>1</sup></td>
</tr>
<tr>
<td style="text-align: left;">  0</td>
<td style="text-align: left;">1107</td>
<td style="text-align: left;">34.1</td>
<td style="text-align: center;">86.7 ± 15.7</td>
<td style="text-align: center;">85.4 ± 15.9</td>
<td style="text-align: left;">86.5 ± 16.0</td>
</tr>
<tr>
<td style="text-align: left;">  1</td>
<td style="text-align: left;">673</td>
<td style="text-align: left;">20.7</td>
<td style="text-align: center;">84.8 ± 15.4</td>
<td style="text-align: center;">83.4 ± 15.8</td>
<td style="text-align: left;">84.9 ± 15.6</td>
</tr>
<tr>
<td style="text-align: left;">  2</td>
<td style="text-align: left;">528</td>
<td style="text-align: left;">16.3</td>
<td style="text-align: center;">82.4 ± 15.4</td>
<td style="text-align: center;">80.8 ± 15.8</td>
<td style="text-align: left;">82.4 ± 15.8</td>
</tr>
<tr>
<td style="text-align: left;">  3</td>
<td style="text-align: left;">450</td>
<td style="text-align: left;">13.9</td>
<td style="text-align: center;">80.3 ± 14.6</td>
<td style="text-align: center;">78.9 ± 14.8</td>
<td style="text-align: left;">80.5 ± 15.1</td>
</tr>
<tr>
<td style="text-align: left;">  4 + </td>
<td style="text-align: left;">488</td>
<td style="text-align: left;">15.0</td>
<td style="text-align: center;">74.7 ± 16.7</td>
<td style="text-align: center;">73.5 ± 16.4</td>
<td style="text-align: left;">74.8 ± 17.3</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>0.96 ± 0.02</p>
<p>(0.89–1.02)</p></td>
<td style="text-align: center;"><p>0.91 ± 0.03</p>
<p>(0.85–0.97)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Number of physician-diagnosed diseases<sup>1</sup></td>
</tr>
<tr>
<td style="text-align: left;">  0</td>
<td style="text-align: left;">1040</td>
<td style="text-align: left;">32.9</td>
<td style="text-align: center;">87.9 ± 14.9</td>
<td style="text-align: center;">86.8 ± 15.0</td>
<td style="text-align: left;">87.9 ± 15.1</td>
</tr>
<tr>
<td style="text-align: left;">  1</td>
<td style="text-align: left;">575</td>
<td style="text-align: left;">18.2</td>
<td style="text-align: center;">87.3 ± 13.2</td>
<td style="text-align: center;">86.1 ± 13.4</td>
<td style="text-align: left;">87.4 ± 13.4</td>
</tr>
<tr>
<td style="text-align: left;">  2</td>
<td style="text-align: left;">524</td>
<td style="text-align: left;">16.6</td>
<td style="text-align: center;">83.8 ± 14.3</td>
<td style="text-align: center;">82.3 ± 14.7</td>
<td style="text-align: left;">83.8 ± 14.8</td>
</tr>
<tr>
<td style="text-align: left;">  3–4</td>
<td style="text-align: left;">684</td>
<td style="text-align: left;">21.7</td>
<td style="text-align: center;">79.5 ± 14.9</td>
<td style="text-align: center;">77.9 ± 15.1</td>
<td style="text-align: left;">79.6 ± 15.2</td>
</tr>
<tr>
<td style="text-align: left;">  5 + </td>
<td style="text-align: left;">335</td>
<td style="text-align: left;">10.6</td>
<td style="text-align: center;">68.4 ± 17.3</td>
<td style="text-align: center;">66.8 ± 17.1</td>
<td style="text-align: left;">68.2 ± 17.9</td>
</tr>
<tr>
<td style="text-align: left;">  RE ± SE (95% CI)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: center;"><p>1.03 ± 0.02</p>
<p>(0.98–1.07)</p></td>
<td style="text-align: center;"><p>0.96 ± 0.02</p>
<p>(0.92–1.01)</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

<sup>1</sup>Self-reported; <sup>2</sup>Currently on sick leave due to the consequences of COVID-19 illness; CI, Confidence Interval; CO, Cognition bolt-on; LSS, Level Sum Scores; PHQ-4, Patient Health Questionnaire-4; PTSD, Post-Traumatic Stress Disorder; RE, Relative Efficacy; ref, Reference; SD, Standard Deviation; SE, Standard Error; SP, Social participation bolt-on; SSD-12, Somatic Symptom Disorder-B criteria scale

</div>

As expected, neither bolt-on improved RE for PCS severity prior to infection. Adding CO significantly improved discrimination of PCS severity groups at baseline and during the most severe COVID-19 episode compared with the EQ-5D-5L alone, whereas EQ-5D-5L + SP performed similarly to the standard EQ-5D-5L.

For work outcomes, results were mixed: EQ-5D-5L + SP showed better discrimination of current sick leave status due to post-COVID symptoms (RE<sub>SP</sub> 1.18, 95% CI 1.13–1.24 vs. RE<sub>CO</sub> = 1.11, 95% CI 1.05–1.16). In contrast, EQ-5D-5L + CO performed better for WAI-assessed work ability and for mental health measures (PHQ-4, SSD-12), while no additional benefit was observed when these measures were combined (Table <a href="#Tab5" data-ref-type="table">5</a>).

#### Explanatory power

Across all outcomes, multivariate models showed that adding a single bolt-on improved the explanatory power of the EQ-5D-5L, with the largest incremental gains observed for PCS (Δ adj. R<sup>2</sup> = 0.05) and WHODAS (Δ adj. R<sup>2</sup> = 0.03); univariate regressions revealed domain-specific patterns (Table <a href="#Tab6" data-ref-type="table">6</a>).

<div id="Tab6" class="table-wrap">

<div class="caption">

The explanatory power of EQ-5D-5L and bolt-ons for EQ VAS, SSD-12, PHQ-4, PCS-Score, PTSD, WHODAS and WAI (all T<sub>1</sub>)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Dimensions</th>
<th colspan="2" style="text-align: left;">EQ VAS (0–100)</th>
<th colspan="2" style="text-align: left;">SSD-12 (0–48)</th>
<th colspan="2" style="text-align: left;">PHQ-4 (0–12)</th>
<th colspan="2" style="text-align: left;">PCS-Score (0–59)</th>
<th colspan="2" style="text-align: left;">PTSD (0–24)</th>
<th colspan="2" style="text-align: left;">WHODAS (12–60)</th>
<th colspan="2" style="text-align: left;">WAI (7–49)</th>
</tr>
<tr>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="15" style="text-align: left;">Individual dimensions</td>
</tr>
<tr>
<td style="text-align: left;">  Mobility</td>
<td style="text-align: center;">0.343</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.253</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.191</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.268</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.181</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.424</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.313</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Self-care</td>
<td style="text-align: center;">0.156</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.095</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.088</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.088</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.117</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.239</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.116</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Usual activities</td>
<td style="text-align: center;"><strong>0.479</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.368</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.287</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.363</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.297</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.583</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.506</strong></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Pain/discomfort</td>
<td style="text-align: center;">0.411</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.330</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.228</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.372</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.223</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.418</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.425</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Anxiety/depression</td>
<td style="text-align: center;">0.317</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.358</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.550</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.250</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.370</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.413</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.332</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Cognition (CO)</td>
<td style="text-align: center;">0.357</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.330</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.301</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.397</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.296</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.484</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.404</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Social participation (SP)</td>
<td style="text-align: center;">0.369</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.329</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.353</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.264</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.398</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.567</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.401</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Combinations</td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L</td>
<td style="text-align: center;">0.593</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.524</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.588</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.495</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.459</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.725</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.627</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L + CO</td>
<td style="text-align: center;"><strong>0.611</strong></td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;"><strong>0.548</strong></td>
<td style="text-align: center;">0.024</td>
<td style="text-align: center;"><strong>0.605</strong></td>
<td style="text-align: center;">0.017</td>
<td style="text-align: center;"><strong>0.558</strong></td>
<td style="text-align: center;">0.053</td>
<td style="text-align: center;">0.482</td>
<td style="text-align: center;">0.023</td>
<td style="text-align: center;">0.759</td>
<td style="text-align: center;">0.034</td>
<td style="text-align: center;"><strong>0.655</strong></td>
<td style="text-align: center;">0.028</td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L + SP</td>
<td style="text-align: center;">0.601</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;">0.535</td>
<td style="text-align: center;">0.011</td>
<td style="text-align: center;">0.601</td>
<td style="text-align: center;">0.013</td>
<td style="text-align: center;">0.501</td>
<td style="text-align: center;">0.006</td>
<td style="text-align: center;"><strong>0.506</strong></td>
<td style="text-align: center;">0.047</td>
<td style="text-align: center;"><strong>0.770</strong></td>
<td style="text-align: center;">0.045</td>
<td style="text-align: center;">0.645</td>
<td style="text-align: center;">0.018</td>
</tr>
</tbody>
</table>

Δ, incremental R<sup>2</sup> compared to EQ-5D-5L; EQ VAS, Visual Analog Scale of the EQ-5D-5L; PCS-Score, Post-COVID syndrome PCS-Score; PHQ-4, Patient Health Questionnaire; SSD-12, Somatic Symptom Disorder-B criteria scale; PTSD, Short screening scale for DSM-IV posttraumatic stress disorder; WAI, Work Ability Index; WHODAS, WHO Disability Assessment Schedule 2.0; Δ, incremental R<sup>2</sup> compared to EQ-5D-5L

</div>

In multivariable models, predicting PCS symptom severity across prevalent health conditions (Table <a href="#Tab7" data-ref-type="table">7</a>), adding CO to the EQ-5D-5L consistently resulted in a notable increase in explanatory power (Δ adj. R<sup>2</sup> = 0.04–0.06), while adding SP yielded negligible changes in model performance (adj. R<sup>2</sup> ≤ 0.01). Univariate models showed the strongest crude associations for CO in most (4/6) conditions. Only for psychological and hormonal/metabolic conditions other items performed better.

<div id="Tab7" class="table-wrap">

<div class="caption">

The explanatory power (adjusted R<sup>2</sup>) of the EQ-5D-5L and bolt-on items (baseline PCS-Score as dependent variable) for the 6 most prevalent health conditions (n \> 200)

</div>

<table>
<thead>
<tr>
<th colspan="15" style="text-align: left;">PCS-Score (0–59)</th>
</tr>
<tr>
<th rowspan="2" style="text-align: left;">Dimensions</th>
<th colspan="2" style="text-align: left;">Total sample</th>
<th colspan="2" style="text-align: left;">Musculoskeletal disorders</th>
<th colspan="2" style="text-align: left;">Cardiovascular diseases</th>
<th colspan="2" style="text-align: left;">Psychological impairments</th>
<th colspan="2" style="text-align: left;">Hormonal/metabolic diseases</th>
<th colspan="2" style="text-align: left;">Respiratory diseases</th>
<th colspan="2" style="text-align: left;">Neurological and sensory disorders</th>
</tr>
<tr>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="15" style="text-align: left;">Individual dimensions</td>
</tr>
<tr>
<td style="text-align: left;">Mobility</td>
<td style="text-align: center;">0.268</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.233</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.238</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.189</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.268</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.212</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.257</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Self-care</td>
<td style="text-align: center;">0.088</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.085</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.085</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.070</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.099</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.064</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.090</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Usual activities</td>
<td style="text-align: center;">0.363</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.300</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.323</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.217</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.351</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.277</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.326</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">   Pain|discomfort</td>
<td style="text-align: center;">0.372</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.284</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.321</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.251</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.331</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.282</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.281</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Anxiety|depression</td>
<td style="text-align: center;">0.249</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.227</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.209</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.117</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.241</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.223</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.237</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Bolt-ons</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Cognition (CO)</td>
<td style="text-align: center;"><strong>0.397</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.333</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.339</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.216</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.337</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.346</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.329</strong></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Social participation (SP)</td>
<td style="text-align: center;">0.263</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.224</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.216</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.138</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.225</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.219</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.271</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">EQ-5D-5L(+ bolt-ons)</td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L</td>
<td style="text-align: center;">0.495</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.427</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.44</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.33</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.462</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.403</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.451</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L + CO</td>
<td style="text-align: center;"><strong>0.558</strong></td>
<td style="text-align: center;">0.063</td>
<td style="text-align: center;"><strong>0.487</strong></td>
<td style="text-align: center;">0.060</td>
<td style="text-align: center;"><strong>0.498</strong></td>
<td style="text-align: center;">0.058</td>
<td style="text-align: center;"><strong>0.383</strong></td>
<td style="text-align: center;">0.053</td>
<td style="text-align: center;"><strong>0.511</strong></td>
<td style="text-align: center;">0.049</td>
<td style="text-align: center;"><strong>0.477</strong></td>
<td style="text-align: center;">0.074</td>
<td style="text-align: center;"><strong>0.490</strong></td>
<td style="text-align: center;">0.039</td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L + SP</td>
<td style="text-align: center;">0.501</td>
<td style="text-align: center;">0.006</td>
<td style="text-align: center;">0.431</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;">0.442</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">0.335</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">0.461</td>
<td style="text-align: center;"> − 0.001</td>
<td style="text-align: center;">0.405</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">0.456</td>
<td style="text-align: center;">0.005</td>
</tr>
</tbody>
</table>

Δ, incremental R<sup>2</sup> compared to EQ-5D-5L; PCS-Score, Post-COVID syndrome PCS-Score

</div>

When predicting HRQoL using the EQ VAS (Table <a href="#Tab8" data-ref-type="table">8</a>), multivariable models indicated a modest additional contribution of CO (Δ adj. R<sup>2</sup> = 0.01–0.02), while adding SP to the EQ-5D-5L resulted in negligible changes (Δ adj. R<sup>2</sup> ≤ 0.01).

<div id="Tab8" class="table-wrap">

<div class="caption">

The explanatory power (adjusted R<sup>2</sup>) of the EQ-5D-5L and bolt-on items (baseline EQ VAS Score as dependent variable) for the 6 most prevalent health conditions (n \> 200)

</div>

<table>
<thead>
<tr>
<th colspan="15" style="text-align: left;">EQ VAS (0–100)</th>
</tr>
<tr>
<th rowspan="2" style="text-align: left;">Dimensions</th>
<th colspan="2" style="text-align: left;">Total sample</th>
<th colspan="2" style="text-align: left;">Musculoskeletal disorders</th>
<th colspan="2" style="text-align: left;">Cardiovascular diseases</th>
<th colspan="2" style="text-align: left;">Psychological impairments</th>
<th colspan="2" style="text-align: left;">Hormonal/metabolic diseases</th>
<th colspan="2" style="text-align: left;">Respiratory diseases</th>
<th colspan="2" style="text-align: left;">Neurological and sensory disorders</th>
</tr>
<tr>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">Adj. R<sup>2</sup></th>
<th style="text-align: left;">Δ</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="15" style="text-align: left;">Individual dimensions</td>
</tr>
<tr>
<td style="text-align: left;">  Mobility</td>
<td style="text-align: center;">0.343</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.304</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.321</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.294</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.377</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.351</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.333</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Self-care</td>
<td style="text-align: center;">0.156</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.162</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.148</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.161</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.177</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.166</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.207</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Usual activities</td>
<td style="text-align: center;"><strong>0.479</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.462</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.479</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.387</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.490</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.426</strong></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><strong>0.452</strong></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Pain/discomfort</td>
<td style="text-align: center;">0.411</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.386</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.381</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.307</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.406</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.377</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.373</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Anxiet/depression</td>
<td style="text-align: center;">0.317</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.299</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.286</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.222</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.313</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.275</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.262</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Bolt-ons</td>
</tr>
<tr>
<td style="text-align: left;">  Cognition (CO)</td>
<td style="text-align: center;">0.357</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.325</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.308</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.243</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.298</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.298</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.334</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  Social participation (SP)</td>
<td style="text-align: center;">0.369</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.338</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.360</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.276</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.333</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.338</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.362</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">EQ-5D-5L (+ bolt-ons)</td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L</td>
<td style="text-align: center;">0.593</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.576</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.578</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.515</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.603</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.564</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.568</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L + CO</td>
<td style="text-align: center;"><strong>0.611</strong></td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;"><strong>0.594</strong></td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;"><strong>0.592</strong></td>
<td style="text-align: center;">0.014</td>
<td style="text-align: center;"><strong>0.529</strong></td>
<td style="text-align: center;">0.014</td>
<td style="text-align: center;"><strong>0.617</strong></td>
<td style="text-align: center;">0.014</td>
<td style="text-align: center;"><strong>0.584</strong></td>
<td style="text-align: center;">0.020</td>
<td style="text-align: center;"><strong>0.583</strong></td>
<td style="text-align: center;">0.015</td>
</tr>
<tr>
<td style="text-align: left;">  EQ-5D-5L + SP</td>
<td style="text-align: center;">0.601</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;">0.584</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;">0.589</td>
<td style="text-align: center;">0.011</td>
<td style="text-align: center;">0.521</td>
<td style="text-align: center;">0.006</td>
<td style="text-align: center;">0.607</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;">0.575</td>
<td style="text-align: center;">0.011</td>
<td style="text-align: center;">0.573</td>
<td style="text-align: center;">0.005</td>
</tr>
</tbody>
</table>

Δ, incremental R<sup>2</sup> compared to EQ-5D-5L

</div>

## Discussion

This study investigated whether adding two existing bolt-ons, cognition and social participation, improved the measurement properties of the EQ-5D-5L in a German cohort of HCW with confirmed occupational SARS-CoV-2 infection and with prominent post-COVID syndromes. It is one of the first to evaluate the added value of CO and SP bolt-ons to the EQ-5D-5L in a large, well-defined post-COVID sample. The use of multiple validated instruments and a 12-month follow-up allowed for robust assessment of psychometric properties. In addition, known groups and explanatory power analyses were conducted across a wide range of clinically relevant subgroups, enhancing the interpretability and applicability of results.

Both bolt-ons showed acceptable distributions, with a slight reduction in ceiling effects compared to the EQ-5D-5L alone, more pronounced for CO than SP (‘11111’ = 18.8% vs. ‘111111’<sub>CO</sub> = 14.8% and ‘111111’<sub>SP</sub> = 17.8%). While most dimensions exhibited high ceilings, CO and pain/discomfort captured a wider spread of reported problems. Construct validity was supported by expected correlation patterns, that is moderate to high correlations with related constructs, e.g. SP and WHODAS 2.0, and no to poor correlations with non-related constructs, e.g. CO and BRS. The inclusion of bolt-ons resulted in comparable or improved known-groups validity across most comparisons, with CO outperforming SP. CO showed the highest explanatory power for PCS-Scores (adj. R<sup>2</sup> = 0.33–0.39) in univariate models. In multivariate models, the bolt-ons had small to moderate explanatory value.

The addition of a CO bolt-on to the EQ-5D-5L has been explored in various studies to enhance the instrument’s ability to capture cognitive health aspects, particularly in populations with neurological conditions or cognitive impairments. The findings of this study align with and expand upon previous evidence on EQ-5D-5L bolt-ons. Consistent with earlier findings, CO demonstrated added value in terms of construct and known-groups validity \[67\]. This supports prior work showing that cognitive limitations are not adequately captured by the core instrument \[10, 13\], especially in populations with neurological or post-infectious conditions \[10, 16, 35, 68\]. Notably, the ceiling was reduced by the inclusion of bolt-ons, mirroring findings from studies in traumatic brain injury, post-traumatic stress disorder and coeliac disease populations \[69–71\]. The particularly strong correlation of both CO and SP with generic instruments (e.g. WHODAS 2.0, WAI) underscores their relevance in capturing broader health dimensions.

Recent longitudinal evidence from non-hospitalized post-COVID-19 patients further contextualizes these findings. In a validation study of EQ-5D-5L breathing and cognition bolt-ons, Stavem and Garratt (2026) demonstrated acceptable construct validity for both bolt-ons; however, only the respiratory bolt-on contributed meaningfully to additional variance explained in EQ VAS scores, whereas the cognition bolt-on added little incremental explanatory value \[72, 73\]. This is consistent with our results, suggesting that cognition bolt-ons primarily enhance content validity, discrimination between clinically relevant groups, and explanatory power for symptom-based outcomes (e.g., PCS severity), rather than substantially improving the explanation of global self-rated health.

To the best of our knowledge, evidence on the SP bolt-on remains limited, as most studies addressing the social aspects of quality of life have focused on social relationships or isolation rather than participation in societal roles and activities \[5, 48, 67, 74, 75\]. Herein, SP showed weaker performance overall, adding little explanatory value and only small improvements in some known-groups comparisons. This may partly reflect conceptual overlap with the UA dimension, as indicated by the moderate to strong correlations between these dimensions, suggesting that the usefulness of the SP bolt-on may be context-dependent and warranting further validation \[17\].

### Limitations

Several limitations must be acknowledged. First, the sample consisted exclusively of HCW, which may limit generalizability to the broader post-COVID population. Second, self-reported data are subject to recall and reporting biases, particularly given the retrospective design of the survey. Moreover, self-completion of the cognition bolt-on may be challenging for individuals with cognitive impairment, potentially requiring interviewer or proxy administration \[76, 77\]; consequently, EuroQol has called for further research on its validity and usability in these populations \[78\]. Third, interpretation of SSD-12 scores is complicated by varying recommended cut-offs across settings: while a threshold of ≥ 13 seems appropriate for primary care and population-based samples, clinical studies suggest higher thresholds (e.g., ≥ 22 or ≥ 29), highlighting the need for further diagnostic validation \[63–65\]. Fourth, the absence of objective clinical endpoints—such as medically confirmed rather than self-reported diagnoses/syndromes—limits the strength of conclusions regarding group comparisons based on these anchors. Fifth, although our findings suggest good feasibility of the descriptive system and acceptable feasibility of the EQ VAS, they should be interpreted with caution, as a subset of n = 234 respondents did not complete any EQ-5D-5L items, likely reflecting survey fatigue at the end of a lengthy questionnaire. Sixth, since fatigue and respiratory symptoms were already captured by the PCS-Score, no additional EQ-5D bolt-ons were included; however, evaluating such bolt-ons could further advance the evidence base and merits future research. Finally, the bolt-on items referred to a 3-month recall period, whereas the EQ-5D items referred to ‘*today’,* which may complicate comparisons and affect reported levels. Evidence from SF-12/SF-36 and SF-6D research suggests that differing recall periods can influence mean scores and sensitivity to recent changes, though psychometric structure is generally preserved \[79, 80\]. Chua et al. (2025) found that EQ-5D-5L variants with longer recall periods (1–4 weeks) showed reduced ceiling effects and superior or comparable reliability, validity, and responsiveness relative to the standard ‘*today*’ version in patients with obstructive airway diseases \[81\].

Differing recall periods may have introduced recall bias because the nature of the reported construct may affect recall accuracy in different ways. Evidence suggests that longer recall periods can alter the level and variability of self‑reported outcomes in patient‑reported instruments, as recall accuracy appears to deteriorate when respondents are asked to aggregate experiences over extended periods rather than report momentary states \[82\]. This may be particularly relevant for SP, which reflects variable and context‑dependent activities over time and may therefore be more susceptible to recall and aggregation effects when longer reference periods are used. By contrast, cognitive difficulties are often experienced and internalized as more persistent impairments with less moment‑to‑moment fluctuation, and may therefore be less affected by differences in recall period \[83, 84\]. Caution is therefore warranted when interpreting differences across dimensions and recall periods.

Against this background, our findings may offer preliminary input for the ongoing development of the EQ-5D Bolt-on Toolbox: the consistent added value of the CO bolt-on aligns with cognition being considered as a candidate domain, whereas the more limited and context-dependent contribution of SP observed here—together with evidence of conceptual overlap and recall sensitivity—may help inform future prioritization and validation efforts.

## Conclusion

Adding a cognition (CO) bolt-on appears to improve specific psychometric properties of the EQ-5D-5L, including distributional properties, known groups validity, and explanatory power, in HCW with self-reported occupational SARS-CoV-2 infection and post-COVID syndromes, whereas a social participation (SP) bolt-on shows some improvement in known-groups validity but adds little explanatory power. Results suggest that particularly CO can improve the instrument’s ability to explain post-COVID health burden/PCS symptom severity, supporting their added value in post-acute care and recovery research. However, their added value in explaining self-reported health outcomes appears limited.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

## Acknowledgements

The authors thank the German Social Accident Insurance provider for non-state institutions within the Health and Welfare Service Sectors (BGW) for supporting the study by providing access to a randomized sample and managing the mailing of invitation and reminder letters.

## Author contributions

All authors contributed to the conception and design of this sub-study; the main study was designed by MH. Data collection was performed by LL and MH. Data preparation and analysis was performed by IB. The first draft of the manuscript was written by IB and all authors commented on previous versions of the manuscript and helped revising the manuscript. All authors read and approved the final manuscript. All authors declare that this contribution reflects their original work.

## Funding

Open Access funding enabled and organized by Projekt DEAL. This study was conducted as a sub-study of a project funded by the German Federal Ministry of Education and Research (BMBF FKZ: 01EP2110A) and was funded by EuroQol Research Foundation (grant no. 1719-RA).

## Declarations

### Competing interests

IB and MFBJ are members of the EuroQol Group. Views expressed in the article are those of the authors and are not necessarily those of the EuroQol Research Foundation. IB and MFBJ received research funding and travel support from the EuroQol Research Foundation. LL and MH have no relevant financial or non-financial interests to disclose.

### Ethical approval

This study was performed in line with the principles of the Declaration of Helsinki. Approval was granted by the Local Ethics Committee of the University Medical Center Hamburg-Eppendorf (No. LPEK-0518). The study was registered with the German Clinical Trials Register (DRKS) under ID DRKS00029314, with regular updates.

### Consent to participate

Participation was anonymous, and active consent was required through a mandatory field in the online survey.

## Footnotes

## References

## References

1. Herdman, M., Gudex, C., Lloyd, A., Janssen, M., Kind, P., Parkin, D., Bonsel, G., & Badia, X. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research: An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,20(10), 1727–1736. 10.1007/s11136-011-9903-x

2. Myers, C., & Wilks, D. (1999). Comparison of EuroQol EQ-5D and SF-36 in patients with chronic fatigue syndrome. Quality of Life Research : An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,8(1–2), 9–16. 10.1023/a:1026459027453

3. Spronk, I., Polinder, S., Bonsel, G. J., Janssen, M. F., & Haagsma, J. A. (2022). Adding a fatigue item to the EQ-5D-5L improves its psychometric performance in the general population. Journal of Patient-Reported Outcomes,6(1), 1. 10.1186/s41687-021-00406-x

4. Gunther, O., Roick, C., Angermeyer, M. C., & Konig, H. H. (2007). The EQ-5D in alcohol dependent patients: Relationships among health-related quality of life, psychopathology and social functioning. Drug and Alcohol Dependence,86(2–3), 253–264. 10.1016/j.drugalcdep.2006.07.001

5. Sussex, A. K., Rencz, F., Gaydon, M., Lloyd, A., & Gallop, K. (2025). Exploring the content validity of the EQ-5D-5L and four bolt-ons (skin irritation, self-confidence, sleep, social relationships) in atopic dermatitis and chronic urticaria. Quality of Life Research : An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,34(4), 991–1002. 10.1007/s11136-024-03875-x

6. Chen, G., & Olsen, J. A. (2023). Extending the EQ-5D: The case for a complementary set of 4 psycho-social dimensions. Quality of Life Research : An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,32(2), 495–505. 10.1007/s11136-022-03243-7

7. Chen, G., & Olsen, J. A. (2020). Filling the psycho-social gap in the EQ-5D: The empirical support for four bolt-on dimensions. Quality of Life Research : An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,29(11), 3119–3129. 10.1007/s11136-020-02576-5

8. Sonntag, M., Konnopka, A., Leichsenring, F., Salzer, S., Beutel, M. E., Herpertz, S., Hiller, W., Hoyer, J., Joraschky, P., Nolting, B., Pohlmann, K., Stangier, U., Strauss, B., Willutzki, U., Wiltink, J., Leibing, E., & Konig, H. H. (2013). Reliability, validity and responsiveness of the EQ-5D in assessing and valuing health status in patients with social phobia. Health and Quality of Life Outcomes,11, 215. 10.1186/1477-7525-11-215

9. Ophuis, R. H., Janssen, M. F., Bonsel, G. J., Panneman, M. J., Polinder, S., & Haagsma, J. A. (2019). Health-related quality of life in injury patients: The added value of extending the EQ-5D-3L with a cognitive dimension. Quality of Life Research : An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,28(7), 1941–1949. 10.1007/s11136-019-02156-2

10. Janssen, M. F., Krabbe, P. F. M., Lamers, L., Oppe, M., Stolk, E., Vermeulen, K., & van Hout, B. A. (2014). The cognition dimension revisited. A detailed study on its added value and interactions with EQ-5D core dimensions. In 30th scientific plenary meeting of the EuroQol group, Montreal, Canada.

11. Mulhern, B. J., Sampson, C., Haywood, P., Addo, R., Page, K., Mott, D., Shah, K., Janssen, M. F., & Herdman, M. (2022). Criteria for developing, assessing and selecting candidate EQ-5D bolt-ons. Quality of Life Research : An International Journal of Quality of Life Aspects in Treatment, Care and Prevention,31(10), 3041–3048. 10.1007/s11136-022-03138-7

12. Geraerds, A., Bonsel, G. J., Janssen, M. F., Finch, A. P., Polinder, S., & Haagsma, J. A. (2021). Methods used to identify, test, and assess impact on preferences of bolt-ons: A systematic review. Value in Health,24(6), 901–916. 10.1016/j.jval.2020.12.011

13. Finch, A. P., Brazier, J., & Mukuria, C. (2021). Selecting bolt-on dimensions for the EQ-5D: Testing the impact of hearing, sleep, cognition, energy, and relationships on preferences using pairwise choices. Medical Decision Making,41(1), 89–99. 10.1177/0272989X20969686

14. Finch, A. P., Brazier, J. E., & Mukuria, C. (2019). Selecting bolt-on dimensions for the EQ-5D: Examining their contribution to health-related quality of life. Value in Health,22(1), 50–61. 10.1016/j.jval.2018.07.001

15. Finch, A. P., John, B., & Clara, M. (2017). An investigation of methods for identifying and selecting bolt-on dimensions : The EQ-5D-5L case study. University of Sheffield.

16. Rencz, F., Pangestu, S., Mulhern, B., Finch, A. P., & Janssen, M. F. (2025). Development and use of cognition bolt-ons for the EQ-5D-3L and EQ-5D-5L: A systematic review. Value in Health. 10.1016/j.jval.2025.05.015. doi:10.1016/j.jval.2025.11.005

17. Cheuk Wai Ng, C., Liao, M., Luo, N., Wong, E. L.-Y., Mulhern, B., Finch, A. P., Olsen, J. A., Peasgood, T., & Rencz, F. (2025). Social relationship bolt-ons for the EQ-5D-3L and EQ-5D-5L: A systematic review. In EuroQol academy meeting 2025.

18. Global Burden of Disease Long COVID Collaborators, Wulf Hanson, S., Abbafati, C., Aerts, J. G., Al-Aly, Z., Ashbaugh, C., Ballouz, T., Blyuss, O., Bobkova, P., Bonsel, G., Borzakova, S., Buonsenso, D., Butnaru, D., Carter, A., Chu, H., De Rose, C., Diab, M. M., Ekbom, E., El Tantawi, M., & Vos, T. (2022). Estimated global proportions of individuals with persistent fatigue, cognitive, and respiratory symptom clusters following symptomatic COVID-19 in 2020 and 2021. JAMA,328(16), 1604–1615. 10.1001/jama.2022.18931

19. Michelen, M., Manoharan, L., Elkheir, N., Cheng, V., Dagens, A., Hastie, C., O’Hara, M., Suett, J., Dahmash, D., Bugaeva, P., Rigby, I., Munblit, D., Harriss, E., Burls, A., Foote, C., Scott, J., Carson, G., Olliaro, P., Sigfrid, L., & Stavropoulou, C. (2021). Characterising long COVID: A living systematic review. BMJ Global Health,6(9), 5427. 10.1136/bmjgh-2021-005427

20. Klein, D. O., Waardenburg, S. F., Janssen, E., Wintjens, M., Imkamp, M., Heemskerk, S. C. M., Birnie, E., Bonsel, G. J., Warle, M. C., Jacobs, L. M. C., Hemmen, B., Verbunt, J., van Bussel, B. C. T., van Santen, S., Kietelaer, B., Jansen, G., Klok, F. A., de Kruif, M. D., Vernooy, K., & van Kuijk, S. M. J. (2025). Two years and counting: a prospective cohort study on the scope and severity of post-COVID symptoms across diverse patient groups in the Netherlands-insights from the CORFU study. British Medical Journal Open,15(9), e093639. 10.1136/bmjopen-2024-093639

21. Nalbandian, A., Sehgal, K., Gupta, A., Madhavan, M. V., McGroder, C., Stevens, J. S., Cook, J. R., Nordvig, A. S., Shalev, D., Sehrawat, T. S., Ahluwalia, N., Bikdeli, B., Dietz, D., Der-Nigoghossian, C., Liyanage-Don, N., Rosner, G. F., Bernstein, E. J., Mohan, S., Beckley, A. A., & Wan, E. Y. (2021). Post-acute COVID-19 syndrome. Nature Medicine,27(4), 601–615. 10.1038/s41591-021-01283-z

22. Ping, W., Zheng, J., Niu, X., Guo, C., Zhang, J., Yang, H., & Shi, Y. (2020). Evaluation of health-related quality of life using EQ-5D in China during the COVID-19 pandemic. PLoS ONE,15(6), e0234850. 10.1371/journal.pone.0234850

23. Hamdan, A., Ghanim, M., & Mosleh, R. (2021). COVID-19 confinement and related well being measurement using the EQ-5D questionnaire: A survey among the Palestinian population. International Journal of Clinical Practice,75(10), e14621. 10.1111/ijcp.14621

24. (2024). COVID-19 rapid guideline: Managing the long-term effects of COVID-19. https://www.ncbi.nlm.nih.gov/pubmed/33555768

25. Garratt, A. M., & Stavem, K. (2024). COVID-19 and self-reported health of the Norwegian adult general population: A longitudinal study 3 months before and 9 months into the pandemic. PLoS ONE,19(10), e0312201. 10.1371/journal.pone.0312201

26. Afshari, S., Poder, T. G., Daroudi, R., Sari, A. A., & Ameri, H. (2025). EQ-5D-5L Iranian population norms derived from the local value set during the COVID-19 pandemic. Quality of Life Research. 10.1007/s11136-025-04089-5

27. Webb, E. J. D., Kind, P., Meads, D., & Martin, A. (2024). COVID-19 and EQ-5D-5L health state valuation. European Journal of Health Economics,25(1), 117–145. 10.1007/s10198-023-01569-8

28. Poteet, S., & Craig, B. M. (2021). QALYs for COVID-19: A comparison of US EQ-5D-5L value sets. Patient (Auckland, N.Z.),14(3), 339–345. 10.1007/s40271-021-00509-z

29. Hay, J. W., Gong, C. L., Jiao, X., Zawadzki, N. K., Zawadzki, R. S., Pickard, A. S., Xie, F., Crawford, S. A., & Gu, N. Y. (2021). A US population health survey on the impact of COVID-19 using the EQ-5D-5L. Journal of General Internal Medicine,36(5), 1292–1301. 10.1007/s11606-021-06674-z

30. Long, D., Bonsel, G. J., Lubetkin, E. I., Janssen, M. F., & Haagsma, J. A. (2022). Anxiety, depression, and social connectedness among the general population of eight countries during the COVID-19 pandemic. Archives of Public Health,80(1), 237. 10.1186/s13690-022-00990-4

31. Long, D., Bonsel, G. J., Lubetkin, E. I., Yfantopoulos, J. N., Janssen, M. F., & Haagsma, J. A. (2022). Health-related quality of life and mental Well-Being during the COVID-19 pandemic in five countries: A one-year longitudinal study. Journal of Clinical Medicine,11(21), 6467. 10.3390/jcm11216467

32. Sun, X., Di Fusco, M., Puzniak, L., Coetzer, H., Zamparo, J. M., Tabak, Y. P., & Cappelleri, J. C. (2023). Assessment of retrospective collection of EQ-5D-5L in a US COVID-19 population. Health and Quality of Life Outcomes,21(1), 103. 10.1186/s12955-023-02187-x

33. Lubetkin, E. I., Long, D., Haagsma, J. A., Janssen, M. F., & Bonsel, G. J. (2022). Health inequities as measured by the EQ-5D-5L during COVID-19: Results from New York in healthy and diseased persons. PLoS ONE,17(7), e0272252. 10.1371/journal.pone.0272252

34. Gidey, K., Niriayo, Y. L., Asgedom, S. W., & Lubetkin, E. (2025). Health-related quality of life in COVID-19 patients: A systematic review and meta-analysis of EQ-5D studies. Health and Quality of Life Outcomes,23(1), 97. 10.1186/s12955-025-02421-8

35. Janols, H., Wadsten, C., Forssell, C., Raffeti, E., Janson, C., Zhou, X., & Kisiel, M. A. (2024). Enhancing EQ-5D-5L sensitivity in capturing the most common symptoms in post-COVID-19 patients: An exploratory cross-sectional study with a focus on fatigue, memory/concentration problems and dyspnea dimensions. International Journal of Environmental Research and Public Health,21(5), 591. 10.3390/ijerph21050591

36. Vizheh, M., Qorbani, M., Arzaghi, S. M., Muhidin, S., Javanmard, Z., & Esmaeili, M. (2020). The mental health of healthcare workers in the COVID-19 pandemic: A systematic review. Journal of Diabetes & Metabolic Disorders,19(2), 1967–1978. 10.1007/s40200-020-00643-9

37. Al-Oraibi, A., Woolf, K., Naidu, J., Nellums, L. B., Pan, D., Sze, S., Tarrant, C., Martin, C. A., Gogoi, M., Nazareth, J., Divall, P., Dempsey, B., Lamb, D., & Pareek, M. (2025). Global prevalence of long COVID and its most common symptoms among healthcare workers: A systematic review and meta-analysis. BMJ Public Health,3(1), e000269. 10.1136/bmjph-2023-000269

38. Bundesamt, S. https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Gesundheitspersonal/_inhalt.html

39. info@corona-in-zahlen.de. (2025). Corona in Zahlen. Retrieved June 06, 2025, from https://www.corona-in-zahlen.de/weltweit/deutschland/

40. Dechent, F., Mayer, G., Hummel, S., Moritz, S., Benoy, C., Almeida, R., Duran, R. L., Ribeiro, O., Frisardi, V., Tarricone, I., Ferrari, S., Lemogne, C., Huber, C., Weidt, S., & Schultz, J. H. (2024). COVID-19 and mental distress among health professionals in eight European countries during the third wave: A cross-sectional survey. Scientific Reports,14(1), 21333. 10.1038/s41598-024-72396-x

41. Hummel, S., Oetjen, N., Du, J., Posenato, E., de Resen Almeida, R. M., Losada, R., Ribeiro, O., Frisardi, V., Hopper, L., Rashid, A., Nasser, H., Konig, A., Rudofsky, G., Weidt, S., Zafar, A., Gronewold, N., Mayer, G., & Schultz, J. H. (2021). Mental health among medical professionals during the COVID-19 pandemic in eight European countries: Cross-sectional survey study. Journal of Medical Internet Research,23(1), e24983. 10.2196/24983

42. Erim, Y., Geiser, F., Beschoner, P., Jerg-Bretzke, L., Weidner, K., Albus, C., Baranowski, A. M., Mogwitz, S., & Morawa, E. (2024). Workplace-related stress experience and mental health of healthcare workers during the COVID-19 pandemic: Risk and protective factors from the VOICE study. Bundesgesundheitsblatt, Gesundheitsforschung, Gesundheitsschutz,67(11), 1248–1255. 10.1007/s00103-024-03954-x

43. Niecke, A., Henning, M., Hellmich, M., Erim, Y., Morawa, E., Beschoner, P., Jerg-Bretzke, L., Geiser, F., Baranowski, A. M., Weidner, K., Mogwitz, S., & Albus, C. (2025). Mental distress of intensive care staff in Germany during the COVID-19 pandemic. Results from the VOICE study. Medizinische Klinik - Intensivmedizin und Notfallmedizin,120(4), 300–306. 10.1007/s00063-024-01164-6

44. Schulze, J., Lind, L., Rojas Albert, A., Lüdtke, L., Hensen, J., Bergelt, C., Härter, M., & Pohontsch, N. J. (2024). German general practitioners’ experiences of managing post-COVID-19 syndrome: A qualitative interview study. European Journal of General Practice,30(1), 2413095. 10.1080/13814788.2024.2413095

45. Lüdtke, L., Haller-Wolf, J., Kriston, L., Koch, U., Nienhaus, A., & Härter, M. (2024). Post-COVID in healthcare workers and its consequences on quality of life, activities, participation, need for rehabilitation and care experiences: Protocol of a cohort study. British Medical Journal Open,14(11), e083422. 10.1136/bmjopen-2023-083422

46. Nitschke, J. P., Forbes, P. A. G., Ali, N., Cutler, J., Apps, M. A. J., Lockwood, P. L., & Lamm, C. (2021). Resilience during uncertainty? Greater social connectedness during COVID-19 lockdown is associated with reduced distress and fatigue. British Journal of Health Psychology,26(2), 553–569. 10.1111/bjhp.12485

47. Henson, G. J., van der Mei, I., Taylor, B. V., Claflin, S. B., Palmer, A. J., Chen, G., & Campbell, J. A. (2025). The health-related quality of life impact of the COVID-19 pandemic on people living with multiple sclerosis and the general population: A comparative study utilizing the EQ-5D-5L with psychosocial bolt-ons. Brain and Behavior,15(1), e70210. 10.1002/brb3.70210

48. Campbell, J. A., Ahmad, H., Chen, G., van der Mei, I., Taylor, B. V., Claflin, S., Henson, G. J., Simpson-Yap, S., Laslett, L. L., Hawkes, K., Hurst, C., Waugh, H., & Palmer, A. J. (2023). Validation of the EQ-5D-5L and psychosocial bolt-ons in a large cohort of people living with multiple sclerosis in Australia. Quality of Life Research,32(2), 553–568. 10.1007/s11136-022-03214-y

49. Bahmer, T., Borzikowsky, C., Lieb, W., Horn, A., Krist, L., Fricke, J., Scheibenbogen, C., Rabe, K. F., Maetzler, W., Maetzler, C., Laudien, M., Frank, D., Ballhausen, S., Hermes, A., Miljukov, O., Haeusler, K. G., Mokhtari, N. E. E., Witzenrath, M., Vehreschild, J. J., … J. J. Group, N. s. (2022). Severity, predictors and clinical correlates of post-COVID syndrome (PCS) in Germany: A prospective, multi-centre, population-based cohort study. EClinicalMedicine,51, 101549. 10.1016/j.eclinm.2022.101549

50. Trifunovic-Koenig, M., Strametz, R., Gerber, B., Mantri, S., & Bushuven, S. (2022). Validation of the German version of the Moral Injury symptom and support scale for health professionals (G-MISS-HP) and its correlation to the second victim phenomenon. International Journal of Environmental Research and Public Health. 10.3390/ijerph19084857. doi:10.3390/ijerph192316016

51. Mantri, S., Lawson, J. M., Wang, Z., & Koenig, H. G. (2021). Prevalence and predictors of moral injury symptoms in health care professionals. Journal of Nervous and Mental Disease,209(3), 174–180. 10.1097/NMD.0000000000001277

52. Kroenke, K., Spitzer, R. L., Williams, J. B., & Löwe, B. (2009). An ultra-brief screening scale for anxiety and depression: The PHQ-4. Psychosomatics,50(6), 613–621. 10.1176/appi.psy.50.6.613

53. Löwe, B., Wahl, I., Rose, M., Spitzer, C., Glaesmer, H., Wingenfeld, K., Schneider, A., & Brähler, E. (2010). A 4-item measure of depression and anxiety: Validation and standardization of the patient health questionnaire-4 (PHQ-4) in the general population. Journal of Affective Disorders,122(1–2), 86–95. 10.1016/j.jad.2009.06.019

54. Toussaint, A., Löwe, B., Brähler, E., & Jordan, P. (2017). The somatic symptom disorder-B criteria scale (SSD-12): Factorial structure, validity and population-based norms. Journal of Psychosomatic Research,97, 9–17. 10.1016/j.jpsychores.2017.03.017

55. Toussaint, A., Murray, A. M., Voigt, K., Herzog, A., Gierk, B., Kroenke, K., Rief, W., Henningsen, P., & Löwe, B. (2016). Development and validation of the somatic symptom disorder-B criteria scale (SSD-12). Psychosomatic Medicine,78(1), 5–12. 10.1097/PSY.0000000000000240

56. Toussaint, A., Riedl, B., Kehrer, S., Schneider, A., Löwe, B., & Linde, K. (2018). Validity of the somatic symptom disorder-B criteria scale (SSD-12) in primary care. Family Practice,35(3), 342–347. 10.1093/fampra/cmx116

57. Breslau, N., Peterson, E. L., Kessler, R. C., & Schultz, L. R. (1999). Short screening scale for DSM-IV posttraumatic stress disorder. The American Journal of Psychiatry,156(6), 908–911. 10.1176/ajp.156.6.908

58. Vaganian, L., Bussmann, S., Boecker, M., Kusch, M., Labouvie, H., Gerlach, A. L., & Cwik, J. C. (2021). An item analysis according to the Rasch model of the German 12-item WHO disability assessment schedule (WHODAS 2.0). Quality of Life Research,30(10), 2929–2938. 10.1007/s11136-021-02872-8

59. Ilmarinen, J. (2009). Work ability–a comprehensive concept for occupational health research and prevention. Scandinavian Journal of Work, Environment & Health,35(1), 1–5. 10.5271/sjweh.1304

60. Ilmarinen, V., Ilmarinen, J., Huuhtanen, P., Louhevaara, V., & Nasman, O. (2015). Examining the factorial structure, measurement invariance and convergent and discriminant validity of a novel self-report measure of work ability: Work ability–personal radar. Ergonomics,58(8), 1445–1460. 10.1080/00140139.2015.1005167

61. Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). L. Erlbaum Associates.

62. Feng, Y. S., Jiang, R., Pickard, A. S., & Kohlmann, T. (2022). Combining EQ-5D-5L items into a level summary score: Demonstrating feasibility using non-parametric item response theory using an international dataset. Quality of Life Research,31(1), 11–23. 10.1007/s11136-021-02922-1

63. Jung, S., Shin, J. S., Lee, S. H., Lee, S., Kim, J., Son, K. L., Hahm, B. J., & Yeom, C. W. (2024). Reliability and validity of the Korean version of the somatic symptom disorder-B criteria scale in a clinical population. Psychiatry Investigation,21(2), 165–173. 10.30773/pi.2023.0352

64. von Schrottenberg, V., T, A., Hapfelmeier, A., Teusen, C., Riedl, B., Henningsen, P., Gensichen, J., Schneider, A., & Linde, K. (2024). Lessons learned from applying established cut-off values of questionnaires to detect somatic symptom disorders in primary care: A cross-sectional study. Frontiers in Psychiatry,14, 1289186. 10.3389/fpsyt.2023.1289186

65. van der Feltz-Cornelis, C. M., Sweetman, J., van Eck van der Sluijs, J. F., Kamp, C. A. D., de Vroege, L., & de Beurs, E. (2023). Diagnostic accuracy of the Dutch version of the somatic symptom disorder-B criteria scale (SSD-12) compared to the Whiteley index (WI) and PHQ-15 in a clinical population. Journal of Psychosomatic Research,173, 111460. 10.1016/j.jpsychores.2023.111460

66. Bethge, M., Radoschewski, F. M., & Gutenbrunner, C. (2012). The work ability index as a screening tool to identify the need for rehabilitation: Longitudinal findings from the Second German sociomedical panel of employees. Journal of Rehabilitation Medicine,44(11), 980–987. 10.2340/16501977-1063

67. Rencz, F., & Janssen, M. F. (2024). Testing the psychometric properties of 9 bolt-ons for the EQ-5D-5L in a general population sample. Value in Health,27(7), 943–954. 10.1016/j.jval.2024.03.2195

68. Del Corral, T., Fabero-Garrido, R., Plaza-Manzano, G., Navarro-Santana, M. J., Fernandez-de-Las-Penas, C., & Lopez-de-Uralde-Villanueva, I. (2023). Minimal clinically important differences in EQ-5D-5L index and VAS after a respiratory muscle training program in individuals experiencing long-term post-COVID-19 symptoms. Biomedicines. 10.3390/biomedicines11092522

69. Geraerds, A., Bonsel, G. J., Janssen, M. F., de Jongh, M. A., Spronk, I., Polinder, S., & Haagsma, J. A. (2019). The added value of the EQ-5D with a cognition dimension in injury patients with and without traumatic brain injury. Quality of Life Research,28(7), 1931–1939. 10.1007/s11136-019-02144-6

70. Angyal, M. M., Janssen, M. F., Lakatos, P. L., Brodszky, V., & Rencz, F. (2025). The added value of the cognition, dining, gastrointestinal problems, sleep and tiredness bolt-on dimensions to the EQ-5D-5L in patients with coeliac disease. European Journal of Health Economics,26(3), 473–485. 10.1007/s10198-024-01719-6

71. Geraerds, A., Bonsel, G. J., Polinder, S., Panneman, M. J. M., Janssen, M. F., & Haagsma, J. A. (2020). Does the EQ-5D-5L benefit from extension with a cognitive domain: Testing a multi-criteria psychometric strategy in trauma patients. Quality of Life Research,29(9), 2541–2551. 10.1007/s11136-020-02496-4

72. Stavem, K., & Garratt, A. M. (2026). Correction: Validity of EQ-5D-5L breathing and cognition bolt-ons in non-hospitalized patients after COVID-19. Quality of Life Research. 10.1007/s11136-026-04188-x

73. Stavem, K., & Garratt, A. M. (2026). Validity of EQ-5D-5L breathing and cognition bolt-ons in non-hospitalized patients after COVID-19. Quality of Life Research,35(2), 31. 10.1007/s11136-025-04133-4

74. Xu, R. H., Rencz, F., Sun, R., Dong, D., & Zhang, S. (2025). Development and testing of the psychometric properties of 20 bolt-on items for the EQ-5D-5L across 31 rare diseases. Value Health. 10.1016/j.jval.2025.01.006. doi:10.1016/j.jval.2025.08.002

75. Chua, A. P., Finch, A. P., Rahman, S. A., Cruz, M., Montaniel, E. N., Ravichandran, K., & Luo, N. (2025). Developing and testing a patient-reported outcome measure for patients with sleep disturbances using EQ-5D and condition-specific bolt-ons: A mixed method study. Quality of Life Research. 10.1007/s11136-025-03985-0. doi:10.1007/s11136-025-04016-8

76. Michalowsky, B., Xie, F., Kohlmann, T., Graske, J., Wubbeler, M., Thyrian, J. R., & Hoffmann, W. (2020). Acceptability and validity of the EQ-5D in patients living with dementia. Value Health,23(6), 760–767. 10.1016/j.jval.2020.01.022

77. Marten, O., & Greiner, W. (2022). Feasibility pr operties of the EQ-5D-3L and 5L in the general population: Evidence from the GP Patient Survey on the impact of age. Health Econ Rev,12(1), 28. 10.1186/s13561-022-00374-y

78. (2025). 20th joint call EuroQol working groups September 2025. EuroQol Research Foundation. Retrieved Dec 12, 2025, from.

79. Keller, S. D., Bayliss, M. S., Ware, J. E., Jr., Hsu, M. A., Damiano, A. M., & Goss, T. F. (1997). Comparison of responses to SF-36 health survey questions with one-week and four-week recall periods. Health Services Research,32(3), 367–384.

80. Topp, J., Andrees, V., Heesen, C., Augustin, M., & Blome, C. (2019). Recall of health-related quality of life: How does memory affect the SF-6D in patients with psoriasis or multiple sclerosis? A prospective observational study in Germany. British Medical Journal Open,9(11), e032859. 10.1136/bmjopen-2019-032859

81. Chua, A. P., Janssen, M. F., Cheng, L. J., Busschbach, J., & Luo, N. (2024). An exploratory study of alternative time frames and descriptors for EQ-5D-5L in obstructive airway diseases using mixed methods. Value Health,27(11), 1564–1572. 10.1016/j.jval.2024.07.004

82. Arizmendi, C., Wang, S., Kaplan, S., & Weinfurt, K. (2024). Evaluating recall periods for patient-reported outcome measures: A systematic review of quantitative methods. Value Health,27(4), 518–526. 10.1016/j.jval.2024.01.016

83. Peasgood, T., Caruana, J. M., & Mukuria, C. (2023). Systematic review of the effect of a one-day versus seven-day recall duration on patient reported outcome measures (PROMs). Patient,16(3), 201–221. 10.1007/s40271-022-00611-w

84. Norquist, J. M., Girman, C., Fehnel, S., DeMuro-Mercon, C., & Santanello, N. (2012). Choice of recall period for patient-reported outcome (PRO) measures: Criteria for consideration. Quality of Life Research,21(6), 1013–1020. 10.1007/s11136-011-0003-8

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary Material 1

</div>

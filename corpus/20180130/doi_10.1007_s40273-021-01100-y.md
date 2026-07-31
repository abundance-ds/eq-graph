---
project_id: "20180130"
work_id: "doi:10.1007/s40273-021-01100-y"
doi: "10.1007/s40273-021-01100-y"
pmid: "34786590"
pmcid: "PMC8595057"
title: "The EQ-5D-5L Valuation Study in Egypt"
journal: "Pharmacoeconomics"
publication_date: "2021-11-17"
volume: "40"
issue: "4"
authors:
  - name: "Sahar Al Shabasy"
    affiliation_ids:
      - "Aff1"
  - name: "Maggie Abbassi"
    affiliation_ids:
      - "Aff1"
  - name: "Aureliano Finch"
    affiliation_ids:
      - "Aff2"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff2"
  - name: "Darrin Baines"
    affiliation_ids:
      - "Aff3"
  - name: "Samar Farid"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Department of Clinical Pharmacy, Faculty of Pharmacy, Cairo University, Kasr El-Aini St., Cairo, 11562 Egypt"
  - id: "Aff2"
    name: "EuroQol Group Office, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "Initiate Consultancy, London, UK"
licence: "cc-by-nc"
source_file: "input/projects/20180130/papers/doi_10.1007_s40273-021-01100-y.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8595057/fullTextXML"
source_method: "epmc_xml"
source_sha256: "73118fd045e08db3406618a11410914b5bf9be004a5eaa97f1b6c67d08222c4b"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The EQ-5D-5L Valuation Study in Egypt

## Abstract

### Introduction

No value sets exist for either the EQ-5D-3L or the EQ-5D-5L in Egypt, despite local pharmacoeconomic guidelines recommending the use of the EQ-5D to derive utility. Most published Egyptian economic evaluation studies have used utility values from other published studies and systematic reviews.

### Objective

Our objective was to develop an Egyptian EQ-5D-5L value set using the international EuroQol standardized protocol (EQ-VT-2.1). This study is a revision of a previous EQ-5D-5L value set for Egypt retracted by the authors.

### Methods

Adult Egyptian participants were recruited from public places using multi-stratified quota sampling based on age, sex, and geographical distribution. Two elicitation techniques were applied: the composite time trade-off (cTTO) and discrete-choice experiments (DCEs). Before actual data collection, interviewers’ performance was assessed in a pilot phase. Data were modelled using generalized least squares, Tobit, heteroskedastic, logit, and hybrid models, and the best fitting model was selected based on logical consistency of the parameters, significance level, prediction accuracy, and model parsimony.

### Results

A total of 1378 interviews were conducted, of which 188 were excluded because they were incomplete and did not comply with the protocol, 216 were pilot interviews, and 974 were included in the final analysis. The heteroskedastic model with constraints (model 4) based on the cTTO data was selected as the preferred model to generate the value set. Values ranged from − 0.964 for the worst health state (55555) to 1 for full health (11111) and 0.948 for 11211, with 1123 of all predicted health states (35.94%) being worse than dead. Mobility had the largest impact on health state preference values.

### Conclusion

This is the first value set for the EQ-5D-5L based on social preferences obtained from a nationally representative sample in Egypt or any Arabic-speaking country. The value set can be used as a scoring system for economic evaluation and to improve the quality of health technology assessment in the Egyptian healthcare system.

Accepted 2021 Sep 28; Issue date 2022.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| This is the first EQ-5D-5L valuation study in Egypt and the Middle East and North Africa region. |
| The Egyptian tariff can be used as a scoring system for economic evaluations, to inform decision making, and to improve the quality of health technology assessment in the Egyptian healthcare system. |
| The availability of the Egyptian tariff will encourage health economists and clinicians to include quality-of-life questionnaires in clinical trials and implement cost-utility analysis and pharmacoeconomic modelling. |

</div>

## Introduction

The EQ-5D was developed by the EuroQol Group and is the most widely used preference-based health-related quality-of-life measure \[1\]. It is used to inform resource allocation decisions in economic evaluations across the world \[2–4\]. In addition, it is the multi-attribute utility instrument preferred by most published pharmacoeconomic guidelines \[5\] and has been reported as valid and responsive in multiple disease areas and conditions and multiple cultural contexts \[6, 7\]. The EQ-5D consists of five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. There are several versions: the three-level EQ-5D (EQ-5D-3L) defining 243 health states, the five-level EQ-5D (EQ-5D-5L) defining 3125 health states, and the youth version (EQ-5D-Y) used for pediatric populations \[8, 9\]. The EQ-5D-5L has advantages over the EQ-5D-3L in that it has more discriminatory power and a more even distribution with improved informativity and reduced ceiling effect \[10–13\].

Egypt is the most populous country in the Middle East and exerts significant cultural influence on the region \[14\]. In Egypt, there is a growing awareness of the importance of pharmacoeconomics. There is a great need to conduct high-quality economic evaluations to support and inform pricing and reimbursement decisions and to develop preference-based measures in different disease states. In Egypt, no value sets exist for either the EQ-5D-3L or the EQ-5D-5L; however, local pharmacoeconomic guidelines recommend the use of the EQ-5D as one of the preferred methods to derive utility \[15\]. Most published Egyptian economic evaluation studies depend on utility values from other published studies and systematic reviews without a reference value set for Egypt \[16–21\].

The aim of this study was to develop the EQ-5D-5L value set for Egypt by eliciting general public preferences, which will allow the assessment of healthcare interventions using cost-utility analysis and cross-country comparison of health technology assessment (HTA) evidence. This study is a revision of a previously published EQ-5D-5L valuation study for Egypt that was retracted by the authors because of an inconsistency in the preferred model \[22, 23\]. The models were revised to avoid any inconsistencies.

## Methods

### Study Design

This study was a computer-based, cross-sectional, interviewer-administered face-to-face survey of a representative Egyptian population following the EQ-VT developed for the valuation of the EuroQoL family of instruments \[24\]. This study was approved by the Research Ethics Committee at the Faculty of Pharmacy, Cairo University. Written informed consent was obtained from all participants. For reporting the key elements of the Egyptian valuation study, we followed the CREATE checklist for multi-attribute utility instruments \[25\].

### The EQ-5D-5L Descriptive System

The EQ-5D-5L describes health in terms of five dimensions. Each dimension is described in terms of five levels of severity: no, mild, moderate, severe, and unable/extreme \[2, 4\]. The combination of the five dimensions and their levels results in a health state. Each health state can be described by a five-digit number that ranges from 11111 (no problems in any of the five dimensions) to 55555 (extreme problems or unable to in all dimensions). The level of sum scores or the “misery score” is a proxy for severity and is calculated by summing the five digits for the given health state \[2\].

### Preferences-Elicitation Techniques

The EQ-VT design elicits preferences using the composite time trade-off (cTTO) and discrete-choice experiments (DCEs). The cTTO consists of the conventional TTO for health states better than dead and the lead time TTO for states considered worse than dead (WTD). The cTTO design consists of a set of 86 health states assigned to ten blocks. As for the DCE tasks, the participants are asked to choose between two impaired health states. It includes 196 pairs of EQ-5D-5L health states divided into 28 blocks of seven pairs. Detailed descriptions of the valuation protocol and the two elicitation techniques have been previously published \[24, 26–28\].

### Sampling Method and Study Population

Egypt is divided into seven regional units containing 27 governorates \[29\]. For the best geographical, social, and cultural representation, adult Egyptian participants were recruited from different Egyptian governorates representing all geographical areas as per the population distribution. Participants were recruited through personal contact and from public places such as university campuses, governmental authorities, sporting clubs, and shops using multi-stratified quota sampling based on Egyptian official statistics updated in March 2019 \[30\]. Adult participants who provided informed consent and were able to understand the valuation tasks were included in the study. The interviews took place at the interviewer’s office, or the participant’s workplace or home, or other public places according to participants’ preferences. The participants did not receive any incentives.

The interviewer team included 12 interviewers (11 females and 1 male). All interviewers were teaching assistants in the Clinical Pharmacy Department, Faculty of Pharmacy, Cairo University, who received intensive training using the training material received from EuroQol. Egypt employs no sex segregation in education, work, or social interactions, so sex matching of interviewers and participants was not necessary.

### Pilot Phase

A well-defined pilot phase (*n* = 216 interviews) took place from July to October 2019. The main objective of the pilot phase was to test the feasibility and cultural appropriateness of the EQ-VT protocol and to describe which specific elements of the protocol might need adaptation. Other objectives were to standardize interviewers’ performance to reduce variability within and across interviewers, promote quality, and improve data distribution while avoiding clustering at specific values. Some adaptations were applied to the standard valuation protocol where the initial practice health state “wheelchair example” was changed to “migraine example” as most of the participants stated that being in a wheelchair would be worse than being dead. The wheelchair example was originally designed to elicit a “better than dead” response, so this change had the positive effect of ensuring consistency with other valuation studies, where the structure of the familiarization session remained unchanged with the application of the same quality control (QC) criteria. In addition, to facilitate illiterate participants’ comprehension of the tasks, we used visual aids that were tested in the pilot phase. Graphics were used to represent the five dimensions, and colored cards (green, yellow, orange, red, and dark crimson) were used to represent levels 1–5, respectively. These colors were adapted from the traffic light system familiar to participants. Interviewers were instructed to read aloud the health states twice to illiterate participants while placing the colored cards corresponding to the level of severity in front of the graphics to express the health states as they appeared on the screen. All methodological changes undertaken to accommodate cultural and social considerations will be presented in a subsequent publication.

### Interview Process

The valuation tasks were carried out using the standardized Egyptian Arabic version of the EQ-VT software (2.1), where participants were given the study objectives with the clarification that valuation tasks were not intended to cause any conflict with their spiritual or religious beliefs \[24\]. Participants then reported and rated their own health using the EQ-5D-5L descriptive system and visual analogue scale (VAS). Five practice cTTO tasks were then completed, followed by the valuation of ten cTTO hypothetical EQ-5D-5L health states. Afterwards, a feedback module was completed in which the ten health states were arranged on the screen, with the highest value at the top and the lowest value at the bottom, according to the participant’s choices \[31\]. Participants could flag any health state that was out of order (flagged health states were excluded from the final data analysis). Next, seven forced paired comparison DCE tasks were presented in random order. Finally, participants completed a validated country-specific questionnaire pertaining to participants’ demographics and views about health, life, and death.

For all the valuation tasks, participants were instructed to read the description of each health state aloud to ensure their engagement.

### Quality Control

The EuroQol Group developed a QC tool \[32\] to improve protocol compliance. This QC tool flagged interviews that were completed in less than 3 minutes for the wheelchair example or less than 5 minutes for the ten TTO tasks, interviews where the interviewer did not explain the WTD element of the task, or interviews with clear inconsistencies. The QC tool also identified the presence of interviewers’ effects by comparing the distribution of cTTO data across interviewers for any skewed distributions or spikes at − 1, − 0.5, 0, 0.5, or 1. It also detected any unusual patterns in DCE responses, such as respondents selecting only A or only B in all seven choice tasks, or respondents alternating A and B, respectively. QC meetings were held between the Egyptian team and the EQ-VT support team—weekly in the pilot phase and biweekly during actual data collection—to discuss the QC reports. Interviewers were dropped or retrained based on their performance according to the QC reports.

### Data Analysis and Model Selection

We used SPSS software version 22 to calculate the percentages of the sample demographics, self-reported health, and descriptive statistics of the cTTO and DCE responses. Statistical modelling was conducted using STATA software version 14 to estimate the EQ-5D-5L values for all health states. Several models were tested, including generalized least square (GLS), Tobit, heteroskedastic, conditional logit, and hybrid models. The 20-parameter model is a main effect model consisting of 20 dummies, one for each dimension level from mobility level 2 to anxiety/depression level 5 (MO2-AD5) using level 1 as the reference. For the cTTO data, random effects (GLS) models (model 1 and 2) were tested to account for the panel structure of the data and heterogeneity of the participants’ views in valuing EQ-5D-5L health states. Tobit models (model 2 and 3) were used to account for the censored nature of cTTO data because participants could hypothetically continue trading below the left lower bound at − 1 for the WTD health states. The heteroskedastic models (model 3 and 4) were investigated to deal with the heteroskedasticity of the error term as the observed variance of the cTTO values increased with increasing severity of the health state. The heteroskedastic model used is a generalization of the Tobit model, which uses the interval regression (intreg) command of STATA. The intreg command models the error term as a function of the dummies MO2-AD5, accounting for multiplicative heteroskedasticity. This means that the error term is modelled in the same way over all participants. The final model would be subjected to monotonicity constraints, if needed. In all models, the dependent variable of the cTTO data was the disutility defined as 1 minus the cTTO observed value for a given health state.

The DCE data were analysed using the conditional logit model (model 5) where a binary outcome was used (0/1), 0 for dead and 1 for full health, representing the choice of the participant for each pair of the DCE tasks. To compare the modelling results of the cTTO and DCE data, the coefficients of the DCE model were rescaled using the rescaling parameter of the TTO model estimations \[33, 34\]. The cTTO and DCE data were combined in a hybrid model by multiplying the likelihood function of the cTTO model by the likelihood function of the DCE model \[33, 34\]. Four hybrid models were tested (models 6–9) by allowing heteroskedasticity and/or censoring at − 1 for the cTTO data and conditional logit model for the DCE data.

### Evaluation of the Model Performance

The model performance was evaluated using prediction accuracy (where root mean square error \[RMSE\] and mean absolute error \[MAE\] were calculated), logical consistency of the parameter estimates, the significance level of the parameters (*P* \< 0.05), the model parsimony, the value range between observed and predicted values, and goodness of fit using the Akaike information criterion (AIC) and Bayesian information criterion (BIC) \[33, 35\]. Other factors were considered in model selection, such as accounting for the censored nature of the data, heteroskedasticity of the error term, and heterogeneity of the participants’ views. Finally, a sensitivity analysis was performed to evaluate the robustness of the tested models by re-inclusion of the participants’ flagged health states.

## Results

### Data Cleaning

A total of 1378 interviews were conducted from July 2019 to March 2020. Of these, 75 interviews were incomplete, 113 were dropped—along with the three interviewers who conducted them—because of poor protocol compliance, and 216 interviews were pilot, which resulted in 974 interviews being included in the final analysis. We planned to have 1000 final interviews, but sampling was interrupted by the global coronavirus disease 2019 (COVID-19) pandemic. We had good-quality data because QC criteria were strictly followed and the pilot phase was extensive, so 974 interviews were deemed adequate.

### Participants’ Characteristics

Table <a href="#Tab1" data-ref-type="table">1</a> shows the characteristics of the study sample in comparison with the Egyptian general population \[30, 36\]. The average age was 36.9 years, and 52.4% of the participants were male. Overall, the sample was representative of the Egyptian adult general population with respect to age, sex, and geographical distribution. However, compared with national statistics, illiterate participants, elderly participants (≥ 65 years), and residents of rural areas were underrepresented in our sample, whereas those aged 35–54 years were overrepresented.

<div id="Tab1" class="table-wrap">

<div class="caption">

Background characteristics of the Egyptian participants

</div>

| Characteristics | Full sample (*n* = 1303) | Actual sample (*n* = 974) | General population<sup>a</sup> | *P* value |
|----|----|----|----|----|
| Sex |  |  |  |  |
|  Male | 672 (51.6) | 510 (52.4) | 51.6 | 0.617 |
|  Female | 631 (48.4) | 464 (47.6) | 48.4 | 0.617 |
| Age (years) | 35.8 ± 12.8 (18–75) | 36.9 ± 12.7 (18–72) | – | – |
|  18–24 | 317 (24.3) | 213 (21.9) | 18.8 | 0.013\* |
|  25–34 | 363 (27.9) | 237 (24.3) | 27.9 | 0.042\* |
|  35–44 | 279 (21.4) | 236 (24.2) | 20.9 | 0.003\* |
|  45–54 | 212 (16.3) | 184 (18.9) | 15.1 | \< 0.001\* |
|  55–64 | 110 (8.4) | 90 (9.2) | 10.6 | 0.156 |
|  ≥65 | 22 (1.7) | 14 (1.4) | 6.6 | \< 0.001\* |
| Geographical region<sup>b</sup> |  |  |  |  |
|  Greater Cairo | 511 (39.3) | 256 (26.3) | 25.1 | 0.390 |
|  Alexandria | 123 (9.5) | 119 (12.2) | 12.4 | 0.849 |
|  Delta | 229 (17.6) | 202 (20.8) | 21.7 | 0.497 |
|  Suez Canal | 123 (9.5) | 114 (11.7) | 11.2 | 0.624 |
|  North upper Egypt | 144 (11.1) | 122 (12.6) | 12.9 | 0.779 |
|  Asyut | 45 (3.5) | 44 (4.5) | 4.9 | 0.561 |
|  South upper Egypt | 126 (9.7) | 115 (11.8) | 11.8 | 1 |
| Residence<sup>b</sup> |  |  |  |  |
|  Urban | 934 (71.8) | 658 (67.7) | 42.2 | \< 0.001\* |
|  Rural | 367 (28.2) | 314 (32.3) | 57.8 | \< 0.001\* |
| Education level<sup>b</sup> |  |  |  |  |
|  Illiterate | 116 (8.9) | 109 (11.2) | 25.8 | \< 0.001\* |
|  Below intermediate<sup>c</sup> | 311 (23.9) | 290 (29.8) | 29.0 | 0.833 |
|  Intermediate<sup>d</sup> | 511 (39.3) | 398 (40.9) | 29.1 | \< 0.001\* |
|  University degree and above | 363 (27.9) | 175 (18) | 15.5 | \< 0.001\* |
| Employment status<sup>b</sup> |  |  |  |  |
|  Employed | 950 (73) | 728 (74.9) | 74.4 | 0.721 |
|  Unemployed/retired/students/other | 351 (27) | 244 (25.1) | 25.6 | 0.721 |
| Marital status<sup>b</sup> |  |  |  |  |
|  Married | 740 (56.8) | 602 (61.9) | 68 | \< 0.001\* |
|  Single/divorced/widowed | 561 (43.2) | 370 (38.1) | 32 | \< 0.001\* |
| Religious beliefs<sup>b</sup> |  |  |  |  |
|  Muslim | 1241 (95.4) | 931 (95.8) | 94.9 <sup>e</sup> | 0.202 |
|  Christian | 60 (4.6) | 41 (4.2) | 5.1 | 0.202 |
| Presence of chronic health condition<sup>b</sup> | 414 (31.8) | 285 (29.3) | – | – |
| Health insurance<sup>b</sup> |  |  |  |  |
|  Covered (full or partial) | 786 (60.4) | 579 (59.6) | 54.7 | 0.0021\* |
|  No coverage | 515 (39.6) | 393 (40.4) | 45.3 | 0.0019\* |
| VAS-5L scores | 77.5 ± 16.2 | 76.9 ± 16.7 |  |  |
| Mobility |  |  |  |  |
|  No problems | 893(68.5) | 664 (68.2) |  |  |
|  Slight problems | 234 (18) | 169 (17.4) |  |  |
|  Moderate problems | 136 (10.4) | 107 (11) |  |  |
|  Severe problems | 39 (3) | 34 (3.5) |  |  |
|  Unable to walk | 1 (0.1) | 0 (0) |  |  |
| Self-care |  |  |  |  |
|  No problems | 1226 (94.1) | 912 (93.6) |  |  |
|  Slight problems | 52 (4) | 40 (4.1) |  |  |
|  Moderate problems | 17 (1.3) | 15 (1.5) |  |  |
|  Severe problems | 8 (0.6) | 7 (0.7) |  |  |
|  Unable to dress and wash | 0(0) | 0 (0) |  |  |
| Usual activities |  |  |  |  |
|  No problems | 891 (68.4) | 667 (68.5) |  |  |
|  Slight problems | 252 (19.3) | 183 (18.8) |  |  |
|  Moderate problems | 132 (10.1) | 100 (10.3) |  |  |
|  Severe problems | 24 (1.8) | 21 (2.2) |  |  |
|  Unable to do usual activities | 4 (0.3) | 3 (0.3) |  |  |
| Pain/discomfort |  |  |  |  |
|  No problems | 510 (39.1) | 386 (39.6) |  |  |
|  Slight problems | 436 (33.5) | 302 (31) |  |  |
|  Moderate problems | 284 (21.8) | 219 (22.5) |  |  |
|  Severe problems | 52 (4) | 48 (4.9) |  |  |
|  Extreme pain or discomfort | 21 (1.6) | 19 (2) |  |  |
| Anxiety/depression |  |  |  |  |
|  No problems | 420 (32.2) | 348 (35.7) |  |  |
|  Slight problems | 410 (31.5) | 287 (29.5) |  |  |
|  Moderate problems | 343 (26.3) | 232 (23.8) |  |  |
|  Severe problems | 76 (5.8) | 61 (6.3) |  |  |
|  Extreme anxiety or depression | 54 (4.1) | 46 (4.7) |  |  |

Data are presented as *n* (%), mean ± standard deviation (range), or % unless otherwise indicated

*VAS* visual analogue scale

\**P* \< 0.05 (based on 1-sample *z*-test for a population proportion)

<sup>a</sup>Data estimated from the Egyptian Central Agency for Public Mobilization and Statistics, March 2019 \[11\]

<sup>b</sup>Sample size was *n* = 1301 for the full sample and *n* = 972 for the actual sample

<sup>c</sup>Below intermediate: below high school level

<sup>d</sup>Intermediate: high school level or 2 years institute

<sup>e</sup>Data obtained from Mohamoud et al. \[30\]

</div>

### Self-Reported Health Using the EQ-5D-5L Descriptive System

In the actual sample, 15.2% of the participants were in full health (11111). The most common health problem reported by Egyptian participants was anxiety and depression (64.3%), and the least common health problem was self-care (6.3%). The mean ± standard deviation VAS score was 76.9 ± 16.7 (Table <a href="#Tab1" data-ref-type="table">1</a>).

### Composite Time Trade-Off and Discrete-Choice Experiment Data

The 974 interviews provided 9740 cTTO responses and 6818 DCE responses. The mean interview time was 41 ± 16 min. The mean iterative steps to reach the point of indifference was 7.2 ± 3.2. The mean time spent in the feedback module was 2.8 ± 10.4 min. The participants flagged 898 cTTO responses using the feedback module. A total of 254 (26%) participants had at least one inconsistency (incorrectly ranked), which reduced to 122 (12.5%) after using the feedback module. The number of inconsistencies related to severity “6” (mild issue in one dimension only) and 55555 states was 11 (1%) and 31 (3%), respectively, and reduced to 6 (0.6%) and 3 (0.3%), respectively, after using the feedback module.

The main analysis included all the unflagged cTTO valuations (8842 responses); 40.9 % of these were considered WTD, and the mean observed value was negative for 36 of the 86 health states included in the cTTO design. The percentages of values clustered at − 1, − 0.5, 0, 0.5, and 1 were 13.3%, 4%, 1.5%, 5.2%, and 12.3%, respectively (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). As the level sum score increased for the EQ-5D-5L health states, lower mean TTO values and a larger standard deviation were observed (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). The mean observed cTTO value of the 86 health states was 0.12 ± 0.73, which ranged from 0.96 ± 0.08 for health state 11211 to − 0.83 ± 0.3 for health state 55555.

<figure id="Fig1">
<p><img src="40273_2021_1100_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40273_2021_1100_Fig1_HTML.gif" /></p>
<figcaption>Observed composite time trade-off (cTTO) value distribution</figcaption>
</figure>

<figure id="Fig2">
<p><img src="40273_2021_1100_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2021_1100_Fig2_HTML.gif" /></p>
<figcaption>Mean observed composite time trade-off (cTTO) values by level of sum scores. <em>SD</em> standard deviation</figcaption>
</figure>

For the DCE tasks, the participants were likely to choose the health states with the lower misery score as the difference in severity increased between the two health states. In total, 23 participants (2.4%) answered using the following specific pattern (AAAAAAA, BBBBBBB, ABABABA, BABABAB). However, their mean time to complete the DCE tasks was acceptable, so we decided not to exclude these interviews from the analysis.

### Modelling Results

Modelling results are shown for the cTTO, DCE, and hybrid models in Tables <a href="#Tab2" data-ref-type="table">2</a>, <a href="#Tab3" data-ref-type="table">3</a>, and <a href="#Tab4" data-ref-type="table">4</a>, respectively. All the tested models were logically consistent except for some minor inconsistencies appearing in the conditional logit models for DCE data in the self-care and usual activities dimensions level 3 (SC3 and UA3) (Table <a href="#Tab3" data-ref-type="table">3</a>). Furthermore, all model parameter estimates were statistically significant except self-care dimension level 2 (SC2) for the Tobit (models 2) (Table <a href="#Tab2" data-ref-type="table">2</a>) and anxiety/depression dimension level 2 (AD2) in the conditional logit model (model 5). Dimension ranking for the cTTO models in terms of relative importance were as follows. For models 1, 2, and 3, mobility was the most important dimension followed by anxiety/depression, pain/discomfort, self-care, and usual activities (least important). For the heteroskedastic model with constraints (model 4), pain/discomfort was more important than anxiety/depression (0.434 vs. 0.413, respectively). Disutility values of the DCE model (model 5) were calculated by dividing the coefficients of the DCE model by the rescaling factor (factor = 3.884). Mobility had the largest impact on health state preference values for all the tested models.

<div id="Tab2" class="table-wrap">

<div class="caption">

Parameter estimates for composite time trade-off models

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Dimension/level</th>
<th colspan="3" style="text-align: left;">Model 1</th>
<th colspan="3" style="text-align: left;">Model 2</th>
<th colspan="3" style="text-align: left;">Model 3</th>
<th colspan="3" style="text-align: left;">Model 4</th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">GLS (random-effect model)</th>
<th colspan="3" style="text-align: left;">GLS Tobit (random effect, censored at − 1)</th>
<th colspan="3" style="text-align: left;">Heteroskedastic Tobit (censored at − 1 with correction for heteroskedasticity)</th>
<th colspan="3" style="text-align: left;">Heteroskedastic model (constrained, heteroskedasticity of the error term, constant suppressed) (value set)</th>
</tr>
<tr>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO2</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.068</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.033</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO3</td>
<td style="text-align: left;">0.202</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.171</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.107</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.208</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO4</td>
<td style="text-align: left;">0.409</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.386</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.334</td>
<td style="text-align: left;">0.022</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.401</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO5</td>
<td style="text-align: left;">0.618</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.659</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.699</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.604</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC2</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.034</td>
<td style="text-align: left;">0.029</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;"><strong>0.074</strong></td>
<td style="text-align: left;">0.026</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.053</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC3</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.105</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC4</td>
<td style="text-align: left;">0.243</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.241</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.236</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.248</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC5</td>
<td style="text-align: left;">0.253</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.316</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.429</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.283</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA2</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">0.04</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.025</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.025</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA3</td>
<td style="text-align: left;">0.075</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.072</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA4</td>
<td style="text-align: left;">0.221</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA5</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.299</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.371</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD2</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.033</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.026</td>
<td style="text-align: left;">0.028</td>
<td style="text-align: left;">0.010</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.054</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD3</td>
<td style="text-align: left;">0.076</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.062</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD4</td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.261</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.274</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD5</td>
<td style="text-align: left;">0.363</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.499</td>
<td style="text-align: left;">0.022</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.434</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD2</td>
<td style="text-align: left;">0.048</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">0.041</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.038</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.054</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD3</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.181</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD4</td>
<td style="text-align: left;">0.298</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.296</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.323</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.331</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD5</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.444</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.527</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.413</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;">0.037</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.037</td>
<td style="text-align: left;">0.037</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.064</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.122</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Dimension ranking</td>
<td colspan="3" style="text-align: left;">MO-AD-PD-SC-UA</td>
<td colspan="3" style="text-align: left;">MO-AD-PD-SC-UA</td>
<td colspan="3" style="text-align: left;">MO-AD-PD-SC-UA</td>
<td colspan="3" style="text-align: left;">MO-PD-AD-SC-UA</td>
</tr>
<tr>
<td style="text-align: left;">Insignificant</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">1</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Illogically ordered</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td colspan="3" style="text-align: left;">10282.88</td>
<td colspan="3" style="text-align: left;">12203.67</td>
<td colspan="3" style="text-align: left;">12419.71</td>
<td colspan="3" style="text-align: left;">11206.28</td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td colspan="3" style="text-align: left;">10445.88</td>
<td colspan="3" style="text-align: left;">12366.68</td>
<td colspan="3" style="text-align: left;">12717.38</td>
<td colspan="3" style="text-align: left;">11482.69</td>
</tr>
<tr>
<td style="text-align: left;">MAE</td>
<td colspan="3" style="text-align: left;">0.3638</td>
<td colspan="3" style="text-align: left;">0.374</td>
<td colspan="3" style="text-align: left;">0.410</td>
<td colspan="3" style="text-align: left;">0.3595</td>
</tr>
<tr>
<td style="text-align: left;">RMSE</td>
<td colspan="3" style="text-align: left;">0.482</td>
<td colspan="3" style="text-align: left;">0.491</td>
<td colspan="3" style="text-align: left;">0.536</td>
<td colspan="3" style="text-align: left;">0.483</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td colspan="3" style="text-align: left;">− 0.911</td>
<td colspan="3" style="text-align: left;">− 1.167</td>
<td colspan="3" style="text-align: left;">− 1.541</td>
<td colspan="3" style="text-align: left;">− 0.964</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *AIC* Akaike information criterion, *BIC* Bayesian information criterion, *Coeff* coefficient, *GLS* generalized least square, *MAE* mean absolute error, *MO* mobility, *PD* pain/discomfort, *RMSE* root mean square error, *SC* self-care, *SE* standard error, *UA* usual activities. Bold *P* value is not significant

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

Parameter estimates for discrete-choice experiment model

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Dimension/level</th>
<th colspan="4" style="text-align: left;">Model 5</th>
</tr>
<tr>
<th colspan="4" style="text-align: left;">Conditional logit model</th>
</tr>
<tr>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">Rescaled Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO2</td>
<td style="text-align: left;">0.266</td>
<td style="text-align: center;">0.069</td>
<td style="text-align: center;">0.058</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO3</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: center;">0.093</td>
<td style="text-align: center;">0.067</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO4</td>
<td style="text-align: left;">1.13</td>
<td style="text-align: center;">0.291</td>
<td style="text-align: center;">0.072</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1–MO5</td>
<td style="text-align: left;">2.28</td>
<td style="text-align: center;">0.587</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC2</td>
<td style="text-align: left;">0.241</td>
<td style="text-align: center;">0.062</td>
<td style="text-align: center;">0.065</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC3</td>
<td style="text-align: left;">0.237</td>
<td style="text-align: center;">0.061</td>
<td style="text-align: center;">0.069</td>
<td style="text-align: center;">0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC4</td>
<td style="text-align: left;">0.783</td>
<td style="text-align: center;">0.202</td>
<td style="text-align: center;">0.071</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1–SC5</td>
<td style="text-align: left;">1.5</td>
<td style="text-align: center;">0.386</td>
<td style="text-align: center;">0.074</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA2</td>
<td style="text-align: left;">0.277</td>
<td style="text-align: center;">0.071</td>
<td style="text-align: center;">0.06</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA3</td>
<td style="text-align: left;">0.261</td>
<td style="text-align: center;">0.067</td>
<td style="text-align: center;">0.069</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA4</td>
<td style="text-align: left;">0.837</td>
<td style="text-align: center;">0.215</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1–UA5</td>
<td style="text-align: left;">1.548</td>
<td style="text-align: center;">0.399</td>
<td style="text-align: center;">0.076</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD2</td>
<td style="text-align: left;">0.18</td>
<td style="text-align: center;">0.046</td>
<td style="text-align: center;">0.064</td>
<td style="text-align: center;">0.005</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD3</td>
<td style="text-align: left;">0.273</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.069</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD4</td>
<td style="text-align: left;">0.734</td>
<td style="text-align: center;">0.189</td>
<td style="text-align: center;">0.069</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1–PD5</td>
<td style="text-align: left;">1.435</td>
<td style="text-align: center;">0.369</td>
<td style="text-align: center;">0.075</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD2</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: center;">0.065</td>
<td style="text-align: center;"><strong>0.222</strong></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD3</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: center;">0.064</td>
<td style="text-align: center;">0.067</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD4</td>
<td style="text-align: left;">0.823</td>
<td style="text-align: center;">0.212</td>
<td style="text-align: center;">0.074</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1–AD5</td>
<td style="text-align: left;">1.529</td>
<td style="text-align: center;">0.394</td>
<td style="text-align: center;">0.082</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">Dimension ranking</td>
<td colspan="4" style="text-align: left;">MO-UA-AD-SC-PD</td>
</tr>
<tr>
<td style="text-align: left;">Insignificant</td>
<td colspan="4" style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;">Illogically ordered</td>
<td colspan="4" style="text-align: left;">2</td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td colspan="4" style="text-align: left;">6776.675</td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td colspan="4" style="text-align: left;">6913.222</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td colspan="4" style="text-align: left;">− 1.135</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *AIC* Akaike information criterion, *BIC* Bayesian information criterion, *MO* mobility, *PD* pain/discomfort, *SC* self-care, *SE* standard error, *UA* usual activities. Bold *P* value is not significant

</div>

<div id="Tab4" class="table-wrap">

<div class="caption">

Parameter estimates for hybrid models

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Dimension/level</th>
<th colspan="3" style="text-align: left;">Model 6</th>
<th colspan="3" style="text-align: left;">Model 7</th>
<th colspan="3" style="text-align: left;">Model 8</th>
<th colspan="3" style="text-align: left;">Model 9</th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">Hybrid (conditional logit model)</th>
<th colspan="3" style="text-align: left;">Hybrid Tobit (censored at − 1, conditional logit model)</th>
<th colspan="3" style="text-align: left;">Hybrid heteroskedastic Tobit (censored at − 1 with heteroskedasticity, conditional logit model)</th>
<th colspan="3" style="text-align: left;">Hybrid heteroskedastic model heteroskedasticity, conditional logit model)</th>
</tr>
<tr>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1-MO2</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.055</td>
<td style="text-align: left;">0.009</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.009</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1-MO3</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.126</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1-MO4</td>
<td style="text-align: left;">0.348</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.342</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.341</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility MO1-MO5</td>
<td style="text-align: left;">0.583</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.621</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.709</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.586</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1-SC2</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.06</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.062</td>
<td style="text-align: left;">0.009</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1-SC3</td>
<td style="text-align: left;">0.09</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.081</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.082</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1-SC4</td>
<td style="text-align: left;">0.245</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.238</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.242</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.242</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility SC1-SC5</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.456</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.349</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1-UA2</td>
<td style="text-align: left;">0.082</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.076</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.009</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1-UA3</td>
<td style="text-align: left;">0.095</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.073</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1-UA4</td>
<td style="text-align: left;">0.236</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.247</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.239</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility UA1-UA5</td>
<td style="text-align: left;">0.342</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.395</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.442</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.337</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1-PD2</td>
<td style="text-align: left;">0.059</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.054</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1-PD3</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.077</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.103</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1-PD4</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.263</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.239</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility PD1-PD5</td>
<td style="text-align: left;">0.341</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.396</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.475</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1-AD2</td>
<td style="text-align: left;">0.06</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.059</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.042</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.055</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1-AD3</td>
<td style="text-align: left;">0.137</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.125</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.114</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.133</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1-AD4</td>
<td style="text-align: left;">0.267</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.282</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.293</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.276</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Disutility AD1-AD5</td>
<td style="text-align: left;">0.395</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.436</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.507</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.399</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.474</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Dimension ranking</td>
<td colspan="3" style="text-align: left;">MO-AD-UA-PD-SC</td>
<td colspan="3" style="text-align: left;">MO-AD-PD-UA-SC</td>
<td colspan="3" style="text-align: left;">MO-AD-PD-SC-UA</td>
<td colspan="3" style="text-align: left;">MO-AD-PD-SC-UA</td>
</tr>
<tr>
<td style="text-align: left;">Insignificant</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Illogically ordered</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
<td colspan="3" style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td colspan="3" style="text-align: left;">19232.64</td>
<td colspan="3" style="text-align: left;">21297.46</td>
<td colspan="3" style="text-align: left;">19207.84</td>
<td colspan="3" style="text-align: left;">18103.23</td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td colspan="3" style="text-align: left;">19401.14</td>
<td colspan="3" style="text-align: left;">21465.95</td>
<td colspan="3" style="text-align: left;">19529.51</td>
<td colspan="3" style="text-align: left;">18424.9</td>
</tr>
<tr>
<td style="text-align: left;">MAE</td>
<td colspan="3" style="text-align: left;">0.362216</td>
<td colspan="3" style="text-align: left;">0.382768</td>
<td colspan="3" style="text-align: left;">0.416236</td>
<td colspan="3" style="text-align: left;">0.363773</td>
</tr>
<tr>
<td style="text-align: left;">RMSE</td>
<td colspan="3" style="text-align: left;">0.485575</td>
<td colspan="3" style="text-align: left;">0.497105</td>
<td colspan="3" style="text-align: left;">0.543049</td>
<td colspan="3" style="text-align: left;">0.486582</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td colspan="3" style="text-align: left;">− 0.999</td>
<td colspan="3" style="text-align: left;">− 1.228</td>
<td colspan="3" style="text-align: left;">− 1.589</td>
<td colspan="3" style="text-align: left;">− 1.041</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *AIC* Akaike information criterion, *BIC* Bayesian information criterion, *Coeff* coefficient, *MAE* mean absolute error, *MO* mobility, *PD* pain/discomfort, *RMSE* root mean square error, *SC* self-care, *SE* standard error, *UA* usual activities

</div>

### Preferred Model and Value Set

Both the GLS model and heteroskedastic model with constraints performed better than the other tested models in terms of prediction accuracy (MAE and RMSE), logical consistency, significance level, and goodness of fit (AIC and BIC) (Table <a href="#Tab2" data-ref-type="table">2</a>). However, the heteroskedastic model with constraints (model 4) was considered the preferred model because of its ability to handle the heteroskedasticity of the error term. In addition, it had a lower MAE than the other tested models in the observed cTTO data, in the mean observed values for the 86 health states included in the design, and in the mean observed values for the mildest health states, with level sum score \< 10, indicating better accuracy (the fit statistics are shown in the electronic supplementary material). The constant term in the model was not significant and was suppressed (Fig. <a href="#Fig3" data-ref-type="fig">3</a>).

<figure id="Fig3">
<p><img src="40273_2021_1100_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="40273_2021_1100_Fig3_HTML.gif" /></p>
<figcaption>Scatterplots of the predicted values of the heteroskedastic model with constraints versus the mean observed values of composite time trade-off (cTTO) of each health state</figcaption>
</figure>

The predicted cTTO values ranged from − 0.964 for the worst health state (55555) to 0.948 for 11211. About 1123 (35.94%) of the health states were WTD. Dimension ranking in terms of relative importance was mobility (most important), pain/discomfort, anxiety/depression, self-care, and usual activities (least important). For any given health state, the utility value can be calculated by subtracting the regular dummies (parameter estimates) for each dimension level of the health state from 1.

### Sensitivity Analysis

The model performance worsened after inclusion of the flagged health states in the feedback module, so we decided to exclude the flagged health states from the analysis. No other exclusions were applied to the data as only three inconsistencies related to 55555 and only one participant gave the same value for all health states.

## Discussion

To the best of our knowledge, this is the first EQ-5D-5L valuation study in Egypt and in the Middle East and North Africa (MENA) region. A consistent tariff was generated with statistically significant decrements for all dimensions for use as a scoring system for economic evaluation to inform decision making and improve the quality of HTA in the Egyptian healthcare system.

The successful application of the EQ-VT valuation protocol on the Egyptian population verified the feasibility and cultural appropriateness of using such valuation techniques in Muslim and Arabic-speaking countries. Furthermore, the extensive pilot phase and the periodic QC meetings allowed the Egyptian study team and the EQ-VT support team to enhance the interviewers’ performance and promote compliance with the valuation tasks.

The heteroskedastic model with constraints (model 4) based on the cTTO data was selected as the preferred model for the Egyptian tariff as the cTTO data were of good quality. The parameter estimates of the heteroskedastic constrained model were statistically significant and monotonic and accounted for the heteroskedasticity feature of the data. Two inconsistencies appeared in the DCE conditional logit model. Furthermore, in the tested models, there was a large difference in terms of size of coefficients for the five dimensions at different levels for the DCE and TTO data as both techniques have different underlying assumptions. cTTO data are time-dependent data influenced by scale compatibility and loss aversion \[24, 37\], whereas the DCE is a choice-based task characterized by attribute non-attendance and lexicographic preferences \[38, 39\]. Although methods have been developed to correct for attribute non-attendance \[40\], there exists no software packages that would allow us to use these in combination with hybrid modelling, making it impossible to anchor the attribute-non-attendance adjusted values onto the quality-adjusted life-year scale using the hybrid modelling technique. Other countries such as the USA \[41\], the Netherlands \[42\], China \[43\], Uruguay \[44\], Korea \[45\], and Hungary \[46\] also used only cTTO data to generate their national value sets.

All EQ-5D-5L valuation studies followed the same standardized international protocol (EQ-VT) so the results can be easily compared across countries. In Egypt, mobility had the largest impact on health state preference values. This may be due to the limited access to social welfare for immobility in this country. Furthermore, Egypt lacks the infrastructure that enables people with mobility problems to live normally and independently in society. Mobility was also the most important dimension in all Asian countries \[31, 43, 45, 47–52\], Hungary \[46\], Uruguay \[44\], and Canada \[53\].

In this study, the predicted cTTO values ranged from − 0.964 for the worst health state (55555) to 0.948 for 11211. The worst health state had a higher value than in Taiwan (− 1.0259) \[49\] and Ireland (− 0.974) \[54\] but was lower than in all other published valuation studies \[31, 41–48, 50–53, 55–60\].

Egypt had the largest percentage (40.9%) of the cTTO observations considered to be WTD compared with other countries such as Taiwan (38.5%) \[49\], Indonesia (35.39%) \[47\], and Japan (7.5%) \[52\]. This may be attributed to cultural and social factors as most participants in Egypt preferred to die than to be a burden on family and friends as a result of severe illness, as stated in the country-specific questionnaire (details will be published subsequently). This is in line with findings published in the Indonesian EQ-5D-5L valuation study \[47\].

There were 1172 (13.3%) observations at − 1, where the participants traded all 20 years of life to avoid living in certain health states in the cTTO task; this percentage was higher than in Ethiopia (8.04%) \[55\] and lower than in the USA (14.7%) \[41\] and Hong Kong (16%) \[31\]. Furthermore, 12.3 and 1.5% of the observations were clustered at 1 and 0, respectively, compared with 20.5 and 5.1%, respectively, in the USA \[41\]. Clustering at these critical points might be due to interviewer’s effect, task shortcutting, and social and cultural factors. In this study, the QC tool was used rigorously, and the pilot phase was extensive to reduce the variability among and within interviewers, standardize their performance, and improve data quality.

There were some limitations in terms of differences in the distribution of background variables in the actual sample compared with the data provided by the Egyptian Central Agency for Public Mobilization and Statistics \[30\]. Rural and illiterate participants were underrepresented in our sample as it was difficult for interviewers to reach some rural areas, but extreme effort was made to represent people living in those areas as much as possible; however, the sample accurately represented the geographical distribution in Egypt. The EQ-VT protocol was designed for literate and educated participants. Tunisia recently published an EQ-5D-3L valuation study that only included literate individuals, despite illiterate people representing 18.8% of the general Tunisian population \[61\]. However, our study team decided not to exclude illiterate participants from the Egyptian study to ensure they had a voice in the produced tariff. The team exerted all possible efforts to interview illiterate participants with the use of some visual aids, without fulfilling the exact quota for illiterate participants (25.8%) because the tool used was not fully validated.

Other demographic characteristics are shown in Table <a href="#Tab1" data-ref-type="table">1</a>. Some characteristics did not significantly deviate from the population, such as religion and employment status, whereas marital status and health insurance coverage differed significantly from the population distribution. Despite the deviations from the exact population distribution, the demographic characteristics still had the required diversity. Furthermore, the estimated quota was not fully fulfilled because the COVID-19 pandemic led to sudden interruption of data collection. These deviations in the sample characteristics in terms of residence and/or education are in line with other valuation studies. Further research is needed to assess the feasibility and impact of weighting of underrepresented characteristics on the produced value sets. A publication exploring the effect of cultural and demographic differences on health valuation in Egypt is underway.

Finally, the availability of the Egyptian tariff will encourage health economists and clinicians to include quality-of-life questionnaires in clinical trials and implement cost-utility analysis and pharmacoeconomic modelling to assist decision makers in appropriate allocation of healthcare resources.

Since cultural and socioeconomic factors play a role in shaping people’s preferences, the high quality of the data used in the Egyptian value set may allow its use in economic evaluations for MENA countries that share common cultural and socioeconomic backgrounds but for which a country-specific value set is not yet available, rather than using tariffs from outside the region \[62\]. It must be noted that recommendations are for each country to develop its own value set to represent the views and preferences of its own population \[63\].

## Conclusion

This is the first value set for EQ-5D-5L based on social preferences obtained from a nationally representative sample in Egypt. The value set will play a key role in economic evaluations and HTAs in Egypt. In addition, other countries in the MENA region may be encouraged to follow suit and develop their own value sets.

## Acknowledgements

The authors thank the EuroQol support team—Elly Stolk, Fatima Al Sayah, and Arnd Jan Prause—for their guidance and support during study preparation, data collection, and QC. We are grateful for the outstanding effort of the interviewers: Eglal A. Bassiouny, Hend K. Eldeib, Sandra N. Naguib, Israa K. Mohamed, Sara AlSherif, Shaza G. Ali, Salma M. Abdelmageed, and Nour A. Sharaf. Finally, we thank the study participants for taking part in this study.

## Declarations

### Funding

This project received financial support from Bournemouth University, UK and the EuroQol Foundation, the Netherlands (project ID: 20180130). The funding agreement ensured the authors’ independence in designing the study and writing and publishing the results.

### Conflict of interest

Aureliano Finch and Bram Roudijk are members of the EuroQol Research Foundation (the copyright holder of the EQ-5D-5L). Sahar Al Shabasy, Maggie Abbassi, Darrin Baines, and Samar Farid have no conflicts of interest directly relevant to the content of this article.

### Ethics approval

The study received ethical approval from the Ethics Committee of the Faculty of Pharmacy Cairo University and was conducted in accordance with the Declaration of Helsinki.

### Consent to participate

Written informed consent was obtained from all participants included in the study. Participants were informed about their freedom of refusal. Anonymity and confidentiality were maintained throughout the research process.

### Consent for publication

Not applicable.

### Availability of data and material

The datasets generated and analysed during the current study are available from the corresponding author upon reasonable request.

### Code availability

Not applicable.

### Author contributions

SAS participated in the study preparation and data collection, created data QC reports, interpreted results, and prepared the draft manuscript. MA and SF participated in the study preparation, proof reading of the translated version, follow-up of the data collection, the QC process, interpreting results, and reviewing the final manuscript. AF participated in follow-up of data collection, the QC process, statistical analysis and interpretation of the study results, and review of the final manuscript. BR participated in the statistical analysis, interpretation of results and review of the final manuscript. DB participated in the study preparation, acquired the funding, and reviewed the final manuscript.

## References

## References

1. Brooks R, Group E EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi: 10.1016/0168-8510(96)00822-6.

2. Brauer CA, Rosen AB, Greenberg D, Neumann PJ. Trends in the measurement of health utilities in published cost-utility analyses. Value Health. 2006;9(4):213–218. doi: 10.1111/j.1524-4733.2006.00116.x.

3. Prosser L, Wittenberg E, editors. Trends in utility elicitation methods: is there still a role for direct elicitation? In: 32nd annual meeting of society for medical decision making, Toronto; 2010.

4. Rabin R, Charro FD. EQ-SD: a measure of health status from the EuroQol Group. Ann Med. 2001;33(5):337–343. doi: 10.3109/07853890109002087.

5. Kennedy-Martin M, Slaap B, Herdman M, van Reenen M, Kennedy-Martin T, Greiner W, et al. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020;21(8):1245–1257. doi: 10.1007/s10198-020-01195-8.

6. Qian X, Tan RL-Y, Chuang L-H, Luo N. Measurement properties of commonly used generic preference-based measures in East and South-East Asia: a systematic review. Pharmacoeconomics. 2020;38(2):159–170. doi: 10.1007/s40273-019-00854-w.

7. Finch AP, Brazier JE, Mukuria C. What is the evidence for the performance of generic preference-based measures? A systematic overview of reviews. Eur J Health Econ. 2018;19(4):557–570. doi: 10.1007/s10198-017-0902-x.

8. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L) Qual Life Res. 2011;20(10):1727–1736. doi: 10.1007/s11136-011-9903-x.

9. The EQ-5D Instruments. 2020. https://euroqol.org/eq-5d-instruments/. Accessed 2 Dec 2020.

10. Janssen M, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, et al. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi: 10.1007/s11136-012-0322-4.

11. Janssen MF, Bonsel GJ, Luo N. Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. 2018;36(6):675–697. doi: 10.1007/s40273-018-0623-8.

12. Devlin N, Brazier J, Pickard AS, Stolk E. 3L, 5L, what the L? A NICE Conundrum. Pharmacoeconomics. 2018;36(6):637–640. doi: 10.1007/s40273-018-0622-9.

13. Buchholz I, Janssen MF, Kohlmann T, Feng Y-S. A systematic review of studies comparing the measurement properties of the three-level and five-level versions of the EQ-5D. Pharmacoeconomics. 2018;36(6):645–661. doi: 10.1007/s40273-018-0642-5.

14. Kausch K. Egypt: inside-out. Geopolitics and democracy in the Middle East: FRIDE; 2015. pp. 21–34 c.

15. Elsisi GH, Kaló Z, Eldessouki R, Elmahdawy MD, Saad A, Ragab S, et al. Recommendations for reporting pharmacoeconomic evaluations in Egypt. Value Health Reg Issues. 2013;2(2):319–327. doi: 10.1016/j.vhri.2013.06.014.

16. Elsisi G, Hassouna A, Taleb AA, Elmahdawy M, Ibrahim S. Cost-effectiveness of pazopanib versus sunitinib in egyptian patients with metastatic renal cell carcinoma from the health insurance perspective: a Markov model. Value Health. 2014;17(3):A90–A91. doi: 10.1016/j.jval.2014.03.526.

17. Elsisi G, Abdallah HM, Elmansy H. Economic evaluation of lidocaine/tetracaine patch versus lidocaine/prilocaine cream for topical anaesthesia before vascular access in Egypt. Value Health. 2015;18(7):A669. doi: 10.1016/j.jval.2015.09.2443.

18. El-Hamamsy MH, Elsisi GH, Eldessouki R, Elmazar MM, Taha AS, Awad BF, et al. Economic evaluation of the combined use of warfarin and low-dose aspirin versus warfarin alone in mechanical valve prostheses. Appl Health Econ Health Policy. 2016;14(4):431–440. doi: 10.1007/s40258-016-0238-1.

19. Elsisi GH, Eldessouki R, Kalo Z, Elmazar MM, Taha AS, Awad BF, et al. Cost-effectiveness of the combined use of warfarin and low-dose aspirin versus warfarin alone in Egyptian patients with aortic valve replacements: a Markov model. Value Health Reg Issues. 2014;4C:24–30. doi: 10.1016/j.vhri.2014.06.004.

20. Hossam M, Elsisi G. Cost-effectiveness analysis of fidaxomicin versus oral vancomycin for the treatment of clostridium difficile infection in Egypt. Value Health. 2016;19(7):A513. doi: 10.1016/j.jval.2016.09.964.

21. Mostafa A, Elsisi GH. A cost-effectiveness analysis of the use of safety-engineered syringes in reducing HBV, HCV, and HIV burden in Egypt. Expert Rev Med Dev. 2019;16(2):155–163. doi: 10.1080/17434440.2019.1561267.

22. Al Shabasy SA, Abbassi MM, Finch AP, Baines D, Farid SF. RETRACTED ARTICLE: the EQ-5D-5L valuation study in Egypt. Pharmacoeconomics. 2021;39(5):549–561. doi: 10.1007/s40273-021-01002-z.

23. Al Shabasy SA, Abbassi MM, Finch AP, Baines D, Farid SF. Retraction note to: the EQ-5D-5L valuation study in Egypt. Pharmacoeconomics. 2021;39(8):971. doi: 10.1007/s40273-021-01055-0.

24. Oppe M, Devlin NJ, van Hout B, Krabbe PF, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17(4):445–453. doi: 10.1016/j.jval.2014.04.002.

25. Xie F, Pickard AS, Krabbe PF, Revicki D, Viney R, Devlin N, et al. A checklist for reporting valuation studies of multi-attribute utility-based instruments (CREATE) Pharmacoeconomics. 2015;33(8):867–877. doi: 10.1007/s40273-015-0292-9.

26. Oppe M, Van Hout B. The “power” of eliciting EQ-5D-5L values: the experimental design of the EQ-VT. EuroQol working paper series. 2017. p. 17003. http://euroqol.org/wp-content/uploads/2016/10/EuroQol-Working-Paper-Series-Manuscript-17003-Mark-Oppe.pdf. Accessed 10 May 2020.

27. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi: 10.1007/s40273-016-0404-1.

28. Devlin NJ, Tsuchiya A, Buckingham K, Tilling C. A uniform time trade off method for states better and worse than dead: feasibility study of the ‘lead time’ approach. Health Econ. 2011;20(3):348–361. doi: 10.1002/hec.1596.

29. General Organization for Physical Planning. http://gopp.gov.eg/eg-map/. Accessed 2 Apr 2018.

30. Central Agency for Public Mobilization and Statistics—CAPMAS. 2019. http://www.capmas.gov.eg/Pages/StaticPages.aspx?page_id=5035. Accessed 9 May 2019.

31. Wong EL, Ramos-Goni JM, Cheung AW, Wong AY, Rivero-Arias O. Assessing the use of a feedback module to model EQ-5D-5L health states values in Hong Kong. Patient. 2018;11(2):235–247. doi: 10.1007/s40271-017-0278-0.

32. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–473. doi: 10.1016/j.jval.2016.10.012.

33. Ramos-Goñi JM, Pinto-Prades JL, Oppe M, Cabasés JM, Serrano-Aguilar P, Rivero-Arias O. Valuation and modeling of EQ-5D-5L health states using a hybrid approach. Med Care. 2017;55(7):e51–e58. doi: 10.1097/MLR.0000000000000283.

34. Ramos-Goni JM, Craig B, Oppe M, van Hout B. Combining continuous and dichotomous responses in a hybrid model. EuroQol working paper series. 2016, p. 16002. https://euroqol.org/wp-content/uploads/working_paper_series/EuroQol_Working_Paper_Series_Manuscript_16002_-_Juan_Ramos-Goni.pdf. Accessed 30 Apr 2020.

35. Feng Y, Devlin NJ, Shah KK, Mulhern B, Hout B. New methods for modelling EQ-5D-5L value sets: an application to English data. Health Econ. 2018;27(1):23–38. doi: 10.1002/hec.3560.

36. Mohamoud YA, Cuadros DF, Abu-Raddad LJ. Characterizing the copts in Egypt: demographic, socioeconomic and health indicators. Q Sci Connect. 2013 doi: 10.5339/connect.2013.22.

37. Bleichrodt H. A new explanation for the difference between time trade-off utilities and standard gamble utilities. Health Econ. 2002;11(5):447–456. doi: 10.1002/hec.688.

38. Lancsar E, Louviere J. Deleting ‘irrational’responses from discrete choice experiments: a case of investigating or imposing preferences? Health Econ. 2006;15(8):797–811. doi: 10.1002/hec.1104.

39. Alemu MH, Mørkbak MR, Olsen SB, Jensen CL. Attending to the reasons for attribute non-attendance in choice experiments. Environ Resour Econ. 2013;54(3):333–359. doi: 10.1007/s10640-012-9597-8.

40. Doherty E, Hobbins A, Whitehurst DG, O’Neill C. An exploration on attribute non-attendance using discrete choice experiment data from the Irish EQ-5D-5L National Valuation Study. PharmacoEconomics-Open. 2021;5(2):237–244. doi: 10.1007/s41669-020-00244-5.

41. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F, et al. United States valuation of EQ-5D-5L health states using an international protocol. Value Health. 2019;22(8):931–941. doi: 10.1016/j.jval.2019.02.009.

42. Versteegh MM, Vermeulen KM, Evers SM, De Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi: 10.1016/j.jval.2016.01.003.

43. Luo N, Liu G, Li M, Guan H, Jin X, Rand-Hendriksen K. Estimating an EQ-5D-5L value set for China. Value Health. 2017;20(4):662–669. doi: 10.1016/j.jval.2016.11.016.

44. Augustovski F, Rey-Ares L, Irazola V, Garay OU, Gianneo O, Fernández G, et al. An EQ-5D-5L value set based on Uruguayan population preferences. Qual Life Res. 2016;25(2):323–333. doi: 10.1007/s11136-015-1086-4.

45. Kim S-H, Ahn J, Ock M, Shin S, Park J, Luo N, et al. The EQ-5D-5L valuation study in Korea. Qual Life Res. 2016;25(7):1845–1852. doi: 10.1007/s11136-015-1205-2.

46. Rencz F, Brodszky V, Gulácsi L, Golicki D, Ruzsa G, Pickard AS, et al. Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time trade-off in Hungary. Value Health. 2020;23(9):1235–1245. doi: 10.1016/j.jval.2020.03.019.

47. Purba FD, Hunfeld JA, Iskandarsyah A, Fitriana TS, Sadarjoen SS, Ramos-Goñi JM, et al. The Indonesian EQ-5D-5L value set. Pharmacoeconomics. 2017;35(11):1153–1165. doi: 10.1007/s40273-017-0538-9.

48. Pattanaphesaj J, Thavorncharoensap M, Ramos-Goñi JM, Tongsiri S, Ingsrisawang L, Teerawattananon Y. The EQ-5D-5L valuation study in Thailand. Expert Rev Pharmacoecon Outcomes Res. 2018;18(5):551–558. doi: 10.1080/14737167.2018.1494574.

49. Lin H-W, Li C-I, Lin F-J, Chang J-Y, Gau C-S, Luo N, et al. Valuation of the EQ-5D-5L in Taiwan. PLoS ONE. 2018;13(12):e0209344. doi: 10.1371/journal.pone.0209344.

50. Mai VQ, Sun S, Minh HV, Luo N, Giang KB, Lindholm L, et al. An EQ-5D-5L Value Set for Vietnam. Qual Life Res. 2020;29(7):1923–1933. doi: 10.1007/s11136-020-02469-7.

51. Shafie AA, Thakumar AV, Lim CJ, Luo N, Rand-Hendriksen K, Yusof FAM. EQ-5D-5L valuation for the Malaysian population. Pharmacoeconomics. 2019;37(5):715–725. doi: 10.1007/s40273-018-0758-7.

52. Shiroiwa T, Ikeda S, Noto S, Igarashi A, Fukuda T, Saito S, et al. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19(5):648–654. doi: 10.1016/j.jval.2016.03.1834.

53. Xie F, Pullenayegum E, Gaebel K, Bansback N, Bryan S, Ohinmaa A, et al. A time trade-off-derived value set of the EQ-5D-5L for Canada. Med Care. 2016;54(1):98–105. doi: 10.1097/MLR.0000000000000447.

54. Hobbins A, Barry L, Kelleher D, Shah K, Devlin N, Goni JMR, et al. Utility values for health states in Ireland: a value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(11):1345–1353. doi: 10.1007/s40273-018-0690-x.

55. Welie AG, Gebretekle GB, Stolk E, Mukuria C, Krahn MD, Enquoselassie F, et al. Valuing health state: an EQ-5D-5L value set for Ethiopians. Value Health Reg Issues. 2020;22:7–14. doi: 10.1016/j.vhri.2019.08.475.

56. Andrade LF, Ludwig K, Goni JMR, Oppe M, de Pouvourville G. A French Value Set for the EQ-5D-5L. Pharmacoeconomics. 2020;38(4):413–425. doi: 10.1007/s40273-019-00876-4.

57. Ferreira PL, Antunes P, Ferreira LN, Pereira LN, Ramos-Goñi JM. A hybrid modelling approach for eliciting health state preferences: the Portuguese EQ-5D-5L value set. Qual Life Res. 2019;28(12):3163–3175. doi: 10.1007/s11136-019-02226-5.

58. Golicki D, Jakubczyk M, Graczyk K, Niewada M. Valuation of EQ-5D-5L health states in Poland: the first EQ-VT-based study in Central and Eastern Europe. Pharmacoeconomics. 2019;37(9):1165–1176. doi: 10.1007/s40273-019-00811-7.

59. Ludwig K, von der Schulenburg J-MG, Greiner W. German value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(6):663–674. doi: 10.1007/s40273-018-0615-8.

60. Ramos-Goñi JM, Craig BM, Oppe M, Ramallo-Fariña Y, Pinto-Prades JL, Luo N, et al. Handling data quality issues to estimate the Spanish EQ-5D-5L value set using a hybrid interval regression approach. Value Health. 2018;21(5):596–604. doi: 10.1016/j.jval.2017.10.023.

61. Chemli J, Drira C, Felfel H, Roudijk B, Al Sayah F, Kouki M, et al. Valuing health-related quality of life using a hybrid approach: Tunisian value set for the EQ-5D-3L. Qual Life Res. 2021;30(5):1445–1455. doi: 10.1007/s11136-020-02730-z.

62. Bailey H, Kind P. Preliminary findings of an investigation into the relationship between national culture and EQ-5D value sets. Qual Life Res. 2010;19(8):1145–1154. doi: 10.1007/s11136-010-9678-5.

63. Roudijk B, Donders ART, Stalmeier PF. Cultural values: can they explain differences in health utilities between countries? Med Decis Making. 2019;39(5):605–616. doi: 10.1177/0272989X19841587.

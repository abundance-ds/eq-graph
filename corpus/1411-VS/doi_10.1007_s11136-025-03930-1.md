---
project_id: "1411-VS"
work_id: "doi:10.1007/s11136-025-03930-1"
doi: "10.1007/s11136-025-03930-1"
pmid: "40019677"
pmcid: "PMC12119695"
title: "Valuing health‐related quality of life: an EQ‐5D‐5L value set for Morocco"
journal: "Quality of Life Research"
publication_date: "2025-02-28"
volume: "34"
issue: "6"
authors:
  - name: "Asmaa Azizi"
    affiliation_ids:
      - "Aff1"
  - name: "Amal Boutib"
    affiliation_ids:
      - "Aff1"
  - name: "Doha Achak"
    affiliation_ids:
      - "Aff1"
  - name: "Fredrick Dermawan Purba"
    affiliation_ids:
      - "Aff2"
  - name: "Fanni Rencz"
    affiliation_ids:
      - "Aff3"
  - name: "Elmadani Saad"
    affiliation_ids:
      - "Aff1"
  - name: "Abderraouf Hilali"
    affiliation_ids:
      - "Aff1"
  - name: "Samir Ahid"
    affiliation_ids:
      - "Aff4"
      - "Aff5"
  - name: "Chakib Nejjari"
    affiliation_ids:
      - "Aff4"
      - "Aff8"
  - name: "Elly A Stolk"
    affiliation_ids:
      - "Aff6"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff6"
  - name: "Ibtissam Youlyouz-Marfak"
    affiliation_ids:
      - "Aff1"
  - name: "Abdelghafour Marfak"
    affiliation_ids:
      - "Aff4"
      - "Aff7"
affiliations:
  - id: "Aff1"
    name: "Laboratory of Health Sciences and Technologies, Higher Institute of Health Sciences, Hassan First University of Settat, 26000 Settat, Morocco"
  - id: "Aff2"
    name: "Faculty of Psychology, Universitas Padjadjaran, Jatinangor, Indonesia"
  - id: "Aff3"
    name: "Department of Health Policy, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff4"
    name: "Euromed Research Center, Euromed University of Fez (UEMF), Fez, Morocco"
  - id: "Aff5"
    name: "Pharmacoeconomics and Pharmacoepidemiology Research Team. Pharmacology and Toxicology Laboratory, Faculty of Medicine and Pharmacy, Mohammed V University of Rabat, Rabat, Morocco"
  - id: "Aff6"
    name: "EuroQol Research Foundation, Marten Meesweg 107, Rotterdam, The Netherlands"
  - id: "Aff7"
    name: "Ministry of Health and Social Protection, National School of Public Health, Rabat, Morocco"
  - id: "Aff8"
    name: "Faculty of Medicine, Pharmacy, and Dentistry, Sidi Mohamed Ben Abdellah University, Fez, Morocco"
licence: "cc-by-nc-nd"
source_file: "input/projects/1411-VS/papers/doi_10.1007_s11136-025-03930-1.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12119695/fullTextXML"
source_method: "epmc_xml"
source_sha256: "c91dba6b0e6b2afc5af21631c142d2fa0898b4309b598c6400f727b10a825eaa"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Valuing health‐related quality of life: an EQ‐5D‐5L value set for Morocco

## Abstract

### Purpose

There is a growing interest in Health Technology Assessment (HTA) in Morocco. A national EQ-5D-5L value set would allow for the computation of Quality Adjusted Life Years (QALYs) in economic evaluations of healthcare interventions to support decision-making. This study aimed to develop a Moroccan EQ-5D-5L value set based on data from a representative sample of the Moroccan adult general population.

### Methods

A Moroccan representative sample of adults was recruited using stratified quota sampling based on gender, age category, and place of residence. Data were collected between November 2022 and December 2023 using the international EuroQol valuation protocol, EQ-VT version 2.6.1. This protocol includes two elicitation techniques: the composite time trade-off (cTTO) and the discrete choice experiment (DCE). cTTO and DCE data were modeled using a heteroskedastic Tobit model and a conditional logit model, respectively. In addition, these models were combined using a hybrid model.

### Results

A total of 976 respondents were included in the final analysis. The hybrid heteroskedastic model was considered the preferred model. The predicted utility values ranged from −1.492 for the worst health state (55555) to 1 for full health (11111), where the two mildest impaired states (11211 and 21111) had a utility value of 0.979. Pain/discomfort had the largest effect on health utility values, followed by anxiety/depression, mobility, self-care and usual activities.

### Conclusion

Morocco is the third country in the Middle East and North Africa (MENA) region with an EQ-5D-5L value set. This study supports the use of EQ-5D-5L data for healthcare decision-making in the Moroccan context.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-025-03930-1.

**Keywords:** EQ-5D-5L, cTTO, DCE, Value set, EQ-VT, Utility

Accepted 2025 Feb 14; Issue date 2025.

## Introduction

Health Technology Assessment (HTA) is a crucial component of healthcare systems, essential for prioritizing interventions and allocating resources effectively \[1\]. It involves the systematic evaluation of health technologies, providing scientific, medical, and economic evidence to support informed decision-making in healthcare \[2\]. In Morocco, there is growing interest in HTA, highlighted as a significant action in the National Health Financing Strategy launched by the Ministry of Health and Social Protection \[3\]. This strategy aims to improve healthcare decision-making through scientific evidence. While HTA is still in its early stages in Morocco, the EQ-5D has been used in numerous studies to assess health outcomes and evaluate the effectiveness of healthcare interventions \[4–9\]. Additionally, several other studies are currently underway, reflecting the growing interest in HTA and health outcomes measurement in the country.

Cost-utility analysis (CUA) has been recommended as the preferred method of HTA to aid the decision-making process in several countries. In CUA, the cost-effectiveness of a healthcare technology is measured in terms of cost per quality-adjusted life-year (QALY) \[10\], where the QALY indicator is calculated by multiplying the lifetime spent in a health state by its utility value \[11\]. The QALY provides a direct comparison of different treatment options in terms of improvements in health-related quality of life (HRQoL) under various conditions. To calculate QALYs, a country-specific utility is recommended. Utility values are typically obtained using preference-based HRQoL measures, which consist of a descriptive system and a scoring algorithm (i.e. value set) that assigns a utility value to each possible combination of health problems described by the descriptive system \[12\].

Country-specific value sets are essential for obtaining accurate estimates of QALYs, as social preferences vary significantly based on demographic, cultural, and socio-economic factors \[13\]. In the Middle East and North Africa (MENA) context, where cultural characteristics and health priorities may differ from those in Western countries, it is crucial to have values specific to the local population to ensure economic evaluations are aligned with local values.

Since its development by the EuroQol Group in the late 1980s, the EQ-5D has become the most used preference-based instrument for calculating QALYs \[14\]. In addition, it is recommended in the HTA guidelines of almost 30 countries \[15, 16\], including those of the UK's National Institute for Health and Care Excellence (NICE) \[17\]. The EQ-5D has also become the most widely applied instrument for measuring HRQoL in different clinical areas and in multiple cultural contexts \[18, 19\]. The original version (EQ-5D-3L) allows respondents to differentiate between 3 levels of severity \[20\]. To improve its sensitivity, a new version, namely EQ-5D-5L was introduced by the EuroQol Group extending the number of response levels per dimension from three to five \[21\], which allows the description of 3125 health states compared with only 243 for the 3-level. The EQ-5D-5L has been translated into more than 130 languages and is widely used, demonstrating good reliability and validity in both patients and the general population \[22\]. At present, EQ-5D-5L value sets are available for more than 30 countries \[23\].

A Moroccan EQ-5D-3L value set was recently developed \[24\], marking the first of its kind in the MENA region. However, the EQ-5D-5L version has been demonstrated to offer superior descriptive and discriminative performance compared to the 3L version in numerous countries \[25\]. Despite this, Morocco currently lacks a national value set for the EQ-5D-5L. Given the need for high-quality economic evaluations to support and inform pricing and reimbursement decisions in Morocco, the development of a Moroccan EQ-5D-5L value set is a priority. Therefore, this study aims to develop a national value set for the EQ-5D-5L based on data from a representative sample of the Moroccan population using the EQ-VT standard protocol.

## Methods

### Study design, sampling, and recruitment

This cross-sectional study followed the Checklist for REporting VAluaTion StudiEs (CREATE) \[26\] to ensure the reporting of key elements of the Moroccan valuation study. Data were collected using computer-assisted face-to-face interviews between November 2022 and December 2023, using the EuroQol Group’s valuation protocol and software (EQ-VT) version 2.6.1 \[27\]. This study was approved by “the Ethics Committee for Biomedical Research from the Faculty of Medicine and Pharmacy of Rabat, Morocco (CERB O-22)”.

A Moroccan representative sample was obtained using stratified quota sampling in terms of sex, age category, and place of residence, based on the latest adult general population and housing census data in 2014 available through the Haut-Commissariat au Plan (HCP) \[28\]. In addition, participants were selected from different regions to ensure geographical representativeness. Respondents were recruited from various settings, including publicly accessible places such as shopping centers, parks, and universities, as well as places with restricted access such as residential areas and factories. Eligible participants were (i) people aged 18 years old and above, (ii) proficient in understanding and speaking either the Moroccan dialect or French, which were the languages used for the interviews, and (iii) agreed to participate in our study. Participants received gift coupons to encourage their participation.

A total of 12 interviewers, comprising 4 professors and 8 PhD students, were recruited from the Higher Institute of Health Sciences at Hassan First University of Settat. The team of interviewers consisted of seven men and five women. All interviewers underwent an intensive two-day training using standardized EuroQol training materials prior to data collection. Of these interviewers, one quit, 2 were let go due to the poor quality of the data collected, and 9 finished data collection.

### Valuation techniques

All interviews were conducted face to face using a laptop computer equipped with the Moroccan Arabic and French versions of the EQ-VT v2.6.1 online software \[27\]. Respondents were given the option to choose the language of the interview. Both language versions were adapted to the local cultural context, ensuring equivalence in content and meaning, thereby minimizing any potential impact on the results. The EQ-VT includes two valuations techniques: the composite time trade-off (cTTO) and the discrete choice experiment (DCE) \[29, 30\]. The cTTO included 86 EQ-5D-5L health states divided into ten blocks, each containing 10 health states. The order of the 10 health states within each block were randomized by the EQ-VT software. Eighty unique heath states were selected using Monte Carlo simulation (eight unique heath states included in each block), five very mild states (only one dimension at level 2 and all others at level 1, e.g., ‘11112’) (each included in two blocks) and the most severe/‘pits’ state (‘55555’) (included in all blocks). In the cTTO tasks, respondents are asked to determine their point of indifference between two lives: life A, comprising 10 or fewer years in full health, and life B, consisting of 10 years in an impaired health state *i*. cTTO applies the classic approach for health states deemed better than dead, wherein the respondent reaches an indifference point between the duration of time ‘x’ in full health (Life A) and 10 years in an impaired health state *i* (Life B). The utility value of the impaired health state *i* (U<sub>i</sub>) is defined as ‘x’ divided by 10 (U<sub>i</sub> = x/10) (Appendix Fig. 1 in Supplemental Materials). If participants still prefer life A when the number of years in life A is zero (meaning life B is considered worse than dead), cTTO then uses a lead-time TTO. The two lives in the lead-time TTO are 10 or fewer years of full health (Life A) and 10 years of full health followed by 10 years in an impaired health state (Life B). When respondents reach an indifference point between the amount of time ‘x’ in Life A and Life B, the utility value of the health state *i* may be calculated as U<sub>i</sub> = (x−10)/10 (Appendix Fig. 2 in Supplemental Materials). In the DCE tasks, participants are presented with two EQ-5D-5L health states and asked to choose which one they consider better. The DCE included 196 EQ-5D-5L health states distributed in 28 blocks, each with 7 choice pairs.

### Interview procedure

Each interview followed these steps:

1.  Explain the purposes and duration of the interview.

2.  Present the informed consent and ask the participant for their agreement to participate in the study.

3.  Collect information on participants’ age, sex and experience with chronic illness.

4.  Assess participant’s HRQoL using the EQ-5D-5L instrument which consists of a descriptive system and a Visual Analogue Scale (EQ VAS). The descriptive system comprises five dimensions (5D) including (i) mobility, (ii) self-care, (iii) usual activities, (iv) pain/discomfort and (v) anxiety/depression. For each dimension there are five levels (5L) representing the severity of problems experienced: no problems (level 1), slight problems (level 2), moderate problems (level 3), severe problems (level 4) and extreme problems/unable (level 5). The EQ VAS was used to assess subject’s health status with a score from 0 to 100, where 0 refers to ‘the worst health you can imagine’ and 100 ‘the best health you can imagine’.

5.  Complete the cTTO tasks, which include two wheelchair examples, three practice EQ-5D-5L states (21121, mild; 15411, moderate and 35554, severe), ten ‘real’ EQ-5D-5L health states, and debriefing questions.

6.  Complete the feedback module to review the ranking of cTTO responses.

7.  Complete the DCE tasks in which the respondent was asked to complete seven paired comparisons, followed by debriefing questions.

8.  Collect participants’ additional socio-demographic and clinical characteristics.

For illiterate participants, the concepts and tasks were explained verbally in detail by the interviewer. Particular attention was given to the wheelchair example, with repeated explanations and checks for understanding before proceeding to the main tasks.

### Pilot study

A pilot study was conducted from November to December 2022 to: (i) test the feasibility and adequacy of the EQ-VT protocol in the Moroccan context, (ii) identify specific elements of the protocol that might require adaptation, and (iii) standardize interviewer performance to reduce intra-interviewer and inter-interviewer variability and to promote data quality. A total of 121 interviews were conducted in the pilot phase.

### Quality control

During both the pilot and live study, two members of the EQ-VT Support Team monitored the performance of the interviewers and the quality of the data collected using the quality control (QC) tool developed by the EuroQol Group \[31\]. After each interviewer completed 10 interviews, a report was generated, and a QC meeting was organized between the EQ-VT Support Team and the Moroccan research team to discuss the reports. This process continued regularly until the end of the study data collection. Interviews were flagged if they met at least one of the following criteria:

1.  The time spent explaining the cTTO tasks using the wheelchair examples was too short (\< 3 min).

2.  There was no explanation of the ‘worse than dead’ format of the wheelchair example.

3.  Inconsistencies in the cTTO responses (i.e. the value of 55555 was not the lowest and was at least 0.5 higher than the health state with the lowest value).

4.  The time spent on the 10 cTTO tasks was less than 5 min.

### Statistical analysis

#### Description of the study sample

Descriptive statistics (frequencies and percentages) were used to describe the socio-demographic characteristics of the sample. Participants’ responses to the EQ-5D-5L instrument were summarized as percentages by severity levels for each health dimension. EQ VAS scores were presented as mean and standard deviation.

#### Data modeling

In order to estimate the Moroccan value set, three statistical models were applied separately to the cTTO (Model 1), DCE (Model 2), and cTTO combined with DCE (Model 3) data.

#### cTTO data modeling

In Model 1, the cTTO data were modeled using a heteroscedastic censored Tobit model \[32\], with 20 parameters (4 dummy variables representing the disutility from level 1 (no problem) to the other levels for each of the 5 dimensions). Due to the way in which the cTTO task is constructed, respondents are constrained in the number of life years they are able to trade to avoid the health problems of Life B. They can at most decide to trade 10 years in full health to avoid 10 years in full health followed by 10 years in the state to be valued, and thereby assigning a value of −1 to the health state. However, it is possible that they would have traded more life years, had this been possible in the cTTO task. To account for this in the modelling, Model 1 left-censored the cTTO data at −1 by introducing a latent variable (cTTO\*) as follows:

``` math
{\mathbf{c}\mathbf{T}\mathbf{T}\mathbf{O}}^{\ast} = \left\{ \begin{array}{l}
{- 1,if\, observed\, cTTO \leq - 1} \\
{cTTO\, observed,\, if\, observed\, cTTO > - 1}
\end{array} \right)
```

In addition, it has been reported that the observed variance of cTTO values increases with the severity of the health states \[33, 34\]. Model 1 takes into account this heteroscedasticity assuming that the error terms are independent and identically distributed following a normal distribution with mean zero and different variances. Therefore, the Model 1 was written:

``` math
\mathit{cTTO}_{\mathit{ij}} = \beta_{MO2}{MO2}_{j} + \beta_{MO3}{MO3}_{j} + \beta_{MO4}{MO4}_{j} + \beta_{MO5}{MO5}_{j} + \beta_{SC2}{SC2}_{j} + \beta_{SC3}{SC3}_{j} + \beta_{SC4}{SC4}_{j} + \beta_{SC5}{SC5}_{j} + \beta_{UA2}{UA2}_{j} + \beta_{UA3}{UA3}_{j} + \beta_{UA4}{UA4}_{j} + \beta_{UA5}{UA5}_{j} + \beta_{PD2}{PD2}_{j} + \beta_{PD3}{PD3}_{j} + \beta_{PD4}{PD4}_{j} + \beta_{PD5}{PD5}_{j} + \beta_{AD2}{AD2}_{j} + \beta_{AD3}{AD3}_{j} + \beta_{AD4}{AD4}_{j} + \beta_{AD5}{AD5}_{j} + \varepsilon_{\mathit{ij}}
```

where *i* refers to the respondent and *j* for the multiple tasks completed. MO, SC, UA, PD and AD are mobility, self-care, usual activities, pain/discomfort and anxiety/depression. The numbers 2, 3, 4 and 5 indicate levels of severity for each dimension, and $`\varepsilon_{\mathit{ij}} \sim N\left( {O,,,\sigma_{j}^{2}} \right)`$ is a heteroscedastic error term.

``` math
\sigma_{j} = \text{exp}{(\gamma_{0} + \gamma_{1}{MO2}_{j} + \gamma_{2}{MO3}_{j} + \gamma_{3}{MO4}_{j} + \gamma_{4}{MO5}_{j} + \gamma_{5}{SC2}_{j} + \gamma_{6}{SC3}_{j} + \gamma_{7}{SC4}_{j} + \gamma_{8}{SC5}_{j} + \gamma_{9}{UA2}_{j} + \gamma_{10}{UA3}_{j} + \gamma_{11}{UA4}_{j} + \gamma_{12}{UA5}_{j} + \gamma_{13}{PD2}_{j} + \gamma_{14}{PD3}_{j} + \gamma_{15}{PD4}_{j} + \gamma_{16}{PD5}_{j} + \gamma_{17}{AD2}_{j} + \gamma_{18}{AD3}_{j} + \gamma_{19}{AD4}_{j} + \gamma_{20}{AD5}_{j})}
```

#### DCE data modeling

The DCE data were modeled using the conditional logistic regression model recommended for modeling data from choice-based experiments \[35\]. This model is used for data collected from participants where the interviewer asks them to choose between two situations A and B. In our study, situations A and B represent two different health states from which the participant must choose their preferred state. In this model, one state is coded as ‘1’ and the other as ‘0’. The values collected are modeled by conditional-logit:

``` math
Prob\left( {c,h,o,i,c,e, = ,i} \right) = \frac{e^{u(\beta,X_{i})}}{e^{u(\beta,X_{i})} + e^{u(\beta,X_{j})}}
```

where, $`Prob\left( {c,h,o,i,c,e, = ,i} \right)`$ is the probability of choosing health state “i” by a participant when both states “i” and “j” are proposed; and $`u(\beta,X_{i})`$ is the function relating parameters b to the health state levels. The probability of choosing health state “i” is a function of both the EQ-5D-5L levels of alternative ‘i’ and those of state ‘j’ presented in a choice task. X<sub>i</sub> and X<sub>j</sub> are the vectors representing the EQ-5D-5L states ‘i’ and ‘j’, respectively. b is a 20-parameters vector to estimate. In this model, we used a dummy-variable coding approach. The level 1 (no problem) for each EQ-5D-5L dimension was omitted. The non-omitted levels (levels 2, 3, 4 and 5 of each health dimension) are assigned a value of 1 when that level is present in the corresponding health state and 0 when another non-omitted level is present in the corresponding profile. Each of the 20 estimated coefficients corresponding to the 20 levels (4 for each health dimension) is a measure of the disutility (or decrement) of that level relative to the no-problem level.

#### Combined cTTO and DCE data modeling

The cTTO and DCE data were combined in a hybrid model by multiplying the likelihood function of the cTTO model by the likelihood function of the DCE model. The hybrid model is based on the idea that both linear regression (applied to cTTO data) and conditional-logistic regression (applied to DCE data) can be obtained by maximum likelihood estimation, and that both models contain a linear component represented by $`\beta X`$ for the cTTO model and $`\beta'X`$ for the DCE model. Assuming that this component, which reflects the weight given to dimensions and their severity levels, is identical between the two regression models, we can find the optimal parameters for the combination of cTTO and DCE data. This is done by creating a single likelihood function for the combined data by multiplying the likelihoods of the cTTO data and the DCE data, assuming the relationship: $`\beta = \theta\beta'`$.

### Sensitivity analysis

A sensitivity analysis was conducted to assess the robustness of the results. In this process, flagged or inconsistent cTTO responses were excluded from the analysis. The impact of these exclusions on the overall results was then compared to the full dataset.

#### Goodness of fit

Model fit was assessed using the following criteria: (i) prediction accuracy (mean absolute error \[MAE\]); (ii) logical consistency: coefficients are positive and their values increase with the level of severity of the health dimension; (iii) significance: coefficients are statistically significant; (iv) the model parsimony, and (v) the AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) evaluation criteria.

Data analysis was performed using STATA software version 18.

## Results

### Participants’ characteristics

Overall, 1590 potential respondents were approached, of whom 1048 were interviewed (response rate 66%). The main reason for refusal to participate was lack of time or disinterest in the subject of the study (n = 542; 34%). A total of 42 interviews were incomplete, 30 were excluded due to poor quality and 976 interviews were included in the final analysis.

The reasons for excluding the 30 respondents were as follows: 3 respondents were excluded because the interviewers spent less than 3 min explaining the wheelchair example (Criterion 1), 2 were excluded for not explaining the “worse than dead” element of the task (Criterion 2), 5 were excluded due to inconsistencies related to the health state 55555 in cTTO (Criterion 3), 17 were excluded for spending less than 5 min on the 10 cTTO tasks (Criterion 4), and 3 for failing both Criteria 3 and 4. These exclusions were made to ensure the validity and reliability of the data collected.

A total of 28.3% participants had at least one inconsistency (incorrectly ranked), which reduced to 20.9% after using the feedback module. The mean interview duration was 58.7 min (SD = 20.6). The mean time spent on a single cTTO task was 114.9 s (SD = 90.8) and on a single DCE task, it was 75.4 s (SD = 66.5). The average number of iterations to reach the indifference point in the cTTO task was 6.8 steps (SD = 8.2).

For DCE tasks, in total, 20 participants answered using a specific pattern (e.g. ABABABA, BABABAB). However, their mean time to complete the DCE tasks was acceptable, so we decided not to exclude these interviews from the analysis.

Table <a href="#Tab1" data-ref-type="table">1</a> presents the characteristics of the study sample. The average age was 41.6 years. The sample was representative of the general Moroccan population in terms of age, sex and place of residence. However, illiterate participants were under-represented compared to the general Moroccan population. Figure <a href="#Fig1" data-ref-type="fig">1</a> shows the geographical distribution of participants. Moroccan geographical areas were well represented, based on data from the latest 2014 general population and housing census available from the HCP \[28\].

<div id="Tab1" class="table-wrap">

<div class="caption">

Socio-demographic and health-related characteristics of respondents

</div>

| Characteristics | Study sample n (%) | Morocco’s general population<sup>a</sup> % | Difference % |
|----|----|----|----|
| *Sex* |  |  |  |
| Male | 498 (49.50) | 49.81 | −0.31 |
| Female | 508 (50.50) | 50.19 | 0.31 |
| *Age (years)* |  |  |  |
| 18–25 | 193 (19.18) | 18.84 | 0.34 |
| 26–30 | 125 (12.42) | 11.84 | 0.58 |
| 31–35 | 111 (11.04) | 11.07 | −0.03 |
| 36–40 | 104 (10.34) | 10.39 | −0.05 |
| 41–45 | 95 (9.44) | 9.39 | 0.05 |
| 46–50 | 84 (8.35) | 8.60 | −0.25 |
| 51–55 | 71 (7.06) | 7.29 | −0.23 |
| 56–60 | 71 (7.06) | 7.04 | 0.02 |
| 61–65 | 55 (5.47) | 5.52 | −0.05 |
| 66–70 | 44 (4.37) | 4.40 | −0.03 |
| 71–75 | 21 (2.09) | 2.46 | −0.37 |
| 75 +  | 32 (3.18) | 3.16 | 0.02 |
| *Residence* |  |  |  |
| Urban | 644 (64.02) | 60.40 | **3.62\*** |
| Rural | 362 (36.98) | 39.60 | −**3.62\*** |
| *Marital status* |  |  |  |
| Single | 291 (28.93) | 34.81 | −**5.88\*\*\*** |
| Married | 678 (67.39) | 57.49 | **9.9\*\*\*** |
| Divorced | 13 (1.29) | 2.21 | −0.92 |
| Widowed | 24 (2.39) | 5.49 | −**3.1\*\*\*** |
| *Education level* |  |  |  |
| Illiterate | 45 (4.47) | 32.25 | −**27.78\*\*\*** |
| Primary | 180 (17.89) | 32.50 | −**14.61\*\*\*** |
| Secondary | 374 (37.18) | 16.40 | **20.78\*\*\*** |
| University | 407 (40.46) | 18.69 | **21.77\*\*\*** |
| *Employment status* |  |  |  |
| Employed | 321 (31.91) | 34.30 | −2.39 |
| Unemployed | 685 (68.09) | 65.70 | 2.39 |
| *Socio-economic level* |  |  |  |
| Low | 139 (13.82) | – | – |
| Medium | 811 (80.62) | – | – |
| High | 56 (5.56) | – | – |
| *Health insurance* |  |  |  |
| No | 303 (30.12) | – | – |
| Yes | 703 (69.88) | – | – |
| *Chronic illness* |  |  |  |
| No | 851 (84.59) | – | – |
| Yes | 155 (15.41) | – | – |
| EQ VAS, mean ± SD | 77.25 ± 17.05 |  |  |
| EQ-5D-5L dimensions (%) |  |  |  |
| *Mobility* |  |  |  |
| No problems | 73.66 |  |  |
| Mild problems | 18.69 |  |  |
| Moderate problems | 6.06 |  |  |
| Severe problems | 1.49 |  |  |
| Unable | 0.10 |  |  |
| *Self-care* |  |  |  |
| No problems | 84.29 |  |  |
| Mild problems | 11.13 |  |  |
| Moderate problems | 3.58 |  |  |
| Severe problems | 0.80 |  |  |
| Unable | 0.20 |  |  |
| *Usual activities* |  |  |  |
| No problems | 73.46 |  |  |
| Mild problems | 19.48 |  |  |
| Moderate problems | 5.86 |  |  |
| Severe problems | 0.70 |  |  |
| Unable | 0.50 |  |  |
| *Pain/ Discomfort* |  |  |  |
| No problems | 67.99 |  |  |
| Mild problems | 26.64 |  |  |
| Moderate problems | 4.77 |  |  |
| Severe problems | 0.50 |  |  |
| Extreme problems | 0.10 |  |  |
| *Anxiety/Depression* |  |  |  |
| No problems | 55.47 |  |  |
| Mild problems | 33.10 |  |  |
| Moderate problems | 10.44 |  |  |
| Severe problems | 0.89 |  |  |
| Extreme problems | 0.10 |  |  |

*EQ VAS* EuroQol Visual Analogue Scale

Significant values are in bold

\*p \< 0.05 and \*\*\*p \< 0.001 from z test

<sup>a</sup>2014 general population and housing census data\[28\]

</div>

<figure id="Fig1">
<p><img src="11136_2025_3930_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="11136_2025_3930_Fig1_HTML.gif" /></p>
<figcaption>Geographical distribution of respondents</figcaption>
</figure>

### Health-related quality of life of participants

Table <a href="#Tab1" data-ref-type="table">1</a> summarizes participants' self-reported EQ-5D-5L responses. Overall, 42.54% of the respondents reported being in full health (11111). The most common health problem reported by participants was anxiety/depression (44.53%), and the least frequent health problem was self-care (15.71%). The mean ± standard deviation EQ VAS score was 77.25 ± 17.05.

### Data characteristics

Figure <a href="#Fig2" data-ref-type="fig">2</a> shows the distribution of observed mean cTTO values obtained for the 86 health states valued. Values ranged from −1 to 1, with intervals of 0.05. The majority of cTTO values were positive (62%), while 38% were negative. The proportion of −1 and + 1 values were 8.6% and 8.4% respectively. There were very few 0 values (1.1%). The mean observed cTTO values for the 86 health states ranged from 0.970 for health state “11211” to −0.940 for worst health state “55555”. Figure <a href="#Fig3" data-ref-type="fig">3</a>, presents the distribution of the mean observed cTTO values of the 86 health states evaluated as a function of the Level Sum Score (LSS). cTTO values were inversely related to LSS. A statistical analysis comparing cTTO value distributions between Arabic and French interviews found no significant difference (p = 0.921), indicating that the interview language did not affect the cTTO values. A statistical analysis was performed to compare the cTTO value distributions between interviews conducted in Arabic and French. A statistical analysis comparing cTTO value distributions between interviews conducted in Arabic and French showed no significant difference (*p* = 0.921), indicating that the interview language did not impact the distribution of cTTO values.

<figure id="Fig2">
<p><img src="11136_2025_3930_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="11136_2025_3930_Fig2_HTML.gif" /></p>
<figcaption>Distribution of the observed composite time trade-off (cTTO) values</figcaption>
</figure>

<figure id="Fig3">
<p><img src="11136_2025_3930_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="11136_2025_3930_Fig3_HTML.gif" /></p>
<figcaption>Mean observed cTTO values by level sum scores</figcaption>
</figure>

### Modelling results

Table <a href="#Tab2" data-ref-type="table">2</a> illustrates the three statistical models tested in order to generate the Moroccan value set for the 3125 EQ-5D-5L health states. The values of the coefficients estimated from the cTTO and DCE data show that all the tested models were logically consistent. Furthermore, all parameter estimates were statistically significant, with the exception of the mobility (level 2) for the cTTO heteroskedastic Tobit model (Model 1) and the usual activities (level 2 and 3) for the Conditional logit model (Model 2). The ranking order of the health dimensions was similar for the 3 models tested, with pain/discomfort and usual activities being the most and least important dimensions, respectively.

<div id="Tab2" class="table-wrap">

<div class="caption">

Parameter estimates for cTTO, DCE and hybrid models

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">cTTO<br />
heteroskedastic Tobit<br />
(Model 1)</th>
<th colspan="3" style="text-align: left;">DCE<br />
Conditional logit<br />
(Model 2)</th>
<th colspan="3" style="text-align: left;">Hybrid<br />
heteroskedastic Tobit<br />
(Model 3, Value set)</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">P-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">P-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">P-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>Mobility</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">MO2</td>
<td style="text-align: left;">0.010</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.105</td>
<td style="text-align: left;">0.465</td>
<td style="text-align: center;">0.065</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO3</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.764</td>
<td style="text-align: center;">0.074</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.110</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO4</td>
<td style="text-align: left;">0.280</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">1.304</td>
<td style="text-align: center;">0.079</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.262</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO5</td>
<td style="text-align: left;">0.507</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">3.068</td>
<td style="text-align: center;">0.108</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.565</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Self-care</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">SC2</td>
<td style="text-align: left;">0.038</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.285</td>
<td style="text-align: center;">0.073</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.038</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC3</td>
<td style="text-align: left;">0.088</td>
<td style="text-align: left;">0.010</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.398</td>
<td style="text-align: center;">0.077</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.080</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC4</td>
<td style="text-align: left;">0.231</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.769</td>
<td style="text-align: center;">0.078</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.197</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC5</td>
<td style="text-align: left;">0.340</td>
<td style="text-align: left;">0.010</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">1.390</td>
<td style="text-align: center;">0.078</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.322</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Usual activities</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">UA2</td>
<td style="text-align: left;">0.030</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">−0.029</td>
<td style="text-align: center;">0.067</td>
<td style="text-align: center;">0.665</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA3</td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;">0.010</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.081</td>
<td style="text-align: center;">0.079</td>
<td style="text-align: center;">0.304</td>
<td style="text-align: left;">0.046</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA4</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">0.010</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.505</td>
<td style="text-align: center;">0.078</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA5</td>
<td style="text-align: left;">0.296</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">1.015</td>
<td style="text-align: center;">0.082</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.268</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Pain/discomfort</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">PD2</td>
<td style="text-align: left;">0.042</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.472</td>
<td style="text-align: center;">0.072</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.049</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD3</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">1.062</td>
<td style="text-align: center;">0.080</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.159</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD4</td>
<td style="text-align: left;">0.506</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">1.948</td>
<td style="text-align: center;">0.084</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.459</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD5</td>
<td style="text-align: left;">0.778</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">3.388</td>
<td style="text-align: center;">0.114</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.751</td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Anxiety/depression</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">AD2</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.176</td>
<td style="text-align: center;">0.076</td>
<td style="text-align: center;">0.021</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: center;">0.004</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD3</td>
<td style="text-align: left;">0.124</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.787</td>
<td style="text-align: center;">0.077</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.159</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD4</td>
<td style="text-align: left;">0.310</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">1.621</td>
<td style="text-align: center;">0.090</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.339</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD5</td>
<td style="text-align: left;">0.566</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">2.724</td>
<td style="text-align: center;">0.100</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.585</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td style="text-align: left;">3684.9</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">5687.8</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">9557.1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td style="text-align: left;">3986.0</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">5825.0</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">9881.3</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">MAE (total)</td>
<td style="text-align: left;">0.275</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0.277</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">MAE (86 states)</td>
<td style="text-align: left;">0.059</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0.063</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">MAE out of sample (state)</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0.071</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">MAE out of sample (block)</td>
<td style="text-align: left;">0.099</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0.110</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">U (55555)</td>
<td style="text-align: left;">−1.489</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">11.585</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">−1.492</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">#illogically ordered</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">#non-significant</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Ranking of dimensions</td>
<td colspan="3" style="text-align: left;">PD, AD, MO, SC, UA</td>
<td colspan="3" style="text-align: left;">PD, MO, AD, SC, UA</td>
<td colspan="3" style="text-align: left;">PD, AD, MO, SC, UA</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *AIC* Akaike information criterion, *BIC* Bayesian information criterion, *MAE* Mean absolute error, *MO* mobility, *N/A* not applicable, *PD* pain/discomfort, *SC* self-care, *SE* standard error, *UA* usual activities

</div>

Comparison of the models showed that the hybrid heteroskedastic Tobit model (Model 3) performed best, as it showed logically consistent, significant coefficients, and comparable fit statistics such as MAE to the cTTO-only heteroskedastic Tobit model. As a result, the hybrid heteroskedastic Tobit model was used to develop the Moroccan value set for the 3125 EQ-5D-5L health states. To obtain the utility value of an EQ-5D-5L health state, the following calculation based on the hybrid model is required:

``` math
\text{Utility value of an EQ} - \text{5D} - \text{5L health state} = 1 - \,\left( {0.021 \ast \text{MO2}} \right) - \left( {0.110 \ast \text{MO3}} \right) - \left( {0.262 \ast \text{MO4}} \right) - \left( {0.565 \ast \text{MO5}} \right) - \left( {0.038 \ast \text{SC2}} \right) - \left( {0.080 \ast \text{SC3}} \right) - \left( {0.197 \ast \text{SC4}} \right) - \left( {0.322 \ast \text{SC5}} \right) - \left( {0.021 \ast \text{UA2}} \right) - \left( {0.046 \ast \text{UA3}} \right) - \left( {0.142 \ast \text{UA4}} \right) - \left( {0.268 \ast \text{UA5}} \right) - \left( {0.049 \ast \text{PD2}} \right) - \left( {0.159 \ast \text{PD3}} \right) - \left( {0.459 \ast \text{PD4}} \right) - \left( {0.751 \ast \text{PD5}} \right) - \left( {0.036 \ast \text{AD2}} \right) - \left( {0.159 \ast \text{AD3}} \right) - \left( {0.339 \ast \text{AD4}} \right) - \left( {0.585 \ast \text{AD5}} \right)
```

According to the hybrid heteroskedastic Tobit model, the pain/discomfort had the largest effect on health state preference values, followed by anxiety/depression, mobility, self-care and usual activities. The predicted cTTO values ranged from –1.492 for the worst health state (55555) to 1 for full health (11111) and 0.979 for 11211 and 21111 health states. Of the 3125 health states, 1271 (40.67%) have negative predicted values.

For example, the utility value for the health state 12345 according to the hybrid heteroskedastic Tobit model is equal to: 1−0−(0.038\*SC2)−(0.046\*UA3)−(0.459\*PD4)−(0.585\*AD5) = −0.128.

## Discussion

The present study reports the Moroccan EQ-5D-5L value set. This is the first study to present utility values for the EQ-5D-5L in Morocco and the third (following Egypt and Saudi Arabia studies) in the MENA region. To meet the study objective, a nationally representative sample of Morocco was recruited using stratified quota sampling. This sampling approach is in line with most previous studies developing EQ-5D-5L value sets \[33, 36–39\]. Our sample was representative of the general Moroccan population in terms of age, sex, geographical area and place of residence according to data from the latest 2014 general population and housing census available from the HCP \[28\].

The distribution of cTTO values obtained for the 86 health states evaluated showed that the majority (62%) of these observed values were positive (better-than-dead), while 38% were negative (worse-than-dead). This percentage of negative values is nearly identical to those reported in EQ-5D-5L valuation studies conducted in Taiwan (38.5%) \[39\], Hong Kong (36%) \[40\], and Indonesia (35.5%) \[37\]. However, it is higher than those observed in studies conducted in Denmark (22%) \[41\], Hungary (21.7%) \[42\], the United States (20%) \[43\], Germany (17.3%) \[33\], France (20.2%) \[44\], and Poland (4.4%) \[45\], but somewhat lower than in Egypt (40.9%) \[46\] and Uganda (44.3%) \[47\]. Furthermore, our study showed that the predicted value for worst health status (55555) was −1.492, which is comparable to Uganda \[48\] (−1.116). However, this value is lower than that attributed to the worst health status (55555) in other countries, including France \[49\] (−0.525), Saudi Arabia \[50\] (−0.683), Indonesia \[33\] (−0.865), and Malaysia \[59\] (−0.442). These variations in the proportion of worse-than-dead values across countries can be attributed to cultural, social, and religious differences, which may shape perceptions of health states and their severity \[13, 51\]. Indeed, in Morocco, the worst health status (55555), which reflect severe and debilitating conditions, may be considered particularly undesirable due to both limited healthcare access and strong societal values around health and well-being. The cTTO values in our study were relatively balanced between −1 and + 1, with proportions of 8.6% and 8.4%, respectively. This contrasts with other countries \[44, 46, 47, 49, 52\], where one extreme tends to dominate, suggesting that cultural factors in Morocco may influence how health states are valued. These findings highlight the necessity of contextualizing EQ-5D-5L value sets based on local conditions when using them in health technology assessments and decision-making.

The Hybrid heteroskedastic Tobit model was selected as the preferred model to develop the Moroccan value set. The model performed similarly to a cTTO-only heteroskedastic Tobit model, and maximizes data utilization by incorporating both the cTTO and DCE data. According to this hybrid model, pain/discomfort had the largest effect on health state preferences, followed by anxiety/depression, mobility, self-care and usual activities. This ranking of the five EQ-5D-5L dimensions in Morocco is similar to that in Spain \[53\]. In addition, pain/discomfort is ranked as the most important dimension in other countries, including Saudi Arabia \[48\], France \[44\] and Uganda \[47\]. In contrast, in Ethiopia \[36\], anxiety/depression was ranked as the most important dimension, followed by pain/discomfort. This contrasts sharply with the EQ-5D-5L value set of Uganda \[47\], where the anxiety/depression was the least important dimension. In addition, a further countries rank mobility as the most important dimension, including Indonesia \[37\], Malaysia \[50\], and Egypt \[46\]. In this study, usual activities are considered the least important dimension. This result is consistent with most previous studies developing EQ-5D-5L value sets, notably Saudi Arabia \[48\], France \[44\], Spain \[53\], Malaysia \[50\], and Egypt \[46\]. However, this contrasts with other countries, including Ethiopia \[36\], which consider the self-care dimension to be the least important. This comparison shows that the EQ-5D-5L value sets differ considerably between countries in terms of the relative importance of the five health dimensions. These differences are assumed to be influenced by a wide range of country-specific institutional and other circumstances, which impact on individuals' health opportunities and challenges, and can shape health expectations and norms.

The comparison between the Moroccan EQ-5D-3L \[24\] and EQ-5D-5L value sets reveals key differences, especially regarding the value assigned to the worst health state (–0.5736 for the worst health state 33333, compared to –1.492 for the worst health state 55555). Additionally, there is a difference in the ranking of the dimensions based on their impact on health state preference values. In the EQ-5D-3L value set, mobility had the largest effect, followed by pain/discomfort, self-care, anxiety/depression, and usual activities. In contrast, in the EQ-5D-5L value set, pain/discomfort was the most influential dimension, followed by anxiety/depression, mobility, self-care, and usual activities. These differences can be attributed to the increased granularity provided by the EQ-5D-5L, which expands the response levels from three to five, allowing for more precise distinctions between mild, moderate, and severe health states. Also, in the EQ-5D-3L, the most severe level of mobility is ‘confined to bed,’ which might have led to mobility being considered the most important dimension. In contrast, the EQ-5D-5L uses ‘Unable to walk’ as the most severe level, which is less extreme than ‘confined to bed.’ While the EQ-5D-3L value set provided a solid starting point, the EQ-5D-5L offers greater precision and reflects a more diverse range of health problems.

This study has several strengths. It is the first to establish an EQ-5D-5L value set for Morocco, representing a significant contribution to HTA and health economic evaluations in the MENA region. With the growing interest in HTA in Morocco and the many studies underway using the EQ-5D-5L instrument, this value set will be crucial. It provides a robust framework for evaluating health outcomes and informing healthcare policies. The data were generated using the internationally standardized EQ-VT protocol developed by the EuroQol Group, ensuring high data quality and external validity. The hybrid heteroskedastic Tobit model, which combines data from cTTO and DCE, maximized data utilization and provided a robust value set tailored to the Moroccan population. The rigorous quality control measures, including standardized interviewer training, frequent monitoring, and a low 2.9% rate of suboptimal-quality interviews, further enhanced the reliability of the results.

Several study limitations and challenges should be noticed. Rural and low-literacy participants were underrepresented compared to Moroccan High Commission for Planning data, despite efforts to ensure geographical diversity. The EQ-VT protocol, designed for literate populations, posed challenges for illiterate participants. Interviewers addressed this by providing detailed verbal explanations, particularly of the wheelchair example, to ensure comprehension. While this facilitated inclusion, the quota for illiterate participants was not fully achieved. Future research should explore tailored approaches to better represent underrepresented populations and address these gaps in valuation studies.

## Conclusions

Morocco is the third country in the MENA region with an EQ-5D-5L value set. The availability of the EQ-5D-5L value set will serve as a scoring algorithm for health economic evaluations, aiding decision-making and improving the quality of HTA in the Moroccan healthcare system. In addition, it may be used to implement patient-reported outcomes measures for routine clinical practice to improve the monitoring and management of patients and thus provide more evidence for decision-makers in the healthcare systems in Morocco. Furthermore, the results can be used for international comparisons to understand similarities and differences in health preferences between populations.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 211 KB)

</div>

## Author contributions

Concept and design: AA, AM, IYM, EAS, BR; Acquisition of data: AA, AM, IYM, AB, DA, ES, AH, EAS, FDP, FR; Analysis and interpretation of data: AA, AM, EAS, FDP, FR, BR, CN, SA; Drafting of the manuscript: AA, AM, IYM, AB, SA, CN, EAS, AB; Critical revision of the paper for important intellectual content: EAS, FDP, FR, AA, AM, BR, AH, ES, DA, AB, IYM, CN, SA; Statistical analysis: AM, AA, EAS, BR; Provision of study materials or patients: AA, AM, DA, IYM, AB; Obtaining funding: AM; Administrative, technical, or logistic support: ES, AH, EAS, FDP, FR; Supervision: AM, IYM, BR, AA.

## Funding

The Moroccan EQ-5D-5L valuation study was funded from the EuroQol Research Foundation, the Netherlands (Grant Number: 1411-VS).

## Data availability

The data presented in this study are available on request from the corresponding author.

## Declarations

### Conflict of interest

F.D.P., F.R., E.A.S. and B.R. are members of the EuroQol Group. The views expressed in this article are those of the authors and do not necessarily reflect those of the EuroQol Research Foundation.

### Ethical approval

This study was approved by “the Ethics Committee for Biomedical Research from the Faculty of Medicine and Pharmacy of Rabat, Morocco (CERB O-22)”.

### Consent to participate

Informed consent was obtained from all individual participants included in the study.

## Footnotes

## References

## References

1. Hailey, D. (2003). Elements of effectiveness for health technology assessment programs. desLibris. Retrieved from https://policycommons.net/artifacts/1215076/elements-of-effectiveness-for-health-technology-assessment-programs/1768175/

2. Tantivess, S. (2008). Policy making and roles of health technology assessment. Journal of the Medical Association of Thailand,91(Suppl 2), S88-99.

3. Stratégie nationale de financement de la santé - Recherche Google. (n.d.). Retrieved April 5, 2023, from https://www.google.com/search?q=strat%C3%A9gie+nationale+de+financement+de+la+sant%C3%A9&rlz=1C1GCEA_enMA1016MA1016&oq=strat%C3%A9gie+nationale+de+financement+de+la+sant%C3%A9&aqs=chrome..69i57j0i512l2.342j0j7&sourceid=chrome&ie=UTF-8

4. Azizi, A., Achak, D., Aboudi, K., Saad, E., Nejjari, C., Nouira, Y., & Marfak, A. (2020). Health-related quality of life and behavior-related lifestyle changes due to the COVID-19 home confinement: Dataset from a Moroccan sample. Data in Brief. 10.1016/j.dib.2020.106239

5. Boutib, A., Chergaoui, S., Azizi, A., Achak, D., Saad, E. M., Hilali, A., & Marfak, A. (2024). Health-related quality of life among Moroccan women after vaginal birth and cesarean section: Cross-sectional study. Heliyon. 10.1016/j.heliyon.2024.e32276

6. Achak, D., El-Ammari, A., Azizi, A., Youlyouz-Marfak, I., Saad, E., Nejjari, C., & Marfak, A. (2023). Lifestyle habits determinants of health-related quality of life in Moroccan College students. International Journal of Environmental Research and Public Health. 10.3390/ijerph20032394

7. Azizi, A., Achak, D., Saad, E., Hilali, A., Nejjari, C., Khalis, M., & Marfak, A. (2022). Health-Related Quality of Life of Moroccan COVID-19 Survivors: A Case-Control Study. International Journal of Environmental Research and Public Health,19(14), 8804. 10.3390/ijerph19148804

8. Traki, L., Rostom, S., Tahiri, L., Bahiri, R., Harzy, T., Abouqal, R., & Hajjaj-Hassouni, N. (2014). Responsiveness of the EuroQol EQ-5D and Hospital Anxiety and Depression Scale (HADS) in rheumatoid arthritis patients receiving tocilizumab. Clinical Rheumatology,33(8), 1055–1060. 10.1007/s10067-014-2609-z

9. Marfak, A., Youlyouz-Marfak, I., El Achhab, Y., Saad, E., Nejjari, C., Hilali, A., & Turman, J. (2020). Improved RIDIT statistic approach provides more intuitive and informative interpretation of EQ-5D data. Health and Quality of Life Outcomes,18(1), 63. 10.1186/s12955-020-01313-3

10. Drummond, M. F., Sculpher, M. J., Claxton, K., Stoddart, G. L., & Torrance, G. W. (2015). Methods for the economic evaluation of health care programmes (4th ed.). Oxford University Press.

11. Sassi, F. (2006). Calculating QALYs, comparing QALY and DALY calculations. Health Policy and Planning,21(5), 402–408. 10.1093/heapol/czl018

12. Cleland, J., Hutchinson, C., Khadka, J., Milte, R., & Ratcliffe, J. (2019). A review of the development and application of generic preference-based instruments with the older population. Applied Health Economics and Health Policy,17(6), 781–801. 10.1007/s40258-019-00512-4

13. Roudijk, B., Donders, A. R. T., Stalmeier, P. F. M., Luo, N., Viney, R., Andrade, M. V., & Tongsiri, S. (2019). Cultural values: Can they explain differences in health utilities between countries? Medical Decision Making,39(5), 605–616. 10.1177/0272989X19841587

14. Richardson, J., Khan, M. A., Iezzi, A., & Maxwell, A. (2015). Comparing and explaining differences in the magnitude, content, and sensitivity of utilities predicted by the EQ-5D, SF-6D, HUI 3, 15D, QWB, and AQoL-8D multiattribute utility instruments. Medical Decision Making,35(3), 276–291. 10.1177/0272989X14543107

15. Kennedy-Martin, M., Slaap, B., Herdman, M., van Reenen, M., Kennedy-Martin, T., Greiner, W., & Boye, K. S. (2020). Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. The European Journal of Health Economics,21(8), 1245–1257. 10.1007/s10198-020-01195-8

16. Rencz, F., Gulácsi, L., Drummond, M., Golicki, D., Prevolnik Rupel, V., Simon, J., & Péntek, M. (2016). EQ-5D in central and eastern Europe: 2000–2015. Quality of Life Research,25(11), 2693–2710. 10.1007/s11136-016-1375-6

17. National Institute for Health and Care Excellence. (2013). Guide to the Methods of Technology Appraisal 2013. London: National Institute for Health and Care Excellence (NICE). Retrieved from http://www.ncbi.nlm.nih.gov/books/NBK395867/

18. Qian, X., Tan, R.L.-Y., Chuang, L.-H., & Luo, N. (2020). Measurement properties of commonly used generic preference-based measures in east and south-east Asia: A systematic review. PharmacoEconomics,38(2), 159–170. 10.1007/s40273-019-00854-w

19. Finch, A. P., Brazier, J. E., & Mukuria, C. (2018). What is the evidence for the performance of generic preference-based measures? A systematic overview of reviews. The European Journal of Health Economics,19(4), 557–570. 10.1007/s10198-017-0902-x

20. Brooks, R. (1996). EuroQol: The current state of play. Health Policy (Amsterdam, Netherlands),37(1), 53–72. 10.1016/0168-8510(96)00822-6

21. Herdman, M., Gudex, C., Lloyd, A., Janssen, M., Kind, P., Parkin, D., & Badia, X. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research,20(10), 1727–1736. 10.1007/s11136-011-9903-x

22. Feng, Y.-S., Kohlmann, T., Janssen, M. F., & Buchholz, I. (2021). Psychometric properties of the EQ-5D-5L: A systematic review of the literature. Quality of Life Research,30(3), 647–673. 10.1007/s11136-020-02688-y

23. Devlin, N., Pickard, S., & Busschbach, J. (2022). The development of the EQ-5D-5L and its value sets. In N. Devlin, B. Roudijk, & K. Ludwig (Eds.), Value sets for EQ-5D-5L: A compendium, comparative review & user guide. Springer.

24. PNS396 Valuing health related quality of life in Morocco: An EQ-5D-3L value set—Value in health. (n.d.). Retrieved 18 Dec 2024, from https://www.valueinhealthjournal.com/article/S1098-3015(19)34674-1/fulltext

25. Janssen, M. F., Bonsel, G. J., & Luo, N. (2018). Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. PharmacoEconomics,36(6), 675–697. 10.1007/s40273-018-0623-8

26. Xie, F., Pickard, A. S., Krabbe, P. F. M., Revicki, D., Viney, R., Devlin, N., & Feeny, D. (2015). A checklist for reporting valuation studies of multi-attribute utility-based instruments (CREATE). PharmacoEconomics,33(8), 867–877. 10.1007/s40273-015-0292-9

27. Stolk, E., Ludwig, K., Rand, K., van Hout, B., & Ramos-Goñi, J. M. (2019). Overview, update, and lessons learned from the international EQ-5D-5L valuation work: Version 2 of the EQ-5D-5L valuation protocol. Value in Health,22(1), 23–30. 10.1016/j.jval.2018.05.010

28. Gauthier, C. (n.d.). Projections de la population totale du Maroc par âge simple et sexe 2014–2050. Site institutionnel du Haut-Commissariat au Plan du Royaume du Maroc. Retrieved 1 Mar 2023, from https://www.hcp.ma/Projections-de-la-population-totale-du-Maroc-par-age-simple-et-sexe-2014-2050_a2209.html

29. Oppe, M., Rand-Hendriksen, K., Shah, K., Ramos-Goñi, J. M., & Luo, N. (2016). EuroQol protocols for time trade-off valuation of health outcomes. PharmacoEconomics,34(10), 993–1004. 10.1007/s40273-016-0404-1

30. Oppe, M., & Hout, B. (2017). The “power” of eliciting EQ-5D-5L values: The experimental design of the EQ-VT.

31. Ramos-Goñi, J. M., Oppe, M., Slaap, B., Busschbach, J. J. V., & Stolk, E. (2017). Quality control process for EQ-5D-5L valuation studies. Value in Health,20(3), 466–473. 10.1016/j.jval.2016.10.012

32. Tobin, J. (1958). Estimation of relationships for limited dependent variables. Econometrica,26(1), 24. 10.2307/1907382

33. Ludwig, K., Graf von der Schulenburg, J.-M., & Greiner, W. (2018). German value set for the EQ-5D-5L. PharmacoEconomics,36(6), 663–674. 10.1007/s40273-018-0615-8

34. Shah, K. K., Ramos-Goñi, J. M., Kreimeier, S., & Devlin, N. J. (2020). An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values. The European Journal of Health Economics,21(7), 1091–1103. 10.1007/s10198-020-01205-9

35. McFadden, D. (1974). Conditional logit analysis of qualitative choice behavior. Frontiers in Econometrics.

36. Welie, A. G., Gebretekle, G. B., Stolk, E., Mukuria, C., Krahn, M. D., Enquoselassie, F., & Fenta, T. G. (2020). Valuing health state: An EQ-5D-5L value set for Ethiopians. Value in Health Regional Issues,22, 7–14. 10.1016/j.vhri.2019.08.475

37. Purba, F. D., Hunfeld, J. A. M., Iskandarsyah, A., Fitriana, T. S., Sadarjoen, S. S., Ramos-Goñi, J. M., & Busschbach, J. J. V. (2017). The Indonesian EQ-5D-5L value set. PharmacoEconomics,35(11), 1153–1165. 10.1007/s40273-017-0538-9

38. Kim, S.-H., Ahn, J., Ock, M., Shin, S., Park, J., Luo, N., & Jo, M.-W. (2016). The EQ-5D-5L valuation study in Korea. Quality of Life Research,25(7), 1845–1852. 10.1007/s11136-015-1205-2

39. Lin, H.-W., Li, C.-I., Lin, F.-J., Chang, J.-Y., Gau, C.-S., Luo, N., & Hsu, C.-N. (2018). Valuation of the EQ-5D-5L in Taiwan. PLoS ONE,13(12), e0209344. 10.1371/journal.pone.0209344

40. Wong, E. L. Y., Ramos-Goñi, J. M., Cheung, A. W. L., Wong, A. Y. K., & Rivero-Arias, O. (2018). Assessing the use of a feedback module to model EQ-5D-5L health states values in Hong Kong. The Patient,11(2), 235–247. 10.1007/s40271-017-0278-0

41. Ce, J., Ss, S., & C, G., Mb, J., Km, P., & Lh, E. (2021). The Danish EQ-5D-5L value set: A hybrid model using cTTO and DCE data. Applied Health Economics and Health Policy. 10.1007/s40258-021-00639-3

42. Rencz, F., Brodszky, V., Gulácsi, L., Golicki, D., Ruzsa, G., Pickard, A. S., & Péntek, M. (2020). Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time trade-off in Hungary. Value in Health,23(9), 1235–1245. 10.1016/j.jval.2020.03.019

43. Pickard, A. S., Law, E. H., Jiang, R., Pullenayegum, E., Shaw, J. W., Xie, F., & Busschbach, J. J. V. (2019). United States valuation of EQ-5D-5L health states using an international protocol. Value in Health,22(8), 931–941. 10.1016/j.jval.2019.02.009

44. Andrade, L. F., Ludwig, K., Goni, J. M. R., Oppe, M., & de Pouvourville, G. (2020). A French value set for the EQ-5D-5L. PharmacoEconomics,38(4), 413–425. 10.1007/s40273-019-00876-4

45. Golicki, D., Jakubczyk, M., Graczyk, K., & Niewada, M. (2019). Valuation of EQ-5D-5L health states in Poland: The first EQ-VT-based study in central and eastern Europe. PharmacoEconomics,37(9), 1165–1176. 10.1007/s40273-019-00811-7

46. Al Shabasy, S., Abbassi, M., Finch, A., Roudijk, B., Baines, D., & Farid, S. (2022). The EQ-5D-5L valuation study in Egypt. PharmacoEconomics,40(4), 433–447. 10.1007/s40273-021-01100-y

47. Yang, F., Katumba, K. R., Roudijk, B., Yang, Z., Revill, P., Griffin, S., & Sculpher, M. (2022). Developing the EQ-5D-5L value set for Uganda using the “lite” protocol. PharmacoEconomics,40(3), 309–321. 10.1007/s40273-021-01101-x

48. Al-Jedai, A., Almudaiheem, H., Al-Salamah, T., Aldosari, M., Almutairi, A. R., Almogbel, Y., & O’jeil, R. (2024). Valuation of EQ-5D-5L in the Kingdom of Saudi Arabia: A national representative study. Value in Health. 10.1016/j.jval.2024.01.017

49. Finch, A. P., Meregaglia, M., Ciani, O., Roudijk, B., & Jommi, C. (2022). An EQ-5D-5L value set for Italy using videoconferencing interviews and feasibility of a new mode of administration. Social Science & Medicine,292, 114519. 10.1016/j.socscimed.2021.114519

50. Shafie, A. A., Vasan Thakumar, A., Lim, C. J., Luo, N., Rand-Hendriksen, K., & Md Yusof, F. A. (2019). EQ-5D-5L valuation for the Malaysian population. PharmacoEconomics,37(5), 715–725. 10.1007/s40273-018-0758-7

51. Jakubczyk, M., Golicki, D., & Niewada, M. (2016). The impact of a belief in life after death on health-state preferences: True difference or artifact? Quality of Life Research,25(12), 2997–3008. 10.1007/s11136-016-1356-9

52. Versteegh, M., & M., M Vermeulen, K., M A A Evers, S., de Wit, G. A., Prenger, R., & A Stolk, E. (2016). Dutch Tariff for the five-level version of EQ-5D. Value in Health,19(4), 343–352. 10.1016/j.jval.2016.01.003

53. Ramos-Goñi, J. M., Craig, B. M., Oppe, M., Ramallo-Fariña, Y., Pinto-Prades, J. L., Luo, N., & Rivero-Arias, O. (2018). Handling data quality issues to estimate the Spanish EQ-5D-5L value set using a hybrid interval regression approach. Value in Health,21(5), 596–604. 10.1016/j.jval.2017.10.023

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 211 KB)

</div>

### Data Availability Statement

The data presented in this study are available on request from the corresponding author.

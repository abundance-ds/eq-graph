---
project_id: "20180030R1"
work_id: "doi:10.1007/s10198-022-01481-7"
doi: "10.1007/s10198-022-01481-7"
pmid: "35688994"
pmcid: "PMC10060331"
title: "EQ-5D-5L: a value set for Romania"
journal: "The European Journal of Health Economics"
publication_date: "2022-06-10"
volume: "24"
issue: "3"
authors:
  - name: "Elena Olariu"
    orcid: "http://orcid.org/0000-0002-8718-5516"
    affiliation_ids:
      - "Aff1"
  - name: "Wael Mohammed"
    orcid: "http://orcid.org/0000-0003-0370-4903"
    affiliation_ids:
      - "Aff1"
  - name: "Yemi Oluboyede"
    orcid: "http://orcid.org/0000-0002-9891-8279"
    affiliation_ids:
      - "Aff1"
  - name: "Raluca Caplescu"
    orcid: "http://orcid.org/0000-0001-6489-171X"
    affiliation_ids:
      - "Aff2"
  - name: "Ileana Gabriela Niculescu-Aron"
    orcid: "http://orcid.org/0000-0003-2902-1641"
    affiliation_ids:
      - "Aff2"
  - name: "Marian Sorin Paveliu"
    orcid: "http://orcid.org/0000-0002-0702-1715"
    affiliation_ids:
      - "Aff3"
  - name: "Luke Vale"
    orcid: "http://orcid.org/0000-0001-8574-8429"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.1006.70000 0001 0462 7212Health Economics Group, Population Health Sciences Institute, Newcastle University, Baddiley-Clark Building, Richardson Road, Newcastle upon Tyne, NE2 4AX UK"
  - id: "Aff2"
    name: "grid.432032.40000 0004 0416 9364Department of Statistics and Econometrics, Faculty of Economic Cybernetics, Statistics and Informatics, Bucharest University of Economic Studies, Bucharest, Romania"
  - id: "Aff3"
    name: "grid.445737.60000 0004 0480 9237Department of Pharmacology and Pharmaeconomics, Faculty of General Medicine, Titu Maiorescu University, Bucharest, Romania"
keywords:
  - "EQ-5D-5L"
  - "Health technology assessment"
  - "I10"
  - "I18"
  - "Utility"
  - "Value set"
licence: "cc-by"
source_file: "input/projects/20180030R1/papers/doi_10.1007_s10198-022-01481-7.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10060331/fullTextXML"
source_method: "epmc_xml"
source_sha256: "1d43766b183a4abf40ac2e65a1ab5cc75d3653182d139c8d45e818b0a097ac6e"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# EQ-5D-5L: a value set for Romania

## Abstract

### Objective

We aimed to develop an EQ-5D-5L value set for Romania.

### Methods

In line with the EuroQoL standardized valuation protocol, computer-assisted interviews were conducted face-to-face in a representative sample in Romania (November 2018–November 2019).

Valuation methods included composite time trade-off and discrete choice experiment tasks. Several models were tested, including models that accounted for data censoring, panel structure of the data, heteroscedasticity, conditional logit, and hybrid models. The final model was selected based on logical consistency, theoretical considerations, and use of all available data. We compared our value set with other value sets from Central and Eastern Europe region.

### Results

Data from 1493 respondents was used to estimate the value set. A censored hybrid model corrected for heteroscedasticity was selected to represent the value set. The highest decrements in utility were observed for the pain/discomfort dimension (0.375), followed by the mobility dimension (0.293). Health utilities ranged from 1.000 to − 0.323 and 1.3% of the values were negative. The model was corrected with survey weights to better reflect the representativeness of the sample, but the first two coefficients of the self-care dimension stopped being logically consistent. Differences were found between the Romanian, Hungarian and Polish EQ-5D-5L value sets. Good agreement was noted with the Romanian EQ-5D-3L value set, with a swap between pain/discomfort and mobility in ranking of dimensions.

### Conclusion

A value set for EQ-5D-5L is now available for Romania. This will push one-step further the development of health technology assessment and encourage more health-related quality-of-life research to be conducted locally.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s10198-022-01481-7.

## Introduction

Quality-adjusted life-years (QALYs) are fundamental to Health Technology Assessment (HTA) processes in many countries across the world. Even though much debated in recent years, QALYs are still considered the most rigorous available method to guide healthcare resource allocation decisions \[1\]. QALYs have the benefit of combining both morbidity and mortality into a single measure allowing transparent and consistent comparisons of different interventions across diseases. To estimate QALYs, duration and health utilities are needed. Health utilities reflect people’s preferences for different health states. They are usually determined in studies conducted in the general population using valuation methods such as visual analogue scale (VAS) or time trade-off (TTO) \[2\]. In spite of harmonisation and standardization efforts put into valuation studies, health utilities differ considerably from one country to another \[3\]. These differences have been attributed to differences in either valuation methodologies, sociodemographic backgrounds of respondents, or cultural values \[3\]. Hence, in order for health utilities to be truly informative for economic evaluations and for QALYs to capture the true impact of morbidity in a certain country, health utilities and value sets should be country specific.

One of the most widely used questionnaires to estimate QALYs is the EQ-5D. The EQ-5D \[4\] is a simple to use, short, self-reported instrument that measures a person’s current health in five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression \[5\]. It consists of a 5-item descriptive system and a visual analogue scale (EQ VAS). Currently, two versions of the questionnaire are available: the EQ-5D-3L and the EQ-5D-5L. Differences between the two versions include wording changes (standardization of middle levels to moderate in all dimensions for EQ-5D-5L; new descriptor for the most severe level for mobility for EQ-5D-5L) and a change in the number of severity levels in each dimension (three levels of severity for EQ-5D-3L and five, for the EQ-5D-5L \[6\]). The recall period for EQ-5D-5L is today and each dimension has five response levels: no, slight, moderate, severe, and unable (extreme problems for the pain/discomfort and anxiety/depression dimensions) \[6\]. The EQ-5D-5L was developed in response to EQ-5D-3L’s ceiling effects and reduced sensitivity to small and medium health changes \[6\], and has improved psychometric properties when compared with the EQ-5D-3L version \[7\].

So far, in Romania, the EQ-5D-5L has been used in studies conducted in clinical populations, such as patients with HIV \[8\], obstructive sleep apnoea \[9\], cancer \[10\] or hepatitis C \[11\]. Nevertheless, the preferred instrument to generate QALYs in Romania is the EQ-5D, just like in many other countries \[12\]. Currently, the Romanian HTA process uses a scorecard system \[13\], but local authorities intend to transition to a full HTA process based on cost–utility studies in the near future \[14\]. Unfortunately, to date, no country-specific value set exists for EQ-5D-5L in Romania, and by default, value sets from other countries, more exactly the United Kingdom, have been used \[12\]. Value sets can be culturally sensitive \[15\] and using data from elsewhere to guide healthcare decisions and policies might introduce bias and not represent good value for money on the long run for the Romanian healthcare system \[14\] Therefore, to encourage the use of national priorities and values, the objective of this study was to develop a country-specific value set for EQ-5D-5L in Romania.

## Methods

This study followed the most recent protocol approved by the EuroQoL research foundation \[i.e., the EuroQol Valuation Technique (EQ-VT) version 2.1\] \[16, 17\]. It was developed to allow a parallel estimation of the EQ-5D-3L value set. This manuscript focuses only on the EQ-5D-5L value set, and details on the EQ-5D-3L valuation can be found elsewhere \[18\].

This study was approved by the Bioethics Committee of Medicines and Medical Devices, Romania (194NP/29.10.2018) and by the Faculty of Medical Sciences Research Ethics Committee, part of Newcastle University's Research Ethics Committee, United Kingdom (Application no. 1430/2069/2018). It was registered with the Romanian National Supervisory Authority for the Processing of Personal Data (Application no. 27512/2017; 28,446/2017).

### Study population

The target population was non-institutionalised adults (18 + years) residing in Romania at the time of the study. Participants were selected using a random-walk technique and next birthday rule from 32 settlements that were randomly selected from all regions of Romania using a three-stage probability sampling procedure stratified by region and settlement size. The sample size was estimated at 1794 participants, so that a representative sample at national level could be achieved. For more details, see Olariu et al. \[11, 19\].

### Data collection and quality control process

Interviews were face-to-face, computer-assisted and took place in respondents’ homes from November 2018 to November 2019.

Interviewers were trained by the local study team using standardized training materials in a 2-day face-to-face training session in October 2018. Due to five interviewers abandoning the study team early on in the data collection process, another face-to-face training session was organised in June 2019 to recruit more interviewers. In total, 30 interviewers performed data collection. One interviewer was excluded from the study team due to non-compliance with quality criteria.

The interview had five sections: background questions and the EQ-5D-5L, composite time trade-off (cTTO) valuation tasks (five examples, ten EQ-5D-5L tasks, three EQ-5D-3L tasks), discrete choice experiment tasks (DCE) (seven tasks for EQ-5D-5L), the EQ-5D-3L, and a country-specific questionnaire. This structure of the interview had been used before by the US and Hungarian EQ-5D-5L valuation teams \[20, 21\]. Similar to other data collection tools, the cTTO valuation tasks were developed using 86 EQ-5D-5L health states divided across ten blocks. DCE tasks included 196 pairs of EQ-5D-5L health states, divided across 28 blocks. Each respondent was assigned to one cTTO block and one DCE block \[22\] (for more details, see Olariu et al. \[19\].

Interviews’ quality was checked weekly by the local team and every 2 weeks by the EuroQoL research foundation. Interviewers’ performance and compliance to the study’s protocol and guidelines were assessed using the EQ-VT QC software developed by the EuroQoL research foundation \[23\]. Interviewers were given feedback regarding their performance either by email or by telephone. Interviews were considered of suspect quality if explanations for the wheelchair examples were less than three minutes, if the worse than dead element was not shown in the examples, if the duration of the ten EQ-5D-5L tasks was less than five minutes, and if the worst health state did not have the lowest value or was at least 0.5 lower than the health state with the lowest value \[15, 23\] \[more details here \[19, 23\].

### Data analysis

All analyses were run using STATA 16 and SPSS 24. Continuous variables were summarised using means, 95% confidence intervals and standard deviations. Categorical variables were reported as frequencies and percentages of all observed levels.

### Exclusion criteria

Prior to modelling, the following exclusion criteria were defined for the cTTO data:

1.  Participants whose interviews were performed by interviewers excluded from the interviewers’ team.

2.  Participants whose interviews were performed by interviewers that did not meet the minimum quality criteria as defined by the QC tool.

3.  Participants whose interviews were performed by interviewers that did not conduct enough interviews (20) to achieve a harmonised learning effect between interviewers \[24\].

4.  Participants that did not have any negative values for all cTTO tasks and whose interviews were flagged in the QC report, because the interviewer had not shown the worse than dead element in the example section of the interview.

5.  Participants that had a positive slope on the regression line between their values and the level sum score of the health states valued or gave the same value to all health states or did not trade time.

6.  Participants that flagged all ten EQ-5D-5L health states as incorrect on the feedback module.

7.  Participants with inconsistencies related to the worse health state (55,555) that were not removed after the feedback module.

Additionally, in all models, individual cTTO observations were removed if the respective health state had been flagged by respondents as being incorrect in the feedback module.

Regarding DCE data, participants with suspect patterns in DCE responses were excluded. Suspect patterns in DCE responses were considered those responses that were all the same in all DCE tasks and those that had variations such as ABABABA or BABABAB.

### Model construction

To estimate values for the EQ-5D-5L health states, econometric modelling was used for both cTTO and DCE data. A hybrid modelling approach was used to combine both cTTO and DCE data into a single model \[25\]. The dependent variable for cTTO data was disutility (one minus the cTTO observed values) and health states were used as explanatory variables. For DCE data, the dependent variable was the binary outcome indicating the respondent’s choice for each pair of EQ-5D-5L states.

We only tested main effects models as the EQ-VT design was optimized for such models \[26\]. All our models had 20 parameters: four dummies were created for each EQ-5D-5L dimension and level one was used as reference. Our dummies were regular dummies, indicating the loss in utility from level one to that respective level. All models were initially tested with a constant. If the constant was found non-significant at the level of 0.05, it was then supressed.

For cTTO data, we tested Tobit models to account for the censored nature of the data, multilevel models with random intercepts for interviewer and respondent effects, random coefficient models, and heteroskedastic models.

For DCE data, we used a conditional logit model. As DCE valuations are estimated on a latent scale, to allow direct comparisons, we had to anchor them on a scale from 0 (dead) to 1 (full health) by rescaling them using the theta parameter of the best-fitting hybrid model \[25\].

To make use of all available data, we also tested hybrid models. To test the assumptions of hybrid models, we used scatter plots to plot DCE versus cTTO. If coefficients of the cTTO models were to be proportional to those of DCE models, a line would be observed on the scatter plots. Hence, the assumption of proportionality between DCE and cTTO held true and hybrid models could be estimated \[more details on hybrid modelling here \[27, 28\]\].

### Model selection

We used the following criteria to select our final model:

1.  Logical consistency of parameters: we only considered models for which coefficients of logically worse health states were lower than coefficients of logically better health states.

2.  Significance of parameters and models’ *p* values: we prioritized models that had the maximum number of significant parameters at the level of 0.05 and only considered models that were statistically significant at the level of 0.05.

3.  Theoretical considerations:

    - models that accounted for the heteroskedastic nature of the data were preferred as the observed variance of the cTTO values increases with the severity of health states \[29\].

    - hybrid models were preferred as they maximise the use of all available data by combining both cTTO and DCE data.

    - models that accounted for the censored nature of the data were preferred as by design, the EQ-VT protocol censors observed cTTO values at − 1.

4.  Finally, we considered the value range, the ranking of dimensions based on the size of the coefficient for the worst level on each dimension and the correlation between predicted and observed utilities.

The final model was selected based on the consistency of results, correction of heteroscedasticity, accounting for data censoring, and the degree it used all the available data.

### Sensitivity analysis

We performed a sensitivity analysis to test the robustness of our estimated parameters when no exclusion criteria were applied (when no participant was excluded). We also tested the impact of using survey weights on the final model to correct for the disproportionate allocation to strata of our design and potential differences between the sample and the Romanian general population (see electronic supplementary material Annex 1 for more details on survey weights).

### Comparison with other value sets

We compared the observed cTTO values for Romania with those of Hungary and Poland for the 86 health states that were common to all three studies. We used a *z* test to determine the statistical significance of the differences between the observed means for Romania and Hungary and Poland, respectively.

We compared our final EQ-5D-5L value set with the Romanian EQ-5D-3L value set and the Polish and Hungarian EQ-5D-5L value sets. This was done using density plots to observe range of values, modality, or skewness. We also used Bland–Altman plots to check the agreement between the Romanian EQ-5D-3L and EQ-5D-5L utilities of those health states that are comparable across the EQ-5D-3L and EQ-5D-5L (i.e., the matched 243 states).

For the entire data analysis, we used a significance level of *α* = 0.05. We considered correlations to be very strong if correlation coefficients were \> 0.9 \[30\].

## Results

1674 interviews were performed (for response rates and interviews performed in each settlement see Annex 2 of the electronic supplementary material). Of these 1674 interviews, 1493 were used in the analysis (see electronic supplementary material Annex 3 for all interviews excluded). The interviews included in the analysis were performed by 24 interviewers.

The mean age of included respondents was 48.6 years (SD = 16.2) (weighted sample: 47.5 years, SD = 17.8) and the mean EQ VAS was 82.5 (SD = 15.5) (weighted sample: 81.3, SD = 16.6) with the majority of the sample (52.4%) reporting full health (weighted percentage 49.7%) (see Table <a href="#Tab1" data-ref-type="table">1</a>). Overall, in our sample, there were more women (66%) and more people from urban areas (72.8%) than national average statistics. There were also differences in age and sex with respect to the Romanian general population: men were underrepresented in all age groups and women were overrepresented in age groups from 25 to 74 years (see Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Sociodemographic characteristics of the sample selected for analysis. V6 dataset corresponds to exclusion criteria 1, 2, 3, 4, and 5

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Variable</th>
<th rowspan="2" style="text-align: left;">Category</th>
<th colspan="2" style="text-align: left;">V6 (<em>n</em> = 1493)</th>
<th colspan="2" style="text-align: left;">Weighted V6 (<em>n</em> = 1493)</th>
<th style="text-align: left;">General population</th>
</tr>
<tr>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">985</td>
<td>66.0</td>
<td style="text-align: left;">776</td>
<td>52.0</td>
<td style="text-align: left;">52</td>
</tr>
<tr>
<td style="text-align: left;">Residence area</td>
<td style="text-align: left;">Urban</td>
<td style="text-align: left;">1087</td>
<td>72.8</td>
<td style="text-align: left;">809</td>
<td>54.2</td>
<td style="text-align: left;">55.2</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">Education level</td>
<td style="text-align: left;">No formal education</td>
<td style="text-align: left;">6</td>
<td>0.4</td>
<td style="text-align: left;">11</td>
<td>0.7</td>
<td style="text-align: left;">2</td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">177</td>
<td>11.9</td>
<td style="text-align: left;">232</td>
<td>15.6</td>
<td style="text-align: left;">36.9</td>
</tr>
<tr>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;">747</td>
<td>50.0</td>
<td style="text-align: left;">795</td>
<td>53.3</td>
<td style="text-align: left;">45.2</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: left;">555</td>
<td>37.2</td>
<td style="text-align: left;">447</td>
<td>29.9</td>
<td style="text-align: left;">15.9</td>
</tr>
<tr>
<td style="text-align: left;">No response</td>
<td style="text-align: left;">8</td>
<td>0.5</td>
<td style="text-align: left;">8</td>
<td>0.5</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Occupation</td>
<td style="text-align: left;">Employed</td>
<td style="text-align: left;">893</td>
<td>59.8</td>
<td style="text-align: left;">793</td>
<td>53.1</td>
<td style="text-align: left;">52.1</td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: left;">32</td>
<td>2.1</td>
<td style="text-align: left;">49</td>
<td>3.3</td>
<td style="text-align: left;">3.9</td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: left;">370</td>
<td>24.8</td>
<td style="text-align: left;">396</td>
<td>26.5</td>
<td style="text-align: left;">26.2</td>
</tr>
<tr>
<td style="text-align: left;">Stay at home/domestic</td>
<td style="text-align: left;">105</td>
<td>7.0</td>
<td style="text-align: left;">132</td>
<td>8.9</td>
<td style="text-align: left;">7.1</td>
</tr>
<tr>
<td style="text-align: left;">In education</td>
<td style="text-align: left;">77</td>
<td>5.2</td>
<td style="text-align: left;">97</td>
<td>6.5</td>
<td style="text-align: left;">4.8</td>
</tr>
<tr>
<td style="text-align: left;">No response</td>
<td style="text-align: left;">16</td>
<td>1.1</td>
<td style="text-align: left;">26</td>
<td>1.7</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;">Income</td>
<td style="text-align: left;">Below the average</td>
<td style="text-align: left;">638</td>
<td>42.7</td>
<td style="text-align: left;">703</td>
<td>47.1</td>
<td style="text-align: left;">41.4</td>
</tr>
<tr>
<td style="text-align: left;">Average</td>
<td style="text-align: left;">264</td>
<td>17.7</td>
<td style="text-align: left;">248</td>
<td>16.6</td>
<td style="text-align: left;">30.7</td>
</tr>
<tr>
<td style="text-align: left;">Above the average</td>
<td style="text-align: left;">471</td>
<td>31.5</td>
<td style="text-align: left;">404</td>
<td>27.1</td>
<td style="text-align: left;">27.9</td>
</tr>
<tr>
<td style="text-align: left;">No response</td>
<td style="text-align: left;">120</td>
<td>8.0</td>
<td style="text-align: left;">137</td>
<td>9.2</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Experience with serious illness</td>
<td style="text-align: left;">In self</td>
<td style="text-align: left;">299</td>
<td>20.0</td>
<td style="text-align: left;">314</td>
<td>21.0</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">In family</td>
<td style="text-align: left;">680</td>
<td>45.5</td>
<td style="text-align: left;">662</td>
<td>44.4</td>
<td rowspan="2" style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;">In caring for others</td>
<td style="text-align: left;">246</td>
<td>16.5</td>
<td style="text-align: left;">216</td>
<td>14.5</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Self-rated health using EQ-5D-5L</td>
<td style="text-align: left;">11,111</td>
<td style="text-align: left;">782</td>
<td>52.4</td>
<td style="text-align: left;">743</td>
<td>49.7</td>
<td rowspan="2" style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;">Any other health state</td>
<td style="text-align: left;">711</td>
<td>47.6</td>
<td style="text-align: left;">750</td>
<td>50.3</td>
</tr>
</tbody>
</table>

</div>

<figure id="Fig1">
<p><img src="10198_2022_1481_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Age and sex distribution in the analysed sample compared with the general population in Romania</figcaption>
</figure>

Interviews lasted on average 47 min (SD = 24). Respondents took on average 83.5 s (SD = 116.4) and 50.5 s (SD = 60) to complete one cTTO and DCE task, respectively. 311 (20.8%) participants provided inconsistent responses regarding the values assigned to cTTO tasks. After the feedback module, 64 respondents reconsidered their choices, thus reducing the number of respondents with logical inconsistencies to 247 (16.5%). Subsequently, the use of the feedback module led to the elimination from analysis of 1,152 cTTO values (7.7% of the total cTTO values). There were only 143 values at zero representing 1% of the valid values assigned in the cTTO tasks[^1] and 679 (4.9%) and 146 (1.1%) values at 0.5 and − 0.5, respectively. 12% of the values assigned by respondents to the health states presented in the valid cTTO tasks were negative and of these 15.9% were values of − 1. 70% of the negative values were assigned to the worst health state (55555). Health states 52455 and 43555 had the second and third highest negative values, but the percentages remained low when compared with 55555 (2.7% and 1.9%, respectively) (see Annex 4).

We tested several cTTO and DCE models (see Annex 5 for full list). Table <a href="#Tab2" data-ref-type="table">2</a> presents the results for those models that had the maximum number of significant and consistent parameters, accounted for heteroscedasticity and/or for the censored nature of the data. All parameters for the selected cTTO models were consistent. The conditional logit model generated two inconsistent parameters at the slight and moderate levels of the self-care domain. However, this was resolved when both cTTO and DCE data were combined using hybrid models, with all hybrid models being consistent. The agreement between cTTO and DCE data was very high as shown by the very strong correlations (\> 0.9) between the predictions of the cTTO models and rescaled DCE model (see Fig. <a href="#Fig2" data-ref-type="fig">2</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

Estimation results for selected cTTO, DCE, and hybrid models

</div>

<img src="10198_2022_1481_Tab2_HTML.jpg" id="MO2" />

*IRM* interval regression model, *IRMC* interval regression model censored at – 1, *CLOGIT* conditional logit model, *HMH* hybrid model heteroskedastic without constant, *HMHC* hybrid model heteroskedastic without constant censored at – 1, *MO* mobility; *SC* self-care; *UA* usual activities, *PD* pain discomfort, *AD* anxiety depression, *U* utility, *AIC* Akaike information criteria, *BIC* Bayesian information criterion, *SD* standard deviation, *WTD* worse than dead

\**p* value \< 0.05; values in bold—best performance for the indicator; values in italics—second best performance for the indicator; shaded columns—final model chosen; ≠ theta value 7.410

</div>

<figure id="Fig2">
<p><img src="10198_2022_1481_Fig2_HTML.jpg" id="MO3" /></p>
<figcaption>Scatter plots of composite time trade-off (cTTO) model predictions versus rescaled discrete choice experiment (DCE) model predictions</figcaption>
</figure>

The two cTTO models performed similarly in terms of range of values, ranking of dimensions, and correlation coefficients (see Table <a href="#Tab2" data-ref-type="table">2</a>). The censored model had a slightly higher number of negative values than the uncensored model. In line with our model selection criteria, our preferred cTTO model was the censored interval regression model (IRMC). The two hybrid models that met our selection criteria had almost identical performance in terms of range of values, ranking of dimensions, correlation coefficients, and number of negative health states (see Table <a href="#Tab2" data-ref-type="table">2</a>). Of the two hybrid models, we preferred the censored hybrid model heteroskedastic (HMHC) given the censored nature of the data. Finally, we chose the HMHC model (the Romanian EQ-5D-5L model) over the IRMC model as the hybrid model used all available data in line with our theoretical considerations and aims (see Annex 6 for full details of the model).

### Sensitivity analysis

When our final model was run on the full dataset with no exclusions applied (dataset V1—see Annex 7 for sociodemographic characteristics and Annex 8 for full model), it generated a value set with fewer negative values and a lower range of values (see Table <a href="#Tab3" data-ref-type="table">3</a>). Overall, the performance of the model decreased when interviews that did not meet the quality criteria standards were kept in the sample. When the model was run on the weighted sample (weighted V6 dataset), it generated two inconsistent parameters at the slight and moderate levels of the self-care dimension (see Table <a href="#Tab3" data-ref-type="table">3</a> and Annex 9 for full model).

<div id="Tab3" class="table-wrap">

<div class="caption">

Sensitivity analysis results

</div>

<img src="10198_2022_1481_Tab3_HTML.jpg" id="MO4" />

*MO* mobility, *SC* self-care, *UA* usual activities, *PD* pain discomfort, *AD* anxiety depression, *U* utility, *AIC* Akaike information criteria, *BIC* Bayesian information criterion, *SD* standard deviation, *WTD* worse than dead, *V1* the dataset that includes all interviews performed with the exception of those interviews performed by interviewers that were subsequently excluded from the interviewers’ team due to quality control issues; *V6* the dataset that includes those interviews that were valid after all exclusion criteria have been applied

\**p* value \< 0.05; values in bold—best performance for the indicator; values in italics—second best performance for the indicator; shaded columns—final model chosen

</div>

Finally, we compared the predictions of the final model run on dataset V1 and V6 regarding the mean observed cTTO values and the model performed well in all cases (see Annex 10).

### Comparison with other value sets

First, we compared our observed cTTO values with the observed cTTO values from the Polish and Hungarian valuation studies for all 86 health states that were common to all three studies (see Fig. <a href="#Fig3" data-ref-type="fig">3</a>). We tested the statistical significance between the observed mean differences, and we found that all differences between the observed Romanian and Hungarian cTTO values were statistically significant, with the exception of the differences observed for four health states 11121, 11122, 12111, and 21112. In 91.4% of the cases, the Romanian observed values were higher than the Hungarian observed values with differences ranging from 0.011 to 0.59 (see Annex 11). Regarding the Polish observed values, only 72% of the observed differences were statistically significant: of these, the Romanian observed values were lower than the Polish ones in 61.3% of the cases.

<figure id="Fig3">
<p><img src="10198_2022_1481_Fig3_HTML.jpg" id="MO5" /></p>
<figcaption>Observed composite time trade-off (cTTO) values for the 86 EQ-5D-5L health states common to the Hungarian, Romanian, and Polish EQ-5D-5L valuation studies</figcaption>
</figure>

We then compared all our estimated values with the Hungarian and the Polish EQ-5D-5L value sets. Similar to the observed cTTO values, the Hungarian EQ-5D-5L value set was consistently lower than the Romanian EQ-5D-5L value set. Regarding the Polish EQ-5D-5L value set, the values of the Romanian EQ-5D-5L value set were lower than the Polish ones for mild states, but as severity increased, the Romanian values became higher than the Polish ones (see Fig. <a href="#Fig4" data-ref-type="fig">4</a>). Also, Romanians assigned the highest value to the worst health state (55,555) (− 0.323 versus -0.590 for Poland \[31\] versus − 0.848 for Hungary \[21\] from all the three countries that we compared. Finally, the importance order of the five dimensions of the questionnaire was different from one country to another: Romanians, just like the Polish, placed most weight on the pain/discomfort dimension, whereas Hungarians ranked mobility first. The anxiety/depression dimension came fourth for all three countries (dimension order for Hungary: mobility, pain/discomfort, self-care, anxiety/depression, usual activities; dimension order for Poland: pain/discomfort, mobility, self-care, anxiety/depression, and usual activities).

<figure id="Fig4">
<p><img src="10198_2022_1481_Fig4_HTML.jpg" id="MO6" /></p>
<figcaption>Comparison between the EQ-5D-5L value sets for Hungary, Poland, and Romania</figcaption>
</figure>

Finally, we compared our EQ-5D-5L value set with the Romanian EQ-5D-3L value set \[18\]. The Kernel density plot showed a unimodal right-skewed distribution for the EQ-5D-5L value set, whereas the EQ-5D-3L distribution had a few clusters. More EQ-5D-3L values were concentrated at both ends of the utility scale than in case of the EQ-5D-5L distribution, differences being starker between the two for the left-end of the utility scale (see Fig. <a href="#Fig5" data-ref-type="fig">5</a>a). The Bland–Altman plot (Fig. <a href="#Fig5" data-ref-type="fig">5</a>b) showed a good agreement across the severity scale between the EQ-5D-3L values and the EQ-5D-5L values of the matched health states, with none of the differences falling outside of the ± 2 SD range. The EQ-5D-3L value set had more negative values than the EQ-5D-5L and the importance of dimensions changed slightly: the most important EQ-5D-3L dimension (MO) became second in the case of EQ-5D-5L and the second most important EQ-5D-3L dimension (PD) became first in the case of EQ-5D-5L. The order of the remaining dimensions stayed the same (see Annex 12).

<figure id="Fig5">
<p><img src="10198_2022_1481_Fig5_HTML.jpg" id="MO7" /></p>
<figcaption>Comparison between the Romanian EQ-5D-3L value set and the Romanian EQ-5D-5L value set using a Kernel density plot (<strong>a</strong>) and a Bland–Altman plot (<strong>b</strong>)</figcaption>
</figure>

## Discussion

In this study, we estimated a Romanian value set for the EQ-5D-5L. We did this according to the latest EQ-VT protocol approved by the EuroQoL research foundation and following best practice in the field. We used a main effects model that combined both cTTO and DCE data and accounted for heteroscedasticity and censored data to estimate our value set. This modelling approach reflects best practice and current analytical advances in the field \[17\]. We chose our model from several candidate models based on maximising the number of consistent and significant parameters and theoretical considerations such as heteroscedasticity correction, data censoring, and maximum use of the collected data.

We opted for a censored hybrid model corrected for heteroscedasticity as our final model. We based our decision on the strong \[30\]agreement between the cTTO and DCE data, which supported the use of single estimation \[25\] considering cTTO and DCE responses to be stemming from the same unique utility function \[25\]. The simultaneous use of the two elicitation methods allowed us to get a better picture of the “true” preferences of our respondents, as DCE answers can improve our understanding of cTTO answers \[25\]. Additionally, it improved our precision in estimating the parameters of our model as reflected by the lower standard errors for all coefficients of our final model when compared with the rest of the models. Finally, it allowed us to maximise the use of all available data. Nevertheless, others might question our decision to use a hybrid modelling approach in determining our value set. This is, because, in spite of the benefits of hybrid modelling, to date, there is no agreement on which modelling strategy might be the best in estimating value sets \[31\]: methods that use cTTO data only \[21, 32\], DCE scoring algorithms anchored on TTO data; \[33, 34\] or methods that use both type of data \[31, 35–39\] are consistently reported in the literature. Additionally, some argue that there is not yet available a robust theoretical justification to combine the two elicitation methods as they represent two very distinct valuation methods \[40\].

We compared our EQ-5D-5L value set with the Polish and Hungarian EQ-5D-5L value sets. We chose these two countries as, in our opinion, Central and Eastern European (CEE) countries have a certain degree of similarity in terms of history and culture. Also, they were the only two countries in the region that had, at the time of writing this manuscript, an EQ-5D-5L value set (at that time, Slovenia only had an EQ-5D-3L value set\[41\]). Nevertheless, differences were noted between the three value sets in terms of values assigned to the worst health state and the relative importance of the five EQ-5D-5L dimensions. The anxiety/depression dimension was ranked last but one in all three CEE countries. This is in contrast with other Western European countries where it ranked second \[32, 35\] or even first \[42\]. Greater stigma and lower awareness about mental health problems in Romania and other CEE countries \[43, 44\] might be behind this finding. Finally, modelling approaches in arriving to the final value set differed from one country to another: Hungary used only cTTO data for \[32\] their model and both Poland and Romania used cTTO and DCE data for their final model. Hence, all these differences underline once more the importance of having a national value set for EQ-5D questionnaires.

We did not compare our value set with the English EQ-5D-5L value set in spite of it being the default option used locally in Romania, especially by researchers \[45–47\]. We decided this given the ongoing study to develop a new EQ-5D-5L value set for the UK \[48\] and the criticisim the current EQ-5D-5L value set for England has received \[49\].

Our EQ-5D-5L value set was fairly similar to the EQ-5D-3L value set in terms of range of values, value for the worst health states, and the ranking of the last three dimensions. The EQ-5D-5L value set had fewer negative values than the EQ-5D-3L value set, but this is in line with the other studies’ results that used the same methodology as ours \[21\]. Nevertheless, we recommend the use of the EQ-5D-5L descriptive system in Romania due to its improved psychometric properties \[6\], reserving the EQ-5D-3L for historical cross-country comparisons or clinical trials that might deem its use more appropriate in their clinical population. Regarding the choice between value sets, national value sets should always be preferred, but other factors should also be considered such as the context in which the results might be used, their research application, and the decisions they might influence \[50\].

Our study has several limitations. First, changes in the members of the local study team could have affected how the feedback and second session of training were provided to the team of interviewers in spite of the team’s efforts to standardize them. Also, our team of interviewers changed its members several times throughout the study making it difficult to keep the team small and motivated enough to ensure a low variability in how interviews were performed. Nevertheless, new comers were always trained and interviewer bias should have been reduced through the regular use of the QC tool. Second, our sample differed from the Romanian general population in terms of age, sex, and place of residence: men were underrepresented in all age categories and places of residence (only 29% of the interviewed men lived in rural areas). One reason why men are underrepresented in our sample, especially in rural areas, might be the temporary migration for work that has been booming in Romania in the past 2 decades. The seasonal agricultural market from abroad attracts each year many Romanian rural workers, especially men \[51\]. To see whether these differences had a meaningful impact, we checked whether the observed cTTO values differed according to age, age groups, sex, and place of residence. In line with previous literature \[52, 53\], we found differences between people from rural and urban areas and between different age groups when they valued health states. When stratified by health state or severity, there was no clear pattern of differences in health state values between groups, with significance achieved in less than 30% of the cases when stratified by severity and less than 15% when stratified by health state. Nevertheless, we decided to adjust our final model with survey weights to account for these differences. Unfortunately, most probably due to the added extra complexity, our final model stopped being consistent when survey weights were introduced.

## Conclusion

In this study, we developed a Romanian value set for the EQ-5D-5L using both cTTO and DCE data. The availability of a national value set for the EQ-5D is a landmark event in the development of HTA in Romania and potentially in the CEE region. It will not only encourage the development of a more locally data-driven HTA process, but also promote cross-country comparisons and collaborations in the CEE region.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (XLSX 101 KB)

</div>

<div class="caption">

Supplementary file2 (DOCX 103 KB)

</div>

### Acknowledgements

We would like to thank our interviewers, study participants, and project partners without whom this study could not have been possible. We would also like to thank Aureliano Finch, Bram Roudijk, and all other members from the EuroQoL valuation taskforce that supported us during the data collection and data analysis steps of this study: Arnd J. Prause, Elly Stolk, Gerben Bakker, and Kristina Ludwig. We would also like to thank Juan Manuel Ramos-Goñi for updating the STATA code that allowed the correction of the final hybrid model with survey weights. Finally, we would like to express our appreciation to our funders for making this study possible.

### Author contributions

EO, IGNA, LV, SP, and YO contributed to the design of the study and analysis plan. EO, LV, RC, SP, and YO were involved in planning, organising, and supervising the project. EO, RC, and SP were involved in the data collection process and data quality control checks. EO, IGNA, WM, and RC performed data analysis. EO wrote the first draft of the manuscript. All authors interpreted the results and provided feedback on the final version of the manuscript.

### Funding

This project is the result of the combined efforts of two teams of researchers that applied independently for funding. The development of the EQ-5D-5L value set was funded by the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 748612. It was also funded by the EuroQol Research Foundation (Grant number: 20180030R1). The development of the EQ-5D-3L value set was funded as part of a project run through the Romanian Operational Programme “Administrative Capacity” (POCA 2014–2020).

### Availability of data and materials

The datasets analysed during the current study are available from the corresponding author on reasonable request.

### Declarations

#### Conflicts of interest

None.

#### Ethics approval

This study was approved by the Bioethics Committee of Medicines and Medical Devices, Romania (194NP/29.10.2018) and by the Faculty of Medical Sciences Research Ethics Committee, part of Newcastle University's Research Ethics Committee, United Kingdom (Application no. 1430/2069/2018). It was also registered with the Romanian National Supervisory Authority for the Processing of Personal Data (Application no. 27512/2017; 28446/2017).

## References

1. Pettitt D, Raza S, Naughton B, Roscoe A, Ramakrishnan A, Ali A, Davies B, Dopson S, Hollander G, Smith J, Brindley D. The limitations of QALY: a literature review. J. Stem Cell Res. Ther. 2016. doi:10.4172/2157-7633.1000334

2. Xie F, Gaebel K, Perampaladas K, Doble B, Pullenayegum E. Comparing EQ-5D valuation studies: a systematic review and methodological reporting checklist. Med. Decis. Making. 2014;34(1):8–20. doi:10.1177/0272989X13480852

3. Roudijk B, Donders ART, Stalmeier PFM. Cultural Values group: cultural values: can they explain differences in health utilities between countries?. Med Decis. Making. 2019;39(5):605–616. doi:10.1177/0272989X19841587

4. Group E. EuroQol—a new facility for the measurement of health-related quality of life. Health Policy. 1990;16(3):199–208. doi:10.1016/0168-8510(90)90421-9

5. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

6. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, Bonsel G, Badia X. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual. Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

7. Buchholz I, Janssen MF, Kohlmann T, Feng YS. A Systematic review of studies comparing the measurement properties of the three-level and five-level versions of the EQ-5D. Pharmacoeconomics. 2018;36(6):645–661. doi:10.1007/s40273-018-0642-5

8. Kall M, Fresan U, Guy D, Brown G, Burgui C, Castilla J, Grecu VI, Dumitrescu F, Delpech V, Lazarus JV. Quality of life in people living with HIV in Romania and Spain. BMC Infect. Dis. 2021;21(Suppl 2):898. doi:10.1186/s12879-021-06567-w

9. Zota IM, Sascau RA, Statescu C, Boisteanu D, Roca M, Leon Constantin MM, Vasilcu TF, Gavril RS, Anghel L, Mitu O, Costan V, Cumpat CM, Mitu F. Quality of life in moderate-severe OSA patients from North-Eastern Romania. Rev. Cercetare Interv. Soc. 2020;68:250–260. doi:10.33788/rcis.68.17

10. Efthymiadou O, Mossman J, Kanavos P. Health related quality of life aspects not captured by EQ-5D-5L: Results from an international survey of patients. Health Policy. 2019;123(2):159–165. doi:10.1016/j.healthpol.2018.12.003

11. Cercel I-C, Polli Ș, Streinu-Cercel O, Streinu-Cercel A, Marinescu A, Streinu-Cercel A. Neurocognitive impairment screening in Romanian HCV infected patients. BMC Infect. Dis. 2013;13(S1):10. doi:10.1186/1471-2334-13-s1-o29

12. Rencz F, Gulacsi L, Drummond M, Golicki D, Prevolnik Rupel V, Simon J, Stolk EA, Brodszky V, Baji P, Zavada J, Petrova G, Rotar A, Pentek M. EQ-5D in Central and Eastern Europe: 2000–2015. Qual Life Res. 2016;25(11):2693–2710. doi:10.1007/s11136-016-1375-6

13. Lopert R, Ruiz F, Chalkidou K. Applying rapid 'de-facto' HTA in resource-limited settings: experience from Romania. Health Policy. 2013;112(3):202–208. doi:10.1016/j.healthpol.2013.07.019

14. Lopert, R., Ruiz, F., Gheorghe, A., Chanturidze, T.: Technical Assistance for institution building of Health Technology Assessment structure, including training for the National Agency for Medicines & Medical Devices. Deliverable 1: Situational analysis of Romanian HTA. Contract No: CS/3/24. (2017)

15. Knies S, Evers SM, Candel MJ, Severens JL, Ament AJ. Utilities of the EQ-5D: transferable or not?. Pharmacoeconomics. 2009;27(9):767–779. doi:10.2165/11314120-000000000-00000

16. Oppe M, Devlin NJ, van Hout B, Krabbe PF, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17(4):445–453. doi:10.1016/j.jval.2014.04.002

17. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goni JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation work: version 2 of the EQ-5D-5L valuation protocol. Value Health. 2019;22(1):23–30. doi:10.1016/j.jval.2018.05.010

18. Paveliu MS, Olariu E, Caplescu R, Oluboyede Y, Niculescu-Aron IG, Ernu S, Vale L. Estimating an EQ-5D-3L value set for romania using time trade-off. Int. J. Environ. Res. Public Health. 2021. doi:10.3390/ijerph18147415

19. Olariu E, Paveliu MS, Baican E, Oluboyede Y, Vale L, Niculescu-Aron IG. Measuring health-related quality of life in the general population and Roma communities in Romania: study protocol for two cross-sectional studies. BMJ Open. 2019;9(8):e029067. doi:10.1136/bmjopen-2019-029067

20. Law EH, Pickard AS, Xie F, Walton SM, Lee TA, Schwartz A. Parallel valuation: a direct comparison of EQ-5D-3L and EQ-5D-5L societal value sets. Med. Decis. Making. 2018;38(8):968–982. doi:10.1177/0272989X18802797

21. Rencz F, Brodszky V, Gulacsi L, Golicki D, Ruzsa G, Pickard AS, Law EH, Pentek M. Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time trade-off in Hungary. Value Health. 2020;23(9):1235–1245. doi:10.1016/j.jval.2020.03.019

22. Oppe, M., van Hout, B.: The “power” of eliciting EQ-5D-5L values. In: EuroQoL Working Paper Series (2017)

23. Ramos-Goni JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–473. doi:10.1016/j.jval.2016.10.012

24. Shah K, Mulhern B, Longworth L, Janssen MF. An Empirical study of two alternative comparators for use in time trade-off studies. Value Health. 2016;19(1):53–59. doi:10.1016/j.jval.2015.10.012

25. Ramos-Goni JM, Pinto-Prades JL, Oppe M, Cabases JM, Serrano-Aguilar P, Rivero-Arias O. Valuation and modeling of EQ-5D-5L health states using a hybrid approach. Med. Care. 2017;55(7):e51–e58. doi:10.1097/MLR.0000000000000283

26. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F, Oppe M, Boye KS, Chapman RH, Gong CL, Balch A, Busschbach JJV. United States valuation of EQ-5D-5L health states using an international protocol. Value Health. 2019;22(8):931–941. doi:10.1016/j.jval.2019.02.009

27. Ramos-Goni, J.M., Craig, B., Oppe, M., Van Hout, B.: Combining continuous and dichotomous responses in a hybrid model. In: EuroQol working paper series (16002) (2016)

28. Oppe, M., Ramos-Goni, J.M., van Hout, B.: Modeling EQ-5D-5L valuation data. In: 29th Scientific Plenary Meeting of the EuroQol Group, Rotterdam, The Netherlands 2012, pp. 61–91 (2012)

29. Feng Y, Devlin NJ, Shah KK, Mulhern B, van Hout B. New methods for modelling EQ-5D-5L value sets: an application to English data. Health Econ. 2018;27(1):23–38. doi:10.1002/hec.3560

30. Schober P, Boer C, Schwarte LA. Correlation coefficients: appropriate use and interpretation. Anesth. Analg. 2018;126(5):1763–1768. doi:10.1213/ANE.0000000000002864

31. Golicki D, Jakubczyk M, Graczyk K, Niewada M. Valuation of EQ-5D-5L health states in Poland: the first EQ-VT-based study in Central and Eastern Europe. Pharmacoeconomics. 2019;37(9):1165–1176. doi:10.1007/s40273-019-00811-7

32. Versteegh M, Vermeulen K, Evers S, de Wit GA, Prenger R, Stolk E. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi:10.1016/j.jval.2016.01.003

33. Shiroiwa T, Ikeda S, Noto S, Igarashi A, Fukuda T, Saito S, Shimozuma K. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19(5):648–654. doi:10.1016/j.jval.2016.03.1834

34. Craig BM, Rand K. Choice defines QALYs: A US valuation of the EQ-5D-5L. Med. Care. 2018;56(6):529–536. doi:10.1097/MLR.0000000000000912

35. Ludwig K, Graf von der Schulenburg JM, Greiner W. German Value Set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(6):663–674. doi:10.1007/s40273-018-0615-8

36. Ferreira PL, Antunes P, Ferreira LN, Pereira LN, Ramos-Goni JM. A hybrid modelling approach for eliciting health state preferences: the Portuguese EQ-5D-5L value set. Qual. Life Res. 2019;28(12):3163–3175. doi:10.1007/s11136-019-02226-5

37. Purba FD, Hunfeld JAM, Iskandarsyah A, Fitriana TS, Sadarjoen SS, Ramos-Goni JM, Passchier J, Busschbach JJV. The Indonesian EQ-5D-5L value set. Pharmacoeconomics. 2017;35(11):1153–1165. doi:10.1007/s40273-017-0538-9

38. Andrade LF, Ludwig K, Goni JMR, Oppe M, de Pouvourville G. A French Value Set for the EQ-5D-5L. Pharmacoeconomics. 2020;38(4):413–425. doi:10.1007/s40273-019-00876-4

39. Mai VQ, Sun S, Minh HV, Luo N, Giang KB, Lindholm L, Sahlen KG. An EQ-5D-5L value set for Vietnam. Qual. Life Res. 2020;29(7):1923–1933. doi:10.1007/s11136-020-02469-7

40. Drummond, M., Sculpher, M.J., Claxton, K., Stoddart, G.L., Torrance, G.W.: Measuring and valuing effects: Health gain. In: Methods for the Economic Evaluation Of Health Care Programmes (fourth edition), pp. 123–170. Oxford University Press (2015)

41. Prevolnik Rupel V, Srakar A, Rand K. Valuation of EQ-5D-3l health states in Slovenia: VAS based and TTO based value sets. Zdr Varst. 2020;59(1):8–17. doi:10.2478/sjph-2020-0002

42. Hobbins A, Barry L, Kelleher D, Shah K, Devlin N, Goni JMR, O'Neill C. Utility values for health states in Ireland: a value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(11):1345–1353. doi:10.1007/s40273-018-0690-x

43. Winkler P, Krupchanka D, Roberts T, Kondratova L, Machů V, Höschl C, Sartorius N, Van Voren R, Aizberg O, Bitter I, Cerga-Pashoja A, Deljkovic A, Fanaj N, Germanavicius A, Hinkov H, Hovsepyan A, Ismayilov FN, Ivezic SS, Jarema M, Jordanova V, Kukić S, Makhashvili N, Šarotar BN, Plevachuk O, Smirnova D, Voinescu BI, Vrublevska J, Thornicroft G. A blind spot on the global mental health map: a scoping review of 25 years' development of mental health care for people with severe mental illnesses in central and eastern Europe. Lancet Psychiatry. 2017;4(8):634–642. doi:10.1016/s2215-0366(17)30135-9

44. Stanculescu M, Nitulescu D, Preotesi M, Ciumageanu M, Sfetcu R. Persoanele cu probleme de sănătate mintală din România: Stereotipuri, cauze si modalitati de îngrijire percepute, atitudini si distanta socială [People with mental health problems in Romania: stereotypes, causes and modalities of care, attitudes and social distances]. Calitatea. Vietii. 2008;3–4:286–316.

45. Mogosan C, Stoica V, Mihai C, Ciofu C, Bojinca M, Milicescu M, Crisan V, Mioara B. Trends of rheumatoid arthritis monitorization in Romania. J. Med. Life. 2010;3(3):330–337.

46. De Smedt D, Clays E, Hofer S, Oldridge N, Kotseva K, Maggioni AP, Janssen B, De Bacquer D. Euroaspire Investigators: Validity and reliability of the HeartQoL questionnaire in a large sample of stable coronary patients: the EUROASPIRE IV Study of the European Society of Cardiology. Eur. J. Prev. Cardiol. 2016;23(7):714–721. doi:10.1177/2047487315604837

47. Paveliu MS, Lorenzovici L, Tudose C. Oral anticoagulant treatment with antivitamin K in Romania. A cost-effectiveness analysis of using INR home testing devices. Farmacia. 2018;66(2):358–364.

48. EuroQol Group: New UK EQ-5D-5L Valuation Study (2020). https://euroqol.org/eq-5d-instruments/eq-5d-5l-about/valuation-standard-value-sets/new-uk-eq-5d-5l-valuation-study_blog/. Accessed 06 May 2022

49. Hernandez Alava M, Wailoo A, Grimm S, Pudney S, Gomes M, Sadique Z, Meads D, O'Dwyer J, Barton G, Irvine L. EQ-5D-5L versus EQ-5D-3L: the impact on cost effectiveness in the United Kingdom. Value Health. 2018;21(1):49–56. doi:10.1016/j.jval.2017.09.004

50. Devlin, N., Parkin, D., Janssen, B.: Analysis of EQ-5D Values. In: Methods for Analysing and Reporting EQ-5D Data. pp. 61–86. Springer International Publishing, Cham (2020)33347096

51. Silasi G, Simina OL. Romania and the new economy of migration: costs, decision, networks development. SSRN Electron. J. 2008. doi:10.2139/ssrn.2161488

52. Shaw JW, Johnson JA, Chen S, Levin JR, Coons SJ. Racial/ethnic differences in preferences for the EQ-5D health states: results from the U.S. valuation study. J. Clin. Epidemiol. 2007;60(5):479–490. doi:10.1016/j.jclinepi.2006.08.008

53. Sayah FA, Bansback N, Bryan S, Ohinmaa A, Poissant L, Pullenayegum E, Xie F, Johnson JA. Determinants of time trade-off valuations for EQ-5D-5L health states: data from the Canadian EQ-5D-5L valuation study. Qual. Life Res. 2016;25(7):1679–1685. doi:10.1007/s11136-015-1203-4

[^1]: Valid cTTO values—values assigned to health states that were not marked as being incorrect by the respondent on the feedback module.

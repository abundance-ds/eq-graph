---
project_id: "341-RA"
work_id: "doi:10.1186/s12955-024-02266-7"
doi: "10.1186/s12955-024-02266-7"
pmid: "38956543"
pmcid: "PMC11218064"
title: "The EQ-5D-5L valuation study for Trinidad and Tobago"
journal: "Health and Quality of Life Outcomes"
publication_date: "2024-07-02"
volume: "22"
authors:
  - name: "Henry Bailey"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Marcel F Jonker"
    affiliation_ids:
      - "Aff3"
      - "Aff4"
      - "Aff5"
  - name: "Eleanor Pullenayegum"
    affiliation_ids:
      - "Aff6"
  - name: "Fanni Rencz"
    affiliation_ids:
      - "Aff7"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff8"
      - "Aff9"
affiliations:
  - id: "Aff1"
    name: "Department of Economics, The University of the West Indies, St Augustine Campus, St Augustine, Trinidad and Tobago"
  - id: "Aff2"
    name: "HEU, Centre for Health Economics, The University of the West Indies, St Augustine Campus, St Augustine, Trinidad and Tobago"
  - id: "Aff3"
    name: "Erasmus School of Health Policy & Management, Erasmus University Rotterdam, Rotterdam, the Netherlands"
  - id: "Aff4"
    name: "Erasmus Centre for Health Economics Rotterdam, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff5"
    name: "Erasmus Choice Modelling Centre, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff6"
    name: "Child Health Evaluative Sciences, The Hospital for Sick Children; Dalla Lana School of Public Health, University of Toronto, Toronto, Canada"
  - id: "Aff7"
    name: "Department of Health Policy, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff8"
    name: "EuroQol Research Foundation, Rotterdam, the Netherlands"
  - id: "Aff9"
    name: "Department of Psychiatry, Erasmus University Medical Center, Rotterdam, the Netherlands"
licence: "cc-by"
source_file: "input/projects/341-RA/papers/doi_10.1186_s12955-024-02266-7.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11218064/fullTextXML"
source_method: "epmc_xml"
source_sha256: "ec2dae9b852f0e2fd38c042c76d355207d7d9e0c9723e5d0d5640daee1b816f5"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The EQ-5D-5L valuation study for Trinidad and Tobago

## Abstract

### Purpose

The 2016 EQ-5D-3L value set for Trinidad and Tobago (T&T) allows for the calculation of EQ-5D-5L values via the crosswalk algorithm. The 2016 value set was based on methods predating the EQ-VT protocol, now considered the gold standard for developing EQ-5D value sets. Furthermore, direct elicitation of EQ-5D-5L is preferred over crosswalked values. This study aimed to produce an EQ-5D-5L value set for T&T.

### Methods

A representative sample (age, sex, geography) of adults each completed 10 composite Time Trade-Off (cTTO) tasks and 12 Discrete Choice Experiment (DCE) tasks in face-to-face interviews. The cTTO data were analyzed using a Tobit model that corrects for heteroskedasticity. DCE data were analyzed using a mixed logit model. The cTTO and DCE data were combined in hybrid models.

### Results

One thousand and seventy-nine adults completed the valuation interviews. Among the modelling approaches that were explored, the hybrid heteroskedastic Tobit model produced all internally consistent, statistically significant coefficients, and performed best in terms of out-of-sample predictivity for single states. Compared to the existing EQ-5D-5L crosswalk set, the new value set had a higher number of negative values (236 or 7.6% versus 21 or 0.7%). The mean absolute difference was 0.157 and the correlation coefficient between the two sets was 0.879.

### Conclusion

This study provides a value set for the EQ-5D-5L for T&T using the EQ-VT protocol. We recommend this value set for QALY computations relating to T&T.

**Keywords:** EQ-5D-5L, Trinidad and Tobago, EQ-VT, QALY

Received 2023 Dec 22; Accepted 2024 Jun 4; Collection date 2024.

## Introduction

The EQ-5D-5L instrument is a health classification system that is used for health outcomes measurement in developed, and now increasingly also in developing countries \[1\]. EQ-5D-5L has many uses in healthcare and health economics including its use as the adjustment for Quality Adjusted Life Years (QALYs), for cost utility analysis and in quantifying burden of illness. EQ-5D-5L comprises 5 dimensions in order: mobility, self-care, usual activities, pain/discomfort and anxiety/depression, on each of which a respondent can indicate problems at one of 5 levels: no, slight, moderate, severe or extreme problems/unable to. With 5 dimensions in 5 levels, there are 5<sup>5</sup> = 3,125 possible states of health that can be described using the classification system. Each of these health states can be presented as a five-digit string. For example, if a respondent indicates he/she has moderate problems (level 3) with walking about, slight problems (level 2) with self care, no problems (level 1) with usual activities, severe (level 4) pain/discomfort and is extremely (level 5) anxious or depressed, the health state can be coded as state “32145”, representing the level of problems on each dimension, in order of appearance. In an EQ-5D-5L valuation study, a societal value is obtained for each EQ-5D-5L state relative to all other EQ-5D-5L states \[2\]. This is known as the index value for the state and the collection of all 3,125 index values for a population is known as a value set. Different countries will have different EQ-5D-5L value sets as the preferences among states of health are known to be driven by many factors, including factors relating to national culture \[3\].

The original EQ-5D instrument (EQ-5D-3L) had 3 levels \[4\]. This was similar to EQ-5D-5L but without the two intermediate levels: slight and severe and using ‘confined to bed’ instead of ‘unable to walk about’ for the highest level of problems with mobility. An EQ-5D-3L valuation study was undertaken for Trinidad and Tobago in 2016 \[5\]. This has been used to produce a set of EQ-5D-3L population norms for Trinidad and Tobago and in several applications \[6–8\]. EQ-5D-5L was introduced to increase the sensitivity of the instrument \[9\]. A crosswalk EQ-5D-5L value set was developed for Trinidad and Tobago based on the EQ-5D-3L value set \[10\]. The Trinidad and Tobago crosswalk value set has been used in several applications in Trinidad and Tobago \[11–15\] and the Trinidad and Tobago EQ-5D-5L crosswalk value set has also been used in other countries in the Caribbean region \[16–18\]. While an EQ-5D-5L crosswalk value set is known to be more sensitive than EQ-5D-3L, a directly elicited EQ-5D-5L value set is preferred over a crosswalk. Directly elicited value sets are not subject to the assumptions underlying mapped value sets, for example the Van Hout et al. crosswalk algorithm was based mostly on responses from European respondents which may not necessarily be representative for countries with different cultures \[10\].

Given the growing role that EQ-5D health outcomes plays in clinical practice and disease studies, and the potential that it offers for policy work in Trinidad and Tobago and the wider Caribbean, a decision was made to develop a directly elicited EQ-5D-5L value set for Trinidad and Tobago. The EuroQol Group has developed and published a standardized protocol for EQ-5D-5L valuation studies known as EQ-VT \[19\]. This study reports the application of EQ-VT in Trinidad and Tobago. The goal of the study was to develop a value set for the EQ-5D-5L, by directly assessing the preferences for EQ-5D-5L health states in the population of Trinidad and Tobago.

## Methods

This study followed the EQ-VT protocol, version 2.1 \[19\]. Computer-assisted personal interviews were utilized in which respondents completed Composite Time Trade Off (cTTO) and Discrete Choice Experiment (DCE) tasks. These data were subsequently modelled to derive a national EQ-5D-5L value set for Trinidad and Tobago. This value set was then compared against the existing Trinidad and Tobago EQ-5D-5L crosswalk value set that was based on the EQ-5D-3L value set. We followed the CREATE checklist for reporting Valuation Studies of Multi-Attribute Utility-Based Instruments \[20\].

### Valuation methods

The cTTO combines the traditional Time Trade Off (TTO) method for health states considered better than dead (BTD), and lead-time TTO (LT-TTO) for states that respondents consider to be worse than dead (WTD) \[21\]. Both methods follow an iterative procedure in which respondents choose between living in two different hypothetical lives. In the TTO, Life A is described as living for a number of life years in full health, and Life B being 10 years in some EQ-5D-5L health state. Depending on the choice made by the respondent, the number of years in full health in Life A is subsequently varied, until the respondent is indifferent between the two lives, and a value can be inferred for the health state of Life B. The LT-TTO is invoked when respondents indicate that they consider a health state to be WTD, and follows a similar iterative procedure, except that the 10 years in Life B are now preceeded by 10 years in full health. Further details can be found elsewhere \[19, 21\].

In the DCE task, respondents were asked to choose which of two different EQ-5D-5L health states they prefer, without any duration of time spent in these health states specified. In contrast to the iterative cTTO method, which produces cardinal values, the DCE task encompasses a single choice, which produces binary outcomes, from which no direct value for a health state can be inferred.

### Interview procedures

Respondents were interviewed in computer-assisted personal interviews, following the standardized EQ-VT interview protocol and interviewer script. First, respondents were presented with information about the aims and the content of the study, and completed an informed consent form. Subsequently, respondents completed a warm-up exercise, which included some demographic questions, a self-completion EQ-5D-5L questionnaire and accompanying EuroQol Visual Analogue scale (EQ VAS). After that, the cTTO task was introduced. Respondents were first presented with an example task in which they valued the health state “being in a wheelchair”. Here, the task was explained to the respondents after which they completed the example question. This was followed by another example question: “a health state much better than being in a wheelchair” or “a health state much worse than being in a wheelchair”, depending on whether the respondent considered “being in a wheelchair” as BTD or WTD. This was followed by another 3 practice questions, using EQ-5D-5L health states (states 21121, 35554 and 15411, representing mild, severe and potentially difficult to imagine health states, respectively). Subsequently, respondents valued 10 EQ-5D-5L health states using the cTTO task. After completing the cTTO tasks, respondents were shown the feedback module: a rank order of their answers, after which they could indicate whether any of the responses were in the wrong order \[22\]. Lastly, respondents were presented with a set of 12 DCE choice pairs, followed by a short demographic survey (with the remaining demographic questions) after which they were thanked for their participation and invited to choose a gift valued at 60 Trinidad and Tobago dollars (about \$9 USD) from range of options including gift vouchers, tote bags, water bottles etc. as compensation for their time.

### Selection of health states

For the cTTO task, the standard EQ-VT health state design was used comprising 86 health states distributed over 10 blocks of 10 health states. Each block consisted of one mild health state (one of the following: 21111, 12111, 11211, 11121 and 11112), the worst health state 55555 and a set of 8 states chosen from an efficient design comprising 80 health states \[23\]. For the DCE tasks, respondents were allocated a block of 12 choice pairs out of 20 unique blocks from a Bayesian efficient design using priors from a set of 19 different EQ-5D-5L valuation studies. The design is described in <a href="#Sec28" data-ref-type="sec">Appendix C</a>. Each respondent was randomly allocated a block of cTTO states and DCE choice pairs.

### Quality control

The EQ-VT quality control (QC) procedures were implemented to ensure adequate data quality. We followed the Ramos-Goñi et al. protocol in which interviews were flagged as potentially non-compliant to the interview protocol if at least one of the following conditions was met: 1) the interviewer did not explain the WTD part of the cTTO task in at least one of the wheelchair practice tasks, 2) the interviewer spent less than 3 min on the two wheelchair tasks, 3) the respondent completed the main 10 cTTO tasks in less than 5 min, and 4) state 55555 did not receive the lowest value and another state received a value that was at least 0.5 lower \[24\]. Data were collected in batches of 10 interviews, after which the data were examined, and the number of interviews that were flagged per interviewer. If more than 40% of interviews were flagged during a single round of interviews, the interviewer failed the QC, their batch of data was removed and the interviewer was retrained. If an interviewer failed the QC twice, the interviewer was removed from the study.

### Sampling

A nationally representative sample of 1000 respondents aged 18 years and over was targeted. Quota sampling was performed based on age and sex, as well as the 14 administrative regions of Trinidad and the combined 7 parishes of Tobago based on the 2011 Population and Housing Census for Trinidad and Tobago (Central Statistical Office (CSO) of Trinidad and Tobago) which was the most recent census data available for Trinidad and Tobago. Streets were randomly selected from the CSO maps and 1 in every 4 households were visited on each selected street. One member of each household was selected using the most recent birthday method and invited to take part in the survey. The respondents were recruited by a local market research company. A team of 14 interviewers, employed by the market research company, was trained during a 1-week training session by two members of the research team (HB and BR). Subsequently, each interviewer completed at least two sets of 5 pilot interviews. Four interviewers failed the QC procedures during the pilot phase or thereafter, and were removed from the study. A team of 10 remaining interviewers completed the data collection. Furthermore, interviewer effects were monitored by assessing whether the interviewers produced roughly similar distributions of values. The data were collected between July and September 2022.

### Analyses

Several 20-parameter models, with each parameter representing the difference between having no problems and having a certain level of problems on a particular dimension, were estimated on the data. The cTTO and DCE data were modelled in isolation as well as jointly. Details on the functional form of these models can be found in <a href="#Sec20" data-ref-type="sec">Appendix B</a>.

We first estimated a random intercept model on the cTTO data to account for the nested structure of the cTTO data (respondents each complete multiple cTTO tasks) and a random left-censored intercept Tobit model (to account for the nesting of the data as well as the fact that respondents cannot assign values lower than -1 to any health state). Furthermore, we estimated models that corrected for the heteroskedastic nature of the cTTO data, with and without the Tobit link to account for the censored nature of the data. The regression constant was suppressed in cases where it was not significant.

The DCE data were analyzed using conditional logit and mixed logit models with the latter accounting for preference heterogeneity. Furthermore, hybrid models were estimated which used a joint likelihood function to model the cTTO and DCE data in combination \[25\]. Hybrid models were estimated taking into account the heteroskedastic nature of the data, as well as the using the Tobit link for the cTTO data. Each model that corrects for heteroskedasticity in the cTTO data, as well as the hybrid models were estimated without a constant when the constant was not significant. Lastly, sensitivity analyses were carried out by estimating the cTTO and hybrid models while leaving out the responses flagged in the feedback module. A final model was selected based on the properties of the model, such as whether heteroskedasticity was present and whether there was a substantial number of censored responses. Furthermore, model fit and predictivity was considered using mean absolute error (MAE). MAE was calculated over all responses as well as how well the models predicted the mean observed cTTO value for the 86 health states included in the cTTO health state design. Lastly, out-of-sample predictivity was tested using a leave-one-out analysis, in which models were estimated by leaving out a single state, predicting its value and evaluating the MAE of the model. The same procedure was used by leaving out a block of health states rather than a single health state. Data analyses were performed in Stata 18, using the xtreg, xttobit, intreg, clogit, mixlogit and hyreg commands.

## Results

### Demographics

A representative sample (age, sex, geography) of 1,079 adults completed the EQ-VT valuation tasks in face-to-face interviews. The response rate was 34%. Table <a href="#Tab1" data-ref-type="table">1</a> shows a breakdown of the age and sex distribution of the sample compared with the population over age 18, and Table <a href="#Tab2" data-ref-type="table">2</a> shows the geographic composition of the sample compared with the population. All comparisons were done against the 2011 census data.

<div id="Tab1" class="table-wrap">

<div class="caption">

Age and sex composition of the sample compared with the population

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Age group</th>
<th colspan="2" style="text-align: left;">Sample</th>
<th colspan="2" style="text-align: left;">Population</th>
</tr>
<tr>
<th style="text-align: left;"><strong>Male</strong></th>
<th style="text-align: left;"><strong>Female</strong></th>
<th style="text-align: left;"><strong>Male</strong></th>
<th style="text-align: left;"><strong>Female</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>18–24</strong></td>
<td style="text-align: left;">7.7%</td>
<td style="text-align: left;">7.4%</td>
<td style="text-align: left;">7.7%</td>
<td style="text-align: left;">7.7%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>25–34</strong></td>
<td style="text-align: left;">10.4%</td>
<td style="text-align: left;">11.3%</td>
<td style="text-align: left;">11.6%</td>
<td style="text-align: left;">11.4%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>35–44</strong></td>
<td style="text-align: left;">9.5%</td>
<td style="text-align: left;">10.9%</td>
<td style="text-align: left;">9.1%</td>
<td style="text-align: left;">8.9%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>45–54</strong></td>
<td style="text-align: left;">6.3%</td>
<td style="text-align: left;">8.2%</td>
<td style="text-align: left;">9.3%</td>
<td style="text-align: left;">9.1%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>55–64</strong></td>
<td style="text-align: left;">6.0%</td>
<td style="text-align: left;">10.2%</td>
<td style="text-align: left;">6.7%</td>
<td style="text-align: left;">6.6%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>65 + </strong></td>
<td style="text-align: left;">5.5%</td>
<td style="text-align: left;">6.7%</td>
<td style="text-align: left;">5.4%</td>
<td style="text-align: left;">6.4%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Total</strong></td>
<td style="text-align: left;">45.3%</td>
<td style="text-align: left;">54.7%</td>
<td style="text-align: left;">49.8%</td>
<td style="text-align: left;">50.2%</td>
</tr>
</tbody>
</table>

</div>

<div id="Tab2" class="table-wrap">

<div class="caption">

The geographic composition of the sample compared with the population

</div>

| Region                      | Sample | Population |
|-----------------------------|--------|------------|
| Arima                       | 1.6%   | 2.7%       |
| Chaguanas                   | 3.2%   | 6.5%       |
| Couva / Tabaquite / Talparo | 16.6%  | 12.6%      |
| Diego Martin                | 8.4%   | 8.2%       |
| Mayaro / Rio Claro          | 2.9%   | 2.6%       |
| Penal / Debe                | 4.2%   | 6.5%       |
| Pt Fortin                   | 1.7%   | 1.8%       |
| Port of Spain               | 3.9%   | 3.8%       |
| Princes Town                | 7.5%   | 7.1%       |
| San Fernando                | 5.4%   | 4.4%       |
| San Juan / Laventille       | 13.7%  | 12.2%      |
| Sangre Grande               | 5.4%   | 5.0%       |
| Siparia                     | 6.8%   | 6.3%       |
| Tobago                      | 5.8%   | 4.8%       |
| Tunapuna / Piarco           | 13.2%  | 15.8%      |
| Total                       | 100.0% | 100.0%     |

</div>

Ethnicity in the sample generally reflected the 2011 census data for the population aged 18 + with Afro- ethnicity slightly under-represented, and mixed/other slightly over-represented. Table <a href="#Tab3" data-ref-type="table">3</a> shows that the sample appeared to be more educated than the 2011 census data with 24.8% of the sample being tertiary/university educated versus 11.5%.

<div id="Tab3" class="table-wrap">

<div class="caption">

Ethnicity and education of the sample compared with population data (aged 18 +) from the 2011 Population and Housing Census for Trinidad and Tobago

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">2022 Sample</th>
<th style="text-align: left;">2011 Census</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: left;">Ethnicity</td>
</tr>
<tr>
<td style="text-align: left;"> Afro-</td>
<td style="text-align: left;">34.2%</td>
<td style="text-align: left;">37.1%</td>
</tr>
<tr>
<td style="text-align: left;"> Indo-</td>
<td style="text-align: left;">40.6%</td>
<td style="text-align: left;">40.0%</td>
</tr>
<tr>
<td style="text-align: left;"> Mixed/Other</td>
<td style="text-align: left;">25.2%</td>
<td style="text-align: left;">22.9%</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Education</td>
</tr>
<tr>
<td style="text-align: left;"> Less than complete secondary</td>
<td style="text-align: left;">18.9%</td>
<td style="text-align: left;">28.8%</td>
</tr>
<tr>
<td style="text-align: left;"> Complete secondary</td>
<td style="text-align: left;">43.5%</td>
<td style="text-align: left;">51.5%</td>
</tr>
<tr>
<td style="text-align: left;"> Vocational</td>
<td style="text-align: left;">12.9%</td>
<td style="text-align: left;">8.2%</td>
</tr>
<tr>
<td style="text-align: left;"> Tertiary / University</td>
<td style="text-align: left;">24.8%</td>
<td style="text-align: left;">11.5%</td>
</tr>
</tbody>
</table>

</div>

### Valuation results

Each of the 1079 respondents completed 10 TTO tasks and 12 DCE tasks, giving a total of 10,790 TTO tasks and 12,948 DCE tasks. The average completion time was 43 min and 7 s (standard deviation 18 min and 10 s). In the QC process 164 interviews (15%) were flagged. In all, 63 interviews were flagged for not explaining the WTD task, 18 for inconsistencies with state 55555, 45 for not spending enough time on the wheelchair examples, and 50 for not spending enough time on the cTTO tasks. There were 2 non-traders (assigning the full health value to all states) in the sample. Figure <a href="#Fig1" data-ref-type="fig">1</a> shows the distribution of responses in the cTTO task.

<figure id="Fig1">
<p><img src="12955_2024_2266_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="12955_2024_2266_Fig1_HTML.gif" /></p>
<figcaption>Responses to the cTTO task</figcaption>
</figure>

There was some clustering of responses at 1, 0.5 and -1, and 19.27% of responses were negative. There were some differences in the proportion of responses at 1, 0.5 and -1, between interviewers, suggesting that there may have been some minor interviewer effects. The proportion of responses equalling zero was 3.05%, while 6.33% of responses were at -1, indicating the share of potentially censored data. A Breusch-Pagan test showed that there was heteroskedasticity present in the modelled data. Because of the presence of heteroskedasticity and a relatively large share of potentially censored observations at -1, only models correcting for heteroskedasticity and accounting for censoring in the cTTO data were considered, as well as DCE-only models. Table <a href="#Tab4" data-ref-type="table">4</a> shows the estimated coefficients of selected cTTO-only, DCE-only and hybrid models. Other models are reported in <a href="#Sec18" data-ref-type="sec">Appendix A</a>, Tables 5, 6 and 7.

<div id="Tab4" class="table-wrap">

<div class="caption">

Modelling results of the best performing models for cTTO-only, DCE-only and hybrid

</div>

<table>
<thead>
<tr>
<th colspan="3" style="text-align: left;"><strong>Heteroskedastic Tobit (cTTO only)</strong></th>
<th colspan="3" style="text-align: left;"><strong>Mixed logit (DCE only)</strong></th>
<th colspan="2" style="text-align: left;"><strong>Hybrid heteroskedastic Tobit (value set)</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>coefficients</strong></th>
<th style="text-align: left;"><strong>Beta</strong></th>
<th style="text-align: left;"><strong>SE</strong></th>
<th style="text-align: left;"><strong>Mean Beta</strong></th>
<th style="text-align: left;"><strong>SE</strong></th>
<th style="text-align: left;"><strong>Beta</strong><sup><strong>a</strong></sup></th>
<th style="text-align: left;"><strong>Beta</strong></th>
<th style="text-align: left;"><strong>SE</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>mo2</strong></td>
<td style="text-align: left;"><strong>0.014</strong></td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;"><strong>0.745**</strong></td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;"><strong>0.048</strong></td>
<td style="text-align: left;"><strong>0.027</strong></td>
<td style="text-align: left;">0.005</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo3</strong></td>
<td style="text-align: left;"><strong>0.058</strong></td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"><strong>1.509**</strong></td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;"><strong>0.097</strong></td>
<td style="text-align: left;"><strong>0.085</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo4</strong></td>
<td style="text-align: left;"><strong>0.162</strong></td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;"><strong>3.165**</strong></td>
<td style="text-align: left;">0.179</td>
<td style="text-align: left;"><strong>0.203</strong></td>
<td style="text-align: left;"><strong>0.187</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo5</strong></td>
<td style="text-align: left;"><strong>0.357</strong></td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;"><strong>5.701**</strong></td>
<td style="text-align: left;">0.298</td>
<td style="text-align: left;"><strong>0.365</strong></td>
<td style="text-align: left;"><strong>0.368</strong></td>
<td style="text-align: left;">0.007</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc2</strong></td>
<td style="text-align: left;"><strong>0.029</strong></td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;"><strong>0.473**</strong></td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;"><strong>0.030</strong></td>
<td style="text-align: left;"><strong>0.024</strong></td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc3</strong></td>
<td style="text-align: left;"><strong>0.074</strong></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"><strong>1.236**</strong></td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;"><strong>0.079</strong></td>
<td style="text-align: left;"><strong>0.072</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc4</strong></td>
<td style="text-align: left;"><strong>0.159</strong></td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"><strong>2.427**</strong></td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;"><strong>0.156</strong></td>
<td style="text-align: left;"><strong>0.150</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc5</strong></td>
<td style="text-align: left;"><strong>0.221</strong></td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"><strong>3.773**</strong></td>
<td style="text-align: left;">0.197</td>
<td style="text-align: left;"><strong>0.242</strong></td>
<td style="text-align: left;"><strong>0.232</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua2</strong></td>
<td style="text-align: left;"><strong>0.016</strong></td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;"><strong>0.173</strong></td>
<td style="text-align: left;">0.108</td>
<td style="text-align: left;"><strong>0.011</strong></td>
<td style="text-align: left;"><strong>0.011</strong></td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua3</strong></td>
<td style="text-align: left;"><strong>0.087</strong></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"><strong>0.961**</strong></td>
<td style="text-align: left;">0.117</td>
<td style="text-align: left;"><strong>0.062</strong></td>
<td style="text-align: left;"><strong>0.065</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua4</strong></td>
<td style="text-align: left;"><strong>0.145</strong></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"><strong>2.152**</strong></td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;"><strong>0.138</strong></td>
<td style="text-align: left;"><strong>0.146</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua5</strong></td>
<td style="text-align: left;"><strong>0.216</strong></td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"><strong>3.186**</strong></td>
<td style="text-align: left;">0.176</td>
<td style="text-align: left;"><strong>0.204</strong></td>
<td style="text-align: left;"><strong>0.219</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd2</strong></td>
<td style="text-align: left;"><strong>0.026</strong></td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;"><strong>1.259**</strong></td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;"><strong>0.081</strong></td>
<td style="text-align: left;"><strong>0.044</strong></td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd3</strong></td>
<td style="text-align: left;"><strong>0.102</strong></td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"><strong>2.373**</strong></td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;"><strong>0.152</strong></td>
<td style="text-align: left;"><strong>0.128</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd4</strong></td>
<td style="text-align: left;"><strong>0.316</strong></td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"><strong>5.031**</strong></td>
<td style="text-align: left;">0.238</td>
<td style="text-align: left;"><strong>0.322</strong></td>
<td style="text-align: left;"><strong>0.311</strong></td>
<td style="text-align: left;">0.007</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd5</strong></td>
<td style="text-align: left;"><strong>0.541</strong></td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;"><strong>7.730**</strong></td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;"><strong>0.495</strong></td>
<td style="text-align: left;"><strong>0.480</strong></td>
<td style="text-align: left;">0.008</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad2</strong></td>
<td style="text-align: left;"><strong>0.024</strong></td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;"><strong>0.263*</strong></td>
<td style="text-align: left;">0.119</td>
<td style="text-align: left;"><strong>0.017</strong></td>
<td style="text-align: left;"><strong>0.020</strong></td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad3</strong></td>
<td style="text-align: left;"><strong>0.057</strong></td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"><strong>1.237**</strong></td>
<td style="text-align: left;">0.137</td>
<td style="text-align: left;"><strong>0.079</strong></td>
<td style="text-align: left;"><strong>0.074</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad4</strong></td>
<td style="text-align: left;"><strong>0.168</strong></td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"><strong>2.436**</strong></td>
<td style="text-align: left;">0.192</td>
<td style="text-align: left;"><strong>0.156</strong></td>
<td style="text-align: left;"><strong>0.161</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad5</strong></td>
<td style="text-align: left;"><strong>0.272</strong></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;"><strong>3.988**</strong></td>
<td style="text-align: left;">0.246</td>
<td style="text-align: left;"><strong>0.256</strong></td>
<td style="text-align: left;"><strong>0.264</strong></td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE (total)</strong></td>
<td style="text-align: left;"><strong>0.295</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>N/A</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>0.303</strong></td>
<td style="text-align: left;"><strong>0.297</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE(86 states)</strong></td>
<td style="text-align: left;"><strong>0.043</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>N/A</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>0.053</strong></td>
<td style="text-align: left;"><strong>0.044</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE out of sample (state)</strong></td>
<td style="text-align: left;"><strong>0.056</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>N/A</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>N/A</strong></td>
<td style="text-align: left;"><strong>0.049</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAEout of sample (block)</strong></td>
<td style="text-align: left;"><strong>0.042</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>N/A</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>N/A</strong></td>
<td style="text-align: left;"><strong>0.050</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>v(55555)</strong></td>
<td style="text-align: left;"><strong>-0.607</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>24.38</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>-0.563</strong></td>
<td style="text-align: left;"><strong>-0.563</strong></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

Rows mo2-ad5 indicate the decrements associated to specific level-dimension combinations, with for example ua4 representing level 4 problems with usual activities

*AIC* Akaike Information Criterion, *BIC* Bayesian Information Criterion, *MAE* Mean Absolute Error

<sup>a</sup>The estimated mean betas for the mixed logit model were rescaled using the scale length for the hybrid heteroskedastic model. Rescaling factor: 0.0641

\*indicates *p*\<0.05

\*\*indicates *p*\<0.01

</div>

In all models pain/discomfort received the highest weight followed by mobility, anxiety/depression, self-care and lastly, usual activities. The value for the worst health state, state 55555, ranged between -0.563 (hybrid heteroskedastic Tobit) and -0.607 (heteroskedastic Tobit model), although other Tobit models, which did not correct for heteroskedasticity, produced lower values (see <a href="#Sec18" data-ref-type="sec">Appendix A</a>). The difference between the CTTO-only heteroskedastic Tobit model and the hybrid heteroskedastic Tobit model was small in terms of fit statistics such as the MAE. In terms of out-of-sample predictivity, the hybrid heteroskedastic Tobit model performed better than the cTTO-only heteroskedastic Tobit model on removing a single state from the design, while the cTTO-only heteroskedastic Tobit model performed better on removing a whole block. Robustness on out-of-sample predictivity for single states was considered more important, and therefore, the hybrid heteroskedastic Tobit model was selected as the final model, to be used as the value set for Trinidad and Tobago. The value set then takes the following form:

``` math
\begin{matrix}
{2)} & {U = 1 - 0.027MO2 - 0.085MO3 - 0.187MO4 - 0.368MO5 - 0.024SC2 - 0.072SC3 - 0.150SC4 - 0.232SC5 - 0.011UA2 - 0.065UA3 - 0.146UA4 - 0.219UA5 - 0.044PD2 - 0.128PD3 - 0.311PD4 - 0.480PD5 - 0.020AD2 - 0.074AD3 - 0.161AD4 - 0.264AD5}
\end{matrix}
```

This means that for example health state 21354 would receive the following value: $`U(21354) = 1 - 0.027MO2 - 0.065UA3 - 0.480PD5 - 0.161AD4 = 0.267`$.

Figure <a href="#Fig2" data-ref-type="fig">2</a> shows a Bland–Altman plot for the existing EQ-5D-5L crosswalk value set and the EQ-VT value set. The EQ-VT produces lower values on average (mean EQ-VT 0.386, while this is 0.524 in the crosswalk). The EQ-VT value set had a higher number of negative values (275 states or 8.8% versus 21 states or 0.7%). The mean absolute difference between the value set and the crosswalk set was 0.157 and the correlation coefficient between the two sets was 0.879. The EQ-VT value set had a wider range (-0.563 to 1.000) than the crosswalk set (-0.163 to 1.000).

<figure id="Fig2">
<p><img src="12955_2024_2266_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="12955_2024_2266_Fig2_HTML.gif" /></p>
<figcaption>Bland–Altman plot for the crosswalk versus the EQ-VT value set<br />
On the vertical axis, the difference between the crosswalk and EQ-VT value sets is shown for all 3125 health states. On the horizontal axis, the average value of the crosswalk and EQ-VT value set is shown for each health state</figcaption>
</figure>

## Discussion

### Main findings

This study produced a set of EQ-5D-5L values that directly represent the preferences of the Trinidad and Tobago adult population and that can now be used in clinical and economic applications in Trinidad and Tobago as well as in other Caribbean countries for applications in which the Trinidad and Tobago crosswalk values might have been used. Furthermore, the current study is the first one to use a mixed logit model to analyse the DCE data, owing to the use of a larger health state design for the DCE task. The mixed logit models produced similar results to the cTTO-only and hybrid models. The existing crosswalk value set was shown to be considerably different from the EQ-VT value set.

### Interpretation

There are two main drivers of differences between values in EQ-5D value sets: differences in scale and differences in the magnitudes of the coefficients of the underlying utility function relative to each other. Differences in scale between EQ-5D-3L value sets and EQ-VT based value sets have been observed in other studies \[26\]. For differences in scale, the lower values and the increase in the number of negative values in the new value set can be explained by several factors. There could have been greater willingness to trade life-years in the EQ-VT protocol than in the modified MVH Time Trade Off (TTO) protocol that was used to recalibrate the DCE data to a 0 (dead) to 1 (full health) scale in the 2016 EQ-5D-3L valuation study \[5\]. In the 2016 study, 10% of the respondents who completed all of the TTO tasks were non-traders (assigning the full health value to all states). In this (2023) study this fell to 0.2% (only 2 non-traders). This would in part be associated with the quality control protocol in EQ-VT which ensures that interviewers explain the cTTO tasks to each respondent, thereby promoting a better understanding of the cTTO tasks on behalf of the respondents. Generally, the introduction of the EQ-VT data quality control protocol ensures that respondents were explained all elements of the cTTO task, leading to more reliable data compared to TTO studies that do not employ a quality control strategy \[24\]. Further, the use of a pilot phase during the data collection may have improved the quality of the collected data which may impact the outcomes of the study as well \[26\]. Lastly, the method used to value health states with negative values has changed compared to the Measurement and Valuation of Health (MVH) protocol that was followed in the 2016 valuation study, which may affect the values elicited for those states.

The differences in patterns among the coefficients of the crosswalk and EQ-VT value sets could be associated with social change over the 7 year period: e.g. greater awareness of mental health may have influenced the anxiety/depression coefficients and the lock down associated with covid over 2020–2022 may have brought increased salience of usual activities to the respondents \[27\]. Such changes may highlight the need for revisiting/updating EQ-5D value sets. Further, the crosswalk algorithm was developed based on responses from European respondents. It is possible that T&T respondents respond differently to EQ-5D-3L and EQ-5D-5L, which may exacerbate any differences in value sets. Lastly, the descriptive systems are different between the EQ-5D-3L and the EQ-5D-5L in the mobility dimension, with level 3 mobility being defined as “confined to bed” in the EQ-5D-3L, while level 5 for mobility in the EQ-5D-5L is defined as “unable to walk about”. Directly valuing “confined to bed” may lead to a higher willingness to trade life years as compared to valuing “unable to walk”, as it may be perceived as being more severe \[28\]. This may (partially) explain differences observed between the crosswalk and directly evaluated EQ-5D-5L value sets, as for the crosswalk, the value for health states with level 4 or 5 problems on mobility are inferred from the value assigned to “being confined to bed”.

Compared to the USA which also used EQ-VT, the Trinidad and Tobago level 5 coefficients follow a similar pattern with pain/discomfort having the largest coefficients in both values sets (0.480 versus 0.414 for the USA) and usual activities having the smallest coefficients (0.219 and 0.255 respectively) \[29\]. At level 5, both value sets show the same ranking of coefficients (smallest to largest): UA, SC, AD, MO, PD. However at other levels the rankings are not the same, for example for the level 1 coefficients the Trinidad and Tobago value set has: UA, AD, SC, MO, PD whereas for the USA this is AD, PD, UA, SC, MO. State 55555 has values of -0.573 (USA) and -0.563 (Trinidad and Tobago). Such differences in ranking and scale show the importance of using local health-state values to inform resource allocation decisions.

This was the first use of mixed logit models in EQ-VT (due to the use of a new DCE design, which has more choice tasks per respondent, which allows for the mixed logit model to be identified). The current study shows that an expanded health state design for the DCE task allows us to estimate mixed logit models on EQ-VT data, which are theoretically superior to the standard conditional logit model. The results of the mixed logit models were, after rescaling, similar to those of the cTTO-only and hybrid models.

### Limitations and strengths

This study had some minor limitations in the sampling. Females in the 35–44 and 55–64 age groups were slightly over-represented. More educated groups were also over-represented but this has been found to have little or no impact on EQ-5D valuation results \[30, 31\]. Another limitation is that there were some protocol compliance issues with some of the interviewers. Some of these could be solved during the pilot phase but some issues persisted beyond, which had to be resolved during the data collection. Furthermore there were also some interviewer effects suggesting that there may have been some differences in how interviewers conducted their interviews, although this could also be associated with demographic differences in the respondents interviewed by each interviewer.

There are several strengths and contributions of this study. First, our study design allowed the use of mixed logit models to analyse the DCE data; the first country to do so for the EQ-5D-5L using the EQ-VT protocol. Second, the study created an updated set of values for the Trinidad and Tobago population that will replace the crosswalk values. Lastly, the crosswalk was originally created to provide interim value sets for countries that had EQ-5D-3L value sets. Crosswalk sets can also be used in resource-constrained settings to allow users time to build capacity in working with health outcomes. This would facilitate the use of EQ-5D without the resource commitment for EQ-VT, until an EQ-5D-5L valuation study can be undertaken. This study gives users in Trinidad and Tobago the opportunity to move to an updated value set that represents the preferences of the population as of 2022.

## Conclusion

This study has produced a state of the art EQ-5D-5L value set for Trinidad and Tobago that can now be used in clinical and resource-allocation decision-making. Changes in the value sets for Trinidad and Tobago over the period 2016 to 2022 highlight the need for revising EQ-5D value sets to ensure they are developed using the highest standard of current practice, and represent the current preferences of the national population. Furthermore, this value set represents the first value set developed using the EQ-VT protocol in the Caribbean and may be used as a reference case for countries in the region with similar population characteristics.

## Acknowledgements

This study was funded by the EuroQol Research Foundation (Project number 341-RA).

### Appendix A

#### Full modelling results

<div id="Taba" class="table-wrap">

<div class="caption">

Results of modeling cTTO responses. NC indicates that no constant was estimated in the model

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;"><strong>Randomintercept</strong></th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;"><strong>Random intercept Tobit</strong></th>
<th colspan="3" style="text-align: left;"><strong>Heteroskedastic</strong></th>
<th colspan="3" style="text-align: left;"><strong>Heteroskedastic (NC)</strong></th>
<th colspan="3" style="text-align: left;"><strong>Heteroskedastic tobit (NC)</strong></th>
</tr>
<tr>
<th style="text-align: left;">coefficients</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>mo2</strong></td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.398</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.048</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo3</strong></td>
<td style="text-align: left;">0.049</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.035</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo4</strong></td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.164</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.164</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.162</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo5</strong></td>
<td style="text-align: left;">0.323</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.334</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.344</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.344</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.357</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc2</strong></td>
<td style="text-align: left;">0.028</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.024</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.029</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc3</strong></td>
<td style="text-align: left;">0.055</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.051</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.076</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.076</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc4</strong></td>
<td style="text-align: left;">0.160</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.157</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.157</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.159</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc5</strong></td>
<td style="text-align: left;">0.257</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.283</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.209</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.208</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.221</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua2</strong></td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">0.033</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.009</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.021</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua3</strong></td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua4</strong></td>
<td style="text-align: left;">0.159</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.157</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.144</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.144</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.145</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua5</strong></td>
<td style="text-align: left;">0.235</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.260</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.202</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.202</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.216</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd2</strong></td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.030</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.028</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.029</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.026</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd3</strong></td>
<td style="text-align: left;">0.110</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.108</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.102</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd4</strong></td>
<td style="text-align: left;">0.316</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.323</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.311</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.311</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.316</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd5</strong></td>
<td style="text-align: left;">0.517</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.535</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.511</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.511</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.541</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad2</strong></td>
<td style="text-align: left;">0.023</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.068</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.143</td>
<td style="text-align: left;">0.026</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.026</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.024</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad3</strong></td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.055</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.067</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.067</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.057</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad4</strong></td>
<td style="text-align: left;">0.178</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.175</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.172</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.172</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad5</strong></td>
<td style="text-align: left;">0.272</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.283</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.264</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.264</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.272</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Constant</strong></td>
<td style="text-align: left;">-0.012</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.411</td>
<td style="text-align: left;">-0.010</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: left;">0.527</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.921</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"><strong>AIC</strong></td>
<td style="text-align: left;">9609.975</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">11,562.85</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">8269.441</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">8267.45</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9265.768</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>BIC</strong></td>
<td style="text-align: left;">9777.562</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">11,730.43</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">8575.468</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">8566.192</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9571.795</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE (total)</strong></td>
<td style="text-align: left;">0.292</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.292</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.294</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.294</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.295</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE(86)</strong></td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.049</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.038</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.038</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.043</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>v(55555)</strong></td>
<td style="text-align: left;">-0.593</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.686</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.530</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.530</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.607</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

<div id="Tabb" class="table-wrap">

<div class="caption">

DCE logit modelling results. Rescaled using the scale length for the hybrid heteroskedastic model. Rescaling factor: 0.0641

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;"><strong>Conditional logit</strong></th>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;"><strong>Mixed logit</strong></th>
<th colspan="2" style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Mean Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Mean Beta (rescaled)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>mo2</strong></td>
<td style="text-align: left;">0.341</td>
<td style="text-align: left;">0.053</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.746</td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.048</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo3</strong></td>
<td style="text-align: left;">0.706</td>
<td style="text-align: left;">0.053</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">1.51</td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.097</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo4</strong></td>
<td style="text-align: left;">1.380</td>
<td style="text-align: left;">0.069</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">3.165</td>
<td style="text-align: left;">0.179</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.203</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo5</strong></td>
<td style="text-align: left;">2.524</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">5.701</td>
<td style="text-align: left;">0.298</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.365</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc2</strong></td>
<td style="text-align: left;">0.152</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.473</td>
<td style="text-align: left;">0.110</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.030</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc3</strong></td>
<td style="text-align: left;">0.488</td>
<td style="text-align: left;">0.054</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">1.236</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.079</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc4</strong></td>
<td style="text-align: left;">1.006</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">2.427</td>
<td style="text-align: left;">0.150</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.156</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc5</strong></td>
<td style="text-align: left;">1.584</td>
<td style="text-align: left;">0.073</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">3.773</td>
<td style="text-align: left;">0.197</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.242</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua2</strong></td>
<td style="text-align: left;">0.088</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">0.173</td>
<td style="text-align: left;">0.108</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">0.011</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua3</strong></td>
<td style="text-align: left;">0.430</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.961</td>
<td style="text-align: left;">0.117</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.062</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua4</strong></td>
<td style="text-align: left;">0.981</td>
<td style="text-align: left;">0.060</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">2.152</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.138</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua5</strong></td>
<td style="text-align: left;">1.450</td>
<td style="text-align: left;">0.068</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">3.186</td>
<td style="text-align: left;">0.176</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.204</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd2</strong></td>
<td style="text-align: left;">0.555</td>
<td style="text-align: left;">0.053</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">1.259</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.081</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd3</strong></td>
<td style="text-align: left;">1.020</td>
<td style="text-align: left;">0.057</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">2.372</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.152</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd4</strong></td>
<td style="text-align: left;">2.178</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">5.031</td>
<td style="text-align: left;">0.238</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.322</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd5</strong></td>
<td style="text-align: left;">3.218</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">7.730</td>
<td style="text-align: left;">0.340</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.495</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad2</strong></td>
<td style="text-align: left;">0.102</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">0.049</td>
<td style="text-align: left;">0.263</td>
<td style="text-align: left;">0.119</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;">0.017</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad3</strong></td>
<td style="text-align: left;">0.515</td>
<td style="text-align: left;">0.056</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">1.237</td>
<td style="text-align: left;">0.137</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.079</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad4</strong></td>
<td style="text-align: left;">1.064</td>
<td style="text-align: left;">0.073</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">2.436</td>
<td style="text-align: left;">0.192</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.156</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad5</strong></td>
<td style="text-align: left;">1.735</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">3.988</td>
<td style="text-align: left;">0.246</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.256</td>
</tr>
<tr>
<td style="text-align: left;"><strong>AIC</strong></td>
<td style="text-align: left;">16424.36</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">15471.58</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>BIC</strong></td>
<td style="text-align: left;">16573.73</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">17348.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE (total)</strong></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.303</td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE(86 states)</strong></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.053</td>
</tr>
<tr>
<td style="text-align: left;"><strong>v(55555)</strong></td>
<td style="text-align: left;">10.51</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">24.38</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.563</td>
</tr>
</tbody>
</table>

</div>

<div id="Tabc" class="table-wrap">

<div class="caption">

Hybrid modelling results

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><strong>Hybrid</strong></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;"><strong>Hybrid tobit</strong></th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;"><strong>Hybrid heteroskedastic</strong></th>
<th colspan="3" style="text-align: left;"><strong>Hybrid heteroskedastic Tobit</strong></th>
</tr>
<tr>
<th style="text-align: left;">coefficient</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">P-value</th>
<th style="text-align: left;">Beta</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>mo2</strong></td>
<td style="text-align: left;">0.034</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.029</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.029</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo3</strong></td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo4</strong></td>
<td style="text-align: left;">0.184</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.185</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.184</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.187</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>mo5</strong></td>
<td style="text-align: left;">0.363</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.379</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.357</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.368</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc2</strong></td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.041</td>
<td style="text-align: left;">0.024</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.024</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc3</strong></td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.072</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc4</strong></td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.150</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>sc5</strong></td>
<td style="text-align: left;">0.233</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.245</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.225</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.232</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua2</strong></td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.388</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.926</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.007</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua3</strong></td>
<td style="text-align: left;">0.061</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.060</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua4</strong></td>
<td style="text-align: left;">0.141</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.143</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ua5</strong></td>
<td style="text-align: left;">0.219</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.231</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.212</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.219</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd2</strong></td>
<td style="text-align: left;">0.066</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.046</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.044</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd3</strong></td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.128</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd4</strong></td>
<td style="text-align: left;">0.318</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.329</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.311</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>pd5</strong></td>
<td style="text-align: left;">0.486</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.511</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.464</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.480</td>
<td style="text-align: left;">0.008</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad2</strong></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.342</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad3</strong></td>
<td style="text-align: left;">0.069</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.065</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.075</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad4</strong></td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.160</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.161</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ad5</strong></td>
<td style="text-align: left;">0.259</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.268</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.257</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.264</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><strong>AIC</strong></td>
<td style="text-align: left;">28194.11</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">30170.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">24743.61</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">25755.71</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>BIC</strong></td>
<td style="text-align: left;">28371.76</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">30347.94</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">25082.75</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">26094.86</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE (total)</strong></td>
<td style="text-align: left;">0.297</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.297</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.296</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.297</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>MAE(86 states)</strong></td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.042</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.044</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>v(55555)</strong></td>
<td style="text-align: left;">-0.560</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.634</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.515</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">-0.563</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

<div id="Tabd" class="table-wrap">

<div class="caption">

leave-out analyses. MAE per model

</div>

| MAE                               | Leave out state | Leave out block |
|-----------------------------------|-----------------|-----------------|
| **Random intercept**              | 0.054           | 0.051           |
| **Random intercept Tobit**        | 0.065           | 0.060           |
| **Heteroskedastic**               | 0.050           | 0.052           |
| **Heteroskedastic (no constant)** | 0.049           | 0.052           |
| **Heteroskedastic Tobit**         | 0.056           | 0.042           |
| **Hybrid**                        | 0.049           | 0.051           |
| **Hybrid Tobit**                  | 0.057           | 0.054           |
| **Hybrid heteroskedastic**        | 0.046           | 0.051           |
| **Hybrid heteroskedastic Tobit**  | 0.049           | 0.050           |

</div>

### Appendix B

#### Technical details on modelling

This technical appendix provides an overview of the functional forms of the estimated models. All models were estimated as 20-parameter models, which means that the observed cTTO responses are modelled as a function of the level-dimension combinations of the EQ-5D-5L health state being valued. As there are 5 dimensions, with 5 levels each, each health state is represented by 20 dummy coded variables, indicating whether a particular level of problems is present on a dimension, with level 1 being the reference category for each dimension. For example, the dummy variable $`MO4`$ then represents having level 4 problems with mobility, or in other words, severe problems with walking about. The associated coefficient $`\beta_{3}`$ represents the decrement in value for having this level of problems on mobility.

#### Random intercept model

``` math
U_{\mathit{ij}} = \beta_{0} + \beta_{1}{MO2}_{j} + \beta_{2}{MO3}_{j} + \beta_{3}{MO4}_{j} + \beta_{4}{MO5}_{j} + \beta_{5}{SC2}_{j} + \beta_{6}{SC3}_{j} + \beta_{7}{SC4}_{j} + \beta_{8}{SC5}_{j} + \beta_{9}{UA2}_{j} + \beta_{10}{UA3}_{j} + \beta_{11}{UA4}_{j} + \beta_{12}{UA5}_{j} + \beta_{13}{PD2}_{j} + \beta_{14}{PD3}_{j} + \beta_{15}{PD4}_{j} + \beta_{16}{PD5}_{j} + \beta_{17}{AD2}_{j} + \beta_{18}{AD3}_{j} + \beta_{19}{AD4}_{j} + \beta_{20}{AD5}_{j} + \varepsilon_{\mathit{ij}} + \mu_{i}
```

The random intercept model models the utility $`U_{\mathit{ij}}`$ assigned by respondents $`i`$ to health state $`j.`$ Here, $`\beta_{0}`$ represents the fixed intercept, while $`\mu_{i}`$ represents a respondent-level intercept parameter, assumed to be normally distributed with mean 0, $`\mu_{j} \sim N{(0,\sigma_{\mu}^{2})}`$. $`\varepsilon_{\mathit{ij}}`$ is the error term for health state $`j`$ valued by respondent $`i`$, and is assumed to be distributed as $`\varepsilon_{\mathit{ij}} \sim N{(0,\sigma_{j}^{2})}`$.

#### Random intercept Tobit model

The random intercept Tobit regression takes the same functional form as that of the random intercept model. However, the data is also assumed to be “left censored” at -1, which means that no values beyond -1 are observed due to the fact that this is not possible in the cTTO task, but that it may be the case that some respondents would have assigned lower values to some health states in case this would have been possible in the cTTO task. Therefore, the following link function is assumed:

``` math
U = \left\{ \begin{matrix}
{U"ifU" > - 1} \\
{- 1ifU" < - 1}
\end{matrix} \right)
```

Here, $`U`$ is the observed cTTO response, while $`U"`$ is a latent variable that is assumed to be underlying of $`U`$, and the tobit model adjusts the parameter estimates based on the probability of the latent variable $`U"`$ being smaller than the threshold -1 \[32, 33\].

#### Heteroskedastic model and heteroskedastic Tobit model

Two models were estimated to correct for the heteroskedastic nature of the data; the fact that the error term is often not normally distributed in 20-parameter models for cTTO data. Instead, the error terms is usually larger for more severe health states, and smaller for those health states which are relatively mild. Therefore, the error term $`\varepsilon_{j}`$ of the equation below, which was modelled as a function of the 20 dummy variables of the model itself, $`{MO2}_{j}`$ to $`{AD5}_{j}`$.

``` math
U_{j} = \beta_{0} + \beta_{1}{MO2}_{j} + \beta_{2}{MO3}_{j} + \beta_{3}{MO4}_{j} + \beta_{4}{MO5}_{j} + \beta_{5}{SC2}_{j} + \beta_{6}{SC3}_{j} + \beta_{7}{SC4}_{j} + \beta_{8}{SC5}_{j} + \beta_{9}{UA2}_{j} + \beta_{10}{UA3}_{j} + \beta_{11}{UA4}_{j} + \beta_{12}{UA5}_{j} + \beta_{13}{PD2}_{j} + \beta_{14}{PD3}_{j} + \beta_{15}{PD4}_{j} + \beta_{16}{PD5}_{j} + \beta_{17}{AD2}_{j} + \beta_{18}{AD3}_{j} + \beta_{19}{AD4}_{j} + \beta_{20}{AD5}_{j} + \varepsilon_{j}
```

The variance function for the error term is then represented as following:

``` math
\sigma_{j}^{2} = \text{exp}{(\gamma_{0} + \gamma_{1}{MO2}_{j} + \gamma_{2}{MO3}_{j} + \gamma_{3}{MO4}_{j} + \gamma_{4}{MO5}_{j} + \gamma_{5}{SC2}_{j} + \gamma_{6}{SC3}_{j} + \gamma_{7}{SC4}_{j} + \gamma_{8}{SC5}_{j} + \gamma_{9}{UA2}_{j} + \gamma_{10}{UA3}_{j} + \gamma_{11}{UA4}_{j} + \gamma_{12}{UA5}_{j} + \gamma_{13}{PD2}_{j} + \gamma_{14}{PD3}_{j} + \gamma_{15}{PD4}_{j} + \gamma_{16}{PD5}_{j} + \gamma_{17}{AD2}_{j} + \gamma_{18}{AD3}_{j} + \gamma_{19}{AD4}_{j} + \gamma_{20}{AD5}_{j})}
```

For the Tobit model corrected for heteroskedasticity, the same functional form for both the model as well as the variance of the error term is assumed, with the additional Tobit link function as assumed in the random intercept Tobit model.

#### Conditional logit model

The conditional logit model assumes that an individual has a utility function $`U(X),`$ which is based on a fixed part, as well as a stochastic part \[34\]. The fixed part in our case takes the form:

``` math
U_{j} = \beta_{1}{MO2}_{j} + \beta_{2}{MO3}_{j} + \beta_{3}{MO4}_{j} + \beta_{4}{MO5}_{j} + \beta_{5}{SC2}_{j} + \beta_{6}{SC3}_{j} + \beta_{7}{SC4}_{j} + \beta_{8}{SC5}_{j} + \beta_{9}{UA2}_{j} + \beta_{10}{UA3}_{j} + \beta_{11}{UA4}_{j} + \beta_{12}{UA5}_{j} + \beta_{13}{PD2}_{j} + \beta_{14}{PD3}_{j} + \beta_{15}{PD4}_{j} + \beta_{16}{PD5}_{j} + \beta_{17}{AD2}_{j} + \beta_{18}{AD3}_{j} + \beta_{19}{AD4}_{j} + \beta_{20}{AD5}_{j}
```

If a respondent chooses between health states $`j`$ and $`k`$, then probability of choosing health state $`j`$ is modelled as:

``` math
P\left( {j,|,X,,,k} \right) = \frac{e^{U_{j}{(\beta X_{j})}}}{e^{U_{j}{(\beta X_{j})}} + e^{U_{k}{(\beta X_{k})}}}
```

Here, $`\beta X`$ represents the weights $`\beta`$ associated to the vector of attributes of the health states $`X`$ as outlined in the fixed part of the utility function. The choice probabilities are subsequently modelled over the whole population, ignoring that each respondent provides multiple datapoints.

#### Mixed logit model

In the mixed logit model, in contrast to the conditional logit, the $`\beta`$ parameters are allowed to vary between respondents. This means that the fixed portion of the utility function takes the form:

``` math
U_{\mathit{ij}} = \beta_{i1}{MO2}_{\mathit{ij}} + \beta_{i2}{MO3}_{\mathit{ij}} + \beta_{i3}{MO4}_{\mathit{ij}} + \beta_{i4}{MO5}_{\mathit{ij}} + \beta_{i5}{SC2}_{\mathit{ij}} + \beta_{i6}{SC3}_{\mathit{ij}} + \beta_{i7}{SC4}_{\mathit{ij}} + \beta_{i8}{SC5}_{\mathit{ij}} + \beta_{i9}{UA2}_{\mathit{ij}} + \beta_{i10}{UA3}_{\mathit{ij}} + \beta_{i11}{UA4}_{\mathit{ij}} + \beta_{i12}{UA5}_{\mathit{ij}} + \beta_{i13}{PD2}_{\mathit{ij}} + \beta_{i14}{PD3}_{\mathit{ij}} + \beta_{i15}{PD4}_{\mathit{ij}} + \beta_{i16}{PD5}_{\mathit{ij}} + \beta_{i17}{AD2}_{\mathit{ij}} + \beta_{i18}{AD3}_{\mathit{ij}} + \beta_{i19}{AD4}_{\mathit{ij}} + \beta_{i20}{AD5}_{\mathit{ij}}
```

This means that respondent $`i`$’s choice probability is modelled as follows:

``` math
P_{i}\left( {j,|,X,,,k} \right) = \int\frac{e^{U_{\mathit{ij}}{({\beta_{i},X_{\mathit{ij}}})}}}{e^{U_{\mathit{ij}}{({\beta_{i},X_{\mathit{ij}}})}} + e^{U_{\mathit{ik}}{({\beta_{i},X_{\mathit{ik}}})}}}f\left( {\beta_{i},{|\theta}} \right)d{(\beta_{i})}
```

Here, $`f\left( {\beta_{i},{|\theta}} \right)`$ represents the density function of $`\beta_{i}.`$

#### Hybrid models

For the hybrid models, the following functional form is again assumed for the cTTO data:

``` math
U_{j} = \beta_{0} + \beta_{1}{MO2}_{j} + \beta_{2}{MO3}_{j} + \beta_{3}{MO4}_{j} + \beta_{4}{MO5}_{j} + \beta_{5}{SC2}_{j} + \beta_{6}{SC3}_{j} + \beta_{7}{SC4}_{j} + \beta_{8}{SC5}_{j} + \beta_{9}{UA2}_{j} + \beta_{10}{UA3}_{j} + \beta_{11}{UA4}_{j} + \beta_{12}{UA5}_{j} + \beta_{13}{PD2}_{j} + \beta_{14}{PD3}_{j} + \beta_{15}{PD4}_{j} + \beta_{16}{PD5}_{j} + \beta_{17}{AD2}_{j} + \beta_{18}{AD3}_{j} + \beta_{19}{AD4}_{j} + \beta_{20}{AD5}_{j} + \varepsilon_{j}
```

These models can be estimated using the Tobit link function to account for left-censoring, as well as modelling the variance of the error term, as specified for the heteroskedastic model. For the DCE data, a conditional logit model type of functional form is assumed. The data is then modelled jointly. For more details on the likelihood function of the hybrid model, see Ramos-Goni et al. \[35\].

### Appendix C

#### DCE health state design

<div id="Tabe" class="table-wrap">

|  |  |  | **A** |  |  |  |  | **B** |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|
| Block | **Choice situation** | **mo** | **sc** | **ua** | **pd** | **ad** | **mo** | **sc** | **ua** | **pd** | **ad** |
| **1** | 1 | 3 | 1 | 1 | 1 | 4 | 1 | 1 | 1 | 2 | 3 |
| **1** | 2 | 4 | 1 | 5 | 3 | 1 | 5 | 2 | 4 | 3 | 1 |
| **1** | 3 | 2 | 3 | 3 | 4 | 2 | 4 | 2 | 2 | 4 | 2 |
| **1** | 4 | 2 | 1 | 2 | 3 | 3 | 2 | 4 | 2 | 2 | 2 |
| **1** | 5 | 2 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 4 | 5 |
| **1** | 6 | 3 | 4 | 5 | 5 | 3 | 1 | 1 | 5 | 5 | 5 |
| **1** | 7 | 3 | 5 | 4 | 1 | 2 | 1 | 4 | 4 | 1 | 4 |
| **1** | 8 | 4 | 4 | 3 | 1 | 5 | 4 | 5 | 3 | 2 | 4 |
| **1** | 9 | 4 | 1 | 4 | 4 | 4 | 2 | 2 | 5 | 4 | 4 |
| **1** | 10 | 5 | 1 | 2 | 5 | 1 | 4 | 2 | 3 | 5 | 1 |
| **1** | 11 | 3 | 3 | 1 | 2 | 5 | 1 | 3 | 1 | 5 | 2 |
| **1** | 12 | 2 | 3 | 2 | 4 | 3 | 5 | 3 | 5 | 1 | 3 |
| **2** | 13 | 1 | 5 | 2 | 3 | 1 | 1 | 1 | 3 | 4 | 1 |
| **2** | 14 | 5 | 4 | 1 | 5 | 1 | 5 | 4 | 2 | 4 | 2 |
| **2** | 15 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 1 | 4 | 1 |
| **2** | 16 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 3 | 3 |
| **2** | 17 | 2 | 5 | 1 | 3 | 2 | 2 | 5 | 2 | 2 | 1 |
| **2** | 18 | 2 | 4 | 5 | 1 | 4 | 3 | 2 | 5 | 1 | 5 |
| **2** | 19 | 5 | 2 | 1 | 2 | 3 | 2 | 2 | 5 | 2 | 5 |
| **2** | 20 | 3 | 3 | 1 | 3 | 5 | 1 | 2 | 4 | 3 | 5 |
| **2** | 21 | 5 | 3 | 4 | 2 | 1 | 3 | 4 | 4 | 2 | 3 |
| **2** | 22 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 1 | 5 | 2 |
| **2** | 23 | 4 | 5 | 2 | 1 | 4 | 5 | 4 | 2 | 1 | 5 |
| **2** | 24 | 1 | 2 | 2 | 5 | 4 | 1 | 5 | 4 | 5 | 1 |
| **3** | 25 | 3 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3 |
| **3** | 26 | 5 | 1 | 4 | 2 | 2 | 5 | 1 | 3 | 4 | 3 |
| **3** | 27 | 1 | 3 | 3 | 2 | 1 | 1 | 2 | 3 | 1 | 2 |
| **3** | 28 | 5 | 2 | 1 | 3 | 4 | 5 | 5 | 3 | 3 | 2 |
| **3** | 29 | 1 | 5 | 5 | 3 | 1 | 1 | 3 | 5 | 4 | 2 |
| **3** | 30 | 2 | 4 | 1 | 2 | 4 | 2 | 3 | 4 | 3 | 4 |
| **3** | 31 | 3 | 4 | 3 | 5 | 3 | 3 | 5 | 1 | 4 | 3 |
| **3** | 32 | 2 | 1 | 2 | 1 | 4 | 3 | 1 | 1 | 1 | 5 |
| **3** | 33 | 2 | 3 | 5 | 5 | 5 | 3 | 3 | 2 | 5 | 4 |
| **3** | 34 | 4 | 2 | 3 | 2 | 1 | 4 | 4 | 1 | 1 | 1 |
| **3** | 35 | 2 | 1 | 2 | 2 | 5 | 4 | 1 | 5 | 2 | 1 |
| **3** | 36 | 4 | 3 | 2 | 1 | 5 | 5 | 3 | 4 | 1 | 3 |
| **4** | 37 | 5 | 2 | 5 | 3 | 2 | 3 | 1 | 5 | 5 | 2 |
| **4** | 38 | 1 | 2 | 1 | 4 | 2 | 1 | 3 | 1 | 3 | 4 |
| **4** | 39 | 3 | 4 | 2 | 3 | 1 | 3 | 3 | 3 | 3 | 2 |
| **4** | 40 | 1 | 5 | 2 | 5 | 3 | 2 | 4 | 4 | 5 | 3 |
| **4** | 41 | 2 | 2 | 3 | 1 | 3 | 2 | 1 | 5 | 1 | 2 |
| **4** | 42 | 4 | 2 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 5 |
| **4** | 43 | 5 | 5 | 4 | 4 | 4 | 5 | 2 | 5 | 5 | 4 |
| **4** | 44 | 3 | 1 | 3 | 3 | 5 | 4 | 1 | 3 | 2 | 4 |
| **4** | 45 | 2 | 5 | 2 | 5 | 3 | 3 | 5 | 5 | 2 | 3 |
| **4** | 46 | 4 | 4 | 4 | 5 | 2 | 2 | 1 | 4 | 5 | 4 |
| **4** | 47 | 1 | 3 | 2 | 4 | 5 | 1 | 5 | 1 | 1 | 5 |
| **4** | 48 | 1 | 4 | 1 | 2 | 5 | 1 | 4 | 5 | 1 | 3 |
| **5** | 49 | 1 | 1 | 3 | 3 | 2 | 2 | 1 | 2 | 3 | 3 |
| **5** | 50 | 5 | 3 | 1 | 5 | 1 | 4 | 4 | 1 | 4 | 1 |
| **5** | 51 | 2 | 4 | 4 | 3 | 1 | 2 | 3 | 5 | 4 | 1 |
| **5** | 52 | 5 | 5 | 3 | 1 | 5 | 3 | 5 | 3 | 5 | 4 |
| **5** | 53 | 1 | 2 | 4 | 4 | 3 | 4 | 2 | 5 | 2 | 3 |
| **5** | 54 | 3 | 2 | 1 | 1 | 3 | 2 | 5 | 1 | 1 | 1 |
| **5** | 55 | 3 | 3 | 2 | 2 | 5 | 5 | 2 | 2 | 2 | 4 |
| **5** | 56 | 4 | 3 | 4 | 2 | 2 | 3 | 5 | 1 | 2 | 2 |
| **5** | 57 | 5 | 4 | 3 | 5 | 3 | 2 | 2 | 3 | 5 | 5 |
| **5** | 58 | 1 | 4 | 4 | 2 | 2 | 1 | 4 | 3 | 3 | 1 |
| **5** | 59 | 4 | 5 | 2 | 3 | 4 | 2 | 4 | 5 | 3 | 4 |
| **5** | 60 | 5 | 1 | 3 | 2 | 4 | 5 | 1 | 5 | 3 | 2 |
| **6** | 61 | 3 | 3 | 2 | 1 | 4 | 5 | 2 | 2 | 1 | 3 |
| **6** | 62 | 4 | 1 | 5 | 4 | 5 | 4 | 5 | 2 | 4 | 4 |
| **6** | 63 | 1 | 3 | 1 | 5 | 3 | 4 | 5 | 1 | 3 | 3 |
| **6** | 64 | 5 | 3 | 4 | 3 | 1 | 2 | 1 | 4 | 4 | 1 |
| **6** | 65 | 1 | 5 | 2 | 2 | 5 | 1 | 2 | 4 | 2 | 4 |
| **6** | 66 | 2 | 3 | 5 | 3 | 1 | 3 | 4 | 5 | 2 | 1 |
| **6** | 67 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 4 | 1 |
| **6** | 68 | 4 | 4 | 3 | 3 | 2 | 4 | 5 | 4 | 1 | 2 |
| **6** | 69 | 5 | 3 | 2 | 4 | 2 | 4 | 3 | 2 | 5 | 3 |
| **6** | 70 | 4 | 2 | 1 | 5 | 5 | 4 | 1 | 5 | 5 | 3 |
| **6** | 71 | 4 | 1 | 2 | 1 | 1 | 1 | 5 | 3 | 1 | 1 |
| **6** | 72 | 3 | 2 | 5 | 4 | 5 | 1 | 4 | 4 | 4 | 5 |
| **7** | 73 | 3 | 2 | 4 | 1 | 5 | 3 | 5 | 4 | 3 | 3 |
| **7** | 74 | 4 | 1 | 4 | 5 | 4 | 5 | 4 | 3 | 5 | 4 |
| **7** | 75 | 4 | 4 | 1 | 3 | 2 | 2 | 5 | 1 | 4 | 2 |
| **7** | 76 | 2 | 3 | 3 | 1 | 3 | 1 | 5 | 3 | 1 | 2 |
| **7** | 77 | 3 | 2 | 2 | 3 | 1 | 4 | 2 | 3 | 1 | 1 |
| **7** | 78 | 5 | 4 | 4 | 4 | 5 | 5 | 1 | 5 | 5 | 5 |
| **7** | 79 | 5 | 3 | 1 | 1 | 4 | 2 | 4 | 1 | 2 | 4 |
| **7** | 80 | 1 | 2 | 4 | 5 | 2 | 4 | 2 | 2 | 4 | 2 |
| **7** | 81 | 1 | 2 | 5 | 2 | 3 | 2 | 3 | 5 | 2 | 2 |
| **7** | 82 | 3 | 3 | 3 | 2 | 3 | 2 | 1 | 3 | 3 | 3 |
| **7** | 83 | 3 | 1 | 3 | 4 | 4 | 5 | 1 | 1 | 2 | 4 |
| **7** | 84 | 5 | 5 | 2 | 5 | 1 | 5 | 5 | 5 | 3 | 4 |
| **8** | 85 | 3 | 5 | 4 | 1 | 5 | 4 | 3 | 4 | 3 | 5 |
| **8** | 86 | 1 | 2 | 5 | 4 | 3 | 1 | 4 | 3 | 4 | 4 |
| **8** | 87 | 2 | 1 | 4 | 4 | 1 | 1 | 1 | 2 | 5 | 1 |
| **8** | 88 | 3 | 3 | 5 | 5 | 2 | 5 | 5 | 5 | 2 | 2 |
| **8** | 89 | 1 | 2 | 3 | 3 | 5 | 2 | 2 | 2 | 3 | 4 |
| **8** | 90 | 3 | 1 | 4 | 3 | 3 | 1 | 1 | 1 | 4 | 3 |
| **8** | 91 | 4 | 5 | 5 | 1 | 2 | 5 | 4 | 5 | 1 | 1 |
| **8** | 92 | 5 | 3 | 2 | 1 | 2 | 4 | 4 | 2 | 1 | 1 |
| **8** | 93 | 2 | 4 | 2 | 2 | 5 | 1 | 4 | 5 | 2 | 4 |
| **8** | 94 | 3 | 2 | 2 | 4 | 1 | 2 | 2 | 1 | 5 | 1 |
| **8** | 95 | 5 | 2 | 1 | 3 | 2 | 5 | 3 | 1 | 2 | 3 |
| **8** | 96 | 3 | 4 | 5 | 5 | 2 | 3 | 2 | 3 | 5 | 4 |
| **9** | 97 | 5 | 1 | 1 | 3 | 5 | 4 | 3 | 1 | 2 | 5 |
| **9** | 98 | 4 | 5 | 4 | 3 | 1 | 3 | 5 | 4 | 2 | 3 |
| **9** | 99 | 2 | 4 | 2 | 5 | 5 | 2 | 5 | 4 | 5 | 2 |
| **9** | 100 | 5 | 3 | 1 | 4 | 5 | 2 | 5 | 2 | 4 | 5 |
| **9** | 101 | 3 | 1 | 1 | 1 | 5 | 5 | 1 | 2 | 1 | 3 |
| **9** | 102 | 4 | 4 | 3 | 4 | 1 | 2 | 3 | 3 | 4 | 4 |
| **9** | 103 | 1 | 2 | 2 | 1 | 5 | 1 | 4 | 3 | 1 | 4 |
| **9** | 104 | 4 | 3 | 5 | 4 | 3 | 4 | 2 | 5 | 2 | 4 |
| **9** | 105 | 1 | 3 | 4 | 5 | 1 | 1 | 3 | 5 | 4 | 2 |
| **9** | 106 | 3 | 1 | 3 | 5 | 2 | 3 | 1 | 4 | 4 | 4 |
| **9** | 107 | 2 | 2 | 3 | 1 | 3 | 2 | 4 | 2 | 1 | 2 |
| **9** | 108 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 3 | 4 | 1 |
| **10** | 109 | 1 | 5 | 4 | 1 | 3 | 1 | 1 | 4 | 2 | 5 |
| **10** | 110 | 3 | 4 | 4 | 2 | 3 | 3 | 4 | 3 | 4 | 2 |
| **10** | 111 | 1 | 5 | 1 | 4 | 4 | 3 | 5 | 1 | 5 | 2 |
| **10** | 112 | 3 | 4 | 2 | 3 | 1 | 3 | 2 | 5 | 1 | 1 |
| **10** | 113 | 5 | 3 | 3 | 1 | 1 | 3 | 3 | 5 | 4 | 1 |
| **10** | 114 | 4 | 1 | 3 | 2 | 3 | 5 | 1 | 2 | 2 | 1 |
| **10** | 115 | 4 | 3 | 4 | 5 | 1 | 4 | 2 | 2 | 5 | 3 |
| **10** | 116 | 3 | 1 | 3 | 1 | 1 | 4 | 1 | 1 | 1 | 2 |
| **10** | 117 | 1 | 5 | 5 | 3 | 5 | 1 | 4 | 5 | 5 | 4 |
| **10** | 118 | 2 | 1 | 4 | 4 | 5 | 2 | 3 | 5 | 3 | 5 |
| **10** | 119 | 4 | 3 | 2 | 3 | 4 | 2 | 4 | 1 | 3 | 4 |
| **10** | 120 | 5 | 2 | 4 | 3 | 5 | 5 | 5 | 1 | 2 | 5 |
| **11** | 121 | 2 | 2 | 3 | 1 | 3 | 2 | 2 | 5 | 3 | 2 |
| **11** | 122 | 3 | 3 | 3 | 2 | 2 | 1 | 3 | 2 | 2 | 4 |
| **11** | 123 | 1 | 1 | 2 | 5 | 2 | 1 | 1 | 5 | 1 | 4 |
| **11** | 124 | 2 | 4 | 4 | 1 | 1 | 2 | 5 | 1 | 2 | 1 |
| **11** | 125 | 5 | 2 | 1 | 4 | 1 | 3 | 2 | 1 | 5 | 4 |
| **11** | 126 | 4 | 2 | 4 | 2 | 2 | 2 | 5 | 4 | 1 | 2 |
| **11** | 127 | 5 | 4 | 5 | 1 | 3 | 5 | 4 | 3 | 3 | 4 |
| **11** | 128 | 2 | 4 | 4 | 2 | 3 | 3 | 4 | 2 | 4 | 3 |
| **11** | 129 | 1 | 4 | 1 | 2 | 1 | 1 | 3 | 1 | 3 | 3 |
| **11** | 130 | 5 | 2 | 3 | 5 | 4 | 4 | 1 | 3 | 5 | 5 |
| **11** | 131 | 5 | 1 | 4 | 1 | 2 | 2 | 2 | 4 | 4 | 2 |
| **11** | 132 | 4 | 4 | 1 | 3 | 3 | 4 | 3 | 1 | 1 | 5 |
| **12** | 133 | 2 | 3 | 4 | 5 | 1 | 3 | 3 | 3 | 5 | 2 |
| **12** | 134 | 4 | 4 | 2 | 4 | 3 | 4 | 3 | 5 | 4 | 4 |
| **12** | 135 | 3 | 5 | 2 | 2 | 4 | 1 | 5 | 3 | 2 | 5 |
| **12** | 136 | 2 | 3 | 3 | 5 | 5 | 1 | 2 | 5 | 5 | 5 |
| **12** | 137 | 5 | 5 | 2 | 5 | 2 | 3 | 5 | 2 | 4 | 5 |
| **12** | 138 | 5 | 1 | 5 | 4 | 1 | 4 | 5 | 5 | 2 | 1 |
| **12** | 139 | 1 | 1 | 1 | 4 | 3 | 1 | 1 | 2 | 3 | 5 |
| **12** | 140 | 2 | 4 | 5 | 5 | 5 | 5 | 5 | 1 | 5 | 5 |
| **12** | 141 | 3 | 2 | 4 | 5 | 4 | 4 | 2 | 2 | 4 | 4 |
| **12** | 142 | 2 | 5 | 5 | 1 | 4 | 4 | 3 | 4 | 1 | 4 |
| **12** | 143 | 1 | 3 | 5 | 3 | 3 | 1 | 2 | 3 | 3 | 4 |
| **12** | 144 | 4 | 1 | 2 | 5 | 2 | 5 | 4 | 2 | 2 | 2 |
| **13** | 145 | 2 | 5 | 3 | 3 | 5 | 4 | 5 | 4 | 3 | 4 |
| **13** | 146 | 3 | 1 | 5 | 3 | 3 | 4 | 1 | 2 | 3 | 5 |
| **13** | 147 | 2 | 4 | 1 | 3 | 2 | 1 | 3 | 1 | 4 | 2 |
| **13** | 148 | 5 | 1 | 4 | 3 | 3 | 5 | 2 | 4 | 2 | 2 |
| **13** | 149 | 3 | 2 | 2 | 5 | 1 | 3 | 4 | 1 | 4 | 1 |
| **13** | 150 | 5 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 1 | 5 |
| **13** | 151 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 4 | 3 |
| **13** | 152 | 5 | 1 | 4 | 2 | 1 | 4 | 5 | 5 | 2 | 1 |
| **13** | 153 | 3 | 5 | 3 | 1 | 1 | 2 | 3 | 5 | 1 | 1 |
| **13** | 154 | 3 | 4 | 2 | 5 | 3 | 2 | 5 | 4 | 5 | 3 |
| **13** | 155 | 1 | 5 | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 2 |
| **13** | 156 | 1 | 1 | 2 | 2 | 3 | 1 | 3 | 2 | 3 | 2 |
| **14** | 157 | 4 | 2 | 1 | 1 | 1 | 1 | 4 | 1 | 1 | 3 |
| **14** | 158 | 2 | 1 | 4 | 1 | 2 | 4 | 1 | 2 | 1 | 3 |
| **14** | 159 | 5 | 3 | 2 | 4 | 4 | 5 | 2 | 4 | 4 | 3 |
| **14** | 160 | 4 | 1 | 1 | 5 | 4 | 4 | 3 | 1 | 4 | 5 |
| **14** | 161 | 1 | 1 | 3 | 4 | 4 | 1 | 3 | 3 | 5 | 1 |
| **14** | 162 | 5 | 2 | 2 | 2 | 5 | 4 | 5 | 3 | 2 | 5 |
| **14** | 163 | 3 | 4 | 1 | 3 | 5 | 2 | 4 | 3 | 2 | 5 |
| **14** | 164 | 5 | 3 | 5 | 4 | 3 | 5 | 4 | 5 | 1 | 5 |
| **14** | 165 | 3 | 5 | 2 | 2 | 2 | 3 | 3 | 1 | 2 | 4 |
| **14** | 166 | 1 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 2 |
| **14** | 167 | 2 | 2 | 5 | 3 | 1 | 3 | 2 | 4 | 2 | 1 |
| **14** | 168 | 1 | 5 | 5 | 2 | 4 | 5 | 5 | 3 | 1 | 4 |
| **15** | 169 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 2 | 3 | 5 |
| **15** | 170 | 2 | 5 | 2 | 4 | 3 | 3 | 5 | 5 | 4 | 1 |
| **15** | 171 | 1 | 4 | 3 | 2 | 1 | 1 | 3 | 1 | 3 | 1 |
| **15** | 172 | 5 | 4 | 4 | 5 | 2 | 5 | 4 | 5 | 2 | 3 |
| **15** | 173 | 1 | 3 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | 4 |
| **15** | 174 | 2 | 5 | 3 | 4 | 4 | 2 | 4 | 5 | 4 | 2 |
| **15** | 175 | 4 | 5 | 3 | 4 | 3 | 4 | 3 | 3 | 2 | 5 |
| **15** | 176 | 2 | 4 | 1 | 1 | 4 | 2 | 5 | 1 | 2 | 2 |
| **15** | 177 | 1 | 1 | 3 | 1 | 5 | 1 | 1 | 4 | 2 | 4 |
| **15** | 178 | 3 | 1 | 1 | 5 | 3 | 4 | 1 | 1 | 4 | 1 |
| **15** | 179 | 4 | 2 | 1 | 5 | 5 | 5 | 2 | 4 | 3 | 5 |
| **15** | 180 | 5 | 2 | 2 | 1 | 2 | 2 | 2 | 4 | 1 | 5 |
| **16** | 181 | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 2 | 4 | 3 |
| **16** | 182 | 5 | 3 | 1 | 5 | 3 | 4 | 2 | 4 | 5 | 3 |
| **16** | 183 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 5 | 3 | 2 |
| **16** | 184 | 2 | 5 | 3 | 5 | 1 | 3 | 3 | 4 | 5 | 1 |
| **16** | 185 | 2 | 1 | 4 | 5 | 4 | 4 | 1 | 5 | 2 | 4 |
| **16** | 186 | 5 | 2 | 2 | 2 | 1 | 4 | 4 | 2 | 1 | 1 |
| **16** | 187 | 1 | 4 | 2 | 5 | 2 | 1 | 4 | 4 | 4 | 3 |
| **16** | 188 | 5 | 5 | 4 | 2 | 5 | 5 | 2 | 3 | 4 | 5 |
| **16** | 189 | 2 | 4 | 1 | 2 | 4 | 3 | 5 | 1 | 1 | 4 |
| **16** | 190 | 5 | 1 | 5 | 1 | 4 | 5 | 1 | 1 | 3 | 5 |
| **16** | 191 | 3 | 4 | 5 | 1 | 2 | 4 | 3 | 1 | 1 | 2 |
| **16** | 192 | 1 | 2 | 4 | 4 | 2 | 1 | 2 | 1 | 5 | 3 |
| **17** | 193 | 4 | 3 | 3 | 5 | 3 | 4 | 5 | 5 | 3 | 3 |
| **17** | 194 | 1 | 3 | 5 | 1 | 1 | 1 | 1 | 4 | 1 | 4 |
| **17** | 195 | 4 | 2 | 5 | 4 | 5 | 2 | 5 | 5 | 5 | 5 |
| **17** | 196 | 4 | 4 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 5 |
| **17** | 197 | 3 | 4 | 3 | 3 | 1 | 2 | 2 | 3 | 3 | 3 |
| **17** | 198 | 2 | 4 | 1 | 4 | 1 | 4 | 1 | 1 | 5 | 1 |
| **17** | 199 | 2 | 3 | 3 | 3 | 1 | 2 | 3 | 2 | 2 | 3 |
| **17** | 200 | 3 | 2 | 5 | 2 | 2 | 3 | 1 | 5 | 1 | 3 |
| **17** | 201 | 5 | 5 | 4 | 4 | 1 | 5 | 4 | 4 | 3 | 5 |
| **17** | 202 | 1 | 3 | 2 | 1 | 4 | 1 | 3 | 4 | 2 | 3 |
| **17** | 203 | 5 | 3 | 4 | 1 | 2 | 5 | 1 | 3 | 2 | 2 |
| **17** | 204 | 2 | 2 | 1 | 5 | 2 | 2 | 3 | 1 | 2 | 4 |
| **18** | 205 | 4 | 5 | 3 | 5 | 2 | 5 | 5 | 3 | 2 | 3 |
| **18** | 206 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 4 | 2 | 5 |
| **18** | 207 | 5 | 4 | 1 | 4 | 4 | 5 | 5 | 5 | 3 | 4 |
| **18** | 208 | 5 | 1 | 1 | 1 | 2 | 4 | 4 | 1 | 1 | 3 |
| **18** | 209 | 1 | 1 | 3 | 5 | 5 | 2 | 1 | 1 | 5 | 4 |
| **18** | 210 | 1 | 2 | 2 | 5 | 1 | 1 | 4 | 2 | 3 | 2 |
| **18** | 211 | 2 | 2 | 3 | 1 | 1 | 1 | 3 | 2 | 1 | 1 |
| **18** | 212 | 1 | 5 | 3 | 4 | 4 | 2 | 5 | 1 | 4 | 5 |
| **18** | 213 | 3 | 2 | 2 | 3 | 1 | 3 | 1 | 5 | 2 | 1 |
| **18** | 214 | 1 | 4 | 5 | 5 | 5 | 4 | 1 | 5 | 4 | 5 |
| **18** | 215 | 3 | 5 | 2 | 1 | 4 | 3 | 3 | 4 | 3 | 4 |
| **18** | 216 | 3 | 1 | 4 | 4 | 2 | 2 | 3 | 3 | 4 | 2 |
| **19** | 217 | 2 | 5 | 5 | 5 | 1 | 3 | 5 | 2 | 5 | 5 |
| **19** | 218 | 5 | 2 | 5 | 5 | 2 | 5 | 4 | 5 | 2 | 4 |
| **19** | 219 | 1 | 5 | 2 | 3 | 1 | 1 | 4 | 1 | 3 | 2 |
| **19** | 220 | 4 | 3 | 4 | 1 | 3 | 4 | 1 | 3 | 3 | 3 |
| **19** | 221 | 5 | 2 | 2 | 4 | 3 | 5 | 1 | 2 | 5 | 1 |
| **19** | 222 | 1 | 2 | 4 | 3 | 4 | 3 | 2 | 5 | 1 | 4 |
| **19** | 223 | 5 | 1 | 1 | 3 | 3 | 4 | 2 | 1 | 3 | 4 |
| **19** | 224 | 4 | 3 | 2 | 2 | 5 | 3 | 3 | 2 | 3 | 4 |
| **19** | 225 | 2 | 4 | 2 | 5 | 5 | 5 | 3 | 3 | 5 | 5 |
| **19** | 226 | 1 | 1 | 5 | 3 | 2 | 2 | 1 | 3 | 4 | 2 |
| **19** | 227 | 5 | 2 | 4 | 1 | 1 | 4 | 3 | 4 | 1 | 3 |
| **19** | 228 | 3 | 5 | 4 | 4 | 2 | 5 | 3 | 2 | 4 | 2 |
| **20** | 229 | 1 | 4 | 3 | 2 | 1 | 3 | 3 | 2 | 2 | 1 |
| **20** | 230 | 1 | 5 | 4 | 1 | 5 | 5 | 5 | 5 | 1 | 2 |
| **20** | 231 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 |
| **20** | 232 | 1 | 2 | 1 | 1 | 4 | 2 | 2 | 1 | 3 | 3 |
| **20** | 233 | 2 | 2 | 3 | 5 | 3 | 4 | 5 | 3 | 3 | 3 |
| **20** | 234 | 2 | 1 | 5 | 2 | 5 | 2 | 4 | 2 | 1 | 5 |
| **20** | 235 | 2 | 5 | 1 | 3 | 4 | 1 | 5 | 1 | 5 | 3 |
| **20** | 236 | 2 | 1 | 4 | 4 | 1 | 2 | 1 | 2 | 2 | 5 |
| **20** | 237 | 4 | 2 | 1 | 2 | 2 | 3 | 3 | 3 | 2 | 2 |
| **20** | 238 | 3 | 2 | 1 | 3 | 1 | 2 | 5 | 1 | 1 | 1 |
| **20** | 239 | 5 | 4 | 4 | 2 | 3 | 1 | 4 | 5 | 4 | 3 |
| **20** | 240 | 4 | 4 | 5 | 4 | 1 | 4 | 5 | 3 | 4 | 2 |

</div>

## Authors’ contributions

Material preparation, data collection and analysis were performed by BR, HB and FR. The first draft of the manuscript was written by BR, HB, MJ and EP. All authors commented on previous versions of the manuscript. All authors read and approved the final manuscript.

## Funding

This study was funded by the EuroQol Research Foundation (Project number 341-RA).

## Availability of data and material

The data that support the findings of this study are available from the corresponding author, but restrictions apply to the availability of these data, which are not publicly available. The data are, however, available from the authors upon reasonable request.

## Declarations

### Ethics approval and consent to participate

Ethical approval for this study was obtained from The University of The West Indies (Exemption letter CREC-SA.1468/03/2022 dated March 7th, 2022) and from the Ministry of Health of Trinidad and Tobago (Approval letter He:3/13/441 VolII dated April 8th, 2022).

Informed consent was obtained from all individual participants included in the study.

### Competing interests

Eleanor Pullenayegum and Fanni Rencz are on the Editorial Board of Health and Quality of Life Outcomes. All of the authors are members of the EuroQol Research Foundation. Bram Roudijk is employed by the EuroQol Research Foundation.

## Footnotes

## References

## References

1. EuroQol Group. About EQ-5D-5L. Available from: https://euroqol.org/eq-5d-instruments/eq-5d-5l-about/.

2. Devlin N, Roudijk B, Ludwig K, editors. Value sets for EQ-5D-5L: a compendium, comparative review & user guide. Cham: Springer International Publishing; 2022. Available from: https://link.springer.com/10.1007/978-3-030-89289-0. Cited 2023 Sep 29.

3. Bailey H, Kind P. Preliminary findings of an investigation into the relationship between national culture and EQ-5D value sets. Qual Life Res. 2010;19:1145–54. doi: 10.1007/s11136-010-9678-5.

4. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37:53–72. doi: 10.1016/0168-8510(96)00822-6.

5. Bailey H, Stolk E, Kind P. Toward Explicit Prioritization for the Caribbean: An EQ-5D Value Set for Trinidad and Tobago. Value in Health Regional Issues [Internet]. 2016 [cited 2023 Jul 3];11:60–7. Available from: https://linkinghub.elsevier.com/retrieve/pii/S221210991630036X. doi:10.1016/j.vhri.2016.07.010

6. Bailey H. EQ-5D-3L Population Norms for Trinidad and Tobago. Caribb Med J. 2022;84. Available from: https://www.caribbeanmedicaljournal.org/wp-content/uploads/2022/01/CMJ052021-Original-EQ-5D-3L-Population-Norms-for-Trinidad-and-Tobago.pdf.

7. Sanchez S, Teelucksingh S, Ali R, Bailey H, Legall G. Quality of Life and Health Status Among Patients Receiving Renal Replacement Therapy in Trinidad and Tobago. West Indies. IJNRD. 2021;14:173–92. doi: 10.2147/IJNRD.S302157.

8. Mencia MM, Moonsie R. Removing a bent femoral nail - man versus metal: A case report. Int J Surg Case Rep. 2022;99:107679. doi: 10.1016/j.ijscr.2022.107679.

9. Janssen MF, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, et al. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22:1717–27. doi: 10.1007/s11136-012-0322-4.

10. van Hout B, Janssen MF, Feng Y-S, Kohlmann T, Busschbach J, Golicki D, et al. Interim Scoring for the EQ-5D-5L: Mapping the EQ-5D-5L to EQ-5D-3L Value Sets. Value in Health. 2012;15:708–15. doi: 10.1016/j.jval.2012.02.008.

11. Bailey H, Janssen MF, La Foucade A, Kind P. EQ-5D-5L population norms and health inequalities for Trinidad and Tobago. Devleesschauwer B, editor. PLoS ONE. 2019;14:e0214283. doi: 10.1371/journal.pone.0214283.

12. Bahall M, Bailey H. The impact of chronic disease and accompanying bio-psycho-social factors on health-related quality of life. J Family Med Prim Care. 2022;11:4694. doi: 10.4103/jfmpc.jfmpc_2399_21.

13. Bailey H, Panday A, Lucky-Samaroo S, Maharajh A. Quality of life of MS patients in Trinidad and Tobago: Anomaly or adaptation? Mult Scler Relat Disord. 2023;76:104795. doi: 10.1016/j.msard.2023.104795.

14. Braithwaite T, Bailey H, Bartholomew D, Saei A, Pesudovs K, Ramsewak SS, et al. Impact of Vision Loss on Health-Related Quality of Life in Trinidad and Tobago. Ophthalmology. 2019;126:1055–8. doi: 10.1016/j.ophtha.2019.01.023.

15. Pran L, Baijoo S, Harnanan D, Slim H, Maharaj R, Naraynsingh V. Quality of life experienced by major lower extremity amputees. Cureus. 2021. Available from: https://www.cureus.com/articles/68415-quality-of-life-experienced-by-major-lower-extremity-amputees. Cited 2023 Jun 27. doi:10.7759/cureus.17440

16. Bailey H, Janssen MF, La Foucade A, Boodraj G, Wharton M, Castillo P. EQ-5D self-reported health in Barbados and Jamaica with EQ-5D-5L population norms for the English-speaking Caribbean. Health Qual Life Outcomes. 2021;19. Available from: https://www.embase.com/search/results?subaction=viewrecord&id=L2010844419&from=export. doi:10.1186/s12955-021-01734-8

17. Bailey H, Janssen MF, La Foucade A, Castillo P, Boodraj G. Health-Related Quality of Life Population Norms for Belize Using EQ-5D-5L. Value Health Reg Issues. 2022;29:45–52. doi: 10.1016/j.vhri.2021.09.005.

18. Bailey HH, Janssen MF, Alladin FM, La Foucade A, Varela R, Moreno JA, et al. Evaluating Health Inequality in Five Caribbean Basin Countries Using EQ-5D-5L. Appl Health Econ Health Policy. 2022;20:857–66. doi: 10.1007/s40258-022-00754-9.

19. Stolk E, Ludwig K, Rand K, Van Hout B, Ramos-Goñi JM. Overview, Update, and Lessons Learned From the International EQ-5D-5L Valuation Work: Version 2 of the EQ-5D-5L Valuation Protocol. Value Health. 2019;22:23–30. doi: 10.1016/j.jval.2018.05.010.

20. Xie F, Pickard AS, Krabbe PFM, Revicki D, Viney R, Devlin N, et al. A Checklist for Reporting Valuation Studies of Multi-Attribute Utility-Based Instruments (CREATE) PharmacoEconomics. 2015;33:867–77. doi: 10.1007/s40273-015-0292-9.

21. Janssen BMF, Oppe M, Versteegh MM, Stolk EA. Introducing the composite time trade-off: a test of feasibility and face validity. Eur J Health Econ. 2013;14:5–13. doi: 10.1007/s10198-013-0503-2.

22. Wong ELY, Ramos-Goñi JM, Cheung AWL, Wong AYK, Rivero-Arias O. Assessing the Use of a Feedback Module to Model EQ-5D-5L Health States Values in Hong Kong. Patient. 2018;11:235–47. doi: 10.1007/s40271-017-0278-0.

23. Oppe M, Norman R, Yang Z, Van Hout B. Experimental Design for the Valuation of the EQ-5D-5L. In: Devlin N, Roudijk B, Ludwig K, editors. Value Sets for EQ-5D-5L. Cham: Springer International Publishing; 2022. p. 29–54. Available from: https://link.springer.com/10.1007/978-3-030-89289-0_3. Cited 2023 Aug 10.

24. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJV, Stolk E. Quality Control Process for EQ-5D-5L Valuation Studies. Value in Health. 2017;20:466–73. doi: 10.1016/j.jval.2016.10.012.

25. Ramos-Goñi JM, Pinto-Prades JL, Oppe M, Cabasés JM, Serrano-Aguilar P, Rivero-Arias O. Valuation and Modeling of EQ-5D-5L Health States Using a Hybrid Approach. Med Care. 2017;55:e51–8. doi: 10.1097/MLR.0000000000000283.

26. Al Shabasy S, Roudijk B, Abbassi M, Finch A, Stolk E, Farid S. The Egyptian EQ-5D-5L Extensive Pilot Study: Lessons Learned. PharmacoEconomics. 2023;41:329–38. doi: 10.1007/s40273-022-01208-9.

27. Webb EJD, Kind P, Meads D, Martin A. COVID-19 and EQ-5D-5L health state valuation. Eur J Health Econ. 2023. Available from: https://link.springer.com/10.1007/s10198-023-01569-8. Cited 2023 Nov 29.

28. Law EH, Pickard AS, Xie F, Walton SM, Lee TA, Schwartz A. Parallel Valuation: A Direct Comparison of EQ-5D-3L and EQ-5D-5L Societal Value Sets. Med Decis Making. 2018;38:968–82. doi: 10.1177/0272989X18802797.

29. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F, et al. United States Valuation of EQ-5D-5L Health States Using an International Protocol. Value Health. 2019;22:931–41. doi: 10.1016/j.jval.2019.02.009.

30. Sayah FA, Bansback N, Bryan S, Ohinmaa A, Poissant L, Pullenayegum E, et al. Determinants of time trade-off valuations for EQ-5D-5L health states: data from the Canadian EQ-5D-5L valuation study. Qual Life Res. 2016;25:1679–85. doi: 10.1007/s11136-015-1203-4.

31. Dolan P, Roberts J. To what extent can we explain time trade-off values from other information about respondents? Soc Sci Med. 2002;54:919–29. doi: 10.1016/S0277-9536(01)00066-1.

32. Tobin J. Estimation of relationships for limited dependent variables. Econometrica: journal of the Econometric Society. 1958;26:24–36.

33. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F, ..., Busschbach JJ. United States valuation of EQ-5D-5L health states using an international protocol. Value Health. 2019;22(8):931–941. doi:10.1016/j.jval.2019.02.009

34. McFadden D. Conditional logit analysis of qualitative choice behavior. 1973.

35. Ramos-Goñi J, Craig AM, Oppe M, Van Hout B. Improving the Valuation of the EQ-5D-5L by Introducing Quality Control and Integrating TTO and DCE. 2016. Combining continuous and dichotomous responses in a hybrid model; p. 133.

## Associated Data

### Data Availability Statement

The data that support the findings of this study are available from the corresponding author, but restrictions apply to the availability of these data, which are not publicly available. The data are, however, available from the authors upon reasonable request.

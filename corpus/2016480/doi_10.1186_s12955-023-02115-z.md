---
project_id: "2016480"
work_id: "doi:10.1186/s12955-023-02115-z"
doi: "10.1186/s12955-023-02115-z"
pmid: "37038172"
pmcid: "PMC10084671"
title: "Experience-based health state valuation using the EQ VAS: a register-based study of the EQ-5D-3L among nine patient groups in Sweden"
journal: "Health and Quality of Life Outcomes"
publication_date: "2023-04-10"
volume: "21"
authors:
  - name: "Fitsum Sebsibe Teni"
    affiliation_ids:
      - "Aff1"
  - name: "Kristina Burström"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Nancy Devlin"
    affiliation_ids:
      - "Aff3"
      - "Aff4"
  - name: "David Parkin"
    affiliation_ids:
      - "Aff4"
      - "Aff5"
  - name: "Ola Rolfson"
    affiliation_ids:
      - "Aff1"
      - "Aff6"
      - "Aff7"
  - name: "The Swedish Quality Register (SWEQR) Study Group"
affiliations:
  - id: "Aff1"
    name: "Health Outcomes and Economic Evaluation Research Group, Department of Learning, Informatics, Management and Ethics, Stockholm Centre for Healthcare Ethics, KarolinskaInstitutet, Stockholm, Sweden"
  - id: "Aff2"
    name: "Equity and Health Policy Research Group, Department of Global Public Health, Karolinska Institutet, Stockholm, Sweden"
  - id: "Aff3"
    name: "Centre for Health Policy, University of Melbourne, Melbourne, Australia"
  - id: "Aff4"
    name: "Office of Health Economics, London, UK"
  - id: "Aff5"
    name: "City University of London, London, UK"
  - id: "Aff6"
    name: "Swedish Arthroplasty Register, Gothenburg, Sweden"
  - id: "Aff7"
    name: "Department of Orthopaedics, Institute of Clinical Sciences, Sahlgrenska Academy, University of Gothenburg, Gothenburg, Sweden"
licence: "cc-by"
source_file: "input/projects/2016480/papers/doi_10.1186_s12955-023-02115-z.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10084671/fullTextXML"
source_method: "epmc_xml"
source_sha256: "929bbaab8f44781b4f9b8740ed94fea60de80a0d59b90a26dadad9955a4c9c6c"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Experience-based health state valuation using the EQ VAS: a register-based study of the EQ-5D-3L among nine patient groups in Sweden

## Abstract

### Background

The EQ VAS component of the EQ-5D questionnaire has been used to assess patients’ valuation of their own health besides its use for self-reporting of overall health status. The objective of the present study was to identify patients’ valuation of EQ-5D-3L health states using the EQ VAS in different patient groups over time and in comparison to the general population.

### Methods

Data were obtained from patients from nine National Quality Registers (*n* = 172,070 patients) at baseline and at 1-year follow-up and compared with data from the general population (*n* = 41,761 participants). The correlation between EQ VAS scores and EQ-5D-3L index based on the Swedish experience-based VAS value set was assessed. Ordinary least squares (OLS) regression models were used to determine the association between EQ-5D-3L dimensions and EQ VAS valuation.

### Results

EQ VAS scores showed consistency with severity of health states both at baseline and at 1-year follow-up in the nine selected EQ-5D-3L health states. The regression models showed mostly consistent decrements by severity levels in each dimension at both time points and similar to the general population. The dimension mainly associated with inconsistency was the self-care severity level three. Problems in the anxiety/depression dimension had the largest impact on overall health status in most of the patient groups and the general population.

### Conclusion

The study has demonstrated the important role EQ VAS can play in revealing patients’ valuation of their health and showed the variation in valuation of EQ-5D-3L dimensions and levels of severity across different patient groups.

### Supplementary Information

The online version contains supplementary material available at 10.1186/s12955-023-02115-z.

**Keywords:** EQ-5D, EQ VAS, Experience-based values, Patient valuation, Swedish National Quality Registers, Health state valuation

Received 2022 Dec 20; Accepted 2023 Mar 22; Collection date 2023.

## Background

EQ-5D is among the most commonly used generic health-related quality of life questionnaires globally \[1\]. It has been used to assess health status, as an outcome measure in economic evaluations, in health surveys among the general population and increasingly in routine data collection as part of clinical/health care \[2\]. The questionnaire has two components: a five-dimension descriptive system and a second component containing the EQ VAS \[3\]. The five dimensions in the descriptive system are mobility, self-care, usual activities, pain/discomfort and anxiety/depression. The EQ VAS component contains a scaled vertical line ranging from 0 (‘the worst health you can imagine’) to 100 (‘the best health you can imagine’) where respondents rate their overall health status \[4, 5\]. The questionnaire is available in three-level (EQ-5D-3L) and five-level (EQ-5D-5L) versions for use in adults. The three severity levels in the EQ-5D-3L questionnaire are ‘no problem’, ‘some/moderate problems’ and ‘unable to/extreme problems’. Individuals who report no problems in all the five dimensions of EQ-5D-3L are described to have a health state of 11111, while those with some/moderate problems across the dimensions have a health state of 22222 and 33333 for ones with severe problems across the dimensions \[4\]. The five severity levels in the EQ-5D-5L are ‘no problems’, ‘slight problems’, ‘moderate problems’, ‘severe problems’ and ‘unable to/extreme problems’ \[5\].

In summarizing responses to the EQ-5D questionnaire into a single index, various formulas/algorithms termed value sets are employed in different settings \[4\]. Value sets incorporate the preferences of respondents, reflecting their views about the relative importance of severity levels under each EQ-5D dimension. In the development of value sets for the EQ-5D-3L in different settings, the time trade-off (TTO) and visual analogue scale (VAS) valuation methods have been employed \[4\]. In valuations through the TTO, respondents are asked to compare living in a specific health state for specific period of time, often 10 years, with living for shorter duration with full health. Through iterations with different durations in full health, the point at which respondents are indifferent describe their values for the specified health state \[6, 7\]. Valuation using the TTO has also been presented by asking respondents to indicate the duration of time in full health they consider to be equal to living in their current health \[8–12\].

VAS is used to value health states; whereas the EQ VAS is used to measure overall self-reported health. EQ VAS was introduced as a warm-up task in valuation studies using the VAS, and subsequently became recognised as a useful way of capturing overall self-reported health \[13\]. Both the EQ VAS and VAS valuations make use of a vertical scale anchored between 0 as the ‘worst imaginable health’ and 100 as the ‘best imaginable health’ indicating that 0 doesn’t equal death \[4, 5\]. VAS (EQ-5D VAS) is used in the valuation of a number of described health states which may be hypothetical to the respondent \[14\]. Unlike in EQ VAS for self-reporting of health, in VAS valuations anchoring dead at zero, which allows worse than death states to have values less than zero, is commonly performed \[15\]. EQ VAS has also been recognised to present a means by which valuations of own (experienced) health of the general population as well as patients can be summarised, which has been shown in several studies \[8, 9, 16–19\].

Arguments for and against VAS as a valuation method have been made. Some consider that VAS does not have a theoretical basis and that it is not a choice-based method unlike other valuation approaches such as TTO and standard gamble (SG) \[20, 21\]. VAS not being a choice-based method has been criticized for not allowing respondents the trade-off which is argued as important for valuation methods to be used in economic evaluation. In addition, the fact that VAS valuation doesn’t incorporate uncertainty which is considered a desired attribute in valuation is criticized and has been associated with lower/downward valuations compared to TTO and SG \[20, 22, 23\]. Another criticism raised concerns the middle point bias/end-aversion bias where respondents avoid the lower and upper ends of the VAS scale \[20, 21\]. However, arguments for the use of VAS in health state valuation challenge the above views and indicate that empirical performance of valuation methods should be focused on in assessing their performance in health state valuation \[24\]. The practical role of VAS in health state valuation was also demonstrated in a recent scoping review which showed its use in different research areas including clinical studies \[25\].

The perspective respondents take in valuation studies could be experience-based or hypothetical. In a hypothetical perspective, respondents value a sub-set of health states described in the EQ-5D instrument, which they may never have experienced themselves and are asked to imagine experiencing. Most EQ-5D-3L and EQ-5D-5L value sets were developed through members of the general public being asked to take this hypothetical perspective \[4, 5\]. The arguments toward the use of hypothetical perspective point to the fact that resource allocation in society should be made by the general population \[22, 26\]. In contrast, experience-based valuations entail respondents valuing their own health \[27\]. It has been employed in the development of a number of EQ-5D-3L \[8, 17, 19\] and EQ-5D-5L \[9, 18\] value sets as well as health state valuations among patients \[16, 28, 29\]. Arguments for the use of experience-based valuations concern the idea that individuals experiencing specific condition/health state are the best sources of information regarding that \[22, 26\].

EQ VAS has been employed to assess both general population values and patient valuations of their health in different studies. In using EQ VAS data to create experience-based values, EQ VAS scores are modelled based on the levels of severity reported in the five EQ-5D dimensions \[16, 28, 30–34\]. Studies using this approach include a study in the UK comparing VAS valuations in the general population and patients with different conditions \[30\]; a comparison of valuations of patients undergoing total hip arthroplasty with the general population \[16\]; and exploration of value sets among patients undergoing total knee replacement, both in the UK \[31\]. Another study used EQ VAS to establish values of patients with non-specific low-back pain compared to the general population in the Netherlands \[32\]; and valuations among patients with different medical conditions in the UK \[33, 34\]. A study in Sweden comparing patient value sets from individuals who underwent total hip arthroplasty with general population ones \[28\] also employed the EQ VAS. However, in the valuation of health states using the EQ VAS a literature gap remains in comparing how valuation varies across different EQ-5D-3L dimensions within patient groups over time and across different patient groups.

In Sweden, there are approximately 100 National Quality Registers (NQRs) which collect clinical data on individual patients with the aim of improving the quality of health care provided to them. As part of this, the data in the registers are employed in research. In about 40 of the registers, data on the EQ-5D questionnaire is collected routinely, including patients’ EQ VAS \[35\]. With their large sample sizes in different patient groups, these registers provide useful data sources to assess patients’ valuations of own health states.

Studying the NQR data in investigating the characteristics of patient valuations using the EQ VAS in different patient groups and over time could contribute to the literature on the importance of different EQ-5D-3L dimensions to patients in influencing their EQ VAS score. Such a study will also provide information on the relative importance of different dimensions in various patient groups and how this compares to that of the general population. Overall, the study could provide comprehensive information on the role of the EQ VAS in patient valuation of health states. Accordingly, the objective of the present study was to identify patients’ valuation of EQ-5D-3L health states using the EQ VAS in different patient groups over time and in comparison to the general population.

## Methods

### Study design

EQ VAS data of patients from nine Swedish NQRs at baseline and 1-year follow-up were assessed and compared with the general population. The present study forms part of the research project described in a study protocol published elsewhere, containing detailed information on the background and the NQRs in the study \[36\]. It follows up on a previous study in the project \[37\].

### Data

Data from nine Swedish NQRs and the general population were employed in the study. The nine registers were selected from those collecting EQ-5D data to include different types of diseases and conditions to make comparisons possible. The availability of EQ VAS data covering patients in the registers; availability of follow-up data as well as willingness of registers to be part of the research project also determined the selection of registers included in the study. The NQRs include six intervention-based registers covering spine surgery, hip, knee, ankle replacement, cruciate ligament injury treatment, and first-line osteoarthritis (Better management of patients with OsteArthritis (BOA)) treatment, and three diagnosis-based registers covering heart failure, respiratory failure, and bipolar disorders. Data on patient-reported outcomes on the EQ-5D-3L questionnaire were retrieved from the NQRs as well as the general population in the study.

EQ VAS data both at baseline and at 1-year follow-up were included to capture patient valuations in different circumstances which could provide clearer information on how one’s valuation of health changes in relation to the change in the disease/condition over time.

The general population data used in the comparison were based on the population survey data of individuals in Scania Region in 2004 and Region Stockholm in 2006, which are generally representative of the Swedish population. Living conditions and self-reported health, which included the EQ-5D-3L questionnaire, were assessed \[8, 38–40\]. The Swedish experience-based EQ-5D-3L value sets were developed using this survey data \[38, 40\]. In the present study, data of 41,761 respondents with complete data on the five EQ-5D-3L dimensions and EQ VAS were included \[8\].

In the present study, in calculating EQ-5D-3L index the Swedish experience-based EQ-5D-3L VAS value set was used \[8\]. This value set was developed in the above described survey where members of the general population valued their own health states through both TTO and VAS methods \[8\].

### Sample size

The study included records of patients with complete data on demographic and EQ-5D-3L data. Data of patients with complete data on EQ VAS score were included at baseline and 1-year follow-up. A total of 172,070 patient records are available from the nine NQRs with data on EQ VAS score and data from a total of 41,761 participants from the general population. A detailed description of the sampling procedure is presented in Table S<a href="#MOESM1" data-ref-type="supplementary-material">1</a>.

### Data analysis

Descriptive analyses on the frequency and proportions of demographic characteristics and problems reported in the five EQ-5D-3L dimensions in each patient group and the general population were performed. The mean and standard deviations of patients’ EQ VAS scores for nine selected EQ-5D-3L health states were calculated in each patient group at baseline and at 1-year follow-up and for the general population. Six of the nine EQ-5D-3L health states were selected as they were common across different patient groups facilitating comparisons of valuations. In addition, the health states 11111, 22222 and 33333 were also selected to compare valuations of full, moderate, and worst health states across patient groups. Considering the association of problems reported on the EQ-5D-3L dimensions with the EQ VAS, the EQ VAS score has been used in the present study as a valuation of the health states reported on the EQ-D-3L dimensions. Owing to the broader construct of EQ VAS than the EQ-5D descriptive system \[13\], a person reporting a health state 11111 could still report an EQ VAS score of \< 100.

The correlation between EQ VAS score and the EQ-5D-3L index based on the Swedish experience-based EQ-5D-3L VAS value set \[8\], in each register and the general population, was analysed using Spearman’s rank correlation. The correlation between changes in EQ VAS score and EQ-5D-3L index was also performed additionally. Spearman’s rank correlation is used as it does not require normality of distribution of the variables \[41\]. The resulting correlation coefficients were interpreted using the cut-off values of 0.00 to 0.19 as very weak, 0.20 to 0.39 as weak, 0.40 to 0.69 as moderate, 0.70 to 0.89 as strong, and 0.90 to 1.00 as very strong \[42\].

Ordinary least squares (OLS) models were used to assess the predictive effect of EQ-5D-3L dimensions on EQ VAS score at baseline and at 1-year follow-up in the nine NQRs. The regression models were performed both in the unadjusted form and adjusted for sex and age groups. The results of the regression analyses were compared with that of the general population in terms of the estimates in each of the EQ-5D-3L dimensions and the severity levels of the problems reported in each dimension. In assessing the face validity of the models, inconsistency was defined as the occurrence of a lower magnitude of decrement for a specific severity level in an EQ-5D-3L dimension than the decrement of a milder level of severity (e.g. if self-care level 3 has a lower decrement than self-care level 2, it is considered an inconsistency). Further OLS models were also performed using the pooled patient data at baseline and 1-year follow-up to assess how patient groups are associated with VAS valuation. In addition to OLS models, multilevel models (two-level random slope and random intercept models) were also performed. A p-value of 0.05 was used as a cut-off for statistical significance. In order to assess the overall translatability of the findings in the analysis here, regression models of baseline and 1-year follow-up EQ-5D-5L data were conducted. The analyses were performed using R version 3.5.0/3.5.1 and SAS version 9.4.

## Results

### Demographic characteristics

The mean age of the patients in the nine registers ranged from about 30 in cruciate ligament injury to older than 73 years among respiratory failure patients, while the mean age was 45.5 years in the general population. In most of the registers, the majority of patients were in the age groups of 50s to 70s while from 30s to 50s in the general population. Women constituted the majority in five of the registers, similar to the general population, except in ankle, cruciate ligament injury and heart failure registers (Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Demographic characteristics of patients in the 9 National Quality Registers (NQRs) and in the general population

</div>

<table>
<thead>
<tr>
<th rowspan="4" style="text-align: left;">Variable</th>
<th colspan="6" style="text-align: left;">Intervention-based registers</th>
<th colspan="3" style="text-align: left;">Diagnosis-based registers</th>
<th rowspan="2" style="text-align: left;">General population</th>
</tr>
<tr>
<th style="text-align: left;"><strong>Spine</strong></th>
<th style="text-align: left;"><strong>Hip</strong></th>
<th style="text-align: left;"><strong>Knee</strong></th>
<th style="text-align: left;"><strong>Ankle</strong></th>
<th style="text-align: left;"><strong>Cruciate ligament</strong></th>
<th style="text-align: left;"><strong>BOA</strong></th>
<th style="text-align: left;"><strong>Heart failure</strong></th>
<th style="text-align: left;"><strong>Respiratory failure</strong></th>
<th style="text-align: left;"><strong>Bipolar</strong></th>
</tr>
<tr>
<th style="text-align: left;"><em>n</em> = 44,196</th>
<th style="text-align: left;"><em>n</em> = 90,658</th>
<th style="text-align: left;"><em>n</em> = 16,324</th>
<th style="text-align: left;"><em>n</em> = 668</th>
<th style="text-align: left;"><em>n</em> = 8,155</th>
<th style="text-align: left;"><em>n</em> = 6,690</th>
<th style="text-align: left;"><em>n</em> = 1,044</th>
<th style="text-align: left;"><em>n</em> = 725</th>
<th style="text-align: left;"><em>n</em> = 3,610</th>
<th style="text-align: left;"><em>n</em> = 41,761</th>
</tr>
<tr>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><strong>Age in years</strong></p>
<p>[mean (SD)]</p></td>
<td style="text-align: left;">58.4 (4.3)</td>
<td style="text-align: left;">68.5 (10.3)</td>
<td style="text-align: left;">68.9 (8.7)</td>
<td style="text-align: left;">63.0 (11.7)</td>
<td style="text-align: left;">29.7 (10.0)</td>
<td style="text-align: left;">65.8 (9.0)</td>
<td style="text-align: left;">71.8 (11.1)</td>
<td style="text-align: left;"><p>73.2</p>
<p>(7.7)</p></td>
<td style="text-align: left;">58.4 (15.3)</td>
<td style="text-align: left;">45.5 (14.9)</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><strong>Age group</strong></td>
</tr>
<tr>
<td style="text-align: left;"> 30</td>
<td style="text-align: left;">3.6</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">1.5</td>
<td style="text-align: left;">59.2</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">15.0</td>
<td style="text-align: left;">17.1</td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td style="text-align: left;">9.9</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">3.0</td>
<td style="text-align: left;">21.2</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">18.8</td>
<td style="text-align: left;">20.4</td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td style="text-align: left;">16.2</td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">1.7</td>
<td style="text-align: left;">7.5</td>
<td style="text-align: left;">15.3</td>
<td style="text-align: left;">4.3</td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">20.7</td>
<td style="text-align: left;">20.8</td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td style="text-align: left;">18.5</td>
<td style="text-align: left;">13.0</td>
<td style="text-align: left;">13.1</td>
<td style="text-align: left;">21.1</td>
<td style="text-align: left;">4.1</td>
<td style="text-align: left;">17.3</td>
<td style="text-align: left;">10.6</td>
<td style="text-align: left;">4.6</td>
<td style="text-align: left;">18.9</td>
<td style="text-align: left;">21.6</td>
</tr>
<tr>
<td style="text-align: left;"> 60–69</td>
<td style="text-align: left;">24.1</td>
<td style="text-align: left;">33.4</td>
<td style="text-align: left;">35.6</td>
<td style="text-align: left;">33.5</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">43.8</td>
<td style="text-align: left;">22.6</td>
<td style="text-align: left;">26.2</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;">14.9</td>
</tr>
<tr>
<td style="text-align: left;"> 70–79</td>
<td style="text-align: left;">21.7</td>
<td style="text-align: left;">35.2</td>
<td style="text-align: left;">38.6</td>
<td style="text-align: left;">30.2</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">28.3</td>
<td style="text-align: left;">35.8</td>
<td style="text-align: left;">47.7</td>
<td style="text-align: left;">7.8</td>
<td style="text-align: left;">4.8</td>
</tr>
<tr>
<td style="text-align: left;"> 80 + </td>
<td style="text-align: left;">6.1</td>
<td style="text-align: left;">13.9</td>
<td style="text-align: left;">11.0</td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">5.6</td>
<td style="text-align: left;">27.2</td>
<td style="text-align: left;">21.2</td>
<td style="text-align: left;">1.3</td>
<td style="text-align: left;">0.4</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><strong>Sex</strong></td>
</tr>
<tr>
<td style="text-align: left;"> Women</td>
<td style="text-align: left;">51.1</td>
<td style="text-align: left;">56.5</td>
<td style="text-align: left;">57.5</td>
<td style="text-align: left;">44.8</td>
<td style="text-align: left;">44.7</td>
<td style="text-align: left;">70.8</td>
<td style="text-align: left;">31.9</td>
<td style="text-align: left;">60.6</td>
<td style="text-align: left;">64.1</td>
<td style="text-align: left;">56.2</td>
</tr>
</tbody>
</table>

*BOA* Better management of patients with OsteoArthritis, *SD* standard deviation

</div>

### Problems reported on the EQ-5D-3L dimensions and EQ VAS score

At baseline, the highest proportion of any problems (level 2 or level 3) were reported in the pain/discomfort dimension among patients in most of the registers and in the general population. Among patients in the respiratory failure and bipolar disorder registers the dimensions with the highest proportions of problems reported were mobility and anxiety/depression respectively. The highest proportions of severe (level 3) problems were also reported in the pain/discomfort dimension across most registers and in the general population. In patients with respiratory failure and bipolar disorder the highest proportions of severe problems were reported in the usual activities and anxiety/depression dimensions respectively (Table <a href="#Tab2" data-ref-type="table">2</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

Problems reported on the EQ-5D-3L dimensions by patients in the 9 National Quality Registers (NQRs) and in the general population

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="4" style="text-align: left;"><strong>Patient group in NQRs/ general population</strong></th>
<th rowspan="4" style="text-align: left;"><strong>Severity level</strong></th>
<th colspan="10" style="text-align: left;"><strong>EQ-5D-3L dimension</strong></th>
<th colspan="2" rowspan="2" style="text-align: left;"><strong>EQ VAS score</strong><br />
Mean (SD)</th>
</tr>
<tr>
<th colspan="5" style="text-align: left;"><strong>Baseline</strong></th>
<th colspan="5" style="text-align: left;"><strong>1-year follow-up</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>Mobility</strong></th>
<th style="text-align: left;"><strong>Self-care</strong></th>
<th style="text-align: left;"><strong>Usual activities</strong></th>
<th style="text-align: left;"><strong>Pain/</strong><br />
<strong>discomfort</strong></th>
<th style="text-align: left;"><strong>Anxiety/</strong><br />
<strong>depression</strong></th>
<th style="text-align: left;"><strong>Mobility</strong></th>
<th style="text-align: left;"><strong>Self-care</strong></th>
<th style="text-align: left;"><strong>Usual activities</strong></th>
<th style="text-align: left;"><strong>Pain/</strong><br />
<strong>discomfort</strong></th>
<th style="text-align: left;"><strong>Anxiety/</strong><br />
<strong>depression</strong></th>
<th rowspan="2" style="text-align: left;"><strong>Baseline</strong></th>
<th rowspan="2" style="text-align: left;"><strong>1-year follow-up</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
<th style="text-align: left;"><strong>%</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="18" style="text-align: left;"><strong>Intervention-based registers</strong></td>
<td rowspan="3" style="text-align: left;"><p><strong>Spine</strong></p>
<p>(<em>n</em> = 44,196)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">15.3</td>
<td style="text-align: left;"><strong>79.7</strong></td>
<td style="text-align: left;">27.7</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">41.9</td>
<td style="text-align: left;"><strong>57.7</strong></td>
<td style="text-align: left;"><strong>91.7</strong></td>
<td style="text-align: left;"><strong>65.9</strong></td>
<td style="text-align: left;">23.0</td>
<td style="text-align: left;"><strong>62.4</strong></td>
<td rowspan="3" style="text-align: left;">47.8 (22.1)</td>
<td rowspan="3" style="text-align: left;">67.9 (22.5)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;"><strong>82.7</strong></td>
<td style="text-align: left;">19.1</td>
<td style="text-align: left;"><strong>53.4</strong></td>
<td style="text-align: left;">49.5</td>
<td style="text-align: left;"><strong>52.1</strong></td>
<td style="text-align: left;">42.1</td>
<td style="text-align: left;">7.8</td>
<td style="text-align: left;">29.8</td>
<td style="text-align: left;"><strong>63.2</strong></td>
<td style="text-align: left;">33.4</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">2.0</td>
<td style="text-align: left;">1.2</td>
<td style="text-align: left;">19.0</td>
<td style="text-align: left;"><strong>49.9</strong></td>
<td style="text-align: left;">6.0</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">4.4</td>
<td style="text-align: left;">13.8</td>
<td style="text-align: left;">4.2</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>Hip</strong></p>
<p>(<em>n</em> = 90,658)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">8.1</td>
<td style="text-align: left;"><strong>77.7</strong></td>
<td style="text-align: left;">40.1</td>
<td style="text-align: left;">1.5</td>
<td style="text-align: left;"><strong>59.7</strong></td>
<td style="text-align: left;"><strong>61.7</strong></td>
<td style="text-align: left;"><strong>92.4</strong></td>
<td style="text-align: left;"><strong>78.0</strong></td>
<td style="text-align: left;">45.5</td>
<td style="text-align: left;"><strong>78.4</strong></td>
<td rowspan="3" style="text-align: left;">56.3 (22.2)</td>
<td rowspan="3" style="text-align: left;">76.7 (20.0)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;"><strong>91.6</strong></td>
<td style="text-align: left;">21.3</td>
<td style="text-align: left;"><strong>50.1</strong></td>
<td style="text-align: left;"><strong>57.9</strong></td>
<td style="text-align: left;">37.1</td>
<td style="text-align: left;">38.1</td>
<td style="text-align: left;">7.0</td>
<td style="text-align: left;">20.0</td>
<td style="text-align: left;"><strong>50.1</strong></td>
<td style="text-align: left;">20.1</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">1.0</td>
<td style="text-align: left;">9.8</td>
<td style="text-align: left;">40.5</td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">2.0</td>
<td style="text-align: left;">4.4</td>
<td style="text-align: left;">1.5</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>Knee</strong></p>
<p>(<em>n</em> = 16,324)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">11.6</td>
<td style="text-align: left;"><strong>93.4</strong></td>
<td style="text-align: left;"><strong>53.4</strong></td>
<td style="text-align: left;">1.8</td>
<td style="text-align: left;"><strong>65.4</strong></td>
<td style="text-align: left;"><strong>62.8</strong></td>
<td style="text-align: left;"><strong>95.1</strong></td>
<td style="text-align: left;"><strong>77.8</strong></td>
<td style="text-align: left;">36.1</td>
<td style="text-align: left;"><strong>78.6</strong></td>
<td rowspan="3" style="text-align: left;">64.6 (22.1)</td>
<td rowspan="3" style="text-align: left;">76.2 (19.4)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;"><strong>88.1</strong></td>
<td style="text-align: left;">5.8</td>
<td style="text-align: left;">41.3</td>
<td style="text-align: left;"><strong>63.3</strong></td>
<td style="text-align: left;">32.2</td>
<td style="text-align: left;">37.1</td>
<td style="text-align: left;">4.4</td>
<td style="text-align: left;">20.6</td>
<td style="text-align: left;"><strong>58.7</strong></td>
<td style="text-align: left;">19.7</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;">5.3</td>
<td style="text-align: left;">35.0</td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">1.7</td>
<td style="text-align: left;">5.2</td>
<td style="text-align: left;">1.7</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>Ankle</strong></p>
<p>(<em>n</em> = 668)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">3.9</td>
<td style="text-align: left;"><strong>88.3</strong></td>
<td style="text-align: left;">37.7</td>
<td style="text-align: left;">1.1</td>
<td style="text-align: left;"><strong>57.5</strong></td>
<td style="text-align: left;">36.7</td>
<td style="text-align: left;"><strong>91.5</strong></td>
<td style="text-align: left;"><strong>63.9</strong></td>
<td style="text-align: left;">24.3</td>
<td style="text-align: left;"><strong>71.4</strong></td>
<td rowspan="3" style="text-align: left;">55.8 (21.4)</td>
<td rowspan="3" style="text-align: left;">70.2 (18.9)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;"><strong>94.5</strong></td>
<td style="text-align: left;">10.8</td>
<td style="text-align: left;"><strong>49.3</strong></td>
<td style="text-align: left;"><strong>49.7</strong></td>
<td style="text-align: left;">38.2</td>
<td style="text-align: left;"><strong>62.9</strong></td>
<td style="text-align: left;">7.5</td>
<td style="text-align: left;">32.2</td>
<td style="text-align: left;"><strong>65.6</strong></td>
<td style="text-align: left;">26.2</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">1.7</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;">13.0</td>
<td style="text-align: left;">49.3</td>
<td style="text-align: left;">4.3</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">1.1</td>
<td style="text-align: left;">3.9</td>
<td style="text-align: left;">10.2</td>
<td style="text-align: left;">2.4</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>Cruciate ligament</strong></p>
<p>(<em>n</em> = 8,155)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;"><strong>67.0</strong></td>
<td style="text-align: left;"><strong>97.4</strong></td>
<td style="text-align: left;"><strong>53.6</strong></td>
<td style="text-align: left;">15.2</td>
<td style="text-align: left;"><strong>49.6</strong></td>
<td style="text-align: left;"><strong>86.9</strong></td>
<td style="text-align: left;"><strong>98.9</strong></td>
<td style="text-align: left;"><strong>79.0</strong></td>
<td style="text-align: left;">35.0</td>
<td style="text-align: left;"><strong>65.2</strong></td>
<td rowspan="3" style="text-align: left;">62.8 (23.0)</td>
<td rowspan="3" style="text-align: left;">74.5 (19.9)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">32.7</td>
<td style="text-align: left;">2.1</td>
<td style="text-align: left;">37.4</td>
<td style="text-align: left;"><strong>79.0</strong></td>
<td style="text-align: left;">44.9</td>
<td style="text-align: left;">13.1</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">19.4</td>
<td style="text-align: left;"><strong>61.9</strong></td>
<td style="text-align: left;">31.5</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">9.0</td>
<td style="text-align: left;">5.7</td>
<td style="text-align: left;">5.5</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;">3.3</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>BOA</strong></p>
<p>(<em>n</em> = 6,690)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">42.9</td>
<td style="text-align: left;"><strong>96.0</strong></td>
<td style="text-align: left;"><strong>75.6</strong></td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;"><strong>67.0</strong></td>
<td style="text-align: left;"><strong>53.3</strong></td>
<td style="text-align: left;"><strong>96.2</strong></td>
<td style="text-align: left;"><strong>80.1</strong></td>
<td style="text-align: left;">9.8</td>
<td style="text-align: left;"><strong>71.1</strong></td>
<td rowspan="3" style="text-align: left;">68.3 (18.6)</td>
<td rowspan="3" style="text-align: left;">70.4 (18.7)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;"><strong>57.0</strong></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">23.0</td>
<td style="text-align: left;"><strong>87.3</strong></td>
<td style="text-align: left;">31.7</td>
<td style="text-align: left;">46.6</td>
<td style="text-align: left;">3.4</td>
<td style="text-align: left;">19.2</td>
<td style="text-align: left;"><strong>82.6</strong></td>
<td style="text-align: left;">27.9</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">1.4</td>
<td style="text-align: left;">10.3</td>
<td style="text-align: left;">1.2</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">7.6</td>
<td style="text-align: left;">1.1</td>
</tr>
<tr>
<td rowspan="9" style="text-align: left;"><strong>Diagnosis-based registers</strong></td>
<td rowspan="3" style="text-align: left;"><p><strong>Heart failure</strong></p>
<p>(<em>n</em> = 1,044)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;"><strong>60.6</strong></td>
<td style="text-align: left;"><strong>91.9</strong></td>
<td style="text-align: left;"><strong>72.6</strong></td>
<td style="text-align: left;"><strong>47.7</strong></td>
<td style="text-align: left;"><strong>60.3</strong></td>
<td style="text-align: left;"><strong>59.3</strong></td>
<td style="text-align: left;"><strong>91.3</strong></td>
<td style="text-align: left;"><strong>72.8</strong></td>
<td style="text-align: left;"><strong>49.2</strong></td>
<td style="text-align: left;"><strong>62.7</strong></td>
<td rowspan="3" style="text-align: left;">65.4 (18.9)</td>
<td rowspan="3" style="text-align: left;">67.4 (18.8)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">39.2</td>
<td style="text-align: left;">7.7</td>
<td style="text-align: left;">24.0</td>
<td style="text-align: left;">47.5</td>
<td style="text-align: left;">36.6</td>
<td style="text-align: left;">40.2</td>
<td style="text-align: left;">8.0</td>
<td style="text-align: left;">24.2</td>
<td style="text-align: left;">43.5</td>
<td style="text-align: left;">34.4</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">3.5</td>
<td style="text-align: left;">4.8</td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">3.0</td>
<td style="text-align: left;">7.3</td>
<td style="text-align: left;">2.9</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>Respiratory failure</strong></p>
<p>(<em>n</em> = 725)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">22.8</td>
<td style="text-align: left;"><strong>62.3</strong></td>
<td style="text-align: left;">25.9</td>
<td style="text-align: left;">29.0</td>
<td style="text-align: left;">42.1</td>
<td style="text-align: left;">17.0</td>
<td style="text-align: left;"><strong>53.4</strong></td>
<td style="text-align: left;">19.5</td>
<td style="text-align: left;">23.9</td>
<td style="text-align: left;">37.5</td>
<td rowspan="3" style="text-align: left;">51.1 (21.3)</td>
<td rowspan="3" style="text-align: left;">49.1 (20.4)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;"><strong>75.6</strong></td>
<td style="text-align: left;">32.4</td>
<td style="text-align: left;"><strong>53.8</strong></td>
<td style="text-align: left;"><strong>57.7</strong></td>
<td style="text-align: left;"><strong>49.0</strong></td>
<td style="text-align: left;"><strong>79.0</strong></td>
<td style="text-align: left;">38.5</td>
<td style="text-align: left;"><strong>50.5</strong></td>
<td style="text-align: left;"><strong>60.0</strong></td>
<td style="text-align: left;"><strong>52.3</strong></td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">1.7</td>
<td style="text-align: left;">5.2</td>
<td style="text-align: left;">20.3</td>
<td style="text-align: left;">13.4</td>
<td style="text-align: left;">9.0</td>
<td style="text-align: left;">4.0</td>
<td style="text-align: left;">8.1</td>
<td style="text-align: left;">30.1</td>
<td style="text-align: left;">16.1</td>
<td style="text-align: left;">10.2</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><strong>Bipolar</strong></p>
<p>(<em>n</em> = 3,610)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;"><strong>85.7</strong></td>
<td style="text-align: left;"><strong>94.9</strong></td>
<td style="text-align: left;"><strong>70.3</strong></td>
<td style="text-align: left;"><strong>53.0</strong></td>
<td style="text-align: left;">38.4</td>
<td style="text-align: left;"><strong>82.5</strong></td>
<td style="text-align: left;"><strong>93.7</strong></td>
<td style="text-align: left;"><strong>69.5</strong></td>
<td style="text-align: left;"><strong>50.6</strong></td>
<td style="text-align: left;">39.6</td>
<td rowspan="3" style="text-align: left;">66.3 (21.1)</td>
<td rowspan="3" style="text-align: left;">67.2 (20.1)</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">14.1</td>
<td style="text-align: left;">4.7</td>
<td style="text-align: left;">26.0</td>
<td style="text-align: left;">40.3</td>
<td style="text-align: left;"><strong>50.6</strong></td>
<td style="text-align: left;">17.0</td>
<td style="text-align: left;">5.8</td>
<td style="text-align: left;">26.5</td>
<td style="text-align: left;">41.6</td>
<td style="text-align: left;"><strong>49.8</strong></td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">6.8</td>
<td style="text-align: left;">11.0</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">4.1</td>
<td style="text-align: left;">7.8</td>
<td style="text-align: left;">10.5</td>
</tr>
<tr>
<td colspan="2" rowspan="3" style="text-align: left;"><p><strong>General population</strong></p>
<p>(<em>n</em> = 41,761)</p></td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;"><strong>91.3</strong></td>
<td style="text-align: left;"><strong>98.6</strong></td>
<td style="text-align: left;"><strong>91.6</strong></td>
<td style="text-align: left;"><strong>53.5</strong></td>
<td style="text-align: left;"><strong>68.4</strong></td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td rowspan="3" style="text-align: left;"><p>79.5</p>
<p>(18.3)</p></td>
<td rowspan="3" style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">8.6</td>
<td style="text-align: left;">1.1</td>
<td style="text-align: left;">7.3</td>
<td style="text-align: left;">42.7</td>
<td style="text-align: left;">29.0</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">1.1</td>
<td style="text-align: left;">3.8</td>
<td style="text-align: left;">2.7</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
</tbody>
</table>

*BOA* Better management of patients with OsteoArthritis, *SD* standard deviation; level 1: no problem; level 2: some/moderate problems; level 3: confined to bed/unable to/ extreme problems; the level with the highest proportion in each group is shown in bold

</div>

At 1-year follow-up the proportion of problems reported across the EQ-5D-3L dimensions decreased in almost all the patient groups. Pain/discomfort remained the dimension where the highest proportions of any problems were reported in most registers. In respiratory failure and bipolar disorder registers, the highest proportions of problems were reported in the mobility and anxiety/depression dimensions respectively. The most frequent severe problems were also reported in the pain/discomfort dimension in most registers while anxiety/depression dimension constituted the most frequent problems in cruciate ligament injury and bipolar disorder registers (Table <a href="#Tab2" data-ref-type="table">2</a>).

At baseline, mean EQ VAS score ranged from 47.8 among patients in the spine register to 68.3 among patients in the BOA register, while it was 79.5 in the general population. At 1-year follow-up mean EQ VAS score ranged from 49.1 among respiratory failure patients to 76.7 in patients who underwent hip replacement. Mean EQ VAS scores showed increases between baseline and 1 year in almost all the patient groups with the exception of patients with respiratory failure. The increases were the highest in most of the intervention-based registers (Table <a href="#Tab2" data-ref-type="table">2</a>). Figure <a href="#Fig1" data-ref-type="fig">1</a> shows the distribution of EQ VAS scores across the patient groups at baseline and at 1-year follow-up and that of the general population.

<figure id="Fig1">
<p><img src="12955_2023_2115_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="12955_2023_2115_Fig1_HTML.gif" /></p>
<figcaption>Distribution (density plot) of EQ VAS score by patient group at baseline and at 1-year follow-up and in the general population (general population data, based on a cross-sectional survey) [BOA: Better management of patients with OsteoArthritis]</figcaption>
</figure>

### Mean EQ VAS scores for selected health states

In total, 204 and 202 distinct health states were reported among the nine patient groups at baseline and at 1-year follow-up respectively. In the general population, 152 distinct health states were reported (Table <a href="#Tab3" data-ref-type="table">3</a>).

<div id="Tab3" class="table-wrap">

<div class="caption">

Mean EQ VAS values among nine selected EQ-5D-3L health states across patient groups and the general population, baseline and 1-year follow-up

</div>

<table>
<tbody>
<tr>
<td rowspan="3" style="text-align: left;"><strong>Time</strong></td>
<td rowspan="3" style="text-align: left;"><strong>Health</strong> <strong>state</strong></td>
<td colspan="10" style="text-align: left;"><strong>Mean EQ VAS scores (standard deviation)</strong></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Intervention-based registers</strong></td>
<td colspan="4" style="text-align: left;"><strong>Diagnosis-based registers</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Spine</strong></td>
<td style="text-align: left;"><strong>Hip</strong></td>
<td style="text-align: left;"><strong>Knee</strong></td>
<td style="text-align: left;"><strong>Ankle</strong></td>
<td style="text-align: left;"><strong>Cruciate ligament</strong></td>
<td style="text-align: left;"><strong>BOA</strong></td>
<td style="text-align: left;"><strong>Heart failure</strong></td>
<td style="text-align: left;"><strong>Respiratory failure</strong></td>
<td style="text-align: left;"><strong>Bipolar</strong></td>
<td style="text-align: left;"><strong>General pop</strong></td>
</tr>
<tr>
<td rowspan="10" style="text-align: left;"><strong>Baseline</strong></td>
<td style="text-align: left;">11111</td>
<td style="text-align: left;">78.3 (17.3)</td>
<td style="text-align: left;">75.9 (21.4)</td>
<td style="text-align: left;">81.7 (15.7)</td>
<td style="text-align: left;">82.5 (3.5)</td>
<td style="text-align: left;">78.3 (18.2)</td>
<td style="text-align: left;">87.2 (12.1)</td>
<td style="text-align: left;">76.4 (15.7)</td>
<td style="text-align: left;">68.8 (23.2)</td>
<td style="text-align: left;">82.4 (14.0)</td>
<td style="text-align: left;">88.8 (9.7)</td>
</tr>
<tr>
<td style="text-align: left;">11121</td>
<td style="text-align: left;">69.8 (16.9)</td>
<td style="text-align: left;">73.5 (17.3)</td>
<td style="text-align: left;">80.8 (15.2)</td>
<td style="text-align: left;">73.9 (20.7)</td>
<td style="text-align: left;">72.8 (19.4)</td>
<td style="text-align: left;">78.1 (14.3)</td>
<td style="text-align: left;">72.1 (16.4)</td>
<td style="text-align: left;">61.9 (24.1)</td>
<td style="text-align: left;">77.9 (14.0)</td>
<td style="text-align: left;">82.5 (11.6)</td>
</tr>
<tr>
<td style="text-align: left;">21121</td>
<td style="text-align: left;">64.0 (17.4)</td>
<td style="text-align: left;">67.6 (17.8)</td>
<td style="text-align: left;">73.1 (17.9)</td>
<td style="text-align: left;">69.3 (16.1)</td>
<td style="text-align: left;">64.0 (20.7)</td>
<td style="text-align: left;">71.2 (16.1)</td>
<td style="text-align: left;">66.8 (13.2)</td>
<td style="text-align: left;">60.6 (15.6)</td>
<td style="text-align: left;">75.8 (12.2)</td>
<td style="text-align: left;">72.0 (17.0)</td>
</tr>
<tr>
<td style="text-align: left;">21122</td>
<td style="text-align: left;">56.3 (17.0)</td>
<td style="text-align: left;">59.8 (16.9)</td>
<td style="text-align: left;">63.8 (17.8)</td>
<td style="text-align: left;">61.2 (17.5)</td>
<td style="text-align: left;">54.5 (21.9)</td>
<td style="text-align: left;">62.9 (16.2)</td>
<td style="text-align: left;">57.1 (16.7)</td>
<td style="text-align: left;">57.3 (23.0)</td>
<td style="text-align: left;">58.8 (18.9)</td>
<td style="text-align: left;">59.7 (18.2)</td>
</tr>
<tr>
<td style="text-align: left;">21221</td>
<td style="text-align: left;">57.2 (17.7)</td>
<td style="text-align: left;">61.9 (18.0)</td>
<td style="text-align: left;">67.2 (18.4)</td>
<td style="text-align: left;">60.6 (17.9)</td>
<td style="text-align: left;">60.6 (22.5)</td>
<td style="text-align: left;">63.8 (16.0)</td>
<td style="text-align: left;">57.7 (14.7)</td>
<td style="text-align: left;">52.6 (19.0)</td>
<td style="text-align: left;">70.8 (14.9)</td>
<td style="text-align: left;">59.8 (18.7)</td>
</tr>
<tr>
<td style="text-align: left;">21222</td>
<td style="text-align: left;">49.8 (16.6)</td>
<td style="text-align: left;">54.2 (16.9)</td>
<td style="text-align: left;">57.9 (18.3)</td>
<td style="text-align: left;">57.4 (13.5)</td>
<td style="text-align: left;">51.9 (20.7)</td>
<td style="text-align: left;">54.6 (16.2)</td>
<td style="text-align: left;">52.0 (15.2)</td>
<td style="text-align: left;">48.7 (14.7)</td>
<td style="text-align: left;">56.0 (14.5)</td>
<td style="text-align: left;">51.7 (17.7)</td>
</tr>
<tr>
<td style="text-align: left;">21232</td>
<td style="text-align: left;">39.8 (19.6)</td>
<td style="text-align: left;">45.1 (20.6)</td>
<td style="text-align: left;">49.4 (21.5)</td>
<td style="text-align: left;">47.6 (19.4)</td>
<td style="text-align: left;">43.4 (22.5)</td>
<td style="text-align: left;">49.7 (19.3)</td>
<td style="text-align: left;">42.7 (14.9)</td>
<td style="text-align: left;">51.4 (26.1)</td>
<td style="text-align: left;">46.8 (17.7)</td>
<td style="text-align: left;">38.4 (16.4)</td>
</tr>
<tr>
<td style="text-align: left;">22222</td>
<td style="text-align: left;">45.8 (17.6)</td>
<td style="text-align: left;">51.7 (17.2)</td>
<td style="text-align: left;">50.1 (18.1)</td>
<td style="text-align: left;">52.0 (5.7)</td>
<td style="text-align: left;">46.6 (20.1)</td>
<td style="text-align: left;">51.2 (17.2)</td>
<td style="text-align: left;">51.5 (24.0)</td>
<td style="text-align: left;">50.3 (17.8)</td>
<td style="text-align: left;">53.0 (18.6)</td>
<td style="text-align: left;">44.4 (17.3)</td>
</tr>
<tr>
<td style="text-align: left;">33333</td>
<td style="text-align: left;">13.3 (20.4)</td>
<td style="text-align: left;">22.3 (26.2)</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">36.7 (45.9)</td>
</tr>
<tr>
<td style="text-align: left;">Total number of health states</td>
<td style="text-align: left;">168</td>
<td style="text-align: left;">169</td>
<td style="text-align: left;">108</td>
<td style="text-align: left;">51</td>
<td style="text-align: left;">103</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">69</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">102</td>
<td style="text-align: left;">152</td>
</tr>
<tr>
<td rowspan="13" style="text-align: left;"><strong>1-year follow-up</strong></td>
<td rowspan="3" style="text-align: left;"><strong>Heaath state</strong></td>
<td colspan="10" style="text-align: left;"><strong>Mean EQ VAS scores (standard deviation)</strong></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Intervention-based registers</strong></td>
<td colspan="4" style="text-align: left;"><strong>Diagnosis-based registers</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Spine</strong></td>
<td style="text-align: left;"><strong>Hip</strong></td>
<td style="text-align: left;"><strong>Knee</strong></td>
<td style="text-align: left;"><strong>Ankle</strong></td>
<td style="text-align: left;"><strong>Cruciate ligament</strong></td>
<td style="text-align: left;"><strong>BOA</strong></td>
<td style="text-align: left;"><strong>Heart failure</strong></td>
<td style="text-align: left;"><strong>Respiratory failure</strong></td>
<td style="text-align: left;"><strong>Bipolar</strong></td>
<td style="text-align: left;"><strong>-</strong></td>
</tr>
<tr>
<td style="text-align: left;">11111</td>
<td style="text-align: left;">89.2 (10.6)</td>
<td style="text-align: left;">89.9 (11.4)</td>
<td style="text-align: left;">88.8 (11.9)</td>
<td style="text-align: left;">83.6 (11.1)</td>
<td style="text-align: left;">85.5 (14.4)</td>
<td style="text-align: left;">89.2 (11.4)</td>
<td style="text-align: left;">78.5 (14.3)</td>
<td style="text-align: left;">64.2 (23.1)</td>
<td style="text-align: left;">82.5 (12.0)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">11121</td>
<td style="text-align: left;">79.5 (12.3)</td>
<td style="text-align: left;">81.5 (12.3)</td>
<td style="text-align: left;">81.9 (12.4)</td>
<td style="text-align: left;">82.7 (8.5)</td>
<td style="text-align: left;">78.9 (15.1)</td>
<td style="text-align: left;">80.0 (12.2)</td>
<td style="text-align: left;">75.3 (11.5)</td>
<td style="text-align: left;">74.1 (14.1)</td>
<td style="text-align: left;">79.2 (12.7)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">21121</td>
<td style="text-align: left;">69.2 (14.8)</td>
<td style="text-align: left;">73.4 (14.8)</td>
<td style="text-align: left;">73.6 (14.7)</td>
<td style="text-align: left;">73.2 (15.9)</td>
<td style="text-align: left;">71.4 (17.3)</td>
<td style="text-align: left;">69.7 (15.0)</td>
<td style="text-align: left;">69.8 (14.8)</td>
<td style="text-align: left;">64.5 (15.6)</td>
<td style="text-align: left;">76.2 (15.4)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">21122</td>
<td style="text-align: left;">60.2 (15.1)</td>
<td style="text-align: left;">63.5 (15.4)</td>
<td style="text-align: left;">63.5 (16.1)</td>
<td style="text-align: left;">68.0 (11.2)</td>
<td style="text-align: left;">59.8 (20.6)</td>
<td style="text-align: left;">60.0 (14.2)</td>
<td style="text-align: left;">59.5 (16.1)</td>
<td style="text-align: left;">50.9 (24.7)</td>
<td style="text-align: left;">66.7 (15.3)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">21221</td>
<td style="text-align: left;">59.5 (15.9)</td>
<td style="text-align: left;">64.0 (16.1)</td>
<td style="text-align: left;">66.5 (16.5)</td>
<td style="text-align: left;">65.7 (17.3)</td>
<td style="text-align: left;">64.6 (17.7)</td>
<td style="text-align: left;">61.1 (16.0)</td>
<td style="text-align: left;">59.8 (16.6)</td>
<td style="text-align: left;">52.5 (17.5)</td>
<td style="text-align: left;">62.9 (11.9)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">21222</td>
<td style="text-align: left;">52.5 (15.1)</td>
<td style="text-align: left;">55.2 (15.7)</td>
<td style="text-align: left;">57.2 (15.9)</td>
<td style="text-align: left;">59.4 (14.1)</td>
<td style="text-align: left;">55.8 (18.7)</td>
<td style="text-align: left;">53.3 (14.7)</td>
<td style="text-align: left;">54.4 (14.6)</td>
<td style="text-align: left;">49.4 (14.9)</td>
<td style="text-align: left;">54.5 (15.1)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">21232</td>
<td style="text-align: left;">39.1 (17.5)</td>
<td style="text-align: left;">40.4 (17.7)</td>
<td style="text-align: left;">45.4 (20.5)</td>
<td style="text-align: left;">47.4 (20.3)</td>
<td style="text-align: left;">42.7 (19.0)</td>
<td style="text-align: left;">44.3 (19.0)</td>
<td style="text-align: left;">55.6 (14.7)</td>
<td style="text-align: left;">45.8 (6.2)</td>
<td style="text-align: left;">43.5 (15.1)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">22222</td>
<td style="text-align: left;">48.2 (15.8)</td>
<td style="text-align: left;">51.6 (16.6)</td>
<td style="text-align: left;">52.4 (17.4)</td>
<td style="text-align: left;">56.9 (10.7)</td>
<td style="text-align: left;">41.7 (18.9)</td>
<td style="text-align: left;">50.4 (13.3)</td>
<td style="text-align: left;">42.0 (20.5)</td>
<td style="text-align: left;">43.7 (16.6)</td>
<td style="text-align: left;">53.5 (13.9)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">33333</td>
<td style="text-align: left;">16.8 (20.5)</td>
<td style="text-align: left;">26.3 (31.6)</td>
<td style="text-align: left;">39.8 (42.0)</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Total number of health states</td>
<td style="text-align: left;">159</td>
<td style="text-align: left;">184</td>
<td style="text-align: left;">125</td>
<td style="text-align: left;">56</td>
<td style="text-align: left;">82</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">72</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">111</td>
<td style="text-align: left;">-</td>
</tr>
</tbody>
</table>

*BOA* Better management of patients with OsteoArthritis

</div>

Both at baseline and at 1-year follow-up, mean EQ VAS scores of the nine selected EQ-5D-3L health states were higher for milder health states and lower among more severe health states. The increase in EQ VAS scores of the health state 11111 and 11121 from baseline to respective health states at 1-year follow-up was higher in most of the intervention-based registers than in diagnosis-based registers. For both health states, at baseline, the EQ VAS scores in most patient groups were lower than in the general population. At 1-year follow-up, the EQ VAS scores increased to be closer to general population. The differences in EQ VAS score from baseline to 1-year follow-up, in the remaining seven health states, were generally lower than that of the health states 11111 and 11121 (Table <a href="#Tab3" data-ref-type="table">3</a>).

The health state 22222 had mean EQ VAS scores at baseline that varied from 45.8 among spine patients to 53.0 among bipolar patients. At 1-year follow-up it varied from 41.7 in cruciate ligament injury patients to 56.9 in patients in ankle register. Meanwhile, 22222 had a mean EQ VAS score of 44.4 in the general population (Table <a href="#Tab3" data-ref-type="table">3</a>).

### Correlation between EQ VAS score and EQ-5D-3L index

EQ VAS scores reported by patients in each register and the general population were correlated with EQ-5D-3L indices based on the Swedish experience-based EQ-5D-3L VAS value set. At baseline almost all patient groups and the general population showed moderate levels of correlation with the EQ-5D-3L index. At 1-year follow-up, correlation coefficients in all patient groups showed increase from baseline. Correlation coefficients among patients in the spine and hip registers were strong. In all the remaining registers moderate levels of correlation were found (Table <a href="#Tab4" data-ref-type="table">4</a>). The results of the correlation analysis between changes in EQ VAS score and changes in EQ-5D-3L index showed low to moderate levels of correlation across the different patient groups (Table S<a href="#MOESM1" data-ref-type="supplementary-material">2</a>).

<div id="Tab4" class="table-wrap">

<div class="caption">

Spearman’s rank correlation coefficient between EQ VAS score and EQ-5D-3L index based on Swedish experience-based EQ-5D-3L VAS value set

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="3" style="text-align: left;"><strong>Register/ general population</strong></th>
<th colspan="4" style="text-align: left;"><strong>Spearman’s correlation</strong></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><strong>Baseline</strong></th>
<th colspan="2" style="text-align: left;"><strong>1-year follow-up</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>Coefficient</strong></th>
<th style="text-align: left;"><strong><em>P</em>-value</strong></th>
<th style="text-align: left;"><strong>Coefficient</strong></th>
<th style="text-align: left;"><strong><em>P</em>-value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6" style="text-align: left;"><strong>Intervention-based</strong></td>
<td style="text-align: left;"><strong>Spine</strong></td>
<td style="text-align: left;">0.522</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.769</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Hip</strong></td>
<td style="text-align: left;">0.441</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.702</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Knee</strong></td>
<td style="text-align: left;">0.419</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.644</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Ankle</strong></td>
<td style="text-align: left;">0.475</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.638</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Cruciate ligament</strong></td>
<td style="text-align: left;">0.428</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.564</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>BOA</strong></td>
<td style="text-align: left;">0.499</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.640</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><strong>Diagnosis-based</strong></td>
<td style="text-align: left;"><strong>Heart failure</strong></td>
<td style="text-align: left;">0.520</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.562</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Respiratory failure</strong></td>
<td style="text-align: left;">0.400</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.539</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bipolar</strong></td>
<td style="text-align: left;">0.619</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">0.650</td>
<td style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>General population</strong></td>
<td style="text-align: left;">0.596</td>
<td style="text-align: left;"> &lt; 0.0001</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
</tbody>
</table>

*BOA* Better management of patients with OsteoArthritis

</div>

### Regression models of the baseline data

The OLS models of the baseline data showed that EQ-5D-3L dimensions predicted EQ VAS score in a mostly consistent way in most of the NQRs and in the general population data. In seven of the nine NQRs and in the general population, the main inconsistency was in the self-care severity level three with lower decrement than in level two. Additionally, inconsistency in the mobility dimension was shown in the knee and heart failure registers and in the general population. In the respiratory failure and bipolar registers, the inconsistency was in the mobility dimension (Table <a href="#Tab5" data-ref-type="table">5</a>, Fig. S<a href="#MOESM1" data-ref-type="supplementary-material">1</a>).

<div id="Tab5" class="table-wrap">

<div class="caption">

Ordinary least squares regressions in the 9 registers at baseline and in the general population

</div>

<img src="12955_2023_2115_Tab5_HTML.jpg" id="MO2" />

*BOA* Better management of patients with OsteoArthritis, *RMSE* Root mean square error, *RSE* Robust standard error; Darker shades under estimate columns show inconsistency in decrement; Lighter shades in the *P*-value columns show non-statistically significant estimates;

</div>

In all except three registers—spine, ankle and heart failure—and in the general population—the highest decrements in EQ VAS score were in the anxiety/depression dimension level three. In the spine and ankle registers level three in the pain/discomfort dimension and the usual activities dimension in the heart failure register had the largest decrements in EQ VAS score (Table <a href="#Tab5" data-ref-type="table">5</a>). The adjusted R squared values ranged from about 14% in respiratory failure patients to about 41% in bipolar patients, and was 48% in the general population. The OLS models at baseline adjusted for sex and age group showed similar results to the unadjusted models in most of the registers and in the general population (Table S<a href="#MOESM1" data-ref-type="supplementary-material">3</a>).

In the two-level model of the data at baseline, findings similar to the OLS models were shown. Accordingly, self-care level three is the dimension with inconsistency in all of the registers and in the general population. Across dimensions the highest decrement was in the anxiety/depression in all the registers and in the general population except for the spine register (pain/discomfort dimension) (Table S<a href="#MOESM1" data-ref-type="supplementary-material">4</a>). The adjusted version of the models showed results similar to the unadjusted models (Table S<a href="#MOESM1" data-ref-type="supplementary-material">5</a>). Comparing the OLS and multilevel models, both unadjusted and adjusted models showed that the multilevel models had estimates with narrower 95% confidence interval than the OLS models (Fig. S<a href="#MOESM1" data-ref-type="supplementary-material">1</a>-S<a href="#MOESM1" data-ref-type="supplementary-material">4</a>).

### Regression (OLS) models of the one-year follow-up data

In the OLS models based on the 1-year follow-up data across the registers, the decrements in all the EQ-5D-3L dimensions showed consistency with severity levels in four of the registers. The registers with any occurrence of inconsistency in the decrements included the spine, ankle, cruciate, heart failure and bipolar registers. The inconsistency in these registers were mainly related to self-care dimension in spine, ankle and cruciate registers and mobility dimensions in the heart failure and bipolar registers. Additional inconsistency in the mobility dimension was also shown in the cruciate ligament injury register.

In most of the registers and in the general population, the highest decrements in EQ VAS score were observed in the anxiety/depression dimension. The exceptions were spine and ankle registers with pain/discomfort and mobility dimensions having the highest decrements respectively (Table <a href="#Tab6" data-ref-type="table">6</a>, Fig. S<a href="#MOESM1" data-ref-type="supplementary-material">6</a>). The adjusted R squared values of the models at 1-year follow-up ranged from about 30% in patients with respiratory failure to 60% in the spine register (Table <a href="#Tab6" data-ref-type="table">6</a>). The OLS models at 1-year follow-up adjusted for sex and age group showed similar results to the unadjusted models (Table S<a href="#MOESM1" data-ref-type="supplementary-material">6</a>).

<div id="Tab6" class="table-wrap">

<div class="caption">

Ordinary least squares regressions in the 9 registers at 1-year follow-up and in the general population

</div>

<img src="12955_2023_2115_Tab6_HTML.jpg" id="MO3" />

*BOA* Better management of patients with OsteoArthritis, *RMSE* Root mean square error, *RSE*: Robust standard error; Darker shades under estimate columns show inconsistency in decrement; Lighter shades in the *P*-value columns show non-statistically significant estimates

</div>

In the two-level model, two of the registers (hip and respiratory failure) had estimates with consistency in all dimensions. In all the other registers inconsistencies were related to the self-care dimension. In terms of the decrements of EQ VAS score, anxiety/depression dimension had the largest decrement in eight of the nine registers and in the general population data. In the spine register, the largest decrement was shown in the pain/discomfort dimension (Table S<a href="#MOESM1" data-ref-type="supplementary-material">7</a>). The models adjusted for sex and age groups, had similar findings to the unadjusted models (Table S<a href="#MOESM1" data-ref-type="supplementary-material">8</a>). The 95% CIs of the estimates, both in the unadjusted and adjusted models, were narrower compared to the estimates of the OLS models (Fig. S<a href="#MOESM1" data-ref-type="supplementary-material">5</a>-S<a href="#MOESM1" data-ref-type="supplementary-material">8</a>).

### Findings of additional analyses

Results of the analysis of the pooled data with patient groups as independent variables showed that the overall association between EQ-5D-3L dimensions and The EQ VAS remained stable. Almost all the patient groups showed association with EQ VAS score with different levels of decrement or increment in comparison to the general population (Tables S<a href="#MOESM1" data-ref-type="supplementary-material">9</a>, S<a href="#MOESM1" data-ref-type="supplementary-material">10</a>).

The OLS models based on EQ-5D-5L data of the two patient groups (BOA and hip) demonstrated an overall comparable findings to those of the findings in the main analysis based on the EQ-5D-3L data (Table S<a href="#MOESM1" data-ref-type="supplementary-material">11</a>).

## Discussion

In the present study, patient valuations of their health states using the EQ VAS was explored. Valuations of nine selected EQ-5D-3L health states showed general consistency by severity. Similarly, moderate to strong correlations were found between EQ VAS valuations based on modelled EQ VAS data and the EQ-5D-3L index. A change in the EQ VAS scores of the same health states over time and differences across patient groups was also observed. Models of EQ VAS score regressed on EQ-5D-3L dimensions showed mostly consistent decrements by severity level in each dimension both at baseline and at 1-year follow-up.

Patients’ values, across nine selected EQ-5D-3L health states, had good face validity: poor health states had lower values than mild health problems, suggesting that these methods provide a reasonable means of broadly reflecting how good or bad patients consider health states to be. The consistency of EQ VAS scores of health states with severity was also reported by a study of the general population on data from 15 countries \[43\]. A number of common health states like in the present study were also reported preoperatively and postoperatively in a study of a knee arthroplasty population in the UK \[31\].

In the EQ VAS scores of the same health states at baseline and at 1-year follow-up, relatively larger increases were observed in valuations of many of the health states from the intervention-based registers than in the diagnosis-based registers. This could be associated with the mainly surgical interventions employed in most of the intervention-based registers relieving pain and mobility problems which are common among such patients \[44\]. In relation to this, the results also seem to support the face validity of using EQ VAS as patient valuations. The differences in EQ VAS scores of the same health states across patient groups and over time could be associated with the broader nature of EQ VAS compared to the EQ-5D-3L, hence capturing broader aspects of health than the EQ-5D dimensions. This was also reported by a study in the UK patient-reported outcome measures program \[13\].

The overall consistency between the EQ VAS and the EQ-5D-3L dimensions was also shown in the significant correlations between EQ VAS score and EQ-5D-3L index which increased from baseline to 1-year follow up in all the patient groups. Comparable findings were reported in similar studies among women with cervical pre-cancer (0.51) in the UK \[34\], and among patients with Parkinson’s disease (0.68) in Spain \[45\].

The OLS models of EQ VAS regressed on the EQ-5D-3L dimensions both at baseline and 1-year follow-up showed mostly consistent decrements by severity level in each dimension in the different patient groups and the general population. An overall similar finding was reported in a study which compared health state valuation between non-specific low back pain patients and the general population in the Netherlands \[32\]. Similarly, overall consistent models were reported in previous studies based on preoperative and postoperative data of patients undertaking hip replacement in Sweden \[28\] and knee replacement in the UK \[31\]. In addition, studies in the general population conducted through experience-based \[8, 9, 18, 19, 46, 47\] and hypothetical \[48–50\] perspectives also showed consistent valuations of EQ-5D health states (3L as well as 5L) through VAS.

In the OLS models, inconsistencies were noted mainly in the self-care dimensions in all the patient groups at baseline and in several patient groups at 1-year follow-up. Inconsistencies in the mobility dimension were also shown among several patient groups at baseline and at 1-year follow-up. Similarly, a study in Sweden exploring valuations among patients undergoing hip replacement the self-care dimension showed inconsistency both in preoperative and postoperative valuations \[28\]. In another study in the UK among patients in four clinical groups (stroke, low back pain, colposcopic investigation and cytological surveillance), the self-care dimension was found to not be statistically significant in either of the severity levels 2 and 3 \[33\]. Inconsistencies in the self-care and mobility dimensions were also noted among low back pain patients in the study from the Netherlands \[32\]. In the present study, the inconsistencies were also noted among in the general population.

One of the possible reasons for the inconsistencies noted in the present study in the self-care and to a certain extent in the mobility dimensions could be the relative importance of the different dimensions depending on whether one is valuing their own health state or a hypothetical health state. This has been discussed in a previous study, based on EQ-5D-3L data from the US, which compared experienced and hypothetical health states where the self-care dimension followed by pain/discomfort were the most important dimensions in the valuation of hypothetical health states. In contrast, usual activities and anxiety/depression dimensions were the most important in experience-based valuations \[51\]. In relation to this, the study also showed that in the experience-based valuations severity levels 2 and 3 of the mobility and self-care dimensions were closest to each other compared to other dimensions and to hypothetical valuations \[51\]. This was in line with the findings across the patient groups as well as in the general population in the present study. The findings here show that that the aspects of health important to patients are different from those of the general public who are asked to imagine health problems. This, in turn, could yield different results when measuring effectiveness of interventions depending on whether patients’ own perspectives or imagined health states by the general public are used.

The second related possible explanation for the inconsistencies could be the relatively small number of individuals reporting severity level 3 problems in the self-care and mobility dimensions. In the mobility dimension, the fact that level 3 is presented as ‘confined to bed’ could have contributed to fewer individuals reporting that level. In relation to that, individuals with more severe problems choosing mobility severity level 2 could possibly contribute to lower EQ VAS scores. In a number of studies where inconsistencies in one or both of the dimensions were shown, the relative number of responses falling in severity level 3 were small accounting for 1% or less of the all the problem levels in studies from Sweden and the UK \[28, 32–34\]. Notably, in the study from the UK among women with low-grade cytological abnormalities (pre-cancer), severity levels 2 and 3 in mobility, self-care, and usual activities dimensions were combined due to very few number of individuals reporting problems in these dimensions \[34\]. Comparatively, EQ-5D-5L has been shown to provide better discriminatory power between severity levels than EQ-5D-3L \[52\] and lower ceiling effects the potential implications of which, on valuation, have been discussed \[52, 53\]. In the context of the present study the categorization of responses in the ‘no problem’ or ‘moderate’ levels, which would otherwise be in between in EQ-5D-5L, could lead to under/over estimation of valuations.

In the present study, anxiety/depression showed the highest decrements in most patient groups at baseline and at 1-year follow-up indicating it to be the most important dimension to patients. A similar finding was also shown in the general population data. In a study based on data from different groups—people with varicose veins, chest pain, chronic obstructive pulmonary disease, irritable bowel syndrome, osteoarthritis, low back pain, elderly women and patients in intensive care unit – anxiety/depression was the dimension with the highest decrement, similar to the present study \[30\]. Similar findings were also shown in several other studies in Sweden \[28, 47\], the Netherlands \[32\] and the UK \[16, 31, 33, 34\], employing patient valuations of their own health.

The dimensions with the highest decrements remained the same from baseline to 1-year follow up in most of the patient groups. However, in patients from the ankle and heart failure registers, a change in the dimension with the highest decrement with time was shown. In the ankle register, pain/discomfort had the highest decrement at baseline and anxiety/depression at 1-year follow-up. Heart failure patients on the other hand, had the highest decrement in the usual activities dimension at baseline and in the anxiety/depression dimension at 1-year follow-up. This could relate to the change in the relative importance of the different dimensions depending on the disease/condition patients have and how they experienced them before and after intervention/treatment. It is also notable that the dimension with the highest decrement at 1-year follow-up in the two patient groups had become similar to that of the general population in the study.

In the anxiety/depression dimension, the highest decrement was recorded among patients with bipolar disorder both at baseline and at 1-year follow-up. This seems to show the ability of the EQ-5D instrument to indicate the importance of specific dimensions to patients in line with their diagnosis/conditions. Comparably large decrements in the anxiety/depression dimension was noted in a study from the UK \[33\]. The decrements in severity level three of the anxiety/depression dimension were comparable to the general population. This could possibly show the emphasis given to experiencing mental health problems in the general population as well, as considerable level of mental health problems are reported in general population samples in Sweden \[54, 55\].

Following anxiety/depression dimension, while comparable to usual activities dimensions at baseline, pain/discomfort had larger decrements at severity level three mainly among patients from musculoskeletal registers. On the other hand, patients with heart failure, respiratory failure and bipolar disorder assigned large decrements to severity level three of the usual activities dimension. The importance of pain and usual activities dimensions for the respective patient groups seems to go in line with the overall symptoms and the associated implications of the disease/conditions in terms of pain or limitation of day-to-day activities.

At baseline, in most of the patient groups, 20–30% of the variances were explained by EQ-5D-3L dimensions while in the data of respiratory failure (about 14%) and bipolar patients (about 41%) the lowest and the highest proportions were recorded. All were lower than r squared in the model of the general population data (48%). The explained variance increased in all the patient groups at 1-year follow up ranging between 35 and 60% for most patient groups. It showed about 30% explained variance in the model for the patients from the respiratory failure register. The explained variance still remained lower than in the general population for most patient groups with higher proportions in the patients from spine and hip registers and comparable proportions noted among patients from bipolar register. Although not directly comparable, a number of r squared statistics have been reported in regression models of different patient groups including 32% with cervical pre-cancer \[34\], 39% in those undergoing knee replacement \[31\] and 47.1% in the eight patients groups cited above \[30\].

One of the strengths of the present study is the large sample size of patients which allowed investigation of experience-based valuation of health by patients through the EQ VAS and comparison with a large general population sample. The comparison across many patient groups is also an important strength enabling assessment of how specific diseases and associated experience relate to valuation of health states. Furthermore, the study investigated how patients’ valuation of their health changes from baseline to 1-year follow-up. In addition, the study compared OLS models with multilevel models and covariate adjusted models through sensitivity analyses.

On the other hand, an important limitation to take into consideration is possible differences in the way EQ-5D data were collected across the different registers to which some of the difference in valuation could be attributed. In addition, as the state *dead* was not anchored in the present study, its immediate use in economic evaluations could be limited. However, studies among a sample of patients to get their valuations of the state *dead* could remedy this in addition to the current discussion on whether anchoring *dead* is necessary and other alternatives \[56\]. VAS/ EQ VAS not providing obvious choice or trade-off in the valuation process and the end aversion bias may have had an implication in the EQ VAS valuation in the context of using it in economic valuation \[20, 21\]. In relation to this, the level of correlation between EQ VAS score and EQ-5D-3L in the different patient groups, even though moderate to high, some level of discrepancy remains between the two measures.

The present study has important implications including showing the feasibility and importance of timing of patient valuations as dimensions important to patients could depend on the type of disease/condition and its stage (e.g., pre- vs. post-operative). This, together with other clinical measures, could facilitate identification of certain aspects of health that may be available for intervention. The broader coverage of EQ VAS than the EQ-5D-3L dimensions was also demonstrated which could emphasize the importance of EQ VAS as a relatively simple but important measure of patients’ overall health. The present study also showed that patient valuations based on EQ VAS scores, elicited through experience-based perspectives, have a potential to be used in the calculation of quality-adjusted life years (QALYs) in comparing different interventions in decision contexts that take patient perspectives into consideration. Furthermore, the study adds information for a discussion on the reconsideration of the need for severity level three in the self-care dimension and to some extent the mobility dimension considering the inconsistencies found in many patient groups. In addition, the findings showed patient valuations could arguably be more appropriate for use in situations where QALYs do not need to be calculated as well; such as summarizing population health survey data and assessing changes in health following surgical and other clinical interventions. The findings also highlighted the importance of mental health among patients with otherwise mainly physical diseases. This provides important information that the mental health aspect is a crucial component in the care of the patients.

The application of clinimetric approaches in future studies of EQ VAS and EQ-5D, besides the current mainly psychometric ones, in assessing patients’ valuations of their health, could provide useful insights in general and in clinical contexts \[57, 58\].

## Conclusions

The present study showed the consistency between the EQ-5D-3L dimensions and EQ VAS valuations in several patient groups at baseline and at 1-year follow-up. The broader construct which EQ VAS covers, in comparison to the EQ-5D-3L dimensions, was also demonstrated. The main source of inconsistency in terms of decrements was severity level three of the self-care dimension, indicating a possible need to reconsider the importance of this severity level. The study also showed the importance of mental health for overall HRQoL despite the mainly physical nature the conditions of most of the patient groups, with large decrements in the anxiety/depression dimension. Overall, the study revealed crucial contribution of the EQ VAS in the patients’ assessment of their own health, and the potential for these data to provide experience based value sets. The unique advantages of patient value sets in showing aspects of health important to patients in real-world scenarios of valuing health which could be useful inputs for clinical and resource allocation decisions were also demonstrated.

## Supplementary Information

<div class="caption">

**Additional file 1: Table S1.** Sampling procedure followed including 9 National Quality Registers (NQRs), baseline to 1-year follow-up and the general population data. **Table S2.** Correlation between change in EQ VAS score and change in EQ-5D index across patient groups. **Table S3.** Ordinary least squares regressions in the 9 registers and the general population, baseline, adjusted for sex and age groups. **Table S4.** Mixed model, estimates, baseline. **Table S5.** Mixed model, estimates, baseline, adjusted for sex and age groups. **Table S6.** Ordinary least squares regressions in the 9 registers and the general population, 1-year follow-up, adjusted for sex and age groups. **Table S7.** Mixed model, estimates, 1-year follow-up. **Table S8.** Mixed model, estimates, 1-year follow-up, adjusted for sex and age groups. **Figure S1.** Estimates, OLS models, baseline. **Figure S2.** Estimates, mixed model, baseline. **Figure S3.** Estimates, OLS models, baseline, adjusted for sex and age groups. **Figure S4.** Estimates, mixed model, baseline, adjusted for sex and age groups. **Figure S5.** Estimates, OLS model, 1-year. **Figure S6.** Estimates, mixed model, 1-year. **Figure S7.** Estimates, OLS model, 1-year, adjusted for sex and age groups. **Figure S8.** Estimates, mixed model, 1-year, adjusted for sex and age groups. **Table S9.** Ordinary least squares regressions in the pooled data at baseline. **Table S10.** Ordinary least squares regressions in the pooled data at 1-year follow-up. **Table S11.** Ordinary least squares models of EQ-5D-5L dimensions on EQ VAS score in the BOA and Hip registers.

</div>

## Acknowledgements

The authors would like to acknowledge Emma Nauclér for providing support in data management and the statistical consultation in the study.

Group authors: members of the Swedish Quality Registers (SWEQR) Study Group in alphabetical order: Allan Abbott, Linköping University, Linköping, Sweden; Magnus Ekström, Lund University, Lund, Sweden; Magnus Forssblad, Karolinska Institutet, Stockholm, Sweden; Peter Fritzell, Futurum Academy for Health and Care, Jönköping, Sweden/RKC Centre for spine surgery, Stockholm, Sweden; Åsa Jonsson, Ryhov County Hospital, Jönköping, Sweden; Mikael Landén, University of Gothenburg, Gothenburg, Sweden; Michael Möller, University of Gothenburg, Gothenburg, Sweden; Malin Regardt, Swedish Rheumatology Quality Register (SRQ)/Karolinska University Hospital, Stockholm; Karolinska Institutet, Stockholm, Sweden; Björn Rosengren, Lund University, Lund, Sweden; Marcus Schmitt-Egenolf, Umeå University, Umeå, Sweden; Johanna Vinblad, Centre of Registers, Gothenburg, Sweden; Annette W-Dahl, Lund University, Lund, Sweden.

## Abbreviations

BOA  
Better management of patients with OsteoArthritis

EQ VAS  
EuroQol visual analogue scale

EQ-5D  
EuroQol five dimensions

EQ-5D-3L  
EuroQol 5 dimensions 3 levels

EQ-5D-5L  
EuroQol 5 dimensions 5 levels

NQRs  
National Quality Registers

OLS  
Ordinary least squares regression

QALY  
Quality-adjusted life year

SD  
Standard deviation

SG  
Standard gamble

TTO  
Time trade-off

UK  
United Kingdom

VAS  
Visual analogue scale

## Authors’ contributions

KB and OR, conceived the study. FST, OR, KB, ND, DP and members of the SWEQR Study Group (AA, ME, MF, PF, ÅJ, ML, MM, MR, BR, MSE, JV, AWD) designed the study. FST performed the data analysis and preliminary interpretation of the data. KB, OR, ND and DP supervised data analysis and interpretation of findings. FST drafted the manuscript. KB, OR, ND, DP and members of the SWEQR Study Group (AA, ME, MF, PF, ÅJ, ML, MM, MR, BR, MSE, JV, AWD) revised the draft manuscript for important intellectual content. All authors approved the submission of the manuscript.

## Funding

Open access funding provided by Karolinska Institute. This research project is supported by a grant from The EuroQol Research Foundation (EQ Project \# 2016480) and Region Stockholm (former Stockholm County Council) (# 4–3464/2018), Stockholm, Sweden.

## Availability of data and materials

Data sharing is not possible according to Swedish law.

## Declarations

### Ethics approval and consent to participate

The study received ethical approval from the Regional Ethics Review Board in Gothenburg for the data from the NQRs (#1185–18/2019–00812 and \#2020–04369) and from the Swedish Ethical Review Authority (#2020–03090) for the general population data.

### Consent for publication

Not applicable.

### Competing interests

KB, ND and DP are members of the EuroQol Group. KB reports grants from EuroQol Research Foundation, grants from Region Stockholm, during the conduct of the study; personal fees from Region Stockholm, outside the submitted work. ML reports personal fees from Lundbeck pharmaceuticals, outside the submitted work. OR reports institutional compensation for educational consultancy from Link Sweden; institutional compensation for research consultancy from Pfizer, outside the submitted work. AA, ME, MF, PF, ÅJ, MM, MR, BR, MSE, FST, AWD and JV declare no competing interests.

## Footnotes

## Contributor Information

Fitsum Sebsibe Teni, Email: fitsum.teni@ki.se.

The Swedish Quality Register (SWEQR) Study Group:

[Allan Abbott]("Abbott A"[Author]), [Magnus Ekström]("Ekström M"[Author]), [Magnus Forssblad]("Forssblad M"[Author]), [Peter Fritzell]("Fritzell P"[Author]), [Åsa Jonsson]("Jonsson Å"[Author]), [Mikael Landén]("Landén M"[Author]), [Michael Möller]("Möller M"[Author]), [Malin Regardt]("Regardt M"[Author]), [Björn Rosengren]("Rosengren B"[Author]), [Marcus Schmitt-Egenolf]("Schmitt-Egenolf M"[Author]), [Johanna Vinblad]("Vinblad J"[Author]), and [Annette W-Dahl]("W-Dahl A"[Author])

## References

## References

1. Brooks R, Boye KS, Slaap B. EQ-5D: a plea for accurate nomenclature. J Patient Rep Outcomes. 2020;4:52. doi: 10.1186/s41687-020-00222-9.

2. Devlin NJ, Brooks R. EQ-5D and the EuroQol group: past, present and future. Appl Health Econ Health Policy. 2017;15:127–137. doi: 10.1007/s40258-017-0310-5.

3. Rabin R, de Charro F. EQ-5D: a measure of health status from the EuroQol Group. Ann Med. 2001;33:337–343. doi: 10.3109/07853890109002087.

4. EuroQol Research Foundation . EQ-5D-3L User Guide. 2018.

5. EuroQol Research Foundation . EQ-5D-5L User Guide. 2019.

6. Lugnér AK, Krabbe PFM. An overview of the time trade-off method: concept, foundation, and the evaluation of distorting factors in putting a value on health. Expert Rev Pharmacoecon Outcomes Res. 2020;20:331–42. doi: 10.1080/14737167.2020.1779062.

7. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34:993–1004. doi: 10.1007/s40273-016-0404-1.

8. Burström K, Sun S, Gerdtham U-G, Henriksson M, Johannesson M, Levin L-Å, et al. Swedish experience-based value sets for EQ-5D health states. Qual Life Res. 2014;23:431–442. doi: 10.1007/s11136-013-0496-4.

9. Burström K, Teni FS, Gerdtham U-G, Leidl R, Helgesson G, Rolfson O, et al. Experience-based Swedish TTO and VAS Value Sets for EQ-5D-5L Health States. Pharmacoeconomics. 2020;38:839–856. doi: 10.1007/s40273-020-00905-7.

10. Burström K, Johannesson M, Diderichsen F. A comparison of individual and social time trade-off values for health states in the general population. Health Policy. 2006;76:359–370. doi: 10.1016/j.healthpol.2005.06.011.

11. Lundberg L, Johannesson M, Isacson DGL, Borgquist L. The Relationship between health-state utilities and the sf-12 in a general population. Med Decis Making. 1999;19:128–40. doi: 10.1177/0272989X9901900203.

12. Bardage C, Isacson D, Ring L, Bingefors K. A Swedish population-based study on the relationship between the SF-36 and health utilities to measure health in hypertension. Blood Pressure. 2003;12:203–210. doi: 10.1080/08037050310002083.

13. Feng Y, Parkin D, Devlin NJ. Assessing the performance of the EQ-VAS in the NHS PROMs programme. Qual Life Res. 2014;23:977–989. doi: 10.1007/s11136-013-0537-z.

14. EuroQoL Group . Terminology. EQ-5D. 2020.

15. Johnson JA, Coons SJ, Ergo A, Szava-Kovats G. Valuation of EuroQOL (EQ-5D) health states in an adult US sample. Pharmacoeconomics. 1998;13:421–433. doi: 10.2165/00019053-199813040-00005.

16. Gutacker N, Patton T, Shah K, Parkin D. Using EQ-5D data to measure hospital performance: are general population values distorting patients’ choices? Med Decis Making. 2020;40:511–521. doi: 10.1177/0272989X20927705.

17. Leidl R, Reitmeir P. A value set for the EQ-5D based on experienced health states: development and testing for the German population. Pharmacoeconomics. 2011;29:521–534. doi: 10.2165/11538380-000000000-00000.

18. Leidl R, Reitmeir P. An Experience-based value set for the EQ-5D-5L in Germany. Value Health. 2017;20:1150–1156. doi: 10.1016/j.jval.2017.04.019.

19. Sun S, Chen J, Kind P, Xu L, Zhang Y, Burström K. Experience-based VAS values for EQ-5D-3L health states in a national general population health survey in China. Qual Life Res. 2015;24:693–703. doi: 10.1007/s11136-014-0793-6.

20. Torrance GW, Feeny D, Furlong W. Visual analog scales: do they have a role in the measurement of preferences for health states? Med Decis Making. 2001;21:329–334. doi: 10.1177/02729890122062622.

21. Whitehead SJ, Ali S. Health outcomes in economic evaluation: the QALY and utilities. Br Med Bull. 2010;96:5–21. doi: 10.1093/bmb/ldq033.

22. Neumann PJ, Goldie SJ, Weinstein MC. Preference-Based Measures in Economic Evaluation in Health Care. Annu Rev Public Health. 2000;21:587–611. doi: 10.1146/annurev.publhealth.21.1.587.

23. Brazier J, Green C, McCabe C, Stevens K. Use of visual analog scales in economic evaluation. Expert Rev Pharmacoecon Outcomes Res. 2003;3:293–302. doi: 10.1586/14737167.3.3.293.

24. Parkin D, Devlin N. Is there a case for using visual analogue scale valuations in cost-utility analysis? Health Econ. 2006;15:653–664. doi: 10.1002/hec.1086.

25. Åström M, Lwin ZMT, Teni FS, Burström K, Berg J. Use of the visual analogue scale for health state valuation. Qual Life Res. 2023 (in press). doi:10.1007/s11136-023-03411-3

26. Brazier J, Rowen D, Karimi M, Peasgood T, Tsuchiya A, Ratcliffe J. Experience-based utility and own health state valuation for a health state classification system: why and how to do it. Eur J Health Econ. 2018;19:881-91. doi:10.1007/s10198-017-0931-5

27. Cubi-Molla P, Shah K, Burström K. Experience-based values: a framework for classifying different types of experience in health valuation research. Patient. 2018;11:253–270. doi: 10.1007/s40271-017-0292-2.

28. Nemes S, Burström K, Zethraeus N, Eneqvist T, Garellick G, Rolfson O. Assessment of the Swedish EQ-5D experience-based value sets in a total hip replacement population. Qual Life Res. 2015;24:2963–2970. doi: 10.1007/s11136-015-1020-9.

29. Leidl R, Reitmeir P, König H-H, Stark R. The performance of a value set for the EQ-5D based on experienced health states in patients with inflammatory bowel disease. Value Health. 2012;15:151–157. doi: 10.1016/j.jval.2011.08.004.

30. Mann R, Brazier J, Tsuchiya A. A comparison of patient and general population weightings of EQ-5D dimensions. Health Econ. 2009;18:363–372. doi: 10.1002/hec.1362.

31. Pickard AS, Hung Y, Lin F, Lee TA. Patient experience-based value sets: are they stable? Med Care. 2017;55:979–984. doi: 10.1097/MLR.0000000000000802.

32. van Dongen JM, van denBerg B, Bekkering GE, van Tulder MW, Ostelo RWJG. Patient versus general population health state valuations: a case study of non-specific low back pain. Qual Life Res. 2017;26:1627–1633. doi: 10.1007/s11136-017-1497-5.

33. Whynes DK. Does the correspondence between EQ-5D health state description and VAS score vary by medical condition? Health Qual Life Outcomes. 2013;11:155. doi: 10.1186/1477-7525-11-155.

34. Whynes DK, TOMBOLA Group Correspondence between EQ-5D health state classifications and EQ VAS scores. Health Qual Life Outcomes. 2008;6:94. doi: 10.1186/1477-7525-6-94.

35. Emilsson L, Lindahl B, Köster M, Lambe M, Ludvigsson JF. Review of 103 Swedish healthcare quality registries. J Intern Med. 2015;277:94–136. doi: 10.1111/joim.12303.

36. Teni FS, Rolfson O, Devlin N, Parkin D, Nauclér E, Burström K, et al. Variations in patients’ overall assessment of their health across and within disease groups using the eq-5d questionnaire: protocol for a longitudinal study in the Swedish national quality registers. JMIR Res Protoc. 2021;10:e27669. doi: 10.2196/27669.

37. Teni FS, Rolfson O, Devlin N, Parkin D, Nauclér E, Burström K. Longitudinal study of patients’ health-related quality of life using EQ-5D-3L in 11 Swedish National Quality Registers. BMJ Open. 2022;12:e048176. doi: 10.1136/bmjopen-2020-048176.

38. Lindgren A, Björk J, Stroh E, Jakobsson K. Adult asthma and traffic exposure at residential address, workplace address, and self-reported daily time outdoor in traffic: a two-stage case-control study. BMC Public Health. 2010;10:716. doi: 10.1186/1471-2458-10-716.

39. Svensson AC, Fredlund P, Laflamme L, Hallqvist J, Alfredsson L, Ekbom A, et al. Cohort profile: The Stockholm Public Health Cohort. Int J Epidemiol. 2013;42:1263–1272. doi: 10.1093/ije/dys126.

40. Stockholms läns landsting. Hälsoenkät 2006-En undersökning om hälsa och levnadsförhållanden i Stockholms län. 2006 [cited 2021 Aug 22]. Available from: http://dok.slso.sll.se/CES/FHG/Folkhalsoarbete/Halsa%20Stockholm/Enkat-2006unga.pdf

41. McDonalds JH. Spearman rank correlation. Handbook of Biological Statistics. Baltimore: Sparkey House Publishing; 2014. p. 210–21.

42. Fowler J, Cohen L, Jarvis P. Measuring correlations. Practical Statistics for Field Biology. 2nd ed. Chichester, West Sussex: Wiley; 2009.

43. Heijink R, Reitmeir P, Leidl R. International comparison of experience-based health state values at the population level. Health Qual Life Outcomes. 2017;15:138. doi: 10.1186/s12955-017-0694-9.

44. Trudelle-Jackson E, Emerson R, Smith S. Outcomes of total hip arthroplasty: a study of patients one year postsurgery. JOSPT Cases. J Orthop Sports Phys Ther. 2002;32:260–7. doi: 10.2519/jospt.2002.32.6.260.

45. García-Gordillo MÁ, del Pozo-Cruz B, Adsuar JC, Cordero-Ferrera JM, Abellán-Perpiñán JM, Sánchez-Martínez FI. Validation and comparison of EQ-5D-3L and SF-6D instruments in a Spanish Parkinson’s disease population sample. Nutr Hosp. 2015;32:2808–2821. doi: 10.3305/nh.2015.32.6.9765.

46. Wu XY, Ohinmaa A, Johnson JA, Veugelers PJ. Assessment of children’s own health status using visual analogue scale and descriptive system of the EQ-5D-Y: linkage between two systems. Qual Life Res. 2014;23:393–402. doi: 10.1007/s11136-013-0479-5.

47. Åström M, Rolfson O, Burström K. Exploring EQ-5D-Y-3L Experience-based VAS values derived among adolescents. Appl Health Econ Health Policy. [cited 2022 Mar 19]. 10.1007/s40258-021-00713-w

48. Augustovski FA, Irazola VE, Velazquez AP, Gibbons L, Craig BM. Argentine valuation of the EQ-5D health states. Value Health. 2009;12:587–596. doi: 10.1111/j.1524-4733.2008.00468.x.

49. Yusof FAM, Goh A, Azmi S. Estimating an EQ-5D value set for Malaysia using time trade-off and visual analogue scale methods. Value Health. 2012;15:S85–90. doi: 10.1016/j.jval.2011.11.024.

50. Goudarzi R, Zeraati H, Akbari Sari A, Rashidian A, Mohammad K. Population-based preference weights for the eq-5d health states using the Visual Analogue Scale (VAS) in Iran. Iran Red Crescent Med J. 2016;18:e21584. doi: 10.5812/ircmj.21584.

51. Rand-Hendriksen K, Augestad LA, Kristiansen IS, Stavem K. Comparison of hypothetical and experienced EQ-5D valuations: relative weights of the five dimensions. Qual Life Res. 2012;21:1005–1012. doi: 10.1007/s11136-011-0016-3.

52. Janssen MF, Bonsel GJ, Luo N. Is EQ-5D-5L Better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. 2018;36:675–697. doi: 10.1007/s40273-018-0623-8.

53. Law EH, Pickard AS, Xie F, Walton SM, Lee TA, Schwartz A. Parallel valuation: a direct comparison of EQ-5D-3L and EQ-5D-5L societal value sets. Med Decis Making. 2018;38:968–982. doi: 10.1177/0272989X18802797.

54. Höglund P, Hakelind C, Nordin S. Severity and prevalence of various types of mental ill-health in a general adult population: age and sex differences. BMC Psychiatry. 2020;20:209. doi: 10.1186/s12888-020-02557-5.

55. Olsson S, Hensing G, Burström B, Löve J. Unmet Need for mental healthcare in a population sample in sweden: a cross-sectional study of inequalities based on gender, education, and country of birth. Community Ment Health J. 2021;57:470–481. doi: 10.1007/s10597-020-00668-7.

56. Sampson C, Parkin D, Devlin N. Drop dead: is anchoring at ‘dead’ a theoretical requirement in health state valuation?. Office of Health Economics; 2020 [cited 2023 Mar 3]. Available from: https://www.ohe.org/publications/drop-dead-anchoring-%E2%80%98dead%E2%80%99-theoretical-requirement-health-state-valuation. doi:10.1002/hec.4863

57. Carrozzino D, Patierno C, Guidi J, BerrocalMontiel C, Cao J, Charlson ME, et al. Clinimetric Criteria for Patient-Reported Outcome Measures. Psychother . 2021;90:222–232. doi: 10.1159/000516599.

58. Carrozzino D, Patierno C, Pignolo C, Christensen KS. The concept of psychological distress and its assessment: a clinimetric analysis of the SCL-90-R. Int J Stress Manag. 2022. 10.1037/str0000280

## Associated Data

### Supplementary Materials

<div class="caption">

**Additional file 1: Table S1.** Sampling procedure followed including 9 National Quality Registers (NQRs), baseline to 1-year follow-up and the general population data. **Table S2.** Correlation between change in EQ VAS score and change in EQ-5D index across patient groups. **Table S3.** Ordinary least squares regressions in the 9 registers and the general population, baseline, adjusted for sex and age groups. **Table S4.** Mixed model, estimates, baseline. **Table S5.** Mixed model, estimates, baseline, adjusted for sex and age groups. **Table S6.** Ordinary least squares regressions in the 9 registers and the general population, 1-year follow-up, adjusted for sex and age groups. **Table S7.** Mixed model, estimates, 1-year follow-up. **Table S8.** Mixed model, estimates, 1-year follow-up, adjusted for sex and age groups. **Figure S1.** Estimates, OLS models, baseline. **Figure S2.** Estimates, mixed model, baseline. **Figure S3.** Estimates, OLS models, baseline, adjusted for sex and age groups. **Figure S4.** Estimates, mixed model, baseline, adjusted for sex and age groups. **Figure S5.** Estimates, OLS model, 1-year. **Figure S6.** Estimates, mixed model, 1-year. **Figure S7.** Estimates, OLS model, 1-year, adjusted for sex and age groups. **Figure S8.** Estimates, mixed model, 1-year, adjusted for sex and age groups. **Table S9.** Ordinary least squares regressions in the pooled data at baseline. **Table S10.** Ordinary least squares regressions in the pooled data at 1-year follow-up. **Table S11.** Ordinary least squares models of EQ-5D-5L dimensions on EQ VAS score in the BOA and Hip registers.

</div>

### Data Availability Statement

Data sharing is not possible according to Swedish law.

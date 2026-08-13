---
project_id: "20180630"
work_id: "doi:10.3389/fpubh.2021.744405"
doi: "10.3389/fpubh.2021.744405"
pmid: "34805069"
pmcid: "PMC8599146"
title: "Health Inequality Analysis in Europe: Exploring the Potential of the EQ-5D as Outcome"
journal: "Frontiers in Public Health"
publication_date: "2021-11-04"
volume: "9"
authors:
  - name: "Inge Spronk"
    affiliation_ids:
      - "aff1"
      - "aff2"
  - name: "Juanita A. Haagsma"
    affiliation_ids:
      - "aff1"
  - name: "Erica I. Lubetkin"
    affiliation_ids:
      - "aff3"
  - name: "Suzanne Polinder"
    affiliation_ids:
      - "aff1"
  - name: "M. F. Janssen"
    affiliation_ids:
      - "aff4"
  - name: "G. J. Bonsel"
    affiliation_ids:
      - "aff1"
      - "aff5"
affiliations:
  - id: "aff1"
    name: "1Department of Public Health, Erasmus MC, University Medical Center Rotterdam, Rotterdam, Netherlands"
  - id: "aff2"
    name: "2Association of Dutch Burn Centers, Maasstad Hospital, Rotterdam, Netherlands"
  - id: "aff3"
    name: "3Department of Community Health and Social Medicine, The City University of New York School of Medicine, New York, NY, United States"
  - id: "aff4"
    name: "4Section Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Rotterdam, Netherlands"
  - id: "aff5"
    name: "5EuroQol Research Foundation, Rotterdam, Netherlands"
keywords:
  - "EQ-5D"
  - "Europe"
  - "health inequality"
  - "outcome"
  - "social determinants"
licence: "cc-by"
source_file: "input/projects/20180630/papers/doi_10.3389_fpubh.2021.744405.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8599146/fullTextXML"
source_method: "epmc_xml"
source_sha256: "5eb9a51de137d460a221f33229ac8ff545d4fe796453e350fffccc04812e57a5"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Health Inequality Analysis in Europe: Exploring the Potential of the EQ-5D as Outcome

## Abstract

**Objective:** This study explored the additive value of the multi-item EuroQol 5-Dimension 5-Level (EQ-5D-5L) as an outcome measure in health inequality analyses, relative to the single-item EuroQol visual analog scale (EQ VAS).

**Methods:** A sample comprising the general population from Italy, the Netherlands, and United Kingdom (UK) completed the EQ-5D-5L and the EQ VAS. The level of education was selected as a proxy for socio-economic status (SES). EQ-5D-5L level sum scores (LSS) were compared against EQ VAS scores. Stratified and multivariable analyses were used to study the associations between SES and the LSS/EQ VAS relative to the presence of chronic health conditions.

**Results:** A total of 10,172 people participated in this study. In the UK and Netherlands, the LSS was worst for respondents with a low educational level and better for respondents with middle and high educational levels. For Italy, the LSS was best for respondents with a middle educational level compared to respondents with low and high educational levels. The same patterns were observed for the EQ VAS, but differences were slightly smaller. Multivariable analyses showed generally stronger predictive relations in the UK, and with the LSS. The presence of chronic health conditions and being unable to work were independent strong predictors, canceling out the effects of education.

**Conclusions:** In three different European countries, the EQ-5D measures show the presence of education-dependent health inequalities, which are universally explained in regression analysis by independently the presence of chronic health conditions and the inability to work. In stratified analysis, the EQ-5D-5L LSS discriminates slightly better between participants with different levels of SES compared to the EQ VAS.

## Introduction

Health inequalities among population groups of various socioeconomic statuses (SES) are an important challenge for public health and social policy, both at the national and international levels (1). Existing health inequalities among countries largely have a socio-economic rather than a medical background (2, 3). Health inequalities are a societal concern; apart from the unfairness of the unequal share in good health *per se*, it is known that such inequalities impact economic and societal development (4).

Health inequality can be defined as the difference in health or health status between defined population groups (5). The uneven distribution of health determinants may be unjust or unfair and avoidable (5, 6). Regardless of the general level of development or prosperity, groups with a lower SES (measured by income, education, and/or occupation) have worse health outcomes, i.e., higher mortality rates and higher disease prevalence rates (7).

The difficulties of touching upon the causes and the resilience for change have resulted in a growing interest in the measurement and analysis of inequalities in health (8–10). So far, the focus has been mainly on the definition of pathways, the techniques to quantify inequalities, and the appropriate manner in which this topic can be communicated (1, 11, 12). Surprisingly, little attention has been paid to the health measure used as an indicator. In the analysis of clinical trials, health care performance measurement, and burden of disease research, the role of self-reported outcomes of patient/person on the health status has grown to the extent that this type of health information is regarded as critical (13–15). In health inequality analysis, however, simple dichotomous measures like mortality or disease indicators, and a single item 5- or 7-point subjective health scale are generally the norm (2, 7, 10, 16). Such simple measures facilitate the computation of inequalities, but also have some disadvantages. First, they give little information on the impact at the person level (general information only) and the contributing role of factors that require some specification on how they work. Second, the use of single-item self-report measures implies a smaller signal to noise ratio and a larger dependency on the homogeneous use of the response scale; consequently, the analytical power is then theoretically decreased (17–20).

Multi-item measures with a summary or utility outcome often outperform single-item measures (21). Therefore, these measures might be valuable in health inequality analyses as well. An example is the widely available and commonly used multidimensional health questionnaire, the EuroQol 5-Dimension (EQ-5D) (22). This self-report instrument is available in many languages, has been validated for many diseases and conditions, and has been used in health inequality assessment (23–26). The EQ-5D includes a descriptive system that consists of five dimensions, which include mobility, self-care, usual activities, pain/discomfort, and anxiety/depression, and the responses can be converted into a utility index or level sum score (LSS) (22, 27), thereby enabling burden of disease and cost-effectiveness estimations which are increasingly used for resource allocation and evaluation of care (28, 29). The EQ-5D also includes a visual analog scale (EQ VAS), which assesses a person's current (subjective) health status on a 0–100 scale. In the descriptive system of the EQ-5D, the extent of problems on each dimension is assessed, whereas in the EQ VAS, the extent of problems is translated into a score or rating of health status.

Theoretically, the multi-item EuroQol 5-Dimension 5-Level (EQ-5D-5L) might outperform the EQ VAS (or other single-item measures) in health inequality analyses, but this may be counterbalanced by the higher refinement of the EQ VAS scale (101 units). Therefore, the aim of this study was to explore the potential additive value of the EQ-5D-5L as an outcome measure in education-related health inequality analyses, relative to the EQ VAS, in a large three-country dataset (Italy, the Netherlands, and the UK). The secondary aim was to study the extent to which the EQ-5D-5L and EQ VAS scores are related to SES (in particular education) and to explore the role of chronic morbidity and other factors, which could play a mediating role.

## Materials and Methods

### Participants

During the period from 29th June to 31st July, 2017, a web-based survey was administered to members of the general public aged between 18 and 75 years, from three European countries (the UK, Italy, and the Netherlands) (30). Participants were recruited by Survey Sampling International. This market agency distributed and launched the surveys in the existing large internet panels. The samples were selected in such a way that they were representative of the population aged between 18 and 75 years in the countries with respect to age, gender, and educational level (<a href="#SM1" data-ref-type="supplementary-material">Appendices 1A</a>,<a href="#SM1" data-ref-type="supplementary-material">B</a> show the distribution of gender and age categories and educational level of the population in Italy, the Netherlands, and the UK). All the panel members had already provided informed consent to participate in online surveys. Informed consent for the present survey was obtained from all those who agreed to complete the questionnaire for this study. The present study was part of the CENTER-TBI study (EC grant 602150), and ethical approval was obtained from the Leids Universitair Centrum—-Commissie Medische Ethiek (approval P14.222/NV/nv). Only data from those respondents who completed the entire questionnaire were included in the analysis.

### Measures

The questionnaire covered socio-demographic information, including the country of residence (UK, Netherlands, or Italy), age, gender, highest achieved level of education, annual household income level, work status, and self-reported presence of chronic health conditions (e.g., asthma, chronic bronchitis, severe heart disease, consequences of a stroke, diabetes, severe back complaints, arthrosis, rheumatism, cancer, memory problems due to a neurological disease/dementia, memory problems due to aging, depression or anxiety disorder, and/or other chronic health conditions). One open field was available for recording the presence of any other chronic health conditions, which were categorized by one of the medically trained authors. Self-reported presence of chronic health conditions was recoded into two variables; one variable indicated if the respondent had chronic health conditions (“yes” / “no”) and another variable indicated the number of self-reported chronic health conditions. The level of education achieved was used as a proxy for SES, avoiding income parity issues between countries. Level of education was measured as the highest level achieved and coded based on the International Standard Classification of Education (ISCED-97) into three groups: up to lower secondary education (ISCED 0, 1, and 2; “low”), completed upper secondary education (ISCED 3 and 4; “mid”) and tertiary education (ISCED 5 and 6; “high”). Work status was categorized as employed (employee and self-employed), unemployed (consisting of those out of work for more than or less than 1 year), looking after others (e.g., a caregiver or parent), student, retired, and unable to work.

The questionnaire also included the EQ-5D-5L (27). The EQ-5D-5L includes five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression, with five ordered response categories, which include no problems, slight problems, moderate problems, severe problems, and extreme problems (27). Based on these five dimensions, a level sum score (LSS) can be calculated. The EQ-5D-5L LSS is defined as the equal-weight sum score of the five dimensions. It ranges from 5 (no problems on all dimensions: 1+1+1+1+1) to 25 (worst possible health state); thus, the LSS has 21 units. The EQ-5D-5L measure also includes a standardized visual analog scale (EQ VAS) for general health, which ranges from 0 (worst imaginable health) to 100 (best imaginable health) (31); hence, the scale has 101 units.

### Hypotheses

1.  1\) Compared to the EQ VAS, the EQ-5D-5L LSS is better able to discriminate between different educational levels, both in table analysis and regression analysis.

2.  2\) Respondents with a lower educational level have a higher (“worse”) EQ-5D-5L LSS and a lower EQ VAS score compared to the participants with a higher educational level.

3.  3\) When respondents are grouped based on the presence or absence of a chronic health condition, the group with chronic health conditions is expected to show less education-related health inequalities (neither EQ-5D-5L LSS nor EQ VAS), as it is assumed that education affects health perception stronger than while being diseased (32).

4.  4\) The health inequality effect, if present, was found to be the strongest in the UK, followed by the Netherlands and then Italy (7).

### Statistical Analysis

Descriptive statistics were used to assess respondent characteristics and health outcomes for the total sample and for the three countries separately. EQ-5D-5L LSS were transformed to a 0–100 scale in order to be comparable with the EQ VAS.

Transformed EQ-5D-5L level sum score (tLSS) = 100 − \[(EQ-5D-5L level sum score − 5) x 5\]

Transformed EQ-5D-5L level sum score and EQ VAS score were compared among the different countries, as well as between the different groups based on the level of education (low/middle/high) within each of the countries. The EQ-5D-5L tLSS was used as an analytical tool for assessing the overall combined performance of the five dimensions. This approach appeared very useful in an earlier study demonstrating the discriminatory power of EQ-5D when comparing different condition groups (33). Differences in mean EQ-5D-5L tLSS and EQ VAS scores were tested with ANOVA, and the differences in median scores were studied with the Kruskal–Wallis H-test. Subsequently, we compared the health outcomes within groups of respondents, with and without a specific health condition. The outcomes of the different groups, based on the level of education, were compared within each country and within these groups. Univariate analyses were used to test the relation between the respondent characteristics and the EQ-5D-5L tLSS, and between the respondent characteristics and the EQ VAS. Subsequently, multivariate stepwise regression analyses models (using backward elimination) were constructed, starting with sex and age in the first step. In the second step, the level of education, work status, income, and a number of chronic conditions were offered as potential explaining variables. This was done for each country separately. SPSS version 25 for Windows (IBM SPSS Statistics, SPSS Inc., Chicago, IL) was used for statistical analyses. Statistical significance was determined by a *p* \< 0.05.

## Results

### Respondents

Total number of 10,172 respondents completed the survey. Of these, 3,026 respondents were from Italy, 3,027 were from the Netherlands, and 4,119 were from the UK. Characteristics of the respondents are presented in <a href="#T1" data-ref-type="table">Table 1</a>. The mean age of all the respondents was 44.5 years (SD 15.3), and the sample included an even representation of men and women. About half of the respondents had middle level education (49%), and a quarter of them had either low (26%) or high level education (25%), respectively. Most of the respondents were employed (52%). Household income was divided among the respondents as 22% (low), 41% (middle), 21% (high), and 16% (unknown). Half of the respondents had at least one chronic health condition. Depression or anxiety disorder was the most often reported chronic health condition (19%).

<div id="T1" class="table-wrap">

<div class="caption">

Characteristics of the study population.

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Characteristic</strong></th>
<th style="text-align: center;"><strong>Italy</strong></th>
<th style="text-align: center;"><strong>Netherlands N (%)</strong></th>
<th style="text-align: center;"><strong>UK N (%)</strong></th>
<th style="text-align: center;"><strong>All countries N (%)</strong></th>
</tr>
<tr>
<th></th>
<th style="text-align: center;"><strong>(<em>n</em> = 3,026)</strong></th>
<th style="text-align: center;"><strong>(<em>n</em> = 3,027)</strong></th>
<th style="text-align: center;"><strong>(<em>n</em> = 4,119)</strong></th>
<th style="text-align: center;"><strong>(<em>n</em> = 10,172)</strong></th>
</tr>
<tr>
<th></th>
<th style="text-align: center;"><strong>N (%)</strong></th>
<th style="text-align: center;"><strong>N (%)</strong></th>
<th style="text-align: center;"><strong>N (%)</strong></th>
<th style="text-align: center;"><strong>N (%)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Sex</strong>: Male</td>
<td style="text-align: center;">1,507 (49.8%)</td>
<td style="text-align: center;">1,520 (50.2%)</td>
<td style="text-align: center;">2,032 (49.3%)</td>
<td style="text-align: center;">5,059 (49.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Age [Mean (SD)]</td>
<td style="text-align: center;">45.0 (14.8)</td>
<td style="text-align: center;">44.7 (15.3)</td>
<td style="text-align: center;">44.0 (15.6)</td>
<td style="text-align: center;">44.5 (15.3)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>Age/sex categories</strong></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>Male</strong></td>
</tr>
<tr>
<td style="text-align: left;">18– &lt;25 year</td>
<td style="text-align: center;">148 (4.9%)</td>
<td style="text-align: center;">188 (6.2%)</td>
<td style="text-align: center;">263 (6.4%)</td>
<td style="text-align: center;">599 (5.9%)</td>
</tr>
<tr>
<td style="text-align: left;">25– &lt;40 year</td>
<td style="text-align: center;">384 (12.7%)</td>
<td style="text-align: center;">402 (13.3%)</td>
<td style="text-align: center;">602 (14.6%)</td>
<td style="text-align: center;">1,388 (13.6%)</td>
</tr>
<tr>
<td style="text-align: left;">40– &lt;60 year</td>
<td style="text-align: center;">673 (22.2%)</td>
<td style="text-align: center;">619 (20.4%)</td>
<td style="text-align: center;">765 (18.6%)</td>
<td style="text-align: center;">2,057 (20.2%)</td>
</tr>
<tr>
<td style="text-align: left;">60–75 year</td>
<td style="text-align: center;">302 (10.0%)</td>
<td style="text-align: center;">311 (10.3%)</td>
<td style="text-align: center;">402 (9.8%)</td>
<td style="text-align: center;">1,015 (10.0%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>Female</strong></td>
</tr>
<tr>
<td style="text-align: left;">18– &lt;25 year</td>
<td style="text-align: center;">142 (4.7%)</td>
<td style="text-align: center;">177 (5.8%)</td>
<td style="text-align: center;">271 (6.6%)</td>
<td style="text-align: center;">590 (5.8%)</td>
</tr>
<tr>
<td style="text-align: left;">25– &lt;40 year</td>
<td style="text-align: center;">435 (14.4%)</td>
<td style="text-align: center;">412 (13.6%)</td>
<td style="text-align: center;">620 (15.1%)</td>
<td style="text-align: center;">1,467 (14.4%)</td>
</tr>
<tr>
<td style="text-align: left;">40– &lt;60 year</td>
<td style="text-align: center;">644 (21.3%)</td>
<td style="text-align: center;">612 (20.2%)</td>
<td style="text-align: center;">777 (18.9%)</td>
<td style="text-align: center;">2,033 (20.0%)</td>
</tr>
<tr>
<td style="text-align: left;">60–75 year</td>
<td style="text-align: center;">298 (12.9%)</td>
<td style="text-align: center;">306 (10.1%)</td>
<td style="text-align: center;">419 (10.2%)</td>
<td style="text-align: center;">1,023 (10.1%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>Level of education</strong></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">880 (29.1%)</td>
<td style="text-align: center;">811 (26.8%)</td>
<td style="text-align: center;">937 (22.7%)</td>
<td style="text-align: center;">2,628 (25.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1,796 (59.4%)</td>
<td style="text-align: center;">1,420 (46.9%)</td>
<td style="text-align: center;">1,783 (43.3%)</td>
<td style="text-align: center;">4,999 (49.2%)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">350 (11.6%)</td>
<td style="text-align: center;">796 (26.3%)</td>
<td style="text-align: center;">1,399 (34.0%)</td>
<td style="text-align: center;">2,545 (25.0%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>Work status</strong></td>
</tr>
<tr>
<td style="text-align: left;">Employed</td>
<td style="text-align: center;">1,494 (49.4%)</td>
<td style="text-align: center;">1,635 (54.0%)</td>
<td style="text-align: center;">2,176 (52.8%)</td>
<td style="text-align: center;">5,305 (52.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: center;">704 (23.3%)</td>
<td style="text-align: center;">316 (10.4%)</td>
<td style="text-align: center;">365 (8.9%)</td>
<td style="text-align: center;">1,385 (13.6%)</td>
</tr>
<tr>
<td style="text-align: left;">Looking after others</td>
<td style="text-align: center;">120 (4.0%)</td>
<td style="text-align: center;">125 (4.1%)</td>
<td style="text-align: center;">277 (6.7%)</td>
<td style="text-align: center;">522 (5.1%)</td>
</tr>
<tr>
<td style="text-align: left;">Student</td>
<td style="text-align: center;">199 (6.6%)</td>
<td style="text-align: center;">209 (6.9%)</td>
<td style="text-align: center;">257 (6.2%)</td>
<td style="text-align: center;">665 (6.5%)</td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: center;">471 (15.6%)</td>
<td style="text-align: center;">386 (12.8%)</td>
<td style="text-align: center;">639 (15.5%)</td>
<td style="text-align: center;">1,496 (14.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Unable to work</td>
<td style="text-align: center;">38 (1.3%)</td>
<td style="text-align: center;">356 (11.8%)</td>
<td style="text-align: center;">405 (9.8%)</td>
<td style="text-align: center;">799 (7.9%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>Household income<a href="#TN1" data-ref-type="table-fn"><sup>*</sup></a></strong></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">871 (28.8%)</td>
<td style="text-align: center;">540 (17.8%)</td>
<td style="text-align: center;">870 (21.1%)</td>
<td style="text-align: center;">2,281 (22.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1,146 (37.9%)</td>
<td style="text-align: center;">1,270 (42.0%)</td>
<td style="text-align: center;">1,732 (42.0%)</td>
<td style="text-align: center;">4,148 (40.8%)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">510 (16.9%)</td>
<td style="text-align: center;">555 (18.3%)</td>
<td style="text-align: center;">1,070 (26.0%)</td>
<td style="text-align: center;">2,135 (21.0%)</td>
</tr>
<tr>
<td style="text-align: left;">Do not know/do not want to tell</td>
<td style="text-align: center;">499 (16.5%)</td>
<td style="text-align: center;">662 (21.9%)</td>
<td style="text-align: center;">447 (10.9%)</td>
<td style="text-align: center;">1,608 (15.8%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong><a href="#TN2" data-ref-type="table-fn"><sup>**</sup></a>Self-reported chronic health conditions, overall prevalence/single prevalence</strong></td>
</tr>
<tr>
<td style="text-align: left;">Asthma, chronic bronchitis</td>
<td style="text-align: center;">7.3/3.2%</td>
<td style="text-align: center;">9.3/3.6%</td>
<td style="text-align: center;">12.9/4.8%</td>
<td style="text-align: center;">10.1/4.0%</td>
</tr>
<tr>
<td style="text-align: left;">Severe heart disease</td>
<td style="text-align: center;">2.4/0.9%</td>
<td style="text-align: center;">3.3/1.0%</td>
<td style="text-align: center;">3.0/0.8%</td>
<td style="text-align: center;">2.9/0.9%</td>
</tr>
<tr>
<td style="text-align: left;">Stroke (sequelae)</td>
<td style="text-align: center;">1.3/0.3%</td>
<td style="text-align: center;">2.3/0.8%</td>
<td style="text-align: center;">1.7/0.5%</td>
<td style="text-align: center;">1.7/0.5%</td>
</tr>
<tr>
<td style="text-align: left;">Diabetes</td>
<td style="text-align: center;">7.1/3.0%</td>
<td style="text-align: center;">7.6/2.5%</td>
<td style="text-align: center;">8.5/3.2%</td>
<td style="text-align: center;">7.8/2.9%</td>
</tr>
<tr>
<td style="text-align: left;">Severe back complaints and/or arthrosis</td>
<td style="text-align: center;">14.6/4.9%</td>
<td style="text-align: center;">17.5/6.5%</td>
<td style="text-align: center;">15.4/4.1%</td>
<td style="text-align: center;">15.8/5.1%</td>
</tr>
<tr>
<td style="text-align: left;">Rheumatism</td>
<td style="text-align: center;">6.7 /1.8%</td>
<td style="text-align: center;">6.1/1.2%</td>
<td style="text-align: center;">4.3/1.1%</td>
<td style="text-align: center;">5.6/1.3%</td>
</tr>
<tr>
<td style="text-align: left;">Cancer</td>
<td style="text-align: center;">1.9/0.9%</td>
<td style="text-align: center;">4.2/1.5%</td>
<td style="text-align: center;">2.8/1.0%</td>
<td style="text-align: center;">3.0/1.1%</td>
</tr>
<tr>
<td style="text-align: left;">Memory problems</td>
<td style="text-align: center;">5.7/1.4%</td>
<td style="text-align: center;">5.1/0.9%</td>
<td style="text-align: center;">6.3/1.1%</td>
<td style="text-align: center;">5.7/1.1%</td>
</tr>
<tr>
<td style="text-align: left;">Depression or anxiety disorder</td>
<td style="text-align: center;">14.5/7.1%</td>
<td style="text-align: center;">11.8/5.0%</td>
<td style="text-align: center;">26.9/11.9%</td>
<td style="text-align: center;">18.7/8.4%</td>
</tr>
<tr>
<td style="text-align: left;">Other chronic health condition</td>
<td style="text-align: center;">8.0/15.3%</td>
<td style="text-align: center;">16.5/25.6%</td>
<td style="text-align: center;">8.3/0.3%</td>
<td style="text-align: center;">10.7/7.6%</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong><a href="#TN3" data-ref-type="table-fn"><sup>***</sup></a>Number of self-reported chronic health conditions</strong></td>
</tr>
<tr>
<td style="text-align: left;">No condition</td>
<td style="text-align: center;">1,683 (55.6%)</td>
<td style="text-align: center;">1,465 (48.4%)</td>
<td style="text-align: center;">1,921 (46.6%)</td>
<td style="text-align: center;">5,069 (49.8%)</td>
</tr>
<tr>
<td style="text-align: left;">1 condition</td>
<td style="text-align: center;">8,376 (27.7%)</td>
<td style="text-align: center;">936 (30.9%)</td>
<td style="text-align: center;">1,267 (30.8%)</td>
<td style="text-align: center;">3,040 (29.9%)</td>
</tr>
<tr>
<td style="text-align: left;">2 conditions</td>
<td style="text-align: center;">322 (10.6%)</td>
<td style="text-align: center;">370 (12.2%)</td>
<td style="text-align: center;">531 (12.9%)</td>
<td style="text-align: center;">1,223 (12.0%)</td>
</tr>
<tr>
<td style="text-align: left;">3 conditions</td>
<td style="text-align: center;">119 (3.9%)</td>
<td style="text-align: center;">150 (5.0%)</td>
<td style="text-align: center;">250 (6.1%)</td>
<td style="text-align: center;">519 (5.1%)</td>
</tr>
<tr>
<td style="text-align: left;">4 conditions</td>
<td style="text-align: center;">48 (1.6%)</td>
<td style="text-align: center;">72 (2.4%)</td>
<td style="text-align: center;">100 (2.4%)</td>
<td style="text-align: center;">220 (2.2%)</td>
</tr>
<tr>
<td style="text-align: left;">≥5 conditions</td>
<td style="text-align: center;">16 (0.5%)</td>
<td style="text-align: center;">34 (1.2%)</td>
<td style="text-align: center;">50 (1.2%)</td>
<td style="text-align: center;">101 (1.0%)</td>
</tr>
</tbody>
</table>

*Income was grouped as low (the UK, \<£14.000; Italy and the Netherlands, \<€20.000), middle (UK, £14.000–£34.999; Italy, €20.000–€39.999; and the Netherlands, €20.000–€49.999), and high (the UK, more than £34.999; Italy, more than €39.999; and the Netherlands more than €49.999)*.

*Prevalence of self-reported chronic health conditions, by type of health condition; overall prevalence: the sum of all patients reporting a specific health condition; single prevalence: the sum of patients only reporting that specific health condition, and thus having no other chronic health condition*.

*Total number of self-reported chronic health conditions*.

</div>

### Health Outcomes According to Country

Mean outcomes of the health measures are shown in <a href="#F1" data-ref-type="fig">Figure 1</a>, separately for each country. The tLSS was highest for respondents from Italy (mean: 90.7, SD: 11.8; median: 95.0, IQR: 85.0–100.0) and lowest for respondents from the UK (mean: 84.8, SD: 18.9; median: 90.0, IQR: 80.0–100.0). A similar pattern was seen for the EQ VAS; the EQ VAS score was the highest for respondents from Italy (mean: 77.6, SD: 17.4; median: 80.0, IQR: 70.0–90.0) and lowest for respondents from the UK (mean: 71.4, SD: 21.6; median: 78.0, IQR: 60.0–89.0).

<figure id="F1">
<p><img src="fpubh-09-744405-g0001.jpg" /></p>
<figcaption>Mean (95% CI) EQ-5D-5L transformed level sum score and mean EQ VAS for the three different countries studied.</figcaption>
</figure>

### Health Outcomes According to the Level of Education

In <a href="#T2" data-ref-type="table">Table 2</a>, health outcomes are tabulated according to the level of education. In the UK and Netherlands, the tLSS was lowest (“worst”) for respondents with a low education level and invariably better for respondents with middle and high educational levels. For Italian respondents, a higher tLSS was observed for respondents with a middle educational level compared to their counterparts with a high educational level. For the EQ VAS, we observed the same pattern, but generally, differences in EQ VAS scores between respondents with low, middle, and high educational levels were slightly smaller compared to the tLSS.

<div id="T2" class="table-wrap">

<div class="caption">

EQ-5D-5L transformed level sum score and EQ VAS outcomes for subgroups based on level of education in the three countries.

</div>

<table>
<thead>
<tr>
<th></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
</tr>
<tr>
<th></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7" style="text-align: left;"><strong>EQ-5D-5L transformed level sum score</strong></td>
</tr>
<tr>
<td style="text-align: left;">Education low</td>
<td style="text-align: center;">95.0 (85.0–100.0)</td>
<td style="text-align: center;">90.6 (12.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">90.0 (75.0–100.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.1 (16.3)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">90.0 (70.0–100.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">81.0 (21.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle</td>
<td style="text-align: center;">95.0 (85.0–100.0)</td>
<td style="text-align: center;">91.0 (11.4)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">95.0 (85.0–100.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">88.8 (14.1)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">90.0 (80.0–100.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">84.8 (19.1)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high</td>
<td style="text-align: center;">95.0 (85.0–100.0)</td>
<td style="text-align: center;">89.2 (13.3)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">95.0 (85.0–100.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">90.6 (13.4)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">95.0 (80.0–100.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">87.4 (16.5)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><strong>EQ VAS</strong></td>
</tr>
<tr>
<td style="text-align: left;">Education low</td>
<td style="text-align: center;">80.0 (70.0–90.0)</td>
<td style="text-align: center;">76.7 (18.8)</td>
<td style="text-align: center;">79.0 (61.0–90.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">74.0 (19.7)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">71.0 (50.0–87.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">67.2 (24.2)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle</td>
<td style="text-align: center;">80.0 (70.0–90.0)</td>
<td style="text-align: center;">78.2 (16.7)</td>
<td style="text-align: center;">80.0 (70.0–90.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">77.1 (17.5)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">78.0 (60.0–90.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">71.6 (21.7)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high</td>
<td style="text-align: center;">80.0 (70.0–90.0)</td>
<td style="text-align: center;">77.0 (17.4)</td>
<td style="text-align: center;">80.0 (70.0–90.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">77.4 (17.4)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.0 (65.0–90.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">73.9 (19.0)<a href="#TN4" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
</tbody>
</table>

*Statistically significantly different between subgroups based on level of education; p \< 0.05*.

</div>

### Health Outcomes for Subgroups With or Without a Chronic Health Condition

Mean and median tLSS and EQ VAS scores for subgroups of respondents with and without a particular chronic health condition are presented in <a href="#T3" data-ref-type="table">Tables 3A</a>,<a href="#T4" data-ref-type="table">B</a>. For each chronic health condition, statistically significant differences between respondents with low, middle, and high educational levels were observed for at least one outcome in at least one country, except for severe heart disease and rheumatism. Based on the tLSS, no statistically significant differences were found between subgroups based on the level of education in any country, among participants with severe heart disease, memory problems, and in those without chronic health conditions (<a href="#T3" data-ref-type="table">Table 3A</a>), whereas this was the case for participants with severe heart disease, stroke, rheumatism, and other chronic health conditions based on the EQ VAS (<a href="#T4" data-ref-type="table">Table 3B</a>). Overall, the number of statistically significant variables using the tLSS as the outcome was largely the same as when using EQ VAS.

<div id="T3" class="table-wrap">

<div class="caption">

EQ-5D-5L transformed level sum score per chronic health condition according to the level of education in the three countries.

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Chronic health condition</strong></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>(number of participants with the condition)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Asthma, chronic bronchitis (</strong><em><strong>n =</strong></em> <strong>1,031)</strong></td>
<td style="text-align: center;">90.0 (80.0–95.0)</td>
<td style="text-align: center;">85.8 (14.6)</td>
<td style="text-align: center;">85.0 (70.0–95.0)</td>
<td style="text-align: center;">81.5 (17.3)</td>
<td style="text-align: center;">85.0 (65.0–95.0)</td>
<td style="text-align: center;">76.2 (23.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 282)</td>
<td style="text-align: center;">90.0 (80.0–96.3)</td>
<td style="text-align: center;">86.5 (15.6)</td>
<td style="text-align: center;">80.0 (70.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">77.7 (17.1)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.0 (50.0–92.5)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.6 (25.5)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 483)</td>
<td style="text-align: center;">90.0 (80.0–95.0)</td>
<td style="text-align: center;">85.9 (14.7)</td>
<td style="text-align: center;">85.0 (75.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">81.9 (16.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (65.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">76.9 (23.2)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 266)</td>
<td style="text-align: center;">85.0 (85.0–95.0)</td>
<td style="text-align: center;">84.7 (13.0)</td>
<td style="text-align: center;">95.0 (85.0–100.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">87.5 (18.5)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">90.0 (70.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">79.6 (21.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Severe heart disease (</strong><em><strong>n =</strong></em> <strong>295)</strong></td>
<td style="text-align: center;">90.0 (75.0–95.0)</td>
<td style="text-align: center;">83.6 (16.1)</td>
<td style="text-align: center;">80.0 (66.3–93.8)</td>
<td style="text-align: center;">78.5 (17.7)</td>
<td style="text-align: center;">75.0 (55.0–90.0)</td>
<td style="text-align: center;">68.7 (25.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 91)</td>
<td style="text-align: center;">95.0 (75.0–100.0)</td>
<td style="text-align: center;">85.4 (21.2)</td>
<td style="text-align: center;">80.0 (65.0–93.8)</td>
<td style="text-align: center;">78.3 (17.2)</td>
<td style="text-align: center;">65.0 (40.0–90.0)</td>
<td style="text-align: center;">62.6 (27.4)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 132)</td>
<td style="text-align: center;">90.0 (75.0–95.0)</td>
<td style="text-align: center;">84.2 (13.7)</td>
<td style="text-align: center;">80.0 (68.8–90.0)</td>
<td style="text-align: center;">78.3 (16.8)</td>
<td style="text-align: center;">75.0 (51.3–90.0)</td>
<td style="text-align: center;">70.0 (24.0)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 72)</td>
<td style="text-align: center;">90.0 (70.0–92.3)</td>
<td style="text-align: center;">79.6 (18.9)</td>
<td style="text-align: center;">85.0 (68.8–95.0)</td>
<td style="text-align: center;">79.4 (21.5)</td>
<td style="text-align: center;">80.0 (55.0–90.0)</td>
<td style="text-align: center;">72.9 (24.0)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Consequences of a stroke (</strong><em><strong>n =</strong></em> <strong>177)</strong></td>
<td style="text-align: center;">85.0 (72.5–91.3)</td>
<td style="text-align: center;">80.1 (17.9)</td>
<td style="text-align: center;">75.0 (60.0–90.0)</td>
<td style="text-align: center;">73.9 (19.2)</td>
<td style="text-align: center;">65.0 (53.8–86.3)</td>
<td style="text-align: center;">65.6 (23.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 57)</td>
<td style="text-align: center;">85.0 (55.0–90.0)</td>
<td style="text-align: center;">75.9 (18.4)</td>
<td style="text-align: center;">72.5 (56.3–90.0)</td>
<td style="text-align: center;">72.8 (19.9)</td>
<td style="text-align: center;">62.5 (53.8–86.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">63.8 (23.2)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 71)</td>
<td style="text-align: center;">90.0 (75.0–95.0)</td>
<td style="text-align: center;">81.8 (16.1)</td>
<td style="text-align: center;">80.0 (60.0–90.0)</td>
<td style="text-align: center;">75.3 (18.6)</td>
<td style="text-align: center;">70.0 (65.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">77.4 (20.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 49)</td>
<td style="text-align: center;">90.0 (76.3–95.0)</td>
<td style="text-align: center;">81.9 (22.5)</td>
<td style="text-align: center;">75.0 (58.8–87.5)</td>
<td style="text-align: center;">72.8 (20.2)</td>
<td style="text-align: center;">60.0 (45.0–65.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">57.0 (22.4)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Diabetes (</strong><em><strong>n =</strong></em> <strong>797)</strong></td>
<td style="text-align: center;">90.0 (80.0–100.0)</td>
<td style="text-align: center;">86.3 (15.7)</td>
<td style="text-align: center;">85.0 (65.0–95.0)</td>
<td style="text-align: center;">79.0 (18.4)</td>
<td style="text-align: center;">80.0 (55.0–95.0)</td>
<td style="text-align: center;">73.5 (23.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 280)</td>
<td style="text-align: center;">95.0 (85.0–100.0)</td>
<td style="text-align: center;">89.8 (11.8)</td>
<td style="text-align: center;">75.0 (60.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">74.3 (19.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">75.0 (55.0–90.0)</td>
<td style="text-align: center;">70.6 (24.7)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 342)</td>
<td style="text-align: center;">90.0 (80.0–100.0)</td>
<td style="text-align: center;">85.5 (15.6)</td>
<td style="text-align: center;">85.0 (70.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">82.2 (16.9)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">77.5 (60.0–95.0)</td>
<td style="text-align: center;">74.6 (22.9)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 175)</td>
<td style="text-align: center;">90.0 (76.3–98.8)</td>
<td style="text-align: center;">82.3 (21.1)</td>
<td style="text-align: center;">87.5 (70.0–100.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">82.8 (17.5)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.0 (62.5–95.0)</td>
<td style="text-align: center;">75.5 (21.4)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Severe back complaints and/or arthrosis (</strong><em><strong>n =</strong></em> <strong>1,605)</strong></td>
<td style="text-align: center;">85.0 (70.0–90.0)</td>
<td style="text-align: center;">79.3 (15.3)</td>
<td style="text-align: center;">80.0 (65.0–90.0)</td>
<td style="text-align: center;">75.4 (16.9)</td>
<td style="text-align: center;">65.0 (45.0–80.0)</td>
<td style="text-align: center;">63.3 (22.8)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 534)</td>
<td style="text-align: center;">85.0 (70.0–90.0)</td>
<td style="text-align: center;">79.6 (16.0)</td>
<td style="text-align: center;">75.0 (65.0–85.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">73.6 (16.4)</td>
<td style="text-align: center;">60.0 (45.0–80.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">59.9 (4.6)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 746)</td>
<td style="text-align: center;">85.0 (70.0–90.0)</td>
<td style="text-align: center;">79.2 (14.4)</td>
<td style="text-align: center;">75.0 (65.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">75.7 (17.0)</td>
<td style="text-align: center;">70.0 (45.0–80.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">62.6 (4.6)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 325)</td>
<td style="text-align: center;">80.0 (70.0–90.0)</td>
<td style="text-align: center;">79.0 (17.5)</td>
<td style="text-align: center;">80.0 (70.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">78.3 (17.5)</td>
<td style="text-align: center;">75.0 (55.0–85.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">68.7 (4.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Rheumatism (</strong><em><strong>n =</strong></em> <strong>568)</strong></td>
<td style="text-align: center;">85.0 (75.0–90.0)</td>
<td style="text-align: center;">80.1 (16.5)</td>
<td style="text-align: center;">70.0 (60.0–85.0)</td>
<td style="text-align: center;">71.0 (16.5)</td>
<td style="text-align: center;">75.0 (50.0–85.0)</td>
<td style="text-align: center;">66.9 (23.4)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 204)</td>
<td style="text-align: center;">85.0 (70.0–95.0)</td>
<td style="text-align: center;">79.5 (17.9)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.0 (70.0–95.0)</td>
<td style="text-align: center;">69.7 (14.5)</td>
<td style="text-align: center;">72.5 (50.0–85.0)</td>
<td style="text-align: center;">65.7 (22.5)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 265)</td>
<td style="text-align: center;">85.0 (78.8–90.0)</td>
<td style="text-align: center;">82.2 (14.2)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (75.0–95.0)</td>
<td style="text-align: center;">72.3 (17.0)</td>
<td style="text-align: center;">75.0 (47.5–90.0)</td>
<td style="text-align: center;">66.6 (24.9)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 99)</td>
<td style="text-align: center;">75.0 (70.0–90.0)</td>
<td style="text-align: center;">73.0 (20.7)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">95.0 (85.0–100.0)</td>
<td style="text-align: center;">70.8 (19.8)</td>
<td style="text-align: center;">80.0 (52.5–85.0)</td>
<td style="text-align: center;">69.4 (22.8)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Cancer (</strong><em><strong>n =</strong></em> <strong>301)</strong></td>
<td style="text-align: center;">85.0 (75.0–95.0)</td>
<td style="text-align: center;">81.9 (17.5)</td>
<td style="text-align: center;">85.0 (70.0–95.0)</td>
<td style="text-align: center;">81.4 (17.3)</td>
<td style="text-align: center;">85.0 (65.0–95.0)</td>
<td style="text-align: center;">77.7 (22.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 80)</td>
<td style="text-align: center;">90.0 (77.5–95.0)</td>
<td style="text-align: center;">82.3 (20.8)</td>
<td style="text-align: center;">75.0 (65.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">76.1 (20.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (45.0–90.0)</td>
<td style="text-align: center;">70.8 (25.5)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 141)</td>
<td style="text-align: center;">85.0 (75.0–95.0)</td>
<td style="text-align: center;">82.4 (16.0)</td>
<td style="text-align: center;">85.0 (70.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.9 (16.5)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (70.0–95.0)</td>
<td style="text-align: center;">82.3 (15.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 80)</td>
<td style="text-align: center;">85.0 (75.0–95.0)</td>
<td style="text-align: center;">78.6 (21.0)</td>
<td style="text-align: center;">95.0 (80.0–100.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">88.3 (12.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">90.0 (65.0–100.0)</td>
<td style="text-align: center;">77.7 (25.4)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Memory problems (</strong><em><strong>n =</strong></em> <strong>584)</strong></td>
<td style="text-align: center;">87.5 (75.0–95.0)</td>
<td style="text-align: center;">82.7 (15.5)</td>
<td style="text-align: center;">75.0 (60.0–90.0)</td>
<td style="text-align: center;">74.6 (18.2)</td>
<td style="text-align: center;">70.0 (45.0–85.0)</td>
<td style="text-align: center;">65.5 (24.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 187)</td>
<td style="text-align: center;">90.0 (80.0–92.5)</td>
<td style="text-align: center;">84.2 (14.1)</td>
<td style="text-align: center;">75.0 (60.0–90.0)</td>
<td style="text-align: center;">73.6 (19.3)</td>
<td style="text-align: center;">65.0 (45.0–80.0)</td>
<td style="text-align: center;">63.2 (22.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 264)</td>
<td style="text-align: center;">90.0 (75.0–95.0)</td>
<td style="text-align: center;">82.2 (16.1)</td>
<td style="text-align: center;">75.0 (60.0–90.0)</td>
<td style="text-align: center;">75.1 (17.0)</td>
<td style="text-align: center;">75.0 (42.5–90.0)</td>
<td style="text-align: center;">65.7 (26.8)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 133)</td>
<td style="text-align: center;">85.0 (75.0–95.0)</td>
<td style="text-align: center;">82.0 (16.4)</td>
<td style="text-align: center;">80.0 (62.5–92.5)</td>
<td style="text-align: center;">75.8 (19.7)</td>
<td style="text-align: center;">70.0 (50.0–90.0)</td>
<td style="text-align: center;">67.6 (22.5)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Depression or anxiety disorder (</strong><em><strong>n =</strong></em> <strong>1,903)</strong></td>
<td style="text-align: center;">85.0 (75.0–90.0)</td>
<td style="text-align: center;">80.2 (13.7)</td>
<td style="text-align: center;">80.0 (65.0–90.0)</td>
<td style="text-align: center;">76.3 (16.1)</td>
<td style="text-align: center;">75.0 (60.0–90.0)</td>
<td style="text-align: center;">70.2 (21.5)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 497)</td>
<td style="text-align: center;">85.0 (75.0–90.0)</td>
<td style="text-align: center;">81.3 (12.7)</td>
<td style="text-align: center;">75.0 (60.0–85.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">72.6 (17.2)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.0 (50.0–85.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">64.3 (22.5)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 918)</td>
<td style="text-align: center;">85.0 (75.0–90.0)</td>
<td style="text-align: center;">79.9 (14.1)</td>
<td style="text-align: center;">80.0 (70.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">76.8 (16.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">75.0 (55.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">69.8 (22.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 488)</td>
<td style="text-align: center;">85.0 (75.0–90.0)</td>
<td style="text-align: center;">79.4 (13.6)</td>
<td style="text-align: center;">85.0 (75.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">81.2 (13.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.0 (65.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">74.9 (18.7)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Other chronic health conditions (</strong><em><strong>n =</strong></em> <strong>1,084)</strong></td>
<td style="text-align: center;">90.0 (80.0–95.0)</td>
<td style="text-align: center;">84.4 (14.5)</td>
<td style="text-align: center;">85.0 (70.0–95.0)</td>
<td style="text-align: center;">79.6 (16.6)</td>
<td style="text-align: center;">70.0 (50.0–85.0)</td>
<td style="text-align: center;">66.6 (23.1)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 313)</td>
<td style="text-align: center;">85.0 (67.5–95.0)</td>
<td style="text-align: center;">81.0 (16.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.0 (65.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">76.1 (17.6)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.0 (45.0–85.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">64.6 (25.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 518)</td>
<td style="text-align: center;">90.0 (80.0–95.0)</td>
<td style="text-align: center;">85.8 (13.1)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (70.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">80.2 (16.3)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.0 (45.0–80.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">63.4 (23.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 253)</td>
<td style="text-align: center;">90.0 (80.0–95.0)</td>
<td style="text-align: center;">86.5 (15.4)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (75.0–95.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">83.1 (14.9)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">75.0 (60.0–90.0)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">72.1 (20.7)<a href="#TN5" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>No chronic health conditions (</strong><em><strong>n =</strong></em> <strong>5,046)</strong></td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.6 (6.7)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.9 (7.6)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.3 (8.6)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 1,160)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.3 (7.3)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.5 (8.4)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">94.8 (9.5)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 2,583)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.7 (6.3)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">96.0 (6.7)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.1 (8.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 1,326)</td>
<td style="text-align: center;">100.0 (90.0–100.0)</td>
<td style="text-align: center;">95.5 (6.8)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">96.0 (8.2)</td>
<td style="text-align: center;">100.0 (95.0–100.0)</td>
<td style="text-align: center;">95.6 (8.5)</td>
</tr>
</tbody>
</table>

*Statistically significantly different between subgroups based on level of education; p \< 0.05*.

</div>

<div id="T4" class="table-wrap">

<div class="caption">

EQ VAS per chronic health condition according to the level of education in the three countries.

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Chronic health condition</strong></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>(number of participants with the condition)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
<th style="text-align: center;"><strong>Median (IQR)</strong></th>
<th style="text-align: center;"><strong>Mean (SD)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Asthma, chronic bronchitis (</strong><em><strong>n =</strong></em> <strong>1,031)</strong></td>
<td style="text-align: center;">79.0 (60.0–87.0)</td>
<td style="text-align: center;">72.0 (19.8)</td>
<td style="text-align: center;">70.0 (60.0–82.5)</td>
<td style="text-align: center;">68.8 (20.0)</td>
<td style="text-align: center;">70.0 (49.8–81.0)</td>
<td style="text-align: center;">63.8 (23.1)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 282)</td>
<td style="text-align: center;">79.0 (50.0–90.0)</td>
<td style="text-align: center;">68.6 (23.8)</td>
<td style="text-align: center;">65.0 (51.0–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">64.7 (21.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">60.0 (40.0–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">59.1 (25.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 483)</td>
<td style="text-align: center;">80.0 (60.0–87.0)</td>
<td style="text-align: center;">72.6 (19.2)</td>
<td style="text-align: center;">70.0 (60.0–81.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">68.4 (19.6)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.0 (50.0–81.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.1 (23.3)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 266)</td>
<td style="text-align: center;">77.0 (66.0–85.0)</td>
<td style="text-align: center;">74.6 (14.7)</td>
<td style="text-align: center;">80.0 (70.0–90.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">77.0 (16.8)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.0 (50.8–81.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.9 (21.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Severe heart disease (</strong><em><strong>n =</strong></em> <strong>295)</strong></td>
<td style="text-align: center;">70.0 (50.0–80.0)</td>
<td style="text-align: center;">64.7 (20.4)</td>
<td style="text-align: center;">70.0 (51.0–79.8)</td>
<td style="text-align: center;">64.7 (19.9)</td>
<td style="text-align: center;">60.0 (40.0–80.0)</td>
<td style="text-align: center;">57.0 (25.7)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 91)</td>
<td style="text-align: center;">76.0 (45.0–80.0)</td>
<td style="text-align: center;">64.9 (30.3)</td>
<td style="text-align: center;">70.0 (60.0–76.5)</td>
<td style="text-align: center;">66.2 (15.5)</td>
<td style="text-align: center;">50.0 (31.0–74.5)</td>
<td style="text-align: center;">50.6 (25.8)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 132)</td>
<td style="text-align: center;">67.5 (50.0–79.3)</td>
<td style="text-align: center;">64.3 (17.1)</td>
<td style="text-align: center;">64.0 (50.0–82.0)</td>
<td style="text-align: center;">63.5 (22.9)</td>
<td style="text-align: center;">60.5 (43.8–79.0)</td>
<td style="text-align: center;">59.3 (23.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 72)</td>
<td style="text-align: center;">69.0 (46.0–82.5)</td>
<td style="text-align: center;">65.8 (21.1)</td>
<td style="text-align: center;">70.0 (50.0–78.8)</td>
<td style="text-align: center;">64.3 (21.6)</td>
<td style="text-align: center;">69.0 (40.0–80.0)</td>
<td style="text-align: center;">60.6 (27.7)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Consequences of a stroke (</strong><em><strong>n =</strong></em> <strong>177)</strong></td>
<td style="text-align: center;">76.0 (50.8–86.8)</td>
<td style="text-align: center;">66.5 (25.3)</td>
<td style="text-align: center;">63.0 (55.0–79.5)</td>
<td style="text-align: center;">64.8 (18.5)</td>
<td style="text-align: center;">62.0 (35.0–80.3)</td>
<td style="text-align: center;">58.5 (27.9)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 57)</td>
<td style="text-align: center;">69.0 (59.0–82.0)</td>
<td style="text-align: center;">65.5 (24.3)</td>
<td style="text-align: center;">61.0 (59.0–80.8)</td>
<td style="text-align: center;">65.2 (21.7)</td>
<td style="text-align: center;">50.0 (31.0–79.5)</td>
<td style="text-align: center;">53.4 (31.1)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 71)</td>
<td style="text-align: center;">80.0 (50.0–90.0)</td>
<td style="text-align: center;">66.8 (26.7)</td>
<td style="text-align: center;">64.0 (51.0–80.0)</td>
<td style="text-align: center;">65.8 (16.0)</td>
<td style="text-align: center;">74.0 (60.5–80.0)</td>
<td style="text-align: center;">69.0 (19.4)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 49)</td>
<td style="text-align: center;">78.0 (43.5–89.0)</td>
<td style="text-align: center;">67.0 (26.5)</td>
<td style="text-align: center;">64.0 (55.5–71.3)</td>
<td style="text-align: center;">62.6 (19.7)</td>
<td style="text-align: center;">45.0 (33.0–83.0)</td>
<td style="text-align: center;">54.6 (29.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Diabetes (</strong><em><strong>n =</strong></em> <strong>797)</strong></td>
<td style="text-align: center;">75.0 (61.0–85.0)</td>
<td style="text-align: center;">71.9 (18.0)</td>
<td style="text-align: center;">70.0 (54.0–80.0)</td>
<td style="text-align: center;">67.2 (19.3)</td>
<td style="text-align: center;">68.0 (41.0–80.0)</td>
<td style="text-align: center;">61.1 (24.1)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 280)</td>
<td style="text-align: center;">77.0 (62.0–90.0)</td>
<td style="text-align: center;">73.6 (18.6)</td>
<td style="text-align: center;">62.0 (50.0–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">63.7 (20.9)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">60.0 (40.0–80.0)</td>
<td style="text-align: center;">58.3 (24.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 342)</td>
<td style="text-align: center;">75.0 (61.0–84.0)</td>
<td style="text-align: center;">72.0 (17.0)</td>
<td style="text-align: center;">70.0 (56.5–81.8)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">67.6 (19.5)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">64.0 (47.5–80.0)</td>
<td style="text-align: center;">61.9 (23.6)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 175)</td>
<td style="text-align: center;">72.5 (58.0–80.5)</td>
<td style="text-align: center;">67.9 (20.7)</td>
<td style="text-align: center;">75.0 (60.8–81.3)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">73.3 (13.6)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.0 (44.0–81.5)</td>
<td style="text-align: center;">63.6 (24.4)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Severe back complaints and/or arthrosis (</strong><em><strong>n =</strong></em> <strong>1,605)</strong></td>
<td style="text-align: center;">70.0 (52.0–81.0)</td>
<td style="text-align: center;">67.0 (19.7)</td>
<td style="text-align: center;">70.0 (56.0–80.0)</td>
<td style="text-align: center;">66.6 (19.6)</td>
<td style="text-align: center;">59.0 (40.0–71.3)</td>
<td style="text-align: center;">54.7 (23.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 534)</td>
<td style="text-align: center;">70.0 (51.0–81.0)</td>
<td style="text-align: center;">67.2 (20.8)</td>
<td style="text-align: center;">70.0 (51.0–80.0)</td>
<td style="text-align: center;">64.3 (19.5)</td>
<td style="text-align: center;">50.0 (38.3–70.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">50.4 (23.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 746)</td>
<td style="text-align: center;">70.0 (55.0–80.0)</td>
<td style="text-align: center;">67.1 (19.0)</td>
<td style="text-align: center;">70.0 (57.0–80.0)</td>
<td style="text-align: center;">67.1 (19.8)</td>
<td style="text-align: center;">60.0 (33.5–72.3)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">54.7 (23.4)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 325)</td>
<td style="text-align: center;">67.0 (50.0–81.0)</td>
<td style="text-align: center;">65.9 (19.7)</td>
<td style="text-align: center;">70.0 (60.0–84.3)</td>
<td style="text-align: center;">69.5 (18.9)</td>
<td style="text-align: center;">62.5 (50.0–75.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">60.1 (22.4)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Rheumatism (</strong><em><strong>n =</strong></em> <strong>568)</strong></td>
<td style="text-align: center;">71.0 (59.3–81.0)</td>
<td style="text-align: center;">68.6 (20.4)</td>
<td style="text-align: center;">60.0 (50.0–74.3)</td>
<td style="text-align: center;">60.4 (19.0)</td>
<td style="text-align: center;">60.0 (40.0–77.5)</td>
<td style="text-align: center;">56.6 (23.9)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 204)</td>
<td style="text-align: center;">72.0 (59.0–85.0)</td>
<td style="text-align: center;">68.5 (24.2)</td>
<td style="text-align: center;">60.0 (46.5–70.5)</td>
<td style="text-align: center;">59.0 (18.6)</td>
<td style="text-align: center;">60.0 (40.0–72.8)</td>
<td style="text-align: center;">56.2 (22.7)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 265)</td>
<td style="text-align: center;">73.5 (60.0–81.0)</td>
<td style="text-align: center;">70.0 (18.7)</td>
<td style="text-align: center;">61.0 (50.0–79.0)</td>
<td style="text-align: center;">61.6 (18.5)</td>
<td style="text-align: center;">60.0 (38.5–80.0)</td>
<td style="text-align: center;">56.4 (24.5)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 99)</td>
<td style="text-align: center;">61.0 (51.0–75.0)</td>
<td style="text-align: center;">63.3 (17.2)</td>
<td style="text-align: center;">60.0 (50.0–75.0)</td>
<td style="text-align: center;">60.8 (21.2)</td>
<td style="text-align: center;">61.0 (40.0–80.0)</td>
<td style="text-align: center;">57.5 (25.4)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Cancer (</strong><em><strong>n =</strong></em> <strong>301)</strong></td>
<td style="text-align: center;">70.0 (50.0–82.0)</td>
<td style="text-align: center;">67.0 (20.1)</td>
<td style="text-align: center;">71.0 (60.0–86.0)</td>
<td style="text-align: center;">70.4 (20.2)</td>
<td style="text-align: center;">69.5 (45.3–81.0)</td>
<td style="text-align: center;">61.8 (24.3)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 80)</td>
<td style="text-align: center;">75.0 (50.0–81.5)</td>
<td style="text-align: center;">65.4 (23.3)</td>
<td style="text-align: center;">70.0 (57.5–85.5)</td>
<td style="text-align: center;">68.5 (21.0)</td>
<td style="text-align: center;">50.5 (31.0–76.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">52.5 (25.4)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 141)</td>
<td style="text-align: center;">70.0 (50.0–82.0)</td>
<td style="text-align: center;">67.9 (18.3)</td>
<td style="text-align: center;">70.0 (58.3–85.0)</td>
<td style="text-align: center;">68.9 (19.8)</td>
<td style="text-align: center;">70.0 (55.5–80.5)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.8 (18.9)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 80)</td>
<td style="text-align: center;">71.0 (50.0–89.0)</td>
<td style="text-align: center;">64.6 (25.7)</td>
<td style="text-align: center;">77.5 (65.3–90.0)</td>
<td style="text-align: center;">75.4 (20.0)</td>
<td style="text-align: center;">73.0 (42.5–87.5)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">64.1 (27.4)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Memory problems (</strong><em><strong>n =</strong></em> <strong>584)</strong></td>
<td style="text-align: center;">72.0 (60.0–84.8)</td>
<td style="text-align: center;">70.1 (20.2)</td>
<td style="text-align: center;">62.0 (50.0–80.0)</td>
<td style="text-align: center;">61.8 (23.0)</td>
<td style="text-align: center;">60.0 (39.8–80.0)</td>
<td style="text-align: center;">57.2 (25.2)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 187)</td>
<td style="text-align: center;">79.0 (60.0–81.0)</td>
<td style="text-align: center;">69.4 (20.7)</td>
<td style="text-align: center;">70.0 (50.0–81.0)</td>
<td style="text-align: center;">62.8 (26.1)</td>
<td style="text-align: center;">50.0 (33.0–72.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">51.0 (24.4)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 264)</td>
<td style="text-align: center;">71.0 (60.0–83.5)</td>
<td style="text-align: center;">69.5 (20.3)</td>
<td style="text-align: center;">61.0 (29.8–80.3)</td>
<td style="text-align: center;">62.0 (19.6)</td>
<td style="text-align: center;">67.5 (39.5–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">58.5 (26.4)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 133)</td>
<td style="text-align: center;">73.5 (61.5–91.3)</td>
<td style="text-align: center;">73.1 (19.8)</td>
<td style="text-align: center;">67.0 (40.0–79.0)</td>
<td style="text-align: center;">58.8 (24.7)</td>
<td style="text-align: center;">68.0 (40.8–82.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">61.8 (23.4)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Depression or anxiety disorder (</strong><em><strong>n =</strong></em> <strong>1,903)</strong></td>
<td style="text-align: center;">70.0 (52.0–80.0)</td>
<td style="text-align: center;">66.6 (19.5)</td>
<td style="text-align: center;">66.0 (50.0–80.0)</td>
<td style="text-align: center;">63.6 (19.0)</td>
<td style="text-align: center;">60.0 (40.0–78.0)</td>
<td style="text-align: center;">58.2 (23.1)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 497)</td>
<td style="text-align: center;">72.0 (61.0–83.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.9 (17.9)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.0 (49.8–79.0)</td>
<td style="text-align: center;">61.9 (21.1)</td>
<td style="text-align: center;">50.0 (38.0–71.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">52.0 (24.3)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 918)</td>
<td style="text-align: center;">70.0 (50.0–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">64.9 (20.6)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.0 (50.0–80.0)</td>
<td style="text-align: center;">63.2 (18.9)</td>
<td style="text-align: center;">60.0 (40.0–78.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">58.1 (23.6)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 488)</td>
<td style="text-align: center;">69.5 (52.0–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">65.6 (16.7)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">70.0 (60.0–80.0)</td>
<td style="text-align: center;">67.6 (15.1)</td>
<td style="text-align: center;">68.0 (50.0–80.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">62.9 (20.3)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Other chronic health conditions (</strong><em><strong>n =</strong></em> <strong>1,084)</strong></td>
<td style="text-align: center;">72.0 (60.0–85.0)</td>
<td style="text-align: center;">69.0 (20.8)</td>
<td style="text-align: center;">70.0 (56.5–80.0)</td>
<td style="text-align: center;">66.7 (19.5)</td>
<td style="text-align: center;">60.0 (39.0–72.0)</td>
<td style="text-align: center;">55.0 (23.7)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 313)</td>
<td style="text-align: center;">64.0 (50.0–83.0)</td>
<td style="text-align: center;">64.4 (22.8)</td>
<td style="text-align: center;">70.0 (50.0–80.0)</td>
<td style="text-align: center;">65.1 (19.7)</td>
<td style="text-align: center;">57.0 (32.5–74.5)</td>
<td style="text-align: center;">53.6 (24.7)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 518)</td>
<td style="text-align: center;">75.5 (62.0–81.8)</td>
<td style="text-align: center;">71.5 (18.4)</td>
<td style="text-align: center;">70.0 (58.0–80.0)</td>
<td style="text-align: center;">66.3 (19.5)</td>
<td style="text-align: center;">55.0 (31.0–71.0)</td>
<td style="text-align: center;">52.4 (24.4)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 253)</td>
<td style="text-align: center;">80.0 (60.0–86.8)</td>
<td style="text-align: center;">69.6 (23.8)</td>
<td style="text-align: center;">73.0 (60.0–81.0)</td>
<td style="text-align: center;">69.6 (19.1)</td>
<td style="text-align: center;">61.0 (40.0–76.8)</td>
<td style="text-align: center;">59.3 (21.5)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>No chronic health conditions (</strong><em><strong>n =</strong></em> <strong>5,046)</strong></td>
<td style="text-align: center;">85.0 (79.0–91.0)</td>
<td style="text-align: center;">83.2 (13.9)</td>
<td style="text-align: center;">85.0 (79.0–92.0)</td>
<td style="text-align: center;">83.8 (13.6)</td>
<td style="text-align: center;">83.0 (72.0–91.0)</td>
<td style="text-align: center;">81.0 (15.7)</td>
</tr>
<tr>
<td style="text-align: left;">Education low (<em>n =</em> 1,160)</td>
<td style="text-align: center;">85.0 (71.0–92.0)</td>
<td style="text-align: center;">81.6 (16.2)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">89.0 (79.0–95.0)</td>
<td style="text-align: center;">84.0 (14.7)</td>
<td style="text-align: center;">82.0 (70.3–92.0)</td>
<td style="text-align: center;">79.9 (18.5)</td>
</tr>
<tr>
<td style="text-align: left;">Education middle (<em>n =</em> 2,583)</td>
<td style="text-align: center;">85.0 (80.0–91.0)</td>
<td style="text-align: center;">83.6 (13.0)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">86.5 (80.0–93.0)</td>
<td style="text-align: center;">84.5 (12.5)</td>
<td style="text-align: center;">82.0 (72.0–91.0)</td>
<td style="text-align: center;">81.0 (15.8)</td>
</tr>
<tr>
<td style="text-align: left;">Education high (<em>n =</em> 1,326)</td>
<td style="text-align: center;">85.0 (80.0–93.0)</td>
<td style="text-align: center;">84.7 (11.2)<a href="#TN6" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">85.0 (78.3–90.0)</td>
<td style="text-align: center;">82.5 (14.5)</td>
<td style="text-align: center;">84.0 (75.0–90.0)</td>
<td style="text-align: center;">81.5 (14.0)</td>
</tr>
</tbody>
</table>

*Statistically significantly different between subgroups based on level of education; p \< 0.05*.

</div>

### Factors Associated With EQ-5D-5L Transformed Level Sum Score and EQ VAS

In <a href="#T5" data-ref-type="table">Table 4</a>, the univariate regression outcomes for the tLSS and EQ VAS are presented for each country separately. Negative coefficients represent a worse outcome compared to the reference group. Compared to the respondents with a high level of education, low and middle levels of education were associated with a worse outcome for both the tLSS and EQ VAS in the UK and Dutch samples, but not in the Italian sample. Low and middle levels of education (compared to a high level) were associated with a better outcome based on the tLSS for the Italian sample; however, no significant relation was seen based on the EQ VAS. Having an increased number of chronic health conditions was consistently associated with a decreased health outcome. Other factors associated with the outcomes are presented in <a href="#T5" data-ref-type="table">Table 4</a>.

<div id="T5" class="table-wrap">

<div class="caption">

Univariate analyses of participant characteristics and the EQ-5D-5L transformed level sum score and EQ VAS in the three countries.

</div>

<table>
<thead>
<tr>
<th></th>
<th colspan="6" style="text-align: center;"><strong>EQ-5D-5L level sum score<a href="#TN7" data-ref-type="table-fn"><sup>*</sup></a></strong></th>
<th colspan="6" style="text-align: center;"><strong>EQ VAS</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>Characteristic</strong></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
</tr>
<tr>
<th></th>
<th style="text-align: center;"><strong>Coef</strong>.</th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><strong><em>P-</em>value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Sex</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.005</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.064</strong></td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">2.160</td>
<td></td>
<td style="text-align: center;">2.595</td>
<td></td>
<td style="text-align: center;">1.667</td>
<td></td>
<td style="text-align: center;">2.287</td>
<td></td>
<td style="text-align: center;">3.467</td>
<td></td>
<td style="text-align: center;">1.245</td>
<td></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>Female (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Age category</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.112</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td style="text-align: left;">18– &lt;25 year</td>
<td style="text-align: center;">2.984</td>
<td></td>
<td style="text-align: center;">1.375</td>
<td></td>
<td style="text-align: center;">4.919</td>
<td></td>
<td style="text-align: center;">4.090</td>
<td></td>
<td style="text-align: center;">4.353</td>
<td></td>
<td style="text-align: center;">3.394</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">25– &lt;40 year</td>
<td style="text-align: center;">0.901</td>
<td></td>
<td style="text-align: center;">1.419</td>
<td></td>
<td style="text-align: center;">3.982</td>
<td></td>
<td style="text-align: center;">1.930</td>
<td></td>
<td style="text-align: center;">1.064</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">40– &lt;60 year (ref)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">3.894</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">60–75 year</td>
<td style="text-align: center;">−0.935</td>
<td></td>
<td style="text-align: center;">0.220</td>
<td></td>
<td style="text-align: center;">1.484</td>
<td></td>
<td style="text-align: center;">−2.318</td>
<td></td>
<td style="text-align: center;">1.584</td>
<td></td>
<td style="text-align: center;">2.921</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Highest level of education</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.038</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.095</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">1.368</td>
<td></td>
<td style="text-align: center;">−5.486</td>
<td></td>
<td style="text-align: center;">−6.325</td>
<td></td>
<td style="text-align: center;">−0.242</td>
<td></td>
<td style="text-align: center;">−3.342</td>
<td></td>
<td style="text-align: center;">−6.781</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1.760</td>
<td></td>
<td style="text-align: center;">−1.774</td>
<td></td>
<td style="text-align: center;">−2.602</td>
<td></td>
<td style="text-align: center;">1.216</td>
<td></td>
<td style="text-align: center;">−0.296</td>
<td></td>
<td style="text-align: center;">−2.294</td>
<td></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>High (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Work status</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>Employed (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: center;">−0.957</td>
<td></td>
<td style="text-align: center;">−6.180</td>
<td></td>
<td style="text-align: center;">−9.026</td>
<td></td>
<td style="text-align: center;">−1.342</td>
<td></td>
<td style="text-align: center;">−4.574</td>
<td></td>
<td style="text-align: center;">−8.249</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Looking after others</td>
<td style="text-align: center;">−0.690</td>
<td></td>
<td style="text-align: center;">−5.683</td>
<td></td>
<td style="text-align: center;">−1.940</td>
<td></td>
<td style="text-align: center;">−1.941</td>
<td></td>
<td style="text-align: center;">−4.566</td>
<td></td>
<td style="text-align: center;">−1.305</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Student</td>
<td style="text-align: center;">1.834</td>
<td></td>
<td style="text-align: center;">−0.783</td>
<td></td>
<td style="text-align: center;">0.678</td>
<td></td>
<td style="text-align: center;">2.347</td>
<td></td>
<td style="text-align: center;">−0.608</td>
<td></td>
<td style="text-align: center;">−0.702</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: center;">−2.406</td>
<td></td>
<td style="text-align: center;">−3.013</td>
<td></td>
<td style="text-align: center;">−5.558</td>
<td></td>
<td style="text-align: center;">−3.568</td>
<td></td>
<td style="text-align: center;">−1.439</td>
<td></td>
<td style="text-align: center;">−2.966</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Unable to work</td>
<td style="text-align: center;">−24.509</td>
<td></td>
<td style="text-align: center;">−20.163</td>
<td></td>
<td style="text-align: center;">−36.006</td>
<td></td>
<td style="text-align: center;">−31.010</td>
<td></td>
<td style="text-align: center;">−20.512</td>
<td></td>
<td style="text-align: center;">−29.239</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Household income</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.009</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">0.104</td>
<td></td>
<td style="text-align: center;">−6.239</td>
<td></td>
<td style="text-align: center;">−11.122</td>
<td></td>
<td style="text-align: center;">−0.338</td>
<td></td>
<td style="text-align: center;">−8.328</td>
<td></td>
<td style="text-align: center;">−10.016</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1.372</td>
<td></td>
<td style="text-align: center;">−1.633</td>
<td></td>
<td style="text-align: center;">−5.141</td>
<td></td>
<td style="text-align: center;">0.916</td>
<td></td>
<td style="text-align: center;">−1.63</td>
<td></td>
<td style="text-align: center;">−5.097</td>
<td></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>High (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;">Do not know/do not want to tell</td>
<td style="text-align: center;">2.758</td>
<td></td>
<td style="text-align: center;">0.263</td>
<td></td>
<td style="text-align: center;">−4.762</td>
<td></td>
<td style="text-align: center;">2.826</td>
<td></td>
<td style="text-align: center;">−0.945</td>
<td></td>
<td style="text-align: center;">−3.752</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Number of chronic health conditions</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>No condition (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;">1 condition</td>
<td style="text-align: center;">−8.023</td>
<td></td>
<td style="text-align: center;">−10.348</td>
<td></td>
<td style="text-align: center;">−11.894</td>
<td></td>
<td style="text-align: center;">−9.780</td>
<td></td>
<td style="text-align: center;">−10.083</td>
<td></td>
<td style="text-align: center;">−11.649</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">2 conditions</td>
<td style="text-align: center;">−13.974</td>
<td></td>
<td style="text-align: center;">−17.307</td>
<td></td>
<td style="text-align: center;">−23.462</td>
<td></td>
<td style="text-align: center;">−14.965</td>
<td></td>
<td style="text-align: center;">−17.908</td>
<td></td>
<td style="text-align: center;">−22.196</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">3 conditions</td>
<td style="text-align: center;">−16.204</td>
<td></td>
<td style="text-align: center;">−24.081</td>
<td></td>
<td style="text-align: center;">−34.620</td>
<td></td>
<td style="text-align: center;">−17.974</td>
<td></td>
<td style="text-align: center;">−22.625</td>
<td></td>
<td style="text-align: center;">−27.615</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">4 conditions</td>
<td style="text-align: center;">−26.198</td>
<td></td>
<td style="text-align: center;">−29.456</td>
<td></td>
<td style="text-align: center;">−44.110</td>
<td></td>
<td style="text-align: center;">−25.209</td>
<td></td>
<td style="text-align: center;">−28.014</td>
<td></td>
<td style="text-align: center;">−38.379</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">≥5 conditions</td>
<td style="text-align: center;">−25.573</td>
<td></td>
<td style="text-align: center;">−34.885</td>
<td></td>
<td style="text-align: center;">−50.660</td>
<td></td>
<td style="text-align: center;">−25.461</td>
<td></td>
<td style="text-align: center;">−32.805</td>
<td></td>
<td style="text-align: center;">−41.759</td>
<td></td>
</tr>
</tbody>
</table>

*Transformed EQ-5D-5L level sum score*.

</div>

Results of the multivariable analyses are presented in <a href="#T6" data-ref-type="table">Table 5</a>. Sex and age were used in the first step and were significantly associated with the outcomes studied, with exceptions being age in the Dutch sample for the tLSS and sex in the UK sample for the EQ VAS. However, the effect of sex disappeared in all the samples, except for the Italian sample for the tLSS, when the level of education, work status, household income, and a number of chronic health conditions were included in the second step. The effect of age disappeared in the Italian sample for both outcomes studied.

<div id="T6" class="table-wrap">

<div class="caption">

Multivariable analyses of participant characteristics and the EQ-5D-5L transformed level sum score and EQ VAS in the three countries.

</div>

<table>
<thead>
<tr>
<th></th>
<th colspan="6" style="text-align: center;"><strong>EQ-5D-5L level sum score<a href="#TN8" data-ref-type="table-fn"><sup>*</sup></a></strong></th>
<th colspan="6" style="text-align: center;"><strong>EQ VAS</strong></th>
</tr>
<tr>
<th style="text-align: left;"><strong>Characteristic</strong></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
<th colspan="2" style="text-align: center;"><strong>Italy</strong></th>
<th colspan="2" style="text-align: center;"><strong>Netherlands</strong></th>
<th colspan="2" style="text-align: center;"><strong>UK</strong></th>
</tr>
<tr>
<th></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
<th style="text-align: center;"><strong>Coef.</strong></th>
<th style="text-align: center;"><em> <strong>P</strong> </em> <strong>-value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: center;">93.390</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">96.488</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">96.984</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">81.741</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">83.561</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">81.988</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sex</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.002</strong></td>
<td></td>
<td style="text-align: center;">0.907</td>
<td></td>
<td style="text-align: center;">0.098</td>
<td></td>
<td style="text-align: center;">0.073</td>
<td></td>
<td style="text-align: center;">0.218</td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">1.142</td>
<td></td>
<td style="text-align: center;">−0.050</td>
<td></td>
<td style="text-align: center;">−0.680</td>
<td></td>
<td style="text-align: center;">1.078</td>
<td></td>
<td style="text-align: center;">0.723</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>Female (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Age category</strong></td>
<td></td>
<td style="text-align: center;">0.316</td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;"><strong>0.007</strong></td>
<td></td>
<td style="text-align: center;">0.132</td>
<td></td>
<td style="text-align: center;"><strong>0.004</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.011</strong></td>
</tr>
<tr>
<td style="text-align: left;">18– &lt;25 year</td>
<td style="text-align: center;">0.990</td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">0.512</td>
<td></td>
<td style="text-align: center;">2.157</td>
<td></td>
<td style="text-align: center;">1.168</td>
<td></td>
<td style="text-align: center;">0.190</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">25– &lt;40 year</td>
<td style="text-align: center;">−0.251</td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">0.218</td>
<td></td>
<td style="text-align: center;">0.728</td>
<td></td>
<td style="text-align: center;">−1.410</td>
<td></td>
<td style="text-align: center;">0.724</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">40– &lt;60 year (ref)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">60–75 year</td>
<td style="text-align: center;">0.683</td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">2.753</td>
<td></td>
<td style="text-align: center;">−1.396</td>
<td></td>
<td style="text-align: center;">2.334</td>
<td></td>
<td style="text-align: center;">3.697</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Highest level of education</strong></td>
<td></td>
<td style="text-align: center;">0.679</td>
<td></td>
<td style="text-align: center;">0.180</td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">0.072</td>
<td></td>
<td style="text-align: center;"><strong>0.017</strong></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">0.515</td>
<td></td>
<td style="text-align: center;">−0.916</td>
<td></td>
<td style="text-align: center;">−0.261</td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">1.197</td>
<td></td>
<td style="text-align: center;">−2.015</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">0.497</td>
<td></td>
<td style="text-align: center;">0.024</td>
<td></td>
<td style="text-align: center;">0.088</td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">1.638</td>
<td></td>
<td style="text-align: center;">−0.061</td>
<td></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>High (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Work status</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>Employed (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: center;">−0.459</td>
<td></td>
<td style="text-align: center;">−3.853</td>
<td></td>
<td style="text-align: center;">−5.051</td>
<td></td>
<td style="text-align: center;">−0.835</td>
<td></td>
<td style="text-align: center;">−2.170</td>
<td></td>
<td style="text-align: center;">−4.305</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Looking after others</td>
<td style="text-align: center;">−0.407</td>
<td></td>
<td style="text-align: center;">−2.512</td>
<td></td>
<td style="text-align: center;">−0.954</td>
<td></td>
<td style="text-align: center;">−1.378</td>
<td></td>
<td style="text-align: center;">−1.289</td>
<td></td>
<td style="text-align: center;">−0.203</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Student</td>
<td style="text-align: center;">0.409</td>
<td></td>
<td style="text-align: center;">−1.861</td>
<td></td>
<td style="text-align: center;">−1.366</td>
<td></td>
<td style="text-align: center;">−0.124</td>
<td></td>
<td style="text-align: center;">−1.765</td>
<td></td>
<td style="text-align: center;">−2.327</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: center;">−0.415</td>
<td></td>
<td style="text-align: center;">0.360</td>
<td></td>
<td style="text-align: center;">−4.258</td>
<td></td>
<td style="text-align: center;">0.621</td>
<td></td>
<td style="text-align: center;">−0.843</td>
<td></td>
<td style="text-align: center;">−2.271</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Unable to work</td>
<td style="text-align: center;">−17.344</td>
<td></td>
<td style="text-align: center;">−10.234</td>
<td></td>
<td style="text-align: center;">−22.548</td>
<td></td>
<td style="text-align: center;">−23.249</td>
<td></td>
<td style="text-align: center;">−10.856</td>
<td></td>
<td style="text-align: center;">−16.990</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Household income</strong></td>
<td></td>
<td style="text-align: center;"><strong>0.003</strong></td>
<td></td>
<td style="text-align: center;">0.402</td>
<td></td>
<td style="text-align: center;">0.263</td>
<td></td>
<td style="text-align: center;">0.159</td>
<td></td>
<td style="text-align: center;"><strong>0.005</strong></td>
<td></td>
<td style="text-align: center;">0.069</td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">0.786</td>
<td></td>
<td style="text-align: center;">−0.059</td>
<td></td>
<td style="text-align: center;">−0.772</td>
<td></td>
<td style="text-align: center;">0.364</td>
<td></td>
<td style="text-align: center;">−3.042</td>
<td></td>
<td style="text-align: center;">−1.084</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1.518</td>
<td></td>
<td style="text-align: center;">0.412</td>
<td></td>
<td style="text-align: center;">−0.995</td>
<td></td>
<td style="text-align: center;">1.005</td>
<td></td>
<td style="text-align: center;">−0.148</td>
<td></td>
<td style="text-align: center;">−1.637</td>
<td></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>High (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;">Do not know/do not want to tell</td>
<td style="text-align: center;">2.131</td>
<td></td>
<td style="text-align: center;">0.947</td>
<td></td>
<td style="text-align: center;">−0.381</td>
<td></td>
<td style="text-align: center;">2.062</td>
<td></td>
<td style="text-align: center;">−0.761</td>
<td></td>
<td style="text-align: center;">0.229</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Number of chronic health conditions</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td></td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td colspan="13" style="text-align: left;"><strong>No disease (ref)</strong></td>
</tr>
<tr>
<td style="text-align: left;">1 disease</td>
<td style="text-align: center;">−7.670</td>
<td></td>
<td style="text-align: center;">−9.053</td>
<td></td>
<td style="text-align: center;">−9.851</td>
<td></td>
<td style="text-align: center;">−9.157</td>
<td></td>
<td style="text-align: center;">−8.763</td>
<td></td>
<td style="text-align: center;">−10.006</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">2 diseases</td>
<td style="text-align: center;">−13.337</td>
<td></td>
<td style="text-align: center;">−14.554</td>
<td></td>
<td style="text-align: center;">−18.762</td>
<td></td>
<td style="text-align: center;">−13.889</td>
<td></td>
<td style="text-align: center;">−15.210</td>
<td></td>
<td style="text-align: center;">−18.555</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">3 diseases</td>
<td style="text-align: center;">−15.300</td>
<td></td>
<td style="text-align: center;">−20.144</td>
<td></td>
<td style="text-align: center;">−26.676</td>
<td></td>
<td style="text-align: center;">−16.524</td>
<td></td>
<td style="text-align: center;">−18.561</td>
<td></td>
<td style="text-align: center;">−21.590</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">4 diseases</td>
<td style="text-align: center;">−25.079</td>
<td></td>
<td style="text-align: center;">−24.514</td>
<td></td>
<td style="text-align: center;">−35.618</td>
<td></td>
<td style="text-align: center;">−23.563</td>
<td></td>
<td style="text-align: center;">−23.255</td>
<td></td>
<td style="text-align: center;">−31.936</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">≥5 diseases</td>
<td style="text-align: center;">−23.031</td>
<td></td>
<td style="text-align: center;">−29.564</td>
<td></td>
<td style="text-align: center;">−40.170</td>
<td></td>
<td style="text-align: center;">−22.084</td>
<td></td>
<td style="text-align: center;">−27.558</td>
<td></td>
<td style="text-align: center;">−33.595</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><em>F</em>-value</td>
<td style="text-align: center;">73.18</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">122.34</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">256.00</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">38.53</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">55.78</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
<td style="text-align: center;">100.24</td>
<td style="text-align: center;"><strong>&lt;0.001</strong></td>
</tr>
<tr>
<td style="text-align: left;"><em>R</em>-squared</td>
<td style="text-align: center;">0.316</td>
<td></td>
<td style="text-align: center;">0.394</td>
<td></td>
<td style="text-align: center;">0.543</td>
<td></td>
<td style="text-align: center;">0.179</td>
<td></td>
<td style="text-align: center;">0.261</td>
<td></td>
<td style="text-align: center;">0.306</td>
<td></td>
</tr>
</tbody>
</table>

*Bold values are statistically significant values*.

*Transformed EQ-5D-5L level sum score*.

</div>

After controlling for other factors, a low level of education was associated with a worse tLSS and worse EQ VAS in the UK sample compared to the respondents with a high level of education. In the different country samples, having an increased number of chronic health conditions was consistently associated with a lower health outcome. Inability to work proved to be another factor that had a high impact in all the samples and on both the outcomes. The explained variability (*R*<sup>2</sup>) of the models was higher for the models based on the tLSS (31.6–54.3%) compared to the EQ VAS (17.9–30.6%), and highest for the UK and lowest for Italy.

Multivariable analyses were also conducted in the subgroups of participants with and without chronic health complaints, separately for each country (<a href="#SM2" data-ref-type="supplementary-material">Appendices 2A</a>,<a href="#SM2" data-ref-type="supplementary-material">B</a>). Inability to work and an increased number of chronic conditions were especially associated with a worse tLSS and worse EQ VAS in the samples from all the countries. The explained variability of the models varied largely from 9.1% for the EQ VAS in the Italian sample to 44.6% for the tLSS in the UK sample. Work status and, to a lower extent, household income were associated with the outcomes in the subgroup without any chronic health complaint. The explained variability of the models was very low (1.2–4.2%).

## Discussion

This study explored the potential of the EQ-5D-5L LSS as an outcome measure in the health inequality analyses relative to the EQ VAS. As hypothesized, our study showed that the EQ-5D-5L LSS tended to better discriminate between participants with a different level of education compared to the EQ VAS, both in the general sample as well as in subgroups of participants with a specific chronic health condition. Furthermore, the present study showed that the health outcomes differed among the three countries studied, with the worst outcomes for participants from the UK and best outcomes for participants from Italy. Participants with a low level of education had worst outcomes and those with a high level of education had the best outcomes in both the UK and the Netherlands, with larger differences among subgroups in the UK. Health inequalities were thus found to be highest in the UK and smallest in Italy, confirming our hypothesis. Multivariable analyses showed generally stronger predictive relations in the UK and with the EQ-5D-5L LSS. The presence of chronic health conditions and being unable to work were strong independent predictors, canceling out the educational effects (apart from a small effect in the UK).

Results from our study are in line with earlier studies that showed that the EQ-5D reflects health inequalities: low SES (defined as low educational level/low status/unskilled manual group/low income/low social class) is associated with a lower EQ outcome (25, 34–40). Some studies used the EQ VAS as an outcome (25, 37, 38), while some used the separate EQ-5D domains as an outcome (25, 34, 37–39), and some others used the EQ utility score as an outcome (35, 36, 39, 40). Use of the separate domains might not be very useful as to disperse populations by the level of inequality, health differences are often summarized into one single value (2, 7, 10, 16). An earlier study used both the EQ-5D utility score and EQ VAS as outcomes and showed that the EQ-5D utility score better discriminated between ethnicity groups than the EQ VAS (41), which is in line with our results. However, in our study, in the UK participants with memory problems and in the subgroups of participants without a chronic health condition, the EQ VAS was discriminative between participants with a different level of education whereas the EQ-5D was not. Potential causes could be the mediation effect of the inability to work and the presence of chronic health conditions, and/or the fact that EQ VAS and EQ-5D scores could assess slightly different outcomes, which was also shown in previous work (42). It was reported that EQ VAS scores could be predicted from EQ-5D scores, but there was the contribution from other factors also, including psychological status, age, education, and distress (42). The EQ-5D-5L LSS thus seems to better discriminate between subgroups, which is valuable in health inequality analysis. However, the use of an instrument that includes more than one question also includes some disadvantages, namely the extra time needed to complete the instrument and the corresponding higher burden for those completing it, which might result in a potentially lower response rate. It is important to consider whether the improved discriminative power outweighs these disadvantages.

Comparison of our findings on differences among countries are in line with the existing literature and confirm our hypothesis (37). A large European comparison study found that the relative index of inequality was the highest in the UK, lower in the Netherlands, and the lowest in Italy, when these three countries were compared (7). The same pattern was seen in a study on socioeconomic inequalities in self-assessed health in 17 European countries (43). Suggested potential factors that might contribute to these smaller health inequalities in Italy include the Mediterranean diet and the relatively low number of female smokers (44, 45). Within our Italian sample, it was surprising that differences in SES did not seem to exist. Previous studies reported the same patterns of worse health outcomes being associated with a low level of education and better health outcomes with a high level of education (7, 43).

Our results indicate that having a chronic health condition does not explain all the differences that arise from the level of education. This confirms earlier studies that showed that a low SES is associated with worse health outcomes, even after controlling for having chronic diseases (25, 41, 46, 47), although the inability to work (the companion variable explaining the education effect) was not always identically covered. Furthermore, within samples with a specific disease, studies also reported that a low level of education is associated with worse outcomes (40, 48–51). However, our results were inconsistent after controlling for relevant demographic factors. Apart from an association between low level of education and worse EQ-5D-5L LSS in the Dutch sample and low level of education and worse EQ VAS in the UK sample, no other association between educational level and outcomes was observed. Thus, other factors seemed to be stronger associated with a worse health outcome, with a consistently strong negative impact of having a chronic health condition. This association was shown to increase with an increase in the number of chronic health conditions. In the subgroup analysis, it is noteworthy that for the UK, low and middle income had a borderline significant negative impact on tLSS for the diseased subgroup, which may be indicative of more pronounced income inequality effects on health in the UK. The subgroup analysis also showed how unable to work had a much larger impact on tLSS in the diseased group when compared to the healthy subgroup for all countries, as expected.

The present study included some strengths and limitations. Strengths included the large sample size and the invitation of persons from three countries that were representative of their population with respect to age, sex, and educational level. Also, some limitations should be considered. By the use of a web-based survey, we only included participants who had access to a computer and internet and who were able to read and understand the survey, which may have led to participation bias as persons with low health literacy (often those with a low SES) may not have been included. We tried to mitigate this by selecting participants with certain characteristics (e.g., age, sex, and educational level) from the existing large panel in order to increase the representativeness of the study sample for the adult population in the selected countries. Also, a detailed analysis of non-responders was not possible due to the system of recruitment used.

Second, we used the educational level as a proxy for SES rather than an indicator that also incorporates income level or financial security. However, educational level is a common and widely used proxy for SES in the field of social epidemiology. It is a characteristic that has strong associations with a multitude of factors linked to health such as risky health behavior, limited access to financial and social resources, and type of work and residency (52–54).

Third, the outcome measure in our study was the LSS rather than the utility scores calculated with value sets of the three countries. Value sets for the EQ-5D reflect the preferences of the population of a country for the EQ-5D-5L health states, and the utility scores for the same health state calculated with different value sets vary substantially (55). Currently, there is no EQ-5D-5L value set available for Italy. Therefore, in order to use the EQ-5D-5L utility scores as an outcome measure, a proxy value set should be applied to assess the EQ-5D-5L utilities for the Italian study sample. In our study, the choice of the alternative value to assess utility scores for the Italian respondents, the Dutch or the UK value set, is arbitrary. The use of one of these value sets would therefore mean that differences in the utility scores between the Italian and UK or Dutch respondents reflect the differences in the EQ-5D-5L profile only and not the differences in the preferences for health states between these countries.

## Conclusion

The present study showed that in three different European countries, EQ-5D measures show the presence of education-dependent health inequalities, which are universally explained in regression analysis by, independently, the presence of chronic health conditions and the inability to work. In stratified analysis, the EQ-5D-5L LSS shows slightly better discrimination between participants with different levels of SES compared to the EQ VAS.

## Data Availability Statement

The data analyzed in this study is subject to the following licenses/restrictions: the datasets generated and/or analyzed during the current study are not publicly available due to privacy/ethical restrictions but are available from the corresponding author on reasonable request. Requests to access these datasets should be directed to Inge Spronk, <i.spronk@erasmusmc.nl>.

## Ethics Statement

The studies involving human participants were reviewed and approved by Leids Universitair Centrum—Commissie Medische Ethiek. The participants provided their written informed consent to participate in this study.

## Author Contributions

IS conceptualized and designed the study, analyzed and interpreted data, drafted the initial manuscript, and reviewed and revised the manuscript. SP, EL, and MJ conceptualized and designed the study, interpreted data, and reviewed and critically revised the manuscript. JH and GB conceptualized and designed the study, analyzed and interpreted data, and reviewed and critically revised the manuscript. All authors approved the final manuscript as submitted and agree to be accountable for all aspects of the work.

## Funding

This work was supported by the EuroQol Research Foundation (Grant No.: 20180630).

## Conflict of Interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's Note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

### Supplementary Material

The Supplementary Material for this article can be found online at: <https://www.frontiersin.org/articles/10.3389/fpubh.2021.744405/full#supplementary-material>

<div class="caption">

Click here for additional data file.

</div>

<div class="caption">

Click here for additional data file.

</div>

## References

1. MarmotM. Social determinants of health inequalities. Lancet. (2005) 365:1099–104. 10.1093/acprof:oso/9780198565895.001.000115781105

2. MackenbachJP. Health Inequalities: Europe in Profile. Rotterdam: COI for the Department of Health. (2006).

3. GrahamH. Understanding Health Inequalities. Berkshire: McGraw-Hill Education. (2009).

4. PhelanJCLinkBGTehranifarP. Social conditions as fundamental causes of health inequalities: theory, evidence, policy implications. J Health Soc Behav. (2010) 51:S28–40. 10.1177/002214651038349820943581

5. World Health O. Handbook on Health Inequality Monitoring: With a Special Focus on Low-and Middle-Income Countries. Geneva: World Health Organization. (2013).

6. WoodwardAKawachiI. Why reduce health inequalities? J Epidemiol Commun Health. (2000) 54:923–9. 10.1136/jech.54.12.92311076989PMC1731601

7. MackenbachJPStirbuIRoskamAJRSchaapMMMenvielleG. Socioeconomic inequalities in health in 22 European countries. N Engl J Med. (2008) 358:2468–81. 10.1056/NEJMsa070751918525043

8. OliverSKavanaghJCairdJLorencTOliverKHardenA. Health Promotion, Inequalities and Young People's Health: A Systematic Review of Research London. (2008).

9. ArcayaMCArcayaALSubramanianS. Inequalities in health: definitions, concepts, and theories. Glob Health Action. (2015) 8:27106. 10.3402/gha.v8.2710626112142PMC4481045

10. KjellssonGGerdthamUGPetrieD. Lies, damned lies, and health inequality measurements: understanding the value judgments. Epidemiology. (2015) 26:673. 10.1097/EDE.000000000000031926133019PMC4521896

11. MackenbachJP. The persistence of health inequalities in modern welfare states: the explanation of a paradox. Soc Sci Med. (2012) 75:761–9. 10.1016/j.socscimed.2012.02.03122475407

12. HatzenbuehlerMLPhelanJCLinkBG. Stigma as a fundamental cause of population health inequalities. Am J Public Health. (2013) 103:813–21. 10.2105/AJPH.2012.30106923488505PMC3682466

13. GarciaSFCellaDClauserSBFlynnKELadTLaiJS. Standardizing patient-reported outcomes assessment in cancer clinical trials: a patient-reported outcomes measurement information system initiative. J Clin Oncol. (2007) 25:5106–12. 10.1200/JCO.2007.12.234117991929

14. CellaDRileyWStoneARothrockNReeveBYountS. The Patient-Reported Outcomes Measurement Information System (PROMIS) developed and tested its first wave of adult self-reported health outcome item banks: 2005-2008. J Clin Epidemiol. (2010) 63:1179–94. 10.1016/j.jclinepi.2010.04.01120685078PMC2965562

15. DeshpandePRRajanSSudeepthiBLNazirCA. Patient-reported outcomes: a new era in clinical research. Perspect Clin Res. (2011) 2:137. 10.4103/2229-3485.8687922145124PMC3227331

16. Van DoorslaerEGerdthamUG. Does inequality in self-assessed health predict inequality in survival by income? Evidence from Swedish data. Soc Sci Med. (2003) 57:1621–9. 10.1016/S0277-9536(02)00559-212948571

17. GardnerDGCummingsLLDunhamRBPierceJL. Single-item versus multiple-item measurement scales: An empirical comparison. Educ Psychol Meas. (1998) 58:898–915. 10.1177/0013164498058006003

18. GogolKBrunnerMGoetzTMartinRUgenSKellerU. “My questionnaire is too long!” The assessments of motivational-affective constructs with three-item and single-item measures. Contemp Educ Psychol. (2014) 39:188–205. 10.1016/j.cedpsych.2014.04.002

19. GolickiDNiewadaMKarlińskaABuczekJKobayashiAJanssenM. Comparing responsiveness of the EQ-5D-5L, EQ-5D-3L and EQ VAS in stroke patients. Qual Life Res. (2015) 24:1555–63. 10.1007/s11136-014-0873-725425288PMC4457098

20. RoelenCAHeymansMWTwiskJWLaaksonenMPallesenSMagerøyN. Health measures in prediction models for high sickness absence: single-item self-rated health versus multi-item SF-12. Eur J Public Health. (2015) 25:668–72. 10.1093/eurpub/cku19225465915

21. DiamantopoulosASarstedtMFuchsCWilczynskiPKaiserS. Guidelines for choosing between multi-item and single-item scales for construct measurement: a predictive validity perspective. J Acad Market Sci. (2012) 40:434–49. 10.1007/s11747-011-0300-3

22. BrooksR. EuroQol: the current state of play. Health Policy. (1996) 37:53–72. 10.1016/0168-8510(96)00822-610158943

23. GundgaardJLauridsenJ. A decomposition of income-related health inequality applied to EQ-5D. Eur J Health Econ. (2006) 7:231–7. 10.1007/s10198-006-0360-316763803

24. SwinburnPLloydABoyeKEdson-HerediaEBowmanLJanssenB. Development of a disease-specific version of the EQ-5D-5L for use in patients suffering from psoriasis: lessons learned from a feasibility study in the UK. Value Health. (2013) 16:1156–62. 10.1016/j.jval.2013.10.00324326169

25. MielckAVogelmannMLeidlR. Health-related quality of life and socioeconomic status: inequalities among adults with a chronic disease. Health Qual Life Outcomes. (2014) 12:1–10. 10.1186/1477-7525-12-5824761773PMC4011770

26. EuroQol Research Foundation. About the EQ-5D-3L. (2019). Available online at: https://euroqol.org/eq-5d-instruments/eq-5d-3l-about/ (accessed April 20, 2019).

27. HerdmanMGudexCLloydAJanssenMKindPParkinD. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. (2011) 20:1727–36. 10.1007/s11136-011-9903-x21479777PMC3220807

28. EichlerHGKongSXGerthWCMavrosPJönssonB. Use of cost-effectiveness analysis in health-care resource allocation decision-making: how are cost-effectiveness thresholds expected to emerge? Value Health. (2004) 7:518–28. 10.1111/j.1524-4733.2004.75003.x15367247

29. Rios-DiazAJLamJRamosMSMoscosoAVVaughnPZoggCK. Global patterns of QALY and DALY use in surgical cost-utility analyses: a systematic review. PLoS ONE. (2016) 11:e0148304. 10.1371/journal.pone.014830426862894PMC4749322

30. VoormolenDCCnossenMCPolinderSGravesteijnBYVon SteinbuechelNRealRGL. Prevalence of post-concussion-like symptoms in the general population in Italy, The Netherlands and the UK. Brain Injury. (2019) 201:1–9. 10.1080/02699052.2019.160755731032649

31. RabinRCharroFD. EQ-5D: a measure of health status from the EuroQol Group. Ann Med. (2001) 33:337–43. 10.3109/0785389010900208711491192

32. FylkesnesKJakobsenMDHenriksenNO. The value of general health perception in health equity research: A community-based cohort study of long-term mortality risk (Finnmark cohort study 1987-2017). SSM Popul Health. (2021) 15:100848. 10.1016/j.ssmph.2021.10084834195347PMC8237603

33. JanssenMFBonselGJLuoN. Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. (2018) 36:675–97. 10.1007/s40273-018-0623-829470821PMC5954015

34. KindPDolanPGudexCWilliamsA. Variations in population health status: results from a UK national questionnaire survey. BMJ. (1998) 316:736–41. 10.1136/bmj.316.7133.7369529408PMC28477

35. BurströmKJohannessonMDiderichsenF. Swedish population health-related quality of life results using the EQ-5D. Qual Life Res. (2001) 10:621–35. 10.1023/A:101317183120211822795

36. SullivanPWGhushchyanV. Preference-based EQ-5D index scores for chronic conditions in the United States. Med Decision Making. (2006) 26:410–20. 10.1177/0272989X0629049516855129PMC2634296

37. KönigHHHeiderDLehnertTRiedel-HellerSGAngermeyerMCMatschingerH. Health status of the advanced elderly in six European countries: results from a representative survey using EQ-5D and SF-12. Health Qual Life Outcomes. (2010) 8:143. 10.1186/1477-7525-8-14321114833PMC3009699

38. LiHWeiXMaAChungRY. Inequalities in health status among rural residents: EQ-5D findings from household survey China. Int J Equity Health. (2014) 13:41. 10.1186/1475-9276-13-4124885378PMC4030034

39. ZhouZFangYZhouZLiDWangDLiY. Assessing income-related health inequality and horizontal inequity in China. Soc Indic Res. (2017) 132:241–56. 10.1007/s11205-015-1221-1

40. ArrospideAMachónMRamos-GoñiJMIbarrondoOMarJ. Inequalities in health-related quality of life according to age, gender, educational level, social class, body mass index and chronic diseases using the Spanish value set for Euroquol 5D-5L questionnaire. Health Qual Life Outcomes. (2019) 17:69. 10.1186/s12955-019-1134-930999899PMC6472013

41. LubetkinEIJiaHFranksPGoldMR. Relationship among sociodemographic factors, clinical conditions, and health-related quality of life: examining the EQ-5D in the US general population. Qual Life Res. (2005) 14:2187–96. 10.1007/s11136-005-8028-516328899

42. WhynesDKHealthTGJ. Correspondence between EQ-5D health state classifications and EQ VAS scores. Health Qual Life Outcomes. (2008) 6:94. 10.1186/1477-7525-6-9418992139PMC2588564

43. HuYvan LentheFJBorsboomGJLoomanCWBoppMBurströmB. Trends in socioeconomic inequalities in self-assessed health in 17 European countries between 1990 and 2010. J Epidemiol Community Health. (2016) 70:644–52. 10.1136/jech-2015-20678026787202

44. MackenbachJPCavelaarsAKunstAEGroenhofF. Socioeconomic inequalities in cardiovascular disease mortality. An international study. Eur Heart J. (2000) 21:1141–51. 10.1053/euhj.1999.199010924297

45. KnoopsKTde GrootLCKromhoutDPerrinAEMoreiras-VarelaO. Mediterranean diet, lifestyle factors, and 10-year mortality in elderly European men and women: the HALE project. JAMA. (2004) 292:1433–9. 10.1001/jama.292.12.143315383513

46. KoYCoonsSJ. Self-reported chronic conditions and EQ-5D index scores in the US adult population. Curr Med Res Opin. (2006) 22:2065–71. 10.1185/030079906X13262217031907

47. MielckAReitmeirPVogelmannMLeidlR. Impact of educational level on health-related quality of life (HRQL): results from Germany based on the EuroQol 5D (EQ-5D). Eur J Public Health. (2013) 23:45–9. 10.1093/eurpub/ckr20622434205

48. WexlerDGrantRWittenbergEBoschJCaglieroEDelahantyL. Correlates of health-related quality of life in type 2 diabetes. Diabetologia. (2006) 49:1489–97. 10.1007/s00125-006-0249-916752167

49. SchweikertBHungerMMeisingerCKönigHHGappOHolleR. Quality of life several years after myocardial infarction: comparing the MONICA/KORA registry to the general population. Eur Heart J. (2009) 30:436–43. 10.1093/eurheartj/ehn50919019995

50. StaffordMSoljakMPledgeVMindellJ. Socio-economic differences in the health-related quality of life impact of cardiovascular conditions. Eur J Public Health. (2012) 22:301–5. 10.1093/eurpub/ckr00721398378PMC3358629

51. XuRHCheungAWLWongELY. Examining the health-related quality of life using EQ-5D-5L in patients with four kinds of chronic diseases from specialist outpatient clinics in Hong Kong SAR China. Patient Prefer Adherence. (2017) 11:1565. 10.2147/PPA.S14394428979104PMC5602472

52. RossCEWuCL. The links between education and health. Am Sociol Rev. (1995) 60:719–45. 10.2307/2096319

53. DalyMCDuncanGJMcDonoughPWilliamsDR. Optimal indicators of socioeconomic status for health research. Am J Public Health. (2002) 92:1151–7. 10.2105/AJPH.92.7.115112084700PMC1447206

54. LahelmaEMartikainenPLaaksonenMAittomakiA. Pathways between socioeconomic determinants of health. J Epidemiol Community Health. (2004) 58:327–32. 10.1136/jech.2003.01114815026449PMC1732713

55. GerlingerCBamberLLeverkusFSchwenkeCHaberlandCSchmidtG. Comparing the EQ-5D-5L utility index based on value sets of different countries: impact on the interpretation of clinical study results. BMC Res Notes. (2019) 12:18. 10.1186/s13104-019-4067-930642397PMC6332559

[^1]: Edited by: Mihajlo Jakovljevic, Hosei University, Japan

[^2]: Reviewed by: Simon Grima, University of Malta, Malta; Thomas Poder, Université de Montréal, Canada

[^3]: This article was submitted to Health Economics, a section of the journal Frontiers in Public Health

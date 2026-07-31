---
project_id: "20180330"
work_id: "doi:10.1186/s12955-021-01771-3"
doi: "10.1186/s12955-021-01771-3"
pmid: "33926461"
pmcid: "PMC8082864"
title: "The relation between EQ-5D and fatigue in a Dutch general population sample: an explorative study"
journal: "Health and Quality of Life Outcomes"
publication_date: "2021-04-29"
volume: "19"
authors:
  - name: "I. Spronk"
    orcid: "https://orcid.org/0000-0001-9571-576X"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "S. Polinder"
    orcid: "https://orcid.org/0000-0002-4331-3141"
    affiliation_ids:
      - "Aff1"
  - name: "G. J. Bonsel"
    orcid: "https://orcid.org/0000-0002-8364-1086"
    affiliation_ids:
      - "Aff1"
      - "Aff3"
  - name: "M. F. Janssen"
    affiliation_ids:
      - "Aff4"
  - name: "J. A. Haagsma"
    orcid: "https://orcid.org/0000-0002-2055-548X"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.5645.2000000040459992XDepartment of Public Health, Erasmus MC, University Medical Center Rotterdam, P.O. Box 2040, 3000 CA Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "grid.416213.30000 0004 0460 0556Association of Dutch Burn Centres, Maasstad Hospital, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "EuroQol Group Executive Office, Rotterdam, The Netherlands"
  - id: "Aff4"
    name: "grid.5645.2000000040459992XSection Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Rotterdam, The Netherlands"
licence: "cc-by"
source_file: "input/projects/20180330/papers/doi_10.1186_s12955-021-01771-3.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8082864/fullTextXML"
source_method: "epmc_xml"
source_sha256: "a337a2cdd2075051fad56f7cef096df1b4ef8416e666216ba92e53a6ef7adafb"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The relation between EQ-5D and fatigue in a Dutch general population sample: an explorative study

## Abstract

### Background

Fatigue negatively influences health-related quality of life. It is questionable whether fatigue is sufficiently covered by the EQ-5D. This study investigated whether fatigue is covered by the existing domains of the EQ-5D.

### Methods

A Dutch general population sample completed the EQ-5D (3L and 5L version) and the Rivermead Post-Concussion Symptoms Questionnaire (RPQ), of which the fatigue item was used. Outcomes were compared between participants with and without a chronic health condition. Convergent validity was assessed, and multivariate regression analyses was used to predict the RPQ fatigue item from the EQ-5D-3L and EQ-5D-5L domains separately.

### Results

3027 people completed the survey, of whom 52% had ≥ 1 chronic health condition. Fatigue was reported by 48% of the participants. Fatigue was moderately correlated to the EQ-5D domains ‘pain/discomfort’, ‘usual activities’, and ‘anxiety/depression’ for the 3L (r = 0.379–0.426) and 5L version (r = 0.411–0.469). For the 5L, also a moderate correlation with ‘mobility’ (r = 0.335) was observed. The remaining correlations were weak. All EQ-5D-3L and 5L domains except for ‘mobility’ were significantly associated with the RPQ fatigue item (unstandardized Beta = − 0.20–0.67; *p* \< 0.01 to *p* = 0.04). Comparable outcomes were found for participants with and without ≥ 1 chronic health condition.

### Conclusions

The extent to which fatigue is covered by the EQ-5D domains is small to moderate, with the EQ-5D-5L being slightly more sensitive to capture fatigue compared to the EQ-5D-3L. An extra fatigue item for the EQ-5D may add value, as fatigue is not fully captured by the existing domains, both in people with and without a chronic health condition.

## Introduction

The impact of a health condition, the effectiveness of treatments and interventions, and the level of quality of care are increasingly evaluated by assessment of health-related quality of life (HRQL) of patients \[1–3\]. HRQL reflects patients’ perceptions of their condition on physical, psychological and social wellbeing \[4\]. HRQL instruments are developed as generic (i.e. applicable to any health condition) or disease-specific measures. Generic instruments facilitate comparison between different health conditions, whereas disease-specific instruments take the effects of a specific health condition into account in more detail \[5\].

A widely used generic HRQL instrument is the EQ-5D \[6\]. Its descriptive system consists of five domains: mobility, self-care, usual activities, pain/discomfort and anxiety/depression, which can be scored on a three or a (more refined) five level ordinal scale (EQ-5D-3L or EQ-5D-5L) \[6, 7\]. The instrument is cognitively simple, has good feasibility and only takes a few minutes to fill out \[8\]. Due to its conciseness the instrument is not comprehensive in all condition areas or populations; it does not capture all (disease-specific) aspects of health \[9, 10\]. This may lead to a lack of content validity and scale sensitivity \[9, 11–13\].

It is questionable whether fatigue is sufficiently covered by the EQ-5D. Fatigue is a sequela of a lot of chronic health conditions and has a considerable impact on HRQL \[14–17\]. An energy/tiredness domain was considered during development of the EQ-5D, but not included in the final version of the instrument as it was concluded that it had no significant additional effect in small-sized analysis \[18–20\]. However, more recent studies suggest that adding a tiredness/fatigue domain to the EQ-5D is valuable \[21–25\]. For example, a study by Efthymiadou et al. among 767 patient representatives from 38 countries showed that 17 important aspects were not captured by the EQ-5D, with fatigue being the most mentioned aspect \[25\].

Before testing the addition of an extra fatigue domain, it should be studied whether, and if so, to what extent, fatigue is captured by the five existing EQ-5D domains. In order to do that, one or more populations in which fatigue is prevalent is needed. In the general population prevalence rates of fatigue up to 50% have been reported \[26–28\]. These relatively high fatigue rates show that the general population is a suitable sample to investigate whether fatigue is captured by the EQ-5D instrument or represents a distinct piece of health information. Studies on the measurement properties of the EQ-5D-3L and EQ-5D-5L have shown that the EQ-5D-5L has a higher sensitivity and precision in health state measurement compared to the EQ-5D-3L \[29, 30\], though the EQ-5D-3L version is still often used. Therefore, the primary aim of this study was to explore whether fatigue is covered by the existing domains of the EQ-5D. The EQ-5D-3L and the EQ-5D-5L are separately tested as sensitivity of the latter is higher. Because fatigue is often related with having a chronic health condition \[24–27\], the secondary aim was to study whether outcomes differ between subgroups of people with and without a chronic health condition.

## Methods

### Participants

During the period June 29th till July 31st 2017, Survey Sampling International recruited participants \[31\]. They distributed and launched a survey in an existing large Dutch internet panel. The selected sample was representative of the population aged 18–75 with respect to age, sex and educational level. Informed consent for this survey was obtained from all members that agreed to fill in the survey. This study was part of the Collaborative European NeuroTrauma Effectiveness Research (CENTER-TBI) study (EC Grant 602150), a European multicentre prospective cohort study on the impact of traumatic brain injury (TBI). The data of the general population sample (used in present study) were to be used as reference data for the assessment of post-injury impact. Ethical approval was obtained from the Leids Universitair Centrum—Commissie Medische Ethiek (approval P14.222/NV/nv). Only data from participants who completed the full survey were included in the analysis.

### Measures

The survey included questions on socio-demographic information. Participants provided information regarding their age, gender, area of residence, educational level, household income level. Level of education was measured as the highest level achieved and coded based on the International Standard Classification of Education (ISCED) into three groups: up to lower secondary education (‘low’), completed upper secondary education (‘middle') and tertiary education (‘high’) \[32\]. Medical information included the presence of self-reported chronic health condition(s), including: asthma, chronic bronchitis, severe heart disease, consequences of a stroke, diabetes, severe back complaints, arthrosis, rheumatism, cancer, memory problems due to a neurological disease/dementia, memory problems due to ageing, depression or anxiety disorder, and/or other chronic health conditions.

The survey also included both the EQ-5D-3L and the EQ-5D-5L for all respondents \[6, 7\]. It was randomly assigned which version was administered first. The EQ-5D asks about your health today; the domains included are: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. The EQ-5D-3L offers three response options (no problems, moderate problems, and extreme problems/unable to) \[6\]. The EQ-5D-5L offers five response options (no problems, slight problems, moderate problems, severe problems, and extreme problems/unable to) \[7\]. Based on the five domains, an EQ-5D value or utility score (through weighting) was calculated based on Dutch value sets, separately for the EQ-5D-3L and EQ-5D-5L \[33, 34\]. The utility score ranges between 0 (referring to a state as bad as being dead) and 1 (referring to full health), with negative values for health states considered worse than death \[8\].

The survey also included the Rivermead Post-Concussion Symptoms Questionnaire (RPQ) \[35\]. This questionnaire assesses sixteen different symptoms. One of these items is about fatigue: ‘Do you (i.e., over the last 24 h) suffer from fatigue?’. Answer options included 0 (not experienced at all), 1 (no more of a problem), 2 (a mild problem), 3 (a moderate problem) and 4 (a severe problem).

### Data analyses

We used IBM SPSS Statistics 25 for all analyses. Descriptive statistics were used to assess the participant characteristics and outcomes of the EQ-5D-3L domains, EQ-5D-5L domains, and the RPQ fatigue item. Data are shown for the overall sample, as well as for subgroups based on whether or not participants had a chronic health condition. EQ-5D and fatigue level scores were compared across groups with Mann Whitney U tests for ordinal variables and with chi-square tests for categorical variables.

We head-to-head compared the EQ-5D-3L and EQ-5D-5L domains with the RPQ fatigue item. The proportion of participants with corresponding answers was assessed and tested using a chi-squared test. Corresponding answers were defined as reporting problems on both the EQ-5D domains and the RPQ fatigue item, or reporting no problems on any instrument. For example, a person reported a corresponding answer for the domains EQ-5D mobility and RPQ fatigue item if he/she reported mobility and fatigue problems, i.e. an EQ-5D mobility score \> 1 and a RPQ fatigue item score \> 1.

The Spearman rank correlation coefficient was used to study rank order correlations between the EQ-5D domains and the RPQ fatigue item, both in the total sample, and in the subgroups of people with and without a chronic health condition \[36\]. Cohen’s criteria were applied to evaluate the strength of association: correlations were strong if r ≥ 0.50, moderate if r ≥ 0.30–0.49, and weak if r ≥ 0.10–0.29 \[37\]. Next, it was measured to what extent variability in fatigue was captured by the EQ-5D domains. We applied multivariate regression analyses to explore which EQ-5D-3L and EQ-5D-5L domains associated with the RPQ fatigue, with relevant participant characteristics added (sex, age, level of education, work status, income and the presence of a chronic health condition). The significance level for all explorative analyses was set at *p* \< 0.05.

## Results

### Participants

A total of 3564 persons returned the questionnaire, of whom 3027 (85%) fully completed it. Participants were on average 44.7 years old (SD 15.3) and 50% was male (Table <a href="#Tab1" data-ref-type="table">1</a>). About half of the participants had a middle level of education (47%), and was employed (54%). Half of the participants had one or more chronic health condition (52%).

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of study population

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristic</th>
<th style="text-align: left;">Total sample (n = 3027)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Sex: Male</td>
<td>1520 (50.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Age (M, SD)</td>
<td>44.7 (15.3)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Age categories</td>
</tr>
<tr>
<td style="text-align: left;"> 18 to &lt; 25 years</td>
<td>365 (12.1%)</td>
</tr>
<tr>
<td style="text-align: left;"> 25 to &lt; 40 years</td>
<td>814 (26.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> 40 to &lt; 60 years</td>
<td>1231 (40.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> 60–75 years</td>
<td>617 (20.4%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Level of education</td>
</tr>
<tr>
<td style="text-align: left;"> Low</td>
<td>811 (26.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> Middle</td>
<td>1420 (46.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> High</td>
<td>796 (26.3%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Work status<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Employed</td>
<td>1635 (54.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed</td>
<td>316 (10.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after others</td>
<td>125 (4.1%)</td>
</tr>
<tr>
<td style="text-align: left;"> Student</td>
<td>209 (6.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> Retired</td>
<td>386 (12.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> Unable to work</td>
<td>356 (11.8%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Household income<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Low</td>
<td>540 (17.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> Middle</td>
<td>1270 (42.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> High</td>
<td>555 (18.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> Do not know/do not want to tell</td>
<td>662 (21.9%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Number of chronic health conditions</td>
</tr>
<tr>
<td style="text-align: left;"> No disease</td>
<td>1453 (48.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> 1 disease</td>
<td>971 (32.1%)</td>
</tr>
<tr>
<td style="text-align: left;"> 2 diseases</td>
<td>368 (12.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> 3 diseases</td>
<td>149 (4.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 4 diseases</td>
<td>86 (2.8%)</td>
</tr>
</tbody>
</table>

<sup>a</sup>Work status was categorized as employed (employee and self-employed), unemployed (consisting out of work for more than and less than 1 year), looking after others (e.g. a carer or parent), a student, retired and unable to work

<sup>b</sup>Income was grouped as low (less than €20.000), middle (€20.000–€49.999) and high (more than €49.999)

</div>

### EQ-5D-3L, EQ-5D-5L, and fatigue outcomes

The mean EQ-5D utility score was 0.82 (SD 0.23) based on the EQ-5D-3L, and 0.83 (SD 0.21) based on the EQ-5D-5L (Table <a href="#Tab2" data-ref-type="table">2</a>). Most problems were reported on the pain/discomfort domain: respectively 46% and 51% of the participants reported problems on the domain based on the EQ-5D-3L and EQ-5D-5L. A total of 23% of the participants reported mild fatigue, 16% moderate fatigue, and 9% severe fatigue. Participants with ≥ 1 chronic health condition had significantly worse outcomes on all EQ-5D domains and the RPQ fatigue item (Table <a href="#Tab2" data-ref-type="table">2</a>). A total of 236 participants (15%) with ≥ 1 chronic health condition reported severe fatigue, whereas only 29 participants (2%) without a chronic health condition reported severe fatigue. Participants with rheumatism experienced fatigue most often (81%), followed by participants with depression or anxiety disorder (79%) (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). Moderate to severe fatigue (RPQ fatigue item ≥ 3) was most often reported by participants with depression or anxiety disorder (60%), followed by participants with rheumatism (53%), and participants with memory problems (50%). Mean EQ-5D-5L utility score ranged between 0.59 for participants with rheumatism to 0.93 for participants without any chronic health condition (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

EQ-5D-3L, EQ-5D-5L and RPQ fatigue outcomes for the total sample and separately for those with and without a chronic health condition

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Total sample<br />
(n = 3027)</th>
<th style="text-align: left;">Without a chronic health condition<br />
(n = 1453)</th>
<th style="text-align: left;">With ≥ 1 chronic health condition<br />
(n = 1574)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">EQ-5D-3L</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility (% with problems)</td>
<td style="text-align: left;">22.6%</td>
<td style="text-align: left;">6.3%*</td>
<td style="text-align: left;">37.5%*</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care (% with problems)</td>
<td style="text-align: left;">7.2%</td>
<td style="text-align: left;">1.7%*</td>
<td style="text-align: left;">12.3%*</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activities (% with problems)</td>
<td style="text-align: left;">25.3%</td>
<td style="text-align: left;">5.8%*</td>
<td style="text-align: left;">43.3%*</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort (% with problems)</td>
<td style="text-align: left;">46.0%</td>
<td style="text-align: left;">21.1%*</td>
<td style="text-align: left;">68.9%*</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression (% with problems)</td>
<td style="text-align: left;">27.2%</td>
<td style="text-align: left;">14.9%*</td>
<td style="text-align: left;">28.6%*</td>
</tr>
<tr>
<td style="text-align: left;"> Utility score (M, SD)</td>
<td style="text-align: left;">0.82 (0.23)</td>
<td style="text-align: left;">0.93* (0.13)</td>
<td style="text-align: left;">0.72* (0.25)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">EQ-5D-5L</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility (% with problems)</td>
<td style="text-align: left;">27.1%</td>
<td style="text-align: left;">8.5%*</td>
<td style="text-align: left;">44.2%*</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care (% with problems)</td>
<td style="text-align: left;">8.7%</td>
<td style="text-align: left;">1.9%*</td>
<td style="text-align: left;">15.0%*</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activities (% with problems)</td>
<td style="text-align: left;">30.3%</td>
<td style="text-align: left;">8.0%*</td>
<td style="text-align: left;">50.9%*</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort (% with problems)</td>
<td style="text-align: left;">51.4%</td>
<td style="text-align: left;">27.8%*</td>
<td style="text-align: left;">73.3%*</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression (% with problems)</td>
<td style="text-align: left;">33.0%</td>
<td style="text-align: left;">18.4%*</td>
<td style="text-align: left;">46.4%*</td>
</tr>
<tr>
<td style="text-align: left;"> Utility score (M, SD)</td>
<td style="text-align: left;">0.83 (0.21)</td>
<td style="text-align: left;">0.93* (0.11)</td>
<td style="text-align: left;">0.73* (0.23)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">RPQ fatigue</td>
</tr>
<tr>
<td style="text-align: left;"> Not experienced at all</td>
<td style="text-align: left;">39.5%</td>
<td style="text-align: left;">55.7%*</td>
<td style="text-align: left;">24.5%*</td>
</tr>
<tr>
<td style="text-align: left;"> No more of a problem</td>
<td style="text-align: left;">12.6</td>
<td style="text-align: left;">13.1%*</td>
<td style="text-align: left;">12.1%*</td>
</tr>
<tr>
<td style="text-align: left;"> Mild fatigue</td>
<td style="text-align: left;">23.4%</td>
<td style="text-align: left;">20.6%*</td>
<td style="text-align: left;">25.9%*</td>
</tr>
<tr>
<td style="text-align: left;"> Moderate fatigue</td>
<td style="text-align: left;">15.8%</td>
<td style="text-align: left;">8.5%*</td>
<td style="text-align: left;">22.6%*</td>
</tr>
<tr>
<td style="text-align: left;"> Severe fatigue</td>
<td style="text-align: left;">8.8%</td>
<td style="text-align: left;">2.0%*</td>
<td style="text-align: left;">15.0%*</td>
</tr>
</tbody>
</table>

\*Statistically significantly different between subgroups with and without a chronic health condition (*p* \< 0.001)

</div>

<figure id="Fig1">
<p><img src="12955_2021_1771_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Frequency of responses on the RPQ fatigue item, according to the presence of a specific chronic health condition, including mean EQ-5D-5L utility score outlined above the bars</figcaption>
</figure>

### Head-to-head comparison EQ-5D-3L, EQ-5D-5L, and RPQ

#### EQ-5D-3L domains and the RPQ fatigue item

For all domains, more than half of the participants (56–69%) reported corresponding answers (e.g. reporting problems on an EQ-5D domain and on the RPQ fatigue item) (Table <a href="#Tab3" data-ref-type="table">3</a>). Most corresponding answers were reported on the ‘pain/discomfort’ domain and the RPQ fatigue item (69%). In case of non-corresponding answers/responses, most participants reported fatigue problems and no problems on the EQ-5D-3L domains. Chi-square test showed that answers on all EQ-5D domains were related to the RPQ fatigue item (all *p* \< 0.001). The distribution of answer options of each EQ-5D domain for each level of fatigue is presented in Fig. <a href="#Fig2" data-ref-type="fig">2</a>. It graphically presents an increasing percentage of participants reporting problems on the EQ-5D domains with higher fatigue levels. This is especially seen for the ‘pain/discomfort’ domain, and the ‘usual activities’ domain. The figure also depicts the differences between the EQ-5D-3L and EQ-5D-5L, with a higher percentage of participants reporting problems on the EQ-5D-5L compared to the EQ-5D-3L for all levels of fatigue and on all domains of the EQ-5D.

<div id="Tab3" class="table-wrap">

<div class="caption">

Head-to-head comparison of outcomes of the EQ-5D-3L domains and the RPQ fatigue item, and EQ-5D-5L domains and the RPQ fatigue item

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Comparison with EQ-5D-3L</th>
<th colspan="2" style="text-align: left;">Comparison with EQ-5D-5L</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">RPQ fatigue item</th>
<th colspan="2" style="text-align: left;">RPQ fatigue item</th>
</tr>
<tr>
<th style="text-align: left;">Fatigue</th>
<th style="text-align: left;">No fatigue</th>
<th style="text-align: left;">Fatigue</th>
<th style="text-align: left;">No fatigue</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;">EQ-5D domains</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Mobility problems</td>
</tr>
<tr>
<td style="text-align: left;">  No (EQ-5D L1)</td>
<td>31.9%</td>
<td><strong>45.5%</strong></td>
<td>28.9%</td>
<td><strong>44.0%</strong></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td><strong>16.0%</strong></td>
<td>6.6%</td>
<td><strong>19.0%</strong></td>
<td>8.1%</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Self-care problems</td>
</tr>
<tr>
<td style="text-align: left;">  No (EQ-5D L1)</td>
<td>42.6%</td>
<td><strong>50.2%</strong></td>
<td>41.5%</td>
<td><strong>49.8%</strong></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td><strong>5.4%</strong></td>
<td>1.8%</td>
<td><strong>6.5%</strong></td>
<td>2.2%</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Usual activities problems</td>
</tr>
<tr>
<td style="text-align: left;">  No (EQ-5D L1)</td>
<td>28.4%</td>
<td><strong>46.3%</strong></td>
<td>24.5%</td>
<td><strong>45.2%</strong></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td><strong>19.5%</strong></td>
<td>5.8%</td>
<td><strong>23.4%</strong></td>
<td>6.9%</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Pain/discomfort problems</td>
</tr>
<tr>
<td style="text-align: left;">  No (EQ-5D L1)</td>
<td>16.7%</td>
<td><strong>37.3%</strong></td>
<td>14.3%</td>
<td><strong>34.3%</strong></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td><strong>31.2%</strong></td>
<td>14.8%</td>
<td><strong>33.6%</strong></td>
<td>17.8%</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Anxiety/depression problems</td>
</tr>
<tr>
<td style="text-align: left;">  No (EQ-5D L1)</td>
<td>27.8%</td>
<td><strong>44.9%</strong></td>
<td>24.1%</td>
<td><strong>43.0%</strong></td>
</tr>
<tr>
<td style="text-align: left;">  Yes</td>
<td><strong>20.1%</strong></td>
<td>7.1%</td>
<td><strong>23.9%</strong></td>
<td>9.1%</td>
</tr>
</tbody>
</table>

Values printed in bold are considered corresponding answers, whereas the values not printed in bold are considered non-corresponding answers

</div>

<figure id="Fig2">
<p><img src="12955_2021_1771_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption><strong>a</strong>–<strong>e</strong> Frequency of responses on the five EQ-5D-3L and the EQ-5D-5L domains, separately for all answer options of the RPQ item</figcaption>
</figure>

#### EQ-5D-5L domains and the RPQ fatigue item

Except for the ‘pain/discomfort’ domain, all domains had more corresponding answers based on the EQ-5D-5L than based on the EQ-5D-3L (Table <a href="#Tab3" data-ref-type="table">3</a>). Most corresponding answers were reported on the ‘usual activities’ domain and the RPQ fatigue item (69%). In case of non-corresponding answers, most participants reported fatigue problems and no problems on the EQ-5D-5L domains, though these percentages were all lower than based on the EQ-5D-3L, meaning that more problems were reported on the 5L version of the instrument. Responses on all EQ-5D-5L domains were significantly related to the RPQ fatigue item (all *p* \< 0.01). Figure <a href="#Fig2" data-ref-type="fig">2</a> graphically demonstrates that more problems on the EQ-5D-5L domains correspond with more fatigue, with most problems reported on the ‘pain/discomfort’ domain.

### Correlation between the EQ-5D domains and the RPQ fatigue item

#### EQ-5D-3L domains and the RPQ fatigue item

Spearman rank correlation coefficients of the EQ-5D-3L domains and the RPQ fatigue item are shown in Table <a href="#Tab4" data-ref-type="table">4</a>. Correlations were moderate between the RPQ item and the domains ‘pain/discomfort’ (r = 0.426), ‘usual activities’ (r = 0.412), and ‘anxiety/depression’ (r = 0.379), and weak between the RPQ item and the other domains. In the subgroup of participants with ≥ 1 chronic health condition, all correlations were substantially stronger compared to the subgroup without a chronic health condition.

<div id="Tab4" class="table-wrap">

<div class="caption">

Spearman’s rank correlation of the EQ-5D-3L domains with the RPQ fatigue item, and the EQ-5D-5L domains with and the RPQ fatigue item

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Mobility</th>
<th style="text-align: left;">Self-care</th>
<th style="text-align: left;">Usual activities</th>
<th style="text-align: left;">Pain/ discomfort</th>
<th style="text-align: left;">Anxiety/ depression</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">RPQ fatigue item</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"> EQ-5D-3L</td>
</tr>
<tr>
<td style="text-align: left;">  All participants</td>
<td>0.297*</td>
<td>0.184*</td>
<td>0.412*</td>
<td>0.426*</td>
<td>0.379*</td>
</tr>
<tr>
<td style="text-align: left;">  Subgroup without chronic health condition</td>
<td>0.086*</td>
<td>0.050</td>
<td>0.200*</td>
<td>0.266*</td>
<td>0.303*</td>
</tr>
<tr>
<td style="text-align: left;">  Subgroup with ≥ 1 chronic health condition</td>
<td>0.230*</td>
<td>0.155*</td>
<td>0.359*</td>
<td>0.332*</td>
<td>0.326*</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"> EQ-5D-5L</td>
</tr>
<tr>
<td style="text-align: left;">  All participants</td>
<td>0.335*</td>
<td>0.210*</td>
<td>0.469*</td>
<td>0.447*</td>
<td>0.411*</td>
</tr>
<tr>
<td style="text-align: left;">  Subgroup without chronic health condition</td>
<td>0.123*</td>
<td>0.073*</td>
<td>0.246*</td>
<td>0.277*</td>
<td>0.333*</td>
</tr>
<tr>
<td style="text-align: left;">  Subgroup with ≥ 1 chronic health condition</td>
<td>0.270*</td>
<td>0.171*</td>
<td>0.428*</td>
<td>0.360*</td>
<td>0.343*</td>
</tr>
</tbody>
</table>

\**p* \< 0.05 for the correlation, based on Spearman’s correlation coefficient

</div>

#### EQ-5D-5L domains and the RPQ fatigue item

Also, all domains of the EQ-5D-5L were correlated with the RPQ fatigue item, with the correlations being stronger compared to the EQ-5D-3L domains. All domains were moderately correlated to the RPQ fatigue item (r = 0.335 – r = 0.469), except for the ‘self-care’ domain, which was weakly correlated (Table <a href="#Tab4" data-ref-type="table">4</a>). And, as with the EQ-5D-3L, all correlations were weaker in the subgroup of participants without a chronic health condition compared to the subgroup of participants with a chronic health condition.

### Variability in fatigue and the EQ-5D-3L and EQ-5D-5L domains

#### EQ-5D-3L domains and the RPQ fatigue item

Multivariate regression analysis showed that the EQ-5D-3L domains ‘anxiety/depression’ (unstandardized Beta = 0.67; *p* \< 0.001), ‘pain/discomfort’ (unstandardized Beta = 0.59; *p* \< 0.001), ‘usual activities’ (unstandardized Beta = 0.56; *p* \< 0.001), and ‘self-care’ (unstandardized Beta = − 0.18; *p* = 0.021) were significantly associated with the RPQ fatigue item. These domains explained 29% of the variance of fatigue. Addition of participant characteristics explained another 5% (R<sup>2</sup> = 0.340) (“Appendix 1”). Females, older age, being unable to work, having a low or unknown income, and having ≥ 1 chronic health complaint were associated with increased fatigue, whereas being a student and being retired were associated with lower fatigue levels.

In respondents having ≥ 1 chronic health condition, the EQ-5D-3L domains ‘anxiety/depression’ (unstandardized Beta = 0.60), ‘usual activities’ (unstandardized Beta = 0.49), and ‘pain/discomfort’ (unstandardized Beta = 0.46) (all *p* \< 0.01), whereas in respondents without a chronic health condition all EQ-5D-3L domains were significantly associated domains (unstandardized Beta = − 0.55 to 0.75; *p* \< 0.01 to *p* = 0.04) with the RPQ fatigue item.

#### EQ-5D-5L domains and RPQ fatigue item

For the EQ-5D-5L, multivariate regression analysis showed that the domains, ‘usual activities’ (unstandardized Beta = 0.42), ‘anxiety/depression’ (unstandardized Beta = 0.39), ‘pain/discomfort’ (unstandardized Beta = 0.34), and ‘self-care’ (unstandardized Beta = − 0.21) were significantly associated with the RPQ fatigue item (all *p* \< 0.01) and explained 31% of the variance of fatigue. With participants characteristics added in the model, 35% of the variance was explained (“Appendix 1”). Females, older age, being unable to work, having a low income, and having ≥ 1 chronic health complaint were associated with increased fatigue, whereas being a student and being retired were associated with less fatigue levels. In both the subgroup of participants with (unstandardized Beta = − 0.15 to 0.39) and without ≥ 1 chronic health condition (unstandardized Beta = − 0.36 to 0.51) the associations between the EQ-5D-5L domains and the RPQ fatigue item were comparable.

## Discussion

This study showed that a 5-level item on fatigue is only partially covered by the existing domains of the EQ-5D-3L and the EQ-5D-5L, most by the domains ‘pain/discomfort’ and ‘usual activities’ and least by the domain ‘self-care’. The EQ-5D domains and the fatigue item were moderately to weakly associated, with somewhat stronger associations when the EQ-5D-5L was used instead of the EQ-5D-3L. The associations between the EQ-5D domains and fatigue were higher in participants with ≥ 1 chronic health condition compared to participants without a chronic health condition.

The results from our study suggest that the extent to which fatigue is covered by the EQ-5D domains is small to moderate, indicating that adding an extra fatigue item to the EQ-5D might be considered. This is in line with earlier studies that suggested adding a fatigue (or related construct) item to the EQ-5D. Comparable constructs that were all related to being fatigued, but named differently were: energy/sleep \[38\], energy \[10\], fitness \[24\], fatigue \[25\], energy/fatigue \[39\], tiredness \[21, 23\]. These studies used different approaches to assess the potential need of a fatigue item for the EQ-5D, but all showed that adding a fatigue item has significant impact \[10, 21, 23–25, 38, 39\]. All these separate studies, including ours, provided indications on the potential value of adding a fatigue item to the EQ-5D, a so-called candidate bolt-on item. A ‘bolt-on’ is a specific domain that covers a specific health problem or dysfunction that has not sufficiently covered by the original instrument \[40\]. During the development of the EQ-5D, an energy/tiredness domain was considered, but eventually not included in the final version of the instrument as the added information—tested in small pilots, was small \[18–20\]. However, the time might be right to re-evaluate and further investigate this decision. As fatigue is an important sequela of many chronic conditions, studying the potential gain of adding a fatigue item to the EQ-5D is highly relevant. Additional analyses on the value of a fatigue bolt-on are valuable to conclude whether an extra domain captures additional information and improves the coverage of HRQL. We recommend that future studies investigate fatigue, with a suitable EQ-5D-5L response set, as a bolt-on item for the EQ-5D.

It is notable that our results showed that fatigue does not always result in problems on the existing domains of the EQ-5D, whereas problems on most EQ-5D domains did seem to result in fatigue. The other EQ-5D domains thus seem to be dominant over fatigue. Also, of note, is that a considerable part of the participants did report fatigue and no pain/discomfort problems, indicating that these participants did not consider fatigue as discomfort. Results of our study on the positive association between having a chronic health condition and experiencing fatigue are in line with earlier studies \[24–27\]. Study participants with one or more chronic health conditions reported significantly more frequently problems with fatigue. Fatigue is a sequel of many chronic health conditions, and is associated with lower HRQL \[24–27\]. Besides, our study showed that the EQ-5D-5L is somewhat more sensitive to capture fatigue compared to the EQ-5D-3L instrument, which is in congruence with current evidence. Earlier studies confirmed that the five level instrument is more sensitive to assess problem on the different domains and ceiling effects are substantially lower compared to the three level instrument \[29, 41\]. Despite the fact that the EQ-5D-5L instrument was somewhat more sensitive, results of all analyses were very consistent among the two versions of the instrument.The present study included some strengths and limitations. A strength included the large sample size that was representative of the Dutch population with respect to age, sex and educational level. Also, the prevalence of a chronic health condition was comparable to the Dutch population (52% vs. 58%) \[42\]. Other strengths include the ability to divide the sample in a group with and without a chronic health condition, and the high prevalence and wide range of fatigue scores which allowed us to study whether fatigue was captured by the EQ-5D instruments. By the inclusion of both the EQ-5D-3L and EQ-5D-5L instrument, we were able to compare outcomes between the EQ-5D-3L and EQ-5D-5L. However, this also could have been a limitation, as people became tired of completing comparable questions and just picked a box. We tried to avoid a systematic effect on the means by randomly assigning the EQ-5D-3L and EQ-5D-5L version first. Another limitation included the use of the RPQ fatigue item to assess fatigue. The RPQ instrument was originally developed for assessing post-concussion symptoms; it is not specifically developed to assess fatigue in the general population, though an earlier study showed its ability to assess fatigue in a general population \[31\]. Another apparent limitation was the difference in timeframe (your health today vs. fatigue in the past 24 h). Another limitation is the web-based administration of the survey without a predefined sampling frame. By this method, we were unaware of selective non-response and unable to study whether relations between 3L, 5L and fatigue were affected by particular respondents being overrepresented.

## Conclusion

This explorative study showed that the extent to which fatigue is captured by the EQ-5D domains is small to moderate in a sample of the general population, with the EQ-5D-5L being slightly to moderately more sensitive to capture fatigue compared to the EQ-5D-3L. An extra fatigue item for the EQ-5D may add value, potentially in the form of a ‘bolt-on’ item, as fatigue is not fully captured by the existing EQ-5D domains, both in people with and without a chronic health condition.

##### Appendix

See Table 

<div id="Tab5" class="table-wrap">

<div class="caption">

Multivariate model for the RPQ fatigue item, separately for the EQ-5D-3L and EQ-5D-5L

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">EQ-5D-3L</th>
<th colspan="2" style="text-align: left;">EQ-5D-5L</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Unstandardized B</th>
<th style="text-align: left;"><em>p</em> value</th>
<th style="text-align: left;">Unstandardized B</th>
<th style="text-align: left;"><em>p</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;">− 0.405</td>
<td>0.004</td>
<td>0.243</td>
<td>0.003</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">EQ-5D domains</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility</td>
<td style="text-align: left;">0.042</td>
<td>0.506</td>
<td>0.024</td>
<td>0.515</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care</td>
<td style="text-align: left;">− 0.098</td>
<td>0.210</td>
<td>− 0.149</td>
<td>0.002</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activities</td>
<td style="text-align: left;">0.430</td>
<td>&lt; 0.001</td>
<td>0.317</td>
<td>&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort</td>
<td style="text-align: left;">0.442</td>
<td>&lt; 0.001</td>
<td>0.259</td>
<td>&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression</td>
<td style="text-align: left;">0.558</td>
<td>&lt; 0.001</td>
<td>0.336</td>
<td>&lt; 0.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Characteristics</td>
</tr>
<tr>
<td style="text-align: left;"> Sex (male)</td>
<td style="text-align: left;">− 0.329</td>
<td>&lt; 0.001</td>
<td>− 0.346</td>
<td>&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;">− 0.005</td>
<td>0.005</td>
<td>− 0.006</td>
<td>0.002</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Level of education</td>
</tr>
<tr>
<td style="text-align: left;">  Low</td>
<td style="text-align: left;">0.089</td>
<td>0.142</td>
<td>0.080</td>
<td>0.181</td>
</tr>
<tr>
<td style="text-align: left;">  Middle</td>
<td style="text-align: left;">0.081</td>
<td>0.112</td>
<td>0.066</td>
<td>0.188</td>
</tr>
<tr>
<td style="text-align: left;">  High (ref)</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Work status</td>
</tr>
<tr>
<td style="text-align: left;">  Employed (ref)</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">  Unemployed</td>
<td style="text-align: left;">− 0.067</td>
<td>0.354</td>
<td>− 0.110</td>
<td>0.120</td>
</tr>
<tr>
<td style="text-align: left;">  Looking after others</td>
<td style="text-align: left;">− 0.106</td>
<td>0.317</td>
<td>− 0.057</td>
<td>0.586</td>
</tr>
<tr>
<td style="text-align: left;">  Student</td>
<td style="text-align: left;">− 0.202</td>
<td>0.027</td>
<td>− 0.268</td>
<td>0.003</td>
</tr>
<tr>
<td style="text-align: left;">  Retired</td>
<td style="text-align: left;">− 0.258</td>
<td>0.001</td>
<td>− 0.241</td>
<td>0.002</td>
</tr>
<tr>
<td style="text-align: left;">  Unable to work</td>
<td style="text-align: left;">0.234</td>
<td>0.002</td>
<td>0.152</td>
<td>0.048</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Household income</td>
</tr>
<tr>
<td style="text-align: left;">  Low</td>
<td style="text-align: left;">0.169</td>
<td>0.022</td>
<td>0.194</td>
<td>0.007</td>
</tr>
<tr>
<td style="text-align: left;">  Middle</td>
<td style="text-align: left;">0.099</td>
<td>0.096</td>
<td>0.088</td>
<td>0.128</td>
</tr>
<tr>
<td style="text-align: left;">  High (ref)</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">  Unknown</td>
<td style="text-align: left;">0.143</td>
<td>0.033</td>
<td>0.116</td>
<td>0.079</td>
</tr>
<tr>
<td style="text-align: left;"> Having ≥ 1 chronic health complaint</td>
<td style="text-align: left;">0.380</td>
<td>&lt; 0.001</td>
<td>0.277</td>
<td>&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><p> F value</p>
<p> R-square</p></td>
<td style="text-align: left;"><p>85.920</p>
<p>0.340</p></td>
<td>&lt; 0.001</td>
<td><p>91.060</p>
<p>0.353</p></td>
<td>&lt; 0.001</td>
</tr>
</tbody>
</table>

</div>

<a href="#Tab5" data-ref-type="table">5</a>.

### Acknowledgements

The views presented in this paper are the personal view of GJ Bonsel and MF Janssen, and do not reflect a view from the EuroQol Executive Office, or from the EuroQol Research Foundation.

### Authors' contributions

IS conceptualized and designed the study, analyzed and interpreted data, drafted the initial manuscript, and reviewed and revised the manuscript. GJB, SP, and MFJ conceptualized and designed the study, interpreted data, and reviewed and critically revised the manuscript. JAH conceptualized and designed the study, analyzed and interpreted data, and reviewed and critically revised the manuscript. All authors read and approved the final manuscript.

### Funding

This study was funded by EuroQol (Grant Number: 20180330).

### Availability of data and materials

Data available on request due to privacy/ethical restrictions.

### Declarations

#### Ethics approval and consent to participate

All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki declaration and its later amendments or comparable ethical standards.

#### Consent for publication

Informed consent was obtained from all individual participants included in the study.

#### Competing interest

The authors have no conflict of interest to declare that are relevant to the content of this article.

## References

1. Fiteni F, Le Ray I, Ousmen A, Isambert N, Anota A, Bonnetain F. Health-related quality of life as an endpoint in oncology phase I trials: a systematic review. BMC Cancer. 2019;19(1):361. doi:10.1186/s12885-019-5579-3

2. Dellenmark-Blom M, Sjöström S, Abrahamsson K, Holmdahl G. Health-related quality of life among children, adolescents, and adults with bladder exstrophy–epispadias complex: a systematic review of the literature and recommendations for future research. Qual Life Res. 2019;28:1–24. doi:10.1007/s11136-019-02119-7

3. Spronk I, Legemate C, Oen I, van Loey NE, Polinder S, van Baar ME. Health related quality of life in adults after burn injuries: a systematic review. PLoS ONE. 2018;13(5):e0197507. doi:10.1371/journal.pone.0197507

4. Guyatt GH, Jaeschke R, Feeny DH, Patrick DL. Measurements in clinical trials: choosing the right approach. In: Spilker B (ed) Quality of life and pharmacoeconomics in clinical trials, vol 2; 1996. p. 41–48.

5. Coons SJ, Rao S, Keininger DL, Hays RD. A comparative review of generic quality-of-life instruments. Pharmacoeconomics. 2000;17(1):13–35. doi:10.2165/00019053-200017010-00002

6. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

7. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

8. Rabin R, Charro FD. EQ-5D: a measure of health status from the EuroQol Group. Ann Med. 2001;33(5):337–343. doi:10.3109/07853890109002087

9. Brazier J, Connell J, Papaioannou D, Mukuria C, Mulhern B, Peasgood T. A systematic review, psychometric analysis and qualitative assessment of generic preference-based measures of health in mental health populations and the estimation of mapping functions from widely used specific measures. Health Technol Assess. 2014;18(34):vii. doi:10.3310/hta18340

10. Jelsma J, Maart S. Should additional domains be added to the EQ-5D health-related quality of life instrument for community-based studies? An analytical descriptive study. J Popul Health Metrics. 2015;13(1):13. doi:10.1186/s12963-015-0046-0

11. Kaarlola A, Pettilä V, Kekki P. Performance of two measures of general health-related quality of life, the EQ-5D and the RAND-36 among critically ill patients. Intensive Care Med. 2004;30(12):2245–2252. doi:10.1007/s00134-004-2471-6

12. Finch AP, Brazier JE, Mukuria C. What is the evidence for the performance of generic preference-based measures? A systematic overview of reviews. Eur J Health Econ. 2018;19(4):557–570. doi:10.1007/s10198-017-0902-x

13. Swinburn P, Lloyd A, Boye K, Edson-Heredia E, Bowman L, Janssen B. Development of a disease-specific version of the EQ-5D-5L for use in patients suffering from psoriasis: lessons learned from a feasibility study in the UK. Value Health. 2013;16(8):1156–1162. doi:10.1016/j.jval.2013.10.003

14. Fortier-Brochu É, Beaulieu-Bonneau S, Ivers H, Morin CM. Relations between sleep, fatigue, and health-related quality of life in individuals with insomnia. J Psychosom Res. 2010;69(5):475–483. doi:10.1016/j.jpsychores.2010.05.005

15. Rupp I, Boshuizen HC, Jacobi CE, Dinant HJ, van den Bos GA. Impact of fatigue on health-related quality of life in rheumatoid arthritis. Arthritis Rheum. 2004;51(4):578–585. doi:10.1002/art.20539

16. Kluthcovsky ACGC, Urbanetz AA, de Carvalho DS, Maluf EMCP, Sylvestre GCS, Hatschbach SBB. Fatigue after treatment in breast cancer survivors: prevalence, determinants and impact on health-related quality of life. Support Care Cancer. 2012;20(8):1901–1909. doi:10.1007/s00520-011-1293-7

17. Gold JI, Mahrer NE, Yee J, Palermo TM. Pain, fatigue and health-related quality of life in children and adolescents with chronic pain. Clin J Pain. 2009;25(5):407. doi:10.1097/AJP.0b013e318192bfb1

18. The EuroQol Group. EuroQol-a new facility for the measurement of health-related quality of life. Health Policy. 1990;16(3):199–208. doi:10.1016/0168-8510(90)90421-9

19. Brooks RG. 28 years of the EuroQol Group: an overview. EuroQol Working Paper Series; 2015.

20. Gudex C. The descriptive system of the EuroQOL instrument. In EQ-5D concepts and methods: a developmental history. Springer; 2005. p. 19–27.

21. Yang Y, Rowen D, Brazier J, Tsuchiya A, Young T, Longworth L. An exploratory study to test the impact on three “bolt-on” items to the EQ-5D. Value Health. 2015;18(1):52–60. doi:10.1016/j.jval.2014.09.004

22. Longworth L, Yang Y, Young T, Mulhern B, Hernandez Alava M, Mukuria C. Use of generic and condition-specific measures of health-related quality of life in NICE decision-making: a systematic review, statistical modelling and survey. Health Technol Assess. 2014;18(9):1–224. doi:10.3310/hta18090

23. Shah K, Mulhern B, Longworth L, Janssen B. Important aspects of health not captured by EQ-5D: Views of the UK general public. Office of Health Economics; 2016.10.1007/s40271-017-0240-128409481

24. Devlin NJ, Hansen P, Selai C. Understanding health state valuations: a qualitative analysis of respondents' comments. Qual Life Res. 2004;13(7):1265–1277. doi:10.1023/B:QURE.0000037495.00959.9b

25. Efthymiadou O, Mossman J, Kanavos P. Health related quality of life aspects not captured by EQ-5D-5L: results from an international survey of patients. Health Policy. 2019;123(2):159–165. doi:10.1016/j.healthpol.2018.12.003

26. van’t Leven M, Zielhuis GA, van der Meer JW, Verbeek AL, Bleijenberg G. Fatigue and chronic fatigue syndrome-like complaints in the general population. Eur J Public Health. 2010;20(3):251–257. doi:10.1093/eurpub/ckp113

27. Cullen W, Kearney Y, Bury G. Prevalence of fatigue in general practice. Ir J Med Sci. 2002;171(1):10. doi:10.1007/BF03168931

28. Basu N, Yang X, Luben RN, Whibley D, Macfarlane GJ, Wareham NJ. Fatigue is associated with excess mortality in the general population: results from the EPIC-Norfolk study. BMC Med. 2016;14(1):122. doi:10.1186/s12916-016-0662-y

29. Janssen M, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi:10.1007/s11136-012-0322-4

30. Janssen MF, Bonsel GJ, Luo N. Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. 2018;36(6):675–697. doi:10.1007/s40273-018-0623-8

31. Voormolen DC, Cnossen MC, Polinder S, Gravesteijn BY, Von Steinbuechel N, Real RGL. Prevalence of post-concussion-like symptoms in the general population in Italy, The Netherlands and the United Kingdom. Brain Inj. 2019;33:1–9. doi:10.1080/02699052.2019.1607557

32. UNESCO United Nations Educational S, Organization C. International standard classification of education, ISCED 1997. Advances in Cross-National Comparison: A European Working Book for Demographic and Socio-Economic Variables; 2003. p. 195–220.

33. Versteegh MM, Vermeulen KM, Evers SM, de Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi:10.1016/j.jval.2016.01.003

34. Lamers LM, McDonnell J, Stalmeier PF, Krabbe PF, Busschbach JJ. The Dutch tariff: results and arguments for an effective design for national EQ-5D valuation studies. Health Econ. 2006;15(10):1121–1132. doi:10.1002/hec.1124

35. King N, Crawford S, Wenden F, Moss N, Wade D. The rivermead post concussion symptoms questionnaire: a measure of symptoms commonly experienced after head injury and its reliability. J Neurol. 1995;242(9):587–592. doi:10.1007/BF00868811

36. De Smedt D, Clays E, Doyle F, Kotseva K, Prugger C, Pająk A. Validity and reliability of three commonly used quality of life measures in a large European population of coronary heart disease patients. Int J Cardiol. 2013;167(5):2294–2299. doi:10.1016/j.ijcard.2012.06.025

37. Cohen J. Statistical power analysis for the behavioral sciences. 2013. London, Routledge.

38. Finch AP, Brazier JE, Mukuria C. Selecting bolt-on dimensions for the EQ-5D: examining their contribution to health-related quality of life. Value Health. 2019;22(1):50–61. doi:10.1016/j.jval.2018.07.001

39. Perneger TV, Courvoisier DS. Exploration of health dimensions to be included in multi-attribute health-utility assessment. Int J Qual Health Care. 2011;23(1):52–59. doi:10.1093/intqhc/mzq068

40. Krabbe PF, Stouthard ME, Essink-Bot M-L, Bonsel GJ. The effect of adding a cognitive dimension to the EuroQol multiattribute health-status classification system. J Clin Epidemiol. 1999;52(4):293–301. doi:10.1016/S0895-4356(98)00163-2

41. Buchholz I, Janssen MF, Kohlmann T, Feng Y-S. A systematic review of studies comparing the measurement properties of the three-level and five-level versions of the EQ-5D. Pharmacoeconomics. 2018;36(6):645–661. doi:10.1007/s40273-018-0642-5

42. Volksgezondheidenzorg.info. Aantal mensen met chronische aandoening bekend bij de huisarts; 2020. https://www.volksgezondheidenzorg.info/onderwerp/chronische-ziekten-en-multimorbiditeit/cijfers-context/huidige-situatie#node-aantal-mensen-met-chronische-aandoening-bekend-bij-de-huisarts.

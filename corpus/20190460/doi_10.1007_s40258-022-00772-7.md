---
project_id: "20190460"
work_id: "doi:10.1007/s40258-022-00772-7"
doi: "10.1007/s40258-022-00772-7"
pmid: "36434410"
pmcid: "PMC9702834"
title: "EQ-5D-5L Population Norms for Italy"
journal: "Applied Health Economics and Health Policy"
publication_date: "2022-11-25"
volume: "21"
issue: "2"
authors:
  - name: "Michela Meregaglia"
    affiliation_ids:
      - "Aff1"
  - name: "Francesco Malandrini"
    affiliation_ids:
      - "Aff1"
  - name: "Aureliano Paolo Finch"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Oriana Ciani"
    affiliation_ids:
      - "Aff1"
  - name: "Claudio Jommi"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "CERGAS, SDA Bocconi School of Management, Milan, Italy"
  - id: "Aff2"
    name: "EuroQol Office, EuroQol Research Foundation, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "Health Values Research and Consultancy, Amsterdam, The Netherlands"
licence: "cc-by-nc"
source_file: "input/projects/20190460/papers/doi_10.1007_s40258-022-00772-7.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9702834/fullTextXML"
source_method: "epmc_xml"
source_sha256: "d842a3b656e5287b494ecdaf400b1907cb684fb8c2f1955672fb86169cf800ef"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# EQ-5D-5L Population Norms for Italy

## Abstract

### Objectives

This study aimed to provide normative data obtained in response to the EQ-5D-5L questionnaire in Italy and compare this with data from other countries.

### Methods

A sample of the Italian adult population (aged ≥ 18 years) was recruited and interviewed online using videoconferencing software (Zoom) between November 2020 and February 2021. The distribution of answers was estimated as per the descriptive system of the EQ-5D-5L, and descriptive statistics were calculated for the EQ VAS score and EQ-5D-5L index value in the whole sample and relevant subgroups. An ordinary least square (OLS) regression was performed to evaluate the impact of sociodemographic variables on EQ-5D-5L results. Lastly, a comparison was made with EQ-5D-5L population norms of other countries. Data analysis was performed using Microsoft Excel and Stata 13.

### Results

Overall, 1182 people representative of the Italian population (2020) in terms of sex and geographical area responded to the survey. Of the 3125 potential EQ-5D-5L health states, only 106 (3.4%) were selected, and the ‘11111’ and ‘11112’ states were chosen by half of the participants. In terms of EQ-5D-5L dimensions, the frequency of any problems (from slight to extreme) associated with anxiety and depression was high among the very young (18–24 years, 56.0%) and in women of all ages (49.7%). The mean index value (± standard deviation \[SD\]) was 0.93 (± 0.11) for the entire sample and gradually decreased with age, moving from 0.95 (± 0.06) in the youngest group (18–24 years) to 0.91 (± 0.13) in the oldest age group (≥ 75 years). Similarly, the mean EQ VAS score (± SD) was 81.8 (± 13.5), and decreased from 87.0 (± 8.9) in the 18–24 years age group to 75.1 (± 16.4) among participants \> 75 years of age. The existence of self-reported chronic conditions (e.g., cardiovascular disease), female sex, and social assistance recipiency were negatively associated with the EQ-5D index value, while the EQ VAS score was significantly lower in people with chronic conditions and aged \> 55 years. Conversely, higher income levels had a positive impact on both the EQ-5D index value and the EQ VAS score. Lastly, both the EQ-5D index value and EQ VAS score in Italy were, on average, higher than in most European countries.

### Conclusions

EQ-5D-5L population norms provide useful insights into the health status of the Italian population and can be used as a reference for other surveys using the same instrument.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40258-022-00772-7.

Accepted 2022 Oct 31; Issue date 2023.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| The overall health status of a sample of Italians captured using the EQ-5D-5L was good compared with the US and most European countries for which population norms are available. |
| The mean index value and EQ VAS scores were 0.93 (± 0.11) and 81.8 (± 13.5), respectively; more than one-third of participants selected the ‘full health’ status. |
| However, the frequency of any problems related to anxiety/depression was rather high (41%), especially among the young sample under 35 years of age. |

</div>

## Introduction

In recent years, there has been growing attention to health-related quality of life (HRQoL) in clinical research, population surveys, and health technology assessment (HTA) of new drugs and other types of health interventions. Two broad categories of measures exist to estimate HRQoL in patients and general populations. Disease-specific instruments are more sensitive in capturing specific health issues but do not allow for comparison with other conditions and interventions. Thus, generic instruments, especially if accompanied by preference-based algorithms for utility values generation, are often preferred in health economics research and HTA, to generate quality-adjusted life-years (QALYs) and allocate scarce resources across different technologies.

The EQ-5D is a widely used, standardised, preference-based generic measure of HRQoL developed by the EuroQol group in 1990. The EQ-5D has shown validity and responsiveness across different diseases and populations \[1\]. The EQ-5D is the most widely adopted instrument to measure HRQoL in cost-effectiveness analysis (<https://euroqol.org/eq-5d-instruments/>) and the most frequently cited in national pharmacoeconomic guidelines \[2\]. Several HTA agencies around the globe, such as the National Institute for Health and Care Excellence (NICE) in the UK, recommend the use of EQ-5D for measuring HRQoL and included it in drug reimbursement requests \[3\]. In 2020 national guidelines, the Italian Drug Agency (AIFA) established that cost-effectiveness analyses should be included in all price and reimbursement dossiers of new drugs or new indications, and conducted with utility values related to the Italian context. Moreover, the document explicitly includes EQ-5D among the recommended instruments to measure HRQoL \[4\].

In 2009, a five-level version of the EQ-5D (EQ-5D-5L) was developed, so as to improve the sensitivity and minimise the ceiling effect bias of the original, three-level version (EQ-5D-3L). The new version kept its original five dimensions (i.e., mobility, self-care, usual activities, pain/discomfort, anxiety/depression) but increased the number of severity levels from three to five (i.e., no problems, slight problems, moderate problems, severe problems, extreme problems/unable to). The 5L version showed better distributional properties and informativity compared with the 3L version \[5\].

Among the EQ-5D-5L applications, a set of utility index and EQ VAS score benchmark values for the general population, i.e., population reference data or population norms, are useful as normative reference values for comparing the health status of the populations across countries and subpopulations (e.g., patients and healthy people) \[6, 7\]. EQ-5D-5L population norms have been developed for numerous countries and regions in Europe and elsewhere \[8\] but were not yet available for Italy.

In 2021, an EQ-5D-5L value set for Italy was developed based on preferences collected from an adult sample of the Italian general population \[9\]. Besides the valuation task, the interviewees self-reported their health using the EQ-5D-5L descriptive system and EQ VAS. The present study aimed to provide normative data for the EQ-5D-5L questionnaire in Italy for age, sex and other subgroups, and compare the results with population norms from other countries.

## Methods

### Sample Recruitment

The Ethics Committee of Bocconi University approved this study on 6 October 2020 (approval number: 2020-SA000136.4). A market research company with experience in quantitative and qualitative healthcare research (Pepe Research) organised the recruitment and scheduled interviews. The target sample was 1000–1200 participants, which was representative of the Italian non-institutionalised adult population. The company identified potential participants using an online panel, a network of local recruiters and quota-based sampling criteria (i.e., age, sex, and geographical distribution by macro-area: north-east, north-west, centre, south and islands). Scheduling assistant software (TIMIFY) was utilised to facilitate interview scheduling and interaction between the company, the interviewers, and the interviewees, who also received a phone call the day before the scheduled interview.

### Data Collection

Due to the current coronavirus disease 2019 (COVID-19) pandemic, the survey was conducted entirely online using computer-assisted personal interviews (CAPIs) administered through a statistical survey online application (Lime Survey), according to the EuroQol valuation technology (EQ-VT) protocol, and videoconferencing software (Zoom). The survey's technical and logistic feasibility was tested through pilot interviews. Data collection was conducted between October 2020 and February 2021 by 11 trained interviewers recruited among researchers and MSc or PhD students at Bocconi University. During the interviews, besides performing the composite time trade-off (cTTO) and discrete choice experiment (DCE) valuation tasks \[9\], participants presented their self-reported health using EQ-5D-5L and EQ VAS and replied to questions about demographic, social, economic and health status. In particular, they self-reported diagnoses of their chronic conditions from a list created by referring to the International Classification of Diseases 11th revision \[10\] and previous studies \[1, 6\]. The quality of the interview was checked using the EQ-VT protocol Quality Control (QC) procedure after each round of data collection (i.e., 10 interviews per interviewer) \[11, 12\].

### EQ-5D-5L

The official Italian EQ-5D-5L questionnaire version was used in the survey. The EQ-5D-5L descriptive system includes five dimensions: mobility (MO), self-care (SC), usual activities (UA), pain/discomfort (PD), and anxiety/depression (AD). Each dimension is articulated into five severity levels: no problems, slight problems, moderate problems, severe problems, extreme problems (or unable to). Consequently, 3125 (5<sup>5</sup>) possible health states are determined by the combination of responses and were identified with a unique five-digit number ranging from the full health state (‘11111’) to the worst state (‘55555’). Each health state can be converted into a single index value using predefined preference weights collected at the population level. In this study, we applied the newly developed Italian value set with index values obtained from two elicitation methods (cTTO and DCE), and range from −0.571 for ‘55555’ and 1 for the healthiest state (‘11111’) \[9\]. The EQ-5D questionnaire also includes a visual analogue scale (EQ VAS) on which participants indicated their self-rated health at the time between 0 (worst imaginable health) and 100 (best imaginable health).

### Data Analysis

The demographic and socioeconomic characteristics of the sample were described. We identified the most selected EQ-5D-5L health states and reported their corresponding mean index value and EQ VAS scores. The distribution of the severity levels (1–5), and the frequencies of ‘no problems’ (level 1) and ‘any problems’ (levels 2–5) using a binary variable, were calculated for each dimension in the descriptive part of the EQ-5D-5L. The significant differences (*p* \< 0.05) across groups were detected using Chi-square tests. The EQ-5D-5L index value and EQ VAS score were analysed as continuous variables (mean, standard deviation; median, range). The *t*-test and one-way analysis of variance (ANOVA) were used to detect statistically significant differences between two groups (e.g., by sex) and across more than two (e.g., by income level), respectively. The sample was stratified by sex, predefined age classes according to the EuroQol standardised format (18–24, 25–34, 35–44, 45–54, 55–64, 65–74 and 75+ years), and other relevant subgroups. Ordinary least square (OLS) regression with robust standard errors was performed to investigate the impact of participant characteristics on the EQ-5D-5L index value and EQ VAS score using backward selection to remove any non-significant variables (*p* \> 0.05). Accordingly, regression coefficients with their corresponding 95% confidence interval and *p*-value were reported only for significant variables. Lastly, results were compared with existing population norms from other countries, as reported by the EuroQol website \[8\], in terms of the EQ-5D-5L index value and EQ VAS score. All statistical analyses were performed using Microsoft Excel (Microsoft Corporation, Armonk, NY, USA) and Stata 13 (StataCorp LLC, College Station, TX, USA).

## Results

### Sample Characteristics

A total of 1182 adults, of whom 606 were women (51.3%), aged between 18 and 84 years, completed the survey. A sample description is provided in Table <a href="#Tab1" data-ref-type="table">1</a> in comparison with national general population characteristics in 2020 (Italian National Institute of Statistics \[ISTAT\] data) \[13, 14\]. The sample was fully representative of the Italian population in terms of sex and geographical area but was, on average, 4 years younger. A subsample of 461 participants (39%) reported being affected by at least one chronic disease. As shown in electronic Supplementary Table S1, the most frequent self-reported chronic condition was cardiovascular disease (*n* = 180), followed by arthritis (*n* = 69), diabetes (*n* = 62) and asthma or chronic obstructive pulmonary disease (*n* = 58), in most cases with mild or moderate symptomatology.

<div id="Tab1" class="table-wrap">

<div class="caption">

Background characteristics of the sample and national adult population (2020)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Full sample<br />
[<em>n</em> = 1182]</th>
<th style="text-align: left;">General population (18+ years of age)<br />
[<em>n</em> = 50,208,329]</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Age, years [mean (SD)]</td>
<td style="text-align: left;">48.29 (16.06)</td>
<td style="text-align: left;">52.05</td>
</tr>
<tr>
<td style="text-align: left;">Age groups, years</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 18–24</td>
<td style="text-align: left;">109 (9.22)</td>
<td style="text-align: left;">4,121,339 (8.21)</td>
</tr>
<tr>
<td style="text-align: left;"> 25–34</td>
<td style="text-align: left;">166 (14.04)</td>
<td style="text-align: left;">6,410,935 (12.77)</td>
</tr>
<tr>
<td style="text-align: left;"> 35–44</td>
<td style="text-align: left;">200 (16.92)</td>
<td style="text-align: left;">7,759,655 (15.45)</td>
</tr>
<tr>
<td style="text-align: left;"> 45–54</td>
<td style="text-align: left;">251 (21.24)</td>
<td style="text-align: left;">9,626,469 (19.18)</td>
</tr>
<tr>
<td style="text-align: left;"> 55–64</td>
<td style="text-align: left;">211 (17.85)</td>
<td style="text-align: left;">8,430,841 (16.79)</td>
</tr>
<tr>
<td style="text-align: left;"> 65+</td>
<td style="text-align: left;">245 (20.72)</td>
<td style="text-align: left;">13,859,090 (27.60)</td>
</tr>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">575 (48.75)</td>
<td style="text-align: left;">24,195,125 (48.19)</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">606 (51.27)</td>
<td style="text-align: left;">26,013,204 (51.81)</td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td style="text-align: left;">1 (0.08)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;">Geographical distribution<sup>a</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> North-West</td>
<td style="text-align: left;">317 (27.16)</td>
<td style="text-align: left;">13,498,616 (26.88)</td>
</tr>
<tr>
<td style="text-align: left;"> North-East</td>
<td style="text-align: left;">225 (19.28)</td>
<td style="text-align: left;">9,790,372 (19.50)</td>
</tr>
<tr>
<td style="text-align: left;"> Centre</td>
<td style="text-align: left;">230 (19.71)</td>
<td style="text-align: left;">10,012,074 (19.95)</td>
</tr>
<tr>
<td style="text-align: left;">South and Islands</td>
<td style="text-align: left;">395 (33.85)</td>
<td style="text-align: left;">16,907,267 (33.67)</td>
</tr>
<tr>
<td style="text-align: left;"> Education<sup>b</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Elementary</td>
<td style="text-align: left;">1 (0.08)</td>
<td style="text-align: left;">8263 (15.90)</td>
</tr>
<tr>
<td style="text-align: left;"> Middle inferior</td>
<td style="text-align: left;">76 (6.43)</td>
<td style="text-align: left;">16,733 (32.19)</td>
</tr>
<tr>
<td style="text-align: left;"> High school</td>
<td style="text-align: left;">637 (53.89)</td>
<td style="text-align: left;">19,038 (36.63)</td>
</tr>
<tr>
<td style="text-align: left;"> Academic degree</td>
<td style="text-align: left;">468 (39.59)</td>
<td style="text-align: left;">7944 (15.28)</td>
</tr>
<tr>
<td style="text-align: left;">Employment status<sup>c</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Employed</td>
<td style="text-align: left;">487 (41.20)</td>
<td style="text-align: left;">18,183,000 (36.21)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-employed</td>
<td style="text-align: left;">150 (12.69)</td>
<td style="text-align: left;">5,302,000 (10.56)</td>
</tr>
<tr>
<td style="text-align: left;"> Student</td>
<td style="text-align: left;">112 (9.48)</td>
<td style="text-align: left;">2,202,487 (4.39)</td>
</tr>
<tr>
<td style="text-align: left;"> Pensioner</td>
<td style="text-align: left;">234 (19.8)</td>
<td style="text-align: left;">16,000,000 (31.87)</td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed</td>
<td style="text-align: left;">92 (7.78)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> Housewife</td>
<td style="text-align: left;">96 (8.12)</td>
<td style="text-align: left;">7,338,000 (14.61)</td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td style="text-align: left;">11 (0.93)</td>
<td style="text-align: left;">1,182,842 (2.36)</td>
</tr>
<tr>
<td style="text-align: left;">Annual household salary</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> &lt; €14,000</td>
<td style="text-align: left;">93 (7.87)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €14,000–€20,999</td>
<td style="text-align: left;">135 (11.42)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €21,000–€27,999</td>
<td style="text-align: left;">168 (14.21)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €28,000–€34,999</td>
<td style="text-align: left;">160 (13.54)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €35,000–€41,999</td>
<td style="text-align: left;">159 (13.45)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €42,000–€48,999</td>
<td style="text-align: left;">64 (5.41)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €49,000–€55,999</td>
<td style="text-align: left;">90 (7.61)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €56,000–€62,999</td>
<td style="text-align: left;">50 (4.23)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €63,000–€69,999</td>
<td style="text-align: left;">40 (3.38)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> €70,000–€90,999</td>
<td style="text-align: left;">43 (3.64)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> &gt; €91,000</td>
<td style="text-align: left;">13 (1.10)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to answer</td>
<td style="text-align: left;">167 (14.13)</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;">Marital status<sup>d</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Single</td>
<td style="text-align: left;">350 (29.61)</td>
<td style="text-align: left;">15,966,146 (31.80)</td>
</tr>
<tr>
<td style="text-align: left;"> Married or living with partner</td>
<td style="text-align: left;">727 (61.51)</td>
<td style="text-align: left;">28,012,121 (55.80)</td>
</tr>
<tr>
<td style="text-align: left;"> Separated or divorced</td>
<td style="text-align: left;">78 (6.60)</td>
<td style="text-align: left;">1,850,178 (3.68)</td>
</tr>
<tr>
<td style="text-align: left;"> Widower/Widow</td>
<td style="text-align: left;">27 (2.28)</td>
<td style="text-align: left;">4,379,884 (8.72)</td>
</tr>
<tr>
<td style="text-align: left;">Children<sup>e</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">691 (58.46)</td>
<td style="text-align: left;">8766 (62.13)</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">491 (41.54)</td>
<td style="text-align: left;">5343 (37.87)</td>
</tr>
<tr>
<td style="text-align: left;">Household size<sup>f</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> One</td>
<td style="text-align: left;">138 (11.67)</td>
<td style="text-align: left;">8410 (32.85)</td>
</tr>
<tr>
<td style="text-align: left;"> Two</td>
<td style="text-align: left;">369 (31.22)</td>
<td style="text-align: left;">7086 (27.69)</td>
</tr>
<tr>
<td style="text-align: left;"> Three</td>
<td style="text-align: left;">285 (24.11)</td>
<td style="text-align: left;">4860 (18.99)</td>
</tr>
<tr>
<td style="text-align: left;"> Four</td>
<td style="text-align: left;">275 (23.27)</td>
<td style="text-align: left;">3907 (15.27)</td>
</tr>
<tr>
<td style="text-align: left;"> Five or more</td>
<td style="text-align: left;">115 (9.73)</td>
<td style="text-align: left;">1330 (5.20)</td>
</tr>
<tr>
<td style="text-align: left;">Chronic conditions<sup>g</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">721 (61.00)</td>
<td style="text-align: left;">31,989 (26.08)</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">461 (39.00)</td>
<td style="text-align: left;">90,643 (73.92)</td>
</tr>
</tbody>
</table>

Data are expressed as *n* (%) unless otherwise specified

*ISTAT* Italian National Institute of Statistics, *NA* not available, *SD* standard deviation

<sup>a</sup>Data of geographical distribution were not recorded for 15 interviews as these were collected by a previous panel company with which the study team terminated the contract

<sup>b</sup>Education of the general public was calculated on a sample of 51,978 residents aged \> 15 years

<sup>c</sup>Occupational data are approximations of ISTAT data; the number of students was calculated as the sum of university students and those enrolled in the last year of high school (aged 18 years)

<sup>d</sup>ISTAT classification of ‘separated’ is within the married category

<sup>e</sup>Number of children in the general public is calculated on a sample of 14,109 couples where the woman is aged \> 15 years

<sup>f</sup>Number of people living in the same household is calculated on a sample of 25,593 families

<sup>g</sup>Number of chronic conditions in the general public is calculated on a sample of 122,632 people aged 18+ years

</div>

### EQ-5D-5L Health States

Of the 3125 possible health states generated by the EQ-5D-5L, 106 (3.4%) were selected by at least one study participant. Table <a href="#Tab2" data-ref-type="table">2</a> reports the 19 states that cumulatively made up 89% of the sample with a mean EQ-5D index value and mean EQ VAS score. More than one-third of respondents (410, 34.7%) indicated a health state without any problems (‘11111’). The mean EQ VAS score for these respondents was 88.7. The second most selected state (16%) was ‘11112’, indicating only slight anxiety/depression, followed by ‘11121’, indicating slight pain/discomfort (12.9%). The corresponding mean EQ VAS scores were 85.6 and 82.9, respectively. The worst reported health state was 44553, with an associated index value of −0.232 and a mean EQ VAS score of 30.

<div id="Tab2" class="table-wrap">

<div class="caption">

List of most frequent health states selected (89% of the sample)

</div>

| Health state | *N*  | %     | % cumulative | Mean EQ-5D index value | Mean EQ VAS score |
|--------------|------|-------|--------------|------------------------|-------------------|
| 11111        | 410  | 34.69 | 34.69        | 1                      | 88.74             |
| 11112        | 190  | 16.07 | 50.76        | 0.956                  | 85.56             |
| 11121        | 153  | 12.94 | 63.71        | 0.953                  | 82.89             |
| 11122        | 96   | 8.12  | 71.83        | 0.909                  | 78.73             |
| 11123        | 31   | 2.62  | 74.45        | 0.844                  | 76.06             |
| 11131        | 30   | 2.54  | 76.99        | 0.912                  | 75.67             |
| 11113        | 24   | 2.03  | 79.02        | 0.891                  | 81.79             |
| 21121        | 22   | 1.86  | 80.88        | 0.902                  | 75.59             |
| 11132        | 18   | 1.52  | 82.40        | 0.868                  | 72.41             |
| 11221        | 11   | 0.93  | 83.33        | 0.903                  | 77.18             |
| 21122        | 10   | 0.85  | 84.18        | 0.858                  | 81.12             |
| 11211        | 9    | 0.76  | 84.94        | 0.950                  | 82.23             |
| 21111        | 9    | 0.76  | 85.70        | 0.949                  | 79.78             |
| 11223        | 7    | 0.59  | 86.29        | 0.794                  | 69.57             |
| 21132        | 7    | 0.59  | 86.89        | 0.817                  | 72.14             |
| 21221        | 7    | 0.59  | 87.48        | 0.852                  | 75.00             |
| 11212        | 6    | 0.51  | 87.99        | 0.906                  | 80.33             |
| 11213        | 6    | 0.51  | 88.49        | 0.841                  | 78.34             |
| 21222        | 6    | 0.51  | 89.00        | 0.808                  | 71.67             |
| Other states | 130  | 11.00 | 100.00       | 0.719                  | 63.54             |
| Total        | 1182 | 100   | 100.00       | 0.927                  | 81.83             |

*VAS* visual analogue scale

</div>

### EQ-5D-5L Dimensions

In all dimensions, more than 50% of participants reported answers of ‘no problems’ (level 1), although this percentage varied between 95.8% for SC and 56.7% for PD. Accordingly, the probability of having ‘any problems’ (from level 2 to 5) was variable across dimensions: 12.1% for MO, 4.2% for SC, 11.6% for UA, 43.3% for PD, and 41.2% for AD. The frequency of levels 4 and 5 answers was very low and ranged between 0.3% for SC and 1.3% for PD, as expected in a general population sample (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<figure id="Fig1">
<p><img src="40258_2022_772_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40258_2022_772_Fig1_HTML.gif" /></p>
<figcaption>Frequency of severity levels (from 2 to 5) in EQ-5D-5L dimensions</figcaption>
</figure>

The distribution of answers was comparable across sexes for all dimensions except AD, where women reported a significantly higher (*p* \< 0.001) frequency (49.7%) of ‘any problems’ (levels 2–5) compared with men (32.3%) (Fig. <a href="#Fig2" data-ref-type="fig">2</a> and electronic Supplementary Table S2). In addition, the frequency of problems increased with age for all dimensions, except for AD, where the percentage of respondents indicating any severity level between 2 and 5 varied from 56.0% in the youngest group (18–24 years) to a minimum of 30.0% among the older groups (\>75 years), as reported in Fig. <a href="#Fig3" data-ref-type="fig">3</a> and electronic supplementary Table S2.

<figure id="Fig2">
<p><img src="40258_2022_772_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40258_2022_772_Fig2_HTML.gif" /></p>
<figcaption>Frequency of any problems (levels 2–5) in EQ-5D-5L dimensions, by sex</figcaption>
</figure>

<figure id="Fig3">
<p><img src="40258_2022_772_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="40258_2022_772_Fig3_HTML.gif" /></p>
<figcaption>Frequency of any problems (levels 2–5) in EQ-5D-5L dimensions, by age group</figcaption>
</figure>

### EQ-5D-5L Index Value

The mean index value (± SD) for the entire sample was 0.93 (± 0.11) and is observed to be higher in men (0.94 ± 0.10) than in women (0.92 ± 0.12) \[*p* = 0.01\]. The value gradually decreased with age, decreasing from 0.95 (± 0.06) in the younger class (18–24 years) to 0.91 (± 0.13) in the older class (≥ 75 years). Such a decrement was relatively more marked in women (from 0.94 to 0.92) than in men (from 0.95 to 0.94) (Table <a href="#Tab3" data-ref-type="table">3</a>, Fig. <a href="#Fig4" data-ref-type="fig">4</a>).

<div id="Tab3" class="table-wrap">

<div class="caption">

EQ-5D-5L index value and EQ VAS, by sociodemographic characteristics

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th rowspan="2" style="text-align: left;"><em>N</em></th>
<th colspan="5" style="text-align: left;">EQ-5D-5L index value</th>
<th colspan="5" style="text-align: left;">EQ VAS score</th>
</tr>
<tr>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Median</th>
<th style="text-align: left;">Range</th>
<th style="text-align: left;"><em>p-</em>value<sup>a</sup></th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Median</th>
<th style="text-align: left;">Range</th>
<th style="text-align: left;"><em>p-</em>value<sup>a</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Total</td>
<td style="text-align: left;">1182</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.83</td>
<td style="text-align: center;">13.53</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Age, years</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 18–24</td>
<td style="text-align: left;">109</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: center;">0.06</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.68, 1</td>
<td style="text-align: center;">&lt;  0.001</td>
<td style="text-align: center;">87.02</td>
<td style="text-align: center;">8.90</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">60, 100</td>
<td style="text-align: center;">&lt;  0.001</td>
</tr>
<tr>
<td style="text-align: left;"> 25–34</td>
<td style="text-align: left;">166</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.01, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">84.38</td>
<td style="text-align: center;">11.33</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 35–44</td>
<td style="text-align: left;">200</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.35, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">83.59</td>
<td style="text-align: center;">12.25</td>
<td style="text-align: left;">89.5</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 45–54</td>
<td style="text-align: left;">251</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.37, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">82.40</td>
<td style="text-align: center;">12.94</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 55–64</td>
<td style="text-align: left;">211</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.12, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">79.57</td>
<td style="text-align: center;">15.32</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 65–74</td>
<td style="text-align: left;">205</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">78.22</td>
<td style="text-align: center;">14.82</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 75+</td>
<td style="text-align: left;">40</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.47, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">75.10</td>
<td style="text-align: center;">16.43</td>
<td style="text-align: left;">77.5</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">575</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.15, 1</td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;">81.56</td>
<td style="text-align: center;">13.04</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;">0.517</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">606</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">82.07</td>
<td style="text-align: center;">14.00</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Educational level</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Elementary or middle inferior</td>
<td style="text-align: left;">77</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;">&lt;  0.001</td>
<td style="text-align: center;">78.19</td>
<td style="text-align: center;">15.86</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;">0.043</td>
</tr>
<tr>
<td style="text-align: left;"> High school</td>
<td style="text-align: left;">637</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.01, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.50</td>
<td style="text-align: center;">13.61</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Academic degree</td>
<td style="text-align: left;">468</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.15, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">82.87</td>
<td style="text-align: center;">12.90</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Employment status</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Employed</td>
<td style="text-align: left;">487</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.23, 1</td>
<td style="text-align: center;">&lt;  0.001</td>
<td style="text-align: center;">83.53</td>
<td style="text-align: center;">12.11</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;">&lt;  0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Self employed</td>
<td style="text-align: left;">150</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.47, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">82.04</td>
<td style="text-align: center;">13.23</td>
<td style="text-align: left;">84</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Student</td>
<td style="text-align: left;">112</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: center;">0.06</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.68, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">87.14</td>
<td style="text-align: center;">8.36</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">61, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Retired</td>
<td style="text-align: left;">234</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.15, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">77.46</td>
<td style="text-align: center;">14.57</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed</td>
<td style="text-align: left;">92</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.01, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.14</td>
<td style="text-align: center;">16.48</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Housewife</td>
<td style="text-align: left;">96</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">78.84</td>
<td style="text-align: center;">16.18</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td style="text-align: left;">11</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">0.74, 0.96</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">73.91</td>
<td style="text-align: center;">12.33</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">45, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Marital status</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Single</td>
<td style="text-align: left;">350</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.53, 1</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">83.90</td>
<td style="text-align: center;">11.80</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Married or cohabiting</td>
<td style="text-align: left;">727</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.30</td>
<td style="text-align: center;">13.74</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Divorced or separated</td>
<td style="text-align: left;">78</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.01, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">79.30</td>
<td style="text-align: center;">17.50</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Widower/widow</td>
<td style="text-align: left;">27</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">0.53, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">76.48</td>
<td style="text-align: center;">12.63</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">50, 95</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Parental status</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">691</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">80.33</td>
<td style="text-align: center;">14.27</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">491</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">0.24, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">83.93</td>
<td style="text-align: center;">12.13</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Household size</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">138</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.24, 1</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">80.44</td>
<td style="text-align: center;">15.22</td>
<td style="text-align: left;">82.5</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: left;">369</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.66</td>
<td style="text-align: center;">13.80</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td style="text-align: left;">2852</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.15, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">80.90</td>
<td style="text-align: center;">13.28</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> 4</td>
<td style="text-align: left;">275</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">83.15</td>
<td style="text-align: center;">12.81</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 5</td>
<td style="text-align: left;">115</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">− 0.01, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">83.20</td>
<td style="text-align: center;">12.65</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Household income (per year)</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> &lt; €14.000</td>
<td style="text-align: left;">93</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.12, 1</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">78.76</td>
<td style="text-align: center;">15.81</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;">0.003</td>
</tr>
<tr>
<td style="text-align: left;"> €14.000–€20.999</td>
<td style="text-align: left;">135</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.16, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.59</td>
<td style="text-align: center;">14.28</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €21.000–€27.999</td>
<td style="text-align: left;">168</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.01</td>
<td style="text-align: center;">13.95</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €28.000–€34.999</td>
<td style="text-align: left;">160</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.42, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">80.59</td>
<td style="text-align: center;">14.00</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €35.000–€41.999</td>
<td style="text-align: left;">159</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.01, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">82.50</td>
<td style="text-align: center;">12.88</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €42.000–€48.999</td>
<td style="text-align: left;">64</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.63, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.11</td>
<td style="text-align: center;">12.85</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €49.000–€55.999</td>
<td style="text-align: left;">90</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">− 0.15, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">79.41</td>
<td style="text-align: center;">14.36</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €56.000–€62.999</td>
<td style="text-align: left;">50</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.77, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">84.40</td>
<td style="text-align: center;">12.33</td>
<td style="text-align: left;">87.5</td>
<td style="text-align: left;">40, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €63.000–€69.999</td>
<td style="text-align: left;">40</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.59, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">84.93</td>
<td style="text-align: center;">10.21</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">50, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €70.000–€90.999</td>
<td style="text-align: left;">43</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.54, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">84.16</td>
<td style="text-align: center;">11.96</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">40, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> €91.000 or more</td>
<td style="text-align: left;">13</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.47, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">83.39</td>
<td style="text-align: center;">14.00</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">50, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to answer</td>
<td style="text-align: left;">167</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">84.43</td>
<td style="text-align: center;">11.902</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">40, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Caregiver role</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">185</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.53, 1</td>
<td style="text-align: center;">0.714</td>
<td style="text-align: center;">81.49</td>
<td style="text-align: center;">11.97</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">30, 100</td>
<td style="text-align: center;">0.719</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">997</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">– 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.89</td>
<td style="text-align: center;">13.81</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Self-sufficiency level of the assisted person</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Slightly not self-sufficient</td>
<td style="text-align: left;">41</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.05</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.84, 1</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">82.29</td>
<td style="text-align: center;">9.37</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">60, 100</td>
<td style="text-align: center;">0.003</td>
</tr>
<tr>
<td style="text-align: left;"> Moderately not self-sufficient</td>
<td style="text-align: left;">84</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.53, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">82.66</td>
<td style="text-align: center;">10.79</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">60, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Severely not self-sufficient</td>
<td style="text-align: left;">60</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.08</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.63, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">79.32</td>
<td style="text-align: center;">14.71</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">3, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Social assistance recipiency</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">42</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: left;">0.12, 1</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">77.55</td>
<td style="text-align: center;">18.76</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;">0.037</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">1140</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">– 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.99</td>
<td style="text-align: center;">13.29</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Chronic condition</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">461</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">– 0.23, 1</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">75.48</td>
<td style="text-align: center;">15.71</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">721</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: center;">0.06</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.53, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">85.89</td>
<td style="text-align: center;">10.02</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">40, 100</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Experience of serious illness</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">232</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.96</td>
<td style="text-align: left;">0.34, 1</td>
<td style="text-align: center;">0.224</td>
<td style="text-align: center;">83.58</td>
<td style="text-align: center;">12.29</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">40, 100</td>
<td style="text-align: center;">0.028</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">950</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">– 0.23, 1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">81.40</td>
<td style="text-align: center;">13.79</td>
<td style="text-align: left;">83</td>
<td style="text-align: left;">20, 100</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

*ANOVA* analysis of variance, *SD* standard deviation, *VAS* visual analogue scale

<sup>a</sup>*t*-test (two groups) or ANOVA (more than two)

</div>

<figure id="Fig4">
<p><img src="40258_2022_772_Fig4_HTML.jpg" id="MO4" /></p>
<p><img src="40258_2022_772_Fig4_HTML.gif" /></p>
<figcaption>EQ-5D-5L index value, by sex and age class. Error Bar: IC 95%</figcaption>
</figure>

The EQ-5D-5L index value was, on average, significantly lower in some groups of participants (Table <a href="#Tab3" data-ref-type="table">3</a>). In detail, a poorer health status was observed in people with low educational level (0.89 ± 0.19) and low income (\< €14,000; 0.90 ± 0.15), pensioners (0.91 ± 0.14), housewives (0.90 ± 0.16), divorcees (0.89 ± 0.17), widowers/widows (0.91 ± 0.11), social assistance recipients (0.85 ± 0.22), and those affected by chronic illnesses (0.88 ± 0.15). Conversely, no significant EQ-5D index value reduction was observed in caregivers, unless the assisted person was severely disabled (0.92 ± 0.08), and in those who experienced a serious illness in the past.

### EQ VAS

The mean (± SD) EQ VAS score was 81.8 (± 13.5) and was found to be very similar for men (81.6 ± 13.0) and women (82.0 ± 14.0), i.e., without a significant difference (*p* = 0.517). Similar to the index value, the mean EQ VAS score gradually decreased with age in both sexes, moving from 87.0 (± 8.9) in the younger class (18–24 years) to 75.1 (± 16.4) in the older class (≥ 75 years). However, women exhibited higher values than men in the younger group (under 44 years of age) and the older group (\> 65 years of age), and lower in the middle-age group (45–64 years) (Table <a href="#Tab3" data-ref-type="table">3</a>, Fig. <a href="#Fig5" data-ref-type="fig">5</a>).

<figure id="Fig5">
<p><img src="40258_2022_772_Fig5_HTML.jpg" id="MO5" /></p>
<p><img src="40258_2022_772_Fig5_HTML.gif" /></p>
<figcaption>EQ VAS score, by sex and age class. Error bar: IC 95%</figcaption>
</figure>

Self-reported health, based on the EQ VAS score, was, on average, significantly poorer in some groups of participants (Table <a href="#Tab3" data-ref-type="table">3</a>), such as people with low education (78.2 ± 15.9) and low income (\< €14,000, 78.8 ± 15.8), pensioners (77.5 ± 14.6), housewives (78.8 ± 16.2), divorcees (79.3 ± 17.5), widowers/widows (76.5 ± 12.6), social assistance recipients (77.5 ± 18.8), and those affected by chronic illnesses (75.5 ± 15.7). Conversely, those who had a previous experience of serious illness reported a higher EQ VAS score on average (0.94 ± 0.09). As for the EQ-5D-5L index, no significant difference was observed in EQ VAS scores by caregiver status, except for carers of the severely disabled (79.3 ± 14.7).

### Multivariate Regression

Table <a href="#Tab4" data-ref-type="table">4</a> presents the results of multivariate linear regression of the EQ-5D-5L index value and EQ VAS score, with statistically significant sociodemographic predictors only (*p* \< 0.05). The presence of chronic health conditions, social recipient status and female sex were negatively associated with the index value, while a higher income level had a positive impact. Similarly, higher annual household income and previous experience with serious illness were positively associated with the EQ VAS score, while chronic conditions and advanced age (\> 55 years) were negative significant predictors.

<div id="Tab4" class="table-wrap">

<div class="caption">

Ordinary least square regression of EQ-5D-5L index, EQ VAS and sociodemographic variables

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">EQ-5D index value</th>
<th colspan="4" style="text-align: left;">EQ VAS score</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">Robust SE</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;"><em>p</em>-value</th>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">Robust SE</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;"><em>p</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Chronic condition(s)</td>
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
<td style="text-align: left;"> No (ref.)</td>
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
<td style="text-align: left;"> Yes</td>
<td style="text-align: center;">− 0.073</td>
<td style="text-align: center;">0.007</td>
<td style="text-align: center;">− 0.087, − 0.059</td>
<td style="text-align: center;">0.000**</td>
<td style="text-align: center;">− 9.371</td>
<td style="text-align: center;">0.829</td>
<td style="text-align: center;">− 10.997, − 7.745</td>
<td style="text-align: center;">0.000**</td>
</tr>
<tr>
<td style="text-align: left;">Social assistance (yes)</td>
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
<td style="text-align: left;"> No (ref.)</td>
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
<td style="text-align: left;">Y es</td>
<td style="text-align: center;">− 0.070</td>
<td style="text-align: center;">0.031</td>
<td style="text-align: center;">− 0.130, − 0.009</td>
<td style="text-align: center;">0.023*</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Sex</td>
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
<td style="text-align: left;"> Male (ref.)</td>
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
<td style="text-align: left;"> Female</td>
<td style="text-align: center;">− 0.020</td>
<td style="text-align: center;">0.006</td>
<td style="text-align: center;">− 0.032, − 0.008</td>
<td style="text-align: center;">0.001**</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Age group, years</td>
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
<td style="text-align: left;"> 18–34 (ref.)</td>
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
<td style="text-align: left;"> 35–44</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">− 1.572</td>
<td style="text-align: center;">1.029</td>
<td style="text-align: center;">− 3.592, 0.447</td>
<td style="text-align: center;">0.127</td>
</tr>
<tr>
<td style="text-align: left;"> 45–54</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">− 1.407</td>
<td style="text-align: center;">1.030</td>
<td style="text-align: center;">− 3.428, 0.613</td>
<td style="text-align: center;">0.172</td>
</tr>
<tr>
<td style="text-align: left;"> 55–64</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">− 2.682</td>
<td style="text-align: center;">1.171</td>
<td style="text-align: center;">− 4.980, − 0.384</td>
<td style="text-align: center;">0.022*</td>
</tr>
<tr>
<td style="text-align: left;"> 65+</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">− 4.125</td>
<td style="text-align: center;">1.139</td>
<td style="text-align: center;">− 6.361, − 1.890</td>
<td style="text-align: center;">0.000**</td>
</tr>
<tr>
<td style="text-align: left;">Annual household income (€)</td>
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
<td style="text-align: left;"> &lt; 34,999 (ref.)</td>
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
<td style="text-align: left;"> 35,000–62,999</td>
<td style="text-align: center;">0.014</td>
<td style="text-align: center;">0.007</td>
<td style="text-align: center;">0.000, 0.027</td>
<td style="text-align: center;">0.048*</td>
<td style="text-align: center;">1.894</td>
<td style="text-align: center;">0.871</td>
<td style="text-align: center;">0.185, 3.603</td>
<td style="text-align: center;">0.030*</td>
</tr>
<tr>
<td style="text-align: left;"> &gt; 63,000</td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;">− 0.011, 0.030</td>
<td style="text-align: center;">0.354</td>
<td style="text-align: center;">3.966</td>
<td style="text-align: center;">1.229</td>
<td style="text-align: center;">1.554, 6.377</td>
<td style="text-align: center;">0.001**</td>
</tr>
<tr>
<td style="text-align: left;"> Unreported</td>
<td style="text-align: center;">0.016</td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;">0.001, 0.031</td>
<td style="text-align: center;">0.031*</td>
<td style="text-align: center;">2.602</td>
<td style="text-align: center;">1.037</td>
<td style="text-align: center;">0.568, 4.636</td>
<td style="text-align: center;">0.012*</td>
</tr>
<tr>
<td style="text-align: left;">Experience of serious illness</td>
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
<td style="text-align: left;"> No (ref.)</td>
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
<td style="text-align: left;"> Yes</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1.902</td>
<td style="text-align: center;">0.850</td>
<td style="text-align: center;">0.234, 3.570</td>
<td style="text-align: center;">0.025*</td>
</tr>
<tr>
<td style="text-align: left;"> Constant</td>
<td style="text-align: center;">0.962</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">0.952, 0.972</td>
<td style="text-align: center;">0.000**</td>
<td style="text-align: center;">85.736</td>
<td style="text-align: center;">0.726</td>
<td style="text-align: center;">84.312, 87.161</td>
<td style="text-align: center;">0.000**</td>
</tr>
<tr>
<td style="text-align: left;"> AIC</td>
<td style="text-align: center;">− 2010.75</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">9323.86</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> BIC</td>
<td style="text-align: center;">− 1975.23</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">9374.61</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

*AIC* Akaike information criterion, *BIC* Bayesian information criterion, *CI* confidence interval, *Coeff.* Coefficient, *SE* standard error, *VAS* visual analogue scale

*\*\*p* \< 0.01, \**p* \< 0.05

</div>

### Cross-Country Comparison

Thirty-five studies \[7, 15–48\] reporting EQ-5D-5L population norms in other countries were reviewed. The cross-country comparison of the mean EQ-5D index value and EQ VAS score is reported in Table <a href="#Tab5" data-ref-type="table">5</a>. The mean EQ-5D-5L utility index value for Italy (0.93) ranked second after Bulgaria (0.94) in Europe, and comparable with countries such as Barbados (0.94) and Hong Kong (0.92) outside Europe; however, it was lower than in many non-European countries (i.e., Belize, 0.95; China, 0.96; Colombia, 0.95; Jamaica, 0.95; Trinidad and Tobago, 0.95).

<div id="Tab5" class="table-wrap">

<div class="caption">

Cross-country comparison

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Country</th>
<th style="text-align: left;">Reference</th>
<th style="text-align: left;">Population</th>
<th style="text-align: left;">Sample size</th>
<th style="text-align: left;">Mean age, years</th>
<th style="text-align: left;">% 11111 (full health)</th>
<th colspan="5" style="text-align: left;">% Level 1 (no problem)</th>
<th style="text-align: left;">EQ-Index</th>
<th style="text-align: left;">EQ VAS score</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">Mean</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Europe</td>
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
<td style="text-align: left;"> Belgium</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR17">17</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">7509</td>
<td style="text-align: left;">48.6</td>
<td style="text-align: left;">35.2%</td>
<td style="text-align: left;">81.0</td>
<td style="text-align: left;">94.0</td>
<td style="text-align: left;">81.0</td>
<td style="text-align: left;">44.0</td>
<td style="text-align: left;">69.0</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">77.1</td>
</tr>
<tr>
<td style="text-align: left;"> Bulgaria</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR19">19</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1005</td>
<td style="text-align: left;">47.5</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">72.8</td>
<td style="text-align: left;">86.4</td>
<td style="text-align: left;">78.1</td>
<td style="text-align: left;">60.8</td>
<td style="text-align: left;">65.4</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">77.9</td>
</tr>
<tr>
<td style="text-align: left;"> Denmark</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR25">25</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1012</td>
<td style="text-align: left;">53.3</td>
<td style="text-align: left;">30.2%</td>
<td style="text-align: left;">74.6</td>
<td style="text-align: left;">95.3</td>
<td style="text-align: left;">73.2</td>
<td style="text-align: left;">51.1</td>
<td style="text-align: left;">80.9</td>
<td style="text-align: left;">0.90</td>
<td style="text-align: left;">82.4</td>
</tr>
<tr>
<td style="text-align: left;"> Germany</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR26">26</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">5001</td>
<td style="text-align: left;">50.7</td>
<td style="text-align: left;">30.6%</td>
<td style="text-align: left;">64.6</td>
<td style="text-align: left;">92.8</td>
<td style="text-align: left;">71.7</td>
<td style="text-align: left;">43.1</td>
<td style="text-align: left;">74.9</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">71.6</td>
</tr>
<tr>
<td style="text-align: left;"> Germany</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR27">27</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2040</td>
<td style="text-align: left;">47.3</td>
<td style="text-align: left;">64.3%</td>
<td style="text-align: left;">81.7</td>
<td style="text-align: left;">93.0</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">71.2</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">85.1</td>
</tr>
<tr>
<td style="text-align: left;"> Germany</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR28">28</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">6074</td>
<td style="text-align: left;">47.1</td>
<td style="text-align: left;">61.6%</td>
<td style="text-align: left;">82.3</td>
<td style="text-align: left;">94.0</td>
<td style="text-align: left;">86.8</td>
<td style="text-align: left;">68.3</td>
<td style="text-align: left;">82.1</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">84.3</td>
</tr>
<tr>
<td style="text-align: left;"> Germany</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR29">29</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2469</td>
<td style="text-align: left;">50.5</td>
<td style="text-align: left;">47.5%</td>
<td style="text-align: left;">76.5</td>
<td style="text-align: left;">91.7</td>
<td style="text-align: left;">81.7</td>
<td style="text-align: left;">54.4</td>
<td style="text-align: left;">77.4</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">91.5</td>
</tr>
<tr>
<td style="text-align: left;"> Germany</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR30">30</span>]</td>
<td style="text-align: left;">Elderly (&gt; 65 years of age)</td>
<td style="text-align: left;">290</td>
<td style="text-align: left;">73.1</td>
<td style="text-align: left;">21.4%</td>
<td style="text-align: left;">47.9</td>
<td style="text-align: left;">84.5</td>
<td style="text-align: left;">64.8</td>
<td style="text-align: left;">31.7</td>
<td style="text-align: left;">72.4</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">73.2</td>
</tr>
<tr>
<td style="text-align: left;"> Ireland</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR33">33</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1131</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">46.0%</td>
<td style="text-align: left;">78.3</td>
<td style="text-align: left;">93.7</td>
<td style="text-align: left;">80.8</td>
<td style="text-align: left;">59.5</td>
<td style="text-align: left;">78.0</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">79.9</td>
</tr>
<tr>
<td style="text-align: left;"> Italy</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1182</td>
<td style="text-align: left;">48.3</td>
<td style="text-align: left;">34.7%</td>
<td style="text-align: left;">87.9</td>
<td style="text-align: left;">95.8</td>
<td style="text-align: left;">88.4</td>
<td style="text-align: left;">56.7</td>
<td style="text-align: left;">58.8</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">81.8</td>
</tr>
<tr>
<td style="text-align: left;"> Norway</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR37">37</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">3120</td>
<td style="text-align: left;">50.9</td>
<td style="text-align: left;">32.2%</td>
<td style="text-align: left;">82.0</td>
<td style="text-align: left;">92.7</td>
<td style="text-align: left;">75.8</td>
<td style="text-align: left;">37.9</td>
<td style="text-align: left;">64.6</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">77.9</td>
</tr>
<tr>
<td style="text-align: left;"> Poland</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR38">38</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">3400</td>
<td style="text-align: left;">48.3</td>
<td style="text-align: left;">52.0%</td>
<td style="text-align: left;">74.2</td>
<td style="text-align: left;">90.9</td>
<td style="text-align: left;">82.6</td>
<td style="text-align: left;">47.8</td>
<td style="text-align: left;">58.5</td>
<td style="text-align: left;">0.89</td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> Poland</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR39">39</span>]</td>
<td style="text-align: left;">Diabetes patients</td>
<td style="text-align: left;">255</td>
<td style="text-align: left;">64.6</td>
<td style="text-align: left;">9.4%</td>
<td style="text-align: left;">38.0</td>
<td style="text-align: left;">74.1</td>
<td style="text-align: left;">59.2</td>
<td style="text-align: left;">18.4</td>
<td style="text-align: left;">32.2</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: left;">56.6</td>
</tr>
<tr>
<td style="text-align: left;"> Slovenia</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR41">41</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1071</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">73.1</td>
<td style="text-align: left;">92.6</td>
<td style="text-align: left;">78.1</td>
<td style="text-align: left;">41.9</td>
<td style="text-align: left;">61.1</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">79.9</td>
</tr>
<tr>
<td style="text-align: left;"> Spain</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR42">42</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">20,587</td>
<td style="text-align: left;">48.0</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">85.8</td>
<td style="text-align: left;">93.9</td>
<td style="text-align: left;">89.0</td>
<td style="text-align: left;">74.6</td>
<td style="text-align: left;">85.0</td>
<td style="text-align: left;">0.62–0.98<sup>a</sup></td>
<td style="text-align: left;">54.6–88.2<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Spain</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">21,007</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">62.0%</td>
<td style="text-align: left;">82.5</td>
<td style="text-align: left;">92.1</td>
<td style="text-align: left;">86.3</td>
<td style="text-align: left;">71.7</td>
<td style="text-align: left;">83.6</td>
<td style="text-align: left;">0.90</td>
<td style="text-align: left;">75.7</td>
</tr>
<tr>
<td style="text-align: left;"> Spain</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;">Diabetes patients</td>
<td style="text-align: left;">1857</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">33.7%</td>
<td style="text-align: left;">53.2</td>
<td style="text-align: left;">76.4</td>
<td style="text-align: left;">62.5</td>
<td style="text-align: left;">45.6</td>
<td style="text-align: left;">70.6</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">61.1</td>
</tr>
<tr>
<td style="text-align: left;"> Sweden</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">25,867</td>
<td style="text-align: left;">64.3</td>
<td style="text-align: left;">24.1%</td>
<td style="text-align: left;">67.3–68.0<sup>b</sup></td>
<td style="text-align: left;">88.4–89.9<sup>b</sup></td>
<td style="text-align: left;">67.9–70.6<sup>b</sup></td>
<td style="text-align: left;">28.8–35.5<sup>b</sup></td>
<td style="text-align: left;">57.8–68.4<sup>b</sup></td>
<td style="text-align: left;">0.90</td>
<td style="text-align: left;">76.6</td>
</tr>
<tr>
<td style="text-align: left;">Extra-Europe</td>
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
<td style="text-align: left;"> South Australia</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR15">15</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2908</td>
<td style="text-align: left;">46.3</td>
<td style="text-align: left;">42.8%</td>
<td style="text-align: left;">74.3</td>
<td style="text-align: left;">95.4</td>
<td style="text-align: left;">82.7</td>
<td style="text-align: left;">55.6</td>
<td style="text-align: left;">75.3</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">78.6</td>
</tr>
<tr>
<td style="text-align: left;"> Barbados</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR16">16</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2347</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">66.4%</td>
<td style="text-align: left;">91.1</td>
<td style="text-align: left;">97.4</td>
<td style="text-align: left;">93.9</td>
<td style="text-align: left;">75.6</td>
<td style="text-align: left;">87.0</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">81.9</td>
</tr>
<tr>
<td style="text-align: left;"> Belize</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR18">18</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2078</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">67.8%</td>
<td style="text-align: left;">88.0</td>
<td style="text-align: left;">96.3</td>
<td style="text-align: left;">91.7</td>
<td style="text-align: left;">78.8</td>
<td style="text-align: left;">85.6</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">82.6</td>
</tr>
<tr>
<td style="text-align: left;"> Canada (Alberta)</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR20">20</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">30,576</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">72.8</td>
<td style="text-align: left;">94.1</td>
<td style="text-align: left;">74.0</td>
<td style="text-align: left;">36.0</td>
<td style="text-align: left;">62.8</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">77.4</td>
</tr>
<tr>
<td style="text-align: left;"> Canada (Quebec)</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR21">21</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2704</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">20.8%</td>
<td style="text-align: left;">72.9</td>
<td style="text-align: left;">91.6</td>
<td style="text-align: left;">70.9</td>
<td style="text-align: left;">32.1</td>
<td style="text-align: left;">46.8</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">75.9</td>
</tr>
<tr>
<td style="text-align: left;"> China</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR22">22</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1296</td>
<td style="text-align: left;">42.0</td>
<td style="text-align: left;">54.0%</td>
<td style="text-align: left;">94.4</td>
<td style="text-align: left;">98.9</td>
<td style="text-align: left;">95.4</td>
<td style="text-align: left;">70.1</td>
<td style="text-align: left;">73.1</td>
<td style="text-align: left;">0.96</td>
<td style="text-align: left;">86.0</td>
</tr>
<tr>
<td style="text-align: left;"> China (Hong Kong)</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR23">23</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1014</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">46.0%</td>
<td style="text-align: left;">88.3</td>
<td style="text-align: left;">98.5</td>
<td style="text-align: left;">91.4</td>
<td style="text-align: left;">59.5</td>
<td style="text-align: left;">74.0</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">82.7</td>
</tr>
<tr>
<td style="text-align: left;"> Colombia</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR24">24</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">3400</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">52.2%</td>
<td style="text-align: left;">87.0</td>
<td style="text-align: left;">96.8</td>
<td style="text-align: left;">87.5</td>
<td style="text-align: left;">68.3</td>
<td style="text-align: left;">67.7</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">85.3</td>
</tr>
<tr>
<td style="text-align: left;"> Indonesia</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR31">31</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1056</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">44.1%</td>
<td style="text-align: left;">92.0</td>
<td style="text-align: left;">98.1</td>
<td style="text-align: left;">89.2</td>
<td style="text-align: left;">60.3</td>
<td style="text-align: left;">65.7</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">79.4</td>
</tr>
<tr>
<td style="text-align: left;"> Iran</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR32">32</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">3060</td>
<td style="text-align: left;">44.0</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">70.5</td>
<td style="text-align: left;">90.6</td>
<td style="text-align: left;">76.3</td>
<td style="text-align: left;">46.8</td>
<td style="text-align: left;">46.0</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">71.7</td>
</tr>
<tr>
<td style="text-align: left;"> Jamaica</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR16">16</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1423</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">68.9%</td>
<td style="text-align: left;">93.6</td>
<td style="text-align: left;">96.6</td>
<td style="text-align: left;">92.9</td>
<td style="text-align: left;">79.6</td>
<td style="text-align: left;">81.4</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">87.8</td>
</tr>
<tr>
<td style="text-align: left;"> Japan</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR34">34</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">10,183</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">26.8–85.9<sup>a</sup></td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">0.84–0.98<sup>a</sup></td>
<td style="text-align: left;">68.1–84.3<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Japan</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR35">35</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1143</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">55.0</td>
<td style="text-align: left;">63.0–98.0<sup>a</sup></td>
<td style="text-align: left;">87.0–100.0<sup>a</sup></td>
<td style="text-align: left;">73.0–99.0<sup>a</sup></td>
<td style="text-align: left;">39.0–80.0<sup>a</sup></td>
<td style="text-align: left;">73.0–87.0<sup>a</sup></td>
<td style="text-align: left;">0.83–0.95<sup>a</sup></td>
<td style="text-align: left;">NA</td>
</tr>
<tr>
<td style="text-align: left;"> New Zealand</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR36">36</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2468</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">22.0%</td>
<td style="text-align: left;">72.1</td>
<td style="text-align: left;">91.4</td>
<td style="text-align: left;">70.2</td>
<td style="text-align: left;">38.3</td>
<td style="text-align: left;">53.6</td>
<td style="text-align: left;">0.85</td>
<td style="text-align: left;">74.8</td>
</tr>
<tr>
<td style="text-align: left;"> Russia</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR40">40</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1020</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">27.4%</td>
<td style="text-align: left;">64.3</td>
<td style="text-align: left;">88.5</td>
<td style="text-align: left;">68.0</td>
<td style="text-align: left;">51.4</td>
<td style="text-align: left;">55.9</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">74.1</td>
</tr>
<tr>
<td style="text-align: left;"> Trinidad and Tobago</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR46">46</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">2036</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">72.0%</td>
<td style="text-align: left;">89.0</td>
<td style="text-align: left;">97.0</td>
<td style="text-align: left;">93.0</td>
<td style="text-align: left;">78.0</td>
<td style="text-align: left;">89.0</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">83.6</td>
</tr>
<tr>
<td style="text-align: left;"> USA</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR7">7</span>]</td>
<td style="text-align: left;">General (face-to-face)</td>
<td style="text-align: left;">1134</td>
<td style="text-align: left;">46.9</td>
<td style="text-align: left;">31.2%</td>
<td style="text-align: left;">71.6</td>
<td style="text-align: left;">93.5</td>
<td style="text-align: left;">75.3</td>
<td style="text-align: left;">49.0</td>
<td style="text-align: left;">61.6</td>
<td style="text-align: left;">0.85</td>
<td style="text-align: left;">80.4</td>
</tr>
<tr>
<td style="text-align: left;"> USA</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR7">7</span>]</td>
<td style="text-align: left;">General (online)</td>
<td style="text-align: left;">2018</td>
<td style="text-align: left;">45.6</td>
<td style="text-align: left;">23.9%</td>
<td style="text-align: left;">70.6</td>
<td style="text-align: left;">87.0</td>
<td style="text-align: left;">68.8</td>
<td style="text-align: left;">37.1</td>
<td style="text-align: left;">48.9</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: left;">74.6</td>
</tr>
<tr>
<td style="text-align: left;"> Vietnam</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR47">47</span>]</td>
<td style="text-align: left;">Hypertensive patients</td>
<td style="text-align: left;">477</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">62.7</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">71.5</td>
</tr>
<tr>
<td style="text-align: left;"> Vietnam</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR48">48</span>]</td>
<td style="text-align: left;">General</td>
<td style="text-align: left;">1567</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;">67.4%</td>
<td style="text-align: left;">94.6</td>
<td style="text-align: left;">97.5</td>
<td style="text-align: left;">75.7</td>
<td style="text-align: left;">90.0</td>
<td style="text-align: left;">84.8</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">87.4</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *MO* mobility, *NA* not available, *PD* pain/discomfort, *SC* self-care, *UA* usual activities, *VAS* visual analogue scale

<sup>a</sup>Range by age group

<sup>b</sup>Range by sex

</div>

The mean EQ VAS score (81.8) was similar to Denmark (82.4) and Slovenia (79.9) in Europe, and Barbados (81.9), Belize (82.6), Hong Kong (82.7) and the US (80.4) outside Europe. Similar to the EQ-5D index value, the mean EQ VAS scores were also observed to be higher than many other European scores, e.g., in Belgium (77.1), Bulgaria (77.9), Norway (77.9), Sweden (76.6), and Spain (75.7).

The proportion of respondents indicated to live in full health in Italy (34.7%) was similar to Belgium (35.2%), Norway (32.2%) and the US (31.2%), but notably lower than in other countries such as Barbados (66.4%), Belize (67.8%), South Australia (42.8%), Spain (62.0%), Trinidad and Tobago (72.0%), Vietnam (67.4%), and Jamaica (68.9%).

Lastly, the Italian sample reported the highest proportions of ‘no problems’ (level 1) in the three functional dimensions (i.e., MO, SC and UA) in Europe (only Spain had a higher frequency for UA, i.e., 89.0% vs. 88.4%). The frequency of ‘no problems’ in PD (56.7%) was intermediate in the European countries’ distribution. Conversely, excluding studies reporting norms for pathological groups \[39\], only Poland reported a slightly lower value in AD (58.5% vs. 58.8%). In comparison with non-European countries, the Italian value for AD was still among the lowest, but higher than in Iran, New Zealand, Quebec and Russia.

## Discussion

This study showed Italian population norms for the EQ-5D-5L descriptive system, EQ-5D-5L index value and EQ VAS score based on a large sample of individuals recruited for the EQ-5D-5L valuation study \[9\]. The overall health status of Italians captured using EQ-5D-5L was good, with more than one-third selecting the ‘full health’ status (i.e., 11111), similar to other countries such as the US and Norway. Both the EQ-5D index value and EQ VAS score (0.93 and 81.8, respectively) were higher than in the US and most European countries for which population norms are available (i.e., Belgium, Norway, Slovenia, Sweden, Germany, Spain and Poland). On the contrary, some counties, especially those outside Europe, presented considerably higher mean values for both measures (e.g., Colombia, China, Jamaica, Trinidad and Tobago). However, cross-country comparisons should be dealt with cautiously as the self-perception of health reported by EQ-5D might be affected by multiple elements, such as national cultural and religious beliefs \[49\].

The effect of ageing on participants’ health status was also investigated. Both EQ-5D-5L index value and EQ VAS score substantially decreased with age (from 0.95 to 0.91 and from 87.0 to 75.1, respectively), as observed in most of the countries analysed (e.g., Belgium, Belize, Poland, Slovenia, Spain). The deterioration in health approximated by the EQ-5D index value was more rapid in women than in men after the age of 44 years, as observed elsewhere (e.g., in Trinidad and Tobago).

In addition, being affected by a chronic condition such as cancer or cardiovascular disease was also a significant negative predictor of both the EQ-5D index value and EQ VAS score. The negative effect of self-reported pathologies on HRQoL was also observed in other studies that collected a similar variable. For example, in Germany, people with three or more medical conditions had a mean index value of 0.72 (± 0.28) versus 0.95 (± 0.08) of those reporting no medical conditions (*p* \< 0.001) \[26\]. Similarly, in Hong Kong, people without any longstanding health conditions presented a significantly higher EQ-5D-5L index value on average (0.938 ± 0.096) compared with people with at least one health condition (0.873 ± 0.321) \[23\]. In New Zealand, respondents with a chronic condition had a − 0.127 lower mean EQ-5D-5L utility and a − 9.1 mean EQ VAS score than people without a chronic illness \[36\]. Conversely, a previous experience of serious illness had a positive impact on the EQ VAS score (not significant on the EQ-5D index value), which may be due to a greater appreciation of life after having been seriously ill.

Beyond the cross-country comparisons, the results obtained in this study can be used as reference values for surveys with patients to calculate their loss of HRQoL in relation to the values typically observed in the general population. For example, an observational study used EQ-5D-3L in a large group of cancer patients treated in Italian hospitals (*n* = 802), obtaining a mean (± SD) EQ VAS score of 71.5 (± 17.38), i.e., 10 points lower than in this study for the general population (81.8 ± 13.5), and a mean (± SD) utility index value of 0.86 (± 0.13), compared with 0.93 (± 0.11) in our study population \[50\]. However, EQ-5D index values are not fully comparable since they were obtained using the 3L algorithm \[51\].

The mean EQ VAS score (81.8 ± 13.5) in this study is lower than the value (84.8 ± 13.8) obtained in the previous instrument version (EQ-5D-3L) Italian valuation study, which, however, had a younger study sample (mean age 46.6 ± 15.3) than in the current study (48.3 ± 16.1 years), since participants were recruited up to a maximum of 75 years \[51\]. Conversely, in a more recent survey conducted by telephone in Lombardy, the mean EQ VAS score was lower (78.2 ± 18.4) than in our study, as well as the mean EQ-5D-5L index value (0.915 ± 0.10) obtained using a mapping algorithm from 3L values \[52\]. This difference might be explained by a higher mean sample age (51.9 ± 17.6 years) than in our study, although a comparison of mean EQ VAS scores by age class still reveals considerably lower values in all groups \> 45 years of age in the referenced study \[52\].

Despite self-reported health results being overall good in our sample, more than 40% of respondents reported various levels of AD. Indeed, compared with the majority of other countries, the Italian sample reported a higher frequency of level 1 (no problems) in the first three EQ-5D-5L dimensions, but notably lower for the last one. AD especially affected the youngest age classes (below 35 years), where over half of participants (56%) reported any problems, compared with 33% in people \> 65 years of age. Very similar findings were shown in the US study, where 57% of respondents aged 18–24 years indicated any problems with AD versus 24% of respondents aged ≥ 65 years \[7\]. This pattern is also present in other international EQ-5D-5L population norms, such as China, where the prevalence of ‘no problem’ (level 1) in AD dramatically increased from 67.9% in people aged 16–19 years to 88.5% in those aged \> 70 years \[22\], and Canada (Alberta), where the percentage increased from 56.0% in the youngest age group (18–24 years) to 68.8% in those aged \> 75 years \[20\]. The high prevalence of psychological disorders in young people also emerged from other types of research, especially those conducted during the COVID-19 pandemic. For example, a global survey of 1653 people from 63 countries used other questionnaires (i.e., Patient Health Questionnaire and State-Trait Anxiety Questionnaire) to measure the impact of the pandemic on mental health and reported that the youngest age group (18–34 years) was more vulnerable to stress, anxiety and depression \[53\].

In our study, women were observed to be more affected by AD, with almost 50% reporting any problems compared with only one-third of men. These results are consistent with norms from other countries in Europe (e.g., Belgium, Bulgaria, Poland, Slovenia) and elsewhere (e.g., Russia, Trinidad and Tobago). Moreover, the mean EQ VAS score was lower in middle-aged women (45–64 years), who are traditionally more invested in family caregiving responsibilities (according to ISTAT, over 70% of these activities are still carried out by women) \[54\].

The study results can also be compared with EQ-5D data collected from the Italian population shortly before the COVID-19 pandemic. A recent study \[55\] collected the EQ-5D-5L in a sample (*n* = 377) of the adult population (18–75 years) in Italy at two pre-pandemic time points (July 2017 and February 2018), reporting a median value of the EQ VAS to score equal to 80 and lower than the median value (85) recorded in this study. Similarly, the median EQ-5D-5L index value, calculated using the UK algorithm, was 0.88 (July 2017) and 0.84 (February 2018), lower than that recorded in this study (0.96). Moreover, the frequency of participants who indicated full health (‘11111’) was 38% in the first survey and 35% in the second survey, which is in line with the results of this study (34.7%).

This study has some limitations. The sample size (*n* = 1182) was smaller compared with other studies but aligned with some population norms developed in Europe (i.e., Bulgaria, *n* = 1005; Denmark, *n* = 1012; Ireland, *n* = 1131; Slovenia, *n* = 1071). The sample enrolled is also about 4 years younger (on average) than the Italian population (48.3 vs. 52.0 years). In particular, those \> 65 years of age constitute only one-fifth of the sample but represent over one-quarter of the Italian population in 2020. Thus, the average values of the EQ-5D-5L index value and EQ VAS score are likely to be overestimated. The use of videoconferencing interviews, which were embraced due to the concurrent pandemic emergency, might have affected the age of participants, who had to show basic computer skills. Moreover, results might be affected by social desirability bias, which is more evident in an interviewer-administered format whereby participants are less likely to truly disclose, especially in relation to the most sensitive dimensions of EQ-5D (AD). However, this effect is likely to be milder in online surveys than in in-person surveys \[56\]. In relation to data analysis, we applied a simple linear model to EQ-5D data, although alternative options (generalized linear model) are reported in the literature \[57\].

Lastly, we collected data during the second wave of the COVID-19 pandemic, and self-reported health might be affected by the extraordinary events and governmental restrictions in place \[58\]. However, the study recruited a high number of individuals (\>1000) who fully represented the Italian adult population in terms of sex and geographical area. This study also allowed us to test the feasibility of a new, promising mode of survey administration that could be replicated by future EQ-5D-5L valuation studies \[9\].

## Conclusions

This study provided the first EQ-5D-5L population norms for Italy based on a large adult sample and using the newly developed algorithm for the Italian instrument version. These normative values will facilitate empirical comparisons between the general population and more specific patient groups in terms of their HRQoL, and across data collection waves at different time points of general population surveys. Moreover, public health authorities and researchers may use these population norms as a basis to further investigate the healthcare needs of the Italian population (which, for example, appeared substantially affected by anxiety and/or depression, especially among the young), as well as cross-country differences in self-reported health (e.g., North vs. South, or town vs. countryside).

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 47 kb)

</div>

## Acknowledgements

The authors are grateful to the EuroQol Research Foundation, AbbVie Italy, Fondazione SmithKline, Merck Sharp & Dohme Italy, Roche Italy, and Sanofi Italy for their unconditional grants for data collection. They also thank the other interviewers (in alphabetical order: Giovanni Andrulli, Arianna Bertolani, Ludovica Borsoi, Riccardo Consadori, Camilla Falivena, Rachele Freddi, Andrea Moro, Carla Rognoni, Carlotta Varriale), Pepe Research for their support in the data collection, and all survey respondents for their participation in this study.

## Funding

Open access funding provided by Università Commerciale Luigi Bocconi within the CRUI-CARE Agreement.

## Declarations

### Funding

The data collection for this study was supported by unconditional grants from the EuroQol Research Foundation, AbbVie Italy, Fondazione SmithKline, Merck Sharp & Dohme Italy, Roche Italy, and Sanofi Italy.

### Conflicts of interest

Aureliano Paolo Finch is a member of the EuroQol Group and is employed by the EuroQol Office. Michela Meregaglia, Francesco Malandrini, Oriana Ciani, and Claudio Jommi have no competing interests to declare that are relevant to the contents of this article.

### Ethics approval

This study was approved by the Ethics Committee of Bocconi University on 6 October 2020 (approval number: 2020-SA000136.4).

### Consent to participate

Consent to participate was obtained by the market research company prior to scheduling the interview.

### Consent for publication (from patients/participants)

Not applicable.

### Availability of data and material

The data set supporting the conclusions of this study may be available upon reasonable request.

### Code availability

Not applicable.

### Authors' contributions

MM, APF, OC and CJ conceived and designed the study. All authors carried out the data collection with the support of a market research company and a team of interviewers. MM and FM analysed the data, and all authors contributed to the interpretation of the findings. MM drafted the first manuscript version and all authors commented on this version. All authors read and approved the final manuscript.

## References

## References

1. Finch AP, Brazier JE, Mukuria C. What is the evidence for the performance of generic preference-based measures? A systematic overview of reviews. Eur J Health Econ. 2018;19(4):557–570. doi: 10.1007/s10198-017-0902-x.

2. Kennedy-Martin M, Slaap B, Herdman M, van Reenen M, Kennedy-Martin T, Greiner W, et al. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020;21(8):1245–1257. doi: 10.1007/s10198-020-01195-8.

3. National Institute for Health and Care Excellence (NICE). Position statement on use of the EQ-5D-5L value set for England (updated October 2019). https://www.nice.org.uk/about/what-we-do/our-programmes/nice-guidance/technology-appraisal-guidance/eq-5d-5l. Accessed 19 Apr 2022.

4. Italian Drug Agency (AIFA). Linee guida per la compilazione del dossier a supporto della domanda di rimborsabilità e prezzo di un medicinale (ai sensi del D.M. 2 agosto 2019). Version 1.0—2020. https://www.aifa.gov.it/documents/20142/1283800/Linee_guida_dossier_domanda_rimborsabilita.pdf. Accessed 2 Feb 2022.

5. Buchholz I, Janssen MF, Kohlmann T, Feng YS. A systematic review of studies comparing the measurement properties of the three-level and five-level versions of the EQ-5D. Pharmacoeconomics. 2018;36(6):645–661. doi: 10.1007/s40273-018-0642-5.

6. Janssen MF, Szende A, Cabases J, Ramos-Goñi JM, Vilagut G, König HH. Population norms for the EQ-5D-3L: a cross-country analysis of population surveys for 20 countries. Eur J Health Econ. 2019;20:205–216. doi: 10.1007/s10198-018-0955-5.

7. Jiang R, Janssen MFB, Pickard AS. US population norms for the EQ-5D-5L and comparison of norms from face-to-face and online samples. Qual Life Res. 2021;30(3):803–816. doi: 10.1007/s11136-020-02650-y.

8. EuroQol. EQ-5D-5L population norms. https://euroqol.org/eq-5d-instruments/eq-5d-5l-about/population-norms/. Accessed 31 Mar 2022.

9. Finch AP, Meregaglia M, Ciani O, Roudijk B. An EQ-5D-5L value set for Italy using videoconferencing interviews and feasibility of a new mode of administration. Soc Sci Med. 2022;292:114519. doi: 10.1016/j.socscimed.2021.114519.

10. World Health Organization. International classification of diseases. 2010. http://www.who.int/classifications/icd/en/. Accessed 5 Aug 2020.

11. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi: 10.1007/s40273-016-0404-1.

12. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJV, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–473. doi: 10.1016/j.jval.2016.10.012.

13. Italian National Institute of Statistics (ISTAT). Demography in Figures. Resident Population by age, sex, and marital status on 1st January. https://demo.istat.it/. Accessed 3 Jun 2021.

14. Italian National Institute of Statistics (ISTAT). I.Stat: Your direct access to the Italian Statistics. http://dati.istat.it/Index.aspx?lang=en&SubSessionId=7d62f8d1-f775-4a3b-8caa-469114a08b5b. Accessed 3 Jun 2021.

15. McCaffrey N, Kaambwa B, Currow DC, Ratcliffe J. Health-related quality of life measured using the EQ-5D-5L: South Australian population norms. Health Qual Life Outcomes. 2016;14(1):133. doi: 10.1186/s12955-016-0537-0.

16. Bailey H, Janssen MF, La Foucade A, Boodraj G, Wharton M, Castillo P. EQ-5D self-reported health in Barbados and Jamaica with EQ-5D-5L population norms for the English-speaking Caribbean. Health Qual Life Outcomes. 2021;19(1):97. doi: 10.1186/s12955-021-01734-8.

17. Van Wilder L, Charafeddine R, Beutels P, Bruyndonckx R, Cleemput I, Demarest S, et al. Belgian population norms for the EQ-5D-5L, 2018. Qual Life Res. 2022;31(2):527–537. doi: 10.1007/s11136-021-02971-6.

18. Bailey H, Janssen MF, La Foucade A, Castillo P, Boodraj G. Health-related quality of life population norms for belize using EQ-5D-5L. Value Health Reg Issues. 2021;29:45–52. doi: 10.1016/j.vhri.2021.09.005.

19. Encheva M, Djambazov S, Vekov T, Golicki D. EQ-5D-5L Bulgarian population norms. Eur J Health Econ. 2020;21:1169–1178. doi: 10.1007/s10198-020-01225-5.

20. The APERSU Team (2018). Alberta population norms for EQ-5D-5L. APERSU Alberta PROMS and EQ-5D Research and Support Unit 2018. https://apersu.ca/about-eq-5d/norms/. Accessed 31 Mar 2022.

21. Poder TG, Carrier N, Kouakou CRC. Quebec health-related quality-of-life population norms using the EQ-5D-5L: decomposition by sociodemographic data and health problems. Value Health. 2020;23(2):251–259. doi: 10.1016/j.jval.2019.08.008.

22. Yang Z, Busschbach J, Liu G, Luo N. EQ-5D-5L norms for the urban Chinese population in China. Health Qual Life Outcomes. 2018;16(1):210. doi: 10.1186/s12955-018-1036-2.

23. Wong EL, Cheung AW, Wong AY, Xu RH, Ramos-Goñi JM, Rivero-Arias O. Normative profile of health-related quality of life for Hong Kong general population using preference-based instrument EQ-5D-5L. Value Health. 2019;22(8):916–924. doi: 10.1016/j.jval.2019.02.014.

24. Bailey HH, Janssen MF, Varela RO, Moreno JA. EQ-5D-5L population norms and health inequality in Colombia. Value Health Reg Issues. 2021;26:24–32. doi: 10.1016/j.vhri.2020.12.002.

25. Jensen MB, Jensen CE, Gudex C, Pedersen KM, Sørensen SS, Ehlers LH. Danish population health measured by the EQ-5D-5L. Scand J Public Health. 2021 doi: 10.1177/14034948211058060.

26. Grochtdreis T, Dams J, König HH, Konnopka A. Health-related quality of life measured with the EQ-5D-5L: estimation of normative index values based on a representative German population sample and value set. Eur J Health Econ. 2019;20(6):933–944. doi: 10.1007/s10198-019-01054-1.

27. Huber MB, Felix J, Vogelmann M, Leidl R. Health-related quality of life of the general German population in 2015: results from the EQ-5D-5L. Int J Environ Res Public Health. 2017;14(4):426. doi: 10.3390/ijerph14040426.

28. Huber MB, Reitmeir P, Vogelmann M, Leidl R. EQ-5D-5L in the general german population: comparison and evaluation of three yearly cross-section surveys. Int J Environ Res Public Health. 2016;13(3):343. doi: 10.3390/ijerph13030343.

29. Hinz A, Kohlmann T, Stöbel-Richter Y, Zenger M, Brähler E. The quality-of-life questionnaire EQ-5D-5L: psychometric properties and normative values for the general German population. Qual Life Res. 2014;23(2):443–447. doi: 10.1007/s11136-013-0498-2.

30. Marten O, Greiner W. EQ-5D-5L reference values for the German general elderly population. Health Qual Life Outcomes. 2021;19(1):76. doi: 10.1186/s12955-021-01719-7.

31. Dermawan Purba F, Hunfeld JAM, Iskandarsyah A, Sahidah Fitriana T, Sadarjoen SS, Passchier J, et al. Quality of life of the Indonesian general population: test-retest reliability and population norms of the EQ-5D-5L and WHOQOL-BREF. PLoS ONE. 2018;13(5):e0197098. doi: 10.1371/journal.pone.0197098.

32. Emrani Z, Akbari Sari A, Zeraati H, Olyaeemanesh A, Daroudi R. Health-related quality of life measured using the EQ-5D-5 L: population norms for the capital of Iran. Health Qual Life Outcomes. 2020;18(1):108. doi: 10.1186/s12955-020-01365-5.

33. Hobbins A, Barry L, Kelleher D, O'Neill C. The health of the residents of Ireland: population norms for Ireland based on the EQ-5D-5L descriptive system—a cross sectional study. HRB Open Res. 2018;1:22. doi: 10.12688/hrbopenres.12848.1.

34. Shiroiwa T, Noto S, Fukuda T. Japanese population norms of EQ-5D-5L and health utilities index mark 3: disutility catalog by disease and symptom in community settings. Value Health. 2021;24(8):1193–1202. doi: 10.1016/j.jval.2021.03.010.

35. Shiroiwa T, Fukuda T, Ikeda S, Igarashi A, Noto S, Saito S, et al. Japanese population norms for preference-based measures: EQ-5D-3L, EQ-5D-5L, and SF-6D. Qual Life Res. 2016;25(3):707–719. doi: 10.1007/s11136-015-1108-2.

36. Sullivan T, Turner RM, Derrett S, Hansen P. New Zealand population norms for the EQ-5D-5L constructed from the personal value sets of participants in a National Survey. Value Health. 2021;24(9):1308–1318. doi: 10.1016/j.jval.2021.04.1280.

37. Garratt AM, Hansen TM, Augestad LA, Rand K, Stavem K. Norwegian population norms for the EQ-5D-5L: results from a general population survey. Qual Life Res. 2022;31:517–526. doi: 10.1007/s11136-021-02938-7.

38. Golicki D, Niewada M. EQ-5D-5L Polish population norms. Arch Med Sci. 2017;13(1):191–200. doi: 10.5114/aoms.2015.52126.

39. Jankowska A, Golicki D. EQ-5D-5L-based quality of life normative data for patients with self-reported diabetes in Poland. PLoS ONE. 2021;16(9):e0257998. doi: 10.1371/journal.pone.0257998.

40. Hołownia-Voloskova M, Tarbastaev A, Golicki D. Population norms of health-related quality of life in Moscow, Russia: the EQ-5D-5L-based survey. Qual Life Res. 2021;30(3):831–840. doi: 10.1007/s11136-020-02705-0.

41. Prevolnik Rupel V, Ogorevc M. EQ-5D-5L Slovenian population norms. Health Qual Life Outcomes. 2020;18(1):333. doi: 10.1186/s12955-020-01584-w.

42. Hernandez G, Garin O, Pardo Y, Vilagut G, Pont A, Suárez M, et al. Validity of the EQ-5D-5L and reference norms for the Spanish population. Qual Life Res. 2018;27(9):2337–2348. doi: 10.1007/s11136-018-1877-5.

43. Garcia-Gordillo MA, Adsuar JC, Olivares PR. Normative values of EQ-5D-5L: in a Spanish representative population sample from Spanish Health Survey, 2011. Qual Life Res. 2016;25(5):1313–1321. doi: 10.1007/s11136-015-1164-7.

44. Collado Mateo D, García Gordillo MA, Olivares PR, Adsuar JC. Normative values of EQ-5D-5L for diabetes patients from Spain. Nutr Hosp. 2015;32(4):1595–1602. doi: 10.3305/nh.2015.32.4.9605.

45. Sebsibe Teni F, Gerdtham UG, Leidl R, Henriksson M, Åström M, Sun S, et al. Inequality and heterogeneity in health-related quality of life: findings based on a large sample of cross-sectional EQ-5D-5L data from the Swedish general population. Qual Life Res. 2022;31:697–712. doi: 10.1007/s11136-021-02982-3.

46. Bailey H, Janssen MF, La Foucade A, Kind P. EQ-5D-5L population norms and health inequalities for Trinidad and Tobago. PLoS ONE. 2019;14(4):e0214283. doi: 10.1371/journal.pone.0214283.

47. Mai VQ, Giang KB, Minh HV, Lindholm L, Sun S, Sahlen KG. Reference data among general population and known-groups validity among hypertensive population of the EQ-5D-5L in Vietnam. Qual Life Res. 2022;31:539–550. doi: 10.1007/s11136-021-02959-2.

48. Nguyen LH, Tran BX, Le Hoang QN, Tran TT, Latkin CA. Quality of life profile of general Vietnamese population using EQ-5D-5L. Health Qual Life Outcomes. 2017;15(1):199. doi: 10.1186/s12955-017-0771-0.

49. Bailey H, Kind P. Preliminary findings of an investigation into the relationship between national culture and EQ-5D value sets. Qual Life Res. 2010;19:1145–1154. doi: 10.1007/s11136-010-9678-5.

50. Casadei G, Tolley K, Bettio M, Bozza F, Cafaro A, Dall’Ara MC, et al. Investigation of health-related quality of life outcomes in cancer patients: findings from an observational study using the EQ-5D in Italy. SN Compr Clin Med. 2020;2:1579–1584. doi: 10.1007/s42399-020-00449-z.

51. Scalone L, Cortesi PA, Ciampichini R, Belisari A, D’Angiolella LS, Cesana G, et al. Italian population-based values of EQ-5D health states. Value Health. 2013;16(5):814–822. doi: 10.1016/j.jval.2013.04.008.

52. Scalone L, Cortesi PA, Ciampichini R, Cesana G, Mantovani LG. Health Related Quality of Life norm data of the general population in Italy: results using the EQ-5D-3L and EQ-5D-5L instruments. Epidemiol Biostat Public Health. 2015;12(3):e11457-1–e11457-15.

53. Varma P, Junge M, Meaklim H, Jackson ML. Younger people are more vulnerable to stress, anxiety, and depression during COVID-19 pandemic: a global cross-sectional survey. Prog Neuropsychopharmacol Biol Psychiatry. 2021;109:110236. doi: 10.1016/j.pnpbp.2020.110236.

54. Sabbadini LL. Dipartimento per le statistiche sociali e ambientali (ISTAT). Il lavoro femminile in tempo di crisi. CNEL II° Commissione – Stati generali sul lavoro delle donne in Italia. Rome; 2 February 2012. https://www.istat.it/it/files/2012/03/Il-lavoro-femminile-in-tempo-di-crisi.ppt. Accessed 25 Jul 2021.

55. Long D, Polinder S, Bonsel GJ, Haagsma JA. Test-retest reliability of the EQ-5D-5L and the reworded QOLIBRI-OS in the general population of Italy, the Netherlands, and the United Kingdom. Qual Life Res. 2021;30(10):2961–2971. doi: 10.1007/s11136-021-02893-3.

56. Jiang R, Shaw J, Mühlbacher A, Lee TA, Walton S, Kohlmann T, et al. Comparison of online and face-to-face valuation of the EQ-5D-5L using composite time trade-off. Qual Life Res. 2021;30:1433–1444. doi: 10.1007/s11136-020-02712-1.

57. Devlin N, Parkin D, Janssen B. Methods for analysing and reporting EQ-5D data. Cham: Springer; 2020.

58. Long D, Haagsma JA, Janssen MF, Yfantopoulos JN, Lubetkin EI, Bonsel GJ. Health-related quality of life and mental well-being of healthy and diseased persons in 8 countries: does stringency of government response against early COVID-19 matter? SSM Popul Health. 2021;15:100913. doi: 10.1016/j.ssmph.2021.100913.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 47 kb)

</div>

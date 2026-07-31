---
project_id: "2021-RA"
work_id: "doi:10.1007/s40258-023-00798-5"
doi: "10.1007/s40258-023-00798-5"
pmid: "36964853"
pmcid: "PMC10039326"
title: "Measurement of Health-Related Quality of Life from Conception to Postpartum Using the EQ-5D-5L Among a National Sample of US Pregnant and Postpartum Adults"
journal: "Applied Health Economics and Health Policy"
publication_date: "2023-03-25"
volume: "21"
issue: "3"
authors:
  - name: "Annette K. Regan"
    orcid: "http://orcid.org/0000-0002-3879-6193"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Pallavi Aytha Swathi"
    affiliation_ids:
      - "Aff3"
      - "Aff4"
  - name: "Marcianna Nosek"
    affiliation_ids:
      - "Aff1"
  - name: "Ning Yan Gu"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.267103.10000 0004 0461 8879School of Nursing and Health Professions, University of San Francisco, San Francisco, CA USA"
  - id: "Aff2"
    name: "grid.19006.3e0000 0000 9632 6718Fielding School of Public Health, University of California Los Angeles, Los Angeles, CA USA"
  - id: "Aff3"
    name: "grid.241116.10000000107903411School of Medicine, University of Colorado, Denver, CO USA"
  - id: "Aff4"
    name: "grid.267103.10000 0004 0461 8879College Arts and Sciences, University of San Francisco, San Francisco, CA USA"
licence: "cc-by-nc"
source_file: "input/projects/2021-RA/papers/doi_10.1007_s40258-023-00798-5.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10039326/fullTextXML"
source_method: "epmc_xml"
source_sha256: "1dea935df539601911206d823932ef202c4ebdf189ceea7dd81fab99bf2a747b"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Measurement of Health-Related Quality of Life from Conception to Postpartum Using the EQ-5D-5L Among a National Sample of US Pregnant and Postpartum Adults

## Abstract

### Background

During pregnancy, physiological changes occur from conception to birth. We assessed the health-related quality of life (HRQoL) throughout pregnancy and postpartum using the EQ-5D-5L.

### Methods

Between May and July 2021 (wave 1) and December 2021 and April 2022 (wave 2), we conducted a series of cross-sectional, national online surveys of 5250 pregnant and postpartum United States (US) adults. The survey included the EQ-5D-5L, EQ visual analog scale (EQ VAS), items measuring respondents’ sociodemographic and health information, last menstrual period, estimated date of delivery, and date of pregnancy end (if postpartum). We examined monthly EQ-5D-5L items, utility values, and EQ VAS scores during pregnancy and postpartum. We used quantile regression adjusted for calendar month of last menstrual period to estimate changes in HRQoL at different time points of pregnancy and postpartum.

### Results

There was a steady increase in the frequency of respondents reporting health-related problems and a decline in EQ-5D-5L utility values from early pregnancy until the ninth month of pregnancy (*β* = − 0.21; standard error \[SE\] 0.02; *P* \< 0.001), followed by a 0.10 (SE 0.02; *P* \< 0.001) unit increase in values during the first postpartum month and a stabilization during the remainder of the postpartum period (*β* = 0.02; SE 0.02; *P* = 0.214). The median EQ-5D-5L utility value was lowest during the ninth month of pregnancy (median 0.78 \[interquartile range 0.30\]).

### Conclusions

HRQoL as measured by EQ-5D-5L varies across pregnancy, indicating progressive declines throughout pregnancy and a return to first trimester values during the first month postpartum. Studies involving HRQoL measurement in pregnant people should account for the stage of pregnancy in their estimates.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40258-023-00798-5.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| Self-reported health-related quality of life (HRQoL) fluctuates during pregnancy and postpartum, with the proportion of individuals reporting problems with pain and discomfort, engaging in usual activities, and mobility increasing throughout pregnancy. |
| Measures of HRQoL were lowest during the ninth month of pregnancy and improved within 1 month postpartum. |
| Given these observed trends, evaluations of HRQoL during pregnancy should account for the stage of pregnancy at the time of assessment. |

</div>

## Introduction

During pregnancy, multi-factored physiological, mental, and social functional changes occur from conception to birth and through the postpartum period. Understanding the impact of pregnancy on the health-related quality of life (HRQoL) of pregnant people throughout the pregnancy journey is imperative for providing effective care for this unique cohort. At the same time, despite ubiquitous applications of the EuroQol EQ-5D-5L in assessing HRQoL in different populations and disease cohorts around the world, there remains a gap of understanding in the utilization of the EQ-5D-5L in pregnant people in the US.

A recent study by Wu et al. (2021) measured the HRQoL of pregnant people in China using the EQ-5D-5L and reported a bell-shaped HRQoL curve during the three trimesters, suggesting that HRQoL improves through the second trimester, where it peaks, and then declines during the third trimester until delivery \[1\]. There has been some application of the EQ-5D-5L in pregnant people with different diseases, for example, pregnant people with HIV in China \[2\], with uterine fibroids in China \[3\], or with depression in England \[4\]. These recent applications have highlighted the importance of gaining a greater appreciation of the HRQoL in pregnancy.

To date, there remains a limited understanding of HRQoL measurement during pregnancy and how measures like the EQ-5D-5L perform in pregnant people in the United States (US). This study aims to assess HRQoL throughout pregnancy and postpartum in a US national pregnant cohort using the EQ-5D-5L instrument.

## Methods

### Study Design and Data Collection

Between May and July 2021 (wave 1) and December 2021 and April 2022 (wave 2), we conducted a series of cross-sectional, national online surveys of pregnant and postpartum adults residing in the US. We used intercept recruitment on social media sites, including Facebook, Instagram, and Twitter, to advertise our survey to currently pregnant and recently pregnant (postpartum) adults. Eligible participants included adults who (1) were 18–49 years old, (2) were residing in the US or a US territory, (3) had a pregnancy ending after March 2020, and (4) completed the survey either during pregnancy or within 9 months after delivery. The survey could be taken in English or Spanish and could be completed over multiple sessions (but could only be submitted once).

Following informed consent, participants were asked to complete a 30-min online survey, which included the EQ-5D-5L instrument with the EQ visual analog scale (EQ VAS) \[5\], the Patient Health Questionnaire-4 (PHQ-4) \[6\], the Generalized Anxiety Disorder-7 questionnaire (GAD-7) \[7\], and survey items on sociodemographic information, diagnosed medical conditions (including asthma, type 1 or type 2 diabetes, coronary heart disease, essential hypertension, or depression), and obstetric factors (Table S1, see the electronic supplementary material). Respondents who were pregnant at the time of survey provided information on their last menstrual period (LMP). In combination with the survey date, self-reported LMP was used to estimate the month of pregnancy at the time of survey (pregnancy months = \[survey date − LMP\]/30). Where LMP was missing, we used the self-reported expected date of delivery to estimate LMP. Respondents who were recently pregnant (postpartum) at the time of survey were asked to provide information on the date of delivery or pregnancy end. In combination with the survey date, we used this information to estimate the number of postpartum months at the time of survey (postpartum month = \[survey date−date of pregnancy end\]/30).

HRQoL was measured using the EQ-5D-5L and the EQ VAS \[5\]. The EQ-5D-5L is a standardized instrument used to assess an individual’s health status across five dimensions describing health in terms of mobility, self-care, usual activities, pain/discomfort, and anxiety/depression \[5, 8\]. Respondents were asked to rate each dimension using a five-point Likert scale, as having (1) no problems, (2) slight problems, (3) moderate problems, (4) severe problems, and (5) extreme problems. To provide a preference-based measure of health status, utility values derived from a US-based value set for the adult population were assigned based on responses to the five items \[8, 9\]. In addition to five-item responses and EQ-5D-5L utility values, respondents were asked to rate their overall health status ‘today’ (i.e., on the day taking the survey) using a visual analog scale (VAS, or EQ VAS). The EQ VAS scores ranged from 0 (the worst health imagined) to 100 (the best health imagined). EQ-5D-5L utility values and EQ VAS scores were analyzed as non-parametric continuous variables. Separately for the five EQ-5D-5L items, we estimated the percentage of respondents reporting any problems on each item.

### Statistical Analysis

To examine HRQoL as measured by the EQ-5D-5L across gestational age through the postpartum period, we evaluated the proportion of respondents experiencing problems with mobility, self-care, usual activities, pain or discomfort, or anxiety or depression for each month of pregnancy and postpartum. We examined the distribution of EQ-5D-5L utility values and EQ VAS scores by month of pregnancy and postpartum. We additionally evaluated ceiling and floor effects for EQ-5D-5L item responses and EQ VAS, by estimating the proportion of respondents who reported maximum values (ceiling effects; the ‘11111’ health state on the EQ-5D-5L or 100 on the EQ VAS) and the proportion of respondents who reported minimum values (floor effects; the ‘55555’ health state on the EQ-5D-5L or 0 on the EQ VAS).

We examined EQ-5D-5L and EQ VAS scores among groups of pregnant people where HRQoL may reasonably differ, including those with at least one self-reported pre-existing medical condition and those with severe problems with anxiety and/or depression (as measured by the PHQ-4 and GAD-7).

We used quantile regression to model EQ-5D-5L utility values and EQ VAS scores as a function of month of pregnancy or postpartum (fit as a cubic spline). To adjust for the potential influence of calendar time, models additionally controlled for the calendar month of LMP. For validation, we performed analyses separately by wave of data collection. Because data were collected during different stages of the coronavirus disease 2019 (COVID-19) pandemic, we performed additional comparisons by quarter and year of conception of the pregnancy in order to evaluate the potential influence of calendar time on our results.

### Ethical Review and Approval

The study protocol was reviewed and approved by the University of San Francisco Institutional Review Board.

## Results

Of the 12,733 individuals who responded to the survey invitation, 6661 (52.3%) US adults 18–49 years old who were either pregnant at the time of survey or recently pregnant (i.e., had a pregnancy ending within 12 months of survey) completed the survey. Of these, nine (1.4%) did not complete all EQ-5D-5L items and 1402 (21.0%) did not provide sufficient information to determine when in relation to pregnancy the survey was completed or completed the survey \> 9 months after delivery. These respondents were excluded from further analysis, leaving 5250 (78.8%) respondents in the final analytic dataset (pregnant at the time of survey *n* = 3618; recently pregnant *n* = 1632). Among respondents, 72.1% were ≥ 30 years old, 15.6% were Latina/x, 2.3% Black, and 78.6% were white; 86.4% resided in a metropolitan area, 86.2% were in a partnership, 13.8% were born overseas, and 92.2% identified as heterosexual (Table <a href="#Tab1" data-ref-type="table">1</a>). In addition, 14.3% of respondents had a pre-existing health condition prior to pregnancy and 18.8% were diagnosed with a pregnancy complication.

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of survey participants (*n* = 5250), overall and by study wave—United States, May 2021–April 2022

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristic</th>
<th style="text-align: left;">US population (2016–2020)*, (%)</th>
<th style="text-align: left;">Total (<em>n</em> = 5250), <em>n</em> (%)</th>
<th style="text-align: left;">Wave 1: May–Jul. 2021 (<em>n</em> = 2458), <em>n</em> (%)</th>
<th style="text-align: left;">Wave 2: Dec. 2021–Apr. 2022 (<em>n</em> = 2792), <em>n</em> (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;">Maternal age</td>
</tr>
<tr>
<td style="text-align: left;"> 18–24 years</td>
<td style="text-align: left;">22.0%</td>
<td>417 (7.9%)</td>
<td>340 (13.8%)</td>
<td>77 (2.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> 24–29 years</td>
<td style="text-align: left;">28.7%</td>
<td>1049 (20.0%)</td>
<td>678 (27.6%)</td>
<td>371 (13.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> 30–34 years</td>
<td style="text-align: left;">29.9%</td>
<td>1892 (36.0%)</td>
<td>784 (31.9%)</td>
<td>1108 (39.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> 35–39 years</td>
<td style="text-align: left;">15.8%</td>
<td>1527 (29.1%)</td>
<td>538 (21.9%)</td>
<td>989 (35.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 40 years</td>
<td style="text-align: left;">3.6%</td>
<td>365 (7.0%)</td>
<td>118 (4.8%)</td>
<td>247 (8.8%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Maternal race/ethnicity</td>
</tr>
<tr>
<td style="text-align: left;"> Latina/x or Hispanic</td>
<td style="text-align: left;">24.2%</td>
<td>817 (15.6%)</td>
<td>281 (11.4%)</td>
<td>536 (19.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Black</td>
<td style="text-align: left;">14.8%</td>
<td>121 (2.3%)</td>
<td>96 (3.9%)</td>
<td>25 (0.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> White</td>
<td style="text-align: left;">51.5%</td>
<td>4128 (78.6%)</td>
<td>1977 (80.4%)</td>
<td>2.151 (77.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> Asian</td>
<td style="text-align: left;">6.1%</td>
<td>151 (2.9%)</td>
<td>79 (3.2%)</td>
<td>72 (2.6%)</td>
</tr>
<tr>
<td style="text-align: left;"> American Indian, Alaskan Native, or Pacific Islander</td>
<td style="text-align: left;">1.0%</td>
<td>22 (0.5%)</td>
<td>16 (0.6%)</td>
<td>6 (0.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Multiple races</td>
<td style="text-align: left;">2.3%</td>
<td>11 (0.2%)</td>
<td>9 (0.4%)</td>
<td>2 (0.1%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Educational attainment</td>
</tr>
<tr>
<td style="text-align: left;"> ≤ High school</td>
<td style="text-align: left;">38.4%</td>
<td>489 (9.3%)</td>
<td>246 (10.0%)</td>
<td>243 (8.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> Some college</td>
<td style="text-align: left;">27.6%</td>
<td>794 (15.1%)</td>
<td>412 (16.8%)</td>
<td>382 (13.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> College graduate</td>
<td style="text-align: left;">21.1%</td>
<td>1810 (34.5%)</td>
<td>878 (35.7%)</td>
<td>932 (33.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> Graduate degree</td>
<td style="text-align: left;">12.8%</td>
<td>2157 (41.1%)</td>
<td>922 (37.5%)</td>
<td>1235 (44.2%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Region of residence</td>
</tr>
<tr>
<td style="text-align: left;"> Midwest</td>
<td style="text-align: left;">20.9%</td>
<td>1342 (25.6%)</td>
<td>623 (25.3%)</td>
<td>719 (25.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> Northeast</td>
<td style="text-align: left;">15.9%</td>
<td>1008 (19.2%)</td>
<td>342 (13.9%)</td>
<td>666 (23.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> South</td>
<td style="text-align: left;">39.7%</td>
<td>1768 (33.7%)</td>
<td>921 (37.5%)</td>
<td>847 (30.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> West</td>
<td style="text-align: left;">23.4%</td>
<td>1121 (21.4%)</td>
<td>568 (23.1%)</td>
<td>553 (19.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> US territory</td>
<td style="text-align: left;">–</td>
<td>11 (0.2%)</td>
<td>4 (0.2%)</td>
<td>7 (0.3%)</td>
</tr>
<tr>
<td style="text-align: left;">Metropolitan residence</td>
<td style="text-align: left;">86.4%</td>
<td>4526 (86.2%)</td>
<td>2058 (83.7%)</td>
<td>2468 (88.4%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Employed</td>
</tr>
<tr>
<td style="text-align: left;"> Employed</td>
<td style="text-align: left;">–</td>
<td>3454 (65.8%)</td>
<td>1666 (67.8%)</td>
<td>1788 (64.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> Maternity leave</td>
<td style="text-align: left;">–</td>
<td>473 (9.0%)</td>
<td>153 (6.2%)</td>
<td>320 (11.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed</td>
<td style="text-align: left;">–</td>
<td>1323 (25.2%)</td>
<td>639 (26.0%)</td>
<td>684 (24.5%)</td>
</tr>
<tr>
<td style="text-align: left;">Insured<sup>†</sup></td>
<td style="text-align: left;">–</td>
<td>4638 (97.4%)</td>
<td>2392 (97.7%)</td>
<td>2246(97.0%)</td>
</tr>
<tr>
<td style="text-align: left;">Married or in a partnership</td>
<td style="text-align: left;">–</td>
<td>4524 (86.2%)</td>
<td>2136 (86.9%)</td>
<td>2388 (85.5%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Sexual orientation<sup>†</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Homosexual/gay</td>
<td style="text-align: left;">–</td>
<td>46 (0.9%)</td>
<td>17 (0.7%)</td>
<td>29 (1.1%)</td>
</tr>
<tr>
<td style="text-align: left;"> Bisexual</td>
<td style="text-align: left;">–</td>
<td>302 (5.8%)</td>
<td>171 (7.1%)</td>
<td>13 (4.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> Heterosexual</td>
<td style="text-align: left;">–</td>
<td>4751 (92.2%)</td>
<td>2199 (90.8%)</td>
<td>2552 (93.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> Something else</td>
<td style="text-align: left;">–</td>
<td>56 (1.1%)</td>
<td>34 (1.4%)</td>
<td>22 (0.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Born overseas</td>
<td style="text-align: left;">21.2%</td>
<td>725 (13.8%)</td>
<td>247 (10.0%)</td>
<td>478 (17.1%)</td>
</tr>
<tr>
<td style="text-align: left;">Pre-existing health condition</td>
<td style="text-align: left;">–</td>
<td>751 (14.3%)</td>
<td>367 (14.9%)</td>
<td>384 (13.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Diagnosed pregnancy complication</td>
<td style="text-align: left;">–</td>
<td>985 (18.8%)</td>
<td>438 (17.8%)</td>
<td>547 (19.6%)</td>
</tr>
<tr>
<td style="text-align: left;">Intended pregnancy</td>
<td style="text-align: left;">–</td>
<td>3786 (72.1%)</td>
<td>1756 (71.4%)</td>
<td>2030 (72.7%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Parity</td>
</tr>
<tr>
<td style="text-align: left;"> 0</td>
<td style="text-align: left;">38.8%</td>
<td>1508 (28.7%)</td>
<td>544 (22.1%)</td>
<td>964 (34.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">31.6%</td>
<td>2089 (39.8%)</td>
<td>1036 (42.1%)</td>
<td>1053 (37.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 2</td>
<td style="text-align: left;">29.6%</td>
<td>1653 (31.5%)</td>
<td>878 (35.7%)</td>
<td>775 (27.8%)</td>
</tr>
</tbody>
</table>

\*Centers for Disease Control and Prevention, National Center for Health Statistics, National Vital Statistics System, Natality on CDC WONDER Online Database. Data are from the Natality Records 2016–2020, as compiled from data provided by the 57 vital statistics jurisdictions through the Vital Statistics Cooperative Program. Accessed at <http://wonder.cdc.gov/natality-expanded-current.html> on Jun 17, 2022 4:46:17 PM

<sup>†</sup>Data were missing on insurance status for 488 respondents and on sexual orientation for 95 respondents

</div>

Based on EQ-5D-5L item measures, problems with anxiety/depression were most common among pregnant and postpartum participants (60.6%), followed by problems with pain or discomfort (59.9%); problems with self-care (11.6%) were least commonly reported. With the exception of problems with anxiety and depression, which remained consistent and above 50% throughout pregnancy and postpartum, problems with mobility, self-care, usual activities, and pain and discomfort appeared to increase throughout pregnancy until the ninth month (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). This was followed by an immediate decline during the first month postpartum and a return to a similar (or lower) level as first trimester by the ninth month postpartum.

<figure id="Fig1">
<p><img src="40258_2023_798_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Percentage of participants reporting problems with mobility, self-care, engaging in usual activities, pain or discomfort, and anxiety and depression (EQ-5D-5L), by the month of pregnancy (P) or postpartum (PP) at the time of survey—United States, May 2021 to April 2022</figcaption>
</figure>

Median EQ-5D-5L utility values were lowest during the ninth month of pregnancy (median 0.78; interquartile range \[IQR\] 0.30) and were highest during the ninth month postpartum (median 0.94; IQR 0.07) (Fig. <a href="#Fig2" data-ref-type="fig">2</a>, Table <a href="#Tab2" data-ref-type="table">2</a>). There was a steady decline in EQ-5D-5L utility values until the ninth month of pregnancy (*β* = − 0.21; standard error \[SE\] 0.02; *P* \< 0.001), followed by a 0.10 (SE 0.02; *P* \< 0.001) unit increase in values during the first postpartum month and a stabilization during the rest of the postpartum period (*β* = 0.02; SE 0.02; *P* = 0.214) (Fig. S1, see the electronic supplementary material). In contrast to EQ-5D-5L utility values, we observed little variability in EQ VAS scores by month of pregnancy or postpartum, and no significant difference through the ninth month of pregnancy (*β* = − 1.1; SE 2.1; *P* = 0.59), during the first postpartum month (*β* = 0.02; SE 0.02; *P* = 0.54), or throughout the postpartum period (*β* = 1.1; SE = 1.4; *P* = 0.41) for EQ-5D-5L VAS scores. In general, EQ-5D-5L utility values and EQ VAS scores were similar across survey waves (Fig. S2), with slightly lower values during the ninth month of pregnancy for wave 1 participants compared to wave 2.

<figure id="Fig2">
<p><img src="40258_2023_798_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Distribution of EQ-5D-5L utility values (<strong>a</strong>) and EQ VAS scores (<strong>b</strong>), by the month of pregnancy (P) or postpartum (PP) at the time of survey—United States, May 2021 to April 2022. <em>VAS</em> visual analog scale</figcaption>
</figure>

<div id="Tab2" class="table-wrap">

<div class="caption">

EQ-5D-5L and EQ VAS measurements among US pregnant people (*n* = 5250), by month of pregnancy or postpartum at the time of survey—United States, May 2021 to April 2022

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Month of pregnancy/postpartum at time of survey</th>
<th rowspan="2" style="text-align: left;">Total, <em>N</em></th>
<th colspan="2" style="text-align: left;">Range (min, max)</th>
<th colspan="2" style="text-align: left;">Median (IQR)</th>
<th colspan="2" style="text-align: left;">Ceiling effects*, <em>n</em> (%)</th>
<th colspan="2" style="text-align: left;">Floor effects<sup>†</sup>, <em>n</em> (%)</th>
</tr>
<tr>
<th style="text-align: left;">EQ-5D-5L utility</th>
<th style="text-align: left;">EQ VAS</th>
<th style="text-align: left;">EQ-5D-5L</th>
<th style="text-align: left;">EQ VAS</th>
<th style="text-align: left;">EQ-5D-5L<br />
[11111]</th>
<th style="text-align: left;">EQ VAS<br />
[100]</th>
<th style="text-align: left;">EQ-5D-5L<br />
[55555]</th>
<th style="text-align: left;">EQ VAS<br />
[0]</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pregnancy 1 m</td>
<td style="text-align: left;">264</td>
<td style="text-align: left;">− 0.24, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.88 (0.13)</td>
<td>80 (20)</td>
<td>45 (17.0%)</td>
<td>7 (2.7%)</td>
<td>0 (0%)</td>
<td>4 (1.5%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 2 m</td>
<td style="text-align: left;">263</td>
<td style="text-align: left;">− 0.21, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.88 (0.13)</td>
<td>80 (18)</td>
<td>64 (24.3%)</td>
<td>7 (2.7%)</td>
<td>0 (0%)</td>
<td>1 (0.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 3 m</td>
<td style="text-align: left;">312</td>
<td style="text-align: left;">− 0.38, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.88 (0.13)</td>
<td>80 (18)</td>
<td>65 (20.8%)</td>
<td>8 (2.6%)</td>
<td>0 (0%)</td>
<td>6 (1.9%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 4 m</td>
<td style="text-align: left;">417</td>
<td style="text-align: left;">− 0.43, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.88 (0.13)</td>
<td>81 (15)</td>
<td>63 (15.1%)</td>
<td>13 (3.1%)</td>
<td>0 (0%)</td>
<td>6 (1.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 5 m</td>
<td style="text-align: left;">497</td>
<td style="text-align: left;">− 0.10, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.88 (0.16)</td>
<td>80 (16)</td>
<td>75 (15.1%)</td>
<td>13 (2.6%)</td>
<td>0 (0%)</td>
<td>6 (1.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 6 m</td>
<td style="text-align: left;">567</td>
<td style="text-align: left;">− 0.31, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.85 (0.21)</td>
<td>80 (20)</td>
<td>61 (10.8%)</td>
<td>11 (1.9%)</td>
<td>0 (0%)</td>
<td>5 (0.9%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 7 m</td>
<td style="text-align: left;">618</td>
<td style="text-align: left;">− 0.28, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.81 (0.22)</td>
<td>80 (20)</td>
<td>66 (10.7%)</td>
<td>14 (2.3%)</td>
<td>0 (0%)</td>
<td>7 (1.1%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 8 m</td>
<td style="text-align: left;">561</td>
<td style="text-align: left;">− 0.11, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.81 (0.25)</td>
<td>81 (18)</td>
<td>56 (10.0%)</td>
<td>13 (2.3%)</td>
<td>0 (0%)</td>
<td>4 (0.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Pregnancy 9 m</td>
<td style="text-align: left;">119</td>
<td style="text-align: left;">− 0.24, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.78 (0.30)</td>
<td>80 (18)</td>
<td>12 (10.1%)</td>
<td>1 (0.8%)</td>
<td>0 (0%)</td>
<td>2 (1.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 1 m</td>
<td style="text-align: left;">217</td>
<td style="text-align: left;">0.09, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.94 (0.13)</td>
<td>80 (16)</td>
<td>48 (22.1%)</td>
<td>6 (2.8%)</td>
<td>0 (0%)</td>
<td>3 (1.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 2 m</td>
<td style="text-align: left;">188</td>
<td style="text-align: left;">0.32, 1</td>
<td style="text-align: left;">5, 100</td>
<td>0.94 (0.13)</td>
<td>81 (15)</td>
<td>70 (37.2%)</td>
<td>8 (4.3%)</td>
<td>0 (0%)</td>
<td>0 (0%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 3 m</td>
<td style="text-align: left;">249</td>
<td style="text-align: left;">0.50, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.94 (0.12)</td>
<td>80 (14)</td>
<td>73 (29.3%)</td>
<td>6 (2.4%)</td>
<td>0 (0%)</td>
<td>4 (1.6%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 4 m</td>
<td style="text-align: left;">224</td>
<td style="text-align: left;">0.09, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.94 (0.12)</td>
<td>80 (19)</td>
<td>66 (29.5%)</td>
<td>3 (1.3%)</td>
<td>0 (0%)</td>
<td>4 (1.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 5 m</td>
<td style="text-align: left;">216</td>
<td style="text-align: left;">0.20, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.94 (0.12)</td>
<td>81 (15)</td>
<td>68 (31.5%)</td>
<td>8 (3.7%)</td>
<td>0 (0%)</td>
<td>2 (0.9%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 6 m</td>
<td style="text-align: left;">157</td>
<td style="text-align: left;">0.14, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.91 (0.07)</td>
<td>81 (15)</td>
<td>37 (23.6%)</td>
<td>3 (1.9%)</td>
<td>0 (0%)</td>
<td>1 (0.6%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 7 m</td>
<td style="text-align: left;">152</td>
<td style="text-align: left;">0.41, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.94 (0.07)</td>
<td>81 (15)</td>
<td>37 (24.3%)</td>
<td>4 (2.6%)</td>
<td>0 (0%)</td>
<td>1 (0.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 8 m</td>
<td style="text-align: left;">127</td>
<td style="text-align: left;">0.51, 1</td>
<td style="text-align: left;">30, 100</td>
<td>0.94 (0.12)</td>
<td>80 (11)</td>
<td>39 (30.7%)</td>
<td>3 (2.4%)</td>
<td>0 (0%)</td>
<td>0 (0%)</td>
</tr>
<tr>
<td style="text-align: left;">Postpartum 9 m</td>
<td style="text-align: left;">102</td>
<td style="text-align: left;">0.53, 1</td>
<td style="text-align: left;">35, 100</td>
<td>0.94 (0.07)</td>
<td>80 (17)</td>
<td>22 (21.6%)</td>
<td>3 (2.9%)</td>
<td>0 (0%)</td>
<td>0 (0%)</td>
</tr>
<tr>
<td style="text-align: left;">Total</td>
<td style="text-align: left;">5250</td>
<td style="text-align: left;">− 0.43, 1</td>
<td style="text-align: left;">0, 100</td>
<td>0.88 (0.16)</td>
<td>80 (18)</td>
<td>967 (18.4%)</td>
<td>131 (2.5%)</td>
<td>0 (0%)</td>
<td>56 (1.1%)</td>
</tr>
</tbody>
</table>

*IQR* interquartile range, *VAS* visual analog scale

\*Ceiling effects assessed the percentage of respondents who reported all maximum health state values (i.e., 11111) on the EQ-5D-5L and EQ VAS (VAS 100).

<sup>†</sup>Floor effects assessed the percentage of respondents who reported all minimum health state values (i.e., 55555) on the EQ-5D-5L and EQ VAS (VAS 0). No floor effects were observed for EQ-5D-5L items

</div>

Ceiling effects for the EQ-5D-5L were more common during the postpartum period, with 22.1% of respondents reporting no problems related to any of the EQ-5D-5L items during the first postpartum month compared to 17.0% during the first month of pregnancy (Table <a href="#Tab2" data-ref-type="table">2</a>). We observed no real pattern in floor or ceiling effects for the EQ VAS, and no respondent reported floor effects for the EQ-5D-5L (i.e., no respondent reported the ‘55555’ health state on the EQ-5D-5L).

The proportion of participants reporting problems with mobility, self-care, usual care, pain or discomfort, or anxiety or depression was in general higher for pregnant people with pre-existing health conditions than for those without pre-existing conditions. However, EQ-5D-5L utility values and EQ VAS values were similar (Table <a href="#Tab3" data-ref-type="table">3</a>). We observed a dose–response decline in EQ-5D-5L utility values and EQ VAS scores and a dose–response increase in the proportion of respondents reporting problems with mobility, self-care, usual care, pain or discomfort, or anxiety or depression as the severity of problems with anxiety and depression increased (as measured by the PHQ-4 and GAD-7) (Table <a href="#Tab3" data-ref-type="table">3</a>).

<div id="Tab3" class="table-wrap">

<div class="caption">

EQ-5D-5L and EQ VAS measurements among pregnant people (*n* = 5250), by pre-existing health conditions and problems with anxiety and/or depression—United States, May 2021 to April 2022

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">EQ-5D-5L measurement</th>
<th colspan="2" style="text-align: left;">Pre-existing health conditions</th>
<th colspan="4" style="text-align: left;">PHQ-4 category</th>
<th colspan="4" style="text-align: left;">GAD-7 category</th>
</tr>
<tr>
<th style="text-align: left;">Any health condition (<em>n</em> = 751)</th>
<th style="text-align: left;">No health conditions (<em>n</em> = 4499)</th>
<th style="text-align: left;">Minimal problems with anxiety and/or depression (<em>n</em> = 3159)</th>
<th style="text-align: left;">Mild problems with anxiety and/or depression (<em>n</em> = 1494)</th>
<th style="text-align: left;">Moderate problems with anxiety and/or depression (<em>n</em> = 438)</th>
<th style="text-align: left;">Severe problems with anxiety and/or depression (<em>n</em> = 158)</th>
<th style="text-align: left;">Minimal anxiety symptoms (<em>n</em> = 2603)</th>
<th style="text-align: left;">Mild anxiety symptoms (<em>n</em> = 1871)</th>
<th style="text-align: left;">Moderate anxiety symptoms (<em>n</em> = 537)</th>
<th style="text-align: left;">Severe anxiety symptoms (<em>n</em> = 239)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11" style="text-align: left;">Any problems with…</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility</td>
<td>172 (22.9%)</td>
<td>722 (16.0%)</td>
<td>375 (11.9%)</td>
<td>334 (22.4%)</td>
<td>136 (31.1%)</td>
<td>49 (31.0%)</td>
<td>284 (10.9%)</td>
<td>358 (19.1%)</td>
<td>184 (34.3%)</td>
<td>68 (28.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care</td>
<td>117 (15.6%)</td>
<td>442 (9.8%)</td>
<td>216 (6.8%)</td>
<td>193 (12.9%)</td>
<td>109 (24.9%)</td>
<td>41 (25.9%)</td>
<td>158 (6.1%)</td>
<td>218 (11.7%)</td>
<td>120 (22.3%)</td>
<td>63 (26.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual care</td>
<td>329 (43.8%)</td>
<td>1548 (34.4%)</td>
<td>860 (27.2%)</td>
<td>677 (45.3%)</td>
<td>237 (54.1%)</td>
<td>102 (64.6%)</td>
<td>678 (26.0%)</td>
<td>777 (41.5%)</td>
<td>280 (52.1%)</td>
<td>142 (59.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain or discomfort</td>
<td>541 (72.0%)</td>
<td>2736 (60.8%)</td>
<td>1764 (55.8%)</td>
<td>1061 (71.0%)</td>
<td>331 (75.6%)</td>
<td>120 (75.9%)</td>
<td>1393 (53.5%)</td>
<td>1297 (69.3%)</td>
<td>395 (73.6%)</td>
<td>192 (80.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety or depression</td>
<td>515 (68.6%)</td>
<td>2629 (58.4%)</td>
<td>1251 (39.6%)</td>
<td>1314 (88.0%)</td>
<td>426 (97.3%)</td>
<td>153 (96.8%)</td>
<td>857 (32.9%)</td>
<td>1548 (82.7%)</td>
<td>504 (93.9%)</td>
<td>235 (98.3%)</td>
</tr>
<tr>
<td style="text-align: left;">Median EQ-5D-5L utility (IQR)</td>
<td>0.85 (0.22)</td>
<td>0.88 (0.16)</td>
<td>0.94 (0.13)</td>
<td>0.82 (0.16)</td>
<td>0.71 (0.25)</td>
<td>0.64 (0.31)</td>
<td>0.94 (0.13)</td>
<td>0.87 (0.19)</td>
<td>0.75 (0.28)</td>
<td>0.66 (0.32)</td>
</tr>
<tr>
<td style="text-align: left;">Median EQ VAS (IQR)</td>
<td>80 (17)</td>
<td>81 (17)</td>
<td>84 (14)</td>
<td>80 (17)</td>
<td>74 (24)</td>
<td>70 (30)</td>
<td>85 (12)</td>
<td>80 (17)</td>
<td>75 (23)</td>
<td>70 (21)</td>
</tr>
</tbody>
</table>

*GAD-7* Generalized Anxiety Disorder-7 questionnaire, *IQR* interquartile range, *PHQ-4* Patient Health Questionnaire-4, *VAS* visual analog scale

</div>

When we examined EQ-5D-5L utility values and EQ-5D-5L VAS scores by quarter (Q) and year of conception, we observed little variation (Fig. S3). The percentage of respondents reporting problems with pain/discomfort increased from 46.6% in Q2 of 2020 to 59.0% in Q3 of 2020, which may suggest that pregnancies coinciding with peak pandemic time periods reported more frequent health problems related to HRQoL and lower EQ-5D-5L values, regardless of month of pregnancy or postpartum (Fig. S4). However, these effects were not observed for problems with anxiety/depression and were less common for problems with mobility and self-care.

## Discussion

Based on data from this large, national US survey of pregnant and postpartum individuals, we observed variation across the five health items of the EQ-5D-5L at different gestational and postpartum time points. Pregnant people reported increasing health-related problems, such as pain/discomfort, throughout pregnancy, and the proportion of respondents reporting these problems peaked at the ninth (and final) month of pregnancy. The proportion of individuals reporting health-related problems declined during the postpartum period, although with considerable variability across individuals. In addition, the EQ-5D-5L was able to ascertain the HRQoL differences in different disease cohorts, including those with chronic medical problems (i.e., asthma, coronary heart disease) and pregnant people with severe anxiety and depression (as measured by the PHQ-4 or GAD-7). These findings suggest that HRQoL varies over the course of the pregnancy and postpartum period and these changes were detected using the EQ-5D-5L.

This observed pattern is similar to the pattern reported by Wu et al. \[1\], who reported a bell-shaped curve of EQ-5D-5L utilities among Chinese pregnant people. Unlike the results in our study, the EQ VAS scores reported by Wu et al. showed a wider range in scores correlated with trimester of pregnancy. We showed no association between EQ VAS scores and month of pregnancy or postpartum; however, it is important to note that we evaluated month of pregnancy rather than trimester—an important difference, which allowed us to more finely evaluate changes over time within each trimester of pregnancy.

Although anxiety and depression were the most common problems reported during pregnancy and postpartum, problems with anxiety and depression did not appear to drive changes in HRQoL by month of pregnancy or postpartum. Changes in HRQoL over time appeared to be predominantly driven by an increase in the frequency of self-reported problems with pain and discomfort and performing usual activities—with additional increases in mobility issues and problems with self-care. As pregnancy progresses and the fetus grows, so do the physiological demands on the pregnant individual. For example, by the third trimester, cardiac output has increased by 30–50%, tidal volume has increased by 40%, and blood volume has increased by 30–40% \[10\]. Pregnancy is also accompanied by weight gain, typically ranging from 20 to 50 pounds \[11\], which can present mobility issues. These physiological changes likely contribute to changes in health-related problems, which could induce fluctuations in HRQoL throughout pregnancy and postpartum.

Our study provides evidence on the usefulness of the EQ-5D-5L in a pregnant population. As such an application is relatively recent, based on the existing literature, the values reported herein could be used for future reference, but additional research with greater variation in race and socioeconomic status would still be useful. Without an understanding of HRQoL measurement around the time of pregnancy, it is challenging to perform valid evaluation of the impacts of environmental, medical, and individual-level factors, interventions, and events on maternal HRQoL. The ongoing COVID-19 pandemic serves as a recent example of clinical interest in monitoring HRQoL around the time of pregnancy. The global COVID-19 pandemic and the corresponding mitigation policies in different countries around the world imposed additional impacts on those who were either planning pregnancy, were already pregnant, or had recently given birth. Pregnant people are more likely than non-pregnant people to experience severe COVID-19, including higher rates of admission to intensive care units, requirement for invasive mechanical ventilation or extracorporeal membrane oxygenation, and death \[12–16\]. As a result, pregnant and recently pregnant people are considered a high-risk group for COVID-19 by the US Centers for Disease Control and Prevention (CDC) \[17\].

Previous studies have sought to evaluate the direct and indirect impacts of the pandemic on perinatal health. For example, researchers have evaluated the impact of COVID-19 illness \[18, 19\] and pandemic-related confinement on the lifestyle and psychological wellbeing of pregnant people \[20\], all using the EQ-5D-5L instrument. More recently, there has been interest in estimating the effect of adverse events following COVID-19 immunization during pregnancy \[21\].

### Strengths and Limitations

Our study draws from a large, national sample of pregnant and recently pregnant individuals, with representation from all US states and two US territories. In comparison to the US birth statistics, our sample was representative of pregnancies in terms of residence and other social factors, but under-represented certain minority groups, most notably Black pregnant people. This may limit the generalizability of our findings due to selection bias. Additional limitations include the fact that these data are observational and rely on self-reported information. Although previous web-based surveys have demonstrated that self-reported information on gestational age is highly valid \[22\], we cannot discount the potential influence of reporting and recall bias. Another limitation is in the cross-sectional nature of the data collection. Because we did not perform longitudinal follow-up of participants, we could not perform any retest and cannot make conclusions regarding test–retest reliability as a result. However, in this population, retest is challenging given the respondent will be at different stages of pregnancy and potentially different health states. Longitudinal follow-up would allow for evaluation of HRQoL trajectories within individuals as well as the responsiveness of HRQoL measures to health problems diagnosed during pregnancy (i.e., preeclampsia, gestational diabetes), and future research should consider this. Finally, it is difficult to disentangle how the pandemic may have influenced our findings, since the month of pregnancy/postpartum is also linked with calendar time. However, our findings are fairly consistent with the pre-pandemic literature \[1\], and we did not observe consistent correlations between pandemic and HRQoL, indicating it is more likely that our observed variations in HRQoL were due to gestational age rather than exposure to the COVID-19 pandemic.

## Conclusions

HRQoL, as measured by the EQ-5D-5L instrument, varies based on the gestational age of pregnant people and length of time since birth among postpartum adults. Studies involving HRQoL measurement in pregnant people should account for the stage of pregnancy in their estimates. Although our study was not originally intended to assess the psychometric performance of the EQ-5D-5L instrument, our results indicate that the EQ-5D-5L instrument may be a useful tool for monitoring HRQoL and detecting changes in HRQoL throughout pregnancy and postpartum. Although further research is needed, this information can be used to inform quality-of-life measurement among pregnant and recently pregnant adults in clinical and general population settings.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (PDF 398 kb)

</div>

### Acknowledgements

The authors would like to acknowledge the contributions made by study participants to this research.

### Declarations

#### Conflict of interest

The authors have no potential conflicts of interest to disclose.

#### Funding

This study received funding from the University of San Francisco and the EuroQol Research Foundation (260-2020-RA; 384-2021-RA). The views expressed by the authors do not necessarily reflect the views of the EuroQol Group.

#### Ethics approval

The study protocol was reviewed and approved by the University of San Francisco Institutional Review Board (# 1754).

#### Consent to participate

All participants received information related to the study and provided informed consent to participate prior to participating in the study.

#### Consent for publication (from patients/participants)

Participants were informed that non-identifiable information would be made publicly available through publication prior to providing informed consent.

#### Code availability

Analytic code used to conduct analyses in R can be made available upon request to the corresponding author.

#### Authors' contributions

AKR provided project oversight, obtained study funding, oversaw data collection, performed all analyses, and wrote the original draft of the manuscript. PAS coordinated data collection and cleaning. MN and NYG contributed to the development of the study protocol. All authors contributed to the revision of the study manuscript and reviewed and approved the final version.

#### Data availability

The authors do not have permission to share the data used to support the findings of this study; however, study data could be made available on request from the corresponding author. The data are not publicly available due to privacy and ethical restrictions.

## References

1. Wu H, Sun W, Chen H, Wu Y, Ding W, Liang S. Health-related quality of life in different trimesters during pregnancy. Health Qual Life Outcomes. 2021;19(1):182. doi:10.1186/s12955-021-01811-y

2. Wang X, Guo G, Zhou L, Zheng J, Liang X, Li Z. Health-related quality of life in pregnant women living with HIV: a comparison of EQ-5D and SF-12. Health Qual Life Outcomes. 2017;15(1):158. doi:10.1186/s12955-017-0731-8

3. Ming W-K, Wu H, Wu Y, Chen H, Meng T, Shen Y. Health-related quality of life in pregnancy with uterine fibroid: a cross-sectional study in China. Health Qual Life Outcomes. 2019;17(1):89. doi:10.1186/s12955-019-1153-6

4. Heslin M, Chua K-C, Trevillion K, Nath S, Howard LM, Byford S. Psychometric properties of the five-level EuroQoL-5 dimension and Short Form-6 dimension measures of health-related quality of life in a population of pregnant women with depression. BJPsych Open. 2019;5(6):e88. doi:10.1192/bjo.2019.71

5. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

6. Löwe B, Wahl I, Rose M, Spitzer C, Glaesmer H, Wingenfeld K. A 4-item measure of depression and anxiety: validation and standardization of the Patient Health Questionnaire-4 (PHQ-4) in the general population. J Affect Disord. 2010;122(1–2):86–95. doi:10.1016/j.jad.2009.06.019

7. Spitzer RL, Kroenke K, Williams JB, Löwe B. A brief measure for assessing generalized anxiety disorder: the GAD-7. Arch Intern Med. 2006;166(10):1092–1097. doi:10.1001/archinte.166.10.1092

8. Devlin N, Pickard S, Busschbach J, Devlin N, Roudijk B, Ludwig K. The development of the EQ-5D-5L and its value sets. Value sets for eq-5d-5l: a compendium, comparative review & user guide. 2022:1–12. Cham, Springer International Publishing.

9. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F. United States valuation of EQ-5D-5L health states using an international protocol. Value Health. 2019;22(8):931–941. doi:10.1016/j.jval.2019.02.009

10. Talbot L, Maclennan K. Physiology of pregnancy. Anaesthesia Intensive Care Med. 2016;17(7):341–345. doi:10.1016/j.mpaic.2016.04.010

11. CDC. Weight Gain During Pregnancy. 2022 (accessed 14 Dec 2022); https://www.cdc.gov/reproductivehealth/maternalinfanthealth/pregnancy-weight-gain.htm.

12. Delahoy MJ, Whitaker M, O'Halloran A, Chai SJ, Kirley PD, Alden N. Characteristics and maternal and birth outcomes of hospitalized pregnant women with laboratory-\confirmed COVID-19 - COVID-NET, 13 States, March 1-August 22, 2020. MMWR Morb Mortal Wkly Rep. 2020;69(38):1347–1354. doi:10.15585/mmwr.mm6938e1

13. Ellington S, Strid P, Tong VT, Woodworth K, Galang RR, Zambrano LD. Characteristics of women of reproductive age with laboratory-confirmed SARS-CoV-2 infection by pregnancy status—United States, January 22-June 7, 2020. MMWR Morb Mortal Wkly Rep. 2020;69(25):769–775. doi:10.15585/mmwr.mm6925a1

14. Allotey J, Stallings E, Bonet M, Yap M, Chatterjee S, Kew T. Clinical manifestations, risk factors, and maternal and perinatal outcomes of coronavirus disease 2019 in pregnancy: living systematic review and meta-analysis. BMJ. 2020;370:m3320. doi:10.1136/bmj.m3320

15. Kasehagen L, Byers P, Taylor K, Kittle T, Roberts C, Collier C. COVID-19-associated deaths after SARS-CoV-2 infection during pregnancy—Mississippi, March 1, 2020-October 6, 2021. MMWR Morb Mortal Wkly Rep. 2021;70(47):1646–1648. doi:10.15585/mmwr.mm7047e2

16. Zambrano LD, Ellington S, Strid P, Galang RR, Oduyebo T, Tong VT. Update: characteristics of symptomatic women of reproductive age with laboratory-confirmed SARS-CoV-2 infection by pregnancy status—United States, January 22-October 3, 2020. MMWR Morb Mortal Wkly Rep. 2020;69(44):1641–1647. doi:10.15585/mmwr.mm6944e3

17. Razzaghi H, Meghani M, Pingali C, Crane B, Naleway A, Weintraub E. COVID-19 vaccination coverage among pregnant women during pregnancy—eight integrated health care organizations, United States, December 14, 2020-May 8, 2021. MMWR Morb Mortal Wkly Rep. 2021;70(24):895–899. doi:10.15585/mmwr.mm7024e2

18. Alaya F, Worrall AP, O'Toole F, Doyle J, Duffy RM, Geary MP. Health-related quality of life and quality of care in pregnant and postnatal women during the coronavirus disease 2019 pandemic: a cohort study. Int J Gynaecol Obstet. 2021;154(1):100–105. doi:10.1002/ijgo.13711

19. Regan A, Aytha-Swathi P, Nosek M, Gu NY. P25 Impact of COVID-19 on the health-related Quality-of-life of pregnant and postpartum persons. Value Health. 2022;25(1):S6-S. doi:10.1016/j.jval.2021.11.024

20. Biviá-Roig G, La Rosa VL, Gómez-Tébar M, Serrano-Raya L, Amer-Cuenca JJ, Caruso S. Analysis of the impact of the confinement resulting from COVID-19 on the lifestyle and psychological wellbeing of Spanish pregnant women: an internet-based cross-sectionalsSurvey. Int J Environ Res Public Health. 2020;17(16):5933. doi:10.3390/ijerph17165933

21. Brinkley E, Mack CD, Albert L, Knuth K, Reynolds MW, Toovey S. COVID-19 vaccinations in pregnancy: comparative evaluation of acute side effects and self-reported impact on quality of life between pregnant and non-pregnant women in the United States. Am J Perinatol. 2022;39(16):1750–1753. doi:10.1055/s-0042-1748158

22. Wise LA, Wang TR, Wesselink AK, Willis SK, Chaiyasarikul A, Levinson JS. Accuracy of self-reported birth outcomes relative to birth certificate data in an Internet-based prospective cohort study. Paediatr Perinat Epidemiol. 2021;35(5):590–595. doi:10.1111/ppe.12769

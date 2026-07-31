---
project_id: "460-RA"
work_id: "doi:10.1007/s11136-026-04285-x"
doi: "10.1007/s11136-026-04285-x"
pmid: "42260238"
pmcid: "PMC13246841"
title: "Socioeconomic inequalities in health-related quality of life during the COVID-19 pandemic: a six-country comparison using the EQ-5D-5 L"
journal: "Quality of Life Research"
publication_date: "2026-06-08"
volume: "35"
issue: "7"
authors:
  - name: "Joëlle Eijkens"
    affiliation_ids:
      - "Aff1"
  - name: "Joshua M Bonsel"
    affiliation_ids:
      - "Aff2"
  - name: "You-Shan Feng"
    affiliation_ids:
      - "Aff3"
  - name: "M F Bas Janssen"
    affiliation_ids:
      - "Aff4"
  - name: "Erica I Lubetkin"
    affiliation_ids:
      - "Aff5"
  - name: "Juanita A Haagsma"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Department of Public Health, Erasmus MC University Medical Center Rotterdam, Dr. Molenwaterplein 40, Rotterdam, 3015 GD The Netherlands"
  - id: "Aff2"
    name: "Department of Orthopaedics and Sports Medicine, Erasmus MC, Rotterdam, the Netherlands"
  - id: "Aff3"
    name: "Institute for Clinical Epidemiology and Applied Biometrics, Medical University of Tübingen, Tübingen, Germany"
  - id: "Aff4"
    name: "Section Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Rotterdam, the Netherlands"
  - id: "Aff5"
    name: "Department of Community Health and Social Medicine, CUNY School of Medicine, New York, NY USA"
licence: "cc-by"
source_file: "input/projects/460-RA/papers/doi_10.1007_s11136-026-04285-x.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13246841/fullTextXML"
source_method: "epmc_xml"
source_sha256: "48a11a77aa0db598cc9ac3be264317f009a2d98874e87f03bcdd345725b996a5"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Socioeconomic inequalities in health-related quality of life during the COVID-19 pandemic: a six-country comparison using the EQ-5D-5 L

## Abstract

### Purpose

Despite the growing attention to health inequalities, there is no global consensus on how to measure socio-economic status. This study examined inequalities in health-related quality of life (HRQoL) during the early phase of the COVID-19 pandemic across six countries—China, Italy, the Netherlands, Sweden, the United Kingdom (UK), and the United States (US)—using three SES indicators: education level, income, and work status.

### Methods

Between April and June 2020, individuals aged 18–75 years old completed a web-based survey. HRQoL was measured using the EQ-5D-5L Level Sum Score (LSS), where higher scores indicate poorer health. Country-specific differences in LSS across SES groups were assessed using Kruskal-Wallis and Mann-Whitney U tests. Multiple linear regression models, adjusted for age, gender, and chronic conditions, were used to explore associations between SES indicators and HRQoL. No formal correction for multiple testing was applied.

### Results

Data from 17,607 respondents were analyzed. In all countries except Italy, individuals with lower education levels reported significantly higher LSS scores. The largest disparity was observed in the UK. In the Netherlands, Sweden, the UK, and the US, lower-income groups also had higher LSS scores, while no such differences were observed in China or Italy. Across all countries, unemployed individuals consistently reported worse HRQoL. Regression analyses confirmed that younger age, chronic conditions, and unemployment were strongly associated with poorer HRQoL.

### Conclusions

Substantial SES-related health inequalities in HRQoL were observed during the COVID-19 pandemic, especially in the UK. Work status emerged as a particularly strong and consistent predictor across countries.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-026-04285-x.

**Keywords:** Health inequality, Health-related quality of life, EQ-5D-5L, Socio-economic status, COVID-19

Received 2025 Aug 4; Accepted 2026 May 3; Issue date 2026.

## Introduction

Health inequalities—systematic differences in health outcomes between population groups—remain a major global public health concern. The World Health Organization (WHO) affirms that “the enjoyment of the highest attainable standard of health is one of the fundamental rights of every human being” \[1\]. Despite this, persistent disparities exist across clinical and public health domains worldwide \[2\].

A large body of research in health economics has shown a robust socioeconomic gradient in health. Studies have repeatedly found that individuals with higher incomes experience better health, lower mortality, and greater longevity, even after adjusting for other socioeconomic factors \[3, 4\].

Socioeconomic status (SES) is therefore considered a key structural determinant of health. Economic theories point to multiple pathways underlying these gradients, influencing health outcomes through intermediary factors such as health behaviors, exposure to stress, environmental exposures, and access to care \[5, 6\]. Individuals with lower SES are more likely to engage in unhealthy behaviors and experience barriers to healthcare, contributing to poorer health outcomes. While SES-related health inequalities are well documented within Europe \[7\], less is known about their magnitude and nature across different countries.

The COVID-19 pandemic further exposed and potentially exacerbated these disparities by disrupting both structural and intermediary determinants of health. Emerging evidence points to increased unhealthy behaviors among socioeconomically disadvantaged groups \[8\], widespread income and employment losses, especially in low-income countries \[9\], and higher rates of infection and mortality among lower-SES populations \[10, 11\]. Despite the growing attention to health inequalities, there is no global consensus on how to measure SES.

SES is inherently multidimensional and no single measure captures its complexity universally. Indicators such as education, income, work status, and material deprivation vary in relevance across national contexts \[12–18\]. For example, income is a central SES indicator in high-income countries with stable labor markets and formalized wage structures. It is however more difficult to interpret in economies with large informal sectors or irregular earnings. Similarly, education serves as a strong predictor of health in many regions, but the meaning of educational attainment is shaped by national education systems and regional variation in quality and access to education. Cross-country differences in compulsory schooling years, vocational tracks, and tertiary education complicate direct comparisons of education-based health gradients.

Work status further illustrates these challenges. Employment categories such as “employed” and “unemployed” may obfuscate important contextual differences, such as temporary contracts, or state-supported welfare systems.

Similarly, outcome measures differ. Health-related quality of life (HRQoL), which captures physical, mental, and social well-being, is increasingly used in health inequality research. The EQ-5D-5L, a widely validated tool, offers a standardized measure of HRQoL across populations \[20\]. While prior studies have demonstrated its sensitivity to education-related differences in selected European countries \[19, 21\], cross-country comparisons and the role of other SES indicators remain underexplored.

This study addresses these gaps by examining health inequalities in HRQoL, as measured by the EQ-5D-5L, across six countries—China, Italy, the Netherlands, Sweden, the United Kingdom (UK), and the United States (US)—during the first phase of the COVID-19 pandemic. Specifically, it investigates education-related disparities and compares the magnitude of HRQoL differences across alternative SES measures: income and work status.

## Methods

### Study design and study population

This cross-sectional study is a secondary analysis of data from the POPulation health impact of the CORoNavirus disease 2019 (COVID-19) pandemic (POPCORN) study \[22\]. For this study, we used data that were collected during the first wave of data collected. These first wave data were collected via a web-based survey from April 22 to May 5, 2020, in China, Italy, the Netherlands, the UK, and the US, and from May 26 to June 1 in Sweden. The participants, aged 18 to 75 years, were recruited from the general population by an international market research agency (Dynata). The participants were members of the market research agency’s existing voluntary panels. Therefore, the participants had already provided informed consent to participate in online surveys. Detailed comparisons between each country’s sample demographics and national population statistics have been published previously using the same dataset \[22\]. Data were collected anonymously.

### Data collection and outcome measures

The survey included questions on demographics, social factors and health related topics. Official translations of the questionnaire instruments were used whenever available. If necessary, the survey was translated into the official language of each country and back into English using translation software. The translations were checked by bilingual native speakers. No missing data were present because the survey design required responses to all items.

The primary outcome was the EQ-5D-5L Level Sum Score (LSS). The EQ-5D-5L is a HRQoL instrument that consists of five dimensions, namely mobility, self-care, usual activities, pain/discomfort and anxiety/depression. Each dimension has five response options representing five levels of severity (1=“no problems”, 2=“slight problems”, 3=“moderate problems”, 4=“severe problems”, 5=“extreme problems”) \[23\]. A Level Sum Score (LSS) was calculated by summing the scores across all five EQ-5D-5 L dimensions, resulting in a total score ranging from 5 (representing “full health”: 1 + 1+1 + 1+1) to 25 (indicating the “worst possible health state”: 5 + 5+5 + 5+5).

We selected LSS for reasons of comparability and methodological consistency across the six study countries. Unlike EQ-5D-5L index values, which rely on country-specific value sets that differ in e.g. elicitation methods, LSS provides a valuation-free metric based solely on the reported severity levels across the five dimensions. This avoids introducing structural heterogeneity unrelated to actual health differences.

The secondary outcome was the EQ VAS. The EQ VAS is a vertical visual analogue scale that is included in the EQ-5D-5L instrument. It captures a respondent’s overall self-rated health on a scale from 0 to 100, where 100 represents “the best health you can imagine” and 0 represents “the worst health you can imagine”. Respondents are asked to indicate their health today by marking a point on the scale.

### Socio-demographic and health characteristics

The survey also included items on age, gender, education level, income, work status and the presence of chronic health conditions. Chronic health conditions were self-reported and included asthma, chronic bronchitis, severe heart disease, stroke-related impairments, diabetes, chronic rheumatoid arthritis, severe or arthritic back pain, arthrosis-related joint issues (knee or hip), cancer, memory problems due to neurological disorders or aging, depression, anxiety disorders, or other long-term health issues. In this study, respondents were categorized based on the presence of one or more of the listed conditions as having “chronic conditions: yes,” or as having “no chronic conditions” if none were reported.

### SES indicators

SES was assessed using three indicators: education level, income, and work status.

Education level was reported as the highest level of education completed, with country-specific response options. These were recoded according to the International Standard Classification of Education (ISCED-97) into three categories: ‘low’ (ISCED levels 1–2), ‘middle’ (levels 3–4), and ‘high’ (level 5 and above) (see Supplementary Material <a href="#MOESM2" data-ref-type="supplementary-material">1a</a>).

Income referred to annual household income from all sources. Based on national income distributions, respondents were grouped into ‘low’ (bottom 20%), ‘middle’ (middle 60%), and ‘high’ (top 20%) income categories for each country (see Supplementary Material 1b for national thresholds).

Work status was captured using eight response options: “in work: employee,” “in work: self-employed,” “out of work for more than 1 year,” “out of work for less than 1 year,” “looking after others,” “student,” “retired,” and “unable to work.” These were recoded into two categories: ‘Employed’: employee, self-employed, student, or retired; ‘Unemployed’: out of work (less or more than 1 year), looking after others, or unable to work (see Supplementary Material 1c). Our primary rationale for the binary recoding of work status was to distinguish individuals participating in a socially structured daily role (employment, education, or retirement) from those experiencing unemployment or an interruption of regular activity due to ill health or caregiving responsibilities.

### Statistical analysis

Descriptive statistics were used to summarize demographic data. The primary and secondary outcome—EQ-5D-5L LSS and EQ VAS—were reported as medians and interquartile ranges (IQRs) for the total sample and by country. Variations in LSS and EQ VAS across SES groups were interpreted as indicators of health inequalities.

Kruskal-Wallis tests were performed to compare LSS and EQ VAS scores between countries. LSS and EQ VAS scores were then further stratified by SES indicators—education level, income, and work status—and described using medians and IQRs for the total sample and within each country. Differences in LSS and EQ VAS between high and low education levels, and between high and low income groups, were assessed using Mann-Whitney U tests. The same test was used to compare LSS and EQ VAS between employed and unemployed respondents.

To examine associations between demographics, SES indicators, and LSS, multiple linear regression analyses were conducted for the total sample and separately for each country. The variable ‘other’ for gender was excluded from the analysis due to the small sample size (*n* = 34; 0.2%). All models included the SES indicators (education level, income level, and work status) and were adjusted for age, sex, and chronic disease status. These variables were retained in all models regardless of statistical significance to avoid instability associated with stepwise selection procedures and enhance comparability across countries. Next, these analysis were repeated with the EQ VAS as dependent variable to examine associations between demographics, SES indicators, and EQ VAS.

Finally, to assess the relative influence of SES indicators, we evaluated both the presence and magnitude of health inequalities and the strength of associations between SES variables and HRQoL in the regression models.

A p-value of \< 0.05 was considered statistically significant. Because the analyses were conducted separately for six countries, three SES indicators and two outcome measures, the number of statistical tests is very large, which may increase the likelihood of Type I error. However, we did not apply formal multiple-testing corrections because our primary aim was not to test isolated hypotheses, but rather to describe and compare patterns of socioeconomic inequalities in HRQoL across countries.

All statistical analyses were carried out using SPSS version 28 for Windows \[24\].

## Results

### Study population

Of the 19,432 individuals who completed the survey, 1,825 (9.4%) did not report their income and were excluded from the analysis. This subgroup differed significantly from those who did report income in terms of age, gender, chronic disease status, education level, and work status (see Supplementary Material 2). The final analytic sample included 17,607 respondents, with the following country distribution: China (*n* = 3,146; 17.9%), Italy (*n* = 2,866; 16.3%), the Netherlands (*n* = 2,736; 15.5%), Sweden (*n* = 2,839; 16.1%), the UK (*n* = 2,964; 16.8%), and the US (*n* = 3,056; 17.4%). Table <a href="#Tab1" data-ref-type="table">1</a> shows the demographics of the respondents included in the study. The median age of the study sample ranged from 34.0 in the Chinese sample to 48.0 in the Dutch and Swedish sample, with an overall median of 43.0 (IQR 25.0). Less than half of the respondents were male (47.7%). Chronic conditions were present in 43.5% of the respondents, ranging from 20.4% in the Chinese sample to 56.9% in the Swedish sample. 2769 respondents (15.7%) and 9089 respondents (51.6%) of the total sample had a low and high educational level, respectively. With regards to income, 3774 respondents (21.4%) had a low income and 3165 (18.0%) had a high income in the overall sample. 14,393 respondents (81.7%) of the overall sample were employed against 3214 unemployed respondents (18.3%).

<div id="Tab1" class="table-wrap">

<div class="caption">

Socio-demographic and medical characteristics of the study population, total and by country

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Age</th>
<th rowspan="2" style="text-align: left;">Median (IQR)</th>
<th style="text-align: left;">China<br />
(<em>n</em> = 3146)</th>
<th style="text-align: left;">Italy<br />
(<em>n</em> = 2866)</th>
<th style="text-align: left;">Netherlands<br />
(<em>n</em> = 2736)</th>
<th style="text-align: left;">Sweden<br />
(<em>n</em> = 2839)</th>
<th style="text-align: left;">UK<br />
(<em>n</em> = 2964)</th>
<th style="text-align: left;">US<br />
(<em>n</em> = 3056)</th>
<th style="text-align: left;">Total<br />
(<em>n</em> = 17607)</th>
</tr>
<tr>
<th style="text-align: left;">34.0 (15.0)</th>
<th style="text-align: left;">43.0 (22.0)</th>
<th style="text-align: left;">48.0 (29.0)</th>
<th style="text-align: left;">48.0 (28.0)</th>
<th style="text-align: left;">44.0 (25.0)</th>
<th style="text-align: left;">46.0 (27.0)</th>
<th style="text-align: left;">43.0 (25.0)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6" style="text-align: left;">Age range</td>
<td style="text-align: left;">18–24</td>
<td style="text-align: center;">478 (15.2%)</td>
<td style="text-align: center;">225 (7.9%)</td>
<td style="text-align: center;">265 (9.7%)</td>
<td style="text-align: center;">253 (8.9%)</td>
<td style="text-align: center;">275 (9.3%)</td>
<td style="text-align: center;">334 (10.9%)</td>
<td style="text-align: center;">1830 (10.4%)</td>
</tr>
<tr>
<td style="text-align: left;">25–34</td>
<td style="text-align: center;">1116 (35.5%)</td>
<td style="text-align: center;">559 (19.5%)</td>
<td style="text-align: center;">483 (17.7%)</td>
<td style="text-align: center;">486 (17.1%)</td>
<td style="text-align: center;">603 (20.3%)</td>
<td style="text-align: center;">522 (17.1%)</td>
<td style="text-align: center;">3769 (21.4%)</td>
</tr>
<tr>
<td style="text-align: left;">35–44</td>
<td style="text-align: center;">824 (26.2%)</td>
<td style="text-align: center;">760 (26.5%)</td>
<td style="text-align: center;">456 (16.7%)</td>
<td style="text-align: center;">496 (17.5%)</td>
<td style="text-align: center;">670 (22.6%)</td>
<td style="text-align: center;">584 (19.1%)</td>
<td style="text-align: center;">3790 (21.5%)</td>
</tr>
<tr>
<td style="text-align: left;">45–54</td>
<td style="text-align: center;">437 (13.9%)</td>
<td style="text-align: center;">595 (20.8%)</td>
<td style="text-align: center;">469 (17.1%)</td>
<td style="text-align: center;">556 (19.6%)</td>
<td style="text-align: center;">484 (16.3%)</td>
<td style="text-align: center;">558 (18.3%)</td>
<td style="text-align: center;">3099 (17.6%)</td>
</tr>
<tr>
<td style="text-align: left;">55–64</td>
<td style="text-align: center;">257 (8.2%)</td>
<td style="text-align: center;">411 (14.3%)</td>
<td style="text-align: center;">530 (19.4%)</td>
<td style="text-align: center;">491 (17.3%)</td>
<td style="text-align: center;">471 (15.9%)</td>
<td style="text-align: center;">524 (17.1%)</td>
<td style="text-align: center;">2684 (15.2%)</td>
</tr>
<tr>
<td style="text-align: left;">65–75</td>
<td style="text-align: center;">34 (1.1%)</td>
<td style="text-align: center;">316 (11.0%)</td>
<td style="text-align: center;">533 (19.5%)</td>
<td style="text-align: center;">557 (19.6%)</td>
<td style="text-align: center;">461 (15.6%)</td>
<td style="text-align: center;">534 (17.5%)</td>
<td style="text-align: center;">2435 (13.8%)</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Gender</td>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">1388 (44.1%)</td>
<td style="text-align: center;">1411 (49.2%)</td>
<td style="text-align: center;">1389 (50.8%)</td>
<td style="text-align: center;">1402 (49.4%)</td>
<td style="text-align: center;">1446 (48.8%)</td>
<td style="text-align: center;">1354 (44.3%)</td>
<td style="text-align: center;">8390 (47.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">1750 (55.6%)</td>
<td style="text-align: center;">1453 (50.7%)</td>
<td style="text-align: center;">1346 (49.2%)</td>
<td style="text-align: center;">1430 (50.4%)</td>
<td style="text-align: center;">1514 (51.1%)</td>
<td style="text-align: center;">1690 (55.3%)</td>
<td style="text-align: center;">9183 (52.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: center;">8 (0.3%)</td>
<td style="text-align: center;">2 (0.1%)</td>
<td style="text-align: center;">1 (0.0%)</td>
<td style="text-align: center;">7 (0.2%)</td>
<td style="text-align: center;">4 (0.1%)</td>
<td style="text-align: center;">12 (0.4%)</td>
<td style="text-align: center;">34 (0.2%)</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Education level</td>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">307 (9.8%)</td>
<td style="text-align: center;">381 (13.3%)</td>
<td style="text-align: center;">673 (24.6%)</td>
<td style="text-align: center;">1143 (40.3%)</td>
<td style="text-align: center;">68 (2.3%)</td>
<td style="text-align: center;">197 (6.4%)</td>
<td style="text-align: center;">2769 (15.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">963 (30.6%)</td>
<td style="text-align: center;">1276 (44.5%)</td>
<td style="text-align: center;">828 (30.3%)</td>
<td style="text-align: center;">516 (18.2%)</td>
<td style="text-align: center;">1080 (36.4%)</td>
<td style="text-align: center;">1086 (35.5%)</td>
<td style="text-align: center;">5749 (32.7%)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">1876 (59.6%)</td>
<td style="text-align: center;">1209 (42.2%)</td>
<td style="text-align: center;">1235 (45.1%)</td>
<td style="text-align: center;">1180 (41.6%)</td>
<td style="text-align: center;">1816 (61.3%)</td>
<td style="text-align: center;">1773 (58.0%)</td>
<td style="text-align: center;">9089 (51.6%)</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Income</td>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">613 (19.5%)</td>
<td style="text-align: center;">691 (24.1%)</td>
<td style="text-align: center;">548 (20.0%)</td>
<td style="text-align: center;">597 (21.0%)</td>
<td style="text-align: center;">774 (26.1%)</td>
<td style="text-align: center;">551 (18.0%)</td>
<td style="text-align: center;">3774 (21.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1800 (57.2%)</td>
<td style="text-align: center;">1761 (61.4%)</td>
<td style="text-align: center;">1720 (62.9%)</td>
<td style="text-align: center;">1789 (63.0%)</td>
<td style="text-align: center;">1539 (51.9%)</td>
<td style="text-align: center;">2059 (67.4%)</td>
<td style="text-align: center;">10,668 (60.6%)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">733 (23.3%)</td>
<td style="text-align: center;">414 (14.4%)</td>
<td style="text-align: center;">468 (17.1%)</td>
<td style="text-align: center;">453 (16.0%)</td>
<td style="text-align: center;">651 (22.0%)</td>
<td style="text-align: center;">446 (14.6%)</td>
<td style="text-align: center;">3165 (18.0%)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Work status</td>
<td style="text-align: left;">Employed</td>
<td style="text-align: center;">2996 (95.2%)</td>
<td style="text-align: center;">2235 (78.0%)</td>
<td style="text-align: center;">2136 (78.1%)</td>
<td style="text-align: center;">2301 (81.0%)</td>
<td style="text-align: center;">2405 (81.1%)</td>
<td style="text-align: center;">2320 (75.9%)</td>
<td style="text-align: center;">14,393 (81.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: center;">150 (4.8%)</td>
<td style="text-align: center;">631 (22.0%)</td>
<td style="text-align: center;">600 (21.9%)</td>
<td style="text-align: center;">538 (19.0%)</td>
<td style="text-align: center;">559 (18.9%)</td>
<td style="text-align: center;">736 (24.1%)</td>
<td style="text-align: center;">3214 (18.3%)</td>
</tr>
<tr>
<td style="text-align: left;">Chronic conditions</td>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">643 (20.4%)</td>
<td style="text-align: center;">1129 (39.4%)</td>
<td style="text-align: center;">1416 (51.8%)</td>
<td style="text-align: center;">1615 (56.9%)</td>
<td style="text-align: center;">1302 (43.9%)</td>
<td style="text-align: center;">1568 (51.3%)</td>
<td style="text-align: center;">7673 (43.6%)</td>
</tr>
</tbody>
</table>

</div>

### Health outcomes

The overall median EQ-5D-5L Level Sum Score (LSS) for the total sample was 6.00 (IQR 3.00). Respondents in China reported the highest HRQoL, with a median LSS of 5.00 (IQR 1.00), followed by those in the Netherlands and the UK, both with a median LSS of 6.00 (IQR 4.00). The highest median LSS scores—indicating poorer HRQoL—were observed in Italy, Sweden, and the US, each with a median of 7.00 (IQRs of 3.00, 4.00, and 4.00, respectively; Table <a href="#Tab2" data-ref-type="table">2</a>). Differences in LSS rank sums across countries were statistically significant (*p* \< 0.01).

<div id="Tab2" class="table-wrap">

<div class="caption">

Median EQ-5D-5L LSS with IQR per SES indicator, total sample and stratified by country

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Median (IQR)</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">China<br />
(n = 3146)</th>
<th style="text-align: left;">Italy<br />
(n = 2866)</th>
<th style="text-align: left;">Netherlands<br />
(n = 2736)</th>
<th style="text-align: left;">Sweden<br />
( n = 2839)</th>
<th style="text-align: left;">UK<br />
(n = 2964)</th>
<th style="text-align: left;">US<br />
(n = 3056)</th>
<th style="text-align: left;">Total<br />
(n = 17,607)</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Total</td>
<td style="text-align: left;">5.00 (1.00)</td>
<td style="text-align: left;">7.00 (3.00)</td>
<td style="text-align: left;">6.00 (4.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;">6.00 (4.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;">6.00 (3.00)</td>
<td style="text-align: left;">p &lt; 0.01**</td>
</tr>
<tr>
<td style="text-align: left;">Education</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;"><strong>5.00 (1.00)*</strong></td>
<td style="text-align: left;">6.00 (2.00)</td>
<td style="text-align: left;"><strong>7.00 (5.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (4.00)*</strong></td>
<td style="text-align: left;"><strong>8.00 (6.00)*</strong></td>
<td style="text-align: left;"><strong>8.00 (7.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (4.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">5.00 (1.00)</td>
<td style="text-align: left;">7.00 (3.00)</td>
<td style="text-align: left;">6.00 (4.00)</td>
<td style="text-align: left;">8.00 (5.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;">6.00 (4.00)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;"><strong>5.00 (1.00)*</strong></td>
<td style="text-align: left;">7.00 (3.00)</td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (4.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (4.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Income</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">5.00 (1.00)</td>
<td style="text-align: left;">7.00 (2.00)</td>
<td style="text-align: left;"><strong>7.00 (5.00)*</strong></td>
<td style="text-align: left;"><strong>8.00 (5.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (4.00)*</strong></td>
<td style="text-align: left;"><strong>8.00 (6.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (4.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">5.00 (1.00)</td>
<td style="text-align: left;">6.00 (3.00)</td>
<td style="text-align: left;">6.00 (3.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;">6.00 (3.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;">6.00 (3.00)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">5.00 (1.00)</td>
<td style="text-align: left;">7.00 (4.00)</td>
<td style="text-align: left;"><strong>6.00 (4.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (2.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Work status</td>
<td style="text-align: left;">Employed</td>
<td style="text-align: left;"><strong>5.00 (1.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: left;"><strong>6.00 (3.00)*</strong></td>
<td style="text-align: left;"><strong>7.00 (2.00)*</strong></td>
<td style="text-align: left;"><strong>9.00 (6.00)*</strong></td>
<td style="text-align: left;"><strong>9.00 (6.00)*</strong></td>
<td style="text-align: left;"><strong>9.00 (7.00)*</strong></td>
<td style="text-align: left;"><strong>9.00 (7.00)*</strong></td>
<td style="text-align: left;"><strong>8.00 (6.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

\*Outcomes in bold differ significantly (p \< 0.05) within the SES indicator in the country or total sample

<sup>\*\*</sup> P-value calculated for the difference in rank sums of LSS across countries

</div>

The overall median EQ VAS score for the total sample and by country was 80.0, except for respondents from China who reported a median EQ VAS score of 90.0 (IQR 15.0) (Table <a href="#Tab3" data-ref-type="table">3</a>). Differences in EQ VAS rank sums across countries were also statistically significant (*p* \< 0.01).

<div id="Tab3" class="table-wrap">

<div class="caption">

Median EQ-5D-5L VAS with IQR per SES indicator, total sample and stratified by country

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Median (IQR)</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">China<br />
(n = 3146)</th>
<th style="text-align: left;">Italy<br />
(n = 2866)</th>
<th style="text-align: left;">Netherlands<br />
(n = 2736)</th>
<th style="text-align: left;">Sweden<br />
( n = 2839)</th>
<th style="text-align: left;">UK<br />
(n = 2964)</th>
<th style="text-align: left;">US<br />
(n = 3056)</th>
<th style="text-align: left;">Total<br />
(n = 17,607)</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Total</td>
<td style="text-align: left;">90.00 (15.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (30.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">p &lt; 0.01**</td>
</tr>
<tr>
<td style="text-align: left;">Education</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">85.00 (10.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (25.00)</td>
<td style="text-align: left;"><strong>75.00 (30.00)*</strong></td>
<td style="text-align: left;"><strong>75.00 (35.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (30.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (25.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">90.00 (15.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">75.00 (25.00)</td>
<td style="text-align: left;">80.00 (30.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">90.00 (15.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>85.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Income</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">90.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;"><strong>80.00 (25.00)*</strong></td>
<td style="text-align: left;"><strong>70.00 (35.00)*</strong></td>
<td style="text-align: left;"><strong>75.00 (35.00)*</strong></td>
<td style="text-align: left;"><strong>75.00 (35.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (30.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">90.00 (10.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (25.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">90.00 (15.00)</td>
<td style="text-align: left;">80.00 (20.00)</td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>85.00 (15.00)*</strong></td>
<td style="text-align: left;"><strong>85.00 (15.00)*</strong></td>
<td style="text-align: left;"><strong>85.00 (15.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Work status</td>
<td style="text-align: left;">Employed</td>
<td style="text-align: left;"><strong>90.00 (15.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>85.00 (20.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (20.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: left;"><strong>85.00 (25.00)*</strong></td>
<td style="text-align: left;"><strong>80.00 (25.00)*</strong></td>
<td style="text-align: left;"><strong>70.00 (25.00)*</strong></td>
<td style="text-align: left;"><strong>70.00 (36.25)*</strong></td>
<td style="text-align: left;"><strong>70.00 (30.00)*</strong></td>
<td style="text-align: left;"><strong>75.00 (35.00)*</strong></td>
<td style="text-align: left;"><strong>75.00 (30.00)*</strong></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

\*Outcomes in bold differ significantly (p \< 0.05) within the SES indicator in the country or total sample

<sup>\*\*</sup> P-value calculated for the difference in rank sums of EQ VAS across countries

</div>

### Health outcomes by education level

In the total sample, respondents with a low education level had a median LSS of 7.00 (IQR 4.00) versus a median LSS of 6.00 (IQR 3.00) for respondents with a high education level (*p* \< 0.05). Respondents from the Netherlands, the UK, and the US with middle or high education levels had a lower median LSS compared to those with a low education group. For respondents from those countries, there was also a significant difference in the rank sums of the LSS between low and high income groups (*p* \< 0.05).The largest difference in median LSS between low and high education groups was observed among respondents from the UK, with a difference of 2 points. For respondents from the Netherlands and the US, this difference was 1 point. Contradictory findings were seen in respondents residing in Italy, the median LSS for respondents with a high education level was 1 point higher than for respondents with a low education level. However, there was no significant difference in rank sums (*p* \> 0.05). For respondents residing in China the median LSS was 5.00 (IQR 1.00) regardless of education level, although there was a significant difference in rank sums (*p* \< 0.05). Similarly, the median LSS for respondents residing in Sweden was 7.00 (IQR 4.00) for both high and low education levels, with a significant difference in ranks sums (*p* \< 0.05) (Table <a href="#Tab2" data-ref-type="table">2</a>).

With regards to the EQ VAS, education showed little overall gradient in the pooled sample. There was only modest country-specific variation for respondents from Sweden UK and US, with a significant difference in the rank sums of the LSS between low and high income groups (*p* \< 0.05). (Table <a href="#Tab3" data-ref-type="table">3</a>**)**.

### Health outcomes by income level

In the total sample, respondents with a low income reported a higher median LSS of 7.00 (IQR 4.00), compared to 6.00 (IQR 3.00) among those with a high income (*p* \< 0.05). In the Netherlands, Sweden, the UK, and the US, individuals with middle or high income consistently had lower median LSS scores than those with low income, with significant differences in rank sums across income groups (*p* \< 0.05). The difference in median LSS between income groups was 1 point in both the Netherlands and the UK, and 2 points in Sweden and the US. In contrast, no differences in median LSS or rank sums were observed in China and Italy by income level (*p* \> 0.05) (Table <a href="#Tab2" data-ref-type="table">2</a>).

For the EQ VAS, we observed that respondents with a high income reported higher EQ VAS in the pooled data (85.0; IQR 15.0) compared with respondents with low or middle income (both 80.0; IQR 30 and 20, respectively). In Sweden, the UK, and the US, individuals with middle or high income had consistently higher median EQ VAS scores than those with low income, with significant differences in rank sums across income groups (*p* \< 0.05). No differences in median EQ VAS or rank sums were observed in China and Italy by income level (*p* \> 0.05) (Table <a href="#Tab3" data-ref-type="table">3</a>).

### Health outcomes by work status

In the total sample, unemployed respondents had a median LSS of 8.00 (IQR 6.00) versus a median LSS of 6.00 (IQR 3.00) for employed respondents (*p* \< 0.05). Across all countries, employed respondents had a lower median LSS compared to the median LSS of unemployed respondents. Additionally, the rank sums were significantly different between employed and unemployed respondents in all countries (*p* \< 0.05). Employed respondents residing in the Netherlands, UK and US had the largest LSS difference (3 points) compared with the unemployed respondents. In Sweden this difference was 2 points. In Italy and China the difference in median LSS was 1 point (Table <a href="#Tab2" data-ref-type="table">2</a>).

The EQ VAS echoes these findings. Unemployed respondents had lower EQ VAS than employed respondents in the pooled sample as well as in all countries, except for Sweden. Differences in median EQ VAS between work status groups were highest among respondents from the Netherlands, Sweden, UK and US (all 10 points differences).The EQ VAS rank sums were significantly different between employed and unemployed respondents in all countries (*p* \< 0.05) (Table <a href="#Tab3" data-ref-type="table">3</a>).

### Association between respondent demographics and SES indicators and the LSS

Table <a href="#Tab4" data-ref-type="table">4</a> presents the multiple linear regression results for the LSS for the total sample and stratified by country. A positive regression coefficient indicates a higher LSS—reflecting poorer HRQoL—relative to the reference group.

<div id="Tab4" class="table-wrap">

<div class="caption">

Multiple linear regression results of participant characteristics, SES indicators and EQ-5D-5 L LSS, total sample and by country

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">China</th>
<th colspan="3" style="text-align: left;">Italy</th>
<th colspan="3" style="text-align: left;">The Netherlands</th>
<th colspan="3" style="text-align: left;">Sweden</th>
<th colspan="3" style="text-align: left;">UK</th>
<th colspan="3" style="text-align: left;">US</th>
<th colspan="3" style="text-align: left;">Total</th>
</tr>
<tr>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">5.560</td>
<td style="text-align: left;">0.093</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">6.408</td>
<td style="text-align: left;">0.145</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">6.363</td>
<td style="text-align: left;">0.188</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">7.015</td>
<td style="text-align: left;">0.190</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">6.521</td>
<td style="text-align: left;">0.213</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">7.892</td>
<td style="text-align: left;">0.209</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">6.378</td>
<td style="text-align: left;">0.075</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">-0.002</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">0.406</td>
<td style="text-align: left;">-0.005</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;">-0.016</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-0.015</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-0.011</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">-0.038</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-0.011</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Gender (ref = female)*</td>
<td style="text-align: left;">-0.055</td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;">0.276</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">0.080</td>
<td style="text-align: left;">0.879</td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.099</td>
<td style="text-align: left;">0.915</td>
<td style="text-align: left;">-0.105</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.320</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">0.107</td>
<td style="text-align: left;">0.308</td>
<td style="text-align: left;">-0.002</td>
<td style="text-align: left;">0.115</td>
<td style="text-align: left;">0.983</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;">0.718</td>
</tr>
<tr>
<td style="text-align: left;">Chronic disease (ref = no)</td>
<td style="text-align: left;">1.848</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.238</td>
<td style="text-align: left;">0.081</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.386</td>
<td style="text-align: left;">0.102</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.627</td>
<td style="text-align: left;">0.108</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.833</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.738</td>
<td style="text-align: left;">0.114</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.693</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Low edu level</td>
<td style="text-align: left;">-0.092</td>
<td style="text-align: left;">0.094</td>
<td style="text-align: left;">0.332</td>
<td style="text-align: left;">-0.194</td>
<td style="text-align: left;">0.133</td>
<td style="text-align: left;">0.145</td>
<td style="text-align: left;">0.514</td>
<td style="text-align: left;">0.132</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-0.002</td>
<td style="text-align: left;">0.117</td>
<td style="text-align: left;">0.987</td>
<td style="text-align: left;">-0.034</td>
<td style="text-align: left;">0.360</td>
<td style="text-align: left;">0.925</td>
<td style="text-align: left;">0.186</td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">0.446</td>
<td style="text-align: left;">0.110</td>
<td style="text-align: left;">0.059</td>
<td style="text-align: left;">0.059</td>
</tr>
<tr>
<td style="text-align: left;">Middle edu level</td>
<td style="text-align: left;">-0.103</td>
<td style="text-align: left;">0.061</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">-0.063</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.470</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.115</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">0.366</td>
<td style="text-align: left;">0.148</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;">0.361</td>
<td style="text-align: left;">0.116</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">0.102</td>
<td style="text-align: left;">0.125</td>
<td style="text-align: left;">0.413</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;">Low income level</td>
<td style="text-align: left;">-0.002</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.972</td>
<td style="text-align: left;">0.044</td>
<td style="text-align: left;">0.099</td>
<td style="text-align: left;">0.661</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.130</td>
<td style="text-align: left;">0.963</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">0.134</td>
<td style="text-align: left;">0.418</td>
<td style="text-align: left;">-0.213</td>
<td style="text-align: left;">0.131</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.461</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">-0.092</td>
<td style="text-align: left;">0.051</td>
<td style="text-align: left;">0.070</td>
</tr>
<tr>
<td style="text-align: left;">High income level</td>
<td style="text-align: left;">0.060</td>
<td style="text-align: left;">0.064</td>
<td style="text-align: left;">0.350</td>
<td style="text-align: left;">0.359</td>
<td style="text-align: left;">0.117</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">0.281</td>
<td style="text-align: left;">0.170</td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;">-0.659</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-0.568</td>
<td style="text-align: left;">0.165</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.166</td>
<td style="text-align: left;">0.615</td>
<td style="text-align: left;">-0.186</td>
<td style="text-align: left;">0.066</td>
<td style="text-align: left;">0.005</td>
</tr>
<tr>
<td style="text-align: left;">Employment (ref = employed)</td>
<td style="text-align: left;">0.881</td>
<td style="text-align: left;">0.124</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.443</td>
<td style="text-align: left;">0.103</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">1.558</td>
<td style="text-align: left;">0.126</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">1.794</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.244</td>
<td style="text-align: left;">0.144</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">1.476</td>
<td style="text-align: left;">0.141</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">1.630</td>
<td style="text-align: left;">0.054</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">R<sup>2</sup></td>
<td colspan="3" style="text-align: left;">0.246</td>
<td colspan="3" style="text-align: left;">0.222</td>
<td colspan="3" style="text-align: left;">0.270</td>
<td colspan="3" style="text-align: left;">0.269</td>
<td colspan="3" style="text-align: left;">0.300</td>
<td colspan="3" style="text-align: left;">0.250</td>
<td colspan="3" style="text-align: left;">0.274</td>
</tr>
</tbody>
</table>

\*Only male and female, no ‘other gender’.

</div>

Across all countries, the presence of one or more chronic conditions was significantly associated with higher LSS scores. Increasing age was linked to lower LSS (better HRQoL) in all countries and in the total sample, except in China, where no significant association was observed. Gender showed no significant association with LSS in any model.

Among SES indicators, lower education level was significantly associated with higher LSS in the Netherlands and the total sample. In Sweden and the UK, a middle education level—rather than a low level—was positively associated with LSS, suggesting a possible U-shaped relationship between education and HRQoL. No significant education-related associations were found in Italy or the US.

Regarding income, higher income levels were significantly associated with lower LSS (better HRQoL) in Sweden and the UK. Conversely, in the Netherlands and Italy, higher income was unexpectedly associated with higher LSS. In the US, lower income was linked to higher LSS, while no significant income-related associations were observed in China or the total sample.

Unemployment was consistently associated with higher LSS scores across all countries and in the total sample, indicating lower HRQoL among unemployed respondents.

### Association between respondent demographics and SES indicators and the EQ VAS

Table <a href="#Tab5" data-ref-type="table">5</a> presents the multiple linear regression results for the EQ VAS for the total sample and stratified by country. A negative regression coefficient indicates a lower EQ VAS—reflecting poorer HRQoL—relative to the reference group.

<div id="Tab5" class="table-wrap">

<div class="caption">

Multiple linear regression results of participant characteristics, SES indicators and EQ VAS, total sample and by country

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">China</th>
<th colspan="3" style="text-align: left;">Italy</th>
<th colspan="3" style="text-align: left;">The Netherlands</th>
<th colspan="3" style="text-align: left;">Sweden</th>
<th colspan="3" style="text-align: left;">UK</th>
<th colspan="3" style="text-align: left;">US</th>
<th colspan="3" style="text-align: left;">Total</th>
</tr>
<tr>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">b</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">91.72</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">87.15</td>
<td style="text-align: left;">1.02</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">80.30</td>
<td style="text-align: left;">1.17</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">80.10</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">79.63</td>
<td style="text-align: left;">1.24</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">84.43</td>
<td style="text-align: left;">1.16</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">83.90</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">-0.14</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-0.09</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.07</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.05</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.319</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.596</td>
<td style="text-align: left;">-0.02</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.002</td>
</tr>
<tr>
<td style="text-align: left;">Gender (ref = female)*</td>
<td style="text-align: left;">1.02</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.024</td>
<td style="text-align: left;">-0.36</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.517</td>
<td style="text-align: left;">-0.48</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.432</td>
<td style="text-align: left;">2.04</td>
<td style="text-align: left;">0.70</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">-0.85</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.173</td>
<td style="text-align: left;">0.67</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: left;">0.301</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.194</td>
</tr>
<tr>
<td style="text-align: left;">Chronic disease (ref = no)</td>
<td style="text-align: left;">-9.73</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-11.18</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-11.82</td>
<td style="text-align: left;">0.63</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-13.92</td>
<td style="text-align: left;">0.71</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-13.51</td>
<td style="text-align: left;">0.63</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-10.72</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-12.72</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Low edu level</td>
<td style="text-align: left;">1.45</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">1.65</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;">1.40</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">0.088</td>
<td style="text-align: left;">-1.59</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">2.09</td>
<td style="text-align: left;">0.871</td>
<td style="text-align: left;">-0.80</td>
<td style="text-align: left;">1.36</td>
<td style="text-align: left;">0.560</td>
<td style="text-align: left;">-0.74</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.045</td>
</tr>
<tr>
<td style="text-align: left;">Middle edu level</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.505</td>
<td style="text-align: left;">-0.10</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.871</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: left;">0.71</td>
<td style="text-align: left;">0.263</td>
<td style="text-align: left;">-1.16</td>
<td style="text-align: left;">0.98</td>
<td style="text-align: left;">0.235</td>
<td style="text-align: left;">-1.69</td>
<td style="text-align: left;">0.67</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;">-0.31</td>
<td style="text-align: left;">0.70</td>
<td style="text-align: left;">0.653</td>
<td style="text-align: left;">-0.48</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.091</td>
</tr>
<tr>
<td style="text-align: left;">Low income level</td>
<td style="text-align: left;">-0.08</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: left;">0.901</td>
<td style="text-align: left;">-0.42</td>
<td style="text-align: left;">0.70</td>
<td style="text-align: left;">0.550</td>
<td style="text-align: left;">-0.18</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.820</td>
<td style="text-align: left;">-3.35</td>
<td style="text-align: left;">0.89</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">3.87</td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-4.69</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">1.88</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">High income level</td>
<td style="text-align: left;">2.04</td>
<td style="text-align: left;">0.58</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">0.998</td>
<td style="text-align: left;">2.35</td>
<td style="text-align: left;">1.06</td>
<td style="text-align: left;">0.026</td>
<td style="text-align: left;">4.03</td>
<td style="text-align: left;">0.97</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">6.74</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">2.51</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">4.16</td>
<td style="text-align: left;">0.42</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Employment (ref = employed)</td>
<td style="text-align: left;">-3.44</td>
<td style="text-align: left;">1.11</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">-3.52</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-6.70</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-8.81</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-8.87</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-6.29</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">-7.01</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">R<sup>2</sup></td>
<td colspan="3" style="text-align: left;">0.117</td>
<td colspan="3" style="text-align: left;">0.140</td>
<td colspan="3" style="text-align: left;">0.168</td>
<td colspan="3" style="text-align: left;">0.207</td>
<td colspan="3" style="text-align: left;">0.231</td>
<td colspan="3" style="text-align: left;">0.145</td>
<td colspan="3" style="text-align: left;">0.186</td>
</tr>
</tbody>
</table>

\*Only male and female, no ‘other gender’.

</div>

In multivariable linear regression, chronic disease and unemployment were the strongest correlates of poorer EQ VAS across all countries. Presence of a chronic disease was associated with 10–14-point lower EQ VAS. Being unemployed (vs. employed) was likewise associated with 3–9-point lower EQ VAS. Income showed a positive gradient in several settings: high income (vs. low income) was associated with higher EQ VAS in the pooled sample, with the largest effects in the UK and Sweden. Low income showed heterogeneous associations: lower VAS in Sweden and US but higher VAS in the UK; in the pooled model the coefficient was small but positive. Educational level exhibited modest and inconsistent associations: compared with high education, the pooled model indicated slightly lower EQ VAS for low education and a non-significant difference for middle education; within countries, significant differences were limited. Gender was generally not associated with EQ VAS, except for higher EQ VAS scores among males in China and Sweden. Age showed a small overall decrease in VAS per year in the pooled model, with heterogeneity by country (decreases in China and Italy; small increases in the Netherlands and Sweden).

## Discussion

This study aimed to examine health inequalities in HRQoL, as measured by the EQ-5D-5L LSS and EQ VAS, across six countries during the COVID-19 pandemic, focusing on education level as the primary SES indicator. Health inequalities were evident in most countries, with lower HRQoL observed among respondents with lower education levels—except in Italy. The greatest disparities were found in the UK. Structural features of the UK context—such as persistent regional deprivation, longstanding income inequality, and marked differences in employment security—may explain why disparities in HRQoL were especially pronounced.

The secondary aim was to assess whether the magnitude of these inequalities differed by SES measure—education, income, or work status. While education and income showed similar magnitudes of inequality, work status consistently revealed larger disparities.

Our findings align with previous studies using EQ-5D data in China \[25\], Sweden \[26\], the Netherlands, and the UK \[19\]. However, unlike Spronk et al. \[19\], we did not find educational disparities in Italy. Differences in sample composition or the impact of the COVID-19 pandemic may explain this discrepancy. Consistent with the study by Spronk et al. \[19\], which was conducted before the COVID-19 pandemic, we found the largest inequalities in the UK and the smallest in Italy.

Regression results showed that lower education was significantly associated with poorer HRQoL, measured with the LSS, in the Netherlands, Sweden and the total sample. In Sweden and the UK, a middle education level was associated with lower HRQoL, suggesting a U-shaped pattern. In China, the relationship was reversed. No associations were found in Italy or the US. Education, as a stable SES measure, may better capture long-term effects on HRQoL compared to income or employment, which can fluctuate over time \[27, 28\].

While visualizations of marginal effects can be informative for illustrating non-linear associations, the U-shaped education–HRQoL patterns observed in a few countries can already be understood from the regression results presented. In particular, the country-specific coefficients clearly indicate where intermediate education groups exhibit slightly lower HRQoL relative to both lower and higher education categories, and where this pattern is absent. These deviations likely reflect contextual factors such as sample composition, cultural differences in health reporting, or income-related measurement differences rather than systematic reversals of socioeconomic gradients. By interpreting the model estimates directly, we are able to highlight these country-specific nuances without adding additional figures, while maintaining clarity and focus in the presentation of results.

Income-related inequalities were inconsistent across countries. Previous research suggested income may be a stronger SES predictor \[29, 30\], but our findings challenge that assumption. Household income data, used in this study, may be less reliable due to cultural differences in household composition and incomplete information.

Work status emerged as the most consistent SES indicator associated with HRQoL. Unemployed individuals reported significantly lower HRQoL across all countries. This aligns with existing literature showing a widening gap in health between employed and unemployed individuals \[31–33\]. Employment positively influences mental and physical health \[34\], but a “healthy worker effect” may confound these findings: healthier individuals are more likely to be employed \[35\]. Because poorer health can lead to job loss or labor-market withdrawal, differences in HRQoL between employed and unemployed groups may partly reflect underlying health selection rather than socioeconomic disadvantage alone. This dynamic may therefore exaggerate observed disparities and complicates interpretation of employment-related SES gradients.

In our study we used both the EQ-5D-5L LSS and the EQ VAS as outcome measure. Overall, the regression analyses for both the EQ-5D-5L LSS and the EQ VAS showed remarkably consistent patterns, identifying the same key determinants of lower HRQoL across countries. Chronic disease and unemployment emerged as the strongest and most consistent predictors of poorer health across both measures. Chronic disease was associated with substantially poorer outcomes (higher LSS; lower EQ VAS) in all countries, and the magnitude of effects was very similar across the two instruments. Likewise, unemployment showed large and statistically significant associations with poorer health in both models, with highly comparable effect sizes.

In contrast, education and income level showed more heterogeneous associations, and the two instruments did not always align. The EQ VAS appears more responsive to income- and education-related differences, whereas the LSS yields more conservative, and sometimes inconsistent, SES effects across countries. This indicates that while the EQ-5D-5L LSS and EQ VAS capture similar determinants of HRQoL, they differ in their sensitivity to socioeconomic gradients.

The findings of this study have important implications for policy makers that aim to reduce socioeconomic inequalities in health and improve population HRQoL. First, the consistent SES-related disparities observed across countries, even under the exceptional conditions of the COVID-19 pandemic, highlight the need for governments to prioritize structural policies that address education access, income security, and labor market protections. Investments in social safety nets, progressive income support, and targeted interventions for low SES groups may help mitigate the persistent HRQoL gaps identified here.

### Strengths and Limitations

Key strengths of this study include a large, multi-country sample and use of a validated HRQoL instrument. However, a key limitation of this study is its cross-sectional design, which captures exposures and outcomes at a single point in time. As a result, the temporal ordering of socioeconomic status and health-related quality of life cannot be established, and causal inferences cannot be drawn. Observed associations may reflect reverse causality. For example, poorer health leading to lower income or reduced employment. Longitudinal data would be necessary to clarify the directionality of these relationships. Lack of pre-pandemic data makes it difficult to assess whether inequalities worsened during COVID-19.

Second, missing income data from respondents who chose not to disclose may have introduced bias. Approximately 10% of respondents did not report their household income and were therefore excluded from the income-based analyses. Because income non-response may be systematically related to sociodemographic or health characteristics, this exclusion may introduce bias and potentially distort the magnitude of observed income-related inequalities in HRQoL. Although multiple imputation could, in principle, offer a more robust way of addressing missing income, implementing a unified imputation model was complicated by substantial cross-country differences in income categorization, response patterns, and the cultural sensitivity of income reporting. To maintain comparability across countries, we opted for a complete-case approach but acknowledge that future studies should consider advanced missing data techniques, such as multiple imputation, to enhance the robustness of income-related analyses.

A third limitation concerns the online recruitment strategy, which relied on a market research agency. Although this approach enabled rapid data collection during the early phase of the pandemic, it may have introduced selection bias, particularly in countries like China, where the sample skewed younger and healthier. Individuals who join online survey panels tend to be younger, more digitally literate, and may have higher socioeconomic status compared with the general population. As a result, certain groups—such as older adults, people with limited internet access, or individuals with lower literacy levels—may be underrepresented. This potential sampling bias could affect the generalizability of our findings, particularly with regard to the magnitude of socioeconomic inequalities in HRQoL.

Another limitation concerns the operationalization of SES, in particular work status. To ensure sufficient sample sizes across categories, we collapsed several work status groups (i.e., respondents who were employed, students and retirees), which may have obscured important distinctions between different forms of employment and non-employment. Moreover, differences in how countries conceptualize employment, particularly for students and retirees, may comparability and interpretation.

A further limitation of this study is the use of the EQ-5D-5L LSS rather than utility values. Although the LSS provides a simple and transparent summary of respondents’ health states, it is not directly comparable to utility scores derived from country-specific value sets. Utility values are widely used in health economics for cost-utility analyses, and substituting the LSS limits comparability with studies that employ standard EQ-5D utilities. This reduces the extent to which our findings can be integrated into economic evaluation frameworks and cross-study comparisons in the health economics literature.

Cultural differences in self-reporting EQ-5D-5L and EQ VAS may also have influenced outcomes, warranting further investigation.

A final limitation relates to the COVID-19 pandemic during which the data were collected. The pandemic may have temporarily altered socioeconomic conditions and HRQoL, raising questions about the generalizability of our findings over time. Moreover, our analysis does not fully account for alternative macro-level factors that may contribute to cross-country differences, such as variations in health system resilience, welfare state structures, and national COVID-19 response strategies. These institutional and policy environments likely shaped countries’ capacity to buffer populations from healthcare disruptions, income loss, and wider social consequences, potentially influencing the magnitude of observed SES-related disparities. Nevertheless, the relative socioeconomic gradients we identify align with longstanding evidence on health inequalities, suggesting they reflect deeper structural mechanisms rather than pandemic-specific effects. Still, because absolute HRQoL levels and the extent of inequalities may evolve as countries recover, future studies incorporating post-pandemic data and explicit contextual indicators will be essential to assess the persistence, change, and drivers of these cross-country patterns.

## Conclusions

Health inequalities in HRQoL during the COVID-19 pandemic were evident in China, the Netherlands, Sweden, the UK, and the US, with the UK showing the greatest disparities. Education and income were similarly associated with HRQoL, but work status appeared to be a more powerful predictor. Although the cross-sectional design limits causal interpretation, the consistent SES-related gradients observed across diverse contexts highlight persistent structural. These findings reinforce the need for governments to prioritize policies that reduce socioeconomic vulnerability, such as strengthening income protection, improving employment security, and expanding access to education and social support.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

<div class="caption">

Supplementary Material 2

</div>

## Author contributions

All authors contributed to the design of the study. JAH, MFJ, EIL designed the questionnaire and collected the data. Data analysis was performed by JE and JAH. JMB and YSF provided input on the statistical models and interpretation of results. JE and JAH wrote the first draft of the manuscript. All authors reviewed and revised the manuscript. All authors read and approved the final version of the manuscript before submission and agree to be accountable for all aspects of the work.

## Funding

This work was supported by the EuroQol Research Foundation (grant numbers 77-2020-RA; 238-2020RA and 460-RA).

## Data availability

Data is available upon reasonable request.

## Declarations

### Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest. YSF, MFJ, EIL and JAH are members of the EuroQol Group. Views expressed by the authors in the publication do not necessarily reflect those of the EuroQol Group.

### Ethical approval

Ethical approval for the POPCORN study was obtained from the Erasmus MC ethics review board (approval MEC-2020-0266).

## Footnotes

## References

## References

1. World Health Organisation. (2005). Constitution of the World Health Organisation. Retrieved 02 April, 2024, from https://www.who.int/about/accountability/governance/constitution

2. Marmot, M., Friel, S., Bell, R., Houweling, T. A., Taylor, S., Commission on Social Determinants of, H. (2008). Closing the gap in a generation: Health equity through action on the social determinants of health. Lancet,372(9650), 1661–1669. doi:10.1016/S0140-6736(08)61690-6

3. Ye, Y., Long, C., Chua, K. C., Moreno-Agostino, D., & Prina, M. (2026). Socio-economic position and healthy ageing across the life course: a systematic review of longitudinal studies. Geroscience. doi:10.1007/s11357-026-02277-w

4. D. M. Cutler, A. Lleras-Muney, & Vogl, T. (2012). Socioeconomic Status and Health: Dimensions and Mechanisms. In S. Glied & P. C. Smith (Eds.), The Oxford Handbook of Health Economics (pp. 124–163): Oxford University Press.

5. Adler, N. E., & Newman, K. (2002). Socioeconomic disparities in health: Pathways and policies. Health Affairs (Project HOPE),21(2), 60–76. doi:10.1377/hlthaff.21.2.60

6. Solar, O., & Irwin, A. (2010). A Conceptual Framework for Action on the Social Determinats of Health. Social Determinants of Health Discussion Paper 2 (Policy and Practice).

7. Mackenbach, J. P., Stirbu, I., Roskam, A. J., Schaap, M. M., Menvielle, G., Leinsalu, M., Kunst, A. E., European Union Working Group on Socioeconomic Inequalities in, H. (2008). Socioeconomic inequalities in health in 22 European countries. The New England Journal of Medicine,358(23), 2468–2481. doi:10.1056/NEJMsa0707519

8. Zajacova, A., Jehn, A., Stackhouse, M., Denice, P., & Ramos, H. (2020). Changes in health behaviours during early COVID-19 and socio-demographic disparities: A cross-sectional analysis. Canadian Journal of Public Health,111(6), 953–962. doi:10.17269/s41997-020-00434-y

9. OECD. (2020). OECD Employment Outlook 2020: Worker security and the COVID-19 crisis. OECD Publishing.

10. Khanijahani, A., Iezadi, S., Gholipour, K., Azami-Aghdash, S., & Naghibi, D. (2021). A systematic review of racial/ethnic and socioeconomic disparities in COVID-19. International Journal for Equity in Health,20(1), Article 248. doi:10.1186/s12939-021-01582-4

11. Hawkins, R. B., Charles, E. J., & Mehaffey, J. H. (2020). Socio-economic status and COVID-19-related cases and fatalities. Public Health,189, 129–134. doi:10.1016/j.puhe.2020.09.016

12. Marmot, M., Allen, J., Bell, R., Bloomer, E., Goldblatt, P., Consortium for the European Review of Social Determinants of, H., the Health, D. (2012). WHO European review of social determinants of health and the health divide. Lancet (London, England),380(9846), 1011–1029. doi:10.1016/S0140-6736(12)61228-8

13. Szende, A., Janssen, M. F., Cabases, J., Ramos-Goni, J. M., & Burström, K. (2022). Socio-demographic indicators of self-reported health based on EQ-5D-3L: A cross-country analysis of population surveys from 18 countries. Frontiers in Public Health,10, Article 959252. doi:10.3389/fpubh.2022.959252

14. Lindberg, M. H., Chen, G., Olsen, J. A., & Abelsen, B. (2022). Combining education and income into a socioeconomic position score for use in studies of health inequalities. BMC Public Health,22(1), 969. doi:10.1186/s12889-022-13366-8

15. Albert-Ballestar, S., & García-Altés, A. (2021). Measuring health inequalities: A systematic review of widely used indicators and topics. International Journal for Equity in Health,20(1), 73. doi:10.1186/s12939-021-01397-3

16. Lynch, J. W., Smith, G. D., Kaplan, G. A., & House, J. S. (2000). Income inequality and mortality: Importance to health of individual income, psychosocial environment, or material conditions. BMJ,320(7243), 1200–1204. doi:10.1136/bmj.320.7243.1200

17. Subramanian, S. V., & Kawachi, I. (2004). Income inequality and health: What have we learned so far? Epidemiologic Reviews,26(1), 78–91. doi:10.1093/epirev/mxh003

18. Psaki, S. R., Seidman, J. C., Miller, M., Gottlieb, M., Bhutta, Z. A., Ahmed, T., Ahmed, A. S., Bessong, P., John, S. M., Kang, G., Kosek, M., Lima, A., Shrestha, P., Svensen, E., Checkley, W., & Investigators, M.-E.N. (2014). Measuring socioeconomic status in multicountry studies: Results from the eight-country MAL-ED study. Population Health Metrics,12(1), 8. doi:10.1186/1478-7954-12-8

19. Spronk, I., Haagsma, J. A., Lubetkin, E. I., Polinder, S., Janssen, M. F., & Bonsel, G. J. (2021). Health inequality analysis in Europe: Exploring the potential of the EQ-5D as outcome. Frontiers in Public Health,9, Article 744405. doi:10.3389/fpubh.2021.744405

20. Brooks, R., Boye, K. S., & Slaap, B. (2020). EQ-5D: A plea for accurate nomenclature. The Journal of Patient-Reported Outcomes,4(1), 52. doi:10.1186/s41687-020-00222-9

21. Szende A, J. B., Cabases J. (2014). Self-Reported Population Health: An International Perspective based on EQ-5D. Retrieved 25 April, 2024, 2024, from https://www.ncbi.nlm.nih.gov/books/NBK500356/

22. Long, D., Haagsma, J. A., Janssen, M. F., Yfantopoulos, J. N., Lubetkin, E. I., & Bonsel, G. J. (2021). Health-related quality of life and mental well-being of healthy and diseased persons in 8 countries: Does stringency of government response against early COVID-19 matter? SSM - Population Health,15, Article 100913. doi:10.1016/j.ssmph.2021.100913

23. Herdman, M., Gudex, C., Lloyd, A., Janssen, M., Kind, P., Parkin, D., Bonsel, G., & Badia, X. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research : An International Journal of Quality of Life Aspects, Concepts and Related Measures,20(10), 1727–1736. doi:10.1007/s11136-011-9903-x

24. IBM, C. (2021). IBM SPSS Statistics for Windows (Version 28.0).

25. Li, H., Wei, X., Ma, A., & Chung, R. Y. (2014). Inequalities in health status among rural residents: EQ-5D findings from household survey China. International Journal for Equity in Health,13, 41. doi:10.1186/1475-9276-13-41

26. Teni, F. S., Gerdtham, U. G., Leidl, R., Henriksson, M., Åström, M., Sun, S., & Burström, K. (2022). Inequality and heterogeneity in health-related quality of life: Findings based on a large sample of cross-sectional EQ-5D-5L data from the Swedish general population. Quality of Life Research : An International Journal of Quality of Life Aspects, Concepts and Related Measures,31(3), 697–712. doi:10.1007/s11136-021-02982-3

27. Singh-Manoux, A., Clarke, P., & Marmot, M. (2002). Multiple measures of socio-economic position and psychosocial health: Proximal and distal measures. International Journal of Epidemiology,31(6), 1192–1199. doi:10.1093/ije/31.6.1192

28. Robert, S., & House, J. S. (1996). SES differentials in health by age and alternative indicators of SES. Journal of Aging and Health,8(3), 359–388. doi:10.1177/089826439600800304

29. Mather, T., Banks, E., Joshy, G., Bauman, A., Phongsavan, P., & Korda, R. J. (2014). Variation in health inequalities according to measures of socioeconomic status and age. Australian and New Zealand Journal of Public Health,38(5), 436–440. doi:10.1111/1753-6405.12239

30. Darin-Mattsson, A., Fors, S., & Kåreholt, I. (2017). Different indicators of socioeconomic status and their relative importance as determinants of health in old age. International Journal for Equity in Health,16(1), 173. doi:10.1186/s12939-017-0670-3

31. Vahid Shahidi, F., Muntaner, C., Shankardass, K., Quiñonez, C., & Siddiqi, A. (2018). Widening health inequalities between the employed and the unemployed: A decomposition of trends in Canada (2000–2014). PLoS ONE,13(11), Article e0208444. doi:10.1371/journal.pone.0208444

32. Farrants, K., Bambra, C., Nylen, L., Kasim, A., Burstrom, B., & Hunter, D. (2016). Recommodification, unemployment, and health inequalities: Trends in England and Sweden 1991–2011. International Journal of Health Services,46(2), 300–324. doi:10.1177/0020731416637829

33. Kroll, L. E., & Lampert, T. (2011). Changing health inequalities in Germany from 1994 to 2008 between employed and unemployed adults. International Journal of Public Health,56(3), 329–339. doi:10.1007/s00038-011-0233-0

34. van der Noordt, M., H, I. J., Droomers, M., & Proper, K. I. (2014). Health effects of employment: A systematic review of prospective studies. Occupational and Environmental Medicine,71(10), 730–736. doi:10.1136/oemed-2013-101891

35. Chowdhury, R., Shah, D., & Payal, A. R. (2017). Healthy worker effect phenomenon: Revisited with emphasis on statistical methods - A review. Indian Journal of Occupational and Environmental Medicine,21(1), 2–8. doi:10.4103/ijoem.IJOEM_53_16

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary Material 1

</div>

<div class="caption">

Supplementary Material 2

</div>

### Data Availability Statement

Data is available upon reasonable request.

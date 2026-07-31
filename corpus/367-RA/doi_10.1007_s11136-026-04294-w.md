---
project_id: "367-RA"
work_id: "doi:10.1007/s11136-026-04294-w"
doi: "10.1007/s11136-026-04294-w"
pmid: "42295447"
pmcid: "PMC13269496"
title: "Measuring inequality in quality of life: further evidence that the EQ-5D-5L may underestimate it"
journal: "Quality of Life Research"
publication_date: "2026-06-15"
volume: "35"
issue: "8"
authors:
  - name: "Admassu N. Lamu"
    orcid: "http://orcid.org/0000-0001-6638-421X"
    affiliation_ids:
      - "Aff1"
  - name: "Gang Chen"
    orcid: "http://orcid.org/0000-0002-8385-5965"
    affiliation_ids:
      - "Aff2"
  - name: "Ling Jie Cheng"
    orcid: "http://orcid.org/0000-0002-5338-578X"
    affiliation_ids:
      - "Aff3"
      - "Aff4"
  - name: "Jan Abel Olsen"
    orcid: "http://orcid.org/0000-0001-9472-2669"
    affiliation_ids:
      - "Aff5"
affiliations:
  - id: "Aff1"
    name: "A Lamu Consulting, Bergen, Norway"
  - id: "Aff2"
    name: "https://ror.org/01ej9dk98grid.1008.90000 0001 2179 088XCancer Health Services Research Unit, University of Melbourne, Melbourne, Australia"
  - id: "Aff3"
    name: "https://ror.org/052gg0110grid.4991.50000 0004 1936 8948National Perinatal Epidemiology Unit, Nuffield Department of Women’s & Reproductive Health, University of Oxford, Oxford, United Kingdom"
  - id: "Aff4"
    name: "https://ror.org/01tgyzw49grid.4280.e0000 0001 2180 6431Alice Lee Centre for Nursing Studies, Yong Loo Lin School of Medicine, National University of Singapore, Singapore, Singapore"
  - id: "Aff5"
    name: "https://ror.org/00wge5k78grid.10919.300000 0001 2259 5234Department of Community Medicine, UiT The Arctic University of Norway, Tromsø, Norway"
keywords:
  - "EQ VAS"
  - "EQ-5D-5L"
  - "EQ-DAPHNIE"
  - "Health inequality"
  - "Health-related quality of life"
  - "Socioeconomic gradient"
licence: "cc-by"
source_file: "input/projects/367-RA/papers/doi_10.1007_s11136-026-04294-w.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13269496/fullTextXML"
source_method: "epmc_xml"
source_sha256: "96ac5b9ba5f71c9e71fb8a5be43c2ff855739e1bf0396e4538ee523b2e0d413e"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Measuring inequality in quality of life: further evidence that the EQ-5D-5L may underestimate it

## Abstract

### Purpose

A previous study found that individuals with identical EQ-5D-5L profiles reported systematically higher EQ VAS scores with increasing educational attainment, which suggests a ‘hidden’ socioeconomic gradient not captured by the EQ-5D-5L. This study examines the robustness and generalisability of these findings using multi-country data.

### Methods

We analysed data from 32,327 respondents aged 25 to 79 years across eight high-income countries: Australia, Canada, France, Germany, the Netherlands, New Zealand, the UK, and the US. The data came from the EQ-DAPHNIE study. Within ten selected EQ-5D-5L health profiles, we used linear regression models to estimate the associations between EQ VAS scores and educational attainment or subjective income status, adjusting for age, sex, and country.

### Results

We observed a consistent educational gradient in EQ VAS scores across most EQ-5D-5L profiles. Tertiary education was associated with higher scores in all ten profiles, with effects statistically significant at *p* \< 0.10 in seven, of which four at *p* \< 0.01. Income status showed an even stronger gradient, with significant associations in nine of the ten profiles. These patterns were evident in all eight countries.

### Conclusion

These multi-country findings provide robust evidence of a socioeconomic gradient in EQ VAS scores among respondents who report identical EQ-5D-5L health profiles, over and above what is reflected in the five EQ-5D-5L dimensions. This pattern has implications for the use of EQ-5D-5L values in equity-informative health technology assessment and population health monitoring.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-026-04294-w.

## Introduction

Health-related quality of life instruments such as the EQ-5D-5L are widely used in health technology assessment, clinical trials, and population health monitoring \[1\]. They characterise health by asking respondents to report problems across a fixed set of dimensions: in the EQ-5D-5L, these are mobility, self-care, usual activities, pain or discomfort, and anxiety or depression. Respondents are also asked to rate their overall health on a visual analogue scale (EQ VAS). The five descriptive dimensions were selected to represent aspects of health that are common across populations, rather than to capture socioeconomic circumstances directly. Nevertheless, when respondents from different socioeconomic groups classify themselves in the same EQ-5D-5L health profile, any remaining systematic differences in their EQ VAS scores may provide insight into both the content coverage of the descriptive system and the way individuals use the response scales.

A longstanding literature in health economics and epidemiology has shown that self-reported health is susceptible to reporting heterogeneity: respondents with different characteristics may use the same response options in systematically different ways, even when their underlying health is similar \[2, 3\]. Analyses using anchoring vignettes, for example, show that correcting for reporting differences can materially change estimated health disparities by socioeconomic status \[2, 3\]. A complementary strand of work has examined whether the EQ-5D descriptive system omits dimensions relevant to Health-related quality of life, particularly psychosocial content, and has assessed the impact of candidate bolt-on items on content validity and discriminatory power \[4–6\]. Together, these strands of research raise the question of whether, within an identical reported EQ-5D-5L profile, EQ VAS scores may still vary systematically by socioeconomic position.

A recently published study showed that individuals with identical EQ-5D-5L profiles reported systematically higher EQ VAS scores with increasing educational attainment \[7\]. These findings suggest either that the use of EQ-5D-5L values may underestimate health inequalities or that a hidden socioeconomic gradient exists that the EQ-5D-5L descriptive system does not capture. However, that study relied on Norwegian data from the Tromsø Study, conducted in a relatively small city \[8\], and on a multi-country survey, the MIC study, in which approximately 80% of participants had chronic conditions \[9\]. These limitations highlight the need for evidence from larger and more diverse populations to assess the robustness and generalisability of the observed pattern.

Against this background, we replicate and extend the analytic approach of Olsen et al. \[7\] using a much larger multi-country dataset, the EQ-DAPHNIE survey \[1\]. In addition to educational attainment, we use *subjective income status* as an alternative indicator of socioeconomic position, motivated by growing evidence that perceived income adequacy captures both economic circumstances and perceived social standing in ways not fully reflected by objective income \[10\]. We assess robustness in two further ways that were not feasible in the earlier study: by examining the distribution of EQ VAS scores within each profile and by conducting country-stratified analyses for the two profiles with sufficient sample sizes across all eight countries.

Therefore, this paper addresses two research questions:

1.  Is there evidence of a ‘hidden’ education–health gradient among respondents who report identical EQ-5D-5L health profiles?

2.  Does a similar pattern emerge when an alternative socioeconomic indicator, such as income status, is used?

## Methods

### Data and study design

We used data from the EuroQol Data for Assessment of Population Health Needs and Instrument Evaluation (EQ-DAPHNIE) study, a cross-sectional online survey of the general adult population aged 18 years and older. We included eight high-income countries: Australia, Canada, France, Germany, the Netherlands, New Zealand, the UK, and the US. Participants were recruited through the online panel provider Dynata (<http://www.dynata.com/>). In each country, the target sample was approximately 4500 respondents. Quota sampling was used to improve representativeness by age, sex, income, region, and language \[1\].

We applied several procedures to ensure data quality and validity across countries, including confirmation of informed consent, consistency checks using duplicated or similar questions, and minimum completion time thresholds \[1, 11\]. In line with previous work \[7\], we excluded respondents younger than 25 years, the expected age of education completion, and those aged over 80 years. We further excluded respondents with implausibly low body mass index (BMI) values as an additional data-quality check; only observations with BMI \> 15 kg/m<sup>2</sup> were retained. After applying all of these data editing procedures, 32,327 observations remained for the final analyses.

### Variables

Educational attainment was reported using country-specific categories and harmonised into three levels to enable cross-country comparability: low (primary or secondary), medium (post-secondary non-tertiary or equivalent), and high (tertiary education, including bachelor’s degree or higher). This classification is consistent with the harmonisation used by Olsen et al. \[7\] and facilitates comparability across the eight countries included in this analysis.

As an alternative indicator of socioeconomic position, we used subjective income status to capture perceived financial adequacy. This measure is particularly relevant in cross-country analyses, in which absolute income levels and purchasing power differ substantially \[12–14\]. Income status was assessed by asking respondents how they felt about their household’s income nowadays, with four response options: comfortable, coping, difficult, and very difficult. Because relatively few respondents selected the lowest category, we combined the last two categories.

For comparability with our previous study \[7\], we examined variation in EQ VAS scores within the same 10 EQ-5D-5L profiles: 11111, 11121, 11122, 21121, 11112, 11221, 11131, 11132, 21231, and 11123. Two of these profiles, 21121 and 11221, were less prevalent in the current dataset.

Health-related quality of life was measured using the EQ VAS, which ranges from 0 (worst imaginable health) to 100 (best imaginable health). To address potential inconsistencies between EQ VAS and EQ-5D-5L responses, we excluded EQ VAS scores below 50 for the full-health profile (11111) and below 30 for all other profiles (Supplementary Table <a href="#MOESM1" data-ref-type="media">S1</a>). These thresholds follow Olsen et al. \[7\] and were intended to remove a small number of responses that were internally inconsistent with the reported EQ-5D-5L profile. Specifically, an EQ VAS score below 50 was considered implausible for respondents reporting full health (11111), and a score below 30 was considered implausible for any of the very mild profiles examined here. The proportion of excluded cases was small, ranging from 0.6 to 3.1% across profiles (Supplementary Table <a href="#MOESM1" data-ref-type="media">S1</a>). Further details of the selected health profiles and the exclusion procedure have been reported elsewhere \[7\].

### Analyses

Before fitting the regression models, we examined the distribution of EQ VAS scores within each of the 10 selected EQ-5D-5L profiles. We computed descriptive statistics, including the mean, standard deviation, median, first and third quartiles, and interquartile range, and inspected combined violin and box plots to assess within-profile skewness and the bounded nature of the EQ VAS scale.

After exploring both linear and alternative semiparametric regression approaches, we found that linear regression models produced results similar to those from more complex specifications, as reported elsewhere \[7\]. Given their simplicity and ease of interpretation, we used linear regression models with survey weights to account for the complex sampling design.

For each EQ-5D-5L profile, we estimated separate regression models with EQ VAS as the dependent variable. Educational attainment was the primary explanatory variable, and models were adjusted for age, sex, and country fixed effects. We conducted corresponding analyses using subjective income status as an alternative indicator of socioeconomic position.

To complement the pooled analyses and assess whether the socioeconomic gradient was also present within countries, we conducted country-stratified regressions for the two profiles with sufficient sample sizes across all eight countries: the full-health profile (11111) and the mildly affected profile (11121). For each country, we fitted separate linear regressions of EQ VAS on educational attainment and, in a parallel specification, on subjective income status, adjusting for age and sex.

Missing data were limited, with the highest proportion observed for EQ VAS (5.8%), followed by educational attainment (2.0%). Assuming that data were missing at random, we used Full Information Maximum Likelihood estimation in the regression analyses. Under this assumption, this approach yields unbiased parameter estimates \[15\]. Following the convention adopted in the parent study \[7\], we report statistical significance at three levels: *p* \< 0.10, *p* \< 0.05, and *p* \< 0.01.

## Results

Table <a href="#Tab1" data-ref-type="table">1</a>and Supplementary Table <a href="#MOESM1" data-ref-type="media">S1</a> present respondent characteristics and the distribution of the most prevalent EQ-5D-5L health profiles. A substantial proportion of respondents had attained tertiary education (44.0%) and reported coping with their current income (40.7%). The 10 selected EQ-5D-5L profiles covered 61% of respondents.

<div id="Tab1" class="table-wrap">

<div class="caption">

Sample characteristics: EQ-DAPHNIE in eight countries, aged 25–79 years

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variable</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">Percent</th>
<th style="text-align: left;">Mean EQ VAS</th>
<th style="text-align: left;">SD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Total sample</td>
<td style="text-align: left;">32,327</td>
<td style="text-align: left;">100.0</td>
<td style="text-align: left;">72.9</td>
<td style="text-align: left;">19.6</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>Sex</em></td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td>17,483</td>
<td>55.0</td>
<td>71.8</td>
<td>19.9</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td>14,490</td>
<td>45.0</td>
<td>74.2</td>
<td>19.0</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>Age category</em></td>
</tr>
<tr>
<td style="text-align: left;">25–40 years</td>
<td>10,405</td>
<td>32.2</td>
<td>74.3</td>
<td>19.0</td>
</tr>
<tr>
<td style="text-align: left;">41–60 years</td>
<td>11,714</td>
<td>36.2</td>
<td>70.9</td>
<td>20.4</td>
</tr>
<tr>
<td style="text-align: left;">61–79 years</td>
<td>10,189</td>
<td>31.5</td>
<td>73.7</td>
<td>18.9</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>Educational attainment</em></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td>10,107</td>
<td>32.0</td>
<td>69.0</td>
<td>21.3</td>
</tr>
<tr>
<td style="text-align: left;">Medium</td>
<td>7573</td>
<td>24.0</td>
<td>71.9</td>
<td>19.8</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td>14,006</td>
<td>44.0</td>
<td>76.1</td>
<td>17.4</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>Income status</em>,<em> n (%)</em></td>
</tr>
<tr>
<td style="text-align: left;">Difficult</td>
<td>9559</td>
<td>30.0</td>
<td>64.4</td>
<td>21.9</td>
</tr>
<tr>
<td style="text-align: left;">Coping</td>
<td>13,167</td>
<td>41.0</td>
<td>73.8</td>
<td>17.7</td>
</tr>
<tr>
<td style="text-align: left;">Comfortable</td>
<td>9467</td>
<td>29.0</td>
<td>80.1</td>
<td>15.9</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>Country</em></td>
</tr>
<tr>
<td style="text-align: left;">Australia</td>
<td>4647</td>
<td>14.0</td>
<td>72.7</td>
<td>19.5</td>
</tr>
<tr>
<td style="text-align: left;">Canada</td>
<td>3952</td>
<td>12.0</td>
<td>71.0</td>
<td>19.4</td>
</tr>
<tr>
<td style="text-align: left;">France</td>
<td>3953</td>
<td>12.0</td>
<td>72.3</td>
<td>19.6</td>
</tr>
<tr>
<td style="text-align: left;">Germany</td>
<td>3940</td>
<td>12.0</td>
<td>73.4</td>
<td>20.3</td>
</tr>
<tr>
<td style="text-align: left;">Netherlands</td>
<td>3927</td>
<td>12.0</td>
<td>74.4</td>
<td>18.5</td>
</tr>
<tr>
<td style="text-align: left;">New Zealand</td>
<td>4013</td>
<td>12.0</td>
<td>75.5</td>
<td>18.2</td>
</tr>
<tr>
<td style="text-align: left;">United Kingdom</td>
<td>4010</td>
<td>12.0</td>
<td>70.6</td>
<td>21.2</td>
</tr>
<tr>
<td style="text-align: left;">United States</td>
<td>3885</td>
<td>12.0</td>
<td>73.2</td>
<td>19.1</td>
</tr>
</tbody>
</table>

Consistent with the previous study, a minimum age of 25 years was chosen to account for the completion of university-level education. Because of variation in the coding across countries, educational attainment was harmonised into three groups: *Low* (primary or secondary school), *Medium* (post-secondary non-tertiary or equivalent), and *High* (all forms of tertiary education from bachelor’s degree and above). *SD*: standard deviation. Row totals may not sum exactly to the total sample size because of missing values on individual variables; percentages are calculated on non-missing cases

</div>

Table <a href="#Tab2" data-ref-type="table">2</a> shows the distribution of EQ VAS scores within each of the 10 EQ-5D-5L profiles. Median EQ VAS scores declined in the expected order across profiles of increasing severity, from 89 (IQR 80–93) in full health (11111) to 69 (IQR 57–75) in the most affected profile (21231). Within-profile distributions were concentrated around the median, with mild left skew, consistent with the upper-bounded nature of the EQ VAS (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

Distribution of EQ VAS scores within each selected EQ-5D-5L profile

</div>

| EQ-5D-5L profile | *n*  | Mean | SD   | Median | Q1   | Q3   | IQR  |
|------------------|------|------|------|--------|------|------|------|
| 11111            | 8569 | 86.1 | 10.3 | 89.0   | 80.0 | 93.0 | 13.0 |
| 11121            | 3323 | 81.1 | 11.6 | 82.0   | 75.0 | 90.0 | 15.0 |
| 11122            | 2435 | 76.3 | 12.2 | 79.0   | 70.0 | 85.0 | 15.0 |
| 21121            | 689  | 78.5 | 12.8 | 80.0   | 71.0 | 89.0 | 18.0 |
| 11112            | 2289 | 79.1 | 12.6 | 80.0   | 71.0 | 89.0 | 18.0 |
| 11221            | 307  | 76.5 | 13.1 | 79.0   | 70.0 | 87.0 | 17.0 |
| 11131            | 444  | 73.2 | 13.8 | 75.0   | 68.0 | 83.0 | 15.0 |
| 11132            | 355  | 70.6 | 12.9 | 70.5   | 62.0 | 80.0 | 18.0 |
| 21231            | 218  | 65.1 | 13.9 | 69.0   | 57.0 | 75.0 | 18.0 |
| 11123            | 869  | 70.3 | 13.2 | 71.0   | 61.0 | 80.0 | 19.0 |

Sample restricted to respondents aged 25–79 years, with body mass index (BMI) \> 15 kg/m<sup>2</sup> and after applying the EQ VAS exclusions described in the Methods (EQ VAS \< 50 for profile 11111 and \< 30 for all other profiles). *SD*: standard deviation; *Q1*: first quartile; *Q3*: third quartile; *IQR*: interquartile range. Within-profile distributions are concentrated around the median, with left-skew consistent with the upper-bounded nature of the EQ VAS

</div>

<figure id="Fig1">
<p><img src="11136_2026_4294_Fig1_HTML.jpg" id="d33e968" /></p>
<figcaption>Distribution of EQ VAS scores by EQ-5D-5L profile: combined violin and box plot. <em>Note</em>: Violin plots show the kernel density estimate of the EQ VAS score distribution within each EQ-5D-5L profile; the width at each EQ VAS value is proportional to the density. Embedded box elements show the median (thick black line), interquartile range (white box), and the remainder of the distribution (thin grey line). The median EQ VAS score for the full-health profile (11111) is higher than for all other profiles, and within-profile distributions are concentrated around the median with mild left-skew consistent with the upper-bounded nature of the EQ VAS. Alternative plots (box plot only; violin and box plot with outliers highlighted) are presented in Supplementary Figs. <a href="#MOESM1" data-ref-type="media">S1</a> and <a href="#MOESM1" data-ref-type="media">S2</a></figcaption>
</figure>

Regression results (Table <a href="#Tab3" data-ref-type="table">3</a>) showed clear socioeconomic gradients in EQ VAS scores across most profiles. Within profile 11121, EQ VAS scores were 0.863 points higher among respondents with medium education and 2.135 points higher among those with high education than among those with low education (Panel A). In the same profile, EQ VAS scores were 2.451 points higher among respondents coping with their income and 4.969 points higher among those living comfortably than among those reporting financial difficulties (Panel B). Overall, higher education was associated with higher EQ VAS scores in all 10 profiles, with seven associations statistically significant at *p* \< 0.10, including four at *p* \< 0.01, while significant income gradients were observed in nine of the 10 profiles.

<div id="Tab3" class="table-wrap">

<div class="caption">

Linear regressions of EQ VAS scores on educational attainment and income status within selected EQ-5D-5L profiles, aged 25–79 years

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Variables</th>
<th colspan="6" style="text-align: left;">Most prevalent profiles</th>
<th colspan="4" style="text-align: left;">Moderate-level profiles</th>
</tr>
<tr>
<th style="text-align: left;">11111</th>
<th style="text-align: left;">11121</th>
<th style="text-align: left;">11122</th>
<th style="text-align: left;">21121</th>
<th style="text-align: left;">11112</th>
<th style="text-align: left;">11221</th>
<th colspan="2" style="text-align: left;">11131</th>
<th style="text-align: left;">11132</th>
<th style="text-align: left;">21231</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11" style="text-align: left;"><strong><em>Panel A: Education gradient in EQ VAS</em></strong></td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Education (ref = Low)</em></td>
</tr>
<tr>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;">1.045***</td>
<td style="text-align: left;">0.863</td>
<td style="text-align: left;">0.467</td>
<td style="text-align: left;">0.381</td>
<td style="text-align: left;">1.507*</td>
<td style="text-align: left;">3.419*</td>
<td colspan="2" style="text-align: left;">2.443</td>
<td style="text-align: left;">− 0.107</td>
<td style="text-align: left;">1.452</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(0.352)</td>
<td style="text-align: left;">(0.558)</td>
<td style="text-align: left;">(0.746)</td>
<td style="text-align: left;">(1.246)</td>
<td style="text-align: left;">(0.812)</td>
<td style="text-align: left;">(1.893)</td>
<td colspan="2" style="text-align: left;">(1.678)</td>
<td style="text-align: left;">(1.972)</td>
<td style="text-align: left;">(2.190)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: left;">1.554***</td>
<td style="text-align: left;">2.135***</td>
<td style="text-align: left;">1.183*</td>
<td style="text-align: left;">0.175</td>
<td style="text-align: left;">2.125***</td>
<td style="text-align: left;">6.489***</td>
<td colspan="2" style="text-align: left;">3.028*</td>
<td style="text-align: left;">0.815</td>
<td style="text-align: left;">4.753*</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(0.295)</td>
<td style="text-align: left;">(0.514)</td>
<td style="text-align: left;">(0.628)</td>
<td style="text-align: left;">(1.213)</td>
<td style="text-align: left;">(0.674)</td>
<td style="text-align: left;">(2.019)</td>
<td colspan="2" style="text-align: left;">(1.719)</td>
<td style="text-align: left;">(1.806)</td>
<td style="text-align: left;">(2.508)</td>
</tr>
<tr>
<td style="text-align: left;">Male (ref = Female)</td>
<td style="text-align: left;">− 0.659***</td>
<td style="text-align: left;">− 1.238***</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.080</td>
<td style="text-align: left;">− 0.470</td>
<td style="text-align: left;">− 0.802</td>
<td colspan="2" style="text-align: left;">0.466</td>
<td style="text-align: left;">− 0.039</td>
<td style="text-align: left;">0.378</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(0.234)</td>
<td style="text-align: left;">(0.414)</td>
<td style="text-align: left;">(0.528)</td>
<td style="text-align: left;">(1.007)</td>
<td style="text-align: left;">(0.564)</td>
<td style="text-align: left;">(1.515)</td>
<td colspan="2" style="text-align: left;">(1.342)</td>
<td style="text-align: left;">(1.519)</td>
<td style="text-align: left;">(1.872)</td>
</tr>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;">75.180***</td>
<td style="text-align: left;">73.913***</td>
<td style="text-align: left;">83.687***</td>
<td style="text-align: left;">47.336***</td>
<td style="text-align: left;">69.145***</td>
<td style="text-align: left;">73.799***</td>
<td colspan="2" style="text-align: left;">67.387***</td>
<td style="text-align: left;">74.819***</td>
<td style="text-align: left;">72.616***</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(1.060)</td>
<td style="text-align: left;">(1.197)</td>
<td style="text-align: left;">(0.560)</td>
<td style="text-align: left;">(6.239)</td>
<td style="text-align: left;">(4.132)</td>
<td style="text-align: left;">(3.049)</td>
<td colspan="2" style="text-align: left;">(3.380)</td>
<td style="text-align: left;">(1.253)</td>
<td style="text-align: left;">(2.072)</td>
</tr>
<tr>
<td style="text-align: left;">R-squared</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.025</td>
<td style="text-align: left;">0.023</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;">0.029</td>
<td style="text-align: left;">0.013</td>
<td colspan="2" style="text-align: left;">0.118</td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;">0.035</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><strong><em>Panel B: Income status gradient in EQ VAS</em></strong></td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Income (ref = Difficult)</em></td>
</tr>
<tr>
<td style="text-align: left;">Coping</td>
<td style="text-align: left;">1.840***</td>
<td style="text-align: left;">2.451***</td>
<td style="text-align: left;">2.125***</td>
<td style="text-align: left;">3.959***</td>
<td style="text-align: left;">1.632**</td>
<td style="text-align: left;">0.764</td>
<td colspan="2" style="text-align: left;">3.780**</td>
<td style="text-align: left;">2.917*</td>
<td style="text-align: left;">5.562**</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(0.352)</td>
<td style="text-align: left;">(0.566)</td>
<td style="text-align: left;">(0.586)</td>
<td style="text-align: left;">(1.368)</td>
<td style="text-align: left;">(0.636)</td>
<td style="text-align: left;">(1.975)</td>
<td colspan="2" style="text-align: left;">(1.654)</td>
<td style="text-align: left;">(1.558)</td>
<td style="text-align: left;">(2.199)</td>
</tr>
<tr>
<td style="text-align: left;">Comfortable</td>
<td style="text-align: left;">4.618***</td>
<td style="text-align: left;">4.969***</td>
<td style="text-align: left;">4.866***</td>
<td style="text-align: left;">4.284***</td>
<td style="text-align: left;">3.149***</td>
<td style="text-align: left;">2.320</td>
<td colspan="2" style="text-align: left;">5.283***</td>
<td style="text-align: left;">1.610</td>
<td style="text-align: left;">8.485***</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(0.345)</td>
<td style="text-align: left;">(0.592)</td>
<td style="text-align: left;">(0.721)</td>
<td style="text-align: left;">(1.450)</td>
<td style="text-align: left;">(0.749)</td>
<td style="text-align: left;">(2.264)</td>
<td colspan="2" style="text-align: left;">(1.869)</td>
<td style="text-align: left;">(2.144)</td>
<td style="text-align: left;">(2.471)</td>
</tr>
<tr>
<td style="text-align: left;">Male (ref = Female)</td>
<td style="text-align: left;">− 0.925***</td>
<td style="text-align: left;">− 1.353***</td>
<td style="text-align: left;">− 0.218</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">− 0.612</td>
<td style="text-align: left;">− 0.770</td>
<td colspan="2" style="text-align: left;">0.116</td>
<td style="text-align: left;">− 0.083</td>
<td style="text-align: left;">0.299</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(0.231)</td>
<td style="text-align: left;">(0.411)</td>
<td style="text-align: left;">(0.526)</td>
<td style="text-align: left;">(0.998)</td>
<td style="text-align: left;">(0.564)</td>
<td style="text-align: left;">(1.548)</td>
<td colspan="2" style="text-align: left;">(1.337)</td>
<td style="text-align: left;">(1.516)</td>
<td style="text-align: left;">(1.839)</td>
</tr>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;">75.207***</td>
<td style="text-align: left;">73.545***</td>
<td style="text-align: left;">82.212***</td>
<td style="text-align: left;">46.390***</td>
<td style="text-align: left;">73.812***</td>
<td style="text-align: left;">71.554***</td>
<td colspan="2" style="text-align: left;">66.740***</td>
<td style="text-align: left;">75.384***</td>
<td style="text-align: left;">73.051***</td>
</tr>
<tr>
<td style="text-align: left;">(SE)</td>
<td style="text-align: left;">(1.029)</td>
<td style="text-align: left;">(1.114)</td>
<td style="text-align: left;">(0.548)</td>
<td style="text-align: left;">(5.930)</td>
<td style="text-align: left;">(4.087)</td>
<td style="text-align: left;">(3.038)</td>
<td colspan="2" style="text-align: left;">(3.216)</td>
<td style="text-align: left;">(1.185)</td>
<td style="text-align: left;">(1.965)</td>
</tr>
<tr>
<td style="text-align: left;">Observations</td>
<td style="text-align: left;">8,569</td>
<td style="text-align: left;">3,323</td>
<td style="text-align: left;">2,435</td>
<td style="text-align: left;">689</td>
<td style="text-align: left;">2,289</td>
<td style="text-align: left;">307</td>
<td colspan="2" style="text-align: left;">444</td>
<td style="text-align: left;">355</td>
<td style="text-align: left;">218</td>
</tr>
<tr>
<td style="text-align: left;">R-squared</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;">0.017</td>
<td colspan="2" style="text-align: left;">0.151</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.071</td>
</tr>
</tbody>
</table>

Entries are linear regression coefficients with robust standard errors in parentheses. Each column is a separate regression for the indicated EQ-5D-5L profile. Dependent variable: EQ VAS score. Panel A reports the model with educational attainment as the primary explanatory variable; Panel B reports the corresponding model with subjective income status. Both models control for age and country dummies (Australia as reference; Canada, France, Germany, the Netherlands, New Zealand, the UK, and the US). Sample sizes and R-squared values apply to both panels within a column and are reported once in Panel B. Educational attainment was harmonised into three levels: *Low* (primary or secondary; reference), *Medium* (post-secondary non-tertiary or equivalent), and *High* (tertiary, bachelor’s degree or higher). Income status: *Difficult* (reference; combined the two lowest categories), *Coping*, *Comfortable*. Significance: \* *p* \< 0.10; \*\* *p* \< 0.05; \*\*\* *p* \< 0.01

</div>

Figure <a href="#Fig2" data-ref-type="fig">2</a> presents predictive margins based on Table <a href="#Tab3" data-ref-type="table">3</a> and shows that these gradients were evident across nearly all profiles for both socioeconomic indicators. The only exception was a small non-significant decline for education in profile 11132. The gradients were steeper for subjective income status than for educational attainment. Country-stratified analyses were restricted to the two profiles (11111 and 11121) that had sufficient sample sizes in all eight countries; results are reported in Supplementary Tables <a href="#MOESM1" data-ref-type="media">S2</a> (profile 11111) and <a href="#MOESM1" data-ref-type="media">S3</a> (profile 11121), and the adjusted income gradient is summarised in Fig. <a href="#Fig3" data-ref-type="fig">3</a>. The income gradient was consistent across countries: for profile 11111, the coefficient for comfortable versus difficult income status was positive and statistically significant at *p* \< 0.05 in all eight countries; for profile 11121, the corresponding coefficient was positive in all eight countries and statistically significant in seven at *p* \< 0.10 (six at *p* \< 0.05). By contrast, the education gradient was more heterogeneous in direction and magnitude across countries.

<figure id="Fig2">
<p><img src="11136_2026_4294_Fig2_HTML.jpg" id="d33e1582" /></p>
<figcaption>Mean EQ VAS by educational attainment and income status within each EQ-5D-5L profile, adjusted for age, sex and country. <em>Note</em>: Points are predictive margins from the linear regression models reported in Table <a href="#Tab3" data-ref-type="table">3</a>, showing the mean EQ VAS score within each EQ-5D-5L profile by level of educational attainment (left panel) or income status (right panel), adjusted for age, sex and country dummies. Educational attainment was harmonised into three levels: <em>Low</em> (primary or secondary), <em>Medium</em> (post-secondary non-tertiary or equivalent), and <em>High</em> (tertiary education, bachelor’s degree or higher)</figcaption>
</figure>

<figure id="Fig3">
<p><img src="11136_2026_4294_Fig3_HTML.jpg" id="d33e1614" /></p>
<figcaption>Country-stratified income gradient in mean EQ VAS within EQ-5D-5L profiles 11111 and 11121, adjusted for age and sex. <em>Note</em>: For each country, the plotted effect is the linear-regression coefficient on <em>Comfortable</em> income status (reference: <em>Difficult</em>), with 95% CIs (coefficient ± 1.96 × robust SE). Full-colour markers indicate <em>p</em> &lt; 0.05; lighter orange (Canada, profile 11121) indicates <em>p</em> &lt; 0.10 only; grey (Netherlands, profile 11121) indicates non-significant. Positive coefficients in all eight countries indicate a consistent within-profile income gradient. Full results in Supplementary Tables <a href="#MOESM1" data-ref-type="media">S2</a> and <a href="#MOESM1" data-ref-type="media">S3</a></figcaption>
</figure>

## Discussion

This multi-country analysis replicates and extends earlier evidence \[7\] that EQ VAS scores are systematically associated with socioeconomic position among respondents who report identical EQ-5D-5L health profiles. In a sample of more than 32,000 adults from eight high-income countries, both educational attainment and subjective income status showed clear positive gradients in EQ VAS scores across most of the 10 profiles examined. The gradient for subjective income status was stronger and more consistent than that for education. This pattern was also robust in country-stratified analyses of the two profiles for which such analyses were feasible. Together, these findings support earlier results from a single Norwegian city \[7, 8\] and from a multi-country survey with a high prevalence of chronic conditions \[9\].

Two broad, non-mutually exclusive explanations are consistent with these findings. First, the five EQ-5D-5L descriptive dimensions may not capture all aspects of health that respondents consider when rating their overall health on the EQ VAS. Dimensions such as vitality, sleep, social relationships, and community connectedness, which have been proposed as psychosocial bolt-ons to the EQ-5D, may be unequally distributed by socioeconomic position \[4–6\]. Under this interpretation, respondents with lower socioeconomic status who classify themselves in the same EQ-5D-5L state as their higher-SES peers may nevertheless experience more problems in domains not captured by the descriptive system, which are then reflected in lower EQ VAS scores. Second, the findings may reflect reporting heterogeneity: individuals from different socioeconomic groups may use the EQ VAS response scale in systematically different ways, as has been shown for several self-rated health measures using anchoring vignettes \[2, 3\]. Although our data cannot distinguish between these mechanisms, both point to the same practical conclusion: EQ-5D-5L descriptive responses alone do not fully summarise socioeconomic differences in overall self-rated health.

The stronger gradient for subjective income status than for education may reflect the fact that perceived income adequacy captures not only material circumstances but also perceived social standing, both of which are independently associated with health outcomes \[10\]. It may also be more directly comparable across countries than either absolute income or nationally coded education categories \[12–14\]. This interpretation is consistent with the greater cross-country stability of the income gradient observed in our analyses.

These findings have two main implications for the use of EQ-5D-5L values. First, in population health monitoring and equity analysis, EQ-5D-5L values are likely to understate socioeconomic disparities in overall self-rated health relative to analyses based on the EQ VAS, and both measures may therefore be worth reporting. Second, in equity-informative health technology assessment, including distributional cost-effectiveness analysis \[16\], the finding that respondents within the same EQ-5D-5L profile still differ systematically in EQ VAS score by socioeconomic position suggests that equity-weighted QALY calculations based on EQ-5D-5L values may miss part of the distributional signal. This does not undermine the use of the EQ-5D-5L in HTA. The descriptive system was not designed to measure socioeconomic circumstances, and its role within a deliberative HTA framework remains well established \[16\]. Rather, our findings strengthen the case for combining EQ-5D-5L values with complementary measures, such as the EQ VAS, selected bolt-on dimensions, or direct indicators of socioeconomic position, when equity is central to the decision problem.

## Strengths and limitations

Our study has several strengths. It uses a large multi-country sample recruited with quota sampling and subject to data-quality controls \[1, 11\]. The analytic design closely mirrors the earlier study, which facilitates comparison \[7\]. It also adds distributional and country-stratified analyses, which strengthen the robustness and generalisability of the conclusions.

Several limitations should be considered. First, the cross-sectional design precludes causal inference. We cannot determine whether lower socioeconomic status leads to poorer self-assessed health or whether unmeasured confounders influence both. Second, recruitment through an online panel may have introduced selection bias, because internet users may differ systematically from the general population in ways related to socioeconomic status and health reporting patterns. Third, perceived income adequacy is a subjective measure and may share psychological determinants with EQ VAS responses, such as optimism, which could inflate the observed associations. The stronger gradient for income status than for education may therefore partly reflect shared measurement properties. Fourth, EQ VAS may be more susceptible to response-style biases associated with socioeconomic position, and our study design cannot distinguish reporting differences from genuine health differences. Fifth, restricting the analysis to eight high-income countries limits generalisability to low- and middle-income settings. Sixth, the country-stratified analyses had limited precision for some estimates. Although the income gradient was directionally consistent across all eight countries for both profiles examined, statistical significance for the moderate profile (11121) was sensitive to the threshold used: the comfortable-versus-difficult income coefficient reached *p* \< 0.05 in six countries, was marginally significant at *p* \< 0.10 in Canada, and was not statistically significant in the Netherlands. Larger country-specific samples would help to clarify the precision of these estimates. Finally, we adopted the EQ VAS exclusion thresholds from Olsen et al. \[7\] to remove internally inconsistent responses. These thresholds should be interpreted as a logical consistency filter rather than a robustness choice: an EQ VAS score below 50 for respondents reporting full health (11111), or below 30 for any of the very mild profiles, is incompatible with the self-reported EQ-5D-5L profile and most plausibly reflects a response error. Retaining such responses would allow a small tail of internally inconsistent values to distort the within-profile mean and attenuate the estimated gradient. The number of affected cases was small (0.6 to 3.1% per profile; Supplementary Table <a href="#MOESM1" data-ref-type="media">S1</a>), and applying the same rule preserves direct comparability with the published benchmark study.

## Conclusion

This study provides robust cross-national evidence of a socioeconomic gradient in overall self-rated health, measured by EQ VAS, among respondents who report identical EQ-5D-5L health profiles. Among these respondents, both educational attainment and, more prominently, income status were systematically associated with higher EQ VAS scores. These findings are consistent with residual health heterogeneity that is not reflected in the five EQ-5D-5L dimensions, and with the hypothesis of reporting heterogeneity by socioeconomic status. They do not imply that the EQ-5D-5L descriptive system fails to capture content it was designed to measure; rather, they describe the relationship between EQ-5D-5L responses and socioeconomic indicators not contained in the descriptive system.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

### Acknowledgements

We would like to acknowledge contributions of the EQ-DAPHNIE Project Team for the methodological design and planning of data collection. The EQ-DAPHNIE Project Team: Principal Investigators: Drs. Jeffrey Johnson (University of Alberta) and M.F. Bas Janssen (EuroQol Research Office); Co-Investigators: Al Sayah (University of Alberta); Bailey (The University of the West Indies), Ghandi (Duke-NUS Medical School), Golicki (Medical University of Warsaw), Gutacker (University of York), Lubetkin (CUNY School of Medicine), Mulhern (University of Technology Sydney), Purba (Universitas Padjadjaran), Scott (University of Cape Town), Sullivan (University of Otago), Viney (University of Technology Sydney), Yang (Guizhou Medical University), Zarate (Merk & Co).

### Author contributions

Admassu N. Lamu: Conceptualisation; Methodology; formal analysis; writing—original draft; writing—review & editing. Gang Chen: Conceptualisation; methodology; writing—review & editing. Ling Jie Cheng: Conceptualisation; methodology; supervision; writing—review & editing. Jan Abel Olsen: Conceptualisation; methodology; supervision; writing—original draft; writing—review & editing.

### Funding

This project was supported by grants from the EuroQol Research Foundation (reference \# 367-RA and 1830-RA). Views expressed by the authors in the publication do not necessarily reflect the views of the EuroQol Foundation.

### Data availability

No datasets were generated or analysed during the current study.

### Declarations

#### Conflict of interest

The authors declare no competing interests.

## References

1. Johnson, J. A., Janssen, M. F., Al Sayah, F., et al. (2025). EuroQol data for assessment of population health needs and instrument evaluation (EQ-DAPHNIE): a study for enhancing population health assessment. Quality of Life Research, 34(12), 3321–3334.40317454 10.1007/s11136-025-03983-2PMC12689827

2. Bago d’Uva, T., van Doorslaer, E., Lindeboom, M., & O’Donnell, O. (2008). Does reporting heterogeneity bias the measurement of health disparities? Health Economics, 17(3), 351–375.17701960 10.1002/hec.1269

3. Dowd, J. B., & Todd, M. (2011). Does self-reported health bias the measurement of health inequalities in U.S adults? Evidence using anchoring vignettes from the Health and Retirement Study. Journals of Gerontology Series B: Psychological Sciences and Social Sciences, 66B(4), 478–489.10.1093/geronb/gbr05021666144

4. Chen, G., & Olsen, J. A. (2020). Filling the psycho-social gap in the EQ-5D: the empirical support for four bolt-on dimensions. Quality of Life Research, 29(11), 3119–3129.32648198 10.1007/s11136-020-02576-5PMC7591404

5. Mulhern, B., Feng, Y., Shah, K., et al. (2022). Criteria for developing, assessing and selecting candidate EQ-5D bolt-ons. Quality of Life Research, 31(10), 3041–3053.35486216 10.1007/s11136-022-03138-7PMC9470642

6. Rencz, F., & Janssen, M. F. (2024). Testing the psychometric properties of 9 bolt-ons for the EQ-5D-5L in a general population sample. Value in Health, 27(7), 943–954.38599517 10.1016/j.jval.2024.03.2195

7. Olsen, J. A., Chen, G., & Lamu, A. (2025). Measuring inequality in quality of life: Why the EQ-5D may underestimate it. Quality Of Life Research, 34(11), 3283–3290.41217656 10.1007/s11136-025-04087-7PMC12681450

8. Hopstock, L. A., Grimsgaard, S., Johansen, H., Kanstad, K., Wilsgaard, T., & Eggen, A. E. (2022). The seventh survey of the Tromsø Study (Tromsø7) 2015–2016: study design, data collection, attendance, and prevalence of risk factors and disease in a multipurpose population-based health survey. Scandinavian Journal of Public Health, 50(7), 919–929.35509230 10.1177/14034948221092294PMC9578102

9. Richardson, J., Khan, M. A., Iezzi, A., & Maxwell, A. (2012). Cross-national comparison of twelve quality of life instruments MIC Paper 1 Background, questions, instruments. https://www.aqol.com.au/papers/researchpaper76.pdf. Accessed on 14 Jan 2026.

10. Galvan, M. J., Payne, B. K., Hannay, J., Georgeson, A. R., & Muscatell, K. A. (2023). What does the MacArthur scale of subjective social status measure? Separating economic circumstances and social status to predict health. Annals of Behavioral Medicine, 57(11), 929–941.37742041 10.1093/abm/kaad054

11. Al Sayah, F., Short, H., Ramos-Goñi, J. M., et al. (2025). Design and implementation of data quality controls in the EQ-DAPHNIE study: insights from the pilot phase and 15-country analysis. Quality of Life Research, 34(12), 3335–3350.41247569 10.1007/s11136-025-04074-yPMC12689740

12. Acton, R. B., White, C. M., Rynard, V. L., & Hammond, D. (2025). Perceived income adequacy versus household income as a measure of socioeconomic status in 6 countries, 2022–2023 International Food Policy Study. Public Health Reports, 140(5–6), 468–476.40832816 10.1177/00333549251358655PMC12367702

13. Litwin, H., & Sapir, E. V. (2009). Perceived income adequacy among older adults in 12 countries: findings from the survey of health, ageing, and retirement in Europe. The Gerontologist, 49(3), 397–406.19386829 10.1093/geront/gnp036PMC2682171

14. Präg, P., Mills, M. C., & Wittek, R. (2016). Subjective socioeconomic status and health in cross-national comparison. Social Science & Medicine, 149, 84–92.26708244 10.1016/j.socscimed.2015.11.044

15. Lee, T., & Shi, D. (2021). A comparison of full information maximum likelihood and multiple imputation in structural equation modeling with missing data. Psychological Methods, 26(4), 466–485.33507765 10.1037/met0000381

16. Cookson, R., Griffin, S., Norheim, O. F., Culyer, A. J., & Chalkidou, K. (2021). Distributional cost-effectiveness analysis comes of age. Value in Health, 24(1), 118–120.33431145 10.1016/j.jval.2020.10.001PMC7813213

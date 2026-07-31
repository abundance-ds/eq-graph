---
project_id: "461-RA"
work_id: "doi:10.1007/s11136-023-03509-8"
doi: "10.1007/s11136-023-03509-8"
pmid: "37682495"
pmcid: "PMC10784346"
title: "Time perspective profile and self-reported health on the EQ-5D"
journal: "Quality of Life Research"
publication_date: "2023-09-08"
volume: "33"
issue: "1"
authors:
  - name: "Fanni Rencz"
    orcid: "http://orcid.org/0000-0001-9674-620X"
    affiliation_ids:
      - "Aff1"
  - name: "Mathieu F. Janssen"
    orcid: "http://orcid.org/0000-0001-6602-6949"
    affiliation_ids:
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/01vxfm326grid.17127.320000 0000 9234 5858Department of Health Policy, Corvinus University of Budapest, 8 Fővám tér, Budapest, 1093 Hungary"
  - id: "Aff2"
    name: "https://ror.org/018906e22grid.5645.20000 0004 0459 992XSection Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Rotterdam, The Netherlands"
keywords:
  - "Cut-point shift"
  - "EQ-5D-5L"
  - "Psychological characteristics"
  - "Response heterogeneity"
  - "Self-reported health"
  - "Time perspective"
licence: "cc-by"
source_file: "input/projects/461-RA/papers/doi_10.1007_s11136-023-03509-8.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10784346/fullTextXML"
source_method: "epmc_xml"
source_sha256: "6359434e47db5c59c9372dd3e3edaeb7a3ac65690aa1e37a897139bdc7b60aea"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Time perspective profile and self-reported health on the EQ-5D

## Abstract

### Objectives

Time perspective (TP) is a psychological construct that is associated with several health-related behaviours, including healthy eating, smoking and adherence to medications. In this study, we aimed to examine the associations of TP profile with self-reported health on the EQ-5D-5L and to detect which domains display response heterogeneity (cut-point shift) for TP.

### Methods

We conducted a secondary analysis of EQ-5D-5L data from a representative general population sample in Hungary (*n* = 996). The 17-item Zimbardo Time Perspective Inventory was used to measure individuals' TP on five subscales: past-negative, past-positive, present-fatalist, present-hedonist and future. The associations between TP subscales and EQ-5D-5L domain scores, EQ VAS and EQ-5D-5L index values were analysed by using partial proportional odds models and multivariate linear regressions.

### Results

Respondents that scored higher on the past-negative and present-fatalist and lower on the present-hedonist and future subscales were more likely to report more health problems in at least one EQ-5D-5L domain (*p* \< 0.05). Adjusting for socio-economic and health status, three EQ-5D-5L domains exhibited significant associations with various TP subscales (usual activities: present-fatalist and future, pain/discomfort: past-negative and future, anxiety/depression: past-negative, present-fatalist, present-hedonist and future). The anxiety/depression domain showed evidence of cut-point shift.

### Conclusions

This study identified response heterogeneity stemming from psychological characteristics in self-reported health on the EQ-5D-5L. TP seems to play a double role in self-reported health, firstly as affecting underlying health and secondly as a factor influencing one’s response behavior. These findings increase our understanding of the non-health-related factors that affect self-reported health on standardized health status measures.

> “*It is far more important to know what person*
>
> *the disease has than what disease the person has*.”
>
> Hippocrates

## Introduction

The belief that psychological dispositions are related to health dates back to Hippocrates (‘the theory of the four humours’) in the 5th century B.C. and has since been generating substantial interest. Over the past decades, an increasing body of evidence demonstrated that personality characteristics are linked to a wide spectrum of health outcomes, including longevity, predicting the development and course of various chronic physical conditions and self-reported health status \[1–4\]. Time perspective (TP) is a psychological construct that describes how one subjectively focuses on the past, present and future \[5\]. Some authors consider it to be a trait, while others argue that it is a flexible cognitive structure that may change over the life course, or in response to life events (e.g. traumatic exposure), psychological interventions or social environment \[5, 6\]. In their seminal work, *Zimbardo and Boyd* distinguished two main aspects of TP, the directionality of one’s thoughts towards time (i.e. past, present or future orientation) and their emotional valence (i.e. positive or negative) \[7\]. TP has gained increasing attention in the contexts of health and healthcare over the past 30 years. Prior work suggests that persons with past negative view are more likely to experience depression \[7\], whereas people having a present TP more commonly report using alcohol, drugs, and tobacco \[8\]. Future TP, in contrast, demonstrated a positive effect on medication adherence and negative effect on partaking in risky sexual behaviour \[9, 10\].

A few previous studies using the general population or smaller patient samples identified a relationship between TP and self-reported health as measured by a single item health question, the SF-36, SF-12 and WHOQOL-HIV \[11–15\]. To date, no studies have investigated the association between TP and self-reported health using the EQ-5D*.* The EQ-5D is the most widely used generic preference-accompanied health status measure with a variety of economic (e.g. cost-utility analysis) and non-economic applications (e.g. observational clinical studies, clinical trials, population health surveys and measuring health inequalities) \[16–20\]. Previous streams of research with the EQ-5D mostly concentrated on the associations between self-reported health and certain personality traits and lifestyle-related attitudes. In these studies, self-reporting less health problems was related to conscientiousness and internal locus of control, while neuroticism, openness, type D personality, ‘live-for-today’ and ‘unconfident fatalist’ attitudes were related to reporting more health problems on the EQ-5D \[21–25\].

A major measurement issue related to self-reporting own health is that, in addition to the probable link between different psychological factors and health outcomes; for example, as a result of variation in health behaviours or lifestyle choices, psychological characteristics such as TP profile, may also lead to systematic variations in self-reporting own health across respondents with the same health status. It is therefore possible that two people with different psychological traits and the same health status perceive and rate their health differently. This latter variation is commonly referred to as response heterogeneity \[26\], which may lead to differential item functioning in health status measures \[27\]. Guided by the framework outlined by *Lindeboom and van Doorslaer*, two forms of response heterogeneity may be distinguished: cut-point shift and index shift \[26\]. Cut-point shift occurs when the relative positions of the level thresholds change for certain subgroups of respondents directly influencing the shape of the distribution of responses \[28\]. Index shift refers to a parallel shift in all of the reporting thresholds for certain subgroups of respondents that leads to a shift in the distribution of responses either to the right or left \[28\]. An extensive body of studies provided evidence of the presence of cut-point or index shift in self-reported health mainly using a single health question \[26, 28–30\]; however, none of these have investigated individuals’ psychological characteristics as a source of response heterogeneity in self-reported health.

This study seeks to explore the possible link between individuals’ TP profile and self-reported health on the five dimensions of EQ-5D-5L, EQ VAS and index values. We aim to go beyond merely demonstrating the association between TP and self-reported health by attempting to detect which EQ-5D-5L domains possibly display response heterogeneity for TP. Among the two forms of response heterogeneity, our sample enabled to investigate the presence of cut-point shift. We hypothesized that respondents with future, present-hedonistic and past-positive TP reported fewer health problems and respondents with present-fatalistic and past-negative TP reported more health problems \[11, 12\]. We expected that the pain/discomfort and anxiety/depression domains would be more likely to exhibit response heterogeneity for TP given the more subjective nature of these domains \[31\].

## Methods

### Study design and population

We conducted a secondary analysis of the cross-sectional data of the EQ-5D-Y-3L (youth) valuation study in Hungary \[32\]. Respondents were recruited from a large online panel in April and May 2021. The target population for the online panel survey was the Hungarian adult general population aged 18 years or over, and quota sampling methods were used to achieve a representative sample in terms of gender and age (across seven age groupings: 18–24, 25–34, 35–44, 45–54, 55–64, 65–74 and 75+). Ethical approval to conduct the data collection was granted by the Research Ethics Committee of the Corvinus University of Budapest (no. KRH/31/2021). All respondents entering the survey were asked to provide informed consent. To ensure high quality of DCE responses, two quality control criteria were used in the survey regarding completion time and dominant pairs \[32\]. Respondents that failed to meet either one or both of these quality control criteria were excluded and did not continue with the remaining sections of the survey. Participants that successfully met both quality control criteria proceeded to complete the EQ-5D-5L, 17-item Zimbardo Time Perspective Inventory (ZTPI) and socio-demographic and health-related questions in a fixed order. For the latter, a list of 12 common chronic health conditions was provided for respondents. The question specifically asked respondents to report those health conditions that had been diagnosed by a physician.

### EQ-5D-5L

The EQ-5D-5L is a generic preference-accompanied health status measure that comprises two parts, a descriptive system and a vertical visual analogue scale (EQ VAS) ranging from ‘the worst imaginable health state’ (0) to ‘the best imaginable health state’ (100) \[33\]. The descriptive system is composed of the following five health domains: mobility, self-care, usual activities, pain/discomfort and anxiety/depression. Each domain has five response levels: no problems (1), slight problems (2), moderate problems (3), severe problems (4) and extreme problems/unable to (5). These five domains describe overall 3125 unique health profiles, with 11111 being the best (full health) and 55555 being the worst possible health state (pits). Index values (i.e. utilities) may be assigned to each profile using a value set that reflects societal preferences. In this study, we computed index values using the Hungarian EQ-5D-5L value set that had been developed using composite time trade-off method \[34\].

### 17-item Zimbardo Time Perspective Inventory (ZTPI)

To measure respondents’ TP profile, we used the validated Hungarian version of the 17-item ZTPI that is a shorter version of the original 56-item questionnaire \[7, 35\]. ZTPI is a multidimensional TP scale that is based on the considerations proposed by *Zimbardo and Boyd* \[7\]. Figure <a href="#Fig1" data-ref-type="fig">1</a> presents the 17 items of the scale, with each being represented by a statement and assessed on a five-point scale with the endpoints of ‘very untrue’ and ‘very true’. Item scores were summed into subscale scores (past-negative, past-positive, present-fatalistic, present-hedonistic and future) following the official scoring of ZTPI (range of subscale scores 1–5, where a higher score indicates more of the trait being measured).

<figure id="Fig1">
<p><img src="11136_2023_3509_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Distribution of responses on the 17-item Zimbardo Time Perspective Scale. Note that the original order of items was reorganised according to subscales for this figure. Figures may not add up to 100% due to rounding</figcaption>
</figure>

### Statistical analyses

There were no missing values as all questions were mandatory in the online survey. Descriptive statistics were used to provide an overview of the characteristics of the study population. Mean, standard deviation (SD), median, interquartile range, minimum and maximum were computed for continuous variables (EQ VAS, EQ-5D-5L index values and each TP subscale).

#### Partial proportional odds models: exploring response heterogeneity

We adopted an analytical strategy that aims to test the equivalence in response level thresholds controlling for a variety of individual characteristics, such as socio-demographics and health status \[26, 29, 30\]. We treated EQ-5D-5L domain scores as ordinal data due to the hierarchy of response levels. The associations between TP subscales and EQ-5D-5L domain scores were analysed using partial proportional odds models \[36\]. The self-care domain was omitted from the analysis due to limited variability of responses. For the other four domains, responses were collapsed into three categories (no problems, slight problems and moderate-to-extreme problems) to account for the low number of respondents reporting severe or extreme health problems. The three categories were divided by two response thresholds: level 1 vs. levels 2–5 (‘no problems’ vs. ‘slight-to-extreme problems’) and levels 1–2 vs. levels 3–5 (‘no or slight problems’ vs. ‘moderate-to-extreme problems’). The five ZTPI subscale scores, four socio-demographic characteristics (age, gender, education, income) and 12 health condition groups were included in the models as independent variables. These latter were considered as proxies for ‘true’ underlying health status. For all independent variables, the proportional odds assumption was tested using Brant test \[37\]. The model was sequentially refitted until no variables complied with this assumption. We report the results as odds ratios (ORs) and their 95% confidence intervals. Independent variables that satisfy the proportional odds assumption have a single OR for both response thresholds. Whereas, independent variables not meeting the proportional odds assumption have different ORs for the threshold of ‘no problems’ vs. ‘slight-to-extreme problems’ relative to ‘no or slight problems’ vs. ‘moderate-to-extreme problems’ providing evidence of response heterogeneity (cut-point shift).

#### Multivariate linear regressions

Multivariate linear regressions were performed to investigate the association between TP subscales and EQ VAS and EQ-5D-5L index values. Two separate regressions were run for both outcomes of interest to explore the contribution of TP profile to the explained variance in EQ VAS and EQ-5D-5L index value. In the first models (‘without TP’), EQ VAS and EQ-5D-5L index were regressed on four socio-demographic variables (age, gender, education, income) and 12 chronic health condition groups. In the second models (‘with TP’), the five ZTPI subscale scores were also added to the regression as independent variables in addition to respondents’ socio-demographic characteristics and chronic conditions. To ease interpretation of the coefficients, ZTPI subscale scores were rescaled to range from 0 to 4 before the regression analyses. The presence of heteroscedasticity was confirmed by the Breusch-Pagan test \[38\]. Robust standard errors were used to correct for any heteroscedasticity. The ‘without TP’ and ‘with TP’ models were compared with regard to the explained variance (*R*<sup>2</sup> statistic). All analyses were performed in Stata 14 and *p*-values \<0.05 were considered statistically significant.

## Results

### Characteristics of the study population

Out of the 1251 participants, 255 (20.4%) did not meet either one or both quality control criteria in the DCE and were consequently excluded from the study. The final sample consisted of 996 respondents and showed an excellent representativeness for gender and age groups. There was a higher proportion of highly educated respondents compared to the adult general population in Hungary (Table <a href="#Tab1" data-ref-type="table">1</a>). The majority reported overall good health status with mean EQ VAS of 78.03 and EQ-5D-5L index of 0.919 (Table <a href="#Tab2" data-ref-type="table">2</a>). Overall, 72, 93, 80, 53 and 67% had no problems with mobility, self-care, usual activities, pain/discomfort and anxiety/depression, and 38% of the sample reported to be in full health (11111).

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of the study population

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Variables</th>
<th style="text-align: left;">Reference population<sup>a</sup></th>
<th colspan="2" style="text-align: left;">Total sample (<em>n</em> = 996)</th>
<th rowspan="2" style="text-align: left;">Variables</th>
<th style="text-align: left;">Reference population<sup>a</sup></th>
<th colspan="2" style="text-align: left;">Total sample (<em>n</em> = 996)</th>
</tr>
<tr>
<th style="text-align: left;">%</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Age (years)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Gender</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 18–24</td>
<td style="text-align: left;">10</td>
<td>103</td>
<td>10</td>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">53</td>
<td>522</td>
<td>52</td>
</tr>
<tr>
<td style="text-align: left;"> 25–34</td>
<td style="text-align: left;">15</td>
<td>157</td>
<td>16</td>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">47</td>
<td>474</td>
<td>48</td>
</tr>
<tr>
<td style="text-align: left;"> 35–44</td>
<td style="text-align: left;">20</td>
<td>195</td>
<td>20</td>
<td style="text-align: left;">Education</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"> 45–54</td>
<td style="text-align: left;">16</td>
<td>167</td>
<td>17</td>
<td style="text-align: left;"> Primary school or less</td>
<td style="text-align: left;">45</td>
<td>219</td>
<td>22</td>
</tr>
<tr>
<td style="text-align: left;"> 55–64</td>
<td style="text-align: left;">17</td>
<td>172</td>
<td>17</td>
<td style="text-align: left;"> Secondary school</td>
<td style="text-align: left;">33</td>
<td>366</td>
<td>37</td>
</tr>
<tr>
<td style="text-align: left;"> 65–74</td>
<td style="text-align: left;">13</td>
<td>134</td>
<td>13</td>
<td style="text-align: left;"> College/university degree</td>
<td style="text-align: left;">31</td>
<td>411</td>
<td>41</td>
</tr>
<tr>
<td style="text-align: left;"> 75+</td>
<td style="text-align: left;">10</td>
<td>68</td>
<td>7</td>
<td style="text-align: left;">EQ-5D-5L domains</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Household’s per capita net monthly income (HUF)</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
<td style="text-align: left;">Mobility</td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 1 (&lt;= 87500.50)</td>
<td style="text-align: left;">n/a</td>
<td>161</td>
<td>16</td>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">n/a</td>
<td>721</td>
<td>72</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 2 (87500.51–131250.25)</td>
<td style="text-align: left;">n/a</td>
<td>154</td>
<td>15</td>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">n/a</td>
<td>198</td>
<td>20</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 3 (131250.26–175000.33)</td>
<td style="text-align: left;">n/a</td>
<td>145</td>
<td>15</td>
<td style="text-align: left;"> Moderate problems - unable to</td>
<td style="text-align: left;">n/a</td>
<td>77</td>
<td>8</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 4 (175000.34–225000.33)</td>
<td style="text-align: left;">n/a</td>
<td>165</td>
<td>17</td>
<td style="text-align: left;">Self-care</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 5 (225000.34+)</td>
<td style="text-align: left;">n/a</td>
<td>162</td>
<td>16</td>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">n/a</td>
<td>930</td>
<td>93</td>
</tr>
<tr>
<td style="text-align: left;"> Don't know/refused to answer</td>
<td style="text-align: left;">n/a</td>
<td>209</td>
<td>21</td>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">n/a</td>
<td>44</td>
<td>4</td>
</tr>
<tr>
<td style="text-align: left;">Chronic health conditions<sup>b,c</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"> Moderate problems - unable to</td>
<td style="text-align: left;">n/a</td>
<td>22</td>
<td>2</td>
</tr>
<tr>
<td style="text-align: left;"> None</td>
<td style="text-align: left;">52</td>
<td>461</td>
<td>46</td>
<td style="text-align: left;">Usual activities</td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"> Allergy</td>
<td style="text-align: left;">15</td>
<td>160</td>
<td>16</td>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">n/a</td>
<td>800</td>
<td>80</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety</td>
<td style="text-align: left;">n/a</td>
<td>78</td>
<td>8</td>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">n/a</td>
<td>146</td>
<td>15</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma</td>
<td style="text-align: left;">5</td>
<td>56</td>
<td>6</td>
<td style="text-align: left;"> Moderate - extreme problems</td>
<td style="text-align: left;">n/a</td>
<td>50</td>
<td>5</td>
</tr>
<tr>
<td style="text-align: left;"> Cancer</td>
<td style="text-align: left;">2</td>
<td>33</td>
<td>3</td>
<td style="text-align: left;">Pain/discomfort</td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Cardiovascular disease</td>
<td style="text-align: left;">&gt;8</td>
<td>120</td>
<td>12</td>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">n/a</td>
<td>526</td>
<td>53</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td style="text-align: left;">8</td>
<td>53</td>
<td>5</td>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">n/a</td>
<td>380</td>
<td>38</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes</td>
<td style="text-align: left;">9</td>
<td>103</td>
<td>10</td>
<td style="text-align: left;"> Moderate - extreme problems</td>
<td style="text-align: left;">n/a</td>
<td>90</td>
<td>9</td>
</tr>
<tr>
<td style="text-align: left;"> Gastrointestinal disease</td>
<td style="text-align: left;">n/a</td>
<td>75</td>
<td>8</td>
<td style="text-align: left;">Anxiety/depression</td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Hypertension</td>
<td style="text-align: left;">31</td>
<td>305</td>
<td>31</td>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">n/a</td>
<td>664</td>
<td>67</td>
</tr>
<tr>
<td style="text-align: left;"> Musculoskeletal disease</td>
<td style="text-align: left;">&gt;20</td>
<td>239</td>
<td>24</td>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">n/a</td>
<td>250</td>
<td>25</td>
</tr>
<tr>
<td style="text-align: left;"> Osteoporosis</td>
<td style="text-align: left;">6</td>
<td>30</td>
<td>3</td>
<td style="text-align: left;"> Moderate - extreme problems</td>
<td style="text-align: left;">n/a</td>
<td>82</td>
<td>8</td>
</tr>
<tr>
<td style="text-align: left;"> Skin disease</td>
<td style="text-align: left;">n/a</td>
<td>78</td>
<td>8</td>
<td style="text-align: left;">11111 (full health)</td>
<td style="text-align: left;">n/a</td>
<td>378</td>
<td>38</td>
</tr>
</tbody>
</table>

<sup>a</sup>Reference values: Hungarian Central Statistical Office: Microcensus 2016

<sup>b</sup>Reference values: Hungarian Central Statistical Office: Health at a glance, 2019

<sup>c</sup>*n*=19 don’t know/refused to answer

Figures may not add up 100% due to rounding. n/a = not available

</div>

<div id="Tab2" class="table-wrap">

<div class="caption">

Descriptive statistics of EQ VAS, EQ-5D-5L index and ZTPI subscale scores

</div>

| Measure | Theoretical range | Observed range | Mean | SD | Median | Q1–Q3 |
|----|----|----|----|----|----|----|
| EQ VAS | 0–100 | 1–100 | 78.03 | 17.22 | 81 | 70–90 |
| EQ-5D-5L index | −0.848 to 1 | −0.393 to 1 | 0.919 | 0.130 | 0.957 | 0.907–1 |
| ZTPI future | 1–5 | 1.75–5 | 3.89 | 0.55 | 4.00 | 3.50–4.25 |
| ZTPI present-fatalistic | 1–5 | 1–5 | 2.94 | 0.83 | 3.00 | 2.33–3.58 |
| ZTPI present-hedonistic | 1–5 | 1–5 | 2.65 | 0.78 | 2.67 | 2.00–3.00 |
| ZTPI past-positive | 1–5 | 1–5 | 3.40 | 0.81 | 3.33 | 3.00–4.00 |
| ZTPI past-negative | 1–5 | 1.5–4.5 | 2.88 | 0.50 | 3.00 | 2.50–3.25 |

*EQ VAS* EuroQol visual analogue scale, *ZTPI* 17-item Zimbardo Time Perspective Inventory

</div>

The distribution of responses on each ZTPI item is presented in Fig. <a href="#Fig1" data-ref-type="fig">1</a>. The item ‘I meet my obligations to friends and authorities on time’ received the highest proportion of affirmative responses (true or very true: 88%), while the disapproval rate (very untrue or untrue) was the highest for the statement ‘I’ve taken my share of abuse and rejection in the past’ (60%). With respect to TP subscales, the highest mean scores were found for the future subscale (3.89), followed by the past-positive (3.40), while the lowest were observed for the present-hedonistic subscale (2.65) (Table <a href="#Tab2" data-ref-type="table">2</a>).

### The association between EQ-5D-5L domain responses and TP

As hypothesized, after adjusting for socio-demographic characteristics and health status, respondents that scored higher on the past-negative and present-fatalistic and lower on the present-hedonistic and future subscales were more likely to report more health problems in at least one EQ-5D-5L domain (Table <a href="#Tab3" data-ref-type="table">3</a>). Three EQ-5D-5L domains exhibited significant associations with various TP subscales (usual activities: present-fatalistic and future \[range ORs: 0.60–1.26\], pain/discomfort: past-negative and future \[range of ORs: 0.69–1.47\], anxiety/depression: past-negative, present-fatalistic, present-hedonistic and future \[range of ORs: 0.42–2.05\]). The mobility domain showed no association with TP profile.

<div id="Tab3" class="table-wrap">

<div class="caption">

Partial proportional odds models of the association between time perspective and EQ-5D-5L domains (odds ratio and 95% CI)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Mobility</th>
<th style="text-align: left;">Usual activities</th>
<th style="text-align: left;">Pain/discomfort</th>
<th style="text-align: left;">Anxiety/depression</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">0.05 (0.01–0.31)**</td>
<td style="text-align: left;">0.24 (0.03–1.79)</td>
<td style="text-align: left;">0.44 (0.09–2.01)</td>
<td style="text-align: left;">0.20 (0.04–1.12)</td>
</tr>
<tr>
<td style="text-align: left;">Time perspective (ZTPI subscales)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Future</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">0.76 (0.56–1.02)</td>
<td rowspan="2" style="text-align: left;">0.60 (0.43–0.84)**</td>
<td rowspan="2" style="text-align: left;">0.69 (0.54–0.89)**</td>
<td style="text-align: left;">0.75 (0.57–0.99)*</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">0.42 (0.26–0.69)**</td>
</tr>
<tr>
<td style="text-align: left;"> Present-hedonistic</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">0.98 (0.79–1.22)</td>
<td rowspan="2" style="text-align: left;">1.00 (0.79–1.28)</td>
<td rowspan="2" style="text-align: left;">0.96 (0.8–1.15)</td>
<td style="text-align: left;">0.90 (0.73–1.10)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">0.58 (0.40–0.86)**</td>
</tr>
<tr>
<td style="text-align: left;"> Present-fatalistic</td>
<td style="text-align: left;">1.14 (0.93–1.4)</td>
<td style="text-align: left;">1.26 (1.00–1.58)*</td>
<td style="text-align: left;">1.14 (0.96–1.35)</td>
<td style="text-align: left;">1.59 (1.31–1.92)***</td>
</tr>
<tr>
<td style="text-align: left;"> Past-positive</td>
<td style="text-align: left;">1.11 (0.89–1.39)</td>
<td style="text-align: left;">1.09 (0.85–1.39)</td>
<td style="text-align: left;">1.05 (0.88–1.25)</td>
<td style="text-align: left;">0.96 (0.80–1.16)</td>
</tr>
<tr>
<td style="text-align: left;"> Past-negative</td>
<td style="text-align: left;">1.07 (0.76–1.49)</td>
<td style="text-align: left;">0.89 (0.62–1.29)</td>
<td style="text-align: left;">1.47 (1.12–1.94)**</td>
<td style="text-align: left;">2.05 (1.51–2.78)***</td>
</tr>
<tr>
<td style="text-align: left;">Age (years)</td>
<td style="text-align: left;">1.03 (1.02–1.04)***</td>
<td style="text-align: left;">1.01 (0.99–1.02)</td>
<td style="text-align: left;">0.99 (0.98–1.00)</td>
<td style="text-align: left;">0.97 (0.96–0.98)***</td>
</tr>
<tr>
<td style="text-align: left;">Gender (ref: male)</td>
<td style="text-align: left;">0.95 (0.68–1.33)</td>
<td style="text-align: left;">1.58 (1.08–2.29)*</td>
<td style="text-align: left;">1.56 (1.19–2.05)**</td>
<td style="text-align: left;">1.27 (0.94–1.71)</td>
</tr>
<tr>
<td style="text-align: left;">Education (ref: primary)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Secondary</td>
<td style="text-align: left;">1.00 (0.66–1.52)</td>
<td style="text-align: left;">0.89 (0.56–1.40)</td>
<td style="text-align: left;">0.76 (0.53–1.09)</td>
<td style="text-align: left;">0.92 (0.61–1.39)</td>
</tr>
<tr>
<td style="text-align: left;"> Tertiary</td>
<td style="text-align: left;">1.00 (0.64–1.56)</td>
<td style="text-align: left;">0.84 (0.52–1.38)</td>
<td style="text-align: left;">0.79 (0.54–1.16)</td>
<td style="text-align: left;">1.02 (0.67–1.57)</td>
</tr>
<tr>
<td style="text-align: left;">Income (ref: quintile 1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 2</td>
<td style="text-align: left;">0.98 (0.58–1.65)</td>
<td style="text-align: left;">0.94 (0.54–1.63)</td>
<td style="text-align: left;">1.35 (0.85–2.15)</td>
<td style="text-align: left;">0.93 (0.56–1.56)</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td style="text-align: left;">0.83 (0.46–1.50)</td>
<td rowspan="2" style="text-align: left;">0.91 (0.50–1.68)</td>
<td rowspan="2" style="text-align: left;">1.60 (0.99–2.60)</td>
<td rowspan="2" style="text-align: left;">1.19 (0.70–2.01)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">1.58 (0.72–3.47)</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 4</td>
<td style="text-align: left;">0.83 (0.47–1.45)</td>
<td style="text-align: left;">0.44 (0.23–0.85)*</td>
<td style="text-align: left;">1.01 (0.63–1.64)</td>
<td style="text-align: left;">0.75 (0.44–1.28)</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 5</td>
<td style="text-align: left;">0.71 (0.39–1.30)</td>
<td style="text-align: left;">0.60 (0.31–1.16)</td>
<td style="text-align: left;">1.31 (0.80–2.16)</td>
<td style="text-align: left;">1.24 (0.72–2.11)</td>
</tr>
<tr>
<td style="text-align: left;"> Don't know/refused to answer</td>
<td style="text-align: left;">0.72 (0.42–1.25)</td>
<td style="text-align: left;">0.58 (0.33–1.05)</td>
<td style="text-align: left;">1.03 (0.66–1.62)</td>
<td style="text-align: left;">0.81 (0.50–1.33)</td>
</tr>
<tr>
<td style="text-align: left;">Chronic conditions (ref: none)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Allergy</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">1.47 (0.95–2.28)</td>
<td rowspan="2" style="text-align: left;">2.09 (1.33–3.27)**</td>
<td style="text-align: left;">0.80 (0.54–1.19)</td>
<td rowspan="2" style="text-align: left;">0.90 (0.60–1.36)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">1.53 (0.86–2.72)</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">1.75 (0.92–3.32)</td>
<td style="text-align: left;">1.48 (0.73–2.99)</td>
<td rowspan="2" style="text-align: left;">2.18 (1.23–3.87)**</td>
<td rowspan="2" style="text-align: left;">8.77 (4.92–15.65)***</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">0.46 (0.15–1.40)</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma</td>
<td style="text-align: left;">0.94 (0.49–1.78)</td>
<td style="text-align: left;">1.83 (0.96–3.46)</td>
<td style="text-align: left;">1.58 (0.88–2.83)</td>
<td style="text-align: left;">0.79 (0.4–1.57)</td>
</tr>
<tr>
<td style="text-align: left;"> Cancer</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">1.52 (0.72–3.20)</td>
<td rowspan="2" style="text-align: left;">1.35 (0.60–3.03)</td>
<td rowspan="2" style="text-align: left;">1.62 (0.79–3.31)</td>
<td style="text-align: left;">0.99 (0.41–2.40)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">3.24 (1.01–10.39)*</td>
</tr>
<tr>
<td style="text-align: left;"> Cardiovascular disease</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td style="text-align: left;">1.39 (0.85–2.27)</td>
<td rowspan="2" style="text-align: left;">2.26 (1.43–3.58)**</td>
<td rowspan="2" style="text-align: left;">2.24 (1.48–3.38)***</td>
<td rowspan="2" style="text-align: left;">1.30 (0.81–2.10)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">2.92 (1.63–5.24)***</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">1.55 (0.73–3.29)</td>
<td style="text-align: left;">3.25 (1.49–7.09)**</td>
<td rowspan="2" style="text-align: left;">2.7 (1.34–5.44)**</td>
<td rowspan="2" style="text-align: left;">4.83 (2.38–9.80)***</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">8.67 (3.26–23.07)***</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">1.20 (0.74–1.96)</td>
<td rowspan="2" style="text-align: left;">1.59 (0.93–2.72)</td>
<td rowspan="2" style="text-align: left;">1.13 (0.71–1.79)</td>
<td style="text-align: left;">1.66 (0.97–2.84)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">4.24 (1.95–9.21)***</td>
</tr>
<tr>
<td style="text-align: left;"> Gastrointestinal disease</td>
<td style="text-align: left;">0.61 (0.33–1.13)</td>
<td style="text-align: left;">0.90 (0.47–1.72)</td>
<td style="text-align: left;">1.32 (0.79–2.19)</td>
<td style="text-align: left;">2.52 (1.48–4.29)**</td>
</tr>
<tr>
<td style="text-align: left;"> Hypertension</td>
<td style="text-align: left;">1.72 (1.20–2.48)**</td>
<td style="text-align: left;">1.64 (1.09–2.47)*</td>
<td style="text-align: left;">1.61 (1.17–2.23)**</td>
<td style="text-align: left;">1.17 (0.81–1.71)</td>
</tr>
<tr>
<td style="text-align: left;"> Musculoskeletal disease</td>
<td style="text-align: left;">8.09 (5.69–11.50)***</td>
<td style="text-align: left;">4.23 (2.88–6.22)***</td>
<td style="text-align: left;">4.40 (3.17–6.13)***</td>
<td style="text-align: left;">1.12 (0.77–1.63)</td>
</tr>
<tr>
<td style="text-align: left;"> Osteoporosis</td>
<td style="text-align: left;">1.11 (0.50–2.44)</td>
<td style="text-align: left;">1.29 (0.55–3.04)</td>
<td style="text-align: left;">1.64 (0.78–3.45)</td>
<td style="text-align: left;">0.92 (0.39–2.18)</td>
</tr>
<tr>
<td style="text-align: left;"> Skin disease</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  Level 1 vs. Levels 2–5</td>
<td rowspan="2" style="text-align: left;">0.78 (0.44–1.39)</td>
<td rowspan="2" style="text-align: left;">0.67 (0.35–1.28)</td>
<td rowspan="2" style="text-align: left;">1.10 (0.67–1.8)</td>
<td style="text-align: left;">0.58 (0.31–1.08)</td>
</tr>
<tr>
<td style="text-align: left;">  Levels 1–2 vs. Levels 3–5</td>
<td style="text-align: left;">1.89 (0.83–4.34)</td>
</tr>
<tr>
<td style="text-align: left;">Model fit</td>
<td style="text-align: left;"><p>χ<sup>2</sup>(28) = 348.86, <em>p </em>&lt; 0.001,</p>
<p>Pseudo <em>R</em><sup>2</sup> = 0.2326</p></td>
<td style="text-align: left;"><p>χ<sup>2</sup>(28) = 242.15, <em>p </em>&lt; 0.001,</p>
<p>Pseudo <em>R</em><sup>2</sup> = 0.2000</p></td>
<td style="text-align: left;"><p>χ<sup>2</sup>(27) = 273.02, <em>p </em>&lt; 0.001,</p>
<p>Pseudo <em>R</em><sup>2</sup> = 0.1486</p></td>
<td style="text-align: left;"><p>χ<sup>2</sup>(31) = 329.07, <em>p</em> &lt; 0.001,</p>
<p>Pseudo <em>R</em><sup>2</sup> = 0.2008</p></td>
</tr>
</tbody>
</table>

Note that modelling was not possible for the self-care dimension due to limited variability in responses. Variables that meet the proportional odds assumption exhibit a consistent odds ratio across response thresholds, i.e. comparing level 1 vs. levels 2–5 to levels 1–2 vs. levels 3–5. Conversely, variables that do not satisfy the proportional odds assumption demonstrate different odds ratios between the ‘level 1 vs. levels 2–5’ and the ‘levels 1–2 vs. levels 3–5’ thresholds, indicating the presence of response heterogeneity (cut-point shift).

ZTPI = 17-item Zimbardo Time Perspective Inventory

Level 1 = no problems, level 2 = slight problems, level 3–5 = moderate-to-extreme problems.

<sup>\*</sup> *p* \< 0.05; \*\* *p* \< 0.01; \*\*\* *p* \< 0.001

</div>

Several TP subscales, socio-demographic and health status characteristics were found to be in a significant association with one or more EQ-5D-5L domains without evidence of cut-point shifting. For every one-year increase in age, the odds of reporting a one-level higher severity of problems was 1.03 (95% CI 1.02–1.04) for mobility and 0.97 (95% CI 0.96–0.98) for anxiety/depression. Women were 1.58 (95% CI 1.08–2.29) and 1.56 (95% CI 1.19–2.05) times more likely to report a one-level higher severity of problems with usual activities and pain/discomfort than men. Education was not associated with any EQ-5D-5L domain scores, but a higher level of income was related to a lower likelihood of reporting a one-level higher severity of problems with usual activities. The presence of different chronic conditions tended to increase the probability of reporting more problems in each EQ-5D-5L domain. Notably, the highest odds ratios were related to the association between having been diagnosed with anxiety and the anxiety/depression domain (OR 8.77, 95% CI 4.92–15.65) and having musculoskeletal disease and the mobility domain (OR 8.09, 95% CI 5.69–11.50).

### Response heterogeneity

The anxiety/depression domain showed evidence of cut-point shift as demonstrated by the distinct ORs between the ‘no problems vs. slight-to-extreme problems’ and the ‘no or slight problems vs. moderate-to-extreme problems’ thresholds (Table <a href="#Tab3" data-ref-type="table">3</a>). Individuals with higher present-hedonistic or future TP subscale scores were less likely to report moderate-to-extreme problems compared to no or slight problems (present-hedonistic: OR 0.58, 95% CI 0.40–0.86 and future: OR 0.42, 95% CI 0.26–0.69) relative to slight-to-extreme problems compared to no problems (present-hedonistic: OR 0.90, 95% CI 0.73–1.10 and future: OR 0.75, 95% CI 0.57–0.99). Age, gender and education showed no evidence of cut-point shift. One income quintile demonstrated cut-point shift for mobility; however, both separate coefficients were insignificant. An array of chronic condition categories indicated cut-point shift (mobility: cardiovascular diseases, usual activities: anxiety and depression, pain/discomfort: allergy, anxiety/depression: cancer, diabetes, skin disease). Note that only four of these seven chronic condition groups had a statistically significant association with the respective EQ-5D-5L domains.

### The association between TP and EQ VAS and EQ-5D-5L index values

In the first EQ VAS model (‘without TP’), respondents with higher income had slightly higher EQ VAS scores and eight of 12 chronic health conditions were associated with a significant decrease in EQ VAS scores ranging from hypertension (2.55) to depression (10.42) (Table <a href="#Tab4" data-ref-type="table">4</a>). In the second model (‘with TP’), after including respondents’ TP subscale scores in addition to their socio-demographic characteristics and health status, four of the five TP subscales had a significant effect on EQ VAS scores. A one-point increase in the past-negative and present-fatalist subscale scores, all else equal, decreased the EQ VAS score by 2.70 and 2.58 (*p* \< 0.05). By contrast, a one-point increase in the future and present-hedonistic subscale scores, all else equal, resulted in a 3.00 and 1.25 increase in EQ VAS score (*p* \< 0.05). Respondents’ TP profile (including all five TP subscale scores) increased the explained variance in EQ VAS score from 26.6% (‘without TP’) to 30.2% (‘with TP’).

<div id="Tab4" class="table-wrap">

<div class="caption">

OLS regression of the association between time perspective and EQ VAS and EQ-5D-5L index values (regression coefficients and standard errors)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variables</th>
<th style="text-align: left;">EQ VAS ‘without TP’</th>
<th style="text-align: left;">EQ VAS ‘with TP’</th>
<th style="text-align: left;">EQ-5D-5L index ‘without TP’</th>
<th style="text-align: left;">EQ-5D-5L index ‘with TP’</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">79.478 (2.43)***</td>
<td style="text-align: left;">78.979 (4.166)***</td>
<td style="text-align: left;">0.934 (0.019)***</td>
<td style="text-align: left;">0.938 (0.031)***</td>
</tr>
<tr>
<td style="text-align: left;">Time perspective (ZTPI subscale score-1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Future</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">2.996 (0.935)**</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0.016 (0.006)**</td>
</tr>
<tr>
<td style="text-align: left;"> Present-hedonistic</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">1.246 (0.619)*</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0.003 (0.005)</td>
</tr>
<tr>
<td style="text-align: left;"> Present-fatalistic</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">−2.575 (0.639)***</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">−0.015 (0.005)**</td>
</tr>
<tr>
<td style="text-align: left;"> Past-positive</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0.259 (0.647)</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">−0.001 (0.004)</td>
</tr>
<tr>
<td style="text-align: left;"> Past-negative</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">−2.700 (0.98)**</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">−0.009 (0.007)</td>
</tr>
<tr>
<td style="text-align: left;">Age (years)</td>
<td style="text-align: left;">0.013 (0.033)</td>
<td style="text-align: left;">0.011 (0.033)</td>
<td style="text-align: left;">0.000 (0.000)</td>
<td style="text-align: left;">0.000 (0.000)</td>
</tr>
<tr>
<td style="text-align: left;">Gender (ref: male)</td>
<td style="text-align: left;">0.426 (0.982)</td>
<td style="text-align: left;">0.635 (0.968)</td>
<td style="text-align: left;">−0.006 (0.008)</td>
<td style="text-align: left;">−0.005 (0.008)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Education (ref: primary)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Secondary</td>
<td style="text-align: left;">2.363 (1.454)</td>
<td style="text-align: left;">2.058 (1.407)</td>
<td style="text-align: left;">0.008 (0.011)</td>
<td style="text-align: left;">0.006 (0.011)</td>
</tr>
<tr>
<td style="text-align: left;"> Tertiary</td>
<td style="text-align: left;">0.915 (1.459)</td>
<td style="text-align: left;">0.216 (1.419)</td>
<td style="text-align: left;">0.014 (0.01)</td>
<td style="text-align: left;">0.009 (0.01)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Income (ref: quintile 1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 2</td>
<td style="text-align: left;">1.343 (2.002)</td>
<td style="text-align: left;">1.116 (1.954)</td>
<td style="text-align: left;">0.013 (0.015)</td>
<td style="text-align: left;">0.011 (0.015)</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 3</td>
<td style="text-align: left;">1.781 (1.938)</td>
<td style="text-align: left;">0.989 (1.877)</td>
<td style="text-align: left;">0.014 (0.015)</td>
<td style="text-align: left;">0.009 (0.014)</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 4</td>
<td style="text-align: left;">4.736 (1.864)*</td>
<td style="text-align: left;">3.966 (1.798)*</td>
<td style="text-align: left;">0.027 (0.014)</td>
<td style="text-align: left;">0.023 (0.014)</td>
</tr>
<tr>
<td style="text-align: left;"> Quintile 5</td>
<td style="text-align: left;">4.042 (1.883)*</td>
<td style="text-align: left;">2.742 (1.832)</td>
<td style="text-align: left;">0.020 (0.014)</td>
<td style="text-align: left;">0.012 (0.013)</td>
</tr>
<tr>
<td style="text-align: left;"> Don't know/refused to answer</td>
<td style="text-align: left;">4.353 (1.765)*</td>
<td style="text-align: left;">3.683 (1.704)*</td>
<td style="text-align: left;">0.025 (0.013)</td>
<td style="text-align: left;">0.021 (0.013)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Chronic conditions (ref: none)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Allergy</td>
<td style="text-align: left;">0.144 (1.347)</td>
<td style="text-align: left;">0.111 (1.353)</td>
<td style="text-align: left;">−0.004 (0.01)</td>
<td style="text-align: left;">−0.005 (0.01)</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety</td>
<td style="text-align: left;">−7.949 (2.129)***</td>
<td style="text-align: left;">−7.140 (2.141)**</td>
<td style="text-align: left;">−0.081 (0.019)***</td>
<td style="text-align: left;">−0.078 (0.019)***</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma</td>
<td style="text-align: left;">−4.411 (2.138)*</td>
<td style="text-align: left;">−3.726 (2.189)</td>
<td style="text-align: left;">−0.018 (0.02)</td>
<td style="text-align: left;">−0.015 (0.02)</td>
</tr>
<tr>
<td style="text-align: left;"> Cancer</td>
<td style="text-align: left;">−9.753 (4.185)*</td>
<td style="text-align: left;">−8.918 (4.123)*</td>
<td style="text-align: left;">−0.014 (0.025)</td>
<td style="text-align: left;">−0.009 (0.024)</td>
</tr>
<tr>
<td style="text-align: left;"> Cardiovascular disease</td>
<td style="text-align: left;">−8.388 (1.831)***</td>
<td style="text-align: left;">−8.673 (1.781)***</td>
<td style="text-align: left;">−0.070 (0.019)***</td>
<td style="text-align: left;">−0.071 (0.018)***</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td style="text-align: left;">−10.416 (2.643)***</td>
<td style="text-align: left;">−9.385 (2.642)***</td>
<td style="text-align: left;">−0.101 (0.028)***</td>
<td style="text-align: left;">−0.095 (0.027)**</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes</td>
<td style="text-align: left;">−6.190 (1.74)***</td>
<td style="text-align: left;">−6.293 (1.686)***</td>
<td style="text-align: left;">−0.031 (0.017)</td>
<td style="text-align: left;">−0.032 (0.017)</td>
</tr>
<tr>
<td style="text-align: left;"> Gastrointestinal disease</td>
<td style="text-align: left;">−2.527 (1.932)</td>
<td style="text-align: left;">−2.184 (1.877)</td>
<td style="text-align: left;">−0.013 (0.017)</td>
<td style="text-align: left;">−0.011 (0.017)</td>
</tr>
<tr>
<td style="text-align: left;"> Hypertension</td>
<td style="text-align: left;">−2.548 (1.208)*</td>
<td style="text-align: left;">−2.600 (1.202)*</td>
<td style="text-align: left;">−0.026 (0.009)**</td>
<td style="text-align: left;">−0.026 (0.009)**</td>
</tr>
<tr>
<td style="text-align: left;"> Musculoskeletal disease</td>
<td style="text-align: left;">−7.316 (1.339)***</td>
<td style="text-align: left;">−7.039 (1.337)***</td>
<td style="text-align: left;">−0.075 (0.01)***</td>
<td style="text-align: left;">−0.074 (0.01)***</td>
</tr>
<tr>
<td style="text-align: left;"> Osteoporosis</td>
<td style="text-align: left;">−7.123 (3.686)</td>
<td style="text-align: left;">−6.844 (3.639)</td>
<td style="text-align: left;">−0.004 (0.024)</td>
<td style="text-align: left;">−0.003 (0.023)</td>
</tr>
<tr>
<td style="text-align: left;"> Skin disease</td>
<td style="text-align: left;">−0.567 (1.738)</td>
<td style="text-align: left;">−0.341 (1.786)</td>
<td style="text-align: left;">0.004 (0.014)</td>
<td style="text-align: left;">0.006 (0.014)</td>
</tr>
<tr>
<td style="text-align: left;">Model fit</td>
<td style="text-align: left;"><p>F(21, 974) = 12.04 (<em>p </em>&lt; 0.001),</p>
<p><em>R</em><sup>2</sup> = 0.266</p></td>
<td style="text-align: left;"><p>F(26, 969) = 12.51 (<em>p </em>&lt; 0.001),</p>
<p><em>R</em><sup>2</sup> = 0.302</p></td>
<td style="text-align: left;">F(21, 974) = 8.25 (<em>p </em>&lt; 0.001), <em>R</em><sup>2</sup> = 0.309</td>
<td style="text-align: left;">F(26, 969) = 7.66 (<em>p </em>&lt; 0.001), <em>R</em><sup>2</sup> = 0.326</td>
</tr>
</tbody>
</table>

*EQ VAS* EuroQol visual analogue scale, *TP* time perspective, *ZTPI* 17−item Zimbardo Time Perspective Inventory

<sup>\*</sup> *p *\< 0.05; \*\* *p *\< 0.01; \*\*\* *p* \< 0.001

</div>

In the first EQ-5D-5L index model (‘without TP’), no socio-demographic characteristics were associated with index values; however, five of 12 chronic health conditions were resulted in a significant decrease in index values ranging from hypertension (0.026) to depression (0.101) (Table <a href="#Tab4" data-ref-type="table">4</a>). In the second model (‘with TP’), after including respondents’ TP subscale scores in addition to their socio-demographic characteristics and health status, two TP subscales had a significant effect on EQ-5D-5L index values. A one-point increase in the present-fatalistic and future TP subscale scores, was associated with a decrease of 0.015 and an increase of 0.016 in EQ-5D-5L index, all else equal (*p* \< 0.05). Respondents’ TP profile increased the explained variance in EQ-5D-5L index from 30.9% (‘without TP’) to 32.6% (‘with TP’).

## Discussion

This study contributes to the growing literature on the link between psychological dispositions and self-reported health on the EQ-5D. Using a large general population sample from Hungary, it provides an insight into the association between individuals’ TP profiles and self-reported health on the EQ-5D. Three EQ-5D domains (usual activities, pain/discomfort and anxiety/depression) as well as the EQ VAS and EQ-5D index values were associated with respondents’ TP profile. Furthermore, we demonstrated the presence of response heterogeneity in the anxiety/depression domain; the probability of reporting more problems in this domain decreased with having more future and present-hedonistic characteristics. As such, this is the first study that identified response heterogeneity on the EQ-5D arising from individual psychological factors. Other authors have used item response theory, Rasch-analysis, Mantel-Haenszel statistics and ordinal logistic regressions, and reported response heterogeneity (or differential item functioning) on the EQ-5D mainly across geographical regions, countries, age groups, sexes, ethnicities, patients vs. proxies and clinically relevant patient groups (e.g. types of cancer or psychosis) \[39–46\].

Multiple TP subscales were significantly associated with EQ-5D-5L and EQ VAS values. However, the overall impact of TP on EQ VAS and EQ-5D-5L values appears to be relatively small. Findings of a large systematic review suggest that personality characteristics account for varying proportions of health (ranging from 0 to 39%), depending on the health status measure used \[4\]. In our study, TP explained 3.6% of the variance of EQ VAS and 1.7% of EQ-5D-5L index values. Although these findings are in the range of those reported in the abovementioned review, they fall towards the lower end. It is worth noting that the percentage of explained variance in EQ-5D-5L index values also depends on the value set used. It is likely that using a value set of another country, where anxiety/depression has a larger weight compared to the Hungarian value set, would result in slightly higher explained variance.

Our findings suggest that the impact of certain TP scales, such as future or present-fatalistic, on index values and EQ VAS scores may approximate previously reported MID estimates (0.03–0.10 for the EQ-5D-5L index and 7–11 for EQ VAS) \[47–55\]. For example, compared to a respondent scoring the minimum on the future TP subscale, a respondent scoring one, two, three or four has, on average, higher EQ-5D-5L index values by 0.016, 0.032, 0.048 and 0.064 and higher EQ VAS scores by 3, 6, 9 and 12 points, respectively.

Respondents’ TP profile and a few chronic condition groups seem to display cut-point shift, a form of response heterogeneity. It is important to stress that for variables not producing any cut-point shift, but being significantly related to self-reported health (e.g. future TP to usual activities and pain/discomfort), an index shift may still occur. In our analytical framework, we accounted for ‘true’ health status by controlling for respondents’ chronic health conditions; however, response heterogeneity may also affect these variables through false reporting \[56\]. Future research is recommended to use different approaches (e.g. anchoring vignettes, performance measurements, objective clinical variables and item response theory) to isolate index shift as a reporting behaviour from variations in underlying health status \[57–62\].

Another noteworthy finding from this study is that the EQ-5D showed no evidence of cut-point shift by age, gender and education. Notwithstanding, some domains exhibited significant associations with age or gender that may signal a possible index shift. This is in line with prior work on response heterogeneity on the EQ-5D, whereby older respondents were more likely to report problems with mobility and less likely with anxiety/depression \[41, 45\]. Even though we cannot rule out the possibility of having more mobility problems with age after controlling for specific chronic health conditions, it may also be possible that these findings are attributable to an index shift. Similarly, our findings suggest a possible index shift on the usual activities and pain/discomfort domains by gender, whereby women were more inclined to report problems than men. In a previous study with cancer patients, the mobility and usual activities domains showed large- and medium-size response heterogeneity by gender \[41\]. Among the two forms of response heterogeneity distinguished in our analytical framework, index shift is less concerning than cut-point shift due to its linear nature \[26\].

Possessing more future and present-hedonistic traits may be seen as desirable qualities leading to less health problems, whereas individuals with more past-negative and present-fatalistic characteristics appear to report more health problems. These results are broadly consistent with those of previous studies that identified an association between TP profile and self-reported health measured by various instruments \[11–13, 15\]. As argued above, these associations must be treated with caution as they are presumably a result of both response heterogeneity and true health effects. A possible explanation for the latter is that TP profile has been found to be related to a number of health behaviours, such as exercising, alcohol, tobacco and substance use, attendance at health screenings and adherence to medications \[8, 10, 63–65\]. The association between health outcomes and TP profiles is further supported by evidence of the effectiveness of TP-based psychological interventions, such as ‘Time Perspective Therapy’, which have successfully improved mental health in patients with posttraumatic stress disorder \[66\].

Our findings may have wider implications for patient management, clinical trials and economic evaluations. It seems that non-health factors, such as TP profile may affect one’s ‘true’ health as well as response behaviour on the EQ-5D. Understanding the relationship between TP and health status may help to identify barriers in treatment adherence and to improve patient self-management. Further research is needed to examine whether psychological characteristics, such as TP profile, may be considered a potential source of systemic differences between the treatment and control groups in clinical trials. Lastly, considering that the EQ-5D index values are used to estimate quality-adjusted life years, individual TP may also represent an uncertainty on the results of cost-effectiveness analyses and healthcare decisions based thereon. Exploring the potential impact of respondents’ TP on health preferences in valuation studies is another an important direction for future research.

This study has a number of limitations. First, we used a general population sample, and therefore, there was less variability in respondents’ health status that motivated us in collapsing response levels and excluding self-care from the domain-specific analyses. Secondly, more abundant information about the clinical status of respondents (e.g. severity/stage, symptoms, limitations in functioning) could have been useful to more adequately adjust our models for ‘true’ health. Thirdly, selection bias may have occurred not only because of the online mode of administration that excluded people without internet access or sufficient computer literacy, but also due to the study design. During the DCE tasks, 255 respondents were excluded based on quality control criteria, such as providing inconsistent responses on the dominant pairs \[32\]. As these tasks may be viewed as some kind of logical or cognitive test, it is likely that respondents with somewhat higher cognitive abilities accomplished them and therefore were selected to the final sample. Fourthly, the original 56-item ZTPI questionnaire has been subject to some criticisms with regard to its construct validity and dimensionality \[5, 67\]. In our study, we used a 17-item short version of this scale that performed well in most psychometric tests in an earlier study in Hungary \[35\]. However, its face validity may still be questioned; for example, some of the items may rather capture beliefs, values or preferences that do not directly relate to TP and therefore may represent alternative psychological constructs \[5, 68, 69\].

In conclusion, this is the first study to explore the association between individuals’ TP and self-reported health on the EQ-5D and also the first to identify response heterogeneity (cut-point shift) stemming from psychological characteristics on the EQ-5D. It seems that psychological factors may play a double role in self-reported health, firstly as affecting underlying health and secondly as a factor influencing one’s response behavior. These findings increase our understanding of the non-health-related factors that affect self-reported health on standardized health status measures.

### Acknowledgement

The authors thank Fatima Al Sayah for her useful comments on an earlier draft of this manuscript.

### Funding

Open access funding provided by Corvinus University of Budapest. This study was supported by a grant from the EuroQol Research Foundation (461-RA).

### Data Availability

All data of this study are available from the corresponding author upon reasonable request.

### Declarations

#### Conflict of interest

FR and MFJ are active members of the EuroQol Group. Views expressed in the article are those of the authors and are not necessarily those of the EuroQol Research Foundation.

#### Ethical approval

All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki declaration and its later amendments or comparable ethical standards. Ethical approval was obtained from the Research Ethics Committee of the Corvinus University of Budapest (no. KRH/31/2021).

#### Informed consent

Informed consent was obtained from all participants included in the study.

## References

1. Taylor SE, Kemeny ME, Reed GM, Bower JE, Gruenewald TL. Psychological resources, positive illusions, and health. American Psychologist. 2000;55(1):99–109. doi:10.1037//0003-066x.55.1.99

2. Ferguson E. Personality is of central concern to understand health: Towards a theoretical model for health psychology. Health Psychology Review. 2013;7(Suppl 1):S32–s70. doi:10.1080/17437199.2010.547985

3. Jokela M, Batty GD, Nyberg ST, Virtanen M, Nabi H, Singh-Manoux A, Kivimäki M. Personality and all-cause mortality: Individual-participant meta-analysis of 3,947 deaths in 76,150 adults. American Journal of Epidemiology. 2013;178(5):667–675. doi:10.1093/aje/kwt170

4. Huang IC, Lee JL, Ketheeswaran P, Jones CM, Revicki DA, Wu AW. Does personality affect health-related quality of life? A systematic review. PLoS One. 2017;12(3):e0173806. doi:10.1371/journal.pone.0173806

5. Mohammed S, Marhefka JT. How have we, do we, and will we measure time perspective? A review of methodological and measurement issues. Journal of Organizational Behavior. 2020;41(3):276–293.

6. Stolarski M, Wojciechowski J, Matthews G. Seeking the origins of time perspectives – Intelligence, temperament, or family environment? A one-year longitudinal study. Personality and Individual Differences. 2021;169:110080.

7. Zimbardo P, Boyd J. Putting time in perspective: A valid, reliable individual-differences metric. Journal of Personality and Social Psychology. 1999;77(6):1271–1288.

8. Keough KA, Zimbardo PG, Boyd JN. Who's smoking, drinking, and using drugs? Time perspective as a predictor of substance use. Basic and Applied Social Psychology. 1999;21(2):149–164.

9. Kooij D, Kanfer R, Betts M, Rudolph CW. Future time perspective: A systematic review and meta-analysis. Journal of Applied Psychology. 2018;103(8):867–893. doi:10.1037/apl0000306

10. Sansbury B, Dasgupta A, Guthrie L, Ward M. Time perspective and medication adherence among individuals with hypertension or diabetes mellitus. Patient Education and Counseling. 2014;95(1):104–110. doi:10.1016/j.pec.2013.12.016

11. Griva F, Tseferidi SI, Anagnostopoulos F. Time to get healthy: Associations of time perspective with perceived health status and health behaviors. Psychology, Health & Medicine. 2015;20(1):25–33. doi:10.1080/13548506.2014.913798

12. Guthrie LC, Butler SC, Ward MM. Time perspective and socioeconomic status: A link to socioeconomic disparities in health?. Social Science & Medicine. 2009;68(12):2145–2151. doi:10.1016/j.socscimed.2009.04.004

13. Laguette V, Apostolidis T, Dany L, Bellon N, Grimaud JC, Lagouanelle-Simeoni MC. Quality of life and time perspective in inflammatory bowel disease patients. Quality of Life Research. 2013;22(10):2721–2736. doi:10.1007/s11136-013-0399-4

14. Préau M, Apostolidis T, Francois C, Raffi F, Spire B. Time perspective and quality of life among HIV-infected patients in the context of HAART. AIDS Care. 2007;19(4):449–458. doi:10.1080/09540120601017464

15. Oyanadel C, Buela-Casal G. Time perception and psychopathology: Influence of time perspective on quality of life of severe mental illness. Actas Españolas de Psiquiatría. 2014;42(3):99–107.

16. Brooks R. EuroQol: The current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

17. Kennedy-Martin M, Slaap B, Herdman M, van Reenen M, Kennedy-Martin T, Greiner W, Busschbach J, Boye KS. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. European Journal of Health Economics. 2020;21(8):1245–1257. doi:10.1007/s10198-020-01195-8

18. Rencz F, Gulácsi L, Drummond M, Golicki D, Prevolnik Rupel V, Simon J, Stolk EA, Brodszky V, Baji P, Závada J, Petrova G, Rotar A, Péntek M. EQ-5D in Central and Eastern Europe: 2000–2015. Quality of Life Research. 2016;25(11):2693–2710. doi:10.1007/s11136-016-1375-6

19. Wang A, Rand K, Yang Z, Brooks R, Busschbach J. The remarkably frequent use of EQ-5D in non-economic research. European Journal of Health Economics. 2021;23(6):1007–1014. doi:10.1007/s10198-021-01411-z

20. Janssen B, Szende A, Szende A, Janssen B, Cabases J. Population Norms for the EQ-5D. Self-reported population health: An international perspective based on EQ-5D. 2014:19–30. Springer.

21. Pickard AS, Jalundhwala YJ, Bewsher H, Sharp LK, Walton SM, Schumock GT, Caskey RN. Lifestyle-related attitudes: Do they explain self-rated health and life-satisfaction?. Quality of Life Research. 2018;27(5):1227–1235. doi:10.1007/s11136-017-1774-3

22. Chapman BP, Franks P, Duberstein PR, Jerant A. Differences between individual and societal health state valuations: Any link with personality?. Medical Care. 2009;47(8):902–907. doi:10.1097/MLR.0b013e3181a8112e

23. Jerant A, Chapman BP, Franks P. Personality and EQ-5D scores among individuals with chronic conditions. Quality of Life Research. 2008;17(9):1195–1204. doi:10.1007/s11136-008-9401-y

24. Whynes DK. Correspondence between EQ-5D health state classifications and EQ VAS scores. Health and Quality of Life Outcomes. 2008;6:94. doi:10.1186/1477-7525-6-94

25. Israelsson J, Thylén I, Strömberg A, Bremer A, Årestedt K. Factors associated with health-related quality of life among cardiac arrest survivors treated with an implantable cardioverter-defibrillator. Resuscitation. 2018;132:78–84. doi:10.1016/j.resuscitation.2018.09.002

26. Lindeboom M, van Doorslaer E. Cut-point shift and index shift in self-reported health. Journal of Health Economics. 2004;23(6):1083–1099. doi:10.1016/j.jhealeco.2004.01.002

27. Hays RD, Morales LS, Reise SP. Item response theory and health outcomes measurement in the 21st century. Medical Care. 2000;38(9 Suppl):II28–II42. doi:10.1097/00005650-200009002-00007

28. Hernández-Quevedo, C., Jones, A. M., & Rice, N. (2004). Reporting bias and heterogeneity in self-assessed health. Evidence from the British Household Panel Survey. Health, Econometrics and Data Group (HEDG) Working paper 05, 4.

29. Pfarr C, Schmid A, Schneider U. Reporting heterogeneity in self-assessed health among elderly Europeans. Health Economics Review. 2012;2(1):21. doi:10.1186/2191-1991-2-21

30. Schneider U, Pfarr C, Schneider BS, Ulrich V. I feel good! Gender differences and reporting heterogeneity in self-assessed health. European Journal of Health Economics. 2012;13(3):251–265. doi:10.1007/s10198-011-0301-7

31. Rencz F, Janssen MF. Analyzing the pain/discomfort and anxiety/depression composite domains and the meaning of discomfort in the EQ-5D: A mixed-methods study. Value Health. 2022;25(12):2003–2016. doi:10.1016/j.jval.2022.06.012

32. Rencz F, Ruzsa G, Bató A, Yang Z, Finch AP, Brodszky V. Value set for the EQ-5D-Y-3L in Hungary. Pharmacoeconomics. 2022;40:205–215. doi:10.1007/s40273-022-01190-2

33. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, Bonsel G, Badia X. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

34. Rencz F, Brodszky V, Gulácsi L, Golicki D, Ruzsa G, Pickard AS, Law EH, Péntek M. Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time trade-off in Hungary. Value Health. 2020;23(9):1235–1245. doi:10.1016/j.jval.2020.03.019

35. Orosz G, Dombi E, Tóth-Király I, Roland-Lévy C. The less is more: The 17-Item Zimbardo Time Perspective Inventory. Current Psychology. 2017;36(1):39–47.

36. Williams R. Generalized ordered logit/partial proportional odds models for ordinal dependent variables. Stata Journal. 2006;6(1):58–82.

37. Brant R. Assessing proportionality in the proportional odds model for ordinal logistic regression. Biometrics. 1990;46:1171–1178.

38. Breusch TS, Pagan AR. The Lagrange multiplier test and its applications to model specification in econometrics. The Review of Economic Studies. 1980;47(1):239–253.

39. Knott RJ, Lorgelly PK, Black N, Hollingsworth B. Differential item functioning in quality of life measurement: An analysis using anchoring vignettes. Social Science & Medicine. 2017;190:247–255. doi:10.1016/j.socscimed.2017.08.033

40. Feng Y, Herdman M, van Nooten F, Cleeland C, Parkin D, Ikeda S, Igarashi A, Devlin NJ. An exploration of differences between Japan and two European countries in the self-reporting and valuation of pain and discomfort on the EQ-5D. Quality of Life Research. 2017;26(8):2067–2078. doi:10.1007/s11136-017-1541-5

41. Smith AB, Cocks K, Parry D, Taylor M. A differential item functioning analysis of the EQ-5D in cancer. Value Health. 2016;19(8):1063–1067. doi:10.1016/j.jval.2016.06.005

42. Salomon JA, Patel A, Neal B, Glasziou P, Grobbee DE, Chalmers J, Clarke PM. Comparability of patient-reported health status: Multicountry analysis of EQ-5D responses in patients with type 2 diabetes. Medical Care. 2011;49(10):962–970. doi:10.1097/MLR.0b013e3182239489

43. Whynes DK, Sprigg N, Selby J, Berge E, Bath PM. Testing for differential item functioning within the EQ-5D. Medical Decision Making. 2013;33(2):252–260. doi:10.1177/0272989X12465016

44. Stochl J, Croudace T, Perez J, Birchwood M, Lester H, Marshall M, Amos T, Sharma V, Fowler D, Jones PB. Usefulness of EQ-5D for evaluation of health-related quality of life in young adults with first-episode psychosis. Quality of Life Research. 2013;22(5):1055–1063. doi:10.1007/s11136-012-0222-7

45. Penton H, Dayson C, Hulme C, Young T. An investigation of age-related differential item functioning in the EQ-5D-5L using item response theory and logistic regression. Value Health. 2022;25(9):1566–1574. doi:10.1016/j.jval.2022.03.009

46. Prieto L, Novick D, Sacristán JA, Edgell ET, Alonso J. A Rasch model analysis to test the cross-cultural validity of the EuroQoL-5D in the Schizophrenia Outpatient Health Outcomes Study. Acta Psychiatrica Scandinavica. Supplementum. 2003;416:24–29. doi:10.1034/j.1600-0447.107.s416.6.x

47. Coretti S, Ruggeri M, McNamee P. The minimum clinically important difference for EQ-5D index: A critical review. Expert Review of Pharmacoeconomics & Outcomes Research. 2014;14(2):221–233. doi:10.1586/14737167.2014.894462

48. Hoehle LP, Phillips KM, Speth MM, Caradonna DS, Gray ST, Sedaghat AR. Responsiveness and minimal clinically important difference for the EQ-5D in chronic rhinosinusitis. Rhinology. 2019;57(2):110–116. doi:10.4193/Rhin18.122

49. McClure NS, Sayah FA, Ohinmaa A, Johnson JA. Minimally important difference of the EQ-5D-5L Index Score in adults with type 2 diabetes. Value Health. 2018;21(9):1090–1097. doi:10.1016/j.jval.2018.02.007

50. McClure NS, Sayah FA, Xie F, Luo N, Johnson JA. Instrument-defined estimates of the minimally important difference for EQ-5D-5L Index Scores. Value Health. 2017;20(4):644–650. doi:10.1016/j.jval.2016.11.015

51. Pickard AS, Neary MP, Cella D. Estimation of minimally important differences in EQ-5D utility and VAS scores in cancer. Health and Quality of Life Outcomes. 2007;5:70. doi:10.1186/1477-7525-5-70

52. Shiroiwa T, Fukuda T, Ikeda S, Igarashi A, Noto S, Shimozuma K. Japanese population norms for preference-based measures: EQ-5D-3L, EQ-5D-5L, and SF-6D. Quality of Life Research. 2016;25(3):707–719. doi:10.1007/s11136-015-1108-2

53. Nolan CM, Longworth L, Lord J, Canavan JL, Jones SE, Kon SS, Man WD. The EQ-5D-5L health status questionnaire in COPD: Validity, responsiveness and minimum important difference. Thorax. 2016;71(6):493–500. doi:10.1136/thoraxjnl-2015-207782

54. Henry EB, Barry LE, Hobbins AP, McClure NS, O'Neill C. Estimation of an instrument-defined minimally important difference in EQ-5D-5L index scores based on scoring algorithms derived using the EQ-VT version 2 valuation protocols. Value Health. 2020;23(7):936–944. doi:10.1016/j.jval.2020.03.003

55. Chen P, Lin KC, Liing RJ, Wu CY, Chen CL, Chang KC. Validity, responsiveness, and minimal clinically important difference of EQ-5D-5L in stroke patients undergoing rehabilitation. Quality of Life Research. 2016;25(6):1585–1596. doi:10.1007/s11136-015-1196-z

56. Baker M, Stabile M, Deri C. What do self-reported, objective, measures of health measure?. The Journal of Human Resources. 2004;39(4):1067–1093.

57. Bago d'Uva T, Van Doorslaer E, Lindeboom M, O'Donnell O. Does reporting heterogeneity bias the measurement of health disparities?. Health Economics. 2008;17(3):351–375. doi:10.1002/hec.1269

58. Au N, Lorgelly PK. Anchoring vignettes for health comparisons: An analysis of response consistency. Quality of Life Research. 2014;23(6):1721–1731. doi:10.1007/s11136-013-0615-2

59. Grol-Prokopczyk H, Freese J, Hauser RM. Using anchoring vignettes to assess group differences in general self-rated health. Journal of Health and Social Behavior. 2011;52(2):246–261. doi:10.1177/0022146510396713

60. Salomon JA, Tandon A, Murray CJ. Comparability of self rated health: Cross sectional multi-country survey using anchoring vignettes. BMJ. 2004;328(7434):258. doi:10.1136/bmj.37963.691632.44

61. Melzer D, Lan TY, Tom BD, Deeg DJ, Guralnik JM. Variation in thresholds for reporting mobility disability between national population subgroups and studies. Journal of Gerontology A Biological Sciences and Medical Sciences. 2004;59(12):1295–1303. doi:10.1093/gerona/59.12.1295

62. Weisscher N, Glas CA, Vermeulen M, De Haan RJ. The use of an item response theory-based disability item bank across diseases: Accounting for differential item functioning. Journal of Clinical Epidemiology. 2010;63(5):543–549. doi:10.1016/j.jclinepi.2009.07.016

63. Henson JM, Carey MP, Carey KB, Maisto SA. Associations among health behaviors and time perspective in young adults: Model testing with boot-strapping replication. Journal of Behavioral Medicine. 2006;29(2):127–137. doi:10.1007/s10865-005-9027-2

64. Guthrie LC, Butler SC, Lessl K, Ochi O, Ward MM. Time perspective and exercise, obesity, and smoking: Moderation of associations by age. American Journal of Health Promotion. 2014;29(1):9–16. doi:10.4278/ajhp.130122-QUAN-39

65. Griva F, Anagnostopoulos F, Potamianos G. Time perspective and perceived risk as related to mammography screening. Women Health. 2013;53(8):761–776. doi:10.1080/03630242.2013.836140

66. Sword RM, Sword RKM, Brunskill SR, Zimbardo PG. Time perspective therapy: A new time-based metaphor therapy for PTSD. Journal of Loss and Trauma. 2014;19(3):197–201.

67. Perry JL, Temple EC, Worrell FC, Zivkovic U, Mello ZR, Musil B, Cole JC, Mckay MT. Different version, similar result? A critical analysis of the multiplicity of shortened versions of the Zimbardo Time Perspective Inventory. SAGE Open. 2020;10(2):2158244020923351.

68. Worrell FC, Temple EC, McKay MT, Živkovič U, Perry JL, Mello ZR, Musil B, Cole JC. A theoretical approach to resolving the psychometric problems associated with the Zimbardo Time Perspective Inventory: Results from the USA, Australia, Slovenia, and the United Kingdom. European Journal of Psychological Assessment. 2018;34(1):41–51.

69. Shipp AJ, Edwards JR, Lambert LS. Conceptualization and measurement of temporal focus: The subjective experience of the past, present, and future. Organizational Behavior and Human Decision Processes. 2009;110(1):1–22.

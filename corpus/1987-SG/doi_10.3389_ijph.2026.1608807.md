---
project_id: "1987-SG"
work_id: "doi:10.3389/ijph.2026.1608807"
doi: "10.3389/ijph.2026.1608807"
pmid: "41727346"
pmcid: "PMC12916432"
title: "Health-Related Quality of Life Among Ukrainian War Refugees Compared to the General Population in Estonia"
journal: "International Journal of Public Health"
publication_date: "2026"
volume: "71"
authors:
  - name: "Rainer Reile"
    affiliation_ids:
      - "aff1"
  - name: "Johann Saavaste"
    affiliation_ids:
      - "aff1"
  - name: "Galina Opikova"
    affiliation_ids:
      - "aff1"
  - name: "Taavi Lai"
    affiliation_ids:
      - "aff2"
  - name: "Juanita Haagsma"
    affiliation_ids:
      - "aff3"
affiliations:
  - id: "aff1"
    name: "National Institute for Health Development, Tallinn, Estonia"
  - id: "aff2"
    name: "Fourth View Consulting, Tallinn, Estonia"
  - id: "aff3"
    name: "Erasmus University Medical Center, Rotterdam, Netherlands"
keywords:
  - "EQ-5D"
  - "Estonia"
  - "Ukraine"
  - "health-related quality of life"
  - "refugee"
licence: "cc-by"
source_file: "input/projects/1987-SG/papers/doi_10.3389_ijph.2026.1608807.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12916432/fullTextXML"
source_method: "epmc_xml"
source_sha256: "6450a38abac3dc7f89ba716b91f835cfcd54394f6d992f19f7007304da9f3ef4"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Health-Related Quality of Life Among Ukrainian War Refugees Compared to the General Population in Estonia

## Abstract

### Objectives

The study aimed to provide a comparative analysis of HRQoL and its health-related and socio-demographic correlates among Ukrainian refugees and general population in Estonia.

### Methods

Study used age and sex matched data (1249 pairs) from two representative cross-sectional surveys covering Ukrainian refugees aged 18–64 years residing in Estonia (n = 1,430), and the general population (n = 2007) of Estonia in 2024. Tobit-regression was used to compare the EQ-5D-3L index values in both groups while controlling for wide range of socio-demographic and health indicators.

### Results

Refugees reported less restrictions in mobility, self-care or in performing usual activities, whereas higher prevalence of pain/discomfort and anxiety/depression was found for refugees compared to control group. Refugees had slightly lower EQ-5D index score (estimate −0.017, p = 0.029) compared to population controls after adjustment for socio-demographic and health-related covariates.

### Conclusion

Variations in EQ-5D-3L dimensions and index scores between refugees and population controls contribute to the literature on refugee HRQoL and extend the knowledge on HRQoL of Ukrainian refugees in the context of ongoing refugee crisis in Europe while also improving knowledge for support provision to this refugee group in Estonia.

## Introduction

According to the United Nations \[1\], over 5.3 million inhabitants have left Ukraine for other European countries following the Russian aggression in February 2022. These displaced people have endured high psychosocial stress, which coupled with migratory status, and lack of social and economic safety nets in the new setting are likely to have direct health impacts \[2\] even though host countries often provide extended health and social care coverage to the refugees. Available evidence suggests that while the health needs of refugees are diverse and complex, mental healthcare, preventive services and long-term care are among top priorities \[3\]. However, there is persisting need for better data on refugees’ health status and health needs to tailor support to the needs of the specific refugee groups.

Health-related quality of life (HRQoL) is an important measure of health as it encompasses not only self-reported physical health but also mental, emotional, and social dimensions of wellbeing. HRQoL among refugees is generally lower than that of the general population of the host countries \[4\]. The reduced HRQoL has often been associated with high exposure to potentially traumatic experiences before or during the displacement \[5, 6\] but difference in HRQoL can also be explained by poorer physical and mental health \[4\]. Refugees may face difficulties in accessing the healthcare system which potentially translates to strong link between HRQoL and social integration reported in earlier studies \[4, 6\]. As demonstrated in previous studies \[7, 8\], the socio-demographic differences between refugees and host population–related mostly to the sex- and age distribution but also to the socioeconomic status–contribute additionally to HRQoL differences. This disparity in HRQoL has significant implications for the health and social care systems of host countries, potentially increasing the demand for medical and psychological support services \[9\].

The escalation of the Russo-Ukrainian war in 2022 caused a large-scale flow of refugees both originating and resettling within Europe. This contrasts with the experience from the refugee crisis following the Syrian war little more than a decade ago \[10\], when larger differences in socio-cultural context might have had varied public health implications compared to current situation. Although a recent experimental study \[11\] has demonstrated consistent and relatively high support for migrants irrespective of background across Europe, several others \[12, 13\] have associated refugees originating from Ukraine with more supportive public attitudes. Given that a systematic review by Gagliardi et al \[6\] has associated lower HRQoL scores with difficulties in accessing and understanding the new healthcare system, community loss and cultural gap experienced in the new country, it is plausible that available evidence on differences of refugee and host populations’ HRQoL might not fully apply in the context of Ukrainian refugees. So far only a few studies \[14–16\] have examined HRQoL in this population and indicate lower HRQoL among Ukrainian refugees, which varies by sociodemographic and mental health indicators. However, the aforementioned studies rely on convenience sampling, which may limit the generalizability of the findings. To the best of our knowledge, there have been no studies that allow direct comparisons of the HRQoL of Ukrainian refugees and that of the general population of the host country using a matched case-control design to reduce the confounding due to socio-demographic differences between the refugees and the general population.

This study will focus on Estonia, where by early 2024 approximately 32,500 refugees from Ukraine had been formally registered, constituting about 2.4% of Estonia’s population (1.37 million) in January 2024 \[17\]. Given the extension of national healthcare coverage to registered refugees, health and social services should be available to all in case of need. According to United nations report, 15%–20% of Ukraine refugees residing in Estonia had specific needs and every third had experienced health problems in 2024. While the report \[18\] also confirmed that healthcare was received when needed in almost nine out of ten cases, an in-depth analysis of HRQoL profile of refugee population can significantly contribute to further policy and service delivery planning to address the perceived needs of the refugees in Estonia. To fill the evidence gap considering HRQoL of Ukrainian refugees, the study aims to compare HRQoL of refugees to the general population in Estonia.

## Methods

The study combined data from two population health surveys conducted in 2024 covering: a) Ukrainian refugees residing in Estonia, and b) Estonian general population. The survey on Health and wellbeing of Ukrainian refugees in Estonia (SHURE) was based on a random sample of 4000 individuals aged 18–64 who had been granted refugee status since 24th February 2022 according to the National Population Registry. Data on general population originates from the 18th wave of Health Behaviour among Estonian Adult Population (HBEP) \[19\]. This biennially repeated cross-sectional survey was based on a representative sample of 16–64-year-old Estonian residents (n = 5,000). Both surveys used mixed-mode (online and postal questionnaires) method and were carried out between March to June 2024. The questionnaires were harmonized, providing comparable data on HRQoL and its correlates for both study populations.

SHURE data included 1,430 responses (334 males and 1,096 females, crude response rate 35.8%) whereas HBEP survey resulted in 2007 responses (835 males and 1,172 females, crude response rate 40.1%). Given the statistically significant differences in demographic distributions between two populations, case-control matching procedure (1:1 exact matching based on sex and age) was applied. Resulting sex and age-matched dataset comprised of 1,249 refugees and 1,249 population controls aged 18–64 years and forms the analytic sample for this study.

EuroQol’s EQ-5D-3L was used to assess HRQoL in both study populations. This widely used generic health status measure includes five dimensions (mobility, self-care, usual activities, pain/discomfort and anxiety/depression) evaluated on a three-level scale \[20\]. The resulting health state description can provide 243 unique health profiles that can be transformed into country-specific index scores. As EQ-5D-3L based value sets for Estonia are not available, European value set \[21\] constructed using VAS valuation data from 11 valuation studies in 6 European countries, was used to derive HRQoL index values.

Both EQ-5D descriptive system and index values were used to compare the refugees and their population controls. Additionally, several socio-demographic and health-related indicators were included in the analysis. For sex, dichotomous classification (male, female) was used. Age (in full years) was used as a continuous variable in modelling whereas descriptive analysis used categorical variable (18–24, 25–34, 35–44, 45–54, 55–64-year). Current marital status was categorized as single, married/cohabiting, divorced/separated. Educational level refers to the highest level of education obtained and was aggregated into three groups: primary or lower, secondary/vocational, and tertiary/higher education. Income was based on average monthly net income per household member and categorized as: \<900, 900–1,299, 1,300–1,700, and \>1,700 Euros. Additional indicator on household’s financial wellbeing during the past month included categories: living comfortably, coping, finding it difficult, finding it very difficult. For health-related variables, self-rated health (good, average, poor) and three indicators on mental health were included. Perceived stress was assessed with a question: “In the past 30 days, have you been stressed, under pressure?” with response options dichotomized as yes/no. Depressiveness was addressed with a question: “In the past 30 days, have you been unhappy, depressed (suffering from depressiveness)?” with dichotomized categories yes/no being used in the analysis. Overtiredness was assessed with a question: “In the past 12 months, how often have you felt overtired?” with response options “almost all the time” or “quite often” referring to being overtired and “seldom” or “never” for no overtiredness.

Descriptive statistics including proportions and their 95% confidence intervals (95% CIs) were used to compare HRQoL by socio-demographic and health indicators in both study populations. Group differences in EQ-5D-3L domains and index values were assessed using z-test with Bonferroni correction applied to account for multiple testing \[22\]. Given the EQ-5D-3L index values are positively skewed and have a ceiling effect, we used Tobit regression. This regression technique is suitable for such data \[23\] and was used to compare the EQ-5D-3L index between Ukrainian refugees and population controls. First, univariate models were run for all independent variables. This was followed by Model 2 where study group variable was additionally adjusted to sex, age, marital status and education. Model 3 included variables from Model 2 and introduced two variables reflecting economic situation. In Model 4, health-related indicators were additionally included. Finally, statistically non-significant variables were sequentially excluded from Model 4 starting from the highest p-value until there were none left which resulted in Model 5. No substitution of missing values was used and the subset with 2180 observations with complete data for all included variables was used in regression models. The results were presented as beta coefficients, indicating the mean change in the reference value within the variable along with the p-values. The analyses were performed using statistical software R 4.3.1 and SPSS 29.0 (IBM Corp).

## Results

<a href="#T1" data-ref-type="table">Table 1</a> presents the socio-demographic and health-related characteristics of the analytical sample. After matching, the sex and age distribution of Ukrainian refugees and general population were identical, but several differences in sociodemographic and health indicators remained statistically significant. Most notably, higher proportion of divorced/widowed and those with tertiary education were found for refugee study group compared to population controls. Substantial differences were also present for both income indicators: 22.9% of controls reported a monthly income exceeding 1700 euros, compared to only 3.6% among refugees and current household subsistence level was assessed as difficult (25.6%) or very difficult (9.4%) by significantly more individuals compared to control group (20.1% and 5.2%, respectively). Statistically significant differences were also found by health indicators with good self-rated health reported by 51.1% of refugees and 59.4% of controls whereas reported stress was more prevalent among the general population (28.5%) compared to refugees (21.7%).

<div id="T1" class="table-wrap">

<div class="caption">

Characteristics of the study sample by socio-demographic and health variables (Estonia, 2024).

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Variable</th>
<th rowspan="3" style="text-align: left;">Category</th>
<th colspan="4" style="text-align: center;">Age &amp; sex matched case-control data</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;">Refugee cases</th>
<th colspan="2" style="text-align: center;">Population controls</th>
</tr>
<tr>
<th style="text-align: center;">n</th>
<th style="text-align: center;">% (95% CI)</th>
<th style="text-align: center;">n</th>
<th style="text-align: center;">% (95% CI)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Total</td>
<td style="text-align: left;">​</td>
<td style="text-align: center;">1,249</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">1,249</td>
<td style="text-align: center;">100</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Sex</td>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">334</td>
<td style="text-align: center;">26.7 (24.3–29.2)</td>
<td style="text-align: center;">334</td>
<td style="text-align: center;">26.7 (24.3–29.2)</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">915</td>
<td style="text-align: center;">73.3 (70.8–75.7)</td>
<td style="text-align: center;">915</td>
<td style="text-align: center;">73.3 (70.8–75.7)</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">Age</td>
<td style="text-align: left;">18–24</td>
<td style="text-align: center;">176</td>
<td style="text-align: center;">14.1 (12.2–16.1)</td>
<td style="text-align: center;">176</td>
<td style="text-align: center;">14.1 (12.2–16.1)</td>
</tr>
<tr>
<td style="text-align: left;">25–34</td>
<td style="text-align: center;">290</td>
<td style="text-align: center;">23.2 (20.9–25.6)</td>
<td style="text-align: center;">290</td>
<td style="text-align: center;">23.2 (20.9–25.6)</td>
</tr>
<tr>
<td style="text-align: left;">35–44</td>
<td style="text-align: center;">365</td>
<td style="text-align: center;">29.2 (26.8–31.8)</td>
<td style="text-align: center;">365</td>
<td style="text-align: center;">29.2 (26.8–31.8)</td>
</tr>
<tr>
<td style="text-align: left;">45–54</td>
<td style="text-align: center;">274</td>
<td style="text-align: center;">21.9 (19.7–24.3)</td>
<td style="text-align: center;">274</td>
<td style="text-align: center;">21.9 (19.7–24.3)</td>
</tr>
<tr>
<td style="text-align: left;">55–64</td>
<td style="text-align: center;">144</td>
<td style="text-align: center;">11.5 (9.8–13.4)</td>
<td style="text-align: center;">144</td>
<td style="text-align: center;">11.5 (9.8–13.4)</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Marital status</td>
<td style="text-align: left;">Single</td>
<td style="text-align: center;">251</td>
<td style="text-align: center;">22.7 (20.3–25.2)</td>
<td style="text-align: center;">301</td>
<td style="text-align: center;">24.2 (21.9–26.6)</td>
</tr>
<tr>
<td style="text-align: left;">Married/cohabiting</td>
<td style="text-align: center;">695</td>
<td style="text-align: left;">62.7 (59.8–65.5)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">829</td>
<td style="text-align: left;">66.6 (64.0–69.2)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Divorced/widowed</td>
<td style="text-align: center;">162</td>
<td style="text-align: center;">14.6 (12.6–16.8)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">114</td>
<td style="text-align: center;">9.2 (7.7–10.9)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Education</td>
<td style="text-align: left;">Primary or less</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">3.7 (2.8–4.9)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">43</td>
<td style="text-align: center;">3.5 (2.5–4.6)</td>
</tr>
<tr>
<td style="text-align: left;">Secondary/vocational</td>
<td style="text-align: center;">617</td>
<td style="text-align: center;">49.8 (47.0–52.5)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">730</td>
<td style="text-align: center;">58.6 (55.8–61.3)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Tertiary</td>
<td style="text-align: center;">577</td>
<td style="text-align: center;">46.5 (43.8–49.3)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">473</td>
<td style="text-align: center;">38.0 (35.3–40.7)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;">Income</td>
<td style="text-align: left;">&lt;900 euros</td>
<td style="text-align: center;">718</td>
<td style="text-align: center;">66.1 (63.2–68.9)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">375</td>
<td style="text-align: center;">30.4 (27.8–33.0)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">900–1,299 euros</td>
<td style="text-align: center;">255</td>
<td style="text-align: center;">23.5 (20.9–26.0)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">337</td>
<td style="text-align: center;">27.3 (24.8–29.8)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">1,300–1700 euros</td>
<td style="text-align: center;">75</td>
<td style="text-align: center;">6.9 (5.4–8.4)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">19.4 (17.2–21.6)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">≥1700 euros</td>
<td style="text-align: center;">39</td>
<td style="text-align: center;">3.6 (2.5–4.7)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">283</td>
<td style="text-align: center;">22.9 (20.6–25.3)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;">Household’s financial wellbeing</td>
<td style="text-align: left;">Living comfortably</td>
<td style="text-align: center;">132</td>
<td style="text-align: center;">12.1 (10.2–14.1)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">249</td>
<td style="text-align: center;">20.0 (17.9–22.3)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Coping</td>
<td style="text-align: center;">579</td>
<td style="text-align: center;">52.9 (50.0–55.9)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">680</td>
<td style="text-align: center;">54.7 (51.9–57.4)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Difficult</td>
<td style="text-align: center;">280</td>
<td style="text-align: center;">25.6 (23.1–28.2)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">250</td>
<td style="text-align: center;">20.1 (17.9–22.4)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Very difficult</td>
<td style="text-align: center;">103</td>
<td style="text-align: center;">9.4 (7.8–11.3)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">65</td>
<td style="text-align: center;">5.2 (4.1–6.6)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Self-rated health</td>
<td style="text-align: left;">Good</td>
<td style="text-align: center;">637</td>
<td style="text-align: center;">51.1 (48.3–53.9)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">739</td>
<td style="text-align: center;">59.4 (56.7–62.2)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Average</td>
<td style="text-align: center;">525</td>
<td style="text-align: center;">42.1 (39.4–44.9)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">409</td>
<td style="text-align: center;">32.9 (30.3–35.5)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Poor</td>
<td style="text-align: center;">84</td>
<td style="text-align: center;">6.7 (5.3–8.1)</td>
<td style="text-align: center;">95</td>
<td style="text-align: center;">7.6 (6.2–9.1)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Stress</td>
<td style="text-align: left;">No</td>
<td style="text-align: center;">970</td>
<td style="text-align: center;">78.3 (75.9–80.5)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">888</td>
<td style="text-align: center;">71.5 (68.9–74.0)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">269</td>
<td style="text-align: center;">21.7 (19.5–24.1)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: center;">354</td>
<td style="text-align: center;">28.5 (26.0–31.1)<a href="#Tfn1" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Depressiveness</td>
<td style="text-align: left;">No</td>
<td style="text-align: center;">899</td>
<td style="text-align: center;">72.3 (69.8–74.8)</td>
<td style="text-align: center;">933</td>
<td style="text-align: center;">75.3 (72.8–77.6)</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">344</td>
<td style="text-align: center;">27.7 (25.2–30.2)</td>
<td style="text-align: center;">306</td>
<td style="text-align: center;">24.7 (22.4–27.2)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Overtiredness</td>
<td style="text-align: left;">No</td>
<td style="text-align: center;">604</td>
<td style="text-align: center;">48.5 (45.7–51.3)</td>
<td style="text-align: center;">588</td>
<td style="text-align: center;">47.3 (44.5–50.0)</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">641</td>
<td style="text-align: center;">51.5 (48.7–54.3)</td>
<td style="text-align: center;">656</td>
<td style="text-align: center;">52.7 (50.0–55.5)</td>
</tr>
</tbody>
</table>

Statistically significant (p \< 0.05) differences between column proportions.

</div>

<a href="#F1" data-ref-type="fig">Figure 1</a> illustrates the HRQoL by EQ-5D-3L descriptive system in both study groups. Any problems with mobility were reported by 13.4% of refugees and 16.7% of controls (p \< 0.05). Similarly, refugees had significantly lower proportion reporting any problems with self-care (2.9% vs. 4.9%), usual activities (14.7% vs. 18.5%), whereas a significantly higher proportion of refugees reported any problems on the pain/discomfort (59.6% vs. 52.8%; p \< 0.05) and anxiety/depression (63.5% vs. 54.7%, p \< 0.05) domains compared the general population. The mean EQ-5D index value in the refugee group was 0.742 (95% CI 0.732–0.752) and 0.763 (95% CI 0.752–0.774) in the general population group, i.e., the refugees had significantly (p = 0.005) lower HRQoL compared to the general population. The EQ-5D-3L index value 1 referring to perfect health state was reported by 22.6% in the refugee and 26.0% in the control group (non-significant difference); the overall distribution of EQ-5D-3L index values in both study groups is given in <a href="#s11" data-ref-type="sec">Supplementary Material</a>.

<figure id="F1">
<p><img src="ijph-71-1608807-g001.jpg" alt="Stacked bar charts display the EQ-5D-3L responses for refugee cases and population controls across five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. Each dimension compares the proportion of individuals with no problems, moderate problems, and severe problems, with larger sections indicating more issues among refugee cases compared to population controls." /></p>
<figcaption>Distribution of responses by health-related quality of life dimension of the refugees versus general population (Estonia, 2024).</figcaption>
</figure>

In univariate regression models (<a href="#T2" data-ref-type="table">Table 2</a>), all variables considered in the study demonstrated significant association with HRQoL. Notably, refugees had significantly lower EQ-5D-3L index score (estimate −0.028, p = 0.008) compared to control group. This difference was slightly attenuated (estimate −0.028, p = 0.018) in model 2 adjusted to sex, age, marital status and education. While females and older respondents had lower HRQoL estimate, being married or cohabiting was associated with higher EQ-5D index value compared to being single. The effects of education on HRQoL were statistically non-significant in Model 2. After inclusion of income and households’ financial situation (Model 3), the difference between refugees and population controls became non-significant. While only group difference between 1,300 and 1700 vs. \<900 euros was significant for income, indicator of household’s financial wellbeing demonstrated a graded association with HRQoL. This effect was heavily attenuated in Model 4 which introduced self-rated health and three mental health indicators. While these indicators were statistically significant predictors of HRQoL, variables of study group, sex, marital status, education and income were rendered statistically non-significant. After sequentially omitting marital status, education and income from the model, the difference in HRQoL by study group became statistically significant. Although the effect was relatively modest compared to health indicators included in the model, refugees had lower EQ-5D-3L index score (estimate −0.017, p = 0.029) compared to control group. In both study groups, females, older respondents, those having financial problems in the household and poorer health had lower HRQoL based on our data.

<div id="T2" class="table-wrap">

<div class="caption">

Tobit regression models describing the association between predictor variables and health-related quality of life index score (Estonia, 2024).

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Predictor variable</th>
<th colspan="2" style="text-align: center;">Model 1 (univariate)</th>
<th colspan="2" style="text-align: center;">Model 2</th>
<th colspan="2" style="text-align: center;">Model 3</th>
<th colspan="2" style="text-align: center;">Model 4</th>
<th colspan="2" style="text-align: center;">Model 5 (final)</th>
</tr>
<tr>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">P-value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">P-value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">P-value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">P-value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">P-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Refugees vs. controls</td>
<td style="text-align: center;"><strong>−0.028</strong></td>
<td style="text-align: center;">0.008</td>
<td style="text-align: center;"><strong>−0.024</strong></td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;">−0.001</td>
<td style="text-align: center;">0.932</td>
<td style="text-align: center;">−0.009</td>
<td style="text-align: center;">0.279</td>
<td style="text-align: center;"><strong>−0.017</strong></td>
<td style="text-align: center;">0.029</td>
</tr>
<tr>
<td style="text-align: left;">Sex: female vs. men</td>
<td style="text-align: center;"><strong>−0.049</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.039</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.030</strong></td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;">−0.013</td>
<td style="text-align: center;">0.137</td>
<td style="text-align: center;"><strong>−0.017</strong></td>
<td style="text-align: center;">0.049</td>
</tr>
<tr>
<td style="text-align: left;">Age (cont.)</td>
<td style="text-align: center;"><strong>−0.003</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.003</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.002</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.002</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.002</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Marital: married/cohabiting vs. single</td>
<td style="text-align: center;">0.009</td>
<td style="text-align: center;">0.489</td>
<td style="text-align: center;"><strong>0.034</strong></td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;"><strong>0.029</strong></td>
<td style="text-align: center;">0.021</td>
<td style="text-align: center;">0.014</td>
<td style="text-align: center;">0.150</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Marital: divorced/separated/widowed vs. single</td>
<td style="text-align: center;"><strong>−0.078</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">−0.028</td>
<td style="text-align: center;">0.154</td>
<td style="text-align: center;">−0.017</td>
<td style="text-align: center;">0.378</td>
<td style="text-align: center;">−0.015</td>
<td style="text-align: center;">0.285</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Education: secondary/vocational vs. primary</td>
<td style="text-align: center;"><strong>−0.058</strong></td>
<td style="text-align: center;">0.050</td>
<td style="text-align: center;">−0.045</td>
<td style="text-align: center;">0.124</td>
<td style="text-align: center;">−0.054</td>
<td style="text-align: center;">0.056</td>
<td style="text-align: center;">−0.034</td>
<td style="text-align: center;">0.114</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Education: tertiary vs. primary</td>
<td style="text-align: center;">−0.044</td>
<td style="text-align: center;">0.136</td>
<td style="text-align: center;">−0.026</td>
<td style="text-align: center;">0.386</td>
<td style="text-align: center;">−0.051</td>
<td style="text-align: center;">0.076</td>
<td style="text-align: center;">−0.034</td>
<td style="text-align: center;">0.125</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Income: 900–1,299 vs. &lt;900</td>
<td style="text-align: center;"><strong>0.048</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0.016</td>
<td style="text-align: center;">0.192</td>
<td style="text-align: center;">0.013</td>
<td style="text-align: center;">0.159</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Income: 1,300–1700 vs. &lt;900</td>
<td style="text-align: center;"><strong>0.080</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>0.032</strong></td>
<td style="text-align: center;">0.047</td>
<td style="text-align: center;">0.023</td>
<td style="text-align: center;">0.058</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Income: &gt;1700 vs. &lt;900</td>
<td style="text-align: center;"><strong>0.096</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0.021</td>
<td style="text-align: center;">0.224</td>
<td style="text-align: center;">0.020</td>
<td style="text-align: center;">0.138</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Financial wellbeing: coping vs. well off</td>
<td style="text-align: center;"><strong>−0.066</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.050</strong></td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">−0.005</td>
<td style="text-align: center;">0.631</td>
<td style="text-align: center;">−0.010</td>
<td style="text-align: center;">0.337</td>
</tr>
<tr>
<td style="text-align: left;">Financial wellbeing: finding it difficult vs. well off</td>
<td style="text-align: center;"><strong>−0.160</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.136</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.036</strong></td>
<td style="text-align: center;">0.006</td>
<td style="text-align: center;"><strong>−0.046</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Financial wellbeing: Very difficult vs. well off</td>
<td style="text-align: center;"><strong>−0.240</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.202</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.041</strong></td>
<td style="text-align: center;">0.025</td>
<td style="text-align: center;"><strong>−0.053</strong></td>
<td style="text-align: center;">0.002</td>
</tr>
<tr>
<td style="text-align: left;">Self-rated health: average vs. good</td>
<td style="text-align: center;"><strong>−0.205</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.129</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.129</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Self-rated health: poor vs. good</td>
<td style="text-align: center;"><strong>−0.402</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.252</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.254</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Stress: yes vs. no</td>
<td style="text-align: center;"><strong>−0.210</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.067</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.068</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Depressiveness: yes vs. no</td>
<td style="text-align: center;"><strong>−0.217</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.077</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.077</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Overtiredness: yes vs. no</td>
<td style="text-align: center;"><strong>−0.219</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><strong>−0.098</strong></td>
<td style="text-align: center;">&lt;0.001</td>
<td style="text-align: center;"><strong>−0.098</strong></td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>(Intercept)</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><strong> <em>0.938</em> </strong></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
<td style="text-align: center;"><strong> <em>0.975</em> </strong></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
<td style="text-align: center;"><strong> <em>1.046</em> </strong></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
<td style="text-align: center;"><strong> <em>1.044</em> </strong></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Log(scale)</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>−1.468</em></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
<td style="text-align: center;"><em>−1.508</em></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
<td style="text-align: center;"><em>−1.790</em></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
<td style="text-align: center;"><em>−1.786</em></td>
<td style="text-align: center;"><em>&lt;0.001</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Log-likelihood</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>−466.8</em></td>
<td style="text-align: center;">​</td>
<td style="text-align: center;"><em>−393.4</em></td>
<td style="text-align: center;">​</td>
<td style="text-align: center;"><em>137.7</em></td>
<td style="text-align: center;">​</td>
<td style="text-align: center;"><em>130.4</em></td>
<td style="text-align: center;">​</td>
</tr>
<tr>
<td style="text-align: left;"><em>d.f</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>na</em></td>
<td style="text-align: center;"><em>9</em></td>
<td style="text-align: center;">​</td>
<td style="text-align: center;"><em>15</em></td>
<td style="text-align: center;">​</td>
<td style="text-align: center;"><em>20</em></td>
<td style="text-align: center;">​</td>
<td style="text-align: center;"><em>13</em></td>
<td style="text-align: center;">​</td>
</tr>
</tbody>
</table>

Bold values represents the P-value \< 0.05. Italic values represents Additional model parameters.

</div>

## Discussion

Using sex- and age-matched survey data on HRQoL of Ukrainian refugees and of Estonian general population, the results demonstrated significant HRQoL differences between the study groups. While refugees reported less problems with mobility, self-care and usual activities, a higher prevalence of pain/discomfort and anxiety/depression was found compared to the control group. The differences in reported problems on the HRQoL dimensions translated into slightly lower EQ-5D-3L index score among Ukrainian refugees. This difference in EQ-5D-3L index score persisted after adjusting for a range of socio-demographic and health-related indicators that demonstrated significant variation between the study groups.

Before discussing these findings in detail, some aspects regarding the data and methods should be considered. While the declining response rates are universal challenge in survey research and also documented for HBEP study \[19\], resulting non-response bias might have affected the data. This is evident in the male-to-female ratio in the refugee survey, which declined from 0.48 in the sample to 0.31 in the data and contrasts with corresponding 0.72 ratio in HBEP data. However, predominant share of women among adult refugees is a common indication of the migrant population fleeing a conflict and conveys, in addition to demographic variations, also distinct epidemiological characteristics. The use of sex- and age-matching was thus an important measure to mitigate the effects of demographic variation in two datasets. However, as the refugee-matched control group has a different demographic structure, the current results cannot be directly generalized to Estonian general population. Secondly, while SHURE study included wide range of indicators addressing the migratory background, change in living conditions etc., corresponding indicators were not present in the HBEP questionnaire and direct comparison was limited only variables available in both datasets. However, despite the inclusion of key socio-demographic and health indicators, it is unlikely that the set of variables accounts for total variance in the dependent variable. Thus, potential residual bias should be considered when interpreting the results. Third, the modelling strategy might have also affected the results. We have conducted a sensitivity analysis using OLS regression which yielded very similar results across all models (see <a href="#s11" data-ref-type="sec">Supplementary Material</a>). Also, models used stepwise removal of non-significant variables which might yield biased coefficients and p-values \[24\]. However, the choice of variables to the analysis reflected those that all data is based on self-reports and could not be validated externally. This might have impact on the results either due to underreport or overreport certain health conditions, particularly mental health symptoms as found in previous study \[25\]. All these considerations are inherent to studies employing similar designs and, as such, do not represent unique or additional limitations to the present study.

The key finding is the persistence of lower HRQoL among refugee group, even after adjusting for a range of socio-demographic and health-related covariates. However, the difference (−0.017 EQ-5D units) compared to the population controls was very minor. Based on the findings of a recent systematic review \[26\], the minimally important difference was −0.02 for deteriorated EQ-5D-3L scores. While the lower EQ-5D index score might not convey clinically significant difference in HRQoL, these results still suggests that refugee status itself may entail unique and enduring stressors that are not adequately captured by demographic or health indicators. Despite similar or slightly better outcomes in physical health domains such as mobility, self-care, and usual activities, refugees exhibited significantly higher levels of problems in the EQ-5D dimensions related to pain/discomfort and anxiety/depression. This corresponds to an earlier systematic review on refugee HRQoL using WHOQOL-Bref instrument \[6\], where refugees had higher scores for the physical and lower scores for psychological domain compared to general population. In our data, the observed difference in the anxiety/depression domain (63.5% vs. 54.7%) may reflect both pre-migration stressors such as exposure to armed conflict and loss, as well as post-migration challenges including acculturation stress, housing insecurity, and separation from family members \[27, 28\]. The latter might be reflected in the distribution of marital status variable, where the refugee population had significantly higher share of divorced/widowed and lower proportion of married/cohabiting individuals compared to population controls. Similarly, a recent study on Ukrainian refugees in Poland \[29\] reported acute stress prevalence exceeding 90% which is indicative of high level of trauma. Although data on post-traumatic stress disorder was not available for general population, 79.6% of refugees in SHURE data had experienced traumatic experience \[30\]. This contrasts with the lower reporting of perceived stress among refugees compared to population controls (21.7% vs. 28.5%, p \< 0.05). It is also plausible that the difference in perceived stress prevalence might stem from peer comparison used in the response options where categories “yes, more than people on the average” or “yes, but no more than people on the average” might have different baseline for refugees and population controls. Also, it is likely that refugees from active conflict zones may be more likely to somatize psychological distress or may have varying thresholds for labelling emotional discomfort as a mental health concern. While the differential item reporting has also potential implications for EQ-5D-3L assessments, the specific topic warrants further research but is out of the scope of the current study.

The results also emphasize that refugees do not exhibit uniformly worse HRQoL compared to host population. In our data, higher proportion of refugees reported no problems on EQ-5D-3L dimensions mobility, self-care, and usual activities. One potential explanation for this finding is the “healthy migrant effect” that suggest individuals who are healthier or more resilient are more likely to migrate \[31\]. While it is mostly applicable to voluntary migration, a positive self-selection may also be present among refugees, particularly those who undertake arduous journeys or who are resettled through official humanitarian programs requiring minimal health screening \[32\]. In the context of Ukrainian refugee crisis, a recent study from Italy \[33\] also reported lower non-communicable disease prevalence among registered refugees compared to rates usually found in the Ukraine population. Indirect support for this argument in our data relates to educational variation where refugees had substantially higher proportion of tertiary education compared to controls (46.5% vs. 38.0%) suggesting that younger, more mobile, but also physically healthier individuals were more likely to emigrate. This is also supported by another recent study in Estonia where 60% of refugees were in ages 18–59 years and individuals \>60 years accounted for \<10% of refugees \[18\]. However, this advantage in physical health may be short-lived, as psychosocial stressors due to displacement, unemployment and other similar factors often contribute to health deterioration over time \[34\]. Consistent with broader public health literature, this study found that both economic vulnerability and perceived poor health were strongly associated with reduced EQ-5D-3L index scores in both study groups. Although the effects of education and income became non-significant after inclusion of health variables in our regression model, the relative measure on household income remained a strong predictor of HRQoL. Based on SHURE survey data \[30\], 34.6% of refugees in Estonia reported financial problems, substantial increase from 15.1% before emigration. The key priority needs for refugee households from Ukraine in Estonia are the need to secure employment/livelihoods support (32%), language courses (33%), access to healthcare services (22%) and training of adults (17%) \[18\]. Therefore, in order to maintain and improve health of the refugees, concentrated intersectoral efforts are needed that address the wider social determinants of health, such as income security, housing, employment, and access to healthcare.

These findings contribute to the literature on refugee HRQoL and extend the knowledge on HRQoL of Ukrainian refugees in the context of ongoing refugee crisis in Europe. The findings underline the complex nature of refugee health and offer a nuanced view of both the vulnerabilities and potential resilience factors in this population. The findings highlight the importance of addressing mental health needs and socioeconomic stressors through integrated interventions. Future longitudinal research is needed to monitor changes in HRQoL over time and evaluate the effectiveness of policy interventions in mitigating health disparities between refugee and host populations.

### Ethics Statement

The studies involving humans were approved by Human Research Ethics Commitee of National Institute for Health Development. The studies were conducted in accordance with the local legislation and institutional requirements. The participants provided their written informed consent to participate in this study.

### Author Contributions

RR designed the study and all authors participated in applying for the funding. RR and JS conducted the analysis and together with GO wrote the initial draft for the manuscript. TL and JH provided critical feedback and revised the manuscript. All authors contributed to the article and approved the submitted version.

### Author Disclaimer

Views expressed by the authors in the publication do not necessarily reflect the views of the EuroQol Foundation.

### Conflict of Interest

Author TL was employed by Fourth View Consulting.

The remaining authors declare that they do not have any conflicts of interest.

### Generative AI Statement

The author(s) declared that generative AI was not used in the creation of this manuscript.

Any alternative text (alt text) provided alongside figures in this article has been generated by Frontiers with the support of artificial intelligence and reasonable efforts have been made to ensure accuracy, including review by the authors wherever possible. If you identify any issues, please contact us.

### Supplementary Material

The Supplementary Material for this article can be found online at: <https://www.ssph-journal.org/articles/10.3389/ijph.2026.1608807/full#supplementary-material>

## References

1. United Nations. High Commissioner for Refugees (UNHCR) Operational Data Portal. In: Ukraine Refugee Situation (2024). Available online at: https://data.unhcr.org/en/situations/ukraine (Accessed January 9, 2026).

2. LabbertonAS HansenTM SkogheimTSYH . Healthcare Needs Among Refugees from Ukraine Arriving in Norway During 2022. Oslo: Norwegian Institute of Public Health (2023).

3. LebanoA HamedS BradbyH Gil-SalmerónA Durá-FerrandisE Garcés-FerrerJ Migrants’ and Refugees’ Health Status and Healthcare in Europe: A Scoping Literature Review. BMC Public Health (2020) 20(1):1039. 10.1186/s12889-020-08749-8 32605605 PMC7329528

4. EssexR GovintharjahP IssaR KalocsányiováE LakikaD MarkowskiM Health Related Quality of Life Amongst Refugees: A Meta Analysis of Studies Using the SF-36. J Immigr Minor Health (2024) 26(5):925–35. 10.1007/s10903-024-01615-4 38958897 PMC11413143

5. SengoelgeM NissenA SolbergØ . Post-Migration Stressors and Health-Related Quality of Life in Refugees from Syria Resettled in Sweden. Int J Environ Res Public Health (2022) 19(5):2509. 10.3390/ijerph19052509 35270200 PMC8909133

6. GagliardiJ BrettschneiderC KönigH-H . Health-Related Quality of Life of Refugees: A Systematic Review of Studies Using the WHOQOL-Bref Instrument in General and Clinical Refugee Populations in the Community Setting. Conflict and Health (2021) 15(1):44. 10.1186/s13031-021-00378-1 34078413 PMC8173726

7. BauerJM BrandT ZeebH . Pre-Migration Socioeconomic Status and Post-Migration Health Satisfaction Among Syrian Refugees in Germany: A Cross-Sectional Analysis. Plos Med (2020) 17(3):e1003093. 10.1371/journal.pmed.1003093 32231355 PMC7108713

8. BuchcikJ BoruttaJ NickelS von dem KnesebeckO WestenhöferJ . Health-Related Quality of Life Among Migrants and Natives in Hamburg, Germany: An Observational Study. J Migration Health (2021) 3:100045. 10.1016/j.jmh.2021.100045 34405190 PMC8352133

9. LuCH WangPX LeiYX LuoZC . Influence of Health-Related Quality of Life on Health Service Utilization in Chinese Rural-To-Urban Female Migrant Workers. Health Quality Life Outcomes (2014) 12:121. 10.1186/s12955-014-0121-4 25123983 PMC4168158

10. AlhaffarM JanosS . Public Health Consequences After Ten Years of the Syrian Crisis: A Literature Review. Glob Health (2021) 17(1):111. 10.1186/s12992-021-00762-9 34538248 PMC8449996

11. BansakK HainmuellerJ HangartnerD . Europeans' Support for Refugees of Varying Background Is Stable over Time. Nature (2023) 620(7975):849–54. 10.1038/s41586-023-06417-6 37558879 PMC10447233

12. XuerebS . Emotions, Perceived Threat, Prejudice, and Attitudes Towards Helping Ukrainian, Syrian, and Somali Asylum Seekers. PloS One (2023) 18(9):e0290335. 10.1371/journal.pone.0290335 37703255 PMC10499223

13. Sosa PopovicL WelfensN . Same, Same but Different? A Discourse Network Analysis of the Eu's Framings of Refugee Arrivals in 2015 and 2022. J Ethn Migr Stud (2025) 51(3):609–32. 10.1080/1369183X.2024.2431053 39845309 PMC11750152

14. KonstantinovV AlexanderR IsralowitzR . Depression and Quality of Life Among Ukrainian Adults Relocated to Russia. J Loss Trauma (2023) 28(6):493–503. 10.1080/15325024.2023.2216986

15. BuchcikJ KovachV AdedejiA . Mental Health Outcomes and Quality of Life of Ukrainian Refugees in Germany. Health Qual Life Outcomes (2023) 21(1):23. 10.1186/s12955-023-02101-5 36894946 PMC9996949

16. HansenT LabbertonAS SkogheimTS HellandY . Self-Reported Health Status Using EQ-5D-5L Among Refugees from Ukraine Arriving in Norway in 2022. Eur J Public Health (2023) 33(Suppl. ment_2):ckad160.1636. 10.1093/eurpub/ckad160.1636

17. Sotsiaalkindlustusamet. Statistika . Available online at: https://www.sotsiaalkindlustusamet.ee/asutus-uudised-ja-kontakt/praktiline-teave/statistika#ua-stat (Accessed January 9, 2026)

18. United Nations High Commissioner for Refugees (UNHCR). Estonia. Socio-Economic Insights Survey 2024. Regional Refugee Response for the Ukraine Situation (2024).

19. ReileRPA SaavasteJ . Eesti täiskasvanud rahvastiku tervisekäitumise uuring 2024. Metoodika ja standardtabelite kogumik [Health Behaviour Among Estonian Adult Population. Methodology and standard tables]. Tallinn: Tervise Arengu Instituut (2025).

20. DevlinN ParkinD JanssenB . An Introduction to EQ-5D Instruments and Their Applications. Springer International Publishing (2020). p. 1–22.

21. GreinerW WeijnenT NieuwenhuizenM OppeS BadiaX BusschbachJ A Single European Currency for EQ-5D Health States. Results from a Six-Country Study. The Eur Journal Health Economics (2003) 4(3):222–31. 10.1007/s10198-003-0182-5 15609189

22. AickinM GenslerH . Adjusting for Multiple Testing when Reporting Research Results: The Bonferroni vs Holm Methods. Am Journal Public Health (1996) 86(5):726–8. 10.2105/ajph.86.5.726 8629727 PMC1380484

23. AustinPC EscobarM KopecJA . The Use of the Tobit Model for Analyzing Measures of Health Status. Qual Life Res (2000) 9(8):901–10. 10.1023/a:1008938326604 11284209

24. HarrellJFE . Regression Modeling Strategies: With Applications to Linear Models, Logistic and Ordinal Regression, and Survival Analysis. 2nd ed. Cham: Springer (2015).

25. MenoldN BiddleL von HermanniH KadelJ BozorgmehrK . Ensuring Cross-Cultural Data Comparability by Means of Anchoring Vignettes in Heterogeneous Refugee Samples. BMC Med Res Methodol (2023) 23(1):213. 10.1186/s12874-023-02015-2 37759183 PMC10536699

26. ChengLJ ChenLA ChengJY HerdmanM LuoN . Systematic Review Reveals that EQ-5D Minimally Important Differences Vary with Treatment Type and May Decrease with Increasing Baseline Score. J Clin Epidemiol (2024) 174:111487. 10.1016/j.jclinepi.2024.111487 39084578

27. KirmayerLJ NarasiahL MunozM RashidM RyderAG GuzderJ Common Mental Health Problems in Immigrants and Refugees: General Approach in Primary Care. Can Med Assoc J (2011) 183(12):E959–E67. 10.1503/cmaj.090292 20603342 PMC3168672

28. LushchakO VelykodnaM BolmanS StrilbytskaO BerezovskyiV StoreyKB . Prevalence of Stress, Anxiety, and Symptoms of Post-Traumatic Stress Disorder Among Ukrainians After the First Year of Russian Invasion: A Nationwide Cross-Sectional Study. Lancet Reg Health Eur (2024) 36:100773. 10.1016/j.lanepe.2023.100773 38019977 PMC10665943

29. KordelP RządeczkaM Studenna-SkrukwaM Kwiatkowska-MoskalewiczK GoncharenkoO MoskalewiczM . Acute Stress Disorder Among 2022 Ukrainian War Refugees: A Cross-Sectional Study. Front Public Health (2024) 12:1280236. 10.3389/fpubh.2024.1280236 38550313 PMC10976942

30. ReileR . Mental Health and Well-Being of Ukrainian War Refugees in Estonia. Preliminary Results from a Population-Based Survey. In: Mental Health During the War in Ukraine: Challenges and Initiatives: European Federation of Psychologists Associations (EFPA) (2024).

31. KennedyS KiddMP McDonaldJT BiddleN . The Healthy Immigrant Effect: Patterns and Evidence from Four Countries. J Int Migration Integration (2015) 16(2):317–32. 10.1007/s12134-014-0340-x

32. MalmusiD Ortiz-BarredaG . Health Inequalities in Immigrant Populations in Spain: A Scoping Review. Revista espanola de salud publica (2014) 88(6):687–701. 10.4321/S1135-57272014000600003 25418561

33. ParenteP MelnykA LombardoP VillaniL GrossiA GolettiM Demographic and Epidemiological Characteristics of Ukrainian Refugees in an Italian Local Health Authority. Eur J Public Health (2023) 33(5):815–20. 10.1093/eurpub/ckad130 37552052 PMC10567240

34. PriebeS GiaccoD El-NagibR . Public Health Aspects of Mental Health Among Migrants and Refugees: A Review of the Evidence on Mental Health Care for Refugees, Asylum Seekers and Irregular Migrants in the WHO European Region. Copenhagen: WHO Regional office for Europe (2016).27809423

[^1]: This Original Article is part of the IJPH Special Issue “The Health of Displaced People: A Challenge for Epidemiology and Public Health”

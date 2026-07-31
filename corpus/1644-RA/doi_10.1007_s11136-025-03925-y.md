---
project_id: "1644-RA"
work_id: "doi:10.1007/s11136-025-03925-y"
doi: "10.1007/s11136-025-03925-y"
pmid: "39998755"
pmcid: "PMC12119780"
title: "Associations between financial toxicity, health-related quality of life, and well-being in Indonesian patients with breast cancer"
journal: "Quality of Life Research"
publication_date: "2025-02-25"
volume: "34"
issue: "6"
authors:
  - name: "Stevanus Pangestu"
    orcid: "http://orcid.org/0000-0003-2546-9449"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Fredrick Dermawan Purba"
    orcid: "http://orcid.org/0000-0002-7336-3043"
    affiliation_ids:
      - "Aff3"
  - name: "Hari Setyowibowo"
    orcid: "http://orcid.org/0000-0001-5091-3180"
    affiliation_ids:
      - "Aff3"
  - name: "Clara Mukuria"
    orcid: "http://orcid.org/0000-0003-4318-1481"
    affiliation_ids:
      - "Aff4"
  - name: "Fanni Rencz"
    orcid: "http://orcid.org/0000-0001-9674-620X"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/01vxfm326grid.17127.320000 0000 9234 5858Department of Health Policy, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff2"
    name: "https://ror.org/01vxfm326grid.17127.320000 0000 9234 5858Doctoral School of Business and Management, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff3"
    name: "https://ror.org/00xqf8t64grid.11553.330000 0004 1796 1481Department of Psychology, Faculty of Psychology, Universitas Padjadjaran, Bandung, Indonesia"
  - id: "Aff4"
    name: "https://ror.org/05krs5044grid.11835.3e0000 0004 1936 9262School of Medicine and Population Health, University of Sheffield, Sheffield, UK"
keywords:
  - "Breast cancer"
  - "EQ-5D"
  - "EQ-HWB"
  - "Financial toxicity"
  - "Heath-related quality of life"
  - "Well-being"
licence: "cc-by"
source_file: "input/projects/1644-RA/papers/doi_10.1007_s11136-025-03925-y.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12119780/fullTextXML"
source_method: "epmc_xml"
source_sha256: "ef17c80b21ef72b35feb1c2da99f6221380b177f17620f7ac81d60f0c78597f8"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Associations between financial toxicity, health-related quality of life, and well-being in Indonesian patients with breast cancer

## Abstract

### Objectives

Financial toxicity (FT) is the impairment of financial well-being experienced by patients with cancer, categorized into subjective (SFT) and objective (OFT) forms. This study aimed to investigate the associations between FT, health-related quality of life, and overall well-being in patients with breast cancer.

### Methods

We analyzed baseline data from a single-center longitudinal study in Indonesia. Patients completed the EQ-5D-5L, EQ Health and Wellbeing (EQ-HWB), COST: A FACIT Measure of Financial Toxicity (FACIT-COST, for measuring SFT), and OFT-related questions. Ordinal logistic regression was used to examine the associations between FT and selected EQ-5D-5L and EQ-HWB items. Multivariable linear regression was used to assess the associations of FT and EQ-5D-5L and EQ-HWB-S index values. The main regression models were adjusted for socio-demographic and clinical factors such as age, income, metastasis status, and symptoms.

### Results

The survey included 300 female patients with breast cancer undergoing treatment (mean age = 51). Overall, 21% experienced high SFT (FACIT-COST ≤ 17.5) and 51% reported any OFT (e.g., incurring debt). Adjusted for covariates, higher SFT was associated with more problems in EQ-5D-5L pain/discomfort and anxiety/depression, and in EQ-HWB exhaustion, anxiety, sadness/depression, frustration, pain, and discomfort. OFT was associated with more problems in exhaustion. Higher SFT was associated with lower EQ-5D-5L and EQ-HWB-S index values, with explained variances of 46.3% for EQ-HWB-S and 31.2% for EQ-5D-5L.

### Conclusions

This study is the first to explore the associations between financial toxicity, EQ-5D-5L, and EQ-HWB outcomes in breast cancer. Our findings provide insight into the cancer burden and its link to health and well-being.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-025-03925-y.

## Introduction

Patients with cancer worldwide often face considerable financial burdens \[1\]. The experienced financial challenges can adversely impact their financial well-being, which is the perceived ability to sustain living standards and achieve financial freedom \[2\]. The term ‘financial toxicity’ (FT) describes the impairment of financial well-being of patients due to cancer diagnosis and its associated care \[3\]. FT has been reported across many countries, regardless of income levels or healthcare systems \[4, 5\]. If unaddressed, FT can lead to treatment non-adherence, reduced health-related quality of life (HRQoL), and worse health and survival outcomes \[6–9\].

In general, FT can be assessed both objectively and subjectively \[10–12\]. Objective FT (OFT) is measured using quantifiable financial metrics (e.g., out-of-pocket expenditure amount or its ratio to household income) or questions on financial coping strategies (e.g., incurring loan and selling assets). Meanwhile, subjective FT (SFT) is the perceived distress arising from the financial burden of their diagnosis and treatment. The measurement of SFT is typically self-reported by the patients using patient-reported outcome measures, such as the COST: A FACIT Measure of Financial Toxicity (FACIT-COST) and Socioeconomic Well-Being Scale (SEWBS) \[13, 14\].

There is an increasing body of literature exploring the association between FT and HRQoL in patients and survivors of cancer \[15, 16\]. Significant correlations were found between high levels of both OFT and SFT and reduced overall HRQoL. Specifically, FT has shown associations with a number of HRQoL domains (e.g., social and mental health), measured using instruments such as the European Organization for Research and Treatment of Cancer of Life Questionnaire Core 30 (EORTC QLQ-C30), EQ-5D-5L, Functional Assessment of Cancer Therapy – General (FACT-G), Patient-Reported Outcomes Measurement Information System-29 (PROMIS-29), and 12-Item Short-Form Health Survey (SF-12) \[15, 16\]. However, most FT studies have been performed in high-income and English-speaking countries \[15, 16\]. Further research is needed in low-and-middle-income countries (LMICs) to better understand FT in different cultures and socio-demographic settings \[10, 17–20\].

While there has been a surge of FT studies examining its associations with HRQoL, very little is known about the relationship between FT and well-being. There are various definitions of well-being; for example, the World Health Organization defines the well-being construct as a broader spectrum of dimensions compared to HRQoL, which predominantly focuses on physical, psychological, and social domains of health \[21–24\]. In an earlier study, SFT was associated with the environment domain of well-being, measured using the World Health Organization Quality of Life Brief Version (WHOQOL-BREF) instrument \[25\]. Evidence suggests that the world is moving toward universal health coverage to ensure access to health care without financial hardship \[26\]. However, FT persists as a major challenge in oncology care across many countries. A better understanding of the relationships between FT, HRQoL, and well-being may offer valuable insights into how financial challenges relate to various health and well-being domains, helping to shape health and social policies that support patients and their households.

Breast cancer is the most prevalent cancer worldwide, including in Indonesia \[27\]. Recent findings also suggest that FT in breast cancer occurs in more than twice as many patients in LMICs compared with their high-income counterparts \[20\]. Indonesia is a middle-income country where cancer is a major cause of mortality and the second costliest chronic disease financed by the country’s single-payer universal health system \[28\]. Despite the presence of a public health system, patients may face challenges such as underinsurance, which does not cover substantial non-healthcare, cancer-related costs (e.g., transportation to healthcare facilities and caregiver fees), and the uneven distribution of medical professionals and equipment \[15\].

Therefore, this study aims to investigate the associations between FT, HRQoL, and well-being outcomes in female patients with breast cancer in Indonesia. We hypothesize that FT is negatively associated with HRQoL and well-being.

## Methods

This study was conducted in accordance with the Indonesian Health Research and Development Ethical Guidelines and Standards \[29\]. Ethics approval was granted by the Research Ethics Committee of the Hasan Sadikin General Hospital (LB.02.01/X.6.5/284/2023).

### Study design and patients

This study analyzed baseline data from a single-center longitudinal study conducted in Indonesia from September 2023 to March 2024 \[30, 31\]. Data were collected at the Hasan Sadikin General Hospital Bandung, a primary public referral hospital in West Java. Inclusion criteria for patients were: (i) female, (ii) at least 18 years of age, (iii) diagnosed with breast cancer of any type and stage, (iv) undergoing any treatment, (v) possessed the cognitive ability to complete the survey, v) fluent in Indonesian, and (vi) provided written informed consent. Patients in the initial round of therapy (e.g., chemotherapy and immunotherapy) were excluded. The recruitment of the patients was performed by research assistants and overseen by the chief oncologist and team of nurses. Patients were approached for survey participation prior to their consultation or treatment session in the waiting area of the hospital’s oncology department. Two separate paper-and-pencil questionnaires were prepared: one for the patients and the other for the nurses.

The patients’ questionnaire included standardized measures in the official Indonesian language version, presented in a fixed order: EQ-HWB, EQ-5D-5L, and FACIT-COST. Patients were also asked to report their socio-demographic background (age, marital status, education, employment status, ethnicity, residential setting, number of children living in the same household, net monthly household income, and health insurance status), symptoms experienced over the past week, and respond to a question on OFT. Three trained research assistants, present in the waiting area, explained the study to the patients, obtained their informed consent, and assisted them when they had difficulties in completing the questionnaires. Pilot testing involving five patients was conducted to assess the feasibility of the survey instrument, and no subsequent modifications were made. All participating patients received a compensation of IDR 100,000 (≈ USD 6.30) after completing the questionnaire, which they were not informed about beforehand.

The oncology nurses’ questionnaire was prepared to gather clinical data on patients based on the hospital’s computerized medical records: stage and type of breast cancer, disease duration, metastasis status, comorbidities, and previous and current treatment(s) (e.g., chemotherapy, immunotherapy, and surgery).

## EQ-5D-5L

The EQ-5D-5L is a generic preference-accompanied measure of HRQoL consisting of two parts \[32\]. The first part is a descriptive system comprising five single-item dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. Each item has five levels of responses: no problems (1), slight problems (2), moderate problems (3), severe problems (4), and extreme problems/unable to (5). An EQ-5D-5L health state profile may be described by a five-digit string. For example, ‘11111’ indicates no problems in all dimensions, and ‘22133’ indicates slight problems in the mobility and self-care dimensions, no problems in the usual activities dimension, and moderate problems in the pain/discomfort and anxiety/dimension dimensions. The descriptive system was scored by assigning an index value to each health state profile using the Indonesian EQ-5D-5L value set, with higher values indicating better HRQoL \[33\]. The second part of the EQ-5D-5L is the EQ visual analog scale (EQ VAS). In this part, patients were asked to indicate their health using a vertical scale which has a value of between 0 (‘the worst health you can imagine’) and 100 (‘the best health you can imagine’). The EQ-5D-5L descriptive system as well as EQ VAS have been widely validated in cancer populations \[34–37\].

## EQ Health and Wellbeing (EQ-HWB)

The EQ-HWB is a newly developed measure that goes beyond conventional measures of HRQoL to include carer- and social care-related quality of life \[38\]. Development of the measure drew on different theories of well-being including objective lists, preference satisfaction, and capabilities under the extra-welfarist paradigm of measuring social welfare \[39\]. There are two versions of the measure: a long 25-item form, and a short 9-item form (EQ-HWB-S), which is a subset of the long version \[38\]. The long form serves a profile measure, while the short form functions a self-classifier for economic evaluations. The items are answered using three different five-level response scales: difficulty, frequency, and severity. The EQ-HWB has earlier been used in cancer populations \[40–43\], and was shown to perform well in item response theory and classical psychometric testing \[38, 40\]. In this study, the patients completed the 25-item EQ-HWB, from which the responses for the EQ-HWB-S were derived. For the EQ-HWB, a level summary score (LSS) was calculated by summing the responses from the 25 items, with higher scores indicating worse health and well-being. The theoretical LSS range of 25–125 was transformed to a scale of 0-100 for analysis. For the EQ-HWB-S, the index value was derived using the UK pilot value set, as no Indonesian value set was available \[44\]. Higher index values indicated better health and well-being.

## COST: A FACIT Measure of Financial Toxicity (FACIT-COST)

The FACIT-COST is the most widely validated and used cancer-specific measure of SFT \[13, 18, 45\]. The latest version (v2) has 12 items with 0–4 response scale, from ‘not at all’ (= 0) to ‘very much’ (= 4). The items relate to financial adequacy, psychosocial reaction, anticipating future financial problems, and financial hardship on family, among others. The FACIT-COST total score was computed by summing items 1 through 11, with items 2, 3, 4, 5, 8, 9, and 10 scored in reverse. The theoretical score ranges between 0 and 44, with lower scores indicating worse SFT. Following a receiver operating characteristic analysis, a cut-off score of ≤ 17.5 was proposed to indicate high SFT \[46\].

## Questions on objective financial toxicity (OFT)

To assess OFT, the patients were asked if they experienced one or more of the following financial coping strategies in treating breast cancer: (i) withdrawing savings or pension fund, (ii) selling assets such as vehicle, land, and gold/jewelry, (iii) incurring debt from a relative or financial institution, and (iv) closing business. These items were selected based on previous studies \[47, 48\], while also giving the option to respondents to specify other financial coping strategies using an open-ended ‘other’ response option.

### Statistical analysis

All variables were descriptively summarized using frequencies and percentages, means and standard deviations, depending on the type of data. Four subgroups were defined by the combination of SFT and OFT experiences: i) low SFT and no OFT, ii) low SFT and at least one OFT, iii) high SFT but no OFT, and iv) high SFT and at least one OFT \[12\]. The twelfth item of FACIT-COST (‘financial hardship to my family and me’), which was not included in the calculation of the FACIT-COST total score, was also used to define three subgroups derived from the five-level response scale of the instrument: i) ‘not at all’, ii) ‘a little bit’ or ‘somewhat’, and iii) ‘quite a bit’ or ’very much’. The mean EQ-5D-L, EQ-HWB-S index values, EQ-HWB LSS, and EQ VAS scores were compared among patient subgroups using the Mann-Whitney or Kruskal-Wallis test.

Spearman’s rho was used to examine the correlations between FACIT-COST total score and selected individual items of EQ-5D-5L and EQ-HWB where associations were hypothesized: EQ-5D-5L pain/discomfort, anxiety/depression, EQ-HWB-S exhaustion, anxiety, sadness/depression, no control over daily life, pain (severity), and EQ-HWB frustration, coping, and discomfort (severity) \[49–52\]. The EQ-5D-5L pain/discomfort and EQ-HWB discomfort items were predicted because the literature suggests that they may also capture psychological forms of discomfort despite primarily targeting physical discomfort \[53\]. The EQ-HWB pain (severity) item was mainly selected as a control because it specifically asks about pain, while the EQ-5D-5L combines pain and discomfort in a single item. Additionally, Pearson’s coefficient was used for the correlations between FACIT-COST total score and: EQ-5D-5L and EQ-HWB-S index values, EQ-HWB LSS, and EQ VAS. The strength of correlations was interpreted as: strong (≥ 0.50), moderate (0.30–0.49), weak (0.10–0.29), and very weak (\< 0.10) \[54\].

To further evaluate the associations between FT (both SFT and OFT), HRQoL, and well-being, regression models were used. For this purpose, the total score of FACIT-COST was recoded to align higher scores with increased SFT. OFT was operationalized as an ordinal variable indicating the number of financial coping strategies employed by the patients. To adjust for covariates in the regressions, a subset of key socio-demographic and clinical characteristics was selected by applying a forward stepwise regression procedure. Variables which exhibited a *p* ≥ 0.05 in bivariate analyses with the outcome variables were excluded: marital status, education, employment status, residential setting, insurance coverage, breast cancer type, cancer stage at diagnosis, and treatments other than chemotherapy. The retained socio-demographic covariates were age, household income, and number of children, while the clinical covariates were cancer diagnosis of one year or less, metastasis status, undergoing chemotherapy, number of comorbidities, and number of symptoms reported in the past week. Ordinal logistic models were also developed to examine the associations between FT and EQ-5D-5L and EQ-HWB items, adjusted for the selected socio-demographic and clinical covariates, with odds ratios and their respective 95% confidence intervals calculated. The ordinal regressions were only performed for items with sufficient variability in responses, thereby excluding EQ-HWB-S no control over daily life and EQ-HWB coping items.

Multivariable ordinary least squares (OLS) models were used for FT predicting EQ-5D-5L and EQ-HWB-S index values, EQ-HWB LSS, and EQ VAS. In the OLS, three models were gradually developed with FT (SFT and OFT) as predictors: (i) no covariates, (ii) adjusted for socio-demographic covariates, and (iii) adjusted for both socio-demographic and clinical covariates. Robust standard errors were used to address heteroskedasticity, which was verified using the Breusch-Pagan test. No instances of multicollinearity among the independent variables were detected in any of the models (variance inflation factor \> 5). The R-squared values were compared to assess which outcome variable was better predicted by the FT variables. All statistical analyses were performed using Stata 18 (StataCorp LLC), with statistical significance set at *p* \< 0.05.

## Results

### Patient characteristics

Overall, 300 female patients with breast cancer completed the survey. The mean age was 51.26 ± 10.29 years (range 23–84). Most patients were married (77.7%), homemakers (73.7%), resided in a rural area (59.7%), had children aged \< 17 living in the same household (52.0%), and completed secondary education (52.3%) (Table <a href="#Tab1" data-ref-type="table">1</a>). The net monthly household income of the patients was \< 5 million IDR (≈ USD 324) for 90% of the patients. All except one patient (99.7%) had insurance coverage for their treatment. The two most common breast cancer types were invasive lobular carcinoma (46.7%) and invasive ductal carcinoma (39.0%). Most patients were diagnosed at stage 2 (62.0%) and 8.0% had metastasis. The most common types of treatment at the time of the survey were immunotherapy (84.3%) and chemotherapy (11.33%). Overall, 81% of the patients underwent surgeries, such as mastectomy or lumpectomy.

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of the patients

</div>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">Characteristic</th>
<th style="text-align: left;"><em>N</em> or Mean</th>
<th style="text-align: left;">% or SD</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;"><strong><em>Socio-demographic characteristics</em></strong></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Age</td>
<td style="text-align: left;">51.26</td>
<td style="text-align: left;">10.29</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> &lt; 50 years</td>
<td style="text-align: left;">132</td>
<td style="text-align: left;">44.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 50 years and above</td>
<td style="text-align: left;">168</td>
<td style="text-align: left;">56.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Marital status</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Married</td>
<td style="text-align: left;">233</td>
<td style="text-align: left;">77.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Single/divorced/widowed</td>
<td style="text-align: left;">67</td>
<td style="text-align: left;">22.3%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Education</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Primary or less</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">30.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Secondary</td>
<td style="text-align: left;">157</td>
<td style="text-align: left;">52.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Tertiary</td>
<td style="text-align: left;">51</td>
<td style="text-align: left;">17.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Employment status</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Employed</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">18.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Homemaker</td>
<td style="text-align: left;">221</td>
<td style="text-align: left;">73.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Unemployed (seeking for work)</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">1.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Retired</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">6.7%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Residential setting</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Rural</td>
<td style="text-align: left;">179</td>
<td style="text-align: left;">59.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Urban</td>
<td style="text-align: left;">121</td>
<td style="text-align: left;">40.3%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Number of children (aged &lt; 17) living in the same household</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 0</td>
<td style="text-align: left;">144</td>
<td style="text-align: left;">48.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">26.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2+</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">20.7%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Net monthly household income<sup>b</sup></td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 5 million IDR and less</td>
<td style="text-align: left;">270</td>
<td style="text-align: left;">90.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> &gt; 5 million IDR</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">10.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Health insurance coverage</td>
<td style="text-align: left;">299</td>
<td style="text-align: left;">99.7%</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><strong><em>Clinical characteristics</em></strong></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Breast cancer type</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Invasive lobular carcinoma</td>
<td style="text-align: left;">140</td>
<td style="text-align: left;">46.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Invasive ductal carcinoma<sup>d</sup></td>
<td style="text-align: left;">117</td>
<td style="text-align: left;">39.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Ductal carcinoma in situ</td>
<td style="text-align: left;">37</td>
<td style="text-align: left;">12.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Lobular carcinoma in situ</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">1.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Inflammatory breast cancer</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Mucinous carcinoma</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.3%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Cancer stage at diagnosis<sup>c</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">26</td>
<td style="text-align: left;">8.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2</td>
<td style="text-align: left;">186</td>
<td style="text-align: left;">62.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 3</td>
<td style="text-align: left;">81</td>
<td style="text-align: left;">27.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 4</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Unknown</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.7%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Disease duration (in years)</td>
<td style="text-align: left;">2.45</td>
<td style="text-align: left;">3.18</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Metastasis</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">8.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Current treatment<sup>a</sup></td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Immunotherapy</td>
<td style="text-align: left;">253</td>
<td style="text-align: left;">84.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Chemotherapy</td>
<td style="text-align: left;">37</td>
<td style="text-align: left;">12.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Radiation therapy</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">3.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Stem cell or bone marrow</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Unknown</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Palliative care</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">7.7%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Surgery history<sup>f</sup></td>
<td style="text-align: left;">243</td>
<td style="text-align: left;">81.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Number of comorbidities<sup>g</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 0</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">26.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">123</td>
<td style="text-align: left;">41.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2+</td>
<td style="text-align: left;">99</td>
<td style="text-align: left;">33.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Number of symptoms in the past week<sup>h</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 0</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">5.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1–3</td>
<td style="text-align: left;">71</td>
<td style="text-align: left;">23.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 4–6</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">22.7%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 7–9</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">20.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 10+</td>
<td style="text-align: left;">84</td>
<td style="text-align: left;">28.0%</td>
</tr>
</tbody>
</table>

<sup>a</sup>May belong in more than one category

<sup>b</sup>IDR= Indonesian Rupiah, 324.34 USD = 5 million IDR (based on the closing 2023 middle exchange rate from Bank Indonesia)

<sup>c</sup>Based on the American Joint Committee on Cancer Staging (0: non-invasive, pre-cancerous, 1: early stage, spread to other tissue in small area, 2: localized, tumor between 20–50 mm and lymph nodes involved or tumor larger than 50 mm with no lymph nodes involved), 3: regional spread, tumor larger than 50 mm with lymph nodes involved in larger region, may have spread to skin or chest wall, 4: metastatic, distant spread beyond the breast and nearby lymph nodes)

<sup>d</sup>Included subtypes: triple negative breast cancer, luminal A, luminal B HER-2 negative, luminal B HER-2 positive, and HER-2 positive

<sup>e</sup>Most common sites were bone (*n* = 7), lung (*n* = 5), and liver (*n* = 3)

<sup>f</sup>Surgeries included single/double mastectomy and lumpectomy

<sup>g</sup>Most common comorbidities: chronic gastritis (*n* = 172), hypertension (*n* = 72), and obesity (*n* = 39)

<sup>h</sup>Most reported symptoms: fatigue (*n* = 175), dizziness (*n* = 143), muscle pain (*n* = 133), sleep problem (123), anxiety (*n* = 122), and hair loss (*n* = 120)

</div>

### Financial toxicity, health, and well-being

The majority of patients reported overall good health status with mean EQ-5D-5L index value of 0.85 ± 0.21, mean EQ VAS of 81.18 ± 15.63, and mean EQ-HWB-S index value of 0.84 ± 0.17 (Table <a href="#Tab2" data-ref-type="table">2</a>). The mean FACIT-COST total score was 24.24 ± 8.65. High SFT as measured by the FACIT-COST (≤ 17.5), was experienced by 21% patients (Table <a href="#Tab3" data-ref-type="table">3</a>). Meanwhile, OFT was experienced by 51% patients who reported at least one financial strategy used to cope with their breast cancer treatment. The two most common strategies used by the patients were borrowing from relatives or financial institution (30.0%) and withdrawing from savings/pension (25.7%).

<div id="Tab2" class="table-wrap">

<div class="caption">

Descriptive statistics of the outcome measures

</div>

| Measure | Theoretical range | Observed range | Mean | Standard deviation | Q1 | Median | Q3 |
|----|----|----|----|----|----|----|----|
| FACIT-COST total score<sup>a, e</sup> | 0–44 | 2–42 | 24.24 | 8.65 | 19 | 25 | 30 |
| EQ-5D-5L index value<sup>a, b</sup> | -0.865 to 1 | -0.31 to 1 | 0.85 | 0.21 | 0.80 | 0.91 | 1 |
| EQ VAS<sup>a</sup> | 0–100 | 10–100 | 81.18 | 15.63 | 75 | 80 | 90 |
| EQ-HWB-S index value<sup>a, d</sup> | -0.384 to 1 | -0.245 to 1 | 0.84 | 0.17 | 0.79 | 0.89 | 0.95 |
| EQ-HWB LSS<sup>c</sup> | 0–100 | 0–65 | 16.48 | 11.76 | 8 | 13 | 23 |

Abbreviations. EQ-HWB = EQ Health and Wellbeing, EQ-HWB-S = EQ-HWB short form, EQ VAS = EQ Visual analogue scale, FACIT-COST = COST - A FACIT Measure of Financial Toxicity, LSS = level summary scores

<sup>a</sup>Higher scores indicate better health-related quality of life, better health and well-being, or lower financial toxicity

<sup>b</sup>Computed using the Indonesian value set (Purba et al., 2017)

<sup>c</sup>LSS recoded into a 0-100 scale, with higher scores indicating worse health and well-being

<sup>d</sup>Computed using the pilot UK value set (Mukuria et al., 2023)

<sup>e</sup>Following the scoring guidelines, the 12th item of FACIT-COST was not included in the overall score computation

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

EQ-5D-5L, EQ VAS, and EQ-HWB scores across financial toxicity categories

</div>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">Financial toxicity</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">Mean EQ-5D-5L index value</th>
<th style="text-align: left;"><em>p</em>-value</th>
<th style="text-align: left;">Mean EQ VAS</th>
<th style="text-align: left;"><em>p</em>-value</th>
<th style="text-align: left;">Mean EQ-HWB-S<br />
index value</th>
<th colspan="3" style="text-align: left;"><em>p</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;">Subjective financial toxicity (SFT)<sup>b, c</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High SFT</td>
<td style="text-align: left;">63</td>
<td style="text-align: left;">21.0%</td>
<td style="text-align: left;">0.75 ± 0.23</td>
<td rowspan="2" style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">72.94 ± 17.75</td>
<td rowspan="2" style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.73 ± 0.24</td>
<td colspan="3" rowspan="2" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Low SFT</td>
<td style="text-align: left;">237</td>
<td style="text-align: left;">79.0%</td>
<td style="text-align: left;">0.87 ± 0.19</td>
<td style="text-align: left;">83.38 ± 14.28</td>
<td style="text-align: left;">0.87 ± 0.13</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Objective financial toxicity (OFT)<sup>d</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">At least one OFT</td>
<td style="text-align: left;">153</td>
<td style="text-align: left;">51.0%</td>
<td style="text-align: left;">0.82 ± 0.23</td>
<td rowspan="2" style="text-align: left;">0.027</td>
<td style="text-align: left;">79.74 ± 17.03</td>
<td rowspan="2" style="text-align: left;">0.103</td>
<td style="text-align: left;">0.82 ± 0.19</td>
<td colspan="3" rowspan="2" style="text-align: left;">0.030</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">No OFT</td>
<td style="text-align: left;">147</td>
<td style="text-align: left;">49.0%</td>
<td style="text-align: left;">0.87 ± 0.17</td>
<td style="text-align: left;">82.69 ± 13.93</td>
<td style="text-align: left;">0.86 ± 0.14</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Borrowing from relatives or financial institution</em></td>
<td colspan="9" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-Yes</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">30.0%</td>
<td style="text-align: left;">0.81 ± 0.21</td>
<td rowspan="2" style="text-align: left;">0.061</td>
<td style="text-align: left;">78.39 ± 16.62</td>
<td rowspan="2" style="text-align: left;">0.042</td>
<td style="text-align: left;">0.79 ± 0.21</td>
<td colspan="3" rowspan="2" style="text-align: left;">0.002</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-No</td>
<td style="text-align: left;">210</td>
<td style="text-align: left;">70.0%</td>
<td style="text-align: left;">0.86 ± 0.20</td>
<td style="text-align: left;">82.38 ± 15.07</td>
<td style="text-align: left;">0.86 ± 0.15</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Withdrawing savings or pension</em></td>
<td colspan="9" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-Yes</td>
<td style="text-align: left;">77</td>
<td style="text-align: left;">25.7%</td>
<td style="text-align: left;">0.82 ± 0.26</td>
<td rowspan="2" style="text-align: left;">0.185</td>
<td style="text-align: left;">79.94 ± 15.95</td>
<td rowspan="2" style="text-align: left;">0.417</td>
<td style="text-align: left;">0.82 ± 0.20</td>
<td colspan="3" rowspan="2" style="text-align: left;">0.320</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-No</td>
<td style="text-align: left;">223</td>
<td style="text-align: left;">74.3%</td>
<td style="text-align: left;">0.85 ± 0.19</td>
<td style="text-align: left;">81.61 ± 15.53</td>
<td style="text-align: left;">0.85 ± 0.16</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Selling assets (e.g., vehicle, land)</em></td>
<td colspan="9" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-Yes</td>
<td style="text-align: left;">33</td>
<td style="text-align: left;">11.0%</td>
<td style="text-align: left;">0.76 ± 0.25</td>
<td rowspan="2" style="text-align: left;">0.010</td>
<td style="text-align: left;">75.76 ± 18.38</td>
<td rowspan="2" style="text-align: left;">0.034</td>
<td style="text-align: left;">0.75 ± 0.26</td>
<td colspan="3" rowspan="2" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-No</td>
<td style="text-align: left;">267</td>
<td style="text-align: left;">89.0%</td>
<td style="text-align: left;">0.86 ± 0.20</td>
<td style="text-align: left;">81.85 ± 15.16</td>
<td style="text-align: left;">0.85 ± 0.15</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Closing business</em></td>
<td colspan="9" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-Yes</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">3.3%</td>
<td style="text-align: left;">0.78 ± 0.25</td>
<td rowspan="2" style="text-align: left;">0.270</td>
<td style="text-align: left;">78.50 ± 12.92</td>
<td rowspan="2" style="text-align: left;">0.582</td>
<td style="text-align: left;">0.76 ± 0.13</td>
<td colspan="3" rowspan="2" style="text-align: left;">0.142</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">-No</td>
<td style="text-align: left;">290</td>
<td style="text-align: left;">96.7%</td>
<td style="text-align: left;">0.85 ± 0.20</td>
<td style="text-align: left;">81.28 ± 15.73</td>
<td style="text-align: left;">0.84 ± 0.17</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">SFT and OFT</td>
<td colspan="2" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High SFT and at least one OFT</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">14.3%</td>
<td style="text-align: left;">0.73 ± 0.25</td>
<td rowspan="4" style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">69.30 ± 17.48</td>
<td rowspan="4" style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.71 ± 0.25</td>
<td colspan="3" rowspan="4" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High SFT and no OFT</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">6.7%</td>
<td style="text-align: left;">0.81 ± 0.17</td>
<td style="text-align: left;">80.75 ± 16.08</td>
<td style="text-align: left;">0.77 ± 0.22</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Low SFT and at least one OFT</td>
<td style="text-align: left;">110</td>
<td style="text-align: left;">36.7%</td>
<td style="text-align: left;">0.86 ± 0.21</td>
<td style="text-align: left;">83.82 ± 15.07</td>
<td style="text-align: left;">0.86 ± 0.14</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Low SFT and no OFT</td>
<td style="text-align: left;">127</td>
<td style="text-align: left;">42.3%</td>
<td style="text-align: left;">0.88 ± 0.17</td>
<td style="text-align: left;">82.99 ± 13.60</td>
<td style="text-align: left;">0.88 ± 0.13</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">FACIT-COST item 12<sup>e</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Quite a bit/very much</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">28.3%</td>
<td style="text-align: left;">0.79 ± 0.21</td>
<td rowspan="3" style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">74.82 ± 17.12</td>
<td rowspan="3" style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.76 ± 0.22</td>
<td colspan="3" rowspan="3" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">A little bit/somewhat</td>
<td style="text-align: left;">114</td>
<td style="text-align: left;">38.0%</td>
<td style="text-align: left;">0.84 ± 0.24</td>
<td style="text-align: left;">81.93 ± 15.66</td>
<td style="text-align: left;">0.84 ± 0.16</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Not at all</td>
<td style="text-align: left;">101</td>
<td style="text-align: left;">33.7%</td>
<td style="text-align: left;">0.90 ± 0.12</td>
<td style="text-align: left;">85.69 ± 12.31</td>
<td style="text-align: left;">0.91 ± 0.09</td>
</tr>
</tbody>
</table>

Abbreviations. EQ-HWB = EQ Health and Wellbeing, EQ-HWB-S = EQ-HWB short form, FACIT-COST = COST - A FACIT Measure of Financial Toxicity, LSS = level summary scores

<sup>a</sup>LSS recoded to a 0-100 scale

<sup>b</sup>High subjective financial toxicity: FACIT-COST score of ≤ 17.5 (Ng et al., 2021)

<sup>c</sup>Following the scoring guidelines, item 12 of the FACIT-COST was not included in the overall score computation

<sup>d</sup>Each patient may have incurred more than one financial coping strategy

<sup>e</sup>’Financial hardship to my family and me’ item (responses recoded from five to three levels)

</div>

Among the four coping strategies, patients who sold their assets had the lowest mean EQ-5D-5L and EQ-HWB-S index values of 0.76 ± 0.25 and 0.75 ± 0.26, respectively. Overall, 42.3% experienced low SFT and no OFT, 36.7% experienced low SFT but at least one OFT, 6.7% experienced high SFT and no OFT, and 14.3% experienced both high SFT and at least one OFT. The mean EQ-5D-5L index values for these four subgroups were 0.88 ± 0.17, 0.86 ± 0.21, 0.81 ± 0.17, 0.73 ± 0.25, while the mean EQ-HWB-S index values were 0.88 ± 0.13, 0.86 ± 0.14, 0.77 ± 0.22, and 0.71 ± 0.25 respectively (*p* \< 0.001 for both instruments) (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). The EQ-5D-L and EQ-HWB-S index values had statistically significant differences for the FACIT-COST item ‘financial hardship to my family and me’: not at all (0.90 ± 0.12, 0.91 ± 0.09), a little bit/somewhat (0.84 ± 0.24, 0.84 ± 0.16), and quite a bit/very much (0.79 ± 0.21, 0.76 ± 0.22) (*p* \< 0.001). Comparisons of EQ-5D-5L and EQ-HWB index values or scores among subgroups as defined by socio-demographic and clinical characteristics are presented in Supplementary Material <a href="#MOESM1" data-ref-type="media">1</a>.

<figure id="Fig1">
<p><img src="11136_2025_3925_Fig1_HTML.jpg" id="d33e1767" /></p>
<figcaption>Mean EQ-5D-L and EQ-HWB-S index values across financial toxicity subgroups. <em>Abbreviations.</em> EQ-HWB-S: EQ Health and Wellbeing short form, OFT: objective financial toxicity, SFT: subjective financial toxicity</figcaption>
</figure>

### Correlations between FACIT-COST, EQ-5D-5L, and EQ-HWB

The FACIT-COST total score demonstrated correlations that were borderline moderate with EQ-HWB coping (-0.34), EQ-HWB-S no control over daily life (-0.33), exhaustion (-0.31), and weakly correlated with the following items: EQ-HWB frustration (-0.29), EQ-HWB-S sadness/depression (-0.28), EQ-5D-5L pain/discomfort (-0.28), and anxiety/depression (-0.27), among others (Table <a href="#Tab4" data-ref-type="table">4</a>). At the instrument level, FACIT-COST total score exhibited moderate correlations with EQ-HWB LSS (-0.48), EQ-HWB-S index values (0.44), EQ VAS scores (0.44), EQ-5D-5L LSS (-0.32), and EQ-5D-5L index values (0.30).

<div id="Tab4" class="table-wrap">

<div class="caption">

Correlations between the EQ-5D-5L, EQ-HWB, and FACIT-COST

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">FACIT-COST total score<sup>*</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><strong><em>Pearson’s correlations</em></strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L index value</td>
<td style="text-align: left;">0.30</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;">0.35</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-S index value</td>
<td style="text-align: left;">0.44</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB LSS</td>
<td style="text-align: left;">-0.48</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong><em>Spearman’s correlations</em></strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L pain/discomfort</td>
<td style="text-align: left;">-0.28</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L anxiety/depression</td>
<td style="text-align: left;">-0.27</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-S exhaustion</td>
<td style="text-align: left;">-0.31</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-S anxiety</td>
<td style="text-align: left;">-0.22</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-S sadness/depression</td>
<td style="text-align: left;">-0.28</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-S pain (severity)</td>
<td style="text-align: left;">-0.23</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-S no control over daily life</td>
<td style="text-align: left;">-0.33</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB frustration</td>
<td style="text-align: left;">-0.29</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB coping</td>
<td style="text-align: left;">-0.34</td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB discomfort (severity)</td>
<td style="text-align: left;">-0.19</td>
</tr>
</tbody>
</table>

Abbreviations. EQ-HWB = EQ Health and Wellbeing, EQ-HWB-S = EQ-HWB short form, FACIT-COST = COST - A FACIT Measure of Financial Toxicity, LSS = level summary scores

<sup>\*</sup>Following the scoring guidelines, the 12th item of FACIT-COST was not included in the overall score computation

All correlation coefficients were *p* \< 0.001

</div>

### Associations between financial toxicity and EQ-5D-5L and EQ-HWB items

After adjusting for socio-demographic and clinical covariates, reporting higher SFT was associated with more problems in the EQ-5D-5L pain/discomfort (OR = 1.07), anxiety/depression (OR = 1.06), EQ-HWB-S exhaustion (OR = 1.06), anxiety (OR = 1.04), sadness/depression (OR = 1.06), pain (OR = 1.06), EQ-HWB frustration (OR = 1.10), and discomfort (OR = 1.04) items (Table <a href="#Tab5" data-ref-type="table">5</a>). Meanwhile, higher OFT was only significantly associated with more problems in the EQ-HWB-S exhaustion item (OR = 1.40).

<div id="Tab5" class="table-wrap">

<div class="caption">

Ordinal logistic regression results

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Variables</th>
<th colspan="2" style="text-align: left;">EQ-5D-5L pain/discomfort</th>
<th colspan="2" style="text-align: left;">EQ-5D-5L anxiety/depression</th>
<th colspan="2" style="text-align: left;">EQ-HWB-S exhaustion</th>
<th colspan="2" style="text-align: left;">EQ-HWB-S<br />
anxiety</th>
<th colspan="2" style="text-align: left;">EQ-HWB-S sadness/depression</th>
<th colspan="2" style="text-align: left;">EQ-HWB-S<br />
pain (severity)</th>
<th colspan="2" style="text-align: left;">EQ-HWB<br />
frustration</th>
<th colspan="2" style="text-align: left;">EQ-HWB<br />
discomfort (severity)</th>
</tr>
<tr>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">OR</th>
<th style="text-align: left;">95% CI</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Subjective financial toxicity<sup>a</sup></td>
<td style="text-align: left;">1.07<sup>***</sup></td>
<td style="text-align: left;">(1.04, 1.1)</td>
<td style="text-align: left;">1.06<sup>**</sup></td>
<td style="text-align: left;">(1.02, 1.10)</td>
<td style="text-align: left;">1.06<sup>***</sup></td>
<td style="text-align: left;">(1.03, 1.10)</td>
<td style="text-align: left;">1.04<sup>**</sup></td>
<td style="text-align: left;">(1.01, 1.08)</td>
<td style="text-align: left;">1.06<sup>**</sup></td>
<td style="text-align: left;">(1.02, 1.09)</td>
<td style="text-align: left;">1.06<sup>***</sup></td>
<td style="text-align: left;">(1.03, 1.10)</td>
<td style="text-align: left;">1.10<sup>**</sup></td>
<td style="text-align: left;">(1.05, 1.15)</td>
<td style="text-align: left;">1.04<sup>*</sup></td>
<td style="text-align: left;">(1.01, 1.07)</td>
</tr>
<tr>
<td style="text-align: left;">Objective financial toxicity</td>
<td style="text-align: left;">1.16</td>
<td style="text-align: left;">(0.87, 1.56)</td>
<td style="text-align: left;">1.23</td>
<td style="text-align: left;">(0.88, 1.71)</td>
<td style="text-align: left;">1.40<sup>*</sup></td>
<td style="text-align: left;">(1.06, 1.87)</td>
<td style="text-align: left;">1.12</td>
<td style="text-align: left;">(0.84, 1.51)</td>
<td style="text-align: left;">1.18</td>
<td style="text-align: left;">(0.87, 1.59)</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">(0.71, 1.24)</td>
<td style="text-align: left;">0.90</td>
<td style="text-align: left;">(0.61, 1.34)</td>
<td style="text-align: left;">1.03</td>
<td style="text-align: left;">(0.77, 1.36)</td>
</tr>
<tr>
<td style="text-align: left;">Pseudo R-squared</td>
<td colspan="2" style="text-align: left;">12.63%</td>
<td colspan="2" style="text-align: left;">14.40%</td>
<td colspan="2" style="text-align: left;">15.14%</td>
<td colspan="2" style="text-align: left;">9.68%</td>
<td colspan="2" style="text-align: left;">6.68%</td>
<td colspan="2" style="text-align: left;">9.20%</td>
<td colspan="2" style="text-align: left;">17.34%</td>
<td colspan="2" style="text-align: left;">10.34%</td>
</tr>
</tbody>
</table>

<sup>\*\*\*</sup>*p* \< 0.001, <sup>\*\*</sup>*p* \< 0.01, <sup>\*</sup>*p* \< 0.05

Abbreviations. CI = confidence interval, EQ-HWB = EQ Health and Wellbeing, EQ-HWB-S = EQ-HWB short form, OR = odds ratio

All regression models were controlled for age, income, number of children, diagnosis duration, metastasis status, current chemotherapy, number of comorbidities and symptoms in the past week

<sup>a</sup>Measured using COST - A FACIT Measure of Financial Toxicity

</div>

### Associations between financial toxicity and EQ-5D-5L and EQ-HWB level sum scores and index values

In the unadjusted OLS models, higher SFT was significantly associated with lower EQ-5D-5L index value (‘Model 1’), EQ VAS (‘Model 4’), EQ-HWB-S index value (‘Model 7’), and higher EQ-HWB LSS (‘Model 10’) (*p* \< 0.001 each) (Table <a href="#Tab6" data-ref-type="table">6</a>). After controlling for the socio-demographic and clinical covariates, the significant associations between SFT and the outcomes persisted (*p* \< 0.001 each): EQ-5D-5L index value (beta=-0.01, ‘Model 3’), EQ VAS (beta=-0.56, ‘Model 6’), EQ-HWB-S index value (beta=-0.01, ‘Model 9’), and EQ-HWB LSS (beta = 0.54, ‘Model 12’). After covariate adjustment, FT explained more variance in EQ-HWB-S index value (R<sup>2</sup> = 46.39%) and EQ-HWB LSS (R<sup>2</sup> = 46.15%) than in EQ-5D-5L index value (R<sup>2</sup> = 31.23%) and EQ VAS (R<sup>2</sup> = 25.60%).

<div id="Tab6" class="table-wrap">

<div class="caption">

Multivariable linear regression results

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="3" style="text-align: left;">Variables</th>
<th colspan="6" style="text-align: left;">Outcome: EQ-5D-5L index value</th>
<th colspan="6" style="text-align: left;">Outcome: EQ VAS</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Model 1</th>
<th colspan="2" style="text-align: left;">Model 2</th>
<th colspan="2" style="text-align: left;">Model 3</th>
<th colspan="2" style="text-align: left;">Model 4</th>
<th colspan="2" style="text-align: left;">Model 5</th>
<th colspan="2" style="text-align: left;">Model 6</th>
</tr>
<tr>
<th style="text-align: left;">B</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">B</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">B</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">B</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">B</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">B</th>
<th style="text-align: left;">SE</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><em>Intercept</em></td>
<td style="text-align: left;"><em>1.00</em></td>
<td style="text-align: left;"><em>0.00</em></td>
<td style="text-align: left;">0.98</td>
<td style="text-align: left;">0.05</td>
<td style="text-align: left;">1.13</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">95.15</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">98.08</td>
<td style="text-align: left;">2.65</td>
<td style="text-align: left;">99.94</td>
<td style="text-align: left;">3.75</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Subjective financial toxicity<sup>a</sup></td>
<td style="text-align: left;">-0.01<sup>***</sup></td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-0.01<sup>***</sup></td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">-0.01<sup>***</sup></td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">-0.63<sup>***</sup></td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">-0.66<sup>***</sup></td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">-0.56<sup>***</sup></td>
<td style="text-align: left;">0.11</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Objective financial toxicity</td>
<td style="text-align: left;">-0.02</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-0.03</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-0.02</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-0.49</td>
<td style="text-align: left;">0.97</td>
<td style="text-align: left;">-0.87</td>
<td style="text-align: left;">0.96</td>
<td style="text-align: left;">-0.22</td>
<td style="text-align: left;">0.94</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Aged 50 years and above</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.06<sup>**</sup></td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-0.03</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-5.26<sup>**</sup></td>
<td style="text-align: left;">1.67</td>
<td style="text-align: left;">-3.53<sup>*</sup></td>
<td style="text-align: left;">1.69</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Income &gt; 5 million IDR<sup>b</sup></td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.08</td>
<td style="text-align: left;">0.05</td>
<td style="text-align: left;">-0.01<sup>*</sup></td>
<td style="text-align: left;">0.05</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">1.64</td>
<td style="text-align: left;">1.96</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">1.88</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Number of children</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.02<sup>*</sup></td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.03<sup>**</sup></td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">1.11</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: left;">0.79</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Diagnosed 1 year or less</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.04</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.29</td>
<td style="text-align: left;">1.68</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Metastasis</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.11<sup>*</sup></td>
<td style="text-align: left;">0.05</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">1.74</td>
<td style="text-align: left;">3.08</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Undergoing chemotherapy</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.10<sup>**</sup></td>
<td style="text-align: left;">0.04</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-5.12</td>
<td style="text-align: left;">2.94</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Comorbidities <em>(ref: none)</em></td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.01</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-1.77</td>
<td style="text-align: left;">1.82</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2+</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.03</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-3.89</td>
<td style="text-align: left;">2.31</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Symptoms in the past week <em>(ref: none)</em></td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1–3</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.02</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">2.49</td>
<td style="text-align: left;">3.22</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 4–6</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.07<sup>*</sup></td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-2.36</td>
<td style="text-align: left;">3.36</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 7–9</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.09<sup>**</sup></td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-2.32</td>
<td style="text-align: left;">3.53</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 10+</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.18<sup>***</sup></td>
<td style="text-align: left;">0.04</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-8.77<sup>*</sup></td>
<td style="text-align: left;">3.55</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Model fit</td>
<td colspan="2" style="text-align: left;"><p>F(2,297) = 16.01</p>
<p>(<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 9.12%</p></td>
<td colspan="2" style="text-align: left;"><p>F(5,294) = 8.11 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 14.88%</p></td>
<td colspan="2" style="text-align: left;"><p>F(14,285) = 7.50 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 31.23%</p></td>
<td colspan="2" style="text-align: left;"><p>F(2,297) = 21.37 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 12.63%</p></td>
<td colspan="2" style="text-align: left;"><p>F(5,294) = 11.50 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 16.36%</p></td>
<td colspan="2" style="text-align: left;"><p>F(14,285) = 6.27 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 25.60%</p></td>
</tr>
<tr>
<td colspan="2" rowspan="3" style="text-align: left;"><strong>Variables</strong></td>
<td colspan="6" style="text-align: left;"><strong>Outcome: EQ-HWB-S index value</strong></td>
<td colspan="6" style="text-align: left;"><strong>Outcome: EQ-HWB LSS</strong> <sup><strong>c</strong></sup></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Model 7</strong></td>
<td colspan="2" style="text-align: left;"><strong>Model 8</strong></td>
<td colspan="2" style="text-align: left;"><strong>Model 9</strong></td>
<td colspan="2" style="text-align: left;"><strong>Model 10</strong></td>
<td colspan="2" style="text-align: left;"><strong>Model 11</strong></td>
<td colspan="2" style="text-align: left;"><strong>Model 12</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong><em>B</em></strong></td>
<td style="text-align: left;"><strong><em>SE</em></strong></td>
<td style="text-align: left;"><strong><em>B</em></strong></td>
<td style="text-align: left;"><strong><em>SE</em></strong></td>
<td style="text-align: left;"><strong><em>B</em></strong></td>
<td style="text-align: left;"><strong><em>SE</em></strong></td>
<td style="text-align: left;"><strong><em>B</em></strong></td>
<td style="text-align: left;"><strong><em>SE</em></strong></td>
<td style="text-align: left;"><strong><em>B</em></strong></td>
<td style="text-align: left;"><strong><em>SE</em></strong></td>
<td style="text-align: left;"><strong><em>B</em></strong></td>
<td style="text-align: left;"><strong><em>SE</em></strong></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><em>Intercept</em></td>
<td style="text-align: left;">1.02</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">1.07</td>
<td style="text-align: left;">0.04</td>
<td style="text-align: left;">1.11</td>
<td style="text-align: left;">0.04</td>
<td style="text-align: left;">2.39</td>
<td style="text-align: left;">1.53</td>
<td style="text-align: left;">-0.84</td>
<td style="text-align: left;">2.04</td>
<td style="text-align: left;">-3.82</td>
<td style="text-align: left;">2.54</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Subjective financial toxicity<sup>a</sup></td>
<td style="text-align: left;">-0.01<sup>*</sup></td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">-0.01<sup>***</sup></td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">-0.01<sup>***</sup></td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">0.63<sup>***</sup></td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">0.69<sup>***</sup></td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">0.54<sup>***</sup></td>
<td style="text-align: left;">0.07</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Objective financial toxicity</td>
<td style="text-align: left;">-0.02</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-0.02</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-0.01</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">1.00</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">-0.03</td>
<td style="text-align: left;">0.73</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Aged 50 years and above</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.06<sup>**</sup></td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-0.03</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">3.81<sup>**</sup></td>
<td style="text-align: left;">1.28</td>
<td style="text-align: left;">1.88</td>
<td style="text-align: left;">1.16</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Income &gt; 5 million IDR<sup>b</sup></td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.05<sup>*</sup></td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-0.07<sup>**</sup></td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">2.50</td>
<td style="text-align: left;">1.69</td>
<td style="text-align: left;">3.27<sup>*</sup></td>
<td style="text-align: left;">1.45</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Number of children</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.02<sup>**</sup></td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.02<sup>**</sup></td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.98</td>
<td style="text-align: left;">0.58</td>
<td style="text-align: left;">-0.68</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Diagnosed 1 year or less</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-1.58</td>
<td style="text-align: left;">1.06</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Metastasis</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.09<sup>*</sup></td>
<td style="text-align: left;">0.04</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">4.83</td>
<td style="text-align: left;">2.76</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Undergoing chemotherapy</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.06<sup>*</sup></td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">1.62</td>
<td style="text-align: left;">1.65</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Comorbidities <em>(ref: none)</em></td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.01</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">1.96</td>
<td style="text-align: left;">1.23</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2+</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.03</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">2.13</td>
<td style="text-align: left;">1.40</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Symptoms in the past week <em>(ref: none)</em></td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1–3</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.01</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">1.28</td>
<td style="text-align: left;">2.13</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 4–6</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.05<sup>*</sup></td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">4.26<sup>*</sup></td>
<td style="text-align: left;">2.12</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 7–9</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.05</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">5.98<sup>**</sup></td>
<td style="text-align: left;">2.28</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 10+</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-0.18<sup>***</sup></td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">14.06<sup>***</sup></td>
<td style="text-align: left;">2.25</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Model fit</td>
<td colspan="2" style="text-align: left;"><p>F(2,297) = 19.94</p>
<p>(<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 19.60%</p></td>
<td colspan="2" style="text-align: left;"><p>F(5,294) = 9.71 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 25.98%</p></td>
<td colspan="2" style="text-align: left;"><p>F(14,285) = 8.82 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 46.39%</p></td>
<td colspan="2" style="text-align: left;"><p>F(2,297) = 34.21</p>
<p>(<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 22.74%</p></td>
<td colspan="2" style="text-align: left;"><p>F(5,294) = 16.58</p>
<p>(<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 26.94%</p></td>
<td colspan="2" style="text-align: left;"><p>F(14,285) = 15.31 (<em>p</em> &lt; 0.001)</p>
<p>R<sup>2</sup> = 46.15%</p></td>
</tr>
</tbody>
</table>

<sup>\*\*\*</sup>*p* \< 0.001, <sup>\*\*</sup>*p* \< 0.01, <sup>\*</sup>*p* \< 0.05

*Abbreviations. B = unstandardized beta coefficient, EQ HWB: EQ Health and Wellbeing, EQ-HWB-S: EQ-HWB short form, LSS = level summary scores, SE = robust standard error of the regression*

<sup>a</sup>Measured using COST - A FACIT Measure of Financial Toxicity

<sup>b</sup>Net monthly household income. IDR = Indonesian Rupiah, 324.34 USD = 5 million IDR (based on the closing 2023 middle exchange rate from Bank Indonesia)

<sup>c</sup>LSS recoded to a 0-100 scale, with higher scores indicating worse health and well-being

</div>

## Discussion

This study aimed to examine the associations between FT, HRQoL, and well-being outcomes in patients with breast cancer. We demonstrated higher SFT to be associated with more problems in EQ-5D-5L pain/discomfort, anxiety/depression, EQ-HWB-S exhaustion, anxiety, sadness/depression, pain, EQ-HWB frustration, discomfort items, lower EQ-5D-5L index value, EQ VAS, EQ-HWB-S index value, and higher EQ-HWB LSS. Higher OFT was also related to more problems in the EQ-HWB-S exhaustion item.

The distress brought about by the financial challenges arising from cancer care was, to some extent, captured by the EQ-5D-5L, EQ VAS, and EQ-HWB. This could be attributed to increased negative emotions related to financial difficulties. Insufficient financial resources may hinder access to optimal healthcare, potentially leading to a diminished HRQoL and well-being \[55, 56\]. Alternatively, it is also possible that the association is bi-directional as shown by studies using HRQoL to predict SFT \[15\]. It can be argued that patients with worse HRQoL or well-being subjectively report higher FT due to their condition and possible productivity loss. Hence, complementing the measurement of SFT with OFT seems important for a more comprehensive description of FT by identifying financial metrics or activities of patients.

Our findings suggest that FT accounted for a greater proportion of the variances in well-being, compared to HRQoL. Higher FT could mean that patients may have to make sacrifices in terms of necessities and wants, which may be related to feelings of isolation and frustration. Well-being may better capture the dynamics of FT, as it may include domains broader than HRQoL, such as pursuits that individuals desire or find meaningful, and sense of connection with one’s environment.

Overall, our results align with the existing literature from other countries and neighboring regions. Previous studies conducted in the United States, Australia, and China, focusing on various cancer types such as gastrointestinal, gynecological, and lung, have investigated associations between the SFT (FACIT-COST) and HRQoL as measured by the EQ-5D; employing other diverse methods such as generalized linear model, latent class analysis, and correlations \[52, 57–60\]. All the studies demonstrated SFT to be significantly related to lower HRQoL. Additionally, two studies, found SFT to be moderately correlated with well-being \[25, 61\]. Recent studies have also demonstrated significant associations between FT and EQ-5D-5L pain/discomfort and anxiety/depression domains with comparable association strengths \[50–52\], suggesting that FT captures or represents a form of psychological distress, a burden commonly experienced by patients with cancer. Patients with higher symptom burden may experience greater financial strain due to non-medical costs related to symptom management and hospital visits, intensifying their psychological distress.

Our analysis did not reveal a statistically significant association between OFT and the outcome variable across most regression models, despite showing significance in the subgroup comparisons. This suggests that the OFT measurement may have benefitted from a more comprehensive approach, such as the currency amount of out-of-pocket health expenditure, as well as more detailed exploration of the financial coping strategies (e.g., loan amount or receipt from sale of assets). For example, two investigations from China and Malaysia found negative associations between both SFT and OFT with HRQoL \[48, 62, 63\]. Notably, these two studies consistently measured OFT using the healthcare cost-to-income ratio, while HRQoL was assessed using various instruments: EORTC QLQ-C30, EQ-5D-5L, and FACT-Lung. However, obtaining precise data on actual healthcare costs may present challenges, such as the patient not being completely in charge of their own finances. Recalling the accurate cost amount would also be challenging, particularly in the case of our sample, whose average disease duration since diagnosis was 2.45 years and nearly 100% had insurance coverage that mitigated direct medical expenses, including diagnostic tests, medications, surgeries, and physician fees.

Reflecting on our findings, some policy implications may be considered. While causality has not been established, our findings indicate a significant correlation between higher FT and diminished HRQoL and well-being. Health and social policymakers may consider interventions aimed at alleviating FT. Firstly, it may be important to screen for FT in patients and their families. Through proper identification of those at risk, necessary mitigation strategies can be implemented. One of the most adopted FT interventions involves financial navigation programs aimed at supporting patients and families with managing the financial hardships of their treatment \[64–66\]. In the most extreme cases of poverty, extending coverage to include non-medical, cancer-related costs (e.g., transportation and accommodation for outpatients residing at a distance from healthcare facilities) may be an approach. The income-earning capacities of patients should also be protected from disruptions due to cancer \[67\], such as through employment reintegration programs to facilitate their return to work \[68\].

This study has some limitations. First, the data were collected from a single center in one country focusing on females with breast cancer. There are also less developed areas in Indonesia with higher poverty rate and lower access to healthcare. Therefore, the results may not be generalized to other types of cancer, male patients, or more resource-poor settings. Second, we solely focused on patients and did not include their caregivers or core family members. In the Indonesian context, men are still predominantly perceived as providers. Our sample primarily consisted of female homemakers and thus, FT may not have been comprehensively captured without the perspectives of the income provider. Third, nearly all patients had insurance coverage that may have led to some socio-demographic covariates not being significantly associated with the outcome variables and excluded from the regressions. However, this could also be attributed to limited response variability. Fourth, our measurement of SFT had its drawbacks. The FACIT-COST was developed in the United States and another measure may be more suited to capture financial well-being in the Indonesian context. However, it is the most widely used cancer-specific measure for SFT, allowing for comparability with previous studies. Fifth, the pilot UK value set was used for calculating the EQ-HWB-S index values, which does not fully reflect the preferences of the Indonesian population. Finally, our study design did not allow us to explore causality, which could be examined in future studies along with potential mediating factors, such as social support.

## Conclusions

This is the first study to identify associations between FT, HRQoL, and well-being outcomes in patients with breast cancer, and the first in the FT literature to use the recently developed EQ-HWB instrument to measure health and well-being. Our findings provide additional insight into the burden of cancer and its link to the HRQoL and well-being of patients in a middle-income country context, highlighting the importance of establishing health and social policies aimed at measuring and alleviating FT.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

### Acknowledgements

We express our gratitude to the Oncology Department of Hasan Sadikin General Hospital, along with Putu Rarasati, Adita Vicianti, and Afina Zahirah for their tremendous support in patient recruitment and data collection. We are also grateful to Dr. Cheng Ling Jie, for his very insightful comments on an earlier draft of the paper.

### Author contributions

All authors contributed to the conception and design, and interpretation of results. Survey instrument development and data collection were performed by Stevanus Pangestu, Fredrick Dermawan Purba, Hari Setyowibowo, and Fanni Rencz. Data analysis was performed by Stevanus Pangestu and Fanni Rencz. The first draft of the manuscript was written by Stevanus Pangestu and all authors provided critical comments on previous versions of the manuscript. All authors read and approved the final manuscript.

### Funding

Open access funding provided by Corvinus University of Budapest.

Data collection was funded by the EuroQol Research Foundation (1644-RA). Open access funding provided by Corvinus University of Budapest.

### Data availability

The data that support the results of this study are available from FDP, upon reasonable request.

### Declarations

#### Ethical approval

This study was performed in line with the principles of the Declaration of Helsinki. Approval was granted by the Ethics Committee of the Hasan Sadikin General Hospital (LB.02.01/X.6.5/284/2023).

#### Informed consent

Informed consent was obtained from all participants included in the study.

#### Conflict of interest

Fredrick Dermawan Purba, Clara Mukuria, and Fanni Rencz are active members of the EuroQol Group. Views expressed in the article are those of the authors and are not necessarily those of the EuroQol Research Foundation. Stevanus Pangestu and Hari Setyowibowo declare no competing interests.

## References

1. Kocarnik, J. M., et al. (2022). Cancer incidence, mortality, years of life lost, years lived with disability, and disability-adjusted life years for 29 cancer groups from 2010 to 2019: A systematic analysis for the global burden of disease study 2019. JAMA Oncology, 8(3), 420–444.34967848 10.1001/jamaoncol.2021.6987PMC8719276

2. Brüggen, E. C., et al. (2017). Financial well-being: A conceptualization and research agenda. Journal of Business Research, 79, 228–237. doi:10.1016/j.jbusres.2017.03.013

3. Witte, J., et al. (2019). Methods for measuring financial toxicity after cancer diagnosis and treatment: A systematic review and its implications. Annals of Oncology, 30(7), 1061–1070.31046080 10.1093/annonc/mdz140PMC6637374

4. Fitch, M. I., et al. (2022). Experiencing financial toxicity associated with cancer in publicly funded healthcare systems: A systematic review of qualitative studies. Journal of Cancer Survivorship, 16(2), 314–328.33723742 10.1007/s11764-021-01025-7

5. Udayakumar, S., et al. (2022). Cancer treatment-related financial toxicity experienced by patients in low- and middle-income countries: A scoping review. Supportive Care in Cancer, 30(8), 6463–6471.35322274 10.1007/s00520-022-06952-4

6. Pangestu, S., & Rencz, F. (2023). Comprehensive score for Financial Toxicity and Health-related quality of life in patients with Cancer and survivors: A systematic review and Meta-analysis. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 26(2), 300–316.36064514 10.1016/j.jval.2022.07.017

7. Bhanvadia, S. K., et al. (2021). Financial toxicity among patients with prostate, bladder, and kidney Cancer: A systematic review and call to action. Eur Urol Oncol, 4(3), 396–404.33820747 10.1016/j.euo.2021.02.007

8. Ritter, J., et al. (2023). Financial hardship in families of children or adolescents with cancer: A systematic literature review. The Lancet Oncology, 24(9), e364–e375.37657477 10.1016/S1470-2045(23)00320-0PMC10775706

9. Sitlinger, A., & Zafar, S. Y. (2018). Health-Related Quality of Life: The impact on morbidity and mortality. Surgical Oncology Clinics of North America, 27(4), 675–684.30213412 10.1016/j.soc.2018.05.008PMC6428416

10. Azzani, M., et al. (2024). Subjective and objective financial toxicity among colorectal cancer patients: A systematic review. Bmc Cancer, 24(1), 40.38182993 10.1186/s12885-023-11814-1PMC10770883

11. Lueckmann, S. L., et al. (2022). Identifying missing links in the conceptualization of financial toxicity: A qualitative study. Supportive Care in Cancer, 30(3), 2273–2282.34716793 10.1007/s00520-021-06643-6PMC8795015

12. Kang, D., et al. (2022). Impact of objective financial burden and subjective financial distress on spiritual well-being and quality of life among working-age cancer survivors. Supportive Care in Cancer, 30(6), 4917–4926.35174421 10.1007/s00520-022-06906-w

13. de Souza, J. A., et al. (2017). Measuring financial toxicity as a clinically relevant patient-reported outcome: The validation of the COmprehensive score for financial toxicity (COST). Cancer, 123(3), 476–484.27716900 10.1002/cncr.30369PMC5298039

14. Head, B. A., & Faul, A. C. (2008). Development and validation of a scale to measure socioeconomic well-being in persons with cancer. The Journal of Supportive Oncology, 6(4), 183–192.18491687

15. Pangestu, S., et al. (2023). Financial toxicity experiences of patients with Cancer in Indonesia: An interpretive phenomenological analysis. Value Health Reg Issues, 41, 25–31.38154366 10.1016/j.vhri.2023.11.007

16. Jiang, H., et al. (2023). Association between financial toxicity and health-related quality of life in cancer survivors: A systematic review. Asia Pac J Clin Oncol, 19(4), 439–457.36457166 10.1111/ajco.13901

17. Zhu, Z., et al. (2020). Cancer survivors’ experiences with financial toxicity: A systematic review and meta-synthesis of qualitative studies. Psychooncology, 29(6), 945–959.32372481 10.1002/pon.5361

18. Zhu, Z., et al. (2022). Psychometric properties of self-reported financial toxicity measures in cancer survivors: A systematic review. British Medical Journal Open, 12(6), e057215.10.1136/bmjopen-2021-057215PMC923480435750459

19. Donkor, A., et al. (2022). Financial toxicity of cancer care in low- and middle-income countries: A systematic review and meta-analysis. Supportive Care in Cancer, 30(9), 7159–7190.35467118 10.1007/s00520-022-07044-zPMC9385791

20. Ehsan, A. N., et al. (2023). Financial toxicity among patients with breast Cancer Worldwide: A systematic review and Meta-analysis. JAMA Netw Open, 6(2), e2255388.36753274 10.1001/jamanetworkopen.2022.55388PMC9909501

21. Romero, M., Vivas-Consuelo, D., & Alvis-Guzman, N. (2013). Is Health Related Quality of Life (HRQoL) a valid indicator for health systems evaluation? Springerplus, 2(1), 664.24353981 10.1186/2193-1801-2-664PMC3866375

22. Yin, S., et al. (2016). Summarizing health-related quality of life (HRQOL): Development and testing of a one-factor model. Popul Health Metr, 14, 22.27408606 10.1186/s12963-016-0091-3PMC4940947

23. Nutbeam, D., & Muscat, D. M. (2021). Health Promotion Glossary 2021. Health Promotion International, 36(6), 1578–1598.33822939 10.1093/heapro/daaa157

24. Linton, M. J., Dieppe, P., & Medina-Lara, A. (2016). Review of 99 self-report measures for assessing well-being in adults: Exploring dimensions of well-being and developments over time. British Medical Journal Open, 6(7), e010641.10.1136/bmjopen-2015-010641PMC494774727388349

25. Yu, H. H., et al. (2021). The COmprehensive score for financial toxicity in China: Validation and responsiveness. J Pain Symptom Manage, 61(6), 1297–1304e1.33412268 10.1016/j.jpainsymman.2020.12.021

26. Cotlear, D., et al. (2015). Going universal: How 24 developing countries are implementing universal health coverage from the bottom up. World Bank.

27. Bray, F., et al. (2018). Global cancer statistics 2018: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. C Ca: A Cancer Journal for Clinicians, 68(6), 394–424.10.3322/caac.2149230207593

28. Kosen, S. (2022). Coverage and implementation of healthcare delivery for cancer under national health insurance, experience of Indonesia. Lancet Reg Health Southeast Asia, 6, 100065.37383347 10.1016/j.lansea.2022.100065PMC10305872

29. Ministry of Health of Republic of Indonesia. Health Research and Development Ethical Guidelines and Standards (In Indonesian) (2021). [cited 2024 January 18]; Available from: https://repository.badankebijakan.kemkes.go.id/id/eprint/4214/1/Pedoman%20dan%20Standar%20Etik%20Penelitian%20dan%20Pengembangan%20Kesehatan%20Nasional.pdf

30. Pangestu, S., et al. (2024). Validity, test-retest reliability, and responsiveness of the Indonesian version of FACIT-COST measure for subjective financial toxicity. Health and Quality of Life Outcomes, 22(1), 89.39427212 10.1186/s12955-024-02303-5PMC11491015

31. Pangestu, S. (2024). The Psychometric properties of the EQ-HWB and EQ-HWB-S in patients with breast Cancer: A comparative analysis with EQ-5D-5L, FACT-8D, and SWEMWBS. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, Online ahead of print.10.1016/j.jval.2024.12.00339733837

32. Herdman, M., et al. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research, 20(10), 1727–1736.21479777 10.1007/s11136-011-9903-xPMC3220807

33. Purba, F. D., et al. (2017). The Indonesian EQ-5D-5L Value Set. Pharmacoeconomics, 35(11), 1153–1165.28695543 10.1007/s40273-017-0538-9PMC5656740

34. Shim, S., et al. (2022). Validation of Korean Version of the COmprehensive score for financial toxicity (COST) among breast Cancer survivors. Cancer Res Treat, 54(3), 834–841.34645130 10.4143/crt.2021.784PMC9296937

35. Sagberg, L. M., Jakola, A. S., & Solheim, O. (2014). Quality of life assessed with EQ-5D in patients undergoing glioma surgery: What is the responsiveness and minimal clinically important difference? Quality of Life Research, 23(5), 1427–1434.24318084 10.1007/s11136-013-0593-4

36. Zeng, X., et al. (2021). Measurement Properties of the EQ-5D-5L and EQ-5D-3L in six commonly diagnosed cancers. Patient, 14(2), 209–222.33123985 10.1007/s40271-020-00466-z

37. Zhu, J., et al. (2021). Comparing EQ-5D-3L and EQ-5D-5L performance in common cancers: Suggestions for instrument choosing. Quality of Life Research, 30(3), 841–854.32930993 10.1007/s11136-020-02636-w

38. Brazier, J., et al. (2022). The EQ-HWB: Overview of the development of a measure of Health and Wellbeing and Key results. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 25(4), 482–491.35277337 10.1016/j.jval.2022.01.009

39. Peasgood, T. (2021). What is the best approach to adopt for identifying the domains for a new measure of health, social care and carer-related quality of life to measure quality-adjusted life years? Application to the development of the EQ-HWB? Eur J Health Econ, 22(7): pp. 1067–1081.10.1007/s10198-021-01306-zPMC831893533909157

40. Peasgood, T., et al. (2022). Developing a New Generic Health and Wellbeing measure: Psychometric survey results for the EQ-HWB. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 25(4), 525–533.35365299 10.1016/j.jval.2021.11.1361

41. Augustovski, F., et al. (2022). The development of a New International Generic measure (EQ-HWB): Face validity and psychometric stages in Argentina. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 25(4), 544–557.35148961 10.1016/j.jval.2021.12.010

42. Monteiro, A. L., Kuharic, M., & Pickard, A. S. (2022). A comparison of a preliminary Version of the EQ-HWB short and the 5-Level version EQ-5D. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 25(4), 534–543.35279371 10.1016/j.jval.2022.01.003

43. Kuharić, M. (2024). The Measurement Properties of the EQ Health and Well-being and EQ Health and Well-Being Short Form in Italian Population: A comparative study with EQ-5D-5L. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research.10.1016/j.jval.2024.03.00238490471

44. Mukuria, C., et al. (2023). Valuing the EQ Health and Wellbeing Short using Time Trade-Off and a Discrete Choice experiment: A feasibility study. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 26(7), 1073–1084.36805577 10.1016/j.jval.2023.02.008

45. de Souza, J. A., et al. (2014). The development of a financial toxicity patient-reported outcome in cancer: The COST measure. Cancer, 120(20), 3245–3253.24954526 10.1002/cncr.28814

46. Ng, M. S. N., et al. (2021). Identifying a cut-off score for the COST measure to indicate high financial toxicity and low quality of life among cancer patients. Supportive Care in Cancer, 29(10), 6109–6117.33797583 10.1007/s00520-020-05962-4

47. Gordon, L. G., et al. (2017). A systematic review of Financial Toxicity among Cancer survivors: We can’t pay the co-pay. Patient, 10(3), 295–309.27798816 10.1007/s40271-016-0204-x

48. Ting, C. Y., et al. (2020). Financial toxicity and its associations with health-related quality of life among urologic cancer patients in an upper middle-income country. Supportive Care in Cancer, 28(4), 1703–1715.31292755 10.1007/s00520-019-04975-y

49. Chan, R. J., et al. (2019). Relationships between Financial Toxicity and Symptom Burden in Cancer survivors: A systematic review. J Pain Symptom Manage, 57(3), 646–660e1.30550833 10.1016/j.jpainsymman.2018.12.003

50. Thaduri, A., et al. (2023). Financial toxicity and mental well-being of the oral cancer survivors residing in a developing country in the era of COVID 19 pandemic - A cross-sectional study. Psychooncology, 32(1), 58–67.36073555 10.1002/pon.6030PMC9539264

51. Murphy, P. B., et al. (2019). Financial toxicity is associated with worse physical and emotional long-term outcomes after traumatic injury. J Trauma Acute Care Surg, 87(5), 1189–1196.31233442 10.1097/TA.0000000000002409PMC6815224

52. Xu, R. H., et al. (2022). Urban-rural differences in financial toxicity and its effect on cancer survivors’ health-related quality of life and emotional status: A latent class analysis. Supportive Care in Cancer, 30(5), 4219–4229.35083540 10.1007/s00520-021-06762-0

53. Rencz, F., & Janssen, M. F. (2022). Analyzing the Pain/Discomfort and Anxiety/Depression composite domains and the meaning of discomfort in the EQ-5D: A mixed-methods study. Value In Health: The Journal of the International Society for Pharmacoeconomics and Outcomes Research, 25(12), 2003–2016.35973925 10.1016/j.jval.2022.06.012

54. Cohen, J. (1992). Quantitative methods in psychology: A power primer. Psychological Bulletin, 112, 1155–1159.10.1037//0033-2909.112.1.15519565683. doi:10.1037/0033-2909.112.1.155

55. Chino, F., & Zafar, S. Y. (2019). Financial Toxicity and Equitable Access to clinical trials. Am Soc Clin Oncol Educ Book, 39, 11–18.31099681 10.1200/EDBK_100019

56. Tucker-Seeley, R. D. (2023). Financial toxicity: A barrier to Achieving Health Equity in Cancer Care. J Am Coll Radiol, 20(1), 37–39.36503172 10.1016/j.jacr.2022.12.004PMC9797364

57. Ehlers, M., et al. (2021). A national cross-sectional survey of financial toxicity among bladder cancer patients. Urologic Oncology, 39(1), 76.e1-76.e7.10.1016/j.urolonc.2020.09.03033268274

58. Gordon, L. G., et al. (2020). The economic impact on Australian patients with neuroendocrine tumours. Patient, 13(3), 363–373.32072460 10.1007/s40271-020-00412-z

59. Bouberhan, S., et al. (2019). Financial toxicity in gynecologic oncology. Gynecologic Oncology, 154(1), 8–12.31053404 10.1016/j.ygyno.2019.04.003PMC7001853

60. Esselen, K. M., et al. (2021). Crowdsourcing to measure financial toxicity in gynecologic oncology. Gynecologic Oncology, 161(2), 595–600.33551197 10.1016/j.ygyno.2021.01.040PMC10029746

61. Chen, G. (2023). Measuring the wellbeing of Cancer patients with generic and Disease-Specific instruments. Cancers (Basel), 15(4).10.3390/cancers15041351PMC995459736831692

62. Xu, R. H. (2020). Quantifying the Effect of Financial Burden on Health-Related Quality of Life among Patients with Non-Hodgkin’s Lymphomas. Cancers (Basel), 12(11).10.3390/cancers12113325PMC769809233187112

63. Chen, J. E., et al. (2018). Objective and subjective financial burden and its associations with health-related quality of life among lung cancer patients. Supportive Care in Cancer, 26(4), 1265–1272.29105024 10.1007/s00520-017-3949-4

64. Smith, G. L., et al. (2022). Navigating financial toxicity in patients with cancer: A multidisciplinary management approach. C Ca: A Cancer Journal for Clinicians, 72(5), 437–453.10.3322/caac.21730PMC1299461435584404

65. Edward, J., et al. (2022). Interventions to address cancer-related financial toxicity: Recommendations from the field. Journal of Rural Health, 38(4), 817–826.10.1111/jrh.12637PMC916320434861066

66. Knight, T. G., et al. (2022). Financial toxicity intervention improves outcomes in patients with hematologic malignancy. JCO Oncol Pract, 18(9), e1494–e1504.35709421 10.1200/OP.22.00056

67. Mols, F., et al. (2020). Financial toxicity and employment status in cancer survivors. A systematic literature review. Supportive Care in Cancer, 28(12), 5693–5708.32865673 10.1007/s00520-020-05719-zPMC7686183

68. Pearce, A., et al. (2019). Financial toxicity is more than costs of care: The relationship between employment and financial toxicity in long-term cancer survivors. Journal of Cancer Survivorship, 13(1), 10–20.30357537 10.1007/s11764-018-0723-7

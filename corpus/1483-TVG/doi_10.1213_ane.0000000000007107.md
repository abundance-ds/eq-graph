---
project_id: "1483-TVG"
work_id: "doi:10.1213/ane.0000000000007107"
doi: "10.1213/ANE.0000000000007107"
pmid: "39042570"
pmcid: "PMC11805468"
title: "Socioeconomic, Patient, and Hospital Determinants for the Utilization of Peripheral Nerve Blocks in Total Joint Arthroplasty"
journal: "Anesthesia and Analgesia"
publication_date: "2025-02-14"
volume: "140"
issue: "3"
authors:
  - name: "Joshua M Bonsel"
    affiliation_ids:
      - "aff1"
  - name: "Hanish Kodali"
    affiliation_ids:
      - "aff2"
  - name: "Jashvant Poeran"
    affiliation_ids:
      - "aff2"
  - name: "Gouke J Bonsel"
    affiliation_ids:
      - "aff3"
affiliations:
  - id: "aff1"
    name: "From the *Department of Orthopedics and Sports Medicine, Erasmus Medical Center, Rotterdam, the Netherlands"
  - id: "aff2"
    name: "Department of Population Health and Policy, Icahn School of Medicine, Mount Sinai Hospital, New York, New York"
  - id: "aff3"
    name: "EuroQol Research Foundation, Rotterdam, the Netherlands."
licence: "cc-by"
source_file: "input/projects/1483-TVG/papers/doi_10.1213_ane.0000000000007107.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11805468/fullTextXML"
source_method: "epmc_xml"
source_sha256: "29b8e49882800ec858ac6d8027cb8d474b27e857dd132b9b4b10f05886bab8a0"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Socioeconomic, Patient, and Hospital Determinants for the Utilization of Peripheral Nerve Blocks in Total Joint Arthroplasty

## Abstract

### BACKGROUND:

While peripheral nerve blocks (PNBs) are associated with various improved outcomes in patients undergoing total hip or knee arthroplasty (THA/TKA), disparities in PNB utilization have been reported. This study assessed the importance of socioeconomic, demographic, clinical, and hospital determinants in explaining PNB utilization using the population-attributable risk (PAR) framework. Subsequently, we examined the association between PNB use and 3 secondary outcomes: Centers for Medicare and Medicaid Services (CMS)-defined complications, 90-day all-cause readmissions, and length of stay \>3 days.

### METHODS:

This retrospective cohort study included 52,926 THA and 94,795 TKA cases from the 5% 2012 to 2021 Medicare dataset. Mixed-effects logistic regression models measured the association between study variables and PNB utilization. Variables of interest were demographic (age, sex), clinical (outpatient setting, diagnosis, prior hospitalizations in the year before surgery, Deyo-Charlson index, obesity, (non)-opioid abuse, smoking), socioeconomic (neighborhood Social Deprivation Index, race and ethnicity) and hospital variables (beds, ownership, region, rurality, resident-to-bed ratio). The model was used for the calculation of variable-specific and variable category-specific PARs (presented in percentages), reflecting the proportion of variation in PNB use explained after eliminating variables (or groups of variables) of interest with all other factors held constant. Subsequently, regression models measured the association between PNB use and secondary outcomes. Associations are presented with odds ratios (ORs) and 95% confidence intervals (95% CIs).

### RESULTS:

Socioeconomic and demographic variables accounted for only a small proportion of variation in PNB use (up to 3% and 7%, respectively). Clinical (THA: 46%; TKA: 34%) and hospital variables (THA: 31%; TKA: 22%) were the primary drivers of variation. In THA, variation by clinical variables was driven by increased PNB use in the inpatient setting (OR, 1.28 \[95% CI, 1.07–1.53\]) and decreased use in patients with ≥2 prior hospitalizations (OR, 0.72 \[95% CI, 0.57–0.90\]). Moreover, nonosteoarthritis diagnoses associated with reduced PNB utilization in THA (OR, 0.64 \[95% CI, 0.58–0.72\]) and TKA (OR, 0.35 \[95% CI, 0.34–0.37\]).

In TKA, PNB use was subsequently associated with fewer complications (OR, 0.82 \[95% CI, 0.75–0.90\]) and less prolonged length of stay (OR, 0.90 \[95% CI, 0.86–0.95\]); no association was found for readmissions (OR, 0.98 \[95% CI, 0.93–1.03\]). In THA, associations did not reach statistical significance.

### CONCLUSIONS:

Among THA and TKA patients on Medicare, large variations exist in the utilization of PNBs by clinical and hospital variables, while demographic and socioeconomic variables played a limited role. Given the consistent benefits of PNBs, particularly in TKA patients, more standardized provision may be warranted to mitigate the observed variation.

Accepted 2024 May 16; Issue date 2025 Mar.

<div class="caption">

###### KEY POINTS

</div>

**Question:** What is the importance of socioeconomic, demographic, clinical, and hospital determinants for the utilization of peripheral nerve blocks (PNBs) in total hip and knee arthroplasty patients (THA/TKA), and do PNBs associate with improved outcomes?

**Findings:** In both THA and TKA patients on Medicare, clinical (eg, indication for surgery) and hospital variables explained most variation in PNB use, while demographic and socioeconomic variables played a limited role; in TKA patients, PNBs were also associated with reduced complications and length of stay.

**Meaning:** Our findings emphasize substantial individual and hospital practice variation in PNB use; as PNBs are consistently associated with improved outcomes, particularly in TKA patients, the findings are a plea for more standardized provision of PNBs.

While peripheral nerve blocks (PNBs) have been associated with improved outcomes in patients undergoing total hip or knee arthroplasty (THA/TKA),<sup>1,2</sup> disparities in their utilization based on patient and hospital determinants have been reported.<sup>3–5</sup> Indeed, studies have shown that being younger, un(der)insured, or belonging to a minority group is associated with lower odds of receiving PNBs.<sup>6,7</sup> At the hospital level, a rural location and teaching status are associated with decreased PNB utilization.<sup>4</sup> However, size and even direction of effect are not always consistent as illustrated by a recent study including both patient- and hospital-level variables.<sup>8</sup>

Separating the effect of factors of interest is complex in both statistical analysis and daily practice, as they are often interrelated. One should account for the so-called “level” of their action (eg, patient-level versus hospital-level effects). Also, the impact indicator should reflect both the prevalence and the strength of the determinants. For example, even if there is a very strong association indicating Black patients receive fewer PNBs, its population-level impact will be limited in a hypothetical population with only a few Black patients. In a population with more Black patients, the population-level impact may still be limited if the strength of the race-PNB association is weaker than other or higher-level factors. The population-attributable risk (PAR) concept, combined with stepwise analysis methods to account for the aforementioned “level” of action issue, provides a valuable approach for this purpose.<sup>9,10</sup> The PAR assesses the impact of a determinant (or study variable of effect) in terms of the proportion of PNB use accounted for by that determinant.

Our study aimed to get a deeper understanding of the source of PNB variation. We estimated the importance of the socioeconomic background (including race/ethnicity and a proxy for socioeconomic status \[SES\]), demographic, clinical, and hospital determinants of the patient in explaining PNB utilization. We hypothesized a greater role of hospital versus patient variables and that within the latter PNB use would be lower in minority patients and those with a lower SES. We subsequently examined the association between PNB use and 3 important outcomes related to THA/TKA (complications, 90-day all-cause readmissions, and length of stay) hypothesizing that PNB would be associated with improved outcomes, further emphasizing the importance of minimizing the hypothesized variation in PNB use.

## METHODS

### Data

In this retrospective cohort study, we analyzed inpatient and outpatient THAs and TKAs performed between 2012 and 2021 (all data available to our research group) as recorded in the Medicare Limited Dataset.<sup>11</sup> Given the deidentified nature of the data source, this study was exempt from full review by the Mount Sinai Institutional Review Board (STUDY-20-01677). This study followed the Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) guidelines.<sup>12</sup>

<figure id="F1">
<p><img src="ane-140-675-g001.jpg" /></p>
<p><img src="ane-140-675-g001.gif" /></p>
<figcaption>Flowchart depicting sample selection.</figcaption>
</figure>

The Medicare database includes patient-level claims of all Medicare-insured patients in the United States. The inpatient and outpatient files contain an incomplete overview of the PNBs used; therefore, we also used the Carrier file to define PNBs, which made it necessary to use the 5% random sample. Each encounter contains information on procedural (Current Procedural Terminology \[CPT\]) and diagnosis-related (International Classification of Diseases ninth Revision codes \[ICD\]) codes. In 2015 the International Classification of Diseases tenth Revision coding system (ICD-10) was introduced. As this database mainly captures individuals aged over 65 and/or with disabilities, younger patients with or without private insurance are not included.

### Inclusion and Exclusion Criteria of the Sample

We constructed an initial cohort of 241,326 primary THA (CPT: 27130, ICD-9: 81.51, ICD-10: 0SR90, 0SRB0) and TKA (CPT: 27477, ICD-9: 81.54, ICD-10: 0SRC0, 0SRD0) patients. To define comorbidity prevalence and complication rate before and after surgery, respectively, we excluded patients who had surgery in 2012 or the last 3 months of 2021 (n = 21,609). Subsequently, we excluded patients who were not continuously enrolled in the database for at least 1 year prior to and 3 months after their joint arthroplasty (n = 41,375); patients inhabiting unincorporated territories of the United States (n = 186); aged \<66 (n = 21,467); eligibility for Medicare due to end-stage renal disease (n = 347); patients having claims of both THA and TKA simultaneously (n = 711). For each patient, we only kept index arthroplasties which were 90 days apart, excluding another n = 2309 claims. Therefore, repeat procedures are not expected.<sup>13</sup> Patients may have had a contralateral procedure or procedure of another joint. Given the nature of the data, we were unable to determine whether patients had prior primary joint replacement before enrolling in Medicare. This process resulted in a sample of 153,322 patients (Figure).

### Variables

Variables were selected based on the potential influence on PNB use either found in previous studies or based on clinical judgement.<sup>4–8,14</sup> Directly obtained were age, sex, and year of surgery. Race and ethnicity was grouped as White, Black, and other (Asian, Hispanic, North American Native, other).<sup>15</sup> Diagnosis was defined as either osteoarthritis or nonosteoarthritis using ICD codes (attached in Supplemental Digital Content 1, Supplemental Table 1, <http://links.lww.com/AA/E911>). We calculated the Deyo-Charlon comorbidity index and categorized it into 0, 1, 2, and ≥3.<sup>16,17</sup> We identified a history of obesity, smoking, nonopioid, and opioid abuse. Prior hospitalization was defined as any acute care hospitalization in the 365 days before receiving surgery (excluding index arthroplasties) and was categorized into 0, 1, or ≥2. The effect of these variables on arthroplasty outcomes is well known, however, to our knowledge they have not been studied in the context of PNB utilization.

The 2019 neighborhood Social Deprivation Index (SDI) provides details on the place of living and was individually linked to the state-county ID. The SDI is a composite measure based on 7 characteristics, where a 1 to 100 SDI score is calculated using 5-year (2014–2019) averaged data from the American Community Survey: % living in poverty, % with \<12 years of education, % single-parent households, % living in rented housing units, % living in the overcrowded housing unit, % of households without a car, and % nonemployed adults under 65 years of age.<sup>18</sup> We categorized it into 5 groups based on the thresholds for the 20th, 40th, 60th, and 80th percentiles.<sup>19</sup> Neighborhood deprivation indices are generally stable over time, and the currently applied measure is assumed valid for the included timeframe.<sup>20</sup>

The following hospital data were derived from the 2017 Hospital Inpatient Prospective Payment System 2017 impact file: beds (0–150, 150–499, and ≥500), ownership (government, physician/proprietary, voluntary), rurality (large urban, small urban and rural), region (Northeast, South, Midwest, and West) and resident-to-bed ratio.<sup>21</sup> The resident-to-bed ratio is defined as the ratio of (interns + residents)/average operating beds; this ratio has previously been used as a proxy for teaching intensity. The ratio was categorized as \<0.05 reflecting no teaching, 0.05 to 0.249 reflecting minor teaching, and ≥0.25 reflecting major teaching.<sup>22,23</sup> Slight variations in hospital variables may occur over time: to maintain the ability to estimate the effects of these variables at the hospital level, we linked the IPPS file available in the middle of the included timeframe.

Missingness in any of the variables was present in 5% of THA and TKA patients and was mainly attributable to hospitals not being recorded in the IPPS file. Missingness was unrelated to outcomes; therefore, we conducted a complete case analysis (Supplemental Digital Content 2, Supplemental Figures 1–4, <http://links.lww.com/AA/E912>). This resulted in a final sample of n = 147,721 patients.

### Peripheral Nerve Block Utilization, Complication Incidence, and Length of Stay (Outcomes)

Our primary outcome was the utilization of any form of PNB for the received joint arthroplasty, which was defined using CPT and ICD codes (Supplemental Digital Content 1, Supplemental Table 1, <http://links.lww.com/AA/E911>) submitted on the day of surgery, or at maximum 1 day before or 1 day after surgery. The 3 secondary outcomes of interest were Centers for Medicare and Medicaid Services (CMS)-defined complication (definition in Supplemental Digital Content 3, Supplemental Table 2, <http://links.lww.com/AA/E913>), 90-day all-cause readmissions and length of stay \>3 days. Based on empirical evidence, CMS has defined outcome measures for commonly performed procedures, which are used to determine hospitals’ performance and to adjust reimbursement rates. The measure captures negative outcomes that are likely attributable to the studied procedure, and which represent the quality of the provided care. In THA and TKA, a CMS-defined complication includes acute myocardial infarction, pneumonia, or sepsis/septicemia/shock during the admission or within 7 days from the date of admission; pulmonary embolism, surgical site bleeding or death during the admission or within 30 days from the date of admission; mechanical complications, surgical site bleeding or peri-prosthetic joint/wound infection during the admission or within 90 days from the date of admission.<sup>24</sup>

### Statistical Analysis

THA and TKA patients were analyzed separately. Patient and hospital variables were compared between recipients and nonrecipients of a PNB. We used χ2 test for categorical variables.

For our first research question, we aimed to explore the relative contribution of each variable to the use of PNBs whilst accounting for potential confounding effects. Because hospital-level variables generally strongly affect PNB use, unmeasured factors may play a role. Logistic regression null models were compared with and without a random intercept for the hospital. Model fit improved drastically, with intraclass correlation coefficients (ICC) of 0.67 (THA) and 0.47 (TKA). The addition of a random intercept for the patient (3-level model) to account for contralateral procedures had minimal effect and was therefore not included in the final models. All variables of interest were entered as fixed effects: age, sex, outpatient setting, diagnosis, prior hospitalizations, Deyo index, obesity, (non)-opiod abuse, smoking, SDI, race and ethnicity, hospital beds, ownership, region, rurality, and resident-to-bed ratio. We assessed potential multicollinearity among variables using Spearman rank correlation indices. With all pairwise correlation indices \<0.4, we determined the risk of multicollinearity to be low, as commonly accepted thresholds range from 0.5 to 0.8.<sup>25,26</sup> The year of the surgery was adjusted for in the analysis, but was not considered a variable of interest with regard to our primary research question; it would have provided no opportunity for practice change. Within a categorical variable, the category with the highest amount of PNBs used was selected as a reference category. The reference category was generally the same for THA and TKA; if not, we opted to keep the same category as a reference in both THA and TKA.

To visualize the contribution of each variable to the use of PNBs we calculated PARs. Conventionally, PARs are calculated as \[Pr(O) – Pr(O\|E)\]/ Pr(O), where Pr(O) is the probability of outcome in the study population, Pr(O\|E) is the hypothetical probability of outcome if the variable of interest were eliminated.<sup>27</sup> This approach fails to take confounders into account; therefore, we used abovementioned regression models to estimate confounder-adjusted PARs, currently the most efficient method available.<sup>27</sup> We followed a previously described approach.<sup>9</sup> Study population estimates of the number of PNBs used \[Pr(O)\] and estimates for each variable’s category predicting the least amount of PNBs \[Pr(O\|E)\] were obtained using the regression models. The PAR for each variable was calculated using the abovementioned formula (univariable PARs). The interpretation of an univariable PAR is the maximum % of PNB variation explained by eliminating that variable while controlling for confounding effects of other variables, assuming all potential confounders have been accounted for.

Sequential PARs were calculated for groups of variables: demographic (age, sex), clinical (outpatient setting, diagnosis, prior hospitalizations, Deyo index, obesity, (non)-opioid abuse, smoking), socioeconomic (SDI, race and ethnicity) and hospital (hospital beds, ownership, region, rurality, resident-to-bed ratio) variables. First, estimates for a group of variables set to the least amount of PNBs are obtained, and the PAR is calculated. Subsequently, the next group of variables is also set to the least amount of PNBs and new estimates are obtained, and the difference in PAR is calculated. This second procedure is repeated until all 4 groups are eliminated. The sequential PAR at each step represents the added variation explained by a group of variables after the preceding group(s) of variables have been eliminated. The order of eliminating groups of variables influences the sequential PARs because variables are potentially interrelated.<sup>28,29</sup> Our primary order of interest was demographic \> clinical \> socioeconomic \> hospital-level variables, based on the assumption that biological variables precede hospital variables. Reverse ordering was also assessed to evaluate the degree of interrelatedness of variables. If PAR estimates are similar for different orderings, groups of variables act independently on the utilization of PNBs. If PAR estimates differ, variable groups are at least statistically interrelated; for example, eliminating clinical variables may explain 10% of the variation in PNB. However, by eliminating demographics before clinical variables, the additional effect of clinical variables may be reduced to 5%, which would indicate interrelatedness between these groups of variables. In case of interrelatedness, univariable PARs exceed the total PAR for all risk factors combined.<sup>30</sup>

For our second research question, mixed-effects logistic regression models with adjustment for the same variables measured the association between PNBs and the 3 secondary outcomes.

Two sensitivity analyses were conducted. Firstly, we checked whether there was a variation in PNB utilization by county of residence beyond the variation measured with the SDI. We re-ran the primary models replacing SDI by state-county ID (n = 3200) as random intercept (3-level model), and entering both simultaneously, and evaluated coefficients and model fit. Secondly, dual eligibility status (Medicare and Medicaid) was added as a variable of interest. As this variable has been collected since 2017,<sup>31</sup> all models were re-run from using data from 2017 onwards.

No post hoc power calculations were performed given the exploratory nature of this study. Interaction between independent variables was not estimated, and the standard errors obtained from the models did not account for potential clustering. We report odds ratios (ORs) with 95% confidence intervals (95% CIs), while PARs are reported in %. Model performance was assessed using the c-statistic. ICCs reflect the variance captured by the random intercept for the hospital in each model. Although a *P*-value \<0.05 was considered statistically significant, they were interpreted in combination with the strength of association. We conducted our analyses using R (version 4.2.3).

## RESULTS

### Descriptive Analysis

We included 52,000 THAs and 93,448 TKAs with 7.9% (n = 4086) and 57.2% (n = 53,459) PNB use, respectively. The use of PNBs increased over the years. Univariable comparison (Table <a href="#T1" data-ref-type="table">1</a>) of variables according to PNB use produced a similar pattern compared to the multivariable analysis (Table <a href="#T2" data-ref-type="table">2</a>) and is therefore not separately discussed; the few exceptions to this pattern are mentioned.

<div id="T1" class="table-wrap">

<div class="caption">

Descriptive Statistics of Total Hip and Knee Arthroplasty Patients by the Utilization of Any Type of PNB

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Total hip arthroplasty</th>
<th colspan="3" style="text-align: left;">Total knee arthroplasty</th>
</tr>
<tr>
<th style="text-align: left;">Variables</th>
<th style="text-align: left;">No PNB</th>
<th style="text-align: left;">PNB</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">No PNB</th>
<th style="text-align: left;">PNB</th>
<th style="text-align: left;"><em>P</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">n</td>
<td style="text-align: left;">47,914</td>
<td style="text-align: left;">4086</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">39,989</td>
<td style="text-align: left;">53,459</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Patient characteristics</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.085</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">  65–69</td>
<td style="text-align: left;">10,774 (22.5)</td>
<td style="text-align: left;">932 (22.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">10,254 (25.6)</td>
<td style="text-align: left;">12,871 (24.1)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  70–74</td>
<td style="text-align: left;">14,572 (30.4)</td>
<td style="text-align: left;">1243 (30.4)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">13,264 (33.2)</td>
<td style="text-align: left;">17,842 (33.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  75–79</td>
<td style="text-align: left;">11,034 (23.0)</td>
<td style="text-align: left;">998 (24.4)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9370 (23.4)</td>
<td style="text-align: left;">13,404 (25.1)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  80–84</td>
<td style="text-align: left;">7051 (14.7)</td>
<td style="text-align: left;">564 (13.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4956 (12.4)</td>
<td style="text-align: left;">6786 (12.7)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  &gt;84</td>
<td style="text-align: left;">4483 (9.4)</td>
<td style="text-align: left;">349 (8.5)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2145 (5.4)</td>
<td style="text-align: left;">2556 (4.8)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">30,186 (63.0)</td>
<td style="text-align: left;">2622 (64.2)</td>
<td style="text-align: left;">.141</td>
<td style="text-align: left;">25,670 (64.2)</td>
<td style="text-align: left;">34,046 (63.7)</td>
<td style="text-align: left;">.112</td>
</tr>
<tr>
<td style="text-align: left;">Inpatient (vs outpatient)</td>
<td style="text-align: left;">43,726 (91.3)</td>
<td style="text-align: left;">3685 (90.2)</td>
<td style="text-align: left;">.022</td>
<td style="text-align: left;">35,562 (88.9)</td>
<td style="text-align: left;">44,193 (82.7)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Diagnosis nonosteoarthritis</td>
<td style="text-align: left;">11,904 (24.8)</td>
<td style="text-align: left;">841 (20.6)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">9257 (23.1)</td>
<td style="text-align: left;">6910 (12.9)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Prior hospitalizations</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.027</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 0</td>
<td style="text-align: left;">39,949 (83.4)</td>
<td style="text-align: left;">3434 (84.0)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">34,611 (86.6)</td>
<td style="text-align: left;">46,984 (87.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">5889 (12.3)</td>
<td style="text-align: left;">511 (12.5)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4162 (10.4)</td>
<td style="text-align: left;">5200 (9.7)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> ≥2</td>
<td style="text-align: left;">2076 (4.3)</td>
<td style="text-align: left;">141 (3.5)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1216 (3.0)</td>
<td style="text-align: left;">1275 (2.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Deyo index</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.834</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.835</td>
</tr>
<tr>
<td style="text-align: left;"> 0 (healthiest)</td>
<td style="text-align: left;">17,600 (36.7)</td>
<td style="text-align: left;">1491 (36.5)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">14,449 (36.1)</td>
<td style="text-align: left;">19,177 (35.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">10,531 (22.0)</td>
<td style="text-align: left;">905 (22.1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9512 (23.8)</td>
<td style="text-align: left;">12,747 (23.8)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: left;">7668 (16.0)</td>
<td style="text-align: left;">637 (15.6)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">6291 (15.7)</td>
<td style="text-align: left;">8408 (15.7)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> ≥3 (least healthy)</td>
<td style="text-align: left;">12,115 (25.3)</td>
<td style="text-align: left;">1053 (25.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9737 (24.3)</td>
<td style="text-align: left;">13,127 (24.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Obese</td>
<td style="text-align: left;">11,132 (23.2)</td>
<td style="text-align: left;">958 (23.4)</td>
<td style="text-align: left;">.772</td>
<td style="text-align: left;">12,138 (30.4)</td>
<td style="text-align: left;">16,888 (31.6)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Abuse of nonopioids</td>
<td style="text-align: left;">2880 (6.0)</td>
<td style="text-align: left;">268 (6.6)</td>
<td style="text-align: left;">.169</td>
<td style="text-align: left;">1485 (3.7)</td>
<td style="text-align: left;">2221 (4.2)</td>
<td style="text-align: left;">.001</td>
</tr>
<tr>
<td style="text-align: left;">Abuse of opioids</td>
<td style="text-align: left;">460 (1.0)</td>
<td style="text-align: left;">58 (1.4)</td>
<td style="text-align: left;">.006</td>
<td style="text-align: left;">270 (0.7)</td>
<td style="text-align: left;">387 (0.7)</td>
<td style="text-align: left;">.399</td>
</tr>
<tr>
<td style="text-align: left;">Smoking</td>
<td style="text-align: left;">4910 (10.2)</td>
<td style="text-align: left;">396 (9,7)</td>
<td style="text-align: left;">.271</td>
<td style="text-align: left;">3892 (9.7)</td>
<td style="text-align: left;">4460 (8.3)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">SDI score</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Q1 (most affluent)</td>
<td style="text-align: left;">10,083 (21.0)</td>
<td style="text-align: left;">789 (19.3)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">7598 (19.0)</td>
<td style="text-align: left;">10,977 (20.5)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Q2–Q4</td>
<td style="text-align: left;">28,854 (60.2)</td>
<td style="text-align: left;">2360 (57.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">23,829 (59.6)</td>
<td style="text-align: left;">32,003 (59.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Q5 (least affluent)</td>
<td style="text-align: left;">8977 (18.7)</td>
<td style="text-align: left;">937 (22.9)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">8562 (21.4)</td>
<td style="text-align: left;">10,479 (19.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Race and ethnicity</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.016</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.001</td>
</tr>
<tr>
<td style="text-align: left;"> White</td>
<td style="text-align: left;">45,255 (94.5)</td>
<td style="text-align: left;">3832 (93.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">36,592 (91.5)</td>
<td style="text-align: left;">49,276 (92.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Black</td>
<td style="text-align: left;">1878 (3.9)</td>
<td style="text-align: left;">163 (4.0)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2040 (5.1)</td>
<td style="text-align: left;">2461 (4.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Asian, Hispanic, North American native, other</td>
<td style="text-align: left;">781 (1.6)</td>
<td style="text-align: left;">91 (2.2)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1357 (3.4)</td>
<td style="text-align: left;">1722 (3.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Year of surgery</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2013</td>
<td style="text-align: left;">4566 (9.5)</td>
<td style="text-align: left;">341 (8.3)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4673 (11.7)</td>
<td style="text-align: left;">5454 (10.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2014</td>
<td style="text-align: left;">4690 (9.8)</td>
<td style="text-align: left;">384 (9.4)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4976 (12.4)</td>
<td style="text-align: left;">4994 (9.3)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2015</td>
<td style="text-align: left;">5396 (11.3)</td>
<td style="text-align: left;">361 (8.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">5236 (13.1)</td>
<td style="text-align: left;">5219 (9.8)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2016</td>
<td style="text-align: left;">5748 (12.0)</td>
<td style="text-align: left;">378 (9.3)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">5576 (13.9)</td>
<td style="text-align: left;">5941 (11.1)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2017</td>
<td style="text-align: left;">5884 (12.3)</td>
<td style="text-align: left;">464 (11.4)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4946 (12.4)</td>
<td style="text-align: left;">6787 (12.7)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2018</td>
<td style="text-align: left;">6029 (12.6)</td>
<td style="text-align: left;">547 (13.4)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4565 (11.4)</td>
<td style="text-align: left;">7165 (13.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2019</td>
<td style="text-align: left;">6218 (13.0)</td>
<td style="text-align: left;">620 (15.2)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4446 (11.1)</td>
<td style="text-align: left;">7424 (13.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2020</td>
<td style="text-align: left;">5334 (11.1)</td>
<td style="text-align: left;">519 (12.7)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3202 (8.0)</td>
<td style="text-align: left;">5730 (10.7)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 2021</td>
<td style="text-align: left;">4049 (8.5)</td>
<td style="text-align: left;">472 (11.6)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2369 (5.9)</td>
<td style="text-align: left;">4745 (8.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Hospital characteristics</td>
</tr>
<tr>
<td style="text-align: left;"> Hospital beds</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">  0–150</td>
<td style="text-align: left;">14,627 (30.5)</td>
<td style="text-align: left;">1230 (30.1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">10,815 (27.0)</td>
<td style="text-align: left;">15,629 (29.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  150–499</td>
<td style="text-align: left;">25,639 (53.5)</td>
<td style="text-align: left;">2086 (51.1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">21,867 (54.7)</td>
<td style="text-align: left;">27,345 (51.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">  ≥500</td>
<td style="text-align: left;">7648 (16.0)</td>
<td style="text-align: left;">770 (18.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">7307 (18.3)</td>
<td style="text-align: left;">10,485 (19.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Hospital ownership</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.024</td>
</tr>
<tr>
<td style="text-align: left;"> Government</td>
<td style="text-align: left;">4950 (10.3)</td>
<td style="text-align: left;">521 (12.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4274 (10.7)</td>
<td style="text-align: left;">5568 (10.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Physician/proprietary</td>
<td style="text-align: left;">7499 (15.7)</td>
<td style="text-align: left;">976 (23.9)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">7349 (18.4)</td>
<td style="text-align: left;">10,179 (19.0)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Voluntary</td>
<td style="text-align: left;">35,465 (74.0)</td>
<td style="text-align: left;">2589 (63.4)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">28,366 (70.9)</td>
<td style="text-align: left;">37,712 (70.5)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Region</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> Northeast</td>
<td style="text-align: left;">9098 (19.0)</td>
<td style="text-align: left;">539 (13.2)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">6334 (15.8)</td>
<td style="text-align: left;">8954 (16.7)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> South</td>
<td style="text-align: left;">17,649 (36.8)</td>
<td style="text-align: left;">1505 (36.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">16,671 (41.7)</td>
<td style="text-align: left;">20,975 (39.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Midwest</td>
<td style="text-align: left;">11,561 (24.1)</td>
<td style="text-align: left;">1230 (30.1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9512 (23.8)</td>
<td style="text-align: left;">13,932 (26.1)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> West</td>
<td style="text-align: left;">9606 (20.0)</td>
<td style="text-align: left;">812 (19.9)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">7472 (18.7)</td>
<td style="text-align: left;">9598 (18.0)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Rurality</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> Large urban</td>
<td style="text-align: left;">23,333 (48.7)</td>
<td style="text-align: left;">2294 (56.1)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">17,409 (43.5)</td>
<td style="text-align: left;">25,815 (48.3)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Small urban</td>
<td style="text-align: left;">20,681 (43.2)</td>
<td style="text-align: left;">1457 (35.7)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">18,405 (46.0)</td>
<td style="text-align: left;">22,799 (42.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Rural</td>
<td style="text-align: left;">3900 (8.1)</td>
<td style="text-align: left;">335 (8.2)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4175 (10.4)</td>
<td style="text-align: left;">4845 (9.1)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Resident-to-bed ratio</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">.249</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> No teaching</td>
<td style="text-align: left;">30,173 (63.0)</td>
<td style="text-align: left;">2525 (61.8)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">26,866 (67.2)</td>
<td style="text-align: left;">36,093 (67.5)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Minor teaching</td>
<td style="text-align: left;">10,861 (22.7)</td>
<td style="text-align: left;">941 (23.0)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9139 (22.9)</td>
<td style="text-align: left;">11,035 (20.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Major teaching</td>
<td style="text-align: left;">6880 (14.4)</td>
<td style="text-align: left;">620 (15.2)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3984 (10.0)</td>
<td style="text-align: left;">6331 (11.8)</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

Values are presented as n (%). *P*-values indicate differences between PNB and no PNB patients.

Abbreviations: PNB, peripheral nerve block; SDI, Social Deprivation Index.

</div>

<div id="T2" class="table-wrap">

<div class="caption">

Mixed-Effects Logistic Regression Models of Patient and Hospital Variables on the Use of PNBs

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Total hip arthroplasty</th>
<th colspan="2" style="text-align: left;">Total knee arthroplasty</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">OR (95% CI)</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">OR (95% CI)</th>
<th style="text-align: left;"><em>P</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">0.21 (0.10–0.43)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">6.92 (4.57–10.46)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Age</td>
</tr>
<tr>
<td style="text-align: left;"> 65–69</td>
<td style="text-align: left;">0.97 (0.86–1.10)</td>
<td style="text-align: left;">.644</td>
<td style="text-align: left;">0.84 (0.80–0.88)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 70–74</td>
<td style="text-align: left;">0.91 (0.82–1.02)</td>
<td style="text-align: left;">.109</td>
<td style="text-align: left;">0.90 (0.86–0.94)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 75–79</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 80–84</td>
<td style="text-align: left;">0.86 (0.75–0.98)</td>
<td style="text-align: left;">.027</td>
<td style="text-align: left;">0.97 (0.91–1.02)</td>
<td style="text-align: left;">.246</td>
</tr>
<tr>
<td style="text-align: left;"> &gt;84</td>
<td style="text-align: left;">0.84 (0.72–0.99)</td>
<td style="text-align: left;">.038</td>
<td style="text-align: left;">0.81 (0.75–0.88)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">1.02 (0.93–1.11)</td>
<td style="text-align: left;">.724</td>
<td style="text-align: left;">0.95 (0.92–0.99)</td>
<td style="text-align: left;">.008</td>
</tr>
<tr>
<td style="text-align: left;">Inpatient (vs outpatient)</td>
<td style="text-align: left;">1.28 (1.07–1.53)</td>
<td style="text-align: left;">.007</td>
<td style="text-align: left;">0.71 (0.67–0.76)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Diagnosis nonosteoarthritis</td>
<td style="text-align: left;">0.64 (0.58–0.72)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.35 (0.34–0.37)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Prior hospitalizations</td>
</tr>
<tr>
<td style="text-align: left;"> 0</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">0.97 (0.86–1.10)</td>
<td style="text-align: left;">.653</td>
<td style="text-align: left;">0.97 (0.92–1.03)</td>
<td style="text-align: left;">.328</td>
</tr>
<tr>
<td style="text-align: left;"> ≥2</td>
<td style="text-align: left;">0.72 (0.57–0.90)</td>
<td style="text-align: left;">.004</td>
<td style="text-align: left;">0.76 (0.68–0.84)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Deyo index</td>
</tr>
<tr>
<td style="text-align: left;"> 0 (healthiest)</td>
<td style="text-align: left;">0.96 (0.86–1.08)</td>
<td style="text-align: left;">.525</td>
<td style="text-align: left;">0.95 (0.90–0.99)</td>
<td style="text-align: left;">.019</td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">1.00 (0.88–1.12)</td>
<td style="text-align: left;">.953</td>
<td style="text-align: left;">1.01 (0.96–1.06)</td>
<td style="text-align: left;">.705</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: left;">0.93 (0.81–1.06)</td>
<td style="text-align: left;">.249</td>
<td style="text-align: left;">0.96 (0.91–1.02)</td>
<td style="text-align: left;">.178</td>
</tr>
<tr>
<td style="text-align: left;"> ≥3 (least healthy)</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">No obesity</td>
<td style="text-align: left;">1.01 (0.91–1.11)</td>
<td style="text-align: left;">.868</td>
<td style="text-align: left;">0.98 (0.95–1.02)</td>
<td style="text-align: left;">.344</td>
</tr>
<tr>
<td style="text-align: left;">No abuse of nonopioids</td>
<td style="text-align: left;">0.96 (0.81–1.14)</td>
<td style="text-align: left;">.654</td>
<td style="text-align: left;">0.98 (0.89–1.07)</td>
<td style="text-align: left;">.595</td>
</tr>
<tr>
<td style="text-align: left;">No abuse of opioids</td>
<td style="text-align: left;">0.58 (0.40–0.84)</td>
<td style="text-align: left;">.004</td>
<td style="text-align: left;">1.04 (0.85–1.28)</td>
<td style="text-align: left;">.671</td>
</tr>
<tr>
<td style="text-align: left;">No smoking</td>
<td style="text-align: left;">1.07 (0.92–1.25)</td>
<td style="text-align: left;">.380</td>
<td style="text-align: left;">0.88 (0.83–0.94)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">SDI score</td>
</tr>
<tr>
<td style="text-align: left;">Q1 (most affluent)</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Q2–Q4</td>
<td style="text-align: left;">0.94 (0.82–1.07)</td>
<td style="text-align: left;">.328</td>
<td style="text-align: left;">1.00 (0.95–1.06)</td>
<td style="text-align: left;">.942</td>
</tr>
<tr>
<td style="text-align: left;">Q5 (least affluent)</td>
<td style="text-align: left;">0.98 (0.83–1.16)</td>
<td style="text-align: left;">.842</td>
<td style="text-align: left;">0.96 (0.89–1.03)</td>
<td style="text-align: left;">.248</td>
</tr>
<tr>
<td style="text-align: left;">Race and ethnicity</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> White</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Black</td>
<td style="text-align: left;">0.95 (0.76–1.17)</td>
<td style="text-align: left;">.620</td>
<td style="text-align: left;">0.91 (0.84–0.99)</td>
<td style="text-align: left;">.029</td>
</tr>
<tr>
<td style="text-align: left;"> Asian, Hispanic, North American Native, other</td>
<td style="text-align: left;">1.18 (0.87–1.59)</td>
<td style="text-align: left;">.285</td>
<td style="text-align: left;">0.94 (0.85–1.04)</td>
<td style="text-align: left;">.213</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Year of surgery</td>
</tr>
<tr>
<td style="text-align: left;"> 2013</td>
<td style="text-align: left;">0.49 (0.39–0.60)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.83 (0.76–0.91)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2014</td>
<td style="text-align: left;">0.53 (0.43–0.65)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.62 (0.56–0.68)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2015</td>
<td style="text-align: left;">0.42 (0.34–0.52)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.55 (0.50–0.60)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2016</td>
<td style="text-align: left;">0.34 (0.28–0.42)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.47 (0.43–0.51)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2017</td>
<td style="text-align: left;">0.44 (0.36–0.54)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.68 (0.63–0.75)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2018</td>
<td style="text-align: left;">0.52 (0.43–0.63)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.80 (0.74–0.87)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2019</td>
<td style="text-align: left;">0.64 (0.53–0.77)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.85 (0.79–0.93)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2020</td>
<td style="text-align: left;">0.67 (0.56–0.79)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.91 (0.83–0.99)</td>
<td style="text-align: left;">.024</td>
</tr>
<tr>
<td style="text-align: left;"> 2021</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Hospital beds</td>
</tr>
<tr>
<td style="text-align: left;"> ≥500</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 150–499</td>
<td style="text-align: left;">0.82 (0.60–1.13)</td>
<td style="text-align: left;">.219</td>
<td style="text-align: left;">0.85 (0.70–1.02)</td>
<td style="text-align: left;">.075</td>
</tr>
<tr>
<td style="text-align: left;"> 0–150</td>
<td style="text-align: left;">1.08 (0.73–1.61)</td>
<td style="text-align: left;">.696</td>
<td style="text-align: left;">0.98 (0.79–1.23)</td>
<td style="text-align: left;">.876</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Hospital ownership</td>
</tr>
<tr>
<td style="text-align: left;"> Government</td>
<td style="text-align: left;">0.71 (0.45–1.13)</td>
<td style="text-align: left;">.152</td>
<td style="text-align: left;">0.94 (0.72–1.23)</td>
<td style="text-align: left;">.661</td>
</tr>
<tr>
<td style="text-align: left;"> Physician/proprietary</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Voluntary</td>
<td style="text-align: left;">0.51 (0.36–0.71)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">1.03 (0.85–1.26)</td>
<td style="text-align: left;">.732</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Region</td>
</tr>
<tr>
<td style="text-align: left;"> Northeast</td>
<td style="text-align: left;">0.40 (0.26–0.62)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.74 (0.58–0.94)</td>
<td style="text-align: left;">.012</td>
</tr>
<tr>
<td style="text-align: left;"> South</td>
<td style="text-align: left;">0.87 (0.62–1.23)</td>
<td style="text-align: left;">.422</td>
<td style="text-align: left;">0.74 (0.61–0.90)</td>
<td style="text-align: left;">.003</td>
</tr>
<tr>
<td style="text-align: left;"> Midwest</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> West</td>
<td style="text-align: left;">1.09 (0.73–1.60)</td>
<td style="text-align: left;">.682</td>
<td style="text-align: left;">0.71 (0.56–0.89)</td>
<td style="text-align: left;">.003</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Rurality</td>
</tr>
<tr>
<td style="text-align: left;"> Large urban</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Small urban</td>
<td style="text-align: left;">0.54 (0.40–0.72)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.80 (0.67–0.94)</td>
<td style="text-align: left;">.007</td>
</tr>
<tr>
<td style="text-align: left;"> Rural</td>
<td style="text-align: left;">0.74 (0.49–1.12)</td>
<td style="text-align: left;">.159</td>
<td style="text-align: left;">0.50 (0.40–0.63)</td>
<td style="text-align: left;">&lt;.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Resident-to-bed ratio</td>
</tr>
<tr>
<td style="text-align: left;"> No teaching</td>
<td style="text-align: left;">0.55 (0.35–0.86)</td>
<td style="text-align: left;">.010</td>
<td style="text-align: left;">0.96 (0.73–1.26)</td>
<td style="text-align: left;">.780</td>
</tr>
<tr>
<td style="text-align: left;"> Minor teaching</td>
<td style="text-align: left;">0.62 (0.37–1.04)</td>
<td style="text-align: left;">.071</td>
<td style="text-align: left;">0.84 (0.62–1.15)</td>
<td style="text-align: left;">.282</td>
</tr>
<tr>
<td style="text-align: left;"> Major teaching</td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Ref</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">C-statistic</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.87</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">ICC</td>
<td style="text-align: left;">0.67</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

A random intercept was included for the hospital. Reference categories are those with the highest number of PNBs as observed in the univariable analysis. This is not always the same for hip and knee arthroplasty patients; we opted to choose the same reference category in those instances for comprehensibility. The c-statistic measured the overall model performance, and the ICC depicted the variance explained by the random intercept for the hospital.

Abbreviations: CI, confidence interval; ICC, intraclass correlation coefficient; OR, odds ratio; PNB, peripheral nerve block; SDI, Social Deprivation Index.

</div>

### Association of Patient and Hospital Variables with Utilization of PNBs

#### THA

After adjustment, race/ethnicity and SDI did not significantly influence the utilization of PNBs. Lower odds for PNBs were seen for diagnoses other than osteoarthritis (OR, 0.64 \[95% CI, 0.58–0.72\]) and ≥2 prior hospitalizations (OR, 0.72 \[95% CI, 0.57–0.90\]). Contrary to the unadjusted analysis, an inpatient (vs outpatient) setting showed higher odds for PNB use (OR, 1.28 \[95% CI, 1.07–1.53\]). Stronger effect estimates were observed for hospital-level variables: voluntary (OR, 0.51 \[95% CI, 0.36–0.71\]) and government-owned hospitals (OR, 0.71 \[95% CI, 0.45–0.13\]) showed lower odds for receiving PNBs compared to physician/proprietary-owned hospitals. Patients undergoing surgery in nonteaching hospitals also had lower odds of receiving a PNB (OR, 0.55 \[95% CI, 0.35–0.86\]). Regional differences were substantial: patients inhabiting the West and Midwest had higher odds of receiving PNBs, as had large urban hospitals.

#### TKA

SDI did not significantly affect PNB utilization, while Black (compared to White) patients had slightly lower odds (OR, 0.91 \[95% CI, 0.84–0.99\]). The inpatient setting showed lower odds for PNB use (OR, 0.71 \[95% CI, 0.67–0.76\]). Similar to THA patients, diagnoses other than osteoarthritis (OR, 0.35 \[95% CI, 0.33–0.37\]) and ≥2 prior hospitalizations (OR, 0.76 \[95% CI, 0.68–0.84\]) were associated with lower odds of receiving PNBs. Regarding hospital variables, only region and rurality reached significance, of which associations aligned with THA results.

### Population Attributable Risks for Utilization of PNB

The highest univariable PAR of patient variables was that of having a diagnosis other than osteoarthritis (Table <a href="#T3" data-ref-type="table">3</a>). In other words, if all THAs and TKAs were theoretically done for only nonosteoarthritis indications, this would result in 19% and 24% lower PNB utilization, respectively. In THA, the outpatient setting (13%) and ≥2 prior hospitalizations (18%) also played a large role. In THA, and to a lesser extent in TKA patients, hospital variables had high univariable PARs. In THA the largest PAR was observed for the region (38%), rurality (20%), and hospital ownership (10%). In TKA, these were rurality (14%), region (3%), and teaching status (3%).

<div id="T3" class="table-wrap">

<div class="caption">

Population Attributable Risks for the Utilization of PNBs

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Total hip arthroplasty</th>
<th colspan="3" style="text-align: left;">Total knee arthroplasty</th>
</tr>
<tr>
<th style="text-align: left;">Variable</th>
<th style="text-align: left;">Worst category</th>
<th style="text-align: left;">Predicted PNBs</th>
<th style="text-align: left;">Percentage</th>
<th style="text-align: left;">Worst category</th>
<th style="text-align: left;">Predicted PNBs</th>
<th style="text-align: left;">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Predicted blocks<br />
(unadjusted variables)<a href="#tab3fn3" data-ref-type="table-fn"><sup>a</sup></a></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3903</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">53,465</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Univariable PAR</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Demographics</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;">&gt;84</td>
<td style="text-align: left;">3671</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">&gt;84</td>
<td style="text-align: left;">51,849</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"> Sex</td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">3880</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">53,219</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Clinical</td>
</tr>
<tr>
<td style="text-align: left;"> Inpatient (vs outpatient)</td>
<td style="text-align: left;">Outpatient</td>
<td style="text-align: left;">3395</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">Inpatient</td>
<td style="text-align: left;">52,788</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;"> Diagnosis</td>
<td style="text-align: left;">Nonosteoarthritis</td>
<td style="text-align: left;">3151</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">Nonosteoarthritis</td>
<td style="text-align: left;">40,732</td>
<td style="text-align: left;">24</td>
</tr>
<tr>
<td style="text-align: left;"> Prior hospitalizations</td>
<td style="text-align: left;">≥2</td>
<td style="text-align: left;">3194</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">≥2</td>
<td style="text-align: left;">49,598</td>
<td style="text-align: left;">7</td>
</tr>
<tr>
<td style="text-align: left;"> Deyo index</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">3783</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">53,006</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;"> Obesity</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3908</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">53,383</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Abuse of nonopioids</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3897</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">53,452</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Abuse of opioids</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3888</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">53,469</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Smoking</td>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">3758</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">53,298</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Socioeconomic</td>
</tr>
<tr>
<td style="text-align: left;"> SDI score</td>
<td style="text-align: left;">Q2–Q4 (medium)</td>
<td style="text-align: left;">3847</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">Q5 (worst)</td>
<td style="text-align: left;">52,968</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;"> Race and ethnicity</td>
<td style="text-align: left;">Black</td>
<td style="text-align: left;">3771</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">Black</td>
<td style="text-align: left;">52,266</td>
<td style="text-align: left;">2</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Hospital variables</td>
</tr>
<tr>
<td style="text-align: left;"> Hospital beds</td>
<td style="text-align: left;">150–500</td>
<td style="text-align: left;">3647</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">150–500</td>
<td style="text-align: left;">52,394</td>
<td style="text-align: left;">2</td>
</tr>
<tr>
<td style="text-align: left;"> Hospital ownership</td>
<td style="text-align: left;">Voluntary</td>
<td style="text-align: left;">3498</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Government</td>
<td style="text-align: left;">52,343</td>
<td style="text-align: left;">2</td>
</tr>
<tr>
<td style="text-align: left;"> Region</td>
<td style="text-align: left;">Northeast</td>
<td style="text-align: left;">2422</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">West</td>
<td style="text-align: left;">51,821</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"> Rurality</td>
<td style="text-align: left;">Small urban</td>
<td style="text-align: left;">3131</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">Rural</td>
<td style="text-align: left;">45,779</td>
<td style="text-align: left;">14</td>
</tr>
<tr>
<td style="text-align: left;"> Resident-to-bed ratio</td>
<td style="text-align: left;">No teaching</td>
<td style="text-align: left;">3627</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">Minor teaching</td>
<td style="text-align: left;">51,923</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Sequential PARs</td>
</tr>
<tr>
<td style="text-align: left;"> Demographics</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3649</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">51,600</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"> Clinical</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1842</td>
<td style="text-align: left;">46</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">33,306</td>
<td style="text-align: left;">34</td>
</tr>
<tr>
<td style="text-align: left;"> SES</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1736</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">31,578</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"> Hospital variables</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">520</td>
<td style="text-align: left;">31</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">19,615</td>
<td style="text-align: left;">22</td>
</tr>
<tr>
<td style="text-align: left;"> Total</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">87</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">62</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Sequential PARs; reverse order</td>
</tr>
<tr>
<td style="text-align: left;"> Hospital variables</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1386</td>
<td style="text-align: left;">64</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">40,170</td>
<td style="text-align: left;">25</td>
</tr>
<tr>
<td style="text-align: left;"> SES</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1304</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">38,410</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"> Clinical</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">571</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">21,175</td>
<td style="text-align: left;">32</td>
</tr>
<tr>
<td style="text-align: left;"> Demographics</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">520</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">19,615</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"> Total</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">86</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">63</td>
</tr>
</tbody>
</table>

Predicted blocks and respective PARs reflect the number of PNBs utilized if a variable is set to the worst category. In other words, the PAR reflects how much PNBs are attributable to that variable, when all other variables are kept constant. We used a mixed-effects logistic regression model to calculate the PARs with a random intercept for the hospital.

Abbreviations: PAR, population attributable risk; PNB, peripheral nerve block; SDI, Social Deprivation Index; SES, socioeconomic status; THA, total hip arthroplasty.

The predicted number of PNBs in the THA cohort does not entirely match the observed number of PNBs (4086), while it is close for the total knee arthroplasty cohort (53,459). This is presumably due to the relatively lower incidence of PNBs applied in the THA cohort, resulting in a slightly poorer predictive capability of the model.

</div>

The sequential PARs visualization provided the cumulative proportion of PNBs which could be explained by the regression model.<sup>9</sup> All variables combined explained a considerably higher percentage of PNBs in THA (87%) compared to in TKA patients (63%). Starting with demographics and ending with hospital variables, in THA, the largest contributing factors were clinical (46%), followed by hospital (31%), demographic (7%), and socioeconomic variables (3%). In TKA, the largest contributors were also clinical (34%), followed by hospital (22%), demographic (3%) and socioeconomic variables (3%). If the order of the groups of variables was reversed (starting with the hospital), hospital variables explained a larger proportion in THA, but not in TKA (THA: 64%, TKA: 25%). The effect of clinical variables reduced in THA (19%) which illustrates the statistical interrelatedness of hospital and clinical variables.

### Association of PNBs with Secondary Outcomes

In THA, use of PNB did not significantly relate to CMS-defined complications (OR, 0.92 \[95% CI, 0.78–1.10\]), 90-day all-cause readmission (OR, 0.98 \[95% CI, 0.87–1.10\]) nor a length of stay \>3 days (OR, 0.99 \[95% CI, 0.89–1.11\]; Table <a href="#T4" data-ref-type="table">4</a>). In TKA, use of PNBs was significantly associated with a reduction in CMS-defined complications (OR, 0.82 \[95% CI, 0.75–0.90\]) and length of stay \>3 days (OR, 0.90 \[95% CI, 0.86–0.95\]), however, no benefit was found on 90-day all-cause readmissions (OR, 0.98 \[95% CI, 0.93–1.03\]). The full models with adjustment factors can be found in Supplemental Digital Content 4, Supplemental Tables 3–8, <http://links.lww.com/AA/E914>.

<div id="T4" class="table-wrap">

<div class="caption">

Mixed-Effects Logistic Regression Models of PNBs on Outcomes

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">Total hip arthroplasty</th>
<th colspan="3" style="text-align: left;">Total knee arthroplasty</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">OR (95% CI)</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">C-statistic</th>
<th style="text-align: left;">ICC</th>
<th colspan="2" style="text-align: left;">OR (95% CI)</th>
<th style="text-align: left;"><em>P</em>-value</th>
<th style="text-align: left;">C-statistic</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">CMS complications</td>
<td style="text-align: left;">0.92 (0.78–1.10)</td>
<td style="text-align: left;">.357</td>
<td style="text-align: left;">0.71</td>
<td style="text-align: left;">0.04</td>
<td colspan="2" style="text-align: left;">0.82 (0.75–0.90)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.70</td>
</tr>
<tr>
<td style="text-align: left;">90-day all-cause readmissions</td>
<td style="text-align: left;">0.98 (0.87–1.10)</td>
<td style="text-align: left;">.738</td>
<td style="text-align: left;">0.67</td>
<td style="text-align: left;">0.01</td>
<td colspan="2" style="text-align: left;">0.98 (0.93–1.03)</td>
<td style="text-align: left;">.380</td>
<td style="text-align: left;">0.67</td>
</tr>
<tr>
<td style="text-align: left;">Length of stay &gt;3 d</td>
<td style="text-align: left;">0.99 (0.89–1.11)</td>
<td style="text-align: left;">.904</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">0.13</td>
<td colspan="2" style="text-align: left;">0.90 (0.86–0.95)</td>
<td style="text-align: left;">&lt;.001</td>
<td style="text-align: left;">0.78</td>
</tr>
</tbody>
</table>

The OR reflects the use of PNBs versus no PNB. The same set of variables that were used in the analysis of the utilization of PNBs was entered as fixed effects. A random effect for the hospital is included in the models. Length of stay is only analyzed in patients who had inpatient surgery (approximately 90% of patients). The c-statistic measures the overall model performance, and the ICC depicts the variance explained by the random intercept for the hospital.

Abbreviations: CI, confidence interval; ICC, intraclass correlation coefficient; OR, odds ratio; PNB, peripheral nerve block; CMS, Centers for Medicare & Medicaid Services.

</div>

### Model Performance

The mixed-effects regression models on PNB utilization produced high c-statistics (THA: 0.94, TKA: 0.86) and ICCs (THA: 0.67, TKA: 0.49; Table <a href="#T2" data-ref-type="table">2</a>). The models for the secondary outcomes had lower c-statistics, varying from 0.66 to 0.82 in both THA and TKA (Table <a href="#T4" data-ref-type="table">4</a>). ICCs were also lower, ranging from 0.02 to 0.16.

### Sensitivity Analysis

The addition of state-county ID as a random effect had no improvement on model fit, and estimates of SDI did not change (Supplemental Digital Content 4, Supplemental Tables 9–10, <http://links.lww.com/AA/E914>). In other words, we did not find evidence of variation in PNB use by county of residence beyond the SDI measure used. The inclusion of dual eligibility had no effect on PNB utilization (Supplemental Digital Content 4, Supplemental Table 11, <http://links.lww.com/AA/E914>), nor did multivariable estimates of outcomes change substantially (Supplemental Digital Content 4, Supplemental Tables 3–8, <http://links.lww.com/AA/E914>).

## DISCUSSION

### Main Findings

To the best of our knowledge, this is the first study to determine patterns of use and effectiveness of PNBs in THA and TKA patients using Medicare data. Contrary to our expectations, socioeconomic background (PAR: THA: 2%–3%, TKA: 3%) played a minor role in the observed variation in PNB utilization. Most variation was explained by clinical (THA: 19%–46%, TKA: 32%–34%) and hospital variables (THA: 31%–64%, TKA: 22%–25%). The PAR for clinical variables was driven by the decreased use of PNBs in patients with a nonosteoarthritis diagnosis, and in THA also by decreased use in the outpatient setting and patients with prior hospitalizations. In all, statistical relations in TKA echo those in THA, but the relative role of hospital-related effects is larger in THA. These findings illustrate that the strongest driving force behind disparities in the utilization of PNBs is based on practice differences (provider based) in semi- and nonelective arthroplasty patients.

Our study adds to the extensive evidence base<sup>1,2</sup> that the use of PNB is associated with improved clinical outcome: in TKA patients, we found fewer complications and length of stay; differences in THA patients did not reach statistical significance.

### Comparison with Other Literature

Previous studies examined the impact of patient and hospital variables on the utilization of PNBs through standard regression techniques, which provide insufficient insight into the strength of the association. The PAR method used in this paper had additional value in this regard. Overall, our study found no clear evidence of disparities according to socioeconomic (SDI, race and ethnicity, and dual eligibility) variables. This finding diverges from a study by Keneally et al,<sup>6</sup> which used ZIP-code-linked median income as SES indicator and found a higher income to significantly relate to increased utilization of PNBs in TKA. A reason for this discrepancy may be because our study applied a different comprehensive type of neighborhood SES indicator and at a different level of linkage. However, as we did not observe variation in PNB utilization according to the county of residence, it is unlikely variation by neighborhood indicators will be found in the current dataset. In TKA a weak association suggested Black patients (compared to White) received fewer PNBs. We do not believe this is strong evidence of an association, as the PAR analysis did not show substantial variation by race/ethnicity and this may also be the result of a type I error. In comparison, a recent study by Zhong et al<sup>8</sup> used a private insurance database and found nonwhite compared to White TKA patients receiving PNBs less often. The contrasting findings highlight that the effect of socioeconomic variables also may differ by the studied population and type of health coverage, that is, private versus public.

PNB utilization was less in patients receiving THA and TKA for nonosteoarthritis indications. Fracture patients typically present in a nonelective setting which could limit the timely administration of PNBs. However, nonosteoarthritis indications for THA/TKA will also include a variety of (semi-)elective diagnoses such as posttraumatic osteoarthritis, osteonecrosis, and rheumatoid arthritis.<sup>32,33</sup> Especially in TKA in which the number of fracture patients is relatively small, there is a large group of (semi-)elective patients in whom the abovementioned explanation may not suffice. Additionally, in THA patients with prior hospitalizations PNBs were used less often, which highlights another potential explanation for differential use: comorbid and/or semielective patients may fall outside of protocolized care pathways with as a consequence less use of PNBs.

Regional practice variations explained a large part of the variation in PNB use. In both THA and TKA patients, the Midwest region and urban hospitals are associated with increased utilization of PNBs. Strengthening the assertion that PNB utilization is largely determined by practice variations was that the addition of a random intercept for the hospital (which covers unspecified hospital effects) drastically improved model fit. Practice variations may indirectly lead to variations in use by socioeconomic or clinical variables, or vice versa. For example, different PNB utilization profiles may drive socioeconomic disparities in the background, because certain regions are inhabited by relatively less affluent and/or more Black patients, such as the South.<sup>34,35</sup> This effect is probably limited, as we did not observe the interrelatedness of socioeconomic and hospital-related variables in the PAR analysis. Clinical and hospital-related variables, however, were statistically interrelated in THA patients, as the role of clinical variables reduced markedly after first accounting for hospital variables. In other words, particular patients (ie, comorbid/nonosteoarthritis) treated in hospitals/regions as reflected by the hospital-related variables received PNBs less often. We currently cannot determine the directionality of this effect. We think that survey data with targeted questions on barriers for use of PNBs per hospital/specialist group could provide valuable insights.<sup>36</sup> This may also reveal if the overall socioeconomic or clinical profile of patients presenting at hospitals in certain regions affects PNB utilization at the policy level.

We expect the practitioners’ choice (surgeon or anesthesiologist) plays a key role in explaining these regional variations, which in turn largely depends on the training received and the experienced comfort with PNB utilization.<sup>4</sup> For example, one study found that PNBs were applied more often in TKA patients when a board-certified anesthesiologist was present.<sup>35</sup> In a study on the utilization of regional anesthesia for acute pain management among military anesthesiology residents and specialists, a potential barrier to apply PNBs was the lack of opportunities to practice during traing.<sup>37</sup> The practice environment may differ largely by regions, and specific hospitals (urban, teaching) may have increased opportunities to practice PNB utilization for residents.

Diverging patterns between THA and TKA patients were observed with regard to hospital ownership: THA patients undergoing surgery in physician/proprietary (for-profit) hospitals had higher odds of receiving a PNB compared to voluntary or government (nonprofit) hospitals, while this was not the case in TKA patients. For-profit hospitals have different incentives and resources available compared to nonprofit hospitals. which may result in increased (earlier) adaptation of novel treatments with a slimmer evidence base.<sup>38</sup> Supporting this notion is the fact that overall uptake of PNBs is far less in THA compared to TKA (8% vs 57%, respectively).

### Strengths and Limitations

This study has some limitations. Due to the observational nature of this study, we can only assess associations and not causal relations. Moreover, it is possible that potential confounders in the studied association were missed; in this scenario, currently observed associations may be overestimated. At the hospital level, separating ambulatory surgical centers owned by or affiliated with teaching hospitals might have resulted in more detailed insights into the effect of the resident-to-bed ratio. Secondly, our findings are only generalizable to the Medicare population; different patterns may exist for commercially insured patients, a growing group of arthroplasty recipients.<sup>4,8</sup> Thirdly, the area-based social deprivation indicator may not entirely reflect deprivation at the individual level. Finally, PAR estimates represent the maximum attainable reduction in variation of PNB utilization; it is unlikely a change in clinical practice will eliminate all variation.

## CONCLUSIONS

In THA and TKA patients on Medicare, large variations exist in the utilization of PNBs by clinical (eg, indication for arthroplasty) and hospital variables, while demographic and socioeconomic variables played a limited role. These findings emphasize the substantial individual and hospital practice variation in PNB utilization. In light of the potential benefit of PNBs observed in our study and various other studies, we believe stakeholders should strive for more standardized provision of PNBs.

## ACKNOWLEDGMENTS

We would like to acknowledge Dr Brocha Stern for her help with the additional analyses performed during the review phase. Moreover, we would like to acknowledge the reviewers for their valuable and in-depth review of this work.

## DISCLOSURES

**Conflicts of Interest:** None. **Funding:** This work was funded by a travel grant provided by the EuroQol Research Foundation (1483-TVG) and the Erasmus Trustfonds (97030.2022.101.935/292/RB). The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication. **This manuscript was handled by:** Olubukola O. Nafiu, MD, FRCA, MS.

## Supplementary Material

## Footnotes

## REFERENCES

## References

1. Memtsoudis SG, Cozowicz C, Bekeris J, et al. Peripheral nerve block anesthesia/analgesia for patients undergoing primary hip and knee arthroplasty: recommendations from the International Consensus on Anesthesia-Related Outcomes after Surgery (ICAROS) group based on a systematic review and meta-analysis of current literature. Reg Anesth Pain Med. 2021;46:971–985. doi:10.1136/rapm-2021-102750

2. Memtsoudis SG, Cozowicz C, Bekeris J, et al. Anaesthetic care of patients undergoing primary hip and knee arthroplasty: consensus recommendations from the International Consensus on Anaesthesia-Related Outcomes after Surgery group (ICAROS) based on a systematic review and meta-analysis. Br J Anaesth. 2019;123:269–287. doi:10.1016/j.bja.2019.05.042

3. Cozowicz C, Poeran J, Zubizarreta N, Mazumdar M, Memtsoudis SG. Trends in the use of regional anesthesia: neuraxial and peripheral nerve blocks. Reg Anesth Pain Med. 2016;41:43–49. doi:10.1097/AAP.0000000000000342

4. Memtsoudis SG, Poeran J, Zubizarreta N, Rasul R, Opperer M, Mazumdar M. Anesthetic care for orthopedic patients: is there a potential for differences in care? Anesthesiology. 2016;124:608–623. doi:10.1097/ALN.0000000000001004

5. Memtsoudis SG, Danninger T, Rasul R, et al. Inpatient falls after total knee arthroplasty: the role of anesthesia type and peripheral nerve blocks. Anesthesiology. 2014;120:551–563. doi:10.1097/ALN.0000000000000120

6. Keneally RJ, Mazzeffi MA, Chow JH, et al. Socioeconomic disparities in method of anesthesia for knee arthroplasties in the US. J Health Care Poor Underserved. 2022;33:1809–1820. doi:10.1353/hpu.2022.0139

7. Schaar AN, Finneran JJ, Gabriel RA. Association of race and receipt of regional anesthesia for hip fracture surgery. Reg Anesth Pain Med. 2023;48:392–398. doi:10.1136/rapm-2022-104055

8. Zhong H, Poeran J, Liu J, et al. Disparities in the provision of regional anesthesia and analgesia in total joint arthroplasty: the role of patient and hospital level factors. J Clin Anesth. 2021;75:110440. doi:10.1016/j.jclinane.2021.110440

9. Poeran J, Borsboom GJJM, de Graaf JP, Birnie E, Steegers EAP, Bonsel GJ. Population attributable risks of patient, child and organizational risk factors for perinatal mortality in hospital births. Matern Child Health J. 2015;19:764–775. doi:10.1007/s10995-014-1562-4

10. Danninger T, Rasul R, Poeran J, et al. Blood transfusions in total hip and knee arthroplasty: an analysis of outcomes. ScientificWorldJ. 2014;2014:623460. doi:10.1155/2014/623460

11. Centers for Medicare & Medicaid Services. Limited data set (LDS) files. Accessed April 1, 2023. https://www.cms.gov/data-research/files-for-order/limited-data-set-lds-files.

12. von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370:1453–1457. doi:10.1016/S0140-6736(07)61602-X

13. Schwarzkopf R, Behery OA, Yu H, Suter LG, Li L, Horwitz LI. Patterns and costs of 90-day readmission for surgical and medical complications following total hip and knee arthroplasty. J Arthroplasty. 2019;34:2304–2307. doi:10.1016/j.arth.2019.05.046

14. Cozowicz C, Poeran J, Memtsoudis SG. Epidemiology, trends, and disparities in regional anaesthesia for orthopaedic surgery. Br J Anaesth. 2015;115:ii57–ii67. doi:10.1093/bja/aev381

15. Barbera JP, Raymond HE, Zubizarreta N, et al. Racial differences in manipulation under anesthesia rates following total knee arthroplasty. J Arthroplasty. 2022;37:1865–1869. doi:10.1016/j.arth.2022.03.088

16. Charlson ME, Pompei P, Ales KL, MacKenzie CR. A new method of classifying prognostic comorbidity in longitudinal studies: development and validation. J Chronic Dis. 1987;40:373–383. doi:10.1016/0021-9681(87)90171-8

17. Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining comorbidities in ICD-9-CM and ICD-10 administrative data. Med Care. 2005;43:1130–1139. doi:10.1097/01.mlr.0000182534.19832.83

18. Robert Graham Center – Policy Studies in Family Medicine & Primary Care. Social Deprivation Index (SDI), 2019. Accessed May 1, 2023. https://www.graham-center.org/maps-data-tools/social-deprivation-index.html.

19. The World Health Organization. Handbook on health inequality monitoring. Accessed May 1, 2023. https://www.who.int/publications/i/item/9789241548632.

20. Ralston K, Dundas R, Leyland AH. A comparison of the Scottish Index of Multiple Deprivation (SIMD) 2004 with the 2009 + 1 SIMD: does choice of measure affect the interpretation of inequality in mortality? Inter J Health Geograph. 2014;13:27. doi:10.1186/1476-072X-13-27

21. Centers for Medicare & Medicaid Services (CMS). Impact file hospital IPPS, 2017. Accessed May 1, 2023. https://www.nber.org/research/data/centers-medicare-medicaid-services-cms-impact-file-hospital-ipps.

22. Silber JH, Rosenbaum PR, Niknam BA, et al. Comparing outcomes and costs of medical patients treated at major teaching and non-teaching hospitals: a national matched analysis. J Gen Intern Med. 2020;35:743–752. doi:10.1007/s11606-019-05449-x

23. Volpp KG, Rosen AK, Rosenbaum PR, et al. Mortality among hospitalized Medicare beneficiaries in the first 2 years following ACGME resident duty hour reform. JAMA. 2007;298:975–983. doi:10.1001/jama.298.9.975

24. Centers for Medicare & Medicaid Services (CMS). Hip and knee arthroplasty complication measures. Accessed May 1, 2023. https://www.cms.gov/medicare/quality/initiatives/hospital-quality-initiative/measure-methodology.

25. Dormann CF, Elith J, Bacher S, et al. Collinearity: a review of methods to deal with it and a simulation study evaluating their performance. Ecography. 2013;36:27–46.

26. Vatcheva KP, Lee M, McCormick JB, Rahbar MH. Multicollinearity in regression analyses conducted in epidemiologic studies. Epidemiology (Sunnyvale). 2016;6:227. doi:10.4172/2161-1165.1000227

27. Benichou JA. Review of adjusted estimators of attributable risk. Stat Methods Med Res. 2001;10:195–216. doi:10.1177/096228020101000303

28. Eide GE, Gefeller O. Sequential and average attributable fractions as aids in the selection of preventive strategies. J Clin Epidemiol. 1995;48:645–655. doi:10.1016/0895-4356(94)00161-i

29. Gefeller O, Land M, Eide GE. Averaging attributable fractions in the multifactorial situation: assumptions and interpretation. J Clin Epidemiol. 1998;51:437–441. doi:10.1016/s0895-4356(98)00002-x

30. Rowe AK, Powell KE, Flanders WD. Why population attributable fractions can sum to more than one. Am J Prev Med. 2004;26:243–249. doi:10.1016/j.amepre.2003.12.007

31. Thirukumaran CP, Cai X, Glance LG, et al. Geographic variation and disparities in total joint replacement use for Medicare beneficiaries: 2009 to 2017. J Bone Joint Surg Am. 2020;102:2120–2128. doi:10.2106/JBJS.20.00246

32. Adhia AH, Feinglass JM, Suleiman LI. What are the risk factors for 48 or more–hour stay and nonhome discharge after total knee arthroplasty? Results from 151 Illinois hospitals, 2016-2018. J Arthroplasty. 2020;35:1466–1473.e1. doi:10.1016/j.arth.2019.11.043

33. Weiner JA, Adhia AH, Feinglass JM, Suleiman LI. Disparities in hip arthroplasty outcomes: results of a statewide hospital registry from 2016 to 2018. J Arthroplasty. 2020;35:1776–1783.e1. doi:10.1016/j.arth.2020.02.051

34. Andrews MR, Tamura K, Claudel SE, et al. Geospatial analysis of neighborhood deprivation index (NDI) for the United States by county. J Maps. 2020;16:101–112. doi:10.1080/17445647.2020.1750066

35. Fleischut PM, Eskreis-Winkler JM, Gaber-Baylis LK, et al. Variability in anesthetic care for total knee arthroplasty: an analysis from the anesthesia quality institute. Am J Med Qual. 2015;30:172–179. doi:10.1177/1062860614525989

36. Posthumus AG, Borsboom GJ, Poeran J, Steegers EA, Bonsel GJ. Geographical, ethnic and socio-economic differences in utilization of obstetric care in the Netherlands. PLoS One. 2016;11:e0156621. doi:10.1371/journal.pone.0156621

37. Jaffe E, Patzkowski MS, Hodgson JA, et al. Practice variation in regional anesthesia utilization by current and former U.S. military anesthesiology residents. Mil Med. 2021;186:e98–e103. doi:10.1093/milmed/usaa269

38. Horwitz JR. Making profits and providing care: comparing nonprofit, for-profit, and government hospitals. Health Aff (Millwood). 2005;24:790–801. doi:10.1377/hlthaff.24.3.790

## Associated Data

### Supplementary Materials

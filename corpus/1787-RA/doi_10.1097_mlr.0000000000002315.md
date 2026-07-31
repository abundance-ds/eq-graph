---
project_id: "1787-RA"
work_id: "doi:10.1097/mlr.0000000000002315"
doi: "10.1097/MLR.0000000000002315"
pmid: "41861120"
pmcid: "PMC13166071"
title: "Can Patient-Reported Outcome Measures Help Predict Unplanned Hospital Readmission?"
journal: "Medical Care"
publication_date: "2026-03-20"
volume: "64"
issue: "6"
authors:
  - name: "Maggie Yu"
    affiliation_ids:
      - "aff1"
  - name: "Mark Harrison"
    affiliation_ids:
      - "aff2"
  - name: "Hubert Wong"
    affiliation_ids:
      - "aff1"
  - name: "Logan Trenaman"
    affiliation_ids:
      - "aff3"
  - name: "Stirling Bryan"
    affiliation_ids:
      - "aff4"
  - name: "Lisa Lix"
    affiliation_ids:
      - "aff5"
  - name: "Rick Sawatzky"
    affiliation_ids:
      - "aff6"
      - "aff7"
  - name: "Lena Cuthbertson"
    affiliation_ids:
      - "aff7"
  - name: "Fatima Al Sayah"
    affiliation_ids:
      - "aff8"
  - name: "Nick Bansback"
    affiliation_ids:
      - "aff1"
affiliations:
  - id: "aff1"
    name: "School of Population and Public Health, University of British Columbia, Advancing Health Outcomes Research Center, Providence Research, Vancouver, BC, Canada"
  - id: "aff2"
    name: "Faculty of Pharmaceutical Sciences, University of British Columbia, Advancing Health Outcomes Research Center, Providence Research, Vancouver, BC, Canada"
  - id: "aff3"
    name: "Department of Health Systems and Population Health, School of Public Health, University of Washington, Seattle, WA"
  - id: "aff4"
    name: "School of Population and Public Health, University of British Columbia, Center for Clinical Epidemiology and Evaluation, Vancouver Coastal Health Research Institute, Vancouver, BC, Canada"
  - id: "aff5"
    name: "Department of Biostatistics, University of Manitoba, Winnipeg, MA, Canada"
  - id: "aff6"
    name: "School of Nursing, Trinity Western University, Advancing Health Outcomes Research Center, Providence Research, Langley, BC, Canada"
  - id: "aff7"
    name: "British Columbia's Office of Patient-Centred Measurement, Vancouver, BC, Canada"
  - id: "aff8"
    name: "School of Public Health, University of Alberta, Edmonton, AB, Canada"
keywords:
  - "administrative data"
  - "hospital readmission"
  - "patient-reported outcomes"
  - "predictive model"
licence: "cc-by-nc-nd"
source_file: "input/projects/1787-RA/papers/doi_10.1097_mlr.0000000000002315.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13166071/fullTextXML"
source_method: "epmc_xml"
source_sha256: "6450e29301da6d37d3974b1aba432c7594fddff77e353b283e314b2dfd9438f5"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Can Patient-Reported Outcome Measures Help Predict Unplanned Hospital Readmission?

## Abstract

### Background:

Administrative data used to predict unplanned hospital readmissions often lack patient-reported symptoms and functional status. Integrating patient-reported outcome measures (PROMs) may improve risk prediction.

### Objectives:

To assess the incremental value of PROMs in predicting unplanned readmissions to inform postdischarge monitoring and ongoing care management.

### Methods:

This population-based retrospective cohort study used linked administrative and PROMs data from British Columbia, Canada. Adults discharged from acute care who provided response to the EQ-5D-5L and Veterans RAND 12-Item Health Survey (VR-12) within 60 days were included. Aggregated Cox proportional hazards models were fitted to estimate unplanned readmission risk across 30-, 180-, and 360-day horizons. The primary prediction horizons were 30 and 180 days. The 360-day horizon was a secondary focus. Model performance was assessed using the concordance statistics and calibration, with subgroup analysis for Ambulatory Care Sensitive Conditions (ACSC).

### Results:

Among 11,177 individuals, observed unplanned readmission rates within 30, 180, and 360 days of discharge were 5.6%, 18.4%, and 25.0%, respectively. Conditional on surviving to weekly landmarks (23–60 days postdischarge), PROMs modestly improved discrimination. For the 180-day horizon following landmarks, the C-index was 0.762 (95% CI, 0.761–0.763) using predictors from administrative data alone, increasing to 0.774 (95% CI, 0.773–0.774) with EQ-5D-5L and 0.782 (95% CI, 0.781–0.783) with VR-12. Similar gains in discrimination were observed at 30-day and 360-day horizons. All models showed adequate calibration. Among patients with ACSCs, including PROMs improved discrimination by 2.4%–3.0%.

### Conclusions:

PROMs added predictive value for unplanned hospital readmissions, particularly among patients with ACSCs.

Hospital readmissions remain a significant challenge for patients and health systems worldwide,<sup>1,2</sup> indicating both clinical complexity and gaps in care delivery. In Canada, readmissions cost the system over \$2.5 billion annually.<sup>3</sup> In the United States, the Centers for Medicare and Medicaid Services (CMS) financially incentivize hospitals to reduce readmission rates through value-based care programs.<sup>4,5</sup> This evidence suggests a growing emphasis on reducing unnecessary rehospitalizations.

Unplanned readmissions occur unexpectedly within a defined period after discharge. They may result from suboptimal care, exacerbation of existing chronic conditions, or medical error.<sup>6</sup> While not all readmissions are preventable, identifying patients at higher risk can guide postdischarge monitoring and help reduce avoidable use of acute care services.<sup>7</sup>

Several prediction models have been developed to identify patients at elevated risk of readmission. The LACE model, for example, predicts 30-day mortality or readmission based on 4 administrative variables: length of stay (“L”), acuity of admission (“A”), comorbidities (“C”), and emergency department visits (“E”).<sup>8</sup> Later extensions further incorporated demographics, frailty, or hospital factors,<sup>9,10</sup> and parallel models also included contextual factors (eg, neighborhood deprivation).<sup>11</sup> These models are relatively straightforward to implement, as they rely on administrative data readily available to clinical teams at the time of discharge. Many have shown reasonable predictive accuracy in external validations.<sup>12</sup> However, they often overlook information about patients’ physical and mental health status.

Patient-reported outcome measures (PROMs) capture aspects of health-related quality of life—including functional limitations, pain, and emotional well-being—that may not be recorded in administrative data. Prior research has shown that PROMs are associated with health care utilization. For example, Boult et al<sup>13</sup> found that functional decline in community-dwelling adults is linked to hospitalization, and Vámosi et al<sup>14</sup> reported associations between patient-reported anxiety and depression and readmission following heart surgery. Despite such evidence, PROMs are typically absent from administrative data.<sup>11</sup>

Integrating routinely collected PROMs with administrative data may provide a scalable, patient-centered approach to improve readmission risk prediction.<sup>15,16</sup> In this study, we linked population-based routinely collected PROMs to administrative data to predict unplanned readmissions. By comparing model performance with and without PROMs, we sought to investigate their incremental predictive value for 30- and 180-day unplanned readmissions, with the goal of supporting postdischarge monitoring and ongoing care management as patients transitioning from hospital to the community.

## METHODS

The study followed the Transparent Reporting of a Multivariable Prediction Model for Individual Prognosis or Diagnosis (TRIPOD) guidelines.<sup>17</sup>

### Study Design and Data Sources

We conducted a retrospective population-based cohort study using data from respondents to a population-based Acute Inpatient Survey, linked to British Columbia’s (BC) provincial health administrative databases. Data access and linkage were provided by Population Data BC.<sup>18</sup> The inpatient survey was conducted in 2016/17 among individuals discharged from 78 acute care hospitals and 2 freestanding rehabilitation hospitals in BC. Biweekly, hospitals randomly selected patients from a discharge list. Contact letters were mailed within 2 weeks of discharge, inviting patients to complete the survey online or by paper. Instructions were included in the mailed package. Survey responses were received between 16- and 200-day postdischarge, with 90% returned within the first 60 days. The overall response rate was 47%.<sup>19</sup>

The survey collected socio-demographic factors (eg, age, ethnicity, education) and included 2 PROMs—EQ-5D-5L<sup>20</sup> and the Veterans RAND 12-Item Health Survey (VR-12, based on the RAND SF-12)<sup>21,22</sup>—both of which have demonstrated strong reliability, validity, and responsiveness in diverse populations:

- EQ-5D-5L: A health-related quality of life instrument assessing 5 dimensions—mobility, self-care, usual activities, pain/discomfort, and anxiety/depression—each with 5 response levels, ranging from no problems to extreme problems. It also includes a visual analog scale (VAS), where respondents rate their overall health on a scale ranging from 0 (worst imaginable health) to 100 (best imaginable health).

- VR-12: A 12-item questionnaire derived from the Veterans RAND 36-Item Health Survey. It measures 6 physical and mental health domains, including physical functioning, role limitations, pain, general health, energy/fatigue, and emotional well-being. Items use Likert-type scales with 3–6 response categories.

Survey data were linked to administrative databases (April 1, 2014–March 31, 2020), including the National Ambulatory Care Reporting System (NACRS, emergency department, day surgeries, and day clinics), the Discharge Abstract Database (DAD; hospital separations), and the Consolidation Data File (demographics).<sup>15</sup> These data sources provided information on the outcomes and predictors.

### Study Population

Eligible participants were patients discharged from BC’s acute care facilities between April 1, 2016, and March 31, 2017, who subsequently responded to the Acute Inpatient Survey (N=16,318). After applying exclusion criteria, the analytic sample included 11,177 individuals, of whom 6253 had complete data for all predictors (Fig. <a href="#F1" data-ref-type="fig">1</a>).

<figure id="F1">
<p><img src="mlr-64-387-g001.jpg" /></p>
<figcaption>Cohort Flow Chart. DAD: Discharge Abstract Database. NACRS: National Ambulatory Care Reporting System. PROMs: patient-reported outcome measures.</figcaption>
</figure>

### Outcome

The primary outcome was time to the first unplanned readmission, defined as an emergency department (ED) visit or acute care hospital readmission for a nonelective medical condition. Follow-up began at defined time points after discharge (ie, landmarks) and continued until the earliest date of unplanned readmission, death, or administrative censoring (March 31, 2020).

### Predictors

Predictors were identified based on a literature review and data availability.<sup>16</sup> Key administrative variables included patient socio-demographics, prior health care utilization, acuity, and length of stay (LOS) of the index admission. Comorbidities were measured using the Elixhauser Comorbidity Index.<sup>23</sup> We modeled these data as a count of the number of comorbidities identified in the year before the episode of index hospital stay (0, 1, 2, 3, ≥4 comorbidities). LOS was categorized in line with the LACE index.<sup>8</sup>

We considered 3 sets of predictors in the models:

- **Base**: All predictors were derived from administrative data available as of the index date, including patient age (per 10-y increment), sex (male vs. female), neighborhood income decile, number of hospitalizations in the prior year (\>1 vs. ≤1), ED visits in the prior year (\>1 vs. ≤1), LOS (2/3/4-6/7-13/14+ days vs. 1 day), and acuity of the index admission (urgent/emergent vs. elective), and comorbidity count in the prior year (1/2/3/4+ vs. 0).

- **EQ-5D-5L-enhanced**: All predictors in the Base plus EQ-5D-5L dimensions (ordinal) and the VAS (continuous, centered, and scaled).

- **VR-12-enhanced**: All predictors in the Base plus VR-12 dimensions (ordinal).

### Data Preprocessing and Imputation

To improve model convergence and ensure comparability, continuous predictors were standardized. There were no missing values for variables from administrative data. Approximately 5% of PROMs data had missing values, and these were imputed ten times using multiple imputation with chained equations (MICE) under the assumption of missing at random (MAR).<sup>24,25</sup> The imputation model included all candidate predictors and outcomes (event status and time to event) to take account of the potential relationship between missing values and the outcome.<sup>24</sup> Convergence was assessed via trace plots, and the distributions of imputed values were compared with the observed.

### Model Derivation

To reduce immortal time bias and to accommodate variation in the timing of PROMs collection in practice, we used the Cox Landmark Supermodel.<sup>26</sup> This modeling approach fits separate Cox models at prespecified time points (“landmarks”) and aggregates them into a combined “supermodel.”

Landmark times were specified at weekly intervals between days 23 and 60 postdischarge, corresponding to the period of PROMs return. Because the EQ-5D-5L and VR-12 were administered on the same day, they were treated as time-fixed and carried forward across landmark times using the last observation carried forward method.<sup>26</sup> Weekly intervals were chosen to ensure adequate sample size (Supplemental Fig. S1, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). Readmission risk was estimated for 30-, 180-, and 360-day horizons after landmarks. The 30- and 180-day horizons were considered the primary prediction windows because they align with the feasibility of postdischarge monitoring and ongoing care management. The 360-day horizon was retained as a secondary focus to capture longer-term risk.

Participants were included in the risk set at each landmark if they remained event-free and had completed PROMs before each landmark time, and readmission risk was estimated for the subsequent 30, 180, and 360-day predictive windows. Each model included fixed effects for landmark time and covariate-by-landmark interaction terms to allow covariate effects to vary across landmarks. Predictors from administrative data were treated as fixed within each model, and risk estimates were generated conditional on PROMs being available at or before the landmark. The proportional hazards assumption was assessed by testing Schoenfeld residuals and inspecting log-minus-log survival plots.<sup>27</sup>

### Model Performance Evaluation

Model performance was assessed using 5-fold cross-validation within each of the 10 imputed datasets. Folds were assigned at the patient level before stacking the risk sets, ensuring all records from a given individual were placed in the same fold. Models were trained on 4 folds and validated on the held-out fold, repeating across folds and imputations. Fold-level estimates were then pooled within dataset and combined across imputations using Rubin’s rules.<sup>24</sup> CIs for performance metrics were obtained via 1,000 bootstrap replications within each imputation and combined across imputations.

Model performance was evaluated among patients under follow-up at each prediction window (30, 180, and 360 d).<sup>24</sup> Discrimination was assessed using the concordance statistic (C-index) for each prediction window and the time-dependent area under the receiver operating characteristic curve (AUC) across landmark times. A C-index or AUC \>0.7 was considered adequate and \>0.8 was considered good.<sup>28</sup> Calibration and predictive accuracy were evaluated using the calibration slope and Brier score.<sup>28</sup> The calibration slope measures agreement between predicted and observed risk. A slope of 1.0 indicates perfect calibration and values \<1 suggesting overfitting. The Brier score, ranging from 0 to 1, measures the mean squared difference between predicted probabilities and observed outcomes, with lower values indicating better predictive accuracy.<sup>28</sup>

To evaluate the added value of PROMs, we compared the Base model to PROM-enhanced models (ie, EQ-5D-5L-enhanced and VR-12-enhanced) using a common analysis cohort for each predictive horizon. To assess the relative contribution of predictors, we computed Wald chi-squared statistics for each covariate and expressed it as a percentage of the total model chi-squared value.<sup>28</sup>

### Subgroup Analysis

We examined the performance of the full-sample model in a subgroup of individuals with Ambulatory Care Sensitive Conditions (ACSCs) in the year before the index hospital admission. Following the definition used by the Canadian Institute for Health Information (CIHI),<sup>29</sup> ACSCs include a range of chronic and acute conditions, such as diabetes, chronic lower respiratory diseases, hypertension, heart failure and pulmonary edema, and angina. Hospitalizations for ACSCs are often considered potentially avoidable.<sup>30</sup> We assessed whether PROMs provided greater incremental value in this subgroup by comparing discrimination and calibration with and without EQ-5D-5L or VR-12.

### Sensitivity Analyses

To test the assumption of time-invariance in the landmark models, we fit a Cox model with time-dependent PROM covariates, with their values becoming active at the date of PROM completion. We repeated the primary analyses in complete cases only to assess sensitivity to the imputation strategy. To assess potential selection bias, we compared baseline characteristics and observed event rates between survey completers and noncompleters using absolute standardized mean differences (SMD).<sup>31,32</sup> An SMD \>0.10 was considered indicative of imbalance between groups.<sup>31</sup> Lastly, we estimated the probability of unplanned readmission or death within 30 and 180 days following PROM completion using logistic regression. The composite outcome was used to account for death as a competing event.

All analyses were performed using SAS 9.4 (SAS Institute) and R 4.4.2 (R Core Team).

## RESULTS

### Participants

Of the 11,177 individuals (Table <a href="#T1" data-ref-type="table">1</a>; Supplement Table S1.1, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>), the mean age was 66.4 (SD: 15.2) years; 53.5% were aged ≥60 years and 56.1% were male. Overall, 58.2% had urgent index hospitalization, and 77.6% stayed in hospital longer than one day. On the basis of VR-12 responses, 23.5% reported improved physical health and 20.4% reported improved mental health compared with a year prior. The average EQ-5D VAS was 67.3 (SD: 22.1). Observed unplanned readmission rates were 5.6% (n=626) at 30 days, 18.4% (n=2057) at 180 days postdischarge; by one year, 25.0% (n=2794) were readmitted and 6.5% (n=727) had died.

<div id="T1" class="table-wrap">

<div class="caption">

Patient Characteristics and Observed Outcomes

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Predictors</th>
<th style="text-align: center;">Analysis cohort</th>
<th style="text-align: center;">Complete cases</th>
<th style="text-align: center;">ACSC subgroup</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">N =</td>
<td style="text-align: center;">11,177</td>
<td style="text-align: center;">6253</td>
<td style="text-align: center;">2954</td>
</tr>
<tr>
<td style="text-align: left;">Age, mean (SD)</td>
<td style="text-align: center;">66.4 (15.2)</td>
<td style="text-align: center;">66.8 (14.9)</td>
<td style="text-align: center;">69 (13.6)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Age group, n (%)</td>
</tr>
<tr>
<td style="text-align: left;"> 18–29</td>
<td style="text-align: center;">640 (5.7)</td>
<td style="text-align: center;">180 (2.9)</td>
<td style="text-align: center;">53 (1.8)</td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td style="text-align: center;">1509 (13.5)</td>
<td style="text-align: center;">441 (7.1)</td>
<td style="text-align: center;">97 (3.3)</td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td style="text-align: center;">992 (8.9)</td>
<td style="text-align: center;">634 (10.1)</td>
<td style="text-align: center;">225 (7.6)</td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td style="text-align: center;">2050 (18.3)</td>
<td style="text-align: center;">1320 (21.1)</td>
<td style="text-align: center;">564 (19.1)</td>
</tr>
<tr>
<td style="text-align: left;"> 60–69</td>
<td style="text-align: center;">2887 (25.8)</td>
<td style="text-align: center;">1852 (29.6)</td>
<td style="text-align: center;">960 (32.5)</td>
</tr>
<tr>
<td style="text-align: left;"> 70–79</td>
<td style="text-align: center;">2136 (19.1)</td>
<td style="text-align: center;">1291 (20.6)</td>
<td style="text-align: center;">744 (25.2)</td>
</tr>
<tr>
<td style="text-align: left;"> 80+</td>
<td style="text-align: center;">961 (8.6)</td>
<td style="text-align: center;">535 (8.6)</td>
<td style="text-align: center;">316 (10.7)</td>
</tr>
<tr>
<td style="text-align: left;">Sex: male, n (%)</td>
<td style="text-align: center;">6268 (56.1)</td>
<td style="text-align: center;">3154 (50.4)</td>
<td style="text-align: center;">1600 (54.2)</td>
</tr>
<tr>
<td style="text-align: left;">&gt;1 ED visit in the previous year, n (%)</td>
<td style="text-align: center;">5544 (49.6)</td>
<td style="text-align: center;">3158 (50.5)</td>
<td style="text-align: center;">1450 (49.1)</td>
</tr>
<tr>
<td style="text-align: left;">&gt;1 Hospital stay in the previous year, n (%)</td>
<td style="text-align: center;">5335 (47.7)</td>
<td style="text-align: center;">3177 (50.8)</td>
<td style="text-align: center;">1471 (49.8)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Comorbidity count, n (%)</td>
</tr>
<tr>
<td style="text-align: left;"> 0</td>
<td style="text-align: center;">5258 (47.0)</td>
<td style="text-align: center;">2691 (43.0)</td>
<td style="text-align: center;">1178 (39.9)</td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: center;">2757 (24.7)</td>
<td style="text-align: center;">1718 (27.5)</td>
<td style="text-align: center;">850 (28.8)</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: center;">1557 (13.9)</td>
<td style="text-align: center;">895 (14.3)</td>
<td style="text-align: center;">462 (15.6)</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td style="text-align: center;">806 (7.2)</td>
<td style="text-align: center;">457 (7.3)</td>
<td style="text-align: center;">236 (8.0)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥4</td>
<td style="text-align: center;">799 (7.1)</td>
<td style="text-align: center;">492 (7.9)</td>
<td style="text-align: center;">228 (7.7)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Acuity of index admission, n (%)</td>
</tr>
<tr>
<td style="text-align: left;"> Elective</td>
<td style="text-align: center;">4672 (41.8)</td>
<td style="text-align: center;">2440 (39.0)</td>
<td style="text-align: center;">1221 (41.3)</td>
</tr>
<tr>
<td style="text-align: left;"> Urgent/emergent</td>
<td style="text-align: center;">6505 (58.2)</td>
<td style="text-align: center;">3813 (61.0)</td>
<td style="text-align: center;">1733 (58.7)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Index admission length of stay, n (%)</td>
</tr>
<tr>
<td style="text-align: left;"> 1 d</td>
<td style="text-align: center;">2506 (22.4)</td>
<td style="text-align: center;">1350 (21.6)</td>
<td style="text-align: center;">617 (20.9)</td>
</tr>
<tr>
<td style="text-align: left;"> 2 d</td>
<td style="text-align: center;">3444 (30.8)</td>
<td style="text-align: center;">1330 (21.3)</td>
<td style="text-align: center;">677 (22.9)</td>
</tr>
<tr>
<td style="text-align: left;"> 3 d</td>
<td style="text-align: center;">1700 (15.2)</td>
<td style="text-align: center;">1104 (17.7)</td>
<td style="text-align: center;">525 (17.8)</td>
</tr>
<tr>
<td style="text-align: left;"> 4-6 d</td>
<td style="text-align: center;">984 (8.8)</td>
<td style="text-align: center;">683 (10.9)</td>
<td style="text-align: center;">300 (10.2)</td>
</tr>
<tr>
<td style="text-align: left;"> 7-13 d</td>
<td style="text-align: center;">1575 (14.1)</td>
<td style="text-align: center;">1113 (17.8)</td>
<td style="text-align: center;">540 (18.3)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥14 d</td>
<td style="text-align: center;">968 (8.7)</td>
<td style="text-align: center;">673 (10.8)</td>
<td style="text-align: center;">295 (10.0)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Neighborhood income decile, n (%)</td>
</tr>
<tr>
<td style="text-align: left;"> 1 – lowest decile</td>
<td style="text-align: center;">1181 (10.6)</td>
<td style="text-align: center;">689 (11.0)</td>
<td style="text-align: center;">314 (10.6)</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: center;">1162 (10.4)</td>
<td style="text-align: center;">662 (10.6)</td>
<td style="text-align: center;">314 (10.6)</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td style="text-align: center;">1372 (12.3)</td>
<td style="text-align: center;">613 (9.8)</td>
<td style="text-align: center;">275 (9.3)</td>
</tr>
<tr>
<td style="text-align: left;"> 4</td>
<td style="text-align: center;">1081 (9.7)</td>
<td style="text-align: center;">594 (9.5)</td>
<td style="text-align: center;">308 (10.4)</td>
</tr>
<tr>
<td style="text-align: left;"> 5</td>
<td style="text-align: center;">1045 (9.3)</td>
<td style="text-align: center;">600 (9.6)</td>
<td style="text-align: center;">305 (10.3)</td>
</tr>
<tr>
<td style="text-align: left;"> 6</td>
<td style="text-align: center;">1045 (9.3)</td>
<td style="text-align: center;">590 (9.4)</td>
<td style="text-align: center;">288 (9.7)</td>
</tr>
<tr>
<td style="text-align: left;"> 7</td>
<td style="text-align: center;">1121 (10.0)</td>
<td style="text-align: center;">629 (10.1)</td>
<td style="text-align: center;">303 (10.3)</td>
</tr>
<tr>
<td style="text-align: left;"> 8</td>
<td style="text-align: center;">1118 (10.0)</td>
<td style="text-align: center;">642 (10.3)</td>
<td style="text-align: center;">297 (10.1)</td>
</tr>
<tr>
<td style="text-align: left;"> 9</td>
<td style="text-align: center;">1052 (9.4)</td>
<td style="text-align: center;">614 (9.8)</td>
<td style="text-align: center;">283 (9.6)</td>
</tr>
<tr>
<td style="text-align: left;"> 10 – highest decile</td>
<td style="text-align: center;">1000 (8.9)</td>
<td style="text-align: center;">620 (9.9)</td>
<td style="text-align: center;">267 (9.0)</td>
</tr>
<tr>
<td style="text-align: left;">30-d unplanned readmission, n (%)</td>
<td style="text-align: center;">626 (5.6)</td>
<td style="text-align: center;">364 (5.8)</td>
<td style="text-align: center;">332 (11.2)</td>
</tr>
<tr>
<td style="text-align: left;">180-d unplanned readmission, n (%)</td>
<td style="text-align: center;">2057 (18.4)</td>
<td style="text-align: center;">1217 (19.5)</td>
<td style="text-align: center;">741 (25.1)</td>
</tr>
<tr>
<td style="text-align: left;">360-d unplanned readmission, n (%)</td>
<td style="text-align: center;">2794 (25.0)</td>
<td style="text-align: center;">1657 (26.5)</td>
<td style="text-align: center;">1010 (34.2)</td>
</tr>
<tr>
<td style="text-align: left;">30-d mortality, n (%)</td>
<td style="text-align: center;">34 (0.3)</td>
<td style="text-align: center;">13 (0.2)</td>
<td style="text-align: center;">15 (1.0)</td>
</tr>
<tr>
<td style="text-align: left;">180-d mortality, n (%)</td>
<td style="text-align: center;">369 (3.3)</td>
<td style="text-align: center;">191 (3.1)</td>
<td style="text-align: center;">192 (6.5)</td>
</tr>
<tr>
<td style="text-align: left;">360-d mortality, n (%)</td>
<td style="text-align: center;">727 (6.5)</td>
<td style="text-align: center;">388 (6.2)</td>
<td style="text-align: center;">363 (12.3)</td>
</tr>
</tbody>
</table>

ACSC indicates Ambulatory Care Sensitive Condition; ED, Emergency Department.

</div>

### Model Performance

The inclusion of PROMs was associated with modest improvements in model discrimination across all predictive horizons. For the 180-day window, the C-index was 0.762 (95% CI, 0.761–0.763) for the Base model, increasing to 0.774 (95% CI, 0.773–0.774) with EQ-5D-5L and 0.782 (95% CI, 0.781–0.783) with VR-12 (Table <a href="#T2" data-ref-type="table">2</a>). Compared with the Base model, adding PROMs led to 1%–2% gains in concordance: 0.012 (95% CI, 0.010, 0.015) with EQ-5D-5L and 0.020 (95% CI, 0.019-0.022) with VR-12. Incremental gains in discrimination were similar at the 30-day horizon (Table <a href="#T2" data-ref-type="table">2</a>).

<div id="T2" class="table-wrap">

<div class="caption">

C-Index (95% CIs) for the Full-Sample Model and ACSC Subgroup Model

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: center;">Predictive horizon</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: center;">30-d</th>
<th style="text-align: center;">180-d</th>
<th style="text-align: center;">360-d</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Full-sample model</td>
</tr>
<tr>
<td style="text-align: left;"> Base</td>
<td style="text-align: left;">0.741 (0.738, 0.745)</td>
<td style="text-align: left;">0.762 (0.761, 0.763)</td>
<td style="text-align: left;">0.772 (0.768, 0.776)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-5L-enhanced</td>
<td style="text-align: left;">0.752 (0.749, 0.756)</td>
<td style="text-align: left;">0.774 (0.773, 0.774)</td>
<td style="text-align: left;">0.786 (0.782, 0.791)</td>
</tr>
<tr>
<td style="text-align: left;"> VR-12-enhanced</td>
<td style="text-align: left;">0.761 (0.756, 0.766)</td>
<td style="text-align: left;">0.782 (0.781, 0.783)</td>
<td style="text-align: left;">0.793 (0.788, 0.798)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, EQ-5D-5L-enhanced)</td>
<td style="text-align: left;">0.011 (0.009, 0.013)</td>
<td style="text-align: left;">0.012 (0.010, 0.015)</td>
<td style="text-align: left;">0.014 (0.011, 0.017)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, VR-12-enhanced)</td>
<td style="text-align: left;">0.020 (0.018, 0.022)</td>
<td style="text-align: left;">0.020 (0.019, 0.022)</td>
<td style="text-align: left;">0.021 (0.018, 0.024)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">ACSC subgroup model</td>
</tr>
<tr>
<td style="text-align: left;"> Base</td>
<td style="text-align: left;">0.712 (0.692, 0.738)</td>
<td style="text-align: left;">0.711 (0.693, 0.731)</td>
<td style="text-align: left;">0.728 (0.716, 0.746)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-5L-enhanced</td>
<td style="text-align: left;">0.714 (0.694, 0.732)</td>
<td style="text-align: left;">0.724 (0.701, 0.733)</td>
<td style="text-align: left;">0.732 (0.719, 0.741)</td>
</tr>
<tr>
<td style="text-align: left;"> VR-12-enhanced</td>
<td style="text-align: left;">0.734 (0.714, 0.754)</td>
<td style="text-align: left;">0.741 (0.722, 0.761)</td>
<td style="text-align: left;">0.762 (0.741, 0.782)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, EQ-5D-5L-enhanced)</td>
<td style="text-align: left;">0.002 (0.001, 0.004)</td>
<td style="text-align: left;">0.013 (0.008, 0.021)</td>
<td style="text-align: left;">0.004 (0.001, 0.007)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, VR-12-enhanced)</td>
<td style="text-align: left;">0.022 (0.018, 0.026)</td>
<td style="text-align: left;">0.030 (0.024, 0.036)</td>
<td style="text-align: left;">0.034 (0.029, 0.039)</td>
</tr>
</tbody>
</table>

ACSC indicates ambulatory care sensitive conditions.

Delta (∆) represents changes in C-index between the Base model and PROM-enhanced models.

</div>

The improvement was more pronounced in the ACSC subgroup, where the VR-12–enhanced model showed a 3% gain (0.030; 95% CI, 0.024–0.036) over the Base model at the 180-day mark, with similar gains in discrimination across other horizons (Table <a href="#T2" data-ref-type="table">2</a>). Calibration slopes were ∼1.0 across all windows, indicating adequate calibration (Table <a href="#T3" data-ref-type="table">3</a>). Time-dependent AUCs were higher at earlier landmark times and stabilized thereafter; PROM-enhanced models consistently outperformed the Base model, with the VR-12-enhanced model performing best. Brier scores ranged from 0.03 to 0.04 for 30-day predictions and increased to 0.12–0.13 for 180-day windows, suggesting lower absolute accuracy for longer-term predictions but remaining within an acceptable range (Fig. <a href="#F2" data-ref-type="fig">2</a>).

<div id="T3" class="table-wrap">

<div class="caption">

Calibration Slope (95% CIs) for the Full-Sample Model and ACSC Subgroup Model

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: center;">Predictive horizon</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: center;">30-d</th>
<th style="text-align: center;">180-d</th>
<th style="text-align: center;">360-d</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Full-sample model</td>
</tr>
<tr>
<td style="text-align: left;"> Base</td>
<td style="text-align: left;">1.034 (0.990, 1.078)</td>
<td style="text-align: left;">1.054 (1.040, 1.068)</td>
<td style="text-align: left;">1.080 (1.073, 1.085)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-5L-enhanced</td>
<td style="text-align: left;">1.001 (0.947, 1.055)</td>
<td style="text-align: left;">1.059 (1.050, 1.068)</td>
<td style="text-align: left;">1.075 (1.068, 1.083)</td>
</tr>
<tr>
<td style="text-align: left;"> VR-12-enhanced</td>
<td style="text-align: left;">1.013 (0.952, 1.074)</td>
<td style="text-align: left;">1.072 (1.057, 1.087)</td>
<td style="text-align: left;">1.078 (1.063, 1.088)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, EQ-5D-5L-enhanced)</td>
<td style="text-align: left;">−0.031 (−0.054, −0.012)</td>
<td style="text-align: left;">0.006 (0.000, 0.010)</td>
<td style="text-align: left;">−0.005 (−0.006, −0.003)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, VR-12-enhanced)</td>
<td style="text-align: left;">−0.020 (−0.046, 0.004)</td>
<td style="text-align: left;">0.018 (0.012, 0.024)</td>
<td style="text-align: left;">−0.006 (−0.009, 0.005)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">ACSC subgroup model</td>
</tr>
<tr>
<td style="text-align: left;"> Base</td>
<td style="text-align: left;">0.974 (0.946, 1.012)</td>
<td style="text-align: left;">0.979 (0.975, 0.989)</td>
<td style="text-align: left;">1.009 (1.005, 1.020)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-5L-enhanced</td>
<td style="text-align: left;">0.972 (0.954, 1.013)</td>
<td style="text-align: left;">1.003 (0.999, 1.007)</td>
<td style="text-align: left;">1.007 (1.000, 1.024)</td>
</tr>
<tr>
<td style="text-align: left;"> VR-12-enhanced</td>
<td style="text-align: left;">0.979 (0.959, 1.009)</td>
<td style="text-align: left;">1.005 (0.997, 1.021)</td>
<td style="text-align: left;">1.012 (1.003, 1.023)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, EQ-5D-5L-enhanced)</td>
<td style="text-align: left;">−0.002 (−0.015, 0.013)</td>
<td style="text-align: left;">0.022 (0.019, 0.029)</td>
<td style="text-align: left;">−0.003 (−0.003, 0.005)</td>
</tr>
<tr>
<td style="text-align: left;"> ∆ (Base, VR-12-enhanced)</td>
<td style="text-align: left;">0.006 (−0.009, 0.015)</td>
<td style="text-align: left;">0.024 (0.021, 0.031)</td>
<td style="text-align: left;">0.004 (−0.002, 0.008)</td>
</tr>
</tbody>
</table>

Delta (∆) represents changes in calibration slope between the Base model and PROM-enhanced models.

</div>

<figure id="F2">
<p><img src="mlr-64-387-g002.jpg" /></p>
<figcaption>Time-dependent AUC and brier score for the full-sample model. AUC: area under the curve. Pointwise 95% CIs for AUC and Brier scores were narrow; full details are in Supplementary File IV, Supplemental Digital Content 1, <a href="http://links.lww.com/MLR/D149">http://links.lww.com/MLR/D149</a>.</figcaption>
</figure>

Across all prediction windows, age, comorbidity count, LOS, acuity of index admission, and hospital or ED visits in the prior year were top predictors of readmission in the Base models. In the VR-12-enhanced models, VR-12 current health status and physical limitations were ranked among the top 15 predictors. Similarly, the mobility dimension and the EQ-5D VAS emerged as top predictors within the EQ-5D-5L-enhanced models (Supplement File III, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). Proportional hazards assessments did not indicate violations within landmarks.

### Subgroup Analysis

In the ACSC subgroup, discrimination improved notably with VR-12 data. Concordance statistics increased by 2.4%-3.0% compared with the Base model across prediction windows (Table <a href="#T2" data-ref-type="table">2</a> and Supplement Fig. S3, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). Including EQ-5D-5L did not significantly improve model discrimination. Calibration slopes improved by 0.01–0.02 in the ACSC subgroup (Table <a href="#T3" data-ref-type="table">3</a>).

### Sensitivity Analyses

Survey completers and noncompleters were broadly similar on measured baseline characteristics, although noncompleters were older and more likely to have an urgent index admission (Supplemental Table S1.2, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). Findings from the time-varying Cox model were consistent with the landmark models (Supplemental Fig. S3, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). For example, at the 360-day window, the c-index was 0.77 (95% CI, 0.76–0.78) for Base, 0.78 (95% CI, 0.76–0.79) for EQ-5D-5L-enhanced, and 0.78 (95% CI, 0.77–0.79) for VR-12 enhanced. These results suggested that assuming PROMs were time-invariant at each landmark did not introduce substantial bias (Supplement Table S2, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). Results from the complete data were consistent with our main findings, indicating the magnitude and direction of change in model concordance and calibration remained stable (Supplement Table S3, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>). In the logistic regression anchored at PROMs completion, the added value of PROMs was consistent with the primary analysis (Supplemental Table S4, Supplemental Digital Content 1, <http://links.lww.com/MLR/D149>).

## DISCUSSION

In this population-based cohort of adults discharged from acute care, adding either EQ-5D-5L or VR-12 to models using administrative data led to modest but consistent improvements in predicting unplanned readmission. While model discrimination tends to increase with the inclusion of more predictors,<sup>28</sup> the 1%–2% gain associated with PROMs represents the contribution of patients’ perspectives of their health—information not typically captured in administrative data. Improvements in model performance were more notable among patients with ACSCs, for whom day-to-day functioning and stamina are pivotal for postdischarge health trajectories. PROM domains related to physical functioning and mobility may account for this added predictive value.

Interpreted against a LACE-like baseline, PROMs added a meaningful patient-centered layer by capturing patients’ perspectives on their functional status and symptom burden—domains that often shape postdischarge care management but are often poorly represented in administrative data. Variable-importance analysis supports this interpretation: in PROM‑enhanced models, VR‑12 items on current health status and physical limitations, and EQ‑5D-5L mobility and VAS consistently ranked among top predictors. Notably, the VR-12 captures a broader set of domains—including mental health, role limitations, and social functioning—which may help explain its relatively larger incremental contribution compared with the EQ-5D-5L.<sup>22</sup> The predictors in our Base model mirrored LACE domains,<sup>8</sup> but our model was not a re-implementation of the LACE index, which was originally developed to estimate 30-day risk of urgent readmission or death. For these reasons, direct comparisons to LACE model performance may not be appropriate. Our findings speak to the incremental contribution of PROMs on a LACE-like baseline rather than comparative performance against LACE.

Our findings align with the growing literature indicating that PROMs marginally improve readmission prediction,<sup>33</sup> although much prior work often relied on smaller samples, focused on specific health conditions, or was developed for quality assurance purposes.<sup>16</sup> Our study extends this literature by using generic and validated PROMs in a general inpatient population, evaluating over multiple horizons, and accommodating real-world variations in survey timing via landmarking. The larger contributions of PROMs observed in clinically complex groups (ie, ACSCs) also align with reports from condition-focused settings such as heart failure,<sup>29</sup> where symptom burden and functional limitations have been shown to predict hospital readmissions.

Beyond prediction, our findings have pragmatic implications. For health systems already collecting PROMs, these data can refine prioritization at the upper end of the risk distribution—where postdischarge monitoring and care management resources (eg, rehabilitation or medication management) are concentrated - without new data collection or major changes to clinical workflows.<sup>15</sup> PROMs have been routinely collected and integrated into electronic health records (EHRs) in the United States and globally to support quality monitoring, inform care planning, and facilitate patient-provider communication.<sup>34</sup> Leveraging the existing infrastructure, the integration of PROM-enhanced prediction models could be used to help identify patients reporting severe mobility problems or functional limitations. Early identification of these patients may guide targeted interventions, which in turn can help prevent functional decline and reduce unplanned readmissions.<sup>35</sup>

Despite a growing emphasis on incorporating the “patient voice” in value-based care and the widespread collection of PROMs,<sup>4</sup> these measures are infrequently used to inform care planning decisions. Several key barriers contribute to this gap: PROM-based workflows are often siloed in pilot projects rather than implemented system-wide; integration into EHRs and clinical decision support is limited; and clinician engagement is low in the absence of visible champions or demonstrated utility.<sup>36</sup> Patient-reported experience measures (PREMs) related to care transitions show that patient-reported data can be implemented for accountability. For example, the Care Transitions Measure (CTM-3), embedded in the federal Hospital Consumer Assessment of Healthcare Providers and Systems (HCAHPS) survey, is used for hospital-level quality reporting.<sup>37,38</sup> In BC, the PROMs in the Acute Inpatient Survey were collected by the Ministry of Health for provincial quality improvement, with the goal of assessing aggregated outcome differences within and between hospital units.<sup>19</sup> We showed that PROM-enhanced models can be developed using routinely collected data without additional patient or clinician burden, and these models can potentially help ministries and health authorities identify patients with elevated readmission risk. By quantifying the incremental predictive value of PROMs over administrative variables, we provide an evidence base to justify investment in integrating PROM-based risk stratification to inform system-level follow-up care planning and resource allocation. While operational challenges remain, the ability to repurpose existing PROMs data for targeted patient follow-up offers a pathway to bridge the gap between data collection and actionable patient-centered care, supporting the ongoing efforts to advance value-based care.

### Strengths and Limitations

This study benefits from a large, population-based sample and routinely collected administrative data linked with validated generic PROMs, enhancing generalizability to health systems where PROM integration is increasingly common. In systems where PROMs are routinely collected after discharge, our models demonstrate how these data can be used to enhance risk prediction and inform postdischarge monitoring and ongoing care management.

Several limitations should be noted. Our analysis was limited to individuals who may be more likely to engage with health system follow-up after discharge. In practice, nonrespondents may differ systematically in health literacy, socioeconomic status, and other unmeasured factors. Nonetheless, this cohort represents those more likely to participate in PROMs as part of routine care.<sup>39</sup> Therefore, while potential response bias exists, the findings retain practical relevance for informing postdischarge follow-up care planning.

Given PROMs were collected weeks after discharge, the predictive horizons represent the periods following prespecified landmark times and may miss early readmissions. To address this and mitigate immortal time bias, we used a Cox landmark model aligning risk estimation with PROMs availability. While this approach does not support immediate discharge decisions, it provides conditional risk assessment for patients already discharged to the community. These findings show that postdischarge functional monitoring—building on foundational concepts like ADLs (Activities of Daily Living)—can help identify patients who may benefit from continued follow-up beyond the initial transition period. Furthermore, PROMs were measured once and carried forward; to assess whether this assumption materially affected results, we conducted a sensitivity analysis treating PROMs as time-dependent covariates. Findings were similar to the main analysis, suggesting any bias from assuming time-invariant PROM effects was small.

Future research should examine how PROMs improve risk prediction in clinically distinct subpopulations, particularly those with multimorbidity and functional impairments. Economic evaluations are needed to assess whether PROM-enhanced models lead to meaningful improvement in downstream outcomes and justify data collection costs. External validation in other jurisdictions will also be essential.

## CONCLUSIONS

In health systems where PROMs are routinely collected, PROM-enhanced prediction models can help identify patients at risk of readmission and support targeted follow-up and ongoing care management after discharge.

## Supplementary Material

<figure id="s001">

</figure>

### ACKNOWLEDGMENTS

Maggie Yu acknowledges the Canada Graduate Scholarships (CGS-M), which supported her academic training.

## REFERENCES

1. SheetritEBriefMElishaO. Predicting unplanned readmissions in the intensive care unit: a multimodality evaluation. Sci Rep. 2023;13:15426.37723231 10.1038/s41598-023-42372-yPMC10507073

2. Overview of Clinical Conditions with Frequent and Costly Hospital Readmissions by Payer, 2018; 278. Accessed May 16, 2025. https://hcup-us.ahrq.gov/reports/statbriefs/sb278-Conditions-Frequent-Readmissions-By-Payer-2018.jsp

3. All Patients Readmitted to Hospital | CIHI. Accessed November 28, 2024. https://www.cihi.ca/en/indicators/all-patients-readmitted-to-hospital

4. Hospital Readmissions Reduction Program (HRRP) | CMS. Accessed May 16, 2025. https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps/hospital-readmissions-reduction-program-hrrp

5. KarenEJoyntMDJoseF. Opinions on the hospital readmission reduction program: results of a national survey of hospital leaders. Am J Manag Care. 2016;22:e287–e294.27556831 PMC6948716

6. McAlisterFAYoungsonEBakalJA. Impact of physician continuity on death or urgent readmission after discharge among patients with heart failure. CMAJ. 2013;185:E681–E689.23959284 10.1503/cmaj.130048PMC3787192

7. TylerNHodkinsonAPlannerC. Transitional care interventions from hospital to community to reduce health care use and improve patient outcomes. JAMA Netw Open. 2023;6:e2344825.38032642 10.1001/jamanetworkopen.2023.44825PMC10690480

8. van WalravenCDhallaIABellC. Derivation and validation of an index to predict early death or unplanned readmission after discharge from hospital to the community. CMAJ. 2010;182:551–557.20194559 10.1503/cmaj.091117PMC2845681

9. DonzéJAujeskyDWilliamsD. Potentially avoidable 30-day hospital readmissions in medical patients: derivation and validation of a prediction model. JAMA Intern Med. 2013;173:632–638.23529115 10.1001/jamainternmed.2013.3023

10. StaplesJAWiksykBLiuG. External validation of the modified LACE+, LACE+, and LACE scores to predict readmission or death after hospital discharge. J Eval Clin Pract. 2021;27:1390–1397.33963605 10.1111/jep.13579

11. PampalonRHamelDGamacheP. A deprivation index for health planning in Canada. Chronic Dis Can. 2009;29:178–191.19804682

12. IbrahimAMKoesterCAl-AkcharM. HOSPITAL Score, LACE Index and LACE+ Index as predictors of 30-day readmission in patients with heart failure. BMJ Evid Based Med. 2020;25:166–167.10.1136/bmjebm-2019-11127131771947

13. BoultCDowdBMcCaffreyD. Screening elders for risk of hospital admission. J Am Geriatr Soc. 1993;41:811–817.8340558 10.1111/j.1532-5415.1993.tb06175.x

14. VámosiMLaubergABorregaardB. Patient-reported outcomes predict high readmission rates among patients with cardiac diagnoses. Findings from the DenHeart study. Int J Cardiol. 2020;300:268–275.31748184 10.1016/j.ijcard.2019.09.046

15. BianchimMSCraneEJonesA. The implementation, use and impact of patient reported outcome measures in value-based healthcare programmes: a scoping review. PLoS One. 2023;18:e0290976.38055759 10.1371/journal.pone.0290976PMC10699630

16. YuMHarrisonMBansbackN. Can prediction models for hospital readmission be improved by incorporating patient-reported outcome measures? A systematic review and narrative synthesis. Qual Life Res. 2024;33:1767–1779.38689165 10.1007/s11136-024-03638-8

17. CollinsGSReitsmaJBAltmanDG. Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD Statement. BMC Med. 2015;13:1.25563062 10.1186/s12916-014-0241-zPMC4284921

18. Population Data BC. Accessed May 16, 2025. https://www.popdata.bc.ca/

19. Patient Reported Outcome Measures (PROMs). NHS England Digital. Accessed May 18, 2025. https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/patient-reported-outcome-measures-proms

20. HerdmanMGudexCLloydA. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20:1727–1736.21479777 10.1007/s11136-011-9903-xPMC3220807

21. WareJEKosinskiMKellerSD. A 12-item short-form health survey: construction of scales and preliminary tests of reliability and validity. Med Care. 1996;34:220.8628042 10.1097/00005650-199603000-00003

22. KwonJYCuthbertsonLSawatzkyR. The use of generic patient-reported outcome measures in emergency department surveys: discriminant validity evidence for the Veterans RAND 12-Item Health Survey and the EQ-5D. Value Health. 2022;25:1939–1946.36055921 10.1016/j.jval.2022.07.016

23. ElixhauserASteinerCHarrisDR. Comorbidity measures for use with administrative data. Med Care. 1998;36:8–27.9431328 10.1097/00005650-199801000-00004

24. RubinDB. Multiple imputation for nonresponse in surveys. New York, NY: John Wiley & Sons; 1987.

25. GomesMGutackerNBojkeC. Addressing missing data in patient-reported outcome measures (PROMS): implications for the use of PROMS for comparing provider performance. Health Econ. 2016;25:515–528.25740592 10.1002/hec.3173PMC4973682

26. Van HouwelingenHC. Dynamic prediction by landmarking in event history analysis. Scandinavian Journal of Statistics. 2007;34:70–85.

27. KleinbaumDGKleinM. Evaluating the proportional hazards assumptionKleinbaumDGKleinM. Survival Analysis: A Self-Learning Text. New York, NY: Springer; 2012:161–200.

28. SteyerbergEWVickersAJCookNR. Assessing the performance of prediction models: a framework for traditional and novel measures. Epidemiology. 2010;21:128.20010215 10.1097/EDE.0b013e3181c30fb2PMC3575184

29. Ambulatory Care Sensitive Conditions | CIHI. Accessed May 23, 2024. https://www.cihi.ca/en/indicators/ambulatory-care-sensitive-conditions

30. PurdySGriffinTSalisburyC. Ambulatory care sensitive conditions: terminology and disease coding need to be more specific to aid policy makers and clinicians. Public Health. 2009;123:169–173.19144363 10.1016/j.puhe.2008.11.001

31. CohenJ. Statistical Power Analysis for the Behavioral Sciences, 2nd ed. Routledge; 2013.

32. AustinPC. Using the standardized difference to compare the prevalence of a binary variable between two groups in observational research. Commun Stat - Simul Comput. 2009;38:1228–1234.

33. RyanPFurnissABreslinK. Assessing and augmenting predictive models for hospital readmissions with novel variables in an urban safety-net population. Med Care. 2021;59:1107.34593712 10.1097/MLR.0000000000001653

34. BrookEMGlerumKMHigginsLD. Implementing patient-reported outcome measures in your practice: pearls and pitfalls. Am J Orthop (Belle Mead NJ). 2017;46:273–278.29309444

35. HondaYHonmaKNishimuraS. Predictors of postoperative physical functional decline at hospital discharge in elderly patients with prolonged intensive care unit stay after cardiac surgery. Heart Lung. 2024;64:86–92.38070278 10.1016/j.hrtlng.2023.11.014

36. FontaineGPoitrasMESassevilleM. Barriers and enablers to the implementation of patient-reported outcome and experience measures (PROMs/PREMs): protocol for an umbrella review. Syst Rev. 2024;13:96.38532492 10.1186/s13643-024-02512-5PMC10964633

37. ColemanEAMahoneyEParryC. Assessing the quality of preparation for posthospital care from the patient’s perspective: the care transitions measure. Med Care. 2005;43:246.15725981 10.1097/00005650-200503000-00007

38. ColemanEAParryCChalmersSA. The central role of performance measurement in improving the quality of transitional care. Home Health Care Serv Q. 2007;26:93–104.18032202 10.1300/J027v26n04_07

39. HarrisIACashmanKLorimerM. Are responders to patient health surveys representative of those invited to participate? An analysis of the Patient-Reported Outcome Measures Pilot from the Australian Orthopaedic Association National Joint Replacement Registry. PLoS One. 2021;16:e0254196.34214088 10.1371/journal.pone.0254196PMC8253407

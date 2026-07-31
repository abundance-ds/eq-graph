---
project_id: "2016160"
work_id: "doi:10.1007/s11136-019-02256-z"
doi: "10.1007/s11136-019-02256-z"
pmid: "31364035"
pmcid: "PMC6803580"
title: "Correspondence of directly reported and recalled health-related quality of life in a large heterogeneous sample of trauma patients"
journal: "Quality of Life Research"
publication_date: "2019-07-30"
volume: "28"
issue: "11"
authors:
  - name: "I. Spronk"
    orcid: "http://orcid.org/0000-0001-9571-576X"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
      - "Aff3"
  - name: "A. J. L. M. Geraerds"
    affiliation_ids:
      - "Aff1"
  - name: "G. J. Bonsel"
    orcid: "http://orcid.org/0000-0002-8364-1086"
    affiliation_ids:
      - "Aff1"
      - "Aff4"
  - name: "M. A. C. de Jongh"
    affiliation_ids:
      - "Aff5"
  - name: "S. Polinder"
    affiliation_ids:
      - "Aff1"
  - name: "J. A. Haagsma"
    orcid: "http://orcid.org/0000-0002-2055-548X"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.5645.2000000040459992XDepartment of Public Health, Erasmus MC, University Medical Center Rotterdam, P.O. Box 2040, 3000 CA Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "grid.416213.30000 0004 0460 0556Association of Dutch Burn Centres, Maasstad Hospital, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "grid.12380.380000 0004 1754 9227Department of Plastic, Reconstructive and Hand Surgery, Amsterdam Movement Sciences, Amsterdam UMC, Vrije Universiteit Amsterdam, Amsterdam, The Netherlands"
  - id: "Aff4"
    name: "grid.7692.a0000000090126352Division Mother and Child, Utrecht University Medical Center, Utrecht, The Netherlands"
  - id: "Aff5"
    name: "Department Trauma TopCare, ETZ Hospital, Hilvarenbeekseweg 60, 5022 GC Tilburg, The Netherlands"
keywords:
  - "EQ-5D"
  - "Health-related quality of life"
  - "Retrospective assessment"
  - "Trauma population"
licence: "cc-by"
source_file: "input/projects/2016160/papers/doi_10.1007_s11136-019-02256-z.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6803580/fullTextXML"
source_method: "epmc_xml"
source_sha256: "d4ef335237248053539fe70aa144b7a96c8ed570348be0276a157a2b0eb7d358"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Correspondence of directly reported and recalled health-related quality of life in a large heterogeneous sample of trauma patients

## Abstract

### Purpose

To evaluate the correspondence of directly reported and recalled health-related quality of life (HRQL) in a heterogeneous sample of trauma patients.

### Methods

Adult trauma patients who attended the Emergency Department and were admitted between 03/2016 and 11/2016 were invited to participate. Postal surveys were sent 1 week (T1), 3 months (T2), and 12 months (T3) post-trauma. The EQ-5D-3L and Visual Analogue Scale (EQ-VAS) were used to assess directly reported and recalled HRQL.

### Results

The EQ-5D was completed by 446 patients at T1, T2, and T3. Directly reported mean T1 EQ-5D summary score was 0.482, whereas recalled T1 EQ-5D summary score was 0.453 (*p* \< 0.05) at T2 and 0.363 (*p* \< 0.001) at T3. Directly reported mean T2 EQ-5D summary score was 0.737 and mean recalled T2 EQ-5D summary score was 0.713 (*p* \< 0.05) at T3. Directly reported mean T1 EQ-VAS was 56.3, whereas mean recalled T1 EQ-VAS at T2 and T3 was 55.4 (*p* = 0.304) and 53.3 (*p* \< 0.05), respectively. Directly reported mean T2 EQ-VAS was 72.5 and recalled T2 EQ-VAS at T3 was 68.0 (*p* \< 0.001). The correspondence between all directly reported and recalled HRQL (both EQ-5D summary and EQ-VAS) was fair (ICC = 0.518–0.598). Lowest correspondence was seen in patients with major trauma (injury severity score ≥ 16) and in patients with middle-level education.

### Conclusions

Recalled HRQL measured by the EQ-5D-3L and EQ-VAS was systematically lower compared to the directly reported HRQL. Patient characteristics, injury severity, subjectivity of the dimension, and time interval appear to influence correspondence between directly reported and recalled HRQL.

### Electronic supplementary material

The online version of this article (10.1007/s11136-019-02256-z) contains supplementary material, which is available to authorized users.

## Introduction

An important outcome in trauma care is health-related quality of life (HRQL) of patients. HRQL reflects a patient’s physical, psychological, and social well-being \[1\]. This subjective measurement is increasingly used in estimating the impact of an injury, in evaluating the quality of care provided, and in providing patient information on particular injuries \[2, 3\]. Measurement of HRQL changes over time may be additionally useful to understand patterns of recovery over time and the role of rehabilitative care \[4, 5\].

It is, however, a challenge to establish reliable and valid outcomes for changes of HRQL over time. The best time frame to measure relevant changes over time may be difficult to define ex ante, data may be incomplete due to censoring (death, withdrawal) or random missings, and the event itself may be unpredictable, which makes prospectively collecting HRQL data difficult or impossible \[4\]. Retrospective assessment can be used to reconstruct the HRQL at an earlier time point. Retrospective assessment is easier to implement and involves less patient burden, but may be confounded by recall bias \[6\], and response shift may occur \[7–9\]. Recall bias is defined as a systematic measurement error, due to memory decay, which is the fading of memory with time. As a result, patients may remember their HRQL as being better or worse than it actually was \[10\]. Response shift on the other hand is the change in the meaning of a person’s evaluation of a specific construct. This can be caused by a change in internal standards, a change in values, and/or a redefinition of the construct \[11, 12\]. Among trauma patients, response shift may occur between multiple post-injury HRQL measurements due to patients adapting to their ill health.

Conventionally measured change in HRQL (post-level minus pre-level) may not be identical to the change in HRQL as reported by the patient, looking back at the time point of interest (retrospective change). If we take post-level minus pre-level as gold standard, retrospective recall bias will depend on the time interval between the measurement and the recall moment, as bias likely increases with longer intervals between measurements \[6\]. The presence of recall effects may also depend on the scale used, where a visual analogue scale (VAS) with a wide range of response options may be easier distorted than a classification-like scale with a limited number of response options, like the descriptive system of the EQ-5D-3L \[13\]. Finally, adequate props and instructions may support retrospective measurement avoiding the tendency to create emotionally fitting stories (cognitive dissonance reduction) \[14\].

Only few studies with varying results have evaluated the correspondence of patient recall of HRQL. Correspondence was poor \[intraclass correlation coefficient (ICC) 0.34–0.40\] among a sample of elderly hospitalized patients (3 day vs. 38 days assessment). A large proportion of this poor correspondence was attributed to recall bias; the correspondence after adjustment for recall bias was excellent (ICC 0.90–0.98) \[15\]. Two other studies in patients with prostate cancer found moderate correspondence (ICC 0.39–0.57) between pre-surgery HRQL and recalled pre-surgery HRQL (pre-surgery and 6–37 months post-surgery assessment) \[16, 17\], and a study in patients with hip arthroplasty found good correspondence of pre-surgery HRQL and retrospectively assessed HRQL at various time points (3 days, 6 weeks, and 3 months assessment) post-surgery (ICC 0.70–0.95) \[18\].

This study is the first study ever to evaluate the correspondence of directly reported HRQL and recalled HQRL in a heterogeneous sample of trauma patients, with specific attention to predefined subgroups. It compares directly reported EQ-5D summary and EQ-VAS scores collected at 1 week and 3 months post-injury, and recalled scores of 1 week collected at 3 months and 12 months post-injury, and recalled scores of 3 months collected at 12 months.

## Methods

### Study design

The present study is part of the Brabant Injury Outcome Surveillance (BIOS) study. This prospective longitudinal cohort study assesses HRQL in trauma patients who were admitted to one of 10 hospitals in the region Noord-Brabant (the Netherlands) \[19\]. The follow-up period in this dataset was 24 months; however, recall questions were only included at the 3 months and 12 months survey. Therefore, the 12-month follow-up data were used for the present study. Approval for the BIOS study was given by the Medical Ethics Committee Brabant (NL50258.028.14).

### Participants

Participants were adult (≥ 18 years) trauma patients, with an intake at the Emergency Department (ED) and who were admitted to either an Intensive Care unit (ICU) or a ward of one of the ten hospitals between March 2016 and November 2016. Only patients who survived hospital discharge were included. Patients who were unable to reply to Dutch language questionnaires, patients with a pathological fracture due to a malignancy or metastasis, and patients without a permanent address were excluded \[19\]. 1 week after their hospital admission, all eligible patients were invited to participate in the present study via a postal invitation, including an informed consent form and the first questionnaire (T1). Non-responders received a phone call to discuss participation one week after receiving the questionnaire. After consent was given, subsequent recall questionnaires were sent 3 months (T2), and 12 months (T3) post-trauma. Only data from patients who completed all items in all questionnaires were included in the analysis. Informed consent was obtained from all individual participants in the study.

### Measures

The first questionnaire covered patient characteristics, like age and gender, and the presence of self-reported chronic morbidity, e.g., diabetes. In such cases the patient was defined as having comorbidity \[20\]. All questionnaires included the EQ-5D-3L, which is a preference-based measure to estimate utility that was used to assess patients health status. It includes five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. The five dimensions have three ordered response options: no problems, moderate problems, and extreme problems \[21\]. Based on these five dimensions, a summary score (through weighting) was calculated by using the Dutch value set. The summary score can range between 0 (death) and 1 (full health) \[22\]. The summary score rarely has a negative value for health states stated to be worse than death. Besides, the EQ-5D-3L includes a visual analogue scale (EQ-VAS) \[23\], consisting of a scale from 0 (worst imaginable health) to 100 (best imaginable health). Participants were asked to complete the EQ-5D-3L and the EQ-VAS for the current situation in all questionnaires. At T2 and T3 they were also asked to report what they remember to have reported on the EQ-5D-3L at the previous assessment(s). We added a general statement emphasizing the recalled time point of interest (T1 or T2) to each of the EQ-5D-3L questionnaires. At T3, we first asked participants to recall T1 and then T2. At T2, the T1 recall was asked and at T3, the T2 and T1 recall was requested.

### Injury data

Injury data of included patients were available from the Brabant Trauma Registry. In this registry, all ten participating hospital are included. Data included the Abbreviated Injury Scale (AIS) \[24\]. The AIS classifies the severity of a trauma via an anatomic reference scale. The AIS describes type, location, and rates—the severity in numbers. Based on the highest AIS score in each injured body region, the Injury Severity Score (ISS) is composed as follows. The three most severely injured body regions according to the severity rating are selected, and the severity scores are squared and summed up. By definition the ISS ranges from 1 to 75. A major trauma is defined as an ISS ≥ 16 \[25\].

### Hypotheses

Our hypotheses are:

- Correspondence between the directly reported and recalled score is lower with the EQ-VAS compared to the EQ-5D summary score as the EQ-5D descriptive system has a limited number of response options and is thus expected to be less prone to recall bias.

- Correspondence between the directly reported and recalled score is higher with the 3-month window compared to the 9- and 12-month window as bias likely increases with longer intervals between measurements

- Correspondence between the directly reported and recalled score is lower among severely injured patients (ISS ≥ 16) as we expect a stronger cognitive dissonance among these patients because their rehabilitation period is long and patients adapt to their non-optimal post-state.

### Statistical analysis

All analyses were performed using SPSS version 23. A non-response analysis was performed to test for differences among responders and non-responders. Chi-square tests were used for categorical variables and Mann–Whitney U tests for continuous variables. We compared T1–T2, T1–T3, and T2–T3 correspondence of direct (i.e., the EQ-5D outcome at that moment) versus recalled outcomes for the EQ-5D summary, the dimensions, and the EQ-VAS scores. The paired *t* test was used to compare the direct versus recalled outcomes for all participants, and for subgroups based on age, gender, education, comorbidity, and ISS. For the subgroup paired *t* test, we split the sample into the aforementioned subgroups. Additionally, we used the intraclass correlation coefficient (ICC) \[26\]. The ICC describes quantitative correspondence of two numericals. Again this analysis was done to compare direct versus recalled outcomes on an individual level for all patients and the subgroups. ICC was defined as being poor (\< 0.40), fair (0.40–0.59), good (0.60–0.74), or excellent (0.75–1.00) \[27\]. A perfect ICC (1.0) is the result of no difference on the individual level. However, an imperfect ICC (say 0.6) may point to a systematic difference between direct and recall outcomes \[e.g., recall always ‘better’\] which in turn will lead to a significant difference in *t* test terms (provided numbers are reasonable), or it may point to a random difference between the two \[e.g., due to vague memory\] which in turn will lead to no (group) difference in *t* test terms. Hence, recall bias and error both limit the ICC, but only bias affects the *t* test.

## Results

### Participants

In total, 5731 trauma patients were invited to participate in present study, of whom 1518 patients (26.5%) agreed to participate. The questionnaire within 1 week of the trauma (T1) was completed by 759 participants (50.0%), the questionnaire at 3 months (T2) by 1294 participants (85.2%) and at 12 months (T3) by 1255 participants (82.7%). In total, 551 participants returned the three questionnaires and the direct EQ-5D and recall EQ-5D were completed by 446 participants (29.4%) for T1–T2–T3. Non-response analysis showed that participants were significantly younger (*p* \< 0.05) and more often males (*p* \< 0.05) than non-respondents.

Responders had a mean age of 61.5 years (SD 15.3) and 55% was male (Table <a href="#Tab1" data-ref-type="table">1</a>). Many responders had middle or high level education and comorbidity was highly prevalent; more than half (57%) of the patients had a chronic disease. Median hospital stay was 4.0 days (IQR 2.0–6.0 days). The most common injuries were mild traumatic brain injury (28%) and hip fracture (21%). Median ISS was 5.0 (IQR 4.0–9.0), with 29 participants (7%) having a major trauma.

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of study population

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristic</th>
<th style="text-align: left;">Participants (<em>n</em> = 446)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Gender: Male</td>
<td style="text-align: left;">247 (55.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Age (M, SD)</td>
<td style="text-align: left;">61.5 (15.3)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Education</td>
</tr>
<tr>
<td style="text-align: left;"> Low</td>
<td style="text-align: left;">97 (21.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> Middle</td>
<td style="text-align: left;">171 (38.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> High</td>
<td style="text-align: left;">171 (38.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> Unknown</td>
<td style="text-align: left;">7 (1.6%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Comorbidity status</td>
</tr>
<tr>
<td style="text-align: left;"> No comorbidity</td>
<td style="text-align: left;">185 (41.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Comorbidity</td>
<td style="text-align: left;">253 (56.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> Unknown</td>
<td style="text-align: left;">8 (1.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Length of hospital stay (Median, IQR)</td>
<td style="text-align: left;">4.0 (2.0-6.0)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Injury type</td>
</tr>
<tr>
<td style="text-align: left;"> Pelvic injury</td>
<td style="text-align: left;">56 (12.6%)</td>
</tr>
<tr>
<td style="text-align: left;"> Hip fracture</td>
<td style="text-align: left;">93 (20.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> Tibia, complex foot or femur fracture</td>
<td style="text-align: left;">58 (13.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> Shoulder and upper arm injury</td>
<td style="text-align: left;">53 (11.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> Radius, ulna or hand fracture</td>
<td style="text-align: left;">32 (7.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Mild TBI</td>
<td style="text-align: left;">124 (27.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> Severe TBI</td>
<td style="text-align: left;">10 (2.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Facial fracture</td>
<td style="text-align: left;">23 (5.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Thoracic injury</td>
<td style="text-align: left;">25 (5.6%)</td>
</tr>
<tr>
<td style="text-align: left;"> Rib fracture</td>
<td style="text-align: left;">60 (13.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Mild abdominal injury</td>
<td style="text-align: left;">10 (2.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Severe abdominal injury</td>
<td style="text-align: left;">3 (0.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> Spinal cord injury</td>
<td style="text-align: left;">2 (0.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> Stable vertebral fracture or disc injury</td>
<td style="text-align: left;">31 (7.0%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Injury severity score</td>
</tr>
<tr>
<td style="text-align: left;"> &lt; 8</td>
<td style="text-align: left;">255 (57.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> 8–16</td>
<td style="text-align: left;">162 (36.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 16</td>
<td style="text-align: left;">29 (6.5%)</td>
</tr>
</tbody>
</table>

*SD* standard deviation, *IRQ* inter quartile range

</div>

### EQ-5D summary scores

#### Directly reported versus recalled measurement comparisons

The directly reported mean T1 EQ-5D summary score was 0.482, whereas the recalled T1 EQ-5D summary was 0.453 (*p* \< 0.05) at T2 and 0.363 (*p* \< 0.001) at T3 (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). The directly reported mean T2 EQ-5D summary score was 0.739 and the recalled T2 EQ-5D summary score was 0.713 (*p* = 0\<0.05) at T3 (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). Confidence intervals of the recalled scores were larger than the direct scores. The proportion of respondents that reported exact the same, lower, and higher scores are displayed in Table <a href="#Tab2" data-ref-type="table">2</a>. Absolute individual differences in EQ-5D summary scores between T1 and recalled T1 at T2 ranged from − 0.97 to 1.14; differences between T1 and recalled T1 at T3 ranged from − 1.13 to 1.20; and differences between T2 and recalled T2 at T3 ranged from − 1.13 to 1.33. The recalled EQ-5D summary scores were lower compared to the direct scores in most studied subgroups, except for the group with a low educational level for T2 versus recalled T2 at T3 (Online Resource 1–3). Some of these differences were statistically significant. The differences between the directly reported T1 score and the recalled T1 score at T2 were significantly different in the subgroup of females, the subgroup \< 65 years old, and the subgroup with a middle education level. For the recalled T2 score at T3 differences were significant in the subgroup females, the subgroup \< 65 years old, the subgroup with a middle educational level, the subgroup with comorbidity, and the subgroup with major injury (ISS ≥ 16). The differences between T1 and the recalled T1 at T3 were significantly different for all subgroups.

<figure id="Fig1">
<p><img src="11136_2019_2256_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Mean and confidence interval EQ-5D summary score assessed 1 week (T1) and recall at 3 months (T2: recall T1) and 12 months (T3: recall T1) post-injury; and mean EQ-5D summary score assessed 3 months (T2) and recall at 12 months (T3: recall T2) post-injury. *Statistically significant (<em>p </em>&lt; 0.05)</figcaption>
</figure>

<div id="Tab2" class="table-wrap">

<div class="caption">

Correspondence of directly reported and recalled EQ-5D summary and EQ-VAS assessed 1 week (T1), 3 months (T2), and 12 months (T3) post-injury

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Directly reported = recalled (%)</th>
<th style="text-align: left;">Directly reported &lt; recalled (%)</th>
<th style="text-align: left;">Directly reported &gt; recalled (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">T1–T2 recall</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D summary</td>
<td style="text-align: left;">22.4</td>
<td style="text-align: left;">36.5</td>
<td style="text-align: left;">41.0</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-VAS</td>
<td style="text-align: left;">4.0</td>
<td style="text-align: left;">47.8</td>
<td style="text-align: left;">48.2</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">T1–T3 recall</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D summary</td>
<td style="text-align: left;">16.4</td>
<td style="text-align: left;">28.7</td>
<td style="text-align: left;">54.9</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-VAS</td>
<td style="text-align: left;">5.6</td>
<td style="text-align: left;">40.4</td>
<td style="text-align: left;">54.0</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">T2–T3 recall</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D summary</td>
<td style="text-align: left;">30.5</td>
<td style="text-align: left;">30.7</td>
<td style="text-align: left;">38.8</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-VAS</td>
<td style="text-align: left;">5.8</td>
<td style="text-align: left;">30.9</td>
<td style="text-align: left;">63.2</td>
</tr>
</tbody>
</table>

Directly reported = recalled: respondents filled in exactly the same EQ-5D and EQ-VAS answers for the recall

Directly reported \< recalled: respondents reported higher scores (less problems) when EQ-5D and EQ-VAS were recalled

Directly reported \> recalled: respondents reported lower scores (more problems) when EQ-5D and EQ-VAS were recalled

</div>

#### Correspondence directly reported versus recalled scores

The correspondence was fair (0.40–0.59) for all comparisons (Online Resource 1–3). This was also shown by the Bland–Altman plots (Online Resource 4–6). The ICC was worst for the recalled T1 score at T3 (ICC = 0.518) and best for the recalled T2 score at T3 (ICC = 0.598). Within the subgroups, the correspondence was lowest in the subgroup \< 65 years old (ICC = 0.498) on T1 versus recalled T1 at T2, and the subgroup with a middle education on T1 versus recalled T1 at T3 (ICC = 0.423) and T2 versus recalled T2 at T3 (ICC = 0.483). For T1 versus recalled T1 at T2 the correspondence was highest in the subgroup ≥ 65 years old (ICC = 0.647), for T1 versus recalled T1 at T3 in the subgroup with a low education level (ICC = 0.627), and for T2 versus recalled T2 at T3 in the subgroup with a high educational level (ICC = 0.673).

### EQ-5D dimensions

Directly reported and recalled dimension scores were also compared. The recalled scores for the dimension anxiety were significantly different for all three comparisons (all *p *\< 0.05) (Table <a href="#Tab3" data-ref-type="table">3</a>). Furthermore, the score for the dimension daily activities was significantly different from its direct score on T1 versus recalled T1 at T2 (*p *\< 0.05), and the score for the dimension self-care on T2 versus recalled T2 at T3 (*p *\< 0.05). And all dimension scores, except for daily activity (*p *= 0.197), were significantly different (*p *\< 0.001) on T1 versus recalled T1 at T3. The correspondence was lowest for the dimension anxiety/depression for T1 versus recalled T1 at T2 (ICC = 0.444) and for T1 versus recalled T1 at T3 (ICC = 0.371) and pain/discomfort for T2 versus recalled T2 at T3 (ICC = 0.484). The correspondence was best for mobility on all comparisons (ICC 0.642–0.676).

<div id="Tab3" class="table-wrap">

<div class="caption">

EQ-5D dimension score assessed at 1 week (T1) and recall at 3 months (T2) and at 12 months (T3) post-injury and intraclass correlation coefficients (ICC) (*n* = 446)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">EQ-5D dimension</th>
<th style="text-align: left;"><em>p</em> value</th>
<th style="text-align: left;">ICC (95% CI)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: left;">T1–T2 recall</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility</td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">0.676 (0.62, 0.72)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care</td>
<td style="text-align: left;">0.757</td>
<td style="text-align: left;">0.632 (0.57, 0.68)</td>
</tr>
<tr>
<td style="text-align: left;"> Daily activities</td>
<td style="text-align: left;">0.019*</td>
<td style="text-align: left;">0.520 (0.45, 0.58)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort</td>
<td style="text-align: left;">0.186</td>
<td style="text-align: left;">0.474 (0.40, 0.54)</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression</td>
<td style="text-align: left;">&lt; 0.001*</td>
<td style="text-align: left;">0.444 (0.37, 0.52)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D summary score</td>
<td style="text-align: left;">0.044*</td>
<td style="text-align: left;">0.575 (0.51, 0.63)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-VAS</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">0.578 (0.51, 0.64)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">T1–T3 recall</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility</td>
<td style="text-align: left;">&lt; 0.001*</td>
<td style="text-align: left;">0.642 (0.58, 0.69)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care</td>
<td style="text-align: left;">&lt; 0.001*</td>
<td style="text-align: left;">0.567 (0.50, 0.63)</td>
</tr>
<tr>
<td style="text-align: left;"> Daily activities</td>
<td style="text-align: left;">0.197</td>
<td style="text-align: left;">0.510 (0.44, 0.58)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort</td>
<td style="text-align: left;">&lt; 0.001*</td>
<td style="text-align: left;">0.383 (0.30, 0.46)</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression</td>
<td style="text-align: left;">&lt; 0.001*</td>
<td style="text-align: left;">0.371 (0.29, 0.45)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D summary score</td>
<td style="text-align: left;">&lt;0.001*</td>
<td style="text-align: left;">0.518 (0.45, 0.58)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-VAS</td>
<td style="text-align: left;">0.002*</td>
<td style="text-align: left;">0.561 (0.49, 0.62)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">T2–T3 recall</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility</td>
<td style="text-align: left;">0.831</td>
<td style="text-align: left;">0.655 (0.60, 0.71)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care</td>
<td style="text-align: left;">0.004*</td>
<td style="text-align: left;">0.513 (0.44, 0.58)</td>
</tr>
<tr>
<td style="text-align: left;"> Daily activities</td>
<td style="text-align: left;">0.766</td>
<td style="text-align: left;">0.554 (0.49, 0.62)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort</td>
<td style="text-align: left;">0.511</td>
<td style="text-align: left;">0.484 (0.41, 0.55)</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression</td>
<td style="text-align: left;">0.031*</td>
<td style="text-align: left;">0.523 (0.45, 0.59)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D summary score</td>
<td style="text-align: left;">0.022*</td>
<td style="text-align: left;">0.598 (0.54, 0.65)</td>
</tr>
<tr>
<td style="text-align: left;"> EQ-VAS</td>
<td style="text-align: left;">&lt; 0.001*</td>
<td style="text-align: left;">0.595 (0.53, 0.65)</td>
</tr>
</tbody>
</table>

*ICC* Intraclass correlation coefficient

\**p *\< 0.05

</div>

### EQ-VAS

#### Directly reported versus recalled measurement comparisons

The directly reported mean T1 EQ-VAS score was 56.3, the recalled T1 EQ-VAS score was 55.4 (*p *= 0.304) at T2 and 53.3 (*p *\< 0.05) at T3 (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). The directly reported mean T2 EQ-VAS score was 72.5 and the recalled T2 score was 68.0 (*p *\< 0.001) at T3 (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). Confidence intervals of the recalled scores were larger than of the directly reported scores. The proportion of respondents that reported the exact same, lower and higher scores are displayed in Table <a href="#Tab2" data-ref-type="table">2</a>. Absolute individual differences in EQ-VAS scores between T1 and recalled T1 at T2 ranged between − 99 and 57; differences between T1 and recalled T1 at T3 ranged between − 100 and 70; and differences between T2 and recalled T2 at T3 ranged between − 76 and 90. Recalled EQ-VAS scores were lower than the directly reported EQ-VAS scores, except for the subgroup 65 + for T1 versus recalled T1 at T2 and for T1 versus recalled T1 at T3, and the subgroup with low education on T2 versus recalled T2 at T3. Subgroup results are presented in Online Resource 7–9. Comparing the recalled T1 at T2 with the directly reported T1 resulted in no statistical differences, except for the subgrou*p *\< 65 years old (*p *\< 0.05) and the subgroup with middle level of education (*p *\< 0.05), while the directly reported T2 EQ-VAS and recalled T2 EQ-VAS at T3 was statistically significant different for all subgroups, except for the subgroup with low level of education. For the recalled T1 EQ-VAS at T3, about half of the subgroups showed statistical significant differences between the directly reported and the recalled EQ-VAS (Online Resource 8).

<figure id="Fig2">
<p><img src="11136_2019_2256_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Mean and confidence interval EQ-VAS score assessed 1 week (T1) and recall at 3 months (T2: recall T1) and 12 months (T3: recall T1) post-injury; and mean EQ-VAS score assessed 3 months (T2) and recall at 12 months (T3: recall T2) post-injury. *Statistically significant (<em>p </em>&lt; 0.05)</figcaption>
</figure>

#### Correspondence directly reported versus recalled scores

The correspondence between directly reported and recalled EQ-VAS scores was fair on all time points (ICC 0.561–0.595) (Online Resource 10–12). The correspondence was lowest for T1 versus recalled T1 at T3 (ICC = 0.561), slightly better for T1 versus recalled T1 at T2 (ICC = 0.578) and highest for T2 versus recalled T2 at T3 (ICC = 0.595). Within the subgroups, the correspondence was lowest in the subgroup with a high ISS for T1 versus recalled T1 at T2 (ICC = 0.188) and T1 versus recalled T1 at T3 (ICC = 0.292) and in the subgroup with a middle educational level for T2 versus recalledT2 at T3 (ICC = 0.512), resembling EQ-5D summary score results. The correspondence was best in the subgroup females for T1 versus recalled T1 at T2 (ICC = 0.636), and in the subgroup with a high educational level for T1 versus recalled T1 at T3 (ICC = 0.652) and T2 versus recalled T2 at T3 (ICC = 0.703).

## Discussion

This study explored the recall effects of HRQL assessment in a large heterogeneous sample of trauma patients. The results showed that recalled HRQL measured by the EQ-5D-3L and EQ-VAS is systematically lower compared to the directly reported HRQL of trauma patients, with a general decrease over time. The relative size of measurement error and bias was larger in EQ-5D-3L summary scores than in EQ-VAS. Most distortion in recalled HRQL was present in the dimensions anxiety/depression and pain/discomfort. The correspondence between directly reported and recalled scores decreased with the time between measurements, and it was influenced by the post-injury phase being recalled: correspondence was better when T2 (3-months post-injury; recovery phase) was recalled compared to when T1 (1-week post-injury; acute phase) was recalled. Patients with a major injury and those with a middle level of education had most difficulties with recalling their prior HRQL, whereas patients with a high educational level were in general best in recalling their prior HRQL.

Our study showed in general fair correspondence between directly reported and recalled HRQL. This is in line with earlier studies on HRQL recall that showed that the association between recalled HRQL and prospective reports of HRQL was moderate \[13\]. This was the case in patients with prostate cancer \[16, 17\] as well as in older hospital patients \[15\]. Two studies on recall of pre-surgery HRQL in prostate cancer found correlations between 0.39 and 0.57 for scores collected before and six to 37 months after surgery \[16, 17\]. In the study of McPhail et al., elderly hospitalized patients reported their HRQL within 3 days of admission and immediately prior to discharge (median hospital stay of 38 days). This study found a poor recall correspondence (ICC of 0.34 for EQ-5D summary score and 0.40 for EQ-VAS) \[15\]. However, as opposed to the results of these studies, a study in patients with hip arthroplasty found good to excellent correspondence of pre-surgery HRQL scores obtained before surgery and 3 days (ICC 0.8–0.9), 6 weeks (ICC 0.7–0.9), and 3 months (ICC 0.85–0.95) post-surgery \[18\]. Results on recall correspondence are thus scarce and seem to depend on the condition that is being recalled as well as on the time frame between the assessments. Earlier studies investigated the test–retest reliability of the EQ-5D-3L. These studies showed that the accuracy of the EQ-5D-3L differed, depending on the timeframe, EQ-5D-3L utility or VAS used, and study population and ranged from 0.70 to 0.85 \[28–31\]. The correspondence between directly reported and recalled HRQL based on the EQ-5D-3L found in our study is much lower, as we expected, since correspondence between directly reported and recalled HRQL cannot be more accurate than the reliability of the instrument. However, it should be noted that test–retest reliability of the EQ-5D-3L was not yet studied in trauma patients and therefore we were not able to compare the correspondence found against the accuracy of the instrument in trauma patients.

As opposed to our hypothesis that a scale with a wider range of response options like the EQ-VAS is easier distorted than a classification-like scale with a limited number of response options, like the EQ-5D-3L \[13\], our findings showed lower ICC scores on the EQ-5D-3L compared to the EQ-VAS. This was also seen in the study of McPhail et al. where the ICC score of the EQ-VAS was higher than the score of the EQ-5D summary (0.40 vs. 0.34) \[15\]. In view of these results, we reject our hypothesis as the EQ-VAS seems to be less distorted compared to the EQ-5D-3L.

Also, the time interval between the initial measurement and the recall moment was seen to influence the correspondence of recall; however, results were partly in contrast with our hypothesis. As expected, recalled scores of 1 week post-trauma differed more from the directly reported scores when recalled at 12 months post-injury compared to 3 months post-injury. This is in line with earlier studies that showed that the correspondence of recall decreases with the time between the initial measurement and the recalled moment \[10\]. However, despite the longer time of 9 months between the initial assessment at 3 months and the recall assessment at 12 months, the correspondence between T2 and T3 was higher (highest ICC rates) compared to the T1 and T2. This seems to indicate that apart from the follow-up time, also the post-injury phase influences the correspondence between directly reported and recalled scores. In the acute phase (1 week post-injury), there are rapid changes in health, which may impede recall, whereas the health state in the recovery phase (3 to 12 months post-injury) may be more comparable to the current health state and therefore easier to remember. These findings are interesting to study further in future studies, for example, to see how a 2-year time period affects the recalled outcomes.

Different subgroups of patients had a different degree of correspondence between the directly measured and recalled HRQL. As hypothesized, patients with a major trauma (ISS ≥ 16) had lower correspondence. This may be due to the severity of the trauma and possibly also due to neurologic complications many of them suffered from. The type and severity of injury thus also seem to influence the correspondence of recall. Also, patients with a middle level of education were among the groups with the lowest correspondence between directly measured and recalled, whereas correspondence was high among patients with a high level of education. To the best of our knowledge, no other studies have investigated whether the correspondence between directly measured and recalled HRQL is different among subgroups based on level of education.

Our finding that recalled EQ-5D-3L and EQ-VAS is systematically lower compared to the directly reported HRQL of trauma patients may have implications for the application of recalled EQ-5D in cost-effectiveness studies. The EQ-5D-3L is a widely applied HRQL instrument for QALY estimations and in cost-effectiveness analyses; however, systematic bias in retrospective assessment, resulting in larger differences in EQ-5D summary scores between two assessments compared to directly reported EQ-5D, can influence cost-effectiveness analyses, and therefore, use of recalled HRQL assessment can potentially lead to inefficiencies in resource allocation.

### Strengths and limitations

This study had several strengths and limitations. Strengths include the sample size of our study, which was large enough to test for differences between different subgroups of trauma patients, and the assessment of the directly reported and recalled HRQL on several time points and with different timeframes between assessments to evaluate both assessment points and follow-up times. Another strength is the inclusion of both the EQ-5D dimensions and the EQ-VAS, which allowed us to compare a classification-like scale with a more subjective scale. Limitations include the potential selection and participation bias and the use of the EQ-5D-3L instrument instead of the 5L version. A low proportion (\< 10%) of all invited trauma patients participated in the study and filled in the various EQ-5D surveys at all assessment points. Therefore, our results may not fully reflect the Dutch trauma population. The EQ-5D-3L, the three answer option instrument, is less sensitive than the more comprehensive EQ-5D-5L version (five answer options). The recall correspondence is expected to be less accurate when more answer options are present. It might be valuable to test the recall correspondence of the EQ-5D-5L in future research.

## Conclusion

Our study showed that recalled HRQL measured by the EQ-5D-3L and EQ-VAS is systematically lower compared to the directly reported HRQL of trauma patients, with a general decrease over time. This indicates that recalled HRQL cannot be used as a replacement for prospectively assessed HRQL. If it is difficult or impossible to collect HRQL data prospectively, retrospective assessment is an option; however, when applying retrospective assessment, researchers should be aware that systematic bias may occur. Our study showed better correspondence for the EQ-VAS compared to the EQ-5D summary score, indicating that the EQ-5D descriptive system is more prone to systematic bias than EQ-VAS. Besides, patient characteristics, injury severity, subjectivity of the dimension, and time interval also influence correspondence between directly reported and recalled HRQL.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary material 1 (PDF 575 kb)

</div>

### Funding

This study was funded by EuroQol (Grant Number: EQ Project 2016160).

### Compliance with ethical standards

#### Conflict of interest

All authors declare that they have no conflict of interest.

#### Ethical approval

All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki Declaration and its later amendments or comparable ethical standards.

#### Informed consent

Informed consent was obtained from all individual participants included in the study.

## References

1. Bakas T, McLennon SM, Carpenter JS, Buelow JM, Otte JL, Hanna KM, Ellett ML, Hadler KA, Welch JL. Systematic review of health-related quality of life models. Health and Quality of Life Outcomes. 2012;10(1):134. doi:10.1186/1477-7525-10-134

2. Sullivan M. The new subjective medicine: Taking the patient’s point of view on health care and health. Social Science and Medicine. 2003;56(7):1595–1604. doi:10.1016/S0277-9536(02)00159-4

3. Bouillon B, Kreder H. Quality of life in patients with multiple injuries–basic issues, assessment, and recommendations. Restor Neurol Neurosci. 2002;20(3–4):125–134.

4. Meyer T, Richter S, Raspe H. Agreement between pre-post measures of change and transition ratings as well as then-tests. BMC Medical Research Methodology. 2013;13(1):52. doi:10.1186/1471-2288-13-52

5. Gabbe BJ, Simpson PM, Harrison JE, Lyons RA, Ameratunga S, Ponsford J, Fitzgerald M, Judson R, Collie A, Cameron PA. Return to work and functional outcomes after major trauma. Annals of Surgery. 2016;263(4):623–632. doi:10.1097/SLA.0000000000001564

6. Blome C, Augustin M. Measuring change in quality of life: Bias in prospective and retrospective evaluation. Value Health. 2015;18(1):110–115. doi:10.1016/j.jval.2014.10.007

7. Schwartz CE, Sprangers MA. Guidelines for improving the stringency of response shift research using the thentest. Quality of Life Research. 2010;19(4):455–464. doi:10.1007/s11136-010-9585-9

8. McClimans L, Bickenbach J, Westerman M, Carlson L, Wasserman D, Schwartz C. Philosophical perspectives on response shift. Quality of Life Research. 2013;22(7):1871–1878. doi:10.1007/s11136-012-0300-x

9. Schwartz CE, Bode R, Repucci N, Becker J, Sprangers MA, Fayers PM. The clinical significance of adaptation to changing health: A meta-analysis of response shift. Quality of Life Research. 2006;15(9):1533–1550. doi:10.1007/s11136-006-0025-9

10. Schmier JK, Halpern MT. Patient recall and recall bias of health state and health status. Expert Review of Pharmacoeconomics & Outcomes Research. 2004;4(2):159–163. doi:10.1586/14737167.4.2.159

11. Sprangers MAG, Schwartz CE. Integrating response shift into health-related quality of life research: A theoretical model. Social Science and Medicine. 1999;48(11):1507–1515. doi:10.1016/S0277-9536(99)00045-3

12. Schwartz CE, Sprangers MAG. Methodological approaches for assessing response shift in longitudinal health-related quality-of-life research. Social Science and Medicine. 1999;48(11):1531–1548. doi:10.1016/S0277-9536(99)00047-7

13. Stull DE, Leidy NK, Parasuraman B, Chassany O. Optimal recall periods for patient-reported outcomes: Challenges and potential solutions. Current Medical Research and Opinion. 2009;25(4):929–942. doi:10.1185/03007990902774765

14. Wicklund RA, Brehm JW. Perspectives on cognitive dissonance. 2013. New York, Psychology Press.

15. McPhail S, Haines T. Response shift, recall bias and their effect on measuring change in health-related quality of life amongst older hospital patients. Health and Quality of Life Outcomes. 2010;8(1):65. doi:10.1186/1477-7525-8-65

16. Karakiewicz P, Shariat SF, Naderi A, Kadmon D, Slawin KM. Reliability of remembered International Index of Erectile Function domain scores in men with localized prostate cancer. Urology. 2005;65(1):131–135. doi:10.1016/j.urology.2004.08.054

17. Litwin MS, McGuigan KA. Accuracy of recall in health-related quality-of-life assessment among men treated for prostate cancer. Journal of Clinical Oncology. 1999;17(9):2882. doi:10.1200/JCO.1999.17.9.2882

18. Howell J, Xu M, Duncan CP, Masri BA, Garbuz DS. A comparison between patient recall and concurrent measurement of preoperative quality of life outcome in total hip arthroplasty. Journal of Arthroplasty. 2008;23(6):843–849. doi:10.1016/j.arth.2007.07.020

19. de Jongh MAC, Kruithof N, Gosens T, van de Ree CLP, de Munter L, Brouwers L, Polinder S, Lansink KWW. Prevalence, recovery patterns and predictors of quality of life and costs after non-fatal injury: The brabant injury outcome surveillance (BIOS) study. Injury Prevention. 2017;23(1):59. doi:10.1136/injuryprev-2016-042032

20. Mosby. Mosby’s Medical Dictionary. 2012. Mosby, St. Louis.

21. Rabin R, Charro FD. EQ-SD: A measure of health status from the EuroQol Group. Annals of Medicine. 2001;33(5):337–343. doi:10.3109/07853890109002087

22. Dolan P. Modeling valuations for EuroQol health states. Medical Care. 1997;35(11):1095–1108. doi:10.1097/00005650-199711000-00002

23. Brooks R, Group E. EuroQol: The current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

24. Gennarelli TA, Wodzin E. AIS 2005: A contemporary injury scale. Injury. 2006;37(12):1083–1091. doi:10.1016/j.injury.2006.07.009

25. Boyd CR, Tolson MA, Copes WS. Evaluating trauma care: The TRISS method. Trauma Score and the Injury Severity Score. Journal of Trauma. 1987;27(4):370–378. doi:10.1097/00005373-198704000-00005

26. Bartko JJ. The intraclass correlation coefficient as a measure of reliability. Psychological Reports. 1966;19(1):3–11. doi:10.2466/pr0.1966.19.1.3

27. Cicchetti DV. Guidelines, criteria, and rules of thumb for evaluating normed and standardized assessment instruments in psychology. Psychological Assessment. 1994;6(4):284. doi:10.1037/1040-3590.6.4.284

28. Fisk J, Brown M, Sketris I, Metz L, Murray T, Stadnyk K. A comparison of health utility measures for the evaluation of multiple sclerosis treatments. Journal of Neurology, Neurosurgery and Psychiatry. 2005;76(1):58–63. doi:10.1136/jnnp.2003.017897

29. Fitzpatrick R, Davey C, Buxton MJ, Jones DR. Evaluating patient-based outcome measures for use in clinical trials. Health Technology Assessment. 1998;2(14):1–74. doi:10.3310/hta2140

30. Hurst N, Kind P, Ruta D, Hunter M, Stubbings A. Measuring health-related quality of life in rheumatoid arthritis: Validity, responsiveness and reliability of EuroQol (EQ-5D). British Journal of Rheumatology. 1997;36(5):551–559. doi:10.1093/rheumatology/36.5.551

31. Slobogean GP, Noonan VK, O’Brien PJ. The reliability and validity of the disabilities of arm, shoulder, and hand, EuroQol-5D, health utilities index, and short form-6D outcome instruments in patients with proximal humeral fractures. Journal of Shoulder and Elbow Surgery. 2010;19(3):342–348. doi:10.1016/j.jse.2009.10.021

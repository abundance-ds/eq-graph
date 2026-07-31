---
project_id: "1654-TVG"
work_id: "doi:10.1007/s10198-024-01710-1"
doi: "10.1007/s10198-024-01710-1"
pmid: "39066840"
pmcid: "PMC11937211"
title: "Psychometric validation of the Chinese versions of EQ-5D-Y-3L and the experimental EQ-TIPS in children and adolescents with COVID-19"
journal: "The European Journal of Health Economics"
publication_date: "2024-07-27"
volume: "26"
issue: "3"
authors:
  - name: "Wenjing Zhou"
    orcid: "http://orcid.org/0000-0003-0770-4564"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Yaqin Li"
    affiliation_ids:
      - "Aff1"
  - name: "Jan Busschbach"
    orcid: "http://orcid.org/0000-0002-8602-0381"
    affiliation_ids:
      - "Aff2"
  - name: "Michael Herdman"
    affiliation_ids:
      - "Aff3"
  - name: "Zhihao Yang"
    orcid: "http://orcid.org/0000-0001-5468-0847"
    affiliation_ids:
      - "Aff4"
  - name: "Yanming Lu"
    orcid: "http://orcid.org/0009-0008-6782-4182"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/0220qvk04grid.16821.3c0000 0004 0368 8293Department of Paediatrics, Renji Hospital, School of Medicine, Shanghai Jiaotong University, No. 2000, Jiangyue Road, Shanghai, China"
  - id: "Aff2"
    name: "https://ror.org/018906e22grid.5645.20000 0004 0459 992XDepartment of Psychiatry, Section Medical Psychology and Psychotherapy, Erasmus Medical Center, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "https://ror.org/01tgyzw49grid.4280.e0000 0001 2180 6431Saw Swee Hock School of Public Health, National University of Singapore, Singapore, Singapore"
  - id: "Aff4"
    name: "https://ror.org/035y7a716grid.413458.f0000 0000 9330 9891Health Services Management Department, Guizhou Medical University, Guiyang, China"
keywords:
  - "COVID-19"
  - "EQ-5D-Y-3L"
  - "EQ-TIPS"
  - "Health-related quality of life"
  - "I19"
  - "Validation"
licence: "cc-by"
source_file: "input/projects/1654-TVG/papers/doi_10.1007_s10198-024-01710-1.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11937211/fullTextXML"
source_method: "epmc_xml"
source_sha256: "fbfa00b6b8d3552027a8ff1492f54f9087f80b767856f57817b64c7a6747a73b"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Psychometric validation of the Chinese versions of EQ-5D-Y-3L and the experimental EQ-TIPS in children and adolescents with COVID-19

## Abstract

### Objectives

Respiratory infectious diseases like COVID-19 profoundly impacts the health of children and adolescents, but validated instruments to measure their impacts on health-related quality of life (HRQoL) are lacking. The EQ-5D-Y-3L, widely used for youth HRQoL, now features a Chinese value set. The experimental EQ-TIPS addresses HRQoL assessment for toddlers and infants. This study tested the psychometric properties of both instruments in paediatric COVID-19 patients, and compared the performance of self-complete and proxy EQ-5D-Y-3L.

### Methods

This longitudinal study recruited 861 COVID-19 patients aged 0–18 years and their parental caregivers, with 311 dyads completing the follow-up. Digital administration included the EQ-TIPS, the EQ-5D-Y-3L, and Overall Health Assessment (OHA). Controls comprised 231 healthy children. Analysis encompassed known-group validity, child-parent agreement, and responsiveness to change in disease severity and OHA.

### Results

COVID-19 children exhibited lower HRQoL than non-infected peers. The EQ-TIPS and the EQ-5D-Y-3L distinguished groups by disease presence, severity and symptoms, showing moderate to good known-group validity (ESs: 0.45–1.39 for EQ-TIPS, 0.44–1.91 for self-complete EQ-5D-Y-3L, and 0.32–1.67 for proxy EQ-5D-Y-3L). Child-parent agreement was moderate to good for EQ-5D-Y-3L (ICC: 0.653–0.823; Gwet’s AC1: 0.470–0.738), and responsiveness was good for both EQ-TIPS Level Sum Score (LSS) (ESs: 1.21–1.39) and EQ-5D-Y-3L index scores (ESs: 1.00–1.16).

### Conclusions

This study demonstrates the reliability, validity, and responsiveness of the experimental EQ-TIPS and the EQ-5D-Y-3L in paediatric COVID-19 patients. It is the first evidence of the EQ-TIPS’ responsiveness, supporting its use in assessing the impact of COVID-19 on paediatric HRQoL.

## Introduction

As of April 30, 2023, the World Health Organization (WHO) has reported over 765 million confirmed COVID-19 cases and 6.9 million deaths worldwide \[1\]. Beyond pulmonary complications and deaths, COVID-19 can impact the physical, emotional, and social well-being of children and adolescents, with increased rates of anxiety and depressive symptoms observed from ages 7 to 17 \[2\]. Longitudinal studies have indicated that COVID-19 impacts on physical and school-related aspects in adolescents aged ≥ 14 years \[3\]. Notably, research focusing on the vulnerable age group of birth to three years is scarce, despite their developmental stage and reliance on carers. A single study of infants and toddlers with atopic dermatitis found significantly worse HRQoL during the pandemic, underscoring the need for further research in this age group \[4\]. Furthermore, recruiting a population with COVID-19 not only offers insights into the direct effects of the disease but also presents a unique opportunity to study a diverse range of symptom severities among younger children, thus providing valuable data to understand the full spectrum of the pandemic’s impact on paediatric populations. However, existing generic HRQoL instruments which have been used to assess HRQoL in children and adolescents affected by COVID-19, such as KIDSCREEN-10, PedsQL 4.0, and KINDL-R questionnaire \[5–7\], lack societal preference-based scores which can be used in economic evaluations.

The EQ-5D-Y-3L is a widely used quality of life instrument for children and adolescents \[8\], which comes with a preference-based measures index score that can be used to calculate the Quality-Adjusted Life Years (QALYs). This provides insights into healthcare resource utilization and costs related to children’s HRQoL impact. There are different administration versions of EQ-5D-Y-3L, the self-complete and the proxy version. The ‘proxy version’ is crucial for parental evaluation when children cannot self-rate. For children aged 4–7 years, a proxy version should be used. In children aged over eight years, the self-complete version is generally recommended \[9\]. Despite demonstrating good reliability, validity, and responsiveness in paediatric patients with severe pneumonia and other respiratory conditions \[10, 11\], it lacks specific psychometric assessment for younger populations affected by COVID-19. Efforts in developing the Chinese EQ-5D-Y-3L value sets demand evaluation \[12\], especially for known-group validity and responsiveness in head-to-head studies \[13–15\]. Moreover, Studies indicate parents of children with COVID-19 or other infections may underestimate their child’s HRQoL \[10, 16\], underscore the importance of examining agreement and discordance between self-complete and proxy versions \[9\].

The experimental version of EQ-TIPS (EQ Toddler and Infant populations questionnaire), developed in 2018, assesses the physical, mental, emotional, and social functions of children aged 0 to 36 months \[17\]. Although currently in the experimental phase with no definitive version or available value sets, the EQ-TIPS has shown good construct validity in young children who have undergone general surgery, burn injury, or cardiac surgery \[18\]. However, additional research is needed to explore other properties, including reliability (examined in a small sample of the general population) \[19\], feasibility, and clinical utility. This research will be useful in moving the experimental EQ-TIPS towards an approved version, particularly with regard to cross-cultural validity.

During the COVID-19 pandemic in China, an opportunity arose to test the psychometric properties of the EQ-5D-Y-3L and the experimental EQ-TIPS in paediatric patients with this condition, utilizing the newly published Chinese value sets with the Y-3L. Therefore, this study had three objectives. First, to assess the validity, inter-rater reliability, and responsiveness of the self-complete version of the EQ-5D-Y-3L in children and adolescents aged 4–18 years. Second, to compare outcomes between the self-complete and proxy versions of the EQ-5D-Y-3L in those aged 6–18 years. Finally, to evaluate the distributional properties, known-group validity, and responsiveness of the experimental EQ-TIPS in children with COVID-19 aged under four years.

## Methods

### Sampling

This was a descriptive, longitudinal, prospective study with a repeated measures designed to test for reliability, validity and responsiveness of the instruments. We recruited paediatric inpatients and outpatients with confirmed COVID-19 infection and treated at Renji Academic Hospital in Shanghai from May 2022 to January 2023, along with their parental carers. A control group, consisting of infants, children and adolescents testing negative for COVID-19 tests with no related symptoms, was recruited using a ‘snowball approach’, primarily by reaching out to the siblings and friends of the patients.

For paediatric patients, the inclusion criteria were: (1) aged between 0 and 18 years; (2) confirmed COVID-19 infection through PCR (Polymerase Chain Reaction) or antigen test; (3) newly diagnosed by a specialist within the past month, without prior infection; and (4) admitted as inpatients or receiving outpatient care. Individuals aged 6–18 years, proficient in Chinese, and capable of independent questionnaire completion were eligible for the self-complete version. Those with other known respiratory viral infections within the preceding three months or known chronic health conditions were excluded.

For non-infected children and adolescents in the control group, the inclusion criteria were as follows: aged 0–18 years, no history of confirmed COVID-19 infection based on negative PCR or antigen test results, and generally healthy with no illnesses or symptoms suggestive of COVID-19 in the past three months. Exclusions applied to individuals not well enough to complete surveys or lacking written informed consent from legal guardians.

For carers, inclusion criteria were: (1) a primary carer was present in the week before the survey for the eligible child, (2) parent of an eligible child respondent, (3) physically present during the outpatient visit or admission, and (4) cognitively able to complete the surveys. The study received approval from the institutional medical ethical review board of Guizhou Medical University (Approval number: GMU2022303).

### Instruments

The EQ-5D-Y-3L assesses HRQoL with five dimensions (mobility; looking after myself; doing usual activities; having pain or discomfort; and feeling worried, sad, or unhappy) and three severity levels. Each health state in the EQ-5D-Y-3L can be summarized using level descriptors, generating 243 (3<sup>5</sup>) unique states. The best state, 11,111, indicates ‘no problems’ in any dimension, while the worst state, 33,333, indicates ‘a lot of problems’ in all dimensions. An index score of 1.0 represent the value of full health, and a score of 0.0 the value of death. Negative values represent health states with values below the value of death. The collection of index scores for all possible states is called a ‘value set’. It includes a 20-cm visual analogue scale (EQ VAS) for overall health rating \[20\]. We used proxy version 1 in this study, involving caregivers providing their impression of the child’s health on the survey day \[9\].

The experimental version of EQ-TIPS, completed by the primary caregiver or parent, assesses six dimensions: movement; play; pain; social interaction; communication; and eating. Like the EQ-5D-Y-3L, each dimension has three severity levels, forming a 6-digit code with 729 (3<sup>6</sup>) unique health states. The best state is 111,111. The EQ VAS is also included. In this study, the EQ-TIPS assessed HRQoL for children aged under four years old, as the EQ-5D-Y-3L proxy version is recommended for those aged four years and older \[9\].

The Chinese versions of EQ-5D-Y-3L and the experimental EQ-TIPS underwent translation per EuroQol Group guidelines \[21\]. Observations from previous surveys revealed a tendency for respondents to omit the impact of COVID-19, likely due to fluctuating conditions in many patients. Therefore, we proposed slight modifications to the instructions of the EQ-5D-Y-3L and the EQ-TIPS. Specifically, we added a short phrase before the original instructions as follows: (1) For the baseline survey completed by proxies: In comparison to the situation before the outbreak of the pandemic, please tick the ONE box that you think best describes the child’s health TODAY; (2) For the follow-up survey completed by proxies: In comparison to the situation during the outbreak of the pandemic, please tick the ONE box that you think best describes the child’s health TODAY; (3) For the self-completed version of EQ-5D-Y-3L: Taking into account the impact of the coronavirus pandemic, please tick the ONE box that you think best describes your health TODAY. The modification was approved by the EuroQol Research Foundation for use in the current study.

The Overall Health Assessment question (OHA), a valid measure of subjective health in children and adolescents \[22\], was phrased as ‘How is your overall health today? Is it excellent, good, fair, poor, or very poor?’ The proxy version gathered the caregiver’s impression of the patient’s overall health on the survey day.

The Chinese COVID-19 severity criteria were: (1) Mild: respiratory symptoms and fever; (2) Moderate: persistent high fever, cough, shortness of breath, with pneumonia imaging; (3) Severe: includes indicators such as high fever, tachypnoea, low oxygen saturation, respiratory distress, altered consciousness, and feeding difficulties \[23\].

Clinical recovery from COVID-19 was defined as having normal body temperature for over 3 days; mostly disappeared or significantly improved symptoms; significant absorption of pneumonia lesions on follow-up CT scan (if present); and either two consecutive negative RT-PCR tests, RT-PCR cycle threshold value ≥ 35, or three consecutive negative antigen tests \[23\].

### Procedures

All consenting patients and parents independently completed the baseline survey using tablets in clinics or wards on the hospital admission day or during outpatient visits. Healthy children and adolescents, along with their parents, completed the survey at home using a smartphone. For children aged 4–18 years, parental carers provided sociodemographic information and completed the EQ-5D-Y-3L questionnaire (digital proxy version, including EQ-VAS), a five-point overall health assessment (OHA) question (proxy version), and questions on the parent’s demographics and the latest COVID-19 test result. For children under four years, the EQ-TIPS was used instead of the EQ-5D-Y-3L (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

The survey for children and adolescents aged over six years included the digital self-complete version of the EQ-5D-Y-3L, EQ VAS, and OHA question. Participants were invited to complete the same questionnaire during follow-up visits to outpatient clinics or on the day of discharge. Follow-up survey forms mirrored baseline forms, excluding demographic questions. On the survey day, the patient’s attending clinician completed the medical record including COVID-19 manifestations, disease duration, complications, severity per Chinese COVID-19 guidelines \[23\], and treatment.

<figure id="Fig1">
<p><img src="10198_2024_1710_Fig1_HTML.jpg" id="d33e391" /></p>
<figcaption>Flow chart of the study from recruitment of children and their parent carers</figcaption>
</figure>

### Data analysis

We calculated descriptive statistics to summarize demographic, socioeconomic, and clinical characteristics. The construct validity, inter-rater agreement, and responsiveness of the EQ-TIPS and the EQ-5D-Y-3L dimensions and summary scores (EQ index score, level sum score and EQ VAS) were assessed.

For EQ-5D-Y-3L: the index score and EQ VAS were generated separately for self-complete (≥ six years) and proxy versions, using the Chinese EQ-5D-Y-3L value set \[12\]. The index score ranges from − 0.088 to 1, with higher values indicating better health utility.

For EQ-TIPS: as no preference-based scoring is available, a level sum score (LSS) was employed to summarize responses on the descriptive system. Numeric values ranged from 6 (no problems on all six dimensions: 1 + 1 + 1 + 1 + 1 + 1 = 6) to 18 (most severe score: level 3 on all dimensions: 3 + 3 + 3 + 3 + 3 + 3 = 18) \[24\].

We evaluated known-group validity by comparing summary scores across four health status categories at baseline: 1) with or without COVID-19; 2) three grades of disease severity of COVID-19 (mild, moderate, or severe); 3) presence of two or more symptoms versus none or one symptom. Appendix Table <a href="#Taba" data-ref-type="table">1</a> provides a detailed breakdown of the symptoms observed in our study population, allowing for a clearer understanding of how symptom presence correlates with disease severity; and 4) ‘excellent’/’good’ versus ‘fair’/’poor’/’very poor’ oral health assessment (OHA). Our hypothesis predicted higher EQ-5D-Y-3L index scores and EQ VAS, as well as lower EQ-TIPS LSS, in ‘good’ health groups compared to ‘poor’ health groups. We used independent t-tests, and ANOVA for comparisons, with Cohen’s D effect size (ES = difference of mean/ pooled SD) indicating the relative efficiency in discriminating between patients with different health conditions \[25\]. Individual dimension-level distribution analysis employed Chi-square test, and Fisher’s exact test if any cell had expected count less than 5.

<div id="Tab1" class="table-wrap">

<div class="caption">

Descriptive statistics of the sample (*n* = 1092)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">EQ-TIPS sample</th>
<th colspan="5" style="text-align: left;">EQ-5D-Y-3L sample</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">COVID-19<br />
<em>n</em> = 230</th>
<th colspan="2" style="text-align: left;">Non-infected <em>n</em> = 77</th>
<th style="text-align: left;"><em>p</em> value</th>
<th colspan="2" style="text-align: left;">COVID-19<br />
<em>n</em> = 631</th>
<th colspan="2" style="text-align: left;">Non-infected <em>n</em> = 154</th>
<th style="text-align: left;"><em>p</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11" style="text-align: left;"><em>Children</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Age (month/year)</em>,<em> mean (SD)</em></td>
<td style="text-align: left;">2.2</td>
<td style="text-align: left;">(1.1)</td>
<td style="text-align: left;">2.0</td>
<td style="text-align: left;">(1.1)</td>
<td style="text-align: left;">0.315</td>
<td style="text-align: left;">8.7</td>
<td style="text-align: left;">(3.3)</td>
<td style="text-align: left;">8.8</td>
<td style="text-align: left;">(2.9)</td>
<td style="text-align: left;">0.561</td>
</tr>
<tr>
<td style="text-align: left;"> 0-12mo (EQ-TIPS)/4–5 year (EQ-5D-Y-3L), % (n)</td>
<td style="text-align: left;">19.6</td>
<td style="text-align: left;">(45)</td>
<td style="text-align: left;">22.1</td>
<td style="text-align: left;">(17)</td>
<td rowspan="3" style="text-align: left;">0.086</td>
<td style="text-align: left;">23.4</td>
<td style="text-align: left;">(148)</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;">(27)</td>
<td rowspan="3" style="text-align: left;">0.197</td>
</tr>
<tr>
<td style="text-align: left;"> 13-24mo (EQ-TIPS)/6–11 year (EQ-5D-Y-3L), % (n)</td>
<td style="text-align: left;">17.0</td>
<td style="text-align: left;">(39)</td>
<td style="text-align: left;">27.3</td>
<td style="text-align: left;">(21)</td>
<td style="text-align: left;">60.1</td>
<td style="text-align: left;">(379)</td>
<td style="text-align: left;">64.9</td>
<td style="text-align: left;">(100)</td>
</tr>
<tr>
<td style="text-align: left;"> 25-48mo (EQ-TIPS)/12–18 year (EQ-5D-Y-3L), % (n)</td>
<td style="text-align: left;">63.5</td>
<td style="text-align: left;">(146)</td>
<td style="text-align: left;">50.6</td>
<td style="text-align: left;">(39)</td>
<td style="text-align: left;">16.5</td>
<td style="text-align: left;">(104)</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;">(27)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Sex</em>,<em> % (n)</em></td>
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
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">52.6</td>
<td style="text-align: left;">(121)</td>
<td style="text-align: left;">53.2</td>
<td style="text-align: left;">(41)</td>
<td rowspan="2" style="text-align: left;">0.923</td>
<td style="text-align: left;">52.8</td>
<td style="text-align: left;">(333)</td>
<td style="text-align: left;">57.8</td>
<td style="text-align: left;">(89)</td>
<td rowspan="2" style="text-align: left;">0.263</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">47.4</td>
<td style="text-align: left;">(109)</td>
<td style="text-align: left;">46.8</td>
<td style="text-align: left;">(36)</td>
<td style="text-align: left;">47.2</td>
<td style="text-align: left;">(298)</td>
<td style="text-align: left;">42.2</td>
<td style="text-align: left;">(65)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Disease duration</em></td>
<td style="text-align: left;">10.0</td>
<td style="text-align: left;">(9.8)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">11.6</td>
<td style="text-align: left;">(10.6)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><em>Numbers of symptoms</em></td>
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
<td style="text-align: left;"> 0/1</td>
<td style="text-align: left;">20.4</td>
<td style="text-align: left;">(47)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">22.7</td>
<td style="text-align: left;">(143)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> More than 2</td>
<td style="text-align: left;">79.6</td>
<td style="text-align: left;">(183)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">77.3</td>
<td style="text-align: left;">(488)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><em>Disease severity</em></td>
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
<td style="text-align: left;"> Mild</td>
<td style="text-align: left;">32.2</td>
<td style="text-align: left;">(74)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">37.6</td>
<td style="text-align: left;">(237)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Moderate</td>
<td style="text-align: left;">43.9</td>
<td style="text-align: left;">(101)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">45.6</td>
<td style="text-align: left;">(288)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;">23.9</td>
<td style="text-align: left;">(55)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">(106)</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;">/</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><em>Proxy OHA</em>,<em> % (n)</em></td>
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
<td style="text-align: left;"> 1</td>
<td style="text-align: left;">14.3</td>
<td style="text-align: left;">(33)</td>
<td style="text-align: left;">24.7</td>
<td style="text-align: left;">(19)</td>
<td rowspan="5" style="text-align: left;">0.002</td>
<td style="text-align: left;">18.4</td>
<td style="text-align: left;">(116)</td>
<td style="text-align: left;">29.9</td>
<td style="text-align: left;">(46)</td>
<td rowspan="5" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: left;">34.3</td>
<td style="text-align: left;">(79)</td>
<td style="text-align: left;">29.9</td>
<td style="text-align: left;">(23)</td>
<td style="text-align: left;">29.2</td>
<td style="text-align: left;">(184)</td>
<td style="text-align: left;">33.8</td>
<td style="text-align: left;">(52)</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td style="text-align: left;">24.3</td>
<td style="text-align: left;">(56)</td>
<td style="text-align: left;">36.4</td>
<td style="text-align: left;">(28)</td>
<td style="text-align: left;">25.4</td>
<td style="text-align: left;">(160)</td>
<td style="text-align: left;">26.0</td>
<td style="text-align: left;">(40)</td>
</tr>
<tr>
<td style="text-align: left;"> 4</td>
<td style="text-align: left;">21.3</td>
<td style="text-align: left;">(49)</td>
<td style="text-align: left;">7.8</td>
<td style="text-align: left;">(6)</td>
<td style="text-align: left;">20.8</td>
<td style="text-align: left;">(131)</td>
<td style="text-align: left;">9.1</td>
<td style="text-align: left;">(14)</td>
</tr>
<tr>
<td style="text-align: left;"> 5</td>
<td style="text-align: left;">5.7</td>
<td style="text-align: left;">(13)</td>
<td style="text-align: left;">1.3</td>
<td style="text-align: left;">(1)</td>
<td style="text-align: left;">6.3</td>
<td style="text-align: left;">(40)</td>
<td style="text-align: left;">1.3</td>
<td style="text-align: left;">(2)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Self-report OHA (≥ 6 years)</em>,<em> % (n)</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 446</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 120</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">23.8</td>
<td style="text-align: left;">(106)</td>
<td style="text-align: left;">41.7</td>
<td style="text-align: left;">(50)</td>
<td rowspan="5" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">28.7</td>
<td style="text-align: left;">(128)</td>
<td style="text-align: left;">33.3</td>
<td style="text-align: left;">(40)</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">20.2</td>
<td style="text-align: left;">(90)</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;">(21)</td>
</tr>
<tr>
<td style="text-align: left;"> 4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">20.0</td>
<td style="text-align: left;">(89)</td>
<td style="text-align: left;">6.7</td>
<td style="text-align: left;">(8)</td>
</tr>
<tr>
<td style="text-align: left;"> 5</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;">(33)</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">(1)</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Parent carer</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Age</em>,<em> mean (SD)</em></td>
<td style="text-align: left;">32.0</td>
<td style="text-align: left;">(4.1)</td>
<td style="text-align: left;">31.9</td>
<td style="text-align: left;">(4.6)</td>
<td style="text-align: left;">0.957</td>
<td style="text-align: left;">37.5</td>
<td style="text-align: left;">(5.4)</td>
<td style="text-align: left;">37.0</td>
<td style="text-align: left;">(4.8)</td>
<td style="text-align: left;">0.342</td>
</tr>
<tr>
<td style="text-align: left;"><em>Residence</em>,<em> % (n)</em></td>
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
<td style="text-align: left;"> Urban</td>
<td style="text-align: left;">92.2</td>
<td style="text-align: left;">(212)</td>
<td style="text-align: left;">89.6</td>
<td style="text-align: left;">(69)</td>
<td rowspan="3" style="text-align: left;">0.098</td>
<td style="text-align: left;">94.5</td>
<td style="text-align: left;">(596)</td>
<td style="text-align: left;">85.1</td>
<td style="text-align: left;">(131)</td>
<td rowspan="3" style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Rural</td>
<td style="text-align: left;">5.7</td>
<td style="text-align: left;">(13)</td>
<td style="text-align: left;">10.4</td>
<td style="text-align: left;">(8)</td>
<td style="text-align: left;">4.8</td>
<td style="text-align: left;">(30)</td>
<td style="text-align: left;">14.9</td>
<td style="text-align: left;">(23)</td>
</tr>
<tr>
<td style="text-align: left;"> Refuse to answer</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">(5)</td>
<td style="text-align: left;">0.0</td>
<td style="text-align: left;">(0)</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">(5)</td>
<td style="text-align: left;">0.0</td>
<td style="text-align: left;">(0)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Relationship</em></td>
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
<td style="text-align: left;"> Father</td>
<td style="text-align: left;">36.1</td>
<td style="text-align: left;">(83)</td>
<td style="text-align: left;">28.6</td>
<td style="text-align: left;">(22)</td>
<td rowspan="2" style="text-align: left;">0.229</td>
<td style="text-align: left;">29.0</td>
<td style="text-align: left;">(183)</td>
<td style="text-align: left;">26.0</td>
<td style="text-align: left;">(40)</td>
<td rowspan="2" style="text-align: left;">0.455</td>
</tr>
<tr>
<td style="text-align: left;"> Mother</td>
<td style="text-align: left;">63.9</td>
<td style="text-align: left;">(147)</td>
<td style="text-align: left;">71.4</td>
<td style="text-align: left;">(55)</td>
<td style="text-align: left;">71.0</td>
<td style="text-align: left;">(448)</td>
<td style="text-align: left;">74.0</td>
<td style="text-align: left;">(114)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Education</em>,<em> % (n)</em></td>
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
<td style="text-align: left;"> Middle/high school</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;">(17)</td>
<td style="text-align: left;">6.5</td>
<td style="text-align: left;">(5)</td>
<td rowspan="3" style="text-align: left;">0.493</td>
<td style="text-align: left;">7.7</td>
<td style="text-align: left;">(48)</td>
<td style="text-align: left;">5.2</td>
<td style="text-align: left;">(8)</td>
<td rowspan="3" style="text-align: left;">0.367</td>
</tr>
<tr>
<td style="text-align: left;"> College or above</td>
<td style="text-align: left;">92.2</td>
<td style="text-align: left;">(212)</td>
<td style="text-align: left;">93.5</td>
<td style="text-align: left;">(72)</td>
<td style="text-align: left;">92.3</td>
<td style="text-align: left;">(577)</td>
<td style="text-align: left;">94.8</td>
<td style="text-align: left;">(145)</td>
</tr>
<tr>
<td style="text-align: left;"> Refuse to answer</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">(1)</td>
<td style="text-align: left;">0.0</td>
<td style="text-align: left;">(0)</td>
<td style="text-align: left;">1.0</td>
<td style="text-align: left;">(6)</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">(1)</td>
</tr>
</tbody>
</table>

SD – standard deviation; OHA – overall health assessment

</div>

Inter-rater reliability was evaluated between patients and carers on the EQ-5D-Y-3L at baseline. For dimensions, Gwet’s AC1 assessed agreement \[26\], with values categorized as: below 0.2 (poor), 0.21–0.4 (fair), 0.41–0.6 (moderate), 0.61–0.8 (good), and above 0.8 (excellent) \[27\]. The agreement on index score and EQ VAS used the intraclass correlation coefficient (ICC), with values classified as: below 0.1 (no agreement), 0.1–0.29 (low agreement), 0.3–0.49 (moderate agreement), 0.5 or higher (high agreement), and 0.7 or above (good reliability) \[28\].

Responsiveness was assessed in patients showing clinical recovery or OHA improvement from baseline to follow-up via independent t-tests to compare mean summary scores. Changes in ‘no problem’ proportions for each dimension were analysed. The results include the Glass’ Δ effect size (ES = difference of mean/ baseline SD), which is recommended when the intervention might influence the standard deviation \[29\]. The percentage of ‘no problem’ reported are detailed in Appendix-Table <a href="#Tabc" data-ref-type="table">3</a>. All analyses utilized SPSS (IBM SPSS Statistics, Version 26.0, IBM Corp).

## Results

Figure <a href="#Fig1" data-ref-type="fig">1</a> illustrates the recruitment of this study involving 1092 children (0–18 years) and their parental caregivers. Among them, 78.8% were COVID-19 infected (average duration: 10.9 days), with 311 completing the follow-up survey after one to three weeks. The control group (21.2%) comprised non-infected children staying at home for at least three months. Baseline characteristics presented in Table <a href="#Tab1" data-ref-type="table">1</a> showed no significant differences except in residence. Most EQ-TIPS respondents were aged 2–4 years (63.5%), while the EQ-5D-Y-3L completers were mostly 6–11 years old (61.0%). Approximately 80% of patients had at least two symptoms, two-thirds had moderate to severe disease, and most caregivers were highly educated (92.1%).

Figure <a href="#Fig2" data-ref-type="fig">2</a>a shows that all EQ-TIPS dimensions contribute to lower scores, with parents of non-infected children reporting fewer problems than those with COVID-19 (*p* \< 0.001), except for ‘communication’ (*p* = 0.110). The proportion reporting ‘no problems’ ranged from 51.3% for ‘pain’ to 74.8% for ‘communication’. Full health (111111) was reported by 30.4% of patients and 61.0% of non-infected children, indicating a higher ceiling effect in the healthier non-infected group across all dimensions as expected, ranging from 83.1% for ‘pain’ to 96.1% for ‘movement’.

Figure <a href="#Fig2" data-ref-type="fig">2</a>b indicates a significant trend of reporting more problems by infected children aged ≥ 4 years on the EQ-5D-Y-3L. In the self-complete version, the proportion of patients reporting ‘no problems’ ranged from 49.0% for ‘pain/discomfort’ to 73.9% for ‘looking after myself’. The proxy version showed a similar pattern with slightly more problems reported, particularly at the extreme level. Full health (11111) was reported by 38.4% of patients using the self-complete version, and by 56.1% of non-infected children. The proxy version percentages were 36.0% for patients and 53.5% for non-infected children. In patients aged 4–5 years, physical items (‘mobility’, ‘looking after myself’ and ‘usual activity’) reported less problems, with no significant difference compared to the non-infected group (p = 0.235, 0.119, and 0.109, respectively).

<figure id="Fig2">
<p><img src="10198_2024_1710_Fig2_HTML.jpg" id="d33e1351" /></p>
<figcaption>Dimension responses of <strong>the EQ-TIPS</strong> and <strong>the EQ-5D-Y-3L</strong> for children with or without COVID-19 infection in different age groups, i.e., aged 0–3 years, 4–5 years, and ≥ 6 years. P-value represent differences between with children COVID-19 and a healthy sample in terms of Chi-square test, and Fisher’s exact test if any cell had expected count less than 5. (<strong>a</strong>) Percentage of dimension responses for the EQ-TIPS for patients with COVID-19 and children without infection aged 0–3 years. (<strong>b</strong>) Percentage of item responses for the EQ-5D-Y-3L for patients with COVID-19 and children without infection aged ≥ four years</figcaption>
</figure>

Table <a href="#Tab2" data-ref-type="table">2</a> presents the known-group validity of EQ-TIPS and EQ-5D-Y-3L summary scores. Those with poorer health status—COVID-19 infection, higher disease severity, multiple symptoms, or poorer OHA—showed higher LSS, lower index and EQ VAS scores. Statistically significant differences were observed between relevant groups (*p* \< 0.05), except for EQ-TIPS LSS between mild and moderate severity (absolute difference = 0.01). Cohen’s D ESs were mostly moderate to high. For the EQ-TIPS LSS, between-groups ESs ranged from 0.58 to 0.84, and for the EQ-5D-Y-3L index, from 0.32 to 0.65 in those aged 4–18 years. ESs of the self-complete EQ-5D-Y-3L index score were larger than proxy version in ages ≥ 6 years (0.44 to 1.26 vs. 0.32 to 0.76). These differences in ESs were particularly evident when categorized based on disease severity and OHA. The greatest discriminative ability, with large effect sizes (0.76 to 1.54), was observed between OHA-defined groups, in all age groups. Satisfactory discriminative validity was shown between the COVID-19 and symptom-based groups (ESs: 0.50 to 0.84 and 0.60 to 0.76, respectively). The EQ-TIPS and the EQ-5D-Y-3L tended to show larger ESs between patients in the moderate and severe groups, compared to the differences between the mild and moderate groups.

<div id="Tab2" class="table-wrap">

<div class="caption">

Known-groups validity of the EQ-TIPS LSS, the EQ-5D-Y-3L index score, and EQ VAS (mean \[SD\]) across different health condition based on with or without COVID-19 infection, disease severity, number of symptoms, and OHA using t-test or ANOVA

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">With or without COVID-19</th>
<th colspan="5" style="text-align: left;">Disease severity</th>
<th colspan="3" style="text-align: left;">Number of symptoms</th>
<th colspan="3" style="text-align: left;">OHA</th>
</tr>
<tr>
<th style="text-align: left;">Non-infected</th>
<th style="text-align: left;">Infected</th>
<th style="text-align: left;">Cohen’s d ES<br />
(95%CI)</th>
<th style="text-align: left;">Mild</th>
<th style="text-align: left;">Moderate</th>
<th style="text-align: left;">Severe</th>
<th style="text-align: left;">Cohen’s d ES (95%CI)<br />
Mild vs. Moderate</th>
<th style="text-align: left;">Cohen’s d ES (95%CI)<br />
Moderate vs. Severe</th>
<th style="text-align: left;">No/single</th>
<th style="text-align: left;">Multiple</th>
<th style="text-align: left;">Cohen’s d ES<br />
(95%CI)</th>
<th style="text-align: left;">Very good/<br />
Good</th>
<th style="text-align: left;">Fair/Poor/<br />
Very Poor</th>
<th style="text-align: left;">Cohen’s d ES<br />
(95%CI)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>0–3 years (proxy)</em></td>
<td style="text-align: left;"><em>n</em> = 77</td>
<td style="text-align: left;"><em>n</em> = 230</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 74</td>
<td style="text-align: left;"><em>n</em> = 101</td>
<td style="text-align: left;"><em>n</em> = 55</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 47</td>
<td style="text-align: left;"><em>n</em> = 183</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 112</td>
<td style="text-align: left;"><em>n</em> = 118</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-TIPS LSS</td>
<td style="text-align: left;">6.70 (1.12)</td>
<td style="text-align: left;">8.77 (2.78)</td>
<td style="text-align: left;"><p>0.84</p>
<p>(0.57, 1.10)</p></td>
<td style="text-align: left;">8.39 (2.70)</td>
<td style="text-align: left;">8.40 (2.60)</td>
<td style="text-align: left;">9.96 (2.91)</td>
<td style="text-align: left;"><p>0.004 <sup>§</sup></p>
<p>(-0.29, -0.30)</p></td>
<td style="text-align: left;"><p>0.58</p>
<p>(0.24, 0.91)</p></td>
<td style="text-align: left;">7.49 (2.09)</td>
<td style="text-align: left;">9.10 (2.84)</td>
<td style="text-align: left;"><p>0.60</p>
<p>(0.27, 0.92)</p></td>
<td style="text-align: left;">7.69 (2.34)</td>
<td style="text-align: left;">9.80 (2.78)</td>
<td style="text-align: left;"><p>0.82</p>
<p>(0.55, 1.09)</p></td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS</td>
<td style="text-align: left;">85.5 (13.4)</td>
<td style="text-align: left;">67.4 (22.8)</td>
<td style="text-align: left;"><p>-0.86</p>
<p>(-1.10, -0.27)</p></td>
<td style="text-align: left;">72.5 (21.1)</td>
<td style="text-align: left;">68.6 (23.3)</td>
<td style="text-align: left;">58.4 (21.9)</td>
<td style="text-align: left;"><p>-0.17 <sup>§</sup></p>
<p>(-0.48, -0.13)</p></td>
<td style="text-align: left;"><p>-0.45</p>
<p>(-0.78, -0.11)</p></td>
<td style="text-align: left;">78.0 (17.5)</td>
<td style="text-align: left;">64.7 (23.3)</td>
<td style="text-align: left;"><p>-0.60</p>
<p>(-0.92, -0.27)</p></td>
<td style="text-align: left;">80.8 (14.3)</td>
<td style="text-align: left;">54.7 (22.2)</td>
<td style="text-align: left;"><p>-1.39</p>
<p>(-1.68, -1.10)</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>4–5 years (proxy)</em></td>
<td style="text-align: left;"><em>n</em> = 27</td>
<td style="text-align: left;"><em>n</em> = 148</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 50</td>
<td style="text-align: left;"><em>n</em> = 60</td>
<td style="text-align: left;"><em>n</em> = 38</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 30</td>
<td style="text-align: left;"><em>n</em> = 118</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 78</td>
<td style="text-align: left;"><em>n</em> = 70</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-Y-3L index</td>
<td style="text-align: left;">0.95 (0.06)</td>
<td style="text-align: left;">0.74 (0.36)</td>
<td style="text-align: left;"><p>-0.63</p>
<p>(-1.05, -0.22)</p></td>
<td style="text-align: left;">0.91 (0.17)</td>
<td style="text-align: left;">0.73 (0.34)</td>
<td style="text-align: left;">0.54 (0.44)</td>
<td style="text-align: left;"><p>-0.65</p>
<p>(-1.04, -0.27)</p></td>
<td style="text-align: left;"><p>-0.50</p>
<p>(-0.91, -0.09)</p></td>
<td style="text-align: left;">0.95 (0.12)</td>
<td style="text-align: left;">0.69 (0.38)</td>
<td style="text-align: left;"><p>-0.76</p>
<p>(-1.16, -0.34)</p></td>
<td style="text-align: left;">0.99 (0.16)</td>
<td style="text-align: left;">0.53 (0.40)</td>
<td style="text-align: left;"><p>-1.54</p>
<p>(-1.91, -1.17)</p></td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS</td>
<td style="text-align: left;">87.2 (10.0)</td>
<td style="text-align: left;">70.3 (26.5)</td>
<td style="text-align: left;"><p>-0.68</p>
<p>(-1.10, -0.27)</p></td>
<td style="text-align: left;">84.7 (16.0)</td>
<td style="text-align: left;">66.4 (28.7)</td>
<td style="text-align: left;">57.5 (25.8)</td>
<td style="text-align: left;"><p>-0.77</p>
<p>(-1.16, -0.38)</p></td>
<td style="text-align: left;"><p>-0.32 <sup>§</sup></p>
<p>(-0.71, -0.09)</p></td>
<td style="text-align: left;">87.9 (13.3)</td>
<td style="text-align: left;">65.8 (27.2)</td>
<td style="text-align: left;"><p>-0.88</p>
<p>(-1.30, -0.47)</p></td>
<td style="text-align: left;">86.4 (14.4)</td>
<td style="text-align: left;">52.4 (25.4)</td>
<td style="text-align: left;"><p>-1.67</p>
<p>(-2.04, -1.30)</p></td>
</tr>
<tr>
<td colspan="15" style="text-align: left;"><em>6–18 years</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Self-report</em></td>
<td style="text-align: left;"><em>n</em> = 114</td>
<td style="text-align: left;"><em>n</em> = 445</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 172</td>
<td style="text-align: left;"><em>n</em> = 214</td>
<td style="text-align: left;"><em>n</em> = 59</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 102</td>
<td style="text-align: left;"><em>n</em> = 343</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 233</td>
<td style="text-align: left;"><em>n</em> = 212</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-Y-3L index</td>
<td style="text-align: left;">0.92 (0.13)</td>
<td style="text-align: left;">0.77 (0.33)</td>
<td style="text-align: left;"><p>-0.50</p>
<p>(-0.71, -0.29)</p></td>
<td style="text-align: left;">0.87 (0.23)</td>
<td style="text-align: left;">0.74 (0.34)</td>
<td style="text-align: left;">0.57 (0.41)</td>
<td style="text-align: left;"><p>-0.44</p>
<p>(-0.64, -0.24)</p></td>
<td style="text-align: left;"><p>-0.48</p>
<p>(-0.77, -0.19)</p></td>
<td style="text-align: left;">0.92 (0.19)</td>
<td style="text-align: left;">0.72 (0.35)</td>
<td style="text-align: left;"><p>-0.62</p>
<p>(-0.85, -0.34)</p></td>
<td style="text-align: left;">0.94 (0.15)</td>
<td style="text-align: left;">0.59 (0.37)</td>
<td style="text-align: left;"><p>-1.26</p>
<p>(-1.46, -1.06)</p></td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS</td>
<td style="text-align: left;">86.5 (12.6)</td>
<td style="text-align: left;">72.2 (25.0)</td>
<td style="text-align: left;"><p>-0.62</p>
<p>(-0.83, -0.41)</p></td>
<td style="text-align: left;">80.9 (19.9)</td>
<td style="text-align: left;">68.8 (26.4)</td>
<td style="text-align: left;">52.9 (24.9)</td>
<td style="text-align: left;"><p>-0.51</p>
<p>(-0.71, -0.31)</p></td>
<td style="text-align: left;"><p>-0.61</p>
<p>(-0.90, -0.32)</p></td>
<td style="text-align: left;">85.4 (17.0)</td>
<td style="text-align: left;">68.3 (25.6)</td>
<td style="text-align: left;"><p>-0.72</p>
<p>(-0.94, -0.49)</p></td>
<td style="text-align: left;">88.7 (11.4)</td>
<td style="text-align: left;">54.1 (23.3)</td>
<td style="text-align: left;"><p>-1.91</p>
<p>(-2.14, -1.69)</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Proxy-report</em></td>
<td style="text-align: left;"><em>n</em> = 127</td>
<td style="text-align: left;"><em>n</em> = 483</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 187</td>
<td style="text-align: left;"><em>n</em> = 228</td>
<td style="text-align: left;"><em>n</em> = 68</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 112</td>
<td style="text-align: left;"><em>n</em> = 371</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 222</td>
<td style="text-align: left;"><em>n</em> = 261</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-Y-3L index</td>
<td style="text-align: left;">0.91 (0.19)</td>
<td style="text-align: left;">0.72 (0.37)</td>
<td style="text-align: left;"><p>-0.56</p>
<p>(-0.76, -0.36)</p></td>
<td style="text-align: left;">0.81 (0.31)</td>
<td style="text-align: left;">0.70 (0.37)</td>
<td style="text-align: left;">0.52 (0.41)</td>
<td style="text-align: left;"><p>-0.32</p>
<p>(-0.51, -0.12)</p></td>
<td style="text-align: left;"><p>-0.47</p>
<p>(-0.75, -0.20)</p></td>
<td style="text-align: left;">0.90 (0.21)</td>
<td style="text-align: left;">0.66 (0.39)</td>
<td style="text-align: left;"><p>-0.67</p>
<p>(-0.89, -0.46)</p></td>
<td style="text-align: left;">0.86 (0.29)</td>
<td style="text-align: left;">0.60 (0.38)</td>
<td style="text-align: left;"><p>-0.76</p>
<p>(-0.95, -0.58)</p></td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS</td>
<td style="text-align: left;">87.8 (10.9)</td>
<td style="text-align: left;">69.9 (24.9)</td>
<td style="text-align: left;"><p>-0.79</p>
<p>(-0.99, 0.59)</p></td>
<td style="text-align: left;">78.6 (20.6)</td>
<td style="text-align: left;">67.8 (24.6)</td>
<td style="text-align: left;">56.9 (24.3)</td>
<td style="text-align: left;"><p>-0.47</p>
<p>(-0.67, -0.28)</p></td>
<td style="text-align: left;"><p>-0.44</p>
<p>(-0.72, 0.17)</p></td>
<td style="text-align: left;">84.4 (17.6)</td>
<td style="text-align: left;">65.3(25.1)</td>
<td style="text-align: left;"><p>-0.81</p>
<p>(-1.03, -0.59)</p></td>
<td style="text-align: left;">85.3 (15.8)</td>
<td style="text-align: left;">56.8 (23.7)</td>
<td style="text-align: left;"><p>-1.39</p>
<p>(-1.59, -1.19)</p></td>
</tr>
</tbody>
</table>

§: p\>0.05; all other p values were \>0.01. ES – effect size; LSS – level sum score; VAS – visual analogue scale; OHA – overall health assessment

</div>

The EQ VAS exhibited moderate to high known-group validity for both EQ-TIPS and EQ-5D-Y-3L, with larger effect sizes observed in older age groups (0.17 to 1.39 for 0–3 years, 0.32 to 1.67 for 4–5 years, 0.44 to 1.91 for 6–18 years, respectively). Additionally, the self-complete version (0.51 to 1.91) showed higher ESs compared to the proxy version (0.44 to1.39).

Table <a href="#Tab3" data-ref-type="table">3</a> presents the inter-rater agreement on EQ-5D-Y-3L dimensions using data from 445 patient-proxy dyads with COVID-19 and a total of 559 child-parent dyads at baseline. For patients with COVID-19, the Gwet’s AC1 values ranged from 0.470 for ‘having pain/discomfort’ to 0.687 for ‘mobility’, demonstrating moderate to good inter-rater reliability for the descriptive system. The ICC values for index and EQ VAS were 0.657 and 0.815, respectively, indicating good inter-rater reliability for both. The overall sample exhibited similar and slightly better reliability, with Gwet’s AC1 ranging from 0.529 to 0.738 and 0.653 to 0.823 for ICC.

<div id="Tab3" class="table-wrap">

<div class="caption">

The child-parent agreement of the self-complete and proxy versions of the EQ-5D-Y-3L at baseline in children ≥ 6 years and their parent carers (*n* = 559)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Patients with COVID-19<br />
<em>n</em> = 445</th>
<th colspan="3" style="text-align: left;">Overall sample<br />
<em>n</em> = 559</th>
</tr>
<tr>
<th style="text-align: left;">Gwet’s AC1</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">Agreement(%)</th>
<th style="text-align: left;">Gwet’s AC1</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">Agreement(%)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility (Walking about)</td>
<td style="text-align: left;">0.687</td>
<td style="text-align: left;">0.631, 0.743</td>
<td style="text-align: left;">75.7</td>
<td style="text-align: left;">0.703</td>
<td style="text-align: left;">0.665, 0.751</td>
<td style="text-align: left;">76.4</td>
</tr>
<tr>
<td style="text-align: left;">Looking after myself</td>
<td style="text-align: left;">0.685</td>
<td style="text-align: left;">0.630, 0.741</td>
<td style="text-align: left;">75.1</td>
<td style="text-align: left;">0.738</td>
<td style="text-align: left;">0.692, 0.783</td>
<td style="text-align: left;">78.5</td>
</tr>
<tr>
<td style="text-align: left;">Doing usual activities</td>
<td style="text-align: left;">0.613</td>
<td style="text-align: left;">0.552, 0.674</td>
<td style="text-align: left;">71.7</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.572, 0.579</td>
<td style="text-align: left;">72.1</td>
</tr>
<tr>
<td style="text-align: left;">Having pain/ discomfort</td>
<td style="text-align: left;">0.470</td>
<td style="text-align: left;">0.403, 0.536</td>
<td style="text-align: left;">63.1</td>
<td style="text-align: left;">0.529</td>
<td style="text-align: left;">0.472, 0.587</td>
<td style="text-align: left;">66.4</td>
</tr>
<tr>
<td style="text-align: left;">Feeling worried/ sad/unhappy</td>
<td style="text-align: left;">0.552</td>
<td style="text-align: left;">0.488, 0.616</td>
<td style="text-align: left;">67.6</td>
<td style="text-align: left;">0.560</td>
<td style="text-align: left;">0.504, 0.616</td>
<td style="text-align: left;">67.8</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ICC</td>
<td style="text-align: left;">95% CI</td>
<td style="text-align: left;"><em>p</em> value</td>
<td style="text-align: left;">ICC</td>
<td style="text-align: left;">95% CI</td>
<td style="text-align: left;"><em>p</em> value</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-Y-3L index</td>
<td style="text-align: left;">0.657</td>
<td style="text-align: left;">0.601, 0.707</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.653</td>
<td style="text-align: left;">0.603, 0.698</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;">0.815</td>
<td style="text-align: left;">0.782, 0.844</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.823</td>
<td style="text-align: left;">0.795, 0.848</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
</tbody>
</table>

VAS – visual analogue scale

</div>

Table <a href="#Tab4" data-ref-type="table">4</a> shows strong responsiveness of the EQ-TIPS and the EQ-5D-Y-3L for both groups to health improvement based on clinical progress and enhanced Overall Health Assessment (OHA). The EQ-TIPS LSS showed ES of 1.21–1.39, and the EQ-5D-Y-3L index score had ES of 1.00–1.16 and 1.08–1.15 for the proxy and self-complete versions, respectively, in children and adolescents with improved health. The EQ VAS demonstrated the highest responsiveness, with SES ranging from 1.38 to 2.01 for proxy versions and 1.77 to 1.94 for self-complete version.

<div id="Tab4" class="table-wrap">

<div class="caption">

Change in mean (SD) of EQ-TIPS LSS, EQ-5D-Y-3L index score and EQ VAS (with corresponding effect sizes) between illness and recovery based on clinical recovery or improved OHA

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">COVID-19 recovery</th>
<th colspan="3" style="text-align: left;">Improved OHA</th>
</tr>
<tr>
<th style="text-align: left;">Baseline</th>
<th style="text-align: left;">Follow-up</th>
<th style="text-align: left;">Glass’ Δ ES</th>
<th style="text-align: left;">Baseline</th>
<th style="text-align: left;">Follow-up</th>
<th style="text-align: left;">Glass’ Δ ES</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>0–3 years (proxy)</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 69</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 64</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-TIPS LSS, mean (SD)</td>
<td style="text-align: left;">10.33 (2.80)</td>
<td style="text-align: left;">6.93 (1.83)</td>
<td style="text-align: left;">1.21</td>
<td style="text-align: left;">10.34 (2.61)</td>
<td style="text-align: left;">6.70 (1.29)</td>
<td style="text-align: left;">1.39</td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS, mean (SD)</td>
<td style="text-align: left;">51.6 (21.6)</td>
<td style="text-align: left;">85.2 (16.7)</td>
<td style="text-align: left;">-1.56</td>
<td style="text-align: left;">48.4 (21.4)</td>
<td style="text-align: left;">85.8 (13.3)</td>
<td style="text-align: left;">-1.75</td>
</tr>
<tr>
<td style="text-align: left;"><em>4–5 years (proxy)</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 48</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 46</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-Y-3L index, mean (SD)</td>
<td style="text-align: left;">0.47 (0.44)</td>
<td style="text-align: left;">0.91 (0.17)</td>
<td style="text-align: left;">-1.00</td>
<td style="text-align: left;">0.45 (0.43)</td>
<td style="text-align: left;">0.90 (0.17)</td>
<td style="text-align: left;">-1.05</td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS, mean (SD)</td>
<td style="text-align: left;">48.7 (27.4)</td>
<td style="text-align: left;">86.5 (9.5)</td>
<td style="text-align: left;">-1.38</td>
<td style="text-align: left;">45.1 (24.2)</td>
<td style="text-align: left;">84.5 (10.9)</td>
<td style="text-align: left;">-1.63</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>6–18 years</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Self-report</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 132</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 138</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-Y-3L index, mean (SD)</td>
<td style="text-align: left;">0.51 (0.38)</td>
<td style="text-align: left;">0.92 (0.21)</td>
<td style="text-align: left;">-1.08</td>
<td style="text-align: left;">0.48 (0.39)</td>
<td style="text-align: left;">0.93 (0.19)</td>
<td style="text-align: left;">-1.15</td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS, mean (SD)</td>
<td style="text-align: left;">47.4 (23.1)</td>
<td style="text-align: left;">88.4 (11.0)</td>
<td style="text-align: left;">-1.77</td>
<td style="text-align: left;">45.5 (21.8)</td>
<td style="text-align: left;">87.9 (10.8)</td>
<td style="text-align: left;">-1.94</td>
</tr>
<tr>
<td style="text-align: left;"><em>Proxy-report</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 141</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 147</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> EQ-5D-Y-3L index, mean (SD)</td>
<td style="text-align: left;">0.45 (0.41)</td>
<td style="text-align: left;">0.91 (0.22)</td>
<td style="text-align: left;">-1.12</td>
<td style="text-align: left;">0.44 (0.41)</td>
<td style="text-align: left;">0.91 (0.20)</td>
<td style="text-align: left;">-1.16</td>
</tr>
<tr>
<td style="text-align: left;"> EQ VAS, mean (SD)</td>
<td style="text-align: left;">46.8 (20.8)</td>
<td style="text-align: left;">87.6 (11.3)</td>
<td style="text-align: left;">-1.96</td>
<td style="text-align: left;">45.8 (20.7)</td>
<td style="text-align: left;">87.5 (11.2)</td>
<td style="text-align: left;">-2.01</td>
</tr>
</tbody>
</table>

All *p* value \>0.01 using independent t-tests; SD – standard deviation; OHA – overall health assessment; VAS – visual analogue scale; ES – effect size

</div>

## Discussion

In this study, we observed acceptable psychometric properties for the Chinese versions of the experimental EQ-TIPS, and for both modes of administration (self-complete and proxy) for the EQ-5D-Y-3L. These findings add to an expanding evidence base for the psychometric robustness of the EQ-5D-Y-3L and provide the first evidence of responsiveness for the EQ-TIPS, which is one of only a handful of preference-weighted HRQoL measures that can be used in the youngest populations. The lack of validated preference-weighted measures for infants and toddlers means that the EQ-TIPS is likely to be widely used, which highlights the importance of providing evidence to support its psychometric performance. Notably, large effect sizes on the EQ-5D-Y-3L were observed when using both clinical changes (disease severity and symptom numbers) and self-rated health changes (OHA) as external criteria for assessing responsiveness (independently of whether proxy or self-report was used), suggesting that the EQ-5D-Y-3L is useful in capturing improvements in health after recovery from COVID-19.

Our study, characterized by a large and diverse sample, broad age representation, and the unique ability to assess responsiveness through clinical recovery criteria, has several strengths. Notably, this is the first study in China to assess the psychometric performance of the experimental EQ-TIPS. Only three studies have been published previously exploring the EQ-TIPS’ measurement properties. While they demonstrated its validity, they provided limited evidence of reliability and none for responsiveness \[18, 19, 30\]. Our research therefore contributes the first evidence of the EQ-TIPS’ responsiveness, indicating its suitability for capturing COVID-19-related HRQoL improvements in infants and toddlers. Additionally, our study is the first to examine the psychometric properties of the EQ-5D-Y-3L in patients with COVID-19 using the corresponding Chinese value set.

The EQ-TIPS, applied to COVID-19 patients, showed a ceiling effect in the ‘communication’ dimension, echoing findings in a broader paediatric health study \[30\]. The non-significant difference suggests minimal impact on children’s communicative abilities. Respiratory effects might not significantly affect physical communication skills in young children. Our previous cognitive interviews revealed parental difficulty in responding to this dimension, emphasizing the need for simplified examples. This aligns with the study’s highest ceiling effect (74.8%) in ‘communication’ among COVID-19-infected children.

The EQ-TIPS LSS discriminated effectively between infected and non-infected groups and individuals with varying OHA, exhibiting significant effect sizes. It also discriminated well between those with moderate and severe disease, with an effect size of 0.58, but not between those with mild and moderate disease (ES of 0.004). It is not clear why this should be the case, but it is of note that the EQ VAS also provided poorer results in this youngest group (ES of 0.17) compared to any of the other age groups when examining its ability to discriminate between patients classified as mild and moderate. As an identical EQ VAS is used in the EQ-TIPS as in the EQ-5D-Y-3L, this finding suggests that the lack of discriminatory capacity between mild and moderate disease is not necessarily due to the instrument itself but rather to other factors. These factors could include difficulties that parents have in deciding on an ‘accurate’ score for their child’s health in such young children, who are unable to communicate how they are feeling, and/or questions about whether the criteria used to decide on disease severity are equally suitable across all age groups. Further research is required to clarify these issues.

This study offers the first evidence of the EQ-TIPS’ responsiveness, revealing significant improvement across all dimensions, as shown by the change in the percentage of patients reporting ‘no problems’ from the first to the second visit. Improvements were observed on all dimensions, suggesting that each dimension serves as a useful indicator of how HRQoL evolves as COVID-19 symptoms improve over time in very young children.

Our study supported the known-group validity, inter-rater reliability, and responsiveness of both self-complete and proxy versions of the EQ-5D-Y-3L, as evidenced by the performance of the index scores and EQ VAS. While previous studies validating the proxy version have mainly compared agreement levels between children and proxy-respondents \[13–15, 31–33\], our study delved into the comparison of validity and responsiveness, in particular, an area with limited exploration \[34, 35\].

In general, the response distribution patterns were similar between the self-complete and proxy versions, regardless of infection status. Our findings align with previous studies, suggesting parental underestimation of children’s HRQoL, particularly in COVID-19 or other infections \[10, 16\]. Specifically, parents reported more problems at level 3, which could be attributed to parents perceiving children’s symptoms as severe, while children might exhibit greater physical tolerance and cope better with the illness \[36\]. Additionally, no high ceiling effects were observed in any EQ-5D-Y-3L dimensions for children or adolescents with COVID-19, indicating the effectiveness of capturing these variations and identifying HRQoL-related problems or limitations.

The EQ-5D-Y-3L demonstrates moderate to good discriminative ability across age groups and health categories, with its strongest performance observed in OHA, consistent with its generic scale nature. Although the instrument excels in capturing variations in symptoms and infection status, its capacity to discern subtleties in disease severity may be constrained by its generic design, especially in scenarios where the distinction between ‘mild’ and ‘moderate’ criteria is not substantial. Nonetheless, the statistical significant differences in index values between mild, moderate, and severe categories suggested that the EQ-5D-Y-3L is a sensitive instrument in COVID-19 economic evaluations. This is particularly relevant for interventions such as vaccines, which can prevent poorer health states, or for treatments that improve health. Additionally, the substantial similarities between self-reports and proxy results suggest that results in trials will be relatively comparable, whichever source is used to collect data on the EQ-5D-Y-3L descriptive system. Although proxies tended to score lower than self-report, the difference between categories of disease severity or number of symptoms is quite similar, so gains or losses will be similar whether self-report or proxy reports are used. For instance, moving from severe to moderate disease severity represents a move from 0.57 to 0.74 using self-report, and 0.52 to 0.70 for proxy, an almost identical difference, suggesting use of one or the other response mode would have little impact on in the context of an economic model.

Our study indicated good inter-rater reliability, supporting the idea that self-report and proxy data are likely to be relatively comparable, and that aggregating them, for example for use in an economic model, is likely to be acceptable. In our study, the reliability of the EQ-5D-Y-3L index score was good, and excellent for EQ VAS indicated by ICC. However, compared to physical items, ‘having pain or discomfort’ and ‘feeling worried, sad, or unhappy’ showed poorer child-parent agreement, with parents reported more problems and lower index scores and EQ VAS. This aligns with previous studies which found lower agreement for emotional and mental items in paediatric populations with haematological malignancies, idiopathic scoliosis or general population and their parents \[13, 15, 37\]. The impact of COVID-19 has further highlighted discrepancies across all dimensions, potentially influenced by factors such as parental education, household income, and the infection status of other family members \[16\]. For example, in our study, 44.6% of proxy respondents of children with COVID-19, reported recent personal infection within the past week.

To our knowledge, this study provides the largest sample for assessing the responsiveness of the EQ-5D-Y-3L in children with COVID-19, especially given the ability to generate index scores based on a recently published value set. Our findings demonstrated good responsiveness to clinical recovery from COVID-19 and health improvements based on overall health assessments (OHA). The considerable effect sizes observed for the EQ-5D-Y-3L index or LSS scores, along with notably larger SESs for EQ VAS, underscore the EQ-5D-Y-3L’s effectiveness in measuring health improvements. Moreover, the effective performance of both the experimental EQ-TIPS and the EQ-5D-Y-3L in children with COVID-19 implies their potential applicability to other prevalent respiratory infectious diseases, which are widespread in many countries. Although our study did not delve into intervention analysis, our future research will explore how specific COVID-19 interventions impact children’s HRQoL. Additionally, investigating whether the new EQ-5D-Y-5 L performs as well or better in these patients than the EQ-5D-Y-3L would be of interest \[38\].

This study has several limitations. Firstly, the data were collected at an academic hospital in Shanghai, involving participants with a relatively higher socioeconomic status and parental education background, limiting generalizability. Secondly, the instruction section of the EQ-TIPS and the EQ-5D-Y-3L was slightly modified to emphasize the impact by the COVID-19 pandemic, which could potentially affect responses when compared to use of the standard instruction.

## Conclusion

In conclusion, the study results show that the experimental EQ-TIPS and the EQ-5D-Y-3L are reliable and valid instruments for assessing the impact of COVID-19 on the HRQoL of children and adolescents, including very young children. Additionally, both instruments are responsive to change as children’s COVID-related health status evolves over time. The study also provides the first application of the new EQ-5D-Y-3L Chinese value set in a clinical population and shows that the values discriminate well between relevant disease groups. These instruments will therefore likely be useful in COVID-related clinical and resource allocation decision-making and in monitoring the well-being of infants, children and adolescents affected by COVID-19 and respiratory infections. Further research using these instruments to explore the impact of specific treatments for COVID-19 would be of interest.

## Appendix

<div id="Taba" class="table-wrap">

<div class="caption">

COVID-19 severity and symptom distribution based on symptom numbers at baseline

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">Number of symptoms<br />
<em>n</em>=861</th>
</tr>
<tr>
<th style="text-align: left;">No<br />
<em>n</em>=16</th>
<th style="text-align: left;">Single<br />
<em>n</em>=173</th>
<th style="text-align: left;">Multiple<br />
<em>n</em>=672</th>
<th style="text-align: left;"><em>p</em> value<br />
No vs. Single</th>
<th style="text-align: left;"><em>p</em> value<br />
No vs. Single vs. Multiple</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;"><em>COVID-19 severity, %(</em> <em>n)</em></td>
</tr>
<tr>
<td style="text-align: left;"> Mild</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">98.3 (170)</td>
<td style="text-align: left;">18.6 (125)</td>
<td rowspan="3" style="text-align: left;">0.766</td>
<td rowspan="3" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Moderate</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">57.9 (389)</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">1.7 (3)</td>
<td style="text-align: left;">23.5 (158)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><em>Symptom</em>,<em> %(n)</em></td>
</tr>
<tr>
<td style="text-align: left;">Fever</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">26.6 (46)</td>
<td style="text-align: left;">4.0 (27)</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">73.4 (127)</td>
<td style="text-align: left;">96.0 (645)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Upper respiratory problems</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">78.6 (136)</td>
<td style="text-align: left;">21.3 (143)</td>
<td rowspan="2" style="text-align: left;">0.045</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">21.4 (37)</td>
<td style="text-align: left;">78.7 (529)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Pneumonia</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">100.0 (173)</td>
<td style="text-align: left;">92.1 (619)</td>
<td rowspan="2" style="text-align: left;">na</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">7.9 (53)</td>
</tr>
<tr>
<td style="text-align: left;">Pain</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">98.3 (170)</td>
<td style="text-align: left;">60.9 (409)</td>
<td rowspan="2" style="text-align: left;">0.817</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">1.7 (3)</td>
<td style="text-align: left;">39.1 (263)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Cardiovascular problems</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">100.0 (173)</td>
<td style="text-align: left;">89.1 (599)</td>
<td rowspan="2" style="text-align: left;">na</td>
<td rowspan="2" style="text-align: left;">0.027</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">10.9 (73)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Gastrointestinal problems</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">98.8 (171)</td>
<td style="text-align: left;">70.8 (476)</td>
<td rowspan="2" style="text-align: left;">0.904</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">1.2 (2)</td>
<td style="text-align: left;">29.2 (196)</td>
</tr>
<tr>
<td style="text-align: left;">Fatigue</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">96.0 (166)</td>
<td style="text-align: left;">51.3 (345)</td>
<td rowspan="2" style="text-align: left;">0.541</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">4.0 (7)</td>
<td style="text-align: left;">48.7 (327)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Olfaction/ Gustation</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">100.0 (173)</td>
<td style="text-align: left;">80.2 (539)</td>
<td rowspan="2" style="text-align: left;">na</td>
<td rowspan="2" style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">19.8 (133)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Shock</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">100.0 (173)</td>
<td style="text-align: left;">93.9 (631)</td>
<td rowspan="2" style="text-align: left;">na</td>
<td rowspan="2" style="text-align: left;">0.038</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">6.1 (41)</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Eye problems</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">100.0 (16)</td>
<td style="text-align: left;">100.0 (173)</td>
<td style="text-align: left;">94.2 (633)</td>
<td rowspan="2" style="text-align: left;">na</td>
<td rowspan="2" style="text-align: left;">0.048</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">0.0 (0)</td>
<td style="text-align: left;">5.8 (39)</td>
</tr>
</tbody>
</table>

*P* value based on using Fisher’s exact test

</div>

<div id="Tabb" class="table-wrap">

<div class="caption">

Known-group’s validity: dimension-level response distributions and “no problem” reported for individual dimension across disease severity

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Mild % (<em>n</em>)</th>
<th colspan="3" style="text-align: left;">Moderate % (<em>n</em>)</th>
<th colspan="3" style="text-align: left;">Severe % (<em>n</em>)</th>
</tr>
<tr>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>0–3 years</em></td>
<td colspan="3" style="text-align: left;"><em>n</em> = 74</td>
<td colspan="3" style="text-align: left;"><em>n</em> = 101</td>
<td colspan="3" style="text-align: left;"><em>n</em> = 55</td>
</tr>
<tr>
<td style="text-align: left;"> Movement, % (n)</td>
<td style="text-align: left;">66.2 (49)</td>
<td style="text-align: left;">23.0 (17)</td>
<td style="text-align: left;">10.8 (8)</td>
<td style="text-align: left;">70.3 (71)</td>
<td style="text-align: left;">24.8 (25)</td>
<td style="text-align: left;">5.0 (5)</td>
<td style="text-align: left;">47.3 (26)</td>
<td style="text-align: left;">38.2 (21)</td>
<td style="text-align: left;">14.5 (8)</td>
</tr>
<tr>
<td style="text-align: left;"> Play, %</td>
<td style="text-align: left;">70.3 (52)</td>
<td style="text-align: left;">20.3 (15)</td>
<td style="text-align: left;">9.5 (7)</td>
<td style="text-align: left;">64.4 (65)</td>
<td style="text-align: left;">26.7 (27)</td>
<td style="text-align: left;">8.9 (9)</td>
<td style="text-align: left;">49.1 (27)</td>
<td style="text-align: left;">32.7 (18)</td>
<td style="text-align: left;">18.2 (10)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain, %</td>
<td style="text-align: left;">52.7 (39)</td>
<td style="text-align: left;">41.9 (31)</td>
<td style="text-align: left;">5.4 (4)</td>
<td style="text-align: left;">59.4 (60)</td>
<td style="text-align: left;">34.7 (35)</td>
<td style="text-align: left;">5.9 (6)</td>
<td style="text-align: left;">34.5 (19)</td>
<td style="text-align: left;">49.1 (27)</td>
<td style="text-align: left;">16.4 (9)</td>
</tr>
<tr>
<td style="text-align: left;"> Social interaction, %</td>
<td style="text-align: left;">73.0 (54)</td>
<td style="text-align: left;">24.3 (18)</td>
<td style="text-align: left;">2.7 (2)</td>
<td style="text-align: left;">69.3 (70)</td>
<td style="text-align: left;">24.8 (25)</td>
<td style="text-align: left;">5.9 (6)</td>
<td style="text-align: left;">58.2 (32)</td>
<td style="text-align: left;">32.7 (18)</td>
<td style="text-align: left;">9.1 (5)</td>
</tr>
<tr>
<td style="text-align: left;"> Communication, %</td>
<td style="text-align: left;">77.0 (57)</td>
<td style="text-align: left;">20.3 (15)</td>
<td style="text-align: left;">2.7 (2)</td>
<td style="text-align: left;">78.2 (79)</td>
<td style="text-align: left;">19.8 (20)</td>
<td style="text-align: left;">2.0 (2)</td>
<td style="text-align: left;">65.5 (36)</td>
<td style="text-align: left;">23.6 (13)</td>
<td style="text-align: left;">10.9 (6)</td>
</tr>
<tr>
<td style="text-align: left;"> Eating, %</td>
<td style="text-align: left;">63.5 (47)</td>
<td style="text-align: left;">25.7 (19)</td>
<td style="text-align: left;">10.8 (8)</td>
<td style="text-align: left;">54.5 (55)</td>
<td style="text-align: left;">37.6 (38)</td>
<td style="text-align: left;">7.9 (8)</td>
<td style="text-align: left;">32.7 (18)</td>
<td style="text-align: left;">52.7 (29)</td>
<td style="text-align: left;">14.5 (8)</td>
</tr>
<tr>
<td style="text-align: left;"><em>4–5 years</em></td>
<td colspan="3" style="text-align: left;"><em>n</em> = 50</td>
<td colspan="3" style="text-align: left;"><em>n</em> = 60</td>
<td colspan="3" style="text-align: left;"><em>n</em> = 38</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility, %</td>
<td style="text-align: left;">90.0 (45)</td>
<td style="text-align: left;">8.0 (4)</td>
<td style="text-align: left;">2.0 (1)</td>
<td style="text-align: left;">76.7 (46)</td>
<td style="text-align: left;">20.0 (12)</td>
<td style="text-align: left;">3.3 (2)</td>
<td style="text-align: left;">47.4 (18)</td>
<td style="text-align: left;">31.6 (12)</td>
<td style="text-align: left;">21.1 (8)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after myself, %</td>
<td style="text-align: left;">80.0 (40)</td>
<td style="text-align: left;">18.0 (9)</td>
<td style="text-align: left;">2.0 (1)</td>
<td style="text-align: left;">61.7 (37)</td>
<td style="text-align: left;">33.3 (20)</td>
<td style="text-align: left;">5.0 (3)</td>
<td style="text-align: left;">39.5 (15)</td>
<td style="text-align: left;">39.5 (15)</td>
<td style="text-align: left;">21.1 (8)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activity, %</td>
<td style="text-align: left;">82.0 (41)</td>
<td style="text-align: left;">16.0 (8)</td>
<td style="text-align: left;">2.0 (1)</td>
<td style="text-align: left;">60.0 (36)</td>
<td style="text-align: left;">26.7 (16)</td>
<td style="text-align: left;">13.3 (8)</td>
<td style="text-align: left;">47.4 (18)</td>
<td style="text-align: left;">34.2 (13)</td>
<td style="text-align: left;">18.4 (7)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort, %</td>
<td style="text-align: left;">72.0 (36)</td>
<td style="text-align: left;">24.0 (12)</td>
<td style="text-align: left;">4.0 (2)</td>
<td style="text-align: left;">40.0 (24)</td>
<td style="text-align: left;">45.0 (27)</td>
<td style="text-align: left;">15.0 (9)</td>
<td style="text-align: left;">23.7 (9)</td>
<td style="text-align: left;">52.6 (20)</td>
<td style="text-align: left;">23.7 (9)</td>
</tr>
<tr>
<td style="text-align: left;"> Feeling worried/sad/unhappy, %</td>
<td style="text-align: left;">84.0 (42)</td>
<td style="text-align: left;">14.0 (7)</td>
<td style="text-align: left;">2.0 (1)</td>
<td style="text-align: left;">46.7 (28)</td>
<td style="text-align: left;">41.7 (25)</td>
<td style="text-align: left;">11.7 (7)</td>
<td style="text-align: left;">39.5 (15)</td>
<td style="text-align: left;">36.8 (14)</td>
<td style="text-align: left;">23.7 (9)</td>
</tr>
<tr>
<td style="text-align: left;"><em>6–18 years</em></td>
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
<td style="text-align: left;"><em>Self-report</em></td>
<td style="text-align: left;"><em>n</em> = 172</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 214</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 59</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Mobility, %</td>
<td style="text-align: left;">84.3 (145)</td>
<td style="text-align: left;">12.8 (22)</td>
<td style="text-align: left;">2.9 (5)</td>
<td style="text-align: left;">65.0 (139)</td>
<td style="text-align: left;">27.1 (58)</td>
<td style="text-align: left;">7.9 (17)</td>
<td style="text-align: left;">50.8 (30)</td>
<td style="text-align: left;">39.0 (23)</td>
<td style="text-align: left;">10.2 (6)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after myself, %</td>
<td style="text-align: left;">84.9 (146)</td>
<td style="text-align: left;">11.6 (20)</td>
<td style="text-align: left;">3.5 (6)</td>
<td style="text-align: left;">70.6 (151)</td>
<td style="text-align: left;">23.4 (50)</td>
<td style="text-align: left;">6.1 (13)</td>
<td style="text-align: left;">54.2 (32)</td>
<td style="text-align: left;">27.1 (16)</td>
<td style="text-align: left;">18.6 (11)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activity, %</td>
<td style="text-align: left;">75.6 (130)</td>
<td style="text-align: left;">18.0 (31)</td>
<td style="text-align: left;">6.4 (11)</td>
<td style="text-align: left;">59.8 (128)</td>
<td style="text-align: left;">32.7 (70)</td>
<td style="text-align: left;">7.5 (16)</td>
<td style="text-align: left;">45.8 (27)</td>
<td style="text-align: left;">39.0 (23)</td>
<td style="text-align: left;">15.3 (9)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort, %</td>
<td style="text-align: left;">65.7 (113)</td>
<td style="text-align: left;">30.2 (52)</td>
<td style="text-align: left;">4.1 (7)</td>
<td style="text-align: left;">41.1 (88)</td>
<td style="text-align: left;">43.0 (92)</td>
<td style="text-align: left;">15.9 (34)</td>
<td style="text-align: left;">28.8 (17)</td>
<td style="text-align: left;">37.3 (22)</td>
<td style="text-align: left;">33.9 (20)</td>
</tr>
<tr>
<td style="text-align: left;"> Feeling worried/sad/unhappy, %</td>
<td style="text-align: left;">71.5 (123)</td>
<td style="text-align: left;">23.3 (40)</td>
<td style="text-align: left;">5.2 (9)</td>
<td style="text-align: left;">56.5 (121)</td>
<td style="text-align: left;">30.8 (66)</td>
<td style="text-align: left;">12.6 (27)</td>
<td style="text-align: left;">37.3 (22)</td>
<td style="text-align: left;">49.2 (29)</td>
<td style="text-align: left;">13.6 (8)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Proxy</em></td>
<td style="text-align: left;"><em>n</em> = 187</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 228</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 68</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Mobility, %</td>
<td style="text-align: left;">80.2 (150)</td>
<td style="text-align: left;">15.0 (28)</td>
<td style="text-align: left;">4.8 (9)</td>
<td style="text-align: left;">68.0 (155)</td>
<td style="text-align: left;">24.6 (56)</td>
<td style="text-align: left;">7.5 (17)</td>
<td style="text-align: left;">50.0 (34)</td>
<td style="text-align: left;">36.8 (25)</td>
<td style="text-align: left;">13.2 (9)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after myself, %</td>
<td style="text-align: left;">80.7 (151)</td>
<td style="text-align: left;">12.8 (24)</td>
<td style="text-align: left;">6.4 (12)</td>
<td style="text-align: left;">73.7 (168)</td>
<td style="text-align: left;">18.0 (41)</td>
<td style="text-align: left;">8.3 (19)</td>
<td style="text-align: left;">52.9 (36)</td>
<td style="text-align: left;">25.0 (17)</td>
<td style="text-align: left;">22.1 (15)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activity, %</td>
<td style="text-align: left;">70.1 (131)</td>
<td style="text-align: left;">20.3 (38)</td>
<td style="text-align: left;">9.6 (18)</td>
<td style="text-align: left;">54.8 (125)</td>
<td style="text-align: left;">34.6 (79)</td>
<td style="text-align: left;">10.5 (24)</td>
<td style="text-align: left;">35.3 (24)</td>
<td style="text-align: left;">39.7 (27)</td>
<td style="text-align: left;">25.0 (17)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort, %</td>
<td style="text-align: left;">61.0 (114)</td>
<td style="text-align: left;">28.3 (53)</td>
<td style="text-align: left;">10.7 (20)</td>
<td style="text-align: left;">43.0 (98)</td>
<td style="text-align: left;">37.7 (86)</td>
<td style="text-align: left;">19.3 (44)</td>
<td style="text-align: left;">32.4 (22)</td>
<td style="text-align: left;">36.8 (25)</td>
<td style="text-align: left;">30.9 (21)</td>
</tr>
<tr>
<td style="text-align: left;"> Feeling worried/sad/unhappy, %</td>
<td style="text-align: left;">67.9 (127)</td>
<td style="text-align: left;">24.6 (46)</td>
<td style="text-align: left;">7.5 (14)</td>
<td style="text-align: left;">49.6 (113)</td>
<td style="text-align: left;">39.9 (91)</td>
<td style="text-align: left;">10.5 (24)</td>
<td style="text-align: left;">36.8 (25)</td>
<td style="text-align: left;">45.6 (31)</td>
<td style="text-align: left;">17.6 (12)</td>
</tr>
</tbody>
</table>

</div>

<div id="Tabc" class="table-wrap">

<div class="caption">

Responsiveness: change in percentage of respondent reporting “no problem” for each dimension between illness and clinical recovery or improved OHA

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">COVID recovery</th>
<th colspan="2" style="text-align: left;">Improved OHA</th>
</tr>
<tr>
<th style="text-align: left;">Baseline, % (<em>n</em>)</th>
<th style="text-align: left;">Follow-up, % (<em>n</em>)</th>
<th style="text-align: left;">Baseline, % (<em>n</em>)</th>
<th style="text-align: left;">Follow-up, % (<em>n</em>)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>0–3 years</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 69</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 64</td>
</tr>
<tr>
<td style="text-align: left;"> Movement, % (n)</td>
<td style="text-align: left;">37.7 (26)</td>
<td style="text-align: left;">88.4 (61)</td>
<td style="text-align: left;">37.5 (24)</td>
<td style="text-align: left;">93.8 (60)</td>
</tr>
<tr>
<td style="text-align: left;"> Play, %</td>
<td style="text-align: left;">31.9 (22)</td>
<td style="text-align: left;">89.9 (62)</td>
<td style="text-align: left;">29.7 (19)</td>
<td style="text-align: left;">92.2 (59)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain, %</td>
<td style="text-align: left;">30.4 (21)</td>
<td style="text-align: left;">85.5 (59)</td>
<td style="text-align: left;">32.8 (21)</td>
<td style="text-align: left;">89.1 (57)</td>
</tr>
<tr>
<td style="text-align: left;"> Social interaction, %</td>
<td style="text-align: left;">46.4 (32)</td>
<td style="text-align: left;">87.0 (60)</td>
<td style="text-align: left;">45.3 (29)</td>
<td style="text-align: left;">87.5 (56)</td>
</tr>
<tr>
<td style="text-align: left;"> Communication, %</td>
<td style="text-align: left;">68.1 (47)</td>
<td style="text-align: left;">87.0 (60)</td>
<td style="text-align: left;">67.2 (43)</td>
<td style="text-align: left;">89.1 (57)</td>
</tr>
<tr>
<td style="text-align: left;"> Eating, %</td>
<td style="text-align: left;">39.1 (27)</td>
<td style="text-align: left;">81.2 (56)</td>
<td style="text-align: left;">35.9 (23)</td>
<td style="text-align: left;">84.4 (54)</td>
</tr>
<tr>
<td style="text-align: left;"><em>4–5 years</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 48</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 46</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility, %</td>
<td style="text-align: left;">56.3 (27)</td>
<td style="text-align: left;">91.7 (44)</td>
<td style="text-align: left;">50.0 (23)</td>
<td style="text-align: left;">89.1 (41)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after myself, %</td>
<td style="text-align: left;">39.6 (19)</td>
<td style="text-align: left;">91.7 (44)</td>
<td style="text-align: left;">32.6 (15)</td>
<td style="text-align: left;">87.0 (40)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activity, %</td>
<td style="text-align: left;">37.5 (18)</td>
<td style="text-align: left;">81.3 (39)</td>
<td style="text-align: left;">34.8 (16)</td>
<td style="text-align: left;">73.9 (34)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort, %</td>
<td style="text-align: left;">16.7 (8)</td>
<td style="text-align: left;">81.3 (39)</td>
<td style="text-align: left;">13.0 (6)</td>
<td style="text-align: left;">78.3 (36)</td>
</tr>
<tr>
<td style="text-align: left;"> Feeling worried/sad/unhappy, %</td>
<td style="text-align: left;">39.6 (19)</td>
<td style="text-align: left;">68.8 (33)</td>
<td style="text-align: left;">30.4 (14)</td>
<td style="text-align: left;">67.4 (31)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>6–18 years</em></td>
</tr>
<tr>
<td style="text-align: left;"><em>Self-report</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 132</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 138</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility, %</td>
<td style="text-align: left;">40.2 (53)</td>
<td style="text-align: left;">90.9 (120)</td>
<td style="text-align: left;">37.7 (52)</td>
<td style="text-align: left;">91.3 (126)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after myself, %</td>
<td style="text-align: left;">42.4 (56)</td>
<td style="text-align: left;">91.7 (121)</td>
<td style="text-align: left;">39.9 (55)</td>
<td style="text-align: left;">92.0 (127)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activity, %</td>
<td style="text-align: left;">31.1 (41)</td>
<td style="text-align: left;">88.6 (117)</td>
<td style="text-align: left;">29.0 (40)</td>
<td style="text-align: left;">89.9 (124)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort, %</td>
<td style="text-align: left;">15.9 (21)</td>
<td style="text-align: left;">80.3 (106)</td>
<td style="text-align: left;">14.5 (20)</td>
<td style="text-align: left;">81.2 (112)</td>
</tr>
<tr>
<td style="text-align: left;"> Feeling worried/sad/unhappy, %</td>
<td style="text-align: left;">30.3 (40)</td>
<td style="text-align: left;">76.5 (101)</td>
<td style="text-align: left;">28.3 (39)</td>
<td style="text-align: left;">77.5 (107)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Proxy</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 141</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>n</em> = 147</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility, %</td>
<td style="text-align: left;">41.8 (59)</td>
<td style="text-align: left;">91.5 (129)</td>
<td style="text-align: left;">40.1 (59)</td>
<td style="text-align: left;">93.2 (137)</td>
</tr>
<tr>
<td style="text-align: left;"> Looking after myself, %</td>
<td style="text-align: left;">51.8 (73)</td>
<td style="text-align: left;">90.1 (127)</td>
<td style="text-align: left;">50.3 (74)</td>
<td style="text-align: left;">89.8 (132)</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activity, %</td>
<td style="text-align: left;">27.7 (39)</td>
<td style="text-align: left;">87.2 (123)</td>
<td style="text-align: left;">27.2 (40)</td>
<td style="text-align: left;">87.8 (129)</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort, %</td>
<td style="text-align: left;">16.3 (23)</td>
<td style="text-align: left;">75.9 (107)</td>
<td style="text-align: left;">15.0 (22)</td>
<td style="text-align: left;">75.5 (111)</td>
</tr>
<tr>
<td style="text-align: left;"> Feeling worried/sad/unhappy, %</td>
<td style="text-align: left;">23.4 (33)</td>
<td style="text-align: left;">68.1 (96)</td>
<td style="text-align: left;">21.8 (32)</td>
<td style="text-align: left;">67.3 (99)</td>
</tr>
</tbody>
</table>

OHA – overall health assessment

</div>

### Acknowledgements

The authors would like to thank all the parents and patients who made this study possible and the EuroQol Research Foundation for funding this study.

### Author contributions

Concept and design: Yanming Lu, Zhihao Yang, Jan Busschbach; Acquisition of data: Wenjing Zhou, Yaqin Li; Analysis and interpretation of data: Wenjing Zhou, Yaqin Li, Michael Herdman; Drafting of the manuscript: Wenjing Zhou, Yaqin Li; Critical revision of the paper for important intellectual content: Wenjing Zhou, Michael Herdman; Obtaining funding: Wenjing Zhou; Supervision: Jan Busschbach, Michael Herdman, Yanming Lu.

### Funding

This research was supported by a grant from the EuroQol Research Foundation (grant number: EQ Project 1654-TVG).

### Data availability

The data that support the findings of this study are openly available in ‘Mendeley’ at: Wenjing, Zhou (2024), “Psychometric Validation of the Chinese Versions of EQ-5D-Y-3L and EQ-TIPS In Children and Adolescents with COVID-19”, Mendeley Data, V1, doi: 10.17632/w4xxkf7brg.1.

### Code availability

The computer code of this study are available from the corresponding author upon reasonable request.

### Declarations

#### Ethical approval

The ethical conduct of this study was guided by the Declaration of Helsinki and ensured that the rights, well-being, and confidentiality of all participants were upheld. The study received approval from the institutional medical ethical review board of Guizhou Medical University (Approval number: GMU2022303) and provided a strong foundation for the research findings and their implications.

#### Consent to participate

Written informed consent was obtained from the participants.

#### Consent for publication

The authors affirm that human research participants provided informed consent for publication of this article.

#### Conflict of interest

Three of the authors, Herdman, Busschbach, and Yang, are members of the EuroQol Group. They occasionally receive research funding and honoraria from the EuroQol Research Foundation, as Zhou did for the present research. The remaining authors declare no conflicts of interest related to the content of this manuscript.

## References

1. American Academy of Pediatrics: Children and COVID-19: state-level data report. (2023). https://www.aap.org/en/pages/2019-novel-coronavirus-covid-19-infections/children-and-covid-19-state-level-data-report. Accessed 8 May 2023

2. de Marques, D., da Silva Athanasio, B., Sena Oliveira, A.C., Simoes-E-Silva, A.C.: How is COVID-19 pandemic impacting mental health of children and adolescents? Int. J. Disaster Risk Reduct. IJDRR. 51, 101845 (2020). 10.1016/j.ijdrr.2020.10184532929399 10.1016/j.ijdrr.2020.101845PMC7481176

3. Fink, T. T., Marques, H. H. S., Gualano, B., Lindoso, L., Bain, V., Astley, C., Martins, F., Matheus, D., Matsuo, O. M., Suguita, P., Trindade, V., Paula, C. S. Y., Farhat, S. C. L., Palmeira, P., Leal, G. N., Suzuki, L., Odone Filho, V., Carneiro-Sampaio, M., Duarte, A. J. S., Antonangelo, L., ? Zheng, Y.: Persistent symptoms and decreased health-related quality of life after symptomatic pediatric COVID-19: A prospective study in a Latin American tertiary hospital. Clinics. (Sao Paulo, Brazil). 76, e3511 (2021). 10.6061/clinics/2021/e351110.6061/clinics/2021/e3511PMC859559334852145

4. Chernyshov, P.V., Vozianova, S.V., Chubar, O.V.: Quality of Life of Infants, toddlers and preschoolers with Seborrhoeic, allergic contact and atopic dermatitis before and during COVID-19 pandemic. Dermatol. Ther. (Heidelb). 11(6), 2017–2026 (2021). 10.1007/s13555-021-00617-634562266 10.1007/s13555-021-00617-6PMC8475414

5. Ravens-Sieberer, U., Kaman, A., Erhart, M., Devine, J., Schlack, R., Otto, C.: Impact of the COVID-19 pandemic on quality of life and mental health in children and adolescents in Germany. Eur. Child. Adolesc. Psychiatry. 31(6), 879–889 (2022). 10.1007/s00787-021-01726-533492480 10.1007/s00787-021-01726-5PMC7829493

6. Kikkenborg Berg, S., Palm, P., Nygaard, U., Bundgaard, H., Petersen, M.N.S., Rosenkilde, S., Thorsted, A.B., Ersbøll, A.K., Thygesen, L.C., Nielsen, S.D., Vinggaard Christensen, A.: Long COVID symptoms in SARS-CoV-2-positive children aged 0–14 years and matched controls in Denmark (LongCOVIDKidsDK): A national, cross-sectional study. Lancet Child. Adolesc. Health. 6(9), 614–623 (2022). 10.1016/S2352-4642(22)00154-735752194 10.1016/S2352-4642(22)00154-7PMC9221683

7. Kurz, D., Braig, S., Genuneit, J., Rothenbacher, D.: Lifestyle changes, mental health, and health-related quality of life in children aged 6–7 years before and during the COVID-19 pandemic in South Germany. Child. Adolesc. Psychiatry Ment Health. 16(1), 20 (2022). 10.1186/s13034-022-00454-135277185 10.1186/s13034-022-00454-1PMC8915143

8. Wille, N., Badia, X., Bonsel, G., Burström, K., Cavrini, G., Devlin, N., Egmar, A.C., Greiner, W., Gusi, N., Herdman, M., Jelsma, J., Kind, P., Scalone, L., Ravens-Sieberer, U.: Development of the EQ-5D-Y: A child-friendly version of the EQ-5D. Qual. Life Res. 19(6), 875–886 (2010). 10.1007/s11136-010-9648-y10.1007/s11136-010-9648-yPMC289261120405245

9. EQ-5DEuroQol Research Foundation, User Guide, -Y.: (2020). https://euroqol.org/publications/user-guides. Accessed 23 Jan 2022

10. Kulpeng, W., Sornsrivichai, V., Chongsuvivatwong, V., Rattanavipapong, W., Leelahavarong, P., Cairns, J., Lubell, Y., Teerawattananon, Y.: Variation of health-related quality of life assessed by caregivers and patients affected by severe childhood infections. BMC Pediatr. 13, 122 (2013). 10.1186/1471-2431-13-12223941314 10.1186/1471-2431-13-122PMC3751113

11. Verstraete, J., Scott, D.: Comparison of the EQ-5D-Y-5L, EQ-5D-Y-3L and PedsQL in children and adolescents. J. Patient Rep. Outcomes. 6(1), 67 (2022). 10.1186/s41687-022-00480-935708825 10.1186/s41687-022-00480-9PMC9203648

12. Yang, Z., Jiang, J., Wang, P., Jin, X., Wu, J., Fang, Y., Feng, D., Xi, X., Li, S., Jing, M., Zheng, B., Huang, W., Luo, N.: Estimating an EQ-5D-Y-3L value set for China. PharmacoEconomics. 40(Suppl 2), 147–155 (2022). 10.1007/s40273-022-01216-936396878 10.1007/s40273-022-01216-9PMC9758244

13. Shiroiwa, T., Fukuda, T., Shimozuma, K.: Psychometric properties of the Japanese version of the EQ-5D-Y by self-report and proxy-report: Reliability and construct validity. Qual. Life Res. 28(11), 3093–3105 (2019). 10.1007/s11136-019-02238-131243620 10.1007/s11136-019-02238-1PMC6803591

14. Gusi, N., Perez-Sousa, M.A., Gozalo-Delgado, M., Olivares, P.R.: Validez y fiabilidad de la versión proxy del EQ-5D-Y en español [Validity and reliability of the Spanish EQ-5D-Y proxy version]. Pediatr. (Barc). 81(4), 212–219 (2014). 10.1016/j.anpedi.2013.11.02810.1016/j.anpedi.2013.11.02824411558

15. Zhou, W., Shen, A., Yang, Z., Wang, P., Wu, B., Herdman, M., Luo, N.: Patient-caregiver agreement and test-retest reliability of the EQ-5D-Y-3L and EQ-5D-Y-5L in paediatric patients with hae- matological malignancies. Eur. J. Health Econ. 22(7), 1103–1113 (2021). 10.1007/s10198-021-01309-w33950465 10.1007/s10198-021-01309-wPMC8318941

16. Jeanbert, E., Baumann, C., Todorović, A., et al.: Factors Associated with discrepancy of Child-Adolescent/Parent reported quality of life in the era of COVID-19. Int. J. Environ. Res. Public. Health. 19(21), 14359 (2022). 10.3390/ijerph19211435936361238 10.3390/ijerph192114359PMC9654617

17. Verstraete, J., Ramma, L., Jelsma, J.: Influence of the child’s perceived general health on the primary caregiver’s health status. Health Qual. Life Outcomes. 16(1), 8 (2018). 10.1186/s12955-018-0840-z29321017 10.1186/s12955-018-0840-zPMC5763523

18. Verstraete, J., Amien, R.: Cross-cultural adaptation and validation of the EuroQoL Toddler and infant populations instrument into Afrikaans for South Africa. Value Health Reg. Issues. 35, 78–86 (2023). 10.1016/j.vhri.2023.01.00936905789 10.1016/j.vhri.2023.01.009

19. Verstraete, J., Ramma, L., Jelsma, J.: Validity and reliability testing of the Toddler and Infant (TANDI) Health Related Quality of Life instrument for very young children. J. Patient Rep. Outcomes. 4(1), 94 (2020). 10.1186/s41687-020-00251-433165662 10.1186/s41687-020-00251-4PMC7652950

20. EuroQol Research Foundation. EQ-5D-5L User Guide: (2019). https://euroqol.org/publications/user-guides. Accessed 6 Sep 2023

21. Rabin, R., Gudex, C., Selai, C., Herdman, M.: From translation to version management: A history and review of methods for the cultural adaptation of the EuroQol five-dimensional questionnaire. Value Health. 17(1), 70–76 (2014). 10.1016/j.jval.2013.10.00624438719 10.1016/j.jval.2013.10.006

22. Idler, E.L., Benyamini, Y.: Self-rated health and mortality: A review of twenty-seven community studies. J. Health Soc. Behav. 38(1), 21–37 (1997)9097506

23. Diagnosis and Treatment Protocol for COVID-19: Infection (Trial Version 10). In Chinese. http://www.nhc.gov.cn/xcs/zhengcwj/202301/32de5b2ff9bf4eaa88e75bdf7223a65a/files/460b0e7b19bd42f3bba00c1efb9b6811. Accessed 6 Jan 2023

24. Devlin, N., Parkin, D., Janssen, B.: Methods for Analysing and Reporting EQ-5D Data. Springer, Cham, Switzerland (2020)33347096

25. Cohen, J.: Statistical Power Analysis for Behavioral Science, 2nd edn. Lawrence Earlbaum Associates, Hilsdale (1988)

26. Gwet, K.L.: Computing inter-rater reliability and its variance in the presence of high agreement. Br. J. Math. Stat. Psychol. 61(1), 29–48 (2008). 10.1348/000711006X12660018482474 10.1348/000711006X126600

27. Wongpakaran, N., Wongpakaran, T., Wedding, D., Gwet, K.L.: A comparison of Cohen’s Kappa and Gwet’s AC1 when calculating inter-rater reliability coefficients: A study conducted with personality disorder samples. BMC Med. Res. Methodol. 13, 61 (2013). 10.1186/1471-2288-13-6123627889 10.1186/1471-2288-13-61PMC3643869

28. Koo, T.K., Li, M.Y.: A Guideline of selecting and reporting Intraclass correlation coefficients for Reliability Research. J. Chiropr. Med. 15(2), 155–163 (2016). 10.1016/j.jcm.2016.02.01227330520 10.1016/j.jcm.2016.02.012PMC4913118

29. Morris, S.B., DeShon, R.P.: Combining effect size estimates in meta-analysis with repeated measures and independent-groups designs. Psychol. Methods. 7(1), 105–125 (2002). 10.1037/1082-989x.7.1.10511928886 10.1037/1082-989x.7.1.105

30. Verstraete, J., Lloyd, A.J., Jelsma, J.: Performance of the Toddler and Infant (TANDI) Health-Related Quality of Life Instrument in 3-4-year-old children. Child. (Basel). 8(10), 920 (2021). 10.3390/children810092010.3390/children8100920PMC853435234682184

31. Perez Sousa, M., Sánchez-Toledo, O., P. R., Gusi Fuerte, N.: Parent-child discrepancy in the assessment of health- related quality of life using the EQ-5D-Y questionnaire. Arch. Argent. Pediatr. 115(6), 541–546 (2017). 10.5546/aap.2017.eng.541 English, Spanish29087107 10.5546/aap.2017.eng.541

32. Abraham, S., Edginton, E., Cottrell, D., Tubeuf, S.: Measuring health-related quality of life measures in children: Lessons from a pilot study. Res. Psychother. 25(1), 581 (2022). 10.4081/ripppo.2022.58135532026 10.4081/ripppo.2022.581PMC9153752

33. Bray, N., Noyes, J., Harris, N., Edwards, R.T.: Measuring the health-related quality of life of children with impaired mobility: Examining correlation and agreement between children and parent proxies. BMC Res. Notes. 10(1), 377 (2017). 10.1186/s13104-017-2683-928797288 10.1186/s13104-017-2683-9PMC5553751

34. Tan, R.L., Soh, S.Z.Y., Chen, L.A., Herdman, M., Luo, N.: Psychometric properties of generic preference-weighted measures for children and adolescents. Syst. Rev. PharmacoEconomics. 41(2), 155–174 (2023). 10.1007/s40273-022-01205-y10.1007/s40273-022-01205-y36404365

35. Wong, C.K.H., Cheung, P.W.H., Luo, N., Lin, J., Cheung, J.P.Y.: Responsiveness of EQ-5D Youth version 5-level (EQ-5D-5L-Y) and 3-level (EQ-5D-3L-Y) in patients with idiopathic scoliosis. Spine (Phila Pa. 1976). 44(21), 1507–1514 (2019). 10.1097/BRS.000000000000311631634302 10.1097/BRS.0000000000003116

36. Vallejo-Slocker, L., Sanz, J., García-Vera, M.P., Fresneda, J., Vallejo, M.A.: Mental Health, Quality of Life and coping strategies in vulnerable children during the COVID-19 pandemic. Psicothema. 34(2), 249–258 (2022). 10.7334/psicothema2021.46735485538 10.7334/psicothema2021.467

37. Lin, J., Wong, C.K.H., Cheung, P.W.H., Luo, N., Cheung, J.P.Y.: Feasibility of proxy-reported EQ-5D-3L-Y and its agreement in self-reported EQ-5D-3L-Y for patients with adolescent idiopathic scoliosis. Spine (Phila Pa. 1976). 45(13), E799–E807 (2020). 10.1097/BRS.000000000000343132539293 10.1097/BRS.0000000000003431

38. Kreimeier, S., Åström, M., Burström, K., Egmar, A.C., Gusi, N., Herdman, M., Kind, P., Perez-Sousa, M.A., Greiner, W.: EQ-5D-Y-5L: Developing a revised EQ-5D-Y with increased response categories. Qual. Life Res. 28(7), 1951–1961 (2019). 10.1007/s11136-019-02115-x30739287 10.1007/s11136-019-02115-xPMC6571085

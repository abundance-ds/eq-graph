---
project_id: "1599-RA"
work_id: "doi:10.1186/s12955-026-02521-z"
doi: "10.1186/s12955-026-02521-z"
pmid: "41943046"
pmcid: "PMC13182084"
title: "Validity and responsiveness of the EQ-5D-5L, EQ-HWB and EQ-HWB-9 to measure health and wellbeing impact of heatwaves among older adults"
journal: "Health and Quality of Life Outcomes"
publication_date: "2026-04-06"
volume: "24"
authors:
  - name: "Meixia Liao"
    affiliation_ids:
      - "Aff1"
  - name: "Fanni Rencz"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Zhihao Yang"
    affiliation_ids:
      - "Aff4"
  - name: "Jianjun Xiang"
    affiliation_ids:
      - "Aff5"
  - name: "Nan Luo"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Saw Swee Hock School of Public Health, National University of Singapore, Singapore, 117549 Singapore"
  - id: "Aff2"
    name: "Department of Health Policy, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff3"
    name: "EuroQol Research Foundation, Rotterdam, The Netherlands"
  - id: "Aff4"
    name: "Health Services Management Department, Guizhou Medical University, Guiyang, 561113 China"
  - id: "Aff5"
    name: "Department of Preventive Medicine, Key Laboratory of Environment and Health of Fujian Higher Education Institutes, School of Public Health, Fujian Medical University, Fuzhou, 350122 China"
licence: "cc-by-nc-nd"
source_file: "input/projects/1599-RA/papers/doi_10.1186_s12955-026-02521-z.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13182084/fullTextXML"
source_method: "epmc_xml"
source_sha256: "c48debce3442c3ec97a59362172314c7e8f71c5abf4931323d256aece53c2300"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Validity and responsiveness of the EQ-5D-5L, EQ-HWB and EQ-HWB-9 to measure health and wellbeing impact of heatwaves among older adults

## Abstract

### Background

The health impact of heatwaves is usually assessed using mortality, morbidity and healthcare service utilization. This study explored the feasibility of using subjective measures to capture and quantify the impact of heatwaves on the health and wellbeing of older adults.

### Methods

A cohort of residents aged ≥ 60 living in Fuzhou city, China, were surveyed four times: before summer in May, during heatwaves in June to July and August, and after summer in October, 2023. At all timepoints, the EQ-5D-5L, experimental EQ-HWB and self-designed questions assessing self-perceived effects of heatwaves were administered through one-on-one, face-to-face interviews. We examined the known-groups validity (using Cohen’s d effect sizes) and responsiveness (using standardized response mean \[SRM\]) of EQ-5D-5L, EQ-HWB and EQ-HWB-9 (including index values and level sum scores \[LSSs\]).

### Results

The responses of 579, 510, 473 and 508 residents were analysed in the four waves of survey, respectively. The ceiling effects for EQ-5D-5L items ranged from 58.2% (*pain/discomfort*) to 94.3% (*self-care*), while for EQ-HWB items, it ranged from 32.3% (*accepted*) to 94.0% (*personal care*). The EQ-5D-5L and EQ-HWB-9 index values, and EQ-HWB LSSs demonstrated discriminative ability in distinguishing between different groups based on the self-perceived impact of heatwaves, with most of the effect sizes being small (Cohen’s d: 0.04–0.31 for EQ-5D-5L; 0.16–0.34 for EQ-HWB-9; 0.28–0.45 for EQ-HWB). We found negligible responsiveness to improvements in self-perceived effects of heat (SRM: 0.07 to 0.18). Unexpectedly, improved health and wellbeing were observed during the first heatwave compared to pre-heatwave.

### Conclusion

The EQ-5D-5L, EQ-HWB and EQ-HWB-9 demonstrated satisfactory known-groups validity but limited responsiveness in measuring the health and wellbeing impact of heatwaves among Chinese older adults. Future research is recommended to further evaluate these measures as well as other outcomes measures for the purpose of quantifying the health and wellbeing impacts of heatwaves and other climate events.

### Supplementary information

The online version contains supplementary material available at 10.1186/s12955-026-02521-z.

**Keywords:** Heatwave, Health, Wellbeing, EQ-5D-5L, EQ-HWB, EQ-HWB-9, Psychometric assessment, Older adult

Received 2025 Oct 30; Accepted 2026 Mar 14; Collection date 2026.

## Introduction

Heatwaves, or periods of excessively hot weather, are getting frequent and intense worldwide, which is considered to be related to climate change \[1\]. In 2022, heatwaves affected millions of people in Asia, America, Europe, North Africa, and Oceania \[2\]. In addition to threatening food production and economies, heatwaves have profound impact on people’s health, particularly the health of vulnerable populations \[3\]. For example, in 2022, there were an estimated 50,900 heatwave-related deaths in China, with 78% occurring among individuals aged 65 and above, underscoring the heightened impact of heatwave on older adults \[4\]. Heatwaves are also associated with increased hospital admissions and emergency department visits \[5\] and heightened workplace injuries \[6\].

To date, research on the health impact of heatwaves has been focused on health outcomes that can only be objectively measured. The focal points of studies involving working populations exposed to high environment temperature have been injuries, disabilities, productivity loss, and their social and economic consequences \[7\]. Research on vulnerable populations such as the elderly has mainly quantified the impact of high temperature in terms of mortality and morbidity. The effects of heatwave exposure on people’s functioning and wellbeing, or health-related quality of life (HRQoL), have not been studied. Given that millions of people around the world are exposed to heatwaves every year, the loss in HRQoL due to heatwaves could be tremendous. Without factoring in this humanistic health burden, the true health impact of heatwaves and the effectivensss of interventions mitigating this impact could be significantly underestimated. Such underestimations could subsequently misinform policies and decision making in the fight against climate change. Therefore, there is a need to fill this knowledge gap in climate change research.

There is currently no well-established theoretical framework for conceptualising health and wellbeing in the context of heatwave research. Nevertheless, existing evidence suggests that exposure to extreme heat and heatwaves affects health and wellbeing through multiple interrelated physiological, psychological, and behavioural pathways. During heat extremes, the body’s thermoregulatory capacity is challenged, increasing the risk of heat-related illness and exacerbating pre-existing conditions through mechanisms such as thermal stress, dehydration, and haemodynamic strain \[8\]. These physiological responses may manifest as physical discomfort, fatigue, reduced appetite, difficulty breathing and reduced functional capacity \[9\], as well as other direct physical symptoms such as skin irritation and rashes \[10\] and heat- or UV-related visual disturbances \[11\]. Heat exposure is also consistently associated with disturbances in sleep quality and duration \[12, 13\], which can impair cognitive performance, emotional regulation, and overall wellbeing. In addition, existing evidence indicates that elevated ambient temperatures and heatwave events are associated with poor mental health, such as increased risks of depression, mania, and suicide \[14–16\]. Emerging evidence further suggests that extreme heat may adversely affect cognitive functioning and social participation, as individuals adapt their daily routines and reduce outdoor or social activities to cope with heat stress \[17, 18\]. Collectively, these pathways provide a conceptual basis for how heatwave may influence multiple dimensions of health and wellbeing.

The EQ-5D \[19\] is a well accepted generic preference-based HRQoL measure for quantifying the effects of health conditions and health technologies such as vaccines, drug therapy, medical devices, and clinical procedures. Although the EQ-5D is primarily used in clinical research, economic evaluations and population health surveys \[20\], it has also been used to measure the health impact of disasters and changed environment \[14, 21–23\], with some promising evidence supporting its usefulness. For example, in a longitudinal study, EQ-5D was shown to capture the health impact of armed conflicts in Colombia \[23\]. In a retrospective study of typhoon survivors, the EQ visual analogue scale (VAS) score was higher among those assigned a volunteer worker but lower among those who lost a family member \[21\]. These studies suggest that the EQ-5D can be useful in studying health hazards beyond diseases.

It is unknown whether EQ-5D is able to capture the adverse impact of extreme weather events, such as heatwaves, as the content of the EQ-5D descriptive system—covering mobility, self-care, usual activities, pain/discomfort, and anxiety/depression—does not provide a clear indication. On one hand, the pain/discomfort, usual activities, and anxiety/depression items may be useful since heatwaves may cause physical discomfort \[8\], work productivity loss \[8\], and mental health problems \[14, 16\]. On the other hand, the EQ-5D lacks items that directly capture the impact of heatwaves on other health dimensions such as sleep \[12, 13\], cognition \[17\], and social activities \[18\]. Recent research has explored the development of a culturally relevant climate adaptation item as a supplementary item (i.e. bolt-on) for the EQ-5D-5L in the Chinese population \[24, 25\]. The newly developed measures for health and wellbeing, EuroQol Health and Wellbeing instrument (EQ-HWB) and its shorter version, EQ-HWB-9 \[26\], may also be useful for assessing the diverse impacts of extreme weather events. The EQ-HWB assesses health and wellbeing across seven domains: activity, autonomy, cognition, feelings and emotions, relationships, physical sensations, and self-identity, while the EQ-HWB-9 covers six domains, excluding self-identity. The EQ-HWB and EQ-HWB-9 have been developed for the assessment of health and wellbeing in populations such as, long-term patients, social care users and carers, particularly in contexts where cross-sectorial decision making may be relevant. However, there is a lack of evidence regarding their application in heatwave research.

This study aimed to evaluate the measurement performance of the EQ-5D-5L, EQ-HWB, and EQ-HWB-9 instruments in capturing health and wellbeing issues experienced among older adults during heatwaves by examining response distributions, ceiling and floor effects, known-groups validity, and responsiveness.

## Methods

### Study design

We conducted an observational cohort study of older adults to measure their health and wellbeing. We planned four waves of data collection, each at a different time in 2023, including early summer in May before heatwaves began (pre-heatwave), the first and a subsequent heatwave in June to August (heatwave 1 and heatwave 2), and in autumn in October (post-heatwave). We chose to study older adults because they are particularly susceptible to heat-related illness and mortality due to age-related declines in thermoregulation, higher prevalence of chronic conditions, and reduced physiological and social adaptability \[4, 27, 28\].

We conducted the study in Fuzhou city, the capital city of Fujian Province in southeast China, which has a humid subtropical climate characterized by hot and humid summers. As there is no internationally agreed definition of heatwave, we adopted China Meteorological Administration’s definition, which states that a heatwave is a continuous occurrence of daily maximum temperatures of ≥ 35 °C for three days \[29\]. According to historical meteorological data, multiple heatwaves occurred in July and August in Fuzhou in the past 23 years. We recruited a cohort of older residents from two urban communities, most of whom resided in reinforced-concrete apartments equipped with electric fans or air-conditioning. There were no city-wide closures of businesses or schools during heatwaves, but government-issued heat alerts and public health advisories were in place.

The longitudinal design aimed to assess the responsiveness of the EQ-5D-5L and EQ-HWB instruments against the hypothesis that the scores would change from pre-heatwave to heatwave and from heatwave to post-heatwave. We hypothesized that health and wellbeing would decline during heatwaves compared to pre-heatwave and post-heatwave periods. As there were no previous heatwave studies using these instruments, we conservatively assumed that the mean change in the EQ-5D-5L index value could be as small as 0.03, with a standard deviation of up to 0.20. Although small, a systematic review suggests that a change of 0.03 could be meaningful in certain contexts \[30\]. Based on this assumption, we determined that a sample of 351 individuals was needed to ensure a statistical power of 80% at a significance level of 0.05. Assuming a drop-out rate of 10% per wave, we targeted an initial sample size of 500 individuals for the first wave of survey.

We prioritised data collection during the first heatwave, as previous studies suggested that the first heatwave has a greater health impact (e.g. higher risks of heat-related hospitalizations and mortality) than subsequent heatwaves \[31, 32\]. Data collection from a subsequent heatwave was also planned to account for the possibility of lagged or cumulated health effects of heatwaves. Prior evidence suggests that some heatwave-related health consequences, such as exacerbation of cardiovascular and respiratory conditions, may occur one week after a heatwave \[3, 33, 34\].

### Participants and recruitment

We recruited a study cohort from two urban residential communities. With help from community officials, we screened selected residents for their eligibility in the recreation centres of their communities. Potentially eligible residents were informed and invited to the recreation centres by their community officials via social media (WeChat), telephone, or word of mouth. Residents who passed by the recreation centres during the recruitment period were also invited for screening if they were interested. The inclusion criteria were: (1) aged 60 years or above; (2) resident of the selected communities; (3) able to communicate in Mandarin or Foochow dialect; (4) cognitively and physically capable of being interviewed by an interviewer; and (5) able to provide informed consent. Residents (1) younger than 60 years old; (2) cognitively impaired; (3) unwilling to provide contact information or give informed consent for follow-up surveys; or (4) exhibiting low cooperation or credibility based on interviewers’ assessment were excluded.

### Data collection

The four waves of data collection were conducted between 10<sup>th</sup> and 25<sup>th</sup> May (mean daily maximum temperature ± SD: 31.70 ± 1.40°C), between 26<sup>th</sup> June and 7<sup>th</sup> July (mean daily maximum temperature ± SD: 35.78 ± 0.38°C), between 3<sup>rd</sup> and 22<sup>nd</sup> August (mean daily maximum temperature ± SD: 36.61 ± 1.57°C), and between 15<sup>th</sup> and 28<sup>th</sup> October (mean daily maximum temperature ± SD: 28.93 ± 1.31°C). The data collection of heatwave 1 and heatwave 2 were conducted during the first and third of five heatwaves in Fuzhou in 2023 which lasted for 22 days and 9 days, respectively.

All four waves of survey were conducted face-to-face in the recreation centres of the selected communities, with the pre-heatwave surveys taking place immediately after recruitment. In addition to following up with participants from earlier waves, a few new participants were recruited during the heatwave 1 and heatwave 2 survey to achieve the desired sample size. At all timepoints, the simplified Chinese versions of EQ-5D-5L, EQ-HWB, and Brief Inventory of Thriving (BIT) questionnaires, as well as questions assessing daily activities and self-perceived effects of high temperature, were administered in a fixed order through one-on-one, face-to-face interviews. Responses were entered directly into an online electronic questionnaire (WeChat Survey Star) using iPads. All interviews were conducted in Chinese by a team of 21 trained graduate and undergraduate students from Fujian Medical University. As temperatures usually reached their highest level between 12 pm and 3 pm in Fuzhou, interviews were conducted in the afternoon.

This study was approved by the Institutional Review Board of Fujian Medical University (reference number: 2023–146).

### Measures

#### EQ-5D-5L

The EQ-5D-5L is a generic preference-based measure that includes a descriptive system and a EQ VAS \[35\]. Its descriptive system consists of five items: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression, each with five response levels (no problems, slight problems, moderate problems, severe problems, extreme problems/unable to). The EQ VAS assesses an individual’s self-rated health on a vertical scale ranging from 0 (the worst health you can imagine) to 100 (the best health you can imagine). Both the descriptive system and EQ VAS use a ‘today’ recall period (i.e. respondents rate their health on the day of completion). In this study, EQ-5D-5L index values were computed using the Chinese value set \[36\], which reflects the preferences of the target population. The UK crosswalk \[37\] and England \[38\] EQ-5D-5L value sets were used for sensitivity analyses to facilitate comparison with the UK-weighted EQ-HWB-9 results (see details below). It should be noted that the England EQ-5D-5L value set is not recommended by National Institute for Health and Care Excellence (NICE) and the UK crosswalk value set was intended as a temporary solution for mapping the EQ-5D-5L to EQ-5D-3L value sets \[39\]. A new UK EQ-5D-5L value set expected to be released in the near future \[40\]. We also calculated the level sum scores (LSSs) for the EQ-5D-5L, where higher LSSs indicate worse health status.

#### EQ-HWB and EQ-HWB-9

The EQ-HWB is a generic measure assessing health and wellbeing across seven domains: activity, autonomy, cognition, feelings and emotions, relationships, physical sensations, and self-identity \[26\]. In this study, the experimental Simplified Chinese EQ-HWB (v1.1) was used, which includes 25 items \[26, 41\]. A subset of these 25 items was selected to develop a shorter 9-item instrument, the EQ-HWB-9, primarily for valuation purposes \[26\]. Each item of the EQ-HWB/EQ-HWB-9 has five levels of difficulty (no difficulty, slight, some, a lot of, unable), frequency (none of the time, only occasionally, sometimes, often, most or all the time), or severity (no, mild, moderate, severe, very severe). The recall period is ‘in the last 7 days’. In this study, only the EQ-HWB was directly completed by respondents, while the EQ-HWB-9 responses were derived from the EQ-HWB. The EQ-HWB-9 index values were calculated using the UK pilot value set, which is currently the only available value set for the EQ-HWB-9 \[42\]. There is no established method for non-preference-based scoring of the EQ-HWB and EQ-HWB-9. Following previous studies \[43–46\], we calculated EQ-HWB and EQ-HWB-9 scores using the LSS approach. Three EQ-HWB subscale scores were also calculated: (1) activities LSS (3 items: day-to-day activities, getting around inside and outside, and personal care), (2) pain/discomfort LSS (4 items: pain \[frequency and severity\] and discomfort \[frequency and severity\]), and (3) psychosocial wellbeing LSS (16 items: sleep, exhausted, lonely, unsupported by people, remembering, concentrating/thinking clearly, anxious, unsafe, frustrated, sad/depressed, nothing to look forward to, control over my day-to-day life, cope with my day-to-day life, accepted by others, feel good about myself, and do the things I wanted to do); and the EQ-HWB-9 with two subscales: (1) psychosocial LSS (6 items: exhausted, lonely, concentrating/thinking clearly, anxious, sad/depressed, and control over my day-to-day life), and physical LSS (3 items: getting around inside and outside, day-to-day activities, and pain \[severity\]) \[43, 44\]. Higher scores on the EQ-HWB/EQ-HWB-9 LSS and their subscale LSS indicate worse health and wellbeing.

#### BIT

The BIT is a 10-item measure of psychological wellbeing \[47\]. Each item is rated on a response scale from 1 (strongly disagree) to 5 (strongly agree). The BIT score is calculated as a single LSS, with higher scores indicating a stronger sense of psychological wellbeing. The BIT does not specify a recall period.

### Additional information

The additional information collected in the questionnaire included demographics (age, sex, education, marital status, annual income, residence, and employment), health-related variables (weight, height, smoking, drinking, and chronic diseases), and heatwave-related questions (cooling measures, daily activities, discomfort symptoms, and self-perceived adaptation to weather). These questions were pilot tested for respondent burden, clarity, and comprehensibility using a convenience sample of 20 respondents. Minor revisions were made based on respondent feedback prior to finalizing the questionnaire. Demographic and health-related questions were administered prior to the health and wellbeing questionnaires, while heatwave-related questions were presented afterward.

The temperature on the day of each interview in this study was sourced from the Reliable Prognosis weather portal (site number of Fuzhou: 558847) \[48\]. The retrieved data comprised daily maximum temperature, daily minimum temperature, daily average temperature, and daily average relative humidity. All temperature readings were reported in degrees Celsius (°C), while relative humidity is expressed as a percentage (%).

### Statistical analysis

Descriptive statistics were used to describe respondent characteristics and scores of EQ-5D-5L, EQ-HWB, EQ-HWB-9 and BIT across all four waves. Continuous variables were summarized as means with standard deviations (SD), while categorical variables were presented as frequencies and percentages. To assess differences between consecutive waves (i.e., pre-heatwave versus heatwave 1, heatwave 1 versus heatwave 2, and heatwave 2 versus post-heatwave), statistical tests, including the chi-squared test, Fisher’s exact test, two-sample t-test, and paired t-test, were applied where appropriate. A *p*-value of less than 0.05 was considered statistically significant.

We assessed psychometric properties of the EQ-5D-5L, EQ-HWB and EQ-HWB-9, including response distributions, ceiling/floor, known-groups validity, and responsiveness. All analyses were performed using Stata 17.0 (StataCorp LLC, College Station, TX).

#### Response distributions and ceiling and floor effects

Response distributions across all four waves of data were examined using absolute and relative frequencies for each item level. The floor and ceiling effects were evaluated by examining the percentage of respondents who achieved the minimum/maximum possible scores or values for each item or each measure \[49\]. The floor/ceiling effects were identified if over 70% of respondents score at either extremes at the item level, or over 15% do so at the instrument level \[45, 46\].

#### Known-groups validity

We examined the known-groups validity of EQ-5D-5L, EQ-HWB and EQ-HWB-9 scores (including index values and LSSs) and compared their sensitivity to the health and wellbeing impact of heatwaves using Cohen’s d (mean difference divided by pooled standard deviations \[SD\] of two known groups). Known-groups were defined in terms of (1) presence or absence of excessive sweating and (2) self-perceived adaptation to weather (yes/no) using data from the heatwave 1 and heatwave 2 survey. The effect size was interpreted as: none (d \< 0.2), small (0.2 ≤ d \< 0.5), medium (0.5 ≤ d \< 0.8), large (0.8 ≤ d \< 1.4), or very large (d ≥ 1.4) \[50\]. The 95% confidence intervals (CIs) for Cohen’s d were calculated using the *esize* command in Stata.

#### Responsiveness

We examined the responsiveness of the EQ-5D-5L, EQ-HWB and EQ-HWB-9 by analysing the scores of residents whose life was affected by heatwaves. We compared the scores between the pre-heatwave and heatwave 1, and scores between the heatwave 2 and post-heatwave. The degree of responsiveness was assessed using the standardized response mean (SRM) (mean change divided by SD of the changed scores) which was interpreted as: none (SRM \< 0.2), low (0.2 ≤ SRM \<0.5), moderate (0.5 ≤ SRM \<0.8), and high (SRM ≥ 0.80) \[50\]. The 95% CIs for the SRM were calculated using bootstrapping with 1000 replications and resampling with replacement in Stata.

Subgroup analyses on response distributions, ceiling/floor, known-groups validity and responsiveness were performed among respondents with chronic conditions.

## Results

Supplementary Figure <a href="#MOESM1" data-ref-type="supplementary-material">1</a> shows the flowchart detailing the recruitment and follow-up across the four waves of the survey. A total of 638, 559, 512 and 557 residents completed the survey of pre-heatwave, heatwave 1, heatwave 2 and post-heatwave, respectively. After excluding respondents who were younger than 60 years old or exhibited low cooperation and/or credibility, a total of 579, 510, 473 and 508 residents were included for analysis, respectively. The mean interview duration was 24.1 minutes (range: 11.1 to 76.6 minutes).

Table <a href="#Tab1" data-ref-type="table">1</a> shows the respondents’ characteristics. In the pre-heatwave survey, most of respondents were aged 60–74 years old (67.5%), female (64.6%), married (80.5%), and without employment (96.7%), and had a secondary education level or below (57.5%). While the cohort’s sociodemographic characteristics remained the same over time, there are salient differences in health and heat-related characteristics across the time points. Specifically, a higher proportion of respondents took cooling measures and felt unadapted to the weather during the heatwave 1 and heatwave 2 survey compared to the pre-heatwave and post-heatwave surveys. A significantly higher proportion of respondents experienced heat-related symptoms and took measures due to feeling unwell during the heatwave 2 survey compared to pre-heatwave, heatwave 1 and post-heatwave survey (see details in Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Respondent characteristics

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"> Characteristic</th>
<th style="text-align: left;"> Level</th>
<th colspan="2" style="text-align: left;">Pre-heatwave (n = 579)</th>
<th colspan="2" style="text-align: left;">Heatwave 1 (n = 510)</th>
<th colspan="2" style="text-align: left;">Heatwave 2 (n = 473)</th>
<th colspan="3" style="text-align: left;">Post-heatwave (n = 508)</th>
<th style="text-align: left;">Pre-heatwave vs Heatwave 1</th>
<th style="text-align: left;">Heatwave 1 vs Heatwave 2</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">%</th>
<th colspan="2" style="text-align: left;"><strong>p-value</strong> <sup><strong>c</strong></sup></th>
<th style="text-align: left;"><strong>p-value</strong> <sup><strong>c</strong></sup></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Age (year)</td>
<td style="text-align: left;">60–74</td>
<td style="text-align: left;">391</td>
<td style="text-align: left;">67.5</td>
<td style="text-align: left;">348</td>
<td style="text-align: left;">68.2</td>
<td style="text-align: left;">317</td>
<td style="text-align: left;">67.0</td>
<td style="text-align: left;">348</td>
<td style="text-align: left;">68.5</td>
<td colspan="2" style="text-align: left;">0.804</td>
<td style="text-align: left;">0.684</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">≥75</td>
<td style="text-align: left;">188</td>
<td style="text-align: left;">32.5</td>
<td style="text-align: left;">162</td>
<td style="text-align: left;">31.8</td>
<td style="text-align: left;">156</td>
<td style="text-align: left;">33.0</td>
<td style="text-align: left;">160</td>
<td style="text-align: left;">31.5</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Sex<sup>a</sup></td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">205</td>
<td style="text-align: left;">35.4</td>
<td style="text-align: left;">164</td>
<td style="text-align: left;">36.2</td>
<td style="text-align: left;">157</td>
<td style="text-align: left;">36.8</td>
<td style="text-align: left;">169</td>
<td style="text-align: left;">37.0</td>
<td colspan="2" style="text-align: left;">0.791</td>
<td style="text-align: left;">0.862</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">374</td>
<td style="text-align: left;">64.6</td>
<td style="text-align: left;">289</td>
<td style="text-align: left;">63.8</td>
<td style="text-align: left;">270</td>
<td style="text-align: left;">63.2</td>
<td style="text-align: left;">288</td>
<td style="text-align: left;">63.0</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Education<sup>a</sup></td>
<td style="text-align: left;">Secondary and below</td>
<td style="text-align: left;">333</td>
<td style="text-align: left;">57.5</td>
<td style="text-align: left;">255</td>
<td style="text-align: left;">56.3</td>
<td style="text-align: left;">244</td>
<td style="text-align: left;">57.1</td>
<td style="text-align: left;">257</td>
<td style="text-align: left;">56.2</td>
<td colspan="2" style="text-align: left;">0.694</td>
<td style="text-align: left;">0.799</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High school and above</td>
<td style="text-align: left;">246</td>
<td style="text-align: left;">42.5</td>
<td style="text-align: left;">198</td>
<td style="text-align: left;">43.7</td>
<td style="text-align: left;">183</td>
<td style="text-align: left;">42.9</td>
<td style="text-align: left;">200</td>
<td style="text-align: left;">43.8</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Marital status<sup>a</sup></td>
<td style="text-align: left;">Married</td>
<td style="text-align: left;">466</td>
<td style="text-align: left;">80.5</td>
<td style="text-align: left;">377</td>
<td style="text-align: left;">83.2</td>
<td style="text-align: left;">347</td>
<td style="text-align: left;">81.3</td>
<td style="text-align: left;">377</td>
<td style="text-align: left;">82.5</td>
<td colspan="2" style="text-align: left;">0.259</td>
<td style="text-align: left;">0.447</td>
</tr>
<tr>
<td style="text-align: left;">Others</td>
<td style="text-align: left;">113</td>
<td style="text-align: left;">19.5</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">18.7</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">17.5</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Annual income (RMB) <sup>a</sup></td>
<td style="text-align: left;">&lt;30,000</td>
<td style="text-align: left;">165</td>
<td style="text-align: left;">28.5</td>
<td style="text-align: left;">127</td>
<td style="text-align: left;">28.0</td>
<td style="text-align: left;">120</td>
<td style="text-align: left;">28.1</td>
<td style="text-align: left;">127</td>
<td style="text-align: left;">27.8</td>
<td colspan="2" style="text-align: left;">0.947</td>
<td style="text-align: left;">0.952</td>
</tr>
<tr>
<td style="text-align: left;">30,000– 60,000</td>
<td style="text-align: left;">265</td>
<td style="text-align: left;">45.8</td>
<td style="text-align: left;">212</td>
<td style="text-align: left;">46.8</td>
<td style="text-align: left;">196</td>
<td style="text-align: left;">45.9</td>
<td style="text-align: left;">209</td>
<td style="text-align: left;">45.7</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">&gt;60,000</td>
<td style="text-align: left;">149</td>
<td style="text-align: left;">25.7</td>
<td style="text-align: left;">114</td>
<td style="text-align: left;">25.2</td>
<td style="text-align: left;">111</td>
<td style="text-align: left;">26.0</td>
<td style="text-align: left;">121</td>
<td style="text-align: left;">26.5</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Residence <sup>a</sup></td>
<td style="text-align: left;">Living only with children</td>
<td style="text-align: left;">152</td>
<td style="text-align: left;">26.3</td>
<td style="text-align: left;">108</td>
<td style="text-align: left;">23.8</td>
<td style="text-align: left;">98</td>
<td style="text-align: left;">23.0</td>
<td style="text-align: left;">115</td>
<td style="text-align: left;">25.2</td>
<td colspan="2" style="text-align: left;">0.883</td>
<td style="text-align: left;">0.948</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Living only with spouse</td>
<td style="text-align: left;">190</td>
<td style="text-align: left;">32.8</td>
<td style="text-align: left;">157</td>
<td style="text-align: left;">34.7</td>
<td style="text-align: left;">153</td>
<td style="text-align: left;">35.8</td>
<td style="text-align: left;">157</td>
<td style="text-align: left;">34.4</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Living alone</td>
<td style="text-align: left;">53</td>
<td style="text-align: left;">9.2</td>
<td style="text-align: left;">42</td>
<td style="text-align: left;">9.3</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">10.5</td>
<td style="text-align: left;">37</td>
<td style="text-align: left;">8.1</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Living with spouse and children</td>
<td style="text-align: left;">167</td>
<td style="text-align: left;">28.8</td>
<td style="text-align: left;">135</td>
<td style="text-align: left;">29.8</td>
<td style="text-align: left;">122</td>
<td style="text-align: left;">28.6</td>
<td style="text-align: left;">136</td>
<td style="text-align: left;">29.8</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Others</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">2.9</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">2.1</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">2.6</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Employment<sup>a</sup></td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">560</td>
<td style="text-align: left;">96.7</td>
<td style="text-align: left;">436</td>
<td style="text-align: left;">96.3</td>
<td style="text-align: left;">410</td>
<td style="text-align: left;">96.0</td>
<td style="text-align: left;">442</td>
<td style="text-align: left;">96.7</td>
<td colspan="2" style="text-align: left;">0.682</td>
<td style="text-align: left;">0.860</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">3.8</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">4.0</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">3.3</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BMI<sup>a</sup></td>
<td style="text-align: left;">Underweight (BMI &lt; 18.5 kg/m<sup>2</sup>)</td>
<td style="text-align: left;">27</td>
<td style="text-align: left;">4.7</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">3.8</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">4.2</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">3.9</td>
<td colspan="2" style="text-align: left;">0.914</td>
<td style="text-align: left;">0.960</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Normal (18.5 ≤ BMI &lt; 25 kg/m<sup>2</sup>)</td>
<td style="text-align: left;">371</td>
<td style="text-align: left;">64.1</td>
<td style="text-align: left;">292</td>
<td style="text-align: left;">64.5</td>
<td style="text-align: left;">276</td>
<td style="text-align: left;">64.6</td>
<td style="text-align: left;">290</td>
<td style="text-align: left;">63.5</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Overweight (25 ≤ BMI &lt; 30 kg/m<sup>2</sup>)</td>
<td style="text-align: left;">152</td>
<td style="text-align: left;">26.3</td>
<td style="text-align: left;">121</td>
<td style="text-align: left;">26.7</td>
<td style="text-align: left;">114</td>
<td style="text-align: left;">26.7</td>
<td style="text-align: left;">129</td>
<td style="text-align: left;">28.2</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Obese (BMI ≥ 30 kg/m<sup>2</sup>)</td>
<td style="text-align: left;">29</td>
<td style="text-align: left;">5.0</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">5.1</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">4.5</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">4.4</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Smoking<sup>a</sup></td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">480</td>
<td style="text-align: left;">82.9</td>
<td style="text-align: left;">381</td>
<td style="text-align: left;">84.1</td>
<td style="text-align: left;">360</td>
<td style="text-align: left;">84.3</td>
<td style="text-align: left;">379</td>
<td style="text-align: left;">82.9</td>
<td colspan="2" style="text-align: left;">0.606</td>
<td style="text-align: left;">0.934</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">99</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">72</td>
<td style="text-align: left;">15.9</td>
<td style="text-align: left;">67</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">17.1</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Drinking<sup>a</sup></td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">443</td>
<td style="text-align: left;">76.5</td>
<td style="text-align: left;">352</td>
<td style="text-align: left;">77.7</td>
<td style="text-align: left;">331</td>
<td style="text-align: left;">77.5</td>
<td style="text-align: left;">349</td>
<td style="text-align: left;">76.4</td>
<td colspan="2" style="text-align: left;">0.651</td>
<td style="text-align: left;">0.947</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">136</td>
<td style="text-align: left;">23.5</td>
<td style="text-align: left;">101</td>
<td style="text-align: left;">22.3</td>
<td style="text-align: left;">96</td>
<td style="text-align: left;">22.5</td>
<td style="text-align: left;">108</td>
<td style="text-align: left;">23.6</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Chronic diseases</td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">151</td>
<td style="text-align: left;">26.1</td>
<td style="text-align: left;">160</td>
<td style="text-align: left;">31.4</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">15.9</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">15.0</td>
<td colspan="2" style="text-align: left;">0.054</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">428</td>
<td style="text-align: left;">73.9</td>
<td style="text-align: left;">350</td>
<td style="text-align: left;">68.6</td>
<td style="text-align: left;">398</td>
<td style="text-align: left;">84.1</td>
<td style="text-align: left;">432</td>
<td style="text-align: left;">85.0</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Taking cooling measures</td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">318</td>
<td style="text-align: left;">54.9</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">402</td>
<td style="text-align: left;">79.1</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.003</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">261</td>
<td style="text-align: left;">45.1</td>
<td style="text-align: left;">498</td>
<td style="text-align: left;">97.7</td>
<td style="text-align: left;">472</td>
<td style="text-align: left;">99.8</td>
<td style="text-align: left;">106</td>
<td style="text-align: left;">20.9</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Cooling measures</td>
<td style="text-align: left;">Electric fan</td>
<td style="text-align: left;">215</td>
<td style="text-align: left;">37.1</td>
<td style="text-align: left;">464</td>
<td style="text-align: left;">91.0</td>
<td style="text-align: left;">422</td>
<td style="text-align: left;">89.2</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">18.1</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.355</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Air conditioner</td>
<td style="text-align: left;">66</td>
<td style="text-align: left;">11.4</td>
<td style="text-align: left;">442</td>
<td style="text-align: left;">86.7</td>
<td style="text-align: left;">437</td>
<td style="text-align: left;">92.4</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">4.7</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cattail leaf fan</td>
<td style="text-align: left;">51</td>
<td style="text-align: left;">8.8</td>
<td style="text-align: left;">200</td>
<td style="text-align: left;">39.2</td>
<td style="text-align: left;">182</td>
<td style="text-align: left;">38.5</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.0</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.813</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Stay in public places with air conditioner</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">4.3</td>
<td style="text-align: left;">42</td>
<td style="text-align: left;">8.9</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.4</td>
<td colspan="2" style="text-align: left;">0.081</td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Others</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">4.9</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">4.9</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.2</td>
<td colspan="2" style="text-align: left;">0.175</td>
<td style="text-align: left;">0.977</td>
</tr>
<tr>
<td style="text-align: left;">How often use air conditioner</td>
<td style="text-align: left;">Not applicable</td>
<td style="text-align: left;">513</td>
<td style="text-align: left;">88.6</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">13.3</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">7.6</td>
<td style="text-align: left;">484</td>
<td style="text-align: left;">95.3</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Always</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">61</td>
<td style="text-align: left;">12.0</td>
<td style="text-align: left;">95</td>
<td style="text-align: left;">20.1</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.6</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Often</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">3.8</td>
<td style="text-align: left;">259</td>
<td style="text-align: left;">50.8</td>
<td style="text-align: left;">261</td>
<td style="text-align: left;">55.2</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.0</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Rarely</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">6.6</td>
<td style="text-align: left;">115</td>
<td style="text-align: left;">22.6</td>
<td style="text-align: left;">81</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">3.0</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Never</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">1.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.2</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Air conditioner temperature setting</td>
<td style="text-align: left;">Not applicable</td>
<td style="text-align: left;">513</td>
<td style="text-align: left;">88.6</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">13.3</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">7.6</td>
<td style="text-align: left;">484</td>
<td style="text-align: left;">95.3</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.017</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">16–20 °C</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">21–25 °C</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">2.6</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">18.0</td>
<td style="text-align: left;">71</td>
<td style="text-align: left;">15.0</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.6</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">26–30 °C</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">8.6</td>
<td style="text-align: left;">341</td>
<td style="text-align: left;">66.9</td>
<td style="text-align: left;">357</td>
<td style="text-align: left;">75.5</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">3.7</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">&gt; 30 °C</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.0</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.1</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.4</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Outdoor activities</td>
<td style="text-align: left;">Increased</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">4.0</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">4.9</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">2.3</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">11.8</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Decreased</td>
<td style="text-align: left;">35</td>
<td style="text-align: left;">6.0</td>
<td style="text-align: left;">125</td>
<td style="text-align: left;">24.5</td>
<td style="text-align: left;">185</td>
<td style="text-align: left;">39.1</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">4.3</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">No change</td>
<td style="text-align: left;">487</td>
<td style="text-align: left;">84.1</td>
<td style="text-align: left;">313</td>
<td style="text-align: left;">61.4</td>
<td style="text-align: left;">252</td>
<td style="text-align: left;">53.3</td>
<td style="text-align: left;">397</td>
<td style="text-align: left;">78.2</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">No outdoor activity</td>
<td style="text-align: left;">34</td>
<td style="text-align: left;">5.9</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">9.2</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">5.3</td>
<td style="text-align: left;">29</td>
<td style="text-align: left;">5.7</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Outdoor duration (hours)</td>
<td style="text-align: left;">duration &lt; 1</td>
<td style="text-align: left;">114</td>
<td style="text-align: left;">19.7</td>
<td style="text-align: left;">95</td>
<td style="text-align: left;">18.6</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">18.0</td>
<td style="text-align: left;">73</td>
<td style="text-align: left;">14.4</td>
<td colspan="2" style="text-align: left;">0.841</td>
<td style="text-align: left;">0.836</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">1 ≤ duration &lt; 2</td>
<td style="text-align: left;">204</td>
<td style="text-align: left;">35.2</td>
<td style="text-align: left;">193</td>
<td style="text-align: left;">37.8</td>
<td style="text-align: left;">186</td>
<td style="text-align: left;">39.3</td>
<td style="text-align: left;">185</td>
<td style="text-align: left;">36.4</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">2 ≤ duration &lt; 3</td>
<td style="text-align: left;">164</td>
<td style="text-align: left;">28.3</td>
<td style="text-align: left;">138</td>
<td style="text-align: left;">27.1</td>
<td style="text-align: left;">118</td>
<td style="text-align: left;">25.0</td>
<td style="text-align: left;">134</td>
<td style="text-align: left;">26.4</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">duration ≥ 3</td>
<td style="text-align: left;">97</td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">84</td>
<td style="text-align: left;">16.5</td>
<td style="text-align: left;">84</td>
<td style="text-align: left;">17.8</td>
<td style="text-align: left;">116</td>
<td style="text-align: left;">22.8</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Experienced discomfort symptoms in the past few days</td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">285</td>
<td style="text-align: left;">49.2</td>
<td style="text-align: left;">273</td>
<td style="text-align: left;">53.5</td>
<td style="text-align: left;">112</td>
<td style="text-align: left;">23.7</td>
<td style="text-align: left;">303</td>
<td style="text-align: left;">59.7</td>
<td colspan="2" style="text-align: left;">0.156</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">294</td>
<td style="text-align: left;">50.8</td>
<td style="text-align: left;">237</td>
<td style="text-align: left;">46.5</td>
<td style="text-align: left;">361</td>
<td style="text-align: left;">76.3</td>
<td style="text-align: left;">205</td>
<td style="text-align: left;">40.4</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Experienced discomfort symptoms in the past few days</td>
<td style="text-align: left;">Headache</td>
<td style="text-align: left;">57</td>
<td style="text-align: left;">9.8</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">8.0</td>
<td style="text-align: left;">35</td>
<td style="text-align: left;">6.9</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Dizziness</td>
<td style="text-align: left;">99</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: left;">63</td>
<td style="text-align: left;">13.3</td>
<td style="text-align: left;">54</td>
<td style="text-align: left;">10.6</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Nausea</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">1.9</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">1.2</td>
<td colspan="2" style="text-align: left;">0.070</td>
<td style="text-align: left;">0.032</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Vomiting</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">1.7</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">0.4</td>
<td colspan="2" style="text-align: left;">1.000</td>
<td style="text-align: left;">0.132</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Thirsty</td>
<td style="text-align: left;">97</td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">14.9</td>
<td style="text-align: left;">172</td>
<td style="text-align: left;">36.4</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">13.4</td>
<td colspan="2" style="text-align: left;">0.404</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Dark yellow urine</td>
<td style="text-align: left;">54</td>
<td style="text-align: left;">9.3</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">7.8</td>
<td style="text-align: left;">73</td>
<td style="text-align: left;">15.4</td>
<td style="text-align: left;">35</td>
<td style="text-align: left;">6.9</td>
<td colspan="2" style="text-align: left;">0.384</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Excessive sweating</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">9.0</td>
<td style="text-align: left;">112</td>
<td style="text-align: left;">22.0</td>
<td style="text-align: left;">228</td>
<td style="text-align: left;">48.2</td>
<td style="text-align: left;">28</td>
<td style="text-align: left;">5.5</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Rash</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">2.5</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="2" style="text-align: left;">1.000</td>
<td style="text-align: left;">0.017</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Fatigue</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">9.0</td>
<td style="text-align: left;">42</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;">88</td>
<td style="text-align: left;">18.6</td>
<td style="text-align: left;">32</td>
<td style="text-align: left;">6.3</td>
<td colspan="2" style="text-align: left;">0.662</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Tinnitus</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">8.1</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">2.6</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">10.2</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">7.5</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Poor appetite</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">8.1</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">4.7</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">11.0</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">4.5</td>
<td colspan="2" style="text-align: left;">0.023</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Polypnea</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">1.4</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">4.2</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.0</td>
<td colspan="2" style="text-align: left;">0.365</td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Palpitations</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">2.8</td>
<td style="text-align: left;">26</td>
<td style="text-align: left;">5.5</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">2.0</td>
<td colspan="2" style="text-align: left;">0.723</td>
<td style="text-align: left;">0.029</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cramp</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">6.7</td>
<td style="text-align: left;">44</td>
<td style="text-align: left;">8.6</td>
<td style="text-align: left;">87</td>
<td style="text-align: left;">18.4</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">15.0</td>
<td colspan="2" style="text-align: left;">0.240</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Weakness</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">33</td>
<td style="text-align: left;">7.0</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">3.2</td>
<td colspan="2" style="text-align: left;">0.070</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Irritable</td>
<td style="text-align: left;">34</td>
<td style="text-align: left;">5.9</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">10.2</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">2.2</td>
<td colspan="2" style="text-align: left;">0.426</td>
<td style="text-align: left;">0.083</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Confusion</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">4.2</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">6.3</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">3.0</td>
<td colspan="2" style="text-align: left;">0.012</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Taking measures due to feeling unwell</td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">448</td>
<td style="text-align: left;">77.4</td>
<td style="text-align: left;">337</td>
<td style="text-align: left;">66.1</td>
<td style="text-align: left;">159</td>
<td style="text-align: left;">33.6</td>
<td style="text-align: left;">360</td>
<td style="text-align: left;">70.9</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">131</td>
<td style="text-align: left;">22.6</td>
<td style="text-align: left;">173</td>
<td style="text-align: left;">33.9</td>
<td style="text-align: left;">314</td>
<td style="text-align: left;">66.4</td>
<td style="text-align: left;">148</td>
<td style="text-align: left;">29.1</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Taking measures due to feeling unwell</td>
<td style="text-align: left;">Reducing or stopping some daily activities</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">3.8</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">7.5</td>
<td style="text-align: left;">114</td>
<td style="text-align: left;">24.1</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">2.6</td>
<td colspan="2" style="text-align: left;">0.008</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Changing the usual routine</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">2.1</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">2.2</td>
<td style="text-align: left;">32</td>
<td style="text-align: left;">6.8</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">0.8</td>
<td colspan="2" style="text-align: left;">0.923</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Reducing or changing diet</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">1.0</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;">46</td>
<td style="text-align: left;">9.7</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">2.8</td>
<td colspan="2" style="text-align: left;">0.014</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Self-medication</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;">41</td>
<td style="text-align: left;">8.0</td>
<td style="text-align: left;">107</td>
<td style="text-align: left;">22.6</td>
<td style="text-align: left;">79</td>
<td style="text-align: left;">15.6</td>
<td colspan="2" style="text-align: left;">0.705</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Self-increasing medication dosage</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="2" style="text-align: left;">1.000</td>
<td style="text-align: left;">0.111</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Planning to see a doctor</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">2.1</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">1.4</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">4.2</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">1.4</td>
<td colspan="2" style="text-align: left;">0.379</td>
<td style="text-align: left;">0.006</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Going to a hospital or clinic for treatment</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">2.8</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">2.6</td>
<td colspan="2" style="text-align: left;">0.734</td>
<td style="text-align: left;">0.693</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Increasing water intake</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">9.0</td>
<td style="text-align: left;">133</td>
<td style="text-align: left;">26.1</td>
<td style="text-align: left;">235</td>
<td style="text-align: left;">49.7</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">15.8</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Others</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.6</td>
<td style="text-align: left;">24.0</td>
<td style="text-align: left;">5.1</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">2.0</td>
<td colspan="2" style="text-align: left;">0.153</td>
<td style="text-align: left;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">Self-perceived adaptation to weather<sup>b</sup></td>
<td style="text-align: left;">Not adapted to weather</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">8.1</td>
<td style="text-align: left;">182</td>
<td style="text-align: left;">35.7</td>
<td style="text-align: left;">169</td>
<td style="text-align: left;">35.7</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">2.0</td>
<td colspan="2" style="text-align: left;">&lt;0.001</td>
<td style="text-align: left;">0.989</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Adapted to weather</td>
<td style="text-align: left;">532</td>
<td style="text-align: left;">91.9</td>
<td style="text-align: left;">328</td>
<td style="text-align: left;">64.3</td>
<td style="text-align: left;">304</td>
<td style="text-align: left;">64.3</td>
<td style="text-align: left;">498</td>
<td style="text-align: left;">98.0</td>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

BMI, Body Mass Index

<sup>a</sup> Data were missing for 57, 46, and 51 respondents in the second, third and fourth waves, respectively

<sup>b</sup> Measured using a question assessing self-perceived adaptation to weather: *Are you adapted to the current weather? The response options include: 1) very well adapted to; 2) adapted to; 3) not adapted to; 4) very poorly adapted to*

<sup>c</sup> Using the chi-squared test or Fisher’s exact test

</div>

Table <a href="#Tab2" data-ref-type="table">2</a> shows the scores of EQ VAS, EQ-5D-5L, EQ-HWB-9, EQ-HWB, and BIT. The mean±SD EQ VAS, EQ-5D-5L and EQ-HWB-9 index values of the heatwave 1 (80.05 ± 11.65; 0.95 ± 0.11; 0.94 ± 0.10) were higher than those of the pre-heatwave (77.17 ± 14.18; 0.93 ± 0.11; 0.92 ± 0.12), heatwave 2 (78.84 ± 11.52; 0.92 ± 0.12; 0.91 ± 0.13) and post-heatwave (78.59 ± 11.58; 0.93 ± 0.11; 0.92 ± 0.12). The mean ± SD EQ-HWB LSSs of the heatwave 1 (34.07 ± 8.91) were lower than those of the pre-heatwave (37.78 ± 10.54), heatwave 2 (37.53 ± 11.30) and post-heatwave (36.39 ± 10.76). All these scores suggested that the health and wellbeing of the cohort was the best during the heatwave 1 survey.

<div id="Tab2" class="table-wrap">

<div class="caption">

Scores of EQ VAS, EQ-5D-5L, EQ-HWB, EQ-HWB-9 and BIT

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Pre-heatwave (n = 579)</th>
<th colspan="2" style="text-align: left;">Heatwave 1 (n = 510)</th>
<th colspan="2" style="text-align: left;">Heatwave 2 (n = 473)</th>
<th colspan="3" style="text-align: left;">Post-heatwave (n = 508)</th>
<th style="text-align: left;">Pre-heatwave vs Heatwave 1</th>
<th style="text-align: left;">Heatwave 1 vs Heatwave 2</th>
<th style="text-align: left;">Heatwave 2 vs Post-heatwave</th>
<th style="text-align: left;">Pre-heatwave vs Heatwave 1 (n = 453)</th>
<th style="text-align: left;">Heatwave 1 vs Heatwave 2 (n = 420)</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th colspan="2" style="text-align: left;"><strong>Mean difference</strong> <sup><strong>a</strong></sup></th>
<th style="text-align: left;"><strong>Mean difference</strong> <sup><strong>a</strong></sup></th>
<th style="text-align: left;"><strong>Mean difference</strong> <sup><strong>a</strong></sup></th>
<th style="text-align: left;"><strong>Mean difference</strong> <sup><strong>b</strong></sup></th>
<th style="text-align: left;"><strong>Mean difference</strong> <sup><strong>b</strong></sup></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;">77.17</td>
<td style="text-align: left;">14.18</td>
<td style="text-align: left;">80.05</td>
<td style="text-align: left;">11.65</td>
<td style="text-align: left;">78.84</td>
<td style="text-align: left;">11.52</td>
<td style="text-align: left;">78.59</td>
<td style="text-align: left;">11.58</td>
<td colspan="2" style="text-align: left;"><strong>−2.88***</strong></td>
<td style="text-align: left;">1.21</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;"><strong>−2.28***</strong></td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L Index (China)</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">0.11</td>
<td colspan="2" style="text-align: left;"><strong>−0.02*</strong></td>
<td style="text-align: left;"><strong>0.03***</strong></td>
<td style="text-align: left;">−0.01</td>
<td style="text-align: left;"><strong>−0.01*</strong></td>
<td style="text-align: left;"><strong>0.03***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L Index (UK, crosswalk)</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">0.90</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.14</td>
<td colspan="2" style="text-align: left;"><strong>−0.03**</strong></td>
<td style="text-align: left;"><strong>0.04***</strong></td>
<td style="text-align: left;"><strong>−0.02*</strong></td>
<td style="text-align: left;"><strong>−0.02**</strong></td>
<td style="text-align: left;"><strong>0.04***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L Index (England)</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.10</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.10</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.10</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">0.10</td>
<td colspan="2" style="text-align: left;"><strong>−0.02**</strong></td>
<td style="text-align: left;"><strong>0.03***</strong></td>
<td style="text-align: left;">−0.01</td>
<td style="text-align: left;"><strong>−0.02**</strong></td>
<td style="text-align: left;"><strong>0.02***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-9 Index (UK)</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.10</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.13</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.12</td>
<td colspan="2" style="text-align: left;"><strong>−0.03***</strong></td>
<td style="text-align: left;"><strong>0.03***</strong></td>
<td style="text-align: left;">−0.01</td>
<td style="text-align: left;"><strong>−0.02***</strong></td>
<td style="text-align: left;"><strong>0.03***</strong></td>
</tr>
<tr>
<td style="text-align: left;">BIT</td>
<td style="text-align: left;">38.70</td>
<td style="text-align: left;">5.21</td>
<td style="text-align: left;">38.75</td>
<td style="text-align: left;">4.70</td>
<td style="text-align: left;">39.00</td>
<td style="text-align: left;">5.09</td>
<td style="text-align: left;">38.39</td>
<td style="text-align: left;">5.42</td>
<td colspan="2" style="text-align: left;">−0.04</td>
<td style="text-align: left;">−0.26</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">−0.31</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L LSS</td>
<td style="text-align: left;">6.27</td>
<td style="text-align: left;">1.77</td>
<td style="text-align: left;">5.94</td>
<td style="text-align: left;">1.56</td>
<td style="text-align: left;">6.48</td>
<td style="text-align: left;">1.91</td>
<td style="text-align: left;">6.33</td>
<td style="text-align: left;">1.91</td>
<td colspan="2" style="text-align: left;"><strong>0.33**</strong></td>
<td style="text-align: left;"><strong>−0.54***</strong></td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;"><strong>0.27***</strong></td>
<td style="text-align: left;"><strong>−0.50***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB LSS</td>
<td style="text-align: left;">37.78</td>
<td style="text-align: left;">10.54</td>
<td style="text-align: left;">34.07</td>
<td style="text-align: left;">8.91</td>
<td style="text-align: left;">37.53</td>
<td style="text-align: left;">11.30</td>
<td style="text-align: left;">36.39</td>
<td style="text-align: left;">10.76</td>
<td colspan="2" style="text-align: left;"><strong>3.70***</strong></td>
<td style="text-align: left;"><strong>−3.45***</strong></td>
<td style="text-align: left;">1.14</td>
<td style="text-align: left;"><strong>3.35***</strong></td>
<td style="text-align: left;"><strong>−3.35***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB Activities LSS</td>
<td style="text-align: left;">3.41</td>
<td style="text-align: left;">1.05</td>
<td style="text-align: left;">3.30</td>
<td style="text-align: left;">0.98</td>
<td style="text-align: left;">3.66</td>
<td style="text-align: left;">1.49</td>
<td style="text-align: left;">3.56</td>
<td style="text-align: left;">1.40</td>
<td colspan="2" style="text-align: left;">0.11</td>
<td style="text-align: left;"><strong>−0.36***</strong></td>
<td style="text-align: left;">0.10</td>
<td style="text-align: left;">0.09</td>
<td style="text-align: left;"><strong>−0.31***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB Pain/discomfort LSS</td>
<td style="text-align: left;">5.92</td>
<td style="text-align: left;">2.42</td>
<td style="text-align: left;">5.30</td>
<td style="text-align: left;">2.12</td>
<td style="text-align: left;">5.89</td>
<td style="text-align: left;">2.39</td>
<td style="text-align: left;">5.91</td>
<td style="text-align: left;">2.50</td>
<td colspan="2" style="text-align: left;"><strong>0.62***</strong></td>
<td style="text-align: left;"><strong>−0.59***</strong></td>
<td style="text-align: left;">−0.02</td>
<td style="text-align: left;"><strong>0.51***</strong></td>
<td style="text-align: left;"><strong>−0.58***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB Psychosocial LSS</td>
<td style="text-align: left;">25.32</td>
<td style="text-align: left;">7.97</td>
<td style="text-align: left;">22.47</td>
<td style="text-align: left;">6.85</td>
<td style="text-align: left;">24.78</td>
<td style="text-align: left;">8.39</td>
<td style="text-align: left;">23.68</td>
<td style="text-align: left;">8.08</td>
<td colspan="2" style="text-align: left;"><strong>2.85***</strong></td>
<td style="text-align: left;"><strong>−2.32***</strong></td>
<td style="text-align: left;"><strong>1.10*</strong></td>
<td style="text-align: left;"><strong>2.63***</strong></td>
<td style="text-align: left;"><strong>−2.22***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-9 LSS</td>
<td style="text-align: left;">12.28</td>
<td style="text-align: left;">4.00</td>
<td style="text-align: left;">11.22</td>
<td style="text-align: left;">3.31</td>
<td style="text-align: left;">12.40</td>
<td style="text-align: left;">4.36</td>
<td style="text-align: left;">12.05</td>
<td style="text-align: left;">4.20</td>
<td colspan="2" style="text-align: left;"><strong>1.05***</strong></td>
<td style="text-align: left;"><strong>−1.18***</strong></td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;"><strong>0.91***</strong></td>
<td style="text-align: left;"><strong>−1.11***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-9 Psychosocial LSS</td>
<td style="text-align: left;">8.39</td>
<td style="text-align: left;">3.16</td>
<td style="text-align: left;">7.64</td>
<td style="text-align: left;">2.70</td>
<td style="text-align: left;">8.35</td>
<td style="text-align: left;">3.36</td>
<td style="text-align: left;">8.06</td>
<td style="text-align: left;">3.34</td>
<td colspan="2" style="text-align: left;"><strong>0.75***</strong></td>
<td style="text-align: left;"><strong>−0.71***</strong></td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;"><strong>0.65***</strong></td>
<td style="text-align: left;"><strong>−0.70***</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB-9 Physical LSS</td>
<td style="text-align: left;">3.89</td>
<td style="text-align: left;">1.27</td>
<td style="text-align: left;">3.59</td>
<td style="text-align: left;">1.21</td>
<td style="text-align: left;">4.05</td>
<td style="text-align: left;">1.54</td>
<td style="text-align: left;">3.99</td>
<td style="text-align: left;">1.50</td>
<td colspan="2" style="text-align: left;"><strong>0.30***</strong></td>
<td style="text-align: left;"><strong>−0.46***</strong></td>
<td style="text-align: left;">0.07</td>
<td style="text-align: left;"><strong>0.26***</strong></td>
<td style="text-align: left;"><strong>−0.42***</strong></td>
</tr>
</tbody>
</table>

BIT, Brief Inventory of Thriving; EQ-HWB, EQ Health and Wellbeing; LSS, level sum score; SD, standard deviation; VAS, visual analogue scale

<sup>a</sup> Using two sample t-test

<sup>b</sup> Using paired t-test

\* *p* \< 0.05, \*\* *p* \< 0.01, \*\*\* *p* \< 0.001

</div>

Figure <a href="#Fig1" data-ref-type="fig">1</a> shows the distribution of EQ-5D-5L and EQ-HWB responses (also see Supplementary Table <a href="#MOESM1" data-ref-type="supplementary-material">1</a>). Based on the data from the pre-heatwave survey, most of EQ-HWB (14 out of 25), EQ-HWB-9 (6 out of 9) and EQ-5D-5L (4 out of 5) items exhibited ceiling effects. For the EQ-5D-5L, the proportion of respondents reporting ‘no problems’ ranged from 58.2% (pain/discomfort) to 94.3% (self-care). For the EQ-HWB, the range was from 32.3% (accepted) to 94.0% (personal care). At the instrument level, both the EQ-5D-5L (47.0%) and EQ-HWB-9 (27.8%) exhibited ceiling effects. No floor effects were observed at either the item or instrument level for EQ-5D-5L, EQ-HWB-9 and EQ-HWB.

<figure id="Fig1">
<p><img src="12955_2026_2521_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="12955_2026_2521_Fig1_HTML.gif" /></p>
<figcaption>Distribution of EQ-5D-5L and EQ-HWB responses. Notes: *part of the EQ-HWB-9. **the responses for the three positively framed items were reversed</figcaption>
</figure>

The percentage of respondents who reported excessive sweating was 22.0% and 48.2%, in the heatwave 1 and heatwave 2 survey, respectively. The percentage of respondents who felt adapted to weather was 64.3% in both the heatwave 1 and heatwave 2 survey. As shown in Table <a href="#Tab3" data-ref-type="table">3</a>, during heatwaves, respondents who did not experience excessive sweating or were adapted to weather had higher EQ VAS, EQ-5D-5L and EQ-HWB-9 index values, and lower EQ-HWB LSS compared to those who experienced excessive sweating or were not adapted to weather, respectively, with the effect sizes ranging from negligible to medium (Cohen’s d: 0 to 0.52 for EQ VAS; 0.04 to 0.31 for EQ-5D-5L; 0.16 to 0.34 for EQ-HWB-9; 0.28 to 0.45 for EQ-HWB). Among the EQ-HWB and EQ-HWB-9 subscales, EQ-HWB pain/discomfort LSS, EQ-HWB psychosocial LSS, and EQ-HWB-9 psychosocial LSS demonstrated small effect sizes (Cohen’s d: 0.20 to 0.45), while EQ-HWB activities LSS and EQ-HWB-9 physical LSS showed negligible effect sizes (Cohen’s d: 0.04 to 0.20). Compared to these scores, BIT score exhibited smaller effect sizes (Cohen’s d: 0.05 to 0.42).

<div id="Tab3" class="table-wrap">

<div class="caption">

Known-groups validity for EQ-5D-5L, EQ-HWB, EQ-HWB-9 and BIT based on heatwaves related symptoms and adaptation

</div>

<img src="12955_2026_2521_Tab3_HTML.jpg" id="MO11" />

</div>

As shown in Table <a href="#Tab4" data-ref-type="table">4</a>, unexpectedly, EQ-5D-5L, EQ-HWB and EQ-HWB-9 scores changed in the opposite direction to the anticipated worsening in excessive sweating and adaptation to weather due to the onset of heatwave (SRM: 0 to 0.44). Specifically, respondents who experienced a worsening in self-perceived effect of heat in the heatwave 1 survey compared to the pre-heatwave survey reported better health and wellbeing. The measures demonstrated negligible responsiveness to improvement in self-perceived effects of heat (SRM: 0.01 to 0.19). The BIT score demonstrated negligible responsiveness to worsening in adaptation to weather due to the commence of heatwave (SRM: 0.04) and changed in the opposite direction to improvement in self-perceived effects of heat

<div id="Tab4" class="table-wrap">

<div class="caption">

Responsiveness for EQ-5D-5L, EQ-HWB, EQ-HWB-9 and BIT

</div>

<img src="12955_2026_2521_Tab4_HTML.jpg" id="MO118" />

</div>

The results of EQ-5D-5L index values based on Chinese EQ-5D-5L value set were similar to those based on the UK crosswalk and England EQ-5D-5L value sets. The findings on response distributions, ceiling/floor, known-groups validity and responsiveness were consistent between the entire sample and the subgroup with chronic conditions (Supplementary Table <a href="#MOESM1" data-ref-type="supplementary-material">2</a>–<a href="#MOESM1" data-ref-type="supplementary-material">4</a>).

## Discussion

In this study, we assessed the validity and responsiveness of the EQ-5D-5L, EQ-HWB, and EQ-HWB-9 instruments for measuring the health and wellbeing impacts of heatwaves among older adults. While some results were puzzling and challenging to interpret, our findings provided promising evidence for the ability of these instruments in capturing the health and wellbeing impact of heatwaves. To our knowledge, this study represents the first of its kind, contributing to advancing research efforts to quantify the HRQoL and wellbeing impacts of climate change events.

Our findings indicate that the EQ-5D-5L, EQ-HWB and EQ-HWB-9 possess satisfactory known-groups validity in distinguishing between different groups based on the self-perceived impact of heatwaves. The magnitude of the between-group differences was small to moderate most of the time, suggesting either suboptimal discriminatory power of the instruments or the small impact of the heatwaves during the study period. The latter is possible as the intensity and duration of the heatwaves in the study site were both lower compared to past years. The relatively good performance of the EQ-HWB and EQ-HWB-9 suggests that measuring both health and wellbeing aspects is relevant in the context of heatwaves. In addition, the EQ VAS demonstrated relatively larger effect sizes for some known groups, suggesting that the EQ VAS may be more sensitive to general differences in self-perceived health impact. As a unique component of the EQ-5D-5L, this finding highlights its potential usefulness in capturing overall health perception in a single question. Within the EQ-HWB, the psychosocial and pain/discomfort subscales demonstrated better known-groups validity than the activities subscale. This could be due to respondents having adjusted their activities such as reducing strenuous or outdoor activities during heatwaves. Changing activities would not be very difficult for the respondents as most of them were retired. As a result, they might not have felt much interference in their daily activities during heatwaves. In contrast, the unpleasant discomfort and mood disturbances due to high temperature are typically not preventable. This finding suggests that psychosocial and physical discomfort might be the main health and wellbeing impacts of heatwaves, highlighting the importance of considering these aspects when assessing outcomes in the context of heatwaves.

It was opposite to our expectation that health and wellbeing improved from the pre-heatwave survey to the first during-heatwave survey. Several potential explanations could account for these unexpected findings. One possible reason is that the instruments used may not be sufficiently responsive or sensitive to change in health status and wellbeing associated with heatwaves. Another contributing factor could be the nature of the heatwave itself. The heatwaves experienced in 2023, when we conducted our surveys, may not have been intense or prolonged enough to exert a significant impact on local residents’ health and wellbeing. This is particularly plausible given that 2023 was an atypical year, with summer temperatures being lower than those in previous and subsequent years \[51\], which may have lessened the impact on health and wellbeing. Additionally, the unexpected score changes from the pre-heatwave survey to the heatwave 1 survey might have reflected the lingering effects of the COVID-19 pandemic. Our pre-heatwave survey was conducted only a few months after the end of lockdown in China, a period during which the health of the study sample might have still been affected by COVID-19. This residual impact could have introduced variability in the health status of the study cohort, leading to unusually low and high levels of health status during the pre-heatwave and heatwave 1 survey, respectively. Because of this unexpected trend and the plausible reasons for it, we only used small subgroups of respondents who reported change in sweating and weather adaptation to evaluate responsiveness. It is worth noting that the magnitude of the mean differences in EQ-5D-5L index values was relatively small. However, given the variability in the recommended minimally important difference (MID) for the EQ-5D-5L index across different value sets, populations and settings \[30, 52\], it remains unclear whether the observed changes are practically meaningful.

Overall, all instruments exhibited limited responsiveness to the health and wellbeing impacts of heatwaves in this study. Comparatively, EQ-HWB with its 25 items measuring health and wellbeing was slightly more responsive than the five-item EQ-5D-5L measuring health, and EQ-HWB psychological subscale was more responsive than the activity and pain/discomfort subscales. Appending relevant bolt-ons targeting psychosocial or climate-related HRQoL dimensions may improve the conceptual coverage of EQ-5D-5L in heatwave research \[24, 25\]. Future studies could investigate whether appending such bolt-ons to the EQ-5D-5L enhances its sensitivity and relevance in capturing heatwave-related health impacts.

This study is subject to several limitations that should be acknowledged. First, there may be selection bias due to our centralized data collection method, which involved conducting face-to-face surveys in community centres. This approach required participants to be physically mobile, potentially excluding individuals whose health was most adversely affected by heatwaves from participation. Future research should consider using online or household surveys to ensure the inclusion of the most vulnerable populations, particularly those who may be less capable to attend centralized survey locations. Second, our study faced suboptimal follow-up rates, which could also be attributed to the data collection method. Participants who were unwell may have been more likely to drop out, particularly given the requirement to travel to the survey venue on hot days, which could have introduced attrition bias. Third, the timing of the heatwave 1 survey may have been suboptimal. Although we hypothesized that the first heatwave of the year would have a greater impact than subsequent heatwaves, it is possible that participants made extra efforts for the very first heatwave to mitigate the effects of heatwaves, such as reducing or changing their daily activities. These adaptive behaviours could have counteracted the effects of heatwaves or even resulted in a paradoxical improvement in health and wellbeing. Future studies should carefully consider the timing of assessments during heatwaves to better capture the true health impacts of heatwaves. Fourth, only the EQ-HWB was administered directly to respondents, and EQ-HWB-9 responses were derived from the corresponding items within the EQ-HWB. As the same item wording and response options were used, any differences between embedded and standalone administration would be expected to be minimal; however, this assumption warrants empirical evaluation in future research. Fifth, this study was conducted in only one city and two communities within China, which may restrict the generalizability of the findings to other geographic areas with different climate patterns, urban layouts, and levels of access to cooling resources. Finally, this study focused on older adults, and the findings may not be applicable to younger, working-age populations who might experience different impacts from heatwaves, such as occupational exposure or different adaptive behaviours. Future research could expand to include a more diverse range of locations and age groups to better understand the broader health implications of heatwaves.

## Conclusion

The EQ-5D-5L, EQ-HWB and EQ-HWB-9 demonstrated satisfactory known-groups validity but limited responsiveness in measuring the health and wellbeing impact of heatwaves among older adults. Further research is warranted to further evaluate these measures as well as other outcome measures for the purpose of quantifying the health and wellbeing impacts of heatwaves and other climate events.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

## Acknowledgements

Not applicable.

## Abbreviations

BIT  
Brief Inventory of Thriving

EQ-HWB  
EQ Health and Wellbeing

HRQoL  
Health-related quality of life

LSSs  
Level sum scores

SD  
Standard deviations

SRM  
Standardized response mean

VAS  
Visual analogue scale

## Author contributions

N.L., J.X., F.R. and Z.Y. contributed to study conceptualization, methodology, and funding acquisition. Data curation, project administration, resources, and supervision were provided by J.X. and N.L. M.L. conducted the formal analysis and, together with J.X. and N.L., drafted the manuscript. All authors reviewed and approved the final manuscript.

## Funding

This study was supported by the EuroQol Research Foundation (1599-RA). The funder had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

## Data availability

The data supporting this study are available from the corresponding authors upon reasonable request.

## Declarations

### Ethics approval and consent to participate

This study was approved by the Institutional Review Board of Fujian Medical University (reference number: 2023–146) and conducted in accordance with the Declaration of Helsinki. Informed consent was obtained from all participants.

### Consent for publication

Not applicable.

### Competing interests

F.R., Z.Y. and N.L. are members of the EuroQol Group. F.R. is employed by the EuroQol Research Foundation. F.R. serves as co-editor-in-chief at Health and Quality of Life Outcomes and had no involvement in the editorial or peer review process for this manuscript. The other authors have no conflicts of interest to declare. Views expressed in the article are those of the authors and are not necessarily those of the EuroQol Research Foundation.

## Footnotes

## Contributor Information

Jianjun Xiang, Email: jianjun.xiang@fjmu.edu.cn.

Nan Luo, Email: ephln@nus.edu.sg.

## References

## References

1. Marx W, Haunschild R, Bornmann L. Heat waves: a hot topic in climate change research. Appl Climatol. 2021;146(1):781–800. doi:10.1007/s00704-021-03758-y

2. The Copernicus Climate Change Service. Heatwaves grip parts of Europe, Asia and north America in the first half of 2022 [Available from: https://climate.copernicus.eu/heatwaves-grip-parts-europe-asia-and-north-america-first-half-2022].

3. Åström DO, Bertil F, Joacim R. Heat wave impact on morbidity and mortality in the elderly population: a review of recent studies. Maturitas. 2011;69(2):99–105. doi:10.1016/j.maturitas.2011.03.008

4. Zhang S, Zhang C, Cai W, Bai Y, Callaghan M, Chang N, et al. The 2023 China report of the Lancet countdown on health and climate change: taking stock for a thriving future. Lancet Public Health. 2023;8(12):e978–95. doi:10.1016/S2468-2667(23)00245-1

5. Mason H, C King J, E Peden A, C Franklin R. Systematic review of the impact of heatwaves on health service demand in Australia. BMC Health Serv Res. 2022;22(1):960. doi:10.1186/s12913-022-08341-3

6. Evoy R, Hystad P, Bae H, Kincl L. The impact of wildfire smoke and temperature on traumatic worker injury claims, Oregon 2009-2018. Health Sci Rep. 2022;5(5):e820. doi:10.1002/hsr2.820

7. Kjellstrom T, Briggs D, Freyberg C, Lemke B, Otto M, Hyatt O. Heat, human performance, and occupational health: a key issue for the assessment of global climate change impacts. Annu. Rev. Public Health. 2016;37(1):97–112. doi:10.1146/annurev-publhealth-032315-021740

8. Ebi KL, Capon A, Berry P, Broderick C, de Dear R, Havenith G, et al. Hot weather and heat extremes: health risks. Lancet. 2021;398(10301):698–708. doi:10.1016/S0140-6736(21)01208-3

9. Palinkas LA, Hurlburt MS, Fernandez C, De Leon J, Yu K, Salinas E, et al. Vulnerable, resilient, or both? A qualitative study of adaptation resources and behaviors to heat waves and health outcomes of low-income residents of urban heat islands. Int J Environ Res Public Health. 2022;19(17):11090. doi:10.3390/ijerph191711090

10. Williams ML. Global warming, heat-related illnesses, and the dermatologist. Int J Multiling Women’s Dermatol. 2021;7(1):70–84. doi:10.1016/j.ijwd.2020.08.007

11. Wong YL, Wong SW, Ting DS, Muralidhar A, Sen S, Schaff O, et al. Impacts of climate change on ocular health: a scoping review. The J Clim Change Health. 2024;15:100296. doi:10.1016/j.joclim.2023.100296

12. Zhou W, Wang Q, Li R, Zhang Z, Kadier A, Wang W, et al. Heatwave exposure in relation to decreased sleep duration in older adults. Environ Int. 2024;183:108348. doi:10.1016/j.envint.2023.108348

13. Obradovich N, Migliorini R, Mednick SC, Fowler JH. Nighttime temperature and human sleep loss in a changing climate. Sci Adv. 2017;3(5):e1601555. doi:10.1126/sciadv.1601555

14. Thompson R, Hornigold R, Page L, Waite T. Associations between high ambient temperatures and heat waves with mental health outcomes: a systematic review. Public Health. 2018;161:171–91. doi:10.1016/j.puhe.2018.06.008

15. Miles-Novelo A, Anderson CA. Climate change and psychology: effects of rapid global warming on violence and aggression. Curr Clim Change Rep. 2019;5:36–46.

16. Fang B, Zhang Q. Heatwaves and its impact on the depressive symptoms among Chinese community-dwelling older adults: examining the role of social participation. Arch Gerontol Geriat. 2025;129:105668. doi:10.1016/j.archger.2024.105668

17. Kong L-s, Chen D, Zhang J-d, Cheng X-f, Zhang Y-l, Li B. The correlation between high temperature and cognitive function: a CHARLS, 2018 cross-sectional study. Archives Public Health. 2025;83(1):181. doi:10.1186/s13690-025-01665-6

18. Wang H, Fang T. Cumulative heat exposure and mental health in older Chinese adults with social isolation mediation. Sci Rep. 2025;15(1):43470. doi:10.1038/s41598-025-27446-3

19. Devlin NJ, Brooks R. EQ-5D and the EuroQol group: past, present and future. Appl Health Econ Health Policy. 2017;15:127–37. doi:10.1007/s40258-017-0310-5

20. Wang A, Rand K, Yang Z, Brooks R, Busschbach J. The remarkably frequent use of EQ-5D in non-economic research. The Eur J Health Econ. 2022;1–8. doi:10.1007/s10198-021-01411-z

21. Hugelius K, Gifford M, Örtenwall P, Adolfsson A. Health among disaster survivors and health professionals after the haiyan typhoon: a self-selected internet-based web survey. Int J Emerg Med. 2017;10:1–9. doi:10.1186/s12245-017-0139-6

22. Andrade MV, de Souza Noronha KVM, Santos AS, de Souza A, Guedes GR, Campolina B, et al. Estimation of health-related quality of life losses owing to a technological disaster in Brazil using EQ-5D-3L: a cross-sectional study. Value Health Reg Issues. 2021;26:66–74. doi:10.1016/j.vhri.2021.02.003

23. Yang F, Leon-Giraldo S, Moreno-Serra R. Health-related quality of life of a conflict-affected population in Colombia. Qual Life Res. 2021;1–11. doi:10.1007/s11136-021-02805-5

24. Fan J, Mao Z, Song X, Rencz F, Yang Z, Luo N, et al. Identifying and developing culturally relevant EQ-5D-5L bolt-on items for Chinese population: qualitative phase of a mixed-methods study. Qual Life Res. 2025;34(10):2851–63. doi:10.1007/s11136-025-04028-4

25. Fan J, Mao Z, Rencz F, Yang Z, Luo N, Wang P. Testing culturally relevant EQ-5D-5L bolt-ons for the Chinese general population: first quantitative phase of a mixed methods study. Qual Life Res. 2026;35(3):62. doi:10.1007/s11136-026-04171-6

26. Brazier J, Peasgood T, Mukuria C, Marten O, Kreimeier S, Luo N, et al. The EQ-HWB: overview of the development of a measure of health and wellbeing and key results. Value Health. 2022;25(4):482–91. doi:10.1016/j.jval.2022.01.009

27. Worfolk JB. Heat waves: their impact on the health of elders. Geriatric Nurs. 2000;21(2):70–77. doi:10.1067/mgn.2000.107131

28. Kenny GP, Yardley J, Brown C, Sigal RJ, Jay O. Heat stress in older individuals and patients with common chronic diseases. Cmaj. 2010;182(10):1053–60. doi:10.1503/cmaj.081050

29. China Meteorological Administration. What is heatwave? 2011 [Available from: https://www.cma.gov.cn/2011qxfw/2011qqxkp/2011qkpdt/201110/t20111026_124192.html].

30. Cheng LJ, Chen LA, Cheng JY, Herdman M, Luo N. Systematic review reveals that EQ-5D minimally important differences vary with treatment type and may decrease with increasing baseline score. J Educ Chang Clin Epidemiol. 2024;174:111487. doi:10.1016/j.jclinepi.2024.111487

31. Liss A, Wu R, Chui KKH, Naumova EN. Heat-related hospitalizations in older adults: an amplified effect of the first seasonal heatwave. Sci Rep. 2017;7(1):39581. doi:10.1038/srep39581

32. Anderson GB, Bell ML. Heat waves in the United States: mortality risk during heat waves and effect modification by heat wave characteristics in 43 US communities. Environ Health Perspectives. 2011;119(2):210–18. doi:10.1289/ehp.1002313

33. Ye X, Wolff R, Yu W, Vaneckova P, Pan X, Tong S. Ambient temperature and morbidity: a review of epidemiological evidence. Environ Health Perspectives. 2012;120(1):19–28. doi:10.1289/ehp.1003198

34. Wang P, Zhang X, Hashizume M, Goggins WB, Luo C. A systematic review on lagged associations in climate-health studies. Int J Epidemiol. 2021;50(4):1199–212. doi:10.1093/ije/dyaa286

35. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20:1727–36. doi:10.1007/s11136-011-9903-x

36. Yang Z, Liu G, Jiang J, Wang P, Jin X, Wu J, et al. Re-estimating an EQ-5D-5L value set for China working paper. 2024.

37. Van Hout B, Janssen M, Y-S F, Kohlmann T, Busschbach J, Golicki D, et al. Interim scoring for the EQ-5D-5L: mapping the EQ-5D-5L to EQ-5D-3L value sets. Value Health. 2012;15(5):708–15. doi:10.1016/j.jval.2012.02.008

38. Devlin NJ, Shah KK, Feng Y, Mulhern B, Van Hout B. Valuing health-related quality of life: an EQ-5 D-5 L value set for England. Health Econ. 2018;27(1):7–22. doi:10.1002/hec.3564

39. NIfHac E. NICE health technology evaluations: the manual, editor. Excellence NIfHaC. 2022.

40. Rowen D, Mukuria C, Bray N, Carlton J, Cooper S, Longworth L, et al. UK valuation of EQ-5D-5L, a generic measure of health-related quality of life: a study protocol. Value Health. 2023;26(11):1625–35. doi:10.1016/j.jval.2023.08.005

41. Long C, Mao Z, Yang Z. A head-to-head comparison of EQ-HWB and EQ-5D-5L in patients, carers, and general public in China. Value Health. 2024;27(7):848–56. doi:10.1016/j.jval.2024.02.012

42. Mukuria C, Peasgood T, McDool E, Norman R, Rowen D, Brazier J. Valuing the EQ health and wellbeing short using time trade-off and a discrete choice experiment: a feasibility study. Value Health. 2023;26(7):1073–84. doi:10.1016/j.jval.2023.02.008

43. Kuharić M, Pickard AS, Mukuria C, Finch AP. The measurement properties of the EQ health and well-being and EQ health and well-being short form in Italian population: a comparative study with EQ-5D-5L. Value Health. 2024. doi:10.1016/j.jval.2024.03.002

44. Feng Y-S, Kohlmann T, Peasgood T, Engel L, Mulhern B, Pickard AS. Scoring the EQ-HWB-S: Can we do it without value sets? A non-parametric item response theory analysis. Qual Life Res. 2024;33(5):1211–22. doi:10.1007/s11136-024-03601-7

45. Pangestu S, Purba FD, Setyowibowo H, Azhar Y, Mukuria C, Rencz F. The psychometric properties of the EQ-HWB and EQ-HWB-S in patients with breast cancer: a comparative analysis with EQ-5D-5L, FACT-8D, and SWEMWBS. Value Health. 2025;28(3):449–59. doi:10.1016/j.jval.2024.12.003

46. Kinchin I, Engel L, Rencz F. A comparative study of health and well-being measures in Ireland using EQ health and wellbeing (EQ-HWB) and its short version, EQ-5D-5L, and ICEpop capability measure for adults (ICECAP-A). Value Health. 2025;28(8):1268–79. doi:10.1016/j.jval.2025.04.2160

47. Su R, Tay L, Diener E. The development and validation of the comprehensive Inventory of Thriving (CIT) and the Brief Inventory of Thriving (BIT). Appl Psychol Health Well Being. 2014;6(3):251–79. doi:10.1111/aphw.12027

48. The Reliable Prognosis weather portal 2023 [Available from: https://rp5.ru/Weather_in_the_world].

49. Terwee CB, Bot SD, de Boer MR, Van der Windt DA, Knol DL, Dekker J, et al. Quality criteria were proposed for measurement properties of health status questionnaires. J Educ Chang Clin Epidemiol. 2007;60(1):34–42. doi:10.1016/j.jclinepi.2006.03.012

50. Cohen J. Statistical power analysis for the behavioral sciences. routledge; 2013.

51. China Meteorological Data Service Centre. 2024 [Available from: http://data.cma.cn/en].

52. Al Sayah F, Jin X, Short H, Ns M, Ohinmaa A, Johnson JA. A systematic literature review of important and meaningful differences in the EQ-5D index and visual analog scale scores. Value Health. 2025;28(3):470–76. doi:10.1016/j.jval.2024.11.006

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary Material 1

</div>

### Data Availability Statement

The data supporting this study are available from the corresponding authors upon reasonable request.

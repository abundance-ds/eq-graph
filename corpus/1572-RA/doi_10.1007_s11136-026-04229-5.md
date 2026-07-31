---
project_id: "1572-RA"
work_id: "doi:10.1007/s11136-026-04229-5"
doi: "10.1007/s11136-026-04229-5"
pmid: "41920450"
pmcid: "PMC13043564"
title: "Measuring health-related quality of life in multiple sclerosis: comparing the acceptability, validity and responsiveness of the EQ-5D-3L and MSIS-8D"
journal: "Quality of Life Research"
publication_date: "2026-04-01"
volume: "35"
issue: "5"
authors:
  - name: "Elizabeth Goodwin"
    affiliation_ids:
      - "Aff1"
  - name: "Bernhard Michalowsky"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Rod Middleton"
    affiliation_ids:
      - "Aff4"
  - name: "Annie Hawton"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "University of Exeter Medical School, University of Exeter, Exeter, UK"
  - id: "Aff2"
    name: "Patient-Reported Outcomes and Health Economics Research, German Center for Neurodegenerative Diseases (DZNE), Greifswald, Germany"
  - id: "Aff3"
    name: "Department of Health Research Methods, Evidence and Impact, McMaster University, Hamilton, Canada"
  - id: "Aff4"
    name: "Population Data Science, Swansea University, Swansea, UK"
licence: "cc-by"
source_file: "input/projects/1572-RA/papers/doi_10.1007_s11136-026-04229-5.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13043564/fullTextXML"
source_method: "epmc_xml"
source_sha256: "1a748073e9280046e6ab2ac4581f27084752a92fecab8dea4eee537ad13c45ae"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Measuring health-related quality of life in multiple sclerosis: comparing the acceptability, validity and responsiveness of the EQ-5D-3L and MSIS-8D

## Abstract

### Purpose

Concerns have been raised about the sensitivity and responsiveness of the EQ-5D, one of the most commonly used preference-based health-related quality of life measures, in the context of multiple sclerosis (MS). In response to these concerns, a condition-specific preference-based measure, the Multiple Sclerosis Impact Scale Eight Dimensions (MSIS-8D), was developed. This research aimed to assess the psychometric and distributional properties of the MSIS-8D compared to the EQ-5D-3L, in people with MS.

### Methods

Analyses were undertaken using data from the UK MS Register. Both measures were compared in terms of acceptability (missing data), distributional properties (health state frequencies, health state density curves and indices), construct validity in relation to disability, mobility, fatigue, anxiety and depression (discriminative and convergent validity, using ANOVA, independent t-tests and Spearman correlations), and responsiveness to symptom onset and relapse (mean change scores, standardised response means, standardised effect sizes, paired t-tests).

### Results

The MSIS-8D exhibited superior distributional properties, while the EQ-5D-3L showed greater acceptability. Both measures demonstrated excellent construct validity. Neither measure appeared responsive to symptom onset, and only the MSIS-8D met all criteria for responsiveness when people moved from a non-relapse to a relapse state.

### Conclusion

Although the MSIS-8D appears to offer superior distributional properties and responsiveness compared to the EQ-5D-3L, the responsiveness of both measures in this analysis was limited. This adds weight to existing concerns about the ability of utility measures used in healthcare decision-making to fully capture treatment effects in MS.

**Keywords:** Preference-based measures, Health-related quality of life, Psychometrics, Economic evaluation, Multiple sclerosis, EQ-5D

Received 2025 Nov 12; Accepted 2026 Mar 10; Issue date 2026.

## Introduction

MS is the most common, non-traumatic cause of disability among younger adults worldwide \[1\]. It is a complex and progressive condition, affecting the central nervous system \[2\]. This causes a wide range of physical, psychological and cognitive symptoms, which vary considerably across individuals \[3\]. The most common subtype is relapsing–remitting MS (RRMS), in which the disease course is characterised by periods of relapse and remission. The majority of people with RRMS go on to develop secondary progressive MS (SPMS). Around 10–15% of people with MS are diagnosed with primary progressive MS (PPMS), which is progressive from the outset. Levels of disability increase as the disease progresses \[2\]. Research has shown that MS patients show considerable decrements compared to the general population on all domains of health-related quality of life (HRQoL) \[4\].

The National Institute for Health and Care Excellence (NICE) recommends the use of the EQ-5D, a generic preference-based measure (PBM) of HRQoL, for use in economic evaluations of new healthcare interventions in England and Wales \[5\]. Following a number of unfavourable decisions by NICE regarding the cost-effectiveness of disease-modifying treatments (DMTs) for multiple sclerosis (MS), concerns were raised about the appropriateness of using the EQ-5D-3L to measure health outcomes in MS \[6\], particularly in relation to its content and construct validity \[7–10\]. Also, evidence for the responsiveness of the EQ-5D to changes in the HRQoL of people with MS is lacking \[10\], which is of particular concern in the context of economic evaluation, given that a measurement tool with poor responsiveness may fail to demonstrate effects of treatment when they occur.

When undertaking economic evaluations of treatments for conditions in which the EQ-5D lacks validity and responsiveness, it can be acceptable to use a condition-specific preference-based measure (CSPBM) \[11\]. The descriptive system for a CSPBM includes dimensions of HRQoL that are of particular relevance to people with that condition, and may exclude less relevant domains that are typically included in generic GPBMs. This enhanced content validity aims to more fully capture important differences and changes in HRQoL, however this can come at a cost \[12\]. Consistent use of the EQ-5D allows direct comparability of economic evaluation results across treatments and conditions. While use of the same valuation protocol will achieve a degree of comparability between PBMs with different descriptive systems, CSPBMs may be less likely to capture side-effects and impacts of comorbidities, and their associated utility values may be prone to focusing effects during valuation due to the lack of a broader context around condition-specific health state descriptions \[13\]. For these reasons, it is generally recommended that CSPBMs are used in addition to, rather than instead of, a generic PBM \[12\].

In response to the concerns regarding the appropriateness of the EQ-5D for MS, a CSPBM, the Multiple Sclerosis Impact Scale-Eight Dimensions (MSIS-8D), was developed, enabling utility values to be estimated from responses to an existing patient-reported measure of HRQoL in MS, the Multiple Sclerosis Impact Scale (MSIS-29-v2) \[14\]. The MSIS-8D tariff was estimated using preferences from a sample of the UK general population via the time trade-off method \[15\]. The MSIS-8D has been used alongside the EQ-5D in trial-based economic evaluations \[16–19\]. However, there is still limited evidence for whether the MSIS-8D demonstrates the intended improvements in acceptability, validity and responsiveness compared to the EQ-5D.

Therefore, this study aimed to assess the acceptability, distributional properties, construct (discriminative and convergent) validity and responsiveness of the MSIS-8D, compared to the EQ-5D-3L, in a large, representative cohort of people with MS living in the UK, in order to inform decisions regarding the appropriate choice of outcome measures for economic evaluations of treatments for MS. The content of this paper is informed by the revised COSMIN reporting guideline for studies on measurement properties of patient-reported outcome measures \[20\].

## Methods

### UK MS register and population

This analysis used data routinely collected by the UK MS Register (UKMSR), a large, ongoing, prospective, longitudinal, observational, cohort study that was launched in 2011 \[21\]. Recruitment to the UKMSR is by word of mouth, information provided to patients of the UKMSR’s clinical partner sites (currently 56 NHS hospitals across the UK), or presentations and display stands at relevant events. At Spring 2023, the number of current, consented UKMSR members was c10,600, with around 54% of these providing full MSIS-29v2 data at this timepoint. The membership of the UKMSR has been shown to be broadly representative of people living with MS in the UK \[22, 23\].

On registration, new members are requested to provide information on socio-demographic and health-related characteristics and to complete a number of patient-reported outcome measures (PROMs). Subsequently, all members receive email reminders to complete the PROMs on a regular basis. From May 2011 to October 2017, members were invited to provide data on a 3-monthly basis, for the MSIS-29v2, EQ-5D-3L, Multiple Sclerosis Walking Scale (MSWS-12), and Hospital Anxiety and Depression Scales (HADS-A, HADS-D). From October 2017 onwards, this changed to 6-monthly data collection, and the self-reported Expanded Disability Status Score (web-EDSS) and Fatigue Severity Scale (FSS) were added to the suite of PROMs. The PROMs are presented as a ’to do’ list with members able to choose their own order of completion. Members are prompted to update their socio-demographic and health-related characteristics data annually. All data entry is online, via a secure internet portal \[21\].

Participants must be aged 18 or over, and provide consent via a Terms of Service agreement \[23\]. Ethical approval for the UKMSR has been provided by the South West Central Bristol Research Ethics Council initially as 16/SW/0164 now 21/SS/0085.

Cross-sectional analyses were based on data from all UKMSR members providing data on both the EQ-5D-3L and MSIS-29 at the Spring 2023 data collection time-point. Responsiveness analysis used data from UKMSR members who reported experiencing either one of two events (described below) that would be expected to have an effect on their HRQoL, up to the Spring 2023 data collection window. The UKMSR restricted the data extracts for both analyses to people who had provided full responses to the EQ-5D-3L at Spring 2023 and on at least four more occasions over the 11 year period.

### Data and instruments

The ‘target measures’ for the analysis were:

- EQ-5D-3L: a generic, preference-based measure of HRQoL with five dimensions (mobility, self-care, usual activities, pain/discomfort, anxiety/depression) and three response levels (1 = no, 2 = some, 3 = extreme problems), generating 243 health states. Respondents are asked to describe their health ‘today’. Responses to the EQ-5D-3L were converted to utility values using the UK value set, which has a maximum value range from −0.594 to 1.000 \[24\].

- MSIS-8D: an MS-specific preference-based measure of HRQoL with eight dimensions taken from items of the MSIS-29v2 (physical tasks, social activities, mobility, daily activities, fatigue, emotion, cognition, depression) and four response levels (1 = not at all, 2 = a little, 3 = moderately, 4 = extremely), generating 65,536 health states. Respondents are asked to describe the impact of their MS on each dimension over the past two weeks. The MSIS-8D descriptive system is presented in the Appendix. MSIS-29v2 responses were converted to MSIS-8D utility values by the application of a published algorithm based on the preferences of a representative sample of the general UK population, which has a maximum value range from 0.079 to 0.882 \[15\].

The variables representing events expected to affect HRQoL were date of most recent relapse, and date of onset of two or more new symptoms. The criteria for selection of these events were (i) hypothesised to have an effect on HRQoL and (ii) recorded on the UKMSR with sufficient detail to enable responsiveness analysis. Further details of these variables and hypotheses are provided in Table <a href="#Tab1" data-ref-type="table">1</a>.

<div id="Tab1" class="table-wrap">

<div class="caption">

Description of variables representing events expected to affect HRQoL, their hypothesised effects on HRQoL, and how they were used in the responsiveness analyses

</div>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">Relapse</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Hypothesis</td>
<td style="text-align: left;">We would expect HRQoL during a relapse to be lower than that experienced during a period of remission. Recovery following relapse is often incomplete, resulting in a sustained negative impact on quality of life for up to 12 months [<span class="citation" data-cites="CR29">29</span>], hence the most relevant comparison will be between pre-relapse and during-relapse utility values</td>
</tr>
<tr>
<td style="text-align: left;">Rationale</td>
<td style="text-align: left;">MS relapses are characterised by an exacerbation of existing MS symptoms, or the appearance of new symptoms, for a period of time, followed by complete or partial remission. People with MS report that relapses impact upon their daily activities, emotional wellbeing, social functioning and work performance [<span class="citation" data-cites="CR30">30</span>]</td>
</tr>
<tr>
<td style="text-align: left;">Variable description</td>
<td style="text-align: left;">Participants who have answered “yes” to “Have you had ANY relapses in the last 6 months?” are asked to report the calendar month during which the most recent relapse occurred. The relevant year can be inferred from the auto-generated date-stamp for this variable. These data were used to create a variable that identifies the month and year in which the relapse occurred</td>
</tr>
<tr>
<td style="text-align: left;">Time-points</td>
<td style="text-align: left;">EQ-5D-3L and MSIS-8D utility values for an assessment point [<em>t</em>–1] <em>prior</em> to the reported relapse were compared with EQ-5D-3L and MSIS-8D utility values for the <em>same assessment point</em> [<em>t</em>] in which the relapse was reported, provided that no current relapse was reported at the date of the earlier utility value [<em>t</em>–1]</td>
</tr>
<tr>
<td style="text-align: left;">Inclusion criteria</td>
<td style="text-align: left;"><p>Participants were included in the analyses if:</p>
<p>• The calendar month and year of their most recent relapse were the same as the calendar month and year of reporting a utility value and</p>
<p>• They reported a utility value at a preceding time-point [<em>t</em>–1] within 12 months (400 days) prior to the date at which the utility value corresponding to the relapse was reported and</p>
<p>• They did not report a current relapse at [<em>t</em>–1]</p>
<p>A participant could be included more than once in the analysis if they met the above inclusion criteria at more than one point during the study period</p></td>
</tr>
<tr>
<td style="text-align: left;">Notes:</td>
<td style="text-align: left;">The actual number of days used to represent one year was increased to 400 days to allow for variation in the point during each data collection window at which the individual MSR member completed the questionnaires</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">Onset of new symptoms</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Hypothesis</td>
<td style="text-align: left;">We would expect the onset of new symptoms to result in an immediate deterioration in HRQoL</td>
</tr>
<tr>
<td style="text-align: left;">Rationale</td>
<td style="text-align: left;">A variety of individual physical, psychological and cognitive symptoms of MS have been found to have a significant, negative impact on the quality of life of people with MS [<span class="citation" data-cites="CR31">31</span>]</td>
</tr>
<tr>
<td style="text-align: left;">Variable description</td>
<td style="text-align: left;">Participants are asked to report which symptoms they experience from a list of 25 symptoms, and to report the date of onset of each symptom</td>
</tr>
<tr>
<td style="text-align: left;">Time-points</td>
<td style="text-align: left;">EQ-5D-3L and MSIS-8D utility values for an assessment point [<em>t</em>–1] <em>prior</em> to the symptom onset date were compared with EQ-5D-3L and MSIS-8D utility values for an assessment point [<em>t</em>] <em>up to 30 days after</em> the symptom onset date</td>
</tr>
<tr>
<td style="text-align: left;">Inclusion criteria</td>
<td style="text-align: left;"><p>Participants were included in the analyses if:</p>
<p>• They reported the onset of a new symptom and the reported date of symptom onset was within the study period and</p>
<p>• They reported a utility value within one year (400 days) prior to the reported start date of the symptom and</p>
<p>• They reported a utility value up to 1 month (30 days) after the reported start date of the symptom and</p>
<p>• They reported the onset of at least two new symptoms between the dates of the two utility values</p>
<p>For people reporting the onset of a particular symptom more than once in the study period, only the first reported date of symptom onset was included. People could be included more than once in the analysis if they reported the onset of two or more symptoms (according to the inclusion criteria above) more than once during the assessment period</p></td>
</tr>
<tr>
<td style="text-align: left;">Other details</td>
<td style="text-align: left;">Symptoms: optic neuritis, double vision, impairment of motor control, sensory loss, pins and needles, muscle pain, bladder problems, bowel problems, sexual dysfunction, altered sensation, weakness, spasticity, difficulty swallowing, difficulty speaking, trigeminal neuralgia, tremors, dysarthia, nystagmus, fatigue, depression, pain, cognitive difficulties, brief repetitive symptoms, gait, ataxia</td>
</tr>
</tbody>
</table>

</div>

Data for analysis also included socio-demographics (age, gender, ethnicity), MS subtype (RRMS, SPMS, PPMS, benign MS) and the following standardized and validated PROMs: the web-EDSS, which measures MS-specific disability \[25\]; the FSS \[26\]; the MSWS-12 \[27\]; and the HADS-A and HADS-D \[28\].

### Statistical analyses

#### Cross-sectional analyses

Acceptability was assessed by comparing rates of missing data for the target measures, using a separate data extract that included all people who responded to at least one of the UKMSR’s regularly administered survey instruments during the Spring 2023 data collection window. The UKMSR data collection portal does not allow partial responses to instruments. Therefore information on acceptability at an individual dimension level was not available.

The distributional properties of the EQ-5D-3L and MSIS-8D descriptive systems were compared by examining the frequency of health states across the sample including floor and ceiling effects, health state density curves (HSDCs) and health state density indices (HSDIs). The HSDC and HSDI are analogous to the Lorenz curve and Gini coefficient that are frequently used to describe income distributions \[32\]. HSDCs provide a graphical representation of how evenly responses to a measure are distributed across the full range of possible health state profiles. Total equality of distribution, i.e. a hypothetical sample in which the same proportion of participants report each health state, is represented by a 45% line. The closer the HSDC is to the 45% line, the more evenly participants are distributed across health states. The HSDI ranges from 0 to 1, where 1 represents total equality of distribution and 0 represents total inequality (i.e. all participants reported the same health state) \[33\]. In addition, bar charts were used to illustrate the distribution of responses across individual dimension levels.

The discriminative validity of the target measures was evaluated according to their ability to differentiate between subgroups based on levels of disability (web-EDSS) and symptom severity (MSWS-12, FSS, HADS), assuming an inverse relationship between disability or symptom severity and HRQoL. The published cut-off scores for the webEDSS \[25\], FSS \[34\], HADS-D and HADS-A \[28\], and the mid-point score for the MSWS-12 \[35\], were used to create binary groups for levels of disability, fatigue, depression, anxiety and walking impairment. The target measures were also compared according to their ability to differentiate between MS subtypes, assuming that HRQoL diminishes from benign MS to RRMS, PPMS and SPMS \[36\]. Differences in mean utility values between subgroups were assessed using one-way ANOVAs or independent t-tests.

Convergent validity was assessed by examining Spearman’s correlation coefficients between the target measures and each of the measures of disability (web-EDSS) and symptom severity (MSWS-12, FSS, HADS). A correlation coefficient between 0.3 and 0.5 represents a moderate relationship; strong relationships are considered to be ≥ 0.5 \[37\].

#### Longitudinal analysis (responsiveness)

The responsiveness of the target measures was assessed by examining changes in utility values from before to during a relapse, and from before to after onset of new symptoms. Paired t-tests were used to indicate the presence or absence of the hypothesised effect on HRQoL, and to provide an initial signal of responsiveness. Standardised effect sizes (SES), calculated as the mean change divided by the standard deviation of the earlier mean score, were used to determine whether the change on either instrument was statistically non-negligible, i.e. at least a small effect size (SES ≥ 0.2) \[38\]. Standardised response means (SRM), calculated as the mean change divided by the standard deviation of the mean change, were used to compare responsiveness between the EQ-5D-3L and MSIS-8D, by estimating 95% confidence intervals for the SRMs \[39, 40\]. Scores on individual dimensions of the target measures before and after reported changes in each of the selected variables were compared using the Wilcoxon Signed Rank Test for paired samples.

All analyses were undertaken in Stata 18.

## Results

### Sample characteristics

Data from 3676 UKMSR members were available for the cross-sectional analyses. The characteristics of this sample are summarised in Table <a href="#Tab2" data-ref-type="table">2</a>.

<div id="Tab2" class="table-wrap">

<div class="caption">

Descriptive statistics for cross-sectional analysis

</div>

<table>
<thead>
<tr>
<th colspan="3" style="text-align: left;">Cross-sectional analysis</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Percent</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: left;">Included in analysis</td>
</tr>
<tr>
<td style="text-align: left;">Observations</td>
<td style="text-align: left;">3676</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">3676</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Gender</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">2727</td>
<td style="text-align: center;">74.18</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">946</td>
<td style="text-align: center;">25.73</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Ethnicity</td>
</tr>
<tr>
<td style="text-align: left;">White British</td>
<td style="text-align: left;">3365</td>
<td style="text-align: center;">91.79</td>
</tr>
<tr>
<td style="text-align: left;">Other/not stated</td>
<td style="text-align: left;">311</td>
<td style="text-align: center;">8.21</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Contemporary MS type<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">RRMS</td>
<td style="text-align: left;">1862</td>
<td style="text-align: center;">50.67</td>
</tr>
<tr>
<td style="text-align: left;">SPMS</td>
<td style="text-align: left;">1110</td>
<td style="text-align: center;">30.2</td>
</tr>
<tr>
<td style="text-align: left;">PPMS</td>
<td style="text-align: left;">491</td>
<td style="text-align: center;">13.36</td>
</tr>
<tr>
<td style="text-align: left;">Benign<sup>b</sup></td>
<td style="text-align: left;">76</td>
<td style="text-align: center;">2.07</td>
</tr>
<tr>
<td style="text-align: left;">Not known</td>
<td style="text-align: left;">136</td>
<td style="text-align: center;">3.7</td>
</tr>
</tbody>
</table>

| Other variables     | Obs  | Mean  | S.D   | Min      | Max   |
|---------------------|------|-------|-------|----------|-------|
| Age<sup>a</sup>     | 3676 | 58.32 | 10.8  | 22       | 89    |
| webEDSS score       | 3619 | 4.94  | 2.06  | 0        | 9     |
| MSWS-12 total score | 2854 | 44.99 | 32.72 | 0        | 100   |
| FSS total score     | 3667 | 4.85  | 1.52  | 1        | 7     |
| HADS-D total score  | 3625 | 6.64  | 4.27  | 0        | 21    |
| HADS-A total score  | 3616 | 6.89  | 4.48  | 0        | 21    |
| EQ-5D-3L value      | 3676 | 0.567 | 0.321 |  − 0.594 | 1     |
| MSIS-8D value       | 3676 | 0.626 | 0.185 | 0.079    | 0.882 |

Obs: observations; S.D.: standard deviation; RRMS: relapsing–remitting MS; SPMS: secondary progressive MS; PPMS: primary progressive MS

<sup>a</sup>MS Type and Age are contemporary with each data collection window (i.e. Age increases over time and MS Type changes if amended by the UKMSR member)

<sup>b</sup>Benign MS is characterised by minimal physical disability maintained over a duration of 10 or more years following diagnosis

</div>

### Acceptability

Of the 6141 UKMSR members who were included in the acceptability (missing data) analysis, 3.14% did not complete the EQ-5D-3L (n = 5948) and 8.57% did not complete the MSIS-8D (n = 5615). Differences were statistically significant (*p* \< 0.001).

### Distributional properties

The EQ-5D-3L exhibited a significantly greater ceiling effect than the MSIS-8D (409 observations, 11.13% versus 142 observations, 3.86%; *p* \< 0.001). Both instruments had negligible floor effects (\< 1%). The most frequently observed EQ-5D-3L health state was 22222 (493 observations, 13.41%). The most frequently observed MSIS-8D health state was 11111111 (142 observations, 3.86%), representing the instrument's ceiling. Nearly half the observations in the sample (49.32%) were covered by five EQ-5D-3L health states: 22222, 11111, 22221, 21222, 21221. Conversely, the five most frequently observed MSIS-8D health states accounted for only 8.19% of the sample: 11111111, 21111111, 11112221, 11112111, 11112121.

Figure <a href="#Fig1" data-ref-type="fig">1</a> illustrates the distribution of EQ-5D-3L and MSIS-8D responses by dimension. Very low proportions of responses were observed at Level 3 of all EQ-5D-3L dimensions. The EQ-5D-3L *Mobility*, *Usual Activities* and *Pain/Discomfort* dimensions show a high concentration of responses at Level 2, and *Self-care* at Level 1. Responses were more evenly distributed across each MSIS-8D dimension than they were for the EQ-5D-3L, although the proportions at the ‘extremely’ level for the *Emotion*, *Cognition* and *Depression* dimensions were relatively low, with higher proportions reporting ‘not at all’ for *Depression* and ‘a little’ for *Emotion* and *Cognition*.

<figure id="Fig1">
<p><img src="11136_2026_4229_Fig1_HTML.jpg" id="d33e868" /></p>
<p><img src="11136_2026_4229_Fig1_HTML.gif" /></p>
<figcaption>Distribution of EQ-5D-3L and MSIS-8D responses by dimension</figcaption>
</figure>

The HSDCs for the EQ-5D-3L and MSIS-8D (Fig. <a href="#Fig2" data-ref-type="fig">2</a>) show that the MSIS-8D HSDC is closer to the dotted line, which represents total equality of distribution, than the EQ-5D-3L HSDC. The HSDI was closer to one for the MSIS-8D than for the EQ-5D (MSIS-8D = 0.577; EQ-5D-3L = 0.215).

<figure id="Fig2">
<p><img src="11136_2026_4229_Fig2_HTML.jpg" id="d33e880" /></p>
<p><img src="11136_2026_4229_Fig2_HTML.gif" /></p>
<figcaption>Health state density curves for the EQ-5D-3L and MSIS-8D</figcaption>
</figure>

### Construct validity

Table <a href="#Tab3" data-ref-type="table">3</a> presents the results for discriminative and convergent validity. Both target measures significantly discriminated between groups based on levels of disability, fatigue, depression, anxiety, walking impairment and type of MS (*p* \< 0.0001). The EQ-5D-3L and MSIS-8D utility values showed strong correlations (rho \> 0.5) with the disability, fatigue, walking and depression measures, and moderate correlations with the anxiety measure (rho \> 0.4), with very high statistical significance (*p* \< 0.0001). While the EQ-5D-3L showed a slightly higher correlation with the disability measure and the walking scale, the MSIS-8D better correlated with the anxiety, depression and fatigue scales.

<div id="Tab3" class="table-wrap">

<div class="caption">

Discriminative and convergent validity of the EQ-5D-3L and MSIS-8D

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">EQ-5D-3L</th>
<th colspan="6" style="text-align: left;">Discriminative validity</th>
<th colspan="2" style="text-align: left;">Convergent validity</th>
</tr>
<tr>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">S.D</th>
<th style="text-align: left;">t-stat</th>
<th style="text-align: left;">df</th>
<th style="text-align: left;"><em>p</em> value*</th>
<th style="text-align: left;">Rho</th>
<th style="text-align: left;"><em>p</em> value*</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="9" style="text-align: left;">Fatigue</td>
</tr>
<tr>
<td style="text-align: left;">FSS &lt; 4</td>
<td style="text-align: left;">923</td>
<td style="text-align: center;">0.773</td>
<td style="text-align: center;">0.233</td>
<td style="text-align: center;">24.307</td>
<td style="text-align: left;">3665</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.553</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">FSS &gt;  = 4</td>
<td style="text-align: left;">2744</td>
<td style="text-align: center;">0.498</td>
<td style="text-align: center;">0.316</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Walking</td>
</tr>
<tr>
<td style="text-align: left;">MSWS &lt; 50</td>
<td style="text-align: left;">1548</td>
<td style="text-align: center;">0.764</td>
<td style="text-align: center;">0.214</td>
<td style="text-align: center;">31.474</td>
<td style="text-align: left;">2852</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.677</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">MSWS &gt;  = 50</td>
<td style="text-align: left;">1306</td>
<td style="text-align: center;">0.469</td>
<td style="text-align: center;">0.284</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Depression</td>
</tr>
<tr>
<td style="text-align: left;">HADS-D &lt; 11</td>
<td style="text-align: left;">2959</td>
<td style="text-align: center;">0.629</td>
<td style="text-align: center;">0.281</td>
<td style="text-align: center;">26.921</td>
<td style="text-align: left;">3623</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.586</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">HADS-D &gt;  = 11</td>
<td style="text-align: left;">666</td>
<td style="text-align: center;">0.290</td>
<td style="text-align: center;">0.345</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Anxiety</td>
</tr>
<tr>
<td style="text-align: left;">HADS-A &lt; 11</td>
<td style="text-align: left;">2811</td>
<td style="text-align: center;">0.621</td>
<td style="text-align: center;">0.293</td>
<td style="text-align: center;">19.947</td>
<td style="text-align: left;">3614</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.414</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">HADS-A &gt;  = 11</td>
<td style="text-align: left;">805</td>
<td style="text-align: center;">0.378</td>
<td style="text-align: center;">0.345</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Disability</td>
</tr>
<tr>
<td style="text-align: left;">webEDSS &lt; 5</td>
<td style="text-align: left;">1719</td>
<td style="text-align: center;">0.745</td>
<td style="text-align: center;">0.221</td>
<td style="text-align: center;">37.490</td>
<td style="text-align: left;">3617</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.704</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">webEDSS &gt;  = 5</td>
<td style="text-align: left;">1900</td>
<td style="text-align: center;">0.406</td>
<td style="text-align: center;">0.311</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;">MS type</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">F-stat</th>
<th style="text-align: left;"><em>p</em> value*</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">RRMS</td>
<td style="text-align: left;">1862</td>
<td style="text-align: center;">0.674</td>
<td style="text-align: center;">0.277</td>
<td rowspan="4" style="text-align: left;">204.100</td>
<td rowspan="4" style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">SPMS</td>
<td style="text-align: left;">1110</td>
<td style="text-align: center;">0.414</td>
<td style="text-align: center;">0.324</td>
</tr>
<tr>
<td style="text-align: left;">PPMS</td>
<td style="text-align: left;">491</td>
<td style="text-align: center;">0.483</td>
<td style="text-align: center;">0.308</td>
</tr>
<tr>
<td style="text-align: left;">Benign</td>
<td style="text-align: left;">76</td>
<td style="text-align: center;">0.773</td>
<td style="text-align: center;">0.281</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">MSIS-8D</th>
<th colspan="6" style="text-align: left;">Discriminative validity</th>
<th colspan="2" style="text-align: left;">Convergent validity</th>
</tr>
<tr>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">S.D</th>
<th style="text-align: left;">t-stat</th>
<th style="text-align: left;">df</th>
<th style="text-align: left;"><em>p</em> value*</th>
<th style="text-align: left;">Rho</th>
<th style="text-align: left;"><em>p</em> value*</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="9" style="text-align: left;">Fatigue</td>
</tr>
<tr>
<td style="text-align: left;">FSS &lt; 4</td>
<td style="text-align: left;">923</td>
<td style="text-align: center;">0.771</td>
<td style="text-align: center;">0.114</td>
<td style="text-align: center;">30.996</td>
<td style="text-align: left;">3665</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.651</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">FSS &gt;  = 4</td>
<td style="text-align: left;">2744</td>
<td style="text-align: center;">0.577</td>
<td style="text-align: center;">0.178</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Walking</td>
</tr>
<tr>
<td style="text-align: left;">MSWS &lt; 50</td>
<td style="text-align: left;">1548</td>
<td style="text-align: center;">0.741</td>
<td style="text-align: center;">0.129</td>
<td style="text-align: center;">33.316</td>
<td style="text-align: left;">2852</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.669</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">MSWS &gt;  = 50</td>
<td style="text-align: left;">1306</td>
<td style="text-align: center;">0.553</td>
<td style="text-align: center;">0.172</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Depression</td>
</tr>
<tr>
<td style="text-align: left;">HADS-D &lt; 11</td>
<td style="text-align: left;">2959</td>
<td style="text-align: center;">0.668</td>
<td style="text-align: center;">0.158</td>
<td style="text-align: center;">32.797</td>
<td style="text-align: left;">3623</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.668</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">HADS-D &gt;  = 11</td>
<td style="text-align: left;">666</td>
<td style="text-align: center;">0.440</td>
<td style="text-align: center;">0.182</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Anxiety</td>
</tr>
<tr>
<td style="text-align: left;">HADS-A &lt; 11</td>
<td style="text-align: left;">2811</td>
<td style="text-align: center;">0.666</td>
<td style="text-align: center;">0.161</td>
<td style="text-align: center;">26.224</td>
<td style="text-align: left;">3614</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.493</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">HADS-A &gt;  = 11</td>
<td style="text-align: left;">805</td>
<td style="text-align: center;">0.488</td>
<td style="text-align: center;">0.196</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Disability</td>
</tr>
<tr>
<td style="text-align: left;">webEDSS &lt; 5</td>
<td style="text-align: left;">1719</td>
<td style="text-align: center;">0.724</td>
<td style="text-align: center;">0.141</td>
<td style="text-align: center;">34.985</td>
<td style="text-align: left;">3617</td>
<td style="text-align: center;"> &lt; 0.0001</td>
<td style="text-align: left;"> − 0.634</td>
<td style="text-align: center;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">webEDSS &gt;  = 5</td>
<td style="text-align: left;">1900</td>
<td style="text-align: center;">0.538</td>
<td style="text-align: center;">0.175</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;">MS type</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">F-stat</th>
<th style="text-align: left;"><em>p</em> value*</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">RRMS</td>
<td style="text-align: left;">1862</td>
<td style="text-align: center;">0.684</td>
<td style="text-align: center;">0.168</td>
<td rowspan="4" style="text-align: left;">184.250</td>
<td rowspan="4" style="text-align: left;"> &lt; 0.0001</td>
</tr>
<tr>
<td style="text-align: left;">SPMS</td>
<td style="text-align: left;">1110</td>
<td style="text-align: center;">0.542</td>
<td style="text-align: center;">0.177</td>
</tr>
<tr>
<td style="text-align: left;">PPMS</td>
<td style="text-align: left;">491</td>
<td style="text-align: center;">0.581</td>
<td style="text-align: center;">0.173</td>
</tr>
<tr>
<td style="text-align: left;">Benign</td>
<td style="text-align: left;">76</td>
<td style="text-align: center;">0.752</td>
<td style="text-align: center;">0.148</td>
</tr>
</tbody>
</table>

S.D.: standard deviation; df: degrees of freedom; RRMS: relapsing-remitting MS; SPMS: secondary progressive MS; PPMS: primary progressive MS

\*Bonferroni correction gives adjusted significance level of *p* \< 0.000962

</div>

### Responsiveness

The characteristics of the UKMSR members included in each of the four analyses (EQ-5D-3L and MSIS-8D responsiveness to symptom onset and relapse) are summarised in Table <a href="#Tab4" data-ref-type="table">4</a>.

<div id="Tab4" class="table-wrap">

<div class="caption">

Descriptive statistics for longitudinal analysis samples

</div>

<table>
<thead>
<tr>
<th colspan="6" style="text-align: left;">EQ-5D-3L analysis</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Relapses</th>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Symptom onset</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Percent</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Percent</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">Included in analysis</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Observations</td>
<td style="text-align: left;">156</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">97</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">142</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">93</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Gender</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">125</td>
<td style="text-align: center;">80.13</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">71</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Male/not reported</td>
<td style="text-align: left;">31</td>
<td style="text-align: center;">19.87</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">26</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Ethnicity</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">White British</td>
<td style="text-align: left;">142</td>
<td style="text-align: center;">91.03</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">88</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Other/not stated</td>
<td style="text-align: left;">14</td>
<td style="text-align: center;">8.97</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">9</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Contemporary MS type<sup>a</sup></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">RRMS</td>
<td style="text-align: left;">125</td>
<td style="text-align: center;">80.13</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">56</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Other/not known</td>
<td style="text-align: left;">24</td>
<td style="text-align: center;">15.38</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">41</td>
<td style="text-align: center;">0.42</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

| Other variables         | Obs | Mean  | S.D   | Obs | Mean  | S.D   |
|-------------------------|-----|-------|-------|-----|-------|-------|
| Age (years)<sup>a</sup> | 156 | 52.37 | 12.47 | 97  | 54.74 | 10.47 |
| Web-EDSS<sup>b</sup>    | 85  | 4.79  | 1.83  | 61  | 5.39  | 1.64  |
| MSWS-12                 | 114 | 43.32 | 30.8  | 53  | 57.32 | 28.27 |
| FSS<sup>b</sup>         | 148 | 5.13  | 1.54  | 96  | 5.52  | 1.17  |
| HADS depression         | 151 | 7.88  | 5     | 97  | 8.62  | 4.36  |
| HADS anxiety            | 151 | 8.48  | 5.23  | 97  | 7.80  | 4.83  |
| EQ-5D-3L value          | 156 | 0.507 | 0.34  | 97  | 0.444 | 0.318 |
| MSIS-8D value           | 152 | 0.573 | 0.21  | 97  | 0.532 | 0.192 |

<table>
<thead>
<tr>
<th colspan="6" style="text-align: left;">MSIS-8D analysis</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Relapses</th>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Symptom onset</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Percent</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Percent</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">Included in analysis</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Observations</td>
<td style="text-align: left;">152</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">95</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">138</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">92</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Gender</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">125</td>
<td style="text-align: center;">82.24</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">72</td>
<td style="text-align: center;">0.76</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Male/not reported</td>
<td style="text-align: left;">27</td>
<td style="text-align: center;">17.76</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">23</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Ethnicity</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">White British</td>
<td style="text-align: left;">139</td>
<td style="text-align: center;">91.45</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">85</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Other/not stated</td>
<td style="text-align: left;">13</td>
<td style="text-align: center;">8.55</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">10</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Contemporary MS type<sup>a</sup></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">RRMS</td>
<td style="text-align: left;">120</td>
<td style="text-align: center;">78.95</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">53</td>
<td style="text-align: center;">0.56</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Other/not known</td>
<td style="text-align: left;">26</td>
<td style="text-align: center;">17.11</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">42</td>
<td style="text-align: center;">0.44</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

| Other variables         | Obs | Mean  | S.D   | Obs | Mean  | S.D   |
|-------------------------|-----|-------|-------|-----|-------|-------|
| Age (years)<sup>a</sup> | 152 | 52.33 | 12.3  | 95  | 54.78 | 10.17 |
| Web-EDSSb               | 86  | 4.83  | 1.86  | 60  | 5.56  | 1.56  |
| MSWS-12                 | 108 | 43.63 | 30.69 | 49  | 58.94 | 27.50 |
| FSS<sup>b</sup>         | 144 | 5.22  | 1.55  | 93  | 5.58  | 1.15  |
| HADS depression         | 148 | 7.91  | 4.86  | 94  | 8.69  | 4.19  |
| HADS anxiety            | 148 | 8.39  | 5.17  | 94  | 7.84  | 4.76  |
| EQ-5D-3L value          | 147 | 0.493 | 0.35  | 93  | 0.441 | 0.306 |
| MSIS-8D value           | 152 | 0.567 | 0.21  | 95  | 0.536 | 0.183 |

Obs: observations; S.D.: standard deviation; RRMS: relapsing-remitting MS

<sup>a</sup>MS Type and Age are contemporary with each data collection window

<sup>b</sup>The webEDSS and FSS were introduced by the UKMSR in 2017, resulting in a lower number of observations for these compared to the other measures

</div>

Table <a href="#Tab5" data-ref-type="table">5</a> shows the results of the responsiveness analyses for the EQ-5D-3L and MSIS-8D for each of the two events. When comparing utility values during relapse with those at an earlier time point at which no relapse was present, only the MSIS-8D produced a significant or non-negligible change (i.e., *p* \< 0.001; SES \> 0.2). The SRM for the MSIS-8D was also significantly higher than the EQ-5D-3L at a 95% confidence level. Neither instrument met the threshold for a significant or non-negligible change in response to the onset of two or more symptoms, although the SRM for the MSIS-8D was significantly higher than for the EQ-5D-3L. No statistically significant changes were observed in the individual dimensions of the EQ-5D-3L or MSIS-8D in response to either relapse or symptom onset.

<div id="Tab5" class="table-wrap">

<div class="caption">

Responsiveness results

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="7" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">SRM</th>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">Direction of change</th>
<th colspan="2" style="text-align: left;"><em>p</em> values</th>
</tr>
<tr>
<th style="text-align: left;">Obs</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">t-stat</th>
<th style="text-align: left;">df</th>
<th style="text-align: left;"><em>p</em> val</th>
<th style="text-align: left;">SES</th>
<th style="text-align: left;">SRM</th>
<th style="text-align: left;">LCL</th>
<th style="text-align: left;">UCL</th>
<th style="text-align: left;"> + ve</th>
<th style="text-align: left;"> − ve</th>
<th style="text-align: left;">None</th>
<th style="text-align: left;">z-stat</th>
<th style="text-align: left;">Actual</th>
<th style="text-align: left;">Exact</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="18" style="text-align: left;">Current relapse</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">EQ-5D-3L</td>
<td colspan="7" style="text-align: left;">Dimension</td>
</tr>
<tr>
<td style="text-align: left;">Change score</td>
<td style="text-align: left;">156</td>
<td style="text-align: left;"> − 0.047</td>
<td style="text-align: center;">0.208</td>
<td style="text-align: center;">2.821</td>
<td style="text-align: left;">155</td>
<td style="text-align: center;">0.0054</td>
<td style="text-align: left;"> − 0.139</td>
<td style="text-align: left;"> − 0.226</td>
<td style="text-align: left;"> − 0.259</td>
<td style="text-align: left;"> − 0.193</td>
<td style="text-align: left;">MB</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;"> 136</td>
<td style="text-align: center;">−2.236</td>
<td style="text-align: center;">0.253</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Pre-relapse</td>
<td style="text-align: left;">156</td>
<td style="text-align: left;">0.554</td>
<td style="text-align: center;">0.338</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">SC</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;">139</td>
<td style="text-align: center;"> − 0.243</td>
<td style="text-align: center;">0.8084</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Relapse</td>
<td style="text-align: left;">156</td>
<td style="text-align: left;">0.507</td>
<td style="text-align: center;">0.342</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">UA</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">122</td>
<td style="text-align: center;"> − 1.362</td>
<td style="text-align: center;">0.1733</td>
<td style="text-align: center;">0.2145</td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">142</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">PD</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">123</td>
<td style="text-align: center;"> − 2.263</td>
<td style="text-align: center;">0.0236</td>
<td style="text-align: center;">0.0351</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">116</td>
<td style="text-align: center;"> − 1.581</td>
<td style="text-align: center;">0.1138</td>
<td style="text-align: center;">0.1539</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">MSIS-8D</td>
<td colspan="7" style="text-align: left;">Dimension</td>
</tr>
<tr>
<td style="text-align: left;">Change score</td>
<td style="text-align: left;">152</td>
<td style="text-align: left;"> − 0.047</td>
<td style="text-align: center;">0.142</td>
<td style="text-align: center;">4.067</td>
<td style="text-align: left;">151</td>
<td style="text-align: center;">0.0001*</td>
<td style="text-align: left;"> − 0.228</td>
<td style="text-align: left;"> − 0.330</td>
<td style="text-align: left;"> − 0.352</td>
<td style="text-align: left;"> − 0.307</td>
<td style="text-align: left;">Phys</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">84</td>
<td style="text-align: center;"> − 2.723</td>
<td style="text-align: center;">0.0065</td>
<td style="text-align: center;">0.0067</td>
</tr>
<tr>
<td style="text-align: left;">Pre-relapse</td>
<td style="text-align: left;">152</td>
<td style="text-align: left;">0.614</td>
<td style="text-align: center;">0.205</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Soc</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">71</td>
<td style="text-align: center;"> − 0.911</td>
<td style="text-align: center;">0.3622</td>
<td style="text-align: center;">0.3707</td>
</tr>
<tr>
<td style="text-align: left;">Relapse</td>
<td style="text-align: left;">152</td>
<td style="text-align: left;">0.567</td>
<td style="text-align: center;">0.214</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Mob</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">80</td>
<td style="text-align: center;"> − 2.636</td>
<td style="text-align: center;">0.0084</td>
<td style="text-align: center;">0.0080</td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">138</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">DA</td>
<td style="text-align: left;">26</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">78</td>
<td style="text-align: center;"> − 2.780</td>
<td style="text-align: center;">0.0054</td>
<td style="text-align: center;">0.0049</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Fat</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">37</td>
<td style="text-align: left;">96</td>
<td style="text-align: center;"> − 2.381</td>
<td style="text-align: center;">0.0173</td>
<td style="text-align: center;">0.0192</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Emo</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">82</td>
<td style="text-align: center;"> − 2.829</td>
<td style="text-align: center;">0.0047</td>
<td style="text-align: center;">0.0049</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cog</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">89</td>
<td style="text-align: center;"> − 1.994</td>
<td style="text-align: center;">0.0462</td>
<td style="text-align: center;">0.0469</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Dep</td>
<td style="text-align: left;">26</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">83</td>
<td style="text-align: center;"> − 2.049</td>
<td style="text-align: center;">0.0405</td>
<td style="text-align: center;">0.0415</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;">Onset of two or more new symptoms</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">EQ-5D-3L</td>
<td colspan="7" style="text-align: left;">Dimension</td>
</tr>
<tr>
<td style="text-align: left;">Change score</td>
<td style="text-align: left;">97</td>
<td style="text-align: left;"> − 0.022</td>
<td style="text-align: center;">0.232</td>
<td style="text-align: center;">0.9307</td>
<td style="text-align: left;">96</td>
<td style="text-align: center;">0.3544</td>
<td style="text-align: left;"> − 0.069</td>
<td style="text-align: left;"> − 0.094</td>
<td style="text-align: left;"> − 0.141</td>
<td style="text-align: left;"> − 0.048</td>
<td style="text-align: left;">MB</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;"> 80</td>
<td style="text-align: center;">−1.698</td>
<td style="text-align: center;">0.0896</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Pre-onset</td>
<td style="text-align: left;">97</td>
<td style="text-align: left;">0.466</td>
<td style="text-align: center;">0.318</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">SC</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;">&lt;10</td>
<td style="text-align: left;"> 81</td>
<td style="text-align: center;">−1.500</td>
<td style="text-align: center;">0.1336</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Post-onset</td>
<td style="text-align: left;">97</td>
<td style="text-align: left;">0.444</td>
<td style="text-align: center;">0.318</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">UA</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">70</td>
<td style="text-align: center;">0.160</td>
<td style="text-align: center;">0.8726</td>
<td style="text-align: center;">1.0000</td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">93</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">PD</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">68</td>
<td style="text-align: center;"> − 1.671</td>
<td style="text-align: center;">0.0947</td>
<td style="text-align: center;">0.1360</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">69</td>
<td style="text-align: center;"> − 0.783</td>
<td style="text-align: center;">0.4338</td>
<td style="text-align: center;">0.4744</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">MSIS-8D</td>
<td colspan="7" style="text-align: left;">Dimension</td>
</tr>
<tr>
<td style="text-align: left;">Change score</td>
<td style="text-align: left;">95</td>
<td style="text-align: left;"> − 0.034</td>
<td style="text-align: center;">0.161</td>
<td style="text-align: center;">2.0653</td>
<td style="text-align: left;">94</td>
<td style="text-align: center;">0.0416</td>
<td style="text-align: left;"> − 0.190</td>
<td style="text-align: left;"> − 0.212</td>
<td style="text-align: left;"> − 0.244</td>
<td style="text-align: left;"> − 0.179</td>
<td style="text-align: left;">Phys</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">27</td>
<td style="text-align: left;">57</td>
<td style="text-align: center;"> − 2.734</td>
<td style="text-align: center;">0.0063</td>
<td style="text-align: center;">0.0059</td>
</tr>
<tr>
<td style="text-align: left;">Pre-onset</td>
<td style="text-align: left;">95</td>
<td style="text-align: left;">0.570</td>
<td style="text-align: center;">0.180</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Soc</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">33</td>
<td style="text-align: left;">38</td>
<td style="text-align: center;"> − 1.246</td>
<td style="text-align: center;">0.2128</td>
<td style="text-align: center;">0.2291</td>
</tr>
<tr>
<td style="text-align: left;">Post-onset</td>
<td style="text-align: left;">95</td>
<td style="text-align: left;">0.536</td>
<td style="text-align: center;">0.183</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Mob</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">29</td>
<td style="text-align: left;">41</td>
<td style="text-align: center;"> − 0.495</td>
<td style="text-align: center;">0.6204</td>
<td style="text-align: center;">0.6270</td>
</tr>
<tr>
<td style="text-align: left;">Participants</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">DA</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">35</td>
<td style="text-align: left;">40</td>
<td style="text-align: center;"> − 2.097</td>
<td style="text-align: center;">0.0360</td>
<td style="text-align: center;">0.0377</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Fat</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">32</td>
<td style="text-align: left;">45</td>
<td style="text-align: center;"> − 2.089</td>
<td style="text-align: center;">0.0367</td>
<td style="text-align: center;">0.0384</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Emo</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">27</td>
<td style="text-align: left;">45</td>
<td style="text-align: center;"> − 0.467</td>
<td style="text-align: center;">0.6404</td>
<td style="text-align: center;">0.6601</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cog</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">49</td>
<td style="text-align: center;"> − 2.122</td>
<td style="text-align: center;">0.0338</td>
<td style="text-align: center;">0.0368</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Dep</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">50</td>
<td style="text-align: center;"> − 0.628</td>
<td style="text-align: center;">0.5303</td>
<td style="text-align: center;">0.5242</td>
</tr>
</tbody>
</table>

Key: Statistical terms (from left to right): Obs: Observations, SD: standard deviation, df: degrees of freedom, *p*-val: *p* value, SES: standardised effect size, SRM: standardised response mean, LCL: lower confidence limit, UCL: upper confidence limit, + ve: positive (improvement), − ve: negative (deterioration), \*significant after Bonferroni correction (*p* \< 0.000962), Cell counts \< 10 suppressed. EQ-5D-5L dimensions: MB: Mobility, SC: Self-care, UA: Usual activities, PD: Pain/discomfort, AD: Anxiety/depression

</div>

## Discussion

This study provides, for the first time, an assessment of the acceptability, validity and responsiveness of the MSIS-8D, compared to the EQ-5D-3L. This evidence, based on a large, representative dataset, provides essential information to address the current lack of knowledge regarding the validity and responsiveness of these measures in people with MS. The use of a range of analysis methods, exploring the descriptive systems of the measures as well as utility values, allows interpretations and potential explanations to be drawn from across the results.

### Cross-sectional analyses

The higher rate of missing data for the MSIS-8D (8.57%) compared to the EQ-5D-3L (3.14%) suggests that the EQ-5D-3L is more acceptable to respondents with MS. This may be due to the longer length of the MSIS-29 questionnaire, from which MSIS-8D values are derived, with 29 items compared to the EQ-5D-3L’s five.

The EQ-5D-3L exhibited a high concentration of relatively few health states. The most commonly reported EQ-5D-3L health state was 22222, which might suggest the need for greater discrimination between the extremes of ‘no problems’ and ‘severe problems’—an issue that has been addressed with the introduction of the EQ-5D-5L \[41\]. This is supported by the high ceiling effect that was observed for the EQ-5D-3L, indicating a lack of sensitivity at higher levels of HRQoL. The results from the HSDCs and HSDIs indicate that participants are more evenly distributed across MSIS-8D health states than across EQ-5D-3L health states, suggesting that the MSIS-8D is better able to differentiate between participants \[33\]. This is likely due to the higher number of unique health states described by the MSIS-8D classification system (65,536) compared to the EQ-5D-3L (243), as well as its condition-specific content.

Responses across the levels of each dimension were more evenly distributed for the MSIS-8D than they were for the EQ-5D-3L. Proportions of responses at the ‘extremely’ level of the MSIS-8D *Emotion*, *Cognition* and *Depression* dimensions were relatively low, however, with more than 40% of responses at Level 2 (‘a little*’*) for *Emotion* and *Cognition* and at Level 1 (‘not at all*’*) for *Depression*. This may indicate that the definitions of these dimension levels are limited in their ability to distinguish between degrees of functioning or symptom severity that are important to people with MS. However, the more even distribution of responses for the MSIS-8D overall may, in part, explain its greater responsiveness compared to the EQ-5D-3L.

Both measures exhibited excellent discriminative validity, with statistically significant differences concerning MS type, and levels of disability, walking impairment, fatigue, depression and anxiety. This supports the ability of the EQ-5D-3L and MSIS-8D to distinguish between groups known to differ in terms of HRQoL. In terms of convergent validity, both the EQ-5D-3L and MSIS-8D correlated strongly with measures of disability, fatigue, walking impairment and depression, and moderately with anxiety. The EQ-5D-3L correlated most strongly with measures related to walking; in addition to the MSWS-12, the webEDSS is also primarily focused on ambulatory function \[25\]. This may be because the mobility item of the EQ-5D-3L focuses specifically on ‘walking’, whereas the MSIS-8D mobility item does not. The MSIS-8D correlated more strongly with anxiety, depression and fatigue. These findings may be informative when selecting outcome measures to evaluate interventions targeting specific MS symptoms.

### Responsiveness analysis

Changes in EQ-5D-3L and MSIS-8D utility values were assessed in relation to relapse and the onset of two or more symptoms. The only statistically significant and/or non-negligible change was for the MSIS-8D in response to relapse, however the SES was small (−0.228). Given the results of other studies, which have found that relapses \[29, 30\] and individual MS symptoms \[31\] have a considerable impact on HRQoL, these findings may suggest a lack of responsiveness for both instruments. This may be unsurprising for the EQ-5D-3L, given the concerns previously raised about its sensitivity to the effects of MS treatment. These concerns primarily relate to content and construct validity, particularly the omission of HRQoL domains important to people with MS, such as fatigue and cognitive problems \[10\], as well as ceiling effects and limited convergent validity \[7\]. This is only partially supported by the current analysis, which identified high ceiling effects for the EQ-5D-3L but excellent convergent validity for both target measures. Furthermore, despite its low ceiling effect and inclusion of fatigue and cognition dimensions, the MSIS-8D also exhibited limitations in responsiveness, although the SRMs for the MSIS-8D were higher than those for the EQ-5D-3L in both analyses.

The MSIS-8D descriptive system was designed to be more sensitive to changes in MS-specific HRQoL, with dimensions selected to represent aspects of HRQoL of most relevance to people with MS \[11\]. This is reflected in the greater content validity exhibited by the MSIS-8D compared to the EQ-5D-3L, as well as its greater responsiveness when assessed using standardised measures (SES and SRM). When using a preference-based measure in economic evaluation, however, it is the magnitude of change in mean values that is relevant. In the current analysis, the mean change in relation to relapse was identical for both instruments (EQ-5D-3L = −0.047, MSIS-8D = −0.047), whereas there was a marked difference in relation to symptom onset (EQ-5D-3L = −0.022, MSIS-8D = −0.034). The former may be due to the narrower potential value range of the MSIS-8D (0.079–0.882) compared to the EQ-5D-3L (− 0.594–1.000) restricting the potential size of changes in values \[36\]. Hence any advantages in responsiveness gained from the MSIS-8D’s condition-specific descriptive system may be off-set by its narrower range of utility values.

### Limitations of the study

During the time period covered by these analyses, the UKMSR administered the EQ-5D-*3L*, introducing the EQ-5D-*5L* in Autumn 2023. The EQ-5D-5L retains the same five dimensions as the EQ-5D-3L, with the number of response options per dimension increased from three to five. This increases the potential sensitivity of the descriptive system to more subtle changes in each dimension, which could improve responsiveness and reduce ceiling effects \[41\]. Findings from previous studies that directly compared the EQ-5D-3L and EQ-5D-5L support the improved sensitivity of the EQ-5D-5L \[42–45\]. Clearly, the results of this study will not reflect any such improvement. The extent to which the shift from three to five levels for the same dimensions will increase sensitivity to change in MS, where the relevance of the EQ-5D dimensions themselves has been the main point of contention \[10\], remains to be seen.

The use of pre-existing datasets in research is increasing due to a number of advantages, including increased efficiency and reduced participant burden. The disadvantage of this approach, however, is that the available data were not designed to address the given research question \[46\]. In the current study, while the UKMSR data proved highly suitable for the cross-sectional analyses, the assessment of responsiveness was more challenging. This was partly due to the need to identify a specific event, occurring at a known point in time, that could be expected to have a detectable, positive or negative, effect on HRQoL. Such clear-cut events were difficult to identify in the UKMSR data, limiting the analyses that could be performed. The recorded timing of events relied on participant self-report, potentially introducing measurement error and temporal misclassification, and the length of time between the reported date of events and a preceding or subsequent utility value was determined by the UKMSR’s fixed three or 6 monthly data collection points, preventing exploration of shorter-term effects. Further to this, previous analysis of UKMSR data shows that responses to PROMs peak at 5–10 years post-diagnosis, reducing monotonically over time thereafter, potentially resulting in under-representation of people with more advanced MS \[47\]. The dataset provided by the UKMSR included only participants who provided EQ-5D-3L responses for at least five timepoints, including complete EQ-5D-3L responses at Spring 2023, thereby reducing the overall number of participants included in the analyses. This may have resulted in under-representation of particular groups, potentially introducing survivorship and selection bias. The two events (relapse, symptom onset) were each considered in isolation; the responsiveness analyses do not control for other events occurring during the relevant time frame that might have influenced HRQoL. For these reasons, the results of the responsiveness analyses reported here should be interpreted with some caution.

## Conclusions

The MSIS-8D demonstrated superior content validity and distributional properties to the EQ-5D-3L, while the EQ-5D-3L showed greater acceptability in this sample of people with MS living in the UK. Both measures exhibited good construct validity. However, neither measure was responsive to the onset of new symptoms, and only the MSIS-8D met all criteria for responsiveness when people moved from a non-relapse to a relapse state. These findings support earlier concerns regarding the sensitivity of the EQ-5D to important changes in the lives of people with MS, and suggest that similar issues may affect the MSIS-8D, albeit to a lesser extent. The responsiveness results, however, should be interpreted with some caution due to a number of limitations that affected the analysis, several of which arose due to the use of existing data. Future studies could usefully explore how best use can be made of valuable data resources such as the UKMSR in longitudinal research, potentially alongside the prospective collection of bespoke data. Further research is also needed to assess the distributional and psychometric properties of the EQ-5D-5L in this population.

## Acknowledgements

The research reported in this paper was funded by the EuroQol Research Foundation (EQ Project 1572-RA). This study makes use of anonymised data held by the UK Multiple Sclerosis Register funded by the MS Society (Award 147) and based on the UK Secure e-Research Platform. We would like to acknowledge all the data providers who make anonymised data available for research.

### Appendix

Sec Fig. <a href="#Fig3" data-ref-type="fig">3</a>.

<figure id="Fig3">
<p><img src="11136_2026_4229_Fig3_HTML.jpg" id="d33e3170" /></p>
<p><img src="11136_2026_4229_Fig3_HTML.gif" /></p>
<figcaption>Descriptive system for the MSIS-8D</figcaption>
</figure>

## Author contributions

All authors contributed to the study conception and design, and to the identification of variables for inclusion in analysis. The data export was obtained by R.M., and data analysis was undertaken by E.G. and B.M. The first draft of the manuscript was written by E.G. and all authors commented on previous versions of the manuscript. All authors read and approved the final manuscript.

## Funding

This work was supported by the EuroQol Research Foundation (EQ Project 1572-RA).

## Data availability

The datasets used in this study are stored in the UK MS Register Secure e-Research platform. These data can be accessed by suitably qualified researchers following governance review. Details of how to apply for the data can be found here: \[<https://ukmsregister.org/Research/WorkingWithUs>\] (https:/ukmsregister.org/Research/WorkingWithUs).

## Declarations

### Competing interests

Financial interests: Elizabeth Goodwin, Rod Middleton and Annie Hawton declare they have no financial interests. Bernhard Michalowsky is a member of the EuroQol Group and has received payment for reviews and board hours. Non-financial interests: Elizabeth Goodwin led the development of the MSIS-8D.

### Ethical approval

This study was performed in line with the principles of the Declaration of Helsinki. Ethical approval for the UKMSR has been granted by the South West Central Bristol Research Ethics Council under registration code initially as 16/SW/0164 now as 21/SW/0085. This ethical approval covers all studies that use data collected by the UKMSR.

### Consent to participate

All individual members of the UK MS Register provide informed consent for their anonymised data to be used in research studies such as this by signing up to the Participant Terms and Conditions: <https://ukmsregister.org/Account/Register>

## Footnotes

## References

## References

1. Brownlee, W. J., Hardy, T. A., Fazekas, F., & Miller, D. H. (2017). Diagnosis of multiple sclerosis: Progress and challenges. Lancet,389(10076), 1336–1346. 10.1016/S0140-6736(16)30959-X

2. Zajicek, J., Freeman, J., & Porter, B. (2007). Multiple sclerosis care: A Practical manual. Oxford: Oxford University Press.

3. Hemmett, L., Holmes, J., Barnes, M., & Russell, N. (2004). What drives quality of life in multiple sclerosis? QJM,97(10), 671–676. 10.1093/qjmed/hch105

4. Nortvedt, M. W., & Riise, T. (2003). The use of quality of life measures in multiple sclerosis research. Multiple Sclerosis,9(1), 63–72. 10.1191/1352458503ms871oa

5. NICE. (2024). Developing NICE guidelines: the manual (PMG20). NICE process and methods. London: National Institute for Health and Care Excellence.

6. Hawton, A., Goodwin, E., Boddy, K., Freeman, J., Thomas, S., Chataway, J., & Green, C. (2022). Measuring the cost-effectiveness of treatments for people with multiple sclerosis: Beyond quality-adjusted life-years. Multiple Sclerosis,28(3), 346–351. 10.1177/1352458520954172

7. Fisk, J. D., Brown, M. G., Sketris, I. S., Metz, L. M., Murray, T. J., & Stadnyk, K. L. (2005). A comparison of health utility measures for the evaluation of multiple sclerosis treatments. Journal of Neurology, Neurosurgery & Psychiatry,76(1), 58–63. 10.1136/jnnp.2003.017897

8. Fogarty, E., Walsh, C., Adams, R., McGuigan, C., Barry, M., & Tubridy, N. (2013). Relating health-related quality of life to disability progression in multiple sclerosis, using the 5-level EQ-5D. Multiple Sclerosis,19(9), 1190–1196. 10.1177/1352458512474860

9. Kohn, C. G., Sidovar, M. F., Kaur, K., Zhu, Y., & Coleman, C. I. (2014). Estimating a minimal clinically important difference for the EuroQol 5-Dimension health status index in persons with multiple sclerosis. Health and Quality of Life Outcomes,12, 66. 10.1186/1477-7525-12-66

10. Kuspinar, A., & Mayo, N. E. (2014). A review of the psychometric properties of generic utility measures in multiple sclerosis. PharmacoEconomics,32(8), 759–773. 10.1007/s40273-014-0167-5

11. NICE. (2022). NICE technology appraisal and highly specialised technologies guidance: The manual (PMG36) NICE process and methods. London: National Institute for Health and Care Excellence.

12. Rowen, D., Brazier, J., Ara, R., et al. (2017). The role of condition-specific preference-based measures in health technology assessment. PharmacoEconomics,35(Suppl 1), 33–41. 10.1007/s40273-017-0546-9

13. Brazier, J., & Tsuchiya, A. (2010). Preference-based condition-specific measures of health: What happens to cross programme comparability? Health Economics,19(2), 125–129. 10.1002/hec.1580

14. Goodwin, E., & Green, C. (2015). A quality-adjusted life-year measure for multiple sclerosis: Developing a patient-reported health state classification system for a multiple sclerosis-specific preference-based measure. Value in Health,18(8), 1016–1024. 10.1016/j.jval.2015.07.002

15. Goodwin, E., Green, C., & Spencer, A. (2015). Estimating a preference-based index for an eight-dimensional health state classification system for multiple sclerosis. Value Health,18(8), 1025–1036. 10.1016/j.jval.2015.10.004

16. Freeman, J., Hendrie, W., Jarrett, L., Hawton, A., Barton, A., Dennett, R., Jones, B., Zajicek, J., & Creanor, S. (2019). Assessment of a home-based standing frame programme in people with progressive multiple sclerosis (SUMS): A pragmatic, multi-centre, randomised, controlled trial and cost-effectiveness analysis. Lancet Neurology,18(8), 736–747. 10.1016/S1474-4422(19)30190-5

17. Gunn, H., Stevens, K. N., Creanor, S., Andrade, J., Paul, L., Miller, L., Green, C., Ewings, P., Barton, A., Berrow, M., Vickery, J., Marshall, B., Zajicek, J., & Freeman, J. A. (2021). Balance Right In Multiple Sclerosis (BRiMS): A feasibility randomised controlled trial of a falls prevention programme. Pilot and Feasibility Studies,7(1), Article 2. 10.1186/s40814-020-00732-9

18. Lincoln, N. B., Bradshaw, L. E., Constantinescu, C. S., Day, F., Drummond, A. E., Fitzsimmons, D., Harris, S., Montgomery, A. A., & das Nair, R. (2020). Group cognitive rehabilitation to reduce the psychological impact of multiple sclerosis on quality of life: The CRAMMS RCT. Health Technology Assessment,24(4), 1–182. 10.3310/hta24040

19. Marsden, J., Dennett, R., Gibbon, A., Knight Lozano, R., Freeman, J. A., Bamiou, D. E., Harris, C., Hawton, A., Goodwin, E., Creanor, S., Sorrell, L., Hoskings, J., & Pavlou, M. (2025). Vestibular rehabilitation in Multiple Sclerosis: Randomized controlled trial and cost-effectiveness analysis comparing customized with booklet based vestibular rehabilitation for vestibulopathy. Neurorehabilitation and Neural Repair,39(9), 687–700. 10.1177/15459683251345444

20. Gagnier, J. J., de Arruda, G. T., Terwee, C. B., & Mokkink, L. B. (2025). COSMIN reporting guideline for studies on measurement properties of patient‑reported outcome measures: Version 2.0. Quality of Life Research,34, 1901–1911. 10.1007/s11136-025-03950-x

21. Ford, D. V., Jones, K. H., Middleton, R. M., Lockhart-Jones, H., Maramba, I. D., Noble, G. J., Osborne, L. A., & Lyons, R. A. (2012). The feasibility of collecting information from people with multiple sclerosis for the UK MS register via a web portal: Characterising a cohort of people with MS. BMC Medical Informatics and Decision Making,12, 73. 10.1186/1472-6947-12-73

22. Nicholas, R., Tallantyre, E. C., Witts, J., Marrie, R. A., Craig, E. M., Knowles, S., Pearson, O. R., Harding, K., Kreft, K., Hawken, J., Ingram, G., Morgan, B., Middleton, R. M., Robertson, N., Research Group, U.R. (2024). Algorithmic approach to finding people with multiple sclerosis using routine healthcare data in Wales. Journal of Neurology, Neurosurgery & Psychiatry,95(11), 1032–1035. 10.1136/jnnp-2024-333532

23. Middleton, R. M., Rodgers, W. J., Chataway, J., Schmierer, K., Rog, D., Galea, I., Akbari, A., Tuite-Dalton, K., Lockhart-Jones, H., Griffiths, D., Noble, D. G., Jones, K. H., Al-Din, A., Craner, M., Evangelou, N., Harman, P., Harrower, T., Hobart, J., Husseyin, H., … Ford, D. V. (2018). Validating the portal population of the United Kingdom multiple sclerosis register. Multiple Sclerosis and Related Disorders,24, 3–10. 10.1016/j.msard.2018.05.015

24. Dolan, P. (1997). Modeling valuations for EuroQol health states. Medical Care,35(11), 1095–1108. 10.1097/00005650-199711000-00002

25. Kurtzke, J. F. (1983). Rating neurologic impairment in multiple sclerosis: An expanded disability status scale (EDSS). Neurology,33(11), 1444–1452. 10.1212/wnl.33.11.1444

26. Krupp, L. B., LaRocca, N. G., Muir-Nash, J., & Steinberg, A. D. (1989). The fatigue severity scale. Application to patients with multiple sclerosis and systemic lupus erythematosus. Archives of Neurology,46(10), 1121–1123. 10.1001/archneur.1989.00520460115022

27. Hobart, J. C., Riazi, A., Lamping, D. L., Fitzpatrick, R., & Thompson, A. J. (2003). Measuring the impact of MS on walking ability: The 12-item MS walking scale (MSWS-12). Neurology,60(1), 31–36. 10.1212/wnl.60.1.31

28. Zigmond, A. S., & Snaith, R. P. (1983). The Hospital Anxiety and depression scale. Acta Psychiatrica Scandinavica,67(6), 361–370. 10.1111/j.1600-0447.1983.tb09716.x

29. Kalincik, T. (2015). Multiple sclerosis relapses: Epidemiology, outcomes and management. A systematic review. Neuroepidemiology,44(4), 199–214. 10.1159/000382130

30. Matza, L. S., Kim, K., Phillips, G., Zorn, K., Chan, K. S., Smith, K. C., & Mowry, E. M. (2019). Multiple sclerosis relapse: Qualitative findings from clinician and patient interviews. Multiple Sclerosis and Related Disorders,27, 139–146. 10.1016/j.msard.2018.09.029

31. Gil-Gonzalez, I., Martin-Rodriguez, A., Conrad, R., & Perez-San-Gregorio, M. A. (2020). Quality of life in adults with multiple sclerosis: A systematic review. British Medical Journal Open,10(11), e041249. 10.1136/bmjopen-2020-041249

32. Devlin, N., Parkin, D., & Janssen, B. (2020). Methods for analysing and reporting EQ-5D data. Springer.

33. Zamora, B., Parkin, D., Feng, Y., Bateman, M., Herdman, M., & Devlin, N. (2018). New methods for analysing the distribution of EQ-5D observations. In Research paper 18/03: Office of health economics.

34. Flachenecker, P., Kumpfel, T., Kallmann, B., Gottschalk, M., Grauer, O., Rieckmann, P., Trenkwalder, C., & Toyka, K. V. (2002). Fatigue in multiple sclerosis: A comparison of different rating scales and correlation to clinical parameters. Multiple Sclerosis,8(6), 523–526. 10.1191/1352458502ms839oa

35. Goldman, M. D., Ward, M. D., Motl, R. W., Jones, D. E., Pula, J. H., & Cadavid, D. (2017). Identification and validation of clinically meaningful benchmarks in the 12-Item multiple sclerosis walking scale. Multiple Sclerosis,23(10), 1405–1414. 10.1177/1352458516680749

36. Heather, A., Goodwin, E., Green, C., Morrish, N., Ukoumunne, O. C., Middleton, R. M., & Hawton, A. (2023). Multiple sclerosis health-related quality of life utility values from the UK MS register. Multiple Sclerosis Journal-Experimental, Translational and Clinical. 10.1177/20552173231178441

37. Hinkle, D. E., Wiersma, W., & Jurs, S. G. (2003). Applied statistics for the behavioral sciences. Houghton Mifflin.

38. Cohen, J. (1988). Statistical power analysis for behavioural sciences. Erlbaum.

39. Husted, J. A., Cook, R. J., Farewell, V. T., & Gladman, D. D. (2000). Methods for assessing responsiveness: A critical review and recommendations. Journal of Clinical Epidemiology,53(5), 459–468. 10.1016/s0895-4356(99)00206-1

40. Beaton, D. E., Hogg-Johnson, S., & Bombardier, C. (1997). Evaluating changes in health status: Reliability and responsiveness of five generic health status measures in workers with musculoskeletal disorders. Journal of Clinical Epidemiology,50(1), 79–93. 10.1016/s0895-4356(96)00296-x

41. Herdman, M., Gudex, C., Lloyd, A., Janssen, M., Kind, P., Parkin, D., Bonsel, G., & Badia, X. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research,20(10), 1727–1736. 10.1007/s11136-011-9903-x

42. Janssen, M. F., Bonsel, G. J., & Luo, N. (2018). Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. PharmacoEconomics,36(6), 675–697. 10.1007/s40273-018-0623-8

43. Thompson, A. J., & Turner, A. J. (2020). A comparison of the EQ-5D-3L and EQ-5D-5L. PharmacoEconomics,38(6), 575–591. 10.1007/s40273-020-00893-8

44. Jiang, R., Rand, K., Kuharic, M., & Pickard, A. S. (2022). EQ-5D-5L measurement properties are superior to EQ-5D-3L across the continuum of health using US value sets. Health and Quality of Life Outcomes,20(1), 134. 10.1186/s12955-022-02031-8

45. Marti-Pastor, M., Pont, A., Avila, M., Garin, O., Vilagut, G., Forero, C. G., Pardo, Y., Tresserras, R., Medina-Bustos, A., Garcia-Codina, O., Cabases, J., Rajmil, L., Alonso, J., & Ferrer, M. (2018). Head-to-head comparison between the EQ-5D-5L and the EQ-5D-3L in general population health surveys. Population Health Metrics,16(1), 14. 10.1186/s12963-018-0170-8

46. Doolan, D. M., Winters, J., & Nouredini, S. (2017). Answering research questions using an existing data set. Medical Research Archives,5(9), 1–14.

47. Lerede, A., Rodgers, J., Middleton, R. M., Hampshire, A., Nicholas, R., UK MS Register Research Group. (2023). Patient-reported outcomes in multiple sclerosis: A prospective registry cohort study. Brain Communications,5(4), fcad199. 10.1093/braincomms/fcad199

## Associated Data

### Data Availability Statement

The datasets used in this study are stored in the UK MS Register Secure e-Research platform. These data can be accessed by suitably qualified researchers following governance review. Details of how to apply for the data can be found here: \[<https://ukmsregister.org/Research/WorkingWithUs>\] (https:/ukmsregister.org/Research/WorkingWithUs).

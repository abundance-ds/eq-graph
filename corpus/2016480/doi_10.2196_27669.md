---
project_id: "2016480"
work_id: "doi:10.2196/27669"
doi: "10.2196/27669"
pmid: "34448726"
pmcid: "PMC8433865"
title: "Variations in Patients’ Overall Assessment of Their Health Across and Within Disease Groups Using the EQ-5D Questionnaire: Protocol for a Longitudinal Study in the Swedish National Quality Registers"
journal: "JMIR Research Protocols"
publication_date: "2021-08-27"
volume: "10"
issue: "8"
authors:
  - name: "Fitsum Sebsibe Teni"
    affiliation_ids:
      - "aff1"
  - name: "Ola Rolfson"
    affiliation_ids:
      - "aff1"
      - "aff2"
      - "aff3"
  - name: "Nancy Devlin"
    affiliation_ids:
      - "aff4"
      - "aff5"
  - name: "David Parkin"
    affiliation_ids:
      - "aff5"
      - "aff6"
  - name: "Emma Nauclér"
    affiliation_ids:
      - "aff3"
  - name: "Kristina Burström"
    affiliation_ids:
      - "aff1"
      - "aff7"
      - "aff8"
  - name: "The Swedish Quality Register (SWEQR) Study Group"
    affiliation_ids:
      - "aff9"
  - name: "Gunther Eysenbach"
  - name: "Kristiann Heesch"
  - name: "Thomas Poder"
affiliations:
  - id: "aff1"
    name: "Health Outcomes and Economic Evaluation Research Group, Stockholm Centre for Healthcare Ethics, Department of Learning, Informatics, Management and Ethics, Karolinska Institutet, Stockholm, Sweden"
  - id: "aff2"
    name: "Department of Orthopaedics, Institute of Clinical Sciences, Sahlgrenska Academy, University of Gothenburg, Gothenburg, Sweden"
  - id: "aff3"
    name: "Swedish Hip Arthroplasty Register, Gothenburg, Sweden"
  - id: "aff4"
    name: "Centre for Health Policy, University of Melbourne, Melbourne, Australia"
  - id: "aff5"
    name: "Office of Health Economics, London, United Kingdom"
  - id: "aff6"
    name: "City, University of London, London, United Kingdom"
  - id: "aff7"
    name: "Equity and Health Policy Research Group, Department of Global Public Health, Karolinska Institutet, Stockholm, Sweden"
  - id: "aff8"
    name: "Health Care Services, Region Stockholm, Stockholm, Sweden"
  - id: "aff9"
    name: "See Acknowledgments,"
licence: "cc-by"
source_file: "input/projects/2016480/papers/doi_10.2196_27669.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8433865/fullTextXML"
source_method: "epmc_xml"
source_sha256: "3bca14c08e195c1a14cbdb35eee45a1c081e177fa8f0bb144647c5b672b1c3ac"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Variations in Patients’ Overall Assessment of Their Health Across and Within Disease Groups Using the EQ-5D Questionnaire: Protocol for a Longitudinal Study in the Swedish National Quality Registers

## Abstract

### Background

EQ-5D is one of the most commonly used questionnaires to measure health-related quality of life. It is included in many of the Swedish National Quality Registers (NQRs). EQ-5D health states are usually summarized using “values” obtained from members of the general public, a majority of whom are healthy. However, an alternative, which remains to be studied in detail, is the potential to use patients’ self-reported overall health on the visual analog scale (VAS) as a means of capturing experience-based perspective.

### Objective

The aim of this study is to assess EQ VAS as a valuation method with an experience-based perspective through comparison of its performance across and within patient groups, and with that of the general population in Sweden.

### Methods

Data on nearly 700,000 patients from 12 NQRs covering a variety of diseases/conditions and nearly 50,000 individuals from the general population will be analyzed. The EQ-5D-3L data from the 12 registers and EQ-5D-5L data from 2 registers will be used in the analyses. Longitudinal studies of patient-reported outcomes among different patient groups will be conducted in the period from baseline to 1-year follow-up. Descriptive statistics and analyses comparing EQ-5D dimensions and observed self-assessed EQ VAS values across and within patient groups will be performed. Comparisons of the change in health state and observed EQ VAS values at 1-year follow-up will also be undertaken. Regression models will be used to assess whether EQ-5D dimensions predict observed EQ VAS values to investigate patient value sets in each patient group. These will be compared across the patient groups and with the existing Swedish experience-based VAS and time trade-off value sets obtained from the general population.

### Results

Data retrieval started in May 2019 and data of patients in the 12 NQRs and from the survey conducted among the general population have been retrieved. Data analysis is ongoing on the retrieved data.

### Conclusions

This research project will provide information on the differences across and within patient groups in terms of self-reported health status through EQ VAS and comparison with the general population. The findings of the study will contribute to the literature by exploring the potential of self-assessed EQ VAS values to develop value sets using an experience-based perspective.

### Trial Registration

ClinicalTrials.gov [NCT04359628](https://clinicaltrials.gov/ct2/show/NCT04359628); https://clinicaltrials.gov/ct2/show/[NCT04359628](https://clinicaltrials.gov/ct2/show/NCT04359628).

### International Registered Report Identifier (IRRID)

DERR1-10.2196/27669

**Keywords:** EQ-5D, EQ VAS, experience-based values, health-related quality of life (HRQoL), hypothetical values, patient values, Swedish National Quality Registers, health state valuation

Received 2021 Feb 2; Revision requested 2021 Apr 3; Revised 2021 Jun 19; Accepted 2021 Jun 29; Collection date 2021 Aug.

## Introduction

### Background

According to the US Food and Drug Administration, patient-reported outcomes (PROs) are defined as outcomes reported by patients without interpretation by anyone else \[1\]. They provide important information on outcomes that matter to patients \[2\], such as symptoms, functional outcomes, and health-related quality of life (HRQoL) \[3,4\]. PROs are increasingly used in health care \[5,6\] with applications in informing clinical practice and guidelines, informing health policy as well as supporting drug approval process among others \[7\]. In addition, PROs can be employed in different areas such as population surveillance, individual patient–clinician interaction, and research \[8\].

Patients provide information on standardized questionnaires termed patient-reported outcome measures (PROMs) \[9\], which are categorized into generic and disease/condition-specific PROMs. Generic PROMs enable comparisons across different patient groups and allow overall evaluation of care and quality of life. EQ-5D and the 36-item Short-Form (SF-36) are among the most common generic questionnaires. Condition-specific PROMs are used to assess outcomes specific to particular diseases/conditions from the perspective of patients \[9,10\].

The EQ-5D is a generic questionnaire used to measure HRQoL worldwide for a range of conditions and treatments \[11\]. It has a descriptive system (a set of questions in an HRQoL questionnaire encompassing different dimensions of health, the answers to which form a profile of an individual’s health) where respondents report their health in 5 dimensions (mobility, self-care, usual activities, pain/discomfort, anxiety/depression). Each of the 5 dimensions is measured with 1 question on the descriptive system of the EQ-5D questionnaire. EQ-5D contains a visual analog scale (EQ VAS) component for recording the respondent’s overall assessment of her/his health. There are 2 versions of the instrument for use in adults: one with 3 levels of severity (EQ-5D-3L) (1=no, 2=some/moderate, and 3=extreme problems/confined to bed/unable to), resulting in 243 (3<sup>5</sup>) unique health states. The other version with 5 levels of severity (EQ-5D-5L) (1=no, 2=slight, 3=moderate, 4=severe, and 5=extreme problems/unable to), resulting in 3125 (5<sup>5</sup>) unique health states. A health state is defined by combining the severity level from each of the 5 dimensions (e.g. for EQ-5D-3L health state 11223; no problem in the mobility \[level 1\] and self-care \[level 1\] dimensions, some problems with performing usual activities \[level 2\], moderate pain/discomfort \[level 2\], and extreme anxiety/depression \[level 3\]) \[11\].

An EQ-5D health state can be summarized into a single index (EQ-5D index) by applying a formula that attaches specific weights to each severity level in each dimension; this set of weights is termed a value set. The weights in a value set reflect the relative importance of the health dimensions and severity levels. The EQ-5D index enables the ranking of health states and can be used as the quality component in the adjustment of life years for calculation of quality-adjusted life years (QALYs) to be used in economic evaluation \[12\]. Commonly, EQ-5D indices are anchored at 1 (full health) and 0 (state as bad as being dead), with states considered worse than being dead given negative values \[13\].

A value set can be obtained using different health state valuation methods; for example, time trade-off (TTO), VAS, the standard gamble (SG) method, and the discrete choice experiments (DCEs) \[12\]. Choice-based health state valuation methods, which involve choosing between alternative scenarios, are crucial to produce health state utility used in the calculation of QALYs for use in cost-utility analyses. Such health state valuation methods are SG, TTO, and DCEs. SG is considered to have the strongest theoretical foundation on the basis of entailing the attributes of being choice based and incorporating an element of uncertainty. However, in terms of feasibility, TTO showed a better response rate \[14\] and is commonly employed in health state valuation. The VAS valuation method involves rating health states on the VAS scale. This leads to choice-based methods being preferred over it, as they are considered to allow choice/trade-off \[15\].

Currently, more than 30 countries have developed value sets for the EQ-5D-3L, predominantly using the TTO method. Some of the value sets have employed the VAS method, where respondents are asked to value described health states on the EQ-5D VAS. The EQ-5D VAS has a similar “thermometer”-like design as the EQ VAS, but when used for valuation purposes, respondents are given instructions to value a series of hypothetical EQ-5D health states by indicating where on the 0-100 line of the VAS they lie \[12,13,16\]. The EQ-5D-3L and EQ-5D-5L sample questionnaires containing the descriptive system and EQ VAS are presented in <a href="#app1" data-ref-type="supplementary-material">Multimedia Appendices 1</a> and <a href="#app2" data-ref-type="supplementary-material">2</a> (Reproduced by permission of the EuroQol Research Foundation). In the development of value sets for the EQ-5D-5L, the TTO method is currently used together with the DCE method based on the EuroQol Valuation Technology (EQ-VT) protocol \[17,18\] for about 30 countries.

Based on the perspective taken by respondents, valuation of health states could be performed through a hypothetical or experience-based perspective. While value sets have usually been based on members of the general population’s values of health states described to them (hypothetical values), another approach involves individuals in the general population valuing their own current health state (experience-based values) \[19-21\]. There are also studies where patients valued hypothetical health states \[22,23\]. A large majority of the value sets have employed a hypothetical perspective \[16,17\]. Many valuation studies which used an experience-based perspective have also been conducted, including studies in Sweden \[24-29\]. According to the Dental and Pharmaceutical Benefits Agency in Sweden, the agency that determines state subsidization of a pharmaceutical product, experience-based values are given priority over hypothetical values \[30,31\]. There is a growing discussion and interest in experience-based perspective in health state valuation, based on general populations’ and patient populations’ valuation of health states globally as shown in different literature \[19-21,32-41\].

As a health state valuation method, the advantages and possible limitations of VAS have been discussed in comparison to other methods such as TTO and SG. The advantages include being quick to complete and relatively easy for self-administration \[42\]. However, the above discussed arguments of lack of theoretical basis and not being choice based have also been raised \[42,43\]. Besides, this idea has been challenged by questioning the need for valuation methods to be based on utility theory \[44\]. It was pointed out that empirical performance should be used to select the relevant valuation method and VAS valuation was regarded advantageous over other methods in this respect \[44\]. A recent paper discussed the issue of anchoring at “dead” (ie, to assign 0 to the state of being dead for the calculation of QALYs) and alternative approaches to remedy challenges associated with anchoring at “dead.” The different alternative approaches provided in the paper indicate the potential of VAS to be used in economic evaluation \[45\].

Some studies comparing VAS with TTO and SG reported the advantage of VAS in terms of feasibility, whereas in other studies it was shown that VAS values differ considerably from TTO and SG values \[14,46-52\]. Specifically, in terms of feasibility, that is, response rate and cost of administration, findings indicated that VAS performed better than the other methods \[14,46-48\]. However, correlations of VAS values with those based on the TTO and SG methods were low to moderate, leading the authors to raise concerns regarding the use of VAS in health state valuation \[14\]. VAS values have also been compared with results from the TTO and DCE methods among patients, professionals, and laypersons. The decision to use VAS or TTO for individual patients and TTO or DCE for laypersons was recommended based on previous findings \[49\]. Transformation of VAS values to SG and TTO values through power functions has also been explored \[50,51\]. Concerning this, advise against transformation between VAS values and SG values through power function was expressed due to a lack of theoretical relationships \[52\]. In short, the studies explored the relationship of VAS with other valuation methods such as TTO and SG, indicating differences in valuations.

EQ VAS, as a component of the EQ-5D instrument, has been used to derive experience-based VAS value sets by using individuals’ overall assessment of their health reported on the EQ VAS to summarize how good or bad the health state they report is. These value sets have been developed in countries such as Sweden, Germany, China, and Canada \[24-28\]. Applying such value sets, studies reporting population reference values (norms data) and those that compared problems reported on EQ-5D dimensions with EQ VAS values were conducted \[53,54\]. Furthermore, another study compared patient value sets with that of the general population \[55\]. In addition, comparisons involving experience-based values developed using patients’ own EQ VAS values across 15 countries indicated significant differences in valuations of the same health states \[32\]. Similarly, EQ VAS values provided to the same health states by patients with 4 different medical conditions were also found to be different \[56\]. The cited studies showed the development of value sets based on EQ VAS and their application in addressing different questions in HRQoL research.

EQ VAS as a component of the EQ-5D has been in routine use with its validity and reliability demonstrated in different studies. Specifically, the EQ-5D questionnaire is employed in several Swedish National Quality Registers (NQRs) \[57\], making it possible to investigate the relationship between EQ-5D health states and self-reported EQ VAS values in different patient populations. As to the routine performance of EQ VAS in clinical settings, its significance as a possible diagnostic tool to predict frailty, the feasibility of its inclusion in daily patient diaries, and its performance in the National Health Service in the United Kingdom have been reported \[58-60\]. The validity, reliability, and responsiveness of EQ VAS values have also been shown by studies in different countries, including Sweden, in the general population, and in specific patient groups \[26,47,61-66\].

As shown above, TTO has been employed commonly for health state valuation, while VAS has also been employed in several studies \[12,16\]. While hypothetical perspectives were used commonly \[16\], increasing interest in experience-based perspectives was shown \[19-21\]. VAS has demonstrated advantages over other valuation methods in terms of feasibility \[14,46-48\]. However, arguments for and against the potential of VAS for use in health states valuation have been forwarded \[42-44\]. Studies employing EQ VAS in the valuation of health states and in reporting health have been conducted \[24-29,53-55\]. However, in the context of patient valuations of their own health, there is a knowledge gap in the literature regarding the relationship between the EQ-5D health states and self-assessed EQ VAS values across and within patient populations.

This research project will contribute to addressing the literature gap by adding to the current literature and international debate on the role of EQ VAS as a valuation method for experience-based health states. Addressing this issue will be facilitated through investigating large data sets containing PRO records of different patient populations covering a wide variety of conditions within the 12 Swedish NQRs. Both the EQ-5D-3L and EQ-5D-5L health states will also be investigated.

### Objective

The research project aims to assess EQ VAS as a valuation method with an experience-based perspective through a comparison of its performance across and within patient groups, and with that of the general population in Sweden. The following research questions will be investigated:

- How do EQ-5D health states and self-assessed EQ VAS values vary across and within patient groups, and at baseline and 1-year follow-up, and in comparison to the general population data?

- To what extent do EQ-5D dimensions predict EQ VAS values, and how do the resulting experience-based patient value sets differ when estimated from patients’ data at baseline and 1-year follow-up and how do the EQ VAS values predicted from EQ-5D dimensions differ between different patient groups?

- How do these patient value sets modeled using data from the registers compare with the Swedish VAS and TTO experience-based EQ-5D value sets obtained from the general population?

- How do value sets for EQ-5D-3L, derived from EQ VAS, differ from value sets for EQ-5D-5L, derived from its EQ VAS?

## Methods

### Study Design

A longitudinal study involving analyses of data on different patient groups will be conducted by assessing PROs from baseline to 1-year follow-up. The data from patients will be compared with cross-sectional survey data from the general population.

### Data Sources

Data from 12 NQRs on about 700,000 patients with PRO records will be included from the over 1.4 million patients in the registers. Clinical data (age, sex, BMI, diagnosis/es, and interventions) and PROs data (EQ-5D-3L, and EQ-5D-5L) will be retrieved from the registers. Data from cross-sectional population surveys in Sweden will be included for comparison; about 45,000 records were used in developing the Swedish experience-based VAS and TTO value sets \[26\]. The registers included in the project are described in <a href="#table1" data-ref-type="table">Tables 1</a> and <a href="#table2" data-ref-type="table">2</a>.

<div id="table1" class="table-wrap">

<div class="caption">

General information on the 12 National Quality Registers \[57,67\].

</div>

| Register | Diagnosis/condition | Intervention<sup>a</sup> | Start year | Unique patients<sup>b</sup> | New entries per year<sup>b</sup> |
|----|----|----|----|----|----|
| Better management of patients with Osteoarthritis (BOA) | Hip, knee, hand osteoarthritis | Supported Osteoarthritis Self-Management Programme (SOASP) | 2008 | 110,000 | 18,000 |
| Swedish Ankle Registry (Swedankle) | Osteoarthritis and inflammatory conditions in the ankle | Total ankle arthroplasty, ankle arthrodesis procedures | 1997 | 4000 | 400 |
| Swedish National Anterior Cruciate Ligament Register (xBase) | Cruciate ligament injuries | Cruciate ligament surgery | 2005 | 46,000 | 4000 |
| Swedish Fracture Register (SFR) | All types of fractures including vertebral/spinal fractures | Surgical and nonsurgical treatments | 2011 | 430,000 | 82,000 |
| Swedish Heart Failure Registry (SwedeHF) | Chronic heart failure | Pharmacological treatment, physical activity | 2003 | 92,000 | 9500 |
| Swedish Hip Arthroplasty Register (SHAR) | Hip osteoarthritis and other hip joint diagnoses | Hip replacement | 1979 | 370,000 | 25,000 |
| Swedish Knee Arthroplasty Register (SKAR) | Knee osteoarthritis and other knee joint diagnoses | Knee replacement | 1975 | 220,000 | 16,000 |
| Swedish National Quality Register for Bipolar Disorder (BipoläR) | Bipolar affective disorder | Pharmacological treatment, patient education | 2004 | 21,000 | 1500 |
| Swedish National Registry for Respiratory Failure (Swedevox) | Respiratory failure | Long-term oxygen therapy | 1987 | 20,000 | 1200 |
| Swedish Rheumatology Quality Register (SRQ) | Rheumatic diseases | Medical treatment, rehabilitation | 1995 | 80,000 | 7000 |
| Swedish Spine Register (Swespine) | Spinal stenosis, disk hernia, and other spinal diagnoses | Spine surgery | 1993 | 130,000 | 10,000 |
| Swedish Registry for Systematic Psoriasis Treatment (PsoReg) | Psoriasis | Systemic treatment for psoriasis | 2007 | 6500 | 500 |

<sup>a</sup>An intervention refers to surgeries or other forms of treatments provided to patients in the registers.

<sup>b</sup>Information on the number of patients and new entries per year was received from registers.

</div>

<div id="table2" class="table-wrap">

<div class="caption">

EQ-5D data collected at the 12 National Quality Registers \[57,67\].

</div>

| Register | Follow-up times |
|----|----|
| Better management of patients with Osteoarthritis (BOA) | First visit, 3 and 12 months; 1, 2, 3, 4, 5, 6, and 7 years after (100 patients per year are randomized to continued follow-ups) |
| Swedish Ankle Registry (Swedankle) | Before surgery, 6 months, 1 and 2 years after |
| Swedish National Anterior Cruciate Ligament Register (xBase) | Before surgery, 1, 2, 5, and 10 years after |
| Swedish Fracture Register (SFR)<sup>a</sup> | A week before injury (recall) and 1 year after |
| Swedish Heart Failure Registry (SwedeHF) | At new visit, within 6 months and 1 year, once every year |
| Swedish Hip Arthroplasty Register (SHAR) | Before surgery, 1, 6, and 10 years after |
| Swedish Knee Arthroplasty Register (SKAR) | Before surgery, 1 year after |
| Swedish National Quality Register for Bipolar Disorder (BipoläR) | At visit |
| Swedish National Registry for Respiratory Failure (Swedevox) | At treatment start, 1 year after |
| Swedish Rheumatology Quality Register (SRQ) | At visit |
| Swedish Spine Register (Swespine) | Before surgery, 1, 2, 5, and 10 years after |
| Swedish Registry for Systematic Psoriasis Treatment (PsoReg) | At each revisit due to psoriasis/visit to the skin clinic/telephone conversation with a dermatologist |

<sup>a</sup>Baseline data in SFR are collected by a recall of a few weeks after the occurrence of fracture.

</div>

### Plan for Data Analyses

The analyses will focus on the 3 main data components coming from the EQ-5D instruments: data collected by the EQ-5D-3L (and EQ-5D-5L for some registers) descriptive systems on the 5 dimensions, the EQ VAS value self-assessed by patients, and indices resulting from transforming the EQ-5D-3L health states into a single index using the Swedish EQ-5D-3L experience-based VAS value sets.

The data from the NQRs will be pooled and diagnoses in each patient group will be used to identify the different subgroups. Records of patients with complete data on age, sex, diagnosis at baseline, and PROs at baseline and 1-year follow-up will be included in the analysis. Although different follow-up times are available in the registers as shown in <a href="#table2" data-ref-type="table">Table 2</a>, the baseline and 1-year follow-up data will be used in the comparison across the different patient groups. To make comparisons with findings from the patient data, demographic, BMI, and EQ-5D-3L data from the general population survey covering about 50,000 participants will be employed. Detailed information on the general population data is available elsewhere \[26\].

All analyses will be conducted using SAS version 9.4 (SAS Institute Inc.) and R version 3.6.2 (R Foundation for Statistical Computing).

### EQ-5D Health States and Observed EQ VAS Values

In addressing the first research question, the proportion of problems (no problem \[level 1\], some problems \[level 2\], and severe problems \[level 3\]) for each dimension and observed EQ VAS values of patients, at baseline and 1-year follow-up, will be compared across and within the patient groups (as well as subgroups based on diagnosis groups) and with the general population data. These descriptive analyses will also be presented by age groups, sex, BMI, and American Society of Anesthesiologists (ASA) physical status classification system (for patient groups with data on ASA class; <a href="#table1" data-ref-type="table">Tables 1</a> and <a href="#table2" data-ref-type="table">2</a>). Comparison of EQ VAS values by sex in the different patient groups, controlling for age, will be performed using analysis of covariance. Cluster analysis will be performed to assess the distribution of the EQ VAS value in the different patient groups at both baseline and 1-year follow-up.

Furthermore, pooled data from all NQRs will be used to analyze EQ VAS and to explore the influence of both patient characteristics and the patient group (registers). This will be performed by accounting for the grouping of patients by register. Linear mixed effects models with the patient group, preoperative EQ VAS (for the analysis at 1 year and the change from baseline), intervention type, age, and sex as fixed effects, and the patient group as the random effect will be used. Age and sex have been shown to influence EQ VAS values in previous studies \[68,69\].

Change over time in terms of the proportions of problems reported in each dimension will be presented using the Paretian Classification of Health Change, introduced to apply the Pareto Principle to EQ-5D health states \[70\]. This analysis will be performed by calculating the proportions of changes in health states from baseline to 1-year follow-up. The changes will be categorized as “no problem” (health state 11111 at both baseline and 1-year follow-up), “no change” (same health state at both baseline and 1-year follow-up), “improved” (improvement in at least one dimension without worsening in any other), “worsened” (worsening in at least one dimension without improvement in any other), and “mixed” (a mix of improvement and worsening) \[70\]. These changes will be analyzed descriptively in different patient groups and subgroups. In addition, changes in EQ VAS in the Paretian Classification of Health Change categories will be analyzed.

### Value Sets Based on Observed EQ VAS Values

In addressing the second research question, data on the EQ-5D health state and observed EQ VAS value at baseline and 1-year follow-up will be included in the respective analyses. To assess how well the observed EQ VAS value reflects the EQ-5D health states, the EQ-5D-3L dimensions will be analyzed as possible predictors of the observed EQ VAS value through regression models, such as ordinary least squares and generalized linear models, in each patient group and the pooled data. Both unadjusted and adjusted (for age and sex) models will be used. Corresponding analyses will be performed for EQ-5D-5L dimensions.

Based on results from predictive performance measures of the models, such as mean absolute error and root mean square error, the most appropriate models will be selected. These models will be used to develop patient value sets based on observed EQ VAS values assessed by the respective patient groups and the pooled data. In this process, value sets will be created for both baseline and 1-year postoperative follow-up.

### Comparison of Patient Value Sets With the Swedish Experience-Based VAS and TTO Value Sets

In addressing the third research question, value sets elicited for each patient group using EQ-5D-3L will then be compared with the Swedish experience-based VAS and TTO value sets for EQ-5D-3L, which are elicited from the general population \[26\]. This will be performed by comparing the regression coefficients (indicating the levels of decrement from full health) of the severity levels in each dimension across patient groups and the general population data. Furthermore, EQ-5D-3L indices calculated based on the value sets elicited from patients will be compared with those of the Swedish experience-based VAS (see model 4 in Table S4 of the supplementary material in Burström et al \[26\]) and TTO (see model 4 in Table 3 in Burström et al \[26\]) value sets to assess the levels of agreement. This will be performed using Lin’s concordance correlation coefficients or intraclass correlation coefficient \[71\].

### Comparison of EQ-5D-3L and EQ-5D-5L Value Sets From Patients in the BOA Register and Swedish Hip Arthroplasty Register

In addressing the fourth research question, a comparison of the value sets for the EQ-5D-3L and EQ-5D-5L versions modeled based on data from patients in the BOA and Swedish Hip Arthroplasty Register (SHAR) will be performed. The 2 patient groups were chosen because it is in these registers EQ-5D-5L data are available. Specifically, the comparisons will assess coefficients of the value sets for the 2 EQ-5D versions, EQ-5D index changes between adjacent health states, and the range of the indices (from minimum to maximum values in each index). Furthermore, analysis to compare the difference in EQ-5D index between comparable EQ-5D-3L and EQ-5D-5L health states will be performed through descriptive statistics using 243 health states from EQ-5D-3L and corresponding states from EQ-5D-5L. For a description of terms discussed in this paper, please see <a href="#box1" data-ref-type="boxed-text">Textbox 1</a>.

<div class="caption">

###### Description of terms.

</div>

**EQ-5D Dimensions**

In both EQ-5D-3L and EQ-5D-5L versions, the 5 domains (mobility, self-care, usual activities, pain/discomfort, and anxiety/depression) constituting the EQ-5D descriptive system \[13\].

**EQ Visual Analog Scale (VAS)**

A 20-cm vertical scale where respondents describe the overall rating of their health-related quality of life. It ranges from 0 (the worst imaginable health state) to 100 (the best imaginable health state) \[13\].

**Health State**

It is also described as an EQ-5D profile. It summarizes the severity of levels described in the 5 EQ-5D dimensions \[13\]. For example, health state 11111 describes no problems in all the 5 dimensions.

**Value Set**

An EQ-5D value set contains values for every possible EQ-5D health state. These values are calculated using algorithms providing weights to the level of problems reported on each EQ-5D dimension \[13\]. The algorithms are developed in valuation studies using different valuation methods.

**EQ-5D Index**

It is also known as EQ-5D value, score, or utility. It is a value that summarizes the value of a health state based on the set of weights assigned to the levels of severity for each dimension \[13\].

**Standard Gamble**

It measures preference under uncertainty. In this method, a respondent is presented with 2 alternatives. The comparison involves staying in a specific health state for a defined number of years (certain alternative) with that of a specific probability of being full health for the same period or a specific probability of immediate death (uncertain alternative) \[72\].

**Time Trade-off**

In time trade-off, respondents are asked to compare 2 certain alternatives. One alternative gives staying in a specific health state for a defined period. The alternative presents staying in full health for a specific duration, usually lower. The point at which the respondent becomes indifferent between the alternatives indicates his/her level of preference for the specific health state \[72\].

**Discrete Choice Experiment**

Respondents are presented with a choice between alternative hypothetical scenarios. The choices provided could vary across different levels of attributes or characteristics. Respondents choose from the alternative scenarios \[73\].

### Ethics Approval and Consent to Participate

The study has been approved by the Regional Ethical Review Board, Gothenburg (1185-18/2019-00812). General population survey data, with approval from the Regional Ethical Review Board, Stockholm (2020-03090), will be used for comparison with patient data sets. The data on the patients will be pseudonymized and stored at the Centre for Registers in Västra Götaland before access is provided to members of the research team authorized to do so. All analyses of the data will be on an aggregate level and there will be no individual-level reporting of data.

### Dissemination of Findings

Findings from studies in the project will be disseminated through publication in peer-reviewed scientific journals and presentations at national or international conferences.

## Results

The study project involves data from 12 NQRs and the general population. Data retrieval started in May 2019. Data of patients from the 12 NQRs and the survey conducted among the general population have been retrieved. Data analysis on the retrieved data is ongoing.

## Discussion

The project will provide information on the pattern of variation of EQ VAS value across patient groups and subgroups, and on how the pattern changes from baseline to 1-year follow-up. Information on the differences between experience-based values from patients and the general population in Sweden will also be provided. This could be an input to the discussion on the merits and characteristics of experience-based valuation.

This project is also expected to provide information on the level of importance of the different dimensions and levels of severity in the EQ-5D questionnaire to different patient groups. This will be assessed based on how a similar level of severity in one dimension (eg, pain/discomfort) is valued in different patient groups in terms of its impact on the EQ VAS value. Furthermore, the importance of different dimensions and severity levels to different patient groups will be assessed in comparison to the general population.

The project will also contribute to the discussion of valuation methods regarding the feasibility and appropriateness of EQ VAS as a valuation method. Based on the findings, the potential benefits of using experience-based EQ VAS values in clinical decisions—rather than values obtained from members of the general population valuing described health states—will be discussed. Furthermore, the potential role of value sets produced using EQ VAS values for use in resource allocation decisions will be discussed. If feasible value sets can be generated from patients’ self-assessed EQ VAS data, this not only provides a means of building patients’ views and experience into decision making, it also means not having to conduct separate, costly, and time-consuming stated preference studies.

## Acknowledgments

This research project is supported by a grant from The EuroQol Research Foundation (EQ Project 2016480) and Stockholm County Council (# 4-3464/2018), Stockholm, Sweden. The funding bodies do not influence the design, data collection, analysis, interpretation, or writing the manuscript. The authors thank members of the Health Outcomes and Economic Evaluation Research Group for their useful comments and suggestions on earlier presentations of this research project. Group authors: members of the Swedish Quality Registers (SWEQR) Study Group in alphabetical order:

**Allan Abbott**, PhD, Linköping University, Linköping, Sweden;

**Magnus Ekström**, MD, PhD, Lund University, Lund, Sweden;

**Magnus Forssblad**, MD, PhD, Karolinska Institutet, Stockholm, Sweden;

**Peter Fritzell**, MD, PhD, Ryhov County Hospital, Jönköping, Sweden;

**Åsa Jonsson**, RN, PhD, Ryhov County Hospital, Jönköping, Sweden;

**Mikael Landén**, MD, PhD, University of Gothenburg, Gothenburg, Sweden;

**Michael Möller**, MD, PhD, University of Gothenburg, Gothenburg, Sweden;

**Malin Regardt**, PhD, Karolinska Institutet, Stockholm, Sweden;

**Björn Rosengren**, MD, PhD, Lund University, Lund, Sweden;

**Marcus Schmitt-Egenolf**, MD, PhD, Umeå University, Umeå, Sweden;

**Johanna Vinblad**, MSc, Centre of Registers, Gothenburg, Sweden;

**Annette W-Dahl**, PhD, Lund University, Lund, Sweden.

## Abbreviations

ANOVA  
analysis of variance

ASA  
American Society of Anesthesiologists

BipoläR  
Swedish National Quality Register for Bipolar Disorder

BOA  
Better management of patients with Osteoarthritis

DCE  
discrete choice experiment

EQ VAS  
EuroQol visual analog scale

EQ-VT  
EuroQol Valuation Technology

HRQoL  
health-related quality of life

NQRs  
National Quality Registers

PRO  
patient-reported outcome

PROM  
patient-reported outcome measure

PsoReg  
Swedish Registry for Systematic Psoriasis Treatment

QALYs  
quality-adjusted life year

SF-36  
36-item Short-Form

SG  
standard gamble

SHAR  
Swedish Hip Arthroplasty Register

SKAR  
Swedish Knee Arthroplasty Register

SRQ  
Swedish Rheumatology Quality Register

Swedankle  
Swedish Ankle Registry

SwedeHF  
Swedish Heart Failure Registry

Swedevox  
Swedish National Registry for Respiratory Failure

Swespine  
Swedish Spine Register

TTO  
time trade-off

VAS  
visual analog scale

xBase  
Swedish National Anterior Cruciate Ligament Register

Sample EQ-5D-3L questionnaire, English.

Sample EQ-5D-5L questionnaire, English.

## Footnotes

## References

## References

1. US Food and Drug Administration Guidance for Industry: Patient-Reported Outcome Measures: Use in Medical Product Development to Support Labeling Claims. 2009. [2020-07-15]. https://www.fda.gov/media/77832/download . doi:10.1186/1477-7525-4-79

2. Makrinioti H, Bush A, Griffiths C. What are patient-reported outcomes and why they are important: improving studies of preschool wheeze. Arch Dis Child Educ Pract Ed. 2020 Jun;105(3):185–188. doi: 10.1136/archdischild-2018-316476.archdischild-2018-316476

3. Mercieca-Bebber R, King MT, Calvert MJ, Stockler MR, Friedlander M. The importance of patient-reported outcomes in clinical trials and strategies for future optimization. Patient Relat Outcome Meas. 2018;9:353–367. doi: 10.2147/PROM.S156279. doi: 10.2147/PROM.S156279.prom-9-353

4. Rothman ML, Beltran P, Cappelleri JC, Lipscomb J, Teschendorf B, Mayo/FDA Patient-Reported Outcomes Consensus Meeting Group Patient-reported outcomes: conceptual issues. Value Health. 2007 Dec;10 Suppl 2:S66–75. doi: 10.1111/j.1524-4733.2007.00269.x. https://linkinghub.elsevier.com/retrieve/pii/S1098-3015(10)60631-6 .S1098-3015(10)60631-6

5. Holmes MM, Lewith G, Newell D, Field J, Bishop FL. The impact of patient-reported outcome measures in clinical practice for pain: a systematic review. Qual Life Res. 2017 Feb;26(2):245–257. doi: 10.1007/s11136-016-1449-5. http://europepmc.org/abstract/MED/27815820 .10.1007/s11136-016-1449-5

6. Appleby J, Devlin N, Parkin D. Using Patient Reported Outcomes to Improve Health Care. Hoboken, NJ: John Wiley & Sons; 2015.

7. Rivera SC, Kyte DG, Aiyegbusi OL, Slade AL, McMullan C, Calvert MJ. The impact of patient-reported outcome (PRO) data from clinical trials: a systematic review and critical analysis. Health Qual Life Outcomes. 2019 Oct 16;17(1):156. doi: 10.1186/s12955-019-1220-z. https://hqlo.biomedcentral.com/articles/10.1186/s12955-019-1220-z .10.1186/s12955-019-1220-z

8. Snyder CF, Jensen RE, Segal JB, Wu AW. Patient-reported outcomes (PROs): putting the patient perspective in patient-centered outcomes research. Med Care. 2013 Aug;51(8 Suppl 3):S73–9. doi: 10.1097/MLR.0b013e31829b1d84. http://europepmc.org/abstract/MED/23774513 .

9. Kingsley C, Patel S. Patient-reported outcome measures and patient-reported experience measures. BJA Education. 2017 Apr 1;17(4):137–144. doi: 10.1093/bjaed/mkw060. doi: 10.1093/bjaed/mkw060.

10. Schifferdecker KE, Yount SE, Kaiser K, Adachi-Mejia A, Cella D, Carluzzo KL, Eisenstein A, Kallen MA, Greene GJ, Eton DT, Fisher ES. A method to create a standardized generic and condition-specific patient-reported outcome measure for patient care and healthcare improvement. Qual Life Res. 2018 Feb;27(2):367–378. doi: 10.1007/s11136-017-1675-5.10.1007/s11136-017-1675-5

11. Devlin NJ, Brooks R. EQ-5D and the EuroQol Group: Past, Present and Future. Appl Health Econ Health Policy. 2017 Apr;15(2):127–137. doi: 10.1007/s40258-017-0310-5. http://europepmc.org/abstract/MED/28194657 .10.1007/s40258-017-0310-5

12. EuroQol Research Foundation EQ-5D-3L User Guide. 2018. [2020-11-09]. https://euroqol.org/publications/user-guides .

13. EuroQoL Group Terminology - EQ-5D. 2020. Jun 03, [2020-10-06]. https://euroqol.org/support/terminology/

14. Brazier J, Deverill M, Green C. A review of the use of health status measures in economic evaluation. J Health Serv Res Policy. 1999 Jul;4(3):174–84. doi: 10.1177/135581969900400310.

15. Whitehead SJ, Ali S. Health outcomes in economic evaluation: the QALY and utilities. Br Med Bull. 2010;96:5–21. doi: 10.1093/bmb/ldq033.ldq033

16. Szende A, Oppe M, Devlin N, editors. EQ-5D Value Sets: Inventory, Comparative Review and User Guide. Dordrecht, The Netherlands: Springer Netherlands; 2007.

17. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goñi JM. Overview, Update, and Lessons Learned From the International EQ-5D-5L Valuation Work: Version 2 of the EQ-5D-5L Valuation Protocol. Value Health. 2019 Jan;22(1):23–30. doi: 10.1016/j.jval.2018.05.010. https://linkinghub.elsevier.com/retrieve/pii/S1098-3015(18)36164-3 .S1098-3015(18)36164-3

18. EuroQol Research Foundation EQ-5D-5L User Guide: Basic information on how to use the EQ-5D-5L instrument Internet. 2019. [2021-08-03]. https://euroqol.org/publications/user-guides .

19. Cubi-Molla P, Shah K, Burström K. Experience-Based Values: A Framework for Classifying Different Types of Experience in Health Valuation Research. Patient. 2018 Jun;11(3):253–270. doi: 10.1007/s40271-017-0292-2.10.1007/s40271-017-0292-2

20. Versteegh MM, Brouwer WBF. Patient and general public preferences for health states: A call to reconsider current guidelines. Soc Sci Med. 2016 Sep;165:66–74. doi: 10.1016/j.socscimed.2016.07.043.S0277-9536(16)30404-X

21. Helgesson G, Ernstsson O, Åström M, Burström K. Whom should we ask? A systematic literature review of the arguments regarding the most accurate source of information for valuation of health states. Qual Life Res. 2020 Jul;29(6):1465–1482. doi: 10.1007/s11136-020-02426-4. http://europepmc.org/abstract/MED/32016683 .10.1007/s11136-020-02426-4

22. Dufresne. Poder TG, Samaan K, Lacombe-Barrios J, Paradis L, Des Roches A, Bégin P. SF-6Dv2 preference value set for health utility in food allergy. Allergy. 2021 Jan;76(1):326–338. doi: 10.1111/all.14444.

23. Happich M, Moock J, von Lengerke T. Health state valuation methods and reference points: the case of tinnitus. Value Health. 2009;12(1):88–95. doi: 10.1111/j.1524-4733.2008.00397.x. https://linkinghub.elsevier.com/retrieve/pii/S1098-3015(10)60677-8 .S1098-3015(10)60677-8

24. Leidl R, Reitmeir P. A value set for the EQ-5D based on experienced health states: development and testing for the German population. Pharmacoeconomics. 2011 Jun;29(6):521–34. doi: 10.2165/11538380-000000000-00000.

25. Leidl R, Reitmeir P. An Experience-Based Value Set for the EQ-5D-5L in Germany. Value Health. 2017 Sep;20(8):1150–1156. doi: 10.1016/j.jval.2017.04.019. https://linkinghub.elsevier.com/retrieve/pii/S1098-3015(17)30219-X .S1098-3015(17)30219-X

26. Burström K, Sun S, Gerdtham U, Henriksson M, Johannesson M, Levin L, Zethraeus N. Swedish experience-based value sets for EQ-5D health states. Qual Life Res. 2014 Mar;23(2):431–42. doi: 10.1007/s11136-013-0496-4. http://europepmc.org/abstract/MED/23975375 .

27. Wu XY, Ohinmaa A, Johnson JA, Veugelers PJ. Assessment of children's own health status using visual analogue scale and descriptive system of the EQ-5D-Y: linkage between two systems. Qual Life Res. 2014 Mar;23(2):393–402. doi: 10.1007/s11136-013-0479-5.

28. Sun S, Chen J, Kind P, Xu L, Zhang Y, Burström K. Experience-based VAS values for EQ-5D-3L health states in a national general population health survey in China. Qual Life Res. 2015 Mar;24(3):693–703. doi: 10.1007/s11136-014-0793-6. http://europepmc.org/abstract/MED/25246184 .

29. Burström K, Teni FS, Gerdtham U, Leidl R, Helgesson G, Rolfson O, Henriksson M. Experience-Based Swedish TTO and VAS Value Sets for EQ-5D-5L Health States. Pharmacoeconomics. 2020 Aug;38(8):839–856. doi: 10.1007/s40273-020-00905-7.10.1007/s40273-020-00905-7

30. The Dental and Pharmaceutical Benefits Agency (TLV) Our mission. 2019. [2019-11-07]. https://www.tlv.se/in-english/organisation/our-mission.html .

31. The Pharmaceutical Benefits Board General Guidelines for Economic Evaluations From the Pharmaceutical Benefits Board. 2003. [2021-07-31]. https://www.tlv.se/download/18.2e53241415e842ce95514e9/1510316396792/Guidelines-for-economic-evaluations-LFNAR-2003-2.pdf .

32. Heijink R, Reitmeir P, Leidl R. International comparison of experience-based health state values at the population level. Health Qual Life Outcomes. 2017 Jul 07;15(1):138. doi: 10.1186/s12955-017-0694-9. https://hqlo.biomedcentral.com/articles/10.1186/s12955-017-0694-9 .10.1186/s12955-017-0694-9

33. Nemes S, Burström K, Zethraeus N, Eneqvist T, Garellick G, Rolfson O. Assessment of the Swedish EQ-5D experience-based value sets in a total hip replacement population. Qual Life Res. 2015 Dec;24(12):2963–70. doi: 10.1007/s11136-015-1020-9.10.1007/s11136-015-1020-9

34. Little MHR, Reitmeir P, Peters A, Leidl R. The impact of differences between patient and general population EQ-5D-3L values on the mean tariff scores of different patient groups. Value Health. 2014 Jun;17(4):364–71. doi: 10.1016/j.jval.2014.02.002. https://linkinghub.elsevier.com/retrieve/pii/S1098-3015(14)00020-5 .S1098-3015(14)00020-5

35. Cooper A, Wallman JK, Gülfe A. What PASSes for good? Experience-based Swedish and hypothetical British EuroQol 5-Dimensions preference sets yield markedly different point estimates and patient acceptable symptom state cut-off values in chronic arthritis patients on TNF blockade. Scand J Rheumatol. 2016 Nov;45(6):470–473. doi: 10.3109/03009742.2016.1143965.

36. Brazier J, Rowen D, Karimi M, Peasgood T, Tsuchiya A, Ratcliffe J. Experience-based utility and own health state valuation for a health state classification system: why and how to do it. Eur J Health Econ. 2018 Jul;19(6):881–891. doi: 10.1007/s10198-017-0931-5. http://europepmc.org/abstract/MED/29022120 .10.1007/s10198-017-0931-5

37. Pickard AS, Hung Y, Lin F, Lee TA. Patient Experience-based Value Sets: Are They Stable? Med Care. 2017 Nov;55(11):979–984. doi: 10.1097/MLR.0000000000000802.00005650-201711000-00013

38. Kind P. Valuing EQ-5D health states?a VAStly simpler solution?. The EuroQol Plenary Meeting; 2007; The Hague, The Netherlands. 2007. pp. 1–13.

39. Rand-Hendriksen K, Augestad LA, Kristiansen IS, Stavem K. Comparison of hypothetical and experienced EQ-5D valuations: relative weights of the five dimensions. Qual Life Res. 2012 Aug;21(6):1005–12. doi: 10.1007/s11136-011-0016-3.

40. Burström K, Johannesson M, Diderichsen F. A comparison of individual and social time trade-off values for health states in the general population. Health Policy. 2006 May;76(3):359–70. doi: 10.1016/j.healthpol.2005.06.011.S0168-8510(05)00154-5

41. Kiadaliri AA, Eliasson B, Gerdtham U. Does the choice of EQ-5D tariff matter? A comparison of the Swedish EQ-5D-3L index score with UK, US, Germany and Denmark among type 2 diabetes patients. Health Qual Life Outcomes. 2015 Sep 15;13:145. doi: 10.1186/s12955-015-0344-z. https://hqlo.biomedcentral.com/articles/10.1186/s12955-015-0344-z .10.1186/s12955-015-0344-z

42. Torrance GW, Feeny D, Furlong W. Visual analog scales: do they have a role in the measurement of preferences for health states? Med Decis Making. 2001;21(4):329–34. doi: 10.1177/0272989X0102100408.

43. Johannesson M, Jönsson B, Karlsson G. Outcome measurement in economic evaluation. Health Econ. 1996;5(4):279–96. doi: 10.1002/(SICI)1099-1050(199607)5:4<279::AID-HEC218>3.0.CO;2-J.10.1002/(SICI)1099-1050(199607)5:4<279::AID-HEC218>3.0.CO;2-J

44. Parkin D, Devlin N. Is there a case for using visual analogue scale valuations in cost-utility analysis? Health Econ. 2006 Jul;15(7):653–64. doi: 10.1002/hec.1086.

45. Sampson C, Devlin N, Parkin D. Drop dead: is anchoring at 'dead' a theoretical requirement in health state valuation?. 35th EuroQol Group Scientific Plenary Meeting; December 15, 2020; Lisbon, Portugal. 2020.

46. Badia X, Monserrat S, Roset M, Herdman M. Feasibility, validity and test-retest reliability of scaling methods for health states: the visual analogue scale and the time trade-off. Qual Life Res. 1999 Jun;8(4):303–10. doi: 10.1023/a:1008952423122.

47. Kim S, Lee S, Jo M. Feasibility, comparability, and reliability of the standard gamble compared with the rating scale and time trade-off techniques in Korean population. Qual Life Res. 2017 Dec;26(12):3387–97. doi: 10.1007/s11136-017-1676-4.10.1007/s11136-017-1676-4

48. Lenert LA, Sturley AE. Acceptability of computerized visual analog scale, time trade-off and standard gamble rating methods in patients and the public. Proc AMIA Symp. 2001:364–8. http://europepmc.org/abstract/MED/11825211 .D010001392

49. Bijlenga D, Birnie E, Mol BW, Bonsel GJ. Obstetrical outcome valuations by patients, professionals, and laypersons: differences within and between groups using three valuation methods. BMC Pregnancy Childbirth. 2011 Dec 12;11:93. doi: 10.1186/1471-2393-11-93. https://bmcpregnancychildbirth.biomedcentral.com/articles/10.1186/1471-2393-11-93 .1471-2393-11-93

50. Stiggelbout AM, Eijkemans MJ, Kiebert GM, Kievit J, Leer JW, De Haes HJ. The 'utility' of the visual analog scale in medical decision making and technology assessment. Is it an alternative to the time trade-off? Int J Technol Assess Health Care. 1996;12(2):291–8. doi: 10.1017/s0266462300009648.

51. Stevens KJ, McCabe CJ, Brazier JE. Mapping between Visual Analogue Scale and Standard Gamble data; results from the UK Health Utilities Index 2 valuation survey. Health Econ. 2006 May;15(5):527–33. doi: 10.1002/hec.1076.

52. Robinson A, Loomes G, Jones-Lee M. Visual analog scales, standard gambles, and relative risk aversion. Med Decis Making. 2001;21(1):17–27. doi: 10.1177/0272989X0102100103.

53. Huber MB, Felix J, Vogelmann M, Leidl R. Health-Related Quality of Life of the General German Population in 2015: Results from the EQ-5D-5L. Int J Environ Res Public Health. 2017 Apr 16;14(4):426. doi: 10.3390/ijerph14040426. https://www.mdpi.com/resolver?pii=ijerph14040426 .ijerph14040426

54. Huber M, Vogelmann M, Leidl R. Valuing health-related quality of life: systematic variation in health perception. Health Qual Life Outcomes. 2018 Aug 02;16(1):156. doi: 10.1186/s12955-018-0986-8. https://hqlo.biomedcentral.com/articles/10.1186/s12955-018-0986-8 .10.1186/s12955-018-0986-8

55. Felix J, Becker C, Vogl M, Buschner P, Plötz W, Leidl R. Patient characteristics and valuation changes impact quality of life and satisfaction in total knee arthroplasty - results from a German prospective cohort study. Health Qual Life Outcomes. 2019 Dec 09;17(1):180. doi: 10.1186/s12955-019-1237-3. https://hqlo.biomedcentral.com/articles/10.1186/s12955-019-1237-3 .10.1186/s12955-019-1237-3

56. Whynes DK. Does the correspondence between EQ-5D health state description and VAS score vary by medical condition? Health Qual Life Outcomes. 2013 Sep 13;11:155. doi: 10.1186/1477-7525-11-155. https://hqlo.biomedcentral.com/articles/10.1186/1477-7525-11-155 .1477-7525-11-155

57. Emilsson L, Lindahl B, Köster M, Lambe M, Ludvigsson JF. Review of 103 Swedish Healthcare Quality Registries. J Intern Med. 2015 Jan;277(1):94–136. doi: 10.1111/joim.12303. doi: 10.1111/joim.12303.

58. Kim S, Won CW, Kim BS, Kim S, Yoo J, Byun S, Jang HC, Cho BL, Son SJ, Lee JH, Park YS, Choi KM, Kim HJ, Lee SG. EuroQol Visual Analogue Scale (EQ-VAS) as a Predicting Tool for Frailty in Older Korean Adults: The Korean Frailty an Aging Cohort Study (KFACS) J Nutr Health Aging. 2018;22(10):1275–80. doi: 10.1007/s12603-018-1077-6.

59. Parkin D, Rice N, Jacoby A, Doughty J. Use of a visual analogue scale in a daily patient diary: modelling cross-sectional time-series data on health-related quality of life. Soc Sci Med. 2004 Jul;59(2):351–60. doi: 10.1016/j.socscimed.2003.10.015.S0277953603005525

60. Feng Y, Parkin D, Devlin NJ. Assessing the performance of the EQ-VAS in the NHS PROMs programme. Qual Life Res. 2014 Apr;23(3):977–89. doi: 10.1007/s11136-013-0537-z. http://europepmc.org/abstract/MED/24081873 .

61. Golicki D, Niewada M, Karlińska A, Buczek J, Kobayashi A, Janssen MF, Pickard AS. Comparing responsiveness of the EQ-5D-5L, EQ-5D-3L and EQ VAS in stroke patients. Qual Life Res. 2015 Jul;24(6):1555–63. doi: 10.1007/s11136-014-0873-7. http://europepmc.org/abstract/MED/25425288 .

62. Lin F-J, Samp J, Munoz A, Wong PS, Pickard AS. Evaluating change using patient-reported outcome measures in knee replacement: the complementary nature of the EQ-5D index and VAS scores. Eur J Health Econ. 2014 Jun;15(5):489–96. doi: 10.1007/s10198-013-0489-9.

63. Sonntag M, Konnopka A, Leichsenring F, Salzer S, Beutel ME, Herpertz S, Hiller W, Hoyer J, Joraschky P, Nolting B, Pöhlmann K, Stangier U, Strauss B, Willutzki U, Wiltink J, Leibing E, König H. Reliability, validity and responsiveness of the EQ-5D in assessing and valuing health status in patients with social phobia. Health Qual Life Outcomes. 2013 Dec 23;11:215. doi: 10.1186/1477-7525-11-215. https://hqlo.biomedcentral.com/articles/10.1186/1477-7525-11-215 .1477-7525-11-215

64. Eneqvist T, Nemes S, Kärrholm J, Burström K, Rolfson O. How do EQ-5D-3L and EQ-5D-5L compare in a Swedish total hip replacement population? Acta Orthop. 2020 Jun;91(3):272–8. doi: 10.1080/17453674.2020.1746124. http://europepmc.org/abstract/MED/32237930 .

65. Larsson I-M, Wallin E, Rubertsson S, Kristofferzon M. Health-related quality of life improves during the first six months after cardiac arrest and hypothermia treatment. Resuscitation. 2014 Mar;85(2):215–20. doi: 10.1016/j.resuscitation.2013.09.017.S0300-9572(13)00755-7

66. Teni FS, Burström K, Berg J, Leidl R, Rolfson O. Predictive ability of the American Society of Anaesthesiologists physical status classification system on health-related quality of life of patients after total hip replacement: comparisons across eight EQ-5D-3L value sets. BMC Musculoskelet Disord. 2020 Jul 06;21(1):441. doi: 10.1186/s12891-020-03399-8. https://bmcmusculoskeletdisord.biomedcentral.com/articles/10.1186/s12891-020-03399-8 .10.1186/s12891-020-03399-8

67. Sveriges Kommuner Och Landsting Nationella Kvalitetsregister [National Quality Register] [2019-04-23]. http://kvalitetsregister.se/hittaregister.1815.html .

68. Katchamart W, Narongroeknawin P, Chanapai W, Thaweeratthakul P. Health-related quality of life in patients with rheumatoid arthritis. BMC Rheumatol. 2019;3:34. doi: 10.1186/s41927-019-0080-9. https://bmcrheumatol.biomedcentral.com/articles/10.1186/s41927-019-0080-9 .80

69. Faxén UL, Hage C, Donal E, Daubert J, Linde C, Lund LH. Patient reported outcome in HFpEF: Sex-specific differences in quality of life and association with outcome. Int J Cardiol. 2018 Sep 15;267:128–132. doi: 10.1016/j.ijcard.2018.04.102.S0167-5273(18)31021-0

70. Devlin NJ, Parkin D, Browne J. Patient-reported outcome measures in the NHS: new methods for analysing and reporting EQ-5D data. Health Econ. 2010 Aug;19(8):886–905. doi: 10.1002/hec.1608.

71. Watson PF, Petrie A. Method agreement analysis: a review of correct methodology. Theriogenology. 2010 Jun;73(9):1167–79. doi: 10.1016/j.theriogenology.2010.01.003. https://linkinghub.elsevier.com/retrieve/pii/S0093-691X(10)00023-3 .S0093-691X(10)00023-3

72. Bleichrodt H, Johannesson M. Standard gamble, time trade-off and rating scale: experimental results on the ranking properties of QALYs. J Health Econ. 1997 Apr;16(2):155–75. doi: 10.1016/s0167-6296(96)00509-7.S0167-6296(96)00509-7

73. Ryan M, Gerard K, Amaya-Amaya M. Discrete choice experiments in a nutshell. In: Ryan M, Gerard K, Amaya-Amaya M, editors. Using Discrete Choice Experiments to Value Health and Health Care. Dordrecht, The Netherlands: Springer Netherlands; 2008. pp. 13–46.

## Associated Data

### Supplementary Materials

Sample EQ-5D-3L questionnaire, English.

Sample EQ-5D-5L questionnaire, English.

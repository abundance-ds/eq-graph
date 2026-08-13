---
project_id: "2016170"
work_id: "doi:10.1007/s40273-018-0642-5"
doi: "10.1007/s40273-018-0642-5"
pmid: "29572719"
pmcid: "PMC5954044"
title: "A Systematic Review of Studies Comparing the Measurement Properties of the Three-Level and Five-Level Versions of the EQ-5D"
journal: "Pharmacoeconomics"
publication_date: "2018-03-23"
volume: "36"
issue: "6"
authors:
  - name: "Ines Buchholz"
    orcid: "http://orcid.org/0000-0001-9729-6992"
    affiliation_ids:
      - "Aff1"
  - name: "Mathieu F. Janssen"
    affiliation_ids:
      - "Aff2"
  - name: "Thomas Kohlmann"
    affiliation_ids:
      - "Aff1"
  - name: "You-Shan Feng"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.5603.0Institute for Community Medicine, University Medicine of Greifswald, Greifswald, Germany"
  - id: "Aff2"
    name: "000000040459992Xgrid.5645.2Department of Medical Psychology and Psychotherapy, Erasmus MC, Rotterdam, The Netherlands"
licence: "cc-by-nc"
source_file: "input/projects/2016170/papers/doi_10.1007_s40273-018-0642-5.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5954044/fullTextXML"
source_method: "epmc_xml"
source_sha256: "2df1ba58a681b046d1bc46331eff5b461a3938d61840992560601c09e2f7bf3c"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# A Systematic Review of Studies Comparing the Measurement Properties of the Three-Level and Five-Level Versions of the EQ-5D

## Abstract

### Background

Since the introduction of the five-level version of the EQ-5D (5L), many studies have comparatively investigated the measurement properties of the original three-level version (3L) with the 5L version.

### Objective

The aim of this study was to consolidate the available evidence on the performance of both instruments.

### Methods

A systematic literature search of studies in the English and German languages was conducted (2007–January 2018) using the PubMed, EMBASE, and PsycINFO (EBSCO) databases, as well as the EuroQol Research Foundation website. Data were extracted and assessed on missing values, distributional properties, informativity indices (Shannon’s H′ and J′), inconsistencies, responsiveness, and test–retest reliability.

### Results

Twenty-four studies were included in the review. Missing values and floor effects (percentage reporting the worst health state) were found to be negligible for both 3L and 5L (\< 5%). From 18 studies, inconsistencies ranged from 0 to 10.6%, although they were generally well below 5%, with 9 studies reporting the most inconsistencies for Usual Activities (mean percentage 4.1%). Shannon’s indices were always higher for 5L than for 3L, and all but three studies reported lower ceiling effects (‘11111’) for 5L than for 3L. There is mixed and insufficient evidence on responsiveness and test–retest reliability, although results on index values showed better performance for 5L on test–retest reliability.

### Conclusion

Overall, studies showed similar or better measurement properties of the 5L compared with the 3L, and evidence indicated moderately better distributional parameters and substantial improvement in informativity for the 5L compared with the 3L. Insufficient evidence on responsiveness and test–retest reliability implies further research is needed.

### Electronic supplementary material

The online version of this article (10.1007/s40273-018-0642-5) contains supplementary material, which is available to authorized users.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| This review supports the use of both the 3L and the 5L in a broad range of patients, populations and countries. |
| The 5L showed better or at least similar measurement properties when compared to the 3L. |
| Evidence on responsiveness is inconclusive and requires further research. |

</div>

## Introduction

The EQ-5D is one of the most widely used instruments to describe and value health \[1, 2\]. It is a generic, self-completion questionnaire consisting of two parts: a 5-item descriptive system and a thermometer-like visual analogue scale ranging from 0 to 100 (the EQ-VAS). It comprises five items, each describing one dimension \[Mobility (MO), Self-Care (SC), Usual Activities (UA), Pain/Discomfort (PD), and Anxiety/Depression (AD)\]. The original questionnaire, introduced in 1990 \[3\], allows respondents to choose between three options; level 1, representing no problems; level 2, reflecting small or moderate problems; and level 3, indicating extreme problems (or ‘unable to’). Self-ratings on the three levels in the five dimensions (items) can be summarized to produce 243 health states, also known as a health profile. Health profiles can be assigned index values derived from econometric techniques to elicit societal preference weights. These index values can then be used in economic evaluation of health programs \[1, 4\].

The EQ-5D was conceptualized to capture deviations from ‘normal’ health, thereby focusing on self-reported health and health-related quality-of-life problems while not attempting to capture aspects beyond health. Internationally, it is currently one of the most widely used preference-based quality-of-life questionnaires. A large body of literature demonstrates that the instrument is valid and reliable \[5–7\]. However, although the EQ-5D was developed to supplement other instruments, this simple and short measure has been increasingly used as a ‘stand-alone tool’ \[8, 9\]. The increase in use of the EQ-5D in the field of health technology assessment raises concerns about methodological measurement issues \[10\]. The first is the EQ-5D’s ceiling effect, or a high proportion of participants reporting ‘no problems’ on one or all dimensions \[11–13\]. Second, some studies found the EQ-5D to be less responsive to changes in health compared with other preference-based measures \[e.g. Health Utility Index (HUI), Short-Form 6-Dimension (SF-6D), Quality of Well-Being Scale–Self Administered (QWB-SA)\] \[14–21\]. To address these concerns, paired with the inherent aspiration of the ever-expanding research community to continually improve the instrument, a new version of the EQ-5D was developed by the EuroQol group \[22–24\]. The new version expanded the response choices from three to five levels and changed the wording of some of the response categories (Table <a href="#Tab1" data-ref-type="table">1</a>). The new version is called the EQ-5D-5L \[25\], and can describe 3125 (= 5<sup>5</sup>) health conditions.

<div id="Tab1" class="table-wrap">

<div class="caption">

Response levels of the EQ-5D-3L and EQ-5D-5L

</div>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">3L</th>
<th colspan="2" style="text-align: left;">5L</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">No problems</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">No problems</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">Slight problems</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">Some/moderate problems</td>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">Moderate problems</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">Severe problems</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">Extreme problems/unable to</td>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">Extreme problems/unable to</td>
</tr>
</tbody>
</table>

When expanding from the 3L to the 5L, some of the wording of response categories was changed. The most significant was that level 3 mobility of the 3L was changed from ‘confined to bed’ to ‘unable to walk about’ for level 5 of the 5L \[24\]

</div>

Since introducing the EQ-5D-5L in 2011, many studies have comparatively investigated the measurement properties of the original EQ-5D (now interchangeably referred to as EQ-5D-3L or 3L) and the newer EQ-5D-5L (now interchangeably referred to as EQ-5D-5L or 5L). In this review we summarize the consolidated findings from these studies.

## Methods

### Data Sources, Search Strategy, Study Selection, and Inclusion and Exclusion Criteria

We conducted a systematic literature search to identify all studies in the English and German languages comparing the 3L and the 5L published between January 2007 and May 2016 using the following keywords: ‘EQ-5D-5L’, ‘EQ-5D 5L’, ‘EuroQol AND 5L’, ‘EuroQoL AND 5 level’. Electronic searches were performed in the PubMed, EMBASE, and PsycINFO (EBSCO) databases, in addition to the EuroQol Research Foundation website, for relevant publications. The inclusion criteria were primary study or conference paper comparing the final versions of the 3L and the 5L(studies using experimental versions were excluded). Articles were further excluded if they did not assess the EQ-5D, were of another publication type, it was not an empirical study in adults, were not in English or German, or were not available in full text. The review was updated during the process of manuscript revision using the same search algorithms, and inclusion and exclusion/eligibility criteria as detailed above. The search was conducted in articles published between May 2016 and January 2018. The process of study selection is shown in Fig. <a href="#Fig1" data-ref-type="fig">1</a>.

<figure id="Fig1">
<p><img src="40273_2018_642_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Literature search and selection process</figcaption>
</figure>

### Screening and Data Extraction

Two researchers independently reviewed the title and abstract of all identified studies, while a third reviewer (TK or MFJ) was consulted in case of variance. After removing duplicates, full-text articles were reviewed by one reviewer (IB) and doubled-checked by the second reviewer (YSF) for missing extractions. For cases of papers that used the same data, those with more information on the indicators of interest were always included. When publications addressed different information based on the same data, both papers were included. For each article, the following information was extracted: authors, title and year of publication, sample characteristics (e.g. sample size, percentage of females, mean age), country, outcome measures used, aims of the study, study design, and parameters describing relevant measure properties. The measurement properties were distributional properties, informativity, inconsistencies, responsiveness and test–retest reliability. All of these properties were assessed in terms of results related to the descriptive systems of the 3L and 5L. For responsiveness and test–retest reliability, results on index values were also included.

### Quality Assessment of Studies

The quality of the full-text articles included for review was assessed using a 9-item critical appraisal tool (see the electronic supplementary material \[ESM\]). The items were defined based on the ‘Quality Assessment Tool for Observational Cohort and Cross-Sectional Studies’ from the National Heart, Lung, and Blood Institute (NHLBI) \[26\], and contained (1) objective/research questions; (2) study population; (3) groups recruited/eligibility criteria; (4) study design; (5) sample size; (6) response rate; (7) data collection; (8) outcome parameter; and (9) statistical tests/analysis. Study quality was assessed as excellent, good, fair or poor, with the corresponding number of criteria fulfilled being 8–9, 5–7, 3–4 or 0–2.

### Distributional Properties

We compared the 3L and 5L on their classical distribution characteristics, such as the number and proportion of missing values, the number and percentage reporting the best (ceiling; ‘no problems’) and worst (floor) level of health state in each dimension and across all dimensions (e.g. ‘11111’ and ‘33333’ for the 3L or ‘55555’ for the 5L, respectively). The results are presented as ranges of percentages or numbers of studies in which the 5L performed equal to, worse than, or better than the 3L (e.g. How often did more than 15% \[as suggested by Terwee et al. \[27\]\] of the study sample report ‘no problems’ when using the 5L compared with the 3L?) We used random effects logit transformation to calculate pooled proportions from single proportions using R’s ‘meta’ package specifically for proportion reporting ‘no problems’ across all dimensions (‘11111’). Pooled proportions give an idea of the overall ceiling effect when taking into account the sample sizes across included studies.

### Informativity

Shannon’s index is based on information theory and allows an assessment on the informational and discriminatory power of each descriptive system.

According to Shannon’s indices, an item is most efficiently used when all responses are evenly distributed across all response options \[28\], with a higher index indicating more information captured by the instrument. While H′ represents the extent to which the information is evenly distributed across all categories, Shannon’s J′ additionally takes into account the number of response options or descriptive categories of the measurement system. J′ can take values between 0 and 1, with a J′ of 0 representing that all responses are concentrated in one response level (most uneven distribution; worst discriminatory power) and 1 representing that all response levels are evenly distributed (even distribution; best discriminatory power). There is no straightforward interpretation for H′. Since H′max depends on the number of levels, within our context H′ can take values between 0 (no informational richness/discriminatory power) and 1.58 (*log*<sub>2</sub>*L*, with the number of levels *L* = 3) for the 3L and 2.32 (*log*<sub>2</sub>*L*, with *L* = 5) for the 5L (which corresponds to the highest informational richness/discriminatory power).

Within this review, H′ and J′ were extracted from the studies or calculated using these formulas, where *p*<sub>*i*</sub> is the proportion of responses in the i<sup>th</sup> response option:
``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$H^{\prime} = - \mathop \sum \limits_{i = 1}^{L} \left( {p_{i} \log_{2} p_{i} } \right)$$\end{document}
```
``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$J^{\prime} = \frac{H'}{H'\hbox{max} }$$\end{document}
```

Both indices are reported for each EQ-5D dimension. We aggregated the mean information gain by the 5L, which was calculated through dividing Shannon’s H′ of the 5L by Shannon’s H′ of the 3L (H′<sub>5L</sub>/H′<sub>3L</sub>) and Shannon’s J′ for the 5L by Shannon’s J′ for the 3L (J′<sub>5L</sub>/J′<sub>3L</sub>), respectively, with H′/J′ ≥1 showing the 5L descriptive classification system to be more informative than the 3L.

### Inconsistencies

Due to the two additional response levels, we expect a redistribution that can be quantified with the help of the parameters already described (i.e. classical distribution properties on the one hand and Shannon’s indices on the other). In order to assess whether this redistribution of responses is conclusive in terms of content, we also considered inconsistent responses, as defined by Janssen et al. \[8\], as a qualitative distribution parameter, or if, and to what degree, 3L and 5L response pairs differ from each other. Operationally, we (1) transformed the 3L response levels 1, 2 and 3 to 5L response levels 1, 3 and 5 to calculate (2) the size of difference of corresponding responses. Paired responses differing more than one level were defined as ‘inconsistent’, with a size of inconsistency ranging from 1 to 3. All studies included in the review used the methods of Janssen et al. \[8\] to calculate inconsistencies.

We report and compare the percentage of inconsistencies by dimension, the range of percentage of inconsistencies by dimension, and the total number and average of inconsistencies. Notwithstanding the fact that the mere presence of inconsistent responses does not provide any information about the underlying causes, their consideration is of particular interest when they occur systematically, e.g. only in certain patient groups, which could affect validity, responsiveness and reliability.

### Responsiveness

To evaluate how the instruments capture changes in health over time, we collected all reported distribution-based effect sizes (ESs), such as the standardized ES and the standardized response mean (SRM), and non-parametric test statistics, such as the Wilcoxon signed-rank order test or the probability of superiority (PS) as defined by Grissom and Kim \[29\]. The ES is the mean change divided by the standard deviation of the baseline measurement. It disregards the variation in change which is considered by the SRM (the ratio of the mean change to the standard deviation of the change). The Wilcoxon test is the non-parametric equivalent of the *t*-test for dependent samples and is applied when the prerequisites for a parametric procedure are not met.

### Test–Retest Reliability

Several methods can determine whether a measurement tool consistently produces the same results if the attribute of interest remains stable \[30, 31\]. We extracted and summarized any reported information regarding the magnitude of agreement of data collected at two points in time: intraclass correlation coefficients (ICCs), Cohen’s Kappa (κ), weighted Kappa (<sub>w</sub>κ), and percentage of agreement (POA).

An ICC quantifies the dependency of interval-scaled data pairs if the order of measurement is negligible. Values range from -1 to 1 with values less than 0 indicating a reliability of 0 and values higher or equal to 0.70 indicating good reliability \[32\].

κ is the most widely used measure to assess the agreement for categorical data \[33\]; it measures the random corrected degree of agreement between two ratings. In contrast to the simple percentage of agreement of two ratings, it considers that ratings will sometimes agree or disagree by chance. When additionally taking into account the size of the deviation (one vs. several categories) within ordinal-scaled data (such as the EQ-5D responses), calculating <sub>w</sub>κ is indicated \[34\]. Kappa is 1 if two ratings perfectly match, and 0 when agreement equals chance. Kappa is negative if the match is poorer than chance \[35\]. Note that a <sub>w</sub>κ using quadratic weights is one type of ICC. Based on the Guidelines for Reporting Reliability and Agreement Studies (GRRAS), a κ \> 0.40 and ICCs \>0.6 were considered acceptable \[30\].

## Results

Of the 497 studies identified from the search, 215 were selected for full-text review based on title and abstract screening. Of those, 190 did not meet the inclusion criteria and were excluded. The remaining 20 articles that compared methodical properties of the official versions of the 3L and 5L were included in the review (Fig. <a href="#Fig1" data-ref-type="fig">1</a> \[36–59\]). An update carried out in the course of the manuscript revision resulted in a further four hits, therefore the final review is based on a total of 24 articles. All papers were of good to excellent quality (see the ESM).

The sample size of the included articles ranged from 50 to 7294 for the 3L, and 50 to 6800 for the 5L (Table <a href="#Tab2" data-ref-type="table">2</a>). Data were collected in 18 different countries in the following settings: general population (8 studies) and patient populations (16 studies). All but two studies directly compared the 3L and the 5L (head-to-head, i.e. the same respondents completed both the 3L and 5L questionnaires). In head-to-head comparison studies, the 5L was administered before the 3L (Table <a href="#Tab3" data-ref-type="table">3</a>). Two of the crossover studies (i.e. studies that randomized the administration order of the 3L and 5L) reported that order of administration had no influence on response trends \[37, 43\].

<div id="Tab2" class="table-wrap">

<div class="caption">

Characteristics of the studies included in this systematic review

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Reference, year</th>
<th style="text-align: left;">Country</th>
<th style="text-align: left;">Sample size [<em>n</em>]<br />
(response rate)</th>
<th style="text-align: left;">Setting</th>
<th style="text-align: left;">Patient population</th>
<th style="text-align: left;">Percentage of women</th>
<th style="text-align: left;">Mean age ± SD (range) in years</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Agborsangaya et al. 2014 [<span class="citation" data-cites="CR36">36</span>]</td>
<td style="text-align: left;">Canada</td>
<td style="text-align: left;"><em>n</em><sub>3L</sub> = 4946 (98.7%)<br />
<em>n</em><sub>5L</sub> = 4752 (98.9%)</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">Respondents of two consecutive survey cycles of the Health Quality Council of Alberta Patient Experience and Satisfaction Survey for 2010 and 2012</td>
<td style="text-align: left;">3L: 52.3<br />
5L: 55.7</td>
<td style="text-align: left;">3L: 46.6 ± 16.5<br />
5L: 47.7 ± 17.1</td>
</tr>
<tr>
<td style="text-align: left;">Buchholz et al. 2015 [<span class="citation" data-cites="CR37">37</span>]</td>
<td style="text-align: left;">Germany</td>
<td style="text-align: left;"><em>n</em><sub>t1</sub> = 230, <em>n</em><sub>t2</sub> = 224, <em>n</em><sub>t3</sub> = 154 (NA)</td>
<td style="text-align: left;">Inpatient rehabilitation</td>
<td style="text-align: left;"><em>n</em> = 114 orthopedic, <em>n</em> = 54 psychosomatic, <em>n</em> = 62 rheumatologic inpatient rehabilitation patients</td>
<td style="text-align: left;">69.6</td>
<td style="text-align: left;">57 ± 12 (26–86)</td>
</tr>
<tr>
<td style="text-align: left;">Conner-Spady et al. 2015 [<span class="citation" data-cites="CR38">38</span>]</td>
<td style="text-align: left;">Canada</td>
<td style="text-align: left;">176 (58%)</td>
<td style="text-align: left;">Orthopedic</td>
<td style="text-align: left;">Patients with osteoarthritis who were referred to an orthopedic surgeon for total joint replacement</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">65 ± 11 (25–88)</td>
</tr>
<tr>
<td style="text-align: left;">Craig et al. 2014 [<span class="citation" data-cites="CR39">39</span>]</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">2614 (91%)</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">Patients with chronic conditions (national representative adult population sample)</td>
<td style="text-align: left;">49</td>
<td style="text-align: left;">NR</td>
</tr>
<tr>
<td style="text-align: left;">Feng et al. 2015 [<span class="citation" data-cites="CR40">40</span>]</td>
<td style="text-align: left;">England</td>
<td style="text-align: left;">3L: 7294 (64%)<br />
5L: 996 (50%)</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">3L: participants were included in the 2012 Health Survey for England, and patients were included in the EQ-5D-5L valuation study, selected at random from residential post codes</td>
<td style="text-align: left;">3L: 55.6<br />
5L: 59.3</td>
<td style="text-align: left;">NR</td>
</tr>
<tr>
<td style="text-align: left;">Ferreira et al. 2016 [<span class="citation" data-cites="CR56">56</span>]</td>
<td style="text-align: left;">Portugal</td>
<td style="text-align: left;">624 (NR)</td>
<td style="text-align: left;">Young general population</td>
<td style="text-align: left;">(Under-) graduate students from two Portuguese universities aged ≤30 years</td>
<td style="text-align: left;">60.4</td>
<td style="text-align: left;">21.7 ± 3.2</td>
</tr>
<tr>
<td style="text-align: left;">Golicki et al. 2015a [<span class="citation" data-cites="CR41">41</span>]</td>
<td style="text-align: left;">Poland</td>
<td style="text-align: left;">408 (NR)</td>
<td style="text-align: left;">Patients during index hospitalization (stroke)</td>
<td style="text-align: left;">Acute stroke patients (types: subarachnoid hemorrhage, <em>n</em> = 8; intracerebral hemorrhage, <em>n</em> = 39; cerebral infarction, <em>n</em> = 353; stroke, not specified, <em>n</em> = 4)</td>
<td style="text-align: left;">48.5</td>
<td style="text-align: left;">69.0 ± 12.9 (23–98)</td>
</tr>
<tr>
<td style="text-align: left;">Golicki et al. 2015b [<span class="citation" data-cites="CR42">42</span>]</td>
<td style="text-align: left;">Poland</td>
<td style="text-align: left;">114 (NR)</td>
<td style="text-align: left;">Hospitalized patients at 1 week and 4 months poststroke</td>
<td style="text-align: left;">Patients with primary or recurrent stroke: 93% ischemic stroke, many comorbidities (72% hypertension, 25% diabetes, 31% coronary artery disease)</td>
<td style="text-align: left;">51.8</td>
<td style="text-align: left;">70.6 ± 11.0 (39–88)</td>
</tr>
<tr>
<td style="text-align: left;">Greene et al. 2014 [<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;"><em>n</em><sub>t1</sub> = 50 (79%)<br />
<em>n</em><sub>t2</sub> = 77 (80%)</td>
<td style="text-align: left;">Orthopedic</td>
<td style="text-align: left;">Patients with hip pain and never had a hip arthroplasty undergoing their first total hip replacement</td>
<td style="text-align: left;">NR</td>
<td style="text-align: left;">t<sub>1</sub>: 63 ± 13 (NR)<br />
t<sub>2</sub>: 66 ± 10 (NR)</td>
</tr>
<tr>
<td style="text-align: left;">Janssen et al. 2013 [<span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;">DK, UK, NL, PL, I, SCO</td>
<td style="text-align: left;">3919 (NA)</td>
<td style="text-align: left;">Mixed</td>
<td style="text-align: left;">COPD/asthma (<em>n</em> = 342), depression (<em>n</em> = 250), diabetes (<em>n</em> = 284), liver disease (<em>n</em> = 645), personality disorders (<em>n</em> = 384), rheumatoid arthritis/arthritis (<em>n</em> = 372), stroke (<em>n</em> = 614), students (<em>n</em> = 443)</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">51.9 ± 20 (18–NR)</td>
</tr>
<tr>
<td style="text-align: left;">Jia et al. 2014 [<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;">China</td>
<td style="text-align: left;"><em>n</em><sub>t1</sub> = 369 outpatients (34.7%) and 276 inpatients (62.0%)<br />
<em>n</em><sub>t2</sub> = 183 inpatients (66.3%)</td>
<td style="text-align: left;">Clinical (hospital for infectious diseases)</td>
<td style="text-align: left;">Patients with liver diseases</td>
<td style="text-align: left;">25.0</td>
<td style="text-align: left;">43.9 ± NR (NR)</td>
</tr>
<tr>
<td style="text-align: left;">Khan et al. 2016 [<span class="citation" data-cites="CR46">46</span>]</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;"><em>n</em><sub>t1</sub> = 97 (99%)<br />
<em>n</em><sub>t2</sub> = 78 (79%)<br />
<em>n</em><sub>t3</sub> = 41 (55%)</td>
<td style="text-align: left;">Clinical</td>
<td style="text-align: left;">Single cohort, prospective (non-interventional) follow-up study in non-small cell lung cancer patients</td>
<td style="text-align: left;">44</td>
<td style="text-align: left;">NR (39–86)</td>
</tr>
<tr>
<td style="text-align: left;">Kim et al. 2013 [<span class="citation" data-cites="CR47">47</span>]</td>
<td style="text-align: left;">South Korea</td>
<td style="text-align: left;"><em>n</em><sub>t1</sub> = 600<br />
<em>n</em><sub>t2</sub> = 100</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">Nationally representative general population</td>
<td style="text-align: left;">t1: 50.5<br />
t2: 49.0</td>
<td style="text-align: left;">t<sub>1</sub>: 44.9 ± 15.3 (19–88)<br />
t<sub>2</sub>: 45.3 ± 15.8 (19–88)</td>
</tr>
<tr>
<td style="text-align: left;">Kim et al. 2012 [<span class="citation" data-cites="CR48">48</span>]</td>
<td style="text-align: left;">South Korea</td>
<td style="text-align: left;"><em>n</em><sub>t1</sub> = 893 (38.5%)<br />
<em>n</em><sub>t2</sub> = 78 (31.2)</td>
<td style="text-align: left;">Ambulatory cancer centre</td>
<td style="text-align: left;">Patients receiving chemotherapy over a 1-month period</td>
<td style="text-align: left;">t1: 56.8<br />
t2: 56.4</td>
<td style="text-align: left;">t<sub>1</sub>: 53.0 ± 11.2<br />
t<sub>2</sub>: 53.9 ± 10.9</td>
</tr>
<tr>
<td style="text-align: left;">Pan et al. 2015 [<span class="citation" data-cites="CR49">49</span>]</td>
<td style="text-align: left;">China</td>
<td style="text-align: left;">289 (96.3%)</td>
<td style="text-align: left;">Hospitalized outpatients</td>
<td style="text-align: left;">Diabetes mellitus type II patients with and without clinical conditions (47% retinopathy, 37.7% neuropathy, 31.8% arthritis, 24.6% dermopathy, 19.7% heart disease)</td>
<td style="text-align: left;">69.5</td>
<td style="text-align: left;">64.9 ± 9.1 (NR)</td>
</tr>
<tr>
<td style="text-align: left;">Pattanaphesaj et al. 2015 [<span class="citation" data-cites="CR50">50</span>]</td>
<td style="text-align: left;">Thailand</td>
<td style="text-align: left;">117 (NR)</td>
<td style="text-align: left;">Clinical</td>
<td style="text-align: left;">Diabetes mellitus patients treated with insulin (54.7% type 2, 45.3% type 1)</td>
<td style="text-align: left;">62.4</td>
<td style="text-align: left;">45 ± NR (aged ≥12 years)</td>
</tr>
<tr>
<td style="text-align: left;">Poór et al. 2017 [<span class="citation" data-cites="CR57">57</span>]</td>
<td style="text-align: left;">Hungary</td>
<td style="text-align: left;">238 (NA)</td>
<td style="text-align: left;">Clinical; academic dermatology clinic</td>
<td style="text-align: left;">Inpatient and outpatient (88.7%) psoriatic patients; 73.1% diagnosed with a moderate-to-severe psoriasis; mean disease duration: 18.1 years (3 months to 52 years)</td>
<td style="text-align: left;">37.4</td>
<td style="text-align: left;">47.4 ± 15.2 (NR)</td>
</tr>
<tr>
<td style="text-align: left;">Scalone et al. 2011 [<span class="citation" data-cites="CR51">51</span>]</td>
<td style="text-align: left;">Italy</td>
<td style="text-align: left;">426 (NA)</td>
<td style="text-align: left;">Clinical</td>
<td style="text-align: left;">Chronic hepatitis C (25.4%), chronic hepatitis B (22.5%), cirrhosis (20.9%), liver transplantation (19.0%), and other chronic hepatic diseases</td>
<td style="text-align: left;">31</td>
<td style="text-align: left;">NR (19–84)</td>
</tr>
<tr>
<td style="text-align: left;">Scalone et al. 2013 [<span class="citation" data-cites="CR52">52</span>]</td>
<td style="text-align: left;">Italy</td>
<td style="text-align: left;">1088 (NA)</td>
<td style="text-align: left;">Clinical</td>
<td style="text-align: left;">Liver diseases</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">59 ± (18–89)</td>
</tr>
<tr>
<td style="text-align: left;">Scalone et al. 2015 [<span class="citation" data-cites="CR53">53</span>]</td>
<td style="text-align: left;">Italy</td>
<td style="text-align: left;">6800 (NA)</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">Representative sample</td>
<td style="text-align: left;">52.0</td>
<td style="text-align: left;">51.9 ± 17.6 (18–101)</td>
</tr>
<tr>
<td style="text-align: left;">Shiroiwa et al. 2015 [<span class="citation" data-cites="CR54">54</span>]</td>
<td style="text-align: left;">Japan</td>
<td style="text-align: left;">1143 (NA)</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">The study oversampled younger people due to sampling design</td>
<td style="text-align: left;">51.2</td>
<td style="text-align: left;">NR</td>
</tr>
<tr>
<td style="text-align: left;">Wang et al. 2016 [<span class="citation" data-cites="CR55">55</span>]</td>
<td style="text-align: left;">Singapore</td>
<td style="text-align: left;">121 (NA)</td>
<td style="text-align: left;">Diabetes clinic of a tertiary hospital</td>
<td style="text-align: left;">Outpatients with type 2 diabetes mellitus</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">55.5 ± 12.7</td>
</tr>
<tr>
<td style="text-align: left;">Yfantopoulos et al. 2017a [<span class="citation" data-cites="CR58">58</span>]</td>
<td style="text-align: left;">Greece</td>
<td style="text-align: left;">2279 (22.5)</td>
<td style="text-align: left;">General population</td>
<td style="text-align: left;">Middle-aged and elderly general population</td>
<td style="text-align: left;">52.1</td>
<td style="text-align: left;">57.3 ± 12.4</td>
</tr>
<tr>
<td style="text-align: left;">Yfantopoulos et al. 2017b [<span class="citation" data-cites="CR59">59</span>]</td>
<td style="text-align: left;">Greece</td>
<td style="text-align: left;">396 (NR)</td>
<td style="text-align: left;">Clinical; 16 private practicing centers</td>
<td style="text-align: left;">Psoriatic patients who were to initiate treatment with calcipotriol plus betamethasone dipropionate in a fixed gel combination under routine clinical practice; 34.6% mild psoriasis, 52.8% moderate psoriasis</td>
<td style="text-align: left;">39.9</td>
<td style="text-align: left;">52.0 ± 16.5</td>
</tr>
</tbody>
</table>

*NR* not reported, *NA* not applicable, *SD* standard deviation, *n* sample size, *n*<sub>*3L*</sub> sample size reported for the 3L, *n*<sub>*5L*</sub> sample size reported for the 5L, *n*<sub>*t1*</sub> sample size reported for baseline, *n*<sub>*t2*</sub> sample size reported for the first follow-up, *n*<sub>*t3*</sub> sample size reported for the second follow-up, *t*<sub>*1*</sub> baseline, *t*<sub>*2*</sub> first follow-up, *COPD* chronic obstructive pulmonary disease, *DK* Denmark, *UK* United Kingdom, *NL* The Netherlands, *PL* Poland, *I* Italy, *SCO* Scotland, *US* United States

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

Study design and type of questionnaire administration of the studies included in this systematic review

</div>

| Reference, year | Study design | Mode of questionnaire administration | Order of administration | Type of comparison |
|----|----|----|----|----|
| Agborsangaya et al. 2014 \[36\] | Cross-sectional | Telephone-based questionnaire administered by random-digit dialing | NA | Indirect |
| Buchholz et al. 2015 \[37\] | Longitudinal multicenter study | Self-complete version on paper | Crossover | Head-to-head |
| Conner-Spady et al. 2015 \[38\] | Longitudinal multicenter | Self-complete version on paper | 5L first | Head-to-head |
| Craig et al. 2014 \[39\] | Cross-sectional | Web survey/online data collection | Random | Head-to-head |
| Feng et al. 2015 \[40\] | Value set study for England; Health Survey for England | Face-to-face, computer-assisted interviews | NA | Indirect |
| Ferreira et al. 2016 \[56\] | Convenience sample | Self-complete version on paper | 5L first | Head-to-head |
| Golicki et al. 2015a \[41\] | Cross-sectional | Self-complete version on paper<sup>a</sup> | NR | Head-to-head |
| Golicki et al. 2015b \[42\] | Single-center, observational, longitudinal cohort study | Self-complete version on paper | NR | Head-to-head |
| Greene et al. 2014 \[43\] | Prospective | First survey: paper-based; second survey: online or on paper | Crossover | Head-to-head |
| Janssen et al. 2013 \[44\] | Multicountry study | Paper and pencil in all countries except England (online) | 5L first | Head-to-head |
| Jia et al. 2014 \[45\] | Cross-sectional | Self-complete version on paper | 5L first | Head-to-head |
| Khan et al. 2016 \[46\] | Single cohort, prospective, non-interventional follow-up study | NR | 3L and 5L were assessed at least 1 week apart to avoid potential for ‘carry over’ | Head-to-head |
| Kim et al. 2013 \[47\] | Cross-sectional | In-person interviews | 5L first | Head-to-head |
| Kim et al. 2012 \[48\] | Consecutive sample of patients | Self-complete version on paper | 5L first | Head-to-head |
| Pan et al. 2015 \[49\] | Consecutive sample of patients | Self-complete version on paper | 5L first | Head-to-head |
| Pattanaphesaj et al. 2015 \[50\] | Convenience sample of patients | Self-complete version on paper | 3L (right column) and 5L (left) on the same page | Head-to-head |
| Poór et al. 2017 \[57\] | Cross-sectional | Self-complete version on paper | 5L first | Head-to-head |
| Scalone et al. 2011 \[51\] | Naturalistic multicenter cost-of-illness study | Self-complete version on paper | 5L first | Head-to-head |
| Scalone et al. 2013 \[52\] | Naturalistic multicenter cost-of-illness study | Self-complete version on paper | 5L first | Head-to-head |
| Scalone et al. 2015 \[53\] | Large-scale telephone survey | Telephone interview | Crossover | Head-to-head |
| Shiroiwa et al. 2015 \[54\] | Register study | Door-to-door survey (mode of administration: self-complete version on paper) | 5L first | Head-to-head |
| Wang et al. 2016 \[55\] | Consecutive sample of patients | Self-complete version on paper | 5L first | Head-to-head |
| Yfantopoulos et al. 2017a \[58\] | Observational survey | Self-complete version on paper | Random | Head-to-head |
| Yfantopoulos et al. 2017b \[59\] | Multicenter, prospective study | Self-complete version on paper | Random | Head-to-head |

*NA* not applicable *NR* not reported, *crossover* half of the sample started with the 3L/5L

<sup>a</sup>In case of aphasia or dementia, the survey was completed by a family member (as a proxy respondent)

</div>

### Missing Values and Distributional Properties

Fifteen studies reported missing values below 5% for both 3L (range for the dimensions: 0–1.9%; range for the profile: 0–6.6%) and 5L (range for the dimensions: 0–1.6%; range of the profile: 0–4.0%). One study found 8.5% left the 5L blank and 0.8% left the 3L blank entirely, which is probably due to the methodology of how the 3L is first presented in this study \[52\]. Floor effects by dimension were reported in 19 studies and were almost always below 5% (3L: 0–26.1%; 5L: 0–6.5%) \[Table <a href="#Tab4" data-ref-type="table">4</a>\]. Mean absolute reduction in floor effects ranged from 0.16 percentage points (Usual Activities) to 4.18 percentage points (Pain/Discomfort). For the profile, floor effects ranged from 0 to 2.7% for the 3L and 0 to 1.8% for the 5L (five studies).

<div id="Tab4" class="table-wrap">

<div class="caption">

Results of the floor and ceiling effects

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">‘33333’/<br />
‘55555’</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>Floor</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Range of floor effects for the 3L (%)</td>
<td style="text-align: left;">0–3.8</td>
<td style="text-align: left;">0–4.9</td>
<td style="text-align: left;">0–10.9</td>
<td style="text-align: left;">0–26.1</td>
<td style="text-align: left;">0–7.3</td>
<td style="text-align: left;">0–2.7</td>
</tr>
<tr>
<td style="text-align: left;"> Range of floor effects for the 5L (%)</td>
<td style="text-align: left;">0–3.0</td>
<td style="text-align: left;">0–3.7</td>
<td style="text-align: left;">0–6.5</td>
<td style="text-align: left;">0–5.7</td>
<td style="text-align: left;">0–2.5</td>
<td style="text-align: left;">0–1.8</td>
</tr>
<tr>
<td style="text-align: left;"> Range of absolute reduction in floor effects (percentage points)</td>
<td style="text-align: left;">−0.9 to 1.7</td>
<td style="text-align: left;">−0.3 to 1.2</td>
<td style="text-align: left;">−1.7 to 6.3</td>
<td style="text-align: left;">0–20.4</td>
<td style="text-align: left;">0–4.8</td>
<td style="text-align: left;">0–0.9</td>
</tr>
<tr>
<td style="text-align: left;"> Mean absolute reduction in floor effects (percentage points)</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">1.43</td>
<td style="text-align: left;">4.29</td>
<td style="text-align: left;">1.64</td>
<td style="text-align: left;">0.21</td>
</tr>
<tr>
<td style="text-align: left;"> Number of studies reporting on floor effects</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">5</td>
</tr>
<tr>
<td style="text-align: left;"> Number of studies reporting lower floor effects for the 5L than for the 3L</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">3</td>
</tr>
</tbody>
</table>

|  | MO | SC | UA | PD | AD | ‘11111’ |
|----|----|----|----|----|----|----|
| *Ceiling* |  |  |  |  |  |  |
|  Range of ceiling effects for the 3L (%) | 10.2–97.7 | 61.4–99.5 | 10.8–94.8 | 2.3–80.3 | 24.5–88.0 | 0.6–68.0 |
|  Range of ceiling effects for the 5L (%) | 4.0–96.5 | 60.2–99.5 | 9.1–93.1 | 0.6–71.2 | 17.9–82.0 | 0–55.0 |
|  Range of absolute reduction in ceiling effects (percentage points) | −0.25 to 16.9 | −1.3 to 30.0 | 0.8–21.3 | 1.5–20.0 | −3.4 to 19.7 | −0.5 to 16.7 |
|  Mean absolute reduction in ceiling effects (percentage points) | 5.73 | 4.15 | 4.88 | 6.77 | 6.17 | 6.50 |
|  Number of studies reporting on ceiling effects | 20 | 20 | 20 | 20 | 20 | 22 |
|  Number of studies reporting lower ceiling effects for the 5L than for the 3L | 19 | 16 | 20 | 20 | 18 | 19 |
|  Number of studies reporting \<15% ceiling for the 3L/5L | 1/2 | 0/0 | 1/2 | 3/3 | 0/0 | 7/8 |

The absolute reduction in floor effects was calculated by subtracting the number or percentage of the reported highest level of problems/‘55555’ for the 5L by the number or percentage of the reported highest level of problems/‘33333’ for the 3L, respectively. The absolute reduction in ceiling effects was calculated by subtracting the number or percentage of reported ‘no problems’/‘11111’ for the 5L by the number or percentage of reported ‘no problems’/‘11111’ for the 3L, respectively

*MO* Mobility, *SC* Self-Care, *UA* Usual Activities, *PD* Pain/Discomfort, *AD* Anxiety/Depression

</div>

All studies reported information on the number or proportion reporting ‘no problems’ in any dimension or for the profile (‘11111’) \[Table <a href="#Tab4" data-ref-type="table">4</a>\]. The percentage reporting ‘no problems’ ranged from 2.3 to 99.5% for the 3L and from 0.6 to 99.5% for the 5L. Using the 5L could reduce ceiling effects up to 16.9 percentage points (Mobility) to 30.0 percentage points (Self-Care). The highest absolute reduction of ceiling effects was found for Self-Care (−1.3 to 30.0 percentage points), followed by Pain/Discomfort (1.5 to 20.0 percentage points), and Anxiety/Depression (−3.4 to 19.7 percentage points). Regarding the profile, full health state profiles were reported for 0.6 to 68.0% of the samples studied with the 3L, compared with 0 to 55.0% of the samples studied with the 5L (Fig. <a href="#Fig2" data-ref-type="fig">2</a>).

<figure id="Fig2">
<p><img src="40273_2018_642_Fig2_HTML.jpg" id="MO4" /></p>
<figcaption>Ceiling for the profile (‘11111’) compared with the 3L and the 5L. <em>f.-up</em> follow-up</figcaption>
</figure>

Figure <a href="#Fig3" data-ref-type="fig">3</a> presents the pooled ceiling effects (proportion reporting ‘11111’) for studies using patient (16 studies) and population (8 studies) samples. The pooled proportion of ceiling in the patient population was 0.23 \[confidence interval (CI) 0.170–0.296\] for 3L and 0.18 (CI 0.131–0.238) for 5L. Furthermore, the pooled proportion of ceiling in population-based studies was 0.53 (CI 0.474–0.593) for 3L, compared with 0.43 (CI 0.369–0.492) for 5L. The pooled proportions did not change substantially when excluding the two studies that did not use direct head-to-head comparisons (3L = 0.55, CI 0.472–0.623; 5L = 0.44, CI 0.367–0.517).

<figure id="Fig3">
<p><img src="40273_2018_642_Fig3_HTML.jpg" id="MO5" /></p>
<figcaption>Ceiling for the profile by sample type: forest plot with study proportions, pooled proportions, and 95% CI of reporting ‘11111’ of the EQ-5D-3L against the EQ-5D-5L<em>. CI</em> confidence interval, <em>P</em> proportion, <em>N</em> sample size, <em>THA</em> total hip arthroplasty, <em>UK</em> United Kingdom, <em>US</em> United States</figcaption>
</figure>

### Informativity

Fourteen studies provided information on Shannon’s H′ and Shannon’s J′. In general, Shannon’s H′ was always higher in the 5L than in the 3L, and Shannon’s J′ was higher for the 5L than the 3L, in all but five studies. Across all studies and dimensions, mean Shannon’s H′ ranged from 0.72 to 1.43 for the 5L and from 0.47 to 0.98 for the 3L (Fig. <a href="#Fig4" data-ref-type="fig">4</a>). Mean information gain for Shannon’s H′ (H′<sub>5L</sub>/H′<sub>3L</sub>) ranged from 1.44 for Anxiety/Depression to 1.65 for Mobility. Shannon’s J′ differences between the 3L and the 5L were marginal (Fig. <a href="#Fig4" data-ref-type="fig">4</a>), with a mean information gain (J′<sub>5L</sub>/J′<sub>3L</sub>) ranging from 1.02 for Self-Care to 1.16 for Mobility.

<figure id="Fig4">
<p><img src="40273_2018_642_Fig4_HTML.jpg" id="MO6" /></p>
<figcaption>Shannon’s H′ and J′ for the 3L and the 5L</figcaption>
</figure>

### Inconsistencies

Eighteen studies provided information on inconsistencies. The total number and proportion of inconsistencies were, with four exceptions, well below 5%, ranging from 0 to 10.6% across 18 studies (Fig. <a href="#Fig5" data-ref-type="fig">5</a>). The most inconsistencies were reported for Usual Activities (mean percentage 4.1%), whereas the lowest number of inconsistencies was found for Mobility (2.5%). The total proportion of inconsistencies was lowest (range 0–5.4%) in healthy and chronic populations and highest (range 6–10.6%) in orthopedic settings (Fig. <a href="#Fig5" data-ref-type="fig">5</a>).

<figure id="Fig5">
<p><img src="40273_2018_642_Fig5_HTML.jpg" id="MO7" /></p>
<figcaption>Percentage of inconsistencies by dimension and overall. <em>THR</em> total hip replacement</figcaption>
</figure>

### Responsiveness

Of the three studies analyzing responsiveness, two studies examined the index-level utility scores (using preference-based weights) \[42, 45\], whereas one study assessed responsiveness on the dimensional-level using percentage of improved, stable and deteriorated patients, and PS, a measure defined by Grissom and Kim \[29, 37\]. Distribution-based ES measures were only included in one of these studies \[42\]. In this longitudinal cohort, stroke patients were classified into three groups of improved, stable and deteriorated patients based on two external criteria: the Barthel Index and the modified Rankin Scale. Although both the 3L and the 5L were responsive, showing moderate ES and SRM, the 5L appeared to be (slightly) less responsive than the 3L but more responsive than the EQ-VAS. The other two studies overall found better responsiveness for the 5L compared with the 3L when using non-parametric test statistics in populations of liver disease patients and inpatient rehabilitation patients (Table <a href="#Tab5" data-ref-type="table">5</a>) \[37, 45\]. Importantly, the two studies \[42, 45\] that analyzed the EQ-5D-5L on the index-level estimated index values using the crosswalk method, which maps 3L preference weights onto the 5L responses, which should be considered when interpreting these results.

<div id="Tab5" class="table-wrap">

<div class="caption">

Evidence of studies reporting on responsiveness for the indices or on dimension level

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Reference, year</th>
<th style="text-align: left;">Sample and sample size</th>
<th style="text-align: left;">Effect measure</th>
<th style="text-align: left;">Time interval</th>
<th style="text-align: left;">Value set</th>
<th style="text-align: left;">Evidence</th>
<th style="text-align: left;">Results</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Jia et al. 2014 [<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;">Chinese hepatitis B patients (<em>n</em> = 120)</td>
<td style="text-align: left;">Wilcoxon signed rank-sum test to compare HRQoL before and after 7 days for patients whose doctors reported improved health states (based on laboratory and blood tests)</td>
<td style="text-align: left;">1 week</td>
<td style="text-align: left;">Level of analysis: index values<br />
3L: Japanese TTO-based value set<br />
5L: mapping the interim scoring of the 5L descriptive system to 3L</td>
<td style="text-align: left;">Except two comparisons, 3L tends to be minimally more responsive than the 5L (NS)</td>
<td style="text-align: left;">Increase in HRQoL<br />
∆<sub>3L</sub> = 0.025 to 0.076<br />
∆<sub>5L</sub> = 0.029 to 0.073</td>
</tr>
<tr>
<td style="text-align: left;">Buchholz et al. 2015 [<span class="citation" data-cites="CR37">37</span>]</td>
<td style="text-align: left;">German inpatient rehabilitation patients (n<sub>t1-t2</sub> = 224 and n<sub>t1-t3</sub> = 154)</td>
<td style="text-align: left;">PS (proportion of patients improving from baseline to follow-up; range 0–1, values &gt; 0.5 if more patients improve than deteriorate)</td>
<td style="text-align: left;">t<sub>1:</sub> Beginning, t<sub>2:</sub> End of, t<sub>3:</sub> 3 months after rehabilitation</td>
<td style="text-align: left;">Level of analysis: dimension level</td>
<td style="text-align: left;">5L outperforms 3L within all comparisons</td>
<td style="text-align: left;">PS<sub>5L</sub> = 0.532 (SC) to 0.766 (PD)<br />
PS<sub>3L</sub> = 0.516 (SC) to 0.673 (PD)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Golicki et al. 2015b [<span class="citation" data-cites="CR42">42</span>]</td>
<td rowspan="2" style="text-align: left;">Polish stroke patients (<em>n</em> = 112)</td>
<td style="text-align: left;">ES and SRM for mRS- and BI-based defined groups of deteriorated patients (<em>n</em><sub>mRS</sub> = 19, <em>n</em><sub>BI</sub> = 15) and improved patients (<em>n</em><sub>mRS</sub> = 43, <em>n</em><sub>BI</sub> = 37)</td>
<td rowspan="2" style="text-align: left;">t<sub>1:</sub> 1 week<br />
t<sub>2:</sub> 4 months poststroke</td>
<td rowspan="2" style="text-align: left;">Level of analysis: index values<br />
3L: Polish TTO value set<br />
5L: Polish interim 5L value set estimated using the crosswalk developed by the EuroQol Group</td>
<td style="text-align: left;">In all comparisons, 3L is more responsive than the 5L (NS)</td>
<td style="text-align: left;">Mean 3L index changes were greater than mean 5L index changes:<br />
mean absolute ∆ES<sub>3L-5L</sub> = 0.21<br />
mean absolute ∆SRM<sub>3L-5L</sub> = 0.13</td>
</tr>
<tr>
<td style="text-align: left;">AUROC for 3L and 5L indices</td>
<td style="text-align: left;">The 3L index was systematically more responsive than the 5L</td>
<td style="text-align: left;">mRS-based:<br />
AUROC<sub>3L</sub> = 0.63–0.81<br />
AUROC<sub>5L</sub> = 0.57–0.75<br />
BI-based:<br />
AUROC<sub>3L</sub> = 0.75–0.91<br />
AUROC<sub>5L</sub> = 0.70–0.83</td>
</tr>
</tbody>
</table>

*AUROC* area under the receiver operating characteristic curve, *BI* Barthel Index, *ES* effect size, *HRQoL* health-related quality of life, *mRS* modified Rankin Scale, *n* sample size, *NS* nonsignificant (*p* \> 0.05), *PS* probability of superiority as defined by Grissom and Kim (18), *SRM* standardized response mean, *t*<sub>*1*</sub> baseline, *t*<sub>*2*</sub> first follow-up, *TTO* time trade-off, *SC* self-care, *PD* pain/discomfort

We decided not to report any confidence intervals since they were only reported in one of the three studies

</div>

### Test–Retest Reliability

Six articles studied the reproducibility of the EQ-5D measure, with all but one specifying two or more measures of agreement. ICC was used in all six studies—<sub>w</sub>κ and POA in three studies, and Kappa in two studies. The time interval between repeated measurements varied from 1 to 3 weeks (Table <a href="#Tab6" data-ref-type="table">6</a>). When using ICC, the studies reported moderate to excellent reproducibility for both 3L and 5L index scores, with ICC ranging from 0.52 to 0.83 for the 3L and from 0.69 to 0.93 for the 5L. When using unweighted Kappa, studies reported good to very good agreement (κ<sub>3L</sub> = 0.39–0.93, κ<sub>5L</sub> = 0.36–0.98, mean κ<sub>3L</sub> = 0.692, mean κ<sub>5L</sub> = 0.678), while studies using <sub>w</sub>κ statistics found mostly fair to moderate agreement (<sub>w</sub>κ<sub>3L</sub> = 0.31–0.70, <sub>w</sub>κ<sub>5L</sub> = 0.33–0.69, mean <sub>w</sub>κ<sub>3L</sub> = 0.527, mean <sub>w</sub>κ<sub>5L</sub> = 0.541). There is no clear pattern of better reliability for either the 3L or the 5L. POA was always the same or higher for the 3L when compared with the 5L (POA<sub>3L</sub> = 0.78–0.97, POA<sub>5L</sub> = 0.64–0.97, mean POA<sub>3L</sub> = 0.877, mean POA<sub>5L</sub> = 0.773).

<div id="Tab6" class="table-wrap">

<div class="caption">

Evidence of studies reporting on test–retest reliability (listed by year of publication)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Reference, year</th>
<th rowspan="2" style="text-align: left;">Sample, sample size</th>
<th rowspan="2" style="text-align: left;">Mean time interval</th>
<th rowspan="2" style="text-align: left;">Evidence</th>
<th rowspan="2" style="text-align: left;">Value set</th>
<th colspan="4" style="text-align: left;">Results</th>
</tr>
<tr>
<th style="text-align: left;">ICC (CI)</th>
<th style="text-align: left;">κ</th>
<th style="text-align: left;"><sub>w</sub>κ</th>
<th style="text-align: left;">POA</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Kim et al. 2012 [<span class="citation" data-cites="CR48">48</span>]</td>
<td style="text-align: left;">Korean cancer patients (<em>n</em> = 78)</td>
<td style="text-align: left;">11.5 days (IQR 6–15)</td>
<td style="text-align: left;">Except for UA, fair to good κ in all dimensions, with κ slightly lower and <sub>w</sub>κ slightly higher for the 5L than for the 3L; differences NS<br />
Comparable ICCs</td>
<td style="text-align: left;">3L: South Korean TTO value set<br />
5L: Interim mapping method; crosswalk</td>
<td style="text-align: left;">ICC<sub>3L</sub> = 0.75 (0.63–0.83), ICC<sub>5L</sub> = 0.77 (0.67–0.58)</td>
<td style="text-align: left;">κ<sub>3L</sub> = 0.39 (UA)–0.66 (SC)<br />
κ<sub>5L</sub> = 0.36 (UA)–0.64 (SC)</td>
<td style="text-align: left;"><sub><strong>w</strong></sub>κ<sub>3L</sub> = 0.43 (UA)–0.70 (SC)<br />
<sub><strong>w</strong></sub>κ<sub>5L</sub> = 0.50 (UA)–0.69 (SC)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Kim et al. 2013 [<span class="citation" data-cites="CR47">47</span>]</td>
<td style="text-align: left;">South Koreans from the general population (<em>n</em> = 100)</td>
<td style="text-align: left;">18.7 days (SD 4.5)</td>
<td style="text-align: left;">Good reproducibility of both 3L and 5L, with hardly any differences<br />
3L and 5L obtained comparably good results</td>
<td style="text-align: left;">3L: South Korean TTO value set<br />
5L: Interim value sets from the EuroQol group</td>
<td style="text-align: left;">ICC<sub>3L</sub> = 0.61 (0.46–0.72)<br />
ICC<sub>5L</sub> = 0.75 (0.64–0.83)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><sub>w</sub>κ<sub>3L</sub> = 0.31 (AD)–0.64 (UA) <sub>w</sub>κ<sub>5L</sub> = 0.33 (SC)–0.69 (MO)</td>
<td style="text-align: left;">POA<sub>3L</sub> = 79 (AD)–97 (SC)<br />
POA<sub>5L</sub> = 76 (PD)–97 (SC)</td>
</tr>
<tr>
<td style="text-align: left;">Conner-Spady et al. 2014 [<span class="citation" data-cites="CR38">38</span>]</td>
<td style="text-align: left;">Canadian OA patients referred for hip/knee replacement (<em>n</em> = 176)</td>
<td style="text-align: left;">2 weeks</td>
<td style="text-align: left;">Acceptable reliability for SC and AD (ICC &gt;0.7)<br />
Possible explanation: variability in the frequency and intensity of pain that can occur in patients with OA</td>
<td style="text-align: left;">3L: UK value set<br />
5L: UK value set based on the mapping approach</td>
<td style="text-align: left;">ICC<sub>5L</sub> = 0.61 (MO)–0.77 (AD)<br />
ICC<sub>5L-index</sub> = 0.87 (NR)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">POA: 60 (UA)–76 (AD)</td>
</tr>
<tr>
<td style="text-align: left;">Jia et al. 2014 [<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;">Chinese hepatitis B patients (<em>n</em> = 120)</td>
<td style="text-align: left;">1 week</td>
<td style="text-align: left;">In patients with stable health states, ICC was higher for 5L than for 3L<br />
Mixed evidence for κ in each dimension in patients with stable health states</td>
<td style="text-align: left;">3L: Japanese TTO-based value set<br />
5L: Mapping the interim scoring of the 5L descriptive system to 3L</td>
<td style="text-align: left;">ICC<sub>3L</sub> = 0.83 (0.76–0.89)<br />
ICC<sub>5L</sub> = 0.93 (0.90–0.95)</td>
<td style="text-align: left;">κ<sub>3L</sub> = 0.74 (UA)–0.93 (SC)<br />
κ<sub>5L</sub> = 0.73 (SC)–0.98 (MO)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Pattanaphesaj et al. 2015 [<span class="citation" data-cites="CR50">50</span>]</td>
<td style="text-align: left;">Thai diabetes patients treated with insulin (<em>n</em> = 117)</td>
<td style="text-align: left;">Approximately 14–21 days</td>
<td style="text-align: left;">Excellent reproducibility for both 3L and 5L<br />
5L slightly less reproducible than 3L in all dimensions (probably too long a time distance between the two measurements, which would be in favor of the less well-differentiated 3L)<br />
<sub>w</sub>κ for SC not calculable due to the high ceiling effect</td>
<td style="text-align: left;">3L: Thai value set<br />
5L: Interim mapping generated from the EuroQol group</td>
<td style="text-align: left;">ICC<sub>3L</sub> = 0.64 (0.51–0.74)<br />
ICC<sub>5L</sub> = 0.70 (0.57–0.79)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><sub>w</sub>κ<sub>3L</sub> = 0.39 (UA)–0.70 (MO)<br />
<sub>w</sub>κ<sub>5L</sub> = 0.44 (PD)–0.57 (MO)</td>
<td style="text-align: left;">POA<sub>3L</sub> = 0.78 (PD)–0.98 (SC)<br />
POA<sub>5L</sub> = 0.67 (PD)–0.97 (SC)</td>
</tr>
</tbody>
</table>

*ICC* intraclass correlation coefficient (two-way random effects, absolute agreement, single measure), ICC \>0.60 acceptable, *POA* percentage of agreement, *κ* Cohens’s kappa, κ \>0.40 acceptable, <sub>*w*</sub>*κ* weighted Kappa, *CI* 95% confidence interval, *NR* not reported, *SD* standard deviation, *n* sample size, *MO* mobility, *SC* self-care, *UA* usual activities *PD* pain/discomfort *AD* anxiety/depression, *TTO* time trade-off, *UK* United Kingdom, *OA* osteoarthritis, *IQR* interquartile range, *NS* nonsignificant

</div>

## Discussion

The EQ-5D-5L was developed to improve the discriminative and evaluative properties of the EQ-5D-3L. Since publication of the 5L, a body of evidence has emerged that allows us to determine whether it has improved upon those properties. This review systematically summarizes the evidence of studies comparing the methodological properties of the EQ-5D-3L and EQ-5D-5L, with a special focus on redistribution of responses, including ceiling effects, floor effects, inconsistent responses, reliability and responsiveness. In the face of the reviewed results, both instruments demonstrated appropriateness for use in a wide range of study populations, addressing a variety of research questions and using different study designs. They show (1) the 5L responses logically distribute from the 3L, and (2) the 5L has advantages in terms of ceiling, (re-)distribution/distributional properties and how the descriptive system is used, but there are (3) some areas, such as responsiveness, in which the evidence is mixed and further research is needed. Furthermore, other aspects beyond the reviewed methodological parameters are important when choosing between 3L and 5L.

The low percentage of inconsistencies found in head-to-head studies demonstrates that the 3L redistributes logically to the 5L and that results of the 5L and 3L are comparable. The 5L is successful in reducing ceiling effects; a smaller proportion of respondents reported ‘11111’ on the 5L than on the 3L, especially in healthier samples. Thus, the 5L is suggested if the main goal is to discriminate among patients with milder health states. Moreover, the 5L outperformed the 3L when considering Shannon’s H′, with H′ being approximately 1.5-fold higher for the 5L compared with the 3L, without a relevant decrease of J′.

Missing values are negligible for both instruments demonstrating acceptance by respondents. Floor effects are also negligible for both instruments, meaning few respondents reported having the third or fifth levels of function in EQ-5D dimensions (e.g. ‘unable to wash or dress myself’). Most value sets assign negative weights to poor EQ-5D health states, meaning respondents valued many of these health states as worse than death (death is anchored at zero).

There is mixed evidence for better reliability on dimensional level, while evidence on index values shows better performance of 5L. Evidence on comparative responsiveness of the 3L and 5L is mixed \[37, 42, 45\]. This is surprising since adding levels to the 3L was intended to improve the responsiveness of the 3L. While two studies found the 5L to be slightly more responsive than the 3L when using non-parametric test statistics, Golicki et al. \[42\] found the crosswalk-derived 5L index to be less responsive than the 3L index when using several distribution-based approaches. There could be an explanation for why Golicki et al. conflicted with the other two studies. Crosswalk-derived utility scores tend to underdetect health gains \[60–62\]. For a preference-based instrument, it may be more appropriate to assess how changes in 5L versus 3L index scores are reflected in incremental cost-effectiveness ratios (ICERs) or quality-adjusted life-years (QALYs) \[63\]. Furthermore, differences with how participants value 3L versus 5L health states must be more closely examined \[64, 65\]. More research into sensitivity to change of the 5L and 3L is needed.

### Limitations

This review has several limitations. Although all but two studies directly compared the 3L and the 5L, there are several reasons that the results of this review are difficult to generalize. The data have been derived from (1) different studies, (2) sampled from different population or patient samples, (3) use different language versions or values sets of the EQ-5D, and (4) use varying research designs (e.g. order of 3L vs. 5L, placing other, and how many, questionnaires in between 3L and 5L). Due to the differing methods, designs, analyses and potential cross-cultural differences in EQ-5D response patterns \[66\], it was difficult to summarize results. There are no guidelines for preference-based measures or established guidelines and standards (such as, for example, COSMIN). The EuroQol Group could create a task force to develop reporting standards in order to ensure future studies are well-defined and use more homogenous methods.

However, choosing between using the 3L and 5L requires consideration of aspects beyond methodological characteristics (which were specifically addressed in the scope of this review), such as setting and respondents, purpose of use, and availability of instruments and value sets. For all self-assessment instruments, and for preference-based instruments in particular, the choice of instrument should always take into account the perspective of those who complete the instrument, i.e. patients or respondents. There is evidence that patients prefer the 5L to the 3L, although the reason is not clear \[8, 45, 67\]. Fewer patients reported problems filling in the EQ-5D-5L questionnaire, and more patients deem the 5L to be easier to answer than the 3L and can find statements to describe their own health state on the 5L.

Another crucial aspect is the available language version, and, related to that, the availability of a value set to calculate the index score for the target population. Currently, both the 3L and 5L are available in more than 120 languages (3L: \>170; 5L: \>130) and for various administration modes ([www.euroqol.org](http://www.euroqol.org)). To calculate an index score, the availability of a value set for the target population is necessary. The number of value sets available for the 3L (at least 27) is much larger than for the 5L (at least 8), with the crosswalk serving as the interim scoring method, while population-specific 5L value sets are being developed. There are also some cases where a 5L value set is available but a 3L is not; for those situations, population-specific 3L scores cannot be calculated.

## Conclusions

This review supports the use of both the 3L and the 5L in a broad range of patients, populations, and countries. The 5L performs slightly better in terms of reducing ‘ceiling’ effects, and similarly in many other distributional properties. More research must be conducted to clarify both instruments’ performance on sensitivity to change and reliability, for which our review found mixed results from a few studies. The EuroQol group considering guiding end users with the decision to use the 5L or 3L as the choice of instrument would be based on aspects beyond measurement properties. The evidence presented in this paper can benefit the development of new EQ-5D versions, such as a 5L version of the child-friendly EQ-5D-Y \[68\], or exploring additional dimensions to the current five-dimension format (‘bolt-ons’) \[69, 70\].

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary material 1 (DOCX 23 kb)

</div>

### Acknowledgements

The authors thank Associate Professor Benjamin M. Craig and Professor A. Simon Pickard for their valuable input while preparing and revising the manuscript. In particular, they would also like to thank Katrin Heyn for carefully reading and managing the references.

### Author Contributions

IB and YSF reviewed the articles and extracted and synthesized the data for this work. MFJ and TK were consulted in case of disagreement, and IB conceptualized the paper. All authors contributed to the drafting, editing, or critically reviewing of the paper.

### Compliance with Ethical Standards

Not applicable since this study describes a literature review.

#### Funding

This work was funded by the EuroQol Research Foundation (grant number EQ Project 2016170).

#### Conflict of interest

All authors are members of the EuroQol Group and receive or have received research grants from the EuroQol Research Foundation.

#### Disclaimer

The views of the authors expressed in this paper do not necessarily reflect the views of the EuroQol Group. Parts of the contents of this paper were presented at the 34th EuroQol Plenary Meeting in Barcelona, Spain.

#### Data Availability Statement

All data analyzed in this review were extracted from published articles (see the ESM) and are available from the corresponding authors of the included articles.

## References

1. Devlin NJ, Brooks R. EQ-5D and the EuroQol Group: Past, Present and Future. Appl Health Econ Health Policy. 2017;15(2):127–137. doi:10.1007/s40258-017-0310-5

2. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

3. Devlin NJ, Krabbe PF. The development of new research methods for the valuation of EQ-5D-5L. Eur J Health Econ. 2013;14(Suppl. 1):1–3. doi:10.1007/s10198-013-0502-3

4. Szende A, Oppe M, Devlin N. EQ-5D value sets: inventory, comparative review and user guide. EuroQol Group Monographs ed. 2007. Dordrecht, Springer.

5. Dyer MTD, Goldsmith KA, Sharples LS, Buxton MJ. A review of health utilities using the EQ-5D in studies of cardiovascular disease. Health Qual Life Outcomes. 2010;8:13. doi:10.1186/1477-7525-8-13

6. Prieto L, Novick D, Sacristan JA, Edgell ET. Alonso J, on behalf of the SOHO Study Group. A Rasch model analysis to test the cross-cultural validity of the EuroQoL-5D in the Schizophrenia Outpatient Health Outcomes Study. Acta Psychiatr Scand. 2003;107(Suppl. 416):24–29. doi:10.1034/j.1600-0447.107.s416.6.x

7. Luo N, Chew LH, Fong KY, Koh DR, Ng SC, Yoon KH, Vasoo S, Li SC, Thumboo J. Validity and reliability of the EQ-5D self-report questionnaire in English-speaking Asian patients with rheumatic diseases in Singapore. Qual Life Res. 2003;12(1):87–92. doi:10.1023/A:1022063721237

8. Janssen MF, Birnie E, Haagsma JA, Bonsel GJ. Comparing the standard EQ-5D three-level system with a five-level version. Value Health. 2008;11(2):275–284. doi:10.1111/j.1524-4733.2007.00230.x

9. Lloyd A. EQ-5D: Moving from Three Levels to Five. Editorial. Value Health. 2018;21(1):57–58. doi:10.1016/j.jval.2017.11.007

10. Payakachat N, Ali MM, Tilford JM. Can the EQ-5D detect meaningful change? A systematic review. PharmacoEconomics. 2015;33(11):1137–1154. doi:10.1007/s40273-015-0295-6

11. Johnson JA, Pickard AS. Comparison of the EQ-5D and SF-12 health surveys in a general population survey in Alberta, Canada. Med Care. 2000;38(1):115–121. doi:10.1097/00005650-200001000-00013

12. Lubetkin E, Jia H, Gold MR. Construct validity of the EQ-5D in low-income Chinese American primary care patients. Qual Life Res. 2004;13(8):1459–1468. doi:10.1023/B:QURE.0000040793.40831.72

13. Agency for Healthcare Research and Quality. National Healthcare Quality Report. 2003.

14. Kopec JA, Willison KD. A comparative review of four preference-weighted measures of health-related quality of life. J Clin Epidemiol. 2003;56(4):317–325. doi:10.1016/S0895-4356(02)00609-1

15. Moock J, Kohlmann T. Comparing preference-based quality-of-life measures: results from rehabilitation patients with musculoskeletal, cardiovascular, or psychosomatic disorders. Qual Life Res. 2008;17(3):485–495. doi:10.1007/s11136-008-9317-6

16. Szende A, Leidy NK, Stahl E, Svensson K. Estimating health utilities in patients with asthma and COPD: evidence on the performance of EQ-5D and SF-6D. Qual Life Res. 2009;18(2):267–272. doi:10.1007/s11136-008-9429-z

17. Richardson J, Iezzi A, Khan A, Chen G, Maxwell A. Measuring the sensitivity and construct validity of 6 utility instruments in 7 disease areas. Med Decis Making. 2016;36(2):147–159. doi:10.1177/0272989X15613522

18. Sintonen H. Comparing properties of the 15D and the EQ-5D in measuring health-related quality of life. Arch Hell Med. 2001;18(2):156–160.

19. Marra CA, Woolcott JC, Kopec JA, Shojania K, Offer R, Brazier JE, Esdaile JM, Anis AH. A comparison of generic, indirect utility measures (the HUI2, HUI3, SF-6D, and the EQ-5D) and disease-specific instruments (the RAQoL and the HAQ) in rheumatoid arthritis. Soc Sci Med. 2005;60(7):1571–1582. doi:10.1016/j.socscimed.2004.08.034

20. Papaioannou D, Brazier J, Parry G. How valid and responsive are generic health status measures, such as EQ-5D and SF-36, in schizophrenia? A Systematic Review. Value Health. 2011;14(6):907–920. doi:10.1016/j.jval.2011.04.006

21. Obradovic M, Lal A, Liedgens H. Validity and responsiveness of EuroQol-5 dimension (EQ-5D) versus Short Form-6 dimension (SF-6D) questionnaire in chronic pain. Health Qual Life Outcomes. 2013;11:110. doi:10.1186/1477-7525-11-110

22. Bonsel G, van Agt H. The number of levels in the descriptive system. 1994:115–120. Rotterdam, Institute of Medical Technology Assessment.

23. Kind P, Macran S. Levelling the playing field: increasing the number of response categories in EQ-5D. 19th Plenary Meeting of the EuroQol Group Discussion Papers. New York, Centre for Health Economics; 2002. pp. 311–22.

24. Van Reenen M, Janssen B. EQ-5D-5L User Guide, Basic Information on how to use the EQ-5D-5L instrument. Version 2.1. EuroQol Research Foundation; 2015.

25. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

26. NIH National Heart, Lung and Blood Institute. Study quality assessment tools. 2017. https://www.nhlbi.nih.gov/health-pro/guidelines/in-develop/cardiovascular-risk-reduction/tools. Accessed 30 Mar 2017

27. Terwee CB, Bot SD, de Boer MR, van der Windt DA, Knol DL, Dekker J. Quality criteria were proposed for measurement properties of health status questionnaires. J Clin Epidemiol. 2007;60(1):34–42. doi:10.1016/j.jclinepi.2006.03.012

28. Teachmann J. Analysis of population diversity. Sociol Methods Res. 1980;8:341–362. doi:10.1177/004912418000800305

29. Grissom RJ, Kim JJ. Effect sizes for research: Univariate and multivariate applications. 2012. New York, Taylor & Francis.

30. Kottner J, Audigé L, Brorsonc S, Donner A, Gajewski BJ, Hróbjartsson A, Roberts C, Shoukri M, Streiner DL. Guidelines for reporting reliability and agreement studies (GRRAS) were proposed. J Clin Epidemiol. 2011;64:96–106. doi:10.1016/j.jclinepi.2010.03.002

31. Watson PF, Petrie A. Method agreement analysis: a review of correct methodology. Theriogenology. 2010;73:1167–1179. doi:10.1016/j.theriogenology.2010.01.003

32. Shrout PE, Fleiss JL. Intraclass correlations: uses in assessing rater reliability. Psychol Bull. 1979;86(2):420–428. doi:10.1037/0033-2909.86.2.420

33. Viera AJ, Garrett JM. Understanding interobserver agreement: the kappa statistic. Fam Med. 2005;37(5):360–363.

34. Spitzer RL, Cohen J, Fleiss JL, Endicott J. Quantification of agreement in psychiatric diagnosis. A new approach. Arch Gen Psychiatry. 1967;17(1):83–87. doi:10.1001/archpsyc.1967.01730250085012

35. Fleiss JL, Cohen J. The equivalence of weighted kappa and the intraclass correlation coefficent as measures of reliability. Educ Psychol Meas. 1973;33:613–619. doi:10.1177/001316447303300309

36. Agborsangaya CB, Lahtinen M, Cooke T, Johnson JA. Comparing the EQ-5D 3L and 5L: measurement properties and association with chronic conditions and multimorbidity in the general population. Health Qual Life Outcomes. 2014;12:74. doi:10.1186/1477-7525-12-74

37. Buchholz I, Thielker K, Feng YS, Kupatz P, Kohlmann T. Measuring changes in health over time using the EQ-5D 3L and 5L: a head-to-head comparison of measurement properties and sensitivity to change in a German inpatient rehabilitation sample. Qual Life Res. 2015;24(4):829–835. doi:10.1007/s11136-014-0838-x

38. Conner-Spady BL, Marshall DA, Bohm E, Dunbar MJ, Loucks L, Al KA. Reliability and validity of the EQ-5D-5L compared to the EQ-5D-3L in patients with osteoarthritis referred for hip and knee replacement. Qual Life Res. 2015;24(7):1775–1784. doi:10.1007/s11136-014-0910-6

39. Craig BM, Pickard AS, Lubetkin EI. Health problems are more common, but less severe when measured using newer EQ-5D versions. J Clin Epidemiol. 2014;67(1):93–99. doi:10.1016/j.jclinepi.2013.07.011

40. Feng Y, Devlin N, Herdman M. Assessing the health of the general population in England: how do the three- and five-level versions of EQ-5D compare?. Health Qual Life Outcomes. 2015;13:171. doi:10.1186/s12955-015-0356-8

41. Golicki D, Niewada M, Buczek J, Karlińska A, Kobayashi A, Janssen MF, Pickard AS. Validity of EQ-5D-5L in stroke. Qual Life Res. 2015;24(4):845–850. doi:10.1007/s11136-014-0834-1

42. Golicki D, Niewada M, Karlinska A, Buczek J, Kobayashi A, Janssen MF. Comparing responsiveness of the EQ-5D-5L, EQ-5D-3L and EQ VAS in stroke patients. Qual Life Res. 2015;24(6):1555–1563. doi:10.1007/s11136-014-0873-7

43. Greene ME, Rader KA, Garellick G, Malchau H, Freiberg AA, Rolfson O. The EQ-5D-5L Improves on the EQ-5D-3L for Health-related Quality-of-life Assessment in Patients Undergoing Total Hip Arthroplasty. Clin Orthop Relat Res. 2015;473(11):3383–3390. doi:10.1007/s11999-014-4091-y

44. Janssen MF, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, Swinburn P, Busschbach J. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi:10.1007/s11136-012-0322-4

45. Jia YX, Cui FQ, Li L, Zhang DL, Zhang GM, Wang FZ. Comparison between the EQ-5D-5L and the EQ-5D-3L in patients with hepatitis B. Qual Life Res. 2014;23(8):2355–2363. doi:10.1007/s11136-014-0670-3

46. Khan I, Morris S, Pashayan N, Matata B, Bashir Z, Maguirre J. Comparing the mapping between EQ-5D-5L, EQ-5D-3L and the EORTC-QLQ-C30 in non-small cell lung cancer patients. Health Qual Life Outcomes. 2016;14:60. doi:10.1186/s12955-016-0455-1

47. Kim TH, Jo MW, Lee SI, Kim SH, Chung SM. Psychometric properties of the EQ-5D-5L in the general population of South Korea. Qual Life Res. 2013;22(8):2245–2253. doi:10.1007/s11136-012-0331-3

48. Kim SH, Kim HJ, Lee SI, Jo MW. Comparing the psychometric properties of the EQ-5D-3L and EQ-5D-5L in cancer patients in Korea. Qual Life Res. 2012;21(6):1065–1073. doi:10.1007/s11136-011-0018-1

49. Pan CW, Sun HP, Wang X, Ma Q, Xu Y, Luo N, Wang P. The EQ-5D-5L index score is more discriminative than the EQ-5D-3L index score in diabetes patients. Qual Life Res. 2015;24(7):1767–1774. doi:10.1007/s11136-014-0902-6

50. Pattanaphesaj J, Thavorncharoensap M. Measurement properties of the EQ-5D-5L compared to EQ-5D-3L in the Thai diabetes patients. Health Qual Life Outcomes. 2015;13:14. doi:10.1186/s12955-014-0203-3

51. Scalone L. Comparing the standard EQ-5D-3L versus 5L version for the assessment of health of patients with live diseases. EuroQol Proc. 2011;16:213–239.

52. Scalone L, Ciampichini R, Fagiuoli S, Gardini I, Fusco F, Gaeta L. Comparing the performance of the standard EQ-5D 3L with the new version EQ-5D 5L in patients with chronic hepatic diseases. Qual Life Res. 2013;22(7):1707–1716. doi:10.1007/s11136-012-0318-0

53. Scalone L, Cortesi PA, Ciampichini R, Cesana G, Mantovani LG. Health Related Quality of Life norm data of the general population in Italy: results using the EQ-5D-3L and EQ-5D-5L instruments. Epidemiol Biostat Public Health. 2015;12(3):e11457-1–e11457-15.

54. Shiroiwa T, Fukuda T, Ikeda S, Igarashi A, Noto S, Saito S, Shimozuma K. Japanese population norms for preference-based measures: EQ-5D-3L, EQ-5D-5L, and Sf-6D. Qual Life Res. 2016;25(3):707–719. doi:10.1007/s11136-015-1108-2

55. Wang Y, Tan NC, Tay EG, Thumboo J, Luo N. Cross-cultural measurement equivalence of the 5-level EQ-5D (EQ-5D-5L) in patients with type 2 diabetes mellitus in Singapore. Health Qual Life Outcomes. 2016;13:103. doi:10.1186/s12955-015-0297-2

56. Ferreira LN, Ferreira PL, Ribeiro FP, Pereira LN. Comparing the performance of the EQ-5D-3L and the EQ-5D-5L in young Portuguese adults. Health Qual Life Outcomes. 2016;14:89. doi:10.1186/s12955-016-0491-x

57. Poór AK, Rencz F, Brodszky V, Gulácsi L, Beretzky Z, Hidvégi B, Holló P, Kárpáti S, Péntek M. Measuement properties of the EQ-5D-5L compared to the EQ-5D-3L in psoriasis patients. Qual Life Res. 2017;26:3409–3419. doi:10.1007/s11136-017-1699-x

58. Yfantopoulos J, Chantzaras AE. Validation and comparison of the psychometric properties of the EQ-5D-3L and EQ-5D-5L instruments in Greese. Eur J Health Econ. 2017;18:519–531. doi:10.1007/s10198-016-0807-0

59. Yfantopoulos J, Chantzaras A, Kontodimas S. Assesment of the psychometric properties of the EQ-5D-3L and EQ-5D-5L instruments in psoriasis. Arch Dermatol Res. 2017;309:357–370. doi:10.1007/s00403-017-1743-2

60. Golicki D, Niewada M, van Hout B, Janssen MF, Pickard AS. Interim eq-5d-5 l value set for Poland: First crosswalk value set in Central and Eastern Europe. Value Health Reg Issues. 2014;4C:19–23. doi:10.1016/j.vhri.2014.06.001

61. Versteegh M, Vermeulen M, Evers AA, de Wit GA, Prenger R, Stolk A. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi:10.1016/j.jval.2016.01.003

62. Petrou S, Rivero-Arias O, Dakin H, Longworth L, Oppe M, Froud R. The maps reporting statement for studies mapping onto generic preference-based outcome measures. Value Health. 2015;18(7):A715–A716. doi:10.1016/j.jval.2015.09.2702

63. Alava MH, Wailoo A, Grimm S, Pudney S, Gomes M, Sadique Z, Meads D, O’Dwyer J, Barton G, Irvine L. EQ-5D-5L versus EQ-5D-3L: the impact on cost effectiveness in the United Kingdom. Value Health. 2018;21(1):49–56. doi:10.1016/j.jval.2017.09.004

64. Luo N, Cheung YB, Ng R, Lee CF. Mapping and direct valuation: do they give equivalent EQ-5D-5L index scores?. Health Qual Life Outcomes. 2015;13:166. doi:10.1186/s12955-015-0361-y

65. Devlin NJ, Shah KK, Feng Y, Mulhern B, van Hout B. Valuing health-related quality of life: An EQ-5D-5L value set for England. Health Econ. 2018;27(1):7–22. doi:10.1002/hec.3564

66. Feng Y, Herdman M, van Nooten F, Cleeland C, Parkin D, Ikeda S. An exploration of differences between Japan and two European countries in the self-reporting and valuation of pain and discomfort on the EQ-5D. Qual Life Res. 2017;26(8):2067–2078. doi:10.1007/s11136-017-1541-5

67. Chevalier J, De Pouvourville G. Testing a new 5 level version of the EQ-5D in France. EuroQol Proceedings. 2008;14:75–88.

68. Ravens-Sieberer U, Wille N, Badia X, Bonsel G, Burström K, Cavrini G, Devlin N, Egmar AC, Gusi N, Herdman M, Jelsma J, Kind P, Olivares PR, Scalone L, Greiner W. Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study. Qual Life Res. 2010;19(6):887–897. doi:10.1007/s11136-010-9649-x

69. Yang Y, Brazier J, Tsuchiya A. Effect of adding a sleep dimension to the EQ-5D descriptive system. A “Bolt-On” experiment. Med Decis Making. 2014;34(1):42–53. doi:10.1177/0272989X13480428

70. Yang Y, Rowen D, Brazier J, Tsuchiya A, Young T, Longworth L. an exploratory study to test the impact on three “Bolt-On” items to the EQ-5D. Value Health. 2015;18(1):52–60. doi:10.1016/j.jval.2014.09.004

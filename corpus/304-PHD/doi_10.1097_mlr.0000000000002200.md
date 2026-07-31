---
project_id: "304-PHD"
work_id: "doi:10.1097/mlr.0000000000002200"
doi: "10.1097/MLR.0000000000002200"
pmid: "40846650"
pmcid: "PMC12422609"
title: "Revisiting the Valuation of Child Health-Related Quality of Life"
journal: "Medical Care"
publication_date: "2025-08-18"
volume: "63"
issue: "10"
authors:
  - name: "Maksat Jumamyradov"
    orcid: "https://orcid.org/0009-0008-0180-7224"
    affiliation_ids:
      - "aff1"
  - name: "Benjamin M. Craig"
    affiliation_ids:
      - "aff1"
  - name: "Michał Jakubczyk"
    affiliation_ids:
      - "aff2"
affiliations:
  - id: "aff1"
    name: "Department of Economics, University of South Florida, Tampa, FL"
  - id: "aff2"
    name: "Division of Decision Analysis and Support, SGH Warsaw School of Economics, Warsaw, Poland"
keywords:
  - "EQ-5D-Y-3L"
  - "Kaizen task"
  - "discrete choice experiments"
  - "inflation reduction act"
  - "quality-adjusted life years"
licence: "cc-by-nc-nd"
source_file: "input/projects/304-PHD/papers/doi_10.1097_mlr.0000000000002200.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12422609/fullTextXML"
source_method: "epmc_xml"
source_sha256: "e25654840107b21d30b5d6283727cdc5fc67abd828adbf624c6d76f92c6716e1"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Revisiting the Valuation of Child Health-Related Quality of Life

## Abstract

### Objectives:

In 2013, the EQ-5D-Y-3L valuation study conducted by Craig and colleagues (ie, the original study) of child health-related quality of life (HRQoL) revealed that U.S. respondents often found it burdensome and guilt-inducing to choose between hypothetical health problems of children. This study introduces an alternative approach where respondents sequentially relieve the health problems of a 10-year-old child for 1 week.

### Methods:

We conducted a discrete choice experiment (DCE) survey (N=631) with paired comparisons and kaizen tasks. Each kaizen task displayed a single profile of a child’s HRQoL using the EQ-5D-Y-3L descriptive system and asked respondents to select first, second, and third improvements for the child’s problems. Combining the preference evidence, a conditional logit model was estimated to produce EQ-5D-Y-3L values on an “experience” scale, where positive values signify experiences better than “being in a coma” and negative values worse.

### Results:

All 10 main effects were statistically significant (*P*\<0.01), with the highest value placed on alleviating pain and discomfort. The worst-case scenario (33333) had a value of −0.337 on the experience scale, indicating it is worse than a coma. These new estimates highly correlate with the original U.S. EQ-5D-Y-3L values (Pearson correlation=0.726; Spearman correlation=0.794).

### Conclusion:

This innovative approach to child health valuation replaces paired comparisons with Kaizen tasks, reducing respondent burden and study costs. Its use of experience scaling, instead of QALYs, aligns with U.S. guidelines (eg, the Inflation Reduction Act of 2022) and summarizes child HRQoL gains for health technology assessment.

Health-related quality of life (HRQoL) is a multidimensional concept that refers to an individual’s or a population’s perceived physical, mental, emotional, and social wellbeing in relation to their health status and the health care they receive.<sup>1</sup> This subjective measure considers a person’s assessment of their own health and how it affects their overall quality of life.<sup>2,3</sup> To summarize gains across HRQoL domains for health technology assessments and other decision analyses, health preference researchers conduct discrete choice experiments (DCEs) that describe the value of HRQoL from the perspective of the general population (ie, social values).<sup>4–6</sup> While several valuation studies in the United States have conducted DCEs that trade off aspects of adult HRQoL,<sup>7–10</sup> few studies have conducted DCEs in child health valuation,<sup>11–13</sup> a rapidly evolving field with unique challenges.<sup>14,15</sup>

In 2013, Craig et al<sup>12</sup> conducted a child health valuation study (N=4,155; paired comparisons) in which they produced U.S. values for all EQ-5D-Y-3L (Y-3L) profiles on a quality-adjusted life year (QALY) scale (throughout this manuscript, we will refer to this study as the original). A QALY scale is anchored at 0 and 1, with the lower anchor representing “dying immediately” and the upper anchor representing “starting today, one year with no health problems then die.” Respondent feedback from this DCE as well as subsequent child health valuation studies indicated that making choices involving the lives of children evoked feelings of guilt for abandoning one child.<sup>15–17</sup> This subsequently raised questions about respondents’ role in supporting policies on child health and prompted critical examination of QALY scaling in general.

In this paper, we emphasize 2 findings regarding respondent burden in child health valuation. First, most child health valuation studies have involved paired comparisons or similar tasks in which respondents choose between the lives of children with health problems (eg, life A vs. life B for a 10-year-old child), and some respondents have expressed feeling emotional strain with their role as a decision-maker in such a hypothetical task.<sup>18</sup> Second, to produce estimates on a QALY scale, all children in these scenarios died (ie, terminal profiles), and some were even described as “dying immediately.” Respondents expressed feeling of added reluctance to choose between a terminally ill child and one facing immediate death. These 2 findings highlighted the need for a less burdensome approach to child health valuation. In addition, by replacing “dying immediately” with “being in a coma,” the published protocol<sup>19</sup> and this paper responds to recent U.S. regulations prohibiting the use of QALY scaling in value assessment.

To revisit the original valuation of child HRQoL, this DCE survey included 10 kaizen tasks. *Kaizen* is a Japanese term that describes continuous improvement (*kai* ~ change, *zen* ~ good). Introduced by Craig et al,<sup>20</sup> kaizen tasks elicit each respondent’s optimal sequence of improvements from an initial profile (ie, preference paths). Instead of asking respondents to choose between the lives of children with health problems as was done in the original study and all subsequent child health valuation studies, the respondents in this study were shown a single profile describing a child’s HRQoL for 1 week and asked to relieve the child’s problems by selecting a first, second, and third improvement. Figure <a href="#F1" data-ref-type="fig">1</a> shows an illustration of a kaizen task where a respondent is being presented with a single Y-3L profile and asked to relieve 3 health problems.

<figure id="F1">
<p><img src="mlr-63-771-g001.jpg" /></p>
<figcaption>Example of a Kaizen task.</figcaption>
</figure>

As a complement to the kaizen tasks, the DCE survey included paired comparisons, asking whether having the problems is preferable to “being in a coma” for a week (ie, whether “no experience” is a relief in certain cases). Using the kaizen and paired comparison evidence, we estimated a conditional logit model to produce U.S. Y-3L values on an “experience” scale, in which a positive value signifies an experience that is better than having no experience at all (ie, “being in a coma”), while a negative value indicates an experience worse than having no experience. Originally, since having no experience could not be described within the 5 dimensions of EQ-5D-3L, the EuroQol Group introduced “unconscious” for completeness.<sup>21,22</sup> Therefore, like death, the “experience” scale can be interpreted as a potential anchor or base of a preference scale for the EQ-5D-3L profiles.

Although it is open to interpretation, Section 1194(e) of the Inflation Reduction Act (IRA) of 2022 states that the U.S. Secretary of Health and Human Services “shall not use evidence from comparative clinical effectiveness research in a manner that treats extending the life of an elderly, disabled, or terminally ill individual as of lower value than extending the life of an individual who is younger, nondisabled, or not terminally ill.” In other words, life extension for all individuals must have the same value (ie, no discrimination). In consequence, the IRA prohibits the valuation of health outcomes using the typical QALY model in which the value of a life extension depends on the person’s HRQoL.

In many contexts, it may be necessary to summarize gains in HRQoL apart from life extensions or monetary costs. Welfarism and extrawelfarism are alternative approaches to the summary of health outcomes. Welfarism focuses solely on maximizing societal welfare as an aggregate of individual utilities and extrawelfarism considers ethical principles beyond utility, such as fairness. For example, a welfarist program may place a higher value on life extensions and quality of life of those willing to pay (eg, wealthy individuals) and an extrawelfarist program may place the same value on the health outcomes of all individuals regardless of their wealth. Using the experience scale, the value of quality of life is the same for all individuals regardless of their wealth (ie, ignores willingness to pay) or length of life (ie, ignores tradeoff between quality and length of life). Under the protocol for this study,<sup>19</sup> respondents only choose between gains in child HRQoL (no life extensions or monetary costs); therefore, this study avoids using the willingness-to-pay and QALY models and aligns with IRA under a responsive form of extrawelfarism. Excluding monetary cost and life extensions from this study may be convenient in view of the fact that choosing between child HRQoL gains, monetary costs, and life extensions is mentally burdensome to many respondents<sup>15,16</sup> and may be subject to framing effects,<sup>23</sup> which is a cognitive bias that may affect respondents’ choice formed due to the presentation or contextual description of attributes, alternatives or choice situations. In this paper, we demonstrate an innovative approach to child health valuation, replacing paired comparisons with kaizen tasks and QALY scaling with experience scaling, as well as revisit the original U.S. value set for the EQ-5D-Y-3L.<sup>12</sup>

## METHODS

After being reviewed by 2 DCE experts, the protocol, including the formative qualitative research, the survey instrument, the experimental design, and the analysis plan, was published by *BMJ Open* before data collection.<sup>19</sup> There were no deviations from this protocol and all R code has been posted on [www.r4hpr.org](http://www.r4hpr.org). Given open access to these materials online, this section provides an abbreviated overview of the methods.

In this study, the HRQoL of a 10-year-old child was described as either “being in a coma” (ie, no experience) or having problems in up to 5 domains for 1 week. More specifically, the Y-3L descriptive profile displays 5 3-level attributes, rendering 243 possible profiles (3<sup>5</sup>) ranging from 11111 (best) to 33333 (worst). For instance, the profile 22222 represents the HRQoL of a child with moderate health problems (level 2) across all 5 domains. To mitigate inference about future HRQoL (beyond this 1 wk episode), respondents were instructed that the child’s remaining life is equivalent regardless of their choices, and they indicated their understanding of this equivalence using a confirmatory checklist, specifically that “in each of these hypothetical scenarios, the cause is the same, the recovery is the same, the rest of their life is the same, and the children survive.”

The survey instrument has 6 sections: consent and screener, background, paired comparisons (Y-3L vs. “being in a coma”; 1 warmup exercise and 5 tasks), paired comparisons (Y-3L vs. Y-3L; 1 warmup and 10 tasks), kaizen tasks (Y-3L preference paths; 1 warmup and 10 tasks), and follow-up.<sup>19</sup> Beta testing of the survey instrument (12 semi-structured interviews) led to substantive improvements, particularly in the description of “being in a coma.”<sup>19</sup> For example, the background component included a 5-question quiz to promote a common understanding of what a coma entails and to detect fraudulent responses that may be generated by an automized bot. The quiz questions were selected to address common misconceptions about comas in terms of (1) their causes, (2) self-care during comas, (3) duration of comas, (4) recovery time and (5) the outcomes of comas.

For this study, we expected to recruit a sample of 600 U.S. adults based on 18 demographic quotas (Dynata online panel vendor). To promote internal validity, the survey instrument randomly assigned respondents from each quota to 1 of 4 D-efficient blocks (ie, a statistical measure used in evaluating how effectively an experimental design estimates the parameters of a model) and randomized the sequence of the last 2 DCE components (eg, Y-3L comparisons followed by kaizen tasks), task sequence (within each component), attribute order (between components), and object position (only in the Y-3L comparisons; eg, left-right).

For descriptive analysis, we compared the sample of respondents who completed the survey (Table <a href="#T1" data-ref-type="table">1</a>; Supplemental Digital Content 1, <http://links.lww.com/MLR/D39>) with those who dropped out and with the 2021 American Community Survey (ACS) 1-year estimates using χ<sup>2</sup> tests<sup>24</sup> (ACS, 2021). Furthermore, we analyzed the median and interquartile range (IQR) of survey time overall and for each DCE component (Supplemental Digital Content 2, <http://links.lww.com/MLR/D40>) as well as respondents’ task preferences (paired comparisons vs. kaizen tasks).

<div id="T1" class="table-wrap">

<div class="caption">

Respondent Characteristics By Completion and Compared With U.S. Census Estimates

</div>

|  | Completed N=631% (n) | Dropout N=168% (n) | *P* | ACS<a href="#T1fn1" data-ref-type="table-fn">*</a> % | 1/3 Rule % |
|:---|:---|:---|:---|:---|:---|
| Age in years |  |  | \<0.001 |  |  |
|  18–34 | 35 (224) | 22 (37) |  | 29 | 83 |
|  35–54 | 37 (234) | 37 (62) |  | 33 | 89 |
|  55 and older | 27 (173) | 41 (69) |  | 38 | 141 |
| Sex |  |  | \<0.001 |  |  |
|  Female | 49 (309) | 65 (109) |  | 51 | 104 |
|  Male | 50 (314) | 33 (56) |  | 49 | 98 |
|  Other/prefer not to say | 1.3 (8) | 2 (3) |  |  |  |
| Race |  |  | \<0.001 |  |  |
|  White | 75 (476) | 67 (113) |  | 64 | 85 |
|  Black or African American | 12 (77) | 23 (39) |  | 12 | 100 |
|  American Indian or Alaska Native | 1 (4) | 1 (1) |  | 1 | 90 |
|  Asian | 4 (27) | 1 (2) |  | 6 | 150 |
|  Native Hawaiian or Other Pacific Islander | 0 (1) | 0 |  | 0 |  |
|  Some other race | 2 (15) | 3 (5) |  | 7 | 350 |
|  Two or more races | 5 (31) | 5 (8) |  | 10 | 200 |
| Ethnicity |  |  | 0.649 |  |  |
|  Hispanic or Latino | 11 (72) | 12 (20) |  | 17 | 155 |
|  Other | 89 (559) | 88 (148) |  | 83 | 93 |
| U.S. regions |  |  | \<0.001 |  |  |
|  Northeast | 20 (126) | 18 (31) |  | 18 | 90 |
|  Midwest | 22 (138) | 18 (30) |  | 21 | 96 |
|  South | 38 (237) | 46 (78) |  | 38 | 100 |
|  West | 21 (130) | 17 (29) |  | 24 | 114 |

Percentages may not add up to 100% due to rounding.

Taken from the United States Census Bureau 2021 American Community Survey.

</div>

Using the analytical sample, we examined the value that U.S. adults place on child HRQoL, with $`V`$ as the value of health outcome for individual $`i \in \{ 1,\ldots,N\}`$ for choice situation (ie, task) $`t \in \{ 1,\ldots T`$}. However, we dropped the subscripts for individual, object and time for simplicity. In the literature, $`V`$ is usually assumed to be linear in parameters<sup>25</sup> and is a function of attributes. We specified the value of a health outcome ($`V`$) as a product of 2 values representing HRQoL ($`V^{H}`$) and life years ($`V^{Y}`$):

``` math
V = V^{H} \times V^{Y}
```

However, this study only considered a one-episode duration (ie, a 1 wk period) and not the value of life extensions, a form of extrawelfarism responsive to IRA; therefore, we constrained $`V^{Y} = 1`$ for the sake of simplicity. This restriction is present in this paper so that we may allow the value of health outcomes to vary by their duration in future studies (including through time discounting and other time preferences).

Further, we assumed that the value of HRQoL is linear $`V^{H} = 1 - X\beta`$, where $`X`$ is a vector of 10 incremental indicators of level changes (ie, from 3 to 2 or from 2 to 1) in mobility (walking around), self-care, usual activities, pain/discomfort and anxiety/depression (ie, $`\mathit{MO}1`$, $`\mathit{MO}2`$, $`\mathit{SC}1`$, $`\mathit{SC}2`$, $`\mathit{UA}1`$, $`\mathit{UA}2`$, $`\mathit{PD}1`$, $`\mathit{PD}2`$, $`\mathit{AD}1`$, $`\mathit{AD}2`$), as well as an 11th indicator for “being in a coma” (COMA), and $`\beta = \{\beta_{1},\ldots,\beta_{11}\}`$ is a vector of main effects (ie, attribute importance). Therefore, we expressed the value of HRQoL as follows:

``` math
V^{H} = 1 - \begin{pmatrix}
{\beta_{1}\mathit{MO}1 + \beta_{2}M02 + \beta_{3}\mathit{SC}1 + \beta_{4}\mathit{SC}2 + \beta_{5}\mathit{UA}1 +} \\
{\beta_{6}\mathit{UA}2 + \beta_{7}\mathit{PD}1 + \beta_{8}\mathit{PD}1 + \beta_{9}\mathit{AD}1 + \beta_{10}\mathit{AD}2 + \beta_{11}\mathit{COMA}}
\end{pmatrix}
```

Under this specification, the value of 11111 (best-case scenario) is 1 due to the absence of problems, and the value of 33333 (worst-case scenario) is 1 minus the sum of all 10 Y-3L main effects. In addition, we set the value of “being in a coma” at zero by constraining its effect ($`\beta_{11} = 1`$). Therefore, the Y-3L values are expressed on an experience scale, anchored by 1, which represents experiencing no health problems, and 0, which represents experiencing nothing (ie, “being in a coma”).

Following McFadden,<sup>26</sup> we expressed the probability of choosing alternative $`j \in \{ 1,\ldots,J\}`$ as follows:

``` math
P_{j} = \frac{\exp{(\sigma V_{j})}}{\sum\limits_{k = 1}^{J}\exp({\sigma V}_{k})}
```

where $`\sigma`$ represents the scaling factor. Under this specification, we estimated the 10 main effects as well as the log of the 2 scaling factors, $`\ln(\sigma)`$: one for kaizen tasks and another for paired comparisons (Y-3L vs. “being in a coma”). To account for within-respondent correlations, all *P*-values and SEs were estimated using cluster bootstrap techniques (with replacement and 1000 iterations). In addition, we examined the association between these Y-3L main effects (kaizen tasks and experience scale) with the original ones (paired comparisons and QALY scale measurements) using Pearson and Spearman correlations. The new (ie, the kaizen tasks and paired comparison estimates from this study) and original values are on different scales; however, these correlations are invariant to linear transformation of each variable.

## RESULTS

### Sample Characteristics

Between September 29 and October 10, 2023, we recruited 1261 U.S. adults to participate in this study; however, 72 (5.7%) dropped out before block assignment and 462 (36.6%) failed the coma quiz 3 times. After block assignment, 96 (7.6%) dropped out and 631 (50%) completed the survey (Table <a href="#T1" data-ref-type="table">1</a>). We found statistically significant differences between individuals who completed the survey and those who dropped out based on their age, sex, race and U.S. regions (*P*\<0.001, respectively; Table <a href="#T1" data-ref-type="table">1</a>). Also, there are a few differences when compared with U.S. Census estimates (Table <a href="#T1" data-ref-type="table">1</a> and Supplemental Digital Content 1, <http://links.lww.com/MLR/D39>). For descriptive analysis, we compared the sample of respondents who completed the survey (Table <a href="#T1" data-ref-type="table">1</a>) with those who dropped out using χ<sup>2</sup> tests and with the 2021 American Community Survey (ACS) 1-year estimates (ACS, 2021) based on 66% and 133% thresholds (ie, 1/3 rule).

The respondents’ median (first and third quartile) time to complete the entire survey was 17.05 minutes (12.6, 24). Similarly, the median completion times for each component were 0.9 minutes (0.7, 1.4) for the initial paired comparisons (Y-3L vs. “being in a coma”), 2.3 minutes (1.4, 3.5) for the Y-3L comparisons, and 2.6 minutes (1.9, 3.8) for the kaizen tasks. The majority of respondents reported that kaizen tasks are easier to complete, easier to understand, and preferred to the paired comparisons (*P*\<0.05; Supplemental Digital Content 2, <http://links.lww.com/MLR/D40>), confirming prior qualitative feedback.

### Parameter Estimates

As shown in Table <a href="#T2" data-ref-type="table">2</a>, all 10 main effects are statistically significant (ie, *P*\<0.01) and their SEs are small (\<0.02 on an experience scale). As expected, the largest incremental effects are PD1 and PD2, with estimated values of 0.270 (0.015) and 0.332 (0.020), respectively. The value of the worst-case scenario (33333) is $`- 0.337`$ on an experience scale, which implies that it is worse than “being in a coma” (ie, no experience; *P*\<0.05). The log of the kaizen scale factor is greater than that of the paired comparisons (0.510 vs. 1.543, *P*\<0.001), which implies that kaizen tasks have more sensitivity to differences in value than the paired comparisons.

<div id="T2" class="table-wrap">

<div class="caption">

Gains in Child Health-Related Quality of Life on an Experience Scale

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Child health-related quality of life (N=631)</th>
<th style="text-align: center;">Estimate (SE)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;">Mobility (walking around)</td>
</tr>
<tr>
<td style="text-align: left;"><strong> </strong>MO1: Some to no problems walking around</td>
<td style="text-align: left;">0.096<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.010)</td>
</tr>
<tr>
<td style="text-align: left;"> MO2: A lot to some problems walking around</td>
<td style="text-align: left;">0.152<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.012)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Looking after myself</td>
</tr>
<tr>
<td style="text-align: left;"> SC1: Some to no problems taking a bath or shower by myself or getting dressed by myself</td>
<td style="text-align: left;">0.042<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.009)</td>
</tr>
<tr>
<td style="text-align: left;"> SC2: A lot to some problems taking a bath or shower by myself or getting dressed by myself</td>
<td style="text-align: left;">0.090<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.010)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Doing usual activities</td>
</tr>
<tr>
<td style="text-align: left;"> UA1: Some to no problems doing my usual activities</td>
<td style="text-align: left;">0.060<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.009)</td>
</tr>
<tr>
<td style="text-align: left;"> UA2: A lot to some problems doing my usual activities</td>
<td style="text-align: left;">0.128<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.011)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Having pain or discomfort</td>
</tr>
<tr>
<td style="text-align: left;"> PD1: Some to no pain or discomfort</td>
<td style="text-align: left;">0.270<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.015)</td>
</tr>
<tr>
<td style="text-align: left;"> PD2: A lot to some pain or discomfort</td>
<td style="text-align: left;">0.332<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.020)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Feeling worried, sad or unhappy</td>
</tr>
<tr>
<td style="text-align: left;"> AD1: A bit to not worried, sad or unhappy</td>
<td style="text-align: left;">0.027<a href="#T2fn2" data-ref-type="table-fn">**</a> (0.011)</td>
</tr>
<tr>
<td style="text-align: left;"> AD2: Very to a bit worried, sad or unhappy</td>
<td style="text-align: left;">0.140<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.013)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Log of the scale factor</td>
</tr>
<tr>
<td style="text-align: left;"> Coma comparisons</td>
<td style="text-align: left;">0.510<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.132)</td>
</tr>
<tr>
<td style="text-align: left;"> Kaizen tasks</td>
<td style="text-align: left;">1.543<a href="#T2fn1" data-ref-type="table-fn">*</a> (0.064)</td>
</tr>
</tbody>
</table>

indicates 0.001.

indicates 0.01.

indiactes 0.05.

Each estimate represents the value associated with an improvement in child HRQoL on an experience scale, namely the incremental effect of relieving a child's health problem based on stakeholder values. The scale factor σ in equation 3 represents the proportional relationship between the experience scale and the log-odds of a choice in a specific task. In other words, σ is a measure of the variation in the latent dependent variable that remains unexplained after inclusion of the explanatory variables (covariates).

</div>

### Comparison of Kaizen Tasks and Paired Comparisons

Figure <a href="#F2" data-ref-type="fig">2</a> illustrates the relationship between the new and original main-effects estimates (taken from the 2013 study) and their CIs (ie, vertical and horizontal bars). These estimates correlate strongly with each other (ie, Pearson and Spearman correlation coefficients equal to 0.726 and 0.794, respectively). Although the sample size of the original survey is over 6 times larger (N=4155 vs. 631), the CIs of these main effects are narrower after adjusting for differences in scale.

<figure id="F2">
<p><img src="mlr-63-771-g002.jpg" /></p>
<figcaption>New and original estimates of EQ-5D-Y-3L values.</figcaption>
</figure>

Next, we assessed whether the main-effect estimates are robust to 2 alternate specifications. First, after we replaced kaizen responses with the Y-3L comparison responses (Supplemental Digital Content 3, <http://links.lww.com/MLR/D41>), the first of the 10 effects becomes insignificant (UA1; *P*=0.2), but these estimates largely agree with the kaizen estimates (ie, Pearson and Spearman correlation as well as Lin concordance coefficients are equal to 0.886, 0.794, and 0.861, respectively) and strongly correlate with the original estimates (ie, Pearson and Spearman correlation coefficients equal to 0.928 and 0.879, respectively). Second, 2 of the 40 block-specific estimates (Supplemental Digital Content 4, <http://links.lww.com/MLR/D42>) are insignificant (Block 3: SC1, *P*-value=0.2; AD1, *P*=0.12). The block-specific estimates largely agree with each other (ie, Lin concordance coefficient ranges from 0.914 to 0.995). Furthermore, Figure 5 in the Supplemental Digital Content 4, <http://links.lww.com/MLR/D42> illustrates the relationship between the block-specific sample sizes and SEs \[eg, with only 50 respondents in Block 1, all effects are significant (*P*\<0.05) and have an SE of \<0.05\]. Finally, we found that the mean and SD of all 10 main effects are significant (*P*\<0.001), and that the mixed logit (Supplemental Digital Content 5, <http://links.lww.com/MLR/D43>) and CL estimates are highly concordant with each other (ie, Pearson correlation and Lin concordance coefficients equal to 0.987 and 0.890, respectively).

## DISCUSSION

This study demonstrates an innovative approach to child health valuation that uses kaizen tasks and experience scaling.<sup>19</sup> Our results suggest that U.S. adults value all 10 improvements in child HRQoL and that “being in a coma” is generally preferred to the Y-3L worst-case scenario (33333). Further, we found that the new U.S. Y-3L values agree with the original ones (Fig. <a href="#F2" data-ref-type="fig">2</a>) and paired-comparison-only estimates (Supplemental Digital Content 3, <http://links.lww.com/MLR/D41>). In summary, the 2 methodological advances put forth under this approach described here, particularly relevant for U.S. value assessment and other contexts in which discrimination against vulnerable populations must be avoided. We conclude that, apart from being less burdensome for respondents, an online DCE survey with about 50 respondents is sufficient to produce a Y-3L value set on an experience scale, which may motivate the use of this approach in other countries or regions (eg, state-specific value sets).

Policymakers in many countries endorse the use of QALYs as a unit of measure for cost-effectiveness analysis<sup>27–29</sup> (CEA). However, in the U.S., the valuation of life extensions under the QALY model has received criticisms regarding its potential discriminatory effects toward people with disabilities, older adults, and the most vulnerable members of society.<sup>30,31</sup> Specifically, the National Council on Disability reported that “QALYs place a lower value on treatments which extend the lives of people with chronic illnesses and disabilities” and suggested that Congress, other federal agencies, and public and private insurers should reject the use of QALYs in CEA.<sup>32</sup> This is directly addressed in the IRA, which prohibits the use of QALYs in programs such as the Medicare Drug Price Negotiation Program, in part because they can discriminate against extending the life expectancy of those who have serious illnesses, are older, or have disabilities.

As described in the introduction, this is not a standard Y-3L value set on a QALY scale.<sup>18</sup> We produced a Y-3L value set on an experience scale. This scale may be used to compare gains in HRQoL apart from life extension, and the elicitation of the values on this scale does not require trading off life extensions or the comparisons of challenging life profiles (eg, immediate death). The QALY scale may be used to summarize gains in HRQoL and life extensions, but studies that produce values on the QALY scale must include tradeoffs between gains in HRQoL and life extensions (including immediate death) for anchoring purposes. For example, respondents in the international protocol, are asked to choose between the lives of a hypothetical child, “Consider your views for a 10-year-old child, what do you prefer Life A, Life B, or Life A and B are about the same?” and Life A may be “immediate death”.<sup>18</sup> An added difference between the QALY and experience scale stems from the fact that “being in a coma” is a reversible outcome contrary to dying immediately, ie, a child may be in coma for a week and then recover similar to a child who experiences other acute problems for a week.

Some may disagree about whether this approach is directly comparable to the original one, because it does not ask respondents to choose between the lives of a hypothetical child or ask them to trade gains in child HRQoL to extend life expectancies.<sup>18</sup> We emphasize that these results cannot summarize the value of life extensions in children. This limitation results from the fact that dying immediately is not positioned on the experience scale. The Y-3L values derived in the present paper only summarize child HRQoL over 1 week and should not be multiplied by weeks to extrapolate the value over a longer duration or divided by 7 to extrapolate the value of a day. Likewise, they should not be used in decision analyses to extrapolate the value of children with varying life expectancies (ie, quality-adjusted life expectancies), which is prohibited by IRA. Several alternative approaches to QALYs have been proposed.<sup>33–36</sup> Under this approach described here, the use of experience scaling emphasizes the respondents’ authority to characterize what constitutes a good or bad week (ie, better than or worse than no experience) for a 10-year-old child.

This paper demonstrates how kaizen tasks and experience scaling can serve as useful tools in health economics, particularly in regard to producing HRQoL value sets. More specifically, this approach holds 3 crucial advantages for child health valuation that we would like to point out. First, each respondent in a kaizen task has control over the sequential relief of child health problems, mimicking the pediatric decision-making process. While life extension is a vital consideration, decision-makers rarely choose whether a child lives or dies, which may be difficult to imagine and emotionally straining. Second, the new estimates correlate well with the original ones, yet this study had a fraction of the original sample size (ie, 631 vs. 4255). Third, the greater precision of these estimates implies that future studies may be conducted in small samples (eg, with patients) or that large ones could better identify preference heterogeneity within a population. We believe that health preference researchers conducting DCE should strive to introduce approaches with greater precision, reduced cost, and lower burdens that may be implemented into clinical practice. In some cases, it is not feasible or is extremely expensive to recruit hundreds of respondents, making this approach even more attractive.

In this paper, we introduce a novel approach to child health valuation and produce a new U.S. Y-3L value set on the experience scale motivated in part by the prohibition of the QALY scale under IRA. Future researchers may use this approach to summarize patient experiences based on a small clinic-specific sample. In child health valuation, this approach may summarize Y-3L values from the perspective of parents with young children or other groups involved in pediatric care. Once it becomes common practice, this tool may prove integral in clinical practice at various levels, where providers regularly ask small groups of patients how they might improve their services.

## Supplementary Material

<div class="caption">

###### SUPPLEMENTARY MATERIAL

</div>

### ACKNOWLEDGMENTS

The authors acknowledge the EuroQol Research Foundation for their support of Maksat Jumamyradov’s dissertation (304-PHD), under the supervision of Drs Murat K. Munkin and Benjamin M. Craig, University of South Florida, Tampa, FL.

## REFERENCES

1. CellaDF . Measuring quality of life in palliative care. Semin Oncol. 1995;22:73–81.7537908

2. SchipperH . Quality of life: principles of the clinical paradigm. J Psychosoc Oncol. 1990;8:171–185.

3. World Health Organization . The First Ten Years of the World Health Organization. Geneva: World Health Organization; 1958. https://iris.who.int/bitstream/handle/10665/37089/a38153_eng_LR_part1.pdf?sequence=14

4. CharltonV DiStefanoM MitchellP . We need to talk about values: a proposed framework for the articulation of normative reasoning in health technology assessment. Health Econ Poli Law. 2024;19:153–173.10.1017/S174413312300003837752732

5. StolkEA CraigBM MulhernB . Health valuation: demonstrating the value of health and lifespan. Pat Pat Center Outcomes Res. 2017;10:515–517.10.1007/s40271-017-0252-x28597376

6. ThurstoneLL . The measurement of values. Psychol Rev. 1954;61:47–58.13134416 10.1037/h0060035

7. CraigBM PickardAS StolkE . US valuation of the SF-6D. Med Decis Making. 2013;33:793–803.23629865 10.1177/0272989X13482524PMC3740344

8. CraigBM ReeveBB BrownPM . US valuation of health outcomes measured using the PROMIS-29. Value Health. 2014;17:846–853.25498780 10.1016/j.jval.2014.09.005PMC4471856

9. CraigBM LancsarE MühlbacherAC . Health preference research: an overview. Pat Pat Center Outcomes Res. 2017;10:507–510.10.1007/s40271-017-0253-928597377

10. CraigBM RandK . Choice defines QALYs: a US valuation of the EQ-5D-5L. Value Health. 2018;21:S12.10.1097/MLR.000000000000091229668646

11. CraigBM BrownDS ReeveBB . The value adults place on child health and functional status. Value Health. 2015;18:449–456.26091599 10.1016/j.jval.2015.02.012PMC4475576

12. CraigBM GreinerW BrownDS . Valuation of child health-related quality of life in the United States. Health Econ. 2016a;25:768–777.25926161 10.1002/hec.3184

13. CraigBM BrownDS ReeveBB . Valuation of child behavioral problems from the perspective of US adults. Med Decis Making. 2016b;36:199–209.26209476 10.1177/0272989X15594370PMC4698056

14. LambA MurrayA LovettR . The challenges of measuring and valuing quality of life in preschool children: a retrospective review of NICE appraisals. Children. 2021;8:765.34572196 10.3390/children8090765PMC8464668

15. DewildeS JanssenMF LloydAJ . Exploration of the reasons why health state valuation differs for children compared with adults: a mixed methods approach. Value Health. 2022;25:1185–1195.35232661 10.1016/j.jval.2021.11.1377

16. PowellPA RowenD Rivero-AriasO . Valuing child and adolescent health: a qualitative study on different perspectives and priorities taken by the adult general public. Health Qual Life Outcomes. 2021;19:1–14.34556133 10.1186/s12955-021-01858-xPMC8461831

17. Rivero-AriasO BuckellJ KnightM . Defining treatment success in children with surgical conditions. Arch Dis Child. 2024;109:377–386.38135491 10.1136/archdischild-2023-326156PMC11041596

18. Ramos-GoñiJM OppeM StolkE . International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics. 2020;38:653–663.32297224 10.1007/s40273-020-00909-3

19. JumamyradovM CraigBM Rivero-AriasO . Child health valuation protocol for a discrete choice experiment comparing paired comparison and kaizen tasks and estimating US EQ-5D-Y-3L values on an experience scale. BMJ Open. 2023;13:e077256.10.1136/bmjopen-2023-077256PMC1060352337879694

20. CraigBM RandK HartmanJD . Preference paths and their Kaizen tasks for small samples. Patient Patient Centered Outcomes Res. 2022;15:187–196.10.1007/s40271-021-00541-zPMC832176934327605

21. DolanP . Modeling valuations for EuroQol health states. Med Care. 1997;35:1095–1108.9366889 10.1097/00005650-199711000-00002

22. ShawJW JohnsonJA CoonsSJ . US valuation of the EQ-5D health states: development and testing of the D1 valuation model. Med Care. 2005;43:203–220.15725977 10.1097/00005650-200503000-00003

23. JakubczykM SchneiderP LipmanSA . This dead or that dead: framing effects in the evaluation of health states. Value Health. 2024;27:95–103.37913922 10.1016/j.jval.2023.10.009

24. American Community Survey [database online] . United States Census Bureau; 2021. Updated August 16, 2023.

25. HensherDA RoseJM GreeneWH . Applied choice analysis: a primer. New York: Cambridge University Press; 2005.

26. McFaddenD . Conditional logit analysis of qualitative choice behavior ZarembkaP . Frontiers in Econometrics. New York: Academic Press; 1974:105–142.

27. DolanP ShawR TsuchiyaA . QALY maximisation and people’s preferences: a methodological review of the literature. Health Econ. 2005;14:197–208.15386656 10.1002/hec.924

28. GarrisonLPJr Kamal-BahlS TowseA . Toward a broader concept of value: identifying and defining elements for an expanded cost-effectiveness analysis. Value Health. 2017;20:213–216.28237197 10.1016/j.jval.2016.12.005

29. LakdawallaDN DoshiJA GarrisonJr LP . Defining elements of value in health care—a health economics approach: an ISPOR Special Task Force report [3]. Value Health. 2018;21:131–139.29477390 10.1016/j.jval.2017.12.007

30. RandLZ KesselheimAS . An international review of health technology assessment approaches to prescription drugs and their ethical principles. J Law Med Ethics. 2020;48:583–594.33021189 10.1177/1073110520958885

31. RandLZ KesselheimAS . Controversy over using quality-adjusted life-years in cost-effectiveness analyses: a systematic literature review: systematic literature review examines the controversy over the use of quality-adjusted life-year in cost-effectiveness analyses. Health Aff (Millwood). 2021;40:1402–1410.34495724 10.1377/hlthaff.2021.00343

32. Quality-Adjusted Life Years and the Devaluation of Life with Disability . National Council on Disability; 2019. https://ncd.gov/sites/default/files/NCD_Quality_Adjusted_Life_Report_508.pdf

33. DiStefanoMJ ZemplenyiA AndersonKE . Alternative approaches to measuring value: an update on innovative methods in the context of the United States Medicare Drug Price Negotiation Program. Exp Rev Pharmacoeconom Outcomes Res. 2023;24:171–180.10.1080/14737167.2023.228358437961908

34. GoldMR StevensonD FrybackDG . HALYS and QALYS and DALYS, Oh My: similarities and differences in summary measures of population Health. Annu Rev Public Health. 2002;23:115–134.11910057 10.1146/annurev.publhealth.23.100901.140513

35. Alternatives to QALY-Based Cost-Effectiveness Analysis for Determining the Value of Prescription Drugs and Other Health Interventions. National Council on Disability; 2022 https://ncd.gov/sites/default/files/NCD_Alternatives_to_the_QALY_508.pdf

36. SullivanSD LakdawallaDN DevineB, . Alternatives To The QALY For Comparative Effectiveness Research. Health Affairs Forefront 2023 https://www.healthaffairs.org/do/10.1377/forefront.20230419.896238

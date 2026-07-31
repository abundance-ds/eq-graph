---
project_id: "2016740"
work_id: "doi:10.3389/fpsyg.2023.1175402"
doi: "10.3389/fpsyg.2023.1175402"
pmid: "37860294"
pmcid: "PMC10583565"
title: "An investigation of age dependency in Dutch and Chinese values for EQ-5D-Y"
journal: "Frontiers in Psychology"
publication_date: "2023-10-03"
volume: "14"
authors:
  - name: "Brigitte Essers"
    affiliation_ids:
      - "aff1"
      - "aff2"
  - name: "Pei Wang"
    affiliation_ids:
      - "aff3"
  - name: "Elly Stolk"
    affiliation_ids:
      - "aff4"
  - name: "Marcel F Jonker"
    affiliation_ids:
      - "aff5"
  - name: "Silvia Evers"
    affiliation_ids:
      - "aff2"
  - name: "Manuela Joore"
    affiliation_ids:
      - "aff1"
      - "aff2"
  - name: "Carmen Dirksen"
    affiliation_ids:
      - "aff1"
      - "aff2"
affiliations:
  - id: "aff1"
    name: "Department of Clinical Epidemiology and Medical Technology Assessment, Maastricht University Medical Centre, Maastricht, Netherlands"
  - id: "aff2"
    name: "Care and Public Health Research Institute (CAPHRI), Maastricht, Netherlands"
  - id: "aff3"
    name: "School of Public Health, Fudan University, Shanghai, China"
  - id: "aff4"
    name: "EuroQol Research Foundation, Rotterdam, Netherlands"
  - id: "aff5"
    name: "Erasmus Choice Modelling Centre, Erasmus University Rotterdam, Rotterdam, Netherlands"
licence: "cc-by"
source_file: "input/projects/2016740/papers/doi_10.3389_fpsyg.2023.1175402.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10583565/fullTextXML"
source_method: "epmc_xml"
source_sha256: "b5f16015e4cf213f55bb353411e9db2e19d1b2d1754241869a7b403246205ba2"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# An investigation of age dependency in Dutch and Chinese values for EQ-5D-Y

## Abstract

### Aims

The primary aim was to explore the age dependency of health state values derived via trade-offs between health-related quality of life (HRQoL) and life years in a discrete choice experiment (DCE). The secondary aim was to explore if people weigh life years and HRQoL differently for children, adolescents, adults, and older adults.

### Methods

Participants from the general population of the Netherlands and China first completed a series of choice tasks offering choices between two EQ-5D-Y states with a given lifespan. The choice model captured the value of a year in full health, disutility determined by EQ-5D-Y, and a discount rate. Next, they received a slightly different choice task, offering choices between two lives that differed in HRQoL and life expectancy but produced the same number of quality-adjusted life years (QALYs). Participants were randomly assigned to fill out the survey for three or four age frames: a hypothetical person of 10, 15, 40, and 70 years (the last one only applicable to China) to allow the age dependency of the responses to be explored.

### Results

A total of 1,234 Dutch and 1,818 Chinese people administered the survey. Controlling for time preferences, we found that the agreement of health state values for different age frames was generally stronger in the Netherlands than in China. We found no clear pattern of differences in the QALY composition in both samples. The probability distribution over response options varied most when levels for lifespan or severity were at the extremes of the spectrum.

### Conclusion/discussion

The magnitude and direction of age effects on values seemed dimension- and country specific. In the Netherlands, we found a few differences in dimension-specific weights elicited for 10- and 15-year-olds compared to 40-year-olds, but the overall age dependency of values was limited. A stronger age dependency of values was observed in China, where values for 70-year-olds differed strongly from the values for other ages. The appropriateness of using existing values beyond the age range for which they were measured needs to be evaluated in the local context.

**Keywords:** health state values, age-dependency, health related quality of life, children, EQ-5D-Y

Received 2023 Feb 27; Accepted 2023 Sep 11; Collection date 2023.

## Introduction

In recent years, the demand for pediatric multi-attribute utility instruments has grown (Chen and Ratcliffe, 2015). One of these utility instruments is the EQ-5D-Youth (EQ-5D-Y), a child-friendly version of the well-known adult questionnaire EQ-5D-3L (Wille et al., 2010). It contains the same five health dimensions, although the wording of three of them (i.e., self-care, anxiety, and usual activities) has been modified in order to fit the needs of the younger respondent. A VAS scale is also included, with endpoints of 0 (the worst health you can imagine) and 100 (the best health you can imagine). The EQ-5D-Y questionnaire can be filled out by children from the age of 8, while for children aged 4–7, a proxy version can be applied. EQ-5D-Y value sets are currently available for nine countries (Devlin et al., 2022).

Key challenges in the area of child health valuation are the impact of different perspectives, i.e., adult, adolescent, or child preferences, and the impact of different health state valuation methods (Rowen et al., 2020). The EQ-5D-Y valuation protocol requires that the general population should be asked to value the EQ-5D-Y health states as proxies for children. People no longer value the health state of a person like themselves but of a 10-year-old hypothetical child. To date, it is unknown whether the obtained values will be sensitive to the specified age of the hypothetical child (e.g., a child aged 10 or an adolescent aged 15), and if so, what framing of age is optimal.

The available evidence about the age dependency of health-related quality of life (HRQoL) values is limited. Kind et al. showed that by using the visual analog scale (VAS), the obtained values were lower for children when respondents were asked to imagine that a health state concerned a 10-year-old child compared to when they valued that state for themselves or another adult (Kind et al., 2015). These results suggest that health problems will affect a child's HRQoL more than an adult's HRQoL. However, the Kind's VAS values were obtained on a scale with the best and worst imaginable health states as the top and bottom anchors and not on the full health-dead scale required for the computation of quality-adjusted life years. Kreimeier et al. (2018) reported that TTO values for children exceed those for adults in the same health state. Shah et al. (2020) found the same result across a range of methods that all produced values on the full health-dead scale.

To better understand the age dependency of HRQoL values, we need to carefully examine the context and meaning of responses given to questions, especially when they involve a time trade-off. Because TTO values are derived from a trade-off between HRQoL and time, HRQoL values are confounded with preferences for time. As a result, differences in TTO values for adults and children have a clear interpretation: Are changes in health affecting children's HRQoL less, or are variations in time preferences impacting the difference as well? This issue needs to be investigated further in order to better understand differences in health state values for children, adolescents, adults, and/or older adults and to advance valuation methods.

The main objective of our research was to examine how age impacts the valuation of EQ-5D-Y health states using a discrete choice experiment (DCE) that included a duration attribute. The second objective was to study if there are cultural differences when valuing health states for children, adolescents, or adults. The third objective was to explore if people attach different relative weights to life years and quality of life for children, adolescents, adults, and older adults.

## Methods

### Strategy

Respondents in the Netherlands were randomized over three arms that only differed by the framing of the valuation task with respect to the age of the hypothetical person that would experience the health states: 10 years (arm 1), 15 years (arm 2), or 40 years (arm 3), representing a child, an adolescent, and an adult. The study in China adopted the same study design as used in the Netherlands and extended it with a fourth study arm focused on older adults over 70 years. This was done to increase the contrast between arms and increase knowledge of the validity and valuation of the EQ-5D in the elderly population. Respondents in both countries completed two tasks. First, they received a series of questions from a discrete choice experiment featuring EQ-5D-Y health states with an associated duration. Next, respondents received a series of questions asking about their preferences for a “QALY composition”. Details of both tasks are provided below. Approval for this study was given by the Ethics Committees of the University of Maastricht and the Institutional Review Board of Fudan University School of Public Health before the start of the study. Data collection took place between August and December 2017 in the Netherlands and between May and July 2019 in China.

### EQ-5D-Y

EQ-5D-Y is a five-dimensional measure of health-related quality of life, derived from EQ-5D (Wille et al., 2010). The included dimensions are mobility, looking after myself, doing usual activities, having pain or discomfort, and feeling worried, sad, or unhappy. Each dimension has three levels: no problems, some problems, and a lot of problems.

### Sample

In the Netherlands, respondents were recruited from a commercial panel “Panelinzicht”. Each respondent received an invitation with a link to participate in the survey. To make sure the sample was representative of the Dutch population, stratified sampling was applied. This means that three strata were defined beforehand: age (with 18 years as a minimum age), gender, and education. Based on the classification as used by Statistics Netherlands (Centraal Bureau voor de Statistiek), the eight levels of education were divided into lower, middle, and higher education. In China, the respondents were enrolled by Survey Engine, and quota sampling was used to generate a representative sample of the general adult population in terms of age and gender.

### The survey

The online survey was developed by Survey Engine in both countries, with the Dutch version being translated into a Chinese version. It started with three questions regarding birth date, gender, and education. Subsequently, respondents were asked to describe their own health based on the EQ-5D-3L and the VAS scale. Then, the objective of the study was explained, and respondents were asked to fill in 15 choice tasks from a discrete choice experiment (DCE). The choice tasks were formatted as matched pairwise choices, following Jonker et al. (2017). This means that they first were asked which of two EQ-5D-Y states, A or B, they preferred for either a 10-year-old child, a 15-year-old adolescent, a 40-year-old adult, or a 70 year old (Chinese version). Both options differed in health but shared an equal life span. Next, they were asked to choose between health states B and C. C represented perfect health, i.e., no problems in any of the five EQ-5D-Y dimensions, but always offered fewer life years compared to B. To make the choice task easier, color coding was applied, with more severe problems darker colored and less severe problems lighter colored (Jonker et al., 2018a). After finishing the DCE, feasibility questions were presented, which means that respondents were asked whether they experienced any difficulties when choosing between A or B and B or C. Examples of both choice sets are presented in <a href="#F1" data-ref-type="fig">Figures 1</a>, <a href="#F2" data-ref-type="fig">2</a>.

<figure id="F1">
<p><img src="fpsyg-14-1175402-g0001.jpg" /></p>
<p><img src="fpsyg-14-1175402-g0001.gif" /></p>
<figcaption>Example choice set health state A and B.</figcaption>
</figure>

<figure id="F2">
<p><img src="fpsyg-14-1175402-g0002.jpg" /></p>
<p><img src="fpsyg-14-1175402-g0002.gif" /></p>
<figcaption>Example choice set health state B and C.</figcaption>
</figure>

Next, we presented a slightly different choice task, that we dubbed a “QALY composition task”. Eight QALY composition tasks were administered. We developed the task to let responses directly tell if people weigh life years and quality of life differently for children, adolescents, adults, or older adults. The QALY composition task involved choices between different ways of achieving a similar QALY total \[e.g., life A 2 years in full health (100% QoL) vs. life B 4 years in 50% QoL\]. Respondents could indicate their preference for life A or life B on a 5-point Likert scale, varying from a very strong preference for life A to a very strong preference for life B. An example of a QALY task is presented in <a href="#F3" data-ref-type="fig">Figure 3</a>. Eight QALY composition tasks were administered. We developed the task to explore if the relative weights attached to time and HRQoL vary for children, adolescents, adults, or older adults.

<figure id="F3">
<p><img src="fpsyg-14-1175402-g0003.jpg" /></p>
<p><img src="fpsyg-14-1175402-g0003.gif" /></p>
<figcaption>Example QALY composition task.</figcaption>
</figure>

At the end of the survey, a number of background questions were asked: employment status, experience in working with children, having children, experience with serious illness of a child, experience with own health during youth, having brother(s) and/or sister(s), experience with serious illness in sibling(s), whether it would have been worse or not if the respondent would have experienced the health states described in the survey instead of the hypothetical 10, 15, 40, or 70-year-olds, what kind of child, adolescent, adult, or older adult they were thinking of when answering the choice tasks, and what kind of religion they belonged to.

### Experimental design DCE

An experimental design with 150 matched pair-wise choice questions was generated using a two-step approach. The EQ-5D-Y states featured as options A and B were selected first, subsequently, option C was added, and in a separate step, the duration levels associated with options A, B, and C were selected. This two-step approach was used to promote consistency with a UK study that used a DCE without duration (Mott et al., 2021 plenary meeting of EuroQoL). Briefly, A and B were selected using an algorithm to create a Bayesian efficient design programmed in Stata. The candidate set was restricted to pairs that had overlapping severity levels in two dimensions. The design accounted for the main effects and two-way interactions. The initial design was created without priors, but data collection was paused two times to allow interim analysis of the data. The obtained coefficients were used as priors to update a design for the next round of data collection. As mentioned above, the C alternative always referred to full health, and hence dominated A and B in terms of quality of life, but was paired with a shorter duration, implying a time trade-off question. The selection of the levels of duration associated with A and B (the same level) and with C (a shorter duration) was also informed by a Bayesian efficient design algorithm (cf.), but this part was programmed in C++ because the utility function accounted for possible non-linearities in preferences for time (i.e., discounting), which standard software packages such as NGENE or STATA could both not handle (Jonker et al., 2018b).

Blocking was applied to divide the 150 matched pairwise choice tasks into 10 blocks, with each block containing 15 pairwise comparisons.

#### Experimental design QALY composition task

The QALY composition task was constructed on the basis of an orthogonal array. The four variables linked to the orthogonal array were:

1.  Life years of a (levels: 2, 4, 6, or 8)

2.  Quality of life of a (levels 0.2, 0.4, 0.6, and 0.8)

3.  Quality of life of b (levels 0.2, 0.5, and 0.7, 1) and

4.  The ratio of total QALYs in a/b (levels 0.8, 1.0, and 1.2).

Together, these four variables were used to define the life years of B, as indicated in <a href="#T1" data-ref-type="table">Table 1</a>. The scenarios presented to respondents in the QALY composition tasks were defined by the variables in the shaded columns. Three variables were directly obtained from the orthogonal array, and the fourth (life years in option B) was computed by matching the information of the first three variables with the QALY multiplier. This procedure ensured that decision rules based on longest life, highest quality of life, or maximum number of QALYs would produce different results.

<div id="T1" class="table-wrap">

<div class="caption">

Design QALY composition tasks.

</div>

| **Scenarios** | **Life years A** | **Qol A** | **Qol B** | **QALY multiplier** | **Life years B<sup>\*</sup>** |
|----|----|----|----|----|----|
| 1 | 2 | 0.2 | 0.25 | 0.8 | 1.5 |
| 2 | 4 | 0.6 | 1 | 1 | 2.5 |
| 3 | 6 | 0.8 | 0.5 | 1 | 10.0 |
| 4 | 8 | 0.4 | 0.7 | 1.2 | 5.5 |
| 5 | 4 | 0.4 | 0.5 | 0.8 | 2.5 |
| 6 | 2 | 0.8 | 0.7 | 1 | 2.3 |
| 7 | 8 | 0.6 | 0.2 | 1 | 24.0 |
| 8 | 6 | 0.2 | 1 | 1.2 | 1.5 |
| 9 | 6 | 0.6 | 0.7 | 0.8 | 4.0 |
| 10 | 8 | 0.2 | 0.5 | 1 | 3.0 |
| 11 | 2 | 0.4 | 1 | 1 | 0.8 |
| 12 | 4 | 0.8 | 0.2 | 1.2 | 19.0 |
| 13 | 8 | 0.8 | 1 | 0.8 | 5.0 |
| 14 | 6 | 0.4 | 0.2 | 1 | 12.0 |
| 15 | 4 | 0,2 | 0.7 | 1 | 1.2 |
| 16 | 2 | 0,6 | 0.5 | 1.2 | 3.0 |

<sup>\*</sup>Numbers are rounded up for convenience.

</div>

### Framing of the survey for the age groups

Exactly, the same DCE design and design of the QALY composition task were used in all arms. The only difference between arms was that respondents were asked to imagine that the health states applied for a different hypothetical person, aged 10, 15, 40, or 70 years. We used the wording of the EQ-5D-Y questionnaire to describe the health states of all arms. Only the examples mentioned between brackets for the dimension usual activities were taken from the adult version of the EQ-5D-3L for the 40-year and 70-year-old arm. For every respondent, randomization was applied per arm, per block, per choice task, and in the left-right order of the health states A and B.

### Data analysis

#### Data quality management

We retained respondents in the sample if they had completed the DCE survey and were not classified as speeders. Speeders were removed from the sample using a speeding threshold set at 530 s for the entire survey. We set this relatively low threshold to account for the fact that choice questions in a DCE repeat much of their content and to avoid undue exclusion of valid responses.

#### Discrete choice experiment

Logistic regression was used to analyze the respondent's DCE choices (STATA version 14). The parameters of the conditional logit model were estimated using maximum likelihood estimation. Conceptually, the utility that the respondent *n* obtains from alternative *j* in a choice task *t* is computed as the utility obtained from the health state characteristics X<sub>njt</sub> with their accompanying preference parameters (β<sub>n</sub>), multiplied by the net present value (NPV<sub>njt</sub>) of the number of years T<sub>njt</sub> associated with that health states, i.e.,

``` math
\begin{array}{l}
{\text{U}_{\text{njt}} = {({\text{β}_{\text{n}.}\text{X}_{\text{njt}}})}_{.}\text{NP}\text{V}_{\text{njt}} + \text{ε}_{\text{njt}}}
\end{array}
```

An exponential discount function was used to compute NPV (Jonker et al., 2018b), which defines NPV by the discount rate r, i.e.,

``` math
\begin{array}{l}
{\text{NP}\text{V}_{\text{ita}} = {({1 - \text{exp}{({- \text{r~~}\text{T}_{\text{ita}}})}})}/{({\text{exp}{(\text{r})} - 1})}\ \textit{if~r} \neq 0}
\end{array}
```

Dummy coding was applied for the levels of the EQ-5D-Y with no problems as a reference level. The coefficients from formula 1 that are associated with the dimension severity levels can be converted to the preferred scale for QALY computation, by dividing the relevant β<sub>n</sub> by the preference parameter associated with years, based on the Net present value computation.

#### Feasibility

Feasibility questions for the DCE were analyzed with descriptive statistics in SPSS version 16.

#### QALY composition

The QALY composition task provided ordinal responses on a 5-point Likert scale. By arm, we computed and compared the percentages of responses in each category. We graphically display the results using horizontally stacked bars. Because minimal differences were found, no attempt was made to study differences across arms using non-parametric tests.

## Results

### Characteristics of the sample

In total, 5,126 Dutch and 4,128 Chinese respondents started the survey, with 1,730 or 2,494 respondents completing it, resulting in a response rate of 34 and 60%, respectively. A total of 496 people were excluded from the Dutch sample as speeders and 676 from the Chinese sample. After these exclusions, the Dutch sample had *N* = 438 respondents in arm 1 (10 years old), *N* = 450 in arm 2 (15 years old), and 346 (40 years old) in arm 3. The final Chinese sample had 454, 455, 454, and 455 respondents in arms 1 (10 years old), 2 (15 years old), 3 (40 years old), and 4 (70 years old), respectively. Sample characteristics are presented in <a href="#T2" data-ref-type="table">Tables 2A</a>, <a href="#T2" data-ref-type="table">B</a>. The samples were representative of the populations in terms of sex and age, although the percentage of respondents with lower education in the Netherlands was smaller compared to the population as registered by the Dutch National Bureau Of Statistics (CBS), while in the Chinese sample, the percentage of respondents with college and higher education was much higher compared to Chinese norms (CotSNPCNE, n.d.).

<div id="T2" class="table-wrap">

<div class="caption">

Characteristics study samples.

</div>

<table>
<thead>
<tr>
<th></th>
<th style="text-align: center;"><strong>10 year old</strong></th>
<th style="text-align: center;"><strong>15 year old</strong></th>
<th style="text-align: center;"><strong>40 year old</strong></th>
<th colspan="2" style="text-align: center;"><strong>Dutch population</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;"><strong>A. Netherlands</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Age</strong></td>
<td style="text-align: center;"><em>N</em> = 438</td>
<td style="text-align: center;"><em>N</em> = 450</td>
<td style="text-align: center;"><em>N</em> = 346</td>
<td colspan="2" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">18–25</td>
<td style="text-align: center;">36 (8%)</td>
<td style="text-align: center;">38 (8%)</td>
<td style="text-align: center;">28 (8%)</td>
<td colspan="2" style="text-align: left;">15%</td>
</tr>
<tr>
<td style="text-align: left;">25–35</td>
<td style="text-align: center;">49 (11%)</td>
<td style="text-align: center;">54 (12%)</td>
<td style="text-align: center;">39 (11%)</td>
<td colspan="2" style="text-align: left;">15%</td>
</tr>
<tr>
<td style="text-align: left;">35–45</td>
<td style="text-align: center;">60 (14%)</td>
<td style="text-align: center;">55 (12%)</td>
<td style="text-align: center;">45 (13%)</td>
<td colspan="2" style="text-align: left;">15%</td>
</tr>
<tr>
<td style="text-align: left;">45–55</td>
<td style="text-align: center;">84 (19%)</td>
<td style="text-align: center;">87 (19%)</td>
<td style="text-align: center;">63 (18%)</td>
<td colspan="2" style="text-align: left;">18%</td>
</tr>
<tr>
<td style="text-align: left;">55–65</td>
<td style="text-align: center;">80 (18%)</td>
<td style="text-align: center;">82 (18%)</td>
<td style="text-align: center;">70 (20%)</td>
<td colspan="2" style="text-align: left;">16%</td>
</tr>
<tr>
<td style="text-align: left;">65–75</td>
<td style="text-align: center;">73 (17%)</td>
<td style="text-align: center;">77 (17%)</td>
<td style="text-align: center;">57 (16%)</td>
<td colspan="2" style="text-align: left;">13%</td>
</tr>
<tr>
<td style="text-align: left;">&gt;75</td>
<td style="text-align: center;">56 (13%)</td>
<td style="text-align: center;">57 (13%)</td>
<td style="text-align: center;">44 (13%)</td>
<td colspan="2" style="text-align: left;">9%</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Education</strong></td>
</tr>
<tr>
<td style="text-align: left;">None</td>
<td style="text-align: center;">1 (0%)</td>
<td style="text-align: center;">0 (0%)</td>
<td style="text-align: center;">2 (1%)</td>
<td colspan="2" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Lower</td>
<td style="text-align: center;">95 (22%)</td>
<td style="text-align: center;">107 (24%)</td>
<td style="text-align: center;">70 (20%)</td>
<td colspan="2" style="text-align: left;">31%</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">186 (42%)</td>
<td style="text-align: center;">185 (41%)</td>
<td style="text-align: center;">165 (48%)</td>
<td colspan="2" style="text-align: left;">40%</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">137 (31%)</td>
<td style="text-align: center;">139 (31%)</td>
<td style="text-align: center;">98 (28%)</td>
<td colspan="2" style="text-align: left;">28%</td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: center;">19 (4%)</td>
<td style="text-align: center;">19 (4%)</td>
<td style="text-align: center;">11 (3%)</td>
<td colspan="2" style="text-align: left;">1%</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Sex</strong></td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">192 (44%)</td>
<td style="text-align: center;">198 (44%)</td>
<td style="text-align: center;">153 (44%)</td>
<td colspan="2" style="text-align: left;">51%</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">246 (56%)</td>
<td style="text-align: center;">252 (56%)</td>
<td style="text-align: center;">193 (56%)</td>
<td colspan="2" style="text-align: left;">49%</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Having children</strong></td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">272 (63%)</td>
<td style="text-align: center;">278 (63%)</td>
<td style="text-align: center;">218 (64%)</td>
<td colspan="2" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td style="text-align: center;">163 (37%)</td>
<td style="text-align: center;">164 (7%)</td>
<td style="text-align: center;">124 (6%)</td>
<td colspan="2" style="text-align: left;"></td>
</tr>
<tr>
<td></td>
<td style="text-align: center;"><strong>10 year old</strong></td>
<td style="text-align: center;"><strong>15 year old</strong></td>
<td style="text-align: center;"><strong>40 year old</strong></td>
<td style="text-align: center;"><strong>70 year old</strong></td>
<td style="text-align: center;"><strong>Chinese norms</strong></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>B. China</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Age</strong></td>
<td style="text-align: center;"><em>N</em> = 454</td>
<td style="text-align: center;"><em>N</em> = 455</td>
<td style="text-align: center;"><em>N</em> = 454</td>
<td style="text-align: center;"><em>N</em> = 455</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">18–25</td>
<td style="text-align: center;">83 (18%)</td>
<td style="text-align: center;">78 (17%)</td>
<td style="text-align: center;">81 (18%)</td>
<td style="text-align: center;">81 (18%)</td>
<td style="text-align: center;">10%</td>
</tr>
<tr>
<td style="text-align: left;">25–35</td>
<td style="text-align: center;">110 (24%)</td>
<td style="text-align: center;">111 (24%)</td>
<td style="text-align: center;">107 (24%)</td>
<td style="text-align: center;">97 (21%)</td>
<td style="text-align: center;">17%</td>
</tr>
<tr>
<td style="text-align: left;">35–45</td>
<td style="text-align: center;">104 (23%)</td>
<td style="text-align: center;">102 (22%)</td>
<td style="text-align: center;">106 (23%)</td>
<td style="text-align: center;">97 (21%)</td>
<td style="text-align: center;">15%</td>
</tr>
<tr>
<td style="text-align: left;">45–55</td>
<td style="text-align: center;">64 (14%)</td>
<td style="text-align: center;">69 (15%)</td>
<td style="text-align: center;">67 (15%)</td>
<td style="text-align: center;">79 (17%)</td>
<td style="text-align: center;">18%</td>
</tr>
<tr>
<td style="text-align: left;">55–65</td>
<td style="text-align: center;">57 (13%)</td>
<td style="text-align: center;">55 (12%)</td>
<td style="text-align: center;">56 (12%)</td>
<td style="text-align: center;">52 (11%)</td>
<td style="text-align: center;">11%</td>
</tr>
<tr>
<td style="text-align: left;">65–75</td>
<td style="text-align: center;">30 (7%)</td>
<td style="text-align: center;">34 (7%)</td>
<td style="text-align: center;">35 (8%)</td>
<td style="text-align: center;">46 (10%)</td>
<td style="text-align: center;">7%</td>
</tr>
<tr>
<td style="text-align: left;">&gt;75</td>
<td style="text-align: center;">6 (1%)</td>
<td style="text-align: center;">6 (1%)</td>
<td style="text-align: center;">2 (0%)</td>
<td style="text-align: center;">3 (1%)</td>
<td style="text-align: center;">4%</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Education</strong></td>
</tr>
<tr>
<td style="text-align: left;">None</td>
<td style="text-align: center;">2 (0%)</td>
<td style="text-align: center;">1 (0%)</td>
<td style="text-align: center;">1 (0%)</td>
<td style="text-align: center;">1 (0%)</td>
<td style="text-align: center;">11%</td>
</tr>
<tr>
<td style="text-align: left;">Primary school</td>
<td style="text-align: center;">3 (1%)</td>
<td style="text-align: center;">5 (1%)</td>
<td style="text-align: center;">4 (1%)</td>
<td style="text-align: center;">4 (1%)</td>
<td style="text-align: center;">25%</td>
</tr>
<tr>
<td style="text-align: left;">Middle school</td>
<td style="text-align: center;">15 (3%)</td>
<td style="text-align: center;">17 (4%)</td>
<td style="text-align: center;">16 (4%)</td>
<td style="text-align: center;">20 (4%)</td>
<td style="text-align: center;">35%</td>
</tr>
<tr>
<td style="text-align: left;">High school</td>
<td style="text-align: center;">71 (16%)</td>
<td style="text-align: center;">88 (19%)</td>
<td style="text-align: center;">80 (18%)</td>
<td style="text-align: center;">93 (20%)</td>
<td style="text-align: center;">15%</td>
</tr>
<tr>
<td style="text-align: left;">College and above</td>
<td style="text-align: center;">363 (80%)</td>
<td style="text-align: center;">344 (76%)</td>
<td style="text-align: center;">353 (78%)</td>
<td style="text-align: center;">337 (74%)</td>
<td style="text-align: center;">15%</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Sex</strong></td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">225 (50%)</td>
<td style="text-align: center;">222 (49%)</td>
<td style="text-align: center;">219 (48%)</td>
<td style="text-align: center;">239 (53%)</td>
<td style="text-align: center;">51%</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">229 (50%)</td>
<td style="text-align: center;">233 (51%)</td>
<td style="text-align: center;">235 (52%)</td>
<td style="text-align: center;">216 (47%)</td>
<td style="text-align: center;">49%</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><strong>Having children</strong></td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">298 (66%)</td>
<td style="text-align: center;">281 (62%)</td>
<td style="text-align: center;">285 (63%)</td>
<td style="text-align: center;">286 (63%)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td style="text-align: center;">79 (17%)</td>
<td style="text-align: center;">83 (18%)</td>
<td style="text-align: center;">70 (15%)</td>
<td style="text-align: center;">93 (20%)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Unknown/missing</td>
<td style="text-align: center;">77 (17%)</td>
<td style="text-align: center;">91 (20%)</td>
<td style="text-align: center;">99 (22%)</td>
<td style="text-align: center;">76 (17%)</td>
<td></td>
</tr>
</tbody>
</table>

</div>

### Feasibility

<a href="#T3" data-ref-type="table">Tables 3A</a>, <a href="#T3" data-ref-type="table">B</a> shows the answers related to the feasibility questions. In the Netherlands, 53% of the 10-year-old arm felt it was difficult to choose between health states A and B, compared to 45% of the adolescent arm and 34% of the adult arm. In addition, when making a choice between an impaired health state B and perfect health state C but with a shorter life duration, 58% of the respondents in the child arm and 49% in the adolescent arm answered that it was difficult to very difficult compared 43% in the adult arm. On the contrary, respondents across the four arms in China felt the degree of difficulty was similar.

<div id="T3" class="table-wrap">

<div class="caption">

Feasibility questions.

</div>

<table>
<thead>
<tr>
<th></th>
<th style="text-align: center;"><strong>10-year old</strong></th>
<th style="text-align: center;"><strong>15 year old</strong></th>
<th colspan="2" style="text-align: left;"><strong>40 year old</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;"><strong>A. Netherlands</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Difficulty choosing between health state A and B</strong></td>
<td style="text-align: center;"><em>N</em> = 438</td>
<td style="text-align: center;"><em>N</em> = 448</td>
<td colspan="2" style="text-align: left;"><em>N</em> = 346</td>
</tr>
<tr>
<td style="text-align: left;">Very difficult</td>
<td style="text-align: center;">55 (13%)</td>
<td style="text-align: center;">25 (6%)</td>
<td colspan="2" style="text-align: left;">15 (4%)</td>
</tr>
<tr>
<td style="text-align: left;">Difficult</td>
<td style="text-align: center;">176 (40%)</td>
<td style="text-align: center;">175 (39%)</td>
<td colspan="2" style="text-align: left;">103 (30%)</td>
</tr>
<tr>
<td style="text-align: left;">Neutral</td>
<td style="text-align: center;">134 (31%)</td>
<td style="text-align: center;">171 (38%)</td>
<td colspan="2" style="text-align: left;">164 (47%)</td>
</tr>
<tr>
<td style="text-align: left;">Easy</td>
<td style="text-align: center;">71 (16%)</td>
<td style="text-align: center;">67 (15%)</td>
<td colspan="2" style="text-align: left;">57 (16%)</td>
</tr>
<tr>
<td style="text-align: left;">Very easy</td>
<td style="text-align: center;">2 (0%)</td>
<td style="text-align: center;">10 (2%)</td>
<td colspan="2" style="text-align: left;">7 (2%)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Difficulty choosing between health state B and C</strong></td>
<td style="text-align: center;"><em>N</em> = 438</td>
<td style="text-align: center;"><em>N</em> = 448</td>
<td colspan="2" style="text-align: left;"><em>N</em> = 346</td>
</tr>
<tr>
<td style="text-align: left;">Very difficult</td>
<td style="text-align: center;">82 (19%)</td>
<td style="text-align: center;">66 (15%)</td>
<td colspan="2" style="text-align: left;">40 (12%)</td>
</tr>
<tr>
<td style="text-align: left;">Difficult</td>
<td style="text-align: center;">172 (39%)</td>
<td style="text-align: center;">155 (35%)</td>
<td colspan="2" style="text-align: left;">110 (32%)</td>
</tr>
<tr>
<td style="text-align: left;">Neutral</td>
<td style="text-align: center;">116 (26%)</td>
<td style="text-align: center;">126 (28%)</td>
<td colspan="2" style="text-align: left;">93 (27%)</td>
</tr>
<tr>
<td style="text-align: left;">Easy</td>
<td style="text-align: center;">56 (13%)</td>
<td style="text-align: center;">79 (18%)</td>
<td colspan="2" style="text-align: left;">85 (24%)</td>
</tr>
<tr>
<td style="text-align: left;">Very easy</td>
<td style="text-align: center;">12 (3%)</td>
<td style="text-align: center;">22 (5%)</td>
<td colspan="2" style="text-align: left;">18 (5%)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Would your choices have been different if the health problems concerned yourself instead of a hypothetical person?</strong></td>
<td style="text-align: center;"><em>N</em> = 435</td>
<td style="text-align: center;"><em>N</em> = 441</td>
<td colspan="2" style="text-align: left;"><em>N</em> = 341</td>
</tr>
<tr>
<td style="text-align: left;">Yes, health problems for myself worse</td>
<td style="text-align: center;">16 (4%)</td>
<td style="text-align: center;">14 (3%)</td>
<td colspan="2" style="text-align: left;">23 (7%)</td>
</tr>
<tr>
<td style="text-align: left;">Yes, loss life years for myself worse</td>
<td style="text-align: center;">16 (4%)</td>
<td style="text-align: center;">20 (5%)</td>
<td colspan="2" style="text-align: left;">25 (7%)</td>
</tr>
<tr>
<td style="text-align: left;">Yes, health problems for myself less bad</td>
<td style="text-align: center;">59 (14%)</td>
<td style="text-align: center;">47 (11%)</td>
<td colspan="2" style="text-align: left;">10 (3%)</td>
</tr>
<tr>
<td style="text-align: left;">Yes, loss life years for myself less bad</td>
<td style="text-align: center;">61 (14%)</td>
<td style="text-align: center;">57 (13%)</td>
<td colspan="2" style="text-align: left;">14 (4%)</td>
</tr>
<tr>
<td style="text-align: left;">No, health problems for myself equally bad</td>
<td style="text-align: center;">104 (24%)</td>
<td style="text-align: center;">143 (32%)</td>
<td colspan="2" style="text-align: left;">163 (48%)</td>
</tr>
<tr>
<td style="text-align: left;">No, loss life years for myself equally bad</td>
<td style="text-align: center;">53 (12%)</td>
<td style="text-align: center;">55 (12%)</td>
<td colspan="2" style="text-align: left;">49 (14%)</td>
</tr>
<tr>
<td style="text-align: left;">I do not know</td>
<td style="text-align: center;">126 (29%)</td>
<td style="text-align: center;">105 (24%)</td>
<td colspan="2" style="text-align: left;">57 (17%)</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><strong>B. China</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Difficulty choosing between health state A and B</strong></td>
<td style="text-align: center;"><em>N</em> = 390</td>
<td style="text-align: center;"><em>N</em> =3 76</td>
<td style="text-align: center;"><em>N</em> = 368</td>
<td style="text-align: center;"><em>N</em> = 389</td>
</tr>
<tr>
<td style="text-align: left;">Very difficult</td>
<td style="text-align: center;">21 (5%)</td>
<td style="text-align: center;">22 (6%)</td>
<td style="text-align: center;">11 (6%)</td>
<td style="text-align: center;">19 (5%)</td>
</tr>
<tr>
<td style="text-align: left;">Difficult</td>
<td style="text-align: center;">94 (24%)</td>
<td style="text-align: center;">87 (23%)</td>
<td style="text-align: center;">88 (23%)</td>
<td style="text-align: center;">86 (22%)</td>
</tr>
<tr>
<td style="text-align: left;">Neutral</td>
<td style="text-align: center;">126 (32%)</td>
<td style="text-align: center;">113 (30%)</td>
<td style="text-align: center;">114 (30%)</td>
<td style="text-align: center;">119 (31%)</td>
</tr>
<tr>
<td style="text-align: left;">Easy</td>
<td style="text-align: center;">113 (29%)</td>
<td style="text-align: center;">122 (32%)</td>
<td style="text-align: center;">118 (32%)</td>
<td style="text-align: center;">127 (33%)</td>
</tr>
<tr>
<td style="text-align: left;">Very easy</td>
<td style="text-align: center;">36 (9%)</td>
<td style="text-align: center;">32 (9%)</td>
<td style="text-align: center;">37 (9%)</td>
<td style="text-align: center;">38 (10%)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Difficulty choosing between health state B and C</strong></td>
<td style="text-align: center;"><em>N</em> = 390</td>
<td style="text-align: center;"><em>N</em> = 376</td>
<td style="text-align: center;"><em>N</em> = 368</td>
<td style="text-align: center;"><em>N</em> = 389</td>
</tr>
<tr>
<td style="text-align: left;">Very difficult</td>
<td style="text-align: center;">23 (6%)</td>
<td style="text-align: center;">28 (7%)</td>
<td style="text-align: center;">27 (7%)</td>
<td style="text-align: center;">27 (7%)</td>
</tr>
<tr>
<td style="text-align: left;">Difficult</td>
<td style="text-align: center;">97 (25%)</td>
<td style="text-align: center;">81 (22%)</td>
<td style="text-align: center;">66 (22%)</td>
<td style="text-align: center;">86 (22%)</td>
</tr>
<tr>
<td style="text-align: left;">Neutral</td>
<td style="text-align: center;">104 (27%)</td>
<td style="text-align: center;">99 (26%)</td>
<td style="text-align: center;">101 (26%)</td>
<td style="text-align: center;">85 (22%)</td>
</tr>
<tr>
<td style="text-align: left;">Easy</td>
<td style="text-align: center;">126 (32%)</td>
<td style="text-align: center;">121 (32%)</td>
<td style="text-align: center;">140 (32%)</td>
<td style="text-align: center;">138 (35%)</td>
</tr>
<tr>
<td style="text-align: left;">Very easy</td>
<td style="text-align: center;">40 (10%)</td>
<td style="text-align: center;">47 (13%)</td>
<td style="text-align: center;">34 (13%)</td>
<td style="text-align: center;">53 (14%)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Would your choices have been different if the health problems concerned yourself instead of a hypothetical person?</strong></td>
<td style="text-align: center;"><em>N</em> = 373</td>
<td style="text-align: center;"><em>N</em> = 361</td>
<td style="text-align: center;"><em>N</em> = 355</td>
<td style="text-align: center;"><em>N</em> = 374</td>
</tr>
<tr>
<td style="text-align: left;">Yes, health problems for myself worse</td>
<td style="text-align: center;">88 (24%)</td>
<td style="text-align: center;">96 (27%)</td>
<td style="text-align: center;">27% (104)</td>
<td style="text-align: center;">98 (26%)</td>
</tr>
<tr>
<td style="text-align: left;">Yes, loss life years for myself worse</td>
<td style="text-align: center;">111 (30%)</td>
<td style="text-align: center;">95 (26%)</td>
<td style="text-align: center;">26% (101)</td>
<td style="text-align: center;">119 (32%)</td>
</tr>
<tr>
<td style="text-align: left;">Yes, health problems for myself less worse</td>
<td style="text-align: center;">39 (10%)</td>
<td style="text-align: center;">34 (9%)</td>
<td style="text-align: center;">9% (44)</td>
<td style="text-align: center;">39 (10%)</td>
</tr>
<tr>
<td style="text-align: left;">Yes, loss life years for myself less worse</td>
<td style="text-align: center;">32 (9%)</td>
<td style="text-align: center;">31 (9%)</td>
<td style="text-align: center;">9% (27)</td>
<td style="text-align: center;">40 (11%)</td>
</tr>
<tr>
<td style="text-align: left;">No, health problems for myself equally worse</td>
<td style="text-align: center;">60 (16%)</td>
<td style="text-align: center;">56 (16%)</td>
<td style="text-align: center;">16% (43)</td>
<td style="text-align: center;">28 (7%)</td>
</tr>
<tr>
<td style="text-align: left;">No, loss life years for myself equally worse</td>
<td style="text-align: center;">22 (6%)</td>
<td style="text-align: center;">28 (8%)</td>
<td style="text-align: center;">8% (17)</td>
<td style="text-align: center;">16 (4%)</td>
</tr>
<tr>
<td style="text-align: left;">I do not know</td>
<td style="text-align: center;">21 (6%)</td>
<td style="text-align: center;">21 (6%)</td>
<td style="text-align: center;">6% (19)</td>
<td style="text-align: center;">34 (9%)</td>
</tr>
</tbody>
</table>

</div>

The percentage of respondents answering that their choices would not have been different if they themselves had experienced the health states rather than a hypothetical child, adolescent, adult, or older person, varied across arms in the Netherlands (<a href="#T3" data-ref-type="table">Table 3A</a>). A total of 62% of the respondents in the adult arm indicated that answering the questions for themselves would have resulted in the same responses, vs. 36% in the child arm and 44% in the adolescent arm. In the child and adolescent arms, 28 and 24% of the people considered health problems or loss of life years *less bad for themselves*, whereas, in the adult arm, respondents more often considered these issues *worse for themselves*. In China, fewer people stated that their responses would have been the same if they were asked about preferences for themselves (11–24% varying across arms), and the majority (varying between 51 and 58%) of the people in all arms state that they would consider health problems or loss of life years worse for themselves (<a href="#T3" data-ref-type="table">Table 3B</a>).

### Results discrete choice experiment

<a href="#T4" data-ref-type="table">Tables 4A</a>, <a href="#T5" data-ref-type="table">B</a> shows the results of the regression model on a latent scale for the Netherlands and China. The parameter “years” reflects the additional utility gained from a life year without health problems, before discounting, and is positive—as expected. In both countries, results show that additional life years generate utility. The interaction terms in the Dutch regression model all have the expected negative sign, except mobility level 2, showing that a deviation from full health with no problems is considered negative. The interaction terms for level 2 problems on the dimensions of self-care, usual activities, and pain/discomfort showed unexpected positive signs in China.

<div id="T4" class="table-wrap">

<div class="caption">

Results non-linear preferences on a latent scale Dutch population.

</div>

<table>
<thead>
<tr>
<th></th>
<th colspan="2" style="text-align: center;"><strong>10 year old</strong></th>
<th colspan="2" style="text-align: center;"><strong>15 year old</strong></th>
<th colspan="2" style="text-align: center;"><strong>40 year old</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
</tr>
<tr>
<td style="text-align: left;">Years</td>
<td style="text-align: center;">1.04</td>
<td style="text-align: center;">0.89; 1.19</td>
<td style="text-align: center;">1.12</td>
<td style="text-align: center;">0.98; 1.25</td>
<td style="text-align: center;">1.05</td>
<td style="text-align: center;">0.90; 1.20</td>
</tr>
<tr>
<td style="text-align: left;">Mo2<sup>*</sup>years</td>
<td style="text-align: center;">0.05</td>
<td style="text-align: center;">0.02; 0.08</td>
<td style="text-align: center;">0.06</td>
<td style="text-align: center;">0.04; 0.09</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.04; 0.11</td>
</tr>
<tr>
<td style="text-align: left;">Mo3<sup>*</sup>years</td>
<td style="text-align: center;">−0.07</td>
<td style="text-align: center;">−0.10; −0.05</td>
<td style="text-align: center;">−0.06</td>
<td style="text-align: center;">−0.09; −0.04</td>
<td style="text-align: center;">−0.09</td>
<td style="text-align: center;">−0.12; −0.06</td>
</tr>
<tr>
<td style="text-align: left;">Sc2<sup>*</sup>years<sup>*</sup></td>
<td style="text-align: center;">−0.01</td>
<td style="text-align: center;">−0.04; 0.01</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: center;">−0.02; 0.03</td>
<td style="text-align: center;">−0.01</td>
<td style="text-align: center;">−0.04; 0.02</td>
</tr>
<tr>
<td style="text-align: left;">Sc3<sup>*</sup>years</td>
<td style="text-align: center;">−0.12</td>
<td style="text-align: center;">−0.15; −0.09</td>
<td style="text-align: center;">−0.13</td>
<td style="text-align: center;">−0.15; −0.10</td>
<td style="text-align: center;">−0.14</td>
<td style="text-align: center;">−0.17; −0.11</td>
</tr>
<tr>
<td style="text-align: left;">Ua2<sup>*</sup>years</td>
<td style="text-align: center;">−0.06</td>
<td style="text-align: center;">−0.09; −0.04</td>
<td style="text-align: center;">−0.07</td>
<td style="text-align: center;">−0.10; −0.05</td>
<td style="text-align: center;">−0.05</td>
<td style="text-align: center;">−0.08; −0.03</td>
</tr>
<tr>
<td style="text-align: left;">Ua3<sup>*</sup>years</td>
<td style="text-align: center;">−0.32</td>
<td style="text-align: center;">−0.37; −0.28</td>
<td style="text-align: center;">−0.32</td>
<td style="text-align: center;">−0.36; −0.28</td>
<td style="text-align: center;">−0.28</td>
<td style="text-align: center;">−0.32; −0.24</td>
</tr>
<tr>
<td style="text-align: left;">Pd2<sup>*</sup>years</td>
<td style="text-align: center;">−0.14</td>
<td style="text-align: center;">−0.18; −0.11</td>
<td style="text-align: center;">−0.10</td>
<td style="text-align: center;">−0.13; −0.08</td>
<td style="text-align: center;">−0.08</td>
<td style="text-align: center;">−0.11; −0.06</td>
</tr>
<tr>
<td style="text-align: left;">Pd3<sup>*</sup>years</td>
<td style="text-align: center;">−0.54</td>
<td style="text-align: center;">−0.61; −0.47</td>
<td style="text-align: center;">−0.49</td>
<td style="text-align: center;">−0.54; −0.43</td>
<td style="text-align: center;">−0.44</td>
<td style="text-align: center;">−0.50; −0.38</td>
</tr>
<tr>
<td style="text-align: left;">Ad2<sup>*</sup>years</td>
<td style="text-align: center;">−0.19</td>
<td style="text-align: center;">−0.22; −0.15</td>
<td style="text-align: center;">−0.17</td>
<td style="text-align: center;">−0.20; −0.14</td>
<td style="text-align: center;">−0.16</td>
<td style="text-align: center;">−0.19; −0.12</td>
</tr>
<tr>
<td style="text-align: left;">Ad3<sup>*</sup>years</td>
<td style="text-align: center;">−0.64</td>
<td style="text-align: center;">−0.72; −0.56</td>
<td style="text-align: center;">−0.63</td>
<td style="text-align: center;">−0.69; −0.56</td>
<td style="text-align: center;">−0.57</td>
<td style="text-align: center;">−0.64; −0.49</td>
</tr>
<tr>
<td style="text-align: left;">Discount rate</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.22; 0.28</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.20; 0.25</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.19; 0.25</td>
</tr>
</tbody>
</table>

<sup>\*</sup>Indicate that this is an interaction between the domain like mobility and years as described under the heading results discrete choice experiment.

</div>

<div id="T5" class="table-wrap">

<div class="caption">

Results non-linear preferences on a latent scale Chinese population.

</div>

<table>
<thead>
<tr>
<th></th>
<th colspan="2" style="text-align: center;"><strong>10 year old</strong></th>
<th colspan="2" style="text-align: center;"><strong>15 year old</strong></th>
<th colspan="2" style="text-align: center;"><strong>40 year old</strong></th>
<th colspan="2" style="text-align: center;"><strong>70 year old</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
<td style="text-align: center;"><strong>Coefficient</strong></td>
<td style="text-align: center;"><strong>95% CI</strong></td>
</tr>
<tr>
<td style="text-align: left;">Years</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">0.23; 0.31</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.25; 0.33</td>
<td style="text-align: center;">0.33</td>
<td style="text-align: center;">0.29; 0.37</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.19; 0.27</td>
</tr>
<tr>
<td style="text-align: left;">Mo2<sup>*</sup>years</td>
<td style="text-align: center;">−0.01</td>
<td style="text-align: center;">−0.03; 0.02</td>
<td style="text-align: center;">−0.01</td>
<td style="text-align: center;">−0.03; 0.02</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: center;">−0.02; 0.03</td>
<td style="text-align: center;">−0.01</td>
<td style="text-align: center;">−0.04; 0.02</td>
</tr>
<tr>
<td style="text-align: left;">Mo3<sup>*</sup>years</td>
<td style="text-align: center;">−0.08</td>
<td style="text-align: center;">−0.10; 0.05</td>
<td style="text-align: center;">−0.10</td>
<td style="text-align: center;">−0.14; 0.06</td>
<td style="text-align: center;">−0.11</td>
<td style="text-align: center;">−0.15; −0.07</td>
<td style="text-align: center;">−0.09</td>
<td style="text-align: center;">−0.13; −0.05</td>
</tr>
<tr>
<td style="text-align: left;">Sc2<sup>*</sup>years</td>
<td style="text-align: center;">0.04</td>
<td style="text-align: center;">0.01; 0.08</td>
<td style="text-align: center;">0.03</td>
<td style="text-align: center;">0.02; 0.08</td>
<td style="text-align: center;">0.06</td>
<td style="text-align: center;">0.03; 0.09</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: center;">−0.01; 0.05</td>
</tr>
<tr>
<td style="text-align: left;">Sc3<sup>*</sup>years</td>
<td style="text-align: center;">−0.02</td>
<td style="text-align: center;">−0.04; 0.03</td>
<td style="text-align: center;">−0.02</td>
<td style="text-align: center;">−0.05; 0.01</td>
<td style="text-align: center;">−0.05</td>
<td style="text-align: center;">−0.08; −0.02</td>
<td style="text-align: center;">−0.06</td>
<td style="text-align: center;">−0.10; −0.02</td>
</tr>
<tr>
<td style="text-align: left;">Ua2<sup>*</sup>years</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: center;">−0.02; 0.03</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: center;">−0.02; 0.05</td>
<td style="text-align: center;">0.03</td>
<td style="text-align: center;">0.00; 0.06</td>
<td style="text-align: center;">0.03</td>
<td style="text-align: center;">−0.00; 0.06</td>
</tr>
<tr>
<td style="text-align: left;">Ua3<sup>*</sup>years</td>
<td style="text-align: center;">−0.04</td>
<td style="text-align: center;">−0.08; 0.00</td>
<td style="text-align: center;">−0.05</td>
<td style="text-align: center;">−0.08; 0.00</td>
<td style="text-align: center;">−0.05</td>
<td style="text-align: center;">−0.09; −0.01</td>
<td style="text-align: center;">−0.05</td>
<td style="text-align: center;">−0.09; −0.02</td>
</tr>
<tr>
<td style="text-align: left;">Pd2<sup>*</sup>years</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: center;">−0.02; 0.03</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: center;">−0.02; −0.03</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: center;">−0.02; 0.03</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: center;">−0.01; 0.05</td>
</tr>
<tr>
<td style="text-align: left;">Pd3<sup>*</sup>years</td>
<td style="text-align: center;">−0.08</td>
<td style="text-align: center;">−0.13; 0.00</td>
<td style="text-align: center;">−0.10</td>
<td style="text-align: center;">−0.14; 0.04</td>
<td style="text-align: center;">−0.10</td>
<td style="text-align: center;">−0.14; −0.06</td>
<td style="text-align: center;">−0.10</td>
<td style="text-align: center;">−0.12; −0.06</td>
</tr>
<tr>
<td style="text-align: left;">Ad2<sup>*</sup>years</td>
<td style="text-align: center;">−0.00</td>
<td style="text-align: center;">−0.03; 0.02</td>
<td style="text-align: center;">−0.03</td>
<td style="text-align: center;">−0.06; 0.00</td>
<td style="text-align: center;">−0.00</td>
<td style="text-align: center;">−0.03; 0.02</td>
<td style="text-align: center;">−0.03</td>
<td style="text-align: center;">−0.04; 0.00</td>
</tr>
<tr>
<td style="text-align: left;">Ad3<sup>*</sup>years</td>
<td style="text-align: center;">−0.14</td>
<td style="text-align: center;">−0.17; −0.11</td>
<td style="text-align: center;">−0.13</td>
<td style="text-align: center;">−0.17; −0.09</td>
<td style="text-align: center;">−0.13</td>
<td style="text-align: center;">−0.18; −0.08</td>
<td style="text-align: center;">−0.13</td>
<td style="text-align: center;">−0.17; −0.10</td>
</tr>
<tr>
<td style="text-align: left;">Discount rate</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.25; 0.33</td>
<td style="text-align: center;">0.33</td>
<td style="text-align: center;">0.28; 0.38</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.28; 0.36</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.27; 0.37</td>
</tr>
</tbody>
</table>

</div>

The estimated discount rate *r* varied between 0.22 and 0.25 across the arms in the Netherlands and was ~0.30 in China in all four arms, suggesting strong discounting of future health outcomes.

<a href="#F4" data-ref-type="fig">Figures 4A</a>, <a href="#F4" data-ref-type="fig">B</a> presents the results on a QALY scale (coefficient interaction term divided by coefficient years). Across arms in the Netherlands, we found a high level of agreement on the health state values, except for the dimensions of pain and discomfort and anxiety/depression; respondents traded-off *more* time to avoid these problems for children than for adults. The Chinese results showed that respondents traded-off more time to avoid severe problems in the 70-year arm.

<figure id="F4">
<p><img src="fpsyg-14-1175402-g0004.jpg" /></p>
<p><img src="fpsyg-14-1175402-g0004.gif" /></p>
<figcaption><strong>(A)</strong> Utility decrements per EQ-5D-Y dimension severity level in the Netherlands. <strong>(B)</strong> Utility decrements per EQ-5D-Y dimension severity level in China.</figcaption>
</figure>

The difference in values for the worst health state (33,333) resulted in −0.630 for children, −0.452 for adolescents, and −0.452 for adults in the Netherlands. On the contrary, older adults in China have a value of −0.870 for the worst state, followed by adolescents (−0.370), children (−0.340), and adults (−0.320).

### QALY composition

<a href="#F5" data-ref-type="fig">Figures 5A</a>, <a href="#F5" data-ref-type="fig">B</a> presents the distribution of the Likert responses by QALY composition task. We found no clear pattern of differences across arms in both countries. The distribution over response options varied most when the life years or quality of life were at the extremes of the spectrum. In the Netherlands, the only distinction between arms was that the percentage of responses in the third response category, indicating no preference for A or B, seemed to be the largest when the questions concerned a 10-year-old child. The Chinese results showed a larger percentage of respondents, indicating no preference between life A and life B compared to the Dutch data, with similar or even less clustering in the child's arm on the no preference option.

<figure id="F5">
<p><img src="fpsyg-14-1175402-g0005.jpg" /></p>
<p><img src="fpsyg-14-1175402-g0005.gif" /></p>
<figcaption><strong>(A)</strong> Distribution of likert responses by scenario in the Netherlands. <strong>(B)</strong> Distribution of likert responses by scenario in China.</figcaption>
</figure>

## Discussion

This study examined the impact of framing of age on values for EQ-5D-Y health states in the Netherlands and China. We tested this issue using a DCE duration approach and a task that assessed preferences for QALY composition. The empirical findings indicated that the values derived from the DCE duration task were similar in the Netherlands for children, adolescents, and adults (except for “pain”) and varied more for children, adolescents, adults, and older adults in China, where the lowest values were found in the group stating preferences for a 70-year-old person. Dutch people comparatively traded-off more time to avoid pain in children than for adults, resulting in lower values, while Chinese people were more willing to trade-off time to avoid any type of severe problem in the elderly compared to the other arms. The QALY composition task showed no clear differences in values for health across age groups.

No evidence for age dependency of health state values was found in the Netherlands. Our results for the 10-year-old arm are consistent with Kreimeier's TTO results (Kreimeier et al., 2018). Based on international results, Kreimeier reported that TTO values applied to children generally were higher compared to values of adults, but in that study, the Dutch results were an exception. In the Netherlands, people gave a lower TTO value to a health state when it concerned a 10 years old compared to themselves (Kreimeier et al., 2018). This indicates that Dutch respondents are prepared to trade-off life years against the quality of life for children. In our research, the results also showed that respondents were prepared to trade-off more time to avoid pain in children than in adults, resulting in lower values, although generally, the agreement of health state values for different ages was quite strong. While the congruence between studies supports the validity of our findings, care should still be taken when generalizing our results to other countries. Stronger evidence for age dependency of values was found in China, where the inclusion of the 70-year arm increased the contrast between groups.

Our estimation of health state utilities followed a state-of-the-art DCE duration approach, requiring a multiplicative utility function that involves a non-linear discount function. The estimated discount rates indicated that respondents valued quality of life in the short term more compared to the long term, which was anticipated, and as argued by Jonker and Bliemer (2019), valid health state utility values can only be obtained if the model adequately accounts for such time preferences. The estimated discount rates were, however, relatively high when compared to the standard rates usually applied in economic evaluations, especially in China. While the discount rates were still within the range of previously estimated discount rates for health-related outcomes (Attema et al., 2018), their reliability needs to be established in the future research. A limitation of the DCE duration method is that the best way to account for time preferences, especially in the presence of discounting, has not been identified. Discount rates can be computed in different ways. Models that account for non-linear time preferences are complex and have not been implemented yet in the standard software that we used for choice modeling, and this limits the modeling options (e.g., we cannot simultaneously account for preference heterogeneity and for non-linear time preferences). Furthermore, this way of assessing preferences places high demands on the design, necessitating interim design updates to ensure that the design is based on adequate priors, and the end results may still depend on the data quality obtained along the way. We excluded speeders *post-hoc*, not before design updates.

If we are examining preferences for a subject like a trade-off between life years and quality of life, we also need to carefully consider what advantages and disadvantages different valuation methods may have when used in such a context. We consider it possible that the use of TTO poses even greater challenges than the DCE of the required accuracy in rating health states and direct assessment. A specific result that may be worth noting is the larger clustering of responses in the child arm vs. the other arms on the no preference answer option in the QALY composition task in the Netherlands. This might indicate that a larger fraction of respondents in the child arm feel uncertain when trading-off quality of life and life years. However, it is also possible that respondents are neutral about their preference for either one of the options and consider them equivalent. Either way, it shows that more respondents in the child's arm were reserved when making a choice. However, it appears that the Chinese results showed a reversed pattern, with more respondents in the child's arms who were more certain to make a decision. The possible explanation may be a cultural difference: paternalism is more prevalent in China.

The findings of this study may be taken into consideration for future updates of the EQ-5D-Y valuation protocol. EQ-5D-Y values are currently elicited from adults who value health states accruing to a 10-year-old child (Ramos-Goñi et al., 2020). This study reflects on the appropriateness of using a specified age (here, 10 years of age) in the elicitation of values that are used across a wider age group by varying the specified age. Age dependency of values was limited in the Netherlands, suggesting that values elicited for a 10-year-old child may also be validly applied for a 15-year-old. However, in China, the values for 70-year-olds differed strongly from the values for other ages, suggesting that the appropriateness of using a fixed, specified age may be questioned. Moreover, many respondents indicated that their choices would have been different if the health state had been experienced by themselves rather than by someone else. This finding is in line with results from other studies (Lipman et al., 2021; Reckers-Droog et al., 2022). More research on the sensitivity of values to age and perspective is warranted.

## Conclusion

Age dependency was observed in the stated preferences for hypothetical health states. The magnitude and direction of age effects in values seemed dimension- and country-specific. In the Netherlands, we found a few differences in dimension-specific weights elicited for 10- and 15-year-olds compared to 40-year-olds, but the overall age dependency of values was limited. A stronger age dependency of values was observed in China, where values for 70-year-olds differed strongly from the values for other ages. The appropriateness of using existing values beyond the age range for which they were measured needs to be evaluated in the local context.

## Data availability statement

The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation.

## Ethics statement

The studies involving human participants were reviewed and approved by the Ethics Committees of the University Maastricht and Institutional Review Board of Fudan University School of Public Health. Written informed consent from the participants was not required to participate in this study in accordance with the national legislation and the institutional requirements.

## Author contributions

BE, PW, ES, MFJ, SE, MJ, and CD: conceptualization and writing and critical review. BE, PW, MFJ, and ES: design and analysis. All authors contributed to the article and approved the submitted version.

## Funding Statement

This study was made possible through funding provided by the EuroQol Research Foundation (project number: EQ-2016740).

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## References

## References

1. Attema A. E., Brouwer W. B. F., Claxton K. (2018). Discounting in economic evaluations. Pharmacoeconomics. 36, 745–758. 10.1007/s40273-018-0672-z

2. Chen G., Ratcliffe J. A. (2015). Review of the development and application of generic multi-attribute utility instruments for paediatric populations. PharmacoEconomics. 33, 1013–1028. 10.1007/s40273-015-0286-7

3. CotSNPCNE (n.d.) . Attainment CotSNPCNE. Available online at: https://www.gov.cn/guoqing/2021-05/13/content_5606149.htm (accessed February 16, 2023).

4. Devlin N., Roudijk B., Viney R., Stolk E. (2022). EQ-5D-Y-3L value sets, valuation methods and conceptual questions. PharmacoEconomics. 40, 123–127. 10.1007/s40273-022-01226-7

5. Jonker M. F., Attema A. E., Donkers B., Stolk E. A., Versteegh M. M. (2017). Are health state valuations from the general public biased? A test of health state reference dependency using self-assessed health and an efficient discrete choice experiment. Health Econ. 26, 1534–1547. 10.1002/hec.3445

6. Jonker M. F., Bliemer M. C. J. (2019). On the optimization of Bayesian D-efficient discrete choice experiment designs for the estimation of QALY tariffs that are corrected for nonlinear time preferences. Value Health J. Int. Soc. Pharmacoecon. Outcomes Res. 22, 1162–1169. 10.1016/j.jval.2019.05.014

7. Jonker M. F., Donkers B., de Bekker-Grob E. W., Stolk E. A. (2018a). Effect of level overlap and color coding on attribute non-attendance in discrete choice experiments. Value Health J. Int. Soc. Pharmacoecon. Outcomes Res. 21, 767–771. 10.1016/j.jval.2017.10.002

8. Jonker M. F., Donkers B., de Bekker-Grob E. W., Stolk E. A. (2018b). Advocating a paradigm shift in health-state valuations: the estimation of time-preference corrected QALY tariffs. Value Health J. Int. Soc. Pharmacoecon. Outcomes Res. 21, 993–1001. 10.1016/j.jval.2018.01.016

9. Kind P., Klose K., Gusi N., Olivares P. R., Greiner W. (2015). Can adult weights be used to value child health states? Testing the influence of perspective in valuing EQ-5D-Y. Qual. Life Res. Int. J. Qual. Life Aspects Treat. Care Rehabil. 24, 2519–2539. 10.1007/s11136-015-0971-1

10. Kreimeier S., Oppe M., Ramos-Goñi J. M., Cole A., Devlin N., Herdman M., et al. (2018). Valuation of EuroQol five-dimensional questionnaire, youth version (EQ-5D-Y) and EuroQol five-dimensional questionnaire, three-level version (EQ-5D-3L) health states: the impact of wording and perspective. Value Health. 21, 1291–1298. 10.1016/j.jval.2018.05.002

11. Lipman S. A., Reckers-Droog V. T., Karimi M., Jakubczyk M., Attema A. E. (2021). Self vs. other, child vs. adult. An experimental comparison of valuation perspectives for valuation of EQ-5D-Y-3L health states. Eur. J. Health Econ. HEPAC Health Econ. Prevent. Care. 22, 1507–1518. 10.1007/s10198-021-01377-y

12. Mott D. J., Shah K. K., Ramos-Goñi J. M., Devlin N. J., Rivero-Arias O. (2021). Valuing EQ-5D-Y-3L health states using a discrete choice experiment: do adult and adolescent preferences differ? Med. Decision Making 41, 584–596. doi:10.1177/0272989X21999607

13. Ramos-Goñi J. M., Oppe M., Stolk E., Shah K., Kreimeier S., Rivero-Arias O., et al. (2020). International valuation protocol for the EQ-5D-Y-3L. PharmacoEconomics. 38, 653–663. 10.1007/s40273-020-00909-3

14. Reckers-Droog V., Karimi M., Lipman S., Verstraete J. (2022). Why do adults value EQ-5D-Y-3L health states differently for themselves than for children and adolescents: a think-aloud study. Value Health J. Int. Soc. Pharmacoecon. Outcomes Res. 25, 1174–1184. 10.1016/j.jval.2021.12.014

15. Rowen D., Rivero-Arias O., Devlin N., Ratcliffe J. (2020). Review of valuation methods of preference-based measures of health for economic evaluation in child and adolescent populations: where are we now and where are we going? PharmacoEconomics. 38, 325–340. 10.1007/s40273-019-00873-7

16. Shah K. K., Ramos-Goñi J. M., Kreimeier S., Devlin N. J. (2020). An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values. Eur. J. Health Econ. HEPAC Health Econ. Prevent. Care. 21, 1091–1103. 10.1007/s10198-020-01205-9

17. Wille N., Badia X., Bonsel G., Burstrom K., Cavrini G., Devlin N., et al. (2010). Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual. Life Res. Int. J. Qual. Life Aspects Treat. Care Rehabil. 19, 875–886. 10.1007/s11136-010-9648-y

## Associated Data

### Data Availability Statement

The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation.

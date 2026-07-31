---
project_id: "289-RA"
work_id: "doi:10.1007/s10198-023-01569-8"
doi: "10.1007/s10198-023-01569-8"
pmid: "36814039"
pmcid: "PMC9946870"
title: "COVID-19 and EQ-5D-5L health state valuation"
journal: "The European Journal of Health Economics"
publication_date: "2023-02-23"
volume: "25"
issue: "1"
authors:
  - name: "Edward J. D. Webb"
    orcid: "http://orcid.org/0000-0001-7918-839X"
    affiliation_ids:
      - "Aff1"
  - name: "Paul Kind"
    affiliation_ids:
      - "Aff2"
  - name: "David Meads"
    affiliation_ids:
      - "Aff1"
  - name: "Adam Martin"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/024mrxd33grid.9909.90000 0004 1936 8403Academic Unit of Health Economics, Leeds Institute of Health Sciences, University of Leeds, Leeds, UK"
  - id: "Aff2"
    name: "grid.9909.90000 0004 1936 8403Institute of Epidemiology and Health, University College London, UK and Academic Unit of Health Economics, Leeds Institute of Health Sciences, University of Leeds, Leeds, UK"
keywords:
  - "COVID-19"
  - "D7"
  - "EQ-5D-5L"
  - "Health shock"
  - "I10"
  - "I30"
  - "Valuation"
  - "Visual analogue scale"
licence: "cc-by"
source_file: "input/projects/289-RA/papers/doi_10.1007_s10198-023-01569-8.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9946870/fullTextXML"
source_method: "epmc_xml"
source_sha256: "910d85f3960ff21c9a98913e94d2d952f6080dbb12a2b86628061ec9135df07c"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# COVID-19 and EQ-5D-5L health state valuation

## Abstract

### Background

We investigate whether and how general population health state values were influenced by the initial stages of the COVID-19 pandemic. Changes could have important implications, as general population values are used in health resource allocation.

### Data

In Spring 2020, participants in a UK general population survey rated 2 EQ-5D-5L states, 11111 and 55555, as well as dead, using a visual analogue scale (VAS) from 100 = best imaginable health to 0 = worst imaginable health. Participants answered questions about their pandemic experiences, including COVID-19’s effect on their health and quality of life, and their subjective risk/worry about infection.

### Analysis

VAS ratings for 55555 were transformed to the full health = 1, dead = 0 scale. Tobit models were used to analyse VAS responses, as well as multinomial propensity score matching (MNPS) to create samples balanced according to participant characteristics.

### Results

Of 3021 respondents, 2599 were used for analysis. There were statistically significant, but complex associations between experiences of COVID-19 and VAS ratings. For example, in the MNPS analysis, greater subjective risk of infection implied higher VAS ratings for dead, yet worry about infection implied lower ratings. In the Tobit analysis, people whose health was affected by COVID-19 rated 55555 higher, whether the effect on health was positive or negative.

### Conclusion

The results complement previous findings that the onset of the COVID-19 pandemic may have impacted EQ-5D-5L health state valuation, and different aspects of the pandemic had different effects.

## Introduction

The COVID-19 pandemic has had an enormous effect on health and society worldwide. Over six million people have died as of July 2022 \[1\]. COVID-19 can lead to a variety of sequelae \[2, 3\], including neurological \[4\] and cardiac \[5\] problems, fatigue \[6\] and mental health effects \[7\]. The pandemic has had a large economic impact \[8\] as well as straining healthcare resources \[9, 10\], diverting care from other areas, worsening outcomes \[11, 12\], and creating a backlog of patients awaiting treatment \[13–15\].

It is plausible that disruption from the pandemic has led people to reassess their preferences, attitudes and priorities, including for health and healthcare; for example, what trade-offs they would be willing to make between health and quality of life. The possibility implies changes in how people would value health states and instruments measuring health-related quality of life. In particular, it is important to examine the EQ-5D instrument \[16\], as in many countries, including the UK \[17\], national EQ-5D value sets are used to allocate healthcare resources according to the public’s preferences. If people’s values for EQ-5D health states have changed due to the COVID-19 pandemic, the implication is that healthcare resources are not being allocated efficiently, a problem which is particularly acute when such resources are scarcer than ever.

If values for EQ-5D health states have changed due to COVID-19, there are also implications for recent and ongoing valuation exercises. Value sets created just before the pandemic may no longer be valid. Alternatively, if the shock to values is transient, value sets created in the present could have a short shelf life. In general, the “life-cycle” of value sets is a neglected area, and there have been calls for further research into it \[18\]. Investigating whether the COVID-19 health crisis affected people’s health preferences gives insight into whether it may have brought to an end the useful life of existing national EQ-5D value sets.

This paper examines specifically whether and how the onset of the COVID-19 pandemic affected how individuals from the UK valued EQ-5D-5L, the five-level version of the instrument \[19\], which measures whether people have problems on five dimensions: mobility, self-care, usual activities, pain/discomfort and anxiety/depression. On each dimension, individuals indicate whether they have no, mild, moderate, severe or extreme problems. Our work is a follow-up to Webb et al. \[20\], who compared survey data collected in 2018 and in 2020, shortly after the onset of the pandemic in the UK. They examined differences between the two time points in how individuals rated two EQ-5D-5L health states, 11111 and 55555, and dead using a visual analogue scale (VAS), as well as a derived value for 55555 on the full health = 1, dead = 0 scale used to calculate quality adjusted life-years (QALYs). In 2020 compared to 2018, ratings for 11111 and dead were lower, whereas ratings for 55555 were higher, both for the original VAS and the 1–0 scale. There were also differential changes according to subgroups such as gender, ethnicity and age.

Webb et al. \[20\] propose that the COVID-19 pandemic is the most likely cause of differences between 2018 and 2020. This paper seeks to complement and reinforce the previous findings by examining the survey data collected in 2020 more closely and exploiting its richness in terms of the number of questions asked about people’s COVID-19 experiences. In particular, we use responses to two survey questions about people’s perceived risk/worry about infection, and four questions about how people’s lives were affected during the pandemic, to examine whether people whose lives were more affected change their values more, which would lend credence to the supposition that the pandemic is the driver of value change.

This study uses VAS to measure people’s preferences for heath states, whereas EQ-5D value sets are usually created using time trade-off (TTO), possibly augmented with a discrete choice experiment (DCE) \[21\]. We comment on the relevance of our result for such value sets in Sect. “Strengths and weaknesses”.

## Methods

### Data collection

Primary data were collected using an online survey. Recruitment took place in two waves: 16th–23rd April 2020 and 4th–15th May 2020. Some individuals responded to both waves, and some only to one. Participants were asked questions about themselves and their experience of COVID-19. They rated two EQ-5D-5L states, 11111 and 55555, as well as dead, using the VAS task illustrated in Fig. <a href="#Fig1" data-ref-type="fig">1</a>. The scale ran from 100 = the best health you can imagine to 0 = the worst health you can imagine.

<figure id="Fig1">
<p><img src="10198_2023_1569_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Example of visual analogue scale task</figcaption>
</figure>

Participants were asked whether they had received a positive diagnosis or test for COVID-19. Those answering no were asked what they considered their chances of becoming infected with COVID-19 were, as well as whether they worried about being infected with COVID-19, both on Likert scales from 1 to 5. In wave 2, only additional questions were asked whether COVID-19 had affected their health and/or quality of life, with possible answers of no, yes-negatively and yes-positively. Participants were asked how often they left their homes to shop, and to get fresh air and exercise, and whether they considered themselves key workers. A full list of the COVID-19-related questions is given in appendix A. The survey did not allow participants to proceed without answering all questions; therefore, there is no missing data in submitted responses. (Although note as specified above, some questions were not asked in wave 1.)

Secondary data on COVID-19 prevalence and deaths on the final day of each recruitment wave (23/4/20 and 15/5/20) at Nomenclature of Territorial Units for Statistics (NUTS) level 1 were drawn from the UK coronavirus dashboard[^1] and linked to each individual. The specific measures were cumulative COVID-19 cases by date of publication and cumulative deaths within 60 days of a positive test by date of death.[^2]

### Analysis

Differences between wave 1 and 2 characteristics were assessed using Mann–Whitney *U* tests.

VAS ratings for 55555 on the 100–0 scale were transformed to the full health = 1, dead = 0 scale used for calculating quality-adjusted life-years (QALYs) \[22\]. This was done using the formula
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
                \begin{document}$${\text{VAS}}_{{{55555}}}^{{{\text{rescaled}}}} = \frac{{{\text{VAS}}_{{{55555}}} - {\text{VAS}}_{{{\text{dead}}}} }}{{{\text{VAS}}_{{{11111}}} - {\text{VAS}}_{{{\text{dead}}}} }}$$\end{document}
```

where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${VAS}_{i}$$\end{document}`$ is the rating of health state $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$i$$\end{document}`$ on the 100–0 scale and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{VAS}}_{{{55555}}}^{{{\text{rescaled}}}}$$\end{document}`$ is the value of 55555 on the 1–0 scale. The rescaled values of 55555 are dependent on ratings for 11111 and dead. Thus, it is possible for individuals’ rescaled 55555 values to increase in response to COVID-19 while their raw VAS ratings decrease, and vice versa, depending on how their ratings for 11111 and dead also change. The rescaling requires VAS ratings to be logical, i.e. $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{VAS}}_{{{11111}}}$$\end{document}`$ $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$>$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{VAS}}_{{{11111}}} {\text{ > VAS}}_{{{55555}}}$$\end{document}`$, and illogical responses were excluded from the analysis.

The VAS task can produce a tail of very low rescaled values for 55555, for example below  – 100, which can have a large influence on the mean \[22\]. In line with the previous study, rescaled values for 55555 were censored at -1.

Few individuals (*N* = 17) reported a formal COVID-19 diagnosis or positive test. Due to the low numbers and the fact that they were not shown key questions about their subjective risk of/degree of worry about COVID-19 infection, they were also excluded from the analysis.

Whether subjective risk of COVID-19 infection and worry about COVID-19 infection differed between the waves was assessed using Mann–Whitney *U* tests.

VAS ratings were analysed using two complementary approaches. Tobit regressions were suitable for analysing the continuous variables of cumulative COVID-19 cases/deaths, as well as allowing for interactions between variables. Multinomial propensity score matching (MNPS) was better able to isolate the causal effects of a given dependent variable, but could not accommodate continuous dependent variables or interaction terms. MNPS also required discarding some information by compressing Likert scale responses from a five- to a three-point scale.

Using pooled wave 1 and wave 2 data, three Tobit regressions were run with VAS ratings of 11111, dead and 55555 as dependent variables and upper limits of 100 and lower limits of 0. A Tobit regression was run with rescaled values of 55555 as the dependent variable and an upper limit of 1 and lower limit of -1 was run. Individuals’ subjective risk of COVID-19 infection, worry about COVID-19 infection and the interaction of the two were included as independent variables, along with cumulative cases and deaths by region and the following controls: age, age<sup>2</sup>, female, white, left school after minimum age, has degree or equivalent qualification, live alone, retired, employed, whether self-report being in levels 2–5 on each EQ-5D-5L dimension, number of long-term health conditions, self-rated health on a Likert scale from 1 to 5.

Using only wave 2 data, similar sets of Tobit regressions were run which added whether COVID-19 had affected participants’ health and/or quality of life. The regressions also included a variable indicating if someone considered themselves a key worker. Two further sets of Tobit regressions were then run which included first how often individuals left the house to shop, and second how often individuals left the house for fresh air and exercise.

There is potential for co-linearity between many variables of interest as well as controls. For example, correlation was expected between subjective risk of infection and worry about COVID-19. Older individuals, or those with long-term health conditions, may also be more concerned about COVID-19, as well as valuing health differently from younger, healthier individuals. MNPS was used to isolate the causal effect of: subjective risk of COVID-19 infection, worry about COVID-19 infection, whether COVID-19 affected health/quality of life, shopping frequency and exercise frequency. The five level responses for subjective risk and worry were collapsed to three groups: 1–2, 3 and 4–5. Responses for frequency of leaving the house for shopping/exercise were collapsed to: less than weekly, weekly and more than weekly. For each variable of interest, samples were created which were balanced on the same control variables used in the Tobit regressions, as well as on the other variables of interest using the twang package for R \[23\]. Twang estimates multinomial propensity score weights using gradient boosted models, an iterative machine learning technique which can accommodate non-linearity and interactions among the variables that the researcher seeks to achieve balance on. The estimand, i.e. the causal effect of interest, was the average treatment effect (ATE). The gradient boosting algorithm was run for 5,000 iterations, with the multinomial propensity score weights used for analysis taken from the iteration which minimised differences between treatment groups. Differences were assessed using the mean standardised effect size across all control variables. ATEs were then found by including the propensity score weights in weighted linear regression models.

To test the results’ robustness to the rescaled 55555 threshold of  – 1, the Tobit models were re-run with thresholds of  – 2 and  – 1.5. In addition, the models were re-run using a number of other approaches, which rather than censoring, removed participants with excessively low values for 55555 from the analysis data. Full details are given in appendix C, but in summary the approaches were: excluding participants with low rescaled values of 55555; excluding participants who had a large influence on the mean rescaled value of 55555; excluding participants with a high rate of change of rescaled 55555 values with respect to raw 55555 values.

All analysis was carried out using R.

## Results

There were 3021 total responses to the survey, comprising 809 people who responded in wave 1 only, 826 who responded in wave 2 only, and 693 people who participated in both. There were 422 responses (14.0%) excluded for illogical VAS ratings. Only 11 respondents (0.4%) said they had received a positive COVID-19 diagnosis and 6 (0.2%) reported ever having a positive test result, all submitted illogical VAS ratings and were excluded on that basis.

Table <a href="#Tab1" data-ref-type="table">1</a> summarises the characteristics of both the full (*N* = 3021) and analysis (*N* = 2599) samples and Table <a href="#Tab2" data-ref-type="table">2</a> summarises their responses to COVID-19-related questions. Both samples were similar, although the analysis sample was slightly older (48.3 years vs. 47.7 years) and were less likely to have a long-term health condition (30.2% vs. 32.7%). There were relatively few older people in the analysis sample, with only 4.1% aged over 75, compared to 8.6% of the UK population \[24\]. Around 20% of wave 2 participants said that COVID-19 had affected their health negatively, while around 5% said its effect was positive. A larger proportion said COVID-19 had affected their quality of life, with almost half reporting a negative impact and 8.3% reporting a positive impact. The modal frequency of leaving the house to shop was weekly, whereas the modal frequency of leaving the house for exercise and fresh air was daily. Almost no one shopped more than daily (6; 0.5%) and few exercised more than daily (67; 5.1%) (Table <a href="#Tab2" data-ref-type="table">2</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Participants’ characteristics

</div>

|  | Full sample |  | Analysis sample |  |  |  |
|----|----|----|----|----|----|----|
|  |  |  | Both waves |  | Wave 2 |  |
|  | *N* | (%) | *N* | (%) | *N* | (%) |
| *Age* |  |  |  |  |  |  |
| Mean (sd) | 47.7 | (16.7) | 48.3 | (16.7) | 49.7 | (16.1) |
| 18–24 | 307 | (10.2) | 243 | (9.30) | 87 | (6.6) |
| 25–34 | 480 | (15.90 | 398 | (15.3) | 196 | (14.9) |
| 35–44 | 475 | (15.70 | 413 | (15.9) | 200 | (15.2) |
| 45–54 | 652 | (21.6) | 547 | \(21\) | 293 | (22.2) |
| 55–64 | 418 | (13.8) | 367 | (14.1) | 212 | (16.1) |
| 65–74 | 577 | (19.1) | 531 | (20.4) | 276 | (20.9) |
| 75 +  | 112 | (3.7) | 100 | (3.8) | 54 | (4.1) |
| *Female* |  |  |  |  |  |  |
|  | 1489 | (49.3) | 1285 | (49.4) | 648 | (49.2) |
| *Ethnicity* |  |  |  |  |  |  |
| White | 2694 | (89.2) | 2337 | (89.9) | 1190 | (90.3) |
| Asian | 130 | (4.3) | 106 | (4.10 | 56 | (4.2) |
| Mixed | 51 | (1.7) | 39 | (1.5) | 19 | (1.4) |
| Black | 88 | (2.9) | 74 | (2.8) | 33 | (2.5) |
| Other | 58 | (1.9) | 43 | (1.7) | 20 | (1.5) |
| *Occupation* |  |  |  |  |  |  |
| Employed | 1789 | (59.2) | 1554 | (59.8) | 799 | (60.6) |
| Key worker\* | 519 | (34.2) | – | **–** | 477 | (36.2) |
| Retired | 653 | (21.6) | 592 | (22.8) | 307 | (23.3) |
| Housework | 204 | (6.80) | 167 | (6.4) | 82 | (6.2) |
| Student | 108 | (3.6) | 93 | (3.60 | 34 | (2.6) |
| Unemployed | 123 | (4.1) | 95 | (3.70) | 49 | (3.7) |
| Prefer not to say | 58 | (1.9) | 40 | (1.50) | 15 | (1.1) |
| Other | 86 | (2.80 | 58 | (2.20) | 32 | (2.4) |
| *Education* |  |  |  |  |  |  |
| Left school after minimum age | 2330 | (77.1) | 2025 | (77.9) | 1026 | (77.8) |
| Degree/ equivalent | 1582 | (52.4) | 1368 | (52.6) | 703 | (53.3) |
| Report being in 11111 | 1037 | (34.3) | 936 | \(36\) | 481 | (36.5) |
| EQ-VAS | 73 | (22.5) | 74.7 | (21.1) | 74.8 | (21.1) |
| Long-term condition | 987 | (32.7) | 786 | (30.2) | 402 | (30.5) |
| *Number of comorbidities* |  |  |  |  |  |  |
| Mean (sd) | 0.7 | (1.20) | 0.6 | (1.20) | 0.6 | (1.1) |
| *Description of own health* |  |  |  |  |  |  |
| Excellent | 357 | (11.8) | 306 | (11.8) | 145 | \(11\) |
| Very good | 1028 | \(340\) | 929 | (35.7) | 478 | (36.3) |
| Good | 990 | (32.8) | 872 | (33.6) | 436 | (33.1) |
| Fair | 507 | (16.8) | 398 | (15.3) | 210 | (15.9) |
| Poor | 139 | (4.6) | 94 | (3.6) | 49 | (3.7) |
| *N* | 3021 |  | 2599 |  | 1318 |  |

Note. \*Only asked in wave 2, *sd * standard deviation

</div>

<div id="Tab2" class="table-wrap">

<div class="caption">

Responses to COVID-19-related questions

</div>

|  | Full sample |  | Analysis sample |  |  |  |
|----|----|----|----|----|----|----|
|  |  |  | Both waves |  | Wave 2 |  |
|  | *N* | (%) | *N* | (%) | *N* | (%) |
| *COVID-19 diagnosis* | 11 | (0.4) | 0 | – | 0 | – |
| COVID-19 positive test | 6 | (0.2) | 0 | – | 0 | – |
| *Worry about catching COVID-19 (1 = never thought about it, 5 = Worried all the time)* |  |  |  |  |  |  |
| Mean (sd) | 2.2 | (1.0) | 2.2 | (1.0) | 2.1 | (1.0) |
| *Subjective risk of COVID-19 infection (1 = highly unlikely, 5 = highly likely* |  |  |  |  |  |  |
| Mean (sd) | 2 | (0.9) | 2 | (0.9) | 2 | (0.9) |
| *COVID-19 affected health?\** |  |  |  |  |  |  |
| Yes, negatively | 328 | (24.9) | – | – | 260 | (19.7) |
| No | 1106 | (72.8) | – | – | 991 | (75.2) |
| Yes, positively | 85 | (6.4) | \- | \- | 67 | (5.1) |
| *COVID-19 affected quality of life?\** |  |  |  |  |  |  |
| Yes, negatively | 729 | (48.0) | – | – | 641 | (48.6) |
| No | 650 | (49.3) | – | – | 567 | (43.0) |
| Yes, positively | 140 | (9.2) | – | – | 110 | (8.3) |
| *Frequency leave house to shop\** |  |  |  |  |  |  |
| Never | 236 | (17.9) | – | – | 198 | (15.0) |
| Less than weekly | 275 | (18.1) | – | – | 245 | (18.6) |
| Weekly | 650 | (49.3) | – | – | 573 | (43.5) |
| 2–6 times per week | 285 | (18.8) | – | – | 246 | (18.7) |
| Daily | 62 | (4.7) | – | – | 50 | (3.8) |
| More than daily | 11 | (0.7) | – | – | 6 | (0.5) |
| *Frequency leave house for exercise\** |  |  |  |  |  |  |
| Never | 175 | (13.3) | – | – | 146 | (11.1) |
| Less than weekly | 165 | (10.9) | – | – | 138 | (10.5) |
| Weekly | 191 | (14.5) | – | – | 152 | (11.5) |
| 2–6 times per week | 440 | (29.0) | – | – | 393 | (29.8) |
| Daily | 469 | (35.6) | – | – | 422 | (32.0) |
| More than daily | 79 | (5.2) | – | – | 67 | (5.1) |
| *N* | 3021 |  | 2599 |  | 1318 |  |

Note. \*Only asked in wave 2, *sd* standard deviation

</div>

Table <a href="#Tab5" data-ref-type="table">5</a> shows the results of comparing the demographics of waves 1 and 2. The only significant difference observed was in age, with wave 2 participants being slightly older than wave 1 at 45.7 compared to 47. There were no significant differences between survey waves in subjective risk of COVID-19 infection (Mann–Whitney *U* *p* value 0.189) or worry about COVID-19 infection (Mann–Whitney *U* *p* value 0.097).

Figure <a href="#Fig2" data-ref-type="fig">2</a> shows histograms of the analysis sample’s VAS responses. A large proportion of respondents rated full health as 100 and dead as 0. Most rescaled 55555 values were positive but low, although many also rated it below 0 (i.e. worse than dead).

<figure id="Fig2">
<p><img src="10198_2023_1569_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Histograms of VAS responses</figcaption>
</figure>

Table <a href="#Tab3" data-ref-type="table">3</a> summarises the Tobit model results, with full results including control variables given in Appendix B. With the whole analysis sample, there was no significant main effect of worry about COVID-19 infection on any VAS responses, but there was a significantly positive main effect of subjective risk of COVID-19 infection and a significantly negative interaction with worry for dead and rescaled 55555. There were no significant effects of regional-level COVID-19 cases or deaths. With wave 2 respondents, there were no significant results for COVID-19’s effect on quality of life, but respondents reporting both negative and positive impact of COVID-19 on health rated 55555 significantly higher. There was a similar result for dead, although only the coefficient for positive impact of COVID-19 on health was significant. Frequency of leaving the house for shopping had no significant coefficients. Those who left the house to exercise less than weekly or weekly rated 11111 significantly lower and dead significantly higher compared to never leaving the house for exercise. Those who exercised weekly also rated 55555 significantly higher. Examining all exercise-related coefficients seems to indicate that the effects of exercise frequency on VAS ratings were not linear. For all sets of Tobit regressions using wave 2 data, the effects of subjective risk and worry about COVID-19 infection were similar to results using both waves, although some coefficients no longer achieved statistical significance. COVID-19 cases and deaths had no significant effects.

<div id="Tab3" class="table-wrap">

<div class="caption">

Results from Tobit regressions of visual analogue scale ratings

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Regression set</th>
<th style="text-align: left;">Dependent variable</th>
<th style="text-align: left;">11111</th>
<th style="text-align: left;">s.e</th>
<th style="text-align: left;">Dead</th>
<th style="text-align: left;">s.e</th>
<th style="text-align: left;">55555</th>
<th style="text-align: left;">s.e</th>
<th style="text-align: left;">55555 rescaled</th>
<th style="text-align: left;">s.e</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Both waves <em> N</em> = 2599</td>
<td style="text-align: left;">Cumulative COVID-19 cases</td>
<td style="text-align: left;"> – 0.013</td>
<td style="text-align: left;">0.0161</td>
<td style="text-align: left;">0.0399</td>
<td style="text-align: left;">0.0417</td>
<td style="text-align: left;">5.85 × 10–3</td>
<td style="text-align: left;">0.0203</td>
<td style="text-align: left;"> – 1.25 × 10–4</td>
<td style="text-align: left;">3.72 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cumulative COVID-19 deaths</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.0712</td>
<td style="text-align: left;"> – 0.248</td>
<td style="text-align: left;">0.184</td>
<td style="text-align: left;"> – 0.0431</td>
<td style="text-align: left;">0.0897</td>
<td style="text-align: left;">9.33 × 10–4</td>
<td style="text-align: left;">1.65 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry about being infected with COVID-19</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> (1 = never thought about it, 5 = all the time)</td>
<td style="text-align: left;">0.0331</td>
<td style="text-align: left;">0.823</td>
<td style="text-align: left;">0.101</td>
<td style="text-align: left;">2.12</td>
<td style="text-align: left;"> – 0.827</td>
<td style="text-align: left;">1.03</td>
<td style="text-align: left;"> – 0.0158</td>
<td style="text-align: left;">0.0189</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Subjective risk of COVID-19 infection</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> (1 = highly unlikely, 5 = highly likely)</td>
<td style="text-align: left;"> – 0.847</td>
<td style="text-align: left;">0.862</td>
<td style="text-align: left;">7.71*</td>
<td style="text-align: left;">2.16</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">1.07</td>
<td style="text-align: left;"> – 0.0578*</td>
<td style="text-align: left;">0.0198</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry × subjective risk</td>
<td style="text-align: left;">0.206</td>
<td style="text-align: left;">0.351</td>
<td style="text-align: left;"> – 2.12*</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;"> – 0.0427</td>
<td style="text-align: left;">0.438</td>
<td style="text-align: left;">0.0193*</td>
<td style="text-align: left;">8.08 × 10–3</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Wave 2—COVID-19 affected health/quality of life <em> N</em> = 1294</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cumulative COVID-19 cases</td>
<td style="text-align: left;"> – 8.01 × 10–3</td>
<td style="text-align: left;">0.0198</td>
<td style="text-align: left;">0.0318</td>
<td style="text-align: left;">0.0498</td>
<td style="text-align: left;"> – 4.29 × 10–4</td>
<td style="text-align: left;">0.0251</td>
<td style="text-align: left;"> – 3.43 × 10–4</td>
<td style="text-align: left;"> – 3.77 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Cumulative COVID-19 deaths</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.0946</td>
<td style="text-align: left;"> – 0.0901</td>
<td style="text-align: left;">0.239</td>
<td style="text-align: left;"> – 0.0342</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">5.88 × 10–4</td>
<td style="text-align: left;">7 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry about being infected with COVID-19</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> (1 = never thought about it, 5 = all the time)</td>
<td style="text-align: left;">1.37</td>
<td style="text-align: left;">1.12</td>
<td style="text-align: left;"> – 2.19</td>
<td style="text-align: left;">2.81</td>
<td style="text-align: left;"> – 1.57</td>
<td style="text-align: left;">1.42</td>
<td style="text-align: left;"> – 0.0198</td>
<td style="text-align: left;">0.0251</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Subjective risk of COVID-19 infection</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> (1 = highly unlikely, 5 = highly likely)</td>
<td style="text-align: left;">0.0996</td>
<td style="text-align: left;">1.15</td>
<td style="text-align: left;">3.97</td>
<td style="text-align: left;">2.77</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">1.45</td>
<td style="text-align: left;"> – 0.0543*</td>
<td style="text-align: left;">0.0258</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry × subjective risk</td>
<td style="text-align: left;"> – 0.223</td>
<td style="text-align: left;">0.473</td>
<td style="text-align: left;"> – 1.06</td>
<td style="text-align: left;">1.17</td>
<td style="text-align: left;">0.0805</td>
<td style="text-align: left;">0.596</td>
<td style="text-align: left;">0.0167</td>
<td style="text-align: left;">0.0106</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">COVID-19 affected health (baseline no)</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> Negatively</td>
<td style="text-align: left;"> – 0.154</td>
<td style="text-align: left;">1.5</td>
<td style="text-align: left;">4.67</td>
<td style="text-align: left;">3.71</td>
<td style="text-align: left;">4.74*</td>
<td style="text-align: left;">1.89</td>
<td style="text-align: left;">0.0168</td>
<td style="text-align: left;">0.0337</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Positively</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: left;">2.55</td>
<td style="text-align: left;">14.8*</td>
<td style="text-align: left;">5.84</td>
<td style="text-align: left;">6.18*</td>
<td style="text-align: left;"> – </td>
<td style="text-align: left;"> – </td>
<td style="text-align: left;">0.0566</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">COVID-19 affected quality of life (baseline no)</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> Negatively</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">1.15</td>
<td style="text-align: left;"> – 2.96</td>
<td style="text-align: left;">2.94</td>
<td style="text-align: left;"> – 0.993</td>
<td style="text-align: left;">1.46</td>
<td style="text-align: left;"> – 9.71 × 10–3</td>
<td style="text-align: left;">0.0258</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Positively</td>
<td style="text-align: left;"> – 3.54</td>
<td style="text-align: left;">2.09</td>
<td style="text-align: left;">8.5</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">2.64</td>
<td style="text-align: left;"> – 0.0763</td>
<td style="text-align: left;">0.0471</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Wave 2—shopping frequency <em> N</em> = 1294</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">How often go shopping (baseline never)</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> &lt; weekly</td>
<td style="text-align: left;"> – 1.56</td>
<td style="text-align: left;">1.67</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">4.22</td>
<td style="text-align: left;"> – 1.22</td>
<td style="text-align: left;">2.15</td>
<td style="text-align: left;"> – 0.0111</td>
<td style="text-align: left;">0.0368</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Weekly</td>
<td style="text-align: left;"> – 0.882</td>
<td style="text-align: left;">1.47</td>
<td style="text-align: left;"> – 2.92</td>
<td style="text-align: left;">3.76</td>
<td style="text-align: left;">0.0746</td>
<td style="text-align: left;">1.89</td>
<td style="text-align: left;">3.53 × 10–3</td>
<td style="text-align: left;">0.0324</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2–6 times/week</td>
<td style="text-align: left;"> – 1.9</td>
<td style="text-align: left;">1.67</td>
<td style="text-align: left;">6.9</td>
<td style="text-align: left;">4.2</td>
<td style="text-align: left;"> – 0.227</td>
<td style="text-align: left;">2.16</td>
<td style="text-align: left;"> – 0.0415</td>
<td style="text-align: left;">0.0369</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Daily</td>
<td style="text-align: left;"> – 5.04</td>
<td style="text-align: left;">2.68</td>
<td style="text-align: left;">10.4</td>
<td style="text-align: left;">6.58</td>
<td style="text-align: left;">5.03</td>
<td style="text-align: left;">3.49</td>
<td style="text-align: left;">0.0116</td>
<td style="text-align: left;">0.0604</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">  &gt; daily</td>
<td style="text-align: left;"> – 0.844</td>
<td style="text-align: left;">7.05</td>
<td style="text-align: left;">5.83</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">8.89</td>
<td style="text-align: left;">0.201</td>
<td style="text-align: left;">0.157</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Wave 2—exercise frequency <em> N</em> = 1294</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">How often exercise (baseline never)</td>
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
<td style="text-align: left;"></td>
<td style="text-align: left;"> &lt; weekly</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;">2.02</td>
<td style="text-align: left;">12.2*</td>
<td style="text-align: left;">5.04</td>
<td style="text-align: left;">3.89</td>
<td style="text-align: left;">2.61</td>
<td style="text-align: left;"> – 0.0155</td>
<td style="text-align: left;">0.0449</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Weekly</td>
<td style="text-align: left;"> – 4.65*</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">14.1*</td>
<td style="text-align: left;">4.96</td>
<td style="text-align: left;">7.22*</td>
<td style="text-align: left;">2.56</td>
<td style="text-align: left;"> – 0.0251</td>
<td style="text-align: left;">0.0442</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 2–6 times/week</td>
<td style="text-align: left;"> – 1.68</td>
<td style="text-align: left;">1.69</td>
<td style="text-align: left;">1.68</td>
<td style="text-align: left;">4.37</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.18</td>
<td style="text-align: left;">0.0255</td>
<td style="text-align: left;">0.0374</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> Daily</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;">1.69</td>
<td style="text-align: left;">5.28</td>
<td style="text-align: left;">4.36</td>
<td style="text-align: left;">2.78</td>
<td style="text-align: left;">2.19</td>
<td style="text-align: left;"> – 5.47 × 10–3</td>
<td style="text-align: left;">0.0373</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"> &gt; daily</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">6.67</td>
<td style="text-align: left;">6.5</td>
<td style="text-align: left;">0.531</td>
<td style="text-align: left;">3.31</td>
<td style="text-align: left;"> – 0.0131</td>
<td style="text-align: left;">0.0563</td>
</tr>
</tbody>
</table>

Note. *s.e.* standard error, \* significant at 5% level; full results including controls in Appendix B

</div>

Table <a href="#Tab4" data-ref-type="table">4</a> shows how balanced responses were across various variables of interest, both with and without propensity score weights. It can be seen in all cases that MNPS improved balance, although the results for COVID-19’s effect on health is notably worse compared to other variables of interest (1.09, compared to the next worst being 0.268). Table <a href="#Tab4" data-ref-type="table">4</a> also presents the results of Tobit regression models following MNPS. For dead, the coefficients for subjective risk of and worry about COVID-19 infection had opposite signs, in line with the negative interaction term seen in the Tobit regression models. Subjective risk had a significantly positive effect on dead and 55555 ratings, whereas worry had a significantly negative impact on dead and a positive effect on rescaled 55555. People who reported COVID-19 had affected their health, either positively or negatively, rated dead significantly higher. A similar result was seen for 55555, although only the coefficient for a negative effect was significant. The only significant coefficient for COVID-19’s effect on quality of life was that those reporting a positive impact rated 11111 lower. There were no significant effects for either shopping or exercise frequency.

<div id="Tab4" class="table-wrap">

<div class="caption">

Average treatment effects of COVID-19-related variables on visual analogue scale ratings using matched data

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Mean standardised effect size</th>
<th rowspan="2" style="text-align: left;">Effective sample size</th>
<th rowspan="2" style="text-align: left;">11111</th>
<th rowspan="2" style="text-align: left;">s.e</th>
<th rowspan="2" style="text-align: left;">Dead</th>
<th rowspan="2" style="text-align: left;">s.e</th>
<th rowspan="2" style="text-align: left;">55555</th>
<th rowspan="2" style="text-align: left;">s.e</th>
<th rowspan="2" style="text-align: left;">55555 rescaled</th>
<th rowspan="2" style="text-align: left;">s.e</th>
</tr>
<tr>
<th style="text-align: left;">Pre-matching</th>
<th style="text-align: left;">Post-matching</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="12" style="text-align: left;"><em>Subjective risk of COVID-19 infection</em></td>
</tr>
<tr>
<td style="text-align: left;">1–2</td>
<td>0.87</td>
<td>0.161</td>
<td style="text-align: left;">2200</td>
<td style="text-align: left;"> – </td>
<td> – </td>
<td style="text-align: left;"> – </td>
<td> – </td>
<td style="text-align: left;"> – </td>
<td style="text-align: left;"> – </td>
<td style="text-align: left;"> – </td>
<td><strong><em> – </em></strong></td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> – 0.681</td>
<td>0.748</td>
<td style="text-align: left;">1.75</td>
<td>0.984</td>
<td style="text-align: left;">1.99 *</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"> – 8.6 × 10–3</td>
<td>0.0194</td>
</tr>
<tr>
<td style="text-align: left;">4–5</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> – 1.43</td>
<td>0.909</td>
<td style="text-align: left;">4.53 *</td>
<td>1.4</td>
<td style="text-align: left;">4.47 *</td>
<td style="text-align: left;">1.32</td>
<td style="text-align: left;">-5.8 × 10–3</td>
<td>0.0253</td>
</tr>
<tr>
<td colspan="12" style="text-align: left;"><em>Worry about being infected with COVID-19</em></td>
</tr>
<tr>
<td style="text-align: left;">1–2</td>
<td>0.817</td>
<td>0.168</td>
<td style="text-align: left;">2094</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>–</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1.38</td>
<td>0.784</td>
<td style="text-align: left;"> – 4.5 *</td>
<td>1.39</td>
<td style="text-align: left;">0.126</td>
<td style="text-align: left;">1.08</td>
<td style="text-align: left;">0.0727 *</td>
<td>0.0243</td>
</tr>
<tr>
<td style="text-align: left;">4–5</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.894</td>
<td>0.878</td>
<td style="text-align: left;"> – 5.6 *</td>
<td>1.44</td>
<td style="text-align: left;"> – 0.723</td>
<td style="text-align: left;">1.23</td>
<td style="text-align: left;">0.0766 *</td>
<td>0.0266</td>
</tr>
<tr>
<td colspan="12" style="text-align: left;"><em>COVID-19 affected health</em></td>
</tr>
<tr>
<td style="text-align: left;">Yes-negatively</td>
<td>1.964</td>
<td>1.088</td>
<td style="text-align: left;">1043</td>
<td style="text-align: left;"> – 1.4</td>
<td>1.16</td>
<td style="text-align: left;">2.97 *</td>
<td>1.48</td>
<td style="text-align: left;">6.61 *</td>
<td style="text-align: left;">1.59</td>
<td style="text-align: left;">0.0316</td>
<td>0.0329</td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>–</td>
</tr>
<tr>
<td style="text-align: left;">Yes-positively</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.94</td>
<td>1.54</td>
<td style="text-align: left;">11 *</td>
<td>4.55</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">3.82</td>
<td style="text-align: left;"> – 0.141</td>
<td>0.103</td>
</tr>
<tr>
<td colspan="12" style="text-align: left;"><em>COVID-19 affected quality of life</em></td>
</tr>
<tr>
<td style="text-align: left;">Yes-negatively</td>
<td>1.575</td>
<td>0.268</td>
<td style="text-align: left;">1050</td>
<td style="text-align: left;">4.37 × 10–3</td>
<td>0.769</td>
<td style="text-align: left;"> – 0.345</td>
<td>1.08</td>
<td style="text-align: left;"> – 0.407</td>
<td style="text-align: left;">1.11</td>
<td style="text-align: left;"> – 8.42 × 10–3</td>
<td>0.0226</td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>–</td>
</tr>
<tr>
<td style="text-align: left;">Yes-positively</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> – 4.09 *</td>
<td>1.91</td>
<td style="text-align: left;">3.23</td>
<td>2.09</td>
<td style="text-align: left;">2.36</td>
<td style="text-align: left;">2.07</td>
<td style="text-align: left;">0.0122</td>
<td>0.0396</td>
</tr>
<tr>
<td colspan="12" style="text-align: left;"><em>How often go shopping</em></td>
</tr>
<tr>
<td style="text-align: left;"> &lt; Weekly</td>
<td>0.812</td>
<td>0.23</td>
<td style="text-align: left;">1132</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>–</td>
</tr>
<tr>
<td style="text-align: left;">Weekly</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.921</td>
<td>0.862</td>
<td style="text-align: left;"> – 1.16</td>
<td>1.31</td>
<td style="text-align: left;">0.54</td>
<td style="text-align: left;">1.2</td>
<td style="text-align: left;">0.0119</td>
<td>0.0254</td>
</tr>
<tr>
<td style="text-align: left;"> &gt; Weekly</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> – 1.37</td>
<td>1.17</td>
<td style="text-align: left;">2.48</td>
<td>1.69</td>
<td style="text-align: left;">2.35</td>
<td style="text-align: left;">1.6</td>
<td style="text-align: left;">1.64 × 10–4</td>
<td>0.0335</td>
</tr>
<tr>
<td colspan="12" style="text-align: left;"><em>How often exercise</em></td>
</tr>
<tr>
<td style="text-align: left;"> &lt; Weekly</td>
<td>0.672</td>
<td>0.184</td>
<td style="text-align: left;">1096</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td>–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>–</td>
</tr>
<tr>
<td style="text-align: left;">Weekly</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> – 0.876</td>
<td>1.36</td>
<td style="text-align: left;">3.35</td>
<td>2.35</td>
<td style="text-align: left;">2.24</td>
<td style="text-align: left;">2.36</td>
<td style="text-align: left;"> – 0.0142</td>
<td>0.0464</td>
</tr>
<tr>
<td style="text-align: left;"> &gt; Weekly</td>
<td></td>
<td></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.439</td>
<td>0.913</td>
<td style="text-align: left;"> – 1.86</td>
<td>1.65</td>
<td style="text-align: left;"> – 1.13</td>
<td style="text-align: left;">1.85</td>
<td style="text-align: left;">0.0161</td>
<td>0.0321</td>
</tr>
</tbody>
</table>

Note. *s.e.*  standard error, \*significant at 5% level

</div>

The results of robustness tests of different ways of handling extremely low rescaled 55555 values are given in Appendix C. In most cases, alternative approaches reproduce similar results to those presented in the main body of the paper. However, the significant influence of worry and subjective risk on rescaled 55555 values is not reproduced in around half the robustness analyses. Similarly, the finding that those reporting a negative influence of COVID-19 on quality of life rated 55555 lower was not found in several alternative analyses.

## Discussion

There are indications in our results that how individuals value health was influenced by the onset of the COVID-19 pandemic. Yet it is also clear that the reasons/drivers for this finding are complex, and people’s reactions to different aspects of the pandemic are difficult to untangle. For example, several COVID-19-related variables had a significant effect on some health states, but not others, and it is difficult to understand why. There is also evidence that subjective risk of and worry about COVID-19 infection had opposite effects for both dead and rescaled 55555. The differing impact of people’s self-assessed likelihood of catching COVID-19 infection and their worry about infection may be due to the danger the disease poses depending heavily on factors such as age and co-morbidities \[25–27\]. Supporting this hypothesis, worry about COVID-19 infection was significantly correlated with age (correlation 0.08, Pearson’s test *p* value \< 0.001) but subjective risk of infection was not (correlation 0.02, Pearson’s test *p* value 0.225).

In several instances, those reporting that COVID-19 had affected their health gave significantly different responses compared to those who reported no effect. However, the direction of change was the same whether the effect of COVID-19 was positive or negative. One interpretation is that individuals’ health being affected either way by a pandemic disease which dominated public life caused them to reassess their views on health. Another possibility is that the result is due to a small sample size, as only around 5% of respondents said COVID-19 has positively affected their health. This group also likely differed systematically from the general population, since positive health impacts were likely due to factors such as avoiding an arduous commute and/or an unpleasant workplace. People who said COVID-19 positively affected their health were 81.3% employed/self-employed, compared to 60.2% for other individuals, and were also younger, with an average age of 38.8 compared to 49.8 for other respondents, lending weight to the supposition. While MNPS can theoretically eliminate differences in observed characteristics between groups, the worst balancing performance was seen for COVID-19’s impact on health, largely due to the small number reporting a positive effect.

While there were no significant correlations between VAS ratings and how often people left the house for shopping, there were significant and non-linear effects for exercise in the Tobit regressions in Table <a href="#Tab3" data-ref-type="table">3</a>. These effects are difficult to interpret, due to it being unclear how large an impact the pandemic had on respondents’ behaviour. COVID-19 may have influenced how often people leave the houses for fresh air and exercise in different ways: Many will have gone out less to mitigate risk of infection, yet others may have exercised outside more, e.g. due to previously preferring alternative leisure activities. It should also be noted that although the signs of the exercise coefficients in MNPS also reflected a non-linear effect, they were not significant.

No significant effects were seen for regional COVID-19 cases or deaths. This could be due to people’s experience of the pandemic being driven either by national level reporting, or by cases reported in much smaller geographic areas, with regional variations of less importance.

Examining the magnitudes of the significant effects, there were some large effects for VAS ratings. For example, in the Tobit analysis, those whose health was positively affected by COVID-19 rated dead 14.8 points higher than those who did not, a difference covering around a seventh of the VAS range from 0 to 100. However, differences in rescaled values of 55555 were typically small, with magnitudes between 0.005 and 0.07. This is comparable to the smallest utility decrement in Devlin et al.’s \[28\] English EQ-5D-5L value set at 0.05. Thus, it may be that any changes to how people value health due to COVID-19 on the full health = 1, dead = 0 scale are relatively small.

Comparing the Tobit and MNPS results, in many cases, they are in agreement in terms of the significance and sign of coefficients. Where this is not the case, it is almost always a significant result using one approach, and an insignificant coefficient with the same sign using the other. Thus, it does not appear that using one approach leads to radically different conclusions than using the other.

It was difficult to determine a causal effect of COVID-19 on health state valuation. It may be that individuals who were more affected by the pandemic also systematically valued health differently from people who were less affected. Including control variables in the Tobit regressions and MNPS analysis mitigates this possibility to some extent. However, they can only control for the influence of observable characteristics. It is plausible that unmeasured personality traits, for example, with risk tolerance, could be associated both with health state valuation and measures of COVID-19’s impact such as subjective risk/worry about infection.

The results presented here represent a stronger (though by no means conclusive) argument for a causal influence of COVID-19 on health-state valuation when viewed as complementary to previous findings in Webb et al. \[20\]. That work showed significant differences in VAS ratings between before (2018) and during the pandemic (2020), and proposed that the pandemic is the most likely cause. And, that some COVID-19-related variables are significantly correlated in this study with VAS responses gives weight to this proposal.

The findings of the two studies are not always in the same direction. For example, in Webb et al. \[20\], VAS ratings for dead were lower in 2020 than in 2018, yet here, subjective risk of infection and COVID-19 affecting health lead to higher ratings. This is not necessarily contradictory, however. Some COVID-19-related variables, such as worry about infection, were shown in this study to have a negative effect on VAS ratings for dead, and in the previous study, some subgroups rated dead higher in 2020 than in 2018. As there are complicated interactions between individual characteristics and COVID-19 can affect people indifferent ways, it is not easy to compare the two studies’ results.

This study only presents evidence from the initial phase of the pandemic in the UK. Whether any acute changes to health state valuations persist is an unresolved question. The question will be addressed in part by the ongoing national UK EQ-5D-5L valuation study, in preparation since before the pandemic.[^3] However, in most other countries, national valuation studies are not planned in the near future.

Our analysis sample was not representative of the UK population. In particular, it is difficult to tell how representative our respondents were in terms of the dependent variables of interest. For example, while there are other survey studies measuring risk and/or worry attitudes in the UK at a similar time (e.g. \[29–31\]), none used exactly the same measures. Different question phrasing and scales make it difficult to compare our participants’ attitudes to those reported elsewhere. Thus, it would not be possible to “re-adjust” existing UK value sets using our results. Another reason why such re-adjustment would not be possible is that the analysis sample is not representative in demographic terms, and the Tobit analysis revealed that demographic factors influenced VAS ratings. For example, female respondents rated 11111 higher and 55555 lower than male respondents and white respondents rated dead lower than non-white respondents.

That demographic characteristics affected VAS ratings raises the question as to whether COVID-19 may have had different impacts among different demographic groups. Investigating this possibility would be a useful topic for future research.

### Policy implications

It is unclear whether knowledge about acute changes to health state values would have had a meaningful impact on how public money was spent in the first few months of the pandemic \[32\]. While some retrospective analyses of COVID-19 spending have been conducted \[33–36\], it is not clear that measures of cost-effectiveness were a factor in decision-making in the initial crisis stages \[37–40\]. Ultimately whether decision-making in an acute crisis should take account of cost-effectiveness measures such as maximising QALY gain per pound spent is a question for policymakers (and by extension the voters who appoint them in a democratic society). Yet if anyone should wish to advocate for a larger role of health economics or health state values in future crises, it is essential to have a firm understanding of, and evidence base for, the validity of health economic techniques in such crises.

We present evidence relating to the COVID-19 pandemic only, and not from any other crisis event which could influence values. Yet that one crisis can influence preferences for health states should be a prompt to investigate to what extent other crises could also affect how people value health.

In the longer term, large-scale EQ-5D valuation studies are resource intensive, so it is impractical to construct new ones in every country in the wake of COVID-19, or after every political, historical or health crisis event that may or may not affect how people think about and value health. Many allocation decisions are long term, such as approving health technologies for use for the foreseeable future. It is not clear that such decisions should be influenced by any short-term preference fluctuations.

Nevertheless, our findings suggest the need to develop standardised, resource-light methods to assess whether and how national EQ-5D value sets still reflect people’s preferences, attitudes and values. Such methods could involve collecting smaller amounts of data than full-scale national value sets, or using less resource intensive methods such as online self-complete surveys. Another approach could be re-analysing existing data (see Webb and Kind \[41\] for a tentative step in this direction).

### Strengths and weaknesses

This study has several strengths. As far as we are aware, this paper and our previous one are the only studies to address whether a large-scale crisis event has affected population health state valuations. Data collection was timely, giving insight into how people valued health shortly after the onset of the COVID-19 pandemic in the UK. We also used complementary analysis techniques: MNPS increased the possibility of identifying causal effects for individual variables, enabling us to disentangle the various effects of different aspects of the pandemic, while the Tobit regressions allowed for continuous dependent variables and interaction terms, as well as exploiting the full variation in the data without compressing responses into coarser categories.

The VAS task asked individuals to give an explicit value for dead, relative to the worst health they can imagine, in contrast to methods such as time trade-off where dead is always assigned a value of 0. This allows us to investigate individuals’ attitudes to health and death, and to what extent people believe any health states are worse than dead. The survey collected several different COVID-19-related variables. This has allowed us to distinguish between different aspects of how the pandemic has affected people.

This study also has several weaknesses. For example, some results were not robust to using different methods to censor or remove extremely low rescaled 55555 values. We valued health states using VAS, whereas national value sets are more usually created using other techniques such as TTO \[21\]. Thus, it may be that our findings would not have been robust to using a more standard technique. Yet if VAS and TTO both elicit the same underlying health preferences, changes found using one technique should be expected to be found using the other.

The only EQ-5D-5L state for which values on the full health = 1, dead = 0 scale was found was 55555. While this state has theoretical importance as the worst state in the classification system, few people report being in it. Thus, it is difficult to say what impact COVID-19 would have on more commonly experienced health states. Age is a large risk factor in COVID-19 mortality and severe illness \[42–44\], so it is older people where the largest effects might be expected to be seen. However, the survey collected relatively few older respondents, with, for example, only 4.1% of the analysis sample aged 75 or older.

## Conclusion

We presented evidence that the COVID-19 pandemic may have affected how people value health, as was also seen in Webb et al. \[20\]. However, there were differences in what aspects of the pandemic influenced individuals’ values. For example, there were differences between people who did and did not report that COVID-19 had affected their health, but no analogous finding for its effect on quality of life. Future research is required to disentangle the complex situation.

Future research could also investigate the influence on valuation of other important health events, or political/social shocks. It would also be useful to investigate whether any effects on valuation, due to COVID-19 or other events, are permanent or transient.

Finally, our results suggest the need to develop standardised methods to quickly and easily assess whether national EQ-5D value sets still represent national values.

##### Appendix

###### Appendix A COVID-19-related survey questions

Do you worry about being infected with the Corona virus?

<div id="Taba" class="table-wrap">

| 1 | 2 | 2 | 4 | 5 |
|----|----|----|----|----|
| Never thought about it | Thought about it, but not worried | Worried me a bit | Worried me a lot | Worried about it all the time |

</div>

What do you think are your chances of becoming infected with the Corona virus?

<div id="Tabb" class="table-wrap">

| 1             | 2      | 3                          | 4        | 5               |
|---------------|--------|----------------------------|----------|-----------------|
| Highly likely | Likely | Equally likely or unlikely | Unlikely | Highly unlikely |

Note: This variable was re-coded for analysis so higher numbers mean higher subjective risk

</div>

Over the past couple of weeks has the COVID-19 pandemic affected your health?

- Yes—it has affected my health for the better

- Yes—it has affected my health for the worse

- No—it has not affected my health

Over the past couple of weeks has the COVID-19 pandemic affected your quality of life?

- Yes—my quality of life has changed for the better

- Yes—my quality of life has changed for the worse

- No—it has not affected my quality of life

Since the start of the COVID-19 lockdown, how often do you leave home to buy food or other essentials?

- Not at all / never

- Less than once a week

- Once a week

- 2–6 times a week

- Once a day

- Several times a day

Since the start of the COVID-19 pandemic, how often do you go outside for fresh air and exercise?

- Not at all / never

- Less than once a week

- Once a week

- 2–6 times a week

- Once a day

- Several times a day

###### Appendix B Comparison of wave 1 and wave 2 demographics

See below Appendix, Table <a href="#Tab5" data-ref-type="table">5</a> here.

<div id="Tab5" class="table-wrap">

<div class="caption">

Comparison of wave 1 and wave 2 demographics

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Wave 1 <em>N</em></th>
<th style="text-align: left;">Wave 2 <em>N</em></th>
<th style="text-align: left;"><em>p</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;"><em>Age</em></td>
</tr>
<tr>
<td style="text-align: left;">Mean (standard deviation)</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">49.7</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Female</em></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">637</td>
<td style="text-align: left;">648</td>
<td>0.775</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Ethnicity</em></td>
</tr>
<tr>
<td style="text-align: left;">White</td>
<td style="text-align: left;">1147</td>
<td style="text-align: left;">1190</td>
<td>0.397</td>
</tr>
<tr>
<td style="text-align: left;">Asian</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">56</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Mixed</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">19</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Black</td>
<td style="text-align: left;">41</td>
<td style="text-align: left;">33</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">20</td>
<td></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Occupation</em></td>
</tr>
<tr>
<td style="text-align: left;">Employed</td>
<td style="text-align: left;">755</td>
<td style="text-align: left;">799</td>
<td>0.22</td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: left;">285</td>
<td style="text-align: left;">307</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Housework</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">82</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Student</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">34</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: left;">46</td>
<td style="text-align: left;">49</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Missing</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">15</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: left;">26</td>
<td style="text-align: left;">32</td>
<td></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Education</em></td>
</tr>
<tr>
<td style="text-align: left;">Left school after minimum age</td>
<td style="text-align: left;">999</td>
<td style="text-align: left;">1026</td>
<td>0.931</td>
</tr>
<tr>
<td style="text-align: left;">Degree or equivalent qualification</td>
<td style="text-align: left;">665</td>
<td style="text-align: left;">703</td>
<td>0.467</td>
</tr>
<tr>
<td style="text-align: left;">In 11111</td>
<td style="text-align: left;">455</td>
<td style="text-align: left;">481</td>
<td>0.605</td>
</tr>
<tr>
<td style="text-align: left;">EQ-VAS</td>
<td style="text-align: left;">74.5</td>
<td style="text-align: left;">74.8</td>
<td>0.732</td>
</tr>
<tr>
<td style="text-align: left;">Long-term condition</td>
<td style="text-align: left;">384</td>
<td style="text-align: left;">402</td>
<td>0.771</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Number of comorbidities</em></td>
</tr>
<tr>
<td style="text-align: left;">Mean (standard deviation)</td>
<td style="text-align: left;">0.644</td>
<td style="text-align: left;">0.605</td>
<td>0.963</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Description of own health</em></td>
</tr>
<tr>
<td style="text-align: left;">Excellent</td>
<td style="text-align: left;">161</td>
<td style="text-align: left;">145</td>
<td>0.393</td>
</tr>
<tr>
<td style="text-align: left;">Very good</td>
<td style="text-align: left;">451</td>
<td style="text-align: left;">478</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Good</td>
<td style="text-align: left;">436</td>
<td style="text-align: left;">436</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Fair</td>
<td style="text-align: left;">188</td>
<td style="text-align: left;">210</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Poor</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">49</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><em>N</em></td>
<td style="text-align: left;">1281</td>
<td style="text-align: left;">1318</td>
<td></td>
</tr>
</tbody>
</table>

Note. *p*-values for Mann–Whitney *U* tests

</div>

###### Appendix C Full Tobit results

See below Appendix, Tables <a href="#Tab6" data-ref-type="table">6</a>, <a href="#Tab7" data-ref-type="table">7</a>, <a href="#Tab8" data-ref-type="table">8</a> and <a href="#Tab9" data-ref-type="table">9</a> here.

<div id="Tab6" class="table-wrap">

<div class="caption">

Tobit regression results for both waves

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">11111</th>
<th style="text-align: left;">s.e</th>
<th style="text-align: left;">Dead</th>
<th style="text-align: left;">s.e</th>
<th style="text-align: left;">55555</th>
<th style="text-align: left;">s.e</th>
<th style="text-align: left;">55555 rescaled</th>
<th style="text-align: left;">s.e</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Constant</td>
<td>99.2*</td>
<td>4.03</td>
<td>16.7</td>
<td style="text-align: left;">10.2</td>
<td>19.1*</td>
<td>5.04</td>
<td style="text-align: left;"> – 0.0935</td>
<td style="text-align: left;">0.0927</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td> – 0.0662</td>
<td>0.152</td>
<td> – 0.501</td>
<td style="text-align: left;">0.389</td>
<td>0.167</td>
<td>0.191</td>
<td style="text-align: left;">5.82 × 10–3</td>
<td style="text-align: left;">3.5 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;">Age<sup>2</sup></td>
<td>3.68 × 10–4</td>
<td>1.65 × 10–3</td>
<td>2.46 × 10–3</td>
<td style="text-align: left;">4.3 × 10–3</td>
<td> – 3.68 × 10–3</td>
<td>2.1 × 10–3</td>
<td style="text-align: left;"> – 5.56 × 10–5</td>
<td style="text-align: left;">3.83 × 10–5</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td>3.27*</td>
<td>0.774</td>
<td> – 3.67</td>
<td style="text-align: left;">2</td>
<td> – 3.68*</td>
<td>0.975</td>
<td style="text-align: left;"> – 0.011</td>
<td style="text-align: left;">0.0179</td>
</tr>
<tr>
<td style="text-align: left;">White</td>
<td>4.03*</td>
<td>1.27</td>
<td> – 17.9*</td>
<td style="text-align: left;">3.08</td>
<td> – 5.62*</td>
<td>1.58</td>
<td style="text-align: left;">0.0787*</td>
<td style="text-align: left;">0.0294</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>Education</em></td>
</tr>
<tr>
<td style="text-align: left;">Left school after minimum age</td>
<td>1.57</td>
<td>1.1</td>
<td> – 6.97*</td>
<td style="text-align: left;">2.9</td>
<td> – 0.864</td>
<td>1.4</td>
<td style="text-align: left;">8.59 × 10–3</td>
<td style="text-align: left;">0.0256</td>
</tr>
<tr>
<td style="text-align: left;">Degree</td>
<td> – 0.946</td>
<td>0.946</td>
<td>7.11*</td>
<td style="text-align: left;">2.49</td>
<td>0.694</td>
<td>1.19</td>
<td style="text-align: left;"> – 0.0192</td>
<td style="text-align: left;">0.0218</td>
</tr>
<tr>
<td style="text-align: left;">Live alone</td>
<td>0.774</td>
<td>0.984</td>
<td> – 4.35</td>
<td style="text-align: left;">2.59</td>
<td> – 2.96*</td>
<td>1.25</td>
<td style="text-align: left;"> – 9.81 × 10–6</td>
<td style="text-align: left;">0.0228</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>Occupation</em></td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td> – 0.864</td>
<td>1.62</td>
<td>3.5</td>
<td style="text-align: left;">4.25</td>
<td>1.61</td>
<td>2.06</td>
<td style="text-align: left;"> – 0.0347</td>
<td style="text-align: left;">0.0376</td>
</tr>
<tr>
<td style="text-align: left;">Employed</td>
<td> – 1.66</td>
<td>1.11</td>
<td>1.8</td>
<td style="text-align: left;">2.83</td>
<td>0.381</td>
<td>1.39</td>
<td style="text-align: left;"> – 1.49 × 10–3</td>
<td style="text-align: left;">0.0257</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>EQ-5D</em></td>
</tr>
<tr>
<td style="text-align: left;">Mobility levels 2–5</td>
<td> – 0.217</td>
<td>1.35</td>
<td> – 3.11</td>
<td style="text-align: left;">3.51</td>
<td>2.49</td>
<td>1.71</td>
<td style="text-align: left;">0.0695*</td>
<td style="text-align: left;">0.0316</td>
</tr>
<tr>
<td style="text-align: left;">Self-care levels 2–5</td>
<td> – 0.759</td>
<td>1.65</td>
<td>7.11</td>
<td style="text-align: left;">4.16</td>
<td>3.7</td>
<td>2.09</td>
<td style="text-align: left;"> – 0.0291</td>
<td style="text-align: left;">0.0388</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities levels 2–5</td>
<td> – 2.22</td>
<td>1.38</td>
<td>6.9</td>
<td style="text-align: left;">3.53</td>
<td>3.27</td>
<td>1.75</td>
<td style="text-align: left;"> – 0.0136</td>
<td style="text-align: left;">0.0323</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort levels 2–5</td>
<td>0.188</td>
<td>0.941</td>
<td>3.78</td>
<td style="text-align: left;">2.43</td>
<td>0.837</td>
<td>1.19</td>
<td style="text-align: left;"> – 0.0249</td>
<td style="text-align: left;">0.0218</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression levels 2–5</td>
<td> – 2.01*</td>
<td>0.862</td>
<td>5.11*</td>
<td style="text-align: left;">2.23</td>
<td>1.74</td>
<td>1.09</td>
<td style="text-align: left;"> – 0.0153</td>
<td style="text-align: left;">2 × 10–2</td>
</tr>
<tr>
<td style="text-align: left;">Number of co-morbidities</td>
<td>0.707</td>
<td>0.399</td>
<td>0.465</td>
<td style="text-align: left;">1.02</td>
<td> – 0.433</td>
<td>0.505</td>
<td style="text-align: left;"> – 0.0114</td>
<td style="text-align: left;">9.3 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;">Description of own health</td>
<td> – 3.45*</td>
<td>0.471</td>
<td> – 0.45</td>
<td style="text-align: left;">1.2</td>
<td>0.49</td>
<td>0.592</td>
<td style="text-align: left;">4.43 × 10–3</td>
<td style="text-align: left;">0.0109</td>
</tr>
<tr>
<td style="text-align: left;">Cumulative COVID-19 cases</td>
<td> – 0.013</td>
<td>0.0161</td>
<td>0.0399</td>
<td style="text-align: left;">0.0417</td>
<td>5.85 × 10–3</td>
<td>0.0203</td>
<td style="text-align: left;"> – 1.25 × 10–4</td>
<td style="text-align: left;">3.72 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;">Cumulative COVID-19 deaths</td>
<td>0.118</td>
<td>0.0712</td>
<td> – 0.248</td>
<td style="text-align: left;">0.184</td>
<td> – 0.0431</td>
<td>0.0897</td>
<td style="text-align: left;">9.33 × 10–4</td>
<td style="text-align: left;">1.65 × 10–3</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>Worry about being infected with COVID-19</em></td>
</tr>
<tr>
<td style="text-align: left;">(1 = never thought about it, 5 = all the time)</td>
<td>0.0331</td>
<td>0.823</td>
<td>0.101</td>
<td style="text-align: left;">2.12</td>
<td> – 0.827</td>
<td>1.03</td>
<td style="text-align: left;"> – 0.0158</td>
<td style="text-align: left;">0.0189</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>Subjective risk of COVID-19 infection</em></td>
</tr>
<tr>
<td style="text-align: left;">(1 = highly unlikely, 5 = highly likely)</td>
<td> – 0.847</td>
<td>0.862</td>
<td>7.71*</td>
<td style="text-align: left;">2.16</td>
<td>1.98</td>
<td>1.07</td>
<td style="text-align: left;"> – 0.0578*</td>
<td style="text-align: left;">0.0198</td>
</tr>
<tr>
<td style="text-align: left;">Worry × subjective risk</td>
<td>0.206</td>
<td>0.351</td>
<td> – 2.12*</td>
<td style="text-align: left;">0.9</td>
<td> – 0.0427</td>
<td>0.438</td>
<td style="text-align: left;">0.0193*</td>
<td style="text-align: left;">8.08 × 10–3</td>
</tr>
</tbody>
</table>

Note. *N* = 2599, *s.e.* standard error, \*significant at 5% level

</div>

<div id="Tab7" class="table-wrap">

<div class="caption">

Tobit regression results including whether COVID-19 affected health or quality of life

</div>

|  | 11111 | s.e | Dead | s.e | 55555 | s.e | 55555 rescaled | s.e |
|----|----|----|----|----|----|----|----|----|
| Constant | 95.4\* | 6.13 | -5.9 | 15.1 | 26.8\* | 7.69 | 0.148 | 0.136 |
| Age | 0.0483 | 0.218 | 0.234 | 0.551 |  – 0.0114 | 0.276 | 1.53 × 10–3 | 4.87 × 10–3 |
| Age<sup>2</sup> |  – 1.16 × 10–3 | 2.33 × 10–3 |  – 5.26 × 10–3 | 6.02 × 10–3 |  – 2.12 × 10–3 | 2.97 × 10–3 |  – 1.98 × 10–5 | 5.21 × 10–5 |
| Female | 2.98\* | 1.07 |  – 2.77 | 2.69 |  – 3.6\* | 1.35 |  – 2.92 × 10–3 | 0.0239 |
| White | 2.94 | 1.75 |  – 12.2\* | 4.14 |  – 3.02 | 2.2 | 0.057 | 0.0393 |
| *Education* |  |  |  |  |  |  |  |  |
| Left school after minimum age | 1.56 | 1.5 |  – 5.77 | 3.85 |  – 2.27 | 1.91 |  – 8.12 × 10–3 | 0.0336 |
| Degree |  – 1.31 | 1.29 | 4.54 | 3.3 | 2.2 | 1.63 | 0.0238 | 0.0287 |
| Live alone | 1.36 | 1.34 |  – 3.99 | 3.47 |  – 3.16 | 1.71 |  – 0.0107 | 0.0299 |
| *Occupation* |  |  |  |  |  |  |  |  |
| Retired | 1.03 | 2.19 | 4.71 | 5.63 | 0.633 | 2.79 |  – 0.0329 | 0.0491 |
| Employed—key worker |  – 1.64 | 1.64 |  – 5.31 | 4.07 |  – 1.07 | 2.06 | 9.54 × 10–4 | 0.0365 |
| Employed—non-key worker |  – 1.65 | 1.75 | 4.78 | 4.24 | 1.54 | 2.19 |  – 0.019 | 0.039 |
| *EQ-5D* |  |  |  |  |  |  |  |  |
| Mobility levels 2–5 | 0.643 | 1.83 |  – 4.95 | 4.64 | 3.01 | 2.33 | 0.0979\* | 0.0413 |
| Self-care levels 2–5 | 0.865 | 2.32 | 4.57 | 5.71 | 2.95 | 2.95 | 4.35 × 10–3 | 0.0528 |
| Usual activities levels 2–5 | -1.86 | 1.93 | 3.23 | 4.84 | 1.55 | 2.47 |  – 0.0338 | 0.0439 |
| Pain/discomfort levels 2–5 | 0.333 | 1.28 | 3.12 | 3.22 |  – 0.304 | 1.63 |  – 0.0189 | 0.0287 |
| Anxiety/depression levels 2–5 |  – 2.09 | 1.19 | 7.19\* | 3 | 1.73 | 1.5 |  – 8.14 × 10–3 | 0.0266 |
| Number of co-morbidities | 0.528 | 0.562 | 1.55 | 1.39 |  – 7.36 × 10–3 | 0.715 |  – 0.0238 | 0.0127 |
| Description of own health |  – 3.96\* | 0.638 | 0.77 | 1.58 | 0.585 | 0.805 | 2.76 × 10–3 | 0.0143 |
| Cumulative COVID-19 cases |  – 8.01 × 10–3 | 0.0198 | 0.0318 | 0.0498 |  – 4.29 × 10–4 | 0.0251 |  – 3.43 × 10–4 |  – 3.77 × 10–4 |
| Cumulative COVID-19 deaths | 0.12 | 0.0946 |  – 0.0901 | 0.239 |  – 0.0342 | 0.12 | 5.88 × 10–4 | 7 × 10–4 |
| Worry about being infected with COVID-19 |  |  |  |  |  |  |  |  |
| (1 = never thought about it, 5 = all the time) | 1.37 | 1.12 |  – 2.19 | 2.81 |  – 1.57 | 1.42 |  – 0.0198 | 0.0251 |
| Subjective risk of COVID-19 infection |  |  |  |  |  |  |  |  |
| (1 = highly unlikely, 5 = highly likely) | 0.0996 | 1.15 | 3.97 | 2.77 | 0.537 | 1.45 |  – 0.0543\* | 0.0258 |
| Worry x subjective risk |  – 0.223 | 0.473 |  – 1.06 | 1.17 | 0.0805 | 0.596 | 0.0167 | 0.0106 |
| COVID-19 affected health |  |  |  |  |  |  |  |  |
| Negatively (baseline no) |  – 0.154 | 1.5 | 4.67 | 3.71 | 4.74\* | 1.89 | 0.0168 | 0.0337 |
| Positively | 1.33 | 2.55 | 14.8\* | 5.84 | 6.18\* | 3.15 |  – 0.0336 | 0.0566 |
| COVID-19 affected quality of life (baseline no) |  |  |  |  |  |  |  |  |
| Negatively | 0.304 | 1.15 |  – 2.96 | 2.94 |  – 0.993 | 1.46 |  – 9.71 × 10–3 | 0.0258 |
| Positively |  – .54 | 2.09 | 8.5 | 5 | 0.804 | 2.64 |  – 0.0763 | 0.0471 |

Note. *N* = 1294, *s.e.* standard error, \*significant at 5% level

</div>

<div id="Tab8" class="table-wrap">

<div class="caption">

Tobit regression results including frequency of leaving the house for shopping

</div>

|  | 11111 | s.e | Dead | s.e | 55555 | s.e | 55555 rescaled | s.e |
|----|----|----|----|----|----|----|----|----|
| Constant | 107\* | 4.97 | 8.27 | 12.1 | 21.3\* | 6.31 |  – 0.0755 | 0.109 |
| Age |  – 0.164 | 0.201 |  – 0.136 | 0.508 | 0.0236 | 0.258 | 5.34 × 10–3 | 4.43 × 10–3 |
| Age<sup>2</sup> | 1.1 × 10–3 | 2.15 × 10–3 |  – 3.23 × 10–3 | 5.54 × 10–3 |  – 2.92 × 10–3 | 2.78 × 10–3 |  – 4.94 × 10–5 | 4.75 × 10–5 |
| Female | 2.43\* | 0.985 |  – 3.88 | 2.49 |  – 2.68\* | 1.27 | 2.92 × 10–3 | 0.0218 |
| White | 2.36 | 1.66 |  – 10.4\* | 3.95 |  – 2.01 | 2.13 | 0.0448 | 0.0368 |
| Education |  |  |  |  |  |  |  |  |
| Left school after minimum age | 1.17 | 1.38 |  – 5.8 | 3.56 |  – 2.25 | 1.79 |  – 0.0138 | 0.0306 |
| Degree |  – 0.973 | 1.17 | 5.66 | 3 | 2.59 | 1.5 | 0.0146 | 0.0257 |
| Live alone | 0.869 | 1.22 |  – 3.12 | 3.14 |  – 3.03 | 1.58 |  – 0.013 | 0.0269 |
| Occupation |  |  |  |  |  |  |  |  |
| Retired | 0.114 | 1.98 | 7.61 | 5.1 | 2.96 | 2.57 |  – 0.0445 | 0.0439 |
| Employed—key worker |  – 1.54 | 1.47 |  – 1.12 | 3.68 | 0.729 | 1.89 |  – 0.0164 | 0.0325 |
| Employed—non-key worker |  – 1.04 | 1.58 | 6.13 | 3.88 | 2.31 | 2.02 |  – 0.0349 | 0.0349 |
| EQ-5D |  |  |  |  |  |  |  |  |
| Mobility levels 2–5 |  – 0.716 | 1.64 |  – 5.03 | 4.22 | 2.97 | 2.14 | 0.0993\* | 0.0368 |
| Self-care levels 2–5 | 1.38 | 2.09 | 6.94 | 5.13 | 4.37 | 2.71 |  – 0.0189 | 0.047 |
| Usual activities levels 2–5 |  – 2.59 | 1.73 | 5.12 | 4.36 | 2.81 | 2.25 |  – 0.0198 | 0.0389 |
| Pain/discomfort levels 2–5 | 0.228 | 1.15 | 2.89 | 2.91 |  – 1.4 | 1.5 |  – 0.036 | 0.0256 |
| Anxiety/depression levels 2–5 |  – 1.59 | 1.05 | 6.55\* | 2.66 | 1.91 | 1.36 |  – 7.3 × 10–3 | 0.0233 |
| Number of co-morbidities | 0.909 | 0.517 | 1.78 | 1.28 |  – 0.38 | 0.67 |  – 0.0347\* | 0.0115 |
| Description of own health |  – 3.38\* | 0.577 |  – 0.764 | 1.44 | 0.695 | 0.743 | 0.0153 | 0.0128 |
| How often go shopping (baseline never) |  |  |  |  |  |  |  |  |
|  \< weekly |  – 1.56 | 1.67 | 1 | 4.22 |  – 1.22 | 2.15 |  – 0.0111 | 0.0368 |
| Weekly |  – 0.882 | 1.47 |  – 2.92 | 3.76 | 0.0746 | 1.89 | 3.53 × 10–3 | 0.0324 |
| 2–6 times per week |  – 1.9 | 1.67 | 6.9 | 4.2 |  – 0.227 | 2.16 |  – 0.0415 | 0.0369 |
| Daily |  – 5.04 | 2.68 | 10.4 | 6.58 | 5.03 | 3.49 | 0.0116 | 0.0604 |
|  \> daily |  – 0.844 | 7.05 | 5.83 | 17 | 15.7 | 8.89 | 0.201 | 0.157 |

Note. *N*  1294, *s.e.* standard error, \*significant at 5% level

</div>

<div id="Tab9" class="table-wrap">

<div class="caption">

Tobit regression results including frequency of leaving the house for exercise and fresh air

</div>

|  | 11111 | s.e | Dead | s.e | 55555 | s.e | 55555 rescaled | s.e |
|----|----|----|----|----|----|----|----|----|
| Constant | 108\* | 4.97 | 2.45 | 12.2 | 17.6\* | 6.32 |  – 0.0745 | 0.109 |
| Age |  – 0.164 | 0.199 |  – 0.198 | 0.501 | 0.0397 | 0.256 | 5.34 × 10–3 | 4.4 × 10–3 |
| Age<sup>2</sup> | 9.56 × 10–4 | 2.12 × 10–3 |  – 2.08 × 10–3 | 5.46 × 10–3 |  – 2.89 × 10–3 | 2.76 × 10–3 |  – 5.02 × 10–5 | 4.72 × 10–5 |
| Female | 2.66\* | 0.976 |  – 4.52 | 2.47 |  – 2.84\* | 1.26 | 2.8 × 10–3 | 0.0217 |
| White | 2.01 | 1.68 |  – 8.67\* | 4 |  – 1.66 | 2.16 | 0.0379 | 0.0375 |
| Education |  |  |  |  |  |  |  |  |
| Left school after minimum age | 1.34 | 1.38 |  – 5.52 | 3.55 |  – 2.39 | 1.79 |  – 0.0175 | 0.0306 |
| Degree |  – 1.04 | 1.16 | 5.35 | 2.99 | 2.48 | 1.5 | 0.0153 | 0.0257 |
| Live alone | 0.686 | 1.21 |  – 2.61 | 3.13 |  – 2.75 | 1.58 |  – 0.0123 | 0.0269 |
| Occupation |  |  |  |  |  |  |  |  |
| Retired | 0.2 | 1.97 | 6.55 | 5.09 | 2.65 | 2.57 |  – 0.0451 | 0.044 |
| Employed—key worker |  – 1.51 | 1.47 |  – 1.59 | 3.67 | 0.364 | 1.89 |  – 0.018 | 0.0326 |
| Employed—non-key worker |  – 1.12 | 1.58 | 6.04 | 3.86 | 2.24 | 2.02 |  – 0.0352 | 0.0349 |
| EQ-5D |  |  |  |  |  |  |  |  |
| Mobility levels 2–5 |  – 0.893 | 1.64 |  – 4.81 | 4.2 | 3.15 | 2.14 | 0.101\* | 0.0368 |
| Self-care levels 2–5 | 1.93 | 2.08 | 6.39 | 5.11 | 4.22 | 2.7 |  – 0.0147 | 0.047 |
| Usual activities levels 2–5 |  – 2.57 | 1.72 | 4.6 | 4.32 | 2.69 | 2.25 |  – 0.0196 | 0.0388 |
| Pain/discomfort levels 2–5 | 0.113 | 1.15 | 2.93 | 2.91 |  – 1.33 | 1.5 |  – 0.0367 | 0.0257 |
| Anxiety/depression levels 2–5 |  – 1.67 | 1.05 | 6.86\* | 2.66 | 1.85 | 1.36 |  – 9.67 × 10–3 | 0.0234 |
| Number of co-morbidities | 0.859 | 0.514 | 2.06 | 1.27 |  – 0.314 | 0.668 |  – 0.0357\* | 0.0115 |
| Description of own health |  – 3.3\* | 0.578 |  – 0.814 | 1.44 | 0.698 | 0.745 | 0.0168 | 0.0128 |
| How often exercise (baseline never) |  |  |  |  |  |  |  |  |
|  \< weekly |  – 4.29\* | 2.02 | 12.2\* | 5.04 | 3.89 | 2.61 |  – 0.0155 | 0.0449 |
| Weekly |  – 4.65\* | 1.98 | 14.1\* | 4.96 | 7.22\* | 2.56 |  – 0.0251 | 0.0442 |
| 2–6 times per week |  – 1.68 | 1.69 | 1.68 | 4.37 | 2.59 | 2.18 | 0.0255 | 0.0374 |
| Daily |  – 2.15 | 1.69 | 5.28 | 4.36 | 2.78 | 2.19 |  – 5.47 × 10–3 | 0.0373 |
|  \> daily | 2.59 | 2.59 | 6.67 | 6.5 | 0.531 | 3.31 |  – 0.0131 | 0.0563 |

Note. *N*  1294, *s.e.* standard error, \*significant at 5% level

</div>

###### Appendix D Alternative methods of censoring rescaled 55555 values

The main analysis presents results with rescaled 55555 values censored at  – 1. For robustness, additional analyses were run with the censoring threshold of  – 1 and  – 2. In addition, a number of additional analyses were run using four separate criteria for removing participants.

1.  Low rescaled 55555 values

    Individuals’ VAS responses were removed from the data if their rescaled 55555 values fell below a given threshold. Analyses were run with thresholds of  – 1,  – 1.5 and  – 2.

2.  Large impact on mean rescaled 55555 values

    Similar to the approach used in Webb et al. (2020), individuals were removed from the data if their responses had a large impact on the mean rescaled value of 55555. The influence of each individual on the mean was found by calculating the differences between the mean with or without a given individual included. Individuals were then excluded if their influence was more than a given number of standard deviations away from the mean influence. Analyses were run with thresholds of 1.5, 2 and 2.5 standard deviations.

3.  High VAS rating for dead

    Many extremely low rescaled values are as a result of an arguably implausibly high rating for dead. Thus, analyses were re-run excluding respondents who rated dead above thresholds of 75, 50 and 25.

4.  High rate of change of rescaled 55555 values with respect to raw values

    A potential cause of extremely low rescaled 55555 values was placing 11111 and dead very close together, meaning that small changes to 55555 on the 100–0 scale led to large changes on the 1–0 scale. Such rescaled values were unlikely to be accurate, so participants were excluded if their rate of change was above a given threshold. The rate of change of the rescaled value of 55555 with respect to the raw value is
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
                    \begin{document}$${\raise0.7ex\hbox{${\partial VAS_{55555}^{{{\text{rescaled}}}} }$} \!\mathord{\left/ {\vphantom {{\partial VAS_{55555}^{{{\text{rescaled}}}} } {\partial VAS_{55555} }}}\right.\kern-0pt} \!\lower0.7ex\hbox{${\partial VAS_{55555} }$}} = {\raise0.7ex\hbox{$1$} \!\mathord{\left/ {\vphantom {1 {\left( {VAS_{11111} - VAS_{{{\text{dead}}}} } \right)}}}\right.\kern-0pt} \!\lower0.7ex\hbox{${\left( {VAS_{11111} - VAS_{{{\text{dead}}}} } \right)}$}}$$\end{document}
    ```

    Participants were excluded from the analysis if $`\documentclass[12pt]{minimal}
                    \usepackage{amsmath}
                    \usepackage{wasysym} 
                    \usepackage{amsfonts} 
                    \usepackage{amssymb} 
                    \usepackage{amsbsy}
                    \usepackage{mathrsfs}
                    \usepackage{upgreek}
                    \setlength{\oddsidemargin}{-69pt}
                    \begin{document}$$\partial VAS_{55555}^{rescaed} /\partial VAS_{55555}$$\end{document}`$ exceeded a given threshold, i.e. if changing the rating of 55555 by 1 on the 100–0 scale implied a change of more than the threshold on the full health = 1, dead = 0 scale. Analyses were run with thresholds of 0.1, 0.075 and 0.05.

Table <a href="#Tab10" data-ref-type="table">10</a> gives the mean VAS responses for the various exclusion criteria. Tables <a href="#Tab11" data-ref-type="table">11</a>, <a href="#Tab12" data-ref-type="table">12</a>, <a href="#Tab13" data-ref-type="table">13</a> and <a href="#Tab14" data-ref-type="table">14</a> give the COVID-19-related coefficients for all robustness analyses. Full results including control variables are available upon request to the corresponding author.

See below Appendix D Tables <a href="#Tab10" data-ref-type="table">10</a>, <a href="#Tab11" data-ref-type="table">11</a>, <a href="#Tab12" data-ref-type="table">12</a>, <a href="#Tab13" data-ref-type="table">13</a> and <a href="#Tab14" data-ref-type="table">14</a> here.

<div id="Tab10" class="table-wrap">

<div class="caption">

Mean VAS responses with different exclusion criteria

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Exclusion criteria</th>
<th style="text-align: left;">Threshold</th>
<th style="text-align: left;">11111</th>
<th style="text-align: left;">Dead</th>
<th style="text-align: left;">55555</th>
<th style="text-align: left;">55555 rescaled</th>
<th style="text-align: left;"><em>N</em></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6" style="text-align: left;">Low rescaled 55555</td>
<td style="text-align: left;"> – 1</td>
<td>90.5</td>
<td style="text-align: left;">6.17</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">0.122</td>
<td style="text-align: left;">2450</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.9, 116)</td>
<td style="text-align: left;">( – 21.8, 34.1)</td>
<td style="text-align: left;">( – 20.3, 55.1)</td>
<td style="text-align: left;">( – 0.439, 0.684)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> – 1.5</td>
<td>90.5</td>
<td style="text-align: left;">7.11</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">0.0973</td>
<td style="text-align: left;">2499</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(65.0, 116)</td>
<td style="text-align: left;">( – 23.6, 37.9)</td>
<td style="text-align: left;">( – 20.4, 55.1)</td>
<td style="text-align: left;">( – 0.559, 0.753)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> – 2</td>
<td>90.5</td>
<td style="text-align: left;">7.73</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">0.0762</td>
<td style="text-align: left;">2528</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(65.0, 116)</td>
<td style="text-align: left;">( – 24.9, 40.4)</td>
<td style="text-align: left;">( – 20.4, 55.1)</td>
<td style="text-align: left;">( – 0.681, 0.834)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Censoring rescaled 55555</td>
<td style="text-align: left;"> – 1</td>
<td>90.4</td>
<td style="text-align: left;">9.6</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;">2599</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.7, 116)</td>
<td style="text-align: left;">( – 29.7, 48.9)</td>
<td style="text-align: left;">( – 20.4, 55.3)</td>
<td style="text-align: left;">( – 0.689, 0.805)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> – 1.5</td>
<td>90.4</td>
<td style="text-align: left;">9.6</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;">2599</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.7, 116)</td>
<td style="text-align: left;">( – 29.7, 48.9)</td>
<td style="text-align: left;">( – 20.4, 55.3)</td>
<td style="text-align: left;">( – 0.689, 0.805)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> – 2</td>
<td>90.4</td>
<td style="text-align: left;">9.6</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;">2599</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.7, 116)</td>
<td style="text-align: left;">( – 29.7, 48.9)</td>
<td style="text-align: left;">( – 20.4, 55.3)</td>
<td style="text-align: left;">( – 0.689, 0.805)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Impact on mean rescaled 55555</td>
<td style="text-align: left;">1.5</td>
<td>90.3</td>
<td style="text-align: left;">9.2</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;"> – 0.0752</td>
<td style="text-align: left;">2587</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.6, 116)</td>
<td style="text-align: left;">( – 28.4, 46.9)</td>
<td style="text-align: left;">( – 20.3, 55.2)</td>
<td style="text-align: left;">( – 3.02, 2.87)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td>90.3</td>
<td style="text-align: left;">9.27</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;"> – 0.105</td>
<td style="text-align: left;">2589</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.6, 116)</td>
<td style="text-align: left;">( – 28.7, 47.2)</td>
<td style="text-align: left;">( – 20.3, 55.2)</td>
<td style="text-align: left;">( – 3.71, 3.50)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">2.5</td>
<td>90.3</td>
<td style="text-align: left;">9.3</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;"> – 0.125</td>
<td style="text-align: left;">2590</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.6, 116)</td>
<td style="text-align: left;">( – 28.8, 47.4)</td>
<td style="text-align: left;">( – 20.3, 55.2)</td>
<td style="text-align: left;">( – 4.25, 4.00)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">High VAS for dead</td>
<td style="text-align: left;">75</td>
<td>90.3</td>
<td style="text-align: left;">8.02</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">0.025</td>
<td style="text-align: left;">2547</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.4, 116)</td>
<td style="text-align: left;">( – 25.0, 41.1)</td>
<td style="text-align: left;">( – 19.7, 53.9)</td>
<td style="text-align: left;">( – 1.50, 1.55)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">50</td>
<td>90.3</td>
<td style="text-align: left;">5.14</td>
<td style="text-align: left;">16.2</td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;">2412</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.3, 116)</td>
<td style="text-align: left;">( – 18.1, 28.4)</td>
<td style="text-align: left;">( – 18.5, 50.8)</td>
<td style="text-align: left;">( – 1.05, 1.24)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">25</td>
<td>90.7</td>
<td style="text-align: left;">1.79</td>
<td style="text-align: left;">15.4</td>
<td style="text-align: left;">0.148</td>
<td style="text-align: left;">2198</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(64.8, 117)</td>
<td style="text-align: left;">( – 7.25, 10.8)</td>
<td style="text-align: left;">( – 17.7, 48.5)</td>
<td style="text-align: left;">( – 0.907, 1.20)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">High rate of change of rescaled 55555</td>
<td style="text-align: left;">0.1</td>
<td>90.8</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">0.0337</td>
<td style="text-align: left;">2539</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(66.9, 115)</td>
<td style="text-align: left;">( – 26.0, 42.4)</td>
<td style="text-align: left;">( – 19.8, 53.9)</td>
<td style="text-align: left;">( – 1.09, 1.16)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">0.075</td>
<td>90.9</td>
<td style="text-align: left;">7.84</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">0.052</td>
<td style="text-align: left;">2520</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(67.8, 114)</td>
<td style="text-align: left;">( – 25.3, 41.0)</td>
<td style="text-align: left;">( – 19.9, 53.8)</td>
<td style="text-align: left;">( – 0.906, 1.01)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">0.05</td>
<td>91.2</td>
<td style="text-align: left;">7.26</td>
<td style="text-align: left;">16.9</td>
<td style="text-align: left;">0.0748</td>
<td style="text-align: left;">2490</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td>(68.8, 113)</td>
<td style="text-align: left;">( – 23.9, 38.5)</td>
<td style="text-align: left;">( – 19.9, 53.7)</td>
<td style="text-align: left;">( – 0.723, 0.873)</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

*Note.* 95% confidence intervals in parentheses

</div>

<div id="Tab11" class="table-wrap">

<div class="caption">

Rescaled 55555 robustness tests for Tobit regressions

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Low rescaled 55555</th>
<th colspan="3" style="text-align: left;">Censoring rescaled 55555</th>
<th colspan="3" style="text-align: left;">Impact on mean rescaled 55555</th>
<th colspan="3" style="text-align: left;">High VAS for dead</th>
<th colspan="3" style="text-align: left;">Rescaled 55555 high rate of change</th>
</tr>
<tr>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2.5</th>
<th style="text-align: left;">75</th>
<th style="text-align: left;">50</th>
<th style="text-align: left;">25</th>
<th style="text-align: left;">0.1</th>
<th style="text-align: left;">0.075</th>
<th style="text-align: left;">0.05</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">11111</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;"> – 0.0136</td>
<td style="text-align: left;"> – .0126</td>
<td style="text-align: left;"> – 0.0137</td>
<td style="text-align: left;"> – 0.013</td>
<td style="text-align: left;"> – 0.013</td>
<td style="text-align: left;"> – 0.013</td>
<td style="text-align: left;"> – 0.0147</td>
<td style="text-align: left;"> – 0.0147</td>
<td style="text-align: left;"> – 0.0147</td>
<td style="text-align: left;"> – 0.0158</td>
<td style="text-align: left;"> – 0.0166</td>
<td style="text-align: left;"> – 0.0168</td>
<td style="text-align: left;"> – 0.0198</td>
<td style="text-align: left;"> – 0.0138</td>
<td style="text-align: left;"> – 0.0126</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0166)</td>
<td style="text-align: left;">(0.0163)</td>
<td style="text-align: left;">(0.0162)</td>
<td style="text-align: left;">(0.0161)</td>
<td style="text-align: left;">(0.0161)</td>
<td style="text-align: left;">(0.0161)</td>
<td style="text-align: left;">(0.0162)</td>
<td style="text-align: left;">(0.0162)</td>
<td style="text-align: left;">(0.0161)</td>
<td style="text-align: left;">(0.0163)</td>
<td style="text-align: left;">(0.0169)</td>
<td style="text-align: left;">(0.0175)</td>
<td style="text-align: left;">(0.0153)</td>
<td style="text-align: left;">(0.0151)</td>
<td style="text-align: left;">(0.0148)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;">0.116</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.128</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.136</td>
<td style="text-align: left;">0.131</td>
<td style="text-align: left;">0.129</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: left;">0.113</td>
<td style="text-align: left;">0.105</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0732)</td>
<td style="text-align: left;">(0.0719)</td>
<td style="text-align: left;">(0.0715)</td>
<td style="text-align: left;">(0.0712)</td>
<td style="text-align: left;">(0.0712)</td>
<td style="text-align: left;">(0.0712)</td>
<td style="text-align: left;">(0.0714)</td>
<td style="text-align: left;">(0.0714)</td>
<td style="text-align: left;">(0.0714)</td>
<td style="text-align: left;">(0.0721)</td>
<td style="text-align: left;">(0.0749)</td>
<td style="text-align: left;">(0.0773)</td>
<td style="text-align: left;">(0.0675)</td>
<td style="text-align: left;">(0.0667)</td>
<td style="text-align: left;">(0.0651)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;"> – 0.0152</td>
<td style="text-align: left;"> – 0.108</td>
<td style="text-align: left;">0.0671</td>
<td style="text-align: left;">0.0331</td>
<td style="text-align: left;">0.0331</td>
<td style="text-align: left;">0.0331</td>
<td style="text-align: left;">0.0691</td>
<td style="text-align: left;">0.0633</td>
<td style="text-align: left;">0.0619</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;"> – 0.24</td>
<td style="text-align: left;"> – 0.102</td>
<td style="text-align: left;"> – 0.0553</td>
<td style="text-align: left;"> – 0.221</td>
<td style="text-align: left;"> – 0.2</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.867)</td>
<td style="text-align: left;">(0.85)</td>
<td style="text-align: left;">(0.834)</td>
<td style="text-align: left;">(0.823)</td>
<td style="text-align: left;">(0.823)</td>
<td style="text-align: left;">(0.823)</td>
<td style="text-align: left;">(0.824)</td>
<td style="text-align: left;">(0.824)</td>
<td style="text-align: left;">(0.823)</td>
<td style="text-align: left;">(0.842)</td>
<td style="text-align: left;">(0.883)</td>
<td style="text-align: left;">(0.951)</td>
<td style="text-align: left;">(0.789)</td>
<td style="text-align: left;">(0.782)</td>
<td style="text-align: left;">(0.769)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;"> – 0.224</td>
<td style="text-align: left;"> – 0.474</td>
<td style="text-align: left;"> – 0.429</td>
<td style="text-align: left;"> – 0.847</td>
<td style="text-align: left;"> – 0.847</td>
<td style="text-align: left;"> – 0.847</td>
<td style="text-align: left;"> – 0.921</td>
<td style="text-align: left;"> – 0.892</td>
<td style="text-align: left;"> – 0.892</td>
<td style="text-align: left;"> – 0.714</td>
<td style="text-align: left;"> – 0.448</td>
<td style="text-align: left;"> – 0.516</td>
<td style="text-align: left;"> – 0.846</td>
<td style="text-align: left;"> – 1.03</td>
<td style="text-align: left;"> – 1.04</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.922)</td>
<td style="text-align: left;">(0.908)</td>
<td style="text-align: left;">(0.888)</td>
<td style="text-align: left;">(0.862)</td>
<td style="text-align: left;">(0.862)</td>
<td style="text-align: left;">(0.862)</td>
<td style="text-align: left;">(0.865)</td>
<td style="text-align: left;">(0.864)</td>
<td style="text-align: left;">(0.864)</td>
<td style="text-align: left;">(0.889)</td>
<td style="text-align: left;">(0.949)</td>
<td style="text-align: left;">(1.04)</td>
<td style="text-align: left;">(0.844)</td>
<td style="text-align: left;">(0.836)</td>
<td style="text-align: left;">(0.823)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Worry x risk</td>
<td style="text-align: left;">0.132</td>
<td style="text-align: left;">0.205</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">0.206</td>
<td style="text-align: left;">0.206</td>
<td style="text-align: left;">0.206</td>
<td style="text-align: left;">0.223</td>
<td style="text-align: left;">0.215</td>
<td style="text-align: left;">0.215</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">0.214</td>
<td style="text-align: left;">0.177</td>
<td style="text-align: left;">0.206*</td>
<td style="text-align: left;">0.273</td>
<td style="text-align: left;">0.227</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.375)</td>
<td style="text-align: left;">(0.369)</td>
<td style="text-align: left;">(0.36)</td>
<td style="text-align: left;">(0.351)</td>
<td style="text-align: left;">(0.351)</td>
<td style="text-align: left;">(0.351)</td>
<td style="text-align: left;">(0.352)</td>
<td style="text-align: left;">(0.352)</td>
<td style="text-align: left;">(0.352)</td>
<td style="text-align: left;">(0.362)</td>
<td style="text-align: left;">(0.384)</td>
<td style="text-align: left;">(0.413)</td>
<td style="text-align: left;">(0.341)</td>
<td style="text-align: left;">(0.337)</td>
<td style="text-align: left;">(0.332)</td>
</tr>
<tr>
<td style="text-align: left;">Dead</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;"> – 8.97 × 10–4</td>
<td style="text-align: left;">-3.4 × 10–3</td>
<td style="text-align: left;"> – 3.07 × 10–4</td>
<td style="text-align: left;">0.0399</td>
<td style="text-align: left;">0.0399</td>
<td style="text-align: left;">0.0399</td>
<td style="text-align: left;">0.0239</td>
<td style="text-align: left;">0.0217</td>
<td style="text-align: left;">0.0235</td>
<td style="text-align: left;">8.77 × 10–3</td>
<td style="text-align: left;">0.0144</td>
<td style="text-align: left;">5.62 × 10–3</td>
<td style="text-align: left;">0.0208</td>
<td style="text-align: left;">0.0137</td>
<td style="text-align: left;">5.1 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0334)</td>
<td style="text-align: left;">(0.035)</td>
<td style="text-align: left;">(0.0367)</td>
<td style="text-align: left;">(0.0417)</td>
<td style="text-align: left;">(0.0417)</td>
<td style="text-align: left;">(0.0417)</td>
<td style="text-align: left;">(0.0401)</td>
<td style="text-align: left;">(0.0404)</td>
<td style="text-align: left;">(0.0405)</td>
<td style="text-align: left;">(0.0366)</td>
<td style="text-align: left;">(0.0292)</td>
<td style="text-align: left;">(0.0144)</td>
<td style="text-align: left;">(0.0381)</td>
<td style="text-align: left;">(0.0376)</td>
<td style="text-align: left;">(0.0363)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;"> – 0.0556</td>
<td style="text-align: left;"> – 0.0417</td>
<td style="text-align: left;"> – 0.051</td>
<td style="text-align: left;"> – 0.248</td>
<td style="text-align: left;"> – 0.248</td>
<td style="text-align: left;"> – 0.248</td>
<td style="text-align: left;"> – 0.159</td>
<td style="text-align: left;"> – 0.155</td>
<td style="text-align: left;"> – 0.162</td>
<td style="text-align: left;"> – 0.0889</td>
<td style="text-align: left;"> – 0.117</td>
<td style="text-align: left;"> – 0.0223</td>
<td style="text-align: left;"> – 0.147</td>
<td style="text-align: left;"> – 0.116</td>
<td style="text-align: left;"> – 0.0777</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.147)</td>
<td style="text-align: left;">(0.154)</td>
<td style="text-align: left;">(0.162)</td>
<td style="text-align: left;">(0.184)</td>
<td style="text-align: left;">(0.184)</td>
<td style="text-align: left;">(0.184)</td>
<td style="text-align: left;">(0.177)</td>
<td style="text-align: left;">(0.178)</td>
<td style="text-align: left;">(0.179)</td>
<td style="text-align: left;">(0.161)</td>
<td style="text-align: left;">(0.129)</td>
<td style="text-align: left;">(0.0634)</td>
<td style="text-align: left;">(0.168)</td>
<td style="text-align: left;">(0.166)</td>
<td style="text-align: left;">(0.16)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;"> – 0.693</td>
<td style="text-align: left;">1.24</td>
<td style="text-align: left;">0.247</td>
<td style="text-align: left;">0.101</td>
<td style="text-align: left;">0.101</td>
<td style="text-align: left;">0.101</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.513</td>
<td style="text-align: left;">0.348</td>
<td style="text-align: left;"> – 0.311</td>
<td style="text-align: left;"> – 0.542</td>
<td style="text-align: left;"> – 0.211</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.915</td>
<td style="text-align: left;">0.57</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.74)</td>
<td style="text-align: left;">(1.82)</td>
<td style="text-align: left;">(1.88)</td>
<td style="text-align: left;">(2.12)</td>
<td style="text-align: left;">(2.12)</td>
<td style="text-align: left;">(2.12)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.04)</td>
<td style="text-align: left;">(2.05)</td>
<td style="text-align: left;">(1.87)</td>
<td style="text-align: left;">(1.52)</td>
<td style="text-align: left;">(0.768)</td>
<td style="text-align: left;">(1.95)</td>
<td style="text-align: left;">(1.92)</td>
<td style="text-align: left;">(1.87)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;">4.65*</td>
<td style="text-align: left;">6.03*</td>
<td style="text-align: left;">5.73*</td>
<td style="text-align: left;">7.71*</td>
<td style="text-align: left;">7.71*</td>
<td style="text-align: left;">7.71*</td>
<td style="text-align: left;">6.72*</td>
<td style="text-align: left;">7.17*</td>
<td style="text-align: left;">7.17*</td>
<td style="text-align: left;">5.25*</td>
<td style="text-align: left;">3.09</td>
<td style="text-align: left;">0.567</td>
<td style="text-align: left;">4.8*</td>
<td style="text-align: left;">5.07*</td>
<td style="text-align: left;">4.93*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.79)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.96)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.08)</td>
<td style="text-align: left;">(2.09)</td>
<td style="text-align: left;">(2.1)</td>
<td style="text-align: left;">(1.93)</td>
<td style="text-align: left;">(1.58)</td>
<td style="text-align: left;">(0.825)</td>
<td style="text-align: left;">(2.05)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(1.96)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Worry x risk</td>
<td style="text-align: left;"> – 1.44</td>
<td style="text-align: left;"> – 1.97*</td>
<td style="text-align: left;"> – 1.57</td>
<td style="text-align: left;"> – 2.12*</td>
<td style="text-align: left;"> – 2.12*</td>
<td style="text-align: left;"> – 2.12*</td>
<td style="text-align: left;"> – 1.91*</td>
<td style="text-align: left;"> – 2.06*</td>
<td style="text-align: left;"> – 1.97*</td>
<td style="text-align: left;"> – 1.48</td>
<td style="text-align: left;"> – 1.29</td>
<td style="text-align: left;">-0.192</td>
<td style="text-align: left;">-1.54</td>
<td style="text-align: left;">-1.73*</td>
<td style="text-align: left;">-1.52</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.751)</td>
<td style="text-align: left;">(0.79)</td>
<td style="text-align: left;">(0.807)</td>
<td style="text-align: left;">(0.9)</td>
<td style="text-align: left;">(0.9)</td>
<td style="text-align: left;">(0.9)</td>
<td style="text-align: left;">(0.862)</td>
<td style="text-align: left;">(0.869)</td>
<td style="text-align: left;">(0.871)</td>
<td style="text-align: left;">(0.802)</td>
<td style="text-align: left;">(0.662)</td>
<td style="text-align: left;">(0.334)</td>
<td style="text-align: left;">(0.84)</td>
<td style="text-align: left;">(0.829)</td>
<td style="text-align: left;">(0.805)</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;">6.05 × 10–3</td>
<td style="text-align: left;">5.09 × 10–3</td>
<td style="text-align: left;">2.38 × 10–3</td>
<td style="text-align: left;">5.85 × 10–3</td>
<td style="text-align: left;">5.85 × 10–3</td>
<td style="text-align: left;">5.85 × 10–3</td>
<td style="text-align: left;">7.74 × 10–3</td>
<td style="text-align: left;">8.29 × 10–3</td>
<td style="text-align: left;">8.39 × 10–3</td>
<td style="text-align: left;">4.49 × 10–3</td>
<td style="text-align: left;">5.65 × 10–3</td>
<td style="text-align: left;">2.52 × 10–3</td>
<td style="text-align: left;">7.5 × 10–3</td>
<td style="text-align: left;">5.33 × 10–3</td>
<td style="text-align: left;">7.29 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0208)</td>
<td style="text-align: left;">(0.0207)</td>
<td style="text-align: left;">(0.0206)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0201)</td>
<td style="text-align: left;">(0.0196)</td>
<td style="text-align: left;">(0.0197)</td>
<td style="text-align: left;">(0.0201)</td>
<td style="text-align: left;">(0.0203)</td>
<td style="text-align: left;">(0.0204)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;"> – 0.0451</td>
<td style="text-align: left;"> – 0.0401</td>
<td style="text-align: left;"> – 0.0284</td>
<td style="text-align: left;"> – 0.0431</td>
<td style="text-align: left;"> – 0.0431</td>
<td style="text-align: left;"> – 0.0431</td>
<td style="text-align: left;"> – 0.0479</td>
<td style="text-align: left;"> – 0.0496</td>
<td style="text-align: left;">-5 × 10–2</td>
<td style="text-align: left;">-0.0281</td>
<td style="text-align: left;">-0.0277</td>
<td style="text-align: left;">-0.0165</td>
<td style="text-align: left;">-0.0444</td>
<td style="text-align: left;">-0.036</td>
<td style="text-align: left;">-0.0444</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0919)</td>
<td style="text-align: left;">(0.0912)</td>
<td style="text-align: left;">(0.091)</td>
<td style="text-align: left;">(0.0897)</td>
<td style="text-align: left;">(0.0897)</td>
<td style="text-align: left;">(0.0897)</td>
<td style="text-align: left;">(0.0898)</td>
<td style="text-align: left;">(0.0898)</td>
<td style="text-align: left;">(0.0898)</td>
<td style="text-align: left;">(0.0888)</td>
<td style="text-align: left;">(0.0869)</td>
<td style="text-align: left;">(0.0869)</td>
<td style="text-align: left;">(0.0889)</td>
<td style="text-align: left;">(0.0894)</td>
<td style="text-align: left;">(0.0901)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;"> – 0.585</td>
<td style="text-align: left;"> – 0.758</td>
<td style="text-align: left;"> – 0.729</td>
<td style="text-align: left;"> – 0.827</td>
<td style="text-align: left;"> – 0.827</td>
<td style="text-align: left;"> – 0.827</td>
<td style="text-align: left;"> – 0.844</td>
<td style="text-align: left;"> – 0.853</td>
<td style="text-align: left;"> – 0.863</td>
<td style="text-align: left;"> – 0.843</td>
<td style="text-align: left;"> – 0.714</td>
<td style="text-align: left;">-0.934</td>
<td style="text-align: left;">-0.736</td>
<td style="text-align: left;">-0.642</td>
<td style="text-align: left;">-0.596</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.08)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.06)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.02)</td>
<td style="text-align: left;">(1.06)</td>
<td style="text-align: left;">(1.03)</td>
<td style="text-align: left;">(1.04)</td>
<td style="text-align: left;">(1.06)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;">2.2</td>
<td style="text-align: left;">2.04</td>
<td style="text-align: left;">2.11</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">2.04</td>
<td style="text-align: left;">1.95</td>
<td style="text-align: left;">1.95</td>
<td style="text-align: left;">1.76</td>
<td style="text-align: left;">1.03</td>
<td style="text-align: left;">1.23</td>
<td style="text-align: left;">1.67</td>
<td style="text-align: left;">1.74</td>
<td style="text-align: left;">1.72</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.14)</td>
<td style="text-align: left;">(1.14)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.08)</td>
<td style="text-align: left;">(1.09)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.1)</td>
<td style="text-align: left;">(1.11)</td>
<td style="text-align: left;">(1.12)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Worry x risk</td>
<td style="text-align: left;"> – 0.171</td>
<td style="text-align: left;"> – 0.0963</td>
<td style="text-align: left;"> – 0.0855</td>
<td style="text-align: left;"> – .0427</td>
<td style="text-align: left;"> – 0.0427</td>
<td style="text-align: left;"> – 0.0427</td>
<td style="text-align: left;"> – 0.0774</td>
<td style="text-align: left;"> – 0.0502</td>
<td style="text-align: left;"> – 0.0448</td>
<td style="text-align: left;"> – 0.0345</td>
<td style="text-align: left;">0.0536</td>
<td style="text-align: left;">0.0614</td>
<td style="text-align: left;">-0.0151</td>
<td style="text-align: left;">-0.0411</td>
<td style="text-align: left;">-0.0714</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.467)</td>
<td style="text-align: left;">(0.464)</td>
<td style="text-align: left;">(0.454)</td>
<td style="text-align: left;">(0.438)</td>
<td style="text-align: left;">(0.438)</td>
<td style="text-align: left;">(0.438)</td>
<td style="text-align: left;">(0.439)</td>
<td style="text-align: left;">(0.438)</td>
<td style="text-align: left;">(0.438)</td>
<td style="text-align: left;">(0.442)</td>
<td style="text-align: left;">(0.441)</td>
<td style="text-align: left;">(0.459)</td>
<td style="text-align: left;">(0.445)</td>
<td style="text-align: left;">(0.447)</td>
<td style="text-align: left;">(0.454)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">55555 rescaled</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;">2.48 × 10–4</td>
<td style="text-align: left;">2.51 × 10–4*</td>
<td style="text-align: left;">1.78 × 10–4</td>
<td style="text-align: left;">-1.25 × 10–4*</td>
<td style="text-align: left;"> – 1.25 × 10–4*</td>
<td style="text-align: left;"> – 1.25 × 10–4*</td>
<td style="text-align: left;"> – 1.85 × 10–3*</td>
<td style="text-align: left;"> – 1.35 × 10–3*</td>
<td style="text-align: left;"> – 1.87 × 10–3*</td>
<td style="text-align: left;"> – 1.66 × 10–4</td>
<td style="text-align: left;">5.49 × 10–5</td>
<td style="text-align: left;">2.5 × 10–4</td>
<td style="text-align: left;">-2.37 × 10–4</td>
<td style="text-align: left;">-1.64 × 10–4</td>
<td style="text-align: left;">2.44 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.69 × 10–4)</td>
<td style="text-align: left;">(3.12 × 10–4)</td>
<td style="text-align: left;">(3.65 × 10–4)</td>
<td style="text-align: left;">(3.72 × 10–4)</td>
<td style="text-align: left;">(3.72 × 10–4)</td>
<td style="text-align: left;">(3.72 × 10–4)</td>
<td style="text-align: left;">(1.39 × 10–3)</td>
<td style="text-align: left;">(1.78 × 10–3)</td>
<td style="text-align: left;">(2.08 × 10–3)</td>
<td style="text-align: left;">(7.67 × 10–4)</td>
<td style="text-align: left;">(5.9 × 10–4)</td>
<td style="text-align: left;">(5.74 × 10–4)</td>
<td style="text-align: left;">(5.26 × 10–4)</td>
<td style="text-align: left;">(4.69 × 10–4)</td>
<td style="text-align: left;">(3.84 × 10–4)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;"> – 8.67 × 10–4</td>
<td style="text-align: left;"> – 9.04 × 10–4</td>
<td style="text-align: left;"> – 6.4 × 10–4</td>
<td style="text-align: left;">9.33 × 10–4</td>
<td style="text-align: left;">9.33 × 10–4</td>
<td style="text-align: left;">9.33 × 10–4</td>
<td style="text-align: left;">8.35 × 10–3</td>
<td style="text-align: left;">7.68 × 10–3</td>
<td style="text-align: left;">9.61 × 10–3</td>
<td style="text-align: left;">2.44 × 10–3</td>
<td style="text-align: left;">1.11 × 10–3</td>
<td style="text-align: left;">-3.26 × 10–5</td>
<td style="text-align: left;">1.59 × 10–3</td>
<td style="text-align: left;">1.26 × 10–3</td>
<td style="text-align: left;">-5.3 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.19 × 10–3)</td>
<td style="text-align: left;">(1.38 × 10–3)</td>
<td style="text-align: left;">(1.61 × 10–3)</td>
<td style="text-align: left;">(1.65 × 10–3)</td>
<td style="text-align: left;">(1.65 × 10–3)</td>
<td style="text-align: left;">(1.65 × 10–3)</td>
<td style="text-align: left;">(6.13 × 10–3)</td>
<td style="text-align: left;">(7.86 × 10–3)</td>
<td style="text-align: left;">(9.19 × 10–3)</td>
<td style="text-align: left;">(3.39 × 10–3)</td>
<td style="text-align: left;">(2.62 × 10–3)</td>
<td style="text-align: left;">(2.53 × 10–3)</td>
<td style="text-align: left;">(2.32 × 10–3)</td>
<td style="text-align: left;">(2.07 × 10–3)</td>
<td style="text-align: left;">(1.69 × 10–3)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;">9.51 × 10–4</td>
<td style="text-align: left;"> – 0.0266</td>
<td style="text-align: left;"> – 9.39 × 10–3</td>
<td style="text-align: left;"> – 0.0158</td>
<td style="text-align: left;"> – 0.0158</td>
<td style="text-align: left;"> – 0.0158</td>
<td style="text-align: left;"> – 0.126</td>
<td style="text-align: left;"> – 0.128</td>
<td style="text-align: left;"> – 0.0714</td>
<td style="text-align: left;">0.0104</td>
<td style="text-align: left;">0.0164</td>
<td style="text-align: left;">9.01 × 10–3</td>
<td style="text-align: left;">-0.0173</td>
<td style="text-align: left;">-0.0212</td>
<td style="text-align: left;">-4.21 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.014)</td>
<td style="text-align: left;">(0.0162)</td>
<td style="text-align: left;">(0.0188)</td>
<td style="text-align: left;">(0.0189)</td>
<td style="text-align: left;">(0.0189)</td>
<td style="text-align: left;">(0.0189)</td>
<td style="text-align: left;">(0.0705)</td>
<td style="text-align: left;">(0.0906)</td>
<td style="text-align: left;">(0.106)</td>
<td style="text-align: left;">(0.0395)</td>
<td style="text-align: left;">(0.0307)</td>
<td style="text-align: left;">(0.0309)</td>
<td style="text-align: left;">(0.027)</td>
<td style="text-align: left;">(0.0241)</td>
<td style="text-align: left;">(0.0198)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;"> – 0.0138</td>
<td style="text-align: left;"> – 0.0363*</td>
<td style="text-align: left;"> – 0.0328</td>
<td style="text-align: left;"> – 0.0578*</td>
<td style="text-align: left;"> – 0.0578*</td>
<td style="text-align: left;"> – 0.0578*</td>
<td style="text-align: left;"> – 0.174*</td>
<td style="text-align: left;"> – 0.29*</td>
<td style="text-align: left;"> – 0.289*</td>
<td style="text-align: left;"> – 0.0733</td>
<td style="text-align: left;"> – 1.94 × 10–3</td>
<td style="text-align: left;">0.0346</td>
<td style="text-align: left;">-0.028</td>
<td style="text-align: left;">-0.0301*</td>
<td style="text-align: left;">-0.023</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0149)</td>
<td style="text-align: left;">(0.0173)</td>
<td style="text-align: left;">(0.0199)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0739)</td>
<td style="text-align: left;">(0.0944)</td>
<td style="text-align: left;">(0.11)</td>
<td style="text-align: left;">(0.0415)</td>
<td style="text-align: left;">(0.0328)</td>
<td style="text-align: left;">(0.0335)</td>
<td style="text-align: left;">(0.0288)</td>
<td style="text-align: left;">(0.0257)</td>
<td style="text-align: left;">(0.0212)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Worry x risk</td>
<td style="text-align: left;">8.83 × 10–3</td>
<td style="text-align: left;">0.0171*</td>
<td style="text-align: left;">0.0114</td>
<td style="text-align: left;">0.0193*</td>
<td style="text-align: left;">0.0193*</td>
<td style="text-align: left;">0.0193*</td>
<td style="text-align: left;">0.0652*</td>
<td style="text-align: left;">0.101*</td>
<td style="text-align: left;">0.0695</td>
<td style="text-align: left;">0.0104</td>
<td style="text-align: left;"> – 3.56 × 10–3</td>
<td style="text-align: left;">-0.016</td>
<td style="text-align: left;">0.0133</td>
<td style="text-align: left;">0.0176</td>
<td style="text-align: left;">8.34 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(6.07 × 10–3)</td>
<td style="text-align: left;">(7.04 × 10–3)</td>
<td style="text-align: left;">(8.08 × 10–3)</td>
<td style="text-align: left;">(8.08 × 10–3)</td>
<td style="text-align: left;">(8.08 × 10–3)</td>
<td style="text-align: left;">(8.08 × 10–3)</td>
<td style="text-align: left;">(0.0302)</td>
<td style="text-align: left;">(0.0387)</td>
<td style="text-align: left;">(0.0451)</td>
<td style="text-align: left;">(0.017)</td>
<td style="text-align: left;">(0.0133)</td>
<td style="text-align: left;">(0.0134)</td>
<td style="text-align: left;">(0.0117)</td>
<td style="text-align: left;">(0.0104)</td>
<td style="text-align: left;">(8.57 × 10–3)</td>
</tr>
</tbody>
</table>

*Note.* Standard errors in parentheses. \*significant at 5% level

</div>

<div id="Tab12" class="table-wrap">

<div class="caption">

Rescaled 55555 robustness tests for Tobit regression results including whether COVID-19 affected health or quality of life

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Low rescaled 55555</th>
<th colspan="3" style="text-align: left;">Censoring rescaled 55555</th>
<th colspan="3" style="text-align: left;">Impact on mean rescaled 55555</th>
<th colspan="3" style="text-align: left;">High VAS for dead</th>
<th colspan="3" style="text-align: left;">Rescaled 55555 high rate of change</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;">1.5</th>
<th style="text-align: left;">2</th>
<th style="text-align: left;">2.5</th>
<th style="text-align: left;">75</th>
<th style="text-align: left;">50</th>
<th style="text-align: left;">25</th>
<th style="text-align: left;">0.1</th>
<th style="text-align: left;">0.075</th>
<th style="text-align: left;">0.05</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">11111</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;"> – 7.59 × 10–3</td>
<td style="text-align: left;"> – 7.8 × 10–3</td>
<td style="text-align: left;"> – 9.16 × 10–3</td>
<td style="text-align: left;"> – 8.01 × 10–3</td>
<td style="text-align: left;"> – 8.01 × 10–3</td>
<td style="text-align: left;"> – 8.01 × 10–3</td>
<td style="text-align: left;"> – 8.87 × 10–3</td>
<td style="text-align: left;"> – 8.87 × 10–3</td>
<td style="text-align: left;"> – 8.82 × 10–3</td>
<td style="text-align: left;"> – 8.81 × 10–3</td>
<td style="text-align: left;">-0.0122</td>
<td style="text-align: left;">-9.54 × 10–3</td>
<td style="text-align: left;">-0.0114</td>
<td style="text-align: left;">-6.38 × 10–3</td>
<td style="text-align: left;">-7.44 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0201)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0197)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(0.0198)</td>
<td style="text-align: left;">(2 × 10–2)</td>
<td style="text-align: left;">(0.0206)</td>
<td style="text-align: left;">(0.0212)</td>
<td style="text-align: left;">(0.019)</td>
<td style="text-align: left;">(0.0189)</td>
<td style="text-align: left;">(0.0183)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">0.105</td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.126</td>
<td style="text-align: left;">0.126</td>
<td style="text-align: left;">0.126</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.132</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;">0.0989</td>
<td style="text-align: left;">0.092</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0958)</td>
<td style="text-align: left;">(0.0943)</td>
<td style="text-align: left;">(0.094)</td>
<td style="text-align: left;">(0.0946)</td>
<td style="text-align: left;">(0.0946)</td>
<td style="text-align: left;">(0.0946)</td>
<td style="text-align: left;">(0.0947)</td>
<td style="text-align: left;">(0.0947)</td>
<td style="text-align: left;">(0.0946)</td>
<td style="text-align: left;">(0.0956)</td>
<td style="text-align: left;">(0.0986)</td>
<td style="text-align: left;">(0.101)</td>
<td style="text-align: left;">(0.0905)</td>
<td style="text-align: left;">(0.0902)</td>
<td style="text-align: left;">(0.0873)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;">1.38</td>
<td style="text-align: left;">1.12</td>
<td style="text-align: left;">1.32</td>
<td style="text-align: left;">1.37</td>
<td style="text-align: left;">1.37</td>
<td style="text-align: left;">1.37</td>
<td style="text-align: left;">1.43</td>
<td style="text-align: left;">1.43</td>
<td style="text-align: left;">1.42</td>
<td style="text-align: left;">1.41</td>
<td style="text-align: left;">1.17</td>
<td style="text-align: left;">1.83</td>
<td style="text-align: left;">0.635</td>
<td style="text-align: left;">0.203</td>
<td style="text-align: left;">0.248</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.16)</td>
<td style="text-align: left;">(1.13)</td>
<td style="text-align: left;">(1.11)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.12)</td>
<td style="text-align: left;">(1.13)</td>
<td style="text-align: left;">(1.19)</td>
<td style="text-align: left;">(1.26)</td>
<td style="text-align: left;">(1.09)</td>
<td style="text-align: left;">(1.09)</td>
<td style="text-align: left;">(1.05)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;">0.227</td>
<td style="text-align: left;">0.296</td>
<td style="text-align: left;">0.0996</td>
<td style="text-align: left;">0.0996</td>
<td style="text-align: left;">0.0996</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.133</td>
<td style="text-align: left;">0.129</td>
<td style="text-align: left;">0.324</td>
<td style="text-align: left;">-0.525</td>
<td style="text-align: left;">-0.875</td>
<td style="text-align: left;">-0.612</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.2)</td>
<td style="text-align: left;">(1.18)</td>
<td style="text-align: left;">(1.16)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.16)</td>
<td style="text-align: left;">(1.16)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.17)</td>
<td style="text-align: left;">(1.24)</td>
<td style="text-align: left;">(1.34)</td>
<td style="text-align: left;">(1.13)</td>
<td style="text-align: left;">(1.14)</td>
<td style="text-align: left;">(1.1)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry x risk</td>
<td style="text-align: left;"> – 0.209</td>
<td style="text-align: left;"> – 0.105</td>
<td style="text-align: left;"> – 0.19</td>
<td style="text-align: left;"> – 0.223</td>
<td style="text-align: left;"> – 0.223</td>
<td style="text-align: left;"> – 0.223</td>
<td style="text-align: left;"> – 0.229</td>
<td style="text-align: left;"> – 0.229</td>
<td style="text-align: left;">-0.226</td>
<td style="text-align: left;">-0.225</td>
<td style="text-align: left;">-0.146</td>
<td style="text-align: left;">-0.333</td>
<td style="text-align: left;">0.0427</td>
<td style="text-align: left;">0.182</td>
<td style="text-align: left;">0.0717</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.495)</td>
<td style="text-align: left;">(0.486)</td>
<td style="text-align: left;">(0.474)</td>
<td style="text-align: left;">(0.473)</td>
<td style="text-align: left;">(0.473)</td>
<td style="text-align: left;">(0.473)</td>
<td style="text-align: left;">(0.474)</td>
<td style="text-align: left;">(0.474)</td>
<td style="text-align: left;">(0.473)</td>
<td style="text-align: left;">(0.478)</td>
<td style="text-align: left;">(0.509)</td>
<td style="text-align: left;">(0.542)</td>
<td style="text-align: left;">(0.461)</td>
<td style="text-align: left;">(0.461)</td>
<td style="text-align: left;">(0.446)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health negative</td>
<td style="text-align: left;">0.409</td>
<td style="text-align: left;">0.204</td>
<td style="text-align: left;"> – 5.81 × 10–3</td>
<td style="text-align: left;"> – 0.154</td>
<td style="text-align: left;"> – 0.154</td>
<td style="text-align: left;"> – 0.154</td>
<td style="text-align: left;"> – 0.165</td>
<td style="text-align: left;"> – 0.165</td>
<td style="text-align: left;"> – 0.154</td>
<td style="text-align: left;"> – 0.0624</td>
<td style="text-align: left;"> – 0.133</td>
<td style="text-align: left;">0.686</td>
<td style="text-align: left;">-0.0867</td>
<td style="text-align: left;">-0.119</td>
<td style="text-align: left;">0.0975</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.55)</td>
<td style="text-align: left;">(1.52)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.52)</td>
<td style="text-align: left;">(1.58)</td>
<td style="text-align: left;">(1.64)</td>
<td style="text-align: left;">(1.44)</td>
<td style="text-align: left;">(1.43)</td>
<td style="text-align: left;">(1.39)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health positive</td>
<td style="text-align: left;">2.31</td>
<td style="text-align: left;">1.77</td>
<td style="text-align: left;">1.83</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: left;">1.41</td>
<td style="text-align: left;">1.41</td>
<td style="text-align: left;">1.41</td>
<td style="text-align: left;">1.84</td>
<td style="text-align: left;">2.91</td>
<td style="text-align: left;">2.4</td>
<td style="text-align: left;">1.57</td>
<td style="text-align: left;">1.63</td>
<td style="text-align: left;">1.74</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.69)</td>
<td style="text-align: left;">(2.6)</td>
<td style="text-align: left;">(2.58)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.62)</td>
<td style="text-align: left;">(2.88)</td>
<td style="text-align: left;">(3.13)</td>
<td style="text-align: left;">(2.47)</td>
<td style="text-align: left;">(2.48)</td>
<td style="text-align: left;">(2.43)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL negative</td>
<td style="text-align: left;">0.552</td>
<td style="text-align: left;">0.697</td>
<td style="text-align: left;">0.601</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">0.344</td>
<td style="text-align: left;">0.344</td>
<td style="text-align: left;">0.346</td>
<td style="text-align: left;">0.348</td>
<td style="text-align: left;">0.363</td>
<td style="text-align: left;">-0.246</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.0583</td>
<td style="text-align: left;">0.14</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.17)</td>
<td style="text-align: left;">(1.16)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.15)</td>
<td style="text-align: left;">(1.17)</td>
<td style="text-align: left;">(1.2)</td>
<td style="text-align: left;">(1.23)</td>
<td style="text-align: left;">(1.1)</td>
<td style="text-align: left;">(1.1)</td>
<td style="text-align: left;">(1.06)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL positive</td>
<td style="text-align: left;"> – 3.21</td>
<td style="text-align: left;"> – 3.35</td>
<td style="text-align: left;"> – 3.41</td>
<td style="text-align: left;"> – 3.54</td>
<td style="text-align: left;"> – 3.54</td>
<td style="text-align: left;"> – 3.54</td>
<td style="text-align: left;"> – 3.63</td>
<td style="text-align: left;"> – 3.63</td>
<td style="text-align: left;"> – 3.64</td>
<td style="text-align: left;"> – 3.79</td>
<td style="text-align: left;"> – 3.34</td>
<td style="text-align: left;">-4.08</td>
<td style="text-align: left;">-3.44</td>
<td style="text-align: left;">-3.61</td>
<td style="text-align: left;">-2.32</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.21)</td>
<td style="text-align: left;">(2.14)</td>
<td style="text-align: left;">(2.13)</td>
<td style="text-align: left;">(2.09)</td>
<td style="text-align: left;">(2.09)</td>
<td style="text-align: left;">(2.09)</td>
<td style="text-align: left;">(2.11)</td>
<td style="text-align: left;">(2.11)</td>
<td style="text-align: left;">(2.11)</td>
<td style="text-align: left;">(2.15)</td>
<td style="text-align: left;">(2.31)</td>
<td style="text-align: left;">(2.4)</td>
<td style="text-align: left;">(2.04)</td>
<td style="text-align: left;">(2.04)</td>
<td style="text-align: left;">(2.01)</td>
</tr>
<tr>
<td style="text-align: left;">Dead</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;"> – 7.83 × 10–3</td>
<td style="text-align: left;"> – 8.59 × 10–3</td>
<td style="text-align: left;">9.2 × 10–3</td>
<td style="text-align: left;">0.0318</td>
<td style="text-align: left;">0.0318</td>
<td style="text-align: left;">0.0318</td>
<td style="text-align: left;">0.0172</td>
<td style="text-align: left;">0.0172</td>
<td style="text-align: left;">0.0213</td>
<td style="text-align: left;">1.47 × 10–3</td>
<td style="text-align: left;">0.0264</td>
<td style="text-align: left;">-5.2 × 10–5</td>
<td style="text-align: left;">0.0278</td>
<td style="text-align: left;">4.88 × 10–3</td>
<td style="text-align: left;">1.25 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.039)</td>
<td style="text-align: left;">(0.0411)</td>
<td style="text-align: left;">(0.0431)</td>
<td style="text-align: left;">(0.0498)</td>
<td style="text-align: left;">(0.0498)</td>
<td style="text-align: left;">(0.0498)</td>
<td style="text-align: left;">(0.0473)</td>
<td style="text-align: left;">(0.0473)</td>
<td style="text-align: left;">(0.0477)</td>
<td style="text-align: left;">(0.0434)</td>
<td style="text-align: left;">(0.0342)</td>
<td style="text-align: left;">(0.0179)</td>
<td style="text-align: left;">(0.045)</td>
<td style="text-align: left;">(0.0438)</td>
<td style="text-align: left;">(0.0428)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;">0.0669</td>
<td style="text-align: left;">0.0981</td>
<td style="text-align: left;">0.0451</td>
<td style="text-align: left;"> – 0.0901</td>
<td style="text-align: left;"> – 0.0901</td>
<td style="text-align: left;"> – 0.0901</td>
<td style="text-align: left;"> – 0.0105</td>
<td style="text-align: left;"> – 0.0105</td>
<td style="text-align: left;"> – 0.0335</td>
<td style="text-align: left;">0.0845</td>
<td style="text-align: left;"> – 0.0841</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">-1.93 × 10–3</td>
<td style="text-align: left;">0.103</td>
<td style="text-align: left;">0.0944</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.187)</td>
<td style="text-align: left;">(0.197)</td>
<td style="text-align: left;">(0.207)</td>
<td style="text-align: left;">(0.239)</td>
<td style="text-align: left;">(0.239)</td>
<td style="text-align: left;">(0.239)</td>
<td style="text-align: left;">(0.227)</td>
<td style="text-align: left;">(0.227)</td>
<td style="text-align: left;">(0.229)</td>
<td style="text-align: left;">(0.208)</td>
<td style="text-align: left;">(0.165)</td>
<td style="text-align: left;">(0.0855)</td>
<td style="text-align: left;">(0.216)</td>
<td style="text-align: left;">(0.21)</td>
<td style="text-align: left;">(0.205)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;"> – 3.97</td>
<td style="text-align: left;"> – 1.3</td>
<td style="text-align: left;"> – 1.81</td>
<td style="text-align: left;"> – 2.19</td>
<td style="text-align: left;"> – 2.19</td>
<td style="text-align: left;"> – 2.19</td>
<td style="text-align: left;"> – 1.45</td>
<td style="text-align: left;"> – 1.45</td>
<td style="text-align: left;"> – 1.82</td>
<td style="text-align: left;"> – 2.17</td>
<td style="text-align: left;"> – 2.03</td>
<td style="text-align: left;">-0.128</td>
<td style="text-align: left;">-1.1</td>
<td style="text-align: left;">-0.652</td>
<td style="text-align: left;">-1.07</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.26)</td>
<td style="text-align: left;">(2.35)</td>
<td style="text-align: left;">(2.43)</td>
<td style="text-align: left;">(2.81)</td>
<td style="text-align: left;">(2.81)</td>
<td style="text-align: left;">(2.81)</td>
<td style="text-align: left;">(2.66)</td>
<td style="text-align: left;">(2.66)</td>
<td style="text-align: left;">(2.69)</td>
<td style="text-align: left;">(2.45)</td>
<td style="text-align: left;">(1.98)</td>
<td style="text-align: left;">(1.06)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.51)</td>
<td style="text-align: left;">(2.45)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;">2.02</td>
<td style="text-align: left;">2.95</td>
<td style="text-align: left;">3.12</td>
<td style="text-align: left;">3.97</td>
<td style="text-align: left;">3.97</td>
<td style="text-align: left;">3.97</td>
<td style="text-align: left;">4.12</td>
<td style="text-align: left;">4.12</td>
<td style="text-align: left;">4.13</td>
<td style="text-align: left;">4.02</td>
<td style="text-align: left;">2.24</td>
<td style="text-align: left;">1.46</td>
<td style="text-align: left;">3.58</td>
<td style="text-align: left;">4.11</td>
<td style="text-align: left;">3.87</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.2)</td>
<td style="text-align: left;">(2.36)</td>
<td style="text-align: left;">(2.44)</td>
<td style="text-align: left;">(2.77)</td>
<td style="text-align: left;">(2.77)</td>
<td style="text-align: left;">(2.77)</td>
<td style="text-align: left;">(2.64)</td>
<td style="text-align: left;">(2.64)</td>
<td style="text-align: left;">(2.66)</td>
<td style="text-align: left;">(2.43)</td>
<td style="text-align: left;">(1.98)</td>
<td style="text-align: left;">(1.09)</td>
<td style="text-align: left;">(2.58)</td>
<td style="text-align: left;">(2.53)</td>
<td style="text-align: left;">(2.47)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry x risk</td>
<td style="text-align: left;"> – 0.454</td>
<td style="text-align: left;"> – 1.14</td>
<td style="text-align: left;"> – 0.987</td>
<td style="text-align: left;"> – 1.06</td>
<td style="text-align: left;"> – 1.06</td>
<td style="text-align: left;"> – 1.06</td>
<td style="text-align: left;"> – 1.2</td>
<td style="text-align: left;"> – 1.2</td>
<td style="text-align: left;"> – 1.03</td>
<td style="text-align: left;"> – 0.95</td>
<td style="text-align: left;"> – 0.939</td>
<td style="text-align: left;">-0.555</td>
<td style="text-align: left;">-1.08</td>
<td style="text-align: left;">-1.25</td>
<td style="text-align: left;">-1.07</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.945)</td>
<td style="text-align: left;">(0.995)</td>
<td style="text-align: left;">(1.02)</td>
<td style="text-align: left;">(1.17)</td>
<td style="text-align: left;">(1.17)</td>
<td style="text-align: left;">(1.17)</td>
<td style="text-align: left;">(1.11)</td>
<td style="text-align: left;">(1.11)</td>
<td style="text-align: left;">(1.11)</td>
<td style="text-align: left;">(1.02)</td>
<td style="text-align: left;">(0.842)</td>
<td style="text-align: left;">(0.454)</td>
<td style="text-align: left;">(1.07)</td>
<td style="text-align: left;">(1.05)</td>
<td style="text-align: left;">(1.02)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health negative</td>
<td style="text-align: left;">2.53</td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">3.26</td>
<td style="text-align: left;">4.67</td>
<td style="text-align: left;">4.67</td>
<td style="text-align: left;">4.67</td>
<td style="text-align: left;">3.67</td>
<td style="text-align: left;">3.67</td>
<td style="text-align: left;">4.42</td>
<td style="text-align: left;">3.26</td>
<td style="text-align: left;">2.16</td>
<td style="text-align: left;">0.977</td>
<td style="text-align: left;">3.92</td>
<td style="text-align: left;">2.21</td>
<td style="text-align: left;">1.95</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.97)</td>
<td style="text-align: left;">(3.12)</td>
<td style="text-align: left;">(3.25)</td>
<td style="text-align: left;">(3.71)</td>
<td style="text-align: left;">(3.71)</td>
<td style="text-align: left;">(3.71)</td>
<td style="text-align: left;">(3.52)</td>
<td style="text-align: left;">(3.52)</td>
<td style="text-align: left;">(3.54)</td>
<td style="text-align: left;">(3.25)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(1.35)</td>
<td style="text-align: left;">(3.36)</td>
<td style="text-align: left;">(3.29)</td>
<td style="text-align: left;">(3.22)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health positive</td>
<td style="text-align: left;">14.9*</td>
<td style="text-align: left;">16.5*</td>
<td style="text-align: left;">15*</td>
<td style="text-align: left;">14.8*</td>
<td style="text-align: left;">14.8*</td>
<td style="text-align: left;">14.8*</td>
<td style="text-align: left;">15.4*</td>
<td style="text-align: left;">15.4*</td>
<td style="text-align: left;">15.3*</td>
<td style="text-align: left;">14.7*</td>
<td style="text-align: left;">8.37</td>
<td style="text-align: left;">-0.586</td>
<td style="text-align: left;">15.2*</td>
<td style="text-align: left;">13.6*</td>
<td style="text-align: left;">13.7*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(4.69)</td>
<td style="text-align: left;">(4.85)</td>
<td style="text-align: left;">(5.12)</td>
<td style="text-align: left;">(5.84)</td>
<td style="text-align: left;">(5.84)</td>
<td style="text-align: left;">(5.84)</td>
<td style="text-align: left;">(5.52)</td>
<td style="text-align: left;">(5.52)</td>
<td style="text-align: left;">(5.58)</td>
<td style="text-align: left;">(5.14)</td>
<td style="text-align: left;">(4.39)</td>
<td style="text-align: left;">(2.52)</td>
<td style="text-align: left;">(5.31)</td>
<td style="text-align: left;">(5.21)</td>
<td style="text-align: left;">(5.15)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL negative</td>
<td style="text-align: left;"> – 1.27</td>
<td style="text-align: left;"> – 2.97</td>
<td style="text-align: left;"> – 3.37</td>
<td style="text-align: left;"> – 2.96</td>
<td style="text-align: left;"> – 2.96</td>
<td style="text-align: left;"> – 2.96</td>
<td style="text-align: left;"> – 2.21</td>
<td style="text-align: left;"> – 2.21</td>
<td style="text-align: left;">-2.12</td>
<td style="text-align: left;">-2.46</td>
<td style="text-align: left;">-0.484</td>
<td style="text-align: left;">-0.115</td>
<td style="text-align: left;">-2.44</td>
<td style="text-align: left;">-2.21</td>
<td style="text-align: left;">-2.02</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.31)</td>
<td style="text-align: left;">(2.44)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.94)</td>
<td style="text-align: left;">(2.94)</td>
<td style="text-align: left;">(2.94)</td>
<td style="text-align: left;">(2.79)</td>
<td style="text-align: left;">(2.79)</td>
<td style="text-align: left;">(2.82)</td>
<td style="text-align: left;">(2.57)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(1.05)</td>
<td style="text-align: left;">(2.66)</td>
<td style="text-align: left;">(2.58)</td>
<td style="text-align: left;">(2.51)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL positive</td>
<td style="text-align: left;">4.34</td>
<td style="text-align: left;">5.57</td>
<td style="text-align: left;">5.29</td>
<td style="text-align: left;">8.5</td>
<td style="text-align: left;">8.5</td>
<td style="text-align: left;">8.5</td>
<td style="text-align: left;">7.51</td>
<td style="text-align: left;">7.51</td>
<td style="text-align: left;">7.39</td>
<td style="text-align: left;">6.08</td>
<td style="text-align: left;">1.53</td>
<td style="text-align: left;">1.83</td>
<td style="text-align: left;">5.85</td>
<td style="text-align: left;">5.72</td>
<td style="text-align: left;">3.52</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(4.13)</td>
<td style="text-align: left;">(4.24)</td>
<td style="text-align: left;">(4.44)</td>
<td style="text-align: left;">(5)</td>
<td style="text-align: left;">(5)</td>
<td style="text-align: left;">(5)</td>
<td style="text-align: left;">(4.78)</td>
<td style="text-align: left;">(4.78)</td>
<td style="text-align: left;">(4.83)</td>
<td style="text-align: left;">(4.44)</td>
<td style="text-align: left;">(3.78)</td>
<td style="text-align: left;">(1.96)</td>
<td style="text-align: left;">(4.63)</td>
<td style="text-align: left;">(4.51)</td>
<td style="text-align: left;">(4.5)</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;">5.61 × 10–3</td>
<td style="text-align: left;">3.46 × 10–3</td>
<td style="text-align: left;">3.67 × 10–4</td>
<td style="text-align: left;">-4.29 × 10–4</td>
<td style="text-align: left;">-4.29 × 10–4</td>
<td style="text-align: left;">-4.29 × 10–4</td>
<td style="text-align: left;">1.01 × 10–3</td>
<td style="text-align: left;">1.01 × 10–3</td>
<td style="text-align: left;">1.14 × 10–3</td>
<td style="text-align: left;">-8.3 × 10–4</td>
<td style="text-align: left;">6.36 × 10–3</td>
<td style="text-align: left;">2.65 × 10–3</td>
<td style="text-align: left;">3.73 × 10–3</td>
<td style="text-align: left;">-6.62 × 10–4</td>
<td style="text-align: left;">4.81 × 10–5</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0256)</td>
<td style="text-align: left;">(0.0253)</td>
<td style="text-align: left;">(0.0253)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.025)</td>
<td style="text-align: left;">(0.0249)</td>
<td style="text-align: left;">(0.0245)</td>
<td style="text-align: left;">(0.0247)</td>
<td style="text-align: left;">(0.0249)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;"> – 0.0604</td>
<td style="text-align: left;"> – 0.0588</td>
<td style="text-align: left;"> – 0.0451</td>
<td style="text-align: left;"> – 0.0342</td>
<td style="text-align: left;"> – 0.0342</td>
<td style="text-align: left;"> – 0.0342</td>
<td style="text-align: left;"> – 0.0409</td>
<td style="text-align: left;"> – 0.0409</td>
<td style="text-align: left;">-0.0417</td>
<td style="text-align: left;">-0.0246</td>
<td style="text-align: left;">-0.063</td>
<td style="text-align: left;">-0.0224</td>
<td style="text-align: left;">-0.0446</td>
<td style="text-align: left;">-0.0242</td>
<td style="text-align: left;">-0.0318</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.122)</td>
<td style="text-align: left;">(0.121)</td>
<td style="text-align: left;">(0.121)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.119)</td>
<td style="text-align: left;">(0.118)</td>
<td style="text-align: left;">(0.118)</td>
<td style="text-align: left;">(0.119)</td>
<td style="text-align: left;">(0.12)</td>
<td style="text-align: left;">(0.12)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;"> – 1.01</td>
<td style="text-align: left;"> – 1.29</td>
<td style="text-align: left;"> – 1.56</td>
<td style="text-align: left;"> – 1.57</td>
<td style="text-align: left;"> – 1.57</td>
<td style="text-align: left;"> – 1.57</td>
<td style="text-align: left;"> – 1.61</td>
<td style="text-align: left;"> – 1.61</td>
<td style="text-align: left;">-1.62</td>
<td style="text-align: left;">-1.73</td>
<td style="text-align: left;">-1.04</td>
<td style="text-align: left;">-0.0528</td>
<td style="text-align: left;">-1.56</td>
<td style="text-align: left;">-1.47</td>
<td style="text-align: left;">-1.44</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.45)</td>
<td style="text-align: left;">(1.43)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.41)</td>
<td style="text-align: left;">(1.41)</td>
<td style="text-align: left;">(1.41)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.43)</td>
<td style="text-align: left;">(1.43)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;">1.04</td>
<td style="text-align: left;">0.863</td>
<td style="text-align: left;">0.668</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">0.485</td>
<td style="text-align: left;">0.485</td>
<td style="text-align: left;">0.484</td>
<td style="text-align: left;">0.485</td>
<td style="text-align: left;">0.624</td>
<td style="text-align: left;">2.39</td>
<td style="text-align: left;">0.599</td>
<td style="text-align: left;">0.634</td>
<td style="text-align: left;">0.645</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.51)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.45)</td>
<td style="text-align: left;">(1.45)</td>
<td style="text-align: left;">(1.45)</td>
<td style="text-align: left;">(1.44)</td>
<td style="text-align: left;">(1.44)</td>
<td style="text-align: left;">(1.44)</td>
<td style="text-align: left;">(1.44)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.54)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.49)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry x risk</td>
<td style="text-align: left;"> – 0.177</td>
<td style="text-align: left;"> – 0.0605</td>
<td style="text-align: left;">0.0371</td>
<td style="text-align: left;">0.0805</td>
<td style="text-align: left;">0.0805</td>
<td style="text-align: left;">0.0805</td>
<td style="text-align: left;">0.0776</td>
<td style="text-align: left;">0.0776</td>
<td style="text-align: left;">0.0849</td>
<td style="text-align: left;">0.145</td>
<td style="text-align: left;">-0.0821</td>
<td style="text-align: left;">-0.693</td>
<td style="text-align: left;">0.0834</td>
<td style="text-align: left;">0.0698</td>
<td style="text-align: left;">0.0426</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.629)</td>
<td style="text-align: left;">(0.62)</td>
<td style="text-align: left;">(0.606)</td>
<td style="text-align: left;">(0.596)</td>
<td style="text-align: left;">(0.596)</td>
<td style="text-align: left;">(0.596)</td>
<td style="text-align: left;">(0.596)</td>
<td style="text-align: left;">(0.596)</td>
<td style="text-align: left;">(0.596)</td>
<td style="text-align: left;">(0.593)</td>
<td style="text-align: left;">(0.604)</td>
<td style="text-align: left;">(0.628)</td>
<td style="text-align: left;">(0.603)</td>
<td style="text-align: left;">(0.607)</td>
<td style="text-align: left;">(0.608)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health negative</td>
<td style="text-align: left;">4.56*</td>
<td style="text-align: left;">4.52*</td>
<td style="text-align: left;">4.47*</td>
<td style="text-align: left;">4.74*</td>
<td style="text-align: left;">4.74*</td>
<td style="text-align: left;">4.74*</td>
<td style="text-align: left;">4.73*</td>
<td style="text-align: left;">4.73*</td>
<td style="text-align: left;">4.76*</td>
<td style="text-align: left;">4.54*</td>
<td style="text-align: left;">4.84*</td>
<td style="text-align: left;">5.15*</td>
<td style="text-align: left;">4.69*</td>
<td style="text-align: left;">4.37*</td>
<td style="text-align: left;">4.51*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.97)</td>
<td style="text-align: left;">(1.95)</td>
<td style="text-align: left;">(1.93)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.88)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.91)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health positive</td>
<td style="text-align: left;">6.34</td>
<td style="text-align: left;">5.93</td>
<td style="text-align: left;">6.28</td>
<td style="text-align: left;">6.18*</td>
<td style="text-align: left;">6.18*</td>
<td style="text-align: left;">6.18*</td>
<td style="text-align: left;">6.09</td>
<td style="text-align: left;">6.09</td>
<td style="text-align: left;">6.08</td>
<td style="text-align: left;">6.47*</td>
<td style="text-align: left;">3.34</td>
<td style="text-align: left;">0.589</td>
<td style="text-align: left;">5.75</td>
<td style="text-align: left;">6.35*</td>
<td style="text-align: left;">5.67</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.32)</td>
<td style="text-align: left;">(3.24)</td>
<td style="text-align: left;">(3.23)</td>
<td style="text-align: left;">(3.15)</td>
<td style="text-align: left;">(3.15)</td>
<td style="text-align: left;">(3.15)</td>
<td style="text-align: left;">(3.16)</td>
<td style="text-align: left;">(3.16)</td>
<td style="text-align: left;">(3.15)</td>
<td style="text-align: left;">(3.18)</td>
<td style="text-align: left;">(3.33)</td>
<td style="text-align: left;">(3.54)</td>
<td style="text-align: left;">(3.17)</td>
<td style="text-align: left;">(3.2)</td>
<td style="text-align: left;">(3.24)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL negative</td>
<td style="text-align: left;"> – 1.69</td>
<td style="text-align: left;"> – 1.53</td>
<td style="text-align: left;"> – 1.27</td>
<td style="text-align: left;"> – 0.993</td>
<td style="text-align: left;"> – 0.993</td>
<td style="text-align: left;"> – 0.993</td>
<td style="text-align: left;"> – 1.12</td>
<td style="text-align: left;"> – 1.12</td>
<td style="text-align: left;">-1.12</td>
<td style="text-align: left;">-1.02</td>
<td style="text-align: left;">-1.18</td>
<td style="text-align: left;">-0.925</td>
<td style="text-align: left;">-1.05</td>
<td style="text-align: left;">-0.905</td>
<td style="text-align: left;">-0.94</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.45)</td>
<td style="text-align: left;">(1.43)</td>
<td style="text-align: left;">(1.44)</td>
<td style="text-align: left;">(1.45)</td>
<td style="text-align: left;">(1.46)</td>
<td style="text-align: left;">(1.46)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL positive</td>
<td style="text-align: left;">1.17</td>
<td style="text-align: left;">0.841</td>
<td style="text-align: left;">0.942</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">0.898</td>
<td style="text-align: left;">0.898</td>
<td style="text-align: left;">0.892</td>
<td style="text-align: left;">0.403</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">2.06</td>
<td style="text-align: left;">0.883</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">0.151</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.81)</td>
<td style="text-align: left;">(2.74)</td>
<td style="text-align: left;">(2.72)</td>
<td style="text-align: left;">(2.64)</td>
<td style="text-align: left;">(2.64)</td>
<td style="text-align: left;">(2.64)</td>
<td style="text-align: left;">(2.66)</td>
<td style="text-align: left;">(2.66)</td>
<td style="text-align: left;">(2.65)</td>
<td style="text-align: left;">(2.67)</td>
<td style="text-align: left;">(2.74)</td>
<td style="text-align: left;">(2.78)</td>
<td style="text-align: left;">(2.67)</td>
<td style="text-align: left;">(2.69)</td>
<td style="text-align: left;">(2.74)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">55555 rescaled</td>
<td style="text-align: left;">Cases</td>
<td style="text-align: left;">4.46 × 10–5</td>
<td style="text-align: left;">1.02 × 10–5</td>
<td style="text-align: left;"> – 3.27 × 10–4</td>
<td style="text-align: left;"> – 3.77 × 10–4</td>
<td style="text-align: left;"> – 3.77 × 10–4</td>
<td style="text-align: left;"> – 3.77 × 10–4</td>
<td style="text-align: left;"> – 1.31 × 10–3</td>
<td style="text-align: left;"> – 1.31 × 10–3</td>
<td style="text-align: left;">-2.37 × 10–3</td>
<td style="text-align: left;">-1.4 × 10–4</td>
<td style="text-align: left;">-3.83 × 10–4</td>
<td style="text-align: left;">1.34 × 10–4</td>
<td style="text-align: left;">-7.13 × 10–4</td>
<td style="text-align: left;">-2.08 × 10–4</td>
<td style="text-align: left;">5.66 × 10–6</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.31 × 10–4)</td>
<td style="text-align: left;">(3.76 × 10–4)</td>
<td style="text-align: left;">(4.34 × 10–4)</td>
<td style="text-align: left;">(4.43 × 10–4)</td>
<td style="text-align: left;">(4.43 × 10–4)</td>
<td style="text-align: left;">(4.43 × 10–4)</td>
<td style="text-align: left;">(1.62 × 10–3)</td>
<td style="text-align: left;">(1.62 × 10–3)</td>
<td style="text-align: left;">(2.51 × 10–3)</td>
<td style="text-align: left;">(1.08 × 10–3)</td>
<td style="text-align: left;">(9.43 × 10–4)</td>
<td style="text-align: left;">(9.81 × 10–4)</td>
<td style="text-align: left;">(6.13 × 10–4)</td>
<td style="text-align: left;">(5.22 × 10–4)</td>
<td style="text-align: left;">(4.56 × 10–4)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Deaths</td>
<td style="text-align: left;"> – 9.83 × 10–4</td>
<td style="text-align: left;"> – 1.3 × 10–3</td>
<td style="text-align: left;"> – 2.34 × 10–4</td>
<td style="text-align: left;">7 × 10–4</td>
<td style="text-align: left;">7 × 10–4</td>
<td style="text-align: left;">7 × 10–4</td>
<td style="text-align: left;">1 × 10–2</td>
<td style="text-align: left;">1 × 10–2</td>
<td style="text-align: left;">0.0166</td>
<td style="text-align: left;">4.01 × 10–3</td>
<td style="text-align: left;">4.1 × 10–3</td>
<td style="text-align: left;">2.8 × 10–3</td>
<td style="text-align: left;">1.42 × 10–3</td>
<td style="text-align: left;">-8.74 × 10–4</td>
<td style="text-align: left;">-1.14 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.58 × 10–3)</td>
<td style="text-align: left;">(1.79 × 10–3)</td>
<td style="text-align: left;">(2.07 × 10–3)</td>
<td style="text-align: left;">(2.12 × 10–3)</td>
<td style="text-align: left;">(2.12 × 10–3)</td>
<td style="text-align: left;">(2.12 × 10–3)</td>
<td style="text-align: left;">(7.74 × 10–3)</td>
<td style="text-align: left;">(7.74 × 10–3)</td>
<td style="text-align: left;">(0.012)</td>
<td style="text-align: left;">(5.15 × 10–3)</td>
<td style="text-align: left;">(4.53 × 10–3)</td>
<td style="text-align: left;">(4.68 × 10–3)</td>
<td style="text-align: left;">(2.93 × 10–3)</td>
<td style="text-align: left;">(2.49 × 10–3)</td>
<td style="text-align: left;">(2.18 × 10–3)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry</td>
<td style="text-align: left;">0.0122</td>
<td style="text-align: left;"> – 0.0255</td>
<td style="text-align: left;"> – 0.022</td>
<td style="text-align: left;"> – 0.0198</td>
<td style="text-align: left;"> – 0.0198</td>
<td style="text-align: left;"> – 0.0198</td>
<td style="text-align: left;"> – 0.0437</td>
<td style="text-align: left;"> – 0.0437</td>
<td style="text-align: left;">0.0836</td>
<td style="text-align: left;">-0.0225</td>
<td style="text-align: left;">0.0262</td>
<td style="text-align: left;">0.0318</td>
<td style="text-align: left;">-0.0321</td>
<td style="text-align: left;">-0.0323</td>
<td style="text-align: left;">-0.0189</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0193)</td>
<td style="text-align: left;">(0.0216)</td>
<td style="text-align: left;">(0.0246)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0921)</td>
<td style="text-align: left;">(0.0921)</td>
<td style="text-align: left;">(0.143)</td>
<td style="text-align: left;">(0.0611)</td>
<td style="text-align: left;">(0.0546)</td>
<td style="text-align: left;">(0.0583)</td>
<td style="text-align: left;">(0.0351)</td>
<td style="text-align: left;">(0.0299)</td>
<td style="text-align: left;">(0.0261)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Risk</td>
<td style="text-align: left;"> – 0.0167</td>
<td style="text-align: left;"> – 0.0332</td>
<td style="text-align: left;"> – 0.0428</td>
<td style="text-align: left;"> – 0.0543</td>
<td style="text-align: left;"> – 0.0543</td>
<td style="text-align: left;"> – 0.0543</td>
<td style="text-align: left;"> – 0.173</td>
<td style="text-align: left;"> – 0.173</td>
<td style="text-align: left;">-0.169</td>
<td style="text-align: left;">-0.124</td>
<td style="text-align: left;">0.0209</td>
<td style="text-align: left;">0.0688</td>
<td style="text-align: left;">-0.041</td>
<td style="text-align: left;">-0.0538</td>
<td style="text-align: left;">-0.0491</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0197)</td>
<td style="text-align: left;">(0.0224)</td>
<td style="text-align: left;">(0.0255)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0941)</td>
<td style="text-align: left;">(0.0941)</td>
<td style="text-align: left;">(0.146)</td>
<td style="text-align: left;">(0.0628)</td>
<td style="text-align: left;">(0.0568)</td>
<td style="text-align: left;">(0.0617)</td>
<td style="text-align: left;">(0.0365)</td>
<td style="text-align: left;">(0.0312)</td>
<td style="text-align: left;">(0.0272)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Worry × risk</td>
<td style="text-align: left;">4.42 × 10–3</td>
<td style="text-align: left;">0.0151</td>
<td style="text-align: left;">0.0155</td>
<td style="text-align: left;">0.0167</td>
<td style="text-align: left;">0.0167</td>
<td style="text-align: left;">0.0167</td>
<td style="text-align: left;">0.0377</td>
<td style="text-align: left;">0.0377</td>
<td style="text-align: left;">-0.0249</td>
<td style="text-align: left;">0.0222</td>
<td style="text-align: left;">-0.0217</td>
<td style="text-align: left;">-0.0401</td>
<td style="text-align: left;">0.0151</td>
<td style="text-align: left;">0.0186</td>
<td style="text-align: left;">0.0136</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(8.19 × 10–3)</td>
<td style="text-align: left;">(9.26 × 10–3)</td>
<td style="text-align: left;">(0.0105)</td>
<td style="text-align: left;">(0.0106)</td>
<td style="text-align: left;">(0.0106)</td>
<td style="text-align: left;">(0.0106)</td>
<td style="text-align: left;">(0.0388)</td>
<td style="text-align: left;">(0.0388)</td>
<td style="text-align: left;">(6 × 10–2)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0234)</td>
<td style="text-align: left;">(0.0251)</td>
<td style="text-align: left;">(0.0149)</td>
<td style="text-align: left;">(0.0127)</td>
<td style="text-align: left;">(0.0111)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health negative</td>
<td style="text-align: left;">0.0435</td>
<td style="text-align: left;">0.0295</td>
<td style="text-align: left;">0.0222</td>
<td style="text-align: left;">0.0168</td>
<td style="text-align: left;">0.0168</td>
<td style="text-align: left;">0.0168</td>
<td style="text-align: left;">0.0571</td>
<td style="text-align: left;">0.0571</td>
<td style="text-align: left;">-0.205</td>
<td style="text-align: left;">0.0587</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">-7.03 × 10–3</td>
<td style="text-align: left;">0.0405</td>
<td style="text-align: left;">0.0519</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0257)</td>
<td style="text-align: left;">(0.0291)</td>
<td style="text-align: left;">(0.0334)</td>
<td style="text-align: left;">(0.0337)</td>
<td style="text-align: left;">(0.0337)</td>
<td style="text-align: left;">(0.0337)</td>
<td style="text-align: left;">(0.124)</td>
<td style="text-align: left;">(0.124)</td>
<td style="text-align: left;">(0.19)</td>
<td style="text-align: left;">(0.0824)</td>
<td style="text-align: left;">(0.073)</td>
<td style="text-align: left;">(0.0764)</td>
<td style="text-align: left;">(0.0468)</td>
<td style="text-align: left;">(0.0399)</td>
<td style="text-align: left;">(0.035)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 health positive</td>
<td style="text-align: left;"> – 0.0377</td>
<td style="text-align: left;"> – 0.0704</td>
<td style="text-align: left;"> – 0.0303</td>
<td style="text-align: left;"> – 0.0336</td>
<td style="text-align: left;"> – 0.0336</td>
<td style="text-align: left;"> – 0.0336</td>
<td style="text-align: left;"> – 0.118</td>
<td style="text-align: left;"> – 0.118</td>
<td style="text-align: left;">-0.0876</td>
<td style="text-align: left;">-0.0494</td>
<td style="text-align: left;">-8.31 × 10–3</td>
<td style="text-align: left;">0.0209</td>
<td style="text-align: left;">-0.0983</td>
<td style="text-align: left;">0.0178</td>
<td style="text-align: left;">-9.32 × 10–4</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0437)</td>
<td style="text-align: left;">(0.0488)</td>
<td style="text-align: left;">(0.0563)</td>
<td style="text-align: left;">(0.0566)</td>
<td style="text-align: left;">(0.0566)</td>
<td style="text-align: left;">(0.0566)</td>
<td style="text-align: left;">(0.206)</td>
<td style="text-align: left;">(0.206)</td>
<td style="text-align: left;">(0.319)</td>
<td style="text-align: left;">(0.139)</td>
<td style="text-align: left;">(0.13)</td>
<td style="text-align: left;">(0.142)</td>
<td style="text-align: left;">(0.0789)</td>
<td style="text-align: left;">(0.0677)</td>
<td style="text-align: left;">(0.0597)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL negative</td>
<td style="text-align: left;"> – 0.0269</td>
<td style="text-align: left;"> – 2.36 × 10–3</td>
<td style="text-align: left;">2.59 × 10–3</td>
<td style="text-align: left;"> – 9.71 × 10–3</td>
<td style="text-align: left;"> – 9.71 × 10–3</td>
<td style="text-align: left;"> – 9.71 × 10–3</td>
<td style="text-align: left;"> – 0.0557</td>
<td style="text-align: left;"> – 0.0557</td>
<td style="text-align: left;">-0.0943</td>
<td style="text-align: left;">-0.0598</td>
<td style="text-align: left;">-0.074</td>
<td style="text-align: left;">-0.0786</td>
<td style="text-align: left;">-0.012</td>
<td style="text-align: left;">-4.52 × 10–3</td>
<td style="text-align: left;">-0.0111</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0193)</td>
<td style="text-align: left;">(0.022)</td>
<td style="text-align: left;">(0.0253)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0258)</td>
<td style="text-align: left;">(0.0943)</td>
<td style="text-align: left;">(0.0943)</td>
<td style="text-align: left;">(0.146)</td>
<td style="text-align: left;">(0.0627)</td>
<td style="text-align: left;">(0.055)</td>
<td style="text-align: left;">(0.057)</td>
<td style="text-align: left;">(0.0357)</td>
<td style="text-align: left;">(0.0303)</td>
<td style="text-align: left;">(0.0264)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">C19 QOL positive</td>
<td style="text-align: left;">2.38 × 10–3</td>
<td style="text-align: left;"> – 0.0314</td>
<td style="text-align: left;"> – 0.0313</td>
<td style="text-align: left;"> – 0.0763</td>
<td style="text-align: left;"> – 0.0763</td>
<td style="text-align: left;"> – -0.0763</td>
<td style="text-align: left;"> – 0.157</td>
<td style="text-align: left;"> – 0.157</td>
<td style="text-align: left;">-0.104</td>
<td style="text-align: left;">-0.176</td>
<td style="text-align: left;">0.0507</td>
<td style="text-align: left;">0.0713</td>
<td style="text-align: left;">-0.0326</td>
<td style="text-align: left;">-0.077</td>
<td style="text-align: left;">-0.0268</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0366)</td>
<td style="text-align: left;">(0.0409)</td>
<td style="text-align: left;">(0.047)</td>
<td style="text-align: left;">(0.0471)</td>
<td style="text-align: left;">(0.0471)</td>
<td style="text-align: left;">(0.0471)</td>
<td style="text-align: left;">(0.172)</td>
<td style="text-align: left;">(0.172)</td>
<td style="text-align: left;">(0.267)</td>
<td style="text-align: left;">(0.116)</td>
<td style="text-align: left;">(0.106)</td>
<td style="text-align: left;">(0.112)</td>
<td style="text-align: left;">(0.0661)</td>
<td style="text-align: left;">(0.0564)</td>
<td style="text-align: left;">(5 × 10–2)</td>
</tr>
</tbody>
</table>

*Note.* Standard errors in parentheses; \* = significant at 5% level

</div>

<div id="Tab13" class="table-wrap">

<div class="caption">

Rescaled 55555 robustness tests for Tobit regression results including frequency of leaving the house for shopping

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Low rescaled 55555</th>
<th colspan="3" style="text-align: left;">Censoring rescaled 55555</th>
<th colspan="3" style="text-align: left;">Impact on mean rescaled 55555</th>
<th colspan="3" style="text-align: left;">High VAS for dead</th>
<th colspan="3" style="text-align: left;">Rescaled 55555 high rate of change</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;">1.5</th>
<th style="text-align: left;">2</th>
<th style="text-align: left;">2.5</th>
<th style="text-align: left;">75</th>
<th style="text-align: left;">50</th>
<th style="text-align: left;">25</th>
<th style="text-align: left;">0.1</th>
<th style="text-align: left;">0.075</th>
<th style="text-align: left;">0.05</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">11111</td>
<td rowspan="2" style="text-align: left;">Shopping &lt; weekly</td>
<td style="text-align: left;"> – 1.48</td>
<td style="text-align: left;"> – 1.5</td>
<td style="text-align: left;"> – 1.38</td>
<td style="text-align: left;"> – 1.56</td>
<td style="text-align: left;"> – 1.56</td>
<td style="text-align: left;"> – 1.56</td>
<td style="text-align: left;"> – 1.54</td>
<td style="text-align: left;"> – 1.54</td>
<td style="text-align: left;"> – 1.54</td>
<td style="text-align: left;"> – 1.55</td>
<td style="text-align: left;"> – 1.15</td>
<td style="text-align: left;"> – 1.53</td>
<td style="text-align: left;"> – 1.32</td>
<td style="text-align: left;"> – 1.33</td>
<td style="text-align: left;"> – 1.23</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.7)</td>
<td style="text-align: left;">(1.68)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.75)</td>
<td style="text-align: left;">(1.79)</td>
<td style="text-align: left;">(1.62)</td>
<td style="text-align: left;">(1.6)</td>
<td style="text-align: left;">(1.53)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping 2–6 times/week</td>
<td style="text-align: left;"> – 1.78</td>
<td style="text-align: left;"> – 1.95</td>
<td style="text-align: left;"> – 1.81</td>
<td style="text-align: left;"> – 1.9</td>
<td style="text-align: left;"> – 1.9</td>
<td style="text-align: left;"> – -1.9</td>
<td style="text-align: left;"> – 1.86</td>
<td style="text-align: left;"> – 1.86</td>
<td style="text-align: left;"> – 1.85</td>
<td style="text-align: left;"> – 1.84</td>
<td style="text-align: left;"> – 1.73</td>
<td style="text-align: left;"> – 1.97</td>
<td style="text-align: left;"> – 1.46</td>
<td style="text-align: left;"> – 1.61</td>
<td style="text-align: left;"> – 1.99</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.71)</td>
<td style="text-align: left;">(1.68)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.67)</td>
<td style="text-align: left;">(1.68)</td>
<td style="text-align: left;">(1.68)</td>
<td style="text-align: left;">(1.68)</td>
<td style="text-align: left;">(1.7)</td>
<td style="text-align: left;">(1.75)</td>
<td style="text-align: left;">(1.81)</td>
<td style="text-align: left;">(1.62)</td>
<td style="text-align: left;">(1.61)</td>
<td style="text-align: left;">(1.54)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping weekly</td>
<td style="text-align: left;"> – 0.59</td>
<td style="text-align: left;"> – 0.593</td>
<td style="text-align: left;"> – 0.539</td>
<td style="text-align: left;"> – 0.882</td>
<td style="text-align: left;"> – 0.882</td>
<td style="text-align: left;"> – 0.882</td>
<td style="text-align: left;"> – 0.789</td>
<td style="text-align: left;"> – 0.789</td>
<td style="text-align: left;"> – 0.79</td>
<td style="text-align: left;"> – 0.727</td>
<td style="text-align: left;"> – 0.499</td>
<td style="text-align: left;"> – 0.684</td>
<td style="text-align: left;"> – 0.792</td>
<td style="text-align: left;"> – 0.874</td>
<td style="text-align: left;"> – 0.714</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.49)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.47)</td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.48)</td>
<td style="text-align: left;">(1.49)</td>
<td style="text-align: left;">(1.54)</td>
<td style="text-align: left;">(1.57)</td>
<td style="text-align: left;">(1.42)</td>
<td style="text-align: left;">(1.4)</td>
<td style="text-align: left;">(1.35)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping daily</td>
<td style="text-align: left;"> – 5.53</td>
<td style="text-align: left;"> – 5.41</td>
<td style="text-align: left;"> – 5.28</td>
<td style="text-align: left;"> – 5.04</td>
<td style="text-align: left;"> – 5.04</td>
<td style="text-align: left;"> – 5.04</td>
<td style="text-align: left;"> – 4.95</td>
<td style="text-align: left;"> – 4.95</td>
<td style="text-align: left;"> – 4.96</td>
<td style="text-align: left;"> – 5.24</td>
<td style="text-align: left;"> – 5.13</td>
<td style="text-align: left;"> – 6.7</td>
<td style="text-align: left;"> – 5.03</td>
<td style="text-align: left;"> – 5.3</td>
<td style="text-align: left;"> – 6.05</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.76)</td>
<td style="text-align: left;">(2.7)</td>
<td style="text-align: left;">(2.69)</td>
<td style="text-align: left;">(2.68)</td>
<td style="text-align: left;">(2.68)</td>
<td style="text-align: left;">(2.68)</td>
<td style="text-align: left;">(2.68)</td>
<td style="text-align: left;">(2.68)</td>
<td style="text-align: left;">(2.68)</td>
<td style="text-align: left;">(2.73)</td>
<td style="text-align: left;">(2.81)</td>
<td style="text-align: left;">(2.95)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.45)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping &gt; daily</td>
<td style="text-align: left;"> – 0.77</td>
<td style="text-align: left;"> – 0.777</td>
<td style="text-align: left;"> – 0.525</td>
<td style="text-align: left;"> – 0.844</td>
<td style="text-align: left;"> – 0.844</td>
<td style="text-align: left;"> – 0.844</td>
<td style="text-align: left;"> – 0.685</td>
<td style="text-align: left;"> – 0.685</td>
<td style="text-align: left;"> – 0.685</td>
<td style="text-align: left;"> – 0.677</td>
<td style="text-align: left;"> – 0.642</td>
<td style="text-align: left;"> – 5.25</td>
<td style="text-align: left;"> – 0.379</td>
<td style="text-align: left;"> – 0.851</td>
<td style="text-align: left;"> – 1.22</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(7.04)</td>
<td style="text-align: left;">(6.99)</td>
<td style="text-align: left;">(6.98)</td>
<td style="text-align: left;">(7.05)</td>
<td style="text-align: left;">(7.05)</td>
<td style="text-align: left;">(7.05)</td>
<td style="text-align: left;">(7.06)</td>
<td style="text-align: left;">(7.06)</td>
<td style="text-align: left;">(7.06)</td>
<td style="text-align: left;">(7.1)</td>
<td style="text-align: left;">(7.14)</td>
<td style="text-align: left;">(8.55)</td>
<td style="text-align: left;">(6.76)</td>
<td style="text-align: left;">(6.66)</td>
<td style="text-align: left;">(6.35)</td>
</tr>
<tr>
<td style="text-align: left;">Dead</td>
<td rowspan="2" style="text-align: left;">Shopping &lt; weekly</td>
<td style="text-align: left;">0.477</td>
<td style="text-align: left;">0.302</td>
<td style="text-align: left;"> – 0.631</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1.45</td>
<td style="text-align: left;">1.45</td>
<td style="text-align: left;">1.4</td>
<td style="text-align: left;"> – 0.331</td>
<td style="text-align: left;">2.09</td>
<td style="text-align: left;">0.343</td>
<td style="text-align: left;"> – 0.221</td>
<td style="text-align: left;"> – 0.675</td>
<td style="text-align: left;"> – 1.53</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.37)</td>
<td style="text-align: left;">(3.57)</td>
<td style="text-align: left;">(3.7)</td>
<td style="text-align: left;">(4.22)</td>
<td style="text-align: left;">(4.22)</td>
<td style="text-align: left;">(4.22)</td>
<td style="text-align: left;">(4.06)</td>
<td style="text-align: left;">(4.06)</td>
<td style="text-align: left;">(4.09)</td>
<td style="text-align: left;">(3.68)</td>
<td style="text-align: left;">(2.96)</td>
<td style="text-align: left;">(1.5)</td>
<td style="text-align: left;">(3.84)</td>
<td style="text-align: left;">(3.72)</td>
<td style="text-align: left;">(3.64)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping 2–6 times/week</td>
<td style="text-align: left;">3.79</td>
<td style="text-align: left;">5.19</td>
<td style="text-align: left;">4.61</td>
<td style="text-align: left;">6.9</td>
<td style="text-align: left;">6.9</td>
<td style="text-align: left;">6.9</td>
<td style="text-align: left;">6.15</td>
<td style="text-align: left;">6.15</td>
<td style="text-align: left;">6.63</td>
<td style="text-align: left;">3.75</td>
<td style="text-align: left;">6.1*</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">5.36</td>
<td style="text-align: left;">4.54</td>
<td style="text-align: left;">4.18</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.39)</td>
<td style="text-align: left;">(3.54)</td>
<td style="text-align: left;">(3.67)</td>
<td style="text-align: left;">(4.2)</td>
<td style="text-align: left;">(4.2)</td>
<td style="text-align: left;">(4.2)</td>
<td style="text-align: left;">(4.05)</td>
<td style="text-align: left;">(4.05)</td>
<td style="text-align: left;">(4.08)</td>
<td style="text-align: left;">(3.67)</td>
<td style="text-align: left;">(2.93)</td>
<td style="text-align: left;">(1.52)</td>
<td style="text-align: left;">(3.81)</td>
<td style="text-align: left;">(3.7)</td>
<td style="text-align: left;">(3.6)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping weekly</td>
<td style="text-align: left;"> – 1.5</td>
<td style="text-align: left;"> – 1.12</td>
<td style="text-align: left;"> – 2.24</td>
<td style="text-align: left;"> – 2.92</td>
<td style="text-align: left;"> – 2.92</td>
<td style="text-align: left;"> – 2.92</td>
<td style="text-align: left;"> – 1.69</td>
<td style="text-align: left;"> – 1.69</td>
<td style="text-align: left;"> – 1.8</td>
<td style="text-align: left;"> – 2.91</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;"> – 0.791</td>
<td style="text-align: left;"> – 2.04</td>
<td style="text-align: left;"> – 1.97</td>
<td style="text-align: left;"> – 2.3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.99)</td>
<td style="text-align: left;">(3.15)</td>
<td style="text-align: left;">(3.26)</td>
<td style="text-align: left;">(3.76)</td>
<td style="text-align: left;">(3.76)</td>
<td style="text-align: left;">(3.76)</td>
<td style="text-align: left;">(3.62)</td>
<td style="text-align: left;">(3.62)</td>
<td style="text-align: left;">(3.65)</td>
<td style="text-align: left;">(3.26)</td>
<td style="text-align: left;">(2.63)</td>
<td style="text-align: left;">(1.33)</td>
<td style="text-align: left;">(3.39)</td>
<td style="text-align: left;">(3.28)</td>
<td style="text-align: left;">(3.19)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping daily</td>
<td style="text-align: left;">7.12</td>
<td style="text-align: left;">9.57</td>
<td style="text-align: left;">7.69</td>
<td style="text-align: left;">10.4</td>
<td style="text-align: left;">10.4</td>
<td style="text-align: left;">10.4</td>
<td style="text-align: left;">11.1</td>
<td style="text-align: left;">11.1</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">6.68</td>
<td style="text-align: left;">9.14*</td>
<td style="text-align: left;">4.54</td>
<td style="text-align: left;">9.61</td>
<td style="text-align: left;">9.81</td>
<td style="text-align: left;">8.19</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(5.38)</td>
<td style="text-align: left;">(5.55)</td>
<td style="text-align: left;">(5.8)</td>
<td style="text-align: left;">(6.58)</td>
<td style="text-align: left;">(6.58)</td>
<td style="text-align: left;">(6.58)</td>
<td style="text-align: left;">(6.3)</td>
<td style="text-align: left;">(6.3)</td>
<td style="text-align: left;">(6.35)</td>
<td style="text-align: left;">(5.83)</td>
<td style="text-align: left;">(4.55)</td>
<td style="text-align: left;">(2.35)</td>
<td style="text-align: left;">(5.95)</td>
<td style="text-align: left;">(5.73)</td>
<td style="text-align: left;">(5.64)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping &gt; daily</td>
<td style="text-align: left;">9.47</td>
<td style="text-align: left;">9.19</td>
<td style="text-align: left;">7.54</td>
<td style="text-align: left;">5.83</td>
<td style="text-align: left;">5.83</td>
<td style="text-align: left;">5.83</td>
<td style="text-align: left;">7.23</td>
<td style="text-align: left;">7.23</td>
<td style="text-align: left;">7.2</td>
<td style="text-align: left;">7.19</td>
<td style="text-align: left;">13.1</td>
<td style="text-align: left;"> – 6.74</td>
<td style="text-align: left;">7.21</td>
<td style="text-align: left;">8.55</td>
<td style="text-align: left;">9.26</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(12.9)</td>
<td style="text-align: left;">(13.8)</td>
<td style="text-align: left;">(14.5)</td>
<td style="text-align: left;">(17.0)</td>
<td style="text-align: left;">(17.0)</td>
<td style="text-align: left;">(17.0)</td>
<td style="text-align: left;">(16.3)</td>
<td style="text-align: left;">(16.3)</td>
<td style="text-align: left;">(16.4)</td>
<td style="text-align: left;">(14.6)</td>
<td style="text-align: left;">(10.8)</td>
<td style="text-align: left;">(8.49)</td>
<td style="text-align: left;">(15.1)</td>
<td style="text-align: left;">(14.5)</td>
<td style="text-align: left;">(14)</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td rowspan="2" style="text-align: left;">Shopping &lt; weekly</td>
<td style="text-align: left;"> – 1.14</td>
<td style="text-align: left;"> – 1.05</td>
<td style="text-align: left;"> – 1.32</td>
<td style="text-align: left;"> – 1.22</td>
<td style="text-align: left;"> – 1.22</td>
<td style="text-align: left;"> – 1.22</td>
<td style="text-align: left;"> – 1.22</td>
<td style="text-align: left;"> – 1.22</td>
<td style="text-align: left;"> – 1.23</td>
<td style="text-align: left;"> – 1.46</td>
<td style="text-align: left;"> – 0.897</td>
<td style="text-align: left;"> – 1.48</td>
<td style="text-align: left;"> – 1.6</td>
<td style="text-align: left;"> – 1.41</td>
<td style="text-align: left;"> – 1.76</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.2)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.17)</td>
<td style="text-align: left;">(2.15)</td>
<td style="text-align: left;">(2.15)</td>
<td style="text-align: left;">(2.15)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.15)</td>
<td style="text-align: left;">(2.13)</td>
<td style="text-align: left;">(2.1)</td>
<td style="text-align: left;">(2.08)</td>
<td style="text-align: left;">(2.14)</td>
<td style="text-align: left;">(2.14)</td>
<td style="text-align: left;">(2.15)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping 2–6 times/week</td>
<td style="text-align: left;">0.0627</td>
<td style="text-align: left;">0.121</td>
<td style="text-align: left;"> – 0.0458</td>
<td style="text-align: left;"> – 0.227</td>
<td style="text-align: left;"> – 0.227</td>
<td style="text-align: left;"> – 0.227</td>
<td style="text-align: left;"> – 0.213</td>
<td style="text-align: left;"> – 0.213</td>
<td style="text-align: left;"> – 0.18</td>
<td style="text-align: left;"> – 0.541</td>
<td style="text-align: left;">0.367</td>
<td style="text-align: left;"> – 0.602</td>
<td style="text-align: left;">0.0676</td>
<td style="text-align: left;"> – 0.265</td>
<td style="text-align: left;"> – 0.203</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.21)</td>
<td style="text-align: left;">(2.19)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.14)</td>
<td style="text-align: left;">(2.1)</td>
<td style="text-align: left;">(2.1)</td>
<td style="text-align: left;">(2.15)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.16)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping weekly</td>
<td style="text-align: left;"> – 0.207</td>
<td style="text-align: left;"> – 0.034</td>
<td style="text-align: left;"> – 0.108</td>
<td style="text-align: left;">0.0746</td>
<td style="text-align: left;">0.0746</td>
<td style="text-align: left;">0.0746</td>
<td style="text-align: left;"> – 0.0408</td>
<td style="text-align: left;"> – 0.0408</td>
<td style="text-align: left;"> – 0.0481</td>
<td style="text-align: left;"> – 0.497</td>
<td style="text-align: left;">0.0719</td>
<td style="text-align: left;"> – 0.112</td>
<td style="text-align: left;"> – 0.27</td>
<td style="text-align: left;"> – 0.199</td>
<td style="text-align: left;"> – 0.178</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.93)</td>
<td style="text-align: left;">(1.91)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.89)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.9)</td>
<td style="text-align: left;">(1.87)</td>
<td style="text-align: left;">(1.84)</td>
<td style="text-align: left;">(1.82)</td>
<td style="text-align: left;">(1.87)</td>
<td style="text-align: left;">(1.88)</td>
<td style="text-align: left;">(1.88)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping daily</td>
<td style="text-align: left;">5.73</td>
<td style="text-align: left;">5.23</td>
<td style="text-align: left;">5.41</td>
<td style="text-align: left;">5.03</td>
<td style="text-align: left;">5.03</td>
<td style="text-align: left;">5.03</td>
<td style="text-align: left;">4.94</td>
<td style="text-align: left;">4.94</td>
<td style="text-align: left;">4.93</td>
<td style="text-align: left;">5.15</td>
<td style="text-align: left;">7.11*</td>
<td style="text-align: left;">5.02</td>
<td style="text-align: left;">4.77</td>
<td style="text-align: left;">4.85</td>
<td style="text-align: left;">5.56</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.62)</td>
<td style="text-align: left;">(3.55)</td>
<td style="text-align: left;">(3.54)</td>
<td style="text-align: left;">(3.49)</td>
<td style="text-align: left;">(3.49)</td>
<td style="text-align: left;">(3.49)</td>
<td style="text-align: left;">(3.49)</td>
<td style="text-align: left;">(3.49)</td>
<td style="text-align: left;">(3.49)</td>
<td style="text-align: left;">(3.48)</td>
<td style="text-align: left;">(3.4)</td>
<td style="text-align: left;">(3.47)</td>
<td style="text-align: left;">(3.47)</td>
<td style="text-align: left;">(3.47)</td>
<td style="text-align: left;">(3.49)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping &gt; daily</td>
<td style="text-align: left;">15.3</td>
<td style="text-align: left;">15.3</td>
<td style="text-align: left;">15.4</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">15.5</td>
<td style="text-align: left;">15.5</td>
<td style="text-align: left;">15.5</td>
<td style="text-align: left;">15.2</td>
<td style="text-align: left;">16.5*</td>
<td style="text-align: left;">2.25</td>
<td style="text-align: left;">15.3</td>
<td style="text-align: left;">15.6</td>
<td style="text-align: left;">15.8</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(8.91)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.89)</td>
<td style="text-align: left;">(8.75)</td>
<td style="text-align: left;">(8.35)</td>
<td style="text-align: left;">(9.93)</td>
<td style="text-align: left;">(8.76)</td>
<td style="text-align: left;">(8.75)</td>
<td style="text-align: left;">(8.75)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">55555 rescaled</td>
<td rowspan="2" style="text-align: left;">Shopping &lt; weekly</td>
<td style="text-align: left;"> – 1.35 × 10–3</td>
<td style="text-align: left;"> – 1.57 × 10–3</td>
<td style="text-align: left;">0.0103</td>
<td style="text-align: left;"> – 0.0111</td>
<td style="text-align: left;"> – 0.0111</td>
<td style="text-align: left;"> – 0.0111</td>
<td style="text-align: left;"> – 0.195</td>
<td style="text-align: left;"> – 0.195</td>
<td style="text-align: left;"> – 0.178</td>
<td style="text-align: left;"> – 0.0566</td>
<td style="text-align: left;"> – 0.0217</td>
<td style="text-align: left;"> – 0.0327</td>
<td style="text-align: left;"> – 0.0316</td>
<td style="text-align: left;">8.19 × 10–3</td>
<td style="text-align: left;">0.0159</td>
</tr>
<tr>
<td style="text-align: left;">(0.0279)</td>
<td style="text-align: left;">(0.0317)</td>
<td style="text-align: left;">(0.0361)</td>
<td style="text-align: left;">(0.0368)</td>
<td style="text-align: left;">(0.0368)</td>
<td style="text-align: left;">(0.0368)</td>
<td style="text-align: left;">(0.154)</td>
<td style="text-align: left;">(0.154)</td>
<td style="text-align: left;">(0.214)</td>
<td style="text-align: left;">(0.0844)</td>
<td style="text-align: left;">(0.0744)</td>
<td style="text-align: left;">(0.0763)</td>
<td style="text-align: left;">(0.0545)</td>
<td style="text-align: left;">(0.0427)</td>
<td style="text-align: left;">(0.0379)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping 2–6 times/week</td>
<td style="text-align: left;">2.44 × 10–3</td>
<td style="text-align: left;"> – 0.0246</td>
<td style="text-align: left;"> – 0.0179</td>
<td style="text-align: left;"> – 0.0415</td>
<td style="text-align: left;"> – 0.0415</td>
<td style="text-align: left;"> – 0.0415</td>
<td style="text-align: left;"> – 0.149</td>
<td style="text-align: left;"> – 0.149</td>
<td style="text-align: left;"> – 0.326</td>
<td style="text-align: left;"> – 0.0317</td>
<td style="text-align: left;"> – 0.0191</td>
<td style="text-align: left;">2.32 × 10–3</td>
<td style="text-align: left;"> – 4 × 10–2</td>
<td style="text-align: left;"> – 0.0191</td>
<td style="text-align: left;">2.5 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0282)</td>
<td style="text-align: left;">(0.0318)</td>
<td style="text-align: left;">(0.0362)</td>
<td style="text-align: left;">(0.0369)</td>
<td style="text-align: left;">(0.0369)</td>
<td style="text-align: left;">(0.0369)</td>
<td style="text-align: left;">(0.155)</td>
<td style="text-align: left;">(0.155)</td>
<td style="text-align: left;">(0.214)</td>
<td style="text-align: left;">(0.0849)</td>
<td style="text-align: left;">(0.0746)</td>
<td style="text-align: left;">(0.0772)</td>
<td style="text-align: left;">(0.0547)</td>
<td style="text-align: left;">(0.043)</td>
<td style="text-align: left;">(0.0381)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Shopping weekly</td>
<td style="text-align: left;"> – 3.35 × 10–4</td>
<td style="text-align: left;"> – 8.74 × 10–3</td>
<td style="text-align: left;">7.11 × 10–3</td>
<td style="text-align: left;">3.53 × 10–3</td>
<td style="text-align: left;">3.53 × 10–3</td>
<td style="text-align: left;">3.53 × 10–3</td>
<td style="text-align: left;"> – 6.34 × 10–3</td>
<td style="text-align: left;"> – 6.34 × 10–3</td>
<td style="text-align: left;">0.0329</td>
<td style="text-align: left;"> – 0.0292</td>
<td style="text-align: left;"> – 0.0527*</td>
<td style="text-align: left;"> – 0.0515</td>
<td style="text-align: left;"> – 4.07 × 10–3</td>
<td style="text-align: left;">2.75 × 10–3</td>
<td style="text-align: left;">0.0143</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0245)</td>
<td style="text-align: left;">(0.0278)</td>
<td style="text-align: left;">(0.0316)</td>
<td style="text-align: left;">(0.0324)</td>
<td style="text-align: left;">(0.0324)</td>
<td style="text-align: left;">(0.0324)</td>
<td style="text-align: left;">(0.136)</td>
<td style="text-align: left;">(0.136)</td>
<td style="text-align: left;">(0.189)</td>
<td style="text-align: left;">(0.0742)</td>
<td style="text-align: left;">(0.0653)</td>
<td style="text-align: left;">(0.0668)</td>
<td style="text-align: left;">(0.0478)</td>
<td style="text-align: left;">(0.0375)</td>
<td style="text-align: left;">(0.0332)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping daily</td>
<td style="text-align: left;">0.0623</td>
<td style="text-align: left;">0.0177</td>
<td style="text-align: left;">0.0591</td>
<td style="text-align: left;">0.0116</td>
<td style="text-align: left;">0.0116</td>
<td style="text-align: left;">0.0116</td>
<td style="text-align: left;"> – 0.0779</td>
<td style="text-align: left;"> – 0.0779</td>
<td style="text-align: left;"> – 4.17 × 10–3</td>
<td style="text-align: left;">0.0805</td>
<td style="text-align: left;">0.0662</td>
<td style="text-align: left;">0.0451</td>
<td style="text-align: left;"> – 0.0193</td>
<td style="text-align: left;"> – 0.025</td>
<td style="text-align: left;">0.0637</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0466)</td>
<td style="text-align: left;">(0.0522)</td>
<td style="text-align: left;">(0.0596)</td>
<td style="text-align: left;">(0.0604)</td>
<td style="text-align: left;">(0.0604)</td>
<td style="text-align: left;">(0.0604)</td>
<td style="text-align: left;">(0.252)</td>
<td style="text-align: left;">(0.252)</td>
<td style="text-align: left;">(0.35)</td>
<td style="text-align: left;">(0.14)</td>
<td style="text-align: left;">(0.123)</td>
<td style="text-align: left;">(0.129)</td>
<td style="text-align: left;">(0.0895)</td>
<td style="text-align: left;">(0.0699)</td>
<td style="text-align: left;">(0.0624)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Shopping &gt; daily</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">0.161</td>
<td style="text-align: left;">0.191</td>
<td style="text-align: left;">0.201</td>
<td style="text-align: left;">0.201</td>
<td style="text-align: left;">0.201</td>
<td style="text-align: left;">0.265</td>
<td style="text-align: left;">0.265</td>
<td style="text-align: left;">0.294</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: left;">0.093</td>
<td style="text-align: left;"> – 0.0689</td>
<td style="text-align: left;">0.221</td>
<td style="text-align: left;">0.187</td>
<td style="text-align: left;">0.187</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.116)</td>
<td style="text-align: left;">(0.133)</td>
<td style="text-align: left;">(0.152)</td>
<td style="text-align: left;">(0.157)</td>
<td style="text-align: left;">(0.157)</td>
<td style="text-align: left;">(0.157)</td>
<td style="text-align: left;">(0.662)</td>
<td style="text-align: left;">(0.662)</td>
<td style="text-align: left;">(0.919)</td>
<td style="text-align: left;">(0.36)</td>
<td style="text-align: left;">(0.307)</td>
<td style="text-align: left;">(0.371)</td>
<td style="text-align: left;">(0.231)</td>
<td style="text-align: left;">(0.18)</td>
<td style="text-align: left;">(0.159)</td>
</tr>
</tbody>
</table>

*Note.* Standard errors in parentheses; \* = significant at 5% level

</div>

<div id="Tab14" class="table-wrap">

<div class="caption">

Rescaled 55555 robustness tests for Tobit regression results including frequency of leaving the house for exercise and fresh air

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Low rescaled 55555</th>
<th colspan="3" style="text-align: left;">Censoring rescaled 55555</th>
<th colspan="3" style="text-align: left;">Impact on mean rescaled 55555</th>
<th colspan="3" style="text-align: left;">High VAS for dead</th>
<th colspan="3" style="text-align: left;">Rescaled 55555 high rate of change</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;"> – 1</th>
<th style="text-align: left;"> – 1.5</th>
<th style="text-align: left;"> – 2</th>
<th style="text-align: left;">1.5</th>
<th style="text-align: left;">2</th>
<th style="text-align: left;">2.5</th>
<th style="text-align: left;">75</th>
<th style="text-align: left;">50</th>
<th style="text-align: left;">25</th>
<th style="text-align: left;">0.1</th>
<th style="text-align: left;">0.075</th>
<th style="text-align: left;">0.05</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">11111</td>
<td rowspan="2" style="text-align: left;">Exercise &lt; weekly</td>
<td style="text-align: left;"> – 3.62</td>
<td style="text-align: left;"> – 3.93</td>
<td style="text-align: left;"> – 3.99*</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;"> – 4.29*</td>
<td style="text-align: left;"> – 4.33*</td>
<td style="text-align: left;"> – 3.67</td>
<td style="text-align: left;"> – 3.82</td>
<td style="text-align: left;"> – 4.44*</td>
<td style="text-align: left;"> – 3.91*</td>
<td style="text-align: left;"> – 3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.06)</td>
<td style="text-align: left;">(2.03)</td>
<td style="text-align: left;">(2.01)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.04)</td>
<td style="text-align: left;">(2.14)</td>
<td style="text-align: left;">(2.19)</td>
<td style="text-align: left;">(1.97)</td>
<td style="text-align: left;">(1.95)</td>
<td style="text-align: left;">(1.88)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise 2–6 times/week</td>
<td style="text-align: left;"> – 1.58</td>
<td style="text-align: left;"> – 1.61</td>
<td style="text-align: left;"> – 1.76</td>
<td style="text-align: left;"> – 1.68</td>
<td style="text-align: left;"> – 1.68</td>
<td style="text-align: left;"> – 1.68</td>
<td style="text-align: left;"> – 1.73</td>
<td style="text-align: left;"> – 1.73</td>
<td style="text-align: left;"> – 1.72</td>
<td style="text-align: left;"> – 1.84</td>
<td style="text-align: left;"> – 1.98</td>
<td style="text-align: left;"> – 1.72</td>
<td style="text-align: left;"> – 2.43</td>
<td style="text-align: left;"> – 2.43</td>
<td style="text-align: left;"> – 2.13</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.72)</td>
<td style="text-align: left;">(1.7)</td>
<td style="text-align: left;">(1.68)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.7)</td>
<td style="text-align: left;">(1.7)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.71)</td>
<td style="text-align: left;">(1.76)</td>
<td style="text-align: left;">(1.8)</td>
<td style="text-align: left;">(1.64)</td>
<td style="text-align: left;">(1.62)</td>
<td style="text-align: left;">(1.55)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise weekly</td>
<td style="text-align: left;"> – 4.58*</td>
<td style="text-align: left;"> – 4.65*</td>
<td style="text-align: left;"> – 4.63*</td>
<td style="text-align: left;"> – 4.65*</td>
<td style="text-align: left;"> – 4.65*</td>
<td style="text-align: left;"> – 4.65*</td>
<td style="text-align: left;"> – 4.8*</td>
<td style="text-align: left;"> – 4.8*</td>
<td style="text-align: left;"> – 4.8*</td>
<td style="text-align: left;"> – 4.79*</td>
<td style="text-align: left;"> – 5.33*</td>
<td style="text-align: left;"> – 5.01</td>
<td style="text-align: left;"> – 5.35*</td>
<td style="text-align: left;"> – 4.56*</td>
<td style="text-align: left;"> – 3.73*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.03)</td>
<td style="text-align: left;">(2.00)</td>
<td style="text-align: left;">(1.98)</td>
<td style="text-align: left;">(1.98)</td>
<td style="text-align: left;">(1.98)</td>
<td style="text-align: left;">(1.98)</td>
<td style="text-align: left;">(1.99)</td>
<td style="text-align: left;">(1.99)</td>
<td style="text-align: left;">(1.99)</td>
<td style="text-align: left;">(2.02)</td>
<td style="text-align: left;">(2.1)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(1.93)</td>
<td style="text-align: left;">(1.92)</td>
<td style="text-align: left;">(1.84)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise daily</td>
<td style="text-align: left;"> – 1.85</td>
<td style="text-align: left;"> – 1.96</td>
<td style="text-align: left;"> – 2.02</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;"> – 2.15</td>
<td style="text-align: left;"> – 2.28</td>
<td style="text-align: left;"> – 2.49</td>
<td style="text-align: left;"> – 2.79</td>
<td style="text-align: left;"> – 2.39</td>
<td style="text-align: left;"> – 2.27</td>
<td style="text-align: left;"> – 1.76</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(1.72)</td>
<td style="text-align: left;">(1.7)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.69)</td>
<td style="text-align: left;">(1.71)</td>
<td style="text-align: left;">(1.76)</td>
<td style="text-align: left;">(1.79)</td>
<td style="text-align: left;">(1.64)</td>
<td style="text-align: left;">(1.62)</td>
<td style="text-align: left;">(1.55)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise &gt; daily</td>
<td style="text-align: left;">3.6</td>
<td style="text-align: left;">3.25</td>
<td style="text-align: left;">3.18</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.64</td>
<td style="text-align: left;">2.64</td>
<td style="text-align: left;">2.63</td>
<td style="text-align: left;">2.54</td>
<td style="text-align: left;">3.13</td>
<td style="text-align: left;">3.67</td>
<td style="text-align: left;">2.5</td>
<td style="text-align: left;">2.41</td>
<td style="text-align: left;">2.38</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.64)</td>
<td style="text-align: left;">(2.6)</td>
<td style="text-align: left;">(2.6)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.67)</td>
<td style="text-align: left;">(2.81)</td>
<td style="text-align: left;">(2.52)</td>
<td style="text-align: left;">(2.48)</td>
<td style="text-align: left;">(2.37)</td>
</tr>
<tr>
<td style="text-align: left;">Dead</td>
<td rowspan="2" style="text-align: left;">Exercise &lt; weekly</td>
<td style="text-align: left;">10.4*</td>
<td style="text-align: left;">11*</td>
<td style="text-align: left;">11.1*</td>
<td style="text-align: left;">12.2*</td>
<td style="text-align: left;">12.2*</td>
<td style="text-align: left;">12.2*</td>
<td style="text-align: left;">12*</td>
<td style="text-align: left;">12*</td>
<td style="text-align: left;">12.1*</td>
<td style="text-align: left;">11.9*</td>
<td style="text-align: left;">7.62*</td>
<td style="text-align: left;">3.33</td>
<td style="text-align: left;">11.5*</td>
<td style="text-align: left;">11.1*</td>
<td style="text-align: left;">8.66*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.98)</td>
<td style="text-align: left;">(4.22)</td>
<td style="text-align: left;">(4.34)</td>
<td style="text-align: left;">(5.04)</td>
<td style="text-align: left;">(5.04)</td>
<td style="text-align: left;">(5.04)</td>
<td style="text-align: left;">(4.8)</td>
<td style="text-align: left;">(4.8)</td>
<td style="text-align: left;">(4.84)</td>
<td style="text-align: left;">(4.34)</td>
<td style="text-align: left;">(3.57)</td>
<td style="text-align: left;">(1.8)</td>
<td style="text-align: left;">(4.61)</td>
<td style="text-align: left;">(4.44)</td>
<td style="text-align: left;">(4.37)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise 2–6 times/week</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">1.47</td>
<td style="text-align: left;">0.983</td>
<td style="text-align: left;">1.68</td>
<td style="text-align: left;">1.68</td>
<td style="text-align: left;">1.68</td>
<td style="text-align: left;">0.528</td>
<td style="text-align: left;">0.528</td>
<td style="text-align: left;">0.943</td>
<td style="text-align: left;">1.19</td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">-0.0619</td>
<td style="text-align: left;">2.78</td>
<td style="text-align: left;">2.46</td>
<td style="text-align: left;">1.3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.44)</td>
<td style="text-align: left;">(3.65)</td>
<td style="text-align: left;">(3.75)</td>
<td style="text-align: left;">(4.37)</td>
<td style="text-align: left;">(4.37)</td>
<td style="text-align: left;">(4.37)</td>
<td style="text-align: left;">(4.17)</td>
<td style="text-align: left;">(4.17)</td>
<td style="text-align: left;">(4.21)</td>
<td style="text-align: left;">(3.77)</td>
<td style="text-align: left;">(3.02)</td>
<td style="text-align: left;">(1.53)</td>
<td style="text-align: left;">(3.97)</td>
<td style="text-align: left;">(3.82)</td>
<td style="text-align: left;">(3.71)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise weekly</td>
<td style="text-align: left;">9.63*</td>
<td style="text-align: left;">11.5*</td>
<td style="text-align: left;">11.3*</td>
<td style="text-align: left;">14.1*</td>
<td style="text-align: left;">14.1*</td>
<td style="text-align: left;">14.1*</td>
<td style="text-align: left;">12.8*</td>
<td style="text-align: left;">12.8*</td>
<td style="text-align: left;">12.8*</td>
<td style="text-align: left;">11.4*</td>
<td style="text-align: left;">8.33*</td>
<td style="text-align: left;">1.92</td>
<td style="text-align: left;">14.1*</td>
<td style="text-align: left;">12*</td>
<td style="text-align: left;">10.4*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.95)</td>
<td style="text-align: left;">(4.16)</td>
<td style="text-align: left;">(4.28)</td>
<td style="text-align: left;">(4.96)</td>
<td style="text-align: left;">(4.96)</td>
<td style="text-align: left;">(4.96)</td>
<td style="text-align: left;">(4.73)</td>
<td style="text-align: left;">(4.73)</td>
<td style="text-align: left;">(4.78)</td>
<td style="text-align: left;">(4.31)</td>
<td style="text-align: left;">(3.52)</td>
<td style="text-align: left;">(1.82)</td>
<td style="text-align: left;">(4.51)</td>
<td style="text-align: left;">(4.38)</td>
<td style="text-align: left;">(4.28)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise daily</td>
<td style="text-align: left;">1.16</td>
<td style="text-align: left;">2.8</td>
<td style="text-align: left;">2.02</td>
<td style="text-align: left;">5.28</td>
<td style="text-align: left;">5.28</td>
<td style="text-align: left;">5.28</td>
<td style="text-align: left;">5.07</td>
<td style="text-align: left;">5.07</td>
<td style="text-align: left;">5.02</td>
<td style="text-align: left;">3.03</td>
<td style="text-align: left;">2.91</td>
<td style="text-align: left;">0.556</td>
<td style="text-align: left;">6.03</td>
<td style="text-align: left;">4.48</td>
<td style="text-align: left;">3.44</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.46)</td>
<td style="text-align: left;">(3.66)</td>
<td style="text-align: left;">(3.77)</td>
<td style="text-align: left;">(4.36)</td>
<td style="text-align: left;">(4.36)</td>
<td style="text-align: left;">(4.36)</td>
<td style="text-align: left;">(4.16)</td>
<td style="text-align: left;">(4.16)</td>
<td style="text-align: left;">(4.19)</td>
<td style="text-align: left;">(3.78)</td>
<td style="text-align: left;">(3.03)</td>
<td style="text-align: left;">(1.53)</td>
<td style="text-align: left;">(3.97)</td>
<td style="text-align: left;">(3.83)</td>
<td style="text-align: left;">(3.72)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise &gt; daily</td>
<td style="text-align: left;">5.23</td>
<td style="text-align: left;">6.88</td>
<td style="text-align: left;">6.31</td>
<td style="text-align: left;">6.67</td>
<td style="text-align: left;">6.67</td>
<td style="text-align: left;">6.67</td>
<td style="text-align: left;">6.98</td>
<td style="text-align: left;">6.98</td>
<td style="text-align: left;">7.08</td>
<td style="text-align: left;">7.53</td>
<td style="text-align: left;">8.8*</td>
<td style="text-align: left;">1.16</td>
<td style="text-align: left;">7.85</td>
<td style="text-align: left;">7.66</td>
<td style="text-align: left;">6.75</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(5.1)</td>
<td style="text-align: left;">(5.38)</td>
<td style="text-align: left;">(5.6)</td>
<td style="text-align: left;">(6.5)</td>
<td style="text-align: left;">(6.5)</td>
<td style="text-align: left;">(6.5)</td>
<td style="text-align: left;">(6.19)</td>
<td style="text-align: left;">(6.19)</td>
<td style="text-align: left;">(6.25)</td>
<td style="text-align: left;">(5.56)</td>
<td style="text-align: left;">(4.32)</td>
<td style="text-align: left;">(2.31)</td>
<td style="text-align: left;">(5.89)</td>
<td style="text-align: left;">(5.66)</td>
<td style="text-align: left;">(5.5)</td>
</tr>
<tr>
<td style="text-align: left;">55555</td>
<td rowspan="2" style="text-align: left;">Exercise &lt; weekly</td>
<td style="text-align: left;">4.07</td>
<td style="text-align: left;">4.29</td>
<td style="text-align: left;">3.99</td>
<td style="text-align: left;">3.89</td>
<td style="text-align: left;">3.89</td>
<td style="text-align: left;">3.89</td>
<td style="text-align: left;">3.87</td>
<td style="text-align: left;">3.87</td>
<td style="text-align: left;">3.87</td>
<td style="text-align: left;">3.43</td>
<td style="text-align: left;">1.84</td>
<td style="text-align: left;">0.437</td>
<td style="text-align: left;">3.38</td>
<td style="text-align: left;">3.46</td>
<td style="text-align: left;">2.69</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.67)</td>
<td style="text-align: left;">(2.65)</td>
<td style="text-align: left;">(2.63)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.58)</td>
<td style="text-align: left;">(2.58)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.61)</td>
<td style="text-align: left;">(2.64)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise 2–6 times/week</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.5</td>
<td style="text-align: left;">2.71</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.59</td>
<td style="text-align: left;">2.62</td>
<td style="text-align: left;">2.62</td>
<td style="text-align: left;">2.65</td>
<td style="text-align: left;">2.62</td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;">1.78</td>
<td style="text-align: left;">2.86</td>
<td style="text-align: left;">2.95</td>
<td style="text-align: left;">2.92</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.22)</td>
<td style="text-align: left;">(2.21)</td>
<td style="text-align: left;">(2.19)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.11)</td>
<td style="text-align: left;">(2.08)</td>
<td style="text-align: left;">(2.17)</td>
<td style="text-align: left;">(2.17)</td>
<td style="text-align: left;">(2.17)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise weekly</td>
<td style="text-align: left;">7.53*</td>
<td style="text-align: left;">7.3*</td>
<td style="text-align: left;">7.42*</td>
<td style="text-align: left;">7.22*</td>
<td style="text-align: left;">7.22*</td>
<td style="text-align: left;">7.22*</td>
<td style="text-align: left;">7.47*</td>
<td style="text-align: left;">7.47*</td>
<td style="text-align: left;">7.47*</td>
<td style="text-align: left;">7.06*</td>
<td style="text-align: left;">6.32*</td>
<td style="text-align: left;">5.26*</td>
<td style="text-align: left;">7.86*</td>
<td style="text-align: left;">7.24*</td>
<td style="text-align: left;">7.38*</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.63)</td>
<td style="text-align: left;">(2.6)</td>
<td style="text-align: left;">(2.59)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.56)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.53)</td>
<td style="text-align: left;">(2.53)</td>
<td style="text-align: left;">(2.55)</td>
<td style="text-align: left;">(2.57)</td>
<td style="text-align: left;">(2.58)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise daily</td>
<td style="text-align: left;">2.48</td>
<td style="text-align: left;">2.51</td>
<td style="text-align: left;">2.76</td>
<td style="text-align: left;">2.78</td>
<td style="text-align: left;">2.78</td>
<td style="text-align: left;">2.78</td>
<td style="text-align: left;">2.83</td>
<td style="text-align: left;">2.83</td>
<td style="text-align: left;">2.82</td>
<td style="text-align: left;">2.76</td>
<td style="text-align: left;">2.73</td>
<td style="text-align: left;">1.13</td>
<td style="text-align: left;">3.15</td>
<td style="text-align: left;">3.03</td>
<td style="text-align: left;">3.12</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(2.23)</td>
<td style="text-align: left;">(2.21)</td>
<td style="text-align: left;">(2.2)</td>
<td style="text-align: left;">(2.19)</td>
<td style="text-align: left;">(2.19)</td>
<td style="text-align: left;">(2.19)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.16)</td>
<td style="text-align: left;">(2.12)</td>
<td style="text-align: left;">(2.08)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
<td style="text-align: left;">(2.18)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise &gt; daily</td>
<td style="text-align: left;">0.0398</td>
<td style="text-align: left;">0.175</td>
<td style="text-align: left;">0.349</td>
<td style="text-align: left;">0.531</td>
<td style="text-align: left;">0.531</td>
<td style="text-align: left;">0.531</td>
<td style="text-align: left;">0.426</td>
<td style="text-align: left;">0.426</td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">0.619</td>
<td style="text-align: left;">0.876</td>
<td style="text-align: left;"> – 2.44</td>
<td style="text-align: left;">0.645</td>
<td style="text-align: left;">0.707</td>
<td style="text-align: left;">0.679</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(3.37)</td>
<td style="text-align: left;">(3.34)</td>
<td style="text-align: left;">(3.34)</td>
<td style="text-align: left;">(3.31)</td>
<td style="text-align: left;">(3.31)</td>
<td style="text-align: left;">(3.31)</td>
<td style="text-align: left;">(3.31)</td>
<td style="text-align: left;">(3.31)</td>
<td style="text-align: left;">(3.31)</td>
<td style="text-align: left;">(3.27)</td>
<td style="text-align: left;">(3.16)</td>
<td style="text-align: left;">(3.2)</td>
<td style="text-align: left;">(3.29)</td>
<td style="text-align: left;">(3.29)</td>
<td style="text-align: left;">(3.29)</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">55555 rescaled</td>
<td rowspan="2" style="text-align: left;">Exercise &lt; weekly</td>
<td style="text-align: left;">0.0125</td>
<td style="text-align: left;">9.41 × 10–4</td>
<td style="text-align: left;"> – 0.0102</td>
<td style="text-align: left;"> – 0.0155</td>
<td style="text-align: left;"> – 0.0155</td>
<td style="text-align: left;"> – 0.0155</td>
<td style="text-align: left;"> – 0.0514</td>
<td style="text-align: left;"> – 0.0514</td>
<td style="text-align: left;"> – 0.0442</td>
<td style="text-align: left;"> – 0.138</td>
<td style="text-align: left;">6.08 × 10–3</td>
<td style="text-align: left;">1.92 × 10–3</td>
<td style="text-align: left;"> – 0.0127</td>
<td style="text-align: left;"> – 0.0169</td>
<td style="text-align: left;">2.95 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;">(0.034)</td>
<td style="text-align: left;">(0.0387)</td>
<td style="text-align: left;">(0.0438)</td>
<td style="text-align: left;">(0.0449)</td>
<td style="text-align: left;">(0.0449)</td>
<td style="text-align: left;">(0.0449)</td>
<td style="text-align: left;">(0.187)</td>
<td style="text-align: left;">(0.187)</td>
<td style="text-align: left;">(0.26)</td>
<td style="text-align: left;">(0.102)</td>
<td style="text-align: left;">(0.0912)</td>
<td style="text-align: left;">(0.0937)</td>
<td style="text-align: left;">(0.0667)</td>
<td style="text-align: left;">(0.0522)</td>
<td style="text-align: left;">(0.0466)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Exercise 2–6 times/week</td>
<td style="text-align: left;">0.0325</td>
<td style="text-align: left;">0.0245</td>
<td style="text-align: left;">0.0294</td>
<td style="text-align: left;">0.0255</td>
<td style="text-align: left;">0.0255</td>
<td style="text-align: left;">0.0255</td>
<td style="text-align: left;">0.0875</td>
<td style="text-align: left;">0.0875</td>
<td style="text-align: left;"> – 0.0396</td>
<td style="text-align: left;">0.0237</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.0202</td>
<td style="text-align: left;">4.48 × 10–3</td>
<td style="text-align: left;">0.0185</td>
<td style="text-align: left;">0.0407</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0282)</td>
<td style="text-align: left;">(0.0321)</td>
<td style="text-align: left;">(0.0364)</td>
<td style="text-align: left;">(0.0374)</td>
<td style="text-align: left;">(0.0374)</td>
<td style="text-align: left;">(0.0374)</td>
<td style="text-align: left;">(0.156)</td>
<td style="text-align: left;">(0.156)</td>
<td style="text-align: left;">(0.217)</td>
<td style="text-align: left;">(0.0854)</td>
<td style="text-align: left;">(0.0746)</td>
<td style="text-align: left;">(0.0762)</td>
<td style="text-align: left;">(0.0553)</td>
<td style="text-align: left;">(0.0432)</td>
<td style="text-align: left;">(0.0383)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise weekly</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;"> – 3.74 × 10–3</td>
<td style="text-align: left;"> – 1.68 × 10–3</td>
<td style="text-align: left;"> – 0.0251</td>
<td style="text-align: left;"> – 0.0251</td>
<td style="text-align: left;"> – 0.0251</td>
<td style="text-align: left;"> – 3.78 × 10–3</td>
<td style="text-align: left;"> – 3.78 × 10–3</td>
<td style="text-align: left;">0.0139</td>
<td style="text-align: left;"> – 0.0244</td>
<td style="text-align: left;">0.0177</td>
<td style="text-align: left;">0.072</td>
<td style="text-align: left;"> – 0.0299</td>
<td style="text-align: left;"> – 0.0114</td>
<td style="text-align: left;">0.0237</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0337)</td>
<td style="text-align: left;">(0.0381)</td>
<td style="text-align: left;">(0.0433)</td>
<td style="text-align: left;">(0.0442)</td>
<td style="text-align: left;">(0.0442)</td>
<td style="text-align: left;">(0.0442)</td>
<td style="text-align: left;">(0.184)</td>
<td style="text-align: left;">(0.184)</td>
<td style="text-align: left;">(0.257)</td>
<td style="text-align: left;">(0.101)</td>
<td style="text-align: left;">(0.0902)</td>
<td style="text-align: left;">(0.0936)</td>
<td style="text-align: left;">(0.0655)</td>
<td style="text-align: left;">(0.0515)</td>
<td style="text-align: left;">(0.0458)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise daily</td>
<td style="text-align: left;">0.0356</td>
<td style="text-align: left;">0.0123</td>
<td style="text-align: left;">0.0254</td>
<td style="text-align: left;"> – 5.47 × 10–3</td>
<td style="text-align: left;"> – 5.47 × 10–3</td>
<td style="text-align: left;"> – 5.47 × 10–3</td>
<td style="text-align: left;"> – 0.189</td>
<td style="text-align: left;"> – 0.189</td>
<td style="text-align: left;"> – 0.159</td>
<td style="text-align: left;"> – 0.0393</td>
<td style="text-align: left;"> – 0.0265*</td>
<td style="text-align: left;"> – 0.0345</td>
<td style="text-align: left;"> – 0.0523</td>
<td style="text-align: left;"> – 6.46 × 10–3</td>
<td style="text-align: left;">0.0149</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0283)</td>
<td style="text-align: left;">(0.0321)</td>
<td style="text-align: left;">(0.0365)</td>
<td style="text-align: left;">(0.0373)</td>
<td style="text-align: left;">(0.0373)</td>
<td style="text-align: left;">(0.0373)</td>
<td style="text-align: left;">(0.155)</td>
<td style="text-align: left;">(0.155)</td>
<td style="text-align: left;">(0.217)</td>
<td style="text-align: left;">(0.0855)</td>
<td style="text-align: left;">(0.0748)</td>
<td style="text-align: left;">(0.0762)</td>
<td style="text-align: left;">(0.0553)</td>
<td style="text-align: left;">(0.0433)</td>
<td style="text-align: left;">(0.0384)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Exercise &gt; daily</td>
<td style="text-align: left;">6.33 × 10–3</td>
<td style="text-align: left;"> – 0.0125</td>
<td style="text-align: left;"> – 3.24 × 10–3</td>
<td style="text-align: left;"> – 0.0131</td>
<td style="text-align: left;"> – 0.0131</td>
<td style="text-align: left;"> – 0.0131</td>
<td style="text-align: left;"> – 6.31 × 10–4</td>
<td style="text-align: left;"> – 6.31 × 10–4</td>
<td style="text-align: left;"> – 0.0222</td>
<td style="text-align: left;"> – 0.0552</td>
<td style="text-align: left;"> – 0.0323</td>
<td style="text-align: left;"> – 0.023</td>
<td style="text-align: left;"> – 0.0119</td>
<td style="text-align: left;"> – 0.0116</td>
<td style="text-align: left;">5.35 × 10–3</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(0.0425)</td>
<td style="text-align: left;">(0.0482)</td>
<td style="text-align: left;">(0.055)</td>
<td style="text-align: left;">(0.0563)</td>
<td style="text-align: left;">(0.0563)</td>
<td style="text-align: left;">(0.0563)</td>
<td style="text-align: left;">(0.235)</td>
<td style="text-align: left;">(0.235)</td>
<td style="text-align: left;">(0.327)</td>
<td style="text-align: left;">(0.128)</td>
<td style="text-align: left;">(0.111)</td>
<td style="text-align: left;">(0.116)</td>
<td style="text-align: left;">(0.0833)</td>
<td style="text-align: left;">(0.0651)</td>
<td style="text-align: left;">(0.0576)</td>
</tr>
</tbody>
</table>

*Note.* Standard errors in parentheses, \*significant at 5% level

</div>

### Acknowledgements

We would like to thank participants at the Winter 2022 Health Economists’ Study Group Workshop in Leeds, particularly Edward Cox (University of York) who acted as a discussant for the paper. We would also like to thank seminar participants at the University of Leeds.

### Funding

The COVID-19 survey was made possible by an unrestricted grant from the EuroQoL Research Foundation. This work is supported by the grant “COVID-19 and EQ-5D health state valuation” (Ref: 289-RA) from the EuroQol Research Foundation (PI: Edward Webb). The funder had no role in the study design or in the collection, analysis, interpretation of data, or in the preparation and submission of this manuscript.

### Data availability

Data may be made available upon request to the corresponding author or Leeds Institute of Health Sciences provided appropriate ethical approvals and data sharing agreements are put in place.

### Declarations

#### Competing interests

The authors declare no competing interests.

#### Ethical approval

Approval for the study (MREC 19–082 – Measuring population health using EQ-5D during a national health emergency) was obtained from the School of Medicine Research Ethics Committee at the University of Leeds.

## References

1. World Health Organization, COVID-19 weekly epidemiological update - 6 July 2022. [Online]. Available: https://www.who.int/publications/m/item/weekly-epidemiological-update-on-covid-19-6-July-2022.

2. Greenhalgh T, Knight M, Buxton M, Husain L. Management of post-acute covid-19 in primary care. BMJ. 2020. doi:10.1136/bmj.m3026

3. Xiong Q. Clinical sequelae of COVID-19 survivors in Wuhan, China: a single-centre longitudinal study. Clin. Microbiol. Infect. 2020. doi:10.1016/j.cmi.2020.09.023

4. Troyer EA, Kohn JN, Hong S. Are we facing a crashing wave of neuropsychiatric sequelae of COVID-19? Neuropsychiatric symptoms and potential immunologic mechanisms. Brain Behav. Immun. 2020. doi:10.1016/j.bbi.2020.04.027

5. Demertzis ZD. Cardiac sequelae of novel coronavirus disease 2019 (COVID-19): a clinical case series. Eur. Heart J. Case Reports. 2020;4(FI1):1–6. doi:10.1093/ehjcr/ytaa179

6. Mahase E. COVID-19: Sore throat, fatigue, and myalgia are more common with new UK variant. BMJ. 2021. doi:10.1136/bmj.n288

7. Khan KS, Mamun MA, Griffiths MD. Ullah I The mental health impact of the COVID-19 pandemic across different cohorts. Int. J. Mental Health Addict. 2020. doi:10.1007/s11469-020-00367-0

8. Miles DK, Stedman M, Heald AH. “Stay at Home, Protect the National Health Service, Save Lives”: a cost benefit analysis of the lockdown in the United Kingdom. Int. J. Clin. Pract. 2021;75(3):e13674. doi:10.1111/ijcp.13674

9. Charlesworth A. What is the right level of spending needed for health and care in the UK. The Lancet. 2021. doi:10.1016/S0140-6736(21)00230-0

10. Burki TK. Cuts in cancer research funding due to COVID-19. Lancet Oncol. 2021;22(1):e6. doi:10.1016/S1470-2045(20)30749-X

11. Spencer K. The impact of the COVID-19 pandemic on radiotherapy services in England, UK: a population-based study. Lancet Oncol. 2021;22(3):309–320. doi:10.1016/S1470-2045(20)30743-9

12. Sud A. Effect of delays in the 2-week-wait cancer referral pathway during the COVID-19 pandemic on cancer survival in the UK: a modelling study. Lancet Oncol. 2020;21(8):1035–1044. doi:10.1016/S1470-2045(20)30392-2

13. Mahase E. BMA urges plan to tackle backlog of patients awaiting non-covid treatment. BMJ. 2020. doi:10.1136/bmj.m2238

14. Carr A, Smith JA, Camaradou J, Prieto-Alhambra D. "Growing backlog of planned surgery due to COVID-19. BMJ. 2021. doi:10.1136/bmj.n339

15. Macdonald N, Clements C, Sobti A, Rossiter D, Unnithan A, Bosanquet N. Tackling the elective case backlog generated by COVID-19: the scale of the problem and solutions. J. Public Health. 2020;42(4):712–716. doi:10.1093/pubmed/fdaa155

16. Dolan, P.: Modeling valuations for EuroQol health states. Medical care, pp. 1095–1108, (1997)10.1097/00005650-199711000-000029366889

17. National Institute for Health and Care Excellence (NICE), "Guide to the Methods of Technology Appraisal," (2013). [Online]. Available: https://www.nice.org.uk/process/pmg9/27905712

18. Stolk, E.: 11th Joint Call EuroQol Working Groups. EuroQol Reserach Foundation (2021)

19. Herdman M. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual. Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

20. Webb EJ, Kind P, Meads D, Martin A. Does a health crisis change how we value health?. Health Econ. 2021;30(10):2547–2560. doi:10.1002/hec.4399

21. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi:10.1007/s40273-016-0404-1

22. Webb EJ, O’Dwyer J, Meads D, Kind P, Wright P. Transforming discrete choice experiment latent scale values for EQ-5D-3L using the visual analogue scale. Eur. J. Health Econ. 2020. doi:10.1007/s10198-020-011

23. Ridgeway, N., et al.: Toolkit for Weighting and Analysis of Nonequivalent Groups: A guide to the twang package (2021)

24. Park, N.: Analysis of population estimates tool for UK [Online] Available: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/analysisofpopulationestimatestoolforuk

25. Jordan RE, Adab P, Cheng K. COVID-19: risk factors for severe disease and death. BMJ Publishing Group. 2020. doi:10.1136/bmj.m1198

26. Esai Selvan M. Risk factors for death from COVID-19. Nat. Rev. Immunol. 2020;20(7):407–407. doi:10.1038/s41577-020-0351-0

27. Wolff D, Nee S, Hickey NS, Marschollek M. Risk factors for COVID-19 severity and fatality: a structured literature review. Infection. 2021;49(1):15–28. doi:10.1007/s15010-020-01509-1

28. Devlin NJ, Shah KK, Feng Y, Mulhern B, van Hout B. Valuing health-related quality of life: An EQ-5 D-5 L value set for England. Health Econ. 2018;27(1):7–22. doi:10.1002/hec.3564

29. Jaspal R, Breakwell GM. Social support, perceived risk and the likelihood of COVID-19 testing and vaccination: cross-sectional data from the United Kingdom. Curr. Psychol. 2022;41(1):492–504. doi:10.1007/s12144-021-01681-z

30. Phillips R. Perceived threat of COVID-19 attitudes towards vaccination, and vaccine hesitancy: a prospective longitudinal study in the UK. British J Health Psychol. 2022. doi:10.1111/bjhp.12606

31. Schneider CR. COVID-19 risk perception: a longitudinal analysis of its predictors and associations with health protective behaviours in the United Kingdom. J. Risk Res. 2021;24(3–4):294–313. doi:10.1080/13669877.2021.1890637

32. Makin AJ, Layton A. The global fiscal response to COVID-19: Risks and repercussions. Econ. Analysis Policy. 2021;69:340–349. doi:10.1016/j.eap.2020.12.016

33. Sheinson D, Dang J, Shah A, Meng Y, Elsea D, Kowal S. A cost-effectiveness framework for COVID-19 treatments for hospitalized patients in the United States. Adv. Ther. 2021;38(4):1811–1831. doi:10.1007/s12325-021-01654-5

34. Kim DD, Neumann PJ. Analyzing the cost effectiveness of policy responses for COVID-19: the importance of capturing social consequences. Med. Decis. Making. 2020;40(3):251–253. doi:10.1177/0272989X20922987

35. Reddy KP. Clinical outcomes and cost-effectiveness of COVID-19 vaccination in South Africa. Nat. Commun. 2021;12(1):1–10. doi:10.1038/s41467-021-26557-5

36. López-Valcárcel, B. G., Vallejo-Torres, L.: The costs of COVID-19 and the cost-effectiveness of testing. Appl. Econ. Analysis (2021)

37. National Audit Office, "Investigation into government procurement during the COVID-19 pandemic," (HC959 Session 2019–2021), (2020)

38. Raffle, A. E.: Screening the healthy population for COVID-19 is of unknown value, but is being introduced nationwide. BMJ, 371, (2020)10.1136/bmj.m443833214143

39. House of Commons Public Accounts Committee, "COVID-19: Government procurement and supply of Personal Protective Equipment," 2021.

40. Limb, M.: Covid-19: Private hospitals “fell well short” in delivering care during the pandemic, says report, ed: British Medical Journal Publishing Group (2021)10.1136/bmj.n247134625407

41. Webb, E. J., Kind, P.: Tracking the evolution of EQ-5D values due to demographic change over a 50-year period, presented at the Health Economists' Study Group 2022 Winter Workshop, Leeds, United Kingdom (2022). [Online]. Available: https://hesg.org.uk/wp-content/uploads/2021/11/Paper-and-Poster-Abstracts-HESG2022-Leeds.pdf.

42. Bonanad C. The effect of age on mortality in patients with COVID-19: a meta-analysis with 611,583 subjects. J. Am. Med. Dir. Assoc. 2020;21(7):915–918. doi:10.1016/j.jamda.2020.05.045

43. Mesas AE. Predictors of in-hospital COVID-19 mortality: A comprehensive systematic review and meta-analysis exploring differences by age, sex and health conditions. PLoS One. 2020;15(11):e0241742. doi:10.1371/journal.pone.0241742

44. Dowd JB. Demographic science aids in understanding the spread and fatality rates of COVID-19. Proc. Natl. Acad. Sci. 2020;117(18):9696–9698. doi:10.1073/pnas.2004911117

[^1]: [www.coronavirus.data.gov.uk](http://www.coronavirus.data.gov.uk).

[^2]: <https://api.coronavirus.data.gov.uk/v2/data?areaType=region&metric=cumCasesByPublishDateRate&metric=cumDeaths60DaysByDeathDateRate&format=csv> for regions of England. <https://api.coronavirus.data.gov.uk/v2/data?areaType=nation&metric=cumCasesByPublishDateRate&metric=cumDeaths60DaysByDeathDateRate&format=csv> for Scotland, Wales and Northern Ireland.

[^3]: <https://euroqol.org/eq-5d-instruments/eq-5d-5l-about/valuation-standard-value-sets/new-uk-eq-5d-5l-valuation-study_blog/> accessed 8/2/22.

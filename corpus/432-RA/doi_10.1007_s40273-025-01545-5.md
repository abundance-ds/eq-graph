---
project_id: "432-RA"
work_id: "doi:10.1007/s40273-025-01545-5"
doi: "10.1007/s40273-025-01545-5"
pmid: "41047448"
pmcid: "PMC12799685"
title: "The Influence of Perspective on the Valuation of the EQ-5D-Y-3L: A Comparison Using the OPUF Tool and a Discrete Choice Experiment"
journal: "Pharmacoeconomics"
publication_date: "2025-10-06"
volume: "44"
issue: "1"
authors:
  - name: "Jake Hitch"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Gayathri Kumar"
    affiliation_ids:
      - "Aff1"
      - "Aff3"
  - name: "Paul Schneider"
    affiliation_ids:
      - "Aff4"
      - "Aff5"
  - name: "Nancy Devlin"
    affiliation_ids:
      - "Aff6"
  - name: "Koonal Shah"
    affiliation_ids:
      - "Aff7"
  - name: "David Mott"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Office of Health Economics, 2nd Floor Goldings House, Hay’s Galleria, 2 Hay’s Lane, London, SE1 2HB UK"
  - id: "Aff2"
    name: "Nuffield Department of Primary Care Health Sciences, University of Oxford, Oxford, UK"
  - id: "Aff3"
    name: "The Health Economics Unit (Hosted by NHS Midlands and Lancashire), London, UK"
  - id: "Aff4"
    name: "Sheffield Centre for Health and Related Research, The University of Sheffield, Sheffield, UK"
  - id: "Aff5"
    name: "Valorem Health, Bochum, Germany"
  - id: "Aff6"
    name: "School of Population and Global Health, The University of Melbourne, Melbourne, Australia"
  - id: "Aff7"
    name: "National Institute for Health and Care Excellence (NICE), London, UK"
licence: "cc-by-nc"
source_file: "input/projects/432-RA/papers/doi_10.1007_s40273-025-01545-5.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12799685/fullTextXML"
source_method: "epmc_xml"
source_sha256: "bf2842b609b80d1520cd81973f4cc4d8a2d2f3aa90502d6f6239654cd9da6adc"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The Influence of Perspective on the Valuation of the EQ-5D-Y-3L: A Comparison Using the OPUF Tool and a Discrete Choice Experiment

## Abstract

### Background

The choice of perspective in valuation tasks is likely to affect the scale of EQ-5D-Y-3L value sets, but less is known about how it affects the relative importance of different dimensions.

### Objectives

The aim of this study was to examine how preferences for EQ-5D-Y-3L health states differ according to different perspectives utilising two methods: the Online elicitation of Personal Utility Functions (OPUF) tool and a discrete choice experiment (DCE).

### Methods

An online survey was designed containing the OPUF tool and a DCE. Adult respondents from the United Kingdom were randomised to one of five different perspective arms: (1) 4-year-old child, (2) 10-year-old child, (3) a child of unspecified age, (4) another adult, and (5) own health. The resulting OPUF value sets (social utility functions), and relative importance scores for the five dimensions from both methods, were compared across perspectives.

### Results

Results differed by perspective in both valuation tasks. In both tasks, ‘looking after myself’ was less important and ‘pain or discomfort’ was more important in the child perspectives than in the adult perspectives. Furthermore, the scale of the value sets produced by the OPUF tool differed by perspective, with the value of the worst health state being significantly lower in the adult perspectives than in the child perspectives.

### Conclusion

Our results suggest that the valuation of the EQ-5D-Y-3L is affected by the perspective that adult respondents are asked to take. Researchers should be aware of the potential impact and ensure that relevant stakeholders understand this when designing valuation studies.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40273-025-01545-5.

Received 2025 Apr 11; Accepted 2025 Sep 17; Issue date 2026.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| This study found that adults value health problems on the EQ-5D-Y-3L differently depending on whether they imagine them happening to themselves, another adult, or a child. |
| When imagining a child, adults placed more importance on pain/discomfort and less on self-care (labelled as ‘looking after myself’ on the EQ-5D-Y-3L) and rated the worst health states as less severe than when imagining themselves or other adults. |
| These findings suggest that the perspective adults are asked to take can significantly affect how child health is valued, which may affect EQ-5D-Y-3L value sets and, ultimately, funding decisions about healthcare for children and adolescents. |

</div>

## Introduction

A substantial body of evidence indicates that society values adult health differently from child health \[1\]. Furthermore, preferences for different aspects of health can vary according to whether the individual is an adult or a child \[2, 3\]. As a result, assessing the cost-effectiveness of health interventions for child and adolescent patient populations requires accurate and reliable evidence on their health-related quality of life (HRQoL) impacts, alongside value sets that reflect these age-specific preferences.

The EQ-5D-Y-3L is a generic instrument that has been developed to measure HRQoL in child/adolescent populations, with the self-report version suitable for use in those aged between 8 and 15 years, and a proxy version available for use in those aged between 4 and 8 years. It comprises the following five dimensions: mobility; usual activities; self-care (looking after myself); having pain or discomfort; and feeling worried, sad, or unhappy. Each dimension has three severity levels: no problems, some problems, and a lot of problems. An international valuation protocol exists for the EQ-5D-Y-3L \[4\], and value sets have been produced for a wide range of different countries in recent years \[5–15\]. The valuation protocol recommends using a discrete choice experiment (DCE)—without duration or using dead as an alternative—to identify the relative importance (RI) of the dimensions and levels. The latent coefficients from the DCE are then anchored using data from a composite time trade-off (cTTO) exercise (conducted separately) onto the 0–1 dead–full health scale. This anchoring is required to construct the value set, which can then be used to estimate quality-adjusted life years (QALYs) for economic evaluation \[16\].

Given the wide range of normative decisions that need to be made when valuing instruments in this context, the valuation protocol was intended to be used as a starting point, and naturally there has since been much discussion around the appropriate methods for valuing the EQ-5D-Y-3L and child/adolescent instruments more generally \[17–20\]. For example, the protocol recommends that adults are sampled and asked to take the perspective of a 10-year-old child in the choice tasks. It is not a given that adults must take this perspective (or indeed, that adults’ preferences should be elicited at all) \[21\]. However, if we assume that adults’ preferences are to be elicited, there are many different options for the choice of perspective. Adults could imagine themselves at their current age, themselves at a younger age, another adult (either of the same age as them, or at another age, if specified at all), a hypothetical child/adolescent of unspecified age, or a child/adolescent of a specified age. The choice of perspective could theoretically affect preferences, the resulting utilities, and ultimately incremental cost-per-QALY ratios of health technologies \[20\].

A small set of studies has investigated the effect of different perspectives on EQ-5D-Y-3L values using different methods. Ramos-Goñi et al. \[22\] analysed the effects of changing the age of the ‘reference child’ that adult respondents were asked to consider when completing a DCE. They included five perspectives: own health (adult), child aged 5–7 years, child aged 8–10 years, child aged 11–13 years, and child aged 14–15 years. They found that changing the age of the reference child had a minimal impact on the RI of the five dimensions. Other studies have sought to explore the impact of perspective on cTTO values and have typically identified differences in values. Shah et al. \[23\] found that adult respondents typically provided lower values when valuing from their own perspective than when they were asked to consider the views of a 10-year-old child. Lipman et al. \[24\] also explored potential differences using four perspectives: own health (adult), other adult (of the same age as the respondent), themselves as a 10-year-old child, and another child aged 10 years. They found small and variable differences in values, with higher valuations for some health states when respondents are required to make decisions using a proxy perspective. Dewilde et al. \[25\] also examined differences in cTTO valuations in a mixed-methods study using two proxy perspectives: an 8-year-old child and a 40-year-old adult. They found that the child valuations were, on average, higher than the adult valuations. Their qualitative research highlighted that many people consider child life-years to be more precious than adult life-years and that the same health state has different implications for adults than for children. Finally, Powell et al. \[26\] looked at differences by perspective using both cTTO and DCE in a qualitative study. They found that people had a different willingness to trade-off life-years for a 10-year-old child than for themselves or another adult.

Given the mixed evidence to date on the impact of perspective, we set out to explore the effects of five different perspectives on the valuation of the EQ-5D-Y-3L. Unlike past studies, which have focused either on the RI of dimensions (via DCE) or on mean values for a small number of health states (via cTTO), we sought to explore the impact of perspective on complete value sets. To achieve this, we utilised the online personal utility functions (OPUF) tool introduced by Schneider et al. \[27\] and based upon earlier work by Devlin et al. \[28\]. The OPUF tool enables full value sets (social utility functions) to be produced with small sample sizes, and to date there are no published studies reporting the use of the OPUF tool to value a child/adolescent HRQoL instrument. In addition, we included a DCE in our OPUF survey to enable comparisons with prior studies and to explore whether differences in perspective were similar between the two methods.

## Methods

### Study Overview

The study was conducted using an online survey containing the OPUF tool, adapted for the EQ-5D-Y-3L instrument, as well as a DCE task. The ordering of the two tasks in the survey was randomised to minimise ordering bias in the results. There were five different survey arms (one for each perspective under study), and the survey questions were adapted accordingly to reflect the relevant perspective.

### The Perspectives and Study Participants

Table <a href="#Tab1" data-ref-type="table">1</a> details the five different perspectives used in the study with example wording from the DCE task, along with the target sample sizes for each arm. The 10-year-old child perspective was included as it is used in the international valuation protocol for the EQ-5D-Y-3L \[4\]. The 4-year-old child perspective was included as this is the youngest age for which the EQ-5D-Y-3L is suitable (via a proxy version). The child of unspecified age perspective was included to explore whether preferences differ from when an age is specified. The other adult perspective was included to explore the extent to which differences in preferences may relate to taking a proxy perspective in general (i.e., adult or child), compared with a child proxy perspective. Finally, the adult self-perspective was included as a general (non-proxy) comparator.

<div id="Tab1" class="table-wrap">

<div class="caption">

The perspectives under study

</div>

| Perspective | Wording | Target sample size |
|----|----|----|
| 4-year-old child | “Considering your views about a 4-year-old child, which scenario would you choose for them?” | 300 |
| 10-year-old child | “Considering your views about a 10-year-old child, which scenario would you choose for them?” | 1000 |
| Child (unspecified age) | “Considering your views about a child, which health state would you choose for them?” | 300 |
| Other adult | “Considering your views about a typical person of the same age as you, which health state would you choose for them?” | 300 |
| Adult self | “Which health state do you prefer?” | 300 |

</div>

Participants in the study were adult members (aged ≥ 18 years) of the UK general population. Quotas were used to obtain a representative sample in relation to age, gender, and ethnicity. The total target sample size was 2200 participants. A target sample size of 300 per survey arm was felt to be sufficient to obtain reliable results for both the OPUF and the DCE components of the survey to explore differences in preferences by perspective. Of the two methods, DCEs require larger sample sizes, and a sample size of 300 for a relatively small descriptive system such as the EQ-5D-Y-3L aligns with commonly cited rules of thumb and published recommendations \[29–31\]. By comparison, the OPUF tool has been successfully implemented with sample sizes as low as 50 and 122 \[27, 32\]. However, for the 10-year-old child arm, the target sample size was inflated to the recommended sample size (for the DCE component) set out in the valuation protocol (n=1000) to enable additional analyses to be conducted (to be reported elsewhere).

Before launching the surveys, two experienced researchers (JH and GK) conducted 10 pre-testing interviews to test the feasibility and comprehension of the survey instrument. The only changes that were made based on the results of the pre-testing interviews were small changes to the wording and formatting of the survey questions. All study participants were recruited online via a panel company called Prolific. Those who successfully completed the pre-testing interviews or survey were compensated for their time in line with Prolific’s guidance on participant reimbursement.

### Stated-Preference Methods

#### The OPUF Tool

The personal utility function approach was introduced as a more direct and reflective valuation method than existing alternatives \[28\] and has recently been developed as an online tool (OPUF) \[27\]. Unlike traditional preference-elicitation methods, OPUF is compositional, meaning that it directly elicits partial values from respondents rather than decomposing partial values from choices between complete health states, as is the case in a DCE. The version of the OPUF tool used in this study consisted of five main steps.

1.  **Dimension ranking:** Participants were asked to rank the five dimensions (described using the worst levels, i.e., level 3) in terms of importance.

2.  **Dimension weighting:** In this swing-weighting exercise, the change in the most important dimension (ranked \#1 in the ranking) from ‘no problems’ to ‘a lot of problems’ was assigned a fixed weight of 100 points. For each of the four dimensions that the respondent ranked 2–5 in the dimension ranking, participants rated the improvement from the worst to best level on that dimension compared with the most important dimension, assigning a weight between 0 and 100 points.

3.  **Level rating:** For each dimension, participants were asked to rate intermediate health problems (e.g., some problems, or level 2) on a scale from 0 to 100, where 100 = no problems and 0 = a lot of problems. Level 1 (no problems) and level 3 (a lot of problems) were fixed at 100 and 0, respectively.

4.  **Anchoring task:** Participants were first asked whether the worst health state (33333) was better than ‘being dead’. If participants selected that 33333 was better than ‘being dead’, they were asked to rate 33333 on a scale between ‘no health problems’ and ‘being dead’. If participants selected that ‘being dead’ was better than 33333, they were asked to rate ‘being dead’ on a scale between ‘no health problems’ and 33333. This is referred to hereafter as the ‘anchoring-visual analogue scale (VAS)’ task.

The OPUF tool has potential advantages over other valuation methods. First, as OPUF can produce individual-level utility functions, it allows for a more thorough examination of heterogeneity in preferences \[27\]. OPUF also has relatively high statistical power, meaning that fewer participants are needed to derive a value set \[27\].

#### DCE Methodology

The DCE component of the survey follows the EQ-5D-Y-3L valuation protocol (i.e., uses the same experimental design; see Ramos-Goñi et al. \[4\] for further details). In summary, participants were presented with a set of pairs of EQ-5D-Y-3L health states and asked to choose which one they would prefer, either for themselves or for the relevant child or adult. Each participant was asked to complete 15 choice tasks. Figure <a href="#Fig1" data-ref-type="fig">1</a> is an example choice task using the 10-year-old child proxy perspective.

<figure id="Fig1">
<p><img src="40273_2025_1545_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40273_2025_1545_Fig1_HTML.gif" /></p>
<figcaption>Example EQ-5D-Y-3L discrete-choice experiment (DCE) choice task</figcaption>
</figure>

### Analysis

#### Analysis of OPUF Data

We used the OPUF data to create five EQ-5D-Y-3L value sets, one for each perspective under study. Equation <a href="#Equ1" data-ref-type="disp-formula">1</a> shows how dimension- and level-specific disutilities for a given participant were calculated from the responses to the dimension weighting, level rating, and the anchoring task.

``` math
c_{\mathit{ijm}} = \frac{\left( {1 - \frac{l_{\mathit{ijm}}}{100}} \right) \cdot w_{\mathit{im}}}{\sum_{k = 1}^{n}\left( w_{\mathit{km}} \right)} \cdot f(a),
```

$`c_{\mathit{ijm}}`$ refers to the disutility for the $`j`$ th level on dimension $`i`$ for participant $`m`$. Accordingly, $`l_{\mathit{ijm}}`$ refers to the rating for level $`j`$ on dimension $`i`$ for participant $`m`$; $`w_{\mathit{im}}`$ refers to the weight for dimension $`i`$ for participant $`m`$; $`w_{\mathit{km}}`$ refers to the weight for dimension $`k`$ (any dimension) for participant $`m`$; $`n`$ refers to the number of dimensions, which in our case is five; and $`f(a)`$ refers to the anchoring factor (see below). Note that $`\sum_{k = 1}^{n}\left( w_{\mathit{km}} \right)`$ is simply the sum of all dimension weights for participant $`m`$, used to rescale the values on the full health to dead scale.

The specification of the anchoring factor is dependent on whether the participant prefers 33333 over being dead, or vice versa. The anchoring factor is given by Equation <a href="#Equ2" data-ref-type="disp-formula">2</a>.

``` math
f(a) = \left\{ \begin{matrix}
{33333\underline{\succ}dead,} & \left( {1 - v_{\mathit{worst}}} \right)^{- 1} \\
{33333\underline{\prec}dead,} & {1 - v_{\mathit{dead}}}
\end{matrix} \right),
```

where $`v_{\mathit{dead}}`$ is the position of ‘being dead’ on a scale of 0 to 1, anchored at full health (= 1) and the worst health state (= 0); and $`v_{\mathit{worst}}`$ is the rating of position of the worst health state on a scale of 0 to 1, anchored at full health (= 1) and dead (= 0). As extreme responses to the former task could lead to the value of the worst state being as low as − 99, responses were censored at − 1. Participants were dropped from the OPUF analysis (and subsequently excluded from the DCE analysis) if they provided a value of 1 for either 33333 or being dead.

To summarise the RI score of the EQ-5D-Y-3L attributes, we first calculated the social utility decrements for each dimension-level pair (denoted as $`\beta_{MO3}`$, for example, for mobility level 3) as the mean of the participant-level decrements for that pair ($`c_{\mathit{ijm}}`$ above). We then calculated the percentage contribution that each dimension makes to the total social utility decrement associated with the worst possible health state (33333) compared with the best possible health state (11111). An example for the RI of mobility is given by Equation <a href="#Equ3" data-ref-type="disp-formula">3</a>, where *MO* refers to ‘mobility’, *LAM* refers to ‘looking after myself’, *UA* refers to ‘usual activities’, *PD* refers to ‘pain or discomfort’, and *WSU* refers to ‘worried, sad or unhappy’. This assumes that the level 3 coefficient is greater in absolute terms than the level 2 coefficients, which is forced to be the case in the OPUF tool (but is not guaranteed in a DCE). We generated 95% confidence intervals using bootstrapping.

``` math
RI_{\mathit{MO}} = \frac{\beta_{MO3}}{\beta_{MO3} + \beta_{LAM3} + \beta_{UA3} + \beta_{PD3} + \beta_{WSU3}}{} \times {}100{}
```

#### Analysis of DCE data

The DCE data were analysed using conditional logit models. The indirect utility function was specified to be a linear additive function of a set of dummy variables for levels 2 and 3 of each of the five EQ-5D-Y-3L dimensions, as in Eq. <a href="#Equ4" data-ref-type="disp-formula">4</a>.

``` math
\begin{matrix}
{V_{\mathit{ni}} = \beta_{1}MO2_{\mathit{ni}} + \beta_{2}MO3_{\mathit{ni}} + \beta_{3}LAM2_{\mathit{ni}} + \beta_{4}LAM3_{\mathit{ni}} + \beta_{5}UA2_{\mathit{ni}}} \\
{+ \beta_{6}UA3_{\mathit{ni}} + \beta_{7}PD2_{\mathit{ni}} + \beta_{8}PD3_{\mathit{ni}} + \beta_{9}WSU2_{\mathit{ni}} + \beta_{10}WSU3_{\mathit{ni}}.}
\end{matrix}
```

The DCE data are not anchored on the full health to dead scale. Instead, we summarised the RI scores for the EQ-5D-Y-3L dimensions in the same manner as the OPUF analysis (Eq. <a href="#Equ3" data-ref-type="disp-formula">3</a>). We generated 95% confidence intervals using the Delta method \[33\]. Additionally, a pooled model was also estimated containing ten interaction terms for four perspectives, with the 10-year-old child perspective as the baseline, to further explore the differences between perspectives in the DCE.

### Ethical Approval

Ethical approval was received from the City, University of London School of Social Sciences Research Ethics Committee (ETH2223-1011).

## Results

Table <a href="#Tab2" data-ref-type="table">2</a> summarises the demographic characteristics of respondents in each study arm. The final sample size was 2080. A total of 121 respondents were dropped from the study because they provided extreme responses in the OPUF tool (i.e., either rating 33333 or ‘being dead’ at a value of 100 in the anchoring-VAS task). The proportion of respondents dropped by study arm varied slightly (between 3 and 7%; see Table <a href="#MOESM1" data-ref-type="supplementary-material">S1</a> in the electronic supplementary material \[ESM\]).

<div id="Tab2" class="table-wrap">

<div class="caption">

Demographic characteristics by perspective

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristic</th>
<th style="text-align: left;">(1) 4-year-old child</th>
<th style="text-align: left;">(2) 10-year-old child</th>
<th style="text-align: left;">(3) Child (unspecified age)</th>
<th style="text-align: left;">(4) Other adult</th>
<th style="text-align: left;">(5) Adult self</th>
<th style="text-align: left;"><em>p</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">Gender</td>
<td style="text-align: left;">0.85</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">140 (50.2)</td>
<td style="text-align: left;">481 (50.8)</td>
<td style="text-align: left;">143 (50.4)</td>
<td style="text-align: left;">147 (50.5)</td>
<td style="text-align: left;">145 (51.8)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">138 (49.5)</td>
<td style="text-align: left;">457 (48.3)</td>
<td style="text-align: left;">136 (47.9)</td>
<td style="text-align: left;">143 (49.1)</td>
<td style="text-align: left;">134 (47.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;">5 (0.5)</td>
<td style="text-align: left;">3 (1.1)</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to say</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;">3 (0.3)</td>
<td style="text-align: left;">2 (0.7)</td>
<td style="text-align: left;">1 (0.3)</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Age, years</td>
<td style="text-align: left;">0.84</td>
</tr>
<tr>
<td style="text-align: left;"> 18–29</td>
<td style="text-align: left;">52 (18.6)</td>
<td style="text-align: left;">190 (20.1)</td>
<td style="text-align: left;">55 (19.4)</td>
<td style="text-align: left;">55 (18.9)</td>
<td style="text-align: left;">56 (20)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td style="text-align: left;">54 (19.4)</td>
<td style="text-align: left;">173 (18.3)</td>
<td style="text-align: left;">56 (19.7)</td>
<td style="text-align: left;">50 (17.2)</td>
<td style="text-align: left;">51 (18.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td style="text-align: left;">52 (18.6)</td>
<td style="text-align: left;">168 (17.8)</td>
<td style="text-align: left;">38 (13.4)</td>
<td style="text-align: left;">54 (18.6)</td>
<td style="text-align: left;">43 (15.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td style="text-align: left;">42 (15.1)</td>
<td style="text-align: left;">178 (18.8)</td>
<td style="text-align: left;">56 (19.7)</td>
<td style="text-align: left;">62 (21.3)</td>
<td style="text-align: left;">50 (17.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 60–74</td>
<td style="text-align: left;">73 (26.2)</td>
<td style="text-align: left;">220 (23.3)</td>
<td style="text-align: left;">72 (25.4)</td>
<td style="text-align: left;">65 (22.3)</td>
<td style="text-align: left;">75 (26.8)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 75</td>
<td style="text-align: left;">6 (2.2)</td>
<td style="text-align: left;">16 (1.7)</td>
<td style="text-align: left;">6 (2.1)</td>
<td style="text-align: left;">3 (1)</td>
<td style="text-align: left;">5 (1.8)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to say</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;">1 (0.1)</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;">2 (0.7)</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Country</td>
<td style="text-align: left;">0.42</td>
</tr>
<tr>
<td style="text-align: left;"> England</td>
<td style="text-align: left;">236 (84.6)</td>
<td style="text-align: left;">817 (86.4)</td>
<td style="text-align: left;">241 (84.9)</td>
<td style="text-align: left;">240 (82.5)</td>
<td style="text-align: left;">232 (82.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Scotland</td>
<td style="text-align: left;">20 (7.2)</td>
<td style="text-align: left;">75 (7.9)</td>
<td style="text-align: left;">19 (6.7)</td>
<td style="text-align: left;">27 (9.3)</td>
<td style="text-align: left;">32 (11.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Wales</td>
<td style="text-align: left;">13 (4.7)</td>
<td style="text-align: left;">34 (3.6)</td>
<td style="text-align: left;">12 (4.2)</td>
<td style="text-align: left;">16 (5.5)</td>
<td style="text-align: left;">12 (4.3)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Northern Ireland</td>
<td style="text-align: left;">10 (3.6)</td>
<td style="text-align: left;">17 (1.8)</td>
<td style="text-align: left;">11 (3.9)</td>
<td style="text-align: left;">7 (2.4)</td>
<td style="text-align: left;">4 (1.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to say</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;">3 (0.3)</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;">1 (0.3)</td>
<td style="text-align: left;">0 (0)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Educated beyond minimum schooling age</td>
<td style="text-align: left;">0.50</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">32 (11.5)</td>
<td style="text-align: left;">115 (12.2)</td>
<td style="text-align: left;">43 (15.1)</td>
<td style="text-align: left;">43 (14.8)</td>
<td style="text-align: left;">35 (12.5)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes (no degree)</td>
<td style="text-align: left;">71 (25.4)</td>
<td style="text-align: left;">258 (27.3)</td>
<td style="text-align: left;">79 (27.8)</td>
<td style="text-align: left;">77 (26.5)</td>
<td style="text-align: left;">79 (28.2)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Yes (has a degree)</td>
<td style="text-align: left;">175 (62.7)</td>
<td style="text-align: left;">565 (59.7)</td>
<td style="text-align: left;">158 (55.6)</td>
<td style="text-align: left;">165 (56.7)</td>
<td style="text-align: left;">165 (58.9)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to say</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;">8 (0.9)</td>
<td style="text-align: left;">4 (1.4)</td>
<td style="text-align: left;">6 (2.0)</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Experience of having regular responsibility for children (past or present)</td>
<td style="text-align: left;">0.36</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">153 (54.8)</td>
<td style="text-align: left;">531 (56.1)</td>
<td style="text-align: left;">158 (55.6)</td>
<td style="text-align: left;">142 (48.8)</td>
<td style="text-align: left;">157 (56.1)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">125 (44.8)</td>
<td style="text-align: left;">403 (42.6)</td>
<td style="text-align: left;">124 (43.7)</td>
<td style="text-align: left;">145 (49.8)</td>
<td style="text-align: left;">122 (43.6)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Prefer not to say</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;">12 (1.3)</td>
<td style="text-align: left;">2 (0.7)</td>
<td style="text-align: left;">4 (1.4)</td>
<td style="text-align: left;">1 (0.4)</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><em>N</em></td>
<td style="text-align: left;">279</td>
<td style="text-align: left;">946</td>
<td style="text-align: left;">284</td>
<td style="text-align: left;">291</td>
<td style="text-align: left;">280</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

*p*-values are from Pearson’s chi-squared tests

Data are presented as *n* (%) unless otherwise indicated

</div>

Overall, the characteristics of each sample were very similar in terms of the main demographics. There were slightly more females than males in each study arm, and more than half of respondents in each study arm had a degree. Around half of respondents in each sample reported having experience of having regular responsibility for children, either at the time of completing the survey or in the past.

Table <a href="#Tab3" data-ref-type="table">3</a> provides the five OPUF value sets, by perspective. The coefficients are anchored on the full health to dead scale. The most substantial differences between the child and adult perspectives can be seen in relation to the ‘looking after myself’ dimension. The utility of the worst health state (33333) is generally higher for the three child perspectives (ranging from 0.198 to 0.262) than for the two adult perspectives (0.158–0.183). The utility of 33333 is highest for the 10-year-old child perspective (0.262) and lowest for the adult self-perspective (0.158). The percentage of respondents saying that 33333 is worse than dead is generally lower for the child perspectives (range 17.7–25.0%) than the adult perspectives (range 25.4–31.8%). The percentage choosing dead over 33333 is highest by some margin for the adult self-perspective. Tables S2 and S3 in the ESM provide summary statistics on the dimension weighting and level rating components of the OPUF tool. Figure <a href="#MOESM1" data-ref-type="supplementary-material">S1</a> in the ESM illustrates the value sets, highlighting that the utilities are generally higher for the child perspectives than the adult perspectives.

<div id="Tab3" class="table-wrap">

<div class="caption">

Online elicitation of Personal Utility Functions (OPUF) EQ-5D-Y-3L value sets for five child and adult perspectives

</div>

| Variable | \(1\) 4-year-old child | \(2\) 10-year-old child | \(3\) Child (unspecified age) | \(4\) Other adult | \(5\) Adult self |
|----|----|----|----|----|----|
| Mobility: Level 2 | − 0.072 (− 0.079 to − 0.065) | − 0.069 (− 0.073 to − 0.066) | − 0.073 (− 0.080 to − 0.066) | − 0.076 (− 0.082 to − 0.070) | − 0.078 (− 0.087 to − 0.070) |
| Mobility: Level 3 | − 0.155 (− 0.167 to − 0.143) | − 0.146 (− 0.151 to − 0.141) | − 0.157 (− 0.169 to − 0.146) | − 0.156 (− 0.168 to − 0.145) | − 0.161 (− 0.174 to − 0.149) |
| Looking after myself: Level 2 | − 0.056 (− 0.063 to − 0.050) | − 0.056 (− 0.059 to − 0.053) | − 0.058 (− 0.063 to − 0.052) | − 0.071 (− 0.078 to − 0.065) | − 0.078 (− 0.087 to 0.070) |
| Looking after myself: Level 3 | − 0.120 (− 0.132 to − 0.109) | − 0.117 (− 0.122 to − 0.113) | − 0.126 (− 0.136 to − 0.117) | − 0.148 (− 0.160 to − 0.137) | − 0.154 (− 0.169 to − 0.139) |
| Usual activities: Level 2 | − 0.071 (− 0.077 to − 0.065) | − 0.068 (− 0.071 to − 0.064) | − 0.07 (− 0.077 to − 0.064) | − 0.076 (− 0.084 to − 0.069) | − 0.075 (− 0.083 to − 0.067) |
| Usual activities: Level 3 | − 0.153 (− 0.164 to − 0.143) | − 0.141 (− 0.147 to − 0.136) | − 0.154 (− 0.165 to − 0.143) | − 0.158 (− 0.170 to − 0.147) | − 0.156 (− 0.168 to − 0.144) |
| Pain or discomfort: Level 2 | − 0.099 (− 0.109 to − 0.089) | − 0.088 (− 0.093 to − 0.083) | − 0.1 (− 0.112 to − 0.089) | − 0.088 (− 0.095 to − 0.080) | − 0.093 (− 0.103 to − 0.083) |
| Pain or discomfort: Level 3 | − 0.199 (− 0.215 to − 0.185) | − 0.180 (− 0.186 to − 0.173) | − 0.201 (− 0.216 to − 0.186) | − 0.182 (− 0.194 to − 0.169) | − 0.192 (− 0.208 to − 0.176) |
| Worried, sad or unhappy: Level 2 | − 0.076 (− 0.084 to − 0.068) | − 0.073 (− 0.077 to − 0.069) | − 0.081 (− 0.089 to − 0.073) | − 0.086 (− 0.094 to − 0.077) | − 0.083 (− 0.094 to − 0.072) |
| Worried, sad or unhappy: Level 3 | − 0.170 (− 0.183 to − 0.157) | − 0.154 (− 0.160 to − 0.148) | − 0.164 (− 0.177 to − 0.152) | − 0.172 (− 0.186 to − 0.159) | − 0.179 (− 0.198 to − 0.162) |
| *N* | 279 | 946 | 284 | 291 | 280 |
| Mean utility of 33333 | 0.202 (0.451) | 0.262 (0.392) | 0.198 (0.445) | 0.183 (0.453) | 0.158 (0.508) |
| 33333 \< 0 (n; %)<sup>a</sup> | 52 (18.6) | 167 (17.7) | 71 (25.0) | 74 (25.4) | 89 (31.8) |
| 33333 = -1 (n; %) | 21 (7.5) | 33 (3.5) | 17 (6.0) | 20 (6.9) | 23 (8.2) |

For the coefficients, figures in parentheses are bootstrapped 95% confidence intervals; for the utility of 33333, figures in parentheses are standard deviations

<sup>a</sup>This is the percentage of respondents who chose being dead over 33333 for the respective child or adult

</div>

Table <a href="#Tab4" data-ref-type="table">4</a> shows the (unanchored) utilities from the conditional logit models estimated using the DCE data. Almost all coefficients are significantly different from zero at the 1% significance level. Only two coefficients are not statistically significant at the 95% level: level 2 of ‘looking after myself’ under the 4-year-old child perspective and level 2 of ‘mobility’ under the other adult perspective. Direct comparisons of coefficients between perspectives were avoided because of potential differences in scale between samples, which can be addressed by focusing on RI scores.

<div id="Tab4" class="table-wrap">

<div class="caption">

Discrete choice experiment (DCE) choice models for five child and adult perspectives

</div>

| Variable | \(1\) 4-year-old child | \(2\) 10-year-old child | \(3\) Child (unspecified age) | \(4\) Other adult | \(5\) Adult self |
|----|----|----|----|----|----|
| Mobility: Level 2 | − 0.256\*\* (0.121) | − 0.496\*\*\* (0.0634) | − 0.368\*\*\* (0.126) | − 0.159\* (0.0919) | − 0.308\*\*\* (0.101) |
| Mobility: Level 3 | − 1.159\*\*\* (0.218) | − 1.266\*\*\* (0.106) | − 1.058\*\*\* (0.215) | − 1.114\*\*\* (0.150) | − 1.348\*\*\* (0.164) |
| Looking after myself: Level 2 | − 0.0949 (0.106) | − 0.279\*\*\* (0.0503) | − 0.323\*\*\* (0.0971) | − 0.593\*\*\* (0.0773) | − 0.466\*\*\* (0.0914) |
| Looking after myself: Level 3 | − 0.635\*\*\* (0.161) | − 1.048\*\*\* (0.0809) | − 0.957\*\*\* (0.157) | − 1.487\*\*\* (0.132) | − 1.509\*\*\* (0.150) |
| Usual activities: Level 2 | − 0.867\*\*\* (0.0907) | − 0.806\*\*\* (0.0512) | − 0.733\*\*\* (0.0940) | − 0.579\*\*\* (0.0770) | − 0.557\*\*\* (0.0808) |
| Usual activities: Level 3 | − 1.908\*\*\* (0.163) | − 1.877\*\*\* (0.0899) | − 1.668\*\*\* (0.165) | − 1.544\*\*\* (0.122) | − 1.500\*\*\* (0.138) |
| Pain or discomfort: Level 2 | − 1.137\*\*\* (0.119) | − 1.148\*\*\* (0.0565) | − 1.159\*\*\* (0.120) | − 0.574\*\*\* (0.0810) | − 0.691\*\*\* (0.0923) |
| Pain or discomfort: Level 3 | − 3.020\*\*\* (0.261) | − 2.819\*\*\* (0.120) | − 2.740\*\*\* (0.247) | − 1.949\*\*\* (0.154) | − 2.074\*\*\* (0.178) |
| Worried, sad or unhappy: Level 2 | − 0.952\*\*\* (0.102) | − 0.761\*\*\* (0.0510) | − 0.839\*\*\* (0.0954) | − 0.263\*\*\* (0.0708) | − 0.546\*\*\* (0.0791) |
| Worried, sad or unhappy: Level 3 | − 2.469\*\*\* (0.197) | − 2.208\*\*\* (0.0917) | − 2.294\*\*\* (0.174) | − 1.363\*\*\* (0.125) | − 1.777\*\*\* (0.136) |
| *N* | 8370 | 28,368 | 8518 | 8728 | 8398 |
| Log Likelihood | − 1358 | − 5228 | − 1536 | − 2202 | − 2013 |

Robust standard errors in parentheses

<sup>\*\*\*</sup>*p* \< 0.01, \*\**p* \< 0.05, \**p* \< 0.1

</div>

Figure <a href="#Fig2" data-ref-type="fig">2</a>a shows the RI scores for the EQ-5D-Y-3L for the OPUF data, by perspective. Regardless of perspective, the difference in RI scores between dimensions is not substantial and, for three of the five dimensions (‘mobility’, ‘usual activities’, and ‘worried, sad or unhappy’), RI scores are all close to 20%. The largest gap between any two dimensions is around 10 percentage points (‘looking after myself’ and ‘pain or discomfort’ in the 4-year-old child perspective). However, there is a similar pattern between these two dimensions across all perspectives. ‘Pain or discomfort’ is the most important dimension, and ‘looking after myself’ is the least important dimension across all perspectives. However, ‘looking after myself’ is less important under the child perspectives than under the adult perspectives, with the opposite effect occurring for ‘pain or discomfort’. There is relatively little variation between the different child perspectives, or between the adult perspectives, within dimensions.

<figure id="Fig2">
<p><img src="40273_2025_1545_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2025_1545_Fig2_HTML.gif" /></p>
<figcaption>Relative importance of EQ-5D-Y-3L dimensions: <strong>a</strong> online elicitation of Personal Utility Functions (OPUF) and <strong>b</strong> discrete choice experiment (DCE)</figcaption>
</figure>

Figure <a href="#Fig2" data-ref-type="fig">2</a>b shows the RI scores for the EQ-5D-Y-3L for the DCE data, by perspective. The RI scores estimated from the DCE data had wider confidence intervals than those from the OPUF data, due to the comparatively greater statistical precision of the latter. There is considerably more variation in the RI scores between and within dimensions than in the OPUF RI scores. Regarding the former, the greatest range between dimensions (within a particular perspective) is around 26 percentage points compared with 10 with the OPUF data (between ‘looking after myself’ and ‘pain or discomfort’ in the 4-year-old child perspective in both cases).

In all the child perspectives, ‘looking after myself’ is the least important dimension (as was the case with the OPUF RI scores). Furthermore, it is less important in the 4-year-old child perspective than in the other child perspectives. In contrast, in the adult perspectives, ‘mobility’ is the least important dimension (in contrast to ‘looking after myself’ in the OPUF RI scores). Across all perspectives, ‘pain or discomfort’ is the most important dimension, but it is less important in the adult perspectives than in the child perspectives (consistent with the OPUF RI scores). Furthermore ‘worried, sad or unhappy’ is less important in the adult perspectives than in the child perspectives. These differences are also seen in the pooled interaction model (Table S4 in the ESM).

## Discussion

In this study, we sought to explore whether the choice of perspective affects the results of EQ-5D-Y-3L valuation tasks using both the OPUF tool and a DCE. With both methods, differences were identified between the perspectives, but the extent of these differences varied.

In the component of the OPUF tool that explored the RI of the five dimensions, ‘looking after myself’ was consistently less important, and ‘pain or discomfort’ was consistently more important, for children than for adults. Other dimensions had similar levels of importance both within and between perspectives. In terms of the scale of the value sets produced, the child perspective value sets were narrower (with higher values for 33333) because a smaller proportion of respondents considered 33333 to be worse than dead when considering a child perspective (31.8% for the adult self-perspective was the highest, whereas the lowest was 17.7% for the 10-year-old child perspective). In relation to scale, there were some differences within the different child and adult arms. Although 33333 was considered worse than dead by a similar proportion for the 4-year-old and 10-year-old child perspectives (18.6% and 17.7%, respectively), 25% of respondents taking the perspective of a child of unspecified age considered 33333 to be worse than dead. Furthermore, a greater proportion of respondents in the adult self-perspective arm considered 33333 to be worse than dead than in the other adult arm (31.8% vs. 25.4%).

The DCE only provided RI results, but these were considerably more varied than those from the OPUF tool, both within and between dimensions. Similar to the OPUF results, ‘looking after myself’ was consistently less important and ‘pain or discomfort’ was consistently more important in the child perspectives than in the adult perspectives (though to a far greater extent in terms of RI scores). There were also further differences, such as ‘worried, sad or unhappy’ being less important for adults and ‘looking after myself’ being less important under a 4-year-old child perspective than under the other child perspectives.

The OPUF-derived EQ-5D-Y-3L value sets suggest that adult respondents valued child health states somewhat higher when they imagined children experiencing these health states as opposed to another adult or themselves. This is the first study to explore differences by perspective using OPUF, but past studies using cTTO have found similar results \[23, 25, 26\]. Given that the OPUF anchoring-VAS task was based on a direct choice (between 33333 and dead) followed by a rating scale, our results cannot be explained in the same way as those from the literature (i.e., that adult respondents are less willing to trade-off life-years on behalf of children than they are for adults). Our results suggest that adults are also relatively hesitant to state that, for a child, being dead is better than being in 33333 (the first part of the task), pointing towards death aversion in this context. However, it is also worth noting that the value sets were still relatively narrow in the adult perspectives in our study, compared with value sets for adult instruments (e.g., EQ-5D-3L or EQ-5D-5L). It is unclear whether this is driven by the method (e.g., the direct nature of the first anchoring-VAS question, and/or the lack of a temporal component) or whether 33333 on the EQ-5D-Y-3L is genuinely viewed as being better than dead by most adults when considering an adult perspective. Although this is typically not the case for 33333 in EQ-5D-3L value sets, or 55555 in EQ-5D-5L value sets, the significant differences in language between these instruments and the EQ-5D-Y-3L may partly explain these differences. For example, ‘anxiety/depression’ in the EQ-5D-3L/EQ-5D-5L is labelled as ‘worried, sad or unhappy’ in the EQ-5D-Y-3L, which may create less concern.

In our study, the RI of three of the EQ-5D-Y-3L dimensions (‘looking after myself’, ‘pain or discomfort’, and ‘worried, sad or unhappy’) appeared to depend on whether a child or adult perspective was taken, irrespective of the method used. The ‘looking after myself’ differences may be explained by the fact that children are already relatively dependent on their parents/guardians, so changes relating to self-care are less important than for independent adults. The ‘pain or discomfort’ differences may be because people have a stronger aversion to imagining pain or discomfort being experienced by children than by themselves, and perhaps also because they perceive adults as having a greater tolerance of pain and discomfort. The ‘worried, sad or unhappy’ differences may also be explained by people having a stronger aversion to imagining children feeling this way. It may also be the case that, although this wording may feel appropriate in the child perspectives, it may seem less severe (than anxiety/depression, for example) when adults are considering this dimension for themselves or other adults. Regardless of the reasons for these differences, the consistency in our results suggests that the choice between an adult or a child perspective may affect the RI of different dimensions of health in valuation studies. Researchers should consider this, in addition to the expected impact on the scale of the value sets, and the consequences for the generation of QALYs and, ultimately, reimbursement decisions \[18\].

The DCE results in our study go one step further and suggest that ‘looking after myself’ is perceived, by adults, to be less important for younger children than for older children. This may be because younger children are relatively more dependent on their parents/guardians than older children. Although this is not directly supported by the OPUF results, it is worth noting that the variation in the RI of the dimensions in the OPUF task was far more limited overall, perhaps due to its nature (a single swing-weighting exercise vs. a series of 15 forced-choice tasks).

Our RI results are in direct contrast to those of Ramos-Goni et al. \[22\], who found no substantial differences in DCE results between a range of different perspectives, which included an adult self-perspective as well as four different child perspectives: ages 5–7 years, 8–10 years, 11–13 years, and 14–15 years. An important difference between our study and theirs, which may have had an impact, is that all respondents in their study completed DCE tasks with every perspective. In contrast, in our study, different respondents completed the task with each perspective. On one hand, our respondents only had to focus on a single perspective throughout, which may have enabled them to more consistently and carefully consider the impact of the health states on the proxy or themselves. On the other hand, the nature of multi-arm studies such as ours means we cannot rule out that the differences between perspectives were driven by differences in underlying preferences between the samples. This is a limitation of our study. That said, the demographic characteristics in each of our samples, and particularly the 4-year-old and 10-year-old child arms, were remarkably similar. Furthermore, it is worth acknowledging that a recent cognitive debriefing study that used the OPUF tool—albeit in the context of valuing a different instrument (EQ-HWB-9)—revealed some concerns about the method, suggesting that interviewer-led data collection may be preferred to ensure data quality \[34\]. Given that our study used online self-completion, this is a further limitation of our study.

Stakeholder engagement is an increasingly important aspect of valuation studies, particularly when the instrument being valued is for children or adolescents \[21, 35, 36\]. Our study highlights that the choice of perspective, among other important considerations, such as whose preferences to elicit (e.g., adults vs. children and/or adolescents) and which elicitation technique to use (e.g., DCE vs. best–worst scaling), is also an important consideration. Furthermore, should stakeholders and researchers opt to collect data using multiple perspectives, it is likely that the resulting value sets will have different characteristics, which may create dilemmas when ultimately deciding upon which value set to use in practice (for which no definitive criteria currently exist). As such, it is advisable for research teams to seek a consensus view with stakeholders on the choice of perspective before embarking on their valuation study. It is also worth noting that deciding on a perspective may be particularly challenging if studies aim to elicit both adult and adolescent preferences \[21\], given that the former are likely to take a child proxy perspective, whereas it is not clear whether it would be feasible for the latter to also do so, given the complexity of valuation tasks \[37–39\].

## Conclusion

Our results suggest that the valuation of child/adolescent health depends somewhat on what perspective adult respondents are required to take in preference-elicitation tasks. With the OPUF tool, utilities were higher when respondents were asked to consider their views about a child than when they were asked to consider another adult or themselves. The RI of the different dimensions also differed by perspective, but far more so in the DCE than in the OPUF tool. Researchers should be aware of the potential impact of the choice of perspective in valuation studies and ensure that relevant stakeholders understand the importance of this decision before embarking on a valuation study.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 57 KB)

</div>

## Acknowledgements

The authors are grateful to Yaling Yang for discussing an earlier version of this manuscript at the 2023 EuroQol Plenary meeting in Rome, Italy.

## Funding

Financial support for the study was provided by a grant from the EuroQol Research Foundation (EQ-432-RA).

## Declarations

### Conflict of Interest

All authors received grants from the EuroQol Research Foundation during the conduct of the study. Koonal Shah, Nancy Devlin, and David Mott are members of the EuroQol Group Association. The views expressed in this paper do not reflect those of the EuroQol Group. David Mott is an employee of the Office of Health Economics (OHE), a registered charity, and an Independent Research Organisation, which receives funding from a variety of private and public sector sources. Jake Hitch and Gayathri Kumar were employees of OHE during the conduct of the study. Koonal Shah is employed by the National Institute for Health and Care Excellence (NICE); the views expressed in this paper do not reflect those of NICE. Nancy Devlin and Paul Schneider have no conflicts of interest to disclose.

### Authorship Statement:

All authors contributed to the study conception and design. The analysis was performed by JH and DM. The first draft of the manuscript was written by JH, and all authors commented on previous versions of the manuscript. All authors read and approved the final manuscript.

### Ethics and Informed Consent

Ethical approval was sought and received from the City, University of London (now City St George’s, University of London) School of Social Sciences Research Ethics Committee (ETH2223-1011). All participants provided informed consent before participating in the study.

### Data Availability

The study materials are available from the corresponding author upon reasonable request.

## References

## References

1. Peasgood T, Howell M, Raghunandan R, Salisbury A, Sellars M, Chen G, et al. Systematic review of the relative social value of child and adult health. Pharmacoeconomics. 2024;42:177–98. 10.1007/s40273-023-01327-x.

2. Kind P, Klose K, Gusi N, Olivares PR, Greiner W. Can adult weights be used to value child health states? Testing the influence of perspective in valuing EQ-5D-Y. Qual Life Res. 2015;24:2519–39. 10.1007/s11136-015-0971-1.

3. Rowen D, Rivero-Arias O, Devlin N, Ratcliffe J. Review of valuation methods of preference-based measures of health for economic evaluation in child and adolescent populations: where are we now and where are we going? Pharmacoeconomics. 2020;38:325–40. 10.1007/s40273-019-00873-7.

4. Ramos-Goñi JM, Oppe M, Stolk E, Shah K, Kreimeier S, Rivero-Arias O, et al. International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics. 2020;38:653–63. 10.1007/s40273-020-00909-3.

5. Ludwig K, Graf von der Schulenburg J-M, Greiner W. German value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36:663–74. 10.1007/s40273-018-0615-8.

6. Fitriana TS, Roudijk B, Purba FD, Busschbach JJV, Stolk E. Estimating an EQ-5D-Y-3L value set for Indonesia by mapping the DCE onto TTO values. Pharmacoeconomics. 2022;40:157–67. 10.1007/s40273-022-01210-1.

7. Dewilde S, Roudijk B, Tollenaar NH, Ramos-Goñi JM. An EQ-5D-Y-3L value set for Belgium. Pharmacoeconomics. 2022;40:169–80. 10.1007/s40273-022-01187-x.

8. Prevolnik Rupel V, Ogorevc M, Group. EQ-5d-y value set for Slovenia. Pharmacoeconomics. 2021;39:463–71. 10.1007/s40273-020-00994-4.

9. Kreimeier S, Mott D, Ludwig K, Greiner W. EQ-5D-Y value set for Germany. Pharmacoeconomics. 2022;40(S2):217–29. 10.1007/s40273-022-01143-9.

10. Shiroiwa T, Ikeda S, Noto S, Fukuda T, Stolk E. Valuation survey of EQ-5D-Y based on the international common protocol: development of a value set in Japan. Med Decis Making. 2021;41:597–606. 10.1177/0272989X211001859.

11. Espirito Santo CM, Miyamoto GC, Santos VS, Ben ÂJ, Finch AP, Roudijk B, et al. Estimating an EQ-5D-Y-3L value set for Brazil. Pharmacoeconomics. 2024;42:1047–63. 10.1007/s40273-024-01404-9.

12. Roudijk B, Sajjad A, Essers B, Lipman S, Stalmeier P, Finch AP. A value set for the EQ-5D-Y-3L in the Netherlands. Pharmacoeconomics. 2022;40:193–203. 10.1007/s40273-022-01192-0.

13. Yang Z, Jiang J, Wang P, Jin X, Wu J, Fang Y, et al. Estimating an EQ-5D-Y-3L value set for China. Pharmacoeconomics. 2022;40:147–55. 10.1007/s40273-022-01216-9.

14. Rencz F, Ruzsa G, Bató A, Yang Z, Finch AP, Brodszky V. Value set for the EQ-5D-Y-3L in Hungary. Pharmacoeconomics. 2022;40:205–15. 10.1007/s40273-022-01190-2.

15. Pan T, Roudijk B, Devlin N, Mulhern B, Norman R. An Australian value set for the EQ-5D-Y-3L. Health Qual Life Outcomes. 2025;23:72. 10.1186/s12955-025-02402-x.

16. Mott DJ, Devlin NJ, Kreimeier S, Norman R, Shah KK, Rivero-Arias O. Analytical considerations when anchoring discrete choice experiment values using composite time trade-off data: the case of EQ-5D-Y-3L. Pharmacoeconomics. 2022;40:129–37. 10.1007/s40273-022-01214-x.

17. Devlin N, Pan T, Kreimeier S, Verstraete J, Stolk E, Rand K, et al. Valuing EQ-5D-Y: the current state of play. Health Qual Life Outcomes. 2022;20:105. 10.1186/s12955-022-01998-8.

18. Devlin NJ, Pan T, Sculpher M, Jit M, Stolk E, Rowen D, et al. Using age-specific values for pediatric HRQoL in cost-effectiveness analysis: is there a problem to be solved? If so, how? Pharmacoeconomics. 2023;41:1165–74. 10.1007/s40273-023-01300-8.

19. Devlin N, Roudijk B, Viney R, Stolk E. EQ-5D-Y-3L value sets, valuation methods and conceptual questions. Pharmacoeconomics. 2022;40:123–7. 10.1007/s40273-022-01226-7.

20. Lipman SA, Reckers-Droog VT, Kreimeier S. Think of the children: a discussion of the rationale for and implications of the perspective used for EQ-5D-Y health state valuation. Value Health. 2021;24:976–82. 10.1016/j.jval.2021.01.011.

21. Powell PA, Rowen D, Keetharuth A, Mukuria C, Shah K. Who should value children’s health and how? An international Delphi study. Soc Sci Med. 2024;355:117127. 10.1016/j.socscimed.2024.117127.

22. Ramos-Goñi JM, Estévez-Carrillo A, Rivero-Arias O, Rowen D, Mott D, Shah K, et al. Does changing the age of a child to be considered in 3-level version of EQ-5D-Y discrete choice experiment–based valuation studies affect health preferences? Value Health. 2022;25:1196–204. 10.1016/j.jval.2022.03.001.

23. Shah KK, Ramos-Goñi JM, Kreimeier S, Devlin NJ. An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values. Eur J Health Econ. 2020;21:1091–103. 10.1007/s10198-020-01205-9.

24. Lipman SA, Reckers-Droog VT, Karimi M, Jakubczyk M, Attema AE. Self vs. other, child vs. adult. An experimental comparison of valuation perspectives for valuation of EQ-5D-Y-3L health states. Eur J Health Econ. 2021;22:1507–18. 10.1007/s10198-021-01377-y.

25. Dewilde S, Janssen MF, Lloyd AJ, Shah K. Exploration of the reasons why health state valuation differs for children compared with adults: a mixed methods approach. Value Health. 2022;25:1185–95. 10.1016/j.jval.2021.11.1377.

26. Powell PA, Rowen D, Rivero-Arias O, Tsuchiya A, Brazier JE. Valuing child and adolescent health: a qualitative study on different perspectives and priorities taken by the adult general public. Health Qual Life Outcomes. 2021;19:222. 10.1186/s12955-021-01858-x.

27. Schneider PP, van Hout B, Heisen M, Brazier J, Devlin N. The online elicitation of personal utility functions (OPUF) tool: a new method for valuing health states. Wellcome Open Res. 2022;7:14. 10.12688/wellcomeopenres.17518.1.

28. Devlin NJ, Shah KK, Mulhern BJ, Pantiri K, van Hout B. A new method for valuing health: directly eliciting personal utility functions. Eur J Health Econ. 2019;20:257–70. 10.1007/s10198-018-0993-z.

29. Hansen TM, Stavem K, Rand K. Sample size and model prediction accuracy in EQ-5D-5L valuations studies: expected out-of-sample accuracy based on resampling with different sample sizes and alternative model specifications. MDM Policy Pract. 2022;7:23814683221083839. 10.1177/23814683221083839.

30. De Bekker-Grob EW, Donkers B, Jonker MF, Stolk EA. Sample size requirements for discrete-choice experiments in healthcare: a practical guide. Patient. 2015;8:373–84. 10.1007/s40271-015-0118-z.

31. Lancsar E, Louviere J. Conducting discrete choice experiments to inform healthcare decision making: a user’s guide. Pharmacoeconomics. 2008;26:661–77. 10.2165/00019053-200826080-00004.

32. Schneider P, Blankart K, Brazier J, Van Hout B, Devlin N. Using the online elicitation of personal utility functions approach to derive a patient-based 5-level version of EQ-5D value set: a study in 122 patients with rheumatic diseases from Germany. Value Health. 2024;27:376–82. 10.1016/j.jval.2023.12.009.

33. Mott DJ, Chami N, Tervonen T. Reporting quality of marginal rates of substitution in discrete choice experiments that elicit patient preferences. Value Health. 2020;21:979–84. doi:10.1016/j.jval.2020.04.1831

34. Peasgood T, Devlin N, Ludwig K, Marten O, McDool E, Schneider P, et al. How well do participants understand the questions asked in the Online Personal Utility Functions (OPUF) approach? A cognitive debrief of the EQ-HWB-S (EQ health and wellbeing short version) valuation. Qual Life Res. 2025;34:2269–78. 10.1007/s11136-025-03989-w.

35. Xie F, Xie S, Pullenayegum E, Ohinmaa A. Understanding Canadian stakeholders’ views on measuring and valuing health for children and adolescents: a qualitative study. Qual Life Res. 2024;33:1415–22. 10.1007/s11136-024-03618-y.

36. Nazari JL, Pickard AS, Gu NY. Findings from a roundtable discussion with US stakeholders on valuation of the EQ-5D-Y-3L. Pharmacoeconomics. 2022;40:139–46. 10.1007/s40273-022-01222-x.

37. Pan T, Ramos-Goni JM, Roudijk B, Xie S, Xie F, Yang Z, et al. Testing the valuation of the EQ-5D-Y-5L in adults and adolescents: Results from a five-country study and implications for the descriptive system. Value Health. 2025;S1098–3015(25):02483. 10.1016/j.jval.2025.07.016.

38. Nazari JL, Ramos-Goñi JM, Gu NY, Pickard AS. An acquired taste: latent class analysis to compare adolescent and adult preferences for EQ-5D-Y-3L health states. Value Health. 2025;28:781–9. 10.1016/j.jval.2025.01.020.

39. Mott DJ, Shah KK, Ramos-Goñi JM, Devlin NJ, Rivero-Arias O. Valuing EQ-5D-Y-3L health states using a discrete choice experiment: do adult and adolescent preferences differ? Med Decis Making. 2021;41:584–96. 10.1177/0272989X21999607.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 57 KB)

</div>

### Data Availability Statement

The study materials are available from the corresponding author upon reasonable request.

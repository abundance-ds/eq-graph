---
project_id: "20180510"
work_id: "doi:10.1007/s40273-020-00994-4"
doi: "10.1007/s40273-020-00994-4"
pmid: "33565048"
pmcid: "PMC8009800"
title: "EQ-5D-Y Value Set for Slovenia"
journal: "Pharmacoeconomics"
publication_date: "2021-02-10"
volume: "39"
issue: "4"
authors:
  - name: "Valentina Prevolnik Rupel"
    affiliation_ids:
      - "Aff1"
  - name: "Marko Ogorevc"
    affiliation_ids:
      - "Aff1"
  - name: "IMPACT HTA HRQoL Group"
affiliations:
  - id: "Aff1"
    name: "Institute for Economic Research, Kardeljeva ploščad 17, 1000 Ljubljana, Slovenia"
  - id: "Aff2"
    name: "School of Public Health, Department of Health Economics and Health Care Management, Bielefeld University, Bielefeld, Germany"
  - id: "Aff3"
    name: "Maths In Health BV, Rotterdam, The Netherlands"
licence: "cc-by-nc"
source_file: "input/projects/20180510/papers/doi_10.1007_s40273-020-00994-4.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8009800/fullTextXML"
source_method: "epmc_xml"
source_sha256: "9a785c300b8808613a0f9bcf40996be6a44225155b970b462fb971deeea0d8c7"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# EQ-5D-Y Value Set for Slovenia

## Abstract

### Background

A value set for the EuroQoL 5-Dimensions (EQ-5D)-Y in Slovenia is not yet available, making the calculation of quality-adjusted life-years (QALYs) for children and adolescents using this generic instrument impossible.

### Objective

The main objective of our study was to obtain adult preferences towards EQ-5D-Y health states in Slovenia, following the EQ-5D-Y-3L international valuation protocol. The adults were asked to take the perspective of a hypothetical 10-year-old child.

### Method

A sample of 1074 adults in Slovenia completed an online discrete-choice experiment (DCE) survey on EQ-5D-Y health states. The latent scale issue was addressed by obtaining the value of the anchor (33333) with 200 composite time trade-off (cTTO) interviews. A mixed (random coefficients) logit model was used to estimate the value set.

### Results

All the estimated coefficients of the mixed logit model were statistically significant at the 1% level and had an expected negative sign. The most important health dimension in EQ-5D-Y is pain/discomfort, followed by anxiety/depression, usual activities, and mobility, with self-care being the least important health dimension.

### Conclusions

The study addresses an important research gap and presents the EQ-5D-Y value set for Slovenia. At the time of writing, no published value sets are available for the EQ-5D-Y-3L appropriate for use in QALY calculations, making this value set the first EQ-5D-Y value set in the world.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40273-020-00994-4.

Accepted 2020 Dec 24; Issue date 2021.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| This paper presents the first childhood/adolescent EuroQoL 5-Dimensions (EQ-5D)-Y-3L value set in the world. |
| An EQ-5D-Y-3L value set for Slovenia was obtained following the international valuation protocol for the EQ-5D-Y-3L published in early 2020. |
| The childhood/adolescent EQ-5D-Y-3L value set allows future cost-utility analysis in the child and adolescent population in Slovenia. |

</div>

## Introduction

In most countries \[1, 2\], the preferred outcome measure for economic evaluation purposes is quality-adjusted life-years (QALYs), which requires the employment of generic preference-based measures of health for calculation. The development of generic measures has been rapid in the past few decades, and many instruments are available, such as the EQ-5D \[3\], the Health Utilities Index (HUI) \[4\], the Short Form 6D (SF-6D) \[5\], the 15D instrument \[6\], and the Assessment of Quality of Life (AQOL) \[7\]. In addition to a descriptive system, a generic preference-based instrument usually presents a scoring algorithm or value set, which reflects the values for the health states it describes. National value sets for the EQ-5D, based on general population preferences, are available for many countries, including Slovenia, where the directly measured visual analogue scale (VAS) and time trade-off (TTO)-based three-level \[8\] and five-level crosswalk \[9\] sets are available.

With ever more active discussion on the inclusion of young people in decision making, more attention has recently been given to the development of multi-attribute health status classification systems specific to children and adolescents \[10\]. Recent reviews \[11, 12\] have identified nine generic preference-based instruments developed specifically for young people (children and adolescents): the Adolescent Health Utility Measure (AHUM) \[13\]; the Assessment of Quality of Life-6 Dimensions (AQoL-6D) \[14\]; the Child Health Utility instrument (CHU9D) \[15\]; the EQ-5D-Y \[16\]; the HUI Mark 2 \[17\]; the HUI Mark 3 \[18\]; the Quality of Well-Being (QWB) \[19\]; the 16-Dimension (16D) \[20\]; and the 17-dimension (17D) \[21\]. In addition to multi-attribute health status classification systems, other approaches are also available to estimate the QALYs of children and adolescents.

Scoring algorithms using samples from children and adolescents are currently available only for the 16D, the AQoL-6D and the CHU9D \[22\]. Canaway and Frew \[23\] established that the use of an adult EQ-5D value set with the EQ-5D-Y health states resulted in values worse than dead for children who were actually considered well enough to be in school at the time. Further studies \[24, 25\] established a need for specific EQ-5D-Y value sets, as the current EQ-5D-Y is not complete without a value set focused on children and adolescents. Progress in developing child- and adolescent-specific value sets has been slow; however, some studies have estimated EQ-5D-Y health state values based on general adult population preferences or have explored ways of valuing EQ-5D-Y health states. Craig et al. \[26\] developed an experimental value set for the EQ-5D-Y by asking adults a series of questions, including the choice between loss of health-related quality of life (HRQoL) and loss of lifespan for a child. In a study that aimed to explore ways of valuing the EQ-5D-Y-3L, Kreimeier et al. \[27\] used a composite TTI (cTTO) and a discrete-choice experiment (DCE) in a survey of the general adult population in Germany, asking them to value the health states of children and adolescents. Recently, the first version of the EQ-5D-Y-3L international valuation protocol was published, which suggests that preferences should be obtained from a sample of the general adult population \[28\].

A value set for the EQ-5D-Y in Slovenia is not yet available, making the calculation of QALYs for children and adolescents directly via the EQ-5D instrument impossible. The main objective of our study was to fill this gap and to obtain and present adult preferences towards EQ-5D-Y health states in Slovenia following the EQ-5D-Y valuation protocol. The study presents the first EQ-5D-Y-3L value set in the world.

## Methods

An online DCE survey was administered to a representative sample of Slovenian adults to enable the calculation of latent scale coefficients. To obtain the value of the anchor (33333), a further 202 cTTO face-to-face interviews were conducted.

### Sampling

For the DCE survey, a sample of 1276 adults in Slovenia was obtained through an online panel of a market research company (Valicon Ljubljana). The quota samples were formed according to age groups (adults: 18–29, 30–39, 40–49, 50–59, 60–69, ≥ 70 years) and sex (female/male), as well as by statistical region (west Slovenia, east Slovenia). The DCE technique produces relative preferences on a latent scale, meaning that this technique does not automatically provide utilities that are anchored to a dead–full health scale. A further 200 cTTO interviews with a non-representative sample of the adult population (aged ≥ 18 years) in one of the Slovenian regions were conducted. Age-based sampling weights were used to reinstate the original importance of each age group within the population. Weights reflecting the population age distribution were applied to the estimation of the mean value of the anchor (33333).

### EQ-5D-Y

The EQ-5D-Y is a patient-reported outcome measure that was designed by the EuroQol Group to measure the HRQoL of children and adolescents aged 8–15 years \[16\]. The EQ-5D-Y uses adapted wording in its descriptive system to make it more understandable for young people. It contains five dimensions (mobility \[MO, ‘walking about’\], self-care \[SC, ‘looking after myself’\], usual activities \[UA, ‘doing usual activities’\], pain or discomfort \[PD, ‘having pain or discomfort’\], and anxiety or depression \[AD, ‘feeling worried, sad or unhappy’\]) with three levels of severity (level 1, describing no problems/no pain/not worried; level 2, describing some problems/some pain/a bit worried; and level 3, measuring a lot of problems/a lot of pain/very worried) in each dimension \[29\]. The respondents used the youth version of the EQ-5D-Y instrument to value the EQ-5D-Y health states, taking the perspective of a hypothetical 10-year-old child \[29\]. The label version from the proxy version was used in the DCE and in the cTTO survey. In the interests of brevity, the traditional dimension labels used in the adult questionnaire and their acronyms are used throughout this paper. For the same reason, in the PD and AD dimensions, we retained the level descriptions ‘no problems’, ‘some problems’ and ‘a lot of problems’.

### Online Discrete-Choice Experiment and Face-to-Face Composite Time Trade-off Survey

In the online survey, a series of DCE tasks was used to obtain health state preferences from adults taking the perspective of a 10-year-old child. Within each DCE task, two health states were presented together, and the respondents were asked to choose their preferred health state (forced choice).

The experimental design took the form of a D-efficient design, with main effects and all two-way interactions, a minimal number of unrealistic health states, overlapping of health states in two dimension levels, and the right level and utility balance. Each respondent completed 15 tasks, and the design was divided into ten blocks yielding a total of 150 pairs. The design allowed the estimation of a multinomial logit model with 50 parameters (ten main effects parameters and all 40 two-way interaction parameters). We randomly selected 150 pairs that maximised the Fisher information matrix. The DCE technique produces relative preferences on a latent scale, meaning that this technique does not automatically provide utilities. Hence, the overall utilities were multiplied to ensure that the value of the pits state (33333) in the DCE survey matched the weighted average value of the pits state in the cTTO survey. The online survey was programmed using LimeSurvey.

All 202 cTTO surveys were conducted in the Primorska region. After a full day’s training in October 2019, three interviewers carried out the interviews with the non-probability purposive sample between November 2019 and February 2020, following the EuroQol protocol. The interviewers explained all the elements of the cTTO task (e.g. ‘worse than dead’ health states, ‘better than dead’ health states) using the wheelchair example.

The respondents received compensation in the form of a €10 voucher. The interviewees were asked to value ten cTTO states and complete an EQ-5D-Y descriptive profile and the VAS, as well as the EQ-5D-5L questionnaire and some socio-demographic questions. Respondents performed an initial rating exercise using three practice health states to familiarize themselves with the task.

The respondents were asked to imagine a 10-year-old child experiencing the health states to be valued. The valuation protocol recommends using the perspective of a 10-year-old child \[28\], and earlier studies have also done so \[26, 30–32\].

### Quality Control

To identify any respondents whose choices suggested a reduced level of attentiveness, engagement or understanding, all the responses in the DCE tasks were checked for rationality through three fixed dominant pairs (quality control \[QC\] task), in which one health state was considered logically dominant. The dominant pairs were excluded from the modelling exercise. The participants were not included in the analysis if they failed two or more of the three QC tasks. Additionally, participants were excluded if the minimum amount of time spent on all the DCE tasks was less than 150 s; in this case, their responses were excluded from the analysis as it was assumed that these respondents were speeders who had not appropriately answered the tasks.

The EuroQol QC protocol was followed in the cTTO data collection \[33\]. First of all, the interview script was translated into the Slovenian language, as this was to be used by the interviewers. The text provided instructions on the aim of the interviews and the role of the interviewer. As the cTTO interviews were expected to be complicated, the script was quite detailed \[29\]. The interview was discarded if any of the following criteria were met:

1.  No explanation of the ‘worse than dead’ task (lead time) in the wheelchair example was given.

2.  Not enough time was spent on the wheelchair example (less than 3 min).

3.  Apparent inconsistency in the cTTO ratings (33333 was not the lowest and it was at least 0.5 higher than the state with the lowest value).

4.  Not enough time was spent on the cTTO task (less than 5 min for the ten cTTO tasks).

The QC reports were prepared every ten interviews for the cTTO tasks and at least once a week for the DCE survey. The data were collected between November 2019 and February 2020.

### Data Analysis

Choice data were modelled using a random utility model, where utility, *U*, for a person *i* choosing alternative *j* is given by Eq. (<a href="#Equ1" data-ref-type="disp-formula">1</a>):

``` math
U_{\mathit{ij}} = V_{\mathit{ij}} + \epsilon_{\mathit{ij}},
```

where $`V_{\mathit{ij}}`$ is an observable component and $`\epsilon_{\mathit{ij}}`$ is unknown and treated as random. To allow for multiple-choice tasks per subject, we rewrote a random utility for a person *i*, an alternative *j*, and a choice occasion *t* as:

``` math
U_{\mathit{ijt}} = x_{\mathit{ijt}}^{T}\beta_{i} + \epsilon_{\mathit{ijt}},i = 1,\ldots,N,j = 1,\ldots,J,t = 1,\ldots T_{i},
```

where *x*<sub>*ijt*</sub> is a *K* × 1 vector of observed alternative attributes; $`\epsilon_{\mathit{ijt}}`$ is the idiosyncratic error term, and is i.i.d. extreme value type 1; the parameter vector $`\beta_{i}`$ is unobserved for each *i* and is assumed to vary in the population following the continuous density $`f(\beta_{i}|\theta)`$, where $`\theta`$ is the parameters of this distribution. We assume that the parameters are distributed as multivariate normal, $`\beta_{i} \sim \text{MNV}\left( {\beta,\Sigma} \right)`$, and the vector $`\beta_{i}`$ can be rewritten as:

``` math
\beta_{i} = \beta + L\eta_{i},
```

where $`\eta_{i} \sim N{(0,I)}`$, and L is the lower-triangular Cholesky factor of $`\Sigma`$ such that $`LL^{T} = VAR{(\beta_{i})} = \Sigma`$. A mixed (with correlated random coefficients) logit model was used to estimate adult preferences for children and adolescents. It has been shown that the mixed logit is associated with better fit than the multinomial model \[34\] and that there are insignificant differences between these models with regard to deriving a latent scale value set.

A linear additive utility model was estimated with all variables dummy coded (‘no problems’ was used as the base level). Estimated coefficients were divided by the overall utility range and rescaled to the weighted censored average value of the pits state (33333) obtained through the cTTO survey, to produce a value set.

Because cTTO does not permit the reporting of values lower than − 1, censoring was applied. All observations at − 1 were treated as equal to or below − 1. The average value was obtained via the Tobit model, including only the constant as the regressor on the data for the pits state. Sampling weights were applied to the sample before estimation. In essence, observations were repeated until the age distribution of responses from the cTTO task matched the original importance of each age group within the population. Standard errors were obtained through bootstrapping (simulation of 10 million value sets). The data analysis was carried out using R.

## Results

Altogether, 1276 adults were included in the estimation of the EQ-5D-Y value set, after excluding those who did not meet minimum quality criteria. A total of 1074 (of 1210 \[88.8%\]) respondents completed the DCE tasks with satisfactory quality, and 202 (of 210 \[96.2%\]) completed the cTTO tasks that met the quality criteria. The descriptive statistics of the DCE and cTTO samples are shown in Table <a href="#Tab1" data-ref-type="table">1</a>.

<div id="Tab1" class="table-wrap">

<div class="caption">

Descriptive statistics of the discrete-choice experiment and composite time trade-off samples

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristics</th>
<th style="text-align: left;">DCE</th>
<th style="text-align: left;">cTTO</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Sample size, <em>N</em></td>
<td style="text-align: left;">1074</td>
<td style="text-align: left;">202</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Sex</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">529 (49.3%)</td>
<td style="text-align: left;">111 (45.1%)</td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">545 (50.7%)</td>
<td style="text-align: left;">91 (54.9%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Age group</td>
</tr>
<tr>
<td style="text-align: left;"> 18–29</td>
<td style="text-align: left;">154 (14.3%)</td>
<td style="text-align: left;">118 (58.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td style="text-align: left;">172 (16.0%)</td>
<td style="text-align: left;">30 (14.8%)</td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td style="text-align: left;">194 (18.1%)</td>
<td style="text-align: left;">24 (11.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td style="text-align: left;">194 (18.1%)</td>
<td style="text-align: left;">14 (6.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> 60–69</td>
<td style="text-align: left;">183 (17.0%)</td>
<td style="text-align: left;">13 (6.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 70</td>
<td style="text-align: left;">177 (16.5%)</td>
<td style="text-align: left;">3 (1.5%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Mobility</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">818 (76.2%)</td>
<td style="text-align: left;">189 (93.6%)</td>
</tr>
<tr>
<td style="text-align: left;"> Some problems</td>
<td style="text-align: left;">230 (21.4%)</td>
<td style="text-align: left;">13 (6.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> A lot of problems</td>
<td style="text-align: left;">26 (2.4%)</td>
<td style="text-align: left;">0 (0%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Self-care</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">1003 (93.4%)</td>
<td style="text-align: left;">200 (99.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> Some problems</td>
<td style="text-align: left;">66 (6.2%)</td>
<td style="text-align: left;">2 (1.0%)</td>
</tr>
<tr>
<td style="text-align: left;"> A lot of problems</td>
<td style="text-align: left;">5 (0.5%)</td>
<td style="text-align: left;">0 (0%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Usual activities</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">873 (81.3%)</td>
<td style="text-align: left;">188 (93.1%)</td>
</tr>
<tr>
<td style="text-align: left;"> Some problems</td>
<td style="text-align: left;">189 (17.6%)</td>
<td style="text-align: left;">14 (6.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> A lot of problems</td>
<td style="text-align: left;">12 (1.1%)</td>
<td style="text-align: left;">0 (0%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Pain/discomfort</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">627 (58.4%)</td>
<td style="text-align: left;">146 (72.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> Some problems</td>
<td style="text-align: left;">415 (38.6%)</td>
<td style="text-align: left;">56 (27.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> A lot of problems</td>
<td style="text-align: left;">32 (3.0%)</td>
<td style="text-align: left;">0 (0%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Anxiety/depression</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">583 (54.3%)</td>
<td style="text-align: left;">172 (85.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Some problems</td>
<td style="text-align: left;">456 (42.5%)</td>
<td style="text-align: left;">28 (13.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> A lot of problems</td>
<td style="text-align: left;">35 (3.3%)</td>
<td style="text-align: left;">2 (1.0%)</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Visual analogue scale</td>
</tr>
<tr>
<td style="text-align: left;"> Mean</td>
<td style="text-align: left;">79.9</td>
<td style="text-align: left;">83.3</td>
</tr>
<tr>
<td style="text-align: left;"> Standard deviation</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">12.4</td>
</tr>
<tr>
<td style="text-align: left;"> Minimum</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">38</td>
</tr>
<tr>
<td style="text-align: left;"> Maximum</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">100</td>
</tr>
<tr>
<td style="text-align: left;"> Median</td>
<td style="text-align: left;">82</td>
<td style="text-align: left;">85</td>
</tr>
</tbody>
</table>

</div>

The sample of adults in the DCE survey slightly under-represents women aged \> 70 years in east Slovenia (− 23%) and slightly over-represents men in the same age group residing in the west Slovenian region (+ 20%). All other groups were well represented, as shown in Fig. <a href="#Fig1" data-ref-type="fig">1</a>. Sampling weights were not used in the estimation.

<figure id="Fig1">
<p><img src="40273_2020_994_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40273_2020_994_Fig1_HTML.gif" /></p>
<figcaption>Discrete-choice experiment task example</figcaption>
</figure>

The sample of adults in the cTTO survey was not representative of the Slovenian population, as the aim of the survey was only to obtain the anchor. The respondents in the cTTO survey were, on average, younger, as 58.4% of the respondents were aged \< 30 years, whereas 14.3% in the DCE survey were aged \< 30 years. The cTTO respondents also had fewer problems with health on all health dimensions, presumably due to age. Moreover, both the mean and the median VAS scores were slightly higher in the cTTO sample. Sampling weights were used in the estimation of mean values to ensure representability.

The mean cTTO scores of the health states valued in the cTTO survey are shown in Fig. <a href="#Fig2" data-ref-type="fig">2</a>. The pits state (33333) value was used in the rescaling of coefficients from the mixed logit model shown in Table <a href="#Tab2" data-ref-type="table">2</a>. The mean cTTO scores ranged from − 0.691 for state 33333 to 1.000 for state 11111 (Fig. <a href="#Fig3" data-ref-type="fig">3</a>). In total, 50 health states (20.6%) had negative values (‘worse than dead’), whereas 10 health states (4.12%) had mean values higher than 0.8 (the full value set is given in the Electronic Supplementary Material).

<figure id="Fig2">
<p><img src="40273_2020_994_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2020_994_Fig2_HTML.gif" /></p>
<figcaption>Sample representativeness in the DCE survey by age, sex and region. <em>DCE</em> discrete-choice experiment</figcaption>
</figure>

<div id="Tab2" class="table-wrap">

<div class="caption">

Regression results of mixed logit model and rescaled coefficients using anchor score

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Mixed logit</th>
<th style="text-align: left;">Rescaled<sup>a</sup></th>
</tr>
<tr>
<th style="text-align: left;">Coeff.</th>
<th style="text-align: left;">Std. dev.</th>
<th style="text-align: left;">Coeff.</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility 2</td>
<td style="text-align: left;">− 0.562*** (0.070)</td>
<td style="text-align: left;">0.215 (0.171)</td>
<td style="text-align: left;">− 0.083*** (0.011)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility 3</td>
<td style="text-align: left;">− 2.062*** (0.122)</td>
<td style="text-align: left;">1.346*** (0.156)</td>
<td style="text-align: left;">− 0.305*** (0.016)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 2</td>
<td style="text-align: left;">− 0.314*** (0.067)</td>
<td style="text-align: left;">0.372** (0.122)</td>
<td style="text-align: left;">− 0.046*** (0.009)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 3</td>
<td style="text-align: left;">− 1.491*** (0.100)</td>
<td style="text-align: left;">0.923*** (0.129)</td>
<td style="text-align: left;">− 0.221*** (0.013)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 2</td>
<td style="text-align: left;">− 0.714*** (0.058)</td>
<td style="text-align: left;">0.502*** (0.101)</td>
<td style="text-align: left;">− 0.106*** (0.009)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 3</td>
<td style="text-align: left;">− 2.177*** (0.097)</td>
<td style="text-align: left;">1.275*** (0.109)</td>
<td style="text-align: left;">− 0.322*** (0.013)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 2</td>
<td style="text-align: left;">− 1.097*** (0.065)</td>
<td style="text-align: left;">0.890*** (0.0838)</td>
<td style="text-align: left;">− 0.162*** (0.010)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 3</td>
<td style="text-align: left;">− 3.126*** (0.125)</td>
<td style="text-align: left;">2.101*** (0.123)</td>
<td style="text-align: left;">− 0.463*** (0.016)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 2</td>
<td style="text-align: left;">− 0.793*** (0.064)</td>
<td style="text-align: left;">0.738*** (0.084)</td>
<td style="text-align: left;">− 0.117*** (0.009)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 3</td>
<td style="text-align: left;">− 2.565*** (0.110)</td>
<td style="text-align: left;">1.907*** (0.104)</td>
<td style="text-align: left;">− 0.380*** (0.014)</td>
</tr>
<tr>
<td style="text-align: left;">Log-Likelihood</td>
<td colspan="3" style="text-align: left;">− 7369.1</td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td colspan="3" style="text-align: left;">14868.27</td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td colspan="3" style="text-align: left;">15367.93</td>
</tr>
<tr>
<td style="text-align: left;">Observations</td>
<td colspan="3" style="text-align: left;">16110</td>
</tr>
<tr>
<td style="text-align: left;">Respondents</td>
<td colspan="3" style="text-align: left;">1074</td>
</tr>
</tbody>
</table>

\**p* \< 0.001

<sup>a</sup>Bootstrapped (10,000,000 simulations)

</div>

<figure id="Fig3">
<p><img src="40273_2020_994_Fig3_HTML.jpg" id="MO4" /></p>
<p><img src="40273_2020_994_Fig3_HTML.gif" /></p>
<figcaption>Mean cTTO scores and the anchor score. <em>cTTO</em> composite time trade-off</figcaption>
</figure>

All the estimated coefficients of the mixed logit model were statistically significant at the 0.1% level and had an expected negative sign, as shown in Table <a href="#Tab2" data-ref-type="table">2</a>. Relatively, in the adults’ opinion, the most important health dimension in EQ-5D-Y was pain/discomfort, followed by anxiety/depression, usual activities, mobility and, finally, self-care as the least important health dimension, as shown in Fig. <a href="#Fig4" data-ref-type="fig">4</a> and Table <a href="#Tab3" data-ref-type="table">3</a>.

<figure id="Fig4">
<p><img src="40273_2020_994_Fig4_HTML.jpg" id="MO3" /></p>
<p><img src="40273_2020_994_Fig4_HTML.gif" /></p>
<figcaption>Relative importance of health dimensions</figcaption>
</figure>

<div id="Tab3" class="table-wrap">

<div class="caption">

Childhood/adolescent value set summary statistics

</div>

| Parameter                                    | EQ-5D-Y       |
|----------------------------------------------|---------------|
| Number of health states                      | 243           |
| Range                                        | − 0.691 to 1  |
| Mean ± SD                                    | 0.265 ± 0.326 |
| Median                                       | 0.326         |
| Skewness                                     | − 0.194       |
| Kurtosis                                     | 2.640         |
| States worse than dead (index \< 0), *n* (%) | 50 (20.6%)    |
| States with index \> 0.8, *n* (%)            | 10 (4.12%)    |

</div>

## Discussion

In this study, 1074 adults participated in a DCE survey valuing 15 pairs of health states defined by the EQ-5D-Y instrument, resulting in relative preferences towards health states on a latent scale. A further 202 cTTO face-to-face interviews were performed with Slovenian adults to obtain the value for the worst state (33333). The interviewees valued ten health states using the cTTO protocol. The EQ-5D-Y-3L value set was estimated using a mixed (random coefficients) logit model. The study closely followed the EQ-5D-Y-3L international valuation protocol \[28\].

The EQ-5D-Y value set shows the high importance of the pain/discomfort dimension for children and adolescents. This is followed by anxiety/depression, usual activities and mobility. Self-care seems to be far less important for children and adolescents, presumably because it is difficult to imagine what the problems with the self-care component might encapsulate in children and adolescents. Also, it might be difficult to imagine children and adolescents not being able to care for themselves to a level adults expect them to.

The representativeness of the DCE sample was controlled with regard to age, sex and region by formed quotas. The sample is not necessarily representative according to other variables, such as education, disease history or having children. It is difficult to say whether these further characteristics would impact the values of health states: having children could affect the preferences, depending on the degree of closeness between parents and children. Also, the respondents with higher education might understand the survey better, which could result in more credible and consistent results; however, their preferences might differ from those who are less educated, leading to biased results. Because the cTTO sample was not representative, sampling weights were applied. A more balanced group of respondents in terms of age or region could result in the anchor being at a different level.

One of the weaknesses of the study was that it was mainly conducted as an online survey. For this reason, it could not reach part of the population with limited access to the internet or those without sufficient technical skills, such as certain groups of the elderly population or those living in remote areas. Online survey methods have been linked to concerns about whether the participants properly engage with and understand the task \[35\]. As the researchers had no face-to-face contact with the participant, it was not possible to directly estimate any lack of understanding, engagement or interest of the participant in the task. To lower the impact of this limitation, we used the QC procedure as described.

Following the published international valuation protocol \[28\], the framing of the valuation task was “Considering your views of a 10-year-old child, which health state do you prefer?” The given age of the child (10 years) could influence the result of the valuation task, as the preferences of people could differ when considering an 8-year-old or a 15-year-old adolescent. Craig et al. \[26\] showed that the values attached to HRQoL losses differ according to the imagined ages of a child. The EQ-5D-Y-3L questionnaire was developed to measure the HRQoL of children and adolescents aged 8–15 years, and the specific age of 10 years was chosen to help the respondents imagine a child within the recommended age range. With such an instruction, the age of child that the respondent is thinking about is known to the researcher. The differences in health state values that adults attach to children of different ages within the EQ-5D-3L-Y recommended age brackets need to be explored further. Further research is also required to examine issues from previous studies (e.g. Kreimeier and Greiner \[36\]) that suggest values attached to health states may differ if a person is asked to value the health state for ‘your own child’, ‘a child you know’ or ‘a hypothetical child’.

## Conclusions

This study addresses a critical research gap and presents an EQ-5D-Y-3L value set for Slovenia that is, at the same time, the first EQ-5D-Y value set in the world. The value set presents adult preferences towards EQ-5D-Y health states in Slovenia, following the EQ-5D-Y-3L international valuation protocol. This childhood/adolescent EQ-5D-Y-3L value set should inform future cost-utility analyses in child and adolescent populations in Slovenia.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 27 KB)

</div>

## Acknowledgements

IMPACT HTA HRQoL Group: Wolfgang Greiner, Simone Kreimeier, Kristina Ludwig, Juan Manuel Ramos-Goni.

## Declarations

### Funding

This research was funded by the European Union’s Horizon 2020 research and innovation programme (H2020) and undertaken under the auspices of IMPACT_HTA (Grant number 779312; <http://www.impact-hta.eu>) and the EuroQol Group (EQ Project no. 20180510). The European Commission had no role in the study design, collection and analysis of data, the writing of the report or the submission of the paper for publication. The views expressed by the authors in the publication do not necessarily reflect the views of the EuroQol Group.

### Conflict of interest

Valentina Prevolnik Rupel, Wolfgang Greiner, Simone Kreimeier, Kristina Ludwig and Juan Manuel Ramos-Goni are members of the EuroQol organisation. Marko Ogorevc has no conflicts of interest that are directly relevant to the content of this article.

### Availability of data and material

All the data and material will be stored and publicly available at the certified data repository Zenodo, hosted by CERN.

### Code availability

Available from the authors on request.

### Author contributions

JMRG prepared the concept and the design of the study; all the authors contributed to the preparation of the material and data collection. The analysis was performed by VPR and MO. The first draft of the manuscript was written by VPR and MO, and all the authors commented on previous versions of the manuscript. All the authors read and approved the final manuscript.

### Ethics approval

The ethical approval for the research project using the DCE method was provided by the Committee of the Republic of Slovenia for Medical Ethics on 15 May 2018, No. 0120-154/2018/8, and annexed on 15 October 2019, No. 0120-154/2018/15. The ethical approval for the elicitation of preferences using the cTTO method was provided by the Committee of the Republic of Slovenia for Medical Ethics on 22 October 2019, No. 0120-471/2019/6.

## Footnotes

## Contributor Information

Valentina Prevolnik Rupel, Email: rupelv@ier.si.

IMPACT HTA HRQoL Group:

[Wolfgang Greiner]("Greiner W"[Author]), [Simone Kreimeier]("Kreimeier S"[Author]), [Kristina Ludwig]("Ludwig K"[Author]), and [Juan Manuel Ramos-Goni]("Ramos-Goni JM"[Author])

## References

## References

1. Heintz E, Gerber-Grote A, Ghabri S, Hamers FF, Prevolnik Rupel V, Slabe-Erker R, Davidson T. Is there a European View on Health Economic Evaluations? Results from a synopsis of methodological guidelines used in the EUnetHTA Partner countries. PharmacoEconomics. 2016;34:59–76. doi: 10.1007/s40273-015-0328-1.

2. Brazier J, Ratcliffe J, Salomon J, Tsuchiya A. Measuring and valuing health benefits for economic evaluation. Oxford: Oxford University Press; 2007.

3. Rabin R, de Charro F. EQ-5D: a measure of health status from the EuroQol Group. Ann Med. 2001;33:337–343. doi: 10.3109/07853890109002087.

4. Horsman J, Furlong W, Feeny D, Torrance G. The Health Utilities Index (HUI®): concepts, measurement properties and applications. Health Qual Life Outcomes. 2003;1:54. doi: 10.1186/1477-7525-1-54.

5. Brazier J, Roberts J, Deverill M. The estimation of a preference-based measure of health from the SF-36. J Health Econ. 2002;21(2):271–292. doi: 10.1016/S0167-6296(01)00130-8.

6. Sintonen H. The 15D instrument of health-related quality of life: properties and applications. Ann Med. 2001;33(5):328–336. doi: 10.3109/07853890109002086.

7. Hawthorne G, Richardson J, Osborne R. The Assessment of Quality of Life (AQoL) instrument: a psychometric measure of Health-Related Quality of Life. Qual Life Res. 1999;8:209–224. doi: 10.1023/A:1008815005736.

8. Prevolnik Rupel V, Srakar A, Rand K. Valuation of EQ-5D-3L health states in Slovenia: VAS based and TTO based value sets. Zdr Varst. 2020;59(1):8–17. doi: 10.2478/sjph-2020-0002.

9. Prevolnik Rupel V, Ogorevc M. Crosswalk EQ-5D-5L Value Set for Slovenia. Zdr Varst. 2020;59(3):189–194. doi: 10.2478/sjph-2020-0024.

10. Ungar W, Boydell K, Dell S. A parent-child dyad approach to the assessment of health status and health-related quality of life in children with asthma. PharmacoEconomics. 2012;30:697–712. doi: 10.2165/11597890-000000000-00000.

11. Chen G, Ratcliffe J. A review of the development and application of generic multi-attribute utility instruments for paediatric populations. Pharmacoeconomics. 2015;33:1013–1028. doi: 10.1007/s40273-015-0286-7.

12. Ravens-Sieberer U, Erhart M, Wille N, Wetzel R, Nickel J, Bullinger M. Generic health-related quality-of-life assessment in children and adolescents methodological considerations. Pharmacoeconomics. 2006;24(12):1199–1220. doi: 10.2165/00019053-200624120-00005.

13. Beusterien KM, Yeung JE, Pang F, Brazier J. Development of the multi-attribute Adolescent Health Utility Measure (AHUM) Health Qual Life Outcomes. 2012;10:102. doi: 10.1186/1477-7525-10-102.

14. Richardson J, Day NA, Peacock S, Iezzi A. Measurement of quality of life for economic evaluation and the Assessment of Quality of Life (AQoL) Mark 2 instrument. Aust Econ Hist Rev. 2004;37:62–88. doi: 10.1111/j.1467-8462.2004.00308.x.

15. Stevens K. Developing a descriptive system for a new preference-based measure of health-related quality of life for children. Qual Life Res. 2009;18(8):1105–1113. doi: 10.1007/s11136-009-9524-9.

16. Wille N, Badia X, Bonsel G, Bürstrom K, Cavrini G, Devlin N, et al. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual Life Res. 2010;19(6):875–886. doi: 10.1007/s11136-010-9648-y.

17. Torrance G, Feeny D, Furling W, Barr RD, Zhang Y, Wang Q. Multi-attribute utility function for a comprehensive health status classification system: Health Utilities Index Mark 2. Med Care. 1996;34:702–722. doi: 10.1097/00005650-199607000-00004.

18. Torrance GW, Furlong W, Feeny D, Boyle M. Multi-attribute preference functions: Health Utilities Index. Pharmacoeconomics. 1995;7:503–520. doi: 10.2165/00019053-199507060-00005.

19. Seiber WJ, Groessl EJ, David KM, Ganiats TG, Kaplan RM. Quality of Well-Being Self-Administered (QWB-SA) Scale: user’s manual. San Diego: University of California; 2008.

20. Apajasalo M, Sintonen H, Holmberg C, Sinkkonen J, Aalberg V, Pihko H, et al. Quality of life in early adolescence: a sixteen-dimensional health-related measure (16D) Qual Life Res. 1996;5:205–211. doi: 10.1007/BF00434742.

21. Apajasalo M, Rautonen J, Holmberg C, Sinkkonen J, Aalberg V, Pihko H, et al. Quality of life in pre-adolescence: a 17-dimensional health-related measure (17D) Qual Life Res. 1996;5:532–538. doi: 10.1007/BF00439227.

22. Ratcliffe J, Huynh E, Chen G, Stevens K, Swait J, Brazier J, et al. Valuing the child health utility 9D: using profile case best-worst scaling methods to develop a new adolescent specific scoring algorithm. Soc Sci Med. 2016;157:48–59. doi: 10.1016/j.socscimed.2016.03.042.

23. Canaway AG, Frew EJ. Measuring preference based quality of life in children aged 6–7 years: a comparison of the performance of the CHU-9D and EQ-5D-Y—the WAVES pilot study. Qual Life Res. 2013;22(1):173–183. doi: 10.1007/s11136-012-0119-5.

24. Thorrington D, Eames K. Measuring health utilities in children and adolescents: a systematic review of the literature. PLoS ONE. 2015;10(8):e0135672. doi: 10.1371/journal.pone.0135672.

25. Jelsma J, Ramma L. How do children at special schools and their parents perceive their HRQoL compared to children at open schools? Health Qual Life Outcomes. 2010;8:72. doi: 10.1186/1477-7525-8-72.

26. Craig BM, Greiner W, Brown DS, Reeve BB. Valuation of child health-related quality of life in the United States. Health Econ. 2016;25(6):768–777. doi: 10.1002/hec.3184.

27. Kreimeier S, Oppe M, Ramos-Goni JM, Cole A, Devlin N, Herdman M, et al. Valuation of EuroQol Five-Dimensional Questionnaire, Youth Version (EQ-5D-Y) and EuroQol Five-Dimensional Questionnaire, Three-Level Version (EQ-5D-3L) Health States: the impact of wording and perspective. Value Health. 2018;21(11):1291–1298. doi: 10.1016/j.jval.2018.05.002.

28. Ramos-Goni JM, Oppe M, Stolk E, Shah K, Kreimeier S, Rivero-Arias O, et al. International valuation protocol for the EQ-5D-Y-3L. PharmacoEconomics. 2020;38:1315–1325. doi: 10.1007/s40273-020-00909-3.

29. EuroQol Group. EQ-5D instruments. https://euroqol.org/eq-5d-instruments/eq-5d-y-available-modes-of-administration/. Accessed 15 Apr 2020.

30. Dalziel K, Catchpool M, García-Lorenzo B, Gorostiza I, Norman R, Rivero-Arias O. Feasibility, validity and differences in adolescent and adult EQ-5D-Y Health State Valuation in Australia and Spain: an Application of Best-Worst Scaling. PharmacoEconomics. 2020;38:499–513. doi: 10.1007/s40273-020-00884-9.

31. McCabe C, Stevens K, Roberts J, Brazier J. Health state values for the HUI 2 descriptive system: results from a UK survey. Health Econ. 2005;14(3):231–244. doi: 10.1002/hec.925.

32. Kind P, Klose K, Gusi N, Olivares PR, Greiner W. Can adult weights be used to value child health states? Testing the influence of perspective in valuing EQ-5D-Y. Qual Life Res. 2015;24:2519–2539. doi: 10.1007/s11136-015-0971-1.

33. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goñi JM. Overview, update, and lessons learned from the International EQ-5D-5L Valuation Work: Version 2 of the EQ-5D-5L Valuation Protocol. Value Health. 2019;22(1):23–30. doi: 10.1016/j.jval.2018.05.010.

34. Mott DJ, Rivero-Arias O, Shah K, Ramos-Gońi JM, Devlin NJ. Valuing the EQ-5D-Y using a discrete choice experiment: do adult and adolescent preferences differ? OHE Research Paper. London: Office of Health Economics; 2019. doi:10.1177/0272989X21999607

35. Jiang R, Shaw J, Mühlbacher A, Lee TA, Walton S, Kohlmann T, et al. Comparison of online and face-to-face valuation of the EQ-5D-5L using composite time trade-off. Qual Life Res. 2020;1–12. doi:10.1007/s11136-020-02712-1

36. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: the instrument’s characteristics, development, current use, and challenges of developing its value set. Value Health. 2019;22:31–37. doi: 10.1016/j.jval.2018.11.001.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 27 KB)

</div>

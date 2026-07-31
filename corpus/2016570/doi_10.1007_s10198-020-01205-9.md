---
project_id: "2016570"
work_id: "doi:10.1007/s10198-020-01205-9"
doi: "10.1007/s10198-020-01205-9"
pmid: "32506281"
pmcid: "PMC7423806"
title: "An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values"
journal: "The European Journal of Health Economics"
publication_date: "2020-06-06"
volume: "21"
issue: "7"
authors:
  - name: "Koonal K Shah"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
      - "Aff3"
  - name: "Juan Manuel Ramos-Goñi"
    affiliation_ids:
      - "Aff4"
      - "Aff5"
  - name: "Simone Kreimeier"
    affiliation_ids:
      - "Aff6"
  - name: "Nancy J Devlin"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
      - "Aff7"
affiliations:
  - id: "Aff1"
    name: "PHMR, London, UK"
  - id: "Aff2"
    name: "School of Health and Related Research, University of Sheffield, Sheffield, UK"
  - id: "Aff3"
    name: "Office of Health Economics, London, UK"
  - id: "Aff4"
    name: "Axentiva Solutions, Tacoronte, Spain"
  - id: "Aff5"
    name: "Office of the EuroQol Research Foundation, Rotterdam, Netherlands"
  - id: "Aff6"
    name: "School of Public Health, Bielefeld University, Bielefeld, Germany"
  - id: "Aff7"
    name: "School of Population and Global Health, University of Melbourne, Melbourne, Australia"
licence: "cc-by"
source_file: "input/projects/2016570/papers/doi_10.1007_s10198-020-01205-9.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7423806/fullTextXML"
source_method: "epmc_xml"
source_sha256: "8d9db24ac445adf37316e26f1bc8264d38faf465726d243c34ee73ed851c60eb"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values

## Abstract

### Objectives

Discrete choice experiments (DCEs) can be used to obtain latent scale values for the EQ-5D-Y, but these require anchoring at 0 = dead to meet the conventions of quality-adjusted life year (QALY) estimation. The primary aim of this study is to compare four preference elicitation methods for obtaining anchors for latent scale EQ-5D-Y values.

### Methods

Four methods were tested: visual analogue scale (VAS), DCE (with a duration attribute), lag-time time trade-off (TTO) and the location-of-dead (LOD) approach. In computer-assisted personal interviews, UK general public respondents valued EQ-5D-3L health states from an adult perspective and EQ-5D-Y health states from a 10-year-old child perspective. Respondents completed valuation tasks using all four methods, under both perspectives.

### Results

349 interviews were conducted. Overall, respondents gave lower values under the adult perspective compared to the child perspective, with some variation across methods. The mean TTO value for the worst health state (33333) was about equal to dead in the child perspective and worse than dead in the adult perspective. The mean VAS rescaled value for 33333 was also higher in the child perspective. The DCE produced positive child perspective values and negative adult perspective values, though the models were not consistent. The LOD median rescaled value for 33333 was negative under both perspectives and higher in the child perspective.

### Discussion

There was broad agreement across methods. Potential criteria for selecting a preferred anchoring method are presented. We conclude by discussing the decision-making circumstances under which utilities and QALY estimates for children and adults need to be commensurate to achieve allocative efficiency.

### Electronic supplementary material

The online version of this article (10.1007/s10198-020-01205-9) contains supplementary material, which is available to authorized users.

**Keywords:** EQ-5D-Y, Children, Valuation, Stated preferences, Quality-adjusted life year

Received 2019 Dec 23; Accepted 2020 May 27; Issue date 2020.

## Introduction

The EQ-5D-Y (Youth; three-level version[^1]) has been developed as a measure of health outcomes suitable for children and adolescents \[1, 2\]. However, no value sets are currently available, so EQ-5D-Y data cannot currently be used to estimate quality-adjusted life years (QALYs), as required for cost-utility analysis. The EuroQol Group has recognised the need to establish a protocol for conducting EQ-5D-Y valuation studies.

Two methodological EQ-5D-Y valuation studies undertaken to date—one using visual analogue scale (VAS) \[3\] and the other using composite time trade-off (C-TTO) and a discrete choice experiment (DCE) with death \[4\]—have reported somewhat contradictory results. Both studies reported differences in values elicited under adult health and child health perspectives (i.e. from respondents’ own perspective and imagining the health states from the perspective of a child, respectively), but in different directions: Kind et al. reported lower mean VAS ratings for the child perspective compared to the adult perspective, while Kreimeier et al. reported higher mean TTO values for the child perspective. The higher TTO values for the child perspective might have been driven by respondents’ aversion or unwillingness to trade off life years for a child (i.e. to choose to effectively shorten a child’s life). Both of the valuation techniques used by Kreimeier et al. included direct comparisons of health states with (immediate) death, whereas the VAS approach used by Kind et al. did not include any attempt to compare with or anchor at dead. Evidence from Kreimeier et al. suggests that relative preferences regarding dimensions/levels are different for the EQ-5D-3L elicited under the adult perspective and the EQ-5D-Y elicited under the child perspective. However, the authors did not find statistically significant differences across perspectives in the valuation of health state 33333 (the worst state in both the EQ-5D-3L and EQ-5D-Y descriptive systems). The Kind et al. study did not include health state 33333 in its design.

The ‘standard’ DCE (as opposed to DCE plus duration/death) seems to be a feasible solution for eliciting preferences under a child perspective as no time is attached to the health states, thus avoiding the issues raised by asking respondents to sacrifice the duration of a child’s life. Indeed, such preference data for the EQ-5D-Y have been collected from a sample of the UK general population, and are reported elsewhere \[5, 6\]. However, the DCE-estimated utilities based on those relative preferences are on an undefined scale, which cannot be used directly in QALY calculations \[7\]. Latent scale DCE data require an anchor point that must be obtained from an additional task or method.

Based on the evidence described above, a key question remains: if we are to use DCE for valuing EQ-5D-Y health states, what is the appropriate method for anchoring the resulting latent scale values? This study tests and compares four methods:

- Visual analogue scale (VAS).

- Lag-time TTO.

- Discrete choice experiment with duration (DCEd; described elsewhere as DCE<sub>TTO</sub> \[8\]).

- Location-of-dead (LOD) method, part of the personal utility function (PUF) approach.

The aims of the study are: to explore the use of these four alternative methods for establishing anchors and the resulting values for health state 33333; to compare anchors for the EQ-5D-3L/adult perspective and the EQ-5D-Y/child perspective; and to inform the development of a protocol for valuing the EQ-5D-Y.

## Methods

### Instruments

We used two versions of the EQ-5D instrument: the EQ-5D-3L \[9\] to describe adult health states and the EQ-5D-Y \[10\] to describe child health states. Both instruments comprise broadly the same five dimensions with three levels of response, usually coded 1, 2 and 3, producing health states that can be summarised using five-digit codes (profiles)—e.g. 11111 represents no problems in any dimension; 33333 represents the worst possible health state in either descriptive system. However, the instruments differ in wording. The EQ-5D-3L uses wording considered appropriate for adults, while the EQ-5D-Y was developed as an adaptation of the EQ-5D-3L for use in child and adolescent populations, with changes made to the labels for various dimension and level descriptions. For example, the ‘self-care’ and ‘anxiety/depression’ dimensions are re-labelled as ‘looking after myself’ and ‘feeling worried, sad or unhappy’ in the EQ-5D-Y (to avoid confusion, we use the adult labels throughout this manuscript). Further, three of the five level 3 descriptors in the EQ-5D-Y describe having ‘a lot of problems’ with the relevant health dimension. This contrasts with the EQ-5D-3L which refers to being ‘confined to bed’ or ‘unable to \[wash or dress myself/perform my usual activities\]’.

### Valuation techniques

There exists a broad range of valuation techniques that produce values on a scale anchored at 0 (dead) and 1 (full health). In this study, we focused on the four described below. The first three are widely used by health preference researchers \[11, 12\]. TTO and DCE are the methods currently favoured for the valuation of the EQ-5D-5L instrument \[7\], albeit different variants of those methods (composite TTO and DCE without duration, respectively) compared to the variants used in this study. VAS is a relatively simple, non-choice-based method, generally agreed to represent the most feasible of the various valuation techniques \[12\]. The fourth method—LOD—is a novel technique \[13\] considered promising by the authors for the purpose of establishing the location of the dead within a descriptive system.

These methods permit latent scale DCE data to be anchored using the value obtained for health state 33333. Other anchoring methods, such as mapping DCE values onto TTO, and combining DCE and TTO data in a hybrid model, have been examined elsewhere \[14\].

### VAS

The VAS exercise involves rating health states (lasting for 10 years, followed by death) or descriptors on a 0-to-100 scale (ranging from ‘The worst health you can imagine’ to ‘The best health you can imagine’). If ratings for ‘Dead’ and ‘11111’ are obtained, then the rating for health state h can be rescaled using the formula: (Rating<sub>h</sub> − Rating<sub>dead</sub>)/(Rating<sub>11111</sub> − Rating<sub>dead</sub>). The rescaled rating is upper bounded at 1 and anchored at 0 = dead.

### TTO

We used the lag-time variant of TTO \[15, 16\]. The lag-time TTO involves, as its starting point, a choice between 20 years in full health followed by death (life A) and 10 years in the EQ-5D health state under evaluation, followed by 10 years in full health (the ‘lag-time’), followed by death (option B). Respondents could indicate that they preferred life A, preferred life B, or considered both lives to be ‘about the same’. Depending on their choice, the amount of time in full health in life A was varied using the same iterative approach as used in the current EQ-5D-5L valuation protocol \[17\]. The task ended when the respondent indicated that life A and life B are about the same. The value for the health state could be calculated (assuming zero temporal discounting) as follows: *U* = (*t *− 10)/10, where *U* is the value (utility) and t is the number of years in full health in life A at the respondent’s point of indifference.

Lag-time TTO was used in favour of lead-time TTO (as used by Kreimeier et al. \[4\] for the valuation of worse-than-dead health states) because in the former the health state under evaluation occurs at the start of the time frame—i.e. if the scenario were to apply to a 10-year-old child, the health state would be experienced whilst the individual in question is still in childhood. However, in lead-time TTO the health state being evaluated occurs after 10 years of full health—i.e. the health state would not be experienced until adulthood. It is acknowledged that if a 10-year-old child enters a health state which then lasts for 10 years, then part of their time experiencing the health state would be in adulthood (particularly given that the EQ-5D-Y is designed for use in 8-to-15-year olds). However, it was deemed useful to maintain consistency with previous EQ-5D-Y valuation work, which had used standard 10-year timeframes \[4\].

### DCEd

The DCEd exercise comprised a series of forced-choice paired comparisons. Respondents were asked to choose which they preferred out of two EQ-5D health states, each lasting a specified duration (1, 3, 6 or 10 years), followed by death. No indifference option was available.

### LOD

The LOD exercise, developed as part of the PUF approach, seeks to locate each respondent’s position of the dead within a descriptive system. It is a simplified version of the approach used by Devlin et al. \[13\] and comprised two parts. First, a ranking task was presented requiring respondents to rank level 1 descriptors for each of the EQ-5D dimensions (e.g. ‘no pain or discomfort’) from ‘most important’ to ‘least important’, thereby asking respondents to consider on which dimensions it was most important to avoid problems. Ties were not permitted. Second, a series of forced-choice paired comparison tasks were presented, each involving a choice between living in a specified EQ-5D health state lasting 10 years (followed by death) and 0 years of life (i.e. immediate death). The information gathered in the ranking task was used to personalise the selection of the health states presented in the paired comparison tasks. This was done via a simple algorithm that applied a rating of 100 to the highest-ranked dimension and progressively smaller ratings to the second, third, fourth and bottom-ranked dimensions. Each rating was then weighted by 1, 0.5 or 0 depending on whether they applied to levels 1, 2 or 3 for the relevant dimension. The weighted ratings were summed to generate a total score for each of the 243 possible health states, thereby allowing a personalised ranking of those health states. The paired comparison tasks were designed to identify the individual’s dividing line between states considered to be better or worse than dead. Hence, the ranking task responses played an indirect role in determining the anchor points using the LOD method.

### Study design

All respondents completed all valuation tasks using two different perspectives. In the adult perspective, they were asked to consider their own health, with the EQ-5D-3L instrument used to describe the health states. In the child perspective, they were asked to consider the health of a 10-year-old child, with the EQ-5D-Y instrument used to describe the health states, following the approach used in previous research \[4, 5\]. No specific instruction was provided about the identity of the 10-year-old child. Half of the respondents were randomly allocated to completing the tasks for the adult perspective first; the other half completed the tasks for the child perspective first. At the half-way point, a pop-up message appeared on the screen advising respondents of the change in perspective. Interviewers were also instructed to advise respondents of this change.

The survey design (Fig. <a href="#Fig1" data-ref-type="fig">1</a>) was developed with the view to minimising respondent burden: given the relatively large number of valuation techniques and perspectives being used, we opted to minimise the numbers of tasks for each valuation technique:

1.  Ranking—single task involving ranking of EQ-5D level 1 descriptors (as needed for the LOD technique).

2.  VAS—ratings for 33333 and Dead. With these two ratings, and assuming that the rating for 11111 is 100 (assumption not tested as part of this study), we were able to calculate an anchored value for 33333.

3.  Lag-time TTO—valuations for 22,222 (as a warm-up task) and 33333. Note that the TTO technique produced values on the 0 and 1 anchored scale.

4.  DCEd—this technique does not produce values directly. Values were estimated by modelling; therefore, a specific experimental design was needed. We used a six-step approach. First, we prepared the set of all 2430 possible candidates with an overlap in two dimensions, no dominant pairs and no repetitions. Second, we simulated 2000 designs each including 42 pairs. Using the D-efficiency measure based on a main effects model, we extracted all pairs included in the best 20 designs. Third, based on priors from Rivero-Arias et al. \[5\] we estimated the choice probabilities for the pairs from step 2. Fourth, using these estimated probabilities, we divided those pairs into three categories: (a) *P* ≤  0.2; (b) 0.2 \< *P* ≤  0.35; and (c) 0.35 \< *P* ≤  0.5 (same for *P* \> 0.5 applies to B state). For (a) we used the high distance between durations of each pair (i.e. 1 year in one state versus 10 years in the other) with the longer duration for the less likely state. For (b), we used a small distance between durations of each pair and the longer duration is for the less likely state. For (c), we used all possible combinations of durations (1, 3, 6, 10 years). Fifth, based on the Bansback et al. model \[18\], where the time was an interaction, we simulated 2000 designs with all possible pairs and selected the best based on the D-efficiency measure. Finally, we blocked the design into six blocks (thereby allocating seven DCE pairs to be completed by each respondent) by minimising the variance of the level balance between blocks. We used the same design for both perspectives.

5.  LOD—this technique does not produce values directly. Respondents were asked to complete up to five paired comparison tasks, each involving a choice between 10 years in a specified health state followed by death (option A) and 0 years/immediate death (option B). No indifference option was available. The health states presented were selected based on a simple algorithm that used each respondent’s responses to the earlier ranking task to generate a personalised ranking of all 243 health states—see above. The algorithm assumed an equal distance (in utility terms) between each dimension rank (i.e. the difference between the first- and second-ranked dimensions was deemed equal to the difference between the second- and third-ranked dimensions), and between levels (i.e. the difference between level 3 and level 2 was deemed equal to the difference between level 2 and level 1). A random number function was used to break ties to generate the ranking. The health state presented in the first task was always 33333 (ranked 243rd for all respondents). Respondents choosing 33333 over immediate death were not given further choice tasks but were asked if they could think of any health problems that were so bad that they would rather choose immediate death, and if so, to describe those problems using an open-ended text box. Respondents choosing immediate death over 33333 proceeded to a second task in which 33333 was replaced by the health state ranked 122nd (half-way between 1st and 243rd; this health state varied from respondent to respondent). In the subsequent tasks, the health state presented either improved or worsened in ranking/estimated personal utility depending on the respondent’s choice in the previous task. An iterative bisection procedure was used for this purpose \[19\]. Following the fifth task, each respondent’s location of dead could be estimated to be within a range comprising 15–16 health states.

<figure id="Fig1">
<p><img src="10198_2020_1205_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="10198_2020_1205_Fig1_HTML.gif" /></p>
<figcaption>Ordering of the tasks for respondents randomised to the ‘adult perspective first’ arm</figcaption>
</figure>

The adult perspective and EQ-5D-3L were used since the aim of the study was to compare anchor points across instruments. However, a small number of additional interviews (*n* = 50), using an otherwise identical survey design, were conducted with respondents valuing EQ-5D-Y health states throughout, in both the adult and the child perspectives. This allowed a comparison of the data collected using different perspectives whilst controlling for the descriptive system. Results relating to this ‘extended sample’ are provided in the supplementary appendix.

The valuation tasks were preceded by a small number of warm-up and background questions and followed by debrief and further background questions.

### Data collection

Data were collected from members of the UK general population. The survey was administered via the EuroQol Group Valuation Technology (EQ-VT) platform. The EQ-VT was used as the basis for computer-assisted, one-to-one personal interviews in the homes of respondents, undertaken by a team of five experienced interviewers. The interviewers completed a 1-day training session on the methodology and procedures for this study and were asked to follow step-by-step instructions and a script to minimise interviewer bias.

The main data collection was preceded by a pilot, which comprised nine cognitive interviews. In addition to completing the valuation tasks using the adapted EQ-VT, pilot respondents were asked probing questions about how they interpreted the tasks, what they found difficult, and how the questionnaire could be improved. All the cognitive interviews were undertaken by two moderators with expertise in qualitative research methods and were carried out in the offices of the moderators’ employer. The cognitive interviews were audio recorded and transcribed. Some minor improvements were made to the software (e.g. amendment of on-screen explanatory text) based on the findings of the pilot.

An adapted version of the quality control process developed for EQ-5D-5L valuation studies \[20\] was followed to ensure protocol compliance. Ethics approval for the survey and data collection procedures was granted by the Ethics Committee of the University of Sheffield’s School of Health and Related Research (approval reference: 011675).

### Sample

Sample size calculations were based on requirements to estimate DCEd models. We estimated that a minimum of 300 (50 × 6) respondents would be needed assuming a requirement of about 50 observations for each of the six blocks of pairs included in the DCEd design. We took the average of two rule of thumb recommendations—by Lancsar and Louviere \[21\] (minimum 20 observations per pair) and Hensher et al. \[22\] (minimum 30 observations per pair)—and doubled that average to be conservative. The sample comprised adult members of the general population (aged 18 years and older) in two regions in the UK (Midlands and London/Southeast). The sample was recruited using a ‘door knock’ approach, with interviewers approaching a household member of every third home in a randomly allocated postal area and scheduling interview appointments for those individuals that agreed to participate. A recruitment questionnaire was used to ensure that the sample was broadly representative of the general population in terms of age and gender. Respondents received a shopping voucher worth GBP £10 to thank them for their participation.

The sample for the pilot comprised adult members of the general population in London, recruited using a mixed on-street and ‘door knock’ approach. Pilot respondents received a shopping voucher worth GBP £40 to thank them for their participation.

### Analysis

Sample background characteristics were described using frequencies and percentages. Box plots were used for describing and comparing lag-time TTO and rescaled VAS values for 33333. TTO values observed at 0 and − 1 were not treated as censored. The DCEd data were described using observed choice probabilities for each of the pairs included in the design. DCEd values for 33333 were calculated via different models, including the regular conditional logit model, and conditional logit models assuming non-constant proportionality \[23\]. We estimated models assuming a fixed ½ power and allowing the model to estimate the best-fitted power. Further details of the modelling can be found in Table A3 of the Supplementary Appendix.

Each respondent’s set of choices in the LOD tasks resulted in a range of states within which dead was deduced to be located (for example, for respondents who chose option A in the first task and option B in all subsequent tasks, it was deduced that they located dead between the 228th and the 243rd health states within their own personal ranking). This approach was not possible for respondents who chose option B in the first LOD task, implying that they located dead below 33333 and, therefore, beyond the descriptive system. For each of the 16 deduced regions, the midpoint rank of the range was calculated and the latent utility corresponding to that midpoint was estimated based on the mixed logit model results from the EQ-5D-Y latent scale DCE study reported by Rivero-Arias et al. \[5\]. This was done by summing the Rivero-Arias et al. coefficients/disutilities for the relevant dimension-levels for each of the 243 health states. That study produced latent utilities based on the DCE responses of a different sample from the present study (albeit also a representative sample of the UK general public), so combining the data in this way relies on an assumption that respondents in the present study would have responded in the same way as respondents in the Rivero-Arias et al. study had they completed a similar DCE survey. These latent utilities ranged from 0 (corresponding to 11111) to − 9.306 (corresponding to 33333; i.e. sum of the five level 3 coefficients/disutilities reported by Rivero-Arias et al.). The value for 33333 was then rescaled onto the 0 (dead) and 1 (full health) scale using the formula: rescaled<sub>33333</sub> = (latent<sub>33333 </sub>− latent<sub>dead</sub>)/(latent<sub>11111 </sub>− latent<sub>dead</sub>).

Analyses were undertaken using Microsoft Excel and Stata software.

## Results

The main interviews were conducted between September and December 2017. The sample comprised 299 respondents; a further respondent found the subject matter distressing during the interview and asked to withdraw from the study. No respondents who completed their interview in full were excluded. The mean (median) duration of the interview was 40.0 (39.1) minutes. The sample was broadly representative of the general population in terms of age and gender \[24\], though the oldest individuals (aged 70 years and over) are slightly underrepresented (Table <a href="#Tab1" data-ref-type="table">1</a>). The majority of the respondents are parents, though in many cases their children are now adults.

<div id="Tab1" class="table-wrap">

<div class="caption">

Sample background characteristics

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Sample</th>
<th style="text-align: left;">Population</th>
</tr>
<tr>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Age</td>
</tr>
<tr>
<td style="text-align: left;"> 18–29</td>
<td style="text-align: center;">58</td>
<td style="text-align: center;">19.4</td>
<td style="text-align: left;">20.0</td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td style="text-align: center;">55</td>
<td style="text-align: center;">18.4</td>
<td style="text-align: left;">16.8</td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">14.7</td>
<td style="text-align: left;">17.1</td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td style="text-align: center;">60</td>
<td style="text-align: center;">20.1</td>
<td style="text-align: left;">16.7</td>
</tr>
<tr>
<td style="text-align: left;"> 60–69</td>
<td style="text-align: center;">45</td>
<td style="text-align: center;">15.1</td>
<td style="text-align: left;">13.7</td>
</tr>
<tr>
<td style="text-align: left;"> 70+</td>
<td style="text-align: center;">37</td>
<td style="text-align: center;">12.4</td>
<td style="text-align: left;">15.8</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Gender</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: center;">151</td>
<td style="text-align: center;">50.5</td>
<td style="text-align: left;">51.1</td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: center;">148</td>
<td style="text-align: center;">49.5</td>
<td style="text-align: left;">48.9</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Experience of serious illness</td>
</tr>
<tr>
<td style="text-align: left;"> In self</td>
<td style="text-align: center;">69</td>
<td style="text-align: center;">23.1</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> In family</td>
<td style="text-align: center;">190</td>
<td style="text-align: center;">63.5</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> In caring for others</td>
<td style="text-align: center;">77</td>
<td style="text-align: center;">25.8</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Self-reported EQ-5D profile</td>
</tr>
<tr>
<td style="text-align: left;"> 11111</td>
<td style="text-align: center;">184</td>
<td style="text-align: center;">62.5</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> Any other health state</td>
<td style="text-align: center;">112</td>
<td style="text-align: center;">37.5</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Children</td>
</tr>
<tr>
<td style="text-align: left;"> No children</td>
<td style="text-align: center;">66</td>
<td style="text-align: center;">22.1</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> Youngest child is &lt; 11 years</td>
<td style="text-align: center;">84</td>
<td style="text-align: center;">28.1</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> Youngest child is 11–18 years</td>
<td style="text-align: center;">25</td>
<td style="text-align: center;">8.4</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> Youngest child is &gt; 18 years</td>
<td style="text-align: center;">124</td>
<td style="text-align: center;">41.5</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Experience of working with children</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: center;">60</td>
<td style="text-align: center;">20.1</td>
<td style="text-align: left;">N/A</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">79.9</td>
<td style="text-align: left;">N/A</td>
</tr>
</tbody>
</table>

</div>

### Ranking

Anxiety/depression was the highest-ranked (considered the most important) dimension on average (i.e. based on mean rank) in the child perspective but only the third-highest ranked in the adult perspective. In the adult perspective, usual activities was the highest-ranked dimension; this was the third-highest ranked in the child perspective. Mobility was found to be the lowest-ranked (least important) dimension on average under both perspectives.

### VAS

On average, VAS ratings and values (rescaled ratings) given to 33333 were higher in the child perspective than in the adult perspective (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). A clear majority of respondents considered 33333 to be better than dead when answering from a child perspective; whereas under the adult perspective the most common response was to rate 33333 as worse than dead.

<figure id="Fig2">
<p><img src="10198_2020_1205_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="10198_2020_1205_Fig2_HTML.gif" /></p>
<figcaption>Box-plots of TTO and rescaled VAS values for health state 33333<sup>a</sup>. <sup>a</sup>One outlier VAS value lower than − 3 was removed from the graph for scaling purposes</figcaption>
</figure>

### TTO

The average value given to 33333 in the child perspective was close to 0 (or, taking the median, exactly 0), whereas in the adult perspective the average value was clearly negative. The majority of respondents gave a higher value to 33333 in the child perspective than in the adult perspective (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). Four of the 349 respondents (1.1%) gave a lower value to 22,222 than to 33333. Excluding these ‘inconsistent’ respondents lowered the mean value for 33333 by 0.006 in the child perspective, while the corresponding difference in the adult perspective was even smaller (0.003).

### DCEd

DCEd model results were in line with VAS and TTO results to the extent that values for 33333 were negative for the adult perspective and positive for the child perspective (this result was consistent across all models). Observed choice probabilities showed a preference for longer life duration in the child perspective (Table <a href="#Tab2" data-ref-type="table">2</a>). This preference for longer duration meant that models were not consistent (i.e. some logically worse health states have higher utilities than logically better, or dominant, health states) in the child perspective. It seems that respondents focused more on the duration of the lives than to the health problems described. The DCEd results indicate that respondents generally avoided shorter life durations and problems with pain/discomfort when considering the health of a 10-year-old child, whereas they focused on problems with mobility and pain/discomfort when considering their own (adult) health.

<div id="Tab2" class="table-wrap">

<div class="caption">

Discrete choice experiment with duration observed choice probabilities

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Health state 1</th>
<th rowspan="2" style="text-align: left;">Years in health state 1</th>
<th rowspan="2" style="text-align: left;">Health state 2</th>
<th rowspan="2" style="text-align: left;">Years in health state 2</th>
<th colspan="3" style="text-align: left;">EQ-5D-3L —&gt; Adult perspective vs EQ-5D-Y —&gt; Child perspective</th>
<th colspan="3" style="text-align: left;">EQ-5D-Y —&gt; Adult perspective vs EQ-5D-Y —&gt; Child perspective</th>
</tr>
<tr>
<th style="text-align: left;">Adult perspective</th>
<th style="text-align: left;">Child perspective</th>
<th style="text-align: left;">Diff adult–child</th>
<th style="text-align: left;">Adult perspective</th>
<th style="text-align: left;">Child perspective</th>
<th style="text-align: left;">Diff adult–child</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">11321</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">31211</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.633</td>
<td style="text-align: left;">0.653</td>
<td style="text-align: left;">− 0.020</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">11321</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">31211</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.479</td>
<td style="text-align: left;">0.313</td>
<td style="text-align: left;">0.167</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">11322</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">12221</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.540</td>
<td style="text-align: left;">0.540</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">11323</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">31222</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.563</td>
<td style="text-align: left;">0.604</td>
<td style="text-align: left;">− 0.042</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.667</td>
<td style="text-align: left;">0.167</td>
</tr>
<tr>
<td style="text-align: left;">12112</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">11213</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.438</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.417</td>
<td style="text-align: left;">− 0.083</td>
</tr>
<tr>
<td style="text-align: left;">12122</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">31112</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.569</td>
<td style="text-align: left;">0.549</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">12211</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">11222</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.404</td>
<td style="text-align: left;">0.447</td>
<td style="text-align: left;">− 0.043</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">12313</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">13111</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.447</td>
<td style="text-align: left;">0.553</td>
<td style="text-align: left;">− 0.106</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.125</td>
</tr>
<tr>
<td style="text-align: left;">12322</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">32221</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.596</td>
<td style="text-align: left;">0.617</td>
<td style="text-align: left;">− 0.021</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.250</td>
</tr>
<tr>
<td style="text-align: left;">13113</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">22112</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.633</td>
<td style="text-align: left;">0.653</td>
<td style="text-align: left;">− 0.020</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.375</td>
</tr>
<tr>
<td style="text-align: left;">13233</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">33113</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.588</td>
<td style="text-align: left;">0.510</td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;">0.667</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">− 0.333</td>
</tr>
<tr>
<td style="text-align: left;">13331</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">23211</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.451</td>
<td style="text-align: left;">0.510</td>
<td style="text-align: left;">− 0.059</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.167</td>
<td style="text-align: left;">− 0.167</td>
</tr>
<tr>
<td style="text-align: left;">13332</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">22322</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.426</td>
<td style="text-align: left;">0.574</td>
<td style="text-align: left;">− 0.149</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.250</td>
</tr>
<tr>
<td style="text-align: left;">13332</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">32312</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">0.519</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">21133</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">22122</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.521</td>
<td style="text-align: left;">− 0.021</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">21223</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">31211</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">0.537</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.375</td>
</tr>
<tr>
<td style="text-align: left;">21233</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">21322</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.556</td>
<td style="text-align: left;">0.481</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">− 0.125</td>
</tr>
<tr>
<td style="text-align: left;">21322</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">31311</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.480</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">− 0.125</td>
</tr>
<tr>
<td style="text-align: left;">22233</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">31133</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.429</td>
<td style="text-align: left;">0.388</td>
<td style="text-align: left;">0.041</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">22323</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">31321</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.520</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.125</td>
</tr>
<tr>
<td style="text-align: left;">22332</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">23311</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.438</td>
<td style="text-align: left;">0.396</td>
<td style="text-align: left;">0.042</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.250</td>
</tr>
<tr>
<td style="text-align: left;">22333</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">23132</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.519</td>
<td style="text-align: left;">0.519</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">23111</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">13331</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.490</td>
<td style="text-align: left;">0.408</td>
<td style="text-align: left;">0.082</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.250</td>
</tr>
<tr>
<td style="text-align: left;">23213</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">31211</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.551</td>
<td style="text-align: left;">0.633</td>
<td style="text-align: left;">− 0.082</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.125</td>
</tr>
<tr>
<td style="text-align: left;">23223</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">32123</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.611</td>
<td style="text-align: left;">0.407</td>
<td style="text-align: left;">0.204</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.125</td>
</tr>
<tr>
<td style="text-align: left;">23312</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">31311</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.468</td>
<td style="text-align: left;">0.404</td>
<td style="text-align: left;">0.064</td>
<td style="text-align: left;">0.750</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">− 0.250</td>
</tr>
<tr>
<td style="text-align: left;">23321</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">22333</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.553</td>
<td style="text-align: left;">0.426</td>
<td style="text-align: left;">0.128</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.125</td>
</tr>
<tr>
<td style="text-align: left;">31111</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">21212</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.520</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">31111</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">21123</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.354</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.583</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">− 0.250</td>
</tr>
<tr>
<td style="text-align: left;">31111</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">12112</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.313</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.083</td>
</tr>
<tr>
<td style="text-align: left;">31111</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">11312</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.388</td>
<td style="text-align: left;">0.327</td>
<td style="text-align: left;">0.061</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.125</td>
</tr>
<tr>
<td style="text-align: left;">31231</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">33111</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.556</td>
<td style="text-align: left;">0.481</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">31233</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">32221</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.400</td>
<td style="text-align: left;">0.540</td>
<td style="text-align: left;">− 0.140</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">− 0.125</td>
</tr>
<tr>
<td style="text-align: left;">31323</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">32122</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">0.420</td>
<td style="text-align: left;">0.480</td>
<td style="text-align: left;">− 0.060</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">32111</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">23311</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.389</td>
<td style="text-align: left;">0.370</td>
<td style="text-align: left;">0.019</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">− 0.125</td>
</tr>
<tr>
<td style="text-align: left;">32133</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">13233</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.431</td>
<td style="text-align: left;">0.471</td>
<td style="text-align: left;">− 0.039</td>
<td style="text-align: left;">0.167</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.333</td>
</tr>
<tr>
<td style="text-align: left;">32211</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">13212</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.383</td>
<td style="text-align: left;">0.404</td>
<td style="text-align: left;">− 0.021</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.625</td>
<td style="text-align: left;">0.125</td>
</tr>
<tr>
<td style="text-align: left;">33122</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">23332</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.431</td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.667</td>
<td style="text-align: left;">0.167</td>
</tr>
<tr>
<td style="text-align: left;">33211</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">33132</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.520</td>
<td style="text-align: left;">0.480</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.375</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">33212</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">23233</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.490</td>
<td style="text-align: left;">0.408</td>
<td style="text-align: left;">0.082</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">− 0.250</td>
</tr>
<tr>
<td style="text-align: left;">33212</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">13223</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">0.392</td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;">− 0.020</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;">33212</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">23223</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0.451</td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;">0.500</td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">− 0.167</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Predicted values for 33333</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"> Logit model</td>
<td style="text-align: left;">− 0.796</td>
<td style="text-align: left;">0.059</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"> Power model (power = 1/2)</td>
<td style="text-align: left;">− 0.468</td>
<td style="text-align: left;">0.280</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"> Power model (power = 0.296)</td>
<td style="text-align: left;">− 0.227</td>
<td style="text-align: left;">0.188</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

Models coefficients are reported in the Appendix (Table A1)

</div>

### LOD

One respondent (0.3%) chose option B in all of the LOD tasks, implying that all of the health states presented were worse than dead. Conversely, a sizeable minority of respondents chose option A in the first task, implying that 33333 is better than dead. The proportion of respondents making this choice was higher in the child perspective (32.8%) than in the adult perspective (23.1%). When asked if they could think of any health states that were so bad that they would rather choose immediate death, 57.0% of the respondents in the child perspective and 53.6% of respondents in the adult perspective said that they could. Most of the descriptions of these ‘worse than dead’ states—in both the child and adult perspectives—focused on being in vegetative states and/or having severe brain damage.

Overall, dead was located lower in the descriptive system in the child perspective than in the adult perspective, resulting in higher rescaled values (Table <a href="#Tab3" data-ref-type="table">3</a>)—in other words, respondents located dead amongst more severe health states in the child perspective. The mean rescaled values shown in Table <a href="#Tab3" data-ref-type="table">3</a> underestimate the actual value for 33333, since they do not take into account the fact that for respondents who chose option A in the first task, the rescaled value for 33333 should be positive. Including such positive values would have an upward effect on the mean; it is worth noting that this effect would be stronger in the child perspective since more respondents chose option A in the first task in this version. The median rescaled values are unaffected by this issue since the median respondent chose option B on at least one occasion.

<div id="Tab3" class="table-wrap">

<div class="caption">

Summary of LOD results

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Set of choices</th>
<th rowspan="3" style="text-align: left;">Deduced range in which dead is located</th>
<th rowspan="3" style="text-align: left;">Midpoint of deduced range (rank)</th>
<th rowspan="3" style="text-align: left;">Latent utility of midpoint</th>
<th rowspan="3" style="text-align: left;">Rescaled utility for 33333</th>
<th colspan="4" style="text-align: left;"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Adult perspective</th>
<th colspan="2" style="text-align: left;">Child perspective</th>
</tr>
<tr>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">BBBBB</td>
<td style="text-align: left;">1st to 17th ranked states</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">− 1.015</td>
<td style="text-align: left;">− 8.170</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.0</td>
</tr>
<tr>
<td style="text-align: left;">BBBBA</td>
<td style="text-align: left;">17th to 32nd ranked states</td>
<td style="text-align: left;">24.5</td>
<td style="text-align: left;">− 1.826</td>
<td style="text-align: left;">− 4.098</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">2.0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.0</td>
</tr>
<tr>
<td style="text-align: left;">BBBAB</td>
<td style="text-align: left;">32nd to 47th ranked states</td>
<td style="text-align: left;">39.5</td>
<td style="text-align: left;">− 2.290</td>
<td style="text-align: left;">− 3.064</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">1.3</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.3</td>
</tr>
<tr>
<td style="text-align: left;">BBBAA</td>
<td style="text-align: left;">47th to 62nd ranked states</td>
<td style="text-align: left;">54.5</td>
<td style="text-align: left;">− 2.690</td>
<td style="text-align: left;">− 2.459</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">5.4</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">3.0</td>
</tr>
<tr>
<td style="text-align: left;">BBABB</td>
<td style="text-align: left;">62nd to 77th ranked states</td>
<td style="text-align: left;">69.5</td>
<td style="text-align: left;">− 3.048</td>
<td style="text-align: left;">− 2.053</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">2.0</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">0.3</td>
</tr>
<tr>
<td style="text-align: left;">BBABA</td>
<td style="text-align: left;">77th to 92nd ranked states</td>
<td style="text-align: left;">84.5</td>
<td style="text-align: left;">− 3.415</td>
<td style="text-align: left;">− 1.725</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">5.0</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">4.3</td>
</tr>
<tr>
<td style="text-align: left;">BBAAB</td>
<td style="text-align: left;">92nd to 107th ranked states</td>
<td style="text-align: left;">99.5</td>
<td style="text-align: left;">− 3.728</td>
<td style="text-align: left;">− 1.496</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">3.0</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">1.7</td>
</tr>
<tr>
<td style="text-align: left;">BBAAA</td>
<td style="text-align: left;">107th to 122nd ranked states</td>
<td style="text-align: left;">114.5</td>
<td style="text-align: left;">− 4.033</td>
<td style="text-align: left;">− 1.307</td>
<td style="text-align: left;">25</td>
<td style="text-align: left;">8.4</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">6.4</td>
</tr>
<tr>
<td style="text-align: left;">BABBB</td>
<td style="text-align: left;">122nd to 138th ranked states</td>
<td style="text-align: left;">130</td>
<td style="text-align: left;">− 4.399</td>
<td style="text-align: left;">− 1.116</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">1.3</td>
</tr>
<tr>
<td style="text-align: left;">BABBA</td>
<td style="text-align: left;">138th to 153rd ranked states</td>
<td style="text-align: left;">145.5</td>
<td style="text-align: left;">− 4.717</td>
<td style="text-align: left;">− 0.973</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">3.0</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">3.7</td>
</tr>
<tr>
<td style="text-align: left;">BABAB</td>
<td style="text-align: left;">153rd to 168th ranked states</td>
<td style="text-align: left;">160.5</td>
<td style="text-align: left;">− 5.005</td>
<td style="text-align: left;">− 0.859</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">4.7</td>
</tr>
<tr>
<td style="text-align: left;">BABAA</td>
<td style="text-align: left;">168th to 183rd ranked states</td>
<td style="text-align: left;">175.5</td>
<td style="text-align: left;">− 5.383</td>
<td style="text-align: left;">− 0.729</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">6.0</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">6.0</td>
</tr>
<tr>
<td style="text-align: left;">BAABB</td>
<td style="text-align: left;">183rd to 198th ranked states</td>
<td style="text-align: left;">190.5</td>
<td style="text-align: left;">− 5.776</td>
<td style="text-align: left;">− 0.611</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">5.7</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">4.7</td>
</tr>
<tr>
<td style="text-align: left;">BAABA</td>
<td style="text-align: left;">198th to 213th ranked states</td>
<td style="text-align: left;">205.5</td>
<td style="text-align: left;">− 6.218</td>
<td style="text-align: left;">− 0.497</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">6.0</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">7.0</td>
</tr>
<tr>
<td style="text-align: left;">BAAAB</td>
<td style="text-align: left;">213th to 228th ranked states</td>
<td style="text-align: left;">220.5</td>
<td style="text-align: left;">− 6.822</td>
<td style="text-align: left;">− 0.364</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">7.0</td>
<td style="text-align: left;">20</td>
<td style="text-align: left;">6.7</td>
</tr>
<tr>
<td style="text-align: left;">BAAAA</td>
<td style="text-align: left;">228th to 243rd ranked states</td>
<td style="text-align: left;">235.5</td>
<td style="text-align: left;">− 7.825</td>
<td style="text-align: left;">− 0.189</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">14.4</td>
<td style="text-align: left;">51</td>
<td style="text-align: left;">17.1</td>
</tr>
<tr>
<td style="text-align: left;">A</td>
<td style="text-align: left;">Dead cannot be located using LOD tasks</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">69</td>
<td style="text-align: left;">23.1</td>
<td style="text-align: left;">98</td>
<td style="text-align: left;">32.8</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Mean rescaled utility for 33333 (excluding respondents who considered 33333 to be better than dead)</td>
<td colspan="2" style="text-align: left;">− 1.076</td>
<td colspan="2" style="text-align: left;">− 0.787</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Mean rescaled utility for 33333 (assuming a rescaled utility of 0 for respondents who considered 33333 to be better than dead)</td>
<td colspan="2" style="text-align: left;">− 0.828</td>
<td colspan="2" style="text-align: left;">− 0.529</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Median rescaled utility for 33333</td>
<td colspan="2" style="text-align: left;">− 0.497</td>
<td colspan="2" style="text-align: left;">− 0.364</td>
</tr>
</tbody>
</table>

</div>

### Comparison across methods

It is possible to report whether each individual respondent valued 33333 as better than dead via the TTO, VAS and LOD tasks (Table <a href="#Tab4" data-ref-type="table">4</a>). Respondents were more likely to value 33333 as better than dead in the child perspective than in the adult perspective. This finding was consistent across all three methods. Respondents valued 33333 as better than dead via VAS more frequently than via the other two methods. The majority of respondents did not provide internally consistent valuations, in that they valued 33333 as better than dead via one of the methods but as worse than or equal to dead via another of the methods.

<div id="Tab4" class="table-wrap">

<div class="caption">

Comparison across methods: valuation of 33333 in relation to 0 = dead

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Child perspective</th>
<th colspan="2" style="text-align: left;">Adult perspective</th>
<th colspan="2" style="text-align: left;">Both perspectives</th>
</tr>
<tr>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">TTO—respondents valuing 33333 as better than dead</td>
<td style="text-align: center;">125</td>
<td style="text-align: center;">41.8</td>
<td style="text-align: center;">68</td>
<td style="text-align: center;">22.7</td>
<td style="text-align: center;">59</td>
<td style="text-align: center;">19.7</td>
</tr>
<tr>
<td style="text-align: left;">VAS—respondents valuing 33333 as better than dead</td>
<td style="text-align: center;">210</td>
<td style="text-align: center;">70.2</td>
<td style="text-align: center;">110</td>
<td style="text-align: center;">36.8</td>
<td style="text-align: center;">96</td>
<td style="text-align: center;">32.1</td>
</tr>
<tr>
<td style="text-align: left;">LOD—respondents valuing 33333 as better than dead</td>
<td style="text-align: center;">98</td>
<td style="text-align: center;">32.8</td>
<td style="text-align: center;">69</td>
<td style="text-align: center;">23.1</td>
<td style="text-align: center;">65</td>
<td style="text-align: center;">21.7</td>
</tr>
<tr>
<td style="text-align: left;">All three methods—respondents providing internally consistent valuations<sup>a</sup></td>
<td style="text-align: center;">109</td>
<td style="text-align: center;">36.5</td>
<td style="text-align: center;">159</td>
<td style="text-align: center;">53.2</td>
<td style="text-align: center;">70</td>
<td style="text-align: center;">23.4</td>
</tr>
</tbody>
</table>

<sup>a</sup>i.e. 33333 valued as better than dead using all three methods OR 33333 valued as worse than or equal to dead across all three methods

</div>

### Debrief questions

The majority of respondents (81.9%) found the child perspective questions more difficult, with a slight majority (54.5%) claiming that they found it somewhat or very difficult to imagine the health of a 10-year-old child (Table <a href="#Tab5" data-ref-type="table">5</a>). Respondents were varied in terms of what sort of child they were thinking of; the most common approach was to think of ‘no particular child’. The vast majority of respondents (81.6%) claimed that their responses might have been different if they had been asked to consider a child of different age, though no information is available about how their responses would have differed. The majority of respondents (62.9%) indicated that the health system should give equal priority to the treatment of adults and children.

<div id="Tab5" class="table-wrap">

<div class="caption">

Responses to debrief questions

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Question/response options</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: left;">Which questions did you find more difficult—the questions about your own health or the questions about the health of a 10-year-old child?</td>
</tr>
<tr>
<td style="text-align: left;"> The questions about my own health were more difficult</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">3.3</td>
</tr>
<tr>
<td style="text-align: left;"> The questions about the health of a 10-year-old child were more difficult</td>
<td style="text-align: center;">245</td>
<td style="text-align: center;">81.9</td>
</tr>
<tr>
<td style="text-align: left;"> Both types of questions were equally difficult</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">14.7</td>
</tr>
<tr>
<td style="text-align: left;"> None of the above/don’t know</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">How easy or difficult did you find it to imagine the health of a 10-year-old child?</td>
</tr>
<tr>
<td style="text-align: left;"> Very easy</td>
<td style="text-align: center;">18</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;"> Somewhat easy</td>
<td style="text-align: center;">61</td>
<td style="text-align: center;">20.4</td>
</tr>
<tr>
<td style="text-align: left;"> Neither easy nor difficult</td>
<td style="text-align: center;">57</td>
<td style="text-align: center;">19.1</td>
</tr>
<tr>
<td style="text-align: left;"> Somewhat difficult</td>
<td style="text-align: center;">98</td>
<td style="text-align: center;">32.8</td>
</tr>
<tr>
<td style="text-align: left;"> Very difficult</td>
<td style="text-align: center;">65</td>
<td style="text-align: center;">21.7</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">What sort of child were you thinking of when responding to the questions?</td>
</tr>
<tr>
<td style="text-align: left;"> My own child</td>
<td style="text-align: center;">102</td>
<td style="text-align: center;">34.1</td>
</tr>
<tr>
<td style="text-align: left;"> A child that I know (but not my own child)</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">15.4</td>
</tr>
<tr>
<td style="text-align: left;"> No particular child</td>
<td style="text-align: center;">122</td>
<td style="text-align: center;">40.8</td>
</tr>
<tr>
<td style="text-align: left;"> Myself as a child</td>
<td style="text-align: center;">11</td>
<td style="text-align: center;">3.7</td>
</tr>
<tr>
<td style="text-align: left;"> None of the above/don’t know</td>
<td style="text-align: center;">18</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Would your responses to the questions have been different if you had been asked to imagine a child of a different age—for example, a 5 year old child?</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: center;">244</td>
<td style="text-align: center;">81.6</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: center;">55</td>
<td style="text-align: center;">18.4</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">How do you think a health care system with a limited budget should prioritise resources?</td>
</tr>
<tr>
<td style="text-align: left;"> The health system should prioritise the treatment of adults</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> The health system should prioritise the treatment of children</td>
<td style="text-align: center;">110</td>
<td style="text-align: center;">36.8</td>
</tr>
<tr>
<td style="text-align: left;"> The health system should give equal priority to the treatment of adults and children</td>
<td style="text-align: center;">188</td>
<td style="text-align: center;">62.9</td>
</tr>
<tr>
<td style="text-align: left;"> Don’t know</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0.3</td>
</tr>
</tbody>
</table>

</div>

## Discussion

Our findings in this study were that three of the methods we tested are feasible to use to obtain stated preference-based anchors for a potential EQ-5D-Y value set (LOD’s failure to handle cases where 33333 is considered better then dead arguably makes it the least feasible). This opens the possibility that the relative importance of dimensions could be rapidly and inexpensively obtained for EQ-5D-Y via DCE, then subsequently anchored at dead = 0 via a smaller-scale (but more resource-intensive) study applying one of the methods reported here. Indeed, while our study was focused on the valuation of the EQ-5D-Y instrument, it is worth noting that in principle this approach could also be followed for the valuation of adult health states using other instruments.

A strong finding from this study was the broad level of agreement across the four very different methods used to locate the relative position of dead = 0 for adult versus child perspectives. Previous studies of EQ-5D-Y valuation, as noted in the introduction, had found contradictory results for TTO and VAS tasks, with values for child health states being higher or lower than corresponding adult health states depending on the method used. However, it is worth noting that the VAS study reported by Kind et al. \[3\] did not include 33333 or the rating of dead. Our results are in line with those reported by Kreimeier et al. \[4\] to the extent that values for 33333 were higher in the child perspective. However, our study found this pattern more clearly in all methods employed.

There are many improvements and alterations that could be made to the specific approaches used to implement all four methods. Notwithstanding that, the evidence from this study suggests that none of the four can be immediately ruled out as being infeasible or not working (though the way in which the LOD data were combined with data from a separate study may be problematic as it requires a high level of agreement between the preferences of the two study samples to be valid). This in turn suggests either that multiple methods could continue to be used in future studies (with conclusions somehow triangulated across methods) or that a choice between them must be made. We have considered the criteria that might be used to guide this choice—our thinking about this is provided here for discussion.

Criteria for choosing between anchoring methods could arguably include:

- Feasibility. We consider multiple methods to be feasible, so in this case feasibility does not identify a single preferred option out of the candidate methods. It should be noted that one respondent in the main study and one respondent in the pilot found the subject matter distressing and their interviews were terminated. This issue does not appear to be linked to any particular valuation technique but rather to the general task of considering the severe ill health and death of children (necessary for all of the candidate methods). Hence, it is worth acknowledging that these kinds of studies are not easy to undertake and can pose a considerable emotional burden on respondents.

- Acceptability to decision makers. This includes any prior beliefs decision makers may have about desirable theoretical properties of methods. For example, NICE requires utilities to be based on ‘choice-based methods’ \[25\]. TTO and DCEd are generally accepted as being choice-based; the LOD approach is also based on choice-based tasks, though the novelty and relative lack of research using the technique is likely to make it less attractive to decision makers. VAS has tended to be rejected by health economists (with rare exceptions \[26\]) on the grounds that it is not choice-based.

- Potential for administration on-line. While the current study was undertaken using face-to-face interviews, it may be desirable for future studies to be capable of being completed online. This would probably preclude the lag-time TTO or other TTO variants, because of the complexity of the tasks, but would favour VAS, DCEd and potentially the LOD approach (e.g. as implemented elsewhere \[27\]).

- Theoretical and empirical coherence with the preference data to be anchored. If unanchored preference data are to be collected via DCE and a second task used for anchoring, it may be considered desirable that there be some degree of consistency or coherence between these two sets of preference data. Our study has proceeded on the basis that this is a legitimate basis for comparing different methods for anchoring the data. VAS valuation may present issues in anchoring latent scale DCE data because the preferences are elicited using completely different sorts of tasks with different biases affecting each. This might favour the use of DCEd—although this raises the question of why DCEd would not then be favoured as the sole approach to eliciting preferences (likewise if TTO emerges as the preferred anchoring method, this raises the question of why TTO would not be used as the sole valuation method rather than obtaining latent scale DCE data that need to be anchored using a second method. Our response to this is that all child health valuation techniques involving duration pose issues, so it is preferable to focus the majority of resources on a non-duration-based approach—i.e. DCE—to obtain as accurate as possible an estimation of the relative importance of different dimensions and levels). In addition, the current state of the art in DCEd, particularly in terms of design and modelling, has yet to achieve a final solution, meaning that further research is needed to understand the dependency of certain kinds of designs on modelling results as we have found in this study. It may also be problematic if the preferences of the sample providing the unanchored data differ systematically from the preferences of the sample providing the data for anchoring purposes. One solution to this would be to use the same sample for both data collection exercises or to ensure that the two samples are matched as closely as possible in terms of observable characteristics.

- Theoretical and empirical consistency with adult valuations in use in HTA. This raises a fundamental consideration: should the values for the EQ-5D-Y, and QALYs estimated from them, be commensurate with those for adult EQ-5D instruments? That is, should a QALY estimated for a child be equal to a QALY estimated for an adult? Where resource allocation decisions are made from a single health care budget, the achievement of allocative efficiency would rely on being able to consider QALYs gained and foregone across both adult and child interventions. Alternatively, if budgets for health care for children are ring-fenced, then the only decisions for which EQ-5D-Y values would be used are to assess the incremental QALY gains and cost-effectiveness of alternative ways of treating children. In the latter case, commensurability with adult values would not be a requirement. So, for example, and given results reported in this paper, the value set for the EQ-5D-Y might contain no states worse than dead. The extent to which budgets and, therefore, cost-effectiveness thresholds, might be characterised as being distinct between adults and children, depends on the nature of the health care system. These normative issues would appropriately be informed by discussions with those responsible for HTA, rather than resting on our judgements as researchers. However, even where the child health care budget is ring-fenced, it is important to note that interventions that avoid the premature death of children involve QALY gains both in childhood and in adulthood, so in practice the complete separation of utilities and QALY estimates is difficult if not impossible.

All four methods used in this paper have their own limitations. The lag-time TTO results relate to a child aged 10 years experiencing health states for 10 years, which takes them to adulthood at 20 years of age, and then experiencing a lag-time period of full health. The time being traded off is, therefore, partly years in young adulthood and (for negative values) partly years in childhood. In addition, a feature of both lead and lag-time TTO is that the minimum value is determined by the ratio of duration in health to lead/lag time (in the current study, − 1) \[15\]. Further, the amount of lead or lag-time available to trade will affect the distribution of values for severe health states (the more time available, the more time is traded).

Similarly, the LOD approach to locating the position of dead within the descriptive system was, in this study, based on quite limited information about the nature of respondents’ utility functions. Further, there lacks an agreed means of identifying the position of the dead when respondents consider it to be worse than 33333 and, therefore, to lie outside the EQ-5D descriptive system. More sophisticated approaches to this task are possible and can be rendered suitable for use online (e.g. see \[27\], where a similar approach was embedded within an online adaptive DCE to create an EQ-5D-5L value set for New Zealand).

A further limitation of this study is that anchors for the EQ-5D-Y were obtained by eliciting stated preferences regarding health states pertaining to a child aged 10 years. We judged that specifying the age for the child to be considered in these tasks was important, or else respondents would have introduced their own, varying and unobserved, assumptions about that. Our choice of 10 years of age in this study was influenced by this being the age also used in the UK latent scale DCE study of EQ-5D-Y values \[5\], which produced the data that we wished to re-scale using the anchors derived in the current study. It is also consistent with previous research by Kind et al. \[3\] and Kreimeier et al. \[4\]. Further, 10 years is the mid-point between the ages of 8 and 12 years where the use of EQ-5D-Y is recommended (ages 12–15 being regarded as an area of overlap where EQ-5D-Y is recommended but the adult EQ-5D can also be used) \[10\]. Nevertheless, the specification of age means that the anchoring results reported here may be specific to that age and might be different for younger or older children. There is some suggestion from our respondents that this is the case, with 83% saying their responses to the tasks might have been different for children of different ages. This is an issue which does not arise in the valuation of adult health states, where respondents are asked to consider health states as if experienced by themselves, at their current age is. However, in both adult and child valuation tasks, there is no guarantee that the preferences obtained and the age of the person imagined to be experiencing the state match the age of the patients reporting EQ-5D-Y data to which those utilities are then applied.

A related limitation is that under the adult perspective, respondents were asked to consider their own health, whereas under the child perspective they were asked to consider the health of another individual. Hence, some of the differences may be due to respondents’ preferences about other individuals rather than about children per se. The importance of differences in perspective when eliciting preferences in health has been examined elsewhere \[28–30\].

The fact that the majority of respondents did not provide internally consistent valuations across the VAS, TTO and LOD methods is potentially concerning. Further research should focus on the reasons why respondents respond differently to different valuation techniques. Approaches that encourage respondents to ‘think aloud’ and/or to reflect and deliberate on their choices would likely be useful for this kind of research \[13, 31\].

The decision to include four valuation methods and two perspectives in the study resulted in a rather complex study design (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). To minimise respondent burden, the number of tasks included for each method was restricted. This meant that the average interview duration for this study was similar to that for typical EQ-5D-5L valuation studies \[32\]. However, it may have been beneficial to have included more VAS and TTO health states to assess whether the response patterns observed for 33333 were consistent over the full range.

In conclusion, this study has shown that multiple options exist for providing post-hoc anchors for latent scale DCE preferences. The stated preference methods tested were mostly feasible to use and produced plausible anchors. There was broad agreement between the methods in terms of the placement of the anchor for dead for children versus adults, with the value for 33333 being higher (and more likely to be positive) for children than for adults. The choice between methods, and on what basis that choice should be made, requires further consideration. The choice of anchors raises wider questions about the extent to which the use of values in cost-effectiveness analysis imposes a requirement of commensurability between adult and child health state values.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 124 kb)

</div>

## Acknowledgements

Funding for this research was provided by a EuroQol Research Foundation Grant (Grant no. 2016570). The views expressed do not necessarily reflect the views of the EuroQol Group. We thank the interviewers and respondents who participated in the study, and to Alison Lawrence and Su-Hing Lo for leading the fieldwork and cognitive interviews. We are grateful for comments received on an earlier draft by participants at the 2018 EuroQol Scientific Plenary Meeting. We thank John Brazier, Aki Tsuchiya, Elly Stolk and Oliver Rivero-Arias in particular for their helpful feedback and suggestions. Finally, we thank the anonymous reviewers.

## Footnotes

## References

## References

1. Wille N, Badia X, Bonsel G, et al. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual. Life Res. 2010;19(6):875–886. doi: 10.1007/s11136-010-9648-y.

2. Ravens-Sieberer U, Wille N, Badia X, et al. Feasibility, reliability and validity of the EQ-5D-Y: results from a multinational study. Qual. Life Res. 2010;19(6):887–897. doi: 10.1007/s11136-010-9649-x.

3. Kind P, Klose K, Gusi N, Olivares PR, Greiner W. Can adult weights be used to value child health states? Testing the influence of perspective in valuing EQ-5D-Y. Qual. Life Res. 2015;24(10):2519–2539. doi: 10.1007/s11136-015-0971-1.

4. Kreimeier S, Cole A, Devlin NJ, Herdman M, Mulhern B, Oppe M, Shah KK, Stolk E, Ramos-Goñi JM, Rivero-Arias O, Greiner W. Valuation of EQ-5D-Y and EQ-5D-3L health states—the impact of wording and perspective. Value Health. 2018;21(11):1291–1298. doi: 10.1016/j.jval.2018.05.002.

5. Rivero-Arias, O., Shah, K., Ramos-Goñi, J.M., Mott, D., Devlin, N.: Estimating latent scale discrete choice utilities to develop an EQ-5D-Y value set in the UK. Paper presented at the 34th EuroQol Plenary Meeting, Barcelona, 21–22 September 2017

6. Mott DJ, Shah KK, Ramos-Goñi JM, Devlin NJ, Rivero-Arias O. Valuing EQ-5D-Y Health States Using a Discrete Choice Experiment: Do Adult and Adolescent Preferences Differ? OHE Research Paper. London: Office of Health Economics; 2019. doi:10.1177/0272989X21999607

7. Oppe M, Devlin NJ, van Hout B, Krabbe PFM, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17(4):445–453. doi: 10.1016/j.jval.2014.04.002.

8. Mulhern B, Bansback N, Brazier J, Buckingham K, Cairns J, Devlin N, Dolan P, Hole AR, Kavetsos G, Longworth L, Rowen D. The feasibility of the DCETTO for deriving health-state values for EQ-5D-5L. Preparatory study for the revaluation of the EQ-5D tariff: methodology report. Health Technol. Assess. 2014;18(12):63–82. doi: 10.3310/hta18120.

9. van Reenen, M., Oppe, M., Boye, K.S., Herdman, M., Kennedy-Martin, M., Kennedy-Martin, T., Slaap, B.: EQ-5D-3L user guide. Basic information on how to use the EQ-5D-3L instrument. https://euroqol.org/wp-content/uploads/2019/10/EQ-5D-3L-User-Guide_version-6.0.pdf (2018). Accessed 13 Nov 2019

10. van Reenen, M., Janssen, B., Oppe, M., Kreimeier, S., Greiner, W.: EQ-5D-Y user guide. Basic information on how to use the EQ-5D-Y instrument. https://euroqol.org/wp-content/uploads/2016/09/EQ-5D-Y_User_Guide_v1.0_2014.pdf (2014). Accessed 24 May 2018

11. Szende A, Oppe M, Devlin N. EQ-5D Value Sets: Inventory, Comparative Review and User Guide. Dordrecht: Springer; 2007.

12. Brazier J, Ratcliffe J, Salomon JA, Tsuchiya A. Measuring and Valuing Health Benefits for Economic Evaluation. Oxford: Oxford University Press; 2017.

13. Devlin NJ, Shah KK, Mulhern BJ, Pantiri K, van Hout B. A new method for valuing health: directly eliciting personal utility functions. Eur. J. Health Econ. 2019;20(2):257–270. doi: 10.1007/s10198-018-0993-z.

14. Rowen D, Brazier J, van Hout B. A comparison of methods for converting DCE values onto the full health-dead QALY scale. Med. Decis. Mak. 2015;35(3):328–340. doi: 10.1177/0272989X14559542.

15. Devlin N, Buckingham K, Shah K, Tsuchiya A, Tilling C, Wilkinson G, van Hout B. A comparison of alternative variants of the lead and lag time TTO. Health Econ. 2013;22(5):517–532. doi: 10.1002/hec.2819.

16. Augustovski F, Rey-Ares L, Irazola V, Oppe M, Devlin NJ. Lead versus lag-time trade-off variants: does it make any difference? Eur. J. Health Econ. 2013;14(1):25–31. doi: 10.1007/s10198-013-0505-0.

17. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi: 10.1007/s40273-016-0404-1.

18. Bansback N, Brazier J, Tsuchiya A, Anis A. Using a discrete choice experiment to estimate societal health state utility values. J. Health Econ. 2012;31:306–318. doi: 10.1016/j.jhealeco.2011.11.004.

19. Lenert LA, Cher DJ, Goldstein MK, Bergen MR, Garber A. The effect of search procedures on utility elicitations. Med. Decis. Mak. 1998;18(1):76–83. doi: 10.1177/0272989X9801800115.

20. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–473. doi: 10.1016/j.jval.2016.10.012.

21. Lancsar E, Louviere J. Conducting discrete choice experiments to inform healthcare decision making. PharmacoEconomics. 2008;26(8):661–677. doi: 10.2165/00019053-200826080-00004.

22. Hensher DA, Rose JM, Greene WH. Applied Choice Analysis: A Primer. Cambridge: Cambridge University Press; 2005.

23. Jakubczyk M, Craig BM, Barra M, Groothuis-Oudshoorn CGM, Hartman JD, Huynh E, Ramos-Goñi JM, Stolk EA, Rand K. Choice defines value: a predictive modeling competition in health preference research. Value Health. 2018;21(2):229–238. doi: 10.1016/j.jval.2017.09.016.

24. Office for National Statistics.: Population estimates for UK, England and Wales, Scotland and Northern Ireland. https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland (2017). Accessed 4 Oct 2017

25. NICE [National Institute for Health and Care Excellence] Guide to the Methods of Technology Appraisal 2013. London: National Institute of Health and Care Excellence; 2013.

26. Parkin D, Devlin N. Is there a case for using visual analogue scale valuations in cost-utility analysis? Health Econ. 2006;15(7):653–664. doi: 10.1002/hec.1086.

27. Sullivan, T., Ward, J., Hansen, P., Devlin, N., Ombler, F., Derrett, S.: A new tool for creating personal and social EQ-5D-5L value sets, including valuing ‘dead’. Economics Discussion Paper 1903, Economics Department, University of Otago. https://www.otago.ac.nz/economics/otago705521.pdf (2019). Accessed 11 Nov 2019

28. Dolan P, Olsen JA, Menzel P, Richardson J. An inquiry into the different perspectives that can be used when eliciting preferences in health. Health Econ. 2003;12(7):545–551. doi: 10.1002/hec.760.

29. Tsuchiya A, Watson V. Re-thinking ‘the different perspectives that can be used when eliciting preferences in health’. Health Econ. 2017;26(12):e103–e107. doi: 10.1002/hec.3480.

30. Cubi-Molla P, Shah K, Burström K. Experience-based values: a framework for classifying different types of experience in health valuation research. Patient. 2018;11(3):253–270. doi: 10.1007/s40271-017-0292-2.

31. Karimi M, Brazier J, Paisley S. Effect of reflection and deliberation on health state values: a mixed-methods study. Value Health. 2019;22(11):1311–1317. doi: 10.1016/j.jval.2019.07.013.

32. Ludwig K, von der Schulenburg JMG, Greiner W. German value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(6):663–674. doi: 10.1007/s40273-018-0615-8.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 124 kb)

</div>

[^1]: Sometimes also denoted as EQ-5D-Y-3L, to distinguish it from the newly developed five-level version.

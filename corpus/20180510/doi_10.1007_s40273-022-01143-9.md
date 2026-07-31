---
project_id: "20180510"
work_id: "doi:10.1007/s40273-022-01143-9"
doi: "10.1007/s40273-022-01143-9"
pmid: "35604633"
pmcid: "PMC9124748"
title: "EQ-5D-Y Value Set for Germany"
journal: "Pharmacoeconomics"
publication_date: "2022-05-23"
volume: "40"
issue: "Suppl 2"
authors:
  - name: "Simone Kreimeier"
    affiliation_ids:
      - "Aff1"
  - name: "David Mott"
    affiliation_ids:
      - "Aff2"
  - name: "Kristina Ludwig"
    affiliation_ids:
      - "Aff1"
  - name: "Wolfgang Greiner"
    affiliation_ids:
      - "Aff1"
  - name: "IMPACT HTA HRQoL Group"
affiliations:
  - id: "Aff1"
    name: "Department of Health Economics and Health Care Management, School of Public Health, Bielefeld University, Bielefeld, Germany"
  - id: "Aff2"
    name: "Office of Health Economics, London, UK"
  - id: "Aff3"
    name: "Institute for Economic Research, 1000 Ljubljana, Slovenia"
  - id: "Aff4"
    name: "Maths In Health, Rotterdam, The Netherlands"
licence: "cc-by-nc"
source_file: "input/projects/20180510/papers/doi_10.1007_s40273-022-01143-9.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9124748/fullTextXML"
source_method: "epmc_xml"
source_sha256: "647b656987ebfcf2c0919489e2f06536648d7926cd1c2511b3acbf9b00a55f34"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# EQ-5D-Y Value Set for Germany

## Abstract

### Background

Demand is increasing for youth-specific preference-based health-related quality-of-life measures for inclusion in evaluations of healthcare interventions for children and adolescents. The EQ-5D-Youth (EQ-5D-Y) has the potential to become such a preference-based measure.

### Objective

This study applied the recently published EQ-5D-Y valuation protocol to develop a German EQ-5D-Y value set and explored the differences between values given to youth health by parents and non-parents.

### Methods

To elicit EQ-5D-Y health state preferences, a representative sample of 1030 adults of the general population completed a discrete choice experiment (DCE) online survey, and 215 adults participated in face-to-face interviews applying composite time trade-off (cTTO). Respondents were asked to consider a 10-year-old child living in the health states. DCE data were modelled using a mixed logit model. To derive the value set, DCE latent scale values were anchored onto adjusted mean cTTO values using a linear mapping approach.

### Results

Adult respondents considered pain/discomfort and feeling worried/sad/unhappy as the two most important dimensions in terms of youth health. Adjusted mean cTTO values ranged from − 0.350 for health state 33333 to 0.970 for health state 21111. The EQ-5D-Y value set showed a logical order for all parameter estimates, and predicted values ranged from − 0.283 to 1. Differences in preferences by parental status were mainly observed for cTTO results, where mean values were larger for parents than for non-parents.

### Conclusions

Applying the valuation protocol, a German EQ-5D-Y value set with internally consistent coefficients was developed. This enables the instrument to be used in economic evaluations of paediatric healthcare interventions.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40273-022-01143-9.

Accepted 2022 Mar 21; Issue date 2022.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| When considering youth health, respondents from the German adult general public considered the health dimensions pain/discomfort and feeling worried/sad/unhappy as most important. |
| Following the international EQ-5D-Youth (EQ-5D-Y) valuation protocol, an EQ-5D-Y value set for Germany was developed, which now enables cost-utility analysis of paediatric healthcare interventions. |

</div>

## Introduction

Economic evaluations compare the costs and benefits of healthcare approaches, applications, and technologies (hereafter, ‘healthcare interventions’). To measure benefit, quality-adjusted life-years (QALYs) are often used as a standard utility measure in cost-utility analyses (CUAs) \[1\]. In several countries, CUAs including QALYs are used to inform decision making in healthcare \[1, 2\]. QALYs combine health-related quality of life (HRQoL), obtained by direct or indirect valuation approaches, with length of life \[3, 4\]. CUAs of healthcare interventions for children and adolescents are less standardised than those for interventions for adults \[5, 6\]. This is because there is less consensus around how HRQoL should be measured and valued for children and adolescents.

A review in 2019 summarised all primary studies reporting health utilities for childhood conditions and identified various approaches that had been used in practice \[3\]. In general, indirect valuation approaches are seen as advantageous as they use standardised generic preference-based HRQoL instruments with corresponding value sets to obtain a single utility for each health state to be used in QALY calculations \[1, 4\]. Several such instruments have been designed for younger populations. However, some were designed only for specific age groups (e.g. 16D for adolescents aged 12–15 years, 17D for children aged 8–11 years, and Assessment of Health Utility Measurement for adolescents aged 12–18 years) or have unclear age ranges and are relatively long (e.g. Assessment of Quality of Life 6 Dimension (AQoL-6D), which has 20 items, and the Quality of Well-Being scale (QWB), which asks about three dimensions and 58 symptoms) \[4, 6\]. Hence, the number of generic preference-based HRQoL instruments applicable to a broad age range in children and adolescents is limited, and there is no widely used child-specific instrument \[4, 6, 7\].

The generation of value sets for youth-specific[^1] HRQoL instruments is a more recent development that follows a debate on methodological and conceptual issues of valuation studies for paediatric instruments. The discussion is first and foremost about whose values should be considered: those of the adult general public, of parents, or of children and adolescents themselves \[6, 7\]. Studies show differences in the values given to child health by the adult general public and parents \[8, 9\] and between those given by adults and adolescents \[10, 11\]. The most suitable elicitation methods and perspectives in valuation tasks have also been discussed \[4, 6, 7\].

The EQ-5D-Youth (EQ-5D-Y) is a short generic instrument developed by the EuroQol Group to measure HRQoL in children and adolescents aged 8–15 years as an equivalent to the adult instrument EQ-5D-3L (three-level version of EQ-5D). It consists of five dimensions: mobility (MO), looking after myself (SC), doing usual activities (UA), having pain/discomfort (PD), and feeling worried/sad/unhappy (AD), with each dimension specifying three levels of severity: no problems/not (level 1), some problems/a bit (level 2), and a lot of problems/very (level 3)[^2] \[12–14\]. The adult instruments are widely used to assess HRQoL and calculate QALYs in economic evaluations, and—with its similar structure—the EQ-5D-Y also has the potential to be used \[2, 7, 15\]. However, very few EQ-5D-Y value sets currently exist \[12, 16, 17\]. As previous studies have shown that health state values for adults and children differ, value sets for adult instruments should not be used to calculate EQ-5D-Y-based utilities. Instead, separate value sets are necessary \[18, 19\]. Based on results of explorative studies testing different approaches of valuing EQ-5D-Y health states, a first international valuation protocol for EQ-5D-Y was recently published \[20\].

In Germany, no youth-specific HRQoL instrument is available that allows for utility calculation. Therefore, the main objective of this study was to develop a German value set for EQ-5D-Y—as one of the first national value sets—according to the methods proposed by the protocol to enable the use of the EQ-5D-Y as a utility measure. In addition, we explored differences in values given to child health states by parents and non-parents.

## Methods

### Data Collection

Data collection took place between November 2019 and July 2020. As suggested by the EQ-5D-Y valuation protocol, it was split in two sub-surveys to collect (1) discrete choice experiment (DCE) data via an online survey and (2) composite time trade-off (cTTO) data via interviews. Ethical approvals for both sub-surveys were received in Germany (Ethics Committee of Bielefeld University, No. EUB 2018-172 and EUB 2019-204).

### Methods for Eliciting Health State Preferences

DCEs are used to assess the relative importance of dimensions and levels, and cTTO is used to rescale/anchor the latent scale DCE values on a scale from full health (1) to dead (0) \[20\]. The DCE task uses pairwise comparisons. The respondent is asked to decide which out of two health states, A and B, is better (forced choice) \[21, 22\]. As we used neither a ‘duration’ attribute nor a comparison to the alternative ‘dead’ in our DCE, only latent scale values were produced. The cTTO identifies the number of life-years in full health at which the respondent is indifferent between a longer period of life-years with impaired health and a shorter life duration in full health. The respondent is asked to trade-off life-years. In cTTO, the conventional TTO is used to start the tasks for all health states. For health states that the respondent considers to be worse than being dead, lead-time TTO is used \[23–25\].

### Health State Selection

The DCE design from the EQ-5D-Y valuation protocol is D-efficient and consists of 150 DCE pairs separated into ten blocks. A two-dimension overlap was used for all pairs, meaning that the health states in each pair differed in the levels of three dimensions, whereas the other two dimensions presented the same level \[20\]. Differences between health states were presented in bold font to reduce non-attendance. Further, level balance among blocks was ensured. In each block, the order of health state pairs was randomized, as  well as the left/right presentation during the task. Each respondent completed 18 DCE tasks: 15 from the experimental design and three for quality control (QC) purposes (see Sect. <a href="#Sec11" data-ref-type="sec">2.7</a>).

The cTTO design included one block of ten health states, which were valued by each respondent. The design included three mild health states (11112, 11121, 21111), two moderate ones (22223, 22232), and five severe health states (31133, 32223, 33233, 33323, 33333) \[20\]. The order of health states was randomised for each participant.

### Framing of Discrete Choice Experiment and Composite Time Trade-Off Tasks

In both valuation tasks, participants were asked to imagine a hypothetical 10-year-old child when valuing the health states. Therefore, the wording of the EQ-5D-Y proxy version 1 was used for the health states, which means only the part of the item describing the dimension and severity level, e.g. ‘no problems walking about’ was used (rather than ‘I have no problems walking about’) \[12\].

### Interview Process

The online DCE survey consisted of the following elements:

1.  Information sheet on the project aim and procedures

2.  Consent

3.  Demographic questions on age, gender, and region to inform the quota sampling

4.  Self-reported EQ-5D-Y to familiarise respondents with the instrument

5.  Three questions on experience with severe illness

6.  18 DCE tasks (15 DCE tasks and three DCE tasks for QC)

7.  Self-reported EQ-5D-5L

8.  Socio-demographic and health-related questions

The cTTO data were collected via computer-assisted personal interviews using the EuroQol portable valuation technology (EQ-PVT). An interviewer guideline was prepared explaining the interviewer’s role, how to handle the software, and instructions to be given to the respondents. Each of the four interviewers attended a day-long training session and had to conduct three test interviews. The interviews consisted of the following[^3]:

1.  Welcome and study aim (information sheet obtained prior to the interview)

2.  Written consent

3.  Self-reported EQ-5D-Y to familiarise respondents with the instrument

4.  cTTO wheelchair examples plus three cTTO practice states

5.  Ten cTTO tasks

6.  Feedback module

7.  Debriefing questions

8.  Socio-demographic questions and three questions on experience with severe illness

9.  Self-reported EQ-5D-5L

Most of the cTTO interviews were conducted face to face; however, with the advent of the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2; coronavirus disease 2019 \[COVID-19\]) pandemic, 32 interviews were conducted online using a video conference application to finish data collection.

### Sample and Recruitment

For the DCE survey, we aimed for a sample of 1000 respondents from the adult general population in Germany recruited by an online panel of a market research agency. To facilitate a representative sample in terms of gender, age groups, educational level, and region (16 federal states in Germany), quota-based sampling was applied based on German official statistics \[26\].

For the cTTO interviews, we aimed for 200 respondents from the adult general population \[20\]. A convenience sample controlled in terms of gender and age groups was recruited. Respondents came from Bielefeld and surrounding areas and were mostly recruited by study team members as well as through advertisements in local newspapers. The interviews were conducted mainly at Bielefeld University. A small number of participants came from other German regions as some interviews were conducted online. All interview respondents received a €20 voucher.

### Quality Control

To identify non-engaged respondents in the DCE online survey, two QC criteria were applied. First, we included three fixed dominant pairs in which one health state logically dominated the other. This enabled us to check choices for rationality and to identify respondents who seemed to have a low level of attentiveness to, engagement with, or understanding of the tasks or made irrational choices. The dominant pairs were presented at the beginning and end of the DCE tasks and at a random position in the middle. Respondents were excluded if they gave a wrong answer to at least two of the three dominant pairs. The dominant pairs were excluded from the modelling analysis. Second, the QC procedure included a time criterion. Respondents were also excluded if they spent less than 150 seconds on all DCE tasks. We assumed that ‘speeders’, who finished the online survey too quickly, did not consider the health states in detail.

For the cTTO interviews, we applied the QC process established by the EuroQol Group for EQ-5D-5L valuation studies \[27\]. Poor interview quality is indicated by

- a short amount of time spent in the wheelchair example to explain cTTO tasks,

- missing explanation for the ‘worse than dead’ task (lead-time TTO),

- less than 5 minutes spent on all cTTO tasks, or

- obvious inconsistency in the cTTO ratings when the value of 33333 is not the lowest or at least 0.5 higher than the state with the lowest value.

If interviews had continuously poor quality, data were excluded from the analysis. Further, the interview included a feedback module by which each respondent was presented with the rank ordering implied by their cTTO valuations. Respondents were asked to review their responses and to flag any health state they felt should be reconsidered. These states could not be re-valued but were excluded from modelling \[28, 29\].

### Data Analysis

Descriptive analyses were used to examine the sample characteristics and the responses to the cTTO. Sample characteristics with regard to experience with illness and self-reported HRQoL were compared with the characteristics of the representative adult sample of the German EQ-5D-5L valuation study \[30\]. The DCE data were analysed using choice models under a random utility framework with a linear, additive utility function, as in Eq. (<a href="#Equ1" data-ref-type="disp-formula">1</a>):

``` math
\begin{array}{l}
{V_{j} = \beta_{1}MO2 + \beta_{2}MO3 + \beta_{3}SC2 + \beta_{4}SC3 + \beta_{5}UA2 + \beta_{6}UA3 + \beta_{7}PD2 + \beta_{8}PD3 + \beta_{9}AD2 + \beta_{10}AD3.}
\end{array}
```

The ten independent variables are made up of two variables for each EQ-5D-Y dimension, representing the two levels beyond level 1 (‘no problems’; the reference category). The coefficients therefore indicate the decrement from level 1 to the respective level.

A mixed logit model specification was chosen, given the a priori expectation that there would be unobservable random preference heterogeneity in the data and that multinomial logit models cannot account for such heterogeneity \[31\]. In this model, each of the ten parameters were modelled as random and normally distributed using 5000 Halton draws. Coefficients from the model were transformed into relative attribute importance (RAI) scores to aid interpretation; these were obtained by dividing the utility range for each attribute by the total utility range.

To produce the value set, the coefficients from the mixed logit model need to be anchored onto the scale of full health to dead. There are several different anchoring approaches, including rescaling based on the mean value of the worst health state (33333 rescaling), mapping the DCE data onto the cTTO data (mapping), and hybrid modelling \[19, 32\]. Earlier studies noted that the ratio of the cTTO and DCE data is not well balanced in the EQ-5D-Y valuation protocol, so the performance of the hybrid model may be suboptimal \[17\]. Of the remaining two approaches, mapping takes into account the mean values of all ten health states valued in the cTTO task, relative to one with 33333 rescaling. Therefore, we chose mapping as the preferred anchoring method. Specifically, we mapped the DCE data onto mean cTTO values, which were adjusted for censoring at − 1 (obtained by estimating Tobit models for each state). This adjustment was deemed appropriate given that the cTTO task does not allow for utilities below − 1.

A range of specifications for the mapping model were examined, including linear models with and without constants, as well as the inclusion of a quadratic term. Based on a combination of parameter significance, adjusted R-squared values, and the alignment between cTTO values and the resulting value sets, the preferred specification was a linear function without a constant, as in Eq. (<a href="#Equ2" data-ref-type="disp-formula">2</a>):

``` math
\text{cTTO}_{i} = {}\beta\left( \text{DCE}_{i} \right) + \varepsilon_{i},
```

where cTTO<sub>*i*</sub> is the adjusted mean cTTO utility and DCE<sub>*i*</sub> is the latent scale DCE utility for *i*th health state (1 ≤ *i* ≤ 10). The estimated *β* was used to rescale the latent scale DCE values from the mixed logit model.

To compare results by parental status, we split the two samples based on responses to the question “Do you or have you ever had primary responsibility for a child (as a birth parent, foster parent, adoptive parent, or similar)?” Respondents who answered “yes” were classified as having parental experience, referred to as ‘parents’, and those answering “no” were referred to as ‘non-parents’. For the DCE responses, we compared conditional logit model results by parental status. For cTTO, we compared the adjusted mean values of the ten cTTO health states for both groups. Value sets by parental status were also estimated and compared.

All statistical analyses were performed using Stata 15.

## Results

### Sample Characteristics

In total, 1030 respondents completed the DCE survey with appropriate data quality (309 failed QC: 277 because of timing and 32 because of dominant pairs). The DCE sample is representative for the German general population aged ≥18 years with respect to gender, age groups, educational level, and region. Table <a href="#Tab1" data-ref-type="table">1</a> shows marginal proportional differences. A comparison of characteristics of included and excluded DCE respondents is presented in Table S1.1 in the electronic supplementary material (ESM). A total of 215 respondents completed the cTTO interviews. The cTTO sample underrepresents male respondents, respondents aged ≥ 70 years, and lower and middle educated respondents, whereas respondents aged 18–29 years are slightly overrepresented (see Table <a href="#Tab1" data-ref-type="table">1</a>). In particular, higher educated people are overrepresented.

<div id="Tab1" class="table-wrap">

<div class="caption">

Sample characteristics

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristics</th>
<th style="text-align: left;">cTTO survey</th>
<th style="text-align: left;">DCE survey</th>
<th rowspan="2" style="text-align: left;">German adult general population [<span class="citation" data-cites="CR26">26</span>]</th>
<th rowspan="2" style="text-align: left;">Proportional difference between cTTO sample and general population</th>
<th rowspan="2" style="text-align: left;">Proportional difference between DCE sample and general population</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><em>N</em> = 215</th>
<th style="text-align: left;"><em>N</em> = 1030</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">Gender</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">139 (64.6)</td>
<td style="text-align: left;">546 (53.0)</td>
<td style="text-align: center;">51.1</td>
<td style="text-align: left;">+ 13.5</td>
<td style="text-align: left;">+ 1.9</td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">76 (35.4)</td>
<td style="text-align: left;">482 (46.8)</td>
<td style="text-align: center;">48.9</td>
<td style="text-align: left;">− 13.5</td>
<td style="text-align: left;">− 2.1</td>
</tr>
<tr>
<td style="text-align: left;"> Diverse</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">2 (0.2)</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Age groups, years</td>
</tr>
<tr>
<td style="text-align: left;"> 18–24</td>
<td style="text-align: left;">27 (12.6)</td>
<td style="text-align: left;">95 (9.2)</td>
<td style="text-align: center;">9.1</td>
<td style="text-align: left;">+ 3.5</td>
<td style="text-align: left;">+ 0.1</td>
</tr>
<tr>
<td style="text-align: left;"> 25–29</td>
<td style="text-align: left;">31 (14.4)</td>
<td style="text-align: left;">69 (6.7)</td>
<td style="text-align: center;">7.5</td>
<td style="text-align: left;">+ 6.9</td>
<td style="text-align: left;">− 0.8</td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td style="text-align: left;">28 (13.0)</td>
<td style="text-align: left;">153 (14.9)</td>
<td style="text-align: center;">15.3</td>
<td style="text-align: left;">− 2.3</td>
<td style="text-align: left;">− 0.4</td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td style="text-align: left;">41 (19.1)</td>
<td style="text-align: left;">152 (14.8)</td>
<td style="text-align: center;">15.0</td>
<td style="text-align: left;">+ 4.1</td>
<td style="text-align: left;">− 0.2</td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td style="text-align: left;">46 (21.4)</td>
<td style="text-align: left;">203 (19.7)</td>
<td style="text-align: center;">19.4</td>
<td style="text-align: left;">+ 2.0</td>
<td style="text-align: left;">+ 0.3</td>
</tr>
<tr>
<td style="text-align: left;"> 60–69</td>
<td style="text-align: left;">26 (12.1)</td>
<td style="text-align: left;">149 (14.5)</td>
<td style="text-align: center;">14.9</td>
<td style="text-align: left;">− 2.8</td>
<td style="text-align: left;">− 0.4</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 70</td>
<td style="text-align: left;">16 (7.4)</td>
<td style="text-align: left;">209 (20.3)</td>
<td style="text-align: center;">18.8</td>
<td style="text-align: left;">− 11.4</td>
<td style="text-align: left;">+ 1.5</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Educational level</td>
</tr>
<tr>
<td style="text-align: left;"> Still in education</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">17 (1.7)</td>
<td style="text-align: center;">3.6</td>
<td style="text-align: left;">− 3.6</td>
<td style="text-align: left;">− 1.9</td>
</tr>
<tr>
<td style="text-align: left;"> Lower education<sup>a</sup></td>
<td style="text-align: left;">11 (5.1)</td>
<td style="text-align: left;">305 (29.6)</td>
<td style="text-align: center;">34.7</td>
<td style="text-align: left;">− 29.6</td>
<td style="text-align: left;">− 5.1</td>
</tr>
<tr>
<td style="text-align: left;"> Middle education<sup>b</sup></td>
<td style="text-align: left;">37 (17.2)</td>
<td style="text-align: left;">336 (32.6)</td>
<td style="text-align: center;">29.8</td>
<td style="text-align: left;">− 12.6</td>
<td style="text-align: left;">+ 2.8</td>
</tr>
<tr>
<td style="text-align: left;"> Higher education<sup>c</sup></td>
<td style="text-align: left;">166 (77.2)</td>
<td style="text-align: left;">365 (35.4)</td>
<td style="text-align: center;">31.9</td>
<td style="text-align: left;">+ 45.3</td>
<td style="text-align: left;">+ 3.5</td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td style="text-align: left;">1 (0.5)</td>
<td style="text-align: left;">7 (0.7)</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Region (federal state)</td>
</tr>
<tr>
<td style="text-align: left;"> Baden-Württemberg</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">135 (13.1)</td>
<td style="text-align: center;">13.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">− 0.2</td>
</tr>
<tr>
<td style="text-align: left;"> Bayern</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">165 (16.0)</td>
<td style="text-align: center;">15.7</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">+ 0.3</td>
</tr>
<tr>
<td style="text-align: left;"> Berlin</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">45 (4.4)</td>
<td style="text-align: center;">4.4</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Brandenburg</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">32 (3.1)</td>
<td style="text-align: center;">3.1</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Bremen</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">9 (0.9)</td>
<td style="text-align: center;">0.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">+ 0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Hamburg</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">23 (2.2)</td>
<td style="text-align: center;">2.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Hessen</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">72 (7.0)</td>
<td style="text-align: center;">7.5</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">− 0.5</td>
</tr>
<tr>
<td style="text-align: left;"> Mecklenburg-Vorpommern</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">22 (2.1)</td>
<td style="text-align: center;">2.0</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">+ 0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Niedersachsen</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">100 (9.7)</td>
<td style="text-align: center;">9.6</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">+ 0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Nordrhein-Westfalen</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">226 (21.9)</td>
<td style="text-align: center;">21.5</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">+ 0.4</td>
</tr>
<tr>
<td style="text-align: left;"> Rheinland-Pfalz</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">50 (4.9)</td>
<td style="text-align: center;">4.9</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Saarland</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">11 (1.1)</td>
<td style="text-align: center;">1.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">− 0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Sachsen</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">51 (5.0)</td>
<td style="text-align: center;">5.0</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Sachsen-Anhalt</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">28 (2.7)</td>
<td style="text-align: center;">2.7</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Schleswig-Holstein</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">36 (3.5)</td>
<td style="text-align: center;">3.5</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Thüringen</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">25 (2.4)</td>
<td style="text-align: center;">2.6</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">− 0.2</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Responsibility for children<sup>d</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td style="text-align: left;">120 (55.8)</td>
<td style="text-align: left;">564 (54.9)</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">95 (44.2)</td>
<td style="text-align: left;">463 (45.1)</td>
<td style="text-align: center;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
</tbody>
</table>

Data are presented as *n* (%) or % unless otherwise indicated

*cTTO* composite time trade-off, *DCE* discrete choice experiment

<sup>a</sup>Lower education: with or without secondary general school certificate

<sup>b</sup>Middle education: intermediate school certificate

<sup>c</sup>Higher education: entrance qualification for universities of applied sciences; university entrance qualification

<sup>d</sup>Original wording of the question in the DCE as well as in the cTTO survey: “Do you or have you ever had primary responsibility for a child (as a birth parent, foster parent, adoptive parent, or similar)?”

</div>

As Table <a href="#Tab2" data-ref-type="table">2</a> illustrates, the cTTO and DCE samples differ in terms of respondents’ experiences with severe illness and respondents’ HRQoL. While the DCE sample contained a higher proportion of respondents who had experienced severe illness themselves than did the cTTO sample (37.7 vs. 22.3%, respectively), the proportion of respondents that had experience with severe illness in terms of other people that they had cared for was higher in the cTTO sample than in the DCE sample (30.7 vs. 14.7%, respectively). The reported problems on EQ-5D-5L and in the mean visual analogue scale (VAS) value show that the cTTO sample reported fewer health problems than the DCE sample. However, the DCE sample corresponds better with the self-reported health of the German adult general population \[30\].

<div id="Tab2" class="table-wrap">

<div class="caption">

Respondents’ experiences with severe illness and health-related quality of life

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Respondents’ experience with illness and their EQ-5D-5L reported HRQoL</th>
<th style="text-align: left;">cTTO survey</th>
<th style="text-align: left;">DCE survey</th>
<th style="text-align: left;">German adult general population [<span class="citation" data-cites="CR30">30</span>]</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Experiences with severe illness</td>
</tr>
<tr>
<td style="text-align: left;"> In yourself (yes)</td>
<td style="text-align: left;">48 (22.3)</td>
<td style="text-align: left;">388 (37.7)</td>
<td style="text-align: left;">34.4</td>
</tr>
<tr>
<td style="text-align: left;"> In your family (yes)</td>
<td style="text-align: left;">150 (69.8)</td>
<td style="text-align: left;">687 (66.7)</td>
<td style="text-align: left;">68.8</td>
</tr>
<tr>
<td style="text-align: left;"> In caring for another person (yes)</td>
<td style="text-align: left;">66 (30.7)</td>
<td style="text-align: left;">151 (14.7)</td>
<td style="text-align: left;">82.6</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>EQ-5D-5L—descriptive system</em></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Mobility (MO)</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">194 (90.2)</td>
<td style="text-align: left;">664 (64.5)</td>
<td style="text-align: left;">69.3</td>
</tr>
<tr>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">14 (6.5)</td>
<td style="text-align: left;">219 (21.3)</td>
<td style="text-align: left;">15.4</td>
</tr>
<tr>
<td style="text-align: left;"> Moderate problems</td>
<td style="text-align: left;">6 (2.8)</td>
<td style="text-align: left;">107 (10.4)</td>
<td style="text-align: left;">9.9</td>
</tr>
<tr>
<td style="text-align: left;"> Severe problems</td>
<td style="text-align: left;">1 (0.5)</td>
<td style="text-align: left;">35 (3.4)</td>
<td style="text-align: left;">5.3</td>
</tr>
<tr>
<td style="text-align: left;"> Unable</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">4 (0.4)</td>
<td style="text-align: left;">0.2</td>
</tr>
<tr>
<td style="text-align: left;"> Missing</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">1 (0.1)</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Self-care (SC)</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">207 (97.2)</td>
<td style="text-align: left;">934 (90.9)</td>
<td style="text-align: left;">93.61</td>
</tr>
<tr>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">3 (1.4)</td>
<td style="text-align: left;">63 (6.1)</td>
<td style="text-align: left;">3.54</td>
</tr>
<tr>
<td style="text-align: left;"> Moderate problems</td>
<td style="text-align: left;">3 (1.4)</td>
<td style="text-align: left;">24 (2.3)</td>
<td style="text-align: left;">1.9</td>
</tr>
<tr>
<td style="text-align: left;"> Severe problems</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">6 (0.6)</td>
<td style="text-align: left;">0.7</td>
</tr>
<tr>
<td style="text-align: left;"> Unable</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">1 (0.1)</td>
<td style="text-align: left;">0.3</td>
</tr>
<tr>
<td style="text-align: left;"> Missing</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">2 (0.2)</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Usual activities (UA)</td>
</tr>
<tr>
<td style="text-align: left;"> No problems</td>
<td style="text-align: left;">195 (90.7)</td>
<td style="text-align: left;">688 (66.9)</td>
<td style="text-align: left;">77.3</td>
</tr>
<tr>
<td style="text-align: left;"> Slight problems</td>
<td style="text-align: left;">14 (6.5)</td>
<td style="text-align: left;">226 (22.0)</td>
<td style="text-align: left;">12.7</td>
</tr>
<tr>
<td style="text-align: left;"> Moderate problems</td>
<td style="text-align: left;">5 (2.3)</td>
<td style="text-align: left;">75 (7.3)</td>
<td style="text-align: left;">7.3</td>
</tr>
<tr>
<td style="text-align: left;"> Severe problems</td>
<td style="text-align: left;">1 (0.5)</td>
<td style="text-align: left;">32 (3.1)</td>
<td style="text-align: left;">2.3</td>
</tr>
<tr>
<td style="text-align: left;"> Unable</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">7 (0.7)</td>
<td style="text-align: left;">0.5</td>
</tr>
<tr>
<td style="text-align: left;"> Missing</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">2 (0.2)</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Pain/discomfort (PD)</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td style="text-align: left;">120 (55.8)</td>
<td style="text-align: left;">347 (33.8)</td>
<td style="text-align: left;">44.4</td>
</tr>
<tr>
<td style="text-align: left;"> Slight</td>
<td style="text-align: left;">73 (34.0)</td>
<td style="text-align: left;">449 (43.7)</td>
<td style="text-align: left;">35.1</td>
</tr>
<tr>
<td style="text-align: left;"> Moderate</td>
<td style="text-align: left;">17 (7.9)</td>
<td style="text-align: left;">188 (18.3)</td>
<td style="text-align: left;">15.8</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;">5 (2.3)</td>
<td style="text-align: left;">42 (4.1)</td>
<td style="text-align: left;">4.4</td>
</tr>
<tr>
<td style="text-align: left;"> Extreme</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">2 (0.2)</td>
<td style="text-align: left;">0.4</td>
</tr>
<tr>
<td style="text-align: left;"> Missing</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">2 (0.2)</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Anxiety/depression (AD)</td>
</tr>
<tr>
<td style="text-align: left;"> Not</td>
<td style="text-align: left;">168 (78.1)</td>
<td style="text-align: left;">589 (57.4)</td>
<td style="text-align: left;">74.4</td>
</tr>
<tr>
<td style="text-align: left;"> Slightly</td>
<td style="text-align: left;">36 (16.7)</td>
<td style="text-align: left;">274 (26.7)</td>
<td style="text-align: left;">17.2</td>
</tr>
<tr>
<td style="text-align: left;"> Moderately</td>
<td style="text-align: left;">9 (4.2)</td>
<td style="text-align: left;">103 (10.0)</td>
<td style="text-align: left;">6.9</td>
</tr>
<tr>
<td style="text-align: left;"> Severely</td>
<td style="text-align: left;">1 (0.5)</td>
<td style="text-align: left;">45 (4.4)</td>
<td style="text-align: left;">1.3</td>
</tr>
<tr>
<td style="text-align: left;"> Extremely</td>
<td style="text-align: left;">1 (0.5)</td>
<td style="text-align: left;">16 (1.6)</td>
<td style="text-align: left;">0.3</td>
</tr>
<tr>
<td style="text-align: left;"> Missing</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">3 (0.3)</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">EQ-5D-5L—Index values</td>
</tr>
<tr>
<td style="text-align: left;"> Mean</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;">0.9</td>
</tr>
<tr>
<td style="text-align: left;"> Standard deviation</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">0.02</td>
</tr>
<tr>
<td style="text-align: left;"> Minimum</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">− 0.3</td>
<td style="text-align: left;">− 0.5</td>
</tr>
<tr>
<td style="text-align: left;"> Maximum</td>
<td style="text-align: left;">1.0</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">EQ-5D-5L—visual analogue scale (VAS)</td>
</tr>
<tr>
<td style="text-align: left;"> Mean</td>
<td style="text-align: left;">86.9</td>
<td style="text-align: left;">73.7</td>
<td style="text-align: left;">79.5</td>
</tr>
<tr>
<td style="text-align: left;"> Standard deviation</td>
<td style="text-align: left;">12.13</td>
<td style="text-align: left;">18.6</td>
<td style="text-align: left;">17.1</td>
</tr>
<tr>
<td style="text-align: left;"> Minimum</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">10</td>
</tr>
<tr>
<td style="text-align: left;"> Maximum</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">100</td>
</tr>
</tbody>
</table>

Data are presented as *n* (%) or % unless otherwise indicated

*cTTO* composite time trade-off, *DCE* discrete choice experiment

</div>

### Modelling

In the feedback module, 13.77% of cTTO responses (*n* = 296) were removed by respondents. The following results include all cTTO valuations after the feedback module (2150–296 = 1854 observations). The mean cTTO values ranged from − 0.260 for health state 33333 to 0.970 for health state 21111 (Table <a href="#Tab3" data-ref-type="table">3</a>). For the adjusted cTTO data, the value for health state 33333 was − 0.350.

<div id="Tab3" class="table-wrap">

<div class="caption">

Composite time trade-off results

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">State</th>
<th rowspan="2" style="text-align: left;"><em>N</em></th>
<th colspan="2" style="text-align: left;">Observed raw data</th>
<th rowspan="2" style="text-align: left;">No. of − 1 observations</th>
<th colspan="2" style="text-align: left;">Adjusted data for censoring at − 1<sup>a</sup></th>
</tr>
<tr>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SE</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">21111</td>
<td style="text-align: left;">205</td>
<td style="text-align: center;">0.9700</td>
<td style="text-align: center;">0.0038</td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">0.9700</td>
<td style="text-align: center;">0.0038</td>
</tr>
<tr>
<td style="text-align: left;">11112</td>
<td style="text-align: left;">205</td>
<td style="text-align: center;">0.9485</td>
<td style="text-align: center;">0.0058</td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">0.9485</td>
<td style="text-align: center;">0.0058</td>
</tr>
<tr>
<td style="text-align: left;">11121</td>
<td style="text-align: left;">207</td>
<td style="text-align: center;">0.9326</td>
<td style="text-align: center;">0.0115</td>
<td style="text-align: left;">1</td>
<td style="text-align: center;">0.9325</td>
<td style="text-align: center;">0.0115</td>
</tr>
<tr>
<td style="text-align: left;">22232</td>
<td style="text-align: left;">169</td>
<td style="text-align: center;">0.4707</td>
<td style="text-align: center;">0.0402</td>
<td style="text-align: left;">11</td>
<td style="text-align: center;">0.4594</td>
<td style="text-align: center;">0.0429</td>
</tr>
<tr>
<td style="text-align: left;">22223</td>
<td style="text-align: left;">180</td>
<td style="text-align: center;">0.4217</td>
<td style="text-align: center;">0.0399</td>
<td style="text-align: left;">13</td>
<td style="text-align: center;">0.4081</td>
<td style="text-align: center;">0.0429</td>
</tr>
<tr>
<td style="text-align: left;">32223</td>
<td style="text-align: left;">175</td>
<td style="text-align: center;">0.2757</td>
<td style="text-align: center;">0.0449</td>
<td style="text-align: left;">18</td>
<td style="text-align: center;">0.2499</td>
<td style="text-align: center;">0.0499</td>
</tr>
<tr>
<td style="text-align: left;">31133</td>
<td style="text-align: left;">172</td>
<td style="text-align: center;">0.1125</td>
<td style="text-align: center;">0.0498</td>
<td style="text-align: left;">27</td>
<td style="text-align: center;">0.0584</td>
<td style="text-align: center;">0.0588</td>
</tr>
<tr>
<td style="text-align: left;">33323</td>
<td style="text-align: left;">170</td>
<td style="text-align: center;">− 0.0250</td>
<td style="text-align: center;">0.0469</td>
<td style="text-align: left;">26</td>
<td style="text-align: center;">− 0.0756</td>
<td style="text-align: center;">0.0550</td>
</tr>
<tr>
<td style="text-align: left;">33233</td>
<td style="text-align: left;">179</td>
<td style="text-align: center;">− 0.0835</td>
<td style="text-align: center;">0.0471</td>
<td style="text-align: left;">35</td>
<td style="text-align: center;">− 0.1584</td>
<td style="text-align: center;">0.0582</td>
</tr>
<tr>
<td style="text-align: left;">33333</td>
<td style="text-align: left;">192</td>
<td style="text-align: center;">− 0.2604</td>
<td style="text-align: center;">0.0425</td>
<td style="text-align: left;">43</td>
<td style="text-align: center;">− 0.3497</td>
<td style="text-align: center;">0.0544</td>
</tr>
</tbody>
</table>

*SE* standard error

<sup>a</sup>Adjustments made using Tobit models

</div>

The coefficients from the mixed logit model, the RAI scores, and the rescaled coefficients (the value set) are shown in Table <a href="#Tab4" data-ref-type="table">4</a>. The results from the mapping model that were used to create the value set can be found in Table S2.1 in the ESM. The predicted values ranged from − 0.283 (for 33333) to 1 (for 11111). The preference ranking, from most to least important, of the dimensions was as follows: (1) PD, (2) AD, (3) UA, (4) SC, and (5) MO. The utility decrements for a movement from MO1 to MO2 and from SC1 to SC2 were particularly small at approximately 0.02. In contrast, the decrement for a movement from PD1 to PD2 was approximately 0.13.

<div id="Tab4" class="table-wrap">

<div class="caption">

Modelling results for the German EQ-5D-Y value set

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Independent variables of the model</th>
<th colspan="3" style="text-align: left;">Latent scale<sup>a</sup></th>
<th style="text-align: left;">Rescaled<sup>b</sup></th>
</tr>
<tr>
<th style="text-align: left;">Coefficient</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Relative attribute importance (%)</th>
<th style="text-align: left;">Value set</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO2</td>
<td style="text-align: left;">− 0.1778** (0.0767)</td>
<td style="text-align: left;">0.1650 (0.1233)</td>
<td rowspan="2" style="text-align: left;">9.2</td>
<td style="text-align: left;">− 0.0242</td>
</tr>
<tr>
<td style="text-align: left;">MO3</td>
<td style="text-align: left;">− 0.8627*** (0.1236)</td>
<td style="text-align: left;">1.0468*** (0.0936)</td>
<td style="text-align: left;">− 0.1175</td>
</tr>
<tr>
<td style="text-align: left;">SC2</td>
<td style="text-align: left;">− 0.1401** (0.0566)</td>
<td style="text-align: left;">0.4098*** (0.1359)</td>
<td rowspan="2" style="text-align: left;">11.3</td>
<td style="text-align: left;">− 0.0191</td>
</tr>
<tr>
<td style="text-align: left;">SC3</td>
<td style="text-align: left;">− 1.0652*** (0.0849)</td>
<td style="text-align: left;">0.5188*** (0.1169)</td>
<td style="text-align: left;">− 0.1450</td>
</tr>
<tr>
<td style="text-align: left;">UA2</td>
<td style="text-align: left;">− 0.6145*** (0.0548)</td>
<td style="text-align: left;">0.1687 (0.2060)</td>
<td rowspan="2" style="text-align: left;">15.5</td>
<td style="text-align: left;">− 0.0837</td>
</tr>
<tr>
<td style="text-align: left;">UA3</td>
<td style="text-align: left;">− 1.4636*** (0.0845)</td>
<td style="text-align: left;">0.5726*** (0.0919)</td>
<td style="text-align: left;">− 0.1993</td>
</tr>
<tr>
<td style="text-align: left;">PD2</td>
<td style="text-align: left;">− 0.9820*** (0.0594)</td>
<td style="text-align: left;">0.0632 (0.0881)</td>
<td rowspan="2" style="text-align: left;">32.7</td>
<td style="text-align: left;">− 0.1337</td>
</tr>
<tr>
<td style="text-align: left;">PD3</td>
<td style="text-align: left;">− 3.0772*** (0.1323)</td>
<td style="text-align: left;">1.4831*** (0.0976)</td>
<td style="text-align: left;">− 0.4190</td>
</tr>
<tr>
<td style="text-align: left;">AD2</td>
<td style="text-align: left;">− 0.9213*** (0.0581)</td>
<td style="text-align: left;">0.2160 (0.1664)</td>
<td rowspan="2" style="text-align: left;">31.3</td>
<td style="text-align: left;">− 0.1254</td>
</tr>
<tr>
<td style="text-align: left;">AD3</td>
<td style="text-align: left;">− 2.9521*** (0.1220)</td>
<td style="text-align: left;">1.6490*** (0.0949)</td>
<td style="text-align: left;">− 0.4019</td>
</tr>
<tr>
<td style="text-align: left;">Log-likelihood</td>
<td colspan="2" style="text-align: left;">− 6094</td>
<td colspan="2" rowspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Observations</td>
<td colspan="2" style="text-align: left;">30,900</td>
</tr>
<tr>
<td style="text-align: left;">Sample size</td>
<td colspan="2" style="text-align: left;">1030</td>
</tr>
</tbody>
</table>

Numbers in parentheses represent standard errors

*AD* feeling worried/sad/unhappy, *cTTO* composite time trade-off, *DCE* discrete choice experiment, *MO* mobility, *PD* having pain/discomfort, *SC* looking after myself, *SD* standard deviation, *UA* doing usual activities

\*\*\**p* \< 0.01, \*\**p* \< 0.05, \**p* \< 0.1

<sup>a</sup>Based on a mixed logit model, with all parameters modelled as random and normally distributed, using 5000 Halton draws. Coefficients indicate the decrement from level 1 to the respective level

<sup>b</sup>Rescaled using a linear mapping model between the DCE results and the adjusted mean values from the cTTO task

</div>

Applying the value set, EQ-5D-Y health state utilities can be estimated by subtracting the relevant decrement for each problem on each dimension from 1. For example, the predicted EQ-5D-Y index value for health state 22233 can be calculated as follows:

``` math
U(22233)\, = \, 1 - 0.0242 - 0.0191 - 0.0837 - 0.4190 - 0.4019\, = \, 0.0521.
```

The symptomatic dimensions (PD and AD) had similar RAI scores, with each about 30%, whereas functional dimensions (MO, SC, and UA) had far lower RAI scores, ranging from 9.2% for MO to 15.5% for UA (Table <a href="#Tab4" data-ref-type="table">4</a>). The decrements of the two symptomatic dimensions, PD and AD, were also similar, with PD having the greatest overall impact. The only dimension with linear utility decrements by level was UA, with larger utility decrements occurring between level 2 and 3 for each of the other dimensions, compared with the decrement between levels 1 and 2 (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<figure id="Fig1">
<p><img src="40273_2022_1143_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40273_2022_1143_Fig1_HTML.gif" /></p>
<figcaption>Utility decrements of German EQ-5D-Y value set. <em>AD</em> feeling worried/sad/unhappy, <em>MO</em> mobility, <em>PD</em> having pain/discomfort, <em>SC</em> looking after myself, <em>UA</em> doing usual activities</figcaption>
</figure>

### Subgroup Analysis: Parental Status

The DCE and cTTO samples showed similar proportions of respondents reporting responsibility for children either at present or in the past (55–56% answering ‘yes’). Demographics differed between parents and non-parents (Table S3.1 in the ESM). For example, non-parents were typically younger, and a higher proportion had high education levels (or were still in education). The DCE results did not differ substantially between these two groups (Table S3.2 in the ESM). Non-parents had a slightly stronger preference for MO and a weaker preference for PD; however, the difference in RAI scores was only 1.4 pp (percentage points) in both cases. Figure <a href="#Fig2" data-ref-type="fig">2</a> illustrates the adjusted mean utilities from the cTTO task for each health state in both subgroups. Mean utilities were always greater for parents than for non-parents. However, only three of the mean differences were statistically significant (two mild and one moderate state). When generating two separate value sets based on data from parents and non-parents, the value sets had significantly different scales (Table S3.3 and Fig. S3.1 in the ESM): the value for 33333 for non-parents was − 0.210 compared with − 0.358 for parents.

<figure id="Fig2">
<p><img src="40273_2022_1143_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2022_1143_Fig2_HTML.gif" /></p>
<figcaption>Comparison of adjusted mean utilities from the composite time trade-off task, by parental status. Mean differences; ***<em>p</em> &lt; 0.01; **<em>p</em> &lt; 0.05; *<em>p</em> &lt; 0.1</figcaption>
</figure>

## Discussion

The EQ-5D-Y valuation study in Germany was one of the first studies to develop an EQ-5D-Y value set. We applied the recently published valuation protocol and obtained health state preferences using a combination of DCE and cTTO. The value set was modelled using a mixed logit model, and the latent DCE coefficients were anchored using a linear mapping approach. The developed German EQ-5D-Y value set can be applied alongside the EQ-5D-Y descriptive system, which is appropriate for use in children and adolescents aged 8–15 years (self-report) and children aged 4–7 years (proxy report); in special cases, the instrument can also be used for adolescents aged 16 or 17 years \[12\]. Indeed, there is discussion on whether values derived considering a 10-year-old in the valuation tasks are suitable for the whole age range of the instrument. A recently published qualitative study indicated that health state preferences for a 10-year-old child might not be representative for the full EQ-5D-Y age range \[33\], whereas quantitate studies did not find significantly different values when different age descriptions were used \[34, 35\].

The results illustrate that the German adult general public considers PD as the most important dimension for children and adolescents, followed by AD. Of the functional dimensions, UA had the highest decrements for level 2 and 3 compared with the two other dimensions (MO and SC). Overall, people consider it important that children and adolescents have no pain/discomfort, are not worried/sad/unhappy, and can do their usual activities without any limitations, as children without health problems do.

The same ordering of the three most important dimensions was observed in the Slovenian EQ-5D-Y valuation study \[16\]. However, the level decrements in all dimensions are higher in the Slovenian than the German EQ-5D-Y value set, with the exception of AD, where decrements are similar. Therefore, the value range is larger in Slovenia (− 0.691 to 1) than in Germany (− 0.283 to 1). Nevertheless, this comparison is limited because Prevolnik Rupel et al. \[16\] used the weighted censored average value of the worst health state 33333 for anchoring, whereas the means of all ten cTTO health states were used for rescaling in Germany. According to the recently published Spanish EQ-5D-Y value set, PD and AD were the two most important dimensions, followed by MO, which differs from the results in Germany and Slovenia. The value range in Spain is relatively large (− 0.539 to 1) and therefore more comparable to the Slovenian than to the German value set \[36\]. In terms of comparability of the value sets, it is worth noting that the Spanish and German EQ-5D-Y value sets were modelled differently \[36\]. The Japanese EQ-5D-Y value set differs from all other EQ-5D-Y value sets as the value range is particularly narrow (0.28–1) and the coefficients are accordingly much smaller. In particular, the level 3 decrements are smaller than those of the German EQ-5D-Y value set. The Japanese team deviated from the protocol by including 26 health states in the cTTO exercise, which also limits comparability \[17\]. Furthermore, there might be cultural differences in the context of valuing child health states between countries that influence the resulting EQ-5D-Y value sets. Notably, the Japanese values for the adult EQ-5D-5L instrument were higher than those of European EQ-5D-5L value sets \[17, 37\].

When comparing the German EQ-5D-5L \[30\] and EQ-5D-Y value sets, it is notable that the latter has a smaller value range and that single decrements per level differ. However, one similarity can be observed: the dimensions with the highest decrements are PD and AD. More detailed comparison is limited because of the different numbers of severity levels between the instruments, the different wording used in the adult- and youth-specific instruments, and the different valuation methods and modelling approaches \[18, 30\].

With the establishment of the valuation protocol, more EQ-5D-Y value sets will be produced in the future, and the influence of using different value sets for children and adolescents and adults in CUA will need to be further explored. There are no guidelines from international agencies on using youth-specific preference-based measures, and there are concerns about how to use youth-specific measures alongside adult measures or how to combine and/or compare these utilities \[6\].

When comparing results by parental status, mean cTTO values were always greater for parents than for non-parents. These differences were only statistically significant for a few health states, although this may partly be explained by the high variation in values for some states (particularly severe states) and the relatively small subgroup sizes. The observed differences are in line with earlier studies \[9, 38\]. Matza et al. \[9\] also found that parents were less willing to trade within TTO tasks, so parents’ responses revealed higher values than those of non-parents. Hartman and Craig \[8\] explored health state values for children using a DCE with a time component, showing that parents preferred a longer lifespan instead of a longer time in healthier states compared with non-parents. If the time component is the key driver of differences between parents and non-parents, this may explain why the DCE results did not differ substantially between these two groups in our study. As noted by Powell et al. \[39\], future valuation studies may benefit from being representative in relation to parental status given the potential impact on preferences when valuing child health. Our results indicate that this representativeness should apply to both the DCE and the cTTO samples.

This study has some limitations. The DCE sample is nationally representative in terms of gender, age groups, education, and region but not necessarily in terms of other variables. Furthermore, there is evidence of a tendency for low-level engagement and random responses when DCEs are administered online \[40\]. We attempted to address this issue by including the QC criteria, but we cannot be entirely sure that the sample consists of only individuals who were fully engaged in the task. However, there is debate within the literature about whether respondents with ‘irrational’ responses should be excluded from analyses \[41\]. Furthermore, a convenience cTTO sample was recruited (rather than a nationally representative sample), and highly educated respondents were overrepresented, which might have influenced the results. Furthermore, the latter portion of the cTTO data collection was affected by the COVID-19 pandemic. Most of the interviews were conducted before the pandemic outbreak, but 32 respondents were interviewed after the lockdown from March to May 2020. These respondents may have had slightly different preferences to the other respondents because of the pandemic. Additionally, the later interviews were online/video interviews, which may also have influenced values, although online interviews have been shown to be feasible, with acceptable data quality \[42\]. Moreover, demographics of the parent and non-parent groups differed, which might have affected health state valuations and the differences found between the two groups. However, differences were as typically expected between these two groups, and it is not possible to disentangle the effects. Additionally, this subgroup analysis was not explicitly considered at the design stage, nor is it part of the EQ-5D-Y valuation protocol, so it was not factored into the experimental design.

It is worth highlighting that there is ongoing discussion on the most appropriate way to value youth health states and analyse valuation data. The EQ-5D-Y valuation protocol represents an initial set of recommendations for achieving this goal but it can (and likely will) be updated over time as further research is conducted (including EQ-5D-Y valuation studies such as this).

## Conclusion

The German EQ-5D-Y valuation study was one of the first studies to apply the recently published EQ-5D-Y valuation protocol. It confirms that the development of EQ-5D-Y value sets using the methods set out in the protocol is feasible. The results of the EQ-5D-Y valuation study in Germany show that the adult general population considers PD and AD to be the most important EQ-5D-Y health dimensions for children and adolescents. The availability of a German EQ-5D-Y value set enables a preference-based HRQoL measurement in children and adolescents in Germany and therefore enables the instrument to be used in economic evaluations, mainly CUAs, of paediatric healthcare interventions. Furthermore, the value set may also prove useful in other contexts (e.g., clinical contexts) in which summarising HRQoL into a single summary score would be helpful.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 67 KB)

</div>

## Acknowledgements

The authors thank Nahne Knizia, Viola Nicasius-Burbach, Lisa Steiner, and Alina Baumgärtner, who acted as interviewers during the study. The authors also thank the EuroQol office staff (Elly Stolk and Bram Roudijk) for their support in conducting the study and their advice/consultation during the data analysis.

IMPACT HTA HRQoL Group: Valentina Prevolnik Rupel<sup>3</sup>, Juan Manuel Ramos-Goñi<sup>4</sup>.

## Funding

Open Access funding enabled and organized by Projekt DEAL.

## Declarations

### Funding

The funding of this study was two-part. Most of the online DCE data collection was conducted within the European Commission-funded project IMPACT HTA (Improved methods and actionable tools for enhancing Health Technology Assessment), work package 5: “Exploring health preferences on different sub-population groups using EQ-5D” (Grant number 779312; [www.impact-hta.eu](http://www.impact-hta.eu)). Additionally obtained DCE data and the cTTO data collection were funded by the EuroQol Research Foundation (EQ project no. 20180510). The European Commission had no role in the study design, collection, and analysis of data; writing of the report; or submission of the paper for publication.

### Conflict of interest

Simone Kreimeier, David Mott, Kristina Ludwig, and Wolfgang Greiner, as well as Valentina Prevolnik Rupel and Juan Manuel Ramos-Goñi (members of the IMPACT HTA HRQoL Group), are members of the EuroQol Group. There are no other conflicts of interest. The views expressed by the authors do not necessarily reflect the views of the EuroQol Group.

### Availability of data and material

All the data and material will be stored and publicly available at the certified data repository Zenodo, hosted by CERN.

### Code availability

Code is available from the authors on request.

### Ethics approval

Ethical approvals for both sub-surveys, using the DCE method and the cTTO method, were received in Germany from the Ethics Committee of Bielefeld University, No. EUB 2018-172 and EUB 2019-204.

### Consent to participate

Not applicable.

### Consent for publication

Not applicable.

### Author contributions

JMR-G prepared the concept and the design of the study. SK, KL, WG, JMR-G, and VPR contributed to the material preparation and data collection. The analysis was performed by DM and SK. The first draft of the manuscript was written by SK and DM, and all authors commented on subsequent versions. All authors read and approved the final manuscript.

### Disclosure

This article is published in a special edition journal supplement wholly funded by the EuroQol Research Foundation

## Footnotes

## Contributor Information

Simone Kreimeier, Email: simone.kreimeier@uni-bielefeld.de.

IMPACT HTA HRQoL Group:

[Valentina Prevolnik Rupel]("Prevolnik Rupel V"[Author]) and [Juan Manuel Ramos-Goñi]("Ramos-Goñi JM"[Author])

## References

## References

1. Drummond MF, Sculpher M, Claxton K, Stoddart GL, Torrance GW. Methods for the economic evaluation of health care programmes. 4. Oxford: Oxford University Press; 2015.

2. Kennedy-Martin M, Slaap B, Herdman M, van Reenen M, Kennedy-Martin T, Greiner W, et al. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020;21:1245–1257. doi: 10.1007/s10198-020-01195-8.

3. Kwon J, Kim SW, Ungar WJ, Tsiplova K, Madan J, Petrou S. Patterns, trends and methodological associations in the measurement and valuation of childhood health utilities. Qual Life Res. 2019;28:1705–1724. doi: 10.1007/s11136-019-02121-z.

4. Chen G, Ratcliffe J. A review of the development and application of generic multi-attribute utility instruments for paediatric populations. Pharmacoeconomics. 2015;33:1013–1028. doi: 10.1007/s40273-015-0286-7.

5. Ungar WJ, Gerber A. The uniqueness of child health and challenges to measuring costs and consequences. In: Ungar WJ, editor. Economic evaluation in child health. Oxford: Oxford Univ. Press; 2010. pp. 3–32.

6. Rowen D, Rivero-Arias O, Devlin N, Ratcliffe J. Review of valuation methods of preference-based measures of health for economic evaluation in child and adolescent populations: where are we now and where are we going? Pharmacoeconomics. 2020;38:325–340. doi: 10.1007/s40273-019-00873-7.

7. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: the instrument's characteristics, development, current use, and challenges of developing its value set. Value Health. 2019;22:31–37. doi: 10.1016/j.jval.2018.11.001.

8. Hartman JD, Craig BM. Comparison of parent and non-parent preferences in the valuation of child health. Value Health. 2016;19:A275. doi: 10.1016/j.jval.2016.03.1960.

9. Matza LS, Boye KS, Feeny DH, Johnston JA, Bowman L, Jordan JB. Impact of caregiver and parenting status on time trade-off and standard gamble utility scores for health state descriptions. Health Qual Life Outcomes. 2014;12:48. doi: 10.1186/1477-7525-12-48.

10. Mott DJ, Shah KK, Ramos-Goñi JM, Devlin NJ, Rivero-Arias O. Valuing EQ-5D-Y-3L health states using a discrete choice experiment: do adult and adolescent preferences differ? Med Decis Mak. 2021;41:584–596. doi: 10.1177/0272989X21999607.

11. Ratcliffe J, Huynh E, Stevens K, Brazier J, Sawyer M, Flynn T. Nothing about us without us? A comparison of adolescent and adult health-state values for the child health utility-9D using profile case best-worst scaling. Health Econ. 2016;25:486–496. doi: 10.1002/hec.3165.

12. EuroQol Research Foundation. EQ-5D-Y user guide: basic information on how to use the EQ-5D-Y instrument. 2014. https://euroqol.org/eq-5d-instruments/eq-5d-y-about/. Accessed 4 Feb 2020.

13. Wille N, Badia X, Bonsel G, Burström K, Cavrini G, Devlin N, et al. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual Life Res. 2010;19:875–886. doi: 10.1007/s11136-010-9648-y.

14. Ravens-Sieberer U, Wille N, Badia X, Bonsel G, Burström K, Cavrini G, et al. Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study. Qual Life Res. 2010;19:887–897. doi: 10.1007/s11136-010-9649-x.

15. Devlin NJ, Brooks R. EQ-5D and the EuroQol Group: past, present and future. Appl Health Econ Health Policy. 2017;15:127–137. doi: 10.1007/s40258-017-0310-5.

16. Prevolnik Rupel V, Ogorevc M. EQ-5D-Y value set for Slovenia. Pharmacoeconomics. 2021;39:463–471. doi: 10.1007/s40273-020-00994-4.

17. Shiroiwa T, Ikeda S, Noto S, Fukuda T, Stolk E. Valuation survey of EQ-5D-Y based on the international common protocol: development of a value set in Japan. Med Decis Mak. 2021;41:597–606. doi: 10.1177/0272989X211001859.

18. Kreimeier S, Oppe M, Ramos-Goñi JM, Cole A, Devlin N, Herdman M, et al. Valuation of EuroQol Five-Dimensional Questionnaire, Youth Version (EQ-5D-Y) and EuroQol Five-Dimensional Questionnaire, Three-Level Version (EQ-5D-3L) health states: the impact of wording and perspective. Value Health. 2018;21:1291–1298. doi: 10.1016/j.jval.2018.05.002.

19. Shah KK, Ramos-Goñi JM, Kreimeier S, Devlin NJ. An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values. Eur J Health Econ. 2020;21:1091–1103. doi: 10.1007/s10198-020-01205-9.

20. Ramos-Goñi JM, Oppe M, Stolk E, Shah K, Kreimeier S, Rivero-Arias O, Devlin N. International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics. 2020;38:653–663. doi: 10.1007/s40273-020-00909-3.

21. Bansback N, Brazier J, Tsuchiya A, Anis A. Using a discrete choice experiment to estimate health state utility values. J Health Econ. 2012;31:306–318. doi: 10.1016/j.jhealeco.2011.11.004.

22. Stolk EA, Oppe M, Scalone L, Krabbe PFM. Discrete choice modeling for the quantification of health states: the case of the EQ-5D. Value Health. 2010;13:1005–1013. doi: 10.1111/j.1524-4733.2010.00783.x.

23. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34:993–1004. doi: 10.1007/s40273-016-0404-1.

24. Janssen BMF, Oppe M, Versteegh MM, Stolk EA. Introducing the composite time trade-off: a test of feasibility and face validity. Eur J Health Econ. 2013;14(Suppl 1):S5–13. doi: 10.1007/s10198-013-0503-2.

25. Devlin NJ, Tsuchiya A, Buckingham K, Tilling C. A uniform time trade off method for states better and worse than dead: feasibility study of the 'lead time' approach. Health Econ. 2011;20:348–361. doi: 10.1002/hec.1596.

26. Federal Statistical Office (DESTATIS). Bevölkerungsstand am 31.12.2018. Fortschreibung des Bevölkerungsstandes auf Grundlage des Zensus 2011. 2019. https://www-genesis.destatis.de/genesis/online?sequenz=statistikTabellen&selectionname=12411#abreadcrumb. Accessed 24 Sept 2019.

27. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJV, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20:466–473. doi: 10.1016/j.jval.2016.10.012.

28. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goñi JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation work: version 2 of the EQ-5D-5L valuation protocol. Value Health. 2019;22:23–30. doi: 10.1016/j.jval.2018.05.010.

29. Ludwig K, von der Schulenburg J-MG, Greiner W. Valuation of the EQ-5D-5L with composite time trade-off for the German population—an exploratory study. Health Qual Life Outcomes. 2017;15:39. doi: 10.1186/s12955-017-0617-9.

30. Ludwig K, Graf von der Schulenburg J-M, Greiner W. German Value Set for the EQ-5D-5L. Pharmacoeconomics. 2018;36:663–674. doi: 10.1007/s40273-018-0615-8.

31. Vass C, Boeri M, Karim S, Marshall D, Craig B, Ho K, Mott DJ, Ngorsuraches S, Badawy S, Muhlbacher A, Gonzalez J, Heidenreich S. Accounting for preference heterogeneity in discrete-choice experiments: a review of the state of practice. Value Health. 2022. (forthcoming). doi:10.1016/j.jval.2022.01.012

32. Rowen D, Brazier J, van Hout B. A comparison of methods for converting DCE values onto the full health-dead QALY scale. Med Decis Mak. 2015;35:328–340. doi: 10.1177/0272989X14559542.

33. Reckers-Droog V, Karimi M, Lipman S, Verstraete J. Why do adults value EQ-5D-Y-3L health states differently for themselves than for children and adolescents: a think-aloud study. Value Health. 2022 doi: 10.1016/j.jval.2021.12.014.

34. Retra JGA, Essers BAB, Joore MA, Evers SMAA, Dirksen CD. Age dependency of EQ-5D-Youth health states valuations on a visual analogue scale. Health Qual Life Outcomes. 2020;18:386. doi: 10.1186/s12955-020-01638-z.

35. Ramos-Goñi JM, Carillo AE, Rivero-Arias O, Rowen D, Mott DJ, Shah K, Oppe M. Does changing the age of a child to be considered in EQ-5D-Y-3L DCE based valuation studies affect health preferences? Value Health. 2022. (forthcoming). doi:10.1016/j.jval.2022.03.001

36. Ramos-Goñi JM, Oppe M, Estévez-Carrillo A, Rivero-Arias O, Wolfgang G, Simone K, et al. Accounting for unobservable preference heterogeneity and evaluating alternative anchoring approaches to estimate country-specific EQ-5D-Y value sets: a case study using Spanish preference data. Value Health. 2021 doi: 10.1016/j.jval.2021.10.013.

37. Shiroiwa T, Ikeda S, Noto S, Igarashi A, Fukuda T, Saito S, Shimozuma K. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19:648–654. doi: 10.1016/j.jval.2016.03.1834.

38. van der Pol M, Shiell A. Extrinsic goals and time tradeoff. Med Decis Mak. 2007;27:406–413. doi: 10.1177/0272989X07302127.

39. Powell PA, Rowen D, Rivero-Arias O, Tsuchiya A, Brazier JE. Valuing child and adolescent health: a qualitative study on different perspectives and priorities taken by the adult general public. Health Qual Life Outcomes. 2021;19:222. doi: 10.1186/s12955-021-01858-x.

40. Mulhern B, Longworth L, Brazier J, Rowen D, Bansback N, Devlin N, Tsuchiya A. Binary choice health state valuation and mode of administration: head-to-head comparison of online and CAPI. Value Health. 2013;16:104–113. doi: 10.1016/j.jval.2012.09.001.

41. Lancsar E, Louviere J. Deleting 'irrational' responses from discrete choice experiments: a case of investigating or imposing preferences? Health Econ. 2006;15:797–811. doi: 10.1002/hec.1104.

42. Lipman SA. Time for Tele-TTO? Lessons learned from digital interviewer-assisted time trade-off data collection. Patient. 2021;14:459–469. doi: 10.1007/s40271-020-00490-z.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 67 KB)

</div>

[^1]: The terms ‘youth specific’ and ‘youth’ as used in this paper refer to both children and adolescents.

[^2]: Due to the number of levels, the EQ-5D-Y is sometimes also referred to as the EQ-5D-Y-3L as a version with five levels is also under development.

[^3]: To address a research objective outside the scope of this paper, the interviews also contained 15 DCE tasks after point seven. However, as these data are not relevant to the context of this article, they are not considered further here.

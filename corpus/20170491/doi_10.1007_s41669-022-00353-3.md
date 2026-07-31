---
project_id: "20170491"
work_id: "doi:10.1007/s41669-022-00353-3"
doi: "10.1007/s41669-022-00353-3"
pmid: "35927410"
pmcid: "PMC9362639"
title: "An EQ-5D-5L Value Set for Belgium"
journal: "PharmacoEconomics Open"
publication_date: "2022-08-04"
volume: "6"
issue: "6"
authors:
  - name: "Nicolas Bouckaert"
    affiliation_ids:
      - "Aff1"
  - name: "Irina Cleemput"
    affiliation_ids:
      - "Aff1"
  - name: "Stephan Devriese"
    affiliation_ids:
      - "Aff1"
  - name: "Sophie Gerkens"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Belgian Health Care Knowledge Centre (KCE), Boulevard du Jardin Botanique 55, 1000 Bruxelles, Belgium"
licence: "cc-by-nc"
source_file: "input/projects/20170491/papers/doi_10.1007_s41669-022-00353-3.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9362639/fullTextXML"
source_method: "epmc_xml"
source_sha256: "c02746111cab030771ec13406412902165f3ec1bff6505a5ca66a0305ba0e866"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# An EQ-5D-5L Value Set for Belgium

## Abstract

### Objective

This study aimed to establish a Belgian EQ-5D-5L value set based on the preferences of the adult Belgian general population.

### Methods

The most recent EuroQol Valuation Technology (EQ-VT 2.1) protocol for EQ-5D-5L valuation studies was followed. Computer-assisted personal interviews were carried out in a representative sample of the adult Belgian population. Potential respondents were randomly selected from the National Register using a multistage, stratified, cluster sampling with unequal probability design. Each respondent valued 10 or 11 health states using composite time trade-off (cTTO) and 14 health states in seven paired choice tasks using a discrete choice experiment (DCE). Different model specifications were explored and assessed based on logical consistency, goodness of fit, predictive accuracy and theoretical considerations.

### Results

A total of 892 respondents were included in the analyses. The sample was representative of the Belgian adult population in terms of age, sex, region of residence, educational attainment, labour market status, self-assessed health status and health-related quality of life (HRQoL). The preferred model specification was a hybrid (DCE and cTTO data combined) multiplicative eight-coefficient model with intercept random effects and correction for heteroskedasticity. Values range from − 0.532 to 1. Loss of HRQoL is highest in the dimension pain/discomfort, closely followed by anxiety/depression.

### Conclusions

This study developed a Belgian EQ-5D-5L value set, based on the preferences of the Belgian adult general population. It provides opportunities for future clinical and economic evaluations in healthcare, for the measurement of patient-reported outcomes and for population health assessments.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s41669-022-00353-3.

Accepted 2022 Jul 5; Collection date 2022 Nov.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| This study established an EQ-5D-5L value set for Belgium, based on the preferences of a random sample of the Belgian general public in 2018–2020. |
| The value set allows researchers and decision makers to value health states described by means of the EQ-5D-5L. It can be employed to assess the impact of health interventions on health-related quality of life in cost-utility analyses or to value patient-reported outcomes measured in trials using the EQ-5D-5L. |
| The current value set should replace the former crosswalk value set used in Belgium. |

</div>

## Introduction

In Belgium, the submission of a health economic evaluation has been mandatory since 2002 for reimbursement requests concerning drugs with a claimed added therapeutic value compared to existing alternatives \[1, 2\]. Guidelines for economic evaluations were first developed in 2008 and updated in 2012 by the Belgian Health Care Knowledge Centre (KCE). Belgium is one of many countries to recommend the use of the EQ-5D to measure health-related quality of life (HRQoL) and to calculate quality-adjusted life years (QALYs) \[1, 3\].

The EQ-5D is a generic multi‑attribute utility instrument with five dimensions to measure health and HRQoL: mobility (MO), self-care (SC), usual activities (UA), pain/discomfort (PD) and anxiety/depression (AD). Depending on the version of the instrument, each health dimension has either three levels of severity (EQ-5D-3L; 3L: no, some/moderate, extreme problems/unable to) or five levels of severity (EQ-5D-5L; 5L: no, slight, moderate, severe, extreme problems/unable to). By increasing the number of response categories per dimension, the five-level version can describe substantially more health states than the earlier three-level version (3125 vs 243), which has improved the discriminatory power of the EQ-5D and reduced its ceiling effects \[4–8\].

An EQ-5D value set assigns a utility value to each health state that can be described with the EQ-5D. A utility value reflects the HRQoL of a health state, based on the preferences of the general public. It is anchored on a scale with 1 equal to full health and 0 equal to dead \[9, 10\]. Health states considered worse than dead have negative utility values \[11\].

While a value set for the EQ-5D-3L has existed since 2003 \[12\], no value set specific to the EQ-5D-5L was available for Belgium. As an intermediary solution, an EQ-5D-5L “crosswalk” value set could be derived from the EQ-5D-3L value set using the mapping procedure proposed by van Hout et al. \[13\]. However, to benefit from the full potential of the EQ-5D-5L, a value set specific to the five-level version was necessary. The objective of this study was to derive a Belgian EQ-5D-5L value set based on preferences of a representative sample of the adult Belgian population.

## Methods

This study followed the most recent EuroQol Valuation Technology (EQ-VT 2.1) protocol for EQ-5D-5L valuation studies \[14, 15\]. The research protocol was approved by the Ethical Committee of the University hospital of Ghent (B670201835610). The reporting of this study follows the CREATE guidelines for valuation studies of multi-attribute utility-based instruments \[16\].

### Sample Selection

Following Oppe and van Hout \[17\], a sample of 1000 respondents with a valid interview was targeted to ensure precision in the model estimates. Potential respondents aged 18–100 years old were randomly selected using a multistage, stratified, cluster sampling with unequal probability design, comparable in design to Demarest et al. \[18\] (more details in the Electronic Supplementary Material: ESM1). In the first stage, a geographical stratification was made, with random selection of municipalities in each province proportional to the provincial population size. Municipalities can be drawn multiple times, and for each draw, ten interviews were allocated. Second, interviews were assigned to a combination of sex and age group (18–29, 30–39, 40–49, 50–59, 60–69, 70–79, 80–89, 90–99), proportional to the provincial demographic composition. Figure <a href="#Fig1" data-ref-type="fig">1</a> presents the selected municipalities and the number of assigned interviews. A good geographic coverage was obtained.

<figure id="Fig1">
<p><img src="41669_2022_353_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="41669_2022_353_Fig1_HTML.gif" /></p>
<figcaption>Selected municipalities and number of interviews (map of Belgium)</figcaption>
</figure>

To deal with non-participation and low-quality interviews, ten potential candidates were selected for each targeted interview from the National Register, which lists all persons officially residing in Belgium. Institutionalized individuals were excluded.

Post-stratification weights (detailed in ESM1) were used to correct for differences between planned and realised interviews.

### Valuation Interview

Professional interviewers from a market research company conducted face-to-face interviews using computer-assisted personal interview (CAPI) software developed by EuroQol for EQ-5D-5L valuation studies \[15\]. The software included interview scripts translated to Dutch and French by a professional translation agency and reviewed by the research team. At the end of the study, because of a transfer to a new EQ-VT platform, it appeared that in the Dutch version, severity level 2 in dimension MO was incorrectly labelled, i.e. “*lopen*” was used instead of “*rondwandelen*”. This was due to the fact that “*lopen*” and “*rondwandelen*” are Dutch for “*walking about*” used in, respectively, the Netherlands and Belgium. The impact of the incorrect labelling was expected to be limited because interviewers also had a printed questionnaire with the correct labels to assist respondents in assessing the severity of the health states described on the screen.

Each interview followed the same structure: (1) introduction to the study, (2) basic background questions (age, sex, health status using EQ-5D-5L descriptive system and EuroQol visual analogue scale (VAS), experiences of severe illness), (3) valuation with composite time trade-off (cTTO), (4) valuation with discrete choice experiment (DCE), (5) country-specific background questions (educational attainment, labour market position, self-assessed health).

#### Techniques for Eliciting Preferences

Two elicitation techniques were used—cTTO and DCE—to gain distinct but complementary information on the respondent’s preferences.

The cTTO valuation applies the standard time trade-off (TTO) for health states considered better than dead and shifts to lead-time TTO for health states valued worse than dead by the respondent \[19\] (more detailed descriptions in \[11, 19–21\]). The resulting cTTO values range between −1 (trading all lead time) and 1 (trading no time) with 0.05 increments. After receiving instructions, the interviewer familiarized the respondent with cTTO by means of an example state “being in a wheelchair”, followed by the evaluation of three practice health states and ten real EQ-5D-5L health states. In a feedback module after finalizing the cTTO task, the respondent was presented with a ranking of the health states based on his/her responses and could mark health states for which the relative rank was deemed unsatisfactory.

In the DCE task, respondents were asked to indicate their preference between two EQ-5D-5L health states (forced choice). After receiving instructions, each respondent performed seven choice tasks.

#### Health States Valued

The EQ-VT experimental design includes a subset of health states to be evaluated by the respondent. These states were selected using a Monte Carlo simulation \[17, 22\].

For the cTTO, a subset of 86 health states were divided into ten blocks with ten health states per block \[23, 24\]. The blocks were balanced regarding the severity of the included states, with each block consisting of one mild state (i.e. four dimensions with severity level 1 and one dimension with severity level 2, e.g. 21111), the most severe state (i.e. state 55555) and eight intermediary states \[14, 17, 24\]. Each block was randomly assigned to respondents and states were presented in a random order.

The *unconscious state* is not part of the EQ-5D-5L descriptive system, and is not by default included in valuation \[25\]. However, the research team deemed it important for clinical research to obtain a utility value for this state, which was also included in the Belgian EQ-5D-3L value set \[12\]. The unconscious state was added as an 11th state to two cTTO blocks as the last state to be valued to avoid interference with the standard cTTO procedure.

For the DCE, 196 choice pairs of EQ-5D-5L health states were divided over 28 blocks of seven pairs \[23, 24\]. The health states in a choice pair were comparable in severity and no choice pairs had to be evaluated where one alternative logically dominated the other. The assignment of a block to a respondent was randomized as was the order of paired choices and the left–right positioning of the states.

### Data Collection and Quality Control

Interviewers were selected based on their experience in handling complex interviews. Prior to deployment, they received one-day training and performed five pilot interviews. A detailed account of the deployed interviewers and fieldwork is provided in ESM2.

Throughout the fieldwork, the quality of the collected data, the interviewer’s overall performance and the compliance with the interview script were monitored using a quality control (QC) tool integrated in the EQ-VT software \[26\]. At regular times, the EuroQol support team drafted QC reports and provided feedback. Interviews that did not meet specific criteria were flagged as “potentially poor quality” and were removed according to pre-defined rules \[15\]. Interviewers with a high rate of flagged interviews were retrained or excluded.

### Modelling and Data Analysis

The representativeness of the sample after data cleaning was assessed descriptively. For value set construction, a range of potential regression models were estimated. Multiple criteria were assessed to select a preferred model. The resulting EQ-5D-5L value set was then compared to the current EQ-5D-3L value set.

#### Final Sample

In addition to interviews excluded in the QC process, we excluded respondents who could not be linked to the sample plan due to an inaccurate registration ID. We also excluded respondents with implausible cTTO response patterns, based on three criteria drawn from previous valuation studies \[19, 27–32\]:

1.  cTTO values were positively associated with the level sum score (misery index) of the health states in a linear regression.

2.  All health states were given the same cTTO value.

3.  The mild and most severe health state were given the same cTTO value.

In consultation with EuroQol, health states flagged in the feedback module were not excluded by default, this in deviation from the EQ-VT protocol and recent valuation studies \[21, 33–35\]. The main concern was to not further reduce the sample size (see “<a href="#Sec5" data-ref-type="sec">Results</a>” section), which was smaller than targeted given the discontinuation of the data collection due to the coronavirus disease 2019 (COVID-19) crisis (see ESM2). The robustness of the results regarding this choice was tested (see Sect. <a href="#Sec14" data-ref-type="sec">2.4.4</a>). No restrictions were imposed based on the DCE data.

Summary statistics of the final sample were calculated to assess representativeness to the Belgian population. Belgian population characteristics were obtained from Statistics Belgium, the Belgian Health Interview Survey (HIS) and the EU Statistics on Income and Living Conditions (EU-SILC).

#### Modelling Approach

As only a subset of health states was valued directly by DCE or cTTO, a modelling approach was pursued to produce a value set for all EQ-5D-5L health states. The EQ-VT protocol does not prescribe a specific model.

The modelling approach consisted in the estimation and evaluation of a large number of potential regression models. Models were fitted on cTTO data only, DCE data only and on the combined cTTO and DCE data (hybrid model) to maximize the available information \[36\].

Based on the literature, four main regression specifications were used, each with the same dependent and independent variables, but a different set of estimated coefficients \[37–40\]. Twenty independent variables were defined, i.e. four binary variables in each dimension indicating the severity level of the state, with level 1 being the reference. The dependent variable was different for the cTTO data, i.e. the reported disutility or deviation in utility from the full health state, and the DCE data, i.e. the choice made between two states. Disutility was preferred over utility because it is always positive (range 0–2), and thus easier to model.

In addition to the frequently used 20-coefficients additive model (ADD20)—with one coefficient for each binary variable—we also applied three multiplicative specifications with 8, 9 or 11 coefficients, allowing for different interactions between levels and dimensions as described in Rand-Hendriksen et al. \[37\], and referred to as MULT8, MULT9 and MULT11. While the additive model is more flexible and more widely used in valuation studies \[21–23, 27, 28, 30–35, 41–47\], research showed that the more restrictive, non-linear multiplicative models might perform better in terms of predictive accuracy \[37, 38, 48\]. Formal specifications are presented in ESM3.

For cTTO-only and hybrid models, different potential alternatives were tested within these four core specifications, again based on the literature: with/without *intercept*; with/without *random effects* (a respondent-specific component in the error term, which can be interpreted as individual variation around the intercept); with/without *heteroscedasticity* (a correction for increasing variability in reported cTTO values as health states worsen) following Ramos-Goñi et al. \[36\]; with/without *censoring* (correction for respondents who would like to value health states below the minimum cTTO value capped at −1 by design).

All models were fitted using maximum likelihood with SAS 9.4 procedure NLMIXED \[49\].

#### Model Selection

The final model should be able to fit the underlying data and predict values based on a subset of observed states. Model selection was based on four criteria (further elaborated in ESM4):

1.  *Logical consistency*: Disutility in a health dimension does not decrease as severity increases.

2.  *Goodness of fit (cTTO-only models)*: Ability of a model to fit the observed data.

3.  *Predictive accuracy (cTTO-only models)*: Ability of a model to predict unobserved values.

4.  *Theoretical considerations:* Evaluation of features (hybrid model, heteroscedasticity, censoring) that may be desirable from a theoretical point of view, but may reduce the model’s performance in terms of predictive accuracy or goodness of fit.

Criteria 1–3 were used to narrow down the selection regarding the core specification (ADD20, MULT8, MULT9, MULT11), the use of an intercept and random effects. Theoretical considerations were substantiated with suggestive evidence where possible.

#### Sensitivity Analysis

The robustness of the results was tested by re-estimating the model using three different data samples: (1) sample without exclusions based on implausible response patterns (see Sect. <a href="#Sec11" data-ref-type="sec">2.4.1</a>); (2) sample excluding interviews collected after the onset of the COVID-19 pandemic (about 5% of the respondents); and (3) sample excluding observations flagged in the feedback module (about 4% of the cTTO observations).

#### Comparing Value Sets

The main features and Kernel density distribution of the Belgian EQ-5D-5L value set was compared with the current Belgian EQ-5D-3L and related crosswalk value sets \[12, 13\].

## Results

### Sample Characteristics

Between May 2018 and September 2020, 22 interviewers performed 916 interviews that passed the EuroQol QC process, while six interviewers performed poorly and had their interviews dropped (*n* = 96) (see ESM2). In addition, 24 further interviews were excluded due to inaccurate IDs (*n* = 3) and implausible responses (*n* = 21) (see Section <a href="#Sec11" data-ref-type="sec">2.4.1</a>), leaving a final sample of 892 respondents.

Sample characteristics are presented in Table <a href="#Tab1" data-ref-type="table">1</a>. The sample was representative of the Belgian adult population in terms of age, sex, region of residence, educational attainment, labour market status, self-assessed health status and HRQoL. Three quarters of the respondents rated their health as good or very good and about 35% reported no health problem in any EQ-5D dimension, a slightly lower fraction than in the Belgian HIS. Problems related to PD were most frequently reported.

<div id="Tab1" class="table-wrap">

<div class="caption">

General characteristics of respondents and the Belgian general adult population

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristics</th>
<th colspan="2" style="text-align: left;">Final sample (<em>N</em> = 892)</th>
<th style="text-align: left;">Belgian general adult population</th>
<th style="text-align: left;">Difference sample − population</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><em>N</em></th>
<th style="text-align: left;">% (weighted)</th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">Percentage points</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;">Demographics (sex, age group)*</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 18–29</td>
<td style="text-align: center;">84</td>
<td style="text-align: center;">9.3</td>
<td style="text-align: center;">9.3</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 30–39</td>
<td style="text-align: center;">70</td>
<td style="text-align: center;">8.2</td>
<td style="text-align: center;">8.1</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 40–49</td>
<td style="text-align: center;">70</td>
<td style="text-align: center;">8.6</td>
<td style="text-align: center;">8.5</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 50–59</td>
<td style="text-align: center;">80</td>
<td style="text-align: center;">8.9</td>
<td style="text-align: center;">8.8</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 60–69</td>
<td style="text-align: center;">63</td>
<td style="text-align: center;">7.0</td>
<td style="text-align: center;">7.0</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 70–79</td>
<td style="text-align: center;">42</td>
<td style="text-align: center;">4.4</td>
<td style="text-align: center;">4.3</td>
<td style="text-align: center;">0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 80–89</td>
<td style="text-align: center;">18</td>
<td style="text-align: center;">2.1</td>
<td style="text-align: center;">2.2</td>
<td style="text-align: center;">–0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Male, aged 90–99</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0.1</td>
<td style="text-align: center;">0.3</td>
<td style="text-align: center;">–0.3</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 18–29</td>
<td style="text-align: center;">84</td>
<td style="text-align: center;">9.2</td>
<td style="text-align: center;">9.2</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 30–39</td>
<td style="text-align: center;">75</td>
<td style="text-align: center;">8.2</td>
<td style="text-align: center;">8.1</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 40–49</td>
<td style="text-align: center;">72</td>
<td style="text-align: center;">8.4</td>
<td style="text-align: center;">8.3</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 50–59</td>
<td style="text-align: center;">84</td>
<td style="text-align: center;">8.8</td>
<td style="text-align: center;">8.8</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 60–69</td>
<td style="text-align: center;">70</td>
<td style="text-align: center;">7.7</td>
<td style="text-align: center;">7.3</td>
<td style="text-align: center;">0.3</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 70–79</td>
<td style="text-align: center;">43</td>
<td style="text-align: center;">5.2</td>
<td style="text-align: center;">5.2</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 80–89</td>
<td style="text-align: center;">31</td>
<td style="text-align: center;">3.6</td>
<td style="text-align: center;">3.6</td>
<td style="text-align: center;">0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Female, aged 90–99</td>
<td style="text-align: center;">5</td>
<td style="text-align: center;">0.4</td>
<td style="text-align: center;">0.8</td>
<td style="text-align: center;">–0.4</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Region of residence*</td>
</tr>
<tr>
<td style="text-align: left;"> Flanders</td>
<td style="text-align: center;">529</td>
<td style="text-align: center;">58.2</td>
<td style="text-align: center;">58.2</td>
<td style="text-align: center;">0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Wallonia</td>
<td style="text-align: center;">293</td>
<td style="text-align: center;">31.6</td>
<td style="text-align: center;">31.7</td>
<td style="text-align: center;">–0.1</td>
</tr>
<tr>
<td style="text-align: left;"> Brussels</td>
<td style="text-align: center;">70</td>
<td style="text-align: center;">10.2</td>
<td style="text-align: center;">10.2</td>
<td style="text-align: center;">0.0</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Educational attainment (highest degree)<sup>§</sup></td>
</tr>
<tr>
<td style="text-align: left;"> No degree, primary or lower secondary</td>
<td style="text-align: center;">212</td>
<td style="text-align: center;">24.0</td>
<td style="text-align: center;">25.8</td>
<td style="text-align: center;">–1.8</td>
</tr>
<tr>
<td style="text-align: left;"> Secondary or post-secondary</td>
<td style="text-align: center;">303</td>
<td style="text-align: center;">34.0</td>
<td style="text-align: center;">36.5</td>
<td style="text-align: center;">–2.5</td>
</tr>
<tr>
<td style="text-align: left;"> Tertiary</td>
<td style="text-align: center;">370</td>
<td style="text-align: center;">42.0</td>
<td style="text-align: center;">37.7</td>
<td style="text-align: center;">4.3</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Labour marker status<sup>§</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Employee</td>
<td style="text-align: center;">423</td>
<td style="text-align: center;">47.5</td>
<td style="text-align: center;">45.2</td>
<td style="text-align: center;">2.3</td>
</tr>
<tr>
<td style="text-align: left;"> Self-employed</td>
<td style="text-align: center;">53</td>
<td style="text-align: center;">6.2</td>
<td style="text-align: center;">6.0</td>
<td style="text-align: center;">0.2</td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">4.2</td>
<td style="text-align: center;">4.0</td>
<td style="text-align: center;">0.2</td>
</tr>
<tr>
<td style="text-align: left;"> Inactive (including students)</td>
<td style="text-align: center;">136</td>
<td style="text-align: center;">15.5</td>
<td style="text-align: center;">19.0</td>
<td style="text-align: center;">–3.5</td>
</tr>
<tr>
<td style="text-align: left;"> Retired</td>
<td style="text-align: center;">237</td>
<td style="text-align: center;">26.6</td>
<td style="text-align: center;">25.3</td>
<td style="text-align: center;">1.3</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Self-assessed health<sup>§</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Very good</td>
<td style="text-align: center;">228</td>
<td style="text-align: center;">26.4</td>
<td style="text-align: center;">27.7</td>
<td style="text-align: center;">–1.3</td>
</tr>
<tr>
<td style="text-align: left;"> Good</td>
<td style="text-align: center;">438</td>
<td style="text-align: center;">49.0</td>
<td style="text-align: center;">46.3</td>
<td style="text-align: center;">2.7</td>
</tr>
<tr>
<td style="text-align: left;"> Fair</td>
<td style="text-align: center;">157</td>
<td style="text-align: center;">17.5</td>
<td style="text-align: center;">16.9</td>
<td style="text-align: center;">0.6</td>
</tr>
<tr>
<td style="text-align: left;"> Bad</td>
<td style="text-align: center;">54</td>
<td style="text-align: center;">6.1</td>
<td style="text-align: center;">7.5</td>
<td style="text-align: center;">–1.4</td>
</tr>
<tr>
<td style="text-align: left;"> Very bad</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">1.0</td>
<td style="text-align: center;">1.6</td>
<td style="text-align: center;">–0.6</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Health status EQ-5D-5L<sup>#</sup></td>
</tr>
<tr>
<td style="text-align: left;"> No problem reported (state 11111)</td>
<td style="text-align: center;">307</td>
<td style="text-align: center;">34.6</td>
<td style="text-align: center;">40.7</td>
<td style="text-align: center;">–6.1</td>
</tr>
<tr>
<td style="text-align: left;"> Problem with mobility</td>
<td style="text-align: center;">199</td>
<td style="text-align: center;">22.7</td>
<td style="text-align: center;">17.4</td>
<td style="text-align: center;">5.3</td>
</tr>
<tr>
<td style="text-align: left;"> Problem with self-care</td>
<td style="text-align: center;">59</td>
<td style="text-align: center;">6.2</td>
<td style="text-align: center;">5.7</td>
<td style="text-align: center;">0.5</td>
</tr>
<tr>
<td style="text-align: left;"> Problem with usual activities</td>
<td style="text-align: center;">195</td>
<td style="text-align: center;">21.6</td>
<td style="text-align: center;">18.0</td>
<td style="text-align: center;">3.6</td>
</tr>
<tr>
<td style="text-align: left;"> Problem with anxiety/depression</td>
<td style="text-align: center;">264</td>
<td style="text-align: center;">28.9</td>
<td style="text-align: center;">22.9</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;"> Problem with pain/discomfort</td>
<td style="text-align: center;">517</td>
<td style="text-align: center;">57.9</td>
<td style="text-align: center;">53.0</td>
<td style="text-align: center;">4.9</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><em>N</em></th>
<th style="text-align: left;">Mean score</th>
<th style="text-align: left;">Mean score</th>
<th style="text-align: left;">Difference in score</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;">Visual Analog Scale (EQ-VAS) by age^</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 15–24</td>
<td style="text-align: center;">93</td>
<td style="text-align: center;">85.9</td>
<td style="text-align: center;">82.9</td>
<td style="text-align: center;">3.0</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 25–34</td>
<td style="text-align: center;">151</td>
<td style="text-align: center;">82.9</td>
<td style="text-align: center;">80.7</td>
<td style="text-align: center;">2.2</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 35–44</td>
<td style="text-align: center;">126</td>
<td style="text-align: center;">80.5</td>
<td style="text-align: center;">78.3</td>
<td style="text-align: center;">2.2</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 45–54</td>
<td style="text-align: center;">147</td>
<td style="text-align: center;">75.6</td>
<td style="text-align: center;">77.3</td>
<td style="text-align: center;">–1.7</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 55–64</td>
<td style="text-align: center;">162</td>
<td style="text-align: center;">75.2</td>
<td style="text-align: center;">76.1</td>
<td style="text-align: center;">–0.9</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 65–74</td>
<td style="text-align: center;">119</td>
<td style="text-align: center;">75.2</td>
<td style="text-align: center;">73.5</td>
<td style="text-align: center;">1.7</td>
</tr>
<tr>
<td style="text-align: left;"> Aged 75 or more</td>
<td style="text-align: center;">94</td>
<td style="text-align: center;">67.7</td>
<td style="text-align: center;">67.3</td>
<td style="text-align: center;">0.4</td>
</tr>
</tbody>
</table>

Six respondents had missing values regarding country-specific background questions (educational attainment, labour market status, self-assessed health)

*EU-SILC* EU Statistics on Income and Living Conditions, *HIS* Health Interview Survey

\*Population characteristics from population data on 1 January 2017 provided by Statistics Belgium

<sup>§</sup>Population characteristics from EU-SILC data wave 2019

<sup>\#</sup>Population characteristics from Belgian HIS wave 2018

^Population characteristics from Belgian HIS wave 2013

</div>

### Data Characteristics

The full range of potential cTTO values was observed, although there was clustering at key values (see ESM5 for details on the distribution of cTTO values). No or a very limited willingness to trade off life years to avoid health problems was observed in 9.5% (value 1) and 9.9% (value 0.95) of the responses. All available lead time was exhausted in 9.1% of the responses (value −1). Overall, 25.2% of cTTO values were negative. There was inter-interviewer variation regarding the fraction of responses clustered at −1 (range 0–32%) and the fraction of negatively valued states (range 4–50%) (see ESM5).

Figure <a href="#Fig2" data-ref-type="fig">2</a> indicates that as health states worsen, cTTO values decrease and the variability is higher (difference 5th percentile \[P5\] and 95th percentile \[P95\] increases up to misery index 13, difference 25th percentile \[P25\] and 75th percentile \[P75\] increases up to misery index 18). The former supports the face validity of the data, while the latter is indicative of heteroscedasticity.

<figure id="Fig2">
<p><img src="41669_2022_353_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="41669_2022_353_Fig2_HTML.gif" /></p>
<figcaption>Distribution of cTTO value by level sum score.<br />
The whiskers of the boxplot indicate the 5th percentile (P5) and 95th percentile (P95). <em>cTTO</em> composite time trade-off</figcaption>
</figure>

In support of the face validity of the DCE data, a correlation was found between the chosen state and the difference in misery index between both states (see Fig. <a href="#Fig3" data-ref-type="fig">3</a>). The health state with the lower misery index was favoured with the preference being more pronounced as the difference widened.

<figure id="Fig3">
<p><img src="41669_2022_353_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="41669_2022_353_Fig3_HTML.gif" /></p>
<figcaption>Preference for alternative A or B in DCE task by difference in level sum score (misery index).<br />
<em>DCE</em> discrete choice experiment</figcaption>
</figure>

### Preferred Model (Belgian EQ-5D-5L Model)

Taking all selection criteria into consideration, the hybrid version of the multiplicative eight-coefficient model with intercept for the cTTO data, with random effects and correction for heteroskedasticity, was selected as the preferred model (the full specification and details of the selection process are given in ESM6).

In summary, the additive cTTO-only model had the best fit, but was excluded because of logical inconsistencies in the coefficients of levels 2/3 in dimension UA. After enforcing logical consistency in dimension UA, inconsistencies showed up in levels 2/3 and 4/5 in dimension SC and levels 1/2 in dimension PD. No inconsistency was found in cTTO-only models for dimension MO, which was reassuring given the incorrect Dutch level 2 label. Second, the multiplicative models,—particularly MULT8 and MULT9, with intercept, random effects and correction for heteroscedasticity performed best on predictive accuracy, while also having a good fit. Third, as the data showed heteroskedasticity, a correction was applied. Fourth, following a high level of agreement between results from DCE-only and cTTO-only models, the combination of both data types in a hybrid model was justified to improve accurateness. In addition, data were not treated as censored given that predictions of the DCE-only models—by design uncensored—had a better fit with results from uncensored cTTO-only models \[28\]. Finally, as the additional coefficient in the MULT9 model was statistically insignificant, the MULT8 model was preferred.

Table <a href="#Tab2" data-ref-type="table">2</a> presents the coefficients and bootstrapped standard errors of the preferred model. The scatterplot (Fig. <a href="#Fig4" data-ref-type="fig">4</a>) between predicted and observed (cTTO) values shows a good fit for the 86 evaluated health states. The utility decrements for the different dimensions at severity level 5 amount to: 0.227 (MO), 0.166 (SC), 0.181 (UA), 0.482 (PD) and 0.439 (AD). This needs to be multiplied with a rescaling factor of 0, 0.139, 0.258, 0.788 or 1 for severity levels 1–5, respectively. The overall utility loss for deviating from full health (intercept) equals 0.038. Loss of HRQoL is highest in the dimension PD, closely followed by AD.

<div id="Tab2" class="table-wrap">

<div class="caption">

Coefficients and bootstrapped standard errors of the preferred model and results of the sensitivity analysis

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">Preferred model</th>
<th colspan="3" style="text-align: left;">Sensitivity analysis</th>
</tr>
<tr>
<th style="text-align: left;">Coefficient value</th>
<th style="text-align: left;">Standard error</th>
<th style="text-align: left;">T statistic</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">Sample, no exclusions on cTTO values</th>
<th style="text-align: left;">Restricted sample pre-COVID</th>
<th style="text-align: left;">Restricted sample feedback module</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span class="math inline"><em>I</em><em>n</em><em>t</em><em>e</em><em>r</em><em>c</em><em>e</em><em>p</em><em>t</em></span></td>
<td style="text-align: center;">0.038</td>
<td style="text-align: center;">0.0148</td>
<td style="text-align: center;">2.55</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">0.037</td>
<td style="text-align: center;">0.041</td>
<td style="text-align: center;">0.033</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>β</em><sub><em>M</em><em>O</em></sub></span></td>
<td style="text-align: center;">0.227</td>
<td style="text-align: center;">0.0102</td>
<td style="text-align: center;">22.19</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.220</td>
<td style="text-align: center;">0.228</td>
<td style="text-align: center;">0.230</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>β</em><sub><em>S</em><em>C</em></sub></span></td>
<td style="text-align: center;">0.166</td>
<td style="text-align: center;">0.0108</td>
<td style="text-align: center;">15.32</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.165</td>
<td style="text-align: center;">0.166</td>
<td style="text-align: center;">0.170</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>β</em><sub><em>U</em><em>A</em></sub></span></td>
<td style="text-align: center;">0.181</td>
<td style="text-align: center;">0.0098</td>
<td style="text-align: center;">18.37</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.181</td>
<td style="text-align: center;">0.180</td>
<td style="text-align: center;">0.184</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>β</em><sub><em>P</em><em>D</em></sub></span></td>
<td style="text-align: center;">0.482</td>
<td style="text-align: center;">0.0138</td>
<td style="text-align: center;">34.84</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.466</td>
<td style="text-align: center;">0.481</td>
<td style="text-align: center;">0.492</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>β</em><sub><em>A</em><em>D</em></sub></span></td>
<td style="text-align: center;">0.439</td>
<td style="text-align: center;">0.0132</td>
<td style="text-align: center;">33.13</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.434</td>
<td style="text-align: center;">0.446</td>
<td style="text-align: center;">0.447</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>L</em><sub>2</sub></span></td>
<td style="text-align: center;">0.139</td>
<td style="text-align: center;">0.0154</td>
<td style="text-align: center;">9.02</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.144</td>
<td style="text-align: center;">0.136</td>
<td style="text-align: center;">0.139</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>L</em><sub>3</sub></span></td>
<td style="text-align: center;">0.258</td>
<td style="text-align: center;">0.0158</td>
<td style="text-align: center;">16.34</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.262</td>
<td style="text-align: center;">0.258</td>
<td style="text-align: center;">0.254</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>L</em><sub>4</sub></span></td>
<td style="text-align: center;">0.788</td>
<td style="text-align: center;">0.0157</td>
<td style="text-align: center;">50.26</td>
<td style="text-align: center;">&lt; 0.0001</td>
<td style="text-align: center;">0.787</td>
<td style="text-align: center;">0.789</td>
<td style="text-align: center;">0.781</td>
</tr>
</tbody>
</table>

Standard errors of the coefficients were derived using the Rao-Wu bootstrap with 1000 replications \[50\]

*AD* anxiety/depression, *COVID* coronavirus disease, *cTTO* composite time trade-off, *MO* mobility, *PD* pain/discomfort, *SC* self-care, *UA* usual activities, $`\beta_{x}`$ coefficient for dimension $`x`$, $`L_{x}`$ coefficient for severity level $`x`$

</div>

<figure id="Fig4">
<p><img src="41669_2022_353_Fig4_HTML.jpg" id="MO4" /></p>
<p><img src="41669_2022_353_Fig4_HTML.gif" /></p>
<figcaption>Scatterplot of predicted (preferred model) and observed (cTTO) utility values for the 86 evaluated states.<br />
The diagonal is presented by the <em>red line</em> and indicates an equal predicted and observed utility values. <em>cTTO</em> composite time trade-off</figcaption>
</figure>

The results are robust to the choices made with respect to the sample. There is an average absolute difference of 0.004, 0.002 and 0.005 between the coefficients of the preferred model and those from, respectively, the full sample, the sample limited to pre-COVID interviews and the sample excluding flagged interviews. The largest deviation was observed in dimension PD. In all robustness checks, the preference ranking of the dimensions was identical.

To ensure that 1 year in full health (state 11111) is valued as 1 QALY in later applications of the value set, its utility value was standardized at 1. To generate utility values for other states in the value set, utility decrements are calculated for each combination of dimension and severity level, summed together with the intercept and subtracted from 1. For example, the utility value for health state 15342 is calculated as follows:

``` math
{Utility}\, 15342 = 1 - {({Intercept} + \beta}_{MO} \times 0 + \beta_{SC} \times 1 + \beta_{UA} \times L_{3} + \beta_{PD} \times L_{4} + \beta_{AD} \times L_{2}{) = 1 - {(0.038 + 0 + 0.166 + 0.047 + 0.380 + 0.061)} = 1 - 0.691 = 0.309}
```

The utility for the unconscious state was obtained directly from the survey and amounts to −0.454. The full value set can be downloaded in CSV format (see ESM7).

### Comparison Value Sets

Kernel density plots (Fig. <a href="#Fig5" data-ref-type="fig">5</a>) and a summary of key features (Table <a href="#Tab3" data-ref-type="table">3</a>) illustrate the discrepancy between the new Belgian EQ-5D-5L, the EQ-5D-3L and the crosswalk value sets. The EQ-5D-3L value set is characterized by two peaks (bimodal distribution). In the crosswalk set, roughly the same utility range is covered, but with a smoother transition between the peaks. In the EQ-5D-5L value set, the peak value is relatively similar, but the distribution of utility values has shifted to the right, i.e. higher valuation of mild states, and to the left, i.e. lower valuation of severe states and a higher share of negative values. The ranking of dimensions differs, although AD and PD still have the highest impact on HRQoL.

<figure id="Fig5">
<p><img src="41669_2022_353_Fig5_HTML.jpg" id="MO5" /></p>
<p><img src="41669_2022_353_Fig5_HTML.gif" /></p>
<figcaption>Kernel density plots of three Belgian EQ-5D value sets: the new EQ-5D-5L, and the current EQ-5D-3L and crosswalk value sets</figcaption>
</figure>

<div id="Tab3" class="table-wrap">

<div class="caption">

Comparison of key characteristics of the Belgian EQ-5D-5L and EQ-5D-3L value sets

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Preferred model</th>
<th style="text-align: left;">EQ-5D-3L value set</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">% health states valued worse than dead</td>
<td style="text-align: left;">15.0%</td>
<td style="text-align: left;">6.6%</td>
</tr>
<tr>
<td style="text-align: left;"><p>Preference ranking of dimensions</p>
<p>(ordered from highest to lowest utility loss at level 5)</p></td>
<td style="text-align: left;"><p>PD</p>
<p>AD</p>
<p>MO</p>
<p>UA</p>
<p>SC</p></td>
<td style="text-align: left;"><p>AD</p>
<p>PD</p>
<p>SC</p>
<p>MO</p>
<p>UA</p></td>
</tr>
<tr>
<td style="text-align: left;">Minimum value</td>
<td style="text-align: left;"><p>−0.532</p>
<p>(state 55555)</p></td>
<td style="text-align: left;"><p>−0.158</p>
<p>(state 33333)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Maximum value</p>
<p>(except full health)</p></td>
<td style="text-align: left;"><p>0.939</p>
<p>(state 12111)</p></td>
<td style="text-align: left;"><p>0.817</p>
<p>(state 11211)</p></td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *MO* mobility, *PD* pain/discomfort, *SC* self-care, *UA* usual activities

</div>

## Discussion

This paper reports on the development of the Belgian EQ-5D-5L value set based on preferences from the Belgian general public and produced following the most recent EQ-VT protocol and QC process to ensure high data quality. The preferred underlying model was the hybrid multiplicative eight-coefficient model with intercept for the cTTO data, random effects and correction for heteroskedasticity.

Given the high level of agreement between results from DCE-only and cTTO-only models, the choice for a hybrid model is justifiable as one can argue that the same value function underlies the responses in both valuations. A hybrid model maximizes the available data, increasing precision. It was preferred in ten out of 15 valuation studies using EQ-VT protocol 2.0 or 2.1 \[21, 22, 32–35, 41, 43, 44, 46–48, 51–53\].

A particular strength of this study was the representativeness of the sample. Although the EQ-VT protocol does not require representative sampling, this was deemed essential for the validity of the value set and its usability in health policy in the Belgian context where different language communities coexist (Dutch, French, German) and federal and regional governments share health competences. Respondents were randomly selected from the National Register using a multistage, stratified, cluster sampling with unequal probability design. Using comparative information from administrative sources and reference surveys, we concluded that the final sample was representative of the Belgian population in terms of age, sex, geographic spread, health status, HRQoL, education and employment status. Although representativeness in these fields does not necessarily imply representativeness in terms of health preferences, it at least reduces the possible impact of lack of representativeness on these factors on the utility values obtained. The stringent sample selection procedure in combination with the QC process led to an extended data collection period. This was, however, not considered problematic as it makes the collected utility values less prone to time specific effects \[35\].

Great effort was also put into the model selection process. Given the nature of the value set where utility values are predicted for 3125 health states based on a limited number of observed states, the criterion of predictive accuracy was considered highly relevant. It was a main argument to prefer the multiplicative eight-parameter model.

The new value set is based on a robust and valid method and provides up-to-date utilities, proper to the EQ-5D-5L instrument. There are several major methodological improvements compared to the EQ-5D-3L and crosswalk value sets. \[12\]. First, the five-level version improved the discriminatory power and sensitivity of the earlier three-level version \[7\]. Second, a clear protocol and QC process improved the quality, consistency and accurateness of the valuation data \[14, 15\]. Third, in comparison with the VAS used for the EQ-5D-3L, cTTO and DCE are more robust valuation techniques for utility measurement, embedded in economic random utility theory. Fourth, face-to-face interviews in a one-to-one setting were conducted instead of postal surveys, which is more appropriate given the cognitive challenging nature of the cTTO task \[15, 20\]. Fifth, for the EQ-5D-3L value set, the sample was geographically limited to one Belgian region, while preferences for the new value set were surveyed from a sample of the entire adult Belgian population. Such extension was desirable since the value set is used for national decision making.

For these reasons, we recommend the use of the EQ-5D-5L instrument in combination with the newly developed value set. Inevitably, this will generate different results than the previous value set. First, the EQ-5D-5L value set has a higher fraction of health states valued worse than dead (15.0% in 5L vs 6.6% in 3L) and covers a larger range of utility values than the EQ-5D-3L set (−0.532 to 0.939 in 5L and −0.158 to 0.817 in 3L, excluding state 11111). The higher valuation of mild health states reflects the very limited willingness to trade off life years to avoid mild health problems that was observed among survey respondents. A wider range of utility values allows for a better discrimination between patients, both for mild and (very) severe health conditions, which improves the applicability of the EQ-5D instrument. Also, a low HRQoL value (−0.454, only five EQ-5D-5L states in the new value set are valued lower) was derived directly from survey responses for the state of unconsciousness (coma). This state cannot be described by the EQ-5D system, but might nevertheless be important in some assessments (e.g. of interventions where patients are or go into coma). Second, the preference ranking of the dimensions has altered. In the 3L value set, the AD dimension is associated with the highest utility loss, followed by PD, SC, MO and UA. In the 5L value set, the dimension PD is associated with the highest loss in HRQoL, closely followed by AD and then MO, UA and SC. Pain and discomfort is also the dimension for which most respondents reported problems regarding their own health. It is expected that policy priorities and resource allocation decisions will reflect the importance attached to pain relief and mental health.

One limitation of the study was that our sample did not reach the targeted 1000 respondents. The COVID-19 pandemic was one reason, but in general, it proved difficult to find sufficient individuals willing to participate, with only a short list of randomly selected, geographically dispersed potential candidates at our disposal. Sampling in fewer locations or from a market research panel would have been faster and less resource intensive, but would come at a cost of reduced representativeness. However, given that the target of 1000 respondents was set to have sufficient power to estimate a 20-parameter additive model, it can be argued that our smaller sample still has sufficient power to accurately estimate a more parsimonious model. A second limitation was that more interviewers worked in the field than put forward in the protocol, this because of replacements and drop-outs. Although there is evidence to support the face validity of the collected data, it seems that part of the variability in the data, and in particular in health states valued worse than dead in the cTTO task, can be attributed to differences between interviewers. However, the random effects included in the model allow for individual variation in the valuation and can (at least partly) absorb such interviewer-specific effects.

A final concern was an incorrect labelling of severity level 2 in the MO dimension in the Dutch version of the EQ-VT software. The impact of this was expected to be limited because interviewers were provided a correctly labelled printed overview to help respondents locate the health state described on the screen. Moreover, the data analysis did not reveal any unexpected pattern in valuation scores in the MO dimension.

## Conclusion

This study established an EQ-5D-5L value set, based on the preferences of a random sample of the Belgian general public in 2018–2020. The EQ-5D-5L value set should replace the currently used EQ-5D-3L value set from 2003. Instead of describing and valuing 243 health states, the current value set values 3125 health states. The value set provides opportunities for future clinical and economic evaluations in healthcare, for the measurement of patient-reported outcomes and for population health assessments.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (PDF 1157 kb)

</div>

<div class="caption">

Supplementary file2 (CSV 125 kb)

</div>

## Acknowledgements

The authors are grateful for the work of Profacts, the interviewers and the EuroQol Research Foundation for support provided throughout the conduct of the study.

## Declarations

### Funding

This research was co-funded by the Belgian Health Care Knowledge Centre (KCE) and the EuroQol Research Foundation (EQ Project 20170490 and 20170491). The KCE is a federal institution that is financed by the National Institute for Health and Disability Insurance (NIHDI, RIZIV – INAMI), the Federal Public Service of health, food chain safety and environment, and the Federal Public Service of social security. The development of health services research studies is part of the legal mission of the KCE. Although the development of the studies is paid by the KCE budget, the sole mission of the KCE is providing scientifically valid information.

### Conflict of interest

Nicolas Bouckaert, Irina Cleemput, Stephan Devriese and Sophie Gerkens declare that they have no conflicts of interest directly relevant to the content of this article.

### Ethics approval

The study received approval from the ethics committee of the university hospital of Ghent (B670201835610) and was conducted in accordance with the Declaration of Helsinki.

### Consent to participate

Informed consent was obtained from all individual participants included in the study. Participants were informed about their freedom of refusal. Anonymity and confidentiality were maintained throughout the research process.

### Consent for publication

The study participants consented to the collection, storage and analysis of their data and the publication of anonymous final results.

### Data sharing

Anonymous datasets generated during and/or analysed during the current study are available from the corresponding author on reasonable request. Requests for personal data at the individual level will be judged case by case to assure compliance with informed consent clauses on confidentiality of personal data as approved by the ethics committee.

### Code availability

Code for data cleaning and analysis are available from the corresponding author on reasonable request.

### Author contributions

All authors contributed to the study conception and design. SD was responsible for the sampling design. SG and IC supervised the data collection and quality control process. NB was responsible for the data analysis. The first draft of the manuscript was written by NB and SG. All authors played a role in the review of the analysis, the interpretation of the results and the review and editing of the final version of the manuscript.

## References

## References

1. Thiry N, Neyt M, Van De Sande S, Cleemput I. Belgian guidelines for economic evaluations: second edition. Int J Technol Assess Health Care. 2014;30(6):601–607. doi: 10.1017/s0266462314000725.

2. Royal Decree laying down the procedures, periods and conditions regarding the reimbursement of the costs of pharmaceutical specialities by the compulsory health and disability insurance. Belgian official journal 1 February 2018.

3. Kennedy-Martin M, Slaap B, Herdman M, van Reenen M, Kennedy-Martin T, Greiner W, et al. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020;21(8):1245–1257. doi: 10.1007/s10198-020-01195-8.

4. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L) Qual Life Res. 2011;20(10):1727–1736. doi: 10.1007/s11136-011-9903-x.

5. Janssen MF, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, et al. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi: 10.1007/s11136-012-0322-4.

6. Pickard AS, De Leon MC, Kohlmann T, Cella D, Rosenbloom S. Psychometric comparison of the standard EQ-5D to a 5 level version in cancer patients. Med Care. 2007;45(3):259–263. doi: 10.1097/01.mlr.0000254515.63841.81.

7. Janssen MF, Bonsel GJ, Luo N. Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. 2018;36(6):675–697. doi: 10.1007/s40273-018-0623-8.

8. Feng Y, Devlin N, Herdman M. Assessing the health of the general population in England: how do the three- and five-level versions of EQ-5D compare? Health Qual Life Outcomes. 2015;13(1):171. doi: 10.1186/s12955-015-0356-8.

9. Whitehead SJ, Ali S. Health outcomes in economic evaluation: the QALY and utilities. Br Med Bull. 2010;96(1):5–21. doi: 10.1093/bmb/ldq033.

10. Brazier J, Ratcliffe J, Salomon JA, Tsuchiya A. Measuring and valuing health benefits for economic evaluation. 2. Oxford: Oxford University Press; 2017.

11. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi: 10.1007/s40273-016-0404-1.

12. Cleemput I. A social preference valuations set for EQ-5D health states in Flanders, Belgium. Eur J Health Econ. 2010;11(2):205–213. doi: 10.1007/s10198-009-0167-0.

13. van Hout B, Janssen MF, Feng Y-S, Kohlmann T, Busschbach J, Golicki D, et al. Interim scoring for the EQ-5D-5L: mapping the EQ-5D-5L to EQ-5D-3L value sets. Value in Health. 2012;15(5):708–715. doi: 10.1016/j.jval.2012.02.008.

14. Oppe M, Devlin NJ, van Hout B, Krabbe PF, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17(4):445–453. doi: 10.1016/j.jval.2014.04.002.

15. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goñi JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation work: version 2 of the EQ-5D-5L valuation protocol. Value Health. 2019;22(1):23–30. doi: 10.1016/j.jval.2018.05.010.

16. Xie F, Pickard AS, Krabbe PFM, Revicki D, Viney R, Devlin N, et al. A checklist for reporting valuation studies of multi-attribute utility-based instruments (CREATE) Pharmacoeconomics. 2015;33(8):867–877. doi: 10.1007/s40273-015-0292-9.

17. Oppe M, van Hout B. The, “power” of eliciting EQ-5D-5L values: the experimental design of the EQ-VT. Rotterdam: EuroQol Group; 2017.

18. Demarest S, Van der Heyden J, Charafeddine R, Drieskens S, Gisle L, Tafforeau J. Methodological basics and evolution of the Belgian health interview survey 1997–2008. Arch Public Health. 2013;71(1):24. doi: 10.1186/0778-7367-71-24.

19. Janssen BMF, Oppe M, Versteegh MM, Stolk EA. Introducing the composite time trade-off: a test of feasibility and face validity. Eur J Health Econ. 2013;14(1):5–13. doi: 10.1007/s10198-013-0503-2.

20. Shah KK, Lloyd A, Oppe M, Devlin NJ. One-to-one versus group setting for conducting computer-assisted TTO studies: findings from pilot studies in England and the Netherlands. Eur J Health Econ. 2013;14(1):65–73. doi: 10.1007/s10198-013-0509-9.

21. Jensen CE, Sørensen SS, Gudex C, Jensen MB, Pedersen KM, Ehlers LH. The Danish EQ-5D-5L value set: a hybrid model using cTTO and DCE data. Appl Health Econ Health Policy. 2021;19(4):579–591. doi: 10.1007/s40258-021-00639-3.

22. Golicki D, Jakubczyk M, Graczyk K, Niewada M. Valuation of EQ-5D-5L health states in Poland: the first EQ-VT-based study in central and eastern Europe. Pharmacoeconomics. 2019;37(9):1165–1176. doi: 10.1007/s40273-019-00811-7.

23. Ramos-Goñi JM, Pinto-Prades JL, Oppe M, Cabases JM, Serrano-Aguilar P, Rivero-Arias O. Valuation and modeling of EQ-5D-5L health states using a hybrid approach. Med Care. 2017;55(7):e51–e58. doi: 10.1097/MLR.0000000000000283.

24. van Hout B, Mulhern B, Feng Y, Shah K, Devlin N. The EQ-5D-5L value set for England: response to the "Quality Assurance". Value Health. 2020;23(5):649–655. doi: 10.1016/j.jval.2019.10.013.

25. Devlin NJ, Brooks R. EQ-5D and the EuroQol Group: past, present and future. Appl Health Econ Health Policy. 2017;15(2):127–137. doi: 10.1007/s40258-017-0310-5.

26. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–473. doi: 10.1016/j.jval.2016.10.012.

27. Devlin NJ, Shah KK, Feng Y, Mulhern B, van Hout B. Valuing health-related quality of life: an EQ-5D-5L value set for England. Health Econ. 2018;27(1):7–22. doi: 10.1002/hec.3564.

28. Versteegh MM, Vermeulen KM, Evers SMAA, de Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi: 10.1016/j.jval.2016.01.003.

29. Xie F, Pullenayegum E, Gaebel K, Bansback N, Bryan S, Ohinmaa A, et al. A time trade-off-derived value set of the EQ-5D-5L for Canada. Med Care. 2016;54(1):98–105. doi: 10.1097/MLR.0000000000000447.

30. Augustovski F, Rey-Ares L, Irazola V, Garay OU, Gianneo O, Fernandez G, et al. An EQ-5D-5L value set based on Uruguayan population preferences. Qual Life Res. 2016;25(2):323–333. doi: 10.1007/s11136-015-1086-4.

31. Kim S-H, Ahn J, Ock M, Shin S, Park J, Luo N, et al. The EQ-5D-5L valuation study in Korea. Qual Life Res. 2016;25(7):1845–1852. doi: 10.1007/s11136-015-1205-2.

32. Ferreira PL, Antunes P, Ferreira LN, Pereira LN, Ramos-Goñi JM. A hybrid modelling approach for eliciting health state preferences: the Portuguese EQ-5D-5L value set. Qual Life Res. 2019;28(12):3163–3175. doi: 10.1007/s11136-019-02226-5.

33. Andrade LF, Ludwig K, Ramos-Goñi JM, Oppe M, de Pouvourville G. A French value set for the EQ-5D-5L. Pharmacoeconomics. 2020;38(4):413–425. doi: 10.1007/s40273-019-00876-4.

34. Ludwig K, Graf von der Schulenburg JM, Greiner W. German value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(6):663–674. doi: 10.1007/s40273-018-0615-8.

35. Hobbins A, Barry L, Kelleher D, Shah K, Devlin N, Ramos-Goñi JM, et al. Utility values for health states in Ireland: a value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36(11):1345–1353. doi: 10.1007/s40273-018-0690-x.

36. Ramos-Goñi JM, Craig B, Oppe M, van Hout B. Combining continuous and dichotomous responses in a hybrid model. Rotterdam: EuroQol Research Foundation; 2016.

37. Rand-Hendriksen K, Ramos-Goñi JM, Augestad LA, Luo N. Less is more: cross-validation testing of simplified nonlinear regression model specifications for EQ-5D-5L health state values. Value Health. 2017;20(7):945–952. doi: 10.1016/j.jval.2017.03.013.

38. Luo N, Liu G, Li M, Guan H, Jin X, Rand-Hendriksen K. Estimating an EQ-5D-5L value set for China. Value Health. 2017;20(4):662–669. doi: 10.1016/j.jval.2016.11.016.

39. Feng Y, Devlin N, Shah K, Mulhern B, van Hout B. New methods for modelling EQ-5D-5L value sets: an application to English data. London: Office of Health Economics; 2016. doi:10.1002/hec.3560

40. Oppe M, Ramos-Goñi JM, van Hout B. Modeling EQ-5D-5L valuation data. In: Busschbach JJ, editor. 29th Scientific Plenary Meeting of the EuroQol Group. Rotterdam; 2012. pp. 61–91.

41. Purba FD, Hunfeld JAM, Iskandarsyah A, Fitriana TS, Sadarjoen SS, Ramos-Goñi JM, et al. The Indonesian EQ-5D-5L value set. Pharmacoeconomics. 2017 doi: 10.1007/s40273-017-0538-9.

42. Shiroiwa T, Ikeda S, Noto S, Igarashi A, Fukuda T, Saito S, et al. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19(5):648–654. doi: 10.1016/j.jval.2016.03.1834.

43. Lin H-W, Li C-I, Lin F-J, Chang J-Y, Gau C-S, Luo N, et al. Valuation of the EQ-5D-5L in Taiwan. PLoS ONE. 2018;13(12):e0209344. doi: 10.1371/journal.pone.0209344.

44. Rencz F, Brodszky V, Gulácsi L, Golicki D, Ruzsa G, Pickard AS, et al. Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time trade-off in Hungary. Value Health. 2020;23(9):1235–1245. doi: 10.1016/j.jval.2020.03.019.

45. Pattanaphesaj J, Thavorncharoensap M, Ramos-Goñi JM, Tongsiri S, Ingsrisawang L, Teerawattananon Y. The EQ-5D-5L valuation study in Thailand. Expert Rev Pharmacoecon Outcomes Res. 2018;18(5):551–558. doi: 10.1080/14737167.2018.1494574.

46. Mai VQ, Sun S, Minh HV, Luo N, Giang KB, Lindholm L, et al. An EQ-5D-5L Value Set for Vietnam. Qual Life Res. 2020;29(7):1923–1933. doi: 10.1007/s11136-020-02469-7.

47. Al Shabasy S, Abbassi M, Finch A, Roudijk B, Baines D, Farid S. The EQ-5D-5L valuation study in Egypt. Pharmacoeconomics. 2021 doi: 10.1007/s40273-021-01100-y.

48. Shafie AA, Vasan Thakumar A, Lim CJ, Luo N, Rand-Hendriksen K, Md Yusof FA. EQ-5D-5L valuation for the Malaysian population. Pharmacoeconomics. 2019;37(5):715–725. doi: 10.1007/s40273-018-0758-7.

49. SAS Institute Inc . SAS/STAT®14.1 user’s guide: the NLMIXED procedure. Cary: SAS Institute Inc.; 2015.

50. Heeringa SG, West BT, Berglund PA. Applied survey data analysis. 2. Boca Raton: Chapman and Hall; 2017.

51. Augustovski F, Belizán M, Gibbons L, Reyes N, Stolk E, Craig BM, et al. Peruvian Valuation of the EQ-5D-5L: a direct comparison of time trade-off and discrete choice experiments. Value Health. 2020;23(7):880–888. doi: 10.1016/j.jval.2020.05.004.

52. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F, et al. United States valuation of EQ-5D-5L health states using an international protocol. Value in Health. 2019;22(8):931–941. doi: 10.1016/j.jval.2019.02.009.

53. Gutierrez-Delgado C, Galindo-Suárez R-M, Cruz-Santiago C, Shah K, Papadimitropoulos M, Feng Y, et al. EQ-5D-5L health-state values for the Mexican population. Appl Health Econ Health Policy. 2021;19(6):905–914. doi: 10.1007/s40258-021-00658-0.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (PDF 1157 kb)

</div>

<div class="caption">

Supplementary file2 (CSV 125 kb)

</div>

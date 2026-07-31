---
project_id: "2015240"
work_id: "doi:10.1007/s40273-019-00811-7"
doi: "10.1007/s40273-019-00811-7"
pmid: "31161586"
pmcid: "PMC6830402"
title: "Valuation of EQ-5D-5L Health States in Poland: the First EQ-VT-Based Study in Central and Eastern Europe"
journal: "Pharmacoeconomics"
publication_date: "2019-06-03"
volume: "37"
issue: "9"
authors:
  - name: "Dominik Golicki"
    affiliation_ids:
      - "Aff1"
      - "Aff3"
  - name: "Michał Jakubczyk"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Katarzyna Graczyk"
    affiliation_ids:
      - "Aff3"
  - name: "Maciej Niewada"
    affiliation_ids:
      - "Aff1"
      - "Aff3"
affiliations:
  - id: "Aff1"
    name: "Department of Experimental and Clinical Pharmacology, Medical University of Warsaw, Banacha 1b St., 02-097 Warsaw, Poland"
  - id: "Aff2"
    name: "Decision Analysis and Support Unit, SGH Warsaw School of Economics, Al. Niepodległości 162, 02-554 Warsaw, Poland"
  - id: "Aff3"
    name: "HealthQuest Spółka z ograniczoną odpowiedzialnością Sp. k., 63 Mickiewicza Street, Megadex A Building, 01-625 Warsaw, Poland"
licence: "cc-by-nc"
source_file: "input/projects/2015240/papers/doi_10.1007_s40273-019-00811-7.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6830402/fullTextXML"
source_method: "epmc_xml"
source_sha256: "e0549ab03230d104ea917821dda53decf99e39b40f8c8871274f50943e438206"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Valuation of EQ-5D-5L Health States in Poland: the First EQ-VT-Based Study in Central and Eastern Europe

## Abstract

### Objective

Cost-utility analyses are becoming increasingly important in Central and Eastern Europe. We aimed to develop a Polish utility tariff for EQ-5D-5L health states.

### Methods

Face-to-face, computer-assisted interviews were collected in a representative sample. Each respondent followed a standardised protocol to collect ten composite time trade-off and seven discrete choice experiment observations. In the Bayesian approach, several model specifications were compared based on model fit, the usability of the final value set and how they reflect the elicitation procedure (e.g. censoring). A hybrid approach (using composite time trade-off and discrete choice experiment data) was employed in the final set, which was compared with the existing ones: EQ-5D-3L and EQ-5D-5L cross-walk.

### Results

Data from 1252 respondents (11,480 composite time trade-off valuations and 8764 discrete choice experiment pairs) were collected over the period June to October 2016. The final model accounted for random parameters, error scaling with fat tails, censoring at − 1, unwillingness to trade in time trade-off by the religious people and Cauchy distribution in discrete choice experiments. Pain/discomfort impacts the utility most: the disutility equals 0.575 when at level 5. In the value set, 4.4% of EQ-5D-5L states are worse than dead. The new value set has a comparable range (minimum of − 0.590 compared to − 0.523) and the same ordering of the first three dimensions (pain/discomfort, mobility, self-care) as the EQ-5D-3L value set and the EQ-5D-5L cross-walk value set. Moreover, it is more sensitive to a moderate decline in health.

### Conclusions

The new value set supports consistency with past decisions in cost-utility studies, while offering a better assessment of even moderate improvements in health. It could represent an option for Central and Eastern Europe countries lacking their own value sets.

### Electronic supplementary material

The online version of this article (10.1007/s40273-019-00811-7) contains supplementary material, which is available to authorized users.

Issue date 2019.

## Key Points For Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| The EQ-5D-5L value set was developed based on directly measured health preferences of a representative sample of Polish society |
| It should provide a substitute for a mapping-based cross-walk value set when calculating quality-adjusted life-years based on EQ-5D-5L results in Poland |
| Researchers from Central and Eastern European countries may consider it as an option when national health preferences data are lacking |
| The new value set provides ground for consistency with past decisions in cost-utility analyses while being sensitive even to moderate health improvements |

</div>

## Introduction

Health technology assessment is developing rapidly in Central and Eastern Europe (CEE): e.g. in Bulgaria, Czechia, Hungary and Croatia \[1–4\]. In Poland, it is compulsory when applying for drug reimbursement \[5\]. The Polish Health Technology Assessment Agency (AOTMiT) has issued approximately 1800 recommendations since its foundation in 2006, and has assessed nearly 500 health technology assessment reports since the introduction of the current Reimbursement Act in 2012 \[6\]. Based on this regulation, cost utility is the preferred form of pharmacoeconomic analysis with the official threshold for the cost per quality-adjusted life-year updated yearly \[7\]. AOTMiT recommends EQ-5D for the purposes of valuing health states and calculating quality-adjusted life-years \[8\].

The EQ-5D questionnaire consists of a descriptive system and a visual analog scale \[9\]. The descriptive system contains five dimensions: mobility (MO), self-care (SC), usual activities (UA), pain/discomfort (PD) and anxiety/depression (AD). In the original version (EQ-5D-3L), each dimension has three levels: *no*, *some* or *severe* problems; whereas there are five levels in the new version (EQ-5D-5L): *no*, *slight*, *moderate*, *severe* or *extreme* problems \[10, 11\]. The previous two mentioned questionnaires define 243 and 3125 health states, respectively. By attaching disutility to each of the levels in each dimension, it is possible to calculate a single value (EQ-Index) for every health state, forming a value set \[12\]. EQ-5D-5L demonstrates better measurement properties than EQ-5D-3L \[13, 14\].

There are only two published EQ-5D-3L value sets in CEE countries: Slovenian \[15\] and Polish \[16\], and no value set for EQ-5D-5L. Although it has been possible to use EQ-5D-5L in Poland \[17–20\], using the mapping-based cross-walk value set \[21, 22\], the lack of a directly measured EQ-5D-5L value set limited the implementation within the decision-making process.

Our objective was to derive a Polish tariff for the EQ-5D-5L descriptive system, using a standardised approach developed by the EuroQol Group. Such a value set could also be used by other CEE countries that are too small to finance valuation studies, yet are culturally similar and are likely to have congruent health preferences.

## Methods

The methods and analyses reported in this paper comply with the CREATE guidelines for reporting valuation studies of multi-attribute utility-based instruments \[23\].

### Study Design

Quota-based sampling was applied using Polish census data from November 2014, based on personal identification number registry (PESEL) and Central Statistical Office data on education \[24\]. A representative sample in terms of age, sex, education, geographical region and the size of the locality was obtained from Polish residents aged 18+ years. Individuals were recruited through a mixed strategy (public locations, personal contact). Interviews were conducted in public venues or at participants’ homes. Respondents received a financial incentive (voucher of value equivalent to €8).

The study design followed a valuation protocol: EuroQol Valuation Technology (EQ-VT 2.0). It includes software for conducting computer-assisted personal interviews, an interviewer script, standardised training materials, data quality-control procedures and an Excel-based quality-control tool enabling monitoring of protocol compliance, interviewer effects and the validity of the collected data \[25\].

### Valuation Interview

Computer-assisted personal interviews consisted of four main parts: introduction, composite time trade-off (TTO) valuation, discrete choice experiment (DCE) valuation and country-specific background questions. After a general introduction and explanation of the purpose of the study, the respondents self-reported their health using the EQ-5D-5L questionnaire and answered basic background questions (about age, sex and experiences of severe illness).

In the composite time trade-off valuation, a composite approach was used: starting with the standard TTO (to find the number of years in full health equivalent to 10 years in an impaired EQ-5D-5L state) and shifting to a ‘lead time’ TTO when participants considered the state to be *worse than dead* (see detailed descriptions \[26–29\]). The resulting TTO values range from − 1 to 1 in 0.05 increments (the smallest tradable unit being 6 months in duration).

The TTO part of the interview consisted of an explanation of the TTO procedure (the ‘being in a wheelchair’ example and three practice states: mild, severe and difficult to imagine), proper TTO valuation of ten EQ-5D-5L health states, a structured TTO debriefing and the TTO feedback module. Each respondent was presented with the rank ordering of health states derived from previous responses, to indicate states for which they were not happy with the ranking (though there was no possibility of re-evaluation).

The TTO experimental design included 86 EQ-5D-5L health states distributed into ten blocks that were balanced in terms of severity of states. The health states used in EQ-VT 2.0 were selected using a Monte Carlo simulation \[30\]. Each block included one of five very mild states (only one dimension at level 2 and all others at 1), the most severe state (‘55555’) and eight intermediate states. Respondents were randomised into one of the ten blocks; the health states were presented in a random order.

In the DCE valuation task, participants were presented with a pair of EQ-5D-5L health states with no duration specified (labelled A and B) and asked to indicate which they consider ‘better’ \[30–32\]. This part of the interview consisted of instructions regarding the task, the valuation of seven pairs and a structured debriefing.

The DCE experimental design included 196 pairs of states randomly divided into 28 blocks, which were identified using an efficient Bayesian design. The blocks were similar in terms of severity, assessed by the sum of the level scores of the health states (i.e. the misery index). Participants were randomly assigned to one of the blocks. The question order and left-right positioning of states were randomised.

The set of Polish country-specific questions covered: priorities in TTO valuations (length or quality of life), general health using an SF-1 question from the SF-36 questionnaire \[33\], comorbidities, potential concerns during severe illness, religiosity and beliefs, relationship status, childcare responsibilities, professional status and financial situation. In accordance with the EQ-VT protocol, the minimal recommended sample size for EQ-5D-5L valuation studies is *N* = 1000 (see the detailed description \[30\]). Given a planned experimental arm of our research, we established the basic target sample size at *N* = 1250 (the methods and results of the experimental substudy will be reported elsewhere).

### Quality Control and Data Analysis

We excluded (1) interviews of suspicious quality (‘flagged’ interviews; for a detailed description of quality-control procedures see Electronic Supplementary Material \[ESM\] 1), (2) the first ten interviews conducted by an interviewer not meeting the minimum quality criteria (at least seven unflagged interviews) and (3) individual TTO valuations when marked by the respondent in the Feedback Module as not adequately representing their health preferences. No individual DCE valuations were excluded. Descriptive statistics were used to summarise the respondent’s characteristics and responses to the TTO and DCE tasks.

### Modelling

#### General Approach

Below, we present the general approach (dependent/independent variables, model-selection criteria, estimation technique and the building blocks of the model specification under consideration). The formal specification is presented in ESM 1, Online Resource 2.

We based the final model on data from both elicitation techniques (often referred to as a hybrid approach). In the recent literature, all three approaches are used: TTO only \[34\], DCE only \[35\] or both \[36–39\]. As it remains unknown if one clearly outperforms the other, we deemed it safest to have both of them impact the value set (which necessarily worsens the model fit). Therefore, there are two dependent variables: the reported utility of a state (for TTO) and the choice made from a pair of states (for DCE). The states’ dimensions are taken as independent variables. In the process of constructing the final model, several specifications were tested: the choices were based on statistical criteria, pragmatic reasons (what the estimation results are used for) or our beliefs concerning how the elicitation tasks work.

In the estimation process, we used a Bayesian approach \[40\], as we find it more intuitive and flexible to work with a code (JAGS model run from within R, the code in ESM 2) directly describing the data generation process. To let the data speak, we used non-informative priors. In the estimation, we used a Markov-chain Monte Carlo simulation with, respectively, 2000, 30,000 and 20,000 adaptive, burn-in and actual iterations (2000, 20,000 and 10,000 for the intermediate models), no thinning and four chains. The medians of posterior distributions were used as point estimates, and 2.5 and 97.5 percentiles to construct 95% credible intervals. The model fit was assessed based on deviance and penalised deviance (deviance information criterion \[DIC\]). Potential scale reduction factors were monitored to diagnose convergence for individual parameters \[41\].

We only used main effects, i.e. no interactions between dimensions. This was a pragmatic decision, undertaken to ensure the final model may also be useful when only partial information is available (e.g. marginal distributions of levels for each dimension separately) \[42\]; for similar reasons, models with no constant term were preferred (also supported by results).

We tested (and utilised in the final model) the random parameters approach: the disutilities of dimensions/levels differ between individuals. Not only do we find this assumption intuitive but in addition the usefulness of random parameters (and the choice of specific distribution) was confirmed by DIC. Nevertheless, to limit random noise and the number of parameters, and also to avoid technical assumptions (the logical ordering of levels), we assumed it is the importance of each dimension (the disutility of level 5) that is distinctive for each individual, while the relative importance of each level is fixed across individuals (somewhat resembling the idea of simplifying how relative level importance is modelled \[43\]).

It is not possible in TTO to report a utility lower than − 1. Hence, we tested (and used in the final model) censoring: the observed −1s are treated as ≤−1. Some authors use censoring at 0 (where TTO is changed for lead time TTO) or at 1 (in TTO, a value greater than 1 cannot be reported) \[38\], which we find unconvincing. Regarding censoring at 0, negative values are possible in the protocol used, and modelling an endogenous self-censoring process would require assumptions (is a given zero the true utility or the effect of censoring?). Being unable to decide if a state is worse than dead is not equivalent to being unable to report \<0 utility. Regarding censoring at 1, values above 1 are impossible, not only owing to the protocol but also because of the logical construction of the descriptive system and how the utility values were normalised.

Typically (and in our dataset), there is more variability in responses to more severe states (with lower utility, on average). This may be explained by the random parameters approach, as used in the present paper. Nonetheless, we find it plausible that for a given individual (the importance of dimensions known) there is an additional error term in TTO responses, and that this error tends to be larger for more severe health states (intuitively, for a state whose true utility for a given individual is close to 1, there is little room for a larger error). Therefore, we assumed that the scale parameter of the distribution increases with the theoretical disutility. Specifically, we used a generalised t-Student distribution with the scale and the number of degrees of freedom treated as parameters, allowing for fat tails (but also having a normal distribution as an asymptote).

In the DCE part, we assumed the probability of one state being chosen is a function of the difference in utilities, as is typically done. In the standard approach, this dependence is given by the cumulative distribution function of the logit distribution. Instead, based on the previous findings \[44\] and the DIC, we used the Cauchy distribution.

Previous research suggests that people with religious beliefs may misrepresent their preferences in TTO tasks, owing to an unwillingness to trade life-years—interpreted as a reporting bias, rather than a difference in preference \[45\]. For this reason, we introduced a parameter that scaled down the disutilities for religious respondents (separately for TTO and DCE), to disentangle the underlying and the reported preferences. In the final model, the scaling was not found in the DCE part, confirming the above interpretation.

#### Intermediate Models

We constructed several models sequentially, introducing additional building blocks in succession, and controlling for the DIC improvement, potential scale reduction factors and for whether the 95% credible interval contained a neutral value (i.e. a form of statistical significance). In this paper, we present the results of some of the intermediate steps (all based solely on TTO data):

- M1—panel random-effects approach, with heteroscedasticity-robust standard errors;

- M2—fixed parameters Bayesian model, with no constant term;

- M3—random parameters Bayesian model;

- M4—as M3, with error depending on the theoretical disutility via a t-Student distribution;

- M5—as M4, with scaling as a result of religiosity.

We decided not to present the intermediate steps of the DCE-only part, as the parameters would require some anchoring (for more details on this issue, see \[46\]). However, as in the DCE part, we monitored the impact of modelling assumptions on DIC.

### Value Set Comparison

There are three EQ-5D value sets available for Poland: EQ-5D-3L \[16\], EQ-5D-5L mapping-based cross-walk \[22\] and the present, directly measured EQ-5D-5L value set. To compare the utility values, we used three methods. First, we estimated the kernel density function of the utility values. Second, we identified the median and the worst levels between the EQ-5D-3L and EQ-5D-5L systems and we presented the utilities for all states. In the ESM 1, Online Resource 6, we additionally present the scatter plot to illustrate the relationship between the EQ-5D-5L value set and the other value sets.

## Results

### Sample Characteristics

From June to October 2016, 15 interviewers conducted 1570 interviews. The mean interview time was 41.1 minutes. In total, 2.3% of interviews were flagged. After excluding interviews with experimental TTO blocks (the results of the study will be reported elsewhere), 29 flagged interviews and six interviews that failed to meet the minimum quality criteria, data from 1252 respondents (52.5% female) aged 18–91 years (mean 46.2; standard deviation 17.6) were available (Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

General characteristics of respondents

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Characteristics</th>
<th colspan="2" style="text-align: left;">Study sample<br />
(<em>N</em> = 1252)</th>
<th style="text-align: left;">Polish general adult population (30.7 million) [<span class="citation" data-cites="CR19">19</span>, <span class="citation" data-cites="CR23">23</span>]</th>
</tr>
<tr>
<th style="text-align: left;"><em>N</em></th>
<th style="text-align: left;">%</th>
<th style="text-align: left;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Age group (years)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> 18–34</td>
<td style="text-align: left;">378</td>
<td style="text-align: left;">30.2</td>
<td style="text-align: left;">30.2</td>
</tr>
<tr>
<td style="text-align: left;"> 35–49</td>
<td style="text-align: left;">313</td>
<td style="text-align: left;">25.0</td>
<td style="text-align: left;">25.1</td>
</tr>
<tr>
<td style="text-align: left;"> 50–64</td>
<td style="text-align: left;">332</td>
<td style="text-align: left;">26.5</td>
<td style="text-align: left;">25.6</td>
</tr>
<tr>
<td style="text-align: left;"> 65+</td>
<td style="text-align: left;">229</td>
<td style="text-align: left;">18.3</td>
<td style="text-align: left;">19.2</td>
</tr>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td style="text-align: left;">657</td>
<td style="text-align: left;">52.5</td>
<td style="text-align: left;">52.6</td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td style="text-align: left;">595</td>
<td style="text-align: left;">47.5</td>
<td style="text-align: left;">47.4</td>
</tr>
<tr>
<td style="text-align: left;">Size of place of residence</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Rural area</td>
<td style="text-align: left;">501</td>
<td style="text-align: left;">40.1</td>
<td style="text-align: left;">39.5</td>
</tr>
<tr>
<td style="text-align: left;"> Town of less than 100,000 inhabitants</td>
<td style="text-align: left;">404</td>
<td style="text-align: left;">32.3</td>
<td style="text-align: left;">32.9</td>
</tr>
<tr>
<td style="text-align: left;"> City of 100,000 and more inhabitants</td>
<td style="text-align: left;">345</td>
<td style="text-align: left;">27.6</td>
<td style="text-align: left;">27.6</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Geographical location of residence (macro-region)</td>
</tr>
<tr>
<td style="text-align: left;"> Central</td>
<td style="text-align: left;">242</td>
<td style="text-align: left;">19.4</td>
<td style="text-align: left;">20.3</td>
</tr>
<tr>
<td style="text-align: left;"> Southwest</td>
<td style="text-align: left;">136</td>
<td style="text-align: left;">10.9</td>
<td style="text-align: left;">10.3</td>
</tr>
<tr>
<td style="text-align: left;"> South</td>
<td style="text-align: left;">245</td>
<td style="text-align: left;">19.6</td>
<td style="text-align: left;">20.6</td>
</tr>
<tr>
<td style="text-align: left;"> Northwest</td>
<td style="text-align: left;">199</td>
<td style="text-align: left;">15.9</td>
<td style="text-align: left;">16.0</td>
</tr>
<tr>
<td style="text-align: left;"> North</td>
<td style="text-align: left;">187</td>
<td style="text-align: left;">15.0</td>
<td style="text-align: left;">15.0</td>
</tr>
<tr>
<td style="text-align: left;"> East</td>
<td style="text-align: left;">241</td>
<td style="text-align: left;">19.3</td>
<td style="text-align: left;">17.9</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Education</td>
</tr>
<tr>
<td style="text-align: left;"> Primary or middle school</td>
<td style="text-align: left;">221</td>
<td style="text-align: left;">17.7</td>
<td style="text-align: left;">17.9</td>
</tr>
<tr>
<td style="text-align: left;"> Vocational school</td>
<td style="text-align: left;">328</td>
<td style="text-align: left;">26.2</td>
<td style="text-align: left;">24.9</td>
</tr>
<tr>
<td style="text-align: left;"> Secondary school</td>
<td style="text-align: left;">428</td>
<td style="text-align: left;">34.2</td>
<td style="text-align: left;">35.9</td>
</tr>
<tr>
<td style="text-align: left;"> Higher</td>
<td style="text-align: left;">273</td>
<td style="text-align: left;">21.8</td>
<td style="text-align: left;">21.3</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Employment status</td>
</tr>
<tr>
<td style="text-align: left;"> Employed/self-employed</td>
<td style="text-align: left;">637</td>
<td style="text-align: left;">51.2</td>
<td style="text-align: left;">49.7</td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed (able to work)</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">7.2</td>
<td style="text-align: left;">8.4</td>
</tr>
<tr>
<td style="text-align: left;"> Unemployed (unable to work, annuitant)</td>
<td style="text-align: left;">77</td>
<td style="text-align: left;">6.2</td>
<td style="text-align: left;">6.7</td>
</tr>
<tr>
<td style="text-align: left;"> Student (full time)</td>
<td style="text-align: left;">114</td>
<td style="text-align: left;">9.2</td>
<td style="text-align: left;">7.2</td>
</tr>
<tr>
<td style="text-align: left;"> Homemaker, housewife</td>
<td style="text-align: left;">32</td>
<td style="text-align: left;">2.6</td>
<td style="text-align: left;">3.4</td>
</tr>
<tr>
<td style="text-align: left;"> Retired person</td>
<td style="text-align: left;">295</td>
<td style="text-align: left;">23.7</td>
<td style="text-align: left;">24.7</td>
</tr>
<tr>
<td style="text-align: left;">Responsibility for children</td>
<td style="text-align: left;">429</td>
<td style="text-align: left;">34.3</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Number of persons in a household, mean, SD</td>
<td style="text-align: left;">2.96</td>
<td style="text-align: left;">1.4</td>
<td style="text-align: left;">2.69</td>
</tr>
<tr>
<td style="text-align: left;">Considering himself/herself as a religious person</td>
<td style="text-align: left;">1127</td>
<td style="text-align: left;">90.1</td>
<td style="text-align: left;">92.3</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Religion (among religious persons)</td>
</tr>
<tr>
<td style="text-align: left;"> Catholicism</td>
<td style="text-align: left;">1106</td>
<td style="text-align: left;">98.1</td>
<td style="text-align: left;">92.0</td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">1.9</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Believe in life after death</td>
</tr>
<tr>
<td style="text-align: left;"> Definitely yes</td>
<td style="text-align: left;">390</td>
<td style="text-align: left;">31.2</td>
<td style="text-align: left;">44.0</td>
</tr>
<tr>
<td style="text-align: left;"> Rather yes</td>
<td style="text-align: left;">375</td>
<td style="text-align: left;">30.0</td>
<td style="text-align: left;">31.0</td>
</tr>
<tr>
<td style="text-align: left;"> I don’t know</td>
<td style="text-align: left;">228</td>
<td style="text-align: left;">18.2</td>
<td style="text-align: left;">7.0</td>
</tr>
<tr>
<td style="text-align: left;"> Rather no</td>
<td style="text-align: left;">127</td>
<td style="text-align: left;">10.1</td>
<td rowspan="2" style="text-align: left;">18.0</td>
</tr>
<tr>
<td style="text-align: left;"> Definitely no</td>
<td style="text-align: left;">113</td>
<td style="text-align: left;">9.0</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Experience with serious illness</td>
</tr>
<tr>
<td style="text-align: left;"> In self</td>
<td style="text-align: left;">382</td>
<td style="text-align: left;">30.5</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> In family</td>
<td style="text-align: left;">892</td>
<td style="text-align: left;">71.2</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> In caring for others</td>
<td style="text-align: left;">626</td>
<td style="text-align: left;">50.0</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Comorbidity confirmed by doctor</td>
<td style="text-align: left;">533</td>
<td style="text-align: left;">42.6</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">General perception of health (SF-1)</td>
</tr>
<tr>
<td style="text-align: left;"> Excellent</td>
<td style="text-align: left;">89</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: left;">6.2</td>
</tr>
<tr>
<td style="text-align: left;"> Very good</td>
<td style="text-align: left;">384</td>
<td style="text-align: left;">30.7</td>
<td style="text-align: left;">25.3</td>
</tr>
<tr>
<td style="text-align: left;"> Good</td>
<td style="text-align: left;">566</td>
<td style="text-align: left;">45.2</td>
<td style="text-align: left;">44.3</td>
</tr>
<tr>
<td style="text-align: left;"> Fair</td>
<td style="text-align: left;">190</td>
<td style="text-align: left;">15.2</td>
<td style="text-align: left;">20.3</td>
</tr>
<tr>
<td style="text-align: left;"> Poor</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">1.8</td>
<td style="text-align: left;">3.9</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Self-rated health using EQ-5D-5L</td>
</tr>
<tr>
<td style="text-align: left;"> 11111</td>
<td style="text-align: left;">437</td>
<td style="text-align: left;">34.9</td>
<td style="text-align: left;">38.5</td>
</tr>
<tr>
<td style="text-align: left;"> Any other health state</td>
<td style="text-align: left;">815</td>
<td style="text-align: left;">65.1</td>
<td style="text-align: left;">61.5</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Self-rated health using EQ-VAS</td>
</tr>
<tr>
<td style="text-align: left;"> 100</td>
<td style="text-align: left;">109</td>
<td style="text-align: left;">8.7</td>
<td style="text-align: left;">8.1</td>
</tr>
<tr>
<td style="text-align: left;"> 90–99</td>
<td style="text-align: left;">432</td>
<td style="text-align: left;">34.5</td>
<td style="text-align: left;">23.8</td>
</tr>
<tr>
<td style="text-align: left;"> 80–89</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">24.0</td>
<td style="text-align: left;">22.0</td>
</tr>
<tr>
<td style="text-align: left;"> &lt; 80</td>
<td style="text-align: left;">411</td>
<td style="text-align: left;">32.8</td>
<td style="text-align: left;">46.4</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS, mean (SD)</td>
<td style="text-align: left;">79.9</td>
<td style="text-align: left;">(16.9)</td>
<td style="text-align: left;">73.7 (19.9)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Any health problems within EQ-5D-5L dimension</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility (MO)</td>
<td style="text-align: left;">360</td>
<td style="text-align: left;">28.8</td>
<td style="text-align: left;">25.8</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care (SC)</td>
<td style="text-align: left;">124</td>
<td style="text-align: left;">9.9</td>
<td style="text-align: left;">9.1</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activities (UA)</td>
<td style="text-align: left;">258</td>
<td style="text-align: left;">20.6</td>
<td style="text-align: left;">17.4</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort (PD)</td>
<td style="text-align: left;">668</td>
<td style="text-align: left;">53.4</td>
<td style="text-align: left;">52.2</td>
</tr>
<tr>
<td style="text-align: left;"><p> Anxiety/depression (AD)</p>
<p>Household income (monthly, per person, €)</p></td>
<td style="text-align: left;">537</td>
<td style="text-align: left;">42.9</td>
<td style="text-align: left;">41.5</td>
</tr>
<tr>
<td style="text-align: left;"> ≤ 200</td>
<td style="text-align: left;">207</td>
<td style="text-align: left;">16.5</td>
<td rowspan="4" style="text-align: left;">Average 340</td>
</tr>
<tr>
<td style="text-align: left;"> 201–320</td>
<td style="text-align: left;">306</td>
<td style="text-align: left;">24.4</td>
</tr>
<tr>
<td style="text-align: left;"> 321–500</td>
<td style="text-align: left;">296</td>
<td style="text-align: left;">23.6</td>
</tr>
<tr>
<td style="text-align: left;"> &gt; 500</td>
<td style="text-align: left;">200</td>
<td style="text-align: left;">16.0</td>
</tr>
<tr>
<td style="text-align: left;"> Refuse to answer</td>
<td style="text-align: left;">243</td>
<td style="text-align: left;">19.4</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

*SD* standard deviation, *VAS* visual analog scale

</div>

The sample was representative of the Polish population in terms of age, sex, educational background, employment status, size and geographical location of the place of residence (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). It was also similar to the Polish population in terms of health as measured by the EQ-5D-5L descriptive system, EQ visual analog scale and SF-1 \[20\].

<figure id="Fig1">
<p><img src="40273_2019_811_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40273_2019_811_Fig1_HTML.gif" /></p>
<figcaption>Geographical representation of respondents in the Polish EQ-5D-5L valuation study</figcaption>
</figure>

### Data Characteristics

In total, 12,520 individual TTO valuations were available, with a mean number of 250 (standard deviation 6.7) observations per mild health state (misery index 6) and a mean number of 125 (standard deviation 5.3) observations for other 80 health states. In TTO, in 10.7% of the experiments, the time was not traded, and eight respondents (0.6%) did not trade for any state (an additional four respondents valued all the states at the same level, in each case with a utility of 0.95). In 1552 (13.5%) experiments, the valuations were considered worse than dead. In 271 (2.4%) and 784 (6.1%) cases, a utility of 0 and − 1 was reported, respectively. The average utility of the 55555 state in TTO was − 0.408 (33.5% at − 1). ESM 1, Online Resource 3 and Fig. <a href="#Fig2" data-ref-type="fig">2</a> for the observed TTO values.

<figure id="Fig2">
<p><img src="40273_2019_811_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2019_811_Fig2_HTML.gif" /></p>
<figcaption>Distribution of observed time trade-off (TTO) values</figcaption>
</figure>

In total, 1040 health states (8.3%) were indicated by the respondents in the feedback module as not revealing their true preferences in hindsight and were removed, leaving 11,480 TTO valuations for modelling. Using the feedback module reduced the number of respondents with inconsistencies related to health state 55555, from an initial 49 (3.9%) to 22 (1.8%). In the DCE data (8764 DCE pairs), 36 respondents (2.9%) presented with a suspicious response pattern (choosing states on the left or right or regularly alternately) but were not excluded from the modelling.

### Preferred Model (Polish EQ-5D-5L Value Set)

In the final model, the estimated decrease of utility for level 5 amounts to: 0.314 (MO), 0.264 (SC), 0.205 (UA), 0.575 (PD) and 0.232 (AD). For example, the relative weights of levels 2–4 in UA are: 0.112 (i.e. 0.023/0.205 in Table <a href="#Tab2" data-ref-type="table">2</a>), 0.195 and 0.471, while in PD: 0.052, 0.087 and 0.455. The intermediate models differ slightly (Table <a href="#Tab2" data-ref-type="table">2</a>). The disutilities increase when accounting for the impact of religion and censoring (both motivated by statistical criteria). In the final value set, we get u(22222) = 0.873, u(33333) = 0.800, u(44444) = 0.296, and u(55555) = − 0.590, as compared to u(22222) = 0.716 and u(33333) = − 0.523 in the Polish EQ-5D-3L tariff. We present the complete results, alongside more technical parameters, in ESM 1, Online Resource 4, a practical example of how to use a scoring algorithm to estimate the value for a health state in ESM 1, Online Resource 5 and all 3125 values for the Polish EQ-5D-5L value set, as well as an index calculator, in ESM 3.

<div id="Tab2" class="table-wrap">

<div class="caption">

Modelling results

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Model 1<br />
panel, random effects</th>
<th style="text-align: left;">Model 2<br />
Bayesian</th>
<th style="text-align: left;">Model 3<br />
M2 + random parameters</th>
<th style="text-align: left;">Model 4<br />
M3 + error scaling with <em>t</em>-Student</th>
<th style="text-align: left;">Model 5<br />
M4 + religion scaling</th>
<th style="text-align: left;">Final model<br />
M5 + DCE, censoring</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Const.</td>
<td style="text-align: left;">0.005 (− 0.010; 0.019)</td>
<td style="text-align: left;">Not used</td>
<td style="text-align: left;">Not used</td>
<td style="text-align: left;">Not used</td>
<td style="text-align: left;">Not used</td>
<td style="text-align: left;">Not used</td>
</tr>
<tr>
<td style="text-align: left;">MO2</td>
<td style="text-align: left;">0.021 (0.002; 0.039)</td>
<td style="text-align: left;">0.023 (0.001; 0.044)</td>
<td style="text-align: left;">0.058 (0.013; 0.073)</td>
<td style="text-align: left;">0.017 (0.014; 0.022)</td>
<td style="text-align: left;">0.019 (0.014; 0.023)</td>
<td style="text-align: left;">0.025 (0.020; 0.029)</td>
</tr>
<tr>
<td style="text-align: left;">MO3</td>
<td style="text-align: left;">0.012 (−0.007; 0.031)</td>
<td style="text-align: left;">0.016 (0.000; 0.036)</td>
<td style="text-align: left;">0.077 (0.021; 0.094)</td>
<td style="text-align: left;">0.015 (0.005; 0.026)</td>
<td style="text-align: left;">0.016 (0.005; 0.028)</td>
<td style="text-align: left;">0.034 (0.026; 0.042)</td>
</tr>
<tr>
<td style="text-align: left;">MO4</td>
<td style="text-align: left;">0.098 (0.077; 0.118)</td>
<td style="text-align: left;">0.101 (0.074; 0.129)</td>
<td style="text-align: left;">0.159 (0.071; 0.181)</td>
<td style="text-align: left;">0.101 (0.085; 0.116)</td>
<td style="text-align: left;">0.107 (0.090; 0.124)</td>
<td style="text-align: left;">0.126 (0.113; 0.141)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>MO5</strong></td>
<td style="text-align: left;"><strong>0.262 (0.238; 0.285)</strong></td>
<td style="text-align: left;"><strong>0.263 (0.239; 0.289)</strong></td>
<td style="text-align: left;"><strong>0.303 (0.271; 0.330)</strong></td>
<td style="text-align: left;"><strong>0.251 (0.228; 0.274)</strong></td>
<td style="text-align: left;"><strong>0.267 (0.242; 0.293)</strong></td>
<td style="text-align: left;"><strong>0.314 (0.286; 0.342)</strong></td>
</tr>
<tr>
<td style="text-align: left;">SC2</td>
<td style="text-align: left;">0.030 (0.014; 0.046)</td>
<td style="text-align: left;">0.037 (0.015; 0.059)</td>
<td style="text-align: left;">0.015 (0.003; 0.087)</td>
<td style="text-align: left;">0.029 (0.024; 0.034)</td>
<td style="text-align: left;">0.031 (0.026; 0.036)</td>
<td style="text-align: left;">0.031 (0.027; 0.036)</td>
</tr>
<tr>
<td style="text-align: left;">SC3</td>
<td style="text-align: left;">0.038 (0.017; 0.059)</td>
<td style="text-align: left;">0.042 (0.014; 0.071)</td>
<td style="text-align: left;">0.005 (0.000; 0.119)</td>
<td style="text-align: left;">0.037 (0.028; 0.047)</td>
<td style="text-align: left;">0.040 (0.029; 0.050)</td>
<td style="text-align: left;">0.047 (0.040; 0.055)</td>
</tr>
<tr>
<td style="text-align: left;">SC4</td>
<td style="text-align: left;">0.122 (0.098; 0.146)</td>
<td style="text-align: left;">0.116 (0.089; 0.143)</td>
<td style="text-align: left;">0.042 (0.027; 0.180)</td>
<td style="text-align: left;">0.108 (0.094; 0.123)</td>
<td style="text-align: left;">0.115 (0.099; 0.131)</td>
<td style="text-align: left;">0.111 (0.099; 0.123)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>SC5</strong></td>
<td style="text-align: left;"><strong>0.276 (0.254; 0.298)</strong></td>
<td style="text-align: left;"><strong>0.269 (0.244; 0.295)</strong></td>
<td style="text-align: left;"><strong>0.242 (0.193; 0.268)</strong></td>
<td style="text-align: left;"><strong>0.258 (0.237; 0.282)</strong></td>
<td style="text-align: left;"><strong>0.273 (0.249; 0.299)</strong></td>
<td style="text-align: left;"><strong>0.264 (0.243; 0.286)</strong></td>
</tr>
<tr>
<td style="text-align: left;">UA2</td>
<td style="text-align: left;">0.031 (0.014; 0.048)</td>
<td style="text-align: left;">0.034 (0.011; 0.058)</td>
<td style="text-align: left;">0.002 (0.000; 0.007)</td>
<td style="text-align: left;">0.033 (0.026; 0.039)</td>
<td style="text-align: left;">0.034 (0.028; 0.042)</td>
<td style="text-align: left;">0.023 (0.019; 0.027)</td>
</tr>
<tr>
<td style="text-align: left;">UA3</td>
<td style="text-align: left;">0.032 (0.009; 0.054)</td>
<td style="text-align: left;">0.041 (0.015; 0.067)</td>
<td style="text-align: left;">0.005 (0.000; 0.014)</td>
<td style="text-align: left;">0.050 (0.040; 0.060)</td>
<td style="text-align: left;">0.053 (0.043; 0.063)</td>
<td style="text-align: left;">0.040 (0.032; 0.048)</td>
</tr>
<tr>
<td style="text-align: left;">UA4</td>
<td style="text-align: left;">0.092 (0.070; 0.115)</td>
<td style="text-align: left;">0.088 (0.062; 0.115)</td>
<td style="text-align: left;">0.024 (0.010; 0.038)</td>
<td style="text-align: left;">0.104 (0.091; 0.117)</td>
<td style="text-align: left;">0.110 (0.095; 0.125)</td>
<td style="text-align: left;">0.097 (0.087; 0.107)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>UA5</strong></td>
<td style="text-align: left;"><strong>0.186 (0.167; 0.206)</strong></td>
<td style="text-align: left;"><strong>0.183 (0.157; 0.209)</strong></td>
<td style="text-align: left;"><strong>0.180 (0.161; 0.201)</strong></td>
<td style="text-align: left;"><strong>0.180 (0.161; 0.200)</strong></td>
<td style="text-align: left;"><strong>0.190 (0.169; 0.212)</strong></td>
<td style="text-align: left;"><strong>0.205 (0.188; 0.224)</strong></td>
</tr>
<tr>
<td style="text-align: left;">PD2</td>
<td style="text-align: left;">0.028 (0.012; 0.044)</td>
<td style="text-align: left;">0.033 (0.012; 0.054)</td>
<td style="text-align: left;">0.041 (0.028; 0.054)</td>
<td style="text-align: left;">0.025 (0.021; 0.028)</td>
<td style="text-align: left;">0.026 (0.022; 0.030)</td>
<td style="text-align: left;">0.030 (0.026; 0.034)</td>
</tr>
<tr>
<td style="text-align: left;">PD3</td>
<td style="text-align: left;">0.034 (0.014; 0.053)</td>
<td style="text-align: left;">0.035 (0.007; 0.063)</td>
<td style="text-align: left;">0.053 (0.036; 0.071)</td>
<td style="text-align: left;">0.030 (0.022; 0.039)</td>
<td style="text-align: left;">0.032 (0.022; 0.041)</td>
<td style="text-align: left;">0.050 (0.043; 0.058)</td>
</tr>
<tr>
<td style="text-align: left;">PD4</td>
<td style="text-align: left;">0.229 (0.208; 0.251)</td>
<td style="text-align: left;">0.228 (0.204; 0.254)</td>
<td style="text-align: left;">0.253 (0.224; 0.276)</td>
<td style="text-align: left;">0.223 (0.208; 0.239)</td>
<td style="text-align: left;">0.235 (0.217; 0.253)</td>
<td style="text-align: left;">0.261 (0.244; 0.280)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>PD5</strong></td>
<td style="text-align: left;"><strong>0.467 (0.440; 0.494)</strong></td>
<td style="text-align: left;"><strong>0.473 (0.446; 0.499)</strong></td>
<td style="text-align: left;"><strong>0.490 (0.464; 0.518)</strong></td>
<td style="text-align: left;"><strong>0.492 (0.463; 0.520)</strong></td>
<td style="text-align: left;"><strong>0.519 (0.485; 0.555)</strong></td>
<td style="text-align: left;"><strong>0.575 (0.538; 0.613)</strong></td>
</tr>
<tr>
<td style="text-align: left;">AD2</td>
<td style="text-align: left;">0.024 (0.006; 0.041)</td>
<td style="text-align: left;">0.032 (0.010; 0.054)</td>
<td style="text-align: left;">0.049 (0.015; 0.061)</td>
<td style="text-align: left;">0.019 (0.016; 0.023)</td>
<td style="text-align: left;">0.020 (0.017; 0.024)</td>
<td style="text-align: left;">0.018 (0.015; 0.021)</td>
</tr>
<tr>
<td style="text-align: left;">AD3</td>
<td style="text-align: left;">0.034 (0.011; 0.056)</td>
<td style="text-align: left;">0.033 (0.006; 0.058)</td>
<td style="text-align: left;">0.085 (0.038; 0.101)</td>
<td style="text-align: left;">0.037 (0.026; 0.049)</td>
<td style="text-align: left;">0.039 (0.027; 0.052)</td>
<td style="text-align: left;">0.029 (0.022; 0.037)</td>
</tr>
<tr>
<td style="text-align: left;">AD4</td>
<td style="text-align: left;">0.114 (0.094; 0.135)</td>
<td style="text-align: left;">0.114 (0.088; 0.139)</td>
<td style="text-align: left;">0.160 (0.116; 0.181)</td>
<td style="text-align: left;">0.119 (0.106; 0.132)</td>
<td style="text-align: left;">0.126 (0.113; 0.142)</td>
<td style="text-align: left;">0.108 (0.097; 0.119)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>AD5</strong></td>
<td style="text-align: left;"><strong>0.224 (0.203; 0.244)</strong></td>
<td style="text-align: left;"><strong>0.226 (0.201; 0.251)</strong></td>
<td style="text-align: left;"><strong>0.176 (0.153; 0.231)</strong></td>
<td style="text-align: left;"><strong>0.211 (0.194; 0.229)</strong></td>
<td style="text-align: left;"><strong>0.223 (0.204; 0.243)</strong></td>
<td style="text-align: left;"><strong>0.232 (0.213; 0.252)</strong></td>
</tr>
<tr>
<td style="text-align: left;">Deviance</td>
<td rowspan="2" style="text-align: left;">61.2% (<em>R</em><sup>2</sup> used instead)</td>
<td style="text-align: left;">11,866</td>
<td style="text-align: left;">−777</td>
<td style="text-align: left;">−13,781</td>
<td style="text-align: left;">−13,780</td>
<td style="text-align: left;">−9215</td>
</tr>
<tr>
<td style="text-align: left;">DIC</td>
<td style="text-align: left;">11,886</td>
<td style="text-align: left;">2597</td>
<td style="text-align: left;">−9704</td>
<td style="text-align: left;">−9704</td>
<td style="text-align: left;">−9215<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">PSRF</td>
<td style="text-align: left;">n.a.</td>
<td style="text-align: left;">All &lt;1.01</td>
<td style="text-align: left;">Maximum = 15</td>
<td style="text-align: left;">All &lt;1.01</td>
<td style="text-align: left;">All &lt;1.01</td>
<td style="text-align: left;">All &lt;1.01</td>
</tr>
<tr>
<td style="text-align: left;">Maximum <em>u</em> (not 11111)</td>
<td style="text-align: left;">0.983</td>
<td style="text-align: left;">0.984</td>
<td style="text-align: left;">0.998</td>
<td style="text-align: left;">0.985</td>
<td style="text-align: left;">0.984</td>
<td style="text-align: left;">0.982</td>
</tr>
<tr>
<td style="text-align: left;"><em>u</em> (22222)</td>
<td style="text-align: left;">0.862</td>
<td style="text-align: left;">0.841</td>
<td style="text-align: left;">0.834</td>
<td style="text-align: left;">0.877</td>
<td style="text-align: left;">0.870</td>
<td style="text-align: left;">0.873</td>
</tr>
<tr>
<td style="text-align: left;"><em>u</em> (33333)</td>
<td style="text-align: left;">0.847</td>
<td style="text-align: left;">0.833</td>
<td style="text-align: left;">0.775</td>
<td style="text-align: left;">0.830</td>
<td style="text-align: left;">0.821</td>
<td style="text-align: left;">0.800</td>
</tr>
<tr>
<td style="text-align: left;"><em>u</em> (44444)</td>
<td style="text-align: left;">0.340</td>
<td style="text-align: left;">0.352</td>
<td style="text-align: left;">0.361</td>
<td style="text-align: left;">0.345</td>
<td style="text-align: left;">0.307</td>
<td style="text-align: left;">0.296</td>
</tr>
<tr>
<td style="text-align: left;"><em>u</em> (55555)</td>
<td style="text-align: left;">− 0.420</td>
<td style="text-align: left;">− 0.415</td>
<td style="text-align: left;">− 0.391</td>
<td style="text-align: left;">− 0.392</td>
<td style="text-align: left;">− 0.471</td>
<td style="text-align: left;">− 0.590</td>
</tr>
<tr>
<td style="text-align: left;">% states <em>u</em> &lt; 0</td>
<td style="text-align: left;">2.85</td>
<td style="text-align: left;">2.88</td>
<td style="text-align: left;">2.69</td>
<td style="text-align: left;">2.78</td>
<td style="text-align: left;">4.26</td>
<td style="text-align: left;">6.66</td>
</tr>
<tr>
<td style="text-align: left;">Dimension order</td>
<td style="text-align: left;">PD, SC, MO, AD, UA</td>
<td style="text-align: left;">PD, SC, MO, AD, UA</td>
<td style="text-align: left;">PD, MO, SC, UA, AD</td>
<td style="text-align: left;">PD, SC, MO, AD, UA</td>
<td style="text-align: left;">PD, SC, MO, AD, UA</td>
<td style="text-align: left;">PD, MO, SC, AD, UA</td>
</tr>
<tr>
<td style="text-align: left;">Levels consistency</td>
<td style="text-align: left;">MO3 &lt; MO2</td>
<td style="text-align: left;">MO3 &lt; MO2</td>
<td style="text-align: left;">SC3 &lt; SC2</td>
<td style="text-align: left;">MO3 &lt; MO2</td>
<td style="text-align: left;">MO3 &lt; MO2</td>
<td style="text-align: left;">Consistent</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *DCE* discrete choice experiment, *DIC* deviance information criterion, *M* model, *MO* mobility, *n.a. PD* pain/discomfort, *PSRF* potential scale reduction factor, *SC* self-care, *u* utility, *UA* usual activities

<sup>a</sup>Failed to calculate penalty in JAGS (“support of observed nodes is not fixed”)

</div>

### Comparison of Polish Value Sets

The kernel density plots (Fig. <a href="#Fig3" data-ref-type="fig">3</a>) and the utility values for the individual states (Fig. <a href="#Fig4" data-ref-type="fig">4</a>) illustrate the high degree of similarity between the three Polish value sets. The new descriptive system is also more sensitive to a slight worsening in health: in the results, there are more utility values close to 1. In all likelihood, because of a higher number of health states, the distribution of the utility value is unimodal for EQ-5D-5L, while bimodal for EQ-5D-3L (though this comparison is made within the domain of health states, not of individuals, and thus it is a property of the descriptive system more than the value set itself). The new value set has a slightly lower worst utility (− 0.590; − 0.523, for both the EQ-5D-3L and the cross-walk), which is intuitive in view of the five-level system, but also in terms of accounting for the censoring and the bias from religious respondents in the present modelling.

<figure id="Fig3">
<p><img src="40273_2019_811_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="40273_2019_811_Fig3_HTML.gif" /></p>
<figcaption>Kernel density functions for the three Polish value sets (EQ-5D-5L directly measured is indicated by a solid line; EQ-5D-5L cross-walk is indicated by a dashed line; EQ-5D-3L is indicated by a dotted line)</figcaption>
</figure>

<figure id="Fig4">
<p><img src="40273_2019_811_Fig4_HTML.jpg" id="MO4" /></p>
<p><img src="40273_2019_811_Fig4_HTML.gif" /></p>
<figcaption>Utility values for all states from three Polish value sets ordered by EQ-5D-5L (EQ-5D-5L directly measured is indicated by a solid line; EQ-5D-5L cross-walk is indicated by a solid light grey line, EQ-5D-3L is indicated by dots)</figcaption>
</figure>

The importance of the dimensions scarcely changed: PD, MO and SC are the most significant, followed by AD and UA in the present value set, whereas by UA and AD in the previous two value sets. In Table <a href="#Tab3" data-ref-type="table">3</a>, additional descriptive statistics are presented. Importantly, some of them are primarily influenced by the descriptive system, rather than the value set (e.g. the percentage of states with negative utility depends on the utilities assigned to health states, and also on how many severe health states are present in a descriptive system).

<div id="Tab3" class="table-wrap">

<div class="caption">

Comparison of three Polish EQ-5D value sets

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Polish EQ-5D-5L value set</th>
<th style="text-align: left;">Polish EQ-5D-5L crosswalk value set</th>
<th style="text-align: left;">Polish EQ-5D-3L value set</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Valuation method</td>
<td style="text-align: left;">Hybrid (TTO/DCE)</td>
<td style="text-align: left;">Crosswalk (TTO)</td>
<td style="text-align: left;">TTO</td>
</tr>
<tr>
<td style="text-align: left;">Dimensions ordering, from the most to the least important (disutility for the worse level within a dimension)</td>
<td style="text-align: left;"><p>PD (− 0.575)</p>
<p>MO (− 0.314)</p>
<p>SC (− 0.264)</p>
<p>AD (− 0.232)</p>
<p>UA (− 0.205)</p></td>
<td style="text-align: left;"><p>PD (− 0.489)<sup>a</sup></p>
<p>MO (− 0.331)</p>
<p>SC (− 0.235)</p>
<p>UA (− 0.212)</p>
<p>AD (− 0.207)</p></td>
<td style="text-align: left;"><p>PD (− 0.489)<sup>a</sup></p>
<p>MO (− 0.331)</p>
<p>SC (− 0.235)</p>
<p>UA (− 0.212)</p>
<p>AD (− 0.207)</p></td>
</tr>
<tr>
<td style="text-align: left;">Number of health states</td>
<td style="text-align: left;">3125</td>
<td style="text-align: left;">3125</td>
<td style="text-align: left;">243</td>
</tr>
<tr>
<td style="text-align: left;">Maximum value (11111)</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;">Second highest value (health state)</td>
<td style="text-align: left;">0.982 (11112)</td>
<td style="text-align: left;">0.940 (11112)</td>
<td style="text-align: left;">0.925 (11112)</td>
</tr>
<tr>
<td style="text-align: left;">Mean value (SD)</td>
<td style="text-align: left;">0.476 (0.286)</td>
<td style="text-align: left;">0.448 (0.253)</td>
<td style="text-align: left;">0.382 (0.310)</td>
</tr>
<tr>
<td style="text-align: left;">Median value (Q1–Q3)</td>
<td style="text-align: left;">0.523 (0.286–0.692)</td>
<td style="text-align: left;">0.483 (0.282–0.642)</td>
<td style="text-align: left;">0.406 (0.155–0.630)</td>
</tr>
<tr>
<td style="text-align: left;">Minimum value (health state)</td>
<td style="text-align: left;">− 0.590 (55555)</td>
<td style="text-align: left;">− 0.523 (55555)</td>
<td style="text-align: left;">− 0.523 (33333)</td>
</tr>
<tr>
<td style="text-align: left;">Value for 22222</td>
<td style="text-align: left;">0.862</td>
<td style="text-align: left;">0.760</td>
<td style="text-align: left;">0.716</td>
</tr>
<tr>
<td style="text-align: left;">Value for 33333</td>
<td style="text-align: left;">0.721</td>
<td style="text-align: left;">0.716</td>
<td style="text-align: left;">−0.523</td>
</tr>
<tr>
<td style="text-align: left;">Value for 44444</td>
<td style="text-align: left;">0.173</td>
<td style="text-align: left;">0.336</td>
<td style="text-align: left;">n.a.</td>
</tr>
<tr>
<td style="text-align: left;">Health states ≥0.8, <em>n</em> (%)</td>
<td style="text-align: left;">160 (5.1)</td>
<td style="text-align: left;">163 (5.2)</td>
<td style="text-align: left;">22 (9.1)</td>
</tr>
<tr>
<td style="text-align: left;">Health states worse than dead (&lt;0), <em>n</em> (%)</td>
<td style="text-align: left;">137 (4.4)</td>
<td style="text-align: left;">124 (4.0)</td>
<td style="text-align: left;">32 (13.2)</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *DC*E discrete choice experiment, *MO* mobility, *n.a.*, *PD* pain/discomfort, *SC* self-care, *SD* standard deviation, *TTO* time trade-off, *UA* usual activities

<sup>a</sup>Disutilities for dimensions, not including the constant (− 0.049)

</div>

## Discussion

In this study, we followed an official EQ-VT protocol, performed over 1200 computer-assisted face-to-face interviews, collected TTO values for 86 EQ-5D-5L health states and DCE choices for 196 pairs of states, and estimated the Polish EQ-5D-5L value set using both elicitation tasks. Our final model accounted for random parameters (respondent heterogeneity), error scaling (greater noise for more severe states), censoring at − 1, unwillingness to trade in TTO by religious participants and non-logit distribution in DCE. All these elements of the model were added in response to the statistical considerations. To the best of our knowledge, two elements are novel: the impact of religiosity and error scaling. We find the latter one rather intuitive; the variance of noise increasing with severity may partially explain why there is a weak relationship between the misery index and the disutility for the negative utility values \[47\]. The former element is probably the most controversial assumption in our model, and our decision to use it followed the reasoning presented in \[45\]. It is important to stress that correcting for the impact of religiosity does not aim at neglecting the preferences of religious individuals, but at correcting for how they may be biased in the TTO task (and how the elicitation task differs from what the resulting utilities are used for; not to actually shorten an individual’s life but to trade-off benefits between different individuals).

There are two more arbitrary decisions we made in the modelling. First, we decided to combine TTO and DCE data. We believe that provided there is no consensus on whether one method is clearly better (not in terms of cost or ease of application but the quality of the results) using both is the safest approach. Second, we decided to use a simple model with no constant and no interaction terms. As mentioned above, that makes the final results more applicable to situations where only limited information is available (e.g. only marginal distributions of levels in individual dimensions). To represent respondents’ answers more accurately (in the sense of predictive validity), a more complex model would probably have to be used (e.g. accounting for a non-linear time preference \[44\]). In this sense, there is a trade-off between trying to represent the data faithfully and using a specification that can be subsequently easily used.

The assumptions resulted in the theoretical value of u(55555) = − 0.590, visibly lower than the average utility elicited in TTO, i.e. − 0.408. This difference stems from three elements of our model. First, censoring leads to interpreting observed − 1s as effectively possibly much lower than − 1 (33.5% of TTO tasks for 55555 ended by assigning − 1). Second, introducing the impact of religiosity in TTO tasks results in effectively assuming that the true disutility is larger than the observed one. Third, by considering the random noise as having a larger variance for severe states, we make the parameters less driven by the actual observations for the severe states. Nevertheless, the final utility for the pit state is similar to the one in the EQ-5D-3L value set (hence, the cross-walk), and the slight decrease is intuitive in view of the larger number of levels.

Regarding the final value set, despite the fact that it describes significantly more possible health states (3125 vs. 243), it is similar to the Polish EQ-5D-3L value set in terms of a minimum utility, the range of values and the order of three most important dimensions \[16\]. The resemblance between the general characteristics of both value sets should support the comparability of Health State Utility Values obtained with these two types of EQ-5D questionnaire, and consequently the comparability of the results from economic analyses and the reimbursement decisions made, what was questioned in some other countries, such as the UK \[48, 49\]. What differentiates our study from the previous Polish valuation is greater attention to sampling, which resulted in a study group similar to Polish society as a whole, in terms of a higher number of demographic features (geographical spread in the first instance, but also employment status and size of locality).

In similarity to some other EQ-5D-5L valuations performed in developed countries, we noted the relative increase in the importance of the anxiety/depression dimension, in comparison to former EQ-5D-3L valuation studies. We suppose that this is primarily a consequence of a change in health state preferences over the period of one or two decades separating the valuation studies, rather than the effect of different wording in the EQ-5D-5L questionnaire. We may observe this phenomenon in England, Germany, the Netherlands, Spain and Japan \[34, 36–38, 50, 51\], whereas in lower income countries, such as Uruguay or The Philippines, anxiety/depression remains the least important domain \[52, 53\]. In addition to this observation, the predominance of the mobility dimension in Asian countries (China, Hong Kong, Indonesia, Japan, South Korea and Thailand) merits further investigation \[39, 54–57\]. Some changes in the dimension weightings may also be subject to change in the descriptive system: in the Polish version, the wording for mobility has been changed from ‘confined to bed’ to ‘extreme problems’.

Taking into account the number of CEE countries (20) and the relatively low gross domestic product these countries have, the objective of searching for simpler and inexpensive valuation protocols acquires further significance. Discrete choice experiment-based valuations performed online constitute a potential solution, although certain methodological challenges still have to be dealt with \[58, 59\]. In the meantime, researchers from the CEE region frequently face the dilemma: ‘what EQ-5D value set should I use in the absence of a national value set?’ According to the results of the recent review, in the case of EQ-5D-3L, CEE researchers mostly prefer the UK Measurement and Valuation of Health study tariff \[60, 61\]. In the case of EQ-5D-5L, the choice will be harder, as the EQ-5D-5L value set for England has faced criticism and is still not supported by the National Institute for Health and Care Excellence \[48\]. Slovenian researchers may use the cross-walk approach based on their visual analog scale-based EQ-5D-3L value set, but recommendations for scientists from other CEE countries are far from straightforward \[21\]. Nevertheless, they should at least consider using either the Polish or the forthcoming Hungarian EQ-5D-5L value sets, as CEE countries share some common cultural and historical background.

## Conclusions

We developed the TTO and DCE-based EQ-5D-5L value set for Poland. It will complement the existing Polish EQ-5D-3L value set and will further stimulate the development of local quality-of-life research and the use of health technology assessment in decision making within the healthcare sector. While the new EQ-5D-5L value set offers more sensitivity, it also provides ground for consistency of past and future decisions. The presented EQ-5D-5L value set may be considered as an option by researchers from CEE countries who lack their own national health preference data.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

ESM 1 Supplementary materials \[Word file\] (DOCX 192 kb)

</div>

<div class="caption">

ESM 2 JAGS code used for the final model estimation \[JAGS file\] (DOCX 4 kb)

</div>

<div class="caption">

ESM 3 EQ-5D-5L value set for Poland (all 3125 values) and Polish EQ-5D-5L Index calculator \[Excel file\] (XLSX 1331 kb)

</div>

## Acknowledgements

The authors are grateful to CBOS interviewers led by Artemis Bellos and Marcin Herrmann for their commitment to collecting high-quality data. We thank colleagues from the EuroQol Office for advice and feedback received throughout the study.

## Author contributions

DG, MJ and MN designed the study and secured funding. DG and KG trained the interviewers and coordinated the data collection process. MJ and DG analysed the data and prepared a first draft of the manuscript. All authors played a role in the review of the analysis, interpretation of the results, and in reviewing and recommending revisions to the final manuscript.

## Funding

This research was funded by the EuroQol Research Foundation (EQ Project 2015240) and HealthQuest, Warsaw, Poland. The views expressed here do not necessarily agree with those of the above-mentioned institutions.

## Compliance with Ethical Standards

### Conflict of Interest

Dominik Golicki and Michał Jakubczyk are members of the EuroQol Research Foundation (the copyright holders of the EQ-5D-5L) and have received grants from the EuroQol Research Foundation. Katarzyna Graczyk and Maciej Niewada have no conflicts of interest that are directly relevant to the content of this article.

### Ethics Approval

The study was approved by the Ethics Committee of the Medical University of Warsaw, Warsaw, Poland (AKBE/137/16).

### Data Sharing

The datasets generated during and/or analysed during the current study are available from the corresponding author on reasonable request.

## Contributor Information

Dominik Golicki, Phone: +48 501 078 203, Email: dominik.golicki@wum.edu.pl.

Michał Jakubczyk, Email: michal.jakubczyk@sgh.waw.pl.

Katarzyna Graczyk, Email: katarzyna.graczyk88@gmail.com.

Maciej Niewada, Email: maciej.niewada@wum.edu.pl.

## References

## References

1. Dimova A, Rohova M, Atanasova E, Kawalec P, Czok K. Drug policy in Bulgaria. Value Health Reg Issues. 2017;13:50–54. doi: 10.1016/j.vhri.2017.08.001.

2. Skoupá J. Drug policy in the Czech Republic. Value Health Reg Issues. 2017;13:55–58. doi: 10.1016/j.vhri.2017.08.002.

3. Inotai A, Csanádi M, Harsányi A, Németh B. Drug policy in Huny. Value Health Reg Issues. 2017;13:16–22. doi: 10.1016/j.vhri.2017.06.003.

4. Culig J, Antolic S, Szkultecka-Dębek M. Drug policy in Croatia. Value Health Reg Issues. 2017;13:27–30. doi: 10.1016/j.vhri.2017.07.005.

5. Jahnz-Różyk K, Kawalec P, Malinowski K, Czok K. Drug policy in Poland. Value Health Reg Issues. 2017;13:23–26. doi: 10.1016/j.vhri.2017.07.001.

6. Biuletyn Informacji Publicznej Agencji Oceny Technologii Medycznych i Taryfikacji. Available from: http://bipold.aotm.gov.pl/. Accessed 10 Jan 2019.

7. Jakubiak-Lasocka J, Jakubczyk M. Cost-effectiveness versus cost-utility analyses: what are the motives behind using each and how do their results differ? A Polish example. Value Health Reg Issues. 2014;4:66–74. doi: 10.1016/j.vhri.2014.06.008.

8. Health Technology Assessment Guidelines (Version 3.0). Warsaw: Agencja Oceny Technologii Medycznych i Taryfikacji; 2016.

9. The Euroqol Group EuroQol: a new facility for the measurement of health-related quality of life. Health Policy. 1990;16:199–208. doi: 10.1016/0168-8510(90)90421-9.

10. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37:53–72. doi: 10.1016/0168-8510(96)00822-6.

11. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L) Qual Life Res. 2011;20:1727–1736. doi: 10.1007/s11136-011-9903-x.

12. Drummond MF, Sculpher MJ, Claxton K, Stoddart GL, Torrance GW. Methods for the economic evaluation of health care programmes. 4. New York: Oxford University Press; 2015.

13. Buchholz I, Janssen MF, Kohlmann T, Feng YS. A systematic review of studies comparing the measurement properties of the three-level and five-level versions of the EQ-5D. Pharmacoeconomics. 2018;36:645–661. doi: 10.1007/s40273-018-0642-5.

14. Janssen MF, Bonsel GJ, Luo N. Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. 2018;36:675–697. doi: 10.1007/s40273-018-0623-8.

15. Prevolnik Rupel V, Ogorevc M. The EQ-5D health states value set for Slovenia. Zdravstveno Varstvo. 2012;51:128–140. doi: 10.2478/sjph-2020-0024.

16. Golicki D, Jakubczyk M, Niewada M, Wrona W, Busschbach JJ. Valuation of EQ-5D health states in Poland: first TTO-based social value set in Central and Eastern Europe. Value Health. 2010;13:289–297. doi: 10.1111/j.1524-4733.2009.00596.x.

17. Janssen MF, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, et al. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22:1717–1727. doi: 10.1007/s11136-012-0322-4.

18. Golicki D, Niewada M, Karlinska A, Buczek J, Kobayashi A, Janssen MF, et al. Comparing responsiveness of the EQ-5D-5L, EQ-5D-3L and EQ VAS in stroke patients. Qual Life Res. 2015;24:1555–1563. doi: 10.1007/s11136-014-0873-7.

19. Golicki D, Niewada M, Buczek J, Karlinska A, Kobayashi A, Janssen MF, et al. Validity of EQ-5D-5L in stroke. Qual Life Res. 2015;24:845–850. doi: 10.1007/s11136-014-0834-1.

20. Golicki D, Niewada M. EQ-5D-5L Polish population norms. Arch Med Sci. 2017;13:191–200. doi: 10.5114/aoms.2015.52126.

21. van Hout B, Janssen MF, Feng YS, Kohlmann T, Busschbach J, Golicki D, et al. Interim scoring for the EQ-5D-5L: mapping the EQ-5D-5L to EQ-5D-3L value sets. Value Health. 2012;15:708–715. doi: 10.1016/j.jval.2012.02.008.

22. Golicki D, Niewada M, Hout BV, Janssen MF, Pickard AS. Interim EQ-5D-5L value set for Poland: first crosswalk value set in Central and Eastern Europe. Value Health Reg Issues. 2014;4:19–23. doi: 10.1016/j.vhri.2014.06.001.

23. Xie F, Pickard AS, Krabbe PF, Revicki D, Viney R, Devlin N, et al. A checklist for reporting valuation studies of multi-attribute utility-based instruments (CREATE) Pharmacoeconomics. 2015;33:867–877. doi: 10.1007/s40273-015-0292-9.

24. Central Statistical Office . Demographic yearbook of Poland. Warsaw: Zakład Wydawnictw Statystycznych; 2015.

25. Ramos-Goni JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20:466–473. doi: 10.1016/j.jval.2016.10.012.

26. Janssen BM, Oppe M, Versteegh MM, Stolk EA. Introducing the composite time trade-off: a test of feasibility and face validity. Eur J Health Econ. 2013;14(Suppl. 1):S5–S13. doi: 10.1007/s10198-013-0503-2.

27. Devlin NJ, Krabbe PF. The development of new research methods for the valuation of EQ-5D-5L. Eur J Health Econ. 2013;14(Suppl. 1):S1–S3. doi: 10.1007/s10198-013-0502-3.

28. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goni JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34:993–1004. doi: 10.1007/s40273-016-0404-1.

29. Devlin NJ, Tsuchiya A, Buckingham K, Tilling C. A uniform time trade off method for states better and worse than dead: feasibility study of the ‘lead time’ approach. Health Econ. 2011;20:348–361. doi: 10.1002/hec.1596.

30. Oppe M, Devlin NJ, van Hout B, Krabbe PF, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17:445–453. doi: 10.1016/j.jval.2014.04.002.

31. Stolk EA, Oppe M, Scalone L, Krabbe PF. Discrete choice modeling for the quantification of health states: the case of the EQ-5D. Value Health. 2010;13:1005–1013. doi: 10.1111/j.1524-4733.2010.00783.x.

32. Ramos-Goni JM, Rivero-Arias O, Errea M, Stolk EA, Herdman M, Cabases JM. Dealing with the health state ‘dead’ when using discrete choice experiments to obtain values for EQ-5D-5L heath states. Eur J Health Econ. 2013;14(Suppl. 1):S33–S42. doi: 10.1007/s10198-013-0511-2.

33. Ware JE, Jr, Sherbourne CD. The MOS 36-item short-form health survey (SF-36). I. Conceptual framework and item selection. Med Care. 1992;30:473–483. doi: 10.1097/00005650-199206000-00002.

34. Versteegh MM, Vermeulen KM, Evers SMAA, de Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level Version of EQ-5D. Value Health. 2016;19:343–352. doi: 10.1016/j.jval.2016.01.003.

35. Craig BM, Rand K. Choice defines QALYs: a US valuation of the EQ-5D-5L. Med Care. 2018;56:529–536. doi: 10.1097/MLR.0000000000000912.

36. Ramos-Goni JM, Craig BM, Oppe M, Ramallo-Farina Y, Pinto-Prades JL, Luo N, et al. Handling data quality issues to estimate the Spanish EQ-5D-5L value set using a hybrid interval regression approach. Value Health. 2018;21:596–604. doi: 10.1016/j.jval.2017.10.023.

37. Ludwig K, Graf von der Schulenburg JM, Greiner W. German value set for the EQ-5D-5L. Pharmacoeconomics. 2018;36:663–674. doi: 10.1007/s40273-018-0615-8.

38. Devlin NJ, Shah KK, Feng Y, Mulhern B, van Hout B. Valuing health-related quality of life: an EQ-5D-5L value set for England. Health Econ. 2018;27:7–22. doi: 10.1002/hec.3564.

39. Purba FD, Hunfeld JAM, Iskandarsyah A, Fitriana TS, Sadarjoen SS, Ramos-Goni JM, et al. The Indonesian EQ-5D-5L value set. Pharmacoeconomics. 2017;35:1153–1165. doi: 10.1007/s40273-017-0538-9.

40. Kruschke J. Doing Bayesian data analysis: a tutorial with R, JAGS, and Stan. 2. Oxford: Academic Press; 2014.

41. Brooks SP, Gelman A. General methods for monitoring convergence of iterative simulations. J Comput Graph Stat. 1997;7:434–455.

42. Jia YX, Cui FQ, Li L, Zhang DL, Zhang GM, Wang FZ, et al. Comparison between the EQ-5D-5L and the EQ-5D-3L in patients with hepatitis B. Qual Life Res. 2014;23:2355–2363. doi: 10.1007/s11136-014-0670-3.

43. Rand-Hendriksen K, Ramos-Goñi JM, Augestad LA, Luo N. Less is more: cross-validation testing of simplified nonlinear regression model specifications for EQ-5D-5L health state values. Value Health. 2017;20:945–952. doi: 10.1016/j.jval.2017.03.013.

44. Jakubczyk M, Craig BM, Barra M, Groothuis-Oudshoorn CGM, Hartman JD, Huynh E, et al. Choice defines value: a predictive modeling competition in health preference research. Value Health. 2018;21:229–238. doi: 10.1016/j.jval.2017.09.016.

45. Jakubczyk M, Golicki D, Niewada M. The impact of a belief in life after death on health-state preferences: true difference or artifact? Qual Life Res. 2016;25:2997–3008. doi: 10.1007/s11136-016-1356-9.

46. Bansback N, Brazier J, Tsuchiya A, Anis A. Using a discrete choice experiment to estimate health state utility values. J Health Econ. 2012;31:306–318. doi: 10.1016/j.jhealeco.2011.11.004.

47. Rand-Hendriksen K, Augestad LA, Dahl FA, Kristiansen IS, Stavem K. A shortcut to mean-based time tradeoff tariffs for the EQ-5D? Med Dec Mak. 2012;32:569–577. doi: 10.1177/0272989X11431607.

48. Hernandez Alava M, Wailoo A, Grimm S, Pudney S, Gomes M, Sadique Z, et al. EQ-5D-5L versus EQ-5D-3L: the impact on cost effectiveness in the United Kingdom. Value Health. 2018;21:49–56. doi: 10.1016/j.jval.2017.09.004.

49. Devlin N, Brazier J, Pickard AS, Stolk E. 3L, 5L, What the L? A NICE conundrum. Pharmacoeconomics. 2018;36:637–640. doi: 10.1007/s40273-018-0622-9.

50. Shiroiwa T, Ikeda S, Noto S, Igarashi A, Fukuda T, Saito S, et al. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19:648–654. doi: 10.1016/j.jval.2016.03.1834.

51. Selivanova A, Buskens E, Krabbe PFM. Head-to-head comparison of EQ-5D-3L and EQ-5D-5L health values. Pharmacoeconomics. 2018;36:715–725. doi: 10.1007/s40273-018-0647-0.

52. Augustovski F, Rey-Ares L, Irazola V, Garay OU, Gianneo O, Fernandez G, et al. An EQ-5D-5L value set based on Uruguayan population preferences. Qual Life Res. 2016;25:323–333. doi: 10.1007/s11136-015-1086-4.

53. Lam H, Purba F, Rivera A, Miguel RT, Cheng KJ. Same person, different languages, different health preferences. Discrete choice experiments (DCE) comparison from the bilinguals of the EQ-5D-5L valuation in the Philippines. In: Presented at the 35th EuroQol Group Scientific Plenary, Lisbon, 21 Sept 2018.

54. Luo N, Liu G, Li M, Guan H, Jin X, Rand-Hendriksen K. Estimating an EQ-5D-5L value set for China. Value Health. 2017;20:662–669. doi: 10.1016/j.jval.2016.11.016.

55. Wong ELY, Ramos-Goni JM, Cheung AWL, Wong AYK, Rivero-Arias O. Assessing the use of a feedback module to model EQ-5D-5L health states values in Hong Kong. Patient. 2018;11:235–247. doi: 10.1007/s40271-017-0278-0.

56. Kim SH, Ahn J, Ock M, Shin S, Park J, Luo N, et al. The EQ-5D-5L valuation study in Korea. Qual Life Res. 2016;25:1845–1852. doi: 10.1007/s11136-015-1205-2.

57. Pattanaphesaj J, Thavorncharoensap M, Ramos-Goni JM, Tongsiri S, Ingsrisawang L, Teerawattananon Y. The EQ-5D-5L valuation study in Thailand. Expert Rev Pharmacoecon Outcomes Res. 2018;18:551–558. doi: 10.1080/14737167.2018.1494574.

58. Bansback N, Hole AR, Mulhern B, Tsuchiya A. Testing a discrete choice experiment including duration to value health states for large descriptive systems: addressing design and sampling issues. Soc Sci Med. 2014;114:38–48. doi: 10.1016/j.socscimed.2014.05.026.

59. Mulhern B, Longworth L, Brazier J, Rowen D, Bansback N, Devlin N, et al. Binary choice health state valuation and mode of administration: head-to-head comparison of online and CAPI. Value Health. 2013;16:104–113. doi: 10.1016/j.jval.2012.09.001.

60. Rencz F, Gulacsi L, Drummond M, Golicki D, Prevolnik Rupel V, Simon J, et al. EQ-5D in Central and Eastern Europe: 2000–2015. Qual Life Res. 2016;25:2693–2710. doi: 10.1007/s11136-016-1375-6.

61. Dolan P. Modeling valuations for EuroQol health states. Med Care. 1997;35:1095–1108. doi: 10.1097/00005650-199711000-00002.

## Associated Data

### Supplementary Materials

<div class="caption">

ESM 1 Supplementary materials \[Word file\] (DOCX 192 kb)

</div>

<div class="caption">

ESM 2 JAGS code used for the final model estimation \[JAGS file\] (DOCX 4 kb)

</div>

<div class="caption">

ESM 3 EQ-5D-5L value set for Poland (all 3125 values) and Polish EQ-5D-5L Index calculator \[Excel file\] (XLSX 1331 kb)

</div>

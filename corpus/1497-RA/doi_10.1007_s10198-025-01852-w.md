---
project_id: "1497-RA"
work_id: "doi:10.1007/s10198-025-01852-w"
doi: "10.1007/s10198-025-01852-w"
pmid: "41160306"
pmcid: "PMC13190540"
title: "Do EQ-5D-Y-3L value sets have common properties, and how do they compare to EQ-5D-5L value sets?"
journal: "The European Journal of Health Economics"
publication_date: "2025-10-29"
volume: "27"
issue: "3"
authors:
  - name: "Bram Roudijk"
    orcid: "http://orcid.org/0000-0001-5000-0875"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Tianxin Pan"
    affiliation_ids:
      - "Aff3"
  - name: "Jan Abel Olsen"
    affiliation_ids:
      - "Aff4"
  - name: "Nancy Devlin"
    affiliation_ids:
      - "Aff3"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/01mrvqn21grid.478988.20000 0004 5906 3508EuroQol Research Foundation, Marten Meesweg 107, Rotterdam, 3068 AV The Netherlands"
  - id: "Aff2"
    name: "https://ror.org/018906e22grid.5645.20000 0004 0459 992XDepartment of Psychiatry, Erasmus University Medical Center, Rotterdam, Netherlands"
  - id: "Aff3"
    name: "https://ror.org/01ej9dk98grid.1008.90000 0001 2179 088XCentre for Health Policy, Melbourne School of Population and Global Health, University of Melbourne, Melbourne, Australia"
  - id: "Aff4"
    name: "https://ror.org/00wge5k78grid.10919.300000 0001 2259 5234Department of Community Medicine, UiT - The Arctic University of Norway, Tromsø, Norway"
keywords:
  - "Comparison"
  - "EQ-5D-5L"
  - "EQ-5D-Y-3L"
  - "Paediatric HRQoL"
  - "Paediatric QALYs"
  - "Tariff"
  - "Utilities"
  - "Valuation"
  - "Value sets"
licence: "cc-by-nc-nd"
source_file: "input/projects/1497-RA/papers/doi_10.1007_s10198-025-01852-w.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13190540/fullTextXML"
source_method: "epmc_xml"
source_sha256: "b5bdef93161e84399a8d524d5f6df482dfa2c199b4ccc2d7d974c38d5dcfe86f"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Do EQ-5D-Y-3L value sets have common properties, and how do they compare to EQ-5D-5L value sets?

## Abstract

### Background

Since the introduction of the EQ-5D-Y-3L valuation protocol, a considerable number of EQ-5D-Y-3L value sets have been published. This provides an opportunity to explore the differences and similarities between EQ-5D-Y-3L value sets across countries, and their similarity to their EQ-5D-5L counterparts.

### Methods

EQ-5D-Y-3L value set publications for 11 countries identified key methodological, sampling and value set characteristics. Similarity between value sets was assessed using kernel density plots and other key characteristics. Preference patterns between groups of value sets were explored. EQ-5D-Y-3L value set properties were compared with those of EQ-5D-5L value sets from the same country.

### Results

All EQ-5D-Y-3L valuation studies used the same DCE design. Six studies used expanded health state designs in the composite Time Trade Off. Analytical strategies differed between studies. Values for state 33333 ranged from − 0.691 (Slovenia) to 0.289 (Japan); the number of negative values ranged from 0 to 21%. Pain/discomfort level 3 received the largest weight in all EQ-5D-Y-3L studies, while self-care level 3 received the smallest weight in 8 out of 11 studies. Similarities were found between European value sets, and between Asian value sets. Value sets for Australia and Brazil had similar scale lengths as the Asian value sets, but differed in other ways.

### Discussion

Although substantial differences were observed between EQ-5D-Y-3L value sets (e.g. regarding the length of the value scale), striking similarities between them existed (e.g. pain/discomfort consistently received the largest weight). Comparing EQ-5D-Y-3L value sets to EQ-5D-5L values generally suggests less willingness to trade life years for life quality for children.

## Introduction

The EQ-5D-Y-3L was introduced in 2010 as a child-friendly version of the EQ-5D-L, aimed at measuring health-related quality of life (HRQoL) in paediatric populations \[1\]. Whereas the EQ-5D-3L (and EQ-5D-5L) focus on measuring HRQoL in adult populations, the EQ-5D-Y-3L is aimed at children and adolescents aged 8 to 15 years old and has been shown to have good psychometric properties in this age group \[2, 3\]. As with other EQ-5D instruments, the EQ-5D-Y-3L is accompanied by value sets, which allow researchers to assign value to profiles to summarize how good or bad a health state is using a single value, based on the preferences of the general population. These value sets can then be utilized for the computation of utilities, which can be used as inputs in economic models to assess Quality Adjusted Life Years (QALYs) gained.

Value sets for the EQ-5D-3L and EQ-5D-5L instruments have been around for a long time (e.g. the MVH study \[4\]), but value sets for paediatric HRQoL instruments are a more recent development. Although the EQ-5D-Y-3L and adult EQ-5D instruments aim to measure the same constructs in two different populations, their descriptive systems are somewhat different, reflecting the fact that the EQ-5D-Y-3L was adapted from the EQ-5D-3L to be appropriate for children. Furthermore, it has been shown that adults’ preferences for children’s health states differ from preferences for the health states of adults \[5\]. These observations led to the development of a protocol to estimate value sets for the EQ-5D-Y-3L (Ramos-Goñi et al. 2020) \[6\]. In this protocol, adult members of the general public complete valuation tasks in which they indicate what they would prefer for a hypothetical 10-year-old child. Two samples are collected: (1) a sample of 1000 respondents, each completing a set of discrete choice tasks (DCE) online, and (2) a sample of around 200 respondents, each completing a set of composite Time Trade-Off tasks (cTTO) in face to face interviews \[7\]. The DCE data are then modelled and anchored on the 0 (dead) to 1 (full health) scale to produce values usable for QALY computations.

Following publication of the valuation protocol for the EQ-5D-Y-3L \[6\], there was considerable interest in undertaking EQ-5D-Y-3L value set studies and rapid development of value sets \[8\]. To date, eleven value sets for the EQ-5D-Y-3L using that protocol have been published for Australia, Belgium, Brazil, China, Germany, Hungary, Indonesia, Japan, the Netherlands, Slovenia and Spain \[9–19\]. More value sets are expected to be published within the coming years.

The EQ-5D-Y-3L protocol sets out minimum requirements for valuation studies, which means that there is some variation in the methods used to generate these value sets \[20\]. This includes differences in how the cTTO data were used to anchor the DCE data to the QALY scale. Different anchoring strategies have been shown to affect the length of the scale for the final value set, thereby influencing the values for all health states \[21\]. This is considered to be one of the remaining challenges in valuing EQ-5D-Y-3L, reflecting a lack of consensus on which scaling approach is the best \[8\].

Value sets for the EQ-5D-3L and EQ-5D-5L instruments are known to differ substantially between countries \[22\]. While there is no evidence that the rate at which respondents trade quality of life for quantity of life differs systematically between countries, evidence exists that the relative importance of the EQ-5D dimensions is related to national culture \[22, 23\]. Several studies have sought to compare value sets between countries, to test whether countries that share similar geographic and societal characteristics also have similar properties in national value sets for the EQ-5D-5L (e.g. Olsen et al., 2018 and Roudijk, Janssen & Olsen, 2022) \[24, 25\]. As EQ-5D-Y-3L value sets have been developed relatively recently, no such comparison between these value sets has been reported to date. Such a comparison is useful to learn more about whether and how value sets for the EQ-5D-Y-3L differ between countries and learn about implications for their use in QALY estimation. It can also help to identify whether variations in methods lead to differences in values.

Furthermore, no comparison has been made between existing value sets for the adult EQ-5D instrument and the EQ-5D-Y-3L value sets. Notwithstanding differences in the descriptive system and in the methods used to elicit the preferences on which the value sets are based, it is relevant to draw comparisons. The comparison between value sets for the adult EQ-5D versions and the EQ-5D-Y-3L allows us to explore differences between these value sets, providing information on the consistency of values when estimating QALYs in economic models involving mixed-age populations i.e., including both children/adolescents and adults. While the EQ-5D-3 L has the same number of levels as the EQ-5D-Y-3L, the EQ-5D-5L is much more widely used to measure adult HRQoL than the EQ-5D-3L, because of its known psychometric advantages \[26\], and because value sets for it have been produced using a standardized protocol and reflect contemporary preferences \[27\]. Thus, users of value sets interested in knowing how adult and child value sets compare (e.g. in economic evaluation models that involve transitions from child to adult health states) are most likely to be interested in the EQ-5D-5L and EQ-5D-Y-3L value sets. Discrepancy between the adult EQ-5D-5L and EQ-5D-Y-3L value sets may be problematic for applications such as health technology assessment (HTA), where cost-utility analyses may cover lifespans that include both childhood and adulthood, and where both EQ-5D-Y-3L and EQ-5D-5L-based utilities may be required. Therefore it is important that these differences are investigated \[20, 28\].

This study aims to address these gaps in the literature by (a) systematically comparing the characteristics and properties of EQ-5D-Y-3L value sets between countries, and (b) comparing the value sets for the EQ-5D-Y-3L with existing value sets for the adult EQ-5D-5L instrument in countries where both are now available. Specifically, we explore the following research questions: to what extent do EQ-5D-Y-3L value sets share common characteristics? Are observed differences between value sets linked to regional/cultural characteristics and the approaches taken to develop the value set? Are there any common preference patterns in EQ-5D-Y-3L value sets? And, to what extent do we observe common characteristics between EQ-5D-Y-3L value sets, and value sets for the EQ-5D-5L?

## Methods

### General approach

As noted above, this study had two aims, and methods are described here for each. First, we extracted the value set al.gorithms for all published value sets for the EQ-5D-Y-3L. The following countries have a published value set for the EQ-5D-Y-3L: Australia, Belgium, Brazil, China, Germany, Hungary, Indonesia, Japan, the Netherlands, Slovenia, and Spain \[9–19\]. Key information around the methods of the valuation study was extracted from the respective manuscripts, and reported as an overview, to facilitate comparisons between countries. We applied each value set to the full set of 243 EQ-5D-Y-3L health states, such that we had a dataset of 243 observations, representing each of the 243 possible health states and their corresponding values according to the different value sets. Several analyses were performed in which key characteristics of EQ-5D-Y-3L and EQ-5D-5L value sets were compared, for those countries in which both an EQ-5D-Y-3L and an EQ-5D-5L value set was available. Algorithms were extracted from published manuscripts (Australia, Belgium, China, Germany, Hungary, Indonesia, Japan, Netherlands, Slovenia, Spain) \[29–38\]. These value sets were applied to a dataset comprising all 3125 possible EQ-5D-5L health states. Subsequently, analyses were conducted to compare the EQ-5D-Y-3L and EQ-5D-5L value sets, again to assess key characteristics of the value sets.

### Comparing EQ-5D-Y-3L value sets

As outlined above, an overview of the methods used in each of the published value sets for EQ-5D-Y-3L was provided. This overview included the number of respondents allocated to each of the two choice tasks, the number of health states included in the health state design for the cTTO tasks, the anchoring strategy, and the final model used as the value set.

We extracted key characteristics of the values produced by the value set al.gorithms, including the range of values (scale length), the median value, the number of unique values, the number and percentage of negative values, and the relative importance of the dimensions of the EQ-5D-Y-3L. Relative importance was assessed by examining the weight assigned to having level 3 problems for each dimension, similarly to Roudijk, Olsen & Janssen (2022) \[25\]. The level-dimension weights reflect the average value assigned to the most severe health problems by the respondents. Larger weights were assumed to be more important than smaller weights. Therefore, the ordering of these coefficients is considered as the relative importance of the dimensions.

In addition, we examined the distribution of values over the scale. First, we looked at the linearity/nonlinearity of the decrement of the weights of health worsening from level 1 to level 2, versus level 2 to level 3 on each of the dimensions, by plotting the decrements for each level-dimension combination for each country. Furthermore, we plotted the distribution of values over the value scale using kernel density plots for each value set. Kernel density plots allow for a visualization of the probability density of a continuous variable, requiring no assumption of the functional form of the distribution of that variable \[39\]. Since EQ-5D-Y-3L value sets have a large number of unique values, kernel density plots provided a better visual representation of the distribution of values as compared to histograms. Lastly, we calculated the relative position of state 22,222 against the scale length, to gauge the location of the descriptive midpoint of the EQ-5D-Y-3L descriptive system on the value scale.

We explored the possibility of identifying common EQ-5D-Y-3L preference patterns among sub-sets of studies following the methods used by Olsen et al. (2018) and Roudijk, Janssen and Olsen (2022) \[24, 25\]. We compared whether the functioning domains (mobility (MO), looking after myself (LAM) and Usual activities (UA)) received approximately the same combined weight as the weights for the symptoms domains (pain/discomfort (PD), feeling worried, sad or unhappy (WSU)) combined. Furthermore, we checked whether PD received a larger weight than WSU and the difference being at least 0.05; and whether WSU received a larger weight than MO, with a difference of at least 0.05.[^1] Similarly, we checked whether MO received a larger value than UA, with a difference of at least 0.03, as well as whether MO received a larger weight than LAM, with a difference of at least 0.03.[^2] The latter 4 criteria were adapted from the criteria by Olsen et al., to be more applicable to the EQ-5D-Y-3L value sets, as the scales for the EQ-5D-Y-3L value sets tended to be smaller, and the relative importance of dimensions to be more similar between value sets. Furthermore, we checked whether the difference between levels 1 and 2 is smaller or larger than the difference between levels 2 and 3 for each country; we checked whether the values for the mildest health states (21111, 12111, 11211, 11121 and 11112) received a value smaller or larger than 0.9; whether state 22222 fell in the \[0.4,0.6\] interval; and lastly, whether state 33333 received a value smaller than − 0.2. Value sets for countries sharing geographical characteristics were compared on these characteristics. If a set of countries sharing geographical characteristics also shared a large number of these characteristics, we assumed that these countries share a common preference pattern. We then generated an “aggregate preference pattern”, by taking the mean of the values for each health state for the countries included in that aggregate preference pattern, which then represented the average preference for a larger set of countries that shared a number of characteristics. Since 9 out of the 11 available values sets are from Asian and European countries, we focused on aggregate preference patterns for Europe and Asia. Performance of these aggregate preference patterns was tested by comparing their kernel densities and calculating the absolute error of the aggregate and individual value sets.

### Comparing EQ-5D-Y-3L and EQ-5D-5L value sets

To compare existing EQ-5D-Y-3L and EQ-5D-5L value sets, we calculated the scale lengths and number/percentage of negative values for both instruments to see how they compared within countries. Furthermore, we compared the ordering of importance of the dimensions between the EQ-5D-5L and EQ-5D-Y-3L value sets for those countries where both EQ-5D-Y-3L and EQ-5D-5L value sets were available. Lastly, we compared how the health states were distributed over the value scale using kernel density plots, and by comparing the location of the descriptive midpoint on the value scale (i.e., the relative location of 22222 in the EQ-5D-Y-3L, and 33333 for the EQ-5D-5L).

## Results

### Study characteristics of included value sets

Although a standardized protocol exists for valuing EQ-5D-Y-3L, methodological differences may still exist between value set studies. Table <a href="#Tab1" data-ref-type="table">1</a> reports key characteristics of each of the included EQ-5D-Y-3L value set studies. Each study collected roughly 1000 respondents for the DCE tasks, and 200 respondents for the cTTO tasks. Exceptions were Japan, (where the full sample of 1047 respondents completed both cTTO and DCE), China and Australia, where a larger sample completed the cTTO tasks (418 and 268 respondents respectively). Five studies used the 10 cTTO health states specified in the protocol, and another six studies used different designs, comprising between 23 and 52 unique health states per study \[9, 11, 15, 17\]. Seven studies modelled the DCE data using a mixed logit model, two studies used a latent class model, one study used a garbage-class mixed logit model and one study used a hybrid model to model the DCE and cTTO data jointly. Of the ten studies that modelled the DCE data in isolation, seven used a mapping approach to anchor the latent DCE values on the QALY scale, while the other three studies anchored the DCE values on the censoring-adjusted cTTO mean for state 33333.

<div id="Tab1" class="table-wrap">

<div class="caption">

Summary of EQ-5D-Y-3L value set study design and methods

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Country</th>
<th style="text-align: left;">Respondents</th>
<th style="text-align: left;">TTO health states selection</th>
<th style="text-align: left;">How are values anchored?</th>
<th style="text-align: left;">Final model</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>Belgium</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 972</p>
<p>TTO: <em>N</em> = 200</p></td>
<td style="text-align: left;">10 Health states in the protocol:</td>
<td style="text-align: left;">Rescaling based on the single state “33333” (censoring adjusted value)</td>
<td style="text-align: left;">DCE: latent class model with 4 classes;</td>
</tr>
<tr>
<td style="text-align: left;"><em>Germany</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 1030</p>
<p>TTO: <em>N</em> = 215</p></td>
<td style="text-align: left;">10 Health states in the protocol</td>
<td style="text-align: left;">Mapping DCE data onto the cTTO data</td>
<td style="text-align: left;"><p>DCE: mixed logit</p>
<p>OLS mapping without intercept</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Hungary</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 996</p>
<p>TTO: <em>N</em> = 200</p></td>
<td style="text-align: left;">10 Health states in the protocol</td>
<td style="text-align: left;">Mapping DCE data onto the cTTO data</td>
<td style="text-align: left;"><p>DCE: mixed logit</p>
<p>OLS mapping without intercept</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Netherlands</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 959</p>
<p>TTO: <em>N</em> = 197</p></td>
<td style="text-align: left;">28 Health states: an orthogonal design of 18 health state + 10 health states consisting of 5 mild health states (21111, 12111,11211,11121,111112), 33333 and four intermediate health states</td>
<td style="text-align: left;">Mapping DCE data onto cTTO data.</td>
<td style="text-align: left;"><p>DCE: mixed logit</p>
<p>OLS mapping without intercept</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Slovenia</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 1074</p>
<p>TTO: <em>N</em> = 202</p></td>
<td style="text-align: left;">10 Health states in the protocol:</td>
<td style="text-align: left;">Rescaling based on the single state “33333” (censoring adjusted value)</td>
<td style="text-align: left;">DCE: mixed logit</td>
</tr>
<tr>
<td style="text-align: left;"><em>Spain</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 1005</p>
<p>TTO: <em>N</em> = 200</p></td>
<td style="text-align: left;">10 Health states in the protocol: mild, 11112, 11121, 21111; moderate, 22223, 22232; and severe, 31133, 32223, 33233, 33323, 33333</td>
<td style="text-align: left;">Rescaling based on the single state “33333” (censoring adjusted value)</td>
<td style="text-align: left;">DCE: latent class model with 4 classes;</td>
</tr>
<tr>
<td style="text-align: left;"><em>China (Mainland)</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 1058</p>
<p>TTO: <em>N</em> = 418</p></td>
<td style="text-align: left;">28 Health states: original cTTO design of 10 health states with an orthogonal design of 18 health state</td>
<td style="text-align: left;">‘Hybrid’ modelling DCE and cTTO data (accounting for heteroscedasticity) jointly</td>
<td style="text-align: left;">hybrid model with the A3 term (gap between state 33333 and other states</td>
</tr>
<tr>
<td style="text-align: left;"><em>Indonesia</em></td>
<td style="text-align: left;"><p>DCE (face-to-face): <em>N</em> = 1072</p>
<p>TTO: <em>N</em> = 222</p></td>
<td style="text-align: left;"><p>23 Health states</p>
<p>(an orthogonal design of 18 health state + 2 severe health states 33332, 32232 + 5 of the 10 suggested states but 2 were overlap)</p></td>
<td style="text-align: left;">Mapping DCE data onto the cTTO data</td>
<td style="text-align: left;"><p>DCE: mixed logit</p>
<p>Non-linear mapping (power without constant)</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Japan</em></td>
<td style="text-align: left;"><p><em>N</em> = 1047</p>
<p>Same sample completed cTTO then DCE tasks in face-to-face interviews</p></td>
<td style="text-align: left;">26 Health states: an orthogonal design of 18 health state + 5 mild states + 3 other states; five blocks each with six health states;</td>
<td style="text-align: left;">Mapping DCE data onto the cTTO data (censoring adjusted value)</td>
<td style="text-align: left;"><p>DCE: mixed logit</p>
<p>OLS mapping with intercept</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Brazil</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 1152</p>
<p>TTO: <em>N</em> = 211</p></td>
<td style="text-align: left;">28 Health states: an orthogonal design of 18 health state + 10 health states consisting of 5 mild health states (21111, 12111,11211,11121,111112), 33333 and four intermediate health states</td>
<td style="text-align: left;">Mapping DCE data onto cTTO data.</td>
<td style="text-align: left;"><p>DCE: mixed logit</p>
<p>OLS mapping without intercept</p></td>
</tr>
<tr>
<td style="text-align: left;"><em>Australia</em></td>
<td style="text-align: left;"><p>DCE: <em>N</em> = 1002</p>
<p>TTO: <em>N</em> = 268</p></td>
<td style="text-align: left;">50 health states from an orthogonal array, complemented with state 33333 and state 22222. Each respondent completed 13 cTTO tasks, including 33333.</td>
<td style="text-align: left;">Mapping DCE data onto cTTO data.</td>
<td style="text-align: left;"><p>DCE: garbage class mixed logit</p>
<p>OLS mapping without intercept</p></td>
</tr>
</tbody>
</table>

</div>

### Distribution of values, scale length and dimension importance

The distribution of values, scale length and dimension importance were compared between value sets. Figure <a href="#Fig1" data-ref-type="fig">1</a> reports the kernel distribution plots of the EQ-5D-Y-3L and EQ-5D-5L value sets for each country.[^3] The studies for the six European countries Belgium, Germany, Hungary, the Netherlands, Slovenia and Spain reported “flatter” distributions of EQ-5D-Y-3L values compared to the studies for the three Asian countries (China, Indonesia and Japan) as well as Australia, indicating that in the European studies the values were distributed more evenly over a wider interval. This was also reflected in the scale range and percentage of negative values for each health state in the EQ-5D-Y-3L value sets, as reported in Table <a href="#Tab2" data-ref-type="table">2</a>. The Slovenian study showed the largest scale range, with − 0.691 for the worst health state and 1 for full health, while Japan showed the smallest scale range with 0.289 for the worst health state and 1 for perfect health, i.e. a difference in value of 0.980 for the worst health state between these studies. The studies for China, Indonesia, Australia, Brazil and Japan reported 0% to 0.4% of values being negative, while this ranged between 3.3% and 20.6% for the other six studies. PD was the most important dimension in all 11 studies, followed by WSU or MO, while LAM was the least important dimension in most studies (the exceptions being Germany, Australia and Brazil). However, all studies except the Brazilian study reported state 12111, with some problems on LAM, to be the health state with the highest value after state 11111. State 22222 was placed between 23.7% and 49.6% of the value scale, indicating that the difference between “some problems” and “a lot of problems” was larger than the difference between “no problems” and “some problems”, for all studies included in our analysis. Figure <a href="#Fig2" data-ref-type="fig">2</a> shows the utility decrements associated with moving from one level to the other for each dimension of the EQ-5D-Y-3L for each country. Most studies reported larger decrements for moving from level 2 to level 3 on each dimension, with the exception of Japan, Brazil and Indonesia Table <a href="#Tab3" data-ref-type="table">3</a>.

<figure id="Fig1">
<p><img src="10198_2025_1852_Fig1_HTML.jpg" id="d33e708" /></p>
<figcaption>Kernel density distributions for all EQ-5D-Y-3L value sets and corresponding EQ-5D-5L value sets</figcaption>
</figure>

<div id="Tab2" class="table-wrap">

<div class="caption">

Value characteristics and relative importance of dimensions in the EQ-5D-Y-3L

</div>

|  | Belgium | Germany | Hungary | Netherlands | Slovenia | Spain | China | Indonesia | Japan | Brazil | Australia |
|----|----|----|----|----|----|----|----|----|----|----|----|
| Range | \[−0.475,1\] | \[−0.2827, 1\] | \[−0.485, 1\] | \[−0.218,1\] | \[−0.691, 1\] | \[−0.5392, 1\] | \[−0.089,1\] | \[−0.0861,1\] | \[0.289, 1\] | \[−0.0059,1\] | \[0.142,1\] |
| Median | 0.362 | 0.4531 | 0.398 | 0.498 | 0.27 | 0.3169 | 0.613 | 0.662 | 0.687 | 0.499 | 0.609 |
| \# of health states worse than dead | 31 | 16 | 30 | 8 | 50 | 39 | 1 | 1 | 0 | 1 | 0 |
| % of health states worse than dead | 12.8% | 6.6% | 12.4% | 3.3% | 20.6% | 16.1% | 0.4% | 0.4% | 0.00% | 0.4% | 0.00% |
| Number of unique value | 206 | 243 | 218 | 212 | 224 | 243 | 219 | 234 | 185 | 242 | 204 |
| Dimension importance order <sup>b</sup> | PD | PD | PD | PD | PD | PD | PD | PD | PD | PD | PD |
|  | AD | AD | AD | AD | AD | AD | MO | MO | AD | MO | AD |
|  | UA | UA | MO | UA | UA | MO | AD | UA | UA | SC | UA |
|  | MO | SC | UA | MO | MO | UA | UA | AD | MO | UA | SC |
|  | SC | MO | SC | SC | SC | SC | SC | SC | SC | AD | MO |
| V(21111) | 0.936 | 0.9758 | 0.946 | 0.964 | 0.917 | 0.8960 | 0.938 | 0.979 | 0.935 | 0.875 | 0.975 |
| V(12111) | 0.954 | 0.9809 | 0.962 | 0.972 | 0.954 | 0.9487 | 0.977 | 0.987 | 0.957 | 0.897 | 0.977 |
| V(11211) | 0.896 | 0.9163 | 0.922 | 0.942 | 0.894 | 0.8998 | 0.942 | 0.975 | 0.937 | 0.897 | 0.948 |
| V(11121) | 0.843 | 0.8663 | 0.867 | 0.889 | 0.838 | 0.8281 | 0.91 | 0.980 | 0.898 | 0.891 | 0.877 |
| V(11112) | 0.895 | 0.8746 | 0.917 | 0.904 | 0.883 | 0.8856 | 0.927 | 0.979 | 0.926 | 0.939 | 0.903 |
| Value 22222 | 0.524 | 0.6139 | 0.614 | 0.671 | 0.486 | 0.4582 | 0.742 | 0.583 | 0.753 | 0.499 | 0.68 |
| As % of scale length | 32.2% | 30.1% | 26% | 27.0% | 30.4% | 35.2% | 23.7% | 38.4% | 34.7% | 49.6% | 37.3% |

</div>

<figure id="Fig2">
<p><img src="10198_2025_1852_Fig2_HTML.jpg" id="d33e1208" /></p>
<figcaption>Changes in EQ-5D-Y-3L utilities between levels for each dimension</figcaption>
</figure>

<div id="Tab3" class="table-wrap">

<div class="caption">

Extracting some key characteristics from each country’s value set in the EQ-5D-Y-3L

</div>

|  | Belgium | Germany | Hungary | Netherlands | Slovenia | Spain | China | Indonesia | Japan | Brazil | Australia |
|----|----|----|----|----|----|----|----|----|----|----|----|
| **Dimensions; relative importance** |  |  |  |  |  |  |  |  |  |  |  |
| (PD + WSU)-(MO + LAM + UA) |  |  |  |  | X | X | X |  |  |  |  |
| PD-WSU (diff \> 0.05) | X | X | X |  | X | X |  | X |  | X |  |
| WSU-MO (diff \> 0.05) | X | X |  | X | X |  | X | X |  | X | X |
| MO -UA (diff \< 0.03) |  |  | X | X | X | X | X | X | X | X | X |
| MO -LAM (diff \< 0.03) | X | X |  |  |  |  |  |  | X | X |  |
| **Levels; characteristics of the scale** |  |  |  |  |  |  |  |  |  |  |  |
| Kink at Level 2 in all dimensions? | X | X | X | X | X | X |  |  | X |  | X |
| Scale value ranges |  |  |  |  |  |  |  |  |  |  |  |
| 21111 \< 0.9 |  |  |  |  |  | X |  |  |  | X |  |
| 12111 \< 0.9 |  |  |  |  |  |  |  |  |  | X |  |
| 11211 \< 0.9 | X |  |  |  | X | X |  |  |  | X |  |
| 11121 \< 0.9 | X | X | X | X | X | X |  |  | X | X | X |
| 11112 \< 0.9 | X | X |  |  | X | X |  |  |  |  |  |
| 22222 \[0.4, 0.6\] | X | \(X\) | \(X\) |  | X | X |  | X |  | X |  |
| 33333 \<−0.2 | X | X | X | X | X | X |  |  |  |  |  |

</div>

### Preference pattern criteria

Olsen et al. (2018) and Roudijk et al. (2022) set a number of characteristics which were used to generate aggregate preference patterns \[24, 25\]. Table <a href="#Tab4" data-ref-type="table">4</a> reports these characteristics and how value sets score on each of these. All European value sets reported a value lower than − 0.2 for 33333, while all Asian value sets reported a value higher than − 0.2 for 33,333. Furthermore, the descriptive midpoint 22,222 lay in the interval \[0.4,0.6\] for each European country except the Netherlands. Out of the Asian studies, only Indonesia had a value for 22222 in the \[0.4,0.6\] interval, while Japan and China reported values larger than 0.6 for state 22222. Australia also reported a value larger than 0.6 for 22222, while for Brazil, the value was close to 0.5.

<div id="Tab4" class="table-wrap">

<div class="caption">

Characteristics of EQ-5D-5L value sets in countries that also have EQ-5D-Y-3L value sets

</div>

|  | Belgium | Germany | Hungary | Netherlands | Slovenia | Spain | China | Indonesia | Japan | Australia |
|----|----|----|----|----|----|----|----|----|----|----|
| Negative values (%) | 12.8% | 15.1% | 21.7% | 15.5% | 32.2% | 8.3% | 10.2% | 35.5% | 0.1% | 9.0% |
| Range | \[−0.475,1\] | \[−0.661,1\] | \[−0.848,1\] | \[−0.446,1\] | \[−1.089,1\] | \[−0.415,1\] | \[−0.344,1\] | \[−0.865,1\] | \[−0.026,1\] | \[−0.301,1\] |
| Dimension ranking | PD | PD | MO | AD | PD | PD | MO | MO | MO | PD |
|  | AD | AD | PD | PD | AD | AD | PD | UA | AD | MO |
|  | MO | SC | SC | MO | MO | MO | AD | SC | PD | AD |
|  | UA | MO | AD | UA | UA | SC | SC | AD | UA | SC |
|  | SC | UA | UA | SC | SC | UA | UA | PD | SC | UA |

</div>

In the Slovenian, Spanish and Chinese value sets, the sum of the weights for the symptom dimensions (PD and WSU) received a similar weight to the sum of the weights for the functioning dimensions (MO, LAM and UA), while for the other value sets one of the two received a substantially larger weight. When concerning PD or WSU, studies for European countries showed values smaller than 0.9 for the mildest states in most cases, while this was only the case for Japan for PD among the three Asian countries. MO received a similar weight to LAM in Belgium, Germany and Japan, while PD was similar to WSU in Germany, the Netherlands and Indonesia. Furthermore, European value sets showed larger decrements when moving from level 2 to 3, as compared to level 1 to 2, while this was more linear for the Asian value sets, except China. All in all, the European value sets shared at least 5 similar characteristics. The Australian value set shared only 4 of these characteristics, while the value set for Brazil shared 9.

### Aggregate preference patterns

Two aggregate preference patterns were developed based on the adapted Olsen et al. criteria; one for Asia (based on the mean of the values for each health state in the Chinese, Indonesian and Japanese value sets), and one for Europe (based on the mean of the values for each health state in the Belgian, German, Hungarian, Dutch, Slovenian and Spanish value sets). The associated values can be found in Table <a href="#Tab5" data-ref-type="table">5</a> of the Appendix.[^4] For both aggregate preference patterns, PD was the most important dimension. The scale length for the European preference pattern ranged \[−0.448,1\], while that of the Asian preference pattern ranged \[0.038,1\].

Figures <a href="#Fig3" data-ref-type="fig">3</a> shows the kernel density distributions of the European and Asian preference patterns for the EQ-5D-Y-3L, as well as for Australia and Brazil (for which the Asian preference pattern is presented as a comparator). The Asian preference pattern seemed to fit well, which is illustrated by small Mean Absolute Error (MAE) when comparing them to the Chinese, Indonesian and Japanese value sets (0.041, 0.053 and 0.051 respectively). The European preference pattern was more mixed, with a good fit for Belgium, Germany, Hungary and Spain, and poorer fit for the Netherlands and Slovenia, as indicated by the MAE (0.0264, 0.077, 0.025, 0.065, 0.113 and 0.106 respectively).

<figure id="Fig3">
<p><img src="10198_2025_1852_Fig3_HTML.jpg" id="d33e1821" /></p>
<figcaption>Kernel density plots of the EQ-5D-Y-3L European preference pattern and Asian preference pattern versus the value sets they represent, and for the other 2 value sets</figcaption>
</figure>

### Comparison of EQ-5D-Y-3L and EQ-5D-5L value sets

Lastly, Table <a href="#Tab4" data-ref-type="table">4</a> reports key characteristics of the EQ-5D-5L value sets: the percentage of negative values, the scale length, and the ordering of dimensions. PD was the most important dimension in Belgium, Germany, Spain, Slovenia and Australia, while anxiety/depression (AD) was most important in the Netherlands. MO was the most important dimension in China, Indonesia and Japan. EQ-5D-5L value scale length ranged from 2.089 in Slovenia, to 1.026 in Japan. Indonesia had the most health states with a negative value at 35.46%, while in Japan, just 0.1% of values were negative. In most European value sets, the percentage of negative values was between 10% and 20%, with Slovenia reporting substantially more negative values at 32%, and Spain reporting fewer at 8.26%.

Figure <a href="#Fig1" data-ref-type="fig">1</a> also shows the kernel distributions for the EQ-5D-5L value sets for each country. In some value sets, such as those of Belgium, Germany, Hungary, Spain and Slovenia, the distribution of values was broadly similar between the EQ-5D-Y-3L and EQ-5D-5L. For the Netherlands, China, Indonesia, Australia and Japan, there were differences in the distributions of values between the adult and youth instruments, with these differences being much larger in China, Indonesia, Australia and Japan. These differences in distributions seemed to reflect differences in scale lengths and the number of negative values.

## Discussion

Substantial differences were found between the EQ-5D-Y-3L value sets. For example, the value assigned to the worst health state, 33333, differed considerably, with the Japanese value set scoring this state at 0.289, while it received a value of −0.691 in the Slovenian value set. Consequentially, the number of negative values also differed between value sets, with 20.58% of values being negative in the Slovenian value set, and no negative values existing in the Japanese and Australian value sets. However, notwithstanding these substantial variations in scale length, similarities also existed. Notably, PD was always the most important dimension in each of the published EQ-5D-Y-3L value sets, while LAM received the lowest weight in each country except for Germany, Australia and Brazil.

It was feasible to generate aggregate preference patterns for the EQ-5D-Y-3L for Europe, as the six European value sets shared similar characteristics \[24, 25\]. Similarly, the three Asian value sets shared similar characteristics, and an aggregate preference pattern was developed. The Asian preference pattern seemed to fit well to each of the included value sets. The European preference pattern did not seem to fit as well for the Netherlands and Slovenia, as compared to the other four included value sets, mainly due to the difference in scale length. For both the Asian as well as the European preference patterns, the fit for severe health states was considerably poorer than for the milder health states. The Australian and Brazilian value sets were not considered for aggregate preference patterns, as there were no other value sets for countries which shared similar regional/cultural characteristics, as well as sharing characteristics of the value sets.

Substantial differences were found between EQ-5D-Y-3L and EQ-5D-5L value sets. For some countries, the order of importance of the dimensions was different in the EQ-5D-Y-3L, as compared to the EQ-5D-5L. Furthermore, substantial differences in scale were found for some value sets, such as the Indonesian, where the lowest value assigned to any health state was − 0.865 for the EQ-5D-5L, but only − 0.0861 in the EQ-5D-Y-3L. Consequently, 35.46% of values were negative for the EQ-5D-5L in Indonesia, while only 0.41% of values were negative in the EQ-5D-Y-3L. Similar but less extreme differences were observed for most other value sets.

Several factors may explain differences and similarities between EQ-5D-Y-3L value sets. First there are methodological differences, as outlined in Table <a href="#Tab1" data-ref-type="table">1</a>. Three studies rescaled their DCE estimates for the EQ-5D-Y-3L using the cTTO value for state 33333; Belgium, Slovenia and Spain. These are also the studies that report the lowest value for state 33333, and have more mild health states (e.g. only one dimension reports level 2 problems) with values lower than 0.9, suggesting the possibility that the scale length may be longer when using this strategy to anchor the DCE values onto the QALY scale. This confirms the findings of Mott et al., who explored different anchoring strategies using a multi-country sample of respondents from England, Germany, Spain and the Netherlands \[21\]. Studies that use larger cTTO health state designs also more frequently use mapping or hybrid models to anchor the DCE estimates on the health-utility scale. These studies also tend to have a shorter scale range on average, which could suggest that the set of included health states or modelling method affects the estimated scale range. Specifically anchoring on the mean cTTO value for 33333 could have an impact. However, this would require further research to test formally.

Another source of differences between value sets could be differences in cultural values. Bailey & Kind (2010) showed that for EQ-5D-3L value sets, the relative importance of EQ-5D-3L dimensions is related to the cultural dimensions of defined by Hofstede et al. \[23, 40\]. This suggests that at least some part of differences in values between studies can be explained by differences in culture, and this is possibly also the case for EQ-5D-Y-L value sets. However, Roudijk et al. did not find any relation between cultural values and the rate at which respondents trade life years to avoid poor health for the EQ-5D-3L and EQ-5D-5L instruments, suggesting that the scale length may not be dependent on cultural values, but on other factors \[22\]. Either way, the fact that we were able to define aggregate preference patterns for two geographical regions, using a small number of value sets, suggests further research into the relationship between cultural values and EQ-5D-Y-3L value sets may be of interest. The observed unwillingness to trade life years in children in some studies and views on children’s resilience to health problems may be culturally dependent - although it is possible that they are dependent on other factors, such as life expectancy and child mortality rates. Furthermore, other country-level factors, such as the translations of the severity labels may also play a relevant role in understanding differences between value sets, and could potentially explain differences in scale length.

Whereas the ordering of dimensions in the EQ-5D-Y-3L shows a lot of similarity between value sets, scale length seems to be the principal factor driving the differences between value sets, and therefore differences in the value assigned to EQ-5D-Y-3L profile data. The choice of which EQ-5D-Y-3L value set to use in applications to clinical data may have an important bearing on results e.g. in terms of improvement in health-related quality of life and estimated QALY gains.

Our analyses show substantial differences in values between EQ-5D-Y-3L and EQ-5D-5L value sets. PD is always the most important dimension in the EQ-5D-Y-3L value sets. However, for the EQ-5D-5L, this is not the case as PD and AD are the most important dimensions in most Western European countries, while MO is the most important dimension in most Eastern European and Asian countries \[25\]. In the case of Indonesia, PD is the least important dimension for the EQ-5D-L, but the most important dimension in the EQ-5D-Y-3L, leading to substantially different values for EQ-5D-5L and EQ-5D-Y-3L values in Indonesia \[15, 32\]. The similarity in relative importance of the dimensions suggests more homogeneity in EQ-5D-Y-3L value sets between countries, although the scales still differ substantially, as they do in EQ-5D-5L value sets, suggesting that the rate at which respondents trade life years for quality of life for children differs substantially between countries.

There are several factors that may explain these differences between EQ-5D-Y-3L and EQ-5D-5L value sets, such as: (i) differences in the descriptive systems of the two instruments, (ii) difference in perspective used in the valuation task (valuing health for oneself or for a hypothetical 10-year-old child) \[41\], (iii) the fact that different valuation methods are used (cTTO-based for EQ-5D-5L, mainly DCE based for the EQ-5D-Y-3L), (iv) special considerations regarding a child’s survival which are not related to the health problems being valued (e.g. unwillingness to trade off life years for a different person, as is done in the cTTO task, or unwillingness to choose “worse than dead” for another person or a child, both of which could affect the scale), or (v) just genuinely different preferences for child health states \[28\]. These differences in values may be problematic when the values are used in economic evaluations using samples in which part of the sample completes the EQ-5D-Y-3L and another part completes the EQ-5D-5L, as differences in values may not reflect differences in the underlying health state. However, further research will be needed to investigate the exact effect on values of using EQ-5D-Y-3L and EQ-5D-5L value sets on response data, to measure the impact of the different value set properties on utility estimates.

### Limitations and strengths

This study has some limitations. First, only a relatively small number of countries have published value sets for the EQ-5D-Y-3L, as well as a value set for the EQ-5D-5L. Including more value sets in the descriptive analyses may allow for a more reliable comparison of EQ-5D-Y-3L value sets between countries, as well as a more reliable comparison between EQ-5D-Y-3L and EQ-5D-5L value sets. However, for the aggregate preference pattern analyses, a similar number of value sets was used by Olsen et al. to derive a reliable aggregate preference pattern for Western countries, suggesting that comparisons of small numbers of value sets may still be informative \[24\]. Second, the criteria set out by Olsen et al. to identify aggregate preference patterns were aimed at value sets for the EQ-5D-5L, and did not fit the EQ-5D-Y-3L value sets \[24\] Therefore, they had to be adapted for a more reliable identification of aggregate preference patterns. This reduces the comparability between the Olsen et al. study and the current study. Third, when comparing EQ-5D-Y-3L and EQ-5D-5L value sets, we are comparing instruments with different descriptive systems. For example, *anxiety/depression* in the EQ-5D-5L replaced by *feeling worried*, *sad or unhappy* in the EQ-5D-Y-3L. Although the AD and WSU dimensions are related, they may be interpreted differently by respondents in valuation studies in terms of how important they are. The same may hold for the SC and LAM dimensions. Furthermore, the levels in these instruments have different severity labels, which may also invoke differences in how many years are traded to avoid health problems, reducing the comparability of values between the instruments. We considered the option of comparing value sets between EQ-5D-Y-3L and EQ-5D-L. However, the methods used to develop EQ-5D-3L value sets varied widely, and some of these value sets are very old. In contrast, both the EQ-5D-5L and EQ-5D-Y-3L value sets are produced by using an EQ-VT protocol and reflect contemporary preferences data. Furthermore, although the EQ-5D-3L and-5D-Y-3L both have three levels, there are nevertheless important differences between their descriptive systems (for example, the latter does not include ‘confined to bed’). For these reasons, we considered it more relevant to compare value sets with EQ-5D-5L instead. Lastly, we assessed dimension importance by the ordering of the coefficients for the worst level for each dimension, which may not fully reflect dimensions importance altogether as only the most extreme level is being considered. An alternative would be to consider weights assigned to the levels 2 of a dimension, or the combination of the weights assigned to both levels.

A strength of this study is that it provides the first comparison of EQ-5D-Y-3L value sets, which provides information on how these value sets compare, and may help to confirm their validity as representations of societal preferences regarding child HRQoL. Furthermore, this is the first comparison of EQ-5D-Y-3L and EQ-5D-5L value sets, which provides some initial information on possible discrepancies between values for adult and paediatric health states, and whether transitions between instruments (e.g. in lifetime cost effectiveness models of paediatric interventions) may lead to substantial differences in values, without any change in the underlying health.

## Conclusion

EQ-5D-Y-3L value sets share some key characteristics, such as the importance of the pain/discomfort dimension, and relatively little importance for the LAM dimension. However, substantial differences remain, mostly in terms of scale length and the number of negative values, which may reflect a difference in the willingness to trade life years for children, for them to avoid poor health. Value sets for European countries seem to share similar characteristics, as do value sets for Asian countries, suggesting that regional aggregate preference patterns are able to describe country value sets with moderate error. This suggests that new value sets from the same geographic/cultural region are likely to be similar to existing value sets. Still, caution should be exercised, as the number of value sets available per region is still small – and we do see exceptions to the ‘rule’. For example, the Australian EQ-5D-Y-3L value set was expected to be similar to those of European countries, given shared cultural characteristics, but in practice its values are more similar to the Asian preference pattern we have reported. Substantial differences between EQ-5D-Y-3L and EQ-5D-5L value sets in countries where both exist, suggesting a discrepancy between the relative value of quality and length of life for adults vs. children. However, given that these instruments differ both in how health is described, and how it is valued, analysis of patient data and value sets will be needed to investigate this further. Future work is planned to investigate the respondent-level data for the cTTO and DCE tasks of the individual EQ-5D-Y-3L valuation studies, which may provide further information on differences in preferences for EQ-5D-Y-3L health states and the resulting value sets.

##### Appendix

Table <a href="#Tab5" data-ref-type="table">5</a>

<div id="Tab5" class="table-wrap">

<div class="caption">

Values for the EQ-5D-Y-3L European and Asian preference patterns \[These values are generated for academic purposes, and are not recommended for use in e.g. economic evaluations\]

</div>

| State | Europe | Asia | State | Europe | Asia | State | Europe | Asia |
|----|----|----|----|----|----|----|----|----|
| 11111 | 1.000 | 1.000 | 21,111 | 0.939 | 0.951 | 31,111 | 0.773 | 0.877 |
| 11112 | 0.893 | 0.944 | 21,112 | 0.832 | 0.895 | 31,112 | 0.666 | 0.814 |
| 11113 | 0.657 | 0.862 | 21,113 | 0.596 | 0.807 | 31,113 | 0.429 | 0.721 |
| 11121 | 0.855 | 0.930 | 21,121 | 0.794 | 0.881 | 31,121 | 0.628 | 0.800 |
| 11122 | 0.748 | 0.875 | 21,122 | 0.688 | 0.815 | 31,122 | 0.521 | 0.726 |
| 11123 | 0.512 | 0.787 | 21,123 | 0.451 | 0.721 | 31,123 | 0.285 | 0.628 |
| 11131 | 0.554 | 0.789 | 21,131 | 0.493 | 0.731 | 31,131 | 0.327 | 0.644 |
| 11132 | 0.447 | 0.725 | 21,132 | 0.386 | 0.657 | 31,132 | 0.220 | 0.562 |
| 11133 | 0.210 | 0.633 | 21,133 | 0.149 | 0.558 | 31,133 | −0.017 | 0.459 |
| 11211 | 0.912 | 0.951 | 21,211 | 0.851 | 0.901 | 31,211 | 0.685 | 0.819 |
| 11212 | 0.805 | 0.895 | 21,212 | 0.744 | 0.833 | 31,212 | 0.578 | 0.743 |
| 11213 | 0.568 | 0.806 | 21,213 | 0.507 | 0.739 | 31,213 | 0.341 | 0.644 |
| 11221 | 0.767 | 0.880 | 21,221 | 0.706 | 0.819 | 31,221 | 0.540 | 0.729 |
| 11222 | 0.660 | 0.814 | 21,222 | 0.599 | 0.742 | 31,222 | 0.433 | 0.644 |
| 11223 | 0.424 | 0.719 | 21,223 | 0.363 | 0.641 | 31,223 | 0.196 | 0.540 |
| 11231 | 0.465 | 0.730 | 21,231 | 0.405 | 0.660 | 31,231 | 0.238 | 0.564 |
| 11232 | 0.359 | 0.655 | 21,232 | 0.298 | 0.575 | 31,232 | 0.131 | 0.472 |
| 11233 | 0.122 | 0.556 | 21,233 | 0.061 | 0.470 | 31,233 | −0.105 | 0.363 |
| 11311 | 0.746 | 0.880 | 21,311 | 0.685 | 0.824 | 31,311 | 0.519 | 0.738 |
| 11312 | 0.639 | 0.818 | 21,312 | 0.578 | 0.752 | 31,312 | 0.412 | 0.658 |
| 11313 | 0.402 | 0.727 | 21,313 | 0.341 | 0.654 | 31,313 | 0.175 | 0.556 |
| 11321 | 0.601 | 0.804 | 21,321 | 0.540 | 0.737 | 31,321 | 0.374 | 0.644 |
| 11322 | 0.494 | 0.732 | 21,322 | 0.433 | 0.655 | 31,322 | 0.267 | 0.554 |
| 11323 | 0.257 | 0.634 | 21,323 | 0.197 | 0.551 | 31,323 | 0.030 | 0.446 |
| 11331 | 0.299 | 0.649 | 21,331 | 0.238 | 0.574 | 31,331 | 0.072 | 0.475 |
| 11332 | 0.193 | 0.569 | 21,332 | 0.132 | 0.484 | 31,332 | −0.035 | 0.377 |
| 11333 | −0.044 | 0.467 | 21,333 | −0.105 | 0.376 | 31,333 | −0.271 | 0.265 |
| 12111 | 0.962 | 0.974 | 22,111 | 0.901 | 0.927 | 32,111 | 0.735 | 0.847 |
| 12112 | 0.855 | 0.921 | 22,112 | 0.794 | 0.863 | 32,112 | 0.628 | 0.776 |
| 12113 | 0.619 | 0.834 | 22,113 | 0.558 | 0.770 | 32,113 | 0.391 | 0.678 |
| 12121 | 0.817 | 0.906 | 22,121 | 0.756 | 0.849 | 32,121 | 0.590 | 0.761 |
| 12122 | 0.710 | 0.843 | 22,122 | 0.650 | 0.775 | 32,122 | 0.483 | 0.680 |
| 12123 | 0.474 | 0.750 | 22,123 | 0.413 | 0.676 | 32,123 | 0.247 | 0.577 |
| 12131 | 0.516 | 0.759 | 22,131 | 0.455 | 0.693 | 32,131 | 0.289 | 0.599 |
| 12132 | 0.409 | 0.687 | 22,132 | 0.348 | 0.610 | 32,132 | 0.182 | 0.510 |
| 12133 | 0.172 | 0.590 | 22,133 | 0.111 | 0.507 | 32,133 | −0.055 | 0.402 |
| 12211 | 0.874 | 0.927 | 22,211 | 0.813 | 0.868 | 32,211 | 0.647 | 0.779 |
| 12212 | 0.767 | 0.862 | 22,212 | 0.706 | 0.792 | 32,212 | 0.540 | 0.696 |
| 12213 | 0.530 | 0.768 | 22,213 | 0.469 | 0.693 | 32,213 | 0.303 | 0.593 |
| 12221 | 0.729 | 0.848 | 22,221 | 0.668 | 0.778 | 32,221 | 0.502 | 0.682 |
| 12222 | 0.622 | 0.773 | **22,222** | **0.561** | **0.693** | 32,222 | 0.395 | 0.590 |
| 12223 | 0.385 | 0.673 | 22,223 | 0.325 | 0.588 | 32,223 | 0.158 | 0.481 |
| 12231 | 0.427 | 0.691 | 22,231 | 0.366 | 0.613 | 32,231 | 0.200 | 0.511 |
| 12232 | 0.321 | 0.607 | 22,232 | 0.260 | 0.519 | 32,232 | 0.093 | 0.411 |
| 12233 | 0.084 | 0.504 | 22,233 | 0.023 | 0.410 | 32,233 | −0.143 | 0.297 |
| 12311 | 0.708 | 0.851 | 22,311 | 0.647 | 0.787 | 32,311 | 0.480 | 0.695 |
| 12312 | 0.601 | 0.781 | 22,312 | 0.540 | 0.706 | 32,312 | 0.374 | 0.607 |
| 12313 | 0.364 | 0.685 | 22,313 | 0.303 | 0.604 | 32,313 | 0.137 | 0.500 |
| 12321 | 0.563 | 0.767 | 22,321 | 0.502 | 0.692 | 32,321 | 0.336 | 0.593 |
| 12322 | 0.456 | 0.687 | 22,322 | 0.395 | 0.602 | 32,322 | 0.229 | 0.495 |
| 12323 | 0.219 | 0.585 | 22,323 | 0.159 | 0.494 | 32,323 | −0.008 | 0.383 |
| 12331 | 0.261 | 0.606 | 22,331 | 0.200 | 0.523 | 32,331 | 0.034 | 0.418 |
| 12332 | 0.154 | 0.518 | 22,332 | 0.094 | 0.425 | 32,332 | −0.073 | 0.312 |
| 12333 | −0.082 | 0.411 | 22,333 | −0.143 | 0.312 | 32,333 | −0.309 | 0.196 |
| 13111 | 0.823 | 0.909 | 23,111 | 0.762 | 0.856 | 33,111 | 0.596 | 0.771 |
| 13112 | 0.716 | 0.850 | 23,112 | 0.655 | 0.786 | 33,112 | 0.489 | 0.694 |
| 13113 | 0.479 | 0.759 | 23,113 | 0.418 | 0.689 | 33,113 | 0.252 | 0.593 |
| 13121 | 0.678 | 0.835 | 23,121 | 0.617 | 0.771 | 33,121 | 0.451 | 0.679 |
| 13122 | 0.571 | 0.766 | 23,122 | 0.510 | 0.691 | 33,122 | 0.344 | 0.592 |
| 13123 | 0.335 | 0.670 | 23,123 | 0.274 | 0.589 | 33,123 | 0.107 | 0.486 |
| 13131 | 0.376 | 0.683 | 23,131 | 0.316 | 0.610 | 33,131 | 0.149 | 0.512 |
| 13132 | 0.270 | 0.605 | 23,132 | 0.209 | 0.522 | 33,132 | 0.042 | 0.417 |
| 13133 | 0.033 | 0.504 | 23,133 | −0.028 | 0.415 | 33,133 | −0.194 | 0.306 |
| 13211 | 0.734 | 0.855 | 23,211 | 0.674 | 0.789 | 33,211 | 0.507 | 0.696 |
| 13212 | 0.628 | 0.784 | 23,212 | 0.567 | 0.708 | 33,212 | 0.400 | 0.607 |
| 13213 | 0.391 | 0.687 | 23,213 | 0.330 | 0.605 | 33,213 | 0.164 | 0.500 |
| 13221 | 0.590 | 0.770 | 23,221 | 0.529 | 0.694 | 33,221 | 0.362 | 0.594 |
| 13222 | 0.483 | 0.688 | 23,222 | 0.422 | 0.602 | 33,222 | 0.256 | 0.495 |
| 13223 | 0.246 | 0.586 | 23,223 | 0.185 | 0.494 | 33,223 | 0.019 | 0.383 |
| 13231 | 0.288 | 0.608 | 23,231 | 0.227 | 0.524 | 33,231 | 0.061 | 0.418 |
| 13232 | 0.181 | 0.518 | 23,232 | 0.120 | 0.424 | 33,232 | −0.046 | 0.311 |
| 13233 | −0.055 | 0.411 | 23,233 | −0.116 | 0.312 | 33,233 | −0.282 | 0.195 |
| 13311 | 0.568 | 0.776 | 23,311 | 0.507 | 0.705 | 33,311 | 0.341 | 0.609 |
| 13312 | 0.462 | 0.700 | 23,312 | 0.401 | 0.619 | 33,312 | 0.234 | 0.515 |
| 13313 | 0.225 | 0.600 | 23,313 | 0.164 | 0.513 | 33,313 | −0.002 | 0.405 |
| 13321 | 0.424 | 0.686 | 23,321 | 0.363 | 0.605 | 33,321 | 0.196 | 0.501 |
| 13322 | 0.317 | 0.600 | 23,322 | 0.256 | 0.508 | 33,322 | 0.090 | 0.397 |
| 13323 | 0.080 | 0.494 | 23,323 | 0.019 | 0.397 | 33,323 | −0.147 | 0.282 |
| 13331 | 0.122 | 0.520 | 23,331 | 0.061 | 0.431 | 33,331 | −0.105 | 0.321 |
| 13332 | 0.015 | 0.426 | 23,332 | −0.046 | 0.327 | 33,332 | −0.212 | 0.210 |
| 13333 | −0.221 | 0.316 | 23,333 | −0.282 | 0.211 | **33,333** | **−0.448** | **0.038** |

</div>

### Acknowledgements

We would like to thank the discussant who discussed an earlier draft of this manuscript at the EuroQol Plenary Meeting in Rome in 2023, as well as two anonymous reviewers that provided helpful comments on earlier drafts of this manuscript.

### Author contributions

All authors contributed to the study conception and design. Specifically, the following activities were performed by the authors:

Conceptualization: Bram Roudijk, Tianxin Pan, Jan Abel Olsen, Nancy Devlin.

Methodology: Bram Roudijk, Tianxin Pan, Jan Abel Olsen, Nancy Devlin.

Formal analysis and investigation: Bram Roudijk.

Writing - original draft preparation: Bram Roudijk.

Writing - review and editing: Bram Roudijk, Tianxin Pan, Jan Abel Olsen, Nancy Devlin.

Funding acquisition: Bram Roudijk, Jan Abel Olsen, Nancy Devlin.

### Funding

This paper is part of an ongoing project funded by the Euroqol Research Foundation, RA-1497. Views expressed in this paper are not necessarily those of the EuroQol Research Foundation.

### Data Availability

Not applicable, as no respondent data was used in this manuscript. Codes for analysis are available upon reasonable request.

### Declarations

#### Conflict of interest

This study was funded by the Euroqol Research Foundation, project number RA-1497. Bram Roudijk, Tianxin Pan, Jan Abel Olsen and Nancy Devlin are members of the EuroQol Group. Bram Roudijk is employed by the EuroQol Research Foundation. All authors have received grants from the EuroQol Research Foundation.

#### Ethic statement

No data was collected in this study, nor was any data used in this study from any individual. Therefore, no ethical approval was required to conduct this study.

## References

1. Wille, N., Badia, X., Bonsel, G., Burström, K., Cavrini, G., Devlin, N., Ravens-Sieberer, U.: Development of the EQ-5D-Y: A child-friendly version of the EQ-5D. Qual. Life Res. 19(6), 875–886 (2010)20405245 10.1007/s11136-010-9648-yPMC2892611

2. Ravens-Sieberer, U., Wille, N., Badia, X., Bonsel, G., Burström, K., Cavrini, G., Greiner, W.: Feasibility, reliability, and validity of the EQ-5D-Y: Results from a multinational study. Qual. Life Res. 19(6), 887–897 (2010)20401552 10.1007/s11136-010-9649-xPMC2892614

3. Herdman, M., Gudex, C., Lloyd, A., Janssen, M.F., Kind, P., Parkin, D., Badia, X.: Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual. Life Res. 20(2011), 1727–1736 (2011)21479777 10.1007/s11136-011-9903-xPMC3220807

4. Dolan, P., Gudex, C., Kind, P., Williams, A.: The time trade-off method: Results from a general population study. Health Econ. 5(2), 141–154 (1996)8733106 10.1002/(SICI)1099-1050(199603)5:2<141::AID-HEC189>3.0.CO;2-N

5. Kreimeier, S., Oppe, M., Ramos-Goñi, J.M., Cole, A., Devlin, N., Herdman, M., Greiner, W.: Valuation of EuroQol five-dimensional questionnaire, youth version (EQ-5D-Y) and EuroQol five-dimensional questionnaire, three-level version (EQ-5D-3L) health states: The impact of wording and perspective. Value Health 21(11), 1291–1298 (2018)30442276 10.1016/j.jval.2018.05.002

6. Ramos-Goñi, J.M., Oppe, M., Stolk, E., Shah, K., Kreimeier, S., Rivero-Arias, O., Devlin, N.: International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics 38, 653–663 (2020)32297224 10.1007/s40273-020-00909-3

7. Janssen, B.M., Oppe, M., Versteegh, M.M., Stolk, E.A.: Introducing the composite time trade-off: A test of feasibility and face validity. Eur. J. Health Econ. 14, 5–13 (2013)23900660 10.1007/s10198-013-0503-2PMC3728457

8. Devlin, N., Pan, T., Kreimeier, S., Verstraete, J., Stolk, E., Rand, K., Herdman, M.: Valuing EQ-5D-Y: The current state of play. Health Qual. Life Outcomes 20(1), 1–11 (2022)35794607 10.1186/s12955-022-01998-8PMC9260978

9. Pan, T., Roudijk, B., Devlin, N., Mulhern, B., Norman, R.: An Australian value set for the EQ-5D-Y-3L. Health Qual. Life Outcomes 23(1), 72 (2025)40660259 10.1186/s12955-025-02402-xPMC12261590

10. Dewilde, S., Roudijk, B., Tollenaar, N.H., Ramos-Goñi, J.M.: An EQ-5D-Y-3L Value Set for Belgium. Pharmacoeconomics (S2),(2022). 10.1007/s40273-022-01187-x10.1007/s40273-022-01187-xPMC962859236316544

11. Espirito Santo, C.M., Miyamoto, G.C., Santos, V.S., Ben, Â.J., Finch, A.P., Roudijk, B., de Jesus-Moraleida, Fabianna Resende, Stein, Airton Tetelbom, Santos, Marisa, Yamato, T.P.: Estimating an EQ-5D-Y-3L Value Set for Brazil. PharmacoEconomics (2024). 10.1007/s40273-024-01404-938954389 10.1007/s40273-024-01404-9PMC11343814

12. Yang, Z., Jiang, J., Wang, P., Jin, X., Wu, J., Fang, Y., Feng, Da., Xi, Xiaoyu, Li, Shunping, Jing, Mingxia, Zheng, Bin, Huang, Weidong, Luo, N.: Estimating an EQ-5D-Y-3L value set for China. Pharmacoeconomics (2022). 10.1007/s40273-022-01216-936396878 10.1007/s40273-022-01216-9PMC9758244

13. Kreimeier, S., Mott, D., Ludwig, K., Greiner, W.: EQ-5D-Y value set for Germany. Pharmacoeconomics. 40(Suppl 2), 217–229 (2022). 10.1007/s40273-022-01143-910.1007/s40273-022-01143-9PMC912474835604633

14. Rencz, F., Ruzsa, G., Bató, A., Yang, Z., Finch, A.P., Brodszky, V.: Value Set for the EQ-5D-Y-3L in Hungary. Pharmacoeconomics (2022). 10.1007/s40273-022-01190-236123448 10.1007/s40273-022-01190-2PMC9485017

15. Fitriana, T.S., Roudijk, B., Purba, F.D., Busschbach, J.J., Stolk, E.: Estimating an EQ-5D-Y-3L value set for Indonesia by mapping the DCE onto TTO values. Pharmacoeconomics 40(2), 157–167 (2022)36348155 10.1007/s40273-022-01210-1PMC9758088

16. Shiroiwa, T., Ikeda, S., Noto, S., Fukuda, T., Stolk, E.: Valuation survey of EQ-5D-Y based on the international common protocol: Development of a value set in Japan. Med. Decis. Making 41(5), 597–606 (2021)33754886 10.1177/0272989X211001859PMC8191148

17. Roudijk, B., Sajjad, A., Essers, B., Lipman, S., Stalmeier, P., Finch, A.P.: A value set for the EQ-5D-Y-3L in the Netherlands. Pharmacoeconomics 40(Suppl 2), 193–203 (2022)36216977 10.1007/s40273-022-01192-0PMC9549846

18. Prevolnik Rupel, V., Ogorevc, M., & IMPACT HTA HRQoL Group http://orcid.org/0000-0002-9568-5190 EQ-5D-Y value set for Slovenia. Pharmacoeconomics, 39(4), 463–471 (2021) http://orcid.org/0000-0001-9552-6969. 10.1007/s40273-022-01143-9s40273-020-00994-410.1007/s40273-020-00994-4PMC800980033565048

19. Ramos-Goñi, J.M., Oppe, M., Estévez-Carrillo, A., Rivero-Arias, O., Wolfgang, G., Simone, K., Kristina, Ludwig, Valentina, R.: Accounting for unobservable preference heterogeneity and evaluating alternative anchoring approaches to estimate country-specific EQ-5D-Y value sets: a case study using Spanish preference data. Value in Health 25(5), 835–843 (2022)35500952 10.1016/j.jval.2021.10.013

20. Devlin, N., Roudijk, B., Viney, R., Stolk, E.: EQ-5D-Y-3L Value Sets, Valuation Methods and Conceptual Questions. PharmacoEconomics (2022). 10.1007/s40273-022-01226-736504378 10.1007/s40273-022-01226-7PMC9758242

21. Mott, D.J., Devlin, N.J., Kreimeier, S., Norman, R., Shah, K.K., Rivero-Arias, O.: Analytical Considerations when Anchoring Discrete Choice Experiment Values Using Composite time trade-off Data: the Case of EQ-5D-Y-3L. PharmacoEconomics (S2),(2022). 10.1007/s40273-022-01214-x10.1007/s40273-022-01214-xPMC975809236396877

22. Roudijk, B., Donders, A.R.T., Stalmeier, P.F.: Cultural values: Can they explain differences in health utilities between countries? Med. Decis. Making 39(5), 605–616 (2019)31257997 10.1177/0272989X19841587PMC6791017

23. Bailey, H., Kind, P.: Preliminary findings of an investigation into the relationship between National culture and EQ-5D value sets. Qual. Life Res. 19, 1145–1154 (2010)20496167 10.1007/s11136-010-9678-5

24. Olsen, J.A., Lamu, A.N., Cairns, J.: In search of a common currency: A comparison of seven EQ-5D‐5L value sets. Health Econ 27(1), 39–49 (2018)29063633 10.1002/hec.3606

25. Roudijk, B., Janssen, B., Olsen, J.A.: How do EQ-5D-5L value sets differ? In: Value Sets for EQ-5D-5L: A Compendium, Comparative Review & User Guide, pp. 235–258. Springer International Publishing, Cham (2022)36810025

26. Janssen, M.F., Pickard, A.S., Golicki, D., Gudex, C., Niewada, M., Scalone, L., Swinburn, Paul, Busschbach, J.: Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Quality of life research 22, 1717–1727 (2013)23184421 10.1007/s11136-012-0322-4PMC3764313

27. Devlin, N., Roudijk, B., & Ludwig, K. Value sets for EQ-5D-5L: a compendium, comparative review & user guide. (2022)36810025

28. Devlin, N.J., Pan, T., Sculpher, M., Jit, M., Stolk, E., Rowen, D., van Hout, B., Norman, R.: Using age-specific values for pediatric HRQoL in cost-effectiveness analysis: Is there a problem to be solved? If so, how? Pharmacoeconomics 41(10), 1165–1174 (2023)37439998 10.1007/s40273-023-01300-8PMC10492668

29. Bouckaert, N., Cleemput, I., Devriese, S., Gerkens, S.: An EQ-5D-5L value set for Belgium. PharmacoEconomics-Open 6(6), 823–836 (2022)35927410 10.1007/s41669-022-00353-3PMC9362639

30. Luo, N., Liu, G., Li, M., Guan, H., Jin, X., Rand-Hendriksen, K.: Estimating an EQ-5D-5L value set for China. Value Health 20(4), 662–669 (2017)28408009 10.1016/j.jval.2016.11.016

31. Ludwig, K., von der Schulenburg, G., J. M., Greiner, W.: German value set for the EQ-5D-5L. Pharmacoeconomics. 36, 663–674 (2018)29460066 10.1007/s40273-018-0615-8PMC5954069

32. Rencz, F., Brodszky, V., Gulácsi, L., Golicki, D., Ruzsa, G., Pickard, A.S., Law, Ernest H.., Péntek, M.: Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time trade-off in Hungary. Value in Health 23(9), 1235–1245 (2020)32940242 10.1016/j.jval.2020.03.019

33. Purba, F.D., Hunfeld, J.A., Iskandarsyah, A., Fitriana, T.S., Sadarjoen, S.S., Ramos-Goñi, J.M., Hunfeld, Joke A. M.., Passchier, Jan, Busschbach, Jan J. V.., Busschbach, J.J.: The Indonesian EQ-5D-5L value set. Pharmacoeconomics 35, 1153–1165 (2017)28695543 10.1007/s40273-017-0538-9PMC5656740

34. Shiroiwa, T., Ikeda, S., Noto, S., Igarashi, A., Fukuda, T., Saito, S., Shimozuma, K.: Comparison of value set based on DCE and/or TTO data: Scoring for EQ-5D-5L health States in Japan. Value Health 19(5), 648–654 (2016)27565282 10.1016/j.jval.2016.03.1834

35. Versteegh, M.M., Vermeulen, K.M., Evers, S.M., De Wit, G.A., Prenger, R., Stolk, E.A.: Dutch tariff for the five-level version of EQ-5D. Value Health 19(4), 343–352 (2016)27325326 10.1016/j.jval.2016.01.003

36. Rupel, V., Ogorevc, M.: EQ-5D-5L value set for Slovenia. Pharmacoeconomics. 111515–1524 (2023). 10.1007/s40273-023-01280-910.1007/s40273-023-01280-9PMC1057020737341959

37. Ramos-Goñi, J.M., Craig, B.M., Oppe, M., Ramallo-Fariña, Y., Pinto-Prades, J.L., Luo, N., Rivero-Arias, O.: Handling data quality issues to estimate the Spanish EQ-5D-5L value set using a hybrid interval regression approach. Value Health 21(5), 596–604 (2018)29753358 10.1016/j.jval.2017.10.023

38. Norman, R., Mulhern, B., Lancsar, E., Lorgelly, P., Ratcliffe, J., Street, D., Viney, R.: The use of a discrete choice experiment including both duration and dead for the development of an EQ-5D-5L value set for Australia. Pharmacoeconomics 41(4), 427–438 (2023)36720793 10.1007/s40273-023-01243-0PMC10020301

39. Chen, Y.C.: A tutorial on kernel density Estimation and recent advances. Biostatistics & Epidemiology 1(1), 161–187 (2017). doi:10.1080/24709360.2017.1396742

40. Hofstede, G., Hofstede, G.J., Minkov, M.: Cultures and Organizations: Software of the Mind, vol. 2. Mcgraw-hill, New York (2005)

41. De Silva, A., van Heusden, A., Lang, Z., Devlin, N., Norman, R., Dalziel, K., Peasgood, T., Pan, T.: How do health state values differ when respondents consider adults versus children living in those states? a systematic review. PharmacoEconomics (2025). 10.1007/s40273-025-01493-040261492 10.1007/s40273-025-01493-0PMC12167273

[^1]: A threshold of 0.05 was used, as this is the smallest possible difference between cTTO observations, making it a suitable unit of measurement to describe differences.

[^2]: We used a threshold of 0.03 rather than 0.05 for these dimensions, as their weights tend to be smaller than those of WSU and PD. This makes it more likely that the weights are more similar, requiring a smaller threshold to detect differences.

[^3]: Brazil is not included in Fig. <a href="#Fig1" data-ref-type="fig">1</a> as it does not have an EQ-5D-5L value set.

[^4]: These numbers are generated for academic purposes only, and are not intended or recommended to be used as a replacement for value sets in countries where value sets are currently not available.

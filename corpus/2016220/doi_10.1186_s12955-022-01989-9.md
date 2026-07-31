---
project_id: "2016220"
work_id: "doi:10.1186/s12955-022-01989-9"
doi: "10.1186/s12955-022-01989-9"
pmid: "35614472"
pmcid: "PMC9131619"
title: "Exploring the importance of controlling heteroskedasticity and heterogeneity in health valuation: a case study on Dutch EQ-5D-5L"
journal: "Health and Quality of Life Outcomes"
publication_date: "2022-05-25"
volume: "20"
authors:
  - name: "Suzana Karim"
    affiliation_ids:
      - "Aff1"
  - name: "Benjamin M Craig"
    affiliation_ids:
      - "Aff1"
  - name: "Catharina G M Groothuis-Oudshoorn"
    affiliation_ids:
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "University of South Florida, 4202 E Fowler Ave, Tampa, FL 33620 USA"
  - id: "Aff2"
    name: "University of Twente, Enschede, The Netherlands"
licence: "cc-by"
source_file: "input/projects/2016220/papers/doi_10.1186_s12955-022-01989-9.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9131619/fullTextXML"
source_method: "epmc_xml"
source_sha256: "fb4cda4696ba5cafbc14672878c18e66090efee71924d757d6bfe4eb94a3a249"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Exploring the importance of controlling heteroskedasticity and heterogeneity in health valuation: a case study on Dutch EQ-5D-5L

## Abstract

### Background

Respondents in a health valuation study may have different sources of error (i.e., heteroskedasticity), tastes (differences in the relative effects of each attribute level), and scales (differences in the absolute effects of all attributes). Although prior studies have compared values by preference-elicitation tasks (e.g., paired comparison \[PC\] and best–worst scaling case 2 \[BWS\]), no study has yet controlled for heteroskedasticity and heterogeneity (taste and scale) simultaneously in health valuation.

### Methods

Preferences on EQ-5D-5L profiles were elicited from a random sample of 380 adults from the general population of the Netherlands, using 24 PC and 25 BWS case 2 tasks. To control for heteroskedasticity and heterogeneity (taste and scale) simultaneously, we estimated Dutch EQ-5D-5L values using conditional, heteroskedastic, and scale-adjusted latent class (SALC) logit models by maximum likelihood.

### Results

After controlling for heteroskedasticity, the PC and BWS values were highly correlated (Pearson's correlation: 0.9167, CI: 0.9109–0.9222) and largely agreed (Lin's concordance: 0.7658, CI: 0.7542–0.7769) on a pits scale. In terms of preference heterogeneity, some respondents (mostly young men) failed to account for any of the EQ-5D-5L attributes (i.e., garbage class), and others had a lower scale (59%; p-value: 0.123). Overall, the SALC model produced a consistent Dutch EQ-5D-5L value set on a pits scale, like the original study (Pearson's correlation:0.7295; Lin's concordance: 0.6904).

### Conclusions

This paper shows the merits of simultaneously controlling for heteroskedasticity and heterogeneity in health valuation. In this case, the SALC model dispensed with a garbage class automatically and adjusted the scale for those who failed the PC dominant task. Future analysis may include more behavioral variables to better control heteroskedasticity and heterogeneity in health valuation.

### Highlights

- The Dutch EQ-5D-5L values based on paired comparison \[PC\] and best-worst scaling \[BWS\] responses were highly correlated and largely agreed after controlling for heteroskedasticity.

- Controlling for taste and scale heterogeneity simultaneously enhanced the Dutch EQ-5D-5Lvalues by automatically dispensing with a garbage class and adjusting the scale for those who failed the dominant task.

- After controlling for heteroskedasticity and heterogeneity, this study produced Dutch EQ-5D-5L values on a pits scale moderately concordant with the original values.

**Keywords:** Health valuation, Best–worst scaling, Heteroskedasticity, Scale heterogeneity, EQ-5D

Received 2021 Dec 3; Accepted 2022 May 6; Collection date 2022.

## Introduction

Developed by the EuroQol group in 2005, the EQ-5D-5L instrument provides a widely used descriptive system for health valuation in multiple languages \[1\]. This descriptive system expresses a person's health along with five attributes, i.e., mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. Each attribute has five levels (no problems, slight problems, moderate problems, severe problems, and unable to/ extreme problems) describing the severity of the person's health problems. Using this system of five five-level attributes, health valuation studies may ask respondents about their preferences regarding its 3125 possible health profiles (5<sup>5</sup>).

In general, collecting ordinal responses using choice tasks, such as PC and BWS, is gaining widespread use in health economics and policy \[2, 3\]. Methodological advances in health preference research (HPR) have been applied successfully in eliciting patient and community preferences for a wide range of health care interventions \[4\]. Many literature reviews have been conducted that show the gaining interest in HPR \[2, 5\]. As a potential methodological extension, some researchers proposed including more choice tasks, such as ranking and best–worst scaling (BWS), as complements or alternatives to the time trade-off (TTO) tasks in the EQ-VT protocol \[6–9\]. Furthermore, many believe that choice tasks with their ordinal responses were less cognitively burdensome than cardinal tasks with their indifference responses \[10–12\]. The EQ-VT protocol currently includes some PC as a complement to the TTO to better understand preferences between EQ-5D-5L profiles; therefore, there seems to be an opportunity to include additional choice tasks within the protocol. In this project, we conducted a Dutch EQ-5D-5L valuation study, including PC and BWS tasks, to explore a natural extension to the EQ-VT protocol. The valuation is done in a pits scale rather than the conventional QALY due to lack of the life span attribute \[13\]. We proposed this project in hopes that BWS might serve as a possible alternative or addition for PC tasks in the EQ-VT protocol. Specifically, the single-profile (or case 2) task is one of the three BWS tasks \[14\]. Unlike a PC, where respondents choose between two EQ-5D-5L profiles, respondents in a case-2 BWS task face a single EQ-5D-5L profile (like a TTO task), making this task more coherent with the TTO task. In the case-2 BWS task, the respondent indicates the best and the worst attribute levels within the given profile. In this study, we hypothesize that the EQ-5D-5L values estimated using the PC and BWS responses agree.

### Heteroskedasticity and heterogeneity in health valuation

Heteroskedasticity and heterogeneity have been identified as key limitations to the analysis and interpretation of preference evidence, particularly ordinal responses\[15\]. A recent review on heterogeneity analyses in HPR showed that most published studies analyzed heterogeneity without controlling for heteroskedasticity or differential scaling \[3\]. This paper further contributes to HPR by demonstrating the implications of controlling heteroskedasticity and heterogeneity in health valuation as well as separating taste and scale heterogeneity.

Like other observable differences \[16\], heteroskedasticity refers to differences in variance by observable factors, such as task-level or individual-level factors. In a heteroskedastic logit, its variance may vary between tasks systematically in response to task complexity and the number of choice alternatives, attribute differences, or individual behavioral differences \[15, 17\]. In this study, we hypothesize that variance varies by task sequence and task type and that controlling this heteroskedasticity can reduce uncertainty in EQ-5D-5L values. Heteroskedasticity is not a form of preference heterogeneity because the difference in variance is derived from a difference in behavior (e.g., task sequence), not preference.

Apart from heteroskedasticity, we also examine two types of preference heterogeneity \[18\]. First, groups of respondents like or dislike different alternatives in a systematic way that reflects the relative importance of the attributes (i.e., taste classes). Taste heterogeneity refers to differences in the relative effects of each attribute level. For example, some respondents may place a greater weight on functioning and others on feeling (e.g., pain/discomfort, anxiety/depression). Alternatively, there can be a group of respondents who fail to account for any of the EQ-5D-5L attributes, and by summing up their preference information creates coefficient estimates of garbage class. The responses of people who belong to a garbage class may show the probability of choosing the best (11111) over the worst (55555) EQ-5D-5L profile is near 50%. Second, groups may like or dislike alternatives systematically that reflect the absolute value of all attributes (i.e., scale classes). Scale heterogeneity refers to more subtle differences in the absolute effects of all attributes (compared to garbage classes), and scale classes may be related to the respondents' difficulty distinguishing between alternatives (e.g., more indifference with a lower scale value).

Estimating differences in attribute importance between respondents without controlling for scale heterogeneity can often mislead the interpretation of taste heterogeneity, which is confounded by scale heterogeneity \[19\]. Using the information on the respondents, a scale-adjusted latent class (SALC) model \[20\] can disentangle taste and scale heterogeneity simultaneously by identifying latent classes of persons who differ in their relative importance (taste classes), as well as latent scale classes—groups of people who differ by how intense (or indifferent) their preferences are. In this paper, heteroskedasticity is associated with observable differences in scale between tasks (e.g., task sequence), and scale heterogeneity is associated with latent differences in scale between individuals (e.g., failing the PC dominance task). The SALC model allows for heteroskedasticity and two forms of heterogeneity, and we hypothesize that controlling for all three can enhance health valuation. Given this background, this study is aimed to run a case analysis on a Dutch EQ-5D-5L valuation dataset with the following objectives. First, we examined the effects of controlling heteroskedasticity by comparing the results of the conditional and heteroskedastic logit. Second, we illustrated the EQ-5D-5L values based on the PC and case-2 BWS responses and assessed their correlation and agreement. Third, we estimated EQ-5D-5L values using the scale-adjusted latent class (SALC) logit models, which control for taste and scale heterogeneity as well as heteroskedasticity. Finally, we compare the Dutch EQ-5D-5L values to the original values produced using the EQ-VT protocol \[21\].

## Methods

### Overview

In September 2016, Dutch respondents were recruited from a marketing panel (Survey Sampling International) to complete computer-based interviews via an online survey instrument. We did not aim for a fully representative sample but sampled from groups with known EQ-5D-5L impairments. We aimed to sample 300 subjects stratified by domain and severity of health problems captured by the EQ-5D-5L. To facilitate the analysis of preference heterogeneity, all respondents completed the same PC and case-2 BWS tasks using the same series of EQ-5D-5L profiles. Examples of the PC and BWS tasks can be found in Appendix <a href="#Sec20" data-ref-type="sec">1</a>.

### EQ-5D-5L profiles

Using the EQ-5D-5L descriptive system, the five five-level attributes can be described by a 5-digit vector of the attribute levels, where the position of the integer refers to the attribute, while the integer itself refers to the attribute level. For example, EQ-5D-5L profile '32512' would describe moderate problems walking about, some problems washing or dressing self, unable to perform usual activities, no pain or discomfort, and some anxiety or depression.

### Experimental design

The BWS' Health profile A' design is based on an orthogonal main effects plan (OMEP) \[22\] that, in the case of the EQ-5D-5L, consists of 25 profiles. With these 25 profiles, in principle, it is possible to estimate 24 individual BWS level parameters. By *rotating the OMEP coding*,[^1] a design was obtained with the minimal number of only one attribute at an extreme level, resulting in 15 out of 25 best choices with at least two attributes with the same lowest level and 16 out of 25 worst choices with at least two attributes with the same highest level. Therefore, at least 31 − 24 = 7 degrees of freedom to estimate a model for every respondent in case the other 19 choices were non-informative. The chosen health profiles are listed in Appendix <a href="#Sec20" data-ref-type="sec">1</a> (Table <a href="#Tab5" data-ref-type="table">5</a>). Moreover, the final design contained no states with all attributes at the same level, which would make the task excessively difficult, and the PC contained only one dominant comparison out of the 25 comparisons. Overall, it is not a representative sample, but more a stratified sample to the severeness of disease. The questionnaire was designed in a fashion that respondents first were asked to perform the BWS case 2 task with profile A.

<div id="Tab5" class="table-wrap">

<div class="caption">

Fraction chosen health states over the comparator state B (24242) and best–worst counts for that health state for each dimension

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Health state</th>
<th style="text-align: left;">DCE</th>
<th colspan="5" style="text-align: left;">BWS counts</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Fraction chosen</th>
<th style="text-align: left;">Mobility</th>
<th style="text-align: left;">Selfcare</th>
<th style="text-align: left;">Usual activities</th>
<th style="text-align: left;">Pain</th>
<th style="text-align: left;">Depression</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">(44154)<sup>−,+</sup></td>
<td style="text-align: center;">0.211</td>
<td style="text-align: center;"> − 58</td>
<td style="text-align: center;"> − 11</td>
<td style="text-align: center;">258</td>
<td style="text-align: center;"> − 118</td>
<td style="text-align: center;"> − 71</td>
</tr>
<tr>
<td style="text-align: left;">(51445)<sup>+</sup></td>
<td style="text-align: center;">0.253</td>
<td style="text-align: center;"> − 49</td>
<td style="text-align: center;">270</td>
<td style="text-align: center;"> − 37</td>
<td style="text-align: center;"> − 80</td>
<td style="text-align: center;"> − 104</td>
</tr>
<tr>
<td style="text-align: left;">(33544)<sup>−</sup></td>
<td style="text-align: center;">0.271</td>
<td style="text-align: center;">175</td>
<td style="text-align: center;">86</td>
<td style="text-align: center;"> − 73</td>
<td style="text-align: center;"> − 113</td>
<td style="text-align: center;"> − 75</td>
</tr>
<tr>
<td style="text-align: left;">(45335)</td>
<td style="text-align: center;">0.279</td>
<td style="text-align: center;"> − 72</td>
<td style="text-align: center;"> − 7</td>
<td style="text-align: center;">137</td>
<td style="text-align: center;">73</td>
<td style="text-align: center;"> − 131</td>
</tr>
<tr>
<td style="text-align: left;">(53352)<sup>−</sup></td>
<td style="text-align: center;">0.284</td>
<td style="text-align: center;"> − 82</td>
<td style="text-align: center;">68</td>
<td style="text-align: center;">83</td>
<td style="text-align: center;"> − 144</td>
<td style="text-align: center;">75</td>
</tr>
<tr>
<td style="text-align: left;">(12555)<sup>+</sup></td>
<td style="text-align: center;">0.311</td>
<td style="text-align: center;">263</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;"> − 61</td>
<td style="text-align: center;"> − 132</td>
<td style="text-align: center;"> − 97</td>
</tr>
<tr>
<td style="text-align: left;">(55214)<sup>+</sup></td>
<td style="text-align: center;">0.321</td>
<td style="text-align: center;"> − 94</td>
<td style="text-align: center;"> − 36</td>
<td style="text-align: center;">51</td>
<td style="text-align: center;">186</td>
<td style="text-align: center;"> − 107</td>
</tr>
<tr>
<td style="text-align: left;">(54533)</td>
<td style="text-align: center;">0.332</td>
<td style="text-align: center;"> − 75</td>
<td style="text-align: center;"> − 15</td>
<td style="text-align: center;"> − 70</td>
<td style="text-align: center;">152</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: left;">(35451)<sup>+</sup></td>
<td style="text-align: center;">0.334</td>
<td style="text-align: center;">89</td>
<td style="text-align: center;"> − 34</td>
<td style="text-align: center;"> − 70</td>
<td style="text-align: center;"> − 139</td>
<td style="text-align: center;">154</td>
</tr>
<tr>
<td style="text-align: left;">(34225)<sup>−</sup></td>
<td style="text-align: center;">0.366</td>
<td style="text-align: center;">38</td>
<td style="text-align: center;"> − 38</td>
<td style="text-align: center;">90</td>
<td style="text-align: center;">75</td>
<td style="text-align: center;"> − 165</td>
</tr>
<tr>
<td style="text-align: left;">(42242)</td>
<td style="text-align: center;">0.403</td>
<td style="text-align: center;"> − 97</td>
<td style="text-align: center;">64</td>
<td style="text-align: center;">117</td>
<td style="text-align: center;"> − 128</td>
<td style="text-align: center;">44</td>
</tr>
<tr>
<td style="text-align: left;">(15143)<sup>−</sup></td>
<td style="text-align: center;">0.442</td>
<td style="text-align: center;">177</td>
<td style="text-align: center;"> − 40</td>
<td style="text-align: center;">87</td>
<td style="text-align: center;"> − 200</td>
<td style="text-align: center;"> − 24</td>
</tr>
<tr>
<td style="text-align: left;">(43423)<sup>+</sup></td>
<td style="text-align: center;">0.447</td>
<td style="text-align: center;"> − 86</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;"> − 115</td>
<td style="text-align: center;">168</td>
<td style="text-align: center;"> − 11</td>
</tr>
<tr>
<td style="text-align: left;">(22434)</td>
<td style="text-align: center;">0.450</td>
<td style="text-align: center;">134</td>
<td style="text-align: center;">114</td>
<td style="text-align: center;"> − 127</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;"> − 129</td>
</tr>
<tr>
<td style="text-align: left;">(21253)<sup>−,+</sup></td>
<td style="text-align: center;">0.471</td>
<td style="text-align: center;">55</td>
<td style="text-align: center;">213</td>
<td style="text-align: center;"> − 4</td>
<td style="text-align: center;"> − 236</td>
<td style="text-align: center;"> − 28</td>
</tr>
<tr>
<td style="text-align: left;">(25522)</td>
<td style="text-align: center;">0.516</td>
<td style="text-align: center;">130</td>
<td style="text-align: center;"> − 53</td>
<td style="text-align: center;"> − 151</td>
<td style="text-align: center;">67</td>
<td style="text-align: center;">7</td>
</tr>
<tr>
<td style="text-align: left;">(23115)<sup>−</sup></td>
<td style="text-align: center;">0.553</td>
<td style="text-align: center;">5</td>
<td style="text-align: center;">14</td>
<td style="text-align: center;">89</td>
<td style="text-align: center;">109</td>
<td style="text-align: center;"> − 217</td>
</tr>
<tr>
<td style="text-align: left;">(41511)<sup>−</sup></td>
<td style="text-align: center;">0.558</td>
<td style="text-align: center;"> − 117</td>
<td style="text-align: center;">79</td>
<td style="text-align: center;"> − 121</td>
<td style="text-align: center;">130</td>
<td style="text-align: center;">29</td>
</tr>
<tr>
<td style="text-align: left;">(24341)<sup>+</sup></td>
<td style="text-align: center;">0.582</td>
<td style="text-align: center;">61</td>
<td style="text-align: center;"> − 58</td>
<td style="text-align: center;">12</td>
<td style="text-align: center;"> − 180</td>
<td style="text-align: center;">165</td>
</tr>
<tr>
<td style="text-align: left;">(52121)<sup>−</sup></td>
<td style="text-align: center;">0.605</td>
<td style="text-align: center;"> − 195</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">136</td>
<td style="text-align: center;"> − 29</td>
<td style="text-align: center;">66</td>
</tr>
<tr>
<td style="text-align: left;">(14412)</td>
<td style="text-align: center;">0.624</td>
<td style="text-align: center;">146</td>
<td style="text-align: center;"> − 58</td>
<td style="text-align: center;"> − 174</td>
<td style="text-align: center;">122</td>
<td style="text-align: center;"> − 36</td>
</tr>
<tr>
<td style="text-align: left;">(32313)<sup>+</sup></td>
<td style="text-align: center;">0.700</td>
<td style="text-align: center;"> − 35</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;"> − 80</td>
<td style="text-align: center;">212</td>
<td style="text-align: center;"> − 103</td>
</tr>
<tr>
<td style="text-align: left;">(11324)<sup>−</sup></td>
<td style="text-align: center;">0.734</td>
<td style="text-align: center;">182</td>
<td style="text-align: center;">63</td>
<td style="text-align: center;"> − 44</td>
<td style="text-align: center;"> − 72</td>
<td style="text-align: center;"> − 129</td>
</tr>
<tr>
<td style="text-align: left;">(31132)</td>
<td style="text-align: center;">0.745</td>
<td style="text-align: center;"> − 52</td>
<td style="text-align: center;">90</td>
<td style="text-align: center;">149</td>
<td style="text-align: center;"> − 117</td>
<td style="text-align: center;"> − 70</td>
</tr>
<tr>
<td style="text-align: left;">(13231)</td>
<td style="text-align: center;">0.811</td>
<td style="text-align: center;">180</td>
<td style="text-align: center;"> − 60</td>
<td style="text-align: center;"> − 56</td>
<td style="text-align: center;"> − 116</td>
<td style="text-align: center;">52</td>
</tr>
</tbody>
</table>

<sup>+</sup>Indicates that a health state has only one dimension with a maximum level, <sup>−</sup>Indicates that a health state has only one dimension with a minimum level

</div>

Next, for the PC task, the 'Health profile B' that was added as a comparator to the BWS' Health profile A' was always the same profile, namely (24242), a state close to the center of the health-profile continuum (based on Devlin et al. \[23\]) that has three attributes at the same level, and the other two as well. Such a constant comparator design reduces efficiency to around 40–50% but provides the only currently known compromise possible between the needs of the case 2 BWS and the needs of the PC tasks \[24\]. This particular dual design appears unusual but is important in that it has properties that reflect the BWS case 2/PC relationship (investigation of "how I rescale my BWS case 2 estimates into PC-space") and practical benefits (minimizing cognitive load in the PC by familiarizing the respondent with profile A, then adding a constant, known, state B). A sample question of both types of tasks can be found in Appendix <a href="#Sec20" data-ref-type="sec">1</a>, Fig. <a href="#Fig4" data-ref-type="fig">4</a>.

<figure id="Fig4">
<p><img src="12955_2022_1989_Fig4_HTML.jpg" id="MO4" /></p>
<p><img src="12955_2022_1989_Fig4_HTML.gif" /></p>
<figcaption>Sample Questions (in Dutch)</figcaption>
</figure>

### Analysis

The final analysis dropped the dominant task from the PC question. Descriptive statistics were used to summarize respondents' characteristics and response feasibility of PC and BWS tasks. To maximize the use of the available data, we implemented a hybrid modeling approach that incorporated all PC and BWS responses to produce the Dutch EQ-5D-5L value set. Conditional logit model, heteroskedastic conditional logit, and heteroskedastic scale-adjusted latent class (SALC) model were estimated by maximum likelihood to illustrate the values for all 3125 EQ-5D-5L profiles \[25\]. The main effects of each model are shown as incremental changes in the level of severity on a pits scale where value (55555) = 0 and value (11111) = 1 \[13\]. Unlike EQ-VT studies, the study did not use the TTO or include any preferences evidence on "dying immediately;" therefore, the main effects cannot be reported on a quality-adjusted life-year (QALY) scale. Statistical analyses were done in R 4.0.2 \[26–28\]. A significance level of 0.05 was considered statistically significant.

#### Main-effect specification of EQ-5D-5L Values

To aid the interpretation of the BWS responses, we envisioned a profile of '00000' that represents a hypothetical ideal. The BWS specification includes twenty incremental variables, each representing the loss in health values for increasing severity from one level to the next of the same dimension, as well as five ancillary variables associated with a change in level from zero to one, which is outside the EQ-5D-5L descriptive system. The primary difference between the best and the worst responses is that the sign of the incremental variables switches (i.e., for best, the incremental variable is negative; for worst, the variable is positive). The hypothetical ideal is not relevant for the interpretation of the PC responses; therefore, its specification includes only the twenty incremental variables.

The twenty main-effect coefficients describe the value of the EQ-5D-5L profiles on a pits scale. The coefficients of the five ancillary variables have no effect on the EQ-5D-5L values; therefore, these estimated coefficients are reported in Appendix <a href="#Sec20" data-ref-type="sec">1</a>. Due to the identification problems of case-2 BWS, only four of the five ancillary parameters can be non-zero; therefore, we constrained the smallest ancillary parameter to zero, which has no effect on the EQ-5D-5L values.

#### Heteroskedasticity and differences by task

Overall, each PC and BWS response is a multinomial choice (from two and five alternatives, respectively) that reflects a respondent's preferences taking into account the 20 and 25 incremental variables, respectively. The conditional logit model assumes homogeneous preference and independent and identically distributed (IID) errors. Relaxing the IID assumption introduces the heteroskedastic conditional logit (HCL) model \[29\], where the scale parameter (inversely related to the variance) is an exponential function of observable factors that identify the source of differential variance and constrains the scale to be non-negative. The differential variance may be associated with individual level, choice set/task level, or alternative level characteristic variables. To avoid confounding between heteroskedasticity and scale heterogeneity, the scale parameter in this paper depends on only task-level variables, namely task sequence and task type (e.g., best/worst/paired comparison).

Furthermore, we estimated the heteroskedastic logit by task (i.e., BWS case 2 and PC) characteristics, computed the PC and BWS values using the interaction results, and assessed their correlation and agreement (Pearson's correlation and Lin's concordance, respectively).

#### Heterogeneity and EQ-5D-5L Values

The SALC model (model formulation in Appendix <a href="#Sec21" data-ref-type="sec">2</a>) allows for preference heterogeneity through latent classes. Taste classes represent groups that share the relative effects of each attribute level, and scale classes represent groups that share the absolute effects of all attributes. The likelihood that each individual belongs to a specific group is known as a respondent's grade-of-membership (GOM) and may be associated with their observable characteristics. In the analysis, we hypothesize that individuals' demographics, socio-economic variables, and health conditions are associated with taste class membership. The scale class, which identifies the irregularities and idiosyncratic features of choice behavior that are not particularly associated with any attribute level, rather captures the variability across subjects, tasks, and objects are identified by individual's age, education level, gender, competency level (whether passed the dominant task), and perception on the difficulty level between the two question types.

As an extension of the HCL \[30, 31\], the standard SALC model \[20\] identifies differences in scale by latent groups (i.e., scale classes), but scale remains constant within each scale class. \[18, 32\]. A SALC model can allow heteroskedasticity by letting the scale factor vary by observable factors within each scale class (i.e., heteroskedastic SALC).

As the number of classes both for the scale and taste classes is decided prior to the analysis rather than identified from estimation, a series of classes is usually estimated, and the best-fitted model is based on statistical and substantive criteria (i.e., BIC, AIC, CAIC) \[33\]. However, in empirical analysis, factors like a smaller size, complexity in the model, and low efficiency may cause identification problems for a higher dimension solution with many latent classes. This study only collected 380 respondents; therefore, the SALC model includes only two taste and two-scale classes.

In order to compare these values with the original Dutch EQ-5D-5L values \[21\], the original values were transformed to a pits scale, and their relationship was illustrated using a scatter plot and estimates using Pearson's correlation and Lin's concordance.

## Results

### Demographics

After excluding the dominant pair from the PC task, the analysis included 24 PC tasks and 25 BWS tasks. In total, 385 respondents completed the questionnaires, from which five were excluded due to engaging in click-through on the PC (no variation in their responses), so subsequent analyses are based on the remaining 380 respondents. Fifty-two percent (n = 198) of the respondents were male (Table <a href="#Tab1" data-ref-type="table">1</a>). Respondents were almost equally divided among the age group 16 to 35, 36 to 55, and above 55. More than half of the respondents had a middle education (n = 197) compared to thirty-five percent (n = 131) having high education. Fifty-seven percent (n = 217) reported having a chronic illness.

<div id="Tab1" class="table-wrap">

<div class="caption">

Descriptive statistics sample (n = 380)

</div>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">Characteristic</th>
<th style="text-align: left;">n (%)</th>
</tr>
<tr>
<th style="text-align: left;">Gender (N, %)</th>
<th style="text-align: left;">Men</th>
<th style="text-align: left;">198 (52.1%)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Woman</td>
<td style="text-align: left;">182 (47.9%)</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">16- 35</td>
<td style="text-align: left;">124 (32.6%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">16 – 55</td>
<td style="text-align: left;">117 (30.8%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">55 above</td>
<td style="text-align: left;">149 (36.6%)</td>
</tr>
<tr>
<td style="text-align: left;">Educational level</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">52 (13.7%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">197 (51.8%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">131 (34.5%)</td>
</tr>
<tr>
<td style="text-align: left;">Chronical Illness</td>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">217 (57.1%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">No</td>
<td style="text-align: left;">163 (42.9%)</td>
</tr>
<tr>
<td style="text-align: left;">VAS score Health</td>
<td style="text-align: left;"> &lt; 70</td>
<td style="text-align: left;">200 (52.6%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">70 above</td>
<td style="text-align: left;">180 (47.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Difficulty BWS</td>
<td style="text-align: left;">Easy</td>
<td style="text-align: left;">71 (18.7%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Not easy / not difficult</td>
<td style="text-align: left;">192 (50.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Difficult</td>
<td style="text-align: left;">117 (30.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Difficulty PC</td>
<td style="text-align: left;">Easy</td>
<td style="text-align: left;">61 (16.1%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Not easy / not difficult</td>
<td style="text-align: left;">173 (45.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Difficult</td>
<td style="text-align: left;">146 (38.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Easiness BWS/PC</td>
<td style="text-align: left;">BWS</td>
<td style="text-align: left;">135 (35.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">No preference</td>
<td style="text-align: left;">173 (45.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">PC</td>
<td style="text-align: left;">72 (19.0%)</td>
</tr>
<tr>
<td style="text-align: left;">Failed dominant task in PC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">72(19.0%)</td>
</tr>
</tbody>
</table>

</div>

### Feasibility

Thirty-one percent (n = 117) found the best–worst questions difficult, compared to thirty-eight percent (n = 146) for the PCs (Table <a href="#Tab1" data-ref-type="table">1</a>). Seventy-two out of 380 respondents preferred in terms of difficulty the PC questions over the best–worst questions. Almost half of the respondents (n = 173) had no preference. Remarkably, from those indicating BWS easier than PC rated 9/380 = 2.3% the difficulty of PC lower (less difficult) than BWS; those indicating PC is easier than BWS rated 13/380 = 3.4% the difficulty of BWS lower than PC. And finally, from those indicating no preference in the easiness of BWS or PC gave 42/380 = 11.1% a different level of difficulty to the two methods. Also, 72 of the total respondents failed the dominant task.

### Difference between homoskedastic and heteroskedastic results

Table <a href="#Tab2" data-ref-type="table">2</a> showed the main effect estimates of the conditional logit (CL) model and heteroskedastic conditional logit (HCL) model. The HCL model fitted better by lowering the BIC value by 1666.29 (CL BIC: 64,458.32, and HCL BIC: 62,792.03). The correlation between the 3125 values measured by the CL and HCL estimates showed a high correlation (Pearson's correlation coefficient is 0.9953 (CI: 0.9950–0.9956) and Lin's concordance correlation coefficient 0.9927 (CI: 0.9922–0.9932)) (Appendix 1 Fig. <a href="#Fig5" data-ref-type="fig">5</a>). In both models, one incremental coefficient is negative (i.e., the change in severity from severe to extreme under usual activity) but insignificant (CL coefficient: − 0.0003 p-value: 0.956; HCL coefficient: − 0.0011, p-value:0.878). The sequence of completing tasks has a positive effect on the scale parameter (0.8419; p \< 0.001), and its square has a negative effect ( − 0.7427, p \< 0.001), indicating that scale increased (i.e., less random responses) up to fourteen tasks and decreased after that (Fig. <a href="#Fig2" data-ref-type="fig">2</a>) with overall p-value \< 0.001. Also, the effect of the PC task on the scale parameter is significantly negative ( − 0.9930, p-value \< 0.001), and the effect of the best task is significantly positive (0.2424, p-value \< 0.001) (Appendix 1 Table <a href="#Tab6" data-ref-type="table">6</a>). Controlling heteroskedasticity had little effect on the standard errors; the standard error decreased in 8 of the 20 estimated parameters (Appendix 1 Table <a href="#Tab6" data-ref-type="table">6</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

Conditional, heteroskedastic, and interaction model (controlling heteroskedasticity)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">Interaction</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Conditional</th>
<th colspan="2" style="text-align: left;">Heteroskedastic</th>
<th colspan="2" style="text-align: left;">Paired comparison</th>
<th colspan="2" style="text-align: left;">Best worst scaling</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">p-value*</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="10" style="text-align: left;">Mobility</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: center;">0.0879</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0726</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0874</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0261</td>
<td style="text-align: center;">0.192</td>
<td style="text-align: center;">0.001</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: center;">0.0331</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0340</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0232</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0478</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">0.917</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: center;">0.1073</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1097</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1103</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1078</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.451</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: center;">0.0134</td>
<td style="text-align: center;">0.015</td>
<td style="text-align: center;">0.0059</td>
<td style="text-align: center;">0.398</td>
<td style="text-align: center;">0.0025</td>
<td style="text-align: center;">0.662</td>
<td style="text-align: center;">0.0308</td>
<td style="text-align: center;">0.091</td>
<td style="text-align: center;">0.931</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Self-care</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: center;">0.0634</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0623</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0652</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0803</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.278</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: center;">0.0062</td>
<td style="text-align: center;">0.270</td>
<td style="text-align: center;">0.0271</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0276</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0545</td>
<td style="text-align: center;">0.028</td>
<td style="text-align: center;">0.273</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: center;">0.0572</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0370</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0498</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0123</td>
<td style="text-align: center;">0.602</td>
<td style="text-align: center;">0.599</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: center;">0.0170</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0164</td>
<td style="text-align: center;">0.003</td>
<td style="text-align: center;"> − 0.0002</td>
<td style="text-align: center;">0.974</td>
<td style="text-align: center;">0.0559</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">0.999</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Usual activity</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: center;">0.0430</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0588</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0685</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0648</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">0.968</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: center;">0.0299</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0280</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0243</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;"> − 0.0784</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">0.611</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: center;">0.0987</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1002</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1008</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1129</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: center;"> − 0.0003</td>
<td style="text-align: center;">0.956</td>
<td style="text-align: center;"> − 0.0011</td>
<td style="text-align: center;">0.878</td>
<td style="text-align: center;"> − 0.0046</td>
<td style="text-align: center;">0.423</td>
<td style="text-align: center;">0.0312</td>
<td style="text-align: center;">0.083</td>
<td style="text-align: center;">0.999</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Pain/discomfort</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: center;">0.0682</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0802</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0854</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0061</td>
<td style="text-align: center;">0.728</td>
<td style="text-align: center;">0.739</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: center;">0.0125</td>
<td style="text-align: center;">0.025</td>
<td style="text-align: center;">0.0324</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0325</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0637</td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;">0.194</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: center;">0.1244</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1034</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.1160</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0856</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.004</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: center;">0.0297</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0336</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0139</td>
<td style="text-align: center;">0.015</td>
<td style="text-align: center;">0.0970</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.999</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Anxiety/depression</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: center;">0.0649</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0605</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0738</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0106</td>
<td style="text-align: center;">0.636</td>
<td style="text-align: center;">0.002</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: center;">0.0486</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0444</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0319</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0568</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.922</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: center;">0.0565</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0634</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0623</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0735</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.710</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: center;">0.0384</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0310</td>
<td style="text-align: center;">0.003</td>
<td style="text-align: center;">0.0296</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;">0.0575</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">0.926</td>
</tr>
</tbody>
</table>

\*p-value showed the significant difference between the PC and BWS coefficient within the heteroskedastic logit

Coefficients are showing as incremental change in the level of severity on a pits scale where value (55555) = 0 and value (11111) = 1; Detailed results are in Appendix <a href="#Sec20" data-ref-type="sec">1</a>

</div>

<figure id="Fig5">
<p><img src="12955_2022_1989_Fig5_HTML.jpg" id="MO5" /></p>
<p><img src="12955_2022_1989_Fig5_HTML.gif" /></p>
<figcaption>Scatter plot of 3125 EQ-5D-5L profiles for conditional logit and heteroskedastic model. *values were estimated in a pits scale where v (55555) = 0 and v (11111) = 1. 95% Confidence interval for Pearson’s correlation 0.9950–0.9956, and for Lin’s concordance: 0.9922–0.9932</figcaption>
</figure>

<figure id="Fig2">
<p><img src="12955_2022_1989_Fig2_HTML.jpg" id="MO1" /></p>
<p><img src="12955_2022_1989_Fig2_HTML.gif" /></p>
<figcaption>Heteroskedasticity: scale by the task sequence. *Scale coefficients were transformed into the original scale</figcaption>
</figure>

<div id="Tab6" class="table-wrap">

<div class="caption">

Full results of the conditional, heteroskedastic model

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Conditional</th>
<th colspan="3" style="text-align: left;">Heteroskedastic</th>
<th colspan="3" style="text-align: left;">DCE</th>
<th colspan="3" style="text-align: left;">BWS</th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Level 1–2</td>
<td style="text-align: left;">0.0879</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0726</td>
<td style="text-align: center;">0.0047</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0874</td>
<td style="text-align: center;">0.0035</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0261</td>
<td style="text-align: center;">0.0200</td>
<td style="text-align: center;">0.192</td>
<td style="text-align: center;">0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Level 2–3</td>
<td style="text-align: left;">0.0331</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0340</td>
<td style="text-align: center;">0.0046</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0232</td>
<td style="text-align: center;">0.0049</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0478</td>
<td style="text-align: center;">0.0170</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">0.917</td>
</tr>
<tr>
<td style="text-align: left;"> Level 3–4</td>
<td style="text-align: left;">0.1073</td>
<td style="text-align: center;">0.0056</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.1097</td>
<td style="text-align: center;">0.0075</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.1103</td>
<td style="text-align: center;">0.0054</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.1078</td>
<td style="text-align: center;">0.0192</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.451</td>
</tr>
<tr>
<td style="text-align: left;"> Level 4–5</td>
<td style="text-align: left;">0.0134</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: center;">0.015</td>
<td style="text-align: left;">0.0059</td>
<td style="text-align: center;">0.0070</td>
<td style="text-align: left;">0.398</td>
<td style="text-align: center;">0.0025</td>
<td style="text-align: center;">0.0056</td>
<td style="text-align: left;">0.662</td>
<td style="text-align: center;">0.0308</td>
<td style="text-align: center;">0.0181</td>
<td style="text-align: center;">0.091</td>
<td style="text-align: center;">0.931</td>
</tr>
<tr>
<td style="text-align: left;">Self-care</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Level 1–2</td>
<td style="text-align: left;">0.0634</td>
<td style="text-align: center;">0.0054</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0623</td>
<td style="text-align: center;">0.0067</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0652</td>
<td style="text-align: center;">0.0037</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0803</td>
<td style="text-align: center;">0.0177</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.278</td>
</tr>
<tr>
<td style="text-align: left;"> Level 2–3</td>
<td style="text-align: left;">0.0062</td>
<td style="text-align: center;">0.0056</td>
<td style="text-align: center;">0.270</td>
<td style="text-align: left;">0.0271</td>
<td style="text-align: center;">0.0053</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0276</td>
<td style="text-align: center;">0.0050</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0545</td>
<td style="text-align: center;">0.0249</td>
<td style="text-align: center;">0.028</td>
<td style="text-align: center;">0.273</td>
</tr>
<tr>
<td style="text-align: left;"> Level 3–4</td>
<td style="text-align: left;">0.0572</td>
<td style="text-align: center;">0.0054</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0370</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0498</td>
<td style="text-align: center;">0.0053</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0123</td>
<td style="text-align: center;">0.0236</td>
<td style="text-align: center;">0.602</td>
<td style="text-align: center;">0.599</td>
</tr>
<tr>
<td style="text-align: left;"> Level 4–5</td>
<td style="text-align: left;">0.0170</td>
<td style="text-align: center;">0.0050</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0164</td>
<td style="text-align: center;">0.0057</td>
<td style="text-align: left;"> &lt; 0.003</td>
<td style="text-align: center;"> − 0.0002</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: left;">0.974</td>
<td style="text-align: center;">0.0559</td>
<td style="text-align: center;">0.0169</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">0.999</td>
</tr>
<tr>
<td style="text-align: left;">Usual activity</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Level 1–2</td>
<td style="text-align: left;">0.0430</td>
<td style="text-align: center;">0.0052</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0588</td>
<td style="text-align: center;">0.0081</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0685</td>
<td style="text-align: center;">0.0037</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0648</td>
<td style="text-align: center;">0.0235</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">0.968</td>
</tr>
<tr>
<td style="text-align: left;"> Level 2–3</td>
<td style="text-align: left;">0.0299</td>
<td style="text-align: center;">0.0052</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0280</td>
<td style="text-align: center;">0.0052</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0243</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"> − 0.0784</td>
<td style="text-align: center;">0.0237</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">0.611</td>
</tr>
<tr>
<td style="text-align: left;"> Level 3–4</td>
<td style="text-align: left;">0.0987</td>
<td style="text-align: center;">0.0057</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.1002</td>
<td style="text-align: center;">0.0071</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.1008</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.1129</td>
<td style="text-align: center;">0.0187</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"> Level 4–5</td>
<td style="text-align: left;"> − 0.0003</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: center;">0.956</td>
<td style="text-align: left;"> − 0.0011</td>
<td style="text-align: center;">0.0072</td>
<td style="text-align: left;">0.878</td>
<td style="text-align: center;"> − 0.0046</td>
<td style="text-align: center;">0.0057</td>
<td style="text-align: left;">0.423</td>
<td style="text-align: center;">0.0312</td>
<td style="text-align: center;">0.0180</td>
<td style="text-align: center;">0.083</td>
<td style="text-align: center;">0.999</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Level 1–2</td>
<td style="text-align: left;">0.0682</td>
<td style="text-align: center;">0.0053</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0802</td>
<td style="text-align: center;">0.0063</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0854</td>
<td style="text-align: center;">0.0037</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0061</td>
<td style="text-align: center;">0.0177</td>
<td style="text-align: center;">0.728</td>
<td style="text-align: center;">0.739</td>
</tr>
<tr>
<td style="text-align: left;"> Level 2–3</td>
<td style="text-align: left;">0.0125</td>
<td style="text-align: center;">0.0056</td>
<td style="text-align: center;">0.025</td>
<td style="text-align: left;">0.0324</td>
<td style="text-align: center;">0.0074</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0325</td>
<td style="text-align: center;">0.0050</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0637</td>
<td style="text-align: center;">0.0249</td>
<td style="text-align: center;">0.010</td>
<td style="text-align: center;">0.194</td>
</tr>
<tr>
<td style="text-align: left;"> Level 3–4</td>
<td style="text-align: left;">0.1244</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.1034</td>
<td style="text-align: center;">0.0071</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.1160</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0856</td>
<td style="text-align: center;">0.0221</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"> Level 4–5</td>
<td style="text-align: left;">0.0297</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0336</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0139</td>
<td style="text-align: center;">0.0057</td>
<td style="text-align: left;">0.015</td>
<td style="text-align: center;">0.0970</td>
<td style="text-align: center;">0.0167</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.999</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Level 1–2</td>
<td style="text-align: left;">0.0649</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0605</td>
<td style="text-align: center;">0.0047</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0738</td>
<td style="text-align: center;">0.0038</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0106</td>
<td style="text-align: center;">0.0223</td>
<td style="text-align: center;">0.636</td>
<td style="text-align: center;">0.002</td>
</tr>
<tr>
<td style="text-align: left;"> Level 2–3</td>
<td style="text-align: left;">0.0486</td>
<td style="text-align: center;">0.0051</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0444</td>
<td style="text-align: center;">0.0050</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0319</td>
<td style="text-align: center;">0.0053</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0568</td>
<td style="text-align: center;">0.0166</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.922</td>
</tr>
<tr>
<td style="text-align: left;"> Level 3–4</td>
<td style="text-align: left;">0.0565</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0634</td>
<td style="text-align: center;">0.0172</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0623</td>
<td style="text-align: center;">0.0057</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0735</td>
<td style="text-align: center;">0.0193</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;">0.710</td>
</tr>
<tr>
<td style="text-align: left;"> Level 4–5</td>
<td style="text-align: left;">0.0384</td>
<td style="text-align: center;">0.0055</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0310</td>
<td style="text-align: center;">0.0105</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: center;">0.0296</td>
<td style="text-align: center;">0.0057</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">0.0575</td>
<td style="text-align: center;">0.0184</td>
<td style="text-align: center;">0.001</td>
<td style="text-align: center;">0.926</td>
</tr>
<tr>
<td style="text-align: left;">Ancillary parameters</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> SC (Level 0–1)</td>
<td style="text-align: left;">0.0513</td>
<td style="text-align: center;">0.0058</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0349</td>
<td style="text-align: center;">0.0046</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> UA (Level 0–1)</td>
<td style="text-align: left;">0.0638</td>
<td style="text-align: center;">0.0058</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0348</td>
<td style="text-align: center;">0.0050</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> PD (Level0-1)</td>
<td style="text-align: left;">0.0549</td>
<td style="text-align: center;">0.0056</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0207</td>
<td style="text-align: center;">0.0072</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> AD (Level 0–1)</td>
<td style="text-align: left;">0.0740</td>
<td style="text-align: center;">0.0056</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">0.0584</td>
<td style="text-align: center;">0.0054</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Pits Value</td>
<td style="text-align: left;">8.7724</td>
<td style="text-align: center;">0.1138</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: left;">8.8533</td>
<td style="text-align: center;">0.3201</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">8.7669</td>
<td style="text-align: center;">0.1194</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;">8.5402</td>
<td style="text-align: center;">0.4977</td>
<td style="text-align: center;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Heteroskedasticity*</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Intercept</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Task sequence</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0.8402</td>
<td style="text-align: center;">0.1664</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Task sequence^2</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"> − 0.7439</td>
<td style="text-align: center;">0.1608</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Task type</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Worst</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">_</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> Best</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">0.2424</td>
<td style="text-align: center;">0.0246</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"> PC</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"> − 0.9931</td>
<td style="text-align: center;">0.0404</td>
<td style="text-align: left;"> &lt; 0.000</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Log-likelihood</td>
<td style="text-align: left;"> − 32,106.1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"> − 31,252.3</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"> − 31,160.3</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td style="text-align: left;">64,458.32</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">62,792.03</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Sample Size</td>
<td style="text-align: left;">18,620</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">18,620</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;">18,620</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

\*Heteroskedastic coefficients presented in log-scale term

</div>

### Differences between the PC and BWS results

Table <a href="#Tab2" data-ref-type="table">2</a> also showed the main-effect coefficients of PC and BWS for the heteroskedastic logit model. In the PC estimates, 17 out of 20 coefficients were significant (p \< 0.05); however, two coefficients were negative but insignificantly different from zero. Under BWS, 13 coefficients were significant, with one significant negative estimate. Only four coefficients have shown a significant difference by task, and the largest difference is 0.1027. Converting the 3125 EQ-5D-5L values into a pits scale, we measured the correlation between PC and BWS values. (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). Between the two 3125 EQ-5D-5L profiles, Pearson's correlation coefficient is 0.9167 (CI: 0.9109–0.9222), and Lin's concordance correlation coefficient is 0.7658 (CI: 0.7542–0.7769). The median absolute difference in the difference between PC and BWS values has 0.0732 (interquartile range 0.0592 to 0.1565).

<figure id="Fig1">
<p><img src="12955_2022_1989_Fig1_HTML.jpg" id="MO2" /></p>
<p><img src="12955_2022_1989_Fig1_HTML.gif" /></p>
<figcaption>Scatter plot of 3125 EQ-5D-5L profiles for heteroskedastic model. *values were estimated in a pits scale where v (55555) = 0 and v (11111) = 1. 95% Confidence interval for Pearson’s correlation 0.9109–0.9222, and for Lin’s concordance: 0.7542–0.7769</figcaption>
</figure>

### Taste and scale heterogeneity

The SALC model increased model fit compared to homogeneous models by achieving the lowest BIC value (56,698.35). Table <a href="#Tab3" data-ref-type="table">3</a> showed the main-effect coefficients of the two taste classes. Taste class 1 had consistent parameters with non-negative values, and 19 of them were significant (p \< 0.050). In all the attributes, changing levels from moderate to severe problems led to the greatest reduction in value. Based on this evidence, taste class 1 is referred to as a Dutch EQ-5D-5L value set on the pits scale.

<div id="Tab3" class="table-wrap">

<div class="caption">

Two taste classes of the scale-adjusted latent class (SALC) model

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Taste class 1<br />
EQ-5D-5L values set</th>
<th colspan="2" style="text-align: left;">Taste class 2<br />
garbage class</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;">Mobility</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0586</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.2954</td>
<td style="text-align: center;">0.004</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0290</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.1132</td>
<td style="text-align: center;">0.348</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.1205</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.1903</td>
<td style="text-align: center;">0.159</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0090</td>
<td style="text-align: center;">0.017</td>
<td style="text-align: left;"> − 0.0825</td>
<td style="text-align: center;">0.518</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Self-care</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0553</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.2140</td>
<td style="text-align: center;">0.143</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0246</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.2202</td>
<td style="text-align: center;">0.127</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.0630</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0745</td>
<td style="text-align: center;">0.531</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0082</td>
<td style="text-align: center;">0.030</td>
<td style="text-align: left;">0.2378</td>
<td style="text-align: center;">0.048</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Usual activity</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0516</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.0386</td>
<td style="text-align: center;">0.794</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0297</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0073</td>
<td style="text-align: center;">0.964</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.1115</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0431</td>
<td style="text-align: center;">0.767</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0002</td>
<td style="text-align: center;">0.967</td>
<td style="text-align: left;">0.0544</td>
<td style="text-align: center;">0.745</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Pain/discomfort</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0686</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.1218</td>
<td style="text-align: center;">0.438</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0290</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0898</td>
<td style="text-align: center;">0.585</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.1085</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.0930</td>
<td style="text-align: center;">0.575</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0346</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.1657</td>
<td style="text-align: center;">0.341</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">Anxiety/depression</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0558</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.3042</td>
<td style="text-align: center;">0.037</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0412</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.0648</td>
<td style="text-align: center;">0.643</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.0753</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.0241</td>
<td style="text-align: center;">0.885</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0262</td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: left;">0.1455</td>
<td style="text-align: center;">0.354</td>
</tr>
<tr>
<td style="text-align: left;">Prob (11111 &gt; 55555) **</td>
<td style="text-align: left;">.998</td>
<td style="text-align: center;"></td>
<td style="text-align: left;">.554</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

Coefficients are showing as incremental change in the level of severity on a pits scale where value (55555) = 0 and value (11111) = 1; Detailed results are in Appendix <a href="#Sec20" data-ref-type="sec">1</a>

\*\*The probability of choosing the best over the worst EQ-5D-5L profile is less than 56% in taste class 2 (calculating probability from the difference between v (11111) and v (55555) on a log-odds scale which is the pits value .2161; log (p/((1-p)) = 0.2161). In this study, taste class 2 is called the garbage class because the responses were unrelated to the ordinal attributes

</div>

On the other hand, taste class 2 had few significant parameters and eight inconsistent estimates. In this class, the probability of choosing the best over the worst EQ-5D-5L profile is 0.554 (Table <a href="#Tab3" data-ref-type="table">3</a>), which is much smaller than the near-unanimous probability found in taste class 1 (0.998). Based on this evidence, taste class 2 is referred to as a garbage class.

Around 71% of the individuals belonged to taste class 1 and 29% in taste class 2 (Table <a href="#Tab4" data-ref-type="table">4</a>). Looking at the grade-of-membership results, respondents in the garbage class are less likely to be female (odds ratio: 0.5173 95% CI: 0.3685 to 0.6661) and more likely to be younger (odds ratio: 2.4143; 95% CI: 1.6509 to 3.1777).

<div id="Tab4" class="table-wrap">

<div class="caption">

Grade-of-membership (GOM) of the scale-adjusted latent class (SALC)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">GOM for taste class 2<br />
garbage class (29% of respondents)</th>
<th colspan="2" style="text-align: left;">GOM for scale class 2 more random class (59% of respondents)</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">0.5022</td>
<td style="text-align: center;">0.098</td>
<td style="text-align: center;">0.5453</td>
<td style="text-align: center;">0.117</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">0.5173</td>
<td style="text-align: center;">0.022</td>
<td style="text-align: center;">1.0399</td>
<td style="text-align: center;">0.882</td>
</tr>
<tr>
<td style="text-align: left;">Age in years</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"> &lt; 0.001</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.875</td>
</tr>
<tr>
<td style="text-align: left;">16–35</td>
<td style="text-align: left;">2.4143</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">1.1669</td>
<td style="text-align: center;">0.554</td>
</tr>
<tr>
<td style="text-align: left;">36–54</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">above 55</td>
<td style="text-align: left;">0.2100</td>
<td style="text-align: center;">0.011</td>
<td style="text-align: center;">1.4360</td>
<td style="text-align: center;">0.141</td>
</tr>
<tr>
<td style="text-align: left;">Educational attainment*</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.686</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.697</td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">0.6366</td>
<td style="text-align: center;">0.388</td>
<td style="text-align: center;">0.8678</td>
<td style="text-align: center;">0.705</td>
</tr>
<tr>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: left;">0.9140</td>
<td style="text-align: center;">0.839</td>
<td style="text-align: center;">0.9635</td>
<td style="text-align: center;">0.911</td>
</tr>
<tr>
<td style="text-align: left;">Chronic Illness</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">1.0643</td>
<td style="text-align: center;">0.895</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">VAS score Health</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Below 70</td>
<td style="text-align: left;">1.8346</td>
<td style="text-align: center;">0.249</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">70 &gt; </td>
<td style="text-align: left;">–</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Difficulty level</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Failed dominant task</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">3.1286</td>
<td style="text-align: center;">0.044</td>
</tr>
<tr>
<td style="text-align: left;">Found tasks easy</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1.1337</td>
<td style="text-align: center;">0.834</td>
</tr>
<tr>
<td style="text-align: left;">Found tasks hard</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.6152</td>
<td style="text-align: center;">0.140</td>
</tr>
</tbody>
</table>

Results are shown on the odds ratio scale. For education, the lowest group included up to the primary, the medium group included secondary to associates, and the highest group included bachelor's degrees and above. The standard errors are shown in Appendix 1 Table <a href="#Tab8" data-ref-type="table">8</a>

</div>

The scale is lower in scale class 2 than in scale class 1, which implies scale class 2 has a higher variance (Appendix 1 Table <a href="#Tab7" data-ref-type="table">7</a>). In scale class 1 (less random class), the effect of the sequence of tasks on the scale has a similar pattern as in the heteroskedastic model (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). However, the coefficient of the sequence square was not significant (Appendix 1 Table <a href="#Tab7" data-ref-type="table">7</a> and Fig. <a href="#Fig2" data-ref-type="fig">2</a>). The effect of task type (i.e., PC or BWS) is the same across both classes, where PC is negatively associated with scale (i.e., increased uncertainty/randomness) and the best task under BWS is positively associated with scale factor (i.e., reduce uncertainty/randomness) (Appendix 1 Table <a href="#Tab7" data-ref-type="table">7</a>). However, the coefficients were only significant in scale class 1. Around 41% of the respondents belong to scale class 1 and 59% to scale class 2. Respondents in scale class 2 were more likely to fail the PC dominant task (Table <a href="#Tab4" data-ref-type="table">4</a>).

<div id="Tab7" class="table-wrap">

<div class="caption">

Full result of the SALC model

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Class 1<br />
(Value set)</th>
<th colspan="3" style="text-align: left;">Class 2<br />
(Garbage class)</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coeff</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coeff</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7" style="text-align: left;">Mobility</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0586</td>
<td style="text-align: left;">0.0029</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.2954</td>
<td style="text-align: left;">0.1024</td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0290</td>
<td style="text-align: left;">0.0030</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.1132</td>
<td style="text-align: left;">0.1206</td>
<td style="text-align: left;">0.348</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.1205</td>
<td style="text-align: left;">0.0037</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.1903</td>
<td style="text-align: left;">0.1351</td>
<td style="text-align: left;">0.159</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0090</td>
<td style="text-align: left;">0.0038</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;"> − 0.0825</td>
<td style="text-align: left;">0.1275</td>
<td style="text-align: left;">0.518</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Self-care</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0553</td>
<td style="text-align: left;">0.0034</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.2140</td>
<td style="text-align: left;">0.1462</td>
<td style="text-align: left;">0.143</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0246</td>
<td style="text-align: left;">0.0034</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.2202</td>
<td style="text-align: left;">0.1445</td>
<td style="text-align: left;">0.127</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.0630</td>
<td style="text-align: left;">0.0037</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0745</td>
<td style="text-align: left;">0.1189</td>
<td style="text-align: left;">0.531</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0082</td>
<td style="text-align: left;">0.0038</td>
<td style="text-align: left;">0.030</td>
<td style="text-align: left;">0.2378</td>
<td style="text-align: left;">0.1204</td>
<td style="text-align: left;">0.048</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Usual activity</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0516</td>
<td style="text-align: left;">0.0028</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.0386</td>
<td style="text-align: left;">0.1477</td>
<td style="text-align: left;">0.794</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0297</td>
<td style="text-align: left;">0.0031</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0073</td>
<td style="text-align: left;">0.1628</td>
<td style="text-align: left;">0.964</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.1115</td>
<td style="text-align: left;">0.0037</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0431</td>
<td style="text-align: left;">0.1458</td>
<td style="text-align: left;">0.767</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0002</td>
<td style="text-align: left;">0.0037</td>
<td style="text-align: left;">0.967</td>
<td style="text-align: left;">0.0544</td>
<td style="text-align: left;">0.1677</td>
<td style="text-align: left;">0.745</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Pain/discomfort</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0686</td>
<td style="text-align: left;">0.0030</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.1218</td>
<td style="text-align: left;">0.1570</td>
<td style="text-align: left;">0.438</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0290</td>
<td style="text-align: left;">0.0029</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.0898</td>
<td style="text-align: left;">0.1645</td>
<td style="text-align: left;">0.585</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.1085</td>
<td style="text-align: left;">0.0034</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.0930</td>
<td style="text-align: left;">0.1659</td>
<td style="text-align: left;">0.575</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0346</td>
<td style="text-align: left;">0.0036</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;"> − 0.1657</td>
<td style="text-align: left;">0.1739</td>
<td style="text-align: left;">0.341</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Anxiety/depression</td>
</tr>
<tr>
<td style="text-align: left;">Level 1–2</td>
<td style="text-align: left;">0.0558</td>
<td style="text-align: left;">0.0028</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.3042</td>
<td style="text-align: left;">0.1456</td>
<td style="text-align: left;">0.037</td>
</tr>
<tr>
<td style="text-align: left;">Level 2–3</td>
<td style="text-align: left;">0.0412</td>
<td style="text-align: left;">0.0033</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.0648</td>
<td style="text-align: left;">0.1399</td>
<td style="text-align: left;">0.643</td>
</tr>
<tr>
<td style="text-align: left;">Level 3–4</td>
<td style="text-align: left;">0.0753</td>
<td style="text-align: left;">0.0041</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.0241</td>
<td style="text-align: left;">0.1664</td>
<td style="text-align: left;">0.885</td>
</tr>
<tr>
<td style="text-align: left;">Level 4–5</td>
<td style="text-align: left;">0.0262</td>
<td style="text-align: left;">0.0039</td>
<td style="text-align: left;"> &lt; 0.001</td>
<td style="text-align: left;">0.1455</td>
<td style="text-align: left;">0.1570</td>
<td style="text-align: left;">0.354</td>
</tr>
<tr>
<td style="text-align: left;">Pits value</td>
<td style="text-align: left;">6.4267</td>
<td style="text-align: left;">0.6489</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.2161</td>
<td style="text-align: left;">0.0710</td>
<td style="text-align: left;">0.002</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Ancillary parameter</td>
</tr>
<tr>
<td style="text-align: left;">SC (Level 0–1)</td>
<td style="text-align: left;">0.0221</td>
<td style="text-align: left;">0.0027</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">0.264</td>
<td style="text-align: left;">0.148</td>
<td style="text-align: left;">0.074</td>
</tr>
<tr>
<td style="text-align: left;">UA (Level 0–1)</td>
<td style="text-align: left;">0.0078</td>
<td style="text-align: left;">0.0023</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">1.039</td>
<td style="text-align: left;">0.309</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD (Level 0–1)</td>
<td style="text-align: left;"> − 0.0030</td>
<td style="text-align: left;">0.0023</td>
<td style="text-align: left;">0.197</td>
<td style="text-align: left;">1.540</td>
<td style="text-align: left;">0.479</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD (Level 0–1)</td>
<td style="text-align: left;">0.0248</td>
<td style="text-align: left;">0.0025</td>
<td style="text-align: left;">0.000</td>
<td style="text-align: left;">1.234</td>
<td style="text-align: left;">0.422</td>
<td style="text-align: left;">0.003</td>
</tr>
<tr>
<td style="text-align: left;">Heteroskedasticity*</td>
<td style="text-align: left;">Scale class 1</td>
<td style="text-align: left;">Scale class 2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">1.0067</td>
<td style="text-align: left;">0.0930</td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Task sequence</td>
<td style="text-align: left;">1.9589</td>
<td style="text-align: left;">0.1990</td>
<td style="text-align: left;">0.220</td>
<td style="text-align: left;">1.0155</td>
<td style="text-align: left;">0.3280</td>
<td style="text-align: left;">0.562</td>
</tr>
<tr>
<td style="text-align: left;">Task sequence^2</td>
<td style="text-align: left;"> − 1.6698</td>
<td style="text-align: left;">0.2004</td>
<td style="text-align: left;">0.222</td>
<td style="text-align: left;"> − 0.6295</td>
<td style="text-align: left;">0.3028</td>
<td style="text-align: left;">0.519</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">Task type</td>
</tr>
<tr>
<td style="text-align: left;">Worst</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Best</td>
<td style="text-align: left;">0.383</td>
<td style="text-align: left;">0.043</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;">0.5628</td>
<td style="text-align: left;">0.0547</td>
<td style="text-align: left;">0.054</td>
</tr>
<tr>
<td style="text-align: left;">PC</td>
<td style="text-align: left;"> − 1.301</td>
<td style="text-align: left;">0.047</td>
<td style="text-align: left;"> − 0.049</td>
<td style="text-align: left;"> − 0.8878</td>
<td style="text-align: left;">0.0955</td>
<td style="text-align: left;">0.097</td>
</tr>
<tr>
<td style="text-align: left;">Log-likelihood</td>
<td style="text-align: left;"> − 27,969.64</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td style="text-align: left;">56,698.35</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Sample Size</td>
<td style="text-align: left;">18,620</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

\*Heteroskedastic coefficients presented in log-scale term

</div>

### Differences between the original and new Dutch EQ-5D-5L values

Comparing the twenty main-effect coefficients estimated in this study with those of the original Dutch value set \[21\], the SALC coefficients had the highest correlation and agreement (Pearson’s correlation: 0.7295, CI: 0.4238–0.8860; Lin’s concordance: 0.6904, CI: 0.4098–0.8516), followed by conditional logit (Pearson’s correlation: 0.6937, CI: 0.3626–0.8693; Lin’s concordance: 0.6601, CI: 0.3554–0.8380) and heteroskedastic conditional logit (Pearson’s correlation: 0.6321, CI: 0.2632–0.8398; Lin’s concordance: 0.5817, CI: 0.2543–0.7894) (Fig. <a href="#Fig3" data-ref-type="fig">3</a>) \[34\]. Looking across the 3125 EQ-5D-5L values, the SALC values had the highest correlation and agreement (Pearson’s correlation: 0.9293, CI: 0.9244–0.9339; Lin’s concordance: 0.8835 CI: 0.8763–0.8903), followed by conditional (Pearson’s correlation: 0.9254, CI: 0.9203–0.9304; Lin’s concordance: 0.8689, CI: 0.8610–0.8764) and, heteroskedastic (Pearson’s correlation: 0.9226, CI: 0.9172–0.9277; Lin’s concordance: 0.8453, CI: 0.8364–0.8537).

<figure id="Fig3">
<p><img src="12955_2022_1989_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="12955_2022_1989_Fig3_HTML.gif" /></p>
<figcaption>Comparing estimated coefficients with the Dutch value set. *Pearson's correlation coefficient for the 20 the conditional (0.6937), heteroskedastic (0.6321), and SALC (0.7295) coefficients</figcaption>
</figure>

## Discussion

Using a population-based sample from the Netherlands, we estimated the value of EQ-5D-5L profiles by task and controlling for heteroskedasticity and heterogeneity. Apart from heteroskedasticity, identifying taste heterogeneity often becomes difficult because of its confounding nature with scales. In this paper, we estimated a heteroskedastic conditional logit and a scale-adjusted latent class model to emphasize three sources of error related to respondent behavior: (1) task sequence, (2) garbage classes, and (3) failing a PC dominance task.

First, heteroskedasticity may occur as individuals' attention span reduces doing tasks consecutively \[30, 35\]). Interestingly, after controlling for heteroskedasticity, only a few incremental coefficients differ significantly between BWS and PC, which suggests the tasks might be used interchangeably. Second, the members of the garbage class may be indifferent between EQ-5D-5L profiles or respond randomly (i.e., a shuffled deck)\[36\]. Although these motives are confounded, this class did not express relative attribute importance; therefore, their responses can be disregarded as uninformative. Lastly, respondents who failed the PC dominance task were more likely to belong to a class with a lower scale, which implies that less weight was given to their preference evidence. Overall, the SALC model adjusts the EQ-5D-5L values to better represent the tasks in the middle of the sequence and persons who did not belong to the garbage class or failed the PC dominance test. By controlling heteroskedasticity and heterogeneity, this study produced a Dutch EQ-5D-5L value set on a pits scale that is moderately concordant with the original values. The moderate agreement is in line with our expectation as the study used an online sample with smaller sample size compared to the original study.

This study has several limitations. First, the results of the estimated model were shown on a pits scale rather than on a QALY scale. Second, this study is more of an exploratory study rather than a confirmatory analysis, which complicates the interpretation of p-values or statistical inference more generally. Third, the confounding between taste and scale in choice-based analysis implies that adjusting the scale might not totally control the scale factor from preference coefficients. Also, due to the design with a constant comparator in PC tasks and relatively smaller sample size, our capability to explore heterogeneity in larger dimensions was beyond the scope. Lastly, important variables such as income and time to complete the tasks were missing in the dataset, which would have been good indicators for class membership, as shown in previous studies \[18\]. Given this, this study is the first attempt to explore heteroskedasticity and heterogeneity in a health valuation study and should aid others considering similar approaches. It is also worth to be mentioned that the SALC model is a certain parametrization of a particular type of disentangling taste and scale. So, the results would be dependent on that particular parametrization and require justified theoretical background.

## Conclusions

In conclusion, this study suggests that proper consideration regarding the sources of variation that affect individuals' decision rules can be included to inform the model analysis in health valuation studies. Considering the demonstrated potential of the case-2 BWS task to produce similar values as of PC, this study produced a Dutch EQ-5D-5L value set on a pits scale that is concordant with the original values by controlling heteroskedasticity and heterogeneity. In order to emphasize the importance of controlling the noises in the dataset, this method should be implemented in future studies with larger sample size and with richer behavioral information.

## Acknowledgements

The authors would like to thank the EuroQol Group for funding this study (Grant EQ Project 2016220, EQ Project 138-2020RA. The authors would also like to thank Dr. Terry Flynn and Dr. Sander Arons for their assistance with the project's proposal, experimental design, and primary data collection.

## Abbreviations

BWS  
Best–worst scaling

EQ-5D-5L  
EuroQol 5 Domains 5 Levels

GOM  
Grade-of-membership

HPR  
Health preference research

OMEP  
Orthogonal main effects plan

PC  
Paired comparison

SALC  
Scale-adjusted latent class

TTO  
Time trade-off

### Appendix 1

See Figs. <a href="#Fig4" data-ref-type="fig">4</a>, <a href="#Fig5" data-ref-type="fig">5</a>, <a href="#Fig6" data-ref-type="fig">6</a>, <a href="#Fig7" data-ref-type="fig">7</a>.

<figure id="Fig6">
<p><img src="12955_2022_1989_Fig6_HTML.jpg" id="MO6" /></p>
<p><img src="12955_2022_1989_Fig6_HTML.gif" /></p>
<figcaption>Distribution of Individual grade-of-membership in taste class 1 from 2scale-2taste class SALC model</figcaption>
</figure>

<figure id="Fig7">
<p><img src="12955_2022_1989_Fig7_HTML.jpg" id="MO7" /></p>
<p><img src="12955_2022_1989_Fig7_HTML.gif" /></p>
<figcaption>Distribution of Individual grade-of-membership in scale class 1 from 2scale-2taste class SALC model</figcaption>
</figure>

See Tables <a href="#Tab5" data-ref-type="table">5</a>, <a href="#Tab6" data-ref-type="table">6</a>, <a href="#Tab7" data-ref-type="table">7</a>, <a href="#Tab8" data-ref-type="table">8</a>.

<div id="Tab8" class="table-wrap">

<div class="caption">

Full result: Grade of membership (GOM) of the scale-adjusted latent class (SALC)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">GOM for taste class 2<br />
Garbage class (29% of respondents)</th>
<th colspan="3" style="text-align: left;">GOM for scale class 2 Uncertain class (59% of respondents)</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Coeff</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
<th style="text-align: left;">Coeff</th>
<th style="text-align: left;">S.E</th>
<th style="text-align: left;">p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: center;">0.5022</td>
<td style="text-align: center;">0.2092</td>
<td style="text-align: center;">0.098</td>
<td style="text-align: center;">0.5453</td>
<td style="text-align: center;">0.7102</td>
<td style="text-align: center;">0.117</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">0.5173</td>
<td style="text-align: center;">0.1488</td>
<td style="text-align: center;">0.022</td>
<td style="text-align: center;">1.0399</td>
<td style="text-align: center;">0.2529</td>
<td style="text-align: center;">0.882</td>
</tr>
<tr>
<td style="text-align: left;">Age in years</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">16–35</td>
<td style="text-align: center;">2.4143</td>
<td style="text-align: center;">0.7634</td>
<td style="text-align: center;">0.005</td>
<td style="text-align: center;">1.1669</td>
<td style="text-align: center;">0.2236</td>
<td style="text-align: center;">0.554</td>
</tr>
<tr>
<td style="text-align: left;">36–54</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">above 55</td>
<td style="text-align: center;">0.2100</td>
<td style="text-align: center;">0.1292</td>
<td style="text-align: center;">0.011</td>
<td style="text-align: center;">1.4360</td>
<td style="text-align: center;">0.1712</td>
<td style="text-align: center;">0.141</td>
</tr>
<tr>
<td style="text-align: left;">Educational attainment</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">0.6366</td>
<td style="text-align: center;">0.3328</td>
<td style="text-align: center;">0.388</td>
<td style="text-align: center;">0.8678</td>
<td style="text-align: center;">0.4312</td>
<td style="text-align: center;">0.705</td>
</tr>
<tr>
<td style="text-align: left;">Medium</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">0.9140</td>
<td style="text-align: center;">0.4058</td>
<td style="text-align: center;">0.839</td>
<td style="text-align: center;">0.9635</td>
<td style="text-align: center;">0.3450</td>
<td style="text-align: center;">0.911</td>
</tr>
<tr>
<td style="text-align: left;">Chronic Illness</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">1.0643</td>
<td style="text-align: center;">0.5052</td>
<td style="text-align: center;">0.895</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">VAS score Health</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Below 70</td>
<td style="text-align: center;">1.8346</td>
<td style="text-align: center;">0.9661</td>
<td style="text-align: center;">0.249</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">70 &gt; </td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Difficulty level</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Failed dominant task</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">3.1286</td>
<td style="text-align: center;">0.1814</td>
<td style="text-align: center;">0.044</td>
</tr>
<tr>
<td style="text-align: left;">Found tasks easy</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1.1337</td>
<td style="text-align: center;">0.5275</td>
<td style="text-align: center;">0.834</td>
</tr>
<tr>
<td style="text-align: left;">Found tasks hard</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.6152</td>
<td style="text-align: center;">0.5356</td>
<td style="text-align: center;">0.140</td>
</tr>
</tbody>
</table>

Results are shown on the odds ratio scale. For education, the lowest group included up to the primary, the medium group included secondary to associates, and the highest group included bachelor’s degrees and above

</div>

### Appendix 2

#### Scale-adjusted latent class (SALC) model

The scale-adjusted latent class model \[20\] is an advanced version of the latent class model in the context of stated choice experiment studies. The latent class model assumes that the population can be decomposed into distinct number of latent classes where each class differs by their preferences (different sets of coefficients). The latent class model is restricted by the assumption of constant scale. The SALC model relax the assumption of constant scale and assumes that the population can be decomposed in two overlapping ways: classes defined by S different scales $`\mu_{s}`$ and classes defined by M different effects $`\beta_{m}`$. This would further imply that, despite sharing the same coefficients, within the same effect class, some subjects may display different levels of uncertainty, thereby belonging to different scale classes. So, the probability of choice $`j`$ by subject $`i`$ in choice situation $`t`$, conditional on scale class s and effect class *m* is

``` math
P{(y_{\mathit{itj}}|s,m)} = \frac{e^{\mu_{s}\beta_{m}'x_{\mathit{itj}}}}{\sum_{k = 1}^{S_{\mathit{it}}}e^{\mu_{s}\beta_{m}'x_{\mathit{itk}}}};j,k \in S_{\mathit{it}}
```

$`S_{\mathit{it}}`$ is the choice set that includes objects specific to individual’s choice situation, and for example, in a binary logit model, each $`S_{\mathit{it}}`$ includes two objects. Similar to the latent class model, the SALC model also identifies class memberships in a probabilistic fashion. However, two different sets of covariates have been used to identify effect and scale class membership ($`z_{1i}`$ and $`z_{2i}`$, respectively). For the effect class, the class assignment will be associated with individual characteristics that are related to preference. On the other hand, scale classes are differentiated by subject's randomness in behavior (e.g., certainty). So, to identify scale class membership we have considered variables related to subjects’ characteristics that might influence their randomness in behavior. As both sets of covariates includes some common variables, each set includes at least one unique variable to identify the model. As for example, demographics \[age, gender, race, ethnicity\] and SES\[educational attainment, household income\]) characteristics influence both preference and scale. However, individual’s current usage of a specific product might influence their preference but not related to any randomness in behavior. On the other hand, behavioral phenomena like time of the day when the survey was completed, and survey completion time period are variables that relate with individual’s randomness in behavior and nothing to do with their taste. In both cases, the covariates are included in multinomial logit models

``` math
P{(m|z_{1i})} = \frac{\exp(\delta_{m}'z_{1i})}{\sum_{k = 1}^{M}\exp{(\delta_{k}'z_{1i})}}
```

``` math
P{(s|z_{2i})} = \frac{\exp(\theta_{s}'z_{2i})}{\sum_{k = 1}^{S}\exp{(\theta_{k}'z_{2i})}}
```

The full choice model of each subject $`i`$ becomes

``` math
P\left( {y_{i}|z_{i},q_{i}} \right) = \sum\limits_{s = 1}^{S}P\left( {{s|}z_{2i}} \right)\sum\limits_{m = 1}^{M}P\left( {{m|}z_{1i}} \right)\prod\limits_{t = 1}^{T}\prod\limits_{j = 1}^{J}P{(y_{\mathit{itj}}|s,m)}^{y_{\mathit{itj}}}
```

This likelihood function *L* is simply a joint cumulative density function (CDF) made up of choice probabilities, scale class probabilities $`P(s|z_{i})`$, and effect class probabilities $`P(m|z_{i})`$. Hence, the overall log-likelihood function for all subjects becomes

``` math
\ln L = \sum\limits_{n = 1}^{N}\ln\left\lbrack {P\left( {y_{i}|z_{i}} \right)} \right\rbrack = \sum\limits_{i = 1}^{N}\ln\left\lbrack {\sum\limits_{s = 1}^{S}P\left( {{s|}z_{2i}} \right)\sum\limits_{m = 1}^{M}P\left( {{m|}z_{1i}} \right)\prod\limits_{t = 1}^{T}\prod\limits_{j = 1}^{J}P{(y_{\mathit{itj}}|s,m)}^{y_{\mathit{itj}}}} \right\rbrack
```

The scale—factor can also be modeled by linear equation. The rationale behind this specification is that the scale factor may depend on latent class and/or independent variable. In order to remain the scale parameter as non-negative, we are constraining the scale parameter as $`\exp(\mu_{s})`$. So, the scale factor model contains a term for scale class and effect of independent variables ($`z_{3it}`$).

``` math
\mu_{s} = \gamma_{s0} + \sum\limits_{z_{3it} = 1}^{Kz_{3}}\gamma_{s1}z_{3it}
```

where for s = 1, the constant term $`\gamma_{s0}`$ is 0 for the identification purpose.

Here in the model, the independent variables are sequence of choice task and time spent per choice task. So, independent variables are task(*t*) specific.

## Author contributions

Catharina G.M. Groothuis-Oudshoorn was primarily involved in experimental design and data collection. Suzana Karim and Benjamin M. Craig were involved in data analysis. All authors contributed to the development of the manuscript. All authors read and approved the final manuscript.

## Funding

EuroQol Group funded this study Grant EQ Project 2016220, EQ Project 138-2020RA.

## Availability of data and materials

The dataset and analysis code are available from the corresponding author upon request.

## Declarations

### Ethics approval and consent to participate

All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki declaration and its later amendments or comparable ethical standards.

### Consent for publication

Not applicable.

### Competing interests

Catharina G.M. Groothuis-Oudshoorn and Suzana Karim received grants from the EuroQol Research Foundation. Dr. Benjamin M Craig is a member of the EuroQol Research Foundation.

## Footnotes

## References

## References

1. Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L) Qual Life Res. 2011;20:1727–1736. doi: 10.1007/s11136-011-9903-x.

2. de Bekker-Grob EW, Ryan M, Gerard K. Discrete choice experiments in health economics: a review of the literature. Health Econ. 2012;21:145–172. doi: 10.1002/hec.1697.

3. Vass CM, Boeri M, Karim S, et al. Accounting for preference heterogeneity in discrete-choice experiments: a review of the state of practice. Value Health. 2022;25:685–94. doi: 10.1016/j.jval.2022.01.012.

4. Craig BM, Lancsar E, Mühlbacher AC, et al. Health preference research: an overview. Patient. 2017;10:507–510. doi: 10.1007/s40271-017-0253-9.

5. Soekhai V, de Bekker-Grob EW, Ellis AR, et al. Discrete choice experiments in health economics: past, present and future. Pharmacoeconomics. 2019;37:201–226. doi: 10.1007/s40273-018-0734-2.

6. Oppe M, Rand-Hendriksen K, Shah K, et al. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34:993–1004. doi: 10.1007/s40273-016-0404-1.

7. Bansback N, Tsuchiya A, Brazier J, et al. Canadian valuation of EQ-5D health states: preliminary value set and considerations for future valuation studies. PLoS ONE. 2012;7:e31115. doi: 10.1371/journal.pone.0031115.

8. Craig BM, Busschbach JJ, Salomon JA. Modeling ranking, time trade-off, and visual analog scale values for EQ-5D health states: a review and comparison of methods. Med Care. 2009;47:634–641. doi: 10.1097/MLR.0b013e31819432ba.

9. Craig BM, Pickard AS, Stolk E, et al. US valuation of the SF-6D. Med Decis Mak. 2013;33:793–803. doi: 10.1177/0272989X13482524.

10. Farkas M, Huynh E, Gulácsi L, et al. Development of population tariffs for the ICECAP-A instrument for hungary and their comparison With the UK Tariffs. Value in Health. 2021. doi:10.1016/j.jval.2021.06.011

11. Krucien N, Watson V, Ryan M. Is best-worst scaling suitable for health state valuation? A comparison with discrete choice experiments. Health Econ. 2017;26:e1–e16. doi: 10.1002/hec.3459.

12. Xie F, Pullenayegum E, Gaebel K, et al. Eliciting preferences to the EQ-5D-5L health states: discrete choice experiment or multiprofile case of best-worst scaling? Eur J Health Econ. 2014;15:281–288. doi: 10.1007/s10198-013-0474-3.

13. Craig BM, Busschbach JJV, Salomon JA. Keep it simple: ranking health states yields values similar to cardinal measurement approaches. J Clin Epidemiol. 2009;62:296–305. doi: 10.1016/j.jclinepi.2008.07.002.

14. Flynn TN, Louviere JJ, Peters TJ, et al. Best–worst scaling: What it can do for health care research and how to do it. J Health Econ. 2007;26:171–189. doi: 10.1016/j.jhealeco.2006.04.002.

15. Louviere J, Eagle T. Confound it! That Pesky Little Scale Constant Messes Up Our Convenient Assumptions. In: Proceedings of the Sawtooth Software Conference. 2006: 211–28.

16. Craig BM, de Bekker-Grob EW, González Sepúlveda JM, et al. A guide to observable differences in stated preference evidence. Patient. 2021: 1–11. doi:10.1007/s40271-021-00551-x

17. Louviere J, Hensher D, Swait J. Stated choice methods: analysis and application. 2000.

18. Karim S, Craig BM, Poteet S. Does controlling for scale heterogeneity better explain respondents' preference segmentation in discrete choice experiments? A case study of us health insurance demand. Med Decis Mak. 2021;41:573–583. doi: 10.1177/0272989X21997345.

19. Groothuis-Oudshoorn C, Flynn T, Yoo H, et al. Key issues and potential solutions for understanding healthcare preference heterogeneity free from patient-level scale confounds. Patient Patient Cent Outcomes Res. 2018;11:1–4. doi: 10.1007/s40271-017-0264-6.

20. Magidson J, Vermunt J. Removing the Scale Factor Confound in Multinomial Logit Choice Models to Obtain Better Estimates of Preference 1. Sawtooth Softw Conf. 2007.

21. Versteegh MM, Vermeulen KM, Evers SMAA, et al. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19:343–352. doi: 10.1016/j.jval.2016.01.003.

22. Reed Johnson F, Lancsar E, Marshall D, et al. Constructing experimental designs for discrete-choice experiments: report of the ISPOR conjoint analysis experimental design good research practices task force. Value Health. 2013;16:3–13. doi: 10.1016/j.jval.2012.08.2223.

23. Devlin NJ, Shah KK, Feng Y, et al. Valuing health-related quality of life: An EQ-5D-5L value set for England. Health Econ. 2018;27:7–22. doi: 10.1002/hec.3564.

24. Marley AAJ, Flynn TN, Louviere JJ. Probabilistic models of set-dependent and attribute-level best-worst choice. J Math Psychol. 2008;52:281–296. doi: 10.1016/j.jmp.2008.02.002.

25. Ramos-Goñi JM, Pinto-Prades JL, Oppe M, et al. Valuation and modeling of EQ-5D-5L health states using a hybrid approach. Med Care. 2017;55:e51–e58. doi: 10.1097/MLR.0000000000000283.

26. Team RDC. R: A language and environment for statistical computing. Vienna, Austria: R Foundation for Statistical Computing, 2020.

27. Hat O. maxLik: a package for maximum likelihood estimation in R. Comput Stat. 2011;26:443–458. doi: 10.1007/s00180-010-0217-1.

28. Hadley W, Mara A, Jennifer B, et al. Welcome to the tidyverse. J Open Source Softw. 2019;4:1686. doi: 10.21105/joss.01686.

29. Hole AR. Small-sample properties of tests for heteroscedasticity in the conditional logit model. Econ Bull. 2006;3:1–14.

30. Deshazo JR, Fermo G. Designing choice sets for stated preference methods: the effects of complexity on choice consistency. J Environ Econ Manag. 2002;44:123–143. doi: 10.1006/jeem.2001.1199.

31. Davis K, Burton M, Kragt M. Scale heterogeneity and its implications for discrete choice analysis. Land Econ. 2019;95:353–368. doi: 10.3368/le.95.3.353.

32. Hess S, Train K. Correlation and scale in mixed logit models. J Choice Modell. 2017;23:1–8. doi: 10.1016/j.jocm.2017.03.001.

33. Greene W, Hensher D. A latent class model for discrete choice analysis: contrasts with mixed logit. Transp Res Part B Methodol. 2003;37:681–698. doi: 10.1016/S0191-2615(02)00046-2.

34. Mv M, Mv K, Maae S, et al. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19:343–352. doi: 10.1016/j.jval.2016.01.003.

35. Swait J, Adamowicz W. The influence of task complexity on consumer choice: a latent class model of decision strategy switching. J Consum Res. 2001;28:135–148. doi: 10.1086/321952.

36. Craig BM, Ramachandran S. Relative risk of a shuffled deck: a generalizable logical consistency criterion for sample selection in health state valuation studies. Health Econ. 2006;15:835–848. doi: 10.1002/hec.1108.

## Associated Data

### Data Availability Statement

The dataset and analysis code are available from the corresponding author upon request.

[^1]: Rotating OMEP coding means permuting the levels of one or more of the attributes such that an equivalent OMEP design is obtained.

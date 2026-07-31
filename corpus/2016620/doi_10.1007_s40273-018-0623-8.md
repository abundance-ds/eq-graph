---
project_id: "2016620"
work_id: "doi:10.1007/s40273-018-0623-8"
doi: "10.1007/s40273-018-0623-8"
pmid: "29470821"
pmcid: "PMC5954015"
title: "Is EQ-5D-5L Better Than EQ-5D-3L? A Head-to-Head Comparison of Descriptive Systems and Value Sets from Seven Countries"
journal: "Pharmacoeconomics"
publication_date: "2018-02-22"
volume: "36"
issue: "6"
authors:
  - name: "Mathieu F Janssen"
    affiliation_ids:
      - "Aff1"
  - name: "Gouke J Bonsel"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
  - name: "Nan Luo"
    affiliation_ids:
      - "Aff4"
affiliations:
  - id: "Aff1"
    name: "Department of Medical Psychology and Psychotherapy, Erasmus MC, Erasmus University, PO Box 2040, 3000 CA Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "Department of Public Health, Erasmus MC, Erasmus University, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "Division Mother and Child, UMC Utrecht, University of Utrecht, Utrecht, The Netherlands"
  - id: "Aff4"
    name: "Saw Swee Hock School of Public Health, National University of Singapore, Singapore, Singapore"
licence: "cc-by-nc"
source_file: "input/projects/2016620/papers/doi_10.1007_s40273-018-0623-8.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5954015/fullTextXML"
source_method: "epmc_xml"
source_sha256: "2a5a43812d1a00c19537929de21d93d39c6c96d87f3c70ccdf24de4f3d6d21ce"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Is EQ-5D-5L Better Than EQ-5D-3L? A Head-to-Head Comparison of Descriptive Systems and Value Sets from Seven Countries

## Abstract

### Objective

This study describes the first empirical head-to-head comparison of EQ-5D-3L (3L) and EQ-5D-5L (5L) value sets for multiple countries.

### Methods

A large multinational dataset, including 3L and 5L data for eight patient groups and a student cohort, was used to compare 3L versus 5L value sets for Canada, China, England/UK (5L/3L, respectively), Japan, The Netherlands, South Korea and Spain. We used distributional analyses and two methods exploring discriminatory power: relative efficiency as assessed by the *F* statistic, and an area under the curve for the receiver-operating characteristics approach. Differences in outcomes were explored by separating descriptive system effects from valuation effects, and by exploring distributional location effects.

### Results

In terms of distributional evenness, efficiency of scale use and the face validity of the resulting distributions, 5L was superior, leading to an increase in sensitivity and precision in health status measurement. When compared with 5L, 3L systematically overestimated health problems and consequently underestimated utilities. This led to bias, i.e. over- or underestimations of discriminatory power.

### Conclusion

We conclude that 5L provides more precise measurement at individual and group levels, both in terms of descriptive system data and utilities. The increased sensitivity and precision of 5L is likely to be generalisable to longitudinal studies, such as in intervention designs. Hence, we recommend the use of the 5L across applications, including economic evaluation, clinical and public health studies. The evaluative framework proved to be useful in assessing preference-based instruments and might be useful for future work in the development of descriptive systems or health classifications.

Issue date 2018.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| EQ-5D-5L (5L) is superior to EQ-5D-3L (3L) with respect to various measurement properties, enabling improvements in sensitivity and precision in health status measurement. |
| 5L provides more precise measurements than 3L at individual and group levels, both in terms of responses to EQ-5D items and the resultant utilities. |
| 3L systematically overestimates health problems when compared with 5L, leading to biased utilities. |
| 5L is recommended for use across applications, including economic evaluation, clinical studies, quality of care and in public health studies. |

</div>

## Introduction

Since the introduction of the original EQ-5D descriptive system in 1990 \[1\] and the first value set in 1997 \[2\], the EuroQol Group has continuously furthered research aimed at enhancing the instrument \[3, 4\]. This entailed refining the descriptive system, developing new valuation methodology and also developing new EQ-5D instruments for specific use. Examples of the latter include the child-friendly EQ-5D version (EQ-5D-Y) as a more comprehensible instrument suitable for children and adolescents \[5, 6\], and the exploration of EQ-5D versions with one or two additional dimensions to the descriptive system \[7–10\]. Arguably, the biggest change has been in refining the ‘granularity’ of the five dimensions by replacing the three response options (levels) of the original EQ-5D (now ‘EQ-5D-3L’) with five levels. The official EQ-5D-5L descriptive system (for convenience we use the term ‘5L’ from here) has been available since 2011 \[11\] and is currently available in more than 150 translations and multiple modes of administration \[12\]. In parallel, a new valuation protocol for the 5L was developed (EQ-VT) to establish new country-specific value sets, warranting a high level of standardisation and quality control as well as introducing new and improved valuation methods \[13, 14\].

Several studies have compared the descriptive systems of EQ-5D-3L (for convenience we use the term ‘3L’ from here) and 5L in terms of their measurement properties, including distributional characteristics such as ceiling effects and evenness, reliability and various types of validity \[15–22\]. Most studies showed that the 5L descriptive system had better or at least similar measurement properties compared with 3L, but two remarks apply. First, we must establish whether the increased descriptive richness of 5L will increase measurement precision rather than measurement error, as this a trade-off. Further, considering that the EQ-5D is a preference-based instrument, it is essential also to investigate whether the increased descriptive richness translates into increased sensitivity of its utility-based index values (hereafter ‘utility values’ or ‘utilities’); again, error may increase due to the increased difficulty in valuing more refined health states. The final question is whether the combined descriptive and valuation effects of 5L improve the discriminatory potential of the utility instrument in, for example, the estimation of quality-adjusted life-years (QALYs) in economic evaluation. As the measurement of health status with the descriptive system is independent from the derivation of utility values and involves different methodologies, improved sensitivity and discrimination of the descriptive system does not necessarily translate into better discriminatory power using utilities (comparing groups or comparing pre- and post-intervention health state). For economic evaluation (e.g. cost-utility analysis), improved discriminatory performance of the utility values would represent a major advantage.

To compare the performance of 3L and 5L in terms of QALYs gained, longitudinal patient-level data on both 3L and 5L in one or multiple study populations would be preferred. In the absence of such longitudinal data we compared 3L and 5L using data from a large multi-country cross-sectional survey, applying country-specific value sets for seven countries.

We first compared the distributional characteristics of the observed utility values by value set, and standard descriptive statistics by condition group and value set. Our main analysis consisted of two tests of discriminatory power. In order to further clarify and explain the results, we performed an exploratory analysis to determine the factors responsible for certain patterns in the results. In this analysis, a clear distinction was made between differences caused by descriptive system results and by the utility values applied to the descriptive data. The separation of descriptive and valuation effects has proven to be of use in an earlier study exploring differences in utilities derived from different preference-based instruments \[23\]. We introduce an evaluative framework consisting of a novel combination of non-parametric methods to establish increased measurement refinement (if any), with parametric methods to demonstrate improved discrimination (if any); 5L is only better than (rather than ‘different from’) 3L if (1) more response levels are efficiently used without a decrease of uniformity of the distribution and (2) this increased use is not offset by more measurement error, both in terms of description and valuation.

Our study had two research questions: (1) Do 5L value sets perform better than 3L value sets in terms of discriminatory power, as a direct result of the improved descriptive sensitivity? (2) What are the underlying factors affecting this performance? Our approach allowed us to make normative assessments on the performance of both instruments and to offer recommendations to users of EQ-5D instruments.

## Methods

### Paired EQ-5D-3L–EQ-5D-5L (3L–5L) Descriptive Data

A large multinational dataset that included paired descriptive 3L and 5L data for eight patient groups and a student cohort was used \[15, 24\]. These data were obtained with the standard 3L and 5L versions for self-report use in adults, describing health on the dimensions of mobility, self-care, usual activities, pain/discomfort and anxiety/depression. The 3L version applied the level descriptors (or labels) ‘no problems’, ‘some/moderate problems’ and ‘extreme problems/unable to’, and the 5L version used ‘no problems’, ‘slight problems’, ‘moderate problems’, ‘severe problems’ and ‘extreme problems/unable to’. For mobility, the most severe response option was changed from ‘confined to bed’ for 3L to ‘unable to walk about’ for 5L. The 3L classification describes 243 unique health states (or health profiles) that are often reported as vectors ranging from 11111 (full health) to 33333 (worst health), whereas the 5L defines 3125 unique health states, with 55555 as the worst health state.

Paper-and-pencil versions of the questionnaires were used in all countries except in England where data collection took place online. Since there were many condition-specific subgroups with small sample sizes, it was decided to combine related patient groups, resulting in nine main condition groups. Only respondents who completed both the 3L and 5L[^1] without any missing responses were included in the analyses (a 3L–5L comparison of missing values is reported elsewhere \[15\]). It was assumed that within a specific condition group country differences were not important so that descriptive data could be pooled.

### Paired 3L–5L Value Sets

At the time of this study there were seven countries with both 3L and 5L value sets available, namely Canada, China, England/UK (5L/3L, respectively), Japan, The Netherlands, South Korea and Spain \[2, 25–37\]. All EQ-5D value sets were obtained using representative samples of the general public, ensuring that they represented the societal perspective. A value set is a set of weights that can convert each health state into an index value on a scale anchored at 1 (referring to full health) and 0 (referring to a state as bad as being dead), allowing for negative values for health states considered to be worse than dead. Most 3L valuation studies followed similar protocols, although there were notable differences with regard to the sampling of respondents (affecting representation), sample size and health state design (varying from 17 to 101 valued health states) \[38, 39\]. All 3L valuation studies were performed with face-to-face interviews and paper-and-pencil methods except for Canada where a web survey was used. All 3L value sets were based on time trade-off (TTO) data. With the introduction of 5L a standardised valuation protocol was developed, the EQ-VT (EuroQol Valuation Technology Platform) \[13\]. In addition to standardisation in terms of health state design, valuation methodology and a computer-assisted personal interview mode of administration, a strict protocol of interviewer training and quality control during the entirety of the data collection process was developed and implemented \[14\]. Discrete choice experiment (DCE) methodology was introduced in the EQ-VT, along with composite TTO as the main valuation method. Since there is no standardised analytic protocol, some 5L value sets were based on hybrid models utilising both TTO and DCE data while others were based on TTO data only. After the initial valuation studies were performed using EQ-VT version 1.0 (Canada, China, England, The Netherlands, Spain) some data quality issues and interviewer effects were apparent and a cyclic quality control process was introduced in version 1.1, which led to a substantial improvement \[14\].

Usually country-specific utility values are used to conduct analyses in a population or patient sample from that particular country, reflecting the appropriate preferences. Since our research questions were of a methodological nature, aiming at making generalisations across value set characteristics, we used the pooled multi-country dataset to compare the characteristics of 14 country-specific 3L and 5L value sets.

### Analyses

#### 3L and 5L Value Sets for Seven Countries

Characteristics of all value sets were reported in terms of model parameters and model characteristics, such as the modelled value range, intercept, interaction parameters and histograms of all possible values (3L: 243; 5L: 3125), which may be responsible for differences in performance between 3L and 5L (see Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of EQ-5D-3L and EQ-5D-5L value sets from seven countries

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">3L and 5L value set models</th>
<th colspan="2" style="text-align: left;">Canada</th>
<th colspan="2" style="text-align: left;">China</th>
<th colspan="2" style="text-align: left;">England/UK</th>
<th colspan="2" style="text-align: left;">Japan</th>
<th colspan="2" style="text-align: left;">The Netherlands</th>
<th colspan="2" style="text-align: left;">South Korea</th>
<th colspan="2" style="text-align: left;">Spain</th>
</tr>
<tr>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L<sup>a</sup></th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: center;">0.051</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.081</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.152</td>
<td style="text-align: left;">0.061</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.047</td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;">0.096</td>
<td style="text-align: left;">0.024</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Mobility</td>
</tr>
<tr>
<td style="text-align: left;"> Slight</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.039</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.066</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.064</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.035</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.046</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.084</td>
</tr>
<tr>
<td style="text-align: left;"> Some/moderate</td>
<td style="text-align: left;">0.046</td>
<td style="text-align: center;">0.078</td>
<td style="text-align: left;">0.099</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">0.069</td>
<td style="text-align: left;">0.076</td>
<td style="text-align: left;">0.075</td>
<td style="text-align: left;">0.113</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.057</td>
<td style="text-align: left;">0.096</td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.099</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.168</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.287</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.207</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.179</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.166</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.133</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.250</td>
</tr>
<tr>
<td style="text-align: left;"> Confined to bed/unable to</td>
<td style="text-align: left;">0.322</td>
<td style="text-align: center;">0.207</td>
<td style="text-align: left;">0.246</td>
<td style="text-align: left;">0.345</td>
<td style="text-align: left;">0.314</td>
<td style="text-align: left;">0.274</td>
<td style="text-align: left;">0.418</td>
<td style="text-align: left;">0.243</td>
<td style="text-align: left;">0.161</td>
<td style="text-align: left;">0.203</td>
<td style="text-align: left;">0.418</td>
<td style="text-align: left;">0.251</td>
<td style="text-align: left;">0.430</td>
<td style="text-align: left;">0.337</td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Self-care</td>
</tr>
<tr>
<td style="text-align: left;"> Slight</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.046</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.048</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.044</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.038</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.032</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.050</td>
</tr>
<tr>
<td style="text-align: left;"> Some/moderate</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: center;">0.092</td>
<td style="text-align: left;">0.105</td>
<td style="text-align: left;">0.116</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.080</td>
<td style="text-align: left;">0.054</td>
<td style="text-align: left;">0.077</td>
<td style="text-align: left;">0.082</td>
<td style="text-align: left;">0.061</td>
<td style="text-align: left;">0.046</td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;">0.134</td>
<td style="text-align: left;">0.053</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.196</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.210</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.164</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.124</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.164</td>
</tr>
<tr>
<td style="text-align: left;"> Unable to</td>
<td style="text-align: left;">0.224</td>
<td style="text-align: center;">0.242</td>
<td style="text-align: left;">0.208</td>
<td style="text-align: left;">0.253</td>
<td style="text-align: left;">0.214</td>
<td style="text-align: left;">0.203</td>
<td style="text-align: left;">0.102</td>
<td style="text-align: left;">0.160</td>
<td style="text-align: left;">0.152</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">0.136</td>
<td style="text-align: left;">0.122</td>
<td style="text-align: left;">0.309</td>
<td style="text-align: left;">0.196</td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Usual activities</td>
</tr>
<tr>
<td style="text-align: left;"> Slight</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.020</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.044</td>
</tr>
<tr>
<td style="text-align: left;"> Some/moderate</td>
<td style="text-align: left;">0.072</td>
<td style="text-align: center;">0.039</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">0.107</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.044</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">0.032</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.051</td>
<td style="text-align: left;">0.051</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.048</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.169</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.194</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.162</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.148</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.192</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.100</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.135</td>
</tr>
<tr>
<td style="text-align: left;"> Unable to</td>
<td style="text-align: left;">0.105</td>
<td style="text-align: center;">0.188</td>
<td style="text-align: left;">0.193</td>
<td style="text-align: left;">0.233</td>
<td style="text-align: left;">0.094</td>
<td style="text-align: left;">0.184</td>
<td style="text-align: left;">0.133</td>
<td style="text-align: left;">0.175</td>
<td style="text-align: left;">0.057</td>
<td style="text-align: left;">0.192</td>
<td style="text-align: left;">0.208</td>
<td style="text-align: left;">0.175</td>
<td style="text-align: left;">0.195</td>
<td style="text-align: left;">0.153</td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Pain/discomfort</td>
</tr>
<tr>
<td style="text-align: left;"> Slight</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.044</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.058</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.045</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.066</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.042</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.078</td>
</tr>
<tr>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.045</td>
<td style="text-align: center;">0.089</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">0.138</td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.080</td>
<td style="text-align: left;">0.068</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">0.037</td>
<td style="text-align: left;">0.053</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">0.101</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.274</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.252</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.276</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.131</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.360</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.166</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.245</td>
</tr>
<tr>
<td style="text-align: left;"> Extreme</td>
<td style="text-align: left;">0.298</td>
<td style="text-align: center;">0.319</td>
<td style="text-align: left;">0.236</td>
<td style="text-align: left;">0.302</td>
<td style="text-align: left;">0.386</td>
<td style="text-align: left;">0.335</td>
<td style="text-align: left;">0.194</td>
<td style="text-align: left;">0.191</td>
<td style="text-align: left;">0.329</td>
<td style="text-align: left;">0.415</td>
<td style="text-align: left;">0.151</td>
<td style="text-align: left;">0.207</td>
<td style="text-align: left;">0.261</td>
<td style="text-align: left;">0.382</td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Anxiety/depression</td>
</tr>
<tr>
<td style="text-align: left;"> Slight</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.038</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.049</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.072</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.070</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.033</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.081</td>
</tr>
<tr>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: center;">0.075</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.063</td>
<td style="text-align: left;">0.110</td>
<td style="text-align: left;">0.124</td>
<td style="text-align: left;">0.145</td>
<td style="text-align: left;">0.043</td>
<td style="text-align: left;">0.046</td>
<td style="text-align: left;">0.062</td>
<td style="text-align: left;">0.128</td>
</tr>
<tr>
<td style="text-align: left;"> Severe</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.241</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.215</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.285</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.357</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.102</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.270</td>
</tr>
<tr>
<td style="text-align: left;"> Extreme</td>
<td style="text-align: left;">0.280</td>
<td style="text-align: center;">0.278</td>
<td style="text-align: left;">0.205</td>
<td style="text-align: left;">0.258</td>
<td style="text-align: left;">0.236</td>
<td style="text-align: left;">0.289</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.196</td>
<td style="text-align: left;">0.325</td>
<td style="text-align: left;">0.421</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">0.137</td>
<td style="text-align: left;">0.144</td>
<td style="text-align: left;">0.348</td>
</tr>
<tr>
<td colspan="15" style="text-align: left;">Interaction parameters</td>
</tr>
<tr>
<td style="text-align: left;"> N3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.022</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.269</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.291</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Num45sq</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">0.0085</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
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
<td style="text-align: left;"> C4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.078</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Highest value (11111)</td>
<td style="text-align: left;">1</td>
<td style="text-align: center;">0.949</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;">Second highest value</td>
<td style="text-align: left;">0.844</td>
<td style="text-align: center;">0.929</td>
<td style="text-align: left;">0.887</td>
<td style="text-align: left;">0.955</td>
<td style="text-align: left;">0.883</td>
<td style="text-align: left;">0.950</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">0.895</td>
<td style="text-align: left;">0.897</td>
<td style="text-align: left;">0.918</td>
<td style="text-align: left;">0.913</td>
<td style="text-align: left;">0.883</td>
<td style="text-align: left;">0.914</td>
<td style="text-align: left;">0.956</td>
</tr>
<tr>
<td style="text-align: left;">Lowest value (33333/55555)</td>
<td style="text-align: left;">− 0.340</td>
<td style="text-align: center;">–0.148</td>
<td style="text-align: left;">− 0.149</td>
<td style="text-align: left;">− 0.386</td>
<td style="text-align: left;">− 0.594</td>
<td style="text-align: left;">− 0.285</td>
<td style="text-align: left;">− 0.111</td>
<td style="text-align: left;">− 0.025</td>
<td style="text-align: left;">− 0.329</td>
<td style="text-align: left;">− 0.446</td>
<td style="text-align: left;">− 0.171</td>
<td style="text-align: left;">− 0.066</td>
<td style="text-align: left;">− 0.654</td>
<td style="text-align: left;">− 0.416</td>
</tr>
<tr>
<td style="text-align: left;">Value range</td>
<td style="text-align: left;">1.340</td>
<td style="text-align: center;">1.097</td>
<td style="text-align: left;">1.149</td>
<td style="text-align: left;">1.386</td>
<td style="text-align: left;">1.594</td>
<td style="text-align: left;">1.285</td>
<td style="text-align: left;">1.111</td>
<td style="text-align: left;">1.025</td>
<td style="text-align: left;">1.329</td>
<td style="text-align: left;">1.446</td>
<td style="text-align: left;">1.171</td>
<td style="text-align: left;">1.066</td>
<td style="text-align: left;">1.654</td>
<td style="text-align: left;">1.416</td>
</tr>
</tbody>
</table>

*3L* EQ-5D-3L, *5L* EQ-5D-5L, *C4* number of level 4s or 5s beyond the first one, *N3* any level 3, *Num45sq* number of level 4s or 5s beyond the first one squared

<sup>a</sup>The 5L model for China is based on an underlying multiplicative eight-parameter model

</div>

#### Distributional Analyses of 3L and 5L Utility Values

Country-specific 3L and 5L utility values were calculated for each value set for all condition groups combined and described numerically and graphically using histograms. We examined clusters and discontinuities (‘gaps’) in the histograms as such patterns theoretically diminish the sensitivity and the accuracy of the instruments and might lead to estimation problems \[40\].

In order to assess the frequency and efficiency of use of the utility scale we applied Shannon’s indices as a means of assessing distributional evenness \[17, 18, 21, 22\]. While Shannon’s *H*′ captures absolute informativity and is simultaneously powered by evenness and the number of categories used, Shannon’s J’ index of relative informativity solely reflects the evenness of a distribution \[41\]. Since Shannon’s *J*′ corrects for the total number of possible categories (here: possible utility values), which could be potentially close (or equal) to 243 for 3L and 3125 for 5L, it was not considered to be a fair comparison (we expected that *J*′ would result in higher values for 3L for this reason). Hence, we also calculated both indices by subdividing the scale range in categories (‘bins’) with a width of 0.05, making the number of categories between 3L and 5L more comparable.

Subsequently, we presented mean utility values (and standard deviations \[SDs\]) by condition group for all 14 value sets, with the addition of an equal weighting score (Level Sum Score \[LSS\] transformed to a 0–1 scale) in order to assess the impact of the descriptive data without the effect of utility weights. The transformed LSS (tLSS) was calculated by summing the level scores for the five dimensions and performing a linear transformation on this sum score to a 0–1 scale so that the value for 11111 is equal to 1.0 and 33333 (for 3L) or 55555 (for 5L) is equal to 0.

#### Discriminatory Performance of 5L Versus 3L

Two tests of discriminatory power were conducted, accommodating different distributional assumptions with respect to utility values: one based on the *F* statistic (parametric), the second on receiver-operating characteristics (non-parametric).

Discriminatory power was assessed using the *F* statistic derived from analysis of variance (ANOVA) to test the equality of means. The *F* statistic is widely used to assess the relative efficiency of patient-reported outcome measures \[21, 42, 43\] and is based on differences in group means divided by the standard error of the difference. A higher *F* statistic means a higher likelihood for a measure to show statistical significance when used to compare groups. Hence, higher *F* statistic values indicate higher discriminatory power. To express the discriminatory power of 5L relative to 3L we computed the ratio of their *F* statistics resulting from comparisons of different condition groups, in such a way that a ratio higher than 1.0 indicated that 5L was more discriminative than 3L: relative efficiency = *F* statistic<sub>5L</sub>/*F* statistic<sub>3L</sub>.

Comparisons were made between (1) the eight disease groups and the student cohort, assuming the students were a valid proxy for a healthy population sample; and (2) patients with a mild condition versus those with a moderate or severe condition. Using the observed mean EQ-5D visual analogue scale (EQ VAS) ratings as reference, we defined diabetes and liver disease as mild conditions (relative to the other conditions), and the remaining six as moderate to severe conditions. Since our main aim was to compare measurement properties of 3L and 5L, we considered this method to be suitable for assessing their ability to distinguish between mild and moderate/severe condition groups.

As a second analysis, we calculated the area under the receiver-operating characteristics curve (AUROC) as a non-parametric method of assessing discriminatory power. AUROC analyses were performed for each pair of condition group comparisons using pooled data on the groups, with group membership being the outcome and the 3L/5L utility score being the exposure. AUROCs for 3L and 5L were calculated and the ratio (5L/3L) was used as the measure of discriminatory power. The AUROC value can range from 0.5 (no prediction) to 1.0 (perfect prediction). Consequently, a 5L/3L AUROC ratio \> 1.0 indicates 5L to be more discriminative than 3L. While the *F* statistic is directly based on means and dispersion, the AUROC employs the full distribution.

For all comparisons 95% confidence intervals (CIs) of the *F* statistic and AUROC ratios were calculated using 3000 bootstrap samples, enabling us to test whether the ratio was statistically different from 1.0.

#### Exploration of Factors Affecting Discriminatory Power

At least three separate factors determine discriminatory power results:

1.  The effects of the descriptive system, involving choice of dimensions, number of levels and corresponding labels, translation effects and reporting heterogeneity.

2.  Valuation effects, relating to the valuation protocol, the valuation study (interviewer effects, quality control, etc.) but also to the modelling of the valuation data. Valuation effects also encompass true country-specific variation in preferences, which may be caused by many underlying factors, e.g. cultural, geographical or related to demographics, language or health system.

3.  A third factor is related to the ability of any scale to capture the location of a respondent on the true latent scale. The precision of measuring this location will have an impact on the descriptive data and consequently the utility distribution of any study sample. As it appears this important factor is often ignored, we discuss this in some detail.

A graphical example can illustrate potential misclassification effects due to distributional descriptive 3L–5L effects (Fig. <a href="#Fig1" data-ref-type="fig">1</a>). The general methodology has been widely discussed in research on reporting heterogeneity \[44–48\]. Imagine a health dimension scaled with three levels of granularity: 3L, 5L and 10L (3, 5 and 10 levels respectively). In this example we do not take specific labels into account (although ‘1’ refers to no problems). There is an underlying unobservable latent scale which is assumed to be continuous: all three measurement systems (3L, 5L, 10L) will only be approximations of the true latent value. The transition area of two adjacent categories is called the cut-off point (or ‘cut-point’), and in the development of measurement scales one strives for clearly defined cut-points with little overlap (as defined by the labels), to avoid error. The distribution of observed scores of the 3L, 5L and 10L ordinal scales depends on the cut-points. Random error may occur at the cut-points when overlap exists, and this overlap may differ between 3L, 5L and 10L. Note that random error may cause a shift of average values for the extreme categories of the scale, as misclassification can only be towards the middle level of the scale due to the censored nature of the EQ-5D dimensions. Also note that when applying labels, the middle category of 3L does not necessarily coincide with the middle level of 10L, or would have the same latent midpoint, i.e. the middle point of the category, equidistant from both cut-points. Various types of misclassification may occur between the three systems. Imagine five different locations on the latent scale (A through to E), which we here refer to as respondents, although these also might indicate group averages. For respondent A there is no discrepancy between 3L, 5L and 10L: no problems are scored in all three systems. For respondent B both 3L and 5L lack refinement (no problems) as evidently there are reported problems on 10L. Respondent C illustrates the reduced ceiling effect with the introduction of 5L over 3L: no problems are reported in 3L whereas problems are reported on 5L. Respondent D might contribute to an overestimation of reported health problems in 3L when compared to 5L: the middle 3L category is chosen whereas a milder category is chosen for 5L. The distance from the 3L midpoint to the true latent value (*X*) is larger than the distance from the 5L midpoint to the latent value (*Y*) and smallest with 10L (*Z*). The same goes for respondent E: the most extreme category is chosen for 3L whereas a less severe category is scored on 5L. As mentioned, these location effects may also apply to group means, potentially leading to misclassification, especially when the group is rather homogeneous. Random error will increase if the mass of observations of a group is close to a cut-point of the scale such as location D, and may then have a strong impact on a crude scale such as 3L, but may only have a small effect on a more refined scale such as 5L, and even less on 10L. Generally, we assume that more levels theoretically will lead to less measurement bias.

<figure id="Fig1">
<p><img src="40273_2018_623_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40273_2018_623_Fig1_HTML.gif" /></p>
<figcaption>Illustration of location effects when five hypothetical latent health states (A through E) are measured on three scales with varying levels of granularity (3L, 5L, 10L). <em>3L</em> 3 levels, <em>5L</em> 5 levels, <em>10L</em> 10 levels</figcaption>
</figure>

With regard to factor 2, specific modelling outcomes on the intercept and dimension coefficients and the use of interaction terms such as the N3 term (representing whether any dimension is at level 3) will affect the resulting utility distributions and may subsequently affect discriminatory power. To explore the role of these modelling effects we studied the impact of altering the models (based on the original valuation data) by performing a sensitivity analysis in which we excluded the N3 term for two 3L value sets (The Netherlands, UK).

We explored the role of factors 1–3 both numerically and graphically. The point of departure was the LSS of the descriptive data, both by dimension and summed over all dimensions. From the LSS, difference scores between 3L and 5L were calculated by condition. We investigated how various value set characteristics contributed to discriminatory power results using tLSS (LSS transformed to a 0–1 scale) as a reference.

As a way of disentangling the intertwined effects of various factors affecting discriminatory power, we performed a multiple regression analysis with the *F* statistic and AUROC as dependent variables and the following variables representing value set or descriptive system characteristics as independent variables: intercept (continuous), modelled range (continuous), N3 (continuous, we included only N3 since this was the most prominent interaction term), version (with 3L as reference) and country (with Canada as reference).

## Results

### 3L and 5L Value Sets for Seven Countries

There were substantial differences in the models across value sets (Table <a href="#Tab1" data-ref-type="table">1</a>). For most countries the modelled 5L value range was smaller than that for the 3L, with the exception of China and The Netherlands. If 5L value sets included an intercept, its size was much smaller than 3L (except for South Korea where the intercept was 0.050 for 3L and 0.096 for 5L). The ‘upper gap’ between the value for 11111 and the second best health state was reduced quite substantially in 5L, ranging from a 0.02 reduction for The Netherlands and 0.04 for Spain to 0.09 for Japan and 0.14 for Canada, with South Korea as the exception (0.09 for 3L and 0.12 for 5L). Note that for Canada the upper gap was only 0.02 for 5L, because the value for 11111 was set at 0.949 (1 minus the intercept). Five countries included the N3 term in their 3L model, while for 5L only two countries used a similar interaction term (Canada and South Korea). Considerable variation was apparent in the model coefficients indicating the utility value decrement (‘disutility’) of dimensions, with mobility showing the highest decrements for level 3 (3L) for Canada, China, Japan, South Korea and Spain and for level 5 (5L) for China, Japan and South Korea. Pain/discomfort had the highest decrement for level 3 (3L) for the UK and The Netherlands and for level 5 (5L) for Canada, England and Spain. Anxiety/depression showed the second largest disutility in 5L for Canada, England, Japan and Spain and the largest for The Netherlands. For The Netherlands, both 3L and 5L value sets include large disutility values for anxiety/depression.

Figure <a href="#Fig9" data-ref-type="fig">9</a> (Appendix) depicts the distribution plots for all possible values for the 3L and 5L value sets. Note that these plots are ranked by utility value for 3L and 5L separately, implying that ‘comparable’ health states such as 21111 for 3L and 31111 for 5L can be at different positions on the common utility space (*X*-axis). For England/UK and Spain, most 3L index values were concentrated at a much lower segment of the utility scale when compared to 5L, while for China it was vice versa, although to a lesser extent.

<figure id="Fig9">
<p><img src="40273_2018_623_Fig9_HTML.jpg" id="MO9" /></p>
<p><img src="40273_2018_623_Fig9_HTML.gif" /></p>
<figcaption>Histograms of all possible 3L (<em>n</em> = 243) and 5L (<em>n</em> = 3125) utility values based on value sets from seven countries. <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L</figcaption>
</figure>

### Distributional Analyses of 3L and 5L Utility Values

The descriptive final dataset consisted of 3L and 5L health profile data for 3467 respondents, with the smallest and largest condition groups being depression (*n* = 250) and liver disease (*n* = 588), respectively (Table <a href="#Tab2" data-ref-type="table">2</a>). The ceiling was always lower in 5L, ranging from a difference between 3L and 5L of 0.8% (stroke) to 12.7% (students). Floor effects were negligible.

<div id="Tab2" class="table-wrap">

<div class="caption">

Characteristics of descriptive EQ-5D data for nine condition groups

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Condition groups</th>
<th style="text-align: left;"><em>N</em></th>
<th style="text-align: left;">Countries</th>
<th style="text-align: left;">Mean age (years)</th>
<th style="text-align: left;">% female</th>
<th style="text-align: left;">Mean EQ VAS (SD)</th>
<th style="text-align: left;">Ceiling 3L (% 11111)</th>
<th style="text-align: left;">Ceiling 5L (% 11111)</th>
<th style="text-align: left;">Floor 3L (% 33333)</th>
<th style="text-align: left;">Floor 5L (% 55555)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="10" style="text-align: left;">Healthy population</td>
</tr>
<tr>
<td style="text-align: left;"> Students</td>
<td style="text-align: center;">443</td>
<td style="text-align: left;">Poland</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">79</td>
<td style="text-align: center;">79 (16)</td>
<td style="text-align: center;">47.0</td>
<td style="text-align: center;">34.3</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Mild disease</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes mellitus</td>
<td style="text-align: center;">271</td>
<td style="text-align: left;">Denmark, England</td>
<td style="text-align: center;">52</td>
<td style="text-align: center;">48</td>
<td style="text-align: center;">74 (20)</td>
<td style="text-align: center;">33.6</td>
<td style="text-align: center;">28.8</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Liver disease</td>
<td style="text-align: center;">588</td>
<td style="text-align: left;">Italy</td>
<td style="text-align: center;">56</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">70 (21)</td>
<td style="text-align: center;">38.6</td>
<td style="text-align: center;">35.7</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td colspan="10" style="text-align: left;">Moderate/severe disease</td>
</tr>
<tr>
<td style="text-align: left;"> Cardiovascular disease</td>
<td style="text-align: center;">251</td>
<td style="text-align: left;">England, Scotland</td>
<td style="text-align: center;">67</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">61 (21)</td>
<td style="text-align: center;">13.2</td>
<td style="text-align: center;">8.0</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0.4</td>
</tr>
<tr>
<td style="text-align: left;"> Stroke</td>
<td style="text-align: center;">582</td>
<td style="text-align: left;">England, Poland</td>
<td style="text-align: center;">68</td>
<td style="text-align: center;">47</td>
<td style="text-align: center;">52 (26)</td>
<td style="text-align: center;">7.0</td>
<td style="text-align: center;">6.2</td>
<td style="text-align: center;">2.8</td>
<td style="text-align: center;">1.9</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma/COPD</td>
<td style="text-align: center;">342</td>
<td style="text-align: left;">England, Scotland</td>
<td style="text-align: center;">67</td>
<td style="text-align: center;">52</td>
<td style="text-align: center;">58 (21)</td>
<td style="text-align: center;">8.5</td>
<td style="text-align: center;">7.0</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: left;"> RA/arthritis</td>
<td style="text-align: center;">367</td>
<td style="text-align: left;">Denmark, England, Scotland</td>
<td style="text-align: center;">61</td>
<td style="text-align: center;">52</td>
<td style="text-align: center;">63 (21)</td>
<td style="text-align: center;">6.5</td>
<td style="text-align: center;">1.9</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td style="text-align: center;">250</td>
<td style="text-align: left;">England</td>
<td style="text-align: center;">42</td>
<td style="text-align: center;">56</td>
<td style="text-align: center;">62 (21)</td>
<td style="text-align: center;">12.0</td>
<td style="text-align: center;">6.4</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: left;"> Personality disorder</td>
<td style="text-align: center;">373</td>
<td style="text-align: left;">The Netherlands</td>
<td style="text-align: center;">32</td>
<td style="text-align: center;">67</td>
<td style="text-align: center;">59 (18)</td>
<td style="text-align: center;">15.8</td>
<td style="text-align: center;">13.3</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: left;">Total</td>
<td style="text-align: center;">3467</td>
<td style="text-align: left;">6 countries</td>
<td style="text-align: center;">52</td>
<td style="text-align: center;">53</td>
<td style="text-align: center;">64 (23)</td>
<td style="text-align: center;">20.5</td>
<td style="text-align: center;">16.1</td>
<td style="text-align: center;">0.5</td>
<td style="text-align: center;">0.3</td>
</tr>
</tbody>
</table>

*3L* EQ-5D-3L, *5L* EQ-5D-5L, *COPD* chronic obstructive pulmonary disease, *EQ VAS* EQ-5D visual analogue scale, *RA* rheumatoid arthritis, *SD* standard deviation

</div>

Figure <a href="#Fig2" data-ref-type="fig">2</a> depicts the empirically observed utility values for all countries. The 5L distributions are smoother and more evenly distributed than those for 3L. The 3L value distributions often show clusters and discontinuities across the entire range of the scale. Due to the intercept for 3L there is a large upper gap for Japan and Canada, and to a slightly lesser extent for The Netherlands and the UK. The 5L country-specific distributions look rather similar despite the model heterogeneity, although for South Korea and Japan the effect of the intercept is also clearly visible. While for England and Spain most possible 3L utility values (Fig. <a href="#Fig9" data-ref-type="fig">9</a>, Appendix) were concentrated at a much lower segment of the scale than 5L, the observed values did not show this pattern.

<figure id="Fig2">
<p><img src="40273_2018_623_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2018_623_Fig2_HTML.gif" /></p>
<figcaption>Histograms of observed utility values based on value sets from seven countries, all condition groups combined. <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L</figcaption>
</figure>

The non-parametric Shannon’s *H*′ and *J*′ indices numerically reflected the graphical results (Table <a href="#Tab3" data-ref-type="table">3</a>). For all comparisons, Shannon’s *H*′ was much higher for 5L and Shannon’s Evenness *J*′ index also was consistently higher for 5L. After subdivision into 0.05 utility space categories 5L clearly showed substantially higher values than 3L for both indices in all countries, establishing better distributional evenness for 5L overall.

<div id="Tab3" class="table-wrap">

<div class="caption">

Distributional evenness (Shannon’s indices) of EQ-5D-3L and EQ-5D-5L utility values from seven countries: all condition groups combined

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">Canada</th>
<th colspan="4" style="text-align: left;">China</th>
<th colspan="4" style="text-align: left;">England/UK</th>
<th colspan="4" style="text-align: left;">Japan</th>
</tr>
<tr>
<th style="text-align: left;">No. categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J</em>′</th>
<th style="text-align: left;">No. of categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J</em>′</th>
<th style="text-align: left;">No. of categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J</em>′</th>
<th style="text-align: left;">No. of categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J</em>′</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="17" style="text-align: left;">All</td>
</tr>
<tr>
<td style="text-align: left;"> 3L</td>
<td style="text-align: center;">236</td>
<td style="text-align: center;">123</td>
<td style="text-align: center;">4.79</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">223</td>
<td style="text-align: center;">118</td>
<td style="text-align: center;">4.76</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">237</td>
<td style="text-align: center;">121</td>
<td style="text-align: center;">4.78</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">123</td>
<td style="text-align: center;">4.78</td>
<td style="text-align: center;">0.61</td>
</tr>
<tr>
<td style="text-align: left;"> 5L</td>
<td style="text-align: center;">2978</td>
<td style="text-align: center;">668</td>
<td style="text-align: center;">7.21</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">2139</td>
<td style="text-align: center;">628</td>
<td style="text-align: center;">7.17</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">1569</td>
<td style="text-align: center;">562</td>
<td style="text-align: center;">6.99</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">3125</td>
<td style="text-align: center;">675</td>
<td style="text-align: center;">7.22</td>
<td style="text-align: center;">0.62</td>
</tr>
<tr>
<td colspan="17" style="text-align: left;">Bins 0.05<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;"> 3L</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">3.38</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">23</td>
<td style="text-align: center;">20</td>
<td style="text-align: center;">3.59</td>
<td style="text-align: center;">0.79</td>
<td style="text-align: center;">32</td>
<td style="text-align: center;">30</td>
<td style="text-align: center;">3.79</td>
<td style="text-align: center;">0.76</td>
<td style="text-align: center;">23</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">3.39</td>
<td style="text-align: center;">0.75</td>
</tr>
<tr>
<td style="text-align: left;"> 5L</td>
<td style="text-align: center;">23</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">3.61</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: center;">28</td>
<td style="text-align: center;">28</td>
<td style="text-align: center;">4.07</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">26</td>
<td style="text-align: center;">26</td>
<td style="text-align: center;">3.91</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">20</td>
<td style="text-align: center;">3.77</td>
<td style="text-align: center;">0.86</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">The Netherlands</th>
<th colspan="4" style="text-align: left;">South Korea</th>
<th colspan="4" style="text-align: left;">Spain</th>
</tr>
<tr>
<th style="text-align: left;">No. of categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J′</em></th>
<th style="text-align: left;">No. of categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J</em>′</th>
<th style="text-align: left;">No. of categories</th>
<th style="text-align: left;">Categories used</th>
<th style="text-align: left;"><em>H</em>′</th>
<th style="text-align: left;"><em>J</em>′</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="13" style="text-align: left;">All</td>
</tr>
<tr>
<td style="text-align: left;"> 3L</td>
<td style="text-align: center;">228</td>
<td style="text-align: center;">118</td>
<td style="text-align: center;">4.77</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">229</td>
<td style="text-align: center;">119</td>
<td style="text-align: center;">4.77</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">229</td>
<td style="text-align: center;">122</td>
<td style="text-align: center;">4.78</td>
<td style="text-align: center;">0.61</td>
</tr>
<tr>
<td style="text-align: left;"> 5L</td>
<td style="text-align: center;">2000</td>
<td style="text-align: center;">582</td>
<td style="text-align: center;">7.11</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">1224</td>
<td style="text-align: center;">504</td>
<td style="text-align: center;">6.88</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">3125</td>
<td style="text-align: center;">675</td>
<td style="text-align: center;">7.22</td>
<td style="text-align: center;">0.62</td>
</tr>
<tr>
<td colspan="13" style="text-align: left;">Bins 0.05<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;"> 3L</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">25</td>
<td style="text-align: center;">3.55</td>
<td style="text-align: center;">0.75</td>
<td style="text-align: center;">24</td>
<td style="text-align: center;">23</td>
<td style="text-align: center;">3.50</td>
<td style="text-align: center;">0.76</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">3.95</td>
<td style="text-align: center;">0.78</td>
</tr>
<tr>
<td style="text-align: left;"> 5L</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">4.07</td>
<td style="text-align: center;">0.84</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">3.64</td>
<td style="text-align: center;">0.82</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">4.00</td>
<td style="text-align: center;">0.82</td>
</tr>
</tbody>
</table>

*3L* EQ-5D-3L, *5L* EQ-5D-5L, *H'* absolute informativity, *J'* relative informativity

<sup>a</sup>The utility scale was subdivided in categories (‘bins’) with 0.05 of utility space each

</div>

Figure <a href="#Fig3" data-ref-type="fig">3</a> shows the observed country-specific mean utility values for each condition group (means and SDs are listed in Table <a href="#Tab6" data-ref-type="table">6</a>, Appendix). The presentation as a line graph was chosen to facilitate pattern comparison between 3L and 5L. Overall, the same ranking of average utilities per condition group across countries is visible in the figure and also a strong similarity of utilities with tLSS (showing only descriptive 3L–5L differences). Two patterns are visible: between-country valuation effects appeared larger than 3L versus 5L effects (judging from the scale differences between countries), and 3L–5L utility differences did not seem to add very much to the difference based on tLSS between 3L and 5L. For mild conditions 5L SDs were generally smaller, except for England/UK and Spain where SDs in 5L were smaller overall. Two countries displayed close to identical 3L and 5L condition group means (Canada and Japan). The other countries and tLSS values generally indicated an upward or downward shift. The UK showed a universal upward shift of 5L, South Korea a downward shift, the remaining countries (China, The Netherlands and Spain) showed a general shift plus a modifying effect in four conditions: CVD, stroke, asthma/chronic obstructive pulmonary disease (COPD) and rheumatoid arthritis (RA)/arthritis, which may have been caused by location effects.

<figure id="Fig3">
<p><img src="40273_2018_623_Fig3a_HTML.jpg" id="MO3" /></p>
<p><img src="40273_2018_623_Fig3a_HTML.gif" /></p>
<p><img src="40273_2018_623_Fig3b_HTML.jpg" id="MO300" /></p>
<p><img src="40273_2018_623_Fig3b_HTML.gif" /></p>
<figcaption>Mean 3L and 5L utility value per condition group for seven countries and the transformed Level Sum Score. <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L, <em>COPD</em> chronic obstructive pulmonary disease, <em>CVD</em> cardiovascular disease, <em>RA</em> rheumatoid arthritis</figcaption>
</figure>

<div id="Tab6" class="table-wrap">

<div class="caption">

Mean EQ-5D-3L and EQ-5D-5L utility values and standard deviations by condition group for seven countries and the transformed Level Sum Score

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Condition groups</th>
<th rowspan="2" style="text-align: left;"><em>N</em></th>
<th colspan="2" style="text-align: left;">Canada</th>
<th colspan="2" style="text-align: left;">China</th>
<th colspan="2" style="text-align: left;">England/UK</th>
<th colspan="2" style="text-align: left;">Japan</th>
<th colspan="2" style="text-align: left;">The Netherlands</th>
<th colspan="2" style="text-align: left;">South Korea</th>
<th colspan="2" style="text-align: left;">Spain</th>
<th colspan="2" style="text-align: left;">tLSS</th>
</tr>
<tr>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="18" style="text-align: left;">Healthy population</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Students</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">443</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.86</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.10</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">443</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: center;">0.86</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: center;">0.09</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;">Mild disease</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Diabetes mellitus</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">271</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.77</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.78</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.86</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.82</td>
<td style="text-align: center;">0.18</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">271</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">0.20</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.79</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.82</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">0.16</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Liver disease</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">588</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.81</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.84</td>
<td style="text-align: center;">0.18</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">588</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.84</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.85</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: center;">0.15</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;">Moderate/severe disease</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> CVD</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">251</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.57</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.63</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.72</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.57</td>
<td style="text-align: center;">0.34</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.21</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">251</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.57</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">0.63</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">0.68</td>
<td style="text-align: center;">0.21</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Stroke</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">582</td>
<td style="text-align: center;">0.54</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.50</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.40</td>
<td style="text-align: center;">0.40</td>
<td style="text-align: center;">0.50</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">0.49</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">0.37</td>
<td style="text-align: center;">0.47</td>
<td style="text-align: center;">0.53</td>
<td style="text-align: center;">0.25</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">582</td>
<td style="text-align: center;">0.52</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">0.41</td>
<td style="text-align: center;">0.39</td>
<td style="text-align: center;">0.51</td>
<td style="text-align: center;">0.34</td>
<td style="text-align: center;">0.51</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.44</td>
<td style="text-align: center;">0.37</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.48</td>
<td style="text-align: center;">0.35</td>
<td style="text-align: center;">0.56</td>
<td style="text-align: center;">0.27</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Asthma/COPD</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">342</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.20</td>
<td style="text-align: center;">0.63</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.72</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.57</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.20</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">342</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.56</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.57</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.68</td>
<td style="text-align: center;">0.22</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> RA/arthritis</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">367</td>
<td style="text-align: center;">0.68</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.59</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.63</td>
<td style="text-align: center;">0.15</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.74</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">0.18</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">367</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.59</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.60</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: center;">0.19</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Depression</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">250</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.20</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.30</td>
<td style="text-align: center;">0.69</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">0.79</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.69</td>
<td style="text-align: center;">0.30</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;">0.20</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">250</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.77</td>
<td style="text-align: center;">0.19</td>
</tr>
<tr>
<td colspan="18" style="text-align: left;"> Personality disorder</td>
</tr>
<tr>
<td style="text-align: left;">  3L</td>
<td style="text-align: center;">373</td>
<td style="text-align: center;">0.69</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">0.69</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.78</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;">0.15</td>
</tr>
<tr>
<td style="text-align: left;">  5L</td>
<td style="text-align: center;">373</td>
<td style="text-align: center;">0.72</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">0.72</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: center;">0.13</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.72</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.76</td>
<td style="text-align: center;">0.13</td>
</tr>
</tbody>
</table>

*3L* EQ-5D-3L, *5L* EQ-5D-5L, *CVD* cardiovascular disease, *COPD* chronic obstructive pulmonary disease, *RA* rheumatoid arthritis, *SD* standard deviation, *tLSS* transformed Level Sum Score

</div>

### Discriminatory Performance of 5L Versus 3L

Both 3L and 5L distinguished well between the healthy and the disease groups as well as between mild and moderate/severe condition groups for all country-specific value sets. All comparisons resulted in statistically significant results. However, performance in terms of relative efficiency varied noticeably across version (3L/5L), value set (country and model effects) and the condition groups compared. Generally, 3L performed better in the healthy–disease comparisons while 5L performed better comparing mild and moderate/severe conditions (Fig. <a href="#Fig4" data-ref-type="fig">4</a>). Japanese and Dutch 5L value sets performed better overall while Canadian and Chinese 3L value sets performed better overall. The bootstrap analysis showed that although most significant results were quite robust, some were borderline significant while others were borderline non-significant.

<figure id="Fig4">
<p><img src="40273_2018_623_Fig4_HTML.jpg" id="MO4" /></p>
<p><img src="40273_2018_623_Fig4_HTML.gif" /></p>
<figcaption>Observed relative efficiency of 5L over 3L using the <em>F</em> statistic ratio. Green cells indicate a significant <em>F</em> ratio showing better discriminatory power for 5L, orange cells for 3L (95% CI, 3000 bootstrap samples). <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L, <em>CI</em> confidence interval, <em>COPD</em> chronic obstructive pulmonary disease, <em>dis.</em> disease/disorder, <em>RA</em> rheumatoid arthritis, <em>tLSS</em> transformed Level Sum Score</figcaption>
</figure>

The results for the AUROC analysis generally supported the relative efficiency results (Fig. <a href="#Fig5" data-ref-type="fig">5</a>), with 3L showing a better performance in the healthy–disease comparison, and 5L in the mild versus moderate/severe comparisons. However, overall results showed a significantly better performance for 5L over 3L when compared to the relative efficiency results, except for Japan.

<figure id="Fig5">
<p><img src="40273_2018_623_Fig5_HTML.jpg" id="MO5" /></p>
<p><img src="40273_2018_623_Fig5_HTML.gif" /></p>
<figcaption>Observed relative efficiency of 5L over 3L using the AUROC. Green cells indicate a significant AUROC comparison showing better discriminatory power for 5L, orange cells for 3L (95% CI, 3000 bootstrap samples). <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L, <em>auc</em> area under the curve, <em>AUROC</em> area under the receiver-operating characteristics curve, <em>CI</em> confidence interval, <em>COPD</em> chronic obstructive pulmonary disease, <em>dis.</em> disease/disorder, <em>RA</em> rheumatoid arthritis, <em>tLSS</em> transformed Level Sum Score</figcaption>
</figure>

### Exploration of Factors Affecting Discriminatory Power

For the exploratory analysis we initially focused on the descriptive data, comparing LSS by dimension. Table <a href="#Tab4" data-ref-type="table">4</a> shows a pronounced shift effect between 3L and 5L (LSS by dimension recoded to no problems = 0; 3L on the same scale as 5L). A standardised difference score (*Δ*) was calculated, adjusting for sample size. For almost all condition groups and all dimensions, a shift to less reported health problems on 5L when compared with 3L occurred, except for mobility, where 5L represents more health problems for five condition groups due to ‘confined to bed’ barely being endorsed in 3L. The sum of the standardised differences scores shows that over all five dimensions the 3L–5L difference (shift) was smallest for the healthy population (28.4) and largest for liver disease (75.0). Level distributions by dimension for the pooled dataset graphically depict this main trend (Fig. <a href="#Fig6" data-ref-type="fig">6</a>). The shift was mainly caused by the very large proportion of respondents scoring level 2 on 3L who scored a level 2 or level 3 on 5L (average 85% over dimensions), leaving a very small proportion scoring level 4 on 5L. For pain/discomfort and anxiety/depression this also occurred at the extreme end of the scale, with a larger proportion scoring level 3 on 3L who scored level 4 on 5L rather than level 5. These observations translate into the conclusion that 3L as a scale tended to overestimate health problems when compared with 5L.

<div id="Tab4" class="table-wrap">

<div class="caption">

EQ-5D-3L versus EQ-5D-5L Level Sum Score by dimension<sup>a</sup> and condition group, including a standardized level shift indicator (Δ = 3L − 5L adjusted for sample size)<sup>b</sup>

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Condition groups</th>
<th colspan="3" style="text-align: left;">Mobility</th>
<th colspan="3" style="text-align: left;">Self-care</th>
<th colspan="3" style="text-align: left;">Usual activities</th>
<th colspan="3" style="text-align: left;">Pain/discomfort</th>
<th colspan="3" style="text-align: left;">Anxiety/depression</th>
<th rowspan="2" style="text-align: left;">Sum (Δ)</th>
</tr>
<tr>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;">3L</th>
<th style="text-align: left;">5L</th>
<th style="text-align: left;">Δ</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="17" style="text-align: left;">Healthy population</td>
</tr>
<tr>
<td style="text-align: left;"> Students</td>
<td style="text-align: center;">18</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">− 0.2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">0.0</td>
<td style="text-align: center;">92</td>
<td style="text-align: center;">91</td>
<td style="text-align: center;">0.2</td>
<td style="text-align: center;">294</td>
<td style="text-align: center;">210</td>
<td style="text-align: center;">19.0</td>
<td style="text-align: center;">404</td>
<td style="text-align: center;">362</td>
<td style="text-align: center;">9.5</td>
<td style="text-align: center;">28.4</td>
</tr>
<tr>
<td colspan="17" style="text-align: left;">Mild disease</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes mellitus</td>
<td style="text-align: center;">172</td>
<td style="text-align: center;">185</td>
<td style="text-align: center;">− 4.8</td>
<td style="text-align: center;">92</td>
<td style="text-align: center;">59</td>
<td style="text-align: center;">12.2</td>
<td style="text-align: center;">230</td>
<td style="text-align: center;">181</td>
<td style="text-align: center;">18.1</td>
<td style="text-align: center;">314</td>
<td style="text-align: center;">255</td>
<td style="text-align: center;">21.8</td>
<td style="text-align: center;">180</td>
<td style="text-align: center;">145</td>
<td style="text-align: center;">12.9</td>
<td style="text-align: center;">60.1</td>
</tr>
<tr>
<td style="text-align: left;"> Liver disease</td>
<td style="text-align: center;">298</td>
<td style="text-align: center;">236</td>
<td style="text-align: center;">10.5</td>
<td style="text-align: center;">140</td>
<td style="text-align: center;">87</td>
<td style="text-align: center;">9.0</td>
<td style="text-align: center;">376</td>
<td style="text-align: center;">305</td>
<td style="text-align: center;">12.1</td>
<td style="text-align: center;">480</td>
<td style="text-align: center;">368</td>
<td style="text-align: center;">19.0</td>
<td style="text-align: center;">552</td>
<td style="text-align: center;">409</td>
<td style="text-align: center;">24.3</td>
<td style="text-align: center;">75.0</td>
</tr>
<tr>
<td colspan="17" style="text-align: left;">Moderate/severe disease</td>
</tr>
<tr>
<td style="text-align: left;"> Cardiovascular disease</td>
<td style="text-align: center;">366</td>
<td style="text-align: center;">396</td>
<td style="text-align: center;">− 12.0</td>
<td style="text-align: center;">236</td>
<td style="text-align: center;">195</td>
<td style="text-align: center;">16.3</td>
<td style="text-align: center;">434</td>
<td style="text-align: center;">401</td>
<td style="text-align: center;">13.1</td>
<td style="text-align: center;">406</td>
<td style="text-align: center;">368</td>
<td style="text-align: center;">15.1</td>
<td style="text-align: center;">278</td>
<td style="text-align: center;">238</td>
<td style="text-align: center;">15.9</td>
<td style="text-align: center;">48.6</td>
</tr>
<tr>
<td style="text-align: left;"> Stroke</td>
<td style="text-align: center;">1140</td>
<td style="text-align: center;">1128</td>
<td style="text-align: center;">2.1</td>
<td style="text-align: center;">1042</td>
<td style="text-align: center;">970</td>
<td style="text-align: center;">12.4</td>
<td style="text-align: center;">1280</td>
<td style="text-align: center;">1191</td>
<td style="text-align: center;">15.3</td>
<td style="text-align: center;">1030</td>
<td style="text-align: center;">950</td>
<td style="text-align: center;">13.7</td>
<td style="text-align: center;">978</td>
<td style="text-align: center;">847</td>
<td style="text-align: center;">22.5</td>
<td style="text-align: center;">66.0</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma/COPD</td>
<td style="text-align: center;">518</td>
<td style="text-align: center;">562</td>
<td style="text-align: center;">− 12.9</td>
<td style="text-align: center;">298</td>
<td style="text-align: center;">267</td>
<td style="text-align: center;">9.1</td>
<td style="text-align: center;">586</td>
<td style="text-align: center;">551</td>
<td style="text-align: center;">10.2</td>
<td style="text-align: center;">624</td>
<td style="text-align: center;">530</td>
<td style="text-align: center;">27.5</td>
<td style="text-align: center;">374</td>
<td style="text-align: center;">305</td>
<td style="text-align: center;">20.2</td>
<td style="text-align: center;">54.1</td>
</tr>
<tr>
<td style="text-align: left;"> RA/arthritis</td>
<td style="text-align: center;">524</td>
<td style="text-align: center;">526</td>
<td style="text-align: center;">–0.5</td>
<td style="text-align: center;">270</td>
<td style="text-align: center;">225</td>
<td style="text-align: center;">12.3</td>
<td style="text-align: center;">588</td>
<td style="text-align: center;">522</td>
<td style="text-align: center;">18.0</td>
<td style="text-align: center;">730</td>
<td style="text-align: center;">657</td>
<td style="text-align: center;">19.9</td>
<td style="text-align: center;">322</td>
<td style="text-align: center;">287</td>
<td style="text-align: center;">9.5</td>
<td style="text-align: center;">59.1</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td style="text-align: center;">172</td>
<td style="text-align: center;">157</td>
<td style="text-align: center;">6.0</td>
<td style="text-align: center;">92</td>
<td style="text-align: center;">75</td>
<td style="text-align: center;">6.8</td>
<td style="text-align: center;">288</td>
<td style="text-align: center;">233</td>
<td style="text-align: center;">22.0</td>
<td style="text-align: center;">330</td>
<td style="text-align: center;">288</td>
<td style="text-align: center;">16.8</td>
<td style="text-align: center;">466</td>
<td style="text-align: center;">409</td>
<td style="text-align: center;">22.8</td>
<td style="text-align: center;">74.4</td>
</tr>
<tr>
<td style="text-align: left;"> Personality disorder</td>
<td style="text-align: center;">116</td>
<td style="text-align: center;">86</td>
<td style="text-align: center;">8.0</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">4.6</td>
<td style="text-align: center;">576</td>
<td style="text-align: center;">555</td>
<td style="text-align: center;">5.6</td>
<td style="text-align: center;">448</td>
<td style="text-align: center;">378</td>
<td style="text-align: center;">18.8</td>
<td style="text-align: center;">816</td>
<td style="text-align: center;">715</td>
<td style="text-align: center;">27.1</td>
<td style="text-align: center;">64.1</td>
</tr>
</tbody>
</table>

*3L* EQ-5D-3L, *5L* EQ-5D-5L, *COPD* chronic obstructive pulmonary disease, *LSS* Level Sum Score, *RA* rheumatoid arthritis, *Δ* difference

<sup>a</sup>Recoded: no problems = 0; 3L and 5L on the same scale. For 3L: level 2 = 2 and level 3 = 4; and for 5L: level 2 = 1, level 3 = 2, level 4 = 3 and level 5 = 4

<sup>b</sup>The difference between LSS by dimension (3L − 5L), adjusted for sample size: ‘28.4’ means that the average level shift per respondent was 0.284

</div>

<figure id="Fig6">
<p><img src="40273_2018_623_Fig6_HTML.jpg" id="MO6" /></p>
<p><img src="40273_2018_623_Fig6_HTML.gif" /></p>
<figcaption>Percentage of reported problems to 3L and 5L descriptive systems: all condition groups combined. <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L</figcaption>
</figure>

Overall, 3L resulted in higher relative efficiency ratios for the healthy–disease comparison whereas 5L performed better for the mild versus moderate/severe comparisons. Figure <a href="#Fig7" data-ref-type="fig">7</a> provides an example explaining this trend. Using tLSS as reference, 3L has overall lower average values than 5L, but as mentioned earlier the differences for the healthy population were smallest, while for the other condition groups they were larger, resulting in a larger difference in means between the healthy and disease groups for 3L (*X*) than for 5L (*Y*), reflected in higher *F* statistics for 3L. For the mild disease showing the most pronounced results on relative efficiency (liver disease), the descriptive difference between 3L and 5L was largest (Table <a href="#Tab4" data-ref-type="table">4</a>). Here the difference pattern was reversed, as indicated at the foot of Fig. <a href="#Fig7" data-ref-type="fig">7</a>. The difference in means between the mild and moderate/severe diseases was larger for 5L (*Y*) than for 3L (*X*), resulting in higher discriminatory power for 5L.

<figure id="Fig7">
<p><img src="40273_2018_623_Fig7_HTML.jpg" id="MO7" /></p>
<p><img src="40273_2018_623_Fig7_HTML.gif" /></p>
<figcaption>Observed redistribution of latent health states from 3L to 5L if descriptive refinement increases. <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L</figcaption>
</figure>

When exploring 3L–5L differences of the country-specific utilities, various model characteristics emerged as important underlying factors. A large intercept generally results in a lower mean and increased variance around the mean. The net effect on the *F* statistic is difficult to predict since both the difference of means and the standard error of the difference are affected. Overall, we detected a negative effect on discriminatory power, exemplified by the very large 3L intercept of Japan, leading to inferior performance when compared to 5L. Second, an effect of the use of model interaction terms was visible. The large N3 terms for the UK, Spain (and to a lesser extent for The Netherlands) appeared to negatively influence discriminatory power, caused by a substantial increase in variance. Note particularly that the Canadian 3L set did not contain an N3 term, but the 5L did include an ‘N4 or N5’ term which might have contributed to poorer discriminatory performance of 5L. Partly caused by the N3 term, but also due to other characteristics of 3L value sets, clusters and gaps occurred in the utility distributions, especially in the moderate to severe region (0–0.5), whereas 5L employed the utility scale more efficiently, resulting in smoother distributions. The histograms for the separate condition group comparisons demonstrate that the modelled range of a given value set bore no relation to the *F* statistic results. Instead, the use of the scale was decisive (as also shown in Fig. <a href="#Fig2" data-ref-type="fig">2</a>). One example is liver disease: while the modelled range for 5L in Canada and Japan was much smaller than for 3L, the available value range was being used much more frequently and efficiently in 5L, contributing to higher discriminatory power in 5L.

The sensitivity analysis, exploring the effect of excluding the N3 term for the 3L value sets for the UK and The Netherlands, confirmed this pattern. Discriminatory power clearly increased for 3L as the number of significant results in favour of 3L increased from 3 versus 4 (3L vs. 5L) to 9 versus 2 for the UK and from 1 versus 10 (3L vs. 5L) to 4 versus 5 for The Netherlands (Figs. <a href="#Fig4" data-ref-type="fig">4</a>, <a href="#Fig8" data-ref-type="fig">8</a>). Descriptive statistics showed that this was mainly due to lower levels of dispersion for the models without N3.

<figure id="Fig8">
<p><img src="40273_2018_623_Fig8_HTML.jpg" id="MO8" /></p>
<p><img src="40273_2018_623_Fig8_HTML.gif" /></p>
<figcaption>Sensitivity analysis main effects without N3 for UK and The Netherlands: observed relative efficiency of 5L over 3L using the <em>F</em> statistic ratio. Green cells indicate a significant F ratio showing better discriminatory power for 5L, orange cells for 3L (95% CI, 3000 bootstrap samples). <em>3L</em> EQ-5D-3L, <em>5L</em> EQ-5D-5L, <em>CI</em> confidence interval, <em>COPD</em> chronic obstructive pulmonary disease, <em>dis.</em> disease/disorder, <em>N3</em> any level 3, <em>RA</em> rheumatoid arthritis</figcaption>
</figure>

The results from the regression on the *F* statistic were a way to validate our interpretation of the relative impact of various factors. Our findings were confirmed (Table <a href="#Tab5" data-ref-type="table">5</a>), demonstrating a significant negative coefficient for 5L for the healthy–disease comparison and a positive coefficient for the mild versus moderate/severe comparisons. The modelled range was not significant for both types of comparison, confirming that the modelled range did not significantly impact upon the *F* statistic. The intercept showed a significant negative value for the healthy–disease comparison, implying that the use of an intercept decreases discriminatory power. The N3 term did not show a significant impact. It is of interest to note that the value sets for the Asian countries resulted in higher discriminatory power than for the non-Asian countries. Using the AUROC as the independent variable showed similar patterns, where the intercept consistently showed a negative effect, as did the N3 term for the mild versus moderate/severe comparison. The modelled range, however, appeared to contribute to discriminatory power.

<div id="Tab5" class="table-wrap">

<div class="caption">

Effect of value set characteristics on discriminatory performance in terms of *F* statistic and area under the receiver-operating characteristics curve

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="4" style="text-align: left;"><em>F</em> statistic</th>
<th colspan="4" style="text-align: left;">AUROC</th>
</tr>
<tr>
<th style="text-align: left;">Coefficient</th>
<th style="text-align: left;"><em>t</em> value</th>
<th style="text-align: left;"><em>p</em> value</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">Coefficient</th>
<th style="text-align: left;"><em>t</em> value</th>
<th style="text-align: left;"><em>p</em> value</th>
<th style="text-align: left;">95% CI</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="9" style="text-align: left;">Healthy vs. disease</td>
</tr>
<tr>
<td style="text-align: left;"> Version 5L<sup>a</sup></td>
<td style="text-align: center;">– 37.3</td>
<td style="text-align: left;">− 4.29</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 56.1 to − 18.5</td>
<td style="text-align: center;">− 0.015</td>
<td style="text-align: center;">− 7.20</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.020 to − 0.011</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"> Country<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;">  China</td>
<td style="text-align: center;">60.0</td>
<td style="text-align: left;">3.91</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">26.8 to 93.1</td>
<td style="text-align: center;">0.000</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: center;">1.00</td>
<td style="text-align: left;">− 0.007 to 0.007</td>
</tr>
<tr>
<td style="text-align: left;">  England/UK</td>
<td style="text-align: center;">− 27.3</td>
<td style="text-align: left;">− 2.00</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: left;">− 56.7 to 2.1</td>
<td style="text-align: center;">− 0.023</td>
<td style="text-align: center;">− 6.42</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.031 to − 0.015</td>
</tr>
<tr>
<td style="text-align: left;">  Japan</td>
<td style="text-align: center;">73.4</td>
<td style="text-align: left;">3.57</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">29.0 to 117.8</td>
<td style="text-align: center;">0.013</td>
<td style="text-align: center;">3.75</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.005 to 0.020</td>
</tr>
<tr>
<td style="text-align: left;">  The Netherlands</td>
<td style="text-align: center;">− 50.2</td>
<td style="text-align: left;">− 3.67</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 79.8 to − 20.7</td>
<td style="text-align: center;">− 0.037</td>
<td style="text-align: center;">− 7.75</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.047 to − 0.027</td>
</tr>
<tr>
<td style="text-align: left;">  South Korea</td>
<td style="text-align: center;">53.3</td>
<td style="text-align: left;">5.54</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">32.5 to 74.1</td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;">6.66</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.012 to 0.024</td>
</tr>
<tr>
<td style="text-align: left;">  Spain</td>
<td style="text-align: center;">− 8.4</td>
<td style="text-align: left;">− 0.47</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: left;">− 47.4 to 30.6</td>
<td style="text-align: center;">− 0.015</td>
<td style="text-align: center;">− 2.39</td>
<td style="text-align: center;">0.03</td>
<td style="text-align: left;">− 0.028 to − 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> Intercept</td>
<td style="text-align: center;">− 342.5</td>
<td style="text-align: left;">− 3.67</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 543.9 to − 141.0</td>
<td style="text-align: center;">− 0.109</td>
<td style="text-align: center;">− 4.43</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.162 to − 0.056</td>
</tr>
<tr>
<td style="text-align: left;"> Modelled range</td>
<td style="text-align: center;">50.4</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: left;">− 36.8 to 137.6</td>
<td style="text-align: center;">0.051</td>
<td style="text-align: center;">3.92</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.023 to 0.079</td>
</tr>
<tr>
<td style="text-align: left;"> N3</td>
<td style="text-align: center;">− 57.5</td>
<td style="text-align: left;">− 1.17</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: left;">− 163.9 to 49.0</td>
<td style="text-align: center;">− 0.029</td>
<td style="text-align: center;">− 1.68</td>
<td style="text-align: center;">0.12</td>
<td style="text-align: left;">− 0.066 to 0.008</td>
</tr>
<tr>
<td style="text-align: left;"> Constant</td>
<td style="text-align: center;">293.5</td>
<td style="text-align: left;">5.24</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">172.4 to 414.6</td>
<td style="text-align: center;">0.746</td>
<td style="text-align: center;">45.08</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.710 to 0.782</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Mild vs. moderate/severe</td>
</tr>
<tr>
<td style="text-align: left;"> Version 5L<sup>a</sup></td>
<td style="text-align: center;">27.2</td>
<td style="text-align: left;">8.81</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">20.5 to 33.8</td>
<td style="text-align: center;">0.023</td>
<td style="text-align: center;">25.02</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.021 to 0.025</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"> Country<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;">  China</td>
<td style="text-align: center;">20.9</td>
<td style="text-align: left;">3.79</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">9.0 to 32.8</td>
<td style="text-align: center;">− 0.004</td>
<td style="text-align: center;">− 2.61</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: left;">− 0.008 to − 0.001</td>
</tr>
<tr>
<td style="text-align: left;">  England/UK</td>
<td style="text-align: center;">0.0</td>
<td style="text-align: left;">0.00</td>
<td style="text-align: center;">1.00</td>
<td style="text-align: left;">− 11.0 to 11.1</td>
<td style="text-align: center;">− 0.008</td>
<td style="text-align: center;">− 3.84</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.012 to − 0.003</td>
</tr>
<tr>
<td style="text-align: left;">  Japan</td>
<td style="text-align: center;">21.1</td>
<td style="text-align: left;">2.66</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: left;">3.9 to 38.2</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">0.37</td>
<td style="text-align: left;">− 0.003 to 0.007</td>
</tr>
<tr>
<td style="text-align: left;">  The Netherlands</td>
<td style="text-align: center;">− 5.0</td>
<td style="text-align: left;">− 1.04</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: left;">− 15.5 to 5.4</td>
<td style="text-align: center;">− 0.006</td>
<td style="text-align: center;">− 3.62</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.010 to − 0.003</td>
</tr>
<tr>
<td style="text-align: left;">  South Korea</td>
<td style="text-align: center;">10.4</td>
<td style="text-align: left;">2.72</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: left;">2.1 to 18.7</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">1.49</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: left;">− 0.001 to 0.006</td>
</tr>
<tr>
<td style="text-align: left;">  Spain</td>
<td style="text-align: center;">8.5</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: left;">− 5.3 to 22.3</td>
<td style="text-align: center;">− 0.008</td>
<td style="text-align: center;">− 3.31</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: left;">− 0.013 to − 0.003</td>
</tr>
<tr>
<td style="text-align: left;"> Intercept</td>
<td style="text-align: center;">60.5</td>
<td style="text-align: left;">1.70</td>
<td style="text-align: center;">0.11</td>
<td style="text-align: left;">− 16.4 to 137.4</td>
<td style="text-align: center;">− 0.057</td>
<td style="text-align: center;">− 4.44</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">− 0.085 to − 0.029</td>
</tr>
<tr>
<td style="text-align: left;">Modelled range</td>
<td style="text-align: center;">− 11.1</td>
<td style="text-align: left;">− 0.86</td>
<td style="text-align: center;">0.40</td>
<td style="text-align: left;">− 39.0 to 16.7</td>
<td style="text-align: center;">0.015</td>
<td style="text-align: center;">4.80</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.008 to 0.022</td>
</tr>
<tr>
<td style="text-align: left;">N3</td>
<td style="text-align: center;">− 11.8</td>
<td style="text-align: left;">− 0.67</td>
<td style="text-align: center;">0.52</td>
<td style="text-align: left;">− 50.1 to 26.5</td>
<td style="text-align: center;">− 0.017</td>
<td style="text-align: center;">− 2.71</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: left;">− 0.031 to − 0.004</td>
</tr>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: center;">126.6</td>
<td style="text-align: left;">6.98</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">87.4 to 165.8</td>
<td style="text-align: center;">0.695</td>
<td style="text-align: center;">159.70</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: left;">0.686 to 0.705</td>
</tr>
</tbody>
</table>

*3L* EQ-5D-3L, *5L* EQ-5D-5L, *AUROC* area under the receiver-operating characteristics curve, *CI* confidence interval, *N3* any level 3

<sup>a</sup>With 3L as reference

<sup>b</sup>With Canada as reference

</div>

## Discussion

Our study showed that the 5L version of the EQ-5D instrument was in many respects superior to the original 3L version. By separating the performance of description and valuation, it became clear that these benefits mainly arise from the improved descriptive system: 5L was superior in terms of the distributional evenness, efficiency of scale use and the face validity of the resulting distributions, leading to an increase in sensitivity and precision in health status measurement. Refinement of 5L was not offset by more error, neither in terms of description nor in valuation.

The fewer cut-points of 3L (two instead of four in 5L) and the position of the cut-points relative to the true latent scale position could be the main drivers of the larger error component in 3L. The net effect was that 3L overestimated self-reported health problems by displaying ‘moderate problems’ where the true latent score most often was more likely to be in between ‘no problems’ and ‘moderate’, i.e. 3L suffered from a rather high cut-point between levels 1 and 2 (and for pain/discomfort and anxiety/depression also between levels 2 and 3). The impact of this artefact of the descriptive system decreased when the number of levels increased. The fact that 3L systematically overestimated reported health problems was unexpected, as for certain condition groups (e.g. in severe patients) the level of reported health problems between 3L and 5L could have been similar, or 3L could have led to the reverse finding. i.e. an underestimation of health problems. The overestimation of 3L was not trivial and affected any difference score when making comparisons: differences may be underestimated or overestimated, such as the overestimation of the difference between a healthy population and most patient groups in our study. This disadvantage of 3L has further consequences in the valuation procedure: if respondents were to value a 3L health profile with moderate problems, and no information was available to inform them that this would actually (empirically) refer to a mix of moderate and predominantly milder health problems, then the disutility would also be overestimated.

When adding utility values to the descriptive data, it was apparent that although absolute utility means varied substantially, 3L–5L differences were not very large, as usually a constant upward or downward shift was observed. Nevertheless, this study showed that seemingly small differences do affect results in discriminating between groups, and are likely to also affect responsiveness. A more precise discrimination between subgroups is achieved with 5L. The effect on QALY comparisons might be smaller since here it would mainly be the difference of mean utilities that would determine the outcome, with the exception being heterogeneous diseases and/or populations where the redistribution effects were non-linear (in our study CVD, stroke, asthma/COPD and RA/arthritis), where larger differences might be expected.

On the assumption that the increased number of levels in 5L led to less bias in the resulting utilities, we concluded that 3L overestimated health problems and consequently underestimated utilities when compared with 5L. This was generally observed across condition groups, but was most pronounced in liver disease (caused by a large misclassification at location D, as depicted in Fig. <a href="#Fig1" data-ref-type="fig">1</a>). Against our expectation, health problems in this group were apparently very mild \[49\], as confirmed by the high mean EQ VAS rating. A result of 3L misclassification is a biased assessment of discriminatory power that could lead to an overestimation of discriminatory power of 3L in the healthy versus disease comparisons in our study, or an underestimation of discriminatory power in the mild versus moderate/severe comparisons.

For mild conditions SDs were lower in 5L, which may be a consequence of 3L overestimation being larger in these conditions, as 5L was better equipped to capture the (very) mild skewed distribution, resulting in lower SDs. For moderate and severe condition groups, 5L SD rates were higher. Graphical and numerical (Shannon’s indices) evidence clearly showed that 5L covered a much wider range of the utility scale in these condition groups and was more evenly distributed, which in our view resulted in a much better reflection of the true underlying distribution. Note also that for the UK and Spain, 3L levels of dispersion were higher overall, which was in part due to the inclusion of the N3 term.

The analysis additionally proved useful in detecting inter-country differences. The relatively poor performance of 5L in some countries may relate to the use of the initial EQ-VT version 1.0. For instance, in Canada and England very few negative values were derived, which could be caused by poor protocol compliance of the interviewers and/or a poor explanation of the worse than dead task in the composite TTO exercise. In general, the value sets for the Asian countries showed better discriminatory power than non-Asian countries. We must also accept that structural components influence preferences, with many possible underlying factors involved (e.g. culture, demographics, language, geography), which was also noted by Olsen et al. \[50\].

Our study rested on two unique features:

1.  The development of an innovative framework to assess the performance of preference-based measures of health with varying levels of sensitivity. Note that a framework such as the COSMIN (COnsensus-based Standards for the selection of health Measurement Instruments) taxonomy only partially applies to instruments with separate descriptive and valuation components \[51, 52\].

2.  The use of a large number of published value sets ‘as is’ in a large multinational parallel 3L–5L dataset across nine condition groups.

Our innovative framework started with the separation of potential systematic effects in description and valuation. This enabled us to clarify hitherto poorly understood mechanisms underlying differences with a 3L versus a 5L system \[19, 53\]. Our study confirms some of the findings from an earlier study by Richardson et al. \[23\], showing that differences between utility results of different preference-based instruments are mainly attributable to the descriptive data, although a different methodological approach was followed in their study, based on parametric techniques. Our framework incorporated ceiling and floor effects, and Shannon’s indices as expressions of the evenness of a distribution. Distributional characteristics were based on the straightforward assumption that we should expect normal or lognormal distributed outcomes, as commonly observed in many naturally occurring phenomena, including self-reported health \[54–56\]. We improved on the use of the F ratio to quantify discriminatory power, differentiating between the various underlying sources, e.g. random error, cut-point-related bias and dispersion in heterogeneous samples. The successful use of the AUROC is an example of the wide applicability of this method beyond diagnostics. This study shows only part of its potential, as described elsewhere \[57, 58\]. A main advantage of our framework lies in the combined strength of the distributional approaches and different methods to assess discriminatory power, enabling us to make claims of the superiority of one measure over another. Our methods make clear that 5L is better than 3L, but they could also demonstrate that a hypothetical 10L might be a poor choice.

There were some limitations that must be acknowledged for the current study. First, the condition samples were not optimal for all groups. We used a student cohort to represent a healthy population, whereas a better matched general population sample, especially in terms of age and education, would have been more suitable. Second, we cannot exclude the possibility that inter-country differences in the descriptive data existed. The condition groups were from various countries, e.g. the liver disease sample was derived from an Italian cohort, the student cohort was entirely Polish and the personality disorder sample was Dutch. The *F* statistic was a key component of our study, assuming a normal distribution. The 3L and 5L utility scores used in our study were often not normally distributed due to ceiling effects or clusters, although in the context of health measurement the key factors are similarity of the distributions rather than normality, and approximately equal-sized samples \[42\]. Our conclusion that 3L overestimated health problems might be challenged for the first three dimensions where level 2 of 3L (some problems) was not identical to level 3 of 5L (moderate problems), although we felt justified generalising over all five dimensions since for pain/discomfort and anxiety/depression, where all labels are identical, overestimation was largest. Finally, as our study was based on cross-sectional data, we cannot make firm conclusions about the 3L versus 5L impact on QALYs. However, in the main pharmacoeconomic application of EQ-5D (cost-utility analysis), the utilities for different health states that are modelled are typically based on cross-sectional data, often derived from different patients subgroups.

## Conclusions

Our study has several implications. Although the 3L can be considered to be a valid measure in itself, we demonstrated that its lack of refinement did lead to more reported health problems on average when compared to a more sensitive and precise measure. We are aware that an even more refined system might reveal misclassification in 5L, but these effects will on average be much smaller. We conclude that 5L results in more precise and valid outcomes, both descriptive and in terms of valuation. The increased sensitivity and precision of 5L is likely to be generalisable to longitudinal designs, such as intervention studies. Hence, we recommend the use of 5L across applications, including economic evaluation, clinical studies and burden of disease or public health studies (e.g. for establishing population norms). Our results indicate that in situations where patient groups would experience a uniform recovery to nearly full health, 3L might artificially show a large effect. This might have led to the overestimation of QALY gains in past economic evaluations, especially in assessing the impact of drugs for mild diseases.

With regard to modelling of the utility data, it was apparent that the inclusion of an interaction term (such as N3) and an intercept would lead to undesirable distributional characteristics such as discontinuities and clusters in the utility scale and would be likely to reduce discriminatory power. It is notable that for the two countries that included an interaction term in their 5L model (Canada and South Korea), discriminatory power was not outstanding. Note that a large intercept might have been caused by misspecification of mild health states in the valuation procedure (by assigning low utility values), which could be due to interviewer effects (especially apparent in EQ-VT version 1.0) or cognitive overload in respondents. Our finding that the use of the scale was an important determinant of discriminatory performance (as opposed to the modelled range) shows that the previous preoccupation with the modelled range is not really justified \[29, 50\], which was also reflected in our regression results (Table <a href="#Tab5" data-ref-type="table">5</a>). The use of 3L in conditions with problems with mobility could lead to severe underreporting of mobility problems. In our study COPD or CVD patients showed many reported problems in walking about on 5L, but since these respondents were not confined to bed they were restricted to score level 2 on 3L, thereby reducing its sensitivity and discriminatory power substantially. This is corroborated by results from a study among patients to receive hip replacement surgery in the UK. Not a single patient reported a level 3 problem on mobility on the 3L, whereas there were many reported problems with mobility in the Oxford Hip Score, a condition-specific measure \[59\]. Changing the most severe level descriptor of 3L ‘confined to bed’ to ‘unable to walk about’ in 5L appeared to be a huge improvement.

A final implication of our study includes the introduction of a powerful evaluative framework, allowing for further extension by using evidence resulting from longitudinal 3L–5L data. Our framework combines parametric (*F* statistic) with non-parametric (AUROC) methods, and may be more broadly applied than assessing granularity of the system (the number of response options), such as to investigate the impact of adding dimensions to the EQ-5D, or assessing translation effects.

The current 5L system would profit from more knowledge on the random error of descriptive data (reliability) and cut-point effects, which would also be useful in the development of any new measure. This includes investigating whether the latent scale people use when responding to the EQ-5D for self-classification is the same as when valuing hypothetical health states.

## Acknowledgements

The authors would like to thank two anonymous reviewers for valuable comments and suggestions.

### Appendix

See Table <a href="#Tab6" data-ref-type="table">6</a> and Fig. <a href="#Fig9" data-ref-type="fig">9</a>.

## Author Contributions

MFJ led the data analysis and interpretation and was primarily responsible for drafting the manuscript. GJB devised the AUROC approach, and GJB and NL supported data analysis and interpretation and commented on and amended the draft manuscript.

## Compliance with Ethical Standards

### Funding

This work was funded by the EuroQol Research Foundation (Grant number EQ Project 2016620).

### Conflict of interest

All authors (Mathieu F. Janssen, Gouke J. Bonsel and Nan Luo) are members of the EuroQol Group.

### Data availability statement

All data analysed in this study are stored at the central data archive of the EuroQol Research Foundation. The data are available from the EuroQol Research Foundation upon reasonable request.

## Footnotes

## References

## References

1. The EuroQol Group EuroQol–a new facility for the measurement of health-related quality of life. Health Policy. 1990;16(3):199–208. doi: 10.1016/0168-8510(90)90421-9.

2. Dolan P. Modeling valuations for EuroQol health states. Med Care. 1997;35(11):1095–1108. doi: 10.1097/00005650-199711000-00002.

3. Brooks R. The EuroQol Group after 25 years. Dordrecht: Springer; 2013.

4. Devlin NJ, Brooks R. EQ-5D and the EuroQol Group: past, present and future. Appl Health Econ Health Policy. 2017;15(2):127–137. doi: 10.1007/s40258-017-0310-5.

5. Wille N, Badia X, Bonsel G, Burstrom K, Cavrini G, Devlin N, et al. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual Life Res. 2010;19(6):875–886. doi: 10.1007/s11136-010-9648-y.

6. Ravens-Sieberer U, Wille N, Badia X, Bonsel G, Burstrom K, Cavrini G, et al. Feasibility, reliability, and validity of the EQ-5D-Y: results from a multinational study. Qual Life Res. 2010;19(6):887–897. doi: 10.1007/s11136-010-9649-x.

7. Krabbe PF, Stouthard ME, Essink-Bot ML, Bonsel GJ. The effect of adding a cognitive dimension to the EuroQol multiattribute health-status classification system. J Clin Epidemiol. 1999;52(4):293–301. doi: 10.1016/S0895-4356(98)00163-2.

8. Swinburn P, Lloyd A, Boye KS, Edson-Heredia E, Bowman L, Janssen B. Development of a disease-specific version of the EQ-5D-5L for use in patients suffering from psoriasis: lessons learned from a feasibility study in the UK. Value Health. 2013;16(8):1156–1162. doi: 10.1016/j.jval.2013.10.003.

9. Yang Y, Brazier J, Tsuchiya A. Effect of adding a sleep dimension to the EQ- 5D descriptive system: a “bolt-on” experiment. Med Decis Making. 2014;34(1):42–53. doi: 10.1177/0272989X13480428.

10. Yang Y, Rowen D, Brazier J, Tsuchiya A, Young T, Longworth L. An exploratory study to test the impact on three “bolt-on” items to the EQ-5D. Value Health. 2015;18(1):52–60. doi: 10.1016/j.jval.2014.09.004.

11. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L) Qual Life Res. 2011;20(10):1727–1736. doi: 10.1007/s11136-011-9903-x.

12. EQ-5D. http://www.euroqol.org. Accessed 24 Oct 2017.

13. Oppe M, Devlin NJ, van Hout B, Krabbe PF, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17(4):445–453. doi: 10.1016/j.jval.2014.04.002.

14. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–473. doi: 10.1016/j.jval.2016.10.012.

15. Janssen MF, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, et al. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi: 10.1007/s11136-012-0322-4.

16. Jia YX, Cui FQ, Li L, Zhang DL, Zhang GM, Wang FZ, et al. Comparison between the EQ-5D-5L and the EQ-5D-3L in patients with hepatitis B. Qual Life Res. 2014;23(8):2355–2363. doi: 10.1007/s11136-014-0670-3.

17. Agborsangaya CB, Lahtinen M, Cooke T, Johnson JA. Comparing the EQ-5D 3L and 5L: measurement properties and association with chronic conditions and multimorbidity in the general population. Health Qual Life Outcomes. 2014;12:74. doi: 10.1186/1477-7525-12-74.

18. Conner-Spady BL, Marshall DA, Bohm E, Dunbar MJ, Loucks L, Al KA, et al. Reliability and validity of the EQ-5D-5L compared to the EQ-5D-3L in patients with osteoarthritis referred for hip and knee replacement. Qual Life Res. 2015;24(7):1775–1784. doi: 10.1007/s11136-014-0910-6.

19. Golicki D, Niewada M, Karlinska A, Buczek J, Kobayashi A, Janssen MF, et al. Comparing responsiveness of the EQ-5D-5L, EQ-5D-3L and EQ VAS in stroke patients. Qual Life Res. 2015;24(6):1555–1563. doi: 10.1007/s11136-014-0873-7.

20. Greene ME, Rader KA, Garellick G, Malchau H, Freiberg AA, Rolfson O. The EQ-5D-5L improves on the EQ-5D-3L for health-related quality-of-life assessment in patients undergoing total hip arthroplasty. Clin Orthop Relat Res. 2015;473(11):3383–3390. doi: 10.1007/s11999-014-4091-y.

21. Pan CW, Sun HP, Wang X, Ma Q, Xu Y, Luo N, Wang P. The EQ-5D-5L index score is more discriminative than the EQ-5D-3L index score in diabetes patients. Qual Life Res. 2014;24(7):1767–1774. doi: 10.1007/s11136-014-0902-6.

22. Pattanaphesaj J, Thavorncharoensap M. Measurement properties of the EQ-5D-5L compared to EQ-5D-3L in the Thai diabetes patients. Health Qual Life Outcomes. 2015;13:14. doi: 10.1186/s12955-014-0203-3.

23. Richardson J, Iezzi A, Khan MA. Why do multi-attribute utility instruments produce different utilities: the relative importance of the descriptive systems, scale and ‘micro-utility’ effects. Qual Life Res. 2015;24(8):2045–2053. doi: 10.1007/s11136-015-0926-6.

24. van Hout B, Janssen MF, Feng YS, Kohlmann T, Busschbach J, Golicki D, et al. Interim scoring for the EQ-5D-5L: mapping the EQ-5D-5L to EQ-5D-3L value sets. Value Health. 2012;15(5):708–715. doi: 10.1016/j.jval.2012.02.008.

25. Xie F, Pullenayegum E, Gaebel K, Bansback N, Bryan S, Ohinmaa A, et al. A time trade-off-derived value set of the EQ-5D-5L for Canada. Med Care. 2016;54(1):98–105. doi: 10.1097/MLR.0000000000000447.

26. Bansback N, Tsuchiya A, Brazier J, Anis A. Canadian valuation of EQ-5D health states: preliminary value set and considerations for future valuation studies. PLoS One. 2012;7(2):e31115. doi: 10.1371/journal.pone.0031115.

27. Luo N, Liu G, Li M, Guan H, Jin X, Rand-Hendriksen K. Estimating an EQ-5D-5L value set for China. Value Health. 2017;20(4):662–669. doi: 10.1016/j.jval.2016.11.016.

28. Liu GG, Wu H, Li M, Gao C, Luo N. Chinese time trade-off values for EQ-5D health states. Value Health. 2014;17(5):597–604. doi: 10.1016/j.jval.2014.05.007.

29. Devlin N, Shah K, Feng Y, Mulhern B, van Hout B. Valuing health-related quality of life: an EQ-5D-5L value set for England. Health Econ. 2017 doi: 10.1002/hec.3564.

30. Shiroiwa T, Ikeda S, Noto S, Igarashi A, Fukuda T, Saito S, Shimozuma K. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19(5):648–654. doi: 10.1016/j.jval.2016.03.1834.

31. Tsuchiya A, Ikeda S, Ikegami N, et al. Estimating an EQ-5D population value set: the case of Japan. Health Econ. 2002;11(4):341–353. doi: 10.1002/hec.673.

32. Versteegh MM, Vermeulen KM, Evers SM, de Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi: 10.1016/j.jval.2016.01.003.

33. Lamers LM, McDonnell J, Stalmeier PF, Krabbe PF, Busschbach JJ. The Dutch tariff: results and arguments for an effective design for national EQ-5D valuation studies. Health Econ. 2006;15(10):1121–1132. doi: 10.1002/hec.1124.

34. Kim SH, Ahn J, Ock M, Shin S, Park J, Luo N, et al. The EQ-5D-5L valuation study in Korea. Qual Life Res. 2016;25(7):1845–1852. doi: 10.1007/s11136-015-1205-2.

35. Lee YK, Nam HS, Chuang LH, Kim KY, Yang HK, Kwon IS, et al. South Korean time trade-off values for EQ-5D health states: modeling with observed values for 101 health states. Value Health. 2009;12(8):1187–1193. doi: 10.1111/j.1524-4733.2009.00579.x.

36. Ramos-Goñi JM, Craig BM, Oppe M, Ramallo-Fariña Y, Pinto-Prades JL, Luo L, et al. Handling data quality issues to estimate the Spanish EQ-5D-5L value set using a hybrid interval regression approach. Value Health (In press). doi:10.1016/j.jval.2017.10.023

37. Badia X, Roset R, Herdman M, Kind P. A comparison of United Kingdom and Spanish general population time trade-off values for EQ-5D health states. Med Decis Making. 2001;21(1):7–16. doi: 10.1177/0272989X0102100102.

38. Xie F, Gaebel K, Perampaladas K, Doble B, Pullenayegum E. Comparing EQ-5D valuation studies: a systematic review and methodological reporting checklist. Med Decis Making. 2014;34(1):8–20. doi: 10.1177/0272989X13480852.

39. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi: 10.1007/s40273-016-0404-1.

40. Parkin D, Devlin N, Feng Y. What determines the shape of an EQ-5D index distribution? Med Decis Making. 2016;36(8):941–951. doi: 10.1177/0272989X16645581.

41. Janssen MF, Birnie E, Bonsel GJ. Evaluating the discriminatory power of EQ-5D, HUI2 and HUI3 in a US general population survey using Shannon’s indices. Qual Life Res. 2007;16(5):895–904. doi: 10.1007/s11136-006-9160-6.

42. Vickrey BG, Hays RD, Genovese BJ, et al. Comparison of a generic to disease-targeted health-related quality-of-life measures for multiple sclerosis. J Clin Epidemiol. 1997;50:557–569. doi: 10.1016/S0895-4356(97)00001-2.

43. Luo N, Johnson JA, Shaw JW, et al. Relative efficiency of the EQ-5D, HUI2, and HUI3 index scores in measuring health burden of chronic medical conditions in a population health survey in the United States. Med Care. 2009;47:53–60. doi: 10.1097/MLR.0b013e31817d92f8.

44. Murray CJL, Özaltin E, Tandon A, Salomon JA, Sadana R, Chatterji SA. Empirical evaluation of the anchoring vignette approach in health surveys. In: Murray CJL, Evans DB, editors. Health system performance assessment: debates, methods and empiricism. Geneva: World Health Organization; 2003. pp. 369–399.

45. Lindeboom M, van Doorslaer E. Cut-point shift and index shift in self-reported health. J Health Econ. 2004;23(6):1083–1099. doi: 10.1016/j.jhealeco.2004.01.002.

46. Rice N, Robone S, Smith P. Analysis of the validity of the vignette approach to correct for heterogeneity in reporting health system responsiveness. Eur J Health Econ. 2011;12(2):141–162. doi: 10.1007/s10198-010-0235-5.

47. Hirve S, Gómez-Olivé X, Oti S, Debpuur C, Juvekar S, Tollman S, et al. Use of anchoring vignettes to evaluate health reporting behavior amongst adults aged 50 years and above in Africa and Asia–testing assumptions. Glob Health Action. 2013;6(1):21064. doi: 10.3402/gha.v6i0.21064.

48. Valentine N, Verdes-Tennant E, Bonsel G. Health systems’ responsiveness and reporting behaviour: multilevel analysis of the influence of individual-level factors in 64 countries. Soc Sci Med. 2015;138:152–160. doi: 10.1016/j.socscimed.2015.04.022.

49. Scalone L, Ciampichini R, Fagiuoli S, Gardini I, Fusco F, Gaeta L, et al. Comparing the performance of the standard EQ-5D 3L with the new version EQ-5D 5L in patients with chronic hepatic diseases. Qual Life Res. 2013;22(7):1707–1716. doi: 10.1007/s11136-012-0318-0.

50. Olsen JA, Lamu AN, Cairns J. In search of a common currency: a comparison of seven EQ-5D-5L value sets. Health Econ. 2017 doi: 10.1002/hec.3606.

51. Mokkink LB, Terwee CB, Knol DL, Stratford PW, Alonso J, Patrick DL, et al. Protocol of the COSMIN study: COnsensus-based Standards for the selection of health Measurement INstruments. BMC Med Res Methodol. 2006;6:2. doi: 10.1186/1471-2288-6-2.

52. Mokkink LB, Terwee CB, Patrick DL, Alonso J, Stratford PW, Knol DL, et al. International consensus on taxonomy, terminology, and definitions of measurement properties for health-related patient-reported outcomes: results of the COSMIN study. J Clin Epidemol. 2010;63:737–745. doi: 10.1016/j.jclinepi.2010.02.006.

53. Hernandez Alava M, Wailoo A, Grimm S, Pudney S, Gomes M, Sadique Z, et al. EQ-5D-5L versus EQ-5D-3L: the impact on cost-effectiveness. Value Health. 2018;21(1):49–56. doi: 10.1016/j.jval.2017.09.004.

54. Huxley JS. Problems of relative growth. London: Methuen and Company Limited; 1932.

55. Gaddum JH. Lognormal distributions. Nature. 1945;156:463–466. doi: 10.1038/156463a0.

56. Fairclough DL. Design and analysis of quality of life studies in clinical trials. 2. New York: CRC Press; 2010.

57. Hilden J. The area under the ROC curve and its competitors. Med Decis Making. 1991;11(2):95–101. doi: 10.1177/0272989X9101100204.

58. Hilden J. Prevalence-free utility-respecting summary indices of diagnostic power do not exist. Stat Med. 2000;19(4):431–440. doi: 10.1002/(SICI)1097-0258(20000229)19:4&#x0003c;431::AID-SIM348&#x0003e;3.0.CO;2-R.

59. Oppe M, Devlin N, Black N. Comparison of the underlying constructs of EQ-5D and Oxford Hip Score: implications for mapping. Value Health. 2011;14:884–891. doi: 10.1016/j.jval.2011.03.003.

## Associated Data

### Data Availability Statement

All data analysed in this study are stored at the central data archive of the EuroQol Research Foundation. The data are available from the EuroQol Research Foundation upon reasonable request.

[^1]: We use the notation ‘3L-5L’ to refer to ‘3L compared to 5L’, ‘3L versus 5L’ or ‘3L and 5L’, depending on the context.

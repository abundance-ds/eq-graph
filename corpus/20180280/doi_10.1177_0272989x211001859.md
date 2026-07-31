---
project_id: "20180280"
work_id: "doi:10.1177/0272989x211001859"
doi: "10.1177/0272989X211001859"
pmid: "33754886"
pmcid: "PMC8191148"
title: "Valuation Survey of EQ-5D-Y Based on the International Common Protocol: Development of a Value Set in Japan"
journal: "Medical Decision Making"
publication_date: "2021-03-23"
volume: "41"
issue: "5"
authors:
  - name: "Takeru Shiroiwa"
    affiliation_ids:
      - "aff1-0272989X211001859"
  - name: "Shunya Ikeda"
    affiliation_ids:
      - "aff2-0272989X211001859"
  - name: "Shinichi Noto"
    affiliation_ids:
      - "aff3-0272989X211001859"
  - name: "Takashi Fukuda"
    affiliation_ids:
      - "aff4-0272989X211001859"
  - name: "Elly Stolk"
    affiliation_ids:
      - "aff5-0272989X211001859"
affiliations:
  - id: "aff1-0272989X211001859"
    name: "Center for Outcomes Research and Economic Evaluation for Health (C2H), National Institute of Public Health, Wako, Saitama, Japan"
  - id: "aff2-0272989X211001859"
    name: "Department of Medicine, International University of Health and Welfare, Narita, Chiba, Japan"
  - id: "aff3-0272989X211001859"
    name: "Department of Health Sciences, Niigata University of Health and Welfare, Niigata, Japan"
  - id: "aff4-0272989X211001859"
    name: "Center for Outcomes Research and Economic Evaluation for Health (C2H), National Institute of Public Health, Wako, Saitama, Japan"
  - id: "aff5-0272989X211001859"
    name: "EuroQol Research Foundation, Rotterdam, South Holland, The Netherlands"
licence: "cc-by-nc"
source_file: "input/projects/20180280/papers/doi_10.1177_0272989x211001859.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8191148/fullTextXML"
source_method: "epmc_xml"
source_sha256: "b3a288bb42e8fb1ae4cad1439d051ff5e147ac1d9198a3e3bf1543837a8656ab"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Valuation Survey of EQ-5D-Y Based on the International Common Protocol: Development of a Value Set in Japan

## Abstract

### Background

EQ-5D-Y is a preference-based measure for children and adolescents (aged 8–15 y). This is the first study to develop an EQ-5D-Y value set for converting EQ-5D-Y responses to index values.

### Methods

We recruited 1047 respondents (aged 20–79 y) from the general population, stratified by gender and age group, in 5 Japanese cities. All data were collected through face-to-face surveys. Respondents were asked to value EQ-5D-Y states for a hypothetical 10-y-old child from a proxy perspective using composite time tradeoff (cTTO) and a discrete choice experiment (DCE). The discrete choice data were analyzed using a mixed logit model. Latent DCE values were then converted to a 0 (death)/1 (full health) scale by mapping them to the cTTO values.

### Results

The mean observed cTTO value of the worst health state \[33333\] was 0.20. Analysis of the DCE data showed that the coefficients of the domains related to mental functions (“Having pain or discomfort” and “Feeling worried, sad, or unhappy”) were larger than those for the domains related to physical and social functions. By converting latent DCE values to a utility scale, we constructed a value set for EQ-5D-Y. No inconsistencies were observed. The minimum predicted score was 0.288 \[33333\], and the second-best score was 0.957 \[12111\].

### Conclusion

A value set for EQ-5D-Y was successfully constructed. This is the first survey of an EQ-5D-Y value set. Interpreting the differences between EQ-5D-Y and EQ-5D-5L value sets is a future task with implications for health care policy.

**Keywords:** composite TTO, discrete choice experiment, EQ-5D-Y, preference-based measure, QALY

Received 2021 Jan 18; Accepted 2021 Feb 16; Issue date 2021 Jul.

EQ-5D-Y instrument is a preference-based measure that has been constructed to measure the health states of children and adolescents (aged 8–15 y). According to a review by Rowen et al.,<sup> 1 </sup> approximately 10 preference-based measures for children and adolescents have been developed as of 2020, including the Child Health Utility 9D (CHU9D),<sup> 2 </sup> the Assessment of Quality of Life-6 Dimensions (AQoL-6D),<sup> 3 </sup> the Health Utilities Index Mark 2 (HUI2),<sup> 4 </sup> and HUI3,<sup> 5 </sup> among others. In 2009, EQ-5D-Y was introduced as a child-friendly version of EQ-5D by the EuroQol Group. EQ-5D-Y is conceptually equivalent to EQ-5D,<sup> 6 </sup> but the wording of the severity levels of the dimensions has been adapted to be more relevant to younger populations. The instrument allows children (or their proxies) to report functioning on 5 basic dimensions of health, and subsequently, a value from a societal perspective can be attached to every reported health state reflecting how preferable that state is.

In 2020, Ramos Goñi et al.<sup> 7 </sup> presented an international valuation protocol for EQ-5D-Y that enabled the Japanese valuation survey to commence. However, there are some controversial issues related to valuation with respect to pediatric instruments. When originally investigating a value set for EQ-5D-Y, Kreimeier et al.<sup> 8 </sup> showed that the values obtained for EQ-5D-Y states exceeded EQ-5D values, which indicated that the labels attached to the levels of the 2 instruments corresponded to different severity levels. Higher values were placed on health states by children when compared with values placed on health states by adults. This tendency was also reported by Shah et al.<sup> 9 </sup> These studies confirmed the necessity to develop EQ-5D-Y value sets and that, in this respect, the application of adult value sets was not appropriate.

The protocol for valuing EQ-5D-Y follows the well-documented protocol for the valuation of EQ-5D-5L, which uses composite time tradeoff (cTTO) and a discrete choice experiment (DCE) as valuation methods.<sup>10,11</sup> In the EQ-5D-5L valuation protocol, cTTO is the primary valuation method and, optionally, the DCE responses can be used to enrich the data set. In contrast, the EQ-5D-Y valuation protocol involves a 2-step approach. The first step involves modeling DCE responses to derive values on a latent scale. In the second step, cTTO values are used to anchor the DCE-derived values onto the full health-dead scale. Similar 2-step approaches have been used to generate utilities for CHU9D in Australia and China and for the Infant Health-related Quality of Life Instrument (IQI). The advantages of this 2-step approach are its feasibility and flexibility. Moreover, unbundling DCE and cTTO allows researchers to exercise choice over how and to whom these tasks are administered, which facilitates experimentation and enables quick dissemination of new results into the protocol, if required.<sup>12,13</sup>

Most other variations among approaches to generate utilities for different instruments appear to be entirely commonplace, with the exception of choices about perspective. Adult health states can usually be valued by adults themselves, but it may not be possible to elicit values from children. Possible approaches to the valuation of child health include eliciting values from adolescents or asking adults to value EQ-5D-Y states from a proxy perspective. In the Australian CHU9D valuation survey,<sup>14,15</sup> the AQoL<sup> 3 </sup> and the 16-Dimension (16D)<sup> 16 </sup> health states were valued by adolescents for themselves. However, values were elicited from the general population for a child (i.e., from proxies) in the valuation of IQI<sup> 13 </sup> and in pilot work concerning EQ-5D-Y.<sup> 7 </sup> The latter approach has now also been adopted in the EQ-5D-Y valuation protocol, to be consistent with the taxpayer perspective, and because it was clear that the tasks could not be administered with children.

In Japan, there are no preference-based measures for children or adolescents featuring a Japanese value set. This has led to some difficulties in evaluating the cost-effectiveness of technology for children. Hence, the aim of this study was to produce a Japanese value set for EQ-5D-Y, following the protocol suggested.<sup> 7 </sup>

## Methods

### Instruments

The EQ-5D-Y instrument is composed of 5 dimensions, each assessed at 3 levels. It has the following domains: “mobility,”“looking after myself,”“doing usual activities,”“having pain or discomfort,” and “feeling worried, sad, or unhappy.” It covers the same basic dimensions of health as the adult version EQ-5D, but the words and phrases have been simplified to be more child friendly and are thus slightly different from those in EQ-5D-3L.<sup>6,8</sup> For example, level 3 for mobility was changed from “confined to bed” to “unable to walk around,” and the fifth dimension was changed from “anxiety/depression” into “feeling worried, sad, or unhappy.” Furthermore, in the Japanese version of EQ-5D-Y, the use of kanji characters was limited. EQ-5D-Y is designed for self-report by children and adolescents aged 8 to 15 y.<sup> 17 </sup> It might be possible for children and adolescents aged 12–15 y to use the adult EQ-5D version. However, for children aged 4–7 y, a proxy version of EQ-5D-Y is recommended.

The Japanese version of EQ-5D-Y was prepared by a Japanese research group, which included the authors of this article, based on a first draft provided by the EuroQol Group. The processes of translation, back translation, and harmonization for the first draft were completed by the EuroQol Group, independently of the Japanese group. The Japanese EQ-5D-Y has been confirmed for its psychometric properties.<sup> 18 </sup>

### cTTO and DCE

Preferences with respect to EQ-5D-Y health states in the general population (not in the population of children and adolescents) were measured using the cTTO and DCE methods using the EuroQol Group’s recently published protocol for EQ-5D-Y valuation.<sup> 7 </sup> cTTO is a TTO variant that adopts conventional TTO for the valuation of better-than-dead states and lead-time TTO for the valuation of worse-than-dead states.<sup> 19 </sup>

According to this protocol,<sup> 7 </sup> the requirement is to include at least 10 states in the cTTO tasks and 150 pairs in the DCE tasks. The value set can be established based on a combination of cTTO and DCE data, which may be linked, for example, using a mapping approach. The sample size should be at least 200 for the cTTO task and 1000 for the DCE task. Inclusion of more states/pairs/individuals is allowed. However, estimation of a value set based on cTTO responses requires the expansion of the TTO task.

In the cTTO task, participants were asked to consider which option was better for a hypothetical 10-y-old child from a proxy perspective: living for 10 y in a health state described by EQ-5D-Y or living *x* years in full health. In lead-time TTO, a series of choices was offered between years of life in full health and a life with “10 y in full health followed by 10 y in the EQ-5D-Y state presented.”

In the DCE survey, similar to the cTTO survey, the participants were required to imagine a hypothetical 10-y-old child’s health state. Then, 2 health states (states A and B) from a combination of EQ-5D-Y descriptions were presented. The participants chose the one they preferred between the 2 options from a proxy perspective. Modeling of the DCE responses produced values on a latent scale, which could be converted to values on a quality-adjusted life-year (QALY) scale by anchoring on the values derived from the cTTO task.

### Participants and Survey Process

Computer-assisted personal interviews were conducted in 5 cities in Japan (Tokyo, Niigata, Osaka, Okayama, and Fukuoka). These cities are representative of various regions in Japan and are geographically dispersed. The inclusion criteria were as follows: 1) aged 20 to 79 y, 2) current Japanese residency, 3) ability to visit the survey room in 1 of the 5 cities, 4) ability to provide informed consent, and 5) ability to complete the tasks in Japanese. The participants were recruited based on nonrandom quota sampling by a research company (ANTERIO Inc.), which sampled 1047 respondents throughout Japan (i.e., considering the size of the population, approximately 300 respondents from Tokyo and from Osaka, 200 from Fukuoka, and 100 from Niigata and from Okayama). The same number of respondents was collected by gender and age group in each city. The interviews were conducted one-on-one at centrally located interview sites. The interviews were fully scripted.

The computer-assisted personal interview tool used in this study was the EuroQol portable valuation technology (EQ-PVT), developed by the EuroQol Group and translated into Japanese. The EQ-PVT was used to implement the TTO and DCE tasks. It stored all responses and the data needed to create quality control reports concerning interviewer performance. Apart from the valuation perspective, implementation of the cTTO task was consistent with that in version 2.1 of the EQ-VT protocol.<sup> 10 </sup>

All participants were asked to complete both the cTTO and DCE tasks, with the former always performed before the latter. After the cTTO and DCE tasks, the participants’ demographic information was collected. In the cTTO phase, the first 3 tasks (wheelchair example) were presented as a practice exercise. First, they considered a hypothetical situation of living for 10 y in a wheelchair as a 10-y-old child. Next, they were asked to consider 2 unlabeled states from the same perspective: “much better than being in a wheelchair” and “much worse than being in a wheelchair, so bad that one would prefer to die immediately.” After this introduction to the task, participants practiced valuing health states using cTTO for 3 states defined by the EQ-5D-Y descriptive system. Finally, they were asked to undertake the real valuation tasks.

One block, including 6 health states, was randomly allocated to each participant from 5 blocks. As the worst EQ-5D-Y state was included in all blocks, a total of 26 health states were used. The 26 health states included 18 states representing an orthogonal array, all 5 mild states (4 dimensions at level 1 and 1 dimension at level 2), and 3 other states. Health states were presented in a random order.

In the DCE task, 1 block consisting of 15 pairs of EQ-5D-Y health states was randomly allocated to each participant from 10 blocks (an experimental design created by the EuroQol Group). A distinctive feature of the DCE design was that all pairs included attribute-level overlap. An efficient design approach was used to create the experimental design. The order in which the questions were presented was randomized, and the presentation positions (left or right) of the 2 health states were also randomized in the DCE survey.

The survey was conducted on weekends (Friday, Saturday, and Sunday) from February to March 2019. Before administering the survey, all the investigators received training for approximately 1 d. To ensure quality and consistency among investigators, the number of investigators was limited to 11 (90–100 samples per interviewer). To reduce the interviewer effect, all interviewers received strict quality control (QC) checks by the EuroQol Group after the survey each week, as described in by Ramos-Goñi et al.<sup> 20 </sup>; subsequently, feedback was provided to each interviewer. The valuation survey was conducted for the first 3 wk in Tokyo, and QC was conducted every week. After all interviewers passed the QC check 3 times in the Tokyo survey, they continued the survey in the other cities.

### Statistical Analyses

A mixed logit model was used for the analysis of the DCE data (model 1). A mixed logit model can consider the heterogeneity of coefficients without an irrelevant alternative assumption, whereas a simple conditional logit model assumes that all responses are independent. When choices are analyzed based on random utility theory, U<sub>ij</sub> (the disutility respondent j derives from choosing item i) can be divided into an explainable component (V<sub>ij</sub>) and a random component (ε<sub>ij</sub>),

``` math
U_{ij} = \ V_{ij} + \varepsilon_{ij}
```

``` math
V_{ij} = \beta_{12}X_{12} + \beta_{12}X_{12} + \ldots + \beta_{pq}X_{pq} + \ldots + \beta_{53}X_{53,}
```

where β<sub>pq</sub> represents the effects of the q<sup>th</sup> level (q = 2 or 3, where the first level is the reference term) of the p<sup>th</sup> (1 ≤ p ≤ 5) item. This model accounted for the panel structure in the data and for heteroscedasticity. At the same time, a simple conditional model was applied (model 2). To confirm the consistency with the DCE results, a linear mixed model was applied to cTTO values of 26 states to estimate each item’s coefficient (model 3). Interaction with any level 3 responses was considered by adding the N3 term (N3 = 1, if any level 3 responses were included in the health states) to model 3 (model 4). As suggested by Stolk et al.,<sup> 10 </sup> the TTO value was censored at 1. Considering these distribution characteristics, the Tobit model was also used for the cTTO data (model 5).

*Mixlogit* of STATA15 was used to estimate each coefficient of the mixed logit model. SAS 9.4 was used for the linear mixed model and the other statistical analyses.

### Constructing the Value Set from DCE Data

To convert the latent DCE values to a scale anchored at full health (1) and dead (0), the modeled DCE values were mapped onto the observed TTO values. The linear relationship function f(.) between the latent DCE values and the cTTO values of the 26 health states was estimated as cTTO<sub>i</sub> = f (DCE<sub>i</sub>) +ε<sub>i</sub>, where cTTO<sub>i</sub> is the observed mean cTTO value and DCE<sub>i</sub> is the latent DCE value for the i<sup>th</sup> health state (1 ≤ i ≤ 26).<sup> 21 </sup> The hybrid model<sup> 22 </sup> was also a candidate for the analysis of DCE and cTTO data in constructing a value set. The model can simultaneously treat both DCE and cTTO data, which is different from the above 2-step approach. However, this was not applied to the data set because the hybrid model is dependent on the relative amounts of TTO and DCE data collected, the ratio of which is arbitrarily set by researchers and not well balanced in the EQ-5D-Y protocol. Because it is uncertain how these features affect the performance of the hybrid model, a mapping approach was applied.

## Results

A total of 1047 respondents from 5 cities (308 from Tokyo, 310 from Osaka, 210 from Fukuoka, 110 from Okayama, and 109 from Niigata) participated in the EQ-5D-Y valuation survey. The participants’ characteristics are summarized in <a href="#table1-0272989X211001859" data-ref-type="table">Table 1</a>. The participants’ age and gender distributions were well balanced. With respect to household income, 50.1% reported earnings of less than JPY 6 million (USD 55,000; USD 1 = JPY 110 as of April 2019), compared with the median household income of all Japanese families of JPY 5.4 million (USD 49,000) in 2016. All participants completed the cTTO and DCE surveys; however, 2 responses were not recorded in the DCE survey using EQ-PVT. A total of 6082 cTTO values and 10,458 DCE choices were collected. The mean and median response times in the 6 cTTO tasks were 9.1 min (*s* = 2.3 min) and 8.8 min (interquartile range 7.6–10.3 min), respectively. Few issues were encountered during the QC process. Only about 2.5% of the interviews were flagged as not meeting QC standards. With respect to the cTTO tasks, the mean number of moves before reaching a point of indifference was 4.8. No data were excluded on account of the QC process. The distribution of cTTO values and the cTTO values for each health state were similar between interviewers. Thus, high levels of protocol compliance and the presence of few interviewer effects in the data were demonstrated.

<div id="table1-0272989X211001859" class="table-wrap">

<div class="caption">

Background Characteristics of Respondents

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: center;"><em>n</em></th>
<th style="text-align: center;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: left;">Location</td>
</tr>
<tr>
<td style="text-align: left;"> Tokyo</td>
<td>308</td>
<td>29.4</td>
</tr>
<tr>
<td style="text-align: left;"> Osaka</td>
<td>310</td>
<td>29.6</td>
</tr>
<tr>
<td style="text-align: left;"> Fukuoka</td>
<td>210</td>
<td>20.1</td>
</tr>
<tr>
<td style="text-align: left;"> Okayama</td>
<td>110</td>
<td>10.5</td>
</tr>
<tr>
<td style="text-align: left;"> Niigata</td>
<td>109</td>
<td>10.4</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Gender</td>
</tr>
<tr>
<td style="text-align: left;"> Male</td>
<td>523</td>
<td>50.0</td>
</tr>
<tr>
<td style="text-align: left;"> Female</td>
<td>524</td>
<td>50.1</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Age, y</td>
</tr>
<tr>
<td style="text-align: left;"> 20–29</td>
<td>174</td>
<td>16.6</td>
</tr>
<tr>
<td style="text-align: left;"> 30–39</td>
<td>174</td>
<td>16.6</td>
</tr>
<tr>
<td style="text-align: left;"> 40–49</td>
<td>175</td>
<td>16.7</td>
</tr>
<tr>
<td style="text-align: left;"> 50–59</td>
<td>175</td>
<td>16.7</td>
</tr>
<tr>
<td style="text-align: left;"> 60–69</td>
<td>174</td>
<td>16.6</td>
</tr>
<tr>
<td style="text-align: left;"> 70–79</td>
<td>175</td>
<td>16.7</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">With children</td>
</tr>
<tr>
<td style="text-align: left;"> Yes</td>
<td>703</td>
<td>67.1</td>
</tr>
<tr>
<td style="text-align: left;"> No</td>
<td>344</td>
<td>32.9</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Employment</td>
</tr>
<tr>
<td style="text-align: left;"> Employed or self-employed</td>
<td>677</td>
<td>64.7</td>
</tr>
<tr>
<td style="text-align: left;"> Retired</td>
<td>76</td>
<td>7.3</td>
</tr>
<tr>
<td style="text-align: left;"> Student</td>
<td>43</td>
<td>4.1</td>
</tr>
<tr>
<td style="text-align: left;"> Homemaker</td>
<td>197</td>
<td>18.8</td>
</tr>
<tr>
<td style="text-align: left;"> Others</td>
<td>54</td>
<td>5.2</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Marital status</td>
</tr>
<tr>
<td style="text-align: left;"> Married</td>
<td>677</td>
<td>64.7</td>
</tr>
<tr>
<td style="text-align: left;"> Unmarried</td>
<td>266</td>
<td>25.4</td>
</tr>
<tr>
<td style="text-align: left;"> Divorced</td>
<td>62</td>
<td>5.9</td>
</tr>
<tr>
<td style="text-align: left;"> Bereaved</td>
<td>41</td>
<td>3.9</td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td>1</td>
<td>0.1</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Education</td>
</tr>
<tr>
<td style="text-align: left;"> Junior high school</td>
<td>27</td>
<td>2.6</td>
</tr>
<tr>
<td style="text-align: left;"> High school</td>
<td>366</td>
<td>35.0</td>
</tr>
<tr>
<td style="text-align: left;"> College</td>
<td>234</td>
<td>22.3</td>
</tr>
<tr>
<td style="text-align: left;"> University or graduate</td>
<td>419</td>
<td>40.0</td>
</tr>
<tr>
<td style="text-align: left;"> Other</td>
<td>1</td>
<td>0.1</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Household income</td>
</tr>
<tr>
<td style="text-align: left;"> &lt;JPY 2 million</td>
<td>71</td>
<td>6.8</td>
</tr>
<tr>
<td style="text-align: left;"> JPY 2 million–4 million</td>
<td>196</td>
<td>18.7</td>
</tr>
<tr>
<td style="text-align: left;"> JPY 4 million–6 million</td>
<td>257</td>
<td>24.6</td>
</tr>
<tr>
<td style="text-align: left;"> JPY 6 million–10 million</td>
<td>311</td>
<td>29.7</td>
</tr>
<tr>
<td style="text-align: left;"> JPY 10 million–15 million</td>
<td>111</td>
<td>10.6</td>
</tr>
<tr>
<td style="text-align: left;"> ≥JPY 15 million</td>
<td>31</td>
<td>3.0</td>
</tr>
<tr>
<td style="text-align: left;"> Unknown</td>
<td>70</td>
<td>6.7</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L ( [<em>s</em>])</td>
<td colspan="2">0.95 [0.08]</td>
</tr>
<tr>
<td style="text-align: left;">EQ-VAS ( [<em>s</em>])</td>
<td colspan="2">82.3 [12.5]</td>
</tr>
</tbody>
</table>

</div>

### cTTO Results

<a href="#table2-0272989X211001859" data-ref-type="table">Table 2</a> shows the average cTTO values for the 26 health states described by EQ-5D-Y. The predicted score (based on <a href="#table3-0272989X211001859" data-ref-type="table">Table 3</a>) and root mean square error are also shown. The TTO values for health states \[11112\] and \[21111\] were 0.94 (the highest), and the score for health state \[33333\] was 0.20 (the lowest). A total of 910 respondents (86.9%) preferred the worst EQ-5D-Y state (33333) to death, and only 137 respondents (13.1%) evaluated it as worse than dead. <a href="#fig1-0272989X211001859" data-ref-type="fig">Figure 1</a> shows the distribution of the cTTO values. The peak of the distribution was at cTTO value = 0.95, and the density of the distribution with a cTTO value \<0 was very low (3.2%). As the misery score (the sum of level scores across dimensions) was higher, the mean cTTO value was lower, and the standard deviation increased with the misery score (<a href="#fig2-0272989X211001859" data-ref-type="fig">Figure 2</a>).

<div id="table2-0272989X211001859" class="table-wrap">

<div class="caption">

Mean Composite Time-Tradeoff Scores of 26 Health States

</div>

| Health State | *n* | . | *s* | Predicted Score<sup> <a href="#table-fn2-0272989X211001859" data-ref-type="table-fn">a</a> </sup> | MSRE |
|:---|----|----|----|----|----|
| 11112 | 211 | 0.94 | 0.08 | 0.93 | 0.054 |
| 11121 | 206 | 0.92 | 0.11 | 0.90 | 0.068 |
| 11211 | 206 | 0.93 | 0.16 | 0.94 | 0.060 |
| 12111 | 211 | 0.93 | 0.09 | 0.96 | 0.047 |
| 21111 | 210 | 0.94 | 0.06 | 0.94 | 0.040 |
| 11122 | 211 | 0.88 | 0.14 | 0.85 | 0.098 |
| 21211 | 206 | 0.89 | 0.18 | 0.90 | 0.086 |
| 12212 | 210 | 0.86 | 0.12 | 0.87 | 0.087 |
| 22121 | 211 | 0.83 | 0.21 | 0.84 | 0.116 |
| 11313 | 209 | 0.68 | 0.25 | 0.72 | 0.181 |
| 13221 | 211 | 0.80 | 0.15 | 0.79 | 0.116 |
| 23112 | 206 | 0.80 | 0.23 | 0.82 | 0.131 |
| 31131 | 211 | 0.64 | 0.26 | 0.62 | 0.184 |
| 12331 | 211 | 0.60 | 0.29 | 0.59 | 0.204 |
| 32113 | 209 | 0.65 | 0.26 | 0.71 | 0.190 |
| 13133 | 209 | 0.47 | 0.33 | 0.48 | 0.217 |
| 21332 | 206 | 0.57 | 0.29 | 0.51 | 0.207 |
| 22223 | 211 | 0.63 | 0.28 | 0.64 | 0.196 |
| 22232 | 209 | 0.58 | 0.31 | 0.56 | 0.209 |
| 31223 | 210 | 0.63 | 0.25 | 0.61 | 0.170 |
| 33311 | 209 | 0.70 | 0.29 | 0.72 | 0.189 |
| 22233 | 210 | 0.49 | 0.29 | 0.45 | 0.215 |
| 32322 | 211 | 0.62 | 0.27 | 0.64 | 0.182 |
| 23323 | 210 | 0.57 | 0.25 | 0.53 | 0.195 |
| 33232 | 211 | 0.48 | 0.33 | 0.46 | 0.238 |
| 33333 | 1047 | 0.20 | 0.37 | 0.29 | 0.284 |

MSR, mean square root error.

Predicted scores are calculated using <a href="#table4-0272989X211001859" data-ref-type="table">Table 4</a>.

</div>

<div id="table3-0272989X211001859" class="table-wrap">

<div class="caption">

Results of Analysis of the DCE and cTTO Data<sup> <a href="#table-fn4-0272989X211001859" data-ref-type="table-fn">a</a> </sup>

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="4" style="text-align: center;">DCE</th>
<th colspan="6" style="text-align: center;">cTTO</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: center;">Model 1 (Mixed Logit)</th>
<th colspan="2" style="text-align: center;">Model 2 (Conditional Logit)</th>
<th colspan="2" style="text-align: center;">Model 3 (Repeated-Measures ANOVA)</th>
<th colspan="2" style="text-align: center;">Model 4 (Model 3 + N3)</th>
<th colspan="2" style="text-align: center;">Model 5 (Tobit)</th>
</tr>
<tr>
<th style="text-align: left;">Dimension/Level</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;"><em>P</em> Value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;"><em>P</em> Value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;"><em>P</em> Value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;"><em>P</em> Value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;"><em>P</em> Value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: center;">—</td>
<td style="text-align: center;">—</td>
<td></td>
<td></td>
<td>0.973</td>
<td>&lt;0.0001</td>
<td>1.025</td>
<td>&lt;0.0001</td>
<td>1.024</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">Mobility</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td>−0.699</td>
<td>&lt;0.0001</td>
<td>−0.545</td>
<td>&lt;0.0001</td>
<td>−0.030</td>
<td>&lt;0.0001</td>
<td>−0.040</td>
<td>&lt;0.0001</td>
<td>−0.038</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td>−1.546</td>
<td>&lt;0.0001</td>
<td>−1.455</td>
<td>&lt;0.0001</td>
<td>−0.117</td>
<td>&lt;0.0001</td>
<td>−0.129</td>
<td>&lt;0.0001</td>
<td>−0.128</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">Looking after myself</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td>−0.319</td>
<td>&lt;0.0001</td>
<td>−0.272</td>
<td>&lt;0.0001</td>
<td>−0.039</td>
<td>&lt;0.0001</td>
<td>−0.045</td>
<td>&lt;0.0001</td>
<td>−0.052</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td>−1.204</td>
<td>&lt;0.0001</td>
<td>−1.028</td>
<td>&lt;0.0001</td>
<td>−0.099</td>
<td>&lt;0.0001</td>
<td>−0.108</td>
<td>&lt;0.0001</td>
<td>−0.106</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">Doing usual activities</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td>−0.658</td>
<td>&lt;0.0001</td>
<td>−0.596</td>
<td>&lt;0.0001</td>
<td>−0.032</td>
<td>&lt;0.0001</td>
<td>−0.041</td>
<td>&lt;0.0001</td>
<td>−0.033</td>
<td>0.003</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td>−1.757</td>
<td>&lt;0.0001</td>
<td>−1.515</td>
<td>&lt;0.0001</td>
<td>−0.107</td>
<td>&lt;0.0001</td>
<td>−0.121</td>
<td>&lt;0.0001</td>
<td>−0.120</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">Having pain or discomfort</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td>−1.340</td>
<td>&lt;0.0001</td>
<td>−1.163</td>
<td>&lt;0.0001</td>
<td>−0.032</td>
<td>&lt;0.0001</td>
<td>−0.044</td>
<td>&lt;0.0001</td>
<td>−0.053</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td>−4.681</td>
<td>&lt;0.0001</td>
<td>−3.209</td>
<td>&lt;0.0001</td>
<td>−0.239</td>
<td>&lt;0.0001</td>
<td>−0.254</td>
<td>&lt;0.0001</td>
<td>−0.260</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;">Feeling worried, sad, or unhappy</td>
</tr>
<tr>
<td style="text-align: left;"> 2</td>
<td>−0.850</td>
<td>&lt;0.0001</td>
<td>−0.728</td>
<td>&lt;0.0001</td>
<td>−0.038</td>
<td>&lt;0.0001</td>
<td>−0.044</td>
<td>&lt;0.0001</td>
<td>−0.047</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td style="text-align: left;"> 3</td>
<td>−2.708</td>
<td>&lt;0.0001</td>
<td>−2.039</td>
<td>&lt;0.0001</td>
<td>−0.191</td>
<td>&lt;0.0001</td>
<td>−0.204</td>
<td>&lt;0.0001</td>
<td>−0.195</td>
<td>&lt;0.0001</td>
</tr>
<tr>
<td style="text-align: left;">N3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>−0.051</td>
<td>&lt;0.0001</td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td colspan="2">10,980</td>
<td colspan="2">11,933</td>
<td colspan="2">–745</td>
<td colspan="2">–766</td>
<td colspan="2">2400</td>
</tr>
</tbody>
</table>

DCE, discrete choice experiment; cTTO, composite time tradeoff; ANOVA, analysis of variance; AIC, akaike information criteria.

DCE coefficients are latent utility and thus are not comparable with cTTO coefficients.

</div>

<figure id="fig1-0272989X211001859">
<p><img src="10.1177_0272989X211001859-fig1.jpg" /></p>
<p><img src="10.1177_0272989X211001859-fig1.gif" /></p>
<figcaption>Composite time-tradeoff (cTTO) value distribution.</figcaption>
</figure>

<figure id="fig2-0272989X211001859">
<p><img src="10.1177_0272989X211001859-fig2.jpg" /></p>
<p><img src="10.1177_0272989X211001859-fig2.gif" /></p>
<figcaption>Mean and standard deviation of composite time-tradeoff (cTTO) value by misery score.</figcaption>
</figure>

### DCE Results and the EQ-5D-Y Value Set

<a href="#table3-0272989X211001859" data-ref-type="table">Table 3</a> presents the parameter estimates obtained from the DCE data using a mixed logit model. The mixed logit model fit the DCE data better than the simple conditional logit model. Similar coefficients were obtained from models 3 to 5, which analyzed cTTO data. The N3 interaction term in model 4 was significantly negative. No inconsistencies were observed for any of the domains in any model; lower levels had lower negative scores. Note that the DCE results were estimated on a latent scale, and it was not possible simply to compare coefficients between the DCE and cTTO models.

Using the coefficients in <a href="#table3-0272989X211001859" data-ref-type="table">Table 3</a> from the mixed logit model, latent DCE values were computed for EQ-5D-Y states. Next, the mapping function was estimated to predict cTTO values based on the modeled latent DCE values. The estimated equation from the regression of the cTTO value (disutility) to the latent DCE values was cTTO value = −0.058 × latent DCE value + 0.975. The relationship between the observed cTTO values and the derived DCE values is shown in <a href="#fig3-0272989X211001859" data-ref-type="fig">Figure 3</a>.

<figure id="fig3-0272989X211001859">
<p><img src="10.1177_0272989X211001859-fig3.jpg" /></p>
<p><img src="10.1177_0272989X211001859-fig3.gif" /></p>
<figcaption>Relationship between latent discrete choice experiment scores and composite time-tradeoff values of 26 EQ-5D-Y states.</figcaption>
</figure>

In <a href="#table4-0272989X211001859" data-ref-type="table">Table 4</a>, the DCE coefficients (from model 1) are rescaled. When the EQ-5D-Y index value is calculated, this table can be used. For example, the score for the EQ-5D-Y health state 23213 can be calculated from <a href="#table3-0272989X211001859" data-ref-type="table">Table 3</a> by 1 + (−0.025 \[intercept\] − 0.040 \[mobility\] − 0.070 \[looking after myself\] − 0.038 \[doing usual activities\] − 0 \[having pain or discomfort\] − 0.156 \[feeling worried, sad, or unhappy\]) = 0.67. The coefficients for the domains “Having pain or discomfort” and “Feeling worried, sad, or unhappy” were smaller than those for the other domains. The coefficient for the “Looking after myself” domain had the largest value. <a href="#fig4-0272989X211001859" data-ref-type="fig">Figure 4</a> shows the distribution of the predicted scores for all 243 EQ-5D-Y health states. The root mean square error and intraclass correlation coefficients between the 26 estimated and empirical cTTO health states were 0.026 and 0.986, respectively. Both of these results showed that the predictions obtained using this function were similar to the empirical cTTO values.

<div id="table4-0272989X211001859" class="table-wrap">

<div class="caption">

Rescaled Discrete Choice Experiment Coefficient for Calculation of EQ-5D-Y Index Based on the Preferred Model

</div>

| Domain                           | Level | Rescaled DCE Coefficient |
|:---------------------------------|-------|--------------------------|
| Intercept                        |       | −0.025                   |
| Mobility                         | 2     | −0.040                   |
|                                  | 3     | −0.089                   |
| Looking after myself             | 2     | −0.018                   |
|                                  | 3     | −0.070                   |
| Doing usual activities           | 2     | −0.038                   |
|                                  | 3     | −0.101                   |
| Having pain or discomfort        | 2     | −0.077                   |
|                                  | 3     | −0.270                   |
| Feeling worried, sad, or unhappy | 2     | −0.049                   |
|                                  | 3     | −0.156                   |

</div>

<figure id="fig4-0272989X211001859">
<p><img src="10.1177_0272989X211001859-fig4.jpg" /></p>
<p><img src="10.1177_0272989X211001859-fig4.gif" /></p>
<figcaption>Distribution of EQ-5D-Y predicted value (all health states).</figcaption>
</figure>

The minimum predicted score was 0.288 \[33333\], and the second-best score was 0.957 \[12111\]. Unlike for the adult Japanese EQ-5D-3L states (second-best score 0.812), no large gap was observed between the best and second-best health states.

## Discussion

The objective of this study was to establish a Japanese value set for EQ-5D-Y. Preferences were elicited from 1047 participants, using DCE and cTTO, for EQ-5D-Y health states, and regression techniques were used to predict values for each of the states. The feasibility of the study protocol was confirmed: respondents were able to perform the tasks, and adequate levels of task engagement were observed. For example, the mean number of moves before reaching the point of indifference was sufficiently large. The interviewers also performed well, with a small percentage of flagged interviews: high levels of protocol compliance were observed, and there were no significant interviewer effects, which was supported by the similar distribution of cTTO values and of cTTO values for each health state. A mixed logit model was used to estimate the values for each of the states based on the DCE observations. All parameters were logically consistent. The least preferred item was level 3 for the “Having pain or discomfort” domain, and the second least was level 3 for the “Feeling worried, sad, or unhappy” domain.

The Japanese EQ-5D-Y value set has a narrow value range as compared with previously reported international results. The observed value of the worst EQ-5D-Y state was 0.20 (and had a predicted value of 0.28). In European countries, the mean observed value for the worst state \[33333\] reported by Kreimeier et al.<sup> 8 </sup> was −0.14. However, this difference in value range is not unique to EQ-5D-Y: Japanese values for the adult EQ-5D-5L were also higher than the corresponding European values.<sup> 23 </sup> The finding that the values for EQ-5D-Y states exceeded the values for the EQ-5D states for adults is consistent with the results published by Kreimeier et al.<sup> 24 </sup> The results thus appear to have good face validity and are also supported by the high level of protocol compliance and the lack of interviewer effects. Hence, the value set obtained reliably reflects the preferences of Japanese participants.

It is important to consider why the values attached to EQ-5D-Y states exceed those for the corresponding EQ-5D-3L or 5L health states (e.g., state 22222), since the consequences with respect to the use of EQ-5D-Y values alongside EQ-5D-3L or 5L values will depend on this finding. These differences are multicausal.

- TTO values for children are higher because people are more reluctant to trade time off on behalf of a child. Therefore, the values are calibrated differently. The same level of quality of life induces a smaller tradeoff where children are concerned.

- The descriptors used in EQ-5D-Y use wording relevant to children, and the choice of words makes the health states look less severe (22222 ≠ 22222). For example, the youth version has labels “some” or “a lot,” whereas the corresponding labels in the adult version are “moderate” or “extreme/unable to.”

- Children can actually have a better quality of life while experiencing the same health problems as an adult. Parents or other caregivers may dedicate more time to their children regardless of their health status. Moreover, children who are developing more independence may be less likely to rely on others for some things as compared with adults.

All of these explanations may hold some truth, which would imply that there is limited comparability of values derived from EQ-5D-Y and EQ-5D. The consequences for users are contemplated below.

A choice was made by the EuroQol Group to attach proxy-reported values from adults for a 10-y-old child to EQ-5D-Y health states. Another option could be to collect self-reported values from adolescents or young adults. For example, the CHU9D value set for Australia has been based on adolescents’ (aged 11–17 y) best-worst scaling responses and young adults’ (aged 18–29 y) TTO results.<sup> 14 </sup> Normally, arguments of inclusiveness support adolescents’ views, but the inherent limitation is that only partial information can be obtained, because tasks involving comparisons to death are not appropriate for this age group. Hence, the CHU-9D team derived TTO values from people closest in age: young adults. An open question is whether self-reported values from young adults or proxy-reported values from adults for a child are more relevant for the valuation of health outcomes in children. Moreover, it is unknown how the self-reported values derived from adolescents and adults (which were found to differ) compared with proxy-reported values from adults. Disentangling age and proxy effects is an important area for future research, and in the absence of evidence, researchers need to remain open-minded toward alternative approaches and to future updates of the protocol.

This study has some limitations. Participants were not recruited through a rigorous random sampling procedure because with such an approach, the time required for the survey would be too long; rather, the subjects were recruited from a few preselected geographical areas. In addition, although the cTTO tasks are already complex, the use of cTTO for valuing child health adds an extra layer of complexity: it may have been difficult for adults to imagine what impact health problems would have had on a hypothetical 10-y-old.

The observed differences in the EQ-5D-Y value ranges for young people and the EQ-5D for adults have implications for users and policy makers. Using the EQ-5D-Y weights presented in this article, it will be possible to compare relative levels of quality of life across different groups of children but not to compare levels of quality of life observed in children and adults. Similarly, if the EQ-5D-Y is to be applied routinely in assessing the cost-effectiveness of new life-saving health care interventions for children, the results can be used to support reimbursement decisions in pediatric settings. However, if children and adults are treated for the same condition, they can have different values attached to comparable quality-of-life outcomes, leading to differences in estimates of QALYs gained. Because the QALY weights for children are higher than the QALY weights for adults, a similar degree of improvement in an adult’s health state will generate fewer QALYs for a child. Thus, simple comparisons of cost-effectiveness ratios for adults and children should be avoided.

To conclude, we expect that this study will promote patient-centered research and economic evaluation in the area of health care technologies for children and adolescents. Important issues that need to be addressed in future research have also been identified.

## Acknowledgments

We received scientific support from the EuroQol Group (project 20180280).

## Footnotes

## Contributor Information

Takeru Shiroiwa, Center for Outcomes Research and Economic Evaluation for Health (C2H), National Institute of Public Health, Wako, Saitama, Japan.

Shunya Ikeda, Department of Medicine, International University of Health and Welfare, Narita, Chiba, Japan.

Shinichi Noto, Department of Health Sciences, Niigata University of Health and Welfare, Niigata, Japan.

Takashi Fukuda, Center for Outcomes Research and Economic Evaluation for Health (C2H), National Institute of Public Health, Wako, Saitama, Japan.

Elly Stolk, EuroQol Research Foundation, Rotterdam, South Holland, The Netherlands.

## References

## References

1. Rowen D, Rivero-Arias O, Devlin N, Ratcliffe J. Review of valuation methods of preference-based measures of health for economic evaluation in child and adolescent populations: where are we now and where are we going? Pharmacoeconomics. 2020;38(4):325–40. doi:10.1007/s40273-019-00873-7

2. Stevens K. Valuation of the Child Health Utility 9D Index. Pharmacoeconomics. 2012;30(8):729–47. doi:10.2165/11599120-000000000-00000

3. Moodie M, Richardson J, Rankin B, Iezzi A, Sinha K. Predicting time trade-off health state valuations of adolescents in four Pacific countries using the Assessment of Quality-of-Life (AQoL-6D) instrument. Value Health. 2010;13(8):1014–27. doi:10.1111/j.1524-4733.2010.00780.x

4. Torrance GW, Feeny DH, Furlong WJ, Barr RD, Zhang Y, Wang Q. Multiattribute utility function for a comprehensive health status classification system. Health Utilities Index Mark 2. Med Care. 1996;34(7):702–22. doi:10.1097/00005650-199607000-00004

5. Feeny D, Furlong W, Torrance GW, et al. Multiattribute and single-attribute utility functions for the health utilities index mark 3 system. Med Care. 2002;40(2):113–28. doi:10.1097/00005650-200202000-00006

6. Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727–36. doi:10.1007/s11136-011-9903-x

7. Ramos-Goñi JM, Oppe M, Stolk E, et al. International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics. 2020;38(7):653–63. doi:10.1007/s40273-020-00909-3

8. Kreimeier S, Oppe M, Ramos-Goni JM, et al. Valuation of EuroQol Five-Dimensional Questionnaire, Youth Version (EQ-5D-Y) and EuroQol Five-Dimensional Questionnaire, Three-Level Version (EQ-5D-3L) health states: the impact of wording and perspective. Value Health. 2018;21(11):1291–8. doi:10.1016/j.jval.2018.05.002

9. Shah KK, Ramos-Goñi JM, Kreimeier S, Devlin NJ. An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values. Eur J Health Econ. 2020;21(7):1091–103. doi:10.1007/s10198-020-01205-9

10. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goni JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation work: version 2 of the EQ-5D-5L valuation protocol. Value Health. 2019;22(1):23–30. doi:10.1016/j.jval.2018.05.010

11. Oppe M, Devlin NJ, van Hout B, Krabbe PF, de Charro F. A program of methodological research to arrive at the new international EQ-5D-5L valuation protocol. Value Health. 2014;17(4):445–53. doi:10.1016/j.jval.2014.04.002

12. Chen G, Xu F, Huynh E, Wang Z, Stevens K, Ratcliffe J. Scoring the Child Health Utility 9D instrument: estimation of a Chinese child and adolescent-specific tariff. Qual Life Res. 2019;28(1):163–76. doi:10.1007/s11136-018-2032-z

13. Krabbe PFM, Jabrayilov R, Detzel P, Dainelli L, Vermeulen KM, van Asselt ADI. A two-step procedure to generate utilities for the Infant health-related Quality of life Instrument (IQI). PLoS One. 2020;15(4):e0230852. doi:10.1371/journal.pone.0230852

14. Ratcliffe J, Huynh E, Chen G, et al. Valuing the Child Health Utility 9D: using profile case best worst scaling methods to develop a new adolescent specific scoring algorithm. Soc Sci Med. 2016;157:48–59. doi:10.1016/j.socscimed.2016.03.042

15. Ratcliffe J, Flynn T, Terlich F, Stevens K, Brazier J, Sawyer M. Developing adolescent-specific health state values for economic evaluation: an application of profile case best-worst scaling to the Child Health Utility 9D. Pharmacoeconomics. 2012;30(8):713–27. doi:10.2165/11597900-000000000-00000

16. Apajasalo M, Sintonen H, Holmberg C, et al. Quality of life in early adolescence: a sixteen-dimensional health-related measure (16D). Qual Life Res. 1996;5(2):205–11. doi:10.1007/BF00434742

17. Euroqol Group. EQ-5D-Y User Guide. 2020. Available from: https://euroqol.org/wp-content/uploads/2020/09/EQ-5D-Y-User-Guide_version-2.0.pdf. Accessed December 18, 2020.

18. Shiroiwa T, Fukuda T, Shimozuma K. Psychometric properties of the Japanese version of the EQ-5D-Y by self-report and proxy-report: reliability and construct validity. Qual Life Res. 2019;28(11):3093–105. doi:10.1007/s11136-019-02238-1

19. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goni JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004. doi:10.1007/s40273-016-0404-1

20. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJ, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health. 2017;20(3):466–73. doi:10.1016/j.jval.2016.10.012

21. Rowen D, Brazier J, Van Hout B. A comparison of methods for converting DCE values onto the full health-dead QALY scale. Med Decis Making. 2015;35(3):328–40. doi:10.1177/0272989X14559542

22. Ramos-Goñi JM, Pinto-Prades JL, Oppe M, Cabasés JM, Serrano-Aguilar P, Rivero-Arias O. Valuation and modeling of EQ-5D-5L health states using a hybrid approach. Med Care. 2017;55(7):e51–8. doi:10.1097/MLR.0000000000000283

23. Shiroiwa T, Ikeda S, Noto S, et al. Comparison of value set based on DCE and/or TTO data: scoring for EQ-5D-5L health states in Japan. Value Health. 2016;19(5):648–54. doi:10.1016/j.jval.2016.03.1834

24. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: the instrument’s characteristics, development, current use, and challenges of developing its value set. Value Health. 2019;22(1):31–7. doi:10.1016/j.jval.2018.11.001

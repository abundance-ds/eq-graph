---
project_id: "2003-RA"
work_id: "doi:10.1007/s10198-025-01857-5"
doi: "10.1007/s10198-025-01857-5"
pmid: "41165953"
pmcid: "PMC13190758"
title: "Child- versus adult-perspective composite time trade-off valuations for the EQ-5D-Y-3L: evidence from the Hungarian valuation study"
journal: "The European Journal of Health Economics"
publication_date: "2025-10-30"
volume: "27"
issue: "3"
authors:
  - name: "Stevanus Pangestu"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff2"
  - name: "Fanni Rencz"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Stefan A Lipman"
    affiliation_ids:
      - "Aff3"
affiliations:
  - id: "Aff1"
    name: "Department of Health Policy, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff2"
    name: "EuroQol Research Foundation, Rotterdam, the Netherlands"
  - id: "Aff3"
    name: "Erasmus School of Health Policy and Management, Erasmus University Rotterdam, Rotterdam, the Netherlands"
licence: "cc-by"
source_file: "input/projects/2003-RA/papers/doi_10.1007_s10198-025-01857-5.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13190758/fullTextXML"
source_method: "epmc_xml"
source_sha256: "96f2d67bf07bfe743e95bb6a3f729349281c851fad33d82b8700a54488019652"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Child- versus adult-perspective composite time trade-off valuations for the EQ-5D-Y-3L: evidence from the Hungarian valuation study

## Abstract

### Background

The EQ-5D-Y-3L is a generic, preference-accompanied health measure intended for pediatric populations. EQ-5D-Y-3L health states are valued using the perspective of a hypothetical 10-year-old child (‘child perspective’) rather than adults valuing for themselves (‘adult perspective’). The perspective used has been shown to influence valuation outcomes, affecting comparability of health utilities. This study explored within-respondent differences in values between adult and child perspectives using data from Hungary.

### Methods

A secondary analysis was conducted using composite time trade-off (cTTO) data from the Hungarian EQ-5D-Y-3L valuation study. Two hundred adults valued 10 health states from the child perspective and four from the adult perspective. The cTTO values for the matched health states (valued from both perspectives) were compared, with differences analyzed using t-tests and random-intercept regression. Associations with respondent characteristics were also explored.

### Results

Differences in cTTO values were observed between perspectives, particularly for more severe health states. Compared to the adult perspective, the child perspective yielded significantly lower values for worse-than-dead observations, but higher values for better-than-dead observations. After adjusting for within-subject variation and respondent characteristics, perspective was not a significant predictor of cTTO values. Instead, differences were partly explained by education, region of residence, parental status, and the view that a child’s life is more valuable than an adult’s.

### Conclusions

This is the first study to explore perspective differences in EQ-5D-Y-3L health state valuation within respondents using nationally representative data from outside Western Europe. The findings highlight the importance of considering individual-level attributes in pediatric health valuation.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s10198-025-01857-5.

**Keywords:** EQ-5D-Y-3L, Health state, Perspective, Composite time trade-off, Valuation, Youth

Received 2025 May 7; Accepted 2025 Oct 7; Issue date 2026.

## Introduction

The EQ-5D-Y-3L is a standardized, generic, preference-accompanied instrument for measuring health-related quality of life in children and adolescents aged 4 to 15 \[1, 2\]. It is an adaptation of the EQ-5D, designed to be comprehensible for younger populations. To develop national value sets for the EQ-5D-Y-3L, which are necessary for calculating quality-adjusted life-years (QALYs), the EQ-5D-Y-3L International Valuation Protocol recommends that members of the general population value hypothetical child-specific health states using both composite time trade-off (cTTO) and discrete choice experiment (DCE) methodologies \[3\]. A key difference from the valuation of the adult EQ-5D instrument is that for the EQ-5D-Y-3L, adults are interviewed to elicit preferences from the perspective of a hypothetical 10-year-old child (hereafter referred to as the child perspective), rather than from their own point of view (hereafter: the adult perspective). As acknowledged by the authors of the protocol \[3\], asking adults to value children’s health states (i.e., to express preferences about which health state would be better for a 10-year-old child) presents both methodological and normative challenges \[4\]. Key concerns include whether adults can accurately represent children’s experiences and the ethical importance of involving children themselves to respect their right to express their views \[5, 6\]. Nevertheless, the use of the child perspective by adults was introduced to reflect a taxpayer view and to address concerns regarding the complexity of the valuation tasks for children \[3\].

Previous research has illustrated how varying perspectives in cTTO can elicit different responses. Such differences may affect the comparability of health state valuations, potentially compromising standardized value sets and leading to biased QALY calculations \[4\]. Generally, health state values for children are higher than those for adults \[3, 7, 8\], with higher valuations linked to less variability \[8\]. Qualitative evidence suggests several reasons for the reluctance to trade-off life years in children: discomfort with imposing hypothetical impairments on children, the perception that adults cope better with difficulties, and uncertainty over who is best suited to make these valuations \[9–11\]. It has been suggested that adults may find it more challenging to value health states using a child’s perspective due to adults perceiving children’s health states as more similar to one another, or using simpler heuristics when considering children’s health-related quality of life \[12\].

Some studies have examined how the same individual (i.e., within respondents) values EQ-5D-Y-3L health states from different perspectives. One experiment with 200 Dutch university students showed that valuation outcomes can systematically vary depending on whether respondents valued health states from the perspective of an adult or a child, and whether they were deciding for themselves or for another person \[8\]. Another experiment involving 150 Dutch adults found no significant differences between valuing child health states using the adult and child perspectives \[13\], whereas two studies with UK adults identified significant differences between these perspectives \[14, 15\]. Such differences in utilities between both perspectives were even found to be more pronounced in lead-time TTO compared to cTTO \[16\].

Despite recent findings on within-respondent differences, further research is needed to better understand how perspective-driven differences influence utility values. Existing studies comparing cTTO perspectives have been conducted primarily in Western Europe \[8, 14–18\]. It is important to determine whether issues related to different perspectives extend across different countries and cultures, as health utilities may vary based on cultural values and geographical contexts \[19–22\]. In addition, previous research has shown that valuation outcomes can also be influenced by individual characteristics such as age, sex, and education \[13, 23\]. This study aims to contribute to the literature by providing insights from Hungary, a Central and Eastern European country where the EQ-5D and EQ-5D-Y-3L are preferred instruments for health technology assessment \[24\]. Our analysis is grounded in data collected using the EuroQol Valuation Technology (EQ-VT) as part of the EQ-5D-Y-3L valuation study in Hungary \[25\].

## Methods

As the study methodology, including preference elicitation methods, health state selection, and sampling, has been described in detail elsewhere \[25, 26\], this section provides only a brief overview of the original methods.

### EQ-5D-Y-3L

The EQ-5D-Y-3L consists of a descriptive system and a visual analogue scale (EQ VAS). The descriptive system assesses health-related quality of life across five dimensions: mobility (walking about), looking after myself (washing or dressing), usual activities (going to school, hobbies, sports, playing, doing things with family or friends), having pain or discomfort, and feeling worried, sad, or unhappy. Each dimension has three response levels: level 1 indicates ‘no problems’, ‘no pain or discomfort’, or ‘not worried, sad, or unhappy’; level 2 indicates ‘some problems’, ‘some pain or discomfort’, ‘a bit worried, sad, or unhappy’; and level 3 indicates ‘a lot of problems’, ‘a lot of pain or discomfort’, or ‘very worried, sad, or unhappy’. A respondent’s health state profile is represented as a five-digit string, where each digit corresponds to the severity level in a given dimension. For example, ‘12323’ indicates no problems with walking about, some problems with washing or dressing, a lot of problems doing usual activities, some pain or discomfort, and very worried, sad, or unhappy. Since each dimension has three levels, there are 243 (3<sup>5</sup>) unique health states. A level-sum-score (LSS) can be calculated by summing the five-digit health state, with possible scores ranging from 5 (full health: 11111) to 15 (worst health: 33333). Next, the EQ VAS captures self-rated health on 0–100 vertical scale, where 0 and 100 represent ‘the worst health you can imagine’ and ‘the best health you can imagine,’ respectively. Existing evidence on the measurement properties of the EQ-5D-Y-3L supports its applicability \[27\]. This study used the official Hungarian version of the EQ-5D-Y-3L.

### Data description

A secondary analysis was conducted using data collected from the Hungarian EQ-5D-Y-3L valuation study, which received ethical approval from the Research Ethics Committee of Corvinus University of Budapest (KRH/31/2021) \[25\]. The cTTO tasks were carried out using the EQ-VT (v2.1) software, which included both conventional 10-year TTO valuations better-than-dead states and a lead-time TTO variant for worse-than-dead states (i.e., 10 years in full health followed by 10 years in an EQ-5D-Y-3L state). The interviews were conducted by four graduate students who had prior experience with the Hungarian EQ-5D-3L and EQ-5D-5L parallel valuation study \[28\]. All interviewers received standardized training on valuation methods, the EQ-VT protocol, and quality control procedures. Each interviewer completed 50 interviews for the EQ-5D-Y-3L valuation study.

Each recruited respondent valued two example health states (e.g., being in a wheelchair), three practice EQ-5D-Y-3L health states (21112, 32323, and 13311), and 10 ‘real’ EQ-5D-Y-3L states from the perspective of a 10-year-old child (exact phrasing: ‘Considering your views for a 10-year-old child.’). Respondents valued the following 10 health states in random order: three mild states (11112, 11121, and 21111), two moderate states (22223 and 22232), four severe states (31133, 32223, 33233, and 33323), and the worst health state (33333). After completing the valuation tasks, respondents were presented with a ranked list of the 10 health states (‘feedback module’) based on their responses. Using this module, respondents had the option to flag any health state valuation that they felt did not reflect their preferences, even if the responses appeared consistent. As the final step of the interview, respondents valued another four EQ-5D-Y-3L health states, this time from their own (adult) perspective. These states were randomly selected from the same set of 10 health states previously valued from the child perspective. The ‘feedback module’ was not used for the adult-perspective valuations.

Overall, 200 Hungarian adults, representative of the general population in terms of age and sex, completed the cTTO tasks. In addition to the valuation exercise, respondents completed a questionnaire covering sociodemographic characteristics (e.g., education, civil status, number of children and their age, and residential area), health status (i.e., chronic conditions and self-rated general health), and self-complete versions of the EQ-5D-3L and EQ-5D-5L. They also rated their agreement with the statement: ‘A child’s life is worth more than an adult’s as they have more ahead of them,’ using a five-level Likert scale (‘strongly disagree’ to ‘strongly agree’).

### Statistical analysis

Each respondent valued 10 health states from the child perspective and four from the adult perspective, allowing for direct paired comparisons of the four matched health states valued from both perspectives. Prior to analysis, observations flagged in the EQ-VT ‘feedback module’ were excluded to ensure data quality. Distributions of cTTO values for the child and adult perspectives were first visualized separately using histograms. Clustering at the extreme values (−1.0 and 1.0) was compared between perspectives using McNemar’s test to confirm that the observed pattern was not due to random variation. The distribution of paired differences (i.e., child minus adult values) was examined using median and deciles, and the Wilcoxon signed-rank test was performed to assess whether the median differed significantly from zero. A Bland-Altman plot was generated to illustrate the difference between the two perspectives, displaying the difference (y-axis) against the mean value for each matched pair (x-axis) with points color-coded by LSS. Mean differences between perspectives were assessed using the Student’s t-test; mean cTTO values were initially compared by individual health state profiles and subsequently by severity categories (i.e., mild, moderate, and severe/worst) to improve statistical power. Subgroup analyses were additionally performed for better-than-dead and only worse-than-dead values, where the number of observations was sufficient. Classification was based on the child-perspective value; e.g., if a state was rated better-than-dead in the child perspective but worse-than-dead in the adult, it was classified as better-than-dead. cTTO values exactly equal to zero were classified as either better-than-dead or worse-than-dead, depending on the type of valuation task completed by respondents: conventional TTO for the former or lead-time TTO for the latter.

To explore predictors of differences in cTTO values between perspectives, four multivariate linear regression models were estimated. Random-intercept models were used to account for the repeated observations per respondent, and robust standard errors were applied to account for heteroskedasticity. In the first two models, cTTO values were regressed separately for the child and adult perspectives to examine perspective-specific associations, using all responses for each perspective (i.e., not limited to the matched observations). Predictors included the LSS of the valued health states (centered by subtracting six to simplify interpretation, given that its values ranged from 6 to 15), age, sex, education, region of residence, number of children, and the view that a child’s life is more valuable than an adult’s (recoded as a binary variable due to limited variability, with responses dichotomized into agreement versus disagreement or neutrality). Individual-level covariates were selected based on prior literature \[19–22\]. For the subsequent models, analyses were restricted to health states that had been valued under both perspectives. In the third model, cTTO values were pooled into a single regression and a dummy variable for perspective was included as an additional predictor (coded 1 for child perspective, 0 for adult). This specification allowed to test the overall effect of perspective, while controlling for the same set of respondent characteristics. In the fourth model, the same predictors (as in the first two models) were used to estimate differences in cTTO values, using the difference between the child and adult values for each matched health state as the dependent variable. The analyses were conducted using Stata/MP 18 (StataCorp LLC, 2023) and the Bland-Altman plot was generated using the ‘ggplot2’ package in RStudio 2024.12.1 + 563 (Posit Software, PBC). Statistical significance was set at *p* \< 0.05.

## Results

Table <a href="#Tab1" data-ref-type="table">1</a> presents an overview of respondent characteristics, while comprehensive details have been previously published \[25\]. The study included 200 respondents (mean age 48.1 ± 18.6; 46.0% female). Most had at least a secondary education (71.5%), were married or partnered (64.5%), and had children (61%). Most respondents reported being in at least good health (80.5%). A total of 34% respondents agreed that a child’s life held greater value than an adult’s, while 28% were neutral and 38% disagreed.

<div id="Tab1" class="table-wrap">

<div class="caption">

Respondent characteristics

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="2" style="text-align: left;">Variables</th>
<th colspan="2" style="text-align: left;">Overall sample (<em>n</em> = 200)</th>
</tr>
<tr>
<th style="text-align: left;"><em>N</em> or Mean</th>
<th style="text-align: left;">% or SD</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;">Age</td>
<td style="text-align: left;">48.1</td>
<td style="text-align: left;">18.6</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Sex</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">108</td>
<td style="text-align: left;">54.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">46.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Highest education</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Primary or less</td>
<td style="text-align: left;">57</td>
<td style="text-align: left;">28.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Secondary</td>
<td style="text-align: left;">82</td>
<td style="text-align: left;">41.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Tertiary</td>
<td style="text-align: left;">61</td>
<td style="text-align: left;">30.5%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Civil status</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Married/partnered</td>
<td style="text-align: left;">129</td>
<td style="text-align: left;">64.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Single</td>
<td style="text-align: left;">37</td>
<td style="text-align: left;">18.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Divorced</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">4.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Widowed</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">10.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Others</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">2.5%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Children<sup>a</sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">None</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">39.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">At least one &lt; 18</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">22.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Only child(ren) ≥ 18</td>
<td style="text-align: left;">77</td>
<td style="text-align: left;">38.5%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Net monthly household income (HUF)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">50,001–500,000</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">24.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">500,001–800,000</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">19.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">800,000+</td>
<td style="text-align: left;">27</td>
<td style="text-align: left;">13.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Didn’t know/refused to answer</td>
<td style="text-align: left;">87</td>
<td style="text-align: left;">43.5%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Residential area</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Western Hungary</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">42.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Central Hungary</td>
<td style="text-align: left;">49</td>
<td style="text-align: left;">24.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Eastern Hungary</td>
<td style="text-align: left;">66</td>
<td style="text-align: left;">33.0%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Views child’s life as more valuable than adult’s</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Strongly disagree</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">8.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Disagree</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">30.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Neutral</td>
<td style="text-align: left;">56</td>
<td style="text-align: left;">28.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Agree</td>
<td style="text-align: left;">53</td>
<td style="text-align: left;">26.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Strongly agree</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">7.5%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Self-rated general health</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Excellent</td>
<td style="text-align: left;">35</td>
<td style="text-align: left;">17.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Very good</td>
<td style="text-align: left;">69</td>
<td style="text-align: left;">34.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Good</td>
<td style="text-align: left;">57</td>
<td style="text-align: left;">28.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Poor</td>
<td style="text-align: left;">32</td>
<td style="text-align: left;">16.0%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Fair</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">3.5%</td>
</tr>
</tbody>
</table>

<sup>a</sup>Included biological, adopted, and stepchildren

</div>

After excluding 68 flagged responses through the feedback module, 772 observations were included in the matched comparisons. Figure <a href="#Fig1" data-ref-type="fig">1</a> shows the full cTTO distributions for both perspectives, displayed as percentages. The adult perspective showed more pronounced clustering at both 1.0 and − 1.0 (McNemar’s chi-square = 28.26, *p* \< 0.001). The distribution of paired differences (child minus adult) was centered around zero, with 80% of observations falling between − 0.30 and 0.29. The Wilcoxon signed-rank test indicated no shift in the median of paired differences from zero (*p* = 0.458). Figure <a href="#Fig2" data-ref-type="fig">2</a> illustrates that differences between perspectives were smaller for milder health states, but variability increased for more severe states, where child-perspective values tended to be higher than adult-perspective values. Further examination revealed that 33 observations were considered worse-than-dead in the adult perspective but better-than-dead in the child perspective, and conversely, 54 were considered better-than-dead in the adult perspective but worse-than-dead in the child perspective. These cases occurred primarily in severe states: 29 (87.9%) and 37 (68.5%), respectively.

<figure id="Fig1">
<p><img src="10198_2025_1857_Fig1_HTML.jpg" id="d33e722" /></p>
<p><img src="10198_2025_1857_Fig1_HTML.gif" /></p>
<figcaption>cTTO values for adult and child perspectives</figcaption>
</figure>

<figure id="Fig2">
<p><img src="10198_2025_1857_Fig2_HTML.jpg" id="d33e729" /></p>
<p><img src="10198_2025_1857_Fig2_HTML.gif" /></p>
<figcaption>Bland-Altman plot assessing perspective differences</figcaption>
</figure>

The mean cTTO difference was close to zero (*p* = 0.839) (Table <a href="#Tab2" data-ref-type="table">2</a>). For mild health states, mean cTTO values were slightly lower for the child perspective (mean difference=−0.01, *p* = 0.015). No significant differences were found for moderate (*p* = 0.128) or severe/worst (*p* = 0.348) health states. When considering only better-than-dead observations, the child perspective showed significantly higher values (mean difference = 0.03, *p* = 0.005), particularly for severe/worst states (mean difference = 0.11, *p* \< 0.001). Conversely, in worse-than-dead observations, the child perspective had overall lower (or worse) values than the adult perspective (mean difference=−0.08, *p* = 0.003), including for severe/worst states (mean difference=−0.06, *p* = 0.042). Comparisons of cTTO values between perspectives by health state profile are presented in Table S1.

<div id="Tab2" class="table-wrap">

<div class="caption">

Comparison of cTTO values between perspectives by health state severity

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="2" style="text-align: left;">Health state</th>
<th rowspan="2" style="text-align: left;"><em>n</em></th>
<th colspan="2" style="text-align: left;">Child perspective<sup>a, b</sup></th>
<th colspan="2" style="text-align: left;">Adult perspective<sup>b</sup></th>
<th rowspan="2" style="text-align: left;">Mean difference</th>
<th rowspan="2" style="text-align: left;"><em>p</em>-value</th>
</tr>
<tr>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">All cTTO values</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">245</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">−0.01</td>
<td style="text-align: left;">0.015</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">145</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">−0.04</td>
<td style="text-align: left;">0.128</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Severe/worst</td>
<td style="text-align: left;">382</td>
<td style="text-align: left;">−0.19</td>
<td style="text-align: left;">0.54</td>
<td style="text-align: left;">−0.21</td>
<td style="text-align: left;">0.60</td>
<td style="text-align: left;">0.02</td>
<td style="text-align: left;">0.348</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Overall</td>
<td style="text-align: left;">772</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.00</td>
<td style="text-align: left;">0.839</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong><em>Better-than-dead states</em></strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">245</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">−0.01</td>
<td style="text-align: left;">0.015</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">129</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.01</td>
<td style="text-align: left;">0.798</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Severe/worst</td>
<td style="text-align: left;">177</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Overall</td>
<td style="text-align: left;">551</td>
<td style="text-align: left;">0.63</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.60</td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">0.007</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong><em>Worse-than-dead states</em></strong> <sup><strong><em>c</em></strong></sup></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Severe/worst</td>
<td style="text-align: left;">205</td>
<td style="text-align: left;">−0.63</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">−0.57</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">−0.06</td>
<td style="text-align: left;">0.042</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Overall</td>
<td style="text-align: left;">221</td>
<td style="text-align: left;">−0.61</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">−0.53</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">−0.08</td>
<td style="text-align: left;">0.003</td>
</tr>
</tbody>
</table>

*Abbrv.* *cTTO * composite time trade-off, *SD* standard deviation

<sup>a</sup>Excluding flagged responses.

<sup>b</sup>Only matched health states, i.e., valued from both perspectives. Better- or worse-than dead classification was based on the child-perspective value.

<sup>c</sup>Moderate health states with negative cTTO values (n = 16) were excluded due to insufficient number of observations.

*Notes.*1. The severity of valued health states were mild (11112, 11121, and 21111), moderate (22223 and 22232), severe (31133, 32223, 33233, and 33323) and worst (33333).

Severe and worst health states were combined in theanalysis. There were 87 observations for the worst health state, with 25 rated as better-than-dead and 62 as worse-than-dead. In the worse-than-dead category, the mean difference forsevere states alone was not statistically significant (mean difference= -0.05, *p*=0.170), suggestingthat the observed effect was primarily driven by the worse state. For both the full set of observations and the better-than-dead category, there results were consistent regardless of whether the worst state was included among the severe states.

</div>

Table <a href="#Tab3" data-ref-type="table">3</a> presents regression results on factors associated with cTTO values. In Models 1 and 2, most respondent characteristics were not statistically significant. In the adult-perspective model (Model 2), having at least one child (aged \< 18) was associated with higher cTTO values (beta = 0.137, *p* \< 0.05). Model 3 showed no significant effect of perspective on cTTO values (beta=−0.002, *p* = 0.871). Across all three models, the LSS of the valued health states was consistently a significant predictor (*p* \< 0.001). Model 4, which analyzed paired differences between perspectives, found that greater value differences (i.e., higher values from the child relative to the adult perspective) were associated with respondents who agreed that a child’s life was more valuable than an adult’s (*p* \< 0.05). Conversely, lower value differences (i.e., higher values from the adult perspective) were associated with possessing secondary education, residence in Central Hungary, and having only adult children (all *p* \< 0.05), with the latter showing the largest effect (beta=−0.116). Sensitivity analyses including the flagged states in the feedback module showed no difference in the regression results.

<div id="Tab3" class="table-wrap">

<div class="caption">

Regression coefficients and robust standard errors

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Variable</th>
<th colspan="3" style="text-align: left;">Outcome: cTTO values</th>
<th style="text-align: left;">Outcome: cTTO value differences<br />
(child minus adult values)</th>
</tr>
<tr>
<th style="text-align: left;">Child perspective</th>
<th style="text-align: left;">Adult perspective</th>
<th style="text-align: left;">Both perspectives<sup>a</sup></th>
<th style="text-align: left;">Both perspectives<sup>a</sup></th>
</tr>
<tr>
<th style="text-align: left;">Model 1</th>
<th style="text-align: left;">Model 2</th>
<th style="text-align: left;">Model 3</th>
<th style="text-align: left;">Model 4</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Constant</td>
<td style="text-align: left;">0.906 (0.073)<sup>***</sup></td>
<td style="text-align: left;">0.783 (0.092)<sup>***</sup></td>
<td style="text-align: left;">0.832 (0.083)<sup>***</sup></td>
<td style="text-align: left;">0.107 (0.053)<sup>*</sup></td>
</tr>
<tr>
<td style="text-align: left;">LSS of valued health state</td>
<td style="text-align: left;">−0.152 (0.003)<sup>***</sup></td>
<td style="text-align: left;">−0.157 (0.005)<sup>***</sup></td>
<td style="text-align: left;">−0.156 (0.004)<sup>***</sup></td>
<td style="text-align: left;">0.003 (0.003)</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">0.017 (0.038)</td>
<td style="text-align: left;">−0.049 (0.048)</td>
<td style="text-align: left;">−0.007 (0.042)</td>
<td style="text-align: left;">0.054 (0.029)</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">0.000 (0.001)</td>
<td style="text-align: left;">0.001 (0.001)</td>
<td style="text-align: left;">0.001 (0.001)</td>
<td style="text-align: left;">0.000 (0.001)</td>
</tr>
<tr>
<td style="text-align: left;">Education (ref: primary)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Secondary</td>
<td style="text-align: left;">0.038 (0.042)</td>
<td style="text-align: left;">0.116 (0.054)</td>
<td style="text-align: left;">0.071 (0.047)</td>
<td style="text-align: left;">−0.092 (0.032)<sup>**</sup></td>
</tr>
<tr>
<td style="text-align: left;">Tertiary</td>
<td style="text-align: left;">0.029 (0.056)</td>
<td style="text-align: left;">0.073 (0.073)</td>
<td style="text-align: left;">0.056 (0.062)</td>
<td style="text-align: left;">−0.037 (0.046)</td>
</tr>
<tr>
<td style="text-align: left;">Country region (ref: Western Hungary)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Central Hungary</td>
<td style="text-align: left;">0.007 (0.054)</td>
<td style="text-align: left;">0.105 (0.072)</td>
<td style="text-align: left;">0.035 (0.060)</td>
<td style="text-align: left;">−0.108 (0.048)<sup>*</sup></td>
</tr>
<tr>
<td style="text-align: left;">Eastern Hungary</td>
<td style="text-align: left;">0.019 (0.039)</td>
<td style="text-align: left;">0.044 (0.052)</td>
<td style="text-align: left;">0.031 (0.045)</td>
<td style="text-align: left;">−0.017 (0.031)</td>
</tr>
<tr>
<td style="text-align: left;">Children (ref: no children)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">At least one child &lt; 18</td>
<td style="text-align: left;">0.074 (0.045)</td>
<td style="text-align: left;">0.137 (0.062)<sup>*</sup></td>
<td style="text-align: left;">0.093 (0.052)</td>
<td style="text-align: left;">−0.075 (0.043)</td>
</tr>
<tr>
<td style="text-align: left;">Only child(ren) &gt; = 18</td>
<td style="text-align: left;">0.018 (0.049)</td>
<td style="text-align: left;">0.129 (0.071)</td>
<td style="text-align: left;">0.064 (0.059)</td>
<td style="text-align: left;">−0.116 (0.041)<sup>**</sup></td>
</tr>
<tr>
<td style="text-align: left;">Views child’s life as more valuable than adult’s<sup>b</sup></td>
<td style="text-align: left;">−0.016 (0.039)</td>
<td style="text-align: left;">−0.084 (0.048)</td>
<td style="text-align: left;">−0.048 (0.042)</td>
<td style="text-align: left;">0.067 (0.028)<sup>*</sup></td>
</tr>
<tr>
<td style="text-align: left;">Child perspective</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">−0.002 (0.014)</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">n</td>
<td style="text-align: left;">1932</td>
<td style="text-align: left;">800</td>
<td style="text-align: left;">1544</td>
<td style="text-align: left;">772</td>
</tr>
<tr>
<td style="text-align: left;">R-squared</td>
<td style="text-align: left;">64.13%</td>
<td style="text-align: left;">60.28%</td>
<td style="text-align: left;">63.46%</td>
<td style="text-align: left;">5.12%</td>
</tr>
</tbody>
</table>

\*, \*\*, and \*\*\* indicate significance at *p* \< 0.05, *p* \< 0.01, and *p* \< 0.001, respectively.

*Abbrv.* *cTTO* composite time trade-off, *LSS* level sum score, *ref* reference category

Note. Flagged responses were excluded from the analyses.

<sup>a</sup>Only matched health states, i.e., valued from both perspectives.

<sup>b</sup>Coded as 1 if respondents agreed with the statement, 0 if neutral or disagreed.

</div>

## Discussion

This study is the first to explore within-respondent differences in valuing EQ-5D-Y-3L health states from both adult and child perspectives in a national sample outside Western Europe. When comparing valuations of the same health states within respondents, we observed varied evidence regarding the influence of perspective. The child perspective yielded higher values for better-than-dead observations, a pattern consistent with findings from earlier studies \[10, 15, 17, 18\]. However, for worse-than-dead observations, the child perspective yielded lower values than the adult perspective. Across both better- and worse-than-dead observations, notable differences were observed across mild, moderate, and severe health states, with the gap widening as severity increased; a pattern also seen in previous research for the most severe states \[8, 23\]. For milder states, valuations tended to converge, perhaps because both children and adults are perceived as similarly able to manage minor health issues. Smaller differences in these cases may also reflect statistical constraints, as large variations are less likely when health states are closer to full health. As hypothetical health problems worsened, the emotional and cognitive burden of the valuation task likely increased. However, the worst health state might not have been the most cognitively demanding; moderate and severe states may have posed greater challenges, requiring more deliberation and nuanced trade-offs. This may help explain the contrasting pattern seen in severe states, where child-perspective values were higher when states were considered better-than-dead but lower when considered worse-than-dead. One possible explanation is the stronger emotional response evoked when imagining a child in extreme suffering. In addition, adults may project stronger time preferences onto children, potentially contributing to opposite valuation patterns in better-than-dead versus worse-than-dead scenarios \[16, 29\]. Respondents may have found it particularly distressing to consider a child experiencing severe illness, pain or disability, possibly due to the children’s greater perceived vulnerability compared to adults \[9, 10\], leading to more negative valuations in worse-than-dead cases. Conversely, when states were judged better-than-dead, the child perspective may have prompted greater optimism or a reluctance to trade life years, resulting in higher valuations. Alternatively, this pattern may reflect methodological effects; the use of lead-time TTO for worse-than-dead states could have introduced additional complexity, potentially influencing how respondents arrived at their decisions.

Interestingly, perspective was not significantly associated with cTTO values after controlling for within-subject variation in the regression analysis. This suggests that the observed differences may be attributable to individual-level attributes rather than perspective alone. Higher values from the child’s perspective were associated with those who held the view that a child’s life is more valuable than an adult’s. This view may reflect a normative or ethical stance that makes respondents more reluctant to trade off life years during valuation tasks. Meanwhile, respondents with secondary education, those living in Central Hungary, and with only adult children were more likely to assign higher values from the adult perspective. Residents of Central Hungary may exhibit more individualistic views, potentially influenced by higher income, different political views, greater healthcare access and urban social norms \[30–32\]. Likewise, parents of adult children may shift their preferences toward adult health issues \[33\], including concerns related to their own and that of their children. Our finding regarding education contrasts with a Dutch general population study, which found that higher educational attainment was associated with a greater prioritization of caring for children \[13\]. These differing public attitudes may reflect underlying cultural values and differences between national healthcare systems.

A recent Delphi study, which gathered input from experts across 18 countries, highlighted that there is still no clear consensus on the perspective to use when adults are asked to value child health states \[34\]. With the introduction of EQ-5D-Y-5L \[2\] and expected rollout of future valuation studies, the question of which perspective to adopt becomes increasingly relevant. Our findings confirm that the perspective used in valuation tasks significantly influences utility values. Such differences can affect the precision and comparability of health state valuations, introducing systematic variations that may impact health economic analyses and reimbursement decisions. However, these differences may not be uniform and vary across populations. To some extent, these variations in valuation outcomes appear to be shaped by cultural and sociodemographic factors. One possible direction for future valuation protocols is to offer a suite of standardized approaches that can be selected based on the health system context. Instead of applying a single fixed method, such a suite would allow decision-makers to choose the approach that best reflects local priorities and value considerations. Further methodological research is needed to determine the most robust approach, alongside stakeholder engagement to establish normatively acceptable valuation practices.

This study has several limitations. As a secondary study which relied on an existing dataset, some analyses may have been underpowered. All respondents valued health states from the child perspective before the adult perspective, introducing a potential order effect that may have influenced the results. This sequencing could have also led to learning effects, as respondents were already familiar with the valuation tasks by the time they reached the adult-perspective exercises \[35\]. Respondent fatigue may have emerged by this stage as well, potentially affecting the quality of responses. The limited overlap in health states valued from both perspectives may have also reduced variability in responses and constrained the scope of our comparisons. More broadly, the relatively small set of 10 states included in many EQ-5D-Y-3L valuation studies may have limited overall variation across respondents. This might have been different if a larger set of states had been presented across respondents, for example by using multiple blocks. Lastly, data collection took place during the COVID-19 pandemic, which may have influenced respondents’ health preferences. Despite these limitations, this study provides valuable insights into factors associated with cTTO value differences, using EQ-VT (v2.1) data that allowed for direct within-respondent comparisons.

## Conclusions

This study identified within-respondent differences in the valuation of child health states depending on the perspective used. However, after adjusting for within-respondent variation, perspective was not a systematic predictor of health state values. Instead, differences were more closely associated with individual-level attributes. These findings highlight the need for careful consideration in future valuation studies, as both the choice of perspective and cultural context can influence utility values and, subsequently, health economic evaluations.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 8.77 MB)

</div>

## Acknowledgements

We would like to thank the interviewers of the Hungarian EQ-5D-Y-3L valuation study: Anna Nikl, Alex Bató, Mercédesz M. Angyal, and Zita Bagdi. An earlier version of this work was presented at the 42nd EuroQol Plenary, and we thank the participants who provided valuable feedback.

## Author contributions

Conception: SP, BR, FR, SAL; Formal analysis: SP; Writing - original draft: SP; Writing - review and editing: SP, BR, FR, SAL; Funding acquisition: SP, BR, FR, SAL; Resources: FR.

## Funding

Open access funding provided by Corvinus University of Budapest. This study was funded by the EuroQol Research Foundation (2003-RA). Data collection was supported by the Higher Education Institutional Excellence Program 2020 of the Ministry of Human Capacities as part of the ‘Financial and Public Services’ research project (TKP2020-IKA-02) at the Corvinus University of Budapest, with additional contributions from the EuroQol Research Foundation (192-2020VS).

## Data availability

The data used in this study are available from FR upon reasonable request.

## Declarations

SP, FR, and BR are employed by the EuroQol Research Foundation. FR, BR, and SAL are members of the EuroQol Group. All authors have received grants from EuroQol for work outside of the scope of this study. The views expressed are those of the authors and do not necessarily reflect the views of the EuroQol Research Foundation.

### Ethics approval

Ethics approval for the Hungarian EQ-5D-Y-3L valuation study (192-2020VS) was obtained from the Research Ethics Committee of Corvinus University of Budapest (no. KRH/31/2021).

### Role of the funder

The funder had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review or approval of the manuscript; and decision to submit the manuscript for publication.

## Footnotes

## References

## References

1. Wille, N., et al.: Development of the EQ-5D-Y: A child-friendly version of the EQ-5D. Qual. Life Res. 19(6), 875–886 (2010). doi:10.1007/s11136-010-9648-y

2. EuroQol Research Foundation: EQ-5D-Y-5L User Guide: How to apply and score, and present results from the EQ-5D-Y-5L, Version 1.0, September 2024, Rotterdam, The Netherlands (2024)

3. Ramos-Goñi, J.M., et al.: International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics 38(7), 653–663 (2020). doi:10.1007/s40273-020-00909-3

4. Lipman, S.A., Reckers-Droog, V.T., Kreimeier, S.: Think of the children: A discussion of the rationale for and implications of the perspective used for EQ-5D-Y health state valuation. Value Health 24(7), 976–982 (2021). doi:10.1016/j.jval.2021.01.011

5. Rowen, D., et al.: Review of valuation methods of Preference-Based measures of health for economic evaluation in child and adolescent populations: where are we now and where are we going? Pharmacoeconomics 38(4), 325–340 (2020). doi:10.1007/s40273-019-00873-7

6. Rowen, D., et al.: Exploring the issues of valuing child and adolescent health States using a mixed sample of adolescents and adults. Pharmacoeconomics 40(5), 479–488 (2022). doi:10.1007/s40273-022-01133-x

7. Kind, P., et al.: Can adult weights be used to value child health states? Testing the influence of perspective in valuing EQ-5D-Y. Qual. Life Res. 24(10), 2519–2539 (2015). doi:10.1007/s11136-015-0971-1

8. Lipman, S.A., et al.: Self vs. other, child vs. adult. An experimental comparison of valuation perspectives for valuation of EQ-5D-Y-3L health States. Eur. J. Health Econ. 22(9), 1507–1518 (2021). doi:10.1007/s10198-021-01377-y

9. Reckers-Droog, V., et al.: Why do adults value EQ-5D-Y-3L health States differently for themselves than for children and adolescents: A Think-Aloud study. Value Health 25(7), 1174–1184 (2022). doi:10.1016/j.jval.2021.12.014

10. Dewilde, S., et al.: Exploration of the reasons why health state valuation differs for children compared with adults: A mixed methods approach. Value Health 25(7), 1185–1195 (2022). doi:10.1016/j.jval.2021.11.1377

11. Åström, M., et al.: Like holding the axe on who should live or not’: Adolescents’ and adults’ perceptions of valuing children’s health States using a standardised valuation protocol for the EQ-5D-Y-3L. Qual. Life Res. 31(7), 2133–2142 (2022). doi:10.1007/s11136-022-03107-0

12. Lipman, S.A., Reckers-Droog, V.T.: Comparing heuristic valuation processes between health state valuation from child and adult perspectives. Eur. J. Health Econ. 25, 1345–1360 (2024). doi:10.1007/s10198-023-01668-6

13. Attema, A.E., Lang, Z., Lipman, S.A.: Can independently elicited Adult- and Child-Perspective Health-State utilities explain priority setting? Value Health 26(11), 1645–1654 (2023). doi:10.1016/j.jval.2023.08.002

14. Hoogenboom, A.F.H., Lipman, S.A.: Loss aversion in EQ-5D-Y-3L: Does it explain differences in willingness to trade-off life years in adults and children? Eur. J. Health Econ., (2025). doi:10.1007/s10198-025-01775-6

15. Lang, Z., Attema, A.E., Lipman, S.A.: The effect of duration and time preference on the gap between adult and child health state valuations in time trade-off. Eur. J. Health Econ. 25(4), 601–613 (2024). doi:10.1007/s10198-023-01612-8

16. Lipman, S.A., et al.: Time and lexicographic preferences in the valuation of EQ-5D-Y with time trade-off methodology. Eur. J. Health Econ. 24(2), 293–305 (2023). doi:10.1007/s10198-022-01466-6

17. Kreimeier, S., et al.: Valuation of EuroQol Five-Dimensional Questionnaire, youth version (EQ-5D-Y) and EuroQol Five-Dimensional Questionnaire, Three-Level version (EQ-5D-3L) health states: The impact of wording and perspective. Value Health 21(11), 1291–1298 (2018). doi:10.1016/j.jval.2018.05.002

18. Lipman, S.A., et al.: In a child’s shoes: Composite time Trade-Off valuations for EQ-5D-Y-3L with different proxy perspectives. Pharmacoeconomics 40(Suppl 2), 181–192 (2022). doi:10.1007/s40273-022-01202-1

19. Roudijk, B., Donders, A.R.T., Stalmeier, P.F.M.: Cultural values: Can they explain differences in health utilities between countries? Medical Decision Making 39(5), 605–616 (2019). doi:10.1177/0272989X19841587

20. Devlin, N., Roudijk, B., Ludwig, K.: Value Sets for EQ-5D-5L: A Compendium, Comparative Review & User Guide. Springer (2022)

21. Sajjad, A., et al.: In search of a ‘pan-European value set’; application for EQ-5D-3L. BMC Med. Res. Methodol. 23(1), 13 (2023). doi:10.1186/s12874-022-01830-3

22. Norman, R., et al.: International comparisons in valuing EQ-5D health states: A review and analysis. Value Health 12(8), 1194–1200 (2009). doi:10.1111/j.1524-4733.2009.00581.x

23. De Silva, A., et al.: How do Health State Values Differ When Respondents Consider Adults Versus Children Living in Those States? A Systematic Review. Pharmacoeconomics, 43(7), 723–740 (2025). doi:10.1007/s40273-025-01493-0

24. Belügyminisztérium: Egészségügyi szakmai irányelve Az egészség gazdaságtani elemzések készítéséhez és értékeléséhez (in english: Health professional guideline for the Preparation and evaluation of health economic analyses). Egészségügyi Közlöny. 75(9), 1250–1275 (2025)

25. Rencz, F., et al.: Value set for the EQ-5D-Y-3L in Hungary. Pharmacoeconomics 40(Suppl 2), 205–215 (2022). doi:10.1007/s40273-022-01190-2

26. Rencz, F., Janssen, M.F.: Time perspective profile and self-reported health on the EQ-5D. Qual. Life Res. 33(1), 73–85 (2024). doi:10.1007/s11136-023-03509-8

27. Golicki, D., Młyńczak, K.: Measurement properties of the EQ-5D-Y: A systematic review. Value Health 25(11), 1910–1921 (2022). doi:10.1016/j.jval.2022.05.013

28. Rencz, F., et al.: Parallel valuation of the EQ-5D-3L and EQ-5D-5L by time Trade-Off in Hungary. Value Health 23(9), 1235–1245 (2020). doi:10.1016/j.jval.2020.03.019

29. Lang, Z., et al.: Is Episodic Future Thinking Effective in Mitigating the Influence of time Preference in time trade-off? The European Journal of Health Economics (2025). doi:10.1007/s10198-025-01812-4

30. Bíró, A., Prinz, D.: Healthcare spending inequality: Evidence from Hungarian administrative data. Health Policy 124(3), 282–290 (2020). doi:10.1016/j.healthpol.2020.01.006

31. Bíró, A., et al.: Life expectancy inequalities in Hungary over 25 years: The role of avoidable deaths. Population Studies 75(3), 443–455 (2021). doi:10.1080/00324728.2021.1877332

32. Kovacs, N., et al.: Comparative analysis of health status and health service utilization patterns among rural and urban elderly populations in hungary: A study on the challenges of unhealthy aging. Geroscience. 46(2), 2017–2031 (2024). doi:10.1007/s11357-023-00926-y

33. Rehm, R.S., et al.: Parent and youth priorities during the transition to adulthood for youth with special health care needs and developmental disability. ANS Adv. Nurs. Sci. 35(3), E57–72 (2012). doi:10.1097/ANS.0b013e3182626180

34. Powell, P.A., et al.: Who should value children’s health and how? An international Delphi study. Soc. Sci. Med. 355, 117127 (2024). doi:10.1016/j.socscimed.2024.117127

35. Augestad, L.A., et al.: Learning effects in time trade-off based valuation of EQ-5D health States. Value Health 15(2), 340–345 (2012). doi:10.1016/j.jval.2011.10.010

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 8.77 MB)

</div>

### Data Availability Statement

The data used in this study are available from FR upon reasonable request.

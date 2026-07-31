---
project_id: "304-PHD"
work_id: "doi:10.1007/s40271-024-00708-4"
doi: "10.1007/s40271-024-00708-4"
pmid: "39031285"
pmcid: "PMC11461645"
title: "The Performance of Kaizen Tasks Across Three Online Discrete Choice Experiment Surveys: An Evidence Synthesis"
journal: "The Patient"
publication_date: "2024-07-20"
volume: "17"
issue: "6"
authors:
  - name: "Benjamin Matthew Craig"
    affiliation_ids:
      - "Aff1"
  - name: "Maksat Jumamyradov"
    affiliation_ids:
      - "Aff1"
  - name: "Oliver Rivero-Arias"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
affiliations:
  - id: "Aff1"
    name: "Department of Economics, University of South Florida, 4202 E. Fowler Avenue, Tampa, FL CMC206A33620 USA"
  - id: "Aff2"
    name: "National Perinatal Epidemiology Unit, Nuffield Department of Population Health, University of Oxford, Oxford, UK"
  - id: "Aff3"
    name: "Health Economics Research Centre, Nuffield Department of Population Health, University of Oxford, Oxford, UK"
licence: "cc-by-nc"
source_file: "input/projects/304-PHD/papers/doi_10.1007_s40271-024-00708-4.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11461645/fullTextXML"
source_method: "epmc_xml"
source_sha256: "012ed970044d1a6ebd382dca9671722067f86c0e8cacc3cf605058a166509c3a"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The Performance of Kaizen Tasks Across Three Online Discrete Choice Experiment Surveys: An Evidence Synthesis

## Abstract

### Background

Kaizen is a Japanese term for continuous improvement (kai ~ change, zen ~ good). In a kaizen task, a respondent makes sequential choices to improve an object’s profile, revealing a preference path. Including kaizen tasks in a discrete choice experiment has the advantage of collecting greater preference evidence than pick-one tasks, such as paired comparisons.

### Objective and Methods

So far, three online discrete choice experiments have included kaizen tasks: the 2020 US COVID-19 vaccination (CVP) study, the 2021 UK Children’s Surgery Outcome Reporting (CSOR) study, and the 2023 US EQ-5D-Y-3L valuation (Y-3L) study. In this evidence synthesis, we describe the performance of the kaizen tasks in terms of response behaviors, conditional logit and Zermelo–Bradley–Terry (ZBT) estimates, and their standard errors in each of the surveys.

### Results

Comparing the CVP and Y-3L, including hold-outs (i.e., attributes shared by all alternatives) seems to reduce positional behavior by half. The CVP tasks excluded multi-level improvements; therefore, we could not estimate logit main effects directly. In the CSOR, only 12 of the 21 logit estimates are significantly positive (*p* \< 0.05), possibly due to the fixed attribute order. All Y-3L estimates are significantly positive, and their predictions are highly correlated (Pearson: logit 0.802, ZBT 0.882) and strongly agree (Lin: logit 0.744, ZBT 0.852) with the paired-comparison probabilities.

### Conclusions

These discrete choice experiments offer important lessons for future studies: (1) include warm-up tasks, hold-outs, and multi-level improvements; (2) randomize the attribute order (i.e., up-down) at the respondent level; and (3) recruit smaller samples of respondents than traditional discrete choice experiments with only pick-one tasks.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40271-024-00708-4.

Accepted 2024 Jul 4; Issue date 2024.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| Iteratively improving a single profile is easier for respondents and elicits more preference evidence than pick-one tasks, such as paired comparisons. |
| Kaizen evidence has strong predictive validity (i.e., predicts paired-comparison probabilities). |
| Due to its small-sample properties, kaizen discrete choice experiments are particularly well suited for large descriptive systems or when targeting populations that are difficult to recruit (e.g., patients with rare conditions) or composed of distinct classes (e.g., various groups involved). |

</div>

## Introduction

A discrete choice experiment (DCE) is a type of behavioral experiment in which choice sets (i.e., stimuli) are randomly assigned to subjects so that scientists can observe, capture, and record subject behaviors and test hypotheses, typically causal relationships between object attributes and behaviors (i.e., attribute importance). Although DCEs may be conducted in a variety of fields (e.g., audiology), economists incorporate DCEs into their surveys to elicit stated preferences on objects (i.e., DCE surveys). For example, a respondent may complete a series of paired-comparison tasks. In these pick-one tasks, the respondent chooses one of two alternatives (A or B), which implies an inequality in the decisional utility between the objects (i.e., A \> B).

A key methodological challenge in stated preference research is how to elicit more preference evidence with fewer respondents, allowing for smaller samples. More preference evidence per respondent also implies greater precision to identify preference heterogeneity. In this paper, we examine evidence from three DCE surveys with kaizen tasks to characterize their performance. Furthermore, we demonstrate the predictive validity of kaizen tasks relative to pick-one tasks (e.g., paired comparisons) and simulate the effects of smaller sample sizes on standard errors (SEs). The paper concludes with lessons learned from these initial studies and builds a foundation for those interested in future DCE surveys with kaizen tasks.

## What is a Kaizen Task?

In 2021, Craig and colleagues introduced kaizen tasks as a novel approach to preference elicitation, where respondents make sequential choices to improve the profile of a single object. \[1\] Kaizen is a Japanese term for continuous improvement (kai ~ change, zen ~ good). Each task elicits the discrete evolution of an object’s profile following an adaptive process of improvement, revealing a preference path. The evidence from their feasibility study demonstrated how a DCE with kaizen tasks can produce an EQ-5D-5L value set on a quality-adjusted life year scale with just a few interviews (20 respondents, 16 kaizen tasks each).

To better understand the potential of kaizen tasks, imagine a set of objects described using five three-level attributes (from the best \[11111\] to worst \[33333\] profile, such as the EQ-5D-Y-3L descriptive system). Each kaizen task will capture the preference path of a single object from an origin profile toward a destination profile (origin-destination pair).

Figure <a href="#Fig1" data-ref-type="fig">1</a> shows an example of a kaizen task, specifically the warm-up task from the 2023 US EQ-5D-Y-3L valuation study (origin-destination pair: 33331, 11111). Figure <a href="#Fig2" data-ref-type="fig">2</a> interprets the task from the respondent and researcher perspectives. From the respondent’s perspective, they are shown an initial profile (33331) and asked to improve this object sequentially until all potential improvements are exhausted (11111). In this task, there are four possible improvements (i.e., gains in an attribute by one or more levels) and the respondent picks 1 of 4, 1 of 3, and 1 of 2, watching the object’s profile evolve discretely from the origin to the destination profile (top portion of Fig. <a href="#Fig2" data-ref-type="fig">2</a>). The preference path in Fig. <a href="#Fig2" data-ref-type="fig">2</a> (shown in red) is just one of the 24 potential paths (4 × 3 × 2) from the origin to the destination.

<figure id="Fig1">
<p><img src="40271_2024_708_Fig1_HTML.jpg" id="MO1" /></p>
<p><img src="40271_2024_708_Fig1_HTML.gif" /></p>
<figcaption>Example of a kaizen task*. *This is the warm-up task for the 2023 U.S. EQ-5D-Y-3L valuation study using origin profile (33331) and the destination profile (11111). After selecting each improvement, the profile adapts, becoming more similar to the destination profile. Respondents who wish to change their selections may click the “Clear” button at any time and return to the origin profile.</figcaption>
</figure>

<figure id="Fig2">
<p><img src="40271_2024_708_Fig2_HTML.jpg" id="MO2" /></p>
<p><img src="40271_2024_708_Fig2_HTML.gif" /></p>
<figcaption>Interpretation of a preference path by perspective</figcaption>
</figure>

A key assumption of any kaizen analysis is that each preference path implies three choices. From the researcher’s perspective, the initial choice set includes all profiles with one improvement (i.e., 4 choose 1), the second set includes all profiles with two improvements (4 choose 2), and the third set includes all profiles with three improvements (4 choose 3). In practice, researchers can apply well-known methods in Health Preference Research (HPR) to design DCE with kaizen tasks (e.g., d-efficiency) and analyze kaizen evidence (e.g., latent-class analysis).

For reference, Fig. <a href="#Fig2" data-ref-type="fig">2</a> also shows the 14 choice probabilities taken from the 2023 U.S. EQ-5D-Y-3L valuation study. By construction, a kaizen task elicits more preference evidence than a paired comparison (e.g., 14 probabilities vs 2 probabilities), which is advantageous empirically; however, kaizen tasks were originally developed to reduce the respondent burden of preference elicitation.

## Where Did the Kaizen Task Come From?

From 2011 to 2015, Craig, Hartman and colleagues conducted a 5-year study funded by the US National Cancer Institute (5R01CA160104; principal investigator: Craig) to assess the value of PROMIS<sup>®</sup>-29 outcomes from societal and cancer survivor perspectives \[2\]. During their DCE surveys, respondents often expressed their displeasure with paired comparisons, having to choose between health outcomes directly. Listening to the patient perspective, the study team conducted an innovative pilot study asking patients in the chemotherapy clinic to report their symptoms and rank their preferred relief. This work was inspired by Jeff Sloan’s Beacon system \[3, 4\] and past ranking studies published by the study team \[5–8\]. The patients reported that ranking the relief of health problems was much less burdensome than paired comparisons.

Insights from patients revealed potential improvements in the process of preference elicitation. Instead of choosing between outcomes directly, patients and other decision makers in involved groups would rather focus on the relief of health problems. The kaizen task was originally presented to colleagues within the International Academy of Health Preference Research and the EuroQol Group. This line of research led to the original feasibility study \[1\] and the first three DCE surveys with kaizen tasks also influenced other innovative methods in HPR. \[9–13\]

## Methods

### Secondary Datasets

As of December 2023, three large DCE surveys adapted the kaizen task for online preference elicitation alongside pick-one tasks: the 2020 US COVID-19 vaccination study (CVP), the 2021 UK Children’s Surgery Outcome Reporting study (CSOR), and the 2023 US EQ-5D-Y-3L valuation study (Y-3L) \[9–13\]. Each study recruited respondents from the general population using a marketing panel (i.e., Dynata, Toluna) as well as other sources (i.e., Facebook, Amazon Mechanical Turk, banner ads). For simplicity, this synthesis combines the preference evidence from the panel respondents of these three DCE surveys.

The CSOR and Y-3L descriptive systems included only ordinal attributes (Table <a href="#Tab1" data-ref-type="table">1</a>); however, the descriptive system of the CVP study included three ordinal attributes and two nominal attributes (i.e., vaccination setting and proof of vaccination). In a kaizen task, each improvement in the initial profile must be a shift toward a preferred level. Therefore, the CVP instrument asked respondents about their preferences between the levels of the nominal attributes (e.g., community vs medical setting) and adapted the kaizen task to match these preferences. For this evidence synthesis, we restricted the CVP sample to exclude those respondents who preferred to be vaccinated in a community setting over the medical setting or did not want a vaccination card. Within this CVP subsample, all respondents had the same improvements in their kaizen tasks, similar to the CSOR and Y-3L studies. In addition, we excluded 230 CSOR respondents that were excluded from the original study.

<div id="Tab1" class="table-wrap">

<div class="caption">

Three DCE surveys with kaizen tasks

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">DCE survey</th>
<th style="text-align: left;">2020 US COVID-19 vaccination study (CVP)</th>
<th style="text-align: left;">2021 UK Children’s Surgery Outcome Reporting study (CSOR)</th>
<th style="text-align: left;">2023 US EQ-5D-Y-3L valuation study (Y-3L)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Target population</td>
<td style="text-align: left;">749 US adults were assigned to one of 15 blocks and 652 (87%) finished the 3 kaizen tasks (<em>N</em> = 652, <em>T</em> = 3) [<span class="citation" data-cites="CR9">9</span>, <span class="citation" data-cites="CR10">10</span>]</td>
<td style="text-align: left;">1357 UK adults were assigned to one of 15 blocks and 1026 (69%) finished the 3 kaizen tasks. An additional 230 respondents were excluded from the primary analysis (<em>N</em> = 807, <em>T</em> = 3) [<span class="citation" data-cites="CR12">12</span>, <span class="citation" data-cites="CR13">13</span>]</td>
<td style="text-align: left;">727 US adults were assigned to one of 4 blocks and 631 (87%) finished the 10 kaizen tasks (<em>N</em> = 631, <em>T</em> = 10) [<span class="citation" data-cites="CR11">11</span>]</td>
</tr>
<tr>
<td style="text-align: left;">Descriptive system</td>
<td style="text-align: left;">4 two-level and 1 four-level attributes in random order</td>
<td style="text-align: left;">5 four-level, 1 three-level, and 1 five-level attributes in fixed order</td>
<td style="text-align: left;">5 three-level attributes in random order</td>
</tr>
<tr>
<td style="text-align: left;">Experimental design<sup>a</sup></td>
<td style="text-align: left;">Full factorial; no hold-outs; single-level improvements</td>
<td style="text-align: left;">D-efficient; 3 hold-outs; multi-level improvements</td>
<td style="text-align: left;"><p>D-efficient; 1 hold-out;</p>
<p>multi-level improvements</p></td>
</tr>
<tr>
<td style="text-align: left;">Number of possible paths</td>
<td style="text-align: left;">60 possible paths (5×4×3)</td>
<td style="text-align: left;">24 possible paths (4×3×2)</td>
<td style="text-align: left;">24 possible paths (4×3×2)</td>
</tr>
</tbody>
</table>

*DCE* discrete choice experiment

<sup>a</sup>A hold-out is an attribute that is at the same level for all alternatives in a choice set. Including hold-outs in a kaizen task implies that one or more attributes cannot be improved

</div>

In all three studies, respondents completed an online DCE survey using the same format and software (LimeSurvey) \[9–13\]. The surveys had a component with pick-one tasks and another with kaizen tasks, each starting with a warm-up task. Within each component, the order of the tasks was randomized. In each kaizen task, respondents selected their first, second, and third improvements to a single profile, revealing a preference path.

The key differences between the design of the kaizen tasks in the three aforementioned DCE surveys are (1) the up-down randomization of attribute positions (i.e., attribute order); (2) the number of hold-outs (i.e., attributes shared by all alternatives in a choice set) in the experimental design; and (3) the use of single-level and multi-level improvements. Further details on each study can be found in their primary publications \[9–13\]. This evidence synthesis describes the performance of kaizen tasks in online DCE surveys with the general population.

### Descriptive Analyses

To aid future studies, we compared the response behavior between kaizen and pick-one tasks in their respective surveys. More specifically, we examined page times using Mood’s median test and the use of information buttons (i.e., pop-ups) and reset buttons (i.e., changed responses) by task and task order (chi-square tests).

In DCEs, some respondents may ignore the profiles entirely and implement a mental shortcut or heuristic to simplify task completion (e.g., always selecting the option closest to the top of the screen). Positional behavior occurs when an attribute’s position influences respondent behavior. In the CVP and Y-3L studies, the attribute order was randomized, so we ran chi-square tests to assess whether any vertical response patterns (e.g., selecting the first, second, and third improvements from the top) are more frequent than random. The CSOR attribute order was fixed, which confounds the interpretation of positional behavior and attribute importance.

### Primary Analyses

Like with the original study, we estimated main effects using conditional logit and Zermelo–Bradley–Terry (ZBT) models for each study. The CVP experimental design excluded multi-level improvements; therefore, its logit estimates represent the differences in the main effects, not the main effects themselves (see Electronic Supplementary Material \[ESM\]) \[9, 10\]. Compared with the logit estimates, the ZBT main-effect estimates are non-negative and do not rely on multi-level effects and the additivity assumption to identify all main effects \[1, 14–16\].

Regardless of specification, each main-effect estimate represents the causal relationship between a single-level change of an attribute (e.g., shift from Level 3 to Level 2) and the likelihood of choosing an object’s profile. Logit main-effect estimates reflect the difference in log-odds of choosing objects with and without the single-level improvement. Zermelo–Bradley–Terry estimates represent the difference in the odds of choosing objects with and without the single-level improvement relative to the difference in the odds of choosing objects with and without all improvements (i.e., ZBT main effects sum to 1 by construction).

For all main effect estimates, we calculated the $`\text{SEs}`$ and 95% confidence intervals and tested whether each is non-negative using bootstrap techniques (with replacement, clustering at the respondent level, stratification by block, and 1000 iterations) \[17\]. We also calculated the effects of reducing the sample size (*n* \< *N*) on the Y-3L main-effect SEs ($`\text{SE}_{\text{n}}`$).

The ESM describes the econometric analysis of kaizen evidence in more detail. Specifically, it evaluates the additivity assumption underlying the main-effect specification of the CSOR and Y-3L conditional logit models (i.e., the effect of a multi-level improvement on log-odds equals the sum of its main effects). The ESM describes the econometric analysis of paired-comparison evidence as well as the association between its estimates and their kaizen counterparts in greater detail.

## Results

### Response Behaviors

In the CVP, CSOR, and Y-3L studies, the median and interquartile range (IQR) in seconds for each kaizen task (excluding the warm-up) was 8.77 (IQR 5.78–14.07), 18.82 (IQR 11.17–29.84), and 12.48 (IQR 8.03–20.13), respectively. For reference, the median times for the pick-one tasks (excluding the warm-up) was CVP 8.74 (IQR 4.75–15.43), CSOR 13.62 (IQR 7.00–22.97), and Y-3L 10.79 (IQR 5.72–18.36). Overall, kaizen tasks take up to 5 seconds more to complete than pick-one tasks; therefore, switching a DCE from pick-one to kaizen tasks may cause a modest increase in the median survey duration (less than 1 minute).

In the CVP, CSOR, and Y-3L studies, the median page time for the warm-up task is higher than later tasks (*p* \< 0.001), and median times decrease in subsequent task (*p* \< 0.001). Like kaizen page times, other response behaviors differ greatly between the warm-up and subsequent kaizen tasks. Respondents used information buttons more frequently during the warm-up task than during the subsequent tasks (9.2% vs 1.1%, 4.2% vs 0.4%, 5.6% vs 0.5%, *p* \< 0.001). Likewise, respondents used the reset button more frequently during the warm-up task than during the subsequent tasks (28.3% vs 6.0%, 28.0% vs 11.6%, 19.9% vs 5.6%, *p* \< 0.001). Like with the pick-one tasks, this evidence reinforces the inclusion of a warm-up task prior to the kaizen tasks.

Unlike the CSOR study, the CVP and Y-3L studies randomized the attribute order (i.e., up-down); however, the frequency of vertical response patterns seems to depend on the presence of hold-outs. The CVP experimental design did not include hold-outs, and the frequency of each CVP response pattern should be 1.7% (i.e., 1 in 60); however, the frequency of each vertical response pattern exceeded this threshold (Student’s t-test, *p* \< 0.001): 11.3% (1st\|2nd\|3rd), 4.6% (3rd\|4th\|5th), 6.8% (5th\|4th\|3rd), 2.5% (4th\|3rd\|2nd), and 3.0% (3rd\|2nd\|1st). The Y-3L experimental design included one hold-out, and the frequency of each Y-3L response pattern should be 4.2% (1 in 24); however, the frequency of three of its four vertical response patterns exceeded this threshold (Student’s *t* test, *p* \< 0.001): 6.8% (1st\|2nd\|3rd), 5.3% (2nd\|3rd\|4th), and 4.5% (3rd\|2nd\|1st). Comparing the positional behaviors of the CVP and Y-3L studies, we infer that including a single hold-out may reduce the frequency of vertical response patterns by about half (e.g., 1st\|2nd\|3rd occurred 11.3% in CVP and 6.8% in Y-3L), enhancing the precision of a kaizen analysis even when the attribute order is randomized.

### Main Effects

Tables <a href="#Tab2" data-ref-type="table">2</a>, <a href="#Tab3" data-ref-type="table">3</a>, <a href="#Tab4" data-ref-type="table">4</a> show the main-effect estimates under the conditional logit and ZBT models of the CVP, CSOR, and Y-3L studies, respectively. Among the main-effect estimates, all Y-3L logit estimates and all ZBT estimates are positive and significant (*p* \< 0.05); however, only 12 of the 21 CSOR logit estimates are positive and significant. In each study, the logit and ZBT estimates are highly correlated (Pearson: 0.959 for CVP, 0.832 for CSOR, 0.959 for Y-3L). Like the original study, Fig. <a href="#Fig3" data-ref-type="fig">3</a> illustrates the log-linear relationship between the logit and ZBT estimates.

<div id="Tab2" class="table-wrap">

<div class="caption">

Main effects from the 2020 US COVID-19 vaccination study (CVP) kaizen analysis

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Attributes</th>
<th colspan="2" style="text-align: left;">Conditional logit</th>
<th colspan="2" style="text-align: left;">ZBT</th>
</tr>
<tr>
<th style="text-align: left;">Change in ln(odds)<sup>a</sup> (95% CI)</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">% Change in odds<sup>b</sup><br />
(95% CI)</th>
<th style="text-align: left;"><em>P</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Proof of vaccination: no card vs card</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">NA</td>
<td style="text-align: center;">0.074 (0.061, 0.088)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Setting: community vs medical</td>
<td style="text-align: left;">0.025 (− 0.096, 0.149)</td>
<td style="text-align: left;">0.700</td>
<td style="text-align: center;">0.071 (0.057, 0.085)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Vaccine effectiveness: 50% vs 70%</td>
<td style="text-align: left;">1.288 (1.134, 1.443)</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: center;">0.334 (0.304, 0.364)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Duration of immunity: 3 vs 6 months</td>
<td style="text-align: left;">0.224 (0.088, 0.369)</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: center;">0.073 (0.059, 0.089)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Risk of severe side effects</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>Lowest risk: 1 in 1,000,000 vs</p>
<p>Very low risk: 1 in 100,000</p></td>
<td style="text-align: left;">0.466 (0.293, 0.645)</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: center;">0.119 (0.099, 0.141)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><p>Very low risk: 1 in 100,000 vs</p>
<p>Low risk: 1 in 10,000</p></td>
<td style="text-align: left;">0.693 (0.522, 0.869)</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: center;">0.160 (0.136, 0.183)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><p>Low risk: 1 in 10,000 vs</p>
<p>Moderate risk: 1 in 1000</p></td>
<td style="text-align: left;">0.780 (0.604, 0.952)</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: center;">0.170 (0.144, 0.195)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
</tbody>
</table>

*CI* confidence interval, *NA * Not applicable , *ZBT* Zermelo–Bradley–Terry

<sup>a</sup>Like in the original kaizen study, CVP included only single-level improvements in its experimental design; therefore, its logit estimates represent differences in main effects (i.e., main effects minus a referent effect \[proof of vaccination\]). For more details, see Appendix <a href="#MOESM2" data-ref-type="supplementary-material">2</a> of the ESM

<sup>b</sup>ZBT main-effect estimates are non-negative and sum to one by construction

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

Main effects from the 2021 UK Children’s Surgery Outcome Reporting study (CSOR) kaizen analysis

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Attributes</th>
<th colspan="2" style="text-align: left;">Conditional logit</th>
<th colspan="2" style="text-align: left;">ZBT</th>
</tr>
<tr>
<th style="text-align: left;">Change in ln(odds) (95% CI)</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">% Change in odds<br />
(95% CI)</th>
<th style="text-align: left;"><em>P</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>Number of planned major operations (PMaj)</em></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">PMaj1: one to no planned major operations</td>
<td style="text-align: center;">− 0.132 (− 0.350, 0.087)</td>
<td style="text-align: center;">0.224</td>
<td style="text-align: center;">0.022 (0.012, 0.034)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PMaj2: two to one planned major operation</td>
<td style="text-align: center;">0.241 (0.054, 0.422)</td>
<td style="text-align: center;">0.020</td>
<td style="text-align: center;">0.063 (0.048, 0.078)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PMaj3: six to two planned major operations</td>
<td style="text-align: center;">0.581 (0.412, 0.758)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.079 (0.064, 0.095)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Number of planned minor operations (PMin)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">PMin1: one to no planned minor operations</td>
<td style="text-align: center;">− 0.271 (− 0.447, − 0.112)</td>
<td style="text-align: center;">0.002</td>
<td style="text-align: center;">0.029 (0.021, 0.036)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PMin2: two to one planned minor operation</td>
<td style="text-align: center;">0.043 (− 0.126, 0.206)</td>
<td style="text-align: center;">0.596</td>
<td style="text-align: center;">0.024 (0.017, 0.032)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PMin3: six to two planned minor operations</td>
<td style="text-align: center;">0.350 (0.170, 0.516)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.045 (0.034, 0.057)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Number of emergency major operations (EMaj)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">EMaj1: one to no emergency major operations</td>
<td style="text-align: center;">0.371 (0.193, 0.542)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.071 (0.052, 0.091)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EMaj2: two to one emergency major operation</td>
<td style="text-align: center;">0.476 (0.334, 0.623)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.081 (0.065, 0.098)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EMaj3: six to two emergency major operations</td>
<td style="text-align: center;">0.815 (0.651, 0.967)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.140 (0.118, 0.163)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Number of emergency minor operations (EMin)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">EMin1: one to no emergency minor operations</td>
<td style="text-align: center;">−0.099 (−0.234, 0.040)</td>
<td style="text-align: center;">0.186</td>
<td style="text-align: center;">0.016 (0.010, 0.024)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EMin2: two to one emergency minor operation</td>
<td style="text-align: center;">0.270 (0.130, 0.410)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.048 (0.038, 0.058)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EMin3: six to two emergency minor operations</td>
<td style="text-align: center;">0.442 (0.284, 0.579)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.044 (0.030, 0.057)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Number of hospital-treated infections (HTI)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">HTI1: one to no hospital-treated infections</td>
<td style="text-align: center;">−0.171 (−0.323, −0.006)</td>
<td style="text-align: center;">0.036</td>
<td style="text-align: center;">0.017 (0.011, 0.024)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">HTI2: two to one hospital-treated infection</td>
<td style="text-align: center;">−0.028 (−0.197, 0.130)</td>
<td style="text-align: center;">0.746</td>
<td style="text-align: center;">0.020 (0.013, 0.028)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">HTI3: six to two hospital-treated infections</td>
<td style="text-align: center;">0.527 (0.378, 0.680)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.052 (0.039, 0.064)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Quality of life (QOL)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">QOL1: fair to good</td>
<td style="text-align: center;">0.154 (−0.038, 0.347)</td>
<td style="text-align: center;">0.114</td>
<td style="text-align: center;">0.066 (0.051, 0.085)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">QOL2: poor to fair</td>
<td style="text-align: center;">0.526 (0.361, 0.675)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.083 (0.069, 0.097)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Duration of survival (DOS)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">DOS1: 20 years to more than 20 years</td>
<td style="text-align: center;">− 0.369 (− 0.598, − 0.140)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.011 (0.006, 0.018)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">DOS2: 5 to 20 years</td>
<td style="text-align: center;">0.342 (0.098, 0.594)</td>
<td style="text-align: center;">0.012</td>
<td style="text-align: center;">0.037 (0.029, 0.047)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">DOS3: 1 to 5 years</td>
<td style="text-align: center;">− 0.301 (− 0.551, − 0.059)</td>
<td style="text-align: center;">0.020</td>
<td style="text-align: center;">0.022 (0.015, 0.030)</td>
<td style="text-align: center;">&lt;0.001</td>
</tr>
<tr>
<td style="text-align: left;">DOS4: 6 months to 1 year</td>
<td style="text-align: center;">0.284 (0.050, 0.560)</td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;">0.029 (0.019, 0.042)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
</tbody>
</table>

*CI* confidence interval, *ZBT* Zermelo–Bradley–Terry

</div>

<div id="Tab4" class="table-wrap">

<div class="caption">

Main effects from the 2023 US EQ-5D-Y-3L valuation study (Y-3L) kaizen analysis

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Attributes</th>
<th colspan="2" style="text-align: left;">Conditional logit</th>
<th colspan="2" style="text-align: left;">ZBT</th>
</tr>
<tr>
<th style="text-align: left;">Change in ln(odds) (95% CI)</th>
<th style="text-align: left;"><em>P</em> value</th>
<th style="text-align: left;">% Change in odds (95% CI)</th>
<th style="text-align: left;"><em>P</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>Mobility (MO; walking around)</em></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">MO1: some to no problems walking around</td>
<td style="text-align: center;">0.448 (0.339, 0.547)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.056 (0.046, 0.067)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO2: a lot to some problems walking around</td>
<td style="text-align: center;">0.711 (0.621, 0.818)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.087 (0.076, 0.099)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Looking after myself (SC)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">SC1: some to no problems taking a bath or shower by myself or getting dressed by myself</td>
<td style="text-align: center;">0.192 (0.106, 0.282)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.034 (0.027, 0.041)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC2: a lot to some problems taking a bath or shower by myself or getting dressed by myself</td>
<td style="text-align: center;">0.422 (0.341, 0.509)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.047 (0.039, 0.055)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Doing usual activities (UA)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">UA1: some to no problems doing my usual activities</td>
<td style="text-align: center;">0.281 (0.187, 0.376)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.045 (0.037, 0.054)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA2: a lot to some problems doing my usual activities</td>
<td style="text-align: center;">0.596 (0.499, 0.692)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.063 (0.053, 0.073)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Having pain or discomfort (PD)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">PD1: some to no pain or discomfort</td>
<td style="text-align: center;">1.263 (1.140, 1.392)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.221 (0.198, 0.245)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD2: a lot to some pain or discomfort</td>
<td style="text-align: center;">1.545 (1.408, 1.687)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.329 (0.298, 0.363)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>Feeling worried, sad, or unhappy (AD)</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">AD1: a bit to not worried, sad, or unhappy</td>
<td style="text-align: center;">0.122 (0.022, 0.231)</td>
<td style="text-align: center;">0.014</td>
<td style="text-align: center;">0.038 (0.031, 0.045)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD2: very to a bit worried, sad, or unhappy</td>
<td style="text-align: center;">0.654 (0.535, 0.774)</td>
<td style="text-align: center;">&lt; 0.001</td>
<td style="text-align: center;">0.080 (0.069, 0.092)</td>
<td style="text-align: center;">&lt; 0.001</td>
</tr>
</tbody>
</table>

*CI* confidence interval, *ZBT* Zermelo–Bradley–Terry

</div>

<figure id="Fig3">
<p><img src="40271_2024_708_Fig3_HTML.jpg" id="MO3" /></p>
<p><img src="40271_2024_708_Fig3_HTML.gif" /></p>
<figcaption>Main effects by models. *Each main effect is shown in their natural unit (logit: change in ln(odds); ZBT: % change in odds). The x-axis is shown on a base-10 log scale to better illustrate the log-linear relationship between estimates.</figcaption>
</figure>

In Table <a href="#Tab2" data-ref-type="table">2</a>, the logit estimates describe the differences between the CVP main effects and the effect of proof of vaccination, and the ZBT estimates describe the CVP main effects directly. Regardless of model, the most important attribute is the risk of severe side effects, but the largest main effect is vaccination effectiveness. The CVP results reinforce the need to include multi-level improvements in the experimental designs of kaizen tasks (ESM).

In Tables <a href="#Tab3" data-ref-type="table">3</a> and <a href="#Tab4" data-ref-type="table">4</a>, the logit and ZBT estimates describe the CSOR and Y-3L main effects, respectively. Regardless of model, the most important effect in CSOR is the number of emergency major operations (EMaj) and the largest effect occurs by reducing the number from six to two (EMaj3). The most important effect in the Y-3L is having pain or discomfort (PD), and the largest effect occurs by reducing from a lot to some pain or discomfort (PD2).

The CSOR and Y-3L secondary analyses in the ESM suggest that relaxing the additivity assumption of main effects (i.e., the effect of a multi-level improvement on log-odds equals the sum of single-level effects) did not change any of the logit estimates significantly (*p* \< 0.05). The Y-3L paired-comparison analysis in the ESM further shows that the Y-3L kaizen and paired-comparison estimates are highly correlated (Pearson: logit 0.885, ZBT 0.917), strongly agree (Lin: logit 0.741, ZBT 0.917), and have similar interpretations (ESM). Figure <a href="#Fig4" data-ref-type="fig">4</a> shows that kaizen predictions and paired-comparison probabilities are also highly correlated (Pearson: logit 0.802, ZBT 0.882) and strongly agree (Lin: logit 0.744, ZBT 0.852).

<figure id="Fig4">
<p><img src="40271_2024_708_Fig4_HTML.jpg" id="MO4" /></p>
<p><img src="40271_2024_708_Fig4_HTML.gif" /></p>
<figcaption>Y-3L paired-comparison probabilities and kaizen predictions by model. *Tables with all probabilities and predictions are in Electronic Supplementary Material 2</figcaption>
</figure>

### Standard Errors (SEs)

Based on the Y-3L kaizen evidence (*N* = 631, *T* = 10), the median logit $`\text{SE}`$ is 0.052 with a range from 0.044 to 0.074, and the median ZBT $`\text{SE}`$ is 0.005 with a range from 0.004 to 0.017. Based on the paired-comparison evidence (*N* = 631, *T* = 10), $`\text{SEs}`$ are larger (logit 0.057 with a range from 0.044 to 0.111; ZBT 0.009 with a range from 0.006 to 0.015).

Using bootstrap techniques, we simulated the Y-3L $`\text{SE}_{n}`$ for a range of smaller samples (*n* = 34 to 100 respondents), where each respondent completes 20 kaizen tasks (*T* = 2). Figure <a href="#Fig5" data-ref-type="fig">5</a> illustrates the effects of reducing the sample size on the Y-3L $`\text{SE}_{\text{n}}`$ under the logit and ZBT models. From the results, we infer that an EQ-5D-Y-3L valuation study with 60 respondents and 20 kaizen tasks (ESM) may be sufficient to achieve a median $`\text{SE}`$ (logit 0.100; ZBT 0.010), a prediction that may be confirmed in Wave 2 of the US EQ-5D-Y-3L valuation study (ongoing).

<figure id="Fig5">
<p><img src="40271_2024_708_Fig5_HTML.jpg" id="MO5" /></p>
<p><img src="40271_2024_708_Fig5_HTML.gif" /></p>
<figcaption>Y-3L standard errors and sample size by model*. *Tables with all SE are in Electronic Supplementary Material 3</figcaption>
</figure>

## Discussion

Like the Scarecrow, the Tin Man, and the Cowardly Lion in *The Wonderful Wizard of Oz*, \[18\] each of these three studies offers potential lessons for future researchers on how they might improve DCEs with kaizen tasks or similar tasks. The CVP experimental design did not include hold-outs or multi-level improvements. The lack of hold-outs in its experimental design may have contributed to its higher frequency of vertical behaviors compared with the Y-3L, and the lack of multi-level improvements impeded the estimation of logit main effects. The CSOR survey instrument did not randomize the order of its attributes at the respondent level, which may have contributed to its negative logit estimates compared with the CVP and Y-3L estimates. Although the Y-3L main-effect estimates are non-negative and demonstrate strong predictive validity, these results could have been achieved with a smaller study. Further confirmation of the Y-3L results may give future researchers the courage to recruit smaller sample sizes than traditional DCEs with only pick-one tasks.

In retrospect, these lessons may not surprise those experienced in health preference research. Nevertheless, they are crucial for future DCEs with kaizen tasks. In addition to allowing for smaller samples, kaizen tasks are particularly well suited for DCEs with larger descriptive systems (i.e., multiple attributes and levels), where comparing full profiles can induce excess respondent burden. For example, the EuroQol Group is currently developing descriptive systems with more than five attributes, such as the EuroQol Health and Wellbeing instrument (EQ-HWB), which has 25 five-level attributes (i.e., 100 main effects). Using a kaizen task, respondents may be presented with a single EQ-HWB profile (i.e., pivot) and asked to choose improvements sequentially. Based on the Y-3L results, a DCE with kaizen tasks would require fewer than 200 respondents to produce a standard EQ-HWB value set. However, DCEs with kaizen tasks may not be suitable for all applications. Based on the available evidence, we do not recommend kaizen tasks for DCEs with nominal attributes or interactions between attributes at this time.

Future DCEs may examine the performance of kaizen tasks in patients or populations that are difficult to recruit or as exploratory studies of alternative scenarios or descriptive systems. Researchers may also add innovations in task design, such as expanding the number of hold-outs or choices per task. Analysts may extend the logit and ZBT models and assess preference heterogeneity (e.g., latent class analyses), interactions in main effects, or heteroskedasticity. At present, the study team is developing hybrid models that merge paired-comparison and kaizen evidence and facilitate scaling, which may enhance the interpretation of the main-effect estimates. More importantly, the team is preparing a suite of open-source software to facilitate researchers interested in the design, collection, and analysis of kaizen evidence. \[19\]

## Conclusions

Overall, this evidence synthesis shows that a kaizen task may take a bit more time for respondents to complete, but it provides a useful alternative to pick-one tasks, particularly when the descriptive system is large or when targeting populations that are difficult to recruit (e.g., patients) or composed of distinct classes (e.g., various groups involved). Based on these findings, we recommend that kaizen DCEs (1) include warm-up tasks, multi-level improvements, and hold-outs; (2) randomize the attribute order at the respondent level; and (3) consider smaller sample sizes than traditional DCEs with only pick-one tasks. We hope that this paper encourages researchers to explore kaizen tasks or similar innovations in preference elicitation.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 56 KB)

</div>

<div class="caption">

Supplementary file2 (DOCX 68 KB)

</div>

<div class="caption">

Supplementary file3 (DOCX 43 KB)

</div>

## Acknowledgements

The authors thank the EuroQol Research Foundation for their support of Maksat Jumamyradov’s dissertation. We also thank John Bucknell and Michał Jakubczyk for their help during the development and conduct of the CSOR and Y-3L studies, respectively.

## Declarations

### Funding

The EuroQol Research Foundation funded the doctoral research of Maksat Jumamyradov under the project titled: Sequential relief of child health problems (304-PHD). The CSOR study is funded by the National Institute of Health Research (NIHR) Health and Social Care Delivery Research Programme (project reference NIHR 127844). The views expressed are those of the author(s) and not necessarily those of the NIHR or the Department of Health and Social Care.

### Conflicts of interest/competing interests

All authors have completed the ICMJE uniform disclosure form at <http://www.icmje.org/disclosure-of-interest/and> declare: no support from any organization for the submitted work; no financial relationships with any organizations that might have an interest in the submitted work in the previous 3 years; no other relationships or activities that could appear to have influenced the submitted work. Benjamin Craig is an Editorial Board Member of The Patient. He was not involved in the selection of peer reviewers for the manuscript nor any of the subsequent editorial decisions.

### Ethics approval

Not applicable.

### Consent to participate

Not applicable.

### Consent for publication

Not applicable.

### Availability of data and material

Data are available upon reasonable request.

### Code availability

The code generated used in the analysis of the study datasets is available from the corresponding author on reasonable request.

### Authors’ contributions

BMC, MJ, and ORA contributed the data for this secondary analysis. BMC and MJ conducted the analysis. All authors interpreted the results, wrote the final manuscript, and agreed to its published version.

## References

## References

1. Craig BM, Rand K, Hartman JD. Preference paths and their kaizen tasks for small samples. Patient. 2022;15:187–96. doi:10.1007/s40271-021-00541-z

2. Craig BM, Reeve BB, Brown PM, Cella D, Hays RD, Lipscomb J, et al. US valuation of health outcomes measured using the PROMIS-29. Value Health. 2014;17:846–53. doi:10.1016/j.jval.2014.09.005

3. Sloan JA, Halyard M, El Naqa I, Mayo C. Lessons from large-scale collection of patient-reported outcomes: implications for big data aggregation and analytics. Int J Radiat Oncol Biol Phys. 2016;95:922–9. doi:10.1016/j.ijrobp.2016.04.002

4. Warsame R, Cook J, Fruth B, Hubbard J, Croghan K, Price KAR, et al. A prospective, randomized trial of patient-reported outcome measures to drive management decisions in hematology and oncology. Contemp Clin Trials Commun. 2022;29: 100964. doi:10.1016/j.conctc.2022.100964

5. Craig BM, Ramachandran S. Relative risk of a shuffled deck: a generalizable logical consistency criterion for sample selection in health state valuation studies. Health Econ. 2006;15:835–48. doi:10.1002/hec.1108

6. Craig BM, Busschbach JJV, Salomon JA. Modeling ranking, time trade-off, and visual analog scale values for EQ-5D health states: a review and comparison of methods. Med Care. 2009;47:634–41. doi:10.1097/MLR.0b013e31819432ba

7. Craig BM, Busschbach JJV, Salomon JA. Keep it simple: ranking health states yields values similar to cardinal measurement approaches. J Clin Epidemiol. 2009;62:296–305. doi:10.1016/j.jclinepi.2008.07.002

8. Craig BM, Busschbach JJ. The episodic random utility model unifies time trade-off and discrete choice approaches in health state valuation. Popul Health Metr. 2009;7:3. doi:10.1186/1478-7954-7-3

9. Craig BM, de Bekker-Grob EW, González Sepúlveda JM, Greene WH. A guide to observable differences in stated preference evidence. Patient. 2022;15:329–39. doi:10.1007/s40271-021-00551-x

10. Craig BM. United States COVID-19 vaccination preferences (CVP): 2020 hindsight. Patient. 2021;14:309–18. doi:10.1007/s40271-021-00508-0

11. Jumamyradov M, Craig BM, Rivero-Arias O, Jakubczyk M. Child health valuation protocol for a discrete choice experiment comparing paired comparison and kaizen tasks and estimating US EQ-5D-Y-3L values on an experience scale. BMJ Open. 2023;13: e077256. doi:10.1136/bmjopen-2023-077256

12. Rivero-Arias O, Buckell J, Knight M, Craig BM, Ramakrishnan R, Kenny S, et al. Defining treatment success in children with surgical conditions. Arch Dis Child. 2024;109:377–86. doi:10.1136/archdischild-2023-326156

13. Rivero-Arias O, Buckell J, Allin B, Craig BM, Ayman G, Knight M. Using stated-preferences methods to develop a summary metric to determine successful treatment of children with a surgical condition: a study protocol. BMJ Open. 2022;12: e062833. doi:10.1136/bmjopen-2022-062833

14. Glickman ME. Introductory note to 1928 (= 1929). In: Zermelo E, Ebbinghaus H-D, Kanamori A, editors. Ernst Zermelo: collected works/Gesammelte Werke II: Volume II/Band II—calculus of variations, applied mathematics, and physics/Variationsrechnung, Angewandte Mathematik und Physik. Berlin: Springer; 2013.p. 616–71. 10.1007/978-3-540-70856-8_13.

15. Zermelo E. The calculations of the results of a tournament as a maximum problem in the calculus of probabilities. Math Z. 1928;29:436–60.

16. David HA. The method of paired comparisons. Number 12 of Griffin's Statistical Monographs and Courses, Hafner Publishing Company, New York, 1963.

17. Efron B, Tibshirani RJ. An introduction to the bootstrap (1st ed.). Chapman and Hall/CRC Press; 1994.

18. Baum LF (Frank L), Denslow WW (Wallace W). The wonderful wizard of Oz. Chicago (IL); New York (NY): G.M. Hill Co.; 1900. http://archive.org/details/wonderfulwizardo00baumiala. Accessed 1 Mar 2024.

19. R4HPR. https://r4hpr.org/. Accessed 1 Mar 2024.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 56 KB)

</div>

<div class="caption">

Supplementary file2 (DOCX 68 KB)

</div>

<div class="caption">

Supplementary file3 (DOCX 43 KB)

</div>

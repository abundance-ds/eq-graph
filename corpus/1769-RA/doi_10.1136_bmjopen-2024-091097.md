---
project_id: "1769-RA"
work_id: "doi:10.1136/bmjopen-2024-091097"
doi: "10.1136/bmjopen-2024-091097"
pmid: "39987002"
pmcid: "PMC11848668"
title: "Health valuation protocol for dual discrete choice experiment (dual-DCE) surveys to estimate the effects of different scenarios and attributes on main effects"
journal: "BMJ Open"
publication_date: "2025-02-22"
volume: "15"
issue: "2"
authors:
  - name: "Benjamin Matthew Craig"
    affiliation_ids:
      - "aff1"
affiliations:
  - id: "aff1"
    name: "University of South Florida, Tampa, Florida, USA"
licence: "cc-by-nc"
source_file: "input/projects/1769-RA/papers/doi_10.1136_bmjopen-2024-091097.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11848668/fullTextXML"
source_method: "epmc_xml"
source_sha256: "f126a2a21cd97088ba2325bbf416a3742bef422e8b4d2c5201a1080c8628889a"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Associated Data

## Abstract

### ABSTRACT

### Introduction

A typical health preference study conducts a single discrete choice experiment (DCE). For example, a health valuation study may elicit preferences on an individual’s health-related quality of life along five EQ-5D-5L attributes (Mobility, Self-care, Usual Activities, Pain/Discomfort, Anxiety/Depression). Using this protocol, researchers can conduct a dual-DCE survey (ie, with two different full-block DCEs completed sequentially). To demonstrate this protocol, we will conduct 12 dual-DCE surveys in two waves and estimate the effects of different scenarios and descriptive systems on main effects (ie, incremental differences in value between levels).

### Methods and analysis

Each of the two DCEs in a dual-DCE survey equates to a stand-alone health valuation study. To demonstrate this protocol, each is an EQ-5D-5L valuation study, including d-efficient blocks of 15 kaizen tasks and 5 paired comparisons. In wave 1 (six surveys, 1000 US adults each), the two DCEs will differ by scenario (1-year episodes ending in recovery or death or no duration/ending described). In wave 2 (six surveys, 200 US adults each), the two DCEs will include the same 5 EQ-5D-5L attributes but differ by the number of additional attributes related to cognition: none, one composite attribute (memory/concentration) and two component attributes (memory, concentration). For each DCE, we will estimate a conditional logit model and test for differences in value using cluster bootstrap techniques. We hypothesise that the values will differ by scenarios and systems. As secondary analyses, we assess the effects of sampling, scenario/system order and DCE order.

### Ethics and dissemination

The independent review board (IRB) at Advarra determined that this research project (Pro00080475; 11 July 2024) is exempt from IRB oversight based on the Department of Health and Human Services regulations found at 45 CFR 46.104(d)(2). Furthermore, the IRB determined that the project is not subject to requirements for continuing review. To disseminate our findings, we will prepare multiple manuscripts for publication in peer-reviewed journals and present highlights at scientific meetings, such as the EuroQol Plenary Meeting, International Academy of Health Preference Research and ISPOR.

**Keywords:** HEALTH ECONOMICS, Patient Reported Outcome Measures, Behaviour, Cognition, Patient Preference, Quality of Life

Received 2024 Jul 11; Accepted 2025 Feb 7; Collection date 2025.

<div class="caption">

###### STRENGTHS AND LIMITATIONS OF THIS STUDY

</div>

- Under this protocol, each survey respondent completes two online discrete choice experiments (DCEs) back-to-back (ie, dual-DCE surveys), eliminating sampling biases when comparing different scenarios and descriptive systems.

- The efficiency of kaizen tasks in gathering preference evidence allows each dual-DCE survey to produce two EQ-5D-5L value sets using a small sample of respondents (i.e., single block, N=200).

- Due to their greater accuracy and efficiency, dual-DCE surveys empower methodological innovation in health preference research.

- The protocol relies on online surveys using a marketing panel, which may not be generalisable to the US general population, particularly to those individuals who are less educated or do not participate in such surveys or panels.

- This article only provides the wave 1 survey instrument, experimental design and analysis plan because we will adapt wave 2 materials based on the wave 1 evidence.

## Introduction

In health preference research, a **discrete choice experiment** (DCE) is a scientific procedure carried out under controlled conditions. These experiments examine how subjects choose between health-related objects. For example, a **health valuation study** may elicit preferences on health-related quality of life (HRQoL) episodes and produce a value set.<sup>1</sup> Prior to preference elicitation, a survey instrument must fully describe the decision context and the descriptive framework of health-related objects to respondents in a manner that they understand.<sup>2</sup> We designed this protocol to test whether the decision context and descriptive framework affect the values individuals place on HRQoL episodes.

A **decision context** is the setting, role and scenario underlying the decision. This context is expressed to the respondent as background information prior to starting the DCE. For example, one DCE may elicit preferences on 1-year episodes ending in recovery and another on 10-year episodes ending in death. Researchers may introduce the decision context using instructions and confirmation checklists prior to starting the DCE. This background information assures that each respondent has a minimum understanding of the setting, role and scenario.<sup>3 4</sup>

A **descriptive framework** is the visual and verbal representation of objects within a decision context. The framework includes attribute labels, definitions and object profiles. A key component of any framework is its **descriptive system**. This system conveys the differences between the objects’ profiles using a multilevel system of attributes and pictograms. As shown in <a href="#T1" data-ref-type="table">table 1</a>, the EQ-5D-5L descriptive system has five ordinal attributes. This system describes HRQoL profiles using adjectival statements.<sup>5</sup> Expressing the best level of each domain as 1 and the worst level as 5, its 3125 profiles range from 11111 to 55555. For example, an episode with moderate problems on all five attributes has the HRQoL profile 33333. Researchers typically introduce the descriptive framework using definitions and hands-on exercises prior to starting the DCE. This introduction assures that all respondents understand how objects differ along specific qualities.

<div id="T1" class="table-wrap">

<div class="caption">

###### EQ-5D-5L descriptive system and additional attributes related to cognition

</div>

<table>
<thead>
<tr>
<th></th>
<th>Level 1</th>
<th>Level 2</th>
<th>Level 3</th>
<th>Level 4</th>
<th>Level 5</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">EQ-5D-5L descriptive system</td>
</tr>
<tr>
<td style="text-align: left;"> Mobility (MO)</td>
<td style="text-align: left;">No problems walking</td>
<td style="text-align: left;">Slight problems walking</td>
<td style="text-align: left;">Moderate problems walking</td>
<td style="text-align: left;">Severe problems walking</td>
<td style="text-align: left;">Unable to walk</td>
</tr>
<tr>
<td style="text-align: left;"> Self-care (SC)</td>
<td style="text-align: left;">No problems washing or dressing myself</td>
<td style="text-align: left;">Slight problems washing or dressing myself</td>
<td style="text-align: left;">Moderate problems washing or dressing myself</td>
<td style="text-align: left;">Severe problems washing or dressing myself</td>
<td style="text-align: left;">Unable to wash or dress myself</td>
</tr>
<tr>
<td style="text-align: left;"> Usual activities (UA)</td>
<td style="text-align: left;">No problems doing my usual activities</td>
<td style="text-align: left;">Slight problems doing my usual activities</td>
<td style="text-align: left;">Moderate problems doing my usual activities</td>
<td style="text-align: left;">Severe problems doing my usual activities</td>
<td style="text-align: left;">Unable to do my usual activities</td>
</tr>
<tr>
<td style="text-align: left;"> Pain/discomfort (PD)</td>
<td style="text-align: left;">No pain or discomfort</td>
<td style="text-align: left;">Slight pain or discomfort</td>
<td style="text-align: left;">Moderate pain or discomfort</td>
<td style="text-align: left;">Severe pain or discomfort</td>
<td style="text-align: left;">Extreme pain or discomfort</td>
</tr>
<tr>
<td style="text-align: left;"> Anxiety/depression (AD)</td>
<td style="text-align: left;">Not anxious or depressed</td>
<td style="text-align: left;">Slightly anxious or depressed</td>
<td style="text-align: left;">Moderately anxious or depressed</td>
<td style="text-align: left;">Severely anxious or depressed</td>
<td style="text-align: left;">Extremely anxious or depressed</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">One composite attribute related to cognition (ie, bolt-on)</td>
</tr>
<tr>
<td style="text-align: left;"> Memory/ concentration (MC)</td>
<td style="text-align: left;">No problems remembering things or concentrating</td>
<td style="text-align: left;">Slight problems remembering things or concentrating</td>
<td style="text-align: left;">Moderate problems remembering things or concentrating</td>
<td style="text-align: left;">Severe problems remembering things or concentrating</td>
<td style="text-align: left;">Extreme problems remembering things or concentrating</td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Two component attributes related to cognition (ie, deep-dive)</td>
</tr>
<tr>
<td style="text-align: left;"> Memory (ME)</td>
<td style="text-align: left;">No problems remembering things</td>
<td style="text-align: left;">Slight problems remembering things</td>
<td style="text-align: left;">Moderate problems remembering things</td>
<td style="text-align: left;">Severe problems remembering things</td>
<td style="text-align: left;">Extreme problems remembering things</td>
</tr>
<tr>
<td style="text-align: left;"> Concentration (CC)</td>
<td style="text-align: left;">No problems concentrating</td>
<td style="text-align: left;">Slight problems concentrating</td>
<td style="text-align: left;">Moderate problems concentrating</td>
<td style="text-align: left;">Severe problems concentrating</td>
<td style="text-align: left;">Extreme problems concentrating</td>
</tr>
</tbody>
</table>

© EuroQol Research Foundation. EQ-5D™ is a trade mark of the EuroQol Research Foundation. Reproduced by permission of EuroQol Research Foundation. Reproduction of is not allowed. For reproduction, use or modification of the EQ-5D (any version), please register your study by using the online EQ registration page: [www.euroqol.org](http://www.euroqol.org).

</div>

In health valuation, researchers conduct DCE to estimate how differences between objects’ profiles influence respondents’ choices (ie, choice defines value).<sup>6</sup> This protocol introduces the concept of a **dual-DCE survey**, where each respondent completes two DCEs sequentially. For example, the two DCEs may have different scenarios or descriptive systems. Under this protocol, researchers can conduct dual-DCE surveys to examine the effects of different scenarios or systems on **main effects** (ie, incremental differences in value between levels). If successful, dual-DCE surveys have the potential to greatly enhance the evaluation of DCE design in health valuation and other forms of health preference research.

### Aims

The overall objective of this protocol is to conduct dual-DCE surveys to estimate the effects of different scenarios and descriptive systems on main effects. Specifically, our aims are:

- To develop and implement dual-DCE surveys for health valuation.

- To examine the effects of different episode scenarios on the values of the US. general population.

- To examine the effects of additional attributes related to cognition on the values of the US general population.

Under this protocol, we will conduct 12 dual-DCE surveys in two waves. Each of the 24 DCE (12 surveys × 2 DCE) represents a stand-alone health preference study. The use of the dual-DCE design reduces biases due to differential sampling and allows the assessment of agreement between DCEs at the respondent level. We hypothesise that the value of each gain in HRQoL is non-negative (Aim 1) and that differences in scenarios/systems affect value (Aims 2 and 3). As a secondary analysis, we will also examine the effects of sampling, scenario/system order and DCE order on the primary findings.

A typical DCE includes so many tasks that it is not feasible for a single respondent to complete all tasks. Instead, the tasks are divided between respondents (ie, **split-block design**). However, the DCEs in this study will use **kaizen tasks** (see ‘Methods and analysis’), which collect greater preference evidence than pick-one tasks, such as paired comparisons.<sup>3 7 8</sup> Under this protocol, each respondent will complete all tasks of two DCEs (ie, full-block designs). Without kaizen tasks, such dual-DCE surveys would not be feasible.

## Methods and analysis

<a href="#F1" data-ref-type="fig">Figure 1</a> presents the different phases of this study. In this protocol, we describe the theory, decision context and descriptive framework; preference elicitation tasks; experimental design; survey instrument; data collection; and analysis and dissemination.

<figure id="F1">
<p><img src="bmjopen-15-2-g001.jpg" /></p>
<p><img src="bmjopen-15-2-g001.gif" /></p>
<figcaption>Phases of the study.</figcaption>
</figure>

We will conduct 12 dual-DCE surveys in two waves (<a href="#T1" data-ref-type="table">table 1</a>). Each DCE will be a stand-alone health preference study asking respondents to choose their own HRQoL episodes (1 year then recover, 1 year then die, 10 years then die and no duration/ending) described by the five attributes of the EQ-5D-5L descriptive system as well as up to two additional attributes related to cognition.

Further details on the wave 1 experimental design, survey instrument and analysis plan can be found in <a href="#SP1" data-ref-type="supplementary-material">onlinesupplemental appendix 1</a><a href="#SP3" data-ref-type="supplementary-material">3</a>, respectively. In <a href="#SP1" data-ref-type="supplementary-material">online supplemental appendix 1</a>, we provide screenshots from the wave 1 online survey instrument with references and detailed description of each page. In <a href="#SP2" data-ref-type="supplementary-material">online supplemental appendix 2</a>, we provide the experimental design, including set selection, blocking and subject design, as well as the settings and terminology implemented in the survey software (LimeSurvey). Finally in <a href="#SP3" data-ref-type="supplementary-material">online supplemental appendix 3</a>, we provide an analysis plan with a detailed list of tests that we perform for descriptive analysis, primary and secondary analyses. These materials are not provided for wave 2 because we will adapt its materials based on the wave 1 evidence.

### Patient and public involvement

Patients and/or the public were not involved in the design, or conduct, or reporting, or dissemination plans of this research.

### Theory, decision context and descriptive framework

#### Theory

Under the **random utility model (RUM**), each respondent selects the object that maximises their decisional utility. This theoretical foundation (see ‘Analysis plan’) was the basis for the original 2016 US EQ-5D-5L valuation study. In this study, 8222 US respondents completed a DCE survey with 20 paired comparisons.<sup>1</sup> We similarly assume that individuals will choose the HRQoL episodes that maximises their decisional utility given the episode scenario and additional attributes (ie, choice defines values).

### Decision context

In each DCE, the respondent’s role is a **decision-maker**. This implies rationality, complete and transitive preferences, non-satiation and perfect information. The setting is within the **general community**, rather than an institutional setting. Therefore, decisions are made autonomously, operating outside formal organisational structures or established institutions. In these DCEs, the scenario is a decision that affects their own HRQoL over an episode (lasting either 1 year or 10 years) with varying endings (either recovery or death). For reference, the scenario in the 2016 EQ-5D-5L valuation study was a decision between HRQoL episodes of varying durations, each ending in death.<sup>1</sup> To better assess the importance of the decision context, wave 1 surveys also include a DCE that does not describe episode duration or ending (ie, generic). This generic scenario mimics the EQ-VT protocol for the EQ-5D-5L valuation.<sup>9</sup>

A **referent** is a labelled object outside the descriptive system (eg, opt-out) whose value serves as a numeraire (ie, a measure of value). In health valuation, the value of the optimal profile is typically one and the value of the referent is zero. The values of all other object profiles may be expressed in proportion to the difference between these two value anchors (ie, a proportional scale).

Across the 12 surveys, the optimal object differs by DCE. In the wave 1 DCE, the optimal object is “no problems” (11111) under three different scenarios (<a href="#T2" data-ref-type="table">table 2</a>): either 1 year then recover (acute episode), 1 year then die (chronic episode) or no duration/ending (generic episode). In the wave 2 DCE, the optimal object is “no problems” under three different descriptive systems (either 11111, 111111 or 1111111) for 10 years then die (chronic episode). Likewise, the referent in the wave 1 DCEs is being “in a coma” under the same three scenarios; however, all wave 2 DCEs have the same referent (“dying immediately”). In summary, each DCE is on a different proportional scale, which complicates the comparisons of values.

<div id="T2" class="table-wrap">

<div class="caption">

###### Twelve dual-DCE surveys in the two waves (n=7200)<a href="#T2_FN1" data-ref-type="table-fn"><sup>*</sup></a>

</div>

| Wave 1 (six dual-DCE surveys; n=6000)First DCE\second DCE<a href="#T2_FN1" data-ref-type="table-fn"><sup>*</sup></a> | 1 year then recover | 1 year then die | No duration/ending | Sample size |
|----|----|----|----|----|
|  1 year then recover (acute) | – | 1.1 | 2.1 | 2000 |
|  1 year then die (chronic) | 1.2 | – | 3.1 | 2000 |
|  No duration/ending (generic) | 2.2 | 3.2 | – | 2000 |

| Wave 2 (six dual-DCE surveys; n=1200)First DCE\second DCE | EQ-5D-5L only | EQ-5D-5L and one composite | EQ-5D-5L and two components | Sample size |
|----|----|----|----|----|
|  EQ-5D-5L only | – | 4.1 | 5.1 | 400 |
|  EQ-5D-5L and one composite | 4.2 | – | 6.1 | 400 |
|  EQ-5D-5L and two components | 5.2 | 6.2 | – | 400 |

Each number (1.1 to 6.2) represents a dual-DCE survey. In wave 1, all DCEs have the same attributes (EQ-5D-5L only), but the scenarios vary. In wave 2, all DCE have the same scenario (10 years then die), but the descriptive systems vary. Regardless, each block of each dual -DCE survey has 200 respondents and each DCE represents a stand-alone EQ-5D-5L valuation study.

DCEdiscrete choice experiment

</div>

In each DCE, the referent is incorporated into the paired comparison tasks. The wave 1 paired comparisons ask respondents to choose between an HRQoL episode and no experience (ie, being in a coma). These choices allow valuation on an **experience scale**, where a higher (lower) value implies a more (less) preferred experience.<sup>10</sup> The wave 2 paired comparisons ask respondents to choose between an HRQoL episode and “dying immediately”.<sup>1</sup> These preferences between life extensions and gains in HRQoL allow valuation on a **quality-adjusted life year (QALY) scale**.

Carefully specifying the scale is critically important in health valuation studies because some referents are considered morally questionable. The Inflation Reduction Act of 2022, under section 1194€(2), states, “The Secretary shall not use evidence from comparative clinical effectiveness research in a manner that treats extending the life of an elderly, disabled, or terminally ill individual as of lower value than extending the life of an individual who is younger, nondisabled, or not terminally ill.” For Medicare price negotiations, using a shorter lifespan as a referent is prohibited (ie, QALY scale), but using an episode with worse HRQoL as referent is allowed (experience scale). In the health literature more broadly, there are many examples of how a flawed referent can promote systemic biases that favour some groups (eg, male norm) and disfavour others (race-based medicine).<sup>11 12</sup>

### Descriptive framework

For each task (<a href="#F2" data-ref-type="fig">figures2</a><a href="#F3" data-ref-type="fig">3</a>), the descriptive framework places a label over each object and provides a definition for each attribute (see information buttons). For most objects, the **label** is “Starting today, {1 year, 10 years} {with health problems, in a coma} then {die, recover}”. For the generic-scenario DCE in wave 1, the object labels are either “Health problems” or “Coma”. In wave 2, the referent label is “dying immediately”. An underline is used to emphasise the difference between the object labels. For reference, the label in the 2016 study was “Starting today, {X days, weeks, months, years} with health problems then die ({X days, weeks, months, years} from today)”.

<figure id="F2">
<p><img src="bmjopen-15-2-g002.jpg" /></p>
<p><img src="bmjopen-15-2-g002.gif" /></p>
<figcaption>Warm-up kaizen task.</figcaption>
</figure>

<figure id="F3">
<p><img src="bmjopen-15-2-g003.jpg" /></p>
<p><img src="bmjopen-15-2-g003.gif" /></p>
<figcaption>Warm-up paired comparison task.</figcaption>
</figure>

Apart from the object labels and attribute definitions, the EQ-5D-5L attribute levels are described using **adjectival statements** (<a href="#T1" data-ref-type="table">table 1</a>). With five five-level attributes, the wave 1 descriptive systems have 20 **main effects** (ie, four incremental differences in attribute levels across five ordinal attributes). In wave 2, the descriptive system expands to include additional attributes. A **composite attribute** is an attribute that is added to an existing descriptive system (ie, bolt-on) to extend its breadth and a **component attribute** extends the depth of a descriptive system along an existing domain (ie, deep-dive). These additional attributes were adapted from prior psychometric studies, creating three nested systems related to cognition: no additional attributes, one additional attribute and two additional attributes.<sup>13</sup> With five levels per attribute, these nested systems have 20, 24 and 28 main effects, respectively. However, the two component attributes may be **complements** (ie, overlap); therefore, we will stratify the memory indicators by concentration level, increasing the number of main effects from 28 to 44.

### Respondent comprehension

The primary challenge in any health preference study is to describe the decision context and descriptive system fully to respondents in a manner that they understand so that they can make informed decisions.<sup>2</sup> Some details can be provided at user request (ie, pulled). For example, respondents can access attribute definitions and examples via user interface elements (ie, information buttons) of the preference elicitation tasks that provide structured information when clicked or hovered over. Other details are imposed (ie, pushed) on each respondent, such as confirmatory checklists and hands-on exercises, to assure minimal understanding.

To introduce the attributes and their levels, the background section begins with a modified version of the EQ-5D-5L instrument (US English V.1.0; <a href="#SP1" data-ref-type="supplementary-material">online supplemental appendix 1</a>). To introduce the referent, the section concludes with an eight-question quiz.<sup>3</sup> To participate in the survey, each respondent must pass the quiz in three attempts.

Prior to the choice tasks, respondents read the hypothetical scenario and complete a confirmatory checklist that verifies understanding of the decision context (ie, role, setting and scenario). Some statements are tailored to reinforce the scenario. For example, DCE on recovery will include “in this scenario, I am going to recover in exactly one year from today, regardless of my choices” and the DCE on death will include “in this scenario, I am going to die in exactly one year from today, regardless of my choices”.

To mitigate potential biases due to attribute order, the order of EQ-5D-5L attributes will be randomised at the respondent level. In wave 2, we will also randomise the order of the attributes; however, the additional attributes will appear always below the EQ-5D-5L attributes to avoid confusion between DCE.

### Preference elicitation

For each DCE, a respondent first completes 15 kaizen tasks, then completes 5 paired comparisons. We assume the Markov property in that the probability of each choice *P<sub>k</sub>* depends only on the choice set, not on any previous choices. Nevertheless, we randomise the sequence of the kaizen tasks and the sequence of the paired comparisons to mitigate potential biases due to task sequence.

In a kaizen task (<a href="#F2" data-ref-type="fig">figure 2</a>), each respondent will be presented with a single HRQoL episode (ie, origin) and asked to relieve three health problems (ie, first, second, third improvement). The ranking of these improvements creates a preference path from an origin profile (without the four improvements) to a destination profile (with the improvements).<sup>8</sup> In the paired comparisons (<a href="#F3" data-ref-type="fig">figure 3</a>), each respondent will be presented with a single HRQoL episode and asked to choose between the episode and a referent (ie, “Starting today, 1 year in a coma then {die, recover}”, “Coma”, “dying immediately”).<sup>1 7 14</sup>

In both tasks, a respondent will read and interpret a single HRQoL episode as well as either four improvements or a referent. Unlike the paired comparisons, a kaizen task draws attention to the relief of health problems rather than the profiles themselves, and a respondent makes three choices, not one. Each choice in a kaizen task is the equivalent of choice in a pick-one task (ie, pick one of four, pick one of six \[i.e., choose two of four improvements=4 × 3/2 = 6\] and pick one of four). Overall, each kaizen task produces 14 choice probabilities, and each paired comparison produces two choice probabilities.

### Experimental design

In wave 1, each DCE has the same five d-efficient blocks of 15 origin-destination (OD) pairs. The process to select the wave 1 blocks has four steps, each programmed in R Statistical Software (V.4.1.3): define the candidate set, block selection by d-efficiency, block evaluation and hold-out assignment (see <a href="#SP2" data-ref-type="supplementary-material">online supplemental appendix 2</a> for the experimental design).<sup>15</sup> For the wave 2 experimental design, we will follow a similar process based on the wave 1 evidence.

### Selecting the OD pairs for the kaizen tasks

To deter lexicographic behaviour, each OD pair includes at least one hold-out (ie, an attribute that the act of choosing will not change its level). In wave 1, the descriptive system has five attributes, which implies four differential attributes and one hold-out per OD pair. The full factorial set has 50 000 OD pairs (ie, five possible hold-outs × (10 possible improvements)<sup>four differential attributes</sup> = 5 × 10<sup>4</sup>).

In step 1, we reduced the full factorial set to a candidate set of 1513 OD pairs by eliminating those with atypical combinations of severe attributes or that contain alternatives with low choice probabilities (see <a href="#SP2" data-ref-type="supplementary-material">online supplemental appendix 2</a>). The candidate pairs are categorised into two groups: incremental and non-incremental pairs. In an incremental pair, attributes are improved by only one level (eg, level 4 to 3). The smallest possible design has five incremental OD pairs (ie, 20 main effects/4 incremental improvements per task=5 OD pairs). In a non-incremental pair, attributes may be improved by two or more levels (eg, level 4 to 2).

In step 2, we began the iterative process of randomly selecting 15 OD pairs (ie, a block of 5 incremental pairs and 10 non-incremental pairs from the candidate set) along four properties. (1) Each of the 20 incremental improvements appears at least once in the five incremental pairs. (2) Each origin profile appears only once (ie, no duplicates within or across blocks); otherwise, the tasks may seem repetitive. (3) Each attribute is a hold-out exactly three times (ie, hold-out balance). (4) Each of the 15 OD has an origin profile.

Next, we assess this block along three criteria: (1) the frequency of each main effect is \>8% (ie, effect balance); (2) each absolute correlation between main effects is \<0.65 (multicollinearity) and (3) utility balance is \>0.6 (ie, b-error).<sup>16 17</sup> Furthermore, we assess the block by computing the determinant of its information matrix (ie, d-error). If a block’s d-error is lower than its predecessors, it is considered more ‘efficient’. We repeated this iterative process until d-efficiency fails to improve (ie, difference in d-error\<0.001). Overall, we selected 75 OD pairs (ie, five blocks) in wave 1 (see ‘Experimental design’).

The third step is to assess the d-efficient blocks based on the worst-case scenarios (eg, null prior, extreme priors) and confirm that that each block has unique origin profiles. The fourth step is to assign the levels of the hold-out attributes to each OD pair and confirm the uniqueness of the origins across the five blocks. The R-code for this experimental design is provided on request.

### Selecting referent pairs for the paired comparisons

From each of the d-efficient blocks of 15 OD pairs, we selected the five origin profiles for the paired comparisons. First, we excluded the origin profiles with level 1 or 2 attributes (ie, reducing the range for profiles from 33333 to 55555). Second, we selected the five profiles that maximised the spacing between values based on the 2016 study (ie, casting the widest net).<sup>1</sup> For each DCE, we hypothesise that the value of each referent lies between the moderate (33333) and extreme (55555) profiles.

Sample size calculations in DCE assure that the number of responses per the choice probability and the number of choice probabilities per main effect estimate are sufficient to meet the needs of the study. With 200 respondents per full-block DCE, choice probabilities as small as 2.5% are approximately normally distributed (ie, NP5 rule: 200 x minimum probability\>5), which is sufficient for this study. In complement to this level of precision, each full-block DCE will produce 220 choice probabilities (15 kaizen tasks × 14 choice probabilities and 5 paired comparisons × 2 choice probabilities) and the number of main effects ranges from 20 to 36 depending on the descriptive system. This implies a minimum of six choice probabilities per main effect (ie, 220/36), which is sufficient for this study. Without the kaizen tasks, it would require 110 paired comparisons per DCE (220/2) to produce the equivalent amount of preference evidence.

Due to the paucity of prior information to inform its experimental designs, each DCE in wave 1 is composed of five full-block DCEs (ie, **multi-block design**; see <a href="#SP2" data-ref-type="supplementary-material">online supplemental appendix 2</a>). The wave 1 results will inform the construction of the wave 2 experimental design, potentially implementing the ‘best’ block for its EQ-5D-5L-only DCEs.

### Survey instrument

The survey instrument consists of five components (for screenshots, see <a href="#SP1" data-ref-type="supplementary-material">online supplemental appendix 1</a>).<sup>18</sup> The first component (six questions) includes a consent form followed by demographic questions that are necessary for implementing the inclusion criteria and ensuring that the recruitment quotas are met.

The background component (18 questions) introduces the descriptive system and confirms respondent knowledge of the referent. For this purpose, respondents completed the US English EQ-5D-5L and EQ-VAS questions, five cognition questions, two self-care questions, two pain/discomfort questions and two anxiety/depression questions. The respondents also complete a quiz and report their perspectives regarding the referent.

The third and fourth components are the two DCEs (46 questions). Specifically, each DCE (23 questions) has a confirmation checklist, a warm-up task, 15 kaizen tasks, 1 warm-up paired comparison and 5 paired comparisons. Question themes for choice tasks were originally developed for a US COVID-19 vaccination study and recently updated to be mobile friendly.<sup>19</sup> The block of OD pairs is the same for the two DCEs, but their sequence differs between DCEs.

The fifth component (11 questions) consists of one debriefing question; seven questions about socio-economic status work and family; four questions on political affiliations and an optional feedback question. Debriefing questions ask the respondent about their preferences on two types of preference elicitation tasks (ie, kaizen tasks vs paired comparisons). Specifically, the questions ask respondents which task they (1) found easier to complete, (2) preferred to complete and (3) found easier to understand. After the debriefing questions, we ask about parental status, residency, marital status, educational attainment (after age 25), 2023 household income, party affiliation and political perspective. The final survey question is an open-text response that allows respondents to provide feedback on the overall survey experience. All respondents should be able to complete the entire survey instrument in 20 min (81 questions; about 15 s per question).

### Data collection

We will recruit 7200 US adults from a panel vendor to complete a survey instrument using a strategy similar to prior US health preference studies (<a href="#T2" data-ref-type="table">table 2</a>).<sup>1 3</sup> In wave 1, each of the six dual-DCE surveys has five blocks with 200 respondents (1000 respondents per DCE). In wave 2, each of the six dual-DCE surveys has one block with 200 respondents (200 respondents per DCE). Potential participants will receive an invitation with information about the survey, estimated time commitment, compensation and a survey link. Data will be monitored by regularly downloading spreadsheets from the platform to ensure recruitment goals are met. No further oversight will be required.

Participation in this survey requires access to a reliable internet connection, a computer or other suitable device, the ability to read English text and the capacity to respond using their chosen device. The study poses no physical risks. However, some questions may ask respondents to consider hypothetical scenarios, which could potentially cause psychological distress in a small number of participants. The survey includes a screening component that will confirm informed consent, verify that participants reside within the 50 United States or Washington, D.C., and ensure they meet one of the 18 predefined demographic quotas.

To align with the 2020 US Census demographics, the recruitment strategy employs 18 quotas stratified by gender (female and other), age (18–34, 35–54, 55+) and race/ethnicity (Hispanic, non-Hispanic Black, non-Hispanic other). While the legal age of adulthood is 18 in most US jurisdictions (47 states and Washington, D.C.), Nebraska and Alabama have a threshold of 19 and Mississippi has a threshold of 20. To ensure inclusivity, our recruitment will prioritise participants from unfilled quotas until the target sample size is reached. We acknowledge that some participants may be excluded after enrolment if they withdraw before completing the survey, exhaust their allotted attempts on the quiz or attempt to retake the survey.

To protect respondent privacy, the survey instrument will not collect any identifying information. To safeguard data confidentiality, the survey data sets will be securely stored as password-protected files on computers equipped with two-factor authentication. To ensure data preservation and minimise the risk of data loss, an automated system will perform real-time data backups of the secured files.

### Analysis plan

The analysis plan (<a href="#SP1" data-ref-type="supplementary-material">online supplemental appendix 3</a>) begins with a series of descriptive analyses examining the external and internal validity of the preference evidence (<a href="#T1" data-ref-type="table">table 1</a> and as appendices of the main papers). These findings aid in the evaluation of the preference evidence prior to choice modelling.

For the primary analyses, we will estimate conditional logit (CL) models by maximum likelihood overall and scenario/descriptive system (<a href="#T2" data-ref-type="table">table 2</a> and as an appendix of the main papers).<sup>20</sup> Values will be shown on either an experience scale (wave 1) or on a QALY scale (wave 2). Each CL estimation will produce main effect estimates $`\beta_{k}`$ as well as estimates for three ancillary parameters: a scale parameter $`\sigma`$ representing the proportional relationship between the value scale and the log-odds scale, an intercept parameter $`\alpha_{0}`$ representing the shift between kaizen and paired comparison main-effect estimates and a slope parameter $`\alpha_{1}`$ representing the difference in precision by task.

In complement to the primary analyses, we will conduct a series of secondary analyses (an appendix of the main papers) to assess potential biases in the scenario/system-specific results due specifically to the design of dual-DCE surveys, namely survey, scenario order and DCE order effects. Furthermore, we will conduct a series of sensitivity analyses (an appendix of the main papers) to assess potential biases in the DCE-specific results, namely block, task sequence and attribute order effects.

<a href="#T3" data-ref-type="table">Table 3</a> summarises the hypotheses of the primary, secondary and sensitivity analyses. Due to the panel format of the preference evidence, all p-values, 95% CIs and SEs will be estimated using cluster bootstrap techniques with replacement, block-specific strata and 1000 iterations.

<div id="T3" class="table-wrap">

<div class="caption">

###### Hypotheses in the primary, secondary and sensitivity analyses

</div>

<table>
<tbody>
<tr>
<td>Wave 1 primary analyses</td>
<td>H1.1: The main effects are zero under acute, chronic and generic episodes (Aim 1)</td>
</tr>
<tr>
<td></td>
<td>H1.2: The main effects are the same under acute, chronic and generic episodes (Aim 2)</td>
</tr>
<tr>
<td rowspan="3">Wave 2 primary analyses</td>
<td>H2.1: The main effects are zero with and without the additional attributes (Aim 1)</td>
</tr>
<tr>
<td>H2.2: The main effects are the same with and without additional attributes (Aim 3)</td>
</tr>
<tr>
<td>H2.3: The main effects of the two component attributes are independent (ie, no overlap) (Aim 3)</td>
</tr>
<tr>
<td rowspan="3">Secondary analyses by scenario/system</td>
<td>H3.1: The main effects are the same in the first DCEs (ie, no sampling effects)</td>
</tr>
<tr>
<td>H3.2: The main effects are the same in the second DCEs (ie, no scenario/system order effects)</td>
</tr>
<tr>
<td>H3.3: The main effects are the same between the first and second DCEs (ie, no DCE order effects)</td>
</tr>
<tr>
<td rowspan="3">Sensitivity analyses byDCE</td>
<td>H4.1: The main effects are the same by block (ie, no block effects)</td>
</tr>
<tr>
<td>H4.2: The main effects are the same by task sequence (ie, no scenario/system order effects)</td>
</tr>
<tr>
<td>H4.3: The main effects are the same by attribute order (ie, no attribute order effects)</td>
</tr>
</tbody>
</table>

DCEdiscrete choice experiment

</div>

Furthermore, we envision explorations of econometric methods, experimental design, task design and preference heterogeneity in future analyses; however, these are beyond the scope of this protocol. Recent studies have shown that estimates of random-parameter models (eg, mixed logit) can differ greatly from the true parameters, even when correctly specified;<sup>21 22</sup> however, we would be interested in estimating scale-adjusted latent-class models to separate differences in behavioural factors and preferences by class.23,25

### Ethics and dissemination

This research project involves two waves of anonymous surveys of adults in the US general population. The independent review board (IRB) at Advarra determined that this research project (Pro00080475; 11 July 2024) is exempt from IRB oversight based on the Department of Health and Human Services regulations found at 45 CFR 46.104(d).<sup>2</sup> Furthermore, the IRB determined that the project is not subject to requirements for continuing review.

To disseminate our findings, we will prepare multiple manuscripts for publication in peer-reviewed journals and present highlights at scientific meetings, such as the EuroQol Plenary Meeting, International Academy of Health Preference Research and ISPOR—The Professional Society for Health Economics and Outcomes Research. We will also share the statistical code, survey instrument screenshots, and deidentified data on reasonable request to enhance the transparency and interpretability of our results.

## supplementary material

10.1136/bmjopen-2024-091097

10.1136/bmjopen-2024-091097

10.1136/bmjopen-2024-091097

## Acknowledgements

BMC appreciates Fanni Rencz and Michał Jakubczyk for their consultation and assistance with the wave 2 grant proposal (1769-RA) and would like to thank Juan M. Ramos-Goñi at Maths in Health for his consultation, assistance and support with the survey instrument, including the survey and question themes for LimeSurvey

## Footnotes

## References

## References

1. Craig BM, Rand K. Choice Defines QALYs: A US Valuation of the EQ-5D-5L. Med Care. 2018;56:529–36. doi: 10.1097/MLR.0000000000000912.

2. Hollin IL, Craig BM, Coast J, et al. Reporting Formative Qualitative Research to Support the Development of Quantitative Preference Study Protocols and Corresponding Survey Instruments: Guidelines for Authors and Reviewers. Patient. 2020;13:121–36. doi: 10.1007/s40271-019-00401-x.

3. Jumamyradov M, Craig BM, Rivero-Arias O, et al. Child health valuation protocol for a discrete choice experiment comparing paired comparison and kaizen tasks and estimating US EQ-5D-Y-3L values on an experience scale. BMJ Open. 2023;13:e077256. doi: 10.1136/bmjopen-2023-077256.

4. Rivero-Arias O, Buckell J, Allin B, et al. Using stated-preferences methods to develop a summary metric to determine successful treatment of children with a surgical condition: a study protocol. BMJ Open. 2022;12:e062833. doi: 10.1136/bmjopen-2022-062833.

5. Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L) Qual Life Res. 2011;20:1727–36. doi: 10.1007/s11136-011-9903-x.

6. Stolk EA, Craig BM, Mulhern B, et al. Health Valuation: Demonstrating the Value of Health and Lifespan. Patient. 2017;10:515–7. doi: 10.1007/s40271-017-0252-x.

7. Craig BM, Jumamyradov M, Rivero-Arias O. The Performance of Kaizen Tasks Across Three Online Discrete Choice Experiment Surveys: An Evidence Synthesis. Patient. 2024;17:635–44. doi: 10.1007/s40271-024-00708-4.

8. Craig BM, Rand K, Hartman JD. Preference Paths and Their Kaizen Tasks for Small Samples. Patient. 2022;15:187–96. doi: 10.1007/s40271-021-00541-z.

9. Oppe M, Rand-Hendriksen K, Shah K, et al. EuroQol Protocols for Time Trade-Off Valuation of Health Outcomes. Pharmacoeconomics. 2016;34:993–1004. doi: 10.1007/s40273-016-0404-1.

10. Jumamyradov M, Craig BM. Measuring Effectiveness Based on Patient Experience (Instead of QALYs) in US Value Assessments. Pharmacoeconomics. 2025;43:171–6. doi: 10.1007/s40273-024-01444-1.

11. Bohannon C. Eve: How the Female Body Drove 200 Million Years of Human Evolution. Random House of Canada; 2023.

12. Li A, Deyrup AT, Graves JL, Jr, et al. Race in the Reading: A Study of Problematic Uses of Race and Ethnicity in a Prominent Pediatrics Textbook. Acad Med. 2022;97:1521–7. doi: 10.1097/ACM.0000000000004666.

13. Sampson C, Addo R, Haywood P, et al. Development and Qualitative Testing of Eq-5d-5l Bolt-Ons for Cognition and Vision. 2020.

14. David HA. London: 1963. The method of paired comparisons.

15. R Core Team R: a language and environment for statistical computing

16. Huber J, Zwerina K. The Importance of Utility Balance in Efficient Choice Designs. JMR. 1996;33:307. doi: 10.2307/3152127.

17. Ngene 1.2 User Manual & Reference Guide. Sydney, Australia: ChoiceMetrics; 2018.

18. LimeSurvey community edition. 2024

19. Craig BM. United States COVID-19 Vaccination Preferences (CVP): 2020 Hindsight. Patient. 2021;14:309–18. doi: 10.1007/s40271-021-00508-0.

20. Henningsen A, Toomet O. maxLik: A package for maximum likelihood estimation in R. Comput Stat. 2011;26:443–58. doi: 10.1007/s00180-010-0217-1.

21. Jumamyradov M, Craig BM, Jakubczyk M. Scale and rate heterogeneity in the EQ-5D-5L valuation. Health Qual Life Outcomes. 2024;22:55. doi: 10.1186/s12955-024-02271-w.

22. Jumamyradov M, Craig BM, Greene WH, et al. Comparing the Mixed Logit Estimates and True Parameters under Informative and Uninformative Heterogeneity: A Simulated Discrete Choice Experiment. Comput Econ. 2024 doi: 10.1007/s10614-024-10637-x.

23. Karim S, Craig BM, Groothuis-Oudshoorn CGM. Exploring the importance of controlling heteroskedasticity and heterogeneity in health valuation: a case study on Dutch EQ-5D-5L. Health Qual Life Outcomes. 2022;20:85. doi: 10.1186/s12955-022-01989-9.

24. Karim S, Craig BM, Poteet S. Does Controlling for Scale Heterogeneity Better Explain Respondents’ Preference Segmentation in Discrete Choice Experiments? A Case Study of US Health Insurance Demand. Med Decis Making. 2021;41:573–83. doi: 10.1177/0272989X21997345.

25. Karim S, Craig BM, Tejada RA, et al. Preference heterogeneity in health valuation: a latent class analysis of the Peru EQ-5D-5L values. Health Qual Life Outcomes. 2023;21:1. doi: 10.1186/s12955-022-02079-6.

<figure id="d67e1392">

</figure>

## Supplementary Materials

10.1136/bmjopen-2024-091097

10.1136/bmjopen-2024-091097

10.1136/bmjopen-2024-091097

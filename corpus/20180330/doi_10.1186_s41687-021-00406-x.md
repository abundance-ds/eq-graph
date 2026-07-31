---
project_id: "20180330"
work_id: "doi:10.1186/s41687-021-00406-x"
doi: "10.1186/s41687-021-00406-x"
pmid: "34982262"
pmcid: "PMC8727660"
title: "Adding a fatigue item to the EQ-5D-5L improves its psychometric performance in the general population"
journal: "Journal of Patient-Reported Outcomes"
publication_date: "2022-01-04"
volume: "6"
authors:
  - name: "Inge Spronk"
    orcid: "http://orcid.org/0000-0001-9571-576X"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Suzanne Polinder"
    orcid: "http://orcid.org/0000-0002-4331-3141"
    affiliation_ids:
      - "Aff1"
  - name: "Gouke J. Bonsel"
    orcid: "http://orcid.org/0000-0002-8364-1086"
    affiliation_ids:
      - "Aff3"
  - name: "M. F. Janssen"
    affiliation_ids:
      - "Aff4"
  - name: "Juanita A. Haagsma"
    orcid: "http://orcid.org/0000-0002-2055-548X"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.5645.2000000040459992XDepartment of Public Health, Erasmus MC, University Medical Center Rotterdam, P.O. Box 2040, 3000 CA Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "grid.416213.30000 0004 0460 0556Association of Dutch Burn Centres, Maasstad Hospital, Rotterdam, the Netherlands"
  - id: "Aff3"
    name: "EuroQol Group Executive Office, Rotterdam, The Netherlands"
  - id: "Aff4"
    name: "grid.5645.2000000040459992XSection Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Rotterdam, The Netherlands"
keywords:
  - "Bolt-on"
  - "EQ-5D"
  - "Fatigue"
  - "General population"
  - "Health-related quality of life"
licence: "cc-by"
source_file: "input/projects/20180330/papers/doi_10.1186_s41687-021-00406-x.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8727660/fullTextXML"
source_method: "epmc_xml"
source_sha256: "fefb959ab8191f9b11ed4670107f4cb10162e7d73e630d72edc6d296b437d41a"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Adding a fatigue item to the EQ-5D-5L improves its psychometric performance in the general population

## Abstract

### Background

Fatigue is a common and often disturbing sequela of serious chronic health conditions. In the widely applied HRQL instrument, the EQ-5D, this aspect is not included directly, for its assumed lack of additional information. We investigated the validity of this assumption by determining the gain—if any—of an additional fatigue item to the EQ-5D-5L in a general population sample.

### Methods

A Dutch general population sample (including diseased people) completed a web-based survey including the EQ-5D-5L and the Rivermead Post-Concussion Symptoms Questionnaire (RPQ). The RPQ fatigue item was used to create the EQ-5D-5L + Fatigue. We head-to-head compared the psychometric performance contrasting the EQ-5D-5L and EQ-5D-5L + Fatigue: distribution (e.g. ceiling), informativity cf. Shannon's indices, convergent validity, domain dependency, and explanatory power. Results were compared between subgroups with and without ≥ 1 chronic health condition.

### Results

The study population consisted of 3027 persons of whom 52% had a chronic health condition. The mean EQ-5D-5L utility score was 0.83 and 48% experienced some degree of fatigue. Adding the fatigue item to the EQ-5D-5L decreased the ceiling effect, increased absolute informativity (Hʹ = 6.44 vs. Hʹ = 4.90) and relative informativity (Jʹ = 0.46 vs. Jʹ = 0.42). The extra fatigue item slightly increased convergent validity (Spearman’s rank correlation coefficient = − 0.61 vs. − 0.62). Domain dependency analysis showed that all EQ-5D-5L domains are dominant over the fatigue item. Explanatory power of the EQ-5D-5L + Fatigue was higher compared to the EQ-5D-5L (R<sup>2</sup> = 0.42 vs. 0.39). The gain is substantially larger in the subgroup with chronic health conditions.

### Conclusions

Adding a fatigue item to the EQ-5D-5L improved all psychometric performance criteria of the enriched instrument in the general population. Effects are substantially larger in the subgroup with chronic health conditions, indicating that adding a fatigue item to the EQ-5D-5L is especially relevant in evaluating the HRQL of diseased people.

## Background

Self-reported health-related quality of life (HRQL) questionnaires are increasingly used to evaluate the impact of a health condition, the effectiveness of treatments and interventions, and the level of quality of care \[1–3\]. HRQL instruments aim to capture the patient's perception of his/her physical, psychological and social wellbeing \[4\]. HRQL instruments can be generic (i.e. applicable to any disease or condition) or disease/condition-specific. Disease-specific instruments focus on one specific condition and may include treatment-defined levels of ill-health, i.e. thresholds defining start or stop of a particular treatment \[5\]. Generic instruments allow for comparison between different diseases, between subgroups of the general population, and often they allow for use within multi-faceted diseases \[5\]. All measures are a compromise between feasibility (i.e. the ease of an instrument in its intended context of use, given constraints such as time or money), on the one hand, and validity (i.e. the degree to which an instrument measures the constructs it purports to measure) and reliability on the other hand \[6\].

The EQ-5D is a widely used generic HRQL instrument both in economic and clinical applications, that has been validated for a wide range of diseases and is available in many languages \[7, 8\]. An advantage is its conciseness and low burden to complete this instrument \[9, 10\]. The EQ-5D consists of five domains: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. The EQ-5D also includes a visual analogue scale (EQ VAS) \[11\]. The five domains can be scored on either a three (EQ-5D-3L) or more refined five level (EQ-5D-5L) ordinal scale \[11, 12\]. Based on these five scores an index with preference interpretation can be calculated by applying weights which have been separately derived. To cover lack of comprehensiveness, the EQ-5D enables the use of ‘bolt-on’ items \[13, 14\]. A ‘bolt-on’ is a item (like fatigue or cognition) on a specific health problem or dysfunction that is not included in the original instrument \[13\].

This paper addresses the construct validity and sensitivity of EQ-5D for fatigue problems. Together with sensory problems and cognitive problems, fatigue is often mentioned as potential deficit in the domain structure of the EQ-5D \[13, 15–17\]. During the inception of the EQ-5D instrument an 'energy/tiredness' was considered as the positively defined inverse of 'fatigue'. It was not included in the final version of the instrument as it failed to show additional effect in small-sized analyses \[18–20\].

In active disease and quite some chronic health conditions, the relevance of fatigue to the patient is beyond doubt \[21–24\]. Focused recent studies suggest that in generic measures (like EQ-5D-5L) the fatigue/energy/tiredness domain could be considered as relevant addition \[15, 16, 25–28\]. A recent study listing 17 specific health-related features not addressed by the EQ-5D, put fatigue forward as the feature most needed \[15\].

The general population also reports some degree of fatigue, up to 50% \[29–31\]. While this limits the domain to be used as disease classifier, it enables research into the coverage of fatigue by other EQ-5D domains using HRQL data from a general population sample. The primary aim of this study is to what extent adding a fatigue item would add unique information to the generic EQ-5D-5L. The secondary aim is to detail the results for people with and without a chronic disease separately.

## Methods

### Participants

A web-based survey was distributed to members of the Dutch general population aged 18–75 years by Survey Sampling International during the period June 29th till July 31st 2017 \[32\]. The sample was selected to be representative of the Dutch population with respect to sex, age, and education. All participants completed an informed consent form before completing the survey. The study was part of the large CENTER-TBI study (EC grant 602150). Ethical approval was provided by the Leids Universitair Centrum—Commissie Medische Ethiek (P14.222/NV/nv).

### Measures

As background information, the survey collected data on age, sex, highest achieved level of education, household income level, and self-reported chronic health conditions. Several health measures were included. The first was a generic measure: the EQ-5D-5L, which assesses a patient’s HRQL and health status today. The default response format is five ordered response options (1–5; no problems, slight problems, moderate problems, severe problems, and extreme problems) \[12\]. Based on the five domain scores, a utility score (through weighting) was calculated at the individual level, using the Dutch value set \[33\]. The utility score is anchored at 0 (referring to a state as bad as being dead) and 1 (full health) \[9\]. This study also used an equally weighted sum of all domain scores, range 5–25, the 'level sum score'. For descriptive analysis the scores of the five domains can be combined to create a health profile; profile ‘11111’ represents the best possible health state given the classification, while profile ‘55555’ represents the worst health state. This composed score is different from the level sum score as the specific score on each domain is indicated, whereas in the level sum score, the domain scores are summed up into one overall score without knowing what domain contributed to a higher score. In addition, the EQ-5D includes a visual analogue scale (EQ VAS) \[34\] that assesses the respondent’s health on a scale from 0 (worst imaginable health) to 100 (best imaginable health) \[9\].

The second instrument was the Rivermead Post-Concussion Symptoms Questionnaire (RPQ) \[35\]. This questionnaire lists 16 different symptoms and complaints (including 'fatigue'), with five ordinal response options. The single fatigue item of the RPQ runs: ‘Do you (i.e., over the last 24 h) suffer from fatigue?’. Response options included: 0 (not experienced at all), 1 (no more of a problem), 2 (a mild problem), 3 (a moderate problem) and 4 (a severe problem). To resemble the 5L format of the EQ-5D, the 0–4 score was recoded into a 1–5 score.

### Data analyses

Descriptive statistics were used to assess characteristics and outcomes of the EQ-5D-5L and the RPQ fatigue item. EQ-5D-5L and RPQ fatigue outcomes were compared between subgroups of respondents with and without ≥ 1 chronic health condition. Mann–Whitney U tests were used for continuous variables and chi-square tests for categorical variables.

The RPQ fatigue item was used to investigate the added value of a fatigue item for the EQ-5D-5L. The EQ-5D-5L + Fatigue was created by combining the EQ-5D-5L with the recoded RPQ fatigue item. First, we studied distributional effects of the EQ-5D-5L and EQ-5D-5L + Fatigue by analyzing the number of unique profiles and the ceiling of the EQ-5D-5L vs. the EQ-5D-5L + Fatigue. The ceiling was calculated by the comparison of full health profiles, ‘11111’ for the EQ-5D-5L and ‘111111’ for the EQ-5D-5L + Fatigue. A higher proportion of full health profiles indicates a higher degree of ceiling. Also, the relation between fatigue and the EQ VAS was investigated by studying the mean EQ VAS for each of the five levels of fatigue. The same relation was studied for the five most frequently observed EQ-5D health states.

Then, the informativity of the EQ-5D-5L and EQ-5D-5L + Fatigue was assessed by calculation of the Shannon index (Hʹ) and the Shannon Evenness index (Jʹ) \[36–38\]. These Shannon indices give information on the ability of the EQ-5D-5L(+ Fatigue) to reflect and quantify diversity in a population \[39\]. The Shannon index (Hʹ) was determined by: $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\text{H}}^{\prime } = - \sum\nolimits_{{\text{i = 1}}}^{{\text{c}}} {{\text{pi}}^{{2}} {\text{log p}}_{{\text{i}}} }$$\end{document}`$. With pi being the proportion of respondents with one specific health profile (e.g., 11111), and C being the total number of theoretically possible health profiles (i.e., 3125 for the EQ-5D-5L, and 15,625 for the EQ-5D-5L + Fatigue). If a profile is not observed its contribution is 0 (zero) to this summation. A higher Shannon index (Hʹ) indicates that more information is captured by the EQ-5D-5L or EQ-5D-5L + Fatigue. The Shannon Evenness index (Jʹ) was calculated as: Jʹ = Hʹ/Hʹmax, with Hʹmax is 2logC. The Shannon Evenness index (Jʹ) reflects whether the extra domain is used to discriminate more health profiles as efficient as the standard set—in that case J' remains unchanged while H' will increase \[40\]. Both Hʹ and Jʹ need to be taken into account for a full interpretation of informativity when comparing classifications \[40\]. We computed H' and J' for the EQ-5D-5L and the EQ-5D-5L + Fatigue, separately.

Convergent validity was assessed by analyzing the Spearman’s rank correlation between the EQ-5D-5L (level sum score) and the EQ VAS, and the EQ-5D-5L + Fatigue (level sum score) and the EQ VAS. Cohen’s criteria were applied to evaluate the strength of association: correlations were strong if r ≥ 0.50, moderate if r ≥ 0.30–0.49, and weak if r ≥ 0.10–0.29 \[41\]. For determination of domain dependency (redundancy) we studied mutual relations between the domains. A domain A is defined to dominate another domain B, if the likelihood that a poor level in A coincides with a good level B is smaller than the probability of the reverse situation, corrected for chance. It is a simple indicator of directionality of relations between domains in a given dataset. These probabilities were presented in domain-to-domain cross tables of the EQ-5D-5L domains and the fatigue item. Profiles with a severe or extreme problem in one domain (L4: severe problem or L5: extreme problem) and no problem (L1: no problem) in another domain were analyzed \[42\]. For example, profiles with fatigue level 4/5 and mobility level 1 were compared to profiles with mobility level 4/5 and fatigue level 1. The ratio of the chance adjusted frequencies provides information on the dominance of a domain: if the result of the equation is equal to 1 the domains are independent; if the result of the equation is \< 1 fatigue dominates; if the result of the equation is \> 1 fatigue is subordinate or dependent \[33\].

Lastly, the added explanatory power of an extra fatigue item was tested through regression analyses, with the EQ VAS score as outcome. Predictive performance was compared of the EQ-5D-5L domains with and without the extra fatigue item in univariate and multivariable analyses. The levels ‘slight problems’ (L2), ‘moderate problems’ (L3), ‘severe problems’ (L4) and ‘extreme problems’ (L5) were used to predict the EQ VAS. The ‘no problems’ level (L1) was used as the reference category. Then, multivariable analyses were performed with combinations of the five EQ-5D domains and the fatigue item in the model. The combinations consisted of the original EQ-5D-5L domains, the EQ-5D-5L + Fatigue dimensions, and all combinations of five out of the six domains. All analyses were done for the whole sample as well as for the two subgroups with (diseased group) and without ≥ 1 chronic health condition (healthy group). With the significance level of all analyses was set at *p* \< 0.05. All analyses were done in IBM SPSS Statistics 25.

### Hypotheses

- Health-related quality of life is better and the proportion and severity of fatigue lower in respondents without a chronic health condition compared to those with ≥ 1 chronic health conditions.

- The ceiling (proportion persons in the best profile) in EQ-5D-5L + Fatigue is lower compared to EQ-5D-5L.

- Adding a fatigue item increases absolute informativity (Hʹ) of the EQ-5D-5L in terms of Shannon's indices; while relative informativity (Jʹ) remains comparable.

- Adding a fatigue item increases convergent validity of the EQ-5D-5L, using the EQ VAS as reference.

- Adding a fatigue item increases explanatory power no less or more than any other domain, using the EQ VAS as reference.

- The added value of fatigue is larger in the subgroup with ≥ 1 chronic health condition compared to the subgroup without a chronic health condition.

## Results

### Respondents

In total, 3027 people returned the questionnaire. The mean age was 44.7 years old (SD 15.3) and half of the participants was male (Table <a href="#Tab1" data-ref-type="table">1</a>). Most had a middle level of education (46.9%), and the majority was employed (54.0%). About half of the participants (52.0%) had one or more chronic health condition (31.2% one condition; 19.9% two or more conditions).

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of study population

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristic</th>
<th style="text-align: left;">Total sample (n = 3027)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>Sex</em>: Male</td>
<td style="text-align: left;">1520 (50.2%)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Age</em> (M, SD)</td>
<td style="text-align: left;">44.7 (15.3)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><em>Age categories</em></td>
</tr>
<tr>
<td style="text-align: left;">18–24 years</td>
<td style="text-align: left;">365 (12.1%)</td>
</tr>
<tr>
<td style="text-align: left;">25–39 years</td>
<td style="text-align: left;">814 (26.9%)</td>
</tr>
<tr>
<td style="text-align: left;">40–59 years</td>
<td style="text-align: left;">1231 (40.7%)</td>
</tr>
<tr>
<td style="text-align: left;">60–75 years</td>
<td style="text-align: left;">617 (20.4%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><em>Level of education</em></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">811 (26.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">1420 (46.9%)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: left;">796 (26.3%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><em>Work status*</em></td>
</tr>
<tr>
<td style="text-align: left;">Employed</td>
<td style="text-align: left;">1635 (54.0%)</td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: left;">316 (10.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Looking after others</td>
<td style="text-align: left;">125 (4.1%)</td>
</tr>
<tr>
<td style="text-align: left;">Student</td>
<td style="text-align: left;">209 (6.9%)</td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: left;">386 (12.8%)</td>
</tr>
<tr>
<td style="text-align: left;">Unable to work</td>
<td style="text-align: left;">356 (11.8%)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><em>Number of chronic health conditions</em></td>
</tr>
<tr>
<td style="text-align: left;">No chronic health condition</td>
<td style="text-align: left;">1453 (48.0%)</td>
</tr>
<tr>
<td style="text-align: left;">1 chronic health condition</td>
<td style="text-align: left;">971 (32.1%)</td>
</tr>
<tr>
<td style="text-align: left;">2 chronic health conditions</td>
<td style="text-align: left;">368 (12.2%)</td>
</tr>
<tr>
<td style="text-align: left;">3 chronic health conditions</td>
<td style="text-align: left;">149 (4.9%)</td>
</tr>
<tr>
<td style="text-align: left;"> ≥ 4 chronic health conditions</td>
<td style="text-align: left;">86 (2.8%)</td>
</tr>
</tbody>
</table>

\*Work status was categorized as employed (employee and self-employed), unemployed (consisting out of work for more than and less than 1 year), looking after others (e.g. a carer or parent), a student, retired and unable to work

</div>

### EQ-5D-5L and fatigue outcomes

The mean EQ-5D-5L utility score was 0.83 (SD 0.21) and the mean EQ VAS was 76.3 (SD 18.1) (Table <a href="#Tab2" data-ref-type="table">2</a>). Most problems were reported for the pain/discomfort domain; 51.4% of the respondents reported at least slight problems. Least problems were reported for self-care; 8.7% reported any problem. A total of 47.9% of the respondents reported at least mild fatigue problems. The mean EQ-5D-5L utility score and EQ VAS score were significantly higher ('better') in healthy respondents without a chronic health condition compared to the diseased group (*p* \< 0.001). A significantly higher proportion of diseased respondents reported fatigue compared to healthy respondents (*p* \< 0.001). The diseased group showed more problems for all domains (*p* \< 0.001), the contrast was largest in the pain/discomfort domain (73.3% vs. 27.8%).

<div id="Tab2" class="table-wrap">

<div class="caption">

EQ-5D-5L and fatigue outcomes

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Total sample (n = 3027)</th>
<th style="text-align: left;">Without a chronic health condition (n = 1453)</th>
<th style="text-align: left;">With ≥ 1 chronic health condition (n = 1574)</th>
<th style="text-align: left;"><em>p</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;"><em>EQ-5D-5L outcomes</em></td>
</tr>
<tr>
<td style="text-align: left;">Mobility (% with problems)</td>
<td style="text-align: left;">819 (27.1%)</td>
<td style="text-align: left;">123 (8.5%)</td>
<td style="text-align: left;">696 (44.2%)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Self-care (% with problems)</td>
<td style="text-align: left;">264 (8.7%)</td>
<td style="text-align: left;">28 (1.9%)</td>
<td style="text-align: left;">236 (15.0%)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities (% with problems)</td>
<td style="text-align: left;">917 (30.3%)</td>
<td style="text-align: left;">116 (8.0%)</td>
<td style="text-align: left;">801 (50.9%)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort (% with problems)</td>
<td style="text-align: left;">1557 (51.4%)</td>
<td style="text-align: left;">404 (27.8%)</td>
<td style="text-align: left;">1153 (73.3%)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression (% with problems)</td>
<td style="text-align: left;">998 (33.0%)</td>
<td style="text-align: left;">267 (18.4%)</td>
<td style="text-align: left;">731 (46.4%)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Utility score (M, SD)</td>
<td style="text-align: left;">0.83 (0.21)</td>
<td style="text-align: left;">0.93 (0.11)</td>
<td style="text-align: left;">0.73 (0.23)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>EQ VAS</em></td>
<td style="text-align: left;">76.3 (18.1)</td>
<td style="text-align: left;">83.8 (13.7)</td>
<td style="text-align: left;">69.5 (19.0)</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"><em>RPQ Fatigue</em></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Not experienced at all</td>
<td style="text-align: left;">1195 (39.5%)</td>
<td style="text-align: left;">810 (55.7%)</td>
<td style="text-align: left;">385 (24.5%)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">No more of a problem</td>
<td style="text-align: left;">381 (12.6%)</td>
<td style="text-align: left;">191 (13.1%)</td>
<td style="text-align: left;">190 (12.1%)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Mild fatigue</td>
<td style="text-align: left;">708 (23.4%)</td>
<td style="text-align: left;">300 (20.6%)</td>
<td style="text-align: left;">408 (25.9%)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Moderate fatigue</td>
<td style="text-align: left;">478 (15.8%)</td>
<td style="text-align: left;">123 (8.5%)</td>
<td style="text-align: left;">355 (22.6%)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">Severe fatigue</td>
<td style="text-align: left;">265 (8.8%)</td>
<td style="text-align: left;">29 (2.0%)</td>
<td style="text-align: left;">236 (15.0%)</td>
<td></td>
</tr>
</tbody>
</table>

</div>

### Distributional effects—ceiling, unique profiles

In total, 1116 of the 3027 respondents (37%) reported full health with the EQ-5D-5L, while 744 (25%) reported full health with the fatigue item added. The 372 respondents that had a full health status based on the EQ-5D-5L, but not based on the EQ-5D-5L + Fatigue were on average 40.4 years old (SD 14.8) and slightly more than half of them were females (53%). Most had a middle education (48%), and the minority had a chronic health condition (27%). The 25% full health group with the fatigue item added had a somewhat higher mean age (44.5 years old; SD 15.6) and lower presence of chronic health conditions (17% instead of 27%).

The number of observed unique health profiles (among all respondents) was 368 out of 3125 (12%) for the EQ-5D-5L, and 636 out of 15,625 (4%) for the EQ-5D-5L + Fatigue. In the healthy group (n = 1453), 90 out of 3125 (3%) possible EQ-5D-5L health profiles, and 156 out of 15,625 (1%) possible EQ-5D-5L + Fatigue health profiles were observed. In the diseased group (n = 1574) respondent 342 out of 3125 (11%) possible EQ-5D-5L health profiles, and 581 out of 15,625 (4%) possible EQ-5D-5L + Fatigue health profiles were observed.

Table <a href="#Tab3" data-ref-type="table">3</a> shows the mean EQ VAS score for each level of fatigue and any EQ-5D outcome, as well as for the five most common EQ-5D profiles. Mean EQ VAS score decreased when the severity of fatigue problems increased. Mean EQ VAS was 84.3 when no fatigue was present, 75.9 when patients experienced mild fatigue problems, and 54.7 when patients experienced severe fatigue problems. The same pattern was more or less present in the selected EQ-5D profiles, except for the profile ‘11111’, where the mean EQ VAS was similar in patients with severe fatigue problems (mean EQ VAS = 84.9) compared to patients with mild fatigue (mean EQ VAS = 83.5) and higher when compared to patients with moderate fatigue problems (mean EQ VAS = 78.4), although these differences were not significantly different.

<div id="Tab3" class="table-wrap">

<div class="caption">

EQ VAS score for each of the five recoded fatigue items, and for the five most common EQ-5D-5L profiles

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">EQ-5D profile</th>
<th colspan="2" style="text-align: left;">Fatigue = 1</th>
<th colspan="2" style="text-align: left;">Fatigue = 2</th>
<th colspan="2" style="text-align: left;">Fatigue = 3</th>
<th colspan="2" style="text-align: left;">Fatigue = 4</th>
<th colspan="2" style="text-align: left;">Fatigue = 5</th>
</tr>
<tr>
<th style="text-align: left;">n</th>
<th style="text-align: left;">Mean EQ VAS (95% CI)</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">Mean EQ VAS (95% CI)</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">Mean EQ VAS (95% CI)</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">Mean EQ VAS (95% CI)</th>
<th style="text-align: left;">n</th>
<th style="text-align: left;">Mean EQ VAS (95% CI)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">All</td>
<td style="text-align: left;">1195</td>
<td>84.3 (83.5–85.1)</td>
<td style="text-align: left;">381</td>
<td>78.0 (76.5–79.6)</td>
<td style="text-align: left;">708</td>
<td>75.9 (74.8–77.0)</td>
<td style="text-align: left;">478</td>
<td>67.8 (66.3–69.4)</td>
<td style="text-align: left;">265</td>
<td>54.7 (52.1–57.2)</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Subgroups based on their EQ-5D profile</em></td>
</tr>
<tr>
<td style="text-align: left;">11111</td>
<td style="text-align: left;">744</td>
<td>87.5 (86.5–88.4)</td>
<td style="text-align: left;">132</td>
<td>85.2 (83.5–86.8)</td>
<td style="text-align: left;">174</td>
<td>83.5 (81.8–85.2)</td>
<td style="text-align: left;">50</td>
<td>78.4 (74.0–82.8)</td>
<td style="text-align: left;">16</td>
<td>84.9 (78.3–91.6)</td>
</tr>
<tr>
<td style="text-align: left;">11121</td>
<td style="text-align: left;">155</td>
<td>85.1 (83.3–86.9)</td>
<td style="text-align: left;">52</td>
<td>83.1 (80.8–85.4)</td>
<td style="text-align: left;">78</td>
<td>81.1 (78.9–83.4)</td>
<td style="text-align: left;">37</td>
<td>81.9 (78.7–85.2)</td>
<td style="text-align: left;">7</td>
<td>78.0 (67.7–88.4)</td>
</tr>
<tr>
<td style="text-align: left;">11112</td>
<td style="text-align: left;">46</td>
<td>80.6 (76.1–85.1)</td>
<td style="text-align: left;">26</td>
<td>75.7 (68.0–83.4)</td>
<td style="text-align: left;">55</td>
<td>79.8 (76.1–83.6)</td>
<td style="text-align: left;">27</td>
<td>79.0 (75.8–82.2)</td>
<td style="text-align: left;">0</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">11122</td>
<td style="text-align: left;">28</td>
<td>77.4 (70.8–84.0)</td>
<td style="text-align: left;">13</td>
<td>75.4 (61.8–89.0)</td>
<td style="text-align: left;">40</td>
<td>78.1 (75.0–81.2)</td>
<td style="text-align: left;">28</td>
<td>73.9 (69.3–78.4)</td>
<td style="text-align: left;">10</td>
<td>72.7 (59.9–85.5)</td>
</tr>
<tr>
<td style="text-align: left;">21221</td>
<td style="text-align: left;">28</td>
<td>81.0 (75.0–87.0)</td>
<td style="text-align: left;">19</td>
<td>78.6 (75.1–82.2)</td>
<td style="text-align: left;">18</td>
<td>73.6 (64.4–82.8)</td>
<td style="text-align: left;">14</td>
<td>77.5 (70.7–84.3)</td>
<td style="text-align: left;">3</td>
<td>78.7 (58.4–90.0)</td>
</tr>
</tbody>
</table>

</div>

### Informativity of the EQ-5D-5L with and without an extra fatigue item

The Shannon Index (Hʹ) was 4.90 for the EQ-5D-5L and 6.44 for the EQ-5D-5L + Fatigue. The Shannon Evenness index (Jʹ) of the EQ-5D-5L was lower than that of the EQ-5D-5L + Fatigue (0.422 vs. 0.462). In healthy respondents, Hʹ was 2.58 and Jʹ was 0.222 for the EQ-5D-5L, while Hʹ was 4.05 and Jʹ was 0.291 for the EQ-5D-5L + Fatigue. In the disease group Hʹ was 6.41 and Jʹ was 0.552 for the EQ-5D-5L and Hʹ was 7.90 and Jʹ was 0.567 for the EQ-5D-5L + Fatigue.

### Convergent validity

The Spearman’s rank correlation coefficient between the EQ-5D-5L (level sum score) and the EQ VAS was − 0.606 (strong), and − 0.621 (strong) between the EQ-5D-5L + Fatigue (level sum score) and the EQ VAS. In the diseased group these coefficients were − 0.331 (moderate), and − 0.369 (moderate) respectively. Correlations almost doubled in the diseased group: − 0.614 (strong) and − 0.637 (strong) respectively.

### Domain dependency

Table <a href="#Tab4" data-ref-type="table">4</a> shows the degree to which domains dominated each other. Severe/extreme problems on fatigue and no problems on other items were relatively common (5.5–20.1%), especially for no problems on self-care (20.1%) and mobility (12.4%). In contrast, no problems on fatigue and severe/extreme problems on other items were very uncommon (0.2–0.7%). Relative frequency analysis showed that the ratio of ‘fatigue level 4/5—other domain level 1’ and ‘other domains level 1—fatigue level 4/5’ was \> 1 for all five domains, indicating that the EQ-5D-5L domains are dominant over fatigue.

<div id="Tab4" class="table-wrap">

<div class="caption">

Combinations of extreme values of the EQ-5D-5L + Fatigue (no versus severe/extreme problems), in absolute numbers and expressed as the percentage of the total number of profiles

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Extreme problems (L4/L5)</th>
<th colspan="6" style="text-align: left;">No problems (L1)</th>
</tr>
<tr>
<th style="text-align: left;">Mobility</th>
<th style="text-align: left;">Self-care</th>
<th style="text-align: left;">Usual activities</th>
<th style="text-align: left;">Pain/discomfort</th>
<th style="text-align: left;">Anxiety/depression</th>
<th style="text-align: left;">Fatigue</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">41 (1.4%)</td>
<td style="text-align: left;">11 (0.4%)</td>
<td style="text-align: left;">9 (0.3%)</td>
<td style="text-align: left;">46 (1.5%)</td>
<td style="text-align: left;">17 (0.6%)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care</td>
<td style="text-align: left;">6 (0.2%)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">8 (0.3%)</td>
<td style="text-align: left;">6 (0.2%)</td>
<td style="text-align: left;">8 (0.3%)</td>
<td style="text-align: left;">6 (0.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities</td>
<td style="text-align: left;">16 (0.5%)</td>
<td style="text-align: left;">40 (1.3%)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">10 (0.3%)</td>
<td style="text-align: left;">26 (0.9%)</td>
<td style="text-align: left;">7 (0.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort</td>
<td style="text-align: left;">35 (1.2%)</td>
<td style="text-align: left;">124 (4.1%)</td>
<td style="text-align: left;">26 (0.9%)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">84 (2.8%)</td>
<td style="text-align: left;">22 (0.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression</td>
<td style="text-align: left;">56 (1.9%)</td>
<td style="text-align: left;">80 (2.6%)</td>
<td style="text-align: left;">22 (0.7%)</td>
<td style="text-align: left;">23 (0.8%)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9 (0.3%)</td>
</tr>
<tr>
<td style="text-align: left;">Fatigue</td>
<td style="text-align: left;">375 (12.4%)</td>
<td style="text-align: left;">608 (20.1%)</td>
<td style="text-align: left;">276 (9.1%)</td>
<td style="text-align: left;">165 (5.5%)</td>
<td style="text-align: left;">296 (9.8%)</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

### Explanatory power of the EQ-5D-5L with and without a fatigue item

Univariate analyses showed substantial impact of fatigue levels 4 (moderate fatigue) and 5 (severe fatigue) (Appendix 1). Table <a href="#Tab5" data-ref-type="table">5</a> shows the multivariable regression analyses (all respondents, and healthy and diseased respondents separately). In all respondents, 38.7% of the variance of the EQ VAS is explained by the five EQ-5D-5L domains. The addition of the fatigue item (41.6%) provided extra explanatory power. In respondents without a chronic health condition, the explained variance increased from 15.6 to 17.5% due to the addition of the fatigue item, whereas it increased from 35.5 to 39.6% in the disease group.

<div id="Tab5" class="table-wrap">

<div class="caption">

Explanatory power of multivariable models for the EQ VAS that include EQ-5D-5L domains with and without an extra fatigue item added

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Selection of EQ-5D-5L + Fatigue items</th>
<th style="text-align: left;">R<sup>2</sup></th>
<th style="text-align: left;">df</th>
<th style="text-align: left;">F-value</th>
<th style="text-align: left;"><em>p</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;"><em>Total sample</em></td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + AD</td>
<td>0.387</td>
<td style="text-align: left;">20</td>
<td>94.8</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC + UA + PD + AD + FA</td>
<td>0.410</td>
<td style="text-align: left;">20</td>
<td>104.3</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + UA + PD + AD + FA</td>
<td>0.413</td>
<td style="text-align: left;">20</td>
<td>105.7</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + PD + AD + FA</td>
<td>0.406</td>
<td style="text-align: left;">20</td>
<td>102.8</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + AD + FA</td>
<td>0.390</td>
<td style="text-align: left;">20</td>
<td>96.2</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + FA</td>
<td>0.397</td>
<td style="text-align: left;">20</td>
<td>98.8</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + AD + FA</td>
<td>0.416</td>
<td style="text-align: left;">24</td>
<td>89.0</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>Without chronic health condition</em></td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + AD</td>
<td>0.156</td>
<td style="text-align: left;">19</td>
<td>14.0</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC + UA + PD + AD + FA</td>
<td>0.167</td>
<td style="text-align: left;">18</td>
<td>16.0</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + UA + PD + AD + FA</td>
<td>0.175</td>
<td style="text-align: left;">20</td>
<td>15.2</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + PD + AD + FA</td>
<td>0.161</td>
<td style="text-align: left;">19</td>
<td>14.4</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + AD + FA</td>
<td>0.147</td>
<td style="text-align: left;">19</td>
<td>14.2</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + FA</td>
<td>0.149</td>
<td style="text-align: left;">19</td>
<td>13.2</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + AD + FA</td>
<td>0.175</td>
<td style="text-align: left;">23</td>
<td>13.2</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"><em>With chronic health condition</em></td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + AD</td>
<td>0.355</td>
<td style="text-align: left;">20</td>
<td>42.8</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC + UA + PD + AD + FA</td>
<td>0.382</td>
<td style="text-align: left;">19</td>
<td>50.7</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + UA + PD + AD + FA</td>
<td>0.392</td>
<td style="text-align: left;">20</td>
<td>50.0</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + PD + AD + FA</td>
<td>0.385</td>
<td style="text-align: left;">20</td>
<td>48.7</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + AD + FA</td>
<td>0.368</td>
<td style="text-align: left;">20</td>
<td>45.2</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + FA</td>
<td>0.378</td>
<td style="text-align: left;">20</td>
<td>47.1</td>
<td> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO + SC + UA + PD + AD + FA</td>
<td>0.396</td>
<td style="text-align: left;">24</td>
<td>42.3</td>
<td> &lt; 0.001</td>
</tr>
</tbody>
</table>

MO, mobility; SC, self-care; UA, Usual activities; PD, Pain/discomfort; AD, Anxiety/depression; FA, Fatigue

</div>

## Discussion

This study demonstrated, in a large sample of the general Dutch population, that an additional fatigue item provides additional information to the standard EQ-5D. As hypothesized, the ceiling effect decreased by adding the extra fatigue item and more information is captured. The extended EQ-5D-5L + Fatigue version was better able to differentiate between respondents compared to the EQ-5D-5L, especially between those with a chronic health condition. Severe/extreme fatigue problems were shown to be associated with a steep decrease in EQ VAS scores and convergent validity showed that the EQ-5D-5L + Fatigue is more strongly related to the EQ VAS compared to the EQ-5D-5L. Compared to the EQ-5D-5L domains, the extra fatigue item added most explanatory power, especially in the subgroup of respondents with a chronic health condition.

Our finding that fatigue provides additional information and is a candidate item to be added to the EQ-5D is in line with less elaborate previous studies that suggested to add a fatigue (or related) item to the EQ-5D \[15–17, 25, 26, 28, 43\]. Despite the use of different approaches, all showed that the EQ-5D would benefit from an additional fatigue or related item. These studies entailed related constructs: energy/sleep \[43\], fatigue \[15\], energy/fatigue \[17\], tiredness \[16, 25, 26\]. Only one study tested the psychometric gains of adding a fatigue item to the EQ-5D, demonstrating a decreased ceiling effect \[17\]. They also studied the explanatory power of adding the energy/fatigue item and showed that it added 5% to the EQ-5D-3L in a sample of the Swiss general population. When considering fatigue to add as a bolt-on item to the EQ-5D, it should be clarified what construct (i.e. energy, tiredness, fatigue) is best. An earlier study showed that energy was less important to add compared to hearing and cognition, though it is unclear whether this also applies when the construct fatigue is used \[44\]. Also, as the wording and terminology may have impact on the outcomes, this should be carefully investigated as well. If fatigue is added as a bolt-on item to the EQ-5D, an important next step is modelling the tariff of the EQ-5D to include the bolt-on item while not substantially altering the weighting system \[45\].

As fatigue is an important sequela of many chronic health conditions, we studied the potential gain of adding a fatigue item to the EQ-5D separately for the subgroups of respondents with and without a chronic health condition. As hypothesized, especially in the subgroup of respondents with a chronic health condition the extra fatigue item captures additional information and improves the coverage of HRQL. For all psychometric aspects studied, the gain of the extra fatigue item was substantially higher for the subgroup of respondents with a chronic health condition, particularly the informativity, convergent validity and the explanatory power. The explanatory power of the EQ-5D-5L increased with 0.9% in the subgroup without a chronic health condition versus 4.1% in the subgroup of respondents with a chronic health condition when the fatigue item was added.

This study included several strengths and limitations. One of the strengths was the large sample size that was representative of the Dutch population for age, sex and educational level. Another strength was the prevalence of having a chronic health condition, which was comparable to the Dutch population (52% vs. 58%) \[46\]. Other strengths included the ability to divide the sample in large subgroups with and without a chronic health condition facilitating the comparison of these subgroups, and the high prevalence and wide range of fatigue scores allowing to study the gain of adding a fatigue item to the EQ-5D-5L. A limitation was, however, the application of the RPQ fatigue item to assess fatigue. The RPQ has been developed for the assessment of post-concussion symptoms. It is not specifically developed for the assessment of fatigue in the general population. However, an earlier study showed the ability of the RPQ fatigue item to assess fatigue in a general population \[32\]. Another limitation was the slightly different phrasing of the timeframe (your health today vs. fatigue in the past 24 h). For future studies it is recommended to add fatigue as a sixth domain to the EQ-5D to study fatigue as a bolt-on item and overcome these issues when assessing the additional value of fatigue. It would also be interesting to study the added value of a fatigue bolt-on in populations with a specific condition for which fatigue is a major consequence \[21–24\]. Also, a limitation was the web-based form of the survey. By using this method, we were not aware of the characteristics of non-respondents, and we were consequently not able to study whether respondents differed from non-respondents.

## Conclusions

The present study showed that adding a fatigue item to the EQ-5D-5L improves the discriminatory power, informativity, convergent validity and explanatory power of the EQ-5D-5L. Effects are substantially larger in the subgroup of respondents with chronic health conditions, indicating that adding a fatigue item to the EQ-5D-5L is especially relevant in evaluating the HRQL of diseased people.

##### Appendix 1

See Table <a href="#Tab6" data-ref-type="table">6</a>.

<div id="Tab6" class="table-wrap">

<div class="caption">

Univariate analyses of the EQ VAS explained by the EQ-5D-5L and extra fatigue item

</div>

|                            | R-Square | Unstandardized B (95% CI)  | *p*-value |
|----------------------------|----------|----------------------------|-----------|
| Mobility level 2           | 0.044    |  − 10.4 (− 12.1 to − 8.7)  |  \< 0.001 |
| Mobility level 3           | 0.071    |  − 18.2 (− 20.5 to − 15.8) |  \< 0.001 |
| Mobility level 4           | 0.052    |  − 24.9 (− 28.6 to − 21.1) |  \< 0.001 |
| Mobility level 5           | 0.001    |  − 8.4 (− 16.6 to − 0.3)   | 0.043     |
| Self-care level 2          | 0.066    |  − 18.6 (− 21.5 to − 15.8) |  \< 0.001 |
| Self-care level 3          | 0.032    |  − 20.6 (− 24.6 to − 16.6) |  \< 0.001 |
| Self-care level 4          | 0.013    |  − 31.0 (− 40.4 to − 21.5) |  \< 0.001 |
| Self-care level 5          | 0.000    |  − 5.6 (− 14.8 to 3.6)     | 0.235     |
| Usual Activities level 2   | 0.044    |  − 9.9 (− 11.6 to − 8.3)   |  \< 0.001 |
| Usual Activities level 3   | 0.121    |  − 21.7 (− 23.8 to − 19.6) |  \< 0.001 |
| Usual Activities level 4   | 0.044    |  − 24.7 (− 28.8 to − 20.6) |  \< 0.001 |
| Usual Activities level 5   | 0.015    |  − 27.0 (− 34.9 to − 19.1) |  \< 0.001 |
| Pain/discomfort level 2    | 0.000    |  − 0.3 (− 1.1 to 1.7)      | 0.690     |
| Pain/discomfort level 3    | 0.071    |  − 14.0 (− 15.8 to − 12.2) |  \< 0.001 |
| Pain/discomfort level 4    | 0.129    |  − 26.9 (− 29.3 to − 24.4) |  \< 0.001 |
| Pain/discomfort level 5    | 0.026    |  − 29.2 (− 35.7 to − 22.8) |  \< 0.001 |
| Anxiety/depression level 2 | 0.027    |  − 7.5 (− 9.0 to − 5.9)    |  \< 0.001 |
| Anxiety/depression level 3 | 0.051    |  − 14.2 (− 16.4 to − 12.0) |  \< 0.001 |
| Anxiety/depression level 4 | 0.043    |  − 23.6 (− 27.6 to − 19.7) |  \< 0.001 |
| Anxiety/depression level 5 | 0.005    |  − 12.7 (− 19.0 to − 6.4)  |  \< 0.001 |
| Fatigue level 2            | 0.001    |  − 1.9 (− 0.03 to − 3.9)   | 0.052     |
| Fatigue level 3            | 0.000    |  − 0.6 (− 2.2 to 0.9)      | 0.413     |
| Fatigue level 4            | 0.041    |  − 10.1 (− 11.9 to − 8.4)  |  \< 0.001 |
| Fatigue level 5            | 0.137    |  − 23.7 (− 25.9 to − 21.6) |  \< 0.001 |

</div>

### Abbreviations

EQ VAS  
EQ-5D visual analogue scale

HRQL  
Health-related quality of life

L1-5  
Level 1–5

RPQ  
Rivermead Post-Concussion Symptoms Questionnaire

SD  
Standard deviation

### Acknowledgements

The views presented in this paper are the personal view of GJ Bonsel and MF Janssen, and do not reflect a view from the EuroQol Executive Office, or from the EuroQol Research Foundation.

### Authors' contributions

IS conceptualized and designed the study, analyzed and interpreted data, drafted the initial manuscript, and reviewed and revised the manuscript. GJB, SP, and MFJ conceptualized and designed the study, interpreted data, and reviewed and critically revised the manuscript. JAH conceptualized and designed the study, analyzed and interpreted data, and reviewed and critically revised the manuscript. All authors approved the final manuscript as submitted and agree to be accountable for all aspects of the work.

### Funding

This study was funded by EuroQol (grant number: 20180330).

### Availability of data and material

The datasets generated and/or analysed during the current study are not publicly available due to privacy/ethical restrictions but are available from the corresponding author on reasonable request.

### Declarations

#### Ethics approval

All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki declaration and its later amendments or comparable ethical standards.

#### Consent to participate

Informed consent was obtained from all individual participants included in the study.

#### Competing interests

The authors have no conflicts of interest to declare that are relevant to the content of this article.

## References

1. Fiteni F, Le Ray I, Ousmen A, Isambert N, Anota A, Bonnetain F. Health-related quality of life as an endpoint in oncology phase I trials: a systematic review. BMC Cancer. 2019;19(1):361. doi:10.1186/s12885-019-5579-3

2. Dellenmark-Blom M, Sjöström S, Abrahamsson K, Holmdahl G. Health-related quality of life among children, adolescents, and adults with bladder exstrophy–epispadias complex: a systematic review of the literature and recommendations for future research. Qual Life Res. 2019;28:1–24. doi:10.1007/s11136-019-02119-7

3. Spronk I, Legemate C, Oen I, van Loey NE, Polinder S, van Baar ME. Health related quality of life in adults after burn injuries: a systematic review. PLoS ONE. 2018;13(5):e0197507. doi:10.1371/journal.pone.0197507

4. Guyatt GH, Jaeschke R, Feeny DH, Patrick DL, Spilker B. Measurements in clinical trials: choosing the right approach. Quality of life and pharmacoeconomics in clinical trials. 1996:41–48. Philadelphia, Lippincott Williams & Wilkins.

5. Coons SJ, Rao S, Keininger DL, Hays RD. A comparative review of generic quality-of-life instruments. Pharmacoeconomics. 2000;17(1):13–35. doi:10.2165/00019053-200017010-00002

6. Mokkink LB, Terwee CB, Patrick DL, Alonso J, Stratford PW, Knol DL. The COSMIN study reached international consensus on taxonomy, terminology, and definitions of measurement properties for health-related patient-reported outcomes. J Clin Epidemiol. 2010;63(7):737–745. doi:10.1016/j.jclinepi.2010.02.006

7. EuroQol Research Foundation (2019) About the EQ-5D-3L. https://euroqol.org/eq-5d-instruments/eq-5d-3l-about/. Accessed 20 April 04 2019

8. Swinburn P, Lloyd A, Boye K, Edson-Heredia E, Bowman L, Janssen B. Development of a disease-specific version of the EQ-5D-5L for use in patients suffering from psoriasis: lessons learned from a feasibility study in the UK. Value Health. 2013;16(8):1156–1162. doi:10.1016/j.jval.2013.10.003

9. Rabin R, Charro FD. EQ-5D: a measure of health status from the EuroQol Group. Ann Med. 2001;33(5):337–343. doi:10.3109/07853890109002087

10. Linde L, Sørensen J, Østergaard M, Hørslev-Petersen K, Hetland ML. Health-related quality of life: validity, reliability, and responsiveness of SF-36, EQ-15D, EQ-5D, RAQoL, and HAQ in patients with rheumatoid arthritis. J Rheumatol. 2008;35(8):1528–1537.

11. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

12. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

13. Krabbe PF, Stouthard ME, Essink-Bot M-L, Bonsel GJ. The effect of adding a cognitive dimension to the EuroQol multiattribute health-status classification system. J Clin Epidemiol. 1999;52(4):293–301. doi:10.1016/S0895-4356(98)00163-2

14. Geraerds AJ, Bonsel GJ, Janssen MF, Finch AP, Polinder S, Haagsma JA. Methods used to identify, test, and assess impact on preferences of bolt-ons: a systematic review. Value Health. 2021;24:901–916. doi:10.1016/j.jval.2020.12.011

15. Efthymiadou O, Mossman J, Kanavos P. Health related quality of life aspects not captured by EQ-5D-5L: results from an international survey of patients. Health Policy. 2019;123(2):159–165. doi:10.1016/j.healthpol.2018.12.003

16. Shah K, Mulhern B, Longworth L, Janssen B (2016) Important aspects of health not captured by EQ-5D: views of the UK general public. Office of Health Economics10.1007/s40271-017-0240-128409481

17. Perneger TV, Courvoisier DS. Exploration of health dimensions to be included in multi-attribute health-utility assessment. Int J Qual Health Care. 2011;23(1):52–59. doi:10.1093/intqhc/mzq068

18. The EuroQol Group. EuroQol-a new facility for the measurement of health-related quality of life. Health Policy. 1990;16(3):199–208. doi:10.1016/0168-8510(90)90421-9

19. Brooks RG (2015) 28 years of the EuroQol Group: an overview. EuroQol Working Paper Series

20. Gudex C (2005) The descriptive system of the EuroQOL instrument. In: EQ-5D concepts and methods: a developmental history, pp 19–27. Springer

21. Fortier-Brochu É, Beaulieu-Bonneau S, Ivers H, Morin CM. Relations between sleep, fatigue, and health-related quality of life in individuals with insomnia. J Psychosom Res. 2010;69(5):475–483. doi:10.1016/j.jpsychores.2010.05.005

22. Rupp I, Boshuizen HC, Jacobi CE, Dinant HJ, van den Bos GA. Impact of fatigue on health-related quality of life in rheumatoid arthritis. Arthritis Rheum. 2004;51(4):578–585. doi:10.1002/art.20539

23. Kluthcovsky ACGC, Urbanetz AA, de Carvalho DS, Maluf EMCP, Sylvestre GCS, Hatschbach SBB. Fatigue after treatment in breast cancer survivors: prevalence, determinants and impact on health-related quality of life. Support Care Cancer. 2012;20(8):1901–1909. doi:10.1007/s00520-011-1293-7

24. Gold JI, Mahrer NE, Yee J, Palermo TM. Pain, fatigue and health-related quality of life in children and adolescents with chronic pain. Clin J Pain. 2009;25(5):407. doi:10.1097/AJP.0b013e318192bfb1

25. Yang Y, Rowen D, Brazier J, Tsuchiya A, Young T, Longworth L. An exploratory study to test the impact on three “bolt-on” items to the EQ-5D. Value Health. 2015;18(1):52–60. doi:10.1016/j.jval.2014.09.004

26. Longworth L, Yang Y, Young T, Mulhern B, Hernandez Alava M, Mukuria C et al (2014) Use of generic and condition-specific measures of health-related quality of life in NICE decision-making: a systematic review, statistical modelling and survey. Health Technol Assess10.3310/hta18090PMC478095424524660

27. Devlin NJ, Hansen P, Selai C. Understanding health state valuations: a qualitative analysis of respondents' comments. Qual Life Res. 2004;13(7):1265–1277. doi:10.1023/B:QURE.0000037495.00959.9b

28. Spronk I, Polinder S, Bonsel GJ, Janssen MF, Haagsma JA. The relation between EQ-5D and fatigue in a Dutch general population sample: an explorative study. Health Qual Life Outcomes. 2021. doi:10.1186/s12955-021-01771-3

29. van’t Leven M, Zielhuis GA, van der Meer JW, Verbeek AL, Bleijenberg G. Fatigue and chronic fatigue syndrome-like complaints in the general population. Eur J Public Health. 2010;20(3):251–257. doi:10.1093/eurpub/ckp113

30. Cullen W, Kearney Y, Bury G. Prevalence of fatigue in general practice. Ir J Med Sci. 2002;171(1):10. doi:10.1007/BF03168931

31. Basu N, Yang X, Luben RN, Whibley D, Macfarlane GJ, Wareham NJ. Fatigue is associated with excess mortality in the general population: results from the EPIC-Norfolk study. BMC Med. 2016;14(1):122. doi:10.1186/s12916-016-0662-y

32. Voormolen DC, Cnossen MC, Polinder S, Gravesteijn BY, Von Steinbuechel N, Real RGL. Prevalence of post-concussion-like symptoms in the general population in Italy, The Netherlands and the United Kingdom. Brain Inj. 2019;33:1–9. doi:10.1080/02699052.2019.1607557

33. Versteegh MM, Vermeulen KM, Evers SM, de Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi:10.1016/j.jval.2016.01.003

34. Brooks R, EuroQol Group. EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

35. King N, Crawford S, Wenden F, Moss N, Wade D. The Rivermead Post Concussion Symptoms Questionnaire: a measure of symptoms commonly experienced after head injury and its reliability. J Neurol. 1995;242(9):587–592. doi:10.1007/BF00868811

36. Janssen MFB, Birnie E, Bonsel GJ. Evaluating the discriminatory power of EQ-5D, HUI2 and HUI3 in a US general population survey using Shannon’s indices. Qual Life Res. 2007;16(5):895–904. doi:10.1007/s11136-006-9160-6

37. Devlin N, Parkin D, Janssen B. Methods for analysing and reporting EQ-5D data. 2020. Cham, Springer Nature.

38. Shannon CE. A mathematical theory of communication. Bell Syst Tech J. 1948;27(3):379–423. doi:10.1002/j.1538-7305.1948.tb01338.x

39. Pickard AS, De Leon MC, Kohlmann T, Cella D, Rosenbloom S. Psychometric comparison of the standard EQ-5D to a 5 level version in cancer patients. Med Care. 2007;45(3):259–263. doi:10.1097/01.mlr.0000254515.63841.81

40. Janssen M, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi:10.1007/s11136-012-0322-4

41. Cohen J. Statistical power analysis for the behavioral sciences. 2013. London, Routledge.

42. Ophuis RH, Janssen MF, Bonsel GJ, Panneman MJ, Polinder S, Haagsma JA. Health-related quality of life in injury patients: the added value of extending the EQ-5D-3L with a cognitive dimension. Qual Life Res. 2019;28(7):1941–1949. doi:10.1007/s11136-019-02156-2

43. Finch AP, Brazier JE, Mukuria C, Bjorner JB. An exploratory study on using principal-component analysis and confirmatory factor analysis to identify bolt-on dimensions: the EQ-5D case study. Value Health. 2017;20(10):1362–1375. doi:10.1016/j.jval.2017.06.002

44. Finch AP, Brazier J, Mukuria C. Selecting bolt-on dimensions for the EQ-5D: testing the impact of hearing, sleep, cognition, energy, and relationships on preferences using pairwise choices. Med Decis Mak. 2021;41(1):89–99. doi:10.1177/0272989X20969686

45. Yang Y, Brazier J, Tsuchiya A. Effect of adding a sleep dimension to the EQ-5D descriptive system: a “bolt-on” experiment. Med Decis Mak. 2014;34(1):42–53. doi:10.1177/0272989X13480428

46. Volksgezondheidenzorg.info (2020) Aantal mensen met chronische aandoening bekend bij de huisarts. https://www.volksgezondheidenzorg.info/onderwerp/chronische-ziekten-en-multimorbiditeit/cijfers-context/huidige-situatie#node-aantal-mensen-met-chronische-aandoening-bekend-bij-de-huisarts

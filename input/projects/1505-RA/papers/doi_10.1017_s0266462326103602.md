---
project_id: "1505-RA"
work_id: "doi:10.1017/s0266462326103602"
doi: "10.1017/S0266462326103602"
pmid: "41749053"
pmcid: "PMC13071849"
title: "What do HTA agencies need for generating health-related quality of life evidence? Findings from a global survey"
journal: "International Journal of Technology Assessment in Health Care"
publication_date: "2026-02-27"
volume: "42"
issue: "1"
authors:
  - name: "Annushiah Vasan Thakumar"
    affiliation_ids:
      - "aff1"
  - name: "Paula Lorgelly"
    affiliation_ids:
      - "aff2"
  - name: "Louise Longworth"
    affiliation_ids:
      - "aff3"
  - name: "Lucila Rey-Ares"
    affiliation_ids:
      - "aff4"
  - name: "Fredrick Purba"
    affiliation_ids:
      - "aff5"
  - name: "Dominik Golicki"
    affiliation_ids:
      - "aff6"
  - name: "Federico Augustovski"
    affiliation_ids:
      - "aff7"
  - name: "Kim Rand"
    affiliation_ids:
      - "aff8"
      - "aff9"
  - name: "Rosalie Viney"
    affiliation_ids:
      - "aff10"
  - name: "Nick Bansback"
    affiliation_ids:
      - "aff11"
  - name: "Nan Luo"
    affiliation_ids:
      - "aff12"
affiliations:
  - id: "aff1"
    name: "School of Pharmacy, Faculty of Health and Medical Sciences, Taylor’s University, Malaysia"
  - id: "aff2"
    name: "School of Population Health and Department of Economics, University of Auckland, New Zealand"
  - id: "aff3"
    name: "Arrow Health Economics, UK"
  - id: "aff4"
    name: "Patient and Health Impact, Pfizer Argentina, Argentina"
  - id: "aff5"
    name: "Department of Clinical and Health Psychology, Faculty of Psychology, Universitas Padjadjaran, Indonesia"
  - id: "aff6"
    name: "Department of Experimental and Clinical Pharmacology, Medical University of Warsaw, Poland"
  - id: "aff7"
    name: "Health Technology Assessment and Health Economics Department, Institute for Clinical Effectiveness (IECS-CONICETUBA), Argentina"
  - id: "aff8"
    name: "Health Services Research Unit, Akershus University Hospital, Lørenskog, Norway"
  - id: "aff9"
    name: "Maths in Health, Klimmen, The Netherlands"
  - id: "aff10"
    name: "Centre for Health Economics Research and Evaluation, University of Technology Sydney, Australia"
  - id: "aff11"
    name: "School of Population and Public Health, The University of British Columbia, Canada"
  - id: "aff12"
    name: "Saw Swee Hock School of Public Health, National University of Singapore, Singapore"
licence: "cc-by-nc-nd"
source_file: "input/projects/1505-RA/papers/doi_10.1017_s0266462326103602.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13071849/fullTextXML"
source_method: "epmc_xml"
source_sha256: "494d09880a686266c8f11352e37b8767c146b9c59c1d6885a71885a31dbc5724"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# What do HTA agencies need for generating health-related quality of life evidence? Findings from a global survey

## Abstract

### Objectives

The overall aim is to understand the practices, views, and needs of health technology assessment (HTA) practitioners worldwide regarding the use of health-related quality of life (HRQoL) data for generating cost-effectiveness evidence.

### Methods

We invited HTA practitioners in sixty countries to complete an online survey on their perspectives on the measurement and valuation of health. We performed descriptive analyses of the overall sample, examined response differences across six regions, and pooled responses to open-ended questions for content analysis.

### Results

A total of 238 individuals from 45 countries completed the survey, with a mean response number per country of 5.28 (SD: 4.45). Most responses came from public sector employees (seventy-two percent), and ninety percent were involved in cost-effectiveness-related work. The top three most frequently used utility instruments were EQ-5D, SF-6D, and EQ-5D-Y, and the elicitation methods were time trade-off, visual analogue scale, and standard gamble. Health-state preferences of the general public from another country were more frequently used than the preferences of the local public. Common data quality issues were poor sample representativeness and a small sample size of utility data. In Asia and Western Europe, the top-voted research priority was developing utility instruments that capture both healthcare and social care impact. In four regions, developing utility instruments for children was the second-highest research priority.

### Conclusions

The survey addressed important knowledge gaps regarding current practices in measuring and valuing HRQoL in HTA and provided insights into HTA practitioners’ views on instruments, methods, and data-related challenges and needs for generating HRQoL evidence.

**Keywords:** global survey, health technology assessment, health-related quality of life, health-state utility, HT A policy, MAUI, preference elicitation

Received 2025 Sep 7; Revised 2026 Jan 16; Accepted 2026 Feb 22; Collection date 2026.

## Introduction

Health technology assessments (HTA) provide a comprehensive framework for integrating evidence of economic, social, and health consequences into decision-making (1). Globally, healthcare systems increasingly rely on HTA to guide resource allocation (2–4). In HTA, cost-effectiveness analysis (CEA) of new health technologies using quality-adjusted life years (QALYs) as the health effects measure is the most recommended form of economic evaluation (2;5). However, estimating QALYs is technically challenging as it requires measuring and valuing patients’ health-related quality of life (HRQoL). Consequently, analysts often rely on HRQoL and health-state utility (HSU, valuation of HRQoL) data from the literature, which can be limited in both quantity and quality.

HSU data can be estimated directly by describing a specific health condition using vignettes and capturing preferences through elicitation methods such as the time trade-off (TTO) and discrete choice experiments (DCE). However, the indirect method of using standardized preference-weighted HRQoL instruments, or multi-attribute utility instruments (MAUIs) such as EQ-5D to obtain HSU data is more commonly used (6). In recent years, there has been significant progress in developing new methods and instruments for measuring and valuing HRQoL. For example, there is an increasing application of DCE in the valuation of HRQoL (7). Since DCE can be used in self-administered online surveys, it significantly lowers costs and shortens data collection timelines compared to traditional preference elicitation methods, which entail interviewer administration. Consequently, it has enabled more MAUIs to be developed, including disease-specific instruments such as the QLU-C10D and FACT-8D (8–10). Other examples include “bolt-on” research to enhance existing EQ-5D instruments (11;12) and the EQ-HWB instrument to broaden the ‘Q’ in QALY to cover both health and well-being (13). A bolt-on dimension refers to a supplementary item, or set of items, capturing specific aspects of health-related quality of life that may not be adequately represented by the original five dimensions of the EQ-5D instrument (14). Despite their attractive features, these new methods and instruments also have disadvantages. For instance, DCE and widely used traditional preference elicitation methods, such as TTO, have been shown to have poor agreement (15;16). Additionally, the primary challenge of DCEs arises during the analysis, as it requires careful assessment of whether respondents have completed the tasks appropriately. The use and testing of newer instruments may not be extensive, resulting in a lack of psychometric evidence and utility weights to inform decision-making. Given the wide range of methods and instruments available, and the proliferation of new ones, it remains unclear how existing instruments and methods are being used, and whether or when the new ones will be adopted by HTA practitioners for routine use.

HTA agencies or bodies (hereafter referred to as ‘HTA agencies’ for simplicity) are authoritative entities or divisions responsible for HTA evidence assessment and/or appraisal of health technologies. Although their size, capacity, and mandate vary, HTA agencies play a pivotal role in using HTA evidence to inform healthcare decisions. Moreover, because of their authority, HTA agencies’ practices and views on evidence generation methods significantly influence practice and therefore, are highly valuable to researchers. One source of information for understanding HTA agencies’ views and preferences is the methods guide they publish (17). However, this approach is suboptimal, particularly if the interest concerns HRQoL measurement and valuation methods. First, published methods guides may become outdated as practices and views continuously evolve, yet these guides are not updated frequently. Second, the guides for certain methodological aspects may be ambiguous or missing. Third, some recommendations in methods guides may not reflect unanimous opinions within HTA agencies. Last but not least, the absence of published methods guides by many HTA agencies limits their use as a resource for understanding these agencies’ practices.

An alternative way to understand HTA agencies’ views and preferences regarding HRQoL measurement and valuation is to survey HTA agency personnel responsible for preparing or reviewing HTA dossiers. This approach offers the advantage of obtaining first-hand, contemporary, and detailed information, which could be very useful for HRQoL researchers to set their priorities. However, to the best of our knowledge, such an approach has not been explored before. Our primary objective was to understand HTA practitioners’ views on and needs for HRQoL-related methods and instruments. Our secondary objective was to understand their current practices and views on the availability and quality of HRQoL data and research priorities.

## Methods

We conducted a cross-sectional online survey of HTA agency personnel from April 2023 to January 2024. In order to achieve broad geographic coverage of this hard-to-reach population, we used purposive sampling and invited survey respondents through the professional networks of the diverse international study team. The study received ethics approval from the Institutional Review Board of National University of Singapore (IRB number: NUS-IRB-2022–426).

### Sampling and recruitment design

We employed a two-stage recruitment procedure. In the first stage, we identified target HTA agencies, defined as independent organizations or governmental divisions authorized to generate and/or review HTA evidence for market access or reimbursement decisions at the health system level. We targeted surveying HTA agencies in fifty countries. We used the search strategy adopted by Kennedy-Martin et al., who identified forty-six countries with existing HTA agencies in 2019 (18). We complemented this strategy with other sources, including the Gear4Health database (19), ISPOR’s Pharmacoeconomic Guidelines Around the World database (17), the WHO Health Technology Assessment and Health Benefit Package Survey 2020/2021 webpage (4), the INAHTA Members List (20), and consulted with EuroQol Group members and colleagues for additional input.

In the second stage, we identified members of the EuroQol Group or their acquaintances as recruiters for the countries we intended to survey. Recruiters sent invitations with country-specific survey links to potential respondents working in the target HTA agencies. Alternatively, they identified a contact person within each HTA agency to extend the survey invitations internally. A survey administrator monitored survey yields and prompted recruiters and/or contact persons to send reminders to potential respondents weekly for at least three consecutive weeks after the survey commenced in each country.

### Participants

Rather than surveying official representatives of the target agencies, we sought to recruit all personnel involved in handling CUA or HRQoL evidence, specifically, individuals responsible for reviewing, generating, and/or using QALY-based evidence. Additionally, those involved in HTA-related work but not directly handling QALY-related tasks were also invited to participate if interested.

The inclusion criteria for the survey were: 1) being an employee of an HTA agency (e.g., governmental or public agency, division, body, or committee) whose agency responsibilities included evaluating or appraising health technologies for the purpose of listing/delisting, reimbursement, or pricing/repricing at the national level, or being a contracted professional, consultant, or advisor to such HTA organization(s); 2) being able to understand the English survey form and complete open-ended questions in their language of choice; and 3) providing informed consent.

### Survey form

After obtaining consent, participants were invited to complete an electronic survey form powered by Qualtrics anonymously at their convenience. The survey form was developed by the study team, aiming to create a short survey that can be self-completed by most respondents in no more than 20 minutes. An iterative question drafting procedure was used, with multiple rounds of pilot-testing conducted with personnel from HTA agencies in Singapore, Indonesia, Canada, England, Norway, Australia, New Zealand, Colombia, and Argentina until the development goal was achieved.

The final survey started off with screening questions followed by a consent-taking question. Eligible and consenting participants were invited to complete six sections of questions revolving around their experience with and opinions on Utility Instruments, Elicitation Methods, Data Source, Data Quality and Appropriateness, and Research Topics of Importance. Further information on the survey form can be found in the [Supplementary Material](http://doi.org/10.1017/S0266462326103602).

We used a four-point Likert-type response scale to assess frequency in Sections One to Four (“never”/ “not sure,” “occasionally,” “often,” and “very often”). In Sections One to Five, text fields were provided for respondents to explain their responses and elaborate on other methods, instruments, concerns, or research topics not covered in the survey.

### Statistical analysis

Descriptive analyses were performed for responses to closed-ended survey questions. For Likert-type questions in Sections One to Four, we first used the mode (or median if no or multiple modes were present) as the summary of the responses for each country, and then used the median of relevant country summaries as the summary of the responses for six regions (Commonwealth – Australia/Canada/New Zealand/United Kingdom, Western Europe, Central/Eastern Europe, Asia, Latin America, and Middle East/Africa).

To analyze the nominated research priorities in Section Five, we calculated a country-specific importance score for each research topic by averaging the scores from all respondents in the relevant country. Once the importance scores for all countries were available, a regional score was calculated by averaging scores from relevant countries in the region and a global score was calculated by averaging the regional scores. More information on how respondent-level scores were assigned is provided in the [Supplementary Material](http://doi.org/10.1017/S0266462326103602).

All statistical analysis was performed using STATA v14 (StataCorp, College Station, TX, USA). All qualitative responses to the open-ended questions were collated and systematically reviewed. Non-English responses were translated using a forward-backward approach. We then undertook a structured content analysis, involving iterative coding and categorization of the data, to identify recurrent themes, underlying concepts, and salient patterns across respondents. This analytic approach facilitated a deeper understanding of the key issues raised by participants and allowed us to synthesize their viewpoints into coherent thematic domains (21).

## Results

### Sample characteristics

Of the sixty countries enlisted and approached, the survey was distributed in forty-nine countries. The remaining eleven countries were excluded for various reasons, including non-responsiveness (*N* = 2), infancy of HTA (*N* = 2), or the non-use of CUA (*N* = 3), declination/technical difficulty (*N* = 2), or political turmoil (*N* = 2). In forty-five of these countries, we received at least one completed survey (median: 4; interquartile range: 2 to 6), while in the remaining four countries, there were zero responses despite multiple follow-ups. [Supplementary Table 1](http://doi.org/10.1017/S0266462326103602) outlines the distribution of responses and reasons for non-responses from the eleven countries approached. In total, 238 individuals in 45 countries and 65 HTA agencies completed and submitted the survey (<a href="#tab1" data-ref-type="table">Table 1</a> and [Supplementary Table 1](http://doi.org/10.1017/S0266462326103602)). Overall, the majority of the responses came from public sector employees (71.9 percent) and had at least four years of experience in HTA work (58.8 percent). Additionally, 81.1 percent of the respondents reported the presence of QALY estimation guidance in their work setting, and 89.5 percent were involved in QALY-related work responsibilities. More than half (61.3 percent) reviewed QALY-based cost-effectiveness evidence submitted by industry or contractors, and 91.2 percent performed HTA work at the national level. Of the 238 respondents surveyed, 25 did not have work responsibilities related to reviewing, generating, and/or using QALY-based cost-effectiveness evidence. These respondents mainly came from Vietnam (*N* = 10), Slovenia (*N* = 3), Austria (*N* = 2), Colombia (*N* = 2), and South Africa (*N* = 2).

<div id="tab1" class="table-wrap">

<div class="caption">

Characteristics of respondents (*N* = 238)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="6" style="text-align: center;">Region, <em>n</em>(%)</th>
<th rowspan="2" style="text-align: center;">Total, <em>n</em>(%)</th>
</tr>
<tr>
<th style="text-align: center;">Common-wealth</th>
<th style="text-align: center;">Western Europe</th>
<th style="text-align: center;">Central/ Eastern Europe</th>
<th style="text-align: center;">Asia</th>
<th style="text-align: center;">Latin America</th>
<th style="text-align: center;">Middle East/ Africa</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8" style="text-align: left;">Public sector employee</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">21 (61.8)</td>
<td style="text-align: center;">24 (77.4)</td>
<td style="text-align: center;">19 (76.0)</td>
<td style="text-align: center;">77 (81.1)</td>
<td style="text-align: center;">20 (52.6)</td>
<td style="text-align: center;">10 (66.7)</td>
<td style="text-align: center;">171 (71.9)</td>
</tr>
<tr>
<td style="text-align: left;">   No</td>
<td style="text-align: center;">13 (35.2)</td>
<td style="text-align: center;">7 (22.6)</td>
<td style="text-align: center;">6 (24.0)</td>
<td style="text-align: center;">18 (19.0)</td>
<td style="text-align: center;">18 (47.4)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">67 (28.2)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Contracted professional</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">17 (50.0)</td>
<td style="text-align: center;">14 (45.2)</td>
<td style="text-align: center;">8 (32.0)</td>
<td style="text-align: center;">33 (34.7)</td>
<td style="text-align: center;">26 (68.4)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">103 (43.3)</td>
</tr>
<tr>
<td style="text-align: left;">   No</td>
<td style="text-align: center;">17 (50.0)</td>
<td style="text-align: center;">17 (54.8)</td>
<td style="text-align: center;">17 (68.0)</td>
<td style="text-align: center;">62 (65.3)</td>
<td style="text-align: center;">12 (31.6)</td>
<td style="text-align: center;">10 (66.7)</td>
<td style="text-align: center;">135 (56.7)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Experience with HTA (years)</td>
</tr>
<tr>
<td style="text-align: left;">   Less than a year</td>
<td style="text-align: center;">3 (8.8)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">6 (24.0)</td>
<td style="text-align: center;">31 (32.6)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">49 (20.6)</td>
</tr>
<tr>
<td style="text-align: left;">   1–3 years</td>
<td style="text-align: center;">6 (17.7)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">7 (28.0)</td>
<td style="text-align: center;">19 (20.0)</td>
<td style="text-align: center;">12 (31.6)</td>
<td style="text-align: center;">2 (13.3)</td>
<td style="text-align: center;">49 (20.6)</td>
</tr>
<tr>
<td style="text-align: left;">   4–6 years</td>
<td style="text-align: center;">7 (20.6)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">9 (9.5)</td>
<td style="text-align: center;">9 (23.7)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">30 (12.6)</td>
</tr>
<tr>
<td style="text-align: left;">   7–9 years</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (4.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">10 (4.2)</td>
</tr>
<tr>
<td style="text-align: left;">   10 years or more</td>
<td style="text-align: center;">18 (52.9)</td>
<td style="text-align: center;">22 (71.0)</td>
<td style="text-align: center;">9 (36.0)</td>
<td style="text-align: center;">29 (30.5)</td>
<td style="text-align: center;">15 (39.5)</td>
<td style="text-align: center;">7 (46.7)</td>
<td style="text-align: center;">100 (42.0)</td>
</tr>
<tr>
<td style="text-align: left;">Gender</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   Female</td>
<td style="text-align: center;">17 (51.5)</td>
<td style="text-align: center;">23 (74.2)</td>
<td style="text-align: center;">17 (70.8)</td>
<td style="text-align: center;">55 (57.9)</td>
<td style="text-align: center;">17 (44.7)</td>
<td style="text-align: center;">7 (46.7)</td>
<td style="text-align: center;">136 (57.6)</td>
</tr>
<tr>
<td style="text-align: left;">   Male</td>
<td style="text-align: center;">16 (48.5)</td>
<td style="text-align: center;">8 (25.8)</td>
<td style="text-align: center;">7 (29.2)</td>
<td style="text-align: center;">40 (42.1)</td>
<td style="text-align: center;">21 (55.3)</td>
<td style="text-align: center;">8 (53.3)</td>
<td style="text-align: center;">100 (42.4)</td>
</tr>
<tr>
<td style="text-align: left;">Age group (years)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   ≤ 25</td>
<td style="text-align: center;">1 (2.94)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (0.4)</td>
</tr>
<tr>
<td style="text-align: left;">   26–35</td>
<td style="text-align: center;">10 (29.4)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">9 (36.0)</td>
<td style="text-align: center;">34 (35.8)</td>
<td style="text-align: center;">8 (21.1)</td>
<td style="text-align: center;">2 (13.3)</td>
<td style="text-align: center;">66 (27.7)</td>
</tr>
<tr>
<td style="text-align: left;">   36–45</td>
<td style="text-align: center;">9 (26.5)</td>
<td style="text-align: center;">8 (25.8)</td>
<td style="text-align: center;">6 (24.0)</td>
<td style="text-align: center;">39 (41.1)</td>
<td style="text-align: center;">11 (29.0)</td>
<td style="text-align: center;">4 (26.7)</td>
<td style="text-align: center;">77 (32.4)</td>
</tr>
<tr>
<td style="text-align: left;">   46–55</td>
<td style="text-align: center;">9 (26.5)</td>
<td style="text-align: center;">14 (45.2)</td>
<td style="text-align: center;">6 (24.0)</td>
<td style="text-align: center;">17 (17.9)</td>
<td style="text-align: center;">13 (34.2)</td>
<td style="text-align: center;">8 (53.3)</td>
<td style="text-align: center;">67 (28.2)</td>
</tr>
<tr>
<td style="text-align: left;">   56–65</td>
<td style="text-align: center;">5 (14.7)</td>
<td style="text-align: center;">6 (19.4)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">3 (3.2)</td>
<td style="text-align: center;">5 (13.2)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">22 (9.2)</td>
</tr>
<tr>
<td style="text-align: left;">   ≥ 66</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">2 (2.1)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">5 (2.1)</td>
</tr>
<tr>
<td style="text-align: left;">Education attainment</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   Bachelors</td>
<td style="text-align: center;">2 (5.9)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">11 (11.6)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">14 (5.9)</td>
</tr>
<tr>
<td style="text-align: left;">   Masters</td>
<td style="text-align: center;">15 (44.1)</td>
<td style="text-align: center;">7 (22.6)</td>
<td style="text-align: center;">12 (48.0)</td>
<td style="text-align: center;">38 (40.0)</td>
<td style="text-align: center;">24 (63.2)</td>
<td style="text-align: center;">4 (26.7)</td>
<td style="text-align: center;">100 (42.0)</td>
</tr>
<tr>
<td style="text-align: left;">   Doctorate</td>
<td style="text-align: center;">17 (50.0)</td>
<td style="text-align: center;">24 (77.4)</td>
<td style="text-align: center;">13 (52.0)</td>
<td style="text-align: center;">46 (48.4)</td>
<td style="text-align: center;">14 (36.8)</td>
<td style="text-align: center;">9 (60.0)</td>
<td style="text-align: center;">123 (51.7)</td>
</tr>
<tr>
<td style="text-align: left;">   Decline to disclose</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">1 (0.4)</td>
</tr>
<tr>
<td style="text-align: left;">Professional identity</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   Health economist</td>
<td style="text-align: center;">31 (91.2)</td>
<td style="text-align: center;">21 (67.7)</td>
<td style="text-align: center;">9 (36.0)</td>
<td style="text-align: center;">29 (30.5)</td>
<td style="text-align: center;">19 (50.0)</td>
<td style="text-align: center;">9 (60.0)</td>
<td style="text-align: center;">118 (50.0)</td>
</tr>
<tr>
<td style="text-align: left;">   Pharmacist</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (3.2)</td>
<td style="text-align: center;">9 (36.0)</td>
<td style="text-align: center;">26 (27.4)</td>
<td style="text-align: center;">3 (7.9)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">40 (16.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Public health workforce</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">4 (12.9)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">21 (22.1)</td>
<td style="text-align: center;">6 (15.8)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">34 (14.3)</td>
</tr>
<tr>
<td style="text-align: left;">   Clinician/Medical doctor</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (3.2)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">2 (2.1)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">2 (13.3)</td>
<td style="text-align: center;">9 (3.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Epidemiologist</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">3 (3.16)</td>
<td style="text-align: center;">6 (15.8)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">9 (3.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Statistician</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">1 (3.2)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">4 (4.21)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">5 (2.1)</td>
</tr>
<tr>
<td style="text-align: left;">   Other</td>
<td style="text-align: center;">3 (8.8)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">1 (4.0)</td>
<td style="text-align: center;">10 (10.5)</td>
<td style="text-align: center;">3 (7.8)</td>
<td style="text-align: center;">3 (20.0)</td>
<td style="text-align: center;">23 (9.7)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Presence of QALY estimation guidance</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">31 (91.2)</td>
<td style="text-align: center;">28 (90.3)</td>
<td style="text-align: center;">17 (68.0)</td>
<td style="text-align: center;">85 (89.5)</td>
<td style="text-align: center;">21 (55.3)</td>
<td style="text-align: center;">11 (73.3)</td>
<td style="text-align: center;">193 (81.1)</td>
</tr>
<tr>
<td style="text-align: left;">   No</td>
<td style="text-align: center;">3 (8.8)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">8 (32.0)</td>
<td style="text-align: center;">10 (10.5)</td>
<td style="text-align: center;">17 (44.7)</td>
<td style="text-align: center;">4 (26.7)</td>
<td style="text-align: center;">45 (18.9)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">QALY-based responsibilities</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">33 (97.1)</td>
<td style="text-align: center;">27 (87.1)</td>
<td style="text-align: center;">22 (88.0)</td>
<td style="text-align: center;">84 (88.4)</td>
<td style="text-align: center;">34 (89.5)</td>
<td style="text-align: center;">13 (86.7)</td>
<td style="text-align: center;">213 (89.5)</td>
</tr>
<tr>
<td style="text-align: left;">   No</td>
<td style="text-align: center;">1 (2.9)</td>
<td style="text-align: center;">4 (12.9)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">11 (11.6)</td>
<td style="text-align: center;">4 (10.5)</td>
<td style="text-align: center;">2 (13.3)</td>
<td style="text-align: center;">25 (10.5)</td>
</tr>
<tr>
<td style="text-align: left;">Role</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   Review Industry</td>
<td style="text-align: center;">31 (91.2)</td>
<td style="text-align: center;">17 (54.8)</td>
<td style="text-align: center;">18 (72.0)</td>
<td style="text-align: center;">52 (54.7)</td>
<td style="text-align: center;">17 (44.7)</td>
<td style="text-align: center;">11 (73.3)</td>
<td style="text-align: center;">146 (61.3)</td>
</tr>
<tr>
<td style="text-align: left;">   Review Public</td>
<td style="text-align: center;">13 (38.2)</td>
<td style="text-align: center;">17 (54.8)</td>
<td style="text-align: center;">9 (36.0)</td>
<td style="text-align: center;">47 (49.5)</td>
<td style="text-align: center;">22 (57.9)</td>
<td style="text-align: center;">8 (53.3)</td>
<td style="text-align: center;">116 (48.7)</td>
</tr>
<tr>
<td style="text-align: left;">   Primary study</td>
<td style="text-align: center;">17 (50.0)</td>
<td style="text-align: center;">10 (32.3)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">34 (35.8)</td>
<td style="text-align: center;">8 (21.1)</td>
<td style="text-align: center;">6 (40.0)</td>
<td style="text-align: center;">77 (32.4)</td>
</tr>
<tr>
<td style="text-align: left;">   Recommend method</td>
<td style="text-align: center;">9 (26.5)</td>
<td style="text-align: center;">7 (22.6)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">12 (12.6)</td>
<td style="text-align: center;">5 (13.2)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">40 (16.8)</td>
</tr>
<tr>
<td style="text-align: left;">   None of the above</td>
<td style="text-align: center;">1 (2.9)</td>
<td style="text-align: center;">4 (12.9)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">8 (21.1)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">23 (9.7)</td>
</tr>
<tr>
<td style="text-align: left;">Level of HTA work</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   National</td>
<td style="text-align: center;">33 (97.1)</td>
<td style="text-align: center;">30 (96.8)</td>
<td style="text-align: center;">25 (100)</td>
<td style="text-align: center;">89 (93.7)</td>
<td style="text-align: center;">30 (79.0)</td>
<td style="text-align: center;">10 (66.7)</td>
<td style="text-align: center;">217 (91.2)</td>
</tr>
<tr>
<td style="text-align: left;">   Regional provincial or state-level</td>
<td style="text-align: center;">3 (8.8)</td>
<td style="text-align: center;">9 (29.0)</td>
<td style="text-align: center;">1 (4.0)</td>
<td style="text-align: center;">15 (15.9)</td>
<td style="text-align: center;">3 (7.9)</td>
<td style="text-align: center;">6 (40.0)</td>
<td style="text-align: center;">37 (15.6)</td>
</tr>
<tr>
<td style="text-align: left;">   Hospital</td>
<td style="text-align: center;">1 (2.9)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">7 (18.4)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">21 (8.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Health plan</td>
<td style="text-align: center;">1 (2.9)</td>
<td style="text-align: center;">5 (16.1)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">13 (13.7)</td>
<td style="text-align: center;">6 (15.8)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">32 (13.5)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Health technology appraised</td>
</tr>
<tr>
<td style="text-align: left;">   Pharmaceuticals</td>
<td style="text-align: center;">34 (100)</td>
<td style="text-align: center;">23 (74.2)</td>
<td style="text-align: center;">23 (92.0)</td>
<td style="text-align: center;">72 (75.8)</td>
<td style="text-align: center;">35 (92.1)</td>
<td style="text-align: center;">12 (80.0)</td>
<td style="text-align: center;">199 (83.6)</td>
</tr>
<tr>
<td style="text-align: left;">   Medical devices</td>
<td style="text-align: center;">17 (50.0)</td>
<td style="text-align: center;">18 (58.1)</td>
<td style="text-align: center;">8 (32.0)</td>
<td style="text-align: center;">39 (41.1)</td>
<td style="text-align: center;">23 (60.5)</td>
<td style="text-align: center;">9 (60.0)</td>
<td style="text-align: center;">114 (47.9)</td>
</tr>
<tr>
<td style="text-align: left;">   Vaccines</td>
<td style="text-align: center;">10 (29.4)</td>
<td style="text-align: center;">15 (48.4)</td>
<td style="text-align: center;">6 (24.0)</td>
<td style="text-align: center;">29 (30.5)</td>
<td style="text-align: center;">20 (52.6)</td>
<td style="text-align: center;">6 (40.0)</td>
<td style="text-align: center;">86 (36.1)</td>
</tr>
<tr>
<td style="text-align: left;">   Diagnostics</td>
<td style="text-align: center;">14 (41.2)</td>
<td style="text-align: center;">17 (54.8)</td>
<td style="text-align: center;">4 (16.0)</td>
<td style="text-align: center;">25 (26.3)</td>
<td style="text-align: center;">22 (57.9)</td>
<td style="text-align: center;">6 (40.0)</td>
<td style="text-align: center;">88 (37.0)</td>
</tr>
<tr>
<td style="text-align: left;">   Surgical procedures</td>
<td style="text-align: center;">11 (32.4)</td>
<td style="text-align: center;">19 (61.3)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">18 (19.0)</td>
<td style="text-align: center;">10 (26.3)</td>
<td style="text-align: center;">4 (26.7)</td>
<td style="text-align: center;">64 (26.9)</td>
</tr>
<tr>
<td style="text-align: left;">   Public health professionals</td>
<td style="text-align: center;">3 (8.8)</td>
<td style="text-align: center;">11 (35.5)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">23 (24.2)</td>
<td style="text-align: center;">5 (13.2)</td>
<td style="text-align: center;">2 (13.3)</td>
<td style="text-align: center;">47 (19.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Other</td>
<td style="text-align: center;">2 (5.9)</td>
<td style="text-align: center;">6 (19.4)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">9 (9.5)</td>
<td style="text-align: center;">2 (5.3)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">22 (9.2)</td>
</tr>
<tr>
<td style="text-align: left;">Therapeutic area</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">   Oncology</td>
<td style="text-align: center;">26 (76.5)</td>
<td style="text-align: center;">14 (45.2)</td>
<td style="text-align: center;">19 (76.0)</td>
<td style="text-align: center;">67 (70.5)</td>
<td style="text-align: center;">29 (76.3)</td>
<td style="text-align: center;">12 (80.0)</td>
<td style="text-align: center;">167 (70.2)</td>
</tr>
<tr>
<td style="text-align: left;">   Cardiovascular Disease</td>
<td style="text-align: center;">16 (47.1)</td>
<td style="text-align: center;">15 (48.4)</td>
<td style="text-align: center;">19 (76.0)</td>
<td style="text-align: center;">40 (42.1)</td>
<td style="text-align: center;">16 (42.1)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">111 (46.6)</td>
</tr>
<tr>
<td style="text-align: left;">   Diabetes/ Hypertension/Dyslipidaemia</td>
<td style="text-align: center;">9 (26.5)</td>
<td style="text-align: center;">12 (38.7)</td>
<td style="text-align: center;">11 (44.0)</td>
<td style="text-align: center;">43 (45.3)</td>
<td style="text-align: center;">13 (34.2)</td>
<td style="text-align: center;">7 (46.7)</td>
<td style="text-align: center;">95 (39.9)</td>
</tr>
<tr>
<td style="text-align: left;">   Respiratory Disease</td>
<td style="text-align: center;">9 (26.5)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">21 (22.1)</td>
<td style="text-align: center;">6 (15.8)</td>
<td style="text-align: center;">3 (20.0)</td>
<td style="text-align: center;">42 (17.7)</td>
</tr>
<tr>
<td style="text-align: left;">   Musculoskeletal/ Rheumatology</td>
<td style="text-align: center;">8 (23.5)</td>
<td style="text-align: center;">8 (25.8)</td>
<td style="text-align: center;">6 (24.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">11 (29.0)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">40 (16.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Gynaecology/Obstetrics</td>
<td style="text-align: center;">1 (2.9)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">1 (4.0)</td>
<td style="text-align: center;">6 (6.3)</td>
<td style="text-align: center;">3 (7.9)</td>
<td style="text-align: center;">3 (20.0)</td>
<td style="text-align: center;">17 (7.1)</td>
</tr>
<tr>
<td style="text-align: left;">   Infections Disease/ HIV/ AIDS</td>
<td style="text-align: center;">1 (2.9)</td>
<td style="text-align: center;">6 (19.4)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">17 (17.9)</td>
<td style="text-align: center;">10 (26.3)</td>
<td style="text-align: center;">6 (40.0)</td>
<td style="text-align: center;">40 (16.8)</td>
</tr>
<tr>
<td style="text-align: left;">   Neurology</td>
<td style="text-align: center;">6 (17.7)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">7 (18.4)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">30 (12.6)</td>
</tr>
<tr>
<td style="text-align: left;">   Psychiatric Disorders/ Substance Abuse</td>
<td style="text-align: center;">2 (5.9)</td>
<td style="text-align: center;">6 (19.4)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">1 (6.7)</td>
<td style="text-align: center;">20 (8.4)</td>
</tr>
<tr>
<td style="text-align: left;">   Gastrointestinal Disease</td>
<td style="text-align: center;">7 (20.6)</td>
<td style="text-align: center;">4 (12.9)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">4 (10.5)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">22 (9.2)</td>
</tr>
<tr>
<td style="text-align: left;">   Endocrine</td>
<td style="text-align: center;">4 (11.8)</td>
<td style="text-align: center;">2 (6.5)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">3 (7.9)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">19 (8.0)</td>
</tr>
<tr>
<td style="text-align: left;">   Surgery/Transplantation</td>
<td style="text-align: center;">2 (5.9)</td>
<td style="text-align: center;">4 (12.9)</td>
<td style="text-align: center;">1 (4.0)</td>
<td style="text-align: center;">6 (6.3)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">14 (5.9)</td>
</tr>
<tr>
<td style="text-align: left;">   Urology/Nephrology</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">4 (12.9)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">7 (7.4)</td>
<td style="text-align: center;">2 (5.3)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">15 (6.3)</td>
</tr>
<tr>
<td style="text-align: left;">   Dermatology</td>
<td style="text-align: center;">5 (14.7)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">0 (0)</td>
<td style="text-align: center;">2 (2.1)</td>
<td style="text-align: center;">1 (2.6)</td>
<td style="text-align: center;">3 (20.0)</td>
<td style="text-align: center;">14 (5.9)</td>
</tr>
</tbody>
</table>

*Note*: *Government employee:* In terms of employment type, the respondent is an employee of a governmental or public agency, division, body, or committee whose responsibilities include evaluation or appraisal of health technologies for the purpose of listing/delisting, reimbursement, or pricing/repricing at the national level; *Contracted professional:* The respondent is a contracted professional, consultant, or advisor of the above-mentioned HTA organisation(s); *QALY-based Responsibilities:* The respondents’ responsibilities in the above work include reviewing, generating, and/or using QALY-based cost-effectiveness evidence; *Role*: Review Industry: I review QALY-based cost-effectiveness evidence submitted by industry or contractors; Review Public: I review publicly available QALY-based cost-effectiveness evidence; Primary study: I conduct primary studies to generate QALY-based cost-effectiveness evidence; Recommend method: I develop or recommend methods for generating QALY-based cost-effectiveness evidence; I do none of the above. One person from the Commonwealth and Central/ Eastern Europe each did not disclose their gender; *Health technology appraised:* Public health professionals refer to appraisals in which workforce capacity or staffing models constituted the object of comparison.

Total number of responses from each region and country: Asia = 95 (China:4, India:5, Indonesia:6, Japan:3, Malaysia:9, Philippines:3, Singapore:15, South Korea:16, Taiwan:11, Thailand:5, Vietnam:18), Central/Eastern Europe = 25 (Bulgaria:6, Croatia:1, Czech Republic:1, Estonia:1, Hungary:5, Latvia:1, Poland:3, Romania:1, Slovenia:6), Western Europe = 31 (Austria:3, Denmark:4, Italy:2, Netherlands:6, Portugal:6, Spain:7, Sweden:3), Latin America = 38 (Argentina:2, Brazil:10, Chile:3, Colombia:12, Ecuador:6, Mexico:3, Peru:2), Middle East/ Africa = 15 (Egypt:2, Saudi Arabia:1, South Africa:5, Tunisia:3, UAE:4), Commonwealth = 34 (Australia:7, Canada:4, England:17, New Zealand:4, Scotland:1, Wales:1).

</div>

### Use and importance of utility instruments

Overall, the top three most frequently used utility instruments by HTA practitioners involved with QALY-related work (*n* = 213) were the EQ-5D (“very often”), SF-6D (“occasionally”), and EQ-5D-Y (“occasionally”) (<a href="#tab2" data-ref-type="table">Table 2</a>). Other instruments respondents have come across during their HTA-related work are listed in [Supplementary Table 2](http://doi.org/10.1017/S0266462326103602). Regionally, the use frequency trend was consistent with a few exceptions. In Western Europe, the use frequency for the EQ-5D-Y was “never,” while in Latin America, it was “often” for SF-6D ([Supplementary Table 3](http://doi.org/10.1017/S0266462326103602)).

<div id="tab2" class="table-wrap">

<div class="caption">

Median (IQR) responses by region

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="6" style="text-align: center;">Response Frequency, Median (IQR)</th>
<th rowspan="2" style="text-align: center;">Total</th>
</tr>
<tr>
<th style="text-align: center;">Common-wealth (<em>n</em> = 6)</th>
<th style="text-align: center;">Western Europe (<em>n</em> = 7)</th>
<th style="text-align: center;">Central/Eastern Europe (<em>n</em> = 9)</th>
<th style="text-align: center;">Asia (<em>n</em> = 11)</th>
<th style="text-align: center;">Latin America (<em>n</em> = 7)</th>
<th style="text-align: center;">Middle-East/Africa (<em>n</em> = 5)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8" style="text-align: left;">Utility Instrument (UI) use frequency</td>
</tr>
<tr>
<td style="text-align: left;">   Total responses (<em>N</em>)</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">83</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">211</td>
</tr>
<tr>
<td style="text-align: left;">   AQOL</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">1 (1.5)</td>
<td style="text-align: center;">1 (1.5)</td>
<td style="text-align: center;">1 (0.5)</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;">   EQ-5D</td>
<td style="text-align: center;">4 (0)</td>
<td style="text-align: center;">4 (0)</td>
<td style="text-align: center;">4 (0)</td>
<td style="text-align: center;">4 (0)</td>
<td style="text-align: center;">3.5 (1.0)</td>
<td style="text-align: center;">4 (0.5)</td>
<td style="text-align: center;">23.5</td>
</tr>
<tr>
<td style="text-align: left;">   EQ-5D-Y</td>
<td style="text-align: center;">1.75 (0.5)</td>
<td style="text-align: center;">1 (1)</td>
<td style="text-align: center;">2 (1.5)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">10.75</td>
</tr>
<tr>
<td style="text-align: left;">   EQ-HWB</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0.75)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">1 (0.5)</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;">   Bolt-ons</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0.25)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;">   HUI</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">1 (1)</td>
<td style="text-align: center;">1.5 (1.0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">8.5</td>
</tr>
<tr>
<td style="text-align: left;">   PROPR</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0.5)</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;">   QWB</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0.5)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">6.0</td>
</tr>
<tr>
<td style="text-align: left;">   SF-6D</td>
<td style="text-align: center;">2 (0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">2.5 (1.0)</td>
<td style="text-align: center;">13.5</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">UI used matters, <em>n</em>(%)</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">31 (91.2)</td>
<td style="text-align: center;">28 (90.3)</td>
<td style="text-align: center;">22 (88.0)</td>
<td style="text-align: center;">83 (88.3)</td>
<td style="text-align: center;">33 (89.2)</td>
<td style="text-align: center;">10 (66.7)</td>
<td style="text-align: center;">207 (87.7)</td>
</tr>
<tr>
<td style="text-align: left;">   No/ not sure</td>
<td style="text-align: center;">3 (8.8)</td>
<td style="text-align: center;">3 (9.7)</td>
<td style="text-align: center;">3 (12.0)</td>
<td style="text-align: center;">11 (11.7)</td>
<td style="text-align: center;">4 (10.8)</td>
<td style="text-align: center;">5 (33.3)</td>
<td style="text-align: center;">29 (12.3)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Elicitation Method (EM) use frequency</td>
</tr>
<tr>
<td style="text-align: left;">   Total responses (<em>N</em>)</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">78</td>
<td style="text-align: center;">32</td>
<td style="text-align: center;">11</td>
<td style="text-align: center;">202</td>
</tr>
<tr>
<td style="text-align: left;">   BWS</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1 (0)</td>
<td style="text-align: center;">1.5 (2.0)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">1.5 (1.0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">8.0</td>
</tr>
<tr>
<td style="text-align: left;">   DCE</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">1.5 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (1.5)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3.5 (1.75)</td>
<td style="text-align: center;">13.0</td>
</tr>
<tr>
<td style="text-align: left;">   PTO</td>
<td style="text-align: center;">1.25 (1.0)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">2 (2.0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">10.25</td>
</tr>
<tr>
<td style="text-align: left;">   SG</td>
<td style="text-align: center;">2.25 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2.75 (1.5)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3.5 (1.5)</td>
<td style="text-align: center;">16.5</td>
</tr>
<tr>
<td style="text-align: left;">   TTO</td>
<td style="text-align: center;">4 (1.0)</td>
<td style="text-align: center;">3.5 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3.5 (1.0)</td>
<td style="text-align: center;">20.0</td>
</tr>
<tr>
<td style="text-align: left;">   VAS</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">3.5 (1.0)</td>
<td style="text-align: center;">16.5</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">EM used matters, <em>n</em> (%)</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">27 (79.4)</td>
<td style="text-align: center;">26 (86.7)</td>
<td style="text-align: center;">16 (69.6)</td>
<td style="text-align: center;">71 (81.6)</td>
<td style="text-align: center;">27 (75.0)</td>
<td style="text-align: center;">11 (84.6)</td>
<td style="text-align: center;">178 (79.8)</td>
</tr>
<tr>
<td style="text-align: left;">   No/ not sure</td>
<td style="text-align: center;">7 (20.6)</td>
<td style="text-align: center;">4 (13.3)</td>
<td style="text-align: center;">7 (30.4)</td>
<td style="text-align: center;">16 (18.4)</td>
<td style="text-align: center;">9 (25.0)</td>
<td style="text-align: center;">2 (15.4)</td>
<td style="text-align: center;">45 (20.2)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Health Preference Source (HPS) use frequency</td>
</tr>
<tr>
<td style="text-align: left;">   Total responses (<em>N</em>)</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">84</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">213</td>
</tr>
<tr>
<td style="text-align: left;">   General population own</td>
<td style="text-align: center;">3.25 (2.0)</td>
<td style="text-align: center;">3 (2.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">14.25</td>
</tr>
<tr>
<td style="text-align: left;">   General population other</td>
<td style="text-align: center;">2.5 (1.0)</td>
<td style="text-align: center;">2 (2.0)</td>
<td style="text-align: center;">4 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">17.5</td>
</tr>
<tr>
<td style="text-align: left;">   Patient own</td>
<td style="text-align: center;">2 (0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">1 (1.0)</td>
<td style="text-align: center;">11.0</td>
</tr>
<tr>
<td style="text-align: left;">   Patient other</td>
<td style="text-align: center;">2 (2.0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">15.0</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">HPS used matter, <em>n</em> (%)</td>
</tr>
<tr>
<td style="text-align: left;">   Yes</td>
<td style="text-align: center;">30 (88.2)</td>
<td style="text-align: center;">30 (96.8)</td>
<td style="text-align: center;">23 (92.0)</td>
<td style="text-align: center;">86 (90.5)</td>
<td style="text-align: center;">35 (92.1)</td>
<td style="text-align: center;">13 (86.7)</td>
<td style="text-align: center;">217 (91.2)</td>
</tr>
<tr>
<td style="text-align: left;">   No/ not sure</td>
<td style="text-align: center;">4 (11.8)</td>
<td style="text-align: center;">1 (3.2)</td>
<td style="text-align: center;">2 (8.0)</td>
<td style="text-align: center;">9 (9.5)</td>
<td style="text-align: center;">3 (7.9)</td>
<td style="text-align: center;">2 (13.3)</td>
<td style="text-align: center;">21(8.9)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Data quality issue frequency</td>
</tr>
<tr>
<td style="text-align: left;">   Total responses (<em>N</em>)</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">31</td>
<td style="text-align: center;">25</td>
<td style="text-align: center;">95</td>
<td style="text-align: center;">38</td>
<td style="text-align: center;">15</td>
<td style="text-align: center;">238</td>
</tr>
<tr>
<td style="text-align: left;">   Patient samples</td>
<td style="text-align: center;">3 (2.0)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">2 (0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (2.0)</td>
<td style="text-align: center;">2.5 (1.0)</td>
<td style="text-align: center;">16.5</td>
</tr>
<tr>
<td style="text-align: left;">   Health states</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">2 (1.5)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (0)</td>
<td style="text-align: center;">4 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">17.0</td>
</tr>
<tr>
<td style="text-align: left;">   Sample size</td>
<td style="text-align: center;">3 (0.5)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">16.0</td>
</tr>
<tr>
<td style="text-align: left;">   Old data</td>
<td style="text-align: center;">2 (0)</td>
<td style="text-align: center;">2 (0.5)</td>
<td style="text-align: center;">2 (1.25)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">2 (2.0)</td>
<td style="text-align: center;">2.5 (0.5)</td>
<td style="text-align: center;">12.5</td>
</tr>
<tr>
<td style="text-align: left;">   Different methods</td>
<td style="text-align: center;">2.75 (1.0)</td>
<td style="text-align: center;">2 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (1.0)</td>
<td style="text-align: center;">3 (2.0)</td>
<td style="text-align: center;">3 (1.5)</td>
<td style="text-align: center;">16.75</td>
</tr>
</tbody>
</table>

Abbreviations: *Responses*: 1: Never/not sure; 2: Occasionally; 3: Often; 4: Very often; *Elicitation Methods: BWS:* best-worst scaling; *DCE*: discrete choice experiment; *PTO:* person trade-off; *SG:* standard gamble; *TTO:* time trade-off; *VAS:* visual analogue scale; *Health preference source*: Refers to general population/ patients of one’s own country or other country; *Data quality issue*: *Patient samples*: The patient samples from which HRQoL/utility data was collected were inappropriate (e.g. poor representativeness); *Health states*: The health states (e.g. the vignettes) for which utility data was available do not match the health states in the CEA model; *Sample size*: The population samples from which HRQoL/utility data was collected were too small; *Old data*: The HRQoL/utility data was too old; *Different methods*: The utility values of different health states used in the same model were derived using different methods/instruments.

Countries in each region: Asia (China, India, Indonesia, Japan, Malaysia, Philippines, Singapore, South Korea, Taiwan, Thailand, Vietnam), Central/Eastern Europe (Bulgaria, Croatia, Czech Republic, Estonia, Hungary, Latvia, Poland, Romania, Slovenia), Western Europe (Austria, Denmark, Italy, Netherlands, Portugal, Spain, Sweden), Latin America (Argentina, Brazil, Chile Colombia, Ecuador, Mexico, Peru), Middle East/ Africa (Egypt, Saudi Arabia, South Africa, Tunisia, UAE), Commonwealth (Australia, Canada, England, New Zealand, Scotland, Wales).

</div>

Respondents across the regions (<a href="#tab3" data-ref-type="table">Table 3</a>) generally agreed that the choice of utility instrument matters (87.7 percent), ranging from 66.7 percent (Middle East/ Africa) to 91.2 percent (Western Europe). Content analysis revealed that the EQ-5D (EQ-5D-3L/ EQ-5D-5L) instrument was most often selected as the more fit-for-purpose instrument (<a href="#tab3" data-ref-type="table">Table 3</a>) mainly due to its low respondent burden, good psychometric properties, availability of value sets, HTA guide recommendations, and its wide usage that promotes comparability and consistency in the HTA setting.

<div id="tab3" class="table-wrap">

<div class="caption">

More fit-for-purpose tool and their pros and cons and data source issues encountered

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Instruments</th>
<th style="text-align: left;">Counts</th>
<th style="text-align: left;">Pros</th>
<th style="text-align: left;">Cons</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">EQ-5D<br />
(EQ-5D-3L/<br />
EQ-5D-5L)</td>
<td style="text-align: center;">148</td>
<td style="text-align: left;">Guidelines, value sets, comparability/ consistency in use, widely used, low respondent burden, familiarity, validated/ good psychometric properties, established in HTA</td>
<td style="text-align: left;">Not sensitive in certain health conditions</td>
</tr>
<tr>
<td style="text-align: left;">Depends</td>
<td style="text-align: center;">37</td>
<td style="text-align: left;">Population/condition, standardisation/ consistency/ comparability</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">SF-6D</td>
<td style="text-align: center;">18</td>
<td style="text-align: left;">Value sets, comparability, established in HTA</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">HUI/ HUI3</td>
<td style="text-align: center;">14</td>
<td style="text-align: left;">More discriminative in certain conditions, value sets</td>
<td style="text-align: left;">Expensive, seldom used</td>
</tr>
<tr>
<td style="text-align: left;">AQoL</td>
<td style="text-align: center;">13</td>
<td style="text-align: left;">More discriminative in certain conditions</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-Y</td>
<td style="text-align: center;">13</td>
<td style="text-align: left;">Child population</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Bolt-ons</td>
<td style="text-align: center;">7</td>
<td style="text-align: left;">Improves sensitivity of EQ–5D in certain health conditions</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-HWB</td>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Broader quality of life outcomes</td>
<td style="text-align: left;">Limited experience, insufficient evidence currently (psychometric properties, value sets)</td>
</tr>
<tr>
<td style="text-align: left;">QWB</td>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Focus on well-being</td>
<td style="text-align: left;">Limited experience</td>
</tr>
<tr>
<td style="text-align: left;">CHU-9D</td>
<td style="text-align: center;">2</td>
<td style="text-align: left;">Use in child population, value sets.</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PROMIS 10</td>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Government use, value sets</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">QLQ-C30</td>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Value sets, disease specific</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

### Use and importance of preference elicitation methods

The top three most frequently used utility elicitation methods were TTO, VAS, and SG, all of which were “often” used (<a href="#tab2" data-ref-type="table">Table 2</a>). Across regions, the TTO was either “often” or “very often” used to inform decision-making. SG and VAS were only “occasionally” used in Western Europe and the Commonwealth. DCE was “occasionally” used in most regions, but its frequency ranged from “often” and “very often” in the Middle East/Africa. The use frequency of BWS and PTO ranged between “never” and “occasionally” in all regions ([Supplementary Table 4](http://doi.org/10.1017/S0266462326103602)).

Respondents across the regions generally agreed that the choice of elicitation method matters (79.8 percent), ranging from 69.6 percent (East and Central Europe) to 86.7 percent (Western Europe). A total of fifty-five respondents mentioned the TTO method as the more fit-for-purpose elicitation method (<a href="#tab3" data-ref-type="table">Table 3</a>). Common reasons (<a href="#tab3" data-ref-type="table">Table 3</a>) included that the TTO had a strong theoretical foundation, involved trade-offs, produced cardinal utilities, was a validated method, and was easy to use. However, the high cognitive burden of the method was often recognized as a limitation of the technique. Many respondents (*n* = 47) mentioned that the elicitation method would need to depend on the disease area, the context of the study, and the availability of evidence.

### Use and importance of health preference data sources

The general public of another country was more frequently used (“often”) than the preferences of the local public (“occasionally”) (<a href="#tab2" data-ref-type="table">Table 2</a>). Region-wise, in Western Europe and the Commonwealth countries, the general population of one’s own country was most frequently used (“often”). In Asia, the general public (own and other countries) and patients (own country) had parallel high usage (“often”). In Latin America, the Middle East/Africa, and Central/Eastern Europe, data of other countries (both general population and patient values) were “often” or “very often” used while the values of one’s own country were only “occasionally” or even “never” utilized ([Supplementary Table 5](http://doi.org/10.1017/S0266462326103602)).

Respondents across the regions had a strong consensus that the health preference data source matters (91.2 percent), ranging from 86.7 percent (Middle East/Africa) to 96.8 percent (Western Europe). Of the 144 qualitative responses received, 81 respondents mentioned that the general public’s preferences should determine the utility values. Commonly cited reasons include HTA/country guide’s recommendations, consistency reasons, taxpayers being the most appropriate in a publicly funded healthcare system, and the tendency of patients to adapt to disease, thereby underestimating the disutilities. Conversely, fifty-three respondents felt that patients’ preferences should determine the values, as they reflect the patient voice and capture the disease experience better. Ten people felt it should come from both, either combining both preferences or using them to address different research questions. A total of seventy-nine respondents mentioned that these preferences should come from one’s own country population, as they reflect the culture and context of the preferences more accurately. None explicitly preferred utility values from other countries over their own.

### Use of data with quality concerns

Data quality issues that were “often” encountered across regions included poor sample representativeness, small sample size, poor matching of available data with that needed for CEA models, and data used in the same CEA model generated from multiple elicitation methods/utility instruments (<a href="#tab2" data-ref-type="table">Table 2</a>). These concerns were generally shared across regions. The issue with using outdated data was less of a concern, with most regions reporting it only “occasionally” ([Supplementary Table 6](http://doi.org/10.1017/S0266462326103602)).

### Research priorities

<a href="#tab4" data-ref-type="table">Table 4</a> depicts the research priority by country and region. The top three research priorities globally were i) to make more recent utility values available (recent tariff, importance score (IS) = 0.20), ii) to develop utility instruments to capture the impact of treatment on children and adolescents (children, 0.19), and iii) to develop utility instruments to capture both healthcare and social care impact (social care, 0.17). In Asia (importance score, 0.21) and Western Europe (0.33), the top-voted research priority was related to social care. In the Middle East/Africa (0.33) and Central/Eastern Europe (0.31), the primary research priority was related to recent tariffs. In the Commonwealth (0.23), the priority was to develop utility instruments to capture the impact of treatment on carers; In Latin America (0.22), the top research topic was to develop utility instruments addressing inequality in care. In all regions except for Western Europe and Latin America, children were the second highest research priority (IS = 0.18 to 0.30). In Asia (0.17) and Western Europe (0.15), recent tariffs remain the third highest research priority.

<div id="tab4" class="table-wrap">

<div class="caption">

Research priority by mean sum score

</div>

| Country | Social Care | Children | Care-givers | Health Specificity | Recent Tariff | Care Inequality | Minority/ rural |
|:---|:---|:---|:---|:---|:---|:---|:---|
| Asia (*n* = 11) | **0.21** | **0.18** | **0.09** | **0.15** | **0.17** | **0.13** | **0.08** |
|    China | 0.25 | 0.17 | 0.00 | 0.17 | 0.17 | 0.17 | 0.08 |
|    India | 0.27 | 0.07 | 0.00 | 0.13 | 0.33 | 0.20 | 0.00 |
|    Indonesia | 0.20 | 0.13 | 0.07 | 0.13 | 0.20 | 0.13 | 0.13 |
|    Japan | 0.22 | 0.22 | 0.11 | 0.11 | 0.22 | 0.00 | 0.11 |
|    Malaysia | 0.17 | 0.17 | 0.08 | 0.13 | 0.13 | 0.29 | 0.04 |
|    Philippines | 0.22 | 0.22 | 0.11 | 0.11 | 0.00 | 0.00 | 0.33 |
|    Singapore | 0.16 | 0.20 | 0.13 | 0.13 | 0.31 | 0.04 | 0.02 |
|    South Korea | 0.19 | 0.27 | 0.08 | 0.22 | 0.22 | 0.02 | 0.00 |
|    Taiwan | 0.28 | 0.12 | 0.07 | 0.17 | 0.20 | 0.07 | 0.10 |
|    Thailand | 0.13 | 0.20 | 0.20 | 0.20 | 0.00 | 0.27 | 0.00 |
|    Vietnam | 0.17 | 0.19 | 0.12 | 0.10 | 0.13 | 0.20 | 0.10 |
| Central/Eastern Europe (*n* = 8) | **0.10** | **0.30** | **0.09** | **0.12** | **0.31** | **0.05** | **0.03** |
|    Bulgaria | 0.17 | 0.22 | 0.06 | 0.11 | 0.11 | 0.06 | 0.28 |
|    Croatia | 0.33 | 0.33 | 0.00 | 0.00 | 0.33 | 0.00 | 0.00 |
|    Czech Republic | 0.00 | 0.33 | 0.33 | 0.00 | 0.33 | 0.00 | 0.00 |
|    Hungary | 0.00 | 0.22 | 0.00 | 0.28 | 0.39 | 0.11 | 0.00 |
|    Latvia | 0.00 | 0.50 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 |
|    Poland | 0.00 | 0.42 | 0.17 | 0.17 | 0.25 | 0.00 | 0.00 |
|    Romania | 0.00 | 0.33 | 0.00 | 0.33 | 0.33 | 0.00 | 0.00 |
|    Slovenia | 0.33 | 0.00 | 0.17 | 0.06 | 0.22 | 0.22 | 0.00 |
| Commonwealth (*n* = 6) | **0.07** | **0.21** | **0.23** | **0.20** | **0.15** | **0.05** | **0.10** |
|    Australia | 0.14 | 0.14 | 0.10 | 0.38 | 0.05 | 0.05 | 0.14 |
|    Canada | 0.08 | 0.08 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 |
|    England | 0.17 | 0.15 | 0.31 | 0.13 | 0.17 | 0.06 | 0.02 |
|    New Zealand | 0.00 | 0.25 | 0.17 | 0.17 | 0.17 | 0.00 | 0.25 |
|    Scotland | 0.00 | 0.33 | 0.33 | 0.00 | 0.33 | 0.00 | 0.00 |
|    Wales | 0.00 | 0.33 | 0.33 | 0.33 | 0.00 | 0.00 | 0.00 |
| Western Europe (*n* = 7) | **0.33** | **0.13** | **0.12** | **0.10** | **0.15** | **0.17** | **0.01** |
|    Austria | 0.39 | 0.22 | 0.00 | 0.00 | 0.17 | 0.22 | 0.00 |
|    Denmark | 0.17 | 0.13 | 0.13 | 0.00 | 0.17 | 0.42 | 0.00 |
|    Italy | 0.33 | 0.00 | 0.17 | 0.17 | 0.33 | 0.00 | 0.00 |
|    Netherlands | 0.42 | 0.06 | 0.17 | 0.11 | 0.00 | 0.25 | 0.00 |
|    Portugal | 0.19 | 0.25 | 0.11 | 0.25 | 0.08 | 0.06 | 0.06 |
|    Spain | 0.28 | 0.11 | 0.17 | 0.06 | 0.17 | 0.22 | 0.00 |
|    Sweden | 0.50 | 0.11 | 0.11 | 0.11 | 0.17 | 0.00 | 0.00 |
| Latin America (*n* = 7) | **0.16** | **0.08** | **0.15** | **0.16** | **0.11** | **0.22** | **0.12** |
|    Argentina | 0.17 | 0.00 | 0.17 | 0.17 | 0.00 | 0.33 | 0.17 |
|    Brazil | 0.07 | 0.10 | 0.15 | 0.18 | 0.18 | 0.22 | 0.10 |
|    Chile | 0.22 | 0.11 | 0.28 | 0.11 | 0.00 | 0.28 | 0.00 |
|    Colombia | 0.17 | 0.14 | 0.11 | 0.25 | 0.08 | 0.17 | 0.08 |
|    Ecuador | 0.22 | 0.11 | 0.22 | 0.22 | 0.06 | 0.11 | 0.06 |
|    Mexico | 0.28 | 0.11 | 0.11 | 0.00 | 0.28 | 0.11 | 0.11 |
|    Peru | 0.00 | 0.00 | 0.00 | 0.17 | 0.17 | 0.33 | 0.33 |
| Middle East/ Africa (*n* = 5) | **0.12** | **0.23** | **0.14** | **0.03** | **0.33** | **0.12** | **0.03** |
|    Egypt | 0.17 | 0.00 | 0.17 | 0.17 | 0.17 | 0.33 | 0.00 |
|    Saudi Arabia | 0.00 | 0.33 | 0.33 | 0.00 | 0.33 | 0.00 | 0.00 |
|    South Africa | 0.13 | 0.13 | 0.07 | 0.00 | 0.37 | 0.17 | 0.13 |
|    Tunisia | 0.17 | 0.42 | 0.00 | 0.00 | 0.42 | 0.00 | 0.00 |
|    UAE | 0.11 | 0.28 | 0.11 | 0.00 | 0.39 | 0.11 | 0.00 |
| Total Average Score | **0.17** | **0.19** | **0.14** | **0.13** | **0.20** | **0.12** | **0.06** |

*Note*: Social care: To develop utility instruments to capture the impact of both health care and social care; Children: To develop utility instruments to capture the impact of treatment on children and adolescents; Caregivers: To develop utility instruments that capture the impact of a treatment on carers and caregivers; Health Impact: To develop utility instruments that capture the impact of treatment on more specific aspects of health (e.g. vision hearing etc.); Recent Tariff: To make more recent utility data and value sets/tariffs available; Care Inequality: To develop utility instruments that can address inequality in care; Minority/Rural: To develop utility instruments that can reflect the health preferences of minority groups (e.g. indigenous populations) or rural population.

For example, respondent A from Thailand endorsed two research priorities; social care and children. Each of these two topics received a score of 0.5 and remain topics received a score of 0. To calculate the score for the social care research priority for Thailand, these scores belonging to the individuals from Thailand were averaged. If 10 respondents from Thailand endorsed at least one topic, and the score for social care was 0.5 for five respondents and 0.2 for the remaining five respondents, the importance score for social care in Thailand is 0.35 (i.e., (\[0.5 x 5\] + \[0.2 x 5\]) / 10).

</div>

## Discussion

In this study, we obtained global insights into the practices, views, and needs of HTA agency personnel across six regions on a broad range of topics related to the measurement and valuation of health. Additionally, we explored data quality issues encountered by HTA practitioners and identified research topics perceived as important.

In general, the respondents’ practices regarding the choice of utility instruments and elicitation methods were consistent with HTA guideline recommendations of using indirect measures such as the EQ-5D instrument as the reference case, and preferring choice-based preference elicitation methods (5;17;18).

Interestingly, only in Western Europe and the Commonwealth were local public health-state preferences used more frequently than those of foreign sources, possibly highlighting the prevalent issue of data availability in the field of HTA (22;23). Additionally, patient preference data is only occasionally used in Western Europe and the Commonwealth, aligning with most HTA guideline recommendations and empirical study findings (24;25). However, patient preference data is often used in regions outside Western Europe and the Commonwealth, perhaps motivated by interest in patients’ views and/or unavailability of preference data from the general public. While respondents’ views regarding the choice of instrument, methods, and health preference data sources generally reflect HTA guidance recommendations, some preferred patient preferences, arguing that the patient voice and disease experience are important. Additionally, some respondents expressed concerns about the shortcomings of the widely used EQ-5D and the TTO method. The main disadvantage of the EQ-5D, as cited by respondents, is poor responsiveness in certain health conditions, while TTO poses a high cognitive burden to respondents. Similar concerns have been documented in the literature (26–28). Interestingly, those respondents did not consider using new instruments such as EQ-HWB, PROPr, “bolt-ons” or new valuation methods such as DCE, perhaps because they were not aware of or familiar with those new alternatives.

This study identified widespread suboptimal use of HRQoL and HSU data in current HTA practice across regions. Data-related issues included sample representativeness, sample size, use of mismatched data, and data generated using different instruments and methods. These issues are likely due to the scarcity of quality and appropriate data, underscoring the need for research to improve data availability (29). Respondents’ comments suggested that HTA practitioners are aware of the data quality issues and the validity of the methods used to address them. This finding echoes the increasing concerns about the methodological rigor in using HSU data for CUA (30–32). However, the magnitude of such issues is largely unknown. A recently conducted systematic review of published CUAs from Asia found that the overall reporting quality for HRQoL or HSU data was very poor (33).

Regarding research priorities, developing instruments to capture the impact of treatments on children and adolescents emerged as an important topic in most regions. This may reflect a real unmet need for fit-for-purpose instruments all around the world. Instruments assessing effects of social care, caregiver needs, and specific health problems are at the top of the wish list of HTA practitioners from many regions. The need for recent tariffs globally as the top research priority further strengthens the importance of valuation work. This need was especially emphasized in the Middle East/Africa and Central/Eastern Europe, where value set generation is only starting to gain momentum (34–36). Countries in these regions generally lack preference-based values. In line with the growth of HTA in these countries, the presence of value sets becomes essential in expanding the use of CUAs and in implementing HTA for wider coverage of healthcare decision-making (37–39). An interesting research topic proposed by a respondent is to develop public depositories of HSU data. Such a depository would act as a library, storing data from different population groups, facilitating crosswalks to other country value sets, and being referenced by HTA practitioners as needed. A properly regulated HSU depository would alleviate the issue of scarce data faced by HTA practitioners globally. These research topics, along with insights from the content analysis, highlight the global need for greater generation of HSUs in different areas to better capture the health preferences of populations.

The above findings on the current practice and views of HTA personnel on instruments, methods, and data for generating QALY-based evidence may provide useful guidance for future research. First, research on instruments targeting children and adolescents, such as EQ-5D-Y, may be prioritized due to a global need for such tools. Compared to HRQoL instruments for adults, those for children and adolescents are fewer and less developed (40). The methods review completed by NICE in 2022 found insufficient evidence for recommending any existing HRQoL instruments for use in pediatric HTA and therefore called for research in this area (41). Second, researchers developing new instruments and elicitation methods may consider shifting from a pure academic approach to a user-oriented approach by engaging stakeholders, particularly HTA agencies, in the whole development process. Such a collaborative approach may increase the chance of developing a product that will be accepted or adopted sooner for use in HTA practice. This approach to involving stakeholders such as patient advocacy groups and decision-makers has been used in developing the EQ-HWB instrument (42). Given that instrument development is a lengthy, multi-stage process and HTA agencies are cautious in endorsing new instruments and methods, sustained engagement and long-term collaboration may be necessary to achieve a tangible impact. Moreover, given that established HTA agencies are more concerned with maintaining consistency and standardization, new instruments and methods may be more likely to be endorsed and accepted by burgeoning HTA agencies. Last but not least, research on methods for making more HRQoL and HSU data available or making better use of existing data seems equally or even more important than making new instruments available (see <a href="#tab5" data-ref-type="table">Table 5</a>, which summarizes respondent-identified priority research topics related to utility values, many of which concern data availability). This is because data scarcity for endorsed HRQoL instruments such as EQ-5D may be a greater issue than the lack of more fit-for-purpose instruments, such as EQ-HWB, because those instruments are routinely used. Such research may involve systematically collecting and publishing HRQoL data from health systems, collating and compiling HRQoL data published in the literature, and developing tools for modifying or transforming HRQoL data for use across health systems. Databases providing HSU data and guidelines promoting appropriate use of HSU data (32;43) have been available. However, those may not be sufficient and more work is needed to fill in this data gap and need.

<div id="tab5" class="table-wrap">

<div class="caption">

Other research topic of importance-related to utility values

</div>

| Research topic |
|:---|
| To assess the validity of quality-adjusted life years in capturing outcomes |
| To capture productivity losses and double counting with quality of life measures |
| To develop a public depository of health-state utilities |
| To develop guidelines on instrument use to increase comparability |
| To develop patient-specific utilities |
| To ensure instruments used have content validity- relevant domains/health states are captured |
| To generate living health-state utilities over long time horizons |
| To generate utility values of rare disease |
| To make country-specific utility data available |
| To make cross-country preference and utility evidence available |
| To produce more research on the impact of shifting to EQ-5D-5L instrument |

</div>

This study had several limitations. In twelve of the forty-five countries, there were fewer than three responses despite repeated reminders, limiting the representativeness of these countries. A further limitation is the difficulty in identifying the most appropriate respondent within an HTA agency. Senior personnel may be well-positioned to speak on behalf of the organisation, but may not possess detailed knowledge of the specific research area. Conversely, analysts may have relevant expertise but may not be able to represent the agency’s official position, for example, due to limited seniority or differing personal views. Another limitation concerns the snowball-type recruitment method we employed. Potential respondents were identified through the network of EuroQol Group members. As a result, HTA personnel who are familiar with or favor EuroQol instruments may be overrepresented in our sample. However, EuroQol Group members come from diverse backgrounds and regions, and many actively participate in HTA development in their respective countries, making them ideal recruiters for this by-invitation-only global survey. A related limitation relates to our recruitment strategy. Because recruitment was organized at the country level rather than at the level of specific HTA bodies, respondents were encouraged to provide their views as individuals rather than as formal representatives of their organizations. Consequently, we were unable to identify respondents by specific HTA agency within each country and therefore could not reanalyze the data using the HTA body as the unit of analysis. Although we considered additional subgroup analyses, for example, examining differences by type of technology appraised or therapeutic area, we judged that such analyses would not yield reliable or interpretable findings. Many respondents reported involvement across multiple therapeutic areas, multiple health technology types, or held several HTA roles, making clear classification challenging. Moreover, the study was not powered to detect meaningful subgroup differences, and uneven distribution across categories would further limit the validity of any conclusions drawn. Lastly, we were not able to verify the eligibility of the respondents. Country-specific survey links were distributed by recruiters to potential respondents in the target HTA agencies. Although screening questions were included at the start of the survey, personal identifiers such as respondent names or the agencies they worked for were not collected to encourage more candid responses.

## Conclusions

This study addresses important knowledge gaps regarding the current practices of measuring and valuing HRQoL in HTA and the views on the challenges and needs of HTA agency personnel worldwide. Findings from this study may guide research aimed at developing tools and methods for providing high-quality QALY evidence for economic evaluations.

## Supporting information

<div class="caption">

###### Vasan Thakumar et al. supplementary material

Vasan Thakumar et al. supplementary material

</div>

10.1017/S0266462326103602.sm001

## Acknowledgements

We extend our deepest gratitude to the following individuals who acted as recruiters for the study and contributed to the success of our study: Aureliano Finch, Claire Gudex, Fanni Rencz, Fatima Al Sayah, Gan Yan Nee, Haarathi Chandriah, Jan Busschbach, Jazmin Joanna Pinzon, Jennifer Jelsma, Juan M. Ramos-Goñi, Marisa Santos, Mimi Astrom, Min-Woo Jo, Patricia Antunes, Petra Došenovič Bonča, Princess Allyza, Sarah Dewilde, Selenia Gomez, Sivaraj Raman, Takeru Shiroiwa, Tommy Chen, Victor Zarate, Vu Quynh Mai, Wang Pei, and Wanrudee Isaranuwatchai. We are also thankful to the following recruiters whose attempts were not successful: Gerard de Pouvourville, Henry Bailey, John Yfantopoulos, Oliver Rivero-Arias, Sarah Dewilde, and Wolfgang Greiner.

## Supplementary material

The supplementary material for this article can be found at <http://doi.org/10.1017/S0266462326103602>.

## Data availability statement

Data generated for the current study are included in this published article (and its supplementary files). They are also available from the corresponding author on reasonable request.

## Author contribution

Concept and design: NL and NB. Acquisition of data: NL, NB, AVT, PL, LL, LRA, FP, DG, FA, KR, and RV. Analysis and interpretation of data: NL, NB, and AVT. Drafting of manuscript: NL, NB, and AVT. Critical revision of paper for important intellectual content: NL, NB, AVT, PL, LL, LRA, FP, DG, FA, KR, and RV. Statistical analysis: AVT, KR, NL, and NB. Supervision: NL and NB.

## Funding statement

This project is supported by the EuroQol Research Foundation (Grant Number: 1505-RA), Rotterdam, the Netherlands.

## Competing interests

Lorgelly, Longworth, Rey-Ares, Purba, Golicki, Augustovski, Rand, Viney, Bansback, and Luo are members of the EuroQol Research Foundation. Vasan Thakumar declares no conflict of interest.

## References

## References

1. Drummond MF, Sculpher MJ, Claxton K, Stoddart GL, Torrance GW. Methods for the economic evaluation of health care programmes. 4th ed. Oxford, UK: Oxford University Press; 2015.

2. Fontrier AM, Visintin E, Kanavos P. Similarities and differences in health technology assessment systems and implications for coverage decisions: evidence from 32 countries. Pharmacoecon Open. 2022;6:315–328. doi:10.1007/s41669-021-00311-5

3. Teerawattananon Y, Rattanavipapong W, Lin LW, et al. Landscape analysis of health technology assessment (HTA): systems and practices in Asia. Int J Technol Assess Health Care. 2019;35:416–421. doi:10.1017/S0266462319000667

4. World Health Organization. Health technology assessment and health benefit package survey 2020/2021. Geneva, Switzerland: World Health Organization. 2024. Available from: https://www.who.int/teams/health-systems-governance-and-financing/economic-analysis/health-technology-assessment-and-benefit-package-design/survey-homepage (16 June 2024).

5. Sharma D, Aggarwal AK, Downey LE, Prinja S. National healthcare economic evaluation guidelines: a cross-country comparison. Pharmacoecon Open. 2021;5:349–364. doi:10.1007/s41669-020-00250-7

6. Center for Evaluation of value and risk in health. Cost-effectiveness analysis (CEA) registry. Boston, MA: Tufts Medical Center. 2024. Available from: https://cevr.tuftsmedicalcenter.org/databases/cea-registry (01 Aug 2024).

7. Wang H, Rowen DL, Brazier JE, Jiang L. Discrete choice experiments in health state valuation: a systematic review of progress and new trends. Appl Health Econ Health Policy. 2023;21:1–14. doi:10.1007/s40258-023-00794-9

8. King MT, Revicki DA, Norman R, et al. United States value set for the functional assessment of cancer therapy-general eight dimensions (FACT-8D), a cancer-specific preference-based quality of life instrument. Pharmacoecon Open. 2024;8:49–63. doi:10.1007/s41669-023-00448-5

9. Shiroiwa T, King MT, Norman R, et al. Japanese value set for the EORTC QLU-C10D: a multi-attribute utility instrument based on the EORTC QLQ-C30 cancer-specific quality-of-life questionnaire. Qual Life Res. 2024;33:1865–1879. doi:10.1007/s11136-024-03655-7

10. Xu RH, Wong EL, Luo N, et al. The EORTC QLU-C10D: the Hong Kong valuation study. Eur J Health Econ. 2024;25:889–901. doi:10.1007/s10198-023-01632-4

11. Wang P, Chong SL, Tan RL, Luo N. A hearing bolt-on item increased the measurement properties of the EQ-5D-5L in a community-based hearing loss screening program. Eur J Health Econ. 2023;24:393–398. doi:10.1007/s10198-022-01479-1

12. Kangwanrattanakul K, Phimarn W. A systematic review of the development and testing of additional dimensions for the EQ-5D descriptive system. Expert Rev Pharmacoecon Outcomes Res. 2019;19:431–443. doi:10.1080/14737167.2019.1637736

13. Brazier J, Peasgood T, Mukuria C, et al. The EQ-HWB: overview of the development of a measure of health and wellbeing and key results. Value Health. 2022;25:482–491. doi:10.1016/j.jval.2022.01.009

14. EuroQol Research Foundation. EQ-5D Bolt-on Toolbox. 2025. Available from: https://euroqol.org/research-at-euroqol/eq-bolt-ons/ (17 December 2025).

15. Shiroiwa T, Murata T, Morii Y, Hoshino E, Fukuda T. Comparison of four value sets derived using different TTO and DCE approaches: application to the new region-specific PBM, AP-7D. Health Qual Life Outcomes. 2024;22:16. doi:10.1186/s12955-024-02233-2

16. Augustovski F, Belizán M, Gibbons L, et al. Peruvian valuation of the EQ-5D-5L: a direct comparison of time trade-off and discrete choice experiments. Value Health. 2020;23:880–888. doi:10.1016/j.jval.2020.05.004

17. ISPOR. Pharmacoeconomic guidelines around the world. 2024. Available from: https://www.ispor.org/heor-resources/more-heor-resources/pharmacoeconomic-guidelines/pe-guideline-detail/ (18 June 2024).

18. Kennedy-Martin M, Slaap B, Herdman M, et al. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020;21:1245–1257. doi:10.1007/s10198-020-01195-8

19. Guideline comparison: what can I learn from the existing health economic evaluation guidelines? [database on the Internet]. 2024. [cited 18 June 2024]. Available from: http://www.gear4health.com/gear/health-economic-evaluation-guidelines.

20. INAHTA. INAHTA members list. 2020. Available from: https://www.inahta.org/members/members_list/ (18 June 2024).

21. Curry LA, Nembhard IM, Bradley EH. Qualitative and mixed methods provide unique contributions to outcomes research. Circulation. 2009;119:1442–1452. doi:10.1161/CIRCULATIONAHA.107.742775

22. Zisis K, Pavi E, Geitona M, Athanasakis K. Real-world data: a comprehensive literature review on the barriers, challenges, and opportunities associated with their inclusion in the health technology assessment process. J Pharm Pharm Sci. 2024;27:12302. doi:10.3389/jpps.2024.12302

23. O’Rourke B, Werkö SS, Merlin T, Huang LY, Schuller T. The ‘top 10’ challenges for health technology assessment: INAHTA viewpoint. Int J Technol Assess Health Care. 2020;36:1–4. doi:10.1017/S0266462319000825

24. Hiligsmann M, Liden B, Beaudart C, et al. HTA community perspectives on the use of patient preference information: lessons learned from a survey with members of HTA bodies. Int J Technol Assess Health Care. 2024;40:e17. doi:10.1017/S0266462324000138

25. van Overbeeke E, Forrester V, Simoens S, Huys I. Use of patient preferences in health technology assessment: perspectives of Canadian, Belgian and German HTA representatives. Patient. 2021;14:119–128. doi:10.1007/s40271-020-00449-0

26. Brazier J, Ara R, Rowen D, Chevrou-Severac H. A review of generic preference-based measures for use in cost-effectiveness models. PharmacoEconomics. 2017;35:21–31. doi:10.1007/s40273-017-0545-x

27. Feng YS, Kohlmann T, Janssen MF, Buchholz I. Psychometric properties of the EQ-5D-5L: a systematic review of the literature. Qual Life Res. 2021;30:647–673. doi:10.1007/s11136-020-02688-y

28. Qian X, Tan RLY, Chuang LH, Luo N. Measurement properties of commonly used generic preference-based measures in east and south-east Asia: a systematic review. PharmacoEconomics. 2020;38:159–170. doi:10.1007/s40273-019-00854-w

29. Claire R, Elvidge J, Hanif S, et al. Advancing the use of real world evidence in health technology assessment: insights from a multi-stakeholder workshop. Front Pharmacol. 2023;14:1289365. doi:10.3389/fphar.2023.1289365

30. Ara R, Brazier J, Lloyd A, Chevrou-Severac H. How health state utilities used in cost-effectiveness models are currently identified, reviewed and reported. Value Outcomes Spotlight. 2018;4:31e3.

31. Ara R, Hill H, Lloyd A, Woods HB, Brazier J. Are current reporting standards used to describe health state utilities in cost-effectiveness models satisfactory? Value Health. 2020;23:397–405. doi:10.1016/j.jval.2019.12.004

32. Brazier J, Ara R, Azzabi I, et al. Identification, review, and use of health state utilities in cost-effectiveness models: an ISPOR good practices for outcomes research task force report. Value Health. 2019;22:267–275. doi:10.1016/j.jval.2019.01.004

33. Yang Z, Zeng X, Huang W, et al. Characteristics of health-state utilities used in cost-effectiveness analyses: a systematic review of published studies in Asia. Health Qual Life Outcomes. 2023;21:59. doi:10.1186/s12955-023-02131-z

34. Al-Jedai A, Almudaiheem H, Al-Salamah T, et al. Valuation of EQ-5D-5L in the Kingdom of Saudi Arabia: a national representative study. Value Health. 2024;27:552. doi:10.1016/j.jval.2024.01.017

35. Al Shabasy S, Abbassi M, Finch A, Roudijk B, Baines D, Farid S. The EQ-5D-5L valuation study in Egypt. PharmacoEconomics. 2022;40:433–447. doi:10.1007/s40273-021-01100-y

36. Prevolnik Rupel V, Ogorevc M. EQ-5D-5L value set for Slovenia. PharmacoEconomics. 2023;41:1515–1524. doi:10.1007/s40273-023-01280-9

37. Callenbach MHE, Ádám L, Vreman RA, Németh B, Kaló Z, Goettsch WG. Reimbursement and payment models in central and eastern European as well as middle eastern countries: a survey of their current use and future outlook. Drug Discov Today. 2023;28:103433. doi:10.1016/j.drudis.2022.103433

38. Falkowski A, Ciminata G, Manca F, et al. How least developed to lower-middle income countries use health technology assessment: a scoping review. Pathog Glob Health. 2023;117:104–119. doi:10.1080/20477724.2022.2106108

39. Kaló Z, Gheorghe A, Huic M, Csanádi M, Kristensen FB. HTA implementation roadmap in central and eastern European countries. Health Econ. 2016;25(Suppl 1):179–192. doi:10.1002/hec.3298

40. Canada’s drug agency (CDA-AMC). Health technology review - methods guide for health technology assessment. Ottawa, ON, Canada: Canada’s Drug Agency (CDA-AMC; 2024, p. 43.

41. Dawoud D, Lamb A, Moore A, et al. Capturing what matters: updating NICE methods guidance on measuring and valuing health. Qual Life Res. 2022;31:2167–2173. doi:10.1007/s11136-022-03101-6

42. Carlton J, Peasgood T, Mukuria C, Johnson J, Ogden M, Tovey W. The role of patient and public involvement and engagement (PPIE) within the development of the EQ health and wellbeing (EQ-HWB). J Patient Rep Outcomes. 2022;6:35. doi:10.1186/s41687-022-00437-y

43. Wolowacz SE, Briggs A, Belozeroff V, et al. Estimating health-state utility for economic models in clinical studies: an ISPOR good research practices task force report. Value Health. 2016;19:704–719. doi:10.1016/j.jval.2016.06.001

## Associated Data

### Supplementary Materials

<div class="caption">

###### Vasan Thakumar et al. supplementary material

Vasan Thakumar et al. supplementary material

</div>

10.1017/S0266462326103602.sm001

### Data Availability Statement

Data generated for the current study are included in this published article (and its supplementary files). They are also available from the corresponding author on reasonable request.

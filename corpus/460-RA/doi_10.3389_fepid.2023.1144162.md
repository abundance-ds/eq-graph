---
project_id: "460-RA"
work_id: "doi:10.3389/fepid.2023.1144162"
doi: "10.3389/fepid.2023.1144162"
pmid: "38455931"
pmcid: "PMC10910898"
title: "Cross-sectional and longitudinal comparison of health-related quality of life and mental well-being between persons with and without post COVID-19 condition"
journal: "Frontiers in Epidemiology"
publication_date: "2023-05-22"
volume: "3"
authors:
  - name: "Emily Stella Scott"
    affiliation_ids:
      - "aff1"
  - name: "Erica I Lubetkin"
    affiliation_ids:
      - "aff2"
  - name: "Mathieu F Janssen"
    affiliation_ids:
      - "aff3"
  - name: "John Yfantopolous"
    affiliation_ids:
      - "aff4"
  - name: "Gouke J Bonsel"
    affiliation_ids:
      - "aff5"
  - name: "Juanita A Haagsma"
    affiliation_ids:
      - "aff1"
affiliations:
  - id: "aff1"
    name: "Department of Public Health, Erasmus MC, Rotterdam, Netherlands"
  - id: "aff2"
    name: "Department of Community Health and Social Medicine, CUNY School of Medicine, New York City, NY, United States"
  - id: "aff3"
    name: "Section Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Rotterdam, Netherlands"
  - id: "aff4"
    name: "Health Department of Economics, National and Kapodistrian University of Athens, Athens, Greece"
  - id: "aff5"
    name: "Department Scientific Support, EuroQol Research Foundation, Rotterdam, Netherlands"
licence: "cc-by"
source_file: "input/projects/460-RA/papers/doi_10.3389_fepid.2023.1144162.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10910898/fullTextXML"
source_method: "epmc_xml"
source_sha256: "5f1817e727fdb9b8fdff38072c36a0c7c3e723ac4eff311a1603f65339cd1763"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Cross-sectional and longitudinal comparison of health-related quality of life and mental well-being between persons with and without post COVID-19 condition

## Abstract

### Background

Still little is known about the impact of post COVID-19 condition (PC) on health-related quality of life (HRQOL) and mental well-being. We compared participants with PC with three groups: an acute COVID-19 infection (AC) only, at least one chronic condition (CC) but no COVID-19, or no condition at all, healthy (PH). Between these disease groups, we also estimated and compared HRQOL and mental well-being change over time.

### Methods

Participants from six countries (Greece, Italy, Netherlands, Sweden, United Kingdom and United States) completed two web-based questionnaires (T1 = April–May 2020 and T2 = April–June 2022). Primary outcomes were HRQOL, measured by EQ-5D-5L and EQ VAS, and mental well-being (measured by World Health Organisation-Five (WHO-5) Well-Being Index, Patient Health Questionnaire (PHQ)-9 and General Anxiety Disorder (GAD)-7). All analyses were stratified by the disease groups.

### Results

In total, 4,999 participants filled out both surveys: 240 were in PC, 107 in AC, 1798 in CC and 2,854 in PH. At T2, the mean EQ-5D-5L index values for the PC, AC, CC and PH groups were 0.70, 0.73, 0.75 and 0.92 (*p* \< .001), respectively. Mean EQ VAS scores were 66, 65, 68 and 81 (*p* \< .001), respectively. Poor mental well-being, depression and anxiety mean values were highest in the PC group (47.7; 9.1; 7.4), followed by the AC group (51.1; 7.7; 5.7), CC group (56.1; 5.2; 4.2) and the PH group (65.6; 2.8; 2.5), respectively (*p* \< .001 between groups). Over time, HRQOL deteriorated in all groups, apart from the PH group. We observed the largest deterioration in the CC (EQ-5D-5L index: Δ0.03, *p* \< .001) and AC group (EQ VAS: Δ6.3, *p* \< .001). For the mental well-being outcomes, deterioration for WHO-5 and PHQ-9 were largest in the AC group (Δ4.8, *p* = .016; Δ-1.3, *p* = .012). Rates for GAD-7 improved for the PH and CC groups (PH: Δ1.27, CC: Δ0.56, *p* \< .001).

### Conclusions

In the cross-sectional analysis, participants with PC had the worst HRQOL and mental well-being compared to the other groups. In terms of change since the start of the COVID-19 pandemic, HRQOL and mental well-being deterioration was highest among AC participants and had a lower impact among PC participants, most likely due to pre-existing chronic disease.

**Keywords:** post COVID-19 condition, COVID-19, health-related quality of life, EQ-5D-5L, mental well-being, longitudinal, chronic condition, healthy control group

Received 2023 Jan 13; Accepted 2023 Apr 27; Collection date 2023.

## Introduction

The long-term burden of the COVID-19 pandemic on population health is reflected in the 10%–20% of persons who report symptoms related to COVID-19 infection beyond three months (1). These long-term symptoms can typically include fatigue, shortness of breath, cognitive dysfunction and mental health problems. They are often described as an extension of the acute COVID-19 infection, although many of them are unlike acute phase symptoms, with some symptoms only developing sometime after the acute phase. Altogether, 20 or more different symptoms have been recognised as potentially long-term symptoms (2, 3). The World Health Organization (WHO) formally defined “post COVID-19 condition” as being present if there is continuation or development of new symptoms three months after the initial severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infection, with symptoms lasting for at least two months, with no other explanation for the symptoms observed (4). So far, no limited set of condition-defining symptoms has been agreed on. Post COVID-19 condition may affect all domains of life, for example work, family relations, and social activities, thereby affecting health-related quality of life (HRQOL) (2) and mental well-being (5). Meta-analyses have shown that if post COVID-19 symptoms are present one month or more after the acute phase, HRQOL is negatively affected (6, 7). Similar evidence was found with longer follow-up (8). Mental well-being has been shown to be significantly impacted by post COVID-19 condition, too (9, 10). However, truly longitudinal evidence on the impact of post COVID-19 condition on HRQOL and mental well-being, i.e., evidence which is based on individual panel data collected before and after COVID-19 infection, is scarce. The commonly used recall data on HRQOL is lower than directly reported HRQOL (11). Longitudinal data would allow for a fair estimate of the impact of post COVID-19 condition and for determining prognostic modifiers once post COVID-19 condition arises. In the best case, preventable risk factors and effective care strategies are among these modifiers. In view of the specific pandemic effects on health, the use of healthy controls and of chronically diseased patients, with conditions sharing post COVID-19 condition symptoms, will further improve the detection and definition of post COVID-19 condition effects. As well as and not least, it would further improve the societal awareness of the conditions relevance to those affected.

In this study we use panel data from the longitudinal POPulation health impact of the CORoNavirus disease 2019 (COVID-19) pandemic (POPCORN) study. POPCORN is a large multi-national cohort-study set up in early 2020 to investigate the effect of the COVID-19 pandemic on HRQOL in the general population, with a special interest in the hypothesized deepening of health gaps across socio-economic and ethnic groups. The early timing of the POPCORN study has allowed us to collect data prior to the emergence of a large number of post COVID-19 condition-affected persons. The study encompassed a large set of outcome measures on HRQOL and mental well-being and the longitudinal structure allows for the comparison of health before and after acquiring post COVID-19 condition. As POPCORN comprises a general population cohort with detailed (co)morbidity information, comparisons between various sub-populations with and without post COVID-19 condition, but with other risks or morbidities are possible, allowing for our intended four-group (I-IV) comparison. Our aim is to estimate the HRQOL and mental well-being in persons with (I) post COVID-19 condition at T2 (April–June 2022) as well as compare their HRQOL and mental well-being with three other independent groups of participants, with either (II) an acute COVID-19 infection, (III) at least one chronic condition but no COVID-19, or (IV) no condition at all, assumed to be healthy. For these four groups, we also estimated the HRQOL and mental well-being at T1 (April–May 2020), and in a further comparison between the four groups, analysed the change in HRQOL and mental well-being from T1 to T2. We were additionally interested in who at T1 would go on to develop post COVID-19 condition at T2.

## Materials and methods

### Study design and population

This study is part of the POPCORN study. Data from the general population from six different countries, namely Greece, Italy, the Netherlands, Sweden, the United Kingdom and the United States (US), were collected via web-based surveys. All participants included in this study completed the survey at T1 (April–May 2020) and at T2 (April–June 2022). Further POPCORN studies have been published elsewhere (12).

### Data collection procedure and consent

The surveys were distributed to participants by a market research agency (Dynata) at T1 and T2. This agency enlisted the participants from an existing large panel in these six countries. The study sample was designed to be representative by age, sex and educational level of the population in the respective country. Upon recruitment to the POPCORN project in 2020 (T1), participants were aged 18 to 75 years. To participate in these online surveys, participants already provided written informed consent upon registration when enrolling in the market research agencies' voluntary panels. As soon as participation in the survey had begun, the data capture system did not allow for any skipped or missed questions; therefore, this study has no missing values. An incentive in the form of cash or points (with a value between 3 and 6 Euro, depending on the participants country of residence) from the research agency was provided upon completion. Data were anonymised, and so the researchers had no direct access to individual participants.

### Questionnaire

The questionnaires at T1 and T2 were close to identical, and included health outcome questions, medical risk factors (including e.g., smoking) and chronic conditions, socioeconomic determinant questions, COVID-19 related questions, demographic questions and questions on healthcare (access, use, etc.). The questionnaires were translated by human translators into the country's official language using computer-assisted translation software, followed by a translation back into English, except in the case of already available instruments with validated translated versions. Bilingual native speakers independently verified these translations. In Sweden, the T1 questionnaire was distributed between May 26 and June 1 in 2020, whereas in the remaining countries this was between April 22 and May 5 in 2020. In 2022 the questionnaires were distributed between 29 April and 25 June in all countries.

### Primary outcome measures

Our primary outcome measures were HRQOL (measured by the EQ-5D-5L descriptive system, index values and EQ VAS) and mental well-being (measured by the World Health Organisation-Five (WHO-5) Well-Being Index, Patient Health Questionnaire (PHQ)-9 and General Anxiety Disorder (GAD)-7). The EQ-5D-5L descriptive system consists of a short set of five questions referring to the participants' self-reported health state today (13). It includes five dimensions, namely Mobility, Self-care, Usual activities, Pain/discomfort and Depression/anxiety. These dimensions can be rated on a 5-item scale from “no problems”, (“1”), to “extreme problems/unable to”, (“5”). The index values are derived from the EQ-5D-5L responses that have been weighted according to a value set, whereby the value set reflects societal preferences within a certain population (usually a country) of these health states. We used a single value set, the US value set (14), for each country, as this allows for cross-country comparisons. The EQ-5D-5L index values range from below 0 (“worse than death”) to 1 (“full health”), whereby the US value set ranges between −0.573 to 1. The EQ VAS (visual analogue scale) is the second part of the EQ-5D-5L instrument, whereby participants rate their overall health today on a scale from 0 (“The worst health you can imagine”) to 100 (“The best health you can imagine”).

The WHO-5 instrument measures subjective mental well-being referring to a period of the last two weeks (15). It is a generic scale without specific diagnostic specificity. It can be used across a wide range of study fields. It consists of five short positively-phrased questions about “feeling cheerful and in good spirits”, “feeling calm and relaxed”, “feeling active and vigorous”, “waking up feeling fresh and rested” and “daily life has been filled with things that interest me”, whereby the scale of six answers range between “all of the time” (“5”) to “at no time” (“0”). The WHO-5 index ranges from 0 (“worst imaginable well-being”) to 100 (“best imaginable well-being”), whereby these are calculated from the unweighted sum of the response scores, multiplied by 4. Using a cut-off score of ≤50 is generally recommendable when screening for clinical depression, and is the most widely used cut-off score across several different health study fields (15).

The PHQ-9 instrument assesses the presence of depressive disorders cf. DSM-IV; it also reflects depression severity, referring to a period of the last two weeks (16). The instrument consists of nine questions about how often the participant has been bothered by feelings or experiencing of “little interest or pleasure in doing things”, “down, depressed or hopeless”, “sleeping problems”, “tired or little energy”, “poor appetite or overeating”, “feeling bad about yourself”, “trouble concentrating”, “trouble moving or speaking slowly or being restless”, “thoughts of being better off dead or hurting self”. Answers are on a 4-item ordinal scale ranging between “not at all” to “nearly every day”. The PHQ-9 sum score ranges between 0 and 27, whereby depression severity is categorised into none (0–4), mild (5–9), moderate (10–14), moderately severe (15–19) and severe (20–27). The recommended cut-off score for screening for clinical depression is ≥10 (16, 17).

The GAD-7 instrument assesses the presence of generalised and other anxiety disorders and also reflects the level of anxiety in general, referring to a period of the last two weeks (18). The instrument consists of seven questions around “feeling nervous, anxious, or on edge”, “not being able to stop or control worrying”, “worrying too much about different things”, “trouble relaxing”, “being restless”, “becoming easily annoyed or irritable” and “feeling afraid as if something awful might happen”. Answers are on a 4-item ordinal scale ranging between “not at all” to “nearly every day”. The GAD-7 sum score ranges between 0 and 21, whereby anxiety severity is categorised into none (0–4), mild (5–9), moderate (10–14) and severe (15–21). The recommended cut-off score for screening for anxiety disorders is ≥8 (19, 20).

### Respondent characteristics

Data on respondent characteristics included age, sex, highest attained education level, income, country of birth, COVID-19 vaccination status, chronic conditions, occupation and living situation. The highest attained education level was categorised into “high”, “middle” and “low” based on the International Standard Classification of Education (ISCED) 2011, levels ISCED 5–8, ISCED 3–4, ISCED 0–2, respectively. Data on the monthly household income from all sources after taxes was collected for each country in their respective currency, and categorised into three groups, namely “low” (lower 20% of the countries' populations income brackets), “middle” (middle 60%) and “high” (upper 20%) income. Country of birth was dichotomised to “native” and “non-native”, based on whether the country of birth was the participant's country of occupancy (either of the six countries) or not. Chronic conditions were dichotomised to “None” or “One or more”; participants were included in the latter category if any one or more of the following chronic conditions was selected: asthma, chronic bronchitis, lung emphysema, heart disease, consequences of a stroke, diabetes, chronic rheumatoid arthritis, severe back complaints/arthrosis of the back, painful/swollen joints of knee, hip or hands due to arthrosis, situation after knee/hip replacement, cancer, memory problems due to a disease, memory problems due to ageing, depression or anxiety disorder and an open text field for other chronic health complaints. Occupation information included employed (employee or self-employed), out of work (for \>1 or \<1 year), looking after others, student, retired and unable to work. Living situation was categorised into “Living alone” (living alone; living alone with one or more children), “Living with others” (living with a partner without children/with one or more children; living with my parents without children/with one or more children; living with my parents and partner with one or more children; living with roommates) and “Other” (other).

### Disease status categorisation

For the purpose of this study, the four disease status groups were defined based on the T2 questionnaire data, namely (I) Post COVID-19 condition, (II) Acute COVID-19 infection, (III) Chronic condition(s) and (IV) Healthy, and are used throughout the study. Those participants in the first (post COVID-19 condition) group were defined by having a likely or confirmed COVID-19 infection in the past and indicating still suffering from symptoms; however, their infection did not occur within the last three months prior to when the questionnaire was sent out. Participants in the second (acute COVID-19 infection) group have the same criteria except that their infection occurred within the last three months prior to the questionnaire. These criteria are in accordance with the WHO post COVID-19 condition definition. Participants in the third \[chronic condition(s)\] group indicated suffering from one or more chronic condition(s), but do not suffer from post COVID-19 condition nor an acute COVID-19 infection. Participants in the fourth (healthy) group form the remainder of the study population.

We additionally defined disease status categories at T1, in order to investigate which health state persons developing post COVID-19 condition at T2 were transitioning from at T1. However, the questions around post COVID-19 condition at T1 differ to the improved questions at T2, due to the lack of knowledge at the time of the development of the questionnaire given this was an emerging condition. Therefore, an exclusive post COVID-19 condition group at T1 does not exist, but instead is combined with likely or confirmed acute COVID-19 infections. The definitions are outlined in further detail in <a href="#s10" data-ref-type="sec">Supplementary Table S1</a>.

### Statistical analyses

Descriptive analyses were performed for the respondent characteristics data as well as all the outcome variables (EQ-5D-5L index values, EQ VAS, WHO-5, PHQ-9 and GAD-7 sum scores). All analyses, including the longitudinal analyses, were carried out separately by disease status group at T2. For age-specific analyses, age was split by the median of the total study sample. To test for a difference in respondent characteristics across the disease groups at T2 as well as in the non-response analysis, we used the one-way ANOVA (for the continuous variable age), and the Fisher's exact and chi-square tests (for remaining categorical variables). A one-way ANOVA was applied to determine the difference in mean outcome between the disease status groups at T2. We included a multiple comparison post-hoc analysis test using the Bonferroni correction method. Detailed responses on the EQ-5D-5L dimensions and WHO-5, PHQ-9 and GAD-7 were graphically displayed through stacked bar charts, whereby the WHO-5, PHQ-9 and GAD-7 sum scores were dichotomised into “good” and “poor” so that participants with a score ≤50 for WHO-5, ≥10 for PHQ-9 and ≥8 for GAD-7 were considered as “poor”. This allowed for visual comparison of outcome patterns across the four disease groups. Change in disease status category was graphically displayed by a Sankey plot. We then determined the outcome indicator change between T1 and T2 by applying paired samples t-tests. The paired differences were calculated using the sum score ranges, thereby a positive (+ve) change in the mean from T1 to T2 is referred to as a “deterioration” in the case for the EQ-5D-5L index value, EQ VAS and WHO-5 score changes and as an “improvement” for the PHQ-9 and GAD-7 score changes. Finally, we described the association (clustering) between WHO-5, PHQ-9 and GAD-7 through Venn diagrams. A *p*-value of \<.05 was required for statistical significance. Statistical analyses were carried out using IBM SPSS version 28.0.1.0, and figures were produced using Windows Excel (Bar charts and box & whisker plots) and R Studio (Sankey plots, Venn diagrams). For the Venn diagrams, the eulerr R package was used (21).

## Results

### Study population

Out of the 19 902 respondents from Greece, Italy, the Netherlands, Sweden, the United Kingdom and the US who completed the questionnaire at T1, 4 999 (response rate: 25%) also completed the questionnaire at T2. Responders at T2 were significantly different compared to non-responders in gender, age, educational level, country and chronic conditions (<a href="#s10" data-ref-type="sec">Supplementary Table S2</a>). The response rate among countries varied between 20% among the Dutch and US respondents and 37% among Greek respondents. <a href="#T1" data-ref-type="table">Table 1</a> shows the characteristics at T2 among the 4 999 respondents in total and by disease status. At T2, the median (IQR) age of all respondents was 55 (22). Slightly more than half of all respondents were female (52.5%), high-educated (50.7%) or without chronic conditions (60.1%).

<div id="T1" class="table-wrap">

<div class="caption">

Characteristics of respondents by T2 disease status (*n* = 4,999).

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Variable</th>
<th style="text-align: center;">Categories</th>
<th style="text-align: center;">Frequency (% of variable)</th>
<th style="text-align: center;">Cases of post COVID-19 condition [<em>n</em> (%)], <em>N</em> = 240</th>
<th style="text-align: center;">Cases of acute COVID-19 infection [<em>n</em> (%)], <em>N</em> = 107</th>
<th style="text-align: center;">Cases of chronic condition(s) [<em>n</em> (%)], <em>N</em> = 1,798</th>
<th style="text-align: center;">Healthy individuals [<em>n</em> (%)], <em>N</em> = 2,854</th>
<th style="text-align: center;"><em>p</em>-value</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3" style="text-align: left;">Gender</td>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">2,372 (47.4)</td>
<td style="text-align: center;">100 (41.7)</td>
<td style="text-align: center;">48 (44.9)</td>
<td style="text-align: center;">828 (46.1)</td>
<td style="text-align: center;">1,396 (48.9)</td>
<td style="text-align: center;">.199</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">2,622 (52.5)</td>
<td style="text-align: center;">140 (58.3)</td>
<td style="text-align: center;">59 (55.1)</td>
<td style="text-align: center;">968 (53.8)</td>
<td style="text-align: center;">1,455 (51)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: center;">5 (0.1)</td>
<td style="text-align: center;"><em>0</em></td>
<td style="text-align: center;"><em>0</em></td>
<td style="text-align: center;">2 (0.1)</td>
<td style="text-align: center;">3 (0.1)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Age</td>
<td style="text-align: left;">Median (IQR)</td>
<td style="text-align: center;">55 (22)</td>
<td style="text-align: center;">49 (18)</td>
<td style="text-align: center;">52 (20)</td>
<td style="text-align: center;">60 (19)</td>
<td style="text-align: center;">52 (22)</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Mean (SD)</td>
<td style="text-align: center;">53.6 (13.7)</td>
<td style="text-align: center;">49.6 (12.9)</td>
<td style="text-align: center;">50.8 (12.9)</td>
<td style="text-align: center;">57.2 (13.2)</td>
<td style="text-align: center;">51.8 (13.6)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Age</td>
<td style="text-align: left;">18–24</td>
<td style="text-align: center;">65 (1.3)</td>
<td style="text-align: center;">3 (1.3)</td>
<td style="text-align: center;">1 (0.9)</td>
<td style="text-align: center;">20 (1.1)</td>
<td style="text-align: center;">41 (1.4)</td>
<td style="text-align: center;">.000</td>
</tr>
<tr>
<td style="text-align: left;">25–34</td>
<td style="text-align: center;">465 (9.3)</td>
<td style="text-align: center;">27 (11.3)</td>
<td style="text-align: center;">13 (12.1)</td>
<td style="text-align: center;">110 (6.1)</td>
<td style="text-align: center;">315 (11)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">35–44</td>
<td style="text-align: center;">852 (17.0)</td>
<td style="text-align: center;">57 (23.8)</td>
<td style="text-align: center;">27 (25.2)</td>
<td style="text-align: center;">205 (11.4)</td>
<td style="text-align: center;">563 (19.7)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">45–54</td>
<td style="text-align: center;">1,060 (21.2)</td>
<td style="text-align: center;">60 (25)</td>
<td style="text-align: center;">21 (19.6)</td>
<td style="text-align: center;">323 (18)</td>
<td style="text-align: center;">656 (23)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">55–64</td>
<td style="text-align: center;">1,196 (23.9)</td>
<td style="text-align: center;">58 (24.2)</td>
<td style="text-align: center;">25 (23.4)</td>
<td style="text-align: center;">476 (26.5)</td>
<td style="text-align: center;">637 (22.3)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">65–77</td>
<td style="text-align: center;">1,361 (27.2)</td>
<td style="text-align: center;">35 (14.6)</td>
<td style="text-align: center;">20 (18.7)</td>
<td style="text-align: center;">664 (36.9)</td>
<td style="text-align: center;">642 (22.5)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Country</td>
<td style="text-align: left;">Greece</td>
<td style="text-align: center;">376 (7.5)</td>
<td style="text-align: center;">12 (5)</td>
<td style="text-align: center;">10 (9.3)</td>
<td style="text-align: center;">140 (7.8)</td>
<td style="text-align: center;">214 (7.5)</td>
<td style="text-align: center;">.000</td>
</tr>
<tr>
<td style="text-align: left;">Italy</td>
<td style="text-align: center;">1,165 (23.3)</td>
<td style="text-align: center;">49 (20.4)</td>
<td style="text-align: center;">19 (17.8)</td>
<td style="text-align: center;">356 (19.8)</td>
<td style="text-align: center;">741 (26)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">The Netherlands</td>
<td style="text-align: center;">644 (12.9)</td>
<td style="text-align: center;">34 (14.2)</td>
<td style="text-align: center;">19 (17.8)</td>
<td style="text-align: center;">272 (15.1)</td>
<td style="text-align: center;">319 (11.2)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Sweden</td>
<td style="text-align: center;">729 (14.6)</td>
<td style="text-align: center;">50 (20.8)</td>
<td style="text-align: center;">10 (9.3)</td>
<td style="text-align: center;">343 (19.1)</td>
<td style="text-align: center;">326 (11.4)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">United Kingdom</td>
<td style="text-align: center;">873 (17.5)</td>
<td style="text-align: center;">52 (21.7)</td>
<td style="text-align: center;">30 (28)</td>
<td style="text-align: center;">287 (16)</td>
<td style="text-align: center;">504 (17.7)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">United States</td>
<td style="text-align: center;">1,212 (24.2)</td>
<td style="text-align: center;">43 (17.9)</td>
<td style="text-align: center;">19 (17.8)</td>
<td style="text-align: center;">400 (22.2)</td>
<td style="text-align: center;">750 (26.3)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Country of birth<a href="#table-fn1" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: left;">Native</td>
<td style="text-align: center;">4,719 (94.4)</td>
<td style="text-align: center;">229 (95.4)</td>
<td style="text-align: center;">102 (95.3)</td>
<td style="text-align: center;">1,700 (94.5)</td>
<td style="text-align: center;">2,688 (94.2)</td>
<td style="text-align: center;">.808</td>
</tr>
<tr>
<td style="text-align: left;">Non-native</td>
<td style="text-align: center;">280 (5.6)</td>
<td style="text-align: center;">11 (4.6)</td>
<td style="text-align: center;">5 (4.7)</td>
<td style="text-align: center;">98 (5.5)</td>
<td style="text-align: center;">166 (5.8)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Chronic condition(s)<a href="#table-fn3" data-ref-type="table-fn"><sup>£</sup></a></td>
<td style="text-align: left;">None</td>
<td style="text-align: center;">3,004 (60.1)</td>
<td style="text-align: center;">96 (40)</td>
<td style="text-align: center;">54 (50.5)</td>
<td style="text-align: center;">NA</td>
<td style="text-align: center;">2,854 (100)</td>
<td style="text-align: center;">.069</td>
</tr>
<tr>
<td style="text-align: left;">One or more</td>
<td style="text-align: center;">1,995 (39.9)</td>
<td style="text-align: center;">144 (60)<a href="#table-fn2" data-ref-type="table-fn"><sup>$</sup></a></td>
<td style="text-align: center;">53 (49.5)</td>
<td style="text-align: center;">1,798 (100)</td>
<td style="text-align: center;">NA</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">COVID-19 vaccination status</td>
<td style="text-align: left;">Yes</td>
<td style="text-align: center;">4,427 (88.6)</td>
<td style="text-align: center;">212 (88.3)</td>
<td style="text-align: center;">91 (85)</td>
<td style="text-align: center;">1,630 (90.7)</td>
<td style="text-align: center;">2,494 (87.4)</td>
<td style="text-align: center;">.005</td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td style="text-align: center;">572 (11.4)</td>
<td style="text-align: center;">28 (11.7)</td>
<td style="text-align: center;">16 (15)</td>
<td style="text-align: center;">168 (9.3)</td>
<td style="text-align: center;">360 (12.6)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Education level<a href="#table-fn1" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: left;">High</td>
<td style="text-align: center;">2,534 (50.7)</td>
<td style="text-align: center;">127 (52.9)</td>
<td style="text-align: center;">64 (59.8)</td>
<td style="text-align: center;">817 (45.4)</td>
<td style="text-align: center;">1,526 (53.3)</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">1,973 (39.5)</td>
<td style="text-align: center;">88 (36.7)</td>
<td style="text-align: center;">37 (34.6)</td>
<td style="text-align: center;">764 (42.5)</td>
<td style="text-align: center;">1,084 (38)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">492 (9.8)</td>
<td style="text-align: center;">25 (10.4)</td>
<td style="text-align: center;">6 (5.6)</td>
<td style="text-align: center;">217 (12.1)</td>
<td style="text-align: center;">244 (8.5)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Income level</td>
<td style="text-align: left;">High</td>
<td style="text-align: center;">782 (15.6)</td>
<td style="text-align: center;">40 (16.7)</td>
<td style="text-align: center;">14 (13.1)</td>
<td style="text-align: center;">247 (13.7)</td>
<td style="text-align: center;">481 (16.9)</td>
<td style="text-align: center;">.005</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">2,867 (57.4)</td>
<td style="text-align: center;">131 (54.6)</td>
<td style="text-align: center;">69 (64.5)</td>
<td style="text-align: center;">1,015 (56.5)</td>
<td style="text-align: center;">1,652 (57.9)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">1,350 (27)</td>
<td style="text-align: center;">69 (28.7)</td>
<td style="text-align: center;">24 (22.4)</td>
<td style="text-align: center;">536 (29.8)</td>
<td style="text-align: center;">721 (25.3)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="8" style="text-align: left;">Occupation</td>
<td style="text-align: left;">Employed (employee)</td>
<td style="text-align: center;">2,358 (47.2)</td>
<td style="text-align: center;">124 (51.7)</td>
<td style="text-align: center;">58 (54.2)</td>
<td style="text-align: center;">628 (34.9)</td>
<td style="text-align: center;">1,548 (54.2)</td>
<td style="text-align: center;">.000</td>
</tr>
<tr>
<td style="text-align: left;">Employed (self-employed)</td>
<td style="text-align: center;">395 (7.9)</td>
<td style="text-align: center;">20 (8.3)</td>
<td style="text-align: center;">8 (7.5)</td>
<td style="text-align: center;">117 (6.5)</td>
<td style="text-align: center;">250 (8.8)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Out of work for &gt;1 year</td>
<td style="text-align: center;">327 (6.5)</td>
<td style="text-align: center;">22 (9.2)</td>
<td style="text-align: center;">4 (3.7)</td>
<td style="text-align: center;">119 (6.6)</td>
<td style="text-align: center;">182 (6.4)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Out of work for &lt;1 year</td>
<td style="text-align: center;">71 (1.4)</td>
<td style="text-align: center;">5 (2.1)</td>
<td style="text-align: center;"><em>0</em></td>
<td style="text-align: center;">30 (1.7)</td>
<td style="text-align: center;">36 (1.3)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Looking after others</td>
<td style="text-align: center;">204 (4.1)</td>
<td style="text-align: center;">9 (3.8)</td>
<td style="text-align: center;">2 (1.9)</td>
<td style="text-align: center;">60 (3.3)</td>
<td style="text-align: center;">133 (4.7)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Student</td>
<td style="text-align: center;">66 (1.3)</td>
<td style="text-align: center;">3 (1.3)</td>
<td style="text-align: center;">1 (0.9)</td>
<td style="text-align: center;">23 (1.3)</td>
<td style="text-align: center;">39 (1.4)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: center;">1,369 (27.4)</td>
<td style="text-align: center;">38 (15.8)</td>
<td style="text-align: center;">23 (21.5)</td>
<td style="text-align: center;">671 (37.3)</td>
<td style="text-align: center;">637 (22.3)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Unable to work</td>
<td style="text-align: center;">209 (4.2)</td>
<td style="text-align: center;">19 (7.9)</td>
<td style="text-align: center;">11 (10.3)</td>
<td style="text-align: center;">150 (8.3)</td>
<td style="text-align: center;">29 (1)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Living situation</td>
<td style="text-align: left;">Living alone</td>
<td style="text-align: center;">1,464 (29.3)</td>
<td style="text-align: center;">60 (25)</td>
<td style="text-align: center;">39 (36.4)</td>
<td style="text-align: center;">601 (33.4)</td>
<td style="text-align: center;">764 (26.8)</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">Living with others</td>
<td style="text-align: center;">3,506 (70.1)</td>
<td style="text-align: center;">178 (74.2)</td>
<td style="text-align: center;">68 (63.6)</td>
<td style="text-align: center;">1,182 (65.7)</td>
<td style="text-align: center;">2,078 (72.8)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: center;">29 (0.6)</td>
<td style="text-align: center;">2 (0.8)</td>
<td style="text-align: center;"><em>0</em></td>
<td style="text-align: center;">15 (0.8)</td>
<td style="text-align: center;">12 (0.4)</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

Variable data is based on data retrieved at T1 POPCORN questionnaire and not T2.

None of the chronic condition(s) listed by individuals in the post COVID-19 condition group were post COVID-19 condition or any similar name.

The chi-square test was only applied to the acute COVID-19 infection and post COVID-19 condition groups. The *p*-value corresponds to the tests of independence between disease status groups.

</div>

### Description of respondents according to disease status

At T2, 240 (5%) were considered to have post COVID-19 condition, 107 (2%) had an acute COVID-19 infection, 1,798 (36%) had one or more chronic condition(s) and 2,854 (57%) participants were presumably healthy (<a href="#T1" data-ref-type="table">Table 1</a> and <a href="#s10" data-ref-type="sec">Supplementary Table S1</a>).

In <a href="#T1" data-ref-type="table">Table 1</a>, the age distribution differed between the disease groups, with the median (IQR) age in the post COVID-19 condition group \[49 (18)\] being the lowest and highest in the chronic condition(s) group \[60 (19)\] compared to the other groups. Country, COVID-19 vaccination status, educational level, income level, occupation and living situation also differed across the disease status groups, while country of birth and chronic condition(s) (between only the acute COVID-19 infection and post COVID-19 condition groups), did not. Notably still, 60% of persons with post COVID-19 condition had one or more chronic condition(s) at T2, compared to 39.9% in the total sample population (<a href="#T1" data-ref-type="table">Table 1</a>). In analysing the transition in disease status from T1 to T2 (<a href="#F1" data-ref-type="fig">Figure 1</a>), the largest proportion of participants with post COVID-19 condition at T2 was previously in the chronic condition(s) group at T1 (*n* = 116, 48.3%), followed by 80 (33.3%) from the healthy group and 44 (18.3%) from the possible acute or past COVID-19 infection group. Therefore, when having one or more chronic condition(s) at T1, the likelihood of having post COVID-19 condition was 5.9%, compared to 3.0% when being healthy. The group of individuals who had chronic condition(s) at T1 and became healthy at T2 were separately analysed due to the large number transitioning between these states (<a href="#s10" data-ref-type="sec">Supplementary Figure S1</a>).

<figure id="F1">
<p><img src="fepid-03-1144162-g001.jpg" /></p>
<p><img src="fepid-03-1144162-g001.gif" /></p>
<figcaption>Transitions between disease status groups in 2020 (T1) [healthy, chronic condition(s), possible acute or past COVID-19 infection] to 2022 (T2) [healthy, chronic condition(s), acute COVID-19 infection and post COVID-19 condition].</figcaption>
</figure>

### Primary outcomes at T2

<a href="#F2" data-ref-type="fig">Figure 2</a> shows that healthy participants reported the lowest rates of any problems (slight to extreme problems/unable to) in all EQ-5D-5L dimensions, whereby the post COVID-19 condition group reported the highest rates of any problems, compared to all other groups. The T2 EQ-5D-5L index value (<a href="#F4" data-ref-type="fig">Figure 4A</a>) was lowest among the post COVID-19 condition group \[mean (SD) = 0.70 (0.29)\], followed by the acute COVID-19 infection group \[0.73 (0.29)\], the chronic condition(s) group \[0.75 (0.25)\], and highest in the healthy group \[0.92 (0.12)\]. For the EQ VAS (<a href="#F4" data-ref-type="fig">Figure 4B</a>), the lowest HRQOL was reported in the acute COVID-19 infection group \[mean (SD) = 65.1 (20.1)\], followed by the post COVID-19 condition group \[65.7 (21.0)\], the chronic condition(s) group \[68.4 (19.8)\], and highest in the healthy group \[80.8 (14.3)\]. The pattern in the EQ-5D-5L respondent rates per dimension between disease groups is largely maintained across the two age groups, 18–54 and 55–77, compared to the total study sample at T2 (<a href="#s10" data-ref-type="sec">Supplementary Figures S2A,B</a>).

<figure id="F2">
<p><img src="fepid-03-1144162-g002.jpg" /></p>
<p><img src="fepid-03-1144162-g002.gif" /></p>
<figcaption>Percentage of respondents per level per EQ-5D-5L dimension in 2020 (T1) and 2022 (T2), by T2 disease status.</figcaption>
</figure>

<figure id="F4">
<p><img src="fepid-03-1144162-g004.jpg" /></p>
<p><img src="fepid-03-1144162-g004.gif" /></p>
<figcaption>(<strong>A–E</strong>): Mean and median EQ-5D-5L index value (<strong>A</strong>), EQ VAS score (<strong>B</strong>), WHO-5 sum score (<strong>C</strong>), PHQ-9 sum score (<strong>D</strong>) and GAD-7 sum score (<strong>E</strong>) in 2020 (T1) and 2022 (T2), by T2 disease status. The X denotes the mean, the line in the box the median, the box is the interquartile range, and the whiskers are the minimum and maximum points with outliers removed and depicted as dots. For the (<strong>A</strong>) EQ-5D-5L index values we used the United States value set. EQ-5D-5L index values range from less than 0 (worse than death) to 1. The (<strong>B</strong>) EQ VAS (Visual analogue scale) ranges from 0 (worst self-rated health) to 100 (best self-rated health). The (<strong>C</strong>) WHO-5 sum score (WHO-5 Well-being index) ranges from 0 (worst imaginable well-being) to 100 (best imaginable well-being). The (<strong>D</strong>) PHQ-9 sum score (Patient health questionnaire 9) ranges from 0 to 27 (Mild: 5–9, Moderate: 10–14, Moderately severe: 15–19, Severe: 20–27). The (<strong>E</strong>) GAD-7 sum score (General anxiety disorder 7-item scale) ranges from 0 to 21 (Mild: 5–9, Moderate: 10–14, Severe: 15–21).</figcaption>
</figure>

Rates for poor mental well-being, depression and anxiety disorder at T2 (<a href="#F3" data-ref-type="fig">Figure 3</a>) were highest in the post COVID-19 condition group followed by the acute COVID-19 infection group, the chronic condition(s) group, and lowest in the healthy group. In <a href="#F4" data-ref-type="fig">Figures 4C–E</a>, the mean (SD) scores are lowest in the post COVID-19 condition group \[WHO-5: 47.7 (26.7); PHQ-9: 9.1 (6.7); GAD-7: 7.4 (5.8)\], followed by the acute COVID-19 infection group \[WHO-5: 51.1 (25.6); PHQ-9: 7.7 (6.5); GAD-7: 5.7 (5.7)\], the chronic condition(s) group \[WHO-5: 56.1 (25.9); PHQ-9: 5.2 (5.6); GAD-7: 4.2 (4.9)\], and highest for the healthy group \[WHO-5: 65.6 (23.2); PHQ-9: 2.8 (4.0); GAD-7: 2.5 (3.8)\]. Comparing the two age groups, 18–54 and 55–77, the younger population had overall higher rates of poor mental well-being (WHO-5, PHQ-9 and GAD-7) at T2 (<a href="#s10" data-ref-type="sec">Supplementary Figures S3A,B</a>). The difference in means between the disease status groups in all the HRQOL and mental well-being outcomes was significant (*p* \< .001) (see <a href="#s10" data-ref-type="sec">Supplementary Table S3</a> for <a href="#F4" data-ref-type="fig">Figures 4A–E</a> values).

<figure id="F3">
<p><img src="fepid-03-1144162-g003.jpg" /></p>
<p><img src="fepid-03-1144162-g003.gif" /></p>
<figcaption>Percentage of respondents with poor mental health according to the WHO-5, PHQ-9 and GAD-7 in 2020 (T1) and 2022 (T2), by T2 disease status. The WHO-5 well-being index measures overall mental well-being, whereby poor mental well-being ranges from 0 to 50 points and good mental well-being from 51 to 100 points. The Patient health questionnaire 9 (PHQ-9) measures depression, whereby depression (i.e. “poor PHQ-9”) includes moderate, moderately severe and severe depression, which ranges from 10 to 27. The General anxiety disorder 7-item scale (GAD-7) measures anxiety, whereby having anxiety (i.e. “poor GAD-7”) includes mild, moderate and severe anxiety from the raw score (ranging from 8 to 21), and no anxiety ranges between 0 and 7.</figcaption>
</figure>

In the multiple comparison post-hoc analysis test across disease status groups, the mean difference between the post COVID-19 condition group was statistically significantly different (*p* \< .001) compared to the healthy group (EQ-5D-5L index: mean difference = .220; EQ VAS: 15.1; WHO-5: 17.9; PHQ-9: −6.3 GAD-7: −4.9), the chronic condition(s) group (EQ-5D-5L index:.05; WHO-5: 8.4; PHQ-9: −3.9; GAD-7: −3.3) and the acute COVID-19 infection group (GAD-7: −1.7, *p* = .004) (<a href="#s10" data-ref-type="sec">Supplementary Table S4</a>).

### Change (T1 to T2) in primary outcomes

From T1 to T2, rates of any problems (slight to extreme problems/unable to) deteriorated in all EQ-5D-5L dimensions among all disease status groups, apart from the healthy group who improved slightly in the self-care, usual activities and anxiety/depression dimensions and the chronic condition(s) group in the anxiety/depression dimension (<a href="#F2" data-ref-type="fig">Figure 2</a>). From T1 to T2, HRQOL deteriorated in all four groups, except for the healthy group (EQ-5D-5L index: Δ0.005, *p* = .035) (<a href="#T2" data-ref-type="table">Table 2</a> and <a href="#s10" data-ref-type="sec">Supplementary Tables S3</a>). We observed the largest deterioration in the EQ-5D-5L index value in the chronic condition(s) group (EQ-5D-5L index: Δ0.03, *p* \< .001). The largest deterioration in EQ VAS was observed in the acute COVID-19 infection group (EQ VAS: Δ6.3, *p* \< .001) followed by the post COVID-19 condition group (EQ VAS: Δ4.96, *p* \< .001).

<div id="T2" class="table-wrap">

<div class="caption">

Paired samples t-test for the change between T1 and T2, by disease status.

</div>

<table>
<thead>
<tr>
<th colspan="2" rowspan="3" style="text-align: left;">Disease status</th>
<th colspan="5" style="text-align: center;">Paired Differences</th>
<th rowspan="3" style="text-align: center;"><em>t</em></th>
<th rowspan="3" style="text-align: center;"><em>df</em></th>
<th rowspan="3" style="text-align: center;">Sig. (2-tailed)</th>
</tr>
<tr>
<th rowspan="2" style="text-align: center;">Mean</th>
<th rowspan="2" style="text-align: center;">Std. Dev.</th>
<th rowspan="2" style="text-align: center;">Std. Error Mean</th>
<th colspan="2" style="text-align: center;">95% confidence interval of the difference</th>
</tr>
<tr>
<th style="text-align: center;">Lower</th>
<th style="text-align: center;">Upper</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;">Healthy</td>
<td style="text-align: left;">EQ-5D-5L index value at T1 and T2<a href="#table-fn5" data-ref-type="table-fn"><sup>1</sup></a></td>
<td style="text-align: center;">−0.005<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">0.12</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: center;">−0.01</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: center;">−2.1</td>
<td style="text-align: center;">2,853</td>
<td style="text-align: center;">0.035</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS score at T1 and T2<a href="#table-fn6" data-ref-type="table-fn"><sup>2</sup></a></td>
<td style="text-align: center;">1.402<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">12.72</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: center;">1.87</td>
<td style="text-align: center;">5.9</td>
<td style="text-align: center;">2,853</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">WHO-5 sum score at T1 and T2<a href="#table-fn7" data-ref-type="table-fn"><sup>3</sup></a></td>
<td style="text-align: center;">0.408</td>
<td style="text-align: center;">19.89</td>
<td style="text-align: center;">0.37</td>
<td style="text-align: center;">−0.32</td>
<td style="text-align: center;">1.14</td>
<td style="text-align: center;">1.1</td>
<td style="text-align: center;">2,853</td>
<td style="text-align: center;">0.273</td>
</tr>
<tr>
<td style="text-align: left;">PHQ-9 sum score at T1 and T2<a href="#table-fn8" data-ref-type="table-fn"><sup>4</sup></a></td>
<td style="text-align: center;">0.754<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">3.72</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;">10.8</td>
<td style="text-align: center;">2,853</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">GAD-7 sum score at T1 and T2<a href="#table-fn9" data-ref-type="table-fn"><sup>5</sup></a></td>
<td style="text-align: center;">1.272<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">3.68</td>
<td style="text-align: center;">0.07</td>
<td style="text-align: center;">0.97</td>
<td style="text-align: center;">1.24</td>
<td style="text-align: center;">16.0</td>
<td style="text-align: center;">2,853</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">Chronic condition(s)</td>
<td style="text-align: left;">EQ-5D-5L index value at T1 and T2<a href="#table-fn5" data-ref-type="table-fn"><sup>1</sup></a></td>
<td style="text-align: center;">0.027<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">0.00</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: center;">0.04</td>
<td style="text-align: center;">6.8</td>
<td style="text-align: center;">1,797</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS score at T1 and T2<a href="#table-fn6" data-ref-type="table-fn"><sup>2</sup></a></td>
<td style="text-align: center;">3.226<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">16.72</td>
<td style="text-align: center;">0.39</td>
<td style="text-align: center;">2.45</td>
<td style="text-align: center;">4.00</td>
<td style="text-align: center;">8.2</td>
<td style="text-align: center;">1,797</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">WHO-5 sum score at T1 and T2<a href="#table-fn7" data-ref-type="table-fn"><sup>3</sup></a></td>
<td style="text-align: center;">2.516<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">20.14</td>
<td style="text-align: center;">0.48</td>
<td style="text-align: center;">1.58</td>
<td style="text-align: center;">3.45</td>
<td style="text-align: center;">5.3</td>
<td style="text-align: center;">1,797</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">PHQ-9 sum score at T1 and T2<a href="#table-fn8" data-ref-type="table-fn"><sup>4</sup></a></td>
<td style="text-align: center;">0.182</td>
<td style="text-align: center;">4.34</td>
<td style="text-align: center;">0.10</td>
<td style="text-align: center;">−0.02</td>
<td style="text-align: center;">0.38</td>
<td style="text-align: center;">1.8</td>
<td style="text-align: center;">1,797</td>
<td style="text-align: center;">0.075</td>
</tr>
<tr>
<td style="text-align: left;">GAD-7 sum score at T1 and T2<a href="#table-fn9" data-ref-type="table-fn"><sup>5</sup></a></td>
<td style="text-align: center;">0.561<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">3.96</td>
<td style="text-align: center;">0.09</td>
<td style="text-align: center;">0.38</td>
<td style="text-align: center;">0.74</td>
<td style="text-align: center;">6.0</td>
<td style="text-align: center;">1,797</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">Acute COVID-19 infection</td>
<td style="text-align: left;">EQ-5D-5L index value at T1 and T2<a href="#table-fn5" data-ref-type="table-fn"><sup>1</sup></a></td>
<td style="text-align: center;">0.018</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">0.02</td>
<td style="text-align: center;">−0.02</td>
<td style="text-align: center;">0.05</td>
<td style="text-align: center;">1.1</td>
<td style="text-align: center;">106</td>
<td style="text-align: center;">0.295</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS score at T1 and T2<a href="#table-fn6" data-ref-type="table-fn"><sup>2</sup></a></td>
<td style="text-align: center;">6.327<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">17.78</td>
<td style="text-align: center;">1.72</td>
<td style="text-align: center;">2.92</td>
<td style="text-align: center;">9.74</td>
<td style="text-align: center;">3.7</td>
<td style="text-align: center;">106</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">WHO-5 sum score at T1 and T2<a href="#table-fn7" data-ref-type="table-fn"><sup>3</sup></a></td>
<td style="text-align: center;">4.785<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">20.26</td>
<td style="text-align: center;">1.96</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: center;">8.67</td>
<td style="text-align: center;">2.4</td>
<td style="text-align: center;">106</td>
<td style="text-align: center;">0.016</td>
</tr>
<tr>
<td style="text-align: left;">PHQ-9 sum score at T1 and T2<a href="#table-fn8" data-ref-type="table-fn"><sup>4</sup></a></td>
<td style="text-align: center;">−1.252<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">5.07</td>
<td style="text-align: center;">0.49</td>
<td style="text-align: center;">−2.22</td>
<td style="text-align: center;">−0.28</td>
<td style="text-align: center;">−2.6</td>
<td style="text-align: center;">106</td>
<td style="text-align: center;">0.012</td>
</tr>
<tr>
<td style="text-align: left;">GAD-7 sum score at T1 and T2<a href="#table-fn9" data-ref-type="table-fn"><sup>5</sup></a></td>
<td style="text-align: center;">−0.168</td>
<td style="text-align: center;">4.30</td>
<td style="text-align: center;">0.42</td>
<td style="text-align: center;">−0.99</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">−0.4</td>
<td style="text-align: center;">106</td>
<td style="text-align: center;">0.687</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">Post COVID-19 condition</td>
<td style="text-align: left;">EQ-5D-5L index value at T1 and T2<a href="#table-fn5" data-ref-type="table-fn"><sup>1</sup></a></td>
<td style="text-align: center;">0.023</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">0.01</td>
<td style="text-align: center;">−0.00</td>
<td style="text-align: center;">0.05</td>
<td style="text-align: center;">1.7</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">0.099</td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS score at T1 and T2<a href="#table-fn6" data-ref-type="table-fn"><sup>2</sup></a></td>
<td style="text-align: center;">4.963<a href="#table-fn10" data-ref-type="table-fn"><sup>*</sup></a></td>
<td style="text-align: center;">15.09</td>
<td style="text-align: center;">0.97</td>
<td style="text-align: center;">3.04</td>
<td style="text-align: center;">6.88</td>
<td style="text-align: center;">5.1</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">&lt;.001</td>
</tr>
<tr>
<td style="text-align: left;">WHO-5 sum score at T1 and T2<a href="#table-fn7" data-ref-type="table-fn"><sup>3</sup></a></td>
<td style="text-align: center;">2.567</td>
<td style="text-align: center;">23.34</td>
<td style="text-align: center;">1.51</td>
<td style="text-align: center;">−0.40</td>
<td style="text-align: center;">5.53</td>
<td style="text-align: center;">1.7</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">0.09</td>
</tr>
<tr>
<td style="text-align: left;">PHQ-9 sum score at T1 and T2<a href="#table-fn8" data-ref-type="table-fn"><sup>4</sup></a></td>
<td style="text-align: center;">−0.388</td>
<td style="text-align: center;">5.76</td>
<td style="text-align: center;">0.37</td>
<td style="text-align: center;">−1.12</td>
<td style="text-align: center;">0.35</td>
<td style="text-align: center;">−1.0</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">0.298</td>
</tr>
<tr>
<td style="text-align: left;">GAD-7 sum score at T1 and T2<a href="#table-fn9" data-ref-type="table-fn"><sup>5</sup></a></td>
<td style="text-align: center;">0.204</td>
<td style="text-align: center;">5.42</td>
<td style="text-align: center;">0.35</td>
<td style="text-align: center;">−0.49</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: center;">0.6</td>
<td style="text-align: center;">239</td>
<td style="text-align: center;">0.56</td>
</tr>
</tbody>
</table>

A positive (+ve) difference in the mean from T1 to T2 is a “deterioration” in the case of the EQ-5D-5L index value, EQ VAS and WHO-5 score changes, and as an “improvement” for the PHQ-9 and GAD-7 score changes.

Pair 1 (EQ-5D-5L index value at T1 and T2).

Pair 2 (EQ VAS score at T1 and T2).

Pair 3 (WHO-5 sum score at T1 and T2).

Pair 4 (PHQ-9 sum score at T1 and T2).

Pair 5 (GAD-7 sum score at T1 and T2).

The mean difference is significant at the 0.05 level.

</div>

From T1 to T2, rates in poor mental well-being measured with WHO-5 remained stable in the healthy group and deteriorated in the other disease status groups (<a href="#F3" data-ref-type="fig">Figure 3</a>), whereby this was statistically significant in the chronic condition(s) group (Δ2.5, *p* \< .001) and in the acute COVID-19 infection group (Δ4.8, *p* = .016) (<a href="#T2" data-ref-type="table">Table 2</a>). The change in PHQ-9 rates for depression were a mix of improvement in the healthy group (Δ0.8, *p* \< .001) and deterioration in the acute COVID-19 infection group (Δ-1.3, *p* = .012) (<a href="#T2" data-ref-type="table">Table 2</a>). The GAD-7 rates for anxiety improved from T1 to T2 in all groups except for the acute COVID-19 infection group (<a href="#F3" data-ref-type="fig">Figure 3</a>), whereby this was statistically significant in the healthy participants (Δ1.3, *p* \< .001) and the chronic condition(s) group (Δ0.6, *p* \< .001) (<a href="#T2" data-ref-type="table">Table 2</a>). This pattern is largely maintained across the two age groups, 18–54 and 55–77, with only slight differences in rates such as in the post COVID-19 condition group for anxiety improving in the 18–54 age group compared to deteriorating in the 55–77 age group (<a href="#s10" data-ref-type="sec">Supplementary Figures S3A,B</a>).

### Overlap in mental well-being outcomes

<a href="#F5" data-ref-type="fig">Figures 5A–D</a> present the co-occurrence of poor mental well-being, depression and anxiety for each disease status group. Healthy participants presented the largest group of unaffected respondents \[2,149 (75%)\] and the least overlap of all three outcomes \[108 (4%)\], in contrast to the post COVID-19 condition group who had the lowest number of unaffected respondents 84 (35%) and the most overlap \[66 (27.5%)\]. In the acute COVID-19 infection group, 23 (21.5%) respondents reported poor mental well-being on all outcomes and 206 (11.5%) respondents from the chronic condition(s) group. Correlations between HRQOL and mental health outcomes are presented in <a href="#s10" data-ref-type="sec">Supplementary Table S5</a>, whereby all were positively correlated and significant.

<figure id="F5">
<p><img src="fepid-03-1144162-g005.jpg" /></p>
<p><img src="fepid-03-1144162-g005.gif" /></p>
<figcaption>Overlap of poor mental well-being (WHO-5), depression (PHQ-9) and anxiety (GAD-7) at T2 in (A) healthy respondents (n=2854), (B) chronic condition(s) respondents (n = 1798), (C) acute COVID-19 infection respondents (n = 107) and (D) post COVID-19 condition respondents (n = 240).</figcaption>
</figure>

## Discussion

### Key findings and comparative studies

Our study showed that participants with post COVID-19 condition overall had a higher prevalence of any problems on the EQ-5D-5L descriptive system in terms of mobility, self-care, usual activities, pain/discomfort and anxiety/depression, compared to the other disease groups. Furthermore, participants with post COVID-19 condition exhibited the worst HRQOL (mean and median EQ-5D-5L and EQ VAS) as compared to the other three groups, apart from the acute COVID-19 infection group reporting a slightly worse EQ VAS outcome. The prevalence of any problems on the EQ-5D-5L descriptive system observed in our post COVID-19 condition group was higher than the prevalence reported by Malik et al. in their meta-analysis of 12 studies on HRQOL of post COVID-19 condition patients (6). In addition, the mean EQ VAS score of respondents with post COVID-19 condition was lower than that of the meta-analysis (6). This discrepancy in findings may be due to a difference in the definition of post COVID-19 condition that was used. In the study of Malik et al., the case definition did not include a restriction on the duration since the acute COVID-19 infection, whereas in our study a respondent was identified as having post COVID-19 condition if symptoms were still occurring 3 months or longer since after the acute COVID-19 infection. Moreover, the discrepancy in HRQOL may further be explained by the relatively high proportion of respondents having co-morbid condition(s) in our post COVID-19 condition group (60% prevalence), compared to the studies included in the meta-analysis. We doubt whether this is a valid comparison, as the source studies of the meta-analysis did not include a similar extensive risk factor and comorbidity list with complete checking. We therefore attribute the higher HRQOL impact in our study mainly to a selection-through-definition effect.

As in the example above, few studies have used a restrictive minimum symptom duration of 3 months post-acute infection as corresponds to the WHO post COVID-19 condition case definition. In addition, even fewer studies have sought to compare this with a healthy group or other comparative (sub)population. One study included a comparison of HRQOL (median EQ-5D-5L and EQ VAS) between persons with post COVID-19 condition to persons with an acute COVID-19 infection with symptoms not lasting beyond 12 weeks or no symptoms at all, without a healthy control group. The former group's HRQOL (in both measures), were statistically significantly worse than the latter group's (22). This comparison holds true in our study, apart from the mean EQ VAS score being slightly worse in the acute COVID-19 infection group, although this was not statistically significant. This may be due to a difference in the acute COVID-19 infection group definitions, which in our definition does not include non-symptomatic infections. In a further study, HRQOL measured with the SF-36 was compared between a group of patients considered to have “long COVID” and a healthy control group consisting of young people at universities, however these participants were solely presumed to be healthy. Not surprisingly, the comparison demonstrated a significantly worse HRQOL in the “long COVID” group (23). Another study comparing a group of post-COVID-19 infected persons with persisting symptoms to a normative general population, observed better HRQOL in both the EQ-5D-3l and EQ VAS in the latter group (24). A detailed comparison of their mean scores to our data, showed even worse HRQOL in the post-COVID-19 infected persons compared to our post COVID-19 condition sample (EQ-5D-3l index value = 0.57 vs. EQ-5D-5L index value = 0.70; EQ VAS = 56.6 vs. 65.7, respectively). An obvious explanation for the comparatively low HRQOL scores, is that the post-COVID-19 infected patients were not specifically defined, and by use of a convenience sample, leading to selection bias.

Similar to HRQOL, poor mental well-being was also most prevalent in post COVID-19 condition participants compared to the other groups in our study. In a large matched cohort study including 145,184 adults with post COVID-19 condition and 723,165 matched controls that were not infected with SARS-CoV-2, the incidence rate ratio for mental health problems, which include depression and anxiety disorders among others, was found to be 1.27 (95% CI: 1.25–1.29) in the former group compared to the matched controls (25). Though we did not measure incidence, the higher prevalence of poor mental well-being in the post COVID-19 condition group compared to the remaining groups can be an indication of an increased incidence in this group relative to the others. Similarly, in the few studies where a control group was used, depression and anxiety were more frequent among those with persisting symptoms after a COVID-19 infection (however duration of persisting symptoms is not defined) compared to the healthy participants (5). Furthermore, rather than evaluating self-reported health questionnaires, a further study sought to evaluate diagnoses of psychiatric disorders, which include psychiatric illness, mood and anxiety disorder, in COVID-19 survivors (not specifically post COVID-19 condition). In this study, it was found that the COVID-19 survivors had a roughly doubled risk of having a newly diagnosed psychiatric disorder 14 to 90 days after a COVID-19 infection compared to matched cohorts that had been diagnosed with another similar health event (such as influenza, respiratory tract infection, skin infection or fracture of a large bone) (26). Though the COVID-19 survivors are not an entirely comparable group to those with post COVID-19 condition, a proportion of the survivors will go on to develop post COVID-19 condition, and the results alone indicate the possible long-term effects that are encountered in post COVID-19 condition. Together, these corroborate our findings that persons with post COVID-19 condition have significantly poorer mental health compared to our remaining groups.

When analysing the longitudinal data over the two years, rates of any problems in HRQOL increased in all groups apart from a few exceptions in healthy and chronic condition(s) participants, with the post COVID-19 condition group already having a higher prevalence of any problems in HRQOL compared to the remaining groups in 2020. Our study's finding that an increased risk in acquiring post COVID-19 condition is associated with prior presence of one or more chronic conditions, corresponds to previous studies that detected a 26% increased risk for individuals with pre-existing comorbidities (27). Furthermore, a strong predictor for post COVID-19 condition was overall burden of comorbidity in the study by Förster et al. (22). Similarly, in a study where information on pre-existing chronic conditions was systematically gathered, the authors found that having one, 2–3 and 4 or more chronic conditions inferred between 23% - 121% and 16% - 90% increased risk among those not having recovered at all or having only partially recovered, respectively, 12 and 18 months after a symptomatic COVID-19 infection (8).

Provided the overall deterioration of HRQOL in this group from 2020 to 2022, we expected to see a similar pattern in all three mental well-being outcomes. However, an overall decrease in the rate of anxiety in the majority of the disease groups as well as a significant improvement in the mean anxiety levels in the healthy and chronic condition(s) participants was detected. This could be due to a global decrease in anxiety due to the adaptation to the novelty of the COVID-19 pandemic and the morbidity and mortality associated with it. In the US, the National Center for Health Statistics estimated the prevalence of symptoms of anxiety disorder, which has also been steadily declining from April 2020 (32.8%) to 2021 (30.5%) to the end of 2022 (28.8%) (28). Moreover, the decrease in rates of anxiety may be due to the alleviation of governmentally induced restrictions or lockdowns in 2022 in the six included countries, as previous findings of the POPCORN study showed that the stringency of government response is associated with worse mental well-being (12).

### Strengths and limitations

Strengths of our study are the longitudinal study design, which allow for the comparison of HRQOL and mental well-being from the beginning of the COVID-19 pandemic in 2020 to later phases of the pandemic, while also enabling the determination of the impact of post COVID-19 condition on HRQOL and mental well-being without having to rely on recall data. Another strength includes the comparison between persons with post COVID-19 condition to three further defined and mutually exclusive health states, which has been lacking so far in the literature. However, the accuracy of the post COVID-19 condition group cannot be guaranteed given the self-reported nature of the questionnaire, and the inclusion of “probable” COVID-19 infections in this group. Furthermore, compared to the chronic condition(s) group, we can speculate that the post COVID-19 condition group had worse HRQOL and mental well-being at T2 and a greater deterioration in HRQOL from T1 to T2 due to acquiring post COVID-19 condition and not due to their co-morbidities. This is because the chronic condition(s) group had overall better HRQOL and mental well-being at T2 and a smaller deterioration in HRQOL over time. However, we are very cautious with this interpretation because we did not test for differences between the two groups in the number and types of chronic conditions, as well as other indicators that could influence the outcomes. In addition, it is important to bear in mind that chronic conditions were self-reported and an option for “other” chronic conditions was available; therefore, conditions were not necessarily verified by health practitioners and were highly diverse and subjective. In all, this challenges the generalisability to the post COVID-19 condition population. Despite this limitation, contrarily to other studies where a convenience sample or a specific post COVID-19 condition population were obtained, e.g., that were hospitalised, we used a general population sample. Furthermore, respondents who did not complete the questionnaire at T2 were significantly younger and more often reported having chronic conditions, though this may have been largely mitigated given the large sample size. Taking into account the higher risk of developing post COVID-19 condition among those with chronic conditions, this may have led to a higher attrition of those with post COVID-19 condition at T2.

Moreover, the non-response analysis could not be applied to the disease status categorisation due to the T1 COVID-19 questions not matching the improved version at T2, given our lack of knowledge of post COVID-19 condition at the time of the production of the questionnaire, as well as the limited COVID-19 testing capacities. This has made the comparison between disease status classification less accurate and made loss to follow up difficult to detect between the disease status groups. On the other hand, the timing of the first wave data collection was close to the start of the pandemic, making it very unlikely to capture many people with post COVID-19 condition at T1.

Some recommendations include the concerted use of the WHO definition of post COVID-19 condition, to ease comparability between epidemiological research, as well as the use of control groups including healthy and with chronic condition(s), as this may allow for the identification of commonalities, a clearer condition definition, and help identify treatment options.

### Conclusions

We conclude that participants with post-COVID condition had the worst HRQOL and mental well-being compared to the other three groups. In terms of change since the start of the COVID-19 pandemic, HRQOL and mental well-being deterioration was highest among the participants with an acute COVID-19 infection and had a lower impact among participants with post-COVID condition, most likely due to pre-existing chronic disease.

## Acknowledgments

We thank Periklis Charalampous, Vanessa Gorasso, Che Henry and Ava Unger for their contributions in checking the translations of the questionnaire.

## Funding Statement

This study was funded by the EuroQol Research Foundation (grant number 460-RA). Views expressed by the authors in the publication do not necessarily reflect those of the EuroQol Group.

## Data availability statement

The original contributions presented in the study are included in the article/<a href="#s10" data-ref-type="sec"><strong>Supplementary Materials</strong></a>, further inquiries can be directed to the corresponding author/s.

## Ethics statement

The studies involving human participants were reviewed and approved by the Erasmus MC ethics review board (approval MEC-2020-0266). The patients/participants provided their written informed consent to participate in this study.

## Author contributions

All authors contributed to the conception and design of the study. JAH, GJB, and MFJ designed the questionnaire, collected the data and developed the analytical design. Material preparation, analysis, and interpretation of data were performed by ESS and JAH. ESS wrote the first draft of the manuscript. All authors reviewed and critically revised the manuscript. All authors contributed to the article and approved the submitted version.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: <https://www.frontiersin.org/articles/10.3389/fepid.2023.1144162/full#supplementary-material>.

## References

## References

1. World Health Organization. Post COVID-19 condition (Long COVID). World Health Organization Regional Office for Europe (2022). Available at: https://www.who.int/europe/news-room/fact-sheets/item/post-covid-19-condition (Accessed December 12, 2022).

2. Aiyegbusi OL, Hughes SE, Turner G, Rivera SC, McMullan C, Chandan JS, et al. Symptoms, complications and management of long COVID: a review. J R Soc Med. (2021) 114:428–42. 10.1177/01410768211032850

3. Amdal CD, Pe M, Falk RS, Piccinin C, Bottomley A, Arraras JI, et al. Health-related quality of life issues, including symptoms, in patients with active COVID-19 or post COVID-19; a systematic literature review. Qual Life Res. (2021) 30:3367–81. 10.1007/s11136-021-02908-z

4. World Health Organization. A clinical case definition of post COVID-19 condition by a delphi consensus, 6 October 2021. Geneva: World Health Organization; (2021) Available at: https://apps.who.int/iris/handle/10665/345824 (Accessed December 12, 2022).

5. Badenoch JB, Rengasamy ER, Watson C, Jansen K, Chakraborty S, Sundaram RD, et al. Persistent neuropsychiatric symptoms after COVID-19: a systematic review and meta-analysis. Brain Commun. (2022) 4:fcab297. 10.1093/braincomms/fcab297

6. Malik P, Patel K, Pinto C, Jaiswal R, Tirupathi R, Pillai S, et al. Post-acute COVID-19 syndrome (PCS) and health-related quality of life (HRQoL)-A systematic review and meta-analysis. J Med Virol. (2022) 94:253–62. 10.1002/jmv.27309

7. Poudel AN, Zhu S, Cooper N, Roderick P, Alwan N, Tarrant C, et al. Impact of COVID-19 on health-related quality of life of patients: a structured review. PLoS One. (2021) 16:e0259164. 10.1371/journal.pone.0259164

8. Hastie CE, Lowe DJ, Mcauley A, Winter AJ, Mills NL, Black C, et al. Outcomes among confirmed cases and a matched comparison group in the long-COVID in Scotland study. Nat Commun. (2022) 13:5663. 10.1038/s41467-022-33415-5

9. Schou TM, Joca S, Wegener G, Bay-Richter C. Psychiatric and neuropsychiatric sequelae of COVID-19—a systematic review. Brain Behav Immun. (2021) 97:328–48. 10.1016/j.bbi.2021.07.018

10. Seeßle J, Waterboer T, Hippchen T, Simon J, Kirchner M, Lim A, et al. Persistent symptoms in adult patients 1 year after coronavirus disease 2019 (COVID-19): a prospective cohort study. Clin Infect Dis. (2022) 74:1191–8. 10.1093/cid/ciab611

11. Spronk I, Geraerds A, Bonsel GJ, De Jongh MAC, Polinder S, Haagsma JA. Correspondence of directly reported and recalled health-related quality of life in a large heterogeneous sample of trauma patients. Qual Life Res. (2019) 28:3005–13. 10.1007/s11136-019-02256-z

12. Long D, Haagsma JA, Janssen MF, Yfantopoulos JN, Lubetkin EI, Bonsel GJ. Health-related quality of life and mental well-being of healthy and diseased persons in 8 countries: does stringency of government response against early COVID-19 matter? SSM Popul Health. (2021) 15:100913. 10.1016/j.ssmph.2021.100913

13. Brooks R. Euroqol: the current state of play. Health Policy. (1996) 37:53–72. 10.1016/0168-8510(96)00822-6

14. Pickard AS, Law EH, Jiang R, Pullenayegum E, Shaw JW, Xie F, et al. United States Valuation of EQ-5D-5L health states using an international protocol. Value Health. (2019) 22:931–41. 10.1016/j.jval.2019.02.009

15. Topp CW, Østergaard SD, Søndergaard S, Bech P. The WHO-5 well-being Index: a systematic review of the literature. Psychother Psychosom. (2015) 84:167–76. 10.1159/000376585

16. Kroenke K, Spitzer RL, Williams JB. The PHQ-9: validity of a brief depression severity measure. J Gen Intern Med. (2001) 16:606–13. 10.1046/j.1525-1497.2001.016009606.x

17. Levis B, Benedetti A, Thombs BD. Accuracy of patient health questionnaire-9 (PHQ-9) for screening to detect major depression: individual participant data meta-analysis. Br Med J. (2019) 365:l1476. 10.1136/bmj.l1476

18. Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing generalized anxiety disorder: the GAD-7. Arch Intern Med. (2006) 166:1092–7. 10.1001/archinte.166.10.1092

19. Johnson SU, Ulvenes PG, Øktedalen T, Hoffart A. Psychometric properties of the general anxiety disorder 7-item (GAD-7) scale in a heterogeneous psychiatric sample. Front Psychol. (2019) 10: Article 1713. 10.3389/fpsyg.2019.01713

20. Kroenke K, Spitzer RL, Williams JB, Monahan PO, Löwe B. Anxiety disorders in primary care: prevalence, impairment, comorbidity, and detection. Ann Intern Med. (2007) 146:317–25. 10.7326/0003-4819-146-5-200703060-00004

21. Larsson J. eulerr: Area-Proportional Euler and Venn Diagrams with Ellipses. R package version 7.0.0 (2022). Available at: https://CRAN.R-project.org/package=eulerr

22. Förster C, Colombo MG, Wetzel AJ, Martus P, Joos S. Persisting symptoms after COVID-19. Dtsch Arztebl Int. (2022) 119:167–74. 10.3238/arztebl.m2022.0147

23. Líška D, Liptaková E, Babičová A, Batalik L, Baňárová PS, Dobrodenková S. What is the quality of life in patients with long COVID compared to a healthy control group? Front Public Health. (2022) 10:975992. 10.3389/fpubh.2022.975992

24. Moens M, Duarte RV, De Smedt A, Putman K, Callens J, Billot M, et al. Health-related quality of life in persons post-COVID-19 infection in comparison to normative controls and chronic pain patients. Front Public Health. (2022) 10: Article 991572. 10.3389/fpubh.2022.991572

25. Roessler M, Tesch F, Batram M, Jacob J, Loser F, Weidinger O, et al. Post-COVID-19-associated morbidity in children, adolescents, and adults: a matched cohort study including more than 157,000 individuals with COVID-19 in Germany. PLoS Med. (2022) 19:e1004122. 10.1371/journal.pmed.1004122

26. Taquet M, Luciano S, Geddes JR, Harrison PJ. Bidirectional associations between COVID-19 and psychiatric disorder: retrospective cohort studies of 62 354 COVID-19 cases in the USA. Lancet Psychiatry. (2021) 8:130–40. 10.1016/S2215-0366(20)30462-4

27. Thompson EJ, Williams DM, Walker AJ, Mitchell RE, Niedzwiedz CL, Yang TC, et al. Long COVID burden and risk factors in 10 UK longitudinal studies and electronic health records. Nat Commun. (2022) 13:3528. 10.1038/s41467-022-30836-0

28. National Center for Health Statistics. Anxiety and Depression—Household Pulse Survey. Centers for Disease Control and Prevention (2023). Available: https://www.cdc.gov/nchs/covid19/pulse/mental-health.htm (Accessed January 11, 2023).

## Associated Data

### Supplementary Materials

### Data Availability Statement

The original contributions presented in the study are included in the article/<a href="#s10" data-ref-type="sec"><strong>Supplementary Materials</strong></a>, further inquiries can be directed to the corresponding author/s.

---
project_id: "464-RA"
work_id: "doi:10.1007/s11136-025-04053-3"
doi: "10.1007/s11136-025-04053-3"
pmid: "40911276"
pmcid: "PMC12689771"
title: "The psychometric performance of the EQ-5D-5L composite and component items in the U.S. General population and by age group"
journal: "Quality of Life Research"
publication_date: "2025-09-05"
volume: "34"
issue: "12"
authors:
  - name: "Minh Pham"
    affiliation_ids:
      - "Aff1"
  - name: "Benjamin M Craig"
    affiliation_ids:
      - "Aff1"
  - name: "Fanni Rencz"
    affiliation_ids:
      - "Aff2"
      - "Aff3"
affiliations:
  - id: "Aff1"
    name: "Department of Economics, College of Arts and Sciences, University of South Florida, 4202 E Fowler Ave, Tampa, FL 33620 USA"
  - id: "Aff2"
    name: "Department of Health Policy, Corvinus University of Budapest, Budapest, Hungary"
  - id: "Aff3"
    name: "EuroQol Research Foundation, Rotterdam, The Netherlands"
licence: "cc-by-nc-nd"
source_file: "input/projects/464-RA/papers/doi_10.1007_s11136-025-04053-3.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12689771/fullTextXML"
source_method: "epmc_xml"
source_sha256: "1d4a77b5283acfcee9227b25f9250598e627b757d83371fa3621ed7dafc8f99e"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The psychometric performance of the EQ-5D-5L composite and component items in the U.S. General population and by age group

## Abstract

### Objectives

EQ-5D-5L items, self-care (SC), pain/discomfort (PD), and anxiety/depression (AD), are composites of two components. While PD (comprised of pain \[PN\] and discomfort \[DI\]) and AD (comprised of anxiety \[AN\] and depression \[DE\]) have been extensively studied, SC (comprised of washing self \[WA\] and dressing self \[DR\]) remains underexplored. Additionally, to our knowledge, the psychometric performance of composites versus components has never been investigated across age groups. This study examines the three composites and six components overall and by age group.

### Methods

In 2024, a representative sample of 6,018 US adults participated in an online survey that included the EQ-5D-5L and its six components in fixed order. In the overall sample and separately across age groups (18–29, 30–39, 40–49, 50–59, 60–69, 70+), we evaluated underreporting, ceilings and floors, agreement (weighted Kappa), convergent validity, informativity, explanatory power for EQ VAS (R²), and structural validity (exploratory factor analysis \[EFA\]).

### Results

The ceiling was lower across all three composites compared to their component items. Strong agreement was found between composites and their corresponding component items (SC: 0.78, PD: 0.91, AD: 0.92). Using component items instead of composites increased the informativity and adjusted R² values. The first-listed components showed stronger convergent validity with their composites.EFA identified three factors: physical functioning (including MO, UA, SC), PD, and AD. Splitting the AD for younger and PD for older populations showed the greatest added value while there were minimal differences between SC and the module of washing and dressing self.

### Conclusions

The EQ-5D-5L composites effectively captured the information provided by their individual components, but replacing PD and AD with their components may improve instrument performance and its adaptability across health concerns relevant to different age groups.

**Keywords:** EQ-5D, Composites, Population health, Psychometrics, Health-related quality of life

Received 2025 Jun 22; Accepted 2025 Aug 12; Issue date 2025.

## Background

The EQ-5D-5L is a widely adopted preference-weighted instrument for assessing health-related quality of life (HRQoL) in both clinical research and general population studies \[1\]. Initially developed to capture and value health outcomes across diverse conditions, the EQ-5D-5L has become a standard instrument for economic evaluations and is now recommended by health technology assessment (HTA) agencies in multiple countries \[1–4\]. The instrument includes a descriptive system with five dimensions—mobility (MO), self-care (washing self/dressing self \[SC\]), usual activities (UA), pain/discomfort (PD), and anxiety/depression (AD)—each rated on a single item across five severity levels, and the EQ visual analogue scale (EQ VAS), which rates health status from 0 (worst health you can imagine) to 100 (best health you can imagine) \[2, 3, 5, 6\]. Despite its widespread adoption, the instrument has been the subject of ongoing scrutiny, particularly regarding how well its five items capture the complexity of patient experiences \[7–10\]. Central to this discussion is the assumption that respondents interpret and report on each of its five items in a consistent and reliable way \[11\]. However, this assumption becomes particularly challenged when dimension conflate two aspects, as is the case with the three dimensions: SC, PD, and AD. In this study, we referred these three dimensions as “composites” (i.e. broader constructs that encompass multiple underlying subitems) and the subitems that comprised them as “components” (i.e. individual items targeting specific aspects within each composite). It is important to note that while the UA item includes multiple examples in its question (“e.g., work, study, housework, family, or leisure activities”), we did not treat these as distinct components. Rather, they serve as illustrative examples to help guide respondents’ interpretation of the question, not as separate constructs to be measured individually.

By construction, composite labels introduce interpretive uncertainty (e.g., severely anxious or depressed): the adjectival statement does not specify whether respondents should report based on one symptom, both, or the more salient of the two, nor does it clarify how researchers or clinicians should interpret responses described by these terms, which may have vastly different actionable implications \[12–14\]. This ambiguity complicates both self-report and routine use, highlighting potential considerations about measurement validity and interpretive consistency. As such, there has been increasing interest in examining their underlying components to better understand response patterns and psychometric properties. Notably, the PD and AD have received extensive attention, with researchers using data from various countries and populations exploring their composite structure and potential for greater granularity.

McDonald et al. (UK English, *n* = 1007 and *n* = 1415) found that ceiling percentages were higher for composites than for their disaggregated components in both current health and worst recalled health assessments \[11\]. This suggested that respondents did not interpret composites as direct reflections of either individual component. Similarly, Tsuchiya et al. (UK English, *n* = 2494) reported that respondents were more likely to select “no problems” on the composites than on both corresponding components when presented separately, with the difference more pronounced for AD than for PD, indicating that PD may be interpreted more consistently with its components \[15\]. In a Hungarian online survey (*n* = 1700), while the differences were smaller between the ceiling percentages of the composites and components compared to other studies, Rencz and Janssen also observed underreporting on composites compared to components and identified systematic ordering effects, where respondents were more likely to respond based on the first-listed component (e.g., pain over discomfort) \[16\]. In a clinical interview study conducted in Amharic (*n* = 462), Belay et al. found that 30.5% of respondents reported no problems on AD, whereas only 13.2% reported no problems on both anxiety and depression, suggesting that those with moderate symptoms in just one domain may underreport problems on the composite \[17\]. Overall, despite variation in the number of respondents reporting “no problems” on the composites versus the components, all studies pointed to potential underreporting driven by ambiguity in the composite framing and highlighted the influence of the first-listed components.

Among the four studies, both McDonald et al. and Tsuchiya et al. randomized respondents to different survey versions, including the standard EQ-5D-5L and modified EQ-6D-5 L (i.e. composite was split and replaced with its two components) \[11, 15\]. Additionally, McDonald et al. also included EQ-4D-5 L + components versions (i.e. composite was split but only one component was retained) \[11\]. In contrast, Belay et al. and Rencz and Janssen administered both the composites and their corresponding components together in a single survey \[16, 17\].

Despite these advancements in PD and AD, SC has not been explored with equivalent depth. This composite captures activities such as washing self and dressing self, and consistently shows worse psychometric performance compared to the other EQ-5D-5L items in many populations \[18–22\]. The evidence on AD and PD leaves open the possibility that separating SC into distinct components, such as “washing self” and “dressing self”, could similarly improve the precision and relevance of the EQ-5D for capturing HRQoL in specific populations. Moreover, despite potential differences in interpretation and reporting, the performance of EQ-5D-5L composites and their components have never been systematically investigated across age groups.

The objective of this study is to describe the psychometric performance of the EQ-5D-5L composites and their components in a U.S. general population sample and by age subgroups: SC, PD, AD, washing self (WA), dressing self (DR), pain (PN), discomfort (DI), anxiety (AN), and depression (DE).

## Methods

### Data

After independent review board (IRB) at Advarra determined that this research project (Pro00080475; 11 July 2024) was exempt from IRB oversight based on the Department of Health and Human Services regulations found at 45 CFR 46.104(d)(2), we conducted an online cross-sectional study between August 27 and September 15, 2024 through an online marketing panel (Dynata). To align with the 2020 U.S. Census demographics, the recruitment strategy employed 18 quotas stratified by gender (female, male and other), age (18–34, 35–54, 55+), and race/ethnicity (Hispanic, non-Hispanic Black, non-Hispanic other).

Among the 16,953 unique respondent identifiers representative of U.S. adults, 12,078 completed the screener, 8395 met the inclusion criteria (i.e., residing in one of the 50 U.S. states or Washington, D.C., and meeting the state-specific age of adulthood: ≥18 in most states, ≥ 19 in Nebraska and Alabama, and ≥ 20 in Mississippi), and 6467 completed the survey fully. Among those who completed the survey, 449 respondents were excluded because they completed it in less than 13 min to prevent low-effort responses, producing an analytical sample of 6,018 respondents. The survey instrument included the U.S. version of the EQ-5D-5L and the six components in fixed order \[6\]. Further details are available in the study protocol, including its survey instrument \[23\].

### Statistical analyses

Building on recent studies by McDonald et at., Belay et al., and Rencz and Janssen that have examined the psychometric properties of EQ-5D-5L composites by comparing them to their components, we conducted a series of psychometric, exploratory factor, and regression analyses at the level of component, composite and module formed from the two components \[11, 16, 17\]. To examine age-related differences in performance, all analyses were repeated within each of six age-stratified subgroups: 18–29, 30–39, 40–49, 50–59, 60–69, and 70 years or older. Our null hypothesis is no difference in psychometric properties by age groups. All statistical analyses were conducted on R version 4.4.2 with packages dplyr version 1.1.4, vegan version 2.6-8, EFA.dimensions version 0.1.8.4, psych version 2.4.6.26 and ggplot2 version 3.3.0 \[24–29\].

### Ceiling and floor

To provide an overview of the dataset and assess the range and potential clustering of responses, we summarized the response frequencies to assess potential underreporting, i.e., respondents reported fewer problems in composites than components. McNemar’s test was then used to determine whether the discrepancies between composites and components were statistically significant. We then calculated the percentage of respondents selecting the best (ceiling) and worst (floor) response option for each composite and its components. These analyses were conducted at the individual level for both composites and components, and additionally at the instrument level by comparing the standard EQ-5D-5L profile to module variants: EQ-4D + components (i.e. replacing each composite by one of its components), EQ-4D + module (i.e. replacing each composite by both components). Based on previous studies, we hypothesized that composites would exhibit underreporting and thus resulting in higher ceiling percentages and lower floor percentages compared to their components \[16, 17, 30\]. By construction, EQ-4D + module instruments capture more problems than EQ-4D + components.

### Response agreement

To assess the level of agreement between each composite and the worst response of its two associated components, we conducted cross-tabulation between the components and their corresponding composites and calculated percent agreement and Cohen’s weighted kappa (i.e. the composite score was compared to the maximum score obtained from their components) \[31\]. Kappa values were interpreted as follows: ≤ 0 (poor), 0.01–0.20 (slight), 0.21–0.40 (fair), 0.41–0.60 (moderate), 0.61–0.80 (substantial), and 0.81–1.00 (almost perfect) \[32\]. For the cross-tabulation analysis, we hypothesized that the proportion of respondents reporting some problems on the composite would be lower than on the components, and that response agreement would be moderate across the three dimensions, with higher agreement expected for the first-listed components (i.e., washing self, pain, and anxiety) \[11, 17\].

### Informativity

To assess the degree of uniform distribution of responses across each item and how evenly the responses are distributed, we employed the Shannon Index (H′) and the Shannon Evenness Index (J′) for the composites, components, and modules. Originally proposed by Claude Shannon in 1948, the Shannon Index has been widely used in the study of the psychometric properties of the EQ-5D-5L \[33, 34\]. Similar to ceiling and floor, the indices were calculated at the individual level and at the instrument level. We hypothesized that H′ and J′ of the components would be higher than their composites with first-listed components being the highest \[17\]. At the instrument level, we hypothesized that EQ-4D-5 L + module instruments would have higher H′ and J′ compared to the original EQ-5D-5L and EQ-4D-5 L + components. The formulas used for calculating these indices are shown below, where *L* represents the number of response options for an item, and *p*<sub>*i*</sub> is the proportion of respondents selecting the *i*th response option:

<div id="Equa" class="disp-formula">

<img src="d33e392.gif" id="d33e392" />

</div>

<div id="Equb" class="disp-formula">

<img src="d33e396.gif" id="d33e396" />

</div>

### Convergent validity

To evaluate the relationship between composites, components, and EQ VAS, we estimated the Spearman’s correlation coefficients. Following the guidelines provided by Cohen, correlations (\|r<sub>s</sub>\|) between 0.1 and 0.29 were considered weak, those between 0.3 and 0.49 were considered moderate, and correlations of 0.5 or higher were regarded as strong \[35\]. Based on previous research, we hypothesized strong correlations between composites and their components, with the first-listed components expected to correlate more strongly, as well as strong associations between these items and EQ VAS \[16, 30\].

### Structural validity

To determine if the composites and components effectively represent the same dimension or if the components provide additional, distinct information, we conducted an exploratory factor analysis (EFA). Factor loadings and eigenvalues were examined to identify underlying structures, with decisions on the number of factors guided by a combination of visual inspection of the scree plot and the Kaiser’s criterion of retaining factors with eigenvalues greater than 1 \[36, 37\]. Rotation (e.g., varimax) was also applied to improve interpretability \[38\]. Factor loadings closer to − 1 or + 1 were interpreted as indicating strong associations between a composite/component and the underlying latent factor, while values near 0 suggested weak or no association. We hypothesized that composites and their components would load onto the same underlying factor.

### Explanatory power

To investigate how components and modules contribute to explaining variation in EQ VAS and EQ-5D-5L health profile level-sum scores, we conducted bivariate and multivariate linear regression analyses \[39\]. These analyses examined the relationships between components (i.e., without interactions between components) and modules (i.e., interactions between components) and EQ VAS without the composites (SC, PD, and AD). Additionally, the effects of splitting the composites into components were also examined at the instrument level (i.e. EQ-4D-5 L + components and EQ-4D-5 L + modules). We hypothesized that including modules in the regression models would increase the explained variance (R²) of EQ VAS beyond what is explained by the composites alone \[40–44\].

## Results

### Characteristics of the study population

Overall, the analytical sample of 6,018 participants was nationally representative and reflected the demographic and regional composition of the U.S. adult population. The analytical sample comprised 866 respondents (14.4%) aged 18–29, 1268 respondents (21%) aged 30–39, 1161 respondents (19.3%) aged 40–49, 997 respondents (16.6%) aged 50–59, 910 respondents (15.1%) aged 60–69, and 802 respondents (13.3%) aged 70 or older (Appendix <a href="#Sec21" data-ref-type="sec">1</a>).

### Distributional characteristics

The response distribution of the overall sample on the individual level is presented in Fig. <a href="#Fig1" data-ref-type="fig">1</a>. For SC, 90.4% respondents reported Level 1, while its components, WA and DR, showed slightly higher ceiling percentages at 91.4% and 90.9%, respectively. Additionally, respondents reported extreme problems in SC more than in its components, with a higher percentage at Level 5 (0.3% versus 0.2% for both components). Our hypothesis of underreporting in composites was not supported, as no evidence of underreporting was found in PD and AD composites either. Their four components all showed higher percentages at Level 1 and lower percentages from Level 3 to Level 5. Similar patterns were observed in the analysis by age groups (Appendix <a href="#Sec22" data-ref-type="sec">2</a>).

<figure id="Fig1">
<p><img src="11136_2025_4053_Fig1_HTML.jpg" id="d33e468" /></p>
<p><img src="11136_2025_4053_Fig1_HTML.gif" /></p>
<figcaption>EQ-5D-5L composites and components response distribution and ceiling and floor percentages by age group, on individual level, %</figcaption>
</figure>

Ceiling percentages were observed to be lower in composites compared to their corresponding components, which further rejected our hypothesis regarding underreporting in composites (Table <a href="#Tab1" data-ref-type="table">1</a>). All increases in ceiling percentages from composites to components were statistically significant (*p* \< 0.001), except for DR (*p* = 0.08) and PN (*p* = 0.63).

<div id="Tab1" class="table-wrap">

<div class="caption">

Results of EQ-5D-5L ceiling and floor percentages at the individual level and instrument level in overall sample, % (n)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">EQ-5D-5L</th>
<th style="text-align: left;">Ceiling</th>
<th style="text-align: left;">Floor</th>
<th style="text-align: left;">Components</th>
<th style="text-align: left;">Ceiling</th>
<th style="text-align: left;">Floor</th>
<th style="text-align: left;"><em>p</em>-value<sup>†</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="8" style="text-align: left;">Individual level</td>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">74.4 (4475)</td>
<td style="text-align: center;">0.5 (33)</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">SC</td>
<td rowspan="2" style="text-align: center;">90.4 (5439)</td>
<td rowspan="2" style="text-align: center;">0.3 (16)</td>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">91.4 (5499)</td>
<td style="text-align: center;">0.2 (10)</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">90.9 (5468)</td>
<td style="text-align: center;">0.2 (11)</td>
<td style="text-align: center;">0.08</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">74.2 (4466)</td>
<td style="text-align: center;">0.5 (29)</td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">PD</td>
<td rowspan="2" style="text-align: center;">38.7 (2327)</td>
<td rowspan="2" style="text-align: center;">1.5 (89)</td>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">38.8 (2337)</td>
<td style="text-align: center;">1.5 (92)</td>
<td style="text-align: center;">0.63</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">43.3 (2603)</td>
<td style="text-align: center;">1.3 (81)</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">AD</td>
<td rowspan="2" style="text-align: center;">48 (2887)</td>
<td rowspan="2" style="text-align: center;">4.1 (247)</td>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">50.9 (3061)</td>
<td style="text-align: center;">3.7 (222)</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">58.2 (3501)</td>
<td style="text-align: center;">3.0 (179)</td>
<td style="text-align: center;"> &lt; 0.001</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Original instrument</th>
<th style="text-align: left;">Ceiling</th>
<th style="text-align: left;">Floor</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Ceiling</th>
<th style="text-align: left;">Floor</th>
<th style="text-align: left;"><em>p</em>-value<sup>‡</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="11" style="text-align: left;">Instrument level</td>
<td rowspan="11" style="text-align: left;">EQ-5D-5L</td>
<td rowspan="11" style="text-align: center;">25.3 (1523)</td>
<td rowspan="11" style="text-align: center;">0.0 (2)</td>
<td style="text-align: left;">EQ-4D-5L + components</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA</td>
<td style="text-align: center;">25.3 (1522)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DR</td>
<td style="text-align: center;">25.3 (1524)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN</td>
<td style="text-align: center;">25.0 (1506)</td>
<td style="text-align: center;">0 (2)</td>
<td style="text-align: left;">0.17</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DI</td>
<td style="text-align: center;">27.7 (1667)</td>
<td style="text-align: center;">0 (2)</td>
<td style="text-align: left;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN</td>
<td style="text-align: center;">25.8 (1553)</td>
<td style="text-align: center;">0 (2)</td>
<td style="text-align: left;">0.03</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DE</td>
<td style="text-align: center;">27.9 (1676)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + Modules</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA + DR</td>
<td style="text-align: center;">25.2 (1519)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;">0.39</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN + DI</td>
<td style="text-align: center;">24.1 (1452)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;"> &lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN + DE</td>
<td style="text-align: center;">24.6 (1478)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;"> &lt; 0.001</td>
</tr>
</tbody>
</table>

†: p values from McNemar’s test for differences between components and composites

‡: p values from McNemar’s test for differences between original instrument and EQ-4D-5L + components, EQ-4D-5L + modules

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

Figure <a href="#Fig1" data-ref-type="fig">1</a> also illustrates the ceiling and floor percentages of the composites and their corresponding components on individual level by age groups. The ceiling percentages for PN and DI decreased from 53 to 31% and from 54 to 39%, respectively, with increasing age. In contrast, the ceiling percentages for AN and DE increased from 34 to 76% and from 46 to 83%, respectively. The ceiling percentages for WA and DR remained relatively stable.

At the instrument level, there were no statistically significant differences in ceiling percentages between the EQ-5D-5L (25.3%) and either EQ-4D-5 L + WA (25.3%) or EQ-4D-5 L + DR (25.3%) (*p* = 1 for both; Table <a href="#Tab1" data-ref-type="table">1</a>). This remained the case when both WA and DR were used (EQ-4D-5 L + WA + DR: 25.2%). In contrast, ceiling percentages increased significantly with the addition of DI and DE (EQ-4D-5 L + DI: 27.7%, EQ-4D-5 L + DE: 27.9%), while significant decreases were observed for EQ-4D-5 L + PN + DI (24.1%) and EQ-4D-5 L + AN + DE (24.6%). In the age group analysis, ceiling percentages for EQ-4D-5 L + DI increased steadily with age, while EQ-4D-5 L + DE showed a decline beginning in the 30–39 age group, followed by a modest increase starting from the 50–59 age group (Fig. <a href="#Fig2" data-ref-type="fig">2</a>).

<figure id="Fig2">
<p><img src="11136_2025_4053_Fig2_HTML.jpg" id="d33e778" /></p>
<p><img src="11136_2025_4053_Fig2_HTML.gif" /></p>
<figcaption>EQ-5D-5L ceiling percentages by age group, on instrument level, %</figcaption>
</figure>

### Response agreement

Table <a href="#Tab2" data-ref-type="table">2</a> presents the cross-tabulations, response agreement, and Cohen’s weighted kappa between composites and their components. Moderate to strong concordance was observed, with high diagonal proportions across Levels 1 to 5, except for Level 4 between washing self and self-care (26.9%), likely due to the small sample size (*n* = 19). However, the hypothesis that fewer respondents would report problems on composites than on components was not supported. For example, 9.6% reported problems on SC, compared to 8.6% for WA and 9.1% for DR; similarly, PD was 61.3% vs. 61.2% (PN) and 56.8% (DI), and AD was 52.0% vs. 49.1% (AN) and 41.8% (DE). However, although composites had fewer “no problems” responses than their components overall, a small number of respondents who reported “no problems” on the composites subsequently reported problems on the components (WA: 1.6%, DR: 2.1%, PN: 7.2%, DI: 8.0%, AN: 5.3%, DE: 2.4%), suggesting little to no underreporting. Our hypothesis regarding moderate agreement with higher concordance for first-listed components was supported. Response agreement ranged from 75.7 to 94.5%, with higher values for WA (94.5%), PN (88.8%), and AN (81.6%) than their counterparts (DR: 94.3%, DI: 77.9%, DE: 75.7%). Weighted kappa values further confirmed this with substantial to almost perfect agreement: 0.78 (SC), 0.91 (PD), and 0.92 (AD).

<div id="Tab2" class="table-wrap">

<div class="caption">

Results of distribution of responses of components by EQ-5D-5L composites, % (n)

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Components</th>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">Composites</th>
<th style="text-align: left;">Problem reporting rate, %</th>
<th style="text-align: left;">Response agreement, %</th>
<th style="text-align: left;">Cohen’s Kappa</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">SC</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 4</th>
<th style="text-align: left;">Level 5</th>
<th style="text-align: left;">SC = 9.60</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;">WA</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">97.3 (5351)</td>
<td style="text-align: left;">2.3 (125)</td>
<td style="text-align: left;">0.3 (19)</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.1 (4)</td>
<td rowspan="5" style="text-align: center;">8.62</td>
<td rowspan="5" style="text-align: center;">94.5</td>
<td rowspan="10" style="text-align: center;">0.78</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">18.6 (69)</td>
<td style="text-align: left;">70.5 (261)</td>
<td style="text-align: left;">9.5 (35)</td>
<td style="text-align: left;">0.8 (3)</td>
<td style="text-align: left;">0.5 (2)</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">15 (17)</td>
<td style="text-align: left;">25.7 (29)</td>
<td style="text-align: left;">54.9 (62)</td>
<td style="text-align: left;">4.4 (5)</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">7.7 (2)</td>
<td style="text-align: left;">19.2 (5)</td>
<td style="text-align: left;">30.8 (8)</td>
<td style="text-align: left;">26.9 (7)</td>
<td style="text-align: left;">15.4 (4)</td>
</tr>
<tr>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">40 (4)</td>
<td style="text-align: left;">60 (6)</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">DR</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">97.4 (5326)</td>
<td style="text-align: left;">2.2 (120)</td>
<td style="text-align: left;">0.3 (18)</td>
<td style="text-align: left;">0 (1)</td>
<td style="text-align: left;">0.1 (3)</td>
<td rowspan="5" style="text-align: center;">9.13</td>
<td rowspan="5" style="text-align: center;">94.3</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">23.1 (95)</td>
<td style="text-align: left;">65.5 (270)</td>
<td style="text-align: left;">10.4 (43)</td>
<td style="text-align: left;">1 (4)</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">14.2 (15)</td>
<td style="text-align: left;">24.5 (26)</td>
<td style="text-align: left;">56.5 (60)</td>
<td style="text-align: left;">2.8 (3)</td>
<td style="text-align: left;">1.9 (2)</td>
</tr>
<tr>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">4.8 (1)</td>
<td style="text-align: left;">14.3 (3)</td>
<td style="text-align: left;">14.3 (3)</td>
<td style="text-align: left;">47.6 (10)</td>
<td style="text-align: left;">19 (4)</td>
</tr>
<tr>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">18.2 (2)</td>
<td style="text-align: left;">9.1 (1)</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">9.1 (1)</td>
<td style="text-align: left;">63.3 (7)</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">PD</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 4</th>
<th style="text-align: left;">Level 5</th>
<th style="text-align: left;">PD = 61.33</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;">PN</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">92.4 (2160)</td>
<td style="text-align: left;">6.9 (161)</td>
<td style="text-align: left;">0.6 (14)</td>
<td style="text-align: left;">0.1 (2)</td>
<td style="text-align: left;">0</td>
<td rowspan="5" style="text-align: center;">61.17</td>
<td rowspan="5" style="text-align: center;">88.8</td>
<td rowspan="10" style="text-align: center;">0.91</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">6.5 (138)</td>
<td style="text-align: left;">88.5 (1884)</td>
<td style="text-align: left;">5 (106)</td>
<td style="text-align: left;">0.1 (2)</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">2.1 (23)</td>
<td style="text-align: left;">8.1 (91)</td>
<td style="text-align: left;">85.3 (954)</td>
<td style="text-align: left;">4.4 (49)</td>
<td style="text-align: left;">0.1 (1)</td>
</tr>
<tr>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">1.5 (5)</td>
<td style="text-align: left;">2.1 (7)</td>
<td style="text-align: left;">12.9 (44)</td>
<td style="text-align: left;">79.5 (271)</td>
<td style="text-align: left;">4.1 (14)</td>
</tr>
<tr>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">1.1 (1)</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">3.3 (3)</td>
<td style="text-align: left;">15.2 (14)</td>
<td style="text-align: left;">80.4 (74)</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">DI</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">82.2 (2140)</td>
<td style="text-align: left;">16.2 (422)</td>
<td style="text-align: left;">1.5 (38)</td>
<td style="text-align: left;">0.1 (3)</td>
<td style="text-align: left;">0</td>
<td rowspan="5" style="text-align: center;">56.75</td>
<td rowspan="5" style="text-align: center;">77.9</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">7.6 (167)</td>
<td style="text-align: left;">75 (1644)</td>
<td style="text-align: left;">16.9 (371)</td>
<td style="text-align: left;">0.4 (9)</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">1.5 (13)</td>
<td style="text-align: left;">8 (70)</td>
<td style="text-align: left;">75.8 (667)</td>
<td style="text-align: left;">13.8 (121)</td>
<td style="text-align: left;">1 (9)</td>
</tr>
<tr>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">2.3 (6)</td>
<td style="text-align: left;">1.9 (5)</td>
<td style="text-align: left;">15.6 (41)</td>
<td style="text-align: left;">69.6 (183)</td>
<td style="text-align: left;">10.6 (28)</td>
</tr>
<tr>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">1.2 (1)</td>
<td style="text-align: left;">2.5 (2)</td>
<td style="text-align: left;">4.9 (4)</td>
<td style="text-align: left;">27.2 (22)</td>
<td style="text-align: left;">64.2 (52)</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">AD</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 4</th>
<th style="text-align: left;">Level 5</th>
<th style="text-align: left;">AD = 52.03</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;">AN</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">89.3 (2734)</td>
<td style="text-align: left;">8.2 (252)</td>
<td style="text-align: left;">2 (61)</td>
<td style="text-align: left;">0.3 (9)</td>
<td style="text-align: left;">0.2 (5)</td>
<td rowspan="5" style="text-align: center;">49.14</td>
<td rowspan="5" style="text-align: center;">81.6</td>
<td rowspan="10" style="text-align: center;">0.92</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">8.8 (132)</td>
<td style="text-align: left;">74.9 (1108)</td>
<td style="text-align: left;">15 (225)</td>
<td style="text-align: left;">1.9 (29)</td>
<td style="text-align: left;">0.4 (6)</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">2.1 (18)</td>
<td style="text-align: left;">10.1 (89)</td>
<td style="text-align: left;">73.5 (645)</td>
<td style="text-align: left;">11.5 (101)</td>
<td style="text-align: left;">2.8 (25)</td>
</tr>
<tr>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">0.3 (1)</td>
<td style="text-align: left;">2.2 (8)</td>
<td style="text-align: left;">17.6 (63)</td>
<td style="text-align: left;">69.7 (249)</td>
<td style="text-align: left;">10.1 (36)</td>
</tr>
<tr>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">0.9 (2)</td>
<td style="text-align: left;">0.9 (2)</td>
<td style="text-align: left;">4.5 (10)</td>
<td style="text-align: left;">14.9 (33)</td>
<td style="text-align: left;">78.8 (175)</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">DE</td>
<td style="text-align: left;">Level 1</td>
<td style="text-align: left;">80.5 (2817)</td>
<td style="text-align: left;">15.2 (532)</td>
<td style="text-align: left;">3.4 (119)</td>
<td style="text-align: left;">0.8 (27)</td>
<td style="text-align: left;">0.2 (6)</td>
<td rowspan="5" style="text-align: center;">41.82</td>
<td rowspan="5" style="text-align: center;">75.7</td>
</tr>
<tr>
<td style="text-align: left;">Level 2</td>
<td style="text-align: left;">4.4 (57)</td>
<td style="text-align: left;">66.4 (857)</td>
<td style="text-align: left;">24.7 (319)</td>
<td style="text-align: left;">3.6 (46)</td>
<td style="text-align: left;">0.9 (11)</td>
</tr>
<tr>
<td style="text-align: left;">Level 3</td>
<td style="text-align: left;">1.1 (8)</td>
<td style="text-align: left;">8.1 (61)</td>
<td style="text-align: left;">70.1 (525)</td>
<td style="text-align: left;">17.1 (128)</td>
<td style="text-align: left;">3.6 (27)</td>
</tr>
<tr>
<td style="text-align: left;">Level 4</td>
<td style="text-align: left;">1.7 (5)</td>
<td style="text-align: left;">2.7 (8)</td>
<td style="text-align: left;">13 (39)</td>
<td style="text-align: left;">66.6 (199)</td>
<td style="text-align: left;">16.1 (48)</td>
</tr>
<tr>
<td style="text-align: left;">Level 5</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.6 (1)</td>
<td style="text-align: left;">1.1 (2)</td>
<td style="text-align: left;">11.7 (21)</td>
<td style="text-align: left;">86.6 (155)</td>
</tr>
</tbody>
</table>

Level 1: No, Level 2: Slight, Level 3: Moderate, Level 4: Severe, Level 5: Extreme/Unable to.

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression.

</div>

### Informativity

Absolute informativity (Shannon H′) and relative informativity (Shannon J′) are presented in Table <a href="#Tab3" data-ref-type="table">3</a>. At the individual level, our hypothesis (i.e. components have higher H′ and J′ than their composites) was only supported for PN (H′ = 1.8383, J′ = 0.7917); all other components showed lower informativity than their corresponding composites. While PN and AN (H′ = 1.8182, J′ = 0.7830) demonstrated greater informativity than DI (H′ = 1.7403, J′ = 0.7495) and DE (H′ = 1.6711, J′ = 0.7197), this pattern did not hold for the SC module. At the instrument level, replacing composites with their corresponding modules resulted in higher absolute informativity compared to the original EQ-5D-5L and versions that included only one component. However, this improvement was not consistent in terms of relative informativity; only EQ-4D-5 L + AN + DE demonstrated comparable relative informativity to EQ-5D-5L, while the other two modules showed lower values. Among the versions with only one component, only EQ-4D-5 L + PN yielded higher absolute informativity than EQ-5D-5L. Age-specific analysis revealed that the first-listed components exhibited higher informativity than the second for all age groups and across all three modules, except for WA and DR in respondents aged 40 and above. Among the EQ-4D-5 L + modules versions, only EQ-4D-5 L + WA + DR exhibited lower relative informativity than EQ-5D-5L across age groups (Appendix <a href="#Sec23" data-ref-type="sec">3</a>).

<div id="Tab3" class="table-wrap">

<div class="caption">

Results of Shannon index (H′) and Shannon evenness index (J′) of EQ-5D-5L composites and components

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Possible health profiles</th>
<th style="text-align: left;">Shannon index (H′)</th>
<th style="text-align: left;">Shannon evenness index (J′)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.1597</td>
<td style="text-align: center;">0.4995</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.5643</td>
<td style="text-align: center;">0.2430</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.1625</td>
<td style="text-align: center;">0.5007</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.8354</td>
<td style="text-align: center;">0.7905</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.8925</td>
<td style="text-align: center;">0.8151</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.5232</td>
<td style="text-align: center;">0.2253</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.5382</td>
<td style="text-align: center;">0.2318</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.8383</td>
<td style="text-align: center;">0.7917</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.7403</td>
<td style="text-align: center;">0.7495</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.8182</td>
<td style="text-align: center;">0.7830</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">1.6711</td>
<td style="text-align: center;">0.7197</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.4271</td>
<td style="text-align: center;">0.6393</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>EQ-4D-5L</em> + <em>components</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.4220</td>
<td style="text-align: center;">0.6042</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DR</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.4173</td>
<td style="text-align: center;">0.6066</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.4486</td>
<td style="text-align: center;">0.6052</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DI</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.3287</td>
<td style="text-align: center;">0.5915</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.3677</td>
<td style="text-align: center;">0.5973</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DE</td>
<td style="text-align: left;">3125</td>
<td style="text-align: center;">5.2314</td>
<td style="text-align: center;">0.5816</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>EQ-4D-5L</em> + <em>modules</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA + DR</td>
<td style="text-align: left;">15,625</td>
<td style="text-align: center;">5.5643</td>
<td style="text-align: center;">0.5975</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN + DI</td>
<td style="text-align: left;">15,625</td>
<td style="text-align: center;">6.0431</td>
<td style="text-align: center;">0.6330</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN + DE</td>
<td style="text-align: left;">15,625</td>
<td style="text-align: center;">6.2030</td>
<td style="text-align: center;">0.6393</td>
</tr>
</tbody>
</table>

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

### Convergent validity

Spearman’s correlation coefficients indicated strong correlations between composites and their components, as well as between components within the same modules (Table <a href="#Tab4" data-ref-type="table">4</a>). In all modules, the first-listed components showed stronger correlations with their respective composites than the second-listed components. Among the components, WA and DR demonstrated weak to moderate correlations with the EQ VAS (\|r<sub>s</sub>\| = 0.29 and \|r<sub>s</sub>\| = 0.31, respectively), whereas the remaining components showed moderate to strong correlations. When analyzed by age groups, the correlation between SC and WA/DR showed a marked increase with age (\|r<sub>s</sub>\| = 0.65–0.82 and \|r<sub>s</sub>\| = 0.64–0.81, respectively). In contrast, the correlations between AD and AN/DE, as well as between PD and PN/DI, remained relatively stable across age groups (Appendix <a href="#Sec24" data-ref-type="sec">4</a>).

<div id="Tab4" class="table-wrap">

<div class="caption">

Results of Spearman’s correlation coefficients between EQ-5D-5L, components, and EQ VAS overall

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">EQ-5D-5L</th>
<th colspan="6" style="text-align: left;">Components</th>
<th rowspan="2" style="text-align: left;">EQ VAS</th>
</tr>
<tr>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">SC</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">UA</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">PD</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">AD</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;">Components</td>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">0.42</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.42</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.42</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> − 0.43</td>
<td style="text-align: left;"> − 0.33</td>
<td style="text-align: left;"> − 0.48</td>
<td style="text-align: left;"> − 0.50</td>
<td style="text-align: left;"> − 0.45</td>
<td style="text-align: left;"> − 0.29</td>
<td style="text-align: left;"> − 0.31</td>
<td style="text-align: left;"> − 0.50</td>
<td style="text-align: left;"> − 0.52</td>
<td style="text-align: left;"> − 0.43</td>
<td style="text-align: left;"> − 0.44</td>
<td style="text-align: left;">1</td>
</tr>
</tbody>
</table>

All correlation coefficients are statistically significant (*p* \< 0.01)

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA,washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

### Structural validity

EFA identified three main fac tors with and without the components: physical functioning (including MO, SC, and UA), PD, and AD (Table <a href="#Tab5" data-ref-type="table">5</a>). In the expanded model, all composites loaded onto the same factors as their corresponding components, with first-listed components exhibited higher loadings on the factors, which confirmed our hypothesis. With or without the components, all items had standardized factor loadings above 0.60, indicating a good fit. Additionally, disaggregating composites into components substantially increased the factor loadings of the composites. These patterns remained consistent across age groups.

<div id="Tab5" class="table-wrap">

<div class="caption">

Results of EQ-5D-5L Factor loadings with and without components overall and by age groups

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Whole sample</th>
<th colspan="2" style="text-align: left;">18–29</th>
<th colspan="2" style="text-align: left;">30–39</th>
<th colspan="2" style="text-align: left;">40–49</th>
</tr>
<tr>
<th style="text-align: left;">Factors</th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="9" style="text-align: left;"><em>Physical functioning</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">0.73</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: center;">0.58</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: left;">0.71</td>
<td style="text-align: center;">0.85</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: center;">0.68</td>
<td style="text-align: left;">0.70</td>
<td style="text-align: center;">0.68</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: center;">0.57</td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.83</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.80</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>Pain and discomfort</em></td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: center;">0.86</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.87</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: center;">0.89</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.89</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.78</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.82</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;"><em>Anxiety and depression</em></td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: left;">0.63</td>
<td style="text-align: center;">0.94</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: left;">0.58</td>
<td style="text-align: center;">0.92</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.86</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.84</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.84</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.84</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.85</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">50–59</th>
<th colspan="2" style="text-align: left;">60–69</th>
<th colspan="2" style="text-align: left;">70 + </th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
<th style="text-align: left;">Without</th>
<th style="text-align: left;">With</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7" style="text-align: left;"><em>Physical functioning</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: left;">0.71</td>
<td style="text-align: center;">0.71</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: center;">0.87</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: center;">0.93</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: center;">0.91</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: left;">0.73</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: left;">0.87</td>
<td style="text-align: center;">0.76</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: center;">0.70</td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.87</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.92</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.86</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>Pain and discomfort</em></td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: center;">0.86</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">0.69</td>
<td style="text-align: center;">0.91</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.91</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.80</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.78</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.82</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>Anxiety and depression</em></td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">0.63</td>
<td style="text-align: center;">0.95</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: center;">0.95</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.89</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.91</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.90</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.90</td>
<td style="text-align: left;">–</td>
<td style="text-align: center;">0.88</td>
</tr>
</tbody>
</table>

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

### Explanatory power

At the individual level, the adjusted R² values for each component were modest, but combining the two components within each module led to slight increases (Table <a href="#Tab6" data-ref-type="table">6</a>). At the instrument level, only EQ-4D-5 L + PN, EQ-4D-5 L + DI, and EQ-4D-5 L + DE showed slightly higher adjusted R² values than the original EQ-5D-5L (0.3956). Contrary to part of our hypothesis, adjusted R² values only modestly improved for the PD and AD modules when both components were included additively (i.e., components + components). However, including interaction terms between components (i.e., components × components) resulted in higher adjusted R² values, with EQ-4D-5 L + WA×DR outperforming the standard EQ-5D-5L at both the individual and instrument levels. Compared to the EQ-5D-5L, EQ-4D-5 L + AN×DE exhibited the largest increase in adjusted R² value in the 18–29 age group, while EQ-4D-5 L + PN×DI showed the largest increase in the 60–69 age group.

<div id="Tab6" class="table-wrap">

<div class="caption">

Results of bivariate and multivariate regression analysis between EQ-5D-5L, components, modules and EQ VAS overall and by age groups

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="7" style="text-align: left;">EQ VAS (Adjusted R<sup>2</sup>)</th>
</tr>
<tr>
<th style="text-align: left;">Selection of items</th>
<th style="text-align: left;">Whole sample</th>
<th style="text-align: left;">18–29</th>
<th style="text-align: left;">30–39</th>
<th style="text-align: left;">40–49</th>
<th style="text-align: left;">50–59</th>
<th style="text-align: left;">60–69</th>
<th style="text-align: left;">70 + </th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">0.2063</td>
<td style="text-align: center;">0.1185</td>
<td style="text-align: center;">0.1368</td>
<td style="text-align: center;">0.1991</td>
<td style="text-align: center;">0.3007</td>
<td style="text-align: center;">0.3071</td>
<td style="text-align: center;">0.2750</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">0.1391</td>
<td style="text-align: center;">0.0723</td>
<td style="text-align: center;">0.1124</td>
<td style="text-align: center;">0.1497</td>
<td style="text-align: center;">0.2160</td>
<td style="text-align: center;">0.1729</td>
<td style="text-align: center;">0.1303</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">0.2465</td>
<td style="text-align: center;">0.1547</td>
<td style="text-align: center;">0.2066</td>
<td style="text-align: center;">0.2391</td>
<td style="text-align: center;">0.3252</td>
<td style="text-align: center;">0.2971</td>
<td style="text-align: center;">0.2846</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">0.2723</td>
<td style="text-align: center;">0.2316</td>
<td style="text-align: center;">0.2092</td>
<td style="text-align: center;">0.2930</td>
<td style="text-align: center;">0.3182</td>
<td style="text-align: center;">0.3115</td>
<td style="text-align: center;">0.2933</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">0.2052</td>
<td style="text-align: center;">0.2021</td>
<td style="text-align: center;">0.2235</td>
<td style="text-align: center;">0.2377</td>
<td style="text-align: center;">0.2995</td>
<td style="text-align: center;">0.1587</td>
<td style="text-align: center;">0.1491</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">0.1109</td>
<td style="text-align: center;">0.0745</td>
<td style="text-align: center;">0.0979</td>
<td style="text-align: center;">0.1134</td>
<td style="text-align: center;">0.1642</td>
<td style="text-align: center;">0.1279</td>
<td style="text-align: center;">0.0891</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">0.1228</td>
<td style="text-align: center;">0.5336</td>
<td style="text-align: center;">0.7515</td>
<td style="text-align: center;">0.1305</td>
<td style="text-align: center;">0.1885</td>
<td style="text-align: center;">0.1753</td>
<td style="text-align: center;">0.1216</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">0.2776</td>
<td style="text-align: center;">0.2418</td>
<td style="text-align: center;">0.2043</td>
<td style="text-align: center;">0.2986</td>
<td style="text-align: center;">0.3218</td>
<td style="text-align: center;">0.3222</td>
<td style="text-align: center;">0.2948</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">0.2921</td>
<td style="text-align: center;">0.2445</td>
<td style="text-align: center;">0.2299</td>
<td style="text-align: center;">0.3105</td>
<td style="text-align: center;">0.3322</td>
<td style="text-align: center;">0.3450</td>
<td style="text-align: center;">0.2894</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">0.1856</td>
<td style="text-align: center;">0.1954</td>
<td style="text-align: center;">0.1989</td>
<td style="text-align: center;">0.2162</td>
<td style="text-align: center;">0.2733</td>
<td style="text-align: center;">0.1530</td>
<td style="text-align: center;">0.1318</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">0.2017</td>
<td style="text-align: center;">0.2018</td>
<td style="text-align: center;">0.2105</td>
<td style="text-align: center;">0.2302</td>
<td style="text-align: center;">0.2812</td>
<td style="text-align: center;">0.1717</td>
<td style="text-align: center;">0.1445</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;"><em>Modules</em></td>
</tr>
<tr>
<td style="text-align: left;">WA + DR</td>
<td style="text-align: center;">0.1344</td>
<td style="text-align: center;">0.0814</td>
<td style="text-align: center;">0.1064</td>
<td style="text-align: center;">0.1418</td>
<td style="text-align: center;">0.1939</td>
<td style="text-align: center;">0.1825</td>
<td style="text-align: center;">0.1253</td>
</tr>
<tr>
<td style="text-align: left;">PN + DI</td>
<td style="text-align: center;">0.3047</td>
<td style="text-align: center;">0.2717</td>
<td style="text-align: center;">0.2370</td>
<td style="text-align: center;">0.3235</td>
<td style="text-align: center;">0.3481</td>
<td style="text-align: center;">0.3626</td>
<td style="text-align: center;">0.3194</td>
</tr>
<tr>
<td style="text-align: left;">AN + DE</td>
<td style="text-align: center;">0.2169</td>
<td style="text-align: center;">0.2270</td>
<td style="text-align: center;">0.2405</td>
<td style="text-align: center;">0.2459</td>
<td style="text-align: center;">0.3074</td>
<td style="text-align: center;">0.1852</td>
<td style="text-align: center;">0.1656</td>
</tr>
<tr>
<td style="text-align: left;">WA × DR</td>
<td style="text-align: center;">0.1380</td>
<td style="text-align: center;">0.0896</td>
<td style="text-align: center;">0.1106</td>
<td style="text-align: center;">0.1480</td>
<td style="text-align: center;">0.1951</td>
<td style="text-align: center;">0.1896</td>
<td style="text-align: center;">0.1316</td>
</tr>
<tr>
<td style="text-align: left;">PN × DI</td>
<td style="text-align: center;">0.3060</td>
<td style="text-align: center;">0.2873</td>
<td style="text-align: center;">0.2419</td>
<td style="text-align: center;">0.3375</td>
<td style="text-align: center;">0.3578</td>
<td style="text-align: center;">0.3737</td>
<td style="text-align: center;">0.3313</td>
</tr>
<tr>
<td style="text-align: left;">AN × DE</td>
<td style="text-align: center;">0.2218</td>
<td style="text-align: center;">0.2499</td>
<td style="text-align: center;">0.2549</td>
<td style="text-align: center;">0.2699</td>
<td style="text-align: center;">0.3261</td>
<td style="text-align: center;">0.2021</td>
<td style="text-align: center;">0.1806</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: center;">0.3956</td>
<td style="text-align: center;">0.3251</td>
<td style="text-align: center;">0.3474</td>
<td style="text-align: center;">0.4064</td>
<td style="text-align: center;">0.4909</td>
<td style="text-align: center;">0.4253</td>
<td style="text-align: center;">0.4161</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;"><em>EQ-4D-5L</em> + <em>components</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA</td>
<td style="text-align: center;">0.3934</td>
<td style="text-align: center;">0.3246</td>
<td style="text-align: center;">0.3534</td>
<td style="text-align: center;">0.3977</td>
<td style="text-align: center;">0.4860</td>
<td style="text-align: center;">0.4317</td>
<td style="text-align: center;">0.4158</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DR</td>
<td style="text-align: center;">0.3932</td>
<td style="text-align: center;">0.3260</td>
<td style="text-align: center;">0.3430</td>
<td style="text-align: center;">0.3966</td>
<td style="text-align: center;">0.4881</td>
<td style="text-align: center;">0.4318</td>
<td style="text-align: center;">0.4173</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN</td>
<td style="text-align: center;">0.3996</td>
<td style="text-align: center;">0.3280</td>
<td style="text-align: center;">0.3501</td>
<td style="text-align: center;">0.4068</td>
<td style="text-align: center;">0.4927</td>
<td style="text-align: center;">0.4361</td>
<td style="text-align: center;">0.4183</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DI</td>
<td style="text-align: center;">0.3998</td>
<td style="text-align: center;">0.3291</td>
<td style="text-align: center;">0.3500</td>
<td style="text-align: center;">0.4060</td>
<td style="text-align: center;">0.4918</td>
<td style="text-align: center;">0.4429</td>
<td style="text-align: center;">0.4166</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN</td>
<td style="text-align: center;">0.3880</td>
<td style="text-align: center;">0.3215</td>
<td style="text-align: center;">0.3369</td>
<td style="text-align: center;">0.3967</td>
<td style="text-align: center;">0.4820</td>
<td style="text-align: center;">0.4311</td>
<td style="text-align: center;">0.4127</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DE</td>
<td style="text-align: center;">0.3977</td>
<td style="text-align: center;">0.3265</td>
<td style="text-align: center;">0.3487</td>
<td style="text-align: center;">0.4057</td>
<td style="text-align: center;">0.4962</td>
<td style="text-align: center;">0.4378</td>
<td style="text-align: center;">0.4152</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;"><em>EQ-4D-5L</em> + <em>modules</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + (WA + DR)</td>
<td style="text-align: center;">0.3944</td>
<td style="text-align: center;">0.3290</td>
<td style="text-align: center;">0.3552</td>
<td style="text-align: center;">0.3987</td>
<td style="text-align: center;">0.4888</td>
<td style="text-align: center;">0.4355</td>
<td style="text-align: center;">0.4202</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + (PN + DI)</td>
<td style="text-align: center;">0.4042</td>
<td style="text-align: center;">0.3413</td>
<td style="text-align: center;">0.3529</td>
<td style="text-align: center;">0.4110</td>
<td style="text-align: center;">0.4963</td>
<td style="text-align: center;">0.4505</td>
<td style="text-align: center;">0.4267</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + (AN + DE)</td>
<td style="text-align: center;">0.4024</td>
<td style="text-align: center;">0.3364</td>
<td style="text-align: center;">0.3606</td>
<td style="text-align: center;">0.4100</td>
<td style="text-align: center;">0.5007</td>
<td style="text-align: center;">0.4417</td>
<td style="text-align: center;">0.4207</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + (WA × DR)</td>
<td style="text-align: center;">0.4044</td>
<td style="text-align: center;">0.3758</td>
<td style="text-align: center;">0.3940</td>
<td style="text-align: center;">0.4378</td>
<td style="text-align: center;">0.5215</td>
<td style="text-align: center;">0.4666</td>
<td style="text-align: center;">0.4446</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + (PN × DI)</td>
<td style="text-align: center;">0.4142</td>
<td style="text-align: center;">0.3832</td>
<td style="text-align: center;">0.3926</td>
<td style="text-align: center;">0.4540</td>
<td style="text-align: center;">0.5351</td>
<td style="text-align: center;">0.4937</td>
<td style="text-align: center;">0.4497</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + (AN × DE)</td>
<td style="text-align: center;">0.4174</td>
<td style="text-align: center;">0.4084</td>
<td style="text-align: center;">0.4060</td>
<td style="text-align: center;">0.4361</td>
<td style="text-align: center;">0.5269</td>
<td style="text-align: center;">0.4838</td>
<td style="text-align: center;">0.4447</td>
</tr>
</tbody>
</table>

All reported regression models are statistically significant (*p* \< 0.001, ANOVA F-test). The Cartesian product A x B implies {(a, b) \| a \epsilon A, b \epsilon B} (i.e. all combinations of levels from two component items, not the simple multiplication of item levels.)

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

## Discussion

This psychometric analysis evaluated the performance of EQ-5D-5L composites and their components in a general population sample of U.S. adults and by age group. We used a range of analytical methods to examine how well the composites captured the information provided by their respective components in terms of descriptive patterns and dimensional structure.

The first finding of our study concerned how composites performed relative to their components. At the individual level, response distributions and cross-tabulations showed that fewer respondents reported “no problems” and more reported some problems on the composites (SC, PD, and AD) than on their corresponding components. Ceiling and floor percentages confirmed that composites reflected a wide range of health problems than their individual components, which supports the interpretation of little to no underreporting. The patterns suggest that respondents interpreted composites as a logical combination of their corresponding components (e.g., pain OR discomfort) rather than focusing solely on a single component. These findings contradict four previous studies that reported fewer problems on composites than on their components \[11, 15–17\]. This discrepancy may be due to methodological differences, such as the separate presentation of composites and components in McDonald et al. and Tsuchiya et al. \[11, 15\], the use of disease-specific populations in Belay et al. or the use of Hungarian language in Rencz and Janssen \[16, 17\]. At the instrument level, the standard EQ-5D-5L generally outperformed the versions with only one component added (e.g., EQ-4D-5 L + WA, EQ-4D-5 L + DR), which further supports the idea that the composites might function better than individual components on their own. However, significant improvements were observed when both components of a composite were included (e.g., EQ-4D-5 L + PN + DI and EQ-4D-5 L + AN + DE). It is important to note that while composites outperformed individual components as stand-alone items, the combined inclusion of both components in a module enhanced the instrument’s overall informativity and explanatory power. This suggests that composites are meaningful and efficiently capture health problems, but disaggregated components may offer additional granularity when both are included. This interpretation is also supported by the lower correlations between the components in the same module compared to the correlations between each component and its composites, except for the PD module. These findings align with Belay et al., who reported increased informativity when replacing composites with their corresponding components \[17\].

On the other hand, our study supports the systematic order effect mentioned by Rencz and Janssen (i.e. respondents’ answers to the composites appeared to be primarily influenced by the first-listed components) \[16\]. Cross-tabulations showed that PN and AN shared a higher proportion of responses with their respective composites, PD and AD, than DI and DE did. Convergent validity results also indicated stronger correlations between PN and PD, and between AN and AD, compared to DI and DE. A similar, though less consistent, pattern was observed for WA and DR. Taken together with our earlier finding that composites captured more reported problems than their corresponding components at the individual level, these results may reflect an ordering bias in the survey structure. Respondents completed the EQ-5D-5L composites before their split components, and the components were presented in a fixed order. Future research should examine whether this pattern holds when the order of components is randomized and when the components are presented between the core EQ-5D-5L dimensions.

Our findings offer practical implications for tailoring EQ-5D-5L applications to specific age groups. Ceiling percentages for PD, PN, and DI decreased with age, suggesting that older adults may benefit from expanded assessment of pain-related issues. In contrast, younger adults, particularly those aged 18–29, reported more mental health concerns, indicating greater relevance of the AD composite and its components in this population. Supporting these patterns, the inclusion of interaction terms further highlighted age-specific differences in explanatory power: the 60–69 age group experienced the largest increase in adjusted R² when PN × DI interactions were included, while the 18–29 age group showed the greatest increase in explanatory power when AN × DE interactions were added. Additionally, EFA showed that the underlying structure of the EQ-5D-5L remained stable with or without the component items, indicating that splitting the composites can enhance measurement precision without altering the instrument’s dimensional integrity. However, as our study was based on a general population sample using an online survey, it is unclear whether these findings generalize to clinical populations. Future research should examine the performance and factor structure of the composite and component items in disease-specific populations to assess the broader applicability.

Lastly, given the performance of WA and DR across our analyses, we did not observe substantial improvements in psychometric performance when analyzing them separately from SC. However, as this study was conducted in a general population sample, these findings may not generalize to clinical populations with higher prevalence of self-care problems (e.g., individuals with stroke, Parkinson’s disease, or multiple sclerosis). Moreover, the correlation between WA and the SC composite was the lowest among the three modules, which suggests that respondents may distinguish between these aspects of self-care. Additionally, variations in how SC is interpreted across different language versions of the EQ-5D-5L may affect the functioning of its components. For example, the U.S. version uses the phrase “washing or dressing myself,” while other translations differ in interpretation. In the Chinese version, the term “洗澡”is used, which means “bathing,” whereas in the Vietnamese version, the term “giặt giũ” is used, which refers to “doing laundry.” \[45, 46\] Such inconsistencies may limit the reliability and comparability of SC component items across settings.

There are limitations to our study that warrant consideration for future research. First, the use of an online survey may have introduced sampling bias, potentially underrepresenting individuals with limited internet access or lower digital literacy, thereby affecting the generalizability of the findings \[47\]. Future research is encouraged to combine online surveys with face-to-face interviews to improve the validity of the data. Second, during the data collection process, we employed quota sampling based on broader age bands (18–34, 35–54, and 55+) but later analyzed and reported results using narrower bands. This could limit the generalizability of age-specific findings and introduce sampling bias, especially if certain age subgroups are over- or underrepresented due to differential response rates. Third, we did not include utility analyses in this study, as our primary focus was on measurement properties and psychometric performance. However, given the widespread use of EQ-5D-5L in health technology assessment, future research should explore how the component- and composite-level data can be leveraged for greater precision when summarizing effectiveness.

## Conclusions

This study found that the EQ-5D-5L composites generally captured the information provided by their components, with comparable or even broader coverage in many aspects. It was also noted that there were little to no statistically significant differences observed between SC and its components (WA and DR). The overall construct of the EQ-5D-5L remained stable with or without components, suggesting robust dimensionality. Age group analyses highlighted the instrument’s potential adaptability, with younger adults reporting more mental health issues and older adults more pain-related problems. Future research should assess the performance and structure of composite and component items in disease-specific populations and explore the effects of randomizing the order and placement of component items within the instrument.

## Acknowledgements

This work was presented at the 9th EuroQol Academy Meeting held March 11–13, 2025, in Barcelona, Catalonia, Spain. We thank Jan Abel Olsen for leading the discussion and the attendees for their insightful comments, particularly those on the measurement of activities for daily living (ADLs) in older adults.

### Appendix 1: Respondent characteristics by completion and compared with U.S. census estimates

<div id="Taba" class="table-wrap">

|  | Completed N = 6018% (n) | Dropout N = 1928% (n) | *p*-value | 2023 ACS\* % |
|----|----|----|----|----|
| Age in years |  |  |  \< 0.001 |  |
| 18 to 34 | 27 (1,621) | 20 (393) |  | 29 |
| 35 to 54 | 38 (2,290) | 33 (631) |  | 32 |
| 55 and older | 35 (2,107) | 47 (904) |  | 39 |
| Gender |  |  |  \< 0.001 |  |
| Female | 51 (3,082) | 60 (1,160) |  | 51 |
| Male | 48 (2,908) | 39 (757) |  | 49 |
| Other/prefer not to say | 0.5 (28) | 0.6 (11) |  |  |
| Race |  |  | 0.054 |  |
| White | 74 (4,476) | 77 (1,494) |  | 63 |
| Black or African American | 14 (849) | 13 (252) |  | 12 |
| American Indian or Alaska Native | 1.2 (73) | 0.7 (13) |  | 0.9 |
| Asian | 3.3 (197) | 2.7 (52) |  | 6.2 |
| Native Hawaiian or Other Pacific Islander | 0.2 (13) | 0.3 (5) |  | 0.2 |
| Some other race | 3.2 (191) | 3.1 (60) |  | 7 |
| Two or more races | 3.6 (219) | 2.7 (52) |  | 11 |
| Ethnicity |  |  |  \< 0.001 |  |
| Hispanic or Latino | 12 (723) | 9.1 (175) |  | 18 |
| Other | 88 (5,295) | 91 (1,753) |  | 82 |
| U.S. regions |  |  | 0.118 |  |
| Northeast | 17 (1,042) | 16 (309) |  | 17 |
| Midwest | 22 (1,311) | 24 (466) |  | 20 |
| South | 42 (2,553) | 41 (791) |  | 39 |
| West | 18 (1,112) | 19 (362) |  | 24 |

\*Taken from the United States Census Bureau 2023 American Community Survey

</div>

### Appendix 2: Distribution of EQ-5D-5L and component responses by age groups, % (n)

<div id="Tabb" class="table-wrap">

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 4</th>
<th style="text-align: left;">Level 5</th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 4</th>
<th style="text-align: left;">Level 5</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">18–29 (<em>n</em> = 865)</th>
<th colspan="5" style="text-align: left;">30–39 (<em>n</em> = 1267)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">86 (743)</td>
<td style="text-align: center;">11 (94)</td>
<td style="text-align: center;">2 (19)</td>
<td style="text-align: center;">1 (9)</td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">85 (1082)</td>
<td style="text-align: center;">10 (126)</td>
<td style="text-align: center;">3 (41)</td>
<td style="text-align: center;">1 (9)</td>
<td style="text-align: center;">1 (9)</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">91 (787)</td>
<td style="text-align: center;">7 (58)</td>
<td style="text-align: center;">2 (14)</td>
<td style="text-align: center;">1 (5)</td>
<td style="text-align: left;">0 (1)</td>
<td style="text-align: center;">93 (1176)</td>
<td style="text-align: center;">5 (63)</td>
<td style="text-align: center;">1 (19)</td>
<td style="text-align: center;">0 (3)</td>
<td style="text-align: center;">0 (6)</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">78 (673)</td>
<td style="text-align: center;">15 (126)</td>
<td style="text-align: center;">5 (43)</td>
<td style="text-align: center;">2 (18)</td>
<td style="text-align: left;">1 (5)</td>
<td style="text-align: center;">81 (1028)</td>
<td style="text-align: center;">13 (160)</td>
<td style="text-align: center;">5 (59)</td>
<td style="text-align: center;">1 (16)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">52 (450)</td>
<td style="text-align: center;">31 (269)</td>
<td style="text-align: center;">13 (113)</td>
<td style="text-align: center;">3 (24)</td>
<td style="text-align: left;">1 (10)</td>
<td style="text-align: center;">47 (597)</td>
<td style="text-align: center;">33 (423)</td>
<td style="text-align: center;">14 (180)</td>
<td style="text-align: center;">5 (58)</td>
<td style="text-align: center;">1 (9)</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">33 (284)</td>
<td style="text-align: center;">25 (218)</td>
<td style="text-align: center;">24 (205)</td>
<td style="text-align: center;">11 (95)</td>
<td style="text-align: left;">7 (63)</td>
<td style="text-align: center;">37 (469)</td>
<td style="text-align: center;">25 (323)</td>
<td style="text-align: center;">23 (289)</td>
<td style="text-align: center;">10 (129)</td>
<td style="text-align: center;">4 (57)</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">92 (792)</td>
<td style="text-align: center;">6 (49)</td>
<td style="text-align: center;">2 (17)</td>
<td style="text-align: center;">1 (5)</td>
<td style="text-align: left;">0 (2)</td>
<td style="text-align: center;">93 (1174)</td>
<td style="text-align: center;">5 (68)</td>
<td style="text-align: center;">1 (16)</td>
<td style="text-align: center;">0 (5)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">93 (803)</td>
<td style="text-align: center;">5 (40)</td>
<td style="text-align: center;">2 (16)</td>
<td style="text-align: center;">1 (6)</td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">94 (1190)</td>
<td style="text-align: center;">4 (53)</td>
<td style="text-align: center;">1 (16)</td>
<td style="text-align: center;">0 (5)</td>
<td style="text-align: center;">0 (3)</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">53 (459)</td>
<td style="text-align: center;">30 (260)</td>
<td style="text-align: center;">13 (109)</td>
<td style="text-align: center;">3 (26)</td>
<td style="text-align: left;">1 (11)</td>
<td style="text-align: center;">48 (607)</td>
<td style="text-align: center;">32 (408)</td>
<td style="text-align: center;">14 (179)</td>
<td style="text-align: center;">5 (62)</td>
<td style="text-align: center;">1 (11)</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">54 (471)</td>
<td style="text-align: center;">21 (269)</td>
<td style="text-align: center;">10 (88)</td>
<td style="text-align: center;">3 (24)</td>
<td style="text-align: left;">2 (13)</td>
<td style="text-align: center;">51 (640)</td>
<td style="text-align: center;">33 (423)</td>
<td style="text-align: center;">12 (154)</td>
<td style="text-align: center;">3 (43)</td>
<td style="text-align: center;">1 (7)</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">34 (292)</td>
<td style="text-align: center;">26 (229)</td>
<td style="text-align: center;">23 (198)</td>
<td style="text-align: center;">10 (83)</td>
<td style="text-align: left;">7 (63)</td>
<td style="text-align: center;">41 (520)</td>
<td style="text-align: center;">27 (348)</td>
<td style="text-align: center;">19 (239)</td>
<td style="text-align: center;">9 (111)</td>
<td style="text-align: center;">4 (49)</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">46 (394)</td>
<td style="text-align: center;">24 (208)</td>
<td style="text-align: center;">18 (156)</td>
<td style="text-align: center;">8 (65)</td>
<td style="text-align: left;">5 (42)</td>
<td style="text-align: center;">49 (617)</td>
<td style="text-align: center;">24 (306)</td>
<td style="text-align: center;">16 (203)</td>
<td style="text-align: center;">7 (95)</td>
<td style="text-align: center;">4 (46)</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">40–49 (<em>n</em> = 1160)</th>
<th colspan="5" style="text-align: left;">50–59 (<em>n</em> = 997)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">77 (890)</td>
<td style="text-align: center;">14 (168)</td>
<td style="text-align: center;">7 (77)</td>
<td style="text-align: center;">2 (19)</td>
<td style="text-align: left;">1 (6)</td>
<td style="text-align: center;">64 (640)</td>
<td style="text-align: center;">22 (220)</td>
<td style="text-align: center;">10 (103)</td>
<td style="text-align: center;">2 (24)</td>
<td style="text-align: center;">1 (10)</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">90 (1043)</td>
<td style="text-align: center;">8 (89)</td>
<td style="text-align: center;">2 (23)</td>
<td style="text-align: center;">0 (5)</td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">87 (867)</td>
<td style="text-align: center;">9 (93)</td>
<td style="text-align: center;">3 (31)</td>
<td style="text-align: center;">0 (3)</td>
<td style="text-align: center;">0 (3)</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">75 (871)</td>
<td style="text-align: center;">16 (188)</td>
<td style="text-align: center;">7 (83)</td>
<td style="text-align: center;">1 (16)</td>
<td style="text-align: left;">0 (2)</td>
<td style="text-align: center;">67 (664)</td>
<td style="text-align: center;">19 (191)</td>
<td style="text-align: center;">10 (104)</td>
<td style="text-align: center;">3 (30)</td>
<td style="text-align: center;">1 (8)</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">38 (440)</td>
<td style="text-align: center;">31 (364)</td>
<td style="text-align: center;">22 (250)</td>
<td style="text-align: center;">7 (83)</td>
<td style="text-align: left;">2 (23)</td>
<td style="text-align: center;">30 (300)</td>
<td style="text-align: center;">36 (359)</td>
<td style="text-align: center;">23 (233)</td>
<td style="text-align: center;">8 (78)</td>
<td style="text-align: center;">3 (27)</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">42 (487)</td>
<td style="text-align: center;">26 (303)</td>
<td style="text-align: center;">18 (204)</td>
<td style="text-align: center;">9 (102)</td>
<td style="text-align: left;">6 (64)</td>
<td style="text-align: center;">46 (454)</td>
<td style="text-align: center;">25 (254)</td>
<td style="text-align: center;">18 (175)</td>
<td style="text-align: center;">7 (65)</td>
<td style="text-align: center;">5 (49)</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">90 (1039)</td>
<td style="text-align: center;">8 (87)</td>
<td style="text-align: center;">2 (27)</td>
<td style="text-align: center;">1 (7)</td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">89 (886)</td>
<td style="text-align: center;">8 (80)</td>
<td style="text-align: center;">3 (25)</td>
<td style="text-align: center;">1 (5)</td>
<td style="text-align: center;">0 (1)</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">89 (1033)</td>
<td style="text-align: center;">8 (93)</td>
<td style="text-align: center;">2 (29)</td>
<td style="text-align: center;">0 (3)</td>
<td style="text-align: left;">0 (2)</td>
<td style="text-align: center;">87 (865)</td>
<td style="text-align: center;">10 (101)</td>
<td style="text-align: center;">3 (25)</td>
<td style="text-align: center;">1 (5)</td>
<td style="text-align: center;">0 (1)</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">38 (440)</td>
<td style="text-align: center;">31 (364)</td>
<td style="text-align: center;">22 (250)</td>
<td style="text-align: center;">7 (83)</td>
<td style="text-align: left;">2 (23)</td>
<td style="text-align: center;">30 (298)</td>
<td style="text-align: center;">36 (360)</td>
<td style="text-align: center;">23 (230)</td>
<td style="text-align: center;">8 (81)</td>
<td style="text-align: center;">3 (28)</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">42 (487)</td>
<td style="text-align: center;">34 (400)</td>
<td style="text-align: center;">16 (188)</td>
<td style="text-align: center;">5 (58)</td>
<td style="text-align: left;">2 (27)</td>
<td style="text-align: center;">35 (349)</td>
<td style="text-align: center;">37 (367)</td>
<td style="text-align: center;">19 (192)</td>
<td style="text-align: center;">7 (69)</td>
<td style="text-align: center;">2 (20)</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">45 (517)</td>
<td style="text-align: center;">27 (312)</td>
<td style="text-align: center;">17 (194)</td>
<td style="text-align: center;">7 (82)</td>
<td style="text-align: left;">5 (55)</td>
<td style="text-align: center;">49 (493)</td>
<td style="text-align: center;">27 (268)</td>
<td style="text-align: center;">14 (139)</td>
<td style="text-align: center;">6 (56)</td>
<td style="text-align: center;">4 (41)</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">51 (596)</td>
<td style="text-align: center;">24 (278)</td>
<td style="text-align: center;">14 (163)</td>
<td style="text-align: center;">6 (75)</td>
<td style="text-align: left;">4 (48)</td>
<td style="text-align: center;">55 (545)</td>
<td style="text-align: center;">25 (245)</td>
<td style="text-align: center;">13 (129)</td>
<td style="text-align: center;">4 (43)</td>
<td style="text-align: center;">4 (35)</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">60–69 (<em>n</em> = 909)</th>
<th colspan="5" style="text-align: left;">70 + (<em>n</em> = 820)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">65 (589)</td>
<td style="text-align: center;">22 (198)</td>
<td style="text-align: center;">9 (86)</td>
<td style="text-align: center;">4 (32)</td>
<td style="text-align: left;">0 (4)</td>
<td style="text-align: center;">65 (531)</td>
<td style="text-align: center;">23 (185)</td>
<td style="text-align: center;">9 (73)</td>
<td style="text-align: center;">3 (27)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">89 (810)</td>
<td style="text-align: center;">8 (72)</td>
<td style="text-align: center;">3 (24)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;">0 (2)</td>
<td style="text-align: center;">92 (756)</td>
<td style="text-align: center;">5 (45)</td>
<td style="text-align: center;">2 (13)</td>
<td style="text-align: center;">0 (2)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">69 (630)</td>
<td style="text-align: center;">20 (182)</td>
<td style="text-align: center;">7 (67)</td>
<td style="text-align: center;">3 (24)</td>
<td style="text-align: left;">1 (6)</td>
<td style="text-align: center;">73 (600)</td>
<td style="text-align: center;">17 (136)</td>
<td style="text-align: center;">8 (69)</td>
<td style="text-align: center;">1 (11)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">31 (278)</td>
<td style="text-align: center;">39 (357)</td>
<td style="text-align: center;">22 (197)</td>
<td style="text-align: center;">7 (62)</td>
<td style="text-align: left;">2 (15)</td>
<td style="text-align: center;">31 (252)</td>
<td style="text-align: center;">45 (369)</td>
<td style="text-align: center;">19 (156)</td>
<td style="text-align: center;">5 (38)</td>
<td style="text-align: center;">1 (5)</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">64 (584)</td>
<td style="text-align: center;">23 (206)</td>
<td style="text-align: center;">9 (85)</td>
<td style="text-align: center;">3 (24)</td>
<td style="text-align: left;">1 (10)</td>
<td style="text-align: center;">74 (609)</td>
<td style="text-align: center;">19 (155)</td>
<td style="text-align: center;">6 (46)</td>
<td style="text-align: center;">1 (6)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td colspan="11" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">92 (837)</td>
<td style="text-align: center;">6 (53)</td>
<td style="text-align: center;">2 (17)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;">0 (1)</td>
<td style="text-align: center;">94 (771)</td>
<td style="text-align: center;">4 (33)</td>
<td style="text-align: center;">1 (11)</td>
<td style="text-align: center;">0 (3)</td>
<td style="text-align: center;">0 (2)</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">90 (817)</td>
<td style="text-align: center;">8 (75)</td>
<td style="text-align: center;">1 (13)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: left;">0 (3)</td>
<td style="text-align: center;">93 (760)</td>
<td style="text-align: center;">6 (50)</td>
<td style="text-align: center;">1 (7)</td>
<td style="text-align: center;">0 (1)</td>
<td style="text-align: center;">0 (2)</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">31 (278)</td>
<td style="text-align: center;">40 (367)</td>
<td style="text-align: center;">21 (192)</td>
<td style="text-align: center;">6 (59)</td>
<td style="text-align: left;">1 (13)</td>
<td style="text-align: center;">31 (255)</td>
<td style="text-align: center;">45 (371)</td>
<td style="text-align: center;">19 (158)</td>
<td style="text-align: center;">4 (30)</td>
<td style="text-align: center;">1 (6)</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">37 (336)</td>
<td style="text-align: center;">41 (373)</td>
<td style="text-align: center;">16 (148)</td>
<td style="text-align: center;">5 (42)</td>
<td style="text-align: left;">1 (10)</td>
<td style="text-align: center;">39 (320)</td>
<td style="text-align: center;">44 (359)</td>
<td style="text-align: center;">13 (110)</td>
<td style="text-align: center;">3 (27)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">67 (612)</td>
<td style="text-align: center;">22 (196)</td>
<td style="text-align: center;">8 (70)</td>
<td style="text-align: center;">2 (21)</td>
<td style="text-align: left;">1 (10)</td>
<td style="text-align: center;">76 (627)</td>
<td style="text-align: center;">18 (147)</td>
<td style="text-align: center;">5 (38)</td>
<td style="text-align: center;">0 (4)</td>
<td style="text-align: center;">0 (4)</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">74 (672)</td>
<td style="text-align: center;">16 (147)</td>
<td style="text-align: center;">7 (66)</td>
<td style="text-align: center;">2 (19)</td>
<td style="text-align: left;">1 (5)</td>
<td style="text-align: center;">83 (677)</td>
<td style="text-align: center;">13 (106)</td>
<td style="text-align: center;">4 (32)</td>
<td style="text-align: center;">0 (2)</td>
<td style="text-align: center;">0 (3)</td>
</tr>
</tbody>
</table>

Level 1: No, Level 2: Slight, Level 3: Moderate, Level 4: Severe, Level 5: Extreme

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

### Appendix 3: Results of Shannon index (H′) and Shannon evenness index (J′) of EQ-5D-5L composites and components by age groups

<div id="Tabc" class="table-wrap">

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Shannon index (H′)</th>
<th style="text-align: left;">Shannon evenness index (J′)</th>
<th style="text-align: left;">Shannon index (H′)</th>
<th style="text-align: left;">Shannon evenness index (J′)</th>
<th style="text-align: left;">Shannon index (H′)</th>
<th style="text-align: left;">Shannon evenness index (J′)</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">18–29</th>
<th colspan="2" style="text-align: left;">30–39</th>
<th colspan="2" style="text-align: left;">40–49</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">0.7665</td>
<td style="text-align: center;">0.3301</td>
<td style="text-align: center;">0.7872</td>
<td style="text-align: center;">0.3390</td>
<td style="text-align: center;">1.0932</td>
<td style="text-align: center;">0.4708</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">0.4950</td>
<td style="text-align: center;">0.2131</td>
<td style="text-align: center;">0.4632</td>
<td style="text-align: center;">0.1995</td>
<td style="text-align: center;">0.5681</td>
<td style="text-align: center;">0.2447</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">0.9871</td>
<td style="text-align: center;">0.4251</td>
<td style="text-align: center;">0.9336</td>
<td style="text-align: center;">0.4021</td>
<td style="text-align: center;">1.1092</td>
<td style="text-align: center;">0.4777</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">1.6656</td>
<td style="text-align: center;">0.7173</td>
<td style="text-align: center;">1.6943</td>
<td style="text-align: center;">0.7297</td>
<td style="text-align: center;">1.9010</td>
<td style="text-align: center;">0.8187</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">2.0963</td>
<td style="text-align: center;">0.9028</td>
<td style="text-align: center;">2.0566</td>
<td style="text-align: center;">0.8857</td>
<td style="text-align: center;">2.0112</td>
<td style="text-align: center;">0.8663</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">0.4909</td>
<td style="text-align: center;">0.2114</td>
<td style="text-align: center;">0.4658</td>
<td style="text-align: center;">0.2006</td>
<td style="text-align: center;">0.5934</td>
<td style="text-align: center;">0.2556</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">0.4315</td>
<td style="text-align: center;">0.1858</td>
<td style="text-align: center;">0.4083</td>
<td style="text-align: center;">0.1759</td>
<td style="text-align: center;">0.6120</td>
<td style="text-align: center;">0.2636</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">1.6726</td>
<td style="text-align: center;">0.7203</td>
<td style="text-align: center;">1.7064</td>
<td style="text-align: center;">0.7349</td>
<td style="text-align: center;">1.9168</td>
<td style="text-align: center;">0.8255</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">1.5933</td>
<td style="text-align: center;">0.6862</td>
<td style="text-align: center;">1.6027</td>
<td style="text-align: center;">0.6903</td>
<td style="text-align: center;">1.8232</td>
<td style="text-align: center;">0.7852</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">2.0473</td>
<td style="text-align: center;">0.8817</td>
<td style="text-align: center;">1.9825</td>
<td style="text-align: center;">0.8538</td>
<td style="text-align: center;">1.9394</td>
<td style="text-align: center;">0.8353</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">1.9082</td>
<td style="text-align: center;">0.8218</td>
<td style="text-align: center;">1.8777</td>
<td style="text-align: center;">0.8087</td>
<td style="text-align: center;">1.8310</td>
<td style="text-align: center;">0.7886</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: center;">4.8989</td>
<td style="text-align: center;">0.6741</td>
<td style="text-align: center;">4.7551</td>
<td style="text-align: center;">0.6389</td>
<td style="text-align: center;">5.1522</td>
<td style="text-align: center;">0.6760</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>EQ-4D-5L</em> + <em>components</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA</td>
<td style="text-align: center;">4.8674</td>
<td style="text-align: center;">0.6698</td>
<td style="text-align: center;">4.7883</td>
<td style="text-align: center;">0.6398</td>
<td style="text-align: center;">5.1795</td>
<td style="text-align: center;">0.6809</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DR</td>
<td style="text-align: center;">4.8269</td>
<td style="text-align: center;">0.6732</td>
<td style="text-align: center;">4.7398</td>
<td style="text-align: center;">0.6347</td>
<td style="text-align: center;">5.1801</td>
<td style="text-align: center;">0.6758</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN</td>
<td style="text-align: center;">4.9146</td>
<td style="text-align: center;">0.6763</td>
<td style="text-align: center;">4.7728</td>
<td style="text-align: center;">0.6405</td>
<td style="text-align: center;">5.1604</td>
<td style="text-align: center;">0.6777</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DI</td>
<td style="text-align: center;">4.8611</td>
<td style="text-align: center;">0.6689</td>
<td style="text-align: center;">4.6453</td>
<td style="text-align: center;">0.6262</td>
<td style="text-align: center;">5.0474</td>
<td style="text-align: center;">0.6616</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN</td>
<td style="text-align: center;">4.8660</td>
<td style="text-align: center;">0.6722</td>
<td style="text-align: center;">4.7036</td>
<td style="text-align: center;">0.6306</td>
<td style="text-align: center;">5.0875</td>
<td style="text-align: center;">0.6694</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DE</td>
<td style="text-align: center;">4.6863</td>
<td style="text-align: center;">0.6508</td>
<td style="text-align: center;">4.6323</td>
<td style="text-align: center;">0.6196</td>
<td style="text-align: center;">5.0015</td>
<td style="text-align: center;">0.6581</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>EQ-4D-5L</em> + <em>modules</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA + DR</td>
<td style="text-align: center;">4.9422</td>
<td style="text-align: center;">0.6678</td>
<td style="text-align: center;">4.8437</td>
<td style="text-align: center;">0.6343</td>
<td style="text-align: center;">5.2964</td>
<td style="text-align: center;">0.6751</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN + DI</td>
<td style="text-align: center;">5.3980</td>
<td style="text-align: center;">0.7023</td>
<td style="text-align: center;">5.2432</td>
<td style="text-align: center;">0.6694</td>
<td style="text-align: center;">5.6302</td>
<td style="text-align: center;">0.7063</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN + DE</td>
<td style="text-align: center;">5.8393</td>
<td style="text-align: center;">0.7414</td>
<td style="text-align: center;">5.6623</td>
<td style="text-align: center;">0.6957</td>
<td style="text-align: center;">5.8532</td>
<td style="text-align: center;">0.7169</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">50–59</th>
<th colspan="2" style="text-align: left;">60–69</th>
<th colspan="2" style="text-align: left;">70 + </th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7" style="text-align: left;"><em>EQ-5D-5L</em></td>
</tr>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: center;">1.4259</td>
<td style="text-align: center;">0.6141</td>
<td style="text-align: center;">1.4108</td>
<td style="text-align: center;">0.6076</td>
<td style="text-align: center;">1.4009</td>
<td style="text-align: center;">0.6033</td>
</tr>
<tr>
<td style="text-align: left;">SC</td>
<td style="text-align: center;">0.7006</td>
<td style="text-align: center;">0.3017</td>
<td style="text-align: center;">0.6067</td>
<td style="text-align: center;">0.2613</td>
<td style="text-align: center;">0.4913</td>
<td style="text-align: center;">0.2116</td>
</tr>
<tr>
<td style="text-align: left;">UA</td>
<td style="text-align: center;">1.3954</td>
<td style="text-align: center;">0.6010</td>
<td style="text-align: center;">1.2947</td>
<td style="text-align: center;">0.5576</td>
<td style="text-align: center;">1.1810</td>
<td style="text-align: center;">0.5086</td>
</tr>
<tr>
<td style="text-align: left;">PD</td>
<td style="text-align: center;">1.9707</td>
<td style="text-align: center;">0.8487</td>
<td style="text-align: center;">1.8923</td>
<td style="text-align: center;">0.8150</td>
<td style="text-align: center;">1.7472</td>
<td style="text-align: center;">0.7524</td>
</tr>
<tr>
<td style="text-align: left;">AD</td>
<td style="text-align: center;">1.9304</td>
<td style="text-align: center;">0.8314</td>
<td style="text-align: center;">1.4251</td>
<td style="text-align: center;">0.6138</td>
<td style="text-align: center;">1.0955</td>
<td style="text-align: center;">0.4718</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>Components</em></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: center;">0.6250</td>
<td style="text-align: center;">0.2692</td>
<td style="text-align: center;">0.4777</td>
<td style="text-align: center;">0.2057</td>
<td style="text-align: center;">0.4043</td>
<td style="text-align: center;">0.1741</td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: center;">0.6940</td>
<td style="text-align: center;">0.2989</td>
<td style="text-align: center;">0.5610</td>
<td style="text-align: center;">0.2416</td>
<td style="text-align: center;">0.4393</td>
<td style="text-align: center;">0.1892</td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: center;">1.9785</td>
<td style="text-align: center;">0.8521</td>
<td style="text-align: center;">1.8685</td>
<td style="text-align: center;">0.8047</td>
<td style="text-align: center;">1.7260</td>
<td style="text-align: center;">0.7433</td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: center;">1.8983</td>
<td style="text-align: center;">0.8175</td>
<td style="text-align: center;">1.7610</td>
<td style="text-align: center;">0.7584</td>
<td style="text-align: center;">1.6399</td>
<td style="text-align: center;">0.7063</td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: center;">1.8308</td>
<td style="text-align: center;">0.7885</td>
<td style="text-align: center;">1.3435</td>
<td style="text-align: center;">0.5786</td>
<td style="text-align: center;">1.0209</td>
<td style="text-align: center;">0.4397</td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: center;">1.7208</td>
<td style="text-align: center;">0.7411</td>
<td style="text-align: center;">1.1799</td>
<td style="text-align: center;">0.5082</td>
<td style="text-align: center;">0.8432</td>
<td style="text-align: center;">0.3631</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: center;">5.5740</td>
<td style="text-align: center;">0.7200</td>
<td style="text-align: center;">4.9711</td>
<td style="text-align: center;">0.6725</td>
<td style="text-align: center;">4.5803</td>
<td style="text-align: center;">0.6472</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>EQ-4D-5L</em> + <em>components</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA</td>
<td style="text-align: center;">5.5557</td>
<td style="text-align: center;">0.7208</td>
<td style="text-align: center;">4.9406</td>
<td style="text-align: center;">0.6731</td>
<td style="text-align: center;">4.5461</td>
<td style="text-align: center;">0.6464</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DR</td>
<td style="text-align: center;">5.5977</td>
<td style="text-align: center;">0.7225</td>
<td style="text-align: center;">4.9607</td>
<td style="text-align: center;">0.6726</td>
<td style="text-align: center;">4.5860</td>
<td style="text-align: center;">0.6461</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN</td>
<td style="text-align: center;">5.6188</td>
<td style="text-align: center;">0.7185</td>
<td style="text-align: center;">4.9895</td>
<td style="text-align: center;">0.6704</td>
<td style="text-align: center;">4.5553</td>
<td style="text-align: center;">0.6477</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DI</td>
<td style="text-align: center;">5.5105</td>
<td style="text-align: center;">0.7070</td>
<td style="text-align: center;">4.8679</td>
<td style="text-align: center;">0.6540</td>
<td style="text-align: center;">4.4982</td>
<td style="text-align: center;">0.6337</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN</td>
<td style="text-align: center;">5.5012</td>
<td style="text-align: center;">0.7082</td>
<td style="text-align: center;">4.9341</td>
<td style="text-align: center;">0.6682</td>
<td style="text-align: center;">4.5217</td>
<td style="text-align: center;">0.6429</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + DE</td>
<td style="text-align: center;">5.4423</td>
<td style="text-align: center;">0.7000</td>
<td style="text-align: center;">4.7854</td>
<td style="text-align: center;">0.6536</td>
<td style="text-align: center;">4.3721</td>
<td style="text-align: center;">0.6246</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><em>EQ-4D-5L</em> + <em>modules</em></td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + WA + DR</td>
<td style="text-align: center;">5.6600</td>
<td style="text-align: center;">0.7197</td>
<td style="text-align: center;">5.0297</td>
<td style="text-align: center;">0.6685</td>
<td style="text-align: center;">4.6380</td>
<td style="text-align: center;">0.6407</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + PN + DI</td>
<td style="text-align: center;">6.1050</td>
<td style="text-align: center;">0.7473</td>
<td style="text-align: center;">5.5231</td>
<td style="text-align: center;">0.7110</td>
<td style="text-align: center;">5.1334</td>
<td style="text-align: center;">0.6913</td>
</tr>
<tr>
<td style="text-align: left;">EQ-4D-5L + AN + DE</td>
<td style="text-align: center;">6.0870</td>
<td style="text-align: center;">0.7389</td>
<td style="text-align: center;">5.3514</td>
<td style="text-align: center;">0.6883</td>
<td style="text-align: center;">4.8160</td>
<td style="text-align: center;">0.6538</td>
</tr>
</tbody>
</table>

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort; AD, anxiety/depression; WA, washing self; DR, dressing self; PN, pain; DI, discomfort; AN, anxiety; DE, depression

</div>

### Appendix 4: Spearman’s correlation coefficients between EQ-5D-5L, components and EQ VAS by age groups

<div id="Tabd" class="table-wrap">

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="5" style="text-align: left;">EQ-5D-5L composites</th>
<th colspan="6" style="text-align: left;">Components</th>
<th style="text-align: left;">EQ VAS</th>
<th colspan="5" style="text-align: left;">EQ-5D-5L composites</th>
<th colspan="6" style="text-align: left;">Components</th>
<th style="text-align: left;">EQ VAS</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="12" style="text-align: left;">18–29</th>
<th colspan="12" style="text-align: left;">30–39</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">SC</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">UA</td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">PD</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">AD</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.65</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">0.65</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.73</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.87</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">0.16</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.85</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;"> − 0.33</td>
<td style="text-align: left;"> − 0.24</td>
<td style="text-align: left;"> − 0.39</td>
<td style="text-align: left;"> − 0.47</td>
<td style="text-align: left;"> − 0.47</td>
<td style="text-align: left;"> − 0.23</td>
<td style="text-align: left;"> − 0.21</td>
<td style="text-align: left;"> − 0.48</td>
<td style="text-align: left;"> − 0.47</td>
<td style="text-align: left;"> − 0.47</td>
<td style="text-align: left;"> − 0.47</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"> − 0.32</td>
<td style="text-align: left;"> − 0.28</td>
<td style="text-align: left;"> − 0.40</td>
<td style="text-align: left;"> − 0.44</td>
<td style="text-align: left;"> − 0.49</td>
<td style="text-align: left;"> − 0.26</td>
<td style="text-align: left;"> − 0.23</td>
<td style="text-align: left;"> − 0.43</td>
<td style="text-align: left;"> − 0.45</td>
<td style="text-align: left;"> − 0.47</td>
<td style="text-align: left;"> − 0.48</td>
<td style="text-align: left;">1</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="12" style="text-align: left;">40–49</th>
<th colspan="12" style="text-align: left;">50–59</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">SC</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">UA</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.54</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.73</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">PD</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.58</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.59</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">AD</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">0.42</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">0.54</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.58</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">0.89</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.59</td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">0.59</td>
<td style="text-align: left;">0.85</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.89</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.89</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.85</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.48</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;"> − 0.43</td>
<td style="text-align: left;"> − 0.34</td>
<td style="text-align: left;"> − 0.48</td>
<td style="text-align: left;"> − 0.53</td>
<td style="text-align: left;"> − 0.48</td>
<td style="text-align: left;"> − 0.30</td>
<td style="text-align: left;"> − 0.32</td>
<td style="text-align: left;"> − 0.53</td>
<td style="text-align: left;"> − 0.53</td>
<td style="text-align: left;"> − 0.45</td>
<td style="text-align: left;"> − 0.45</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"> − 0.52</td>
<td style="text-align: left;"> − 0.41</td>
<td style="text-align: left;"> − 0.56</td>
<td style="text-align: left;"> − 0.54</td>
<td style="text-align: left;"> − 0.52</td>
<td style="text-align: left;"> − 0.36</td>
<td style="text-align: left;"> − 0.38</td>
<td style="text-align: left;"> − 0.54</td>
<td style="text-align: left;"> − 0.56</td>
<td style="text-align: left;"> − 0.50</td>
<td style="text-align: left;"> − 0.49</td>
<td style="text-align: left;">1</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="12" style="text-align: left;">60–69</th>
<th colspan="12" style="text-align: left;">70 + </th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
<th style="text-align: left;">WA</th>
<th style="text-align: left;">DR</th>
<th style="text-align: left;">PN</th>
<th style="text-align: left;">DI</th>
<th style="text-align: left;">AN</th>
<th style="text-align: left;">DE</th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">SC</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">UA</td>
<td style="text-align: left;">0.73</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">PD</td>
<td style="text-align: left;">0.60</td>
<td style="text-align: left;">0.38</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">1</td>
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
<td style="text-align: left;">AD</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">WA</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.20</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DR</td>
<td style="text-align: left;">0.46</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.54</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.47</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.69</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PN</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.93</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DI</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.40</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.41</td>
<td style="text-align: left;">0.85</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AN</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.34</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">0.16</td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">DE</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">0.30</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.80</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.71</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">0.70</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ VAS</td>
<td style="text-align: left;"> − 0.55</td>
<td style="text-align: left;"> − 0.36</td>
<td style="text-align: left;"> − 0.54</td>
<td style="text-align: left;"> − 0.56</td>
<td style="text-align: left;"> − 0.39</td>
<td style="text-align: left;"> − 0.29</td>
<td style="text-align: left;"> − 0.35</td>
<td style="text-align: left;"> − 0.57</td>
<td style="text-align: left;"> − 0.59</td>
<td style="text-align: left;"> − 0.37</td>
<td style="text-align: left;"> − 0.38</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;"> − 0.51</td>
<td style="text-align: left;"> − 0.31</td>
<td style="text-align: left;"> − 0.52</td>
<td style="text-align: left;"> − 0.53</td>
<td style="text-align: left;"> − 0.34</td>
<td style="text-align: left;"> − 0.26</td>
<td style="text-align: left;"> − 0.31</td>
<td style="text-align: left;"> − 0.53</td>
<td style="text-align: left;"> − 0.52</td>
<td style="text-align: left;"> − 0.32</td>
<td style="text-align: left;"> − 0.32</td>
<td style="text-align: left;">1</td>
</tr>
</tbody>
</table>

All correlation coefficients are statistically significant (*p* \< 0.01)

MO, mobility; SC, self-care; UA, usual activity; PD, pain/discomfort AD, anxiety/depression; WA: washing self, DR: dressing self, PN: pain, DI: discomfort, AN: anxiety, DE: depression

</div>

## Author contributions

BMC was responsible for the original grant proposal, study design, instrument construction and online survey. MP, BMC, and FR developed the grant proposal for this secondary data analysis, developed the data analysis strategy, conducted the analysis, and drafted the manuscript.

## Funding

This study is funded by the EuroQol Research Foundation (464-RA\[original study\]; 1970-RA\[secondary analysis\]). We are also grateful to the Foundation for the travel grant for Minh Pham to attend the 5th EuroQol Early Career Researcher (ECR) Meeting 2025 and present this research at the 9th EuroQol Academy 2025.

## Data availability

Data will be made available upon reasonable request.

## Declarations

### Conflict of interest

Benjamin M. Craig and Fanni Rencz are members of the EuroQol Group and its Descriptive Systems Working Group (DSWG). Fanni Rencz is employed by the EuroQol Research Foundation. Views expressed by the authors in the publication do not necessarily reflect the views of the EuroQol Research Foundation or the DSWG .

## Footnotes

## References

## References

1. Kennedy-Martin, M., Slaap, B., Herdman, M., van Reenen, M., Kennedy-Martin, T., Greiner, W., et al. (2020). Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. European Journal of Health Economics,21, 1245–1257. doi:10.1007/s10198-020-01195-8

2. EuroQol—a new facility for the measurement of health-related quality of life. (1990). Health Policy. 16, 199–208. doi:10.1016/0168-8510(90)90421-9

3. Devlin, N. J., & Brooks, R. (2017). EQ-5D and the EuroQol group: Past, present and future. Applied Health Economics and Health Policy,15, 127–137. doi:10.1007/s40258-017-0310-5

4. Rencz, F., Gulácsi, L., Drummond, M., Golicki, D., Prevolnik Rupel, V., Simon, J., et al. (2016). EQ-5D in central and eastern Europe: 2000–2015. Quality of Life Research,25, 2693–2710. doi:10.1007/s11136-016-1375-6

5. Brooks, R. (1996). EuroQol: The current state of play. Health Policy,37, 53–72. doi:10.1016/0168-8510(96)00822-6

6. Herdman, M., Gudex, C., Lloyd, A., Janssen, M. F., Kind, P., Parkin, D., et al. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research,20, 1727–1736. doi:10.1007/s11136-011-9903-x

7. Whalley, D., Globe, G., Crawford, R., Doward, L., Tafesse, E., Brazier, J., et al. (2018). Is the EQ-5D fit for purpose in asthma? Acceptability and content validity from the patient perspective. Health and Quality of Life Outcomes,16, 160. doi:10.1186/s12955-018-0970-3

8. Lin, F.-J., Pickard, A. S., Krishnan, J. A., Joo, M. J., Au, D. H., Carson, S. S., et al. (2014). Measuring health-related quality of life in chronic obstructive pulmonary disease: Properties of the EQ-5D-5L and PROMIS-43 short form. BMC Medical Research Methodology,14, 78. doi:10.1186/1471-2288-14-78

9. Efthymiadou, O., Mossman, J., & Kanavos, P. (2019). Health related quality of life aspects not captured by EQ-5D-5L: Results from an international survey of patients. Health Policy (Amsterdam),123, 159–165. doi:10.1016/j.healthpol.2018.12.003

10. Matza, L. S., Boye, K. S., Stewart, K. D., Curtis, B. H., Reaney, M., & Landrian, A. S. (2015). A qualitative examination of the content validity of the EQ-5D-5L in patients with type 2 diabetes. Health and Quality of Life Outcomes,13, 192. doi:10.1186/s12955-015-0373-7

11. McDonald, R., Mullett, T. L., & Tsuchiya, A. (2020). Understanding the composite dimensions of the EQ-5D: An experimental approach. Social Science & Medicine,265, Article 113323. doi:10.1016/j.socscimed.2020.113323

12. Peasgood, T., Mukuria, C., Carlton, J., Connell, J., & Brazier, J. (2021). Criteria for item selection for a preference-based measure for use in economic evaluation. Quality of Life Research,30, 1425–1432. doi:10.1007/s11136-020-02718-9

13. Grant Levy, S. (2019). Deconstructing a double-barreled alternative: Evolution and creationism. Psychological Reports,122, 1995–2004. doi:10.1177/0033294118795145

14. Menold, N. (2020). Double barreled questions: An analysis of the similarity of elements and effects on measurement quality. Journal of Official Statistics,36, 855–886.

15. Tsuchiya, A., Bansback, N., Hole, A. R., & Mulhern, B. (2019). Manipulating the 5 dimensions of the EuroQol instrument: The effects on self-reporting actual health and valuing hypothetical health states. Medical Decision Making,39, 380–392. doi:10.1177/0272989X19851049

16. Rencz, F., & Janssen, M. F. (2022). Analyzing the pain/discomfort and anxiety/depression composite domains and the meaning of discomfort in the EQ-5D: A mixed-methods study. Value in Health,25, 2003–2016. doi:10.1016/j.jval.2022.06.012

17. Belay, Y. B., Mihalopoulos, C., Lee, Y. Y., Mulhern, B., & Engel, L. (2023). Examining the psychometric properties of a split version of the EQ-5D-5L anxiety/depression dimension in patients with anxiety and/or depression. Quality of Life Research,32, 2025–2036. doi:10.1007/s11136-023-03372-7

18. Feng, Y.-S., Kohlmann, T., Janssen, M. F., & Buchholz, I. (2021). Psychometric properties of the EQ-5D-5L: A systematic review of the literature. Quality of Life Research,30, 647–673. doi:10.1007/s11136-020-02688-y

19. Hinz, A., Kohlmann, T., Stöbel-Richter, Y., Zenger, M., & Brähler, E. (2014). The quality of life questionnaire EQ-5D-5L: Psychometric properties and normative values for the general German population. Quality of Life Research,23, 443–447. doi:10.1007/s11136-013-0498-2

20. Liu, X., Chan, W. W., Tang, E. H., Suen, A. H., Fung, M. M., Woo, Y. C., et al. (2023). Psychometric properties of EQ-5D-5L for use in patients with Graves’ disease. Health and Quality of Life Outcomes,21, 90. doi:10.1186/s12955-023-02177-z

21. Rencz, F., Brodszky, V., & Janssen, M. F. (2023). A direct comparison of the measurement properties of EQ-5D-5L, PROMIS-29+2 and PROMIS Global Health Instruments and EQ-5D-5L and PROPr utilities in a general population sample. Value in Health,26, 1045–1056. doi:10.1016/j.jval.2023.02.002

22. Konnopka, A., & Koenig, H.-H. (2017). The, “no problems”-problem: An empirical analysis of ceiling effects on the EQ-5D 5L. Quality of Life Research,26, 2079–2084. doi:10.1007/s11136-017-1551-3

23. Craig, B. M. (2025). Health valuation protocol for dual discrete choice experiment (dual-DCE) surveys to estimate the effects of different scenarios and attributes on main effects. 2025 [cited 2025 Mar 30]; Available from: https://bmjopen.bmj.com/content/15/2/e091097. doi:10.1136/bmjopen-2024-091097

24. R: The R Project for Statistical Computing [Internet]. [cited 2025 Jun 5]. Available from: https://www.r-project.org/

25. Wickham, H., François, R., Henry, L., Müller, K., Vaughan, D., Software, P., et al. (2023) dplyr: A Grammar of Data Manipulation [Internet]. [cited 2025 Jun 5]. Available from: https://cran.r-project.org/web/packages/dplyr/index.html

26. Oksanen, J., Simpson, G. L., Blanchet, F. G., Kindt, R., Legendre, P., Minchin, P. R., et al. (2025) vegan: Community Ecology Package [Internet]. [cited 2025 Jun 5]. Available from: https://cran.r-project.org/web/packages/vegan/index.html?utm_source=chatgpt.com

27. O’Connor, B. P. (2024) EFA.dimensions: Exploratory Factor Analysis Functions for Assessing Dimensionality [Internet]. [cited 2025 Jun 5]. Available from: https://cran.r-project.org/web/packages/EFA.dimensions/index.html

28. Revelle, W. (2025) psych: Procedures for Psychological, Psychometric, and Personality Research [Internet]. [cited 2025 Jun 5]. Available from: https://cran.r-project.org/web/packages/psych/index.html

29. Create Elegant Data Visualisations Using the Grammar of Graphics [Internet]. [cited 2025 Jun 5]. Available from: https://ggplot2.tidyverse.org/

30. Engel, L., Whitehurst, D. G. T., Haagsma, J., Janssen, M. F., & Mulhern, B. (2023). What is measured by the composite, single-item pain/discomfort dimension of the EQ-5D-5L? An exploratory analysis. Quality of Life Research,32, 1175–1186. doi:10.1007/s11136-022-03312-x

31. Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement,20, 37–46.

32. McHugh, M. L. (2012). Interrater reliability: The kappa statistic. Biochemia Medica,22, 276–282.

33. Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal,27, 379–423.

34. BasJanssen, M. F., Birnie, E., & Bonsel, G. J. (2007). Evaluating the discriminatory power of EQ-5D, HUI2 and HUI3 in a US general population survey using Shannon’s indices. Quality of Life Research,16, 895–904. doi:10.1007/s11136-006-9160-6

35. Cohen, J. (2013). Statistical power analysis for the behavioral sciences (2nd ed.). Routledge.

36. Brown, T. A. (2015). Confirmatory factor analysis for applied research (2nd ed.). Guilford Publications.

37. Kaiser, H. F. (1960). The application of electronic computers to factor analysis. Educational and Psychological Measurement,20, 141–151.

38. Costello, A. B., Osborne, J. Best practices in exploratory factor analysis: four recommendations for getting the most from your analysis. [cited 2025 May 29]; Available from: https://openpublishing.library.umass.edu/pare/article/id/1650/

39. Rencz, F., & Janssen, M. F. (2024). Testing the psychometric properties of 9 bolt-ons for the EQ-5D-5L in a general population sample. Value in Health,27, 943–954. doi:10.1016/j.jval.2024.03.2195

40. Balicki, P., Sołtysik, B. K., Borowiak, E., Kostka, T., & Kostka, J. (2025). Activities of daily living limitations in relation to the presence of pain in community-dwelling older adults. Scientific Reports,15, 15027. doi:10.1038/s41598-025-00241-w

41. Lay, K., Crocker, M., Engel, L., Ratcliffe, J., Charlton, S., & Hutchinson, C. (2023). How do older adults receiving aged care services understand and respond to the EQ-5D-5L? A think-aloud study in residential care. Quality of Life Research,32, 3161–3170. doi:10.1007/s11136-023-03466-2

42. Lopez, J., Perez-Rojo, G., Noriega, C., Sánchez-Cabaco, A., Sitges, E., & Bonete, B. (2024). Quality-of-life in older adults: Its association with emotional distress and psychological wellbeing. BMC Geriatrics,24, 815. doi:10.1186/s12877-024-05401-7

43. van Oppen, J. D., Conroy, S. P., Coats, T. J., Mackintosh, N. J., & Valderas, J. M. (2023). Measuring health-related quality of life of older people with frailty receiving acute care: Feasibility and psychometric performance of the EuroQol EQ-5D. BMC Emergency Medicine,23, 137. doi:10.1186/s12873-023-00909-4

44. Krawczyk-Suszek, M., & Kleinrok, A. (2022). Health-related quality of life (HRQoL) of people over 65 years of age. International Journal of Environmental Research and Public Health,19, 625. doi:10.3390/ijerph19020625

45. Yang, F., Jiang, S., He, X. N., Li, H. C., Wu, H. Y., Zhang, T. T., et al. (2020). Do rural residents in China understand EQ-5D-5L as intended? Evidence from a qualitative study. PharmacoEconomics. 10.1007/s41669-020-00212-z

46. Mai, V. Q., Sun, S., Minh, H. V., Luo, N., Giang, K. B., Lindholm, L., et al. (2020). An EQ-5D-5L value set for Vietnam. Quality of Life Research,29, 1923–1933. doi:10.1007/s11136-020-02469-7

47. Bethlehem, J. (2010). Selection bias in web surveys. International Statistical Review,78, 161–188.

## Associated Data

### Data Availability Statement

Data will be made available upon reasonable request.

---
project_id: "2015200"
work_id: "doi:10.1371/journal.pone.0290606"
doi: "10.1371/journal.pone.0290606"
pmid: "37624857"
pmcid: "PMC10456181"
title: "Exploring differences and similarities of EQ-5D-3L, EQ-5D-5L and WHOQOL-OLD in recipients of aged care services in Germany"
journal: "PLOS ONE"
publication_date: "2023-08-25"
volume: "18"
issue: "8"
authors:
  - name: "Ole Marten"
    affiliation_ids:
      - "aff001"
  - name: "Wolfgang Greiner"
    affiliation_ids:
      - "aff001"
affiliations:
  - id: "aff001"
    name: "Department of Health Economics and Health Care Management, Bielefeld University, Bielefeld, North Rhine-Westphalia, Germany"
  - id: "edit1"
    name: "University of Bamberg, GERMANY"
licence: "cc-by"
source_file: "input/projects/2015200/papers/doi_10.1371_journal.pone.0290606.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10456181/fullTextXML"
source_method: "epmc_xml"
source_sha256: "5b8e0aaef87898c3ff7a339dde9ebe4db327ba0b49f063b856b2fb8b4ba785dc"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Exploring differences and similarities of EQ-5D-3L, EQ-5D-5L and WHOQOL-OLD in recipients of aged care services in Germany

## Abstract

European countries more than ever face shifts towards aging societies with accompanying challenges for health and aged care services. Economic evaluation has mainly relied on health measures such as EQ-5D across populations and conditions. We want to know how well the EQ-5D performs in the target population to avoid bias to the disadvantage of older adults and care-dependents. Therefore, we aim to explore differences and similarities of EQ-5D-3L and EQ-5D-5L in comparison to the old-age specific WHOQOL-OLD instrument in a sample of older adults receiving aged care services. We collected data from n = 329 older adults (≥65 years) receiving aged care services in Germany; the majority was at least 80 years and had varying care needs. We assessed instruments’ feasibility, test-retest reliability, instruments’ association and sensitivity to known-group differences. In terms of feasibility and test-retest reliability both EQ-5D versions performed better than the WHOQOL-OLD. All measures differentiated well between groups based on aspects of general health and care levels. The analysis of relationship between measures indicated that EQ-5D and WHOQOL-OLD assess partially overlapping, but distinct constructs. We found no clear evidence of superiority of either EQ-5D version over the other. The EQ-5D-5L performed better in terms of test-retest reliability and stronger correlations with WHOQOL-OLD facets. We conclude that using the WHOQOL-OLD alongside EQ-5D in this sample added further information on different aspects of quality of life.

## Data Availability

All relevant data are within the paper and <a href="#sec015" data-ref-type="sec">Supporting Information</a> files.

## Introduction

European countries experienced a major increase in life expectancy over the past decades. Recent projections for the countries of the European Union indicate that the share of older people, i.e. those being 65 years and above, is further going to increase from ~21% in 2021 up to 31.3% in 2100. Similarly, the proportion of those aged 80 and over is also expected to increase from 6% to 14.6% during that time \[1\]. Moreover, the association between aging and diminished health and even multimorbidity is well documented \[2, 3\] and corresponds to higher health and aged care service utilisation in older adults in comparison to the younger general population \[2, 4, 5\].

Aged care involves a set of services addressing a person’s health and care needs, which arise as a consequence of reduced functional capacity \[6\]. These services can be either provided at home, where recipients stay in their familiar living environment, or in institutions such as nursing homes. On the other hand, aged care services may be provided by formal caregivers, who usually have a professional training and provide paid care services, whereas informal care refers to unpaid care provided by people in close contact to the dependent (e.g. partners, children or relatives) \[7, 8\]. In simple terms, aged care services can be characterised based on where and by whom these services are provided.

In 2021 around 4.96 million people in Germany were dependent on care with 84% being cared for at home. Overall, slightly more than 50% of care dependents exclusively received informal care through relatives and one fifth received a combination of formal and informal care services at home. On the other hand, in 2021 around 16% of care dependents in Germany were living in nursing homes \[9\]. Due to the great number of older adults and in the perspective of continuously increasing demand for aged care services many complex interventions are being developed to address the needs of older adults. In this population, where interventions may operate at the intersection of health and aged care, the outcomes may well go beyond health. In this regard, the outcome of care may not be restored health or functional ability, but rather improved quality of life (QoL) by helping recipients to participate in activities of daily living or social interaction \[10\]. While health care and aged care may be related sectors, budgets are strictly separated. Especially with finite resources the accurate measurement of outcomes is of significant importance, since this information is crucial for effective decision-making based on economic evaluation for either sector.

So far, economic evaluation has mainly relied on generic measures of health—such as EQ-5D (hereafter, used to refer to both the EQ-5D-3L and EQ-5D-5L)—as the preferred outcome measure, where this is to ensure comparability of outcome measurement across conditions and all adult age groups. However, if conditions or interventions affect outcomes other than health or if benefits accrue in more than one sector measures of health may be limited in their capacity to fully grasp the important outcomes \[11\]. The EQ-5D appears to be frequently used in economic evaluation of interventions addressing older adults \[12, 13\] as well as in aged care settings \[8, 14\]. In this instance the outcome assessment could be supplemented with an old-age-specific measure of QoL, which can contribute additional profile information. Old-age-specific measures are developed with older people considering what aspects are important to them, where the WHOQOL-OLD is one of the more prominent instruments in this field \[15, 16\]. With the EQ-5D being a keystone measure for a variety of different populations, but also in older adults and those being dependent on care, we want to know how well the EQ-5D performs in the target population to avoid bias to the disadvantage of older adults and care-dependents. Gottschalk et al. \[17\] systematically reviewed EQ-5D measurement properties in samples of older adults with an average age ≥75 years and update the work of Haywood and colleagues \[18\]. Even though the EQ-5D-5L has been around for quite some time \[19\], the evidence on its measurement properties in older adults is relatively scarce; especially with regard to the assessment of the instrument’s reliability \[17, 20\]. Furthermore, we are unaware of further studies assessing the relationship of either the EQ-5D-3L or EQ-5D-5L with the old-age specific QoL instrument WHOQOL-OLD in German recipients of aged care services.

The EQ-5D and WHOQOL-OLD are not measuring identical but overlapping constructs, however, if both measures are designed or regularly applied to evaluate interventions for older people and aged care services, then we want to know how well they perform in this context. Therefore, this paper aimed to understand the differences and similarities between EQ-5D-3L, EQ-5D-5L and the old-age specific WHOQOL-OLD instrument in a sample of older adults receiving aged care services by investigating sensitivity to known-group differences and test-retest reliability of the measures as well as by exploring the relationship of the EQ-5D with the WHOQOL-OLD.

## Methods

### Sampling procedure

For this study, we used a convenience sampling approach to recruit respondents. In order to invite participants to the survey, we applied a two-staged contacting procedure. In the first stage, we approached social care providers, e.g. nursing homes, ambulatory care services or adult day-care centres, in the cities of Bielefeld (North Rhine-Westphalia) and Schwerin (Mecklenburg-western Pomerania) as well as their surrounding areas to invite institutions to cooperate in this study. Only in the second stage, potential participants from cooperating institutions were invited to participate in this survey between September 2019 and March 2020. However, respondents were exclusively contacted by their respective care facility to assess their willingness to participate in this study to minimise external and unfamiliar contacts for this potentially vulnerable group.

Participants eligible for this study were i) at least 65 years and ii) in need of aged care services; that involves services that address an individual’s health or personal care needs and that is either given by family members or friends or in a professionalised setting by health and social care workers \[21\]. Inclusion into the study was based on respondents’ self-reports; no official records were reviewed. The collected data is anonymous and, hence, no formal written consent was required. Ethics approval under the number 2017–207 was obtained from the Research Ethics Committee at Bielefeld University.

### Survey design and instruments

The survey consisted of two different EQ-5D versions, the WHOQOL-OLD as well as a sociodemographic questionnaire. The EQ-5D-3L (3L) is a generic preference-based measure of health-related quality of life comprising two parts. The first is the descriptive system made up of five dimensions: mobility, self-care, usual activities, pain or discomfort and anxiety or depression. Each of the dimensions can be described by one of three severity levels ranging from no problems to extreme problems. The 3L can describe 243 unique health states \[22\]. The EQ-5D-5L (5L) is a later version of the instrument comprising the same five dimensions. However, in this variant the number of response options was increased to five severity levels representing no, slight, moderate, severe or extreme problems. Thus, the descriptive system differentiates 3125 individual health states \[19\]. The second component of both the 3L and 5L is the EQ VAS. Respondents are asked to indicate their subjective overall health on this vertical scale, which uses ‘the worst health you can imagine’ and the ‘the best health you can imagine’ as reference points to the scale \[23\].

The WHOQOL-OLD is an old age-specific measure of quality of life intend for use in adults being 60 years or older. The measure was developed by the WHOQOL group with the aim to generate a measure that is psychometrically sound with older adults and, secondly, covers dimensions that are of importance to older respondents. The WHOQOL-OLD has 24 items that are equally distributed across six facets: sensory abilities; autonomy; past, present and future activities; social participation; death and dying; and intimacy \[15\]. Each facet can be scored and transformed onto a scale ranging from 0 to 100 allowing the calculation of a profile of scores. In addition, a total score can be computed by averaging across the scores of the six sub-scales. This study uses the German version of the WHOQOL-OLD, which has been shown to be psychometrically valid in the German older population \[16\].

For the sociodemographic questionnaire, respondents were asked to self-report their gender, age group, educational level, marital status and care setting as well as care level. Care levels were categorised in accordance with the German statutory long-term care insurance \[24, 25\], where five care levels facilitate the classification of the type and severity of impairments with independence or ability, irrespective of whether these are physical, mental or psychological. To determine the independence of a person needing care, they will be evaluated in the following six modules: “mobility”, “mental and communication-related abilities”, “behaviour and psychological issues”, “self-care”, “independent handling of requirements and challenge associated with illness or therapy–and their management” and “everyday life and social contacts”. Depending on the degree of impairments, they will be assigned to one of five care levels labelled as ‘minor’, ‘considerable’, ‘serious’, severe’ or ‘most severe’ impairments of independence or ability; the assigned care level consequently affects the amount of benefits people in need of care can receive from the statutory long-term care insurance \[26\]. Further, participants answered a single-item general health status question on a five-point scale (very good, good, moderate, bad, very bad). Lastly, respondents indicated whether they needed help answering the survey and what kind of help they needed.

For each respondent, two surveys were performed, where the second survey was required to assess the test-retest reliability of the WHOQOL-OLD and both EQ-5D versions. Since both the 3L and 5L include an identical visual analogue scale (EQ VAS), we included this component only once. Respondents first answered a version of the EQ-5D including the EQ VAS followed by the WHQOOL-OLD and then continued with the second versions of the EQ-5D. The survey finished with the sociodemographic questionnaire. The presentation order of the EQ-5D versions was varied, so that half of the sample answered the 3L first and then the 5L (after they had finished the WHOQOL-OLD) or vice versa. For the second survey, the sociodemographic questionnaire was dropped to minimise respondent burden.

Cooperating institutions were provided with a bespoke number of survey packages. Each package included an information sheet, the paper-based survey as well as stamped and addressed return envelopes. To assess test-retest reliability of the survey components, the second survey was also included in the survey package, where both the initial and retest survey were marked with a matching four-digit identification number. The retest interval was set to 14 days, assuming that the interval would be short enough so that the health status would be fairly constant, but just long enough to minimise the risk that survey participants recall the questions and their answers \[27\]. Generally, each of the included instruments was designed as a self-complete measure and applied as such. However, if respondents required help with the survey, they could be assisted.

### Data analysis

The health and QoL information as generated by the 3L, 5L and the WHOQOL-OLD was collected as self-reported data from each participant individually. We derived the interval-scaled summary scores for each respondent and for each instrument using the recommended scoring technique. The European VAS tariff by Greiner et al. \[28\] was used to calculate the 3L index values, whereas for the 5L variant we applied the tariff by Ludwig et al. \[29\] to generate the index. To generate the WHOQOL-OLD facet scores and the total score, we used the recommended procedure by Conrad et al. \[30\].

Feasibility of the included measures was analysed in terms of missing values for the descriptive system for the 3L, 5L and WHOQOL-OLD as well as for the EQ VAS; additionally, we summarise problems that occurred with the EQ VAS. We examine completion rates for all measures based on their summary score. Further, we analysed the amount of time respondents needed to complete the survey as well as the extent and type of aid they required.

Test-retest reliability of interval-scale data, i.e. 3L and 5L indices, EQ VAS score, WHOQOL-OLD facets’ and total scores, were determined using intraclass correlation coefficients (ICCs). In accordance with Koo and Li \[31\], we used two-way mixed effects models specifying the absolute agreement option. Recommended threshold values for ICCs to categorise reliability are \<0.5, 0.5–0.75, 0.75–0.9 and \>0.9 representing poor, moderate, good or excellent reliability \[31\]. The intra-rater reliability of categorical variables, i.e. the EQ-5D descriptive system and individual WHOQOL-OLD items, was assessed using Cohen’s weighted kappa. Landis and Koch \[32\] suggest the following cut-off points for the kappa values: agreement is classified as slight for values below 0.2, 0.21–0.4 as fair, 0.41–0.6 moderate, 0.61–0.8 substantial and as almost perfect for values above 0.8. Respondents were eligible for the retest analysis, if they indicated no change in their health status, i.e. respondents answered the general health status questions in the initial assessment and at follow-up with the same category \[27\].

Evidence suggests that health significantly contributes to older adults’ conceptualisation of QoL \[33, 34\]. In the absence of a ‘gold standard’ for the assessment of QoL in older adults, we evaluated the relationship between EQ-5D and WHOQOL-OLD by correlating EQ-5D dimensions, indices and EQ VAS with the WHOQOL-OLD total score and facet scores. Relationship of the constructs was expressed either as a Pearson correlation coefficient (interval data) or as a Spearman correlation coefficient (ordinal data). According to the guidelines proposed by Cohen \[35\] correlations below 0.3 were considered as poor, between 0.3 and below 0.5 as moderate and above 0.5 as strong. Since generic health status as assessed by EQ-5D and old-age specific QoL as measured by WHOQOL-OLD are related constructs, we assumed that EQ-5D indices and the WHOQOL-OLD total score demonstrate a positive, moderate and significant correlation. We expected moderate and significant correlations between the EQ-5D physical dimensions mobility, self-care and usual activities and the WHOQOL-OLD facets autonomy, social participation and past, present and future activities. Similarly, we expected a moderate and significant correlation between anxiety or depression and death and dying. However, for the other EQ-5D dimensions we expected poor correlations between death and dying, intimacy or sensory abilities.

Further, we examined sensitivity to known-group differences in EQ-5D index scores (3L and 5L), EQ VAS, WHOQOL-OLD facet scores and total score by subgroups based on gender, educational level, care level and general health status using analysis of variance (ANOVA) and t-test. For the two group comparison we report Cohen’s d as an effect size measure, whereas for more than two groups we report eta squared. Cohen’s d was interpreted to the thresholds: small (0.2–0.49), medium (0.5–0.79) and large (\>0.79). Whereas thresholds for eta squared after ANOVA were categorised as small (0.01–0.059), medium (0.06–0.139) and large (\>0.139) \[35\]. We hypothesised that being male, lower education, a higher care level and a lower general health status would result in lower health or QoL scores. For all analyses we use STATA 17 \[36\].

## Results

### Sample characteristics

Questionnaires were sent to 800 persons with the help of 43 cooperation institutions. In summary, 334 persons returned the survey. Of these, five respondents were younger than 65 years and, hence, were excluded.

<a href="#pone.0290606.t001" data-ref-type="table">Table 1</a> provides an overview over the sample characteristics. The initial questionnaire was available from 329 eligible respondents, whereas information from the retest survey was provided from 266 respondents (81%). However, the eligible retest analysis sample consists of 168 respondents who indicated no change on the health transition question. The sample was predominantly female and more than 65% were older than 80 years. No respondent was above 100 years. One fifth of the respondents indicated to have no officially assigned care level. Moreover, respondents with high intensity care needs—as represented by care levels 4 and 5—only accounted for 10.9% of the sample. About 60% of the sample received long-term care and support in a home-based setting, i.e. respondents were living in their homes receiving care from their family/relatives, an ambulatory care service or visited an adult day-care centre. The remaining respondents were either living in a nursing home or did not provide this information. Further, the information on the care setting was recoded to represent subgroups that received only formal or informal care. In total, 80 survey respondents were living at home receiving care only from unpaid family members or relatives, whereas 123 respondents were living in a nursing home receiving care from professional health and social care workers. The distinction in the care setting between ‘where’ and by ‘whom’ people receive care was necessary, as we observed a high degree of mixed care arrangements including both formal and informal care components.

<div id="pone.0290606.t001" class="table-wrap">

10.1371/journal.pone.0290606.t001

<div class="caption">

###### Summary of sample characteristics.

</div>

<img src="pone.0290606.t001.jpg" id="pone.0290606.t001g" />

<table>
<thead>
<tr>
<th colspan="2" rowspan="2" style="text-align: left;">Characteristics</th>
<th colspan="2" style="text-align: center;">Sample (test)</th>
<th colspan="2" style="text-align: center;">Retest sample</th>
</tr>
<tr>
<th style="text-align: center;">N</th>
<th style="text-align: center;">%</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">%</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3" style="text-align: left;"><strong>Gender</strong></td>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">215</td>
<td style="text-align: center;">65.4%</td>
<td style="text-align: center;">105</td>
<td style="text-align: center;">62.5%</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">98</td>
<td style="text-align: center;">29.8%</td>
<td style="text-align: center;">57</td>
<td style="text-align: center;">33.9%</td>
</tr>
<tr>
<td style="text-align: left;">missing</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">4.9%</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">3.6%</td>
</tr>
<tr>
<td rowspan="8" style="text-align: left;"><strong>Age group</strong></td>
<td style="text-align: left;">65–70 years</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">8.2%</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">9.5%</td>
</tr>
<tr>
<td style="text-align: left;">71–75 years</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">6.4%</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">7.7%</td>
</tr>
<tr>
<td style="text-align: left;">76–80 years</td>
<td style="text-align: center;">62</td>
<td style="text-align: center;">18.8%</td>
<td style="text-align: center;">35</td>
<td style="text-align: center;">20.8%</td>
</tr>
<tr>
<td style="text-align: left;">81–85 years</td>
<td style="text-align: center;">78</td>
<td style="text-align: center;">23.7%</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">24.4%</td>
</tr>
<tr>
<td style="text-align: left;">86–90 years</td>
<td style="text-align: center;">88</td>
<td style="text-align: center;">26.8%</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">23.8%</td>
</tr>
<tr>
<td style="text-align: left;">91–95 years</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">12.2%</td>
<td style="text-align: center;">18</td>
<td style="text-align: center;">10.7%</td>
</tr>
<tr>
<td style="text-align: left;">96–100 years</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">2.7%</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2.4%</td>
</tr>
<tr>
<td style="text-align: left;">missing</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1.2%</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0.6%</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;"><strong>Marital status</strong></td>
<td style="text-align: left;">Single</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">6.7%</td>
<td style="text-align: center;">11</td>
<td style="text-align: center;">6.6%</td>
</tr>
<tr>
<td style="text-align: left;">Married/partnership</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">30.4%</td>
<td style="text-align: center;">58</td>
<td style="text-align: center;">34.5%</td>
</tr>
<tr>
<td style="text-align: left;">Widowed</td>
<td style="text-align: center;">176</td>
<td style="text-align: center;">53.5%</td>
<td style="text-align: center;">85</td>
<td style="text-align: center;">50.6%</td>
</tr>
<tr>
<td style="text-align: left;">Divorced/separated</td>
<td style="text-align: center;">24</td>
<td style="text-align: center;">7.2%</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">6.0%</td>
</tr>
<tr>
<td style="text-align: left;">missing</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">2.3%</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2.4%</td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Educational level</strong></td>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">183</td>
<td style="text-align: center;">55.6%</td>
<td style="text-align: center;">96</td>
<td style="text-align: center;">57.1%</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">77</td>
<td style="text-align: center;">23.4%</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">23.8%</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">62</td>
<td style="text-align: center;">18.8%</td>
<td style="text-align: center;">30</td>
<td style="text-align: center;">17.9%</td>
</tr>
<tr>
<td style="text-align: left;">missing</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">2.1%</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1.2%</td>
</tr>
<tr>
<td rowspan="7" style="text-align: left;"><strong>Care level</strong></td>
<td style="text-align: left;">0</td>
<td style="text-align: center;">61</td>
<td style="text-align: center;">18.5%</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">20.2%</td>
</tr>
<tr>
<td style="text-align: left;">1</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">6.7%</td>
<td style="text-align: center;">15</td>
<td style="text-align: center;">8.9%</td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: center;">99</td>
<td style="text-align: center;">30.1%</td>
<td style="text-align: center;">51</td>
<td style="text-align: center;">30.4%</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: center;">90</td>
<td style="text-align: center;">27.4%</td>
<td style="text-align: center;">45</td>
<td style="text-align: center;">26.8%</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">8.8%</td>
<td style="text-align: center;">14</td>
<td style="text-align: center;">8.3%</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">2.1%</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">1.8%</td>
</tr>
<tr>
<td style="text-align: left;">missing</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">6.4%</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">3.6%</td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Care setting</strong></td>
<td style="text-align: left;">Home based</td>
<td style="text-align: center;">196</td>
<td style="text-align: center;">61.4%</td>
<td style="text-align: center;">111</td>
<td style="text-align: center;">67.3%</td>
</tr>
<tr>
<td style="text-align: left;">Nursing home</td>
<td style="text-align: center;">123</td>
<td style="text-align: center;">38.6%</td>
<td style="text-align: center;">54</td>
<td style="text-align: center;">32.7%</td>
</tr>
<tr>
<td style="text-align: left;">Formal care</td>
<td style="text-align: center;">123</td>
<td style="text-align: center;">60.6%</td>
<td style="text-align: center;">54</td>
<td style="text-align: center;">51.9%</td>
</tr>
<tr>
<td style="text-align: left;">Informal care</td>
<td style="text-align: center;">80</td>
<td style="text-align: center;">39.4%</td>
<td style="text-align: center;">50</td>
<td style="text-align: center;">48.1%</td>
</tr>
</tbody>
</table>

</div>

### Feasibility

As <a href="#pone.0290606.t002" data-ref-type="table">Table 2</a> indicates, the observed share of missing values for all EQ-5D dimensions was well below 4%. The proportion of missing responses on the WHOQOL-OLD items were mostly below 5%; except for item 12 (‘Satisfied with opportunities to continue archiving’), which was missing in 5.8% of respondents. Completion rates for all instruments were fairly high; the index score could be calculated in 94.2%, 96.4% and 97.2% of the cases for the 5L, 3L and the WHOQOL-OLD total score, respectively. Problems with answering the EQ VAS were prevalent for 31% of respondents. In 25.5% of all EQ VAS responses the required mark on the scale was not placed, while just 2.7% of the responses were missing. Other problems such as reporting a range, mismatching values in the box and on the scale account for the remaining 3%.

<div id="pone.0290606.t002" class="table-wrap">

10.1371/journal.pone.0290606.t002

<div class="caption">

###### Proportion of missing values per dimension/item for the EQ-5D-5L, EQ-5D-3L and WHOQOL-OLD.

</div>

<img src="pone.0290606.t002.jpg" id="pone.0290606.t002g" />

<table>
<tbody>
<tr>
<td colspan="3" style="text-align: left;"><strong>EQ-5D-5L</strong></td>
<td style="text-align: center;"><strong>Missing</strong></td>
<td colspan="3" style="text-align: left;"><strong>EQ-5D-3L</strong></td>
<td style="text-align: center;"><strong>Missing</strong></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><strong>Mobility</strong></td>
<td style="text-align: center;">2.1%</td>
<td colspan="3" style="text-align: left;">Mobility</td>
<td style="text-align: center;">2.1%</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><strong>Self-care</strong></td>
<td style="text-align: center;">3.0%</td>
<td colspan="3" style="text-align: left;">Self-care</td>
<td style="text-align: center;">1.8%</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><strong>Usual activities</strong></td>
<td style="text-align: center;">3.7%</td>
<td colspan="3" style="text-align: left;">Usual activities</td>
<td style="text-align: center;">2.1%</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><strong>Pain/ Discomfort</strong></td>
<td style="text-align: center;">2.7%</td>
<td colspan="3" style="text-align: left;">Pain/ Discomfort</td>
<td style="text-align: center;">1.2%</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><strong>Anxiety/ Depression</strong></td>
<td style="text-align: center;">3.3%</td>
<td colspan="3" style="text-align: left;">Anxiety/ Depression</td>
<td style="text-align: center;">1.5%</td>
</tr>
<tr>
<td style="text-align: left;"><strong>WHOQOL-OLD facet</strong></td>
<td style="text-align: left;">Item number</td>
<td style="text-align: left;">Item text</td>
<td style="text-align: center;"><strong>Missing</strong></td>
<td style="text-align: left;"><strong>WHOQOL-OLD facet</strong></td>
<td style="text-align: left;">Item number</td>
<td style="text-align: left;">Item text</td>
<td style="text-align: center;"><strong>Missing</strong></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Sensory Abilities</strong></td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">Impairments to senses affect daily life</td>
<td style="text-align: center;">1.8%</td>
<td rowspan="4" style="text-align: left;"><strong>Social Participation</strong></td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">Have enough to do each day</td>
<td style="text-align: center;">3.0%</td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;">Loss of sensory abilities affect participation in activities</td>
<td style="text-align: center;">2.4%</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">Satisfied with the way you use your time</td>
<td style="text-align: center;">3.3%</td>
</tr>
<tr>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Problems with sensory functioning affect ability to interact</td>
<td style="text-align: center;">1.5%</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">Satisfied with level of activity</td>
<td style="text-align: center;">3.0%</td>
</tr>
<tr>
<td style="text-align: left;">20</td>
<td style="text-align: left;">Rate sensory functioning</td>
<td style="text-align: center;">2.1%</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">Satisfied with opportunity to participate in community</td>
<td style="text-align: center;">2.4%</td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Autonomy</strong></td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">Freedom to make own decisions</td>
<td style="text-align: center;">2.1%</td>
<td rowspan="4" style="text-align: left;"><strong>Death and dying</strong></td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Concerned about the way you will die</td>
<td style="text-align: center;">3.7%</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">Feel in control of your future</td>
<td style="text-align: center;">3.7%</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">Afraid of not being able to control death</td>
<td style="text-align: center;">3.3%</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: left;">People around you are respectful of your freedom</td>
<td style="text-align: center;">4.3%</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">Scared of dying</td>
<td style="text-align: center;">3.3%</td>
</tr>
<tr>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Able to do things you’d like to</td>
<td style="text-align: center;">2.1%</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">Fear pain before death</td>
<td style="text-align: center;">3.3%</td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Past, present and future activities</strong></td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">Satisfied with opportunities to continue archiving</td>
<td style="text-align: center;">5.8%</td>
<td rowspan="4" style="text-align: left;"><strong>Intimacy</strong></td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">Feel a sense of companionship in life</td>
<td style="text-align: center;">3.3%</td>
</tr>
<tr>
<td style="text-align: left;">13</td>
<td style="text-align: left;">Received the recognition you deserve in life</td>
<td style="text-align: center;">3.7%</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">Experience love in life</td>
<td style="text-align: center;">3.7%</td>
</tr>
<tr>
<td style="text-align: left;">15</td>
<td style="text-align: left;">Satisfied with what you’ve achieved in life</td>
<td style="text-align: center;">2.1%</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">Opportunities to love</td>
<td style="text-align: center;">2.4%</td>
</tr>
<tr>
<td style="text-align: left;">19</td>
<td style="text-align: left;">Happy with things to look forward to</td>
<td style="text-align: center;">3.0%</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">Opportunities to be loved</td>
<td style="text-align: center;">4.0%</td>
</tr>
</tbody>
</table>

</div>

In total, 298 respondents reported a valid completion time for the survey; this was calculated as the difference between reported start and end times. The average time to complete the survey was 28.4 minutes with a range of 5 to 165 minutes. The mean completion time of those completing the survey without help did not differ from those who required help. We were not able to calculate separate times for the completion of individual parts, e.g. for the 5L, as only the total time was available.

Over half of the respondents (59%; n = 194) indicated that they required help completing the survey. Of those, 81% needed help from someone reading the questions to them and 79.4% had the responses filled in for them. Cross-tabulation of these two aid types showed that 77.2% (n = 139 out of 180) needed assistance with both. Further, 8.8% reported to need help with translations. However, it remains unclear, if translations were required into a foreign language or, if this was meant in terms of age-adequate language.

### Test-retest reliability

Of those who a returned retest survey, only 64.9% (n = 168) were eligible for the retest analysis, i.e. those indicating no change in health status as assessed by the general health status question. The average time interval between both measurements was 17 days (median 14 days) with a minimum of 7 days and a maximum of 75 days for the retest sample. There was no significant difference in the mean interval between test and retest between respondents who were eligible for the retest analysis and those who were not included in the analysis.

Agreement as measured by Cohen’s weighted kappa was substantial for all 3L dimensions except for usual activities, which can be rated moderate (see <a href="#pone.0290606.t003" data-ref-type="table">Table 3</a>). In case of the 5L, reliability was rated as substantial for all dimensions. Overall, reliability of the 5L was similar or better than that of the 3L with the exception of mobility, where the weighted kappa was slightly lower. The agreement of the interval-scaled EQ-5D indices can be categorised as good for the 3L (0.86) and excellent in the case of the 5L (0.91) as assessed by ICCs. Reliability of responses was lower for the EQ VAS, but still moderate.

<div id="pone.0290606.t003" class="table-wrap">

10.1371/journal.pone.0290606.t003

<div class="caption">

###### Test-retest reliability of the EQ-5D-3L and EQ-5D-5L.

</div>

<img src="pone.0290606.t003.jpg" id="pone.0290606.t003g" />

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Dimension</th>
<th style="text-align: left;">EQ-5D-3L</th>
<th style="text-align: left;">EQ-5D-5L</th>
</tr>
<tr>
<th style="text-align: left;">Weighted Kappa</th>
<th style="text-align: left;">Weighted Kappa</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Mobility</strong></td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;">0.73</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Self-care</strong></td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.75</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Usual activities</strong></td>
<td style="text-align: left;">0.59</td>
<td style="text-align: left;">0.65</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Pain/discomfort</strong></td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.65</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Anxiety/depression</strong></td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.63</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><strong>Intraclass correlation coefficient</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>EQ-5D index</strong></td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.91</td>
</tr>
<tr>
<td style="text-align: left;"><strong>EQ VAS</strong></td>
<td colspan="2" style="text-align: left;">0.70</td>
</tr>
</tbody>
</table>

</div>

Weighted kappa values for WHOQOL-OLD items were generally lower than those of both EQ-5D versions. These ranged from 0.39–0.65 suggesting fair to substantial agreement. It appears that agreement of items in the autonomy and past, present and future activities facets are consistently lower than others. ICCs of facet scores resemble this pattern; while agreement on these two facets is moderate, it is considered good on the other four facets. Similarly, the ICC on the WHOQOL-OLD total score is 0.83, thus also being considered good (see <a href="#pone.0290606.t004" data-ref-type="table">Table 4</a>).

<div id="pone.0290606.t004" class="table-wrap">

10.1371/journal.pone.0290606.t004

<div class="caption">

###### Test-retest reliability of WHOQOL-OLD items, facets and total score.

</div>

<img src="pone.0290606.t004.jpg" id="pone.0290606.t004g" />

<table>
<thead>
<tr>
<th style="text-align: left;">WHOQOL-OLD facet</th>
<th style="text-align: left;">Item number</th>
<th style="text-align: left;">Item text</th>
<th style="text-align: center;">Weighted kappa</th>
<th style="text-align: left;">WHOQOL-OLD facet</th>
<th style="text-align: left;">Item number</th>
<th style="text-align: left;">Item text</th>
<th style="text-align: center;">Weighted kappa</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Sensory Abilities</strong></td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">Impairments to senses affect daily life</td>
<td style="text-align: center;">0.58</td>
<td rowspan="4" style="text-align: left;"><strong>Social Participation</strong></td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">Have enough to do each day</td>
<td style="text-align: center;">0.62</td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;">Loss of sensory abilities affect participation in activities</td>
<td style="text-align: center;">0.59</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">Satisfied with the way you use your time</td>
<td style="text-align: center;">0.57</td>
</tr>
<tr>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Problems with sensory functioning affect ability to interact</td>
<td style="text-align: center;">0.56</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">Satisfied with level of activity</td>
<td style="text-align: center;">0.51</td>
</tr>
<tr>
<td style="text-align: left;">20</td>
<td style="text-align: left;">Rate sensory functioning</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">Satisfied with opportunity to participate in community</td>
<td style="text-align: center;">0.50</td>
</tr>
<tr>
<td style="text-align: center;"><strong>ICC</strong></td>
<td colspan="3" style="text-align: center;"><strong>0.79</strong></td>
<td style="text-align: center;"><strong>ICC</strong></td>
<td colspan="3" style="text-align: center;"><strong>0.77</strong></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Autonomy</strong></td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">Freedom to make own decisions</td>
<td style="text-align: center;">0.48</td>
<td rowspan="4" style="text-align: left;"><strong>Death and dying</strong></td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Concerned about the way you will die</td>
<td style="text-align: center;">0.64</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">Feel in control of your future</td>
<td style="text-align: center;">0.41</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">Afraid of not being able to control death</td>
<td style="text-align: center;">0.57</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: left;">People around you are respectful of your freedom</td>
<td style="text-align: center;">0.39</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">Scared of dying</td>
<td style="text-align: center;">0.63</td>
</tr>
<tr>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Able to do things you’d like to</td>
<td style="text-align: center;">0.43</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">Fear pain before death</td>
<td style="text-align: center;">0.65</td>
</tr>
<tr>
<td style="text-align: center;"><strong>ICC</strong></td>
<td colspan="3" style="text-align: center;"><strong>0.57</strong></td>
<td style="text-align: center;"><strong>ICC</strong></td>
<td colspan="3" style="text-align: center;"><strong>0.78</strong></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Past, present and future activities</strong></td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">Satisfied with opportunities to continue archiving</td>
<td style="text-align: center;">0.46</td>
<td rowspan="4" style="text-align: left;"><strong>Intimacy</strong></td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">Feel a sense of companionship in life</td>
<td style="text-align: center;">0.52</td>
</tr>
<tr>
<td style="text-align: left;">13</td>
<td style="text-align: left;">Received the recognition you deserve in life</td>
<td style="text-align: center;">0.44</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">Experience love in life</td>
<td style="text-align: center;">0.62</td>
</tr>
<tr>
<td style="text-align: left;">15</td>
<td style="text-align: left;">Satisfied with what you’ve achieved in life</td>
<td style="text-align: center;">0.49</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">Opportunities to love</td>
<td style="text-align: center;">0.54</td>
</tr>
<tr>
<td style="text-align: left;">19</td>
<td style="text-align: left;">Happy with things to look forward to</td>
<td style="text-align: center;">0.39</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">Opportunities to be loved</td>
<td style="text-align: center;">0.57</td>
</tr>
<tr>
<td style="text-align: center;"><strong>ICC</strong></td>
<td colspan="3" style="text-align: center;"><strong>0.59</strong></td>
<td style="text-align: center;"><strong>ICC</strong></td>
<td colspan="3" style="text-align: center;"><strong>0.79</strong></td>
</tr>
<tr>
<td colspan="8" style="text-align: center;"><strong>ICC Total score 0.83</strong></td>
</tr>
</tbody>
</table>

</div>

### Relationship between EQ-5D and WHOQOL-OLD

The Spearman correlation coefficients between comparable dimensions and facets (EQ-5D Mobility, Self-care, Usual activities and WHOQOL-OLD facets autonomy, past, present and future activities and social participation) showed significant and mostly moderate correlations. The pain or discomfort and anxiety or depression dimensions showed significant but weak correlation with the WHOQOL-OLD facets. Similarly, the facets intimacy (not significant), death and dying and sensory abilities had negligible or weak correlation with almost any of the EQ-5D dimensions (<a href="#pone.0290606.t005" data-ref-type="table">Table 5</a>). Comparably and at the summary score level, Pearson’s correlation coefficients between EQ-5D indices or EQ VAS and the WHOQOL-OLD total score and facet scores followed that pattern consistently; facets that were dissimilar to the EQ-5D contents such as intimacy, death and dying and sensory abilities had negligible or weak correlations with the EQ-5D indices or EQ VAS. In turn, the WHOQOL-OLD total score as well as the facets autonomy, past, present and future activities and social participation showed significant and moderate correlations with the EQ-5D indices and EQ VAS (<a href="#pone.0290606.t005" data-ref-type="table">Table 5</a>).

<div id="pone.0290606.t005" class="table-wrap">

10.1371/journal.pone.0290606.t005

<div class="caption">

###### Relationship of EQ-5D and WHOQOL-OLD; Spearman correlation coefficients of EQ-5D dimensions and Pearson correlation coefficients of EQ-5D indices and EQ VAS with WHOQOL-OLD summary and facet scores.

</div>

<img src="pone.0290606.t005.jpg" id="pone.0290606.t005g" />

<table>
<thead>
<tr>
<th style="text-align: left;">Dimension</th>
<th style="text-align: left;">Version</th>
<th style="text-align: left;">WHOQOL-OLD total score</th>
<th style="text-align: left;">Sensory abilities</th>
<th style="text-align: left;">Autonomy</th>
<th style="text-align: left;">Past, present and future activities</th>
<th style="text-align: left;">Social participation</th>
<th style="text-align: left;">Death and dying</th>
<th style="text-align: left;">Intimacy</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: left;"><strong>Mobility</strong></td>
<td style="text-align: left;">3L</td>
<td style="text-align: left;">-0.270<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.143</td>
<td style="text-align: left;">-0.215<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.215<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.314<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.102</td>
<td style="text-align: left;">-0.052</td>
</tr>
<tr>
<td style="text-align: left;">5L</td>
<td style="text-align: left;">-0.346<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.286<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.297<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.276<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.397<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.070</td>
<td style="text-align: left;">-0.061</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>Self-care</strong></td>
<td style="text-align: left;">3L</td>
<td style="text-align: left;">-0.293<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.195<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.323<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.204<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.309<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.052</td>
<td style="text-align: left;">-0.086</td>
</tr>
<tr>
<td style="text-align: left;">5L</td>
<td style="text-align: left;">-0.350<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.218<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.346<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.258<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.394<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.065</td>
<td style="text-align: left;">-0.135<a href="#t005fn002" data-ref-type="table-fn">*</a></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>Usual Activities</strong></td>
<td style="text-align: left;">3L</td>
<td style="text-align: left;">-0.376<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.255<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.326<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.326<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.420<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.071</td>
<td style="text-align: left;">-0.089</td>
</tr>
<tr>
<td style="text-align: left;">5L</td>
<td style="text-align: left;">-0.442<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.320<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.446<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.348<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.513<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.112</td>
<td style="text-align: left;">-0.024</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>Pain/discomfort</strong></td>
<td style="text-align: left;">3L</td>
<td style="text-align: left;">-0.229<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.154<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.132<a href="#t005fn002" data-ref-type="table-fn">*</a></td>
<td style="text-align: left;">-0.159<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.202<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.138<a href="#t005fn002" data-ref-type="table-fn">*</a></td>
<td style="text-align: left;">-0.112</td>
</tr>
<tr>
<td style="text-align: left;">5L</td>
<td style="text-align: left;">-0.236<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.205<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.153<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.158<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.269<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.162<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.015</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>Anxiety/depression</strong></td>
<td style="text-align: left;">3L</td>
<td style="text-align: left;">-0.345<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.242<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.204<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.250<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.263<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.284<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.099</td>
</tr>
<tr>
<td style="text-align: left;">5L</td>
<td style="text-align: left;">-0.406<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.283<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.275<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.274<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.275<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.353<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">-0.117<a href="#t005fn002" data-ref-type="table-fn">*</a></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>EQ-5D index</strong></td>
<td style="text-align: left;">3L</td>
<td style="text-align: left;">0.425<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.250<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.348<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.331<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.418<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.174<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.122<a href="#t005fn002" data-ref-type="table-fn">*</a></td>
</tr>
<tr>
<td style="text-align: left;">5L</td>
<td style="text-align: left;">0.396<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.257<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.331<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.300<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.435<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.166<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.041</td>
</tr>
<tr>
<td style="text-align: left;"><strong>EQ VAS</strong></td>
<td style="text-align: left;">n/a</td>
<td style="text-align: left;">0.400<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.303<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.268<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.308<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.411<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.177<a href="#t005fn001" data-ref-type="table-fn">**</a></td>
<td style="text-align: left;">0.053</td>
</tr>
</tbody>
</table>

\*\* p \< 0.01

\* p \< 0.05

</div>

### Sensitivity to known group differences

Sensitivity to known-group differences based on EQ-5D and WHOQOL-OLD components with regard to subgroups based on gender, education, care levels and general health status are displayed in <a href="#pone.0290606.t006" data-ref-type="table">Table 6</a>. For the remaining subgroup characteristics <a href="#pone.0290606.t006" data-ref-type="table">Table 6</a> only provides a descriptive summary based on mean summary scores. The EQ-5D indices and EQ VAS significantly and to a similar extent discriminate between different care levels and categories of general health status with medium to large effect sizes, where higher care levels, i.e. more extensive care needs, and lower general health resulted in lower scores. Similarly, the WHOQOL-OLD total score and facet scores were able to detect significant differences between these groups with mostly medium effect sizes. Exceptions were found in the intimacy and death and dying facets, where group differences were not significant. Differences between groups based on gender and education were mostly not significant; however, few exceptions were observed for subgroups based on education for WHOQOL-OLD total score and autonomy, past, present and future activities and intimacy facets with small effect sizes.

<div id="pone.0290606.t006" class="table-wrap">

10.1371/journal.pone.0290606.t006

<div class="caption">

###### Mean values and standard deviation for EQ-5D-3L, EQ-5D-5L, EQ VAS and WHOQOL-OLD total as well as facet scores for the total sample and by subgroups.

</div>

<img src="pone.0290606.t006.jpg" id="pone.0290606.t006g" />

<table>
<thead>
<tr>
<th colspan="2" rowspan="2" style="text-align: left;">Characteristics</th>
<th style="text-align: center;">N</th>
<th colspan="2" style="text-align: center;">5L index</th>
<th colspan="2" style="text-align: center;">3L index</th>
<th colspan="2" style="text-align: center;">EQ VAS</th>
<th colspan="2" style="text-align: center;">WHOQOL-OLD total score</th>
<th colspan="2" style="text-align: center;">Sensory abilities</th>
<th colspan="2" style="text-align: center;">Autonomy</th>
<th colspan="2" style="text-align: center;">Past, present and future activities</th>
<th colspan="2" style="text-align: center;">Social participation</th>
<th colspan="2" style="text-align: center;">Death and dying</th>
<th colspan="2" style="text-align: center;">Intimacy</th>
</tr>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
<th style="text-align: center;">Mean</th>
<th style="text-align: center;">SD</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><strong>Total sample</strong></td>
<td style="text-align: center;">329</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.30</td>
<td style="text-align: center;">0.54</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">57.2</td>
<td style="text-align: center;">19.8</td>
<td style="text-align: center;">62.7</td>
<td style="text-align: center;">13.3</td>
<td style="text-align: center;">62.7</td>
<td style="text-align: center;">22.0</td>
<td style="text-align: center;">59.4</td>
<td style="text-align: center;">21.0</td>
<td style="text-align: center;">63.8</td>
<td style="text-align: center;">16.6</td>
<td style="text-align: center;">57.3</td>
<td style="text-align: center;">19.9</td>
<td style="text-align: center;">64.3</td>
<td style="text-align: center;">27.5</td>
<td style="text-align: center;">68.1</td>
<td style="text-align: center;">21.2</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><strong>Gender</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: center;">215</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.53</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">57.8</td>
<td style="text-align: center;">19.5</td>
<td style="text-align: center;">63.8</td>
<td style="text-align: center;">13.3</td>
<td style="text-align: center;">64.8</td>
<td style="text-align: center;">23.0</td>
<td style="text-align: center;">60.8</td>
<td style="text-align: center;">21.5</td>
<td style="text-align: center;">64.9</td>
<td style="text-align: center;">15.7</td>
<td style="text-align: center;">58.4</td>
<td style="text-align: center;">20.1</td>
<td style="text-align: center;">65.1</td>
<td style="text-align: center;">27.6</td>
<td style="text-align: center;">68.7</td>
<td style="text-align: center;">20.3</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: center;">98</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">0.56</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">55.3</td>
<td style="text-align: center;">20.8</td>
<td style="text-align: center;">61.6</td>
<td style="text-align: center;">12.5</td>
<td style="text-align: center;">59.8</td>
<td style="text-align: center;">19.7</td>
<td style="text-align: center;">57.9</td>
<td style="text-align: center;">20.0</td>
<td style="text-align: center;">63.0</td>
<td style="text-align: center;">17.5</td>
<td style="text-align: center;">54.7</td>
<td style="text-align: center;">19.5</td>
<td style="text-align: center;">64.8</td>
<td style="text-align: center;">25.9</td>
<td style="text-align: center;">68.3</td>
<td style="text-align: center;">22.5</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Cohen’s d</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>04</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>17</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>13</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>17</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>23</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>14</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>12</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>18</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>01</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>02</em></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="8" style="text-align: left;"><strong>Age group</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">65–70 years</td>
<td style="text-align: center;">27</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;">0.35</td>
<td style="text-align: center;">0.47</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">50.6</td>
<td style="text-align: center;">25.4</td>
<td style="text-align: center;">61.5</td>
<td style="text-align: center;">14.8</td>
<td style="text-align: center;">68.0</td>
<td style="text-align: center;">29.1</td>
<td style="text-align: center;">64.6</td>
<td style="text-align: center;">23.0</td>
<td style="text-align: center;">56.6</td>
<td style="text-align: center;">14.9</td>
<td style="text-align: center;">54.7</td>
<td style="text-align: center;">20.1</td>
<td style="text-align: center;">55.5</td>
<td style="text-align: center;">33.9</td>
<td style="text-align: center;">68.9</td>
<td style="text-align: center;">20.0</td>
</tr>
<tr>
<td style="text-align: left;">71–75 years</td>
<td style="text-align: center;">21</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.57</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">61.6</td>
<td style="text-align: center;">18.9</td>
<td style="text-align: center;">61.6</td>
<td style="text-align: center;">17.0</td>
<td style="text-align: center;">63.0</td>
<td style="text-align: center;">23.4</td>
<td style="text-align: center;">55.7</td>
<td style="text-align: center;">25.3</td>
<td style="text-align: center;">60.6</td>
<td style="text-align: center;">21.8</td>
<td style="text-align: center;">51.7</td>
<td style="text-align: center;">26.3</td>
<td style="text-align: center;">69.0</td>
<td style="text-align: center;">25.6</td>
<td style="text-align: center;">71.7</td>
<td style="text-align: center;">22.2</td>
</tr>
<tr>
<td style="text-align: left;">76–80 years</td>
<td style="text-align: center;">62</td>
<td style="text-align: center;">0.69</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">61.7</td>
<td style="text-align: center;">20.2</td>
<td style="text-align: center;">62.3</td>
<td style="text-align: center;">12.6</td>
<td style="text-align: center;">65.3</td>
<td style="text-align: center;">19.1</td>
<td style="text-align: center;">56.8</td>
<td style="text-align: center;">20.1</td>
<td style="text-align: center;">64.7</td>
<td style="text-align: center;">16.7</td>
<td style="text-align: center;">57.4</td>
<td style="text-align: center;">19.6</td>
<td style="text-align: center;">61.1</td>
<td style="text-align: center;">27.4</td>
<td style="text-align: center;">67.4</td>
<td style="text-align: center;">23.2</td>
</tr>
<tr>
<td style="text-align: left;">81–85 years</td>
<td style="text-align: center;">78</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">55.4</td>
<td style="text-align: center;">19.3</td>
<td style="text-align: center;">61.5</td>
<td style="text-align: center;">11.4</td>
<td style="text-align: center;">61.5</td>
<td style="text-align: center;">19.2</td>
<td style="text-align: center;">60.1</td>
<td style="text-align: center;">17.5</td>
<td style="text-align: center;">63.8</td>
<td style="text-align: center;">14.8</td>
<td style="text-align: center;">55.1</td>
<td style="text-align: center;">17.8</td>
<td style="text-align: center;">59.4</td>
<td style="text-align: center;">26.4</td>
<td style="text-align: center;">68.4</td>
<td style="text-align: center;">18.4</td>
</tr>
<tr>
<td style="text-align: left;">86–90 years</td>
<td style="text-align: center;">88</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.34</td>
<td style="text-align: center;">0.53</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">58.5</td>
<td style="text-align: center;">18.5</td>
<td style="text-align: center;">64.9</td>
<td style="text-align: center;">13.2</td>
<td style="text-align: center;">62.3</td>
<td style="text-align: center;">21.5</td>
<td style="text-align: center;">61.1</td>
<td style="text-align: center;">22.1</td>
<td style="text-align: center;">66.6</td>
<td style="text-align: center;">17.1</td>
<td style="text-align: center;">60.9</td>
<td style="text-align: center;">20.7</td>
<td style="text-align: center;">70.3</td>
<td style="text-align: center;">23.9</td>
<td style="text-align: center;">67.6</td>
<td style="text-align: center;">21.9</td>
</tr>
<tr>
<td style="text-align: left;">91–95 years</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.20</td>
<td style="text-align: center;">53.5</td>
<td style="text-align: center;">19.5</td>
<td style="text-align: center;">64.4</td>
<td style="text-align: center;">13.1</td>
<td style="text-align: center;">61.7</td>
<td style="text-align: center;">25.0</td>
<td style="text-align: center;">60.4</td>
<td style="text-align: center;">20.9</td>
<td style="text-align: center;">66.0</td>
<td style="text-align: center;">15.1</td>
<td style="text-align: center;">58.7</td>
<td style="text-align: center;">18.6</td>
<td style="text-align: center;">71.2</td>
<td style="text-align: center;">29.8</td>
<td style="text-align: center;">68.4</td>
<td style="text-align: center;">20.3</td>
</tr>
<tr>
<td style="text-align: left;">96–100 years</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.43</td>
<td style="text-align: center;">0.20</td>
<td style="text-align: center;">52.8</td>
<td style="text-align: center;">18.6</td>
<td style="text-align: center;">53.4</td>
<td style="text-align: center;">17.6</td>
<td style="text-align: center;">45.8</td>
<td style="text-align: center;">27.4</td>
<td style="text-align: center;">47.2</td>
<td style="text-align: center;">25.4</td>
<td style="text-align: center;">53.5</td>
<td style="text-align: center;">17.4</td>
<td style="text-align: center;">54.2</td>
<td style="text-align: center;">19.3</td>
<td style="text-align: center;">54.2</td>
<td style="text-align: center;">33.6</td>
<td style="text-align: center;">65.3</td>
<td style="text-align: center;">27.3</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;"><strong>Marital status</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Single</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">0.78</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">56.3</td>
<td style="text-align: center;">16.0</td>
<td style="text-align: center;">59.3</td>
<td style="text-align: center;">14.1</td>
<td style="text-align: center;">69.0</td>
<td style="text-align: center;">21.9</td>
<td style="text-align: center;">61.6</td>
<td style="text-align: center;">21.2</td>
<td style="text-align: center;">59.2</td>
<td style="text-align: center;">19.8</td>
<td style="text-align: center;">51.5</td>
<td style="text-align: center;">17.5</td>
<td style="text-align: center;">67.3</td>
<td style="text-align: center;">26.5</td>
<td style="text-align: center;">46.4</td>
<td style="text-align: center;">24.4</td>
</tr>
<tr>
<td style="text-align: left;">Married/partnership</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.30</td>
<td style="text-align: center;">0.54</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">55.5</td>
<td style="text-align: center;">20.6</td>
<td style="text-align: center;">62.1</td>
<td style="text-align: center;">12.2</td>
<td style="text-align: center;">60.3</td>
<td style="text-align: center;">21.6</td>
<td style="text-align: center;">55.6</td>
<td style="text-align: center;">19.6</td>
<td style="text-align: center;">63.0</td>
<td style="text-align: center;">16.7</td>
<td style="text-align: center;">55.2</td>
<td style="text-align: center;">19.3</td>
<td style="text-align: center;">60.7</td>
<td style="text-align: center;">27.8</td>
<td style="text-align: center;">77.2</td>
<td style="text-align: center;">19.0</td>
</tr>
<tr>
<td style="text-align: left;">Widowed</td>
<td style="text-align: center;">176</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">0.52</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">57.9</td>
<td style="text-align: center;">20.3</td>
<td style="text-align: center;">63.3</td>
<td style="text-align: center;">14.0</td>
<td style="text-align: center;">62.6</td>
<td style="text-align: center;">22.9</td>
<td style="text-align: center;">59.9</td>
<td style="text-align: center;">22.0</td>
<td style="text-align: center;">65.4</td>
<td style="text-align: center;">16.3</td>
<td style="text-align: center;">59.1</td>
<td style="text-align: center;">20.4</td>
<td style="text-align: center;">65.7</td>
<td style="text-align: center;">27.5</td>
<td style="text-align: center;">66.5</td>
<td style="text-align: center;">19.0</td>
</tr>
<tr>
<td style="text-align: left;">Divorced/separated</td>
<td style="text-align: center;">24</td>
<td style="text-align: center;">0.73</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">61.1</td>
<td style="text-align: center;">16.4</td>
<td style="text-align: center;">66.0</td>
<td style="text-align: center;">10.0</td>
<td style="text-align: center;">68.5</td>
<td style="text-align: center;">18.3</td>
<td style="text-align: center;">71.1</td>
<td style="text-align: center;">16.5</td>
<td style="text-align: center;">62.5</td>
<td style="text-align: center;">15.0</td>
<td style="text-align: center;">60.9</td>
<td style="text-align: center;">18.3</td>
<td style="text-align: center;">72.0</td>
<td style="text-align: center;">23.4</td>
<td style="text-align: center;">62.2</td>
<td style="text-align: center;">22.0</td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><strong>Educational level</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: center;">183</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.31</td>
<td style="text-align: center;">0.52</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">56.1</td>
<td style="text-align: center;">19.9</td>
<td style="text-align: center;">61.0</td>
<td style="text-align: center;">13.2</td>
<td style="text-align: center;">62.4</td>
<td style="text-align: center;">20.7</td>
<td style="text-align: center;">56.3</td>
<td style="text-align: center;">22.1</td>
<td style="text-align: center;">61.5</td>
<td style="text-align: center;">17.0</td>
<td style="text-align: center;">56.2</td>
<td style="text-align: center;">20.6</td>
<td style="text-align: center;">64.9</td>
<td style="text-align: center;">27.9</td>
<td style="text-align: center;">64.1</td>
<td style="text-align: center;">21.4</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: center;">77</td>
<td style="text-align: center;">0.70</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">59.6</td>
<td style="text-align: center;">19.7</td>
<td style="text-align: center;">64.4</td>
<td style="text-align: center;">13.3</td>
<td style="text-align: center;">64.5</td>
<td style="text-align: center;">24.1</td>
<td style="text-align: center;">63.1</td>
<td style="text-align: center;">20.9</td>
<td style="text-align: center;">65.7</td>
<td style="text-align: center;">15.4</td>
<td style="text-align: center;">58.9</td>
<td style="text-align: center;">19.3</td>
<td style="text-align: center;">64.4</td>
<td style="text-align: center;">25.0</td>
<td style="text-align: center;">70.1</td>
<td style="text-align: center;">20.8</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: center;">62</td>
<td style="text-align: center;">0.66</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.56</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">57.5</td>
<td style="text-align: center;">19.8</td>
<td style="text-align: center;">65.8</td>
<td style="text-align: center;">13.0</td>
<td style="text-align: center;">62.9</td>
<td style="text-align: center;">23.1</td>
<td style="text-align: center;">64.1</td>
<td style="text-align: center;">16.9</td>
<td style="text-align: center;">68.9</td>
<td style="text-align: center;">15.6</td>
<td style="text-align: center;">58.9</td>
<td style="text-align: center;">18.4</td>
<td style="text-align: center;">62.5</td>
<td style="text-align: center;">28.9</td>
<td style="text-align: center;">76.6</td>
<td style="text-align: center;">18.2</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Eta squared</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>012</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>01</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>005</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>024</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>001</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>029</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>032</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>005</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>001</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>053</em></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="7" style="text-align: left;"><strong>Care level</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">0</td>
<td style="text-align: center;">61</td>
<td style="text-align: center;">0.83</td>
<td style="text-align: center;">0.14</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.17</td>
<td style="text-align: center;">66.9</td>
<td style="text-align: center;">17.7</td>
<td style="text-align: center;">68.1</td>
<td style="text-align: center;">11.9</td>
<td style="text-align: center;">65.3</td>
<td style="text-align: center;">18.7</td>
<td style="text-align: center;">68.3</td>
<td style="text-align: center;">17.3</td>
<td style="text-align: center;">69.7</td>
<td style="text-align: center;">15.0</td>
<td style="text-align: center;">68.4</td>
<td style="text-align: center;">16.2</td>
<td style="text-align: center;">62.4</td>
<td style="text-align: center;">25.4</td>
<td style="text-align: center;">74.6</td>
<td style="text-align: center;">20.3</td>
</tr>
<tr>
<td style="text-align: left;">1</td>
<td style="text-align: center;">22</td>
<td style="text-align: center;">0.75</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.67</td>
<td style="text-align: center;">0.18</td>
<td style="text-align: center;">61.5</td>
<td style="text-align: center;">18.3</td>
<td style="text-align: center;">64.1</td>
<td style="text-align: center;">10.5</td>
<td style="text-align: center;">70.5</td>
<td style="text-align: center;">21.2</td>
<td style="text-align: center;">65.0</td>
<td style="text-align: center;">17.9</td>
<td style="text-align: center;">65.2</td>
<td style="text-align: center;">10.3</td>
<td style="text-align: center;">58.8</td>
<td style="text-align: center;">19.6</td>
<td style="text-align: center;">59.8</td>
<td style="text-align: center;">24.8</td>
<td style="text-align: center;">66.2</td>
<td style="text-align: center;">18.0</td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: center;">99</td>
<td style="text-align: center;">0.60</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.50</td>
<td style="text-align: center;">0.21</td>
<td style="text-align: center;">55.9</td>
<td style="text-align: center;">19.0</td>
<td style="text-align: center;">60.2</td>
<td style="text-align: center;">14.0</td>
<td style="text-align: center;">59.5</td>
<td style="text-align: center;">22.4</td>
<td style="text-align: center;">55.1</td>
<td style="text-align: center;">22.3</td>
<td style="text-align: center;">62.6</td>
<td style="text-align: center;">17.4</td>
<td style="text-align: center;">55.5</td>
<td style="text-align: center;">19.2</td>
<td style="text-align: center;">63.2</td>
<td style="text-align: center;">28.8</td>
<td style="text-align: center;">65.0</td>
<td style="text-align: center;">23.2</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: center;">90</td>
<td style="text-align: center;">0.59</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.49</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">52.4</td>
<td style="text-align: center;">19.1</td>
<td style="text-align: center;">61.1</td>
<td style="text-align: center;">12.7</td>
<td style="text-align: center;">62.7</td>
<td style="text-align: center;">22.7</td>
<td style="text-align: center;">58.4</td>
<td style="text-align: center;">18.8</td>
<td style="text-align: center;">61.1</td>
<td style="text-align: center;">17.8</td>
<td style="text-align: center;">52.0</td>
<td style="text-align: center;">19.6</td>
<td style="text-align: center;">65.2</td>
<td style="text-align: center;">27.1</td>
<td style="text-align: center;">66.7</td>
<td style="text-align: center;">21.5</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">0.50</td>
<td style="text-align: center;">0.34</td>
<td style="text-align: center;">0.39</td>
<td style="text-align: center;">0.27</td>
<td style="text-align: center;">53.8</td>
<td style="text-align: center;">19.4</td>
<td style="text-align: center;">61.6</td>
<td style="text-align: center;">12.0</td>
<td style="text-align: center;">60.3</td>
<td style="text-align: center;">20.5</td>
<td style="text-align: center;">54.1</td>
<td style="text-align: center;">21.4</td>
<td style="text-align: center;">63.2</td>
<td style="text-align: center;">13.6</td>
<td style="text-align: center;">54.5</td>
<td style="text-align: center;">20.8</td>
<td style="text-align: center;">65.4</td>
<td style="text-align: center;">18.6</td>
<td style="text-align: center;">71.2</td>
<td style="text-align: center;">18.1</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">0.61</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.33</td>
<td style="text-align: center;">32.9</td>
<td style="text-align: center;">26.7</td>
<td style="text-align: center;">49.3</td>
<td style="text-align: center;">14.4</td>
<td style="text-align: center;">41.1</td>
<td style="text-align: center;">23.6</td>
<td style="text-align: center;">41.4</td>
<td style="text-align: center;">21.6</td>
<td style="text-align: center;">55.4</td>
<td style="text-align: center;">22.9</td>
<td style="text-align: center;">34.8</td>
<td style="text-align: center;">24.7</td>
<td style="text-align: center;">62.2</td>
<td style="text-align: center;">34.1</td>
<td style="text-align: center;">60.7</td>
<td style="text-align: center;">23.6</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Eta squared</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>16</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>20</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>11</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>075</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>041</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>08</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>042</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>12</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>003</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>032</em></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>Care setting</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Home based</td>
<td style="text-align: center;">196</td>
<td style="text-align: center;">0.62</td>
<td style="text-align: center;">0.32</td>
<td style="text-align: center;">0.53</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">55.7</td>
<td style="text-align: center;">20.7</td>
<td style="text-align: center;">61.0</td>
<td style="text-align: center;">13.1</td>
<td style="text-align: center;">59.9</td>
<td style="text-align: center;">21.4</td>
<td style="text-align: center;">57.6</td>
<td style="text-align: center;">20.8</td>
<td style="text-align: center;">62.1</td>
<td style="text-align: center;">16.8</td>
<td style="text-align: center;">55.1</td>
<td style="text-align: center;">20.0</td>
<td style="text-align: center;">60.1</td>
<td style="text-align: center;">26.9</td>
<td style="text-align: center;">70.4</td>
<td style="text-align: center;">20.6</td>
</tr>
<tr>
<td style="text-align: left;">Nursing home</td>
<td style="text-align: center;">123</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">58.6</td>
<td style="text-align: center;">18.5</td>
<td style="text-align: center;">64.8</td>
<td style="text-align: center;">12.9</td>
<td style="text-align: center;">66.6</td>
<td style="text-align: center;">22.6</td>
<td style="text-align: center;">61.7</td>
<td style="text-align: center;">21.5</td>
<td style="text-align: center;">65.7</td>
<td style="text-align: center;">15.9</td>
<td style="text-align: center;">59.3</td>
<td style="text-align: center;">19.4</td>
<td style="text-align: center;">71.6</td>
<td style="text-align: center;">26.5</td>
<td style="text-align: center;">64.2</td>
<td style="text-align: center;">21.8</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">c</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">b</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Formal care</td>
<td style="text-align: center;">123</td>
<td style="text-align: center;">0.65</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.55</td>
<td style="text-align: center;">0.23</td>
<td style="text-align: center;">58.6</td>
<td style="text-align: center;">18.5</td>
<td style="text-align: center;">64.8</td>
<td style="text-align: center;">12.9</td>
<td style="text-align: center;">66.6</td>
<td style="text-align: center;">22.6</td>
<td style="text-align: center;">61.7</td>
<td style="text-align: center;">21.5</td>
<td style="text-align: center;">65.7</td>
<td style="text-align: center;">15.9</td>
<td style="text-align: center;">59.3</td>
<td style="text-align: center;">19.4</td>
<td style="text-align: center;">71.6</td>
<td style="text-align: center;">26.5</td>
<td style="text-align: center;">64.2</td>
<td style="text-align: center;">21.8</td>
</tr>
<tr>
<td style="text-align: left;">Informal care</td>
<td style="text-align: center;">80</td>
<td style="text-align: center;">0.68</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.58</td>
<td style="text-align: center;">0.25</td>
<td style="text-align: center;">59.2</td>
<td style="text-align: center;">20.0</td>
<td style="text-align: center;">62.3</td>
<td style="text-align: center;">11.6</td>
<td style="text-align: center;">61.9</td>
<td style="text-align: center;">20.5</td>
<td style="text-align: center;">57.0</td>
<td style="text-align: center;">19.8</td>
<td style="text-align: center;">61.7</td>
<td style="text-align: center;">14.8</td>
<td style="text-align: center;">56.1</td>
<td style="text-align: center;">18.7</td>
<td style="text-align: center;">63.1</td>
<td style="text-align: center;">27.1</td>
<td style="text-align: center;">73.2</td>
<td style="text-align: center;">21.0</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>General health status</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">a</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">d</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;">Very good</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">0.82</td>
<td style="text-align: center;">0.22</td>
<td style="text-align: center;">0.71</td>
<td style="text-align: center;">0.28</td>
<td style="text-align: center;">73.1</td>
<td style="text-align: center;">17.1</td>
<td style="text-align: center;">67.1</td>
<td style="text-align: center;">13.9</td>
<td style="text-align: center;">64.1</td>
<td style="text-align: center;">28.9</td>
<td style="text-align: center;">56.5</td>
<td style="text-align: center;">30.6</td>
<td style="text-align: center;">64.1</td>
<td style="text-align: center;">16.3</td>
<td style="text-align: center;">67.2</td>
<td style="text-align: center;">20.8</td>
<td style="text-align: center;">75.0</td>
<td style="text-align: center;">19.2</td>
<td style="text-align: center;">75.0</td>
<td style="text-align: center;">16.8</td>
</tr>
<tr>
<td style="text-align: left;">Good</td>
<td style="text-align: center;">97</td>
<td style="text-align: center;">0.82</td>
<td style="text-align: center;">0.16</td>
<td style="text-align: center;">0.69</td>
<td style="text-align: center;">0.20</td>
<td style="text-align: center;">70.9</td>
<td style="text-align: center;">16.2</td>
<td style="text-align: center;">69.4</td>
<td style="text-align: center;">10.4</td>
<td style="text-align: center;">70.5</td>
<td style="text-align: center;">21.5</td>
<td style="text-align: center;">67.5</td>
<td style="text-align: center;">19.5</td>
<td style="text-align: center;">69.1</td>
<td style="text-align: center;">14.7</td>
<td style="text-align: center;">64.4</td>
<td style="text-align: center;">19.2</td>
<td style="text-align: center;">73.7</td>
<td style="text-align: center;">20.8</td>
<td style="text-align: center;">70.1</td>
<td style="text-align: center;">20.3</td>
</tr>
<tr>
<td style="text-align: left;">Moderate</td>
<td style="text-align: center;">174</td>
<td style="text-align: center;">0.64</td>
<td style="text-align: center;">0.24</td>
<td style="text-align: center;">0.53</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">55.0</td>
<td style="text-align: center;">15.4</td>
<td style="text-align: center;">62.3</td>
<td style="text-align: center;">12.5</td>
<td style="text-align: center;">62.1</td>
<td style="text-align: center;">20.4</td>
<td style="text-align: center;">59.6</td>
<td style="text-align: center;">19.4</td>
<td style="text-align: center;">64.4</td>
<td style="text-align: center;">15.5</td>
<td style="text-align: center;">57.9</td>
<td style="text-align: center;">17.4</td>
<td style="text-align: center;">61.8</td>
<td style="text-align: center;">28.5</td>
<td style="text-align: center;">67.9</td>
<td style="text-align: center;">20.6</td>
</tr>
<tr>
<td style="text-align: left;">Bad</td>
<td style="text-align: center;">47</td>
<td style="text-align: center;">0.29</td>
<td style="text-align: center;">0.33</td>
<td style="text-align: center;">0.26</td>
<td style="text-align: center;">0.19</td>
<td style="text-align: center;">35.4</td>
<td style="text-align: center;">18.0</td>
<td style="text-align: center;">50.4</td>
<td style="text-align: center;">11.8</td>
<td style="text-align: center;">51.1</td>
<td style="text-align: center;">21.1</td>
<td style="text-align: center;">43.9</td>
<td style="text-align: center;">19.5</td>
<td style="text-align: center;">50.7</td>
<td style="text-align: center;">18.3</td>
<td style="text-align: center;">39.7</td>
<td style="text-align: center;">19.1</td>
<td style="text-align: center;">55.4</td>
<td style="text-align: center;">30.0</td>
<td style="text-align: center;">63.1</td>
<td style="text-align: center;">25.1</td>
</tr>
<tr>
<td style="text-align: left;">Very bad</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><em>Eta squared</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>37</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>34</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>36</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>21</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>098</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>13</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>12</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>17</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>07</em></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><em>0</em>.<em>016</em></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

<sup>a</sup> p \< 0.001

<sup>b</sup> p \< 0.05

<sup>c</sup> p \< 0.1

<sup>d</sup> not significant

</div>

With regard to the different care settings the results are just of descriptive nature, since causality of the effect of the care setting on health status or QoL cannot be inferred; here, the EQ-5D indices and EQ VAS did not show significant difference between these subgroups. In turn, significant differences between home based and institutionalised care-recipients were found on the WHOQOL-OLD total score as well as on the sensory abilities, death and dying and intimacy facets. Then again, when looking at the differences between formal and informal care recipients, significant differences were only observable on two facets, where recipients of formal care express less fear of death and dying, and informal care recipients report a higher level of intimacy.

## Discussion

To the best of our knowledge, this is the first prospective study to assess similarities and differences between the EQ-5D versions and the WHOQOL-OLD in a sample of aged care service recipients. The aim of this study was to assess and compare the relationship of instruments, their sensitivity to known-group differences, feasibility and test-retest reliability across EQ-5D and WHOQOL-OLD. In terms of feasibility and test-retest reliability both EQ-5D versions performed better than the WHOQOL-OLD. All three measures were sensitive to known-group differences based on aspects of general health status and care level. The analysis of association between measures indicated that EQ-5D and WHOQOL-OLD assess partially overlapping, but distinct constructs. When comparing the properties of the 3L and 5L in this sample, we found no superiority of either measure over the other. The 5L seemed to do better in terms of test-retest reliability and had stronger correlations with WHOQOL-OLD facets.

The calculated mean summary scores for the different types of care indicate higher QoL on almost all WHOQOL-OLD facets for recipients of formal care or respondents living in nursing homes. An exception to this rule is the intimacy facet, which suggests that respondents receiving informal care report a higher sense of companionship. With regard to the EQ index and EQ VAS results were less clear. Again, mean EQ-5D index and EQ VAS values were higher for the residential care subgroup, which was in line with the reported values on the WHOQOL-OLD facets, however, the opposite was found for the informal care subgroup, who reported slightly higher mean values. These results were contradictory to an earlier study. Borowiak and Kostka \[37\] used the 3L to compare QoL of older adults living in the community and in aged care institutions and found consistently higher values and fewer reported problems in the community-dwelling subgroup. Hence, we assume that our two-staged sampling process resulted in an underrepresentation of severely ill and highly dependent respondents living in care homes. However, the difference in mean general health status between respondents living at home or in institutions was small. Nevertheless, the direction of causality between health and care provision remains unclear. It could be either way that an individual’s health or QoL status determines the type of provided care or that the type of care has an impact on the individual’s health or QoL status.

With regard to sensitivity to known-group differences we found that both EQ-5D indices and EQ VAS discriminate well between different needs of care, i.e. care levels, which is in line with findings from Hara and colleagues \[38\] for the Japanese version of the 5L. Similarly, we observed satisfactory ability to differentiate different levels of general health status, which was also confirmed based on the 3L index for older adults in the literature \[39, 40\]. The WHOQOL-OLD total score and facets performed equally well differentiating subgroups based on their care levels and general health status. We only identified one study assessing and confirming known-groups validity of the WHOQOL-OLD, which assessed differences in general health \[41\]. These findings confirm our hypotheses with regard to care levels and general health status. On the other hand, we were not able to confirm our hypotheses with regard to group differences based on gender and education.

In the context of aged care services, the imperfect assessment of care needs and care provision makes it difficult to formally state hypotheses and analyse known group differences. Hence, we only reported mean group values based on EQ-5D and WHOQOL-OLD summary scores on a descriptive basis. For EQ-5D indices and EQ VAS we were not able to differentiate subgroups based on different care settings, which was also observed elsewhere \[39\]. Then again, non-health facets of the WHOQOL-OLD indicated differences in mean values between different care settings at a significant level, which is in line with the broader QoL scope of the measure and the specific target population of older adults.

Moreover, assessing the relationship between the EQ-5D versions and the WHOQOL-OLD, we only observed poor to moderate correlations. At both the individual dimension level as well as for indices or summary scores our hypotheses for central health-related aspects of the EQ-5D with WHOQOL-OLD facets, viz. physical and social functioning (EQ-5D Mobility, Self-care, Usual activities and WHOQOL-OLD facets autonomy, past, present and future activities and social participation), were largely confirmed. However, we had to reject our hypotheses on the correlation with mobility and self-care with the past, present and future activities facet as well for the correlation of mobility with the autonomy facet. On the other hand, our hypotheses with regard to non-health facets of the WHOQOL-OLD were confirmed; as expected, correlations of the facets death and dying and intimacy with all EQ-5D components except anxiety or depression were found to be poor. This suggests that EQ-5D and WHOQOL-OLD capture distinct aspects as indicated by the low correlation. We may conclude that the WHOQOL-OLD assess additional information, which would remain undetected by the EQ-5D. Hence, the best practice model of using additional age-specific measures alongside EQ-5D may be advisable in this population.

This study contributes to the scarce information on the feasibility properties of the 5L in samples of older adults as evidence suggests \[20\]. Generally, the proportion of missing values for both 3L and 5L was below 4%, which is very consistent with references found for the EQ-5D in the general population as well as in older adults and can be considered good. Similarly, the resulting completion rates for the 3L and 5L were also found to be very high with more than 94% of respondents reporting complete EQ-5D health state information \[20, 42–44\]. Even though 5L and 3L were consistently close, the 5L did not result in better feasibility properties than the 3L as suggested elsewhere \[44, 45\]. Nevertheless, these results should be considered in the light of the high proportion of respondents who required help completing the survey, which was around 59%. Of these, almost 70% had both someone reading the questions to them and helped filling in the response, which technically corresponds to an interviewer-based approach. This figure is consistent with other studies using the 3L in older adults, but highlights the increased need of assistance for older people when participating in QoL surveys \[46, 47\]. Interestingly, missing values were also very low for the WHOQOL-OLD. This seems surprising given that longer measures, such as the AQoL-4D or the SF-36, which are frequently used in samples of older adults, tend to produce more missing values in comparison to the EQ-5D \[48, 49\]. However, a study by Rolstad et al. \[50\] found that response burden is not necessarily associated with length of the questionnaire, but with content. Hence, this may explain the better feasibility of the WHOQOL-OLD, which is specifically designed for the use in older respondents. Another important aspect is the mixed evidence with regard to the completion of the EQ VAS. While only 4% of all responses to the EQ VAS were completely missing, we observed a considerable share of respondents (33%) with inadequate responses. Response or comprehension issues with the EQ VAS in older populations were reported before \[20, 46, 47, 49\]. However, while we were able to extract an EQ VAS rating for more than 90% of the respondents, these ratings seem to be more prone to error given that almost one third failed to respond in accordance with the instructions.

Overall, our test-retest findings suggest good reproducibility of both the 3L and 5L for the index as well as the individual dimensions, with no clear pattern of superiority for either version. According to a recent review from Gottschalk et al. \[17\] this is the first study assessing test-retest reliability of the 5L in older adults, thus, our reliability findings on the 5L cannot directly be compared with an age-adequate sample. With regard to reliability of the 3L index, our results suggest slightly better reproducibility in comparison to what was found in earlier studies with older adults; however, these included respondents with Alzheimer’s disease and dementia \[51–53\]. In a broader comparison, our resulting retest statistics agree with those reported in Buchholz et al. \[42\], but appear at the upper end of the range of reported test statistics. This is likely due to the fact that we aimed to control for a stable health state and retest respondents had a very consistent interval of 14 days between assessments \[54\]. In comparison to the EQ-5D, evidence with regard to the reproducibility of the WHOQOL-OLD was mixed. While the ICC for the total score was comparable in size to the 3L and 5L index scores, the ICC of the individual facets deviated widely. A similar pattern was observed for the weighted kappa statistics on the 24 WHOQOL-OLD items. The findings from an earlier study deviate from ours, in the sense that calculated ICCs were higher for the individual facets. At the same time, the lower reproducibility for the autonomy and past, present and future activities facets was not shown in the Chinese study \[55\].

### Strength and limitations

A strength of our study is the high proportion of older respondents even beyond the age of 80 and the good representation of respondents with greater need for care as suggested by the more severe care levels. Our study also adds to the scarce literature on test-retest reliability with a comparatively large retest sample of older care-dependents. However, the convenience sample is a limitation in our study for two reasons. First, the sample is unlikely to be representative, which does not allow to generalise the results towards the entire population. Secondly, the two-staged sampling strategy may have resulted in a sampling bias. Feedback from cooperating institutions suggests that participation was primarily refused due to a lack of interest or a self-perceived health status that was too poor to participate. Hence, this sample may have a positive selection with regard to health status and impairments. Furthermore, it has been discussed that the EQ-5D may be problematic in dementia, which is often prevalent in older adults. Unfortunately, we were not able to control our results for the cognitive status of respondents. But, given the promising results found here and in contrast to the problematic application of EQ-5D in patients with dementia described in the literature, we have to assume that mental conditions were underrepresented in our sample.

## Conclusion

Both the 3L and 5L showed good test-retest and feasibility properties in this sample with high completion rates, few missing values and good reproducibility of the index and individual dimensions. Generally, the EQ-5D descriptive system seems to be sensitive towards greater need for care as classified by the German needs assessment for care, i.e. the resulting care levels. The analysis of relationship between measures indicated that EQ-5D and WHOQOL-OLD assess partially overlapping, but distinct constructs. Hence, we conclude that using the WHOQOL-OLD alongside EQ-5D in this sample added further information on different aspects of QoL from care-dependents. However, researchers should be aware of the high proportion of people needing assistance to complete these measures, which may have important implications for the data collection process in similar samples. Even though neither version of the EQ-5D indicated superiority over the other, proper investigation of measurement aspects of the 5L are rare. Overall, further research is warranted to generalise these findings with additional validation studies in the context of aged care services–with an emphasis on evidence on the 5L to provide a better basis to decide which version of the EQ-5D to pick in clinical or economic evaluation studies in the context of health and aged care.

## Supporting information

<div class="caption">

(XLSX)

</div>

<div class="caption">

Click here for additional data file.

</div>

### Abbreviations

ANOVA  
Analysis of variance

3L  
EQ-5D-3L; 5L –EQ-5D-5L; EQ VAS—EQ-5D Visual Analogue Scale

ICC  
Intraclass correlation coefficient

QoL  
Quality of life

## References

1. Eurostat. Statistics explained. Population structure and ageing. 2022 [cited 3 Jan 2023]. Available from: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Population_structure_and_ageing.

2. AtellaV, Piano MortariA, KopinskaJ, BelottiF, LapiF, CricelliC, et al. Trends in age-related disease burden and healthcare utilization. Aging Cell. 2019; 18:e12861. Epub 2018/11/29. doi: 10.1111/acel.12861 .30488641PMC6351821

3. DivoMJ, MartinezCH, ManninoDM. Ageing and the epidemiology of multimorbidity. Eur Respir J. 2014; 44:1055–68. Epub 2014/08/19. doi: 10.1183/09031936.00059814 .25142482PMC4918092

4. PalladinoR, Tayu LeeJ, AshworthM, TriassiM, MillettC. Associations between multimorbidity, healthcare utilisation and health status: evidence from 16 European countries. Age Ageing. 2016; 45:431–5. Epub 2016/03/24. doi: 10.1093/ageing/afw044 .27013499PMC4846796

5. KhadkaJ, LangC, RatcliffeJ, CorlisM, WesselinghS, WhiteheadC, et al. Trends in the utilisation of aged care services in Australia, 2008–2016. BMC Geriatr. 2019; 19:213. Epub 2019/08/06. doi: 10.1186/s12877-019-1209-9 .31387533PMC6685150

6. European Commission. The 2021 ageing report. Economic and Budgetary Projections for the EU Member States (2019–2070). Luxembourg: Publications Office of the European Union; 2021.

7. LiJ, SongY. Formal and informal care. In: GuD, DupreME, editors. Encyclopedia of Gerontology and Population Aging. Cham: Springer International Publishing; 2020.

8. SietteJ, KnaggsGT, ZurynskiY, RatcliffeJ, DoddsL, WestbrookJ. Systematic review of 29 self-report instruments for assessing quality of life in older adults receiving aged care services. BMJ Open. 2021; 11:e050892. Epub 2021/11/18. doi: 10.1136/bmjopen-2021-050892 .34794991PMC8603300

9. Federal Statistical Office. Pflegebedürftige nach Versorgungsart, Geschlecht und Pflegegrade 2021. 2022 [cited 4 Jan 2023]. Available from: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Pflege/Tabellen/pflegebeduerftige-pflegestufe.html.

10. NettenA, BurgeP, MalleyJ, PotoglouD, TowersA-M, BrazierJ, et al. Outcomes of social care for adults: developing a preference-weighted measure. Health Technol Assess. 2012; 16:1–166. doi: 10.3310/hta16160 .22459668

11. BrazierJE, PeasgoodT, MukuriaC, MartenO, KreimeierS, LuoN, et al. The EQ-HWB: Overview of the Development of a Measure of Health and Wellbeing and Key Results. Value Health. 2022; 25:482–91. Epub 2022/03/08. doi: 10.1016/j.jval.2022.01.009 .35277337

12. Kennedy-MartinM, SlaapB, HerdmanM, van ReenenM, Kennedy-MartinT, GreinerW, et al. Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. Eur J Health Econ. 2020; 21:1245–57. Epub 2020/06/08. doi: 10.1007/s10198-020-01195-8 .32514643PMC7561556

13. ClelandJ, HutchinsonC, KhadkaJ, MilteR, RatcliffeJ. A Review of the Development and Application of Generic Preference-Based Instruments with the Older Population. Appl Health Econ Health Policy. 2019; 17:781–801. doi: 10.1007/s40258-019-00512-4 .31512086

14. BulamuNB, KaambwaB, RatcliffeJ. A systematic review of instruments for measuring outcomes in economic evaluation within aged care. Health Qual Life Outcomes. 2015; 13:179. Epub 2015/11/09. doi: 10.1186/s12955-015-0372-8 .26553129PMC4640110

15. PowerM, QuinnK, SchmidtS. Development of the WHOQOL-old module. Qual Life Res. 2005; 14:2197–214. doi: 10.1007/s11136-005-7380-9 .16328900

16. ConradI, MatschingerH, Riedel-HellerS, Gottberg C von, Kilian R. The psychometric properties of the German version of the WHOQOL-OLD in the German population aged 60 and older. Health Qual Life Outcomes. 2014; 12:105. doi: 10.1186/s12955-014-0105-4 .25213736PMC4172837

17. GottschalkS, KönigH-H, NejadM, DamsJ. Measurement properties of the EQ-5D in populations with a mean age of ≥ 75 years: a systematic review. Qual Life Res. 2022. Epub 2022/08/01. doi: 10.1007/s11136-022-03185-0 .35915354PMC9911506

18. HaywoodKL, GarrattAM, FitzpatrickR. Quality of life in older people: a structured review of generic self-assessed health instruments. Qual Life Res. 2005; 14:1651–68. doi: 10.1007/s11136-005-1743-0 .16119178

19. HerdmanM, GudexC, LloydA, JanssenM, KindP, ParkinD, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011; 20:1727–36. doi: 10.1007/s11136-011-9903-x .21479777PMC3220807

20. MartenO, BrandL, GreinerW. Feasibility of the EQ-5D in the elderly population: a systematic review of the literature. Qual Life Res. 2022; 31:1621–37. Epub 2021/10/06. doi: 10.1007/s11136-021-03007-9 .34613597PMC9098572

21. NortonEC. Chapter 17 Long-term care. In: CulyerAJ, NewhouseJP, editors. Handbook of Health Economics. Elsevier; 2000. pp. 955–94.

22. BrooksR. EuroQol: the current state of play. Health Policy. 1996; 37:53–72. doi: 10.1016/0168-8510(96)00822-6 .10158943

23. EuroQol Research Foundation. EQ-5D-5L User Guide. 2019 [cited 26 Mar 2020]. Available from: https://euroqol.org/publications/user-guides.

24. BüscherA, WingenfeldK, SchaefferD. Determining eligibility for long-term care-lessons from Germany. Int J Integr Care. 2011; 11:e019. doi: 10.5334/ijic.584 .21949486PMC3178799

25. BlümelM, SprangerA, AchstetterK, MaressoA, BusseR. Germany: Health System Review 2020. 2020 [cited 10 Jan 2023]. Available from: https://apps.who.int/iris/bitstream/handle/10665/341674/HiT-22-6-2020-eng.pdf.34232120

26. Federal Ministry of Health. Long-Term Care Guide. Everything you need to know about long-term care. 2020 [cited 16 Mar 2023]. Available from: https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Pflege/Broschueren/200320_BMG_Ratgeber-Pflege_DINA5_ENG_bf.pdf.

27. PolitDF. Getting serious about test-retest reliability: a critique of retest research and some recommendations. Qual Life Res. 2014; 23:1713–20. doi: 10.1007/s11136-014-0632-9 .24504622

28. GreinerW, WeijnenT, NieuwenhuizenM, OppeS, BadiaX, BusschbachJ, et al. A single European currency for EQ-5D health states. Results from a six-country study. Eur J Health Econ. 2003; 4:222–31. doi: 10.1007/s10198-003-0182-5 .15609189

29. LudwigK, Graf von der SchulenburgJ-M, GreinerW. German Value Set for the EQ-5D-5L. Pharmacoeconomics. 2018; 36:663–74. doi: 10.1007/s40273-018-0615-8 .29460066PMC5954069

30. ConradI, MatschingerH, KilianR, Riedel-HellerS. WHOQOL-OLD und WHOQOL_BREF. Manual: Handbuch für die deutschsprachigen Versionen der WHO_instrumente zur Erfassung der Lebensqualität im Alter. 1st ed. Göttingen, Bern, Wien: Hogrefe; 2016.

31. KooTK, LiMY. A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research. J Chiropr Med. 2016; 15:155–63. doi: 10.1016/j.jcm.2016.02.012 .27330520PMC4913118

32. LandisJR, KochGG. The Measurement of Observer Agreement for Categorical Data. Biometrics. 1977; 33:159. doi: 10.2307/2529310 843571

33. PentonH, DaysonC, HulmeC, YoungT. A Qualitative Investigation of Older Adults’ Conceptualization of Quality of Life and a Think-Aloud Content Validation of the EQ-5D-5L, SF-12v2, Warwick Edinburgh Mental Wellbeing Scale, and Office of National Statistics-4. Value Health. 2022; 25:2017–27. Epub 2022/06/25. doi: 10.1016/j.jval.2022.04.1735 .35760713

34. BowlingA, BanisterD, SuttonS, EvansO, WindsorJ. A multidimensional model of the quality of life in older age. Aging Ment Health. 2002; 6:355–71. doi: 10.1080/1360786021000006983 .12425770

35. CohenJ. Statistical Power Analysis for the Behavioral Sciences. 2nd ed. Hoboken: Taylor and Francis; 1988.

36. STATACorp. Stata Statistical Software: Release 17. College Station, TX: StataCorp LLC; 2021.

37. BorowiakE, KostkaT. Predictors of quality of life in older people living at home and in institutions. Aging Clin Exp Res. 2004; 16:212–20. doi: 10.1007/BF03327386 .15462464

38. HaraK, NakabeT, TanakaM, ImanakaY. Measuring the quality of life of long-term care service users in Japan: a cross-sectional questionnaire study. BMC Geriatr. 2022; 22:955. Epub 2022/12/12. doi: 10.1186/s12877-022-03662-8 .36510174PMC9746158

39. KaambwaB, GillL, McCaffreyN, LancsarE, CameronID, CrottyM, et al. An empirical comparison of the OPQoL-Brief, EQ-5D-3 L and ASCOT in a community dwelling population of older people. Health Qual Life Outcomes. 2015; 13:164. Epub 2015/09/30. doi: 10.1186/s12955-015-0357-7 .26420314PMC4588872

40. MichalowskyB, XieF, KohlmannT, GräskeJ, WübbelerM, ThyrianJR, et al. Acceptability and Validity of the EQ-5D in Patients Living With Dementia. Value Health. 2020; 23:760–7. Epub 2020/05/22. doi: 10.1016/j.jval.2020.01.022 .32540234

41. Lucas-CarrascoR, LaidlawK, PowerMJ. Suitability of the WHOQOL-BREF and WHOQOL-OLD for Spanish older adults. Aging Ment Health. 2011; 15:595–604. doi: 10.1080/13607863.2010.548054 .21815852

42. BuchholzI, JanssenMF, KohlmannT, FengY-S. A Systematic Review of Studies Comparing the Measurement Properties of the Three-Level and Five-Level Versions of the EQ-5D. Pharmacoeconomics. 2018; 36:645–61. doi: 10.1007/s40273-018-0642-5 .29572719PMC5954044

43. BuchholzI, MartenO, JanssenMF. Feasibility and validity of the EQ-5D-3L in the elderly Europeans: a secondary data analysis using SHARE(d) data. Qual Life Res. 2022; 31:3267–82. Epub 2022/05/27. doi: 10.1007/s11136-022-03158-3 .35624409PMC9546963

44. MartenO, GreinerW. Feasibility properties of the EQ-5D-3L and 5L in the general population: evidence from the GP Patient Survey on the impact of age. Health Econ Rev. 2022; 12:28. Epub 2022/05/20. doi: 10.1186/s13561-022-00374-y .35593942PMC9121571

45. ChristiansenASJ, MøllerMLS, KronborgC, HauganKJ, KøberL, HøjbergS, et al. Comparison of the three-level and the five-level versions of the EQ-5D. Eur J Health Econ. 2021; 22:621–8. Epub 2021/03/18. doi: 10.1007/s10198-021-01279-z .33733344

46. CoastJ, PetersTJ, RichardsSH, GunnellDJ. Use of the EuroQoL among elderly acute care patients. Qual Life Res. 1998; 7:1–10. doi: 10.1023/a:1008857203434 .9481146

47. HulmeC, LongAF, KneafseyR, ReidG. Using the EQ-5D to assess health-related quality of life in older people. Age Ageing. 2004; 33:504–7. doi: 10.1093/ageing/afh178 .15315921

48. BrazierJE, WaltersSJ, NichollJP, KohlerB. Using the SF-36 and Euroqol on an elderly population. Qual Life Res. 1996; 5:195–204. doi: 10.1007/BF00434741 .8998488

49. HollandR, SmithRD, HarveyI, SwiftL, LenaghanE. Assessing quality of life in the elderly: a direct comparison of the EQ-5D and AQoL. Health Econ. 2004; 13:793–805. doi: 10.1002/hec.858 .15322991

50. RolstadS, AdlerJ, RydénA. Response burden and questionnaire length: is shorter better? A review and meta-analysis. Value Health. 2011; 14:1101–8. doi: 10.1016/j.jval.2011.06.003 .22152180

51. AnkriJ, BeaufilsB, NovellaJ-L, MorroneI, GuilleminF, JollyD, et al. Use of the EQ-5D among patients suffering from dementia. J Clin Epidemiol. 2003; 56:1055–63. doi: 10.1016/s0895-4356(03)00175-6 .14614996

52. NaglieG, TomlinsonG, TanseyC, IrvineJ, RitvoP, BlackSE, et al. Utility-based Quality of Life measures in Alzheimer’s disease. Qual Life Res. 2006; 15:631–43. doi: 10.1007/s11136-005-4364-8 .16688496

53. van LeeuwenKM, BosmansJE, JansenAPD, HoogendijkEO, van TulderMW, van der HorstHE, et al. Comparing measurement properties of the EQ-5D-3L, ICECAP-O, and ASCOT in frail older adults. Value Health. 2015; 18:35–43. Epub 2014/11/11. doi: 10.1016/j.jval.2014.09.006 .25595232

54. PattanaphesajJ, ThavorncharoensapM. Measurement properties of the EQ-5D-5L compared to EQ-5D-3L in the Thai diabetes patients. Health Qual Life Outcomes. 2015; 13:14. doi: 10.1186/s12955-014-0203-3 .25890017PMC4328309

55. LiuR, WuS, HaoY, GuJ, FangJ, CaiN, et al. The Chinese version of the world health organization quality of life instrument-older adults module (WHOQOL-OLD): psychometric evaluation. Health Qual Life Outcomes. 2013; 11:156. doi: 10.1186/1477-7525-11-156 .24034698PMC3847352

[^1]: **Competing Interests:** I have read the journal’s policy and the authors of this manuscript have the following competing interests: OM and WG are members of the EuroQol Group and receive or have received research grants from the EuroQol Research Foundation. The views of the authors expressed in this paper do not necessarily reflect the views of the EuroQol Group. This does not alter our adherence to PLOS ONE policies on sharing data and materials.

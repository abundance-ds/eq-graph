---
project_id: "2015200"
work_id: "doi:10.1186/s13561-022-00374-y"
doi: "10.1186/s13561-022-00374-y"
pmid: "35593942"
pmcid: "PMC9121571"
title: "Feasibility properties of the EQ-5D-3L and 5L in the general population: evidence from the GP Patient Survey on the impact of age"
journal: "Health Economics Review"
publication_date: "2022-05-20"
volume: "12"
authors:
  - name: "Ole Marten"
    orcid: "http://orcid.org/0000-0002-2576-9110"
    affiliation_ids:
      - "Aff1"
  - name: "Wolfgang Greiner"
    orcid: "https://orcid.org/0000-0001-9552-6969"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "grid.7491.b0000 0001 0944 9128School of Public Health, Department of Health Economics and Health Care Management, Bielefeld University, Universitaetsstrasse 25, Bielefeld, Germany"
keywords:
  - "EQ-5D-3L"
  - "EQ-5D-5L"
  - "Feasibility"
  - "GPPS"
  - "Health-related quality of life"
  - "Older population"
licence: "cc-by"
source_file: "input/projects/2015200/papers/doi_10.1186_s13561-022-00374-y.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9121571/fullTextXML"
source_method: "epmc_xml"
source_sha256: "f6bf4223959913d08df7ab29e97c5b767e0307dc2c1f1f6b6c71cddb2b1fabef"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Feasibility properties of the EQ-5D-3L and 5L in the general population: evidence from the GP Patient Survey on the impact of age

## Abstract

### Background

There is evidence to suggest that the proportion of missing values is slightly higher in the older population resulting in lower completion rates of the EQ-5D. However, existing studies rarely provide a within-sample comparison of feasibility properties across age groups to quantify this difference. Hence, this study examines feasibility properties of the EQ-5D-3L and 5L in the general population and explores the impact of age on the completion of EQ-5D instruments.

### Methods

We pool five waves from the English GP Patient Survey, where respondents self-report their health in either EQ-5D-3L or 5L. Descriptive analysis was undertaken to analyse the distribution and proportion of missing values and completion rates stratified by age and EQ-5D version; logistic regression models were specified to quantify the impact of age, gender and potential long-term conditions on the completion of each of the EQ-5D instruments.

### Results

The total sample comprises ~ 4.36 million observations, of which 2.88 million respondents report their health in 5L and 1.47 million in 3L, respectively. Respondents over 64 years have slightly more missing values in each dimension than younger respondents. The highest share was observed for the oldest age group in the dimension anxiety/depression (3L 9.1% vs. 5L 7.6%), but was otherwise below 5%. Consequently, completion rates (observed and predicted) decreased with older age and at a higher rate after the age of 64; this was more pronounced for the 3L.

### Conclusion

Evidence from our study suggests that both the EQ-5D-3L and 5L have good feasibility properties. In comparison to younger populations there appears to be a higher proportion of respondents with incomplete responses beyond the age of 64 years. Overall, the 5L version compares more favourably in terms of missing values, completion rates as well as with regard to the expected probability of an incomplete descriptive system.

### Supplementary Information

The online version contains supplementary material available at 10.1186/s13561-022-00374-y.

## Background

Over the past decades the consideration of the patient perspective has gained enormous importance for health care and policy decision making \[1–3\]. With regard to this, the measurement of self-reported health-related quality of life (HRQoL) is a major component on this pathway. The EQ-5D is a well-established and widely used instrument develop by the EuroQol Group specifically intended for that purpose \[4\]. Over the years the EQ-5D has developed a significant role in economic decision making, since prominent health technology assessment bodies in the United Kingdom, the Netherlands, Spain or France recommend or clearly specify that HRQoL should be measured using the EQ-5D \[5, 6\]. Since the release of the EQ-5D-5L – with five response levels - \[7\], extensive research has been conducted to compare the measurement properties of the EQ-5D-3L and EQ-5D-5L (hereafter 3L and 5L, respectively). A recent literature review confirms that both the 3L and the 5L are applicable to a wide range of populations, while confirming improved informativity, less ceiling effects and better distributional properties for the 5L \[8\]. Further studies examined the measures’ feasibility, which was commonly operationalised in terms of missing values and completion rates at the individual level. The former is either defined as unit nonresponse or as item nonresponse, where information is unavailable for the respondent as a whole or just on individual items \[9\]. Whereas the latter construct is defined as the share of computable EQ-5D index values, which requires complete information on all five items of the descriptive system \[10\]. Studies by Janssen et al. \[11\] and Agborsangaya et al. \[12\] reported very good feasibility of both 3L and 5L with missing values of less than 2%, whereas Buchholz et al. \[8\] conclude on a proportion of missing values of less than 5% from reviewing 15 studies.

However, there is evidence to suggest that the proportion of missing values is slightly higher in the older population resulting in lower completion rates of the instrument \[10\]. Even though studies conducted with older respondents \[13–17\] report missing values well within the margin reported by Buchholz et al. \[8\], there are other studies reporting proportions of up to 10% \[18–21\]. On the contrary, the samples in Janssen et al. \[11\], Agborsangaya et al. \[12\] and other studies \[22–24\] were younger than 65 years and reported considerable fewer missing values. Hence, we suspect that the share of missing responses and incomplete descriptive systems may be driven by an age-dependent effect, as this was also described for the SF-36 \[25–27\]. Terwee et al. \[28\] argue that missing values may be indicative of problems with item interpretability, which is confirmed by findings from Hulme et al. \[19\] and van Leeuwen et al. \[29\] who report this kind of response issues on the 3L for older people.

Hence, this study aims to assess the magnitude of missing values and incomplete responses for both the 3L and 5L using five waves of the large-scale General Practitioner Patient Survey (GPPS) based on age-stratified comparisons of these feasibility parameters in the English general population, which allows a within-sample assessment of differences between the older and the younger general public.

## Methods

### Data

For the analysis we utilise individual-level self-reported EQ-5D data from the GPPS \[30\]. This is a large-scale cross-sectional survey undertaken on behalf of the National Health Service (NHS) England. Since 2007 the survey is sent yearly to more than 2 million adults asking them about their experience with their general practitioner and other NHS services. The questionnaire is primarily posted to participants; however, the survey can also be completed online or by telephone. Moreover, it is available in a variety of languages. The overall GPPS samples are obtained by drawing proportionately stratified samples from each practice using registration data held by the NHS Digital database. Individuals are eligible for inclusion in the survey, if they are 18 years or above, hold a valid NHS registration number and were continuously registered with a general practitioner (GP) for at least 6 months \[31\]. Even though respondents are recruited via GP registries, we would like to argue that the underlying sample is in effect recruited from the general population, since registration with a GP does not necessarily imply that respondents are currently under treatment for a condition or an illness.

### Variables

The primary aim of the GPPS survey is to assess patients’ experiences with their GP and other local NHS services; questions include aspects such as access to services, appointments, waiting times and how people manage their health. In addition to that, respondents answer the EQ-5D, which has been used in the survey between 2011 and 2017 \[31\]. The EQ-5D is a standardised generic measure of HRQoL developed by the EuroQol Group. The EQ-5D descriptive system entails five dimensions: mobility, self-care, usual activities, pain or discomfort and anxiety or depression. The initially developed EQ-5D-3L has three response levels, allowing respondents to describe their health status based on three options: no problems (level 1); some or moderate problems (level 2); or extreme problems/unable to (level 3) \[32\]. The EQ-5D-5L is a re-developed version covering the same five dimensions, but expanding the available response options to five levels, again, ranging from no problems (level 1), over slight, moderate and severe problems to extreme problems/unable to (level 5) \[7\]. The response from each dimension-level can be concatenated to form a health profile, which can be linked to a value set – a scoring algorithm with preference-based weights for each dimension-level – to generate a single summary index score \[33\]. The second component of the EQ-5D - the visual analogue scale (EQ VAS) – is not included in the GPPS survey \[34\].

In this study, we pool data from several years. We use data from 2012, as this is the last year the 3L was used, also capturing the effect of changing the instrument to the 5L between the first and the second wave of 2012. Further, we examine data from 2016 and 2017, since this was the most recent data when we applied for the data set. The survey mode was equivalent across all 3 years in the sense that the vast majority of respondents answered the questionnaire paper-based and only 4–6% of the respondents answered using the online survey, while telephone responses were negligible \[30, 35–38\]. Since the publicly available analysis tool does not allow in depth examination of all EQ-5D data, we submitted an application for individual-level data to NHS England. Further, we were granted access to reported background information, which is based on gender, age groups and existence of any of the following long-term conditions: Alzheimer’s disease/ dementia, angina/heart problem, arthritis/joint problem, asthma/chest problem, blindness, cancer, deafness, diabetes, epilepsy, high blood pressure, kidney or liver disease, long-term back problem, long-term mental health problem or long-term neurological problem \[31\]. The information on the administration mode was not included in the individual-level data set and, hence, could not be controlled for.

### Analysis

We examine feasibility of the EQ-5D in older persons in comparison to the general population by investigating distributional properties of EQ-5D data as well as the prevalence and distribution of missing values, which ultimately prevent the calculation of an EQ-5D index value. We do so by conducting descriptive analysis based on the proportion of respondents per level in both 3L and 5L for the whole sample as well as stratified by age groups. We expect to observe a lower proportion of level 1 responses (i.e. at the ceiling) on the 5L in general and more pronounced in respondents aged 65 and above.

As suggested by Janssen et al. \[11\], we examine feasibility for both 3L and 5L in terms of missing values separately for each dimension and stratified for age groups. We further report completion rates based on the same criteria. We analyse the proportion of missing values by age groups using chi-square tests to examine potential associations with age. Given the large-scale of this exercise, we report standardised effect sizes based on Cramer’s V to quantify the magnitude of observed differences \[39\]. We further explored the impact of age, gender and having a long-term health condition on the probability of returning an incomplete EQ-5D using logistic regression analysis. We used “incomplete response” as a binary dependent variable where 1 indicates that at least one EQ-5D item was not answered and, thus, we were unable to calculate an index value. We used ‘female’ and ‘condition’ as binary independent variables, where 1 represents being female or having a long-term condition, respectively. Further, age group was added as a categorical variable into the model with 18–24 years as the reference category. We used STATA’s *margins* post-estimation command to calculate predicted probabilities of returning an incomplete EQ-5D for each age group holding the other variables at their sample means. We apply the conventional significance level of 5%. All analysis was conducted using STATA 16 \[40\].

## Results

### Sample description

After pooling five different waves of the GPPS the total sample comprised 4,358,700 observations. Of those, 1,476,395 contributed to the 3L sample, whereas 2,882,305 respondents were represented in the 5L sample. As Table <a href="#Tab1" data-ref-type="table">1</a> suggests, the sample characteristics were similar across the 3L and 5L sample including slightly more women. About one third of the sample was 65 years and above (3L: 33.8%; 5L: 36.7%) and about 60% reported at least one long-standing health condition. The most prevalent long-term condition was high blood pressure (23%) followed by arthritis or joint problems (16%). Mental health problems including Alzheimer’s disease/dementia and neurological problems were reported by 15.9 and 15.5% for the 3L and 5L sample, respectively.

<div id="Tab1" class="table-wrap">

<div class="caption">

Sample characteristics of five waves of GP Patient survey data

</div>

<table>
<thead>
<tr>
<th rowspan="2">Characteristics</th>
<th colspan="2">EQ-5D-3L sample</th>
<th colspan="2">EQ-5D-5L sample</th>
<th colspan="2">Total</th>
</tr>
<tr>
<th>N</th>
<th>%</th>
<th>N</th>
<th>%</th>
<th>N</th>
<th>%</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">Gender</td>
</tr>
<tr>
<td> Male</td>
<td>636,076</td>
<td>43.1</td>
<td>1,255,846</td>
<td>43.6</td>
<td>1,891,922</td>
<td>43.4</td>
</tr>
<tr>
<td> Female</td>
<td>840,324</td>
<td>56.9</td>
<td>1,626,459</td>
<td>56.4</td>
<td>2,466,783</td>
<td>56.6</td>
</tr>
<tr>
<td colspan="7">Age group</td>
</tr>
<tr>
<td> 18–24 years</td>
<td>65,729</td>
<td>4.5</td>
<td>116,338</td>
<td>4.0</td>
<td>182,067</td>
<td>4.2</td>
</tr>
<tr>
<td> 25–34 years</td>
<td>148,966</td>
<td>10.1</td>
<td>267,430</td>
<td>9.3</td>
<td>416,396</td>
<td>9.6</td>
</tr>
<tr>
<td> 35–44 years</td>
<td>203,616</td>
<td>13.8</td>
<td>363,407</td>
<td>12.6</td>
<td>567,023</td>
<td>13.0</td>
</tr>
<tr>
<td> 45–54 years</td>
<td>259,698</td>
<td>17.6</td>
<td>501,875</td>
<td>17.4</td>
<td>761,573</td>
<td>17.5</td>
</tr>
<tr>
<td> 55–64 years</td>
<td>300,329</td>
<td>20.3</td>
<td>577,672</td>
<td>20.0</td>
<td>878,001</td>
<td>20.1</td>
</tr>
<tr>
<td> 65–74 years</td>
<td>273,922</td>
<td>18.6</td>
<td>595,753</td>
<td>20.7</td>
<td>869,675</td>
<td>20.0</td>
</tr>
<tr>
<td> 75–84 years</td>
<td>169,686</td>
<td>11.5</td>
<td>347,876</td>
<td>12.1</td>
<td>517,562</td>
<td>11.9</td>
</tr>
<tr>
<td> 85 or over</td>
<td>54,454</td>
<td>3.7</td>
<td>111,954</td>
<td>3.9</td>
<td>166,408</td>
<td>3.8</td>
</tr>
<tr>
<td colspan="7">Long-standing health condition</td>
</tr>
<tr>
<td> Yes</td>
<td>895,175</td>
<td>60.6</td>
<td>1,771,617</td>
<td>61.5</td>
<td>2,666,792</td>
<td>61.2</td>
</tr>
<tr>
<td> No</td>
<td>535,210</td>
<td>36.3</td>
<td>1,022,939</td>
<td>35.5</td>
<td>1,558,149</td>
<td>35.8</td>
</tr>
<tr>
<td> Don’t know/ can’t say</td>
<td>27,722</td>
<td>1.9</td>
<td>58,320</td>
<td>2.0</td>
<td>86,042</td>
<td>2.0</td>
</tr>
<tr>
<td> Missing</td>
<td>18,293</td>
<td>1.2</td>
<td>29,429</td>
<td>1.0</td>
<td>47,722</td>
<td>1.1</td>
</tr>
<tr>
<td colspan="7">Long-term condition</td>
</tr>
<tr>
<td> Alzheimer/ dementia</td>
<td>9929</td>
<td>0.7</td>
<td>21,101</td>
<td>0.7</td>
<td>31,030</td>
<td>0.7</td>
</tr>
<tr>
<td> Angina/ heart problems</td>
<td>96,707</td>
<td>6.6</td>
<td>179,424</td>
<td>6.2</td>
<td>276,131</td>
<td>6.3</td>
</tr>
<tr>
<td> Arthritis/ joint problems</td>
<td>240,480</td>
<td>16.3</td>
<td>466,970</td>
<td>16.2</td>
<td>707,450</td>
<td>16.2</td>
</tr>
<tr>
<td> Asthma/ chest problems</td>
<td>147,325</td>
<td>10.0</td>
<td>297,099</td>
<td>10.3</td>
<td>444,424</td>
<td>10.2</td>
</tr>
<tr>
<td> Blindness/ visual problems</td>
<td>18,500</td>
<td>1.3</td>
<td>32,530</td>
<td>1.1</td>
<td>51,030</td>
<td>1.2</td>
</tr>
<tr>
<td> Cancer in the last 5 yrs</td>
<td>54,362</td>
<td>3.7</td>
<td>118,398</td>
<td>4.1</td>
<td>172,760</td>
<td>4.0</td>
</tr>
<tr>
<td> Deaf/ hearing problems</td>
<td>70,311</td>
<td>4.8</td>
<td>139,745</td>
<td>4.9</td>
<td>210,056</td>
<td>4.8</td>
</tr>
<tr>
<td> Diabetes</td>
<td>123,405</td>
<td>8.4</td>
<td>266,795</td>
<td>9.3</td>
<td>390,200</td>
<td>9.0</td>
</tr>
<tr>
<td> Epilepsy</td>
<td>15,531</td>
<td>1.1</td>
<td>28,152</td>
<td>1.0</td>
<td>43,683</td>
<td>1.0</td>
</tr>
<tr>
<td> High blood pressure</td>
<td>337,554</td>
<td>22.9</td>
<td>668,507</td>
<td>23.2</td>
<td>1,006,061</td>
<td>23.1</td>
</tr>
<tr>
<td> Kidney or liver problems</td>
<td>25,649</td>
<td>1.7</td>
<td>56,508</td>
<td>2.0</td>
<td>82,157</td>
<td>1.9</td>
</tr>
<tr>
<td> Long-term back problems</td>
<td>157,361</td>
<td>10.7</td>
<td>306,127</td>
<td>10.6</td>
<td>463,488</td>
<td>10.6</td>
</tr>
<tr>
<td> Long-term mental health problems</td>
<td>51,121</td>
<td>3.5</td>
<td>119,783</td>
<td>4.2</td>
<td>170,904</td>
<td>3.9</td>
</tr>
<tr>
<td> Long-term neurological problems</td>
<td>26,744</td>
<td>1.8</td>
<td>60,278</td>
<td>2.1</td>
<td>87,022</td>
<td>2.0</td>
</tr>
<tr>
<td> Long-term other health problems</td>
<td>172,282</td>
<td>11.7</td>
<td>366,061</td>
<td>12.7</td>
<td>538,343</td>
<td>12.4</td>
</tr>
</tbody>
</table>

</div>

### Comparison of response distribution

Tables <a href="#Tab2" data-ref-type="table">2</a> and <a href="#Tab3" data-ref-type="table">3</a> provide an overview of the response distribution for each dimension stratified by age groups for both the 3L and 5L, respectively. Unsurprisingly, problems were always least prevalent in the youngest age groups with a monotonically increasing trend with increasing age. Problems were more frequently reported when using the 5L and limitations were spread wider across the severity range. Generally, self-care appears to be the least affected dimension with a considerable ceiling effect. Even in the highest age group only 40% report any problems with self-care, whereas 82% report problems in mobility and pain or discomfort in that age group. Interestingly, problems with pain or discomfort and anxiety or depression were the most frequent in younger age groups (around 30% vs. self-care 5% vs. mobility 9%). While limitations in pain or discomfort increase considerably with age, the proportion of any reported problems in anxiety or depression remains fairly stable; this pattern is constant across both EQ-5D versions. Overall, floor effects, where respondents respond with the worst answer category, are not observable in this general population sample. Severe and extreme problems are least prevalent in the dimensions self-care and anxiety or depression. However, while severe and extreme problems with self-care increase with age the opposite seems to be the case for anxiety or depression. Again, this pattern is consistent across both the 3L and 5L, with the exception being level 3 in mobility in the 3L (‘confined to bed’), which was the least frequent overall.

<div id="Tab2" class="table-wrap">

<div class="caption">

Distribution of EQ-5D-5L responses by dimension and age group

</div>

<table>
<thead>
<tr>
<th colspan="2">Parameter</th>
<th>Total</th>
<th colspan="8">Age group<br />
Proportion in %</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dimension</strong></td>
<td><strong>Level</strong></td>
<td>N</td>
<td>18–24</td>
<td>25–34</td>
<td>35–44</td>
<td>45–54</td>
<td>55–64</td>
<td>65–74</td>
<td>75–84</td>
<td>85+</td>
</tr>
<tr>
<td rowspan="5"><strong>Mobility</strong></td>
<td>No problems</td>
<td>1,958,750</td>
<td>91.2</td>
<td>90.2</td>
<td>86.2</td>
<td>78.5</td>
<td>68.6</td>
<td>58.8</td>
<td>39.6</td>
<td>18.0</td>
</tr>
<tr>
<td>Slight problems</td>
<td>403,522</td>
<td>4.6</td>
<td>5.0</td>
<td>7.0</td>
<td>10.5</td>
<td>14.7</td>
<td>18.9</td>
<td>23.9</td>
<td>23.0</td>
</tr>
<tr>
<td>Moderate problems</td>
<td>268,905</td>
<td>1.6</td>
<td>1.8</td>
<td>2.9</td>
<td>5.3</td>
<td>8.5</td>
<td>12.2</td>
<td>20.3</td>
<td>29.2</td>
</tr>
<tr>
<td>Severe problems</td>
<td>170,235</td>
<td>0.6</td>
<td>0.8</td>
<td>1.6</td>
<td>3.4</td>
<td>5.7</td>
<td>7.3</td>
<td>12.1</td>
<td>22.0</td>
</tr>
<tr>
<td>Unable to</td>
<td>22,630</td>
<td>0.4</td>
<td>0.4</td>
<td>0.4</td>
<td>0.5</td>
<td>0.6</td>
<td>0.7</td>
<td>1.3</td>
<td>4.1</td>
</tr>
<tr>
<td rowspan="5"><strong>Self-care</strong></td>
<td>No problems</td>
<td>2,484,621</td>
<td>94.9</td>
<td>94.7</td>
<td>92.9</td>
<td>89.6</td>
<td>86.2</td>
<td>84.3</td>
<td>76.6</td>
<td>60.2</td>
</tr>
<tr>
<td>Slight problems</td>
<td>149,380</td>
<td>1.7</td>
<td>1.8</td>
<td>2.5</td>
<td>3.7</td>
<td>5.0</td>
<td>6.1</td>
<td>9.5</td>
<td>15.0</td>
</tr>
<tr>
<td>Moderate problems</td>
<td>118,583</td>
<td>1.0</td>
<td>1.0</td>
<td>1.6</td>
<td>3.0</td>
<td>4.4</td>
<td>5.0</td>
<td>7.2</td>
<td>12.5</td>
</tr>
<tr>
<td>Severe problems</td>
<td>41,437</td>
<td>0.4</td>
<td>0.4</td>
<td>0.7</td>
<td>1.2</td>
<td>1.7</td>
<td>1.6</td>
<td>2.0</td>
<td>4.7</td>
</tr>
<tr>
<td>Unable to</td>
<td>20,059</td>
<td>0.4</td>
<td>0.4</td>
<td>0.4</td>
<td>0.4</td>
<td>0.5</td>
<td>0.5</td>
<td>1.2</td>
<td>4.3</td>
</tr>
<tr>
<td rowspan="5"><strong>Usual activities</strong></td>
<td>No problems</td>
<td>1,943,526</td>
<td>85.3</td>
<td>85.4</td>
<td>81.8</td>
<td>75.0</td>
<td>67.7</td>
<td>61.4</td>
<td>45.3</td>
<td>24.6</td>
</tr>
<tr>
<td>Slight problems</td>
<td>446,180</td>
<td>7.8</td>
<td>7.9</td>
<td>9.5</td>
<td>12.6</td>
<td>15.9</td>
<td>19.3</td>
<td>24.3</td>
<td>24.3</td>
</tr>
<tr>
<td>Moderate problems</td>
<td>259,886</td>
<td>3.3</td>
<td>3.0</td>
<td>4.0</td>
<td>6.1</td>
<td>8.6</td>
<td>10.9</td>
<td>17.2</td>
<td>25.0</td>
</tr>
<tr>
<td>Severe problems</td>
<td>114,562</td>
<td>1.2</td>
<td>1.3</td>
<td>1.9</td>
<td>3.1</td>
<td>4.4</td>
<td>4.5</td>
<td>6.4</td>
<td>11.5</td>
</tr>
<tr>
<td>Unable to</td>
<td>55,120</td>
<td>0.6</td>
<td>0.6</td>
<td>0.8</td>
<td>1.1</td>
<td>1.5</td>
<td>1.7</td>
<td>3.9</td>
<td>10.9</td>
</tr>
<tr>
<td rowspan="5"><strong>Pain/Discomfort</strong></td>
<td>No</td>
<td>1,272,899</td>
<td>72.4</td>
<td>68.6</td>
<td>60.3</td>
<td>49.3</td>
<td>40.3</td>
<td>33.6</td>
<td>24.6</td>
<td>18.0</td>
</tr>
<tr>
<td>Slight</td>
<td>874,407</td>
<td>18.2</td>
<td>20.7</td>
<td>24.9</td>
<td>29.7</td>
<td>33.2</td>
<td>33.6</td>
<td>34.6</td>
<td>31.2</td>
</tr>
<tr>
<td>Moderate</td>
<td>460,993</td>
<td>5.6</td>
<td>6.4</td>
<td>8.7</td>
<td>12.4</td>
<td>16.1</td>
<td>20.0</td>
<td>26.7</td>
<td>33.8</td>
</tr>
<tr>
<td>Severe</td>
<td>171,788</td>
<td>1.5</td>
<td>2.0</td>
<td>3.1</td>
<td>4.9</td>
<td>6.8</td>
<td>7.3</td>
<td>9.5</td>
<td>11.3</td>
</tr>
<tr>
<td>Extreme</td>
<td>39,224</td>
<td>0.4</td>
<td>0.6</td>
<td>1.0</td>
<td>1.6</td>
<td>1.8</td>
<td>1.4</td>
<td>15</td>
<td>2.0</td>
</tr>
<tr>
<td rowspan="5"><strong>Anxiety/Depression</strong></td>
<td>No</td>
<td>1,879,193</td>
<td>67.0</td>
<td>68.6</td>
<td>67.5</td>
<td>64.5</td>
<td>64.5</td>
<td>67.3</td>
<td>62.0</td>
<td>53.6</td>
</tr>
<tr>
<td>Slight</td>
<td>556,159</td>
<td>17.3</td>
<td>17.7</td>
<td>18.4</td>
<td>19.4</td>
<td>19.4</td>
<td>19.0</td>
<td>20.7</td>
<td>24.1</td>
</tr>
<tr>
<td>Moderate</td>
<td>252,616</td>
<td>9.0</td>
<td>8.0</td>
<td>8.0</td>
<td>9.2</td>
<td>9.4</td>
<td>7.8</td>
<td>8.9</td>
<td>12.4</td>
</tr>
<tr>
<td>Severe</td>
<td>61,933</td>
<td>3.1</td>
<td>2.4</td>
<td>2.4</td>
<td>2.9</td>
<td>2.6</td>
<td>1.3</td>
<td>1.2</td>
<td>1.6</td>
</tr>
<tr>
<td>Extreme</td>
<td>30,483</td>
<td>1.7</td>
<td>1.3</td>
<td>1.4</td>
<td>1.6</td>
<td>1.2</td>
<td>0.5</td>
<td>0.5</td>
<td>0.7</td>
</tr>
</tbody>
</table>

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

Distribution of EQ-5D-3L responses by dimension and age group

</div>

<table>
<thead>
<tr>
<th colspan="2">Parameter</th>
<th>Total</th>
<th colspan="8">Age group<br />
Proportion in %</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dimension</strong></td>
<td><strong>Level</strong></td>
<td>N</td>
<td>18–24</td>
<td>25–34</td>
<td>35–44</td>
<td>45–54</td>
<td>55–64</td>
<td>65–74</td>
<td>75–84</td>
<td>85+</td>
</tr>
<tr>
<td rowspan="3"><strong>Mobility</strong></td>
<td>No problems</td>
<td>1,074,533</td>
<td>92.7</td>
<td>92.0</td>
<td>88.2</td>
<td>82.0</td>
<td>73.2</td>
<td>63.6</td>
<td>45.5</td>
<td>23.1</td>
</tr>
<tr>
<td>Some problems</td>
<td>362,930</td>
<td>4.9</td>
<td>5.7</td>
<td>9.3</td>
<td>15.6</td>
<td>24.5</td>
<td>33.6</td>
<td>51.0</td>
<td>72.5</td>
</tr>
<tr>
<td>Confined to bed</td>
<td>4545</td>
<td>0.3</td>
<td>0.3</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.5</td>
<td>1.7</td>
</tr>
<tr>
<td rowspan="3"><strong>Self-care</strong></td>
<td>No problems</td>
<td>1,307,043</td>
<td>95.6</td>
<td>95.5</td>
<td>93.8</td>
<td>91.4</td>
<td>88.8</td>
<td>86.2</td>
<td>79.9</td>
<td>64.7</td>
</tr>
<tr>
<td>Some problems</td>
<td>118,593</td>
<td>2.0</td>
<td>2.2</td>
<td>3.7</td>
<td>6.0</td>
<td>8.4</td>
<td>10.2</td>
<td>14.3</td>
<td>25.0</td>
</tr>
<tr>
<td>Unable to</td>
<td>11,759</td>
<td>0.4</td>
<td>0.4</td>
<td>0.4</td>
<td>0.4</td>
<td>0.5</td>
<td>0.7</td>
<td>1.6</td>
<td>5.5</td>
</tr>
<tr>
<td rowspan="3"><strong>Usual activities</strong></td>
<td>No problems</td>
<td>1,061,308</td>
<td>88.1</td>
<td>87.9</td>
<td>83.6</td>
<td>77.8</td>
<td>71.6</td>
<td>66.3</td>
<td>51.3</td>
<td>30.4</td>
</tr>
<tr>
<td>Some problems</td>
<td>332,279</td>
<td>8.9</td>
<td>9.2</td>
<td>12.8</td>
<td>18.0</td>
<td>23.7</td>
<td>27.9</td>
<td>38.5</td>
<td>49.6</td>
</tr>
<tr>
<td>Unable to</td>
<td>47,921</td>
<td>0.9</td>
<td>1.0</td>
<td>1.5</td>
<td>2.2</td>
<td>2.8</td>
<td>3.4</td>
<td>6.5</td>
<td>15.6</td>
</tr>
<tr>
<td rowspan="3"><strong>Pain/Discomfort</strong></td>
<td>No</td>
<td>780,144</td>
<td>73.1</td>
<td>76.3</td>
<td>68.8</td>
<td>58.5</td>
<td>49.2</td>
<td>40.8</td>
<td>29.9</td>
<td>22.6</td>
</tr>
<tr>
<td>Moderate</td>
<td>571,456</td>
<td>17.5</td>
<td>19.8</td>
<td>25.6</td>
<td>33.7</td>
<td>41.6</td>
<td>49.0</td>
<td>57.5</td>
<td>63.1</td>
</tr>
<tr>
<td>Extreme</td>
<td>84,005</td>
<td>1.3</td>
<td>1.7</td>
<td>3.2</td>
<td>5.4</td>
<td>7.0</td>
<td>7.2</td>
<td>8.4</td>
<td>9.6</td>
</tr>
<tr>
<td rowspan="3"><strong>Anxiety/Depression</strong></td>
<td>Not</td>
<td>1,057,588</td>
<td>78.6</td>
<td>77.7</td>
<td>74.4</td>
<td>70.7</td>
<td>70.8</td>
<td>71.9</td>
<td>66.8</td>
<td>59.3</td>
</tr>
<tr>
<td>Moderately</td>
<td>314,019</td>
<td>16.1</td>
<td>17.2</td>
<td>19.4</td>
<td>22.3</td>
<td>22.5</td>
<td>20.9</td>
<td>23.4</td>
<td>29.5</td>
</tr>
<tr>
<td>Extremely</td>
<td>38,506</td>
<td>2.7</td>
<td>2.6</td>
<td>3.2</td>
<td>3.7</td>
<td>3.0</td>
<td>1.5</td>
<td>1.4</td>
<td>2.1</td>
</tr>
</tbody>
</table>

</div>

### Feasibility of the EQ-5D-3L and 5L

Table <a href="#Tab4" data-ref-type="table">4</a> summarises the share of missing values and completion rates by age groups based on the 3L and 5L. Overall, the proportion of missing values in any of the EQ-5D dimensions was very low but increasing with age. Chi-square tests suggest that the proportion of missing values in any dimension are not independent of the respondents’ age (*p* \< 0.001). Given the large sample size, this test result is not surprising and mitigated by the negligible association (Cramér’s V). Nonetheless, it appears as if there is a steeper increase in the last two age categories. The highest proportions were found in anxiety or depression for respondents 65 years and above, where the proportion of missing responses peaks at 7.6% (5L) and 9.1% (3L) for the oldest respondents. Apart from this, the proportion of missing responses is less than 5% across all dimensions, and generally lower for the 5 L in comparison to the 3L. Missing value patterns stratified for age groups can be found in the Appendix (see Appendix Tables <a href="#MOESM1" data-ref-type="media">A1</a> and <a href="#MOESM1" data-ref-type="media">A2</a>). Among those respondents with missing values, patterns with just one missing item account for ~ 60–70% depending on age and EQ-5D version. Moreover, patterns with two to four missing responses only accumulate between 22 up to 30% of respondents with missings. Interestingly, the proportion of complete non-response to both 3L and 5L is highest among young adults (18–24 years - 5 L: 19.8%; 3L: 18.4%) and drastically decreases with higher age (85 years and over - 5 L: 2.8%; 3L: 2.6%).

<div id="Tab4" class="table-wrap">

<div class="caption">

Proportion of missing values and overall EQ-5D completion rate stratified by age and EQ-5D version

</div>

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Missing</th>
<th colspan="8">Age group<br />
Proportion in %</th>
<th>Cramér’s V</th>
</tr>
</thead>
<tbody>
<tr>
<td>EQ-5D-5L</td>
<td>N (%)</td>
<td><strong>18–24</strong></td>
<td><strong>25–34</strong></td>
<td><strong>35–44</strong></td>
<td><strong>45–54</strong></td>
<td><strong>55–64</strong></td>
<td><strong>65–74</strong></td>
<td><strong>75–84</strong></td>
<td><strong>85+</strong></td>
<td></td>
</tr>
<tr>
<td> Mobility</td>
<td>58,263 (2.02)</td>
<td>1.61</td>
<td>1.68</td>
<td>1.89</td>
<td>1.88</td>
<td>1.89</td>
<td>2.04</td>
<td>2.71</td>
<td>2.72</td>
<td>0.0229</td>
</tr>
<tr>
<td> Self-care</td>
<td>68,225 (2.37)</td>
<td>1.66</td>
<td>1.72</td>
<td>1.98</td>
<td>2.07</td>
<td>2.22</td>
<td>2.57</td>
<td>3.52</td>
<td>3.37</td>
<td>0.0363</td>
</tr>
<tr>
<td> Usual activities</td>
<td>63,034 (2.19)</td>
<td>1.85</td>
<td>1.88</td>
<td>2.06</td>
<td>2.00</td>
<td>1.94</td>
<td>2.11</td>
<td>2.98</td>
<td>3.76</td>
<td>0.0310</td>
</tr>
<tr>
<td> Pain/Discomfort</td>
<td>62,994 (2.19)</td>
<td>1.82</td>
<td>1.82</td>
<td>2.05</td>
<td>2.03</td>
<td>1.93</td>
<td>2.08</td>
<td>3.05</td>
<td>3.78</td>
<td>0.0328</td>
</tr>
<tr>
<td> Anxiety/Depression</td>
<td>101,921 (3.54)</td>
<td>1.98</td>
<td>2.01</td>
<td>2.37</td>
<td>2.46</td>
<td>2.89</td>
<td>4.12</td>
<td>6.78</td>
<td>7.56</td>
<td>0.0897</td>
</tr>
<tr>
<td>Completion rate</td>
<td>93.11%</td>
<td>96.01</td>
<td>95.89</td>
<td>95.18</td>
<td>94.68</td>
<td>94.06</td>
<td>92.24</td>
<td>87.78</td>
<td>85.92</td>
<td>0.1103</td>
</tr>
<tr>
<td colspan="11">EQ-5D-3L</td>
</tr>
<tr>
<td> Mobility</td>
<td>34,391 (2.33)</td>
<td>2.10</td>
<td>2.05</td>
<td>2.24</td>
<td>2.18</td>
<td>2.07</td>
<td>2.53</td>
<td>3.00</td>
<td>2.77</td>
<td>0.0205</td>
</tr>
<tr>
<td> Self-care</td>
<td>39,003 (2.64)</td>
<td>1.98</td>
<td>1.97</td>
<td>2.21</td>
<td>2.20</td>
<td>2.27</td>
<td>2.89</td>
<td>4.22</td>
<td>4.86</td>
<td>0.0496</td>
</tr>
<tr>
<td> Usual activities</td>
<td>34,890 (2.36)</td>
<td>2.06</td>
<td>2.03</td>
<td>2.15</td>
<td>2.01</td>
<td>1.87</td>
<td>2.43</td>
<td>3.68</td>
<td>4.42</td>
<td>0.0441</td>
</tr>
<tr>
<td> Pain/Discomfort</td>
<td>40,795 (2.76)</td>
<td>2.19</td>
<td>2.18</td>
<td>2.48</td>
<td>2.42</td>
<td>2.29</td>
<td>2.98</td>
<td>4.26</td>
<td>4.61</td>
<td>0.0439</td>
</tr>
<tr>
<td> Anxiety/Depression</td>
<td>66,287 (4.49)</td>
<td>2.66</td>
<td>2.54</td>
<td>2.99</td>
<td>3.28</td>
<td>3.79</td>
<td>5.69</td>
<td>8.36</td>
<td>9.14</td>
<td>0.0963</td>
</tr>
<tr>
<td>Completion rate</td>
<td>91.57%</td>
<td>94.88</td>
<td>94.91</td>
<td>93.98</td>
<td>93.39</td>
<td>92.70</td>
<td>89.83</td>
<td>85.20</td>
<td>83.14</td>
<td>0.1199</td>
</tr>
</tbody>
</table>

</div>

Further, we report completion rates based on age groups, i.e. proportion of respondents with all five items completed (see also Table <a href="#Tab4" data-ref-type="table">4</a>). Across all age groups the 5L completion rate was found to be higher in comparison to the 3L and for both completion was negatively associated with age, however, this effect was very weak. While on average only 4% of the 5L utilities cannot be calculated in the youngest age group, this figure increases to more than 14% in those 85 years and above. Correspondingly, these figures range from 5% (18–24 years) to 16.8% (85+ years) for the 3L.

Figure <a href="#Fig1" data-ref-type="fig">1</a> presents predicted probabilities for returning an incomplete 3L or 5L for each age group controlling for gender and the presence of any reported long-term condition. Firstly, the probability of an incomplete EQ-5D response was lowest in the age group 25–34 years for the 3L (5.3%) and for the 5L (4.3%) in those 18–24 years, respectively. Up until the age of 64, the probability only marginally increased by 1.2 percentage points for both the 3L and 5L. However, beyond the age of 64 years the probability of an incomplete EQ-5D response accelerated quickly peaking at 13.9% for the 3L and 11.5% for the 5L in those being 85 years and above. Secondly, the probability of an incomplete response was found to be lower at any given age for the 5L in comparison to the 3L. The difference was between 1.0 (25–34 years) and 2.4 (85 or over) percentage points (see Fig. <a href="#Fig1" data-ref-type="fig">1</a>) with the spread being wider after the age of 64 years.

<figure id="Fig1">
<p><img src="13561_2022_374_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Predicted probabilities for returning incomplete EQ-5D-3L or 5L based on age groups using logistic regression</figcaption>
</figure>

## Discussion

The aim of this study was to assess feasibility of the 3L and 5L for older respondents in direct comparison to younger adults in the general population. The 5L showed better feasibility than the 3L across all age groups. The superiority of the 5L was more noticeable in older age groups, which was indicated by fewer missing values, higher completion rates and an overall lower likelihood of an incomplete response to the descriptive system.

With respect to the descriptive system we observe an improved response distribution when measured with the 5L as compared to the 3L version. As one might expect, the proportion of respondents at the ceiling is lower on the 5L and further decreasing with increasing age. This finding is consistent with other studies comparing the 3L and 5L version \[8, 11\]. Similarly, the response distribution in individual dimensions in the older population was also similar to that found in earlier studies, where self-care is the least informative dimension, whereas pain or discomfort is the most informative. Again, the response distribution in anxiety or depression does not seem to be moderated by age in both 3L and 5L \[41–43\].

The cross tabulation of incomplete responses per dimension with age categories clearly shows an increasing trend in higher age groups (Table <a href="#Tab4" data-ref-type="table">4</a>). Generally, our findings are in line with proportions of missing values reported earlier \[11, 12\]. Especially in younger age groups we rarely observe more than 2% missing values per dimension, whereas the proportions are only marginally higher in older age and fall well within the overall margin reported in Buchholz et al. \[8\]. As an exception to this rule, we observed a higher proportion of missing values in the dimension of anxiety or depression, which go as high as 7.6% (5L) and 9.1% (3L) in those being 85 years and over. Holland and colleagues \[44\] report that this dimension caused some embarrassment in older respondents. This may partially explain the higher prevalence of missing values in that particular dimension. Moreover, we found that in each dimension and for any given age group the proportion of missing responses was lower for the 5L – even though the difference was less than half a percent. This findings are also in line with earlier studies \[8, 17, 45\].

While the share of missing response was relatively low at the dimension-level, the completion rate, i.e. the ability to generate the utility value from the respondent’s reported health state, was just above 90% on the total sample for both 3L and 5L. A potential explanation for this observation may be that missing values resulted from relatively many individuals with just one missing item rather than from respondents with multiple missing responses, which was suggested by the analysis of missing value patterns (see Appendix Tables <a href="#MOESM1" data-ref-type="media">A1</a> and <a href="#MOESM1" data-ref-type="media">A2</a>). Moreover, completion of the 3L and 5L decreased by approximately 10 percentage points from the youngest to the oldest age group and more rapidly after the age of 64 years. For the total sample, we find that our observed completion rates for the 3L and 5L are about 5 percentage points lower than those reported in other studies in the general population \[12, 46–49\]. Considering the older population, 3L completion rates were 5–10 percentage points lower than those reported in a study from Switzerland, which also reports age group-specific completion \[50\]. However, the differences in the data collection process may largely account for this variance, since Luthy et al. \[50\] used computer-assisted personal interviews to collect data instead of self-reports as was the case in this sample. Overall, literature on the feasibility properties of the 3L and 5L in the general public is scarce, where completion rates are predominantly reported for the overall sample. We are unaware of other studies providing age-specific completion rates, which limits further comparison with our findings.

We further provide predicted probabilities for an incomplete response based on a logistic regression model controlling for age groups, gender and presence of a long-term condition. The predicted probabilities largely follow the pattern from the uncontrolled cross-tabulations (Table <a href="#Tab4" data-ref-type="table">4</a>) confirming the hypothesis of an age-dependent impact on the EQ-5D’s completion with a more pronounced effect beyond the age of 64 years. Importantly, the 5L performs better than the 3L in the sense that the predicted probability of returning an incomplete descriptive system is consistently lower for the 5L. Evidence from the literature suggests that the length of the response scale has an effect on the data quality \[51\]. The question-answer process may be distorted, if the intended response does not match the available response options, which may cause the respondent to refuse to answer \[29, 52\]. Hence, it may be assumed that the lack of sensitivity in the 3L is in part responsible for the higher prevalence of missing values in the descriptive system, since respondents may lack the ability to report an appropriate level of problems on the three-level scale. Therefore, the improved sensitivity of the 5L \[53, 54\] may lead to improved feasibility as well, which is supported by our findings of better feasibility of the 5L in terms of reduced missing values, higher completion rates and lower probability of reporting an incomplete descriptive system. This notion is further underpinned by findings from Janssen and colleagues \[55\], where respondents argued that the 5L was easier to use and better reflects their response in comparison to the 3L.

Depending on the purpose of future studies, the slightly higher propensity for missing responses among aged respondents may have different implications. If the aim is to collect HRQoL data in a limited sample and to calculate quality-adjusted life years, researchers could consider assisted or interviewer-based approaches to mitigate the risk of bias due to incomplete response from older respondents \[13, 56, 57\]. At the same time, applying interviewer-based approaches may come at the cost of introducing other types of biases such as interviewer effects, socially desirable answers or a reduced willingness to disclose sensitive information, which may trade-off the gains of increased completeness \[58\]. However, on an aggregate level, such as in a population health survey like the GPPS, the extent of missing values can be rated as good or negligible \[8, 11\]. Nevertheless, our results suggest that missing values vary systematically by age groups and were more prevalent in older adults. This ultimately implies a bias in estimated utility values against older respondents, which needs to be addressed adequately in statistical analyses.

A strength of our study is the huge sample size, which we gained by pooling data from several years of a consistent population health survey. In addition to that, we are able to compare responses to the descriptive system of both versions of the EQ-5D and across all age groups, however, it was not possible to compare the 3L and 5L on a like-for-like comparison, since respondents did not complete both measures. Due to the origin of the data, we had no information on how independently respondents answered the EQ-5D, i.e. whether respondents may have received help filling in the questionnaire and, hence, the level of feasibility problems for a self-report survey may be underestimated. A major limitation of our study is the missing EQ VAS component, which was not included in the survey and, hence, we were unable to investigate its feasibility properties. An in-depth analysis of the EQ VAS’ feasibility properties in the general population seems desirable, since it is known to present problems to older adults \[10\]. Similarly, a qualitative study may facilitate a better understanding of the differences in feasibility properties between the 3L and 5L, which would also be welcomed for the EQ VAS. Future research should further explore the impact of different administration modes, i.e. paper-based vs. online completion, as we were not able to control for this factor even though the sample size would have been sufficient. Additionally, the GPPS data may allow an in-depth exploration od the impact of different long-term conditions on completion of both EQ-5D versions.

## Conclusion

Evidence from our study suggests that both the 3L and 5L have good feasibility properties. The proportion of missing values is acceptable and low across all age groups. However, in comparison to younger populations there appears to be a higher proportion of respondents with incomplete responses, thus resulting in lower completion rates. Predicted probabilities for an incomplete response significantly increased beyond the age of 64 years for both versions of the EQ-5D, indicating a higher likelihood of missing values. Generally, we conclude that either version of the EQ-5D is applicable and feasible in the older population. However, the 5L version compares more favourably in terms of missing values, completion rates as well as with regard to the expected probability of an incomplete descriptive system.

## Supplementary Information

<div class="caption">

**Additional file 1.**

</div>

### Abbreviations

3L  
EQ-5D-3L

5L  
EQ-5D-5L

EQ VAS  
EQ-5D visual analogue scale

GP  
General practitioner

GPPS  
General Practitioner Patient Survey

HRQoL  
Health-related quality of life

NHS  
National Health Service

### Acknowledgements

The GP Patient survey is run by NHS England and NHS Improvement, who provided the data included in this paper. The views expressed by the authors do not necessarily reflect the view of the EuroQol Group.

### Authors’ contributions

OM and WG contributed to the conception of the work. OM applied for the data as well as analysed and interpreted the data; WG provided critical feedback to the analyses. OM drafted the manuscript. WG revised the manuscript. OM and WG read and approved the final manuscript.

### Funding

Open Access funding enabled and organized by Projekt DEAL. This study was funded by EuroQol (grant number: 2015200).

### Availability of data and materials

The data that support the findings of this study are available from NHS England but restrictions apply to the availability of these data, which were used under license for the current study, and so are not publicly available. Data are however available from the authors upon reasonable request and with permission of NHS England.

### Declarations

#### Ethics approval and consent to participate

This study is part of a larger research study, which was approved by the Ethics Committee of Bielefeld University, Number 2017–207. All analyses are based on anonymised secondary data and did not require additional research ethics approval.

#### Consent for publication

Not applicable.

#### Competing interests

OM and WG are members of the EuroQol Group. There are no other conflicts of interest.

## References

1. Guyatt GH, Feeny DH, Patrick DL. Measuring health-related quality of life. Ann Intern Med. 1993;118(8):622–629. doi:10.7326/0003-4819-118-8-199304150-00009

2. Devlin NJ, Appleby J. Getting the most out of PROMS: putting health outcomes at the heart of NHS decision-making: the king’s fund. 2010.

3. National Institute for Health and Care Excellence. Shared decision making: NICE guideline. 2021.

4. Devlin NJ, Brooks R. EQ-5D and the EuroQol group: past, present and future. Appl Health Econ Health Policy. 2017;15(2):127–137. doi:10.1007/s40258-017-0310-5

5. Rowen D, Azzabi Zouraq I, Chevrou-Severac H, van Hout B. International regulations and recommendations for utility data for health technology assessment. Pharmacoeconomics. 2017;35(S1):11–19. doi:10.1007/s40273-017-0544-y

6. Haute Autorité de Santé. Choices in Methods for Economic Evaluation. 2012.

7. Herdman M, Gudex C, Lloyd A, Janssen MF, Kind P, Parkin D, Bonsel G, Badia X. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

8. Buchholz I, Janssen MF, Kohlmann T, Feng Y-S. A systematic review of studies comparing the measurement properties of the three-level and five-level versions of the EQ-5D. Pharmacoeconomics. 2018;36(6):645–661. doi:10.1007/s40273-018-0642-5

9. de Leeuw ED. Reducing missing data in surveys: an overview of methods. Qual Quant. 2001;35:147–160. doi:10.1023/A:1010395805406

10. Marten O, Brand L, Greiner W. Feasibility of the EQ-5D in the elderly population: a systematic review of the literature. Qual Life Res. 2021;31(6):1621–1637. doi:10.1007/s11136-021-03007-9

11. Janssen MF, Pickard AS, Golicki D, Gudex C, Niewada M, Scalone L, Swinburn P, Busschbach J. Measurement properties of the EQ-5D-5L compared to the EQ-5D-3L across eight patient groups: a multi-country study. Qual Life Res. 2013;22(7):1717–1727. doi:10.1007/s11136-012-0322-4

12. Agborsangaya CB, Lahtinen M, Cooke T, Johnson JA. Comparing the EQ-5D 3L and 5L: measurement properties and association with chronic conditions and multimorbidity in the general population. Health Qual Life Outcomes. 2014;12(1):74. doi:10.1186/1477-7525-12-74

13. Coast J, Peters TJ, Richards SH, Gunnell DJ. Use of the EuroQoL among elderly acute care patients. Qual Life Res. 1998;7:1–10. doi:10.1023/a:1008857203434

14. Kunz S. Psychometric properties of the EQ-5D in a study of people with mild to moderate dementia. Qual Life Res. 2010;19(3):425–434. doi:10.1007/s11136-010-9600-1

15. Orgeta V, Edwards RT, Hounsome B, Orrell M, Woods B. The use of the EQ-5D as a measure of health-related quality of life in people with dementia and their carers. Qual Life Res. 2015;24(2):315–324. doi:10.1007/s11136-014-0770-0

16. Davis JC, Liu-Ambrose T, Richardson CG, Bryan S. A comparison of the ICECAP-O with EQ-5D in a falls prevention clinical setting: are they complements or substitutes?. Qual Life Res. 2013;22(5):969–977. doi:10.1007/s11136-012-0225-4

17. Christiansen ASJ, Møller MLS, Kronborg C, Haugan KJ, Køber L, Højberg S, Brandes A, Graff C, Diederichsen SZ, Nielsen JB, Krieger D, Holst AG, Svendsen JH. Comparison of the three-level and the five-level versions of the EQ-5D. Eur J Health Econ. 2021;22(4):621–628. doi:10.1007/s10198-021-01279-z

18. Brazier JE, Walters SJ, Nicholl JP, Kohler B. Using the SF-36 and Euroqol on an elderly population. Qual Life Res. 1996;5(2):195–204. doi:10.1007/bf00434741

19. Hulme C, Long AF, Kneafsey R, Reid G. Using the EQ-5D to assess health-related quality of life in older people. Age Ageing. 2004;33(5):504–507. doi:10.1093/ageing/afh178

20. Grund S, Breitinger E, Fricke S, Alpers G, Hundsdorfer W, Schäfer H. Health-related quality of life measurement inpatient geriatric rehabilitation: a comparison of the feasibility and suitability between the SF-36 and EQ-5D-5L questionnaires. J Gerontol Geriatr Res. 2017;06(06). 10.4172/2167-7182.1000458.

21. Michalowsky B, Xie F, Kohlmann T, Gräske J, Wübbeler M, Thyrian JR, Hoffmann W. Acceptability and validity of the EQ-5D in patients living with dementia. Value Health. 2020;23(6):760–767. doi:10.1016/j.jval.2020.01.022

22. Badia X, Schiaffino A, Alonso J, Herdman M. Using the EuroQoI 5-D in the Catalan general population: feasibility and construct validity. Qual Life Res. 1998;7(4):311–322. doi:10.1023/A:1024933913698

23. Hughes DA. Feasibility, validity and reliability of the welsh version of the EQ-5D health status questionnaire. Qual Life Res. 2007;16(8):1419–1423. doi:10.1007/s11136-007-9238-9

24. Yfantopoulos J, Chantzaras A, Kontodimas S. Assessment of the psychometric properties of the EQ-5D-3L and EQ-5D-5L instruments in psoriasis. Arch Dermatol Res. 2017;309(5):357–370. doi:10.1007/s00403-017-1743-2

25. Gerard K, Nicholson T, Mullee M, Mehta R, Roderick P. EQ-5D versus SF-6D in an older, chronically ill patient group. Appl Health Econ Health Policy. 2004;3(2):91–102. doi:10.2165/00148365-200403020-00005

26. Peyre H, Coste J, Leplège A. Identifying type and determinants of missing items in quality of life questionnaires: application to the SF-36 French version of the 2003 decennial health survey. Health Qual Life Outcomes. 2010;8(1):16. doi:10.1186/1477-7525-8-16

27. Coste J, Quinquis L, Audureau E, Pouchot J. Non response, incomplete and inconsistent responses to self-administered health-related quality of life measures in the general population: patterns, determinants and impact on the validity of estimates - a population-based study in France using the MOS SF-36. Health Qual Life Outcomes. 2013;11:44. doi:10.1186/1477-7525-11-44

28. Terwee CB, Bot SDM, de Boer MR, van der Windt DAWM, Knol DL, Dekker J, Bouter LM, de Vet HCW. Quality criteria were proposed for measurement properties of health status questionnaires. J Clin Epidemiol. 2007;60(1):34–42. doi:10.1016/j.jclinepi.2006.03.012

29. van Leeuwen KM, Jansen APD, Muntinga ME, Bosmans JE, Westerman MJ, van Tulder MW, van der Horst HE. Exploration of the content validity and feasibility of the EQ-5D-3L, ICECAP-O and ASCOT in older adults. BMC Health Serv Res. 2015;15:201. doi:10.1186/s12913-015-0862-8

30. IPSOS MORI. GP patient survey: national report - July 2017 publication. 2017.

31. IPSOS MORI. GP Patient Survey: Technical Annex. 2017.

32. Brooks R. EuroQol: the current state of play. Health Policy. 1996;37(1):53–72. doi:10.1016/0168-8510(96)00822-6

33. EuroQol Reseach Foundation. EQ-5D-5L User Guide. 2019.

34. IPSOS MORI. GP Patient Survey: Questionnaire redevelopment. 2018.

35. IPSOS MORI. GP patient survey: national summary report - January 2016 publication. 2016. https://gp-patient.co.uk/surveysandreports-10-16. Accessed 6 May 2022.

36. IPSOS MORI. GP patient survey: national summary report - July 2016 publication. 2016. https://gp-patient.co.uk/surveysandreports-10-16. Accessed 6 May 2022.

37. IPSOS MORI. GP Patient Survey: Year 2011/2012 Summary Report. 2012.

38. IPSOS MORI. GP patient survey: January - September 2012 Summary Report. 2012.

39. Rea LM, Parker RA. Designing and conducting survey research: A comprehensive guide. 2014. San Francisco, Jossey-Bass.

40. Corp S. Stata Statisitcal software: release 16. 2019. College Station, StataCorp LLc.

41. Garcia-Gordillo MA, Adsuar JC, Olivares PR. Normative values of EQ-5D-5L: in a Spanish representative population sample from Spanish health survey, 2011. Qual Life Res. 2016;25(5):1313–1321. doi:10.1007/s11136-015-1164-7

42. Grochtdreis T, Dams J, König H-H, Konnopka A. Health-related quality of life measured with the EQ-5D-5L: estimation of normative index values based on a representative German population sample and value set. Eur J Health Econ. 2019;20(6):933–944. doi:10.1007/s10198-019-01054-1

43. Kularatna S, Whitty JA, Johnson NW, Jayasinghe R, Scuffham PA. EQ-5D-3L derived population norms for health related quality of life in Sri Lanka. PLoS One. 2014;9(11):e108434. doi:10.1371/journal.pone.0108434

44. Holland R, Smith RD, Harvey I, Swift L, Lenaghan E. Assessing quality of life in the elderly: a direct comparison of the EQ-5D and AQoL. Health Econ. 2004;13(8):793–805. doi:10.1002/hec.858

45. Corbacho B, Keding A, Chuang L-H, Ramos-Goni JM, Joshi K, Cockayne S, Torgerson D. Comparison of the EQ-5D-5L and the EQ-5D-3L using individual patient data from the REFORM trial. F1000Res. 2021;10:974. doi:10.12688/f1000research.54554.1

46. Młyńczak K, Golicki D. Validity of the EQ-5D-5L questionnaire among the general population of Poland. Qual Life Res. 2021;30(3):817–829. doi:10.1007/s11136-020-02667-3

47. Perneger TV, Combescure C, Courvoisier DS. General population reference values for the French version of the EuroQol EQ-5D health utility instrument. Value Health. 2010;13(5):631–635. doi:10.1111/j.1524-4733.2010.00727.x

48. Ferreira LN, Ferreira PL, Ribeiro FP, Pereira LN. Comparing the performance of the EQ-5D-3L and the EQ-5D-5L in young Portuguese adults. Health Qual Life Outcomes. 2016;14(1):89. doi:10.1186/s12955-016-0491-x

49. Barton GR, Sach TH, Avery AJ, Jenkinson C, Doherty M, Whynes DK, Muir KR. A comparison of the performance of the EQ-5D and SF-6D for individuals aged or= 45 years. Health Econ. 2008;17(7):815–832. doi:10.1002/hec.1298

50. Luthy C, Cedraschi C, Allaz A-F, Herrmann FR, Ludwig C. Health status and quality of life: results from a national survey in a community-dwelling sample of elderly people. Qual Life Res. 2015;24(7):1687–1696. doi:10.1007/s11136-014-0894-2

51. DeCastellarnau A. A classification of response scale characteristics that affect data quality: a literature review. Qual Quant. 2018;52(4):1523–1559. doi:10.1007/s11135-017-0533-4

52. de Leeuw E, Hox J, Huisman M. Prevention and treatment of item nonresponse. J Off Stat. 2003;19:153–176.

53. Janssen MF, Bonsel GJ, Luo N. Is EQ-5D-5L better than EQ-5D-3L? A head-to-head comparison of descriptive systems and value sets from seven countries. Pharmacoeconomics. 2018;36(6):675–697. doi:10.1007/s40273-018-0623-8

54. Mulhern B, Feng Y, Shah K, Janssen MF, Herdman M, van Hout B, Devlin NJ. Comparing the UK EQ-5D-3L and English EQ-5D-5L value sets. Pharmacoeconomics. 2018;36(6):699–713. doi:10.1007/s40273-018-0628-3

55. Janssen MF, Birnie E, Haagsma JA, Bonsel GJ. Comparing the standard EQ-5D three-level system with a five-level version. Value Health. 2008;11(2):275–284. doi:10.1111/j.1524-4733.2007.00230.x

56. Hickson M, Frost G. An investigation into the relationships between quality of life, nutritional status and physical function. Clin Nutr. 2004;23(2):213–221. doi:10.1016/S0261-5614(03)00127-4

57. Rohr M, Brandstetter S, Plomer A-S, Loss J, Kretschmer R, Apfelbacher C. A qualitative study exploring content validity and feasibility of frequently used generic health-related quality of life measures in older people with hip fracture: the patients' perspective. Injury. 2021;52(2):134–141. doi:10.1016/j.injury.2020.09.061

58. Bowling A. Mode of questionnaire administration can have serious effects on data quality. J Public Health (Oxf). 2005;27(3):281–291. doi:10.1093/pubmed/fdi031

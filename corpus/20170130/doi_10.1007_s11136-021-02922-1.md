---
project_id: "20170130"
work_id: "doi:10.1007/s11136-021-02922-1"
doi: "10.1007/s11136-021-02922-1"
pmid: "34236579"
pmcid: "PMC8800896"
title: "Combining EQ-5D-5L items into a level summary score: demonstrating feasibility using non-parametric item response theory using an international dataset"
journal: "Quality of Life Research"
publication_date: "2021-07-08"
volume: "31"
issue: "1"
authors:
  - name: "You-Shan Feng"
    orcid: "http://orcid.org/0000-0003-1509-3409"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Ruixuan Jiang"
    affiliation_ids:
      - "Aff3"
  - name: "A. Simon Pickard"
    affiliation_ids:
      - "Aff4"
  - name: "Thomas Kohlmann"
    affiliation_ids:
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "grid.10392.390000 0001 2190 1447Institute for Clinical Epidemiology and Applied Biometrics, Medical University of Tübingen, Silcherstraße 5 72076, Tübingen, Germany"
  - id: "Aff2"
    name: "grid.5603.0Institute for Community Medicine, University of Greifswald, Greifswald, Germany"
  - id: "Aff3"
    name: "Center for Observational and Real-World Evidence, Merck & Co, Kenilworth, NJ USA"
  - id: "Aff4"
    name: "grid.185648.60000 0001 2175 0319College of Pharmacy, University of Illinois At Chicago, Chicago, IL USA"
keywords:
  - "EQ-5D-5L"
  - "Mokken scaling"
  - "Non-economic scoring approaches"
  - "Non-parametric item response theory"
  - "Unweighted summary score"
licence: "cc-by"
source_file: "input/projects/20170130/papers/doi_10.1007_s11136-021-02922-1.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8800896/fullTextXML"
source_method: "epmc_xml"
source_sha256: "31a12c3b6a3a92ad42477d7a58d561a571922c320f30927ee5af4421efd9a849"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Combining EQ-5D-5L items into a level summary score: demonstrating feasibility using non-parametric item response theory using an international dataset

## Abstract

### Background

The EQ-5D-5L is a well-established health questionnaire that estimates health utilities by applying preference-based weights. Limited work has been done to examine alternative scoring approaches when utility weights are unavailable or inapplicable. We examined whether the Mokken scaling approach can elucidate 1) if the level summary score is appropriate for the EQ-5D-5L and 2) an interpretation of such a score.

### Methods

The R package “mokken” was used to assess monotonicity (scaling coefficients H, automated item selection procedure) and manifest invariant item ordering (MIIO: paired item response functions \[IRF\], H<sup>T</sup>). We used a rich dataset (the Multiple Instrument Comparison, MIC) which includes EQ-5D-5L data from six Western countries.

### Results

While all EQ-5D-5L items demonstrated monotonicity, the anxiety/depression (AD) item had weak scalability (H<sub>i</sub> = 0.377). Without AD, scalability improved from H<sub>s</sub> = 0.559 to H<sub>s</sub> = 0.714. MIIO revealed that the 5 items can be ordered, and the ordering is moderately accurate in the MIC data (H<sup>T</sup> = 0.463). Excluding AD, H<sup>T</sup> improves to 0.743. Results were largely consistent across disease and country subgroups.

### Discussion

The 5 items of the EQ-5D-5L form a moderate to strong Mokken scale, enabling persons to be ordered using the level summary score. Item ordering suggests that the lower range of the score represents mainly problems with pain and anxiety/depression, the mid-range indicates additional problems with mobility and usual activities, and middle to higher range of scores reveals additional limitations with self-care. Scalability and item ordering are even stronger when the anxiety/depression item is not included in the scale.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-021-02922-1.

## Background

The EQ-5D is a widely used generic measure of health \[1, 2\]. As it is brief and not disease specific, the EQ-5D is applied in a broad range of settings, including measurement of health status in clinical practice, population health surveillance, assessment of healthcare quality, medical decision making, and patient communication \[3–9\]. The EQ-5D-5L expanded the response levels to five from the original three-level version (EQ-5D-3L) \[10\].

The EQ-5D is best known for the generation of quality-adjusted life years (QALY) in cost-utility analysis, used to inform drug reimbursement and pricing decisions in some countries/regions. Utility values, which are used to estimate QALYs, are calculated for EQ-5D-5L health states by applying a societal value set. Societal value sets are preference-based scoring weights estimated using valuation studies \[11\]. In valuation studies, hypothetical EQ-5D-5L health states are valued using choice-based methods, such as the time trade-off. These studies are generally conducted using representative, location/region-specific population samples. However, for many applications of the EQ-5D, population/country-specific utility scores may be unjustifiable or even introduce additional statistical biases \[7, 9, 12\]. An alternative method to summarize the instrument, relevant when utility weights are unavailable or unsuitable (e.g., EQ-5D-Y), is a total sum score of the severity levels on each dimension. Because each item of the EQ-5D has the same number of response levels, all items and severity levels contribute equally to this additive score. This approach has been termed “equally weighted” score \[13\], “unweighted” scoring approach \[14, 15\], and informally the “misery” score/index \[16–18\]. The term “level sum score” (LSS) was used in the recently published guidebook for analyzing EQ-5D data \[16\] and will be used for the remainder of this paper for consistency and clarity. The appeal of the LSS is its simplicity and consistency across populations (i.e., the same scoring system for all countries and populations).

Both the LSS and utility values are summary scores with similar limitations in interpretation; two patients may have the same summary score, but one may have extreme problems in a single dimension, whereas the other may have slight problems in several dimensions. Utility scores have found widespread acceptance over the LSS for the EQ-5D, potentially due to the rigorous development of preference elicitation.

The LSS has one major merit over utility scores when societal preference scores are unnecessary (i.e., non-economic applications): no algorithm is required to estimate the LSS, the end-user does not need to choose a specific value set to use (e.g., in multinational studies). Although previous investigations into the use of the EQ-5D LSS found substantial agreement and similar psychometric properties between the LSS and utility scores \[13–15\], the high correlations (ICC/Rho \> 0.9) do not prove LSS accurately describes HRQoL or is appropriate for statistical inference. There is a dearth of literature specifically assessing the appropriateness of the LSS to describe HRQoL.

Item response theory (IRT) comprises a large set of models used to aid the construction and evaluation of multi-item scales. In general, these models assess the relationship between a latent variable of interest (θ) and the manifest/observable response patterns of a set of items. The probability of endorsing a particular response level on items of a scale is dependent on the respondent’s θ level. Parametric IRT has been previously applied to study the EQ-5D, although not to elucidate scoring \[19–22\]. Non-parametric item response theory (NP-IRT) approaches do not make strict assumptions about the shape of the function that describes the relationship between the response probability and the latent variable \[23\]. NP-IRT investigates whether the ordering of respondents along the summary score reflects the stochastic ordering of persons along θ \[23, 24\] instead of estimating θ. If the LSS is a proxy for θ (i.e., underlying health), then ordering of persons along the summary score is the ordering of persons along θ. Mokken scaling is a scaling approach comprising of a set of methods to assess whether the data fit a set of NP-IRT models. Two nested NP-IRT models included in Mokken scaling are as follows: the monotone homogeneity model (MHM), which examines ordering of persons along θ; and double monotonicity model (DMM), which examines ordering of persons and items along θ \[25, 26\]. If EQ-5D-5L data fit the MHM or DMM, then the use of LSS to represents underlying health can be justified and interpreted. The EQ-5D-5L is a good candidate for applying Mokken scaling as all items have the same number of ordered response categories with analogous adjectives.

The aims of these analyses were to investigate whether the MHM and DMM fit EQ-5D-5L data in order to 1) determine whether the LSS can be justified for the EQ-5D-5L and 2) examine whether an interpretation can be applied to such a score.

## Methods

### EQ-5D-5L

The EQ-5D health profile includes the items mobility (MO), self-care (SC), usual activities (UA), pain/discomfort (PD) and anxiety/depression (AD) \[2\]. The EQ-5D-5L asks respondents to endorse one of five response levels for each item: “no problems,” “slight problems,” “moderate problems,” “severe problems,” and “extreme problems”/ “unable to” \[20, 27\], describing 3125 (5<sup>5</sup>) health state profiles. The instrument also includes a visual analog scale (VAS) anchored by 0 (worst imaginable health) and 100 (best imaginable health) that is usually analyzed separately from the health profile.

The LSS is typically calculated by assigning a numerical value to each response level (i.e., 1 for “no problems”, 5 for “extreme problems”/”unable to”) and summing these values across the five items, resulting in a score from 5 (11,111, no problems on any dimension) to 25 (55,555, extreme problems on all dimensions) for the EQ-5D-5L.

#### Dataset

The Multi Instrument Comparison (MIC) project surveyed six countries in 2012 (Australia, Canada, Germany, Norway, UK, and USA), sampling respondents who self-reported seven chronic illnesses plus a healthy sample with no self-reported chronic conditions \[28, 29\]. Respondents completed a battery of health status, subjective well-being and capability measures, including the EQ-5D-5L. This dataset provides an opportunity to assess the scaling properties of the EQ-5D-5L in a large sample across disease and country subgroups. The disease groups chronic obstructive pulmonary disease and stroke were only sampled in the Australia and therefore excluded from analysis. All analyses were repeated by the subgroups self-reported disease and country.

Data management and descriptive statistics were handled in Microsoft Excel and Stata SE 13 \[30\], while all other analyses were conducted using the statistical language and environment R \[31\] with Van der Ark’s package “mokken” \[32, 33\]. The R script is included as supplementary material A. Permission to use the MIC dataset can be obtained here: <https://www.aqol.com.au/index.php/mic-data>.

#### Mokken scale analysis

We investigated the assumptions of two nested NP-IRT models that examine the ordinal location of patients and items along a single latent variable θ: respondents were ordered according to their LSS and items are ordered according to mean item scores \[23, 25, 26\]. The polytomous MHM and DMM models are extended from the dichotomous models \[34, 35\]. The MHM can elucidate whether a summary score can be used to order individuals along the latent variable. The more restrictive DMM is nested within the MHM and can further elucidate whether the items (i.e., EQ-5D-5L dimensions in these analyses) can be ordered invariantly along the latent variable. We examined how well polytomous MHM and DMM models fit EQ-5D-5L data.

#### Assessment of fit of the monotone homogeneity model

The MHM has three assumptions:

1.  Unidimensionality: items within the scale measure the same underlying latent variable;

2.  Local independence: responses to scale items are influenced only on level by θ; and

3.  Monotonicity: probability of endorsing particular response levels is monotonically non-decreasing as θ increases.

Loevinger’s homogeneity coefficients, automated item selection procedure, and manifest monotonicity were used to assess the fit of the MHM to EQ-5D-5L data. Additionally, we examined scale reliability using Molenaar and Sijtsma’s rho (ρ) \[36\] and Guttman’s lamda-2 (λ-2) \[37, 38\].

Scalability of the EQ-5D-5L items was assessed using Loevinger’s scalability coefficients H, for which H values reflect item fit within a scale. H is measured on the item pair (H<sub>ij</sub>), item (H<sub>i</sub>), and scale (H<sub>S</sub>) levels. H<sub>ij</sub> is the normed covariance between a pair of item scores while H<sub>i</sub> is the normed covariance between item and rest scores \[23, 32\]. H<sub>S</sub> is a weighted mean of H<sub>i</sub>. Negative H<sub>ij</sub> and H<sub>i</sub> coefficients indicate an item violates MHM. The closer H<sub>i</sub> is to 1, the better an item can discriminate subjects along θ. On the item level, H<sub>i</sub> \> 0.3 is considered sufficient, while H<sub>i</sub> \> 5 indicates a strongly discriminating item. The commonly accepted rules of thumb for interpreting H<sub>S</sub> were applied: H<sub>S</sub> \< 0.3 indicates the item set is unscalable, H<sub>S</sub> between 0.3 and 0.4 indicates a weak scale, H<sub>S</sub> between 0.4 and 0.5 indicates moderate, and H<sub>S</sub> ≥ 0.5 indicates strong \[25\]. H<sub>ij</sub> \> 0 indicates that the data fit the MHM. We also used the H<sub>ij</sub> to examine which item pairs are more strongly related than other pairs.

Automated item selection procedure (AISP) is a standard feature of the “mokken” package which selects subsets of items from a larger set that can represent attributes on which respondents can be ordered by total scores \[32\]. Although the lower bound of 0.3 is suggested for accepting items in a scale, it was more informative to determine at which level of H<sub>i</sub> was items no longer scalable. Therefore, we first executed the AISP 12 times with the lower bound for H<sub>i</sub> set between 0 and 0.5, increasing in steps of 0.05 \[23, 32\]. Then we pinpointed the level of H<sub>i</sub> at which each of the five items was no longer appropriate for the scale by decreasing H<sub>i</sub> in steps of 0.001 from the cutoff identified in the previous step.

#### Monotonicity

Latent monotonicity generally also implies manifest monotonicity, which is observable in the data \[32\] Therefore, if the LSS is a proxy for θ, then ordering of persons along the LSS reflects the ordering of persons along θ. Manifest monotonicity was assessed by examining whether the cumulative probability for a dimension-level rating at or above each dimension-level rating does not decrease across rest score groups. Rest scores are calculated by subtracting the item of interest from the LSS. Rest score groups are created automatically based on minimum sample size requirements for each group \[32, 33\]. Only violations greater than the default minimum (*minvi* = 0.03 for the function check.monotonicity of the R package “mokken”) were reported \[32\]. Furthermore, item step response functions (ISRFs) and item response functions (IRFs) were visually inspected for monotonicity. ISRF plots the probability for endorsing a response level or higher across the latent variable. IRF for polytomous items is the sum of an item’s ISRFs.

#### Assessment of invariant item ordering

The DMM model is a special case of MHM for which all assumptions of the MHM hold with an additional assumption that the IRF or ISRF of items does not intersect. Non-interception of ISRF is not necessarily evidence of item order \[39\] and would not be meaningful for interpretation of the LSS. Therefore, we did not examine non-interception of ISRF as a measure of DMM fit, rather focusing on invariant item ordering. Invariant item ordering can provide an interpretation: If the items have the same ordering along θ, then the summary score might be interpreted based on that order \[32, 33, 39\]. We therefore examined manifest invariant item ordering (MIIO) as suggested by Ligtvoet et al. (2010, 2011) \[40, 41\].

We assessed MIIO using the check.iio function of the R package “mokken,” which orders items by their conditional mean scores and checks each item pair for violations of ordering for rest score groups. Violations that exceed the default minimum value (number of ISRFs times 0.03) are reported \[33, 41\]. Coefficient H<sup>T</sup> gives an indication of the degree to which the sample follows item ordering. We applied the rules of thumb that H<sup>T</sup> \< 0.3 implies the item ordering accuracy is too low, H<sup>T</sup> between 0.3 and 0.4 as ordering with low accuracy, H<sup>T</sup> between 0.4 and 0.5 as moderate accuracy, and H<sup>T</sup> \> 0.5 as highly accurate item ordering \[41\].

## Results

The included 7,933 subjects of the MIC reported 566 of the 3125 possible response patterns on the EQ-5D-5L; “11,111” (full health) and slight problems with PD with no problems on the other dimensions (“11,121”) were the first and second most often endorsed (19.3% and 14.3%, respectively). Subjects without chronic conditions were most homogeneous in regard to health profile (94 unique profiles), while those with diabetes reported the most diverse range of health (239 unique profiles; supplementary materials B and C). Number of distinct health profiles ranged from 164 (Norway) to 276 (UK) across country samples. Although over 8% of MIC respondents noted their general health as “poor,” endorsements of the most severe EQ-5D-5L levels were rare, especially for MO and SC (Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of the study sample (MIC)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Sample size</th>
<th style="text-align: left;">7933</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Highest education</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Health conditions</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">4140</td>
<td style="text-align: left;">(52.19)</td>
<td style="text-align: left;">High school</td>
<td style="text-align: left;">2482</td>
<td style="text-align: left;">(31.29)</td>
<td style="text-align: left;">Healthy</td>
<td style="text-align: left;">1760</td>
<td style="text-align: left;">(22.19)</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Diploma/certificate/trade</td>
<td style="text-align: left;">3208</td>
<td style="text-align: left;">(40.44)</td>
<td style="text-align: left;">Asthma</td>
<td style="text-align: left;">856</td>
<td style="text-align: left;">(10.79)</td>
</tr>
<tr>
<td style="text-align: left;"> 18–24</td>
<td style="text-align: left;">513</td>
<td style="text-align: left;">(6.47)</td>
<td style="text-align: left;">University</td>
<td style="text-align: left;">2243</td>
<td style="text-align: left;">(28.27)</td>
<td style="text-align: left;">Cancer</td>
<td style="text-align: left;">772</td>
<td style="text-align: left;">(9.73)</td>
</tr>
<tr>
<td style="text-align: left;"> 25–34</td>
<td style="text-align: left;">943</td>
<td style="text-align: left;">(11.89)</td>
<td style="text-align: left;">Self-Rated Health</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Depression</td>
<td style="text-align: left;">917</td>
<td style="text-align: left;">(11.56)</td>
</tr>
<tr>
<td style="text-align: left;"> 35–44</td>
<td style="text-align: left;">1133</td>
<td style="text-align: left;">(14.28)</td>
<td style="text-align: left;">Excellent</td>
<td style="text-align: left;">433</td>
<td style="text-align: left;">(5.46)</td>
<td style="text-align: left;">Diabetes</td>
<td style="text-align: left;">924</td>
<td style="text-align: left;">(11.65)</td>
</tr>
<tr>
<td style="text-align: left;"> 45–54</td>
<td style="text-align: left;">1672</td>
<td style="text-align: left;">(21.08)</td>
<td style="text-align: left;">Very Good</td>
<td style="text-align: left;">2089</td>
<td style="text-align: left;">(26.34)</td>
<td style="text-align: left;">Hearing problems</td>
<td style="text-align: left;">832</td>
<td style="text-align: left;">(10.49)</td>
</tr>
<tr>
<td style="text-align: left;"> 55–64</td>
<td style="text-align: left;">1977</td>
<td style="text-align: left;">(24.92)</td>
<td style="text-align: left;">Good</td>
<td style="text-align: left;">2726</td>
<td style="text-align: left;">(34.37)</td>
<td style="text-align: left;">Arthritis</td>
<td style="text-align: left;">929</td>
<td style="text-align: left;">(11.71)</td>
</tr>
<tr>
<td style="text-align: left;"> 65 + </td>
<td style="text-align: left;">1695</td>
<td style="text-align: left;">(21.37)</td>
<td style="text-align: left;">Fair</td>
<td style="text-align: left;">2039</td>
<td style="text-align: left;">(25.71)</td>
<td style="text-align: left;">Heart Conditions</td>
<td style="text-align: left;">943</td>
<td style="text-align: left;">(11.89)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Poor</td>
<td style="text-align: left;">645</td>
<td style="text-align: left;">(8.13)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="11" style="text-align: left;">EQ-5D-5L results</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Mobility</th>
<th colspan="2" style="text-align: left;">Self-Care</th>
<th colspan="2" style="text-align: left;">Usual Activities</th>
<th colspan="2" style="text-align: left;">Pain/Discomfort</th>
<th colspan="2" style="text-align: left;">Anxiety Depression</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
<th style="text-align: left;"><em>n</em></th>
<th style="text-align: left;">(%)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">No Problems/ None</td>
<td style="text-align: left;">5163</td>
<td style="text-align: left;">(65.08)</td>
<td style="text-align: left;">6984</td>
<td style="text-align: left;">(88.04)</td>
<td style="text-align: left;">5163</td>
<td style="text-align: left;">(65.08)</td>
<td style="text-align: left;">2331</td>
<td style="text-align: left;">(29.38)</td>
<td style="text-align: left;">3982</td>
<td style="text-align: left;">(50.20)</td>
</tr>
<tr>
<td style="text-align: left;">Slight (Problems)</td>
<td style="text-align: left;">1707</td>
<td style="text-align: left;">(21.52)</td>
<td style="text-align: left;">624</td>
<td style="text-align: left;">(7.87)</td>
<td style="text-align: left;">1707</td>
<td style="text-align: left;">(21.52)</td>
<td style="text-align: left;">3214</td>
<td style="text-align: left;">(40.51)</td>
<td style="text-align: left;">2319</td>
<td style="text-align: left;">(29.23)</td>
</tr>
<tr>
<td style="text-align: left;">Moderate (Problems)</td>
<td style="text-align: left;">771</td>
<td style="text-align: left;">(9.72)</td>
<td style="text-align: left;">258</td>
<td style="text-align: left;">(3.25)</td>
<td style="text-align: left;">771</td>
<td style="text-align: left;">(9.72)</td>
<td style="text-align: left;">1595</td>
<td style="text-align: left;">(20.11)</td>
<td style="text-align: left;">1088</td>
<td style="text-align: left;">(13.71)</td>
</tr>
<tr>
<td style="text-align: left;">Severe (Problems)</td>
<td style="text-align: left;">244</td>
<td style="text-align: left;">(3.08)</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">(0.74)</td>
<td style="text-align: left;">244</td>
<td style="text-align: left;">(3.08)</td>
<td style="text-align: left;">683</td>
<td style="text-align: left;">(8.61)</td>
<td style="text-align: left;">383</td>
<td style="text-align: left;">(4.83)</td>
</tr>
<tr>
<td style="text-align: left;">Unable to/ Extreme</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">(0.61)</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">(0.10)</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">(0.61)</td>
<td style="text-align: left;">110</td>
<td style="text-align: left;">(1.39)</td>
<td style="text-align: left;">161</td>
<td style="text-align: left;">(2.03)</td>
</tr>
</tbody>
</table>

</div>

### AISP and scalability

The EQ-5D-5L is a reliable scale, with ρ = 0.822 and λ-2 = 0.819. AISP placed all five items onto a single latent variable when the lower bound for H<sub>i</sub> was set at the default 0.3, even when considering the 95% confidence interval (derived from standard errors). AD was identified as an unscalable item at H<sub>i</sub> ≥ 0.378. PD was rejected from the scale at H<sub>i</sub> ≥ 0.685, SC at H<sub>i</sub> ≥ 0.721, and no items could be scaled at H<sub>i</sub> ≥ 0.75 (Table <a href="#Tab2" data-ref-type="table">2</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

Item characteristics of the EQ-5D-5L

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Item</th>
<th rowspan="2" style="text-align: left;">Mean</th>
<th rowspan="2" style="text-align: left;">H<sub>i</sub></th>
<th rowspan="2" style="text-align: left;">(SE)</th>
<th colspan="3" style="text-align: left;">Monotonicity</th>
<th colspan="3" style="text-align: left;">MIIO</th>
</tr>
<tr>
<th style="text-align: left;">AC</th>
<th style="text-align: left;">VI</th>
<th style="text-align: left;">Crit</th>
<th style="text-align: left;">AC</th>
<th style="text-align: left;">VI</th>
<th style="text-align: left;">Crit</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">1. Mobility</td>
<td>0.524</td>
<td>0.600</td>
<td style="text-align: left;">(0.008)</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">128</td>
</tr>
<tr>
<td style="text-align: left;">2. Self-Care</td>
<td>0.170</td>
<td>0.597</td>
<td style="text-align: left;">(0.010)</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">3. Usual Activities</td>
<td>0.526</td>
<td>0.647</td>
<td style="text-align: left;">(0.007)</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">150</td>
</tr>
<tr>
<td style="text-align: left;">4. Pain/Discomfort</td>
<td>1.121</td>
<td>0.603</td>
<td style="text-align: left;">(0.008)</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">5. Anxiety/Depression</td>
<td>0.793</td>
<td>0.377</td>
<td style="text-align: left;">(0.011)</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">216</td>
</tr>
<tr>
<td style="text-align: left;"> H<sub>s</sub></td>
<td></td>
<td>0.559</td>
<td style="text-align: left;">(0.007)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Rho</td>
<td></td>
<td>0.822</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Lambda</td>
<td></td>
<td>0.819</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td colspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">1. Mobility</td>
<td>0.524</td>
<td>0.731</td>
<td style="text-align: left;">(0.007)</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">2. Self-Care</td>
<td>0.170</td>
<td>0.681</td>
<td style="text-align: left;">(0.011)</td>
<td style="text-align: left;">33</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">3. Usual Activities</td>
<td>0.526</td>
<td>0.730</td>
<td style="text-align: left;">(0.007)</td>
<td style="text-align: left;">33</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;">4. Pain/Discomfort</td>
<td>1.121</td>
<td>0.701</td>
<td style="text-align: left;">(0.008)</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
</tr>
<tr>
<td style="text-align: left;"> H<sub>s</sub></td>
<td></td>
<td>0.714</td>
<td style="text-align: left;">(0.007)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Rho</td>
<td></td>
<td>0.880</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"> Lambda</td>
<td></td>
<td>0.856</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

*AC* Active Pairs, *VI* Violations, *Crit* Critical Values, *Hi* Coefficient H for items, *Hs* Coefficient H for the Scale, *MIIO* manifest invariant item ordering

</div>

H<sub>i</sub> values were above 0.6 for all items except for AD, which had a H<sub>i</sub> of 0.377. H<sub>ij</sub> of AD with the other items ranged from 0.292 (MO) to 0.448 (UA) (Table <a href="#Tab3" data-ref-type="table">3</a>). H<sub>ij</sub> of SC and PD was larger than all AD item pairs, but smaller than 0.7, while all other item pairs had H<sub>ij</sub> above 0.7. Because the H<sub>i</sub> of AD was close to 0.3, the value of acceptability for H<sub>i</sub>, we decided to assess scalability by omitting this item. If the reduced item set would yield a much stronger scale, this would be an important finding. Researchers would possibly decide to employ the reduced items set in studies where a scale with increased scalability is needed, such as in instances where item ordering must be strictly maintained. When AD was removed from the model, H<sub>S</sub> increased from 0.559 to 0.714, and the H<sub>i</sub> of the four remaining items also increased (Table <a href="#Tab2" data-ref-type="table">2</a>).

<div id="Tab3" class="table-wrap">

<div class="caption">

Scalability coefficients and standard error for item pairs of the EQ-5D-5L

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Self-care</th>
<th colspan="2" style="text-align: left;">Usual activities</th>
<th colspan="2" style="text-align: left;">Pain/discomfort</th>
<th colspan="2" style="text-align: left;">Anxiety/depression</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility</td>
<td>0.705</td>
<td style="text-align: left;">(0.013)</td>
<td>0.750</td>
<td style="text-align: left;">(0.009)</td>
<td>0.725</td>
<td style="text-align: left;">(0.009)</td>
<td>0.292</td>
<td style="text-align: left;">(0.014)</td>
</tr>
<tr>
<td style="text-align: left;">Self-Care</td>
<td></td>
<td style="text-align: left;"></td>
<td>0.718</td>
<td style="text-align: left;">(0.013)</td>
<td>0.617</td>
<td style="text-align: left;">(0.015)</td>
<td>0.364</td>
<td style="text-align: left;">(0.018)</td>
</tr>
<tr>
<td style="text-align: left;">Usual Activities</td>
<td></td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"></td>
<td>0.717</td>
<td style="text-align: left;">(0.009)</td>
<td>0.448</td>
<td style="text-align: left;">(0.013)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/Discomfort</td>
<td></td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"></td>
<td></td>
<td style="text-align: left;"></td>
<td>0.398</td>
<td style="text-align: left;">(0.013)</td>
</tr>
</tbody>
</table>

*H*<sub>*ij*</sub> Coefficient H for item pairs, *SE* Standard Error

</div>

### Fit of the MHM model

Figure <a href="#Fig1" data-ref-type="fig">1</a> illustrates the IRF and ISRF charted over rest score groups for the five items of the EQ-5D-5L. All IRFs and ISRFs increased monotonically with no violations of manifest monotonicity observed (Table <a href="#Tab2" data-ref-type="table">2</a>). Critical values of all items were zero, showing no misfit of the MHM.

<figure id="Fig1">
<p><img src="11136_2021_2922_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Item step response functions and item response functions of the five items of the EQ-5D-5L</figcaption>
</figure>

### Fit of MIIO

Two violations of MIIO were observed between 1) AD and MO, and 2) AD and UA (Table <a href="#Tab4" data-ref-type="table">4</a>). AD had the highest critical value, and in backward selection was recommended for exclusion. Due to this recommendation for exclusion, we examined MIIO excluding the AD item, after which no violations of MIIO remained.

<div id="Tab4" class="table-wrap">

<div class="caption">

EQ-5D-5L Item scaling coefficients stratified by disease type and country

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Mobility H<sub>i</sub></th>
<th colspan="2" style="text-align: left;">Self-Care H<sub>i</sub></th>
<th colspan="2" style="text-align: left;">Usual Activities H<sub>i</sub></th>
<th colspan="2" style="text-align: left;">Pain/ Discomfort H<sub>i</sub></th>
<th style="text-align: left;">Anxiety/ Depression H<sub>i</sub></th>
<th colspan="2" style="text-align: left;">Scale H<sub>S</sub></th>
<th colspan="2" style="text-align: left;">H<sup>T</sup></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Full scale</th>
<th style="text-align: left;">Without AD</th>
<th style="text-align: left;">Full Scale</th>
<th style="text-align: left;">Without AD</th>
<th style="text-align: left;">Full Scale</th>
<th style="text-align: left;">Without AD</th>
<th style="text-align: left;">Full Scale</th>
<th style="text-align: left;">Without AD</th>
<th style="text-align: left;">Full Scale</th>
<th style="text-align: left;">Full Scale</th>
<th style="text-align: left;">Without AD</th>
<th style="text-align: left;">Full Scale</th>
<th style="text-align: left;">Without AD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Complete Sample*</td>
<td>†0.600</td>
<td>0.731</td>
<td>0.597</td>
<td>0.681</td>
<td>†0.647</td>
<td>0.730</td>
<td>0.603</td>
<td>0.701</td>
<td>‡0.377</td>
<td>0.559</td>
<td>0.714</td>
<td>0.463</td>
<td>0.743</td>
</tr>
<tr>
<td style="text-align: left;">Healthy Sample</td>
<td>0.422</td>
<td>0.563</td>
<td>0.453</td>
<td>0.555</td>
<td>0.414</td>
<td>0.517</td>
<td>0.389</td>
<td>0.503</td>
<td>0.193</td>
<td>0.356</td>
<td>0.532</td>
<td>0.493</td>
<td>0.808</td>
</tr>
<tr>
<td colspan="14" style="text-align: left;">Self-Reported Chronic Condition</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma*</td>
<td>†0.606</td>
<td>0.729</td>
<td>0.563</td>
<td>0.674</td>
<td>†0.635</td>
<td>0.731</td>
<td>0.601</td>
<td>0.687</td>
<td>‡0.355</td>
<td>0.549</td>
<td>0.709</td>
<td>0.470</td>
<td>0.760</td>
</tr>
<tr>
<td style="text-align: left;"> Cancer*</td>
<td>†0.615</td>
<td>0.740</td>
<td>0.595</td>
<td>0.669</td>
<td>†0.642</td>
<td>0.734</td>
<td>0.598</td>
<td>0.683</td>
<td>‡0.366</td>
<td>0.561</td>
<td>0.711</td>
<td>0.467</td>
<td>0.712</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td>0.426</td>
<td>0.592</td>
<td>0.484</td>
<td>0.565</td>
<td>0.511</td>
<td>0.592</td>
<td>0.408</td>
<td>0.584</td>
<td>0.230</td>
<td>0.393</td>
<td>0.585</td>
<td>0.747</td>
<td>0.651</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes*</td>
<td>†0.627</td>
<td>0.747</td>
<td>0.610</td>
<td>0.700</td>
<td>†0.664</td>
<td>0.744</td>
<td>0.617</td>
<td>0.692</td>
<td>‡0.393</td>
<td>0.579</td>
<td>0.723</td>
<td>0.467</td>
<td>0.730</td>
</tr>
<tr>
<td style="text-align: left;"> Hearing Problems*</td>
<td>†0.535</td>
<td>0.657</td>
<td>0.570</td>
<td>0.644</td>
<td>†0.568</td>
<td>0.667</td>
<td>0.524</td>
<td>0.594</td>
<td>‡0.305</td>
<td>0.492</td>
<td>0.640</td>
<td>0.534</td>
<td>0.797</td>
</tr>
<tr>
<td style="text-align: left;"> Arthritis*</td>
<td>0.549</td>
<td>0.709</td>
<td>0.544</td>
<td>0.641</td>
<td>†0.599</td>
<td>0.713</td>
<td>0.559</td>
<td>0.660</td>
<td>†0.277</td>
<td>0.499</td>
<td>0.685</td>
<td>0.664</td>
<td>0.848</td>
</tr>
<tr>
<td style="text-align: left;"> Heart Disease*</td>
<td>†0.628</td>
<td>0.745</td>
<td>0.636</td>
<td>0.721</td>
<td>†0.658</td>
<td>0.752</td>
<td>0.640</td>
<td>0.715</td>
<td>‡0.406</td>
<td>0.589</td>
<td>0.735</td>
<td>0.497</td>
<td>0.745</td>
</tr>
<tr>
<td colspan="14" style="text-align: left;">Country of survey sample</td>
</tr>
<tr>
<td style="text-align: left;"> Australia*</td>
<td>†0.582</td>
<td>0.752</td>
<td>0.570</td>
<td>0.653</td>
<td>†0.615</td>
<td>0.739</td>
<td>0.586</td>
<td>0.715</td>
<td>‡0.289</td>
<td>0.520</td>
<td>0.723</td>
<td>0.465</td>
<td>0.794</td>
</tr>
<tr>
<td style="text-align: left;"> USA*</td>
<td>†0.602</td>
<td>0.715</td>
<td>0.595</td>
<td>0.667</td>
<td>†0.647</td>
<td>0.719</td>
<td>0.607</td>
<td>0.672</td>
<td>‡0.419</td>
<td>0.570</td>
<td>0.697</td>
<td>0.502</td>
<td>0.758</td>
</tr>
<tr>
<td style="text-align: left;"> UK*</td>
<td>†0.663</td>
<td>0.805</td>
<td>0.650</td>
<td>0.758</td>
<td>†0.687</td>
<td>0.794</td>
<td>0.650</td>
<td>0.772</td>
<td>‡0.349</td>
<td>0.595</td>
<td>0.784</td>
<td>0.373</td>
<td>0.678</td>
</tr>
<tr>
<td style="text-align: left;"> Canada</td>
<td>0.591</td>
<td>0.722</td>
<td>0.570</td>
<td>0.663</td>
<td>0.652</td>
<td>0.733</td>
<td>0.617</td>
<td>0.705</td>
<td>0.399</td>
<td>0.561</td>
<td>0.711</td>
<td>0.510</td>
<td>0.772</td>
</tr>
<tr>
<td style="text-align: left;"> Norway</td>
<td>0.436</td>
<td>0.553</td>
<td>0.468</td>
<td>0.506</td>
<td>0.573</td>
<td>0.600</td>
<td>0.503</td>
<td>0.578</td>
<td>0.369</td>
<td>0.468</td>
<td>0.568</td>
<td>0.506</td>
<td>0.749</td>
</tr>
<tr>
<td style="text-align: left;"> Germany*</td>
<td>†0.582</td>
<td>0.703</td>
<td>0.570</td>
<td>0.668</td>
<td>†0.615</td>
<td>0.699</td>
<td>0.586</td>
<td>0.675</td>
<td>‡0.289</td>
<td>0.520</td>
<td>0.688</td>
<td>0.467</td>
<td>0.732</td>
</tr>
</tbody>
</table>

\*Backward item selection excluded AD; † one violation found; ‡ two violations found

H<sub>i</sub>: Coefficient H for items; H<sub>s</sub>: Coefficient H for the Scale; H<sup>T</sup>: Coefficient H for accuracy of item ordering

H<sup>T</sup> calculated without exclusion due to backward item selection

</div>

In order to visualize the IRF of all items in one figure, we selected item-pair results from the check.restscore function (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). IRF charted over rest score groups indicate that the lower rest scores (≤ 3) were driven by PD and secondarily by AD. In the slightly higher rest score groups (2–4), the IRFs of MO and UA equally increased and overlapped, while AD’s IRF flattened. IRF of AD crossed both MO and US at rest scores 4–5. The IRF of SC did not increase until reaching higher rest score groups (4–5). Moderate item ordering was observed for the complete MIC sample (H<sup>T</sup> = 0.463) (Table <a href="#Tab4" data-ref-type="table">4</a>).

<figure id="Fig2">
<p><img src="11136_2021_2922_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Item response functions of the five items of the EQ-5D-5L, estimated from paired restore groups</figcaption>
</figure>

### Stratified analysis across subgroups

H coefficients were estimated for disease and country subgroups for the complete EQ-5D-5L scale as well as for the scale omitting the AD item as AD was recommended for exclusion by the check.iio procedure for many subgroups (Table <a href="#Tab4" data-ref-type="table">4</a>). For the complete scale, H<sub>s</sub> was weak for the healthy subsample (0.363), moderate for subjects with hearing problems and from Norway (0.496, 0.476, respectively). H<sub>s</sub> for all other subgroups was “strong” but was all below 0.6.

H<sup>T</sup> for the full scale ranged from 0.373 (Norway) to 0.747 (depression). Violations were found in the AD and MO and AD and UA pairs consistently across all subgroups except for respondents without self-reported chronic illness, depression, arthritis, and Canadian respondents (Table <a href="#Tab4" data-ref-type="table">4</a>). Backward item selection recommended excluding AD for all subsamples that detected violations except for Norway. Critical values for Norway were 34 for UA and 50 for AD, demonstrating non-serious misfit. Figure <a href="#Fig3" data-ref-type="fig">3</a> plots IRF of item pairs AD/MO and AD/UA for subgroups which did not recommend AD for removal. Not surprisingly, AD was easier to endorse at all rest score groups than MO or UA for the subgroup with depression, and the IRFs are far enough apart that they do not intersect.

<figure id="Fig3">
<p><img src="11136_2021_2922_Fig3_HTML.jpg" id="MO3" /></p>
<figcaption>Paired item response functions of anxiety/depression with mobility and usual activities, across selected subgroups</figcaption>
</figure>

H<sub>ij</sub> tends to be largest between AD and UA, AD and PD across all subsamples except for healthy respondents, those reporting hearing problems and the Australian sample, showing that AD is more closely related to UA and PD than MO and SC (Table <a href="#Tab5" data-ref-type="table">5</a>). H<sub>ij</sub> between AD and all the other EQ-5D-5L items was particularly small for the healthy subsample.

<div id="Tab5" class="table-wrap">

<div class="caption">

Item pair coefficient for anxiety/depression

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Mobility</th>
<th colspan="2" style="text-align: left;">Self-Care</th>
<th colspan="2" style="text-align: left;">Usual activities</th>
<th colspan="2" style="text-align: left;">Pain/Discomfort</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
<th style="text-align: left;">H<sub>ij</sub></th>
<th style="text-align: left;">(SE)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Complete sample</td>
<td>0.292</td>
<td style="text-align: left;">(0.014)</td>
<td>0.364</td>
<td style="text-align: left;">(0.018)</td>
<td>0.448</td>
<td style="text-align: left;">(0.013)</td>
<td>0.398</td>
<td style="text-align: left;">(0.013)</td>
</tr>
<tr>
<td style="text-align: left;">Healthy sample</td>
<td>0.117</td>
<td style="text-align: left;">(0.043)</td>
<td>0.167</td>
<td style="text-align: left;">(0.080)</td>
<td>0.169</td>
<td style="text-align: left;">(0.047)</td>
<td>0.252</td>
<td style="text-align: left;">(0.034)</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Self-reported chronic condition</td>
</tr>
<tr>
<td style="text-align: left;"> Asthma</td>
<td>0.297</td>
<td style="text-align: left;">(0.042)</td>
<td>0.249</td>
<td style="text-align: left;">(0.050)</td>
<td>0.395</td>
<td style="text-align: left;">(0.041)</td>
<td>0.419</td>
<td style="text-align: left;">(0.042)</td>
</tr>
<tr>
<td style="text-align: left;"> Cancer</td>
<td>0.301</td>
<td style="text-align: left;">(0.042)</td>
<td>0.376</td>
<td style="text-align: left;">(0.053)</td>
<td>0.415</td>
<td style="text-align: left;">(0.040)</td>
<td>0.378</td>
<td style="text-align: left;">(0.042)</td>
</tr>
<tr>
<td style="text-align: left;"> Depression</td>
<td>0.155</td>
<td style="text-align: left;">(0.023)</td>
<td>0.294</td>
<td style="text-align: left;">(0.034)</td>
<td>0.356</td>
<td style="text-align: left;">(0.029)</td>
<td>0.176</td>
<td style="text-align: left;">(0.023)</td>
</tr>
<tr>
<td style="text-align: left;"> Diabetes</td>
<td>0.330</td>
<td style="text-align: left;">(0.036)</td>
<td>0.349</td>
<td style="text-align: left;">(0.052)</td>
<td>0.447</td>
<td style="text-align: left;">(0.037)</td>
<td>0.434</td>
<td style="text-align: left;">(0.034)</td>
</tr>
<tr>
<td style="text-align: left;"> Hearing Problems</td>
<td>0.228</td>
<td style="text-align: left;">(0.048)</td>
<td>0.329</td>
<td style="text-align: left;">(0.072)</td>
<td>0.293</td>
<td style="text-align: left;">(0.051)</td>
<td>0.372</td>
<td style="text-align: left;">(0.047)</td>
</tr>
<tr>
<td style="text-align: left;"> Arthritis</td>
<td>0.214</td>
<td style="text-align: left;">(0.029)</td>
<td>0.286</td>
<td style="text-align: left;">(0.037)</td>
<td>0.318</td>
<td style="text-align: left;">(0.030)</td>
<td>0.309</td>
<td style="text-align: left;">(0.030)</td>
</tr>
<tr>
<td style="text-align: left;"> Heart Disease</td>
<td>0.355</td>
<td style="text-align: left;">(0.034)</td>
<td>0.386</td>
<td style="text-align: left;">(0.050)</td>
<td>0.423</td>
<td style="text-align: left;">(0.034)</td>
<td>0.455</td>
<td style="text-align: left;">(0.035)</td>
</tr>
<tr>
<td colspan="9" style="text-align: left;">Country of Survey Sample</td>
</tr>
<tr>
<td style="text-align: left;"> Australia</td>
<td>0.204</td>
<td style="text-align: left;">(0.033)</td>
<td>0.346</td>
<td style="text-align: left;">(0.048)</td>
<td>0.324</td>
<td style="text-align: left;">(0.035)</td>
<td>0.318</td>
<td style="text-align: left;">(0.033)</td>
</tr>
<tr>
<td style="text-align: left;"> USA</td>
<td>0.334</td>
<td style="text-align: left;">(0.031)</td>
<td>0.390</td>
<td style="text-align: left;">(0.044)</td>
<td>0.470</td>
<td style="text-align: left;">(0.030)</td>
<td>0.467</td>
<td style="text-align: left;">(0.029)</td>
</tr>
<tr>
<td style="text-align: left;"> UK</td>
<td>0.296</td>
<td style="text-align: left;">(0.031)</td>
<td>0.326</td>
<td style="text-align: left;">(0.040)</td>
<td>0.402</td>
<td style="text-align: left;">(0.032)</td>
<td>0.362</td>
<td style="text-align: left;">(0.030)</td>
</tr>
<tr>
<td style="text-align: left;"> Canada</td>
<td>0.298</td>
<td style="text-align: left;">(0.034)</td>
<td>0.329</td>
<td style="text-align: left;">(0.048)</td>
<td>0.470</td>
<td style="text-align: left;">(0.032)</td>
<td>0.452</td>
<td style="text-align: left;">(0.030)</td>
</tr>
<tr>
<td style="text-align: left;"> Norway</td>
<td>0.185</td>
<td style="text-align: left;">(0.038)</td>
<td>0.367</td>
<td style="text-align: left;">(0.056)</td>
<td>0.520</td>
<td style="text-align: left;">(0.036)</td>
<td>0.376</td>
<td style="text-align: left;">(0.034)</td>
</tr>
<tr>
<td style="text-align: left;"> Germany</td>
<td>0.331</td>
<td style="text-align: left;">(0.031)</td>
<td>0.389</td>
<td style="text-align: left;">(0.036)</td>
<td>0.507</td>
<td style="text-align: left;">(0.028)</td>
<td>0.380</td>
<td style="text-align: left;">(0.031)</td>
</tr>
</tbody>
</table>

*H*<sub>*ij*</sub> Coefficient H for item pairs, *SE* Standard Error

</div>

## Discussion

The EQ-5D-5L items form a strong Mokken scale, fitting the MHM and thus demonstrating that LSS, an additive summary score independent of population value sets, is acceptable and meaningful for measurement. These results empirically demonstrate that the EQ-5D-5L LSS orders respondents along a latent variable of health, with higher score indicating poorer health. The MHM fit of the EQ-5D-5L data reflects the rigorous work in questionnaire development, especially with refinement of the response levels \[19, 27, 42\]. Meijer and colleagues cautioned that sometimes strong Mokken scales are not optimal because they could reflect items covering similar or overlapping content \[43, 44\]. However, the EQ-5D is a brief scale with items covering diverse aspects of function and symptoms, so this concern is minimized.

MIIO results suggest that an interpretation of functional limitations and health symptoms can also be applied to the LSS: the low range of the score represents mainly problems with PD and AD, the lower to mid-range scores indicate additional problems with MO and UA, while the middle to higher scores reveal limitations in SC. The ordering of these items was found to be moderate. The finding that item ordering was not accurate for the healthy sub-sample reflected the observation of less variation in EQ-5D-5L responses in that subsample.

Our results empirically demonstrate what is conceptually understood: the LSS of the EQ-5D-5L orders persons by their levels of health. The relatively consistent performance of the EQ-5D-5L scale across countries is encouraging for the purpose of providing evidence to support the use of the LSS to compare the EQ-5D across countries. This is important because the EQ-5D has historically been scored using weights based on country-specific societal preferences. The LSS is used to describe data quality of valuation studies \[45, 46\] but has yet seen broader acceptance. A summary scoring function independent of population-specific value sets that is simple, psychometrically valid, and international in its applicability has tremendous advantages for researchers and population health scientists who wish to have a composite indicator of health for international comparisons using a measure available in hundreds of languages and is freely licensed and distributed by the EuroQol by non-profit organizations.

Although AD was initially retained in the scale as its H<sub>i</sub> was above the commonly accepted cutoff of 0.3, it was excluded when the cutoff was only raised to above 0.378. Additionally, AD was found to violate MIIO in most subgroups—its IRF crosses the UA and MO IRFs at rest scores 3–4—and AD removal from the scale was suggested in backward model selection. The determination of whether an item should remain in a scale is not based solely on H<sub>i</sub> but depends on conceptual and empirical considerations and the application of the instrument. When AD was omitted, H<sub>s</sub> and H<sup>T</sup> improved to above 0.7 to indicate very strong person and item ordering. Therefore, in applications where scalability or item ordering is required to be strong, one could apply the LSS to only the four physical items of the EQ-5D and assess the AD item separately. Although the EQ-5D is rarely used as a diagnostic tool on the level of individual patients, item ordering can still be relevant for group level applications. For example, although patient groups with mainly physical symptoms do not suffer from anxiety/depressive problems more than the general population, the AD item may be more difficult to endorse than the physical items at moderate or more severe levels of disease (as indicated in these results). However, for conditions for which mental health is affected, the AD item could be easier to endorse than MO, SC and UA across the scale (as supported by our findings of MIIO in the subgroup with depression). The relationship between items may also be modified by other factors such as age or gender. This is an area needing future research.

IRT approaches to evaluating the EQ-5D have been relatively scarce in the literature: our results are comparable to available evidence. A recent investigation of the EQ-5D using Rasch rating scale model reported similar item ordering as our findings: PD was the easiest to endorse, UA, AD, and MO are at middle levels of difficulty of endorsement, and SC was the most difficult to endorse item \[21\]. Our scalability results were similar to previously published results for the physical function subscale of the SF-36—H<sub>S</sub> of 0.69 and H<sup>T</sup> of 0.53 \[44\].

IRT assumes items are indicators of a single latent variable. However, the EQ-5D was constructed using five different dimensions to create a composite measure of health status. AD conceptually measures mental health, while the other four items address physical health \[48–50\]. A previous study revealed that when several health measures were modeled with the EQ-5D-5L, MO, SC, and UA belonged to one dimension, AD to a second, and PD to a third \[51\]. However, other investigations found sufficient evidence that self-reported physical and mental health can be summarized using a single score \[52\]. Recent confirmatory factor analysis found the model including all five EQ-5D-5L items to have acceptable fit statistics \[47\]. These previous findings along with this study illustrate the tension between the multidimensional nature of health and summarizing health as a single latent construct. The theoretical measurement model, such as whether the EQ-5D is a formative or reflective measurement \[47, 54, 55\], must be considered when applying scoring approaches.

A limitation of this study was that the dataset only included adult participants from Western, developed countries. If person and item ordering are dependent on how item descriptions and response categories are interpreted, then these results may not extend to other populations. Further, the data were collected via online survey panels, and such participants may differ from the general population \[29\]. There is also a pressing need to conduct similar research in children. Due to ethical, methodological, and conceptual problems involved in eliciting preferences for children, the version of the EQ-5D for children and adolescents (EQ-5D-Y) does not have a preference value set \[53\]. Therefore, application of the LSS may be particularly relevant for the EQ-5D-Y as its use expands.

## Conclusion

A conceptually cohesive scale of health can be operationalized using the LSS using all five items of the EQ-5D-5L as higher LSS scores indicate worse health and more severe functional limitations. In general, lower range of the score represents mainly problems with pain, the mid-range indicates additional problems with mobility and usual activities, and middle to higher range of scores reveals additional limitations with self-care. Anxiety/depression is easier to endorse than MO or UA at the lower range of scores, but at moderate and higher scores becomes more difficult to endorse. Compared to utility scores, LSS scores have advantages depending on the application and subgroup/population. However, the scale is weak in the healthy subsample, indicating it may be less informative in such populations. More work must be done to investigate whether person and item order holds for other populations, especially for children and adolescents.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (R 12 KB)

</div>

<div class="caption">

Supplementary file2 (DOCX 48 KB)

</div>

<div class="caption">

Supplementary file3 (DOCX 24 KB)

</div>

### Acknowledgements

EuroQol group for funding this research and investigators of the Multiple Comparison Project for sharing their data. This project was supported by the EuroQol Research Foundation (Grant Number: EQ Project 20170130). The submitted manuscript was not censored or directed by the foundation. The views expressed by the authors in the publication do not necessarily reflect the view of the EuroQol Group.

#### Supporting Information

Supplementary Material Table 1B: EQ-5D-5L Characteristics Across Health Conditions of the MIC Dataset

Supplementary Material Table 1C: EQ-5D-5L Characteristics Across Country Subsamples of the MIC Dataset

### Funding

Open Access funding enabled and organized by Projekt DEAL. EuroQol group fully funded this project (Grant ID EQ Project 20170130).

### Declarations

#### Conflict of Interest

All authors are members of the EuroQol group. Outside of scientific meetings, group members do not receive any financial support. Ruixuan Jiang is an employee of Merck; however, conceptualization and most of study analyses were completed during her graduate studies.

#### Ethical approval

This paper only used secondary data and authors did not contain human or animal data collection performed by any of the authors.

## References

1. Brazier J, Ara R, Rowen D, Chevrou-Severac H. A review of generic preference-based measures for use in cost-effectiveness models. PharmacoEconomics. 2017;35(1):21–31. doi:10.1007/s40273-017-0545-x

2. van Reenen, M., & Janssen, B. (2015, April 2015). EQ-5D-5L User guide: Basic information on how to use the EQ-5D-5L instrument. 2.1. Retrieved January 23, 2017, from http://www.euroqol.org/fileadmin/user_upload/Documenten/PDF/Folders_Flyers/EQ-5D-5L_UserGuide_2015.pdf.

3. APERSU - Alberta PROMS and EQ-5D Research and Support Unit. from http://apersu.ca/.

4. Brooks R. EuroQol Group after 25 Years. 2013. Rotterdam, The Netherlands, Springer.

5. Devlin, N., & Appleby, J. (2010). Getting the most out of PROMS - Putting health outcomes at the heart of NHS decision-making. Retrieved January 5, 2017, from https://www.kingsfund.org.uk/sites/files/kf/Getting-the-most-out-of-PROMs-Nancy-Devlin-John-Appleby-Kings-Fund-March-2010.pdf.

6. Devlin NJ, Brooks R. EQ-5D and the EuroQol group: Past, present and future. Applied Health Economics and Health Policy. 2017;15(2):127–137. doi:10.1007/s40258-017-0310-5

7. Devlin NJ, Parkin D, Browne J. Patient-reported outcome measures in the NHS: New methods for analysing and reporting EQ-5D data. Health Economics. 2010;19(8):886–905. doi:10.1002/hec.1608

8. Hostetter, M., & Klein, S. (2012). Using Patient-Reported Outcomes to Improve Health Care Quality. Retrieved January 5, 2017, from http://www.commonwealthfund.org/publications/newsletters/quality-matters/2011/december-january-2012/in-focus.

9. Parkin D, Rice N, Devlin N. Statistical analysis of EQ-5D profiles: Does the use of value sets bias inference?. Medical Decision Making. 2010;30(5):556–565. doi:10.1177/0272989X09357473

10. Hernandez G, Garin O, Pardo Y, Vilagut G, Pont A, Suarez M, Neira M, Rajmil L, Gorostiza I, Ramallo-Farina Y, Cabases J, Alonso J, Ferrer M. Validity of the EQ-5D-5L and reference norms for the Spanish population. Quality of Life Research. 2018;27(9):2337–2348. doi:10.1007/s11136-018-1877-5

11. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goni JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation Work: Version 2 of the EQ-5D-5L valuation protocol. Value in Health. 2019;22(1):23–30. doi:10.1016/j.jval.2018.05.010

12. Gutacker N, Bojke C, Daidone S, Devlin N, Street A. Hospital variation in patient-reported outcomes at the level of EQ-5D dimensions: Evidence from England. Medical Decision Making. 2013;33(6):804–818. doi:10.1177/0272989X13482523

13. Wilke CT, Pickard AS, Walton SM, Moock J, Kohlmann T, Lee TA. Statistical implications of utility weighted and equally weighted HRQL measures: An empirical study. Health Economics. 2010;19(1):101–110. doi:10.1002/hec.1467

14. Lamu AN, Gamst-Klaussen T, Olsen JA. Preference weighting of health state values: What difference does it make, and why?. Value Health. 2017;20(3):451–457. doi:10.1016/j.jval.2016.10.002

15. Prieto L, Sacristan JA. What is the value of social values? The uselessness of assessing health-related quality of life through preference measures. BMC Medical Research Methodology. 2004;4:10. doi:10.1186/1471-2288-4-10

16. Devlin N, Parkin D, Janssen B. Analysis of EQ-5D Profiles. Methods for Analysing and Reporting EQ-5D Data. 2020:23–49. Cham, Springer International Publishing.

17. Geraerds AJLM, Bonsel GJ, Janssen MF, de Jongh MA, Spronk I, Polinder S, Haagsma JA. The added value of the EQ-5D with a cognition dimension in injury patients with and without traumatic brain injury. Quality of Life Research. 2019;28(7):1931–1939. doi:10.1007/s11136-019-02144-6

18. Yang ZH, Luo N, Bonsel G, Busschbach J, Stolk E. Effect of health state sampling methods on model predictions of EQ-5D-5L values: Small designs can suffice. Value in Health. 2019;22(1):38–44. doi:10.1016/j.jval.2018.06.015

19. Pickard AS, Kohlmann T, Janssen MF, Bonsel G, Rosenbloom S, Cella D. Evaluating equivalency between response systems: Application of the Rasch model to a 3-level and 5-level EQ-5D. Medical Care. 2007;45(9):812–819. doi:10.1097/MLR.0b013e31805371aa

20. van Hout B, Janssen MF, Feng YS, Kohlmann T, Busschbach J, Golicki D, Lloyd A, Scalone L, Kind P, Pickard AS. Interim scoring for the EQ-5D-5L: Mapping the EQ-5D-5L to EQ-5D-3L value sets. Value Health. 2012;15(5):708–715. doi:10.1016/j.jval.2012.02.008

21. Wahlberg M, Zingmark M, Stenberg G, Munkholm M. Rasch analysis of the EQ-5D-3L and the EQ-5D-5L in persons with back and neck pain receiving physiotherapy in a primary care context. European Journal of Physiotherapy. 2021;23(2):102–109.

22. Pickard AS, De Leon MC, Kohlmann T, Cella D, Rosenbloom S. Psychometric comparison of the standard EQ-5D to a 5 level version in cancer patients. Medical Care. 2007;45(3):259–263. doi:10.1097/01.mlr.0000254515.63841.81

23. Sijtsma K, van der Ark LA. A tutorial on how to do a Mokken scale analysis on your test and questionnaire data. British Journal of Mathematical & Statistical Psychology. 2017;70(1):137–158. doi:10.1111/bmsp.12078

24. van der Ark LA, Bergsma WP. A note on stochastic ordering of the latent trait using the sum of polytomous item scores. Psychometrika. 2010;75(2):272–279.

25. Sijtsma K, Molenaar IW. Introduction to Nonparametric Item Response Theory. 2002. Thousand Oaks, CA, SAGE Publications Inc.

26. van Schuur WH. Mokken scale analysis: Between the Guttman scale and parametric item response theory. Political Analysis. 2003;11(2):139–163.

27. Herdman M, Gudex C, Lloyd A, Janssen M, Kind P, Parkin D, Bonsel G, Badia X. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality of Life Research. 2011;20(10):1727–1736. doi:10.1007/s11136-011-9903-x

28. Richardson J, Khan MA, Iezzi A, Maxwell A. Comparing and explaining differences in the magnitude, content, and sensitivity of utilities predicted by the EQ-5D, SF-6D, HUI 3, 15D, QWB, and AQoL-8D multiattribute utility instruments. Medical Decision Making. 2015;35(3):276–291. doi:10.1177/0272989X14543107

29. Richardson JL, Angelo; Maxwell, Aimee;. Cross-national comparison of twelve quality of life instruments: MIC paper 1: Background, questions, instruments, research paper 76. 2012. Melbourne, Australia, Monash University.

30. StataCorp. Stata Statistical Software: Release 13. 2013. College Station, TX, StataCorp LP.

31. R Development Core Team. R: A Language and Environment for Statistical Computing (Version 3.5.2). 2018. Vienna, Austria, R Foundation for Statistical Computing.

32. Van der Ark, L. A. (2007). Mokken Scale Analysis in R. 2007, 20(11), 19.

33. van der Ark, L. A. (2012). New Developments in Mokken Scale Analysis in R. 2012, 48(5), 27.

34. Molenaar I, van der Linden WJ, Hambleton RK. Nonparametric Models for Polytomous Responses. Handbook of Modern Item Response Theory. 1997:369–380. New York, NY, Springer.

35. Wind SA. An instructional module on mokken scale analysis. Educational Measurement-Issues and Practice. 2017;36(2):50–66.

36. Sijtsma K, Molenaar IW. Reliability of Test-scores in nonparametric item response theory. Psychometrika. 1987;52(1):79–97.

37. Callender J, Osburn H. An empirical comparison of coefficient alpha, Guttman's Lambda-2, and MSPLIT maximized split-half reliability estimates. Journal of Educational Measurement. 2005;16:89–99.

38. Guttman L. A basis for analyzing test-retest reliability. Psychometrika. 1945;10(4):255–282. doi:10.1007/BF02288892

39. Sijtsma K, Meijer R, van der Ark A. Mokken scale analysis as time goes by: An update for scaling practitioners. Personality and Individual Differences. 2011;50:31–37.

40. Ligtvoet R, van der Ark A, Bergsma W, Sijtsma K. Polytomous latent scales for the investigation of the ordering of items. Psychometrika. 2011;76:200–216.

41. Ligtvoet R, van der Ark LA, te Marvelde JM, Sijtsma K. Investigating an invariant item ordering for polytomously scored items. Educational and Psychological Measurement. 2010;70(4):578–595.

42. Luo N, Li M, Liu GG, Lloyd A, de Charro F, Herdman M. Developing the Chinese version of the new 5-level EQ-5D descriptive system: The response scaling approach. Quality of Life Research. 2013;22(4):885–890. doi:10.1007/s11136-012-0200-0

43. Meijer RR, Baneke JJ. Analyzing psychopathology items: A case for nonparametric item response theory modeling. Psychological Methods. 2004;9(3):354–368. doi:10.1037/1082-989X.9.3.354

44. Meijer RR, Egberink IJL. Investigating invariant item ordering in personality and clinical scales: Some empirical findings and a discussion. Educational and Psychological Measurement. 2012;72(4):589–607.

45. Golicki D, Jakubczyk M, Graczyk K, Niewada M. Valuation of EQ-5D-5L health states in Poland: The first EQ-VT-based study in central and Eastern Europe. PharmacoEconomics. 2019;37(9):1165–1176. doi:10.1007/s40273-019-00811-7

46. Pickard AS, Law EH, Jiang R, Oppe M, Shaw JW, Xie F, Boye KS, Gong CL, Chapman RH, Balch A. United States valuation of EQ-5D-5L health States: An initial model using a standardized protocol. Value in Health. 2018;21:S4–S5. doi:10.1016/j.jval.2019.02.009

47. Feng YS, Jiang R, Kohlmann T, Pickard AS. Exploring the internal structure of the EQ-5D using non-preference-based methods. Value Health. 2019;22(5):527–536. doi:10.1016/j.jval.2019.02.006

48. Davis JC, Liu-Ambrose T, Richardson CG, Bryan S. A comparison of the ICECAP-O with EQ-5D in a falls prevention clinical setting: Are they complements or substitutes?. Quality of Life Research. 2013;22(5):969–977. doi:10.1007/s11136-012-0225-4

49. Keeley T, Coast J, Nicholls E, Foster NE, Jowett S, Al-Janabi H. An analysis of the complementarity of ICECAP-A and EQ-5D-3 L in an adult population of patients with knee pain. Health and Quality of Life Outcomes. 2016;14:36. doi:10.1186/s12955-016-0430-x

50. Wittrup-Jensenm KL, Jørgen. An Assessment of Two Generic Health-Related Quality of Life (HRQoL) Instruments in Patients Suffering from Low Back Pain. 2008. Odense, University of Southern Denmark.

51. Finch AP, Brazier JE, Mukuria C, Bjorner JB. An exploratory study on using principal-component analysis and confirmatory factor analysis to identify bolt-on dimensions: The EQ-5D case study. Value Health. 2017;20(10):1362–1375. doi:10.1016/j.jval.2017.06.002

52. Yin S, Njai R, Barker L, Siegel P, Liao Y. Summarizing health-related quality of life (HRQOL): Development and testing of a one-factor model. Population Health Metrics. 2016;14(1):22. doi:10.1186/s12963-016-0091-3

53. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: The instrument's characteristics, development, current use, and challenges of developing its value set. Value Health. 2019;22(1):31–37. doi:10.1016/j.jval.2018.11.001

54. Costa DS. Reflective, causal, and composite indicators of quality of life: A conceptual or an empirical distinction?. Quality of Life Research. 2015;24(9):2057–2065. doi:10.1007/s11136-015-0954-2

55. Gamst-Klaussen T, Gudex C, Olsen JA. Exploring the causal and effect nature of EQ-5D dimensions: An application of confirmatory tetrad analysis and confirmatory factor analysis. Health and quality of life outcomes. 2018;16(1):153–215. doi:10.1186/s12955-018-0975-y

---
project_id: "1627-RA"
work_id: "doi:10.1186/s12955-025-02421-8"
doi: "10.1186/s12955-025-02421-8"
pmid: "41057923"
pmcid: "PMC12506383"
title: "Health-related quality of life in COVID-19 patients: a systematic review and meta-analysis of EQ-5D studies"
journal: "Health and Quality of Life Outcomes"
publication_date: "2025-10-07"
volume: "23"
authors:
  - name: "Kidu Gidey"
    affiliation_ids:
      - "Aff1"
  - name: "Yirga Legesse Niriayo"
    affiliation_ids:
      - "Aff1"
  - name: "Solomon Weldegebreal Asgedom"
    affiliation_ids:
      - "Aff1"
  - name: "Erica Lubetkin"
    affiliation_ids:
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/04bpyvy69grid.30820.390000 0001 1539 8988Department of Clinical Pharmacy, School of Pharmacy, College of Health Sciences, Mekelle University, Mekelle, Ethiopia"
  - id: "Aff2"
    name: "https://ror.org/00wmhkr98grid.254250.40000 0001 2264 7145Department of Community Health and Social Medicine, CUNY School of Medicine, New York, NY USA"
keywords:
  - "COVID-19"
  - "EQ-5D"
  - "HRQoL"
  - "Health-Related quality of life"
  - "Systematic review"
licence: "cc-by"
source_file: "input/projects/1627-RA/papers/doi_10.1186_s12955-025-02421-8.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12506383/fullTextXML"
source_method: "epmc_xml"
source_sha256: "69f528610fb97eb60c0542a9778eaf007491e7722fbf685732feb7d3b1e8c694"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Health-related quality of life in COVID-19 patients: a systematic review and meta-analysis of EQ-5D studies

## Abstract

### Background

COVID-19 has affected millions globally, with a significant proportion experiencing long-COVID and impaired health-related quality of life (HRQoL). This systematic review and meta-analysis aimed to synthesize the existing literature on HRQoL in COVID-19 patients.

### Methods

We conducted a systematic search of PubMed, Embase, Web of Science, Scopus, and the Cochrane Library for studies published between December 2019 and March 2025. Eligible studies were peer-reviewed and assessed HRQoL in COVID-19 patients using the EQ-5D instrument. Study quality and risk of bias were evaluated using the Newcastle-Ottawa Scale. Pooled health utility values were estimated using a random-effects model, and heterogeneity was assessed via I<sup>2</sup> statistics. Predictors of poor HRQoL were qualitatively narrated.

### Results

Out of 3539 references, 187 studies with 116,525 participants were analyzed. The majority (80.2%) used the EQ-5D-5 L version. The pooled mean EQ-5D utility score was 0.76 (95% CI 0.74–0.79, I<sup>2</sup> = 99.9%) while the mean EQ-5D Visual Analogue Scale (VAS) score was 70.76 (95% CI 68.48–73.04; I<sup>2</sup> = 99.7%). Pain/discomfort and anxiety/depression were the most affected domains, reported by 51% and 46% of patients, respectively. Subgroup analysis showed significant differences in HRQoL based on national income status (*p* = 0.038) and geographic region (*p* \< 0.001). Common predictors of lower HRQoL included older age, female gender, disease severity, comorbidities, and post-COVID-19 symptoms.

### Conclusion

This systematic review demonstrates a substantial reduction in HRQoL among COVID-19 patients compared to the general population. The pooled utility values of COVID-19 contribute to understanding patients’ HRQoL and can assist in calculating Quality-Adjusted Life Years. This provides essential data for future economic evaluations and informs health policy decisions.

### Supplementary Information

The online version contains supplementary material available at 10.1186/s12955-025-02421-8.

## Introduction

COVID-19 was discovered in December 2019 in Wuhan, China. Thereafter, the virus continued to spread, affecting millions of individuals across the world \[1\]. COVID-19 presents a wide spectrum of symptoms, ranging from mild to life-threatening, with many patients experiencing prolonged effects known as long COVID \[2–4\]. As a result of the persistent symptoms and complications, people with long COVID face significant reductions in health-related quality of life (HRQoL) \[5, 6\]. Therefore, HRQoL has become a crucial outcome measure for understanding the broader impact of COVID-19.

A variety of validated surveys exist for measuring a patient’s HRQoL, which mainly include the EQ-5D, Health Utilities Index (HUI), and Short-Form 6-Dimension (SF-6D) questionnaires \[7\]. The EQ-5D is the most widely used HRQoL instrument due to its robustness, reliability, and responsiveness across many health conditions and countries \[8\]. It is also a preferred method for evaluating health state utilities involved in health technology assessment as recommended by National Institute for Health and Care Excellence (NICE) \[9\]. Compared with instruments such as the SF-36 or HUI, the EQ-5D is well suited for COVID-19 research due to its extensive validation, brevity, and ease of use, making it particularly appropriate for rapid evaluation in both clinical and community settings during a pandemic when timely measurement is critical \[10\]. However, EQ-5D may not fully capture some aspect of quality of life such as fatigue, cognitive dysfunction, and breathlessness which are common symptoms of long-COVID not explicitly represented in its five dimensions \[11\].

The EQ-5D questionnaire consists of two components: the descriptive system and the visual analogue scale (EQ-VAS) \[12\]. The descriptive system assesses the current self-reported health status in five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. The EQ-5D dimensions, such as mobility and self-care, are critical for assessing COVID-19’s impact. Both acute and long COVID often impair physical functioning and daily independence more abruptly than many chronic conditions, and studies report significant declines in these symptoms among affected patients \[13\].

The EQ-VAS evaluates the overall health status of the respondent on a visual analogue scale ranging from 0 (worst imaginable health) to 100 (best imaginable health). Two versions of the EQ-5D are available: the EQ-5D-3 L and the EQ-5D-5 L. The key difference between these versions lies in the descriptive system, with the EQ-5D-3 L having 3 levels of severity for each dimension (no problems, some problems, extreme problems) and the EQ-5D-5 L offering 5 levels (adding mild and severe problems) to provide greater sensitivity. The EQ-5D index is calculated by applying a ‘value set/tariff’ to each health profile, converting the descriptive data into a single summary score. These tariffs are derived from population-based surveys and are specific to individual countries or regions, reflecting the societal preferences for different health states \[14\]. The recall period for EQ-5D is today \[15\].

The HRQoL measured by EQ-5D plays a crucial role in economic evaluation \[8\] Systematic reviews and meta-analyses, considered the highest level of evidence, enhance the precision and generalizability of EQ-5D utility values by employing formal synthesis techniques that pool data from multiple studies \[16\]. As economic analysts increasingly rely on these comprehensive reviews to inform decision-analytic models, experts advocate for transparent and high-quality meta-analyses to strengthen the evidence base, ensuring better decision-making and outcomes in economic evaluations \[17, 18\].

Understanding the impact of COVID-19 on HRQoL is crucial for healthcare professionals and policymakers in developing effective interventions. Long COVID has emerged as a significant public health concern globally, defined by the World Health Organization as persistent symptoms occurring at least three months after the initial SARS-CoV-2 infection onset, lasting for at least two months, and not explained by an alternative diagnosis \[19\]. Millions of people have been affected with long COVID since the beginning of the pandemic with substantial implications for HRQoL \[20\]. While numerous studies have investigated the impact of COVID-19 on HRQoL, a comprehensive analysis particularly using the EQ-5D is still lacking. Existing systematic reviews have documented significant HRQoL reductions among COVID-19 survivors; however, some did not report utility values \[21\] which are essential for economic evaluation, while others relied on a variety of measurement tools and included only a small number of studies conducted during the early stages of the pandemic \[22, 23\]. In addition, there are several articles that have been published since the last reviews, and a comprehensive analysis would be beneficial to provide a pooled utility values and with extensive subgroup analysis. This study aimed to systematically review the available evidence on COVID-19 patients’ HRQoL using the EQ-5D, estimate pooled utility values, identify key influencing factors, explore subgroup differences, and assess the most affected EQ-5D dimensions.

## Materials and methods

### Study design

This review was developed in accordance with Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (Appendix 1) \[24\]. Protocol registration was not undertaken for this systematic review, as our aim was not to estimate treatment effects.

### Search strategy

A systematic search of all studies published between December 1, 2019, and March 1, 2025, was conducted in PubMed, Embase, Web of Science, Scopus, and Cochrane Library. We developed search strings using a combination of keywords related to the EQ-5D and COVID-19. The complete search terms for each database are provided in Table <a href="#MOESM1" data-ref-type="media">S1</a>. In addition, we systematically hand-searched the reference lists of all included studies and relevant reviews to identify any additional eligible articles not captured through electronic database searches. However, gray literature was not included, as we focused on peer-reviewed publications to ensure consistency and reliability in study quality.

### Eligibility criteria

#### Inclusion criteria

Studies were eligible for inclusion if they met the following criteria:

- Report on HRQoL in patients with COVID-19.

- Reported either or both EQ-5D index values and EQ-VAS scores using the EQ-5D-3 L or EQ-5D-5 L instruments involving adult populations.

- Were reported in English.

#### Exclusion criteria

Studies were excluded if:

- They were editorial, letter to the editor, comment, narrative case report, or opinion article.

- They were a review, intervention or a protocol.

- The EQ-5D outcomes (utility values or EQ-VAS) were not reported.

- Studies reported EQ-5D values derived from mapping other measures of health outcomes.

- No relevant data were presented (e.g. only abstract is available or full text not available).

### Study selection

The titles and abstracts of all identified studies were exported into EndNote (version 20.0.1, 2020 Clarivate), a reference management software, and duplicates were removed. The titles and abstracts of articles from the electronic database searches were independently screened by two reviewers using the pre-specified eligibility criteria (first screening). After the title/abstract review, full-text articles were reviewed by two reviewers to evaluate the eligibility of studies for inclusion (second screening). Discrepancies regarding study inclusion were resolved through consensus with a third author.

### Risk-of-bias (quality) assessment

Quality was assessed using the Newcastle-Ottawa scale (NOS) for cohort and case-control studies \[25\] and the adapted NOS tool for cross-sectional studies \[26\] (Appendix 2). Two reviewers independently assessed the risk of bias/quality appraisal. Any discrepancies were solved by a discussion or by consulting a third researcher. Judgments on the overall risk of bias were categorized as either low, moderate, or high risk based on the quality score.

### Data extraction

Data extraction was performed by two independent researchers using a data extraction form prepared on Microsoft Excel (Version 2016). For each included study, the following data were extracted:

- Publication details: authors, publication date, country/countries where study was conducted.

- Study design.

- Number of participants, mean age, percentage of males and females.

- Socio-demographic characteristics (educational status, income level, employment status, smoking status, residence (urban or rural)).

- Location of the participants (e.g. ICU, inpatient (wards), community).

- Version of EQ-5D descriptive system (e.g., EQ-5D-3 L, EQ-5D-5 L).

- Mode of administration of the EQ-5D instruments (self-complete, interviewer-administered, digital).

- Response rate in percentage.

- Mean duration of COVID-19 at the time of assessment of EQ-5D instruments.

- Comorbidities (percentage of patients with hypertension, diabetes mellitus, asthma, COPD, coronary artery disease, kidney disease, malignancy, HIV/AIDS).

- Severity of the disease (asymptomatic, mild, moderate, severe).

- Tariff used.

- EQ-5D index scores (5 L and 3 L).

- EQ-VAS scores.

- EQ-5D health profiles \[Percentage reporting no problem in each dimension\].

There were many rounds of scientific meetings among the three investigators for consensus on any differences in article screening, selection, and data extraction.

### Statistical analysis

Data were recorded using a Microsoft Excel sheet (version 16). All statistical analyses were performed using R version 4.3.3 (R Foundation for Statistical Computing, Vienna, Austria). The selected studies were reviewed, and the pooled estimate of health utility values (the means of EQ-5D utility scores and EQ-VAS scores) were computed by a Random effect model meta-analysis (DerSimonian–Laird method). Heterogeneity among included studies was assessed using the I<sup>2</sup> statistics \[27\]. We conducted sensitivity analyses to assess the robustness of the results, and Egger’s regression test was used to examine publication bias.

Most studies reported the mean health utility values. For studies presenting median values with interquartile ranges or overall ranges, we estimated corresponding means and standard deviations using established techniques \[28, 29\]. However, these methods are primarily established under the assumption of normal data and perform poorly for skewed distributions, potentially leading to biased or less accurate estimates \[29\]; this limitation should be considered when interpreting the pooled estimates. In cases where EQ-5D utility scores and VAS scores were measured at multiple time points; we used the data from the final assessment. Depending on the availability of data, subgroup analyses were performed using the following covariates: age group (e.g., over 60 years old, under 60 years old), study design, timing of HRQoL measurements after COVID-19 diagnosis (HRQoL at \< 12 weeks vs. HRQoL at ≥ 12 weeks), geographical regions, low-middle income vs. high-income countries, and version of the EQ-5D instruments (3 L vs. 5 L).

## Results

### Study selection

A total of 3539 references were initially retrieved from the databases. Following the removal of duplicates, 1905 records underwent further evaluation through title and abstract screening. A full-text examination was then performed on 528 studies, leading to the selection of 187 studies for systematic review and meta-analysis. No further relevant studies were identified through manual searching. Study selection process is illustrated in a PRISMA flow diagram shown in Fig. <a href="#Fig1" data-ref-type="fig">1</a>.

<figure id="Fig1">
<p><img src="12955_2025_2421_Fig1_HTML.jpg" id="d33e529" /></p>
<figcaption>Flow diagram showing the selection process of primary studies</figcaption>
</figure>

### Basic characteristics of the included studies

The systematic review analyzed 187 studies involving 116,525 participants ranging from 10 to 19,784. The mean age of participants was 52.6 years (SD: 9.8), and males comprised 42.3% of the population. Most studies were conducted in Europe (56.1%), followed by Asia (19.3%) and North America (11.2%), with fewer studies conducted in South America (5.9%), Africa (2.7%), and Australia (2.7%). Only four studies involved more than one continent. The study designs were mainly cohort studies (58.3%, *n* = 109), followed by cross-sectional surveys (40.1%, *n* = 75) and case-control studies (1.6%, *n* = 3) (Table <a href="#MOESM1" data-ref-type="media">S2</a>).

### Health-related quality of life evaluation methods

The majority of the studies included (80.2%) used the EQ-5D-5 L version. The most frequent mode of administration was via face-to-face interviews (*n* = 44, 23.5%) followed by digital (*n* = 43, 23%). Approximately 68% of the studies reported EQ-5D index values, while 86.1% provided EQ-5D VAS scores. The UK (*n* = 20) and US (*n* = 12) value sets were the most applied across the studies, and 75 of the studies did not report which value set they had used. Additionally, EQ-5D profiles were presented in more than half of the studies (55.6%) (Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

HRQoL in patients with COVID-19 disease measured by the EQ-5D

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Author, publication year</th>
<th rowspan="2" style="text-align: left;">Version of EQ-5D</th>
<th colspan="3" style="text-align: left;">Utility score</th>
<th colspan="2" style="text-align: left;">VAS scores</th>
<th colspan="5" style="text-align: left;">Percent reporting “no problem” in 5 dimensions</th>
<th rowspan="2" style="text-align: left;">Administration</th>
</tr>
<tr>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">Value set</th>
<th style="text-align: left;">Mean</th>
<th style="text-align: left;">SD</th>
<th style="text-align: left;">MO</th>
<th style="text-align: left;">SC</th>
<th style="text-align: left;">UA</th>
<th style="text-align: left;">PD</th>
<th style="text-align: left;">AD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Arab-Zozani et al., 2020 [<span class="citation" data-cites="CR30">30</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.6125</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">Iranian</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">53.34</td>
<td style="text-align: left;">87.75</td>
<td style="text-align: left;">58.97</td>
<td style="text-align: left;">57.97</td>
<td style="text-align: left;">41.26</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Daher et al., 2020 [<span class="citation" data-cites="CR2">2</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">63*</td>
<td style="text-align: left;">53–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Betschart et al., 2021 [<span class="citation" data-cites="CR112">112</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">Self-administered and mail</td>
</tr>
<tr>
<td style="text-align: left;">Meys et al., 2020 [<span class="citation" data-cites="CR113">113</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">Dutch</td>
<td style="text-align: left;">50.71</td>
<td style="text-align: left;">18.87</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">85.7</td>
<td style="text-align: left;">6.2</td>
<td style="text-align: left;">2.9</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Fernandes et al., 2021 [<span class="citation" data-cites="CR114">114</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">60–90</td>
<td style="text-align: left;">86.7</td>
<td style="text-align: left;">89.6</td>
<td style="text-align: left;">53.1</td>
<td style="text-align: left;">68.7</td>
<td style="text-align: left;">62.5</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Halpin et al., 2021 [<span class="citation" data-cites="CR115">115</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.724</td>
<td style="text-align: left;">0.223</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">69.1</td>
<td style="text-align: left;">82.4</td>
<td style="text-align: left;">63.2</td>
<td style="text-align: left;">85.3</td>
<td style="text-align: left;">83.8</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Hodgson et al., 2021 [<span class="citation" data-cites="CR116">116</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8*</td>
<td style="text-align: left;">0.7–0.9</td>
<td style="text-align: left;">Australian</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">60–85</td>
<td style="text-align: left;">57.3</td>
<td style="text-align: left;">84.3</td>
<td style="text-align: left;">55.7</td>
<td style="text-align: left;">50.4</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Huang et al., 2021 [<span class="citation" data-cites="CR53">53</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">75–90</td>
<td style="text-align: left;">94</td>
<td style="text-align: left;">99</td>
<td style="text-align: left;">98</td>
<td style="text-align: left;">73</td>
<td style="text-align: left;">77</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Iqbal et al., 2021 [<span class="citation" data-cites="CR71">71</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70.76</td>
<td style="text-align: left;">22.42</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">69.6</td>
<td style="text-align: left;">27.2</td>
<td style="text-align: left;">25.9</td>
<td style="text-align: left;">39.9</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Johnsen et al., 2021 [<span class="citation" data-cites="CR117">117</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">55–81</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Kaso et al., 2021 [<span class="citation" data-cites="CR31">31</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.688</td>
<td style="text-align: left;">0.285</td>
<td style="text-align: left;">Zimbabwe</td>
<td style="text-align: left;">69</td>
<td style="text-align: left;">12.9</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Kohlbrenner et al., 2021 [<span class="citation" data-cites="CR76">76</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.96*</td>
<td style="text-align: left;">0.82, 1.00</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">74,94</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Kotwani et al., 2021 [<span class="citation" data-cites="CR118">118</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.755</td>
<td style="text-align: left;">0.18</td>
<td style="text-align: left;">Thailand</td>
<td style="text-align: left;">75.05</td>
<td style="text-align: left;">12.12</td>
<td style="text-align: left;">43.5</td>
<td style="text-align: left;">57.4</td>
<td style="text-align: left;">52.8</td>
<td style="text-align: left;">41.7</td>
<td style="text-align: left;">17.6</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Lerum et al., 2021 [<span class="citation" data-cites="CR119">119</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Malinowska et al., 2021 [<span class="citation" data-cites="CR32">32</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">64.83</td>
<td style="text-align: left;">18.6</td>
<td style="text-align: left;">76.1</td>
<td style="text-align: left;">89.5</td>
<td style="text-align: left;">73.1</td>
<td style="text-align: left;">73.1</td>
<td style="text-align: left;">88.1</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Menges et al., 2021 [<span class="citation" data-cites="CR120">120</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.89</td>
<td style="text-align: left;">0.16</td>
<td style="text-align: left;">Dutch</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">88.8</td>
<td style="text-align: left;">99.5</td>
<td style="text-align: left;">89.5</td>
<td style="text-align: left;">64.7</td>
<td style="text-align: left;">69.1</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Monti et al., 2021 [<span class="citation" data-cites="CR121">121</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">74</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">82</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">54</td>
<td style="text-align: left;">79</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Och et al., 2021 [<span class="citation" data-cites="CR122">122</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">64.4</td>
<td style="text-align: left;">16.2</td>
<td style="text-align: left;">38.4</td>
<td style="text-align: left;">68.5</td>
<td style="text-align: left;">50.7</td>
<td style="text-align: left;">71.2</td>
<td style="text-align: left;">72.6</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Ordinola Navarro et al., 2021 [<span class="citation" data-cites="CR101">101</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">85*</td>
<td style="text-align: left;">75–90</td>
<td style="text-align: left;">73</td>
<td style="text-align: left;">92</td>
<td style="text-align: left;">62</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Ozkeskin et al., 2021 [<span class="citation" data-cites="CR123">123</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">80.5</td>
<td style="text-align: left;">20.1</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Rousseau et al., 2021 [<span class="citation" data-cites="CR124">124</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">71*</td>
<td style="text-align: left;">61–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Shah AS et al. 2021, [<span class="citation" data-cites="CR125">125</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.9*</td>
<td style="text-align: left;">0.81–0.95</td>
<td style="text-align: left;">Canadian</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">75–90</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Shah et al., 2021 [<span class="citation" data-cites="CR54">54</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">55.83</td>
<td style="text-align: left;">22.94</td>
<td style="text-align: left;">43.8</td>
<td style="text-align: left;">77.6</td>
<td style="text-align: left;">20.5</td>
<td style="text-align: left;">18.9</td>
<td style="text-align: left;">31.3</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Tessitore et al., 2021 [<span class="citation" data-cites="CR126">126</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">78.4</td>
<td style="text-align: left;">16.1</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">98</td>
<td style="text-align: left;">79</td>
<td style="text-align: left;">58</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Todt et al., 2021 [<span class="citation" data-cites="CR55">55</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.80*</td>
<td style="text-align: left;">0.74-1.00</td>
<td style="text-align: left;">Brazilian</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">86</td>
<td style="text-align: left;">92.6</td>
<td style="text-align: left;">84.4</td>
<td style="text-align: left;">60.5</td>
<td style="text-align: left;">65.6</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Walle-Hansen et al., 2021 [<span class="citation" data-cites="CR33">33</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">65.8</td>
<td style="text-align: left;">19.1</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">83</td>
<td style="text-align: left;">89</td>
<td style="text-align: left;">67</td>
<td style="text-align: left;">74</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Akova et al., 2022 [<span class="citation" data-cites="CR127">127</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">83.9</td>
<td style="text-align: left;">16.1</td>
<td style="text-align: left;">73.5</td>
<td style="text-align: left;">94.7</td>
<td style="text-align: left;">82.1</td>
<td style="text-align: left;">60.9</td>
<td style="text-align: left;">61.6</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Attauabi et al., 2021 [<span class="citation" data-cites="CR128">128</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.18</td>
<td style="text-align: left;">Danish</td>
<td style="text-align: left;">77.1</td>
<td style="text-align: left;">18.8</td>
<td style="text-align: left;">75.4</td>
<td style="text-align: left;">89.4</td>
<td style="text-align: left;">64.9</td>
<td style="text-align: left;">54.4</td>
<td style="text-align: left;">51.8</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Azizi et al., 2022 [<span class="citation" data-cites="CR34">34</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">50.89</td>
<td style="text-align: left;">20.46</td>
<td style="text-align: left;">13.8</td>
<td style="text-align: left;">16.4</td>
<td style="text-align: left;">11.3</td>
<td style="text-align: left;">9.3</td>
<td style="text-align: left;">5.4</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Barani et al., 2022 [<span class="citation" data-cites="CR67">67</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.925</td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;">Thailand</td>
<td style="text-align: left;">90.68</td>
<td style="text-align: left;">11.81</td>
<td style="text-align: left;">94.1</td>
<td style="text-align: left;">97.8</td>
<td style="text-align: left;">91.7</td>
<td style="text-align: left;">84.4</td>
<td style="text-align: left;">87.6</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Barreto et al., 2022 [<span class="citation" data-cites="CR56">56</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">50–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Cuerda et al., 2022 [<span class="citation" data-cites="CR129">129</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">40*</td>
<td style="text-align: left;">25–50</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">36</td>
<td style="text-align: left;">66</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">d’Ettorre et al., 2022 [<span class="citation" data-cites="CR35">35</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">Italian</td>
<td style="text-align: left;">72.38</td>
<td style="text-align: left;">15.18</td>
<td style="text-align: left;">66.4</td>
<td style="text-align: left;">86.1</td>
<td style="text-align: left;">62.1</td>
<td style="text-align: left;">45.2</td>
<td style="text-align: left;">48.9</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Oliveira et al., 2022 [<span class="citation" data-cites="CR130">130</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–100</td>
<td style="text-align: left;">70.9</td>
<td style="text-align: left;">93.4</td>
<td style="text-align: left;">67.1</td>
<td style="text-align: left;">53.5</td>
<td style="text-align: left;">50.2</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Demoule et al., 2022 [<span class="citation" data-cites="CR66">66</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.91*</td>
<td style="text-align: left;">0.52-1.00</td>
<td style="text-align: left;">French</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">60–85</td>
<td style="text-align: left;">71</td>
<td style="text-align: left;">79</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">66</td>
<td style="text-align: left;">53</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Farhanah et al., 2022 [<span class="citation" data-cites="CR131">131</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;">Indonesian</td>
<td style="text-align: left;">82.98</td>
<td style="text-align: left;">11.56</td>
<td style="text-align: left;">89.4</td>
<td style="text-align: left;">91.3</td>
<td style="text-align: left;">68.3</td>
<td style="text-align: left;">82.7</td>
<td style="text-align: left;">72.1</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Fontes et al., 2022 [<span class="citation" data-cites="CR132">132</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">Portuguese</td>
<td style="text-align: left;">65</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">38.4</td>
<td style="text-align: left;">63.7</td>
<td style="text-align: left;">22.2</td>
<td style="text-align: left;">43.4</td>
<td style="text-align: left;">35.4</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Haberland et al., 2022 [<span class="citation" data-cites="CR133">133</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">83.6</td>
<td style="text-align: left;">15.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Han et al., 2022 [<span class="citation" data-cites="CR134">134</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;">0.16</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">18</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Hegde et al., 2022 [<span class="citation" data-cites="CR36">36</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.95</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">95.1</td>
<td style="text-align: left;">98.4</td>
<td style="text-align: left;">96.7</td>
<td style="text-align: left;">95.9</td>
<td style="text-align: left;">99.2</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Heubner et al., 2022 [<span class="citation" data-cites="CR135">135</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">60*</td>
<td style="text-align: left;">45–75</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Huynh et al., 2022 [<span class="citation" data-cites="CR37">37</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">Vietnam</td>
<td style="text-align: left;">78.6</td>
<td style="text-align: left;">19.9</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">93.5</td>
<td style="text-align: left;">83.4</td>
<td style="text-align: left;">54.8</td>
<td style="text-align: left;">53.5</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Kalyani et al. 2022 [<span class="citation" data-cites="CR136">136</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">72.5</td>
<td style="text-align: left;">15.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Kaso et al., 2022 [<span class="citation" data-cites="CR38">38</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.94*</td>
<td style="text-align: left;">0.78–0.97</td>
<td style="text-align: left;">Ethiopian</td>
<td style="text-align: left;">87*</td>
<td style="text-align: left;">70, 91</td>
<td style="text-align: left;">59.6</td>
<td style="text-align: left;">59.4</td>
<td style="text-align: left;">50.9</td>
<td style="text-align: left;">40.4</td>
<td style="text-align: left;">45.4</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Koullias et al., 2022 [<span class="citation" data-cites="CR39">39</span>]</td>
<td style="text-align: left;">Equation 5D5L</td>
<td style="text-align: left;">0.788</td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">73.78</td>
<td style="text-align: left;">17.65</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Lim et al., 2022 [<span class="citation" data-cites="CR88">88</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.881</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">Canadian</td>
<td style="text-align: left;">78.8</td>
<td style="text-align: left;">18.1</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">96</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">64</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Luong et al., 2022 [<span class="citation" data-cites="CR137">137</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.13</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Martins et al., 2022 [<span class="citation" data-cites="CR138">138</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Portuguese</td>
<td style="text-align: left;">75*</td>
<td style="text-align: left;">40–100</td>
<td style="text-align: left;">37</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">34</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Moens et al., 2022 [<span class="citation" data-cites="CR139">139</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">Belgian</td>
<td style="text-align: left;">56.6</td>
<td style="text-align: left;">18.2</td>
<td style="text-align: left;">57.04</td>
<td style="text-align: left;">86.84</td>
<td style="text-align: left;">17.55</td>
<td style="text-align: left;">10.42</td>
<td style="text-align: left;">57.4</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Morrow et al., 2022 [<span class="citation" data-cites="CR140">140</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">43.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Nakshbandi et al., 2022 [<span class="citation" data-cites="CR141">141</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">0.13</td>
<td style="text-align: left;">Dutch</td>
<td style="text-align: left;">79.8</td>
<td style="text-align: left;">15.7</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Ojeda et al., 2022 [<span class="citation" data-cites="CR98">98</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8*</td>
<td style="text-align: left;">0.57–0.87</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">60–80</td>
<td style="text-align: left;">30.8</td>
<td style="text-align: left;">67.7</td>
<td style="text-align: left;">53.8</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">58.5</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Pacho-Hernández et al., 2022 [<span class="citation" data-cites="CR99">99</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Pan et al., 2022 [<span class="citation" data-cites="CR142">142</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">China</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Said et al., 2022 [<span class="citation" data-cites="CR57">57</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">73</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Schallner et al., 2022 [<span class="citation" data-cites="CR143">143</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">0.4</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">30</td>
<td style="text-align: left;">35.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Soh and Cho, 2022 [<span class="citation" data-cites="CR58">58</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.09</td>
<td style="text-align: left;">Korean</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">93.2</td>
<td style="text-align: left;">98.6</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">76.2</td>
<td style="text-align: left;">74.1</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Tabacof et al., 2022 [<span class="citation" data-cites="CR144">144</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">64*</td>
<td style="text-align: left;">6–99</td>
<td style="text-align: left;">44</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">72</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Tak, 2023 [<span class="citation" data-cites="CR89">89</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">41.6</td>
<td style="text-align: left;">21.1</td>
<td style="text-align: left;">37.4</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">12.2</td>
<td style="text-align: left;">28.1</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Tarazona et al., 2022 [<span class="citation" data-cites="CR83">83</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.87</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">French</td>
<td style="text-align: left;">78</td>
<td style="text-align: left;">17.6</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Tsuzuki et al., 2022 [<span class="citation" data-cites="CR90">90</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.17</td>
<td style="text-align: left;">Japanese</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Umbrello et al., 2022 [<span class="citation" data-cites="CR80">80</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.798</td>
<td style="text-align: left;">0.288</td>
<td style="text-align: left;">Italian</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">60–89</td>
<td style="text-align: left;">49</td>
<td style="text-align: left;">77</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">48</td>
<td style="text-align: left;">67</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Vejen et al., 2022 [<span class="citation" data-cites="CR145">145</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">75*</td>
<td style="text-align: left;">50–90</td>
<td style="text-align: left;">49</td>
<td style="text-align: left;">77</td>
<td style="text-align: left;">46</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Weihe et al., 2022 [<span class="citation" data-cites="CR146">146</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">51–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Wimmer et al., 2022 [<span class="citation" data-cites="CR147">147</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.749</td>
<td style="text-align: left;">0.176</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">67.4</td>
<td style="text-align: left;">16.6</td>
<td style="text-align: left;">23.7</td>
<td style="text-align: left;">45.8</td>
<td style="text-align: left;">45.8</td>
<td style="text-align: left;">23.7</td>
<td style="text-align: left;">74.6</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Wu D, et al. 2022 [<span class="citation" data-cites="CR148">148</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.88</td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;">Chinese</td>
<td style="text-align: left;">80.9</td>
<td style="text-align: left;">14.2</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Zhang et al., 2022 [<span class="citation" data-cites="CR40">40</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">Chinese</td>
<td style="text-align: left;">81.89</td>
<td style="text-align: left;">14.76</td>
<td style="text-align: left;">91.37</td>
<td style="text-align: left;">98.04</td>
<td style="text-align: left;">93.33</td>
<td style="text-align: left;">79.61</td>
<td style="text-align: left;">68.24</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Fietsam et al., 2023 [<span class="citation" data-cites="CR149">149</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">68.9</td>
<td style="text-align: left;">18.4</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Hoque et al., 2023 [<span class="citation" data-cites="CR41">41</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">70.26</td>
<td style="text-align: left;">11.13</td>
<td style="text-align: left;">54.23</td>
<td style="text-align: left;">49.01</td>
<td style="text-align: left;">47.21</td>
<td style="text-align: left;">44.86</td>
<td style="text-align: left;">37.84</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Huarcaya-Victoria et al., 2022 [<span class="citation" data-cites="CR6">6</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">71.4</td>
<td style="text-align: left;">67.2</td>
<td style="text-align: left;">85.7</td>
<td style="text-align: left;">40.3</td>
<td style="text-align: left;">58</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Iribarren-Diarasarri et al., 2022 [<span class="citation" data-cites="CR79">79</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.709</td>
<td style="text-align: left;">0.247</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">60.53</td>
<td style="text-align: left;">17.6</td>
<td style="text-align: left;">53.9</td>
<td style="text-align: left;">79.7</td>
<td style="text-align: left;">55.3</td>
<td style="text-align: left;">69.3</td>
<td style="text-align: left;">72.7</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Román-Montes et al., 2023 [<span class="citation" data-cites="CR72">72</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">69</td>
<td style="text-align: left;">86</td>
<td style="text-align: left;">66</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Rosa et al., 2023 [<span class="citation" data-cites="CR73">73</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.24</td>
<td style="text-align: left;">Brazilian</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Rousseau et al., 2023 [<span class="citation" data-cites="CR150">150</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">Belgian</td>
<td style="text-align: left;">71.3</td>
<td style="text-align: left;">18.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Sánchez-García et al., 2023 [<span class="citation" data-cites="CR151">151</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">60.6</td>
<td style="text-align: left;">20.2</td>
<td style="text-align: left;">62.5</td>
<td style="text-align: left;">67.9</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">44.6</td>
<td style="text-align: left;">64.3</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Shah et al., 2023 [<span class="citation" data-cites="CR42">42</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">91.69</td>
<td style="text-align: left;">12.34</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">18.6</td>
<td style="text-align: left;">17</td>
<td style="text-align: left;">20.4</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Wong et al.,0.2023 [<span class="citation" data-cites="CR94">94</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">60*</td>
<td style="text-align: left;">50–75</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Taboada et al., 2020 [<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.7054</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">66.36</td>
<td style="text-align: left;">18.26</td>
<td style="text-align: left;">44</td>
<td style="text-align: left;">87</td>
<td style="text-align: left;">63</td>
<td style="text-align: left;">52</td>
<td style="text-align: left;">54</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Ferrarello et al., 2023 [<span class="citation" data-cites="CR91">91</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.87</td>
<td style="text-align: left;">0.16</td>
<td style="text-align: left;">Italian</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">64</td>
<td style="text-align: left;">86</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">64</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Slotegraaf et al., 2023 [<span class="citation" data-cites="CR59">59</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">67.9</td>
<td style="text-align: left;">19.1</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Zupanc et al., 2023 [<span class="citation" data-cites="CR152">152</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">Slovenian</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">71</td>
<td style="text-align: left;">39</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">88</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Giurgi-Oncu et al., 2021 [<span class="citation" data-cites="CR74">74</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">64</td>
<td style="text-align: left;">14.6</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Cavalleri et al., 2022 [<span class="citation" data-cites="CR153">153</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Belgian</td>
<td style="text-align: left;">72.5*</td>
<td style="text-align: left;">60–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Sandmann et al., 2021 [<span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.18</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">80.2</td>
<td style="text-align: left;">18.4</td>
<td style="text-align: left;">85.8</td>
<td style="text-align: left;">94.8</td>
<td style="text-align: left;">83.9</td>
<td style="text-align: left;">61</td>
<td style="text-align: left;">59.9</td>
<td style="text-align: left;">Digital or mail</td>
</tr>
<tr>
<td style="text-align: left;">Carenzo et al., 2021 [<span class="citation" data-cites="CR154">154</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">85*</td>
<td style="text-align: left;">77.5–90</td>
<td style="text-align: left;">81</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Morelli et al., 2022 [<span class="citation" data-cites="CR155">155</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70.4</td>
<td style="text-align: left;">18.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Evans et al., 2022 [<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0·75</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">67·0</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">46</td>
<td style="text-align: left;">74</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">44</td>
<td style="text-align: left;">51</td>
<td style="text-align: left;">Self-administered</td>
</tr>
<tr>
<td style="text-align: left;">Brus et al. 2023 [<span class="citation" data-cites="CR52">52</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.28</td>
<td style="text-align: left;">Dutch</td>
<td style="text-align: left;">47.2</td>
<td style="text-align: left;">18.7</td>
<td style="text-align: left;">39.8</td>
<td style="text-align: left;">82.3</td>
<td style="text-align: left;">29</td>
<td style="text-align: left;">29.4</td>
<td style="text-align: left;">52.8</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Sawano et al. 2025 [<span class="citation" data-cites="CR156">156</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">49*</td>
<td style="text-align: left;">32–61</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Scott et al. 2023 [<span class="citation" data-cites="CR157">157</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">65.7</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">65</td>
<td style="text-align: left;">88</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Khoja et al. 2024 [<span class="citation" data-cites="CR158">158</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">44</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">93.3</td>
<td style="text-align: left;">6.7</td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;">6.7</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Cataldo et al. 2024 [<span class="citation" data-cites="CR159">159</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">65.4</td>
<td style="text-align: left;">17.4</td>
<td style="text-align: left;">66.1</td>
<td style="text-align: left;">89.9</td>
<td style="text-align: left;">51.4</td>
<td style="text-align: left;">24.8</td>
<td style="text-align: left;">12.8</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Wemhöner et al. 2025 [<span class="citation" data-cites="CR160">160</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">60.4</td>
<td style="text-align: left;">19.9</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Engel et al. 2025 [<span class="citation" data-cites="CR161">161</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">64*</td>
<td style="text-align: left;">50–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Malesevic et al. 2023 [<span class="citation" data-cites="CR162">162</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">20.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Ding et al. 2024 [<span class="citation" data-cites="CR163">163</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.14</td>
<td style="text-align: left;">Chinese</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Crescioli et al. 2024 [<span class="citation" data-cites="CR164">164</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.61*</td>
<td style="text-align: left;">0-0.91</td>
<td style="text-align: left;">Danish</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">0–80</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Egger et al. 2024 [<span class="citation" data-cites="CR85">85</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.63</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">23.9</td>
<td style="text-align: left;">32.3</td>
<td style="text-align: left;">59.7</td>
<td style="text-align: left;">22.6</td>
<td style="text-align: left;">16.1</td>
<td style="text-align: left;">45.2</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Neelima et al. 2023 [<span class="citation" data-cites="CR81">81</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.51</td>
<td style="text-align: left;">0.43</td>
<td style="text-align: left;">Indian</td>
<td style="text-align: left;">68.97</td>
<td style="text-align: left;">22.27</td>
<td style="text-align: left;">23.4</td>
<td style="text-align: left;">32.7</td>
<td style="text-align: left;">43</td>
<td style="text-align: left;">30.8</td>
<td style="text-align: left;">26.2</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Leavy et al. 2024 [<span class="citation" data-cites="CR165">165</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Berentschot et al. 2024 [<span class="citation" data-cites="CR60">60</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">73.4</td>
<td style="text-align: left;">18.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Zhao X, et al. 2024 [<span class="citation" data-cites="CR166">166</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">78.76</td>
<td style="text-align: left;">9.18</td>
<td style="text-align: left;">86.1</td>
<td style="text-align: left;">93.6</td>
<td style="text-align: left;">90.2</td>
<td style="text-align: left;">95.4</td>
<td style="text-align: left;">90.2</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Colleran R et al. 2023 [<span class="citation" data-cites="CR167">167</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">14.8</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">98</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Visser et al. 2024 [<span class="citation" data-cites="CR77">77</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">Dutch</td>
<td style="text-align: left;">65.8</td>
<td style="text-align: left;">18.6</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Neumann et al. 2025 [<span class="citation" data-cites="CR46">46</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.91*</td>
<td style="text-align: left;">0.89-1.00</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Appel et al. 2024 [<span class="citation" data-cites="CR168">168</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">73.9</td>
<td style="text-align: left;">20.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Deesomchok et al. 2023 [<span class="citation" data-cites="CR169">169</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.18</td>
<td style="text-align: left;">Thailand</td>
<td style="text-align: left;">81.8</td>
<td style="text-align: left;">11.6</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Kato et al. 2025 [<span class="citation" data-cites="CR170">170</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Japanese</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">65, 90</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Rego de Figueiredo et al. 2023 [<span class="citation" data-cites="CR47">47</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.73</td>
<td style="text-align: left;">0.26</td>
<td style="text-align: left;">Portuguese</td>
<td style="text-align: left;">64</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Gorsler et al. 2024 [<span class="citation" data-cites="CR171">171</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">67.4</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Naik et al. 2025 [<span class="citation" data-cites="CR87">87</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;">Canadian</td>
<td style="text-align: left;">68.8</td>
<td style="text-align: left;">17.2</td>
<td style="text-align: left;">85.3</td>
<td style="text-align: left;">93.7</td>
<td style="text-align: left;">75.5</td>
<td style="text-align: left;">63.5</td>
<td style="text-align: left;">50.9</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Sun X et al. 2024 [<span class="citation" data-cites="CR100">100</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.17</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Hatakeyama et al. 2025 [<span class="citation" data-cites="CR48">48</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">0.336</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Soare et al. 2024 [<span class="citation" data-cites="CR75">75</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">18.7</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Rover et al. 2024 [<span class="citation" data-cites="CR172">172</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;">Brazilian</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Janols et al. 2024 [<span class="citation" data-cites="CR173">173</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.77</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">Swedish</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Guaraldi et al. 2023 [<span class="citation" data-cites="CR174">174</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">67</td>
<td style="text-align: left;">16</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Kwon et al. 2024 [<span class="citation" data-cites="CR175">175</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.501</td>
<td style="text-align: left;">0.287</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">51.9</td>
<td style="text-align: left;">21.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Smith et al. 2023 [<span class="citation" data-cites="CR176">176</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.13</td>
<td style="text-align: left;">Belgian</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Tak C 2023 [<span class="citation" data-cites="CR177">177</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.51*</td>
<td style="text-align: left;">0.59, 039</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">41.6*</td>
<td style="text-align: left;">55,31</td>
<td style="text-align: left;">37.4</td>
<td style="text-align: left;">59</td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">12.2</td>
<td style="text-align: left;">28.1</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Qorolli et al. 2023 [<span class="citation" data-cites="CR178">178</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">66.8</td>
<td style="text-align: left;">16.3</td>
<td style="text-align: left;">35.9</td>
<td style="text-align: left;">79.5</td>
<td style="text-align: left;">25.7</td>
<td style="text-align: left;">30.8</td>
<td style="text-align: left;">76.9</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Tiels et al. 2025 [<span class="citation" data-cites="CR102">102</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.67</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">Dutch</td>
<td style="text-align: left;">60.9</td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Hansen KS et al. 2023 [<span class="citation" data-cites="CR179">179</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.69*</td>
<td style="text-align: left;">0.69–0.70</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Mastrorosa et al. 2023 [<span class="citation" data-cites="CR61">61</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Italian</td>
<td style="text-align: left;">70.1</td>
<td style="text-align: left;">18.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Elneima O, et al. 2024 [<span class="citation" data-cites="CR180">180</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.64</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">67.3</td>
<td style="text-align: left;">21.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Sun et al. 2023 [<span class="citation" data-cites="CR181">181</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.808</td>
<td style="text-align: left;">0.204</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">73.3</td>
<td style="text-align: left;">16.9</td>
<td style="text-align: left;">17.2</td>
<td style="text-align: left;">11.4</td>
<td style="text-align: left;">16.6</td>
<td style="text-align: left;">27.6</td>
<td style="text-align: left;">41</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Fernández-de-las-Peñas et al. 2023 [<span class="citation" data-cites="CR182">182</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">Spain</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Mercier et al. 2023 [<span class="citation" data-cites="CR183">183</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.863</td>
<td style="text-align: left;">0.116</td>
<td style="text-align: left;">Canada</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Tsuruoka et al. 2025 [<span class="citation" data-cites="CR184">184</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Vietnam</td>
<td style="text-align: left;">90*</td>
<td style="text-align: left;">80–90</td>
<td style="text-align: left;">94.1</td>
<td style="text-align: left;">95.7</td>
<td style="text-align: left;">94.1</td>
<td style="text-align: left;">82.3</td>
<td style="text-align: left;">77.4</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">van Tol et al. 2024 [<span class="citation" data-cites="CR185">185</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.32</td>
<td style="text-align: left;">Various</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Carlile et al. 2024 [<span class="citation" data-cites="CR68">68</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.31</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Carrera et al. 2025 [<span class="citation" data-cites="CR186">186</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.73*</td>
<td style="text-align: left;">0.59-1</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Elumalai et al. 2023 [<span class="citation" data-cites="CR82">82</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.98</td>
<td style="text-align: left;">0.05</td>
<td style="text-align: left;">Indian</td>
<td style="text-align: left;">92.14</td>
<td style="text-align: left;">8.39</td>
<td style="text-align: left;">88.8</td>
<td style="text-align: left;">98.7</td>
<td style="text-align: left;">89.8</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">89.7</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Di Fusco et al. 2023 [<span class="citation" data-cites="CR187">187</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.727</td>
<td style="text-align: left;">0.242</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">74.5</td>
<td style="text-align: left;">17.2</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Kuodi et al. 2023 [<span class="citation" data-cites="CR84">84</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">US</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">72</td>
<td style="text-align: left;">88</td>
<td style="text-align: left;">68</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Godfrey et al. 2025 [<span class="citation" data-cites="CR188">188</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Lomholt-Welch et al. 2023 [<span class="citation" data-cites="CR189">189</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">61.54</td>
<td style="text-align: left;">21.95</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Atchison et al. 2023 [<span class="citation" data-cites="CR190">190</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">64.7</td>
<td style="text-align: left;">21.1</td>
<td style="text-align: left;">53.3</td>
<td style="text-align: left;">79.4</td>
<td style="text-align: left;">36.6</td>
<td style="text-align: left;">24.3</td>
<td style="text-align: left;">34.6</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Walker et al. 2023 [<span class="citation" data-cites="CR95">95</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.54</td>
<td style="text-align: left;">0.27</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">26.9</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">36.3</td>
<td style="text-align: left;">3.8</td>
<td style="text-align: left;">5.1</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Schröder et al. 2024 [<span class="citation" data-cites="CR62">62</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">Germany</td>
<td style="text-align: left;">57.6</td>
<td style="text-align: left;">22.2</td>
<td style="text-align: left;">66.2</td>
<td style="text-align: left;">92.6</td>
<td style="text-align: left;">30.5</td>
<td style="text-align: left;">19.1</td>
<td style="text-align: left;">39.8</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Duwel et al. 2023 [<span class="citation" data-cites="CR191">191</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">79.6</td>
<td style="text-align: left;">14.5</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Pietruszka-Wałęka et al. 2024 [<span class="citation" data-cites="CR192">192</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Polish</td>
<td style="text-align: left;">76*</td>
<td style="text-align: left;">69–78</td>
<td style="text-align: left;">41.18</td>
<td style="text-align: left;">94.12</td>
<td style="text-align: left;">70.59</td>
<td style="text-align: left;">35.29</td>
<td style="text-align: left;">41.18</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Samuelsson et al. 2025 [<span class="citation" data-cites="CR193">193</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.83</td>
<td style="text-align: left;">0.13</td>
<td style="text-align: left;">Swedish</td>
<td style="text-align: left;">67.6</td>
<td style="text-align: left;">19.2</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">65</td>
<td style="text-align: left;">31</td>
<td style="text-align: left;">49</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Seeley et al. 2025 [<span class="citation" data-cites="CR194">194</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.67*</td>
<td style="text-align: left;">0.49–0.80</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">36.4</td>
<td style="text-align: left;">63.6</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">12.1</td>
<td style="text-align: left;">24.2</td>
<td style="text-align: left;">Face-to-face interview and Digital</td>
</tr>
<tr>
<td style="text-align: left;">Agergaard et al. 2023 [<span class="citation" data-cites="CR195">195</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.76*</td>
<td style="text-align: left;">0.62–0.85</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview and Digital</td>
</tr>
<tr>
<td style="text-align: left;">Amedewonu et al. 2024 [<span class="citation" data-cites="CR92">92</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.815</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">Zimbabwe</td>
<td style="text-align: left;">75.6</td>
<td style="text-align: left;">22</td>
<td style="text-align: left;">74</td>
<td style="text-align: left;">84</td>
<td style="text-align: left;">73.3</td>
<td style="text-align: left;">67.3</td>
<td style="text-align: left;">66.7</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">D’Souza et al. 2024 [<span class="citation" data-cites="CR196">196</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8*</td>
<td style="text-align: left;">0.71, 0.86</td>
<td style="text-align: left;">Australian</td>
<td style="text-align: left;">66*</td>
<td style="text-align: left;">45–80</td>
<td style="text-align: left;">51</td>
<td style="text-align: left;">82</td>
<td style="text-align: left;">23</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Carenzo et al. 2024 [<span class="citation" data-cites="CR197">197</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Italian</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">69.2</td>
<td style="text-align: left;">88.5</td>
<td style="text-align: left;">69.2</td>
<td style="text-align: left;">41.7</td>
<td style="text-align: left;">56.3</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">McCarthy et al. 2024 [<span class="citation" data-cites="CR198">198</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.653</td>
<td style="text-align: left;">0.3</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Malesevic et al. 2023 [<span class="citation" data-cites="CR199">199</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.818</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">66</td>
<td style="text-align: left;">20.3</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">87.9</td>
<td style="text-align: left;">69.7</td>
<td style="text-align: left;">46.9</td>
<td style="text-align: left;">65.2</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Dennis et al. 2023 [<span class="citation" data-cites="CR200">200</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.71*</td>
<td style="text-align: left;">0.56–0.81</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">60–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Cannata et al. 2023 [<span class="citation" data-cites="CR201">201</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">90.9</td>
<td style="text-align: left;">97.3</td>
<td style="text-align: left;">86.4</td>
<td style="text-align: left;">90</td>
<td style="text-align: left;">69.1</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Wang J et al. 2024 [<span class="citation" data-cites="CR202">202</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.64*</td>
<td style="text-align: left;">0.59, 0.69</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Wangnamthip S et al. 2024 [<span class="citation" data-cites="CR203">203</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.9</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">Thailand</td>
<td style="text-align: left;">87.6</td>
<td style="text-align: left;">12.8</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Caamano et al. 2024 [<span class="citation" data-cites="CR63">63</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.91*</td>
<td style="text-align: left;">0.76-1</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">60–90</td>
<td style="text-align: left;">73.3</td>
<td style="text-align: left;">84.2</td>
<td style="text-align: left;">91.1</td>
<td style="text-align: left;">58.4</td>
<td style="text-align: left;">53.5</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Sinaga et al. 2023 [<span class="citation" data-cites="CR204">204</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Indonesian</td>
<td style="text-align: left;">87.6</td>
<td style="text-align: left;">8.1</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">96</td>
<td style="text-align: left;">96</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Tabacof et al. 2023 [<span class="citation" data-cites="CR205">205</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">59*</td>
<td style="text-align: left;">54.9–61.4</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Thanh HN et al. 2024 [<span class="citation" data-cites="CR206">206</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">Vietnamese</td>
<td style="text-align: left;">84.2</td>
<td style="text-align: left;">13.11</td>
<td style="text-align: left;">94.4</td>
<td style="text-align: left;">98.7</td>
<td style="text-align: left;">94.7</td>
<td style="text-align: left;">74.6</td>
<td style="text-align: left;">67.3</td>
<td style="text-align: left;">Digital or Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Cijs et al. 2023 [<span class="citation" data-cites="CR207">207</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">0.03</td>
<td style="text-align: left;">German</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face or Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Domazet Bugarin et al. 2023 [<span class="citation" data-cites="CR208">208</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">40–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Cázares-Lara et al. 2024 [<span class="citation" data-cites="CR209">209</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.87*</td>
<td style="text-align: left;">0.80–0.94</td>
<td style="text-align: left;">Mexican</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–85</td>
<td style="text-align: left;">81</td>
<td style="text-align: left;">94.6</td>
<td style="text-align: left;">87.8</td>
<td style="text-align: left;">68.2</td>
<td style="text-align: left;">55.4</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Pavithra et al. 2023 [<span class="citation" data-cites="CR210">210</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70.7</td>
<td style="text-align: left;">17.2</td>
<td style="text-align: left;">57</td>
<td style="text-align: left;">70</td>
<td style="text-align: left;">58</td>
<td style="text-align: left;">35</td>
<td style="text-align: left;">58</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Bolgeo et al. 2024 [<span class="citation" data-cites="CR49">49</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">0.15</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">66.99</td>
<td style="text-align: left;">21.59</td>
<td style="text-align: left;">55.8</td>
<td style="text-align: left;">59.8</td>
<td style="text-align: left;">50.3</td>
<td style="text-align: left;">49.2</td>
<td style="text-align: left;">57.3</td>
<td style="text-align: left;">Digital or Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Salem et al. 2023 [<span class="citation" data-cites="CR50">50</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.955</td>
<td style="text-align: left;">0.105</td>
<td style="text-align: left;">Malaysia</td>
<td style="text-align: left;">93</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Honda et al. 2025 [<span class="citation" data-cites="CR211">211</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.9*</td>
<td style="text-align: left;">0.8-1.0</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">87.7</td>
<td style="text-align: left;">93.3</td>
<td style="text-align: left;">89.7</td>
<td style="text-align: left;">63.2</td>
<td style="text-align: left;">72.7</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Gharibzadeh et al. 2024 [<span class="citation" data-cites="CR212">212</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">70*</td>
<td style="text-align: left;">50–80</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Berentschot et al. 2024 [<span class="citation" data-cites="CR213">213</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail</td>
</tr>
<tr>
<td style="text-align: left;">Macedo Junior et al. 2024 [<span class="citation" data-cites="CR96">96</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.79*</td>
<td style="text-align: left;">0.74–0.85</td>
<td style="text-align: left;">Brazilian</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">99.1</td>
<td style="text-align: left;">100</td>
<td style="text-align: left;">89.9</td>
<td style="text-align: left;">55</td>
<td style="text-align: left;">47.7</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Álvarez-Hernández et al. 2023 [<span class="citation" data-cites="CR214">214</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">0.25</td>
<td style="text-align: left;">Spanish</td>
<td style="text-align: left;">72.7</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">71.3</td>
<td style="text-align: left;">87.8</td>
<td style="text-align: left;">65.4</td>
<td style="text-align: left;">47.3</td>
<td style="text-align: left;">57.4</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Prata TA, et al. 2024 [<span class="citation" data-cites="CR97">97</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">60.2</td>
<td style="text-align: left;">83.3</td>
<td style="text-align: left;">71</td>
<td style="text-align: left;">41.9</td>
<td style="text-align: left;">50.5</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Alanazi MQ et al. 2023 [<span class="citation" data-cites="CR215">215</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.92</td>
<td style="text-align: left;">0.13</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">86.96</td>
<td style="text-align: left;">15.31</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview and Digital</td>
</tr>
<tr>
<td style="text-align: left;">Moisoglou et al. 2024 [<span class="citation" data-cites="CR70">70</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">Greek</td>
<td style="text-align: left;">54.1</td>
<td style="text-align: left;">21.71</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Ramos et al. 2024 [<span class="citation" data-cites="CR216">216</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.8*</td>
<td style="text-align: left;">0.69-1</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">70–90</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Gursoy et al. 2023 [<span class="citation" data-cites="CR217">217</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">75.42</td>
<td style="text-align: left;">17.39</td>
<td style="text-align: left;">43.4</td>
<td style="text-align: left;">46.9</td>
<td style="text-align: left;">45.5</td>
<td style="text-align: left;">48.3</td>
<td style="text-align: left;">49</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Wang R et al. 2023 [<span class="citation" data-cites="CR218">218</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.52</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">China</td>
<td style="text-align: left;">48.52</td>
<td style="text-align: left;">24.29</td>
<td style="text-align: left;">31.2</td>
<td style="text-align: left;">50.4</td>
<td style="text-align: left;">22.4</td>
<td style="text-align: left;">9.3</td>
<td style="text-align: left;">35.3</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Demirhan et al. 2023 [<span class="citation" data-cites="CR219">219</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.86</td>
<td style="text-align: left;">0.193</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">78.84</td>
<td style="text-align: left;">16.15</td>
<td style="text-align: left;">79.3</td>
<td style="text-align: left;">89.8</td>
<td style="text-align: left;">87.2</td>
<td style="text-align: left;">74.5</td>
<td style="text-align: left;">84.2</td>
<td style="text-align: left;">Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Firouzabadi et al. 2024 [<span class="citation" data-cites="CR51">51</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">76.5</td>
<td style="text-align: left;">26.6</td>
<td style="text-align: left;">61.8</td>
<td style="text-align: left;">95.4</td>
<td style="text-align: left;">86.1</td>
<td style="text-align: left;">86.1</td>
<td style="text-align: left;">55.7</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Sun C et al. 2024 [<span class="citation" data-cites="CR69">69</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.94</td>
<td style="text-align: left;">0.07</td>
<td style="text-align: left;">Chinese</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">94.07</td>
<td style="text-align: left;">97.78</td>
<td style="text-align: left;">94.81</td>
<td style="text-align: left;">81.48</td>
<td style="text-align: left;">70.37</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Galanis et al. 2023 [<span class="citation" data-cites="CR64">64</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.37</td>
<td style="text-align: left;">Greek</td>
<td style="text-align: left;">54.1</td>
<td style="text-align: left;">21.71</td>
<td style="text-align: left;">20.5</td>
<td style="text-align: left;">62.3</td>
<td style="text-align: left;">19.7</td>
<td style="text-align: left;">20.5</td>
<td style="text-align: left;">13.9</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Dodd et al. 2024 [<span class="citation" data-cites="CR78">78</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">82.87</td>
<td style="text-align: left;">12.09</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Rahimi et al. 2024 [<span class="citation" data-cites="CR220">220</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">60–85</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Holland et al. 2024 [<span class="citation" data-cites="CR221">221</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">62*</td>
<td style="text-align: left;">3–100</td>
<td style="text-align: left;">76</td>
<td style="text-align: left;">94</td>
<td style="text-align: left;">63</td>
<td style="text-align: left;">63</td>
<td style="text-align: left;">29</td>
<td style="text-align: left;">Digital or Telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Zalaquett et al. 2024 [<span class="citation" data-cites="CR93">93</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">85*</td>
<td style="text-align: left;">75–90</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">96</td>
<td style="text-align: left;">79</td>
<td style="text-align: left;">38</td>
<td style="text-align: left;">40</td>
<td style="text-align: left;">Digital</td>
</tr>
<tr>
<td style="text-align: left;">Bodey et al. 2024 [<span class="citation" data-cites="CR222">222</span>]</td>
<td style="text-align: left;">EQ-5D-5 L</td>
<td style="text-align: left;">0.53</td>
<td style="text-align: left;">0.29</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">57.67</td>
<td style="text-align: left;">20.19</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Mail or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Kho et al. 2023 [<span class="citation" data-cites="CR223">223</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">80*</td>
<td style="text-align: left;">75–90</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face interview</td>
</tr>
<tr>
<td style="text-align: left;">Yalçın-Çolak et al. 2023 [<span class="citation" data-cites="CR224">224</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;">0.19</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">69.56</td>
<td style="text-align: left;">19.04</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Face-to-face or telephone interview</td>
</tr>
<tr>
<td style="text-align: left;">Kılınçarslan et al. 2023 [<span class="citation" data-cites="CR65">65</span>]</td>
<td style="text-align: left;">EQ-5D-3 L</td>
<td style="text-align: left;">1*</td>
<td style="text-align: left;">0.79-1.00</td>
<td style="text-align: left;">UK</td>
<td style="text-align: left;">100*</td>
<td style="text-align: left;">75–100</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">Digital</td>
</tr>
</tbody>
</table>

“–” represents the value is not reported by the article. \*Represents the utility or VAS score was reported in the median (IQR or range)

*AD* Anxiety/Depression, *EQ-5D* EuroQol 5 Dimensions, *F* Face-to-face interview, *HRQoL* Health-Related Quality of Life, *IQR* interquartile range, *MO* mobility, *PD* Pain/Discomfort, *SC* self-care, *SD* standard deviation, *UA* usual activities, *VAS* Visual Analog Scale

</div>

### EQ-5D index scores, EQ-VAS scores, and EQ-5D profiles

Of the 187 studies included, 127 (68%) reported EQ-5D utility scores for COVID-19 patients, with a pooled mean EQ-5D utility score of 0.76 (95% CI 0.74–0.79) (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). Additionally, 161 studies reported EQ-VAS scores, with a pooled mean of 70.76 (95% CI 68.48–73.04) (Table <a href="#Tab2" data-ref-type="table">2</a>). Despite these pooled estimates, considerable heterogeneity was observed across studies, with an I<sup>2</sup> value of 99.9% for EQ-5D index scores and 99.7% for EQ-5D VAS scores (Figure <a href="#MOESM1" data-ref-type="media">S1</a>).

<figure id="Fig2">
<p><img src="12955_2025_2421_Fig2_HTML.jpg" id="d33e6685" /></p>
<figcaption>Random effect meta-analysis of EQ-5D utility in patients with COVID-19</figcaption>
</figure>

<div id="Tab2" class="table-wrap">

<div class="caption">

Pooled estimates of EQ-5D utility scores, EQ-5D VAS scores, and EQ-5D profiles among COVID-19 patients

</div>

| Variable | No. of articles | Estimate | Lower bound | Upper bound | Std. error |
|----|----|----|----|----|----|
| Pooled estimate of EQ-5D index | 127 | 0.76 | 0.74 | 0.79 | 0.01 |
| Pooled estimate of EQ-VAS Score | 161 | 70.76 | 68.48 | 73.04 | 1.16 |
| Pooled estimate of any problems in mobility (%) | 104 | 37 | 32 | 42 | 2.5 |
| Pooled estimate of any problems in self-care (%) | 104 | 21 | 17 | 24 | 1.9 |
| Pooled estimate of any problems in usual activity (%) | 104 | 42 | 35 | 48 | 3.3 |
| Pooled estimate of any problems in pain/discomfort (%) | 104 | 51 | 45 | 56 | 2.8 |
| Pooled estimate of any problems in anxiety/depression (%) | 104 | 46 | 40 | 52 | 3.0 |

*EQ−5D* EuroQol 5 Dimensions, *VAS* Visual Analog Scale

</div>

Pooled estimates were also calculated for the different dimensions of the EQ-5D instrument, including mobility (Figure <a href="#MOESM1" data-ref-type="media">S2</a>), self-care (Figure <a href="#MOESM1" data-ref-type="media">S3</a>), usual activities (Figure <a href="#MOESM1" data-ref-type="media">S4</a>), pain/discomfort (Figure <a href="#MOESM1" data-ref-type="media">S5</a>), and anxiety/depression (Figure <a href="#MOESM1" data-ref-type="media">S6</a>). Among these, pain/discomfort and anxiety/depression were the most affected dimensions, affecting 51% (95% CI 45–56) and 46% (95% CI 40–52) of patients, respectively, as summarized in Table <a href="#Tab2" data-ref-type="table">2</a>.

### Subgroup analysis of EQ-5D utility scores

Our subgroup meta-analysis aimed to identify factors contributing to the wide variation in HRQoL among COVID-19 patients. Of the six variables examined, only geographic region and national income status showed a statistically significant association with HRQoL.

***EQ-5D instrument versions***: When comparing utility scores across the two versions of the EQ-5D instrument, the results showed that a similar mean utility score of the EQ-5D-5 L score of 0.76 (95% CI 0.74–0.79), compared to a mean score of 0.76 (95% CI 0.71–0.81) for studies using the EQ-5D-3 L version. Statistically, this difference was not significant (*p* = 0.88), as illustrated in Figure <a href="#MOESM1" data-ref-type="media">S7</a>.

***Geographic regions***: Patients in Asia had the highest mean utility score of 0.85 (95% CI 0.76–0.93), followed by North America at 0.84 (95% CI 0.82–0.86), while Europe had the lowest at 0.72 (95% CI 0.70–0.74). The differences in mean utility scores among the different continents were statistically significant (*p* \< 0.001) (Figure <a href="#MOESM1" data-ref-type="media">S8</a>).

***Study design***: Utility scores were slightly higher in cohort studies (0.75, 95% CI 0.70–0.80) compared to cross-sectional studies (0.77, 95% CI 0.74–0.80), though the difference was not statistically significant (*p* = 0.45) (Figure <a href="#MOESM1" data-ref-type="media">S9</a>).

***Time of HRQoL measurements after the COVID-19 diagnosis***: Patients evaluated three months or more after their diagnosis tended to report slightly higher utility scores (0.80, 95% CI 0.77–0.82) compared to those assessed within the first three months (0.78, 95% CI 0.70–0.86). However, this difference was not statistically significant (*p* = 0.72) (Figure <a href="#MOESM1" data-ref-type="media">S10</a>).

***Income category***: When stratifying by income, patients in the low to middle-income subgroup had higher utility scores of 0.83 (95% CI 0.76–0.90) compared to the high-income subgroup at 0.75 (95% CI 0.72–0.77). This difference was statistically significant (*p* = 0.038) (Figure <a href="#MOESM1" data-ref-type="media">S11</a>).

***Age classification***: Patients aged 60 and over tended to report slightly lower utility scores (0.74, 95% CI 0.69–0.80), than those under 60 (0.76, 95% CI 0.73–0.78), but this small difference wasn’t statistically meaningful (*p* = 0.67) (Figure <a href="#MOESM1" data-ref-type="media">S12</a>).

### Sensitivity analysis and publication bias

We conducted a sensitivity analysis to verify the robustness of the results. The leave-one-out method showed that removing any single study did not affect the overall result, confirming that the findings are stable and not driven by any one study (Figure <a href="#MOESM1" data-ref-type="media">S13</a>). Excluding studies with fewer than 100 participants yielded a utility score of 0.77 (95% CI 0.75–0.79). Similarly, omitting studies with a NOS score below 6 resulted in a mean utility score of 0.77 (95% CI 0.74–0.81), confirming the stability of our results (Table <a href="#MOESM1" data-ref-type="media">S3</a>). The risk of publication bias was assessed using Egger’s regression test, and the results showed no significant evidence of bias (*p* = 0.27), indicating that the findings are likely to be reliable and not influenced by unpublished studies.

### Predictors of poor HRQoL in patients with COVID-19: qualitative synthesis of literature

We identified 42 studies that reported on the predictors of poor HRQoL among COVID-19 survivors. We found that over 50 different predictor variables were documented (Table <a href="#MOESM1" data-ref-type="media">S4</a>). We have grouped these predictors into three main categories: demographic, socioeconomic, and clinical factors.

### Demographic factors

Age was consistently identified as a predictor, with most studies reporting that older individuals generally exhibited lower HRQoL scores \[6, 30–51\]. However, one study found that younger age was linked to worse HRQoL \[52\]. Sex was also a significant factor; several studies consistently associated female sex with poorer HRQoL \[30, 35, 37, 39, 40, 51, 53–65\], whereas three studies identified male sex as a predictor of poorer HRQoL \[42, 43, 66\].

### Socioeconomic factors

Being unemployed was associated with poorer HRQoL \[30, 35, 52, 60, 62, 67\] and being a housewife or retired was also linked to lower HRQoL \[41\]. Higher education, compared with lower or middle education levels, was reported in some studies as a predictor of poor HRQoL \[30\], whereas other studies found that lower education levels were associated with worse outcomes \[52, 65, 68\]. Lower household income \[68, 69\], and living in rural areas, compared with urban settings, were also associated with poorer HRQoL \[67\]. Additional factors linked to reduced HRQoL included higher social impairment \[62\], lower resilience \[70\], and less support from significant others \[70\].

### Clinical factors

***Disease severity***: Greater disease severity during acute COVID-19 was consistently associated with poorer HRQoL \[31, 33, 38, 42, 50, 58, 71–75\]. Specific indicators of severe disease such as ICU admission or requirement \[30, 55, 76\], oxygen requirements during COVID-19 \[42\], lung diffusion impairment \[53\], pulmonary injury \[74\], pulmonary embolism \[77\], higher level of CRP levels \[74, 78\], and experiencing delirium \[79\] during the acute phase were reported to have worse HRQoL.

***Comorbidities***: Presence of comorbidity \[33, 35, 37, 41, 42, 49, 52, 61, 71, 80–82\], greater number of comorbidities \[32, 68\], pre-existing specific conditions like diabetes \[30, 34, 75\], cardiovascular disease \[30, 34, 47, 60, 62, 74, 83\], hypertension \[75, 84\], kidney disease \[34\], asthma \[31, 38, 47\], COPD \[38, 47\], pulmonary disease \[60\], malignancy \[38\], presence of metabolic diseases \[58\], higher preclinical frailty \[85, 86\], history of depression \[62, 87\], and autoimmune disease \[62\] were associated with poorer HRQoL.

***Post-COVID symptoms or syndromes***: Persistent COVID-19 symptom/long covid status \[6, 37, 40, 41, 44, 58, 62, 64, 69–71, 78, 82, 83, 88–93\] including specifically reported symptoms such as fatigue \[46, 56, 91, 94, 95\], dyspnea \[56, 66, 91, 94, 96, 97\], anxiety and depression \[57, 58, 94, 95, 98, 99\], sleep quality \[99\], headache \[91\], pain \[46, 56, 57, 91, 98\], memory problems \[91\], delirium \[48\], number of persistent symptoms \[46, 49, 74\], visual problems \[65\], myalgia \[65\], seeing a physician for olfactory dysfunction \[57\], disability \[68\], being in a higher symptom burden phenotype \[100\], seeking care in long COVID clinic \[89\], altered physical activities \[101\], and higher functional impairment \[49\] were significantly associated with poorer HRQoL.

***Hospitalization and treatment***: Duration of illness at admission \[42, 54\], being hospitalized \[39, 84\], length of hospital stay \[38, 42, 43, 54, 60, 74, 80\], ICU admission \[51\], length of ICU stay \[43, 81\], not being vaccinated \[52, 84\], hospitalization during the acute phase \[75\], mechanical ventilation use \[43, 45, 48, 85\], and duration of mechanical ventilation \[63\] were linked to poorer HRQoL in some studies. Other factors associated with poorer HRQoL were tracheostomy \[66, 79\], presence of fibrous stripe on chest CT \[40\], and longer duration of steroid use \[42\]. However, steroid use was reported in some studies to improve HRQoL compared with no steroid use \[31, 61\].

***Other factors*** such as obesity and/or BMI \> 35 \[35, 41, 45, 52, 66, 83\],, history of smoking \[34, 36, 53, 66, 72, 75\], death of a family member from COVID-19 \[6\], pre-existing psychological condition \[78\], living alone \[6, 37\], stress \[37\], lower self-efficacy \[102\], and poorer HRQoL in people exercising more than 5 h per week pre-COVID compared to 2 to 5 h and 0 to 2 h \[89\] were also identified as predictors.

### Risk-of-bias (quality) assessment results

In our study, we utilized the NOS to evaluate the quality of included studies, focusing on three key criteria: selection, comparability, and outcome assessment. Each study was assigned a quality score out of a possible 9 points. Specifically, studies could earn up to 4 stars for selection, 2 stars for comparability, and 3 stars for outcome assessment.

We classified the quality of the articles as follows: high quality for scores between 7 and 9 stars, moderate quality for scores between 4 and 6 stars, and low quality for scores between 0 and 3 stars. The median quality score across all articles was 6, with scores ranging from 3 to 9. Among the evaluated studies, 2.7% (*n* = 5) were deemed to be of low quality, 58.5% (*n* = 110) were of moderate quality, and 38.8% (*n* = 73) were considered high quality. Detailed quality scores for each article can be found in Supplementary Table <a href="#MOESM1" data-ref-type="media">S1</a>.

## Discussion

We conducted a comprehensive systematic review and meta-analysis of HRQoL following COVID-19, using the EQ-5D instrument for assessment. The analysis found that the pooled mean EQ-5D index score and EQ-VAS score were 0.76 and 70.76, respectively. These values indicate a reduction in HRQoL among COVID-19 patients compared to population norms. For example, reported EQ-5D utility scores from population norms in various countries, such as the US (0.87), France (0.89), and Korea (0.95), UK (0.86), China (0.95), Zimbabwe (0.83) are higher than those observed in our study \[103\]. A recent meta-analysis also reported a higher pooled mean EQ-5D utility score of 0.89 in the general population, further underscoring the impact of COVID-19 on patient HRQoL \[104\]. Lower EQ-5D utility scores in COVID-19 patients compared to population norms show the lasting impact of long COVID and the need for a holistic recovery approach. Healthcare systems should use these findings to guide comprehensive rehabilitation and mental health services aimed at restoring quality of life. Policymakers should also adopt targeted public health and socioeconomic measures to reduce disparities among vulnerable groups.

Our findings show that pain/discomfort and anxiety/depression are the most affected HRQoL dimensions, with impairments reported by 51% and 46% of participants, respectively. These results are consistent with previous research, which has also identified these dimensions as commonly affected \[23\]. The high prevalence of pain/discomfort may reflect persistent physical sequelae, such as musculoskeletal pain, neuropathic symptoms, and chronic fatigue, whereas anxiety/depression likely results from a combination of biological mechanisms (e.g., neuroinflammation, hypothalamic–pituitary–adrenal axis dysregulation) and psychosocial stressors (e.g., social isolation, employment loss, uncertainty about recovery) \[105, 106\].

We found higher levels of impairment in pain/discomfort and anxiety/depression than those reported in population norms from a multicountry European study (28.5% for pain/discomfort and 8% for anxiety/depression) \[107\], as well as in general population samples from China (10.7% and 8.7%) and the UK (33% and 21%) \[103\]. The substantial impairments in our study underscore the need for tailored clinical interventions. Implementing comprehensive pain management strategies, which include pharmacological interventions, physical therapy, and mental health support, is essential \[108, 109\]. Additionally, cognitive behavioral therapy and physical exercise programs have shown significant effectiveness in mitigating depression and anxiety linked to the COVID-19 pandemic \[110\]. Adopting these evidence-based approaches is vital for improving the overall quality of life for those affected. However, the results of our meta-analysis should be interpreted cautiously due to high study heterogeneity.

The heterogeneity in EQ-5D index scores (I<sup>2</sup> = 99.9%) and VAS scores (I<sup>2</sup> = 99.7%) indicates substantial variability in reported outcomes across studies. This heterogeneity may arise from various factors, including differences in study populations, geographical locations, access to rehabilitation services, and healthcare systems. Factors such as disease severity, comorbidities, socioeconomic status, and access to healthcare services can influence the variability. Moreover, variations in methodological sources including variations in EQ-5D administration (telephone, online, face-to-face), choice of value sets for index calculation, differences in time since infection when HRQoL was measured, and survey design (self-reported vs. interviewer-administered) may also contribute to the observed heterogeneity. HRQoL in COVID-19 patients may have also changed over time due to improvements in treatment, vaccination, and viral variants. These temporal factors may contribute to differences across studies and should be considered when interpreting results.

Our subgroup analysis revealed significant variations in HRQoL across geographic regions, with patients in Asia generally reporting higher utility scores (0.85) compared to those in Europe (0.72). However, direct comparisons of HRQoL across continents are inherently complex and demand cautious interpretation due to different influencing factors. These include methodological differences across studies, the specific populations surveyed (e.g., general population vs. hospitalized patients), differences in quarantine and isolation measures, diverse socioeconomic, cultural, and social conditions that impact health states. The inconsistencies warrant cautious interpretation and highlight the need for standardized EQ-5D reporting in future studies to facilitate cross-comparisons.

When stratified by income, patients in the low-middle-income subgroup reported higher utility scores (0.83; 95% CI 0.76–0.90) compared to the high-income subgroup (0.75; 95% CI 0.72–0.77). This disparity could result from the large number of articles from European countries (56%) included in the study, given that Europe generally experienced a relative decline in HRQoL, and most European countries are high-income, which could have potentially lowered the overall high-income average. The finding may also reflect differences in baseline health expectations, variations in life expectancy, differences in sample composition, or selection bias toward less severe cases in LMIC studies.

Various studies have identified predictors of poor HRQoL in COVID-19 patients, including, female gender, severe disease, comorbidities, and post-COVID symptoms, highlighting the vulnerability of certain groups. This observation is consistent with findings from a previous systematic review that employed a different HRQoL measure \[111\].

In our literature review, we observed that EQ-5D is widely used, but variability in the reporting of different components of the EQ-5D across various studies exists. Some studies solely reported the EQ-5D profile, while others reported either the EQ VAS or EQ-5D index, or both. For consistency and to facilitate synthesis of information, it is recommended that studies report all index scores, VAS scores, and health profiles where possible \[14\].

One of the strengths of our systematic review and meta-analysis is that it includes a large number of studies (187 in total) conducted over a long period. By using a single, widely accepted tool, the EQ-5D, we ensured consistent measurement of HRQoL across all studies, making it easier to combine the results. While other reviews, like the one by Nandasena et al., have also looked at HRQoL in COVID-19 patients, they only included 21 studies and did not provide a pooled estimate of utility values \[111\]. Malik et al. conducted a meta-analysis on post-acute COVID-19 syndrome and HRQoL, but this was done early in the pandemic and only included 12 studies \[23\].

Our findings have important implications for clinical practice and policy-making. They can help healthcare professionals and policymakers better understand which groups might experience a greater burden due to COVID-19. Researchers and decision-makers can also use the mean utility value from our study for cost-effectiveness analyses related to COVID-19 interventions, aiding in the calculation of QALYs. Our pooled EQ-5D utility values can inform cost–utility analyses for long-COVID programs, such as in assessing the cost-effectiveness of rehabilitation programs aimed at restoring mobility and usual activities, in prioritizing mental health interventions like cognitive behavioral therapy for anxiety/depression, and remote care models.

However, our study is not without limitations. The quality of the studies included varied, with some having small sample sizes, low response rates, or incomplete data. This variability may have affected the pooled estimates and generalizability of our findings. Additionally, we had initially planned subgroup analyses based on factors such as disease severity, complications, vaccination status, and access to COVID testing. However, due to inadequate or unclear information about these factors, we were unable to conduct these analyses. Some studies reported medians and ranges rather than means and standard deviations. To maintain consistency across studies, we used only the final HRQoL assessment when multiple time points were reported. While this approach helps standardize comparisons, it may bias results toward recovery, as HRQoL tends to improve over time. We estimated means and SDs using established methods and these estimations may be less accurate for skewed data, potentially affecting the precision of our pooled results. We also limited our review to English-language publications due to resource constraints, which may have excluded relevant studies from non-English-speaking regions.

Despite the large number of studies included, several important gaps remain that warrant attention in future research. Data on key factors such as vaccination status, which could modulate HRQoL through reduced symptom severity; access to COVID-19 testing and early diagnosis; adherence to treatment protocols like oxygen therapy or antivirals, hospitalization status or ICU admissions, limiting our ability to assess their impact on HRQoL outcomes. Future research should prioritize longitudinal studies incorporating these variables to identify modifiable risk factors and evaluate intervention efficacy over time.

## Conclusion

This systematic review and meta-analysis contribute to the growing body of literature on HRQoL in patients with COVID-19. Our findings show that individuals with COVID-19 had lower EQ-5D index scores, EQ-VAS scores, and EQ-5D profiles, indicating a reduced HRQoL compared to the general population. In our subgroup analysis, we identified geographic locations and incomes status of the countries as significant factors associated with HRQoL. The mean utility value derived from this study aids in understanding patients’ HRQoL and could assist future economic studies and policy decisions.

## Supplementary Information

<div class="caption">

Supplementary Material 1

</div>

### Abbreviations

COPD  
Chronic Obstructive Pulmonary Disease

COVID-19  
Coronavirus Disease 2019

EQ-5D  
EuroQol-5 Dimension

EQ-VAS  
EuroQol Visual Analogue Scale

HRQoL  
Health-Related Quality of Life

HUI  
Health Utilities Index

I<sup>2</sup>  
I-squared (statistic for heterogeneity in meta-analysis)

ICU  
Intensive Care Unit

NICE  
National Institute for Health and Care Excellence

NOS  
Newcastle-Ottawa Scale

PRISMA  
Preferred Reporting Items for Systematic Reviews and Meta-Analyses

QALYs  
Quality-Adjusted Life Years

SD  
Standard Deviation

SF-6D  
Short-Form 6-Dimension

### Acknowledgements

This study was funded by the EuroQol Research Foundation (Grant No. 1627-RA).

### Author contributions

KG and EL conceived and designed the study. KG, YLN, and SWA acquired the data, while KG, YLN, SWA, and EL analyzed and interpreted it. KG and YLN drafted the manuscript, with all authors (KG, YLN, SWA, and EL) providing critical revisions for intellectual content. KG secured funding, and KG and EL provided administrative and logistical support. EL supervised the study. All authors have read and approved the final manuscript.

### Funding

This project has been supported by the EuroQol Research Foundation (1627-RA). **Role of the Funder/Sponsor**: The funder had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

### Data availability

The datasets used and/or analyzed during the current study are available from the corresponding author on reasonable request.

### Declarations

#### Competing interests

The authors declare no competing interests.

#### Ethical approval and consent to participate

Not applicable.

#### Consent for publication

Not applicable.

#### Disclaimer

The views expressed by the authors in the publication do not necessarily reflect the views of EuroQol group.

## References

1. Chauhan S. Comprehensive review of coronavirus disease 2019 (COVID-19). Biomed J. 2020;43(4):334–40.32788071 10.1016/j.bj.2020.05.023PMC7263230

2. Daher A, Balfanz P, Cornelissen C, Müller A, Bergs I, Marx N, et al. Follow up of patients with severe coronavirus disease 2019 (COVID-19): pulmonary and extrapulmonary disease sequelae. Respir Med. 2020;174:106197.33120193 10.1016/j.rmed.2020.106197PMC7573668

3. Burn E, Tebe´ C, Fernandez-Bertolin S, et al. The natural history of symptomatic COVID-19 during the first wave in Catalonia. Nat Commun. 2021;12:777.33536436 10.1038/s41467-021-21100-yPMC7858639

4. Aiyegbusi OL, Hughes SE, Turner G, Rivera SC, McMullan C, Chandan JS, Haroon S, Price G, Davies EH, Nirantharakumar K. Symptoms, complications and management of long COVID: a review. J R Soc Med. 2021;114:428–42.34265229 10.1177/01410768211032850PMC8450986

5. Huang C, Huang L, Wang Y, Li X, Ren L, Gu X, Kang L, Guo L, Liu M, Zhou X, et al. 6-Month consequences of COVID-19 in patients discharged from hospital: A cohort study. Lancet. 2021;397:220–32.33428867 10.1016/S0140-6736(20)32656-8PMC7833295

6. Huarcaya-Victoria J, Alarcon-Ruiz CA, Barzola-Farfan W, Cruzalegui-Bazan C, Cabrejos-Espinoza M, Aspilcueta-Montoya G, et al. One-year follow-up of depression, anxiety, and quality of life of Peruvian patients who survived COVID-19. Qual Life Res. 2023;32:139–49.35939252 10.1007/s11136-022-03208-wPMC9358105

7. Horowitz E, Hassidim H, Abadi-Korek I, Shemer J. [Assessment of health related quality of life–part 3–preference based measures]. Harefuah. 2008;147:914–9.19264015

8. Brazier JE, Rowen D, Lloyd A, Karimi M. Future directions in valuing benefits for estimating QALYs: is time up for the EQ-5D? Value Health. 2019;22:62–8.30661635 10.1016/j.jval.2018.12.001

9. National Institute for Health and Care Excellence (NICE). Guide to the Methods of Technology Appraisal; 2013. https://www.nice.org.uk/process/pmg927905712

10. Vergouwe M, Birnie E, van Veelen S, Biemond JJ, Appelman B, Peters-Sengers H, de Bree GJ, Popping S, Wiersinga WJ. Group T-CS. A longitudinal description of the Health-Related quality of life among individuals at high risk after SARS-CoV-2 infection: A Dutch multicenter observational cohort study. Open Forum Infect Dis. 2025;12:ofaf055.10.1093/ofid/ofaf055PMC1183717239974282

11. Efthymiadou O, Mossman J, Kanavos P. Health related quality of life aspects not captured by EQ-5D-5L: results from an international survey of patients. Health Policy. 2019;123:159–65.30598239 10.1016/j.healthpol.2018.12.003

12. Whynes DK. Correspondence between EQ-5D health state classifications and EQ VAS scores. Health Qual Life Outcomes. 2008;6:94.18992139 10.1186/1477-7525-6-94PMC2588564

13. Vélez-Santamaría R, Fernández-Solana J, Méndez-López F, Domínguez-García M, González-Bernal JJ, Magallón-Botaya R, et al. Functionality, physical activity, fatigue and quality of life in patients with acute COVID-19 and long COVID infection. Sci Rep. 2023;13:19907.37963962 10.1038/s41598-023-47218-1PMC10645778

14. Devlin N, Parkin D, Janssen B. Methods for analysing and reporting EQ-5D data. Cham (CH): Springer; 2020.33347096

15. Bansback N, Sun H, Guh DP, Li X, Nosyk B, Griffin S, et al. Impact of the recall period on measuring health utilities for acute events. Health Econ. 2008;17:1413–9.18404664 10.1002/hec.1351

16. Sutton AJ, Higgins JP. Recent developments in meta-analysis. Stat Med. 2008;27(5):625–50.17590884 10.1002/sim.2934

17. Petrou S, Kwon J, Madan J. A practical guide to conducting a systematic review and meta-analysis of health state utility values. Pharmacoeconomics. 2018;36:1043–61.29750430 10.1007/s40273-018-0670-1

18. Ara R, Brazier J, Peasgood T, et al. The identification, review and synthesis of health state utility values from the literature. Pharmacoeconomics. 2017;35(Suppl 1):43–55.29052156 10.1007/s40273-017-0547-8

19. Soriano JB, Murthy S, Marshall JC, Relan P, Diaz JV. A clinical case definition of post-COVID-19 condition by a Delphi consensus. Lancet Infect Dis. 2022;22:e102–7.34951953 10.1016/S1473-3099(21)00703-9PMC8691845

20. Al-Aly Z, Davis H, McCorkell L, Soares L, Wulf-Hanson S, Iwasaki A, et al. Long COVID science, research and policy. Nat Med. 2024;30:2148–64.39122965 10.1038/s41591-024-03173-6

21. Xu F, Brodszky V. The impact of COVID-19 on health-related quality of life: a systematic review and evidence-based recommendations. Discover Psychology. 2024;4:90. doi:10.1007/s44202-024-00204-8

22. Figueiredo EAB, Silva WT, Tsopanoglou SP, Vitorino DFM, Oliveira LFL, Silva KLS, Luz HDH, Ávila MR, Oliveira LFF, Lacerda ACR, et al. The health-related quality of life in patients with post-COVID-19 after hospitalization: a systematic review. Rev Soc Bras Med Trop. 2022;55:e0741.35352761 10.1590/0037-8682-0741-2021PMC9053755

23. Malik P, Patel K, Pinto C, Jaiswal R, Tirupathi R, Pillai S, et al. Post-acute COVID-19 syndrome (PCS) and health-related quality of life (HRQoL)-a systematic review and meta-analysis. J Med Virol. 2022;94:253–62.34463956 10.1002/jmv.27309PMC8662132

24. Moher D, Liberati A, Tetzlaff J, Altman DG. Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. BMJ. 2009;339:b2535.19622551 10.1136/bmj.b2535PMC2714657

25. Wells G, Shea B, O’Connell D, et al. The Newcastle-Ottawa scale (NOS) for assessing the quality of non-randomized studies in meta-analysis. Appl Eng Agric. 2014;18(6):727–34.

26. Herzog R, Álvarez-Pasquin MJ, Díaz C, Del Barrio JL, Estrada JM, Gil Á. Are healthcare workers’ intentions to vaccinate related to their knowledge, beliefs and attitudes? A systematic review. BMC Public Health. 2013;13:1–17.23421987 10.1186/1471-2458-13-154PMC3602084

27. Higgins JP, Thompson SG, Deeks JJ, et al. Measuring inconsistency in meta-analyses. BMJ. 2003;327(7414):557–60.12958120 10.1136/bmj.327.7414.557PMC192859

28. Hozo SP, Djulbegovic B, Hozo I. Estimating the mean and variance from the median, range, and the size of a sample. BMC Med Res Methodol. 2005;5:13.15840177 10.1186/1471-2288-5-13PMC1097734

29. Wan X, Wang W, Liu J, Tong T. Estimating the sample mean and standard deviation from the sample size, median, range and/or interquartile range. BMC Med Res Methodol. 2014;14:135.25524443 10.1186/1471-2288-14-135PMC4383202

30. Arab-Zozani M, Hashemi F, Safari H, Yousefi M, Ameri H. Health-related quality of life and its associated factors in COVID-19 patients. Osong Public Health Res Perspect. 2020;11:296–302.33117634 10.24171/j.phrp.2020.11.5.05PMC7577388

31. Kaso AW, Agero G, Hurisa Z, Kaso T, Ewune HA, Hailu A. Evaluation of health-related quality of life of Covid-19 patients: a hospital-based study in South central Ethiopia. Health Qual Life Outcomes. 2021;19:268.34930294 10.1186/s12955-021-01900-yPMC8685489

32. Malinowska A, Muchlado M, Ślizień Z, Biedunkiewicz B, Heleniak Z, Dębska-Ślizień A, et al. Post-COVID-19 sydrome and decrease in health-related quality of life in kidney transplant recipients after SARS-COV-2 infection—a cohort longitudinal study from the North of Poland. J Clin Med. 2021;10(21):5205.34768725 10.3390/jcm10215205PMC8584685

33. Walle-Hansen MM, Ranhoff AH, Mellingsæter M, Wang-Hansen MS, Myrstad M. Health-related quality of life, functional decline, and long-term mortality in older patients following hospitalisation due to COVID-19. BMC Geriatr. 2021;21(1):199.33752614 10.1186/s12877-021-02140-xPMC7983098

34. Azizi A, Achak D, Saad E, Hilali A, Nejjari C, Khalis M, et al. Health-related quality of life of Moroccan COVID-19 survivors: a case-control study. Int J Environ Res Public Health. 2022;19(14):8804.35886656 10.3390/ijerph19148804PMC9317197

35. d’Ettorre G, Vassalini P, Coppolelli V, Gentilini Cacciola E, Sanitinelli L, Maddaloni L, Fabris S, Mastroianni CM, d’Ettorre G, Ceccarelli G. Health-related quality of life in survivors of severe COVID-19 infection. Pharmacol Rep. 2022;74:1286–95.36376776 10.1007/s43440-022-00433-5PMC9662770

36. Hegde S, Sreeram S, Bhat KR, Satish V, Shekar S, Babu M. Evaluation of post-COVID health status using the EuroQol-5D-5L scale. Pathog Glob Health. 2022;116:498–508.35129097 10.1080/20477724.2022.2035623PMC9639560

37. Huynh G, Nguyen BT, Nguyen HTN, Le NT, An PL, Tran TD. Health-Related quality of life among patients recovered from COVID-19. Inquiry. 2022;59:469580221143630.36527371 10.1177/00469580221143630PMC9760520

38. Kaso AW, Tesema HG, Hareru HE, Kaso T, Ashuro Z, Talemahu AA, et al. Health-related quality of life and associated factors among Covid-19 survivors. Experience from Ethiopian treatment centers. Infect Drug Resist. 2022;15:6143–53.36304968 10.2147/IDR.S386566PMC9593469

39. Koullias E, Fragkiadakis G, Papavdi M, Manousopoulou G, Karamani T, Avgoustou H, et al. Long-term effect on health-related quality of life in patients with COVID-19 requiring hospitalization compared to non-hospitalized COVID-19 patients and healthy controls. Cureus. 2022;14:e31342.36514618 10.7759/cureus.31342PMC9741546

40. Zhang L, Lei J, Zhang J, Yin L, Chen Y, Xi Y, et al. Undiagnosed long COVID-19 in China among non-vaccinated individuals: identifying persistent symptoms and impacts on patients’ health-related quality of life. J Epidemiol Glob Health. 2022;12:560–71.36434150 10.1007/s44197-022-00079-9PMC9702954

41. Hoque MM, Datta PK, Basu KC, Rahman MF, Khan MMH, Kamal MM, et al. Post-discharge quality of life of COVID-19 patients at 1-month follow-up: a cross-sectional study in the largest tertiary care hospital of Bangladesh. PLoS One. 2023;18:e0280882.36719890 10.1371/journal.pone.0280882PMC9888719

42. Shah C, Keerthi BY, Gali JH. An observational study on health-related quality of life and persistent symptoms in COVID-19 patients after hospitalization at a tertiary care centre. Lung India. 2023;40:12–8.36695253 10.4103/lungindia.lungindia_126_22PMC9894290

43. Taboada M, Moreno E, Leal S, Pita-Romero R, Sanduende Y, Rama P, Cid M, Seoane-Pillado T. Long-term outcomes after tracheostomy for COVID-19. Arch Bronconeumol. 2021;57:54–6.34629652 10.1016/j.arbres.2021.01.014PMC8046359

44. Sandmann FG, Tessier E, Lacy J, Kall M, Van Leeuwen E, Charlett A, Eggo RM, Dabrera G, Edmunds WJ, Ramsay M, et al. Long-Term Health-Related quality of life in Non-Hospitalized coronavirus disease 2019 (COVID-19) cases with confirmed severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infection in england: longitudinal analysis and Cross-Sectional comparison with controls. Clin Infect Dis. 2022;75:e962–73.35245941 10.1093/cid/ciac151PMC8903473

45. Evans RA, Leavy OC, Richardson M, Elneima O, McAuley HJC, Shikotra A, Singapuri A, Sereno M, Saunders RM, Harris VC et al. Clinical characteristics with inflammation profiling of long-COVID and association with one-year recovery following hospitalisation in the UK: a prospective observational study. Lancet Respir Med. 2021;10(8):761–75.10.1016/S2213-2600(22)00127-8PMC903485535472304

46. Neumann C, Hartung TJ, Boje K, Bahmer T, Keil J, Lieb W, Franzpoetter K, Welzel J, Chaplinskaya-Sobol I, Endres M, et al. Factors associated with reduction in quality of life after SARS-CoV-2 infection. Sci Rep. 2025;15:6833.40000883 10.1038/s41598-025-91388-zPMC11861590

47. Rego de Figueiredo I, Branco Ferrao J, Dias S, Drummond Borges D, Fernandes J, Bernardino V, Gruner H, Panarra A. The prevalence of COVID-19 fog and the impact on quality of life after SARS-CoV-2 infection (QoL-COVID): A cross sectional study. Acta Med Port. 2023;36:631–8.36790319 10.20344/amp.18784

48. Hatakeyama J, Nakamura K, Inoue S, Liu K, Yamakawa K, Nishida T, et al. Two-year trajectory of functional recovery and quality of life in post-intensive care syndrome: a multicenter prospective observational study on mechanically ventilated patients with coronavirus disease-19. J Intensive Care. 2025;13:7.39915821 10.1186/s40560-025-00777-zPMC11800417

49. Bolgeo T, Di Matteo R, Gatti D, Cassinari A, Damico V, Ruta F, Gambalunga F, Maconi A. Impact of COVID-19 on quality of life after hospital discharge in patients treated with noninvasive ventilation/continuous positive airway pressure: an observational, prospective multicenter study. Dimens Crit Care Nurs. 2024;43:3–12.38059706 10.1097/DCC.0000000000000614

50. Salem A, Mostafa R, Sedrak A, Hegazy M, Mohamed H, Ibrahim M, et al. Assessing health-related quality of life and inducing factors in COVID-19 cases at Kasralainy teaching hospital, Egypt. Egypt J Med Microbiol. 2023;32:117–26. doi:10.21608/ejmm.2023.325931

51. Firouzabadi D, Mahmoudi L, Kadkhodamohammadi M, Niknam R, Amanati A. Health-related quality of life (HRQoL) in COVID-19 patients after recovering from the acute infection. Arch Pediatr Infect Dis. 2024;12(4):e149370. doi:10.5812/apid-149370

52. Brus IM, Spronk I, Haagsma JA, de Groot A, Tieleman P, Biere-Rafi S, Polinder S. The prolonged impact of COVID-19 on symptoms, health-related quality of life, fatigue and mental well-being: a cross-sectional study. Front Epidemiol. 2023;3:1144707.38455946 10.3389/fepid.2023.1144707PMC10911032

53. Huang L, Yao Q, Gu X, Wang Q, Ren L, Wang Y, et al. 1-year outcomes in hospital survivors with COVID-19: a longitudinal cohort study. Lancet. 2021;398:747–58.34454673 10.1016/S0140-6736(21)01755-4PMC8389999

54. Shah R, Ali FM, Nixon SJ, Ingram JR, Salek SM, Finlay AY. Measuring the impact of COVID-19 on the quality of life of the survivors, partners and family members: a cross-sectional international online survey. BMJ Open. 2021;11:e047680.34035105 10.1136/bmjopen-2020-047680PMC8154981

55. Todt BC, Szlejf C, Duim E, Linhares AOM, Kogiso D, Varela G, Campos BA, Baghelli Fonseca CM, Polesso LE, Bordon INS, et al. Clinical outcomes and quality of life of COVID-19 survivors: A follow-up of 3 months post hospital discharge. Respir Med. 2021;184:106453.34010740 10.1016/j.rmed.2021.106453PMC8116128

56. Barreto APA, Barreto Filho MA, Duarte LC, Cerqueira-Silva T, Camelier A, Tavares NM, Barral-Netto M, Boaventura V, Lima MCC. Metabolic disorders and post-acute hospitalization in black/mixed-race patients with long COVID in brazil: A cross-sectional analysis. PLoS ONE. 2022;17:e0276771.36315558 10.1371/journal.pone.0276771PMC9621406

57. Said M, Luong T, Jang SS, Davis ME, DeConde AS, Yan CH. Clinical factors associated with lower health scores in COVID-19-related persistent olfactory dysfunction. Int Forum Allergy Rhinol. 2022;12:1242–53.35032409 10.1002/alr.22978PMC9011709

58. Soh HS, Cho B. Long COVID-19 and health-related quality of life of mild cases in Korea: 3-months follow-up of a single community treatment center. J Korean Med Sci. 2022;37:e326.36631024 10.3346/jkms.2022.37.e326PMC9705205

59. Slotegraaf AI, Gerards MHG, Verburg AC, de van der Schueren MAE, Kruizenga HM, Graff MJL, Cup EHC, Kalf JG, Lenssen AF, Meijer WM et al. Evaluation of primary allied health care in patients recovering from COVID-19 at 6-month follow-up: Dutch nationwide prospective cohort study. JMIR Public Health Surv. 2023;9:e44155.10.2196/44155PMC1059272137862083

60. Berentschot JC, Bek LM, Heijenbrok-Kal MH, van Bommel J, Ribbers GM, Aerts J, Hellemons ME, van den Berg-Emons HJG. Group C-Fc: Long-term health outcomes of COVID-19 in ICU- and non-ICU-treated patients up to 2 years after hospitalization: a longitudinal cohort study (CO-FLOW). J Intensive Care. 2024;12:47.39516956 10.1186/s40560-024-00748-wPMC11546104

61. Mastrorosa I, Del Duca G, Pinnetti C, Lorenzini P, Vergori A, Brita AC, Camici M, Mazzotta V, Baldini F, Chinello P, et al. What is the impact of post-COVID-19 syndrome on health-related quality of life and associated factors: a cross-sectional analysis. Health Qual Life Outcomes. 2023;21:28.36949439 10.1186/s12955-023-02107-zPMC10031164

62. Schroder D, Heinemann S, Heesen G, Hummers E, Schmachtenberg T, Dopfer-Jablonka A, et al. Association of long COVID with health-related quality of life and social participation in Germany: finding from an online-based cross-sectional survey. Heliyon. 2024;10:e26130.38380019 10.1016/j.heliyon.2024.e26130PMC10877341

63. Caamano E, Velasco L, Garcia MV, Asencio JM, Pineiro P, Hortal J, et al. Prognostic factors for deterioration of quality of life one year after admission to ICU for severe SARS-COV2 infection. Qual Life Res. 2024;33:123–32.37615735 10.1007/s11136-023-03503-0

64. Galanis P, Katsiroumpa A, Vraka I, Kosiara K, Siskou O, Konstantakopoulou O, et al. Post-COVID-19 syndrome and related dysautonomia: reduced quality of life, increased anxiety and manifestation of depressive symptoms: evidence from Greece. Acta Med Lituan. 2023;30:139–51.10.15388/Amed.2023.30.2.6PMC1095243038516508

65. Kılınçarslan MG, Ocak Ö, Şahin EM. Health-related quality of life in long COVID-19 in context of symptom type. Annals of Clinical and Analytical Medicine. 2023;14:379–83. doi:10.4328/ACAM.21508

66. Demoule A, Morawiec E, Decavele M, Ohayon R, Malrin R, Galarza-Jimenez MA, et al. Health-related quality of life of COVID-19 two and 12 months after intensive care unit admission. Ann Intensive Care. 2022;12:16.35184214 10.1186/s13613-022-00991-0PMC8858438

67. Barani S, Bhatnagar T, Natarajan M, Gayathri K, Sonekar HB, Sasidharan A, et al. Health-related quality of life among COVID-19 individuals: a cross-sectional study in Tamil Nadu, India. Clin Epidemiol Glob Health. 2022;13:100943.35018308 10.1016/j.cegh.2021.100943PMC8739503

68. Carlile O, Briggs A, Henderson AD, Butler-Cole BFC, Tazare J, Tomlinson LA, et al. Impact of long COVID on health-related quality-of-life: an opensafely population cohort study using patient-reported outcome measures (OpenPROMPT). The Lancet Regional Health. 2024;40:100908.38689605 10.1016/j.lanepe.2024.100908PMC11059448

69. Sun C, Liu Z, Li S, Wang Y, Liu G. Impact of long COVID on health-related quality of life among patients after acute COVID-19 infection: a cross-sectional study. Inquiry. 2024;61:469580241246461.38646896 10.1177/00469580241246461PMC11036910

70. Moisoglou I, Katsiroumpa A, Kolisiati A, Vraka I, Kosiara K, Siskou O, et al. Resilience and social support improve mental health and quality of life in patients with post-COVID-19 syndrome. Eur J Investig Health Psychol Educ. 2024;14:230–42.38248135 10.3390/ejihpe14010015PMC10814826

71. Iqbal A, Iqbal K, Arshad Ali S, Azim D, Farid E, Baig MD, Bin Arif T, Raza M. The COVID-19 sequelae: A Cross-Sectional evaluation of Post-recovery symptoms and the need for rehabilitation of COVID-19 survivors. Cureus. 2021;13:e13080.33680620 10.7759/cureus.13080PMC7932827

72. Roman-Montes CM, Flores-Soto Y, Guaracha-Basanez GA, Tamez-Torres KM, Sifuentes-Osornio J, Gonzalez-Lara MF, de Leon AP. Post-COVID-19 syndrome and quality of life impairment in severe COVID-19 Mexican patients. Front Public Health. 2023;11:1155951.37255755 10.3389/fpubh.2023.1155951PMC10225709

73. Rosa RG, Cavalcanti AB, Azevedo LCP, Veiga VC, de Souza D, Dos Santos R, Schardosim RFC, Rech GS, Trott G, Schneider D, et al. Association between acute disease severity and one-year quality of life among post-hospitalisation COVID-19 patients: coalition VII prospective cohort study. Intensive Care Med. 2023;49:166–77.36594987 10.1007/s00134-022-06953-1PMC9808680

74. Giurgi-Oncu C, Tudoran C, Pop GN, Bredicean C, Pescariu SA, Giurgiuca A, et al. Cardiovascular abnormalities and mental health difficulties result in a reduced quality of life in the post-acute covid-19 syndrome. Brain Sci. 2021;11(11):1456.34827455 10.3390/brainsci11111456PMC8615893

75. Soare IA, Ansari W, Nguyen JL, Mendes D, Ahmed W, Atkinson J, et al. Health-related quality of life in mild-to-moderate COVID-19 in the UK: a cross-sectional study from pre- to post-infection. Health Qual Life Outcomes. 2024;22:12.38287294 10.1186/s12955-024-02230-5PMC10826014

76. Kohlbrenner D, Kuhn M, Stüssi-Helbling M, Nordmann Y, Spielmanns M, Clarenbach CF. Longitudinal smartphone-based post-hospitalisation symptom monitoring in SARS-CoV-2 associated respiratory failure: a multi-centre observational study. Front Rehabil Sci. 2021;2:777396.36188784 10.3389/fresc.2021.777396PMC9397765

77. Visser C, Berentschot JC, de Jong CMM, Antoni ML, Bek LM, van den Berg-Emons RJG, et al. The impact of pulmonary embolism on health outcomes of COVID-19 at 3 months after hospitalization. Res Pract Thromb Haemost. 2024;8:102573.40206268 10.1016/j.rpth.2024.102573PMC11980619

78. Dodd S, Mohebbi M, O’Donohue J, Matthews G, Darley DR, Berk M. Psychiatric sequelae after SARS-Cov-2 infection: trajectory, predictors and associations in a longitudinal Australian cohort. Acta Neuropsychiatr. 2024;36:195–210.37681420 10.1017/neu.2023.45

79. Iribarren-Diarasarri S, Bermudez-Ampudia C, Barreira-Mendez R, Vallejo-Delacueva A, Bediaga-Diazdecerio I, Martinez-Alutiz S, et al. Post-intensive care syndrome one month after discharge in surviving critically ill COVID-19 patients. Medicina Intensiva (English Edition). 2023;47:493–500.10.1016/j.medine.2022.10.012PMC957918536319532

80. Umbrello M, Miori S, Sanna A, Lassola S, Baruzzo E, Penzo D, et al. High rates of impaired quality of life and social and economic problems at 6 months after COVID-19-related ARDS. J Anesth Analg Crit Care. 2022;2:20.37386529 10.1186/s44158-022-00048-5PMC9109430

81. Neelima M, Chivukula SK. Assessment of health-related quality of life and its determinants among COVID-19 intensive care unit survivors. J Fam Med Prim Care. 2023;12:3319–25.10.4103/jfmpc.jfmpc_739_23PMC1086624738361881

82. Elumalai R, Bagepally BS, Ponnaiah M, Bhatnagar T, Barani S, Kannan P, et al. Post C-st: health-related quality of life and associated factors among COVID-19 individuals managed with Indian traditional medicine: a cross-sectional study from South India. Clin Epidemiol Glob Health. 2023;20:101250.36816535 10.1016/j.cegh.2023.101250PMC9922434

83. Tarazona V, Kirouchena D, Clerc P, Pinsard-Laventure F, Bourrion B. Quality of life in COVID-19 outpatients: a long-term follow-up study. J Clin Med. 2022;11(21):6478.36362706 10.3390/jcm11216478PMC9657247

84. Kuodi P, Gorelik Y, Zayyad H, Wertheim O, Beiruti Wiegler K, Abu Jabal K, et al. Association between BNT162b2 vaccination and health-related quality of life up to 18 months post-SARS-CoV-2 infection in Israel. Sci Rep. 2023;13:15801.37737268 10.1038/s41598-023-43058-1PMC10516916

85. Egger M, Wimmer C, Stummer S, Reitelbach J, Bergmann J, Muller F, et al. Reduced health-related quality of life, fatigue, anxiety and depression affect COVID-19 patients in the long-term after chronic critical illness. Sci Rep. 2024;14:3016.38321074 10.1038/s41598-024-52908-5PMC10847136

86. van Tol LS, Haaksma ML, Cesari M, Dockery F, Everink IHJ, Francis BN, et al. Post-COVID-19 patients in geriatric rehabilitation substantially recover in daily functioning and quality of life. Age Ageing. 2024;53(5):afae084.38725361 10.1093/ageing/afae084PMC11082471

87. Naik H, Wilton J, Tran KC, Janjua NZ, Levin A, Zhang W. Long-term health-related quality of life in working-age COVID-19 survivors: a cross-sectional study. Am J Med. 2025;138:850-e861858.38795939 10.1016/j.amjmed.2024.05.016

88. Lim RK, Rosentreter R, Chen Y, Mehta R, McLeod G, Wan M, et al. Quality of life, respiratory symptoms, and health care utilization 1 year following outpatient management of COVID-19: a prospective cohort study. Sci Rep. 2022;12(1):12988.35906362 10.1038/s41598-022-17243-7PMC9334740

89. Tak C. The long-term impacts of long COVID: an examination of health-related quality of life, disability, and health status among individuals with self-reported post-acute COVID syndrome. Qual Life Res. 2022;31:S26.10.1186/s41687-023-00572-0PMC1002978536943643

90. Tsuzuki S, Miyazato Y, Terada M, Morioka S, Ohmagari N, Beutels P. Impact of long-COVID on health-related quality of life in Japanese COVID-19 patients. Health Qual Life Outcomes. 2022;20:125.35986269 10.1186/s12955-022-02033-6PMC9388960

91. Ferrarello F, Iacopino C, Pierinelli C, Paci M. Physical functioning and health-related quality of life after COVID-19: a long-term perspective case series. Int J Rehabil Res. 2023;46:77–85.36728854 10.1097/MRR.0000000000000563

92. Amedewonu EA, Aryeetey GC, Godi A, Sackeyfio J, Dai-Kosi AD. Assessment of the quality of life of COVID-19 recovered patients at the Ghana infectious disease centre. PLoS One. 2024;19:e0306118.39024249 10.1371/journal.pone.0306118PMC11257348

93. Zalaquett N, Lutchman K, Iliaki E, Buley J, Nathan N, Sotos Prieto M, et al. Findings associated with prolonged COVID-19 recovery among Boston healthcare workers. J Occup Environ Med. 2024;66:962–9.39196796 10.1097/JOM.0000000000003221

94. Wong AW, Tran KC, Binka M, Janjua NZ, Sbihi H, Russell JA, et al. Use of latent class analysis and patient reported outcome measures to identify distinct long COVID phenotypes: a longitudinal cohort study. PLoS One. 2023;18:e0286588.37267379 10.1371/journal.pone.0286588PMC10237387

95. Walker S, Goodfellow H, Pookarnjanamorakot P, Murray E, Bindman J, Blandford A, et al. Impact of fatigue as the primary determinant of functional limitations among patients with post-COVID-19 syndrome: a cross-sectional observational study. BMJ Open. 2023;13:e069217.37286327 10.1136/bmjopen-2022-069217PMC10335413

96. Macedo Junior HB, Mediano MFF, Kasal DAB. Self-reported dyspnea is associated with reduced health-related quality of life in quaternary hospital workers 1 year post mild COVID-19 infection. Healthcare. 2024;12(24):2534.39765961 10.3390/healthcare12242534PMC11675433

97. Prata TA, Leite AS, Augusto VM, Bretas DC, Andrade BH, Oliveira J, et al. Lung function and quality of life one year after severe COVID-19 in Brazil. J Bras Pneumol. 2024;50:e20230261.38808823 10.36416/1806-3756/e20230261PMC11185156

98. Ojeda A, Calvo A, Cuñat T, Mellado-Artigas R, Comino-Trinidad O, Aliaga J, et al. Characteristics and influence on quality of life of new-onset pain in critical COVID-19 survivors. Eur J Pain. 2022;26:680–94.34866276 10.1002/ejp.1897PMC9015597

99. Pacho-Hernández JC, Fernández-de-Las-Peñas C, Fuensalida-Novo S, Jiménez-Antona C, Ortega-Santiago R, Cigarán-Mendez M. Sleep quality mediates the effect of sensitization-associated symptoms, anxiety, and depression on quality of life in individuals with post-COVID-19 pain. Brain Sci. 2022;12(10):1363.36291297 10.3390/brainsci12101363PMC9599807

100. Sun X, DeShazo JP, Anatale-Tardiff L, Di Fusco M, Allen KE, Porter TM, et al. Latent class analysis of post-acute sequelae of SARS-CoV-2 infection. J Biopharm Stat. 2024;35(5):902–17.39550613 10.1080/10543406.2024.2424844

101. Ordinola Navarro A, Cervantes-Bojalil J, Cobos Quevedo OJ, Avila Martínez A, Hernández-Jiménez CA, Pérez Álvarez E, González Gil A, Peralta Amaro AL, Vera-Lastra O. Lopez Luis BA: decreased quality of life and spirometric alterations even after mild-moderate COVID-19. Respir Med. 2021;181:106391.33865161 10.1016/j.rmed.2021.106391PMC8044599

102. Tiels LM, Wintjens M, Waardenburg S, van Rosmalen F, van Kuijk SMJ, van der Horst ICC, Luiten R, van Bussel BCT, van Mook W, Hemmen B, van Santen S. More self-efficacy is associated with longitudinally higher health-related quality of life in mechanically ventilated COVID-19 ICU survivors: the prospective maastriccht cohort. Nurs Crit Care. 2025;30(4):e13241.10.1111/nicc.13241PMC1222204439805317

103. Szende A, Janssen B, Cabases J. Self-reported population health: an international perspective based on EQ-5D. Dordrecht: Springer; 2014.29787044

104. Nshimirimana DA, Kokonya D, Gitaka J, Wesonga B, Mativo JN, Rukanikigitero JMV. Impact of COVID-19 on health-related quality of life in the general population: a systematic review and meta-analysis. PLOS Glob Public Health. 2023;3:e0002137.37883383 10.1371/journal.pgph.0002137PMC10602258

105. Davis HE, McCorkell L, Vogel JM, Topol EJ. Author correction: long COVID: major findings, mechanisms and recommendations. Nat Rev Microbiol. 2023;21:408.37069455 10.1038/s41579-023-00896-0PMC10408714

106. Gulyaeva NV. Brain mechanisms involved in post COVID syndrome: a narrative review. Neurochemical J. 2024;18:397–405. doi:10.1134/S1819712424700156

107. König HH, Bernert S, Angermeyer MC, Matschinger H, Martinez M, Vilagut G, et al. Comparison of population health status in six European countries: results of a representative survey using the EQ-5D questionnaire. Med Care. 2009;47:255–61.19169128 10.1097/MLR.0b013e318184759e

108. El-Tallawy SN, Perglozzi JV, Ahmed RS, Kaki AM, Nagiub MS, LeQuang JK, et al. Pain management in the post-COVID era-an update: A narrative review. Pain Ther. 2023;12:423–48.36853484 10.1007/s40122-023-00486-1PMC9971680

109. Vargas-Schaffer G. Pharmacological proposal approach to managing chronic pain associated with COVID-19. Biomedicines. 2023;11(7):1812.37509450 10.3390/biomedicines11071812PMC10376228

110. He J, Lin J, Sun W, Cheung T, Cao Y, Fu E, Chan SHW, Tsang HWH. The effects of psychosocial and behavioral interventions on depressive and anxiety symptoms during the COVID-19 pandemic: a systematic review and meta-analysis. Sci Rep. 2023;13:19094.37925535 10.1038/s41598-023-45839-0PMC10625531

111. Nandasena H, Pathirathna ML, Atapattu A, Prasanga PTS. Quality of life of COVID 19 patients after discharge: systematic review. PLoS One. 2022;17:e0263941.35171956 10.1371/journal.pone.0263941PMC8849513

112. Betschart M, Rezek S, Unger I, Ott N, Beyer S, Böni A, et al. One year follow-up of physical performance and quality of life in patients surviving COVID-19: a prospective cohort study. Swiss Med Wkly. 2021;151:w30072.34751538 10.4414/smw.2021.w30072

113. Meys R, Delbressine JM, Goërtz YMJ, Vaes AW, Machado FVC, Van Herck M, et al. Generic and respiratory-specific quality of life in non-hospitalized patients with COVID-19. J Clin Med. 2020;9(12):3993.33317214 10.3390/jcm9123993PMC7764406

114. Fernandes J, Fontes L, Coimbra I, Paiva JA. Health-related quality of life in survivors of severe COVID-19 of a university hospital in Northern Portugal. Acta Med Port. 2021;34:601–7.34708687 10.20344/amp.16277

115. Halpin SJ, McIvor C, Whyatt G, Adams A, Harvey O, McLean L, et al. Postdischarge symptoms and rehabilitation needs in survivors of COVID-19 infection: a cross-sectional evaluation. J Med Virol. 2021;93:1013–22.32729939 10.1002/jmv.26368

116. Hodgson CL, Higgins AM, Bailey MJ, Mather AM, Beach L, Bellomo R, Bissett B, Boden IJ, Bradley S, Burrell A, et al. The impact of COVID-19 critical illness on new disability, functional outcomes and return to work at 6 months: a prospective cohort study. Crit Care. 2021;25:382.34749756 10.1186/s13054-021-03794-0PMC8575157

117. Johnsen S, Sattler SM, Miskowiak KW, Kunalan K, Victor A, Pedersen L, et al. Descriptive analysis of long COVID sequelae identified in a multidisciplinary clinic serving hospitalised and non-hospitalised patients. ERJ Open Res. 2021;7(3):00205-2021.34345629 10.1183/23120541.00205-2021PMC8091683

118. Kotwani P, Patwardhan V, Pandya A, Saha S, Patel GM, Jaiswal S, et al. Valuing out-of-pocket expenditure and health related quality of life of COVID-19 patients from Gujarat, India. J Commun Dis. 2021;53:104–9.

119. Lerum TV, Aaløkken TM, Brønstad E, Aarli B, Ikdahl E, Lund KMA, et al. Dyspnoea, lung function and CT findings 3 months after hospital admission for COVID-19. Eur Respir J. 2021;57(4):2003448.33303540 10.1183/13993003.03448-2020PMC7736755

120. Menges D, Ballouz T, Anagnostopoulos A, Aschmann HE, Domenghino A, Fehr JS, et al. Burden of post-COVID-19 syndrome and implications for healthcare service planning: a population-based cohort study. PLoS One. 2021;16(7):e0254523.34252157 10.1371/journal.pone.0254523PMC8274847

121. Monti G, Leggieri C, Fominskiy E, Scandroglio AM, Colombo S, Tozzi M, et al. Two-months quality of life of COVID-19 invasively ventilated survivors; an Italian single-center study. Acta Anaesthesiol Scand. 2021;65:912–20.33655487 10.1111/aas.13812PMC8014684

122. Och A, Tylicki P, Polewska K, Puchalska-Reglińska E, Parczewska A, Szabat K, et al. Persistent post-COVID-19 syndrome in hemodialyzed patients—a longitudinal cohort study from the North of Poland. J Clin Med. 2021;10(19):4451.34640471 10.3390/jcm10194451PMC8509624

123. Özkeskin M, Özden F, Karaman B, Ekmekçi Ö, Yüceyar N. The comparison of fatigue, sleep quality, physical activity, quality of life, and psychological status in multiple sclerosis patients with or without COVID-19. Mult Scler Relat Disord. 2021;55:103180.34352513 10.1016/j.msard.2021.103180PMC8324500

124. Rousseau AF, Minguet P, Colson C, Kellens I, Chaabane S, Delanaye P, Cavalier E, Chase JG, Lambermont B, Misset B. Post-intensive care syndrome after a critical COVID-19: cohort study from a Belgian follow-up clinic. Ann Intensive Care. 2021;11:118.34324073 10.1186/s13613-021-00910-9PMC8319705

125. Shah AS, Ryu MH, Hague CJ, Murphy DT, Johnston JC, Ryerson CJ, et al. Changes in pulmonary function and patient-reported outcomes during COVID-19 recovery: a longitudinal, prospective cohort study. ERJ Open Res. 2021;7(3):00243-2021.34522693 10.1183/23120541.00243-2021PMC8310958

126. Tessitore E, Handgraaf S, Poncet A, Achard M, Höfer S, Carballo S, et al. Symptoms and quality of life at 1-year follow up of patients discharged after an acute COVID-19 episode. Swiss Med Wkly. 2021;151:w30093.34909433 10.4414/smw.2021.w30093

127. Akova İ, Gedikli MA. Determination of ongoing symptoms, quality of life levels, and risk factors in post-COVID-19 patients. Erciyes Med J. 2022;44:208–15.

128. Attauabi M, Dahlerup JF, Poulsen A, Hansen MR, Vester-Andersen MK, Eraslan S, et al. Outcomes and long-term effects of COVID-19 in patients with inflammatory bowel diseases - a Danish prospective population-based cohort study with individual-level data. J Crohns Colitis. 2022;16:757–67.34755858 10.1093/ecco-jcc/jjab192PMC8689957

129. Cuerda C, López IS, Martínez CG, Viveros MM, Velasco C, Peñafiel VC, Jiménez MM, Gonzalo I, González-Sánchez V, Carrasco AR, et al. Covid-19 impact of COVID-19 in nutritional and functional status of survivors admitted in intensive care units during the first outbreak. Preliminary results of the NUTRICOVID study. Clin Nutr. 2022;41:2934–9.34893357 10.1016/j.clnu.2021.11.017PMC8609675

130. de Oliveira JF, de Ávila RE, de Oliveira NR, da Cunha Severino Sampaio N, Botelho M, Gonçalves FA, et al. Persistent symptoms, quality of life, and risk factors in long COVID: a cross-sectional study of hospitalized patients in Brazil. Int J Infect Dis. 2022;122:1044–51.35908724 10.1016/j.ijid.2022.07.063PMC9330427

131. Farhanah N, Budiman C, Sofro MAU, Riyanto B, Hadisaputro S, Gasem MH. The persistent symptoms and decreased quality of life of COVID-19 patients (a 3-month follow-up after discharge). Open Access Maced J Med Sci. 2022;10(B):1419–25. doi:10.3889/oamjms.2022.9755

132. Fontes L, Costa PJR, Fernandes JCJ, Vieira TS, Reis NC, Coimbra IMM, et al. The impact of severe COVID-19 on health-related quality of life and disability: an early follow-up perspective. Rev Bras Ter Intensiva. 2022;34:141–6.35766663 10.5935/0103-507X.20220008-enPMC9345590

133. Haberland E, Haberland J, Richter S, Schmid M, Hromek J, Zimmermann H, Geng S, Winterer H, Schneider S, Kollum M. Seven months after mild COVID-19: A Single-Centre controlled Follow-Up study in the district of Constance (FSC19-KN). Int J Clin Pract. 2022;2022:8373697.36035510 10.1155/2022/8373697PMC9391166

134. Han JH, Womack KN, Tenforde MW, Files DC, Gibbs KW, Shapiro NI, et al. Associations between persistent symptoms after mild COVID-19 and long-term health status, quality of life, and psychological distress. Influenza Other Respir Viruses. 2022;16:680–9.35347854 10.1111/irv.12980PMC9111447

135. Heubner L, Petrick PL, Güldner A, Bartels L, Ragaller M, Mirus M, et al. Extreme obesity is a strong predictor for in-hospital mortality and the prevalence of long-COVID in severe COVID-19 patients with acute respiratory distress syndrome. Sci Rep. 2022;12:18418.36319681 10.1038/s41598-022-22107-1PMC9626466

136. Kalyani T, Kumar BV. A study to analyze potential long-term post-COVID clinical conditions and their management in a tertiary care hospital. Int J Pharm Clin Res. 2022;14:353–60.

137. Luong T, Jang SS, Said M, DeConde AS, Yan CH. Impact of COVID-19 versus chronic rhinosinusitis/rhinitis associated olfactory dysfunction on health utility and quality of life. Laryngoscope Investig Otolaryngol. 2022;7:1299–307.36249088 10.1002/lio2.921PMC9538416

138. Martins S, Ferreira AR, Fernandes J, Vieira T, Fontes L, Coimbra I, et al. Depressive and anxiety symptoms in severe COVID-19 survivors: a prospective cohort study. Psychiatr Q. 2022;93:891–903.35947293 10.1007/s11126-022-09998-zPMC9363264

139. Moens M, Duarte RV, De Smedt A, Putman K, Callens J, Billot M, et al. Health-related quality of life in persons post-COVID-19 infection in comparison to normative controls and chronic pain patients. Front Public Health. 2022;10:991572.36339175 10.3389/fpubh.2022.991572PMC9632164

140. Morrow AJ, Sykes R, McIntosh A, Kamdar A, Bagot C, Bayes HK, Blyth KG, Briscoe M, Bulluck H, Carrick D, et al. A multisystem, cardio-renal investigation of post-COVID-19 illness. Nat Med. 2022;28:1303–13.35606551 10.1038/s41591-022-01837-9PMC9205780

141. Nakshbandi G, Moor CC, Nossent EJ, Geelhoed JJM, Baart SJ, Boerrigter BG, et al. Home monitoring of lung function, symptoms and quality of life after admission with COVID-19 infection: the HOMECOMIN’ study. Respirology. 2022;27:501–9.35441433 10.1111/resp.14262PMC9115460

142. Pan J, Zhou K, Wang J, Zheng Y, Yu D, Kang H, et al. Quality of life and mental health status in recovered COVID-19 subjects at two years after infection in Taizhou, China: a longitudinal cohort study. Brain Sci. 2022;12(7):939.35884745 10.3390/brainsci12070939PMC9316455

143. Schallner N, Lieberum J, Kalbhenn J, Bürkle H, Daumann F. Intensive care unit resources and patient-centred outcomes in severe COVID-19: a prospective single-centre economic evaluation. Anaesthesia. 2022;77:1336–45.36039476 10.1111/anae.15844PMC9538123

144. Tabacof L, Tosto-Mancuso J, Wood J, Cortes M, Kontorovich A, McCarthy D, et al. Post-acute COVID-19 syndrome negatively impacts physical function, cognitive function, health-related quality of life, and participation. Am J Phys Med Rehabil. 2022;101:48–52.34686631 10.1097/PHM.0000000000001910PMC8667685

145. Vejen M, Hansen EF, Al-Jarah BNI, Jensen C, Thaning P, Jeschke KN, et al. Hospital admission for COVID-19 pneumonitis - long-term impairment in quality of life and lung function. Eur Clin Respir J. 2022;9:2024735.35024101 10.1080/20018525.2021.2024735PMC8745367

146. Weihe S, Mortensen CB, Haase N, Andersen LPK, Mohr T, Siegel H, et al. Long-term cognitive and functional status in Danish ICU patients with COVID-19. Acta Anaesthesiol Scand. 2022;66:978–86.35748019 10.1111/aas.14108PMC9350352

147. Wimmer C, Egger M, Bergmann J, Huge V, Müller F, Jahn K. Critical COVID-19 disease: clinical course and rehabilitation of neurological deficits. Front Neurol. 2022;13:1012685.36388208 10.3389/fneur.2022.1012685PMC9649895

148. Wu D, Ding H, Lin J, Xiao M, Xie J, Xie F, et al. Fighting COVID-19: a qualitative study into the lives of intensive care unit survivors in Wuhan, China. BMJ Open. 2022;12:e055365.35351715 10.1136/bmjopen-2021-055365PMC8960460

149. Fietsam AC, Bryant AD, Rudroff T. Fatigue and perceived fatigability, not objective fatigability, are prevalent in people with post-COVID-19. Exp Brain Res. 2023;241:211–9.36462035 10.1007/s00221-022-06518-0PMC9735153

150. Rousseau AF, Colson C, Minguet P, Kellens I, Collard M, Vancraybex C, et al. Characteristics of mid-term post-intensive care syndrome in patients attending a follow-up clinic: a prospective comparison between COVID-19 and non-COVID-19 survivors. Crit Care Explor. 2023;5:e0850.36699242 10.1097/CCE.0000000000000850PMC9851681

151. Sanchez-Garcia AM, Martinez-Lopez P, Gomez-Gonzalez AM, Rodriguez-Capitan J, Pavon-Moron FJ, Jimenez-Lopez RJ, Garcia-Almeida JM, Avanesi-Molina E, Zamboschi N, Rueda-Molina C, et al. Post-Intensive care unit multidisciplinary approach in patients with severe bilateral SARS-CoV-2 pneumonia. Int J Med Sci. 2023;20:1–10.36619225 10.7150/ijms.77792PMC9812800

152. Zupanc A, Vidmar G, Majdic N, Novak P. Health-related quality-of-life during rehabilitation in patients with critical illness neuropathy/myopathy after severe coronavirus disease 2019. Int J Rehabil Res. 2023;46:53–60.36728893 10.1097/MRR.0000000000000558

153. Cavalleri J, Treguier D, Deliège T, Gurdebeke C, Ernst M, Lambermont B, et al. One-year functional decline in COVID-19 and non-COVID-19 critically ill survivors: a prospective study incorporating a pre-ICU status assessment. Healthcare. 2022. 10.3390/healthcare10102023.36292470 10.3390/healthcare10102023PMC9602164

154. Carenzo L, Protti A, Dalla Corte F, Aceto R, Iapichino G, Milani A, et al. Short-term health-related quality of life, physical function and psychological consequences of severe COVID-19. Ann Intensive Care. 2021;11:91.34089104 10.1186/s13613-021-00881-xPMC8177269

155. Morelli N, Parry SM, Steele A, Lusby M, Montgomery-Yates AA, Morris PE, et al. Patients surviving critical COVID-19 have impairments in dual-task performance related to post-intensive care syndrome. J Intensive Care Med. 2022;37:890–8.35072548 10.1177/08850666221075568PMC9160440

156. Sawano M, Wu Y, Shah RM, Zhou T, Arun AS, Khosla P, Kaleem S, Vashist A, Bhattacharjee B, Ding Q, et al. Long COVID characteristics and experience: A descriptive study from the Yale LISTEN research cohort. Am J Med. 2025;138:712–e720713.38663793 10.1016/j.amjmed.2024.04.015

157. Scott ES, Lubetkin EI, Janssen MF, Yfantopolous J, Bonsel GJ, Haagsma JA. Cross-sectional and longitudinal comparison of health-related quality of life and mental well-being between persons with and without post COVID-19 condition. Front Epidemiol. 2023;3:1144162.38455931 10.3389/fepid.2023.1144162PMC10910898

158. Khoja O, Silva-Passadouro B, Cristescu E, McEwan K, Doherty D, O’Connell F, et al. Clinical characterization of new-onset chronic musculoskeletal pain in long COVID: a cross-sectional study. J Pain Res. 2024;17:2531–50.39100135 10.2147/JPR.S466294PMC11298172

159. Cataldo SA, Micciulli A, Margulis L, Cibeyra M, Defeo S, Horovitz SG, Martino A, Melano R, Mena M, Parisi F, et al. Cognitive impact and brain structural changes in long COVID patients: a cross-sectional MRI study two years post infection in a cohort from Argentina. BMC Neurol. 2024;24:450.39558250 10.1186/s12883-024-03959-8PMC11572126

160. Wemhoner L, Brandts C, Dinse H, Skoda EM, Jansen S, Teufel M, et al. Consequences of COVID-19 for geriatric patients during a pandemic. Sci Rep. 2025;15:3136.39856128 10.1038/s41598-024-84379-zPMC11759943

161. Engel L, Strassmann S, Merten M, Schaefer S, Farber J, Windisch W, et al. Surviving critical care: a follow-up study assessing pulmonary function, cardiopulmonary exercise testing, and quality of life in COVID-19-affected patients. Respiration. 2025;104:15–25.39154632 10.1159/000540598

162. Malesevic S, Sievi NA, Baumgartner P, Roser K, Sommer G, Schmidt D, Vallelian F, Jelcic I, Clarenbach CF, Kohler M. Impaired health-related quality of life in long-COVID syndrome after mild to moderate COVID-19. Sci Rep. 2023;13:7717.37173355 10.1038/s41598-023-34678-8PMC10175927

163. Ding N, Zhou H, Chen C, Chen H, Shi Y. Comparison of the measurement properties of EQ-5D-5L and SF-6Dv2 in COVID-19 patients in China. Appl Health Econ Health Policy. 2024;22:555–68.38641755 10.1007/s40258-024-00881-5

164. Crescioli E, Nielsen FM, Bunzel AM, Eriksen ASB, Siegemund M, Poulsen LM, Andreasen AS, Bestle MH, Iversen SA, Brochner AC, et al. Long-term mortality and health-related quality of life with lower versus higher oxygenation targets in intensive care unit patients with COVID-19 and severe hypoxaemia. Intensive Care Med. 2024;50:1603–13.39235624 10.1007/s00134-024-07613-2PMC11446942

165. Leavy OC, Russell RJ, Harrison EM, Lone NI, Kerr S, Docherty AB, et al. 1-year health outcomes associated with systemic corticosteroids for COVID-19: a longitudinal cohort study. ERJ Open Res. 2024;10(5):00474-2024.39351379 10.1183/23120541.00474-2024PMC11440406

166. Zhao X, Chen L, Huo L, Wang M, Gao Z, Jiang H, et al. Prevalence and risk factors of long COVID among maintenance hemodialysis patients post SARS-CoV-2 infection: a one-year follow-up study in China. J Med Virol. 2024;96:e29932.39300811 10.1002/jmv.29932

167. Colleran R, Rai H, Fitzgerald S, McGovern L, Byrne RJ, Cradock A, Lavery R, Bisset J, McKeogh S, Cantwell G et al. Symptom burden, coagulopathy and heart disease, and quality of life at baseline and after 1-year follow-up following acute SARS-CoV-2 infection in a community medicine setting. Eur Heart J. 2023;44:ehad655.2615.

168. Appel KS, Nurnberger C, Bahmer T, Forster C, Polidori MC, Kohls M, et al. Definition of the Post-COVID syndrome using a symptom-based Post-COVID score in a prospective, multi-center, cross-sectoral cohort of the German National pandemic cohort network (NAPKON). Infection. 2024;52:1813–29.38587752 10.1007/s15010-024-02226-9PMC11499320

169. Deesomchok A, Liwsrisakun C, Chaiwong W, Pothirat C, Duangjit P, Bumroongkit C, et al. Long-term impacts of COVID-19 pneumonia on quality of life: a single institutional pilot study. Healthcare. 2023;11(13):1963.37444797 10.3390/healthcare11131963PMC10341595

170. Kato H, Ichihara N, Saito H, Fujitani S, Ota K, Takahashi Y, et al. Prevalence of erectile dysfunction as long-COVID symptom in hospitalized Japanese patients. Sci Rep. 2025;15:6279.39979349 10.1038/s41598-025-88904-6PMC11842839

171. Gorsler A, Franke C, Quitschau A, Kulzow N. Cognitive recovery of post critical care patients with and without COVID-19: differences and similarities, an observational study. Neurol Res Pract. 2024;6:50.39438985 10.1186/s42466-024-00349-wPMC11495021

172. Rover MM, Scolari FL, Trott G, da Silva MMD, de Souza D, da, Rosa Minho Dos, Santos R, De Carli Schardosim RF, de Souza Roldao E, Pozza Estivalete G, Rech GS et al. Association between vaccination and persistent COVID-19-related symptoms among patients with mild Omicron infection: a prospective cohort study. Vaccine X 2024;21:100579.10.1016/j.jvacx.2024.100579PMC1158242839582794

173. Janols H, Wadsten C, Forssell C, Raffeti E, Janson C, Zhou X, et al. Enhancing EQ-5D-5L sensitivity in capturing the most common symptoms in post-COVID-19 patients: an exploratory cross-sectional study with a focus on fatigue, memory/concentration problems and dyspnea dimensions. Int J Environ Res Public Health. 2024;21(5):591.38791805 10.3390/ijerph21050591PMC11121728

174. Guaraldi G, Milic J, Barbieri S, Marchio T, Caselgrandi A, Motta F, et al. Quality of life and intrinsic capacity in patients with post-acute COVID-19 syndrome is in relation to frailty and resilience phenotypes. Sci Rep. 2023;13:8956.37268716 10.1038/s41598-023-29408-zPMC10235830

175. Kwon J, Milne R, Rayner C, Rocha Lawrence R, Mullard J, Mir G, Delaney B, Sivan M, Petrou S. Impact of long COVID on productivity and informal caregiving. Eur J Health Econ. 2024;25:1095–115.38146040 10.1007/s10198-023-01653-zPMC11377524

176. Smith P, De Pauw R, Van Cauteren D, Demarest S, Drieskens S, Cornelissen L, Devleesschauwer B, De Ridder K, Charafeddine R. Post COVID-19 condition and health-related quality of life: a longitudinal cohort study in the Belgian adult population. BMC Public Health. 2023;23:1433.37495947 10.1186/s12889-023-16336-wPMC10373376

177. Tak CR. The health impact of long COVID: a cross-sectional examination of health-related quality of life, disability, and health status among individuals with self-reported post-acute sequelae of SARS CoV-2 infection at various points of recovery. J Patient Rep Outcomes. 2023;7:31.36943643 10.1186/s41687-023-00572-0PMC10029785

178. Qorolli M, Beqaj S, Ibrahimi-Kacuri D, Murtezani A, Krasniqi V, Macak Hadziomerovic A. Functional status and quality of life in post-COVID-19 patients two to three weeks after hospitalization: a cross-sectional study. Health Sci Rep. 2023;6:e1510.37621387 10.1002/hsr2.1510PMC10444983

179. Hansen KS, Jorgensen SE, Skouboe MK, Agergaard J, Schiottz-Christensen B, Vibholm LK, et al. Examination of autoantibodies to type I interferon in patients suffering from long COVID. J Med Virol. 2023;95:e29089.37698062 10.1002/jmv.29089

180. Elneima O, Hurst JR, Echevarria C, Quint JK, Walker S, Siddiqui S, et al. Long-term impact of COVID-19 hospitalisation among individuals with pre-existing airway diseases in the UK: a multicentre, longitudinal cohort study - PHOSP-COVID. ERJ Open Res. 2024;10(4):00982-2023.39010888 10.1183/23120541.00982-2023PMC11247371

181. Sun X, Fusco Di M, Puzniak L, Coetzer H, Zamparo JM, Tabak YP, et al. Assessment of retrospective collection of EQ-5D-5L in a US COVID-19 population. Health Qual Life Outcomes. 2023;21:103.37679771 10.1186/s12955-023-02187-xPMC10486034

182. Fernandez-de-Las-Penas C, Paras-Bravo P, Ferrer-Pargada D, Cancela-Cilleruelo I, Rodriguez-Jimenez J, Nijs J, et al. Sensitization symptoms are associated with psychological and cognitive variables in COVID-19 survivors exhibiting post-COVID pain. Pain Pract. 2023;23:23–31.35757896 10.1111/papr.13146PMC9350126

183. Mercier K, Piche J, Rioux-Perreault C, Lemaire-Paquette S, Piche A. A longitudinal prospective cohort study of health-related quality of life assessment in outpatient adults with post-COVID-19 conditions. J Assoc Med Microbiol Infect Dis Can. 2024;8:309–18.38250617 10.3138/jammi-2023-0010PMC10797766

184. Tsuruoka M, Huynh MK, Toizumi M, Hoang TT, Nguyen TB, Dao AT, et al. Characteristics and long-term health outcomes of the first domestic COVID-19 outbreak cases in Da Nang, Vietnam: a longitudinal cohort study. Trop Med Health. 2025;53:6.39810272 10.1186/s41182-024-00670-9PMC11731347

185. van Tol LS, Lin T, Caljouw MAA, Cesari M, Dockery F, Everink IHJ, Francis BN, Gordon AL, Grund S, Matchekhina L, et al. Post-COVID-19 recovery and geriatric rehabilitation care: a European inter-country comparative study. Eur Geriatr Med. 2024;15:1489–501.39136862 10.1007/s41999-024-01030-wPMC11614975

186. Carrera M, Gonzalez A, Peralta BL, Diaz Ballve LP. Evolution of quality of life, functional capacity, nutritional status, and return to work in patients admitted with severe COVID-19 pneumonia requiring invasive mechanical ventilation: a one-year follow-up study post-intensive care discharge. Cureus. 2025;17:e77706.39981451 10.7759/cureus.77706PMC11841964

187. Di Fusco M, Sun X, Moran MM, Coetzer H, Zamparo JM, Alvarez MB, et al. Impact of COVID-19 and effects of booster vaccination with BNT162b2 on six-month long COVID symptoms, quality of life, work productivity and activity impairment during Omicron. J Patient Rep Outcomes. 2023;7:77.37486567 10.1186/s41687-023-00616-5PMC10366033

188. Godfrey B, Shardha J, Witton S, Bodey R, Tarrant R, Greenwood DC, et al. A personalised pacing and active rest rehabilitation programme for post-exertional symptom exacerbation and health status in long COVID (PACELOC): a prospective cohort study. J Clin Med. 2024;14(1):97.39797180 10.3390/jcm14010097PMC11722468

189. Lomholt-Welch H, Morrow AJ, Sykes R, Saleh M, Zahra B, MacIntosh A, et al. Mental health symptoms and illness trajectory following COVID-19 hospitalization: a cohort study. Heart and Mind. 2023;7:235–45. doi:10.4103/hm.HM-D-23-00037

190. Atchison CJ, Davies B, Cooper E, Lound A, Whitaker M, Hampshire A, et al. Long-term health impacts of COVID-19 among 242,712 adults in England. Nat Commun. 2023;14:6588.37875536 10.1038/s41467-023-41879-2PMC10598213

191. Duwel V, de Kort JML, Becker CM, Kock SM, Tromp GG, Busari JO. A cross-sectional study of the physical and mental well-being of long COVID patients in Aruba. Clin Med Res. 2023;21:69–78.37407214 10.3121/cmr.2023.1821PMC10321723

192. Pietruszka-Waleka E, Rzad M, Rozynska R, Miklusz P, Zieniuk-Lesiak E, Zabicka M, Jahnz-Rozyk K. Quality of life in follow-up up to 9 months after COVID-19 hospitalization among the polish population-a prospective single center study. Biomedicines 2024;12:1282.10.3390/biomedicines12061282PMC1120101438927489

193. Samuelsson CM, Hussain N, Drummond A, Persson CU. Health-related quality of life one year after intensive care unit admission for COVID-19: a retrospective, cross-sectional, longitudinal observational study. Health Sci Rep. 2025;8:e70507.40008224 10.1002/hsr2.70507PMC11850194

194. Seeley MC, Gallagher C, Ong E, Langdon A, Chieng J, Bailey D, et al. High incidence of autonomic dysfunction and postural orthostatic tachycardia syndrome in patients with long COVID: implications for management and health care planning. Am J Med. 2025;138:354-e361351.37391116 10.1016/j.amjmed.2023.06.010PMC10307671

195. Agergaard J, Gunst JD, Schiottz-Christensen B, Ostergaard L, Wejse C. Long-term prognosis at 1.5 years after infection with wild-type strain of SARS-CoV-2 and alpha, delta, as well as omicron variants. Int J Infect Dis. 2023;137:126–33.37907167 10.1016/j.ijid.2023.10.022

196. D’Souza AN, Merrett M, Griffin H, Tran-Duy A, Struck C, Fazio TN, et al. Recovering from COVID-19 (ReCOV): feasibility of an allied-health-led multidisciplinary outpatient rehabilitation service for people with long COVID. Int J Environ Res Public Health. 2024;21(7):958.39063534 10.3390/ijerph21070958PMC11277266

197. Carenzo L, Zini L, Mercalli C, Stomeo N, Milani A, Amato K, et al. Health related quality of life, physical function, and cognitive performance in mechanically ventilated COVID-19 patients: a long term follow-up study. J Crit Care. 2024;82:154773.38479299 10.1016/j.jcrc.2024.154773

198. McCarthy A, Robinson K, Dockery F, McLoughlin K, O’Connor M, Milos A, Corey G, Carey L, Steed F, Haaksma M, et al. Long-Term outcomes of older adults in Ireland after geriatric rehabilitation for COVID-19: A prospective cohort study. Age Ageing. 2024;53:iv24–5.10.1007/s11845-024-03723-4PMC1145006938856964. doi:10.1093/ageing/afae178.097

199. Malesevic S, Sievi NA, Schmidt D, Vallelian F, Jelcic I, Kohler M, et al. Physical health-related quality of life improves over time in post-COVID-19 patients: an exploratory prospective study. J Clin Med. 2023;12(12):4077.37373770 10.3390/jcm12124077PMC10298963

200. Dennis A, Cuthbertson DJ, Wootton D, Crooks M, Gabbay M, Eichert N, Mouchti S, Pansini M, Roca-Fernandez A, Thomaides-Brears H, et al. Multi-organ impairment and long COVID: a 1-year prospective, longitudinal cohort study. J R Soc Med. 2023;116:97–112.36787802 10.1177/01410768231154703PMC10041626

201. Cannata F, Pinto G, Chiarito M, Maurina M, Condello F, Bombace S, et al. Long-term prognostic impact of subclinical myocardial dysfunction in patients recovered from COVID-19. Echocardiography. 2023;40:464–74.37100745 10.1111/echo.15575

202. Wang J, Goodfellow H, Walker S, Blandford A, Pfeffer P, Hurst JR, et al. Trajectories of functional limitations, health-related quality of life and societal costs in individuals with long COVID: a population-based longitudinal cohort study. BMJ Open. 2024;14:e088538.39537389 10.1136/bmjopen-2024-088538PMC11574431

203. Wangnamthip S, Zinboonyahgoon N, Rushatamukayanunt P, Papaisarn P, Pajina B, Jitsinthunun T, Promsin P, Sirijatuphat R, Fernandez-de-Las-Penas C, Arendt-Nielsen L, de Andrade DC. The incidence, characteristics, impact and risk factors of post-COVID chronic pain in thailand: A single-center cross-sectional study. PLoS ONE. 2024;19:e0296700.38215071 10.1371/journal.pone.0296700PMC10786369

204. Sinaga JP, Sinaga BY, Siagian P, Eyanoer PC, Unata IM. Factors associated with the quality of life and persistent dyspnea severity in COVID-19 survivors: a cross-sectional study among healthcare workers. Narra J. 2023;3:e419.38455626 10.52225/narra.v3i3.419PMC10919434

205. Tabacof L, Wood J, Breyman E, Tosto-Mancuso J, Kelly A, Wilkey K, et al. Dysautonomia, but not cardiac dysfunction, is common in a cohort of individuals with long COVID. J Pers Med. 2023;13(11):1606.38003921 10.3390/jpm13111606PMC10671897

206. Thanh HN, Minh DC, Thu HH, Quang DN. Symptoms, mental health, and quality of life among patients after COVID-19 infection: a cross-sectional study in Vietnam. J Prev Med Public Health. 2024;57:128–37.38419549 10.3961/jpmph.23.511PMC10999303

207. Cijs B, Valkenet K, Heijnen G, Visser-Meily JMA, van der Schaaf M. Patients with and without COVID-19 in the intensive care unit: physical status outcome comparisons 3 months after discharge. Phys Ther. 2023;103:pzad039.37079487 10.1093/ptj/pzad039PMC10492575

208. Domazet Bugarin J, Saric L, Delic N, Dosenovic S, Ilic D, Saric I, et al. Health-related quality of life of COVID-19 survivors treated in intensive care unit-prospective observational study. J Intensive Care Med. 2023;38:710–6.36803217 10.1177/08850666231158547PMC9944436

209. Cazares-Lara JO, Ordinola-Navarro A, Carmona-Aguilera Z, Benitez-Altamirano GM, Beltran-Ontiveros LD, Ramirez-Hinojosa JP, et al. Main predictors of decreasing in quality of life in patients with post-COVID-19: a cross-sectional study. Value Health Reg Issues. 2025;45:101039.39255548 10.1016/j.vhri.2024.101039

210. Pavithra A, Sofia HN, Kumari HVM, Lakshmikantham T, Meenakumari R. A cross-sectional study on quality of life and the functional status in post covid-19 patients. Int J Ayurvedic Med. 2023;14:959–62.

211. Honda H, Takamatsu A, Miwa T, Tabuchi T, Taniguchi K, Shibuya K, et al. Prolonged symptoms after COVID-19 in Japan: a nationwide survey of the symptoms and their impact on patients’ quality of life. Am J Med. 2025;138:98-e107104.37236416 10.1016/j.amjmed.2023.04.040PMC10208656

212. Gharibzadeh S, Routen A, Razieh C, Zaccardi F, Lawson C, Gillies C, Heller S, Davies M, Atkins H, Bain SC, et al. Long term health outcomes in people with diabetes 12 months after hospitalisation with COVID-19 in the UK: a prospective cohort study. EClinicalMedicine. 2025;79:103005.39834716 10.1016/j.eclinm.2024.103005PMC11743801

213. Berentschot JC, Martine Bek L, Heijenbrok-Kal MH, van den Berg-Emons RJG, Ribbers GM, Aerts J, Hellemons ME. Group C-FC: acute COVID-19 treatment is not associated with health problems 2 years after hospitalization. Int J Infect Dis. 2024;142:106966.38367953 10.1016/j.ijid.2024.02.009

214. Alvarez-Hernandez J, Matia-Martin P, Cancer-Minchot E, Cuerda C, Nsgo SENDIMAD. Long-term outcomes in critically ill patients who survived COVID-19: the NUTRICOVID observational cohort study. Clin Nutr. 2023;42:2029–35.37659250 10.1016/j.clnu.2023.08.008

215. Alanazi MQ, Abdelgawwad W, Almangour TA, Mostafa F, Almuheed M. Impact of COVID-19 on the health-related quality of life of patients during infection and after recovery in Saudi Arabia. Int J Environ Res Public Health. 2023;20(6):5026.36981935 10.3390/ijerph20065026PMC10049034

216. Rosa Ramos JG, Laporte LR, Ribeiro de Souza F, Neto M, Ferreira F, Amorim YDS, Freire de Andrade L. Characteristics associated with Long-Term outcomes in severe COVID-19 patients after a Post-Acute care hospitalization: A prospective cohort study. J Am Med Dir Assoc. 2024;25:105220.39155045 10.1016/j.jamda.2024.105220

217. Gursoy E, Eren S. The burden of Post-COVID-19 syndrome: A Cross-Sectional study of symptoms and quality of life in a Turkish sample. Eurasian J Family Med. 2023;12:159–66. doi:10.33880/ejfm.2023120307

218. Wang R, Jia Y, Sun T, Ruan B, Zhou H, Yu L, et al. Does physical activity affect clinical symptoms and the quality of life of mild-infected individuals with COVID-19 in China? A cross-sectional study. Healthcare. 2023;11(15):2163.37570403 10.3390/healthcare11152163PMC10418943

219. DemİRhan E, Atar S, Er G, Okutan İ, Kuru Ö. Postdischarge pain, fatigue severity and quality of life in COVID-19 survivors. Eur Res J. 2023;9:57–65. doi:10.18621/eurj.1034610

220. Rahimi F, Saadat M, Hessam M, Ravanbakhsh M, Monjezi S. Post-COVID-19 physical and cognitive impairments and associations with quality of life: a cross-sectional study. Front Sports Act Living. 2024;6:1246585.38504691 10.3389/fspor.2024.1246585PMC10948450

221. Holland AE, Fineberg D, Marceau T, Chong M, Beaman J, Wilson L, Buchanan JA, Uren J, Dal Corso S, Lannin NA, et al. The Alfred health post-COVID-19 service, melbourne, 2020–2022: an observational cohort study. Med J Aust. 2024;220:91–6.38130117 10.5694/mja2.52192

222. Bodey R, Grimaldi J, Tait H, Godfrey B, Witton S, Shardha J, et al. How long is long COVID? Evaluation of long-term health status in individuals discharged from a specialist community long COVID service. J Clin Med. 2024;13(19):5817.39407877 10.3390/jcm13195817PMC11477015

223. Kho SS, Lim KC, Muhammad NA, Nasaruddin MZ, Ismail I, Daut UM, et al. Clinical and radiological outcomes of SARS-CoV-2 related organising pneumonia in COVID-19 survivors. Med J Malaysia. 2023;78:131–8.36988520

224. Yalcin-Colak N, Kader C, Eren-Gok S, Erbay A. Long-term symptoms and quality of life in persons with COVID-19. Infect Dis Clin Microbiol. 2023;5:212–20.38633559 10.36519/idcm.2023.248PMC10985820

---
project_id: "429-RA"
work_id: "doi:10.1007/s11136-026-04223-x"
doi: "10.1007/s11136-026-04223-x"
pmid: "41920472"
pmcid: "PMC13043590"
title: "From QI-disability to QID-12: creating a brief proxy-report measure of quality of life for children with intellectual disability"
journal: "Quality of Life Research"
publication_date: "2026-04-01"
volume: "35"
issue: "5"
authors:
  - name: "Melissa K Licari"
    affiliation_ids:
      - "Aff1"
  - name: "Andrew JO Whitehouse"
    affiliation_ids:
      - "Aff1"
  - name: "Natasha N Ludwig"
    affiliation_ids:
      - "Aff2"
  - name: "Mary Wojnaroski"
    affiliation_ids:
      - "Aff3"
  - name: "Rebecca Hommer"
    affiliation_ids:
      - "Aff4"
  - name: "Gabrielle Conecker"
    affiliation_ids:
      - "Aff5"
  - name: "JayEtta Hecker"
    affiliation_ids:
      - "Aff5"
  - name: "Kelly Muzyczka"
    affiliation_ids:
      - "Aff5"
  - name: "Helen Leonard"
    affiliation_ids:
      - "Aff1"
  - name: "Katrina J Williams"
    affiliation_ids:
      - "Aff6"
      - "Aff7"
  - name: "Dinah S Reddihough"
    affiliation_ids:
      - "Aff8"
      - "Aff9"
  - name: "Jenny Downs"
    affiliation_ids:
      - "Aff1"
      - "Aff10"
  - name: "Peter Jacoby"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "The Kids Research Institute Australia, Centre for Child Health Research, The University of Western Australia, PO Box 855, West Perth, Perth, WA 6872 Australia"
  - id: "Aff2"
    name: "Kennedy Krieger Institute, Center for Neuropsychological and Psychological Assessment/Psychiatry and Behavioral Sciences, Johns Hopkins School of Medicine, Baltimore, MD USA"
  - id: "Aff3"
    name: "Department of Psychology/Psychiatry and Behavioral Health, Nationwide Children’s Hospital, Ohio State University, Columbus, OH USA"
  - id: "Aff4"
    name: "Maryland & DC DeafBlind Project, Connections Beyond Sight and Sound, College Park, MD USA"
  - id: "Aff5"
    name: "The Inchstone Project, Decoding Developmental Epilepsies, Washington, DC USA"
  - id: "Aff6"
    name: "Clinical Sciences, Monash University, Melbourne, Australia"
  - id: "Aff7"
    name: "Department of Paediatrics, Monash Children’s Hospital, Melbourne, Australia"
  - id: "Aff8"
    name: "Neurodisability and Rehabilitation, Murdoch Children’s Research Institute, Melbourne, Australia"
  - id: "Aff9"
    name: "Department of Paediatrics, The University of Melbourne, Melbourne, Australia"
  - id: "Aff10"
    name: "Curtin School of Allied Health, Curtin University, Perth, Australia"
licence: "cc by"
source_file: "input/projects/429-RA/papers/doi_10.1007_s11136-026-04223-x.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13043590/fullTextXML"
source_method: "epmc_xml"
source_sha256: "65ae57046de369fa94d69b7ba772e367a6e666ecf03b434067c7afe07f579194"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# From QI-disability to QID-12: creating a brief proxy-report measure of quality of life for children with intellectual disability

## Abstract

### Purpose

Quality of Life Disability (QI-Disability) is a 32-item parent-report measure assessing quality of life (QOL) in children with intellectual disability across domains of physical health, positive emotions, negative emotions, social interactions, leisure and outdoors, and independence. This study aimed to develop and validate a short form for use in clinical and research settings.

### Methods

Caregivers of 1,699 children with intellectual disability aged 3–18 years and representing mild to profound functional impairments, completed the QI-Disability measure as part of different studies. A Genetic Algorithm (GA) was applied to select a reduced item set. The short form was evaluated against the original scale using correlational, reliability, and Rasch analyses.

### Results

The GA-derived 12-item set (QID-12) represented each of the six QOL domains. Correlation between QID-12 and QI-Disability total scores was high (*r* = 0.97). Internal consistency of QID-12 was acceptable (α = 0.85). Rasch analysis demonstrated good fit of all items to the partial credit model, person separation reliability was 0.84, and there was no evidence of multidimensionality (*p* \> 0.99). Item targeting was appropriate across the ability spectrum. Disordered category thresholds were observed for three items, but overall psychometric performance remained satisfactory.

### Conclusion

QID-12 provides a valid and reliable short form of the QI-Disability. It retains coverage of the key domains of child QOL while substantially reducing respondent burden, supporting its use in both clinical practice and population research.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-026-04223-x.

**Keywords:** Quality of life, Intellectual disability, Children, Measurement, Short-form

Received 2025 Dec 15; Accepted 2026 Mar 5; Issue date 2026.

## Introduction

Quality of life (QOL) is a multidimensional construct that reflects an individual’s overall wellbeing within the context of culture, personal values and goals \[1\]. In children, QOL typically encompasses physical health, emotional wellbeing, and social connectedness, as well as aspects of personal development and activity. Valid QOL measures enable understanding of lived experience and guidance for clinical care, and inform clinical monitoring, benchmarking, and evaluation of interventions, supports, and services. For example, measures of QOL are increasingly important in therapeutic trials for neurodevelopmental and rare genetic disorders, where QOL outcomes complement biomedical measures \[2, 3\]. Given the unique challenges for self-report faced by many children with intellectual disability, especially for those with more severe to profound intellectual disability, caregiver-proxy reports can provide important observations to capture QOL across multiple life domains \[4\].

Developed from extensive qualitative data collected from parents of children with an intellectual disability, the Quality of Life Inventory – Disability (QI-Disability) \[5\] is a validated 32-item measure of parent-reported child QOL. The scale captures six domains: physical health, positive emotions, negative emotions, social interaction, leisure and outdoors, and independence. There is evidence for its reliability and validity across a number of etiologies of intellectual disability and associated conditions including CDKL5 deficiency disorder, Down syndrome, Rett syndrome, cerebral palsy and autism spectrum disorder \[6–8\]. While used extensively in research studies, e.g., \[9, 10\] the 32-item length may be considered time consuming for some respondents, particularly in settings where time is limited or multiple questionnaires are administered. Developing an abbreviated version of the questionnaire without sacrificing psychometric robustness has the potential to reduce respondent burden for some clinical or population research contexts.

Traditional scale reduction methods are grounded in Classical Test Theory (CTT) or Item Response Theory (IRT) \[11\]. CTT-based methods typically retain items with the highest factor loadings or those that most influence internal consistency (Cronbach’s alpha), while IRT approaches select items with high information value or broad coverage of difficulty levels \[11\]. Both approaches may prioritise internal consistency at the expense of conceptual breadth.

In recent years, optimisation algorithms inspired by natural processes have been applied to short form development. These include Ant Colony Optimisation (ACO) \[12\] and Genetic Algorithms (GA) \[13\]. The GA technique simulates natural evolution by randomly generating different short versions of a scale, including different sets of items. These sets of items are evaluated according to a specified criterion. The sets of items that are most “fit” are retained, then randomly altered into slightly different sets (akin to natural “mutations” of an organism), and then again evaluated. The process continues until the algorithm converges to a solution that, according to the specified fitness criterion, appears to be optimal and further alterations of the item sets lead to no improvement. In this context, the fitness function aims to maximise the variance in the long form scores explained by a linear combination of items while penalising the number of items used. Although this method may still favour items with high item-total correlation, it typically avoids selecting pairs of highly correlated – and therefore homogeneous or even redundant – items \[14\].

While CTT methods lead to short measures with high internal consistency, the GA method is more capable of preserving the conceptual breadth of the construct being measured with retained items more heterogeneous in their content \[14\]. Both ACO and GA have been shown to outperform CTT methods in generating efficient and psychometrically sound short versions when considering unidimensionality, reliability, sensitivity and validity \[15\]. The GA algorithm has been successfully applied in the abbreviation of scales including the Psychopathic Personality Inventory – Revised \[16\] and the Challenge of Living with Cystic Fibrosis scale \[17\].

The aim of this study was to develop and validate a short form of QI-Disability using a GA approach in a large sample of children with intellectual disability. We hypothesised that the short form would demonstrate comparable psychometric properties to the full version of QI-Disability while offering a brief, efficient tool for use in some clinical practice and research contexts.

## Methods

### Sources of data

Completed QI-Disability datasets were drawn from datasets collected between 2016 and 2023. These datasets included children aged three to 18 years with mild to profound intellectual disability and associated conditions. To avoid duplicates across datasets (i.e., cases present across more than one dataset), all cases were checked and any duplicates excluded. The sample sources included:

1.  The Kids Research Institute Australia datasets:

    1.  *QI-Disability dataset evaluating the determinants of QOL*: The initial validation of QI-Disability involved primary caregivers of 5-to-18-year-old children with intellectual disability and evidence for satisfactory goodness of fit, known-group validity and demonstrated test-retest reliability \[5, 18, 19\]. Following initial validation, a follow-up study of 435 5-to-18-year-old children with intellectual disability across four diagnostic groups (Rett syndrome with a pathogenic variant on the *MECP2* gene \[20\], Down syndrome, cerebral palsy and intellectual disability, or autism spectrum disorder and intellectual disability) identified dependency in managing personal needs, eye contact and participation in the community were predictors of QOL \[21\]. In this dataset, approximately half of children with Down syndrome (52%) or autism and intellectual disability (53%) spoke well and were easily understood and very few were diagnosed with epilepsy whereas the majority with Rett syndrome (98%) or cerebral palsy and intellectual disability (6%) had difficulty with speech or did not use speech for communication and had received a diagnosis of epilepsy \[5\]. Complete QOL datasets (*n* = 418) from this study were included in the current study.

    2.  *CDKL5 dataset*: A questionnaire including questions on comorbidities, functional abilities and QI-Disability was completed in 2018 by parents of 129 children aged 3 to 29 years who were registered with the International CDKL5 Disorder Database \[22\] and had a pathogenic variant on *CDKL5* \[2\]. Nearly 20% used sign or spoken language, nearly a quarter were fully enterally fed, nearly two thirds had daily seizures and 70% were taking two or more antiseizure medications \[22\]. Predictors of poorer QOL included lack of ability to sit, use hands and communicate, and taking three or more anti-epileptic medications \[22\]. Seventy-six children aged 3 to 18 years from this dataset were included in the current analysis.

    3.  *EQ-5D-Y-5 L evaluation dataset*: A cross-sectional survey was administered to a convenience sample of 234 caregivers of 4-to-18-year-old children with intellectual disability between June 2022 and March 2023, where 36% had autism and intellectual disability, 27% had cerebral palsy and intellectual disability and 12% had Down syndrome \[23\]. The data were used to examine psychometric properties of a proxy report version of the EQ-5D-Y-5 L, including some comparisons with QI-Disability domain scores \[23\]. One hundred and nine unique individuals were included in the current analysis.

2.  *Simons Searchlight dataset* (<https://www.simonssearchlight.org/>): Simons Searchlight is an online registry for individuals with a genetic diagnosis associated with autism and other neurodevelopmental disorders \[24\]. At data download (V11, released 2023), the current Simons Searchlight Gene List (<https://www.simonssearchlight.org/research/what-we-study/>) contained cohorts for multiple gene and copy number variants. The data collection includes developmental and behavioural surveys submitted by parents through an online study portal. QI-Disability was administered between December 2022 and March 2023. Data from 953 individuals aged 3-to-18-year-old whose genetic variant was associated with intellectual disability were included in this analysis. In this group, nearly half (45%) had received a diagnosis of epilepsy and there were 114 gene and copy number variants (e.g., 16p11.2 deletion (*n* = 105); SCN2A (*n* = 58); 16p11.2 duplication (*n* = 55); PPP2R5D (*n* = 49); Table <a href="#Tab1" data-ref-type="table">1</a>).

3.  *Inchstone DEE Parents Speak survey dataset*: Parent advocacy groups from developmental and epileptic encephalopathy (DEE) communities within the DEE-P Connections network (<https://deepconnections.net/>) invited their members to participate in an anonymous online survey between June and November 2023. Parents were eligible to complete the survey if their child had a neurodevelopmental condition and severely impaired communication. QI-Disability was completed by 242 caregivers of individuals 2 to 18 years of whom the majority did not use words for communication (72%), 62% were diagnosed with epilepsy and 27% were taking two or more antiseizure medications \[25\]. To avoid potential duplicates, participants with gene variants (ASXL3, CSNK2A1, GRIN1, GRIN2A, GRIN2B, SCN2A, STXBP1) represented also in the Simons Searchlight dataset were removed from the Inchstone dataset. This analysis was restricted to individuals who were three years or older providing 143 participants for the current dataset. In this group, 128 (89.5%) reported a genetic cause for their child’s condition (e.g., SCN8A (*n* = 24; FOXG1 (*n* = 18); Table <a href="#Tab1" data-ref-type="table">1</a>).

<div id="Tab1" class="table-wrap">

<div class="caption">

Sample characteristics by data source (*n* = 1,699)

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th rowspan="2" style="text-align: left;">Simons Searchlight^<br />
(<em>N</em> = 953)</th>
<th colspan="6" style="text-align: left;">The Kids (<em>N</em> = 603)</th>
<th rowspan="2" style="text-align: left;">Inchstone DEE Parents Speak<sup>#</sup><br />
(<em>N</em> = 143)</th>
</tr>
<tr>
<th style="text-align: left;">Autism (<em>N</em> = 152)</th>
<th style="text-align: left;">CDD<br />
(<em>N</em> = 76)</th>
<th style="text-align: left;">CP<br />
(<em>N</em> = 180)</th>
<th style="text-align: left;">Down syndrome (<em>N</em> = 94)</th>
<th style="text-align: left;">Rett syndrome (<em>N</em> = 68)</th>
<th style="text-align: left;">Other<br />
(<em>N</em> = 33)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Age</p>
<p>Median (Range)</p></td>
<td style="text-align: center;">8.5 (3.0–17.9)</td>
<td style="text-align: center;">10.9 (4.7–17.6)</td>
<td style="text-align: center;">10.2 (5.0–18.0)</td>
<td style="text-align: center;">12.3 (5.9–18.0)</td>
<td style="text-align: center;">9.5 (5.1–17.8)</td>
<td style="text-align: left;">11.2 (5.0–17.9)</td>
<td style="text-align: center;">10.1 (5.0–18.2)</td>
<td style="text-align: center;">8.4 (3.0–18.3)</td>
</tr>
<tr>
<td style="text-align: left;"><p>Sex</p>
<p>Male (%)</p></td>
<td style="text-align: center;">535 (56.1)</td>
<td style="text-align: center;">115 (75.7)</td>
<td style="text-align: center;">13 (17.1)</td>
<td style="text-align: center;">106 (58.9)</td>
<td style="text-align: center;">39 (41.5)</td>
<td style="text-align: left;"></td>
<td style="text-align: center;">17 (51.5)</td>
<td style="text-align: center;">65 (45.5)</td>
</tr>
<tr>
<td style="text-align: left;">Female (%)</td>
<td style="text-align: center;">418 (43.9)</td>
<td style="text-align: center;">37 (24.3)</td>
<td style="text-align: center;">63 (82.9)</td>
<td style="text-align: center;">74 (41.1)</td>
<td style="text-align: center;">55 (58.5)</td>
<td style="text-align: left;">68 (100)</td>
<td style="text-align: center;">16 (48.5)</td>
<td style="text-align: center;">78 (54.6)</td>
</tr>
<tr>
<td style="text-align: left;"><p>Walks independently</p>
<p>N (%)</p></td>
<td style="text-align: center;">804 (88.1)</td>
<td style="text-align: center;">149 (98.0)</td>
<td style="text-align: center;">24 (32.0)</td>
<td style="text-align: center;">66 (36.7)</td>
<td style="text-align: center;">94 (100.0)</td>
<td style="text-align: left;">18 (26.5)</td>
<td style="text-align: center;">24 (72.7)</td>
<td style="text-align: center;">53 (37.3)</td>
</tr>
<tr>
<td style="text-align: left;"><p>QI-Disability Total scores</p>
<p>Mean (SD)</p></td>
<td style="text-align: center;">71.5 (14.4)</td>
<td style="text-align: center;">67.7 (11.1)</td>
<td style="text-align: center;">60.2 (15.0)</td>
<td style="text-align: center;">66.5 (13.3)</td>
<td style="text-align: center;">77.8 (10.4)</td>
<td style="text-align: left;">66.0 (11.3)</td>
<td style="text-align: center;">67.8 (17.7)</td>
<td style="text-align: center;">60.2 (14.4)</td>
</tr>
<tr>
<td style="text-align: left;"><p>QID-12 scores</p>
<p>Mean (SD)</p></td>
<td style="text-align: center;"><p>69.9</p>
<p>(15.7)</p></td>
<td style="text-align: center;">67.9 (12.2)</td>
<td style="text-align: center;">58.6 (17.3)</td>
<td style="text-align: center;">64.0 (14.9)</td>
<td style="text-align: center;">77.4 (11.7)</td>
<td style="text-align: left;">63.1 (12.6)</td>
<td style="text-align: center;">66.3 (18.0)</td>
<td style="text-align: center;">58.2 (16.2)</td>
</tr>
</tbody>
</table>

^ Gene diagnoses in the Simons Searchlight dataset: 16p11.2 deletion (*n* = 105); SCN2A (*n* = 58); 16p11.2 duplication (*n* = 55); PPP2R5D (*n* = 49); STXBP1 (*n* = 39); SLC6A1 (*n* = 37); CSNK2A1 (*n* = 35); CTNNB1 (*n* = 35); MED13L (*n* = 35); GRIN2B (*n* = 33); 1q21.1 duplication (*n* = 26); ASXL3 (*n* = 25); 1q21.1 deletion (*n* = 22); SYNGAP1 (*n* = 21); DLG4 (*n* = 17); HIVEP2 (*n* = 17); SETBP1 (*n* = 17); DISTAL 16p11.2 duplication (*n* = 14); HNRNPH2 (*n* = 12); CHAMP1 (*n* = 11); DYRK1A (*n* = 11); DISTAL 16p11.2 deletion (*n* = 10); 15q11.2 BP1-BP2 deletion (*n* = 9); 7q11.23 duplication (*n* = 9); AUTS2 (*n* = 8); CHD2 (*n* = 8); PACS1 (*n* = 8); VPS13B (*n* = 8); MED13 (*n* = 7); WDFY3 (*n* = 7); ANKRD11 (*n* = 6); ARID1B (*n* = 6); CSNK2B (*n* = 6); SETD5 (*n* = 6); ADNP (*n* = 5); FOXP1 (*n* = 5); KMT2E (*n* = 5); TRIO (*n* = 5); TRIP12 (*n* = 5); and 75 variants with frequency \< 5.

<sup>\#</sup> Parent reported gene diagnoses in the Inchstone dataset: Phelan McDermid syndrome (*n* = 31); SCN8A (*n* = 24); FOXG1 (*N* = 18); ASXL1 (*N* = 12); DUP15Q (*N* = 6); KCNT1 (*N* = 6); CACNA1A (*N* = 5); and 26 gene variants with frequency \< 5. No genetic diagnosis reported for 15 individuals.

</div>

### Variables

*Quality of life* - QI-Disability is a parent-report measure used to assess quality of life for children and adolescents with intellectual disability. It is a 32-item measure with responses rated on a 5-point scale. Items cluster into six domains of physical health, positive and negative emotions, social interaction, leisure and the outdoors, and independence. Scores are scaled to a 0–100-point scale, with higher scores indicating better QOL \[5\].

*Descriptive variables* –Descriptive variables that were common across the datasets included age, sex, diagnosis, and ability to walk (classified as independent walking or not). Genetic variant information was available for children with Rett syndrome or Down syndrome in the QI-Disability determinants, CDKL5 deficiency disorder, Simons Searchlight and Inchstone datasets.

### Statistical methods

*Short Form Development* - The Genetic algorithm (GA) was implemented using R package *GAabbreviate.*. The GA simulates natural evolution by randomly generating short versions of the scale and evaluating them according to a fitness function until an optimal solution is reached. The algorithm is designed to minimise the following fitness function \[26\], where

<div id="Equa" class="disp-formula">

<img src="d33e611.gif" id="d33e611" />

</div>

‘I’ is a user-specified fixed item cost, ‘k’ is the number of items to be retained, ‘s’ is the number of subscales, ‘w<sub>i</sub>’ are the weights associated with each subscale and ‘R<sub>i</sub><sup>2</sup>’ is the amount of variance in the subscale explained by a linear combination of retained item scores. We fixed the number of retained items to be 12 and, given that our retained items would form a single subscale, minimising the above fitness function reduces to a simple maximisation of the variance in total QI-Disability score explained by a subset of 12 items.

The algorithm was run 500 times with different seed values, and the final item set selected consisted of the 12 items which appeared most often in the 500 optimum solutions. We also specified a constraint that the final item set had to contain at least one item from each QI-Disability domain and no more than 3 items from any domain.

*Short Form Psychometric Evaluation* - Pearson correlation coefficient was used to compare the 12-item total score with the QI-Disability 32-item total score. Internal consistency of the reduced item set was assessed with Cronbach’s Alpha.

Rasch analysis of the final item set was performed using the partial credit model within the R package *eRm.* Item fit to the Rasch model was assessed using Infit and Outfit mean square statistics; person separation reliability was calculated and the Martin-Loef test was used to confirm unidimensionality of the reduced item set. Targeting of the items was assessed using the Person-Item map showing the correspondence between item difficulties and person abilities. Finally Disordered Category Thresholds for any item were noted. Disordered thresholds occur when the ordering of the thresholds does not correspond to the natural order of difficulty of the categories.

## Results

A total of 1,699 unique and complete QI-Disability measures were included. The median age was 9.4 years (range 3.0–18.3 years). The country of residence was known for participants in all datasets except for the Simons Searchlight dataset (*n* = 953; a global database where anonymous data are provided). Among the remaining participants, 539 were from Oceania, with the majority from Australia; 160 were from North America, with most from the United States; 38 were from Europe, with the largest group from Germany (*n* = 10); and small numbers were from South America, Africa, and Asia.

The mean (SD) QI-Disability total score was 69.2 (14.4) (Table <a href="#Tab1" data-ref-type="table">1</a>). Participant characteristics varied across cohorts, including differences in diagnosis, sex distribution, ability to walk, and QI-Disability scores. Across datasets, the sample included children with a wide range of functional abilities, including variation in mobility, communication, and independence, consistent with mild to profound intellectual disability and a range of adaptive behaviour abilities. For example, most children with autism were male (75.7%), most with CDD were female (82.9%) and all children with RTT were female (100%). Most children in the Simons dataset (88.1%), with autism and intellectual disability (98.0%) and all with Down syndrome could walk independently. Smaller fractions of children with cerebral palsy and intellectual disability (32.0%), CDD (32.0%), RTT (26.5%) and in the Inchstone dataset (37.3%) could walk independently. Higher QI-Disability Total and QID-12 scores were observed for children with Down syndrome and lower QI-Disability Total and QID-12 scores were observed for children with a genetically caused epilepsy condition including CDD and many of those in the Inchstone dataset. See Table <a href="#Tab1" data-ref-type="table">1</a>.

After applying the genetic scale reduction algorithm and domain membership restrictions, the most frequently selected items comprising the final QID-12 include two items from the Physical Health domain, three items from the Positive Emotions domain, one item each from the Negative Emotions and Social Interactions domain, three items from the Leisure and the Outdoors domain and two items from the Independence domain (Table <a href="#Tab2" data-ref-type="table">2</a>).

<div id="Tab2" class="table-wrap">

<div class="caption">

Fit Statistics and item locations for the items in the reduced item set

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Domain</th>
<th style="text-align: left;">Item</th>
<th style="text-align: left;">Outfit Mean Square*</th>
<th style="text-align: left;">Infit Mean Square*</th>
<th style="text-align: left;">Item Location (logits)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: left;">Physical health</td>
<td style="text-align: left;">Had enough energy to participate in routines and activities</td>
<td style="text-align: center;">0.97</td>
<td style="text-align: center;">0.921</td>
<td style="text-align: center;">-0.167</td>
</tr>
<tr>
<td style="text-align: left;">Slept well through the night</td>
<td style="text-align: center;">1.213</td>
<td style="text-align: center;">1.16</td>
<td style="text-align: center;">0.664</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Positive emotions</td>
<td style="text-align: left;">Been in a good mood</td>
<td style="text-align: center;">0.765</td>
<td style="text-align: center;">0.777</td>
<td style="text-align: center;">-0.561</td>
</tr>
<tr>
<td style="text-align: left;">Smiled or brightened their facial expression</td>
<td style="text-align: center;">0.697</td>
<td style="text-align: center;">0.738</td>
<td style="text-align: center;">-0.369</td>
</tr>
<tr>
<td style="text-align: left;">Showed happiness through body language</td>
<td style="text-align: center;">0.637</td>
<td style="text-align: center;">0.671</td>
<td style="text-align: center;">-0.143</td>
</tr>
<tr>
<td style="text-align: left;">Negative emotions</td>
<td style="text-align: left;">Appeared upset or angry</td>
<td style="text-align: center;">1.433</td>
<td style="text-align: center;">1.407</td>
<td style="text-align: center;">1.215</td>
</tr>
<tr>
<td style="text-align: left;">Social interactions</td>
<td style="text-align: left;">Appeared relaxed when making eye contact</td>
<td style="text-align: center;">0.888</td>
<td style="text-align: center;">0.887</td>
<td style="text-align: center;">0.712</td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;">Leisure and the outdoors</td>
<td style="text-align: left;">Enjoyed feeling steady or stable during physical activities</td>
<td style="text-align: center;">0.809</td>
<td style="text-align: center;">0.821</td>
<td style="text-align: center;">0.802</td>
</tr>
<tr>
<td style="text-align: left;">Enjoyed physical activities</td>
<td style="text-align: center;">0.784</td>
<td style="text-align: center;">0.822</td>
<td style="text-align: center;">0.449</td>
</tr>
<tr>
<td style="text-align: left;">Enjoyed going on outings in the community</td>
<td style="text-align: center;">0.914</td>
<td style="text-align: center;">0.912</td>
<td style="text-align: center;">0.758</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Independence</td>
<td style="text-align: left;">Made their own choices for activities or things they enjoy</td>
<td style="text-align: center;">1.053</td>
<td style="text-align: center;">1.039</td>
<td style="text-align: center;">0.822</td>
</tr>
<tr>
<td style="text-align: left;">Helped to complete routine activities</td>
<td style="text-align: center;">1.086</td>
<td style="text-align: center;">1.092</td>
<td style="text-align: center;">1.450</td>
</tr>
</tbody>
</table>

\*Satisfactory model fit indicated by mean square values below 1.5

</div>

Correlation of the 12-item total with the QI-Disability total score (average of domain scores) was high (Pearson’s rho = 0.970), demonstrating that the short form reflected overall QOL. Internal consistency (Alpha = 0.84) was satisfactory, supporting the reliability of the reduced dataset.

Rasch analysis of the QID-12 confirmed satisfactory fit to the partial credit model, with both Infit and Outfit mean square statistics all below the recommended upper threshold of 1.5. (Table <a href="#Tab2" data-ref-type="table">2</a>). Person separation reliability was 0.84, and the Martin-Loef test showed no significant departure from unidimensionalty (*p* = 0.12). The Person Item map (Fig. <a href="#Fig1" data-ref-type="fig">1</a>) showed reasonable targeting with the item difficulty locations covering the full range of ability scores in the sample although there was better coverage at the lower end of the quality of life score spectrum. Minor irregularities in category thresholds were observed for the items ‘feeling steady or stable during physical activities’, ’making their own choices’ and ‘helped with routines’ where the difficulty thresholds between categories 1 and 2 (‘Never’ and ‘Rarely’) and categories 2 and 3 (‘Rarely and ‘Sometimes’) were reversed from their natural order.

<figure id="Fig1">
<p><img src="11136_2026_4223_Fig1_HTML.jpg" id="d33e1188" /></p>
<p><img src="11136_2026_4223_Fig1_HTML.gif" /></p>
<figcaption><strong>Person-Item map for the reduced QI-Disability item set</strong></figcaption>
</figure>

## Discussion

This study developed and validated a 12-item short form of QI-Disability, referred to as QID-12. The Genetic Algorithm (GA) has been shown to outperform other techniques for scale reduction and has been successfully applied by researchers to abbreviate scales in a variety of medical and psychological settings \[17, 18\]. Using a GA approach in a large and diverse sample of 1,699 children with intellectual disability, we systematically identified a reduced item set that retained strong alignment with the original 32-item scale. The QID-12 showed high correlation with the original measure, acceptable internal consistency, and good Rasch model fit, confirming that it provides an accurate representation of overall quality of life.

The final 12 items spanned the six domains of the original measure to preserve the conceptual breadth of QOL as operationalised by QI-Disability. Correlation with the full scale was high (0.97) demonstrating that QID-12 scores reflected overall QOL scores, observed also in the score patterns for different groups with the dataset. While the high correlation between QID-12 and the full QI-Disability is reassuring, it should be interpreted in context. The short form draws directly from the original 32-item measure and was developed within the same sample, which likely inflates the association. Reliability estimates, although slightly reduced compared to the full scale, remained within acceptable ranges (α = 0.85; person separation reliability = 0.84). Rasch analysis further confirmed the psychometric adequacy of the short form, with satisfactory item fit, and item difficulty reasonably well distributed to capture the full range of children’s quality of life, along with evidence of unidimensionality. Although quality of life is multidimensional, the absence of strong evidence against unidimensionality supports the use of the QID-12 as an index of overall quality of life rather than a domain-level assessment tool. Although three items (‘steady stable’, ‘choices’ and ‘helped routine’) showed slight inconsistencies in response category ordering, it has been shown that this phenomenon occurs when there is a low frequency of intermediate response categories and that it probably does not compromise the utility of a measurement scale \[27\].

The QID-12 has clear utility in settings where respondent burden is a concern, such as large-scale surveys, longitudinal studies, registries, and clinical settings where caregivers are asked to complete multiple measures. In these contexts, the availability of a brief and psychometrically robust index of overall quality of life will support the inclusion of patient and caregiver-reported outcomes alongside other measures, improving feasibility without compromising measurement integrity. In clinical settings, the QID-12 may be useful as a quick screening and monitoring tool to track overall quality of life over time or the effectiveness of interventions and services. However, it is not intended to replace the full QI-Disability in situations where detailed domain-level assessment is required. While the short form offers a more efficient way to assess QOL, the longer version of the QI-Disability still holds distinct advantages. The full 32-item measure covers a wide range of questions, providing a more comprehensive understanding of a child’s QOL in certain contexts. Although the short forms reduced length is beneficial in some situations, it may miss acumen for each of the dimensions when more detailed information is required. Specifically, in clinical settings where more detailed insight into a child’s specific QOL-challenges is needed, the full version provides more granular insights. Therefore, it is important not to overlook the original 32-item measure in these instances.

Strengths of this study include the large, heterogeneous sample, which included data from multiple sources and spanned a broad age range and functional abilities. The use of an advanced optimisation method also represents a methodological strength, allowing for systematic identification of an item set that maintains conceptual breadth whilst reducing length. One limitation is that a few items exhibited disordered category thresholds although it unlikely impacted the overall psychometric performance of a scale when disordered thresholds are an artefact of a low frequency of intermediate response categories \[27\]. There were also limited descriptive variables that were common across the data sources, although more sample description is provided in each of the accompanying papers. Additionally, while the QID-12 was validated against the full version, future research should focus on validating the QID-12 in independent cohorts and across more diverse settings. This would help confirm the tool’s generalizability and assess whether it performs the same way as the full version in different populations and contexts.

## Conclusions

The QID-12 presents a psychometrically sound and efficient short form of QI-Disability. It provides clinicians and researchers with a practical tool for measuring child QOL that minimises burden while maintaining conceptual breadth and measurement integrity. Future research should focus on further validation of the QID-12 in independent cohorts, examining its responsiveness to change in clinical trials, and comparing its performance to the full 32-item version across diverse settings.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

## Acknowledgements

We would firstly like to acknowledge and thank all families who participated in this study. The authors acknowledge access to Simons Searchlight phenotypic data on the SFARI Base. Approved researchers can obtain the Simons Searchlight population dataset (https://www.sfari.org/resource/simons-searchlight/) by applying at https://base.sfari.org. Funding for the data collections were provided by National Health and Medical Research Council (1103745), the EuroQol Research Foundation (EQ Project 429-RA) and donations to the Inchstone Project. We also acknowledge the ongoing support from the International Foundation for CDKL5 Research. AW is supported by an Investigator Grant from the National Health and Medical Research Council (2034130). JD is supported by a Fellowship from the Stan Perron Charitable Foundation. NNL is supported by a Eunice Kennedy Shriver National Institute of Child Health & Human Development of the National Institutes of Health Career Development Award (1K23HD115865). The funders had no influence on the content of the paper. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

## Author contributions

Melissa K. Licari, Jenny Downs and Peter Jacoby contributed to the study conception and design. Data preparation and analysis were performed by Melissa K. Licari, Jenny Downs and Peter Jacoby. The first draft of the manuscript was written by Melissa K. Licari and all authors contributed to previous versions of the manuscript. All authors read and approved the final manuscript.

## Funding

Open Access funding enabled and organized by CAUL and its Member Institutions. Funding for the data collections were provided by National Health and Medical Research Council (1103745), the EuroQol Research Foundation (EQ Project 429-RA) and donations to the Inchstone Project. We also acknowledge the ongoing support from the International Foundation for CDKL5 Research. AW is supported by an Investigator Grant from the National Health and Medical Research Council (2034130). JD is supported by a Fellowship from the Stan Perron Charitable Foundation, and by an Investigator Grant from the National Health and Medical Research Council (2041484). NNL is supported by a Eunice Kennedy Shriver National Institute of Child Health & Human Development of the National Institutes of Health Career Development Award (1K23HD115865). The funders had no influence on the content of the paper. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

## Data availability

The data supporting the findings of this study were obtained from multiple studies and are subject to ethical and governance restrictions. As these data include sensitive information relating to children with intellectual disability, they are not publicly available. De-identified data may be made available upon reasonable request to the corresponding author, subject to approval by the relevant ethics committees and data custodians.

## Declarations

### Competing interests

MKL: Consultancy for Neurogene. Any renumeration has been made to her department. JD: Consultancy for Marinus, Ultragenyx, Acadia, Avexis, Orion, Takeda, Neurogene and Taysha; Clinical Trials with Anavex and Newron; Consulting/Advisory Board member for SCN2A Australia. Any remuneration has been made to her department. NNL: Consultant honoraria from Taysha Gene Therapies and Stoke Therapeutics. MW: Consultancy for Biotechnology Value Fund. The remaining authors have no relevant financial or non-financial interests to disclose.

### Ethics approval

This validation study for the Quality of Life Inventory – Disability including analyses of Simons Searchlight data was approved by the Human Ethics Research Committee of the University of Western Australia (2019/RA/4/20/4276). The CDKL5 data collection was approved by the Human Research Committee of the University of Western Australia (2020/[ET000271](https://www.ncbi.nlm.nih.gov/nuccore/ET000271)). The collection of additional data as part of the EuroQOL funded study was approved by the Human Research Committee of the University of Western Australia (2022/[ET000126](https://www.ncbi.nlm.nih.gov/nuccore/ET000126)). The Inchstone study protocol was reviewed and determined to be exempt by the North Star Ethics Review Board (protocol \# NB300112), with acknowledgement from the institution review boards of the Johns Hopkins School of Medicine and Nationwide Children’s Hospital. Additionally, the study received approval from the Human Research Ethics Committee at The University of Western Australia (2019/RA/4/20/6198).

### Consent to participate

Informed written consent was obtained from the parents included in the study.

## Footnotes

## References

## References

1. World Health Organization. (1993). Measuring quality of life: the development of the World Health Organization Quality of Life Instrument (WHOQOL). Division of Mental Health, World Health Organisation.

2. Leonard, H., Downs, J., Benke, T. A., Swanson, L., Olson, H., & Demarest, S. (2022). CDKL5 deficiency disorder: clinical features, diagnosis, and management. The Lancet Neurology, 21(6), 563–576. doi:10.1016/S1474-4422(22)00035-7

3. Scheffer, I. E., Zuberi, S., Mefford, H. C., Guerrini, R., & McTague, A. (2024). Developmental and epileptic encephalopathies. Nat Rev Dis Primers, 10(1), 61. doi:10.1038/s41572-024-00546-6

4. Santoro, S. L., Donelan, K., & Constantine, M. (2022). Proxy-report in individuals with intellectual disability: A scoping review. Journal Of Applied Research In Intellectual Disabilities, 35(5), 1088–1108. doi:10.1111/jar.13013

5. Downs, J., Jacoby, P., Leonard, H., Epstein, A., Murphy, N., Davis, E., Reddihough, D., Whitehouse, A., & Williams, K. (2019). Psychometric properties of the Quality of Life Inventory-Disability (QI-Disability) measure. Quality Of Life Research, 28(3), 783–794. doi:10.1007/s11136-018-2057-3

6. Downs, J., Jacoby, P., Saldaris, J., Leonard, H., Benke, T., Marsh, E., & Demarest, S. (2022). Negative impact of insomnia and daytime sleepiness on quality of life in individuals with the cyclin-dependent kinase-like 5 deficiency disorder. Journal Of Sleep Research, e13600.

7. Saldaris, J. M., Jacoby, P., Leonard, H., Benke, T. A., Demarest, S., Marsh, E. D., & Downs, J. (2023). Psychometric properties of QI-Disability in CDKL5 Deficiency Disorder: Establishing readiness for clinical trials. Epilepsy & Behavior, 139, 109069. doi:10.1016/j.yebeh.2022.109069

8. Tangarorang, J., Leonard, H., Epstein, A., & Downs, J. (2019). A framework for understanding quality of life domains in individuals with the CDKL5 deficiency disorder. Am J Med Genet A, 179(2), 249–256. doi:10.1002/ajmg.a.61012

9. Downs, J., Jacoby, P., Specchio, N., Cross, H., Amin, S., Bahi-Buisson, N., Rajaraman, R., Suter, B., Devinsky, O., Aimetti, A., Busse, G., Olson, H. E., Demarest, S., Benke, T. A., & Pestana-Knight, E. (2024). Effects of ganaxolone on non-seizure outcomes in CDKL5 Deficiency Disorder: Double-blind placebo-controlled randomized trial. European Journal Of Paediatric Neurology : Ejpn : Official Journal Of The European Paediatric Neurology Society, 51, 140–146. doi:10.1016/j.ejpn.2024.06.005

10. Ziegler, A., Carroll, J., Bain, J. M., Sands, T. T., Fee, R. J., Uher, D., Kanner, C. H., Montes, J., Glass, S., Douville, J., Mignon, L., Gleeson, J. G., Crooke, S. T., & Chung, W. K. (2024). Antisense oligonucleotide therapy in an individual with KIF1A-associated neurological disorder. Nature Medicine, 30(10), 2782–2786. doi:10.1038/s41591-024-03197-y

11. Koğar, H. (2020). Development of a Short Form: Methods, Examinations, and Recommendations. Journal of Measurement and Evaluation in Education and Psychology, 11(3), 302–310.

12. Leite, W. L., Huang, I. C., & Marcoulides, G. A. (2008). Item Selection for the Development of Short Forms of Scales Using an Ant Colony Optimization Algorithm. Multivariate Behav Res, 43(3), 411–431. doi:10.1080/00273170802285743

13. Crone, D. L., Rhee, J. J., & Laham, S. M. (2021). Developing brief versions of the Moral Foundations Vignettes using a genetic algorithm-based approach. Behavior Research Methods, 53(3), 1179–1187. doi:10.3758/s13428-020-01489-y

14. Passarelli, M., Casetta, L., Rizzi, L., Chiorri, C., Cassina, F., Voi, S., & Rocco, D. (2024). Short and sweet: Comparing strategies for the reduction of questionnaires on self-criticism and social safeness while preserving construct validity. International Journal Of Psychology : Journal International De Psychologie, 59(6), 1234–1244. doi:10.1002/ijop.13249

15. Schroeders, U., Wilhelm, O., & Olaru, G. (2016). Meta-Heuristics in Short Scale Construction: Ant Colony Optimization and Genetic Algorithm. PLoS One, 11(11), e0167110.

16. Eisenbarth, H., Lilienfeld, S. O., & Yarkoni, T. (2015). Using a genetic algorithm to abbreviate the Psychopathic Personality Inventory-Revised (PPI-R). Psychological Assessment, 27(1), 194–202. doi:10.1037/pas0000032

17. McCray, G., Hope, H. F., Glasscoe, C., Hill, J., Quittner, A., Southern, K. W., & Lancaster, G. A. (2025). Development and validation of a short form psychometric tool assessing the caregiving Challenge of Living with Cystic Fibrosis (CLCF-SF) in a child. Psychology & Health, 40(3), 410–432. doi:10.1080/08870446.2023.2231489

18. Epstein, A., Williams, K., Reddihough, D., Murphy, N., Leonard, H., Whitehouse, A., Jacoby, P., & Downs, J. (2019). Content validation of the Quality of Life Inventory-Disability. Child: Care, Health And Development, 45(5), 654–659. doi:10.1111/cch.12691

19. Jacoby, P., Epstein, A., Kim, R., Murphy, N., Leonard, H., Williams, K., Reddihough, D., Whitehouse, A., & Downs, J. (2020). Reliability of the Quality of Life Inventory-Disability (QI-Disability) measure in children with intellectual disability. Journal of Developmental and Behavioral Pediatrics, 41(7), 534–539. doi:10.1097/DBP.0000000000000815

20. Leonard, H., Cobb, S., & Downs, J. (2017). Clinical and biological progress over 50 years in Rett syndrome. Nat Rev Neurol, 13(1), 37–51. doi:10.1038/nrneurol.2016.186

21. Williams, K., Jacoby, P., Whitehouse, A., Kim, R., Epstein, A., Murphy, N., Reid, S., Leonard, H., Reddihough, D., & Downs, J. (2021). Functioning, participation and quality of life in children with intellectual disability: An observational study. Developmental Medicine and Child Neurology, 63, 89–96. doi:10.1111/dmcn.14657

22. Leonard, H., Junaid, M., Wong, K., Demarest, S., & Downs, J. (2021). Exploring quality of life in individuals with a severe developmental and epileptic encephalopathy, CDKL5 Deficiency Disorder. Epilepsy Research, 169, 106521. doi:10.1016/j.eplepsyres.2020.106521

23. Downs, J., Norman, R., Mulhern, B., Jacoby, P., Reddihough, D., Choong, C. S., Finlay-Jones, A., & Blackmore, A. M. (2024). Psychometric Properties of the EQ-5D-Y-5L for Children With Intellectual Disability. Value In Health : The Journal Of The International Society For Pharmacoeconomics And Outcomes Research, 27(6), 776–783. doi:10.1016/j.jval.2024.02.016

24. Simons Vip Consortium. (2012). Simons Variation in Individuals Project (Simons VIP): a genetics-first approach to studying autism spectrum and related neurodevelopmental disorders. Neuron, 73(6), 1063–1067. doi:10.1016/j.neuron.2012.02.014

25. Ludwig, N. N., Licari, M. K., Wojnaroski, M., Conecker, G., Hecker, J., Hommer, R., Muzyczka, K., Jacoby, P., & Downs, J. (2026). Caregiver-reported quality of life in individuals with developmental and epileptic encephalopathy and other severe neurodevelopmental encephalopathies. Quality Of Life Research, 35(2), 45. doi:10.1007/s11136-025-04153-0

26. Sahdra, B. K., Ciarrochi, J., Parker, P., & Scrucca, L. (2016). Using genetic algorithms in a large nationally representative american sample to abbreviate the Multidimensional Experiential Avoidance Questionnaire. Frontiers in Psychology, 7, 189. doi:10.3389/fpsyg.2016.00189

27. Adams, R. C., Wu, M., & Wilson, M. (2012). The Rasch rating model and the disordered threshold controversy. Educational and Psychological Measurement, 72(4), 547–573.

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary Material 1

</div>

### Data Availability Statement

The data supporting the findings of this study were obtained from multiple studies and are subject to ethical and governance restrictions. As these data include sensitive information relating to children with intellectual disability, they are not publicly available. De-identified data may be made available upon reasonable request to the corresponding author, subject to approval by the relevant ethics committees and data custodians.

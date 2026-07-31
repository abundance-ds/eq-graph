---
project_id: "1812-PHD"
work_id: "doi:10.1186/s13643-025-03060-2"
doi: "10.1186/s13643-025-03060-2"
pmid: "41540454"
pmcid: "PMC12892695"
title: "Generic health-related quality of life instruments among children and adolescents in low- and middle-income countries: a scoping review"
journal: "Systematic Reviews"
publication_date: "2026-01-16"
volume: "15"
authors:
  - name: "Goitom Molalign Takele"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Trudy Sullivan"
    affiliation_ids:
      - "Aff3"
  - name: "Ari Samaranayaka"
    affiliation_ids:
      - "Aff4"
  - name: "Mimmi Åström"
    affiliation_ids:
      - "Aff5"
  - name: "Michael Herdman"
    affiliation_ids:
      - "Aff6"
  - name: "Gashaw Arega"
    affiliation_ids:
      - "Aff7"
  - name: "Sarah Derrett"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Ngāi Tahu Māori Health Research Unit, Division of Health Sciences, Ōtākou Whakaihu Waka University of Otago, Dunedin, New Zealand"
  - id: "Aff2"
    name: "School of Nursing, College of Health Sciences, Mekelle University, Mekelle, Ethiopia"
  - id: "Aff3"
    name: "Department of Preventive and Social Medicine, Division of Health Sciences, University of Otago, Dunedin, New Zealand"
  - id: "Aff4"
    name: "Biostatistics Centre, Department of Preventive and Social Medicine, Division of Health Sciences, University of Otago, Dunedin, New Zealand"
  - id: "Aff5"
    name: "Health Outcomes and Economic Evaluation Research Group, Department of Learning, Informatics, Management and Ethics, Stockholm Centre for Healthcare Ethics, Karolinska Institutet, Stockholm, Sweden"
  - id: "Aff6"
    name: "Saw Swee Hock School of Public Health, National University of Singapore, Singapore, Singapore"
  - id: "Aff7"
    name: "Department of Paediatrics and Child Health, School of Medicine, College of Health Sciences, Addis Ababa University, Addis Ababa, Ethiopia"
licence: "cc-by-nc-nd"
source_file: "input/projects/1812-PHD/papers/doi_10.1186_s13643-025-03060-2.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12892695/fullTextXML"
source_method: "epmc_xml"
source_sha256: "b48f6ba215560bfecea3fdb9c5173900c174b5c39d8a9e381af9e5b08a7ef95c"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Generic health-related quality of life instruments among children and adolescents in low- and middle-income countries: a scoping review

## Abstract

### Background

Health-related quality of life (HRQoL) measures are widely used in research and clinical practice; however, their application among children and adolescents in low- and middle-income countries (LMICs), where most of the world’s youth reside remains underexplored. This scoping review aims to identify generic HRQoL instruments used in LMICs and describe their applications and reported psychometric properties.

### Method

Guided by Arksey and O’Malley’s framework, a search for peer-reviewed papers published between 2000 and 2024 was conducted in six databases (Medline, Embase, PubMed, Scopus, CINAHL, and Web of Science). The review included papers reporting the use of generic HRQoL instruments among individuals aged 0–19 years in LMICs.

### Results

A total of 152 papers originating from 22 (of 75) LMICs were included. Nearly half of the papers were from India 50 (32.9%) and Egypt 25 (16.5%). Eight generic HRQoL instruments (PedsQL 4.0 GCS, KIDSCREEN-10/27/52, HUI-2/3, EQ-5D-Y-3L/5L, PROMIS-25, PedsQL Short Form (15-items), EQ-5D-3L/5L, and SF-36) were identified. Of these, PedsQL 4.0 GCS was reported in 78% of papers. Only 11 (7.2%) papers reported use of the instruments in the general population, and only one generated population norms. Very few studies 2 (1.3%) included children ≤ 4 years. One-third (34.9%) of the studies included both self- and proxy-reported HRQoL data. Most of the instruments were used for general health assessment (77.6%); only 9.9% of studies evaluated treatment or intervention outcomes, and 12.5% were psychometric studies. None of the psychometric studies assessed all nine measurement properties recommended by COSMIN.

### Conclusion

The use of generic HRQoL instruments in studies of children and adolescents in LMICs, mainly with PedsQL, has increased in recent years, though almost half of the studies identified were carried out in only two countries. Despite their growing use, gaps remain in population coverage, psychometric evidence, and the geographic distribution of research in LMICs using generic HRQoL instruments.

### Scoping review registration

The protocol was submitted to Open Science Framework on 24 January 2025. Registration DOI: <https://doi.org/10.17605/OSF.IO/MVG62>

### Supplementary Information

The online version contains supplementary material available at 10.1186/s13643-025-03060-2.

**Keywords:** Health-related quality of life (HRQoL), Children, Adolescents, Generic instrument, Low- and middle-income countries (LMICs)

Received 2025 Sep 15; Accepted 2025 Dec 23; Collection date 2026.

## Background

Two-thirds (65%) of the world’s children and adolescents live in low- and middle-income countries (LMICs), and this is projected to rise further by 2050 \[1–3\]. Importantly, a disproportionate burden of both communicable and non-communicable diseases and injuries is borne in LMICs compared to high-income countries \[4–6\]. These burdens can restrict, or even prevent, children and adolescents from attaining their full potential \[7\]. In light of this, major global and regional organizations have emphasized the health and well-being of children and adolescents in LMICs \[3, 8, 9\].

While measures of mortality and morbidity are important, it is also necessary to understand the health needs of children and adolescents from their perspectives. Consequently, generic measures of health-related quality of life (HRQoL), which assess the physical, psychological, and social aspects of overall health \[10\], are increasingly used in general population research as well as in clinical settings \[11\]. These generic HRQoL instruments have been used to monitor population health changes over time, in clinical settings, and in economic evaluations \[12–20\].

For LMICs with limited healthcare budgets and the higher burden of illnesses and injuries, generic instruments could provide substantial benefits by enabling the monitoring of health changes, evaluating medical interventions, identifying high-risk groups, and prioritizing healthcare interventions.

Although various HRQoL instruments have been developed and validated for children and adolescents, no comprehensive review has examined the use of generic HRQoL instruments in LMICs. Existing reviews have focused on specific diseases \[21–23\], geographic regions \[24\] or populations \[25\], leaving a gap in understanding of their broader use in LMICs. Consequently, this review addresses this knowledge gap by focusing on the use of generic HRQoL measures among children and adolescents in LMICs.

This scoping review aims to systematically identify the generic HRQoL instruments used, their stated purposes or applications, and reported psychometric properties among children and adolescents in LMICs. The evidence generated is expected to provide researchers, clinicians, and policymakers with a comprehensive understanding of the current state of HRQoL measurement in LMICs and highlight opportunities for improving their use in future studies.

## Methods

The scoping review was registered in Open Science Framework (OSF) \[26\]. The review follows the framework proposed by Arksey and O’Malley \[27\], incorporating the refinements recommended by Levac et al.’s guidelines for conducting scoping reviews to enhance the rigor and transparency \[28\]. The Preferred Reporting Items for Systematic Review and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR) \[29\] was used to ensure complete and transparent reporting of the scoping review (Supplementary Data 1).

### Search strategy

A systematic search of Medline (via Ovid), Embase (via Ovid), PubMed, Scopus, CINAHL, and Web of Science databases was conducted to identify peer-reviewed papers published in English from 2000 to 2024. The search strategy was developed in consultation with the Health Sciences librarian at the University of Otago and the wider research team. It combined Medical Subject Headings \[30\], keywords, abbreviations, and synonyms using Boolean operators (‘AND’ and ‘OR’) (Supplementary Data 2).

### Study selection and eligibility criteria

Identified papers were independently screened by two reviewers (GM and a second reviewer). The first 100 abstracts were jointly reviewed to ensure consistency. Subsequently, the reviewers independently conducted title and abstract screening, followed by a full-text screening of all eligible papers. Regular meetings were held to resolve any discrepancies at the end of each stage through consensus.

Papers fulfilling the following criteria were included:

1.  Peer-reviewed research papers presenting empirical quantitative findings derived from the use of generic HRQoL instruments in children and adolescents aged ≤ 19 years (to ensure inclusion of generic HRQoL instruments designed for use across the full range of paediatric age ranges, extending from birth to 19 years according to the World Health Organization \[31\]) in LMICs (based on the World Bank Classification \[32\]). Papers that included both LMICs and non-LMICs data were eligible if the LMIC findings were reported separately.

2.  Peer-reviewed papers published between 1 January 2000 and 31 December 2024.

3.  Papers published in the English language (due to the resource and time constraints and absence of translation capacity within the research team).

Papers were excluded if they:

1.  Reported only on the use of non-generic HRQoL instruments;

2.  Were conference abstracts, editorials, discussion papers, or papers that were unable to be retrieved;

3.  Did not specify the target population as coming from a LMICs or the relevant age group;

4.  Reported findings from qualitative studies, meta-analyses, systematic reviews, or scoping reviews.

### Data extraction

Papers identified for inclusion were read in full, and study data were extracted by the first reviewer (GM). Data were collected on the study characteristics (Tables <a href="#Tab1" data-ref-type="table">1</a>, <a href="#Tab2" data-ref-type="table">2</a> and <a href="#Tab3" data-ref-type="table">3</a>, Figs. <a href="#Fig2" data-ref-type="fig">2</a> and <a href="#Fig3" data-ref-type="fig">3</a>, and Supplementary Data 3) using a Microsoft Excel spreadsheet.

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of the included papers

</div>

| Characteristics | Category | Papers *n* (%) |
|----|----|----|
| Mutually exclusive age groups | 1 month – 4 years | 2 (1.3) |
|  | 1–12 years | 8 (5.3) |
|  | 2–18 years | 26 (17.0) |
|  | 5–18 years | 41 (27.0) |
|  | 8–18 years | 65 (42.8) |
|  | \< 18 years | 10 (6.6) |
| Years of publication | 2005–2009 | 1 (0.7) |
|  | 2010–2014 | 25 (16.4) |
|  | 2015–2019 | 48 (31.6) |
|  | 2020–2024 | 78 (51.3) |
| Study designs | Randomized controlled trials | 11 (7.3) |
|  | Cross-sectional | 128 (84.3) |
|  | Case–control | 8 (5.2) |
|  | Cohort study | 4 (2.6) |
|  | Quasi experimental | 1 (0.6) |
| Study settings<sup>\*</sup> | Outpatient clinics | 70 (46.0) |
|  | Inpatient clinics | 16 (10.5) |
|  | Inpatient and outpatient clinics | 6 (4.0) |
|  | Community | 20 (13.2) |
|  | Schools | 46 (30.3) |
|  | Care homes | 3 (2.0) |
|  | Specialized schools | 3 (2.0) |
|  | Not stated | 38 (25.0) |

<sup>\*</sup>Participants were recruited from more than one setting in several studies, therefore the total number of study settings is greater than the total number of papers

</div>

<div id="Tab2" class="table-wrap">

<div class="caption">

Characteristics of completion and purpose of using HRQoL instruments

</div>

| Characteristics | Category | *n* (%) |
|----|----|----|
| Who completed the instruments | Child and/or adolescent and/or proxy | 69 (45.4) |
|  | Child and/or adolescent | 51 (33.5) |
|  | Proxy | 20 (13.2) |
|  | Not clearly stated | 12 (7.9) |
| How was the instrument completed | Self-completed | 67 (44.1) |
|  | Interviewer administered | 52 (34.2) |
|  | Mixed (self and interview) | 10 (6.6) |
|  | Not clearly stated | 23 (15.1) |
| Mode of completion | Pen-and-paper | 95 (62.6) |
|  | Phone interviews | 4 (2.6) |
|  | Electronic (PC, table, or smartphone) | 9 (5.9) |
|  | Mixed | 4 (2.6) |
|  | Not clearly stated | 40 (26.3) |
| Application of HRQoL instruments | General HRQoL assessment | 118 (77.6) |
|  | Evaluation of treatment or intervention outcomes | 15 (9.9) |
|  | Psychometric studies | 19 (12.5) |

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

Psychometric properties of included instruments reported according to COSMIN

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;"><strong>Reliability (Referenced to papers reporting reliability)</strong></th>
<th colspan="3" style="text-align: left;"><strong>Validity (Referenced to papers reporting validity)</strong></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Test–retest</th>
<th style="text-align: left;">Internal consistency</th>
<th style="text-align: left;">Interrater reliability</th>
<th style="text-align: left;">Structural validity</th>
<th style="text-align: left;">Hypothesis testing</th>
<th style="text-align: left;">Content validity</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">PedsQL 4 GCS</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR33">33</span>–<span class="citation" data-cites="CR36">36</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR33">33</span>–<span class="citation" data-cites="CR42">42</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR33">33</span>, <span class="citation" data-cites="CR34">34</span>, <span class="citation" data-cites="CR40">40</span>, <span class="citation" data-cites="CR42">42</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR33">33</span>, <span class="citation" data-cites="CR36">36</span>, <span class="citation" data-cites="CR38">38</span>, <span class="citation" data-cites="CR41">41</span>, <span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR34">34</span>, <span class="citation" data-cites="CR35">35</span>, <span class="citation" data-cites="CR38">38</span>–<span class="citation" data-cites="CR42">42</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR36">36</span>, <span class="citation" data-cites="CR39">39</span>]</td>
</tr>
<tr>
<td style="text-align: left;">KIDSCREEN-10</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">KIDSCREEN-27</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>, <span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>, <span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR44">44</span>]</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">KIDSCREEN-52</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR43">43</span>]</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-Y-3L</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-Y-5L</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR45">45</span>]</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: left;">[<span class="citation" data-cites="CR46">46</span>]</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR46">46</span>]</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">PROMIS-25</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR47">47</span>]</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">[<span class="citation" data-cites="CR47">47</span>]</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

<figure id="Fig2">
<p><img src="13643_2025_3060_Fig2_HTML.jpg" id="MO1" /></p>
<p><img src="13643_2025_3060_Fig2_HTML.gif" /></p>
<figcaption>Disease conditions classification according to ICD-11 classification <em>(as more than one disease condition is included in some papers, the total number is higher than 152)</em></figcaption>
</figure>

<figure id="Fig3">
<p><img src="13643_2025_3060_Fig3_HTML.jpg" id="MO2" /></p>
<p><img src="13643_2025_3060_Fig3_HTML.gif" /></p>
<figcaption>HRQoL instruments used among children and adolescents by year of publication</figcaption>
</figure>

### Data analyses

The description of included papers was guided by the review’s research questions. Psychometric properties were categorized and reported according to the COnsensus-based Standards for the selection of health Measurement INstruments (COSMIN) categorization \[48\]. Reported disease conditions were categorized based on the International Classification of Diseases version (ICD-11) \[49\]. For the application (i.e. purpose of using the HRQoL instrument), first, the objectives of the extracted studies were examined, and three categories were identified: general HRQoL assessment, evaluation of treatment or care outcomes/assessing change for intervention (trials), and cross-cultural validation and/or psychometric studies. Then, within each paper’s reported purpose category, data were summarized descriptively with frequencies (percentages). As studies were highly heterogeneous in design, population, HRQoL instruments, and outcomes reported, narrative synthesis was used as a robust approach for presenting and interpreting the findings and identifying patterns in instrument use and psychometric evidence in relation to the review’s aims and research questions. In line with the methodological guidance of Arksey and O’Malley and the subsequent enhancement by Levac et al. \[27, 28\] of scoping review study formal quality appraisal is not mandatory, and this review aimed to map the breadth of evidence on the use, application, and reported psychometric properties of generic HRQoL instruments rather than evaluating study quality. All descriptive statistics were carried out in Microsoft Excel.

## Results

The search of six databases identified a total of 2154 potential papers. After removing duplicate papers, the number was reduced to 1484. Following title and abstract screening, 1104 papers were excluded, leaving 380 eligible for full-text review. Of these, 228 were removed after full-text review. Consequently, 152 papers reporting findings from 145 distinct studies were included in the review’s synthesis (Fig. <a href="#Fig1" data-ref-type="fig">1</a>).

<figure id="Fig1">
<p><img src="13643_2025_3060_Fig1_HTML.jpg" id="MO3" /></p>
<p><img src="13643_2025_3060_Fig1_HTML.gif" /></p>
<figcaption>PRISMA ScR flow diagram summarising literature search and selection of papers</figcaption>
</figure>

Fifteen papers reported findings from seven of the 145 distinct studies. The studies with multiple publications were conducted in India \[50–55\], Vietnam \[33, 56, 57\], Nigeria \[58, 59\], Sri Lanka \[30, 60\], and Malawi \[37, 45\].

### Characteristics of the included papers

The search sought to identify papers published from 1 January 2000 to 31 December 2024; however, all retained eligible papers were published from 2009 to 2024. Of the 152 papers, 126 (83%) were published in the last 10 years (Table <a href="#Tab1" data-ref-type="table">1</a>); 26 (19%) being published in 2024 alone.

Most of the papers reported on studies using cross-sectional designs (n = 128) \[30, 33–47, 50–160\], followed by randomized controlled trials (n = 11) \[161–171\], case–control studies (n = 8) \[172–179\], cohort studies (n = 4) \[180–183\], and there was one quasi-experimental study (n = 1) \[184\]. Only one study employed a mixed-methods approach, combining both quantitative and qualitative methods (only the quantitative results were included in this review) \[114\] (Table <a href="#Tab1" data-ref-type="table">1</a>). Participants were mostly recruited from outpatient settings (n = 70), inpatient settings (n = 16), schools (n = 46), and other community sites (e.g., homes, public parks) (n = 20). A smaller number of papers reported recruitment from both inpatient and outpatient settings (n = 6), care homes (n = 3), and specialized schools (n = 3, including two for Deaf children and one for children with intellectual disabilities). The recruitment setting was not clearly stated in 38 papers (Supplementary Data 3).

The papers covered a wide range of health conditions as well as studies focusing on healthy child and adolescent populations (Table <a href="#Tab2" data-ref-type="table">2</a>). Among the 152 papers, the most frequently reported clinical conditions were cancer (n = 22), blood disorders (n = 21), and infectious diseases (n = 18) (Fig. <a href="#Fig2" data-ref-type="fig">2</a>). Eleven (7.2%) studies focused on general child and adolescent populations; one study generated population norm data.

### Countries of origin

The 152 papers identified are from 22 of the 75 LMICs \[32\]. The majority, 129 (84.9%), were conducted in lower-middle-income countries, while the remaining 23 (15.1%) papers came from low-income countries (Supplementary Data 3). Fifty papers (32.9%) came from studies undertaken in India, 25 (16.5%) from Egypt, and the remaining coming from the 20 other countries (Supplementary Data 3). One cross-country study reported HRQoL findings from two countries (Uganda and Kenya) \[43\].

### Characteristics of participants in the included papers

The participant sample size reported in the included papers ranged from 18 \[137\] to 3227 \[111\] children and/or adolescents. Most papers reported HRQoL findings for children and adolescents aged 8–18 years (n = 65), followed by those aged 5–18 years (n = 41); 10 included children and adolescents of all age groups. Studies involving younger children, particularly those aged ≤ 4 years, were scarce. Only two papers were identified; one focusing on those aged 1 month to 2 years \[144\] and another on toddlers 2–4 years \[57\] (Supplementary Data 3).

### HRQoL instruments

Eight different generic HRQoL instruments were used in the 152 papers (Supplementary Data 4; Fig. <a href="#Fig3" data-ref-type="fig">3</a>). The most frequently used instrument was the Paediatrics Quality of Life Inventory 4.0 Generic Core Scale (PedsQL 4.0 GCS) (n = 118; 77.6%) \[185\], followed by the KIDSCREEN (n = 14; 9.2%: KIDSCREEN-10: n = 6, KIDSCREEN-27: n = 8, and KIDSCREEN-52: n = 2) \[186, 187\], the EQ-5D (n = 8; 5.3%; EQ-5D-Y-3L: n = 6, EQ-5D-Y-5L: n = 3, EQ-5D-3L: n = 1, EQ-5D-5L: n = 2) \[188–190\], the Health Utility Index (n = 5; 3.3%; HUI-2: n = 2, and HUI-3: n = 4) \[191, 192\], Paediatrics Quality of Life Inventory Short Form 15-items (PedsQL SF 15-items) (n = 3; 2.0%) \[193\], Patient-Reported Outcomes Measurement Information System-25 (PROMIS-25) (n = 2; 1.3%) \[194\], and Short Form Health Survey 36-items (SF-36) (n = 1; \< 1%) \[195\]. The two instruments developed for use in adult populations, the EQ-5D-3L/5L \[46, 160\] and SF-36 \[62\], were used in studies among adolescents aged 13–18 years and 15–18 years, respectively. The use of PedsQL instruments has increased through the years (Fig. <a href="#Fig3" data-ref-type="fig">3</a>). Among the n = 118 papers reporting use of PedsQL 4.0 GCS, 40 were from India and 23 from Egypt. Use of the EQ-5D-Y-3L/5L and EQ-5D-3L/5L instruments in LMICs has emerged more recently, with eligible papers using these instruments all being published after 2020.

### Participants completing the HRQoL instruments

Details regarding the methods of HRQoL data collection, including the respondent (child/adolescent or proxy), response mode, and administration format were obtained or derived from the papers (Supplementary Data 3). Almost all the identified generic HRQoL instruments are available for self- and proxy-report. Most papers (n = 53; 34.9%) reported both self- and proxy-reports (by parents or caregivers), followed by self-report only (n = 48; 31.6%), and proxy-report only (n = 17; 11.2%). Additionally, 21 papers (13.8%) reported the use of proxies only in certain situations, such as younger children under 7 years. Twelve papers (7.9%) did not clearly state the reporting method. Among proxy-reported HRQoL, only one paper used physicians (rather than parents/caregivers) as proxies \[84\]. Most papers used self-completed questionnaires (n = 67; 44.1%), followed by interviewer-administered format (n = 52; 34.2%) and mixed methods (self-completed and interviewer-administered) (n = 10; 6.6%). The mode of administration was unclear or not reported in 23 papers (15.1%) (Table <a href="#Tab2" data-ref-type="table">2</a>).

### Methods of instrument completion

The HRQoL instruments were administered in several ways, mainly via pen-and-paper questionnaires (n = 95; 62.5%), digital questionnaires on devices such as tablets, PCs, and smartphones (n = 9; 5.9%), telephone interviews (n = 4; 2.6%), and mixed methods (n = 4; 2.6%). The method of instrument completion was not clearly stated in 40 papers (26.3%) (Table <a href="#Tab2" data-ref-type="table">2</a>).

### Purpose of using the HRQoL instruments

Eligible retained papers were categorized into three main groups based on the primary purpose of HRQoL instrument application: general HRQoL assessment (n = 118; 77.6%), evaluation of treatment or intervention outcomes (n = 15; 9.9%), and cross-cultural adaptation and/or psychometric studies (n = 19; 12.5%) (Table <a href="#Tab2" data-ref-type="table">2</a>).

Within the general HRQoL assessment category, various purposes were reported. Papers focused on: describing HRQoL among specific clinical populations \[81, 84, 85, 91, 96, 98, 107, 108, 110, 113, 125, 129, 136, 141, 158, 179, 181, 183\], identifying factors associated with disease and/or comparing HRQoL across clinical and healthy populations \[30, 51, 55, 59–65, 67, 68, 71–74, 76, 77, 79, 86, 88–90, 92, 94, 95, 100–103, 105, 112, 114–119, 121, 122, 124, 126, 127, 132–135, 138, 139, 145–149, 151, 153–156, 159, 172, 174–178\], assessing HRQoL among healthy populations \[66, 69, 100, 106, 109, 111, 123, 131, 140, 142, 151\], comparing self- and proxy-reported outcomes \[50, 52, 54, 56, 58, 70, 74, 75, 79, 80, 83, 85, 87, 93, 97, 99, 102, 104–106, 120, 130, 173, 196\], and generating population norms \[142\].

Studies evaluating treatments or interventions used HRQoL instruments to assess physical therapies such as sensory-perceptual motor training \[161\], progressive resistance exercises \[162\], Pilates exercises \[164\], a structured physiotherapy programme \[168\], muscle stretching and isometric exercises \[169\], respiratory muscle exercises \[170\], and vestibular-specific neuromuscular training \[171\]. Other studies evaluated medical or educational interventions, including surgery \[166\], omega-3 fatty acid supplements \[182\], the impact of subcutaneous administration of emicizumab \[180\], and the effectiveness of specific educational programmes \[165, 184\].

Cross-cultural adaptation and psychometric studies were often reported as being conducted for the first time in their respective countries \[33, 34, 37, 39, 40, 42, 45–47, 137\]. Some were nested within larger studies that required instrument translation and cross-cultural adaptation \[34, 44, 83\], while some explicitly aimed to undertake psychometric testing \[160\].

### Comparison between self-reported and Proxy-reported HRQoL

One third (n = 52, 35%) of the papers reported using a combined approach of both self- and proxy-reports to gather HRQoL data, and comparison of these approaches was reported in 24 papers. In 12 (50%) of the papers investigating the relationships between self-report and proxy-report, there was moderate to excellent correlation \[56, 70, 74, 83, 97, 130, 173, 196\] or no difference between self- and proxy-reported data \[75, 80, 85, 99\]. Nevertheless, in nine (37%) of the papers, proxies (parents or caregivers) reported poorer HRQoL compared to child or adolescent self-reported HRQoL \[52, 54, 58, 87, 93, 102, 103, 105\]. Only in two papers did the proxy-parents or caregivers report a better HRQoL than the self-reported by the children or adolescents \[106, 120\].

### Reported psychometric properties of included instruments

Of the included studies, 19 reported on the cross-cultural adaptation and psychometric testing of generic HRQoL instruments. These included PedsQL 4.0 GCS \[33–42, 83, 105\], KIDSCREEN-10/27/52 \[43, 44\], EQ-5D-Y-3L, EQ-5D-Y-5L, EQ-5D-3L and EQ-5D-5L \[37, 46, 137, 160\], and PROMIS-25 \[47\]. Among these, more than half (63.2%) focused on the PedsQL 4.0 GCS. Table <a href="#Tab3" data-ref-type="table">3</a> shows the psychometric properties reported by these studies categorized using COSMIN guidelines.

Across all papers, 103 (68.0%) stated that they used a linguistically validated instrument, eight (5.0%) reported the use of instruments which had not been cross-culturally validated, and in 41 (27.0%) papers this information was not clearly stated.

Across the included papers, Cronbach’s alpha was the most frequently reported psychometric statistic in 42 (27.6%) papers, primarily for the PedsQL, KIDSCREEN, and PROMIS-25 instruments \[33–41, 43, 44, 47, 56, 57, 62, 64, 69, 70, 72–75, 99, 101, 106, 111, 119, 123, 132, 133, 140, 143, 148, 151, 155, 156, 179\]. None of the included studies reported Cronbach’s alpha for the SF-36 or EQ-5D instruments.

Of the 19 cross-cultural adaptation and/or psychometrics testing studies, reliability was reported in various forms: internal consistency using Cronbach’s alpha was reported in 14 studies \[33–44, 47, 105\], test–retest reliability measured with the intraclass correlation coefficient (ICC) was reported in five studies \[33–36, 46\], and inter-rater reliability was reported in five studies \[33, 34, 40, 42, 44\].

Some studies assessed convergent validity by examining correlation with other instruments \[36–39, 45\] or examined correlation between domains within the same instrument \[35, 40, 41, 47\]. Most of the studies evaluated known-groups validity \[33–35, 37, 38, 40–42, 44–47, 160\]. Structural validity was assessed using confirmatory factor analysis, exploratory factor analysis, or Rasch analysis in some studies \[33, 36, 38, 41, 43, 44\]. Two studies used quantitative content analysis with item-level content validity (I-CVI) and scale-level content validity (S-CVI), and face validity was reported \[36, 39, 40\]. Although linguistic validation procedures (translation and cognitive debriefing) were performed for all the instruments, none of the studies evaluated cross-cultural validity. Responsiveness (sensitivity to change) and measurement error of the instruments were not assessed in any of the studies.

### Reported strengths and limitations of included papers

Although we did not formally assess the quality of the included studies, we have summarized their reported strengths and limitations. Some papers (n = 17) reported the use of validated instruments \[30, 39, 50, 51, 60, 61, 85, 90, 97, 98, 105, 116, 143, 144, 146, 147, 178\], supporting the use of HRQoL instruments in their research contexts. The inclusion of large sample sizes \[30, 42, 53, 60, 78, 85, 91, 116, 123, 143, 144, 146, 147, 155, 196\] and achieving a balanced sample across urban–rural areas, socioeconomic status, health facilities (at different levels of the health system), and public and private schools \[89, 111, 123, 142, 159, 181, 196\] were also strengths reported in some papers. Some studies were reported for being the first of their kind within a given country or population group \[45, 47, 69, 80, 107, 119, 123, 131, 137, 159, 163\], which is also arguably a strength in terms of providing new information about the health of children and adolescents from LMICs. Additional strengths commonly reported included the use of child self-reported HRQoL \[55, 61, 111, 123\], including proxy reports by parents or caregivers \[50, 53, 85, 123, 159\], the inclusion of control groups \[53, 69, 144\], and achieving a high response rate \[80, 85, 142–144, 153, 181\].

Several limitations were also reported across the included papers, including small sample sizes \[34, 61, 63, 65, 70, 75, 83, 96, 105, 110, 113, 122, 139, 161, 162\], limited generalizability due to sampling challenges (e.g. urban vs rural areas, and single rather than multi-centre recruitment strategies) or narrow inclusion criteria (e.g. restricted age ranges such as 10–12 years) \[38–40, 43, 64, 75, 79, 83, 94, 100, 106, 111, 123, 128, 131, 143, 144, 161–163, 165, 197\].

Other methodological issues included follow-up times that were considered by the researchers to be too short \[63, 78, 161, 163\], limited consideration of relevant sociodemographic and clinical covariates (e.g. socioeconomic status, family size, family psychological relations, educational status, length of hospital stay, and disease stages) \[42, 65, 67, 78–80, 85, 114, 115, 146, 147, 164\]. Potential response bias was another limitation, particularly where proxy reports only were used or where researchers did not account for the characteristics of the reporting proxy \[56, 57, 75, 97, 98, 109, 110, 112, 117, 123, 131, 134, 173, 174, 181, 197\]. Additionally, sampling-related concerns such as using convenience sampling which may introduce selection bias \[34, 50, 53, 54, 68, 71, 80, 83, 87, 93, 112, 114, 116, 139, 153, 162, 166, 170\], recall bias \[30, 34, 60, 68, 69, 90, 96, 97, 101, 117, 123, 132, 140\], and low response rates attrition \[118, 128, 165, 174\] were also reported.

Importantly, psychometric limitations were mentioned in many papers, including the lack of evidence on test–retest reliability, linguistic validation, and responsiveness \[34, 36–38, 40, 43–47, 50, 51, 70, 81, 105, 112, 114, 122, 133, 142, 178\]. The absence of population norms \[75, 79, 94, 95, 107, 109, 112, 153\] to allow comparison with their samples, and not including proxy reports where appropriate \[81, 107\], were also noted as potential limitations.

## Discussion

To the best of our knowledge, this scoping review is the first to systematically examine the use of generic HRQoL instruments among children and adolescents in LMICs. We identified a total of 152 papers derived from 145 distinct studies across 22 countries. Interestingly, 82% of these papers were published in the last 10 years, reflecting a growing interest in evaluating HRQoL in this population. This increase reflects the recent focus on assessing the well-being of children and adolescents in LMICs \[3\], which is particularly important given the increasing proportion of children and adolescents living in LMICs \[1, 2\].

It is well established that the HRQoL of children and adolescents should be assessed using HRQoL instruments specifically developed for the respective age groups of interest \[198–200\]. In line with this, almost all studies included in this review used child-specific HRQoL instruments. A few studies (n = 3) used adult instruments (i.e., EQ-5D-3L/5L and SF-36) to assess the HRQoL of adolescents, which others have considered appropriate \[188\].

Among the eight generic HRQoL instruments identified, the PedsQL was by far the most frequently reported. This is consistent with previous reviews among Indigenous children or youth \[25\] and children with Down syndrome \[201\], where the PedsQL was also most widely used. The less frequent use of some instruments, particularly the EQ-5D-Y-3L/Y-5L, may be attributed to their relatively recent adoption in LMICs as papers reporting the use of this family of instruments were all published within the past three years \[45, 46, 71, 122, 128, 137, 160, 180\]. Furthermore, the licensing fees associated with the use of some HRQoL instruments, such as the HUI instruments, may limit their use in LMICs \[202\]. The concentration of nearly half of the eligible papers coming from only two countries may have also skewed instrument selection towards specific HRQoL instruments.

Evaluating HRQoL in children and adolescents is essential for clinical evaluation, monitoring population health, identifying hidden morbidities, and informing health policy \[15, 16, 203\]. With the growing burden of communicable and non-communicable diseases in LMICs, assessing HRQoL is vital for measuring health and prioritizing health interventions \[11, 204\]. In this review, while the increase in HRQoL research in children and adolescent populations of LMICs is encouraging, this trend was not evenly distributed across all LMIC countries; in fact, papers were identified in only 22 (29%) of 75 LMICs. As mentioned, half the papers originated from only two countries (India and Egypt). We can only hypothesize why this may be the case. For example, there may be paediatric HRQoL champions or research groups within those countries. Our findings suggest that more consideration should be given to including HRQoL assessments in future child and adolescent studies, particularly in underrepresented countries. It would be useful for future research to identify the barriers to assessing HRQoL in all LMICs, particularly given the health challenges facing children and adolescents globally, and inequitably in LMICs.

Longitudinal studies that monitor changes in HRQoL over time and identify factors affecting HRQoL outcomes are important for understanding children's and adolescents' general health, as well as the impact of specific diseases and injuries \[12–14\]. However, in this review, only four (2.6%) papers reported findings from longitudinal cohort studies and one quasi-experimental design. This suggests a paucity of research assessing changes in HRQoL over time or evaluating the long-term effects of interventions. An increase in the number of longitudinal studies in LMICs will enable the improved identification of factors affecting HRQoL, the identification of vulnerable or marginalized groups within the population, and the monitoring of population well-being. Such research would align well with the United Nations Sustainable Development Goal 3, which aims to ensure the well-being of all children \[205, 206\]. Again, it would be important to identify and address the barriers to this important longitudinal research being undertaken. We hypothesize that in some countries, the funding to support research activities is very constrained relative to need.

In the current review, although most of the included papers assessed HRQoL in children and adolescents with a range of conditions (e.g., cancer, blood disorders, and infectious diseases), very few focused on general populations, especially adolescents \[69, 109, 111, 123, 131, 140, 151\]. Only one study reported PedsQL population norm data for children and adolescents in India \[142\]. Despite the widespread use of generic HRQoL instruments in clinical settings, their application in the child and adolescent general population remains limited. Notably, in this review, the KIDSCREEN instrument was used in a few large population studies to assess HRQoL in general adolescent populations \[69, 111, 123, 140\]. KIDSCREEN and EQ-5D-Y-3L/5L have been used to generate population norm data in developed countries \[11, 207\]. Population norm data have significant public health importance, serving as essential benchmarks for monitoring health changes over time and comparing with clinical populations \[204, 208\]. Therefore, future research should also focus on general children and adolescent populations in LMICs.

Another important component to consider in assessing HRQoL is who completes the questionnaires. Where possible, HRQoL should be self-reported by children and adolescents \[198, 209\]. In this review, most studies (n = 101) used self-reported measurements, with 53 of these including both self-reports and proxy reports. This could be attributed to the fact that the majority (n = 65) of papers included those aged 8–18 years, which aligned with the recommended age limit for self-report \[210\], and proxy-reports for younger children or those with an intellectual disability \[211\]. In 17 studies, proxy-parents or caregivers’ reports were used, with one study reporting proxy data from physicians \[84\], mainly due to being younger or having an intellectual disability \[52, 57, 64, 65, 78, 113, 124, 144, 148, 149, 168, 181, 183, 197\]. In line with previous studies, discrepancies between self- and proxy-reports have also been reported in the included papers, with proxy-parent or caregiver reporting poorer HRQoL than the children themselves \[52, 54, 58, 87, 93, 102, 103, 105\], better \[106, 120\], or no significant difference \[75, 99, 165\]. These inconsistencies suggest that while prioritizing self-reports, proxy reports (where necessary) should be interpreted with caution and ideally complement child self-reports \[212\].

In terms of the administration method, a previous review recommended the use of electronic measures \[213\]. A review of the use of patient-reported outcomes measures within routine care of children and young people found that most of the reports were collected through electronic devices \[15\]. In contrast, our review found that most of the HRQoL data were collected in LMICs using pen-and-paper. Only nine papers employed electronic methods such as PCs, tablets or smartphones, mostly during the time of the COVID-19 pandemic. This finding aligns with recent evidence highlighting multiple barriers to the implementation of digital endpoints in LMICs, including limited infrastructure, affordability challenges, and technological literacy \[214\]. Our review points to the importance of the pen-and-paper method of HRQoL data collection in LMICs, ensuring inclusivity and feasibility, and future research should consider retaining it alongside digital tools to maximize data collection in LMICs.

All the instruments identified in this review were originally developed in English. Given that English is not the primary language in many LMICs, rigorous translation and cross-cultural adaptation (i.e., forward–backward translations and cognitive debriefing) are critical before their use in these settings \[215\]. Such adaptation should follow standardized guidelines to ensure conceptual, semantic, and cultural equivalence of items and response formats. Following adaptation, psychometric evaluation should be used to establish the reliability and validity of these instruments in the target population \[208, 215\]. Instruments with insufficient psychometric evidence can compromise the validity and reliability of findings, resulting in inaccurate interpretations of health outcomes \[216\]. Our review identified 19 papers that described the evaluation of five generic HRQoL instruments, yet none of the studies evaluated all nine psychometric properties recommended by the COSMIN guidelines \[48\].

Across all the instruments, key psychometric properties such as test–retest reliability, content validity, and structural validity were only sporadically reported. Moreover, psychometric properties such as measurement error and responsiveness that are essential for evaluating sensitivity to change were not reported in any of the studies. The findings of our review indicate that there is limited evidence about the psychometric properties of instruments used to assess HRQoL of children and adolescents in LMICs. The lack of comprehensive psychometric testing raises concerns about the appropriateness of using these instruments to capture HRQoL across culturally diverse populations. Future research should focus on comprehensive psychometric validation of HRQoL instruments prior to their widespread use.

## Strengths and limitations of the review

A strength of this review is the systematic search of relevant databases: Medline, Embase, PubMed, Scopus, CINAHL, and Web of Science using a rigorous dual-review screening process. The review adhered to predefined objectives and systematically mapped the use and evaluation of generic HRQoL instruments in LMICs. Additionally, the review identified the application of HRQoL instruments in the general children and adolescent populations. However, this scoping review had some limitations. As the aim of this review was to identify papers reporting generic HRQoL instruments, there will be a range of condition-specific HRQoL measures that were not within the scope of this review. Although the search was focused on major databases, literature from regional databases and grey literature may potentially have been overlooked. Restricting eligible papers to those published in English potentially excluded papers published in other languages. Although a standardized data extraction form was employed, conducting data extraction by a single reviewer may still have introduced potential errors.

### Implications of the review

- Almost all studies used HRQoL instruments that were specifically developed for or applicable to child and adolescent populations. Research was identified from only 29% of LMICs, and there is a notable lack of studies conducted in low-income countries specifically, highlighting a geographical research gap. Perhaps international collaborations could help enhance capacity building in paediatric HRQoL measurement in LMICs, including shared training, standardized methodological standards, and coordinated efforts to improve psychometric evaluation across different settings.

- Very few studies included very young children (≤ 4 years), suggesting the need to include younger age groups in future research.

- Only a small number of studies focused on general child or adolescent populations, and only one study reported population norm data.

- Evidence on the psychometric properties of the identified instruments is limited, highlighting the need for further validation studies.

## Conclusion

The use of generic HRQoL instruments to measure the health of children and adolescents in LMICs has increased in recent years. These instruments, predominantly the PedsQL, have been applied across a range of health conditions and to a lesser extent in general child and adolescent populations. However, despite their growing use, gaps remain in terms of population coverage, psychometric evidence, and the geographic distribution of countries reporting HRQoL using generic instruments. Future research should focus on culturally validating tools, psychometric testing, and generating population-level norm data to inform equitable health policies.

## Supplementary Information

<div class="caption">

Supplementary Material 1.

</div>

<div class="caption">

Supplementary Material 2.

</div>

<div class="caption">

Supplementary Material 3.

</div>

<div class="caption">

Supplementary Material 4.

</div>

## Acknowledgements

We acknowledge Christy Ballard, Health Sciences subject librarian at the University of Otago for her assistance in the development of search terms and strategies for this scoping review. We thank Gebretsadkan Gebremedhin for his counter-review of the papers through each of the screening stages.

## Abbreviations

LMICs  
Low- and middle-income countries

HRQoL  
Health-related quality of life

Prisma-ScR  
Preferred Reporting Items for Systematic Reviews and Scoping Reviews

RCTs  
Randomized controlled trials

## Authors’ contributions

Conceptualization: GM, SD, TS, AS. Data curation: GM. Methodology: GM, SD, TS, AS, MÅ, MH, GA. Formal analysis: GM. Writing original draft: GM. Writing review and editing: GM, SD, TS, AS, MÅ, MH, GA. All authors (SD, TS, AS, MÅ, MH, and GA) provided input and comments on multiple iterations of this article. All authors read and approved the final manuscript.

## Funding

This manuscript has been prepared as part of the first author’s (GM) PhD research at the University of Otago. The EuroQol Research Foundation provided GM with funding for a PhD stipend.

## Declarations

### Ethics approval and consent to participate

Ethical approval and consent to participate are not required for this scoping review as no human participants were involved in this study.

### Consent for publication

Not applicable.

### Competing interests

The authors declare they have no competing interests. Sarah Derrett, Trudy Sullivan, Mimmi Åstrom, and Michael Herdman are members of the EuroQol Group, which developed and is responsible for the EQ-5D instruments, including the EQ-5D-Y-3L and the EQ-5D-Y-5L.

## Footnotes

## References

## References

1. UNICEF. Generation 2030 Africa 2.0 Prioritizing investments in children to reap the demographic dividend. 2014, United Nations Children’s Fund: New York.

2. UNICEF. Adolescent Demographics- UNICEF Data. 2025. https://data.unicef.org/topic/adolescents/. Accessed 20 Jul 2025.

3. Shinde S, et al. Counting adolescents. In: the development of an adolescent health indicator framework for population-based settings. EClinicalMedicine. 2023;61:102067. doi:10.1016/j.eclinm.2023.102067

4. Lam CG, et al. Science and health for all children with cancer. Science. 2019;363(6432):1182–6. doi:10.1126/science.aaw4892

5. Azzopardi P. The unfinished agenda of communicable diseases among children and adolescents before the COVID-19 pandemic, 1990–2019: a systematic analysis of the Global Burden of Disease Study 2019. Lancet. 2023;402:313–35. doi:10.1016/S0140-6736(23)00860-7

6. Boyden RBJ. Understanding the lives of youth in low-income countries, in Nature. 2018:22;554(7693):435–437. doi:10.1038/d41586-018-02107-w

7. Bundy DAP, SN, Horton S, Jamison DT, Patton GC, editors. Child and adolescent health and development, in The International Bank for Reconstruction and Development 2017, World Bank: Washington, DC.

8. The Global Strategy for Women’s Children’s and Adolescents’ Health (2016–2030). Available from: https://www.who.int/docs/default-source/child-health/the-global-strategy-for-women-s-children-s-and-adolescents-health-2016-2030.pdf. Cited 28 Jul 2025. doi:10.2471/BLT.16.174714

9. World Health Organization. Sustainable development goals. 2017.

10. Revicki DA. Health-related quality of life in the evaluation of medical therapy for chronic illness. J Fam Pract. 1989;29(4):377–80.

11. Befus E-G, et al. Use of KIDSCREEN health-related quality of life instruments in the general population of children and adolescents: a scoping review. Health Qual Life Outcomes. 2023;21(1):6. doi:10.1186/s12955-023-02088-z

12. Meade T, Dowswell E. Adolescents’ health-related quality of life (HRQoL) changes over time: a three year longitudinal study. Health Qual Life Outcomes. 2016;14(1):14. doi:10.1186/s12955-016-0415-9

13. Mikkelsen HT, et al. Changes in health-related quality of life in adolescents and the impact of gender and selected variables: a two-year longitudinal study. Health Qual Life Outcomes. 2022;20(1):123. doi:10.1186/s12955-022-02035-4

14. Poon JL, Doctor JN, Nichol MB. Longitudinal changes in health-related quality of life for chronic diseases: an example in hemophilia A. J Gen Intern Med. 2014;29 Suppl 3(Suppl 3): S760–6. doi:10.1007/s11606-014-2893-y

15. Alarilla A, et al. Routine use of patient-reported experience and outcome measures for children and young people: a scoping review. Syst Rev. 2024;13(1):293. doi:10.1186/s13643-024-02706-x

16. Sitaresmi MN, et al. Health-related quality of life profile of Indonesian children and its determinants: a community-based study. BMC Pediatr. 2022;22(1):103. doi:10.1186/s12887-022-03161-0

17. Straatmann VS, et al. Changes in physical activity and screen time related to psychological well-being in early adolescence: findings from longitudinal study ELANA. BMC Public Health. 2016;16:977. doi:10.1186/s12889-016-3606-8

18. Rajmil L, et al. Socioeconomic inequalities in mental health and health-related quality of life (HRQOL) in children and adolescents from 11 European countries. Int J Public Health. 2014;59(1):95–105. doi:10.1007/s00038-013-0479-9

19. Seid M, et al. Health-related quality of life as a predictor of pediatric healthcare costs: a two-year prospective cohort analysis. Health Qual Life Outcomes. 2004;2:48. doi:10.1186/1477-7525-2-48

20. Bowling A. Measuring health: a review of quality of life measurement scales, ed. n. edition. 1997, Buckingham ; Philadelphia: Open University Press.

21. Huisman EJ, MC, Bai G, Raat H,Cnossen MH. Knowledge gaps in health-related quality of life research performed in children with bleeding disorders – A scoping review. Hemophilia. 2024;30: 295–305. doi:10.1111/hae.14941

22. Lamsal R, Finlay B, Whitehurst DGT, Zwicker JD. Generic preference-based health-related quality of life in children with neurodevelopmental disorders: a scoping review. Dev Med Child Neurol. 2020;62:169–77. doi:10.1111/dmcn.14301

23. McDool E, Powell P, Carlton J. Measuring health-related quality of life (HRQoL) in Lysosomal Storage Disorders (LSDs): a rapid scoping review of available tools and domains. Orphanet J Rare Dis. 2024;19:252. 10.1186/s13023-024-03256-0.

24. Ngwira LG, et al. A systematic literature review of preference-based health-related quality-of-life measures applied and validated for use in childhood and adolescent populations in sub-Saharan Africa. Value Health Reg Issues. 2021;25:37–47. doi:10.1016/j.vhri.2020.11.009

25. McCarty G, Wyeth E, Sullivan T, et al. Health-related quality of life measures used with Indigenous children/ youth in the Pacific Rim: a scoping review. BMJ Open 2023;13(13:e070156). doi:10.1136/bmjopen-2022-070156

26. Goitom Molalign, TS, Ari Samaranayaka, Sarah Derrett. The use of generic health-related quality of life (HRQoL) instruments among children and adolescents in low- and middle-income countries (LMICs): a scoping review protocol: a registered protocol. Article in press, 2025. doi:10.1186/s13643-025-03060-2

27. Arksey H, O’Malley L. Scoping studies: towards a methodological framework. Int J Soc Res Methodol. 2005;8(1):19–32.

28. Levac D, Colquhoun H, O’Brien KK. Scoping studies: advancing the methodology. Implementation Sci. 2010;5:69. 10.1186/1748-5908-5-69.

29. Andrea C, Tricco EL, Wasifa Zarin et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation. Ann Intern Med. 2018;169: 467–473. doi:10.7326/M18-0850

30. Ranasinghe N, et al. Functional gastrointestinal diseases and psychological maladjustment, personality traits and quality of life. BMC Gastroenterol. 2018;18:1–1. doi:10.1186/s12876-018-0760-8

31. World Health Organization and the United Nations Children’s Fund (UNICEF). Improving the health and wellbeing of children and adolescents: guidance on scheduled child and adolescent well-care visits. 2023, World Health Organization and UNICEF: Geneva.

32. WorldBank. World Bank country classifications by income level for 2024–2025 2025.

33. Trang DTH, Ha NT, Ha LTT. Validation of Vietnamese version of Pediatric quality of life inventory version 4.0 generic score scale among school children. Southeast Asian J Trop Med Public Health. 2019;50(5):942–51.

34. Arabiat D, et al. Cross-cultural validation of the Pediatric Quality of Life Inventory™ 4.0 (PedsQL™) generic core scale into Arabic language. Scand J Caring Sci. 2011;25(4):828–33. doi:10.1111/j.1471-6712.2011.00889.x

35. El-Beh K, et al. Measuring health-related quality of life in children with chronic medical conditions: reliability and validity of the Arabic version of PedsQL 4.0 generic core scales. Middle East Curr Psychiatry. 2018;25(1):16–22.

36. Melesse TG, et al. Translation and evaluation of psychometric properties of the Amharic pediatric quality of life inventory 4.0 generic core scale for children with cancer. Health Qual Life Outcomes. 2023;21(1): 1–8. doi:10.1186/s12955-022-02077-8

37. Ngwira LG, et al. Cross-cultural adaptation and psychometric validation of the Chichewa (Malawi) PedsQL(™) 4.0 generic core scales child self-report and PedsQL(™) 4.0 GCS teen self-report. J Patient Rep Outcomes. 2024;8(1):103. doi:10.1186/s41687-024-00761-5

38. Atilola O, Stevanović D. PedsQLTM 4.0 generic core scales for adolescents in the Yoruba language: translation and general psychometric properties. Clin Child Psychol Psychiatry. 2014;19(2):286–98. doi:10.1177/1359104513488375

39. Awasthi S, et al. Assessment of health-related quality of life in school-going adolescents: validation of PedsQL instrument and comparison with WHOQOL-BREF. Natl Med J India. 2012;25(2):74–9.

40. Danansuriya MN, Rajapaksa LC. Psychometric properties of the Sinhala version of the PedsQL™ 4.0 generic core scales in early adolescents in Sri Lanka. Health Qual Life Outcomes. 2012;10(1):105–12. doi:10.1186/1477-7525-10-105

41. Girma D, et al. Reliability and Validity of Ethiopian Amharic Version of the PedsQL(TM) 4.0 Generic Core Scales and PedsQL(TM) 3.0 Diabetes Module. Adolesc Health Med Ther. 2021;12:77–89. doi:10.2147/AHMT.S312323

42. Sabbah I, Sabbah H, Sabbah S, Akoum H, Droubi N, Mercier M. Measurement properties of the Arabic Lebanon version of the Pediatric Quality of Life Inventory 4.0 generic core scales for young child (5–7 years), and child aged 8–12 years: quality of life of in urban and rural children in Lebanon. Creat Educ. 2012;3:959–70.

43. Masquillier C, et al. Measuring health-related quality of life of HIV-positive adolescents in resource-constrained settings. PLoS ONE. 2012;7(7):1–8. doi:10.1371/journal.pone.0040628

44. Power R, et al. Cross-cultural validation of the Bengali version KIDSCREEN-27 quality of life questionnaire. BMC Pediatr. 2019;19(1):19. doi:10.1186/s12887-018-1373-7

45. Ngwira LG, et al. Psychometric performance of the Chichewa versions of the EQ-5D-Y-3L and EQ-5D-Y-5L among healthy and sick children and adolescents in Malawi. J Patient Rep Outcomes. 2023;7(1):22. doi:10.1186/s41687-023-00560-4

46. Welie AG, et al. Reliability and validity of using EQ-5D-5L among healthy and adolescents with major mental health disorders in Ethiopia. Eur J Health Econ. 2022;23(7):1105–19. doi:10.1007/s10198-021-01412-y

47. Westmoreland K, et al. Translation, psychometric validation, and baseline results of the Patient-Reported Outcomes Measurement Information System (PROMIS) pediatric measures to assess health-related quality of life of patients with pediatric lymphoma in Malawi. Pediatr Blood Cancer. 2018;65(11):e27353. doi:10.1002/pbc.27353

48. Mokkink LB, et al. The COSMIN study reached international consensus on taxonomy, terminology, and definitions of measurement properties for health-related patient-reported outcomes. J Clin Epidemiol. 2010;63(7):737–45. doi:10.1016/j.jclinepi.2010.02.006

49. World Health Organization. ICD-11 for mortality and morbidity statistics. 2025.

50. Gothwal VK, Bharani S, Mandal AK. Parent-child agreement on health-related quality of life in congenital glaucoma. Transl Vis Sci Technol. 2018;7(4):15. doi:10.1167/tvst.7.4.15

51. Gothwal VK, Seelam B, Mandal AK. Quality of life following surgery for congenital glaucoma: findings of the LVPEI congenital glaucoma registry. Eye (Lond). 2019;33(4):659–67. doi:10.1038/s41433-018-0293-y

52. Batra A, et al. Parents’ perspective of quality of life of retinoblastoma survivors. Pediatr Blood Cancer. 2016;63(7):1287–9. doi:10.1002/pbc.25982

53. Batra A, et al. Quality of life assessment in retinoblastoma: a cross-sectional study of 122 survivors from India. Pediatr Blood Cancer. 2016;63(2):313–7. doi:10.1002/pbc.25781

54. Bansal M, et al. Perception of Indian parents on health-related quality of life of children during maintenance therapy of acute lymphoblastic leukemia: a comparison with siblings and healthy children. J Pediatr Hematol Oncol. 2014;36(1):30–6. doi:10.1097/MPH.0b013e3182a8f23f

55. Bansal M, et al. Comparison of health-related quality of life of children during maintenance therapy with acute lymphoblastic leukemia versus siblings and healthy children in India. Leuk Lymphoma. 2013;54(5):1036–41. doi:10.3109/10428194.2012.736985

56. Tran Thi TH, Lin CY, Huang MC. Agreement between quality of life assessed using family proxy and child self-reports among children with hematologic malignancy. Eur J Pediatr. 2024;183(8):3377–88. doi:10.1007/s00431-024-05613-4

57. Tran Thi TH, Wang JD, Huang MC. Quality of life trajectories in children aged 2–4 years with acute lymphoblastic leukemia. Eur J Pediatr. 2025;184(3):202. doi:10.1007/s00431-025-06031-w

58. Salako A, et al. Parental perception of health-related quality of life of children [8-12 years] living with HIV. Central Eur J Paediatr. 2021;17(1):8–15.

59. Salako AO, et al. Health-related quality of life of children and adolescents living with HIV in Lagos, Nigeria: a cross-sectional study. Pan Afr Med J. 2022;41:344. doi:10.11604/pamj.2022.41.344.23664

60. Ranasinghe N, et al. Psychological maladjustment and quality of life in adolescents with constipation. Arch Dis Child. 2017;102(3):268–73. doi:10.1136/archdischild-2016-310694

61. Abdul-Sattar AB, et al. Determinants of health-related quality of life impairment in Egyptian children and adolescents with juvenile idiopathic arthritis: Sharkia Governorate. Rheumatol Int. 2014;34(8):1095–101. doi:10.1007/s00296-014-2950-1

62. Adeyemo TA, et al. Health related quality of life and perception of stigmatisation in adolescents living with sickle cell disease in Nigeria: a cross sectional study. Pediatr Blood Cancer. 2015;62(7):1245–51. doi:10.1002/pbc.25503

63. Afifi ZEM, et al. Quality of life of children with Phenylketonuria at primary health care center in Cairo Egypt: an exploratory cross-sectional study. Vulnerable Child Youth Stud. 2023;18(2):282–97.

64. Agrawal S, Krishnamurthy S, Naik BN. Assessment of quality of life in children with nephrotic syndrome at a teaching hospital in South India. Saudi J Kidney Dis Transpl. 2017;28(3):593–8. doi:10.4103/1319-2442.206452

65. Aier A, Pais P, Raman V. Psychosocial functioning and health-related quality of life in children with nephrotic syndrome: preliminary findings. J Indian Assoc Child Adolesc Ment Health. 2022;18(4):306–14.

66. Al-Akour NA, et al. Health-related quality of life of adolescents with overweight or obesity in the north of Jordan. Child Care Health Dev. 2011;38(2):237–43. doi:10.1111/j.1365-2214.2011.01248.x

67. Al-Nassan S, et al. Health-related quality of life among Jordanian adolescent cancer patients receiving active treatment. Asian Pac J Cancer Prev. 2019;20(10):3107–11. doi:10.31557/APJCP.2019.20.10.3107

68. Al-Smadi S, et al. Correlation between Fatigue and Quality of Life in Adolescent Oncology Patients in Jordan. Open Nurs J. 2024;18:e18744346340041.

69. Anjum A, et al. Health-related quality of life (HRQoL) and associated factors in Bangladeshi adolescents during COVID-19. Health Sci Rep. 2024;7(2):e1927. doi:10.1002/hsr2.1927

70. Anu VK, Onta M, Joshi S. Health-related quality of life of Nepalese children with leukemia using Pediatric Quality of Life Inventory 4.0 Generic Core Scale. J Pediatr Oncol Nurs. 2017;34(5):322–30. doi:10.1177/1043454217703593

71. Attuparambath S, et al. A Cross-Sectional Study Assessing the Functional Status in Children With Juvenile Idiopathic Arthritis and Its Correlation With Their Quality of Life and Burden on Caregivers. Cureus. 2024;16(8):e66178. doi:10.7759/cureus.66178

72. Ayuk A, et al. Health-related quality of life in school-aged children with and without asthma in Enugu, South East Nigeria. Niger J Paediatr. 2013;40(4):364–9.

73. Bal HS, et al. An assessment of quality of life of operated cases of esophageal atresia in the community. J Indian Assoc Pediatr Surg. 2016;21(3):131–8. doi:10.4103/0971-9261.182588

74. Banerjee T, Pensi T, Banerjee D. HRQoL in HIV-infected children using PedsQL™ 4.0 and comparison with uninfected children. Qual Life Res. 2010;19(6):803–12. doi:10.1007/s11136-010-9643-3

75. Bannink F, Idro R, Van Hove G. Health related quality of life in children with spina bifida in Uganda. Disabil Health J. 2018;11(4):650–4. doi:10.1016/j.dhjo.2018.03.008

76. Bansal D, et al. Predictors of health related quality of life in childhood epilepsy and comparison with healthy children: findings from an Indian study. Turk J Med Sci. 2017;47(2):490–8. doi:10.3906/sag-1511-148

77. Batool N, et al. Factors affecting health-related quality of life (HRQoL) in Pakistani children with thalassemia. Fam Med Prim Care Rev. 2022;24(1):37–42.

78. Batra P, et al. Assessment of quality of life during treatment of pediatric oncology patients. Indian J Public Health. 2014;58(3):168–73. doi:10.4103/0019-557X.138623

79. Bekele BT, Demie TG, Worku F. Health-related quality-of-life and associated factors among children and adolescents with type 1 diabetes mellitus: a cross-sectional study. Pediatr Health Med Ther. 2022;13:243–56. doi:10.2147/PHMT.S364454

80. Ben Abdesselem I, et al. Influencing factors of health-related quality-of-life perceived by both children/adolescents patients with type-1 diabetes mellitus and their parents: a North-African study. F1000Res. 2024;13:429. doi:10.12688/f1000research.148074.2

81. Bradley-Hewitt T, et al. The impact of echocardiographic screening for rheumatic heart disease on patient quality of life. J Pediatr. 2016;175:123–9. doi:10.1016/j.jpeds.2016.04.087

82. Caocci G, et al. Health related quality of life in Middle Eastern children with beta-thalassemia. BMC Blood Disord. 2012;12(1):6–12. doi:10.1186/1471-2326-12-6

83. Chaudhry Z, Siddiqui S. Health related quality of life assessment in Pakistani paediatric cancer patients using PedsQL™ 4.0 generic core scale and PedsQL™ cancer module. Health Qual Life Outcomes. 2012;10(1):52–9. doi:10.1186/1477-7525-10-52

84. Chirivella S, et al. Health-related quality of life among children with cancer in Hyderabad, India. Indian J Pediatr. 2009;76(12):1231–5. doi:10.1007/s12098-009-0262-3

85. Choi H, et al. Health-related quality of life of pediatric brain tumor survivors after treatment in Jordan. Neuro-Oncol Pract. 2024;11(1):82–91. doi:10.1093/nop/npad054

86. Chordiya K, et al. Quality of life (QoL) and the factors affecting it in transfusion-dependent thalassemic children. Indian J Pediatr. 2018;85(11):978–83. doi:10.1007/s12098-018-2697-x

87. Dardas LA, et al. Quality of life in Arab children with congenital heart disease. PLoS ONE. 2024;19(1):e0290306. doi:10.1371/journal.pone.0290306

88. Das S, et al. Quality of life and psychosocial functioning of HIV infected children. Indian J Pediatr. 2010;77(6):633–7. doi:10.1007/s12098-010-0087-0

89. Desalew A, et al. Health related quality of life and associated factors among children living in previous leprosarium and nonleprosarium areas of eastern Ethiopia. Sci Rep. 2024;14(1):1–11. doi:10.1038/s41598-024-73852-4

90. Devanarayana NM, Rajindrajith S, Benninga MA. Quality of life and health care consultation in 13 to 18 year olds with abdominal pain predominant functional gastrointestinal diseases. BMC Gastroenterol. 2014;14. doi:10.1186/1471-230X-14-150

91. Devi AK, et al. Long-term neurological, behavioral, functional, quality of life, and school performance outcomes in children with Guillain-Barré syndrome admitted to PICU. Pediatr Neurol. 2023;140:18–24. doi:10.1016/j.pediatrneurol.2022.11.002

92. Dhandapani M, et al. Clinical outcome, cognitive function, and quality of life after endoscopic third ventriculostomy versus ventriculo-peritoneal shunt in non-tumor hydrocephalus. Neurol India. 2021;69(Suppl):S556-s560. doi:10.4103/0028-3886.332271

93. Dhingra H, et al. A study analyzing the health-related quality of life of retinoblastoma survivors in India. Indian J Ophthalmol. 2021;69(6):1482–6. doi:10.4103/ijo.IJO_2428_20

94. Eid R, Fathy AA, Hamdy N. Health-related quality of life in Egyptian children with nephrotic syndrome. Qual Life Res. 2020;29(8):2185–96. doi:10.1007/s11136-020-02438-0

95. Eid R, et al. Health related quality of life in Juvenile-Onset systemic lupus erythematosus: a questionnaire-based study. Matern Child Health J. 2023;27(9):1578–88. doi:10.1007/s10995-023-03680-x

96. El Sehmawy AA, et al. Assessment of mental health and quality of life among children with congenital heart disease. J Pediatr Rehabil Med. 2024;17(3):307–15. doi:10.3233/PRM-220109

97. El Shafei AM, et al. Assessment of quality of life among children with end-stage renal disease: a cross-sectional study. J Environ Public Health. 2018;2018:8565498. doi:10.1155/2018/8565498

98. Ellis GK, et al. Pediatric lymphoma patients in Malawi present with poor health-related quality of life at diagnosis and improve throughout treatment and follow-up across all Pediatric PROMIS-25 domains. Pediatr Blood Cancer. 2021;68(10):e29257. doi:10.1002/pbc.29257

99. Ezzahri M, et al. Factors influencing the quality of life of Moroccan patients with juvenile idiopathic arthritis. Clin Rheumatol. 2014;33(11):1621–6. doi:10.1007/s10067-014-2489-2

100. Fagbohun AO, et al. Obesity affects health-related quality of life in schools functioning among adolescents in southwest of Nigeria. Niger J Clin Pract. 2021;24(7):1015–21. doi:10.4103/njcp.njcp_490_20

101. Gharaibeh HF, Gharaibeh MK. Factors influencing health-related quality of life of thalassaemic Jordanian children. Child Care Health Dev. 2012;38(2):211–8. doi:10.1111/j.1365-2214.2011.01224.x

102. Girma D, et al. Health-Related Quality of Life and Its Associated Factors in Children and Adolescents with Type1 Diabetes, Addis Ababa, Ethiopia. Global Pediatr Health. 2021;8(8):2333794X211030879. doi:10.1177/2333794X211030879

103. Gopakumar KG, et al. Impact of care at foster homes on the health-related quality of life of HIV-infected children and adolescents: a cross-sectional study from India. Qual Life Res. 2018;27(4):871–7. doi:10.1007/s11136-017-1726-y

104. Gopakumar KG, et al. Health-related quality of life in children with HIV infection-a cross-sectional study from South India. J Pediatr Infect Dis. 2017;12(2):104–9.

105. Gunawardana S, et al. Physical and psychosocial quality of life in children with overweight and obesity from Sri Lanka. BMC Public Health. 2021;21(1):86. doi:10.1186/s12889-020-10104-w

106. Ha NT, Trang DTH, Ha LTT. Is obesity associated with decreased health-related quality of life in school-age children?-Results from a survey in Vietnam. Aims Public Health. 2018;5(4):338–51. doi:10.3934/publichealth.2018.4.338

107. Haj-Ahmad LM, Alqaisi A, Altamimi E. Assessing the impact of celiac disease on the quality of life in Jordan. Cureus. 2024;16(11):e74395. doi:10.7759/cureus.74395

108. Hammad EEM, et al. Quality of life in cardiac patients attending Assuit University Children Hospital. Egypt J Hosp Med. 2023;91:4952–9.

109. Hashem MM, et al. Children sleep habits and their knowledge during COVID-19: the impact on quality of life. Egypt J Neurol Psychiatry Neurosurg. 2023;59(1):1–12.

110. Hashmi MM, et al. Health Related Quality of Life (HRQOL) in pediatric population after surgical intervention in traumatic lower limb injuries: A prospective cohort. Pakistan J Med Sci. 2023;39(4):1134–9. doi:10.12669/pjms.39.4.7128

111. Hunduma G, et al. Internalizing and externalizing mental health problems affect in-school adolescent’s health-related quality of life in eastern Ethiopia: a cross-sectional study. PLoS ONE. 2022;17(8):e0272651. doi:10.1371/journal.pone.0272651

112. Imani PD, et al. Chronic kidney disease impacts health-related quality of life of children in Uganda, East Africa. Pediatr Nephrol. 2021;36(2):323–31. doi:10.1007/s00467-020-04705-1

113. Ismail DK, et al. Evaluation of health-related quality of life and muscular strength in children with beta thalassemia major. Egypt J Med Hum Genet. 2018;19(4):353–7.

114. Kambasu DM, et al. Health-related quality of life of adolescents with sickle cell disease in sub-Saharan Africa: a cross-sectional study. BMC Hematol. 2019;19:9. doi:10.1186/s12878-019-0141-8

115. Kamdem F, et al. Pattern and determinants of health-related quality of life of adolescents with congenital heart disease in Cameroon: a single-center cross-sectional study. JRSM Cardiovasc Dis. 2024;13:20480040241247396. doi:10.1177/20480040241247396

116. Karnavat PK, Hegde AU, Kulkarni S. Quality of life in children with epilepsy in private and public tertiary care centers in India. Int J Epilepsy. 2018;5(1):28–37.

117. Khalil AMS, Osman FES. Psychological and social status of children treated with renal dialysis and their mothers at Tanta City. Int J Nurs Educ. 2020;12(4):275–84.

118. Kinung’hi S, et al. Infection with Schistosoma mansoni has an Effect on Quality of Life, but not on Physical Fitness in Schoolchildren in Mwanza Region, North-Western Tanzania: A Cross-Sectional Study. PLoS Neglected Tropical Dis. 2016;10(12): 1–14. doi:10.1371/journal.pntd.0005257

119. Ladak LA, et al. Health-related quality of life in surgical children and adolescents with congenital heart disease compared with their age-matched healthy sibling: a cross-sectional study from a lower middle-income country, Pakistan. Arch Dis Child. 2019;104(5):419–25. doi:10.1136/archdischild-2018-315594

120. Lang T, et al. Quality of life and psychosocial well-being among children living with HIV at a care home in Southern India. Vulnerable Child Youth Stud. 2014;9(4):345–52. doi:10.1080/17450128.2014.933942

121. Lohiya N, et al. Test anxiety among school-going children and adolescents, factors affecting and impact on quality of life: a multicenter study. Indian J Pediatr. 2021;88(9):892–8. doi:10.1007/s12098-021-03676-x

122. Hossny Elham M, RHE-O, Batoul M. Abdel Raouf*, Samia Aboajela A. Innajih. Health-related quality of life assessment using EQ-5D-Y questionnaire in a group of Egyptian asthmatic children. Egypt J Pediatr Allergy Immunol. 2020;18(1): 25–34.

123. Magai DN, Koot HM. Quality of life in children and adolescents in Central Kenya: associations with emotional and behavioral problems. Qual Life Res. 2019;28(5):1271–9. doi:10.1007/s11136-019-02099-8

124. Magai DN, et al. Long-term mental health and quality of life outcomes of neonatal insults in Kilifi, Kenya. Child Psychiatry Hum Dev. 2022;53(2):212–22. doi:10.1007/s10578-020-01079-1

125. Maher SE, Abdel-Magid RA. Assessment of health related quality of life (HRQL) in Egyptian children with rheumatic diseases; its relation to disease activity and functional disability. Int J Pediatrics-Mashhad. 2019;7(1):8795–803.

126. Mahmood S, et al. Assessment of health-related quality of life in children with osteogenesis imperfecta (OI). Prof Med J. 2024;31(6):994–8.

127. Makalo L, et al. Sociodemographic and clinical factors predictive of poor health-related quality of life of children with sickle cell anemia in The Gambia. Hemoglobin. 2024;48(6):375–83. doi:10.1080/03630269.2024.2440030

128. Mannava S, Borah RR, Shamanna BR. Measuring utility values of eye conditions among children in India using the EQ-5D-Y instrument. Health Econ Rev. 2024;14(1):1–8. doi:10.1186/s13561-024-00552-0

129. Masroor M, et al. Quality of life of children treated for split cord malformation. World Neurosurg. 2024;188:e163–7. doi:10.1016/j.wneu.2024.05.074

130. Mazahir R, Anand K, Pruthi PK. Quality of life in children with nephrotic syndrome: a cross-sectional study using Hindi version of PedsQL 4.0 generic core scales. Clin Exp Nephrol. 2022;26(6):552–60. doi:10.1007/s10157-022-02186-0

131. Mitri R, Khalife V, Ziade F. Determinants of health-related quality of life among adolescents: The role of the Mediterranean diet. Revue D Epidemiologie Et De Sante Publique. 2023;71(5):102148. doi:10.1016/j.respe.2023.102148

132. Mucunguzi D, et al. Quality of life of children after completion of surgical treatment for anorectal malformation: a single-centre cross-sectional study in south-western Uganda. J Pediatr Surg. 2025;60(1):161998. doi:10.1016/j.jpedsurg.2024.161998

133. Mwazyunga Z, et al. Health Related Quality of Life among Children with Sickle Cell Anaemia in Northwestern Tanzania. Open J Blood Dis. 2022;12(2):11–28. doi:10.4236/ojbd.2022.122002

134. Nambiar SP, et al. Predictors of quality of life (QOL) and treatment adherence among children with nephrotic syndrome. J Family Med Prim Care. 2024;13(9):3598–602. doi:10.4103/jfmpc.jfmpc_1825_23

135. Nandi M, et al. Health-related quality of life in children with juvenile idiopathic arthritis: a developing country perspective. Indian J Rheumatol. 2022;17(1):16–23.

136. Narnaware T, et al. Assessment of quality of life and long-term health-related problems among children with intracranial tumor. Nurs Midwifery Res J. 2023;19(4):222–35.

137. Ngwira LG, et al. Cross-cultural adaptation of the Beta EQ-5D-Y-5L into Chichewa (Malawi). Value Health Reg Issues. 2022;29:36–44. doi:10.1016/j.vhri.2021.09.007

138. Ogbonna-Nwosu CG, et al. Health-Related Quality of Life Among HIV-Infected Children and Its Association With Socio-Demographic, Clinical and Nutritional Variables: A Comparative Approach. Cureus J Med Sci. 2022;14(5):e25222. doi:10.7759/cureus.25222

139. Padamandala K, et al. Quality of life of retinoblastoma survivors in tertiary care eye hospital in South India. Indian J Ophthalmol. 2024;72(10):1433–41. doi:10.4103/IJO.IJO_2857_23

140. Pandit M, Margaret B, Yashoda S. Impact of Covid-19 lockdown on health-related quality of life, mental well-being, and daily routines among high school children of Udupi district, Karnataka, India: a cross-sectional study. Clin Epidemiol Glob Health. 2023;24:101452.

141. Pothiraj P, Shamal C, Krishnan V. Body image dissatisfaction, depression, and health-related quality of life amongst Indian obese school children: a cross-sectional study. J Indian Assoc Child Adolesc Ment Health. 2022;18(1):63–72.

142. Raj M, et al. Health-related quality of life in Indian children: a community-based cross-sectional survey. Indian J Med Res. 2017;145(4):521–9. doi:10.4103/ijmr.IJMR_447_16

143. Raj M, et al. Health-related quality of life (HRQOL) in children and adolescents with congenital heart disease: a cross-sectional survey from South India. BMJ Paediatr Open. 2019;3(1):e000377. doi:10.1136/bmjpo-2018-000377

144. Raj M, et al. Health-related quality of life in infants and toddlers with congenital heart disease: a cross-sectional survey from South India. Arch Dis Child. 2018;103(2):170–5. doi:10.1136/archdischild-2017-313165

145. Rajendran V, Roy FG. Comparison of health related quality of life of primary school deaf children with and without motor impairment. Ital J Pediatr. 2010;36:75. doi:10.1186/1824-7288-36-75

146. Rajindrajith S, Devanarayana NM, Benninga MA. Fecal incontinence in adolescents is associated with child abuse, somatization, and poor health-related quality of life. J Pediatr Gastroenterol Nutr. 2016;62(5):698–703. doi:10.1097/MPG.0000000000001006

147. Rajindrajith S, et al. Quality of life and somatic symptoms in children with constipation: a school-based study. J Pediatr. 2013;163(4):1069-72.e1. doi:10.1016/j.jpeds.2013.05.012

148. Saha R, Misra R, Saha I. Health related quality of life and its predictors among Bengali thalassemic children admitted to a tertiary care hospital. Indian J Pediatr. 2015;82(10):909–16. doi:10.1007/s12098-014-1670-6

149. Sasinthar K, et al. Health-related quality of life of intellectually disabled children attending a special school in Puducherry-a cross-sectional study. J Fam Med Prim Care. 2022;11(8):4549–54. doi:10.4103/jfmpc.jfmpc_520_21

150. Shah H, Dani A. A study on effect of sleep training program in children with ADHD: a comparative prospective study. J Indian Assoc Child Adolesc Ment Health. 2023;19(4):370–7.

151. Shahjalal M, et al. Madrasa student’s health-related quality of life and its associated factors: a cross-sectional study from Bangladesh. Sci Rep. 2024;14(1):17902. doi:10.1038/s41598-024-65677-y

152. Sharma S, et al. Quality of life in children with thalassemia and their caregivers in India. Indian J Pediatr. 2017;84(3):188–94. doi:10.1007/s12098-016-2267-z

153. Sims-Williams HJ, et al. Quality of life among children with spina bifida in Uganda. Arch Dis Child. 2017;102(11):1057–61. doi:10.1136/archdischild-2016-312307

154. Singh AK, et al. A comparative evaluation of quality of life and variables influencing it in children suffering from attention deficit hyperactivity disorder versus bronchial asthma: study conducted at a tertiary care centre. Int J Med Public Health. 2024;14(3):91–3.

155. Tafesse S, et al. Quality of Life and Its Associated Factors Among Children with Spina Bifida in Ethiopia: A Cross-Sectional Study to Inform Policy and Practice. World Neurosurg. 2024;189:e253–9. doi:10.1016/j.wneu.2024.06.028

156. Terer CC, et al. Evaluation of the Health-related Quality of Life of Children in Schistosoma haematobium-endemic Communities in Kenya: A Cross-sectional Study. PLoS Negl Trop Dis. 2013;7(3):1–13. doi:10.1371/journal.pntd.0002106

157. Tharwat S, Nassar MK. Musculoskeletal symptoms and their impact on health-related quality of life in chronic nonbacterial osteomyelitis patients. Pediatr Rheumatol. 2024;22(1):1–10. doi:10.1186/s12969-024-00971-7

158. Tharwat S, et al. Extraarticular manifestations of juvenile idiopathic arthritis and their impact on health-related quality of life. Clin Rheumatol. 2024;43(7):2295–305. doi:10.1007/s10067-024-07008-0

159. Thiyagarajan A, Bagavandas M, Kosalram K. Assessing the role of family well-being on the quality of life of Indian children with thalassemia. BMC Pediatr. 2019;19(1):100. doi:10.1186/s12887-019-1466-y

160. Verstraete J, et al. Transitioning between the EQ-5D youth and adult descriptive systems in a group of adolescents. J Patient Rep Outcomes. 2024;8(1):93. doi:10.1186/s41687-024-00770-4

161. Abd El-Maksoud GM, Abd-Elmonem AM, Rezk-Allah SS. Effect of individual and group sensory-perceptual motor training on motor proficiency and quality of life in children with Down syndrome. Int J Therapies Rehab Res. 2016;5(4):37–44.

162. Abd-Elmonem AM, et al. Effects of progressive resistance exercises on quality of life and functional capacity in pediatric patients with chronic kidney disease: a randomized trail. J Musculoskelet Neuronal Interact. 2019;19(2):187–95.

163. Abdelbasset WK, et al. Optimization of pulmonary function, functional capacity, and quality of life in adolescents with thoracic burns after a 2-month arm cycling exercise programme: a randomized controlled study. Burns. 2022;48(1):78–84. doi:10.1016/j.burns.2021.03.010

164. Al-Nemr A, Reffat S. Effect of Pilates exercises on balance and gross motor coordination in children with Down syndrome. Acta Neurol Belg. 2024;124(5):1499–505. doi:10.1007/s13760-024-02517-w

165. Ben Abdesselem I, et al. Effect of diabetes self-management education on health-related quality of life of Tunisian children with type1 diabetes mellitus and their parents: a randomized controlled trial. Tunis Med. 2024;102(4):205–11. doi:10.62438/tunismed.v102i4.4846

166. Dwivedi R, et al. Surgery for Drug-Resistant Epilepsy in Children. N Engl J Med. 2017;377(17):1639–47. doi:10.1056/NEJMoa1615335

167. Gupta A, et al. Evaluation of cyavanaprāśa on health and immunity related parameters in healthy children: a two arm, randomized, open labeled, prospective, multicenter, clinical study. Anc Sci Life. 2017;36(3):141–50. doi:10.4103/asl.ASL_8_17

168. Joshi S, et al. Effectiveness of structured physiotherapy in constipation in children with neurodevelopmental disorders-a randomized trial. Physiother Theory Pract. 2024;40(1):2–10. doi:10.1080/09593985.2022.2100299

169. Khalf-Allah SH, et al. Effect of muscle stretching and isometric exercises on quality of life in children undergoing regular hemodialysis. Pediatr Nephrol. 2024;39(11):3289–99. doi:10.1007/s00467-024-06398-2

170. Moawd SA, et al. Impacts of Respiratory Muscle Training on Respiratory Functions, Maximal Exercise Capacity, Functional Performance, and Quality of Life in School-Aged Children with Postoperative Congenital Diaphragmatic Hernia. Dis Markers. 2020;2020:8829373. doi:10.1155/2020/8829373

171. Rajendran V, Roy FG, Jeevanantham D. A preliminary randomized controlled study on the effectiveness of vestibular-specific neuromuscular training in children with hearing impairment. Clin Rehabil. 2013;27(5):459–67. doi:10.1177/0269215512462909

172. Allam N, Bashar A, Eid R. Assessment of health-related quality of life in Sudanese children with nephrotic syndrome: a questionnaire-based study. Pan Afr Med J. 2022;43:1–9. doi:10.11604/pamj.2022.43.154.34980

173. Atwa ZT, Wahed WYA. The impact of illness perception and socio-clinico-demographic factors on perceived quality of life in children and adolescents with thalassemia intermedia. Pediatr Blood Cancer. 2019;66(7):e27735. doi:10.1002/pbc.27735

174. Hakeem GLA, et al. Health-related quality of life in pediatric and adolescent patients with transfusion-dependent s-thalassemia in upper Egypt (single center study). Health Qual Life Outcomes. 2018;16(1):59. doi:10.1186/s12955-018-0893-z

175. Mettananda S, et al. Health related quality of life among children with transfusion dependent β-thalassaemia major and haemoglobin e β-thalassaemia in Sri Lanka: A case control study. Health Qual Life Outcomes. 2019;17(1):137. doi:10.1186/s12955-019-1207-9

176. Mikael NA, Al-Allawi NAS. Factors affecting quality of life in children and adolescents with Thalassemia in Iraqi Kurdistan. Saudi Med J. 2018;39(8):799–807. doi:10.15537/smj.2018.8.23315

177. Nguyen SN, et al. First report on health-related quality of life among children with chronic immune thrombocytopenia in Vietnam. Clin Epidemiol Glob Health. 2021;12:100914.

178. Power R, et al. Health-related quality of life of adolescents with cerebral palsy in rural Bangladesh. PLoS ONE. 2018;14(6):e0217675. doi:10.1371/journal.pone.0217675

179. Rugemalira E, et al. Health-related quality of life after childhood bacterial meningitis. Pediatr Infect Dis J. 2021;40(11):987–92. doi:10.1097/INF.0000000000003243

180. Hassan AS, et al. Health-related quality of life in children with severe hemophilia A on emicizumab prophylaxis. Egypt J Haematol. 2024;49(2):192–6.

181. Jagnoor J, et al. Health-Related Quality of Life and Function after Paediatric Injuries in India: A Longitudinal Study. Int J Environ Res Public Health [Electronic Resource]. 2017;14(10):28. doi:10.3390/ijerph14101144

182. Kasemy ZA, et al. Effect of omega-3 supplements on quality of life among children on dialysis: a prospective cohort study. Medicine (Baltimore). 2020;99(40):e22240. doi:10.1097/MD.0000000000022240

183. Khalil M, et al. Quality of life in children operated for spina bifida; low- and middle-income country perspective. Childs Nerv Syst. 2023;39(11):3155–61. doi:10.1007/s00381-023-05993-2

184. K K, P A, Sikandar BJ. Impact of SCOPE Program on Health-Related Quality of Life and Health Status of Children With Thalassemia: A Quasi-Experimental Study. J Pediatr Hematol Oncol Nurs. 2024;41(3):199–211. doi:10.1177/27527530231214542

185. Varni JW, Seid M, Rode CA. The pedsQL™: measurement model for the pediatric quality of life inventory. Med Care. 1999;37(2):126–39. doi:10.1097/00005650-199902000-00003

186. Ravens-Sieberer U, et al. The KIDSCREEN-52 quality of life measure for children and adolescents: psychometric results from a cross-cultural survey in 13 European countries. Value Health. 2008;11(4):645–58. doi:10.1111/j.1524-4733.2007.00291.x

187. Ravens-Sieberer U, et al. The European KIDSCREEN approach to measure quality of life and well-being in children: development, current application, and future advances. Qual Life Res. 2014;23(3):791–803. doi:10.1007/s11136-013-0428-3

188. EuroQol Research Foundation. EQ-5D-5L User Guide. 2025.

189. Kreimeier S, et al. EQ-5D-Y-5L: developing a revised EQ-5D-Y with increased response categories. Qual Life Res. 2019;28(7):1951–61. doi:10.1007/s11136-019-02115-x

190. Wille N, et al. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual Life Res. 2010;19(6):875–86. doi:10.1007/s11136-010-9648-y

191. Feeny D, et al. Multi-attribute health status classification systems. Pharmacoeconomics. 1995;7(6):490–502. doi:10.2165/00019053-199507060-00004

192. Richardson J, McKie J, Bariola E. Multiattribute Utility Instruments and Their Use. In: Culyer AJ, editor. Encyclopedia of Health Economics. San Diego: Elsevier; 2014. p. 341–57.

193. Chan KS, et al. The PedsQL: reliability and validity of the short-form generic core scales and asthma module. Med Care. 2005;43(3):256–65. doi:10.1097/00005650-200503000-00008

194. Forrest CB, et al. Commentary: the patient-reported outcome measurement information system (PROMIS®) for children and youth: application to pediatric psychology. J Pediatr Psychol. 2012;37(6):614–21. doi:10.1093/jpepsy/jss038

195. Ware JE Jr, Sherbourne CD. The MOS 36-item short-form health survey (SF-36). I. Conceptual framework and item selection. Med Care. 1992;30(6):473–83.

196. Agrawal A, et al. Quality of life is impaired in children with chronic pancreatitis: A multicenter study. Pancreatology. 2024;24(6):817–26. doi:10.1016/j.pan.2024.06.009

197. Jahan MU, et al. Cognitive Functions and Health Related Quality of Life of Institutional Autism Spectrum Disorder Children in Dhaka city. Bangladesh Med Res Counc Bull. 2015;41(3):151–9. doi:10.3329/bmrcb.v41i3.29973

198. Ravens-Sieberer U, Erhart M, Wille N, et al. Generic health-related quality-of-life assessment in children and adolescents methodological considerations. Pharmacoeconomics. 2006;24:1199–220. doi:10.2165/00019053-200624120-00005

199. Matza LS, et al. Pediatric patient-reported outcome instruments for research to support medical product labeling: report of the ISPOR PRO good research practices for the assessment of children and adolescents task force. Value Health. 2013;16(4):461–79. doi:10.1016/j.jval.2013.04.004

200. U.S. FDA. Guidance for industry: patient-reported outcome measures: use in medical product development to support labeling claims: draft guidance. Health Qual Life Outcomes. 2006;4:79. doi:10.1186/1477-7525-4-79

201. Rodríguez-Grande E-I, et al. Instruments for the assessment of quality of life in children and adolescents with Down syndrome: a scoping review. BMC Pediatr. 2024;24(1):688. doi:10.1186/s12887-024-05028-y

202. Horsman J, et al. The health utilities index (HUI): concepts, measurement properties and applications. Health Qual Life Outcomes. 2003;1:54. doi:10.1186/1477-7525-1-54

203. Varni JW, Burwinkle TM, Lane MM. Health-related quality of life measurement in pediatric clinical practice: an appraisal and precept for future research and application. Health Qual Life Outcomes. 2005;3(1):34. doi:10.1186/1477-7525-3-34

204. Szende A, Janssen B, Cabases J. Self-reported population health: An international perspective based on EQ-5D. New York: Springer Open. 2014, New York: Springer Open.

205. Clark H, et al. A future for the world’s children? A WHO–UNICEF–<em>Lancet</em> Commission. The Lancet. 2020;395(10224):605–58. doi:10.1016/S0140-6736(19)32540-1

206. World Health Organization. Sustainable development goals. 2017. Accessed 15 Jul 2025.

207. Åström M, et al. Population health status based on the EQ-5D-Y-3L among adolescents in Sweden: results by sociodemographic factors and self-reported comorbidity. Qual Life Res. 2018;27(11):2859–71. doi:10.1007/s11136-018-1985-2

208. Chen TH, Li L, Kochen MM. A systematic review: how to choose appropriate health-related quality of life (HRQOL) measures in routine general practice? J Zhejiang Univ Sci B. 2005;6(9):936–40. doi:10.1631/jzus.2005.B0936

209. Khanna D, et al. Are we agreed? Self- versus proxy-reporting of paediatric health-related quality of life (HRQoL) using generic preference-based measures: a systematic review and meta-analysis. Pharmacoeconomics. 2022;40(11):1043–67. doi:10.1007/s40273-022-01177-z

210. Riley AW. Evidence that school-age children can self-report on their health. Ambul Pediatr. 2004;4(4):371–6. doi:10.1367/A03-178R.1

211. Guyatt GHFD, Patrick DL. Measuring health-related quality of life. Ann Intern Med. 1993;118(8):622–9. doi:10.7326/0003-4819-118-8-199304150-00009

212. Pickard AS, Knight SJ. Proxy evaluation of health-related quality of life: a conceptual framework for understanding multiple proxy perspectives. Med Care. 2005;43(5):493–9. doi:10.1097/01.mlr.0000160419.27642.a8

213. Coombes L, et al. Enhancing validity, reliability and participation in self-reported health outcome measurement for children and young people: a systematic review of recall period, response scale format, and administration modality. Qual Life Res. 2021;30(7):1803–32. doi:10.1007/s11136-021-02814-4

214. Al Meslamani AZ. Barriers to digital endpoints in data collection in low and middle-income countries. Expert Rev Pharmacoecon Outcomes Res. 2024;24(6):701–3. doi:10.1080/14737167.2024.2331047

215. Cruchinho P, et al. Translation, cross-cultural adaptation, and validation of measurement instruments: a practical guideline for novice researchers. J Multidiscip Healthc. 2024;17:2701–28. doi:10.2147/JMDH.S419714

216. Gagnier JJ, Johnston BC. Poor quality patient reported outcome measures bias effect estimates in orthopaedic randomized studies. J Clin Epidemiol. 2019;116:36–8. doi:10.1016/j.jclinepi.2019.07.012

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary Material 1.

</div>

<div class="caption">

Supplementary Material 2.

</div>

<div class="caption">

Supplementary Material 3.

</div>

<div class="caption">

Supplementary Material 4.

</div>

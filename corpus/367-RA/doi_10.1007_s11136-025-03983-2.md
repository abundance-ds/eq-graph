---
project_id: "367-RA"
work_id: "doi:10.1007/s11136-025-03983-2"
doi: "10.1007/s11136-025-03983-2"
pmid: "40317454"
pmcid: "PMC12689827"
title: "EuroQol data for assessment of population health needs and instrument evaluation (EQ-DAPHNIE): a study for enhancing population health assessment"
journal: "Quality of Life Research"
publication_date: "2025-05-03"
volume: "34"
issue: "12"
authors:
  - name: "Jeffrey A Johnson"
    affiliation_ids:
      - "Aff1"
  - name: "Mathieu F Janssen"
    affiliation_ids:
      - "Aff2"
  - name: "Fatima Al Sayah"
    affiliation_ids:
      - "Aff3"
  - name: "Henry Bailey"
    affiliation_ids:
      - "Aff4"
  - name: "Mihir Gandhi"
    affiliation_ids:
      - "Aff5"
  - name: "Dominik Golicki"
    affiliation_ids:
      - "Aff6"
  - name: "Nils Gutacker"
    affiliation_ids:
      - "Aff7"
  - name: "Erica Lubetkin"
    affiliation_ids:
      - "Aff8"
  - name: "Brendan Mulhern"
    affiliation_ids:
      - "Aff9"
  - name: "Fredrick Dermawan Purba"
    affiliation_ids:
      - "Aff10"
  - name: "Juan M Ramos-Goñi"
    affiliation_ids:
      - "Aff11"
  - name: "Desiree Scott"
    affiliation_ids:
      - "Aff12"
  - name: "Hilary Short"
    affiliation_ids:
      - "Aff3"
  - name: "Trudy Sullivan"
    affiliation_ids:
      - "Aff13"
  - name: "Rosalie Viney"
    affiliation_ids:
      - "Aff9"
  - name: "Zhihao Yang"
    affiliation_ids:
      - "Aff14"
  - name: "Victor Zárate"
    affiliation_ids:
      - "Aff15"
affiliations:
  - id: "Aff1"
    name: "School of Public Health, University of Alberta, Edmonton, AB Canada"
  - id: "Aff2"
    name: "EuroQol Research Foundation, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "University of Alberta, Edmonton, Canada"
  - id: "Aff4"
    name: "The University of the West Indies, St. Augustine, Trinidad and Tobago"
  - id: "Aff5"
    name: "Duke-NUS Medical School, Singapore, Singapore"
  - id: "Aff6"
    name: "Medical University of Warsaw, Warszaw, Poland"
  - id: "Aff7"
    name: "Centre for Health Economics, University of York, York, UK"
  - id: "Aff8"
    name: "CUNY School of Medicine, New York, USA"
  - id: "Aff9"
    name: "University of Technology Sydney, Sydney, Australia"
  - id: "Aff10"
    name: "Universitas Padjadjaran, Jatinangor, Indonesia"
  - id: "Aff11"
    name: "Decision Analysis and Support Unit, SGH, Warsaw School of Economics, Warszaw, Poland"
  - id: "Aff12"
    name: "University of Cape Town, Cape Town, South Africa"
  - id: "Aff13"
    name: "University of Otago, Dunedin, New Zealand"
  - id: "Aff14"
    name: "Guizhou Medical University, Guiyang, China"
  - id: "Aff15"
    name: "Merck & Co., Santiago, Chile"
licence: "cc-by-nc-nd"
source_file: "input/projects/367-RA/papers/doi_10.1007_s11136-025-03983-2.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12689827/fullTextXML"
source_method: "epmc_xml"
source_sha256: "d206123f5d69763c576d3ea181736ec840ad6376a6721bbb82ec054dd0a2f5fb"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# EuroQol data for assessment of population health needs and instrument evaluation (EQ-DAPHNIE): a study for enhancing population health assessment

## Abstract

### Background

Methods for collecting self-reported health status measures in population health surveys vary significantly across countries, presenting challenges to comparability. The EuroQol Data for Assessment of Population Health Needs and Instrument Evaluation (EQ-DAPHNIE) project aims to address this issue by developing infrastructure to generate representative datasets across multiple countries. This initiative aims to standardize data collection methodologies and to evaluate the performance of various health status measures, providing a foundation for reliable population health assessments. This paper describes the rationale, design and data collection methods for the EQ-DAPHNIE project.

### Methods/design

EQ-DAPHNIE employs a cross-sectional online survey design targeting the general adult population across various countries. Participants were recruited through an online panel provider. Each country had a target sample of 4500 responses, with quota sampling to ensure representativeness based on age, sex, income, region, and language. The survey collected comprehensive data on social determinants of health at both individual and neighbourhood levels. Participation was voluntary, and measures were taken to maintain data anonymity and ensure data quality through pre-testing and various quality assurance approaches.

### Discussion

The EQ-DAPHNIE project represents a significant advancement in generating large, representative, and comparable population health datasets across multiple countries. By employing precise sampling strategies, robust recruitment and data collection methods, and rigorous quality control measures, the project aims to provide a valuable resource for assessing and understanding population health and evaluating various health-related quality of life (HRQoL) and wellbeing instruments.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-025-03983-2.

**Keywords:** EQ-5D, EQ-HWB, PROMIS-10, WHO-5, ASCOT, ICECAP-A, Population health assessment, Instrument comparison

Accepted 2025 Apr 21; Issue date 2025.

## Background

International population health surveys are essential for understanding global health trends and informing policy decisions. Given the diverse health systems, cultural practices, and socio-economic conditions across different countries, standardizing data collection methods is essential to ensure comparability. However, methods used in generating survey data and population health norms vary considerably across countries, making data less comparable \[1–3\]. Standardization minimizes biases and errors, ensuring data is accurate and reliable. This precision enables an accurate reflection of population health worldwide and facilitates meaningful cross-country comparisons, which is essential for identifying global health inequalities \[4, 5\]. However, standardizing data collection poses several challenges such as ensuring cultural sensitivity, managing technological variability, and navigating ethical and legal constraints in different regions. Addressing these challenges through careful planning, cultural adaptation, and capacity building is essential.

Self-reported measures of health status, quality of life, and wellbeing have long been essential components of population health surveys. These instruments provide valuable insights into how individuals perceive their physical and mental health, daily functioning, and overall satisfaction with life. By asking individuals to evaluate their own health, researchers can gather subjective data that complements objective health indicators such as disease prevalence and mortality rates, enriching the overall understanding of population health \[6, 7\]. Instruments such as the EQ-5D-5L \[8\], Patient-Reported Outcomes Measurement Information System Global Health Scale (PROMIS-10) \[9\], World Health Organisation-Five Well-Being Index (WHO-5) \[10\], and Adult Social Care Outcomes Toolkit (ASCOT) \[11\] have been widely used to assess health-related quality of life (HRQoL), capturing dimensions like physical functioning, pain, emotional wellbeing, and social support. These measures are crucial for understanding the broader impact of health conditions on people’s lives, informing public health policies and interventions aimed at improving population-level wellbeing.

Numerous international initiatives have incorporated these health status measures. Examples include the Organisation for Economic Co-operation and Development (OECD) Patient-Reported Indicator Surveys (PaRIS) \[12\], the Covid-19 vAccine preference anD Opinion sURvey (CANDOUR) Study \[13\], the POPulation health impact of the CORoNavirus (POPCORN) Study \[14\], and the Commonwealth Fund International Health Policy Survey of Older Adults \[15\]. These efforts highlight the value of such measures in enabling cross-country comparisons and facilitating the evaluation of various health instruments. The Multi Instrument Comparison (MIC) project \[16\], for example, collected data from 12 health status measures across six countries, targeting seven chronic disease areas, and providing valuable insights for researchers or evaluators in selecting the most appropriate quality of life instrument for specific conditions \[17\]. However, while these efforts are significant, no initiative has yet combined the broad objectives of population health assessment and instrument comparison with the same scale in terms of sample size and countries involved, and the range of data collected.

The EQ-DAPHNIE project aims to establish infrastructure for generating representative datasets of the general adult population across multiple countries, aimed at measuring population health status and evaluating the performance of standardized health status measures. Ensuring standardization of data collection methods, data quality, and representativeness of these datasets is critical for the validity and generalizability of the findings using the EQ-DAPHNIE infrastructure. This paper describes the rationale, design and data collection methods for the EQ-DAPHNIE project.

## Methods

### Setting and population

A cross-sectional online survey design was employed, targeting the general adult population in each country, with a goal of obtaining 4,500 responses per country. The survey was conducted in two rounds following a pilot study. The first round targeted five predominantly English-speaking countries: Australia, Canada, New Zealand, the United Kingdom (UK), and the United States (US). The second round expanded to ten additional countries that required language adaptations: Argentina, Brazil, Chile, China, France, Germany, Japan, Mexico, the Netherlands, and Spain. Future rounds will continue expanding the EQ-DAPHNIE data collection to include countries from other regions such as Africa, the Middle East, and East Asia.

Participants were recruited through international online research panels managed by Dynata ([www.dynata.com](http://www.dynata.com)), a provider with panelists spanning 90 countries recruited through websites, social media, and direct email to participants in various consumer brand loyalty programs. Each recruitment channel delivers a different population, providing diversity, representativeness and enabling hard-to-reach population segments. While there are some drawbacks to online sampling, there are also many advantages such as time and cost to recruit large, diverse samples quickly \[18\]. Potential issues in online sampling, such as sample representativeness, have been addressed in our study design using quota sampling, described later, as well as post-stratification weighting. Participation in this study was voluntary and open to adult participants ≥ 18 years who are a member of a panel. An invitation to the study was emailed to participants individually using an automated router. Participants access the survey link via their Dynata dashboard. Additionally, panelists who log into their Dynata account during the study period were directed to the survey if they fit the targeted quotas. Enrollment into the survey within each stratum was on a first-come, first-serve basis. Participants were awarded on a point-based system by Dynata, meaning panelists accumulate points by completing surveys which can be redeemed for gift cards, airline miles, or other prizes. A control system prevents unauthorized access to the survey questionnaire, and duplicate records from the same participant were not permitted. Dynata’s comprehensive panels and point-based incentive system enhances participation rates and ensures a diverse pool of respondents \[19\].

### Country selection and sample size

The project team employed a modified Delphi approach to reach a consensus on the number of countries to target and the sample size for each. After careful deliberation, the team considered two main strategies: targeting fewer countries with larger sample sizes or including more countries with smaller sample sizes, while considering constraints of budget and time. Through this approach, it was decided that each of the 15 countries selected for rounds 1 and 2 would have a sample of 4500 participants who complete the entire survey. The countries were chosen based on factors such as feasibility, geographical diversity, representativeness, and alignment with research interests and priorities of the EuroQol Group.

### Eligibility criteria

Any panelists who were ≥ 18 years in their country of residence and willing and able to complete the survey were eligible to participate in this study.

### Sampling strategy

Survey data were collected anonymously through a web-based platform, LimeSurvey (version 5+). Maths in Health ([www.mathsinhealth.com](http://www.mathsinhealth.com)) was contracted to manage the server infrastructure, survey programming within LimeSurvey, and coordinate with Dynata, the data collection agency.

A quota sampling design was implemented to ensure that each country’s sample was representative of the general population. Quotas were based on census or national datasets from 2020 to 2023, with specific targets for age, sex, household income (monthly or annually, depending on country), and area of residence (i.e., rural and urban residents). In countries with multiple official languages (e.g., Canada, the US), quotas were set according to the proportion of population speaking each language. Data collection in each country was targeted to span a 6-week period, with quota controls relaxed at the 5-week mark if quotas had not been met, aiming to achieve a minimum of 85% adherence to each quota threshold.

Before starting the survey, participants were presented with an information letter detailing the study and were required to provide their consent to proceed. Only individuals who could provide their own consent were eligible for participation. Participants had the option to withdraw from the survey at any time. However, to maintain anonymity, once a survey was submitted, it could not be retracted. Participants who did not complete the survey were not included in the final sample count.

The online survey was designed, pre-tested, and administered using Dynata’s services in conjunction with Maths in Health’s LimeSurvey platform. Before official launch in each country, our team conducted usability and technical functionality tests to ensure the survey operated smoothly. During the soft launch phase, we collected an initial sample of 250 responses, which were thoroughly reviewed by our team before proceeding with the full-scale launch.

### Study survey

A standardized core questionnaire was administered across all participating countries, with an estimated average completion time of around 20 minutes. The survey is organized into four sections: social determinants of health, health status and wellbeing, health behaviors and habits, and use of health services and insurance coverage. The study survey was developed by the EQ-DAPHNIE Project Team using a modified Delphi method for selecting measures and variables. Details of the survey components within each section are outlined in Table <a href="#Tab1" data-ref-type="table">1</a>**.**

<div id="Tab1" class="table-wrap">

<div class="caption">

Overview of EQ-DAPHNIE survey content

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Survey section</th>
<th style="text-align: left;">Variables or measures</th>
<th style="text-align: left;">Source</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="23" style="text-align: left;">Section 1: Social determinants of health</td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td style="text-align: left;">Gender</td>
<td style="text-align: left;">Health Quality Council of Alberta (HQCA). COVID-19 Continuing Care Study. 2021; <a href="https://hqca.ca/reports/covid-19-continuing-care-study/">https://hqca.ca/reports/covid-19-continuing-care-study/</a></td>
</tr>
<tr>
<td style="text-align: left;">Marital status</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Education (Modified International Standard Classification of Education ISCED 2011)</td>
<td style="text-align: left;">UNESCO Institute for Statistics. <em>International Standard Classification of Education ISCED 2011.</em> 2012</td>
</tr>
<tr>
<td style="text-align: left;">Number of years of education</td>
<td style="text-align: left;">Statistics Canada. Classifications, variables and statistical units. 2021; <a href="https://www.statcan.gc.ca/en/concepts/search#dataset-filter1">https://www.statcan.gc.ca/en/concepts/search#dataset-filter1</a></td>
</tr>
<tr>
<td style="text-align: left;">Employment</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. British Household Panel Survey. [data series]. 3rd Release. UK Data Service. SN: 200,005. 2023</td>
</tr>
<tr>
<td style="text-align: left;">Total annual household income</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Financial deprivation</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Ethnicity</td>
<td style="text-align: left;">Canadian Institute for Health Information. <em>Guidance on the Use of Standards for Race-Based and Indigenous Identity Data Collection and Health Reporting in Canada.</em> Ottawa, ON: CIHI; 2022</td>
</tr>
<tr>
<td style="text-align: left;">Country born</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td style="text-align: left;">Years lived in country</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td style="text-align: left;">Region of residence (province/territory/state)</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td style="text-align: left;">Area of residence (urban/suburban/rural)</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Household size</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Children in household</td>
<td style="text-align: left;">Health Quality Council of Alberta (HQCA). COVID-19 Continuing Care Study. 2021; <a href="https://hqca.ca/reports/covid-19-continuing-care-study/">https://hqca.ca/reports/covid-19-continuing-care-study/</a></td>
</tr>
<tr>
<td style="text-align: left;">Financial hardship in childhood</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Domestic conflict in childhood</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Food Insecurity (Hunger Vital Sign 2-item screening tool)</td>
<td style="text-align: left;">Gattu RK, Paik G, Wang Y, Ray P, Lichenstein R, Black MM. The Hunger Vital Sign Identifies Household Food Insecurity among Children in Emergency Departments and Primary Care. <em>Children (Basel).</em> 2019;6(10)</td>
</tr>
<tr>
<td style="text-align: left;">Social deprivation</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Immigration status</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Minority status</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Religion</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td rowspan="17" style="text-align: left;">Section 2: Overall health and wellbeing</td>
<td style="text-align: left;">EQ-5D-5L</td>
<td style="text-align: left;">Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). <em>Qual Life Res.</em> 2011;20(10):1727–1736</td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L bolt-ons</td>
<td style="text-align: left;"><p>Finch AP, Brazier J, Mukuria C. Selecting Bolt-on Dimensions for the EQ-5D: Testing the Impact of Hearing, Sleep, Cognition, Energy, and Relationships on Preferences Using Pairwise Choices. <em>Medical Decision Making.</em> 2021;41(1):89–99</p>
<p>Rencz F, Janssen MF. Testing the Psychometric Properties of 9 Bolt-Ons for the EQ-5D-5L in a General Population Sample. <em>Value in Health.</em> 2024;27(7):943–954</p>
<p>Hoogendoorn M, Oppe M, Boland MRS, Goossens LMA, Stolk EA, Rutten–van Mölken MPMH. Exploring the Impact of Adding a Respiratory Dimension to the EQ-5D-5L. <em>Medical Decision Making.</em> 2019;39(4):393–404</p>
<p>Geraerds AJLM, Bonsel GJ, Janssen MF, et al. The added value of the EQ-5D with a cognition dimension in injury patients with and without traumatic brain injury. <em>Quality of Life Research.</em> 2019;28(7):1931–1939</p>
<p>Swinburn P, Lloyd A, Boye KS, Edson-Heredia E, Bowman L, Janssen B. Development of a Disease-Specific Version of the EQ-5D-5L for Use in Patients Suffering from Psoriasis: Lessons Learned from a Feasibility Study in the UK. <em>Value in Health.</em> 2013;16(8):1156–1162</p></td>
</tr>
<tr>
<td style="text-align: left;">EQ-5D-5L response-scale heterogeneity vignette</td>
<td style="text-align: left;">Knott RJ, Black N, Hollingsworth B, Lorgelly PK. Response-Scale Heterogeneity in the EQ-5D. <em>Health Economics.</em> 2017;26(3):387–394</td>
</tr>
<tr>
<td style="text-align: left;"><strong>EQ-HWB*</strong></td>
<td style="text-align: left;">Brazier J, Peasgood T, Mukuria C, et al. The EQ-HWB: Overview of the Development of a Measure of Health and Wellbeing and Key Results. <em>Value in Health.</em> 2022;25(4):482–491</td>
</tr>
<tr>
<td style="text-align: left;"><strong>PROMIS-10</strong></td>
<td style="text-align: left;">Hays RD, Bjorner JB, Revicki DA, Spritzer KL, Cella D. Development of physical and mental health summary scores from the patient-reported outcomes measurement information system (PROMIS) global items. <em>Qual Life Res</em> 2009; 18: 873 – 880</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ASCOT* or ICECAP-A*</strong></td>
<td style="text-align: left;"><p>Rand S, Malley J, Towers A-M, Netten A, Forder J. Validity and test–retest reliability of the self-completion adult social care outcomes toolkit (ASCOT-SCT4) with adults with long-term physical, sensory and mental health conditions in England. <em>Health and Quality of Life Outcomes.</em> 2017;15(1):163</p>
<p>Al-Janabi H, N Flynn T, Coast J. Development of a self-report measure of capability wellbeing for adults: the ICECAP-A. <em>Quality of Life Research.</em> 2012;21(1):167–176</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>WHO-5</strong></td>
<td style="text-align: left;">Topp CW, Østergaard SD, Søndergaard S, Bech P. The WHO-5 Well-Being Index: A Systematic Review of the Literature. <em>Psychotherapy and Psychosomatics.</em> 2015;84(3):167–176</td>
</tr>
<tr>
<td style="text-align: left;"><strong>OPQOL-brief (for respondents 65 + only)</strong></td>
<td style="text-align: left;">Bowling A, Hankins M, Windle G, Bilotta C, Grant R. A short measure of quality of life in older age: the performance of the brief Older People’s Quality of Life questionnaire (OPQOL-brief). <em>Arch Gerontol Geriatr.</em> 2013;56(1):181–187</td>
</tr>
<tr>
<td style="text-align: left;"><strong>PHQ-2</strong></td>
<td style="text-align: left;">Kroenke K, Spitzer RL, Williams JB. The Patient Health Questionnaire-2: validity of a two-item depression screener. <em>Med Care.</em> 2003;41(11):1284–1292</td>
</tr>
<tr>
<td style="text-align: left;"><strong>GAD-2</strong></td>
<td style="text-align: left;">Skapinakis P. The 2-item Generalized Anxiety Disorder scale had high sensitivity and specificity for detecting GAD in primary care. <em>Evid Based Med.</em> 2007;12(5):149</td>
</tr>
<tr>
<td style="text-align: left;">Physical disability</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Mental disability</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Chronic conditions</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Medications</td>
<td style="text-align: left;">Goldsworthy RC, Schwartz NC, Mayhorn CB. Beyond abuse and exposure: framing the impact of prescription-medication sharing. <em>Am J Public Health.</em> 2008;98(6):1115–1121</td>
</tr>
<tr>
<td style="text-align: left;">Long COVID-19 status</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td style="text-align: left;">Height</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td style="text-align: left;">Weight</td>
<td style="text-align: left;">Author derived</td>
</tr>
<tr>
<td rowspan="7" style="text-align: left;">Section 3: Health behaviours and habits</td>
<td style="text-align: left;">Physical activity</td>
<td style="text-align: left;">Smith BJ, Marshall AL, Huang N. Screening for physical activity in family practice: evaluation of two brief assessment tools. <em>Am J Prev Med.</em> 2005;29(4):256–264</td>
</tr>
<tr>
<td style="text-align: left;">Sedentary time (Global Physical Activity Questionnaire single item of sedentary activity)</td>
<td style="text-align: left;">Cleland CL, Hunter RF, Kee F, Cupples ME, Sallis JF, Tully MA. Validity of the Global Physical Activity Questionnaire (GPAQ) in assessing levels and change in moderate-vigorous physical activity and sedentary behaviour. <em>BMC Public Health.</em> 2014;14(1):1255</td>
</tr>
<tr>
<td style="text-align: left;">Dietary habits (Summary of Diabetes Self-Care Activities Measure)</td>
<td style="text-align: left;">Toobert DJ, Hampson SE, Glasgow RE. The summary of diabetes self-care activities measure: results from 7 studies and a revised scale. <em>Diabetes Care.</em> 2000;23(7):943–950</td>
</tr>
<tr>
<td style="text-align: left;">Sleep quality (PROMIS Short Form v1.0 – Sleep Disturbance 4a)</td>
<td style="text-align: left;">Yu L, Buysse DJ, Germain A, et al. Development of short forms from the PROMIS™ sleep disturbance and Sleep-Related Impairment item banks. <em>Behav Sleep Med.</em> 2011;10(1):6–24</td>
</tr>
<tr>
<td style="text-align: left;">Smoking habits</td>
<td style="text-align: left;">National Health Service (NHS). Health Survey for England, 2021 part 1. 2022; <a href="https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england/2021">https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england/2021</a></td>
</tr>
<tr>
<td style="text-align: left;">Alcohol use</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Substance use (Single-Question Screening Test for Drug Use)</td>
<td style="text-align: left;">Boston Medical Center Corporation. <em>Validation of self-administered single-item screening question (SISQ) for unhealthy drug use. (Unpublished report, Principal Investigator: Richard Saitz, MD).</em> 2012</td>
</tr>
<tr>
<td rowspan="9" style="text-align: left;">Section 4: Health services and coverage</td>
<td style="text-align: left;">General Practitioner use</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Outpatient use</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Days admitted in hospital</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Emergency Department use</td>
<td style="text-align: left;">University of Essex Institute for Social and Economic Research. Understanding Society: Calendar Year Dataset, 2020. [data collection]. UK Data Service. SN: 8988. 2022</td>
</tr>
<tr>
<td style="text-align: left;">Healthcare access</td>
<td style="text-align: left;">European Social Survey. Source Questionnaire Development. 2024; <a href="https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development">https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire/source-questionnaire-development</a></td>
</tr>
<tr>
<td style="text-align: left;">Healthcare satisfaction (The Patient Satisfaction Questionnaire Short Form)</td>
<td style="text-align: left;">Thayaparan AJ, Mahdi E. The Patient Satisfaction Questionnaire Short Form (PSQ-18) as an adaptable, reliable, and validated tool for use in various settings. <em>Med Educ Online.</em> 2013;18:21747</td>
</tr>
<tr>
<td style="text-align: left;">Healthcare insurance</td>
<td style="text-align: left;">Long D, Haagsma JA, Janssen MF, Yfantopoulos JN, Lubetkin EI, Bonsel GJ. Health-related quality of life and mental well-being of healthy and diseased persons in 8 countries: Does stringency of government response against early COVID-19 matter? <em>SSM Popul Health.</em> 2021;15:100913</td>
</tr>
<tr>
<td style="text-align: left;">Health literacy (Single Item Literacy Screener)</td>
<td style="text-align: left;">Morris NS, MacLean CD, Chew LD, Littenberg B. The Single Item Literacy Screener: Evaluation of a brief instrument to identify limited reading ability. <em>BMC Family Practice.</em> 2006;7(1):21</td>
</tr>
<tr>
<td style="text-align: left;">Care provider status</td>
<td style="text-align: left;">Engel L, Rand S, Hoefman R, et al. Measuring Carer Outcomes in an Economic Evaluation: A Content Comparison of the Adult Social Care Outcomes Toolkit for Carers, Carer Experience Scale, and Care-Related Quality of Life Using Exploratory Factor Analysis. <em>Medical Decision Making.</em> 2020;40(7):885–896</td>
</tr>
</tbody>
</table>

\*Dependent on language availability **Bolded** = randomized in order

</div>

The following standardized health measures were included in the survey: EQ-5D-5L \[8\], EQ-5D-5L bolt-ons \[20–24\], EQ Health and Wellbeing instrument (EQ-HWB) \[25\], PROMIS-10 \[26, 27\], ASCOT \[11, 28\] or ICEpop CAPability measure for Adults (ICECAP-A) \[29\], WHO-5 \[10\], Older People’s Quality of Life questionnaire-brief (OPQOL-brief) \[30\], 2-item Patient Health Questionnaire (PHQ-2) \[31\], 2-item Generalized Anxiety Disorder questionnaire (GAD-2) \[32\] and an author-developed EQ-5D-5L response-scale heterogeneity vignette \[33, 34\]. Standardized measures were acquired directly from the developers if language versions were available. Table <a href="#Tab2" data-ref-type="table">2</a> displays which standardized measures are collected in each country.

<div id="Tab2" class="table-wrap">

<div class="caption">

Standardized health measures administered by country

</div>

<table>
<thead>
<tr>
<th colspan="2" style="text-align: left;">Country</th>
<th style="text-align: left;">EQ-5D-5L</th>
<th style="text-align: left;">EQ-5D-5L bolt-ons</th>
<th style="text-align: left;">EQ-HWB</th>
<th style="text-align: left;">PROMIS-10</th>
<th style="text-align: left;">ASCOT</th>
<th style="text-align: left;">ICECAP-A</th>
<th style="text-align: left;">WHO-5</th>
<th style="text-align: left;">OPQOL-brief</th>
<th style="text-align: left;">PHQ-2</th>
<th style="text-align: left;">GAD-2</th>
</tr>
<tr>
<th style="text-align: left;">Pilot</th>
<th style="text-align: left;">United Kingdom</th>
<th style="text-align: left;">X</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Long form</th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;">9-item version</th>
<th style="text-align: left;">7-item version</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;">Round 1</td>
<td style="text-align: left;">Australia</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Short form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Canada</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Short form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">New Zealand</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">United Kingdom</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">United States</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Short form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td rowspan="10" style="text-align: left;">Round 2</td>
<td style="text-align: left;">Argentina</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Skin irritation</p>
<p>⋅ Self confidence</p></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Brazil</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Chile</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Skin irritation</p>
<p>⋅ Self confidence</p></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">China</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Vision</p>
<p>⋅ Hearing</p>
<p>⋅ Breathing</p>
<p>⋅ Sleep</p>
<p>⋅ Tiredness</p>
<p>⋅ Social relationships</p>
<p>⋅ Self confidence</p>
<p>⋅ Cognition</p></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">France</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Germany</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Social relationships</p>
<p>⋅ Skin irritation</p>
<p>⋅ Self confidence</p></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Japan</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">⋅ Cognition</td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Mexico</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Skin irritation</p>
<p>⋅ Self confidence</p></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Netherlands</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Vision</p>
<p>⋅ Hearing</p>
<p>⋅ Breathing</p>
<p>⋅ Sleep</p>
<p>⋅ Tiredness</p>
<p>⋅ Social relationships</p>
<p>⋅ Skin irritation</p>
<p>⋅ Self confidence</p>
<p>⋅ Cognition</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
<tr>
<td style="text-align: left;">Spain</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"><p>⋅ Skin irritation</p>
<p>⋅ Self confidence</p></td>
<td style="text-align: left;">Long form</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
<td style="text-align: left;">X</td>
</tr>
</tbody>
</table>

</div>

#### EQ-5D-5L

The EQ-5D-5L descriptive system consists of five dimensions rated ‘today’: mobility, self-care, usual activities, pain/discomfort and anxiety/depression. These dimensions are rated on a scale ranging from “no problems” (level 1) to “extreme problems/unable to” (level 5). The EQ VAS (visual analogue scale) is the second part of the instrument, whereby participants rate their overall health today on a scale from 0 (“the worst health you can imagine”) to 100 (“the best health you can imagine”) \[8\].

#### EQ-5D-5L Bolt-ons

Bolt-ons are additional dimensions that can be attached to the EQ-5D-5L to capture aspects of HRQoL not sufficiently covered by the five core dimensions \[24\]. Various combinations of bolt-ons were employed depending on availability and survey burden. Bolt-ons considered included: vision \[20, 24\], hearing \[20, 24\] breathing \[21, 24\], sleep \[20, 24\], tiredness \[24\], social relationships \[20, 24\], cognition \[20, 22, 24\], skin irritation \[23, 24\], and self-confidence \[23, 24\].

#### EQ-HWB

The EQ-HWB is an experimental preference-based instrument with 25 dimensions developed by the EuroQol Group to measure aspects of health and wellbeing referring to a period of “over the last 7 days” \[25\]. A short version has also been designed which currently includes a subset of 9 dimensions.

#### PROMIS-10

PROMIS-10 is a shortened, 10-item version of PROMIS that was created as a general health assessment tool. Nine questions on PROMIS-10 are answered using a 5-point Likert scale, with the tenth question answered using a numeric rating scale. Three questions include a recall period ‘in the past 7 days’. The remaining questions are asked ‘in general’.

#### ASCOT

The ASCOT four-level self-complete (SCT4) is designed to measure social care-related quality of life. It includes 9 items on a 4-point Likert scale and is preference-weighted \[11\].

#### ICECAP-A

ICECAP-A captures individuals’ capabilities regarding their ability to do and be things in life that are important to them, referring to a recall period ‘at the moment’. It has five dimensions: stability, attachment, autonomy, achievement, and enjoyment \[29\]. There are four response categories for each of the five dimensions, ranging from not being able to experience a capability at all (1) to being able to fully experience a capability (4).

#### WHO-5

The WHO-5 instrument measures subjective mental well-being referring to a period of last two weeks \[10\]. It is a generic scale without diagnostic specificity. It can be used across a wide range of study fields. It consists of five short positively-phrased questions about “feeling cheerful and in good spirits”, “feeling calm and relaxed”, “feeling active and vigorous”, “waking up feeling fresh and rested” and “daily life has been filled with things that interest me”, whereby the scale of six answers ranges between “all of the time” (5) to “at no time” (0) \[10\].

#### OPQOL-brief

The OPQOL-brief consists of 14 items, with one of them not included in the total score, and grouped into two dimensions: (1) Psychological wellbeing, defined as a higher-order concept that includes both emotional or psychological well-being, as well as social and collective well-being; and (2) “Life restrictions and limitations”, which refer to difficulties an individual may have in carrying out activities or engaging in life situations in the actual context in which they live. A 5-point Likert-type scale is applied to the 13 items with a neutral response, with 1 “strongly disagree”, 2 “disagree”, 3 “neither agree or disagree”, 4 “agree” and 5 “strongly agree” \[30\]. Adaptive questioning is used so the OPQOL-brief is only displayed to respondents 65+ years.

#### PHQ-2

The PHQ-2, assesses presence and frequency of depressive symptoms “over the last two weeks”. A total score of ≥ 3 (range: 0–6) indicates presence of depressive symptoms.

#### GAD-2

The GAD-2 assesses presence and frequency of anxiety symptoms “over the last two weeks”. A total score ≥ 3 (range: 0–6) indicates presence of anxiety symptoms.

#### EQ-5D-5L response-scale heterogeneity vignette

Several studies provide evidence that self-rated health may differ systematically by age, gender, cultural background, education level, income, and employment status \[35–40\]. This heterogeneity in response is known as differential item functioning \[41\] or reporting/response-scale heterogeneity \[33\] and can lead to inaccurate conclusions about relative health of different groups \[34\]. One technique to identify and adjust for this phenomenon is the use of anchoring vignettes \[34, 35, 42\]. This technique involves asking respondents to rate the health of a hypothetical person based on a short description (i.e., a vignette) \[33, 34\]. This rating is used to anchor the individual’s assessment of their own health, and ‘adjust’ inter-personal comparisons. The authors developed a vignette of “Alex’s health” and asked respondents to complete the EQ-5D-5L on behalf of Alex, imagining that Alex is the same age and has the same background as them. The description of Alex’s health is in Appendix A (Supplemental file).

The study survey was developed by the study team after several rounds of reviews for selection of variables and measures. A comprehensive list of variables and measures were considered and then voted on for inclusion. The survey was designed to allow comparability between countries and ensure local relevance at the same time, particularly regarding socio-demographics questions or those related to healthcare usage and coverage. As such, and where possible, response questions were grouped into fewer categories, and introduced additional responses as needed to align with each country’s context.

Surveys were translated by RWS ([www.rws.com](http://www.rws.com)) to Spanish, French, Portuguese, Japanese, Simplified Chinese, Dutch, and German and other languages as required. Translations of standardized measures were acquired directly from the developers, if available. After surveys were translated, the content was reviewed by native speakers to ensure the language and response options were appropriate for use in the local language and for general insights. English surveys were also reviewed by local researchers in the target countries. Certain questions were adapted in each country’s survey to ensure the applicability of the question, while comparability across countries was also considered.

### Survey features

In sect. 2 of the survey, EQ-5D-5L and EQ-5D-5L response-scale heterogeneity vignette are fixed at the beginning, as EQ-5D-5L is required to be completed prior to completing the vignette. Remaining standardized health measures (i.e., EQ-HWB, WHO-5, PROMIS-10, ASCOT or ICECAP-A, OPQOL-brief, PHQ-2, and GAD-2) are randomized in order to reduce response bias. Age and marital status questions are duplicated within the survey to assess consistency and data quality (e.g., random responses). No responses are mandatory, and participants can skip any questions they prefer not to answer. Participants are able to change their responses by clicking back to a previous page. For questions that may be considered sensitive in nature (e.g., income, substance use, religion), a hover-over information box provides details about why the question is asked and to remind participants they can skip the question if they feel uncomfortable answering it. There are approximately 50 screens (i.e., online pages) of the core survey. The number of screens varies slightly by country due to variations in the measures included. Some questions are also asked conditionally to reduce the number of questions asked (e.g., sex-related health care utilization).

### Study timelines

A pilot study was conducted in the United Kingdom in 2023. Round 1 countries were surveyed between February and May 2024. Round 2 countries were surveyed between May and December 2024. Data collection timelines per country are shown in Table <a href="#Tab3" data-ref-type="table">3</a>**.** Subsequent survey rounds in other countries are planned for 2025 and beyond.

<div id="Tab3" class="table-wrap">

<div class="caption">

Data collection timeframe by country

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Phase</th>
<th style="text-align: left;">Country</th>
<th style="text-align: left;">Start date</th>
<th style="text-align: left;">End date</th>
<th style="text-align: left;">Sample size</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pilot</td>
<td style="text-align: left;">United Kingdom</td>
<td style="text-align: left;">06-Apr-23</td>
<td style="text-align: left;">20-Apr-23</td>
<td style="text-align: left;">3012</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;">Round 1</td>
<td style="text-align: left;">United Kingdom</td>
<td style="text-align: left;">02-Feb-24</td>
<td style="text-align: left;">14-Mar-24</td>
<td style="text-align: left;">4505</td>
</tr>
<tr>
<td style="text-align: left;">New Zealand</td>
<td style="text-align: left;">13-Feb-24</td>
<td style="text-align: left;">20-Mar-24</td>
<td style="text-align: left;">4514</td>
</tr>
<tr>
<td style="text-align: left;">Australia</td>
<td style="text-align: left;">22-Mar-24</td>
<td style="text-align: left;">08-May-24</td>
<td style="text-align: left;">5040</td>
</tr>
<tr>
<td style="text-align: left;">Canada</td>
<td style="text-align: left;">02-Apr-24</td>
<td style="text-align: left;">07-May-24</td>
<td style="text-align: left;">4707</td>
</tr>
<tr>
<td style="text-align: left;">United States</td>
<td style="text-align: left;">12-Apr-24</td>
<td style="text-align: left;">21-May-24</td>
<td style="text-align: left;">4523</td>
</tr>
<tr>
<td rowspan="10" style="text-align: left;">Round 2</td>
<td style="text-align: left;">France</td>
<td style="text-align: left;">06-May-24</td>
<td style="text-align: left;">21-Jun-24</td>
<td style="text-align: left;">4502</td>
</tr>
<tr>
<td style="text-align: left;">Brazil</td>
<td style="text-align: left;">29-May-24</td>
<td style="text-align: left;">05-Jul-24</td>
<td style="text-align: left;">4513</td>
</tr>
<tr>
<td style="text-align: left;">Japan</td>
<td style="text-align: left;">08-Jul-24</td>
<td style="text-align: left;">8-Aug-24</td>
<td style="text-align: left;">4502</td>
</tr>
<tr>
<td style="text-align: left;">Netherlands</td>
<td style="text-align: left;">28-Aug-24</td>
<td style="text-align: left;">07-Oct-24</td>
<td style="text-align: left;">4506</td>
</tr>
<tr>
<td style="text-align: left;">China</td>
<td style="text-align: left;">05-Sep-24</td>
<td style="text-align: left;">14-Oct-24</td>
<td style="text-align: left;">4519</td>
</tr>
<tr>
<td style="text-align: left;">Spain</td>
<td style="text-align: left;">17-Oct-24</td>
<td style="text-align: left;">22-Nov-24</td>
<td style="text-align: left;">4526</td>
</tr>
<tr>
<td style="text-align: left;">Mexico</td>
<td style="text-align: left;">24-Oct-24</td>
<td style="text-align: left;">16-Dec-24</td>
<td style="text-align: left;">4508</td>
</tr>
<tr>
<td style="text-align: left;">Chile</td>
<td style="text-align: left;">29-Oct-24</td>
<td style="text-align: left;">25-Dec-24</td>
<td style="text-align: left;">4503</td>
</tr>
<tr>
<td style="text-align: left;">Argentina</td>
<td style="text-align: left;">08-Nov-24</td>
<td style="text-align: left;">23-Dec-24</td>
<td style="text-align: left;">4506</td>
</tr>
<tr>
<td style="text-align: left;">Germany</td>
<td style="text-align: left;">11-Nov-24</td>
<td style="text-align: left;">26-Dec-24</td>
<td style="text-align: left;">4537</td>
</tr>
</tbody>
</table>

</div>

### EQ-DAPHNIE governance

The EQ-DAPHNIE Project Team comprises of multidisciplinary researchers from around the world. The Project Team meets quarterly to discuss the project methodologic plan. The Project Team is divided into two sub-teams; Population Health Sub-team and Instrument Comparison Sub-team. These teams will take on related research activities to their teams. A Project Executive Committee was also formed and meets monthly for overall project decision-making. We also established a Data Access Review Team (DART), composed of EQ-DAPHNIE Project Team members, which will support data sharing across the EuroQol Group membership. We also have external advisors with expertise in global population health assessment that contribute on an as-needed consultation basis.

## Discussion

The EQ-DAPHNIE project aims to generate large, representative, and comparable sets of population health data would support a broad range of research objectives and offer a valuable research resource and ‘option value’ \[43\]. This project stands out as a comprehensive initiative aimed at filling the gap in the availability of globally representative and comparable HRQoL data. By leveraging robust sampling methods and implementing stringent data collection processes, the project seeks to create an invaluable resource for assessing population health across diverse settings. Inclusion of a wide array of instruments allows for detailed evaluation of various health domains. While previous multi-country studies \[12–17\] have been significant in their contributions, EQ-DAPHNIE’s focus on a broader population base across numerous regions enhances its potential to influence public health policy and healthcare interventions. The rigorous methodological approach of the project, which includes pre-testing, pilot phases, and continuous quality checks, ensures data will be reliable and applicable for future research. Despite the challenges posed by the online nature of data collection—such as exclusion of individuals without internet access—the quota sampling design aims to mitigate these issues of obtaining representativeness. EQ-DAPHNIE’s infrastructure will be key in understanding global health disparities and will support efforts to address emerging health challenges.

### Limitations

Despite rigorous methods in the survey development and design, we nonetheless recognize several challenges and limitations. Reliance on web-based surveys may exclude individuals with poor or no internet access, potentially biasing the samples. There may be additional biases present by using online panels regarding population representativeness. Our intention is to explore different sampling and data collection methods in subsequent surveys to understand and mitigate these limitations. Additionally, cultural differences in the interpretation and functioning of measures may affect comparability of results across countries. These limitations must be acknowledged and addressed in analysis and interpretation of data. The data is collected at a single time period as a cross-section of the population, thus limiting the questions that can be addressed. Longitudinal follow-up with a subset of participants would offer additional insights into changes in population health over time and reliability of instruments used. Serial panels with biennial or triennial data collection cycles would further enhance the dataset’s robustness, allowing for continuous monitoring and validation. These approaches may be considered in future applications of the EQ-DAPHNIE infrastructure.

### Ethical considerations

Ethics approval for the study was granted from the following institutions, where required for local requirements: University of Alberta (Health Research Ethics Board Pro00123401) on November 3, 2022 and University of Otago (Human Ethics Research Committee H23/130) on November 20, 2023. Advarra (Pro00077236) also granted the study exemption status from IRB oversight on February 16, 2024.

This study will be conducted according to Canadian and international standards of Good Clinical Practice for all studies. As we expand data collection in subsequent survey rounds, ethics approvals from other local institutions will be sought, as needed. Applicable government regulations and university research policies and procedures will also be followed. This study description and any amendments will be submitted to applicable Health Research Ethics Boards for formal approval to conduct the study.

## Conclusion

The EQ-DAPHNIE project represents a significant effort to establish infrastructure to easily and reliably collect large, representative, and comparable sets of population health data across multiple countries. By adhering to stringent sampling strategies, robust recruitment and data collection methods, and ensuring high data quality, the project aims to provide a valuable resource for understanding population health and evaluating health status measures. Future research should focus on addressing the identified challenges and exploring potential for longitudinal follow-up to enhance understanding of population health dynamics over time.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 15 kb)

</div>

## Author contributions

JAJ and MFJ are the principal investigators. FAS, HB, MG, DG, NG, EL, BM, FP, DS, TS, RV, ZY, and VZ are co-investigators. HS is the research coordinator. Together, these authors conceived and designed the study. All authors have contributed to the writing of this paper and have read and approved the final manuscript.

## Funding

This study was funded by EuroQol Research Foundation Grant Number: 367-RA.

## Data availability

The data that supports the findings of this study are available from the EuroQol Group, but restrictions apply to the availability of these data. Data are currently only available to members of the EuroQol Group, however, data are available for use in collaboration with EuroQol member(s). The authors can advise upon reasonable request. The complete core survey content is available upon request.

## Declarations

### Competing interests

All authors except HS are members of the EuroQol Group.

### Ethical approval

This study will be performed in line with the principles of the Declaration of Helsiniki. Approval was granted by the University of Alberta (Health Research Ethics Board Pro00123401), University of Otago (Human Ethics Research Committee H23/130), and Advarra (Pro00077236).

### Consent to participate

Informed consent will be obtained from all participants included in the study.

## Footnotes

## References

## References

1. Mindell, J. S., Moody, A., Vecino-Ortiz, A. I., Alfaro, T., Frenz, P., Scholes, S., Gonzalez, S. A., Margozzini, P., De Oliveira, C., Sanchez Romero, L. M., & Alvarado, A. (2017). Comparison of health examination survey methods in Brazil, Chile, Colombia, Mexico, England, Scotland, and the United States. American Journal of Epidemiology,186(6), 648–658. doi:10.1093/aje/kwx045

2. Janssen, M. F., Szende, A., Cabases, J., Ramos-Goñi, J. M., Vilagut, G., & König, H. H. (2019). Population norms for the EQ-5D-3L: a cross-country analysis of population surveys for 20 countries. The European Journal of Health Economics,20(2), 205–216. doi:10.1007/s10198-018-0955-5

3. Tolonen, H., Reinikainen, J., Koponen, P., Elonheimo, H., Palmieri, L., & Tijhuis, M. J. (2021). Cross-national comparisons of health indicators require standardized definitions and common data sources. Archives of Public Health,79(1), 208. doi:10.1186/s13690-021-00734-w

4. World Health Organization. (2020). World health statistics 2020: Monitoring health for the SDGs, sustainable development goals. World Health Organization.

5. Boerma, T., Eozenou, P., Evans, D., Evans, T., Kieny, M. P., & Wagstaff, A. (2014). Monitoring progress towards universal health coverage at country and global levels. PLOS Medicine,11(9), e1001731. doi:10.1371/journal.pmed.1001731

6. Weldring, T., & Smith, S. M. (2013). Patient-reported outcomes (PROs) and patient-reported outcome measures (PROMs). Health Services Insights,6, 61–68. doi:10.4137/HSI.S11093

7. Bull, C., Teede, H., Watson, D., & Callander, E. J. (2022). Selecting and implementing patient-reported outcome and experience measures to assess health system performance. JAMA Health Forum,3(4), e220326–e220326. doi:10.1001/jamahealthforum.2022.0326

8. Herdman, M., Gudex, C., Lloyd, A., Janssen, M. F., Kind, P., Parkin, D., Bonsel, G., & Badia, X. (2011). Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Quality Life Research,20(10), 1727–1736. doi:10.1007/s11136-011-9903-x

9. Cella, D., Riley, W., Stone, A., Rothrock, N., Reeve, B., Yount, S., Amtmann, D., Bode, R., Buysse, D., Choi, S., & Cook, K. (2010). The patient-reported outcomes measurement information system (PROMIS) developed and tested its first wave of adult self-reported health outcome item banks: 2005–2008. Journal of Clinical Epidemiology,63(11), 1179–1194. doi:10.1016/j.jclinepi.2010.04.011

10. Topp, C. W., Østergaard, S. D., Søndergaard, S., & Bech, P. (2015). The WHO-5 well-being index: A systematic review of the literature. Psychotherapy and Psychosomatics,84(3), 167–176. doi:10.1159/000376585

11. Netten, A., Burge, P., Malley, J., Potoglou, D., Towers, A. M., Brazier, J., Flynn, T., & Forder, J. (2012). Outcomes of social care for adults: Developing a preference-weighted measure. Health Technology Assessment,16(16), 1–166. doi:10.3310/hta16160

12. Valderas, J. M., Porter, I., Martin-Delgado, J., Rijken, M., de Jong, J., Groene, O., Bloemeke-Cammin, J., Sunol, R., Williams, R., Ballester, M., & de Bienassis, K. (2024). Development of the patient-reported indicator surveys (PaRIS) conceptual framework to monitor and improve the performance of primary care for people living with chronic conditions. BMJ Quality & Safety. 10.1136/bmjqs-2024-017301

13. Violato, M., Pollard, J., Lloyd, A., Roope, L. S., Duch, R., Becerra, M. F., & Clarke, P. M. (2023). The COVID-19 pandemic and health-related quality of life across 13 high- and low-middle-income countries: A cross-sectional analysis. PLOS Medicine,20(4), e1004146. doi:10.1371/journal.pmed.1004146

14. Alexandrov, N., Scott, E. S., Janssen, M. F., Lubetkin, E. I., Yfantopoulos, J. N., Bonsel, G. J., & Haagsma, J. A. (2024). The relationship between healthcare access and change in health-related quality-of-life among the general population of five countries during the COVID-19 pandemic. Quality of Life Research,33, 2541. doi:10.1007/s11136-024-03704-1

15. The Commonwealth Fund. 2017 Commonwealth Fund International Health Policy Survey of Older Adults. 2024 April 4, 2024]; Available from: https://www.commonwealthfund.org/publications/surveys/2017/nov/2017-commonwealth-fund-international-health-policy-survey-older.

16. Monash University. The Multi Instrument Comparison (MIC) study. 2024 April 4, 2024]; Available from: https://www.monash.edu/business/che/aqol/mic.

17. Richardson, J., Iezzi, A., & Maxwell, A. (2012). Cross-national comparison of twelve quality of life instruments: MIC Paper 1 Background, questions, instruments. Centre for Health Economics, Monash University, Melbourne

18. Hays, R. D., Liu, H., & Kapteyn, A. (2015). Use of Internet panels to conduct surveys. Behavior Research Methods,47(3), 685–690. doi:10.3758/s13428-015-0617-9

19. Craig, B. M., Hays, R. D., Pickard, A. S., Cella, D., Revicki, D. A., & Reeve, B. B. (2013). Comparison of US panel vendors for online surveys. Journal of Medical Internet Research,15(11), e260. doi:10.2196/jmir.2903

20. Finch, A. P., Brazier, J., & Mukuria, C. (2021). Selecting bolt-on dimensions for the EQ-5D: Testing the impact of hearing, sleep, cognition, energy, and relationships on preferences using pairwise choices. Medical Decision Making,41(1), 89–99. doi:10.1177/0272989X20969686

21. Hoogendoorn, M., Oppe, M., Boland, M. R., Goossens, L. M., Stolk, E. A., & Rutten-Mölken, M. P. (2019). Exploring the impact of adding a respiratory dimension to the EQ-5D-5L. Medical Decision Making,39(4), 393–404. doi:10.1177/0272989X19847983

22. Geraerds, A. J., Bonsel, G. J., Janssen, M. F., de Jongh, M. A., Spronk, I., Polinder, S., & Haagsma, J. A. (2019). The added value of the EQ-5D with a cognition dimension in injury patients with and without traumatic brain injury. Quality of Life Research,28(7), 1931–1939. doi:10.1007/s11136-019-02144-6

23. Swinburn, P., Lloyd, A., Boye, K. S., Edson-Heredia, E., Bowman, L., & Janssen, B. (2013). Development of a disease-specific version of the EQ-5D-5L for use in patients suffering from psoriasis: Lessons learned from a feasibility study in the UK. Value in Health,16(8), 1156–1162. doi:10.1016/j.jval.2013.10.003

24. Rencz, F., & Janssen, M. F. (2024). Testing the psychometric properties of 9 Bolt-Ons for the EQ-5D-5L in a general population sample. Value in Health,27(7), 943–954. doi:10.1016/j.jval.2024.03.2195

25. Brazier, J., Peasgood, T., Mukuria, C., Marten, O., Kreimeier, S., Luo, N., Mulhern, B., Pickard, A. S., Augustovski, F., Greiner, W., & Engel, L. (2022). The EQ-HWB: Overview of the development of a measure of health and wellbeing and key results. Value in Health,25(4), 482–491. doi:10.1016/j.jval.2022.01.009

26. Hays, R. D., Schalet, B. D., Spritzer, K. L., & Cella, D. (2017). Two-item PROMIS® global physical and mental health scales. Journal of Patient-Reported Outcomes,1(1), 2. doi:10.1186/s41687-017-0003-8

27. Cella, D., Yount, S., Rothrock, N., Gershon, R., Cook, K., Reeve, B., Ader, D., Fries, J. F., Bruce, B., Rose, M., PROMIS Cooperative Group. (2007). The patient-reported outcomes measurement information system (PROMIS): Progress of an NIH roadmap cooperative group during its first two years. Medical Care,45(5 Suppl 1), S3–S11. doi:10.1097/01.mlr.0000258615.42478.55

28. Rand, S., Malley, J., Towers, A. M., Netten, A., & Forder, J. (2017). Validity and test-retest reliability of the self-completion adult social care outcomes toolkit (ASCOT-SCT4) with adults with long-term physical, sensory and mental health conditions in England. Health and Quality of Life Outcomes,15(1), 163. doi:10.1186/s12955-017-0739-0

29. Al-Janabi, H., Flynn, T. N., & Coast, J. (2012). Development of a self-report measure of capability wellbeing for adults: The ICECAP-A. Quality of Life Research,21(1), 167–176. doi:10.1007/s11136-011-9927-2

30. Bowling, A., Hankins, M., Windle, G., Bilotta, C., & Grant, R. (2013). A short measure of quality of life in older age: The performance of the brief older people’s quality of life questionnaire (OPQOL-brief). Archives of Gerontology and Geriatrics,56(1), 181–187. doi:10.1016/j.archger.2012.08.012

31. Kroenke, K., Spitzer, R. L., & Williams, J. B. (2003). The patient health questionnaire-2: Validity of a two-item depression screener. Medical Care,41(11), 1284–1292. doi:10.1097/01.MLR.0000093487.78664.3C

32. Skapinakis, P. (2007). The 2-item generalized anxiety disorder scale had high sensitivity and specificity for detecting GAD in primary care. Evidence-Based Medicine,12(5), 149. doi:10.1136/ebm.12.5.149

33. Knott, R. J., Black, N., Hollingsworth, B., & Lorgelly, P. K. (2017). Response-scale heterogeneity in the EQ-5D. Health Economics,26(3), 387–394. doi:10.1002/hec.3313

34. Au, N., & Lorgelly, P. K. (2014). Anchoring vignettes for health comparisons: An analysis of response consistency. Quality of Life Research,23(6), 1721–1731. doi:10.1007/s11136-013-0615-2

35. Murray, C. J., Tandon, A., Salomon, J. A., Mathers, C. D., & Sadana, R. (2003). Cross population comparability of evidence for health policy.

36. Lindeboom, M., & van Doorslaer, E. (2004). Cut-point shift and index shift in self-reported health. Journal of Health Economics,23(6), 1083–1099. doi:10.1016/j.jhealeco.2004.01.002

37. Shmueli, A. (2003). Socio-economic and demographic variation in health and in its measures: The issue of reporting heterogeneity. Social Science and Medicine,57(1), 125–134. doi:10.1016/s0277-9536(02)00333-7

38. Dowd, J. B., & Zajacova, A. (2010). Does self-rated health mean the same thing across socioeconomic groups? Evidence from biomarker data. Ann Epidemiol,20(10), 743–749. doi:10.1016/j.annepidem.2010.06.007

39. Jürges, H. (2007). True health vs response styles: Exploring cross-country differences in self-reported health. Health Economics,16(2), 163–178. doi:10.1002/hec.1134

40. Kerkhofs, M., & Lindeboom, M. (1995). Subjective health measures and state dependent reporting errors. Health Economics,4(3), 221–235. doi:10.1002/hec.4730040307

41. Knott, R. J., Lorgelly, P. K., Black, N., & Hollingsworth, B. (2017). Differential item functioning in quality of life measurement: An analysis using anchoring vignettes. Social Science & Medicine,190, 247–255. doi:10.1016/j.socscimed.2017.08.033

42. King, G., Murray, C. J., Salomon, J. A., & Tandon, A. (2004). Enhancing the validity and cross-cultural comparability of measurement in survey research. American Political Science Review,98(1), 191–207.

43. Roope, L. S., Candio, P., Kiparoglou, V., McShane, H., Duch, R., & Clarke, P. M. (2021). Lessons from the pandemic on the value of research infrastructure. Health Research Policy and Systems,19(1), 54. doi:10.1186/s12961-021-00704-2

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 15 kb)

</div>

### Data Availability Statement

The data that supports the findings of this study are available from the EuroQol Group, but restrictions apply to the availability of these data. Data are currently only available to members of the EuroQol Group, however, data are available for use in collaboration with EuroQol member(s). The authors can advise upon reasonable request. The complete core survey content is available upon request.

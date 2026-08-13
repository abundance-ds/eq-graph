---
project_id: "1456-PD"
work_id: "doi:10.3390/curroncol32110645"
doi: "10.3390/curroncol32110645"
pmid: "41294707"
pmcid: "PMC12651012"
title: "Examining the Association Between Equity-Related Factors and EQ-5D-3L Health Utilities of Patients with Cancer"
journal: "Current Oncology"
publication_date: "2025-11-19"
volume: "32"
issue: "11"
authors:
  - name: "Teresa C. O. Tsui"
    orcid: "https://orcid.org/0000-0002-9806-9393"
    affiliation_ids:
      - "af1-curroncol-32-00645"
      - "af2-curroncol-32-00645"
      - "af3-curroncol-32-00645"
      - "af4-curroncol-32-00645"
  - name: "Rebecca E. Mercer"
    orcid: "https://orcid.org/0000-0002-9264-7797"
    affiliation_ids:
      - "af1-curroncol-32-00645"
      - "af3-curroncol-32-00645"
  - name: "Eleanor M. Pullenayegum"
    orcid: "https://orcid.org/0000-0003-4265-1330"
    affiliation_ids:
      - "af2-curroncol-32-00645"
      - "af4-curroncol-32-00645"
  - name: "Kelvin K. W. Chan"
    orcid: "https://orcid.org/0000-0002-2501-3057"
    affiliation_ids:
      - "af1-curroncol-32-00645"
      - "af2-curroncol-32-00645"
      - "af3-curroncol-32-00645"
affiliations:
  - id: "af1-curroncol-32-00645"
    name: "Sunnybrook Research Institute, Toronto, ON M4N 3M5, Canada; teresa.tsui@alumni.utoronto.ca (T.C.O.T.); rebecca.mercer@sunnybrook.ca (R.E.M.)"
  - id: "af2-curroncol-32-00645"
    name: "Dalla Lana School of Public Health, University of Toronto, Toronto, ON M5S 1A1, Canada; eleanor.pullenayegum@sickkids.ca"
  - id: "af3-curroncol-32-00645"
    name: "Canadian Centre for Applied Research in Cancer Control (ARCC), Toronto, ON M4N 3M5, Canada"
  - id: "af4-curroncol-32-00645"
    name: "Child Health Evaluative Sciences, The Hospital for Sick Children, Toronto, ON M5G 1X8, Canada"
keywords:
  - "EQ-5D-3L"
  - "equity"
  - "health utility"
  - "oncology"
licence: "cc-by"
source_file: "input/projects/1456-PD/papers/doi_10.3390_curroncol32110645.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12651012/fullTextXML"
source_method: "epmc_xml"
source_sha256: "19bfb2da63063cce642690b71bf45233c2d032a78b2f1268adc4ae45be9c9ed8"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Examining the Association Between Equity-Related Factors and EQ-5D-3L Health Utilities of Patients with Cancer

## Abstract

Background and existing knowledge: Health utilities are a measure of health-related quality of life (HRQoL) used in cancer drug funding decisions. These are often derived from clinical trials with highly selected, socioeconomically advantaged participants, which can over-estimate HRQoL. To address this issue, we explored associations between EQ-5D-3L health utilities across a range of socioeconomic statuses in a real-world sample of patients with cancer. New findings: We found that HRQoL measured through EQ-5D-3L health utilities was lowest in patients in the lowest (under CAD 29,000) and undisclosed income categories. Implications: Our findings suggest that HRQoL measured through EQ-5D-3L health utilities may be associated with socioeconomic status, particularly family income. These findings can be used to support equity-informed health technology assessment.

## 1. Introduction

Health-related quality of life (HRQoL) is an important outcome in clinical decision-making and health economic evaluations in cancer care \[1,2\]. Health utilities are a quantitative measure of HRQoL, anchored at 0 (dead) and 1 (perfect health). Health utilities provide a weight on cancer-related survival to arrive at the quality-adjusted life year (QALY), used in cost–utility analysis, as part of health technology assessments (HTA) \[3\].

Health utilities used in HTA are often collected in pivotal clinical trials \[4,5\]. Participants enrolled in clinical trials are usually healthier \[6\] and are more socioeconomically advantaged than real-world patients \[7,8\]. Health utilities derived from these trials may therefore over-estimate the health utilities of those with lower socioeconomic status. There are important equity implications, since cost–utility analyses rely on trial-based health utilities, decisions arising from these analyses may be biased and favour interventions that were evaluated in these highly selected trial-based populations \[9,10\].

The EQ-5D questionnaire, developed by the EuroQol group (5), is the most common health utility instrument used in clinical trials and health technology assessments to measure HRQoL \[11\]. The EQ-5D-3L assesses five dimensions of HRQoL: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression \[12,13\]. Each of these has three levels: no problems, some problems, or extreme problems/unable to perform activities \[13\]. The 5L version uses the same five dimensions, but has expanded to five levels: no problems, slight problems, moderate problems, severe problems, and unable to \[14\]. For both the EQ-5D-3L and EQ-5D-5L versions, an additional visual analogue scale (VAS) asks respondents to rate their current health from 0 (worst imaginable) to 100 (best imaginable) \[15\].

Socioeconomic status (SES), one’s access to material and social resources, aligns with the indicators used for socioeconomic position (SEP), in the World Health Organization’s social determinants of health conceptual framework \[16\]. These indicators (income, education, occupation), along with stratifiers such as social class, gender, and race/ethnicity, influence one’s exposure to advantage and disadvantage \[16\]. Social position determines health through intermediate factors, including material, psychosocial, behavioural, and biological factors \[16\], which impact HRQoL \[17\].

SES is associated with EQ-5D health utilities in oncology \[18,19,20\]. In Canada, a large survey of cancer survivors (*n* = 1759) found higher EQ-5D-3L health utilities among those with a university/college education compared with no university/college education *p* \< 0.001, and lower health utilities among individuals not married compared with married or common law (*p* = 0.001). The same study found a large difference in mean (SE) health utilities by cancer site, from 0.76 (0.03) in pancreatic cancer to 0.90 (0.05) in chronic lymphocytic leukemia \[18\]. In China, among a sample of patients with colorectal cancer, lower household income was associated with lower EQ-5D-5L health utility, with a mean (SD) of 0.505 (0.419) for \<¥20K to 0.759 (0.315) for \>¥80K. These examples illustrate how factors such as marital status, income, education level, and cancer site have been associated with EQ-5D-3L or 5L responses in Canada and China \[18,19\].

In the Canadian cancer care space, health utilities are often collected in clinical trials under highly monitored conditions \[21\], yet there is no routine collection of real-world health utilities, which could improve patient care and facilitate real-world cost–utility analyses to inform health technology assessments.

Our team recently conducted a feasibility study of implementing the EQ-5D-3L questionnaire at a pilot oncology centre in Ontario, Canada \[22\], enabling us to examine how patient characteristics and SES impact EQ-5D-3L health utilities. We used the EQ-5D-3L instrument instead of the more recent EQ-5D-5L version, as the 3L version has more historic use than the 5L version as a clinical outcome assessment in health technology assessment, regulatory reviews, and systematic literature reviews \[23\]. The objective of this current study was to examine patient characteristics that may be responsible for differences in EQ-5D-3L health utilities in a real-world sample of patients with cancer. We hypothesized that patient characteristics of age, sex, education, marital status, employment status, income, primary cancer site, and ethnicity would be associated with EQ-5D-3L health utilities.

## 2. Materials and Methods

### 2.1. Study Design and Population

This was a cross-sectional analysis of initial EQ-5D-3L responses from patients with cancer. We accrued a prospective convenience sample of patients with any solid tumour or hematological malignancy to complete the EQ-5D-3L during their chemotherapy appointment at the Sunnybrook Odette Cancer Centre in Toronto, Ontario, Canada. Eligible patients were 18 years or over, starting any publicly reimbursed systemic therapy, and provided informed consent. Along with completing the EQ-5D-3L and EQ-VAS, patients were invited to complete a demographic questionnaire. The patient’s primary cancer site was abstracted from their visit record at screening. Patients were accrued from May to November 2024, with patient accrual described in greater detail in our earlier manuscript \[20\].

### 2.2. Study Sources and Measures

The EQ-5D-3L health utility score was the outcome variable of interest in this study. We included covariates comprising patient demographics and clinical characteristics identified from the literature \[18,24\], conceptual relevance, and refined based on expert opinion (KC). The specific variables tested in our models were age, sex, education, marital status, employment status, family income, ethnicity, and primary cancer site. Age was tested as both a continuous and categorical variable in separate models. Models with and without the birth sex variable were tested to assess the effect of sex-specific cancers. First, we included data with all cancers and excluded sex as a variable (*n* = 170). To incorporate sex as a variable, we excluded individuals with gynecological, breast, and prostate cancers in our multivariable analysis (*n* = 111). These sample sizes allowed the estimation of model parameters and their 95% confidence intervals (CIs) with reasonable precision, according to linear regression best practices \[25\], and the accuracy in parameter estimation principle \[26\].

### 2.3. Statistical Analysis

We conducted ordinary least squares (OLS) multivariable regression to estimate the association between multiple covariates and EQ-5D-3L utility scores.

We tested main effects models followed by models with interactions between birth sex and age categories (\<50, 50 to 74, \>75 years) based on conceptual relevance. Main effects models and models with interactions were assessed using analysis of variance (ANOVA) to evaluate the significance of the interaction term. Nested models were compared using the Bayesian Information Criterion (BIC), where a smaller BIC represents a simpler model. Reference categories were assigned based on either the largest sample size or the group thought to be most privileged, based on the literature \[27,28\]. Because the calculated health utilities were left-skewed (<a href="#app1-curroncol-32-00645" data-ref-type="app">Supplementary material Figure S1</a>) and income was categorizeed into ordinal levels, Spearman’s rank correlations were explored between numerical income categories (\<CAD 29,999 to \>CAD 150,000) and each EQ-5D-3L dimension. Positive coefficients indicate that lower income is associated with higher problem severity.

### 2.4. Software

All analyses were conducted using R version 4.5.0. EQ-5D-3L health utilities were scored using the eq5d package (version 0.15.7), with the Canadian EQ-5D-3L time-trade-off (TTO) scoring model \[29\]. The best and worst health states for this Canadian TTO value set ranged from 1.000 for 11,111 (best health) to a predicted mean (SE) −0.340 (0.013) for 33,333 (worst health) \[30\].

## 3. Results

### 3.1. Participant Characteristics

A summary of patient characteristics is presented in <a href="#curroncol-32-00645-t001" data-ref-type="table">Table 1</a>. Most respondents identified as White—108 (65.5%)—and a large percentage completed at least some college or university education—127 (75.6%). Most respondents were married or in a common-law relationship—115 (68.9%)—and half were retired—83 (50.3%). Of patients who reported a family income, 29 (17.3%) reported an annual family income of over CAD 150,000; however, 79 (46.5%) did not report a family income. In the full sample, amongst those with a reported primary cancer site, the gynecological cancers were most common—40 (23.5%)—whereas head and neck cancers were the most common amongst cancers affecting all sexes—32 (18.8%). As the second most frequent cancer, head and neck cancers were assigned as the reference category for primary cancer sites, to ensure that models with all cancers and models without sex-specific cancers could be compared.

### 3.2. EQ-5D-3L Health Utility by Cancer Site

<a href="#curroncol-32-00645-t002" data-ref-type="table">Table 2</a> shows descriptive statistics of mean health utility (SD) for the different cancer sites. The primary cancer sites with the highest mean health utilities (SD) were colorectal—0.918 (0.127); skin—0.819 (0.096); and breast—0.815 (0.162). In contrast, the primary cancer sites with the lowest mean health utilities (SD) were upper gastrointestinal—0.731 (0.127); genitourinary—0.717 (0.174); and thoracic—0.712 (0.254).

### 3.3. Association Between EQ-5D-3L Dimension and Income

<a href="#curroncol-32-00645-t003" data-ref-type="table">Table 3</a> shows the Spearman’s rank correlation (ρ) between EQ-5D-3L dimensions and income. <a href="#curroncol-32-00645-f001" data-ref-type="fig">Figure 1</a> is a stacked bar plot of income level and the percentage of patients within each income level. The dimensions pain/discomfort (PD) and anxiety/depression (AD) were significantly associated with lower income (ρ PD = 0.291, *p* = 0.008; ρAD = 0.219, *p* = 0.046).

Stacked bar plots (<a href="#curroncol-32-00645-f001" data-ref-type="fig">Figure 1</a>) illustrate a higher percentage of responses of “some problems” and “extreme problems” in the income groups “prefer not to answer” and CAD 0 to 29,999, particularly for dimensions UA, PD, and AD. The largest percentage of “extreme problems” was seen within the “prefer not to answer” (11%) income category and CAD 0 to 29,999 (18%) category, both for the PD dimension. These percentages are in agreement with Spearman’s correlation.

### 3.4. Patient Demographics Associated with Health Utility

<a href="#curroncol-32-00645-t004" data-ref-type="table">Table 4</a> presents the results of our multivariable regression models of patient demographic factors associated with EQ-5D-3L health utility. The two models presented are (i) one including birth sex and excluding participants with no sex-specific cancers (*n* = 111) and (ii) one excluding birth sex and including all cancers (*n* = 170). Model fit statistics of all fitted models, including those with interactions are presented in the <a href="#app1-curroncol-32-00645" data-ref-type="app">Supplementary materials Table S1</a>.

In both the models with and without birth sex, a family income of CAD 0 to 29K and undisclosed income were associated with a significantly lower health utility (*p* \< 0.05). The model with birth sex had a disutility estimate for income \< CAD 0 to 29K (95% CI) of −0.202 (−0.371 to −0.033), and undisclosed income had a disutility estimate of −0.123 (−0.235 to −0.012). The model that excludes birth sex had a disutility estimate for income CAD 0 to 29K (95% CI) of −0.163 (−0.280 to −0.046), and undisclosed income had a disutility estimate of −0.106 (−0.184 to −0.028).

Of all primary cancer sites, those with colorectal cancers had significantly higher utility estimates (*p* \< 0.05) by 0.135 (0.010 to 0.260) for the model with the sex variable, and 0.147 (0.031 to 0.263) for the model excluding the sex variable.

The interaction term between age as a categorical variable and birth sex was not statistically significant. Models with interaction terms between birth sex and age found that tests of significance of the interaction terms were not significant (*p* = 0.359) (See <a href="#app1-curroncol-32-00645" data-ref-type="app">Supplementary materials Tables S2 and S3</a>).

## 4. Discussion

This study found significant associations between income and EQ-5D-3L health utility. Individuals in the lowest family income category (CAD 0 to 29,999) and those who did not disclose their income had significantly lower health utilities than those with a family income of at least CAD 150,000. Our sample of participants included participants with birth sex distributions similar to those with cancer in Canada \[32\], participants of a higher average age than in Ontario (our study: 64.5; Ontario: 41.3 years) \[33\], and more participants with a family income \> CAD 150,000 compared with Ontario (our study: 17.1%; Ontario: 15.4%) \[34\]. Participants in the lowest family income category in our study were within the lowest 10% of after-tax income for people in an economic family or the lowest 20% of people not in an economic family in Ontario, Canada \[35\]. The resulting health utility gaps between those in the lowest and highest income categories are relevant to HTA decisions.

Income has been associated with EQ-5D-3L health utilities across a number of countries. Janssen et al. reported population norms of EQ-5D-3L in 20 countries, finding that macroeconomic factors including prior living standards, represented by GDP per capita and health expenditure per capita, were positively correlated with mean EQ-VAS scores at 0.58 and 0.55, respectively \[27\]. In a population-level study from Brazil, participants in intermediate and lower SES classes had significantly lower EQ-5D-3L health utilities compared with the higher SES classes, regardless of their age, sex, and education, based on a multivariable analysis \[20\]. These findings are in agreement with our findings that being in the lowest income category is associated with lower health utility.

In Canada, like other countries with a universal health care system, the societal costs of cancer include both health care system costs as well as costs borne by people with cancer and their caregivers \[36\]. People diagnosed with cancer, along with their caregivers, experience direct costs, indirect costs, and psychosocial costs, where the latter includes health-related quality of life costs \[36\]. Population norms for EQ-5D-3L have consistently found that individuals in a low-income category have lower health utilities, independent of their health status \[20,27,37,38\]. We hypothesize that individuals in a lower income category may experience further decrements to their health utility as a consequence of the financial impacts of a cancer diagnosis. This is consistent with our findings of positive associations between low income and high problem-severity level, particularly in the pain/discomfort and anxiety/depression dimensions.

Our findings add to the larger body of literature on the association of family income with health utilities amongst people with cancer. The findings from this study are comparable with another large study on cancer health utilities collected in Ontario, Canada \[18\]. Naik et al. analyzed EQ-5D-3L responses from 1759 ambulatory patients with cancer, calculated EQ-5D-3L scores across 26 cancers, and constructed a multivariable model to establish an association of factors influencing EQ-5D-3L response. A notable difference was that our sample of patients with colorectal cancers had higher EQ-5D-3L health utilities (SD)—0.918 (0.127)—compared with Naik—0.83 (0.107) \[18\]. Patients presenting with colorectal cancer in our study had the highest EQ-5D-3L health utilities, potentially because of long-term survivorship or positive response to treatment. Of the cancer sites that were similarly categorized, mean health utilities were comparable between our studies \[18\]. A key methodological difference is that Naik et al. did not include age, sex, and income as variables in their multivariable model. They reported that age was not a significant variable (*p* = 0.54) and excluded sex as a variable because of the inclusion of sex-specific cancers. In contrast, our study incorporated SES variables including age, sex, and income to explore equity-related response heterogeneity in the EQ-5D-3L, which has not been previously studied in the Canadian cancer care context.

There are strengths and limitations to our study. A major strength of our findings is our contribution to the association of patient characteristics with cancer health utilities. We found an association between individuals in a lower income category or who prefer not to report their income and lower health utilities. Our sample collected birth sex and gender, and noted complete concordance between the two, largely owing to our small sample size. Broader implementation of the EQ-5D across Ontario would allow any gender specific analyses to be properly completed. Another strength of our findings is in adding to the knowledge on EQ-5D-3L health utilities in the Canadian context to provide input parameters for future cost–utility analyses. There are several limitations of our study. First, using EQ-5D-3L to measure health utilities is susceptible to ceiling effects \[39\], which can under-estimate overall population-level health utilities. These ceiling effects are thought to be reduced by using the EQ-5D-5L, which also has improved responsiveness \[39\]. In a sample of patients with cancer from Iran, the EQ-5D-5L demonstrated lower ceiling effects compared with the EQ-5D-3L. Ceiling effects were observed for both EQ-5D-3L and EQ-5D-5L (12.07% and 9.44%, respectively), both lower than the acceptable limit of 15% for health status questionnaires \[40\]. We did not account for unmeasured confounding in this study, including comorbidities or cancer stage, which have been shown to influence EQ-5D-3L health utilities \[18\]. Our model that includes the birth sex variable (28 df, *n* = 111) has wider 95% CI estimates, even though it satisfies model parsimony and clinical relevance. Lastly, we conducted a cross-sectional pilot single-site study in an urban Canadian oncology centre, which had a small sample size (*n* = 170 full sample; *n* = 111 sample excluding sex-specific cancers). The impact of our smaller sample size is that all health utility estimates are susceptible to wider standard errors, reflecting the uncertainty in measurement.

There are implications of our work for users of EQ-5D-3L health utilities. Our findings suggest that HTAs that use trial-based health utilities may be over-estimated, yet the implications on incremental QALYs gained from novel therapies are unclear. We therefore encourage health economists, researchers, and policy makers to consider the association of patient characteristics and SES, specifically income, with health utilities used in economic models for HTA. Incorporating real-world health utilities, which account for equity-related factors, can more judiciously allocate scarce health care resources, so that health care decisions can better reflect the HRQoL of equity-deserving populations. Future research can explore longitudinal health utility collection to understand the association of equity-deserving variables on change in health utilities from initial diagnosis onwards, and their applications on distributional cost-effectiveness analyses \[41\].

## 5. Conclusions

This study provides the first Canadian real-world estimates that quantify the effect of income on EQ-5D-3L health utilities in oncology. Patient demographic characteristics and SES, in particular low income, are associated with lower EQ-5D-3L health utilities.

### Acknowledgments

The authors thank these individuals from the Sunnybrook Odette Cancer Centre: Carlo DiAngelis and Christine Peragine from the pharmacy team for initial patient screening; Kirsty Wield from the nursing team for partnership to facilitate patient recruitment; Elena Zhou, Rahul Desai, Shreya Chatterjee, and Curtis Yeung for assisting with patient recruitment; and Suzanne Chung, REDCap Programmer, the Centre for Clinical Trial Support (CCTS), Sunnybrook Research Institute, for setting up the data capture forms.

#### Supplementary Materials

The following supporting information can be downloaded at <https://www.mdpi.com/article/10.3390/curroncol32110645/s1>. Figure S1. Histogram distribution of EQ-5D-3L health utility scores. Table S1. Table of multivariable model fit statistics. Table S2. Table of age (categorical)/birth sex interaction, no participants with female and male cancers. Table S3. Table of birth sex/age (categorical) interaction, no participants with female and male cancers.

### Author Contributions

Conceptualization, T.C.O.T., E.M.P. and K.K.W.C.; methodology, T.C.O.T., R.E.M., E.M.P. and K.K.W.C.; formal analysis, T.C.O.T., E.M.P. and K.K.W.C.; resources, R.E.M. and K.K.W.C.; data curation, R.E.M. and T.C.O.T.; writing—original draft preparation, T.C.O.T.; writing—review and editing, T.C.O.T., R.E.M., E.M.P. and K.K.W.C.; visualization, T.C.O.T.; supervision, E.M.P. and K.K.W.C.; project administration, R.E.M.; funding acquisition, T.C.O.T., E.M.P. and K.K.W.C. All authors have read and agreed to the published version of the manuscript.

### Institutional Review Board Statement

This study obtained research ethics approval from the Sunnybrook Research Institute (REB Project ID: 5714; approval date: 17 January 2025).

### Informed Consent Statement

Written informed consent was obtained from all subjects involved in the study.

### Data Availability Statement

The raw data supporting the conclusions of this article can be made available by the authors on request.

### Conflicts of Interest

Teresa Tsui is an employee of Canada’s Drug Agency. The current work was unrelated to her employment, and Canada’s Drug Agency had no role in the funding, design, or oversight of the work reported. The remaining authors declare no conflicts of interest.

### Abbreviations

The following abbreviations are used in this manuscript:

AD

Anxiety and depression

ANOVA

Analysis of variance

BIC

Bayesian Information Criterion

CI

Confidence interval

HRQoL

Health-related quality of life

HTA

Health technology assessment

MO

Mobility

OLS

Ordinary least squares

PD

Pain and discomfort

QALY

Quality-adjusted life year

SC

Self care

SD

Standard deviation

SES

Socioeconomic status

TTO

Time trade off

UA

Usual activity

VAS

Visual analogue scale

## References

1. Cella D.F. Quality of life outcomes: Measurement and validation. Oncology. 1996;10:233–246.

2. Guyatt G.H., Feeny D.H., Patrick D.L. Measuring health-related quality of life. Ann. Intern. Med. 1993;118:622–629. doi:10.7326/0003-4819-118-8-199304150-00009

3. Weinstein M.C., Torrance G., McGuire A. QALYs: The basics. Value Health. 2009;12((Suppl. S1)):S5–S9. doi:10.1111/j.1524-4733.2009.00515.x

4. National Institute for Health and Care Excellence. NICE Health Technology Evaluations: The Manual.

5. Canadian Agency for Drugs and Technologies in Health. Guidelines for the Economic Evaluation of Health Technologies. 2017. Ottawa, ON, Canada, Canadian Agency for Drugs and Technologies in Health.

6. Unger J.M., Hershman D.L., Fleury M.E., Vaidya R. Association of Patient Comorbid Conditions With Cancer Clinical Trial Participation. JAMA Oncol. 2019;5:326–333. doi:10.1001/jamaoncol.2018.5953

7. Unger J.M., Gralow J.R., Albain K.S., Ramsey S.D., Hershman D.L. Patient Income Level and Cancer Clinical Trial Participation: A Prospective Survey Study. JAMA Oncol. 2016;2:137–139. doi:10.1001/jamaoncol.2015.3924

8. Donzo M.W., Nguyen G., Nemeth J.K., Owoc M.S., Mady L.J., Chen A.Y., Schmitt N.C. Effects of socioeconomic status on enrollment in clinical trials for cancer: A systematic review. Cancer Med. 2024;13:e6905. doi:10.1002/cam4.6905

9. Asaria M., Griffin S., Cookson R. Distributional Cost-Effectiveness Analysis: A Tutorial. Med. Decis. Mak. 2016;36:8–19. doi:10.1177/0272989X15583266

10. Cookson R., Mirelman A.J., Griffin S., Asaria M., Dawkins B., Norheim O.F., Verguet S., Culyer A.J. Using Cost-Effectiveness Analysis to Address Health Equity Concerns. Value Health. 2017;20:206–212. doi:10.1016/j.jval.2016.11.027

11. Drummond M.F., Sculpher M.J., Claxton K., Stoddart G.L., Torrance G.W. Methods for the Economic Evaluation of Health Care Programmes. 2015. Oxford, UK, Oxford University Press.

12. Dolan P., Gudex C., Kind P., Williams A. A Social Tariff for EuroQol: Results from a UK General Population Survey. 1995. York, UK, Centre for Health Economics, University of York.

13. EuroQol Foundation. EQ-5D-3L User Guide. 2018. Rotterdam, The Netherlands, EuroQol Foundation.

14. Herdman M., Gudex C., Lloyd A., Janssen M., Kind P., Parkin D., Bonsel G., Badia X. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual. Life Res. 2011;20:1727–1736. doi:10.1007/s11136-011-9903-x

15. Devlin N., Parkin D., Janssen B. Methods for Analysing and Reporting EQ-5D Data. 2020. Cham, Switzerland, Springer Nature.

16. World Health Organization. A Conceptual Framework for Action on the Social Determinants of Health. Social Determinants of Health Discussion Paper 2.

17. Wilson I.B., Cleary P.D. Linking clinical variables with health-related quality of life. A conceptual model of patient outcomes. JAMA. 1995;273:59–65. doi:10.1001/jama.1995.03520250075037

18. Naik H., Howell D., Su S., Qiu X., Brown M.C., Vennettilli A., Irwin M., Pat V., Solomon H., Wang T. EQ-5D Health Utility Scores: Data from a Comprehensive Canadian Cancer Centre. Patient. 2017;10:105–115. doi:10.1007/s40271-016-0190-z

19. Huang W., Yang J., Liu Y., Liu C., Zhang X., Fu W., Shi L., Liu G. Assessing health-related quality of life of patients with colorectal cancer using EQ-5D-5L: A cross-sectional study in Heilongjiang of China. BMJ Open. 2018;8:e022711. doi:10.1136/bmjopen-2018-022711

20. Tura B.R., da Costa M.R., Lordello S., Barros D., Souza Y., da Silva Santos M. Health inequity assessment in Brazil: Is EQ-5D-3L sensible enough to detect differences among distinct socioeconomic groups?. Health Qual. Life Outcomes. 2024;22:22. doi:10.1186/s12955-024-02235-0

21. Booth C.M., Tannock I.F. Randomised controlled trials and population-based observational research: Partners in the evolution of medical evidence. Br. J. Cancer. 2014;110:551–555. doi:10.1038/bjc.2013.725

22. Tsui T.C.O., Mercer R.E., Zhou E.J., Desai R.K., Chatterje S., Yeung C.Y.L., Pullenayegum E.M., Chan K.K.W. Patient Experiences Regarding Feasibility of Implementing Real-World EQ-5D Collection at an Oncology Centre in Ontario, Canada. Curr. Oncol. 2025;32. doi:10.3390/curroncol32060308

23. Shaw C., Longworth L., Bennett B., McEntee-Richardson L., Shaw J.W. A Review of the Use of EQ-5D for Clinical Outcome Assessment in Health Technology Assessment, Regulatory Claims, and Published Literature. Patient. 2024;17:239–249. doi:10.1007/s40271-023-00662-7

24. Moskovitz M., Jao K., Su J., Brown M.C., Naik H., Eng L., Wang T., Kuo J., Leung Y., Xu W. Combined cancer patient-reported symptom and health utility tool for routine clinical implementation: A real-world comparison of the ESAS and EQ-5D in multiple cancer sites. Curr. Oncol. 2019;26:e733–e741. doi:10.3747/co.26.5297

25. Harrell F.E. Regression Modeling Strategies. 2015. Cham, Switzerland, Springer Nature.

26. Maxwell S.E., Kelley K., Rausch J.R. Sample size planning for statistical power and accuracy in parameter estimation. Annu. Rev. Psychol. 2008;59:537–563. doi:10.1146/annurev.psych.59.103006.093735

27. Janssen M.F., Szende A., Cabases J., Ramos-Goni J.M., Vilagut G., Konig H.H. Population norms for the EQ-5D-3L: A cross-country analysis of population surveys for 20 countries. Eur. J. Health Econ. 2019;20:205–216. doi:10.1007/s10198-018-0955-5

28. Reeve B.B., Graves K.D., Lin L., Potosky A.L., Ahn J., Henke D.M., Pan W., Fall-Dickson J.M. Health-related quality of life by race, ethnicity, and country of origin among cancer survivors. J. Natl. Cancer Inst. 2023;115:258–267. doi:10.1093/jnci/djac230

29. Morton F., Nijjar J. eq5d: Methods for Analysing ‘EQ-5D’ Data and Calculating ‘EQ-5D’ Index Scores. R package version 0.15.7. 2025.

30. Bansback N., Tsuchiya A., Brazier J., Anis A. Canadian valuation of EQ-5D health states: Preliminary value set and considerations for future valuation studies. PLoS ONE. 2012;7. doi:10.1371/journal.pone.0031115

31. Canadian Institute for Health Information. Guidance on the Use of Standards for Race-Based and Indigenous Identity Data Collection and Health Reporting in Canada.

32. Canadian Cancer Society. Canadian Cancer Statistics Dashboard.

33. Statistics Canada. Demographic Estimates by Age and Gender, Provinces and Territories: Interactive Dashboard.

34. Statistics Canada. Focus on Geography Series, 2021 Census of Population.

35. Statistics Canada. Table 11-10-0192-01 Upper Income Limit, Income Share and Average Income by Economic Family Type and Income Decile.

36. Canadian Cancer Society. Canadian Cancer Statistics Advisory Committee in Collaboration with the Canadian Cancer Society, Statistics Canada and the Public Health Agency of Canada. Canadian Cancer Statistics: A 2024 Special Report on the Economic Impact of Cancer in Canada.

37. Kangwanrattanakul K., Krageloh C.U. EQ-5D-3L and EQ-5D-5L population norms for Thailand. BMC Public Health. 2024;24. doi:10.1186/s12889-024-18391-3

38. Bailey H., Jonker M.F., Pullenayegum E., Rencz F., Roudijk B. EQ-5D-5L population norms and health inequality for Trinidad and Tobago in 2022–2023 and comparison with 2012. Health Qual. Life Outcomes. 2024;22:103. doi:10.1186/s12955-024-02323-1

39. Schwenkglenks M., Matter-Walstra K. Is the EQ-5D suitable for use in oncology? An overview of the literature and recent developments. Expert Rev. Pharmacoecon. Outcomes Res. 2016;16:207–219. doi:10.1586/14737167.2016.1146594

40. Moradi N., Poder T.G., Safari H., Mojahedian M.M., Ameri H. Psychometric properties of the EQ-5D-5L compared with EQ-5D-3L in cancer patients in Iran. Front. Oncol. 2022;12. doi:10.3389/fonc.2022.1052155

41. Meunier A., Longworth L., Kowal S., Ramagopalan S., Love-Koh J., Griffin S. Distributional Cost-Effectiveness Analysis of Health Technologies: Data Requirements and Challenges. Value Health. 2023;26:60–63. doi:10.1016/j.jval.2022.06.011

<figure id="curroncol-32-00645-f001">
<p><img src="curroncol-32-00645-g001.jpg" /></p>
<figcaption>Stacked bar plots of percentages of response level by dimension and income category. No participants selected income category CAD 90,000 to 119,999.</figcaption>
</figure>

<div id="curroncol-32-00645-t001" class="table-wrap">

curroncol-32-00645-t001_Table 1

<div class="caption">

Baseline characteristics of study participants.

</div>

<table>
<thead>
<tr>
<th style="text-align: center;">Variable<br />
</th>
<th style="text-align: center;">Study Participants<br />
(<em>n</em> = 170);<br />
Number (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Sex</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">Male</td>
<td style="text-align: center;">71 (41.8%)</td>
</tr>
<tr>
<td style="text-align: center;">Female</td>
<td style="text-align: center;">96 (56.5%)</td>
</tr>
<tr>
<td style="text-align: center;">Age</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">Mean (standard deviation)</td>
<td style="text-align: center;">64.5 (12.9)</td>
</tr>
<tr>
<td style="text-align: center;">Range</td>
<td style="text-align: center;">23 to 99</td>
</tr>
<tr>
<td style="text-align: center;">&lt;50</td>
<td style="text-align: center;">23 (13.5%)</td>
</tr>
<tr>
<td style="text-align: center;">50 to 74</td>
<td style="text-align: center;">111 (65.3%)</td>
</tr>
<tr>
<td style="text-align: center;">75 to 99</td>
<td style="text-align: center;">32 (18.8%)</td>
</tr>
<tr>
<td style="text-align: center;">Not disclosed</td>
<td style="text-align: center;">4 (2.4%)</td>
</tr>
<tr>
<td style="text-align: center;">Education</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">Did not attend college or university</td>
<td style="text-align: center;">38 (22.4%)</td>
</tr>
<tr>
<td style="text-align: center;">Attended college or university</td>
<td style="text-align: center;">127 (74.7%)</td>
</tr>
<tr>
<td style="text-align: center;">Other</td>
<td style="text-align: center;">3 (1.8%)</td>
</tr>
<tr>
<td style="text-align: center;">Not disclosed</td>
<td style="text-align: center;">2 (1.2%)</td>
</tr>
<tr>
<td style="text-align: center;">Marital status</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">Married or common law</td>
<td style="text-align: center;">115 (67.6%)</td>
</tr>
<tr>
<td style="text-align: center;">Other</td>
<td style="text-align: center;">55 (32.4%)</td>
</tr>
<tr>
<td style="text-align: center;">Employment status</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">Working full-time</td>
<td style="text-align: center;">43 (25.3%)</td>
</tr>
<tr>
<td style="text-align: center;">Other</td>
<td style="text-align: center;">25 (14.7%)</td>
</tr>
<tr>
<td style="text-align: center;">Unemployed</td>
<td style="text-align: center;">7 (4.1%)</td>
</tr>
<tr>
<td style="text-align: center;">Working part-time</td>
<td style="text-align: center;">10 (5.9%)</td>
</tr>
<tr>
<td style="text-align: center;">Retired</td>
<td style="text-align: center;">83 (48.8%)</td>
</tr>
<tr>
<td style="text-align: center;">Not disclosed</td>
<td style="text-align: center;">2 (1.2%)</td>
</tr>
<tr>
<td style="text-align: center;">Family Income *</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">&lt;CAD 29,999</td>
<td style="text-align: center;">17 (10.0%)</td>
</tr>
<tr>
<td style="text-align: center;">CAD 30,000–59,999</td>
<td style="text-align: center;">14 (8.2%)</td>
</tr>
<tr>
<td style="text-align: center;">CAD 60,000–89,999</td>
<td style="text-align: center;">12 (7.1%)</td>
</tr>
<tr>
<td style="text-align: center;">CAD 90,000–119,999</td>
<td style="text-align: center;">0 (0.0%)</td>
</tr>
<tr>
<td style="text-align: center;">CAD 120,000–149,999</td>
<td style="text-align: center;">11 (6.5%)</td>
</tr>
<tr>
<td style="text-align: center;">&gt;CAD 150,000</td>
<td style="text-align: center;">29 (17.1%)</td>
</tr>
<tr>
<td style="text-align: center;">Do not know</td>
<td style="text-align: center;">21 (12.4%)</td>
</tr>
<tr>
<td style="text-align: center;">Prefer not to answer</td>
<td style="text-align: center;">56 (32.9%)</td>
</tr>
<tr>
<td style="text-align: center;">Missing</td>
<td style="text-align: center;">10 (5.9%)</td>
</tr>
<tr>
<td style="text-align: center;">Ethnicity</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">White</td>
<td style="text-align: center;">108 (63.5%)</td>
</tr>
<tr>
<td style="text-align: center;">East, SE, or South Asian **</td>
<td style="text-align: center;">48 (28.2%)</td>
</tr>
<tr>
<td style="text-align: center;">Black</td>
<td style="text-align: center;">4 (2.4%)</td>
</tr>
<tr>
<td style="text-align: center;">Other population/race ***</td>
<td style="text-align: center;">7 (4.1%)</td>
</tr>
<tr>
<td style="text-align: center;">Prefer not to answer</td>
<td style="text-align: center;">3 (1.8%)</td>
</tr>
<tr>
<td style="text-align: center;">Primary Cancer Site</td>
<td style="text-align: center;"> </td>
</tr>
<tr>
<td style="text-align: center;">Breast</td>
<td style="text-align: center;">18 (10.6%)</td>
</tr>
<tr>
<td style="text-align: center;">Colorectal</td>
<td style="text-align: center;">12 (7.1%)</td>
</tr>
<tr>
<td style="text-align: center;">Genitourinary</td>
<td style="text-align: center;">5 (2.9%)</td>
</tr>
<tr>
<td style="text-align: center;">Gynecological</td>
<td style="text-align: center;">40 (23.5%)</td>
</tr>
<tr>
<td style="text-align: center;">Head and Neck</td>
<td style="text-align: center;">32 (18.8%)</td>
</tr>
<tr>
<td style="text-align: center;">Hematological</td>
<td style="text-align: center;">17 (10.0%)</td>
</tr>
<tr>
<td style="text-align: center;">Skin</td>
<td style="text-align: center;">9 (5.3%)</td>
</tr>
<tr>
<td style="text-align: center;">Thoracic</td>
<td style="text-align: center;">12 (7.1%)</td>
</tr>
<tr>
<td style="text-align: center;">Upper Gastrointestinal</td>
<td style="text-align: center;">13 (7.6%)</td>
</tr>
<tr>
<td style="text-align: center;">Other ****</td>
<td style="text-align: center;">12 (7.1%)</td>
</tr>
</tbody>
</table>

 \* Annual household income refers to fiscal year 2024 in Canadian dollars (CAD). \*\* All Asians were combined into one group, comprising East Asian, South Asian, Southeast Asian. \*\*\* Ethnicities in the other population/race group comprising responses from individuals who selected Other, Indigenous, Latin American, and Middle Eastern as per CIHI’s Guidance on the Use of Standards for Race-Based and Indigenous Identity Data Collection and Health Reporting in Canada \[31\]. \*\*\*\* Other primary cancer sites included cancers of the central nervous system, neuroendocrine cancers, other cancers, and missing cancer sites.

</div>

<div id="curroncol-32-00645-t002" class="table-wrap">

curroncol-32-00645-t002_Table 2

<div class="caption">

Cancer site, mean health utility (SD), and number of patients.

</div>

| Primary Cancer Site    | n   | Mean Utility | SD Utility |
|------------------------|-----|--------------|------------|
| Colorectal             | 12  | 0.918        | 0.127      |
| Skin                   | 9   | 0.819        | 0.096      |
| Breast                 | 18  | 0.815        | 0.162      |
| Hematological          | 17  | 0.802        | 0.172      |
| Head and Neck          | 32  | 0.757        | 0.170      |
| Gynecological          | 40  | 0.752        | 0.164      |
| Upper Gastrointestinal | 13  | 0.731        | 0.127      |
| Genitourinary          | 5   | 0.717        | 0.174      |
| Thoracic               | 12  | 0.712        | 0.254      |
| Other \*               | 12  | 0.848        | 0.141      |

\* Other categorization includes central nervous system, neuroendocrine, other, and missing cancer sites.

</div>

<div id="curroncol-32-00645-t003" class="table-wrap">

curroncol-32-00645-t003_Table 3

<div class="caption">

EQ-5D-3L dimension and Spearman’s rank correlation with income level.

</div>

| Dimension | Spearman’s ρ | *p*-Value |
|-----------|--------------|-----------|
| MO        | 0.114        | 0.306     |
| SC        | 0.103        | 0.353     |
| UA        | 0.199        | 0.071     |
| PD        | 0.291        | 0.008     |
| AD        | 0.219        | 0.046     |

MO: mobility. SC: self-care. UA: usual activity. PD: pain and discomfort. AD: anxiety and depression.

</div>

<div id="curroncol-32-00645-t004" class="table-wrap">

curroncol-32-00645-t004_Table 4

<div class="caption">

EQ-5D-3L health utility as the outcome predicted by socioeconomic status: two main effects models with and without sex-specific cancers.

</div>

<table>
<thead>
<tr>
<th style="text-align: center;"></th>
<th colspan="3" style="text-align: center;">Model Including Birth Sex Variable, No<br />
Participants with Sex-Specific Cancers<br />
(<em>n</em> = 111)</th>
<th colspan="3" style="text-align: center;">Model Excluding Birth Sex Variable, Including Participants with All Cancers<br />
(<em>n</em> = 170)</th>
</tr>
<tr>
<th style="text-align: center;">Variable</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">95% CI</th>
<th style="text-align: center;"><em>p</em>-Value</th>
<th style="text-align: center;">Estimate</th>
<th style="text-align: center;">95% CI</th>
<th style="text-align: center;"><em>p</em>-Value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">(Intercept)</td>
<td style="text-align: left;">0.866</td>
<td style="text-align: left;">(0.729 to 1.002)</td>
<td style="text-align: left;">&lt;0.001 ***</td>
<td style="text-align: left;">0.811</td>
<td style="text-align: left;">(0.718 to 0.903)</td>
<td style="text-align: left;">&lt;0.001 ***</td>
</tr>
<tr>
<td style="text-align: left;">Age</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">&lt;50</td>
<td style="text-align: left;">−0.029</td>
<td style="text-align: left;">(−0.156 to 0.099)</td>
<td style="text-align: left;">0.655</td>
<td style="text-align: left;">−0.035</td>
<td style="text-align: left;">(−0.118 to 0.049)</td>
<td style="text-align: left;">0.411</td>
</tr>
<tr>
<td style="text-align: left;">50 to 74</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">75 to 99</td>
<td style="text-align: left;">0.047</td>
<td style="text-align: left;">(−0.046 to 0.141)</td>
<td style="text-align: left;">0.317</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">(−0.070 to 0.080)</td>
<td style="text-align: left;">0.899</td>
</tr>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">−0.032</td>
<td style="text-align: left;">(−0.105 to 0.040)</td>
<td style="text-align: left;">0.377</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Education</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Did not attend<br />
college/<br />
university</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">(−0.088 to 0.094)</td>
<td style="text-align: left;">0.953</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">(−0.053 to 0.084)</td>
<td style="text-align: left;">0.652</td>
</tr>
<tr>
<td style="text-align: left;">Attended college or<br />
university</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: left;">0.060</td>
<td style="text-align: left;">(−0.193 to 0.313)</td>
<td style="text-align: left;">0.637</td>
<td style="text-align: left;">0.057</td>
<td style="text-align: left;">(−0.142 to 0.256)</td>
<td style="text-align: left;">0.571</td>
</tr>
<tr>
<td style="text-align: left;">Marital status</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Married or<br />
common law</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: left;">0.032</td>
<td style="text-align: left;">(−0.058 to 0.122)</td>
<td style="text-align: left;">0.480</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">(−0.026 to 0.098)</td>
<td style="text-align: left;">0.258</td>
</tr>
<tr>
<td style="text-align: left;">Employment status</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Working part-time</td>
<td style="text-align: left;">−0.018</td>
<td style="text-align: left;">(−0.187 to 0.152)</td>
<td style="text-align: left;">0.836</td>
<td style="text-align: left;">0.060</td>
<td style="text-align: left;">(−0.067 to 0.187)</td>
<td style="text-align: left;">0.353</td>
</tr>
<tr>
<td style="text-align: left;">Working full-time</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: left;">−0.043</td>
<td style="text-align: left;">(−0.172 to 0.087)</td>
<td style="text-align: left;">0.515</td>
<td style="text-align: left;">−0.042</td>
<td style="text-align: left;">(−0.127 to 0.043)</td>
<td style="text-align: left;">0.326</td>
</tr>
<tr>
<td style="text-align: left;">Unemployed</td>
<td style="text-align: left;">0.039</td>
<td style="text-align: left;">(−0.151 to 0.230)</td>
<td style="text-align: left;">0.682</td>
<td style="text-align: left;">0.062</td>
<td style="text-align: left;">(−0.076 to 0.200)</td>
<td style="text-align: left;">0.376</td>
</tr>
<tr>
<td style="text-align: left;">Retired</td>
<td style="text-align: left;">−0.013</td>
<td style="text-align: left;">(−0.114 to 0.089)</td>
<td style="text-align: left;">0.804</td>
<td style="text-align: left;">0.017</td>
<td style="text-align: left;">(−0.053 to 0.088)</td>
<td style="text-align: left;">0.628</td>
</tr>
<tr>
<td style="text-align: left;">Income</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">CAD 0–29K</td>
<td style="text-align: left;">−0.202</td>
<td style="text-align: left;">(−0.371 to −0.033)</td>
<td style="text-align: left;">0.020 *</td>
<td style="text-align: left;">−0.163</td>
<td style="text-align: left;">(−0.280 to −0.046)</td>
<td style="text-align: left;">0.007 **</td>
</tr>
<tr>
<td style="text-align: left;">CAD 30K–59K</td>
<td style="text-align: left;">−0.049</td>
<td style="text-align: left;">(−0.193 to 0.095)</td>
<td style="text-align: left;">0.503</td>
<td style="text-align: left;">−0.043</td>
<td style="text-align: left;">(−0.160 to 0.075)</td>
<td style="text-align: left;">0.474</td>
</tr>
<tr>
<td style="text-align: left;">CAD 60K–89K</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">(−0.142 to 0.169)</td>
<td style="text-align: left;">0.859</td>
<td style="text-align: left;">−0.013</td>
<td style="text-align: left;">(−0.131 to 0.104)</td>
<td style="text-align: left;">0.822</td>
</tr>
<tr>
<td style="text-align: left;">CAD 120K–149K</td>
<td style="text-align: left;">−0.032</td>
<td style="text-align: left;">(−0.177 to 0.113)</td>
<td style="text-align: left;">0.664</td>
<td style="text-align: left;">−0.041</td>
<td style="text-align: left;">(−0.160 to 0.078)</td>
<td style="text-align: left;">0.496</td>
</tr>
<tr>
<td style="text-align: left;">&gt;CAD 150K</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Do not know</td>
<td style="text-align: left;">−0.053</td>
<td style="text-align: left;">(−0.188 to 0.081)</td>
<td style="text-align: left;">0.433</td>
<td style="text-align: left;">−0.046</td>
<td style="text-align: left;">(−0.149 to 0.057)</td>
<td style="text-align: left;">0.377</td>
</tr>
<tr>
<td style="text-align: left;">Prefer not to<br />
answer</td>
<td style="text-align: left;">−0.123</td>
<td style="text-align: left;">(−0.235 to −0.012)</td>
<td style="text-align: left;">0.031 *</td>
<td style="text-align: left;">−0.106</td>
<td style="text-align: left;">(−0.184 to −0.028)</td>
<td style="text-align: left;">0.008 **</td>
</tr>
<tr>
<td style="text-align: left;">Primary cancer site</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Head and neck</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">Gynecological</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">(−0.064 to 0.099)</td>
<td style="text-align: left;">0.670</td>
</tr>
<tr>
<td style="text-align: left;">Breast</td>
<td style="text-align: left;">NA</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;">0.070</td>
<td style="text-align: left;">(−0.028 to 0.169)</td>
<td style="text-align: left;">0.162</td>
</tr>
<tr>
<td style="text-align: left;">Colorectal</td>
<td style="text-align: left;">0.135</td>
<td style="text-align: left;">(0.010 to 0.260)</td>
<td style="text-align: left;">0.034 *</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">(0.031 to 0.263)</td>
<td style="text-align: left;">0.013 *</td>
</tr>
<tr>
<td style="text-align: left;">Genitourinary <sup>@</sup></td>
<td style="text-align: left;">−0.118</td>
<td style="text-align: left;">(−0.315 to 0.079)</td>
<td style="text-align: left;">0.237</td>
<td style="text-align: left;">−0.066</td>
<td style="text-align: left;">(−0.230 to 0.097)</td>
<td style="text-align: left;">0.425</td>
</tr>
<tr>
<td style="text-align: left;">Hematological</td>
<td style="text-align: left;">0.043</td>
<td style="text-align: left;">(−0.078 to 0.163)</td>
<td style="text-align: left;">0.483</td>
<td style="text-align: left;">0.051</td>
<td style="text-align: left;">(−0.055 to 0.156)</td>
<td style="text-align: left;">0.346</td>
</tr>
<tr>
<td style="text-align: left;">Other</td>
<td style="text-align: left;">0.022</td>
<td style="text-align: left;">(−0.114 to 0.157)</td>
<td style="text-align: left;">0.753</td>
<td style="text-align: left;">0.035</td>
<td style="text-align: left;">(−0.092 to 0.162)</td>
<td style="text-align: left;">0.584</td>
</tr>
<tr>
<td style="text-align: left;">Skin</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">(−0.125 to 0.162)</td>
<td style="text-align: left;">0.801</td>
<td style="text-align: left;">0.043</td>
<td style="text-align: left;">(−0.090 to 0.175)</td>
<td style="text-align: left;">0.526</td>
</tr>
<tr>
<td style="text-align: left;">Thoracic</td>
<td style="text-align: left;">−0.033</td>
<td style="text-align: left;">(−0.159 to 0.094)</td>
<td style="text-align: left;">0.609</td>
<td style="text-align: left;">−0.024</td>
<td style="text-align: left;">(−0.139 to 0.091)</td>
<td style="text-align: left;">0.678</td>
</tr>
<tr>
<td style="text-align: left;">Upper gastrointestinal</td>
<td style="text-align: left;">−0.017</td>
<td style="text-align: left;">(−0.141 to 0.107)</td>
<td style="text-align: left;">0.785</td>
<td style="text-align: left;">−0.006</td>
<td style="text-align: left;">(−0.118 to 0.106)</td>
<td style="text-align: left;">0.912</td>
</tr>
<tr>
<td style="text-align: left;">Ethnicity</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">White</td>
<td style="text-align: left;">Reference</td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
<td style="text-align: left;"> </td>
</tr>
<tr>
<td style="text-align: left;">East/SE/South Asian</td>
<td style="text-align: left;">−0.015</td>
<td style="text-align: left;">(−0.097 to 0.068)</td>
<td style="text-align: left;">0.727</td>
<td style="text-align: left;">−0.017</td>
<td style="text-align: left;">(−0.076 to 0.043)</td>
<td style="text-align: left;">0.577</td>
</tr>
<tr>
<td style="text-align: left;">Other/Not<br />
Identified<br />
Elsewhere (NIE)</td>
<td style="text-align: left;">−0.046</td>
<td style="text-align: left;">(−0.256 to 0.163)</td>
<td style="text-align: left;">0.660</td>
<td style="text-align: left;">−0.089</td>
<td style="text-align: left;">(−0.229 to 0.051)</td>
<td style="text-align: left;">0.213</td>
</tr>
<tr>
<td style="text-align: left;">Black <sup>#</sup></td>
<td style="text-align: left;">−0.375</td>
<td style="text-align: left;">(−0.732 to −0.017)</td>
<td style="text-align: left;">0.040 *</td>
<td style="text-align: left;">−0.066</td>
<td style="text-align: left;">(−0.236 to 0.104)</td>
<td style="text-align: left;">0.444</td>
</tr>
</tbody>
</table>

Significance levels: \* *p* \< 0.05, \*\* *p* \< 0.01, \*\*\* *p* \< 0.001. <sup>\#</sup> One participant identified with being of black ethnicity; therefore, the estimate is very uncertain. <sup>@</sup> One participant with prostate cancer was removed from the analysis with *n* = 111 patients.

</div>

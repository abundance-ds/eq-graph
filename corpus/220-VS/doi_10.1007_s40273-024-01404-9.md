---
project_id: "220-VS"
work_id: "doi:10.1007/s40273-024-01404-9"
doi: "10.1007/s40273-024-01404-9"
pmid: "38954389"
pmcid: "PMC11343814"
title: "Estimating an EQ-5D-Y-3L Value Set for Brazil"
journal: "Pharmacoeconomics"
publication_date: "2024-07-02"
volume: "42"
issue: "9"
authors:
  - name: "Caique Melo Espirito Santo"
    affiliation_ids:
      - "Aff1"
  - name: "Gisela Cristiane Miyamoto"
    affiliation_ids:
      - "Aff1"
  - name: "Verônica Souza Santos"
    affiliation_ids:
      - "Aff1"
  - name: "Ângela Jornada Ben"
    affiliation_ids:
      - "Aff2"
  - name: "Aureliano Paolo Finch"
    affiliation_ids:
      - "Aff3"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff3"
  - name: "Fabianna Resende de Jesus-Moraleida"
    affiliation_ids:
      - "Aff4"
  - name: "Airton Tetelbom Stein"
    affiliation_ids:
      - "Aff5"
  - name: "Marisa Santos"
    affiliation_ids:
      - "Aff6"
  - name: "Tiê Parma Yamato"
    affiliation_ids:
      - "Aff1"
      - "Aff7"
      - "Aff8"
affiliations:
  - id: "Aff1"
    name: "Master’s and Doctoral Programs in Physical Therapy, Universidade Cidade de São Paulo, Rua Cesário Galeno, 448/475, Tatuapé, São Paulo, 03071-000 Brazil"
  - id: "Aff2"
    name: "Department of Health Sciences, Faculty of Science, Amsterdam Public Health Institute, Vrije Universiteit Amsterdam, Amsterdam, The Netherlands"
  - id: "Aff3"
    name: "EuroQol Research Foundation, Rotterdam, The Netherlands"
  - id: "Aff4"
    name: "Master Program in Physiotherapy and Functioning, Federal University of Ceará, Fortaleza, Brazil"
  - id: "Aff5"
    name: "Department of Public Health, Federal University of Health Sciences of Porto Alegre, Porto Alegre, Rio Grande do Sul Brazil"
  - id: "Aff6"
    name: "Instituto Nacional de Cardiologia, Rio de Janeiro, Brazil"
  - id: "Aff7"
    name: "Faculty of Medicine and Health, School of Health Sciences, The University of Sydney, Sydney, Australia"
  - id: "Aff8"
    name: "Nepean Blue Mountains Local Health District, Penrith, NSW Australia"
licence: "cc-by-nc"
source_file: "input/projects/220-VS/papers/doi_10.1007_s40273-024-01404-9.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11343814/fullTextXML"
source_method: "epmc_xml"
source_sha256: "819cffd610ec5aa47211c1d82bb8df6d122cacdb547fc23a19e5797280eb9fc3"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Estimating an EQ-5D-Y-3L Value Set for Brazil

## Abstract

### Introduction

The EQ-5D-Y-3L is a generic measure of health-related quality of life in children and adolescents. Although the Brazilian-Portuguese EQ-5D-Y-3L version is available, there is no value set for it, hampering its use in economic evaluations. This study aimed to elicit a Brazilian EQ-5D-Y-3L value set based on preferences of the general adult population.

### Methods

Two independent samples of adults participated in an online discrete choice experiment (DCE) survey and a composite time trade-off (cTTO) face-to-face interview. The framing was “*considering your views for a 10-year-old child*”. DCE data were analyzed using a mixed-logit model. The 243 DCE predicted values were mapped into the observed 28 cTTO values using linear and non-linear mapping approaches with and without intercept. Mapping approaches’ performance was assessed to estimate the most valid method to rescale DCE predicted values using the model fit (*R*<sup>2</sup>), Akaike Information Criteria (AIC), root mean squared error (RMSE), and mean absolute error (MAE).

### Results

A representative sample of 1376 Brazilian adults participated (DCE, 1152; cTTO, 211). The linear mapping without intercept (*R*<sup>2</sup> = 96%; AIC, − 44; RMSE, 0.0803; MAE, − 0.0479) outperformed the non-linear without intercept (*R*<sup>2</sup> = 98%; AIC, − 63; RMSE, 0.1385; MAE, − 0.1320). Utilities ranged from 1 (full health) to − 0.0059 (the worst health state). Highest weights were assigned to having pain or discomfort (pain/discomfort), followed by walking about (mobility), looking after myself (self-care), doing usual activities (usual activities), and feeling worried, sad, or unhappy (anxiety/depression).

### Conclusion

This study elicited the Brazilian EQ-5D-Y-3L value set using a mixed-logit DCE model with a power parameter based on a linear mapping without intercept, which can be used to estimate the quality-adjusted life-years for economic evaluations of health technologies targeting the Brazilian youth population.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40273-024-01404-9.

Accepted 2024 May 27; Issue date 2024.

## Infographic

<img src="40273_2024_1404_Figa_HTML.jpg" id="MO1" />

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| This study developed a national value set of the EQ-5D-Y-3L from the Brazilian population of adults. |
| The EQ-5D-Y-3L value set allows to calculate the quality-adjusted life-years in economic evaluations investigating health technologies for children and adolescents in Brazil. |
| This is the first study to estimate the EQ-5D-Y-3L value set in North, Central, and South America. |

</div>

## Introduction

There has been an increasing growth of interest in the development of generic preference-based measures specific to children and adolescents in the last decades \[1, 2\]. Among these instruments, the Adolescent Health Utility Measure (AHUM) \[3\], Assessment of Quality of Life-6 Dimensions (AQoL-6D) \[4\], Child Health Utility 9 Dimensions (CHU9D) \[5\], EQ-5D-Y-3L \[6\], Health Utility Index 2 (HUI2) \[7\], and Health Utility Index 3 (HUI3) \[8\] are some examples available in the literature. The EQ-5D-Y-3L is a generic instrument developed by the EuroQol Group to measure health-related quality of life (HRQoL) in children and adolescents aged 8–15 years old \[6, 9\]. This instrument was adapted from the adult instrument EQ-5D-3L, but with appropriate wording for children and adolescents \[6, 10\]. Its scoring system is based on value sets, which allow utilities to be calculated for conducting economic evaluations \[11\]. In addition, according to the literature, this instrument has been one of the most used in children and adolescents \[12\].

The process of recommendations for coverage and reimbursement for new medicines, devices, equipment, or interventions in the Brazilian Unified Health System (SUS) is conducted by the National Commission for Technology Incorporation, called CONITEC in Brazil \[13\]. This commission (that responds to the Ministry of Health) advises on incorporation, exclusion, or alteration based on health technology assessment (HTA) for adults and children, which includes measures of safety, efficacy, effectiveness, and cost-effectiveness \[13\]. The Brazilian Health Technology Assessment guideline recommends that cost-utility analysis using quality-adjusted life-years (QALYs) are employed as the main outcome \[14–16\]. However, the HTA recognizes that making decisions in the health system for adults and children should not be based only considering the QALYs, as other factors beyond this one are also relevant, including safety, efficacy, evidence, and other aspects (social, economic, and organizational) \[15, 16\]. The commission formulate recommendations for clinical protocols and therapeutic guidelines to be published through legal documents, including economic analysis guidelines publicly available \[15, 16\]. Since the introduction of the policy (April 2022) when economic evaluation became mandatory for decision-making related to the incorporation of health technologies in the Brazilian Public Healthcare System \[17\], there were 123 recommendations (76 for incorporations and 47 for nonincorporations) made by the commission \[18\]. The updated numbers of health technologies submitted to the commission in the Brazilian Unified Health System can be found elsewhere \[18\]. Furthermore, in November 2022, the Ministry of Health established a cost-effectiveness threshold of US\$ 15,834.49 (R\$40,000 Brazilian real) per QALY gained for health decision-making by the National Commission for Technology Incorporation—an alternative threshold \[valued up to US\$ 47,503.47 (R\$120,000)\] be considered for children and adolescents’ health conditions \[15, 19\]. This cost-effectiveness willingness to pay threshold represents a significant advancement for healthcare in Brazil, as it provides an additional parameter for the incorporation of new technologies \[15\]. QALYs is a measure that combines length of life and quality of life, and it can be calculated using a preference-based measure of health-related quality of life to describe patients’ health states \[20–23\]. These patients’ health states are converted into utilities using national value sets \[14, 21–23\]. Utilities represent individuals’ preferences for a given health state anchored on a scale between 0 (representing “dead”) and 1 (representing “full health”), with negative values representing a specific health state named “worse than dead” \[21\].

There are a few valuation methods to elicit preferences, such as visual analog scale \[24\], discrete choice experiment (DCE) \[25\], time trade-off (TTO) \[26\], and standard gamble \[27\]. Over the last decades, these valuation methods have been investigated and used to elicit the preferences, especially in adults, with the TTO being the main method used for the EQ-5D \[28\]. However, although these methods are considered robust and mature for the adult population, the valuation methods for children and adolescents seems to present unique challenges, as the methods are emergent and still evolving \[29, 30\]. The International Valuation Protocol of the EQ-5D-Y-3L is a first step in setting out the minimum requirements, but it is also expected that the learnings and findings from valuation studies will possibly provide method updates in the future \[29\]. Thus, it is important to understand the complexity of eliciting preferences and valuing health states for children and adolescents underscoring the importance of the use of appropriate methods to estimate it \[31\]. The main challenges are related to how well children and adolescents understand the tasks from the taxpayer’s perspective, as the values are used to inform health technology assessment and resources allocation \[30\]. Whereas for adults the challenge is to imagine being in a child's health state, for children it can be challenging to understand abstract concepts, hypothetical scenarios, or trade-offs between health states. Furthermore, there are ethical implications in asking children and adolescents about health states worse than “dead” \[32, 33\]. Therefore, the EuroQol Group has developed a protocol for valuing the EQ-5D-Y-3L, which involves adults completing valuation tasks, from a perspective of what they would prefer for a 10-year-old child \[10, 26, 30, 34\].

In contrast to the valuation methods of the EQ-5D-5L, the EQ-5D-Y-3L valuation consists of a two-step approach: an online DCE to estimate the relative importance of the levels and dimensions of the EQ-5D-Y-3L and collecting composite time trade-off (cTTO) in a smaller sample to anchor the DCE values onto 1 (full health) or 0 (dead) \[30\]. In the cTTO, a conventional TTO is used to value the health states considered better than dead and a lead-time TTO is used to value the health states considered worse than dead (negative values) \[30\]. Several countries such as Japan \[35\], Indonesian \[36\], Hungary \[37\], the Netherlands \[38\], Slovenia \[39\], Germany \[40\], Belgium \[41\], Spain \[42\], and China \[43\] also developed their EQ-5D-Y-3L value sets using the minimum requirements of International Valuation Protocol with different anchoring methods such as just the worst health state, hybrid modelling or mapping approaches. The International Valuation Protocol provides guidelines that serve as minimum requirements for valuing EQ-5D-Y-3L. Each respondent should complete 15 pairs of the DCE from 150 pairs distributed over 10 blocks with a minimum sample size of 1,000 respondents. For the cTTO, the interview should collect ten cTTO tasks/health states with 200 respondents \[30\]. Furthermore, authors can determine to have larger samples or even use more than those ten health states suggested for the cTTO, by the International Valuation Protocol. Different from the study conducted in Germany that considered ten health states, studies from Japan, China, Netherlands, and Indonesia considered adding more health states in the cTTO aiming to improve the estimate of the DCE-cTTO relationship \[35, 36, 38, 40, 43\].

In Brazil, only the EQ-5D-3L value set is available and the 243 health states of the EQ-5D-3L instrument were based on a sample of 3,362 literate individuals aged between 18-64 years old who lived in an urban area \[44, 45\]. There is no value set available for the EQ-5D-Y-3L in the Brazilian population that would allow to calculate the QALYs in economic evaluation. Therefore, this valuation study aimed to develop the value set of the EQ-5D-Y-3L instrument for Brazilian children and adolescents.

## Methods

### Study Design

This valuation study was conducted following the International Valuation Protocol of the EQ-5D-Y-3L and reported according to the Checklist for Reporting Valuation Studies of the EQ-5D (CREATE) \[30, 46\]. Details of the CREATE can be found in the Supplementary Information <a href="#MOESM1" data-ref-type="supplementary-material">1</a>. A two-step valuation approach using independent surveys with different samples and modes of administration was conducted in this study: an online structured self-completed survey with discrete choice experiment (DCE) tasks and face-to-face computer-assisted personal interviews with cTTO tasks. The language of DCE and cTTO surveys was Brazilian Portuguese. Both surveys included information on the study, informed consent, three introductory questions (i.e., age, gender, and experience with severe illness), the self-reported version of the EQ-5D-Y-3L, the valuation task, feedback questions, and complementary questions (e.g., educational level, marital status, socioeconomic level, religious beliefs, general health, health conditions, and pain conditions).

This study was approved by the Human Ethics Committee of the Universidade Cidade de São Paulo (UNICID) (CAAE: 45241321.6.0000.0064). DCE and cTTO surveys were conducted in a sample of adults aged 18 years or above from the general population who provided informed consent to participate in this study. The respondents were adults asked to do the tasks considering a child’s perspective (i.e., adults imagined the health state of a 10-year-old child). This choice was made on the basis of previous studies to possibly avoid ethical issues associated with the consideration of dead if a sample of children was used \[27, 44\].

### EQ-5D-Y-3L

This study used the Brazilian Portuguese version of the EQ-5D-Y-3L \[6\]. The EQ-5D-Y-3L is a child-friendly version adapted from the EQ-5D-3L instrument for measuring general health-related quality of life. The EQ-5D-Y-3L is composed of two parts: a descriptive system and a Visual Analog Scale (EQ-VAS). The descriptive system consists of five dimensions with appropriate age wording: walking about (mobility), looking after myself (self-care), doing usual activities (usual activities), having pain or discomfort (pain/discomfort), and feeling worried, sad, or unhappy (anxiety/depression). Each dimension has three levels of severity: (1) no problems/no pain or discomfort/not worried, sad, or unhappy; (2) some problems/some pain or discomfort/a bit worried, sad, or unhappy; and (3) a lot of problems/a lot of pain or discomfort/very worried, sad, or unhappy \[6\]. The responses generate a five-digit numeric code that expresses the child’s health state ranging from 11111 (full health, representing no problems in any domain) to 33333 (the worst health state, representing a lot of problems in all domains), totalizing 243 health states. The EQ-VAS ranges from 0 to 100, where 0 represents “the worst health state you can imagine” and 100 represents “the best health state you can imagine” \[6\].

### Valuation tasks

The DCE and cTTO tasks were conducted using the EuroQol Valuation Technology (EQ-VT) software (v2.1) \[28\]. Two valuation methods were used in this study: DCE and cTTO. The DCE and cTTO tasks were collected in two samples considering the perspective of the respondents for a 10-year-old child. In the DCE tasks, respondents expressed their preference between two different EQ-5D-Y-3L health states, classified as options A or B, and no specification of the duration of living in the health states was included \[30\].

The cTTO task consisted of a conventional time trade-off to elicit values for the health states considered “better than dead” (i.e., 10-year time trade-off) and a lead-time to elicit values for the states considered “worse than dead” \[47\] (i.e., 20-year time trade-off, 10 years in full health followed by 10 years in the health state), in which, the lowest tradable time trade-off was 6 months. Thus, respondents were asked to trade-off life-years in one hypothetical situation to identify the number of life-years in full health, where they would be indifferent for a kid to be living a shorter period of life-years in full health and a longer period of life-years in a specific health state \[26, 30\]. In this hypothetical situation, the respondent can prefer “life A,” “life B,” or consider “life A and B about the same” \[26\]. “Life A” corresponds to living with full health for a few years before death, and “life B” corresponds to living with full health before living a few years in a hypothetical health state from the EQ-5D-Y-3L before death \[26\]. Depending on the answer, the time of full health in “life A” changed, and the task finished when the respondent answered that “life A and B are about the same” (i.e., respondent’s point of indifference).

### Health State Selection

The DCE design consisted of 150 pairs of health states distributed over 10 blocks of 15 pairs. Each respondent was randomly allocated to complete one of the ten blocks. The order of the health state pair presentation and right/left presentation was randomized in each block. A two-dimension overlap was imposed for all pairs. Thus, the health states in each pair presented two dimensions with the same level of severity and three dimensions with different levels of severity. To help responders identify the differences between health states and reduce attribute non-attendance, a bold font was applied in the dimensions with level overlap \[48\]. The bold font was used as there is no color coding in the International Valuation Protocol \[30\]. Each respondent also completed three fixed dominant pairs for quality control. These dominant pairs were presented in the first pair, in the last pair, and at a random point. A dominant pair represents the health state that was always obviously better than the other (e.g., three dimensions with equal severity levels and two with worse severity levels). Thus, each respondent completed a total of 18 DCE tasks (15 health state pairs for valuation and three dominant pairs for quality control that were extensions of minimum requirements of the International Valuation Protocol). As DCE generates values on a latent scale, another valuation method is needed to anchor the utilities ranging from 1 to 0, where 1 represents “full health”, 0 represents “dead”, and negative values represent health states considered “worse than dead” \[30\]. The anchored utilities were developed through the cTTO task. The samples of the DCE and cTTO tasks were different, and those answering one did not participate in the other.

In the cTTO design, an orthogonal design including 18 health states was used \[49, 50\]. In addition to the orthogonal array, we considered the worst health state (33333), five mild health states (21111, 12111, 11211, 11121, and 11112), and four moderate health states to maintain near-orthogonality. In this study, the cTTO design consisted of 28 health states divided into 3 blocks of 10 health states (i.e., 9 health states per block, and the worst health state “33333” were included in all blocks). At least one mild health state was included in each block. Each respondent was randomly allocated to complete one of the three blocks. The order of the health states was also randomized. Before respondents completed the ten health states for the valuation study, each respondent valued two wheelchair examples considering a situation better than dead and another worse than dead, as well as three health states: a mild (21112), a severe (32323), and a health state difficult to imagine (13311). After the cTTO tasks, a ranking with all ten health states was presented to the respondents as an opportunity to verify if they agree with the rank ordering that is inferred from their responses. If necessary, inconsistencies flagging one or more cTTO valuations could be detected at this stage \[51\]. The average time for completing the cTTO task was around 60 min.

### Sampling, Recruitment, and Data Collection

The International Valuation Protocol for the EQ‐5D‐Y‐3L \[30\] recommends sample sizes of 1000 respondents for the DCE survey and 200 respondents for the cTTO survey. For the DCE, the respondents were recruited from general population, considering the proportional distribution of Brazilian regions according to the Brazilian Institute of Geography and Statistics (*Instituto Brasileiro de Geografia e Estatística—*IBGE) data (i.e., of the total sample, 8.9% were recruited from north region, 27% from northeast region, 7.8% from central-west region, 14.3% from south region, and 42% from southeast region) \[52\]. For the cTTO, the respondents were recruited from the general population in three urban centers from three Brazilian states: Sao Paulo (69.5% of the total sample, representing the southeast region), Rio Grande do Sul (17% of the total sample, from Rio Grande do Sul, representing the south region), and Ceara (27% of the total sample, representing the northeast region) states \[52\]. The total population from all these three urban centers represents 31.6% of the whole Brazilian population. Additionally, the population from Sao Paulo consisted of 45.5% immigrants from other Brazilian states, showing good cultural representativeness from different states of Brazil \[53\]. Furthermore, quotas were used for age (18–24 years, 25–34 years, 35–44 years, 45–54 years, 55–64 years, \> 65 years), sex (male and female), educational level (primary, middle, and high), and socioeconomic level based on the household income per month according to the Brazilian Association of Survey Companies \[classification ranges from A to D/E, as A represents a household higher than \$9678 (R\$25,000)/month and D/E represents a household lower than \$278 (R\$719)/month\] \[54\]. All quotas were considered for the recruitment of both surveys (DCE and cTTO).

Respondents were invited through a recruitment panel company for both surveys (DCE and cTTO). In the DCE approach, the respondents received a unique link by e-mail to access the DCE task. In the cTTO, the respondents were asked to attend a face-to-face interview at the local university according to their geographical location (e.g., Universidade Cidade de São Paulo in the Southeast region; Universidade Federal de Ciências da Saúde de Porto Alegre in the South region; and Universidade Federal do Ceará in the Northeast region). The interviews were conducted in private rooms and the respondents received a compensation for their transport and a food voucher.

The cTTO interviews were conducted by five interviewers, all of them working in research positions in the health area. Principal investigators of this study (GCM and TPY) received training from the EuroQol group on the valuation methods, EQ-VT protocol, and the quality control procedure. After the training, each principal investigator conducted ten pilot interviews with family and friends before offering standardized training for the interviewers. Interviewers received a 1-day hybrid training and a written script on the cTTO approach in Brazilian Portuguese. After the interviewers’ training, each interviewer conducted 10 pilot interviews with family and friends followed by 20 pilot interviews with the general population (assuring diverse socioeconomic and level educational background) before the data collection commenced. Although not all interviewers conducted 40 interviews in data collection because they were in Ceara and Rio Grande do Sul states (which needed a smaller number of interviews compared Sao Paulo state), our three interviewers from Sao Paulo state \[CMES (*n* = 50), (VSS *n* = 49), and GCM (*n* = 40)\] completed the interviews. Our interviewers had intensive training in conducting more pilot interviewers when compared to other conventional studies, and the data collection started when we reached an adequate quality of the interviewers following the quality control criteria from the EuroQol. Thus, we ensured that all interviewers (background in health area) had sufficient training and were guided by the principal investigators and also by the EuroQol group to maintain the quality of the interviews. During the pilot interviews and data collection, the interviewers shared their experiences as a group, and the principal investigators provided daily feedback on their performance. During data collection period, each interviewer performed a maximum of ten interviews per week to not overload the capacity of each interviewer. Data collection of the DCE and cTTO was performed from October to December 2022.

### Quality Control

According to recommendations from previous studies, all respondents in the DCE tasks who failed in any of the three dominant tasks (i.e., respondents preferred the obviously worse health state), and those “fast respondents” (i.e., respondents completed the DCE survey in less than 150–8.3 s/DCE task) were excluded from the final sample \[28, 39, 51\].

The quality control process consists of two main steps: (1) ensuring the protocol compliance and (2) investigating the presence of interviewer effects. In the first step (protocol compliance), we assessed four main criteria: (1) whether there was no explanation of the worse than dead task (lead-time) on the wheelchair example to each respondent; (2) whether a short time was spent on explaining the wheelchair examples (less than 3 min); (3) whether a short time was spent to complete all cTTO tasks (less than 5 min total time for completing the ten health states); and (4) whether there was any inconsistency in the cTTO responses (i.e., 33333 should be the lowest or at least 0.5 value higher than the health state with the lowest value) \[51\]. If at least one of the four criteria was met, the interview was flagged as an indication of potential poor quality. In the second step (presence of interviewer effects), we have monitored interviewer effects to ensure the data quality. The quality of the cTTO data was assessed every ten completed interviews (by each interviewer), using the quality control process defined by the EuroQol group \[51\]. The quality control process assesses interviewers’ performance related to interviewer effects and cTTO protocol compliance. Every week the data quality was discussed with the EQ-VT support team until completing cTTO data collection. After EQ-VT support team considerations, every week, the principal investigators discussed feedback on the performance and quality of the interviews with each interviewer to improve their skills.

### Data Analysis and Modeling

All statistical analyses were conducted with STATA v.15 (StataCorp, College Station, Texas, USA). Descriptive analysis was used to describe the characteristics of the respondents, the descriptive system of the EQ-5D-Y-3L, the EQ-VAS, and the cTTO values. Statistical analyses were conducted in two steps. In the first step, two different models were used to estimate the DCE values on a latent scale derived from the DCE responses, namely (1) a conditional logistic model and (2) a mixed-logit model. The DCE model was estimated using a mixed-logit model as it handles unobserved preferences heterogeneity by allowing the model parameters to vary across individuals \[55\]. The dependent variable was coded as 1 for the chosen option in each DCE task (e.g., ‘life A’) or as 0 for the alternative (e.g., ‘life B’). Dummy variables for response levels 2 and 3 in each EQ-5D-Y-3L dimension were included as covariates in both models. Bayesian Information Criteria (BIC) was used to select the best DCE model \[56\]. The coefficients derived from both models were used to calculate the predicted DCE values for all 243 health states of the EQ-5D-Y-3L (i.e., the DCE values).

In the second step, a mapping function was used to map the predicted DCE values onto the mean observed cTTO values for the 28 health states in the cTTO design exploring two mapping approaches: linear mapping (Eq. <a href="#Equ1" data-ref-type="disp-formula">1</a>) and non-linear mapping (Eq. <a href="#Equ2" data-ref-type="disp-formula">2</a>). The mapping function consisted of a regression model to identify the relationship between the predicted DCE values for the 243 health states and the mean observed cTTO values for the 28 health states considered in the cTTO survey design \[36, 37, 57\].

``` math
V_{\text{cTTOh}} = \gamma_{0} + \gamma_{1}V_{\text{DCEh}}
```

``` math
V_{\text{cTTOh}} = \gamma_{0} + \left( {\gamma_{1}V_{\text{DCEh}}} \right)^{\delta}
```

“*V*<sub>cTTOh</sub>” is the mean observed cTTO value for health state “h”, “*V*<sub>DCEh</sub>” is the predicted DCE value for the same health state “h”, “*γ*<sub>0</sub>” is the regression intercept, “*γ*<sub>1</sub>” is the slope between the cTTO and DCE values, and “δ” is a power parameter that may adjust for any possible non-linearity in the relationship between cTTO and DCE data. Linear and non-linear mapping models with and without intercept (including or excluding *γ*<sub>0</sub>, respectively) were applied. We structured the cTTO and DCE values as “disutilities” instead of “utilities” to facilitate the analysis (i.e., the cTTO and DCE values were scaled with 0 being the lowest value and least disutility, and the other values that were positive indicated greater disutility). To estimate the utilities of the 243 EQ-5D-Y-3L health states, we rescaled the coefficients of both DCE models based on rescaling parameters (i.e., the coefficients of the mapping approaches were considered with and without intercept) \[58\]. The intercept in the mapping model indicates an estimated mean utility when all EQ-5D health dimensions are zero. In general population samples, a relatively high proportion of responders score no problems in all EQ-5D dimensions leading to a large intercept, which can result in a gap between full health and the second-best health state. To partially deal with this gap, the mapping can be performed without the intercept in which utility decrements depend only on health dimensions coefficients size \[59\]. The preferred mapping approach was selected based on model fit. A relatively higher *R*<sup>2</sup> and a lower Akaike Information Criteria (AIC) value, root mean squared error (RMSE), and mean absolute error (MAE) indicate a better model fit and thus prediction accuracy \[58\].

## Results

### Respondent Characteristics

In total, 3006 individuals accepted to participate in this valuation study, 2790 for the DCE and 216 for the cTTO. For the DCE survey, 1638 individuals were excluded (1365 respondents did not complete all DCE tasks and 273 respondents completed the DCE tasks in less than 150 s or failed in the logically dominant pairs). Data from 1152 respondents were analyzed in the DCE. For the cTTO survey, only five scheduled respondents did not attend the interview and two interviews were flagged to be poor quality \[both interviews were flagged as they did not receive an explanation of the worse than dead task (lead-time) in the wheelchair example—note that those interviews were still considered in the final analyses\]. Data from the 211 respondents were analyzed in the cTTO.

Table <a href="#Tab1" data-ref-type="table">1</a> shows the sociodemographic characteristics, experience with severe illness, religious beliefs, general health, health conditions, and pain conditions. Both samples (DCE and cTTO) were similar in all characteristics, except for experiences with severe illness. Most respondents did not present any health or pain conditions at the moment of the data collection. Table <a href="#Tab2" data-ref-type="table">2</a> reports the EQ-5D-Y-3L responses for both samples. The EQ-VAS and response distribution of the EQ-5D-Y-3L were also similar in both samples.

<div id="Tab1" class="table-wrap">

<div class="caption">

Characteristics of respondents

</div>

| Variables | cTTO sample (*n* = 211) | DCE sample (*n* = 1152) |
|----|----|----|
| Age (years), mean (SD) | 42 (15.3) | 39.9 (12.4) |
| Gender, *n* (%) |  |  |
|  Female | 115 (54.5) | 577 (50.1) |
|  Male | 95 (45.0) | 572 (49.6) |
|  Other | 1 (0.5) | 3 (0.3) |
| Marital status<sup>a</sup> |  |  |
|  Single | 95 (45.0) | 448 (39.8) |
|  Living together | 23 (10.9) | 129 (11.5) |
|  Married | 64 (30.3) | 425 (37.8) |
|  Separated | 5 (2.4) | 31 (2.8) |
|  Divorced | 16 (7.6) | 76 (6.8) |
|  Widow(er) | 8 (3.8) | 16 (1.4) |
| Educational level, *n* (%)<sup>a</sup> |  |  |
|  Low | 9 (4.3) | 38 (3.4) |
|  Moderate | 95 (45) | 446 (39.7) |
|  High | 107 (50.7) | 641 (56.9) |
| Region, *n* (%) |  |  |
|  South | 34 (16.1) | 165 (14) |
|  Southeast | 150 (71.1) | 484 (42) |
|  North | 0 | 103 (9) |
|  Northeast | 27 (12.8) | 311 (27) |
|  Central west | 0 | 90 (8) |
| Socioeconomic level, *n* (%)<sup>b</sup> |  |  |
|  Class A1/A2 | 64 (30.4) | 305 (27.2) |
|  Class B1 | 76 (36.0) | 346 (30.8) |
|  Class B2 | 43 (20.4) | 254 (22.6) |
|  Class C1 | 24 (11.4) | 140 (12.5) |
|  Class C2 | 2 (0.9) | 35 (3.1) |
|  Class D/E | 2 (0.9) | 43 (3.8) |
| Religion, *n* (%)<sup>c</sup> |  |  |
|  Agnostic | 16 (7.6) | 50 (4.4) |
|  Buddhism | 2 (0.9) | 3 (0.3) |
|  Ecumenical | 2 (0.9) | 2 (0.2) |
|  Umbandista/candomblé | 10 (4.7) | 10 (0.9) |
|  Wicca | 0 | 1 (0.1) |
|  Islam | 0 | 2 (0.2) |
|  Rationalism | 0 | 1 (0.1) |
|  Jewish | 0 | 1 (0.1) |
|  Catholic | 82 (38.9) | 403 (35.9) |
|  Protestantism | 62 (29.5) | 315 (28.0) |
|  Adventism | 1 (0.5) | 17 (1.5) |
|  Anglicanism |  | 3 (0.3) |
|  Mormonism | 2 (0.9) | 3 (0.3) |
|  Eastern Orthodox Church | 0 | 5 (0.4) |
|  Jehovah's Witnesses | 0 | 29 (2.6) |
|  Spiritualism | 14 (6.6) | 97 (8.6) |
|  Atheism | 5 (2.4) | 35 (3.1) |
|  Do not want to declare | 15 (7.1) | 145 (12.9) |
| Experienced serious illness, *n* (%) |  |  |
|  In yourself |  |  |
|  Yes | 113 (53.5) | 258 (22.4) |
|  No | 98 (46.5) | 894 (77.6) |
|  In your family |  |  |
|  Yes | 158 (74.9) | 759 (65.9) |
|  No | 53 (25.1) | 393 (34.1) |
|  In caring for others |  |  |
|  Yes | 59 (28.0) | 322 (27.9) |
|  No | 152 (72.0) | 830 (72.1) |
| Overall health, *n* (%)<sup>c</sup> |  |  |
|  Very good | 61 (28.9) | 276 (24.6) |
|  Good | 104 (49.3) | 605 (53.9) |
|  Neither good or bad | 39 (18.5) | 208 (18.5) |
|  Bad | 5 (2.4) | 30 (2.7) |
|  Very bad | 2 (0.9) | 3 (0.3) |
| Health problems, *n* (%)<sup>c</sup> |  |  |
|  None | 137 (64.9) | 766 (68.3) |
|  Metabolic disorder | 18 (8.5) | 85 (7.6) |
|  Cancer | 2 (0.9) | 11 (1.0) |
|  HIV | 1 (0.5) | 2 (0.2) |
|  Rheumatological diseases | 9 (4.3) | 65 (7.8) |
|  Neurological diseases | 3 (1.4) | 19 (1.7) |
|  Respiratory diseases | 7 (3.3) | 38 (3.4) |
|  Cardiovascular diseases | 35 (16.1) | 58 (5.2) |
|  Mental disorders | 7 (5.2) | 34 (3.0) |
|  Eye Disorders | 1 (0.5) | 11 (1.0) |
|  Gastrointestinal diseases | 2 (0.9) | 17 (1.5) |
|  Hearing loss | 0 | 2 (0.2) |
|  Thyroid diseases | 5 (2.4) | 8 (0.7) |
|  Urologic diseases | 5 (2.4) | 10 (0.9) |
|  Osteoporosis | 1 (0.5) | 1 (0.1) |
| Pain condition, *n* (%)<sup>c</sup> |  |  |
|  None | 134 (63.5) | 662 (59.0) |
|  Fibromyalgia | 4 (1.9) | 29 (2.6) |
|  Migraine/headache | 20 (9.5) | 255 (22.7) |
|  Irritable bowel syndrome | 1 (0.5) | 41 (3.6) |
|  Thoracic/low back pain | 23 (10.9) | 137 (12.2) |
|  Neck pain | 8 (3.8) | 58 (5.2) |
|  Bursitis/tendinitis | 2 (0.9) | 13 (1.1) |
|  Muscle pain and cramp | 0 | 7 (0.6) |
|  Knee pain | 13 (6.2) | 9 (0.8) |
|  Leg pain | 4 (1.9) | 6 (0.5) |
|  Abdominal pain | 3 (1.4) | 5 (0.4) |
|  Feet pain | 2 (0.9) | 3 (0.3) |
|  Arm/shoulder pain | 4 (1.9) | 4 (0.4) |
|  Carpal tunnel syndrome/hand pain | 0 | 3 (0.3) |
|  Hip pain | 2 (0.9) | 3 (0.3) |
|  Temporomandibular pain | 0 | 2 (0.2) |

*cTTO* composite time trade-off, *DCE* discrete choice experiment, *SD* standard deviation; *n* (%), number absolute and percentage.

<sup>a</sup>DCE sample, 1125

<sup>b</sup>DCE sample, 1123

<sup>c</sup>DCE sample, 1122

</div>

<div id="Tab2" class="table-wrap">

<div class="caption">

EQ-5D-Y-3L responses for the DCE and cTTO samples

</div>

| EQ-5D-Y-3L | cTTO sample (*n* = 211) | DCE sample (*n* = 1152) |
|----|----|----|
| Mobility (walking about), *n* (%) |  |  |
|  No | 172 (81.5) | 1015 (88.1) |
|  Some | 37 (17.6) | 129 (11.2) |
|  A lot of | 2 (0.9) | 8 (0.7) |
| Looking after myself, *n* (%) |  |  |
|  No | 208 (98.6) | 1101 (95.6) |
|  Some | 3 (1.4) | 49 (4.2) |
|  A lot of | 0 | 2 (0.2) |
| Doing usual activities, *n* (%) |  |  |
|  No | 180 (85.3) | 972 (84.4) |
|  Some | 28 (13.3) | 173 (15.0) |
|  A lot of | 3 (1.4) | 7 (0.6) |
| Having pain or discomfort, *n* (%) |  |  |
|  No | 132 (63.6) | 590 (51.2) |
|  Some | 73 (34.6) | 543 (47.1) |
|  A lot of | 6 (2.8) | 19 (1.7) |
| Feeling worried, sad, or unhappy, *n* (%) |  |  |
|  Not | 119 (56.4) | 496 (43.1) |
|  A bit | 82 (38.9) | 590 (51.2) |
|  Very | 10 (4.7) | 66 (5.7) |
| EQ-VAS | 81.6 (16.7) | 80.0 (17.2) |

*cTTO* composite time trade-off; DCE, discrete choice experiment; EQ-VAS, visual analog scale; *n* = sample size; *n* (%), number absolute and percentage

</div>

### Description of the cTTO data

Table <a href="#Tab3" data-ref-type="table">3</a> describes the mean cTTO values for the 28 health states of the EQ-5D-Y-3L. The highest mean cTTO value was 0.955 \[standard deviation (SD): 0.050\] for the health state “12111,” and the lowest mean cTTO value was − 0.280 (SD: 0.577) for the health state “33333”, which was the only negative observed mean value. The distribution of cTTO values is presented in the Fig. <a href="#Fig1" data-ref-type="fig">1</a>.

<div id="Tab3" class="table-wrap">

<div class="caption">

Block design for composite time trade-off

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Block 1<br />
<em>n</em> = 57</th>
<th style="text-align: left;">Level sum<br />
score</th>
<th style="text-align: left;">Severity</th>
<th style="text-align: left;">Mean value (SD)</th>
<th style="text-align: left;">Block 2<br />
<em>n</em> = 70</th>
<th style="text-align: left;">Level sum<br />
score</th>
<th style="text-align: left;">Severity</th>
<th style="text-align: left;">Mean value (SD)</th>
<th style="text-align: left;">Block 3<br />
<em>n</em> = 84</th>
<th style="text-align: left;">Level sum<br />
score</th>
<th style="text-align: left;">Severity</th>
<th style="text-align: left;">Mean value (SD)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">11121</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.900 (0.151)</td>
<td style="text-align: left;">21111</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.955 (0.050)</td>
<td style="text-align: left;">12111</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.932 (0.088)</td>
</tr>
<tr>
<td style="text-align: left;">11112</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.952 (0.073)</td>
<td style="text-align: left;">11122</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.878 (0.206)</td>
<td style="text-align: left;">11211</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.933 (0.098)</td>
</tr>
<tr>
<td style="text-align: left;">11313</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.732 (0.221)</td>
<td style="text-align: left;">12212</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.827 (0.116)</td>
<td style="text-align: left;">21211</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">Mild</td>
<td style="text-align: left;">0.836 (0.145)</td>
</tr>
<tr>
<td style="text-align: left;">31131</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.562 (0.336)</td>
<td style="text-align: left;">13221</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.761 (0.145)</td>
<td style="text-align: left;">22121</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.746 (0.158)</td>
</tr>
<tr>
<td style="text-align: left;">32113</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.578 (0.255)</td>
<td style="text-align: left;">23112</td>
<td style="text-align: left;">9</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.766 (0.143)</td>
<td style="text-align: left;">21133</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.575 (0.336)</td>
</tr>
<tr>
<td style="text-align: left;">12331</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.492 (0.277)</td>
<td style="text-align: left;">22222</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.598 (0.274)</td>
<td style="text-align: left;">21323</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.487 (0.346)</td>
</tr>
<tr>
<td style="text-align: left;">33311</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.524 (0.306)</td>
<td style="text-align: left;">31223</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.541 (0.289)</td>
<td style="text-align: left;">22233</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.263 (0.480)</td>
</tr>
<tr>
<td style="text-align: left;">13133</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.482 (0.257)</td>
<td style="text-align: left;">21332</td>
<td style="text-align: left;">11</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.511 (0.304)</td>
<td style="text-align: left;">23323</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">Severe</td>
<td style="text-align: left;">0.134 (0.527)</td>
</tr>
<tr>
<td style="text-align: left;">32322</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.323 (0.405)</td>
<td style="text-align: left;">32232</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;">Moderate</td>
<td style="text-align: left;">0.346 (0.403)</td>
<td style="text-align: left;">33232</td>
<td style="text-align: left;">13</td>
<td style="text-align: left;">Severe</td>
<td style="text-align: left;">0.098 (0.510)</td>
</tr>
<tr>
<td style="text-align: left;">33333*</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">Severe</td>
<td style="text-align: left;">−0.280 (0.577)</td>
<td style="text-align: left;"></td>
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

*SD* standard deviation

\*The health state 33333 was included in all blocks (*n* = 211).

The severity was estimated by the sum of the five-digit code of the EQ-5D-Y-3L health state, which represents the response level in each dimension (level sum score ranging from 5 to 15, where 5 to 7 represents mild health state, 8 to 12 represents moderate health state, and \>12 represents severe health state)

</div>

<figure id="Fig1">
<p><img src="40273_2024_1404_Fig1_HTML.jpg" id="MO2" /></p>
<p><img src="40273_2024_1404_Fig1_HTML.gif" /></p>
<figcaption>The density distribution of the 28 observed composite time trade-off (cTTO) values</figcaption>
</figure>

### Description of the DCE data

Table <a href="#Tab4" data-ref-type="table">4</a> shows the results from the conditional logistic regression model and the mixed-logit model on the DCE data. In both models, all coefficients were statistically significant (*p* \< 0.001). Both models resulted in a larger coefficient magnitude in each domain with a more severe response level (i.e., level 3 indicated a lot of problems/a lot of pain or discomfort/very worried, sad, or unhappy). For the conditional logistic model, walking about (mobility) received the largest weight, followed by having pain or discomfort, looking after myself, doing usual activities, and feeling worried, sad, or unhappy. For the mixed-logit model, having pain or discomfort received the largest weight, followed by walking about (mobility), looking after myself, doing usual activities, and feeling worried, sad, or unhappy. In both models, feeling worried, sad, or unhappy with moderate response level (i.e., level 2 indicated some problems/some pain or discomfort/a bit worried, sad, or unhappy) received the smallest weight. The best DCE model was the mixed-logit model, as it demonstrates better goodness of fit than the conditional logistic model with lower BIC (22613 versus 23979, respectively).

<div id="Tab4" class="table-wrap">

<div class="caption">

Discrete choice experiment models

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">EQ-5D-Y-3L level</th>
<th colspan="4" style="text-align: left;">Conditional logistic regression model</th>
<th colspan="4" style="text-align: left;">Mixed logit model</th>
</tr>
<tr>
<th style="text-align: left;">Coefficients</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;"><em>p</em> value</th>
<th style="text-align: left;">Coefficients</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;"><em>p</em> value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility 2</td>
<td style="text-align: left;">− 0.803</td>
<td style="text-align: center;">0.040</td>
<td style="text-align: left;">− 0.881 to − 0.724</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.998</td>
<td style="text-align: center;">0.058</td>
<td style="text-align: left;">− 1.112 to − 0.885</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Mobility 3</td>
<td style="text-align: left;">− 1.451</td>
<td style="text-align: center;">0.050</td>
<td style="text-align: left;">− 1.549 to − 1.353</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.827</td>
<td style="text-align: center;">0.074</td>
<td style="text-align: left;">− 1.972 to − 1.682</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 2</td>
<td style="text-align: left;">− 0.677</td>
<td style="text-align: center;">0.030</td>
<td style="text-align: left;">− 0.736 to − 0.618</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.820</td>
<td style="text-align: center;">0.044</td>
<td style="text-align: left;">− 0.907 to − 0.733</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 3</td>
<td style="text-align: left;">− 1.177</td>
<td style="text-align: center;">0.042</td>
<td style="text-align: left;">− 1.259 to − 1.095</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.525</td>
<td style="text-align: center;">0.059</td>
<td style="text-align: left;">− 1.641 to − 1.409</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 2</td>
<td style="text-align: left;">− 0.662</td>
<td style="text-align: center;">0.030</td>
<td style="text-align: left;">− 0.720 to − 0.604</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.8261</td>
<td style="text-align: center;">0.043</td>
<td style="text-align: left;">− 0.9101 to − 0.741</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 3</td>
<td style="text-align: left;">− 1.144</td>
<td style="text-align: center;">0.037</td>
<td style="text-align: left;">− 1.217 to − 1.071</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.484</td>
<td style="text-align: center;">0.056</td>
<td style="text-align: left;">− 1.593 to − 1.375</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 2</td>
<td style="text-align: left;">− 0.635</td>
<td style="text-align: center;">0.028</td>
<td style="text-align: left;">− 0.691 to − 0.579</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.875</td>
<td style="text-align: center;">0.045</td>
<td style="text-align: left;">− 0.963 to − 0.788</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 3</td>
<td style="text-align: left;">− 1.346</td>
<td style="text-align: center;">0.037</td>
<td style="text-align: left;">− 1.418 to − 1.274</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.892</td>
<td style="text-align: center;">0.069</td>
<td style="text-align: left;">− 2.027 to − 1.756</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 2</td>
<td style="text-align: left;">− 0.325</td>
<td style="text-align: center;">0.032</td>
<td style="text-align: left;">− 0.388 to − 0.261</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.484</td>
<td style="text-align: center;">0.046</td>
<td style="text-align: left;">− 0.574 to − 0.394</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 3</td>
<td style="text-align: left;">− 0.969</td>
<td style="text-align: center;">0.038</td>
<td style="text-align: left;">− 1.043 to − 0.895</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.309</td>
<td style="text-align: center;">0.060</td>
<td style="text-align: left;">− 1.426 to − 1.192</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">BIC</td>
<td style="text-align: left;">23,979</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">22,613</td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

*BIC* Bayesian Information Criteria, *95% CI* 95% Confidence Interval, *SE* Standard Error

</div>

### Mapping results

Table <a href="#Tab5" data-ref-type="table">5</a> shows the results of four different mapping functions used to define the relationship between predicted DCE values and mean observed cTTO values: linear mapping with (column 1) and without (column 2) intercept, and non-linear mapping with (column 3) and without (column 4) intercept. Figure <a href="#Fig2" data-ref-type="fig">2</a> shows the relationship between the mapped DCE derived values and the observed cTTO values across all tested mapping functions. The mapping functions were conducted considering only the data derived from the mixed-logit model, as it assumes responses are correlated within participants. The mixed-logit model also considers preference heterogeneity providing a more precise estimate given that respondents are allowed to differ in their preferences. The linear mapping without intercept presented a higher R-squared and an AIC value but lower RMSE and MAE compared to the linear mapping with intercept, indicating a relatively better fit. Despite a slightly lower *R*<sup>2</sup> and a higher AIC value, the linear mapping without intercept presented lower RMSE and MAE compared with the non-linear mapping approaches, suggesting a relatively better fit, especially in predicting moderate health states as shown in Fig. <a href="#Fig2" data-ref-type="fig">2</a>. The linear mapping without the intercept was, therefore, selected as the preferred approach to describe the relationship between the predicted DCE values and the observed cTTO disutilities (Table <a href="#Tab5" data-ref-type="table">5</a> and Fig. <a href="#Fig2" data-ref-type="fig">2</a>).

<div id="Tab5" class="table-wrap">

<div class="caption">

Estimation results for linear and non-linear mapping using mixed logit model

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;">Model parameters and fit statistics</th>
<th colspan="4" style="text-align: left;">Mixed-logit model</th>
</tr>
<tr>
<th style="text-align: left;">Linear mapping</th>
<th style="text-align: left;">Linear mapping (no intercept)</th>
<th style="text-align: left;">Non-linear mapping</th>
<th style="text-align: left;">Non-linear mapping (no intercept)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Intercept</td>
<td style="text-align: left;">−  0.1115</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">0.0606</td>
<td style="text-align: left;">–</td>
</tr>
<tr>
<td style="text-align: left;">Coefficient (SE)</td>
<td style="text-align: left;">0.1501(0.0387)</td>
<td style="text-align: left;">0.1251 (0.0052)</td>
<td style="text-align: left;">0.1443</td>
<td style="text-align: left;">0.1480</td>
</tr>
<tr>
<td style="text-align: left;">Power</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">1.7897</td>
<td style="text-align: left;">1.5398</td>
</tr>
<tr>
<td style="text-align: left;"><em>R</em><sup>2</sup></td>
<td style="text-align: left;">0.9003</td>
<td style="text-align: left;">0.9560</td>
<td style="text-align: left;">0.9785</td>
<td style="text-align: left;">0.9773</td>
</tr>
<tr>
<td style="text-align: left;">AIC</td>
<td style="text-align: left;">– 50</td>
<td style="text-align: left;">− 44</td>
<td style="text-align: left;">− 63</td>
<td style="text-align: left;">− 63</td>
</tr>
<tr>
<td style="text-align: left;">RMSE</td>
<td style="text-align: left;">0.1450</td>
<td style="text-align: left;">0.0803</td>
<td style="text-align: left;">0.1271</td>
<td style="text-align: left;">0.1385</td>
</tr>
<tr>
<td style="text-align: left;">MAE</td>
<td style="text-align: left;">−0.1398</td>
<td style="text-align: left;">− 0.0479</td>
<td style="text-align: left;">− 0.1185</td>
<td style="text-align: left;">− 0.1320</td>
</tr>
<tr>
<td style="text-align: left;">Predicted value profile 33333</td>
<td style="text-align: left;">−0.2066</td>
<td style="text-align: left;">− 0.0059</td>
<td style="text-align: left;">− 0.1601</td>
<td style="text-align: left;">− 0.1896</td>
</tr>
</tbody>
</table>

*SE* standard error, *MAE* mean absolute error, *RMSE* root mean squared error, *AIC* Akaike Information Criterion

</div>

<figure id="Fig2">
<p><img src="40273_2024_1404_Fig2_HTML.jpg" id="MO3" /></p>
<p><img src="40273_2024_1404_Fig2_HTML.gif" /></p>
<figcaption>Scatterplots showing the relationship between the predicted DCE values and observed cTTO disutility values. <strong>A</strong> Linear mapping with intercept; <strong>B</strong>) Linear mapping without intercept; C) Non-linear mapping with intercept; and D) Non-linear mapping without intercept. <em>cTTO </em>composite time-trade off,<em> DCE </em>discrete choice experiment,<em> cTTOd </em>observed cTTO disutility values</figcaption>
</figure>

The linear mapping without intercept was selected as the preferred approach to rescale the predicted DCE values. All mixed-logit coefficients were multiplied by the rescaling parameter identified by the linear mapping without intercept, namely 0.125148. Therefore, the final model used for the value set is presented in the following algorithm:

``` math
U = 1 - ((0.9982155{} \ast 0.125148{} \ast MO2) + (1.827159{} \ast 0.125148{} \ast MO3) + (0.8202576{} \ast 0.125148{} \ast SC2) + (1.525397{} \ast 0.125148{} \ast SC3) + (0.8257411{} \ast 0.125148{} \ast UA2) + (1.484434{} \ast 0.125148{} \ast UA3) + (0.87543136{} \ast 0.125148{} \ast PD2) + (1.891593{} \ast 0.125148{} \ast PD3) + (0.4842359{} \ast 0.125148{} \ast AD2) + (1.309006{} \ast 0.125148{} \ast AD3))
```

For example, in this value set, the health state 13231 would be assigned the value *U* = 1 – (0.1908 + 0.1033 + 0.237), which equals 0.4692. The final model ranged from 1 for “full health” (11111) to – 0.0059 for “the worst health state” (33333), which was the only negative utilities of the whole elicited value set. Table <a href="#Tab6" data-ref-type="table">6</a> provides the utilities for all 243 health profiles of the EQ-5D-Y-3L.

<div id="Tab6" class="table-wrap">

<div class="caption">

Utilities for all 243 health profiles of the EQ-5D-Y-3L

</div>

| Profile | Utilities | Profile | Utilities | Profile | Utilities | Profile | Utilities | Profile | Utilities | Profile | Utilities | Profile | Utilities |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 11111 | 1 | 12212 | 0.733 | 13313 | 0.460 | 22121 | 0.663 | 23222 | 0.411 | 31323 | 0.312 | 33131 | 0.344 |
| 11112 | 0.939 | 12213 | 0.630 | 13321 | 0.514 | 22122 | 0.602 | 23223 | 0.307 | 31331 | 0.349 | 33132 | 0.283 |
| 11113 | 0.836 | 12221 | 0.684 | 13322 | 0.453 | 22123 | 0.499 | 23231 | 0.344 | 31332 | 0.288 | 33133 | 0.180 |
| 11121 | 0.890 | 12222 | 0.624 | 13323 | 0.350 | 22131 | 0.536 | 23232 | 0.284 | 31333 | 0.185 | 33211 | 0.477 |
| 11122 | 0.830 | 12223 | 0.521 | 13331 | 0.387 | 22132 | 0.475 | 23233 | 0.180 | 32111 | 0.669 | 33212 | 0.416 |
| 11123 | 0.727 | 12231 | 0.557 | 13332 | 0.326 | 22133 | 0.372 | 23311 | 0.498 | 32112 | 0.608 | 33213 | 0.313 |
| 11131 | 0.763 | 12232 | 0.497 | 13333 | 0.223 | 22211 | 0.669 | 23312 | 0.438 | 32113 | 0.505 | 33221 | 0.367 |
| 11132 | 0.703 | 12233 | 0.393 | 21111 | 0.875 | 22212 | 0.608 | 23313 | 0.335 | 32121 | 0.559 | 33222 | 0.307 |
| 11133 | 0.599 | 12311 | 0.712 | 21112 | 0.814 | 22213 | 0.505 | 23321 | 0.389 | 32122 | 0.499 | 33223 | 0.204 |
| 11211 | 0.897 | 12312 | 0.651 | 21113 | 0.711 | 22221 | 0.560 | 23322 | 0.328 | 32123 | 0.395 | 33231 | 0.240 |
| 11212 | 0.836 | 12313 | 0.548 | 21121 | 0.766 | 22222 | 0.499 | 23323 | 0.225 | 32131 | 0.432 | 33232 | 0.180 |
| 11213 | 0.733 | 12321 | 0.602 | 21122 | 0.705 | 22223 | 0.396 | 23331 | 0.262 | 32132 | 0.371 | 33233 | 0.077 |
| 11221 | 0.787 | 12322 | 0.541 | 21123 | 0.602 | 22231 | 0.432 | 23332 | 0.201 | 32133 | 0.268 | 33311 | 0.395 |
| 11222 | 0.727 | 12323 | 0.438 | 21131 | 0.638 | 22232 | 0.372 | 23333 | 0.098 | 32211 | 0.565 | 33312 | 0.334 |
| 11223 | 0.623 | 12331 | 0.475 | 21132 | 0.578 | 22233 | 0.269 | 31111 | 0.771 | 32212 | 0.505 | 33313 | 0.231 |
| 11231 | 0.660 | 12332 | 0.414 | 21133 | 0.475 | 22311 | 0.587 | 31112 | 0.711 | 32213 | 0.402 | 33321 | 0.285 |
| 11232 | 0.599 | 12333 | 0.311 | 21211 | 0.772 | 22312 | 0.526 | 31113 | 0.608 | 32221 | 0.456 | 33322 | 0.225 |
| 11233 | 0.496 | 13111 | 0.809 | 21212 | 0.711 | 22313 | 0.423 | 31121 | 0.662 | 32222 | 0.395 | 33323 | 0.121 |
| 11311 | 0.814 | 13112 | 0.748 | 21213 | 0.608 | 22321 | 0.477 | 31122 | 0.601 | 32223 | 0.292 | 33331 | 0.158 |
| 11312 | 0.754 | 13113 | 0.645 | 21221 | 0.662 | 22322 | 0.416 | 31123 | 0.498 | 32231 | 0.329 | 33332 | 0.097 |
| 11313 | 0.650 | 13121 | 0.700 | 21222 | 0.602 | 22323 | 0.313 | 31131 | 0.535 | 32232 | 0.268 | 33333 | −0.006 |
| 11321 | 0.705 | 13122 | 0.639 | 21223 | 0.498 | 22331 | 0.350 | 31132 | 0.474 | 32233 | 0.165 |  |  |
| 11322 | 0.644 | 13123 | 0.536 | 21231 | 0.535 | 22332 | 0.289 | 31133 | 0.371 | 32311 | 0.483 |  |  |
| 11323 | 0.541 | 13131 | 0.572 | 21232 | 0.474 | 22333 | 0.186 | 31211 | 0.668 | 32312 | 0.422 |  |  |
| 11331 | 0.577 | 13132 | 0.512 | 21233 | 0.371 | 23111 | 0.684 | 31212 | 0.607 | 32313 | 0.319 |  |  |
| 11332 | 0.517 | 13133 | 0.409 | 21311 | 0.689 | 23112 | 0.624 | 31213 | 0.504 | 32321 | 0.373 |  |  |
| 11333 | 0.414 | 13211 | 0.706 | 21312 | 0.629 | 23113 | 0.520 | 31221 | 0.558 | 32322 | 0.313 |  |  |
| 12111 | 0.897 | 13212 | 0.645 | 21313 | 0.525 | 23121 | 0.575 | 31222 | 0.498 | 32323 | 0.210 |  |  |
| 12112 | 0.837 | 13213 | 0.542 | 21321 | 0.580 | 23122 | 0.514 | 31223 | 0.395 | 32331 | 0.246 |  |  |
| 12113 | 0.734 | 13221 | 0.596 | 21322 | 0.519 | 23123 | 0.411 | 31231 | 0.431 | 32332 | 0.186 |  |  |
| 12121 | 0.788 | 13222 | 0.536 | 21323 | 0.416 | 23131 | 0.447 | 31232 | 0.371 | 32333 | 0.082 |  |  |
| 12122 | 0.727 | 13223 | 0.432 | 21331 | 0.453 | 23132 | 0.387 | 31233 | 0.267 | 33111 | 0.580 |  |  |
| 12123 | 0.624 | 13231 | 0.469 | 21332 | 0.392 | 23133 | 0.284 | 31311 | 0.586 | 33112 | 0.520 |  |  |
| 12131 | 0.661 | 13232 | 0.408 | 21333 | 0.289 | 23211 | 0.581 | 31312 | 0.525 | 33113 | 0.417 |  |  |
| 12132 | 0.600 | 13233 | 0.305 | 22111 | 0.772 | 23212 | 0.520 | 31313 | 0.422 | 33121 | 0.471 |  |  |
| 12133 | 0.497 | 13311 | 0.623 | 22112 | 0.712 | 23213 | 0.417 | 31321 | 0.476 | 33122 | 0.410 |  |  |
| 12211 | 0.794 | 13312 | 0.563 | 22113 | 0.609 | 23221 | 0.471 | 31322 | 0.415 | 33123 | 0.307 |  |  |

</div>

## Discussion

### Main Findings

According to the International Valuation Protocol, this valuation study generated an EQ-5D-Y-3L value set for Brazil \[30\]. We collected the DCE tasks to generate the latent scale values and 28 cTTO health states to anchor the utilities (i.e., five health states more than the 23 recommended in the Indonesian valuation study) \[30\]. We investigated four different mapping approaches to estimate the Brazilian EQ-5D-Y-3L value set. The linear mapping without intercept was chosen as the preferred approach for rescaling predicted DCE values, resulting in a final model for the value set. The respondents assigned highest weights dimensions related to having pain or discomfort, followed by walking about (mobility), looking after myself, doing usual activities, and feeling worried, sad, or unhappy.

### Comparison with other EQ-5D-Y-3L value set studies

Although the International Valuation Protocol did not recommend a specific modeling technique for estimating DCE values from the responses, the mixed-logit model has been the most employed method among the valuation studies for the EQ-5D-Y-3L \[35–37, 39, 40\]. Our findings are aligned with such studies as the mixed-logit model outperformed the conditional model when predicting DCE values on a latent scale. The International Valuation Protocol also did not recommend a specific modeling technique for mapping DCE values into cTTO \[30\]. Similar to analyses conducted in the Indonesian EQ-5D-Y-3L valuation study \[36\], we used four different mapping approaches to evaluate the relationship between DCE and cTTO data and selected the one that presented a better overall fit<sup>33</sup>. The main differences between our study and the Indonesian value set were that we had 28 health states for the cTTO and the best mapping approach was linear; whereas the Indonesia study considered 23 health states and the best mapping approach was non-linear \[36\]. The valuation study in Hungary (ten health states) and the Netherlands (28 health states) explored two and three mapping approaches, respectively. In both studies, the ordinary least squares regression without constant was chosen as the preferred mapping model \[37, 38\]. The valuation study in China and Spain adopted a hybrid model that combined DCE and cTTO data jointly \[42, 43\]. Overall, these methodological choices (e.g., mapping approaches) highlight the complexity of eliciting preferences, particularly in health valuation research in pediatric populations and country-specific contexts. Further research is needed to evaluate the magnitude and impact of such methodological choices on eliciting preferences and decision-making to provide clear guidance on this matter.

We found a discrepancy between the predicted value for the worst health state (33333) of − 0.006 and the mean observed value of − 0.28. The value for the worst health state (33333) could not be predicted well from the values assigned to other health states; however, this may not be very problematic because this health state is rare in child and adolescent patient populations. As mild and moderate health states are more prevalent in this population, it would possibly be more relevant to predict those health states more accurately than the severe ones. On the other hand, despite being rare, severe health states usually are those that also drive high costs (i.e., children and adolescents with cancer). Thus, it is relevant to validity predict preferences for those severe health states, and users should be aware of this limitation when using the Brazilian EQ-5D-Y-3L. In the Indonesia valuation study, the authors presented a similar issue. The preferred model was the non-linear one (without intercept), demonstrating lower misprediction for the milder health states \[36\]. The findings suggested that anchoring the worst health state (33333) may generate lower minimum values than other anchoring approaches (i.e., hybrid model). This highlights the importance of (1) considering different anchoring approaches in the valuation studies and (2) understanding if this reflects the non-linearity in the preferred model or if this is regarding the choice of methods \[29\].

In the EQ-5D-3L Brazilian value set, the worst health state (33333) was valued as − 0.176, which is lower than the lowest value of the EQ-5D-Y-3L \[45\]. This difference may be explained by the descriptive systems and the valuation methods used in both studies. Our results were similar to those observed in other previous valuation studies \[35, 36, 39, 43\], highlighting the differences in the importance of dimensions between the adult and child EQ-5D-3L versions. For instance, pain/discomfort (having pain or discomfort) was the highest weighted dimension in the child valuation whereas mobility, in the adult. There are several challenges regarding the differences of using the QALY in HTA for children and adolescents when compared to adults. While we acknowledge the importance of considering age-specific QALY values and the issues associated with their incorporation into models spanning the lifetime, it is essential to remember that recommendations are not solely based on cost-effectiveness analyses \[29\]. Other factors such as available resources, characteristics and impact of the condition, equity, and context are also taken into account, especially for the population of children and adolescents \[29, 60\]. Valuation studies with the EQ-5D-Y-3L are still being developed around the world and new methodologies with different versions (i.e., age-dependent valuation) can be considered such as the proxy version for younger children (\< 8 years), the EQ-5D-Y-5L version, and/or the experimental Toddler and Infant Populations version (EQ-TIPs) \[29\]. Furthermore, new methods for conducting valuation studies with the EQ-5D instrument in children and adolescents should be considered, as this is also the case with other similar instruments (i.e., CHU9D). In this scenario, the adolescents (rather than adults) would elicit their preferences, taking into account their own perspectives and this could potentially minimize the likelihood of having the QALYs for different age groups \[29, 61\]. Thus, caution is needed for stakeholders, decisions-makers and researchers on how to interpret and use, in practice, the results descendent from the current literature.

### Strengths and Limitations

This study has some strengths. Firstly, all the cTTO interviews were conducted by experienced healthcare professionals who work with research. Furthermore, only two out of 211 interviews were flagged as poor quality (less than 1%), which guaranteed a quality control process during the cTTO data collection. Secondly, we also included quotas for age, sex, educational level, and socioeconomic level for both the DCE and cTTO surveys to guarantee the representativeness of the Brazilian population in our sample. Finally, the online DCE survey included respondents from all Brazilian regions (south: 14%; southeast: 42%; north: 9%; northeast: 27%; and central west: 8%), which aligns with the latest population estimate according to the Brazilian Institute of Geography and Statistics' Demographic Census of 2022 \[62\]. Thus, our findings support a good geographic representation of the Brazilian population, which can be considered a great challenge as Brazil is a country with continental dimensions \[63\].

This study also has some limitations. Despite the good representativeness of the DCE data, attention is needed to possible levels of low engagement and random responses in the online DCE survey. Our findings demonstrated that 58% (1638 of 2790) of respondents were excluded from the DCE task due to not completing all tasks. Of those 1638 excluded, 1365 (83%) did not completed all DCE tasks and 273 (17%) completed the tasks in less than 150 s or failed in the logically dominant pairs according to our quality criteria. Furthermore, although internet access in Brazil has increased in recent years, the DCE sample may present a selection bias due to the low levels of income, education, and digital literacy of a proportion of the Brazilian population \[63, 64\]. Even though we have also cautiously selected quotas for the DCE and cTTO to guarantee representativeness, and cTTO was considered for three Brazilian states representing about 31.6% of the whole Brazilian population. Thus, apart from guarantying feasibility of the study, it is complex to geographically fully represent a country like Brazil considering the five regions in the cTTO as the territorial extension of Brazil is 8,510,418 km<sup>2</sup> according to the Brazilian Institute of Geography and Statistics \[63\]. Another limitation is that DCE and cTTO were conducted in different samples and different modes of administration.

An important discussion has been raised around several key points regarding conducting the cTTO method in adults when eliciting preference for an instrument designed for children and adolescents aged 8–15 years \[31\]. There is a debate regarding the appropriateness of framing the task as “considering your views about a 10-year-old child” as it may introduce a potential bias or limitations when adults are asked to imagine the children and adolescents’ perspective. It has been discussed that there are important differences between the preferences of health for a child of 10-year-old compared with an adolescent of 17 years old \[65\]. Secondly, alternative perspectives, such as imagining one’s child, a known child, or simply imagining another child remain unknown as it could alter values and potentially influence preferences \[66\]. Lastly, there is an ongoing discussion on the feasibility of including adolescents in the valuation tasks in the EQ-5D-Y-3L and as previous studies for the CHU9D for example \[33, 67–69\]. These discussions aim to enhance the validity and reliability of preference elicitation for child and adolescent-specific instruments.

### Future Studies and Implications for Practice

This study opens possibilities for future studies, such as randomized controlled trials, observational studies (i.e., cross-sectional and cohort), and methodological studies (psychometric studies) to measure HRQoL in children and adolescents using the EQ-5D-Y-3L value set in Brazil. As with the EQ-5D-3L and EQ-5D-5L, future research should be conducted with the EQ-5D-Y-3L to validate it in youth populations with specific health conditions (e.g., obesity, asthma, cancer, musculoskeletal, and mental conditions) in Brazil. Our findings raise the opportunity for researchers to use the Brazilian EQ-5D-Y-3L value set to estimate the QALYs to conduct economic evaluations (i.e., cost-utility analysis) for incorporation of health technologies assessment in the youth population in Brazil. The EQ-5D-Y-3L value set can be used in clinical studies, psychometric studies, and population-based studies as well as by researchers, clinicians, and policy/decision makers interested in valuing health-related quality of life using utilities \[70\]. We provide the descriptions and syntaxes for estimating utilities using R, STATA, SPSS, and Microsoft Excel in the Supplementary Information <a href="#MOESM2" data-ref-type="supplementary-material">2</a>. The use of the Brazilian EQ-5D-Y-3L value set should be recommended in the updated version of the Brazilian Health Technology Assessment guideline \[16\]. Thus, in the same way that the EQ-5D-3L has been used as a preferred decision-making instrument for the incorporation of new health technologies assessment in Brazil \[16\], we believe the EQ-5D-Y-3L value set can be widely used in the decision-making process for the Brazilian population of children and adolescents.

## Conclusion

To conclude, this study provided a national value set of the EQ-5D-Y-3L for Brazilian children and adolescents based on adult population preference considering the viewpoint of a 10-year-old child. The utilities ranged from 1 for “full health” to –0.0059 for “the worst health state.” The dimension with the largest weight was having pain or discomfort followed by walking about (mobility). The elicited Brazilian EQ-5D-Y-3L value set can be used to estimate the quality-adjusted life-years for economic evaluations of health technologies targeting the Brazilian youth population.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 21 KB)

</div>

<div class="caption">

Supplementary file2 (MOV 257826 KB)

</div>

<div class="caption">

Supplementary file3 (XLS 22 KB)

</div>

## Acknowledgments

Caique de Melo do Espirito Santo, Verônica Souza Santos, and Tiê Parma Yamato would like to thank Sao Paulo Research Foundation (FAPESP) for all financial grant support. Authors would like to thank Universidade Cidade de São Paulo, Universidade Federal do Ceará, and Universidade Federal de Ciências da Saúde de Porto Alegre for all resources and structure to conduct the interviews of this study. Authors would like to thank Julia Lima for all support as interviewer in the data collection of this study in Rio Grande do Sul.

## Declarations

### Funding

This study was funded by the EuroQol Research Foundation (220-VS). Caique de Melo do Espirito Santo was granted PhD scholarship from the Sao Paulo Research Foundation (FAPESP)—process number 2021/08776-4; Verônica Souza Santos was granted a PhD scholarship from the Sao Paulo Research Foundation (FAPESP)—process number 2019/12049-0; and Tiê Parma Yamato received a research grant from the Sao Paulo Research Foundation (FAPESP)—process number 2017/17484-1. The funding agencies (the EuroQol Research Foundation and the Sao Paulo Research Foundation—FAPESP) of this study had no influence on the design of the study and collection, analysis, and interpretation of data and writing of the manuscript.

### Competing Interests

Aureliano Paolo Finch and Bram Roudijk are both employed by the EuroQol Research Foundation, and Marisa Santos is a member of the EuroQol Group. The views expressed in this article are those of the authors and do not necessarily reflect those of the EuroQol Research Foundation. Caique de Melo do Espirito Santo, Gisela Cristiane Miyamoto, Verônica Souza Santos, Ângela Jornada Ben, Fabianna Resende de Jesus-Moraleida, Airton Tetelbom Stein, and Tiê Parma Yamato have no conflicts of interest to declare.

### Data Availability Statements

All data included in this study are freely available upon request to the study authors or can be obtained from the EuroQol office. The descriptions and syntaxes for estimating utilities using R, STATA, SPSS, and Microsoft Excel are available in the supplementary material. Additionally, the calculator for estimating utilities is also free available at: <https://1drv.ms/f/s!AlXe7Z7nw0ZUrH007EKk4YQMvoeS?e=NWGmEZ>.

### Ethics Approval

This study was approved by the Human Ethics Committee of the Universidade Cidade de São Paulo (CAAE: 45241321.6.0000.0064) and we certify that the study was performed in accordance with the ethical standards as laid down in the 1964 Declaration of Helsinki.

### Consent to Participate

Informed consent was obtained from all participants included in the study.

### Authors’ Contributions

C.M.E.S., G.C.M., V.S.S., M.S., A.P.F., F.R.J.M., A.T.S., and T.P.Y. developed the study design. C.M.E.S., G.C.M., V.S.S., F.R.J.M., and A.T.S. collected data. G.C.M., A.J.B., A.P.F., B.R., and T.P.Y. analyzed and interpreted data for the work. C.M.E.S., G.C.M., V.S.S., A.J.B., A.P.F., B.R., F.R.J.M., A.T.S., M.S., and T.P.Y. drafted and reviewed the content of the work. All authors read and approved the final version of the manuscript to be published.

## References

## References

1. Chen G, Ratcliffe J. A Review of the development and application of generic multi-attribute utility instruments for paediatric populations. Pharmacoeconomics. 2015;33:1013–28. 10.1007/s40273-015-0286-7

2. Ravens-Sieberer U, Erhart M, Wille N, Wetzel R, Nickel J, Bullinger M. Generic health-related quality-of-life assessment in children and adolescents: methodological considerations. Pharmacoeconomics. 2006;24:1199–220. 10.2165/00019053-200624120-00005

3. Beusterien KM, Yeung JE, Pang F, Brazier J. Development of the multi-attribute Adolescent Health Utility Measure (AHUM). Health Qual Life Outcomes. 2012;10:1–9. 10.1186/1477-7525-10-102

4. Richardson J, Day NA, Peacock S, Iezzi A. Measurement of the quality of life for economic evaluation and the assessment of quality of life (AQoL) mark 2 instrument. Aust Econ Rev. 2004;37:62–88. 10.1111/j.1467-8462.2004.00308.x

5. Stevens K. Developing a descriptive system for a new preference-based measure of health-related quality of life for children. Qual Life Res. 2009;18:1105–13. 10.1007/s11136-009-9524-9

6. Wille N, Badia X, Bonsel G, Burström K, Cavrini G, Devlin N, et al. Development of the EQ-5D-Y: a child-friendly version of the EQ-5D. Qual Life Res. 2010;19:875–86. 10.1007/s11136-010-9648-y

7. Torrance GW, Furlong W, Feeny D, Boyle M. Multi-attribute preference functions. Pharmacoeconomics. 1995;7:503–20. 10.2165/00019053-199507060-00005

8. Feeny D, Furlong W, Torrance GW, Goldsmith CH, Zhu Z, DePauw S, et al. Multiattribute and single-attribute utility functions for the Health Utilities Index Mark 3 system. Med Care. 2002;40:113–28. 10.1097/00005650-200202000-00006

9. Ravens-Sieberer U, Wille N, Badia X, Bonsel G, Burström K, Cavrini G, et al. Feasibility, reliability, and validity of the EQ-5D-Y: Results from a multinational study. Qual Life Res. 2010;19:887–97. 10.1007/s11136-010-9649-x

10. Kreimeier S, Greiner W. EQ-5D-Y as a health-related quality of life instrument for children and adolescents: the instrument’s characteristics, development, current use, and challenges of developing its value set. Value in Health. 2019;22:31–7. 10.1016/j.jval.2018.11.001

11. Devlin NJ, Brooks R. EQ-5D and the EuroQol Group: past, present and future. Appl Health Econ Health Policy. 2017;15:127–37. 10.1007/s40258-017-0310-5

12. Rowen D, Keetharuth AD, Poku E, Wong R, Pennington B, Wailoo A. A review of the psychometric performance of selected child and adolescent preference-based measures used to produce utilities for child and adolescent health. Value Health Internet. 2021;24:443–60. 10.1016/j.jval.2020.09.012. 10.1016/j.jval.2020.09.012

13. Ministério da Saúde. DIRETRIZES METODOLÓGICAS: Diretriz de Avaliação Econômica [Internet]. Brasília; 2014. Available from: https://www.gov.br/conitec/pt-br/assuntos/avaliacao-de-tecnologias-em-saude/diretrizes-metodologicas.

14. Miyamoto GC, Ben ÂJ, Bosmans JE, van Tulder MW, Lin CWC, Cabral CMN, et al. Interpretation of trial-based economic evaluations of musculoskeletal physical therapy interventions. Braz J Phys Ther. 2021;25:514–29. 10.1016/j.bjpt.2021.06.011

15. Ministério da Saúde. O USO DE LIMIARES DE CUSTO-EFETIVIDADE NAS DECISÕES EM SAÚDE: Recomendações da Comissão Nacional de Incorporação de Tecnologias no SUS [Internet]. Brasília; 2022. Available from: http://conitec.gov.br/

16. Santos M, Monteiro AL, Biz AN, Guerra A, Cramer H, Canuto V, et al. Guidelines for utility measurement for economic analysis: the Brazilian policy. Value Health Reg Issues [Internet]. 2022;31:67–73. 10.1016/j.vhri.2022.03.004. 10.1016/j.vhri.2022.03.004

17. Senado Federal. Projeto de Lei do Senado n° 415, de 2015 [Internet]. 2021 [cited 2023 Jun 29]. Available from: https://www25.senado.leg.br/web/atividade/materias/-/materia/122071.

18. Comissão Nacional de Incorporação de Tecnologias no Sistema Único de Saúde. Conitec em números [Internet]. 2020 [cited 2024 Apr 21]. Available from: https://lookerstudio.google.com/embed/reporting/ed1f017c-58e0-4177-aeb2-61f59d50b183/page/PzCbB.

19. Salary Converter [Internet]. [cited 2024 May 9]. Available from: http://salaryconverter.nigelb.me/.

20. Karimi M, Brazier J. Health, health-related quality of life, and quality of life: what is the difference? Pharmacoeconomics. 2016;34:645–9. 10.1007/s40273-016-0389-9

21. Whitehead SJ, Ali S. Health outcomes in economic evaluation: the QALY and utilities. Br Med Bull. 2010;96:5–21. 10.1093/bmb/ldq033

22. Gray AM, Clarke PM, Wolstenholme JL, Wordsworth S. Applied methods of cost-effectiveness analysis in health care. 1st ed. New York: Oxford University Press; 2010.

23. Drummond MF, Sculpher MJ, Torrance GW, O’Brien BJ, Stoddart GL. Methods for the economic evaluation of health care programmes. 3rd ed. New York: Oxford University Press; 2005.

24. Wu XY, Ohinmaa A, Johnson JA, Veugelers PJ. Assessment of children’s own health status using visual analogue scale and descriptive system of the EQ-5D-Y: Linkage between two systems. Qual Life Res. 2014;23:393–402. 10.1007/s11136-013-0479-5

25. Mott DJ, Shah KK, Ramos-Goñi JM, Devlin NJ, Rivero-Arias O. Valuing EQ-5D-Y-3L qual life res? Med Decis Making. 2021;41:584–96. 10.1177/0272989X21999607

26. Shah KK, Ramos-Goñi JM, Kreimeier S, Devlin NJ. An exploration of methods for obtaining 0 = dead anchors for latent scale EQ-5D-Y values. Eur J Health Econ [Internet]. 2020;21:1091–103. 10.1007/s10198-020-01205-9. 10.1007/s10198-020-01205-9

27. Ratcliffe J, Couzner L, Flynn T, Sawyer M, Stevens K, Brazier J, et al. Valuing Child health utility 9D health states with a young adolescent sample. Appl Health Econ Health Policy [Internet]. 2011;9:15–27. Available from: https://link.springer.com/content/pdf/10.2165%2F11536960-000000000-00000.pdf. doi:10.2165/11536960-000000000-00000

28. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goñi JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation work: version 2 of the EQ-5D-5L valuation protocol. Value Health. 2019;22:23–30. 10.1016/j.jval.2018.05.010

29. Devlin N, Roudijk B, Viney R, Stolk E. EQ-5D-Y-3L Value sets, valuation methods and conceptual questions. Pharmacoeconomics. 2022;40:123–7. 10.1007/s40273-022-01226-7

30. Ramos-Goñi JM, Oppe M, Stolk E, Shah K, Kreimeier S, Rivero-Arias O, et al. International valuation protocol for the EQ-5D-Y-3L. Pharmacoeconomics [Internet]. 2020;38:653–63. 10.1007/s40273-020-00909-3. 10.1007/s40273-020-00909-3

31. Ungar WJ. Challenges in health state valuation in paediatric economic evaluation: Are QALYs contraindicated? Pharmacoeconomics. 2011;29:641–52. 10.2165/11591570-000000000-00000

32. Kind P, Klose K, Gusi N, Olivares PR, Greiner W. Can adult weights be used to value child health states? Testing the influence of perspective in valuing EQ-5D-Y. Qual Life Res [Internet]. 2015;24:2519–39. 10.1007/s11136-015-0971-1. 10.1007/s11136-015-0971-1

33. Ratcliffe J, Huynh E, Stevens K, Brazier J, Sawyer M, Flynn T. Nothing about us without us? A comparison of adolescent and adult health-state values for the child health utility-9D using profile case best-worst scaling. Health Econ. 2016;25:486–96. 10.1002/hec.3165

34. Mott DJ, Ramos-goñi JM, Devlin NJ, Rivero-arias O, Mott DJ, Devlin NJ. Do adult and adolescent preferences differ? Office of Health Economics Research Paper [Internet]. 2019 [cited 2022 May 22]; https://www.ohe.org/publications/valuing-eq-5d-yhealth-states-using-discrete-choice-experiment-do-adult-and-adolescent.

35. Shiroiwa T, Ikeda S, Noto S, Fukuda T, Stolk E. Valuation survey of EQ-5D-Y based on the international common protocol: development of a value set in Japan. Med Decis Making. 2021;3:1–10. doi:10.1177/0272989X211001859

36. Fitriana TS, Roudijk B, Purba FD, Busschbach JJV, Stolk E. Estimating an EQ-5D-Y-3L value set for Indonesia by mapping the DCE onto TTO values. Pharmacoeconomics [Internet]. 2022;40:157–67. 10.1007/s40273-022-01210-1. 10.1007/s40273-022-01210-1

37. Rencz F, Ruzsa G, Bató A, Yang Z, Finch AP, Brodszky V. Value Set for the EQ-5D-Y-3L in Hungary. Pharmacoeconomics [Internet]. 2022;40:205–15. 10.1007/s40273-022-01190-2. 10.1007/s40273-022-01190-2

38. Roudijk B, Sajjad A, Essers B, Lipman S, Stalmeier P, Finch AP. A value set for the EQ-5D-Y-3L in the Netherlands. Pharmacoeconomics [Internet]. 2022;40:193–203. 10.1007/s40273-022-01192-0. 10.1007/s40273-022-01192-0

39. Prevolnik Rupel V, Ogorevc M, Greiner W, Kreimeier S, Ludwig K, Ramos-Goni JM. EQ-5D-Y value set for Slovenia. Pharmacoeconomics. 2021;39:463–71. 10.1007/s40273-020-00994-4

40. Kreimeier S, Mott D, Ludwig K, Greiner W, Prevolnik Rupel V, Ramos-Goñi JM. EQ-5D-Y value set for Germany. Pharmacoeconomics. 2022;40:217–29. 10.1007/s40273-022-01143-9

41. Dewilde S, Roudijk B, Tollenaar NH, Ramos-Goñi JM. An EQ-5D-Y-3L value set for Belgium. Pharmacoeconomics [Internet]. 2022;40:169–80. 10.1007/s40273-022-01187-x. 10.1007/s40273-022-01187-x

42. Ramos-Goñi JM, Oppe M, Estévez-Carrillo A, Rivero-Arias O, Wolfgang G, Simone K, et al. Accounting for unobservable preference heterogeneity and evaluating alternative anchoring approaches to estimate country-specific EQ-5D-Y value sets: a case study using Spanish preference data. Value Health. 2022;25:835–43. 10.1016/j.jval.2021.10.013

43. Yang Z, Jiang J, Wang P, Jin X, Wu J, Fang Y, et al. Estimating an EQ-5D-Y-3L value set for China. Pharmacoeconomics [Internet]. 2022;40:147–55. 10.1007/s40273-022-01216-9. 10.1007/s40273-022-01216-9

44. Santos M, Cintra MACT, Monteiro AL, Santos B, Gusmão-Filho F, Andrade MV, et al. Brazilian valuation of EQ-5D-3L health states. Med Decis Making. 2016;36:253–63. 10.1177/0272989X15613521

45. Santos M, Cintra MACT, Monteiro AL, Santos B, Gusmão-Filho F, Andrade M V, et al. Brazilian valuation of EQ-5D-3L health states: results from a saturation study. Med Decis Making [Internet]. 2015;117–28. Available from: http://www.ncbi.nlm.nih.gov/pubmed/26492896. doi:10.1177/0272989X15613521

46. Xie F, Gaebel K, Perampaladas K, Doble B, Pullenayegum E. Comparing EQ-5D valuation studies: A systematic review and methodological reporting checklist. Med Decis Making. 2014;34:8–20. 10.1177/0272989X13480852

47. Webb EJD, Kind P, Meads D, Martin A. Does a health crisis change how we value health? Health Econ (United Kingdom). 2021;30:2547–60. 10.1002/hec.4399

48. Jonker MF, Donkers B, de Bekker-Grob EW, Stolk EA. Effect of level overlap and color coding on attribute non-attendance in discrete choice experiments. Value Health [Internet]. 2018;21:767–71. 10.1016/j.jval.2017.10.002. 10.1016/j.jval.2017.10.002

49. Yang Z, Luo N, Bonsel G, Busschbach J, Stolk E. Selecting health states for EQ-5D-3L valuation studies: statistical considerations matter. Value Health [Internet]. 2018;21:456–61. 10.1016/j.jval.2017.09.001. 10.1016/j.jval.2017.09.001

50. Yang Z, Luo N, van Busschbach J, Stolk E. Using orthogonal design in selecting health states for the construction of EQ-5D-3L Value Set. Value Health. 2016; p. A386.

51. Ramos-Goñi JM, Oppe M, Slaap B, Busschbach JJV, Stolk E. Quality control process for EQ-5D-5L valuation studies. Value Health [Internet]. 2017;20:466–73. 10.1016/j.jval.2016.10.012. 10.1016/j.jval.2016.10.012

52. (IBGE) IB de G e E. Censo demográfico [Internet]. 2021 [cited 2021 Feb 23]. Available from: https://www.ibge.gov.br/estatisticas/sociais/populacao.html

53. Perillo SR, de Perdigão ML. Percursos migratórios no Estado de São Paulo: uma análise do período 1995–2000. São Paulo em Perspectiva. 2005;19:97–109. 10.1590/S0102-88392005000300009

54. Associação Brasileira de Empresas de Pesquisa. Critério de Classificação Econômica Brasil (CCEB) [Internet]. 2019 [cited 2021 Sep 3]. Available from: https://www.abep.org/

55. McFadden D, Train K. Mixed MNL models for discrete response. J Appli Economet. 2000;15:447–70. 10.1002/1099-1255(200009/10)15:5<447::AID-JAE570>3.0.CO;2-1

56. Schawarz G. Estimating the dimension of a model. Ann Stat Internet. 1978;6:461–4. 10.1214/aos/1176344136.full. 10.1214/aos/1176344136.full

57. Rowen D, Brazier J, Van Hout B. A comparison of methods for converting DCE values onto the full health-dead QALY scale. Med Decis Making. 2015;35:328–40. 10.1177/0272989X14559542

58. Mott DJ, Devlin NJ, Kreimeier S, Norman R, Shah KK, Rivero-Arias O. Analytical considerations when anchoring discrete choice experiment values using composite time trade-off data: the case of EQ-5D-Y-3L. Pharmacoeconomics [Internet]. 2022;40:129–37. 10.1007/s40273-022-01214-x. 10.1007/s40273-022-01214-x

59. Devlin N, Parkin D, Janssen B. Methods for analysing and reporting EQ-5D data Internet. Springer Cham; 2020 [cited 2024 May 12]. 10.1007/978-3-030-47622-9.

60. Sinha IP, Altman DG, Beresford MW, Boers M, Clarke M, Craig J, et al. Standard 5: selection, measurement, and reporting of outcomes in clinical trials in children. Pediatrics [Internet]. 2012 [cited 2024 May 12];129:S146–56. Available from: https://publications.aap.org/pediatrics/article-abstract/129/Supplement_3/S146/32258/Standard-5-Selection-Measurement-and-Reporting-of?redirectedFrom=fulltext. doi:10.1542/peds.2012-0055H

61. Stevens K. Valuation of the child health utility 9D index. Pharmacoeconomics. 2012;30:729–47. 10.2165/11599120-000000000-00000

62. Instituto Brasileiro de Geografia e Estatística (IBGE). Prévia da população calculada com base nos resultados do Censo Demográfico 2022 até 25 de dezembro de 2022. Instituto Brasileiro de Geografia e Estatística. Brasília; 2022.

63. Instituto Brasileiro de Geografia e Estatística. Instituto Brasileiro de Geografia e Estatística (IBGE) [Internet]. 2022 [cited 2023 Jul 19]. https://www.ibge.gov.br/.

64. Manganello J, Gerstner G, Pergolino K, Graham Y, Falisi A, Strogatz D. The relationship of health literacy with use of digital technology for health information: Implications for public health practice. J Public Health Manag Pract. 2017;23:380–7. 10.1097/PHH.0000000000000366

65. Lipman SA, Reckers-Droog VT, Kreimeier S. Think of the children: a discussion of the rationale for and implications of the perspective used for EQ-5D-Y health state valuation. Value Health [Internet]. 2021;24:976–82. 10.1016/j.jval.2021.01.011. 10.1016/j.jval.2021.01.011

66. Lipman SA, Essers BAB, Finch AP, Sajjad A, Stalmeier PFM, Roudijk B. In a child’s shoes: composite time trade-off valuations for EQ-5D-Y-3L with different proxy perspectives. Pharmacoeconomics [Internet]. 2022;40:181–92. 10.1007/s40273-022-01202-1. 10.1007/s40273-022-01202-1

67. Åström M, Conte H, Berg J, Burström K. ‘Like holding the axe on who should live or not’: adolescents’ and adults’ perceptions of valuing children’s health states using a standardised valuation protocol for the EQ-5D-Y-3L. Qual Life Res Internet. 2022;31:2133–42. 10.1007/s11136-022-03107-0. 10.1007/s11136-022-03107-0

68. Åström M, Rolfson O, Burström K. Exploring EQ-5D-Y-3L Experience-based VAS values derived among adolescents. Appl Health Econ Health Policy [Internet]. 2022;20:383–93. 10.1007/s40258-021-00713-w. 10.1007/s40258-021-00713-w

69. Dalziel K, Catchpool M, García-Lorenzo B, Gorostiza I, Norman R, Rivero-Arias O. Feasibility, validity and differences in adolescent and adult EQ-5D-Y health state valuation in Australia and Spain: an application of best–worst scaling. Pharmacoeconomics [Internet]. 2020;38:499–513. 10.1007/s40273-020-00884-9. 10.1007/s40273-020-00884-9

70. Gnanasakthy A, DeMuro CR. The limitations of EQ-5D as a clinical outcome assessment tool. Patient. 2024;17:215–7. 10.1007/s40271-024-00683-w

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary file1 (DOCX 21 KB)

</div>

<div class="caption">

Supplementary file2 (MOV 257826 KB)

</div>

<div class="caption">

Supplementary file3 (XLS 22 KB)

</div>

### Data Availability Statement

All data included in this study are freely available upon request to the study authors or can be obtained from the EuroQol office. The descriptions and syntaxes for estimating utilities using R, STATA, SPSS, and Microsoft Excel are available in the supplementary material. Additionally, the calculator for estimating utilities is also free available at: <https://1drv.ms/f/s!AlXe7Z7nw0ZUrH007EKk4YQMvoeS?e=NWGmEZ>.

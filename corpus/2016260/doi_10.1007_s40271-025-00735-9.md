---
project_id: "2016260"
work_id: "doi:10.1007/s40271-025-00735-9"
doi: "10.1007/s40271-025-00735-9"
pmid: "40088394"
pmcid: "PMC12170736"
title: "How do Design Characteristics Affect Respondent Engagement? Assessing Attribute Non-attendance in Discrete Choice Experiments Valuing the EQ-5D-5L"
journal: "The Patient"
publication_date: "2025-03-15"
volume: "18"
issue: "4"
authors:
  - name: "Peiwen Jiang"
    orcid: "http://orcid.org/0009-0000-4173-3487"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Deborah Street"
    orcid: "http://orcid.org/0000-0002-4476-0656"
    affiliation_ids:
      - "Aff1"
  - name: "Richard Norman"
    orcid: "http://orcid.org/0000-0002-8210-9936"
    affiliation_ids:
      - "Aff3"
  - name: "Rosalie Viney"
    orcid: "http://orcid.org/0000-0002-0039-9635"
    affiliation_ids:
      - "Aff1"
  - name: "Mark Oppe"
    orcid: "http://orcid.org/0000-0003-4286-8855"
    affiliation_ids:
      - "Aff4"
  - name: "Brendan Mulhern"
    orcid: "http://orcid.org/0000-0003-3656-8063"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/03f0f6041grid.117476.20000 0004 1936 7611Faculty of Health, Centre for Health Economics Research and Evaluation, University of Technology Sydney, Broadway, PO Box 123, Sydney, NSW 2007 Australia"
  - id: "Aff2"
    name: "https://ror.org/05j37e495grid.410692.80000 0001 2105 7653Population Health Research & Epidemiology, South Western Sydney Local Health District, Sydney, NSW Australia"
  - id: "Aff3"
    name: "https://ror.org/02n415q13grid.1032.00000 0004 0375 4078School of Population Health, Curtin University, Perth, WA Australia"
  - id: "Aff4"
    name: "https://ror.org/018906e22grid.5645.20000 0004 0459 992XSection Medical Psychology and Psychotherapy, Department of Psychiatry, Erasmus MC, Erasmus University, Rotterdam, The Netherlands"
licence: "cc-by"
source_file: "input/projects/2016260/papers/doi_10.1007_s40271-025-00735-9.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12170736/fullTextXML"
source_method: "epmc_xml"
source_sha256: "627e3aa895a17583b844b0fcab39ad9b7d4d37a905f5d1e020708e78569c1b65"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# How do Design Characteristics Affect Respondent Engagement? Assessing Attribute Non-attendance in Discrete Choice Experiments Valuing the EQ-5D-5L

## Abstract

### Introduction

Discrete choice experiments (DCEs) are increasingly applied to develop value sets for health-related quality-of-life instruments, but respondents may adopt various simplifying heuristics that affect the resulting health state values. Attribute level overlap can make these DCE tasks easier and thereby increase respondent engagement. This study uses choice tasks involving EQ-5D-5L health states to compare designs with and without overlap, constructed using different methods (generator-developed design, Ngene, SAS, and Bayesian D-efficient design) to assess respondent non-attendance to attributes.

### Methods

A multi-arm DCE using the EQ-5D-5L was conducted in the Australian general population. The performance of designs with various properties was compared using the level of respondent engagement. Respondent engagement was quantified through the inferred attribute non-attendance (ANA) estimated by the equality constrained latent class model. Utility decrements derived using all respondents (i.e., including non-attendees) were compared with estimates obtained only from those who attended to all EQ-5D-5L attributes.

### Results

The inclusion of overlap improved full attendance rates from 22.3–28.4% to 28.2–54.2%. Within designs with overlap, modified Fedorov designs (constructed using either Ngene or SAS macros) had higher full attendance rates than other designs. The relative attribute importance of the EQ-5D-5L also differed significantly before and after data exclusion using ANA analysis, but there was no clear pattern in the differences.

### Conclusions

This study found evidence to support the use of modified Fedorov designs (constructed using Ngene or SAS) with attribute overlap to reduce ANA and improve respondent engagement in DCE studies. It highlights the potential value of ANA analysis as a quality-control tool for the inclusion and exclusion of respondents in future health valuation work for the EQ-5D-5L.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s40271-025-00735-9.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| Modified Fedorov designs implemented in Ngene or SAS with attribute overlap are recommended to reduce attribute non-attendance (ANA) and enhance respondent engagement in discrete choice experiments (DCEs). |
| ANA models can be used to exclude respondents who did not attend to any attributes and to identify partial attenders for further robustness checks, improving the quality of the data for analysis. |
| Future research should focus on developing advanced models capable of disentangling the effects of preference heterogeneity and attribute attendance. |

</div>

## Introduction

Attribute non-attendance (ANA) is a phenomenon in discrete choice experiments (DCEs) whereby respondents consider only one or a few attributes presented in a choice task \[1\]. ANA can arise for two main reasons. First, it may reflect genuine preferences: some respondents may ignore certain attributes simply because they do not consider them relevant to their decision-making. In this case, ANA is an indication that those attributes are not important and do not meaningfully influence their choices. Second, ANA can occur as a decision heuristic, where respondents actively ignore attributes, not because they are unimportant but as a strategy to simplify complex tasks.

Heuristic-driven ANA is particularly likely to occur in highly complex choice tasks where respondents are required to consider multiple attributes presented at different levels at the same time. Design construction methods in DCEs are specifically developed to optimise the statistical efficiency of the experiment, aiming to maximise the information obtained from respondents’ choices while minimising the required sample size. However, there is a trade-off between behavioural efficiency and statistical efficiency.

Despite this need for balance, most studies evaluating DCE design methods have focused on statistical efficiency alone, with limited attention to the behavioural implications of different construction techniques \[2–4\]. The choice of construction method—such as orthogonal designs (which maintain attribute level independence) or efficient designs (which relax orthogonality constraints to optimise information yield)—can influence the rate of ANA \[1, 5\]. A study focusing on preferences of healthcare providers compared ANA between orthogonal and efficient designs using the equality constrained latent class (ECLC) model \[5\]. They found higher levels of ANA in efficient designs than in orthogonal designs and a more pronounced difference among illiterate respondents than among literate respondents. Another study on threatened species in New Zealand also adopted ECLC models to evaluate behavioural efficiency between orthogonal, generator-developed, and efficient designs \[6\]. Their results showed that the orthogonal design resulted in the lowest rate of full attendance and the D-efficient design achieved the highest level of full attendance. These contrasting findings suggest that construction methods may affect ANA differently.

In light of the increasing importance placed on respondent efficiency, attribute overlap has been recognised as a useful strategy to improve attribute attendance \[7, 8\]. Various design methods have included this feature in the construction of DCE designs \[9–11\]. Attribute overlap refers to the practice of setting a subset of attributes at the same level across options within the choice task. Jonker et al. \[8\] employed a Bayesian D-efficiency design to compare designs with no overlapping attributes and those with three of six attributes overlapped, using the EQ-5D-5L as the descriptive system. Their study showed that designs with attribute overlap significantly improved attribute attendance, increasing the number of attended attributes from two to three of a total of five.

Both studies comparing DCE construction methods—one focused on healthcare provider preferences and the other on threatened species—used designs without attribute overlap \[5, 6\]. Despite this similarity, their findings differed significantly, suggesting that construction method alone may not fully explain variations in ANA. Attribute overlap has been proposed as a potential way to enhance both respondent efficiency and attribute attendance, potentially playing a more influential role than construction method alone. This highlights the need to examine both construction method and attribute overlap together to understand their combined effects on respondent behaviour.

The growing interest in integrating attribute overlap in DCEs has led to its incorporation into various DCE construction algorithms, such as Ngene \[9\], SAS macros \[10\], and generator-developed designs \[11\]. It is surprising that no investigation has yet explored the ANA among designs featuring level overlap, particularly those constructed via differing methods. Furthermore, there remains a notable gap in the realm of preference measures, with limited exploration of design methodologies and structures, except for the studies by Jonker et al. \[8, 12\]. The current study aims to fill this knowledge gap and contribute to the literature by comprehensively comparing various design construction methods while considering the impact of attribute overlap in the domain of preference measures.

## Methods

### Choice Experiment

The descriptive system used in this study is the most widely used health-related quality-of-life instrument, the EQ-5D-5L. It contains five attributes—mobility, self-care, usual activities, pain/discomfort, and anxiety/depression—each presented at one of five levels (no problems, slight problems, moderate problems, severe problems, and extreme problems/ unable to). Health states are described by the quintuples of levels, with 11111 denoting the best health state possible and 55555 representing the worst health state possible. There were two hypothetical situations within each choice task, and respondents were asked to choose which they preferred, as shown in Fig. <a href="#Fig1" data-ref-type="fig">1</a>.

<figure id="Fig1">
<p><img src="40271_2025_735_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Context and typical choice set. Please consider, and imagine living with, one of the two health states described below. Then tell us which description you would prefer to experience.</figcaption>
</figure>

The study included a total of 19 designs constructed using six construction methods (Generator-developed design, modified Fedorov algorithm implemented in Ngene, modified Fedorov algorithm implemented in SAS, Bayesian D-efficient design, STATA, and modified coordinate–exchange algorithm implemented in Ngene), using zero and non-zero priors, and including attribute level overlap on two of the five attributes or on none (see Mulhern \[13\] for details). Each respondent was randomly allocated to one of the 19 designs, and a total of 21 choice sets were presented to these respondents. In this article, we focus on a subset of four construction methods capable of generating designs with attribute overlap and only on designs constructed using zero priors. We selected only these designs to ensure comparability because efficient designs can be affected significantly by misspecifications in the priors \[3\]. By exclusively considering designs with zero priors, we effectively eliminated bias and enhanced the validity of our comparisons.

The four construction methods included in this article are generator-developed design \[11\], Ngene \[9\], SAS macros \[10\], and Bayesian D-efficient design algorithm implemented in R by Oppe and van Hout \[14\] based on Rose et al. \[15\]. Each of these construction methods was used to generate one design with no overlap and another with two overlapping attributes out of five. This resulted in a total of eight designs, which are briefly outlined below.

The generator-developed design started with an initial set of profiles that form an orthogonal array for five attributes each with five levels, and a set of generators \[11\]. To obtain a 100% efficient design for zero priors for a design with no overlapping attributes, two generators are required. For each attribute, the two generators must between them have one entry that is 1 or 4 and one entry that is 2 or 3. In addition, our selection of generators was strategically aimed at minimising the number of dominant pairs within the design. Therefore, for the design with no overlapping attributes, the generators were (1,1,1,2,2) and (2,2,2,4,4). For the design with two overlapping attributes, we elected to again have two generators. To obtain attributes with equal levels in two of the attributes in the two options, a generator must have two elements that are equal to 0. We used the generators (1,1,1,0,0) and (0,0,2,1,1).

The modified Fedorov algorithm was used in both the Ngene software and the SAS macros to compare software implementations rather than to focus on different design algorithms. For designs with no overlap, the algorithm iteratively exchanges a profile in the design with one from all possible candidate profiles until no substantial improvement in the D-error value is observed. With regards to designs with overlap, a candidate set of choice sets consisting of all 40,000 pairs with two overlapping attributes was used in both Ngene and SAS. These choice sets then underwent iteration to identify the optimal design with overlap on two attributes.

The fourth construction method we included was the Bayesian D-efficient design algorithm implemented in R by Oppe and van Hout \[14\] based on Rose et al. \[15\]. Overlapping and non-overlapping designs were generated, subject to the constraints that no pair could be duplicated, choice sets could not include dominated options, and the designs needed to meet a specific requirement for level balance (see the electronic supplementary material \[ESM\]-A).

The survey consisted of several sections. It began with basic demographic questions (age, gender, and region) to ensure quota distribution, followed by survey details and consent. Participants then completed a self-reported EQ-5D-5L assessment before receiving instructions on the DCE tasks. This was followed by 21 DCE choice tasks. Finally, respondents answered follow-up questions regarding survey difficulty and additional demographic details.

### Sample Recruitment

A total of 3365 respondents were recruited by an Australian online panel company, Pureprofile. The panel company gave a small incentive to respondents who fully completed the survey. The study sample was representative of the Australian general population in terms of age, gender, and region. As mentioned, 8 of 19 designs were selected for this study, so we used a subset of the sample (*N* = 1432). The quota allocation (age, gender, and region) was applied to each design to minimise the potential impact of these demographics on the results.

### Attribute Non-attendance

The performance of the designs was compared by evaluating ANA. The ECLC model was used to identify the variations in ANA patterns to the dimensions of the EQ-5D-5L across these designs. Unlike the commonly used latent class model that focuses on preference heterogeneity, the ECLC model defines classes based on respondents’ behaviour regarding attribute attendance. A high membership probability in a class indicates a greater likelihood of engaging in the attribute attendance behaviour associated with that class. This model not only generates preference estimates but also provides information on the probability of each possible ANA strategy for each individual. When an attribute is ignored, its coefficient is assumed to be zero. For attributes that are considered, they are set to have the same values across all classes, assuming homogeneous taste parameters. However, information-processing behaviour is assumed to be heterogeneous.

There are 32 (= 2<sup>5</sup>) possible ANA strategies for the choice sets used, ranging from attending to each dimension to ignoring all dimensions of the EQ-5D-5L and choosing the preferred health state randomly. Other possible ANA strategies include nonattendance to one, two, three, or four of the five attributes. These strategies translate into 32 possible classes within the ECLC model. However, including all 32 classes simultaneously could result in issues of over-identification. To address this, a five-step approach was adopted to include and exclude ANA patterns. Classes with a membership probability below 5% were deemed insignificant and therefore excluded from the model, as suggested by Doherty et al. \[16\]. Only significant classes were retained in the ECLC model. The estimation of the ECLC model began with six classes, including one class representing full attendance and five classes featuring non-attendance to exactly one of the five dimensions. In the second step, nonsignificant classes from step one were removed and the next 10 = $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${C}_{2}^{5}$$\end{document}`$ processing strategies where respondents ignored exactly two attributes were included in the model estimation. Similarly, the model in step three removed nonsignificant classes from step two and included the next 10 = $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${C}_{3}^{5}$$\end{document}`$ classes representing respondents assumed to have ignored exactly three attributes. In step four, the model was re-estimated including significant classes from step three, along with five ANA patterns = $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${C}_{4}^{5}$$\end{document}`$ where respondents considered only one dimension, and a class where all attributes were ignored. Finally, the resulting ECLC model, consisting only of significant classes, was used to generate estimates for the EQ-5D-5L.

### Statistical Modelling

The multinomial logit (MNL) model was employed to analyse the choice data. The utility for respondent *i* associated with option *j* in choice task *t* is given by

<div id="Equ1" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U_{ijt} = x_{ijt} \beta + \epsilon_{ijt} .$$\end{document}
```

</div>

where *x*<sub>*ijt*</sub> is a vector of dummy coded attribute levels shown to individual *i* as option *j* in choice task *t*, and *β* is a preference vector for the effects of these attribute levels, assuming preference homogeneity. The error term $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\epsilon_{ijt}$$\end{document}`$ is assumed to have a standard type I extreme value distribution. The probability of respondent *i* choosing option *j* in choice task *t* under the MNL framework can be described as:

<div id="Equ2" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P_{ijt} \vee \beta = \frac{{e^{{\beta x_{ijt} }} }}{{\mathop \sum \nolimits_{j = 1}^{J} e^{{\beta x_{ijt} }} }}.$$\end{document}
```

</div>

The MNL model assigns a weight to each dimension for every respondent, even if respondents might not engage with the dimensions. To address this issue, the ECLC model was used to explore different ANA patterns. In this model, individuals are classified into latent classes based on their ANA patterns, and the parameter of class *c* is denoted by *β*<sub>*c*</sub>. Across all classes, preference parameters are assumed to be the same except for the non-attended dimensions, and hence are the same as the MNL model. For non-attended dimensions, their parameters are set to be zero. The probability of observing the ANA pattern *c* for individual *i* choosing option *j* in choice task *t* can be written as:

<div id="Equ3" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P_{ijt} \vee \beta_{c} = \frac{{e^{{\beta_{c} x_{ijt} }} }}{{\mathop \sum \nolimits_{j = 1}^{J} e^{{\beta_{c} x_{ijt} }} }}.$$\end{document}
```

</div>

Based on the ANA analysis, respondents who have attended all five attributes (full attenders) and those who did not attend all five (partial attenders) can be identified. To test for differences in estimates by full attendance status, the data were first analysed using the MNL model with main effects and interactions between a dummy indicating full attendance or not, and each attribute level.

In addition, separate MNL main effects models were estimated for all respondents and full attenders. This was conducted to compare the EQ-5D-5L coefficients before and after exclusion, employing ANA analysis as a quality check procedure. To compare MNL results across different models, the coefficients were anchored using the coefficient for the worst EQ-5D-5L state (55555). Furthermore, we examined the relative attribute importance (RAI) scores both before and after data exclusion. The RAI scores were calculated by dividing the sum of all coefficients for each dimension by the sum of all coefficients, as shown in Eq. <a href="#Equ4" data-ref-type="disp-formula">4</a>.

<div id="Equ4" class="disp-formula">

``` math
\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$RAI_{k} = \frac{{\beta_{k} }}{{\beta_{MO} + \beta_{SC} + \beta_{UA} + \beta_{PD} + \beta_{AD} }}$$\end{document}
```

</div>

where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\beta }_{k}$$\end{document}`$ is the sum of all coefficients for each dimension of the EQ-5D-5L.

An external validity analysis was conducted to assess the extent to which the ECLC model’s attendance classifications align with respondents’ levels of engagement and attentiveness. Specifically, the presence of straightlining (i.e., selecting the same option repeatedly, e.g., AAAA … or BBBB …), completion times for both the choice tasks and the overall survey, and feedback question responses regarding task difficulty and consideration of the entire description were examined. These indicators were then compared across the three attendance classes (full attenders, partial attenders, and non-attenders) to determine whether the observed behaviours matched the expected pattern of decreasing attentiveness and engagement.

The ANA analysis was performed in Latent GOLD 5.1 \[17\], and the MNL models were estimated in R \[18\] and RStudio \[19\], using the *gmnl* package \[20\].

## Results

### Respondent Characteristics

The characteristics of the overall sample are similar to those of the overall Australian population in terms of age, gender, and region at the state and territory level. There is no significant difference between the subsamples at the 0.05 level by age, gender, or region for the overlap or non-overlap groups. This is also the case for most of the other demographic characteristics measured. However, the respondents are more highly educated than the overall Australian population. At the overall level, 47% of the sample reported having a long-term health condition, and 22% reported themselves to be in the best EQ-5D-5L health state.

### ANA Probabilities

Table <a href="#Tab1" data-ref-type="table">1</a> presents estimated probabilities from the ECLC model. For designs without overlap, the generator-developed designs showed the highest probability of attending to all five EQ-5D attributes (28.4%), whereas the lowest estimated full attendance rate was observed in SAS designs (22.3%). The lowest probability of ignoring all attributes was found in Ngene designs (8.5%) and the highest in R designs (17.8%).

<div id="Tab1" class="table-wrap">

<div class="caption">

Estimated class probabilities from the final equality constrained latent class (ECLC) model for each design

</div>

<table>
<thead>
<tr>
<th colspan="4" style="text-align: left;">No overlap</th>
<th colspan="4" style="text-align: left;">Overlap</th>
</tr>
<tr>
<th style="text-align: left;">Class</th>
<th style="text-align: left;">Attributes non-attended</th>
<th style="text-align: left;">Prob. (%)</th>
<th style="text-align: left;">95% CI</th>
<th style="text-align: left;">Class</th>
<th style="text-align: left;">Attributes non-attended</th>
<th style="text-align: left;">Prob. (%)</th>
<th style="text-align: left;">95% CI</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8" style="text-align: left;">Gen-dev</td>
</tr>
<tr>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td style="text-align: left;"><strong>28.4</strong></td>
<td><strong>28.3–28.6</strong></td>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td><strong>30.8</strong></td>
<td><strong>30.7–31.0</strong></td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;">PD+AD</td>
<td style="text-align: left;">6.3</td>
<td>6.2–6.3</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">AD</td>
<td>21.2</td>
<td>21.1–21.4</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: left;">MO+UA+AD</td>
<td style="text-align: left;">5.1</td>
<td>5.0–5.1</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">MO+SC</td>
<td>9.9</td>
<td>9.8–10.0</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">MO+SC+UA+PD</td>
<td style="text-align: left;">15.7</td>
<td>15.6–15.7</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">PD+AD</td>
<td>16.6</td>
<td>16.4–16.7</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: left;">MO+SC+UA+AD</td>
<td style="text-align: left;">9.3</td>
<td>9.2–9.4</td>
<td style="text-align: left;"><strong>5</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td><strong>21.5</strong></td>
<td><strong>21.4–21.6</strong></td>
</tr>
<tr>
<td style="text-align: left;">6</td>
<td style="text-align: left;">MO+UA+PD+AD</td>
<td style="text-align: left;">8.2</td>
<td>8.1–8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">7</td>
<td style="text-align: left;">SC+UA+PD+AD</td>
<td style="text-align: left;">12.1</td>
<td>12.0–12.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>8</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td style="text-align: left;"><strong>15.0</strong></td>
<td><strong>15.0–15.2</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">Ngene</td>
</tr>
<tr>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td style="text-align: left;"><strong>24.6</strong></td>
<td><strong>24.6–24.9</strong></td>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td><strong>54.2</strong></td>
<td><strong>54.2–54.4</strong></td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">9.7</td>
<td>9.5–9.7</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">PD+AD</td>
<td>22.9</td>
<td>22.8–23.1</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: left;">MO+SC</td>
<td style="text-align: left;">12.5</td>
<td>12.4–12.6</td>
<td style="text-align: left;"><strong>3</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td><strong>22.9</strong></td>
<td><strong>22.7–22.9</strong></td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">SC+PD+AD</td>
<td style="text-align: left;">8.5</td>
<td>8.4–8.5</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: left;">UA+PD+AD</td>
<td style="text-align: left;">8.6</td>
<td>8.5–8.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">6</td>
<td style="text-align: left;">MO+SC+UA+PD</td>
<td style="text-align: left;">14.3</td>
<td>14.3–14.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">7</td>
<td style="text-align: left;">MO+UA+PD+AD</td>
<td style="text-align: left;">8.9</td>
<td>8.8–8.9</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">8</td>
<td style="text-align: left;">SC+UA+PD+AD</td>
<td style="text-align: left;">4.3</td>
<td>4.3–4.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>9</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td style="text-align: left;"><strong>8.5</strong></td>
<td><strong>8.5–8.6</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">SAS</td>
</tr>
<tr>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td style="text-align: left;"><strong>22.3</strong></td>
<td>22.1–22.3</td>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td><strong>49.4</strong></td>
<td><strong>49.4–49.8</strong></td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;">SC</td>
<td style="text-align: left;">9.8</td>
<td>9.7–9.9</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">SC+UA</td>
<td>14.3</td>
<td>14.1–14.3</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: left;">MO+SC+UA</td>
<td style="text-align: left;">5.8</td>
<td>5.6–5.8</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">UA+AD</td>
<td>10.4</td>
<td>10.3–10.4</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">UA+PD+AD</td>
<td style="text-align: left;">16.8</td>
<td>16.7–16.9</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">PD+AD</td>
<td>8.2</td>
<td>8.1–8.3</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: left;">MO+SC+UA+PD</td>
<td style="text-align: left;">12.9</td>
<td>12.9–13.0</td>
<td style="text-align: left;"><strong>5</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td><strong>17.6</strong></td>
<td><strong>17.5–17.7</strong></td>
</tr>
<tr>
<td style="text-align: left;">6</td>
<td style="text-align: left;">MO+SC+UA+AD</td>
<td style="text-align: left;">5.6</td>
<td>5.5–5.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">7</td>
<td style="text-align: left;">SC+UA+PD+AD</td>
<td style="text-align: left;">14.6</td>
<td>14.5–14.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><strong>8</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td style="text-align: left;"><strong>12.3</strong></td>
<td><strong>12.1–12.3</strong></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="8" style="text-align: left;">R</td>
</tr>
<tr>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td style="text-align: left;"><strong>22.6</strong></td>
<td><strong>22.4–22.7</strong></td>
<td style="text-align: left;"><strong>1</strong></td>
<td style="text-align: left;"><strong>None</strong></td>
<td><strong>28.2</strong></td>
<td><strong>28.1–28.3</strong></td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;">MO</td>
<td style="text-align: left;">9.8</td>
<td>9.6–9.8</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">AD</td>
<td>8.7</td>
<td>8.6–8.8</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: left;">AD</td>
<td style="text-align: left;">21.6</td>
<td>21.6–21.8</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;">MO+SC</td>
<td>16.1</td>
<td>16.0–16.2</td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">MO+SC+UA</td>
<td style="text-align: left;">6.1</td>
<td>6.0–6.2</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">PD+AD</td>
<td>15.4</td>
<td>15.3–15.5</td>
</tr>
<tr>
<td style="text-align: left;">5</td>
<td style="text-align: left;">MO+SC+UA+PD</td>
<td style="text-align: left;">9.4</td>
<td>9.3–9.4</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">SC+UA+PD</td>
<td>9.2</td>
<td>9.1–9.2</td>
</tr>
<tr>
<td style="text-align: left;">6</td>
<td style="text-align: left;">SC+UA+PD+AD</td>
<td style="text-align: left;">12.8</td>
<td>12.8–12.9</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">SC+UA+PD+AD</td>
<td>8.4</td>
<td>8.2–8.4</td>
</tr>
<tr>
<td style="text-align: left;"><strong>7</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td style="text-align: left;"><strong>17.8</strong></td>
<td><strong>17.6–17.8</strong></td>
<td style="text-align: left;"><strong>7</strong></td>
<td style="text-align: left;"><strong>MO+SC+UA+PD+AD</strong></td>
<td><strong>14.1</strong></td>
<td><strong>14.0–14.2</strong></td>
</tr>
</tbody>
</table>

Bold text indicates full attendance and non-attendance classes

*AD* anxiety/depression, *CI* confidence interval, *Gen-dev* generator-developed designs \[11\], *MO* mobility, *Ngene* modified Fedorov designs constructed in Ngene \[9\], *PD* pain/discomfort, *Prob.* probability, *R* Bayesian D-efficient design algorithm implemented in R by Oppe and van Hout \[14\] based on Rose et al. \[15\], *SAS* modified Fedorov designs constructed in SAS \[10\], *SC* self-care, *UA* usual activities

</div>

More importantly, the inclusion of attribute overlap had a significant impact on the inferred attendance rates for all attributes, regardless of the specific design method employed. It is worth noting that Ngene and SAS designs had the most significant improvements. The attendance estimates for these two methods without attribute overlap were at 24.6% and 22.3%, respectively. When examining designs with attribute overlap, these rates increased to 54.2% and 49.4%, respectively. An intriguing observation is that attribute overlap not only increased the estimated rate of attendance to all attributes in the generator-developed, Ngene, and SAS designs but also increased the estimated rate of non-attendance (i.e., none of the dimensions being considered). However, this effect was not observed in the R designs.

### Health State Valuation

Table <a href="#Tab2" data-ref-type="table">2</a> focuses on designs with overlap and presents estimates derived from MNLs with main effects and interactions between a dummy indicating whether or not the respondent considered all attribute levels (i.e., reflecting partial attenders and full attenders). The corresponding estimates derived from designs with no overlap can be found in Table <a href="#Tab3" data-ref-type="table">3</a>. Most of the main effects of the dimensions were statistically different from zero. Several interaction terms were statistically significant, especially for levels 4 and 5 in each attribute. This suggests that attribute attendance influenced the decrements of these attribute levels. The number of statistically significant interaction terms ranged from 13 to 17 in designs with overlap and from 12 to 15 in designs without overlap. Furthermore, most significant parameter magnitudes were larger among full attenders than among partial attenders. For example, examining MO3 for the generator-developed design with overlap in Table <a href="#Tab2" data-ref-type="table">2</a>, the decrements of MO3 for partial attenders and full attenders were significantly different, at − 0.427 and − 1.168 (− 0.427 to − 0.741), respectively. However, there was one exception: the magnitude of level 2 in the mobility dimension in the R design with overlap was larger in partial attenders than in full attenders.

<div id="Tab2" class="table-wrap">

<div class="caption">

Estimates from multinomial logit models with full attendance interactions for designs with overlap

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Gendev</th>
<th colspan="3" style="text-align: left;">Ngene</th>
<th colspan="3" style="text-align: left;">SAS</th>
<th colspan="3" style="text-align: left;">R</th>
</tr>
<tr>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO2</td>
<td style="text-align: left;">− 0.216</td>
<td style="text-align: left;">0.121</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">− 0.246</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.077</td>
<td style="text-align: left;">− 0.236</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">− 0.414</td>
<td style="text-align: left;">0.121</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO3</td>
<td style="text-align: left;">− 0.427</td>
<td style="text-align: left;">0.151</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;">− 0.234</td>
<td style="text-align: left;">0.151</td>
<td style="text-align: left;">0.122</td>
<td style="text-align: left;">− 0.601</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.277</td>
<td style="text-align: left;">0.116</td>
<td style="text-align: left;">0.017</td>
</tr>
<tr>
<td style="text-align: left;">MO4</td>
<td style="text-align: left;">− 0.937</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.665</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.672</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.800</td>
<td style="text-align: left;">0.129</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO5</td>
<td style="text-align: left;">− 1.197</td>
<td style="text-align: left;">0.132</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.148</td>
<td style="text-align: left;">0.166</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.536</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.025</td>
<td style="text-align: left;">0.130</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC2</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;">0.824</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.141</td>
<td style="text-align: left;">0.800</td>
<td style="text-align: left;">− 0.198</td>
<td style="text-align: left;">0.149</td>
<td style="text-align: left;">0.183</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.129</td>
<td style="text-align: left;">0.498</td>
</tr>
<tr>
<td style="text-align: left;">SC3</td>
<td style="text-align: left;">− 0.322</td>
<td style="text-align: left;">0.152</td>
<td style="text-align: left;">0.034</td>
<td style="text-align: left;">0.059</td>
<td style="text-align: left;">0.154</td>
<td style="text-align: left;">0.703</td>
<td style="text-align: left;">− 0.169</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">0.247</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">0.923</td>
</tr>
<tr>
<td style="text-align: left;">SC4</td>
<td style="text-align: left;">− 0.826</td>
<td style="text-align: left;">0.154</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.457</td>
<td style="text-align: left;">0.150</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">− 0.575</td>
<td style="text-align: left;">0.151</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.325</td>
<td style="text-align: left;">0.150</td>
<td style="text-align: left;">0.030</td>
</tr>
<tr>
<td style="text-align: left;">SC5</td>
<td style="text-align: left;">− 1.160</td>
<td style="text-align: left;">0.131</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.591</td>
<td style="text-align: left;">0.137</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.723</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.596</td>
<td style="text-align: left;">0.144</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA2</td>
<td style="text-align: left;">− 0.236</td>
<td style="text-align: left;">0.088</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">0.226</td>
<td style="text-align: left;">0.136</td>
<td style="text-align: left;">0.095</td>
<td style="text-align: left;">0.211</td>
<td style="text-align: left;">0.149</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">− 0.139</td>
<td style="text-align: left;">0.137</td>
<td style="text-align: left;">0.312</td>
</tr>
<tr>
<td style="text-align: left;">UA3</td>
<td style="text-align: left;">− 0.483</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">0.569</td>
<td style="text-align: left;">0.048</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">0.731</td>
<td style="text-align: left;">− 0.102</td>
<td style="text-align: left;">0.136</td>
<td style="text-align: left;">0.453</td>
</tr>
<tr>
<td style="text-align: left;">UA4</td>
<td style="text-align: left;">− 1.052</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.092</td>
<td style="text-align: left;">0.134</td>
<td style="text-align: left;">0.490</td>
<td style="text-align: left;">0.098</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">0.502</td>
<td style="text-align: left;">− 0.218</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">0.119</td>
</tr>
<tr>
<td style="text-align: left;">UA5</td>
<td style="text-align: left;">− 1.354</td>
<td style="text-align: left;">0.094</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.545</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.329</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">− 0.486</td>
<td style="text-align: left;">0.174</td>
<td style="text-align: left;">0.005</td>
</tr>
<tr>
<td style="text-align: left;">PD2</td>
<td style="text-align: left;">− 0.199</td>
<td style="text-align: left;">0.123</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.049</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;">0.753</td>
<td style="text-align: left;">0.114</td>
<td style="text-align: left;">0.136</td>
<td style="text-align: left;">0.404</td>
<td style="text-align: left;">− 0.118</td>
<td style="text-align: left;">0.129</td>
<td style="text-align: left;">0.360</td>
</tr>
<tr>
<td style="text-align: left;">PD3</td>
<td style="text-align: left;">− 0.230</td>
<td style="text-align: left;">0.154</td>
<td style="text-align: left;">0.135</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">0.142</td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">− 0.389</td>
<td style="text-align: left;">0.136</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">− 0.255</td>
<td style="text-align: left;">0.133</td>
<td style="text-align: left;">0.055</td>
</tr>
<tr>
<td style="text-align: left;">PD4</td>
<td style="text-align: left;">− 0.829</td>
<td style="text-align: left;">0.158</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.037</td>
<td style="text-align: left;">0.154</td>
<td style="text-align: left;">0.808</td>
<td style="text-align: left;">− 0.691</td>
<td style="text-align: left;">0.131</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.661</td>
<td style="text-align: left;">0.115</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD5</td>
<td style="text-align: left;">− 1.043</td>
<td style="text-align: left;">0.135</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.096</td>
<td style="text-align: left;">0.128</td>
<td style="text-align: left;">0.454</td>
<td style="text-align: left;">− 0.856</td>
<td style="text-align: left;">0.140</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.601</td>
<td style="text-align: left;">0.146</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD2</td>
<td style="text-align: left;">− 0.038</td>
<td style="text-align: left;">0.130</td>
<td style="text-align: left;">0.770</td>
<td style="text-align: left;">0.139</td>
<td style="text-align: left;">0.182</td>
<td style="text-align: left;">0.446</td>
<td style="text-align: left;">0.364</td>
<td style="text-align: left;">0.134</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">0.219</td>
<td style="text-align: left;">0.168</td>
<td style="text-align: left;">0.194</td>
</tr>
<tr>
<td style="text-align: left;">AD3</td>
<td style="text-align: left;">− 0.128</td>
<td style="text-align: left;">0.155</td>
<td style="text-align: left;">0.407</td>
<td style="text-align: left;">− 0.277</td>
<td style="text-align: left;">0.190</td>
<td style="text-align: left;">0.144</td>
<td style="text-align: left;">− 0.071</td>
<td style="text-align: left;">0.134</td>
<td style="text-align: left;">0.595</td>
<td style="text-align: left;">− 0.171</td>
<td style="text-align: left;">0.143</td>
<td style="text-align: left;">0.229</td>
</tr>
<tr>
<td style="text-align: left;">AD4</td>
<td style="text-align: left;">− 0.341</td>
<td style="text-align: left;">0.157</td>
<td style="text-align: left;">0.030</td>
<td style="text-align: left;">0.407</td>
<td style="text-align: left;">0.185</td>
<td style="text-align: left;">0.028</td>
<td style="text-align: left;">− 0.407</td>
<td style="text-align: left;">0.132</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">− 0.818</td>
<td style="text-align: left;">0.147</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD5</td>
<td style="text-align: left;">− 0.439</td>
<td style="text-align: left;">0.135</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">0.050</td>
<td style="text-align: left;">0.148</td>
<td style="text-align: left;">0.738</td>
<td style="text-align: left;">− 0.633</td>
<td style="text-align: left;">0.135</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.863</td>
<td style="text-align: left;">0.132</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td colspan="13" style="text-align: left;">Interaction with full attendance</td>
</tr>
<tr>
<td style="text-align: left;"> MO2</td>
<td style="text-align: left;">− 0.111</td>
<td style="text-align: left;">0.264</td>
<td style="text-align: left;">0.673</td>
<td style="text-align: left;"><strong>− 0.603</strong></td>
<td style="text-align: left;">0.209</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;"><strong>− 0.443</strong></td>
<td style="text-align: left;">0.224</td>
<td style="text-align: left;">0.048</td>
<td style="text-align: left;">0.070</td>
<td style="text-align: left;">0.281</td>
<td style="text-align: left;">0.802</td>
</tr>
<tr>
<td style="text-align: left;"> MO3</td>
<td style="text-align: left;"><strong>− 0.741</strong></td>
<td style="text-align: left;">0.335</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;"><strong>− 0.653</strong></td>
<td style="text-align: left;">0.231</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;"><strong>− 0.777</strong></td>
<td style="text-align: left;">0.268</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">− 0.344</td>
<td style="text-align: left;">0.290</td>
<td style="text-align: left;">0.236</td>
</tr>
<tr>
<td style="text-align: left;"> MO4</td>
<td style="text-align: left;"><strong>− 1.121</strong></td>
<td style="text-align: left;">0.350</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;"><strong>− 1.221</strong></td>
<td style="text-align: left;">0.258</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.013</strong></td>
<td style="text-align: left;">0.277</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.817</strong></td>
<td style="text-align: left;">0.289</td>
<td style="text-align: left;">0.005</td>
</tr>
<tr>
<td style="text-align: left;"> MO5</td>
<td style="text-align: left;"><strong>− 1.904</strong></td>
<td style="text-align: left;">0.316</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.421</strong></td>
<td style="text-align: left;">0.266</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.513</strong></td>
<td style="text-align: left;">0.311</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.275</strong></td>
<td style="text-align: left;">0.318</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> SC2</td>
<td style="text-align: left;">− 0.309</td>
<td style="text-align: left;">0.274</td>
<td style="text-align: left;">0.258</td>
<td style="text-align: left;">− 0.146</td>
<td style="text-align: left;">0.225</td>
<td style="text-align: left;">0.515</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;">0.272</td>
<td style="text-align: left;">0.993</td>
<td style="text-align: left;"><strong>− 1.378</strong></td>
<td style="text-align: left;">0.318</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> SC3</td>
<td style="text-align: left;"><strong>− 0.841</strong></td>
<td style="text-align: left;">0.333</td>
<td style="text-align: left;">0.012</td>
<td style="text-align: left;"><strong>− 0.512</strong></td>
<td style="text-align: left;">0.249</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;"><strong>− 0.477</strong></td>
<td style="text-align: left;">0.237</td>
<td style="text-align: left;">0.044</td>
<td style="text-align: left;"><strong>− 0.979</strong></td>
<td style="text-align: left;">0.336</td>
<td style="text-align: left;">0.004</td>
</tr>
<tr>
<td style="text-align: left;"> SC4</td>
<td style="text-align: left;"><strong>− 1.315</strong></td>
<td style="text-align: left;">0.343</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.661</strong></td>
<td style="text-align: left;">0.245</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;"><strong>− 1.652</strong></td>
<td style="text-align: left;">0.277</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.905</strong></td>
<td style="text-align: left;">0.397</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> SC5</td>
<td style="text-align: left;"><strong>− 1.936</strong></td>
<td style="text-align: left;">0.313</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.072</strong></td>
<td style="text-align: left;">0.249</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.293</strong></td>
<td style="text-align: left;">0.299</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.803</strong></td>
<td style="text-align: left;">0.452</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> UA2</td>
<td style="text-align: left;">− 0.284</td>
<td style="text-align: left;">0.200</td>
<td style="text-align: left;">0.157</td>
<td style="text-align: left;">− 0.256</td>
<td style="text-align: left;">0.202</td>
<td style="text-align: left;">0.206</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.289</td>
<td style="text-align: left;">0.771</td>
<td style="text-align: left;">− 0.359</td>
<td style="text-align: left;">0.305</td>
<td style="text-align: left;">0.239</td>
</tr>
<tr>
<td style="text-align: left;"> UA3</td>
<td style="text-align: left;">− 0.235</td>
<td style="text-align: left;">0.210</td>
<td style="text-align: left;">0.263</td>
<td style="text-align: left;"><strong>− 0.995</strong></td>
<td style="text-align: left;">0.229</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.341</td>
<td style="text-align: left;">0.266</td>
<td style="text-align: left;">0.200</td>
<td style="text-align: left;">− 0.358</td>
<td style="text-align: left;">0.301</td>
<td style="text-align: left;">0.234</td>
</tr>
<tr>
<td style="text-align: left;"> UA4</td>
<td style="text-align: left;"><strong>− 0.903</strong></td>
<td style="text-align: left;">0.248</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.044</strong></td>
<td style="text-align: left;">0.216</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.874</strong></td>
<td style="text-align: left;">0.252</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.518</strong></td>
<td style="text-align: left;">0.352</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> UA5</td>
<td style="text-align: left;"><strong>− 0.879</strong></td>
<td style="text-align: left;">0.225</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.860</strong></td>
<td style="text-align: left;">0.213</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.321</strong></td>
<td style="text-align: left;">0.256</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.590</strong></td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> PD2</td>
<td style="text-align: left;">− 0.328</td>
<td style="text-align: left;">0.279</td>
<td style="text-align: left;">0.241</td>
<td style="text-align: left;"><strong>− 0.558</strong></td>
<td style="text-align: left;">0.242</td>
<td style="text-align: left;">0.021</td>
<td style="text-align: left;">− 0.280</td>
<td style="text-align: left;">0.235</td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;">0.032</td>
<td style="text-align: left;">0.323</td>
<td style="text-align: left;">0.921</td>
</tr>
<tr>
<td style="text-align: left;"> PD3</td>
<td style="text-align: left;">− 0.518</td>
<td style="text-align: left;">0.356</td>
<td style="text-align: left;">0.145</td>
<td style="text-align: left;"><strong>− 0.959</strong></td>
<td style="text-align: left;">0.226</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.740</strong></td>
<td style="text-align: left;">0.242</td>
<td style="text-align: left;">0.002</td>
<td style="text-align: left;"><strong>− 0.809</strong></td>
<td style="text-align: left;">0.302</td>
<td style="text-align: left;">0.007</td>
</tr>
<tr>
<td style="text-align: left;"> PD4</td>
<td style="text-align: left;"><strong>− 1.782</strong></td>
<td style="text-align: left;">0.407</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.072</strong></td>
<td style="text-align: left;">0.256</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.796</strong></td>
<td style="text-align: left;">0.256</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.502</strong></td>
<td style="text-align: left;">0.323</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> PD5</td>
<td style="text-align: left;"><strong>− 2.403</strong></td>
<td style="text-align: left;">0.358</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.667</strong></td>
<td style="text-align: left;">0.231</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.864</strong></td>
<td style="text-align: left;">0.286</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.971</strong></td>
<td style="text-align: left;">0.433</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD2</td>
<td style="text-align: left;">− 0.587</td>
<td style="text-align: left;">0.330</td>
<td style="text-align: left;">0.075</td>
<td style="text-align: left;">− 0.242</td>
<td style="text-align: left;">0.295</td>
<td style="text-align: left;">0.412</td>
<td style="text-align: left;"><strong>− 1.027</strong></td>
<td style="text-align: left;">0.250</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.667</td>
<td style="text-align: left;">0.419</td>
<td style="text-align: left;">0.112</td>
</tr>
<tr>
<td style="text-align: left;"> AD3</td>
<td style="text-align: left;"><strong>− 1.640</strong></td>
<td style="text-align: left;">0.390</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.747</strong></td>
<td style="text-align: left;">0.276</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;"><strong>− 1.103</strong></td>
<td style="text-align: left;">0.240</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.296</strong></td>
<td style="text-align: left;">0.349</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD4</td>
<td style="text-align: left;"><strong>− 3.253</strong></td>
<td style="text-align: left;">0.405</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.581</strong></td>
<td style="text-align: left;">0.289</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.262</strong></td>
<td style="text-align: left;">0.289</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 3.464</strong></td>
<td style="text-align: left;">0.493</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD5</td>
<td style="text-align: left;"><strong>− 4.247</strong></td>
<td style="text-align: left;">0.429</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.610</strong></td>
<td style="text-align: left;">0.245</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.150</strong></td>
<td style="text-align: left;">0.319</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.950</strong></td>
<td style="text-align: left;">0.439</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Significant interaction terms (<em>n</em>)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">13</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">17</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">16</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">14</td>
</tr>
<tr>
<td style="text-align: left;"> AIC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3941</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3666</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3452</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4164</td>
</tr>
<tr>
<td style="text-align: left;"> BIC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4189</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3913</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3700</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4411</td>
</tr>
<tr>
<td style="text-align: left;">L L</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 1930</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 1793</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 1686</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 2042</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *AIC* Akaike information criterion, *BIC* Bayesian information criterion, *Coef* coefficient estimate, *Gen-dev* generator-developed designs \[11\], *LL* log-likelihood, *MO* mobility, *Ngene* modified Fedorov designs constructed in Ngene \[9\], *Obs* number of observations, *P* p-value, *PD* pain/discomfort, *R* Bayesian D-efficient design algorithm implemented in R by Oppe and van Hout \[14\] based on Rose et al. \[15\], *SAS* modified Fedorov designs constructed in SAS \[10\], *SC* self-care, *SE* standard error, *UA* usual activities

Significant interaction terms are in bold

</div>

<div id="Tab3" class="table-wrap">

<div class="caption">

Estimates from multinomial logit models with full attendance interactions for designs with no overlap

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Gendev</th>
<th colspan="3" style="text-align: left;">Ngene</th>
<th colspan="3" style="text-align: left;">SAS</th>
<th colspan="3" style="text-align: left;">R</th>
</tr>
<tr>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
<th style="text-align: left;">Coef</th>
<th style="text-align: left;">SE</th>
<th style="text-align: left;"><em>P</em></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO2</td>
<td style="text-align: left;">− 0.272</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">− 0.083</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.329</td>
<td style="text-align: left;">− 0.177</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.036</td>
<td style="text-align: left;">0.031</td>
<td style="text-align: left;">0.116</td>
<td style="text-align: left;">0.791</td>
</tr>
<tr>
<td style="text-align: left;">MO3</td>
<td style="text-align: left;">− 0.214</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.014</td>
<td style="text-align: left;">− 0.157</td>
<td style="text-align: left;">0.088</td>
<td style="text-align: left;">0.075</td>
<td style="text-align: left;">− 0.276</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">− 0.038</td>
<td style="text-align: left;">0.096</td>
<td style="text-align: left;">0.690</td>
</tr>
<tr>
<td style="text-align: left;">MO4</td>
<td style="text-align: left;">− 0.599</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.723</td>
<td style="text-align: left;">0.093</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.811</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.447</td>
<td style="text-align: left;">0.108</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">MO5</td>
<td style="text-align: left;">− 0.853</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.989</td>
<td style="text-align: left;">0.100</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 1.099</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.663</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC2</td>
<td style="text-align: left;">− 0.151</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">0.074</td>
<td style="text-align: left;">− 0.245</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">− 0.110</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.200</td>
<td style="text-align: left;">− 0.007</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">0.945</td>
</tr>
<tr>
<td style="text-align: left;">SC3</td>
<td style="text-align: left;">− 0.191</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;">− 0.143</td>
<td style="text-align: left;">0.088</td>
<td style="text-align: left;">0.104</td>
<td style="text-align: left;">− 0.104</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.224</td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.101</td>
<td style="text-align: left;">0.860</td>
</tr>
<tr>
<td style="text-align: left;">SC4</td>
<td style="text-align: left;">− 0.429</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.681</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.397</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.364</td>
<td style="text-align: left;">0.100</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">SC5</td>
<td style="text-align: left;">− 0.597</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.687</td>
<td style="text-align: left;">0.093</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.658</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.680</td>
<td style="text-align: left;">0.118</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA2</td>
<td style="text-align: left;">− 0.129</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.128</td>
<td style="text-align: left;">0.055</td>
<td style="text-align: left;">0.091</td>
<td style="text-align: left;">0.545</td>
<td style="text-align: left;">− 0.110</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.198</td>
<td style="text-align: left;">− 0.152</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;">0.170</td>
</tr>
<tr>
<td style="text-align: left;">UA3</td>
<td style="text-align: left;">− 0.210</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">− 0.061</td>
<td style="text-align: left;">0.095</td>
<td style="text-align: left;">0.518</td>
<td style="text-align: left;">− 0.136</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.115</td>
<td style="text-align: left;">− 0.058</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;">0.601</td>
</tr>
<tr>
<td style="text-align: left;">UA4</td>
<td style="text-align: left;">− 0.281</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">− 0.238</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.006</td>
<td style="text-align: left;">− 0.199</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">0.022</td>
<td style="text-align: left;">− 0.418</td>
<td style="text-align: left;">0.099</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">UA5</td>
<td style="text-align: left;">− 0.384</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.399</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.267</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">− 0.640</td>
<td style="text-align: left;">0.108</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD2</td>
<td style="text-align: left;">− 0.143</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">− 0.131</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">0.155</td>
<td style="text-align: left;">− 0.094</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.276</td>
<td style="text-align: left;">0.110</td>
<td style="text-align: left;">0.112</td>
<td style="text-align: left;">0.328</td>
</tr>
<tr>
<td style="text-align: left;">PD3</td>
<td style="text-align: left;">− 0.295</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;">− 0.275</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">0.003</td>
<td style="text-align: left;">− 0.124</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.151</td>
<td style="text-align: left;">0.069</td>
<td style="text-align: left;">0.127</td>
<td style="text-align: left;">0.587</td>
</tr>
<tr>
<td style="text-align: left;">PD4</td>
<td style="text-align: left;">− 0.493</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.517</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.485</td>
<td style="text-align: left;">0.082</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.375</td>
<td style="text-align: left;">0.092</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">PD5</td>
<td style="text-align: left;">− 0.706</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.694</td>
<td style="text-align: left;">0.095</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.602</td>
<td style="text-align: left;">0.085</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.543</td>
<td style="text-align: left;">0.119</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD2</td>
<td style="text-align: left;">0.047</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.570</td>
<td style="text-align: left;">− 0.121</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">0.160</td>
<td style="text-align: left;">− 0.306</td>
<td style="text-align: left;">0.084</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">0.101</td>
<td style="text-align: left;">0.106</td>
<td style="text-align: left;">0.342</td>
</tr>
<tr>
<td style="text-align: left;">AD3</td>
<td style="text-align: left;">− 0.137</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.100</td>
<td style="text-align: left;">− 0.081</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">0.369</td>
<td style="text-align: left;">− 0.374</td>
<td style="text-align: left;">0.086</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.182</td>
<td style="text-align: left;">0.124</td>
<td style="text-align: left;">0.142</td>
</tr>
<tr>
<td style="text-align: left;">AD4</td>
<td style="text-align: left;">− 0.582</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.733</td>
<td style="text-align: left;">0.095</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.793</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.615</td>
<td style="text-align: left;">0.117</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;">AD5</td>
<td style="text-align: left;">− 0.573</td>
<td style="text-align: left;">0.087</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.830</td>
<td style="text-align: left;">0.090</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.845</td>
<td style="text-align: left;">0.089</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.773</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td colspan="13" style="text-align: left;">Interaction with full attendance</td>
</tr>
<tr>
<td style="text-align: left;"> MO2</td>
<td style="text-align: left;">− 0.207</td>
<td style="text-align: left;">0.227</td>
<td style="text-align: left;">0.360</td>
<td style="text-align: left;">0.083</td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;">0.724</td>
<td style="text-align: left;">− 0.362</td>
<td style="text-align: left;">0.262</td>
<td style="text-align: left;">0.167</td>
<td style="text-align: left;">− 0.153</td>
<td style="text-align: left;">0.384</td>
<td style="text-align: left;">0.690</td>
</tr>
<tr>
<td style="text-align: left;"> MO3</td>
<td style="text-align: left;"><strong>− 0.706</strong></td>
<td style="text-align: left;">0.246</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;"><strong>− 0.709</strong></td>
<td style="text-align: left;">0.244</td>
<td style="text-align: left;">0.004</td>
<td style="text-align: left;">− 0.087</td>
<td style="text-align: left;">0.298</td>
<td style="text-align: left;">0.771</td>
<td style="text-align: left;"><strong>− 0.885</strong></td>
<td style="text-align: left;">0.260</td>
<td style="text-align: left;">0.001</td>
</tr>
<tr>
<td style="text-align: left;"> MO4</td>
<td style="text-align: left;"><strong>−1.369</strong></td>
<td style="text-align: left;">0.276</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.898</strong></td>
<td style="text-align: left;">0.255</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.882</strong></td>
<td style="text-align: left;">0.328</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;"><strong>−1.526</strong></td>
<td style="text-align: left;">0.381</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> MO5</td>
<td style="text-align: left;"><strong>−1.995</strong></td>
<td style="text-align: left;">0.273</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.517</strong></td>
<td style="text-align: left;">0.290</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.324</strong></td>
<td style="text-align: left;">0.325</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.788</strong></td>
<td style="text-align: left;">0.367</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> SC2</td>
<td style="text-align: left;">− 0.292</td>
<td style="text-align: left;">0.221</td>
<td style="text-align: left;">0.185</td>
<td style="text-align: left;">− 0.382</td>
<td style="text-align: left;">0.230</td>
<td style="text-align: left;">0.097</td>
<td style="text-align: left;">− 0.399</td>
<td style="text-align: left;">0.282</td>
<td style="text-align: left;">0.156</td>
<td style="text-align: left;"><strong>− 0.785</strong></td>
<td style="text-align: left;">0.310</td>
<td style="text-align: left;">0.011</td>
</tr>
<tr>
<td style="text-align: left;"> SC3</td>
<td style="text-align: left;">− 0.169</td>
<td style="text-align: left;">0.253</td>
<td style="text-align: left;">0.506</td>
<td style="text-align: left;"><strong>− 0.973</strong></td>
<td style="text-align: left;">0.226</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;">− 0.452</td>
<td style="text-align: left;">0.284</td>
<td style="text-align: left;">0.111</td>
<td style="text-align: left;"><strong>−1.257</strong></td>
<td style="text-align: left;">0.336</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> SC4</td>
<td style="text-align: left;"><strong>−1.241</strong></td>
<td style="text-align: left;">0.259</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.479</strong></td>
<td style="text-align: left;">0.259</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.948</strong></td>
<td style="text-align: left;">0.269</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.967</strong></td>
<td style="text-align: left;">0.358</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> SC5</td>
<td style="text-align: left;"><strong>−1.743</strong></td>
<td style="text-align: left;">0.291</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.423</strong></td>
<td style="text-align: left;">0.271</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.977</strong></td>
<td style="text-align: left;">0.305</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−2.178</strong></td>
<td style="text-align: left;">0.385</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> UA2</td>
<td style="text-align: left;">− 0.105</td>
<td style="text-align: left;">0.219</td>
<td style="text-align: left;">0.631</td>
<td style="text-align: left;">0.071</td>
<td style="text-align: left;">0.241</td>
<td style="text-align: left;">0.768</td>
<td style="text-align: left;">− 0.439</td>
<td style="text-align: left;">0.273</td>
<td style="text-align: left;">0.109</td>
<td style="text-align: left;">− 0.078</td>
<td style="text-align: left;">0.324</td>
<td style="text-align: left;">0.809</td>
</tr>
<tr>
<td style="text-align: left;"> UA3</td>
<td style="text-align: left;">− 0.217</td>
<td style="text-align: left;">0.262</td>
<td style="text-align: left;">0.408</td>
<td style="text-align: left;">− 0.181</td>
<td style="text-align: left;">0.261</td>
<td style="text-align: left;">0.488</td>
<td style="text-align: left;"><strong>− 0.603</strong></td>
<td style="text-align: left;">0.272</td>
<td style="text-align: left;">0.027</td>
<td style="text-align: left;">− 0.321</td>
<td style="text-align: left;">0.313</td>
<td style="text-align: left;">0.305</td>
</tr>
<tr>
<td style="text-align: left;"> UA4</td>
<td style="text-align: left;"><strong>− 0.545</strong></td>
<td style="text-align: left;">0.266</td>
<td style="text-align: left;">0.040</td>
<td style="text-align: left;"><strong>− 0.930</strong></td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.653</strong></td>
<td style="text-align: left;">0.341</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.354</strong></td>
<td style="text-align: left;">0.304</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> UA5</td>
<td style="text-align: left;"><strong>−1.344</strong></td>
<td style="text-align: left;">0.265</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>−1.112</strong></td>
<td style="text-align: left;">0.227</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.191</strong></td>
<td style="text-align: left;">0.363</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.562</strong></td>
<td style="text-align: left;">0.306</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> PD2</td>
<td style="text-align: left;">0.100</td>
<td style="text-align: left;">0.212</td>
<td style="text-align: left;">0.637</td>
<td style="text-align: left;">− 0.324</td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;">0.165</td>
<td style="text-align: left;">− 0.129</td>
<td style="text-align: left;">0.266</td>
<td style="text-align: left;">0.629</td>
<td style="text-align: left;">− 0.259</td>
<td style="text-align: left;">0.351</td>
<td style="text-align: left;">0.461</td>
</tr>
<tr>
<td style="text-align: left;"> PD3</td>
<td style="text-align: left;">− 0.073</td>
<td style="text-align: left;">0.217</td>
<td style="text-align: left;">0.736</td>
<td style="text-align: left;"><strong>− 0.641</strong></td>
<td style="text-align: left;">0.236</td>
<td style="text-align: left;">0.007</td>
<td style="text-align: left;">− 0.254</td>
<td style="text-align: left;">0.283</td>
<td style="text-align: left;">0.369</td>
<td style="text-align: left;">− 0.611</td>
<td style="text-align: left;">0.368</td>
<td style="text-align: left;">0.097</td>
</tr>
<tr>
<td style="text-align: left;"> PD4</td>
<td style="text-align: left;"><strong>− 1.065</strong></td>
<td style="text-align: left;">0.214</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.700</strong></td>
<td style="text-align: left;">0.263</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.297</strong></td>
<td style="text-align: left;">0.288</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.485</strong></td>
<td style="text-align: left;">0.329</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> PD5</td>
<td style="text-align: left;"><strong>− 1.704</strong></td>
<td style="text-align: left;">0.257</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.718</strong></td>
<td style="text-align: left;">0.278</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.903</strong></td>
<td style="text-align: left;">0.404</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.761</strong></td>
<td style="text-align: left;">0.364</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD2</td>
<td style="text-align: left;">− 0.182</td>
<td style="text-align: left;">0.214</td>
<td style="text-align: left;">0.395</td>
<td style="text-align: left;"><strong>− 0.532</strong></td>
<td style="text-align: left;">0.231</td>
<td style="text-align: left;">0.022</td>
<td style="text-align: left;"><strong>− 0.872</strong></td>
<td style="text-align: left;">0.267</td>
<td style="text-align: left;">0.001</td>
<td style="text-align: left;"><strong>− 1.293</strong></td>
<td style="text-align: left;">0.337</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD3</td>
<td style="text-align: left;"><strong>− 0.539</strong></td>
<td style="text-align: left;">0.218</td>
<td style="text-align: left;">0.013</td>
<td style="text-align: left;"><strong>− 1.028</strong></td>
<td style="text-align: left;">0.247</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 0.670</strong></td>
<td style="text-align: left;">0.236</td>
<td style="text-align: left;">0.005</td>
<td style="text-align: left;"><strong>− 2.108</strong></td>
<td style="text-align: left;">0.407</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD4</td>
<td style="text-align: left;"><strong>− 1.597</strong></td>
<td style="text-align: left;">0.234</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.313</strong></td>
<td style="text-align: left;">0.278</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 2.001</strong></td>
<td style="text-align: left;">0.368</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 3.638</strong></td>
<td style="text-align: left;">0.477</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td style="text-align: left;"> AD5</td>
<td style="text-align: left;"><strong>− 2.290</strong></td>
<td style="text-align: left;">0.266</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.619</strong></td>
<td style="text-align: left;">0.270</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 1.599</strong></td>
<td style="text-align: left;">0.342</td>
<td style="text-align: left;">&lt; 0.001</td>
<td style="text-align: left;"><strong>− 4.140</strong></td>
<td style="text-align: left;">0.588</td>
<td style="text-align: left;">&lt; 0.001</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Significant interaction terms (<em>n</em>)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">12</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">15</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">13</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">15</td>
</tr>
<tr>
<td style="text-align: left;"> AIC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4112</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3752</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3875</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3999</td>
</tr>
<tr>
<td style="text-align: left;"> BIC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4360</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4122</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">4247</td>
</tr>
<tr>
<td style="text-align: left;"> LL</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 2016</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 1836</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 1898</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">− 1959</td>
</tr>
</tbody>
</table>

*AD* anxiety/depression, *AIC* Akaike information criterion, *BIC* Bayesian information criterion, *Coef* coefficient estimate, *Gen-dev* generator-developed designs \[11\], *LL* log-likelihood, *MO* mobility, *Ngene* modified Fedorov designs constructed in Ngene \[9\], *Obs* number of observations, *P* *p*-value, *PD* pain/discomfort, *R* Bayesian D-efficient design algorithm implemented in R by Oppe and van Hout \[14\] based on Rose et al. \[15\], *SAS* modified Fedorov designs constructed in SAS \[10\], *SC* self-care, *SE* standard error, *UA* usual activities

Significant interaction terms are in bold

</div>

MNLs with main effects only were then fitted using data from both all respondents and full attenders only (unanchored and anchored MNL results can be found in ESM-B). Figure <a href="#Fig2" data-ref-type="fig">2</a> shows the RAI scores derived from these MNL results. The RAI scores for self-care, usual activities, and pain/discomfort varied across designs, but there was no clear pattern. A notable observation was found when comparing RAI for all respondents versus full attenders, especially in the dimensions of mobility and anxiety/depression. Mobility consistently showed higher importance when using the data before exclusion as opposed to the data from only full attenders. Conversely, anxiety/depression had greater importance assigned to this dimension among full attenders than among their counterparts.

<figure id="Fig2">
<p><img src="40271_2025_735_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Relative attribute importance (RAI). <em>A</em> all respondents, <em>AD</em> anxiety/depression, <em>F</em> full attenders, <em>Gen-dev</em> generator-developed designs [<span class="citation" data-cites="CR11">11</span>], <em>MO</em> mobility, <em>Ngene</em> modified Fedorov designs constructed in Ngene [<span class="citation" data-cites="CR9">9</span>], <em>PD</em> pain/discomfort, <em>R</em> Bayesian D-efficient design algorithm implemented in R by Oppe and van Hout [<span class="citation" data-cites="CR14">14</span>] based on Rose et al. [<span class="citation" data-cites="CR15">15</span>], <em>SAS</em> modified Fedorov designs constructed in SAS [<span class="citation" data-cites="CR10">10</span>], <em>SC</em> self-care, <em>UA</em> usual activities</figcaption>
</figure>

### External Validity of the ECLC Model

Table <a href="#Tab4" data-ref-type="table">4</a> summarises the indicators of external validity across the three attendance classes identified by the ECLC model. Respondents classified as non-attenders had the highest overall rate of straightlining (3.9%), whereas partial attenders showed moderate levels (1.2%) and full attenders the lowest (0.4%). Median completion times mirrored this pattern: non-attenders spent the least time on the choice tasks (3.2 min) and on the entire survey (7.6 min), followed by partial attenders (5.0 and 8.7 min, respectively), and finally full attenders, who spent the most time on both the tasks (6.3 min) and the survey (10.2 min).

<div id="Tab4" class="table-wrap">

<div class="caption">

Straightlining, completion time, and feedback questions across three attendance classes

</div>

|  | Full attendance (*N* = 493) | Partial attendance (*n* = 705) | Non-attendance (*n* = 234) |
|----|----|----|----|
| Straightlining |  |  |  |
|  Left-most option | 2 (0.4) | 8 (1.1) | 6 (2.6) |
|  Right-most option | 0 (0.0) | 1 (0.1) | 3 (1.3) |
|  Total | 2 (0.4) | 9 (1.2) | 9 (3.9) |
| Completion time |  |  |  |
|  DCE choice tasks | 6.3 | 5.0 | 3.2 |
|  Entire survey | 10.2 | 8.7 | 7.6 |
| Feedback question<sup>a</sup> |  |  |  |
|  Task difficult<sup>b</sup> | 45 (9.7) | 87 (12.8) | 39 (17.3) |
|  Difficult to tell difference<sup>c</sup> | 52 (11.2) | 124 (18.3) | 60 (26.6) |
|  Difficult to imagine<sup>d</sup> | 84 (18.1) | 138 (20.4) | 51 (22.7) |
| Consider whole description<sup>e</sup> | 386 (82.5) | 483 (71.3) | 125 (55.6) |

Data are presented as minutes or as *N* (%)

*DCE* discrete choice experiment

<sup>a</sup>These questions were optional, and the reported percentages were calculated only among respondents who provided answers

<sup>b</sup>Percentage of respondents who selected ‘strongly agree’ or ‘agree’ for the question, "I found the tasks difficult"

<sup>c</sup>Percentage of respondents who selected ‘strongly agree’ or ‘agree’ for the question, "I found it difficult to tell the difference between the descriptions"

<sup>d</sup>Percentage of respondents who selected ‘strongly agree’ or ‘agree’ to the question, "I found it difficult to imagine the scenarios"

<sup>e</sup>Percentage of respondents who selected ‘strongly agree’ or ‘agree’ to the question, "I considered the entire description"

</div>

Feedback question responses aligned with these differences in response behaviour. Non-attenders were more likely to report that the tasks were difficult (17.3% vs. 12.8% of partial attenders and 9.7% of full attenders) and to find it difficult to tell the difference between the options (26.6% vs. 18.3% and 11.2%, respectively). In addition, only 55.6% of non-attenders strongly agreed or agreed that they considered the entire description when making their choices, in contrast to 71.3% of partial attenders and 82.5% of full attenders. These findings provide strong evidence for the external validity of the ECLC model’s classification of full attenders, partial attenders, and non-attenders, reflecting correspondingly high, moderate, and low levels of engagement and attentiveness.

In addition, demographic characteristics across the three attendance classes are presented in Table 3 in ESM-B. Non-attenders were more likely to be male, younger, and single than both full or partial attenders. No apparent differences were observed in education, household income, or region among the three classes.

## Discussion

Our analysis revealed significant variations in attribute attendance across diverse design construction methods. Moreover, the incorporation of attribute overlap yielded a significant enhancement in attribute attendance levels. In particular, modified Fedorov designs (implemented in Ngene and SAS) with attribute overlap had the highest attribute attendance rates, supporting the use of modified Fedorov designs with attribute overlap to enhance respondent engagement.

The ANA probabilities within designs without overlap in this study are in line with the results from the comparison study conducted by Iles and Rose \[5\] but inconsistent with the findings of Yao et al. \[6\]. Iles and Rose \[5\] found a higher percentage of ANA in answering efficient design surveys than with orthogonal designs, among both illiterate and literate respondents. However, Yao et al. \[6\] reported conflicting findings: that the likelihood of belonging to the class with full attendance was greater in efficient designs than in generator-developed designs. The disparate findings may be explained by the different levels of perceived difficulty of the survey. Iles and Rose \[5\] focused on preferences for healthcare providers among illiterate and literate respondents in India, whereas Yao et al. \[6\] recruited respondents from the general New Zealand population to answer questions about threatened species in planted forests. Several factors may contribute to the variance in full attendance rates, such as perceived difficulty levels, familiarity with the topic of the survey, and population characteristics. Exploring the impact of these factors on attribute attendance is a valuable potential area for future research.

Another important finding is that attribute overlap substantially enhanced the level of attribute attendance across the dimensions of the EQ-5D-5L, regardless of the methods employed in design construction. This finding aligns with the conclusions drawn by Jonker et al. \[12\], which suggested that attribute overlap leads to a rise in the average number of attended attributes from two to three. In our study, when examining the Ngene design, we observed that attribute overlap increases the full attendance rate significantly from 24.6% to 54.2%. This indicates that, even with the implementation of attribute overlap, approximately 50% of the respondents did not engage with at least one dimension of the EQ-5D-5L despite the use of attribute overlap. ANA analysis can serve as a useful quality-control tool for the inclusion and exclusion of respondents in data analysis. Ideally, the analysis should exclude respondents who did not attend to any attributes, as their choices are likely to be driven by heuristic decision-making rather than reflective of their true preferences. However, partial non-attendance may indicate either a lack of attention or a deliberate decision reflecting genuine indifference. Additional robustness checks may be warranted, particularly for respondents who focus exclusively on a single attribute.

The consideration of ANA has an influence on the coefficients of the EQ-5D-5L in health state valuations. This impact was more pronounced within the mobility and anxiety/depression dimensions. Upon ANA adjustment, the utility decrement in the mobility dimension decreased, whereas the decrements associated with anxiety/depression increased. Although this study did not directly test the order effects, it may be that respondents, especially partial attenders, prioritised dimensions presented earlier in the sequence of mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. This possibility is supported by previous research indicating that the dimension order has some influence on the valuation of the EQ-5D-5L, using methods such as DCE<sub>TTO</sub> \[21\], time trade-off (TTO) \[22\], and DCE \[22\]. In contrast, Mulhern et al. \[23\] observed no significant impact of dimension order in DCEs with duration. This discrepancy highlights the potential variability in how different preference-elicitation techniques may interact with dimension ordering. Therefore, further research is warranted to dissect the influence of dimension order on EQ-5D-5L valuations across various elicitation methods.

Preference heterogeneity is another possible explanation of the impact of ANA on the coefficients of the EQ-5D-5L. Within the framework of ECLC models, preference homogeneity among respondents is assumed. However, ANA may occur when respondents do not consider attributes because they are not important to them or arise from respondents simplifying choice tasks by ignoring attributes as a type of decision heuristic. Indeed, the impact of ANA on the valuation of EQ-5D-5L varied significantly between these two ANA assumptions \[16\]. A substantial impact of ANA on estimates was observed when assuming decision heuristics for ANA, whereas the impact was less pronounced under the preference-based explanation of ANA \[16\]. In our study, respondents placing lower importance on a particular attribute might be inaccurately classified as non-attenders. In alignment with a study by Hole et al. \[24\], the findings may reflect the upper limits relating to ANA within this dataset.

## Conclusion

Attribute attendance varied across the different design construction methods, and the implementation of attribute overlap significantly improved attendance rates. Modified Fedorov designs implemented in Ngene or SAS with attribute overlap are recommended to reduce ANA and enhance respondent engagement in DCEs. ANA models can be used to exclude respondents who did not attend to any attributes and to identify partial attenders for further robustness checks, improving the quality of data for analysis.

## Supplementary Information

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary file1 (DOCX 58 KB)

</div>

### Acknowledgements

The authors are grateful to the respondents who participated in the study. The authors also appreciate the reviewers and editors for their insightful comments and suggestions, which have significantly improved the quality and clarity of this paper.

### Funding

Open Access funding enabled and organized by CAUL and its Member Institutions.

### Declarations

#### Conflicts of Interest

This study was partially supported by a grant from the EuroQol Research Foundation (2016260). PJ’s doctoral scholarship was funded by the Australian Research Council (DP210102021). The views expressed in this paper are not necessarily those of the funders. The authors have no conflicts of interest. DS, RN, RV, MO, and BM are members of the EuroQol Research Foundation

#### Ethics Approval Statement

Ethics approval was obtained under the Centre for Health Economics Research and Evaluation Program Ethics (UTS HREC REF NO. 2015000135).

#### Author Contributions

Conceptualization: Jiang and Mulhern. Methodology: Jiang, Street, Mulhern, and Oppe. Formal analysis and investigation: Jiang and Street. Writing - original draft preparation: Jiang, Street, and Mulhern. Writing - review and editing: Norman, Viney, Oppe, Street, Mulhern, and Jiang. Funding acquisition: Mulhern, Street, Norman, and Viney. Supervision: Mulhern.

#### Data Availability

The data that support the findings of this study are available from the Centre for Health Economics Research and Evaluation, but restrictions that were applied in relation to the ethics of the current study apply to the availability of these data, so they are not publicly available. However, the data are available from the authors upon reasonable request and with the permission of the Centre for Health Economics Research and Evaluation.

## References

1. Scarpa R, Zanoli R, Bruschi V, Naspetti S. Inferred and stated attribute non-attendance in food choice experiments. J Agric Econ. 2013;95(1):165–80. 10.1093/ajae/aas073.

2. Olsen S, Meyerhoff J. Will the alphabet soup of design criteria affect discrete choice experiment results? Eur Rev Agric Econ. 2017;44(2):309–36. 10.1093/erae/jbw014.

3. Walker JL, Wang Y, Thorhauge M, Ben-Akiva M. D-efficient or deficient? a robustness analysis of stated choice experimental designs. Theor Decis. 2018;84(2):215–38. 10.1007/s11238-017-9647-3.

4. Falke A, Hruschka H. A Monte Carlo study of design-generating algorithms for the latent class mixed logit model. OR Spectrum. 2017;39(4):1035–53. 10.1007/s00291-017-0483-1.

5. Iles RA, Rose JM. Stated choice design comparison in a developing country: recall and attribute nonattendance. Heal Econ Rev. 2014;4(1):25. 10.1186/s13561-014-0025-3.10.1186/s13561-014-0025-3PMC420945725386388

6. Yao RT, Scarpa R, Rose JM, Turner JA. Experimental design criteria and their behavioural efficiency: an evaluation in the field. Environ Resource Econ. 2015;62(3):433–55. 10.1007/s10640-014-9823-7.

7. Chrzan K. Using partial profile choice experiments to handle large numbers of attributes. Int J Mark Res. 2010;52(6):827–40. 10.2501/S1470785310201673.

8. Jonker M, Donkers B, de Bekker-Grob E, Stolk E. Effect of level overlap and color coding on attribute non-attendance in discrete choice experiments. Value Health. 2018. 10.1016/j.jval.2017.10.002.30005748 10.1016/j.jval.2017.10.002

9. ChoiceMetrics. Ngene 1.1.2 user manual and reference guide. Technical report, Australia, 2014. Retrieved from http://www.choice-metrics.com/. Accessed 20 Mar 2019.

10. Kuhfeld W. Marketing Research Methods in SAS (Tech. Rep.). SAS. 2010. http://support.sas.com/techsup/technote/mr2010.pdf. Accessed 25 Aug 2024.

11. Street DJ, Burgess L. The construction of optimal stated choice experiments: theory and methods. Hoboken: Wiley; 2007.

12. Jonker MF, Donkers B, de Bekker-Grob E, Stolk EA. Attribute level overlap (and color coding) can reduce task complexity, improve choice consistency, and decrease the dropout rate in discrete choice experiments. Health Econ. 2019;28:350–63. 10.1002/hec.3846.30565338 10.1002/hec.3846PMC6590347

13. Mulhern B. Broadening the measurement and valuation of health and quality of life [Doctoral dissertation, University of Technology Sydney]; 2020. UTS Digital Thesis Collection. https://opus.lib.uts.edu.au/handle/10453/142429info:eu-repo/semantics/openAccess. Accessed 25 Aug 2024.

14. Oppe M, van Hout B. The “power” of eliciting EQ-5D-5L values: the experimental design of the EQ-VT. EuroQol Working paper 17003; 2017. https://euroqol.org/wp-content/uploads/2016/10/EuroQol-Working-Paper-Series-Manuscript-17003-Mark-Oppe.pdf. Accessed 25 Aug 2024.

15. Rose J. M., Scarpa R., Bliemer M.C.J. Incorporating model uncertainty into the generation of efficient stated choice experiments: A model averaging approach; 2009. ITLS working paper. ITLS-WG-09-08.

16. Doherty E, Hobbins A, Whitehurst DGT, O’Neill C. An exploration on attribute non-attendance using discrete choice experiment data from the Irish EQ-5D-5L national valuation study. Pharmacoeconomics Open. 2021;5(2):237–44. 10.1007/s41669-020-00244-5.33481204 10.1007/s41669-020-00244-5PMC8160058

17. Vermunt JK, Magidson J. Technical guide for latent GOLD 5.1: basic, advanced, and syntax. Belmont: Statistical Innovations Inc; 2016.

18. R Core Team. R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria. 2023. https://www.R-project.org/. Accessed 10 Jun 2024.

19. Posit team. RStudio: Integrated Development Environment for R. Posit Software, PBC, Boston, MA. 2023. http://www.posit.co/. Accessed 10 Jun 2024.

20. Sarrias M, Daziano R. Multinomial logit models with continuous and discrete individual heterogeneity in R: the gmnl package. J Stat Softw. 2017;79(2):1–46. 10.18637/jss.v079.i02.30220889

21. Tsuchiya A, Mulhern B, Bansback N, Hole AR. Using DCE with duration to examine the robustness of preferences across the five dimensions of the EuroQol instrument: the second paper from the FEDEV project. In: EuroQol Group Plenary Proceedings; 2014.

22. Mulhern B, Shah K, Janssen M, Longworth L, Ibbotson R. Valuing health using time trade-off and discrete choice experiment methods: does dimension order impact on health state values? Value Health. 2016;19(2):210–7. 10.1016/j.jval.2015.11.005.27021755 10.1016/j.jval.2015.11.005

23. Mulhern B, Norman R, Lorgelly P, Lancsar E, Ratcliffe J, Brazier J, Viney R. Is Dimension order important when valuing health states using discrete choice experiments including duration? Pharmacoeconomics. 2017;35(4):439–51. 10.1007/s40273-016-0475-z.27873226 10.1007/s40273-016-0475-z

24. Hole AR, Norman R, Viney R. Response patterns in health state valuation using endogenous attribute attendance and latent class analysis. Health Econ. 2016;25(2):212–24. 10.1002/hec.3134.25521533 10.1002/hec.3134

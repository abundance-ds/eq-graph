---
project_id: "1612-RA"
work_id: "doi:10.1007/s11136-024-03770-5"
doi: "10.1007/s11136-024-03770-5"
pmid: "39269579"
pmcid: "PMC11541319"
title: "The impact of demographic change on value set validity and obsolescence"
journal: "Quality of Life Research"
publication_date: "2024-09-13"
volume: "33"
issue: "11"
authors:
  - name: "Marcel F. Jonker"
    orcid: "http://orcid.org/0000-0001-8433-1402"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/057w15z03grid.6906.90000 0000 9262 1349Erasmus School of Health Policy & Management, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "https://ror.org/057w15z03grid.6906.90000 0000 9262 1349Erasmus Choice Modelling Centre, Erasmus University Rotterdam, Rotterdam, The Netherlands"
keywords:
  - "Demographic trends"
  - "EQ-5D"
  - "Value set obsolescence"
  - "Value set redundancy"
  - "Value set validity"
licence: "cc-by"
source_file: "input/projects/1612-RA/papers/doi_10.1007_s11136-024-03770-5.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11541319/fullTextXML"
source_method: "epmc_xml"
source_sha256: "700fb82b14fb2167bcf102c9d6be5bebebd3f331aae6967252916502f681c253"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# The impact of demographic change on value set validity and obsolescence

## Abstract

### Purpose

To investigate the contribution of demographic trends in countries’ age and gender composition to value set validity and obsolescence.

### Methods

Time-trade off (TTO) valuation data from 3 EQ-5D-3L value sets of 20 years or older from the United Kingdom, Japan, and the United States were re-analyzed using Bayesian heteroskedastic Tobit models with sex and age group-specific scale parameters. Original value sets were obtained by weighting the original preference structures with the countries’ original demographic composition at the time of the data collection. Updated value sets were created using the original preference structure weighted using the countries’ most recent demographic composition. The differences between the original and updated value sets were monitored and compared based on 95% credible intervals.

### Results

The gender and age composition of the investigated countries changed in all 3 countries over time. The modelled health state preferences also depended on the respondents’ gender and age. However, the overall impact of this demographic change on the investigated value sets was negligeable in all 3 countries and this finding was robust to accounting for the impact of ethnicity trends in the United States.

### Conclusion

Value sets may become redundant and obsolete for various reasons, but demographic change was not identified as a contributing factor.

### Supplementary Information

The online version contains supplementary material available at 10.1007/s11136-024-03770-5.

## Introduction

The use of preference-based value sets in health technology assessment (HTA) and other applications is widespread, and the validity of reported results depends on the value sets reflecting contemporary societal preferences \[1\]. On the one hand, decision-makers often prioritize consistency in value sets, at times prescribing specific sets for analyses to maintain consistency in between-study comparisons \[1, 2\]. Consequently, they may hesitate to abandon older value sets. On the other hand, several factors can render value sets increasingly outdated and eventually obsolete over time. These factors include the development of improved methods for eliciting and modelling preferences, changes in populations’ preferences, and shifts in the demographic composition of populations over time.

To date, there are no universally accepted expiration dates or guidelines for reassessing the validity of value sets. In fact, the concept of value set invalidity and subsequent obsolescence has received, with some notable exceptions, very little attention in the literature \[3, 4\]. At the same time, value sets are becoming older and are seldom updated. Hence there is a growing need to investigate the determinants of value set obsolescence. This paper focuses on a specific aspect of value set obsolescence, which is the impact of demographic shifts in the demographic composition of populations. More specifically, it aims to determine whether changes in the age/sex composition of populations, all other things being equal (ceteris paribus), can implicitly generate an expiration date for preference-based value sets.

## Methods

To evaluate the impact of demographic change on preference-based values sets, 3 of the oldest EQ-5D value sets were selected for re-analysis: those of the United Kingdom (UK) \[5, 6\], Japan (JPN) \[7\], and the United States (US) \[8\]. Permission to re-analyze the data was obtained from the corresponding authors and the time trade-off (TTO) valuation data were subsequently obtained from public data repositories and from the corresponding author of the Japanese value set. The obtained data comprised, in addition to the TTO-derived health-state values, also the participating respondents’ sex and age, and in the case of the USA, the respondents’ race/ethnicity, which was used in a sensitivity analysis that is reported in the online supplemental materials. The respondents’ age was recoded into 4 groups, i.e. 18–34, 35–54, 55–74, and 75+.

To allow for an evaluation of the impact of changes in the age and sex composition of the populations of these 3 countries, demographic data were obtained from the World Bank \[9\]. Both the demographic composition in the year the TTO data were collected and the most recent demographic composition from the year 2022 was obtained. This allowed the original value sets to be obtained by weighting the estimated preference structures with the countries’ original demographic composition at the time of the data collection, and updated value sets by weighting the original preference structure with the countries’ most recent demographic composition.

This was performed by re-analyzing the TTO valuation using state-of-the-art methods \[10\]. In the Japanese dataset, each respondent completed the same set of 17 TTO tasks. In the UK and US datasets, each respondent completed 12 TTO tasks that were included in the analysis, which were sampled from an overall design that comprised 45 EQ-5D-3 L health states. First, respondents with fewer than 10 observations were excluded from the analyses. Second, respondents with a positively sloped relationship between their TTO valuations and the misery index of the health states were excluded from the analyses. Third, the data of the remaining respondents was analyzed using Bayesian heteroskedastic Tobit models with censoring at -1 using a model specification that included demographic-specific scale parameters. More specifically, the observed TTO values for respondent i in task t were censored as:

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
                \begin{document}$$\:{\text{T}\text{T}\text{O}}_{\text{i}\text{t}}=\left\{\begin{array}{ll}{{\:TTO}_{it}^{*}}&{if\quad{TTO}_{it}^{*}>-1}\\{-1}&{if \quad{TTO}_{it}^{*}\le\:-1}\end{array}\right.$$\end{document}
```

</div>

with the latent $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{TTO}_{it}^{*}$$\end{document}`$ values assumed to be normally distributed:

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
                \begin{document}$$\:{\text{T}\text{T}\text{O}}_{it}^{*}\sim Normal\left(\:{\mu\:}_{it},{\sigma\:}_{it}\right).$$\end{document}
```

</div>

Here the mean $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$({\mu\:}_{it})$$\end{document}`$ and standard deviation $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$(\:{\sigma\:}_{it})$$\end{document}`$ reflect the average health state value and variation among respondents in their valuation of the health state presented in task t of respondent i, respectively. Similar to Pickard et al. \[11\]., the standard deviation $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$(\:{\sigma\:}_{it})$$\end{document}`$ was modelled as a 4th-order polynomial of the health state values:

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
                \begin{document}$$\:{{\sigma\:}_{it}=exp(\:{{\gamma\:}}_{0}+{{\gamma\:}}_{1}\mu\:}_{\text{i}\text{t}}+{{\gamma\:}}_{2}{\mu\:}_{it}^{2}+{{\gamma\:}}_{3}{\mu\:}_{it}^{3}+{{\gamma\:}}_{4}{\mu\:}_{it}^{4})$$\end{document}
```

</div>

,

which ensured that the variances of the predicted values could flexibly depend on the health state severity.

The mean$`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$(\:{\mu\:}_{it})$$\end{document}`$ was specified as follows:

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
                \begin{document}$$\begin{aligned}{{\mu\:}}_{\text{i}\text{t}}&={\beta\:}_{0}+\left({\beta\:}_{1}{\text{MO2}}_{it}+{\beta}_{2}{\text{MO3}}_{it}\right)*{{\varphi\:}\_\text{M}\text{O}}_{sa}\\&\;+\left({\beta\:}_{3}{\text{SC2}}_{it}+{\beta\:}_{4}{\text{SC3}}_{it}\right)*{{\varphi\:}\_\text{S}\text{C}}_{sa}\\&\;+({\beta\:}_{5}{\text{UA2}}_{it}+{{\:\beta\:}_{6}\text{UA3}}_{it}){\text{*}{\varphi\:}\_\text{U}\text{A}}_{sa}\\&\;+{\beta\:}_{7}{PD2}_{it}{+\:\beta\:}_{8}{PD3}_{it})*{{\varphi\:}\_\text{P}\text{D}}_{sa}\\&\;+\left({\beta\:}_{9}{AD2}_{it}{+\:\beta\:}_{10}{AD3}_{it}\right)*\:{{\varphi\:}\_\text{A}\text{D}}_{sa}.\end{aligned}$$\end{document}
```

</div>

Here $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{\beta\:}_{0}$$\end{document}`$ denotes the intercept, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{\beta\:}_{1-10}$$\end{document}`$ denote the slope coefficients that capture the EQ-5D decrements for levels 2 and 3, and the $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\varphi\:$$\end{document}`$ parameters are multiplicative scale parameters that shrink or amplify respondents’ slope coefficients based on their sex s and age group a $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$(a\:\in\:\left\{1-4\right\})$$\end{document}`$, which amounts to 8 scale parameters $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$(\:\varphi\:)$$\end{document}`$ per EQ-5D dimension. For statistical identification, the scale parameters were constrained to be positive and subject to a mean-of-one constraint.

Bayesian Markov Chain Monte Carlo (MCMC) methods were used to fit the models, which involves the selection of prior distributions for the unknown parameters and updating these via the likelihood of the observed data. Uninformative normal priors with a mean of zero and standard deviation of 10 were assigned to the $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\beta\:$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\gamma\:$$\end{document}`$ parameters and mean-to-one constrained log-normal parameters were assigned to the dimension-specific $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{\varphi\:}$$\end{document}`$ parameters. Similar to Jonker et al. \[12\], the standard deviation of the log-normal priors was set to 0.4 and the mean of the log-normal priors was defined as µ = -σ<sup>2</sup>/2 = -0.08 to ensure that the prior distribution had an expectation of 1. The models were implemented in the BUGS language and fitted using OpenBUGS \[13\]. A custom-implemented Metropolis-within-Gibbs algorithm with antithetic sampling was used to update the $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\beta\:$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\gamma\:$$\end{document}`$ parameters and a custom-implemented slice sampling algorithm was used to update the dimension-specific $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{\varphi\:}$$\end{document}`$ parameters subject to the mean-of-one constraints \[12\]. All reported estimates were based on 10,000 burn-in iterations to let three chains converge and a total of 30,000 MCMC iterations to reliably approximate the posterior distributions. Note that the model codes are included in the online supplemental and that convergence was evaluated based on a visual inspection of the MCMC chains and the convergence diagnostics as implemented in the OpenBUGS package.

During the Bayesian MCMC estimation, the original value sets were monitored by multiplying the $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\beta\:$$\end{document}`$ parameters with the corresponding $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{\varphi\:}$$\end{document}`$ scale parameters and then taking a weighted average using weights determined as the proportion of the population in the respective sex and age categories of the scale parameters at the time of the TTO data collection. Similarly, updated value sets were monitored by taking a weighted average of the original preference structure with weights determined by the countries’ most recent demographic composition. Finally, also the difference between the original and updated value sets was monitored during the model estimations. This allowed for a direct assessment of the impact of the change in countries’ age and gender compositions on the value sets.

## Results

The UK valuation dataset contained 3,395 respondents, 82 respondents who completed fewer than 10 TTO observations and 43 respondents with a positively sloped relationship between their TTO valuations and the misery indices of the health states were excluded, resulting in 3,270 respondents. The Japanese valuation dataset contained 543 respondents, 3 respondents who completed fewer than 10 TTO observations and 4 respondents with positive slopes were excluded, resulting in 536 respondents. And the United States valuation dataset contained 4,048 respondents, all of whom completed 10 or more TTO tasks and 133 respondents with positive slopes were excluded, resulting in 3,915 respondents.

Table <a href="#Tab1" data-ref-type="table">1</a> presents the demographic composition of the samples and compares them to the nationally representative benchmarks. None of the samples were accurately nationally representative at the time of the original data collection. This underscores the need to obtain regression-weighted value sets, both using the original and updated demographic weights. Also, in all three countries the population compositions have shifted and became significantly older in the last 2 decades; most prominently in Japan but also in the other 2 countries.

<div id="Tab1" class="table-wrap">

<div class="caption">

Survey respondents and national representative benchmarks, by country, sex, age group, and year

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;"></th>
<th rowspan="3" style="text-align: left;"></th>
<th colspan="14" style="text-align: left;">   Country</th>
</tr>
<tr>
<th colspan="4" style="text-align: left;">United Kingdom</th>
<th style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">Japan</th>
<th style="text-align: left;"></th>
<th colspan="4" style="text-align: left;">United States</th>
</tr>
<tr>
<th style="text-align: left;">Dataset</th>
<th colspan="3" style="text-align: left;">National population</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Dataset</th>
<th colspan="3" style="text-align: left;">National population</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">Dataset</th>
<th colspan="3" style="text-align: left;">National population</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Sex</td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">(<em>N</em> = 3,270)</td>
<td style="text-align: left;">1997</td>
<td style="text-align: left;">2022</td>
<td style="text-align: left;">Δ</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(<em>N</em> = 536)</td>
<td style="text-align: left;">1998</td>
<td style="text-align: left;">2022</td>
<td style="text-align: left;">Δ</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">(<em>N</em> = 3,915)</td>
<td style="text-align: left;">2002</td>
<td style="text-align: left;">2022</td>
<td style="text-align: left;">Δ</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">18–34</td>
<td style="text-align: left;">13.9%</td>
<td style="text-align: left;">15.6%</td>
<td style="text-align: left;">13.8%</td>
<td style="text-align: left;">-1.8%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">9.7%</td>
<td style="text-align: left;">15.2%</td>
<td style="text-align: left;">9.9%</td>
<td style="text-align: left;">-5.3%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">16.1%</td>
<td style="text-align: left;">16.2%</td>
<td style="text-align: left;">14.9%</td>
<td>-1.3%</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">35–54</td>
<td style="text-align: left;">13.9%</td>
<td style="text-align: left;">17.5%</td>
<td style="text-align: left;">16.0%</td>
<td style="text-align: left;">-1.5%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">15.5%</td>
<td style="text-align: left;">17.2%</td>
<td style="text-align: left;">15.9%</td>
<td style="text-align: left;">-1.3%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">16.5%</td>
<td style="text-align: left;">19.4%</td>
<td style="text-align: left;">16.3%</td>
<td>-3.1%</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">55–74</td>
<td style="text-align: left;">12.5%</td>
<td style="text-align: left;">11.5%</td>
<td style="text-align: left;">14.0%</td>
<td style="text-align: left;">2.5%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">15.5%</td>
<td style="text-align: left;">13.3%</td>
<td style="text-align: left;">14.8%</td>
<td style="text-align: left;">1.5%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">7.5%</td>
<td style="text-align: left;">10.1%</td>
<td style="text-align: left;">13.9%</td>
<td>3.8%</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">75+</td>
<td style="text-align: left;">3.1%</td>
<td style="text-align: left;">3.3%</td>
<td style="text-align: left;">5.1%</td>
<td style="text-align: left;">1.8%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1.3%</td>
<td style="text-align: left;">2.9%</td>
<td style="text-align: left;">7.6%</td>
<td style="text-align: left;">4.7%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.0%</td>
<td style="text-align: left;">2.9%</td>
<td style="text-align: left;">3.9%</td>
<td>1.0%</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">18–34</td>
<td style="text-align: left;">18.1%</td>
<td style="text-align: left;">15.7%</td>
<td style="text-align: left;">13.3%</td>
<td style="text-align: left;">-2.4%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">12.7%</td>
<td style="text-align: left;">14.5%</td>
<td style="text-align: left;">9.5%</td>
<td style="text-align: left;">-5.0%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">22.3%</td>
<td style="text-align: left;">15.7%</td>
<td style="text-align: left;">14.5%</td>
<td>-1.2%</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">35–54</td>
<td style="text-align: left;">16.9%</td>
<td style="text-align: left;">17.7%</td>
<td style="text-align: left;">16.4%</td>
<td style="text-align: left;">-1.3%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">25.6%</td>
<td style="text-align: left;">16.9%</td>
<td style="text-align: left;">15.4%</td>
<td style="text-align: left;">-1.5%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">22.2%</td>
<td style="text-align: left;">19.9%</td>
<td style="text-align: left;">16.2%</td>
<td>-3.7%</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">55–74</td>
<td style="text-align: left;">16.0%</td>
<td style="text-align: left;">12.7%</td>
<td style="text-align: left;">14.8%</td>
<td style="text-align: left;">2.1%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">17.7%</td>
<td style="text-align: left;">14.7%</td>
<td style="text-align: left;">15.5%</td>
<td style="text-align: left;">0.8%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">10.0%</td>
<td style="text-align: left;">11.0%</td>
<td style="text-align: left;">15.1%</td>
<td>4.1%</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">75+</td>
<td style="text-align: left;">5.6%</td>
<td style="text-align: left;">6.0%</td>
<td style="text-align: left;">6.6%</td>
<td style="text-align: left;">0.6%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.1%</td>
<td style="text-align: left;">5.3%</td>
<td style="text-align: left;">11.4%</td>
<td style="text-align: left;">6.1%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3%</td>
<td style="text-align: left;">4.8%</td>
<td style="text-align: left;">5.2%</td>
<td>0.4%</td>
</tr>
<tr>
<td style="text-align: left;">Total</td>
<td style="text-align: left;">18+</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;">100%</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

The Tobit regression coefficients are presented in the online supplemental. Briefly summarized, in all 3 countries all $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:\beta\:$$\end{document}`$ parameters and 2 or more $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\:{\gamma\:}$$\end{document}`$ parameters are statistically different from zero - in the sense that the 95% credible intervals do not comprise 0. Moreover, in all 3 countries there are sex and age group-specific scale parameters $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$(\:{\varphi\:})$$\end{document}`$ that are different from 1 – in the sense that the 95% credible intervals do not comprise 1. In the United Kingdom, all five EQ domains have scale parameters that are significantly different from 1. In the United States, all domains except for mobility are significantly different from 1, and in Japan, the pain and discomfort and anxiety and depression domains have scale parameters that are significantly different from 1.

The overall impact of the scale parameters and shifts in demographic compositions (i.e., differential preferences and associated weights) is summarized in Table <a href="#Tab2" data-ref-type="table">2</a>, which provides the original and updated value set decrements as well as their differences. As shown, the value sets themselves are country-specific but the differences between the original and updated value set decrements are close to identical. Most differences are 0.00 or smaller and the maximum difference is 0.01. Most importantly, all differences have 95% credible intervals that comprise 0, implying that the original and updated value sets are not significantly different.

<div id="Tab2" class="table-wrap">

<div class="caption">

EQ-5D health state decrements, original and age/sex corrected, by country

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">United Kingdom</th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">Japan</th>
<th style="text-align: left;"></th>
<th colspan="3" style="text-align: left;">United States</th>
</tr>
<tr>
<th style="text-align: left;">1997</th>
<th style="text-align: left;">2022</th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">1998</th>
<th style="text-align: left;">2022</th>
<th style="text-align: left;">Δ</th>
<th style="text-align: left;"></th>
<th style="text-align: left;">2002</th>
<th style="text-align: left;">2022</th>
<th style="text-align: left;">Δ</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MO2</td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.07 — -0.06)</p></td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.07 — -0.06)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.10</p>
<p>(-0.11 — -0.08)</p></td>
<td style="text-align: left;"><p>-0.10</p>
<p>(-0.11 — -0.08)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.04</p>
<p>(-0.04 — -0.03)</p></td>
<td style="text-align: left;"><p>-0.04</p>
<p>(-0.04 — -0.03)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">MO3</td>
<td style="text-align: left;"><p>-0.34</p>
<p>(-0.36 — -0.33)</p></td>
<td style="text-align: left;"><p>-0.34</p>
<p>(-0.36 — -0.33)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.43</p>
<p>(-0.46 — -0.4)</p></td>
<td style="text-align: left;"><p>-0.43</p>
<p>(-0.46 — -0.4)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(-0.01 — 0.01)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.34</p>
<p>(-0.35 — -0.32)</p></td>
<td style="text-align: left;"><p>-0.34</p>
<p>(-0.35 — -0.32)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">SC2</td>
<td style="text-align: left;"><p>-0.11</p>
<p>(-0.12 — -0.11)</p></td>
<td style="text-align: left;"><p>-0.12</p>
<p>(-0.12 — -0.11)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.01)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.05</p>
<p>(-0.07 — -0.04)</p></td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.07 — -0.04)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.07</p>
<p>(-0.08 — -0.07)</p></td>
<td style="text-align: left;"><p>-0.07</p>
<p>(-0.08 — -0.07)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">SC3</td>
<td style="text-align: left;"><p>-0.23</p>
<p>(-0.25 — -0.22)</p></td>
<td style="text-align: left;"><p>-0.24</p>
<p>(-0.26 — -0.23)</p></td>
<td style="text-align: left;"><p>0.01</p>
<p>(0.01 — 0.01)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.09</p>
<p>(-0.11 — -0.07)</p></td>
<td style="text-align: left;"><p>-0.09</p>
<p>(-0.12 — -0.07)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.01)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.24</p>
<p>(-0.25 — -0.23)</p></td>
<td style="text-align: left;"><p>-0.24</p>
<p>(-0.26 — -0.23)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">UA2</td>
<td style="text-align: left;"><p>-0.08</p>
<p>(-0.09 — -0.07)</p></td>
<td style="text-align: left;"><p>-0.08</p>
<p>(-0.09 — -0.07)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.03</p>
<p>(-0.05 — -0.02)</p></td>
<td style="text-align: left;"><p>-0.03</p>
<p>(-0.05 — -0.02)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.04</p>
<p>(-0.05 — -0.04)</p></td>
<td style="text-align: left;"><p>-0.04</p>
<p>(-0.05 — -0.04)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">UA3</td>
<td style="text-align: left;"><p>-0.22</p>
<p>(-0.23 — -0.21)</p></td>
<td style="text-align: left;"><p>-0.22</p>
<p>(-0.23 — -0.21)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.13</p>
<p>(-0.15 — -0.11)</p></td>
<td style="text-align: left;"><p>-0.12</p>
<p>(-0.15 — -0.1)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(-0.01 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.17</p>
<p>(-0.18 — -0.16)</p></td>
<td style="text-align: left;"><p>-0.18</p>
<p>(-0.19 — -0.16)</p></td>
<td style="text-align: left;"><p>0.01</p>
<p>(0.00 — 0.01)</p></td>
</tr>
<tr>
<td style="text-align: left;">PD2</td>
<td style="text-align: left;"><p>-0.09</p>
<p>(-0.09 — -0.08)</p></td>
<td style="text-align: left;"><p>-0.09</p>
<p>(-0.09 — -0.08)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.07 — -0.05)</p></td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.07 — -0.04)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.05</p>
<p>(-0.06 — -0.05)</p></td>
<td style="text-align: left;"><p>-0.05</p>
<p>(-0.06 — -0.04)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">PD3</td>
<td style="text-align: left;"><p>-0.47</p>
<p>(-0.48 — -0.45)</p></td>
<td style="text-align: left;"><p>-0.47</p>
<p>(-0.48 — -0.45)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.18</p>
<p>(-0.2 — -0.17)</p></td>
<td style="text-align: left;"><p>-0.17</p>
<p>(-0.19 — -0.16)</p></td>
<td style="text-align: left;"><p>-0.01</p>
<p>(-0.01 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.36</p>
<p>(-0.37 — -0.35)</p></td>
<td style="text-align: left;"><p>-0.36</p>
<p>(-0.37 — -0.35)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">AD2</td>
<td style="text-align: left;"><p>-0.12</p>
<p>(-0.13 — -0.11)</p></td>
<td style="text-align: left;"><p>-0.12</p>
<p>(-0.13 — -0.11)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.08 — -0.05)</p></td>
<td style="text-align: left;"><p>-0.06</p>
<p>(-0.08 — -0.05)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.08</p>
<p>(-0.09 — -0.07)</p></td>
<td style="text-align: left;"><p>-0.08</p>
<p>(-0.09 — -0.07)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
</tr>
<tr>
<td style="text-align: left;">AD3</td>
<td style="text-align: left;"><p>-0.37</p>
<p>(-0.38 — -0.35)</p></td>
<td style="text-align: left;"><p>-0.37</p>
<p>(-0.38 — -0.36)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.12</p>
<p>(-0.14 — -0.11)</p></td>
<td style="text-align: left;"><p>-0.12</p>
<p>(-0.14 — -0.1)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(-0.01 — 0.00)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>-0.26</p>
<p>(-0.27 — -0.25)</p></td>
<td style="text-align: left;"><p>-0.27</p>
<p>(-0.28 — -0.26)</p></td>
<td style="text-align: left;"><p>0.00</p>
<p>(0.00 — 0.01)</p></td>
</tr>
</tbody>
</table>

</div>

## Discussion

There are multiple reasons why value sets can become redundant and obsolete over time. For example, valuation methods have significantly improved in the past 2 decades, HTA bodies may require different value sets or methods to be used, and most importantly, population preferences can and likely have shifted over time. In this paper one aspect of value set obsolescence has been investigated, which is the extent to which demographic changes in the age/sex composition of populations have, keeping all other things constant, implicitly created an expiration date on preference-based value sets. Based on the presented results, we can conclude that demographic change is not an important determinant of value set validity.

Strengths of this study are that the results were obtained using the original TTO valuation data from 3 different countries from 3 different continents, a state-of-the-art Bayesian modelling approach, and a conceptually simple yet effective method to obtain both original and updated value sets. A potential weakness is that only age and gender were considered in the presented analyses; for example, the impact of ethnicity was ignored even though it could particularly for the United States have been an important determinant of value set obsolescence. Fortunately, according to the sensitivity analysis presented in the online supplemental, changes in the ethnic composition of the US population over the last two decades did not affect the validity of the US value set. Another potential weakness is that historic demographic trends may be smaller than future changes in populations’ age and sex compositions over time. However, the included countries experienced relatively large demographic shifts in the sex/age composition of their populations \[9\] and the demographic shifts as experienced over the past 20–25 years are equally large or larger than the predicted shifts in the age/sex distribution in the coming 20–25 years \[14\]. Accordingly, the preference differentials need to be at least an order of magnitude larger than those presented in this paper before demographic change would be able to significantly contribute to value set obsolescence. In other words, the presented results are robust, although contingent upon the assumption that the original preference structure as observed in the TTO datasets has remained constant over time. Future research is therefore necessary to establish the extent to which health-state preferences have indeed remained constant over time, as well as to determine appropriate criteria and threshold values for value set validity and obsolescence.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary Material 1

</div>

### Acknowledgements

The author would like to thank Claire Gudex, Aki Tsuchiya, and James Shaw for their permission to re-analyze the TTO data and gratefully acknowledges financial support from the EuroQol Research Foundation. The views expressed in this article do not necessarily reflect those of the EuroQol Group.

### Funding

This work was supported by a grant (EQ Project 1612-RA) from the EuroQol Research Foundation.

### Data availability

The UK valuation data are available at 10.5255/UKDA-SN-3444-1. The US valuation data are available at <https://archive.ahrq.gov/professionals/clinicians-providers/resources/rice/EQ5Dproj.html>. The Japanese valuation data are not publicly available. The demographic data can be obtained from <https://databank.worldbank.org/source/health-nutrition-and-population-statistics>.

### Declarations

#### Ethics statement

Permission to re-analyze the legacy valuation data was granted by the corresponding authors of the original publications. The UK and USA data are publicly available, while the Japanese data were obtained in anonymized form from the corresponding author.

#### Role of the funder/sponsor

The funder had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

#### Conflict of interest

Dr. Jonker reported being a member of the EuroQol Group. No other disclosures were reported.

## References

1. Kennedy-Martin, M., Slaap, B., Herdman, M., van Reenen, M., Kennedy-Martin, T., Greiner, W., Busschbach, J., & Boye, K. S. (2020). Which multi-attribute utility instruments are recommended for use in cost-utility analysis? A review of national health technology assessment (HTA) guidelines. The European Journal of Health Economics, 21, 1245–1257.32514643 10.1007/s10198-020-01195-8PMC7561556

2. National Institute for Health and Care Excellence (2022). NICE health technology evaluations: the manual. Process and methods [PMG36].

3. Pickard, A. S. (2015). Is it time to update societal value sets for preference-based measures of health? Pharmacoeconomics, 33(3), 191–192.25586758 10.1007/s40273-015-0253-3

4. Law, E. H., Pickard, A. S., Walton, S. M., Xie, F., Lee, T. A., & Schwartz, A. (2022). Time-Specific Differences in Stated Preferences for Health in the United States. Medical Care, 60(6), 462–469.35315380 10.1097/MLR.0000000000001714

5. Gudex, C., Dolan, P., Williams, A. H., & Kind, P. (1993). Health State Valuations from the British General Public [data collection]. UK Data Service. SN: 3444. 10.5255/UKDA-SN-3444-1

6. Dolan, P. (1997). Modeling valuations for EuroQol health states. Medical care. 1997 Nov 1:1095 – 108.10.1097/00005650-199711000-000029366889

7. Tsuchiya, A., Ikeda, S., Ikegami, N., Nishimura, S., Sakai, I., Fukuda, T., Hamashima, C., Hisashige, A., & Tamura, M. (2002). Estimating an EQ-5D population value set: The case of Japan. Health Economics, 11(4), 341–353.12007165 10.1002/hec.673

8. Shaw, J. W., Johnson, J. A., & Coons, S. J. (2005 Mar). US valuation of the EQ-5D health states: Development and testing of the D1 valuation model. Medical care, 1, 203–220.10.1097/00005650-200503000-0000315725977

9. World Bank Group Health nutrition and population statistics. https://databank.worldbank.org/source/health-nutrition-and-population-statistics Accessed 10/19/2023.

10. Rowen, D., Mukuria, C., & McDool, E. (2022). A systematic review of the methodologies and modelling approaches used to generate international EQ-5D-5L value sets. Pharmacoeconomics, 40(9), 863–882.35829931 10.1007/s40273-022-01159-1

11. Pickard, A. S., Law, E. H., Jiang, R., Pullenayegum, E., Shaw, J. W., Xie, F., Oppe, M., Boye, K. S., Chapman, R. H., Gong, C. L., & Balch, A. (2019). United States valuation of EQ-5D-5L health states using an international protocol. Value in Health, 22(8), 931–941.31426935 10.1016/j.jval.2019.02.009

12. Jonker, M. F., Donkers, B., de Bekker-Grob, E., & Stolk, E. A. (2019). Attribute level overlap (and color coding) can reduce task complexity, improve choice consistency, and decrease the dropout rate in discrete choice experiments. Health Economics, 28(3), 350–363.30565338 10.1002/hec.3846PMC6590347

13. Lunn, D., Jackson, C., Best, N., Thomas, A., & Spiegelhalter, D. (2012). The BUGS book: A practical introduction to Bayesian analysis. CRC press; Oct 2.

14. World Bank Group Population estimates and predictions. https://databank.worldbank.org/source/population-estimates-and-projections. Accessed 11/06/2023.

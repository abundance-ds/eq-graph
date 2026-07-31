---
project_id: "304-PHD"
work_id: "doi:10.1186/s12955-024-02271-w"
doi: "10.1186/s12955-024-02271-w"
pmid: "39003479"
pmcid: "PMC11555889"
title: "Scale and rate heterogeneity in the EQ-5D-5L valuation"
journal: "Health and Quality of Life Outcomes"
publication_date: "2024-07-13"
volume: "22"
authors:
  - name: "Maksat Jumamyradov"
    affiliation_ids:
      - "Aff1"
  - name: "Benjamin M. Craig"
    affiliation_ids:
      - "Aff1"
  - name: "Michał Jakubczyk"
    affiliation_ids:
      - "Aff2"
affiliations:
  - id: "Aff1"
    name: "https://ror.org/032db5x82grid.170693.a0000 0001 2353 285XDepartment of Economics, University of South Florida, Tampa, FL USA"
  - id: "Aff2"
    name: "https://ror.org/032cph770grid.426142.70000 0001 2097 5735Division of Decision Analysis and Support, SGH Warsaw School of Economics, Warsaw, Poland"
keywords:
  - "EQ-5D-5L"
  - "Health valuation"
  - "Scale and discount rate"
licence: "cc-by"
source_file: "input/projects/304-PHD/papers/doi_10.1186_s12955-024-02271-w.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11555889/fullTextXML"
source_method: "epmc_xml"
source_sha256: "59e62ecd0e11fd4edab1abe87f830fd33f578a81ac16790591ed370542118ba4"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Scale and rate heterogeneity in the EQ-5D-5L valuation

## Abstract

### Objectives

To estimate values on a quality-adjusted life year (QALY) scale using individual preference evidence, choice analyses typically include ancillary parameters, such as scale factors and discount rates. These parameters potentially differ among respondents. In this study, we investigated how allowing heterogeneity in scale and rate affects the estimation of EQ-5D-5L values.

### Methods

Using the first wave of the 2016 EQ-5D-5L valuation study (*N* = 1017), we estimated a conditional logit (CL) model and three mixed logit models: random scale, random rate, and bivariate. Prior to the exploratory study, we hypothesized that scale and rate are correlated and that allowing heterogeneity in both parameters decreases the number of insignificant incremental effects. We confirmed the exploratory findings by re-estimating these models using paired comparison responses from a second wave (*N* = 1229).

### Results

Scale and rate exhibited significant heterogeneity and were positively correlated. As hypothesized, allowing this heterogeneity improved the face validity of the EQ-5D-5L value set by reducing the number of insignificant incremental effects (from 6 to 2 *p*-values \> 0.05; out of 20). Nevertheless, the CL and bivariate mixed logit estimates are highly correlated and concordant (Pearson correlation coefficient of 0.897, Spearman correlation coefficient of 0.888, Lin’s concordance coefficient of 0.763).

### Conclusions

Allowing this heterogeneity adds three parameters to the estimation (two variances and a correlation) and improves the face validity of the EQ-5D-5L values. This finding may influence experimental design and choice analysis in health valuation more generally.

## Introduction

In health valuation, the purpose is to estimate preference weights for health outcomes that represent societal values on a quality-adjusted life-year (QALY) scale. On a QALY scale, “immediate death” has a value of 0, and “Starting today 1 year with no health problem then die” has a value of 1. Apart from these two anchors, choice analyses often include ancillary parameters, such as scale factors and discount rates. The primary aim of this paper is to investigate how allowing heterogeneity in scale and rate affects the estimation of EQ-5D-5L values.

In a logistic regression, the scale parameter defines the proportional relationship between the value of the initial QALY and a change in the log-odds of choice. A smaller (larger) scale parameter implies that a larger (smaller) difference in value is necessary to achieve the same change in log-odds of choice. In other words, the scale parameter is an inverse measure of the size of the random component. Varying the scale parameter between individuals implies that some respondents have different sensitivities to the value of the initial QALY \[1\]. The sources of this scale heterogeneity may be related to their behavior (e.g., attention span) or preferences (e.g., connoisseur) \[2\]. In health preference research more generally, scaling parameters are estimated in analyses of willingness-to-pay (i.e., monetary scaling) and maximum acceptable risk (MAR).

Apart from the scale parameter, the value of a health outcome depends on temporal discounting. Starting in the 1970s, researchers characterized the value of quality-adjusted life span by simply multiplying quality of life by length of life (i.e., no discounting). However, in the late 2010s, it was shown that discounting may be incorporated into health valuations \[3–5\]. Discounting is widely accepted in economics and finance; however, some outcome researchers express health-state utilities anchored on “dead” and “full health” and do not account for temporal discounting. In economic evaluations more generally, the marginal utility of time is decreasing (i.e., each additional day is worth less than the prior day), so incorporating discounting into health valuation enhanced its coherence with microeconomic theory \[6, 7\]. More recently, Karim and colleagues showed how the discount rate may vary within and between latent classes \[8\]. The sources of rate heterogeneity may be related to the respondents’ perceptions of death (e.g., nontraders) or their marginal decrease in utility of life years.

Prior to the exploratory analysis, we hypothesized that by allowing individual-level randomness in these two ancillary parameters, the estimates of the EQ-5D-5L value set might improve in terms of face validity. The EQ-5D-5L descriptive system has five ordinal domains, each representing increasing severity of health problems. Therefore, we assessed face validity by counting the number of insignificant incremental effects under alternative logit specifications estimated using a first survey wave. To complement this aim, we explored the variances and correlations of these parameters and their implications beyond health valuation.

As recommended by Craig, de Bekker-Grob, González Sepúlveda, and Greene, we confirmed the initial findings using a second wave \[9\]. The exploratory results led us to further hypothesize that scale and rate are positively correlated at the individual level. For example, the net present value (NPV) of the 10 QALYs depends on the discount rate, but the effect of NPV on the log-odds ratio depends on the scale parameter. Persons who discount heavily (lightly) may seem to be more (less) sensitive to differences in NPV, leading to a positive correlation. Analogously, a person who dislikes spicy foods may seem more sensitive to spice. Although this may now seem intuitive, to the best of our knowledge, no study has produced empirical evidence of this correlation.

The remainder of this paper is organized as follows. Section 2 describes the methods we used in this project, including the theoretical foundation, model specifications, exploratory (i.e., wave 1) and confirmatory (i.e., wave 2) data, and estimation techniques. In Sects. 3, 4 and 5, we provide the results, discussion and conclusions, respectively.

## Methods

### Random utility theory for paired comparisons

The theoretical framework of this choice analysis is based on random utility maximization (RUM) theory. According to RUM theory, the utility function $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${U}_{itj}={V}_{itj}+{\varepsilon }_{itj}$$\end{document}`$ of individual $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$i=1,\dots N$$\end{document}`$ for alternative $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$j=1,\dots ,J$$\end{document}`$ in choice situation $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$t=1,\dots T$$\end{document}`$ can be decomposed into a deterministic part of utility $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}$$\end{document}`$ (representative utility) and a random part of utility $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\varepsilon }_{itj}$$\end{document}`$. In paired comparison modeling \[10\], individual $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$i$$\end{document}`$ will choose an alternative $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$j$$\end{document}`$ if and only if the probability that the utility associated with alternative $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$j$$\end{document}`$ is higher than the utility of its alternative.

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
                \begin{document}$$\begin{array}{c}{P}_{itj}=P\left({U}_{itj}>{U}_{itk} \right), \forall \,k\ne j\\ {P}_{itj}=P\left({V}_{itj}+{\varepsilon }_{itj}>{V}_{itk}+{\varepsilon }_{itk}\right), \forall \,k\ne j\\ {P}_{itj}=P\left({\varepsilon }_{itk}-{\varepsilon }_{itj}<{V}_{itj}-{V}_{itk} \right), \forall \,k\ne j\end{array}$$\end{document}
```

</div>

Choice probabilities are calculated based on a relative measure where the utility of one of the alternatives in the choice set is taken as a reference. To derive the choice probabilities, we need to make distributional assumptions about the random part of utility. The conditional logit (CL) model is derived under the assumption that $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\varepsilon }_{itj}$$\end{document}`$ is independently and identically distributed (IID) with an extreme value type I (EV1) distribution \[11–13\]. As a result, the difference between two IID EV1 random error terms $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${(\varepsilon }_{itk}-{\varepsilon }_{itj})$$\end{document}`$ has a logistic distribution with scale parameter $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda$$\end{document}`$. This implies that the choice probabilities of the CL model can be expressed in terms of a logistic distribution with a cumulative distribution function

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
                \begin{document}$${{{P}}}_{{{i}}{{t}}{{j}}}=\frac{1}{1+\sum_{{{k}}=1}^{{{J}}}\text{exp}[{{\lambda}}({{{V}}}_{{{i}}{{t}}{{k}}}-{{{V}}}_{{{i}}{{t}}{{j}}})]},\boldsymbol{ }\forall \,\boldsymbol{ }{{k}}\ne {{j}}$$\end{document}
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
                \begin{document}$$\lambda$$\end{document}`$ is the scale parameter \[14\].

### Scale and rate heterogeneity in health valuation

For this study, we extended the CL model (Eq. <a href="#Equ2" data-ref-type="disp-formula">2</a>) for health valuation on a quality-adjusted life-year (QALY). By construction, the scale parameter is always positive, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda =\text{exp}(\mu )$$\end{document}`$, and represents the relationship between log-odds and the value of a health outcome $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}$$\end{document}`$ on a QALY scale. We specify the value of a health outcome $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}$$\end{document}`$ as a product of two values representing heath $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}^{H}$$\end{document}`$ and life years $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}^{Y}$$\end{document}`$:

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
                \begin{document}$${{{V}}}_{{{i}}{{t}}{{j}}}={{{V}}}_{{{i}}{{t}}{{j}}}^{{{H}}}\times {{{V}}}_{{{i}}{{t}}{{j}}}^{{{Y}}}$$\end{document}
```

</div>

In this paper, we assume that the value of health $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}^{H}=1-{\beta {'}x}_{itj}$$\end{document}`$, where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${x}_{itj}$$\end{document}`$ is a vector of 20 incremental indicators of health problems in mobility, self-care, usual activities, pain/discomfort and anxiety/depression (i.e., MO, SC, UA, PD, AD), and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\beta$$\end{document}`$ is a vector of preference weights on a QALY scale. Its homogeneity is a simplifying assumption for the estimation of a single EQ-5D-5L5L value set that may be relaxed in future work.

More specifically, the value of the health profiles is parameterized using 20 incremental effects (i.e., 5 attributes with 4 levels each), where each effect is caused by a dummy variable representing an incremental change in the level of severity of an EQ-5D-5L attribute. Therefore, we can write

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
                \begin{document}$${V}_{itj}^{H}=1-\left(\begin{array}{c}\begin{array}{c}{\beta }_{1}M{O}_{12}+{\beta }_{2}M{O}_{23}+{\beta }_{3}M{O}_{34}+{\beta }_{4}M{O}_{45}+\\ {\beta }_{5}S{C}_{12}+{\beta }_{6}S{C}_{23}+{\beta }_{7}S{C}_{34}+{\beta }_{8}S{C}_{45}+\\ {\beta }_{9}U{A}_{12}+{\beta }_{10}U{A}_{23}+{\beta }_{11}U{A}_{34}+{\beta }_{12}U{A}_{45}+\end{array}\\ {\beta }_{13}P{D}_{12}+{\beta }_{14}P{D}_{23}+{\beta }_{15}P{D}_{34}+{\beta }_{16}P{D}_{45}+\\ {\beta }_{17}A{D}_{12}+{\beta }_{18}A{D}_{23}+{\beta }_{19}A{D}_{34}+{\beta }_{20}A{D}_{45}\end{array}\right)$$\end{document}
```

</div>

As a criterion of face validity, all 20 incremental effects in vector $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\beta$$\end{document}`$ should be positive since they represent losses in value due to increases in the level of severity of a health condition from the full health profile \[14\].

For the value of life years $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}^{Y}$$\end{document}`$, the identity function is commonly assumed to be $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}^{Y}={Y}_{itj}$$\end{document}`$, where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${Y}_{itj}$$\end{document}`$ represents life years (i.e., no discounting). However, this functional form does not accurately represent the time preferences of the general population \[4, 5\]. Individuals usually discount over time; i.e., future outcomes affect choices less than present outcomes. To allow for temporal discounting, we adapt the power function (see <a href="#Equ4" data-ref-type="disp-formula">4</a>)
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
                \begin{document}$${V}_{itj}^{Y}={Y}_{itj}^{{\alpha }_{i}}$$\end{document}
```
where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}$$\end{document}`$ is the individual-specific power. On a QALY scale, the value of time $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${V}_{itj}^{Y}$$\end{document}`$ equals 1 when $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${Y}_{itj}$$\end{document}`$ equals 1, regardless of the power $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}$$\end{document}`$, and the identity function (i.e., no discounting) implies that the power is unity, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}=1$$\end{document}`$.

Apart from restricting the individual-specific scale parameter to be positive, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\lambda }_{i}=\text{exp}({\mu }_{i})$$\end{document}`$, we restricted the power $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}$$\end{document}`$ to the unit interval, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$0\le {\alpha }_{i}\le 1$$\end{document}`$. More specifically, we transform the power into a discount rate using the complementary log–log (CLL) function, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}=\text{exp}(-\text{exp}\left({r}_{i}\right))$$\end{document}`$ which is naturally bounded to the unit interval. At first glance, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ has an inverse relationship with $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}$$\end{document}`$, and a lower $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}$$\end{document}`$ implies greater discounting of life years; therefore, a higher rate $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ implies greater discounting. Future analyses may allow for negative discounting or alternative functional forms \[15–17\].

### The bivariate distribution of the scale and rate among respondents

Due to limited panel evidence per respondent, it is not feasible to estimate individual-specific scales and rates as fixed effects (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$). Instead, we estimated a conditional logit (CL) model and three mixed logit models. First, we estimated the CL model under homogeneity $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$({\mu }_{i}=\mu ; {r}_{i}=r)$$\end{document}`$. Under this specification, all respondents have the same scale parameter and discount rate. In the second and third specifications, we estimated the mixed logit models with random scale and random rate, respectively. We refer to these two mixed logit specifications as “univariate” models because each contains only one normally distributed random parameter.

Finally, in the fourth specification, we estimated a bivariate mixed logit model, including the mean and standard deviation of $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\sigma }_{\mu }$$\end{document}`$, respectively) and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$r$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\sigma }_{r}$$\end{document}`$, respectively), as well as their correlation. The ancillary parameters vary under a bivariate normal distribution and may be correlated. We assume that $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ are normally distributed such that $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\left({\mu }_{i},{r}_{i}\right)\sim N({\sigma }_{\mu }^{2},\rho ,{\sigma }_{r}^{2})$$\end{document}`$ where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\sigma }_{\mu }^{2}=Var({\mu }_{i})$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\sigma }_{r}^{2}=Var({r}_{i})$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\rho =Corr({\mu }_{i},{r}_{i})$$\end{document}`$.

To shed more light on this potential bias, we express the individual-specific ancillary component, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\lambda }_{i}{V}_{itj}^{Y}$$\end{document}`$ (apart from the value of health), as an exponential regression with two ancillary parameters (an intercept $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and a coefficient $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i})$$\end{document}`$, where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${Y}_{itj}>0:$$\end{document}`$
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
                \begin{document}$${\lambda }_{i}{V}_{\mathit{itj}}^{Y}=\text{exp}\left({\mu }_{i}\right){Y}_{itj}^{{\alpha }_{i}}=\text{exp}\left({\mu }_{i}+{\alpha }_{i}ln\left({Y}_{itj}\right)\right)$$\end{document}
```

In this study, life years $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${Y}_{itj}$$\end{document}`$ range from 1 to 10 years; therefore, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$ln\left({Y}_{itj}\right)$$\end{document}`$ ranges from zero to 2.303. Given that $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$ln\left({Y}_{itj}\right)$$\end{document}`$ is always positive, the ancillary component can increase through either ancillary parameter ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ or $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\alpha }_{i}$$\end{document}`$). In econometric terms, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$ln\left({Y}_{itj}\right)$$\end{document}`$ is an instrumental variable needed to identify the two ancillary parameters.

### Data

In 2016, 8,222 U.S. respondents (4074 in wave 1 and 4148 in wave 2) from all 50 states and Washington, D.C., completed an online survey that included 20 paired comparisons. The design of the paired comparisons was largely based on the EuroQol Valuation Technology (EQ-VT v1.0) protocols \[18\]. An example of the paired comparison conducted in the study is illustrated in Fig. <a href="#Fig1" data-ref-type="fig">1</a>. In this paper, we provide a general overview of the study. More details can be found in other studies \[3, 19\].

<figure id="Fig1">
<p><img src="12955_2024_2271_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Example of a paired comparison</figcaption>
</figure>

Each paired comparison is presented as a variation of health descriptions based on the EQ-5D-5L. The five dimensions (i.e., attributes) of the EQ-5D-5L are mobility, self-care, usual activities, pain/discomfort and anxiety/depression, where each dimension is characterized by five levels ranging from no problems (i.e., level 1) to slight, moderate, severe, and unable/extreme problems (i.e., level 5). For instance, the health description on the right side of Fig. <a href="#Fig1" data-ref-type="fig">1</a> can be represented as a vector of five numbers 33333 since all five dimensions are at a moderate level. For each comparison, respondents were asked, “Which do you prefer?” regarding a pair of alternatives described using the EQ-5D-5L and lifespan attributes.

The online survey consisted of 3160 pairs, 1600 of which are efficient (or “quality only”) pairs and 1560 of which are quantity-quality pairs. In efficient pairs, both health descriptions consisted of varying levels of health problems with the same life years (e.g., 12345 vs 54321). In the quantity-quality pairs, one of the health descriptions involves no health problems (i.e., 11111). Furthermore, 80 out of 1560 quantity-quality pairs included “immediate death”, which represents “dead” pairs, as one of the alternatives. The data were collected in two parts: an exploratory survey consisting of 1560 pairs and a confirmatory survey consisting of 1600 pairs. The survey data were collected at four temporal units (i.e., days, weeks, months, and years). This analysis included only the pairs with year units (1017 respondents in wave 1 and 1229 in wave 2) because the other pairs did not describe events after 1 year (i.e., discounting).

With the diversity of pairs, it is mathematically feasible to identify the scale and rate separately using either wave of this dataset. Imagine a paired comparison with identical lifespans. These pairs may identify differential scales within a population, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$. Imagine a paired comparison with differential life years. These pairs may identify differential scales, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and rates, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$. Apart from its pair types, this dataset is one of the largest national health valuation studies ever conducted \[3\], has both exploratory and confirmatory waves, and applied quota sampling at the pair level to assure that each pair had a minimum number of respondents along 18 demographic quotas.

### Mixed logit and maximum simulated likelihood

To estimate the mixed logit models, the maximum likelihood (ML) estimator of parameter vector $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\theta$$\end{document}`$ can be utilized when the density of dependent variable $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${y}_{i}$$\end{document}`$ conditional on a vector of independent variables $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${x}_{i}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$f({y}_{i}|{x}_{i},\theta )$$\end{document}`$, has a closed-form such that
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
                \begin{document}$${\widehat{\theta }}_{N}=\text{arg}\underset{\uptheta }{\text{max}}{\sum }_{i=1}^{N}\text{log}f({y}_{i}|{x}_{i},\theta )$$\end{document}
```
where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$i=1,\dots ,N$$\end{document}`$. However, ML is not feasible when $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$f({y}_{i}|{x}_{i},\theta )$$\end{document}`$ does not have a tractable closed-form. This can be because the density is specified only conditional on latent variables, which cannot be integrated out. Thus, the MSL estimator is a possible alternative \[20, 21\]. Suppose $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\widetilde{f}({y}_{i},{x}_{i},{u}_{i},\theta )$$\end{document}`$ is an unbiased simulator of the conditional density $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$f({y}_{i}|{x}_{i},\theta )$$\end{document}`$ such that
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
                \begin{document}$$f\left({y}_{i}|{x}_{i},\theta \right)={\text{E}}_{\text{u}}[\widetilde{f}({y}_{i},{x}_{i},{u}_{i},\theta )|{y}_{i},{x}_{i}]$$\end{document}
```
where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${u}_{i}$$\end{document}`$ is an individual-specific latent vector ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$) whose distribution is known and independent of $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$({y}_{i},{x}_{i})$$\end{document}`$. Then, the MSL estimator of $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\theta$$\end{document}`$ is defined as
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
                \begin{document}$${\widehat{\theta }}_{SN}=\text{arg}\underset{\uptheta }{\text{max}}\sum\limits_{i=1}^{N}\text{log}\left[\frac{1}{s}\sum\limits_{s=1}^{S}\widetilde{f}({y}_{i},{x}_{i},{u}_{i}^{s},\theta )\right]$$\end{document}
```
where $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${u}_{i}^{s}(s=1,\dots ,S)$$\end{document}`$ are drawn independently for each individual $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$i$$\end{document}`$ from the distribution of $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${u}_{i}$$\end{document}`$. The MSL estimator is obtained by replacing the intractable conditional p.d.f. $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$f({y}_{i}|{x}_{i},\theta )$$\end{document}`$ with its unbiased approximation based on the simulator $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\widetilde{f}({y}_{i},{x}_{i},{u}_{i}^{s},\theta )$$\end{document}`$. In this study, we estimate the mean and variance of each random parameter as well as their *p*-values \[3\].

In our MSL estimations of the three specifications of the mixed logit model, we use 250 Halton draws (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S=250$$\end{document}`$) \[22\]. We used the MATLAB programming language for all estimations. More specifically, we began by estimating the CL comparator and three specifications using the wave 1 data, which helped us state our hypotheses more clearly. Afterwards, we re-estimated the models and tested these hypotheses using the wave 2 data. Furthermore, we compare the results between waves and models to assess how allowing heterogeneity in scale and rate affects the estimation of EQ-5D-5L values.

## Results

In this section, we present the results for CL and mixed logit estimation using waves 1 and 2 separately. In Table <a href="#Tab1" data-ref-type="table">1</a>, we compare the CL estimates with the mixed logit estimates where we allow correlations between $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$. In Table 1A (<a href="#Sec13" data-ref-type="sec">Appendix</a>), we present the univariate results for the mixed logit estimation with random scale and random rate separately.

<div id="Tab1" class="table-wrap">

<div class="caption">

Results for conditional and bivariate mixed logit models

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Conditional Logit</th>
<th colspan="2" style="text-align: left;">Bivariate Mixed Logit</th>
</tr>
<tr>
<th style="text-align: left;"><em>N</em> = 1017 &amp; 1229</th>
<th style="text-align: left;">Exploratory</th>
<th style="text-align: left;">Confirmatory</th>
<th style="text-align: left;">Exploratory</th>
<th style="text-align: left;">Confirmatory</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$M{O}_{12}$$\end{document}$</span></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.044<sup>b</sup></td>
<td style="text-align: left;">0.014<sup>a</sup></td>
<td style="text-align: left;">0.033<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$M{O}_{23}$$\end{document}$</span></td>
<td style="text-align: left;">0.044<sup>b</sup></td>
<td style="text-align: left;">0.050<sup>b</sup></td>
<td style="text-align: left;">0.044<sup>b</sup></td>
<td style="text-align: left;">0.064<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$M{O}_{34}$$\end{document}$</span></td>
<td style="text-align: left;">0.141<sup>b</sup></td>
<td style="text-align: left;">0.142<sup>b</sup></td>
<td style="text-align: left;">0.110<sup>b</sup></td>
<td style="text-align: left;">0.084<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$M{O}_{45}$$\end{document}$</span></td>
<td style="text-align: left;">0.117<sup>b</sup></td>
<td style="text-align: left;">0.122<sup>b</sup></td>
<td style="text-align: left;">0.069<sup>b</sup></td>
<td style="text-align: left;">0.034<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S{C}_{12}$$\end{document}$</span></td>
<td style="text-align: left;">0.027<sup>a</sup></td>
<td style="text-align: left;">0.095<sup>b</sup></td>
<td style="text-align: left;">0.025<sup>b</sup></td>
<td style="text-align: left;">0.087<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S{C}_{23}$$\end{document}$</span></td>
<td style="text-align: left;">0.038<sup>b</sup></td>
<td style="text-align: left;">0.016</td>
<td style="text-align: left;">0.025<sup>b</sup></td>
<td style="text-align: left;">0.045<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S{C}_{34}$$\end{document}$</span></td>
<td style="text-align: left;">0.151<sup>b</sup></td>
<td style="text-align: left;">0.110<sup>b</sup></td>
<td style="text-align: left;">0.108<sup>b</sup></td>
<td style="text-align: left;">0.062<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S{C}_{45}$$\end{document}$</span></td>
<td style="text-align: left;">0.153<sup>b</sup></td>
<td style="text-align: left;">0.147<sup>b</sup></td>
<td style="text-align: left;">0.098<sup>b</sup></td>
<td style="text-align: left;">0.090<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{12}$$\end{document}$</span></td>
<td style="text-align: left;">0.024<sup>a</sup></td>
<td style="text-align: left;">0.018</td>
<td style="text-align: left;">0.015<sup>a</sup></td>
<td style="text-align: left;">0.022<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{23}$$\end{document}$</span></td>
<td style="text-align: left;">0.027<sup>b</sup></td>
<td style="text-align: left;">0.011</td>
<td style="text-align: left;">0.024<sup>b</sup></td>
<td style="text-align: left;">0.027<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{34}$$\end{document}$</span></td>
<td style="text-align: left;">0.144<sup>b</sup></td>
<td style="text-align: left;">0.173<sup>b</sup></td>
<td style="text-align: left;">0.119<sup>b</sup></td>
<td style="text-align: left;">0.131<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{45}$$\end{document}$</span></td>
<td style="text-align: left;">0.030</td>
<td style="text-align: left;">0.099<sup>b</sup></td>
<td style="text-align: left;">0.027<sup>b</sup></td>
<td style="text-align: left;">0.056<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}$</span></td>
<td style="text-align: left;">-0.002</td>
<td style="text-align: left;">-0.016</td>
<td style="text-align: left;">0.021<sup>b</sup></td>
<td style="text-align: left;">-0.006</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{23}$$\end{document}$</span></td>
<td style="text-align: left;">0.047<sup>b</sup></td>
<td style="text-align: left;">0.050<sup>b</sup></td>
<td style="text-align: left;">0.034<sup>b</sup></td>
<td style="text-align: left;">0.061<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{34}$$\end{document}$</span></td>
<td style="text-align: left;">0.225<sup>b</sup></td>
<td style="text-align: left;">0.215<sup>b</sup></td>
<td style="text-align: left;">0.161<sup>b</sup></td>
<td style="text-align: left;">0.153<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{45}$$\end{document}$</span></td>
<td style="text-align: left;">0.096<sup>b</sup></td>
<td style="text-align: left;">0.092<sup>b</sup></td>
<td style="text-align: left;">0.048<sup>b</sup></td>
<td style="text-align: left;">0.048<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{12}$$\end{document}$</span></td>
<td style="text-align: left;">0.020</td>
<td style="text-align: left;">-0.022</td>
<td style="text-align: left;">0.035<sup>b</sup></td>
<td style="text-align: left;">0.023<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{23}$$\end{document}$</span></td>
<td style="text-align: left;">0.100<sup>b</sup></td>
<td style="text-align: left;">0.046<sup>b</sup></td>
<td style="text-align: left;">0.058<sup>b</sup></td>
<td style="text-align: left;">0.045<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{34}$$\end{document}$</span></td>
<td style="text-align: left;">0.163<sup>b</sup></td>
<td style="text-align: left;">0.168<sup>b</sup></td>
<td style="text-align: left;">0.123<sup>b</sup></td>
<td style="text-align: left;">0.130<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{45}$$\end{document}$</span></td>
<td style="text-align: left;">0.033<sup>b</sup></td>
<td style="text-align: left;">-0.016</td>
<td style="text-align: left;">0.021<sup>a</sup></td>
<td style="text-align: left;">0.000</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu (mean)$$\end{document}$</span></td>
<td style="text-align: left;">0.401<sup>b</sup></td>
<td style="text-align: left;">0.062</td>
<td style="text-align: left;">0.988<sup>b</sup></td>
<td style="text-align: left;">0.704<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$r (mean)$$\end{document}$</span></td>
<td style="text-align: left;">-0.196<sup>b</sup></td>
<td style="text-align: left;">-0.634<sup>b</sup></td>
<td style="text-align: left;">-0.003</td>
<td style="text-align: left;">-2.051<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu (SD)$$\end{document}$</span></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.788<sup>b</sup></td>
<td style="text-align: left;">0.998<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$r (SD)$$\end{document}$</span></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.858<sup>b</sup></td>
<td style="text-align: left;">3.120<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu$$\end{document}$</span> and <span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$r$$\end{document}$</span> (corr)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.836<sup>b</sup></td>
<td style="text-align: left;">0.912<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$V(55555)$$\end{document}$</span></td>
<td style="text-align: left;">-0.588<sup>b</sup></td>
<td style="text-align: left;">-0.545<sup>b</sup></td>
<td style="text-align: left;">-0.180<sup>b</sup></td>
<td style="text-align: left;">-0.191<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">$\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$LL$$\end{document}$</span></td>
<td style="text-align: left;">-12,225</td>
<td style="text-align: left;">-14,278</td>
<td style="text-align: left;">-10,249</td>
<td style="text-align: left;">-11,890</td>
</tr>
</tbody>
</table>

Notice that the scale parameter is equal to $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda =\text{exp}(\mu )$$\end{document}`$, and the power is equal to $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\alpha =\text{exp}(-\text{exp}(r))$$\end{document}`$ to bound the power between 0 and 1

<sup>a</sup>, <sup>b</sup>represent significance levels at the 5% and 1%, respectively

</div>

### Exploratory results

As shown in Table <a href="#Tab1" data-ref-type="table">1</a>, the exploratory CL results produce three insignificant positive effects (*p*-value \< 0.01; $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$M{O}_{12}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{45}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${AD}_{12}$$\end{document}`$) and one insignificant negative effect for $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}`$. There are also two additional effects with p-values between 1 and 5% (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S{C}_{12}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{12}$$\end{document}`$). Furthermore, the CL results suggest that “immediate death” is better than experiencing the worst possible EQ-5D-5L description for 1 year (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$V\left(55555\right)=-0.588$$\end{document}`$). Since the estimated $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu$$\end{document}`$ is 0.401, the scale parameter in the CL model is $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda =\text{exp}\left(0.401\right)=1.493$$\end{document}`$. Similarly, since the estimated $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$r$$\end{document}`$ is $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$-0.196$$\end{document}`$, the power $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\alpha$$\end{document}`$ in the CL model is $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\text{exp}\left(-\text{exp}\left(-0.196\right)\right)=0.439$$\end{document}`$.

In Table A1 (<a href="#Sec13" data-ref-type="sec">Appendix</a>), we present the univariate results where we allow for random scale and random rate separately. The standard deviations of $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ are 1.232 and 1.325, respectively, suggesting that scale and rate heterogeneity exist. However, the random scale model has insignificant effect (5 with *p*-value \> 0.05), i.e., one more than the CL model, while the random rate model has same number of insignificant effects (4 with *p*-value \> 0.05). In the exploratory results, allowing for one random parameter increases the log-likelihood, but had little impact on the significance of the effects.

When we allow for heterogeneity in both ancillary parameters (Table <a href="#Tab1" data-ref-type="table">1</a>), there are substantive improvements in the estimated incremental effects. In the bivariate mixed logit results, all 20 effects are positive and significant. The estimated standard deviations for $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ are 0.788 and 2.858, respectively, which suggest that both the scale and rate parameters are heterogeneous. Furthermore, we find a strong correlation between $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$, 0.836 (*p*-value \< 0.01).

In the bivariate mixed logit model, “immediate death” is better than experiencing the worst possible EQ-5D-5L description for 1 year (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$V\left(55555\right)=-0.180$$\end{document}`$); however, this value is closer to zero compared to the CL estimate. Apart from this difference in the lower bound, the twenty incremental effects are highly correlated and concordant between the CL and bivariate mixed logit estimates (Pearson correlation 0.970, Spearman correlation 0.916, Lin’s concordance 0.843). Furthermore, we computed the mean scale and power of the bivariate mixed logit as $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda =\text{exp}\left(0.988\right)=2.686$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\alpha =\text{exp}\left(-\text{exp}\left(-0.003\right)\right)=0.369$$\end{document}`$. Therefore, the bivariate mixed logit model produce higher scale and lower power than the CL model.

### Confirmatory results

The confirmatory CL results produce 6 insignificant incremental effects (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$S{C}_{23}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{12}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$U{A}_{23}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{12}$$\end{document}`$, and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{45}$$\end{document}`$), 3 of which are negative (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}`$, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{12}$$\end{document}`$, and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{45}$$\end{document}`$). Compared to the exploratory CL results, there are the same number of positive insignificant effects and 2 more negative effects. The confirmatory CL results suggest that the value of “immediate death” is better than experiencing the worst possible EQ-5D-5L description for 1 year (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$V\left(55555\right)=-0.545$$\end{document}`$), which is slightly lower than the exploratory CL estimate ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$0.588$$\end{document}`$). The estimated $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$r$$\end{document}`$ in the confirmatory CL are 0.062 and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$-0.634$$\end{document}`$, respectively. Therefore, the scale and power can be derived as $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda =\text{exp}\left(0.062\right)=1.064$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\alpha =\text{exp}\left(-\text{exp}\left(-0.634\right)\right)=0.588$$\end{document}`$. Compared to the confirmatory CL results, the exploratory scale is larger ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$1.493$$\end{document}`$), but its power is smaller ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$0.439$$\end{document}`$).

When we allow for heterogeneity in scale and rate in the confirmatory analysis, there are substantive improvements in the estimated incremental effects. Specifically, in the bivariate mixed logit results, there is only 1 negative (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}`$) and 1 positive (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{45}$$\end{document}`$) insignificant incremental effect. We computed the scale and power of the bivariate mixed logit model as $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\lambda =\text{exp}\left(0.704\right)=2.022$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\alpha =\text{exp}\left(-\text{exp}\left(-2.051\right)\right)=0.879$$\end{document}`$, respectively, which are higher than those of the CL model. The estimated standard deviations for $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ are 0.998 and 3.120, respectively, which suggests that both the scale and rate parameters are heterogeneous. Furthermore, we find a strong correlation between $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${\mu }_{i}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$, 0.912 (*p*-value \< 0.01).

In the bivariate mixed logit model, “immediate death” is better than experiencing the worst possible EQ-5D-5L description for 1 year (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$V\left(55555\right)=-0.191$$\end{document}`$); however, this value is closer to zero compared to the CL estimate ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$-0.545$$\end{document}`$). Apart from this difference in the lower bound, the twenty incremental effects are highly correlated and concordant between the CL and bivariate mixed logit estimates (Pearson correlation 0.897, Spearman correlation 0.888, Lin’s concordance 0.763).

## Discussion

In this paper, we explored and confirmed heterogeneity in scale and rate, their correlation, and their effects on the estimation of EQ-5D-5L values. Allowing heterogeneity in scale and rate improved the EQ-5D-5L value set estimates in terms of face validity, namely, reducing the number of insignificant incremental effects.

A higher discount rate $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}$$\end{document}`$ implies that there is less variability in the net present value of life years. For instance, with a high discount rate, the value of 10 years decreases toward the value of 1 year. A higher scale implies that smaller differences in the value of health have a greater impact on log-odds. In other words, a larger scale parameter means more sensitivity. Since our results suggest that there is a high positive correlation between the scale parameter and the discount rate, we can infer that people who discount the future are more sensitive to smaller differences in the net present value of life years. This important finding may be confirmed in future health valuation studies.

In practical terms, allowing for scale heterogeneity implies that the analyst should also allow for rate heterogeneity (or vice versa) as well as estimate the correlation between scale and rate. However, no econometric package is currently available to facilitate this specification of the mixed logit, which may deter its uptake. In terms of the experimental design and blocking, future studies may assign “dying immediately,” episodes of one-year duration, and multi-year episodes to each respondent. This blocking can aid in the identification of scale and rate heterogeneity. If future studies block accordingly and such a package becomes available, reporting this correlation may become common practice in health valuation.

Although the twenty incremental effects are highly correlated and concordant between the CL and bivariate mixed logit estimates, controlling for scale and rate heterogeneity, reduced the size of the incremental effects, raising the lower bound of the EQ-5D-5L values from -0.545 to -0.191. Although some effects decreased in size, the confirmatory bivariate estimation produced only two insignificant effects ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}`$ and $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{45}$$\end{document}`$), which merits further discussion. The incremental effect $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$P{D}_{12}$$\end{document}`$ represents the effect of the change from no to slight pain or discomfort. This effect is negative and insignificant in both the conditional logit models as well as the confirmatory bivariate mixed logit, which seems to suggest that U.S. adults are unwilling to sacrifice life years to relieve slight pain or discomfort. Further research is needed to verify this effect. The incremental effect $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$A{D}_{45}$$\end{document}`$ represents the effect of the change from severely to extremely anxious or depressed. In two prior papers, Craig and colleagues \[23, 24\] showed that many U.S. adults prefer “extremely” over “severely” in this domain. This preference inversion contradicts the descriptive system and may be due to the diagnostic implications of severe mental health problems and/or the belief that moods may fluctuate between extrema under normal circumstances. The higher lower bound and two insignificant effects may accurately represent the EQ-5D-5L preferences of U.S. adults.

Although the incremental effects of the bivariate mixed logit model appear to be better in terms of sign and significance, they are highly correlated with the CL estimates (Pearson correlation 0.897, Spearman correlation 0.888, Lin’s concordance 0.763). Figure <a href="#Fig2" data-ref-type="fig">2</a> shows the 20 incremental effects from the confirmatory CL and bivariate mixed logit, where incremental effects are color-coded by dimension (i.e., MO: red, SC: green; UA: blue, PD: yellow, AD: black). The differences between the estimates seem to be larger among the more severe effects (from level 3 to 4 or from level 4 to 5).

<figure id="Fig2">
<p><img src="12955_2024_2271_Fig2_HTML.jpg" id="MO2" /></p>
<figcaption>Plot of 20 incremental effects for the conditional logit and bivariate mixed logit</figcaption>
</figure>

Alternatively, some analysts may choose to use a hyperbolic discount function instead of a power function to allow for temporal discounting. Craig and colleagues \[4\] showed that decreasing the marginal value of life span under the assumption of power discounting provides better model fit than alternative functional forms. While Craig and colleagues \[4\] assumed a homogeneous discount rate (i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$${r}_{i}=r$$\end{document}`$), Jonker and colleagues \[5\] estimated the mixed logit model with a random hyperbolic discount rate and found strong evidence for non-linear time preferences. In this study, we extended both approaches and estimated a bivariate mixed logit model allowing a correlation between scale and power.

Future analyses may allow for heterogeneity in the incremental effects as well as scale and discount rate parameters, building from these findings. Before the estimation of such a complex model is attempted, we recommend that the authors conduct simulation analyses to verify that they can mitigate the simulation biases. For instance, Jumamyradov and colleagues conducted a simulation study and showed that the mixed logit model can produce biased results even when the model is correctly specified \[25\]. Nevertheless, we believe that our more parsimonious specification produced reliable results since we found a high correlation both in exploratory and confirmatory datasets.

There are three limitations in our analysis that we would like to mention. First, our mixed logit analysis is based on MSL estimation. This may be problematic for the bivariate specification because Jumamyradov and colleagues \[25\] showed that the MSL estimator of the mixed logit has difficulty estimating correlations and may produce biased estimates even when correctly specified. Second, we assume only normally distributed random parameters and may consider other distributional assumptions in future research. Third, because of computational capacity constraints, we used only 250 Halton draws in our estimations, which is common place in the literature \[22\]. Some \[26\] have shown that increasing the number of Halton draws decreases the simulation bias for bivariate normal and bivariate Poisson-lognormal models.

Our study utilized EQ-5D-5L values from a United States-specific valuation study. While the data source was specific to the U.S., the underlying principles and results of this study are not confined to the U.S. context alone. The methodological approach and findings presented are designed to be broadly applicable and are likely to be generalizable to other settings. Similar methodologies can be applied to different populations and healthcare systems, reinforcing the validity of our approach across diverse settings.

We also would like to point that we acknowledge that the scale heterogeneity is a form of correlation among coefficients in mixed logit models \[27, 28\]. However, this is not relevant in our study since we are focusing on the correlation between the scale parameter and the discount rate.

## Conclusion

Allowing heterogeneity in rate and scale added three parameters to the conditional logit model (two variances and a correlation) and greatly improved the face validity of the EQ-5D-5L values. We confirmed that persons who highly discount the future are more sensitive to differences in the net present value of QALYs. This intuitive pattern may be confirmed in future EQ-5D-5L valuation studies as well as influence experimental design and choice analysis in health preference research more generally.

##### Appendix

<div id="Taba" class="table-wrap">

<div class="caption">

**Table 1A**. Results for univariate mixed logit models

</div>

|  | Random scale |  | Random rate |  |
|----|----|----|----|----|
| *N* = 1017 & 1229 | Exploratory | Confirmatory | Exploratory | Confirmatory |
| *MO*<sub>12</sub> | -0.012 | 0.019<sup>b</sup> | 0.003 | 0.025<sup>b</sup> |
| *MO*<sub>23</sub> | 0.049<sup>b</sup> | 0.076<sup>b</sup> | 0.045<sup>b</sup> | 0.064<sup>b</sup> |
| *MO*<sub>34</sub> | 0.087<sup>b</sup> | 0.093<sup>b</sup> | 0.103<sup>b</sup> | 0.082<sup>b</sup> |
| *MO*<sub>45</sub> | 0.104<sup>b</sup> | 0.054<sup>b</sup> | 0.049<sup>b</sup> | 0.028<sup>a</sup> |
| *SC*<sub>12</sub> | 0.016 | 0.057<sup>b</sup> | 0.022<sup>b</sup> | 0.097<sup>b</sup> |
| *SC*<sub>23</sub> | 0.023<sup>a</sup> | 0.027<sup>b</sup> | 0.020<sup>b</sup> | 0.025<sup>b</sup> |
| *SC*<sub>34</sub> | 0.130<sup>b</sup> | 0.081<sup>b</sup> | 0.101<sup>b</sup> | 0.073<sup>b</sup> |
| *SC*<sub>45</sub> | 0.082<sup>b</sup> | 0.109<sup>b</sup> | 0.089<sup>b</sup> | 0.083<sup>b</sup> |
| *UA*<sub>12</sub> | -0.001 | -0.011 | 0.016<sup>a</sup> | 0.013<sup>a</sup> |
| *UA*<sub>23</sub> | 0.018<sup>a</sup> | 0.017<sup>a</sup> | 0.020<sup>b</sup> | 0.027<sup>b</sup> |
| *UA*<sub>34</sub> | 0.127<sup>b</sup> | 0.132<sup>b</sup> | 0.118<sup>b</sup> | 0.126<sup>b</sup> |
| *UA*<sub>45</sub> | 0.030<sup>a</sup> | 0.091<sup>b</sup> | 0.013 | 0.067<sup>b</sup> |
| *PD*<sub>12</sub> | -0.007 | -0.043<sup>b</sup> | 0.013 | -0.020<sup>b</sup> |
| *PD*<sub>23</sub> | 0.035<sup>b</sup>  | 0.046<sup>b</sup> | 0.029<sup>b</sup> | 0.062<sup>b</sup> |
| *PD*<sub>34</sub> | 0.155<sup>b</sup> | 0.175<sup>b</sup> | 0.140<sup>b</sup> | 0.142<sup>b</sup> |
| *PD*<sub>45</sub> | 0.124<sup>b</sup> | 0.065<sup>b</sup> | 0.058<sup>b</sup> | 0.034<sup>b</sup> |
| *AD*<sub>12</sub> | 0.009 | -0.023<sup>b</sup> | 0.030<sup>b</sup> | 0.012 |
| *AD*<sub>23</sub> | 0.083<sup>b</sup> | 0.032<sup>b</sup> | 0.060<sup>b</sup> | 0.043<sup>b</sup> |
| *AD*<sub>34</sub> | 0.094<sup>b</sup> | 0.138<sup>b</sup> | 0.101<sup>b</sup> | 0.122<sup>b</sup> |
| *AD*<sub>45</sub> | 0.018<sup>a</sup> | 0.002 | 0.014 | 0.013 |
| *μ (mean)* | 0.194 | 0.228<sup>b</sup> | 1.275<sup>b</sup> | 0.899<sup>b</sup> |
| *r (mean)* | -0.227<sup>a</sup> | -0.483<sup>b</sup> | 0.422<sup>b</sup> | -0.489<sup>b</sup> |
| *μ (SD)* | 1.232<sup>b</sup> | 1.136<sup>b</sup> |  |  |
| *r (SD)* |  |  | 1.325<sup>b</sup> | 1.320<sup>b</sup> |
| *V(55555)* | -0.162<sup>b</sup> | -0.134<sup>b</sup> | -0.043<sup>b</sup> | -0.118<sup>b</sup> |
| *LL* | -11964 | -12989 | -10666 | -12279 |

Notice that the scale parameter is equal to  and the power is equal to  to bound the power between 0 and 1

<sup>a</sup>, <sup>b</sup> represent significance levels at 5% and 1%, respectively

</div>

### Abbreviations

MSL  
Maximum simulated likelihood

ML  
Maximum likelihood

QALY  
Quality-adjusted life year

CL  
Conditional logit

MO  
Mobility

SC  
Self-care

UA  
Usual activities

PD  
Pain and discomfort

AD  
Anxiety and depression

EQ-VT  
EuroQol Valuation Technology

CLL  
Complementary log–log

MAR  
Maximum acceptable risk

NPV  
Net present value

EV1  
Extreme value type 1

IID  
Independently and identically distributed

RUM  
Random utility maximization

### Acknowledgements

The authors would like to thank the EuroQol Research Foundation for their support of Maksat Jumamyradov’s dissertation, under awards 207-2020RA and 304-PHD. We also thank Drs. Murat Munkin and William Greene who advise Maksat on his dissertation.

#### Precis

We investigate how allowing heterogeneity in scale and rate affect the estimation of EQ-5D-5L values.

### Authors’ contributions

BMC and MJu were responsible for the concept and design of the manuscript. BMC and MJa were involved in data collection. BMC and MJu were involved in analysis, interpretation of data, and drafting of the manuscript. All authors were involved in critical revision of paper for important intellectual content. MJu was responsible for the statistical analysis.

### Funding

The EuroQol Research Foundation supported this project (No: 207-2020RA).

### Availability of data and materials

The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request.

### Declarations

#### Ethics approval and consent to participate

Not applicable.

#### Consent for publication

Not applicable.

#### Competing interests

Jumamyradov reports grants from EuroQol Research Foundation, during the conduct of the study. Dr. Craig has nothing to disclose. Dr. Jakubczyk has nothing to disclose.

## References

1. Jonker MF. The garbage class mixed logit model: accounting for low-quality response patterns in discrete choice experiments. Value Health. 2022;25(11):1871–7.36202702 10.1016/j.jval.2022.07.013

2. Groothuis-Oudshoorn CG, Flynn TN, Yoo HI, Magidson J, Oppe M. Key issues and potential solutions for understanding healthcare preference heterogeneity free from patient-level scale confounds. Patient. 2018;11(5):463–6.29691804 10.1007/s40271-018-0309-5

3. Craig BM, Rand K. Choice defines QALYs: a US valuation of the EQ-5D-5L. Med Care. 2018;56(6):529–36.29668646 10.1097/MLR.0000000000000912

4. Craig BM, Rand K, Bailey H, Stalmeier PF. Quality-adjusted life-years without constant proportionality. Value Health. 2018;21(9):1124–31.30224118 10.1016/j.jval.2018.02.004

5. Jonker MF, Donkers B, de Bekker-Grob EW, Stolk EA. Advocating a paradigm shift in health-state valuations: the estimation of time-preference corrected QALY tariffs. Value Health. 2018;21(8):993–1001.30098678 10.1016/j.jval.2018.01.016

6. Jonker MF, Bliemer MC. On the optimization of Bayesian D-efficient discrete choice experiment designs for the estimation of QALY tariffs that are corrected for nonlinear time preferences. Value Health. 2019;22(10):1162–9.31563259 10.1016/j.jval.2019.05.014

7. Jonker MF, Norman R. Not all respondents use a multiplicative utility function in choice experiments for health state valuations, which should be reflected in the elicitation format (or statistical analysis). Health Econ. 2022;31(2):431–9.34841637 10.1002/hec.4457PMC9298783

8. Karim S, Craig BM, Tejada RA, Augustovski F. Preference heterogeneity in health valuation: a latent class analysis of the Peru EQ-5D-5L values. Health Qual Life Outcomes. 2023;21(1):1.36593473 10.1186/s12955-022-02079-6PMC9808950

9. Craig BM, de Bekker-Grob EW, González Sepúlveda JM, Greene WH. A guide to observable differences in stated preference evidence. Patient. 2022;15(3):329–39.34697755 10.1007/s40271-021-00551-xPMC8545560

10. McFadden D. Conditional logit analysis of qualitative choice behavior. In: Zarembka P, editor. Frontiers in Econometrics. New York, USA: Academic Press; 1974. p. 105–42.

11. Revelt D, Train K. Mixed logit with repeated choices: households’ choice of appliance efficiency level. Rev Econ Stat. 1998;80(4):647–57. doi:10.1162/003465398557735

12. Brownstone D, Train K. Forecasting new product penetration with flexible substitution patterns. J Econom. 1998;89(1–2):109–29. doi:10.1016/S0304-4076(98)00057-8

13. McFadden D, Train K. Mixed MNL models of discrete response. J Appl Economet. 2000;15(5):447–70. doi:10.1002/1099-1255(200009/10)15:5<447::AID-JAE570>3.0.CO;2-1

14. David HA. The method of paired comparisons. London, UK: Griffin; 1963.

15. Attema AE, Bleichrodt H, L’haridon O, Peretti-Watel P, Seror V. Discounting health and money: New evidence using a more robust method. J Risk Uncertain. 2018;56:117–40.31007384 10.1007/s11166-018-9279-1PMC6445504

16. Lipman SA, Attema AE, Versteegh MM. Correcting for discounting and loss aversion in composite time trade-off. Health Econ. 2022;31(8):1633–48.35474364 10.1002/hec.4529PMC9541376

17. Jonker MF, Donkers B. Interaction effects in health state valuation studies: an optimal scaling approach. Value in Health. 2023;26(4):554–6.36323377 10.1016/j.jval.2022.10.008

18. Oppe M, Rand-Hendriksen K, Shah K, Ramos-Goñi JM, Luo N. EuroQol protocols for time trade-off valuation of health outcomes. Pharmacoeconomics. 2016;34(10):993–1004.27084198 10.1007/s40273-016-0404-1PMC5023738

19. Jakubczyk M, Craig BM, Barra M, et al. Choice defines value: a predictive modeling competition in health preference research. Value Health. 2018;21(2):229–38.29477405 10.1016/j.jval.2017.09.016

20. Gourieroux C, Monfort A. Simulation based inference in models with heterogeneity. Annales d’Economie et de Statistique. 1991;20(21):69–107.

21. Gourieroux C, Monfort A. Simulation-based econometric methods. New York, USA: Oxford University Press; 1996.

22. Palma MA, Vedenov DV, Bessler D. The order of variables, simulation noise, and accuracy of mixed logit estimates. Empir Econ. 2020;58(5):2049–83. doi:10.1007/s00181-018-1609-2

23. Craig BM, Pickard AS, Rand-Hendriksen K. Do health preferences contradict ordering of EQ-5D labels? Qual Life Res. 2015;24:1759–65.25519940 10.1007/s11136-014-0897-zPMC5115631

24. Craig BM, Monteiro AL, Herdman M, Santos M. Further evidence on EQ-5D-5L preference inversion: a Brazil/US collaboration. Qual Life Res. 2017;26:2489–96.28484914 10.1007/s11136-017-1591-8

25. Jumamyradov M, Craig BM, Munkin M, and Geene W. Comparing the mixed logit estimates and true parameters under informative and uninformative heterogeneity: a simulated discrete choice experiment. Comput Econ. Accepted 2024. 10.1007/s10614-024-10637-x.

26. Jumamyradov M, Munkin MK. Biases in Maximum Simulated Likelihood Estimation of Bivariate Models. J Econom Methods. 2021;11(1):55–70. doi:10.1515/jem-2021-0003

27. Hess S, Rose JM. Can scale and coefficient heterogeneity be separated in random coefficients models? Transportation. 2012;39:1225–39. doi:10.1007/s11116-012-9394-9

28. Hess S, Train K. Correlation and scale in mixed logit models. J Choice Model. 2017;23:1–8. doi:10.1016/j.jocm.2017.03.001

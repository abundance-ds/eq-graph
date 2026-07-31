---
project_id: "2015300"
work_id: "doi:10.1007/s40273-018-0694-6"
doi: "10.1007/s40273-018-0694-6"
pmid: "30030818"
pmcid: "PMC6182499"
title: "Severity-Stratified Discrete Choice Experiment Designs for Health State Evaluations"
journal: "Pharmacoeconomics"
publication_date: "2018-07-21"
volume: "36"
issue: "11"
authors:
  - name: "Sesil Lim"
    orcid: "http://orcid.org/0000-0002-2227-8906"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Marcel F. Jonker"
    affiliation_ids:
      - "Aff1"
      - "Aff3"
      - "Aff4"
  - name: "Mark Oppe"
    affiliation_ids:
      - "Aff1"
      - "Aff5"
  - name: "Bas Donkers"
    affiliation_ids:
      - "Aff1"
      - "Aff2"
  - name: "Elly Stolk"
    affiliation_ids:
      - "Aff1"
      - "Aff5"
affiliations:
  - id: "Aff1"
    name: "0000000092621349grid.6906.9Erasmus Choice Modelling Centre, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff2"
    name: "0000000092621349grid.6906.9Erasmus School of Economics, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff3"
    name: "0000000092621349grid.6906.9Erasmus School of Health Policy & Management, Erasmus University Rotterdam, Rotterdam, The Netherlands"
  - id: "Aff4"
    name: "0000 0004 1936 7961grid.26009.3dDuke Clinical Research Institute, Duke University, Durham, NC USA"
  - id: "Aff5"
    name: "0000 0004 5906 3508grid.478988.2EuroQol Research Foundation, Rotterdam, The Netherlands"
licence: "cc-by-nc"
source_file: "input/projects/2015300/papers/doi_10.1007_s40273-018-0694-6.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6182499/fullTextXML"
source_method: "epmc_xml"
source_sha256: "2e1cebc0108c6fcbda08377396fad8012bf8ccdbcbed8b62102cfb924221e8e1"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Severity-Stratified Discrete Choice Experiment Designs for Health State Evaluations

## Abstract

### Background

Discrete choice experiments (DCEs) are increasingly used for health state valuations. However, the values derived from initial DCE studies vary widely. We hypothesize that these findings indicate the presence of unknown sources of bias that must be recognized and minimized. Against this background, we studied whether values derived from a DCE are sensitive to how well the DCE design spans the severity range.

### Methods

We constructed an experiment involving three variants of DCE tasks for health state valuation: standard DCE, DCE-death, and DCE-duration. For each type of DCE, an experimental design was generated under two different conditions, enabling a comparison of health state values derived from current best practice Bayesian efficient DCE designs with values derived from ‘severity-stratified’ designs that control for coverage of the severity range in health state selection. About 3000 respondents participated in the study and were randomly assigned to one of the six study arms.

### Results

Imposing the severity-stratified restriction had a large effect on health states sampled for the DCE-duration approach. The unstratified efficient design returned a skewed distribution of selected health states, and this introduced bias. The choice probability of bad health states was underestimated, and time trade-offs to avoid bad states were overestimated, resulting in too low values. Imposing the same restriction had limited effect in the DCE-death approach and standard DCE.

### Conclusion

Variation in DCE-derived values can be partially explained by differences in how well selected health states spanned the severity range. Imposing a ‘severity stratification’ on DCE-duration designs is a validity requirement.

### Electronic supplementary material

The online version of this article (10.1007/s40273-018-0694-6) contains supplementary material, which is available to authorized users.

## Key Points for Decision Makers

<div id="Taba" class="table-wrap">

|  |
|----|
| Unstratified efficient design algorithms cannot guarantee adequate coverage of the severity range. |
| If health state selection bias occurs in DCE-duration studies, the derived values may be too low. |
| Sampling choice task from different severity strata is a way to prevent skewed designs and biased values. |

</div>

## Introduction

The use of the discrete choice experiment (DCE) has attracted researchers’ interest as an alternative to more conventional techniques, such as the time trade-off (TTO) method, to derive quality-adjusted life years (QALYs) in health state evaluation. One of the merits of using DCE methodologies is that they improve the feasibility of valuation studies. In contrast to TTO valuations, which require organizationally complex and costly face-to-face interviews, DCE valuation surveys can be self-administered \[1, 2\]. However, the use of a DCE for valuation introduces an unusual requirement in the DCE, namely that the estimated values are anchored at 1 for full health and 0 for death. The validity of the proposed approaches to achieve that has yet to be established. Two proposed strategies include the DCE-death and the DCE-duration approaches. However, results obtained from initial applications of those methods were markedly different. For instance, Norman et al. \[3, 4\] showed that DCE-duration approaches consistently produce lower values than DCE-death approaches. Also compared to conventional health valuation methods, DCEs have produced discrepant results. Craig et al. \[5\] and Jonker et al. \[6\] reported a considerably longer value range derived from their DCE approaches (minimum values \< −  1.5) than the range obtained with the conventional TTO for EQ-5D (− 0.594 to 1.000) \[7\]. Researchers now aim to understand why.

We aim to contribute to the body of knowledge of how best to implement DCE methods for health state valuation, with a focus on strategies for the development of the experimental design. In this area, methodological advancements made best practice somewhat of a moving target. On top of that, best practice for choosing a strategy for designs may well be context dependent \[8, 9\]. Whereas some general considerations always apply, such as the importance of identification and statistical efficiency, other demands can be application specific. The latter may be the case in the field of health state valuation.

A popular approach for the construction of experimental designs in DCEs is the (Bayesian) efficient design approach. These designs exploit prior information to arrive at a design that produces small asymptotic standard errors. Because of the direct link between standard errors and sample size requirement, this is a desirable property \[10\]. Efficient designs have been frequently used in DCEs for health valuation \[2, 6, 11, 12\]. However, these designs are not without problems. A potential problem is that designs purely optimized for statistical efficiency can produce more difficult choice sets \[13\]. As a result, respondents might not always have a clear preference for any of the options, or they may be tempted to use simplifying decision rules that obscure their true preferences and cause bias \[14\]. A current line of research is whether such concerns can be addressed by introducing constraints on the design generation algorithms for DCEs, for example, by forcing attribute-level overlap in the constructed choice sets \[15, 16\]. Another potential problem is that the choice sets will not be selected at random, but rather chosen to support estimation of a proposed utility function \[8, 17\]. The algorithm will favor choice tasks that clearly reveal attribute trade-offs and avoid strongly dominant alternatives \[18\]. As a consequence, each health state has a different probability to be included in the choice tasks \[17\]. This can cause bias if decisions derived from included health states do not predict decisions about health states that have a lower inclusion probability due to model misspecification.

Currently, it is unknown whether this bias is a problem in DCEs designed to capture the value of health, but we hypothesize that it might be. Because optimization algorithms consider the level of utility balance for better statistical efficiency \[19\], the fact that the DCE-death and the DCE-duration approaches present respondents with very different fixed alternatives can cause other health states to be favored in the different approaches. To investigate the issue, we set up an experiment featuring EQ-5D-5L health states. First, we examine whether the current best practice efficient DCE designs (i.e. ‘*unstratified*’ efficient designs) tend to favor a particular type of health states in the context of various DCE formats. Second, we investigate the sensitivity of estimated health state values to the potentially skewed selection of health states by comparing estimates derived from unstratified designs with those from DCE designs that satisfy the requirement that the set of selected health states has to span the entire severity scale (i.e. ‘*severity*-*stratified*’ designs).

## Methods

To investigate the issues mentioned above, we proposed a strategy for generating severity-stratified designs and compared the severity-stratified designs to unstratified efficient designs on (1) health state selection for inclusion in DCE tasks and (2) values derived from the DCE tasks. We did this in the context of three different DCE formats: standard DCE, DCE-death, and DCE-duration. Table <a href="#Tab1" data-ref-type="table">1</a> shows the overview of the six study arms used in this study.

<div id="Tab1" class="table-wrap">

<div class="caption">

Overview of the study arms

</div>

|              | Unstratified | Severity-stratified |
|--------------|--------------|---------------------|
| Standard DCE | 1            | 4                   |
| DCE-death    | 2            | 5                   |
| DCE-duration | 3            | 6                   |

*DCE* discrete choice experiment

</div>

### The Discrete Choice Experiment (DCE) Choice Tasks

Figure <a href="#Fig1" data-ref-type="fig">1</a> provides an example of the three DCE formats. The health states were defined by the five dimensions of the EQ-5D-5L instrument: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. For each dimension, five levels are used to describe the severity of impairment in monotonic order from ‘no problems’ (level 1) to ‘extreme problems/unable’ (level 5).

<figure id="Fig1">
<p><img src="40273_2018_694_Fig1_HTML.jpg" id="MO1" /></p>
<figcaption>Presentation of choice tasks: <strong>a</strong> standard DCE; <strong>b</strong> DCE-death; <strong>c</strong> DCE-duration. <em>DCE</em> discrete choice experiment</figcaption>
</figure>

The *standard DCE* was a forced choice paired comparison between two health states where respondents were asked to choose between 10 years in health state A and 10 years in health state B. This task focused on the direct trade-off between the health state attributes and produces values on a latent scale.

In the *DCE*-*death* format, each choice task had three alternatives, A, B, and C, and respondents compared A to B and B to C using a so-called ‘matched pairwise choice task’ \[6, 15, 20\]. The A–B comparison resembled the standard DCE described above. The next question was a forced choice between 10 years in health state B versus immediate death (i.e., B–C comparison). Each choice task thus comprises two pairwise comparisons so that the number of observations will be twice as high as in the standard DCE. However, the cognitive burden is only marginally increased, because option B appears in both comparisons and option C is fixed and easy to imagine.

In the *DCE*-*duration* format, each choice task also had three alternatives, A, B, and C, that were compared using a matched pairwise choice task. Respondents were first asked to choose between 10 years in health state A and 10 years in health state B (i.e., A–B comparison), followed by the B–C comparison, where option C was always health state 11111 (i.e., no problems in any EQ-5D dimension) with a duration shorter than that of option B. Length of life in the perfect health was restricted to 12 levels: 2, 4, 6 months and 1, 2, …, 9 years.[^1]

In order to reduce task complexity and respondent burden, all choice tasks for the A–B comparisons included attribute-level overlap \[6, 15\]. For each pair of choices A and B, a minimum of two out of five dimensions were presented at the same level. In addition, combinations of the first level (no problem) of usual activities with the fifth level (extreme problems) of pain/discomfort and/or anxiety/depression were avoided to make health states easier to imagine and evaluate. Lastly, intensity color coding was used to further reduce task complexity. Imposing attribute-level overlap and color coding as well as excluding implausible states is currently best practice considering the reduced dropout rate and improved respondents’ attribute attendance in DCE \[15\].

### Experimental Designs With/Without Severity-Stratified Restriction

We implemented heterogeneous DCE design algorithms to create for each study arm a unique experimental design comprising 168 choice tasks, distributed over eight sub-designs \[21\]. The algorithm optimizes for Bayesian D error for the total design, while simultaneously optimizing for the Bayesian D errors of each of the eight sub-designs. In essence, this strategy produces a blocked design with eight blocks, where the design within each block is optimized in addition to the optimization of the overall design across blocks. A Latin hypercube sample optimized for maximum minimum distance between points and a greedy optimization algorithm was used to optimize the weighted averaged Bayesian D error with one-third of the weight assigned to the aggregated efficiency and two-thirds on the individual efficiencies of the sub-designs. Note that the design algorithm controlled for left–right randomization of the two states by including both options A and B in comparison with option C in the Bayesian design criterion, even though only one of the two choice options was presented (in random order) to the survey respondents.

To obtain an identifiable DCE design at the individual level, each sub-design contained 21 choice tasks, that is, the number of parameters to be estimated in a main effects model. As Bliemer and Rose \[22\] suggested, a DCE design optimized for a standard conditional logit model performs well for estimating panel mixed logit models. Therefore, the design was optimized for a conditional logit model, which reduced the computational burden substantially.

Whereas the full candidate set of all possible EQ-5D-5L health states (excluding 225 implausible health states) was used to optimize the unstratified DCE designs, the severity-stratified DCE designs used different candidate sets for each choice task. The creation of severity-stratified designs involved the following steps:

1.  Informative priors were used to predict latent utility values for all health states, which were subsequently used to divide the health states into 21 severity strata (i.e., 3125/21 = ~ 148 states per stratum for each DCE format, thus comprising as many severity strata as there were choice tasks in each DCE design).

2.  A total of 225 implausible health states were removed from the full set of 3125 health states and from each of the 21 strata.

3.  For each stratum, candidate sets were constructed by creating all possible combinations of health states in the stratum with all other possible health states (i.e., 148 × 2899/2 = ~ 0.2 million).

4.  The design algorithm created a DCE design that included exactly one choice task from each candidate set in each sub-design.

Prior values used for the DCE design optimization (and thus also in step 1) were obtained from previous research (based on an unstratified DCE design; unpublished to date), which contains 350 Dutch respondents for each DCE format. The design algorithm was implemented in Julia \[23\].

### Statistical Analysis

To analyze the health state preferences, a mixed logit model[^2] was used. For the standard DCE, the utility of the respondent *i* for the health state *j* in the choice task *t* was specified as:

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
                \begin{document}$$U_{ijt} = X_{ijt} \beta_{i} + \epsilon_{ijt}$$\end{document}
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
                \begin{document}$$X_{ijt}$$\end{document}`$ consists of 20 dummies for EQ-5D-5L instruments assuming the level 1 (no health problem) as the reference category for each dimension. The error $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\epsilon_{ijt}$$\end{document}`$ is assumed independent and identically distributed with an extreme value distribution, and the vector of individual-specific coefficients $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\beta_{i}$$\end{document}`$ is assumed to follow a multivariate normal distribution with the population mean $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu$$\end{document}`$ and covariance matrix $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\sum$$\end{document}`$, that is, $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\beta_{i} \sim {\text{MVN}}\left( {\mu , \;\sum } \right)$$\end{document}`$. The same utility function was applied to the DCE-death approach; however, now $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$X_{ijt}$$\end{document}`$ includes a dummy indicating death options.

For the DCE-duration approach, the utility was specified as the function of the product of the number of life years ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$T_{ijt}$$\end{document}`$) and its observed characteristics ($`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$X_{ijt}$$\end{document}`$) and their corresponding coefficients as follows:

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
                \begin{document}$$U_{ijt} = \left( {T_{ijt} X_{ijt} } \right)\beta_{i} + \epsilon_{ijt}$$\end{document}
```

</div>

Note that $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$X_{ijt}$$\end{document}`$ consists of dummies for the EQ-5D-5L instrument and an intercept with the value 1, and the coefficient for the duration main effect represents the value respondent *i* assigns to living in perfect health for 1 year.

The specified models were estimated using the Bayesian Markov chain Monte Carlo (MCMC) methods as implemented in the *R* package *bayesm* \[25\]. Gibbs sampling was used to update $`\documentclass[12pt]{minimal}
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
                \begin{document}$$\sum$$\end{document}`$, and a Metropolis–Hastings algorithm was used to update $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\beta_{i}$$\end{document}`$. A multivariate normal prior (with a mean of zero and a variance of *100∙I*) was used for $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\mu$$\end{document}`$, and an inverse Wishart prior (with the dimension of $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\sum$$\end{document}`$ plus 3 degrees of freedom, i.e., $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\nu ,$$\end{document}`$ and a location parameter $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\nu I$$\end{document}`$) was used for $`\documentclass[12pt]{minimal}
                \usepackage{amsmath}
                \usepackage{wasysym} 
                \usepackage{amsfonts} 
                \usepackage{amssymb} 
                \usepackage{amsbsy}
                \usepackage{mathrsfs}
                \usepackage{upgreek}
                \setlength{\oddsidemargin}{-69pt}
                \begin{document}$$\sum$$\end{document}`$. Mean posterior estimates and 95% credible intervals were calculated by thinning the MCMC draws every fifth iteration for a total of 100,000 iterations. Convergence was established using visual inspection of chains and the convergence diagnostics as implemented in the R package *CODA* \[26\].

For testing hypotheses, the values for health states derived from the DCE-death and DCE-duration approaches were rescaled on the QALY scale where death has a value of 0 and full health a value of 1. To rescale the values, we divided the EQ-5D-5L parameters by the absolute value of the parameter for ‘death’ for DCE-death, and by the parameter value for ‘duration’ for DCE-duration for each draw of the posterior distribution of parameters. Next, the hypotheses that efficient design algorithms for the DCE-death and DCE-duration approaches tend to choose health states in skewed severity ranges was tested by comparing the distribution of values between designs with and without the severity stratification. For the hypothesis regarding the sensitivity of extrapolated health state values to the selection of health states, differences in values for the same health states between the designs with and without severity stratification were examined.

As DCEs aim to predict the choice probabilities of alternatives among given choice sets, we compared the predictive performance of estimates from the severity-stratified designs with those without that restriction using the mean errors (MEs), that is, the average deviation of predicted choice probability of a health state from the observed choice probabilities in each study arm. We used MEs to examine the direction of the bias that the estimates of each study arm produced.[^3] Specifically, when comparing the impaired health states with the death or perfect health states, positive (negative) MEs regarding the impaired health state suggests that the predicted model of the study arm is likely to undervalue (overvalue) the disutility of impaired states so that it over-predicts (under-predicts) the choice probability of living in the impaired health condition compared with the actual observation. Cross validation of the MEs was done by applying the valuation function obtained in one study arm to the data of the other study arm of the same DCE format. The posterior predictive choice probability distribution was obtained by simulating mixed logit probabilities for each sample of the parameters in the posterior distribution, from which the distribution of MEs was inferred. Whether MEs were significantly different from zero was determined based on the 95% level credible intervals of the distribution of MEs.

### Data Collection

The fieldwork was undertaken by Survey Sampling International (SSI) through an online platform during 2 weeks in December 2015. The target sample size was 3000 respondents (i.e., 500 respondents per study arm) representative of the Dutch general population regarding age, gender, and education. Respondents were recruited from SSI’s online panel that contains representative panelists of the population aged 15–65 years and as many panelists aged over 65 years to resemble a nationally representative sample as much as possible. All respondents who gave consent for participation were asked about their demographics to enable stratification of the sample and were randomly assigned by SSI’s survey management software to one of the six study arms and to one of eight sub-designs within that arm. After receiving the information regarding EQ-5D-5L instruments, respondents completed the 21 choice tasks in a random order. A total of 693 respondents who did not complete the tasks were excluded from the analysis. The average response time of respondents was 27 min (50% of respondents completed within 10 min).

## Results

Table <a href="#Tab2" data-ref-type="table">2</a> shows the background characteristics of respondents. Respondents’ characteristics are comparable to those in the Dutch population, and no significant imbalance in respondents’ characteristics between unstratified and severity-stratified designs was found.

<div id="Tab2" class="table-wrap">

<div class="caption">

Descriptive statistics of respondents

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">Characteristics</th>
<th style="text-align: left;">Subgroup</th>
<th colspan="2" style="text-align: left;">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Overall sample vs. Netherlands population</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Overall sample (<em>N</em> = 3122)</td>
<td style="text-align: left;">Dutch population<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;">15–20</td>
<td style="text-align: left;">197 (6.3%)</td>
<td style="text-align: left;">7.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">20–40</td>
<td style="text-align: left;">1006 (32.2%)</td>
<td style="text-align: left;">29.5%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">40–65</td>
<td style="text-align: left;">1390 (44.5%)</td>
<td style="text-align: left;">41.3%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">65–80</td>
<td style="text-align: left;">472 (15.1%)</td>
<td style="text-align: left;">16.8%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Over 80</td>
<td style="text-align: left;">57 (1.8%)</td>
<td style="text-align: left;">5.2%</td>
</tr>
<tr>
<td style="text-align: left;"> Gender</td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">1530 (49.0%)</td>
<td style="text-align: left;">54.9%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">1592 (51.0%)</td>
<td style="text-align: left;">45.2%</td>
</tr>
<tr>
<td style="text-align: left;"> Education</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">1026 (32.9%)</td>
<td style="text-align: left;">30.1%<sup>b</sup></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;">1402 (44.9%)</td>
<td style="text-align: left;">39.8%</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">694 (22.2%)</td>
<td style="text-align: left;">30.1%</td>
</tr>
<tr>
<td style="text-align: left;"> Self-rated health</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.819 ± 0.218</td>
<td style="text-align: left;">0.869 ± 0.170<sup>c</sup></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Standard DCE</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Unstratified (<em>N</em> = 526)</td>
<td style="text-align: left;">Severity-stratified (<em>N</em> = 520)</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;">15–20</td>
<td style="text-align: left;">31 (5.9%)</td>
<td style="text-align: left;">30 (5.8%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">20–40</td>
<td style="text-align: left;">165 (31.4%)</td>
<td style="text-align: left;">186 (35.8%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">40–65</td>
<td style="text-align: left;">229 (43.5%)</td>
<td style="text-align: left;">223 (42.9%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">65–80</td>
<td style="text-align: left;">88 (16.7%)</td>
<td style="text-align: left;">68 (13.1%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Over 80</td>
<td style="text-align: left;">13 (2.5%)</td>
<td style="text-align: left;">13 (2.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Gender</td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">259 (49.2%)</td>
<td style="text-align: left;">254 (48.8%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">267 (50.8%)</td>
<td style="text-align: left;">266 (51.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Education</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">167 (31.7%)</td>
<td style="text-align: left;">161 (31.0%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;">235 (44.7%)</td>
<td style="text-align: left;">233 (44.8%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">124 (23.6%)</td>
<td style="text-align: left;">126 (24.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-rated health</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.815 ± 0.214</td>
<td style="text-align: left;">0.827 ± 0.218</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">DCE-death</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Unstratified (<em>N</em> = 520)</td>
<td style="text-align: left;">Severity-stratified (<em>N</em> = 518)</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;">15–20</td>
<td style="text-align: left;">42 (8.1%)</td>
<td style="text-align: left;">36 (6.9%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">20–40</td>
<td style="text-align: left;">171 (32.9%)</td>
<td style="text-align: left;">158 (30.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">40–65</td>
<td style="text-align: left;">232 (44.6%)</td>
<td style="text-align: left;">235 (45.4%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">65–80</td>
<td style="text-align: left;">67 (12.9%)</td>
<td style="text-align: left;">83 (16.0%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Over 80</td>
<td style="text-align: left;">8 (1.5%)</td>
<td style="text-align: left;">6 (1.2%)</td>
</tr>
<tr>
<td style="text-align: left;"> Gender</td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">257 (49.4%)</td>
<td style="text-align: left;">267 (51.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">263 (50.6%)</td>
<td style="text-align: left;">251 (48.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Education</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">174 (33.5%)</td>
<td style="text-align: left;">177 (34.2%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;">232 (44.6%)</td>
<td style="text-align: left;">235 (45.4%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">114 (21.9%)</td>
<td style="text-align: left;">106 (20.5%)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-rated health</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.821 ± 0.219</td>
<td style="text-align: left;">0.812 ± 0.221</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">DCE-duration</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Unstratified (<em>N</em> = 521)</td>
<td style="text-align: left;">Severity-stratified (<em>N</em> = 517)</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: left;">15–20</td>
<td style="text-align: left;">25 (4.8%)</td>
<td style="text-align: left;">33 (6.4%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">20–40</td>
<td style="text-align: left;">164 (31.5%)</td>
<td style="text-align: left;">162 (31.3%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">40–65</td>
<td style="text-align: left;">238 (45.7%)</td>
<td style="text-align: left;">233 (45.1%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">65–80</td>
<td style="text-align: left;">86 (16.5%)</td>
<td style="text-align: left;">80 (15.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Over 80</td>
<td style="text-align: left;">8 (1.5%)</td>
<td style="text-align: left;">9 (1.7%)</td>
</tr>
<tr>
<td style="text-align: left;"> Gender</td>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">252 (48.4%)</td>
<td style="text-align: left;">241 (46.6%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">269 (51.6%)</td>
<td style="text-align: left;">276 (53.4%)</td>
</tr>
<tr>
<td style="text-align: left;"> Education</td>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">174 (33.4%)</td>
<td style="text-align: left;">173 (33.5%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">Medium</td>
<td style="text-align: left;">233 (44.7%)</td>
<td style="text-align: left;">234 (45.3%)</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">High</td>
<td style="text-align: left;">114 (21.9%)</td>
<td style="text-align: left;">110 (21.3%)</td>
</tr>
<tr>
<td style="text-align: left;"> Self-rated health</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.835 ± 0.203</td>
<td style="text-align: left;">0.807 ± 0.232</td>
</tr>
</tbody>
</table>

Education: low = primary and junior secondary education including both general and vocational schools; medium = senior secondary education including general and vocational schools, and pre-university; high = bachelor’s, master’s and doctoral degree. Self-rated health: average values of respondents’ self-rated EQ-5D-5L health state that converted on QALY scale using a Dutch tariff \[27\]

*DCE* discrete choice experiment, *QALY* quality-adjusted life year

<sup>a</sup>Population rates in the Netherlands in 2017 were retrieved from the Statistics Netherlands (CBS) website. The distribution of age and gender were given for the population over 15 years old, while the distribution according to the level of education was available only for the population between 15 and 75 years old

<sup>b</sup>The population with unknown educational level (1.5%) was included. Also, the population with level 1 diploma of the senior secondary vocational school was included, while respondents with that characteristic belonged to the middle education group in the study

<sup>c</sup>Reference values for the Dutch general population based on 979 respondents \[27\]. Note that this paper did not collect data stratified by respondents’ health state

</div>

Figure <a href="#Fig2" data-ref-type="fig">2</a> and Table <a href="#Tab3" data-ref-type="table">3</a> show the distributions of the modeled values for all EQ-5D-5L health states. As shown in Fig. <a href="#Fig2" data-ref-type="fig">2</a>, the distribution of states included in the design more closely followed the distribution for all health states when the severity stratification was applied for all DCE formats. It is most apparent for the DCE-duration format, where the unstratified design has a much more skewed distribution than the severity-stratified design.

<figure id="Fig2">
<p><img src="40273_2018_694_Fig2_HTML.jpg" id="MO4" /></p>
<figcaption>Comparison of distributions of health state values between designs with and without severity-stratification. Distribution of modeled values for all possible EQ-5D health states (red bars) and modeled values for EQ-5D health states included in the designs (black bars). Health state values are on latent utility scales for the standard DCE (<strong>a</strong>), while they are on QALY scales for DCE-death (<strong>b</strong>) and DCE-duration (<strong>c</strong>). <em>DCE</em> discrete choice experiment, <em>QALY</em> quality-adjusted life year</figcaption>
</figure>

<div id="Tab3" class="table-wrap">

<div class="caption">

Distribution of health states selected for the designs over severity strata

</div>

<table>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"></th>
<th colspan="2" style="text-align: left;">Standard DCE</th>
<th colspan="2" style="text-align: left;">DCE-death</th>
<th colspan="2" style="text-align: left;">DCE-duration</th>
</tr>
<tr>
<th style="text-align: left;">Unstratified</th>
<th style="text-align: left;">Severity-stratified</th>
<th style="text-align: left;">Unstratified</th>
<th style="text-align: left;">Severity-stratified</th>
<th style="text-align: left;">Unstratified</th>
<th style="text-align: left;">Severity-stratified</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Number of unique health states</td>
<td style="text-align: left;">284 (100%)</td>
<td style="text-align: left;">319 (100%)</td>
<td>275 (100%)</td>
<td>319 (100%)</td>
<td>256 (100%)</td>
<td>310 (100%)</td>
</tr>
<tr>
<td style="text-align: left;">Better<br />
health state</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>127 (46.2%)</td>
<td>112 (35.1%)</td>
<td>88 (34.4%)</td>
<td>44 (14.2%)</td>
</tr>
<tr>
<td style="text-align: left;">Medium<br />
health state</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>114 (41.5%)</td>
<td>188 (58.9%)</td>
<td>125 (48.8%)</td>
<td>145 (46.7%)</td>
</tr>
<tr>
<td style="text-align: left;">Bad<br />
health state</td>
<td style="text-align: left;">–</td>
<td style="text-align: left;">–</td>
<td>33 (12%)</td>
<td>19 (6.0%)</td>
<td>43 (16.8%)</td>
<td>121 (39.0%)</td>
</tr>
</tbody>
</table>

Bad health states for QALY ≤ 0, medium health state for 0 \< QALY ≤ 0.5, and better health state for 0.5 \< QALY. Because the standard DCE produces values on a latent scale, the division in three severity strata was omitted for those designs

*DCE* discrete choice experiment, *QALY* quality-adjusted life year

</div>

For DCE-duration, the mean and the standard deviation (SD) of the distribution of health state values included in the unstratified design (i.e., the black bars) were 0.31 and 0.44, respectively, whereas those in the severity-stratified design were 0.09 and 0.35. A similar effect was hypothesized to exist in the DCE-death approach, but no strong evidence was found (mean 0.41 and SD 0.30 for the unstratified design; mean 0.40 and SD 0.26 for the severity-stratified design).

Table <a href="#Tab4" data-ref-type="table">4</a> shows the parameter estimates and corresponding 95% credible intervals for all six study arms. Almost all estimates are statistically significant, and all models resulted in logically consistent parameter estimates in the sense that worse levels of impairment are associated with larger utility decrements.

<div id="Tab4" class="table-wrap">

<div class="caption">

EQ-5D parameter estimates with 95% credible intervals on QALY scales for 6 study arms

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Perfect health</th>
<th colspan="4" style="text-align: left;">Standard DCE<sup>a</sup></th>
<th colspan="4" style="text-align: left;">DCE-death</th>
<th colspan="4" style="text-align: left;">DCE-duration</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Unstratified (arm 1)</th>
<th colspan="2" style="text-align: left;">Severity-stratified (arm 4)</th>
<th colspan="2" style="text-align: left;">Unstratified (arm 2)</th>
<th colspan="2" style="text-align: left;">Severity-stratified (arm 5)</th>
<th colspan="2" style="text-align: left;">Unstratified (arm 3)</th>
<th colspan="2" style="text-align: left;">Severity-stratified (arm 6)</th>
</tr>
<tr>
<th style="text-align: left;">0.00</th>
<th style="text-align: left;">(N/A)</th>
<th style="text-align: left;">0.00</th>
<th style="text-align: left;">(N/A)</th>
<th style="text-align: left;">1.00</th>
<th style="text-align: left;">(N/A)</th>
<th style="text-align: left;">1.00</th>
<th style="text-align: left;">(N/A)</th>
<th style="text-align: left;">1.00</th>
<th style="text-align: left;">(N/A)</th>
<th style="text-align: left;">1.00</th>
<th style="text-align: left;">(N/A)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility 2</td>
<td style="text-align: left;">−  0.19</td>
<td style="text-align: left;">(−  0.38, 0.03)</td>
<td style="text-align: left;">−  0.21</td>
<td style="text-align: left;">(−  0.43, −  0.01)</td>
<td style="text-align: left;">− 0.01</td>
<td style="text-align: left;">(− 0.03, 0.00)</td>
<td style="text-align: left;">− 0.03</td>
<td style="text-align: left;">(− 0.04, − 0.01)</td>
<td style="text-align: left;">− 0.08</td>
<td style="text-align: left;">(− 0.10, − 0.06)</td>
<td style="text-align: left;">− 0.06</td>
<td style="text-align: left;">(− 0.09, − 0.04)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility 3</td>
<td style="text-align: left;">−  0.56</td>
<td style="text-align: left;">(−  0.77, −  0.33)</td>
<td style="text-align: left;">−  0.62</td>
<td style="text-align: left;">(−  0.86, −  0.38)</td>
<td style="text-align: left;">− 0.06</td>
<td style="text-align: left;">(− 0.07, − 0.04)</td>
<td style="text-align: left;">− 0.06</td>
<td style="text-align: left;">(− 0.07, − 0.04)</td>
<td style="text-align: left;">− 0.15</td>
<td style="text-align: left;">(− 0.17, − 0.13)</td>
<td style="text-align: left;">− 0.11</td>
<td style="text-align: left;">(− 0.14, − 0.09)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility 4</td>
<td style="text-align: left;">−  2.34</td>
<td style="text-align: left;">(−  2.65, −  2.01)</td>
<td style="text-align: left;">−  2.23</td>
<td style="text-align: left;">(−  2.56, −  1.92)</td>
<td style="text-align: left;">− 0.15</td>
<td style="text-align: left;">(− 0.17, − 0.14)</td>
<td style="text-align: left;">− 0.17</td>
<td style="text-align: left;">(− 0.19, − 0.15)</td>
<td style="text-align: left;">− 0.33</td>
<td style="text-align: left;">(− 0.37, − 0.29)</td>
<td style="text-align: left;">− 0.26</td>
<td style="text-align: left;">(− 0.30, − 0.22)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility 5</td>
<td style="text-align: left;">−  3.81</td>
<td style="text-align: left;">(−  4.24, −  3.37)</td>
<td style="text-align: left;">−  3.50</td>
<td style="text-align: left;">(−  3.98, −  3.07)</td>
<td style="text-align: left;">− 0.22</td>
<td style="text-align: left;">(− 0.25, − 0.20)</td>
<td style="text-align: left;">− 0.23</td>
<td style="text-align: left;">(− 0.25, − 0.20)</td>
<td style="text-align: left;">− 0.45</td>
<td style="text-align: left;">(− 0.51, − 0.40)</td>
<td style="text-align: left;">− 0.37</td>
<td style="text-align: left;">(− 0.42, − 0.32)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 2</td>
<td style="text-align: left;">−  0.07</td>
<td style="text-align: left;">(−  0.28, 0.15)</td>
<td style="text-align: left;">−  0.47</td>
<td style="text-align: left;">(−  0.69, −  0.26)</td>
<td style="text-align: left;">− 0.02</td>
<td style="text-align: left;">(− 0.04, − 0.01)</td>
<td style="text-align: left;">− 0.03</td>
<td style="text-align: left;">(− 0.04, − 0.01)</td>
<td style="text-align: left;">− 0.08</td>
<td style="text-align: left;">(− 0.10, − 0.06)</td>
<td style="text-align: left;">− 0.07</td>
<td style="text-align: left;">(− 0.10, − 0.05)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 3</td>
<td style="text-align: left;">−  0.82</td>
<td style="text-align: left;">(−  1.05, −  0.58)</td>
<td style="text-align: left;">−  0.90</td>
<td style="text-align: left;">(−  1.11, −  0.69)</td>
<td style="text-align: left;">− 0.08</td>
<td style="text-align: left;">(− 0.10, − 0.06)</td>
<td style="text-align: left;">− 0.05</td>
<td style="text-align: left;">(− 0.07, − 0.04)</td>
<td style="text-align: left;">− 0.13</td>
<td style="text-align: left;">(− 0.16, − 0.11)</td>
<td style="text-align: left;">− 0.13</td>
<td style="text-align: left;">(− 0.16, − 0.10)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 4</td>
<td style="text-align: left;">−  2.25</td>
<td style="text-align: left;">(−  2.55, −  1.96)</td>
<td style="text-align: left;">−  2.01</td>
<td style="text-align: left;">(−  2.31, −  1.73)</td>
<td style="text-align: left;">− 0.14</td>
<td style="text-align: left;">(− 0.16, − 0.13)</td>
<td style="text-align: left;">− 0.16</td>
<td style="text-align: left;">(− 0.18, − 0.14)</td>
<td style="text-align: left;">− 0.31</td>
<td style="text-align: left;">(− 0.35, − 0.27)</td>
<td style="text-align: left;">− 0.27</td>
<td style="text-align: left;">(− 0.31, − 0.23)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care 5</td>
<td style="text-align: left;">−  2.89</td>
<td style="text-align: left;">(−  3.26, −  2.53)</td>
<td style="text-align: left;">−  2.86</td>
<td style="text-align: left;">(−  3.24, −  2.50)</td>
<td style="text-align: left;">− 0.19</td>
<td style="text-align: left;">(− 0.21, − 0.17)</td>
<td style="text-align: left;">− 0.18</td>
<td style="text-align: left;">(− 0.21, − 0.16)</td>
<td style="text-align: left;">− 0.40</td>
<td style="text-align: left;">(− 0.46, − 0.36)</td>
<td style="text-align: left;">− 0.31</td>
<td style="text-align: left;">(− 0.36, − 0.27)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 2</td>
<td style="text-align: left;">−  0.41</td>
<td style="text-align: left;">(−  0.62, −  0.21)</td>
<td style="text-align: left;">−  0.57</td>
<td style="text-align: left;">(−  0.78, −  0.36)</td>
<td style="text-align: left;">− 0.03</td>
<td style="text-align: left;">(− 0.05, − 0.02)</td>
<td style="text-align: left;">− 0.04</td>
<td style="text-align: left;">(− 0.05, − 0.02)</td>
<td style="text-align: left;">− 0.05</td>
<td style="text-align: left;">(− 0.07, − 0.03)</td>
<td style="text-align: left;">− 0.08</td>
<td style="text-align: left;">(− 0.11, − 0.06)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 3</td>
<td style="text-align: left;">−  0.90</td>
<td style="text-align: left;">(−  1.11, −  0.69)</td>
<td style="text-align: left;">−  0.92</td>
<td style="text-align: left;">(−  1.17, −  0.69)</td>
<td style="text-align: left;">− 0.09</td>
<td style="text-align: left;">(− 0.11, − 0.07)</td>
<td style="text-align: left;">− 0.07</td>
<td style="text-align: left;">(− 0.09, − 0.06)</td>
<td style="text-align: left;">− 0.09</td>
<td style="text-align: left;">(− 0.12, − 0.07)</td>
<td style="text-align: left;">− 0.13</td>
<td style="text-align: left;">(− 0.15, − 0.10)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 4</td>
<td style="text-align: left;">−  2.49</td>
<td style="text-align: left;">(−  2.79, −  2.19)</td>
<td style="text-align: left;">−  2.55</td>
<td style="text-align: left;">(−  2.88, − 2.24)</td>
<td style="text-align: left;">− 0.20</td>
<td style="text-align: left;">(− 0.22, − 0.18)</td>
<td style="text-align: left;">− 0.18</td>
<td style="text-align: left;">(− 0.19, − 0.15)</td>
<td style="text-align: left;">− 0.27</td>
<td style="text-align: left;">(− 0.31, − 0.23)</td>
<td style="text-align: left;">− 0.25</td>
<td style="text-align: left;">(− 0.29, − 0.21)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities 5</td>
<td style="text-align: left;">−  3.25</td>
<td style="text-align: left;">(−  3.62, −  2.86)</td>
<td style="text-align: left;">−  3.63</td>
<td style="text-align: left;">(− 4.06, − 3.22)</td>
<td style="text-align: left;">− 0.25</td>
<td style="text-align: left;">(− 0.27, − 0.23)</td>
<td style="text-align: left;">− 0.25</td>
<td style="text-align: left;">(− 0.27, − 0.22)</td>
<td style="text-align: left;">− 0.42</td>
<td style="text-align: left;">(− 0.48, − 0.37)</td>
<td style="text-align: left;">− 0.35</td>
<td style="text-align: left;">(− 0.41, − 0.31)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 2</td>
<td style="text-align: left;">−  0.29</td>
<td style="text-align: left;">(−  0.50, −  0.08)</td>
<td style="text-align: left;">−  0.46</td>
<td style="text-align: left;">(− 0.67, − 0.24)</td>
<td style="text-align: left;">− 0.03</td>
<td style="text-align: left;">(− 0.04, − 0.01)</td>
<td style="text-align: left;">− 0.04</td>
<td style="text-align: left;">(− 0.06, − 0.03)</td>
<td style="text-align: left;">− 0.08</td>
<td style="text-align: left;">(− 0.10, − 0.06)</td>
<td style="text-align: left;">− 0.11</td>
<td style="text-align: left;">(− 0.13, − 0.09)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 3</td>
<td style="text-align: left;">−  1.08</td>
<td style="text-align: left;">(−  1.31, −  0.84)</td>
<td style="text-align: left;">−  1.14</td>
<td style="text-align: left;">(− 1.39, − 0.89)</td>
<td style="text-align: left;">− 0.10</td>
<td style="text-align: left;">(− 0.12, − 0.09)</td>
<td style="text-align: left;">− 0.10</td>
<td style="text-align: left;">(− 0.12, − 0.08)</td>
<td style="text-align: left;">− 0.16</td>
<td style="text-align: left;">(− 0.18, − 0.13)</td>
<td style="text-align: left;">− 0.15</td>
<td style="text-align: left;">(− 0.17, − 0.12)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 4</td>
<td style="text-align: left;">−  3.27</td>
<td style="text-align: left;">(−  3.70, −  2.85)</td>
<td style="text-align: left;">−  3.28</td>
<td style="text-align: left;">(− 3.70, − 2.89)</td>
<td style="text-align: left;">− 0.24</td>
<td style="text-align: left;">(− 0.27, − 0.22)</td>
<td style="text-align: left;">− 0.26</td>
<td style="text-align: left;">(− 0.29, − 0.23)</td>
<td style="text-align: left;">− 0.42</td>
<td style="text-align: left;">(− 0.47, − 0.37)</td>
<td style="text-align: left;">− 0.37</td>
<td style="text-align: left;">(− 0.42, − 0.32)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort 5</td>
<td style="text-align: left;">−  5.31</td>
<td style="text-align: left;">(−  5.89, −  4.74)</td>
<td style="text-align: left;">−  5.08</td>
<td style="text-align: left;">(− 5.68, − 4.54)</td>
<td style="text-align: left;">− 0.37</td>
<td style="text-align: left;">(− 0.40, − 0.34)</td>
<td style="text-align: left;">− 0.39</td>
<td style="text-align: left;">(− 0.43, − 0.36)</td>
<td style="text-align: left;">− 0.66</td>
<td style="text-align: left;">(− 0.74, − 0.58)</td>
<td style="text-align: left;">− 0.53</td>
<td style="text-align: left;">(− 0.61, − 0.47)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 2</td>
<td style="text-align: left;">−  0.76</td>
<td style="text-align: left;">(−  0.98, −  0.54)</td>
<td style="text-align: left;">−  0.71</td>
<td style="text-align: left;">(− 0.91, − 0.50)</td>
<td style="text-align: left;">− 0.05</td>
<td style="text-align: left;">(− 0.07, − 0.04)</td>
<td style="text-align: left;">− 0.06</td>
<td style="text-align: left;">(− 0.08, − 0.05)</td>
<td style="text-align: left;">− 0,09</td>
<td style="text-align: left;">(− 0.12, − 0.07)</td>
<td style="text-align: left;">− 0.09</td>
<td style="text-align: left;">(− 0.12, − 0.07)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 3</td>
<td style="text-align: left;">−  1.37</td>
<td style="text-align: left;">(−  1.66, −  1.08)</td>
<td style="text-align: left;">−  1.12</td>
<td style="text-align: left;">(− 1.40, − 0.86)</td>
<td style="text-align: left;">− 0.11</td>
<td style="text-align: left;">(− 0.13, − 0.09)</td>
<td style="text-align: left;">− 0.10</td>
<td style="text-align: left;">(− 0.12, − 0.08)</td>
<td style="text-align: left;">− 0,19</td>
<td style="text-align: left;">(− 0.22, − 0.16)</td>
<td style="text-align: left;">− 0.17</td>
<td style="text-align: left;">(− 0.21, − 0.14)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 4</td>
<td style="text-align: left;">−  3.66</td>
<td style="text-align: left;">(−  4.12, −  3.21)</td>
<td style="text-align: left;">−  2.96</td>
<td style="text-align: left;">(− 3.40, − 2.55)</td>
<td style="text-align: left;">− 0.26</td>
<td style="text-align: left;">(− 0.29, − 0.24)</td>
<td style="text-align: left;">− 0.24</td>
<td style="text-align: left;">(− 0.27, − 0.21)</td>
<td style="text-align: left;">− 0,40</td>
<td style="text-align: left;">(− 0.46, − 0.35)</td>
<td style="text-align: left;">− 0.37</td>
<td style="text-align: left;">(− 0.42, − 0.32)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression 5</td>
<td style="text-align: left;">−  5.84</td>
<td style="text-align: left;">(−  6.53, −  5.16)</td>
<td style="text-align: left;">−  5.15</td>
<td style="text-align: left;">(− 5.81, − 4.55)</td>
<td style="text-align: left;">− 0.36</td>
<td style="text-align: left;">(− 0.40, − 0.33)</td>
<td style="text-align: left;">− 0.36</td>
<td style="text-align: left;">(− 0.39, − 0.32)</td>
<td style="text-align: left;">− 0,70</td>
<td style="text-align: left;">(− 0.78, − 0.62)</td>
<td style="text-align: left;">− 0.54</td>
<td style="text-align: left;">(− 0.62, − 0.47)</td>
</tr>
<tr>
<td style="text-align: left;">State 55555</td>
<td style="text-align: left;">−  21.1</td>
<td style="text-align: left;">(−  23.4, −  19.2)</td>
<td style="text-align: left;">−  20.2</td>
<td style="text-align: left;">(− 22.1, − 18.2)</td>
<td style="text-align: left;">− 0.40</td>
<td style="text-align: left;">(− 0.48, − 0.32)</td>
<td style="text-align: left;">− 0.41</td>
<td style="text-align: left;">(− 0.50, − 0.32)</td>
<td style="text-align: left;">− 1.64</td>
<td style="text-align: left;">(− 1.93, − 1.38)</td>
<td style="text-align: left;">− 1.11</td>
<td style="text-align: left;">(− 1.37, − 0.89)</td>
</tr>
</tbody>
</table>

*DCE* discrete choice experiment, *N/A* not applicable, *QALY* quality-adjusted life year

<sup>a</sup>For standard DCE, parameter estimates and 95% credible intervals are reported on latent utility scales

</div>

For the standard DCE, estimates in Table <a href="#Tab4" data-ref-type="table">4</a> are expressed on the latent utility scale, and therefore the obtained parameter estimates cannot be directly compared to the ones obtained in the other arms. However, the difference in scale between the unstratified and severity-stratified designs is very small, as can be seen from the values for state 55555 (the worst EQ-5D-5L state) and the fact that the 95% credible intervals overlap for all parameters when comparing the models from both designs. Similar results were observed for the DCE-death estimates on the QALY scale. For DCE-duration, estimated values for state 55555 are different and 95% credible intervals for several parameters (i.e., level 4 of ‘Mobility’ and level 5 of ‘Self-care’ and ‘Anxiety/depression’) do not overlap when comparing the unstratified design with the severity-stratified design.

Figure <a href="#Fig3" data-ref-type="fig">3</a> shows scatter plots for each DCE format, comparing the values obtained by the designs with and without severity stratification. For the standard DCE and DCE-death formats, estimated values based on the severity-stratified design are close to those of the unstratified design. However, for the DCE-duration format, health state values of the severity-stratified design are higher than those of the unstratified design, especially on the range of states that are worse than death. The proportion of health states considered worse than death among 3125 health states was 56.0% for the unstratified design versus 42.8% for the severity-stratified design.

<figure id="Fig3">
<p><img src="40273_2018_694_Fig3_HTML.jpg" id="MO5" /></p>
<figcaption>Comparison of values for all EQ-5D health states between designs with and without severity-stratification. The 45° line is omitted from the graph on the left, which shows the impact of the severity-stratified restriction in the standard DCE choice task, because both sets of values are on a latent scale and adding a 45° line might be misleading as a basis for comparison. <em>DCE</em> discrete choice experiment</figcaption>
</figure>

Table <a href="#Tab5" data-ref-type="table">5</a> shows MEs by study arm to compare the in-sample and out-of-sample forecasting accuracy of the severity-stratified design with those of the unstratified design. That is, column 4 shows the ‘unstratified’ model predicting the ‘unstratified’ observed choice probabilities; column 5 shows the ‘severity-stratified’ model predicting the ‘unstratified’ observed choice probabilities; column 6 shows the ‘unstratified’ model predicting the ‘severity-stratified’ observed choice probabilities; column 7 shows the ‘severity-stratified’ model predicting the ‘severity-stratified’ observed choice probabilities.

<div id="Tab5" class="table-wrap">

<div class="caption">

Mean signed errors for predicting choice probability

</div>

<table>
<thead>
<tr>
<th rowspan="3" style="text-align: left;">Parameter estimates used</th>
<th colspan="4" style="text-align: left;">Choice sets predicted</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Unstratified choice sets</th>
<th colspan="2" style="text-align: left;">Severity-stratified choice sets</th>
</tr>
<tr>
<th style="text-align: left;">Unstratified</th>
<th style="text-align: left;">Severity-stratified</th>
<th style="text-align: left;">Unstratified</th>
<th style="text-align: left;">Severity-stratified</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Standard DCE</td>
<td style="text-align: left;">0.3446 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.1850 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  0.9972 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  1.3217 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">DCE-death</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> All health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">0.7730 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.0810 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.1181 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.1725 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">0.8205 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.6095 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.5434 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.2958 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">0.7217 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.6624 × 10<sup>− 18</sup></td>
<td style="text-align: left;">− 0.3774 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.0441 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">0.7730 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.0810 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.1181 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.1725 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Bad health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">0.0056</td>
<td style="text-align: left;">0.0130<sup>a</sup></td>
<td style="text-align: left;">−  0.0039</td>
<td style="text-align: left;">−  0.0098</td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">0.0062<sup>a</sup></td>
<td style="text-align: left;">0.0142<sup>a</sup></td>
<td style="text-align: left;">0.0043<sup>a</sup></td>
<td style="text-align: left;">0.0012</td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">0.0045</td>
<td style="text-align: left;">0.0097</td>
<td style="text-align: left;">−  0.0259</td>
<td style="text-align: left;">−  0.0331</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Medium health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">0.0015</td>
<td style="text-align: left;">−  0.0030</td>
<td style="text-align: left;">0.0103<sup>a</sup></td>
<td style="text-align: left;">0.0049</td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">−  0.0025<sup>a</sup></td>
<td style="text-align: left;">−  0.0025<sup>a</sup></td>
<td style="text-align: left;">0.0021<sup>a</sup></td>
<td style="text-align: left;">0.0020<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">0.0097</td>
<td style="text-align: left;">−  0.0044</td>
<td style="text-align: left;">0.0289<sup>a</sup></td>
<td style="text-align: left;">0.0110</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Better health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">−  0.0017</td>
<td style="text-align: left;">−  0.0087<sup>a</sup></td>
<td style="text-align: left;">0.0022</td>
<td style="text-align: left;">−  0.0028</td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">−  0.0005</td>
<td style="text-align: left;">−  0.0016<sup>a</sup></td>
<td style="text-align: left;">−  0.0044<sup>a</sup></td>
<td style="text-align: left;">−  0.0037<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">−  0.0067</td>
<td style="text-align: left;">−  0.0265<sup>a</sup></td>
<td style="text-align: left;">0.0178</td>
<td style="text-align: left;">−  0.0008</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;">DCE-duration</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> All health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">−  0.6185 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  1.2218 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.1516 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.2327 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">−  1.0474 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  2.0947 × 10<sup>− 18</sup></td>
<td style="text-align: left;">0.4598 × 10<sup>− 18</sup></td>
<td style="text-align: left;">1.2122 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">−  0.1624 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  0.2443 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  0.1796 × 10<sup>− 18</sup></td>
<td style="text-align: left;">−  0.7710 × 10<sup>− 18</sup></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Bad health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">−  <em>0.0122</em><sup>a</sup></td>
<td style="text-align: left;">0.0015</td>
<td style="text-align: left;">−  0.0200<sup>a</sup></td>
<td style="text-align: left;">−  <em>0.0052</em></td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">−  <em>0.0012</em></td>
<td style="text-align: left;">0.0009</td>
<td style="text-align: left;">−  0.0029<sup>a</sup></td>
<td style="text-align: left;">−  <em>0.0012</em><sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">−  <em>0.0347</em><sup>a</sup></td>
<td style="text-align: left;">0.0028</td>
<td style="text-align: left;">−  0.0559<sup>a</sup></td>
<td style="text-align: left;">−  <em>0.0135</em></td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Medium health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">0.0028</td>
<td style="text-align: left;">0.0151<sup>a</sup></td>
<td style="text-align: left;">−  0.0086</td>
<td style="text-align: left;">0.0035</td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">0.0038<sup>a</sup></td>
<td style="text-align: left;">0.0060<sup>a</sup></td>
<td style="text-align: left;">0.0048<sup>a</sup></td>
<td style="text-align: left;">0.0060<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">0.0007</td>
<td style="text-align: left;">0.0345<sup>a</sup></td>
<td style="text-align: left;">−  0.0365<sup>a</sup></td>
<td style="text-align: left;">−  0.0017</td>
</tr>
<tr>
<td colspan="5" style="text-align: left;"> Better health states</td>
</tr>
<tr>
<td style="text-align: left;">  All</td>
<td style="text-align: left;">0.0041</td>
<td style="text-align: left;">0.0049</td>
<td style="text-align: left;">0.0032</td>
<td style="text-align: left;">0.0038</td>
</tr>
<tr>
<td style="text-align: left;">  A–B</td>
<td style="text-align: left;">−  0.0041<sup>a</sup></td>
<td style="text-align: left;">−  0.0075<sup>a</sup></td>
<td style="text-align: left;">−  0.0074<sup>a</sup></td>
<td style="text-align: left;">−  0.0162<sup>a</sup></td>
</tr>
<tr>
<td style="text-align: left;">  B–C</td>
<td style="text-align: left;">0.0228</td>
<td style="text-align: left;">0.0355<sup>a</sup></td>
<td style="text-align: left;">0.0309<sup>a</sup></td>
<td style="text-align: left;">0.0449<sup>a</sup></td>
</tr>
</tbody>
</table>

All = choice probabilities of impaired health states (regardless of comparison tasks); A–B = choice probabilities of impaired health states in A–B comparison tasks; B–C = choice probabilities of impaired health states in B–C comparison tasks

Note, bad health states for QALY ≤ 0, medium health state for 0 \< QALY ≤ 0.5, and better health state for 0.5 \< QALY. Because the standard DCE produces values on a latent scale, the division in three severity strata was omitted for those designs

*DCE* discrete choice experiment, *QALY* quality-adjusted life year

<sup>a</sup>Significant at 5% level

</div>

For DCE-death and DCE-duration, MEs were computed by separating health states into severity ranges: bad, medium, and better health state for QALY ≤ 0, 0 \< QALY ≤ 0.5, and QALY \> 0.5, respectively. In addition, comparisons of the choice tasks were separately included: choice probabilities of impaired health states in A-B comparison tasks and B-C comparison tasks.

When we computed MEs across all health states, all six study arms produced insignificant MEs that were very close to zero because positive and negative errors offset each other. However, when we divided health states into severity ranges, some errors were found to be significantly different from zero. An expected result was that the out-of-sample predictions are more likely to show significant errors than the in-sample predictions, regardless of whether the severity stratification was applied. Beyond that, we found few noticeable differences between designs in most cases. However, for the DCE-duration, we found that the unstratified design produced significant negative errors for bad health states (i.e., column 4, italicized) while errors in the severity-stratified design were not significant (i.e., column 7, italicized), especially on B-C tasks. Also, for B-C tasks, the out-of-sample predictions produced by the severity-stratified design (0.0028) were much better than the unstratified design (− 0.0559) suggesting that the latter overestimated the willingness to trade-off life years to avoid bad health states significantly. These results suggest that the skewed health states selection for the DCE-duration introduced a downward bias on estimated values.

## Discussion

This paper investigated the effect of imposing the severity stratification on Bayesian D-efficient DCE designs created for valuing health. We found that imposing severity stratification on DCE-duration was required to ensure that the selected set of health states covered the severity range well. The model estimates derived from the severity-stratified design also demonstrated better predictive performance than unstratified designs, especially regarding the choice probability of bad health states, preventing a downward bias on the values for poor health states. In the other investigated DCE types, we find less evidence of favoritism in the selection of health states, and imposing severity stratification had no substantial effect on values. The results suggest that efficient design algorithms need to be implemented carefully in the contexts of DCE-duration studies for health valuation.

It is instructive to reflect on the reasons why it matters so much to impose severity stratification on an efficient design algorithm used to construct a DCE with duration for health valuation. The low accuracy of predicted values of poor states based on a pro-mild set of health states reveals an extrapolation issue. Extrapolation per se does not cause a bias; it only does so when the model is misspecified. Hence, our findings indicate that the model was misspecified and that we can mitigate this problem by better spreading the data, thus ensuring that the resulting QALY tariffs are less affected by extrapolation. In particular, the DCE-duration model seems to be sensitive to the assumptions made regarding duration preferences, as immediate death is not included so that the anchor point for the QALY scale is completely defined by extrapolation. The efficient optimization of the DCE design with a fixed (perfect health) comparator has aggravated the extrapolation problem, because it is efficient to include a skewed selection of relatively healthy health states. This reflects the special characteristic of DCE-duration models that utilities are derived using a multiplicative utility function with life years acting as a multiplier of the health state utility. Issues with utility dominance may arise in this context more easily than in standard applications of DCEs.

A limitation of this study is that it was beyond its scope to explore the extent to which our results are specific to the matched pairwise choice format that was used in this study. Having full health as a fixed alternative and the relatively long duration (i.e., 10 years) assumed for the impaired health states might have exaggerated issues that led to skewed selection of health states. Furthermore, we have not considered the merit of efficient designs in this context relative to other design generating approaches that do not require the implementation of strategies to enhance the spread of the data. The need to impose severity stratification makes construction of efficient designs for DCE-duration studies more difficult, and hence may influence the trade-offs between pros and cons of efficient versus other designs. Third, we did not find evidence of health state selection in the DCE-death approach, but we do not know if this result holds when valuing health states derived from other descriptive systems (e.g., disease-specific ones, where the mass of health states may be on a different location on the full health–dead scale). Fourth, assuming the normal distribution for parameters’ distribution may be inappropriate to specify the monotonic attribute-level effect due to its unbounded nature. Using more flexible distribution with a fixed bound can be considered to avoid the potential violation of monotonicity. Last, we measured respondents’ preference on the length of life using both months and years as the temporal unit in the perfect health state and converted months to years in the analysis. However, respondents may not treat values in months and the equivalent amount of years in the same way when valuing health states; thus, be cautious in further study \[28\].

## Conclusion

We conclude that differences in how well selected health states span the severity range can explain part of the differences in values across DCE (duration) studies. Imposing ‘severity stratification’ on DCE-duration designs ensures robustness of the results against extrapolation from a misspecified model. Until we know how widespread associated extrapolation issues are in reported value sets, we need to be careful in the use of DCE-derived health state values.

### Data Availability Statement

The datasets generated for and/or analyzed during the current study are available from the corresponding author on reasonable request.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

<div class="caption">

Supplementary material 1 (PDF 300 kb)

</div>

#### Funding

This work has received financial support from the EuroQol Research Foundation grant number 2015300.

### Acknowledgements

Sesil Lim conducted the statistical analyses and drafted the first version of the manuscript. Marcel F. Jonker conceptualized the severity stratification approach, developed the study design, managed the data collection, and helped review and edit the manuscript. Mark Oppe, Bas Donkers, and Elly Stolk supported the development of the study design, analysis of the data, and interpretation of results as well as helped in the detailed review and editing of the manuscript. The views expressed in this work are those of the individual authors and do not necessarily reflect the views of the EuroQol Group.

#### Conflict of Interest

Marcel F. Jonker, Mark Oppe, and Elly Stolk are members of the EuroQol Group. Elly Stolk and Mark Oppe are employees of the EuroQol Research Foundation. Sesil Lim and Bas Donkers have no conflict of interest to declare.

## References

1. Bijlenga D, Birnie E, Bonsel GJ. Feasibility, reliability, and validity of three health-state valuation methods using multiple-outcome vignettes on moderate-risk pregnancy at term. Value Health. 2009;12(5):821–827. doi:10.1111/j.1524-4733.2009.00503.x

2. Stolk EA, Oppe M, Scalone L, Krabbe PF. Discrete choice modeling for the quantification of health states: the case of the EQ-5D. Value Health. 2010;13(8):1005–1013. doi:10.1111/j.1524-4733.2010.00783.x

3. Norman R, Viney R, Brazier J, Burgess L, Cronin P, King M, Ratcliffe J, Street D. Valuing SF-6D health states using a discrete choice experiment. Med Decis Making. 2014;34(6):773–786. doi:10.1177/0272989X13503499

4. Norman R, Mulhern B, Viney R. The impact of different DCE-based approaches when anchoring utility scores. Pharmacoeconomics. 2016;34(8):805–814. doi:10.1007/s40273-016-0399-7

5. Craig BM, Greiner W, Brown DS, Reeve BB. Valuation of child health-related quality of life in the United States. Health Econ. 2016;25(6):768–777. doi:10.1002/hec.3184

6. Jonker MF, Attema AE, Donkers B, Stolk EA, Versteegh MM. Are health state valuations from the general public biased? A test of health state reference dependency using self-assessed health and an efficient discrete choice experiment. Health Econ. 2017;26(12):1534–1547. doi:10.1002/hec.3445

7. Dolan P. Modeling valuations for EuroQol health states. Med Care. 1997;35:1095–1108. doi:10.1097/00005650-199711000-00002

8. Bridges JF, Hauber AB, Marshall D, Lloyd A, Prosser LA, Regier DA, Johnson FR, Mauskopf J. Conjoint analysis applications in health–a checklist: a report of the ISPOR good research practices for conjoint analysis task force. Value Health. 2011;14(4):403–413. doi:10.1016/j.jval.2010.11.013

9. Johnson FR, Lancsar E, Marshall D, Kilambi V, Mühlbacher A, Regier DA, Bresnahan BW, Kanninen B, Bridges JF. Constructing experimental designs for discrete-choice experiments: report of the ISPOR conjoint analysis experimental design good research practices task force. Value Health. 2013;16(1):3–13. doi:10.1016/j.jval.2012.08.2223

10. Rose JM, Bliemer MC. Constructing efficient stated choice experimental designs. Transp Rev. 2009;29(5):587–617. doi:10.1080/01441640902827623

11. Bansback N, Hole AR, Mulhern B, Tsuchiya A. Testing a discrete choice experiment including duration to value health states for large descriptive systems: addressing design and sampling issues. Soc Sci Med. 2014;114:38–48. doi:10.1016/j.socscimed.2014.05.026

12. Mulhern B, Bansback N, Hole AR, Tsuchiya A. Using discrete choice experiments with duration to model EQ-5D-5L health state preferences. Med Decis Making. 2016;37(3):285–297. doi:10.1177/0272989X16670616

13. Flynn TN, Bilger M, Malhotra C, Finkelstein EA. Are efficient designs used in discrete choice experiments too difficult for some respondents? A case study eliciting preferences for end-of-life care. Pharmacoeconomics. 2016;34(3):273–284. doi:10.1007/s40273-015-0338-z

14. Dellaert BGC, Donkers B, Van Soest AHO. Complexity effects in choice experiment–based models. J Marketing Res. 2012;49(3):424–434. doi:10.1509/jmr.09.0315

15. Jonker MF, Donkers B, De Bekker-Grob EW, Stolk EA. The effect of level overlap and color coding on attribute non-attendance in discrete choice experiments. Value Health. 2017. doi:10.1016/j.jval.2017.10.002

16. Norman R, Viney R, Aaronson NK. Using a discrete choice experiment to value the QLU-C10D: feasibility and sensitivity to presentation format. Qual Life Res. 2016;25:637–649. doi:10.1007/s11136-015-1115-3

17. Walker JL, Wang Y, Thorhauge M, Ben-Akiva M. D-efficient or deficient? A robustness analysis of stated choice experimental designs. Theory Decis. 2018;84(2):215–238. doi:10.1007/s11238-017-9647-3

18. Bliemer MCJ, Rose JM. Experimental design influences on stated choice outputs: an empirical study in air travel choice. Transport Res A-Policy Pract. 2011;45:63–79. doi:10.1016/j.tra.2010.09.003

19. Huber J, Zwerina K. The importance of utility balance in efficient choice designs. J Marketing Res. 1996;33(3):307–317. doi:10.2307/3152127

20. Jonker MF, Donkers B, De Bekker-Grob EW, Stolk E. Advocating a paradigm shift in health-state valuations: the estimation of time-preference corrected QALY tariffs. Value Health. 2018. doi:10.1016/j.jval.2018.01.016

21. Sándor Z, Wedel M. Heterogeneous conjoint choice designs. J Marketing Res. 2005;42(2):210–218. doi:10.1509/jmkr.42.2.210.62285

22. Bliemer MC, Rose JM. Construction of experimental designs for mixed logit models allowing for correlation across choice observations. Transport Res B-Meth. 2010;44(6):720–734. doi:10.1016/j.trb.2009.12.004

23. Bezanson J, Karpinski S, Shah VB, Edelman A. Julia: a fast dynamic language for technical computing. 2012. https://arxiv.org/abs/1209.5145v1. Accessed 31 May 2018.

24. Hensher DA, Greene WH. The mixed logit model: the state of practice. Transportation. 2003;30:133–176. doi:10.1023/A:1022558715350

25. Rossi P, McCulloch R. bayesm: Bayesian inference for marketing/micro-econometrics. R package version 3.1-0.1. 2017. https://cran.r-project.org/web/packages/bayesm/bayesm.pdf. Accessed 8 Feb 2018.

26. Plummer M. Package ‘coda’. R package version 0.91-1. 2016. https://cran.r-project.org/web/packages/coda/coda.pdf. Accessed 1 July 2018.

27. Versteegh MM, Vermeulen KM, Evers SMAA, De Wit GA, Prenger R, Stolk EA. Dutch tariff for the five-level version of EQ-5D. Value Health. 2016;19(4):343–352. doi:10.1016/j.jval.2016.01.003

28. Jakubczyk M, Craig BM, Barra M, Groothuis-Oudshoorn CGM, Hartman JD, Huynh E, Ramos-Goñi JM, Stolk EA, Rand K. Choice defines value: a predictive modeling competition in health preference research. Value Health. 2018;21(2):229–238. doi:10.1016/j.jval.2017.09.016

[^1]: Experimental designs to make respondents compare two health states within a vast gap of life years (i.e., 10 years in impaired health state vs. 2 months in the perfect health) may make the model sensitive to potential non-attendance to duration then inflate the impact of severely impaired health states. To clear this concern, we re-analyzed parameter values for the DCE-duration format excluding choice tasks containing 2 months of duration in perfect health (i.e., choice tasks with the biggest differences in duration). Our findings were qualitatively the same and quantitatively also almost identical.

[^2]: We used the mixed logit rather than other discrete choice models (i.e., conditional logit model) because it (1) does not exhibit the independence from irrelevant alternatives (IIA) property and the restrictive substitution pattern, (2) allows the correlation among coefficients, and (3) can take potential correlated responses across observations from the same individual into account in the repeated choices situation \[24\].

[^3]: We also examined mean squared errors (MSE) by study arms (see the electronic supplementary material) to provide a full insight for the effect of imposing the severity-stratified restriction.

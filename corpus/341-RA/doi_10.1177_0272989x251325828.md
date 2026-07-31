---
project_id: "341-RA"
work_id: "doi:10.1177/0272989x251325828"
doi: "10.1177/0272989X251325828"
pmid: "40110719"
pmcid: "PMC11992645"
title: "Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be"
journal: "Medical Decision Making"
publication_date: "2025-03-20"
volume: "45"
issue: "4"
authors:
  - name: "Eleanor M Pullenayegum"
    affiliation_ids:
      - "aff1-0272989X251325828"
      - "aff2-0272989X251325828"
  - name: "Marcel F Jonker"
    affiliation_ids:
      - "aff3-0272989X251325828"
  - name: "Henry Bailey"
    affiliation_ids:
      - "aff4-0272989X251325828"
  - name: "Bram Roudijk"
    affiliation_ids:
      - "aff5-0272989X251325828"
affiliations:
  - id: "aff1-0272989X251325828"
    name: "Child Health Evaluative Sciences, The Hospital for Sick Children, Toronto, ON, Canada"
  - id: "aff2-0272989X251325828"
    name: "Dalla Lana School of Public Health, University of Toronto, Toronto, Canada"
  - id: "aff3-0272989X251325828"
    name: "Erasmus School of Health Policy & Management, Erasmus Centre for Health Economics and Erasmus Choice Modelling Centre, Erasmus University Rotterdam, The Netherlands"
  - id: "aff4-0272989X251325828"
    name: "Department of Economics & HEU Centre for Health Economics, the University of the West Indies, St Augustine, Trinidad, West Indies"
  - id: "aff5-0272989X251325828"
    name: "EuroQol Research Foundation, Rotterdam, The Netherlands"
licence: "cc-by"
source_file: "input/projects/341-RA/papers/doi_10.1177_0272989x251325828.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11992645/fullTextXML"
source_method: "epmc_xml"
source_sha256: "036bafe3f84a51fb7ddc2eb1b43dfb5d1f875d00818b0cfea54a6bd2b4138efe"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be

## Abstract

### Objectives

Discrete choice experiments (DCEs) as a valuation method require preferences to be anchored on the quality-adjusted life-year scale, usually through tasks involving choices between immediate death and various impaired health states or between health states with varying durations of life. We sought to determine which anchoring approach aligns best with the composite time tradeoff (cTTO) method, with a view to informing a valuation protocol that uses DCEs in place of the cTTO.

### Methods

A total of 970 respondents from Trinidad and Tobago completed a DCE with duration survey. Tasks involved choosing between 2 lives with identical durations, followed by a third option, representing either full health for a number of years or immediate death. Data were analyzed using mixed logit models, both with and without exponential discounting for time preferences.

### Results

Assuming linear time preferences, the estimated utility of immediate death was −2.1 (95% credible interval \[CrI\] −3.2 to −1.2) versus −0.28 (95% CrI −0.47, −0.10) when allowing for nonlinear time preferences. Under linear time preferences, the predicted health-state values anchored on duration had range (−1.03, 1) versus (0.34, 1) when anchored on immediate death. The ranges under nonlinear time preferences were (−0.54, 1) versus (−0.22, 1). The estimated discount parameter was 23% (95% CrI 22% to 25%).

### Conclusions

The nonzero discount parameter indicates that time preferences were nonlinear. Nonlinear time preferences anchored on duration provided the closest match to the benchmark EQ-VT cTTO values in Trinidad and Tobago, whose range was (−0.6, 1). Thus, DCE with duration can provide similar values to cTTO provided that nonlinear time preferences are accounted for and anchoring is based on duration.

### Highlights

- Time preferences for health states in Trinidad and Tobago were nonlinear.

- In discrete choice tasks, we show that immediate death has a utility less than zero.

- DCE utilities under nonlinear time preferences with anchoring on duration agreed well with cTTO utilities.

**Keywords:** health state valuation, discrete choice experiment

Received 2024 Aug 19; Accepted 2025 Jan 23; Issue date 2025 May.

Quality-adjusted life-years are a key component in economic evaluations in many countries<sup>1–4</sup> and typically rely on instruments such as the EQ-5D-5L,<sup> 5 </sup> SF-6D,<sup> 6 </sup> or HUI3<sup> 7 </sup> to elicit health utilities. These instruments require a value set that specifies the population utility associated with each health state captured by the instrument. Discrete choice experiments (DCEs) have emerged as a promising approach to creating such value sets, as they can be done online and do not need to be administered by an interviewer.<sup>8,9</sup> This makes them an attractive alternative to the widely used composite time tradeoff (cTTO),<sup> 10 </sup> which needs to be administered by a trained interviewer. It is thus of interest to examine whether DCEs can yield similar results to cTTO tasks: if this is the case, then costly interviewer-administered cTTO protocols could be replaced by DCEs.

When respondents choose between 2 health states without duration, preferences can be inferred on a latent scale (i.e., up to a linear transform). Some additional information is required to anchor the utilities on the full-health–dead scale (where full health has a utility of 1 and being dead has a utility of 0). These anchors can be either external<sup>11,12</sup> or based on additional discrete choice tasks. This latter option is the focus of this article. There are 2 types of additional tasks that can be used to anchor the latent utilities: a discrete form of TTO anchoring that involves trading off an impaired health state of a specified duration with full health for a shorter duration or trading off impaired health states of a specified duration with immediate death.

Under a QALY model, both being dead for any duration and a health state of duration zero should have a utility of zero; see Roudijk et al.<sup> 13 </sup> for a detailed theoretical justification. Several studies have assumed that immediate death also has a utility of zero<sup>8,9</sup>; however, there is empirical evidence that this is not the case and that its utility is lower than zero.<sup>14,15</sup> This finding is consistent with qualitative findings from TTO interviews, which suggest that there is both a discontinuity in preferences as durations approach zero<sup>16,17</sup> as well as heterogeneity in how people interpret immediate death.

In dealing with either of these issues, a third issue must be contended with: time preferences are nonlinear. There is empirical evidence that respondents discount future health status in favor of improved health now.<sup>18,19</sup> However, estimating this discount rate requires careful selection of discrete choice tasks to make the parameter identifiable.<sup> 20 </sup>

An important limitation in previous work exploring anchoring on immediate death is that the DCE tasks were not designed to permit estimation of the discount parameter. It is therefore currently unknown whether anchoring latent utilities from DCEs on immediate death remains problematic when incorporating discounting into the estimation procedure.

Two valuation studies of the EQ-5D-5L in Trinidad and Tobago were recently published. The first valuation study used the international EQ-5D-5L EQ-VT valuation protocol based on cTTO tasks,<sup> 10 </sup> whereas the second used DCE with duration following a protocol<sup>19,21,22</sup> that permits the estimation of nonlinear time preferences and compared the results with that those obtained using the EQ-VT valuation protocol.<sup> 23 </sup>

In this work, we use data collected in the Trinidad and Tobago DCE with a duration valuation study to examine whether immediate death continues to have a lower utility than a state of duration zero after accounting for discounting. We compute value sets anchoring on a duration of zero and anchoring on immediate death and examine how well the range of the value sets agrees with the range of the value set based on cTTO,<sup> 23 </sup> to inform recommendations on how to anchor latent scale DCE utilities.

## Methods

### Population

This study is a secondary analysis of an existing sample of 970 respondents included in the Trinidad and Tobago DCE with duration study.<sup> 24 </sup> This study used quota sampling to achieve a population that was representative of the general population in terms of age, sex, and geography. Recruitment was through a panel company, which used both an internet panel (e-mailed links to the survey) and recruitment in public places (e.g., libraries, transit hubs) with survey completion done on the recruiter’s laptop. Ethical approval was obtained from the University of The West Indies (exemption letter CREC-SA.1468/03/2022 dated March 7, 2022).

### Task Types

Each respondent completed 1 set of 18 split triplets,<sup> 25 </sup> 15 of which involved tradeoffs with full health and 3 of which involved tradeoffs with immediate death. Each triplet began with a pair of health states of equal duration (life A and life B), from which the respondent was asked to choose their preference. To simplify the task, life A and life B differed in just 3 of the 5 EQ-5D-5L dimensions; the other 2 dimensions were the same in life A and life B.

Regardless of the stated preference, in the second half of the triplet, life A was blurred and the respondent was asked to choose between life B and life C. In those split triplets involving tradeoffs with full health, life C was defined as full health but with a shorter duration than life B; this choice is thus a discrete version of a traditional TTO task. In those split triplets involving tradeoffs with immediate death, life C was immediate death.

### DCE Design

A near-orthogonal design was used initially, the responses to which (*n* = 211) were analyzed to create a more efficient design using the TPC-QD software package.<sup> 20 </sup> The design was further updated at intervals of 200 respondents until the priors used to generate the design did not change substantially between updates. Durations were whole years from 1 up to and including 15, with an additional duration of 6 mo. Each design contained 10 subdesigns with 18 split triplets as described above. Respondents were randomly assigned to 1 of the 18 split triplets, with the order of lives A and B also randomly assigned.

### Analytic Plan

#### Utility model

We assumed a main effects model and subject-specific regression coefficients for the latent utilities to account for between-subject heterogeneity in preferences. Specifically, letting $`U_{ijt}`$ be the latent utility for respondent *i* valuing health state *j* with a duration *t*, we used a mixed logit model with discounting, that is,

``` math
U_{ijt} = X_{j}\beta_{i}D(t;\rho) + \beta_{{ip} + 1}I({state}\ j\ {is}\ {immediate}\ {death}) + \sigma\epsilon_{ijt}
```

where *X<sub>j</sub>* is a *p*-dimensional row vector of attributes of health state *j* whose first element is 1 to provide an intercept, $`\left. \epsilon_{ijt} \right.\sim`$ iid Gumbel, $`\left. \beta_{i} \right.\sim{MVN}(\beta,\Sigma_{\beta})`$, I() denotes an indicator function, and $`D(t;\rho`$) is the discounted duration under exponential discounting with discount parameter ρ, that is, $`D(t;\rho) = \ \frac{1 - \exp(\rho t)}{\exp\left\{ \rho \right\} - 1}`$ for ρ \> 0 and *D*(*t*; ρ) = *t* for ρ = 0.

We assumed a main effects functional form for the design matrix, specifically *X<sub>j</sub>* = (1, MO2<sub>j</sub>, MO3<sub>j</sub>, MO4<sub>j</sub>, MO5<sub>j</sub>, SC2<sub>j</sub>, SC3<sub>j</sub>, SC4<sub>j</sub>, SC5<sub>j</sub>, UA2<sub>j</sub>, UA3<sub>j</sub>, UA4<sub>j</sub>, UA5<sub>j</sub>, PD2<sub>j</sub>, PD3<sub>j</sub>, PD4<sub>j</sub>, PD5<sub>j</sub>, AD2<sub>j</sub>, AD3<sub>j</sub>, AD4<sub>j</sub>, AD5<sub>j</sub>), where MO2<sub>j</sub>, MO3<sub>j</sub>, MO4<sub>j</sub>, MO5<sub>j</sub> are indicators (0 = no, 1 = yes) for whether mobility in health state *j* is at level 2, 3, 4, or 5, respectively, and similarly for self-care, usual activities, pain/discomfort, and anxiety/depression.

#### Discount parameter

We fitted 2 models. The first assumed no discounting, that is, ρ = 0, whereas the second used a uniform(0,1) prior for ρ.

#### Estimation

Models were estimated using OpenBugs, using 3 chains, a burn-in of 50,000 and 50,000 draws from the posterior distributions. Convergence was evaluated based on inspection of the chains and diagnostics proposed by Geweke.<sup> 26 </sup> The BUGS models, including the exact specification of the prior distributions, are included in the [online supplemental](https://journals.sagepub.com/doi/suppl/10.1177/0272989X251325828).

#### Anchoring

The fitted models do not estimate the coefficients β but rather scaled versions that must be anchored. Specifically, the fitted models yield estimates of $`\Sigma_{\beta}/\left. \sqrt{}2\sigma \right.`$, $`\beta^{*} = \beta/\left. \sqrt{}2\sigma \right.`$, and ρ. To anchor the utilities to the full health–dead scale, we have 2 options:

1.  Option 1 is to assume that immediate death has a utility of zero. Since full health has a utility of 1, the difference in utility between full health and immediate death is 1. Referring back to equation (1) for the anchored coefficients, we have $`\beta_{1} - \beta_{p + 1} = 1`$; it then follows that $`\beta_{1}^{*} - \beta_{p + 1}^{*}\  = \ 1/\sqrt{2}\sigma`$ so that $`\beta = \beta^{*}/(\beta_{1}^{*} - \ \beta_{p + 1}^{*})`$.

2.  Option 2 is to anchor on duration and note that since full health has a utility of 1 by definition, we have $`\beta_{1}`$ = 1, and thus, $`\beta_{1}^{*} = \ 1/\left. \sqrt{}2\sigma \right.`$ so $`\beta = \ \beta^{*}/\beta_{1}^{*}.`$

We anchored the utilities using each option in turn.

## Results

As can be seen from <a href="#table1-0272989X251325828" data-ref-type="table">Table 1</a>, both the choice of anchor and the choice of time preferences affect the coefficients.

<div id="table1-0272989X251325828" class="table-wrap">

<div class="caption">

Disutilities (Standard Errors) under Linear and Nonlinear Time Preferences and with Anchoring on Either Immediate Death or Duration

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: center;">Linear Time Preferences</th>
<th colspan="2" style="text-align: center;">Nonlinear Time Preferences</th>
<th rowspan="3" style="text-align: center;">cTTO</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th colspan="2" style="text-align: center;">Anchored on</th>
<th colspan="2" style="text-align: center;">Anchored on</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: center;">Immediate Death</th>
<th style="text-align: center;">Duration</th>
<th style="text-align: center;">Immediate Death</th>
<th style="text-align: center;">Duration</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobility level 2</td>
<td style="text-align: left;">0.021<br />
(0.015, 0.028)</td>
<td style="text-align: left;">0.065<br />
(0.047, 0.088)</td>
<td style="text-align: left;">0.025<br />
(0.015, 0.036)</td>
<td style="text-align: left;">0.032<br />
(0.019, 0.046)</td>
<td style="text-align: left;">0.014<br />
(0.000, 0.028)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility level 3</td>
<td style="text-align: left;">0.048<br />
(0.038, 0.060)</td>
<td style="text-align: left;">0.146<br />
(0.115, 0.188)</td>
<td style="text-align: left;">0.075<br />
(0.061, 0.090)</td>
<td style="text-align: left;">0.095<br />
(0.078, 0.113)</td>
<td style="text-align: left;">0.058<br />
(0.033, 0.083)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility level 4</td>
<td style="text-align: left;">0.095<br />
(0.079, 0.114)</td>
<td style="text-align: left;">0.29<br />
(0.232, 0.368)</td>
<td style="text-align: left;">0.169<br />
(0.147, 0.193)</td>
<td style="text-align: left;">0.215<br />
(0.191, 0.240)</td>
<td style="text-align: left;">0.162<br />
(0.135, 0.189)</td>
</tr>
<tr>
<td style="text-align: left;">Mobility level 5</td>
<td style="text-align: left;">0.153<br />
(0.128, 0.187)</td>
<td style="text-align: left;">0.469<br />
(0.384, 0.589)</td>
<td style="text-align: left;">0.284<br />
(0.250, 0.322)</td>
<td style="text-align: left;">0.361<br />
(0.328, 0.397)</td>
<td style="text-align: left;">0.357<br />
(0.330, 0.384)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care level 2</td>
<td style="text-align: left;">0.026<br />
(0.020, 0.034)</td>
<td style="text-align: left;">0.080<br />
(0.059, 0.108)</td>
<td style="text-align: left;">0.031<br />
(0.020, 0.042)</td>
<td style="text-align: left;">0.039<br />
(0.025, 0.054)</td>
<td style="text-align: left;">0.029<br />
(0.015, 0.043)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care level 3</td>
<td style="text-align: left;">0.037<br />
(0.030, 0.047)</td>
<td style="text-align: left;">0.115<br />
(0.088, 0.151)</td>
<td style="text-align: left;">0.057<br />
(0.044, 0.070)</td>
<td style="text-align: left;">0.072<br />
(0.056, 0.088)</td>
<td style="text-align: left;">0.074<br />
(0.052, 0.096)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care level 4</td>
<td style="text-align: left;">0.084<br />
(0.070, 0.102)</td>
<td style="text-align: left;">0.256<br />
(0.205, 0.324)</td>
<td style="text-align: left;">0.142<br />
(0.124, 0.163)</td>
<td style="text-align: left;">0.181<br />
(0.160, 0.203)</td>
<td style="text-align: left;">0.159<br />
(0.134, 0.184)</td>
</tr>
<tr>
<td style="text-align: left;">Self-care level 5</td>
<td style="text-align: left;">0.121<br />
(0.102, 0.145)</td>
<td style="text-align: left;">0.369<br />
(0.295, 0.467)</td>
<td style="text-align: left;">0.223<br />
(0.196, 0.253)</td>
<td style="text-align: left;">0.283<br />
(0.257, 0.313)</td>
<td style="text-align: left;">0.221<br />
(0.197, 0.245)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities level 2</td>
<td style="text-align: left;">0.023<br />
(0.015, 0.033)</td>
<td style="text-align: left;">0.069<br />
(0.050, 0.090)</td>
<td style="text-align: left;">0.017<br />
(0.006, 0.028)</td>
<td style="text-align: left;">0.022<br />
(0.007, 0.036)</td>
<td style="text-align: left;">0.016<br />
(0.002, 0.030)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities level 3</td>
<td style="text-align: left;">0.037<br />
(0.027, 0.049)</td>
<td style="text-align: left;">0.111<br />
(0.089, 0.142)</td>
<td style="text-align: left;">0.045<br />
(0.032, 0.059)</td>
<td style="text-align: left;">0.058<br />
(0.041, 0.074)</td>
<td style="text-align: left;">0.087<br />
(0.065, 0.109)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities level 4</td>
<td style="text-align: left;">0.069<br />
(0.056, 0.087)</td>
<td style="text-align: left;">0.210<br />
(0.175, 0.262)</td>
<td style="text-align: left;">0.107<br />
(0.090, 0.124)</td>
<td style="text-align: left;">0.135<br />
(0.116, 0.156)</td>
<td style="text-align: left;">0.145<br />
(0.123, 0.167)</td>
</tr>
<tr>
<td style="text-align: left;">Usual activities level 5</td>
<td style="text-align: left;">0.098<br />
(0.081, 0.123)</td>
<td style="text-align: left;">0.300<br />
(0.251, 0.374)</td>
<td style="text-align: left;">0.166<br />
(0.144, 0.189)</td>
<td style="text-align: left;">0.210<br />
(0.187, 0.236)</td>
<td style="text-align: left;">0.216<br />
(0.191, 0.241)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort level 2</td>
<td style="text-align: left;">0.029<br />
(0.022, 0.037)</td>
<td style="text-align: left;">0.089<br />
(0.064, 0.118)</td>
<td style="text-align: left;">0.046<br />
(0.035, 0.059)</td>
<td style="text-align: left;">0.059<br />
(0.045, 0.073)</td>
<td style="text-align: left;">0.026<br />
(0.014, 0.038)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort level 3</td>
<td style="text-align: left;">0.046<br />
(0.037, 0.057)</td>
<td style="text-align: left;">0.140<br />
(0.110, 0.181)</td>
<td style="text-align: left;">0.078<br />
(0.064, 0.093)</td>
<td style="text-align: left;">0.099<br />
(0.083, 0.116)</td>
<td style="text-align: left;">0.102<br />
(0.077, 0.127)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort level 4</td>
<td style="text-align: left;">0.101<br />
(0.083, 0.122)</td>
<td style="text-align: left;">0.308<br />
(0.246, 0.390)</td>
<td style="text-align: left;">0.181<br />
(0.157, 0.209)</td>
<td style="text-align: left;">0.230<br />
(0.205, 0.258)</td>
<td style="text-align: left;">0.316<br />
(0.291, 0.341)</td>
</tr>
<tr>
<td style="text-align: left;">Pain/discomfort level 5</td>
<td style="text-align: left;">0.153<br />
(0.128, 0.186)</td>
<td style="text-align: left;">0.469<br />
(0.378, 0.591)</td>
<td style="text-align: left;">0.287<br />
(0.250, 0.328)</td>
<td style="text-align: left;">0.365<br />
(0.329, 0.403)</td>
<td style="text-align: left;">0.541<br />
(0.510, 0.572)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression level 2</td>
<td style="text-align: left;">0.030<br />
(0.023, 0.038)</td>
<td style="text-align: left;">0.093<br />
(0.071, 0.122)</td>
<td style="text-align: left;">0.042<br />
(0.031, 0.053)</td>
<td style="text-align: left;">0.053<br />
(0.039, 0.067)</td>
<td style="text-align: left;">0.024<br />
(0.012, 0.036)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression level 3</td>
<td style="text-align: left;">-0.060<br />
(0.050, 0.072)</td>
<td style="text-align: left;">0.184<br />
(0.140, 0.238)</td>
<td style="text-align: left;">0.100<br />
(0.084, 0.117)</td>
<td style="text-align: left;">0.127<br />
(0.109, 0.146)</td>
<td style="text-align: left;">0.057<br />
(0.033, 0.081)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression level 4</td>
<td style="text-align: left;">0.114<br />
(0.096, 0.136)</td>
<td style="text-align: left;">0.349<br />
(0.274, 0.446)</td>
<td style="text-align: left;">0.205<br />
(0.179, 0.234)</td>
<td style="text-align: left;">0.261<br />
(0.233, 0.291)</td>
<td style="text-align: left;">0.168<br />
(0.144, 0.192)</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety/depression level 5</td>
<td style="text-align: left;">0.136<br />
(0.115, 0.162)</td>
<td style="text-align: left;">0.418<br />
(0.328, 0.533)</td>
<td style="text-align: left;">0.255<br />
(0.224, 0.290)</td>
<td style="text-align: left;">0.324<br />
(0.292, 0.360)</td>
<td style="text-align: left;">0.272<br />
(0.250, 0.294)</td>
</tr>
<tr>
<td style="text-align: left;">Immediate death</td>
<td style="text-align: left;">n/a</td>
<td style="text-align: left;">2.102<br />
(1.159, 3.210)</td>
<td style="text-align: left;">n/a</td>
<td style="text-align: left;">0.275<br />
(0.099, 0.469)</td>
<td style="text-align: left;">n/a</td>
</tr>
</tbody>
</table>

</div>

Time preferences were not linear; the estimated discount rate parameter has a posterior mean of 23.4% with a 95% credible interval (CrI) of 21.7% to 25.1%. Assuming linear time preferences (i.e., fixing the discount parameter at zero) generally led to smaller disutilities when anchoring on immediate death, while it led to larger disutilities when anchoring on a duration of zero (<a href="#table1-0272989X251325828" data-ref-type="table">Table 1</a>).

Anchoring on immediate death led to smaller disutilities than anchoring on zero duration regardless of whether or not time preferences were assumed to be linear, although the effect was more pronounced under linear time preferences. See <a href="#table1-0272989X251325828" data-ref-type="table">Table 1</a> for tabulated regression coefficients.

Furthermore, when time preferences were assumed to be linear and anchoring was on duration, immediate death had a posterior mean utility of −2.1 (95% CrI −3.2 to −1.2). This increased substantially to −0.28 (95% CrI −0.47, −0.10) on allowing for nonlinear time preferences (<a href="#table1-0272989X251325828" data-ref-type="table">Table 1</a>).

The worst health state had an estimated utility of 0.34 (95% CrI 0.20, 0.44) with linear time preferences anchored on immediate death, −1.03 (95% CrI −1.54, −0.65) with linear time preferences anchored in duration, −0.21 (95% CrI −0.37, −0.08) with nonlinear time preferences anchored on immediate death, and −0.54 (95% CrI −0.69, −0.41) with nonlinear time preferences anchored on duration (<a href="#fig1-0272989X251325828" data-ref-type="fig">Figure 1</a>). For comparison, the reported utility for the worst health state using cTTO was −0.61. Correspondence between the health state utilities under cTTO and DCE are shown in <a href="#fig2-0272989X251325828" data-ref-type="fig">Figure 2</a>, with nonlinear time preferences anchored on duration providing the closest correspondence.

<figure id="fig1-0272989X251325828">
<p><img src="10.1177_0272989X251325828-fig1.jpg" /></p>
<p><img src="10.1177_0272989X251325828-fig1.gif" /></p>
<figcaption>Length of the quality-adjusted life-year (QALY) scale under different time preferences and anchor choices.</figcaption>
</figure>

<figure id="fig2-0272989X251325828">
<p><img src="10.1177_0272989X251325828-fig2.jpg" /></p>
<p><img src="10.1177_0272989X251325828-fig2.gif" /></p>
<figcaption>Comparison of discrete choice experiment (DCE)–based tariffs to the composite time tradeoff (cTTO) tariff.</figcaption>
</figure>

## Discussion

A unique contribution of this article is that we have compared anchoring on duration versus anchoring on immediate death while accounting for nonlinear time preferences. Our findings in a general population sample from Trinidad and Tobago are that, first, immediate death does not have a utility of zero (this is true regardless of whether linear time preferences are assumed, although the utility is closer to zero on assuming nonlinear time preferences); second, that time preferences are nonlinear; and third, that when comparing the 4 DCE QALY tariffs with the cTTO tariff, assuming nonlinear time preferences and anchoring on duration yields close agreement, whereas the other 4 choices yield poor agreement.

Anchoring on immediate death resulted in utilities estimated through DCEs exceeding the cTTO utilities. Since the mixed logit attributes a coefficient for immediate death that is less than zero, when the utility scale is anchored on immediate death, a zero duration will be given a utility that is greater than 0 (since immediate death is placed at zero, a duration of zero is positioned above zero), and therefore, the preferences for the EQ-5D-5L health states are shifted toward 1. Anchoring on a duration of zero and using linear time preferences led to DCE utilities that were in most cases lower than cTTO utilities. It is unclear why this is the case; what is clear is that failing to take the curvature in the time preferences into account when determining the anchor point for zero duration results in too many health states valued below 0.

The nonlinear time preferences we observed have also been noted in a number of valuation studies using both DCE<sup>18,19,27</sup> and TTO,<sup>28–30</sup> and a greater impact for DCE-based valuation over TTO-based valuation has been hypothesized.<sup> 19 </sup> Mistakenly assuming linear time preferences led to a utility scale ranging from 0.338 to 1 when anchoring on immediate death or to a range of −1.026 to 1 when anchoring on a duration of zero (with immediate death having an estimated utility of −2.1). The utility range on anchoring on immediate death, and the utility attached to immediate death are, in our opinion, unreasonable. Thus, the assumption of linear time preferences is not only empirically refuted by the estimated discount parameter having a posterior distribution with most of its mass away from zero but also leads to a value set that lacks face validity. This has important implications for the design of DCE studies incorporating duration: specifically, the choice tasks need to be selected in such a way as to make the discount parameter identifiable. When using a D-efficient design, this corresponds to selecting an analytic model that includes nonlinear time preferences and using design updates as data accumulates to optimize information about the discount parameter; see Jonker and Bliemer<sup> 20 </sup> for details on how to achieve this.

A shifting of preferences for immediate death away from zero on anchoring the tariff using duration has also been noted elsewhere. For example, immediate death was reported to have utilities of −0.46 (95% CI −0.79, −0.02) and −3.94 (−5.56, −2.36) in Australian studies of the EQ-5D-5L and SF-6D, respectively, on using the mixed logit model.<sup> 15 </sup> Under a conditional logit model, anchoring on immediate death has been noted to lead to a shorter scale than anchoring on full health.<sup> 31 </sup> Notably, however, these analyses all assumed linear time preferences.

There are several explanations for the shift of immediate death away from zero. While equivalence to death has been formally defined,<sup> 32 </sup> the processes by which respondents decide whether something is better or worse than dead do not always match this definition<sup> 33 </sup> and are, moreover, sensitive to framing.<sup> 34 </sup>

We have studied the EQ-5D-5L in Trinidad and Tobago; generalizability to other countries and to other instruments needs to be carefully considered. Preferences have been noted to be country specific, and in particular, values around immediate death and life span in impaired health states may vary across cultures. We see no reason why the results would not generalize to other instruments such as the QLU-C10,<sup> 35 </sup> FACT,<sup> 36 </sup> or SF-6D,<sup> 37 </sup> for which valuation has been done using DCE with duration, and indeed nonlinear time preferences have been noted for the WOOP and SF-6D<sup>19,21</sup> and a reduced utility range on anchoring on immediate death has been noted for the SF-6D.<sup> 38 </sup>

We are fairly confident about the quality of the cTTO data as this used a protocol with an established quality-control procedure<sup> 10 </sup>; however, this was not the case for the DCE with duration data. While we excluded speeders (see Roudijk et al.<sup> 24 </sup> for further details), there was no interview debrief, and hence, we have no information on whether respondents either understood or engaged with the task, beyond noting that the estimated utility decrements show good face validity and that population-level preferences for the cTTO align with those for the DCE with duration data when modeled and anchored appropriately.

While we have shown that nonlinear preferences anchored on duration align well with cTTO preferences at the population level, we have not shown agreement at the individual level. This is not possible to evaluate in our data as the DCE with duration and cTTO tasks were completed by different respondents.

Given the lack of face validity on anchoring on immediate death and previously described theoretical concerns over choices involving death,<sup> 39 </sup> investigators using DCE for health state valuation may wish to consider dropping tasks involving comparisons to immediate death and instead consider comparisons with full health.

When nonlinear time preferences were accounted for and when anchoring was on duration, the observed utility range of −0.55 to 1 agreed well with that obtained for Trinidad and Tobago<sup> 23 </sup> using cTTO preferences elicited using the widely used EQ-VTv2 protocol<sup> 10 </sup> (utilities ranged from −0.6 to 1 ). Moreover, the 2 sets of preferences agreed well not just in range but at the individual state level.<sup> 24 </sup>

In summary, we recommend that valuation studies using DCEs with duration design the choice tasks so as to be able estimate discount parameters and examine whether nonlinear time preferences are present. We further suggest that, given respondents’ potential for heterogeneous interpretations of immediate death, tariffs be anchored on duration rather than immediate death.

## Supplemental Material

<div class="caption">

###### sj-docx-1-mdm-10.1177_0272989X251325828 – Supplemental material for Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be

</div>

Supplemental material, sj-docx-1-mdm-10.1177_0272989X251325828 for Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be by Eleanor M. Pullenayegum, Marcel F. Jonker, Henry Bailey and Bram Roudijk in Medical Decision Making

## Footnotes

## Contributor Information

Eleanor M. Pullenayegum, Child Health Evaluative Sciences, The Hospital for Sick Children, Toronto, ON, Canada; Dalla Lana School of Public Health, University of Toronto, Toronto, Canada.

Marcel F. Jonker, Erasmus School of Health Policy & Management, Erasmus Centre for Health Economics and Erasmus Choice Modelling Centre, Erasmus University Rotterdam, The Netherlands

Henry Bailey, Department of Economics & HEU Centre for Health Economics, the University of the West Indies, St Augustine, Trinidad, West Indies.

Bram Roudijk, EuroQol Research Foundation, Rotterdam, The Netherlands.

## References

## References

1. Pharmaceutical Benefits Advisory Committee. Guidelines for Preparing Submissions to the Pharmaceutical Benefits Advisory Committee. Sydney: Australian Government, Department of Health; 2013.

2. National Institute for Health and Care Excellence. Guide to the Methods of Technology Appraisal. London: National Institute for Health and Care Excellence (NICE); 2013.

3. Canadian Agency for Drugs and Technology in Health. Guidelines for the Economic Evaluation of Health Technologies. Ottawa: The Canadian Coordinating Office for Health Technology Assessment; 2017.

4. Versteegh M, Knies S, Brouwer W. From good to better: new Dutch guidelines for economic evaluations in healthcare. Pharmacoeconomics. 2016;34(11):1071–4. doi:10.1007/s40273-016-0431-y

5. Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual life Res. 2011;20(10):1727–36. doi:10.1007/s11136-011-9903-x

6. Brazier JE, Roberts J. The estimation of a preference-based measure of health from the SF-12. Med Care. 2004;42(9):851–9. doi:10.1097/01.mlr.0000135827.18610.0d

7. Feeny D, Furlong W, Torrance GW, et al. Multiattribute and single-attribute utility functions for the Health Utilities Index Mark 3 system. Med Care. 2002;40(2):113–28. doi:10.1097/00005650-200202000-00006

8. Mulhern B, Norman R, Street DJ, Viney R. One method, many methodological choices: a structured review of discrete-choice experiments for health state valuation. Pharmacoeconomics. 2019;37(1):29–43. doi:10.1007/s40273-018-0714-6

9. Bahrampour M, Byrnes J, Norman R, Scuffham PA, Downes M. Discrete choice experiments to generate utility values for multi-attribute utility instruments: a systematic review of methods. Eur J Health Econ. 2020;21(7):983–92. doi:10.1007/s10198-020-01189-6

10. Stolk E, Ludwig K, Rand K, van Hout B, Ramos-Goñi JM. Overview, update, and lessons learned from the international EQ-5D-5L valuation work: version 2 of the EQ-5D-5L valuation protocol. Value Health. 2019;22(1):23–30. doi:10.1016/j.jval.2018.05.010

11. Rowen D, Brazier J, Van Hout B. A comparison of methods for converting DCE values onto the full health-dead QALY scale. Med Decis Making. 2015;35(3):328–40. doi:10.1177/0272989X14559542

12. Ramos-Goñi JM, Pinto-Prades JL, Oppe M, Cabasés JM, Serrano-Aguilar P, Rivero-Arias O. Valuation and modeling of EQ-5D-5L health states using a hybrid approach. Med Care. 2017;55(7):e51–8. doi:10.1097/MLR.0000000000000283

13. Roudijk B, Donders ART, Stalmeier PFM. Setting dead at zero: applying scale properties to the QALY model. Med Decis Making. 2018;38(6):627–34. doi:10.1177/0272989X18765184

14. Norman R, Mulhern B, Viney R. The impact of different DCE-based approaches when anchoring utility scores. Pharmacoeconomics. 2016;34(8):805–14. doi:10.1007/s40273-016-0399-7

15. Jonker MF, Norman R. Not all respondents use a multiplicative utility function in choice experiments for health state valuations, which should be reflected in the elicitation format (or statistical analysis). Health Econ. 2022;31(2):431–9. doi:10.1002/hec.4457

16. Stalmeier PF, Busschbach JJ, Lamers LM, Krabbe PF. The gap effect: discontinuities of preferences around dead. Health Econ. 2005;14(7):679–85. doi:10.1002/hec.986

17. Roudijk B, Donders ART, Stalmeier PFM. A head-on ordinal comparison of the composite time trade-off and the better-than-dead method. Value Health. 2020;23(2):236–41. doi:10.1016/j.jval.2019.10.006

18. Craig BM, Rand K, Bailey H, Stalmeier PFM. Quality-adjusted life-years without constant proportionality. Value Health. 2018;21(9):1124–31. doi:10.1016/j.jval.2018.02.004

19. Jonker MF, Donkers B, de Bekker-Grob EW, Stolk EA. Advocating a paradigm shift in health-state valuations: the estimation of time-preference corrected QALY tariffs. Value Health. 2018;21(8):993–1001. doi:10.1016/j.jval.2018.01.016

20. Jonker MF, Bliemer MCJ. On the optimization of Bayesian D-efficient discrete choice experiment designs for the estimation of QALY tariffs that are corrected for nonlinear time preferences. Value Health. 2019;22(10):1162–9. doi:10.1016/j.jval.2019.05.014

21. Himmler S, Jonker M, van Krugten F, Hackert M, van Exel J, Brouwer W. Estimating an anchored utility tariff for the well-being of older people measure (WOOP) for the Netherlands. Soc Sci Med. 2022;301:114901. doi:10.1016/j.socscimed.2022.114901

22. van Krugten FCW, Jonker MF, Himmler SFW, Hakkaart-van Roijen L, Brouwer WBF. Estimating a preference-based value set for the Mental Health Quality of Life Questionnaire (MHQoL). Med Decis Making. 2024;44(1):64–75. doi:10.1177/0272989X231208645

23. Bailey H, Jonker MF, Pullenayegum E, Rencz F, Roudijk B. The EQ-5D-5L valuation study for Trinidad and Tobago. Health Qual Life Outcomes. 2024;22(1):51. doi:10.1186/s12955-024-02266-7

24. Roudijk B, Jonker MF, Bailey H, Pullenayegum E. A direct comparison between discrete choice with duration and composite time trade-off methods: do they produce similar results? Value Health. 2024;27(9):1280–8. doi:10.1016/j.jval.2024.05.016

25. Jonker MF, Attema AE, Donkers B, Stolk EA, Versteegh MM. Are health state valuations from the general public biased? A test of health state reference dependency using self-assessed health and an efficient discrete choice experiment. Health Econ. 2017;26(12):1534–47. doi:10.1002/hec.3445

26. Geweke J. Evaluating the accuracy of sampling-based approaches to the calculation of posterior moments. In: Bernardo JM, Berger JO, Dawid P, Smith AFM, eds. Bayesian Statistics. Oxford (UK): Oxford University Press; 1992. p 169–94.

27. Jakubczyk M, Craig BM, Barra M, et al. Choice defines value: a predictive modeling competition in health preference research. Value Health. 2018;21(2):229–38. doi:10.1016/j.jval.2017.09.016

28. Attema AE, Brouwer WB. On the (not so) constant proportional trade-off in TTO. Qual Life Res. 2010;19(4):489–97. doi:10.1007/s11136-010-9605-9

29. Lipman SA, Brouwer WBF, Attema AE. QALYs without bias? Nonparametric correction of time trade-off and standard gamble weights based on prospect theory. Health Econ. 2019;28(7):843–54. doi:10.1002/hec.3895

30. Lipman SA, Attema AE, Versteegh MM. Correcting for discounting and loss aversion in composite time trade-off. Health Econ. 2022;31(8):1633–48. doi:10.1002/hec.4529

31. Yu WSA. Does Changing the Way a Discrete Choice Experiment (DCE) Is Presented to Respondents Affect Results? An Investigation in the Context of Health Using Between-Subject Designs, in Centre for Health Economics Research and Evaluation (CHERE). Sydney (Australia): University of Technology Sydney; 2021.

32. Sharma R, Stano M. Implications of an economic model of health states worse than dead. J Health Econ. 2010;29(4):536–40. doi:10.1016/j.jhealeco.2010.05.005

33. Al Sayah F, Mladenovic A, Gaebel K, Xie F, Johnson JA. How dead is dead? Qualitative findings from participants of combined traditional and lead-time time trade-off valuations. Qual Life Res. 2016;25(1):35–43. doi:10.1007/s11136-015-1073-9

34. Jakubczyk M, Schneider P, Lipman SA, Sampson C. This dead or that dead: framing effects in the evaluation of health states. Value Health. 2024;27(1):95–103. doi:10.1016/j.jval.2023.10.009

35. King MT, Costa DS, Aaronson NK, et al. QLU-C10D: a health state classification system for a multi-attribute utility measure based on the EORTC QLQ-C30. Qual Life Res. 2016;25(3):625–36. doi:10.1007/s11136-015-1217-y

36. Cella DF, Tulsky DS, Gray G, et al. The Functional Assessment of Cancer Therapy scale: development and validation of the general measure. J Clin Oncol. 1993;11(3):570–9. doi:10.1200/JCO.1993.11.3.570

37. Brazier JE, Mulhern BJ, Bjorner JB, et al. Developing a new version of the SF-6D health state classification system from the SF-36v2: SF-6Dv2. Med Care. 2020;58(6):557–65. doi:10.1097/MLR.0000000000001325

38. Mulhern BJ, Bansback N, Norman R, Brazier J; SF-6Dv2 International Project Group. Valuing the SF-6Dv2 classification system in the United Kingdom using a discrete-choice experiment with duration. Med Care. 2020;58(6):566–73. doi:10.1097/MLR.0000000000001324

39. Flynn TN, Louviere JJ, Marley AA, Coast J, Peters TJ. Rescaling quality of life values from discrete choice experiments for use as QALYs: a cautionary tale. Popul Health Metr. 2008;6:6. doi:10.1186/1478-7954-6-6

## Associated Data

### Supplementary Materials

<div class="caption">

###### sj-docx-1-mdm-10.1177_0272989X251325828 – Supplemental material for Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be

</div>

Supplemental material, sj-docx-1-mdm-10.1177_0272989X251325828 for Immediate Death: Not So Bad If You Discount the Future but Still Worse than It Should Be by Eleanor M. Pullenayegum, Marcel F. Jonker, Henry Bailey and Bram Roudijk in Medical Decision Making

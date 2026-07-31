---
project_id: "20190080R1"
work_id: "doi:10.1002/hec.4529"
doi: "10.1002/hec.4529"
pmid: "35474364"
pmcid: "PMC9541376"
title: "Correcting for discounting and loss aversion in composite time trade‐off"
journal: "Health Economics"
publication_date: "2022-04-26"
volume: "31"
issue: "8"
authors:
  - name: "Stefan A Lipman"
    affiliation_ids:
      - "hec4529-aff-0001"
  - name: "Arthur E Attema"
    affiliation_ids:
      - "hec4529-aff-0001"
  - name: "Matthijs M Versteegh"
    affiliation_ids:
      - "hec4529-aff-0002"
affiliations:
  - id: "hec4529-aff-0001"
    name: "Erasmus Centre for Health Economics Rotterdam, Erasmus School of Health Policy & Management, Erasmus University Rotterdam, Rotterdam, Netherlands"
  - id: "hec4529-aff-0002"
    name: "Institute for Medical Technology Assessment, Erasmus University Rotterdam, Rotterdam, Netherlands"
licence: "cc-by"
source_file: "input/projects/20190080R1/papers/doi_10.1002_hec.4529.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9541376/fullTextXML"
source_method: "epmc_xml"
source_sha256: "ec5d3c6548102af9949816354ec9702e332f373e215702bd15cc0ff3d99402e5"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Correcting for discounting and loss aversion in composite time trade‐off

## Abstract

Time trade‐off utilities have been suggested to be biased upwards. This bias is a result of the method being applied assuming linear utility of life duration, which is violated when individuals discount future life years or are loss averse for health. Applying a “corrective approach”, that is, measuring individuals' discount function and loss aversion and correcting time trade‐off utilities for these individual characteristics, may reduce this bias in utilities. Earlier work has developed this approach for time trade‐off in a student sample. In this study, the corrective approach was extended to composite time trade‐off (cTTO) methodology, which enabled correcting utilities for health states worse than dead. In digital interviews a sample of 150 members of the general public completed cTTO tasks for six health states, and afterward they completed measurements of loss aversion and discounting. cTTO utilities were corrected using these measurements under multiple specifications. Respondents were also asked to reflect on and adjust their cTTO utilities directly. Our results show considerable loss aversion and both positive and negative discounting were prevalent. As predicted, correction generally resulted in lower utilities. This was in accordance with the direction of adjustments made by respondents themselves.

**Keywords:** discounting, loss aversion, reference‐dependence, time trade‐off

Revised 2022 Mar 30; Received 2020 Dec 9; Accepted 2022 Mar 31; Issue date 2022 Aug.

## INTRODUCTION

Allocation of scarce health care resources can be informed by economic evaluation, in which costs associated with treatments are compared to the outcomes they yield (Drummond et al., 2015). These outcomes are often expressed as quality‐adjusted life‐years (QALYs), a measure of health comprising length of life and health‐related quality of life (HRQOL). Calculating QALYs requires a weight that represents the value or utility of a state of health, which is multiplied by the duration for which this state is experienced. A health state in which HRQOL is impaired, that is considered better than dead (BTD), receives a utility between 0 and 1, with negative utilities assigned to health states that are considered worse than dead (WTD).

The utilities required to calculate QALYs can be obtained by means of several health state valuation methods. Of these methods, the time trade‐off (TTO) remains particularly relevant, as it is used in valuation of EQ‐5D instruments (Ramos‐Goñi et al., 2020; Stolk et al., 2019), which are recommended for the measurement and valuation of HRQOL in countries such as the UK (NICE, 2018) and the Netherlands (ZINL, 2015). In TTO tasks, individuals are asked to imagine a life in impaired health, for example, 10 years in a wheelchair, for which a life time equivalent in perfect health is elicited, for example, 8 years in perfect health. The task is often (e.g., in EQ‐5D valuation) framed by asking respondents how much time in impaired health they would give up.

TTO is typically applied assuming the linear QALY model holds (Pliskin et al., 1980, defined in Section <a href="#hec4529-sec-0020" data-ref-type="sec">2</a>). This model assumes utility of life duration is linear, that is, future life years are not discounted. In practice, this assumption is violated for many individuals, who positively discount the future, which means they derive less utility from health in the future (Attema & Brouwer, 2014; Attema et al., 2012; Van Der Pol & Roux, 2005). On the other hand, negative discounting has been observed as well, that is, individuals assigning more weight to health in the future (e.g., Lipman & Attema, 2020; Van Der Pol & Cairns, 2000). Since the linear QALY model assumes no discounting, systematic deviations from this assumption could yield bias.

Another violation of the linear QALY model that may affect TTO is reference‐dependence (Kahneman & Tversky, 1979; Tversky & Kahneman, 1992), which entails that health outcomes are evaluated relative to a reference‐point. Outcomes considered better than the reference‐point are coined gains, while outcomes worse than the reference‐point are losses. This distinction is relevant when individuals are loss averse, that is, when losses loom larger than gains of the same size. Although loss aversion with respect to a reference‐point was established for monetary decision‐making, it has been found to apply to health outcomes as well (Kemel & Paraschiv, 2018; Lipman et al., 2019a). Loss aversion has been argued to lead to bias in TTO (Bleichrodt, 2002; Lipman et al., 2019c), assuming that the time spent in impaired health serves as reference‐point. An individual's expected life duration has also been suggested to serve as reference‐point (Lipman et al., 2020b; Van Nooten & Brouwer, 2004), with other authors suggesting reference‐points in the domain of HRQOL to be relevant in health contexts (Wouters et al., 2015).

If bias in TTO related to discounting and loss aversion is considered undesirable, earlier work suggests it may be corrected for (Attema & Brouwer, 2009; Lipman et al., 2019c; van Osch et al., 2004). Such a correction process typically involves approximating the degree of discounting and loss aversion and taking this into account when deriving TTO utilities (Lipman et al., 2019b). Several authors have explored correcting TTO for discounting (Attema & Brouwer, 2009; Attema et al., 2013; Van Der Pol & Roux, 2005; van Osch et al., 2004), but so far only one study applied such a corrective approach to TTO for both loss aversion and discounting (Lipman et al., 2019c). This study measured discounting and loss aversion using the non‐parametric method, developed by Abdellaoui et al. (2016), for each individual. TTO utilities were significantly lower after bias was corrected for, which is in accordance with earlier theoretical predictions (Bleichrodt, 2002) and empirical work (Lipman et al., 2020a).

However, several issues preclude the use of the corrective approach in practice (Lipman et al., 2019b). First, most work on correction for discounting and loss aversion is based on student samples in a lab‐setting, which hampers external validity. Second, most work on the corrective approach has focused on correcting TTO utilities for relatively mild health states. When severe health states are used, some respondents may provide responses suggesting they find health states WTD, which would require an alternative variant of TTO (Attema et al., 2013; Tilling et al., 2010) for which no corrective approach has yet been developed. Third, earlier studies have predominantly used self‐completed TTO, whereas interviewer‐assisted TTO data collection yields data of higher quality compared to (online) self‐completed TTO (Norman et al., 2010).

Hence, the main motivation of this study was to extend the approach developed by Lipman et al. (2019c) for use in valuation studies such as those for EQ‐5D (Ramos‐Goñi et al., 2020; Stolk et al., 2019). This extension involved: i) the use of (methods suitable for) a non‐student sample, ii) developing corrections for composite TTO, which uses lead‐time TTO for eliciting utilities for WTD health states (Attema et al., 2013; Ramos‐Goñi et al., 2020; Stolk et al., 2019), and iii) using computer‐assisted personal interviewing (following the protocol developed by Stolk et al., 2019).

The remainder of this paper is structured as follows. Section <a href="#hec4529-sec-0020" data-ref-type="sec">2</a> defines our notational conventions, while Section <a href="#hec4529-sec-0030" data-ref-type="sec">3</a> presents the extensions applied to the corrective approach used. Next, the experiment used to test this extended corrective approach is reported in Section <a href="#hec4529-sec-0060" data-ref-type="sec">4</a>. Section <a href="#hec4529-sec-0140" data-ref-type="sec">5</a> presents the results of this experiment, which are discussed in Section <a href="#hec4529-sec-0220" data-ref-type="sec">6</a>.

## NOTATION AND PRELIMINARIES

Preference notation is as usual, that is, $`\succ , \succcurlyeq ,`$ and ∼ represent strict preference, weak preference and indifference, respectively. For chronic health states, we will denote health profiles as $`(Q,T),`$ that is, health state $`Q`$ with duration $`T`$ with. We will also write $`\left( {Q_{x},T_{x};\, Q_{y},T_{x} + 1:T_{y}} \right)`$ to express a health profile in which quality of life is equal to $`Q_{x}`$ in $`\text{periods}\ 1,\ 2,\ \text{…}\ \text{to}\ T_{x},`$ followed by $`Q_{y}\`$ for period $`T_{x} + 1,\ \text{…},\ T_{y}`$. Note that subscripts are added to $`T`$ and $`Q,\`$ for example, $`T_{x},\ T_{y},\mspace{9mu} Q_{x}`$ and $`Q_{y}`$, only when needed to clarify which duration $`T`$ and state *Q* applies to which period or outcome, and otherwise we will just write $`T`$ or $`Q`$. If health profiles involve perfect quality of life (i.e., no impairments), we will express this duration in full health as $`\left( \text{FH},T \right)`$. In the general QALY model, preferences for health profiles of the form $`(Q,T)\`$ are evaluated by a utility function $`U( \cdot )`$ which comprises the utility of length of life, modeled by $`L( \cdot )`$, and quality of life, modeled by $`H( \cdot )`$:

``` math
U(Q,T) = H(Q) \ast L(T).
```

Using this notation, TTO indifferences elicited with the usual gauge duration of 10 years (Ramos‐Goñi et al., 2020; Stolk et al., 2019), that is, of the form $`\left( \text{FH},T \right) \sim (Q,10)`$ are evaluated by: $`H\left( \text{FH} \right) \ast L(T) = H(Q) \ast L(10).`$ If, as is usual, we assume $`H\left( \text{FH} \right) = 1`$, we can derive the utility of health state $`Q`$ as:

``` math
H(Q) = L(T)/L(10).
```

If utility of life duration is assumed to be linear, as in the linear QALY model, that is, $`L(T) = T,`$ Equation <a href="#hec4529-disp-0002" data-ref-type="disp-formula">(2</a>) simplifies to:

``` math
H(Q) = T/10.
```

This TTO approach is not valid for eliciting utility for health profiles considered WTD. Different methods exist for eliciting such utilities (Augustovski et al., 2013; Tilling et al., 2010). In the recent valuation protocols for EQ‐5D valuation studies, the lead‐time TTO is used for this purpose (Ramos‐Goñi et al., 2020; Stolk et al., 2019). Lead‐time TTO involves choices between two health profiles: full health for some duration (i.e., the lead time) followed by impaired health for some duration. Typically, the lead time duration and the time in impaired health are equal (they need not be, but we will assume they are for simplicity), and both are often 10 years in practice (Ramos‐Goñi et al., 2020; Stolk et al., 2019). The other health profile, as in “conventional” TTO tasks, involves full health for some duration, of which the duration is typically varied until indifference is obtained. Using our notational conventions, such lead time TTO indifferences can be expressed as: $`\left( \text{FH},T \right) \sim \left( \text{FH},10;\ Q,11:20 \right)`$. Under the general QALY model, such indifferences can be evaluated as: $`H\left( \text{FH} \right) \ast L(T) = H\left( \text{FH} \right) \ast L(10) + H(Q) \ast \left( L(20) - L(10) \right)`$, which assuming $`H\left( \text{FH} \right) = 1`$, yields the utility of health state $`Q`$ as:

``` math
H = \frac{L(T) - L(10)}{L(20) - L(10)}.
```

If utility of life duration is assumed to be linear ($`L(T)\left. = T \right)`$, this simplifies to:

``` math
H(Q) = \frac{T - 10}{10}.
```

Although lead‐time TTO can yield both positive and negative utilities, that is, is suitable for valuation of both health states BTD and WTD, in valuation studies for EQ‐5D it is solely used for WTD health states (Ramos‐Goñi et al., 2020; Stolk et al., 2019). Such use of TTO for BTD health states and lead‐time TTO for WTD health states is referred to as the “composite TTO” (cTTO). By definition, the use of cTTO implies that utilities are elicited onto a single scale by two distinct tasks, involving trade‐offs at different points in time. If an individual's utility function for life duration is non‐linear, whether a period of impaired health occurs earlier or later will affect utilities (Attema & Versteegh, 2013), meaning that the use of cTTO without applying a corrective approach could be, at least conceptually, seen as problematic.

## CORRECTIVE APPROACH FOR CTTO

In this paper, we will use and extend the approach developed in Lipman et al. (2019c) to derive corrections for cTTO. In order to extend the corrective approach to composite TTO, the approach should be extended to lead‐time TTO for WTD health states. Seeing as this is the main contribution of this paper, this is elaborated on in some detail.

The model developed by Lipman et al. (2019c) extends the general QALY model to accommodate insights from prospect theory in three ways, here summarized shortly. First, the model incorporates a reference‐point ($`\left. Q_{r},T_{r} \right)`$. Importantly, the reference‐point can be different between tasks. Second, we modify the scale for utility function for analytical convenience. That is, we apply a different scaling to utility of life duration such that $`L(0) = 0\`$ and $`L(20) = 1,\`$ i.e., the utility of 0 life years is set to 0, and the utility of living 20 years is set to 1. The advantage of this scaling is, compared to the scaling used in (Lipman et al., 2019c), is that the zero condition is still satisfied, that is, the product of $`L(0)`$ and $`H(Q)`$ will always be 0 irrespective of the quality of life, reflecting the intuition that all health states are valued equally in the case of zero life duration (Miyamoto et al., 1998). In order to distinguish between gains and losses w.r.t. The reference‐point, we will rewrite the formula of the general QALY model Equation <a href="#hec4529-disp-0001" data-ref-type="disp-formula">(1</a>), to define evaluation of health profiles with respect to a reference‐point $`\left( {Q_{r},T_{r}} \right)`$ as follows:

``` math
U\left( {Q_{x},T_{x}} \right) = H\left( Q_{r} \right) \ast L\left( T_{r} \right) + \left( {H\left( Q_{x} \right) - H\left( Q_{r} \right)} \right) \ast L\left( T_{x} \right) + H\left( Q_{r} \right) \ast \left( {L\left( T_{x} \right) - L\left( T_{r} \right)} \right).
```

In this expression, we decomposed the total utility into the utility of the reference‐point, a gain/loss part with respect to $`Q_{r}`$, and a gain/loss part with respect to $`T_{r}`$, respectively. Note that this decomposition is a modified expression of the general QALY model. This means that for any $`Q_{x},T_{x},\ Q_{r}`$ and $`T_{r},\`$ the resulting utility derived through Equations <a href="#hec4529-disp-0001" data-ref-type="disp-formula">(1</a>) and Equation <a href="#hec4529-disp-0006" data-ref-type="disp-formula">(6</a>) are identical, as can be seen from Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">A</a>. Our addition to general QALY model is to introduce a loss aversion index $`\lambda`$ to losses in *T*, that is, $`T < T_{r}`$, with $`\lambda\  > \ 1\ (\lambda = 1,\ \lambda\  < \ 1)`$ indicating loss aversion (loss neutrality, gain seeking). For gains in *T*, that is, $`T \geq T_{r}`$, as well as gains and losses in $`Q`$ ($`Q \succcurlyeq Q_{r}\`$ and $`Q \prec Q_{r}\`$ respectively), we assume no loss aversion (i.e., $`\left. \lambda = 1 \right).\`$ Loss aversion is, thus, defined over life duration only, as it is not meaningful for health status, which is considered a qualitative measure. This model is a slightly modified version of the model proposed by Shalev (2002), that accounts for varying reference points, which we assume in this paper. If we multiply the loss in lifetime $`L(T) - L\left( T_{r} \right)`$ with $`\lambda`$, Equation <a href="#hec4529-disp-0006" data-ref-type="disp-formula">(6</a>) becomes:

``` math
U\left( {Q_{x},T_{x}} \right) = H\left( Q_{r} \right) \ast L\left( T_{r} \right) + \left( {H\left( Q_{x} \right) - H\left( Q_{r} \right)} \right) \ast L\left( T_{x} \right) + H\left( Q_{r} \right) \ast \lambda\left( {L\left( T_{x} \right) - L\left( T_{r} \right)} \right).
```

### Corrective approach for TTO

As in earlier work (Bleichrodt, 2002; Lipman et al., 2019c) we will make the (simplifying) assumption that TTO indifferences of the form $`\left( \text{FH},T \right) \sim (Q,10)`$ are elicited with $`(Q,10)\`$ as reference‐point (as this coincides with the framing typically used). That is, we have $`Q_{r} = Q`$ and $`T_{r} = 10`$. According to Equation <a href="#hec4529-disp-0006" data-ref-type="disp-formula">(6</a>), this indifference can be evaluated by

``` math
H(Q)\ L(10) + \left( H\left( \text{FH} \right) - H(Q) \right)\ L(T) + H(Q)\lambda\left( L(T) - L(10) = H(Q)L(10). \right.
```

From this expression, it becomes explicit that the option $`\left( \text{FH},T \right)`$ involves a gain in QoL, $`\left( H\left( \text{FH} \right) - H(Q) \right) \ast L(T)`$, and a loss in lifetime spent in $`Q`$, $`H(Q) \ast \lambda\left( L(T) - L(10) \right)`$.

Given our scaling of $`H\left( \text{FH} \right) = 1`$, solving for $`H(Q)`$ yields:

``` math
H(Q) = \frac{L(T)\ }{\lambda L(10) + (1 - \lambda)L(T)}.
```

### Corrective approach for lead‐time TTO

Applying a corrective approach to lead‐time TTO requires an assumption about the reference‐point in this method. Earlier qualitative work on gambles for length of life suggested that the outcome that remains constant across elicitations may serve as reference‐point (van Osch et al., 2006). In “conventional” TTO, this yielded the prediction that $`(Q,10)`$ serves as reference‐point (Bleichrodt, 2002; Lipman et al., 2019c), for which some qualitative support can be found in Van Osch (2007). If this logic is symmetrically applied to lead‐time TTO, one could expect $`\left( \text{FH},10;\ Q,11:20 \right)`$ to be the reference‐point. In cTTO, lead‐time TTO is only applied for WTD health states, which implies $`T < 10`$. As such, if $`\left( \text{FH},10;\ Q,11:20 \right)`$ is the reference‐point, then $`\left( \text{FH},T \right)`$ entails a loss of 10 years in $`Q`$ and a loss of $`10 - T`$ years in FH. Compared to the conventional TTO, we now have a reference health profile consisting of two instead of one chronic health states, but the same logic can be applied, see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">A</a>. That is, $`\left( \text{FH},T \right) \sim \left( \text{FH},10;\ Q,11:20 \right),`$ is evaluated as:

``` math
H\left( \text{FH} \right)L(10) + H(Q)\left( L(20) - L(10) \right) + H\left( \text{FH} \right) \ast \lambda\left( L(T) - L(10) \right) + H(Q) \ast \lambda\left( L(10) - L(20) \right) = H\left( \text{FH} \right)L(10) + H(Q)\left( L(20) - L(10) \right).
```

Solving for $`H(Q)`$, and applying the scaling introduced earlier, gives:

``` math
H(Q) = \frac{L(T) - L(10)}{1 - L(10)}.
```

However, assuming $`\left( \text{FH},10;\ Q,11:20 \right)`$ is taken as reference‐point, implies that we assume respondents take as reference‐point a health profile with a WTD health state and consider giving up life years in that state $`Q\`$ as a loss. This may be considered unlikely. Hence, we also apply our model assuming that respondents use a life duration of $`\left( \text{FH},10 \right)`$ years as a reference‐point. In that case, respondents incur a loss in life duration (i.e., $`T - 10`$ in FH) in the option $`\left( \text{FH},T \right)`$, and a gain in life time (i.e., $`20 - 10`$) in $`Q`$ in the option $`\left( \text{FH},10;\ Q,11:20 \right)`$. The latter is in fact valued negatively because *Q* is a WTD health state. As such, $`\left( \text{FH},T \right) \sim \left( \text{FH},10;\ Q,11:20 \right)`$ is evaluated by (see also Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">A</a>):

``` math
H\left( \text{FH} \right)L(10) + H\left( \text{FH} \right)\ \lambda\left( L(T) - L(10) \right) = H\left( \text{FH} \right)L(10) + H(Q)\left( L(20) - L(10) \right).
```

Solving for $`H(Q)`$ and applying our scaling gives:

``` math
H(Q) = \frac{\lambda\left( L(T) - L(10) \right)\ }{1 - L(10)}.
```

Notice that, because in this case $`T_{r}`$  =  $`10`$, the only difference between Equations (<a href="#hec4529-disp-0011" data-ref-type="disp-formula">10</a>) and (<a href="#hec4529-disp-0013" data-ref-type="disp-formula">12</a>) is the addition of $`\lambda`$ to the numerator of Equation (<a href="#hec4529-disp-0013" data-ref-type="disp-formula">12</a>). That is, $`H(Q)`$ is predicted to be larger (i.e., less negative) if the reference point is $`\left( \text{FH},10;\ Q,11:20 \right)`$ than if it is $`\left( \text{FH},\ 10 \right)`$ for $`\lambda > 1`$.

## EXPERIMENT

As demonstrated in the previous section, the corrective approach for cTTO can be operationalized either by correcting using Equations (<a href="#hec4529-disp-0009" data-ref-type="disp-formula">8</a>) and (<a href="#hec4529-disp-0011" data-ref-type="disp-formula">10</a>) or by Equations (<a href="#hec4529-disp-0009" data-ref-type="disp-formula">8</a>) and <a href="#hec4529-disp-0013" data-ref-type="disp-formula">(12</a>). The former approach, that is, based on Equations (<a href="#hec4529-disp-0009" data-ref-type="disp-formula">8</a>) and (<a href="#hec4529-disp-0011" data-ref-type="disp-formula">10</a>), assumes that respondents faced with TTO or lead‐time TTO use the constant outcome as reference‐point. This approach is referred to as *correction based on constant alternative* (in short: constant alternative correction). If on the other hand, we use the latter approach, that is, based on Equations (<a href="#hec4529-disp-0009" data-ref-type="disp-formula">8</a>) and <a href="#hec4529-disp-0013" data-ref-type="disp-formula">(12</a>), we assumed that the reference‐point is 10 years for both TTO and lead‐time TTO, which corresponds to the maximum time attainable in a BTD health state in both TTO and lead‐time TTO. As such, we refer to this approach as *correction based on maximum BTD time* (or in short: maximum BTD correction). Both these approaches involve different assumptions about the reference‐point for lead‐time TTO and no research is available to determine a priori which reference‐point individuals use. Therefore, both approaches were applied in our experiment in which 6 cTTO utilities were elicited as well as $`\lambda`$ and the utility function $`L(T)`$ on the domain 0–20.

### Sample and data collection strategy

The sample for this experiment consisted of 150 respondents of the general public, recruited through a marketing company. The marketing company was instructed to recruit such that the sample was a reasonable reflection of the Dutch population in terms of age, gender and education level, but no strict quota were applied. We believe such non‐random sampling is warranted as this study aimed to extend and replicate findings of Lipman et al. (2019c) in the general public, rather than to obtain representative cTTO utilities. Respondents were recruited for taking part in an academic study on the value of health and were invited for personal interviews taking place on university campus. For completing the interview, which lasted around an hour, respondents were rewarded 30 euro. All interviews were completed in the Netherlands by the first author, using a personal laptop, in sessions of up to 7 interviews per day. Data collection commenced on March 8, 2020 and by March 13, 36 interviews were completed. The global outbreak of COVID‐19 and the lockdown of public facilities that followed it, however, necessitated a change in mode of administration, as face‐to‐face interviews were no longer possible. The remaining 114 interviews were completed digitally using videotelephony software (i.e., Zoom). The use of such software has several advantages and disadvantages for cTTO interviews, which are discussed elsewhere (Lipman, 2020). Table <a href="#hec4529-tbl-0001" data-ref-type="table">1</a> shows respondent characteristics for the full sample, the sample that completed interviews in person, and the sample that completed interviews digitally. Furthermore, few differences existed between those sampled for personal or digital interviews, with only those sampled for digital interviews being slightly younger (*T*‐test, *p* = 0.001) and more likely to be married. We find no evidence of differences between the sample recruited for any of the other demographics reported in Table <a href="#hec4529-tbl-0001" data-ref-type="table">1</a> (Chi‐squared tests, all *p*'s \> 0.10).

<div id="hec4529-tbl-0001" class="table-wrap">

<div class="caption">

Demographics for the full sample and subsamples depending on data collection strategy

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Full sample (<em>n</em> = 150)</th>
<th style="text-align: left;">Personal interviews (<em>n</em> = 36)</th>
<th style="text-align: left;">Digital interviews (<em>n</em> = 114)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Sex</td>
</tr>
<tr>
<td style="text-align: left;">Male</td>
<td style="text-align: left;">74 (49.3%)</td>
<td style="text-align: left;">13 (36.1%)</td>
<td style="text-align: left;">61 (53.5%)</td>
</tr>
<tr>
<td style="text-align: left;">Female</td>
<td style="text-align: left;">76 (50.7%)</td>
<td style="text-align: left;">23 (63.9%)</td>
<td style="text-align: left;">53 (46.5%)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Age (in years)</td>
</tr>
<tr>
<td style="text-align: left;">Mean (SD)</td>
<td style="text-align: left;">42.7 (15.6)</td>
<td style="text-align: left;">50.3 (15.5)</td>
<td style="text-align: left;">40.3 (14.8)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Education level</td>
</tr>
<tr>
<td style="text-align: left;">Low</td>
<td style="text-align: left;">10 (6.7%)</td>
<td style="text-align: left;">5 (13.9%)</td>
<td style="text-align: left;">5 (4.4%)</td>
</tr>
<tr>
<td style="text-align: left;">Middle</td>
<td style="text-align: left;">52 (34.7%)</td>
<td style="text-align: left;">11 (30.6%)</td>
<td style="text-align: left;">41 (36.0%)</td>
</tr>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: left;">88 (58.7%)</td>
<td style="text-align: left;">20 (55.6%)</td>
<td style="text-align: left;">68 (59.6%)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Household income</td>
</tr>
<tr>
<td style="text-align: left;">&lt;15,000 euros</td>
<td style="text-align: left;">40 (26.7%)</td>
<td style="text-align: left;">9 (25%)</td>
<td style="text-align: left;">31 (27.2%)</td>
</tr>
<tr>
<td style="text-align: left;">15,000–30,000 euros</td>
<td style="text-align: left;">44 (29.3%)</td>
<td style="text-align: left;">10 (27.8%)</td>
<td style="text-align: left;">34 (29.8%)</td>
</tr>
<tr>
<td style="text-align: left;">30,000–60,000s</td>
<td style="text-align: left;">42 (28%)</td>
<td style="text-align: left;">12 (33.3%)</td>
<td style="text-align: left;">30 (26.3%)</td>
</tr>
<tr>
<td style="text-align: left;">&gt;60,000 euros</td>
<td style="text-align: left;">21 (14%)</td>
<td style="text-align: left;">3 (8.3%)</td>
<td style="text-align: left;">18 (15.8%)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Marital status</td>
</tr>
<tr>
<td style="text-align: left;">Married</td>
<td style="text-align: left;">39 (26%)</td>
<td style="text-align: left;">15 (41.7%)</td>
<td style="text-align: left;">24 (21.1%)</td>
</tr>
<tr>
<td style="text-align: left;">Not married</td>
<td style="text-align: left;">111 (74%)</td>
<td style="text-align: left;">21 (58.3%)</td>
<td style="text-align: left;">90 (78.9%)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Current student</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">12 (8%)</td>
<td style="text-align: left;">2 (5.6%)</td>
<td style="text-align: left;">10 (8.8%)</td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td style="text-align: left;">138 (92%)</td>
<td style="text-align: left;">34 (94.4%)</td>
<td style="text-align: left;">104 (91.2%)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Has children</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">66 (44%)</td>
<td style="text-align: left;">20 (55.6%)</td>
<td style="text-align: left;">46 (40.4%)</td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td style="text-align: left;">84 (56%)</td>
<td style="text-align: left;">16 (44.4%)</td>
<td style="text-align: left;">68 (59.6%)</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Religious</td>
</tr>
<tr>
<td style="text-align: left;">Yes</td>
<td style="text-align: left;">33 (22%)</td>
<td style="text-align: left;">5 (13.9%)</td>
<td style="text-align: left;">28 (24.6%)</td>
</tr>
<tr>
<td style="text-align: left;">No</td>
<td style="text-align: left;">117 (78%)</td>
<td style="text-align: left;">31 (86.1%)</td>
<td style="text-align: left;">86 (75.4%)</td>
</tr>
</tbody>
</table>

*Note*: Education level was recoded as it was reported in terms of Dutch educational attainment. The following recoding is used: low education levels: VMBO, LBO or MAVO, middle education levels: VWO, MBO, or HAVO, and high education levels: HBO or WO.

</div>

### Design

The interview protocol consisted of the following parts: a) Introduction and Demographics, b) cTTO introduction, c) main cTTO task for 6 states presented in randomized order (based on the EQ‐VT protocol), d) elicitation of loss aversion and discounting in randomized order, and e) a modification of the validation task developed by Lipman et al. (2020a). Ethical approval was provided by the Erasmus School of Health Policy's internal review board. Parts b) to c) were operationalized in Microsoft Powerpoint (using standardized EQ‐VT software), while d) and e) were operationalized in *R* Shiny. Each of these is elaborated on below (including how this was operationalized in digital interviews). The final design of this protocol was developed after conducting pilot sessions with 28 students and 5 test interviews with members of the general public. The main changes implemented after these pilot sessions involved clarifications of the instructions used and a reduction of the amount of health states in part c) from 10 to 6 to avoid fatigue in members of the general public.

#### Introduction and Demographics

To commence the interview, the interviewer explained the goal of the interview (i.e., to measure the value of health in order to decide which treatment to fund), after which informed consent was obtained. In personal interviews written informed consent was provided, whereas in digital interviews informed consent was obtained and recorded verbatim. Afterward, a questionnaire was filled out capturing the following demographics (for details, see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">B</a>): age, sex, income, subjective life expectancies (SLEs), religion, and beliefs about life after death and euthanasia (adapted from van Nooten et al., 2016). This part of the interview was concluded by respondents filling out the EQ‐5D‐5L instrument, that is, self‐reporting their health in terms of mobility, self‐care, ability to perform daily activities, pain or discomfort and anxiety or depression. Also, the EQ‐5D‐5L instrument contains a visual analog scale (EQ‐VAS) on which respondents report their health on a scale from 0 to 100, where 0 and 100 represent the worst and best imaginable health possible, respectively. In face‐to‐face interviews, respondents filled out the questionnaires on paper, in digital interviews respondents were shown the questionnaire and stated their answers verbatim which were stored by the interviewer.

#### cTTO introduction and main cTTO task

Next, respondents were introduced to the cTTO task. The introduction used in this experiment is adapted from the EQ‐VT protocol, with slight modifications in place for our purposes. As is outlined in Stolk et al. (2019), cTTO was introduced to respondents by a “wheelchair” example, in which respondents are asked to imagine living for 10 more years in a wheelchair and are offered to live for 10 more years in perfect health instead. Next, the top‐down titration search procedure outlined in Oppe et al. (2014) was employed to elicit a cTTO indifference for this respondent. In both face‐to‐face and digital interviews, the respondent indicated their preference verbatim, which was entered into the software by the interviewer (for screenshots, see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">C</a>). Next, respondents completed a second example employed to show the lead‐time component of cTTO (or equivalently the “conventional” TTO if life in a wheelchair was considered WTD).

All cTTO tasks were completed with health states described by EQ‐5D‐5L, that is, the EQ‐5D instrument that distinguishes five levels of severity on each of 5 domains of health‐related of life. This instrument uses the following five domains to described health‐related quality of life: mobility, self‐care, usual activities, pain/discomfort, and anxiety/depression, and describes problems on these domains with severity labels ranging from “no problems” to “extreme problems/unable to”. Health states are typically denoted by 5‐digit codes like 22113, with each number representing severity of the relevant domain. Respondents completed two practice cTTO tasks involving a relatively mild and severe health state (21211 and 35554 respectively). Next, for the main cTTO task, respondents completed a series of 6 cTTO tasks in succession for the following 6 health states (presented in random order): 11211, 13313, 35332, 22434, 24443, and 55555. These health states were selected to cover a range of health problems, from relatively mild to very severe and were also included in the Dutch valuation of EQ‐5D‐5L (Versteegh et al., 2016).

#### Elicitation of loss aversion and discounting

Loss aversion was measured by means of the non‐parametric method (Abdellaoui et al., 2016). Note that this method can be used to measure the full prospect theory functional; that is, the utility for gains, utility for losses, probability weighting for gains and losses, and the loss aversion index. However, since we only need the loss aversion coefficient for our purposes, we only use the parts of this methodology required to assess loss aversion. This involves eliciting three chained indifferences (see Table <a href="#hec4529-tbl-0002" data-ref-type="table">2</a> for an example), which allow estimating loss aversion as defined by Köbberling and Wakker (2005). The provision of an elaborate formal rationale for this method is beyond the scope of this paper, but they can be found in Abdellaoui et al. (2016) or the Online Supplements of Lipman et al. (2019c). Implementing this method for measuring loss aversion requires a reference‐point (denoted $`r`$) to which gains and losses are compared and a starting gain amount $`G`$ from which the chained elicitation is started. To test the robustness of our corrective approach to different reference‐points, we measured loss aversion for two reference‐points, living for 10 and 20 more years.[^1] These years were described as being lived without health problems, as Lipman et al. (2019a) have shown the loss aversion coefficient estimated with this method does not depend systematically on the quality of life of the life duration gained and lost). Outcomes in the task were denoted as compared to this reference‐point (that is, +2 and −2 years denoted living for 12 and 8 years, respectively, when $`\left. r = 10 \right)`$. The gauge outcome $`G`$ was set to 5 years.

<div id="hec4529-tbl-0002" class="table-wrap">

<div class="caption">

Indifferences elicited in the non‐parametric method, where $`x_{0.5}y`$ denotes a gamble yielding $`x`$ with probability 0.5 and $`y`$ otherwise and the example indifferences yield a loss aversion coefficient of $`\lambda = 2`$

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">General notation</th>
<th style="text-align: left;">Goal</th>
<th style="text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Indifference 1: Mixed prospect</td>
<td style="text-align: left;"><span class="math inline"><em>G</em></span> <sub>0.5</sub> <span class="math inline">ℒ</span> ∼ r</td>
<td style="text-align: left;">Eliciting <span class="math inline">ℒ</span></td>
<td style="text-align: left;"><div id="jats-math-114_df" class="disp-formula">
5
</div>
<sub>0.5</sub>
<div id="jats-math-115_df" class="disp-formula">
−
3
∼
0
</div></td>
</tr>
<tr>
<td style="text-align: left;">Indifference 2: Certainty equivalence – gains</td>
<td style="text-align: left;"><span class="math inline"><em>G</em></span> <sub>0.5</sub> <span class="math inline"><em>r</em></span> ∼ <span class="math inline"><em>x</em><sub>1</sub><sup>+</sup></span></td>
<td style="text-align: left;">Eliciting <span class="math inline"><em>x</em><sub>1</sub><sup>+</sup></span></td>
<td style="text-align: left;"><div id="jats-math-120_df" class="disp-formula">
5
</div>
<sub>0.5</sub>
<div id="jats-math-121_df" class="disp-formula">
0
</div>
<div id="jats-math-122_df" class="disp-formula">
∼
2
</div></td>
</tr>
<tr>
<td style="text-align: left;">Indifference 3: Certainty equivalence ‐ losses</td>
<td style="text-align: left;"><span class="math inline">ℒ</span> <sub>0.5</sub> <span class="math inline"><em>r</em></span> ∼ <span class="math inline"><em>x</em><sub>1</sub><sup>−</sup></span></td>
<td style="text-align: left;">Eliciting <span class="math inline"><em>x</em><sub>1</sub><sup>−</sup></span></td>
<td style="text-align: left;"><div id="jats-math-127_df" class="disp-formula">
−
3
</div>
<sub>0.5</sub>
<div id="jats-math-128_df" class="disp-formula">
0
</div>
<div id="jats-math-129_df" class="disp-formula">
∼
−
1
</div></td>
</tr>
<tr>
<td style="text-align: left;">Köbberling and Wakker (<span class="citation" data-cites="hec4529-bib-0018">2005</span>)</td>
<td style="text-align: left;"><div id="jats-math-130_df" class="disp-formula">
λ
=
x
1
+
−
x
1
−
</div></td>
<td style="text-align: left;">Loss aversion coefficient</td>
<td style="text-align: left;"><div id="jats-math-131_df" class="disp-formula">
λ
=
2
−
(
−
1
)
=
2
</div></td>
</tr>
</tbody>
</table>

</div>

Discounting (i.e., the curvature of the utility function $`L(T)`$) was elicited by means of the direct method (Attema et al., 2012). This method lets a subject compare two simple health profiles with the same time horizon, which are both combinations of two health states, for example, full health (FH) and some imperfect state $`Q\`$ that was operationalized by describing a state labeled chronic back pain (BP). This state was also described using EQ‐5D‐5L, that is, it was described as 21211. Both profiles had a 20‐year duration, which is assumed to be the reference‐point. Assuming our model holds, the use of the direct method provides the utility curvature of $`L(T)`$ from $`L`$ (0) to $`L(20)`$. The difference between the profiles is that one starts with the better health state $`\text{FH}`$ for some duration[^2] (denoted $`T_{d1/2}`$) and ends with the worse state $`\text{BP}`$ for the remainder of the 20 years period (i.e., from $`T_{d1/2}`$ to 20). Using our notation this can be expressed as $`(\text{FH},\ T_{d1/2};\text{BP},T_{d1/2} + 1\ :20)`$. The other health profile starts with $`\text{BP}`$ for duration, followed by an improvement toward FH: that is, $`\left( {\text{BP},\ T_{d1/2};\ \text{FH},T_{d1/2} + 1:20} \right)`$ Now, the purpose is to elicit the point $`T_{d1/2}`$ such that an individual is indifferent between the two profiles; that is, $`\left( {\text{FH},T_{d1/2};\ \text{BP},T_{d1/2} + 1\ :20} \right) \sim \left( {\text{BP},T_{d1/2};\ \text{FH},T_{d1/2} + 1\ :20} \right).`$ Using our model, which does not involve losses in life duration and, hence, can be evaluated using the general QALY model, this indifference yields: $`L(20) - L\left( T_{d1/2} \right) = L\left( T_{d1/2} \right) - L(0).`$ Hence, the period $`\left\lbrack {1,T_{d1/2}} \right\rbrack\`$ has the same utility as $`\lbrack T_{d1/2},20\rbrack`$. Given our normalization, *L* $`(0) = 0\ \text{and}\ L(20) = 1`$, this gives $`L\left( T_{d1/2} \right) = 1/2`$ \* $`\left\lbrack L(20) + L(0) \right\rbrack = {1/2}*1 =`$ $`1/2`$. As is demonstrated in Attema et al. (2012), this procedure can be repeated by finding $`T_{d1/4}\`$ such that $`L`$ ($`\left. T_{d1/4} \right) =`$ $`L\left( T_{d1/2} \right) - L\left( T_{d1/4} \right)`$ and, hence, $`L\left( T_{d1/4} \right) = 1/4`$. As a result, this method allows for a measurement of the utility function for life duration up to any desired precision. In this experiment, this procedure was performed 5 times, i.e., to determine the points $`T`$ that yield $`L(T_{d1/8}) = \frac{1}{8},\ L(T_{d1/4}) = \frac{1}{4},L(T_{d1/2}) = \frac{1}{2},L(T_{d3/4}) = \frac{3}{4},L(T_{d7/8}) = \frac{7}{8}`$. To apply Equations <a href="#hec4529-disp-0009" data-ref-type="disp-formula">(8), (10)</a> and <a href="#hec4529-disp-0011" data-ref-type="disp-formula">(12)</a> for any $`T`$, we use linear interpolation, which allows for correcting cTTO utilities without assuming a parametric form for $`L(T)`$. The shape of $`L(T)`$ can be characterized non‐parametrically by calculating the area under the curve (AUC). This AUC is calculated for a new function *L\**(*x*), where *x* = *T*/20, such that duration *T* is normalized to 0–1 scale. For this new function, the shape of *L\** $`(x)\`$ is concave \[linear, convex\] whenever $`\text{AUC}\  > 0.5\ \left\lbrack \text{AUC} = 0.5,\ \text{AUC}\  < 0.5 \right\rbrack`$. Although the corrective approach will be applied non‐parametrically, we also use the direct method data to estimate a discount rate with non‐linear least squares estimation and an exponential parametric form, that is: *L\** $`(x) = \frac{1 - \exp( - \rho x)}{1 - \exp( - \rho)},`$ which, as in our notation, yields $`L(0) = 0`$ and $`L(T = 20,\mspace{9mu} x = 1) = 1`$. For $`\rho = 0`$ we take *L\** $`(x) = x`$.

#### Validation task

The final task performed in this experiment was an adaptation of the validation task developed by Lipman et al. (2020a). As in the original method, respondents are first explained the goal of QALYs and the role cTTO utilities play in calculating them (see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">C</a> for screenshots of the task and the instruction used). Seeing the importance these utilities play in guiding allocation decisions, respondents are asked to reflect on what their choices imply about their views about the health states and their position on the QALY scale (i.e., from −1 to 1). This reflection has the following form. First, respondents are shown the utility elicited for a health state based on their stated preferences (based on Equations (<a href="#hec4529-disp-0003" data-ref-type="disp-formula">3</a>) and <a href="#hec4529-disp-0005" data-ref-type="disp-formula">(5</a>)) and asked to indicate if it: a) is exactly right, b) should be higher, c) should be lower. Afterward, respondents have the opportunity to specify a different utility for that health state with a slider between −1 and 1 using 2 decimals. Note that this validation task does not involve choice‐based trade‐offs of length and quality of life, but rather respondents reflect on, adjust (if necessary) and confirm utilities obtained for elicited stated preferences. The utilities derived from the cTTO task (obtained through Equations (<a href="#hec4529-disp-0003" data-ref-type="disp-formula">3</a>) and (<a href="#hec4529-disp-0005" data-ref-type="disp-formula">5</a>)) will be referred to as “elicited cTTO utilities” and the utilities confirmed by respondents are referred to as “confirmed cTTO utilities”.

### Data analysis

Throughout we use a significance level of $`\alpha = 0.05`$. Seeing as many tests are reported, adjusting for multiple comparisons may be needed. Although many approaches for adjusting for multiple comparisons are defensible, in our analyses, Bonferroni adjusted *p*‐values are also reported whenever a single test is repeated multiple times. For example, when cTTO utilities before and after correction are compared for all 6 states with paired *t*‐tests, *p* values are multiplied by the number of tests (in this case 6). In such cases, *p* values are referred to as adjusted p's. Note that this approach is only applied to significant results, as Bonferroni adjustment is used to reduce the risk of Type I errors. Before further elaborating on data analysis, we compared data quality between digital and personal interviews, as differences between their data would warrant separate analysis and reporting of all results, or perhaps even exclusion of part of the sample. Next, we provided descriptive statistics for our sample, which also included loss aversion and discounting. Utilities are reported descriptively first, and a set of paired comparisons is used to compare confirmed, elicited and compared utilities per health state. Furthermore, the direction of correction was compared to the direction in which respondents adjusted their utilities themselves in the validation task.

## RESULTS

### Data quality

#### Interviews completed

Out of the 150 interviews performed, 2 interviews were terminated before data could be collected for discounting and loss aversion, because it took over 50 min to complete parts a) to c) of the interview (i.e., measurement of cTTO utilities). To avoid having to cancel other interviews scheduled that day, these two interviews (1 personal and 1 digital interview) were ended prematurely. Furthermore, a single digital interview was terminated after approximately 20 min, after part b), as the respondent indicated to find deciding about health and trading off life years to be unacceptable due to religious reasons. As such, we have complete data for 147 respondents, and partial data (cTTO utilities only) for 149 respondents.

#### Comparing personal and digital interviews and overall data quality

As is also discussed elsewhere (Lipman, 2020), we found no differences between digitally and personally completed TTO interviews (see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">D</a>) on any of the quality indicators included in our analysis. That is, we find digital and personal interviews to both have a similar amount of problematic responses, as defined by Alava et al. (2020). Furthermore, Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">D</a> also reports a series of analyses that indicate that no difference existed in cTTO utilities between digital and personal interviews. Hence, all further analyses (including further analysis of data quality) are reported for the combined sample. When exploring data quality in the full sample, a relatively large amount of non‐trading and all‐in‐trading responses were observed. That is, 134 (15%) and 118 (13%) out of the total 894 states valued (6 per respondent) received cTTO utilities of 1 and −1 respectively. Furthermore, 40 (27%) out of 149 respondents assigned at least 1 state the same as 55555. However, this relevantly high percentage appears to be inflated by non‐trading responses, as only 15 (10%) out of 149 respondents had such counterintuitive preferences when non‐trading responses were excluded.

### Descriptive statistics

Table <a href="#hec4529-tbl-0003" data-ref-type="table">3</a> contains descriptive statistics for the various measures completed in the interviews. Each is discussed separately below.

<div id="hec4529-tbl-0003" class="table-wrap">

<div class="caption">

Frequency table for EQ‐5D‐5L and descriptive statistics for remaining demographics, loss aversion and discounting measures

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Level 1</th>
<th style="text-align: left;">Level 2</th>
<th style="text-align: left;">Level 3</th>
<th style="text-align: left;">Level 4</th>
<th style="text-align: left;">Level 5</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">EQ‐5D‐5L: Mobility</td>
<td style="text-align: left;">126</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ‐5D‐5L: Self‐care</td>
<td style="text-align: left;">147</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ‐5D‐5L: Usual activities</td>
<td style="text-align: left;">118</td>
<td style="text-align: left;">24</td>
<td style="text-align: left;">6</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ‐5D‐5L: Pain/discomfort</td>
<td style="text-align: left;">82</td>
<td style="text-align: left;">47</td>
<td style="text-align: left;">19</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">EQ‐5D‐5L: Anxiety/depression</td>
<td style="text-align: left;">107</td>
<td style="text-align: left;">34</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"><strong>Mean</strong></td>
<td style="text-align: left;"><strong>SD</strong></td>
<td style="text-align: left;"><strong>Median</strong></td>
<td style="text-align: left;"><strong>Q1</strong></td>
<td style="text-align: left;"><strong>Q3</strong></td>
</tr>
<tr>
<td style="text-align: left;">EQ‐VAS</td>
<td style="text-align: left;">80.67</td>
<td style="text-align: left;">12.14</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">90</td>
</tr>
<tr>
<td style="text-align: left;">SLE</td>
<td style="text-align: left;">83.95</td>
<td style="text-align: left;">8.07</td>
<td style="text-align: left;">85</td>
<td style="text-align: left;">80</td>
<td style="text-align: left;">89.25</td>
</tr>
<tr>
<td style="text-align: left;">SLE‐max</td>
<td style="text-align: left;">93.28</td>
<td style="text-align: left;">9.9</td>
<td style="text-align: left;">93</td>
<td style="text-align: left;">87</td>
<td style="text-align: left;">100</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>λ</em> </span> with <span class="math inline">RP (10 years</span>)</td>
<td style="text-align: left;">3.51</td>
<td style="text-align: left;">5.49</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">1.29</td>
<td style="text-align: left;">3.42</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>λ</em> </span> with <span class="math inline">RP (20 years</span>)</td>
<td style="text-align: left;">3.48</td>
<td style="text-align: left;">6.02</td>
<td style="text-align: left;">1.88</td>
<td style="text-align: left;">1</td>
<td style="text-align: left;">3.12</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-175_df" class="disp-formula">
T
d
1
/
8
</div></td>
<td style="text-align: left;">2.64</td>
<td style="text-align: left;">1.27</td>
<td style="text-align: left;">2.5</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;">3</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-176_df" class="disp-formula">
T
d
1
/
4
</div></td>
<td style="text-align: left;">5.03</td>
<td style="text-align: left;">1.88</td>
<td style="text-align: left;">5</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">6</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-177_df" class="disp-formula">
T
d
1
/
2
</div></td>
<td style="text-align: left;">9.67</td>
<td style="text-align: left;">2.23</td>
<td style="text-align: left;">10</td>
<td style="text-align: left;">8.25</td>
<td style="text-align: left;">11</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-178_df" class="disp-formula">
T
d
3
/
4
</div></td>
<td style="text-align: left;">14.35</td>
<td style="text-align: left;">2.15</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">13.5</td>
<td style="text-align: left;">15.5</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-179_df" class="disp-formula">
T
d
7
/
8
</div></td>
<td style="text-align: left;">16.8</td>
<td style="text-align: left;">1.98</td>
<td style="text-align: left;">17.5</td>
<td style="text-align: left;">16.5</td>
<td style="text-align: left;">17.5</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-180_df" class="disp-formula">
AUC
</div></td>
<td style="text-align: left;">0.49</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">0.50</td>
<td style="text-align: left;">0.44</td>
<td style="text-align: left;">0.53</td>
</tr>
<tr>
<td style="text-align: left;"><div id="jats-math-181_df" class="disp-formula">
ρ
</div></td>
<td style="text-align: left;">0.21</td>
<td style="text-align: left;">1.45</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">−0.34</td>
<td style="text-align: left;">0.72</td>
</tr>
</tbody>
</table>

Abbreviation: SLE, subjective life expectancy.

</div>

#### EQ‐5D‐5L and demographic questionnaire

Respondents were generally healthy, the far majority reporting no problems on each separate dimension (84%, 98%, 79%, 55% and 71% respectively), and 39% of the sample reported no health problems at all (i.e., 11111). The three most occurring health profiles were: 11111, 11112, and 11121. If the Dutch tariff (Versteegh et al., 2016) is used to translate these EQ‐5D‐5L health states to utilities, we find a mean utility of 0.89 (SD = 0.12). If we compare subjective life expectancy (SLE) to individuals' age, we find that respondents' remaining SLE was 41.24 years (SD = 18.46).

#### Loss aversion and discounting

When loss aversion was measured with 10 years as reference‐point, we found 82%, 14% and 4% of respondents to be loss averse, gain seeking or loss neutral, respectively. When the reference‐point was set to 20 years, the proportion of respondents being loss averse was slightly lower, with more respondents being loss neutral, that is, at 73% (loss averse), 13% (gain seeking) and 14% (loss neutral). Nonetheless, the mean estimate of $`\lambda`$ was not significantly different between reference‐points (paired *t*‐test: *t* (146) = 0.07, *p* = 0.94). Indeed, 75% of respondents were classified the same regardless of the RP used for measuring $`\lambda.\`$ In particular, 66% of respondents were loss averse throughout. Although a Chi‐squared analysis suggested that classification was not independent of the RP used, that is, $`\chi^{2}(4,\ n = 147) = 43.94,\ p < 0.001`$, it is good to point out that the 75% agreement observed is only slightly larger than the 60% agreement expected assuming independence. We found no differences in loss aversion (for either reference‐point) for sex, marital status, student status and parental status (*t*‐test, all *p*'s \> 0.13), with one exception: non‐students had higher loss aversion parameters estimated with a 20 years RP (*t*‐test, *p* = 0.02, adjusted *p* = 0.21). ANOVA analyses suggested that loss aversion was similar across education and income levels (all *p*'s \> 0.32). Furthermore, neither measure of loss aversion was associated with age or SLE (Spearman correlation, all *p*'s \> 0.16). This lack of systematic association between loss aversion and demographics was substantiated with separate multivariate linear regressions for both $`\lambda`$ measures as dependent variables and all demographics as predictors. For both measures, none of the demographics significantly predicted $`\lambda`$ in this multivariate model (all *p*'s \> 0.23). Note also that both $`\lambda`$ measures were not correlated with $`\rho`$, that is, we find no evidence for correlations between loss aversion and discounting (Pearson *r*'s \< 0.04, *p*'s \> 0.63).

At the aggregate level, we find little evidence for discounting, as can be seen from Table <a href="#hec4529-tbl-0003" data-ref-type="table">3</a>. However, when we classify respondents using AUC, we find less evidence for linear utility. That is, the shape of $`L(T)`$ was concave for 37%, linear for 13% and convex for 49% of the sample. Hence, it appears that large heterogeneity exists in individuals' discounting. We found no significant differences in the shape of $`L(T)`$ for sex, marital status, student status and parental status (*t*‐test, all *p*'s \> 0.06), but those reporting to be religious had more convex $`L(T)`$, that is, assigning more weight to the future (*t*‐test, *p* = 0.02, adjusted *p* = 0.08). Utility curvature was not associated with age or SLE (Spearman correlation, *p*'s \> 0.06), and no differences were observed for education and income level (ANOVA, *p*'s \> 0.36). A multivariate linear regression with AUC as dependent and all demographics as predictor confirmed this finding for religion (*p* \< 0.005). Furthermore, in a multivariate model AUC was associated with age and education level (*p*'s \< 0.03), such that older individuals and individuals with a higher education level have more concave $`L(T)`$, that is, assigning more weight to health in the present. None of the other demographics was a significant predictor of the shape of $`L(T)`$ (all *p*'s \> 0.06).

### Elicited, confirmed and corrected cTTO utilities

Table <a href="#hec4529-tbl-0004" data-ref-type="table">4</a> reports the mean and median cTTO utilities elicited before and after correction (see also Figure <a href="#hec4529-fig-0001" data-ref-type="fig">1</a>), including the utilities “confirmed” by respondents in the validation task. Confirmed cTTO utilities were significantly lower than elicited cTTO utilities for all health states (paired *t*‐tests, all *p*'s \< 0.03), except for state 24443 (paired *t*‐tests, *p* = 0.39). Depending on health state, 38%–69% left cTTO utilities unchanged in the validation task (i.e., equal to elicited utilities). The median number of changes each respondent made was 3, out of 6 health states. If a change was made, this was more likely to be downwards (21%–47% of the sample) than upwards (7%–29% of the sample) for all health states.

<div id="hec4529-tbl-0004" class="table-wrap">

<div class="caption">

Mean elicited, confirmed and corrected composite time trade‐off (cTTO) utilities, with standard deviations in brackets

</div>

<table>
<thead>
<tr>
<th style="text-align: left;">State</th>
<th style="text-align: left;">11211</th>
<th style="text-align: left;">13313</th>
<th style="text-align: left;">35332</th>
<th style="text-align: left;">22434</th>
<th style="text-align: left;">24443</th>
<th style="text-align: left;">55555</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Elicited</td>
<td style="text-align: left;">0.96 (0.07)</td>
<td style="text-align: left;">0.8 (0.24)</td>
<td style="text-align: left;">0.52 (0.48)</td>
<td style="text-align: left;">0.23 (0.59)</td>
<td style="text-align: left;">−0.21 (0.66)</td>
<td style="text-align: left;">−0.68 (0.42)</td>
</tr>
<tr>
<td style="text-align: left;">Confirmed</td>
<td style="text-align: left;">0.95 (0.07)</td>
<td style="text-align: left;">0.76 (0.21)</td>
<td style="text-align: left;">0.47 (0.4)</td>
<td style="text-align: left;">0.26 (0.46)</td>
<td style="text-align: left;">−0.15 (0.56)</td>
<td style="text-align: left;">−0.72 (0.4)</td>
</tr>
<tr>
<td style="text-align: left;"><em>Sig. (Elicited vs. confirmed)</em></td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">**</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><strong>Corrected</strong></td>
</tr>
<tr>
<td style="text-align: left;">Constant alternative</td>
<td style="text-align: left;">0.93 (0.15)</td>
<td style="text-align: left;">0.7 (0.3)</td>
<td style="text-align: left;">0.4 (0.49)</td>
<td style="text-align: left;">0.09 (0.81)</td>
<td style="text-align: left;">−0.47 (1.38)</td>
<td style="text-align: left;">−0.94 (1.28)</td>
</tr>
<tr>
<td style="text-align: left;">Sig. (vs. Elicited)</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">***</td>
</tr>
<tr>
<td style="text-align: left;">Sig. (vs. Confirmed)</td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">***</td>
</tr>
<tr>
<td style="text-align: left;">Maximum BTD</td>
<td style="text-align: left;">0.93 (0.15)</td>
<td style="text-align: left;">0.67 (0.59)</td>
<td style="text-align: left;">0.22 (1.67)</td>
<td style="text-align: left;">−0.32 (3.3)</td>
<td style="text-align: left;">−1.88 (7.02)</td>
<td style="text-align: left;">−3.41 (7.79)</td>
</tr>
<tr>
<td style="text-align: left;">Sig. (vs. Elicited)</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">**</td>
</tr>
<tr>
<td style="text-align: left;">Sig. (vs. Confirmed)</td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">***</td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">*<a href="#hec4529-note-0003" data-ref-type="table-fn"> <sup>a</sup> </a></td>
</tr>
<tr>
<td colspan="7" style="text-align: left;"><strong>Differences</strong></td>
</tr>
<tr>
<td style="text-align: left;">Elicited – confirmed utilities</td>
<td style="text-align: left;">0.02 (0.04)</td>
<td style="text-align: left;">0.04 (0.11)</td>
<td style="text-align: left;">0.06 (0.21)</td>
<td style="text-align: left;">−0.02 (0.28)</td>
<td style="text-align: left;">−0.05 (0.24)</td>
<td style="text-align: left;">0.04 (0.20)</td>
</tr>
<tr>
<td style="text-align: left;">Confirmed – corrected (constant alternative)</td>
<td style="text-align: left;">0.02 (0.12)</td>
<td style="text-align: left;">0.09 (0.44)</td>
<td style="text-align: left;">0.25 (1.55)</td>
<td style="text-align: left;">0.59 (3.13)</td>
<td style="text-align: left;">1.73 (6.86)</td>
<td style="text-align: left;">2.69 (7.77)</td>
</tr>
<tr>
<td style="text-align: left;">Sig (vs. Elicited‐confirmed)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">*<a href="#hec4529-note-0004" data-ref-type="table-fn"> <sup>a</sup> </a></td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">***</td>
</tr>
<tr>
<td style="text-align: left;">Confirmed – corrected (maximum BTD)</td>
<td style="text-align: left;">0.02 (0.12)</td>
<td style="text-align: left;">0.06 (0.17)</td>
<td style="text-align: left;">0.07 (0.30</td>
<td style="text-align: left;">0.16 (0.61)</td>
<td style="text-align: left;">0.31 (1.16)</td>
<td style="text-align: left;">0.22 (1.19)</td>
</tr>
<tr>
<td style="text-align: left;">Sig (vs. Elicited‐confirmed)</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">**</td>
<td style="text-align: left;">***</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

indicates test was no longer significant after correcting for multiple testing.

\**p* \< 0.05, \*\**p* \< 0.01 and \*\*\**p* \< 0.001, indicate paired *t*‐test were significant with respectively.

</div>

<figure id="hec4529-fig-0001">
<p><img src="HEC-31-1633-g001.jpg" id="jats-graphic-1" /></p>
<p><img src="HEC-31-1633-g001.gif" /></p>
<figcaption>Mean utilities for all six health states elicited in this experiment</figcaption>
</figure>

Generally, corrected utilities were significantly lower than elicited utilities (paired *t*‐tests, all *p*'s \< 0.03), and confirmed utilities (paired *t*‐tests, all *p*'s \< 0.03). The only exception was state 35332, for which was not lower after constant alternative correction (paired *t*‐test, *p* = 0.053). Hence, although individuals adjusted their cTTO utilities downwards in the validation task, yielding lower confirmed than elicited utilities, corrected utilities were even lower. Note that these results are less pronounced when Bonferonni correction is applied (see Table <a href="#hec4529-tbl-0004" data-ref-type="table">4</a>). Interestingly, we find that for both corrective approaches for multiple states, the difference between elicited and confirmed cTTO utilities is smaller than the difference between confirmed and corrected cTTO utilities (paired *t*‐tests, all *p*'s \< 0.01). These results that the corrective approach may be “overcorrecting”, which is an issue returned to in the Discussion.

Finally, we determined whether changes in confirmed utilities were in the direction predicted by the corrective approach. That is, we classified each upward or downward change in utilities as being “predicted” whenever it was in accordance with the direction of change implied by the corrective approach, and “unpredicted” if the corrective approach predicted no change or a change in the other direction. These findings can be found in Table <a href="#hec4529-tbl-0005" data-ref-type="table">5</a>. The majority of changes made by respondents was predicted by the corrective approach, which was a significant majority for 4 out of 6 health states (Chi‐squared tests, *p*'s \< 0.004, adjusted *p*'s \< 0.025), with health state 35332 and 55555 as exceptions (Chi‐squared tests, *p*'s \> 0.06). As can be seen from Table <a href="#hec4529-tbl-0005" data-ref-type="table">5</a>, both corrective approaches yield the same qualitative results. Nonetheless, corrected utilities for constant correction were significantly lower for severe health states (in which lead‐time TTO was most likely to be encountered): that is, 24443 and 55555 (Wilcoxon tests, all *p*'s \< 0.008, adjusted *p*'s \< 0.05).

<div id="hec4529-tbl-0005" class="table-wrap">

<div class="caption">

Overview of number of respondents who made changes for confirmed utilities classified by predictions made by the corrective approach

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="6" style="text-align: left;">Constant correction</th>
</tr>
<tr>
<th style="text-align: left;"><strong>Health state</strong></th>
<th style="text-align: left;"><strong>11211</strong></th>
<th style="text-align: center;"><strong>13313</strong></th>
<th style="text-align: center;"><strong>35332</strong></th>
<th style="text-align: center;"><strong>22434</strong></th>
<th style="text-align: center;"><strong>24443</strong></th>
<th style="text-align: center;"><strong>55555</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Downward: Predicted</td>
<td style="text-align: left;">54</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">25</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">15</td>
</tr>
<tr>
<td style="text-align: left;">Downward: Unpredicted</td>
<td style="text-align: left;">3</td>
<td style="text-align: center;">20</td>
<td style="text-align: center;">35</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">12</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: left;">Upward: Predicted</td>
<td style="text-align: left;">15</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">9</td>
</tr>
<tr>
<td style="text-align: left;">Upward: Unpredicted</td>
<td style="text-align: left;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th colspan="6" style="text-align: left;">Maximum BTD correction</th>
</tr>
<tr>
<th style="text-align: left;"><strong>Health state</strong></th>
<th style="text-align: left;"><strong>11211</strong></th>
<th style="text-align: center;"><strong>13313</strong></th>
<th style="text-align: center;"><strong>35332</strong></th>
<th style="text-align: center;"><strong>22434</strong></th>
<th style="text-align: center;"><strong>24443</strong></th>
<th style="text-align: center;"><strong>55555</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Downward: Predicted</td>
<td style="text-align: left;">54</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">25</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">15</td>
</tr>
<tr>
<td style="text-align: left;">Downward: Unpredicted</td>
<td style="text-align: left;">3</td>
<td style="text-align: center;">20</td>
<td style="text-align: center;">35</td>
<td style="text-align: center;">29</td>
<td style="text-align: center;">12</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: left;">Upward: Predicted</td>
<td style="text-align: left;">15</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">19</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">9</td>
</tr>
<tr>
<td style="text-align: left;">Upward: Unpredicted</td>
<td style="text-align: left;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

</div>

## DISCUSSION

With this project we aimed to extend the corrective approach for use in valuation studies such as those used for valuation of EQ‐5D, by developing corrections for cTTO. This paper has several strengths compared to earlier work applying a corrective approach. First, it is the first applying a corrective approach with interviewer‐assisted data collection with members of the general public. Some authors have explored correction for discounting in cTTO in the general public using online self‐completed data collection (Attema & Brouwer, 2014), but this mode of administration will generally lead to lower quality data and increased no‐shows (Norman et al., 2010). Furthermore, our results may be of larger practical relevance, as cTTO utilities were obtained following the EQ‐VT protocol. Data in this project was generally of high quality, even when the interviews were facilitated through videotelephony software (see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">D</a>). Second, as parameters needed for applying a corrective approach were obtained at an individual level, this paper allows exploring heterogeneity in individuals' decision‐making in cTTO. The inclusion of the validation task developed by Lipman et al. (2020a) also enables exploring the validity of the corrective approach at the individual level.

Generally, the estimates of loss aversion and discounting are in accordance with earlier work. The median loss aversion estimate is close the initial estimate (i.e., 2.25) elicited for financial decision‐making in Kahneman and Tversky's (1979) work. Whereas earlier work has shown that loss aversion for life duration is independent of the quality of life described for its measurement (Lipman et al., 2019a), our paper adds to this literature that loss aversion is mostly unaffected by the reference‐point described (i.e., living for 10 or 20 more years). Our results for discounting suggest that the median discount function is linear, but we find large heterogeneity, suggesting that no single mean discount function can be applied to correct TTO responses and that it is sample‐specific, hence adding to the task burden of valuation studies. Such a linear curve for $`L(T)`$ was also observed in Lipman et al. (2019a), but we find large heterogeneity. Many respondents have a concave shape for $`L(T),`$ that is, reflecting positive discounting. Nonetheless, we observed negative discounting for the majority of respondents, which implies that discounting should be measured with methods flexible enough to capture both positive and negative discounting.

In this paper, we extended the corrective approach for lead‐time TTO, meaning that it can now be readily applied to correct cTTO utilities. We applied two different approaches, which differed in terms of the assumptions made about the reference‐point for lead‐time TTO. As a result, we find no difference between corrected cTTO utilities between the two approaches for relatively mild health states (as lead‐time TTO is unlikely to be required in these cases). The choice of reference‐point for the corrective approach, however, has a significant impact on corrected utilities for severe states. Future work should explore means of determining which reference‐point respondents used, for example, through decision process tracing (Pachur et al., 2018) or qualitative methods (van Osch et al., 2006). In line with our observation of no/little discounting on average, if we correct for loss aversion only, or discounting only (see Appendix <a href="#hec4529-sup-0001" data-ref-type="supplementary-material">D</a>), we find that the downward trend observed when applying a corrective approach to cTTO utilities is exclusively driven by loss aversion (as in Lipman et al., 2019c). This finding is in contrast to earlier work using the direct method that has suggested that correcting for discounting would influence TTO utilities (Attema & Brouwer, 2014). Future work should aim to replicate our results, as considered in isolation they could suggest that, if only average utilities are of importance, correcting for discounting may not be necessary.

To our knowledge, this is only the second study to ask respondents to reflect on cTTO utilities on a cardinal scale. As in the first study (Lipman et al., 2020a), we find that cTTO utilities were more likely to be adjusted downwards than upwards. Hence, these findings also appear to apply to more severe health states. Although one may be inclined to interpret this as suggesting a corrective approach is needed, at least two caveats deserve mentioning. First, our findings suggest that in most cases cTTO utilities are left unchanged. This can be interpreted multiple ways. For example, respondents may have seen no need for adjusting the elicited utilities, but it could also be argued that respondents were confused by the task and left utilities unchanged for that reason. Second, confirmed utilities may have been lower due to respondents who feel that giving up life‐years is so undesirable that improved quality of life cannot easily offset it. In the validation task, no trade‐offs are required, and hence such non‐trading may be less pronounced. The corrective approach can capture such reluctance to trade‐off life years by incorporating loss aversion to a degree, but is not applicable to lexicographic non‐trading (i.e., loss aversion predicts life years are still given up albeit reluctantly).

Interestingly, corrected utilities were generally lower than confirmed utilities. How this discrepancy should be interpreted depends on which (if any) of the cTTO utilities reported in Table <a href="#hec4529-tbl-0004" data-ref-type="table">4</a>, one views as the best representation of individuals' judgments about the value of impaired relative to perfect health. Elicited cTTO utilities were highest and were derived with the state‐of‐the‐art approach used for health state valuation in practice (Stolk et al., 2019). However, one may feel that these utilities are unfit as benchmark, given that they are obtained while assuming no discounting or loss aversion. Both current literature and findings reported in this study provide ample challenge of these assumptions. It is not clear, on the other hand, if confirmed cTTO utilities provide a suitable benchmark to compare against. Confirmed cTTO utilities were obtained after respondents considered the goal of health state valuation and the scaling used for QALYs. Respondents that adjusted elicited utilities may have identified cases in which health states were assigned utilities that are too high or low, suggesting that corrected utilities are lower than necessary. The latter statement, would, however, appear to assign respondents significant introspective capability and sophistication, as it assumes they are able to identify most or all cases of biased elicited utilities and the method used for adjustment is not biased. Moreover, it is widely believed that preferences are shaped by the task with which they are elicited (Braga & Starmer, 2005), and hence any differences between confirmed and elicited utilities and cTTO utilities may merely be reflections of the different tasks used. Furthermore, it is well‐known that individuals may be “anchoring” on previous information (Tversky & Kahneman, 1974), in this case elicited utilities, and as a result adjust insufficiently. Thus, an argument may as well be made in favor of the lower corrected utilities to be used as benchmark, if one believes individuals' adjustments were only partial. Hence, given that it is debatable if true “utilities” exist or can be measured (Braga & Starmer, 2005), the interpretation of the utilities presented in this paper and the differences between them remains unclear. Additional work discussing the psychological realism and normative implications of the corrective approach appears warranted (e.g., Infante et al., 2016).

Nonetheless, three limitations of using the corrective approach developed in this paper should be mentioned. First, correcting cTTO utilities involves taking into account additional error in health state valuation. That is, measurement of time preference and loss aversion is subject to error, which may be especially true for chained methods such as the non‐parametric method (Abdellaoui et al., 2016) and the direct method (Attema et al., 2012). Although earlier work suggested there is little evidence for error propagation in such chained methods (Bleichrodt & Pinto, 2000; Lipman et al., 2019c), the two additional parameters required to correct elicited cTTO utilities may increase variability in utilities. However, when utilities are applied in practice, this is often based on the average of the point estimates as estimated from a tariff, disregarding the parameter uncertainty in the tariff itself (for a discussion, see: Devlin et al., 2017). Information about the variance in utilities is, thus, typically disregarded (for an exception, see: Versteegh et al., 2019). Second, the corrective approach implies that cTTO utilities are no longer bounded at −1, and as a result, utilities for WTD health states were much lower after correction. In this study, this may be problematic as the scale used to confirmed utilities was bounded at −1, which may also explain why confirmed utilities were higher than corrected utilities. The lack of a lower bound may be seen as problematic in practice (Tilling et al., 2010), but there is no normative basis for such a lower bound to exist. In fact, the cTTO approach applied in EQ‐VT arbitrarily sets this bound at −1 and if alternative approaches for valuation of WTD health states would have been incorporated, the lower bound would have been different (Attema et al., 2013; Attema & Versteegh, 2013; Augustovski et al., 2013). Third, in line with Lipman et al. (2019c) the corrective approach applied in this paper models loss aversion for life duration only. That is, life duration that exceeds some reference‐point is considered to be gained, whereas life duration that falls short of the reference‐point is considered lost. In this approach, the health state experienced in the life duration gained or lost does not impact loss aversion. This may have somewhat counterintuitive consequences, as for example, life years in a state WTD that exceed the reference‐point would be considered to be gained, whereas life years “given up” compared to a reference‐point in a state WTD are considered losses (and thus multiplied by a coefficient capturing loss aversion). This limitation may be addressed in future work expanding our approach to include loss aversion for $`Q`$, although this may be challenging given that $`Q`$ is typically considered a qualitative measure for which loss aversion is undefined (Bleichrodt & Miyamoto, 2003).

To conclude, in this paper we have provided the foundations for the corrective approach to be used for health state valuation in practice. The methods used for measuring loss aversion and discounting were applied in a sample of the general public, and the corrective approach was extended to incorporate lead‐time TTO in cTTO. As in earlier work, correction has a downward effect on cTTO utilities for both mild and severe health states, which is largely driven by correction for loss aversion. The need to correct for loss aversion depends, however on which reference‐point is taken by respondents, and the required methods for enabling such correction have only recently been developed. Even though loss aversion appears a robust phenomenon in decisions about health, whether and how to account for its influence in health state valuation are still open questions.

## CONFLICT OF INTEREST

Matthijs Versteegh is a member of the EuroQol Group. All authors have received research grants from the EuroQol Research Foundation for work outside the scope of the submitted work.

## Supporting information

<div class="caption">

Supplementary Material

</div>

<div class="caption">

Click here for additional data file.

</div>

## ACKNOWLEDGEMENTS

The views expressed by the authors do not necessarily reflect the views of the EuroQol group. We also gratefully acknowledge the valuable assistance and comments provided by Elly Stolk and Benjamin Craig. This study was made possible through funding provided by the EuroQol Research Foundation (project number: 20190080R1).

Lipman, S. A. , Attema, A. E. , & Versteegh, M. M. (2022). Correcting for discounting and loss aversion in composite time trade‐off. Health Economics, 31(8), 1633–1648. 10.1002/hec.4529

## ENDNOTES

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

## References

1. Abdellaoui, M. , Bleichrodt, H. , L’haridon, O. , & Van Dolder, D. (2016). Measuring loss aversion under ambiguity: A method to make prospect theory completely observable. Journal of Risk and Uncertainty, 52, 1–20. 10.1007/s11166-016-9234-y

2. Alava, M. H. , Pudney, S. , & Wailoo, A. (2020). The EQ‐5D‐5L value set for England: Findings of a quality assurance program. Value in Health, 23(5), 642–648. doi:10.1016/j.jval.2019.10.017

3. Attema, A. E. , Bleichrodt, H. , & Wakker, P. P. (2012). A direct method for measuring discounting and QALYs more easily and reliably. Medical Decision Making, 32(4), 583–593. 10.1177/0272989x12451654

4. Attema, A. E. , & Brouwer, W. B. (2009). The correction of TTO‐scores for utility curvature using a risk‐free utility elicitation method. Journal of Health Economics, 28(1), 234–243. 10.1016/j.jhealeco.2008.10.004

5. Attema, A. E. , & Brouwer, W. B. (2014). Deriving time discounting correction factors for TTO tariffs. Health Economics, 23(4), 410–425. 10.1002/hec.2921

6. Attema, A. E. , & Versteegh, M. M. (2013). Would you rather be ill now, or later? Health Economics, 22(12), 1496–1506. 10.1002/hec.2894

7. Attema, A. E. , Versteegh, M. M. , Oppe, M. , Brouwer, W. B. , & Stolk, E. A. (2013). Lead time TTO: Leading to better health state valuations? Health Economics, 22(4), 376–392. 10.1002/hec.2804

8. Augustovski, F. , Rey‐Ares, L. , Irazola, V. , Oppe, M. , & Devlin, N. J. (2013). Lead versus lag‐time trade‐off variants: Does it make any difference? The European Journal of Health Economics, 14(3), 25–31. 10.1016/j.jval.2013.03.205

9. Bleichrodt, H. (2002). A new explanation for the difference between time trade‐off utilities and standard gamble utilities. Health Economics, 11(5), 447–456. 10.1002/hec.688

10. Bleichrodt, H. , & Miyamoto, J. (2003). A characterization of quality‐adjusted life‐years under cumulative prospect theory. Mathematics of Operations Research, 28(1), 181–193. 10.1287/moor.28.1.181.14261

11. Bleichrodt, H. , & Pinto, J. L. (2000). A parameter‐free elicitation of the probability weighting function in medical decision analysis. Management Science, 46(11), 1485–1496. 10.1287/mnsc.46.11.1485.12086

12. Braga, J. , & Starmer, C. (2005). Preference anomalies, preference elicitation and the discovered preference hypothesis. Environmental and Resource Economics, 32(1), 55–89. 10.1007/s10640-005-6028-0

13. Devlin, N. , Shah, K. , & Buckingham, K. (2017). What is the normative basis for selecting the measure of “average” preferences for use in social choices. OHE research paper. Office of Health Economics. https://www.ohe.org/system/files/private/publications/OHE%20RP%20(Devlin%20et%20al.%20average%20preferences)%20FINAL.pdf

14. Drummond, M. F. , Sculpher, M. J. , Claxton, K. , Stoddart, G. L. , & Torrance, G. W. (2015). Methods for the economic evaluation of health care programmes. Oxford university press.

15. Infante, G. , Lecouteux, G. , & Sugden, R. (2016). Preference purification and the inner rational agent: A critique of the conventional wisdom of behavioural welfare economics. Journal of Economic Methodology, 23, 1–25. 10.1080/1350178x.2015.1070527

16. Kahneman, D. , & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263–291. 10.2307/1914185

17. Kemel, E. , & Paraschiv, C. (2018). Deciding about human lives: An experimental measure of risk attitudes under prospect theory. Social Choice and Welfare, 51(1), 163–192. 10.1007/s00355-018-1111-y

18. Köbberling, V. , & Wakker, P. P. (2005). An index of loss aversion. Journal of Economic Theory, 122(1), 119–131. 10.1016/j.jet.2004.03.009

19. Lipman, S. A. (2020). Time for tele‐TTO? Lessons learned from digital interviewer‐assisted time trade‐off data collection. The Patient, 14(5), 459–469. 10.1007/s40271-020-00490-z

20. Lipman, S. A. , & Attema, A. E. (2020). Good things come to those who wait—decreasing impatience for health gains and losses. PLoS One, 15(3), e0229784. 10.1371/journal.pone.0229784

21. Lipman, S. A. , Brouwer, W. B. , & Attema, A. E. (2019a). A QALY loss is a QALY loss is a QALY loss: A note on independence of loss aversion from health states. The European Journal of Health Economics, 20(3), 419–426. 10.1007/s10198-018-1008-9

22. Lipman, S. A. , Brouwer, W. B. F. , & Attema, A. E. (2019b). The corrective approach: Policy implications of recent developments in QALY measurement based on prospect theory. Value in Health, 22(7), 816–821. 10.1016/j.jval.2019.01.013

23. Lipman, S. A. , Brouwer, W. B. F. , & Attema, A. E. (2019c). QALYs without bias? Non‐parametric correction of time trade‐off and standard gamble weights based on prospect theory. Health Economics, 28(7), 843–854. 10.1002/hec.3895

24. Lipman, S. A. , Brouwer, W. B. , & Attema, A. E. (2020a). What’s it going to be, TTO or SG? A direct test of the validity of health state valuation. Health Economics, 29(11), 1475–1481. doi:10.1002/hec.4131

25. Lipman, S. A. , Brouwer, W. B. F. , & Attema, A. E. (2020b). Living up to expectations: Experimental tests of subjective life expectancy as reference point in time trade‐off and standard gamble. Journal of Health Economics, 71, 102318. 10.1016/j.jhealeco.2020.102318

26. Miyamoto, J. M. , Wakker, P. P. , Bleichrodt, H. , & Peters, H. J. (1998). The zero‐condition: A simplifying assumption in QALY measurement and multiattribute utility. Management Science, 44(6), 839–849. 10.1287/mnsc.44.6.839

27. NICE . (2018). Guide to the processes of technology appraisal. In N. I. F. H. A. C. (Ed.), Excellence. https://www.nice.org.uk/Media/Default/About/what-we-do/NICE-guidance/NICE-technology-appraisals/technology-appraisal-processes-guide-apr-2018.pdf

28. Norman, R. , King, M. T. , Clarke, D. , Viney, R. , Cronin, P. , & Street, D. (2010). Does mode of administration matter? Comparison of online and face‐to‐face administration of a time trade‐off task. Quality of Life Research, 19(4), 499–508. 10.1007/s11136-010-9609-5

29. Oppe, M. , Devlin, N. J. , Van hout, B. , Krabbe, P. F. , & De Charro, F. (2014). A program of methodological research to arrive at the new international EQ‐5D‐5L valuation protocol. Value in Health, 17(4), 445–453. 10.1016/j.jval.2014.04.002

30. Pachur, T. , Schulte‐Mecklenbeck, M. , Murphy, R. O. , & Hertwig, R. (2018). Prospect theory reflects selective allocation of attention. Journal of Experimental Psychology: General, 147(2), 147–169. 10.1037/xge0000406

31. Pliskin, J. S. , Shepard, D. S. , & Weinstein, M. C. (1980). Utility functions for life years and health status. Operations Research, 28(1), 206–224. 10.1287/opre.28.1.206

32. Ramos‐goñi, J. M. , Oppe, M. , Stolk, E. , Shah, K. , Kreimeier, S. , Rivero‐Arias, O. , & Devlin, N. (2020). International valuation protocol for the EQ‐5D‐Y‐3L. PharmacoEconomics, 1–11. doi:10.1007/s40273-020-00909-3

33. Shalev, J. (2002). Loss aversion and bargaining. Theory and Decision, 52(3), 201–232. 10.1023/a:1019674323804

34. Stolk, E. , Ludwig, K. , Rand, K. , Van Hout, B. , & Ramos‐Goñi, J. M. (2019). Overview, update, and lessons learned from the international EQ‐5D‐5L valuation work: Version 2 of the EQ‐5D‐5L Valuation Protocol. Value in Health, 22(1), 23–30. 10.1016/j.jval.2018.05.010

35. Tilling, C. , Devlin, N. , Tsuchiya, A. , & Buckingham, K. (2010). Protocols for time tradeoff valuations of health states worse than dead: A literature review. Medical Decision Making, 30(5), 610–619. 10.1177/0272989x09357475

36. Tversky, A. , & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131. 10.1126/science.185.4157.1124

37. Tversky, A. , & Kahneman, D. (1992). Advances in prospect theory: Cumulative representation of uncertainty. Journal of Risk and Uncertainty, 5(4), 297–323. 10.1007/bf00122574

38. Van Der Pol, M. , & Roux, L. (2005). Time preference bias in time trade‐off. The European Journal of Health Economics, 6(2), 107–111. 10.1007/s10198-004-0265-y

39. Van Der Pol, M. M. , & Cairns, J. A. (2000). Negative and zero time preference for health. Health Economics, 9(2), 171–175. 10.1002/(sici)1099-1050(200003)9:2<171::aid-hec492>3.0.co;2-z

40. Van Nooten, F. , & Brouwer, W. (2004). The influence of subjective expectations about length and quality of life on time trade‐off answers. Health Economics, 13(8), 819–823. 10.1002/hec.873

41. Van Nooten, F. , Van Exel, N. , Eriksson, D. , & Brouwer, W. (2016). Back to the future: Influence of beliefs regarding the future on TTO answers. Health and Quality of Life Outcomes, 14(1), 4. 10.1186/s12955-015-0402-6

42. Van Osch, S. M. , Van Den Hout, W. B. , & Stiggelbout, A. M. (2006). Exploring the reference point in prospect theory: Gambles for length of life. Medical Decision Making, 26(4), 338–346. 10.1177/0272989x06290484

43. Van Osch, S. M. , Wakker, P. P. , Van Den Hout, W. B. , & Stiggelbout, A. M. (2004). Correcting biases in standard gamble and time tradeoff utilities. Medical Decision Making, 24(5), 511–517. 10.1177/0272989x04268955

44. Van Osch, S. M. C. (2007). The construction of health state utilities. Leiden University.

45. Versteegh, M. M. , Ramos, I. C. , Buyukkaramikli, N. C. , Ansaripour, A. , Reckers‐Droog, V. T. , & Brouwer, W. B. (2019). Severity‐adjusted probability of being cost effective. PharmacoEconomics, 37(9), 1155–1163. 10.1007/s40273-019-00810-8

46. Versteegh, M. M. , Vermeulen, K. M. , M A A Evers, S. , Evers, S. M. , De Wit, G. A. , Prenger, R. , A Stolk, E. , & Stolk, E. A. (2016). Dutch tariff for the five‐level version of EQ‐5D. Value in Health, 19(4), 343–352. 10.1016/j.jval.2016.01.003

47. Wouters, S. , Van Exel, N. J. , Rohde, K. I. , & Brouwer, W. B. (2015). Are all health gains equally important? An exploration of acceptable health as a reference point in health care priority setting. Health and Quality of Life Outcomes, 13(1), 79. 10.1186/s12955-015-0277-6

48. ZINL . (2015). Richtlijn voor het uitvoeren van economische evaluaties in de gezondheidszorg. Zorginstituut Nederland. https://www.zorginstituutnederland.nl/publicaties/publicatie/2016/02/29/richtlijn-voor-het-uitvoeren-van-economische-evaluaties-in-de-gezondheidszorg

## Associated Data

### Supplementary Materials

<div class="caption">

Supplementary Material

</div>

<div class="caption">

Click here for additional data file.

</div>

### Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

[^1]: Note that the two reference‐points were included as we expected a priori that both could be relevant for correcting cTTO depending on the reference‐point assumed. However, in the final specification only $`\lambda`$ elicited with a 10 year reference‐point is needed in Equations <a href="#hec4529-disp-0009" data-ref-type="disp-formula">(8</a>) and <a href="#hec4529-disp-0013" data-ref-type="disp-formula">(12</a>).

[^2]: *T* <sub> *d*1/2</sub> stands for the time point up until which half of the total utility of life duration is experienced, as explained in the remainder of this paragraph.

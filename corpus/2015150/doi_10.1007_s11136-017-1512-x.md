---
project_id: "2015150"
work_id: "doi:10.1007/s11136-017-1512-x"
doi: "10.1007/s11136-017-1512-x"
pmid: "28185039"
pmcid: "PMC5420378"
title: "Cultural values: can they explain self-reported health?"
journal: "Quality of Life Research"
publication_date: "2017-02-10"
volume: "26"
issue: "6"
authors:
  - name: "Bram Roudijk"
    affiliation_ids:
      - "Aff1"
  - name: "Rogier Donders"
    affiliation_ids:
      - "Aff1"
  - name: "Peep Stalmeier"
    affiliation_ids:
      - "Aff1"
affiliations:
  - id: "Aff1"
    name: "Radboud University Medical Center, Radboud Institute for Health Sciences, Nijmegen, The Netherlands"
licence: "cc-by"
source_file: "input/projects/2015150/papers/doi_10.1007_s11136-017-1512-x.xml"
source_url: "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5420378/fullTextXML"
source_method: "epmc_xml"
source_sha256: "fd5d55ec8aec95ec877b838f8d9e60929a6324387a284d47c9e5741697cf55e7"
converter: "scripts/to_markdown.py"
converter_version: 1
pandoc: "3.10"
---

# Cultural values: can they explain self-reported health?

## Abstract

### Purpose

Self-reported health (SRH) is a measure widely used in health research and population studies. Differences in SRH have been observed between countries and cultural values have been hypothesized to partly explain such differences. Cultural values can be operationalized by two cultural dimensions using the World Values Survey (WVS), namely the traditional/rational–secular and the survival/self-expression dimension. We investigate whether there is an association between the WVS cultural dimensions and SRH, both within and between countries.

### Methods

Data from 51 countries in the WVS is used and combined with macroeconomic data from the Worldbank database. The association between SRH and the WVS cultural dimensions is tested within each of the 51 countries and multilevel mixed models are used to test differences between these countries. Socio-demographic and macroeconomic variables are used to correct for non-cultural variables related to SRH.

### Results

Within countries, the survival/self-expression dimension was positively associated with SRH, while in most countries there was a negative association for the traditional/rational–secular dimension. Values range between 4 and 17% within countries. Further analyses show that the associations within countries and between countries are similar. Controlling for macroeconomic and socio-demographic factors did not change our results.

### Discussion

The WVS cultural dimensions predict SRH within and between countries. Contrary to our expectations, traditional/rational–secular values were negatively associated with SRH. As SRH is associated with cultural values between countries, cultural values could be considered when interpreting SRH between countries.

**Keywords:** Self-reported health, Cultural values, World Values Survey, Multilevel modeling

Accepted 2017 Jan 20; Issue date 2017.

## Introduction

Self-reported health (SRH) is one of the most widely used health measures in academic research and is often included in population surveys, such as the European SHARE \[1\], the worldwide OECD PIAAC \[2\] studies, and the European Union Eurostat statistical bureau. It is used in demographic studies as a proxy for health or as an effective predictor for mortality \[3, 4\]. SRH has been studied extensively, but much remains unknown about the determinants of SRH. Several correlates have been proposed, mostly referring to respondents’ socio-demographic factors such as age, gender, education and social class \[5–8\]. Income and income inequality have been reported as important determinants for SRH \[9, 10\]. In this study, we consider culture as a determinant of SRH and use it to explain differences in SRH between countries.

Culture has been described as “The rich complex of meanings, beliefs, practices, symbols, norms and values prevalent among people in a society” \[11\]. Alternatively, as described by Hofstede et al. \[12\], culture consists of values and practices shared by a group. In general, values are related to norms wherein norms provide rules for behavior in specific situations, and values identify what should be judged as good or evil \[13\]. Alternatively, values have been defined as a set of stable, general beliefs that emerge from societal norms and individual psychological needs \[14\]. Scholars differ on how cultural values should be theorized. Schwartz has developed three cultural value dimensions, while other researchers, such as Hofstede et al. \[12\] and Rokeach \[13\] have developed theories on cultural values with even more cultural dimensions. Inglehart \[15\], Inglehart and Baker \[16\] has derived two cultural dimensions, using the World Values Survey (WVS). These dimensions, to be explained below, are labeled as “traditional versus rational/secular” and “survival versus self-expression”. Cultural values are known to differ between countries \[17\], which is illustrated by the Inglehart–Welzel cultural map \[18, 19\].

Having introduced cultural values, we consider their possible role in SRH within and between countries. Within countries, there is evidence that cultural values play a role in SRH. Zola has compared symptoms reported by Italian-American and Irish-American patients with an identical diagnosis \[20, 21\]. The Irish-Americans tended to attribute their complaints mainly to specific parts of the body such as the eye or ear, while expressing that they did not experience much pain. The Italian-Americans reported more vague complaints and stated that the complaints were interfering with their everyday lives, while also reporting more pain than the Irish-Americans. Summarizing, Zola showed that people from different cultures communicate differently about their health. A study by Diener et al. on well-being \[22\] is also relevant as well-being is related to SRH \[23–25\]. Diener states that people with characteristics valued within their culture tend to feel happier \[22\]. For example, they have found that self-esteem predicts well-being better in individualistic cultures than in collectivistic cultures \[26\]. These studies suggest that within countries, SRH may be influenced by cultural values.

Between countries, several studies have found evidence for a role of cultural values on SRH. Jürges found differences in mean SRH between countries and hypothesizes that cultural values may explain those differences \[27\]. Mackenbach \[28\] has studied the relation between health and cultural dimensions over European countries and found significant relations between these cultural dimensions and a variety of health behaviors, health outcomes and health policies. Diener et al. \[29\] report that well-being differs between cultures and offers different cultural standards for feeling and expressing positive emotions as a cause \[22, 30\]. These studies suggest that an association exists between cultural values and SRH, but now between countries.

The above findings give rise to the hypothesis that cultural values are related to SRH. The aim of this study is then to determine such a relation exists, both within and between countries. This leads to the following two research questions:

1.  Is there an association between the WVS cultural dimensions and self-reported health within countries?

2.  Is there an association between the WVS cultural dimensions and self-reported health between countries?

We formulate the following hypotheses. First, findings within countries suggest cultural values determine how people perceive their health \[20–22\]. This could lead to differences in SRH. Therefore, we hypothesize an association between cultural values and SRH within countries. Second, based on the evidence of Jürges \[27\], Mackenbach \[28\] and Diener \[29\], we hypothesize that there is an association between cultural values and SRH between countries. Third, as wealthier countries, with more sophisticated health care, tend to have positive scores on the two WVS cultural dimensions, we hypothesize that the WVS cultural dimensions are positively associated to SRH.

## Methods

### Rationale

The association found between countries, the ecological level, may not be representative for the associations within countries, the individual level, which troubles the interpretation of associations between countries. For instance, a positive association for cultural values and SRH may exist between countries, while a negative association exists within countries. Extrapolating the between country level to the individual level would then lead to a false inference. This problem is called the ecological fallacy. To avoid it, we assess the associations both between and within countries. Thus between country associations can be interpreted in the light of within country associations. Socio-demographic factors will be used as control variables, as their importance for SRH has been shown in previous studies. Macroeconomic variables are also included as control variables, as they can account for non-cultural differences between countries and are shown to be correlated with happiness \[31\].

### Measures

To fulfill the aims of this research paper, cultural values need to be operationalized into a quantifiable concept that discriminates between countries. The World Values Survey (WVS) Association has done so and their data is used here. The World Values Survey Longitudal Data \[32\] and the European Values Survey Longitudinal Data (EVS) \[33\] were merged to create the Integrated Values Survey (IVS) database, using the protocol provided by the WVS \[34\]. This dataset includes almost 100 countries, up to 6 waves per country, containing at least 1000 respondents per country and wave in most cases. The dataset contains 506,268 unique respondents and respondents only participate in one single wave. The sampling scheme is representative in each country \[35\]. The survey includes composite cultural values, socio-demographic variables and SRH. The IVS allows for a computation of two composite cultural dimensions: survival versus self-expression and traditional versus rational/secular.

Figure <a href="#Fig1" data-ref-type="fig">1</a> shows how the two composite cultural dimensions are described, based on factor analysis of 10 items. In the upper left of Fig. <a href="#Fig1" data-ref-type="fig">1</a>, survival values emphasize economic and physical security and have low levels of trust and tolerance. In the lower left, self-expression values correspond with higher levels of trust, tolerance and political activism. The upper right shows that traditional values are related to religion, authority, national pride, and parent–child ties. The lower right of the table shows rational–secular values, which are the opposite of traditional values. The two cultural variables are continuous. Negative scores on the traditional/rational–secular variable indicate that respondents have traditional values, while a positive score indicate that respondents have rational–secular values. Negative scores on the survival/self-expression dimension indicate that respondent have more survival values, while positive scores indicate self-expression values.

<figure id="Fig1">
<p><img src="11136_2017_1512_Fig1_HTML.jpg" id="d29e404" /></p>
<p><img src="11136_2017_1512_Fig1_HTML.gif" /></p>
<figcaption>The cultural dimensions and their factor items</figcaption>
</figure>

WVS researchers Ronald Inglehart and Christian Welzel have been able to create the Inglehart–Welzel cultural map \[18, 19\], which illustrates that countries can be differentiated by cultural values. European countries and English speaking countries score high on both self-expression and rational/secular values, while African and Islamic countries score low on these values. Asian and former Soviet countries score high on rational/secular, but lower on self-expression. Lastly, Latin American countries score high on self-expression and lower on secular/rational values.

The WVS and EVS databases contain a variety of socio-demographic variables, such as gender, education, income, self-perceived social class and age. Gender is coded as 0 for female and 1 for male. Education, income (position in the scale of incomes from lowest to highest) and self-reported social class are categorical variables that have 1 as lowest value and 5 or 10 as highest values. Self-reported health was a categorical variable coded as (1) Very good, (2) Good, (3) Fair, (4) Poor or (5) Very poor. SRH was reversed to (5) very good health to (1) very poor health. Macroeconomic data is obtained from the World Bank \[36\]. The macroeconomic variables are country level variables and include GDP per capita (Gross Domestic Product, a measure of wealth within a country, PPP 2011 US dollars), government health expenditure as percentage of the GDP, life expectancy at birth, total health expenditure per capita (PPP, 2011 US dollars) and out of pocket expenditure on health (as percentage of total spending on health).

### Analyses

For research question 1, information is needed on the coefficients of the association between cultural values and SRH, which will be provided by models 1 and 2. Regressions are performed for each country separately. In both models, SRH is the dependent variable and the two cultural dimensions are the independent variables. Model 2 also includes socio-demographic variables.

``` math
\text{SR}\text{H}_{i} = \mathit{\beta}_{i0} + \mathit{\beta}_{i1}\text{Tradrat} + \mspace{600mu}\mathit{\beta}_{i2}\,\text{Survself} + \mathit{\varepsilon}
```

``` math
\text{SR}\text{H}_{i} = \mathit{\beta}_{i0} + \mathit{\beta}_{i1}\text{Tradrat} + \mspace{600mu}\mathit{\beta}_{i2}\,\text{Survself} + {\overline{\mathit{\beta}}}_{i3}\overline{\text{Socio}} + \mathit{\varepsilon}\mspace{600mu}
```

A subscript $`i`$ indicates a country, while variables and parameters with bars on top indicate that the parameter is a vector of control variables and their $`\mathit{\beta}`$’s. $`{\overline{\mathit{\beta}}}_{i3}\overline{\text{Socio}}`$ contains for example, the variables age, gender, scale of incomes, social class (subjective) and education, each with their own slope $`{\overline{\mathit{\beta}}}_{i3}`$ for each of the $`i`$ countries. Abbreviations are used to indicate the two cultural dimensions and the random error term is denoted by $`\mathit{\varepsilon}`$.

To test whether the intercepts and slopes from model 1 and 2 differ between countries, models 3, 4 and 5 are constructed. These multilevel mixed effects models include random slopes for the cultural variables and random country dependent intercepts. SRH is the dependent variable, the WVS cultural dimensions are the independent variables and country is the level variable.

``` math
\text{SRH} = \left( {\mathit{\beta}_{0} + \mathit{\mu}_{0}} \right) + \left( {\mathit{\beta}_{1} + \mathit{\mu}_{1}} \right)\text{Tradrat} + \left( {\mathit{\beta}_{2} + \mathit{\mu}_{2}} \right)\text{Survself} + \mathit{\varepsilon}
```

``` math
\text{SRH} = \left( {\mathit{\beta}_{0} + \mathit{\mu}_{0}} \right) + \left( {\mathit{\beta}_{1} + \mathit{\mu}_{1}} \right)\text{Tradrat} + \left( {\mathit{\beta}_{2} + \mathit{\mu}_{2}} \right)\text{Survself} + \overline{\mathit{\beta}_{3}}\mspace{600mu}\overline{Socio} + \mathit{\varepsilon}\sqrt{2}
```

``` math
\text{SRH} = \left( {\mathit{\beta}_{0} + \mathit{\mu}_{0}} \right) + \left( {\mathit{\beta}_{1} + \mathit{\mu}_{1}} \right)\text{Tradrat} + \left( {\mathit{\beta}_{2} + \mathit{\mu}_{2}} \right)\text{Survself} + {\overline{\mathit{\beta}}}_{3}\,\overline{\text{Socio}} + {\overline{\mathit{\beta}}}_{4}\mspace{600mu}\overline{\text{Macro}} + \mspace{600mu}\mathit{\varepsilon}
```

The mixed models can be interpreted as following: $`\left( {\mathit{\beta}_{0} + \mathit{\mu}_{0}} \right)`$ is the intercept for each country, with a fixed part $`\mathit{\beta}_{0}`$ and a random part $`\mathit{\mu}_{0}`$, which allows for a constant intercept and a country dependent deviation of the intercept. $`\left( {\mathit{\beta}_{1} + \mathit{\mu}_{1}} \right)`$ and $`\left( {\mathit{\beta}_{2} + \mathit{\mu}_{2}} \right)`$ are the slopes for the cultural dimensions and consist of a fixed part $`\mathit{\beta}_{1}`$ or $`\mathit{\beta}_{2}`$ and a random, country dependent part $`\mathit{\mu}_{1}`$ or $`\mathit{\mu}_{2}`$, which allows again for a constant slope and a country dependent deviation of the slope. We assume that $`\mathit{\mu}_{0}`$, $`\mathit{\mu}_{1}`$ and $`\mathit{\mu}_{2}`$ are multivariate normally distributed with mean 0 and have an unstructured covariance matrix. If a random effect is significant, corresponding intercept or slopes differ reliably between countries. Again, socio-demographic variables are included in model 4. Model 5 adds macroeconomic control variables, to account for non-cultural differences between countries. Socio-demographic and macroeconomic variables are centered in all the models, creating a mean of 0 for all these variables.

For research question 2, information is needed about the association between countries. As multilevel models do not generate such an association between countries, a simple regression analysis with country level values for the cultural values and SRH was performed, to determine an association for the cultural dimensions and SRH between countries. Model 6 provides a mathematical representation of this regression analysis.

``` math
\text{SRH} = \mspace{600mu}\mathit{\beta}_{0} + \mathit{\beta}_{1}\text{Tradrat} + \mathit{\beta}_{2}\text{Survself} + {\overline{\mathit{\beta}}}_{3}\,\overline{\text{Socio}} + \mathit{\varepsilon}
```

As in the earlier models, $`{\overline{\mathit{\beta}}}_{3}\,\overline{\text{Socio}}`$ is a vector of socio-demographic variables and their slopes.

## Results

A sample from the IVS was obtained, including 506,268 respondents. Some of the macroeconomic data was not available for the first two waves of the WVS, which led to the exclusion of the first two waves. The unavailable macroeconomic data concerns mostly health-related variables, while variables such as GDP per capita were available and led to the exclusion of 92,456 cases. Furthermore, not all questions were asked in each country and wave, which led to the exclusion of 142,468 more cases. Missing macroeconomic data and unasked questions reduced the dataset to 271,344 cases. An additional 113,761 cases contained missing values for SRH, the cultural values or socio-demographic data, leaving 157,583 cases from 51 countries to be used for our within-country analyses. The mixed models contained a minimum of 45 countries, totaling 100,590 respondents. The difference between the sample sizes of the regression models and the mixed models is caused by missing macroeconomic data, mainly in wave 3 of the WVS. No data estimation for missing data was used.

Means of SRH differ per country; all countries in the sample have a mean between 3.1 and 4.4. Figure <a href="#Fig2" data-ref-type="fig">2</a> illustrates that countries can be mapped into a two-dimensional plane, based on their scores on the two cultural dimensions and shows whether the country mean is below (black dot) or above (white dot) the median (3.85) of SRH.

<figure id="Fig2">
<p><img src="11136_2017_1512_Fig2_HTML.jpg" id="d29e1245" /></p>
<p><img src="11136_2017_1512_Fig2_HTML.gif" /></p>
<figcaption>Cultural map, by mean SRH</figcaption>
</figure>

Regressions for SRH and cultural values were performed for 51 countries, using models 1 and 2. The coefficients for each cultural dimension per country are presented in histograms in Figs. <a href="#Fig3" data-ref-type="fig">3</a> and <a href="#Fig4" data-ref-type="fig">4</a>. The coefficients for the traditional/rational–secular variable are represented by the white bars in the histograms, while the coefficients for the survival/self-expression variable are represented by the grey bars. Figure <a href="#Fig3" data-ref-type="fig">3</a> shows the regressions without socio-demographic variables (averages are 0.258 for the survival/self-expression variable and − 0.089 for the traditional/rational–secular variable, while $`R^{2}`$ values ranged between 4 and 17% within each country), Fig. <a href="#Fig4" data-ref-type="fig">4</a> shows the regression coefficients that are corrected for socio-demographic variables (averages are 0.178 for the survival/self-expression variable and − 0.140 for the traditional/rational–secular variable, $`R^{2}`$ values ranged between 6 and 37% within each country).

<figure id="Fig3">
<p><img src="11136_2017_1512_Fig3_HTML.jpg" id="d29e1257" /></p>
<p><img src="11136_2017_1512_Fig3_HTML.gif" /></p>
<figcaption>Regression coefficients per country for model 1</figcaption>
</figure>

<figure id="Fig4">
<p><img src="11136_2017_1512_Fig4_HTML.jpg" id="d29e1269" /></p>
<p><img src="11136_2017_1512_Fig4_HTML.gif" /></p>
<figcaption>Regression coefficients per country for model 2, including socio-demographic variables</figcaption>
</figure>

The results of the mixed models, Eqs. (<a href="#Equ3" data-ref-type="disp-formula">3</a>), (<a href="#Equ4" data-ref-type="disp-formula">4</a>) and (<a href="#Equ5" data-ref-type="disp-formula">5</a>), are presented in Table <a href="#Tab1" data-ref-type="table">1</a>. Model 3 contained only cultural variables, while model 4 includes socio-demographic control variables and model 5 contained both socio-demographic and macroeconomic control variables. The upper part of the table shows the coefficients of the fixed effects for each model. These fixed effects represent the average slopes of the cultural variables and the average intercept within countries. Socio-demographic and macroeconomic control variables are also included. Random effects are presented in the lower part of the table and represent the variation from the fixed effect for that variable between countries, expressed as a standard deviation. There is again a significant association between cultural values and SRH, which can be seen from the coefficients for the fixed effects. For the traditional/rational–secular variable, there is a negative association with SRH, while there is a positive association for the survival/self-expression variable and SRH. The random effects for the cultural variables and the constant are significant as well, indicating that the slopes of these variables differ between countries.

<div id="Tab1" class="table-wrap">

<div class="caption">

Mixed effects models with self-reported health as the dependent variable

</div>

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">Model 3<br />
<span class="math inline"><em>N</em> = 157, 583</span></th>
<th style="text-align: left;">Model 4<br />
<span class="math inline"><em>N</em> = 157, 583</span></th>
<th style="text-align: left;">Model 5<br />
<span class="math inline"><em>N</em> = 100, 590</span></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">Fixed effects</td>
</tr>
<tr>
<td style="text-align: left;"> Traditional/rational–secular</td>
<td style="text-align: center;">−0.071**</td>
<td style="text-align: center;">−0.122**</td>
<td style="text-align: center;">−0.140**</td>
</tr>
<tr>
<td style="text-align: left;"> Survival/self-expression</td>
<td style="text-align: center;">0.265**</td>
<td style="text-align: center;">0.188**</td>
<td style="text-align: center;">0.188**</td>
</tr>
<tr>
<td style="text-align: left;"> Age</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">−0.013**</td>
<td style="text-align: center;">0.013**</td>
</tr>
<tr>
<td style="text-align: left;"> Education</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.020**</td>
<td style="text-align: center;">0.018**</td>
</tr>
<tr>
<td style="text-align: left;"> Social class (subjective)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.054**</td>
<td style="text-align: center;">0.052**</td>
</tr>
<tr>
<td style="text-align: left;"> Income scale (subjective)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.027**</td>
<td style="text-align: center;">0.027**</td>
</tr>
<tr>
<td style="text-align: left;"> Gender</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">−0.091**</td>
<td style="text-align: center;">−0.080 **</td>
</tr>
<tr>
<td style="text-align: left;"> GDP per capita (in 1000$)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.00048**</td>
</tr>
<tr>
<td style="text-align: left;"> Health expenditure per capita (in 1000$)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.0046**</td>
</tr>
<tr>
<td style="text-align: left;"> Life expectancy</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.019 **</td>
</tr>
<tr>
<td style="text-align: left;"> Government health expenditure (% of GDP)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.084**</td>
</tr>
<tr>
<td style="text-align: left;"> Out of pocket health expenses</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0.006**</td>
</tr>
<tr>
<td style="text-align: left;"> Constant</td>
<td style="text-align: center;">3.844**</td>
<td style="text-align: center;">3.874**</td>
<td style="text-align: center;">3.856**</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">Random effects</td>
</tr>
<tr>
<td style="text-align: left;"> SD traditional/rational–secular</td>
<td style="text-align: center;">0.093**</td>
<td style="text-align: center;">0.074**</td>
<td style="text-align: center;">0.074**</td>
</tr>
<tr>
<td style="text-align: left;"> SD survival/self-expression</td>
<td style="text-align: center;">0.062**</td>
<td style="text-align: center;">0.049**</td>
<td style="text-align: center;">0.038**</td>
</tr>
<tr>
<td style="text-align: left;"> SD constant</td>
<td style="text-align: center;">0.215**</td>
<td style="text-align: center;">0.188**</td>
<td style="text-align: center;">0.266**</td>
</tr>
</tbody>
</table>

\*\*$`p < 0.01`$

</div>

The between country regression coefficients from model 6 are reported in Table <a href="#Tab2" data-ref-type="table">2</a>. Only significant variables are included. The coefficients of this model are similar to those of the mixed models and there is a negative association for the traditional/rational–secular dimension and a positive association for the survival/self-expression dimension. The $`R^{2}`$ is 34%. The effects of the cultural variables on SRH between countries can be sizable. Combining the range of cultural values from Fig. <a href="#Fig2" data-ref-type="fig">2</a> with the coefficients from Table <a href="#Tab2" data-ref-type="table">2</a>, the between country effect of cultural values on SRH corresponds with a change of about 0.75 on a 5 point scale, that is around 15%.

<div id="Tab2" class="table-wrap">

<div class="caption">

Model 6: between country regression with SRH as the dependent variable

</div>

|                              |            |
|------------------------------|------------|
| *N*                          | 51         |
| *R* <sup>2</sup>             | 0.3352     |
| Traditional/rational–secular | −0.143\*   |
| Survival/self-expression     | 0.239\*\*  |
| Age                          | −0.022\*\* |
| Income                       | 0.214\*\*  |
| Constant                     | 3.824\*\*  |

\*\**p* \< 0.01, \**p* \< 0.05

</div>

## Discussion

Our main finding is that the associations between the two cultural dimensions and SRH are similar both within and between countries. Within countries, there is a positive association between the survival/self-expression dimension and SRH and a negative association between the traditional/rational–secular variable and SRH. The amount of variance explained by cultural values varied between 4 and 17% for each country. Adding socio-demographic and macroeconomic variables left the association between the two cultural dimensions and SRH unchanged, while doubling the amount of variance explained. Between countries, similar associations were found as within countries. Cultural values can result in a 0.75 change on the 5 point SRH scale in the extreme case. The associations within and between countries were similar, although the slopes and average SRH differ between countries.

### Ecological fallacy

Our results show a similar association between cultural values and SRH within and between countries. This similarity is relevant, as within and between country associations are not necessarily the same. It is possible that individual associations do not hold on a country level or vice versa. Our results present evidence that these associations are similar, which allows us to extrapolate the association between cultural values and SRH from one level to the other. Thus we avoid the ecological fallacy of making inferences at the ecological level, while the association at the individual level is unknown. This is an important result of our research, as we can now justify claims about the association between countries by similar findings at the individual level.

### Associations between cultural values and SRH

From our Western European point of view, we hypothesized that both cultural dimensions would be positively associated with SRH. Western countries score relatively high on rational–secular and self-expression values and are usually considered to have sophisticated health care. In agreement with this, the survival/self-expression variable was positively associated with SRH, confirming a finding by Inglehart and Baker \[16\]. This is plausible, as self-expression values are related to tolerance for abortion and homosexuality, happiness and trust. A more trusting environment, as shown by Mansyur et al \[5\], and happiness \[37\] could lead people to report better health. Furthermore, Inglehart \[15\] argues that countries, scoring high on self-expression, shift away from an emphasis on economic growth and security towards an emphasis on quality of life \[28\]. As a consequence, this could lead these countries to implement policies to improve the quality of life of the population.

Contrary to our hypothesis, the traditional/rational–secular dimension was negatively associated to SRH. This implies that traditional values are related to higher SRH and rational–secular values to lower SRH. We can only provide ad hoc explanations for this relation. Traditional values are related to a high importance of authority, intolerance for abortion and homosexuality, religion and family ties, while rational–secular values imply the opposite. It is well known that family ties and social support play a role in the well-being of individuals, shown by high correlates of social functioning and mental and physical health in quality of life measures \[38\]. This suggests that strong family ties and higher levels of social support could lead to a higher SRH. Alternatively, religion may play a role in the relation between traditional values and SRH. Religious communities may provide social support, which could have an effect on SRH. Furthermore, religion reduces health-risk behavior such as substance abuse \[39, 40\] and could therefore potentially lead to higher SRH. Religious coping could also play a role \[41, 42\]. For instance, positive religious coping such as surrendering, putting your fate in God’s hands, is positively associated with mental health and quality of life. However, negative religious coping, believing that your illness is a punishment from God, is negatively associated with physical health \[41\]. Taken together, it is unclear how religious coping affects SRH. Summarizing, several explanations have been put forward, but no firm conclusions can be drawn. Future research is needed to interpret the relation between traditional values and SRH.

Between countries, differences in SRH, and also differences in the associations between cultural values and SRH have been found. These differences, shown by the significant random effect in slopes in the mixed models, will not be further explored. A purely methodological explanation could be, for example, measurement error. Another explanation might be that cultural concepts or health differ between countries. The significant random intercepts in the mixed models show that SRH differs between countries, confirming earlier findings. The variance in slopes and intercepts suggests that SRH is not only explained by cultural values, socio-demographic and macroeconomic variables, but also by other unaccounted differences between countries.

### Limitations and strengths

One of the limitations of this study is that the IVS and Worldbank databases contain many missing values. The original IVS database included some 500,000 respondents, while our final dataset contains only 157,583 respondents for the within country regressions and 100,590 respondents for the mixed models. This reduction is mainly caused by missing macroeconomic data and unasked survey questions in a substantial amount of the waves in the IVS. This accounts for around 230,000 missing values, while around 110,000 missing values arise for other reasons. Additional analyses revealed no substantial differences between the final dataset and the data that was excluded from analysis and the remaining dataset is still very large and contains more than 1000 respondents per wave for each country in most cases. Therefore, we assume that there is no systematic selection bias. Another limitation is that we make the assumption that the association between cultural values and SRH does not change over time. WVS data were collected in waves, but these waves were collapsed into a single wave because our focus is on differences between countries and not on temporal effects. Furthermore, another limitation of our study is that cultural subgroups within countries may have a different relation between cultural values and SRH than the relation at the aggregate group level (that is country level), for which we cannot control. Furthermore, other literature suggests that differences in response styles might cause differences in SRH between countries \[27\]. However, in the WVS, no information on response styles is available, which is a limitation. In addition, we acknowledge the limitation of using linear regression analysis for the within-country analyses. The SRH variable is a categorical variable, for which a conditional probit model would have been more appropriate. However, using regression models simplifies the interpretation of the within and between country models, which is why we chose linear regression models.

The main strength of this study is that we avoid the ecological fallacy. Another strength of this study is that it confirms the associations between SRH and socio-demographic and macroeconomic variables found in earlier studies \[5–9\]. Lastly, a major strength of this research is the large sample size from the WVS.

## Conclusion

SRH is widely used in academic research and population studies as a measure of health. Large cross-country studies such as the Survey of Health, Aging and Retirement in Europe (SHARE) \[1\], the OECD Survey of Adult Skills (PIAAC) \[2\] and the European Union Eurostat bureau include SRH in their surveys to support policy analyses. The aim of this paper was to assess the association between cultural values and SRH within countries and between countries. We found that associations between the WVS cultural dimensions and SRH within countries and between countries are similar and this can lead to a change of up to 0.75 on the 5 point SRH scale. Contrary to our expectations, the traditional/rational–secular dimension was negatively associated to self-reported health. As SRH is associated with cultural values between countries, cultural values could be considered when interpreting SRH between countries.

## Acknowledgements

This study was funded by the EuroQol Research Foundation (EQ Project 2015150). The authors kindly thank Eelke de Jong and two anonymous referees for reading and commenting on earlier versions of the manuscript.

## Compliance with ethical standards

### Conflict of interest

BR declares that he has no conflict of interest. RD declares that he has no conflict of interest. PS declares that he has no conflict of interest.

### Ethical approval

This article does not contain any studies with human participants or animals performed by any of the authors.

## References

## References

1. Börsch-Supan, A. (2015). Survey of Health, Ageing and Retirement in Europe (SHARE) Wave 5. Release version: 1.0.0. SHARE-ERIC. Data set. DOI:10.6103/SHARE.w5.100.

2. OECD. (2016). The Survey of Adult Skills (PIAAC): https://www.oecd.org/site/piaac/surveyofadultskills.htm. Retrieved 14-04-2016.

3. Idler, E. L., & Benyamini, Y. (1997). Self-rated health and mortality: a review of twenty-seven community studies. Journal of Health and Social Behavior, 21–37.

4. Vuorisalmi M, Lintonen T, Jylhä M. Global self-rated health data from a longitudinal study predicted mortality better than comparative self-rated health in old age. Journal of Clinical Epidemiology. 2005;58(7):680–687. doi: 10.1016/j.jclinepi.2004.11.025.

5. Mansyur C, Amick BC, Harrist RB, Franzini L. Social capital, income inequality, and self-rated health in 45 countries. Social Science & Medicine. 2008;66(1):43–56. doi: 10.1016/j.socscimed.2007.08.015.

6. Borrell C, Muntaner C, Benach J, Artazcoz La. Social class and self-reported health status among men and women: what is the role of work organisation, household material standards and household labour? Social Science & Medicine. 2004;58(10):1869–1887. doi: 10.1016/S0277-9536(03)00408-8.

7. Cott CA, Gignac M, Badley EM. Determinants of self rated health for Canadians with chronic disease and disability. Journal of Epidemiology and Community Health. 1999;53(11):731–736. doi: 10.1136/jech.53.11.731.

8. Subramanian SV, Huijts T, Avendano M. Self-reported health assessments in the 2002 World Health Survey: how do they correlate with education? Bulletin of the World Health Organization. 2010;88(2):131–138. doi: 10.2471/BLT.09.067058.

9. Shibuya K, Hashimoto H, Yano E. Individual income, income distribution, and self rated health in Japan: cross sectional analysis of nationally representative sample. Bmj. 2002;324(7328):16. doi: 10.1136/bmj.324.7328.16.

10. Kondo N, Sembajwe G, Kawachi I, van Dam RM, Subramanian S, Yamagata Z. Income inequality, mortality, and self rated health: meta-analysis of multilevel studies. Bmj. 2009;339:b4471. doi: 10.1136/bmj.b4471.

11. Schwartz SH. A theory of cultural value orientations: Explication and applications. Comparative Sociology. 2006;5(2):137–182. doi: 10.1163/156913306778667357.

12. Hofstede G, Hofstede GJ, Minkov M. Cultures and organizations: Software of the mind. Maidenhead: McGraw-Hill; 1991.

13. Rokeach M. The nature of human values. New York: Free press; 1973.

14. Eccles JS, Wigfield A. Motivational beliefs, values, and goals. Annual Review of Psychology. 2002;53(1):109–132. doi: 10.1146/annurev.psych.53.100901.135153.

15. Inglehart R. Modernization and postmodernization: Cultural, economic, and political change in 43 societies. Princeton: Princeton University Press; 1997.

16. Inglehart R, Baker WE. Modernization, cultural change, and the persistence of traditional values. American Sociological Review. 2000;65(1):19–51. doi: 10.2307/2657288.

17. Welzel C, Inglehart R. Agency, values, and well-being: A human development model. Social Indicators Research. 2010;97(1):43–63. doi: 10.1007/s11205-009-9557-z.

18. Inglehart, R., & Welzel, C. (2005). Modernization, cultural change, and democracy: The human development sequence. Cambridge: Cambridge University Press.

19. Inglehart, R., & Welzel, C. (2015). Retrieved 14-03-2016, from http://www.worldvaluessurvey.org/images/Cultural_map_WVS6_2015.jpg.

20. Zola, I. K. (1966). Culture and symptoms–an analysis of patient’s presenting complaints. American Sociological Review, 615–630.

21. Zola IK. Pathways to the doctor—from person to patient. Social Science & Medicine (1967) 1973;7(9):677–689. doi: 10.1016/0037-7856(73)90002-4.

22. Diener E. New findings and future directions for subjective well-being research. American Psychologist. 2012;67(8):590. doi: 10.1037/a0029541.

23. Palmore, E., & Luikart, C. (1972). Health and social factors related to life satisfaction. Journal of Health and Social Behavior, 68–80.

24. Okun MA, Stock WA, Haring MJ, Witter RA. Health and subjective well-being: a meta-analysis. International Journal of Aging & Human Development. 1983;19(2):111–132. doi: 10.2190/QGJN-0N81-5957-HAQD.

25. Røysamb E, Tambs K, Reichborn-Kjennerud T, Neale MC, Harris JR. Happiness and health: environmental and genetic contributions to the relationship between subjective well-being, perceived health, and somatic illness. Journal of Personality and Social Psychology. 2003;85(6):1136. doi: 10.1037/0022-3514.85.6.1136.

26. Diener E, Diener M. Cross-cultural correlates of life satisfaction and self-esteem. Journal of Personality and Social Psychology. 1995;68(4):653–663. doi: 10.1037/0022-3514.68.4.653.

27. Jürges H. True health vs response styles: exploring cross-country differences in self-reported health. Health Economics. 2007;16(2):163–178. doi: 10.1002/hec.1134.

28. Mackenbach JP. Cultural values and population health: a quantitative analysis of variations in cultural values, health behaviours and health outcomes among 42 European countries. Health & Place. 2014;28:116–132. doi: 10.1016/j.healthplace.2014.04.004.

29. Diener E, Oishi S, Lucas RE. Personality, culture, and subjective well-being: Emotional and cognitive evaluations of life. Annual Review of Psychology. 2003;54(1):403–425. doi: 10.1146/annurev.psych.54.101601.145056.

30. Eid M, Diener E. Norms for experiencing emotions in different cultures: inter-and intranational differences. Journal of Personality and Social Psychology. 2001;81(5):869. doi: 10.1037/0022-3514.81.5.869.

31. Di Tella R, MacCulloch RJ, Oswald AJ. The macroeconomics of happiness. Review of Economics and Statistics. 2003;85(4):809–827. doi: 10.1162/003465303772815745.

32. v.20150418, W. V. S. A. WORLD VALUES SURVEY 1981 -2014 LONGITUDINAL AGGREGATE v.20150418. Madrid SPAIN: Aggregate File Producer: JDSystems.

33. Study EV. EVS (2015): European Values Study Longitudinal Data File 1981–2008 ZA4804 Data file Version 3.0.0. Cologne. Germany: GESIS Data Archive; 2015.

34. Association, W. V. S. (2016). FAQ. Retrieved 10-03-2016, from http://www.worldvaluessurvey.org/WVSContents.jsp.

35. Association, W. V. S. Fieldwork and Sampling. Retrieved 07-04-2016, from http://www.worldvaluessurvey.org/WVSContents.jsp.

36. World Bank (2016). Economy & growth and health indicators. data.worldbank.org/indicators. Accessed 2 Feb 2016.

37. Easterlin RA. Explaining happiness. Proceedings of the National Academy of Sciences. 2003;100(19):11176–11183. doi: 10.1073/pnas.1633144100.

38. Ware Jr, J. E., Kosinski, M., Bayliss, M. S., McHorney, C. A., Rogers, W. H., & Raczek, A. (1995). Comparison of methods for the scoring and statistical analysis of SF-36 health profile and summary measures: Summary of results from the Medical Outcomes Study. Medical Care, AS264–AS279.

39. Cochran JK, Akers RL. Beyond hellfire: An exploration of the variable effects of religiosity on adolescent marijuana and alcohol use. Journal of Research in Crime and Delinquency. 1989;26(3):198–225. doi: 10.1177/0022427889026003002.

40. Nonnemaker JM, McNeely CA, Blum RW. Public and private domains of religiosity and adolescent health risk behaviors: Evidence from the National Longitudinal Study of Adolescent Health. Social Science & Medicine. 2003;57(11):2049–2054. doi: 10.1016/S0277-9536(03)00096-0.

41. Koenig HG, Pargament KI, Nielsen J. Religious coping and health status in medically ill hospitalized older adults. The Journal of Nervous and Mental Disease. 1998;186(9):513–521. doi: 10.1097/00005053-199809000-00001.

42. Pargament KI, Koenig HG, Tarakeshwar N, Hahn J. Religious coping methods as predictors of psychological, physical and spiritual outcomes among medically ill elderly patients: A two-year longitudinal study. Journal of Health Psychology. 2004;9(6):713–730. doi: 10.1177/1359105304045366.

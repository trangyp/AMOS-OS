---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1104.3009v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1104.3009v2_Ratings_and_rankings__Voodoo_or_Science_

> Source: 1104.3009v2_Ratings_and_rankings__Voodoo_or_Science_.pdf

> Pages: 28

---


## Page 1


arXiv:1104.3009v2  [stat.AP]  20 Jul 2012
Ratings and rankings: Voodoo or Science?
Paolo Paruolo1
Department of Economics, University of Insubria, Varese, Italy.
Michaela Saisana
European Commission, Joint Research Centre, Ispra (VA), Italy.
Andrea Saltelli
European Commission, Joint Research Centre, Ispra (VA), Italy.
Summary. Composite indicators aggregate a set of variables using weights which are
understood to reﬂect the variables’ importance in the index. In this paper we propose
to measure the importance of a given variable within existing composite indicators via
Karl Pearson’s ‘correlation ratio’; we call this measure ‘main effect’. Because socio-
economic variables are heteroskedastic and correlated, relative nominal weights are
hardly ever found to match relative main effects; we propose to summarize their dis-
crepancy with a divergence measure. We discuss to what extent the mapping from
nominal weights to main effects can be inverted. This analysis is applied to six com-
posite indicators, including the Human Development Index and two popular league
tables of university performance. It is found that in many cases the declared impor-
tance of single indicators and their main effect are very different, and that the data
correlation structure often prevents developers from obtaining the stated importance,
even when modifying the nominal weights in the set of nonnegative numbers with unit
sum.
1.
Introduction
In social sciences, composite indicators aggregate individual variables with the
aim to capture relevant, possibly latent, dimensions of reality such as a coun-
try’s competitiveness (World Economic Forum (2010)), the quality of its gover-
nance (Agrast et al. (2010)), the freedom of its press (Reporters Sans Frontieres
(2011); Freedom House (2011)) or the eﬃciency of its universities or school system
(Leckie and Goldstein (2009)). These measures have been termed ‘pragmatic’ (see
Hand (2009), pp.
12-13), in that they answer a practical need to rate individ-
ual units (such as countries, universities, hospitals or teachers) for some assigned
purpose.
Composite indicators (which are also referred to here as indices) have been in-
creasingly adopted by many institutions, both for speciﬁc purposes (such as to
determine eligibility for borrowing from international loan programs) and for pro-
viding a measurement basis for shaping broad policy debates, in particular in the
public sector (Bird et al. (2005)). As a result, public interest in composite indicators
has enjoyed a ﬁvefold increase over the period 2005 −2010: a search of ‘composite
1Address for correspondence: Paolo Paruolo, Department of Economics, University of
Insubria, Via Monte Generoso 71, 21100 Varese, Italy.
E-mail: paolo.paruolo@uninsubria.it
Date: October 22, 2018


## Page 2


2
Paruolo, Saisana & Saltelli
indicators’ on Google Scholar gave 992 matches on October 2005 and 5, 340 at the
time of the ﬁrst version of this paper (December 2010).
Composite indicators are fraught with normative assumptions in variable selec-
tion and weighting. Here ‘normative’ is understood to be ‘related to and dependent
upon a system of norms and values’. For example, the proponents of the Human
Development Index (HDI) advocate replacing gross domestic product (GDP) per
capita as a measure of the progress of societies with a combination of (i) GDP
per capita (ii) education and (iii) life expectancy, see Ravallion (2010). Both the
selection of these three speciﬁc dimensions and the choice of building the index by
giving these dimensions equal importance are normative, see Stiglitz et al. (2009),
p. 65. Composite indicators are thus often the subject of controversy, see Saltelli
(2007), Hendrik et al. (2008).
The statistical analysis of composite indicators is essential to prevent media and
stakeholders taking them at face value (see the recommendations in Organisation for Economic Co-oper
(2008)), possibly leading to questionable policy choices. For example, a policy maker
might think of merging higher education institutions just because the most popu-
lar league table of universities puts a prize on larger universities, see Saisana et al.
(2011).
Most existing composite indicators are linear, i.e. weighted arithmetic averages
(Organisation for Economic Co-operation and Development, 2008). Linear aggre-
gation rules have been criticized because weaknesses in some dimensions are com-
pensated by strengths in other dimensions; this characteristic is called ‘compen-
satory’. Non-compensatory and non-linear aggregate ranking rules have been advo-
cated by the literature on multicriteria decision making, see for example Billaut et al.
(2010), Munda (2008), Munda and Nardo (2009), Balinski and Laraki (2010). In
this paper we concentrate on linear aggregation, because of its widespread use.
In this paper we address the issue of measuring variable importance in existing
composite indicators. As illustrated by a motivating example at the end of this sec-
tion, nominal weights are not a measure of variable importance, although weights
are assigned so as to reﬂect some stated target importance, and they are commu-
nicated as such. In linear aggregation, the ratio of two nominal weights gives the
rate of substitutability between the two individual variables, see (Boyssou et al.,
2006, Chapter 4), or Decancq and Lugo (2010), and hence can be used to reveal
the target relative importance of individual indicators. This target importance can
then be compared with ex-post measures of variables’ importance, such as the one
presented in this paper.
We propose to measure the importance of a given variable via Karl Pearson’s
‘correlation ratio’, which is widely applied in global sensitivity analysis as a ﬁrst-
order sensitivity measure; we call this measure ‘main eﬀect’. Main eﬀects represent
the expected relative variance reduction obtained in the output (the index) if a
given input variable could be ﬁxed (Saltelli and Tarantola (2002), see Section 3.1).
They are based on the statistical modelling of the relation between the variable and
the index.
This statistical modelling can be parametric or non-parametric; we compare a
linear and a non-parametric alternative based on local-linear kernel smoothing. We
apply the main eﬀects approach to six composite indicators, including the HDI and
two popular league tables of university performance. We ﬁnd that in some cases, a
linear model can give a reasonable estimate of the main eﬀects, but in other cases
the non-parametric ﬁt must be preferred. Further, we ﬁnd that nominal weights
hardly ever coincide with main eﬀects. We propose to summarize this deviation in


## Page 3


Ratings and rankings
3
a discrepancy statistic, which can be used by index developers and users alike to
gauge the gap between the eﬀective and the target importance of each variable.
We also pose the question of whether the target importance stated by the de-
velopers is actually attainable by appropriate choice of nominal weights; we call
this the ‘inverse problem’. We ﬁnd that in most instances the correlation structure
prevents developers from obtaining the stated importance by changing the nominal
weights within the set of nonnegative numbers with sum equal to 1. These ﬁndings
may oﬀer a useful insight to users and critics of an index, and a stimulus to its
developers to try alternative, possibly non-compensatory, aggregation strategies.
Our proposed measure of importance is also in line with current practice in Sen-
sitivity Analysis. Recently, some of the present authors proposed a global sensitivity
analysis approach to test the robustness of a composite indicator, see Saisana et al.
(2005, 2011); this approach performs an error propagation analysis of all sources
of uncertainty which can aﬀect the construction of a composite indicator.
This
analysis might be called ‘invasive’ in that it demands all sources of uncertainty to
be modeled explicitly, e.g. by assuming alternative methods to impute missing val-
ues, diﬀerent weights, diﬀerent aggregation strategies; the method may also test the
eﬀect of including or excluding individual variables from the index.
In contrast, the approach suggested in this paper is non-invasive, because it
does not require explicit modeling of uncertainties.
The proposed measure also
requires minimal assumptions, in the sense that it exists whenever second moments
exist. Moreover, it takes the data correlation structure into account. When this
analysis is performed by the developers themselves, it adds to the understanding
– and ultimately to the quality, of the index. When performed ex-post by a third
party on an already developed index, this procedure may reveal un-noticed features
of the composite indicator.
The paper is organized as follows: the rest of Section 1 reports a motivating ex-
ample and discusses related work. Section 2 describes linear composite indicators.
Section 3 deﬁnes the main eﬀects and discusses their estimation. It also deﬁnes
a discrepancy statistic between main eﬀects and nominal weights. Finally it dis-
cusses the inversion of the map from nominal weights to main eﬀects. Section 4
presents detailed results for six indices: the 2009 Human Development Index (2009
HDI), the Academic Ranking of World Universities by Shanghais Jiao Tong Univer-
sity (ARWU), the university ranking by the Times Higher Education Supplement
(THES), the 2010 Human Development Index (2010 HDI), the Index of African
Governance (IAG) and the Sustainable Society Index (SSI). Section 5 contains a
discussion and conclusions. A solution to the inverse problem is reported in the
Appendix.
1.1.
Motivating example
In weighted arithmetic averages, nominal weights are communicated by develop-
ers and perceived by users as a form of judgement of the relative importance of
the diﬀerent variables, including the case of equal weights where all variables are
assumed to be equally important. When using ‘budget allocation’, a strategy to
assign weights, experts are given a number of tokens, say 100, and asked to ap-
portion them to the variables composing the index, assigning more tokens to more
important variables. This is a vivid example of how weights are perceived and used
as measures of importance. However, the relative importance of variables depends
on the characteristics of their distribution (after normalization) as well as their cor-


## Page 4


4
Paruolo, Saisana & Saltelli
relation structure, as we illustrate with the following example. This gives rise to
a paradox, of weights being perceived by users as reﬂecting the importance of a
variable, where this perception can be grossly oﬀthe mark.
Consider a University Dean who is asked to evaluate the performance of faculty
members, giving equal importance to indicators of publications x1, of teaching x2
and of oﬃce hours and administrative work x3. Hence she considers an equally-
weighted index, y = 1
3(x1 + x2 + x3), and she employs R2
i := corr2(y, xi) in order to
measure the association between the index y and each of the x variables ex post.
We consider two diﬀerent situations, which illustrate the inﬂuence of variances
and of correlations of the x variables on the performance of faculty members. In
both situations, we let the variables x1, x2, x3 be jointly normally distributed with
mean zero. First assume that the variance of x1 is equal to 7 while x2 and x3 have
unit variances, and that the xj variables are uncorrelated; the value 7 is chosen here
in order to make the variance of y equal to 1. We then ﬁnd
R2
1 = 7
9 ≈0.778,
R2
2 = R2
3 = 1
63 ≈0.016,
which implies that the importance (as measured by R2
i ) of the variables x2 and x3
relative to x1 is equal to 1/49 ≈0.020. This shows how variances can greatly aﬀect
this measure of importance. We conclude that the Dean needs to do something
about the indicators’ variances before computing the index.
Changing the weights from 1/3 to 1/(c√σii), where c := P3
i=1 1/√σii and σii
is the variance of xi would compensate for unequal variances; this corresponds to
standardizing indicators before aggregation. In current practice, composite indica-
tors builders prefer to normalise indicators before aggregation, for instance dividing
by the highest score. Going back to the Dean’s example, the yearly number of
administration hours can be divided by the total number of hours within a year,
delivering x3 as the fraction of administration hours. We remark that, in general,
normalised scores present diﬀerent variances.
Consider next the situation where x1, x2, x3 are standardized, i.e. have all unit
variances. Assume also that the correlations ρij := corr(xi, xj) are all equal to zero,
except ρ23 = ρ32 > 0. Simple algebra shows that
R2
1 =
1
3 + 2ρ23
,
R2
2 = R2
3 = (1 + ρ23)2
3 + 2ρ23
,
R2
1
R2
2
=
1
(1 + ρ23)2 ,
i.e.
that the importance of indicators x2 and x3 is the same; this is a general
property of standardized indicators. Note that the importance of indicators x2 and
x3 is greater that the one of x1, because ρ23 > 0. Taking for instance ρ23 = 0.7,
one ﬁnds
R2
1 = 5
22 ≈0.227,
R2
2 = R2
3 = 289
440 ≈0.657,
R2
1
R2
2
= 100
289 ≈0.346.
One may well imagine a faculty member looking at the relative importance of x1
with respect to x2, complaining that research has become dispensable, because – al-
though the index’s formula seems to suggest that all variables are equally important
– in fact teaching is valued more than publications by a factor of 3. In this second
situation, even if the Dean has standardized the variables measuring publications
x1, teaching x2 and administration x3, the last two have a higher inﬂuence on the
faculty performance indicator y due to their correlation.


## Page 5


Ratings and rankings
5
This example describes diﬀerent situations which generate the paradox. The
occurrence of diﬀerent variances is one such situation; this is a problem also in
practice, because usually individual indicators are normalized to be between 0 and
1 or 0 and 100, and hence they have diﬀerent variances in general.
Also when
correcting for diﬀerent variances using standardized indicators, however, the para-
dox can be generated by correlations. This is of practical concern as well, because
diﬀerent individual indicators are usually correlated.
The paradox illustrated by the preceding example equally applies when the
index’s architecture is made of pillars, each pillar aggregating a subset of variables.
An hypothetical sustainability index could have environmental, economic, social
and institutional pillars, and equal weights for these four pillars would ﬂag the
developers’ belief that these dimensions share the same importance. Still one of the
four pillars with a weighting in principle of 25% could contribute little or nothing
to the index, e.g. because the variance of the pillar is comparatively small and/or
the pillar is not correlated to the remaining three. A case study of this nature is
discussed later in the present work.
1.2.
Related work
The connection of the present paper with global sensitivity analysis has been dis-
cussed above. A related approach to measure variable importance in linear aggre-
gations is the one of ‘eﬀective weights’, introduced in the psychometric literature
by Stanley and Wang (1968), Wang and Stanley (1970). The eﬀective weight of a
variable xi is deﬁned as the covariance between wixi and the composite indicator
y = Pk
i=1 wixi divided by its variance, i.e. ǫi := cov(y, wixi)/V(y). The same
approach has been employed in recent literature in global sensitivity analysis, see
e.g. Li et al. (2010).
Eﬀective weights ǫi are, however, not necessarily positive, and hence they make
an improper apportioning of the variance V (y): ǫi cannot be interpreted as a ‘bit’
of variance. On the contrary, the measure of importance Si proposed in this paper
(i.e. Pearson’s correlation ratio) is always positive and can be interpreted as the
fractional reduction in the variance of the index that could be achieved (on average)
if variable xi could be ﬁxed. Si also ﬁts into an ANOVA variance decomposition
framework, see Saltelli (2002) for a discussion.
Moreover, eﬀective weights assume that the dependence structure of the vari-
ables xi is fully captured by their covariance structure, as in linear regression. As
we show in the following, the relation between the index and its components may
well be nonlinear, and the measure of importance proposed in this paper extends to
this case as well. The case-studies reported in Section 4 show that nonlinearity is
often the rule rather than the exception. In the case of a linear relation between y
and xi, our measure Si reduces to R2
i , the square of corr(y, xi), used in the example
above; hence in this case, the present approach leads to a simple transformation of
the eﬀective weights.
For some indices, such as the Product Market Regulation Index (see Nicoletti et al.
(2000)), Principal Component Analysis (PCA) has been used to select aggregation
weights. PCA chooses weights that maximize (minimize) the variance of the index,
and hence weights do not reﬂect the normative aspects of the deﬁnition of the in-
dex. Consequently, weights are diﬃcult to interpret and to communicate, and as a
result the use of PCA in this context is not widespread. The same Product Market
Regulation Index moved from the use of PCA to a simpler and more transparent


## Page 6


6
Paruolo, Saisana & Saltelli
technique for linear aggregation after a statistical analysis of the implications of
such a change (Nardo, 2009).
2.
Weights and importance
Consider the case of a composite indicator y calculated as a weighted arithmetic
average of k variables xi
yj =
k
X
i=1
wixji,
j = 1, 2, · · ·, n
(1)
where xji is the normalized score of individual j (e.g., country) based on the value
Xji of variable X·i, i = 1, . . . , k and wi is the nominal weight assigned to variable
X·i. The most common approach is to normalize original variables, see Bandura
(2008), by the min-max normalisation method
xji =
Xji −Xmin,i
Xmax,i −Xmin,i
,
(2)
where Xmax,i and Xmin,i are the upper and lower values respectively for the variable
X·i; in this case all scores xji vary in [0, 1]. Here we indicate the transformation
(2) as ‘normalisation’; the normalised variables in (2) are denoted as x·i. We let
µi := E(xji) and σii = V(xji) indicate their expectation and variance respectively.
In the following, we replace X·i and x·i by Xi and xi respectively, unless needed for
clarity.
Observe that the normalisation (2) implies a ﬁxed scale of the individual indi-
cators; this is useful for instance for comparability in repeated waves of the same
index. However, normalisation does not imply any standardization of diﬀerent x·i
variables, which hence have diﬀerent means µi and variances σii in general.
A popular alternative to the min-max normalization in (2) is given by standard-
ization
xji = Xji −E (Xji)
p
V (Xji)
,
(3)
where E (Xji) and V (Xji) are the mean and variances of the original variables X·i.
When standardized, all xi have the same mean and variance, µi = 0, σii = 1 for all
i, removing one source of heterogeneity among variables. However, standardization
does not aﬀect the correlation structure of the variables Xi (or xi). Both transfor-
mations (2) and (3) are invariant to the choice of unit of measurement of Xi, see
(Hand, 2009, Chapter 1).
While standardization may appear a better approach than normalization, sta-
tistically, there are advantages and disadvantages of both. For example standard-
ization may be expected not to work so well when the distribution is very skewed
or long tailed. Moreover it does not enhance comparison across diﬀerent waves of
the same aggregate indicator over the years, if the mean and variances used in (3)
change over time. Also one cannot achieve both standardization and normalization
at the same time through a linear transformation of Xi. This implies that index
developers suﬀer the unwanted disadvantages of the chosen transformation.
Whatever the transformation, in the following we denote the column vector of
scores of unit j as xj := (xj1, . . . , xjk)′ and indicate by µ := (µ1, . . . , µk)′ and Σ :=
(σit)k
i,t=1 the corresponding vector of means and the implied variance-covariance


## Page 7


Ratings and rankings
7
matrix. The weight, wi, attached to each variable, xi, in the aggregate is meant
to appreciate the importance of that variable with respect to the concept being
measured. The vector of weights w := (w1, . . . , wk)′ is selected by developers on
the basis of diﬀerent strategies, be those statistical, such as PCA, or based on expert
evaluation, such as analytic hierarchy process, see Saaty (1980, 1987).
In what follows we indicate by ζ2
iℓthe target relative importance of indicators i
and ℓ. When this is not explicitly stated, the ratios wi/wℓcan be taken to be the
‘revealed target relative importance’. In fact wi/wℓis a measure of the substitution
eﬀect between xi and xℓ, i.e. how much xℓmust be increased to oﬀset or balance
a unit decrease in xi, see Decancq and Lugo (2010).
For simplicity of notation
and without loss of generality, we assume that the maximal weight is assigned to
indicator 1, i.e. that w1 ≥wi for i = 2, . . . , k, and we consider ζ2
i := ζ2
i1.
Note that the previous discussion applies to pillars as well as to individual vari-
ables, where a pillar is deﬁned as an aggregated subset of variables, identiﬁed by
the developers as representing a salient – possibly latent, or normative – dimension
of the composite indicator.
3.
Measuring importance
3.1.
Measures of importance
In this paper we propose a variance-based measure of importance. We note that
E (y) = w′µ,
V (y) = w′Σw,
(4)
where, if (3) is used, E (y) = 0 and the diagonal elements of Σ are equal to 1; here
we have dropped the subscript j in yj for conciseness. In the following, we focus
attention on the variance term.
Following Pearson (1905), we consider the question ‘what would be the average
variance of y, if variable xi were held ﬁxed?’ This question leads to consider
Exi (Vx∼i (y | xi)) ,
where x∼i is deﬁned as the vector containing all the variables in x except variable
xi. Owing to the well known identity
Vxi (Ex∼i (y | xi)) + Exi (Vx∼i (y | xi)) = V (y)
we can deﬁne the ratio of Vxi (Ex∼i (y | xi)) to V (y) as a measure of the relative
reduction in variance of the composite indicator to be expected by ﬁxing a variable,
i.e.
Si ≡η2
i := Vxi (Ex∼i (y | xi))
V (y)
.
(5)
The notation Si reﬂects the use of this measure as a ﬁrst order sensitivity measure
(also termed ‘main eﬀect’) in sensitivity analysis, see Saltelli and Tarantola (2002).
The notation η2
i reﬂects the original notation used in Pearson (1905); he called it
‘correlation ratio η2’.
The conditional expectation Ex∼i (y | xi) in the numerator of (5) can be any non-
linear function of xi; in fact fi (xi) := Ex∼i (y | xi) = wixi+Pk
ℓ=1,ℓ̸=i wℓEx∼i (xℓ| xi),
where the latter conditional expectations may be linear or nonlinear in xi. For the
connection of fi (xi) to global sensitivity analysis see Saltelli et al. (2008).


## Page 8


8
Paruolo, Saisana & Saltelli
In the special case of fi (xi) linear in xi, we ﬁnd that Si reduces to R2
i , where
Ri is the product-moment correlation coeﬃcient of the regression of y on xi. In
fact, it is well known that when fi is linear, i.e. fi (xi) = αi + βixi, it coincides
with the L2 projection of y on xi, which implies that βi = cov(y, xi)/σii, see e.g.
Wooldridge (2010). Hence Si has the form Si = Vxi (βixi + αi) /V(y) and one ﬁnds
Si = β2
i σii/V(y) = cov2(y, xi)/(σiiV(y)) = R2
i .
A further special case corresponds to fi linear and x made of uncorrelated
components. We ﬁnd cov(y, xi) = Pk
t=1 wtσti and V(y) = Pk
t=1 w2
t σtt so Si =
w2
i σii/ Pk
t=1 w2
t σtt. The main diﬀerence between the uncorrelated and the corre-
lated case is that in the former Pk
i=1 Si = 1 because Si = w2
i σii/ Pk
h=1 w2
hσhh,
while for the latter Pk
i=1 Si might well exceed one, see e.g. Saltelli and Tarantola
(2002). We note that in general Si can still be high also when R2
i is low, e.g. in
case of a non-monotonic U-shaped relationship for fi(xi). Hence in general fi(xi)
needs to be estimated in a nonparametric way, see Section 3.2.
As these special cases illustrate, Si is quadratic measure in terms of the weights
wj for linear aggregation schemes (1); this follows from its deﬁnition as a variance-
based measure. The main eﬀect Si is an appealing measure of importance of a
variable (be it indicator or pillar) for several reasons:
• it oﬀers a precise deﬁnition of importance of a variable, that is ‘the expected
fractional reduction in variance of the composite indicator that would be ob-
tained if that variable could be ﬁxed’;
• it can be applied when relationships between the index and its components
are linear or nonlinear.
Such nonlinearity may be the eﬀect of nonlinear
aggregation (e.g. Condorcet-like, see Munda (2008)) and/or of nonlinear re-
lationships among the single variables. It can be used regardless of the degree
of correlation between variables. Unlike the Pearson or Spearman correlation
coeﬃcients, it is not constrained by assumptions of linearity or monotonicity;
• it is not invasive, that is no changes are made to the composite indicator or to
the correlation structure of the indicators, unlike e.g. the error propagation
analysis presented in Saisana et al. (2005). While the error propagation can
be considered as a stress test of the index, the present approach is a test of
its internal coherence.
3.2.
Estimating main effects
In this subsection we consider estimating the main eﬀects and focus on the 2009
HDI to illustrate our approach. In Section 4 we describe the six case-studies of our
approach in detail.
In sensitivity analysis, the estimation of Si is an active research ﬁeld. Si can be
estimated from design points: Sobol’ (1993); Saltelli (2002); Saltelli et al. (2010);
Fourier analysis: Tarantola et al. (2006); Plischke (2010); Xu and Gertner (2011),
or others. Many nonparametric estimators can be used to estimate fi(xi), such as
State Dependent Regression: Ratto et al. (2007); Ratto and Pagano (2010).
In the present work we employ a nonparametric, local-linear, kernel regression to
estimate m(·) := fi(·), and then use it in (5) to estimate Si, replacing the variances
in the numerator and denominator with the corresponding sample variances, i.e.
using Pn
j=1(mj −¯m)2/ Pn
j=1(yj −¯y)2, where ¯y := n−1 Pn
j=1 yj, ¯m := n−1 Pn
j=1 mj,
mj := ˆm(xji) and ˆm(·) is the estimate of m(·) := fi(·).


## Page 9


Ratings and rankings
9
0.2
0.4
0.6
0.8
1
5.1
5.2
5.3
5.4
x 10
−3
Cross validation
h
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
linearity test p−value
h
0.2
0.4
0.6
0.8
1
0.79
0.8
0.81
0.82
0.83
0.84
0.85
Si
h
0.2
0.4
0.6
0.8
1
0.2
0.4
0.6
0.8
1
hDPI= 0.0841, hCV=0.0884
x1
Fig. 1. 2009 HDI (y), Life expectancy (x1). Upper left: Cross validation criterion as a function
of the smoothing parameter h; upper right: linearity test p-value as a function of h; lower
left: main effects Si as a function of h; lower right: cross plot of y versus x1 with linear ﬁt
and local linear ﬁts for hDP I (direct plug-in, dotted line) and hCV (cross validation, dashed
line). The values of hDP I and hCV are plotted as vertical lines in the ﬁrst 3 panels (dotted
lines and dashed lines respectively).


## Page 10


10
Paruolo, Saisana & Saltelli
Local linear kernel estimators achieve automatic boundary corrections and en-
joy some typical optimal properties, that are superior to Nadaraya-Watson kernel
estimators, see Ruppert and Wand (1994) and reference therein. As a result, local
linear kernel smoother are often considered the standard nonparametric regression
method, see e.g. Bowman and Azzalini (1997).
The local linear nonparametric kernel regression is indexed by a bandwidth
parameter h, which is usually held constant across the range of value for xi. For
large h, the local linear nonparametric kernel regression converges to the linear
least squares ﬁt. This allows us to interpret 1/h as the deviation from linearity; it
suggests that we investigate the sensitivity of the estimation of Si to variation in
the bandwidth parameter h. In order to make this dependence explicit we write
Si(h) to indicate the value of Si obtained by a local-linear kernel regression with
bandwidth parameter h. In the application we use a Gaussian kernel.
The choice of the smoothing parameter h can be based either on cross-validation
(CV) principles (see Bowman and Azzalini (1997)) or on plug-in choices for the
smoothing parameter, such as the ones proposed in Ruppert et al. (1995).
We
describe these approaches in turn, starting with cross validation. Let ˆm(x) indicate
the local linear nonparametric kernel estimate for fi(x) at xi = x based on all n
observations, and let ˆm−j(x) be the same applied to all data points except for the
one with index j; then the least-squares Cross Validation criterion for variable xi is
deﬁned as
CV (h) = 1
n
n
X
j=1
(yj −ˆm−j(xji))2
The optimal value for the CV criterion is given by the bandwidth hCV corre-
sponding to the minimum of CV (h). In practice, a grid H of possible values for h
is considered, and the minimum of the function CV (h) is found numerically. In the
application we chose the grid of h values as follows: we deﬁned a regular grid of 50
values for u :=
√
h in the range from 0.1 to 5. The values for h were then obtained
as h = a + u2/b, for index-speciﬁc constants a and b; the resulting set of values in
this grid is denoted H in what follows.
The default values for indices with range from 0 to 10 or 100 were a = 0.05,
b = 1, so that .06 < h ≤25.05; for indices with range from 0 to 1, (namely 2009
and 2010 HDI ), we chose a = 0.01, b = 25, so that .01 < h ≤1.01. In some cases
CV(h) attains its minimum at the right end of the grid H; This happened both for
ARWU{1, 2, 3} and THES{4, 6}, see Table 1, as well as for IAG{2, 5} and SSI{2},
see Table 3, where the digits in braces refer to the subscript i of the xi variables.
In these cases, in practice, a linear regression ﬁt would not be worse than the ﬁt of
the local linear kernel estimator, according to the CV criterion.
In the implementation of the CV criterion, when a local linear kernel regres-
sion implied a row of the smoothing matrix with numerical ‘divisions by zero’, we
replaced it with a local mean (Nadaraya-Watson) estimator. When also the latter
would imply numerical divisions by zero, we replaced the row of the smoothing
matrix with a sample leave-one-out mean.
An alternative choice of bandwidth is given by plug-in-rules. One popular choice
is given by the ‘direct plug-in’ selector hDP I introduced by Ruppert et al. (1995),
which minimizes the Asymptotic Mean Integrated Squared Error for the local linear
Gaussian kernel smoother, on the basis of the following preliminary estimators. Let
θrs := E(m(s)m(r)), where m(r)(x) is the r-th derivative of m(x). The range of
xi is partitioned into N blocks and a quartic is ﬁtted on each block. Using this


## Page 11


Ratings and rankings
11
0.2
0.4
0.6
0.8
1
5.8
6
6.2
6.4
x 10
−3
Cross validation
h
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
linearity test p−value
h
0.2
0.4
0.6
0.8
1
0.76
0.78
0.8
0.82
Si
h
0.2
0.4
0.6
0.8
1
0.2
0.4
0.6
0.8
1
hDPI= 0.0666, hCV=0.05
x2
Fig. 2. 2009 HDI (y), Adult literacy (x2). See caption of Fig 1.
estimation, an estimate for θ24 is found, along with an estimator for the error
variance σ2 := E(yj −m(xji))2. These estimates are then used to obtain a plug-
in bandwidth g, which is used in a local cubic ﬁt to estimate θ22 and to obtain
a diﬀerent plug-in bandwidth λ.
The λ bandwidth is then used in a ﬁnal local
linear kernel smoother to estimate σ2, which is fed into the ﬁnal formula for hDP I,
along with the previous estimate of θ22. The choice of N, the number of blocks,
is obtained minimizing Mallow’s Cp criterion over the set {1, 2, . . ., Nmax}, where
Nmax = max{min(⌊n/20⌋, N ∗), 1}.
In the application we chose N ∗= 5 as suggested by Ruppert et al. (1995); in
case of numerical instabilities, we decreased N ∗to 4. Moreover we performed an
α-trimming in the estimation of θ24 and θ22 with α = 0.05. Because the choice of
bandwidth can be aﬀected by values at the end of the x-range, we only considered
pairs of observations for which x > 0 in the choice of bandwidth, both for the CV
criterion and the DPI criterion.
The resulting choice of bandwidth hDP I was sometimes very close to hCV , as
in the case for the 2009 HDI, which is depicted in Fig. 1-4, where each ﬁgure refers
to one of the four xi indicators used in the construction of the 2009 HDI. Fig. 1
refers to the x1 indicator (life expectancy), and contains four panels, which report
– counterclockwise from upper-right – the p-value of the linearity test introduced
below, the cross validation criterion CV , the S1 measure and the regression cross
plot. The ﬁrst 3 graphs show functions of the bandwidth parameter h, while the
ﬁnal one has the values of x1 on the horizonal axis. Fig. 2-4 have the same format,
and refer to indicators x2, x3 and x4.
Tables 1 and 3 report the selected values of hCV and hDP I for the 2009 HDI
and for the other 5 indices, described in detail in Section 4. It can be seen that the


## Page 12


12
Paruolo, Saisana & Saltelli
0.2
0.4
0.6
0.8
1
5.2
5.4
5.6
5.8
6
6.2
x 10
−3
Cross validation
h
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
linearity test p−value
h
0.2
0.4
0.6
0.8
1
0.74
0.76
0.78
0.8
0.82
0.84
0.86
Si
h
0.2
0.4
0.6
0.8
1
0.2
0.4
0.6
0.8
1
hDPI= 0.0631, hCV=0.0424
x3
Fig. 3. 2009 HDI(y), Enrolment in education (x3). See caption of Fig 1.
values of hCV sometimes diﬀered from hDP I by several orders of magnitude.
As in many other contexts, in the estimation of main eﬀects Si the linear case
is a relevant reference model, and one would like to address inference on Si and
on the possible linearity of fi(xi) jointly. To this end we implemented the test for
linearity proposed in Bowman and Azzalini (1997, Chapter 5). The ﬁt of the linear
kernel smoother can be represented as ˆy = Sy, where the matrix S depends on
all values xji, j = 1, . . . , n. A test of linearity can be based on the F statistic,
F := (RSS0 −RSS1)/RSS1, that compares the residual sum of squares under the
linearity assumption RSS0 with the one corresponding to the local linear kernel
smoother RSS1. Letting Fobs indicate the value of the statistic, the p-value of the
test is computed as the probability that z′Cz > 0 where z is a vector of independent
standard Gaussian random variables and C := M(I −(1 + Fobs)A)M with A =
(I −S)′(I −S), M = I −X(X′X)−1X′ and X equal to the linear regression design
matrix, with ﬁrst column equal to the constant vector and the second column equal
to the values of xji, j = 1, . . . , n.
Bowman and Azzalini (1997) suggest approximating the quantiles of the quadratic
form with the distribution of aχ2
b + c, where a, b and c are obtained by matching
moments of the quadratic form and the aχ2
b + c distribution; here χ2
b represents a
χ2 distribution with b degrees of freedom. We implemented this approximation; the
upper right panels in Fig. 1-4 report the resulting p-values of the test as a function of
h for the 2009 HDI. It can be seen for some xi variable the test rejects the linearity
hypothesis for all values of h in the grid H, and for some other pairs the test rejects
only for a subset of H. In a few other pairs, the test never rejects for all h ∈H.
Results for the linearity test are reported in Tables 1 and 3 for selected values of h,
both the 2009 HDI and for 5 other indices, described in detail in Section 4.


## Page 13


Ratings and rankings
13
0.2
0.4
0.6
0.8
1
3.8
4
4.2
4.4
x 10
−3
Cross validation
h
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
linearity test p−value
h
0.2
0.4
0.6
0.8
1
0.84
0.85
0.86
0.87
0.88
Si
h
0
0.2
0.4
0.6
0.8
1
0.2
0.4
0.6
0.8
1
hDPI= 0.0771, hCV=0.0884
x4
Fig. 4. 2009 HDI (y), GDP per capita (x4). See caption of Fig 1.
To show sensitivity of the main eﬀects Si to the smoothing parameter h, we also
computed the Si(h) index as a function of h. We also recorded the min and max
values obtained for Si(h) varying h in H; we denote these values as Si,min, Si,max.
We report the plot of Si(h) as a function of h in the lower left panels of Fig. 1-4.
3.3.
Comparing weights and main effects
In this section we compare revealed or target relative importance measures ζ2
i with
the relative main eﬀects Si/S1. First notice that, in the independent case, Si =
w2
i σii/ Pk
h=1 w2
hσhh, so that Si/S1 = w2
i σii/w2
1σ11.
When the xi variables are
standardized, all σii = 1 and hence Si/S1 = w2
i /w2
1. The relative main eﬀects Si/S1
do not reduce to ζ2
i = wi/w1, except in the homoskedastic case (σii = σ11) when the
nominal weights are equal, (wi = w1), so that w2
i σii/w2
1σ11 = w2
i /w2
1 = 1 = wi/w1.
In the general case, Si depends on w and Σ in a more complicated way, and hence
there is no reason, a priori, to expect Si/S1 to coincide with ζ2
i .
One can compare how the eﬀective relative importance Si/S1 deviates from
the (revealed) target relative importance ζ2
i ; to this end we deﬁne the maximal
discrepancy statistic dm as
dm =
max
i∈{2,...,k}
ζ2
i −Si
S1
,
(6)
In the case of revealed target relative importance, recall that w1 is assumed to
be the highest nominal weight wmax. In the case when more than one variable has
maximum weight equal to wmax, we selected as reference variable the one with max-
imum value for Sℓ(hℓ,DP I) with ℓ∈{1, . . . , k}, i.e. ℓ= argmaxi∈{1,...,k}Si(hi,DP I)
where hi,DP I is the DPI bandwidth choice for indicator i.


## Page 14


14
Paruolo, Saisana & Saltelli
The higher the value of dm, the more discrepancy there is between relative target
importance and the corresponding relative main eﬀects. In dm we have chosen to
capture the discrepancy by focusing on the maximal deviation; alternatively one
can consider any absolute power mean, f-divergence function or distance between
the (un-normalized) distributions {ζ2
i } and {Si/S1}. For simplicity, in the following
we indicate these distributions used in the comparison as {ζ2
i } and {Si}.
Because dm depends on the choice of bandwidth parameters h in the estimation
of Si(h), i = 1, . . . , k we also calculated bounds on the variation of dm obtained by
varying h. Speciﬁcally, we computed dm comparing {ζ2
i } with {Si,ℓi} choosing ℓi
as either equal to min or max, considering all possible combinations. For instance,
with k = 2, we considered {S1,min, S2,min}, {S1,min, S2,max}, {S1,max, S2,min} and
{S1,max, S2,max}.
Within the distribution of values of dm obtained in this way,
we recorded the minimum and the maximum, denoted as dm,min dm,max. Table
5 reports the dm for h equal to hDP I, hCV and in the linear case, along with the
values dm,min, dm,max, which provide a measure of sensitivity of dm with respect to
the choice of bandwidth h.
To compare the Si values with the weights wi graphically, in Fig 5 we re-scale
the Si values to have sum equal to one, considering S∗
i := Si/c with c := Pk
t=1 St,
which we call ‘normalized Si’. In order to visualise bounds for S∗
i , we plot bars
with endpoints equal to Si,min/c and Si,max/c; these bars inform on the sensitivity
of S∗
i with respect to the variation of the bandwidth parameter h.
3.4.
Reverse-engineering the weights
This section discusses when it is possible to ﬁnd nominal weights wi that imply
pre-determined, given values z2
i for the relative main eﬀects Si/S1; here we indicate
the target relative importance z2
i to diﬀerentiate it from ζ2
i of the previous sec-
tions. This reverse-engineering exercise can help developers of composite indicators
to anticipate criticism by enquiring if the stated relative importance of pillars or
indicators is actually attainable.
For the purpose of this inversion, we consider the case of fi(xi) linear in xi;
in this case Si coincides with R2
i , the square of Pearson’s product moment corre-
lation coeﬃcients between y and xi. The linear case can be seen as a ﬁrst order
approximation to the nonlinear general case; this choice is motivated by the fact
that one can ﬁnd an exact solution to the inversion problem of the map from wi
to R2
i /R2
1 when one allows weights wi also to be negative. One expects that the
reverse-engineering formula in the linear case to be indicative of the one based on a
non-linear approach, where the latter would be computationally more demanding.
We wish to ﬁnd a value w∗:= (w∗
1, . . . , w∗
k)′ for the vector of nominal weights
w := (w1, . . . , wk)′ such that R2
i /R2
1 equals pre-selected target values z2
i , for i =
1, . . . , k. We call this the ‘inverse problem’. The weights w∗
i are chosen to sum to
1, but they are allowed also to be negative; this choice makes the inverse problem
solvable, and in the Appendix we show that it has a unique solution, given by
w∗=
1
1′Σ−1gΣ−1g.
(7)
where g is a vector with i-th entry equal to gi := zi
p
σii/σ11 and 1 is a k-vector of
ones.
Because the solution to this inverse problem is unique, if some of the weights w∗
j
in (7) are negative, it means that a solution to the inverse problem with all positive


## Page 15


Ratings and rankings
15
Table 1. Bandwidth choice at indicator level. Bandwidth h: hi,CV (cross
validation), hi,DP I (direct plug-in, DPI); p-values for the linearity test:
pi,CV (p-value for hi,CV ), pi,DP I (p-value for hi,DP I); n is the number
of observations with xji > 0 used for CV and DPI; ∗: right end of the grid
H.
hCV
pCV
hDP I
pDP I
n
2008 ARWU
Alumni winning Nobel
25.05∗
0.88
3.43
0.71
198
Staﬀwinning Nobel
25.05∗
0.59
3.13
0.27
135
Highly cited res.
25.05∗
0.00
1.15
0.00
424
Art. in Nature and Science
9.05
0.00
1.78
0.00
494
Art. in Science and Social CI
2.94
0.00
2.26
0.00
503
Academic perf. (size adj)
1.74
0.00
2.12
0.00
503
2008 THES
Academic review
4.46
0.00
1.74
0.00
400
Recruiter review
5.81
0.00
2.62
0.00
400
Teacher/Student ratio
4.46
0.07
4.76
0.08
399
Citations per faculty
25.05∗
0.04
2.44
0.20
400
International staﬀ
6.81
0.04
2.97
0.22
398
International students
25.05∗
0.18
4.13
0.65
399
2009 HDI
Life expectancy
0.09
0.00
0.08
0.00
142
Adult literacy
0.05
0.00
0.07
0.00
142
Enrolment in education
0.04
0.00
0.06
0.00
142
GDP per capita
0.09
0.00
0.08
0.00
142
weights does not exist, and hence the targets z2
i are not attainable, owing to the data
covariance structure. This can help designers to re-formulate their targets to make
them attainable, and the stakeholders involved in the use of the composite indicator
to evaluate wether the individual indicators can have the stated importance by an
appropriate choice of weights.
4.
Case studies
In this section we apply the statistical analysis that was described in Section 3 to
the six composite indicators. In Section 4.1 we consider the three indices for which
aggregation was performed at indicator level and in Section 4.2 we consider the
three indices for which aggregation was performed at the pillar level.
4.1.
Importance at the indicator level
We consider the Human Development Index (HDI) and two well known composite
indicators of university performance: the Academic Ranking of World Universities
by Shanghai’s Jiao Tong University (ARWU) and the one associated to the UK’s
Times Higher Education Supplement (THES).
University Ranking
The ARWU, Center for World-Class Universities (2008), summarizes quality of ed-
ucation, quality of faculty, research output and academic performance of world
universities using six indicators: the number of alumni of an institution having


## Page 16


16
Paruolo, Saisana & Saltelli
Table 2. Main effects at indicator level. Nominal weights wi; main effects Si: Si,lin :=
Si(∞) (linear ﬁt), Si,CV := Si(hCV ) (cross validation), Si,DP I := Si(hDP I) (direct
plug-in), Si,min := minh∈H Si(h), Si,max := maxh∈H Si(h).
wi
Si,lin
Si,CV
Si,DP I
Si,min
Si,max
2008 ARWU
Alumni winning Nobel
0.10
0.64
0.65
0.67
0.65
0.76
Staﬀwinning Nobel
0.20
0.72
0.72
0.73
0.72
0.80
Highly cited res.
0.20
0.81
0.85
0.87
0.85
0.90
Art. in Nature and Science
0.20
0.87
0.88
0.88
0.88
0.94
Art. in Science and Social CI
0.20
0.63
0.70
0.70
0.64
0.90
Academic perf. (size adj)
0.10
0.71
0.76
0.75
0.72
0.88
2008 THES
Academic review
0.40
0.77
0.81
0.82
0.78
0.85
Recruiter review
0.10
0.45
0.54
0.54
0.46
0.62
Teacher/Student ratio
0.20
0.19
0.21
0.20
0.18
0.42
Citations per faculty
0.20
0.38
0.38
0.41
0.38
0.50
International staﬀ
0.05
0.10
0.12
0.12
0.10
0.31
International students
0.05
0.16
0.16
0.17
0.16
0.34
2009 HDI
Life expectancy
0.33
0.80
0.80
0.80
0.78
0.85
Adult literacy
0.22
0.77
0.78
0.77
0.76
0.83
Enrolment in education
0.11
0.77
0.81
0.78
0.73
0.86
GDP per capita
0.33
0.85
0.84
0.84
0.84
0.88
won Nobel Prizes or Fields Medals (weight of 10%), the number of Nobel or Fields
laureates among the staﬀof an institution (weight of 20%), the number of highly
cited researchers (weight of 20%), the number of articles published in Nature or Sci-
ence, Science Citation Index Expanded and Social Sciences Citation Index (weight
of 40%), and ﬁnally the academic performance measured as the weighted average
of the above ﬁve indicators divided by the number of full-time equivalent academic
staﬀ(weight of 10%). The raw data are normalized by assigning to the best perform-
ing institution a score of 100 and all other institutions receiving a score relative to
the leader. The ARWU score is a weighted average of the six normalized indicators,
which is ﬁnally re-scaled to a maximum of 100. The six indicators have moder-
ate to strong correlations in the range from 0.48 to 0.87 and an average bivariate
correlation of 0.68.
The THES, Times Higher Education Supplement (2008), summarizes university
features related to research quality, graduate employability, international orienta-
tion and teaching quality using six indicators: the opinion of academics on which
institutions they consider to be the best in the relevant ﬁeld of expertise (weight
of 40%), the number of papers published and citations received by research staﬀ
(weight of 20%), the opinion of employers about the universities from which they
would prefer to recruit graduates (weight of 10%), the percentage of overseas staﬀ
at the university (weight of 5%), the percentage of overseas students (weight of
5%), and ﬁnally the ratio between the full-time equivalent faculty and the number
of students enrolled at the university (weight of 20%). Raw data are standardized.
The standardized indicator scores are then scaled by dividing by the best score.
The THES score is the weighted average of the six normalized indicators, which is
ﬁnally re-scaled to a maximum of 100. The six indicators have very low to moderate
correlations that range from 0.01 to 0.64 and a low average bivariate correlation of
0.24.


## Page 17


Ratings and rankings
17
Results for ARWU and THES are given in Tables 1-2 and 5.
The ﬁrst two
panels of Table 1 provide the bandwidth selection results for ARWU and THES;
the corresponding panels of Table 2 give estimates of the importance measure Si
for diﬀerent choices of bandwidth. The ﬁrst two lines in Table 5 give the maximum
discrepancy statistic dm for ARWU and THES. Finally the two upper graphs in
Fig. 5 summarize the comparison between target and actual relative importance of
indicators. For ARWU the main eﬀects Si are more similar to each other than the
nominal weights, i.e. ranging between 0.14 and 0.19 (normalised Si values to unit
sum, cross validation estimates) when weights should either be 0.10 or 0.20.
The situation is worse for THES, where the combined importance of peer review
based variables (recruiters and academia) appears larger than stipulated by devel-
opers, indirectly supporting the hypothesis of linguistic bias at times addressed to
this measure (see e.g. Saisana et al. (2011) for a review). Further for THES the
‘teachers to student ratio’, a key variable aimed at capturing the teaching dimen-
sion, is much less important than it should be when comparing normalized Si (0.09,
cross validation estimate) with the nominal weight (0.20).
Overall, there is more discrepancy between the nominal weights assigned to the
six indicators and their respective main eﬀects in THES (dm,CV = 0.42) than in
ARWU (dm,CV = 0.36), cross validation estimates. Comparing this result with
the conclusions in Saisana et al. (2011), we can see the value-added of the present
measure of importance. In that paper we could not draw a judgement about the
relative quality of THES with respect to ARWU. The main eﬀects used here allow
us to say that – leaving aside the diﬀerent normative frameworks about which no
statistical inference can be made – ARWU is statistically more consistent with its
declared targets than THES.
When considering the sensitivity of dm values to the choice of bandwidths h, one
can see that the range [dm,min, dm,max] is slightly shorter for ARWU ([0.26, 0.50])
than for THES ([0.29, 0.55]); this implies that ARWU is slightly less sensitive than
THES to the choice of bandwidths h. Note however that the two ranges overlap,
so that there are choice of bandwidths h for which the ordering of dm values is
reversed. This, however, does not happen at the values hCV and hDP I.
The hypothesis of linearity is not rejected for two indicators for ARWU and for
four indicators for THES, when evaluating the tests at hDP I and hCV . The two
indicators for ARWU are those with the highest proportion of values equal to 0,
which were discarded in the choice of bandwidth; the number of valid cases n are
198 and 135 respectively. This may reﬂect the fact that it is more diﬃcult to reject
linearity with smaller samples. The indicators used in THES instead do not have so
many zero values; also here however, one ﬁnds that E(y|xi) is approximately linear
for 4 indicators.
The Human Development Index 2009
The HDI, see United Nations Development Programme (2009), summarizes human
development in 182 countries based on four indicators: a long healthy life measured
by life expectancy at birth (weight of 1/3), knowledge measured by adult literacy
rate (weight of 2/9) and combined primary, secondary and tertiary gross enrollment
ratio (weight of 1/9), and a decent standard of living measured by the GDP per
capita (weight of 1/3). Raw data in the four indicators are normalized by using
the min-max approach to be in [0, 1]. The 2009 HDI score is the weighted average
of the four normalized indicators. Because data on Adult literacy rate was missing


## Page 18


18
Paruolo, Saisana & Saltelli
Table 3. Bandwidth choice at pillar level. Bandwidth h: hi,CV (cross
validation), hi,P DI (DPI); p-values for the linearity test: pi,CV (p-value for
hi,CV ), pi,DP I (p-value for hi,DP I); n is the number of observations with
xji > 0 used for CV and DPI; ∗: right end of the grid H.
hCV
pCV
hDP I
pDP I
n
2010 HDI
Life expectancy
0.08
0.00
0.07
0.00
169
Education
0.02
0.09
0.06
0.21
169
GDP per capita
0.05
0.00
0.06
0.00
169
IAG
Safety and security
17.69
0.15
3.31
0.45
53
rule of law and corruption
25.05∗
0.30
4.75
0.94
53
part. and human rights
4.89
0.08
2.85
0.41
53
Sust. economic opportunity
22.14
0.09
4.21
0.51
53
Human development
25.05∗
0.17
3.42
0.87
53
SSI
Personal development
0.69
0.00
0.37
0.00
151
Healthy environment
25.05∗
0.41
0.49
0.69
151
Well-balanced society
0.69
0.00
0.42
0.01
151
Sustainable use of resources
0.30
0.00
0.30
0.00
150
Sustainable World
0.86
0.00
0.38
0.01
151
for several countries, we analyzed data only for the countries without missing data;
this gave a total of 142 countries. The four indicators present strong correlations
that range from 0.70 to 0.81 and an average bivariate correlation of 0.74.
Nominal weights and estimates of the main eﬀects are given in the last panel
of Table 2, while the choice of bandwidth is given in Table 1.
The maximum
discrepancy is given in Table 5 and a graphical comparison of nominal weights and
estimates of the main eﬀects is provided in Fig. 5. Table 1 reports evidence on the
choice of bandwidth h and the p-values for the linearity test, at the values hDP I
and hCV of the smoothing parameter h.
Both the main eﬀects Si and the Pearson correlation coeﬃcients reveal a rela-
tively balanced impact of the four indicators ‘life expectancy’, ‘GDP per capita’,
‘enrolment in education’, and ‘adult literacy’ on the variance of the HDI scores, with
the adult literacy being slightly less important. It would seem that HDI depends
more equally from its four variables than the weights assigned by the developers
would imply. For example, if one could ﬁx adult literacy the variance of the HDI
scores would on average be reduced by 77% (CV estimate), whereas by ﬁxing the
most inﬂuential indicator, GDP per capita, the variance reduction would be 84%
on average.
One might suspect that it was precisely the developers’ intention, when assign-
ing nominal weights 11% and 33% to these two variables respectively, to make them
equally important on the basis of the Si measure; however this is is not stated explic-
itly in the index documentation report United Nations Development Programme
(2009). Overall, there is considerable discrepancy between the nominal weights as-
signed to the four indicators and their respective main eﬀects in 2009 HDI (dm,CV =
0.63).
The analysis of the 2009 HDI illustrates vividly that assigning unequal weights to
the indicators is not a suﬃcient condition to ensure unequal importance. Although
the 2009 HDI developers assigned weights varying between 11% and 33%, all four
indicators are roughly equally important. The scatterplots in Fig. 1-4 help visualize


## Page 19


Ratings and rankings
19
Table 4. Main effects at pillar level. Nominal weights wi; main effects Si: Si,lin :=
Si(∞) (linear ﬁt), Si,CV := Si(hCV ) (cross validation), Si,DP I := Si(hDP I) (direct
plug-in), Si,min := minh∈H Si(h), Si,max := maxh∈H Si(h).
wi
Si,lin
Si,CV
Si,DP I
Si,min
Si,max
2010 HDI
Life expectancy
0.33
0.82
0.84
0.84
0.81
0.86
Education
0.33
0.86
0.87
0.86
0.84
0.89
GDP per capita
0.33
0.90
0.90
0.90
0.89
0.93
IAG
Safety and security
0.20
0.52
0.54
0.63
0.51
0.87
rule of law and corruption
0.20
0.77
0.76
0.78
0.76
1.00
part. and human rights
0.20
0.44
0.63
0.68
0.43
1.00
Sust. economic opportunity
0.20
0.52
0.52
0.56
0.52
0.98
Human development
0.20
0.50
0.50
0.55
0.49
0.94
SSI
Personal development
0.13
0.05
0.14
0.17
0.04
0.27
Healthy environment
0.13
0.04
0.04
0.07
0.04
0.27
Well-balanced society
0.13
0.13
0.21
0.21
0.12
0.32
Sustainable use of resources
0.30
0.48
0.64
0.64
0.47
0.72
Sustainable World
0.30
0.02
0.06
0.10
0.02
0.29
the situation. In cases like this, where the variables are strongly and roughly equally
correlated with the overall index, each of them ranks the countries roughly equally,
and the weights are little more than cosmetic.
4.2.
Importance at the pillar level
The issue of weighting is particularly fraught with normative implications in the
case of pillars. As mentioned above, pillars in composite indicators are often given
equal weights on the ground that each pillar represents an important – possibly
normative – dimension which could not and should not be seen to have more or less
weight than the stipulated fraction. The discrepancy measure presented here can
be of particular relevance and interest to gauge the quality of a composite indicator
with respect to this important assumption. Here we consider the 2010 version of
the HDI, the Index of African Governance (IAG) and the Sustainable Society Index
(SSI).
The Human Development Index 2010
In this section we analyze the 2010 version of the HDI at the pillar level, covering
169 countries. From the methodological viewpoint the main novelty in this version
of the index is the use of a geometric – as opposed to an arithmetic – mean, in
the aggregation of the three pillars. The three pillars cover health (life expectancy
at birth) xlife, education xedu and income (gross national income per capita) xinc.
Education is the combination of two variables, namely mean years of schooling and
expected years of schooling, see United Nations Development Programme (2010).
The 2010 HDI index y is computed as
y = (xlife · xedu · xinc)
1
3
where all three dimensions have equal weights. The reason for this change of ag-
gregation scheme is to introduce an element of ‘imperfect substitutability across all


## Page 20


20
Paruolo, Saisana & Saltelli
Table 5. Maximum discrepancy statistic dm for different choice
of the bandwidth h in the main effect estimator Si(h). DPI: di-
rect plug-in, CV: cross validation, lin: linear ﬁt, min and max
values where obtained by considering all possible combina-
tions of Si,ℓi values, where ℓi = min, max.
dm,DP I
dm,CV
dm,lin
dm,min
dm,max
ARWU
0.36
0.36
0.31
0.26
0.50
THES
0.41
0.42
0.34
0.29
0.55
2009 HDI
0.59
0.63
0.57
0.50
0.69
2010 HDI
0.06
0.07
0.09
0.03
0.13
IAG
0.29
0.34
0.42
0.13
0.57
SSI
0.85
0.91
0.95
0.38
0.98
HDI dimensions’, i.e. to reduce the compensatory nature of the linear aggregation,
see (United Nations Development Programme, 2010, p. 216).
Nominal weights and estimates of the main eﬀects are given in the ﬁrst panel
of Table 4, while the choice of bandwidth is given in Table 3.
The maximum
discrepancy is given in row 4 of Table 5 and a graphical comparison of nominal
weights and estimates of the main eﬀects is provided in Fig. 5.
Overall, the HDI 2010 shows very little discrepancy between the goals of equal
importance of the three pillars and the main eﬀects. In fact all three pillars have
similar impact on the index variance (roughly 84 −90%). Hence, in this case the
relative nominal weights are approximately equal to the relative impact of the pil-
lars’ on the index variance. Such a correspondence is of value because it indicates
than no pillar impacts too much or too little the variance of the index as compared
to its ‘declared’ equal importance. Compared to the other examples discussed, the
2010 HDI is the most consistent in this respect (dm,CV = 0.07). The linearity tests
reveal that the role of education is approximately linear within the index, despite
the multiplicative aggregation scheme.
In order to assess the impact of the choice of the aggregation scheme on the
index balance, we also perform a counterfactual analysis of the 2010 HDI using
linear aggregation of the three dimensions. We ﬁnd that this choice does not aﬀect
the relative importance of dimensions, as these have comparable variances and
covariances. Hence the 2010 HDI would have been balanced also under a linear
aggregation scheme. This, however, does not detract from the conceptual appeal of
imperfect substitutability implicit in geometric aggregation.
Index of African Governance
The Index of African Governance was developed by the Harvard Kennedy School,
see Rotberg and Gisselquist (2008); for a validation study see Saisana et al. (2009).
In the 2008 version of the index, 48 African countries are ranked according to ﬁve-
pillars: (i) Safety and Security, (ii) Rule of Law, Transparency, and Corruption,
(iii) Participation and Human Rights, (iv) Sustainable Economic Opportunity, and
(v) Human Development. The ﬁve pillars are described by fourteen sub-pillars that
are in turn composed of 57 indicators in total (in a mixture of qualitative and
quantitative variables). Raw indicator data were normalized using the min-max
method on a scale from 0 to 100. The ﬁve pillar scores per country were calculated
as the simple average of the normalized indicators. Finally, the IAG scores were
calculated as the simple average of the ﬁve pillar scores.
The ﬁve pillars have


## Page 21


Ratings and rankings
21
x1
x2
x3
x4
x5
x6
0
0.2
0.4
ARWU
x1
x2
x3
x4
x5
x6
0
0.2
0.4
THES
x1
x2
x3
x4
0
0.2
0.4
HDI 2009
x1
x2
x3
0
0.2
0.4
HDI 2010
x1
x2
x3
x4
x5
0
0.2
0.4
IAG
x1
x2
x3
x4
x5
0
0.5
SSI
Fig. 5. Comparison of normalized main effects S∗
i (in light grey) and wi (in dark grey). S∗
i :=
Si/c with c := Pk
t=1 St and Si := Si,CV (cross validation). The indicators xi are numbered
consecutively as in Tables 1–4. Bounds for S∗
i are constructed as Si,min/c, Si,max/c.
correlations that range from 0.096 to 0.76 and average bivariate correlation of 0.45.
Three pairwise correlations (involving Participation and Human Rights and either
Sustainable Economic Opportunity or Human Development or Safety & Security)
are not statistically signiﬁcant at the 5% level.
Nominal weights and main eﬀects are given in Table 4 and in Fig. 5, while the
choice of bandwidth is reported in Table 3 and the discrepancy statistics in Table 5.
The main conclusions are summarized as follows: The IAG is a good example of the
situation discussed in Section 1 whereby all pillars represent important normative
elements which by design should be equally important in the developers’ intention.
Overall the IAG appears to be balanced with respect to four pillars that have similar
impact on the index variance (roughly 50 −63%), but the ﬁfth pillar on the Rule of
Law is more inﬂuential than conceptualised (Si = 76%, cross validation estimate).
The IAG has a maximal discrepancy statistic dm,CV = 0.34.
The linearity tests in Table 3 suggest that there is no statistical evidence against
linearity for all the ﬁve indicators. Hence one could calculate Si here as R2
i .
Sustainable Society Index
The Sustainable Society Index (SSI) has been developed by the Sustainable Soci-
ety Foundation for 151 countries and it is based on a deﬁnition of sustainability of


## Page 22


22
Paruolo, Saisana & Saltelli
the Brundtland Commission (van de Kerk and Manuel, 2008). Also in this exam-
ple, the ﬁve pillars of the index represent normative dimensions which are, how-
ever, considered of diﬀerent importance: Personal Development (weight of 1/7),
Healthy Environment (1/7), Well-balanced Society (1/7), Sustainable Use of Re-
sources (2/7), and Sustainable World (2/7). These ﬁve pillars are described by 22
indicators. Raw indicator data were normalized using the min-max method on a
scale from 0 to 10. The ﬁve pillars were calculated as the simple average of the
normalized indicators. The SSI scores were calculated as the weighted average of
the ﬁve pillar scores.
One can note that the linearity test suggests that for the second pillar ‘Healthy
Environment’ there is no evidence against linearity of its relation to the SSI index.
The ﬁve pillars have correlations that range from −0.62 to 0.75, where negative
correlations between pillars are generally undesired, as they suggest the presence
of trade-oﬀs between pillars (e.g. economic performance can only come with an
environmental cost). Such trade-oﬀs within index dimensions are a reminder of the
danger of compensability between dimensions.
For the Sustainable Society Index, there are notable diﬀerences between declared
and variance-based importance for the ﬁve pillars. The diﬀerent association between
a pillar and the overall index can also be grasped visually in Fig. 5.
The two
pillars on ‘Sustainable use of resources’ and on ‘Sustainable World’ are meant to be
equally important accordingly to the nominal weights (2/7 each), while the main
eﬀects suggest that the variance reduction obtained by ﬁxing the former is 67%
compared to merely 9% by ﬁxing the latter. This strong discrepancy is due to the
signiﬁcant negative correlations present among the SSI pillars. Overall, the level of
maximal discrepancy of the SSI is the highest of the examples discussed (dm,CV =
0.91). The authors and the developers of the SSI have been communicating on this
issue, and the 2010 version of the SSI index appears considerably improved, see
http://www.ssfindex.com/ssi/.
4.3.
Reverse-engineering the weights
Applying the reverse engineering exercise described in Section 3.4 and the Appendix
to our test cases (except for the case of 2010 HDI that has low maximal discrep-
ancy between relative weights and relative importance for the three pillars, and
it is not obtained by the linear aggregation scheme (1)), we ﬁnd that to achieve
a relative impact of the indicators (or pillars) (as measured by the square of the
Pearson correlation coeﬃcient R2
i ) that equals the relative ‘declared’ importance
of the indicators, negative nominal weights are involved in all studies except for
the SSI. In the case of SSI, to guarantee that the two pillars on Sustainable Use of
Resources and Sustainable World are twice as important as the other three pillars,
the nominal weights to be assigned to them are Personal Development (weight of
0.19), Healthy Environment (0.16), Well-balanced Society (0.07), Sustainable Use
of Resources (0.16), and Sustainable World (0.41). For all other cases, the data
correlation structure does not allow the developers to achieve the stated relative
importance by choosing positive weights.
5.
Conclusions
According to many – including some of the authors of the Stiglitz report, see
Stiglitz et al. (2009) – composite indicators have serious shortcomings. The debate


## Page 23


Ratings and rankings
23
among those who prize their pragmatic nature in relation to pragmatic problems,
see Hand (2009), and those who consider them an aberration is unlikely to be set-
tled soon, see Saltelli (2007) for a review of pros and cons. Still these measures
are pervasive in the public discourse and represent perhaps the best known face of
statistics in the eyes of the general public and media.
One might muse that what oﬃcial statistics are to the consolidation of the mod-
ern nation state, see Hacking (1990), composite indicators are to the emergence of
post-modernity, – meaning by this the philosophical critique of the exact Science
and rational knowledge programme of Descartes and Galileo, see Toulmin (1990),
p. 11-12. On a practical level, it is undeniable that composite indicators give voice
to a plurality of diﬀerent actors and normative views. The authors in Stiglitz et al.
(2009) remark (p. 65):
“The second [argument against composite indicators] is a general criticism that
is frequently addressed at composite indicators, i.e. the arbitrary character of the
procedures used to weight their various components. (...) The problem is not that
these weighting procedures are hidden, non-transparent or non-replicable — they are
often very explicitly presented by the authors of the indices, and this is one of the
strengths of this literature. The problem is rather that their normative implications
are seldom made explicit or justiﬁed.”
The analysis of this paper shows that, although the weighting procedures are often
very explicitly presented by the authors of the indices, the implications of these
are neither fully understood, nor assessed in relation to the normative implications.
This paper proposes a variance-based tool to measure the internal discrepancy of a
composite indicator between target and eﬀective importance.
Our main conclusions can be summarized as follows. For transparency and sim-
plicity, composite indicators are most often built using linear aggregation procedures
which are fraught with the diﬃculties described in the Introduction: practitioners
know that weights cannot be used as importance, while they are precisely elicited as
if they were. Weights are instead measures of substitutability in linear aggregation.
The error is particularly severe when a variable’s weight substantially deviates from
its relative strength in determining the ordering of the units (e.g. countries) being
measured.
Pearson’s correlation ratio (or main eﬀect) that is suggested in this paper is a
suitable measure of importance of a variable (be it indicator or pillar) because: i) it
oﬀers a precise deﬁnition of importance (that is ‘the expected reduction in variance
of the composite indicator that would be obtained if a variable could be ﬁxed’), ii)
it can be used regardless of the degree of correlation between variables, iii) it is
model-free, in that it can be applied also in non-linear aggregations, and ﬁnally iv)
it is not invasive, in that no changes are made to the composite indicator or to the
correlation structure of the indicators.
Because of property i) and the fact that it takes the whole covariance structure
into account, the main eﬀect can also be useful to prioritise variables on which a
country or university, or whatever units are being rated, could intervene to improve
its overall score. Note that the indicator with highest main eﬀect is not necessarily
the one in which the country scores the worst.
The main eﬀects approach can complement the techniques for robustness analy-
sis applied to composite indicators thus far seen in the literature, see e.g. Saisana et al.
(2005); Organisation for Economic Co-operation and Development (2008); Saisana et al.


## Page 24


24
Paruolo, Saisana & Saltelli
(2011). The approach described in this paper does not need an explicit modeling
of error-propagation but it is simply based on the data as produced by developers.
The discrepancy statistic based on the absolute error between ratios of the main
eﬀects and of the corresponding target relative importance provides a pragmatic
answer to the research question posed in this paper.
Relative main eﬀects are
variance-based, and hence they are ratios of quadratic forms of nominal weights,
while target relative importance are often deduced as ratios of nominal weights.
Comparing them via the discrepancy statistic is a way to compare these two impor-
tance measures, one of which is stated ex-ante as a target and the other one that is
computed ex-post; this allows to see how close the two measures are in practice.
The discrepancy statistic has been eﬀective in the six examples discussed, in that
it allowed an analytic judgement about the discrepancy in the assignment of the
weights in two well known measures of higher education performance (dm = 0.42
for THES versus dm = 0.36 for ARWU), two versions of a human development
index (dm = 0.63 for the 2009 HDI and dm = 0.02 for the 2010 HDI), one index of
governance (dm = 0.34 for the IAG) and one index of sustainability (dm = 0.86 for
the SSI).
Our reverse engineering analysis shows that in most cases it is not possible to
ﬁnd nominal weights that would give the desired importance to variables. This can
be a useful piece of information to developers, and might induce a deeper reﬂection
on the cost of the simpliﬁcation achieved with linear aggregation. Developers could
thus:
a) avoid associating nominal weights with importance, but inform users of the
relative importance of the variables or pillars, using statistics such as those
presented in this paper;
b) abstain from aggregating pillars when these display important trade oﬀs which
make it diﬃcult to give them target weights in an aggregated index;
c) reconsider the aggregation scheme, moving from the linear one (which is fully
compensatory) to a partially- or fully-non-compensatory alternative, such as
e.g. a Condorcet-like (or approximate Condorcet) approach, where weights
would fully play their role as measure of importance, see Munda (2008);
d) assess diﬀerent weighting strategies, so as to select the one that leads to a
minimum discrepancy statistic between target weights and variables impor-
tance.
Acknowledgement
We thank, without implicating, Beatrice d’Hombres, Giuseppe Munda, the Asso-
ciate Editor and two Referees for useful comments. The views expressed are those
of the authors and not of the European Commission or the University of Insubria.
Appendix - Solution to the inverse problem
In the linear case, the ratio Si/S1 equals the ratio of squares of Pearson’s correlation
coeﬃcients R2
i /R2
1; this is a function Hi (w) of w := (w1, . . . , wk) and of the covari-
ance matrix Σ of x := (x1, . . . , xk)′. One ﬁnds H (w) = (e′
iΣw)2 σ11/((e′
1Σw)2 σii),
where ei is the i-th column of the identity matrix of order k and σii is the i-th vari-
ance on the diagonal of Σ. We wish to make Hi (w) equal to a pre-selected value


## Page 25


Ratings and rankings
25
z2
i for all i:
Hi (w) = z2
i ,
i = 1, . . . , k,
(8)
and seeks to ﬁnd a solution w ∈Rk to this problem such that nominal weight to
sum to 1, i.e.
1′w = 1.
(9)
We show that this solution is unique and it is given by (7) in the text, where g is a
vector with i-th entry equal to gi := zi
p
σii/σ11 > 0 and 1 is a k-vectors of ones.
Note that by construction g1 = 1. One has that (8) can be written as e′
1Σw −
1
gi e′
iΣw = 0, or, setting G := diag(1, 1/g2, . . . 1/gk), F := 1e′
1 as (F −G) Σw = 0.
This shows that Σw should be selected in the right null space of F −G. We observe
that
F −G =






0
0
0
1
−1/g2
...
...
...
0
1
0
−1/gk






whose right null-space A is one dimensional; moreover A is spanned by g :=
(1, g2, . . . , gk)′. Hence Σw = gc for a nonzero c or w = Σ−1gc. Substituting this
expression in (9), one ﬁnds 1 = 1′w = 1′Σ−1gc, which implies c = 1/1′Σ−1g. One
hence concludes that the weights that satisfy (8) are given by (7), and that they
are unique.
References
Agrast, M. D., J. C. Botero, and A. Ponce (2010). Rule of law index 2010. Technical
report, World Justice Project, Washington, DC, http://worldjusticeproject.org/.
Balinski, M. and R. Laraki (2010). Majority Judgment. Measuring, ranking and
electing. MIT Press.
Bandura, R. (2008). A survey of composite indices measuring country performance:
2008 update. Technical report, United Nations Development Programme - Oﬃce
of Development Studies, New York.
Billaut, J. C., D. Bouyssou, and P. Vincke (2010). Should you believe in the Shang-
hai ranking? Scientometrics 84, 237–263.
Bird, S. M., D. Cox, V. T. Farewell, H. Goldstein, T. Holt, and P. C. Smith (2005).
Performance indicators: good, bad, and ugly. J. R. Statist. Soc. A 168, 1–27.
Bowman, A. W. and A. Azzalini (1997). Applied Smoothing Techniques for Data
Analysis: A Kernel Approach with S-Plus Illustrations. Oxford: Clarendon Press.
Boyssou, D., T. Marchant, M. Pirlot, and A. Tsouki`as (2006). Evaluation and De-
cision Models with Multiple Criteria: Stepping Stones for the Analyst. Springer.
Center for World-Class Universities (2008). Academic ranking of world universities
- 2008.
Technical report, Institute of Higher Education, Shanghai Jiao Tong
University, China, http://www.arwu.org/.


## Page 26


26
Paruolo, Saisana & Saltelli
Decancq,
K.
and
M.
Lugo
(2012).
Weights
in
multidimensional
in-
dices of well-being:
An overview.
Econometric Reviews in press, DOI:
10.1080/07474938.2012.690641.
Freedom House (2011).
Freedom of the press 2011.
Technical report, Freedom
House, Wasghington DC, http://www.freedomhouse.org.
Hacking, I. (1990). The Taming of Chance. Cambrige University Press.
Hand, D. (2009). Measurement Theory and Practice: The World Through Quan-
tiﬁcation. Wiley.
Hendrik, W., C. Howard, and A. Maximilian (2008). Conwsequences of data error
in aggregate indicators: Evidence from the human development index. Technical
report, Department of Agricultral and Resource economics, UCB, UC Berkeley.
Leckie, G. and H. Goldstein (2009). The limitations of using school league tables
to inform school choice. J. R. Statist. Soc. A 172, 835–851.
Li, G., H. Rabitz, P. Yelvington, O. Oluwole, F. Bacon, C. Kolb, and J. Schoendorf
(2010). Global sensitivity analysis for systems with independent and/or correlated
inputs. Journal of Physical Chemistry 114,, 6022.
Munda, G. (2008). Social Multi-Criteria Evaluation for a Sustainable Economy.
Berlin Heidelberg: Springer-Verlag.
Munda, G. and M. Nardo (2009). Non-compensatory/non-linear composite indica-
tors for ranking countries: a defensible setting. Applied Economics 41, 1513–1523.
Nardo, M. (2009). Product market regulation: Robustness and critical assessment
1998-2003-2007 - How much conﬁdence can we have on PMR ranking?, EUR
23667. Technical report, European Commission, JRC-IPSC, Ispra, Italy.
Nicoletti, G., S. Scarpetta, and O. Boylaud (2000). Summary indicators of prod-
uct market regulation with an extension to employment protection legislation.
Technical report, OECD, Economics department working papers No. 226, OECD
Publishing. http://dx.doi.org/10.1787/215182844604.
Organisation for Economic Co-operation and Development (2008). Handbook on
Constructing Composite Indicators. Methodology and User guide. Paris: OECD.
Pearson, K. (1905). On the General Theory of Skew Correlation and Non-linear
Regression, volume XIV of Mathematical Contributions to the Theory of Evolu-
tion, Drapers’ Company Research Memoirs. Dulau & Co., London, Reprinted in:
Early Statistical Papers, Cambridge University Press, Cambridge, UK, 1948.
Plischke, E. (2010). An eﬀective algorithm for computing global sensitivityindices
(EASI). Reliability Engineering and System Safety 95, 354–360.
Ratto, M. and A. Pagano (2010). Using recursive algorithms for the eﬃcient iden-
tiﬁcation of smoothing spline ANOVA models.
AStA Advances in Statistical
Analysis 94, 367–388.
Ratto, M., A. Pagano, and P. Young (2007). State dependent parameter metamod-
elling and sensitivity analysis. Computer Physics Communications 177, 863–876.


## Page 27


Ratings and rankings
27
Ravallion, M. (2010). Troubling tradeoﬀs in the human development index, policy
research working paper 5484. Technical report, The World Bank, Development
Research Group, Washington, DC.
Reporters Sans Frontieres (2011). Press freedom index. Technical report, Reporters
Without Borders, Paris http://en.rsf.org/press-freedom-index-2010,1034.html.
Rotberg, R. and R. Gisselquist (2008). Strengthening african governance. ibrahim
index of african governance:
Results and rankings 2008.
Technical report,
Kennedy School of Government, Harward.
Ruppert, A., S. J. Sheather, and M. P. Wand (1995).
An eﬀective bandwidth
selector for local least squares regression. Journal of the American Statistical
Association 90, 1257–1270.
Ruppert, D. and M. P. Wand (1994). Multivariate locally weighted least squares
regression. The Annals of Statitics 22, 1346–1370.
Saaty, T. (1980). The Analytic Hierarchy Process. McGraw-Hill, New York.
Saaty, T. L. (1987). The analytic hierarchy process: what it is and how it is used.
Mathematical Modelling 9, 161–176.
Saisana, M., P. Annoni, and M. Nardo (2009). A robust model to measure gover-
nance in African countries, EUR 23773. Technical report, European Commission,
JRC-IPSC, Ispra, Italy.
Saisana, M., B. d’Hombres, and A. Saltelli (2011). Rickety numbers: Volatility of
university rankings and policy implications. Research Policy 40, 165–177.
Saisana, M., A. Saltelli, and S. Tarantola (2005). Uncertainty and sensitivity analy-
sis techniques as tools for the quality assessment of composite indicators. Journal
of the Royal Statistical Society - A 168(2), 307–323.
Saltelli, A. (2002). Making best use of model valuations to compute sensitivity
indices. Computer Physics Communications 145, 280–297.
Saltelli, A. (2007). Composite Indicators between analysis and advocacy. Social
Indicators Research 81, 65–77.
Saltelli, A., P. Annoni, I. Azzini, F. Campolongo, M. Ratto, and S. Tarantola (2010).
Variance based sensitivity analysis of model output. design and estimator for the
total sensitivity index. Computer Physics Communications 181, 259–270.
Saltelli, A., M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli,
M. Saisana, and S. Tarantola (2008). Global Sensitivity Analysis - The Primer.
John Wiley & Sons, Ltd.
Saltelli, A. and S. Tarantola (2002). On the relative importance of input factors in
mathematical models: safety assessment for nuclear waste disposal. Journal of
American Statistical Association 97, 702–709.
Sobol’, I. (1993). Sensitivity analysis for non-linear mathematical models. Math-
ematical Modelling and Computational Experiment 1, 407–414. Translated from
Russian: Sobol’, I. M., 1990, Sensitivity estimates for nonlinear mathematical
models, Matematicheskoe Modelirovanie 2, 112-118.


## Page 28


28
Paruolo, Saisana & Saltelli
Stanley, J. and M. Wang (1968). Diﬀerential weighting: a survey of methods and
empirical studies. Technical report, Johns Hopkins University, Baltimore.
Stiglitz, J. E., A. Sen, and J. Fitoussi (2009). Report by the commission on the
measurement of economic performance and social progress.
Technical report,
www.stiglitz-sen-ﬁtoussi.fr.
Tarantola, S., D. Gatelli, and T. Mara (2006). Random balance designs for the
estimation of ﬁrst order global sensitivity indices. Reliability Engineering and
System Safety 91(6), 717–727.
Times Higher Education Supplement (2008). World university rankings. Technical
report, http://www.timeshighereducation.co.uk.
Toulmin, S. (1990). Cosmopolis - The hidden agenda of modernity. University of
Chicago Press.
United Nations Development Programme (2009). Human development report 2009.
Technical report, http://hdr.undp.org/en/reports/.
United Nations Development Programme (2010). Human development report 2010.
Technical report, http://hdr.undp.org/en/reports/.
van de Kerk, G. and A. R. Manuel (2008). A comprehensive index for a sustainable
society: The SSI, Sustainable Society Index. Journal of Ecological Economics 66,
228–242.
Wang, M. W. and J. C. Stanley (1970). Diﬀerential weighting: a review of methods
and empirical studies. Review of Educational Research 40(5), 663–705.
Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data:
Second Edition. The Mit Press.
World Economic Forum (2010). The Global Competitiveness Report 2010-2011.
Technical report, World Economic Forum, http://www.weforum.org/.
Xu, C. and G. Gertner (2011). Understanding and comparisons of diﬀerent sam-
pling approaches for the fourier amplitudes sensitivity test (fast). Computational
Statistics and Data Analysis 55, 184–198.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.02502v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.02502v1_Marginalization_in_nonlinear_mixed-effects_models_with_an_application_to_dose-re

> Source: 1707.02502v1_Marginalization_in_nonlinear_mixed-effects_models_with_an_application_to_dose-re.pdf

> Pages: 11

---


## Page 1


Marginalization in nonlinear mixed-eﬀects models –
with an application to dose-response analysis
Daniel Gerhard daniel.gerhard@canterbury.ac.nz
School of Mathematics & Statistics,
University of Canterbury, Christchurch, New Zealand
and
Christian Ritz ritz@nexs.ku.dk
Department of Nutrition, Exercise and Sports, Faculty of Science,
University of Copenhagen, Rolighedsvej 30, 1958 Frederiksberg C, Denmark
July 11, 2017
Abstract
Inference in hierarchical nonlinear models needs careful consideration about targeting parameters
that have either a conditional or population-average interpretation. For the special case of mixed-
eﬀects nonlinear sigmoidal models we propose a method for the estimation of derived parameters with
a marginal interpretation, but also maintaining the random eﬀect structure of the nonlinear model,
by using a combination of numerical quadrature and the delta method, integrating over the random
eﬀect distribution conditional on the estimated variance components. The diﬀerence between these
marginalized estimates, generalized nonlinear least squares estimates, and conditional estimation is
characterised by means of two representative case studies. The case studies consist of the estimation of
eﬀective dose levels in a human toxicology study, and the relative potency estimation for two herbicides
in an agricultural ﬁeld trial. Both case studies exhibit an experimental design that results in data
with at least one hierarchical level of between- and within-cluster variation. A user-friendly software
implementation is made available with the R package medrc, providing an automated framework for
mixed-eﬀects dose-response modelling.
1
Introduction
Clustered data showing nonlinear trends have recently become routine output of experiments in agricul-
ture, biology, and toxicology (e.g., Clayton et al. (2003); Serroyen et al. (2005); Makowski and Lavielle
(2006)).
For these applied disciplines parameter estimates with marginal interpretations rather than
conditional interpretations would usually be relevant as such quantities provide insights and understand-
ing of population-level behaviour in the biological systems considered. This is a very diﬀerent focus as
compared to pharmacokinetics and pharmacodynamics studies where interest almost solely lies in the
conditional parameters (Davidian and Giltinan, 1995). Still, in practice conditional results derived from
nonlinear mixed-eﬀects models seem to be used most of the time.
For non-normal clustered data the diﬀerences between marginal and conditional modelling are well-
understood (e.g., McCulloch et al. (2008); Serroyen et al. (2009); Fitzmaurice et al. (2012); Gbur et al.
(2012); Demidenko (2013); Vonesh (2012)).
In particular the diﬀerence in interpretation in terms of
population-level versus conditional eﬀects have been both clariﬁed and debated over the last decade. It
has been argued that conditional modelling was to be preferred (Lee and Nelder, 2004), but there seems
to be pros and cons (Lee and Nelder, 2004, rejoinder). The conditional eﬀects focus on a single subject,
e.g. reporting a dose-response relationship with a subject-speciﬁc initial response at the lowest dose level.
This initial eﬀect might lead to a steeper curve, an earlier or later response, and a higher maximum
response level compared to the population average.
If no information about a speciﬁc individual is
available to predict a response and just a general eﬀect of a whole population of individuals is of interest,
the conditional eﬀects will not be an eﬃcient way to summarize the population distribution. And it has
1
arXiv:1707.02502v1  [stat.AP]  8 Jul 2017


## Page 2


to be noted that conditioning on the average subject eﬀects will not result in the expected population
response for nonlinear models.
In an attempt to bridge the gap between conditional and marginal models some authors have considered
marginalization (e.g.,Heagerty and Zeger (2000); Wang and Louis (2004); Parzen et al. (2011); Griswold
et al. (2013)). However, these authors only considered special cases of generalized linear mixed-eﬀects
models, using non-standard distributional assumptions for the random eﬀects or approximate attenuation
factors to address the integration over the random eﬀects distributions.
Conditional inference requires distributional assumptions at the level of each cluster next to assumptions
on the distribution of each measurement whereas marginal inference may be carried out while completely
ignoring the hierarchical structure. The marginal approach results in regression coeﬃcients that can
be interpreted as marginal eﬀects but their standard errors will not fully incorporate the correlation
between observations within individuals; i.e. for generalized estimation equation models Liang and Zeger
(1986) showed that the standard errors of estimated marginal regression coeﬃcients may be consistently
estimated, even when the assumed within-cluster correlation is incorrect. The relative eﬃciency of the
estimator will, however, be substantially increased by using a correctly speciﬁed correlation structure,
especially in case of highly correlated coeﬃcients.
For clustered data with nonlinear trends the arguments in favour of conditional modelling using nonlinear
mixed-eﬀects methodology are even more compelling than in the case for non-normal clustered data.
In the context of generalized linear mixed-eﬀects models all parameters are deﬁned on the same scale
introduced through the link function, which establishes the connection between the data scale and the
so-called model scale of the linear predictor (Stroup, 2014). In contrast, for nonlinear clustered data
usually several model scales are needed to accommodate all model parameters entering the nonlinear
model equation. For instance, three model scales, asymptotes, steepness, and ED50, are in use for the
four-parameter log-logistic model, which we will introduce in detail below. Random eﬀects are ideally
suited to describe varying magnitudes of variation inherent to these diﬀerent scales and diﬀerent random
eﬀects on diﬀerent scales will ensure that variation is captured in terms of the scale where it is present.
It is diﬃcult to imagine that marginal models can achieve a similar description of the variation based
on the data scale only.
Moreover, as pointed out by Griswold et al. (2013) choosing a conditional
modelling approach does not rule out considering marginal interpretations of parameter estimates of
interest. Indeed, conditional modelling allows both conditional and marginal interpretations of results. It
is noteworthy that choosing a marginal modelling strategy does not provide the same ﬂexibility as only
marginal interpretations will eventually be possible (McCulloch et al., 2008, p. 246).
Instead of the direct estimation of marginal parameters as in Heagerty and Zeger (2000), we focus on
calculating marginal predictions by means of population averages.
Whereas the random eﬀects in a
nonlinear hierarchical model can be deﬁned on the diﬀerent scales of the model parameters, estimating
nonlinear model coeﬃcients conditional on these random eﬀects, the main interest might lie on the
population averaged predictions. Based on the marginal predictions related marginalized parameters can
be derived.
In the present study, the marginalization approach, which was recently proposed by Gerhard et al. (2014)
for a speciﬁc nonlinear model for analysis of quantitative real-time polymerase chain reaction (QPCR)
data, is extended for arbitrary nonlinear mixed-eﬀects regression models, i.e., allowing for arbitrary
random eﬀects structures and also correlated residual errors. This extension leads a novel and operational
combination of numerical integration based on Gaussian quadrature and the delta method for error
propagation.
We will focus on important applications in pharmacology and toxicology where dose-response models
play a prominent role in evaluation of toxicity of chemicals. Such assessments usually involve one or more
quantities derived from the model parameters, e.g., eﬀective doses that correspond to a 10%, 20%, and
50% reduction in toxicity (ED10, ED20, and ED50). These parameters are interpreted by toxicologists
naturally in a population context (e.g., Weimer et al., 2012) but unfortunately the estimates that are
currently available when ﬁtting hierarchical models do not allow for such an interpretation. Hence, there
is an urgent need for a ﬂexible marginalization approach that is adapted to the more complex hierarchical
designs that now also becoming more common in toxicological experiments. Speciﬁcally, we extend the
comprehensive infrastructure for dose-response modelling outlined by Ritz and Streibig (2005), but only
for models without random eﬀects, to the case of dose-response mixed-eﬀects models.
We demonstrate its usefulness through two case studies exhibiting diﬀerent aspects of clustered data: a
2


## Page 3


toxicity evaluation in terms of eﬀective doses in a human toxicology study that was replicated six times
over time, and an assessment of potency in a ﬁeld trial comparing two pesticides using ﬁve blocks.
Section 2 introduces nonlinear mixed-eﬀects models in general. In Section 3 the marginalization approach
is derived. A short simulation study is presented in Section 4. Section 5 report results from two case
studies. Finally, we oﬀer a perspective on the developed methodology in Section 6.
2
Hierarchical nonlinear regression models
Following the notation of Davidian and Giltinan (2003), a nonlinear regression model with a single
hierarchical level can be deﬁned in two stages that parametrise the variation within and between speciﬁc
curves, respectively.
Stage 1: For the ith individual (i = 1, . . . , m), we assume the following nonlinear regression model:
yij = f(xij, βi) + ϵij
(1)
where {yi1, . . . , yini} and {xi1, . . . , xini} denote the vectors of response values and covariate levels, re-
spectively. A population of i diﬀerent curves is characterized by the nonlinear function f through the
curve-speciﬁc eﬀect βi (a q × 1 vector). The within-cluster variation is explained through the residual
error vector ϵi = (ϵi1, . . . , ϵini), which is assumed to be mean-zero normally distributed with variance-
covariance matrix Λi. In practice this matrix is often structured as σ2Ini or diag(σ2
1, . . . , σ2
ni).
Stage 2: The between curve variation is captured by splitting the curve-speciﬁc eﬀect βi into components
describing the systematic and random variation between curves:
βi = Aiβ + Bibi
where Ai and Bi denote the ﬁxed eﬀects and random eﬀects design matrices, respectively, β denotes the
ﬁxed eﬀects parameters (a p × 1 vector with p ≤q), and the bi’s denote the curve-speciﬁc random eﬀects.
The random eﬀects can be assumed to follow a mean-zero normal distribution with a variance-covariance
matrix denoted G, which usually is simply the unstructured matrix. In what follows we only consider
models with dummy coded design matrices for categorical predictors. These hierarchical models will
still cover many experimental settings used in practice, such as comparison of several treatments in a
dose-response experiment.
3
Quadrature
As already mentioned in the introduction the ﬁxed eﬀect parameters in nonlinear mixed-eﬀects models
usually cannot in general be interpreted as population quantities that are independent of the random
eﬀects, due to the inequality:
f(xij, Aiβ + 0) ̸= E {f(xij, βi)} = ˜f(xj, ˜
Ai˜β)
(2)
where ˜f denotes the unknown marginal mean function and, in particular, ˜β denotes the parameters we
are interested in.
In contrast, f denotes the mean function that was speciﬁed as part of the model
speciﬁcation. At this point we should mention that there are a few exceptions such as applications of
nonlinear mixed-eﬀects models with additive random eﬀects on the data scale, meaning that marginal
eﬀects are directly available (e.g., Blankenship et al. (2003), Demidenko (2013, Chap. 6)).
The marginal expectation for a nonlinear mixed-eﬀects model is calculated as follows:
E {f(xij, βi)} =
Z
· · ·
Z
f{xij, (βi1 + b1, . . . , βip + bp)} Φ(b1, . . . , bp, G) db1 · · · dbp
where Φ() denotes the density function of a p-dimensional normal distribution with mean vector 0 and
variance-covariance matrix G. Note that diﬀerent nonlinear mixed-eﬀects models will lead to slightly
diﬀerent deﬁnitions of population-average eﬀects. Speciﬁcally, this implies that derived marginal eﬀects
are aﬀected by the distributional assumptions made for the random eﬀects.
3


## Page 4


Through a change of variables the original random eﬀects may be transformed into a vector of indepen-
dent and identically distributed random eﬀects: bi = Ωui where G = ΩΩT is based on the Cholesky
decomposition and ui ∼N(0, Ip×p). We may then approximate the integral by the weighted sum:
E {f(xij, βi)} ≈
N
X
n=1
wnf{xij, (βi1 + ξ1n, . . . , βip + ξpn)},
with
wn =
p
Y
r=1
wrn,
(3)
using numerical Gauss-Hermite quadrature assuming a p × N matrix of nodes Ψ and corresponding
weights wrn, based on independent standard normal distribution functions (Smyth, 1998). The quadra-
ture nodes are transformed by ξ = ΨT bΩto reﬂect the scales and covariances of the random eﬀects. The
approximation to the integral can be thought of as an average of the individual curves, but instead of
considering a simple mean involving the predicted random eﬀects (the so-called EBLUPs), the average is
based on the estimated multivariate normal distribution of the random eﬀects. Standard errors of derived
parameter estimates are obtained by applying the delta method to Eq. (3) (van der Vaart, 1998, Chap.
5) using a numerically calculated gradient and extending the results by Gerhard et al. (2014).
3.1
Dose-response models
We will focus on the model functions f in Eq. (1) used for the analysis of dose-response data. A number
of diﬀerent model functions have been proposed in the literature; a short overview and references can
be found in Ritz (2010). However, in practice only a few functions appear to be used routinely. Among
these models the sigmoidal log-logistic model function is by far the one used the most. We deﬁne the
ﬁve-parameter log-logistic model function as follows:
f(x, β) = β2 +
β3 −β2
(1 + exp[β1{log(x) −log(β4)}])β5
(4)
The commonly used four-parameter version is obtained by setting β5 = 1; this model is routinely applied
in biology, toxicology and weed science (e.g., Price et al. (2012)). One reason for the popularity of this
model is the fact that the model parameters have direct biological interpretations: The parameters β2 and
β3 denote the lower and upper horizontal asymptotes that conﬁne the sigmoidal regression curve. The
parameter β4 denotes the dose resulting in a halfway reduction between the limits β2 and β3 (which corre-
sponds to the ED50 in mixed-eﬀects dose-response models, which are symmetrical increasing/decreasing
around an inﬂection point, but might be inﬂuenced by parameters for asymmetry or hormesis). The pa-
rameter β1 indicates the steepness of the curve in its transition between the two horizontal asymptotes.
The ﬁfth parameter β5 is an asymmetry parameter leading to asymmetry in one or the other tail for
β5 < 1 and β5 > 1, respectively.
Many a time not only the model parameters explicitly included in the model equation are of interest, but
also some derived parameters, like the eﬀective dose resulting in a 100α% (0 < α < 1) reduction relative
to the lower and upper limits (i.e., ED100α) or the ratio of two such eﬀective doses (often referred to as
the relative potency). Inference for derived parameters may be based on using the delta method, which
results in an estimated approximate (asymptotically-based) variance-covariance matrix of the derived
parameters.
For a given ﬁxed eﬀects parameter conﬁguration A0β (e.g., a speciﬁc treatment) the eﬀective dose ED100α
is deﬁned as the solution to the following inverse regression problem:
˜f(ED100α, A0β) = α ˜f(∞, A0β) + (1 −α) ˜f(0, A0β)
which may be re-arranged into:
α =
˜f(ED100α, A0β) −˜f(0, A0β)
˜f(∞, A0β) −˜f(0, A0β)
(5)
By deﬁnition ED100α values are relative quantities that are deﬁned relative to the lower and upper
limits β2 and β3 in Eq. (4), which corresponds to ˜f(0, A0β) and ˜f(∞, A0β), respectively. Instead of the
population-level eﬀective dose, a conditional ED100α may also be calculated from the inverse regression of
f(ED100α, A0β+b0), that is conditioning on a given known random eﬀects vector b0, which is often taken
4


## Page 5


to be 0. However, both types of eﬀective doses may be derived using the same nonlinear mixed-eﬀects
model.
A related approach used for summarizing dose-response data is the benchmark dose methodology (Piegorsch,
2010). Ritz et al. (2013) proposed an operational deﬁnition of the benchmark dose for continuous end-
points, allowing for the incorporation of an a priori speciﬁed background level p0 and risk level (benchmark
response: BMR). This deﬁnition allows benchmark doses to be estimated as certain eﬀective doses.
3.2
Software implementation
Our approach is implemented in R (R Core Team, 2014). Speciﬁcally, we developed the extension package
medrc, which combines the dose-response modelling framework of the package drc, which allows nonlinear
least-squares estimation for one or more dose-response curves through a convenient infrastructure for
model speciﬁcation and automatic calculation of suitable starting values (Ritz and Streibig, 2005), with
nonlinear mixed-eﬀects estimation using the package nlme (Pinheiro and Bates, 2000).
This framework oﬀers several key features such as having a set of predeﬁned dose-response functions
directly available, providing a uniﬁed parametrisation (b: steepness, c,d: lower and upper asymptotes, e:
inﬂection point location) and an easy-to-use formula interface for specifying the dose-response relationship
and for parametrisation of modelling multiple curves and random eﬀects.
The package medrc is available on GitHub under
https://github.com/daniel-gerhard/medrc.git. An accompanying vignette shows the full function-
ality of the package through additional examples.
4
Simulation Study
The accuracy of the proposed marginalization approach was investigated through simulations and com-
parisons to the marginal estimates obtained by ﬁtting a generalized nonlinear least squares (GNLS)
model assuming a compound-symmetry structure and an ordinary nonlinear least-squares regression
(NLS) model, which entirely ignores the between-cluster variability. Both these marginal models provide
parameter estimates that can be directly interpreted as population parameters, but the information about
cluster eﬀects is lost, i.e., the information is not quantiﬁed and therefore not incorporated as a separate
contribution in the estimated standard errors, if appropriate. We also compared the marginalized es-
timates to the conditional estimates obtained directly from the nonlinear mixed eﬀects model ﬁts. As
the conditional parameters have a diﬀerent interpretation and the marginal parameters are even derived
from diﬀerent models, it is not expected that these approaches will result in estimates for the marginal-
ized parameter. But it might be possible to characterise the performance of the marginalized estimates
relative to these alternatives.
The simulation scenario was similar to the ﬁrst case study introduced in the next section: We simulated
from a three-parameter log-logistic model with a random intercept on each of the three parameters and
a dose range from 0.01 to 3 with 10 equally spaced dose levels on the log-scale. The number of clusters
was varied from 2 to 20 to evaluate the precision of the derived parameter estimates as the standard
deviations of the random eﬀects become more precisely determined. The speciﬁc conﬁguration of ﬁxed
eﬀects parameters and standard deviations is shown in Table 1. Note the very diﬀerent magnitudes of
the variation on the three model scales. In order to investigate the inﬂuence of diﬀerent covariance struc-
tures of the random eﬀects and corresponding model misspeciﬁcation, either a diagonal or unstructured
covariance matrix was assumed for the true and modelled dependence structure.
Table 1: Parameter settings in the simulation study.
Fixed
Random eﬀects
Correlation of random eﬀects
Parameter
eﬀect
Std. Dev.
Unstructured
Diagonal
Steepness (β1)
5
0.5
1
-0.9
0.8
1
0
0
Upper asymptote (β2)
2000
500
-0.9
1
-0.5
0
1
0
ED50 (β4)
0.5
0.1
0.8
-0.5
1
0
0
1
Residuals (ϵij)
100
5


## Page 6


The ‘true’ marginal eﬀective dose parameters were obtained by Monte Carlo integration with 100,000
sampling steps for each parameter settings; this means sampling directly from a multivariate normal
distribution conditioning on the pre-deﬁned, true covariance of the random eﬀects. The accuracy of the
eﬀective doses was evaluated by the median deviation of the estimated parameter relative to the true
marginal parameter as shown in Figure 1. This ‘bias’ has to be cautiously interpreted for the conditional
and marginal approaches, as it shows the deviation to the true marginalized eﬀective dose, which of
course has a diﬀerent interpretation.
The marginalized estimates had the smallest deviation to the ‘true’ eﬀective dose in every scenario with
a correctly speciﬁed correlation structure. The conditional estimate instead remained constant regardless
of the number of clusters. Only when the model was misspeciﬁed, assuming a diagonal instead of a true
unstructured covariance matrix of the random eﬀects, the marginalized estimates showed an increased
deviation even at a large number of clusters, but nevertheless this deviation is still in a similar range as
for the marginal estimates.
By increasing the standard deviation of the random eﬀects associated with the parameter ED50 tenfold,
the diﬀerences between conditional and marginalized estimated eﬀective doses increased, resulting in an
increasing diﬀerence for the conditional estimates (results are shown as Supporting Information). The
diﬀerences for the conditional and marginalized estimates were always going in the same direction. For
ED50 and even more so for ED10 the conditional estimates showed a positive diﬀerence whereas there
was a negative diﬀerence for ED90; this ﬁnding is a result of assuming that random eﬀects are associated
with the upper asymptote but not with the lower asymptote, which was ﬁxed at 0.
It is worth noting that overall the two marginal approaches yielded very similar results even though
they involved diﬀerent assumptions about the correlation structure.
By generating the data given a
diagonal random eﬀects structure smaller deviation was observed, as it can be better approximated by
the compound symmetry assumption on the residuals than the unstructured covariance. Moreover, for
ED10 and ED50 the marginal estimates behaved like the marginalized estimates, but for ED90 they
resulted in a deviation in the opposite direction from the conditional and marginalized estimates.
Marginalized Model: Diagonal
True: Diagonal
Marginalized Model: Diagonal
True: Unstructured
Marginalized Model: Unstructured
True: Diagonal
Marginalized Model: Unstructured
True: Unstructured
−0.050
−0.025
0.000
0.025
0.050
−0.050
−0.025
0.000
0.025
0.050
−0.050
−0.025
0.000
0.025
0.050
ED10
ED50
ED90
5
10
15
20
25
5
10
15
20
25
5
10
15
20
25
5
10
15
20
25
Number of clusters
Median difference to the true marginalized ED
ED estimate
Marginalized
Cluster−specific
GNLS
NLS
Figure 1: Simulation result: Median of estimated diﬀerences to the true marginalized eﬀective dose
for marginalized, conditional, GNLS, and NLS estimates of ED10, ED50, and ED90 (rows) using either
an unstructured or diagonal variance-covariance matrix for the true and/or modelled random eﬀects
(columns). The true parameter corresponds to the dashed horizontal line at 0.
Figure 2 shows the medians of the estimated standard errors of the eﬀective dose estimates from the
simulation study. The standard errors of the marginalized estimates are comparable to the ones of the
6


## Page 7


conditional estimates. The dependence of the marginal estimates on the diﬀerent scales of the random
eﬀects is apparent: In comparison to the proposed marginalization approach the two marginal models,
which showed very similar behaviour, resulted in estimated standard errors for the estimated ED50 that
were somewhat smaller, but became larger with increasing distance from the inﬂection point. For the
estimated ED90 (near the lower asymptote that was ﬁxed at zero) the marginal estimates had standard
errors that were larger by a factor 1.5–2, indicating the inability of the marginal models to borrow strength
across diﬀerent model scales.
ED10
ED50
ED90
0.025
0.050
0.075
0.100
5
10
15
20
25
5
10
15
20
25
5
10
15
20
25
Number of clusters
Median of the effective dose standard errors
ED estimate
Marginalized
Cluster−specific
GNLS
NLS
Figure 2: Simulation result: Median of estimated standard errors for marginalized, conditional, GNLS,
and NLS estimates of ED10, ED50, and ED90. An unstructured variance-covariance matrix of the random
eﬀects was used for data generation and modelling.
5
Case Studies
The following case studies were analysed throughout using the R packages drc and medrc as previously
described. Source code to reproduce the results is available in the documentation of the package medrc
(see Section 3.2).
5.1
An example with between-assay variation
Nellemann et al. (2003) carried out experiments to assess the in vitro eﬀects of the fungicide vinclozolin.
The data were obtained using an androgen receptor reporter gene assay, which was repeated six times
(on diﬀerent days). Each assay resulted in concentration-response data with nine concentrations (in µM)
of the fungicide, and the response measured was chemiluminescence (in luminescence units). The same
nine concentrations were used in all six assays. However, in one assay results were only obtained for eight
concentrations.
A plausible biological assumption was that no signal would be observed for very high fungicide concen-
trations, indicating that a three-parameter log-logistic model with a lower asymptote at 0 ((Eq. (4) with
β2 = 0 and β5 = 1)) would be a realistic model for the data. Assay-speciﬁc random eﬀects on each of
the three model parameters, but not on the ﬁxed lower asymptote. This model allowed summarizing the
between-assay variation in terms of a 3 × 3 variance-covariance matrix.
A marginal generalized nonlinear least-squares model (GNLS) is used for comparison. Instead of a full
random eﬀects representation of the between-assay variability on the scales of the ﬁxed eﬀects parameters,
a compound-symmetry structure is assumed for the within-assay residuals.
The ﬁtted dose-response curves for the conditional, marginal, and marginalized approaches are shown in
Figure 3 along with the individual assay-speciﬁc ﬁtted curves (inserting estimated random eﬀects). In
this case they agreed quite well for high concentration but the marginalized ﬁt is below the conditional ﬁt
7


## Page 8


G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
1000
2000
0.01
0.025
0.05
0.1
0.25
0.5
1
2
3
Concentration [µM]
Chemiluminescence
Fitted curves
Conditional
Marginalized
GNLS
Assay−specific
Figure 3: Chemiluminescence observations together with conditional, marginalized, and assay-speciﬁc
ﬁtted curves based on a nonlinear mixed-eﬀects regression model assuming a three-parameter log-logistic
regression relationship. The corresponding marginal prediction based on GNLS is also shown.
and slightly below the marginal ﬁt for low concentrations where the response is more variable. Estimated
eﬀective doses are shown in Table 2. For large concentrations (> ED50) the standard errors were smaller
for the marginalized approach than for the marginal and only slightly larger than for the conditional
approach, indicating that the gain in precision achieved using a nonlinear mixed-eﬀects model is retained
through marginalization. For the highest ED levels the standard errors in the marginal approach were
twice as large compared to the conditional and marginalized approaches. This is presumably the result
of modelling the within-assay correlation on the scale of the residuals, independent of the diﬀerence in
scales of the two asymptotes.
Table 2: Eﬀective dose estimates for the vinclozolin study obtained from conditional, marginal (GNLS),
and marginalized models.
Conditional
Marginalized
Marginal (GNLS)
ED
Estimate
Std.Error
Estimate
Std.Error
Estimate
Std.Error
10
0.002
0.001
0.001
0.001
0.001
0.001
25
0.013
0.007
0.010
0.007
0.009
0.004
50
0.101
0.031
0.097
0.039
0.075
0.028
75
0.781
0.141
0.834
0.196
0.655
0.393
90
6.012
1.949
7.638
2.666
5.710
5.394
5.2
An example with between-assay variation and diﬀerent treatments
Streibig and Dayan (1999) investigated the inhibition of photosynthesis in response to two synthetic
photosystem II inhibitors, the herbicides diuron and bentazon. In an experiment, the eﬀect of oxygen
consumption of thylakoid membranes (chloroplasts) from spinach was measured after incubation with
the synthetic inhibitors. Five assays, three treated with bentazon and two with diuron, were used. For
each assay six increasing herbicide concentrations were applied together with a negative control, using
diﬀerent dose ranges on a logarithmic scale for the two treatments to encompass the whole dose-response
range based on preliminary experiments.
For the comparison of the two herbicides, dose-response curves were ﬁtted assuming a four-parameter
log-logistic model with a separate set of ﬁxed eﬀects coeﬃcients for each of the two treatments (in total 8
model parameters). Random eﬀects were included for each of the four parameters to model the between-
assay variability in the diﬀerent model scales. Using the information about the between-assay variability
is especially advantageous as the dose levels for the two herbicides did not cover the same dose range.
The two ﬁxed eﬀect curves were compared by means of relative potencies based on ED10, ED20, ED50,
ED75, ED90 estimates.
8


## Page 9


Again, a generalized nonlinear least-squares model (GNLS) is used for comparison, assuming a compound-
symmetry structure of the residuals to reﬂect the within-assay correlation.
G
G
G
G
G
G
G
G
GGG
G
G
G
GG
GG
G
GG
G
G
G
G
GG
GG
G
GG
GGG
GGG
G
GG
GG
G
G
GG
GGG
GGG
G
GG
G
GG
0.5
1.0
1.5
2.0
0.01
0.025 0.05
0.1
0.25
0.5
1
2.5
5
10
25
100
Concentration [µM]
Oxygen consumption of thylakoid membranes
Herbicide
G bentazon
diuron
Fitted curves
Marginalized
GNLS
Assay−specific
Figure 4: Observations of oxygen consumption and conditional, marginalized, and assay-speciﬁc ﬁtted
curves based on a nonlinear mixed-eﬀects regression model assuming a four-parameter log-logistic regres-
sion relationship for each treatment group. The corresponding marginal prediction based on GNLS is
also shown. For the herbicide treatments their corresponding assay-speciﬁc curves are shown, predicting
a response at each assay level.
The ﬁtted mean dose-response curves, derived using the marginal (GNLS) and marginalized approaches,
as well as the assay-speciﬁc ﬁtted curves are shown in Figure 4. We can conclude that the marginalized
approach recovers the marginal mean curve very accurately in this case as the ﬁtted mean curves are all
very similar. The estimated relative potencies are shown in Table 3. The conditional and marginalized
estimates were identical and this may be explained by the fact that the between-assay standard deviation
for the slope and ED50 parameters (β1 and β4) eﬀectively were equal to 0; with random eﬀects only on
the scales on the asymptotes of a four-parameter log-logistic model, the ﬁxed eﬀects can be interpreted
as marginal eﬀects. For the marginal model the estimated within-assay correlation coeﬃcient for the
compound symmetry structure was 0.55, but it is not speciﬁc to the diﬀerent scales of the two asymptotes.
Therefore, the conﬁdence intervals were narrower for small ED values and wider for the high ED values.
Table 3: Estimated eﬀective doses and corresponding relative potencies for the spinach data example.
Eﬀective Dose
Relative
Conﬁdence limits
Model
ED
Bentazon
Diuron
potency
Lower
Upper
10
0.038
0.058
0.652
0.280
1.056
25
0.232
0.108
2.144
1.420
2.911
Conditional
50
1.433
0.203
7.056
5.217
8.980
75
8.832
0.380
23.220
13.112
33.940
90
54.437
0.712
76.415
23.776
133.970
10
0.038
0.058
0.651
0.278
1.058
25
0.232
0.108
2.144
1.421
2.911
Marginalized
50
1.433
0.203
7.056
5.216
8.980
75
8.832
0.380
23.220
13.112
33.940
90
54.437
0.712
76.415
23.776
133.969
10
0.030
0.058
0.513
-0.147
1.278
25
0.207
0.108
1.909
0.584
3.382
Marginal
50
1.445
0.203
7.110
2.385
12.157
75
10.076
0.381
26.478
-6.314
61.692
90
70.286
0.713
98.601
-95.172
318.229
9


## Page 10


6
Discussion
We have proposed a novel and ﬂexible marginalization approach for obtaining marginal estimates from
nonlinear mixed-eﬀects models that are routinely used in toxicology and biological science applications.
The approach combines the best of two worlds: interpretable population-level estimates obtained using
models that allow to borrow strength across observations.
For all of the two case studies, the population average interpretation is useful, looking at a representative
sample of subjects characterizing the population of possible subject eﬀects. Basing the interpretation of
a dose eﬀect on a single subject will not be easy to generalise for a range of other future samples from
the subject population; this is diﬀerent for e.g. medical applications where the beneﬁt of a single patient
might be of foremost interest instead of a general population eﬀect.
We speciﬁcally focused on nonlinear mixed-eﬀects dose-response models although the proposed methodol-
ogy is also applicable to other types of nonlinear mixed-eﬀects regression models with normally distributed
random eﬀects.
As an alternative to the Gauss-Hermite quadrature, Monte Carlo integration could be used, sampling
directly from a multivariate normal distribution conditioning on the estimated covariance of the random
eﬀects. But as it is a computationally very demanding approach we do not at present recommend it for
routine analyses.
A limitation of the marginalization approach is the conditioning on estimated standard deviations of the
random eﬀects. This means we ignore the uncertainty involved in using estimated variance components,
potentially leading to underestimation of the uncertainty of our parameter estimates of interest with
consequences for derived p-values and conﬁdence intervals.
References
Blankenship, E. E., Stroup, W. W., Evans, S. P., and Knezevic, S. Z. (2003). Statistical inference for
calibration points in nonlinear mixed eﬀects models. Journal of Agricultural, Biological, and Environ-
mental Statistics 8, 455–468.
Clayton, C. A., Starr, T. B., Sielken, R. L., Williams, R. L., Pontal, P.-G., and Tobia, A. J. (2003). Using
a nonlinear mixed eﬀects model to characterize cholinesterase activity in rats exposed to Aldicarb.
Journal of Agricultural, Biological, and Environmental Statistics 8, 420–437.
Davidian, M. and Giltinan, D. M. (1995). Nonlinear Models for Repeated Measurement Data. London:
Chapman & Hall/CRC Monographs on Statistics & Applied Probability.
Davidian, M. and Giltinan, D. M. (2003). Nonlinear models for repeated measurement data: An overview
and update. Journal of Agricultural, Biological, and Environmental Statistics 8, 387–419.
Demidenko, E. (2013).
Mixed Models: Theory and Applications in R.
Mathematics. Hoboken, New
Jersey: John Wiley & Sons, Inc.
Fitzmaurice, G. M., Laird, N. M., and Ware, J. H. (2012). Applied Longitudinal Analysis. Hoboken, New
Jersey: John Wiley & Sons, Inc.
Gbur, E. E., Stroup, W. W., McCarter, K. S., Durham, S., Young, L. J., Christman, M., West, M.,
and Kramer, M. (2012). Analysis of Generalized Linear Mixed Models in the Agricultural and Natural
Resources Sciences. American Society of Agronomy and Soil Science of America and Crop Science
Society of America.
Gerhard, D., Bremer, M., and Ritz, C. (2014). Estimating marginal properties of quantitative real-time
PCR data using nonlinear mixed models. Biometrics 70, 247–254.
Griswold, M. E., Swihart, B. J., Caﬀo, B. S., and Zeger, S. L. (2013). Practical Marginalized Multilevel
Models. Stat 2,.
Heagerty, P. J. and Zeger, S. L. (2000). Marginalized Multilevel Models and Likelihood Inference. Sta-
tistical Science 15, 1–26.
10


## Page 11


Lee, Y. and Nelder, J. A. (2004). Conditional and Marginal Models: Another View. Statistical Science
19, 219–238.
Liang, K.-Y. and Zeger, S. L. (1986). Longitudinal Data Analysis Using Generalized Linear Models.
Biometrika 73, 13.
Makowski, D. and Lavielle, M. (2006). Using SAEM to estimate parameters of models of response to
applied fertilizer. Journal of Agricultural, Biological, and Environmental Statistics 11, 45–60.
McCulloch, C. E., Searle, S. R., and Neuhaus, J. M. (2008). Generalized, Linear, and Mixed Models.
London: John Wiley & Sons, 2nd edition.
Nellemann, C., Majken, D., Lam, H. R., and Vinggaard, A. M. (2003). The Combined Eﬀects of Vinclo-
zolin and Procymidone Do Not Deviate from Expected Additivity in Vitro and in Vivo. Toxicological
Sciences 71, 251–262.
Parzen, M., Ghosh, S., Lipsitz, S., Sinha, D., Fitzmaurice, G. M., Mallick, B. K., and Ibrahim, J. G.
(2011).
A generalized linear mixed model for longitudinal binary data with a marginal logit link
function. The Annals of Applied Statistics 5, 449–467.
Piegorsch, W. W. (2010). Translational benchmark risk analysis. Journal of Risk Research 13, 653–667.
Pinheiro, J. C. and Bates, D. M. (2000). Mixed-Eﬀects Models in S and S-Plus. Statistics and Computing.
New York: Springer.
Price, W. J., Shaﬁi, B., and Seefeldt, S. S. (2012). Estimation of Dose-Response Models for Discrete and
Continuous Data in Weed Science. Weed Technology 26, 587–601.
R Core Team (2014). R: A Language and Environment for Statistical Computing. R Foundation for
Statistical Computing, Vienna, Austria.
Ritz, C. (2010). Toward a uniﬁed approach to dose-response modeling in ecotoxicology. Environmental
Toxicology and Chemistry 29, 220–229.
Ritz, C., Gerhard, D., and Hothorn, L. A. (2013). A Uniﬁed Framework for Benchmark Dose Estimation
Applied to Mixed Models and Model Averaging. Statistics in Biopharmaceutical Research 5, 79–90.
Ritz, C. and Streibig, J. C. (2005). Bioassay analysis using R. Journal of Statistical Software 12, 1–22.
Serroyen, J., Molenberghs, G., Verbeke, G., and Davidian, M. (2009). Nonlinear Models for Longitudinal
Data. The American Statistician 63, 378–388.
Serroyen, J., Molenberghs, G., Verhoye, M., Meir, V., and Linden, A. (2005). Dynamic manganese-
enhanced MRI signal intensity processing based on nonlinear mixed modeling to study changes in
neuronal activity. Journal of Agricultural, Biological, and Environmental Statistics 10, 170–183.
Smyth, G. K. (1998). Numerical integration. In Armitage, P. and Colton, T., editors, Encyclopedia of
Biostatistics, pages 3088–3095. London: Wiley.
Streibig, J. C. and Dayan, F. E. (1999). Joint action of natural and synthetic photosystem II inhibitors.
Pesticide Science 146, 137–146.
Stroup, W. W. (2014). Rethinking the Analysis of Non-Normal Data in Plant and Soil Science. Agronomy
Journal 106, 1–17.
van der Vaart, A. W. (1998). Asymptotic Statistics. Cambridge: Cambridge University Press.
Vonesh, E. F. (2012). Generalized Linear and Nonlinear Models for Correlated Data: Theory and Appli-
cations Using SAS. Cary, NC, USA: SAS Institute Inc.
Wang, Z. and Louis, T. A. (2004). Marginalized binary mixed-eﬀects models with covariate-dependent
random eﬀects and likelihood inference. Biometrics 60, 884–891.
Weimer, M., Jiang, X., Ponta, O., Stanzel, S., Freyberger, A., and Kopp-Schneider, A. (2012). The
impact of data transformations on concentration-response modeling. Toxicology Letters 213, 292–298.
11

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1707_02502v1_marginalization_in_nonlinear_mixed_effects_models_with_an_application_to_dose_re
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1707_02502V1_MARGINALIZATION_IN_NONLINEAR_MIXED_EFFECTS_MODELS_WITH_AN_APPLICATION_TO_DOSE_RE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

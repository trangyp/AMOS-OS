---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.02597v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1707.02597v1_Parameter_uncertainty_in_structural_equation_models__Confidence_sets_and_fungibl

> Source: 1707.02597v1_Parameter_uncertainty_in_structural_equation_models__Confidence_sets_and_fungibl.pdf

> Pages: 39

---


## Page 1


Running head: CONFIDENCE SETS AND FUNGIBLE ESTIMATES
1
This version may have minor deviations from the ﬁnal published version on Psychological
Methods.
Parameter uncertainty in structural equation models:
Conﬁdence sets and fungible estimates
Jolynn Pek
The Ohio State University
Hao Wu
Boston College
Jolynn Pek, Department of Psychology, The Ohio State University; Hao Wu, Department of Psy-
chology, Boston College
Author note: Both authors contributed equally to this work and correspondence concerning
this article should be addressed to Jolynn Pek, Department of Psychology, The Ohio State Uni-
versity, 1835 Neil Avenue, Columbus, OH 43210-1222. E-mail: pek.5@osu.edu. The writing and
reﬁnement of this work was supported by the Natural Sciences and Engineering Research Council
of Canada (NSERC) Discovery Grant RGPIN-04301-2014 and the Ontario Ministry of Research
and Innovation Early Researcher Award ER15-11-004 awarded to Jolynn Pek.
arXiv:1707.02597v1  [stat.ME]  9 Jul 2017


## Page 2


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
2
Abstract
Current concerns regarding the dependability of psychological ﬁndings call for methodolog-
ical developments to provide additional evidence in support of scientiﬁc conclusions. This pa-
per highlights the value and importance of two distinct kinds of parameter uncertainty which are
quantiﬁed by conﬁdence sets (CSs) and fungible parameter estimates (FPEs; T. Lee, MacCallum,
& Browne, in press); both provide essential information regarding the defensibility of scientiﬁc
ﬁndings. Using the structural equation model, we introduce a general perturbation framework
based on the likelihood function that uniﬁes CSs and FPEs and sheds new light on the concep-
tual distinctions between them. A targeted illustration is then presented to demonstrate the factors
which differentially inﬂuence CSs and FPEs, further highlighting their theoretical differences.
With three empirical examples on initiating a conversation with a stranger (Bagozzi & Warshaw,
1988), posttraumatic growth of caregivers in the context of pediatric palliative care (Cadell et al.,
2014), and the direct and indirect effects of spirituality on thriving among youth (Dowling et al.,
2004), we illustrate how CSs and FPEs provide unique information which lead to better informed
scientiﬁc conclusions. Finally, we discuss the importance of considering information afforded by
CSs and FPEs in strengthening the basis of interpreting statistical results in substantive research,
conclude with future research directions, and provide example OpenMx code for the computation
of CSs and FPEs.
Keywords: conﬁdence sets, fungible estimates, sensitivity analysis, proﬁle likelihood, struc-
tural equation modeling


## Page 3


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
3
Parameter uncertainty in structural equation models:
Conﬁdence sets and fungible estimates
Statistical practice in psychological science is undergoing reform in response to concerns over
the dependability of ﬁndings (Harlow, Mulaik, & Steiger, 2016; Open Science Collaboration,
2015; Pashler & Wagenmakers, 2012; Simmons, Nelson, & Simonsohn, 2011; Sijtsma, 2015).
In response to these concerns, the reporting of effect sizes or focal parameter estimates and their
conﬁdence intervals (CIs) have been recommended as best practice (Cumming, 2014; Wilkinson
& the Task Force on Statistical Inference, 1999). Conﬁdence intervals communicate precision in
estimation, providing information to researchers on whether inferences about their commensu-
rate parameters can be drawn. Note that conﬁdence regions (CRs) are an extension of CIs from
a single parameter to a set of multiple parameters, and we use the term conﬁdence sets (CSs) to
collectively refer to CIs and CRs. Additionally, recent quantitative developments show that exam-
ining parameter sensitivity (T. Lee & MacCallum, 2015) and fungible parameter estimates (FPEs;
T. Lee et al., in press; MacCallum, Browne, & Lee, 2009; Waller, 2008) can add to substantive
researchers’ diagnostic toolkit in terms of generating more information about the validity of their
statistical results. Relative to CSs, FPEs are unfamiliar to substantive researchers; and although
CSs and FPEs are different types of parameter uncertainty, little is known about FPEs in relation
to CSs and how FPEs can be computed in practice.
This paper has several aims. First, we provide a nontechnical overview of FPEs, their inter-
pretation, and guidance regarding their computation. To better understand FPEs, this overview
introduces an alternative perturbation to deﬁne FPEs (cf., T. Lee et al., in press; MacCallum, Lee,
& Browne, 2013; MacCallum et al., 2009). Second, we emphasize the value in quantifying pa-
rameter uncertainty with the construction and computation of CSs and FPEs for drawing strong
conclusions in substantive research. Third, we clarify the relationship between CSs and FPEs, and
emphasize the distinct information each type of parameter uncertainty quantiﬁes in SEM. Fourth,
we provide example OpenMx code to construct CSs and FPEs in practice.
In SEM, parameter estimates are typically interpreted when a model is considered to ﬁt the
data well. The ﬁt of a model is related to the amount of model error (Browne & Cudeck, 1993;
MacCallum, 2003; Wu & Browne, 2015a, 2015b) addressed by estimates of model ﬁt indices
such as the root mean square error of approximation (RMSEA, denoted as ε; Steiger, 2016; Browne
& Cudeck, 1993), the Comparative Fit Index (CFI; Bentler, 1990), and the Tucker-Lewis index
(TLI; Tucker & Lewis, 1973). All of these indicators of model ﬁt stem from the estimated model
discrepancy, ˆF . Note that the term model ﬁt here represents a quantiﬁcation of how distant the
speciﬁed model, which is a collection of distributions indexed by parameters, is from the sample
or population. It is usually taken to be the smallest discrepancy between the given sample or pop-
ulation and the model, and the set of parameter values which indexes the member of the model
which gives this smallest discrepancy is considered the best estimates. Given good model ﬁt
where the model serves as a good representation of the sample, CSs should then be constructed so
as to quantify sampling variability or estimate precision about the population parameters. Tighter
CSs imply less sampling variability, higher estimate precision, and a stronger tendency to con-
clude statistical signiﬁcance. Finally, as part of model diagnostics, the inﬂuence of parameters in
relation to the model’s ﬁt to data should be considered so that valid conclusions about parameter
estimates can be made with conﬁdence (Green, 1977). Fungible parameter estimates (FPEs) quan-
tify parameter inﬂuence on the model’s ﬁt to the data in terms of variability in the values param-


## Page 4


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
4
eters can take within the small neighborhood of the optimal estimate. These FPEs are associated
with the same speciﬁed model and serve as alternative parameter values which describe the data
just slightly worse than the unique set of optimal parameter estimates which achieves the best ﬁt.
Tighter sets of FPEs indicate less variability or robustness in the speciﬁed model’s description of
the data afforded by the alternative parameter estimates, providing a stronger basis for the validity
of the optimal parameter estimates. Conﬁdence sets and the set of FPEs are important and distinct
expressions of parameter uncertainty to be quantiﬁed and evaluated when strong scientiﬁc conclu-
sions are sought (e.g., see Pek, Chalmers, & Monette, 2016 for developments in multiple linear
regression).
We begin by reviewing the SEM to establish notation, emphasizing maximum likelihood
(ML) estimation. Next, we review proﬁle likelihood CSs and FPEs and introduce a general frame-
work based on the likelihood function that uniﬁes CSs and FPEs in SEM as different aspects of
parameter uncertainty, and showing how likelihood-based CSs and FPEs are analytically related.
We then make use of a targeted illustration to demonstrate how different modeling factors inﬂu-
ence CSs and sets of FPEs, emphasizing the distinct information each quantiﬁcation of parameter
uncertainty carries. Next, we illustrate the application of CSs and FPEs with three real data ex-
amples on initiating a conversation with a stranger (Bagozzi & Warshaw, 1988), posttraumatric
growth in caregivers of children with life-limiting illnesses (Cadell et al., 2014), and the direct
and indirect effects of spirituality on thriving among youth (Dowling et al., 2004). Finally, we
discuss the importance of considering CSs and FPEs in interpreting results obtained from the ap-
plication of SEM, and conclude with future research directions.
The Structural Equation Model
Structural equation models are multi-parameter models where a system of linear equations
among sets of measured and latent variables (MVs and LVs) are speciﬁed. The p × p population
covariance matrix of the MVs is denoted by Σ, and the model impled k × 1 vector of parameters
is denoted by θ. The SEM is expressed as Σ = Σ(θ), implying that the population covariance
matrix for the MVs is a function of the model parameters. Parameter estimates ˆθ are computed
by minimizing the discrepancy between the model impled population matrix Σ(θ) and the sam-
ple covariance matrix S, which is expressed as a discrepancy function, F[Σ,S]. Observe that this
function relates parameter values to a quantiﬁcation of ﬁt to a given sample.
Many discrepancy functions for computing parameter estimates have been devised such as
generalized least squares (GLS) and asymptotic distribution free (ADF; Browne, 1984). The
method of maximum Wishart likelihood (MWL) continues to be the most popular approach, as-
suming that the p MVs follow a multivariate normal distribution. Minimizing the MWL discrep-
ancy function is equivalent to maximizing the likelihood function of the sample covariance matrix
S (see Bollen, 1989, p.134–135). The MWL discrepancy function is
F[Σ,S] = ln|S|+tr(SΣ−1)−ln|Σ|−p,
(1)
where p is the number of MVs and tr(·) denotes the trace of a square matrix.
The estimated sample discrepancy function is denoted as ˆF = F[Σ(ˆθ),S] and multiplying ˆF
by (N −1), where N is the sample size, obtains the goodness-of-ﬁt test statistic:
X2 = (N −1) ˆF.


## Page 5


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
5
This X2 test statistic asymptotically follows a χ2 distribution with p(p+1)/2−k degrees of free-
dom under the null hypothesis that the model implied covariance matrix Σ(θ) is exactly the same
as the population covariance matrix Σ, H0 : Σ = Σ(θ). This goodness-of-ﬁt test statistic, which
quantiﬁes a model’s ﬁt to the data, is also a likelihood ratio test (LRT) statistic because X2 is
twice the difference between two log-likelihoods (see Equation 1). Inverting a similar LRT statis-
tic which compares two nested models is one basis of quantifying parameter uncertainty from the
likelihood function.
Quantifying Parameter Uncertainty
Conﬁdence Sets
Recall that conﬁdence sets collectively refer to CIs for a single parameter and CRs for mul-
tiple parameters, and supplement point estimates by conveying their estimate precision and sam-
pling variability. Although CSs are estimated from sample data, they are devices for statistical
inference in that they are statements about unknown population parameters. Formally, a CS pro-
vides a range of plausible population values for the set of parameters θ, and (1−α)100% of such
CSs are expected to contain the vector of population parameters over repeated sampling. There
are several approaches to construct CSs and we focus on the proﬁle likelihood method.
Proﬁle likelihood conﬁdence intervals. Typically, SEMs have nuisance parameters which
are required to complete the model and are not of substantive interest (e.g., unique variances in
a factor analytic model). For simplicity, suppose that the vector of model parameters θ is parti-
tioned into two sets: a single focal parameter θ f , and a set of nuisance parameters θn. A proﬁle
likelihood CI for a kf = 1 focal parameter is constructed by inverting a LRT which tests the null
hypothesis H0 : θf = θ0 f , where θ0f is a scalar value of the population parameter deﬁned under
the null hypothesis. The LRT statistic is deﬁned as G2 = 2[l(ˆθ) −l(θ0f , ˜θn)], where l(ˆθ) is the
log-likelihood associated with the k × 1 vector of ML estimates ˆθ = (ˆθ f , ˆθn)′, and l(θ0f , ˜θn) is
the log-likelihood associated with the ML estimates (θ0f , ˜θn)′, where θ0f is held ﬁxed under the
null hypothesis. Note that the vector of estimates for the nuisance parameters ˆθn is distinct from
˜θn because ˆθn is estimated jointly with ˆθf whereas ˜θn is estimated while θf = θ0f is held ﬁxed.
Given the observed data, a proﬁle likelihood is an expression of values of G2 in relation to the fo-
cal parameter θ0f , where the nuisance parameters θn have been eliminated; θn is eliminated by
computing their ML estimates, ˜θn, for each ﬁxed value of θ0 f which relates to a G2 value.
Under the assumption of multivariate normality, this LRT statistic, G2, asymptotically follows
a χ2 distribution with kf = 1 degree of freedom. The proﬁle likelihood CI is an inversion of G2
because the CI is the set of values of θ0f that satisfy G2 ≤χ2
1,1−α. The right side of this inequal-
ity is the critical value based on the χ2 distribution where the ﬁrst subscript denotes the degrees
of freedom, and the second subscript (1 −α) denotes the conﬁdence level. The unique upper and
lower bounds of the CI are deﬁned when G2 = χ2
1,1−α. In practice, because the proﬁle likelihood
for θf is obtained numerically, due to the re-estimation of ˜θn for different ﬁxed values of θ0f , the
search for values of θ0f such that G2 = χ2
1,1−α is also a numerical one. A faster search algorithm,
which does not involve re-estimating ˜θn, was proposed by Wu and Neale (2012) and reviewed by
Pek and Wu (2015).
Proﬁle likelihood conﬁdence regions. Constructing a proﬁle likelihood CR for kf > 1 pa-
rameters is a direct extension of the kf = 1 case. The G2 LRT statistic is modiﬁed into a joint test


## Page 6


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
6
where the null hypothesis, H0 : θ f = θ0f , is an expression of vectors and
G2 = 2[l(ˆθ)−l(θ0f , ˜θn)].
(2)
Accordingly, a (1−α)100% CR for kf > 1 focal parameters is deﬁned as the set of values of θ0f
that satisfy the inequality
G2 ≤χ2
kf ,1−α.
(3)
Observe that the degrees of freedom associated with the critical value based on the χ2 distribution
are now kf (cf., Scheff´e, 1953). Similarly, boundary points to the CR are uniquely deﬁned when
G2 = χ2
kf ,1−α.
Computing proﬁle likelihood conﬁdence sets. In practice, computing a high dimensional CS
becomes computationally untenable as the number of dimensions in kf increase, and presenting
and interpreting such results become complex. Researchers have typically addressed the challenge
of high-dimensionality by focusing on a limited number of focal parameters (e.g., T. Lee et al.,
in press) or by computing kf simultaneous CIs which are one-dimensional projections of the CS
(e.g., Pek et al., 2016; Pek & Wu, 2015). We primarily focus on the method of a limited number
of focal parameters.
Fungible Parameter Estimates
Fungible parameter estimates provide diagnostic information about statistical results from the
broader framework of sensitivity analysis (Cook, 1986; S.-Y. Lee & Wang, 1996). Speciﬁcally,
FPEs inform of whether their commensurate parameter estimates should be validly interpreted.
In a sensitivity analysis, one introduces small perturbations to the data (e.g., deleting a case to
quantify case inﬂuence; Pek & MacCallum, 2011) or to the model (e.g., perturbing parameter esti-
mates to quantify parameter sensitivity; Cadigan, 1995; T. Lee & MacCallum, 2015) and examine
the effects of such perturbations on statistical results. The goal of sensitivity analysis is to deter-
mine the extent to which results are sensitive or robust to such small perturbations. Stability of
statistical results are sought under controlled perturbations to the data or model so as to establish
their validity. Conversely, observed instability of results under small introduced perturbations can
undermine conﬁdence in their deﬁnitive interpretation.
In a seminal paper, Green (1977) stated that parameters with large effects on the ﬁt of a sin-
gle speciﬁed model provide a strong basis for scientiﬁc conclusions. The rationale behind this
statement stems from the link between values a model’s parameters can assume (i.e., ˆθ) and their
implied ﬁt to the data (e.g., ˆF ). Parameters closely tied to model ﬁt play an essential role in de-
termining how well the model describes the data; their strong inﬂuence on the speciﬁed model’s
ﬁt to data serves to validate their rigorous interpretation. Conversely, parameters which do not ex-
ert inﬂuence on model ﬁt have little basis for interpretation because they are relatively uninvolved
with how well the model represents the data (T. Lee & MacCallum, 2015). This inﬂuence or sen-
sitivity of parameters can be determined from a sensitivity analysis where optimal focal parameter
estimates ˆθ f are perturbed to quantify their inﬂuence on model ﬁt (S.-Y. Lee & Wang, 1996); pa-
rameters which strongly inﬂuence model ﬁt are deemed sensitive whereas the converse holds for
insensitive parameters.
Fungible parameter estimates approach the issue of parameter sensitivity by perturbing model
ﬁt instead of optimal parameter estimates. Thus, given a slight and ﬁxed perturbation to a speci-
ﬁed model’s ﬁt to data, FPEs are alternative parameter estimates located within the small neigh-


## Page 7


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
7
borhood of the optimal estimate that yield the same level of perturbed model ﬁt. Stated differ-
ently, the FPE approach considers a discrepancy function value slightly greater than the mini-
mum and its associated parameter values; the suboptimal discrepancy function value is consid-
ered an alternative model ﬁt, and the commensurate parameter values (i.e., FPEs) are alternative
estimates. Tight sets of FPEs with limited variability reﬂect inﬂuential parameters. Conversely,
highly varying sets of FPEs reﬂect insensitive parameters. The key diagnostic information com-
municated by FPEs is the stability of the model’s description of the data afforded by the parame-
ter estimates ˆθ in relation to estimated model ﬁt. Here, stability or robustness enhances the valid-
ity of parameter estimates.
When a speciﬁed model is ﬁt to sample data, optimal parameter estimates ˆθ are obtained at
the minimum value of the discrepancy function, ˆF . Typically, model ﬁt is assessed by making a
judgment on the value of ˆF or some function thereof, and parameter estimates ˆθ are interpreted
when the model is deemed to ﬁt the data well. Fungible parameter estimates are regarded as al-
ternative estimates which yield the same value of suboptimal model ﬁt, ˆF∗; because this is a
type of sensitivity analysis, suboptimal model ﬁt is broadly deﬁned as slightly worse than opti-
mal model ﬁt where the difference between optimal and suboptimal ﬁt is of no substantive conse-
quence (T. Lee et al., in press). The variability of the set of FPEs from the ML estimate ˆθ quan-
tiﬁes the stability of the model’s description of the data, in terms of parameter estimates, under a
slight perturbation to model ﬁt. Wildly varying FPEs imply that parameter estimates can take on
very different values (cf., insensitive parameters) and consequently very different interpretations,
raising questions about their validity and reducing conﬁdence in drawing inferences about them.
Conversely, invariable FPEs (cf. sensitive parameters) suggest that parameter estimates are stable
and remain relatively consistent under a slight perturbation to model ﬁt, establishing their valid-
ity and strengthening conﬁdence in their rigorous interpretation.1 Note that the interpretation of
parameter estimates requires alignment with substantive theory and related conceptual and philo-
sophical issues (Bagozzi & Yi, 1988). To the extent that FPEs corroborate substantive theory and
concepts as alternative parameter estimates, they provide evidence on the stability of the model’s
description of the data.
Let ˆθ
∗denote the set of FPEs which are uniquely deﬁned when a slight perturbation is added
to the value of the estimated discrepancy function value ˆF , denoted as ˆF∗= ˆF + δFPE , where
δFPE is a non-random and ﬁxed value. Similar to the arbitrary choice of 1%, 5% or 10% signiﬁ-
cance levels, the magnitude of the perturbation δFPE to apply is subjective but should be consis-
tent with the notion that perturbations are necessarily small to the extent that suboptimal model ﬁt
is practically no different from the ﬁt of the optimal solution. We are reluctant to ascribe guide-
lines for recommended magnitudes of δFPE because the value of constructing sets of FPEs lies in
the extent of stability or uncertainty communicated by their variability associated with a range of
levels of perturbation. Indeed, the construction of FPEs is for the diagnostic purpose of ascertain-
1From the perspective of estimation where a function relating model ﬁt to parameter values is optimized (e.g.,
Equation 1), A set of FPEs contain alternative parameter values associated with a suboptimal solution. Suppose the
likelihood is to be optimized such that unique optimal parameter estimates are ML estimates. By perturbing the max-
imum likelihood value which is also a quantiﬁcation of model ﬁt (e.g., minus two the log-likelihood, −2LL), FPEs
are a ‘slice’ of the likelihood and communicate the extent of information present in the data about the parameters
(see Myung, 2003 for a tutorial on ML estimation). Highly varying FPEs communicate limited information whereas
invariant FPEs communicate high information, and more information augments the validity of the commensurate
parameter estimates.


## Page 8


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
8
ing whether parameters can be validly interpreted based on the extent of parameter sensitivity or
the stability of the parameter estimates under a slight perturbation to model ﬁt. In this vein, sev-
eral levels of perturbation are recommended for practice (T. Lee et al., in press). Here, we focus
on two types of perturbations with different properties: the ﬁrst is based on the RMSEA, and the
second is based on ˆF .
Extant research on FPEs forward that because a perturbation to model ﬁt is more interpretable
in the scale of the RMSEA compared to ˆF (T. Lee et al., in press; MacCallum et al., 2009), the
perturbation δFPE can be deﬁned in the metric of the RMSEA. The RMSEA is a measure of
discrepancy per degree of freedom and takes into account model complexity (Browne & Cud-
eck, 1992; Steiger, 2016). The population RMSEA is ε =
p
F0/d f , where F0 is the discrep-
ancy due to model error in the population and d f = p(p + 1)/2 −k is the model degrees of
freedom. The sample RMSEA, which corrects for the bias in ˆF as an estimator of F0, is ˆε =
q
max( ˆF
d f −
1
N−1,0) where max(·) is the maximum operator (Browne & Cudeck, 1992). The
range ˆε ≤0.05 is conventionally viewed as indicating a close ﬁt of the model to the data rela-
tive to the model degrees freedom. Note that when F0 is close to zero, and sample size is small, ˆε
is truncated at zero because the bias correction term
1
(N−1) could be larger than
ˆF
d f .
Let the perturbed value of RMSEA be ε∗= ˆε+ ˜ε, where ˜ε denotes the perturbation to the op-
timal RMSEA. Several levels of perturbation are recommended in a sensitivity analysis; previous
research has used ˜ε = .001 and .005 based on the rationale that such perturbations do not sub-
stantively change model ﬁt (e.g., see T. Lee et al., in press, MacCallum et al., 2013; cf. T. Lee &
MacCallum, 2015). For example, ˆε = .05, ˆε = .051, and ˆε = .055 suggest inconsequential differ-
ences in model ﬁt as operationalized by the RMSEA. The perturbed discrepancy function value is
then
ˆF∗= d f[(ˆε+ ˜ε)2 +
1
N −1],
(4)
when the estimated RMSEA ̸= 0. Although FPEs should theoretically reﬂect properties of the
model and be independent of sample size (cf., Waller, 2008), the perturbation based on the RM-
SEA in the scale of F , denoted as δε = ˆF∗−ˆF , is affected by sample size N because of the bias
correction. This dependence will be discussed later.2 Note that FPEs are formulated to provide
diagnostic information about the stability of a particular model’s parameter estimates, and the
property of invariance for the perturbation δFPE across samples and models is unimportant in this
context.
An alternative perturbation to deﬁne FPEs, which is explicitly free from sample size and d f ,
can be applied directly to the sample discrepancy function value ˆF . Speciﬁcally, a small percent-
age of ˆF can be used as a perturbation. Under this alternative scheme the perturbed discrepancy
function value is
ˆF∗= ˆF +δF,
(5)
where δF is some small percentage of ˆF . For instance, when the perturbation is deﬁned by 5% or
δF = .05 ˆF , ˆF∗= 1.05 ˆF . Unlike δε, δF is free of sample size (for the same observed covariance
2For a perturbation based on the RMSEA to be free of sample size, the RMSEA without the bias correction can be
perturbed instead. Note that Waller’s (2008) fungible weights in multiple linear regression are independent of sample
size because the perturbation is based on the unadjusted R2; if the bias adjusted R2 is perturbed, resulting fungible
weights will also be affected by sample size.


## Page 9


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
9
matrix) and its resulting FPEs are free from the inﬂuence of sample size and purely reﬂect stabil-
ity of the parameter estimates. In contrast to deﬁning a perturbation in the scale of RMSEA, ˜ε,
the scale of F tends to be more unfamiliar to researchers although it can be considered a sum of
squared standardized residuals under certain regularity conditions (Steiger, 2016). The magnitude
of δF , which is a percentage of ˆF , directly depends on the size of ˆF such that larger ˆF would
be associated with larger δF in magnitude, and vice-versa. Consistent with any sensitivity analy-
sis, several levels of δF (e.g., .02 ˆF and .05 ˆF ) should be used in practice to adequately gauge the
stability of focal parameter estimates under slight perturbations to model ﬁt.
Regardless of the form of the perturbation δFPE , which can be δε or δF , FPEs for the k pa-
rameters, denoted by the vector ˆθ
∗= ˆθ+ε, are obtained by solving
F[Σ(ˆθ
∗,S)] = ˆF∗,
or equivalently,
F[Σ(ˆθ+ε,S)] = ˆF +δFPE,
(6)
where S, ˆF∗and ˆθ are known, and the set of FPEs is obtained by perturbing the ML estimates ˆθ
by a set of vectors ε such that ˆF∗is obtained. Each unique vector ε deﬁnes the magnitude and
direction of where each unique FPE lies from ˆθ. In practice, the search for ε is a numerical one
because no closed-form solution exists in SEM, and we highlight the proﬁle likelihood approach
below in the context of focal parameters (for a closed form solution to multiple linear regression,
see Pek et al., 2016).
A pair of proﬁle likelihood fungible estimates. Consider computing a pair of FPEs about
a single focal parameter θ f ; this pair of scalar FPEs will be deﬁned by two unique and distinct
values of ε that fall below (εL) and above (εU ) the optimal estimate ˆθf . With the partitioning
of focal and nuisance parameters θ = (θf ,θn)′, the deﬁnition of FPEs in Equation 6 is modiﬁed
to reﬂect this partitioning. Speciﬁcally, the lower FPE value is deﬁned as F[Σ(ˆθf + εL, ˜θn),S] =
ˆF + δFPE . Similarly, the upper FPE value is deﬁned by substituting εL with εU . Note that εL
is necessarily negative and εU is necessarily positive. By reducing the dimensionality of k pa-
rameters to a kf = 1 focal parameter, the search for FPEs is reduced to a single dimension in the
parameter space.
A proﬁle likelihood fungible contour. Typically, researchers are interested in a limited num-
ber of focal parameters in SEM. Computing a set of FPEs which form a contour for kf > 1 pa-
rameters is a direct extension of the kf = 1 case. In particular, the scalar θ f is generalized to a
vector θ f of length kf ; likewise, the two scalar values of εL and εU are generalized to a set of
multiple vectors, each denoted as ε with length kf , that span the kf -dimensional space. Formally,
FPEs for kf parameters is expressed as
F[Σ(ˆθ f +ε, ˜θn),S] = ˆF +δFPE.
(7)
The vector ε quantiﬁes the magnitude and direction with which ˆθ f is perturbed to satisfy the
slightly perturbed model ﬁt value ˆF∗.
Computing proﬁle likelihood fungible estimates. MacCallum et al. (2013) introduced a
root ﬁnding algorithm by Brent (1973; cited in Press, Teukolsky, Vetterling, & Flannery, 1992) as
one approach to compute FPEs3. This root ﬁnding algorithm was adapted from previous work by
3MacCallum et al.’s (2013) computational method is distinct from the proﬁle likelihood method outlined in this


## Page 10


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
10
MacCallum, Lee, and Browne (2010) on the phenomenon of isopower in SEM, and has also been
included in a review of likelihood-based methods to compute CSs (see Pek & Wu, 2015). Alterna-
tively, FPEs can be estimated via the faster algorithm developed by Wu and Neale (2012), which
does not involve the nested iterative estimation of ˜θn. This algorithm has been implemented in the
current version of OpenMx (Neale et al., 2015) for proﬁle likelihood CIs. Indeed, the estimation
of proﬁle likelihood CSs and FPEs can make use of the same algorithms because both types of
parameter uncertainty can be uniﬁed under a general perturbation framework based on the likeli-
hood function (see also supplemental material).
A General Perturbation Framework
Parameter uncertainty is fully represented by the likelihood function (Pawitan, 2001), such
that proﬁle likelihood CSs and FPEs can be uniﬁed under a general framework (cf., Pek et al.,
2016). First, observe that parameters θ can be represented as a function of some form of the like-
lihood such as F from Equation 1 (see Bollen, 1989, p. 131–135 for the derivation of the discrep-
ancy function from the log-likelihood). Next, the computation of a boundary point of a CS or an
FPE for focal parameters θ f can be couched as a perturbation from the optimal focal estimates ˆθ f
by the vector ε due to a perturbation δ applied to the likelihood value associated with the optimal
model ˆF :
F[Σ(ˆθ f ,+ε, ˜θn),S] = ˆF +δ,
(8)
where the nuisance parameters are eliminated by their ML estimation in ˜θn. Geometrically, the
perturbation δ is the vertical distance from the maximum point of the likelihood, which deﬁnes a
horizontal ‘slice’ of the proﬁle likelihood surface expressed in F .
Conﬁdence Sets
The deﬁnition of CSs for kf focal parameters from Equations 2 and 3 can be re-expressed
to follow the form of Equation 8 of the general perturbation framework. Speciﬁcally, the LRT
statistic G2, which is inverted to construct CSs, can be re-expressed in the metric of the MWL
discrepancy function: G2 = (N −1)[F[Σ(θ0f , ˜θn),S] −ˆF], where Σ(θ0f , ˜θn) is the population
covariance matrix holding the focal parameters θ f ﬁxed at values θ0f under the null, while the
nuisance parameters are eliminated by re-estimation to obtain ˜θn. Recall that θ0f are boundary
points to the CS for the kf focal parameters, which can be expressed as perturbations from the
optimal focal parameter estimates, θ0f = ˆθf + ε. With further algebraic manipulations, CSs can
be alternatively deﬁned as
F[Σ(ˆθf +ε, ˜θn),S] = ˆF +χ2
1−α,kf /(N −1).
(9)
In relation to Equation 8, the perturbation of δ to ˆF , which uniquely deﬁnes CSs, is the scaled
critical value associated with G2: δCS = χ2
1−α,kf /(N −1), where the subscript CS denotes the per-
turbation that deﬁnes CSs. Because CSs are a special expression within the general perturbation
framework of Equation 8, boundary points to CSs can be taken as alternative parameter estimates
that are perturbed by ε from optimal estimates ˆθ f due to a perturbation of optimal model ﬁt ˆF by
paper in that the nuisance parameters θn are held ﬁxed at ˆθn instead of re-estimated as ˜θn . Their approach likely
results in the conservative approximation of the size of fungible contours because the uncertainty of the nuisance
parameters is not taken into account (T. Lee et al., in press).


## Page 11


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
11
a magnitude of χ2
1−α,kf /(N −1). The perturbation deﬁning CSs is a function of the critical value
associated with the G2 test statistic that requires the assumption of multivariate normality. Note
that this perturbation is inversely related to sample size: a larger sample size produces a smaller
perturbation and therefore a smaller CS.
Fungible Parameter Estimates
Similar to CSs, the expression of FPEs also follow the form of Equation 8 of the general per-
turbation framework. When a perturbation is added to the RMSEA to deﬁne FPEs (see Equation
4), the perturbation in Equations 7 and 8 is δ = δε, i.e.,
δε = d f

(ˆε+ ˜ε)2 +(N −1)−1	
−ˆF =
 d f ˜ε2 +(N −1)−1d f −ˆF
if ˆε = 0
d f
 ˜ε2 +2ˆε˜ε

if ˆε > 0
(10)
Equation 10 sheds light on the way sample size N may affect the size of sets of FPEs. We note
that for ˆε > 0, this perturbation does not explicitly involve sample size, but it is ultimately af-
fected by sample size because ˆε is involved in the linear term. For a ﬁxed sample covariance ma-
trix S, when ˆε = 0, δε decreases with increasing sample size until it reaches its minimum value
of d f ˜ε; when ˆε becomes positive, δε increases with sample size because ˆε increases with sam-
ple size. For samples of increasing sizes from a given population, this perturbation varies due to
sampling error around a constant value when ˆε is mostly positive but has a random but decreasing
trend when ˆε has a sizable chance of zero.
When FPEs are deﬁned by a perturbation as a percentage of ˆF (see Equation 5), the pertur-
bation in Equations 7 and 8 is δ = δF . For a ﬁxed sample covariance matrix S, this perturbation
is constant and does not change with sample size or d f . For samples of increasing sizes from a
given population, this perturbation is random with a decreasing trend.
The two deﬁnitions of FPEs, based on δε and δF , are special expressions within the general
perturbation framework of Equation 8. In contrast to the perturbation deﬁning CSs, perturbations
deﬁning FPEs are free from distributional assumptions because δFPE is not deﬁned through any
sampling distribution. Similar to CSs, however, FPEs can be interpreted as perturbed values of
ε from the optimal focal parameters ˆθ f due to a perturbation of magnitude δε or δF to optimal
model ﬁt, ˆF or ˆε, respectively.
It is interesting to note the following relationship between δε and δF . From Equation 10, for
N = ∞,
δε
ˆF = d f
 ˜ε2 +2ˆε˜ε

d f ˆε2
=
 ˜ε
ˆε
2
+2
 ˜ε
ˆε

.
(11)
This suggests that if we perturb RMSEA with no bias-adjustment proportional to its observed
value, the result is equivalent to proportionally perturbing the observed discrepancy function
value. For example, increasing the RMSEA (without bias adjustment) by 1% would be equiva-
lent to increasing ˆF by about 2%, irrespective of the d f of the model or the value of RMSEA or
ˆF .
Analytical Relationship
Given that CSs and FPEs can be expressed as a function of the likelihood in the form of Equa-
tion 8, we now consider the issue of when these two kinds of parameter uncertainty are numeri-
cally equivalent. Speciﬁcally, by equating the perturbations δCS with δε or δF , CSs and FPEs are


## Page 12


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
12
numerically equivalent if and only if
χ2
1−α,kf /(N −1) = d f[(ˆε+ ˜ε)2 +
1
N −1]−ˆF
(12)
or
χ2
1−α,kf /(N −1) = δF.
(13)
Although Equations 12 and 13 analytically establish the numerical equivalence of CSs and FPEs,
these two kinds of uncertainty are neither substantively nor theoretically equivalent. Knowledge
about one type of parameter uncertainty does not aid in the interpretation of the other type of un-
certainty. Equations 12 and 13 show that CSs and FPEs are different aspects of parameter un-
certainty which can be quantiﬁed by the proﬁle likelihood expressed in Equations 9 and 7, re-
spectively. More important, observe that the perturbation deﬁning CSs is a function of the critical
value of the LRT to be inverted and sample size; because LRTs are about population parameters,
CSs are inferential devices. In particular, sample size reﬂects sampling variability in that larger N
will reduce the magnitude of δCS and the size of the CS itself. In contrast, the magnitude of the
perturbations which deﬁne FPEs (δε or δF ) are primarily arbitrarily determined by the analyst
for the purpose of conducting a sensitivity analysis regarding the stability of the focal parameters;
FPEs are diagnostic devices in that they provide information on whether optimal parameter esti-
mates can be validly interpreted.. The two deﬁnitions of FPEs (δε or δF ) measure model misﬁt
differently and have contrasting properties: for a given sample covariance matrix, δε is affected
by both model d f and sample size; in contrast, δF is free of N and d f , and is in a standardized
scale of a percentage of ˆF .
Conceptual Distinctions
The two aspects of parameter uncertainty, quantiﬁed by CSs and FPEs, can be uniﬁed under a
framework based on the likelihood function. Suppose that the direct effect of a latent predictor on
a latent outcome is the focal parameter of interest in a LV mediation model (see supplemental ma-
terial for details of this example based on Schmitt, Branscombe, Kobrynowicz, and Owen, 2002).
After controlling for the latent mediator, the residual effect of the latent predictor on outcome is
−0.19, 95% CI = [−0.39,−0.01]. Although the CI implies a statistically signiﬁcant and negative
direct effect at the 5% level of signiﬁcance, the plausible population values for this parameter can
be very close to zero. Conversely, a perturbation of ˜ε = .005 or δF = .076 ˆF in a sensitivity anal-
ysis is associated with FPE values of −.533 and 0.097. The FPEs suggest instability of the direct
effect under a slight perturbation to model ﬁt because the FPEs are widely varying, and the upper
FPE suggests that the direct effect could be positive although the optimal estimate is negative. In
this instance, the FPEs suggest that the direct effect should not be validly interpreted and the CS
implies high estimate imprecision about the population direct effect.
Conﬁdence sets allow researchers to make inferential statements about unknown population
parameters because they span a range of plausible population values within their boundary points,
which are limits to a range of estimates (see Equation 3). Stated differently, the parameter values
located on the boundary of the CS as well as within the CS are of substantive interest. Addition-
ally, CSs communicate information about estimate precision and quantify sampling variability.
The information communicated by CSs informs researchers of how precise parameter estimates
are, and CSs deﬁne the range of plausible values which the population parameters can take on.


## Page 13


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
13
In contrast, FPEs are subjectively and arbitrarily deﬁned, and there can be more than one deﬁ-
nition of FPEs (e.g., ˜ε versus δF ). Indeed, several sets of FPEs should be constructed to quantify
the stability of a model’s description of the data, afforded by the parameter estimates, with respect
to a slight change in model ﬁt. Note that the values which FPEs take on as alternative parameter
estimates are not meant to be interpreted from a substantive standpoint. Instead these FPEs are
constructed to communicate the variability and stability in the values which parameter estimates
can assume, which informs of whether optimal parameter estimates can be validly interpreted.
Several sets of FPEs provide important information on whether parameter estimates can be inter-
preted deﬁnitively (T. Lee et al., in press). When sets of FPEs with limited variability are obtained
in a sensitivity analysis, strong conclusions can be drawn from the interpretation of signiﬁcant
focal parameters. When sets of FPEs with high variability are observed, which implies wildly
different interpretations of effects that are associated with a slightly perturbed value of model ﬁt,
there is little basis to interpret the optimal estimates. Unlike CSs, where the region located within
boundary points is meaningful as plausible population parameter values, only points in the set of
FPEs are of interest; estimates lying within the contour or surface formed by the FPEs are associ-
ated with a perturbation to model ﬁt that is smaller than what is speciﬁed. Important distinctions
between CSs and FPEs are summarized in Table 1.
Targeted Illustration
To further emphasize the distinction between CSs and FPEs, we report on a targeted illus-
tration examining three factors which could inﬂuence the behavior of CSs and FPEs: (a) sample
size, (b) model ﬁt, and (c) the magnitude of correlations among the MVs.
Factors
Sample size. Sample size is expected to inﬂuence the size of CSs because the perturbation
deﬁning CSs decrease with increasing sample size. Increasing sample size would result in tighter
CSs, reﬂecting higher precision and lower sampling variability. Sample size is expected to mini-
mally inﬂuence the size of FPE sets as discussed. Two levels of sample size, N = 200 and N =
1000, were chosen to reﬂect moderate and large sample sizes typically observed in substantive
research.
Model ﬁt. Limited exploratory computations of FPEs on published examples have revealed
a tendency for the size of FPE contours or surfaces to vary with model ﬁt; larger FPE contours
have been observed to be associated with less well-ﬁtting models whereas tighter FPE contours
have been observed to be associated with good ﬁtting models. The estimated model discrepancy,
ˆF , will be large under poor model ﬁt, suggesting a ﬂat likelihood surface. In this vein, decreasing
levels of model ﬁt is likely associated with decreasing peakedness of the likelihood surface. Al-
ternatively, improving model ﬁt is expected to be associated with tighter CSs and FPE contours.
Three levels of model ﬁt were examined, as deﬁned by the population RMSEA: ε = 0 (perfect
ﬁt), ε = 0.03 (good ﬁt), and ε = .09 (poor ﬁt). Overall model ﬁt was controlled by using the
method of Cudeck and Browne (1992) to construct a covariance matrix which yields a speciﬁed
minimum discrepancy function value in the population, F0, adding realism to the data generation
process as actual data do not appear to follow models which hold exactly in the samples (Tucker,
Koopman, & Linn, 1969).
Magnitude of correlations. In general, larger correlations compared to smaller correlations


## Page 14


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
14
among MVs are associated with more power to reject false models (Neale & Miller, 1997). Fewer
models can ﬁt well to data structures with larger correlations among MVs, implying more peaked
likelihood surfaces. Thus, it is hypothesized that data structures with larger correlations would
result in tighter CSs and FPEs for focal parameters and vice-versa. Two levels of the magnitude
of correlations among the MVs were speciﬁed (small versus large) and two approaches to control
this magnitude were employed, resulting in four models. These two approaches are detailed in the
section below.
Population Generating Models
Data were generated based on a published LV mediation model by Schmitt et al. (2002),
where a LV mediation model was ﬁt to 13 MVs, conﬁrming that the effect of Perceived Discrim-
ination on Well-being is mediated by In-group Identiﬁcation4. The population generating model
can be expressed as
Σ = Λ(I−B)Φ(I−B)′Λ′ +Ψ,
(14)
where Λ is a 13 × 3 matrix of factor loadings, I is a 3 × 3 identity matrix, and B is the 3 × 3
matrix of structural paths; Φ is a 3 × 3 matrix containing the variances and covariances of the
exogenous LV as well as the residual variances and covariances of the endogenous LVs, and Ψ is
a diagonal 13 × 13 matrix of the MV unique variances. The exogenous and mediating LVs each
have four MVs, and the endogenous LV has ﬁve MVs. All 13 factor loadings in Λ were speciﬁed
to be close to 0.8 to avoid equivalent population parameter values, and the matrix Φ is speciﬁed
to be diagonal with unit variances.
Magnitude of correlations. The magnitude of correlations among MVs was determined by
either altering the size of the unique MV variances in Ψ or the size of the structural paths in B.
These two approaches were examined because some substantive research is solely focused on
measurement models while others focus on structural paths.
Unique variances. The size of unique variances of MVs indirectly affects their correlations.
The variance of each MV is due to three sources of variation: common variance, speciﬁc variance,
and error variance. Common variance is due to the common factor or LV, speciﬁc variance repre-
sents systematic factors affecting the MV, and error variance represents random error of measure-
ment or unreliability. Reliable variance in an MV is the sum of common and speciﬁc variances,
and unique variance is the sum of speciﬁc and error variances. Small unique variances translate to
larger correlations between MVs by reﬂecting accuracy of measurement associated with increased
power to reject false models (Browne, MacCallum, Kim, Andersen, & Glaser, 2002). Two levels
of unique variances are speciﬁed, resulting in low and high correlations among MVs. Large and
small measurement errors are deﬁned by unique variances Ψ j j close to 0.5 and 0.1, respectively,
where j = 1,...,13. Small levels of random noise were added to 0.5 or 0.1 to avoid equivalent
population parameter values.
Structural paths. The magnitude of correlations among MVs are also inﬂuenced by the size
of structural pathways in B; the larger the structural paths, the larger the correlations among the
4The supplemental material includes computations of CSs and FPEs for the direct and indirect effects of Per-
ceived Discrimination on Well-being.


## Page 15


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
15
MVs. Small and large structural paths were, respectively, speciﬁed as
B =


0
0
0
0.2076
0
0
−0.1989
0.2015
0

and B =


0
0
0
0.6076
0
0
−0.5989
0.6015
0

.
The 2 (size of unique variances) × 2 (size of structural paths)= 4 different models varied in
the average strength of correlations among MVs. The model with large unique variances and
small structural paths (Σ1) had the smallest average correlations followed by small unique vari-
ances and small structural paths (Σ2), then large unique variances and large structural paths (Σ3),
and ﬁnally small unique variances and large structural paths (Σ4). Three levels of model ﬁt (ε =
0, 0.03, and 0.09) where then applied to these four matrices, resulting in 12 population generating
models.
Data Generation and Analysis
Given the 12 population generating models, a random sample for two levels of sample size
(N = 200 and 1000) were drawn, resulting in 24 sample covariances and a total of 36 conditions
including the 12 population covariances. Following convention, we constructed 95% CRs for two
focal parameters on the sample data. The FPE contours for the same two focal parameters were
deﬁned by a perturbation to the RMSEA of ˜ε = .005 (MacCallum et al., 2009, 2010) and a per-
turbation of δF = .05 ˆF , and FPEs are obtained for the population and sample covariances. Note,
FPEs based on δF are not obtained for population covariance matrices where model ﬁt is per-
fect (i.e., F = 0). Each CR and FPE contour was constructed with 100 points which sampled
the kf = 2-dimensional proﬁle likelihood surface using a variant of the root ﬁnding algorithm of
MacCallum et al. (2010).
The focal parameters of interest are the two structural paths of the indirect effect θ f = (β21,β32)′.
To identify the model with k = 29 parameters and d f = 62, all LVs were scaled to have 1.0 vari-
ance or residual variances. This speciﬁcation of the model results in proﬁle likelihood surfaces
which tend to be elliptical in nature (cf., standardized structural effects in the empirical examples
to follow) such that the widths of the major and minor axes of the CRs and FPEs can be reason-
ably computed to numerically quantify their size. Table 2 presents model ﬁt information, in terms
of RMSEA and F , for the 36 covariances. Across the population covariances, ε and F are in-
variant. In sample covariances, ˆε and ˆF vary between different models, sample sizes, and model
ﬁt, reﬂecting sampling variability and model error. As sample size decreases or model misﬁt in-
creases, ˆF increases. Similarly, ˆε increases with increasing model misﬁt while holding sample
size constant, and vice-versa. Note that ˆε is slightly smaller for N = 200 compared to N = 1000
because of the larger effect of the sample size correction in smaller samples.
Results
Characteristics of different perturbation schemes. Under the general perturbation frame-
work, the ﬁrst step to computing CSs or FPEs is to perturb F in the population or ˆF in the sample
(see Equation 8). Graphically, the perturbation δ is the vertical distance from the ML estimates of
the focal parameters, ˆθ0f , which deﬁnes CSs and FPEs; larger δ results in moving farther down
the kf -dimensional proﬁle likelihood surface which leads to wider CSs and FPEs and vice-versa.
In the scale of F , the perturbations for CSs when N = 200 and 1000 are ﬁxed at .030 and .006,
respectively. As expected, increasing sample sizes decreases δCS resulting in tighter CSs.


## Page 16


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
16
Table 2 presents FPE perturbations where ˜ε = .005 and δF = .05F in the scale of F , de-
noted by δε and δF respectively. From Table 2, controlling for model ﬁt, δε for the population is
invariant across the four population covariances because no sample size adjustment is involved.
In contrast, holding model misﬁt constant, δε varies across sample covariances and sample size
because of sampling variability and the sample size adjustment. Thus, a ﬁxed perturbation value
of ˜ε does not result in an invariant magnitude of δε across different populations coupled with
sampling variability. Note also that when sample size is held constant, δF is relatively consistent
across different population covariances and levels of model misﬁt. In general, ˜ε = .005 is associ-
ated with a larger perturbation compared to δF = .05 ˆF ; the converse is true when sample size is
small (see Equation 11).
Sample size. Table 3 presents the means and standard deviations (SD) of major and minor
axis widths for CRs across the three levels of model ﬁt. As expected, CRs increase in size when
sample size decreases as indicated by the larger widths at smaller sample sizes; the zero SDs of
the major and minor axes of the CRs indicate that model ﬁt did not affect their size. Additionally,
Table 3 also presents values of major and minor axis widths of FPE sets by sample size and model
ﬁt. For FPEs deﬁned by RMSEA (˜ε), increases in sample size decreased the size of FPE sets in
the condition of perfect ﬁt (ε = 0); for the conditions of imperfect ﬁt, sample size exerted little
inﬂuence on the size of sets of FPEs (see Equation 10). For FPEs deﬁned by a proportion to ˆF
(δF ), increasing sample size led to smaller sets of FPEs.
Model ﬁt. Contrary to expectations, CSs were unrelated to model ﬁt and were essentially
constant in size across the three levels of model ﬁt as evidenced by the zero SDs in Table 3. Fig-
ure 1 presents CRs and FPE contours based on ˜ε for the 36 conditions. Figure 2 presents FPEs
based on δF for the 36 conditions. Sample size increases from the top to the middle row of plots
within each ﬁgure, and ML estimates (or population parameters) for each of the four models
are presented as solid geometric shapes within each plot. The last row of plots in Figures 1 and
2 relate to population models where only FPEs are computed. Boundary points forming CRs
and FPE contours of the focal parameters are represented by analogous open geometric shapes;
the large unique variances and small structural paths model (Σ1) is represented by squares, the
small unique variances and small structural paths model (Σ2) is represented by triangles, the large
unique variances and large structural paths model (Σ3) is represented by diamonds, and ﬁnally the
small unique variances and large structural paths model (Σ4) is represented by circles. Because
CSs are not inﬂuenced by model ﬁt, they were not presented by different levels of model ﬁt.
FPE contours were inﬂuenced by model ﬁt as shown in Figures 1 and 2. Among the plots of
FPEs, model ﬁt decreases from the left most to the right most columns of plots in each Figure.
For FPEs deﬁned by δF (see Figure 2), improving model ﬁt is associated with smaller FPE con-
tours. For FPEs deﬁned by ˜ε, at the level of the population and at N = 1000 (second and third
rows of FPE contours in Figure 1), improving model ﬁt is related to smaller FPE contours. How-
ever, at N = 200, model ﬁt does not show a monotonic relationship with the size of FPE contours
(ﬁrst row of FPE contours in Figure 1); the smallest FPE contour is associated with good model
ﬁt (ε = .03), followed by perfect model ﬁt (ε = 0), and ﬁnally poor model ﬁt (ε = .09). These
results are not surprising. As shown in Equation 10, when ˆε > 0, the δε decreases with improv-
ing model ﬁt until it reaches the minimum of d f ˜ε2 at ˆε = 0; after that it increases with improving
model ﬁt until it reaches d f(˜ε2 +(N −1)−1) at ˆF = 0. Although the perturbation deﬁning FPEs,
δε = .005, is a ﬁxed value in the scale of RMSEA, this perturbation translates to different val-
ues in the scale of F (i.e., δε; see Table 2), which depends on sample size and model error (see


## Page 17


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
17
Equation 4; cf., Chen, Curran, Bollen, Kirby, & Paxton, 2008). For instance, for the model with
small unique variances and large structural paths (Σ4), ˜ε = .005 translates to δε = .030, .014, and
.055 for perfect, good, and poor model ﬁt in the scale of F at N = 200, respectively. For the same
model, δε = .009, .018, and .056 at N = 1000 for perfect, good, and poor model ﬁt, respectively.
Magnitude of correlations. Recall that the magnitude of correlations were manipulated by
either changing the size of unique variances of the MVs or the size of the structural paths, result-
ing in four models. Computations for these four models are presented within each plot in Figures
1 and 2; the two elliptical forms lying to the bottom left of each plot represent models with small
structural paths whereas the two elliptical forms lying to the top right of each plot represent mod-
els with large structural paths. The overlapping pairs of elliptical forms represent models with
small and large unique variances. Note that the values of of the focal parameters in the population
are identical, and increase in variability as seen by their separation in Figures 1 and 2 as sample
size decreases.
Unique variances. Holding the size of the structural paths constant, models with small unique
variances are associated with smaller CSs and FPE contours for the two focal parameters com-
pared to large unique variances (Σ2 versus Σ1 and Σ4 versus Σ3) as shown in Figures 1 and 2 and
corroborated in Table 3. Additionally, Figures 1 and 2 suggest that changing the magnitude of the
unique variances did not seem to change the shape of the proﬁle likelihood surface. As hypoth-
esized, larger correlations due to smaller unique variances led to more peaked proﬁle likelihood
surfaces, resulting in tighter CRs and FPE contours.
Structural paths. Holding unique variances constant, CRs and FPE contours for models with
smaller structural paths tend to be smaller compared to those for larger structural paths in a me-
diation model (Σ1 versus Σ3 and Σ2 versus Σ4). From Table 3, the major and minor axes of CRs
and FPE contours for the two focal parameters across the different sample sizes conﬁrm these ob-
servations. Increasing the size of structural paths increased the correlations among the MVs, but
resulted in less peaked proﬁle likelihood surfaces and larger CRs and FPE contours. Additionally,
from Figures 1 and 2, increasing the magnitude of structural effects also changed the shape of the
likelihood surface for the focal parameters.
These results suggest that manipulating the size of the correlations among the MVs changes
the peakedness and shape of the proﬁle likelihood surface, inﬂuencing the size and shape of CRs
and FPE contours. However, it is not the magnitude of the correlations per se that determine the
shape of the proﬁle likelihood surface, but how the correlations were manipulated. Decreasing
unique variances and decreasing structural effects in a mediation model led to more peaked like-
lihood surfaces of the focal parameters and tighter CRs and FPE contours. In contrast, increasing
unique variances and increasing structural effects in a mediation model results in ﬂatter proﬁle
likelihood surfaces and larger CRs and FPE contours.
Empirical Data Illustrations
Given the distinct properties of CSs and EWs, we turn to illustrating their utility and inter-
pretation with three empirical examples below. These examples involve using a SEM to model
attitudes in prediction of initiating a conversation with a stranger (Example 1, Bagozzi & War-
shaw, 1988), a regression model involving latent variables in predicting posttraumatric growth in
the context of pediatric palliative care (Example 2, Cadell et al., 2014), and a latent variable medi-
ation model examining the indirect effect of adolescent spirituality on thriving through religiosity


## Page 18


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
18
(Example 3, Dowling et al., 2004). OpenMx code of examples are provided in the supplementary
material.
Example 1: Conversation with a Stranger
Bagozzi and Yi (1988) presented research by Bagozzi and Warshaw (1988) which investi-
gated what motivates people to initiate a conversation with an attractive stranger. Attitude towards
trying to initiate such a conversation is hypothesized as a predictor of actual, subsequent Trying
to initiate a conversation in the succeeding week, and Intention to try is included as a mediator.
Figure 3 presents a path diagram of the hypothesized relationship which also includes Subjective
Norm of others’ opinions that one should try as a covariate. Attitude and Intention are measured
by three and two indicators, respectively. Trying and Subjective Norm are measured variables
themselves. The model has a total of 17 parameters, and the correlation matrix of all measured
variables based on N = 250 is reported in Table 5 of Bagozzi and Yi (1988).
Our analysis reproduced the estimates of model ﬁt reported in Bagozzi and Yi (1988) with
χ2(11) = 6.801, ˆF = 0.0273, RMSEA = 0, and CFI = TLI = 1. Parameter estimates of all param-
eters are given in the supplementary material. Below, we focus on the direct effect of Attitude on
Trying and its indirect effect through Intention. Parameter estimates, CIs and FPEs of these pa-
rameters are summarized in Table 4. We ﬁrst consider the direct effect. The ML estimate of this
path is very small with a 95% proﬁle likelihood CI including zero, suggesting a lack of evidence
of the existence of a direct effect beyond the mediation effect through Intention in the population.
The perturbation applied to ˆF is δCS = χ2
.95,1/(250−1) = 0.0154 for this CI.
From a sensitivity analysis, two perturbations to model ﬁt were ﬁrst selected for RMSEA,
˜ε1 = .001 (δFPE1 = .0169) and ˜ε2 = .005 (δFPE2 = .0171). The two pairs of FPEs coincide
with the CI to the second decimal place because the three perturbations are very close in magni-
tude. The FPEs suggest that slight changes in model ﬁt could change the sign of the direct effect,
raising the question of whether inferences based on the parameter estimate are valid. We further
perturb the model ﬁt with δFPE3 = 0.02 ˆF = 0.00055 and δFPE4 = 0.05 ˆF = 0.00137. Neither pairs
of FPEs includes zero, indicating that the sign of the estimate is robust to these perturbations. The
lack of evidence of a direct effect is entirely due to sampling error.
We now consider the indirect effect of Attitude on Trying through Intention. The ML esti-
mates for both paths are positive. A perturbation of δCS = χ2
.95,2/(250 −1) = 0.024 deﬁnes
the 95% joint CR. The same four perturbations deﬁned above were used to compute four sets
of FPEs. Because the perturbation deﬁning the CR is now larger than those deﬁning the FPEs,
the CR is larger than the FPE contours. The intervals listed in Table 4 are projections of the CR
and sets of FPEs from two dimensions to one dimension. Figure 4 depicts the CR and FPE con-
tours. The largest contour of crosses represent the CR. The next two largest contours, represented
by open and closed circles, are the two sets of overlapping FPEs obtained from perturbing the
RMSEA. Finally, the two smallest FPE contours, represented by open and closed diamonds, are
associated with perturbations of ˆF . The 95% CR does not contain any values of 0, implying that
the two estimated positive effects are both signiﬁcant at the 5% level of signiﬁcance. The four sets
of FPE contours are even smaller, suggesting the estimates are stable against slight perturbations
to RMSEA and ˆF , justifying the valid interpretation and inference afforded by these parameter
estimates.
This example illustrates the situation where FPEs are smaller than or of about equal size to a
CS. In this situation, parameter estimates are not as sensitive to perturbations to model ﬁt as they


## Page 19


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
19
are to sampling error, and conclusions based entirely on the analysis of sampling variability is
valid.
Example 2: Posttraumatic Growth of Caregivers
Cadell et al. (2014) investigated factors which contribute to post-traumatic growth (PTG) of
caregivers to children with a life-limiting illness. In this context of caregiving, PTG refers to
the positive changes that people experience as a result of adverse circumstances due to a trau-
matic event (Tedeschi, Park, Calhoun, et al., 1998) and is measured by ﬁve subscales of the Post-
traumatic Growth Inventory (PTGI; Tedeschi & Calhoun, 1996): Relating to Others (y1), New
Possibilities (y2), Personal Strength (y3), Appreciation of Life (y4) and Spiritual Change (y5).
Because “ﬁnding meaning” is an important part of the process which leads to PTG, meaning in
caregiving (MCG) that is deﬁned as the sense which people make of their caregiving experiences
is included as a key variable. Five additional variables were also included in their study: Self-
esteem, Optimism, Spirituality, Depression and Caregiver burden. The correlation matrix and
standard deviations of the ﬁve subscales of PTGI and the six other variables are presented in Table
2 of Cadell et al. (2014), and the total sample size is N = 273.
For illustrative purposes, we consider a latent variable regression model where PTG is pre-
dicted by MCG, Spirituality, and a latent variable Psychological Well-being (PWB) which is indi-
cated by Self-esteem (x1), Optimism (x2), Depression (x3) and Caregiver Burden (x4). MCG and
Spirituality are single indicators and the square root of their reliability values (0.82 and 0.93 as
reported in Cadell et al., 2014) were used as ﬁxed (standardized) loadings. All variables are stan-
dardized, with 11 manifest variable standard deviations included separately as nuisance parame-
ters. The model has a total 27 parameters, including a free path from spirituality to the Spiritual
Change subscale of PTG (see Figure 5). This model has acceptable ﬁt, with χ2(39) = 112.71,
ˆF = 0.414, RMSEA= 0.0834 with 95% CI (0.062,0.105), CFI= 0.948 and TLI= 0.927. All
loadings are above 0.40 and signiﬁcant at p < .05. Details of parameter estimates are reported in
the supplementary material. We focus on the regression paths as presented in Table 5.
Parameter estimates, CIs and FPEs are summarized in Table 5. The point estimates show a
large effect of MCG on PTG, controlling for Spirituality and PWB. The regression coefﬁcients
associated with Spirituality and PWB are negative, implying that an increase in one of these vari-
ables predicts a decrease in PTG after controlling for MCG and the other variable. The 95%
point-wise CIs suggest that the effect of MCG on PTG is large and statistically signiﬁcant, whereas
the conditional effects of Spirituality and PWB on PTG could be non-existent in the popula-
tion because their CIs are close to zero. These CIs correspond to the perturbation to ˆF , δCS =
χ2
.95,1/(273−1) = 0.0141.
Next, we compute FPEs for the three focal coefﬁcients in a sensitivity analysis. The same four
perturbations applied in Example 1 were also applied to Example 2, and the resultant increases
in ˆF are presented in the last column of Table 5. The ﬁrst and third pairs of FPEs (i.e., based on
˜ε1 and δF1 ) are tighter around their ML estimates than the CIs because δFPE < δCS. For these
δFPE perturbations, parameter estimate uncertainty is smaller than that due to sampling error. In
contrast, the second and fourth FPEs (i.e., based on ˜ε2 and δF2 ) are wider than the CIs. Note, the
most variable pair of FPEs (deﬁned by ˜ε2) is associated with negative and positive alternative val-
ues for both individual effects of Spirituality and PWB on PTG, suggesting that these individual
effects are not robust. Taken together, the sensitivity analysis regarding the stability of individual
coefﬁcients suggests that the individual conditional effects of Spirituality and PWB on PTG are


## Page 20


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
20
both unstable, raising questions on whether inferences about these effects are valid.
In addition to individual coefﬁcients, we can also consider the total effect of Spirituality and
PWB, controlling for MCG, on PTG. This contribution can be measured as the variance of PTG
due to Spirituality and PWB for a given level of MCG, which is a function of the path coefﬁcients
and the correlations among the three predictors. The point estimate of this variance, 0.029, is
relatively small; although relatively close to zero, the 95% CI (0.004,0.075) suggests that this
effect is signiﬁcant at the 5% level of signiﬁcance. Sensitivity analysis provides information on
the lack of validity of this result in that this effect could essentially be zero (i.e., 3 × 10−6) based
on largest of the four perturbations. The FPEs suggest that inferences about this total effect are
potentially invalid.
This example demonstrates the unique utility of FPEs as a diagnostic device for evaluating
whether parameter estimates can be validly interpreted based on their stability in relation to the
model’s ﬁt to data. For a model whose ﬁt is acceptable but not close, perturbations to model ﬁt
may reveal instability in parameter estimates which exceed the uncertainty due to sampling error
even for medium sample size. Thus, inspection of FPEs would provide valuable diagnostic infor-
mation unavailable from CIs and CRs.
Example 3: Adolescent Thriving
Dowling et al. (2004) investigated the relationship among Spirituality, Religiosity, and Thriv-
ing of adolescents in a latent variable mediation model. Thriving is deﬁned as positively devel-
oping, Religiosity is deﬁned as the relationship between a particular doctrine about a supernatu-
ral power through institutional afﬁliation and participation in prescribed practices (Reich, Oser,
& Scarlett, 1999), and Spirituality is deﬁned as seeing life and living in new and better ways
and taking something to be transcendant (Reinhart, 2015). It was hypothesized that the effect of
Spirituality on Thriving is mediated through Religiosity, and data from a sample of N = 1000
youth from the Search Institute Young Adolescents and their Parents archival data set was ana-
lyzed. Religiosity, Spirituality, and Thriving were conceptualized as second order factors (e.g., see
Dowling, Gestsdottir, Anderson, von Eye, & Lerner, 2003), each subsuming four, three and nine
ﬁrst order factors, respectively; each ﬁrst order factor was indicated by two or three items, with a
total of 47 items. Despite a second order factor conceptualization, the authors reported a model
with the three latent variables measured directly by the items without the ﬁrst order factors. They
reported that their model ﬁt well, χ2(998) = 2441.28, RMSEA= 0.049 and CFI = 0.90, and the
indirect effect of Spirituality on Thriving through Religiosity was signiﬁcant.
For illustrative purposes, we simpliﬁed the model and selected 14 out of the 47 variables to
indicate the three latent variables. One variable was selected from each of the 16 lower order
factors to maximize content validity of the latent variable save for “Participation in Activities of
Self-Interest” because items loaded weakly (< 0.1) onto this factor. Additionally, only one of the
six items measuring the lower order factors of “Rules for Youth Presented by Father” and “Rules
for Youth Presented by Mother”, which are subsumed by Thriving, was selected to avoid corre-
lated residuals. This model has 31 parameters and yields χ2(74) = 254.7, RMSEA = 0.049, CFI
= 0.87, TLI = 0.84 and SRMR = 0.042. Parameter estimates of all parameters are reported in
the accompanying supplementary material. Below we focus on the latent variable mediation.
Parameter estimates, CIs and FPEs of the three paths among the latent variables are summa-
rized in Table 6. The 95% point-wise CI for the direct effect is constructed with δCI = χ2
.95,1/(1000−
1) = 0.0038; the 95% joint CIs for the two paths of the indirect effect are constructed with δCI =


## Page 21


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
21
χ2
.95,2/(1000 −1) = 0.0060. The ﬁrst, third and fourth FPEs were constructed with the same per-
turbations as in the other two examples. Because ˜ε2 = .005 (δFPE2 = .0384) would lead to very
wide FPEs which require a delicate choice of parameter boundaries in the code for proper conver-
gence, the second FPE was deﬁned as δFPE2 = .0300 (˜ε2 = .00394) instead.
All parameter estimates of the three paths are positive, but the 95% CI of one of the indirect
path includes zero, suggesting that the positive indirect effect of Spirituality on Thriving through
Religiosity could be due to sampling error. The CIs for the direct effect is smaller than the four
pairs of FPEs, and the CIs for the two paths of the indirect effect are smaller than three of the four
FPEs. The small CIs are due to the large sample size. Although the two smaller pairs of FPEs are
similar to the CIs, the two larger pairs of FPEs show greater instability in the values with which
the focal parameters can take. In particular, the second set of FPEs deﬁned by ˜ε2 implies a direct
path greater than 2 and an indirect path of almost −1.5. Figure 6 presents plots of FPE contours
for two pairs of the three paths. They convey a similar message in that the largest FPE contour
(represented by open circles) communicates instability of the focal effects predicting Thriving
from Religiosity and Spirituality, raising concerns regarding their validity.
A closer look at this FPE contour reveals that this is due to collinearity: an alternative value
of the effect of Spirituality on Religiosity is 0.96, which is extremely close to 1.0. In this simple
linear regression of Religiosity on Spirituality, because the standardized regression coefﬁcient is
also the correlation coefﬁcient, these two variables as predictors of Thriving could become highly
correlated and manifest as a problem of collinearity. Indeed, Figure 6 shows that the extreme FPE
values of the coefﬁcients of Spirituality and Religiosity (on the ordinate) are associated with this
near perfect correlation between the two predictors (on the abscissa). Unlike wide CIs which can
be minimized by a larger sample size, the variability in the sets of FPEs suggest a possible issue
with the research design. For a given correlation between Spirituality and Religiosity in the pop-
ulation, its FPEs could be reduced by the use of indicators with higher loadings (i.e., improved
measurement) and a model which ﬁts better (see targeted illustration above). This problem of
collinearity which invalidates the results would have been inappropriately overlooked without the
consideration of FPEs.
This example again shows the unique value of FPEs in a sensitivity analysis. When sample
size is large, CIs and CRs are usually small due to the limited sampling error. In such situations,
small perturbations to model ﬁt may reveal instability in parameter estimates which exceed the
uncertainty due to sampling error. Thus, inspection of FPEs could provide valuable diagnostic
information regarding the valid interpretation of parameter estimates which are unavailable from
CIs and CRs.
Summary and Discussion
Conﬁdence sets and FPEs communicate different aspects of parameter uncertainty which pro-
vide information with regards to the extent to which a scientiﬁc ﬁnding can be rigorously inter-
preted. Conﬁdence sets communicate sampling variability and estimate precision whereas FPEs
communicate information on whether parameter estimates can be validly interpreted based on the
stability of parameter values in relation to the speciﬁed model’s ﬁt to data. By introducing a per-
turbation framework based on the likelihood function, it is shown that CSs and FPEs share similar
properties despite their distinct interpretations. Given their apparent commonalities, we clarify the
theoretical relationship between CSs and FPEs by establishing their analytical relationship. In-


## Page 22


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
22
deed, CSs and FPEs are horizontal intersections of the likelihood surface deﬁned by the vertical
distance or perturbation δ from the maximum of the likelihood. We demonstrate distinct charac-
teristics between CSs and FPEs in a targeted illustration and summarize key differences between
CSs and FPEs in Table 1. Further, we illustrate with three empirical examples the value of con-
sidering the distinct information communicated by CSs and FPEs regarding the defensibility of
estimated parameter estimates or effect sizes (cf.,Green, 1977).
Theoretical Properties
In general, the size of CSs and FPE sets are inﬂuenced by: (a) the magnitude of the perturba-
tion δ that uniquely deﬁnes these two kinds of parameter uncertainty, or (b) the peakedness and
shape of the likelihood surface. Note that when sample covariances are modeled, the likelihood
surface is inﬂuenced by sampling variability.
Perturbations. Proﬁle likelihood CSs are deﬁned by a perturbation δCS that is determined by
sample size, the Type I error rate α, and the χ2 quantile. Larger sample sizes, larger error rates,
and smaller quantiles that are determined by a smaller number of kf focal parameters, result in
smaller perturbations and tighter CSs. Conversely, smaller sample sizes, smaller α levels, and
larger quantiles deﬁne larger CSs. The perturbation deﬁning CSs is primarily a function of sample
size and parameter degrees of freedom, and independent of model ﬁt; thus, CSs carry information
only about sampling variability and not model ﬁt.
Fungible parameter estimates are deﬁned by a perturbation, chosen by the researcher, such
that the perturbed model ﬁt is practically no different from optimal model ﬁt. Larger perturba-
tions, in the scale of F , result in larger FPE contours and vice-versa. Based on current convention
(T. Lee et al., in press; MacCallum et al., 2013; MacCallum et al., 2009), we examined perturba-
tions that deﬁne FPEs in the scale of the RMSEA, ˜ε and introduce an alternative perturbation as
a percentage of ˆF . For a given ˜ε, the size of this perturbation in the scale of F is primarily deter-
mined by model ﬁt, and is not very much affected by sample size for a ﬁxed level of model ﬁt in
the population when ˆε > 0. Only when ε = 0 in the population does increasing sample size show
a decreasing effect on the size of sets of FPEs deﬁned by ˜ε. Alternatively, FPEs deﬁned by δF
increase in size with decreasing model ﬁt. Unlike FPEs deﬁned by ˜ε, sample size has a negative
effect on the size of FPE sets deﬁned by δF for a ﬁxed level of model ﬁt in the population but has
no effect for a ﬁxed level of model ﬁt in a sample. However, δε and δF are monotonically related
in certain conditions (see Equation 11). In general, FPE contours carry information largely about
model ﬁt, which dominates information about sampling variability.
Likelihood surface. The likelihood function fully represents parameter uncertainty (Pawitan,
2001), and CSs and FPEs are horizontal ‘slices’ of the likelihood surface which are determined by
their vertical distances (δCS and δFPE ) from the maximum point of the likelihood surface, ˆθ. The
peakedness and shape of the likelihood surface thus determines the size and form of CSs and FPE
contours or surfaces. Contrary to expectations, changes in model ﬁt via the Cudeck and Browne
(1992) method do not alter the shape of the likelihood surface, and changes in the magnitude of
the correlations among the MVs do not directly change the shape of the likelihood surface. In-
stead, manipulating the unique variances of MVs results in different levels of likelihood surface
peakedness; smaller unique variances reﬂecting higher measurement reliability have more peaked
likelihood surfaces, whereas larger unique variances reﬂecting higher measurement error have less
peaked likelihood surfaces. Additionally, changing the magnitude of structural paths (in a latent
variable mediation model) results in changing the shape and peakedness of the likelihood surface;


## Page 23


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
23
larger structural paths were associated with shallower likelihood surfaces that tended to detract
from an elliptical form whereas smaller structural paths had more peaked likelihood surfaces that
were more elliptical in shape.
Considerations for Practice
Conﬁdence sets and FPEs are distinct kinds of parameter uncertainty which provide unique
and useful information to substantive researchers in terms of validly and rigorously interpreting
their effect sizes. Table 1 provides a summary of their distinct properties and uses. In any data
analysis, diagnostics should be conducted to ensure the validity and stability of the model solu-
tion (cf., Belsey, Kuh, & Welsch, 1980; Cook & Weisberg, 1982; e.g., Pek & MacCallum, 2011).
Scientiﬁc conclusions based on inferential methods should move away from null hypothesis sig-
niﬁcance tests which tend to result in essentialist dichotomies (i.e., signiﬁcant or not; see Cohen,
1994). By considering parameter uncertainty due to sampling variability as quantiﬁed by CSs,
and slight perturbations to model ﬁt as quantiﬁed by sets of FPEs, results of an analysis can more
seamlessly be interpreted to reﬂect degrees of conﬁdence in their defensibility.
A model which can appropriately describe or explain phenomena well should ﬁt the data well,
be robust in its description of the data as reﬂected by the size of FPE contours or surfaces such
that parameter estimates can be validly interpreted, and have tight CSs (Green, 1977).5 Conﬁ-
dence sets provide a measure of uncertainty in the estimation of parameters due to sampling vari-
ability; they inform researchers of the statistical signiﬁcance of parameter estimates, the preci-
sion and stability of estimation, and provide a range of plausible population parameter values.
Tight CSs provide a strong basis for inferences whereas wide CSs weaken conﬁdence in mak-
ing inferences about the population. The information inherent in CSs are strictly about statis-
tical inference. On the other hand, FPEs convey diagnostic information regarding the validity
of the model’s description of the data, afforded by optimal parameter estimates, in relation to
the model’s ﬁt to data. When slight perturbations result in compact and tight FPE contours, the
model’s description of the data is stable, providing a basis for interpreting optimal parameter es-
timates and drawing strong and deﬁnitive conclusions. Alternatively, when large FPE contours
are observed such that wildly varying alternative parameter estimates describe the data just as
well as the optimal estimates in terms of model ﬁt, this instability of the model’s description of
the data casts doubts on the validity behind interpreting the optimal parameter estimates. Thus,
the information communicated by FPE contours can either enhance or undermine the validity and
deﬁnitive interpretation of optimal parameter estimates.
Consistent with calls to focus on the stochastic nature of statistical results (e.g., Cumming &
Fidler, 2009; Waldman & Lilienfeld, 2015), we encourage researchers to report CSs about their
effects or focal parameter estimates (for example, see Steinberg & Thissen, 2006). Prior to in-
terpreting CSs, researchers should routinely conduct sensitivity analysis to assess the validity of
statistical results, and FPE contours communicate the stability of a model’s description of the data
via parameter estimates in relation to model ﬁt. To that end, we provide example OpenMx code
for two of our empirical examples to compute CSs and FPEs in the supplemental material. The
practice of constructing CSs and FPEs convey the stochastic nature of statistical results, and can
buttress the case for drawing strong scientiﬁc conclusions. Because research regarding the type
and magnitude of perturbation to deﬁne FPEs is still under development, we recommend using
5The link between sample size and parameter sensitivity has been made by Davis-Stober (2011) for multiple
linear regression.


## Page 24


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
24
several different magnitudes of ˜ε and δF when constructing FPEs to fully explore the stability of
the model’s description afforded by parameter estimates under slight perturbations to model ﬁt.
Future Directions
In this paper, we consolidated contemporary work on proﬁle likelihood CSs (Pek & Wu, 2015)
and FPEs (T. Lee et al., in press; MacCallum et al., 2009, 2010) in SEM by establishing their an-
alytical relationship. We introduced an alternative deﬁnition of FPEs so as to better understand
the nature of FPEs in relation to the measure of model misﬁt to be perturbed. We also illustrated
how these two kinds of parameter uncertainty are distinct, as well as their relevance to drawing
deﬁnitive scientiﬁc conclusions about parameter estimates in practice. To have a fuller under-
standing of the nature of CSs and FPEs, other factors which impact their size and shape such as
the number and types of parameters in the model should be examined in future studies. A better
understanding of the factors which affect CSs and FPE contours is valuable for theory and prac-
tice because the size and shape of FPE contours and CSs determine the limits to which deﬁnitive
interpretations of parameter estimates can be made. Another extension to this work involves de-
veloping a single quantiﬁcation of parameter uncertainty that jointly takes into account stability
of the model’s description of the data via parameter estimates and sampling variability (cf., Wu
& Browne, 2015a, 2015b). Further developing methods to quantify different aspects of parameter
uncertainty can only serve to facilitate researchers’ informed choices behind drawing valid and
deﬁnitive scientiﬁc conclusions.
References
Bagozzi, R. P., & Warshaw, P. R. (1988). From unintended to goal-type behavior and outcomes:
A theory of human action. Unpublished working paper. The University of Michigan.
Bagozzi, R. P., & Yi, Y. (1988). On the evaluation of structural equation models. Journal of
the Academy of Marketing Science, 16(1), 74–94. Retrieved from http://dx.doi.org/
10.1007/bf02723327 doi: 10.1007/bf02723327
Belsey, D. A., Kuh, E., & Welsch, R. E. (1980). Regression diagnostics: Identifying inﬂuential
data and sources of collinearity. New York: John Wiley.
Bentler, P. M. (1990). Comparative ﬁt indexes in structural models. Psychological Bulletin, 107,
238–246. doi: 10.1037/0033-2909.107.2.238
Bollen, K. A. (1989). Structural equation models with latent variables. New York: Wiley.
Brent, R. (1973). Algorithms for minimization with derivatives. Englewood Cliffs, NJ: Prentice-
Hall.
Browne, M. W. (1984). Asymptotically distribution-free methods for the analysis of covariance
structures. British Journal of Mathematical and Statistical Psychology, 37, 62–83. doi:
10.1111/j.2044-8317.1984.tb00789.x
Browne, M. W., & Cudeck, R. (1992, nov). Alternative ways of assessing model ﬁt. Sociological
Methods & Research, 21(2), 230–258. Retrieved from http://dx.doi.org/10.1177/
0049124192021002005 doi: 10.1177/0049124192021002005
Browne, M. W., & Cudeck, R. (1993). Alternative ways of assessing model ﬁt. In K. A. Bollen
& J. S. Long (Eds.), Testing structural equation models. (pp. 136–162). Newbury Park, CA:
Sage.
Browne, M. W., MacCallum, R. C., Kim, C.-T., Andersen, B. L., & Glaser, R. (2002). When ﬁt
indices and residuals are incompatible. Psychological Methods, 7, 403–421. doi: 10.1037/


## Page 25


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
25
1082-989X.7.4.403
Cadell, S., Hemsworth, D., Smit Quosai, T., Steele, R., Davies, E., Liben, S., ... Siden, H.
(2014). Posttraumatic growth in parents caring for a child with a life-limiting illness:
A structural equation model. American Journal of Orthopsychiatry, 2, 123–133. doi:
10.1037/h0099384
Cadigan, N. G. (1995). Local inﬂuence in structural equation models. Structural Equation Mod-
eling, 2, 13–30. doi: 10.1080/10705519509539992
Chen, F., Curran, P. J., Bollen, K. A., Kirby, J., & Paxton, P. (2008). An empirical evaluation of
the use of ﬁxed cutoff points in RMSEA test statistic in structural equation models. Socio-
logical Methods & Research, 36, 462–494. doi: 10.1177/0049124108314720
Cohen, J. (1994). The earth is round ( p < .05). American Psychologist, 49, 997-1003. doi:
10.1037/0003-066X.49.12.997
Cook, R. D. (1986). Assessment of local inﬂuence. Journal of the Royal Statistical Society Series
B, 48, 133–169.
Cook, R. D., & Weisberg, S. (1982). Residuals and inﬂuence in regression. New York: Chapman
& Hall.
Cudeck, R., & Browne, M. W. (1992). Constructing a covariance matrix that yields a speciﬁed
minimizer and a speciﬁed minimum discrepancy function value. Psychometrika, 57, 357–
369. doi: 10.1007/BF02295424
Cumming, G. (2014). The new statistics: Why and how. Psychological Science, 25, 7–29. doi:
10.1177/0956797613504966
Cumming, G., & Fidler, F. (2009). Conﬁdence intervals: Better answers to better questions.
Zeitschrift f¨ur Psychologie/ Journal of Psychology, 217, 15–26. doi: 10.1027/0044-3409
.217.1.15
Davis-Stober, C. P. (2011). A geometric analysis of when ﬁxed weighting schemes will outper-
form ordinary least squares. Psychometrika, 76(4), 650–669. doi: 10.1007/s11336-011
-9229-1
Dowling, E. M., Gestsdottir, S., Anderson, P. M., Von Eye, A., Almerigi, J., & Lerner, R. M.
(2004). Structural relations among spirituality, religiosity, and thriving in adolescence.
Applied Developmental Science, 8, 7–16. doi: 10.1207/S1532480XADS0801 2
Dowling, E. M., Gestsdottir, S., Anderson, P. M., von Eye, A., & Lerner, R. M. (2003). Spir-
ituality, religiosity, and thriving among adolescents: Identiﬁcation and conﬁrmation
of factor structures.
Applied Developmental Science, 7(4), 253–260.
doi: 10.1207/
s1532480xads0704 4
Green, B. F. (1977). Parameter sensitivity in multivariate methods. Multivariate Behavioral
Research, 12, 263–287. doi: 10.1207/s15327906mbr1203 1
Harlow, L. L., Mulaik, S. A., & Steiger, J. H. (2016). What if there were no signiﬁcance tests?
(2nd ed.). Mahwah, NJ: Routledge.
Lee, S.-Y., & Wang, S.-J. (1996). Sensitivity analysis of structural equation models. Psychome-
trika, 61, 93–108. doi: 10.1007/BF02296960
Lee, T., & MacCallum, R. C. (2015). Parameter inﬂuence in structural equation modeling. Struc-
tural Equation Modeling, 22, 102–114. doi: 10.1080/10705511.2014.935255
Lee, T., MacCallum, R. C., & Browne, M. W. (in press). Fungible parameter estimates in struc-
tural equation modeling. Psychological Methods. doi: 10.1037/met0000130


## Page 26


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
26
MacCallum, R. C. (2003). 2001 presidential address: Working with imperfect models. Multivari-
ate Behavioral Research, 38, 113–139. doi: 10.1207/S15327906MBR3801 5
MacCallum, R. C., Browne, M. W., & Lee, T. (2009). Fungible parameter estimates in structural
equation modeling. Paper presented at the Annual Meeting of the Society of Multivariate
Experimental Psychology. Salishan Resort, Oregon.
MacCallum, R. C., Lee, T., & Browne, M. W. (2010). The issue of isopower in power analysis
for tests of structural equation models. Structural Equation Modeling, 17, 23–41. doi:
10.1080/10705510903438906
MacCallum, R. C., Lee, T., & Browne, M. W. (2013). Fungible parameter estimates in latent
curve models. In M. C. Edwards & R. C. MacCallum (Eds.), Current topics in the theory
and application of latent variable models (pp. 183–197). New York, NY: Routledge.
Myung, I. J. (2003). Tutorial on maximum likelihood estimation. Journal of Mathematical
Psychology, 47(1), 90–100. doi: 10.1016/s0022-2496(02)00028-7
Neale, M. C., Hunter, M. D., Pritkin, J., Zahery, M., Brick, T. R., Kirkpatrick, R. M., ... Boker,
S. M. (2015). OpenMx 2.0: Extended structural equation and statistical modeling. Psy-
chometrika. doi: 10.1007/s11336-014-9435-8
Neale, M. C., & Miller, M. B. (1997). The use of likelihood-based conﬁdence intervals in genetic
models. Behavior Genetics, 27, 113–120. doi: 10.1023/A:1025681223921
Open Science Collaboration. (2015). Estimating the reproducibility of psychological science.
Science, 349, aac4716. doi: 10.1126/science.aac4716
Pashler, H., & Wagenmakers, E.-J. (2012). Editors introduction to the special section on repli-
cability in psychological science: A crisis of conﬁdence? Perspectives on Psychological
Science, 7, 528–530. doi: 10.1177/1745691612465253
Pawitan, Y. (2001). In all likelihood: Statistical modelling and inference using likelihood. Oxford,
UK: Oxford University Press.
Pek, J., Chalmers, R. P., & Monette, G. (2016). On the relationship between conﬁdence regions
and exchangeable weights in multiple linear regression. Multivariate Behavioral Research,
51, 719–739. doi: 10.1080/00273171.2016.1225563
Pek, J., & MacCallum, R. C. (2011). Sensitivity analysis in structural equation models: Cases and
their inﬂuence. Multivariate Behavioral Research, 46, 202–228. doi: 10.1080/00273171
.2011.561068
Pek, J., & Wu, H. (2015). Proﬁle likelihood-based conﬁdence intervals and regions for structural
equation models. Psychometrika, 80, 1123–1145. doi: 10.1007/s11336-015-9461-1
Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (1992). Numerical recipes in
Fortran: The art of scientiﬁc computing (2nd ed.). Cambridge, UK: Cambridge University
Press.
Reich, H., Oser, F. K., & Scarlett, W. G. (1999). Spiritual and religious development: Transcen-
dence and transformations of the self. In H. Reich, F. L. Oser, & W. G. Scarlett (Eds.),
Psychological studies on spiritual and religious development: Being human: The case of
religion (Vol. 2, pp. 57–82). Scottsdale, AZ: Pabst Science Publishers.
Reinhart, A. (2015). Statistics done wrong: The woefully complete guide. San Francisco, CA: No
Starch Press, Inc.
Scheff´e, H. (1953). A method for judging all constrasts in the analysis of variance. Biometrika,
40, 87–110. doi: 10.1093/biomet/40.1-2.87
Schmitt, M. T., Branscombe, N. R., Kobrynowicz, D., & Owen, S. (2002). Perceiving discrim-


## Page 27


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
27
ination against one’s gender group has different implications for well-being in women
and men.
Personality and Social Psychology Bulletin, 28, 197–210.
doi: 10.1177/
0146167202282006
Sijtsma, K. (2015). Playing with data – or how to discourage questionable research practices and
stimulate researchers to do things right. Psychometrika, 81, 1–15. doi: 10.1007/s11336-015
-9446-0
Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology undisclosed
ﬂexibility in data collection and analysis allows presenting anything as signiﬁcant. Psycho-
logical Science, 22, 1359–1366. doi: 10.1177/0956797611417632
Steiger, J. H. (2016). Notes on the steiger-lind (1980) handout. Structural Equation Modeling, 23,
777-781. doi: 10.1080/10705511.2016.1217487
Steinberg, L., & Thissen, D. (2006). Using effect sizes for research reporting: Examples using
item response theory to analyze differential item functioning. Psychological Methods, 11,
402–415. doi: 10.1037/1082-989X.11.4.402
Tedeschi, R. G., & Calhoun, L. G. (1996). The posttraumatic growth inventory: Measuring
the positive legacy of trauma. Journal of Traumatic Stress, 9, 455–471. doi: 10.1002/
jts.2490090305
Tedeschi, R. G., Park, C. L., Calhoun, L. G., et al. (1998). Posttraumatic growth: Positive changes
in the aftermath of crisis. Mahwah, NJ: Lawrence Erlbaum.
Tucker, L. R., Koopman, R. F., & Linn, R. L. (1969). Evaluation of factor analytic research pro-
cedures by means of simulated correlation matrices. Psychometrika, 34, 421–459. doi:
10.1007/BF02290601
Tucker, L. R., & Lewis, C. (1973). A reliability coefﬁcient for maximum likelihood factor analy-
sis. Psychometrika, 38, 1–10. doi: 10.1007/BF02291170
Waldman, I. D., & Lilienfeld, S. O. (2015). Thinking about data, research methods, and statistical
analyses: Commentary on Sijtsma’s (2014) “Playing with data”. Psychometrika, 81, 16–26.
doi: 10.1007/s11336-015-9447-z
Waller, N. G. (2008). Fungible weights in multiple regression. Psychometrika, 73, 691—703.
doi: 10.1007/s11336-008-9066-z
Wilkinson, L., & the Task Force on Statistical Inference. (1999). Statistical methods in psychol-
ogy journals: Guidelines and explanations. American Psychologist, 54, 594–604. doi:
10.1037/0003-066X.54.8.594
Wu, H., & Browne, M. W. (2015a). Quantifying adventitious error in a covariance structure as a
random effect. Psychometrika, 80, 571–600. doi: 10.1007/s11336-015-9451-3
Wu, H., & Browne, M. W. (2015b). Random model discrepancy: Interpretations and technicalities
(A rejoinder). Psychometrika, 80, 619–624. doi: 10.1007/s11336-015-9456-y
Wu, H., & Neale, M. C. (2012). Adjusted conﬁdence intervals for a bounded parameter. Behavior
Genetics, 42, 886–898. doi: 10.1007/s10519-012-9560-z


## Page 28


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
28
Table 1: Distinctions between Conﬁdence Sets and Fungible Parameter Estimates
Conﬁdence Sets
Fungible Parameter Estimates
Purpose
Inference
Diagnostics; sensitivity Analysis
Assumption
Data follows some distribution
None
Type of uncertainty
Sampling variability
Stability of parameter estimates in relation to
model ﬁt
Magnitude of
perturbation
Single value determined by N, α, and
critical value of test to be inverted
Several arbitrary values; suboptimal ﬁt practi-
cally the same as optimal ﬁt
Region within
boundary points
Associated with same level of conﬁdence
Associated with smaller perturbation to model
ﬁt
Interpretation of points
Range of plausible population values for
the set of focal parameter(s)
Alternative parameter estimates which explain
the data just as well as the optimal parameter
estimates in terms of model ﬁt
Properties
Converge to a point with increasing N
Converge to a set with increasing N
Unrelated to model ﬁt
Smaller with improved model ﬁt
Note. N=sample size and α = Type I error rate.


## Page 29


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
29
Table 2: Model Fit and Perturbation Values for FPEs in scale of F
Population
N = 1000
N = 200
Model
ε
F
δε
δF
ˆε
ˆF
δε
δF
ˆε
ˆF
δε
δF
Σ1
0
0
.002
−
0
.059
.004
.003
0
.277
.037
.014
.03
.056
.020
.003
.027
.106
.018
.005
.021
.338
.014
.017
.09
.502
.057
.025
.088
.530
.055
.026
.087
.793
.056
.040
Σ2
0
0
.002
−
0
.056
.007
.003
0
.280
.033
.014
.03
.056
.020
.003
.028
.110
.019
.005
.021
.338
.014
.017
.09
.502
.057
.025
.088
.544
.056
.027
.087
.784
.056
.039
Σ3
0
0
.002
−
0
.056
.007
.003
0
.289
.024
.014
.03
.056
.020
.003
.025
.102
.017
.005
.022
.343
.015
.017
.09
.502
.057
.025
.086
.526
.055
.026
.087
.781
.055
.039
Σ4
0
0
.002
−
0
.054
.009
.003
0
.283
.030
.014
.03
.056
.020
.003
.026
.104
.018
.005
.020
.337
.014
.017
.09
.502
.057
.025
.087
.534
.056
.027
.086
.774
.055
.039
Note. FPE = fungible parameter estimates, N = sample size, ε = population model ﬁt in the scale of RMSEA,
ˆε= sample RMSEA, and δε = perturbation of ˜ε = .005 in the scale of F; %F = perturbation of δF = .05F;
Σ1 = large unique variances and small structural effects, Σ2 = small unique variances and small structural
effects, Σ3= large unique variances and large structural effects, and Σ4 = small unique variances and large
structural effects.


## Page 30


30
Table 3: Widths of Major and Minor Axes across Model Fit
Conﬁdence Sets
FPEs (˜ε = .005)
FPEs (δF = .05)
Major Axis
Minor Axis
ε = 0
ε = .03
ε = .09
ε = 0
ε = .03
ε = .09
N
Mean
SD
Mean
SD
Major
Minor
Major
Minor
Major
Minor
Major
Minor
Major
Minor
Major
Minor
Σ1
1000
0.19
0
0.18
0
0.16
0.15
0.33
0.32
0.59
0.56
0.13
0.13
0.18
0.17
0.40
0.38
200
0.43
0
0.40
0
0.48
0.44
0.30
0.28
0.60
0.55
0.29
0.27
0.32
0.30
0.50
0.46
Σ2
1000
0.17
0
0.16
0
0.18
0.18
0.29
0.29
0.51
0.50
0.11
0.11
0.16
0.15
0.36
0.35
200
0.38
0
0.36
0
0.39
0.38
0.26
0.25
0.52
0.50
0.26
0.25
0.28
0.27
0.43
0.42
Σ3
1000
0.25
0
0.20
0
0.27
0.22
0.42
0.34
0.75
0.61
0.17
0.14
0.23
0.18
0.52
0.42
200
0.56
0
0.44
0
0.50
0.39
0.40
0.31
0.76
0.59
0.38
0.30
0.42
0.33
0.63
0.50
Σ4
1000
0.20
0
0.17
0
0.25
0.22
0.35
0.30
0.62
0.53
0.14
0.12
0.19
0.16
0.43
0.37
200
0.46
0
0.39
0
0.46
0.39
0.32
0.27
0.63
0.53
0.32
0.27
0.35
0.29
0.53
0.45
Note. FPE = fungible parameter estimate, N = sample size, and SD = standard deviation; Σ1 = large unique variances and small structural effects, Σ2 = small unique
variances and small structural effects, Σ3= large unique variances and large structural effects, and Σ4 = small unique variances and large structural effects; ε = population
value of model ﬁt in the scale of RMSEA.


## Page 31


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
31
Table 4: Parameter estimates, CIs and FPEs for Example 1
Attitude →Trying
Attitude →Intention
Intention →Trying
δ
ML Estimate
0.050
0.639
0.486
CI (d f = 1)
[−0.119,0.216]
0.0154
CI (d f = 2)
[0.513,0.743]
[0.285,0.672]
0.024
FPE1 (˜ε1 = .001)
(−0.126,0.223)
(0.535,0.727)
(0.318,0.643)
0.0169
FPE2 (˜ε2 = .005)
(−0.128,0.225)
(0.534,0.728)
(0.317,0.644)
0.0171
FPE3 (δF1 = 0.02 ˆF)
( 0.019,0.082)
(0.624,0.656)
(0.457,0.515)
0.00055
FPE4 (δF2 = 0.05 ˆF)
(0.00027,0.100)
(0.611,0.666)
(0.440,0.532)
0.00137
Note. ML = maximum likelihood, CI = conﬁdence interval, FPE = fungible parameter estimate, d f = degrees of
freedom, and δ = perturbation in the scale of F. Additionally, ˜ε = perturbation to the RMSEA and δF = perturbation to ˆF
by a percentage.


## Page 32


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
32
Table 5: Parameter estimates, CIs and FPEs for Example 2
MCG →PTG
Spirituality →PTG
PWB →PTG
δ
ML Estimate
0.870
−0.083
−0.154
CI (d f = 1)
[0.747,0.994]
[−0.219,0.049]
[−0.267,−0.041]
0.0141
FPE1 (˜ε1 = .001)
(0.787,0.953)
(−0.175,0.007)
(−0.231,−0.077)
0.0065
FPE2 (˜ε2 = .005)
(0.677,1.067)
(−0.296, 0.120)
(−0.330,0.020)
0.0335
FPE3 (δF1 = 0.02 ˆF)
(0.777,0.964)
(−0.186,0.018)
(−0.240,−0.068)
0.0083
FPE4 (δF2 = 0.05 ˆF)
(0.720,1.021)
(−0.248,0.077)
(−0.292,−0.018)
0.0207
Note. PTG = posttraumatic growth, MCG = meaning in caregiving, and PWB = psychological well-being; ML =
maximum likelihood, CI = conﬁdence interval, FPE = fungible parameter estimate, d f = degrees of freedom, and δ =
perturbation in the scale of F. Additionally, ˜ε = perturbation to the RMSEA and δF = perturbation to ˆF by a percentage.


## Page 33


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
33
Table 6: Parameter estimates, CIs and FPEs for Example 3
Spirituality →Thriving
Spirituality →Religiosity
Religiosity →Thriving
δ
ML Estimate
0.706
0.617
0.252
CI(d f = 1)
[0.526,0.969]
0.0038
CI(d f = 2)
[0.465,0.773]
[−0.123,0.463]
0.0060
FPE1 (˜ε1 = .001)
(0.460,1.144)
(0.448,0.791)
(−0.199,0.485)
0.0074
FPE2 (˜ε2 = .00394)
(0.197,2.323)
(0.273,0.960)
(−1.481,0.706)
0.0300
FPE3 (δF1 = 0.02 ˆF)
(0.500,1.030)
(0.477,0.760)
(−0.076,0.449)
0.0051
FPE4 (δF2 = 0.05 ˆF)
(0.386,1.354)
(0.395,0.852)
(−0.458,0.548)
0.0127
Note. ML = maximum likelihood, CI = conﬁdence interval, FPE = fungible parameter estimate, d f = degrees of freedom, and δ =
perturbation in the scale of F. Additionally, ˜ε = perturbation to the RMSEA and δF = perturbation to ˆF by a percentage.


## Page 34


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
34
Confidence Sets
N = 200
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
Fungible Contours
ε = 0
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
Fungible Contours
ε = 0.03
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
Fungible Contours
ε = 0.09
β32
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
G
G
G
G
G
N = 1000
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
β
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
G
G
G
G
G
G
Σ1 ML Estimate or Population Parameter
Σ1 Boundary value
Σ2 ML Estimate or Population Parameter
Σ2 Boundary value
Σ3 ML Estimate or Population Parameter
Σ3 Boundary value
G
G
Σ4 ML Estimate or Population Parameter
Σ4 Boundary value
Population
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
β21
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
G
G
G
G
G
Figure 1: Proﬁle likelihood conﬁdence sets and fungible contours (deﬁned by ˜ε) of β21 and β32 by sample size N and type of model;
ε= 0 indicates perfect model ﬁt, ε=.03 indicates good model ﬁt, and ε=.09 indicates poor model ﬁt; Σ1= large unique variances and
small structural effects, Σ2= small unique variances and small structural effects, Σ3= large unique variances and large structural effects,
and Σ4= small unique variances and large structural effects.


## Page 35


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
35
ε = 0
N = 200
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
ε = 0.03
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
ε = 0.09
β32
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
β
N = 1000
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
Σ1 ML Estimate or Population Param
Σ1 Boundary value
Σ2 ML Estimate or Population Param
Σ2 Boundary value
Σ3 ML Estimate or Population Param
Σ3 Boundary value
G
G
Σ4 ML Estimate or Population Param
Σ4 Boundary value
Population
β21
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
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
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
Figure 2: Fungible contours (deﬁned by δF = .05 ˆF ) of β21 and β32 by sample size N and type of
model; ε= 0 indicates perfect model ﬁt, ε=.03 indicates good model ﬁt, and ε=.09 indicates poor
model ﬁt; Σ1= large unique variances and small structural effects, Σ2= small unique variances
and small structural effects, Σ3= large unique variances and large structural effects, and Σ4=
small unique variances and large structural effects.


## Page 36


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
36
δ1
δ2
δ3
0
0
ε1
ε2
ζ1
ζ2
x1
x2
x3
x4
y1
y2
y3
Attitude
Subjective
Norm
Intention
Trying
1.00
1.00
0.639
0.050
0.486
Figure 3: Path Diagram for Example 1


## Page 37


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
37
Figure 4: Proﬁle likelihood conﬁdence region and fungible parameter contours for the indirect
effect of Attitude on Trying.


## Page 38


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
38
δ1
δ2
δ3
δ4
ε1
ε2
ε3
ε4
ε5
ζ1
x5
x6
x1
x2
x3
x4
y1
y2
y3
y4
y5
Psychological
Well-being
Posttraumatic
Growth
Meaning in
Caregiving
Spirituality
√
0.82
√
0.93
Figure 5: Path Diagram for Example 2. Note. x1 = Self-esteem, x2 = Optimism, x3 = Depression,
x4 = Caregiver Burden, y1 = New Possibilities, y2 = Relating to Others, y3 = Personal Strength,
y4 = Appreciation of Life, and y5 = Spiritual Change.


## Page 39


CONFIDENCE SETS AND FUNGIBLE ESTIMATES
39
Figure 6: Fungible parameter contours for Example 3.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
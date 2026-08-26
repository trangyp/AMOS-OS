---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.01838v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1905.01838v1_Robust_multiple_comparisons_against_a_control_group_with_application_in_toxicolo

> Source: 1905.01838v1_Robust_multiple_comparisons_against_a_control_group_with_application_in_toxicolo.pdf

> Pages: 13

---


## Page 1


arXiv:1905.01838v1  [stat.AP]  6 May 2019
Robust multiple comparisons against a control
group with application in toxicology
Ludwig A. Hothorn
Im Grund 12, D-31867 Lauenau, Germany and
Felix M. Kluxen
ADAMA Deutschland GmbH, D-51149 Cologne, Germany
May 2019


## Page 2


Abstract
The Dunnett procedure compares several treatment or dose groups with a
control group, while controlling the familywise error rate. When deviations
from the normal distribution and heterogeneous variances occur, the nom-
inal α level may be violated, and power may be reduced. Various robust
modiﬁcations are discussed, whereby the novel most likely transformation
(MLT)-Dunnett version is recommended as almost always appropriate by
means of a simulation study. The MLT-Dunnett is especially useful because
it can jointly and comparably analyse diﬀerently scaled endpoints. Further-
more, a related multiple endpoints test is proposed using the odds ratio as
a common eﬀect size. With the statistical software R, the method is readily
applicable using the CRAN libraries multcomp and mlt, real data can be
easily analyzed.


## Page 3


1
Introduction
The Dunnett [3] multiple comparison procedure is commonly used for treat-
ment or dose groups inference against a placebo group in randomized clinical
trials or against negative control in non-clinical studies. This test belongs
to a class of max-t multiple contrast tests for a one way, k-sample design
assuming a common variance estimator S, and a common degree of freedom
df, i.e. N(µi, σ2) [10]. Modiﬁcations in the generalized linear model are avail-
able using a general parametric model [11], particularly for proportions [20],
poly-k estimates in long-term carcinogenicity studies [22], the Cox-model [8]
and multinomial vectors [21].
Multiple deviations from the normal distribution occur frequently and
simultaneously in real data; for example a continuous primary endpoint with
common mildly unbalanced designs, such as radiographical change in joint
space width when treating knee osteoarthritis [19] or hemoglobin change from
baseline when characterizing anemia in chronic kidney disease [17].
Pre-tests on these conditions, such as Kolmogorov-Smirnov test, are not
recommended [4] and therefore robust modiﬁcations are considered in the
current manuscript which are less sensitive to violations of the N(µi, σ2) as-
sumption, i.e. maintain ˆα and show no substantial power loss.
In addition to robustness, there is usually the problem to encounter multiple
diﬀerently scaled endpoints within one bioassay, such as clinical chemistry
endpoints in a 13-week toxicological bioassay with sodium dichromate di-
hydrate administered to F344 rats [2]. It is unrealistic to assume that all
these endpoints follow a certain distribution (like the normal distribution)
or can be converted to it by exactly one transformation (like commonly-used
log transformation). Therefore, a test is needed which evaluates diﬀerently
scaled endpoints fairly comparably using either an independent univariate
analysis or a simultaneous multiple endpoint analysis.
The availability of simultaneous conﬁdence intervals (in addition to compat-
ibly adjusted p-values) should be ensured for any testing procedure, because
estimation procedures are more informative than statistical tests which lead
to a practical limitation of single-step procedures. For example, the ICH E9
guideline states that ’Estimates of treatment eﬀects should be accompanied
by conﬁdence intervals...’.
Five modiﬁcations of the Dunnett test will be compared by the evalua-
tion of a real data example and a simulation study with the original test,
and to each other, particularly considering small sample size design (com-
mon in non-clinical studies, down to ni = 10): i) nonparametric procedure
for relative eﬀect size [14], ii) Dunnett-test using modiﬁed degree of freedom
2


## Page 4


according to Sattherwhaite [5], iii) Dunnett-test using sandwich estimator for
robust variance-covariance estimation [9], iv) robust M-estimator [13], and
v) a novel most likely transformation (MLT) [12].
Of those, the MLT-Dunnett test procedure performs best and can be recom-
mended as being appropriate in conditions that are considered unsuitable for
the original Dunnett test and is more powerful than the published alterna-
tives.
Further, odds ratios (OR) can be used as a common eﬀect size for a Dunnett-
type procedure for both univariate endpoints and correlated multiple and dif-
ferently scaled endpoints, optimally dichotomized for continuous endpoints
by continuous outcome logistic regression (COLR, [16]). The R-code to im-
plement these procedures is given alongside.
2
Robust Dunnett-type procedures
The multiple comparison procedure introduced by Dunnett [3] estimates a
studentized tests statistic assuming normal distributed errors with homoge-
neous variances. Adjusted p-values and/or compatible simultaneous conﬁ-
dence limits are available. The simultaneous conﬁdence intervals (sCI) (2-
sided) of multiple contrast tests are [Pk
i=0 ci¯xi±S∗tq,df,R,2−sided,1−α
qPk
i c2
i /ni]
with the contrast coeﬃcients ci (-1 for the control, 1 for a treated group, 0
otherwise for the Dunnett-test), q the number of multiple contrasts (where
q = k for Dunnett-test), the correlation matrix R = (ρij) (for the Dunnett-
test ρij =
q
1
(1+n0/ni)(1+n0/nj)
(1 ≤i ̸= j ≤k))(may be complex in other sce-
narios [1]). By means of the CRAN R package multcomp [11] these sCIs can
be easily estimated, as well as the compatible, multiplicity-adjusted p-values
derived as an alternative. In the case of variance heterogeneity (particularly
in unbalanced designs), the common degree of freedom df =
Pk
i=0(ni −1)
can be replaced by df Sattherwhaite and ρij depends on the group-speciﬁc vari-
ances estimates [5]. Alternatively, the common variance-covariance can be
estimated via sandwich estimator [9].
Although pairwise-ranking, such as Steel procedure, and joint-ranking, such
as Kruskal-Wallis test are commonly used, a robust approach against viola-
tions of normal distribution and variance homogeneity should be used for the
relative treatment eﬀect between control (0) and treatment i: p0i = Pr(X0 <
Xi) + 1
2Pr(X0 = Xi) =
R F0dFi [14]. The simultaneous conﬁdence intervals
are similar to the parametric standard above, where the correlation matrix
is estimated from sample sizes, contrast coeﬃcients and the sample speciﬁc
variances. An appropriate t-distributed version and a range [0, 1] preventing
transformations can be recommended. A related CRAN R package nparcomp
3


## Page 5


[15] is available. A robust procedure can be achieved by using robust esti-
mators, such as the M estimator [13]. The analysis of quite diﬀerently-scaled
endpoints (including tied, skewed or censored) can be performed by the con-
cept of most likely transformation [12].
The most likely transformation approach is embedded in a maximum like-
lihood framework whereas the parametrization of the monotone increasing
transformation function is achieved by Bernstein polynomials (of order 5 in
the example). For a deeper discussion of this MLT- approach, we refer the
reader to [12]. The object-oriented properties of packages mlt and multcomp
make it easy to estimate corresponding simultaneous Dunnett-type conﬁ-
dence intervals on the assumption of large ni. The R code of all procedures
is available below.
Real data example
Eleven clinical chemistry endpoints from a 13-week
study with sodium dichromate dihydrate administered to F344 rats are used
as an example [2]. In Table 1 multiplicity adjusted p-values for the compari-
son of the medium 250 mg dose versus control of the 11 endpoints are shown,
i.e.
original Dunnett (Dun), M-robust version (Rob), MLT-modiﬁcation
(MLT), non-parametric version (Rel). And, a normal/non-normal decision
based on a Cramer test is given along with each comparison. The endpoint
creatin kinase (CreatK) is interesting: for this non-normal distributed end-
point, the parametric Dunnett-test is non-signiﬁcant, whereas the robust and
the MLT modiﬁcation reveal much smaller p-values. The response against
dose groups in mg/kg bw/d is plotted as a boxplot in Figure ?? and in-
cludes superimposed individual values next to mean and standard deviation.
Note the extreme values in group 62.5 and 1000 mg/kg bw/d, which induce
variance heterogeneity. Although the comparison of interest 250 vs control
reveals no extreme value and no obvious variance heterogeneity, it is not sur-
prising that the Dunnett test reveals a large non-signiﬁcant p-value because
it is a k-sample test with a common mean square error estimator.
The R-code for the ﬁve modiﬁed Dunnett tests for the endpoint CreatK
is:
#### R code for the data example
library("devtools")
install_github("lahothorn/SiTuR")
data("clin", package="SiTuR") # import data example
clin$dose<-as.factor(clin$Dose) # dose as factor
library("mlt"); library("nparcomp")
library("robustbase"); library("ggplot2")
modCK<-lm(CreatKinase~dose, data=clin) # linear model
rmodCK<-lmrob(CreatKinase~dose, data=clin,
setting = "KS2014") # robust M estimators
4


## Page 6


n=10
n=10
n=10
n=10
n=10
n=10
0
400
800
1200
0
62.5
125
250
500
1000
Dose
Outcome
Figure 1: Creatin kinase example
Table 1: Univariate 250 vs. control comparisons: adjusted p-values
Dun
Rob
MLT
Rel
Normal?
Nuc
0.404
0.368
0.240
0.261
yes
BUN
0.040
0.051
0.011
0.018
yes
SerG
0.489
0.410
0.330
0.466
no
CreatK
0.437
0.012
0.010
0.027
no
ALT
0.005
0.001
0.000
0.000
no
SDH
0.015
0.006
0.000
0.000
no
Chol
0.077
0.079
0.026
0.079
yes
Tri
0.001
0.003
0.001
0.029
no
Chlor
0.834
0.679
0.740
0.740
no
Sodium
0.97
0.99
0.97
0.99
yes
Potsa
0.71
0.99
0.91
0.99
no
CDU<-fortify(summary(glht(modCK,
linfct = mcp(dose = "Dunnett"))))# Dunnett test
rCDU<-fortify(summary(glht(rmodCK,
linfct = mcp(dose = "Dunnett")))) # robust Dunnett
yvar <- numeric_var("CreatKinase", support =
quantile(clin$CreatKinase, prob = c(.01, .99))) # MLT
bstorder<-5 # order of Bernstein polynomial
yb <- Bernstein_basis(yvar, ui = "increasing",
order =bstorder) # Bernstein polynomial
ma <- ctm(yb, shifting = ~ dose,
todistr = "Normal", data = clin) # condit transf mod
m_mlt<-mlt(ma, data = clin) # most likely transformation
K <- diag(length(coef(m_mlt))) # contrast matrix
rownames(K) <- names(coef(m_mlt))
matr<-bstorder+1
K <- K[-(1:matr),] # for order 5 Bernstein
C<-glht(m_mlt, linfct = K) # MLT-Dunnett-type test
CMLT<-fortify(summary(C))
NPC<-nparcomp(CreatKinase~dose, data=clin,
asy.method = "probit", alternative = "two.sided",
type = "Dunnett",plot.simci = FALSE,
info = FALSE)$Analysis$p.Value # relat effects
pCK<-cbind(CDU[, c(1,6)], rCDU[, 6], CMLT[, 6], NPC)
5


## Page 7


The object pCK contains the multiplicity-adjusted p-values for the mod-
iﬁed Dunnett-tests. Notice, instead of the asymptotic version, for the com-
mon small sample sizes designs, a t-distributed maximum test can be recom-
mended, simply by using the degree of freedom of the linear model
sC<-glht(m_mlt, linfct = K, df=modCK$df.residual). For both randomized clinical trials
and toxicological bioassays a directional evaluation, i.e. one-sided conﬁdence
limits (or compatible adjusted p-values) are appropriate and available.
A continuous outcome logistic regression approach
In addition to
robustness, there is usually the problem to encounter multiple diﬀerently
scaled endpoints within one bioassay: normally distributed (such as body
weight), skewed distributed (such as ASAT), dichotomous (such as tumor
rate), ordered categorized (such as graded pathological ﬁndings), etc. Usu-
ally diﬀerent test principles are used, such as parametric, nonparametric
and those for proportions. An alternative is the comparable evaluation of
diﬀerently scaled endpoints with an approach that uses an uniform eﬀect
size. Continuous outcome logistic regression (COLR) [16] provides the di-
mensionless odd ratios (and their conﬁdence intervals) as eﬀect size optimally
dichotomized for the endpoint speciﬁc distribution (any continuous, any dis-
crete up to binary, censored etc.) as well as taking also the higher moments
(location, scale and shape) into account. This approach is similar to a speciﬁc
version of most likely transformation (MLT) with the distribution function
argument logistic [12] whereas the CRAN package tram is used here. Against
a recommendation for a routine use speaks its problematic small sample size
characteristics of this asymptotic procedure. A Dunnett-type test for the
non-normal distributed endpoint creatine kinase is shown as an example:
data("clin", package="SiTuR") # import data example
clin$dose<-as.factor(clin$Dose) # defining dose as factor
library("tram")
COC<-Colr(CreatKinase~dose, data=clin) # COLR
CC<-glht(COC, linfct = diag(length(coef(COC))))
ccMLT<-1/exp(confint(CC)$confint)# OR and sCI
summary(CC)$test$pvalue # adj.p-value
The odds ratios versus control together with their lower simultaneous
conﬁdence limits and the adjusted p-values are given in Table 2:
The chance of increased creatine kinase levels in the 250 mg/kg dose
group is at least 1.4 times higher compared to control, which is an eﬀect size
representation equivalent to the p-value of 0.016.
6


## Page 8


Table 2: Dunnett-type continuous outcome logistic regression
Comparison
OR
lower limit
adj. p-value
62.5/0
3
0.4
0.5
125/0
6
0.8
0.11
250/0
12
1.4
0.016
500/0
52
5.3
0.0001
1000/0
98
9.7
0.000002
Joint analysis of multiple correlated and diﬀerently-scaled end-
points
To limit false positive claims it can be helpful to conduct a joint
analysis of multiple endpoints considering their correlations and dimension
k. A related Dunnett-type test assuming multivariate normality and vari-
ance homogeneity [6] and variance heterogeneity [7] is available. A multiple
endpoint approach based on the unique eﬀect size odds ratio for diﬀerently
scaled endpoints is proposed here. The joint distribution of the underlying
Tmax-test [6] is achieved by multiple marginal model approach [18], which
allows maximum tests on multiple linear models without the explicit formula-
tion of the correlation matrix. The variance-covariance matrix of parameter
estimates can be obtained using derivatives of the log-likelihood function
in a single endpoint model, and hence for multiple models a vector of log-
likelihood functions is used. By plugging in parameter estimates, a consistent
sandwich estimator of the variance-covariance matrix is obtained, i.e. the em-
pirical covariance based on functions of the data, not on the data itself. A
related function mmm is available with the R package multcomp [11]. From the
above clinical chemistry example, the bivariate case of creatine kinase and
the right-skewed distributed alanine aminotransferase (ALT) is selected:
yCK <- numeric_var("CreatKinase", support =
quantile(clin$CreatKinase, prob = c(.01, .99)))
yAL <- numeric_var("ALT", support =
quantile(clin$ALT, prob = c(.01, .99)))
bstorder<-5 # order of Bernstein polynomial
yC <- Bernstein_basis(yCK, ui = "increasing",
order =bstorder) # Bernstein polynomial
yA <- Bernstein_basis(yAL, ui = "increasing",
order =bstorder) # Bernstein polynomial
mC <- ctm(yC, shifting = ~ dose,todistr = "Logistic",
data = clin) # condit. transf. model
mC_mlt<-mlt(mC, data = clin) # most likely transformation
K <- diag(length(coef(mC_mlt))) # contrast matrix
rownames(K) <- names(coef(mC_mlt))
matr<-bstorder+1
K <- K[-(1:matr),] # matrix for order 5 Bernstein
C<-glht(mC_mlt, linfct = K) # MLT-Dunnett-type test
CMLT<-fortify(summary(C))
mA <- ctm(yA, shifting = ~ dose,todistr = "Logistic",
data = clin) # condit transf mod
7


## Page 9


mA_mlt<-mlt(mA, data = clin) # most likely transformation
A<-glht(mA_mlt, linfct = K) # MLT-Dunnett-type test
AMLT<-fortify(summary(A))
MMMDF <- c(mC_mlt$df, mA_mlt$df)
conLH <- diag(2)%x%K # contrast matrix for bivar Dunnett
bread.mlt_fit <- function(x) vcov(x) * nrow(x$data) # sandwich
MMn <-summary(glht(mmm(mC_mlt, mA_mlt),
linfct=conLH, df=mean(MMMDF)))
The related adjusted p-values (adjusted against multiple comparisons ver-
sus control and the two correlated endpoints) are are presented in Table 3:
Table 3: Adjusted p-values bivariate MLT-Dunnett
Hypothesis
Lower limit OR
p-value
Creatin: 62.5/0
0.2
0.6922
Creatin: 125/0
0.5
0.2354
Creatin: 250/0
0.8
0.0699
Creatin: 500/0
3.0
0.0069
Creatin: 1000/0
5.8
0.0023
ALT: 62.5/0
91.5
0.0004
ALT: 125/0
9.7
0.0028
ALT: 250/0
15.0
0.0016
ALT: 500/0
10.9
0.0023
ALT: 1000/0
18.2
0.0013
As expected, the multiplicity-adjusted p-values of the bivariate analysis
are increased compared to the univariate analysis (just as the lower limit
is decreased analogously). This is the necessary penalty for a claim accross
multiple endpoints, which increases with the number of considered endpoints
and with lower correlations. Thus, a careful selection of relevant endpoints
is suggested for a follow-up multivariate analysis.
3
Simulations
In a simulation study, the empirical size bα under the null hypothesis (H0) and
the empirical power under the alternative hypothesis (H1) of the following
Dunnett-type procedures are compared (in 10000 runs): i) original [3] (Dun),
ii) adjusted for variance heterogeneity by sandwich estimator [8] (SaW), iii)
adjusted for variance heterogeneity by reduced df (Sat), [5], iv) robust linear
model [13] (Rob), v) most likely transformation [12] (MLT), vi) pairwise-
ranking Steel test [23] (Ste), vii) nonparametric multiple contrast test [15]
(Rel). The expected values and variances are chosen similar to the endpoint
8


## Page 10


cholesterol in the example study whereas a balanced and unbalanced design
with a control and three dose groups with small sample sizes (ni = 10)
were considered for normal distribution (N) and a skewed distribution (M),
which consist of a mixture of 10% and 20% extreme high values respectively,
parametrized by variance inﬂation factor of ξ.
The results of the simulation study are shown in Table 4. Under the
null-hypothesis the empirical α levels should be near the the nominal level
of 0.05: too large values (liberal behavior) are a sign against the validity of a
level α-test, too small values indicates a conservative behavior, which leads
to undesirable high false negative rate in safety assessment. The power of a
test must and cannot be maximal in every situation examined, but it should
be uniformly high.
Table 4: Simulation results: bα and power
Hyp
ξ
n1
n4
Dun
Sat
SaW
Rob
MLT
Ste
Rel
N,H0
1
10
10
0.05
0.03
0.08
0.06
0.06
0.04
0.03
H0
2
10
10
0.04
0.03
0.08
0.06
0.07
0.04
0.03
H0
3
10
10
0.04
0.02
0.07
0.05
0.05
0.04
0.04
H0
4
10
10
0.03
0.03
0.06
0.04
0.06
0.03
0.03
H1
1
10
10
0.84
0.79
0.89
0.86
0.85
0.70
0.74
H1
2
10
10
0.75
0.69
0.81
0.79
0.77
0.63
0.65
H1
3
10
10
0.65
0.58
0.69
0.72
0.70
0.57
0.56
H1
4
10
10
0.52
0.47
0.58
0.71
0.63
0.51
0.47
H0
1
20
10
0.04
0.03
0.07
0.06
0.05
0.04
0.04
H0
4
20
10
0.06
0.03
0.06
0.06
0.06
0.04
0.04
H1
1
20
10
0.94
0.92
0.94
0.94
0.95
0.90
0.88
H1
4
20
10
0.73
0.67
0.65
0.84
0.78
0.72
0.62
H0
1
5
20
0.04
0.02
0.11
0.05
0.05
0.03
0.05
H0
4
5
20
0.02
0.00
0.11
0.05
0.04
0.03
0.06
H1
1
5
20
0.64
0.47
0.79
0.67
0.70
0.50
0.63
H1
4
5
20
0.36
0.22
0.67
0.63
0.57
0.41
0.56
M,H0
1
20
10
0.09
0.07
0.09
0.16
0.08
0.06
0.06
H0
2
20
10
0.09
0.07
0.08
0.20
0.07
0.04
0.05
H0
3
20
10
0.13
0.10
0.09
0.22
0.09
0.07
0.05
H0
4
20
10
0.13
0.09
0.07
0.20
0.07
0.06
0.05
H1
1
20
10
0.71
0.68
0.57
0.74
0.65
0.51
0.34
H1
2
20
10
0.63
0.57
0.44
0.69
0.53
0.43
0.26
H1
3
20
10
0.52
0.47
0.33
0.64
0.44
0.37
0.22
H1
4
20
10
0.46
0.40
0.26
0.61
0.39
0.34
0.19
H0
1
5
20
0.00
0.00
0.10
0.02
0.01
0.00
0.04
H0
4
5
20
0.00
0.00
0.09
0.02
0.01
0.00
0.05
H1
1
5
20
0.31
0.19
0.59
0.41
0.32
0.21
0.41
H1
4
5
20
0.10
0.05
0.41
0.35
0.20
0.15
0.34
The simulations show that the problematic conservative behavior with
increasing variance heterogeneity only occurs when ni < n0. As expected,
the asymptotic tests (SaW, MLT) reveal a liberal behavior for the small ni,
common in toxicology. Increasing variance in the high dose group causes a
problematic power loss, which is still lowest at MLT. For rarely used designs
with n0 < ni Dun and Sat are extremely conservative (connected with power
loss). As expected for mixing distribution, a substantial power loss occurs
which is extreme for Rel. Even from a size/power perspective, MLT is an
almost always appropriate test.
9


## Page 11


4
Discussion
Multiple deviations from the normal distribution occur frequently and si-
multaneously in real data. This is often caused by extreme single values and
heterogeneous variances and may be complicated by unbalanced designs. In
these cases, the Dunnett procedure, which is recommended in many guide-
lines, can react with size violation, i.e. deviation from the nominal alpha,
and/or power loss.
There are two strategies to address this. Common is an application of
so-called assumption/pre- tests, which are subsequently used in a decision
tree-like procedure. There are several issues with this approach, see for de-
tails [4]. One major disadvantage is the use of diﬀerent test types in the ﬁnal
main analysis, for which eﬀect sizes and estimates are not present or compa-
rable. Another problem is that the main test alternatives do not necessarily
address the issues identiﬁed by the pre-tests, e.g. heterogeneous variances.
The method presented in this manuscript allows the application of a ro-
bust test, i.e. a common and comparable analysis for multiple endpoints,
which is applicable even when deviations from the Dunnett test assump-
tions occur. Various robust modiﬁcations have been compared, whereby the
MLT-version is recommended as almost always appropriate. As shown in a
simulation study, all procedures considered are problematic for very small ni,
especially for unbalanced designs (e.g. the common n0 > ni ) and variance
heterogeneity- both due to insuﬃcient power and non-maintenance of the
intended α level. While the MLT-Dunnett performed best in conditions of
the simulation study, no suitable test was identiﬁed for common small sam-
ple designs, and accordingly statistical signiﬁcance needs to be considered
cautiously in the absence of biological relevance.
We showed the application of the MLT-Dunnett in real data examples,
namely the derivation of p-values and eﬀect sizes. Its performance has been
compared in a simulation study with the original Dunnett test and its various
published alternatives and modiﬁcations.
The modiﬁcation of using continuous outcome logistic regression (COLR)
allows the comparison of common odds ratios over diﬀerently scaled end-
points, which is a clear advantage to using diﬀerent main tests for those
endpoints. Since such endpoints usually occur together in toxicological bioas-
says, this procedure might be helpful to assess a toxic response in more detail
and coherence. The application of multiple marginal models allows simulta-
neous claims over several correlated endpoints, which allows a more reﬁned
statistical, and by the use of odds ratios, toxicological assessment of corre-
lated eﬀects. The current practice in toxicology is to statistically compare
each endpoint within one bioassay in isolation and thus consciously ignoring
10


## Page 12


known correlations while accepting size violation along with increased rate
of false positive claims.
Together, the MLT-Dunnett can be recommended to be used in toxicology
especially because several, diﬀerently scaled endpoints can be analyzed com-
parably and jointly as a multiple endpoint test. Both adjusted p-values and
simultaneous conﬁdence intervals are available for all procedures, although
some of the latter can no longer be interpreted on the clinical scale. With the
CRAN libraries multcomp, tram and mlt, real data can be easily analyzed
with this method.
References
[1] Hothorn, L.A. Statistics in Toxicology-using R (2015).
[2] National Toxicology Program. 13 Weeks gavage study on female F344 rats adminis-
tered with Sodium dichromate dihydrate (VI) (CASRN: 7789-12-0, Study Number:
C20114,TDMS Number:2011402.
[3] C. W. Dunnett. A multiple comparison procedure for comparing several treatments
with a control. J Am Stat Assoc, 50(272):1096–1121, 1955.
[4] Kluxen F.M. and Hothorn L.A. A generic procedure to conduct statistical testing as
an alternative to decision trees in regulatory (eco-) toxicological bioassays. ArchTox
(to be submitted), 2019.
[5] M. Hasler and L. A. Hothorn. Multiple contrast tests in the presence of heteroscedas-
ticity. Biometrical Journal, 50(5):793–800, October 2008.
[6] M. Hasler and L. A. Hothorn.
A dunnett-type procedure for multiple endpoints.
International Journal of Biostatistics, 7(1):3, 2011.
[7] M. Hasler and L. A. Hothorn. Multi-arm trials with multiple primary endpoints and
missing values. Statistics in Medicine, 37(5):710–721, February 2018.
[8] E. Herberich and L.A. Hothorn.
Statistical evaluation of mortality in long-term
carcinogenicity bioassays using a Williams-type procedure.
Regul Toxicol Pharm,
64:26–34, 2012.
[9] E. Herberich, J. Sikorski, and T. Hothorn. A robust procedure for comparing multiple
means under heteroscedasticity in unbalanced designs. Plos One, 5(3):e9788, March
2010.
[10] L. A. Hothorn. How to deal with multiple treatment or dose groups in randomized
clinical trials? Fundam Clin Pharm, 21(2):137–154, 2007.
[11] T. Hothorn, F. Bretz, and P. Westfall. Simultaneous inference in general parametric
models. Biometrical J, 50(3):346–363, 2008.
[12] T. Hothorn, L. Most, and P. Buhlmann. Most likely transformations. Scandinavian
Journal of Statistics, 45(1):110–134, March 2018.
11


## Page 13


[13] M. Koller and W. A. Stahel. Sharpening wald-type inference in robust regression for
small samples. Computational Statistics & Data Analysis, 55(8):2504–2515, August
2011.
[14] F. Konietschke and L.A. Hothorn. Rank-based multiple test procedures and simul-
taneous conﬁdence intervals. Electron J Stat, 6:738–759, 2012.
[15] F. Konietschke, M. Placzek, F. Schaarschmidt, and L.A. Hothorn. nparcomp: An
R software package for nonparametric multiple comparisons and simultaneous conﬁ-
dence intervals. Journal of Statistical Software, 64(9):1–17, 2015.
[16] T Lohse, S Rohrmann, D Faeh, and T Hothorn. Continuous outcome logistic regres-
sion for analyzing body mass index distributions. F1000Research, 2017, 6:1933 (doi:
10.12688/f1000research.12934.1).
[17] E. R. Martin, M. T. Smith, B. J. Maroni, Q. C. Zuraw, and E. M. deGoma. Clinical
trial of vadadustat in patients with anemia secondary to stage 3 or 4 chronic kidney
disease. American Journal of Nephrology, 45(5):380–388, 2017.
[18] Christian Bressen Pipper, Christian Ritz, and Hans Bisgaard. A versatile method for
conﬁrmatory evaluation of the eﬀects of a covariate in multiple models. Journal of
the Royal Statistical Society Series C-applied Statistics, 61:315–326, 2012.
[19] J. Y. Reginster, J. Badurski, N. Bellamy, W. Bensen, R. Chapurlat, X. Chevalier,
C. Christiansen, H. Genant, F. Navarro, E. Nasonov, P. N. Sambrook, T. D. Spector,
and C. Cooper. Extended report eﬃcacy and safety of strontium ranelate in the treat-
ment of knee osteoarthritis: results of a double-blind, randomised placebo-controlled
trial. Annals of the Rheumatic Diseases, 72(2):179–186, February 2013.
[20] F. Schaarschmidt, E. Biesheuvel, and L. A. Hothorn. Asymptotic simultaneous con-
ﬁdence intervals for many-to-one comparisons of binary proportions in randomized
clinical trials. Journal of Biopharmaceutical Statistics, 19(2):292–310, 2009.
[21] F. Schaarschmidt, D. Gerhard, and C. Vogel. Simultaneous conﬁdence intervals for
comparisons of several multinomial samples. Computational Statistics & Data Anal-
ysis, 106:65–76, February 2017.
[22] F. Schaarschmidt, M. Sill, and L. A. Hothorn. Poly-k-trend tests for survival adjusted
analysis of tumor rates formulated as approximate multiple contrast test. J Biopharm
Stat, 18(5):934–948, 2008.
[23] R. G. D. Steel. A multiple comparison rank sum test - treatments versus control.
Biometrics, 15(4):560–572, 1959.
Acknowledgment: We thank Prof. Dr. Torsten Hothorn (University of Zurich) for the
speciﬁc instruction for the packages mlt and tram to use for multiple contrast tests.
12

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
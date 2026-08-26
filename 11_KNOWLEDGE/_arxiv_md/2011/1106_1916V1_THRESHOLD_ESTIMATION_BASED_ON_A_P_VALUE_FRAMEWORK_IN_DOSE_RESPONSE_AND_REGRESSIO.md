---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1106.1916v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1106.1916v1_Threshold_estimation_based_on_a_p-value_framework_in_dose-response_and_regressio

> Source: 1106.1916v1_Threshold_estimation_based_on_a_p-value_framework_in_dose-response_and_regressio.pdf

> Pages: 23

---


## Page 1


arXiv:1106.1916v1  [stat.ME]  9 Jun 2011
THRESHOLD ESTIMATION BASED ON A p-VALUE FRAMEWORK IN
DOSE-RESPONSE AND REGRESSION SETTINGS
A. MALLIK, B. SEN, M. BANERJEE, AND G. MICHAILIDIS
ABSTRACT. We use p-values to identify the threshold level at which a regression function
takes off from its baseline value, a problem motivated by applications in toxicological and
pharmacological dose-response studies and environmental statistics. We study the problem
in two sampling settings: one where multiple responses can be obtained at a number of dif-
ferent covariate-levels and the other the standard regression setting involving limited number
of response values at each covariate. Our procedure involves testing the hypothesis that the
regression function is at its baseline at each covariate value and then computing the poten-
tially approximate p-value of the test. An estimate of the threshold is obtained by ﬁtting a
piecewise constant function with a single jump discontinuity, otherwise known as a stump,
to these observed p-values, as they behave in markedly different ways on the two sides of the
threshold. The estimate is shown to be consistent and its ﬁnite sample properties are studied
through simulations. Our approach is computationally simple and extends to the estimation
of the baseline value of the regression function, heteroscedastic errors and to time-series. It
is illustrated on some real data applications.
1. INTRODUCTION
In a number of applications, the data follow a regression model where the regression func-
tion µ is constant at its baseline value τ0 up to a certain covariate threshold d0 and deviates
signiﬁcantly from τ0 at higher covariate levels. For example, consider the data shown in the
left panel of Fig. 1. It depicts the physiological response of cells from the IPC-81 leukemia
rat cell line to a treatment, at different doses; more details are given in Section 3.2. The
objective here is to study the toxicity in the cell culture to assess environmental hazards. The
function stays at its baseline value for high dose levels which corresponds to the dose becom-
ing lethal, and then takes off for lower doses, showing response to treatment. This problem
requires procedures that can identify the change-point in the regression function, namely
where it deviates from the baseline value. The threshold is of interest as it corresponds to
maximum safe dose level beyond which cell cultures stop responding. Similar problems also
arise in other toxicological applications (Cox, 1987).
1


## Page 2


2
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
1
2
3
4
5
6
7
−0.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Log(dose)
Response
400
450
500
550
600
650
700
750
−1
−0.8
−0.6
−0.4
−0.2
0
Range
logratio
1850
1880
1910
1940
1970
2000
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
Year
Temperature Anomalies
FIGURE 1. The three data examples. Left panel: Response of cell-cultures
at different doses. Middle panel: Logratio measurements over range. Right
panel: Annual global temperature anomalies from 1850 to 2009.
Problems with similar structure also arise in other pharmacological dose-response stud-
ies, where µ(x) quantiﬁes the response at dose-level x and is typically at the baseline value
up to a certain dose, known as the minimum effective dose; see Chen & Chang (2007) and
Tamhane & Logan (2002) and the references therein. In such applications, the number of
doses or covariate levels is relatively small, say up to 20, and many procedures proposed
in the literature are based on testing ideas (Tamhane & Logan, 2002; Hsu & Berger, 1999).
However, in other application domains, the number of doses can be fairly large compared
to the number of replicates at each dose. The latter is effectively the setting of a standard
regression model. In the extreme case, there is a single observation per covariate level. Data
from such a setting are shown in the middle panel of Fig. 1, depicting the outcome of a light
detection and ranging experiment, used to detect the change in the level of atmospheric pollu-
tants. This technique uses the reﬂection of laser-emitted light to detect chemical compounds
in the atmosphere (Holst et al., 1996; Ruppert et al., 1997). The predictor variable, range,
is the distance traveled before the light is reﬂected back to its source, while the response
variable, logratio, is the logarithm of the ratio of received light at two different frequencies.
The negative of the slope of the underlying regression function is proportional to mercury
concentration at any given value of range. The point at which the function falls from its
baseline level corresponds to an emission plume containing mercury and, thus, is of interest.
An important difference between these two examples is that the former provides the luxury
of multiple observations at each covariate level, while the latter does not.
Another relevant application in a time-series context is given in the right panel of Fig. 1,
where annual global temperature anomalies are reported from 1850 to 2009. The study of
such anomalies, temperature deviations from a base value, has received much attention in the
context of global warming from both the scientiﬁc as well as the general community (Melillo,


## Page 3


THRESHOLD ESTIMATION
3
1999; Delworth and Knutson, 2000). The ﬁgure suggests an initial ﬂat stretch followed by
a rise in the function. Detecting the advent of global warming, which is the threshold, is of
interest here. While we take advantage of the independence of errors in the previous two
datasets, this application has an additional feature of short range dependence which needs to
be addressed appropriately.
Formally, we consider a function µ(x) on [0, 1] with the property that µ(x) = τ0 for x ≤d0
and µ(x) > τ0 for x > d0 for some d0 ∈(0, 1). As already mentioned, quantities of prime
interest are d0 and τ0 that need to be estimated from realizations of the model Y = µ(X)+ǫ.
We call d0 the τ0 threshold of the function µ. Here τ0 is the global minimum for the function
µ. To ﬁx ideas, we work only with this setting in mind. The methods proposed can be easily
imitated for the ﬁrst data application where the baseline stretch is on the right as well as for
the second data application where τ0 is the maximum.
In this generality, i.e., without any assumptions on the behavior of the function in a neigh-
borhood of d0, the estimation of the threshold d0 has not been extensively addressed in the
literature. In the simplest possible setting of the problem posited, µ has a jump discontinuity
at d0. In this case, d0 corresponds to a change-point for µ and the problem reduces to esti-
mating this change-point. Such models are well studied; see Mueller (1992), Loader (1996),
Koul & Qian (2002), Pons (2003), Lan et al. (2009), Pons (2009) and the references therein.
Results on estimating a change-point in a density can be found in Ibragimov & Khasminskii
(1982).
The problem becomes signiﬁcantly harder when µ is continuous at d0; in particular, the
smoother µ is in a neighborhood of d0, the more challenging the estimation. If d0 is a cusp
of µ of some known order p, i.e., the ﬁrst p−1 right derivatives of µ at d0 equal 0 but the p-th
does not, so that d0 is a change-point in the p-th derivative, one can obtain nonparametric
estimates for d0 using either kernel based (Mueller, 1992) or wavelet based (Raimondo,
1998) methods. If the degree of differentiability of µ at d0 is not known, this becomes an
even harder problem. In fact, it was pointed out to us by one of the referees that if p is
unknown then there is no method for which the estimate, ˆd, will be uniformly consistent,
i.e., for any ǫ > 0, supµ Pµ{| ˆd−d0| > ǫ} →0. Here, the supremum is taken over all choices
of µ with a τ0 threshold at d0.
This paper develops a novel approach for the consistent estimation of d0 in situations
where single or multiple observations can be sampled at a given covariate value. The devel-
oped nonparametric methodology relies on testing for the value of µ at the design values of
the covariate. The obtained test statistics are then used to construct p-values which, under


## Page 4


4
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
mild assumptions on µ, behave in markedly different manner on either side of the threshold
d0 and it is this discrepancy that is used to construct an estimate of d0. The approach is
computationally simple to implement and does not require knowledge of the smoothness of
µ at d0. In a dose-response setting involving several doses and large number of replicates per
dose, the p-values are constructed using multiple observations at each dose. The approach
is completely automated and does not require the selection of any tuning parameter. In the
case of limited or even single observation at each covariate value, referred to as the stan-
dard regression setting in this paper, the p-values are constructed by borrowing information
from neighboring covariate values via smoothing which only involves selecting a smoothing
bandwidth. The ﬁrst data application falls under the dose-response setting and the other two
examples fall under the standard regression regime. We establish consistency of the proposed
procedure in both settings.
An estimate of µ, say ˆµ, by itself, fails to offer a satisfactory solution for estimating d0.
Naive estimates, using ˆµ, may be of the form ˆd(1) = sup{x : ˆµ(x) ≤τ0} or ˆd(2) = inf{x :
ˆµ(x) > τ0}. The estimator ˆd(1) performs poorly when µ is not monotone, and is close to
τ0 at values to the far right of d0, e.g., when µ is tent-shaped. Also, ˆd(2), by itself, is not
consistent and one would typically need to substitute τ0 with a τ0 + ηn, with ηn →0 at an
appropriate rate, to attain consistency. In contrast, our approach does not need to introduce
such exogenous parameters.
2. FORMULATION AND METHODOLOGY
2.1. Problem Formulation. Consider a regression model Y = µ(X) + ǫ, where µ is a
function on [0, 1] and
µ(x) = τ0 (x ≤d0), µ(x) > τ0 (x > d0),
(1)
for d0 ∈(0, 1), with an unknown τ0 ∈R. The covariate X is sampled from a Lebesgue
density f on [0, 1] and E(ǫ | X = x) = 0, σ2(x) = var(ǫ | X = x) > 0 for x ∈
[0, 1]. We assume that f is continuous and positive on [0, 1] and µ is continuous. No further
assumptions are made on the behavior of µ, especially around d0. We have the following
realizations:
Yij = µ(Xi) + ǫij (i = 1, . . . , n; j = 1, . . . , m),
(2)
with N = m × n being the total budget of samples. The ǫijs are independent given X
and distributed like ǫ and the Xis are independent realizations from f. Also, (2) with m =


## Page 5


THRESHOLD ESTIMATION
5
1 corresponds to the usual regression setting which simply has only one response at each
covariate level.
We construct consistent estimates of d0 under dose-response and standard regression set-
tings. In the dose-response setting, we allow both m and n to be large and construct p-values
accordingly. We refer to the corresponding approach as Method 1 from now on. In the other
setting, we consider the case when m is much smaller compared to n and extend our ap-
proach through smoothing. We refer to this extension as Method 2, which requires choosing
a smoothing bandwidth. The two methods rely on the same dichotomous behavior exhibited
by the approximate p-values, although constructed differently.
2.2. Dose-Response Setting (Method 1). We start by introducing some notation. Let ¯Yi· =
Pm
i=1 Yij/m and x ∈(0, 1) denote a generic value of the covariate. Let ˆσm,n ≡ˆσ and
ˆτm,n ≡ˆτ denote the estimators of σ(·) and τ0 respectively. For homoscedastic errors, ˆσm,n(·)
is the standard pooled estimate, i.e., ˆσ2
m,n(x) ≡P
i,j(Yij −¯Yi·)2/(nm −m), while for the
heteroscedastic case ˆσ2
m,n(Xi) = Pm
j=1(Yij−¯Yi·)2/(m−1). Estimators of τ0 are discussed in
Section 2.4. We seek to estimate d0 by constructing p-values for testing the null hypothesis
H0,x : µ(x) = τ0 against the alternative H1,x : µ(x) > τ0 at each dose Xi = x. The
approximate p-values are
pm,n(Xi) = pm,n(Xi, ˆτm,n) = 1 −Φ{m1/2( ¯Yi· −ˆτ)/ˆσ(Xi)}.
Indeed, these approximate p-values would correspond to the exact p-values for the uniformly
most powerful test if we worked with a known σ, a known τ and normal errors.
To the left of d0, the null hypothesis holds and these approximate p-values converge
weakly to a Uniform(0,1) distribution, for suitable estimators of τ0. In fact, the distribu-
tion of pm,n(Xi)s does not even depend on Xi when Xi ≤d0. Moreover, to the right of d0,
where the alternative is true, the p-values converge in probability to 0. This dichotomous
behavior of the p-values on either side of d0 can be used to prescribe consistent estimates of
the latter. We can ﬁt a stump, a piecewise constant function with a single jump discontinuity,
to the pm,n(Xi)s, i = 1, . . . , n, with levels 1/2, which is the mean of a Uniform (0,1) random
variable, and 0 on either side of the break-point and prescribe the break-point of the best
ﬁtting stump (in the sense of least squares) as an estimate of d0. Formally, we ﬁt a stump of
the form ξd(x) = (1/2)1(x ≤d), minimizing
˜Mm,n(d) = ˜Mm,n(d, ˆτ) =
X
i:Xi≤d
{pm,n(Xi) −1/2}2 +
X
i:Xi>d
{pm,n(Xi)}2
(3)


## Page 6


6
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
over d ∈[0, 1]. Let ˆdm,n = arg mind∈[0,1] ˜Mm,n(d). The success of our method relies
on the fact that the pm,n(Xi)s eventually show stump like dichotomous behavior. In this
context, no estimate of µ could exhibit such a behavior directly. Our procedure can be
thought of as ﬁtting the limiting stump model to the observed pm,n(Xi)s by minimizing an
L2 norm. In fact, the expression in (3) can be simpliﬁed, and it can be seen that ˆdm,n =
arg maxd∈[0,1] Mm,n(d), where Mm,n(d) = n−1 P
i:Xi≤d {pm,n(Xi) −1/4} . The estimate
can be computed easily via a simple search algorithm as it is one of the order statistics.
In heteroscedastic models, the estimation of the error variance ˆσ(·) can often be tricky. The
proposed procedure can be modiﬁed to avoid the estimation of the error variance altogether
for the construction of the p-values, as the desired dichotomous behavior of the p-values
is preserved even when we do not normalize by the estimate of the variance. Thus, we
can consider the modiﬁed p-values ˜pm,n(Xi) = 1 −Φ{m1/2( ¯Yi· −ˆτ)} and the dichotomy
continues to be preserved as E{1 −Φ(Z)} = 0.5 for a normally distributed Z with zero
mean and arbitrary variance. In practice though, we recommend, whenever possible, using
the normalized p-values as they exhibit good ﬁnite sample performance.
Next, we prove the consistency of our proposed procedure when using the unnormalized
p-values. The technique illustrated here can be carried forward to prove consistency for
other variants of the procedure, e.g., when normalizing by the estimate of the error vari-
ance, but require individual attention depending upon the assumption of heteroscedastic-
ity/homoscedasticity.
Theorem 1. Consider the dose-response setting of the problem and let ˆdm,n denote the esti-
mator based on the non-normalized version of p-values, e.g., ˜pm,n(Xi) = 1 −Φ{m1/2( ¯Yi· −
ˆτ)}. Assume that m1/2(ˆτm,n −τ0) = op(1) as m, n →∞, i.e., given ǫ, η > 0, there
exists a positive integer L, such that for m, n ≥L, P(m1/2|ˆτ −τ0| > ǫ) < η. Then,
ˆdm,n −d0 = op(1) as m, n →∞.
2.3. Standard Regression Setting (Method 2). We now consider the case when m is much
smaller than n.
Let ˆµ(x) = ˆr(x)/ ˆf(x) denote the Nadaraya–Watson estimator, where
ˆr(x) = (nhn)−1Pn
i=1 ¯Yi·K {h−1
n (x −Xi)} and ˆf(x) = (nhn)−1Pn
i=1 K

hn
−1(x −Xi)
	
,
with K being a symmetric probability density or simply a kernel and hn the smoothing
bandwidth. We take hn = cn−β for β ∈(0, 1). Let ˆσn(·) and ˆτn denote estimators of σ(·)
and τ0 respectively. An estimate of σ2(·) can be constructed through standard techniques,
e.g., smoothing or averaging the squared residuals m{ ¯Yi· −ˆµ(Xi)}2, depending upon the
assumption of heteroscedastic or homoscedastic errors.


## Page 7


THRESHOLD ESTIMATION
7
For x < d0, the statistic T(x, τ0) = (nhn)1/2(ˆµ(x)−τ0) converges to a normal distribution
with zero mean and variance V 2(x) = σ2(x) ¯K2/{mf(x)} with ¯K2 =
R
K2(u)du. The
approximate p-value for testing H0,x against H1,x can then be constructed as:
pn(x) = pn(x, ˆτn) = 1 −Φ
n
T(x, ˆτn)/ ˆVn(x)
o
,
where ˆV 2
n (x) = ˆσ2
n(x) ¯K2/{m ˆf(x)}. It can be seen that these p-values also exhibit the
desired dichotomous behavior. Finally, an estimate of d0 is obtained by maximizing
Mn(d) = (1/n)
X
i:Xi≤d
{pn(Xi) −1/4}
(4)
over d ∈[0, 1]. Let ˆdn = arg maxd∈[0,1] Mn(d). Under suitable conditions on ˆτn, this
estimator can be shown to be consistent when n grows large.
We have avoided sophisticated means of estimating µ(·), as our focus is on estimation
of d0, and not particularly on efﬁcient estimation of the regression function. Also, the
Nadaraya–Watson estimate does not add substantially to the computational complexity of
the problem and provides a reasonably rich class of estimators through choices of band-
widths and kernels.
In many applications, particularly when m = 1 and under heteroscedastic errors, estimat-
ing the variance function σ2(·) accurately could be cumbersome. As with Method 1, Method
2 can also be modiﬁed to avoid estimating the error variance, e.g., the estimator constructed
using (4), based on ˜pn(Xi)s, with ˜pn(x) = 1 −Φ

(nhn)1/2(ˆµ(x) −ˆτn)
	
. Next, we prove
consistency for the proposed procedure when we do not normalize by the estimate of the vari-
ance. The technique illustrated here can be carried forward to prove consistency for other
variants of the procedure. We make the following additional assumptions.
(a) For some η > 0, the functions σ2(·) and σ(2+η)(x) ≡E(|ǫ|2+η | X = x), x ∈[0, 1],
are continuous.
(b) The kernel K is either compactly supported or has exponentially decaying tails,
i.e., for some C, D and a > 0, and for all sufﬁciently large x, P{|W| > x} ≤
C exp(−Dxa), where W has density K. Also, ¯
K2 =
R
K2(u)du < ∞.
Assumption (a) is very common in non-parametric regression settings for justifying asymp-
totic normality of kernel based estimators. Also, the popularly used kernels, namely uniform,
Gaussian and Epanechnikov, do satisfy assumption (b).


## Page 8


8
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
Theorem 2. Consider the standard regression setting of the problem with m staying ﬁxed
and n →∞. Assume that (nhn)1/2(ˆτn −τ0) = op(1) as n →∞. Let ˆdn denote the estimator
computed using ˜pn(Xi) = 1 −Φ{T(Xi, ˆτn)}. Then, ˆdn −d0 = op(1) as n →∞.
Remark 1. The model in (2) incorporates the situations with discrete responses. For example,
we can consider binary responses with Yijs indicating a reaction to a dose at level Xi . We
assume that the function µ(x), the probability that a subject yields a reaction at dose x, is
of the form (1) and takes values in (0, 1) so that σ2(x) = µ(x){1 −µ(x)} > 0. The results
from this section as well as those from Section 2.2 will continue to hold for this setting.
Remark 2. Our assumption of continuity of µ can be dropped and the results from this section
as well as those from Section 2.2 will continue to hold provided that µ is bounded and
continuous almost everywhere with respect to Lebesgue measure. This includes the classical
change-point problem where µ has a jump discontinuity at d0 but is otherwise continuous.
2.4. Estimators of τ0. Suitable estimates of τ0 are required that satisfy the conditions stated
in Theorems 1 and 2. In a situation where d0 may be safely assumed to be greater than some
known positive η, an estimate of τ0 can be obtained by taking the average of the response
values on the interval [0, η]. The estimator would be (nm)1/2-consistent and would therefore
satisfy the required conditions. Such an estimator is seen to be reasonable for most of the
data applications that are considered in this paper. In situations when such a solution is not
satisfactory, we propose an approach to estimate τ0 that does not require any background
knowledge, once again using p-values.
We now construct an explicit estimator ˆτ of τ0 in the dose-response setting, as re-
quired in Theorem 1, using p-values.
For convenience, let Zim(τ) = pm,n(Xi, τ) =
1 −Φ

m1/2( ¯Yi· −τ)/ˆσm,n(Xi)
	
. Let τ > τ0. As m increases, for µ(Xi) < τ, Zim(τ)
converges to 1 in probability, while for µ(Xi) > τ, Zim(τ) converges to 0 in probability.
For any τ < τ0, it is easy to see that Zim(τ) always converges to 0, whereas when τ = τ0,
Zim(τ) converges to 0 for Xi > d0 and E{Zim(τ)} converges to 1/2 for Xi < d0. Thus, it is
only when τ = τ0 that Zim(τ)s are closest to 1/2 for a substantial number of observations.
This suggests a natural estimate of τ0:
ˆτ ≡ˆτm,n = arg min
τ
n
X
i=1
{Zim(τ) −1/2}2.
(5)
Theorem 3 shows that under some mild conditions and homoscedasticity, m1/2 (ˆτm,n −τ0) is
op(1), a condition required for Theorem 1. This proof is given in Supplementary Material 1.


## Page 9


THRESHOLD ESTIMATION
9
Theorem 3. Consider the same setup as in Theorem 1. Assume that the errors are ho-
moscedastic with variance σ2
0. Further suppose that the regression function µ satisﬁes:
(A) Given η
>
0,
there exists ǫ
>
0 such that,
for every τ
>
τ0,
R
{x>d0:|µ(x)−τ|≤ǫ} f(x)dx < η.
Also assume that φm, the density function of m1/2 ǫ1./σ0, converges pointwise to φ, the stan-
dard normal density. Then m1/2 (ˆτm,n −τ0) = op(1).
Remark 3. Condition (A) is guaranteed if, for example, µ is strictly increasing to the right of
d0 although it holds under weaker assumptions on µ. In particular, it rules out ﬂat stretches to
the right of d0. The assumption that φm converges to φ is not artiﬁcial, since convergence of
the corresponding distribution functions to the distribution function of the standard normal
is guaranteed by the central limit theorem.
This approach in (5) can also be emulated to construct estimators of τ0 for the standard re-
gression setting by just going through the procedure with pn(Xi, τ)s instead of pm,n(Xi, τ)s
and it is clear that this estimator is consistent. However, the theoretical properties of this
estimator, such as the rate of convergence, are not completely known. Nevertheless, the
procedure has good ﬁnite sample performance as indicated by the simulation studies in Sec-
tion 3. The estimator is positively biased. This is due to the fact that a value larger than τ0 is
likely to minimize the objective function in (5) as it can possibly ﬁt the p-values arising from
a stretch extending beyond [0, d0], in presence of noisy observations. The values smaller than
τ0 do not get such preference as the true function never falls below τ0.
2.5. To smooth or not to smooth. The consistency of the two methods established in the
previous sections justiﬁes good large sample performance of the procedures, but does not
provide us with practical guidelines on which method to use given a real application. In dose-
response studies, it is quite difﬁcult to ﬁnd situations where both m and n are large. Typically,
such studies do not administer too many dose levels which precludes n from being large. So,
we compare the ﬁnite sample performance of the two methods for different allocations of m
and n to highlight their relative merits.
We study the performance of the two methods for three different choices of regression
functions. All these functions are assumed to be at the baseline value 0 to the left of d0 ≡0.5.
Speciﬁcally, M1 is a piece-wise linear function rising from 0 to 0.5 between d0 and 1; M2, a
convex curve, grows like a quadratic beyond d0, and reaches 0.5 at 1; M3 rises linearly with
unit slope for values ranging from d0 to 0.8 and then decreases with unit slope for values


## Page 10


10
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
between 0.8 and 1.0. So, M1 and M2 are strictly monotone to the right of d0 and exhibit
increasing level of smoothness at d0. On the other hand, M3 is tent-shaped and estimating d0
is expected to be harder for M3 compared to M1.
For each allocation pair (m, n) and a choice of a regression function, we generate re-
sponses {Yi1, . . . , Yim}, with Yij = µ(Xi) + ǫij, the ǫijs being independent N(0, σ2) with
σ = 0.3. The Xis are sampled from Uniform(0,1). The performance for estimating d0 ≡0.5
is studied based on root mean square error computed over 2000 replicates, assuming a known
variance and a known τ0 ≡0. For illustrative purposes, we use the Gaussian kernel for
Method 2. Based on heuristic computations, a bandwidth of the form hn = cn−1/(2p+1) is
chosen as it is expected to attain the minimax rate of convergence for estimating a cusp of
order p, as per Raimondo (1998). For M1 and M3, p = 1 while for M2, p is 2. We report the
simulations for the best c which minimizes the average of the root mean square errors for the
sample sizes considered, over a ﬁne grid.
There are results in the literature which suggest a possibly different minimax rate
of convergence based on calculations in a slightly different model (Neumann, 1997;
Goldenshluger et al., 2006) and hence a possibly different choice of optimal bandwidth. But
not much improvement was seen in terms of the root mean square errors for other choices of
bandwidth.
The root mean square errors and the biases for each allocation pair are given in Table 1.
Both procedures are inherently biased to the right as the p-values are not necessarily close
to zero to the immediate right of d0. When m and n are comparable, e.g., m ≤15 and
n ≤15, Method 2, which relies on smoothing, does not perform well compared to Method
1. However, when m is much smaller than n, e.g., m = 4 and n = 80, smoothing is efﬁcient
and Method 2 is preferred over Method 1. When both m and n are large, both methods work
well. As Method 1 does not require selecting any tuning parameter, we recommend Method
1 in such situations.
2.6. Extension to Dependent Data. The global warming data falls under the standard re-
gression setup, but involves dependent errors. Moreover, the data arises from a ﬁxed design
setting, with observations recorded annually. Here, we discuss the extension of Theorem 2
in this setting. Under ﬁxed uniform design, we consider the model Yi,n = µ (i/n)+ǫi,n (i =
1, . . . , n). Under such a model, Yi,n and ǫi,n must be viewed as triangular arrays. The es-
timator of the regression function is ˜µ(x) = (nhn)−1 P
i Yi,nK {h−1
n (x −i/n)}. For each
n, we assume that the process ǫi,n is stationary and exhibits short-range dependence. Under


## Page 11


THRESHOLD ESTIMATION
11
TABLE 1. Root mean square errors (×102) and biases (×102), the ﬁrst and
second entries respectively, for the estimate of threshold d0 obtained using
Methods 1 and 2, for the three models with σ = 0.3 and different choices of
m and n.
(m, n)
M1
M2
M3
Method 1
Method 2
Method 1
Method 2
Method 1
Method 2
(0.04n−1/3)
(0.08n−1/5)
(0.04n−1/3)
(5, 5)
16.9, 4.5
18.0, 9.6
20.2, 11.6
21.8, 10.9
20.5, 7.5
23.7, 14.3
(5, 10)
15.7, 6.7
16.6, 9.1
21.8, 17.2
21.3, 11.5
20.1, 10.9
20.8, 12.4
(10, 10)
13.4, 3.3
14.1, 5.6
19.0, 13.9
19.3, 8.6
14.9, 4.6
15.6, 6.9
(10, 15)
11.8, 4.9
12.6, 5.2
18.7, 15.5
19.0, 7.8
12.2, 5.3
12.9, 5.8
(10, 20)
10.8, 6.2
10.9, 4.6
18.5, 16.7
17.6, 6.9
10.9, 6.4
11.0, 4.9
(15, 10)
12.5, 1.8
12.6, 4.0
17.7, 11.7
18.4, 7.0
13.5, 2.0
13.2, 4.6
(15, 15)
10.4, 3.8
10.9, 4.0
17.2, 14.0
17.5, 6.6
10.9, 3.8
11.2, 3.8
(15, 20)
9.4, 4.2
9.8, 3.8
17.0, 14.9
17.4, 5.9
9.2, 4.4
10.0, 3.6
(20, 10)
12.4, 1.0
12.3, 2.9
16.5, 11.2
17.5, 6.5
12.7, 0.7
12.3, 3.9
(20, 15)
10.2, 2.5
10.6, 2.5
16.2, 13.3
17.0, 5.8
10.3, 2.6
10.6, 2.7
(20, 20)
8.9, 3.3
9.7, 2.3
15.9, 13.9
16.1, 5.4
8.7, 3.6
9.3, 2.7
(3, 80)
16.2, 14.5
10.5, 8.0
26.9, 26.2
16.4, 9.3
19.7, 16.6
11.0, 8.3
(3, 100)
16.2, 14.6
9.9, 7.7
27.0, 26.5
15.9, 8.9
18.7, 15.9
9.8, 7.4
(4, 80)
14.1, 12.4
9.4, 6.9
24.8, 24.2
15.7, 8.6
15.0, 12.9
9.8, 6.8
(4, 100)
14.0, 12.5
8.8, 6.3
24.9, 24.4
14.8, 7.8
14.4, 12.5
8.7, 6.3
Assumptions 1-5, listed in Robinson (1997), it can be shown that (nhn)1/2{˜µ(xk) −µ(xk)},
xk ∈(0, 1), k = 1, 2 and x1 ̸= x2, converge jointly in distribution to independent nor-
mals with zero mean. In this setting, the working p-values, deﬁned here to be p(1)
n (x, τ0) =
1 −Φ{(nhn)1/2(˜µ(x) −τ0)}, still exhibit the desired dichotomous behavior. To keep the
approach simple, we have not normalized by the estimate of the variance as this would have
involved estimating the auto-correlation function. The conclusions of Theorem 2 can be
shown to hold when ˆdn is constructed using (4) based on p(1)
n (Xi, ˆτ)s. Here, ˆτ is constructed
via averaging the responses over an interval that can be safely assumed to be on the left of
d0, as discussed in Section 2.4.


## Page 12


12
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
TABLE 2. Root mean square errors (×102) and biases (×102), the ﬁrst and
second entries respectively, for the estimate of threshold d0 obtained using
Method 1 and the estimate of τ0 with σ = 0.3 for the three models.
(m, n)
M1
M2
M3
d0
τ0
d0
τ0
d0
τ0
(5, 5 )
25.5, 21.5
17.5, 9.9
28.2, 25.5
13.4, 6.0
31.2, 26.2
14.2, 8.4
(5, 10 )
24.8, 20.5
14.3, 8.6
27.1, 22.3
10.2, 4.9
30.3, 24.3
11.2, 7.2
(10, 10 )
20.7, 15.7
12.4, 6.7
24.6, 21.6
7.7, 3.5
27.2, 21.5
10.4, 6.9
(10, 20 )
17.2, 13.9
9.0, 5.2
24.0, 22.4
5.4, 2.9
24.8, 19.8
8.6, 6.2
(10, 50 )
13.6, 12.1
5.6, 3.8
23.5, 22.8
3.8, 2.7
18.6, 15.7
7.0, 5.8
(20, 50 )
9.0, 7.6
3.1, 1.8
19.4, 18.7
2.5, 1.7
12.4, 10.0
5.0, 3.4
(50, 100 )
5.0, 4.3
1.1, 0.7
15.2, 14.8
1.2, 0.9
5.2, 4.6
1.4, 0.9
3. SIMULATION RESULTS AND DATA ANALYSIS
3.1. Simulation Studies. We consider the same three choices of the regression function M1,
M2 and M3, as in Section 2.5. The data are generated for allocation pair (m, n) and a choice
of regression function, with the errors being independent N(0, σ2), where σ = 0.3. The Xis
are again sampled from Uniform(0,1). We study the performance of the two methods when
the estimates of d0 are constructed using p-values that are normalized by their respective
estimates of variances.
Firstly, we consider Method 1. In Table 2, we report the root mean square error and the
bias for the estimators of d0 and τ0, for different choices of m and n. For moderate sample
sizes, M3 shows greater root mean square errors in general than M1 and M2 as the signal is
weak close to 1 for M3. For large sample sizes, the performance of the estimate is similar
for M1 and M3 and is better than that for M2, which can be ascribed to M2 being smoother
at d0. The procedure is inherently biased to the right as p-values are not necessarily close to
zero to the immediate right of d0. Further, the estimator, on average, moves to the left with
increase in m as the desired dichotomous behavior becomes more prominent.
Next, we study the performance of Method 2. As the estimation procedure is entirely
based on {(Xi, ¯Yi·)}n
i=1, without loss of generality, we take m to be 1. We again work with the
Gaussian kernel with the smoothing bandwidth chosen in the same fashion as in Section 2.5.
In Table 3, we report the root mean square error and the bias for the two estimators, for
different choices of m and n. We see trends similar to those for Method 1, across the choices
of the regression functions.


## Page 13


THRESHOLD ESTIMATION
13
TABLE 3. Root mean square errors (×102) and biases (×102), the ﬁrst and
second entries respectively, for the estimate of threshold d0 obtained using
Method 2 and the estimate of τ0 with σ = 0.3 for the three models.
n
M1
M2
M3
hn = 0.1n−1/3
hn = 0.15n−1/5
hn = 0.1n−1/3
d0
τ0
d0
τ0
d0
τ0
20
28.5, 17.9
20.9, 10.5
29.0, 17.8
14.7, 5.7
32.6, 22.4
17.4, 8.4
30
26.8, 15.5
18.4, 9.4
26.8, 14.6
12.2, 3.8
31.9, 21.8
15.1, 7.4
50
23.7, 13.8
15.8, 8.0
24.4, 12.4
9.9, 3.1
28.4, 18.7
13.1, 6.9
80
21.5, 11.2
13.7, 6.6
22.2, 8.4
7.8, 1.9
27.0, 17.8
11.7, 6.8
100
19.5, 9.6
12.5, 5.3
21.6, 8.2
7.5, 1.7
25.1, 14.7
10.9, 6.1
200
15.9, 6.2
8.8, 3.5
19.1, 6.0
4.9, 1.1
21.0, 12.2
9.2, 5.3
500
10.4, 0.6
4.6, 1.4
16.4, 3.9
2.7, 0.5
14.2, 5.4
6.0, 2.5
1000
9.5, 0.4
3.1, 0.7
15.0, 2.0
2.0, 0.4
10.5, 2.1
3.9, 1.2
1500
8.5, 0.3
2.3, 0.5
14.8, 1.5
1.8, 0.3
8.8, 0.8
2.8, 0.8
2000
7.2, 0.2
2.0, 0.5
13.8, 0.7
1.5, 0.2
8.1, 0.1
2.3, 0.5
We studied the performance of the estimates under settings where d0 is closer to the bound-
ary of [0, 1]. Optimal allocation pairs (m, n) were also computed for a given model and a
ﬁxed budget N = m × n. These details are skipped here but can be found in Section 5.1 of
the Supplementary Material 1. We also compared Method 1 to some competing procedures
developed in the pharmacological dose-response setting to identify the minimum effective
dose, namely the approaches in Williams (1971), Hsu & Berger (1999), Chen (1999) and
Tamhane & Logan (2002). Method 1 was seen to perform well in comparison with these
methods. For more details, see Section 5.2 of the Supplementary Material 1.
Based on our simulation study, including results not shown here due to space considera-
tions, the following practical recommendations are in order. In terms of optimal allocation
under a ﬁxed budget N, it is better for one to invest in an increased number of covariate val-
ues n, rather than replicates m. In the case where the threshold d0 is closer to the boundaries,
investment in n proves fairly important. Further, when the sample size is reasonably large,
the procedure that avoids estimating the variance function and works with non-normalized
p-values, is competitive and is recommended in the regression settings with heteroscedastic
errors and time-series.


## Page 14


14
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
3.2. Data Applications. The ﬁrst data application deals with a dose-response experiment
that studies the effect on cells from the IPC-81 leukemia rat cell line to treatment with 1-
methyl-3-butylimidazolium tetraﬂuoroborate, at different doses measured in µM, micro mols
per liter (Ranke et al., 2004). The substance treating the cells is an ionic liquid and the
objective is to study its toxicity in a mammalian cell culture to assess environmental hazards.
The question of interest here is at what dose level toxicity becomes lethal and cell cultures
stop responding.
It can be seen from the physiological responses shown in the left panel of Fig. 1, that
there is a decreasing trend followed by a ﬂat stretch. Hence, it is reasonable to postulate a
response function that stays above a baseline level τ0 until a transition point d0 beyond which
it stabilizes at its baseline level. We assume errors to be heteroscedastic, as the variability
in the responses changes with level of dose, with more variation for moderate dose levels
compared to extreme dose levels. This is the small (m, n) case with m and n being compa-
rable; in fact, m = n = 9. Hence we apply Method 1 to this problem. The estimate of τ0
was constructed using the procedure based on p-values as described in Section 2.4. We get
ˆτ = 0.0286 with the corresponding ˆd = 5.522 log µM, the third observation from right. We
believe that this is an accurate estimate of d0, since the cell-cultures exhibit high responses
at earlier dose levels and no signiﬁcant signal to the right of the computed ˆd.
The second example, as discussed in the introduction, involves measuring mercury con-
centration in the atmosphere through the light detection and ranging technique. There are
221 observations with the predictor variable range varying from 390 to 720. As supported
by the middle panel of Fig. 1, the underlying response function is at its baseline level fol-
lowed by a steep descent, with the point of change being of interest. There is evidence of
heteroscedasticity and hence, we employ Method 2 without normalizing by the estimate of
the variance. It is reasonable to assume here that till the range value 480 the function is at
its baseline. The estimate of τ is obtained by taking the average of observations until range
reaches 480, which gives ˆτ = −0.0523. The estimates ˆd, computed for bandwidths vary-
ing from 5 to 30, show a fairly strong agreement as they lie between 534 and 547, with the
estimates getting bigger for larger bandwidths. The cross-validated optimal bandwidth for
regression is 14.96 for which the corresponding estimate of d0 is 541.
The global warming data contains global temperature anomalies, measured in degree Cel-
sius, for the years 1850 to 2009. These anomalies are temperature deviations measured with
respect to the base period 1961–1990. The data are modeled as described in Section 2.6.
As can be seen in the right panel of Fig. 1, the function stays at its baseline value for a


## Page 15


THRESHOLD ESTIMATION
15
while followed by a non-decreasing trend. The ﬂat stretch at the beginning is also noted in
Zhao and Woodroofe (2011) where isotonic estimation procedures are considered in settings
with dependent data. The estimate of the baseline value, after averaging the anomalies up to
the year 1875, is ˆτ = −0.3540. With the dataset having 160 observations, estimates of the
threshold were computed for bandwidths ranging from 5 to 30. The estimates varied over
a fairly small time frame, 1916–1921. This is consistent with the observation on page 2 of
Zhao and Woodroofe (2011) that global warming does not appear to have begun until 1915.
The optimal bandwidth for regression obtained through cross-validation is 13.56, for which
ˆd is 1920.
3.3. Extensions. Here we discuss some of the possible extensions of our proposed proce-
dure.
(i) Fixed design setting: Although the results in this paper have been proven assuming
a random design, they can be easily extended to a ﬁxed design setup. Consistency of the
procedures will continue to hold.
(ii) Unequal replicates: In this paper, we dealt with the case of a balanced design with
a ﬁxed number of replicates m for every dose level Xi. The case of varying number of
replicates mi can be handled analogously. In the dose-response setting, Theorem 1 will
continue to hold provided the minimum of the mis goes to inﬁnity. In the standard regression
setting, Theorem 2 can also be generalized to the situation with unequal number of replicates
at different doses.
(iii) Adaptive stump model: The use of 1/2 and 0 as the stump levels may not always
be the best strategy. The p-values to the right of d0 may not be small enough to be well
approximated by 0 for small m. One can deal with this issue by using a more adaptive
approach which keeps the stump-levels unspeciﬁed and estimates them from the data. For
example, in the dose-response setting, one can deﬁne,
(ˆαm,n, ˆβm,n, ˆdm,n) = arg
min
(α,β,d)∈[0,1]3
n
X
i=1
{pm,n(Xi) −α 1(Xi ≤d) −β 1(Xi > d)}2 .
Please see pages 5 and 16 in Supplementary Material 1 for more details on this estimator.
4. CONCLUDING DISCUSSION
We brieﬂy discuss a few issues, some of which constitute ongoing and future work on this
topic. While we have developed a novel methodology for threshold estimation and estab-
lished consistency properties rigorously, a pertinent question that remains to be addressed is


## Page 16


16
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
the construction of conﬁdence intervals for d0. A natural way to approach this problem is
to consider the limit distribution of our estimators for the two settings and use the quantiles
of the limit distribution to build asymptotically valid conﬁdence intervals. This is expected
to be a highly non-trivial problem involving hard non-standard asymptotics. The rate of
convergence crucially depends on the order of the cusp, p, at d0. As mentioned earlier, the
minimax rate for this problem is N−1/(2p+1) as per Raimondo (1998). This is in disagree-
ment with the faster rates min(N−2/(2p+3), N−1/(2p+1)) obtained in Neumann (1997) for a
change-point estimation problem in a density deconvolution model. There are recent results
(Goldenshluger et al., 2006, 2008) which suggest that Neumann’s rate should be optimal, but
an asymptotic equivalence between the density model in Neumann (1997) and the regression
model assumed in Raimondo (1998) and our paper has not been formally established. Based
on preliminary calculations, it is expected that our procedure will, at least, attain a rate of
N−1/(2p+1), under optimal allocation between m and n for Method 1 and for a suitable choice
of bandwidth for Method 2.
In this paper, we have restricted ourselves to a univariate regression setup. Our approach
can potentially be generalized to identify the baseline region, the set on which the function
stays at its minimum, in multi-dimensional covariate spaces. This is a special case of level
sets estimation, a problem of considerable interest in statistics and engineering. The p-values,
constructed analogously, will continue to exhibit a limiting dichotomous behavior which can
be exploited to construct estimates of the baseline region. Procedures that look for a jump in
the derivative of a certain order of µ (Mueller, 1992; Raimondo, 1998) do not have natural
extensions to high dimensional settings as the order of differentiability can vary from point
to point on the boundary of the baseline region.
ACKNOWLEDGEMENT
We thank Harsh Jain for bringing to our attention a threshold estimation problem that
eventually led to the formulation and development of this framework. The work of the
authors were partially supported by NSF and NIH grants.
SUPPLEMENTARY MATERIAL
The proof of Theorem 3, an extensive simulation study and a discussion on other
variants of the proposed methods are given in Supplementary Material 1 available at
http://arxiv.org/PS cache/arxiv/pdf/1008/1008.4316v1.pdf.


## Page 17


THRESHOLD ESTIMATION
17
APPENDIX
Proofs. We start with establishing an auxiliary result used in the subsequent developments.
Theorem 4. Let T be an indexing set and {Mτ
n : τ ∈T }∞
n=1 a family of real-valued sto-
chastic processes indexed by h ∈H. Also, let {Mτ : τ ∈T } be a family of deterministic
functions deﬁned on H, such that each Mτ is maximized at a unique point h(τ) ∈H. Here
H is a metric space and denote the metric on H by d. Let ˆhτ
n be a maximizer of Mτ
n. Assume
further that:
(a) supτ∈T suph∈H |Mτ
n(h) −Mτ(h)| = op(1), and
(b) for every η > 0, c(η) ≡infτ infh/∈Bη{h(τ)} [Mτ{h(τ)} −Mτ(h)] > 0, where Bη(h)
denotes the open ball of radius η around h.
Then, (i) supτ d{ˆhτ
n, h(τ)} = op(1). Furthermore, if T is a metric space and h(τ) is
continuous in τ, then (ii) ˆhτn
n −h(τ0) = op(1), provided τn converges to τ0. In particular, if
the Mτ
ns themselves are deterministic functions, the conclusions of the theorem hold with the
convergence in probability in (i) and (ii) replaced by usual non-stochastic convergence.
Proof. We provide the proof in the case when H is a sub-interval of the real line, the case
that is relevant for our applications. However, there is no essential difference in generalizing
the argument to metric spaces - euclidean distances simply need to be replaced by the metric
space distance and open intervals by open balls.
Given η
>
0, we need to deal with P ⋆{supτ∈T |ˆhτ
n −h(τ)|
>
η}, where P ∗
is the outer probability.
The event An,η
≡
{supτ∈T |ˆhτ
n −h(τ)|
>
η} implies
that for some τ, ˆhτ
n
/∈(h(τ) −η, h(τ) + η) and therefore Mτ{h(τ)} −Mτ(ˆhτ
n) ≥
infh/∈(h(τ)−η,h(τ)+η) [Mτ{h(τ)} −Mτ(h)] . This is equivalent to Mτ{h(τ)} −Mτ(ˆhτ
n) +
Mτ
n(ˆhτ
n) −Mτ
n{h(τ)} ≥infh/∈(h(τ)−η,h(τ)+η) [Mτ{h(τ)} −Mτ(h)] + Mτ
n(ˆhτ
n) −Mτ
n{h(τ)} .
Now, Mτ
n(ˆhτ
n) −Mτ
n{h(τ)} ≥0 and the left side of the above inequality is bounded above
by
2 ∥Mτ
n −Mτ∥H ≡2 sup
h∈H
|Mτ
n(h) −Mτ(h)| ,
implying that 2∥Mτ
n −Mτ∥H ≥infh/∈(h(τ)−η,h(τ)+η) [Mτ{h(τ)} −Mτ(h)] which, in turn,
implies that 2 supτ∈T ∥Mτ
n −Mτ∥H ≥infτ∈T infh/∈(h(τ)−η,h(τ)+η) [Mτ{h(τ)} −Mτ(h)] ≡
c(η) by deﬁnition. Hence An,η ⊂{supτ∈T ∥Mτ
n −Mτ∥H ≥c(η)/2}. By assumptions (a)
and (b), P ⋆{supτ∈T ∥Mτ
n −Mτ∥H ≥c(η)/2} goes to 0 and therefore so does P ⋆(An,η).
□


## Page 18


18
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
Remark 4. We will call the sequence of steps involved in deducing the inclusion:

sup
τ∈T
|ˆhτ
n −h(τ)| > η

⊂

sup
τ∈T
∥Mτ
n −Mτ∥H ≥c(η)/2

,
as generic steps. Very similar steps will be required again in the proofs of the theorems to
follow. We will not elaborate those arguments, but refer back to the generic steps in such
cases.
of Theorem 1. To exhibit the dependence on the baseline value τ0 (or its estimate), we use
notations of the form Mn(d, τ0) and ˆdm,n(τ0). For convenience, let T (m)(Xi) = m1/2( ¯Yi· −
τ0) and Zim(τ0) = ˜pm,n(Xi, τ0) = 1 −Φ{T (m)(Xi)}. As m changes, the distribution of
Zim(τ0) changes, and so we effectively have a triangular array {(Xi, Zim(τ0))}n
i=1 ∼Pm,
say. Using empirical process notation, Mm,n(d, τ0) ≡Pn,m{Z1m(τ0) −1/4}1(X1 ≤d),
where Pn,m denotes the empirical measure of the data. Firstly, we ﬁnd the limiting process
for Mm,n(d, τ0). Deﬁne Mm(d) ≡Pm{Z1m(τ0) −1/4}1(X1 ≤d) where Mm(d) can be
simpliﬁed as
Mm(d) =
Z d
0
{νm(x) −1/4}f(x)dx,
(6)
where νm(x) = E{Zim(τ0) | Xi = x}. Observe that for Xi = x, as m →∞, T (m)(x)
converges in distribution to N(0, σ2(x)) for x ≤d0 and T (m)(x) = m1/2{ ¯Yi· −µ(x)} +
m1/2{µ(x) −τ0} →∞, in probability, for x > d0. Thus, νm(x) →ν(x) for all x ∈[0, 1],
where ν(x) = (1/2)1(x ≤d0).
Let M(d) be the same expression for Mm(d) in (6)
with νm(x) replaced by ν(x), e.g., M(d) =
R d
0 {ν(x) −1/4}f(x)dx. Observe that for
c = (1/4)
R d0
0 f(x)dx, M(d) ≤c for all d, and M(d0) = c. Also, it is easy to see that
d0 is the unique maximizer of M(d). Now, the difference |Mm(d) −M(d)|, can be bounded
by
R 1
0 |νm(x)−ν(x)|f(x)dx which goes to 0 by the dominated convergence theorem. As the
bound does not depend on d, we get ∥Mm −M∥∞→0, where ∥·∥∞denotes the supremum.
By Theorem 4, dm = arg maxd∈[0,1] Mm(d) →arg maxd∈[0,1] M(d) = d0 as m →∞. It
would now sufﬁce to show that { ˆdm,n(ˆτ) −dm} is op(1).
Fix ǫ > 0 and consider the event {| ˆdm,n(ˆτ) −dm| > ǫ}. Since dm maximizes Mm and
ˆdm,n(ˆτ) maximizes Mm,n(·, ˆτ), by arguments analogous to the generic steps in the proof of
Theorem 4, we have:
| ˆdm,n(ˆτ) −dm| > ǫ ⇒∥Mm,n(·, ˆτ) −Mm(·)∥∞≥ηm(ǫ)/2 ,
where ηm(ǫ) = infd∈(dm−ǫ,dm+ǫ)c{Mm(dm) −Mm(d)}.


## Page 19


THRESHOLD ESTIMATION
19
We claim that there exists η > 0 and an integer M0 such that ηm(ǫ) > η > 0 for all
m ≥M0. To see this, let us bound Mm(dm)−Mm(d) below by −2∥Mm−M∥∞+M(dm)−
M(d). As ∥Mm −M∥∞→0 as m →∞, it is enough to show that there exists η > 0
such that for all sufﬁciently large m, infd∈(dm−ǫ,dm+ǫ)c{M(dm) −M(d)} > η. We split
M(dm) −M(d) into two parts as {M(d0) −M(d)} + {M(dm) −M (d0)}. Notice that by
the continuity of M(·), the second term goes to 0. To handle the ﬁrst term, notice that M(d)
is a continuous function with a unique maximum at d0. There exists M0 ∈N such that for
all m > M0, we have (d0 −ǫ/2, d0 + ǫ/2) ⊂(dm −ǫ, dm + ǫ) as dm →d0. So, for m > M0,
infd∈(dm−ǫ,dm+ǫ)c{M(d0) −M(d)} ≥infd∈(d0−ǫ/2,d0+ǫ/2)c{M(d0) −M(d)}. As M(d0) −
M(d) is continuous, this inﬁmum is attained in the compact set [0, 1] ∩(d0 −ǫ/2, d0 + ǫ/2)c
and is strictly positive. Thus, a positive choice for η, as claimed, is available.
The claim yields,
Pm{| ˆdm,n(ˆτ) −dm| > ǫ}
(7)
≤
Pm{∥Mm,n(·, ˆτ) −Mm,n(·, τ0)∥∞> η/4} + Pm{sup
l≥n
∥Mm,l(·, τ0) −Mm∥∞> η/4}.
For the ﬁrst term, notice that, ∥Mm,n(·, ˆτ) −Mm,n(·, τ0)∥∞
≤
maxi≤n |Zim(ˆτ) −
Zim(τ0)|.
This is bounded above by supu∈R |Φ (u) −Φ {u + √m(ˆτ −τ0)}|.
As
supu∈R |Φ (u) −Φ (u + a)| = 2Φ (|a|/2) −1, for a ∈R, ∥Mm,n(·, ˆτ) −Mm,n(·, τ0)∥∞
is bounded by {2Φ
 m1/2|ˆτ −τ0|/2

−1}, which goes in probability to zero.
To show that the last term in (7) goes to zero, consider the class of functions F ≡
{fd(x, z) ≡(z −1/4)1(x ≤d)|d ∈[0, 1]} with the envelope F(x, z) = 1. The class F is
formed by multiplying a ﬁxed function z 7→(z −1/4) with a bounded Vapnik-Chervonenkis
classes of functions {1(x ≤d) : 0 ≤d ≤1} and therefore satisﬁes the entropy condi-
tion in the third display on page 168 of van der Vaart & Wellner (1996). It follows that F
satisﬁes the conditions of Theorem 2.8.1 of van der Vaart & Wellner (1996) and is therefore
uniformly Glivenko–Cantelli for the class of probability measures {Pm}, i.e.,
sup
m≥1
Pm{sup
n≥k
∥Mm,n(·, τ0) −Mm(·)∥∞> ǫ} →0
for every ǫ > 0 as k →∞. Thus, we get P{| ˆdm,n(ˆτ) −dm| > ǫ} →0 as m, n →∞. This
completes the proof of the theorem.
□
Recall that T(x, τ0) = (nhn)1/2{ˆµ(x) −τ0}. The following standard result from non-
parametric regression theory is useful in proving Theorem 2. The proof follows, for example,
from the results in Section 2.2 of Bierens (1987).


## Page 20


20
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
Lemma 1. Assume that µ(·) and σ2(·) is continuous on [0, 1]. is continuous on [0,1]. We
then have:
(i) For 0 < x, y < d0 and x ̸= y,
 
T(x, τ0)
T(y, τ0)
!
→N
  
0
0
!
,
 
¯
K2σ2(x)/{mf(x)}
0
0
¯
K2σ2(y)/{mf(y)}
!!
,
in distribution.
(ii) For d0 < z < 1, T(z, τ0)→∞in probability.
Proof of Theorem 2. Let ν(x) and M(d) be as deﬁned in proof of Theorem 1, e.g., ν(x) =
(1/2)1(x ≤d0). For notational convenience, let Zi(τ0) = ˜pn(Xi) = 1 −Φ{T(Xi, τ0)}.
We eventually show that ∥Mn(·, ˆτ) −M(·)∥∞converges to 0 in probability and then apply
argmax continuous mapping theorem to prove consistency. By calculations similar to those
in the proof of Theorem 1, ∥Mn(·, ˆτ) −Mn(·, τ0)∥≤{2Φ
 (nhn)1/2|ˆτ −τ0|/2

−1}, which
converges to 0 in probability. So, it sufﬁces to show that ∥Mn(·, τ0) −M(·)∥∞converges to
0 in probability. We ﬁrst establish marginal convergence. We have
E [Φ{T(X1, τ0)}| X1 = x]
(8)
=
E

Φ
(nhn)−1/2 [{µ(x) −τ0 + ǫ1}K(0) + Pn
i=2(Yi −τ0)K {h−1
n (x −Xi)}]
(nhn)−1 [K(0) + Pn
i=2 K {h−1
n (x −Xi)}]

.
The ﬁrst term, both in the numerator and the denominator of the argument, is asymp-
totically negligible and thus, the expression in (8) equals E[Φ{T(x, τ0) + op(1)}].
Using Lemma 1, this converges to 1 −ν(x), by deﬁnition of weak convergence.
As
Zi(τ0) = 1 −Φ{T(Xi, τ0)}, we get E {Mn(d, τ0)} = E[E {Z1(τ0) −0.25}1(X1 ≤d)|X1]
which converges to M(d). Further, var{Mn(d, τ0)} = n−1var [{Z1(τ0) −0.25}1(X1 ≤d)]+
n−1(n −1)cov [{Z1(τ0) −0.25}1(X1 ≤d), {Z2(τ0) −0.25}1(X2 ≤d)] .
The
ﬁrst
term
in
this
expression
goes
to
zero
as
|Z1(τ0)|
≤
1.
For
y
̸=
x,
by
calculations
similar
to
(8),
E {Z1(τ0)Z2(τ0)| X1 = x, X2 = y}
=
E [Φ {T(x, τ0) + op(1)} Φ {T(y, τ0) + op(1)}].
Using Lemma 1, T(x, τ0) and T(y, τ0)
are asymptotically independent. Thus, by taking iterated expectations, it can be shown that
cov [{Z1(τ0) −0.25}1(X1 ≤d), {Z2(τ0) −0.25}1(X2 ≤d)] →0. This justiﬁes pointwise
convergence, e.g., Mn(d, ˆτ0) −M(d) = op(1), for d ∈[0, 1]. Further, as |Zi(ˆτ) −1/4| ≤1,


## Page 21


THRESHOLD ESTIMATION
21
for d1 < d < d2, we have
E [|{Mn(d, τ0) −Mn(d1, τ0)}{Mn(d2, τ0) −Mn(d, τ0)}|]
≤
E
"(
1
n
n
X
i=1
1(Xi ∈(d1, d])
) (
1
n
n
X
i=1
1(Xi ∈(d, d2])
)#
.
The above two terms, under expectation, are independent and thus, the expression is bounded
by ∥f∥2
∞(d−d1)(d2−d) ≤∥f∥2
∞(d2−d1)2. As f is continuous on [0, 1], ∥f∥∞< ∞. Thus,
the processes {Mn(·, τ0)}n≥1 are tight in D[0, 1] using Theorem 15.6 in Billingsley (1968).
So, Mn(·, τ0) converges weakly to M as processes in D[0, 1]. As the limiting process is
degenerate and the map x(·) 7→supd∈[0,1] |x(d)| is continuous, by continuous mapping, we
get ∥Mn(·, τ0)−M(·)∥converges in probability to zero. As d0 is the unique maximizer of the
continuous function M(·) and ˆdn(ˆτ) is tight as ˆdn(ˆτ) ∈[0, 1]. Hence, by argmax continuous
mapping theorem in van der Vaart & Wellner (1996), we get the result.
✷
REFERENCES
BIERENS, H. J. (1987). Kernel Estimators of Regression Functions, in: T. F. Bewley, ed.,
Advances in Econometrics, 1, (Cambridge University Press), 99-144.
BILLINGSLEY, P. (1968). Convergence of probability measures. Wiley, New York.
CHEN, Y. (1999). Nonparametric Identiﬁcation of the Minimum Effective Dose. Biometrics,
55, 1236–1240.
CHEN, Y. & CHANG, Y. (2007). Identiﬁcation of the minimum effective dose for right-
censored survival data. Comp. Statist. Data Ana., 51, 3213-3222.
COX, C. (1987). Threshold dose-response models in toxicology. Biometrics, 43, 511-523.
DELWORTH, T.L. AND KNUTSON, T.R. (2000). Simulation of early 20th century global
warming. Science, 287, 2246-2250.
GOLDENSHLUGER, A. TSYBAKOV, A. AND ZEEVI, A.
(2006). Optimal change–point
estimation from indirect observations Ann. Statist., 34, 350–372.
GOLDENSHLUGER, A., JUDITSKY, A. TSYBAKOV, A. AND ZEEVI, A. (2008). Change–
point estimation from indirect observations. 1. Minimax Complexity. Ann. Inst. Henri
Poincar´e Probab. Stat., 44, 787–818.
HOLST, U., HOSSJER, O., BJORKLUND, C., RAGNARSON, P. AND EDNER, H. (1996).
Locally weighted least squares kernel regression and statistical evaluation of LIDAR mea-
surements, Environmetrics, 7, 401-416.


## Page 22


22
A. MALLIK, B. SEN, M. BANERJEE AND G. MICHAILIDIS
HSU, J. & BERGER, R. (1999). Stepwise conﬁdence intervals without multiplicity adjust-
ment for dose–response and toxicity studies. J. Amer. Statist. Assoc., 94, 468-482.
IBRAGIMOV, I. A., AND KHASMINSKII,R. Z. (1981). Statistical Estimation: Asymptotic
Theory. Springer, New York.
KOUL, H. L. AND QIAN, L. (2002). Asymptotics of maximum likelihood estimator in a
two-phase linear regression model. C. R. Rao 80th birthday felicitation volume, Part II. J.
Statist. Plann. Infer., 108, 99–119.
LAN, Y., BANERJEE, M. AND MICHAILIDIS, G. (2009). Change-point estimation under
adaptive sampling, Ann. Statist., 37, 1752–1791.
LOADER, C. R. (1996). Change point estimation using nonparametric regression. Ann. of
Statist., 24, 1667–1678.
MELILLO, J.M. (1999). Climate change: warm, warm on the range. Science, 283, 183-184.
MUELLER, H. G. (1992). Change-points in nonparametric regression analysis. Ann. Statist.,
20, 737–761.
NEUMANN, M. H. (1997). Optimal changepoint estimation in inverse problems. Scand. J.
Statist., 24, 503–521.
PONS, O. (2003). Estimation in a Cox regression model with a change–point according to a
threshold in a covariate Ann. Statist., 31, 442–463.
PONS, O. (2009). Estimation and tests in distribution mixtures and change–points models.
Paris.
RAIMONDO, M. (1998). Minimax estimation of sharp change points. Ann. Statist., 26, 1379–
1397.
RANKE, J., MOLTER, K., STOCK, F., BOTTIN–WEBER, U., POCZOBUTT, J., HOFF-
MANN, J., ONDRUSCHKA, B., FILSER, J. AND JASTORFF B. (2004) Biological effects of
imidazolium ionic liquids with varying chain lengths in acute Vibrio ﬁscheri and WST-1
cell viability assays. Ecotoxicology and Environmental Safety, 28, 396-404.
ROBINSON, P. M. (1997). Large-sample inference for nonparametric regression with depen-
dent errors. Ann. Statist., 25, 2054-2083
RUPPERT, D., WAND, M.P., HOLST, U. AND HOSSJER, O. (1996). Local polynomial vari-
ance function estimation. Technometrics, 39, 262-273.
TAMHANE, A. AND LOGAN, B. (2002). Multiple test procedures for identifying the mini-
mum effective and maximum safe doses of a drug. J. Amer. Statist. Assoc., 97, 293–301.
VAN DER VAART, A. W. & WELLNER, J. A. (1996). Weak Convergence and Empirical
Processes. Springer, New York.


## Page 23


THRESHOLD ESTIMATION
23
WILLIAMS, D. A. (1971). A Test for Differences between Treatment Means When Several
Dose Levels are Compared with a Zero Dose Control. Biometrics, 27, 103–117.
ZHAO, O. AND WOODROOFE, M.W. (2011). Estimating a monotone trend. To appear in
Stat. Sinica.
DEPARTMENT OF STATISTICS, UNIVERSITY OF MICHIGAN, ANN ARBOR, MI 48109
E-mail address: atulm@umich.edu
DEPARTMENT OF STATISTICS, COLUMBIA UNIVERSITY, NEW YORK, NY 10027
E-mail address: bodhi@stat.columbia.edu
DEPARTMENT OF STATISTICS, UNIVERSITY OF MICHIGAN, ANN ARBOR, MI 48109
E-mail address: moulib@umich.edu
DEPARTMENT OF STATISTICS, UNIVERSITY OF MICHIGAN, ANN ARBOR, MI 48109
E-mail address: gmichail@umich.edu

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
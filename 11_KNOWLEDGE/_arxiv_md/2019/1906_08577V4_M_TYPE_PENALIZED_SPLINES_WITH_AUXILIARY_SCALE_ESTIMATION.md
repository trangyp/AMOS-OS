---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.08577v4
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1906.08577v4_M-type_penalized_splines_with_auxiliary_scale_estimation

> Source: 1906.08577v4_M-type_penalized_splines_with_auxiliary_scale_estimation.pdf

> Pages: 26

---


## Page 1


M-type penalized splines with auxiliary scale estimation
Ioannis Kalogridis and Stefan Van Aelst
March 9, 2020
Abstract
Penalized spline regression is a popular and ﬂexible method of obtaining estimates
in nonparametric models but the classical least-squares criterion is highly susceptible
to model deviations and atypical observations.
Penalized spline estimation with a
resistant loss function is a natural remedy, yet to this day the asymptotic properties of
M-type penalized spline estimators have not been studied. We show in this paper that
M-type penalized spline estimators achieve the same rates of convergence as their least-
squares counterparts, even with auxiliary scale estimation. We further ﬁnd theoretical
justiﬁcation for the use of a small number of knots relative to the sample size. We
illustrate the beneﬁts of M-type penalized splines in a Monte-Carlo study and two
real-data examples, which contain atypical observations.
1
Introduction
Based on data (xi, Yi), . . . , (xn, Yn) with ﬁxed xi ∈[a, b] and −∞< a < b < ∞, consider
the classical nonparametric regression model
Yi = f(xi) + ϵi,
(1)
where f(·) is a suﬃciently smooth function which we shall endeavour to estimate and the
ϵi, i = 1, . . . , n are independent and identically distributed error terms, commonly assumed
to have zero mean and ﬁnite variance σ2.
Nonparametric regression has been a burgeoning ﬁeld for many years and many inge-
nious methods have been proposed for the estimation of the regression function f(·). These
methods broadly comprise kernel regression, orthogonal series, splines and wavelets, see,
e.g., Wasserman (2006) for an overview. In this paper, we focus on robust estimation with
penalized splines. Owing to their ease of ﬁtting and ﬂexible choice of knots and penalties, pe-
nalized splines have been exceedingly popular in recent years following the seminal works of
O’Sullivan (1986) and Eilers et al. (1996). Penalized splines oﬀer a compromise between the
simplicity of (unpenalized) regression splines and the computational complexity of smoothing
splines, see Wahba (1990, Chapter 7) for this point. Asymptotic properties of least-squares
penalized spline estimators have been studied by Hall et al. (2005), who established their
1
arXiv:1906.08577v4  [stat.ME]  6 Mar 2020


## Page 2


consistency, Li et al. (2008), who derived the equivalent kernel representation for lower-order
splines, and more broadly by Claeskens et al. (2009), who obtained rates of convergence for
a variety of settings.
It is well-known that estimators derived from the minimization of an L2 norm are sus-
ceptible to atypical observations. That is, a single gross outlier can signiﬁcantly distort the
estimates as well as inferences based on them. This fact has motivated proposals that aim to
achieve some degree of resistance towards outlying observations. Lee et al. (2007) proposed
replacing the squared loss with a loss function that increases more slowly and supplied an
algorithm based on pseudo-observations. In the same vein, Tharmaratnam et al. (2010)
proposed minimizing a robust scale of the residuals with an additional penalty term in order
to obtain resistant estimates. However, despite the well-studied theoretical properties of
least-squares penalized splines, it is curious that no asymptotic results have been established
outside that framework. This comes in stark contrast to robust smoothing and regression
splines whose asymptotic properties have been established as early as Cox (1983) and Shi et
al. (1995) with signiﬁcant extensions with respect to scale estimation oﬀered by Cunningham
et al. (1991) and He et al. (1995) respectively.
To ﬁll this gap we study the consistency and establish rates of convergence of general M-
type penalized spline estimators with a derivative-based penalty. Moreover, we also consider
the case where a preliminary scale estimator is used to standardize the residuals in the loss
function. As mentioned previously, this type of estimator was already considered by Lee et
al. (2007) from a computational point of view, but without any theoretical support. Our
approach further diﬀers from their proposal in three key aspects. Firstly, we use the nearly
orthogonal B-spline basis instead of the badly conditioned truncated polynomials and derive
theoretical properties based on that representation. Secondly, we use a robust preliminary
scale estimate that does not require model ﬁtting as opposed to the originally proposed
concomitant scale estimate. This dramatically reduces the computational burden as there
is no need anymore to iterate between coeﬃcient and scale estimates. Finally, we propose
a fast, eﬀective and automatic method of selecting the penalty parameter which has the
advantage that the penalty parameter no longer needs to be chosen at each iteration of the
algorithm.
The rest of the paper is structured as follows. We review a few basic facts about spline
estimation in Section 2 and describe the proposed M-type penalized estimator and its compu-
tation in Section 3. In Section 4 the asymptotic properties of the estimator are studied. We
obtain an asymptotic expansion of the estimator and show that it achieves the optimal rates
of convergence, even with auxiliary scale estimation. Section 5 examines the performance of
the proposed method via a Monte-Carlo study while Section 6 illustrates the advantages of
its use in two real data examples. Finally, some possible directions for future research are
discussed in the concluding section of this paper.
2


## Page 3


2
Spline-based estimation
A spline is deﬁned as a piecewise polynomial that is smoothly connected at its joints
(knots). More speciﬁcally, for any ﬁxed integer p ≥1, denote Sp
K the set of spline functions
of order p with knots a = t0 < t1 . . . < tK+1 = b. Then for p = 1, S1
K is the set of step
functions with jumps at the knots and for p ≥2,
Sp
K =

s ∈Cp−2[a, b] : s(x) is a polynomial of degree (p −1) on each subinterval [ti, ti+1]
	
.
It is easy to see that Sp
K is a p + K dimensional subspace of Cp−2[a, b] and a basis may
be derived by means of the truncated polynomials 1, x, . . . , xp−1, (x −t1)p−1
+ , . . . (x −tK)p−1
+
with (x)+ = xI(x ≥0). However, truncated polynomial functions are known to be highly
collinear for a large number of knots. Hence, it is preferable to use the more stable B-spline
basis for Sp
K, which we now brieﬂy discuss; we refer to De Boor (2001, Chapter IX) for a full
treatment.
The B-spline functions may be deﬁned recursively but they may also be directly derived
as linear combinations of the truncated polynomial functions (x −t1)p−1
+ , . . . , (x −tK)p−1
+ .
Several important properties follow immediately from this construction. Let {ti}K+2p
i=1
be an
augmented and relabelled sequence of knots obtained by repeating t0 and tK+1 exactly p
times. The B-spline basis for the family Sp
K is given by
BK,i(x) = (ti+p −ti) [ti, . . . , ti+p] (t −x)p−1
+ ,
i = 1, . . . , K + p
(2)
where for a function g the placeholder notation [ti, . . . , ti+p] g denotes the pth order divided
diﬀerence of g(·) at ti, . . . , ti+p.
Among other interesting properties B-splines of order p
satisfy
(a) Each BK,i is a polynomial of order p on each interval (ti, ti+1) and has (p−2) continuous
derivatives.
(b) 0 < BK,i(x) ≤1 for x ∈(ti, ti+p) and BK,i(x) = 0 otherwise.
(c) PK+p
i=1 BK,i(x) = 1 for all x ∈[a, b].
Property (b) is referred to as the local support property of the B-spline basis and it is one of
the reasons for the popularity of the basis in digital computing and functional approximation.
Further properties of splines and the B-spline basis may be found in the classical monographs
of DeVore et al. (1993), De Boor (2001) and Schumaker (2007). Spline functions from a
statistical perspective are covered in, e.g., Wahba (1990), Green et al. (1993), Eubank (1999)
and Gu (2013).
Of particular interest are the approximation properties of spline functions. Provided that
f(·) is a suﬃciently smooth function, in the sense of having a number of continuous deriva-
tives, the spline approximation theorems, see, e.g., Schumaker (2007, Chapter 6), allow us to
deduce that f(·) may be well-approximated by a spline function f ⋆(x) = PK+p
j=1 β⋆
j BK,j(x).
3


## Page 4


This fact underlies all spline-based estimation techniques except for the smoothing spline
construction, see the end of this section. A reasonable approximation may thus be con-
structed by expanding f(·) in the B-spline basis and estimating the coeﬃcient vector β. The
most popular estimation method to that end is the least squares criterion leading to the
minimization of
n−1
n
X
i=1
(
Yi −
X
j≤K+p
βjBK,j(xi)
)2
.
(3)
See Agarwal et al. (1980), Wegman et al. (1983) and Shen et al. (1998) for more details on
least-squares regression splines. To compensate for the lack of robustness of the least-squares
criterion Shi et al. (1995) proposed minimizing instead
n−1
n
X
i=1
ρ
 
Yi −
X
j≤K+p
βjBK,j(xi)
!
,
(4)
for a suitably chosen convex function ρ, see Huber (1973). Unfortunately, a common draw-
back in both procedures is the sensitivity of the estimator to the number of knots as well
as their position. Selection procedures are non-trivial and very often involve either a step-
wise/backward knot placement procedure or minimization of a complex information criterion,
Eubank (1999, Chapter 6).
An alternative estimation method results from adding a ridge-type roughness penalty to
the above minimization problem eﬀectively shifting the focus from the knots to the penalty
parameter. In particular, O’Sullivan (1986) proposed adding a roughness penalty in the form
of the integrated squared qth derivative of the spline function and minimize
n−1
n
X
i=1
(
Yi −
X
j≤K+p
βjBK,j(xi)
)2
+ λ
Z
[a,b]


( X
j≤K+p
βjBK,j(t)
)(q)

2
dt,
(5)
for some knot sequence t1, . . . , tK+2p. In the original proposal, q was equal to 2 but general-
ization to higher order penalties is straightforward. The present penalized spline estimator,
commonly referred to as O-spline, has two smoothing parameters: the number of knots and
the penalty parameter. The inclusion of the penalty parameter, however, aﬀords us the
use of a large number of knots. It is customary to select these knots in quasi-automated
manner, for example, a large number of them may be placed at the quantiles of the xi. The
penalty parameter λ is usually chosen either through cross-validation methods or through
the mixed-model connection. We refer to Ruppert et al. (2003); Wood (2017) for more details
and illustrative examples for the case of the least-squares penalized spline estimator.
Finally, we brieﬂy review smoothing spline estimators. These estimators arise as solutions
to the variational problem
min
f∈Wq,2([a,b])
"
n−1
n
X
i=1
{Yi −f(xi)}2 + λ
Z
[a,b]

f (q)(x)
	2 dx
#
,
(6)
4


## Page 5


where Wq,2([a, b]) refers to the Sobolev space of order q, that is,
Wq,2([a, b]) = {f : [a, b] →R, f has q −1 absolutely continuous derivatives
f (1), . . . , f (q−1) and
Z b
a
{f (q)(x)}2dx < ∞},
See Adams et al. (2003) for more details on Sobolev spaces. It is a remarkable fact that
without any constraints the solution to the above problem is a special kind of spline: a
natural polynomial spline of degree 2q−1 with knots at xi. This spline may also be written as
a linear combination of B-spline functions with special care so that the boundary conditions
are respected, see De Boor (2001). Since this spline is the unique solution to the problem,
smoothing splines, unlike regression and penalized splines, incur no approximation error.
More details on least-squares smoothing splines may be found in Eubank (1999) while M-
type smoothing splines are discussed in Huber (1979), Cox (1983), Cunningham et al. (1991)
and Eggermont et al. (2009), who study the L1 smoothing spline in detail.
3
M-type penalized spline estimators
3.1
Estimating equations and preliminary scale estimation
Up to now M-type penalized spline estimators have received much less attention in the
literature in comparison to both M-type regression splines and smoothing splines. However,
penalized splines are situated in between regression and smoothing splines and as such are
well-suited for a wide variety of problems. To be precise, the estimator bf(·) = P
j BK,j(·)bβj
that we consider minimizes
1
n
n
X
i=1
ρ
 
Yi −
X
j≤K+p
βjBK,j(xi)
!
+ λ
Z
[a,b]


( X
j≤K+p
βjBK,j(t)
)(q)

2
dt,
(7)
for some nonnegative ρ that is symmetric about zero, satisﬁes ρ(0) = 0 and can be either
convex or non-convex. The choice ρ(x) = x2 brings us back to the least squares minimization
problem, but (7) allows for more general functions that reduce the eﬀect of large residuals.
Examples include Huber’s function (Huber, 1964) given by
ρc(x) =
(
(1/2)x2,
|x| ≤c
c|x| −(1/2)c2,
|x| > c
(8)
where the constant c regulates the degree of resistance. For large values of c one essentially
obtains the ordinary quadratic loss function but for smaller values a higher degree of ro-
bustness is achieved. Many other ρ-functions can be constructed by imitating parametric
likelihood models, such as the Cauchy, logistic and Laplace models. The case of a Laplace
model, in particular, leading to the L1 loss function may be understood as a limiting case of
the Huber loss function for c →0.
5


## Page 6


For ease of notation deﬁne the spline basis vector evaluated at x as B(x), that is,
B(x) := {BK,1(x), . . . , BK,K+p(x)}⊤, denote the n × (K + p) spline design matrix with
B := {B⊤(x1), . . . , B⊤(xn)}⊤and let Di,j =
R
B(q)
K,jB(q)
K,i.
See De Boor (2001, pp.
116-
117) for derivative expressions for B-splines. With this notation, it is easy to see that the
minimizer bβ satisﬁes
−1
n
n
X
i=1
ρ′ 
Yi −B⊤(xi) bβ

B(xi) + 2λD bβ = 0.
The solution is unique for strictly convex ρ-functions but non-unique otherwise.
To include a preliminary scale estimate bσ it suﬃces to modify the ρ function according
to ρbσ(x) := ρ(x/bσ). Traditionally in robust statistics, see, e.g., Maronna et al. (2006), bσ
is obtained by an initial robust regression ﬁt to the data. This may be avoided by using
the technique of pseudo-residuals as in Cunningham et al. (1991). Speciﬁcally, assuming
x1 < . . . < xn, let
bϵi = wiYi−1 + siYi+1 −Yi,
i = 2, . . . , n −1
(9)
with
wi = (xi+1 −xi)/(xi+1 −xi−1)
and
si = (xi −xi−1)/(xi+1 −xi−1).
It is easy to see that the pseudo-residuals are constructed by using straight line ﬁts on two
outer observations in order to predict the middle observation. Gasser et al. (1986) proposed
estimating σ2 in (1) using
bσ2 =
1
n −2
n−1
X
i=2
bϵ2
i
w2
i + s2
i + 1,
where the standardization results from noticing that E{|bϵi|2} = (w2
i + s2
i + 1)σ2 + O(n−2)
for f(·) ∈C2[a, b]. The sample variance is not robust with respect to outliers but robust
estimates can also be obtained from pseudo-residuals. For example, one may compute the
median absolute deviation, an M-scale or the inter-quartile range (IQR), as suggested by
Cunningham et al. (1991) in the context of smoothing splines. Another class of robust scale
estimators may be constructed using pairwise diﬀerences of Yi. In particular, Boente et al.
(1997) propose estimating σ with
bσ = (21/20.6745)−1 median |Yi+1 −Yi|,
which may be viewed as a robust alternative to the well-known Rice estimator.
It should be noted that contrary to unpenalized regression, such as regression splines,
standardizing with a scale estimate will not, in general, lead to scale equivariant estimates.
This will be approximately the case, though, provided that the penalty term is negligible,
that is, either λ is small or
R
{ bf (q)}2 is small, i.e., the estimating function is "close" to being
a polynomial. Nevertheless, the inclusion of a robust scale estimate leads to useful diagnostic
tools for outliers, see the real data examples of Section 6 for some interesting illustrations.
6


## Page 7


3.2
Computation and smoothing parameter selection
The success of any penalized spline estimator, least-squares and robust alike, rests on
appropriate selection of the smoothing parameters: the dimension of the spline basis and the
penalty parameter. Here, we shall assume that the order of the spline and the penalty has
been ﬁxed in advance by the practitioner, common choices being p = 4 and q = 2. First, we
make a brief note on the computation of the penalized estimates.
The solution to (7) may be computed eﬃciently by a modiﬁcation of the well-known
iteratively reweighted least squares (IRWLS) algorithm (Maronna et al., 2006).
Deﬁne
ri(β) = Yi −B⊤(xi)β, let Wi(β) = ρ′(ri(β)/bσ)/(ri(β)/bσ), i = 1, . . . , n and put W(β) =
diag{Wi(β)}. It can be seen that bβ satisﬁes
−(nbσ2)−1
n
X
i=1
Wi(bβ)
n
Yi −B⊤(xi)bβ
o
B(xi) + 2λDbβ = 0.
(10)
Thus bβ is the minimizer of a weighted penalized least-squares criterion. This suggests an
iterative scheme for the computation of bβ. At the mth step one deﬁnes weights Wi(β(m)), i =
1, . . . , n and obtains the updated approximation to bβ, β(m+1), by solving
n
n−1B⊤W(β(m))B + 2bσ2λD
o
β(m+1) = n−1B⊤W(β(m))Y.
It follows from arguments given in Maronna et al. (2006); Huber et al. (2009) that the
procedure is guaranteed to converge to bβ, independently of the starting point, provided
that ρ is convex, symmetric about zero and ρ′(x)/x is bounded and monotone decreasing
for x > 0. Omitting the convexity assumption has the consequence that the algorithm still
converges but convergence may instead be to a local minimum. Thus, the choice of the
starting point becomes crucial.
Due to the banded structure of the matrices involved, successive systems of linear equa-
tions can be solved in O(K) computations, after forming the necessary matrices. This needs
to be contrasted with the O(n) computations that would have been required by smoothing
splines with the B-spline basis. Since often K << n, penalized spline estimators require
much less computational eﬀort, particularly for large datasets. Moreover, as Wahba (1990,
Chapter 7) notes, a ridge regression type argument shows that there always exists a λ > 0
such that the mean-squared error of the corresponding penalized spline estimator is smaller
than for λ = 0, i.e., for the regression spline estimator. These facts illustrate the balance
penalized splines seek to achieve.
To implement the estimator we follow the recommendation in Ruppert et al. (2003,
Chapter 5) for the number and location of knots. Speciﬁcally, we take
K = min{1/4 × number of unique xi, 40},
(11)
and for the interior knots
tk =
 k + 1
K + 2

th sample quantile of the unique xi,
(12)
7


## Page 8


for k = 1, . . . , K. Both K and the location of the knots are chosen independently of λ, as
experience with penalized splines has shown that λ is more important than K, provided that
the latter quantity is taken large enough. To choose λ we use the generalized cross-validation
(GCV) criterion adapted from Cunningham et al. (1991), that is,
GCV(λ) =
n−1 Pn
i=1 Wi(bβ)
n
Yi −B⊤(xi)bβ
o2
{1 −n−1 Tr H(λ)}2
(13)
where H(λ) = B{B⊤W( bβ)B + 2nλbσ2D}−1B⊤W( bβ)Y is the hat matrix obtained upon
convergence of the algorithm. We choose λ as the minimizer of this function.
The minimization is usually carried out with a blind grid search leaving to the user
the awkward speciﬁcation of the candidate penalty values.
In order to produce a fully
automatic method we recommend using a numerical derivative-free optimizer such as the
Nelder-Mead method (Nocedal et al., 2006, 238–240). The method is available in standard
software, converges fast and, in our experience, works well for a wide variety of problems. It
is therefore our preferred choice for the simulation experiments and the real data analyses
presented herein.
4
Asymptotic properties
We now investigate the rates of convergence of the M-type penalized spline estimator
deﬁned in (7), both with and without the use of an auxiliary scale estimate. For the purpose
of comparison, we ﬁrst list the asymptotic mean-squared errors of regression and smoothing
spline estimators under their respective assumptions. For either least-squares or M-type
regression spline estimates deﬁned in (3)-(4), denoted generically by bfrsp(·), one has
1
n
n
X
i=1
{ bfrsp(xi) −f(xi)}2 = OP
K
n

+ OP
 K−2p
,
(14)
for f(·) ∈Cp[a, b], see Shi et al. (1995). On the other hand, for least-squares and M-type
smoothing splines, denoted generically by bfsmsp(·), one has
1
n
n
X
i=1
{ bfsmsp(xi) −f(xi)}2 = OP

1
nλ1/2q

+ OP (λ) ,
(15)
for f(·) ∈Wq,2([a, b]), as seen from the results of Wahba (1990) and Cox (1983). It follows
from these results that with appropriate selection of the smoothing parameters K and λ,
bfrsp(·) and bfsmsp(·) can attain the optimal rates of convergence for Cp([a, b]) and Wq,2([a, b])
functions respectively (Stone, 1982). Since Cq([a, b]) ⊂Wq,2([a, b]) smoothing splines require
somewhat milder smoothness assumptions in order to attain the same rates of convergence.
It should be noted that the above results cannot be directly extended to M-type penalized
splines since regression splines do not take into account the eﬀect of the penalization while
8


## Page 9


smoothing splines ignore the approximation error incurred by the sieved nature of penalized
splines. An independent treatment is thus required. The assumptions that will be needed
for our theoretical development are as follows.
A.1 For the unique knots {ti}K+p
i=p
deﬁne hi := ti −ti−1 and h := maxi hi. Assume that
maxi |hi+1 −hi| = o(K−1) and there exists a constant M such that (h/ mini hi) ≤M.
A.2 For deterministic design points xi ∈[a, b], i = 1, . . . , n, assume that there exists a dis-
tribution function Q with corresponding continuous density w bounded away from zero
and inﬁnity such that, with Qn the empirical distribution of x1, . . . , xn, supx |Qn(x) −
Q(x)| = o(K−1).
A.3 The number of knots K = o(n).
Assumption 1 essentially requires that the knots are quasi-uniform and dense in [a, b]. As-
sumption 2 is a weak restriction on the knot distribution and ﬁnally, assumption 3 puts a
limit to the rate of growth of the knots, that is, the number of predictor variables in the re-
gression model. This is a common assumption for sieved estimators, see Eubank (1999) and
Eggermont et al. (2009). All three assumptions are also used for the least-squares setting.
For the M-type estimators considered herein we require the following additional assumption
on the ρ-function and the distribution of ϵ.
A.4 For ψ(·) := ρ′(·) we require ψ(·) ∈C2(−∞, ∞) and satisﬁes supx |ψ′′(x)| < ∞,
E{ψ(ϵ)} = 0, E{ψ′(ϵ)} > 0, E{|ψ(ϵ)|2} < ∞and E{|ψ′(ϵ)|2} < ∞.
Examples of ρ-functions that satisfy the smoothness conditions are the convex logistic and
the non-convex Tukey bisquare. The Huber ρ-function does not meet these requirements
but smoothed, yet asymptotically equivalent versions of it do, see Hampel et al. (2011a)
for a possible smoothing scheme. As Huber (1973) notes, the smoothness conditions on ρ
are technically convenient but seem hardly essential for the results to hold. The moment
conditions involving the ψ-function occur very often in the context of robust estimation, see
Maronna et al. (2006). In essence, they are identiﬁability (Fisher-consistency) conditions so
that the correct function f(·) is estimated.
Following Huber (1973) and Cox (1983) we aim to approximate the M-type penalized
spline estimator with a sequence of special least-squares estimators. To that end, let us
deﬁne the pseudo-observations
eYi = f(xi) +
ψ(ϵi)
E{ψ′(ϵ)},
(16)
and let ef(·) := B⊤(·)eβ be the minimizer of
1
n
n
X
i=1
(
eYi −
X
j≤K+p
βjBK,j(xi)
)2
+
λ
E{ψ′(ϵ)}
Z
[a,b]


( X
j≤K+p
βjBK,j(t)
)(q)

2
dt.
9


## Page 10


Motivation for the use of pseudo-observations may be found in the linearization of univariate
M-estimators that is achieved with the help of the inﬂuence function (Maronna et al., 2006).
Note that by A.4 the ψ(ϵi) have mean zero and ﬁnite squared expectation. Thus, Theorem
1 of Claeskens et al. (2009) applies for this theoretical least-squares estimator. With the
notation of Section 3, let us ﬁnally deﬁne the estimating equations
Φ(β) = −1
n
n
X
i=1
ψ
 Yi −B⊤(xi)β

B(xi) + 2λDβ
(17)
Ψ(β) = −1
n
n
X
i=1
{eYi −B⊤(xi)β}B(xi) +
2λ
E{ψ′(ϵ)}Dβ.
(18)
The solution to (7) is a zero of Φ. The zero of Ψ, ef(·) := P
j eβjBK,j(·), does not correspond
to a real estimator, but its implied theoretical properties help in establishing the rates of
convergence of bf(·) with respect to the semi-norm ||g||2
n := n−1 P
i=1 |g(xi)|2.
For notational simplicity, dependence on n is, in general, suppressed whenever possible.
Further, for reasons of convenience both here and in our proofs we also identify each spline
function s(·) = P
j βjBK,j(·) with its coeﬃcient vector β. This comes without confusion as
all ﬁnite-dimensional spaces are isomorphic to Euclidean spaces of equal dimension.
Theorem 1. Let bf(·) = B⊤(·)bβ denote a solution of Φ(β) = 0. Assume A.1-A.4 and write
Cn := E{|| ef −f||2
n}. Then for any δ > 0 there exists n0 such that for all n ≥n0
Pr
h
there is a solution bf(·) to Φ(β) = 0 satisfying || bf −ef||2
n ≤δCn
i
≥1 −δ.
Equivalently, there exists a sequence of M-type penalized spline estimates bfn(·) such that
|| bf −ef||2
n/Cn
P−→0.
The theorem states that with high probability there exists an M-type penalized spline
estimate bf(·) such that bf(·) and ef(·) will be much closer than ef(·) and f(·). Theorem 1
further establishes a useful representation of M-estimators: in a certain sense, M-estimators
are equivalent to least-squares estimators applied on the pseudo-observations given in (16).
This illustrates how diﬀerent ρ-functions operate on the error term: large errors will be either
trimmed or discarded based on whether ρ is convex or non-convex with ﬁnite rejection point,
(Hampel et al., 2011b).
Additionally, since
|| bf −f||2
n ≤2|| bf −ef||2
n + 2|| ef −f||2
n = oP(Cn) + OP(Cn) = OP(Cn),
the conclusion is that bf(·) will enjoy the same rates of convergence as the least squares
estimator ef(·). In particular, let
10


## Page 11


Kq,n = ec1/2q
1
(Kn + p −q)λ1/2q
n
,
where the constant ec1 is deﬁned in Lemma A3 of Claeskens et al. (2009) and depends only
on q and the design density w(·). The sequence Kq,n determines the order of the asymptotic
mean squared error, as Theorem 2 shows.
Theorem 2. Under assumptions A.1-A.4 the following statements hold
(a) If Kq,n < 1 eventually and f(·) ∈Cp[a, b] for p > 1, then there exists a sequence of
penalized spline M-estimates bfn(·) satisfying
|| bfn −f||2
n = OP
K
n

+ OP
 λ2K2q
+ OP
 K−2p
(b) If Kq,n ≥1 eventually, f(·) ∈Cq[a, b] and limn nλ(2q+1)/2qK2q−1 = limn λK4q−1 = ∞, then
there exists a sequence of penalized spline M-estimates bfn(·) satisfying
|| bfn −f||2
n = OP

1
nλ1/2q

+ OP (λ) + OP
 K−2q
Theorem 2 establishes the least-squares mean-squared errors for penalized M-estimators
without requiring any moments of the error term.
Thus, while inﬁnite error variance
would make least-squares estimators inconsistent, M-estimators with bounded ψ functions
still maintain their consistency. It should be noted that the conditions p > 1 as well as
limn nλ(2q+1)/2qK2q−1 = limn λK4q−1 = ∞(in parts (a) and (b), respectively) are purely
technical and are not needed by Claeskens et al. (2009). They are important for the M-type
estimators because they allow us to control the leverages, which are important quantities in
the asymptotics of robust regression estimators with a diverging number of parameters, see
Huber (1973); Yohai et al. (1979); Cox (1983) and the proof of Theorem 1.
The rates are extremely interesting because they illustrate the compromise between re-
gression and smoothing splines depending on how fast the number of knots grows, which
is essentially what the condition on Kq,n entails. In the ﬁrst case, we have an asymptotic
scenario that is similar to that of robust regression splines, cfr. (14). The additional term
λ2K2q reﬂects the shrinkage bias from the penalty parameter and is negligible for a small
number of knots. On the other hand, with a larger rate of growth for the number of knots
one is led to an asymptotic scenario that is very similar to that of least-squares or M-type
smoothing splines, cfr. (15). The additional term K−2q is the result of the error of approxi-
mation for a Cq[a, b] function by a spline, see the Jackson-type inequality in (De Boor, 2001,
Chapter XII). As discussed previously, smoothing splines incur no approximation error as
they are exact solutions to the minimization problem (6).
Balancing all the MSE components in case (a), by setting Kn ≍n1/(2p+1) and λ ≍n−γ
where γ > (p + q)/(2p + 1), yields || bf −f||2
n = OP(n−2p/(2p+1)), which is the optimal rate
of convergence for f(·) ∈Cp[a, b]. Similarly, taking Kn ≍nv, with v ≥1/(2q + 1), and
λn ≍n−2q/(2q+1) in case (b) yields || bf−f||2
n = OP(n−2q/(2q+1)), the optimal rate of convergence
11


## Page 12


for f(·) ∈Cq[a, b] (Stone, 1982). Since we have assumed that p > q, the rates of convergence
in case (a) are faster than in case (b). As Claeskens et al. (2009) remark, this fact provides
justiﬁcation for selecting a small number of knots relative to n for penalized spline estimators.
Theorem 2 only asserts the existence of a "good" sequence of estimates. Naturally, this may
be strengthened to both existence and uniqueness if one uses a strictly convex ρ-function.
The empirical norm || · ||n depends on xi so that the question arises of whether it is
possible to obtain rates of convergence with respect to a global measure. Corollary 1 shows
that this is indeed possible with respect to the standard L2([a, b]) metric denoted by || · ||.
Rates of convergence for the derivatives in the L2([a, b]) metric may also be obtained.
Corollary 1. Assume A.1-A.4 and let bfn(·) denote the sequence of penalized M-estimates
of Theorem 1. Then, if f ∈Cp[a, b], K ≍n1/(2p+1) and λ ≍n−γ for γ > (p + q)/(2p + 1),
|| bf (j) −f (j)||2 = OP(n−(2p−j)/(2p+1)),
while if f ∈Cq[0, 1], K ≍nv with v ≥1/(2q + 1) and λ ≍n−2q/(2q+1),
|| bf (j) −f (j)||2 = OP(n−(2q−j)/(2q+1)).
Corollary 1 shows that, as one may expect, higher-order derivatives are more diﬃcult to
estimate. Unfortunately, this cannot be improved as these rates of convergence are optimal
under the weak assumptions of Stone (1982).
We now turn to the problem of penalized spline M-estimation with auxiliary scale es-
timation, such as the IQR of the pseudo-residuals discussed in Section 3. The estimating
equations are now modiﬁed to
Φbσ(β) = −1
n
n
X
i=1
ψ
Yi −B⊤(xi)β
bσ
 B(xi)
bσ
+ 2λDβ
(19)
Ψσ(β) = −1
n
n
X
i=1

eYi −B⊤(xi)β

B(xi) + 2λ
σ2
E{ψ′(ϵ/σ)}Dβ,
(20)
with eYi = f(xi) + σψ(ϵi/σ)/E{ψ′(ϵ/σ)}. We aim to show analogues of Theorems 1 and 2 for
this case. To that end we need a root-n condition on bσ and a modiﬁcation of A.4, as follows:
B.4 √n(bσ −σ) = OP(1) for some scaling constant σ.
B.5 ψ(·) ∈C2(−∞, ∞) with supx |ψ′′(x)| < ∞. For any ϵ > 0 there exists Mϵ < ∞such
that
|ψ(tx) −ψ(sx)| ≤Mϵ|t −s|,
for all t, s > ϵ and −∞< x < ∞.
Further, E{ψ(ϵ/σ)} = 0, E{ψ′(ϵ/σ)} > 0,
E{|ψ(ϵ/σ)|2} < ∞and E{|ψ′(ϵ/σ)|2} < ∞.
12


## Page 13


The scaling constant σ does not need to be the standard deviation of the error term,
but it can be when the error has ﬁnite variance. Assumption B.5 implies the smoothness
of ψ but also that ψ changes slowly in the tail. The latter also implies that ψ is bounded.
This condition was also used by He et al. (1995) and is satisﬁed, e.g., by redescending
ψ functions and Huber ψ-functions modulo the smoothness assumption, see the remarks
following A.4. The moment conditions parallel those of A.4 and ensure the Fisher-consistency
of the estimates.
With these assumptions we can prove that there still exists a sequence of M-estimates
that achieves the optimal rates of convergence.
Theorem 3. Under assumptions A.1-A.3 and B.4-B.5 there exists a sequence of M-type
penalized spline estimates bfn(·) solving Φbσ(β) = 0 for which the following statements hold:
(a) If f(·) ∈Cp[a, b], K ≍n1/(2p+1) and λ ≍n−γ with γ > (q + p)/(2p + 1),
|| bf −f||2
n = OP(n−2p/(2p+1)).
(b) If f(·) ∈Cq[a, b], K ≍nv with v > 1/(2q + 1) and λ ≍n−2q/(2q+1),
|| bf −f||2
n = OP(n−2q/(2q+1)).
Note that the rate of growth of the knots and the rates of decay for λ in each one of these
cases ensure that we eventually have either Kq,n < 1 or Kq,n ≥1. Corollary 1 regarding
rates of convergence of derivatives in the L2([a, b]) metric carries over to this case in the same
manner as previously. In general, scale estimators constructed using linear combinations of
Yi, such as those discussed in Section 3.1, satisfy the root-n condition and thus provide good
preliminary scale estimates.
5
A Monte-Carlo study
In our simulation experiments we compare the performance of the M-type penalized spline
estimator with auxiliary scale to the least-squares penalized spline and smoothing spline es-
timators. For the penalized M-estimator we use the Huber ρ-function with tuning parameter
equal to 1.345, corresponding to 95% eﬃciency in the location model. The auxiliary scale
estimate is the IQR of the pseudo-residuals and we select the smoothing parameters for
the penalized spline M-estimator as outlined in Section 3.2. The least-squares estimators
can be easily ﬁtted with the gam function (Wood, 2019) in the freeware R, (R Development
Core Team, 2019). By default, the penalty parameter is estimated by restricted maximum
likelihood, see Ruppert et al. (2003) and Wood (2017) for more details on this technique.
We investigate the performance of the estimators in the regression model Yi = f(ti) + ϵi
where ti = i/n and f(·) is each of the following three functions
1. f1(t) = sin(2πt) + exp{−3(t −0.5)2} + 0.4,
2. f2(t) = 1/(0.1 + t) + 8 exp{−400(t −0.5)2},
13


## Page 14


3. f3(t) = φ((t −0.5)/0.15) −φ((t −0.8)/0.04),
where φ(·) denotes the Gaussian density. All three functions are smooth but they diﬀer
qualitatively as f2(·) and f3(·), in contrast to f1(·), exhibit strong local characteristics in the
form of spikes and bumps.
In order to assess the eﬀect of outliers on the estimates diﬀerent distributions for the
error term were considered. Other than the standard Gaussian distribution, we have com-
plemented our set-up with a t-distribution with 3 degrees of freedom, a mixture of mean-zero
Gaussians with standard deviations equal to 1 and 9 and weights equal to 0.85 and 0.15 re-
spectively, as well as Tukey’s Slash distribution.
The resulting mean-squared-errors are
summarized in Table 1 for sample sizes of 100 and 1000 replications.
Huber(Psp)
Least-squares(Psp)
Least-squares(Smsp)
f(·)
Distribution
Mean
Median
Mean
Median
Mean
Median
f1(·)
Gaussian
0.067
0.055
0.068
0.052
0.062
0.049
t3
0.100
0.079
0.186
0.129
0.190
0.184
M. Gaussian
0.144
0.107
0.714
0.454
0.701
0.418
Slash
0.968
0.355
4979.6
5.761
5084.5
6.012
f2(·)
Gaussian
0.225
0.217
0.203
0.198
0.212
0.198
t3
0.359
0.323
0.487
0.419
0.515
0.430
M. Gaussian
0.699
0.535
1.772
1.594
1.883
1.583
Slash
4.051
3.029
2476.7
8.506
2790.2
9.341
f3(·)
Gaussian
0.056
0.045
0.064
0.048
0.062
0.047
t3
0.080
0.056
0.154
0.092
0.143
0.087
M. Gaussian
0.079
0.061
0.665
0.350
0.550
0.306
Slash
0.481
0.146
1892.39
5.998
2604.5
5.489
Table 1: Means and medians of the 1000 MSEs of the penalized spline Huber M-estimator,
the penalized spline least-squares estimator and the smoothing spline least-squares estimator.
Comparing the two least-squares estimators reveals that using fewer basis functions than
the number of observations hardly impacts performance. The results further demonstrate
the extreme sensitivity of least-squares estimators with respect to even a small number of
aberrant observations. We note, in particular, that both the t-distribution with 3 degrees
of freedom and the mixture of Gaussian distributions have ﬁrst moments equal to zero and
ﬁnite second moments yet the performance of least-squares estimators is unduly aﬀected.
By contrast, the Huber estimator matches the performance of the least-squares estimator
in Gaussian data and exhibits a large degree of resistance to aberrant observations. These
facts illustrate the favourable trade-oﬀpenalized M-estimators tend to achieve.
14


## Page 15


6
Real data examples
6.1
Mid-atlantic wage data
We now illustrate the proposed M-type penalized spline estimators on two real datasets:
the mid-atlantic wage dataset and the mammals dataset. For the purpose of comparison we
also include the least-squares estimator. The datasets are freely available in the R-packages
ISLR (James et al., 2013) and quantreg (Koenker et al., 2012) respectively.
The mid-atlantic wage dataset consists of 3000 observations on diﬀerent characteristics
of male workers in the said region of the United States. The dataset contains eleven socio-
economic variables but here we focus on the relationship between age in years and yearly
raw wages recorded in 2011 US dollars. Typically, income distribution is right-skewed so
a few outlying observations would be the rule rather than the exception. A scatter-plot of
these variables with the Huber and the least-squares penalized ﬁts is shown in the left panel
of Figure 1.
Figure 1: Left: scatter plot of the mid-atlantic wage dataset with least-squares (dashed
curve) and Huber (solid curve) ﬁts superimposed. Right: A closer look at the ﬁts with
a rescaled vertical axis.
The symbols ▲, ♦, ■correspond to observations with weights
(0, 0.33], (0.33, 0.66], (0.66, 1] respectively.
Both ﬁts point towards a curvilinear relationship with a slight bend downwards; this
reﬂects the fact that workers reach their peak income at the middle of their work life and their
income slightly decreases afterwards. Some care, however, is needed in this interpretation as
relatively few observations are available for workers past the usual retirement age.
Comparing the ﬁts in more detail leads us to notice that the least-squares ﬁt overestimates
the mean salary for younger to middle-aged workers; this may be explained by observing that
a number of very high-earners exert disproportionate inﬂuence on the estimate, eﬀectively
15


## Page 16


pulling the ﬁt upwards. By contrast, the M-estimator remains largely resistant to these
atypical observations. To better understand this discrepancy the plot also includes color and
shape coding based on the weights generated by the M-estimator. While all observations
receive equal weights by the least-squares estimator, the observations corresponding to atyp-
ically high-earners are greatly down-weighted by the M-estimator leading to diﬀerences in
the ﬁts. Restricting attention to observations in the middle on the right panel shows that
these diﬀerences can be as high as 10000 US dollars, which is a respectable amount of money
from both individual and policy standpoints.
6.2
Mammals weight and speed data
The mammals dataset consists of 107 observations on maximal running speeds and
weights of mammals, see Garland (1983) for more information as well as a parametric re-
gression analysis of this relationship. A scatter plot of these variables with the Huber and
the least-squares penalized ﬁts is shown in the left panel of Figure 2.
Figure 2: Left: scatter plot of the mammals dataset with least-squares (dashed curve) and
Huber (solid curve) ﬁts superimposed. Right: QQ plot of the residuals of the Huber ﬁt.
The symbols ▲, ♦, ■correspond to observations with weights (0, 0.33], (0.33, 0.66], (0.66, 1]
respectively.
The scatter plot and the ﬁts easily refute the naive hypothesis that speed should be a
decreasing function of weight. Curiously, speed seems to increase with weight up to a certain
point, which we may call "optimal weight", and decrease afterwards. That is, neither the
smallest nor the largest animals are the fastest.
Several outliers signiﬁcantly impact the least-squares analysis, however. These for the
most part correspond to small rodent-like animals (see the included labels) whose speed is far
below what could be expected given their weight. The eﬀect of these outlying observations is
16


## Page 17


again to pull the least-squares ﬁt towards them resulting in substantial added curvature. On
the contrary, the 4 most outlying observations receive a near-zero weight by the M-estimator
and as a result their impact on the estimated regression function is limited. The QQ plot
in the right panel indicates that rather than trying to ﬁt all observations, the M-estimator
only focuses on the "good" majority for which it provides a better ﬁt than the least-squares
estimator.
Overall, both examples illustrate the beneﬁts of using an M-type penalized spline esti-
mator for the analysis of data with atypical observations.
7
Discussion
The results in this paper indicate that there is little theoretical diﬀerence between
least-squares and general M-type penalized spline estimators. In particular, the ﬁndings
of Claeskens et al. (2009) in support for a smaller number of knots also apply to M-type
penalized spline estimators. The latter class of estimators is broad enough to include the
least-squares estimator as a special case but also includes estimators that are much less sus-
ceptible to atypical observations while performing as well as the least-squares estimators in
clean data sets. For these M-type estimators, under some weak restrictions the results carry
over even if one uses a preliminary scale estimate as a means of standardization. This can be
useful for outlier detection, as demonstrated in our two real-data examples. In eﬀect, we view
the proposed penalized spline estimator as the ﬁrst of its kind combining good theoretical
properties and computational ease.
It would be of great interest to extend the penalized spline estimation techniques pre-
sented here to robust generalized linear models, using, e.g., the estimator proposed by Can-
toni et al. (2001). Generalized additive models have been immensely popular in recent years
due to their ﬂexibility and ease of use and we are conﬁdent that M-type penalized spline
estimation can be successfully used in this context as well. Another important area where
robust penalized sieved estimators can be successful is functional regression and its variants,
which have also attracted great interest recently. We aim to study such extensions in detail
as a part of our future work.
Software availability
An implementation of the M-type penalized spline estimator with settings described
herein may be found in the website https://wis.kuleuven.be/statdatascience/robust/
papers-2010-2019. The code also reproduces the plots of Section 6.
Appendix
The Appendix contains the proofs of Theorem 1, Corollary 1 and Theorem 3. A proof
that the computational algorithm converges to a stationary point of the objective function
17


## Page 18


is available from the authors upon request.
We start with two lemmas that are crucial for the proofs of the results of Section 4.
Lemma 1 essentially states that splines are excellent approximators of smooth functions and
Lemma 2 establishes a set of strong Lindeberg-type conditions on the rows of the spline-
design matrix.
Lemma 1. For each f(·) ∈Cj[a, b] there exists a spline function sf of order p, p > j such
that
sup
x∈[a,b]
|f(x) −sf(x)| ≤const.p,j |t|j
sup
|x−y|<t
|f (j)(x) −f (j)(y)|
where t = maxi |ti −ti−1| and the constant depends only on p and j.
Proof. See De Boor (2001, pp.145-149).
Lemma 2. Deﬁne G := n−1 Pn
i=1 B(xi)B⊤(xi) + λD with B(xi) and D deﬁned in Section
3.1. Under A.1-A.3 the following asymptotic relations hold
(i) n−1 max1≤i≤n B⊤(xi)G−1B(xi) = o(1), as n →∞.
(ii) Cn max1≤i≤n B⊤(xi)G−1B(xi) = o(1) as n →∞,
(iii) max1≤i≤n B⊤(xi)G−1B(xi)/(Cnn) = O(1) as n →∞, under the conditions of Theorem
3.
where Cn = E{|| ef −f||2
n} is the average mean-squared error of the theoretical least-squares
estimator.
Proof. It suﬃces to prove (ii) and (iii) as (i) follows directly from (ii) given that Cn converges
to zero at a rate strictly lower than the parametric rate.
Assume ﬁrst that Kq,n < 1 eventually. Either by Lemma 6.2 of Shen et al. (1998) or by
Lemma 5.1 of Shi et al. (1995) it follows that for large n there exists a positive constant c
such that
λmin(n−1
n
X
i=1
B(xi)B⊤(xi)) ≥cK−1,
where λmin(·) denotes the function that returns the smallest eigenvalue of a symmetric pos-
itive semi-deﬁnite matrix. Further, since for any β ∈RK+p,
0 ≤
Z
[a,b]


( X
j≤K+p
βjBK,j(t)
)(q)

2
dt = β⊤Dβ,
18


## Page 19


the penalty matrix D is positive semi-deﬁnite and, as λ > 0, we ﬁnd that
max
1≤i≤n B⊤(xi)G−1B(xi) ≤max
1≤i≤n B⊤(xi)
(
n−1
n
X
j=1
B(xj)B⊤(xj)
)−1
B(xi)
≤c−1K max
1≤i≤n
K+p
X
ℓ=1
|Bk,ℓ(xi)|2
≤c−1K max
1≤i≤n
max
1≤ℓ≤K+p Bk,ℓ(xi)
|
{z
}
≤1
K+p
X
ℓ=1
Bk,ℓ(xi)
|
{z
}
=1
≤c−1K,
by properties (b) and (c) of the B-spline functions. Result (ii) now follows from the expression
for Cn for Kq,n < 1 of Theorem 2 and the additional assumption that p > 1.
In the case that Kq,n ≥1 eventually we need a tighter bound for the smallest eigenvalue
G, as given in Lemma A1 of Claeskens et al. (2009). In particular, for Kq,n ≥1 these authors
show that with probability tending to one
λmin(G) ≥cK−1(1 + K2q
q,n),
for the same constant c. Since K2q
q,n ∼ec1K2qλ, to check (ii) it suﬃces to establish that

1
nλ1/2q + λ + K−2q

K1−2qλ−1 = oP(1),
as n →∞. This holds by assumption. In particular, it holds for λ ≍n−2q/(2q+1) and K ≍nv
with v ≥1/(2q + 1) that lead to the optimal rates of convergence.
To prove (iii) note that either Cn ≍n−2p/(2p+1) or Cn ≍n−2p/(2p+1) under the conditions
of Theorem 3, that is, the rates of growth of K and the rates of decay of λ. The statement
follows from simple multiplication.
We now turn to the proof of Theorem 1.
Proof of Theorem 1. From Lemma 1 there exists a spline function f ⋆such that
sup
x∈[a,b]
|f(x) −f ⋆(x)| = O(DK),
where DK = K−p or DK = K−q depending on whether f ∈Cp[a, b] or f ∈Cq[a, b] respec-
tively. Since B-splines form a basis for Sp
K we can put f ⋆= PK+p
j=1 β⋆
j BK,j.
Expanding Ψ we can write
Ψ(β) = −1
n
n
X
i=1

f(xi) −B⊤(xi)β
	
B(xi) −
1
nE{ψ′(ϵ)}
n
X
i=1
ψ(ϵi)B(xi) + 2
λ
E{ψ′(ϵ)}Dβ.
19


## Page 20


Let λ0 := 2λ/E{ψ′(ϵ)} and deﬁne, as before,
G := n−1B⊤B + λ0D.
Recall that ψ(·) ∈C2(−∞, ∞), by A.4. A Taylor expansion allows us to write
n
X
i=1
ψ
 Yi −B⊤(xi)β

B(xi) =
n
X
i=1
ψ
 ϵi + f(xi) −B⊤(xi)β

B(xi)
=
n
X
i=1
ψ(ϵi)B(xi) +
n
X
i=1
ψ′(ϵi)

f(xi) −B⊤(xi)β
	
B(xi)
+ 1
2
n
X
i=1
ψ′′(ci)

f(xi) −B⊤(xi)β
	2 B(xi).
for some mean values ci, each depending on the ith observation.
On RK+p deﬁne the bilinear form
∥β∥2
G := n−1||BG−1β||2
E,
where || · ||E denotes the usual euclidean norm. We note that|| · ||G is well-deﬁned because
G is invertible for large n, see the proof of Lemma 1. From the triangle inequality we have
∥Ψ(β) −Φ(β)/E{ψ′(ϵ)}∥G ≤T1 + T2,
with
T1 =





1
nE{ψ′(ϵ)}
n
X
i=1
ψ′(ϵi)

f(xi) −B⊤(xi)β
	
B(xi) −1
n
n
X
i=1

f(xi) −B⊤(xi)β
	
B(xi)





G
=





1
nE{ψ′(ϵ)}
n
X
i=1

f(xi) −B⊤(xi)β
	
{ψ′(ϵi) −E{ψ′(ϵ)}} B(xi)





G
,
and
T2 =





1
2nE{ψ′(ϵ)}
n
X
i=1
ψ′′(ci)

f(xi) −B⊤(xi)β
	2 B(xi)





G
.
Using A.2, A.4 as well as the independence and identical distributions of ϵi, we have
ET 2
1 =
Var{ψ′(ϵ)}
n2 (E{ψ′(ϵ)})2
n
X
i=1

f(xi) −B⊤(xi)β
	2 ∥B(xi)∥2
G
≤n−1 max
1≤i≤n ∥B(xi)∥2
G
E{|ψ′(ϵ)|2}
(E{ψ′(ϵ)})2n−1
n
X
i=1

f(xi) −B⊤(xi)β
	2 .
(21)
20


## Page 21


The second term, T2, can now be estimated similarly to give the bound
T2 ≤sup| ψ′′(x)|
2E{ψ′(ϵ)} n−1
n
X
i=1

f(xi) −B⊤(xi)β
	2 ∥B(xi)∥G
≤supx |ψ′′(x)|
2E{ψ′(ϵ)}
max
1≤i≤n ∥B(xi)∥G n−1
n
X
i=1

f(xi) −B⊤(xi)β
	2 ,
where we again have used A.4.
Now let f ⋆= P
j βjBK,j denote the spline approximation to f constructed with the help
of Lemma 1 and let ef(·) = P
j eβjBK,j(·) denote the zero of Ψ. We have
|| ef −f ⋆||2
n ≤2|| ef −f||2
n + 2||f −f ⋆||2
n = OP(Cn) + O(DK)
(22)
where Cn = E{|| ef −f||2
n}. Since the approximation error DK is included in Cn, see Theorem
1 of Claeskens et al. (2009), we conclude that || ef −f ⋆||2
n = OP(Cn) and hence there exists a
constant K1(δ) such that || ef −f ⋆||n ≤1/2(K1Cn)1/2 for all large n with probability greater
than 1 −δ/4.
Deﬁne the sets
Fn :=

s ∈Sp
K : ||s −f ⋆||2
n ≤K1Cn
	
.
(23)
Letting B := (8δ−1 Var{ψ′(ϵ)}(E{ψ′(ϵ)})−2)1/2, Markov’s inequality and (21) imply that
T1 ≤B
 n−1A2
n||f −s||2
n
1/2 ,
where A2
n = maxi≤n ||B(xi)||2
G, with probability greater than 1 −δ/8.
Working now on
Fn, by the previous decomposition it follows that there exists a constant K2(δ) such that
||s −f||2
n ≤K2Cn with probability also greater than 1 −δ/8. Combining these two events
we see that with probability greater than 1 −δ/4
T1 ≤B
 n−1K2CnA2
n
1/2 ,
(24)
for all large n. If s ∈Fn and we set B′ := (2E{ψ′(ϵ)})−1 supx |ψ′′(x)| we also have
T2 ≤B′K2AnCn
(25)
with probability greater than 1 −δ/8 for all large n.
Combining all the above bounds we obtain that for large n
||Φ(β)/E{ψ′(ϵ)} −G(β −β⋆)||G ≤||Φ(β)/E{ψ′(ϵ)} −Ψ(β)||G
+ ||G(β −˜β) −G(β −β⋆)||G
≤B(n−1K2CnA2
n)1/2 + B′K2CnAn + 2−1(K1Cn)1/2
21


## Page 22


on an event with probability greater than 1 −δ, the ﬁrst inequality following from the fact
that
Ψ(β) = Gβ −n−1B⊤Y = Gβ −Geβ,
as eβ is the zero of Ψ and the second inequality from all previous probabilistic bounds.
Factoring (K1Cn)1/2 we may certainly write
||Φ(β)/E{ψ′(ϵ)} −G(β −β⋆)||G ≤
n
B(K2K−1
1 n−1A2
n)1/2 + B′K2K−1/2
1
AnC1/2
n
+ 2−1o
(K1Cn)1/2.
(26)
Further, since D is positive semideﬁnite and λ0 > 0,
A2
n = max
1≤i≤n ||B(xi)||2
G = max
1≤i≤n n−1
n
X
j=1

B⊤(xj)G−1B(xi)
	2
= max
1≤i≤n B⊤(xi)G−1
(
n−1
n
X
j=1
B(xj)B⊤(xj)
)
G−1B(xi)
≤max
1≤i≤n B⊤(xi)G−1B(xi),
(27)
Lemma 2 allows us to deduce that limn A2
nCn = limn n−1A2
n = 0. This in turn means that
the term inside the curly brackets in (26) will be smaller than 1 for n suﬃciently large.
For such n if s ∈Fn −f ⋆with coeﬃcient vector β and we deﬁne
U(β) := β −G−1Φ(β + β⋆)/E{ψ′(ϵ)}
(28)
then on account of (26) we must have ||BU(β)||2
E ≤K1Cn for all large n. The set Fn −f ⋆
is clearly convex. We claim that for suﬃciently large n it is also compact. Indeed, the set
is ﬁnite-dimensional, closed and because the matrix n−1B⊤B is nonsingular for large n, see
the proof of Lemma 2, it is also bounded. Hence the claim holds.
We now see that U(β) is a continuous function mapping the compact, convex set Fn −f ⋆
into itself. Thus, Brouwer’s theorem assures us of the existence of a ﬁxed point s′ in Fn −f ⋆.
Putting bf := s′ + f ⋆, it is easily seen that Φ(bβ) = 0, i.e. bβ is the zero of the estimating
equation .
By the above, and since n−1||B bβ −B eβ||2
E = || bf −ef||2
n, it now follows
|| bf −ef||n = ||Φ(bβ)/E{ψ′(ϵ)} −Ψ(bβ)||G
=
n
B(K2K−1
1 n−1A2
n)1/2 + B′K2K−1/2
1
AnC1/2
n
o
(K1Cn)1/2,
where the inequality holds on an event of probability greater than 1 −δ. Applying again the
limit relations lim n−1A2
n = lim A2
nCn = 0 shows that || bf −ef||2
n = oP(Cn). This concludes
the proof of the theorem.
22


## Page 23


Proof of Corollary 1. The proof follows from Lemma 8 and Lemma 9 of Stone (1985) after
identifying the density w of A.2 with the density of ti. By assumption w fulﬁls Condition 1
of Stone (1985), as it is bounded away from zero and inﬁnity. Check also that K = o(n) by
A.3 and therefore there exists an α > 0 such that
lim
n→∞nα−1K = 0
in either of the two cases K ≍n1/(2p+1) or K ≍nv, v ≥1/(2q + 1).
Proof of Theorem 3. We will show that under the conditions of Theorem 3,
Pr
h
there is a solution bf(·) to Φbσ(β) = 0 satisfying || bf −ef||2
n ≤δCn
i
≥1 −δ,
with Cn := E{|| ef −f||2
n}, where ef denotes the zero of estimating equation (20). Since
||Φbσ(β) −Ψσ(β||G ≤||Φbσ(β) −Φσ(β)||G + ||Φσ(β) −Ψσ(β||G,
and from the proof of Theorem 1 it may be deduced that on Fn there exists a constant D > 0
such that
||Φσ(β) −Ψσ(β||G ≤DC1/2
n ,
the theorem will be proven with a ﬁxed-point argument, provided that we can establish the
existence of another constant Z > 0 such that
||Φbσ(β) −Φσ(β)||G ≤ZC1/2
n .
(29)
Hereafter, we shall use Z > 0 as a generic constant which may take diﬀerent values at
diﬀerent appearance.
To prove the theorem note that, as bσ
P−→σ, for every δ > 0 we
will have bσ−1 ∈(σ−1 −δ, σ−1 + δ) with probability tending to one.
This implies that
bσ−1 ≥(2σ)−1 with probability tending to one. Choose ϵ = (2σ)−1 in B.5. Adding and
subtracting ψ(ri(β)/bσ)σ−1, the boundedness of ψ implied by B.5 yields
ψ
ri(β
bσ
 1
bσ −ψ
ri(β
σ
 1
σ
 ≤Z |bσ −σ|
bσσ
+ Mσ
|bσ −σ|
bσσ
≤Z |bσ −σ|
2σ2
,
for some Z > 0 with probability tending to one.
Thus, there exists a constant Z > 0
depending only on σ such that
|||Φbσ(β) −Φσ(β)||G ≤ZAn|bσ −σ|
with probability tending to one. But n1/2(bσ−σ) = OP(1), by B.4 and AnC−1/2
n
n−1/2 = OP(1),
by the deﬁnition of An, inequality (27) and Lemma 2(iii).
This shows that there exists
another constant Z > 0 such that with high probability
||Φbσ(β) −Φσ(β)||G ≤ZC1/2
n ,
for all large n. The theorem is thus established.
23


## Page 24


8
Bibliography
Adams, J. R. & Fournier, J.F. J.(2003) Sobolev spaces, second edition. Elsevier
Agarwal, G. G. & Studden, J. W.(1980) Asymptotic Integrated Mean Square Error
Using Least Squares and Bias Minimizing Splines. Annals of Statistics 8(6), 1307–1325.
Boente, G., Fraiman,
R. & Meloche, J. (1997) Robust plug-in bandwidth estimators
in nonparametric regression. Journal of Statistical Planning and Inference 57(1), 109–142.
Cantoni, E. & Ronchetti, M. E. (2001) Robust inference for generalized linear models.
Journal of the American Statistical Association 96(455), 1022–1030.
Claeksens, G., Krivobokova, D. & Opsomer, D. J. (2009) Asymptotic properties
of penalised spline estimators. Biometrika 96(3), 529–544.
Cox, D. D.(1983) Asymptotics for M-type smoothing splines. Annals of Statistics 11(2),
530–551.
Cunningham, K. J., Eubank, L.
R. & Hsing, T. (1991) M-type smoothing splines
with auxiliary scale estimation. Computational Statistics & Data Analysis 11(1), 43–51.
De Boor, C.(2001) A Practical Guide to Splines, revised edition. Springer
DeVore, A. R. & Lorentz, G. G.(1993) Constructive approximation. Springer.
Eggermont, P. P. & LaRiccia, N. V.(2009) Maximum Penalized Likelihood Estimation,
Volume II: Regression. Springer.
Eilers, P. H. & Marx, B. D.(1996) Flexible Smoothing with B-splines and Penalties.
Statistical Science 11(2), 89–102.
Eubank, L.
R.(1999) Nonparametric Regression and Spline Smoothing, second edition.
CRC press.
Garland,
T.(1983)
The relation between maximal running speed and body mass in
terrestrial mammals. Journal of Zoology 199, 157–170.
Gasser, T., Sroka, L. & Jennen-Steinmetz, C. (1986) Residual variance and residual
pattern in nonlinear regression. Biometrika 73(3), 625—633.
Green, J.
P. & Silverman, W.
B. (1993) Nonparametric Regression and Generalized
Linear Models: A roughness penalty approach. Chapman & Hall.
Gu, C.(2013) Smoothing spline ANOVA models, second edition. Springer.
Hall, G. P.& Opsomer, D. J.(2005) Theory for penalized spline regression. Biometrika
92(1), 105–118.
24


## Page 25


Hampel, F., Hennig, C. & Ronchetti, E.(2011) A smoothing principle for the Huber
and other location M-estimators. Computational Statistics and Data Analysis 55(1), 324–
337.
Hampel, R.
F., Ronchetti, M. E., Rousseeuw, J. P. & Stahel, A. W.(2011b)
Robust Statistics: The Approach Based on Inﬂuence Functions, second edition. Wiley.
He, X. & Shi, P.(1995) Asymptotics for M-Type Regression Splines with Auxiliary Scale
Estimation. The Indian Journal of Statistics, Series A 57(3), 452–461.
Huber, J.
P.(1964) Robust Estimation of a Location Parameter. Annals of Statistics
35(1), 73–101.
Huber, J. P.(1973) Robust Regression: Asymptotics, Conjectures and Monte Carlo. The
Annals of Statistics 1(5), 799—821.
Huber, J. P.(1979) Robust smoothing. Robustness in statistics, Academic Press, 33–48.
Huber, J.
P. & Ronchetti, M. E.(2009) Robust Statistics, second edition. Wiley.
James,
G., Witten,
D., Hastie,
T. & Tibshirani,
R.(2013) ISLR: Data for an
introduction to statistical learning with applications in R. R package.
Koenker,
R., Portnoy,
S., Ng,
P.T., Zeileis,
A., Grosjean,
P. & Ripley,
B.(2012) Quantile Regression. R package.
Lee, C.M.
T. & Oh, H.S.(2007) Robust penalized regression spline ﬁtting with applica-
tion to additive mixed modeling. Computational Statistics 22(1), 159–171.
Li, Y. & Ruppert, D. (2008) On the asymptotics of penalised splines. Biometrika 95(2),
415–436.
Maronna, A. R., Martin, R. D. & Yohai, J. V.(2006) Robust Statistics: Theory and
Methods. Wiley.
Nocedal, J., & Weight, J. S.(2006) Numerical Optimization, second edition. Springer.
O’Sullivan,
F.(1986) A statistical perspective of ill-posed problems. Statistical Science
1(4), 502–518.
R Development Core Team (2019). R: A Language and Environment for Statistical
Computing. Vienna, Austria: R Foundation for Statistical Computing. ISBN 3-900051-
07-0, http://www.R-project.org.
Ruppert, D., Wand, P.
M. & Carroll, J.
R.
(2003) Semiparametric Regression
Cambridge.
Schumaker, L.(2007) Spline functions: basic theory, third edition. Cambridge.
25


## Page 26


Shen, X., Wolfe, D. A. & Zhou, S.(1998) Local Asymptotics for Regression Splines
and Conﬁdence Regions. Annals of Statistics 26(5), 1760–1782.
Shi, P. & Li, G. (1995) Global convergence rates of B-spline M-estimators in nonparametric
regression. Statistica Sinica 5, 303–318.
Stone, J.
C.(1982) Optimal global rates of convergence for nonparametric regression.
Annals of Statistics 10(4), 1040–1053.
Stone, J.
C.(1985) Additive Regression and Other Nonparametric Models. Annals of
Statistics 13(2), 689–705.
Tharmaratnam, K., Claeskens, G., Croux, C. , & Salibian–Barrera M. (2009)
S-Estimation for Penalized Regression Splines. Journal of Computational and Graphical
Statistics 19(3), 609–625.
Wahba, G.(1990) Spline models for observational data. Siam.
Wegman, J. E. & Wright, W. I.(1983) Splines in Statistics. Journal of the American
Statistical Association 78(382), 351– 365.
Wasserman, L. (2006) All of nonparametric statistics. Springer.
Wood, N. S. (2017) Generalized Additive Models: An Introduction with R, second edition.
CRC press.
Wood, N. S.(2019) Mixed GAM Computation Vehicle with Automatic Smoothness Esti-
mation. CRAN.
Yohai, J. V. & Maronna, A. R.(1979) Asymptotic Behavior of M-Estimators for the
Linear Model. Annals of Statistics 7(2), 258–268.
26

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
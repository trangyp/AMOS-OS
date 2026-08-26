---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.07553v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.07553v1_A_projection_approach_for_multiple_monotone_regression

> Source: 1911.07553v1_A_projection_approach_for_multiple_monotone_regression.pdf

> Pages: 23

---


## Page 1


A PROJECTION APPROACH FOR MULTIPLE MONOTONE REGRESSION
LIZHEN LIN, BRIAN ST. THOMAS, WALTER W. PIEGORSCH, JAMES SCOTT AND CARLOS CARVALHO
Abstract. Shape-constrained inference has wide applicability in bioassay, medicine, economics,
risk assessment, and many other ﬁelds.
Although there has been a large amount of work on
monotone-constrained univariate curve estimation, multivariate shape-constrained problems are
much more challenging, and fewer advances have been made in this direction. With a focus on
monotone regression with multiple predictors, this current work proposes a projection approach to
estimate a multiple monotone regression function. An initial unconstrained estimator – such as a
local polynomial estimator or spline estimator – is ﬁrst obtained, which is then projected onto the
shape-constrained space. A shape-constrained estimate is obtained by sequentially projecting an
(adjusted) initial estimator along each univariate direction. Compared to the initial unconstrained
estimator, the projection estimate results in a reduction of estimation error in terms of both
Lp (p ≥1) distance and supremum distance.
We also derive the asymptotic distribution of
the projection estimate.
Simple computational algorithms are available for implementing the
projection in both the unidimensional and higher dimensional cases. Our work provides a simple
recipe for practitioners to use in real applications, and is illustrated with a joint-action example
from environmental toxicology.
Keywords: Monotone regression with multiple predictors; Drug interaction; Environmental
risk assessment; Projection
1. Introduction
Shape-constrained (e.g. monotone constrained) statistical inference is applied to a variety of data-
analytic problems. In environmental toxicology, for instance, monotone constraints are imposed
based on natural assumptions that the response of subjects exposed to certain chemical pollutants
will not in general decrease with the increasing pollutant dose [29]. Another common application
can be found in disease screening, where the probability of disease is assumed non-decreasing with
increasing measurements of a pertinent biomarker [25, 2]. Or in economics, the demand and supply
curve is in general assumed to be monotone [10]. Motivated by this large variety of applications,
a panoply of statistical approaches has been developed for estimating monotone curves, i.e., one-
dimensional monotone functions.
Frequentist methods in general fall into three categories; the
ﬁrst involves kernel based approaches such as described by [26], [24] and [13]. The second class of
methods models the regression function as a linear span of a spline basis such as in [31] and [21].
1
arXiv:1911.07553v1  [stat.ME]  18 Nov 2019


## Page 2


The third class of methods is based on isotonic regression [32, 3], recent developments of which can
be found in [5, 6, 7, 8] and [23]. In addition, a few Bayesian approaches have been proposed in,
for example, [9], [22], [36] and [37]. Although there is large body of work on estimating monotone
curves, shape-constrained problems with respect to multiple predictors, which are, e.g., important in
drug interaction studies or in risk analyses involving the joint action of multiple pollutants, are more
challenging. This is due to the diﬃculty in incorporating the multivariate shape constraints. Along
these lines, [34] proposes a Bayesian approach for multiple regression using marked point processes,
while [22] combines Gaussian processes with projections for estimating a multivariate monotone
function. In [11], a monotone arrangement procedure [19] is applied to an initial unconstrained
estimator.
Our motivation here is to develop a theoretically appealing, computationally feasible, and convenient-
to-implement approach for estimating monotone constrained functions with multiple predictors. We
propose use of a projection of some initial, unconstrained estimator of the regression function, i.e.,
ﬁnding the monotone function closest to this initial estimator in some distance norm. Such esti-
mates are intuitive, and can result in reduction of the estimation error compared to that of a na¨ıve
initial estimator. Note that a general projection framework for constrained functional parameters,
in particular for constrained functions forming a closed convex cone in a Hilbert space, is proposed
in [17]. Our approach falls into this general framework; however, our projection algorithm makes
use of the fact that the convex cone of a multivariate monotone function is an intersection of a
collection of convex cones of univariate monotone functions. We then derive an expression for the
projection estimate, making use of unidimensional projections. It can be shown that the projection
of an initial estimator onto the space of monotone functions with multiple predictors can be decom-
posed into sequential projections of an adjusted initial estimator along each univariate direction.
This simpliﬁes the operation substantially, and allows us to suggest computational algorithms for
approximating such functions.
In the next section, we study in detail this monotone projection framework and the properties
of our projection estimates. In section 3, we describe a bootstrap methodology for constructing
conﬁdence intervals. In section 4, we carry out a simulation study to explore the methods’ operating
characteristics, and we apply our methods to a two-dose, joint-action data set from environmental
toxicology. Section 5 ends with a short discussion.
2


## Page 3


2. A projection framework for monotone regression with multiple predictors
2.1. Preliminary estimator for the proposed approach. Let x ∈Rp be a p-dimensional
predictor and y be a response variable.
The response variable can be discrete or continuous,
depending on the application of interest.
We deﬁne the regression function F(x) in a general
framework as
F(x) = E(y | x).
(2.1)
For instance, if y is binary, taking values 0 or 1, then take F(x) as the response probability F(x) =
P(y = 1 | x).
Denote the data as (xi, yi), i = 1, . . . , n. Without loss of generality, we assume the predictors
or covariates satisfy xi = (xi1, . . . , xip) ∈[0, 1]p ⊂Rp. The regression function F(x) is assumed
to be monotone with respect to a natural partial ordering on Rp, that is, for x1 = (x11, . . . , x1p),
x2 = (x21, . . . , x2p) and x1j ≤x2j (for j = 1, . . . , p), one has F(x1) ≤F(x2). We are interested in
conducting inference on F(x) under the monotonicity constraint.
Denote M as the space of monotone functions on X = [0, 1]p. It can be seen that M is a closed
convex cone. Our approach relies on projecting an initial estimator of F(x) on to M. For instance,
the initial estimator could be a local polynomial estimator such as the popular kernel estimator or
a local linear estimator. Alternatively, one could employ expansions of spline bases such as a B-
spline basis. In any case, we will show the resulting projection estimates exhibit desirable theoretical
properties as well as good ﬁnite-sample performance. Eﬃcient computational algorithms are also
straightforward to develop for implementing our approach.
To illustrate, we ﬁrst consider a local polynomial regression estimator for a one-dimensional
curve. Let K(x) be a kernel function with
R
K(x)dx = 1,
R
xK(x)dx = 0 and
R
x2K(x)dx < ∞.
Denote Kh(x) = h−1K(x/h). Let γ = (γ0, γ1, . . . , γp) be a (p + 1)-dimensional coeﬃcient vector,
and take
bγ = arg min
γ∈Rp+1
n
X
i=1
Kh(x −xi)


yi −
p
X
j=0
γj(x −xi)j



2
.
An initial local polynomial estimator of F(x) can be simply
bF(x) = bγ0,
which can be ﬁtted easily via weighted least squares.
3


## Page 4


Another popular class of methods for nonparametric regression involves spline models [39]. More
precisely, one can construct a class of initial estimators by modeling the regression function as a
linear span of a spline basis, the most of popular of which is the B-spline basis [16]. Given the knot
sequence τ1, τ2, · · · , τN, the cubic B-spline basis {Bj,4}4
j=1 is deﬁned recursively as follows:
Bj,1(x) =







1
τj ≤x ≤τj+1
0
otherwise,
Bj,l(x) =
x −τj
τj+l−1 −τj
Bj,l−1(x) +
τj+l −x
τj+l −τj+1
Bj+1,l−1(x) (l = 2, 3, 4).
With this, one obtains an initial estimator of F(x) as a linear combination of the spline basis
functions. Using the B-spline basis above, this sets
F(x) =
N
X
j=1
βjBj,4(x),
(2.2)
where (β1, . . . , βN) is the vector of coeﬃcients. The estimate is bF(x) = PN
i=1 bβiBi(x) with
(bβ1, . . . , bβN) = arg min
β∈Rm
"
λ
n
X
i=1
{yi −F(xi)}2 + (1 −λ)
Z
{F ′′(x)}2dx
#
.
Here λ is a smoothing parameter that controls the tradeoﬀbetween tighter ﬁt to the data and
smoothness of the estimates. We refer to [38] for a general reference on smoothing splines.
For the multivariate case, one can easily obtain a kernel based initial estimator by employing a
multivariate kernel K. Or one can obtain an initial estimator using tensor product B-splines [16].
For example, take p = 2 with the two-dimensional function F(x1, x2). Let {Bi1(x1)}, i = 1, . . . , N1,
be a B-spline basis along the x1 direction, and {Bj2(x2)}, j = 1, . . . , N2, be a spline basis along the
x2 direction. A tensor product spline basis is given by {Bi1Bj2}, i = 1, . . . , N1, j = 1, . . . , N2. The
multivariate function is modeled as a linear span of the tensor product B-spline basis. An initial
estimator bF(x1, x2) can be obtained by minimizing the objective function
λ
n
X
i=1
{yi −F(xi1, xi2)}2 + (1 −λ)
Z Z (∂2F
∂x2
1
2
+ 2
 ∂2F
∂x1x2
2
+
∂2F
∂x2
2
2)
dx1dx2.
With any initial estimator bF(x1, x2), one then projects bF(x1, x2) onto the monotone space M,
which produces our ultimate estimator of F(x1, x2). We now proceed to give a rigorous deﬁnition
of this projection and characterize its properties in the next subsection.
4


## Page 5


2.2. A projection framework for shape constrained estimators. Let w be a function on
X = [0, 1]p. We deﬁne the projection of w onto the constrained space M as
Pw = argmin
G∈M
Z
X
{w(t) −G(t)}2dt.
(2.3)
That is, the projection estimate is deﬁned to be the element in M that is closest to the initial
(pre-projected function) estimator in L2 distance.
Recall M = M[0, 1]p, which is the space of monotone functions on [0, 1]p. Focusing initially on
the p = 1 case, (2.3) has the following closed form solution (see [22] and [1])
Pw(x) = inf
v≥x sup
u≤x
1
v −u
Z v
u
w(t)dt,
x ∈[0, 1].
(2.4)
The existence and uniqueness of the projection follow from Theorem 1 in [33].
Letting h be any function on [0,1], the greatest convex minorant of h is deﬁned by
T(h) = arg max{z : z ≤h, z convex}
(2.5)
The solution (2.4) is the slope of the greatest convex minorant of w(t) =
R t
0 w(s)ds.
Remark 2.1. The projection in (2.4) can be well approximated using the pooled adjacent violators
algorithm [3].
One can easily generalize the above one-dimensional projection algorithm to multiple dimensions
(p > 1).
Take p = 2; for which the following algorithm [22] converges to the two-dimensional
projection
Pw = argmin
G∈M
Z 1
0
Z 1
0
{w(s, t) −G(s, t)}2dsdt.
Algorithm 1. For any ﬁxed t, w(s, t) is a function of s and we use the projection (2.4) to obtain
a monotone function in s. We perform this projection for all values of t, and denote the resulting
surface by bw(1)(s, t). Letting S(1) = bw(1) −w, for any ﬁxed s, project w + S(1) as a function of
t onto M[0, 1] using (2.4). Perform this projection for all values of s and denote the surface by
ew(1)(s, t). Set T (1) = ew(1) −(w + S(1)). Letting i = 2, . . . , k, in the ith step we obtain bw(i) by
projecting w + T (i−1) along the s direction for every ﬁxed t value in [0,1] and ew(i) as the projection
of w + S(i) along the t direction for every ﬁxed s value in [0,1]. The algorithm terminates when
bw(i) or ew(i) is monotone with respect to both s and t for some step i.
Via an induction argument, one can show that projecting a p-dimensional function onto M[0, 1]p
with p > 2 can be characterized similarly to Algorithm 1, above, by introducing p residual sequences.
5


## Page 6


Given an initial estimate bF(x), we denote the projection estimate of F(x) under the shape
constraints as eF(x) with
eF(x) = P b
F (x)(x).
(2.6)
eF(x) is the ultimate estimate used for inference.
Now, let
∥eF(x) −F(x)∥2 =
"Z
[0,1]p{ eF(x) −F(x)}2dx
#1/2
=
Z 1
0
· · ·
Z 1
0
{ eF(x) −F(x)}2dx1 · · · dxp
1/2
,
which is the L2 norm for a p-dimensional function F(x).
The following propositions show that eF(x) is ‘closer’ to the true regression monotone function
F(x), compared to the initial estimator bF(x). As a consequence, bF(x) produces smaller error in
the L2 norm compared to that of the initial estimator bF(x).
Proposition 2.1. Let x ∈Rp (p ≥1). Let bF(x) be an initial estimator of F(x) and eF(x) = P b
F (x).
Then the following holds:
∥eF(x) −F(x)∥2 ≤∥bF(x) −F(x)∥2
(2.7)
For a proof, see the Appendix.
Corollary 2.2 follows immediately from Proposition 2.1.
Corollary 2.2.
∥bF(x) −F(x)∥2 = O(λn).
where λn →0 as n →∞. Then
∥eF(x) −F(x)∥2 = O(λn).
In the one-dimensional case, we can derive more general results on the reduction in estimation
error for the projection estimator.
Theorem 2.3. Assume x ∈R. Let Φ be any convex function and eF(x) be an initial estimator of
F(x), such as a kernel estimator or a spline estimator. Let eF(x) = P b
F (x)(x). One has
Z 1
0
Φ
n
eF(x) −F(x)
o
dx ≤
Z 1
0
Φ
n
bF(x) −F(x)
o
dx.
(2.8)
6


## Page 7


For a proof, see the Appendix.
Corollary 2.4. Assume x ∈R. Let eF(x) be an initial estimator of F(x) such as a kernel estimator
or a spline estimator. Let eF(x) = P b
F (x)(x). One has
sup
x | eF(x) −F(x)| ≤sup
x | bF(x) −F(x)|,
(2.9)
and
Z 1
0
| eF(x) −F(x)|qdx ≤
Z 1
0
| bF(x) −F(x)|qdx,
(2.10)
where q ∈[1, ∞).
Proof. Taking Φ = ∥x∥q in Theorem 2.3, (2.10) follows. As q →∞, (2.9) holds. Note that a
diﬀerent proof for (2.9) is given in [22].
□
The following proposition concerns the asymptotic distribution of the projection, which follows
from the general results of Theorem 3.4 in [17].
Proposition 2.5. Let the tangent cone of M be TM(F), which is the closure of {λ(G −F), G ∈
M, λ > 0}. If
bF(x) −F(x)
tn
L
−→U(x)
for some tn →0 as n →∞, then
eF(x) −F(x)
tn
L
−→ePU(x),
(2.11)
where ePU(x) is the projection of U(x) onto the tangent cone TM(F) and
L
−→indicates convergence
in distribution.
Remark 2.2. Let M1, . . . , Mp be p convex cones of functions such that Mk is the convex cone
of functions which are monotone with respect to the kth direction of x. That is, for any F ∈Mk,
F(x1, . . . , xp) is monotone with respect to xk at any ﬁxed value of the other coordinates. It is not
diﬃcult to see that M is the intersection of the p convex cones M1, . . . , Mp, i.e., M = ∩p
k=1Mk.
The projection algorithm (Algorithm 1) can be viewed as a sequential projection of a p-variate
function onto each convex cone Mk, while at each step the projected function is adjusted by
adding residual sequences from the previous step.
Note that similar algorithms consisting of a
projection step and an adjustment step hold for any space that can be written as the intersection
of a collection of convex cones (see [4]).
7


## Page 8


3. Bootstrap confidence intervals
In this section we appeal to the bootstrap [12] for constructing conﬁdence intervals from our
estimators. Consider the following procedure for generating a nonparametric estimate, along with
conﬁdence intervals, for a monotone function F(x). The data are (xi, yi) pairs, i = 1, . . . , n.
(1) Fit the curve to obtain an initial estimator bF which need not satisfy the monotonicity
constraint(s).
(2) Project the estimate onto M, the space of monotone functions. Call this projected estimate
eF, and let ei = yi −eF(xi) be the residual of the ith point from the monotone estimate.
(3) Repeat the following procedure B = 2000 times.
(a) Resample the residuals with replacement, yielding e⋆
1, . . . , e⋆
n.
(b) Set y⋆
i = eF(xi) + e⋆
i .
(c) Apply steps 1 and 2 to the bootstrapped points (xi, y⋆
i ) to yield eF ⋆.
(4) Collect the B diﬀerent bootstrapped estimates eF ⋆. We adopt percentile-based methods for
constructing point-wise conﬁdence intervals [15]. For example, the lower and upper 95%
conﬁdence bounds of F(x) are given by the 2.5 percentile and 97.5 percentile of the ranked
bootstrapped estimates, respectively.
In the next section, both a simulation study and a real data example are presented to illustrate
use of the bootstrap procedure for constructing 95% pointwise conﬁdence intervals on the monotone
regression function in Section 4.
4. Simulation studies and data analysis
In this section we report the results of a series of short Monte Carlo simulations used to gauge
selected operating characteristics of the projection estimator. We also illustrate the methodology
using a contemporary data set from environmental toxicology.
4.1. Root mean squared errors. To study the various features of our projection estimators,
we simulated data from a variety of one-, two-, and three-predictor monotone regression models
under a normal parent distribution.
For example, with one predictor, x1, we generated yi ∼
N

F(xi1), σ2	
, i = 1, . . . , n with n set to 100, where the covariates were taken to be equidistant on
their domain, and the mean function F(x1) was chosen from a class of monotone curves originally
proposed by [20] and [27]:
(a) ﬂat function, F11(x1) = 3, x1 ∈(0, 10];
(b) sinusoidal function, F12(x1) = 0.32{x1 + sin(x1)}, x1 ∈(0, 10];
8


## Page 9


(c) step function, F13(x1) = 3 if x1 ∈(0, 8] and F3(x1) = 6 if x1 ∈(8, 10];
(d) linear function, F14(x1) = 0.3x1, x1 ∈(0, 10];
(e) exponential function, F15(x1) = 0.15 exp{0.6x1 −3}, x1 ∈(0, 10];
(f) logistic function, F16(x1) = 3/ (1 + exp{−2x1 + 10}), x1 ∈(0, 10].
(g) half-normal function, F17(x1) = 3 exp

−1
2(0.02)2(0.1x1 −1)2	
, x1 ∈(0, 10].
(h) mixture function, F18(x1) = 6F(0.1x1), where F(·) is the c.d.f. from the equal mixture of
N(0.25, 0.0042) and N(0.75, 0.042).
The standard deviation parameter σ was varied over a range of σ = 0 (i.e., a purely deterministic
response), 0.1, 0.2, . . . , 1.2, 1.3. These same models were also employed at n = 100 and σ = 1 in a
comparative study by [36].
Each simulation was replicated 50 times for every value of σ, and the square root of the empirical
root mean squared error (RMSE) for the projection estimator was recorded using either a kernel
estimator or a cubic spline estimator for the initial bF(x). More precisely, the RMSE is deﬁned as
RMSE( bF(x)) =
v
u
u
t 1
n
n
X
i=1
{ bF(x) −F(x)}2.
These resultant RMSEs using either initial estimator were then averaged over the 50 replicate
simulation trials for each model.
The results are summarized in Figure 1 for the initial kernel
estimator (top) and the initial spline estimator (bottom). One sees that the average RMSE rises
gradually but consistently with increasing σ, and that these errors are substantially higher with
both the step function, F13(x), and the mixture function, F18(x), models. By contrast, the ﬂat
function, F11(x), and half-normal function, F17(x), models separate out with lower average RMSEs
as σ rises. Also, for many values of σ, the average spline-based RMSE exceeds the average kernel-
based RMSE. Table 4.1 gives further detail on the one-predictor RMSE simulations, by reporting
the average RMSEs and the standard error of the RMSES at σ = 1
2 and σ = 1 across all models.
Note that the standard errors of the 50 RMSE values are quite small, indicating that there is small
variability for the average RMSE.
For the two-predictor setting with x1 and x2, we again generated yi ∼N

F(xi1, xi2), σ2	
, i =
1, . . . , 100, with σ ranging over σ = 0, 0.1, . . . , 1.3.
Now, (x1, x2) ∈[0, 1] × [0, 1] and the two-
dimensional mean functions were taken from a study considered in [34]:
(a) F21(x1, x2) = √x1;
(b) F22(x1, x2) = 0.5x1 + 0.5x2;
(c) F23(x1, x2) = min(x1, x2);
9


## Page 10


Figure 1. Average root mean squared error (RMSE) for one-dimensional projec-
tion estimates based on initial kernel estimator (top) and initial spline estimator
(bottom) for eF(x). Digits correspond to model numbers (second digits) in Sec. 4.1.
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0.0
0.1
0.2
0.3
0.4
RMSE results, Kernel
σ
Average RMSE
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
6
6
6
6
6
7
7
7
7
7
7
7
7
7
7
7
7
7
7
8
8
8
8
8
8
8
8
8
8
8
8
8
8
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0.0
0.1
0.2
0.3
0.4
RMSE results, Spline
σ
Average RMSE
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
6
6
6
6
6
7
7
7
7
7
7
7
7
7
7
7
7
7
7
8
8
8
8
8
8
8
8
8
8
8
8
8
8
(d) F24(x1, x2) = 0.25x1 + 0.25x2 + 0.5 × 1{x1+x2>1};
(e) F25(x1, x2) = 0.25x1 + 0.25x2 + 0.5 × 1{min(x1,x2)>0.5};
(f) F26(x1, x2) = 1{(x1−1)2+(x2−1)2<1} ×
p
1 −(x1 −1)2 −(x2 −1)2.
The consequent average RMSEs are plotted in Figure 2, separated by initial kernel estimator (top)
and initial spline estimator (bottom). The broad patterns appear similar to those seen with one
predictor, although there is less separation/distinguishablity in the RMSEs across models. Also,
the spline-based RMSEs are often much closer to their kernel-based cousins, although for large σ
the former generally still exceed the latter. Table 2 reports the average RMSE values at σ = 1
2 and
σ = 1.
Lastly, we simulated n = 100 data points from models whose true regression functions involve
three predictors, x1, x2, x3, where each xj ∈[0, 10], and again using a Normal model with constant
10


## Page 11


Table 1. The mean and standard error of one-predictor root mean square errors
(RMSEs) for simulated data at n = 100, averaged across 50 simulation replicates,
listed by underlying mean function F(x1) from Sec. 4.1 and standard deviation
parameter σ.
Mean function, F(x1)
Initial estimator
σ = 1
2
σ = 1
2
σ = 1
σ = 1
Average
SE
Average
SE
ﬂat, F11(x1)
Kernel
0.0485
0.0048
0.0858
0.0101
Spline
0.0573
0.0053
0.1102
0.0150
sinusoidal, F12(x1)
Kernel
0.1228
0.0049
0.2217
0.0080
Spline
0.1255
0.0063
0.2307
0.0099
step, F13(x1)
Kernel
0.3144
0.0072
0.3875
0.0113
Spline
0.3209
0.0043
0.4048
0.0114
linear, F14(x1)
Kernel
0.1129
0.0053
0.2009
0.0106
Spline
0.0813
0.0074
0.1631
0.0159
exponential, F15(x1)
Kernel
0.1155
0.0047
0.1895
0.0110
Spline
0.1060
0.0053
0.2179
0.0159
logistic, F16(x1)
Kernel
0.1475
0.0051
0.2438
0.0103
Spline
0.1369
0.0055
0.2430
0.0111
half-normal, F17(x1)
Kernel
0.0470
0.0048
0.0950
0.0087
Spline
0.0570
0.0060
0.1166
0.0144
mixture, F18(x1)
Kernel
0.3045
0.0040
0.3893
0.0086
Spline
0.3180
0.0042
0.4092
0.0086
standard deviation σ ranging over σ = 0, 0.1, . . . , 1.3. For the underlying mean monotone functions
we employed the following collection:
(a) F31(x1, x2, x3) = 0.15(x1 + x2 + x3);
(b) F32(x1, x2, x3) = 0.5x1x2x3;
(c) F33(x1, x2, x3) = min(x1, x2, x3);
(d) F34(x1, x2, x3) = 1/ [1 + exp{−(x1 + x2 + x3)}];
(e) F35(x1, x2, x3) = exp{0.01x1 + 0.1√x2} + sin(x3/5);
Fifty replicate trials were generated under each model conﬁguration, and from these the average
RMSEs were calculated.
These are plotted as a function of σ in Figure 3, again separated by
initial kernel estimator (top) and initial spline estimator (bottom). The broad patterns appear
more similar to those seen in the one-predictor setting. Table 3 reports the average RMSE values
at σ = 1
2 and σ = 1.
11


## Page 12


Figure 2. Average root mean squared error (RMSE) for two-dimensional projec-
tion estimates based on initial kernel estimator (top) and initial spline estimator
(bottom) for eF(x). Digits correspond to model numbers (second digits) in Sec. 4.1.
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0.00
0.10
0.20
0.30
RMSE results, Kernel
σ
Average RMSE
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
6
6
6
6
6
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0.0
0.1
0.2
0.3
RMSE results, Spline
σ
Average RMSE
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
6
6
6
6
6
4.2. Bootstrap interval coverage. We also used our simulation approach to explore the pointwise
coverage characteristics of the bootstrap conﬁdence intervals from Section 3. Following the same
procedures described in Section 4.1, we generated pseudo-random data yi ∼N

F(xi1), σ2	
, i =
1, . . . , 100, where the one-predictor mean function F(x1) was chosen as either the sinusoidal (F12) or
logistic (F16) form listed above. The standard deviation parameter was set to σ = 1. The predictor
variable was again taken over x1 ∈[0, 10). We also generated pseudo-random two-predictor data:
yi ∼N

F(xi1, xi2), σ2	
, i = 1, . . . , 100, where the two-predictor mean function F(xi1, xi2) was
chosen as either function F21 or F26 from above. As there, the predictor variables were taken over
the unit square. For both the one-predictor and two-predictor settings, 2000 samples were generated
at each parameter conﬁguration.
12


## Page 13


Table 2. The mean and standard error of two-predictor root mean square errors
(RMSEs) for simulated data at n = 100, averaged across 50 simulation replicates,
listed by underlying mean function F(x1, x2) from Sec. 4.1 and standard deviation
parameter σ.
Mean function, F(x1, x2)
Initial estimator
σ = 1
2
σ = 1
2
σ = 1
σ = 1
Average
SE
Average
SE
F21(x1, x2)
Kernel
0.1125
0.0074
0.1923
0.0158
Spline
0.1153
0.0075
0.2383
0.0138
F22(x1, x2)
Kernel
0.1274
0.0054
0.1874
0.0137
Spline
0.1439
0.0054
0.2484
0.0117
F23(x1, x2)
Kernel
0.1356
0.0065
0.2175
0.0111
Spline
0.1360
0.0058
0.2514
0.0220
F24(x1, x2)
Kernel
0.1783
0.0071
0.2551
0.0130
Spline
0.1929
0.0055
0.3036
0.0010
F25(x1, x2)
Kernel
0.1530
0.0056
0.2601
0.0137
Spline
0.1768
0.0051
0.2861
0.0149
F26(x1, x2)
Kernel
0.1687
0.0062
0.2491
0.0116
Spline
0.1715
0.0055
0.2849
0.0116
Table 3. The mean and standard error of three-predictor root mean square errors
(RMSEs) for simulated data at n = 100, averaged across 50 simulation replicates,
listed by underlying mean function F(x1, x2, x3) in Sec. 4.1 and standard deviation
parameter σ.
Mean function, F(x1, x2, x3)
Initial estimator
σ = 1
2
σ = 1
2
σ = 1
σ = 1
Average
SE
Average
SE
F31(x1, x2, x3)
Kernel
0.0841
0.0085
0.1846
0.0147
Spline
0.2078
0.0133
0.3449
0.0262
F32(x1, x2, x3)
Kernel
0.1677
0.0052
0.2586
0.0110
Spline
0.2216
0.0130
0.4232
0.0216
F33(x1, x2, x3)
Kernel
0.1616
0.0376
0.2714
0.0464
Spline
0.2138
0.0136
0.4108
0.0158
F34(x1, x2, x3)
Kernel
0.1590
0.0053
0.2511
0.0144
Spline
0.2600
0.0113
0.5119
0.0175
F35(x1, x2, x3)
Kernel
0.2249
0.0065
0.3687
0.0117
Spline
0.2857
0.0088
0.5454
0.0281
To study pointwise coverage in the one-predictor case, we evaluated how often out of the 2000
replicate simulations the bootstrap intervals contained the true mean response at a series of values
for x1 over the range 0.5, 1.5, 2.5, 3.5, 5.5, . . . , 9.5. We set the nominal pointwise conﬁdence level
to 95%. The empirical coverage rates appear in Table 4, where we see the bootstrap procedure
13


## Page 14


Figure 3. Average root mean squared error (RMSE) for three-dimensional pro-
jection estimates based on initial kernel estimator (top) and initial spline estimator
(bottom) for eF(x). Digits correspond to model numbers (second digits) in Sec. 4.1.
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0.0
0.1
0.2
0.3
0.4
RMSE results, Kernel
σ
Average RMSE
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0.0
0.1
0.2
0.3
0.4
0.5
0.6
RMSE results, Spline
σ
Average RMSE
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
generally contains the true mean function at or near the pointwise nominal level. The few cases
where rates drop substantively below nominal occur when the mean function turns sharply (i.e.,
x = 7.5 or x = 8.5 for the sinusoidal function F12 and x = 3.5 or x = 5.5 for the logistic function
F16). In all the studies, an initial kernel estimate is used.
Table 4. One-predictor empirical coverage rates (×100) based on 2000 simulation
replicates, each at sample size of n = 100. Rates are stratiﬁed by underlying mean
function F(x1), and are pointwise at each of the listed values of the predictor
variable. Nominal conﬁdence level is 95%.
x1
Mean function, F(x1)
0.5
1.5
2.5
3.5
5.5
6.5
7.5
8.5
9.5
sinusoidal, F12(x1)
82.4
97.0
97.6
95.0
98.1
94.2
85.2
78.3
96.2
logistic, F16(x1)
98.1
98.5
90.6
79.8
75.4
84.7
86.8
98.1
99.7
14


## Page 15


In similar fashion, we calculated pointwise empirical coverage with the two-predictor models
over a series of (x1, x2) pairs in the unit square.
Table 5 displays the predictor pairs and the
consequent coverage rates. We ﬁnd that the bootstrap procedure again generally contains the true
mean function pointwise values at or near the nominal level. Some degradation in coverage is seen
at the origin (0, 0), and for F21(x1, x2) also at the corner points (0, 1) and (1, 0).
Table 5. Two-predictor empirical coverage rates (×100) based on 2000 simulation
replicates, each at sample size of n = 100. Rates are stratiﬁed by underlying mean
function F(x1), and are pointwise at each of the listed pairings of the predictor
variables. Nominal conﬁdence level is 95%.
x1
x2
0.00
0.25
0.50
0.75
1.00
Mean function: F21
0.00
88.5
96.5
94.1
92.4
71.1
0.25
96.6
98.9
97.5
88.2
94.0
0.50
94.2
97.2
92.4
95.5
98.9
0.75
92.4
88.7
95.3
94.9
97.3
1.00
68.9
93.2
98.2
96.5
96.8
Mean function: F26
0.00
86.8
88.2
90.6
92.0
98.7
0.25
88.7
82.9
84.0
90.2
95.1
0.50
91.0
84.2
88.2
94.3
97.4
0.75
91.8
90.0
95.0
97.9
97.9
1.00
98.1
97.7
98.0
97.7
98.8
4.3. Application: environmental toxicology data. To illustrate use of our projection method
in practice, we consider two-predictor data from an environmental toxicology experiment described
in [14]. Two potentially hazardous agents, dichlorodiphenyltrichloroethane (DDT) and titanium
dioxide nanoparticles (nano-TiO2), were studied for their ability to induce cellular damage (as
micronucleus formation) in human hepatic cells. The two predictor variables here are taken as
log-transformed concentrations of the toxins: x1 = log10(DDT) + 4 and x2 = log10(TiO2) + 3.
(Control doses at zero concentrations were adjusted using consecutive-dose average spacing, from
[28].) The data in Table 4.3 show proportions of cells exhibiting damage after exposure to various
combinations of x1 and x2.
We applied our monotonic projection method to these data in which an initial kernel estimator
is used, in order to estimate the probability of response over the range of log-transformed doses.
From this, pointwise 95% bootstrap conﬁdence bounds were also calculated, based on 2000 bootstrap
samples. The bootstrap bounds and function estimate are plotted in Figure 4. The display shows
that the eﬀect of TiO2 is slight, but the eﬀect of DDT is marked. The probability of cellular damage
15


## Page 16


Table 6. Proportions of human hepatic cells exhibiting micronuclei after exposure
to DDT (as predictor variable x1; see text) and nano-TiO2 (as predictor variable
x2; see text); adapted from [35].
x2: nano-TiO2
0
1
2
3
0
59/3000
65/3000
70/3000
67/3000
1
67/3000
75/3000
83/3000
84/3000
x1: DDT
2
76/3000
87/3000
96/3000
83/3000
3
94/3000
107/3000
110/3000
117/3000
rises quickly with exposure, then levels. It then jumps up further after a concentration of about
0.05 µmol/L, such that the response appears to be essentially a step function.
Figure 4. Projection estimate and pointwise 95% bootstrap conﬁdence bounds
for data in Table 4.3 on proportions of human hepatic cells exhibiting micronuclei
(per 3,000). The function estimate and observed data are in black, and bounds are
in gray. The concentrations are given in their log10 scale
5. Discussion
We propose a general projection framework for estimating multiple monotone regression func-
tions. An initial naive estimator such as the kernel or spline estimator is ﬁrst obtained, which is
projected onto the monotone space serving as the ultimate estimate of the true monotone regression
regression. The projection estimate is shown to reduce estimation error, compared to that of an
initial estimator. Eﬃcient computational algorithms are available for approximating the estimates.
16


## Page 17


A simulation study and a data example show that the estimates possess practical ﬁnite-sample
performance.
The methods exhibit good performance, although future work can expand their practicality. For
example, it is of both theoretical and practical interest to extend the pointwise conﬁdence bounds
on the estimated surface into simultaneous conﬁdence bands. Constructing conﬁdence bands for
nonparametric regression functions is overall a very challenging problem (see. e.g., [30]) and we
hope to report results on this under our shape constraint framework in a future work.
Appendix
Proof of Proposition 2.1. Our proposition falls as a special case of Lemma 2.3 of [17], we give
another proof here which gives more insights onto the projection algorithm.
By Algorithm 1, the multivariate projection is obtained by a collection of sequential one-dimensional
projections. Let w = bF(x) be the pre-projected estimate and Pw = eF(x) be the projection of w.
We ﬁrst prove that Proposition 2.1 holds for p = 2, the two-dimensional projection. Therefore,
Pw = argmin
G∈M
Z 1
0
Z 1
0
{w(s, t) −G(s, t)}2dsdt.
(A.1)
Note that Pw is the limit of bw(k) and ew(k), where bw(k) is the one-dimensional projection of w+T (k−1)
along the s direction for any t, and ew(k) is the one-dimensional projection of w + S(k) along the t
direction for any s.
Deﬁne the norm of any two-dimensional function f(s, t) as ||f|| = ⟨f, f⟩1/2 =
R 
f 2(s, t)
	
dsdt
1/2
with ⟨·, ·⟩denoting the inner product. Then by the property of projection, one has
⟨w −Pw, Pw⟩= 0,
(A.2)
and
⟨w −Pw, h⟩≤0 for any h ∈M.
(A.3)
In the following, we proceed to show that for any k,
|| bw(k)|| ≥|| ew(k)|| ≥|| bw(k+1)||,
(A.4)
i.e., that the norm of the sequence bw(k) and ew(k) is not increasing. In order to do so, we ﬁrst
introduce the notion of cones and dual cones of functions. Let Cs be the cone of the continuous
17


## Page 18


functions f(s, t) which are monotone with respect to s for any t, and Ct be the cone of continuous
functions which are monotone with respect to t for any s. Deﬁne their dual cones C∗
s and C∗
t as
C∗
s =

g(s, t) ∈C[0, 1]2 :
Z
f(s, t)g(s, t)ds ≤0, for all t and f ∈Cs

,
and
C∗
t =

g(s, t) ∈C[0, 1]2 :
Z
f(s, t)g(s, t)dt ≤0, for all s and f ∈Ct

.
Denote P(w | Cs) as the projection of w over Cs found by minimizing
R
(w −f)2ds for all f ∈Cs
and any ﬁxed t. Denote P(w | Ct) as the projection of w over Ct found by minimizing
R
(w −f)2dt
for all f ∈Ct and any ﬁxed s. By Lemma A1 of [22], the following holds:
P(w | C∗
s ) = w −P(w | Cs) and P(w | C∗
t ) = w −P(w | Ct).
(A.5)
Note that −S(k+1) = (w + T (k)) −bw(k) = (w + T (k)) −P(w + T (k)|Cs) = P(w + T (k)|C∗
s ) where
the last equality follows from (A.5). Here P(w + T (k)|Cs) denotes the projection of w + T (k) onto
Cs and P(w + T (k)|C∗
s ) is the projection onto C∗
s . Therefore −S(k+1) minimizes ||(w + T (k)) −f||
for all f ∈C∗
s and −T (k) minimizes ||(w + S(k)) −f|| for all f ∈C∗
t . Then, one concludes that
|| bw(k)|| = ||w + S(k) −(−T (k−1))|| ≥||w + S(k) −(−T (k))|| ≥||w + T (k) −(−S(k+1))||
for all k. Therefore, one has || bw(k)|| ≥|| ew(k)|| ≥|| bw(k+1)||.
Now, for suﬃciently large k, one has
∥Pw∥≤∥bw(k+1)∥≤∥ew(k)∥≤∥bw(k)∥≤· · · ≤∥w∥.
(A.6)
By the above equation and (A.3),
∥Pw −F∥2 = ∥Pw∥2 + ∥F∥2 −2⟨F, Pw⟩
≤∥w∥2 + ∥F∥2 −2⟨F, w⟩
= ∥w −F∥2,
proving our contention.
□
Lemma A.1. Denote C as the convex cone of a function on some domain set X = [0, 1]p, which
includes M, the convex cone of monotone functions on X. Let g be any function on X and g∗∈C
18


## Page 19


such that
g∗= arg min
f∈C
Z
X

g(x) −f(x)
	2dx.
(A.7)
Then, one has for every f ∈C,
Z
x∈X

g(x) −g∗(x)
	
g∗(x) −f(x)
	
dx ≥0,
(A.8)
so that
Z
x∈X

g(x) −g∗(x)
	
g∗(x)dx = 0,
(A.9)
and
Z
x∈X

g(x) −g∗(x)
	
f(x)dx ≤0.
(A.10)
Proof. By the deﬁnition of a convex cone, for any α ∈[0, 1] and any f ∈C, (1 −α)g∗+ αf ∈C.
Then
Z
X

g(x) −{(1 −α)g∗+ αf}
2dx
achieves its minimum at α = 0. Now, take the derivative of the above objective function to ﬁnd
2
Z
X

g(x) −{(1 −α)g∗+ αf}

g∗(x) −f(x)
	
dx,
which is non-negative at α = 0. Therefore,
Z
x∈X

g(x) −g∗(x)
	
g∗(x) −f(x)
	
dx ≥0.
Now let f(x) = cg∗(x), so that
Z
x∈X

g(x) −g∗(x)
	
(1 −c)g∗(x)dx ≥0.
By letting 0 < c ≤1, for example, letting c = 1/2, one has
1
2
Z
x∈X

g(x) −g∗(x)
	
g∗(x)dx ≥0.
Now let c ≥1, e.g, c = 2 then
Z
x∈X

g(x) −g∗(x)
	
g∗(x)dx ≤0.
19


## Page 20


This implies that
Z
x∈X

g(x) −g∗(x)
	
g∗(x)dx = 0,
which further implies
Z
x∈X

g(x) −g∗(x)
	
f(x)dx ≤0.
□
Proof of Theorem 2.3. Let φ(u) be the derivative of the convex function Φ(u). By the property of
convex functions, one has
Φ(v) −Φ(u) ≥(v −u)φ(u).
Let u = eF(x) −F(x) and v = bF(x) −F(x). Then
Φ
n
bF(x) −F(x)
o
≥Φ
n
eF(x) −F(x)
o
+
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
.
Thus,
Z 1
0
Φ
n
bF(x) −F(x)
o
dx ≥
Z 1
0
Φ
n
eF(x) −F(x)
o
dx +
Z 1
0
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
dx.
It suﬃces to show that
Z 1
0
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
dx ≥0.
Note that eF(x) is the slope of T(¯bF(x)), the greatest convex minorant of ¯bF(x) =
R x
0 bF(s)ds. One
can write the unit interval [0,1] as the union of the sets {x : T(¯bF(x)) = ¯bF(x)}, over which the
function bF(x) is monotone, and the disjoint open sets {x : T(¯bF(x)) < ¯bF(x)}. One can see that over
each of the disjoint sets {x : T(¯bF(x)) < ¯bF(x)}, T(¯bF(x)) is a linear function. (Otherwise, one can
always construct a convex function above it, leading to a contradiction.) Therefore, eF(x), which
is the derivative of T(¯bF(x)), is a constant function over each of these sets. Let {x : T(¯bF(x)) <
¯bF(x)} = ∪Ui where Ui and Uj are disjoint intervals for i ̸= j. Let eF(x) = ci over the set Ui. One
has ci =
R
Ui bF(x)dx
|Ui|
(see Lemma 2 of [18]), where |Ui| denotes the length of the intervals, which
can be viewed as the projection of bF(x) restricted to the set Ui. Then
Z 1
0
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
dx =
X
i
Z
Ui
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
dx.
20


## Page 21


Since F(x) is a monotone increasing function, −F is decreasing, thus φ
n
eF(x) −F(x)
o
is decreas-
ing over Ui. Then by equation (A.10) of Lemma A.1, one has
R
Ui
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
dx ≥
0. Then
Z 1
0
n
bF(x) −eF(x)
o
φ
n
eF(x) −F(x)
o
dx ≥0,
which implies that
Z 1
0
Φ
n
eF(x) −F(x)
o
dx ≤
Z 1
0
Φ
n
bF(x) −F(x)
o
dx.
□
References
[1] D. Anevski and P. Soulier. Monotone spectral density estimation. Ann. Statist., 39(1):418–438, 02 2011.
[2] S. G. Baker. Identifying combinations of cancer markers for further study as triggers of early intervention.
Biometrics, 56(4):1082–1087, 2000.
[3] R. Barlow, D. J. Bartholomew, J. M. Bremner, and H. D. Brunk. Statistical Inference Under Order Restrictions:
The Theory and Application of Isotonic Regression. Out-of-print Books on demand. John Wiley & Sons, New
York, 1972.
[4] H. Bauschke and J. Borwein. Dykstra’s alternating projection algorithm for two sets. Journal of Approximation
Theory, 79(3):418 – 443, 1994.
[5] R. Bhattacharya and M. Kong. Consistency and asymptotic normality of the estimated eﬀective doses in bioassay.
Journal of Statistical Planning and Inference, 137(3):643 – 658, 2007. Special Issue on Nonparametric Statistics
and Related Topics: In honor of M.L. Puri.
[6] R. Bhattacharya and L. Lin. An adaptive nonparametric method in benchmark analysis for bioassay and envi-
ronmental studies. Statistics & Probability Letters, 80:1947 – 1953, 2010.
[7] R. Bhattacharya and L. Lin. Nonparametric benchmark analysis in risk assessment: a comparative study by
simulation and data analysis. Sankhya B, 73(1):144–163, 2011.
[8] R. Bhattacharya and L. Lin. Recent progress in the nonparametric estimation of monotone curves—with appli-
cations to bioassay and environmental risk assessment. Computational Statistics & Data Analysis, 63:63 – 80,
2013.
[9] B. Bornkamp and K. Ickstadt. Bayesian nonparametric estimation of continuous monotone functions with ap-
plications to dose–response analysis. Biometrics, 65(1):198–205, 2009.
[10] N. Chehrazi and T. A. Weber. Monotone approximation of decision problems. Operations Research, 58(4-part-
2):1158–1177, 2010.
[11] V. Chernozhukov, I. Fernandez-Val, and A. Galichon. Improving point and interval estimators of monotone
functions by rearrangement. Biometrika, 96(3):559–575, 2009.
[12] A. C. Davison and D. V. Hinkley. Bootstrap Methods and Their Application. Cambridge Series in Statistical
and Probabilistic Mathematics, 1. Cambridge University Press, Cambridge, 1997.
21


## Page 22


[13] H. Dette, N. Neumeyer, and K. F. Pilz. A note on nonparametric estimation of the eﬀective dose in quantal
bioassay. Journal of the American Statistical Association, 100(470):503–510, 2005.
[14] R. C. Deutsch and W. W. Piegorsch. Benchmark dose proﬁles for joint-action quantal data in quantitative risk
assessment. Biometrics, 68(4):1313–1322, 2012.
[15] T. J. DiCiccio and J. P. Romano. A review of bootstrap conﬁdence intervals (with discussion). J. Roy. Statist.
Soc., Ser. B (Methodol.), 50(3):338–370 (corr. vol. 51, no. 3, p. 470), 1988.
[16] P. H. C. Eilers and B. D. Marx. Splines, knots, and penalties. WIREs Comput. Stat., 2(6):637–653, 2010.
[17] A. Fils-Villetard, A. Guillou, and J. Segers. Projection estimates of constrained functional parameters. Discussion
Paper 2005-111, Tilburg University, Center for Economic Research, 2005.
[18] P. Groeneboom and G. Jongbloed. Generalized continuous isotonic regression. Statistics & Probability Letters,
80(3):248 – 253, 2010.
[19] G. Hardy, J. Littlewood, and G. P´olya. Inequalities. Cambridge Mathematical Library. Cambridge University
Press, Cambridge, 1952.
[20] C. C. Holmes and N. A. Heard. Generalized monotonic regression using random change points. Statistics in
Medicine, 22(4):623–638, 2003.
[21] M. Kong and R. L. Eubank. Monotone smoothing with application to dose–response curve. Communications in
Statistics - Simulation and Computation, 35(4):991–1004, 2006.
[22] L. Lin and D. B. Dunson. Bayesian monotone regression using Gaussian process projection. Biometrika,
101(2):303–317, 2014.
[23] L. Lin, W. W. Piegorsch, and R. Bhattacharya. Nonparametric benchmark dose estimation with continuous
dose–response data. Scandinavian Journal of Statistics, 42(3):713–731, 2015.
[24] E. Mammen. Estimating a smooth monotone regression function. Ann. Statist., 19(2):724–740, 06 1991.
[25] M. W. McIntosh and M. S. Pepe. Combining several screening tests: Optimality of the risk score. Biometrics,
58(3):657–664, 2002.
[26] H.-G. Mueller and T. Schmitt. Kernel and probit estimates in quantal bioassay. Journal of the American Sta-
tistical Association, 83(403):750–759, 1988.
[27] B. Neelon and D. B. Dunson. Bayesian isotonic regression and trend analysis. Biometrics, 60(2):398–406, 2004.
[28] W. W. Piegorsch and A. J. Bailer. Analyzing Environmental Data. John Wiley & Sons, Chichester, 2005.
[29] W. W. Piegorsch, H. Xiong, R. N. Bhattacharya, and L. Lin. Benchmark dose analysis via nonparametric
regression modeling. Risk An., 34(1):135–151, 2014.
[30] K. Proksch. On conﬁdence bands for multivariate nonparametric regression. Annals of the Institute of Statistical
Mathematics, pages 1–28, 2014.
[31] J. O. Ramsay. Monotone regression splines in action. Statist. Sci., 3(4):425–441, 11 1988.
[32] T. Robertson, F. Wright, and R. Dykstra. Order Restricted Statistical Inference. Probability and Statistics
Series. John Wiley & Sons, New York, 1988.
[33] T. Rychlik. Projecting Statistical Functionals. Lecture Notes in Statistics. Springer, New York, 2001.
[34] O. Saarela and E. Arjas. A method for Bayesian monotonic multiple regression. Scandinavian Journal of Sta-
tistics, 38(3):499–513, 2011.
22


## Page 23


[35] Y. Shi, J.-H. Zhang, M. Jiang, L.-H. Zhu, H.-Q. Tan, and B. Lu. Synergistic genotoxicity caused by low concen-
tration of titanium dioxide nanoparticles and p,p’-DDT in human hepatocytes. Environmental and Molecular
Mutagenesis, 51(3):192–204, 2010.
[36] T. S. Shively, T. W. Sager, and S. G. Walker. A Bayesian approach to non-parametric monotone function
estimation. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 71(1):159–175, 2009.
[37] T. S. Shively, S. G. Walker, and P. Damien. Nonparametric function estimation subject to monotonicity, con-
vexity and other shape constraints. Journal of Econometrics, 161(2):166 – 181, 2011.
[38] G. Wahba. Spline Models for Observational Data. CBMS-NSF Regional Conference Series in Applied Mathe-
matics. Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 1990.
[39] H. H. Zhang. Splines in nonparametric regression. In A. H. El-Shaarawi and W. W. Piegorsch, editors, Ency-
clopedia of Environmetrics 5, pages 2610–2626. John Wiley & Sons, Chichester, 2nd edition, 2012.
E-mail address: lizhen.lin@nd.edu
E-mail address: brian.st.thomas@duke.edu
E-mail address: piegorsch@math.arizona.edu
E-mail address: james.scott@mccombs.utexas.edu
E-mail address: carlos.carvalho@mccombs.utexas.edu
Department of Applied and Computational Mathematics and Statistics, The University of Notre
Dame, Notre Dame, IN
Department of Statistical Science, Duke University, Durham, NC.
BIO5 Institute and Department of Mathematics, The University of Arizona, Tucson, AZ
The University of Texas McCombs School of Business, Austin, TX
The University of Texas McCombs School of Business, Austin, TX
23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
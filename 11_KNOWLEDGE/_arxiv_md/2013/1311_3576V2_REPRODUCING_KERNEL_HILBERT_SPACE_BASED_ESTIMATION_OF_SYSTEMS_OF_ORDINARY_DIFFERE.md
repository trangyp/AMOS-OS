---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1311.3576v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1311.3576v2_Reproducing_kernel_Hilbert_space_based_estimation_of_systems_of_ordinary_differe

> Source: 1311.3576v2_Reproducing_kernel_Hilbert_space_based_estimation_of_systems_of_ordinary_differe.pdf

> Pages: 18

---


## Page 1


Reproducing kernel Hilbert space based estimation
of systems of ordinary differential equations
Javier Gonz´alez1, Ivan Vujaˇci´c and Ernst Wit
Johann Bernoulli Institute of Mathematics and Computer Science,
University of Groningen, Nijenborgh 9. 9747 AG Groningen, The Netherlands
Abstract
Non-linear systems of differential equations have attracted the interest in ﬁelds
like system biology, ecology or biochemistry, due to their ﬂexibility and their
ability to describe dynamical systems. Despite the importance of such models in
many branches of science they have not been the focus of systematic statistical
analysis until recently. In this work we propose a general approach to estimate the
parameters of systems of differential equations measured with noise. Our method-
ology is based on the maximization of the penalized likelihood where the system
of differential equations is used as a penalty. To do so, we use a Reproducing
Kernel Hilbert Space approach that allows us to formulate the estimation problem
as an unconstrained numeric maximization problem easy to solve. The proposed
method is tested with synthetically simulated data and it is used to estimate the
unobserved transcription factor CdaR in Steptomyes coelicolor using gene expres-
sion data of the genes it regulates.
Keywords: System of ordinary differential equations, differential operator,
reproducing kernel Hilbert space, gene regulatory network
1. Introduction
Despite the fact that differential equations are a common modelling tool within
science and engineering, statistical methods for estimating such models have only
received wide-spread attention during the last few years. The difﬁculty of solving
differential equations in general has been a major stumbling block for efﬁcient
statistical procedures. Only in the last six years, serious progress has been made
1j.gonzalez.hernandez@rug.nl
Preprint submitted to Pattern Recognition Letters
October 3, 2018
arXiv:1311.3576v2  [stat.ME]  8 May 2014


## Page 2


on the estimation of parameters within systems of differential equations measured
with noise. More importantly, solving the differential equation in these meth-
ods is not necessary for estimating the parameters of the differential equation.
Ramsay et al. [19] introduced an approximate, two-stage maximum likelihood es-
timation procedure, where the solution of the differential equation was linked to
a smoothed version of the data. In [5] a Bayesian method is proposed similar in
spirit, whereby the solution of the ordinary differential equation (ODE) was given
as a Gaussian process prior. Estimation was effectively again a two-stage process,
where the product of experts provided a crucial link. In [21] a kernel method is
developed for estimating 1-dimensional, periodic differential equations. In [6] a
fully Bayesian inferential framework is developed to quantify uncertainty in ODE
models. In this paper, we combine the frequentist set-up, such as in [19], with
the kernel approach of [21]. The main advantage is that we can deﬁne the esti-
mation problem explicitly as a maximum likelihood problem, whereby the differ-
ential equation is interpreted as a constraint. By introducing a reproducing kernel
Hilbert space (RKHS), we transform the constrained maximization problem into
an unconstrained maximization problem. We detail this idea in Sections 3 and 4
after a revision of the main properties of RKHSs and penalized likelihood models
in Section 2. In Section 5 we focus on the implementation of our methodology.
Sections 6 and 7 illustrate the behaviour of the technique in simulated and real data
scenarios, respectively. We conclude in Section 8 with a discussion of practical
results of this work.
2. The RKHS framework: Green’s functions, penalized likelihood models
and Gaussian Processes
Reproducing Kernel Hilbert Spaces [3, 7] have played an important role in a
number of successful applications in the last decades [17, 23, 15, 10]. In this work
we use this theory for ODE estimation in the context of constrained likelihood
models.
An RKHS is a Hilbert space of functions where all the linear evaluation func-
tionals Ft : H →IR such that Ft(x) = x(t), for t ∈T, are bounded. By virtue
of the Riesz representation theorem, for each t ∈T there exists kt ∈H such that
for every x ∈H, x(t) = ⟨kt, x⟩, where ⟨, ⟩denotes the inner product in H. The
RKHS H is uniquely characterized by a continuous, symmetric and positive def-
inite function K : X × X →IR named Mercer Kernel or reproducing kernel for
H [3]. All linear combinations x(t) = P
i αiK(t, ti) where αi ∈IR and ti ∈T
2


## Page 3


equipped with the adequate inner product form a space which is dense in H. See
[23, 7] for details.
Let T be a closed interval and consider a random sample S = {(yi, ti) ∈
IR × T}n
i=1 made up of n independent observations. Assume that the conditional
distribution of yi given ti is Gaussian such that yi|ti, x, σ2 ∼N(x(ti), σ2), where
σ2 is the variance of the model and x : T →IR is the target regression function
to be estimated. To estimate x, one needs to restrict x to belong to a particular
class of models, which can be done by penalizing the likelihood with a convex
functional acting on x, generally a norm or seminorm in some Hilbert space H. A
widely studied approach is to use a differential operator P to impose smoothing
conditions on x [9]. In the Gaussian case, assuming that σ2 is known, the resulting
penalized log-likelihood is
lλ(x|S, σ2) = −1
2σ2∥x(t) −y∥2 −λ
2∥Px∥2
L2,
(1)
where ∥· ∥L2 is L2 norm, t = (t1, . . . , tn) , y = (y1, . . . , yn)T and λ > 0 controls
the balance between the ﬁtting to the data and the smoothness of the model.
The maximization of (1) can be written as a regularization problem in an
RKHS [4, 18]. To do so, a way to connect the differential operator P with a
kernel in a Hilbert space is required. A semi-constructive way to build such ker-
nel is to use the concept of the Green’s function. The Green’s function of a linear
operator P is a function G : T × T →IR that satisﬁes PG(t, z) = δ(t −z) for
δ the Dirac distribution. Roughly speaking G is the inverse of P [8]. Consider a
differential operator P and let be K a Green’s function of P ∗P where P ∗is the
adjoint operator of P. It can be shown [2] that ∥Px∥2
L2 = ∥x∥2
HK, for ∥· ∥HK the
norm in the RKHS deﬁned by K.
Expression (1) can be understood as a projection mechanism onto the ﬁnite
dimensional space spanned by {K(t, ti)} when the penalization term ∥Px∥2
L2 is
replaced by ∥x∥2
K [12, 14]. In particular, the maximizer of (1) is the function
ˆx(t) = Pn
i=1 ˆαiK(t, ti) with coefﬁcients ˆαi, obtained by maximizing
lλ(x|S, σ2) = −1
2σ2∥y −K[t]α∥2 −λ
2αTK[t]α,
(2)
with respect to α = (α1 . . . , αn)T, where K[t] is the matrix with entries (K[t])ij =
K(ti, tj). By using standard methods of differential calculus it can be shown
that the solution to the maximization problem in (2) is given by ˆα = (λσ2In +
K[t])−1y, where In is the n-dimensional identity matrix [22, 10].
3


## Page 4


3. Explicit ODE and regularization approach
3.1. Explicit ODE
In this work we are interested in dynamical systems with m interacting ele-
ments evolving in some closed time interval T. We denote by xj : T →IR for
j = 1, . . . , m, the functions describing the evolution of the elements of the system
and by uj : T →IR for i = 1, . . . , p, the action of p external forces. In compact
notation, we denote by x(t) = (x1(t), . . . , xm(t))T and u(t) = (u1(t), . . . , up(t))T
the vectors of state variables and external forces respectively. We assume that each
state variable xj satisﬁes
Pθjxj(t) = fj(x(t), u(t), β), j = 1, . . . , m, t ∈T,
(3)
where Pθj = Pd
k=1 θjkdk−1/dt is the linear differential operator associated to the
j-th equation of the system, which is deﬁned by parameters θj = (θj1, . . . , θjd)T,
and fj is a known function depending on t through x(t) and u(t) for a vector of
parameters β. In the sequel, we refer to the whole set parameters of the system
by {θ, β}, where θ = {θ1, . . . , θm}.
Typically, a ﬁnite sample of the states x is observed at a grid of time points
t = (t1, . . . , tn)T, that for simplicity we assume equal for all the states. The
sample y(t) is made up of noisy measurement of the states of the ODE. That is,
y(t) satisﬁes
y(t) = x(t) + ϵ(t),
where ϵ(t) represents a noise process. We assume ϵ(t) is independent multivariate
zero-mean Gaussian noise with variance σ2
j for each jth state. Other noise models
are possible though not trivial.
Let yj indicate the available data for state j and let xj(t) indicate the vector of
values corresponding to evaluated j-th state at time points t. The log-likelihood
of the model given the sample y(t) is given by
l(θ, β, x|y(t)) = −
m
X
j=1
1
2σ2
j
∥yj−xj(t)∥2 given that Pθjxj(t) = fj(x(t), u(t), β),
(4)
where x depends on {θ, β} although it is not explicitly speciﬁed. Indeed, for each
set of parameters {θ, β} a family of feasible solutions of the system of differential
equation is available for different initial conditions x(0).
4


## Page 5


3.2. Regularization
The maximum likelihood estimators of {β, θ} and x require explicit solutions
of the differential equation, which are generally unknown. Alternatively, compu-
tational ODE solvers result intractable in cases with a large number of parameters.
Our goal is to reformulate (4) in order to obtain a computationally tractable solu-
tion that does not require an explicit solution of the differential equation. The key
element of our approach is the penalized log-likelihood
lλ(θ, β, x|y(t)) = −
m
X
j=1
1
2σ2
j
∥yj −xj(t)∥2 −λ
2
m
X
j=1
Ω(xj)
(5)
where Ω(xj) is a convex functional that adds to the probabilistic model of the data
the information provided by the ODE and λ > 0 is a regularization parameter. As
we detail next, an RKHS representation of the ODE can be used to deﬁne Ω(xj)
avoiding the computational burden of numerical ODE solvers.
4. RKHS representation of ODE systems
If the system is homogeneous, each equation
Pθjxj = 0,
(6)
is independent of the rest. Consider the set of functions Hj = {x : ∥Pθjxj∥2 = 0}.
By the deﬁnition of the norm, Hj contains all the solutions of the differential
equation Pθjxj = 0 for some ﬁxed θj: ∥Pθjxj∥2 = 0 if and only if Pθjx = 0.
Using the connection between differential operators and RKHS detailed in Section
2, we can express the set Hj as Hj = {x : ∥x∥2
Kθj = 0} where Kθj is the Green’s
function of P ∗
θjPθj and ∥· ∥Kθj the norm in the RKHS deﬁned by Kθ. Therefore,
it makes sense to deﬁne
Ω(xj) = ∥Pθjxj∥= ∥xj∥2
Kθj ,
(7)
as penalty and proceed using the properties of penalized likelihood models in
RKHS described in Section 2. Note that by using this penalty in (5) each xj is
assumed to be an element in Hθj rather than a solution of the differential equation
unless we force ∥x∥2
Kθj to be zero, which can be imposed by taking λ →∞. In
this case, approaches in (4) and (5) are equivalent.
The main drawback is that a closed-form expression for the Green’s function
of P ∗
θjPθj is rarely available. However, note that as shown in (2), to solve the
5


## Page 6


regularization problem only the evaluation of Kθj on the sampled time points is
required. Consider the difference equation given by
Pθjxj = 0,
(8)
where Pθj = Pd
k=1 θjkDk−1 is a d-order polynomial difference operator (matrix)
acting on elements deﬁned on t and where D ∈IRn×n is a ﬁrst order differ-
ence operator such that (Dxj)1 = (t2 −t1)−1(xj,2 −xj,1), (Dxj)i = (2(ti+1 −
ti−1))−1(xj,i+1 −xj,i−1) and (Dxj)n = (tn −tn−1)−1(xj,n −xj,n−1). Note that this
this difference operator is different to the one proposed in [21], which it is only
valid for periodic differential equations. The following proposition holds.
Proposition 1. [21] Denote by H the space of functions (vectors) xj : t ⊂T →IR
equipped with the usual L2 inner product ⟨·, ·⟩. Then the Green’s function of the
difference operator P∗
θjPθj, where P∗
θj is the adjoint (transpose) operator of Pθj,
is the s × s dimensional matrix
Kθj = (PT
θjPθj)−1.
(9)
Roughly, the proof uses the fact that IRn is an RKHS whose reproducing kernel
is the location function δi, whose inner product with xj(t) yields δT
i xj(t) = xj(ti)
and therefore only the inverse of PT
θjPθj in needed. See [21] for details.
Penalty Ω(xj), although originally deﬁned for the function xj, affects the reg-
ularization process through the values of xj evaluated at a ﬁnite dimensional grid,
generally the one corresponding to the available sample. By replacing the differ-
ential equation in (6) by the difference equation (8) and using Proposition 1, we
deﬁne the penalty of the log-likelihood as
Ω(xj) = ∥Pθjxj∥2 = xT
j PT
θjPθjxj = αT
j Kθjαj,
where αj = K−1
θj xj.
4.1. Generalizations to nonhomogeneous equations
In general, the interest in inferring parameters of ODE is for systems which
are not homogeneous. In the same spirit of above, one might like to consider
Ω(xj) = ∥Pθjxj −fj(x, u, β)∥2,
(10)
as a penalty. However (10) cannot be directly used as penalizer for two reasons.
Expression (10) cannot be reformulated as a norm of xj in an RKHS. Note that
6


## Page 7


when xj = 0 then ∥Pθjxj −fj(x, u, β)∥2 is not necessarily zero. Also, in this
case the equations of the ODE are not independent. In a general setting, each xj
is affected by x1, . . . , xn.
To circumvent previous problem we follow an approach that reduces the non-
homogeneous system to an homogeneous one. The key aspect is to consider that
each fj is a function of β that does not depends directly on x but that still reﬂects
the dynamics of the system. To do so, we replace x by some ﬁxed surrogate,
namely x′(t), which is independent of θ and β and that it is estimated using the
data. In section 5 we elaborate on the deﬁnition of an appropriate x′.
In general, in order to ﬁnd a RKHS representation of the ODE system we
assume that a Green’s function Gj of each Pθj exists. Consider
˜xj(t) = xj(t) −x∗
j(t),
(11)
where x∗
j(t) =
R
T Gj(z, t)fj(x′(z), u(z), β)dz is a collection of solutions of the
differential equation. Since Pθj is a linear operator we obtain that, for all ˜xj,
Pθj ˜xj(t) = Pθjxj(t) −Pθjx∗
j(t) = Pθjxj(t) −fj(x′(z), u(z), β),
which includes the trivial solution ˜xj = 0. We can now write
Ω(˜xj) = ∥Pθjxj(t) −Pθjx∗
j(t)∥2 = ∥Pθj ˜xj∥2,
(12)
which can be studied and computed as a norm for ˜xj in Hθj equivalent to (7).
Note that the surrogate x′ is essential to linearize the system and to write Ω(˜xj) as
a norm. In practice, noise samples are obtained for xj and not for ˜xj. Therefore to
focus the inference problem on ˜xj requires to transform the original data. Details
are given in Section 5.
5. Approximate ODE inference
The goal of this section is to provide computational details to infer the set of
parameters {θ, β} using the approximate ODE representation described in Sec-
tion 4. As detailed in Section 4.1, a deﬁnition of each x′
j, a surrogate of xj is
required. In this work we express each x′
j in terms of a penalized splines basis
expansion,
x′
j(t) =
q
X
k=1
cjkφk(t) = cT
j φ(t),
(13)
7


## Page 8


for φ = (φ1(t), . . . φq(t)) and where each φj(t) a piecewise polynomial function
of degree k whose brake points or knots are located at t1, . . . , tn. The coefﬁcients
cj can be explicitly estimated by cj = (ΦTWΦ)−1ΦTWyj for Φ the design matrix
and where W is a weight matrix which allows for possible covariance structure
among the residuals See [20] for details. The number of basis q is assumed to
be large enough to capture the variation of the solutions of the ODE. Here we
assume that coefﬁcients cj are ﬁxed values obtained by smoothing the data but
further generalizations are possible.
Deﬁnition 1. Consider the penalized likelihood model in (5). Consider the objects
t, yj, xj and Pθj as deﬁned above. Let ˆx′
1, . . . , ˆx′
m be estimates of (13) for j =
1, . . . , m. We deﬁne the approximated pseudo-log-likelihood of the ODE model
associated to (5) as
lλ(θ, β|y(t), ˆx′) = −
m
X
j=1
1
2σ2
j
∥yj −xj∥2 −λ
2
m
X
j=1
∥Pθjxj −fj(ˆx′(t), u(t), β)∥2
where λ > 0 and ˆx′(t) = (ˆx1(t), . . . , ˆxm(t))T.
Next, we show how to compute lλ in practice.
Proposition 2. Assume that P−1
θj exists and deﬁne,
˜yj = yj −P−1
θj fj(u(t), ˆx′(t), β).
(14)
for j = 1, . . . , m. Consider the function
gλ(θ, β|y(t)) =
m
X
j=1
1
2σ2
j
˜yT
j
h
I −(I + σ2λK−1
θj )−1i
˜yj.
(15)
It holds that
{ˆθ, ˆβ} = arg max
θ,β lλ(θ, β, y(t)) = arg max
θ,β gλ(θ, β|y(t)).
Remark that we do not need the explicit computation of Kθj. Only its inverse
is needed, which can be obtained directly from (9). Notice that (14) performs the
data transformation equivalent to (11) that is needed to obtain a RKHS represen-
tation of the ODE in general cases. Optimization of (2) with a conjugate gradient
method produces estimates of {θ, β}. If the set of parameters of the systems is
8


## Page 9


separable by equations, independent optimization can be done for those, which
helps to avoid local minima and speed up the procedure. Finally, estimates for
each ˆxj are available by means of
ˆxj = Kˆθj ˆαj + P−1
θj fj(u(t), ˆx′(t), ˆβ)
(16)
where ˆαj = (Kˆθj + λσ2
jI)−1˜yj.
5.1. Model selection
The effective number of parameters for each equations is deﬁned as dfj =
Tr(Kˆθj(Kˆθj + λσ2
jI))−1 where Tr(·) represents the trace operator. We propose as
model selection criteria for λ the Akaike information criteria [1], which is deﬁned
in our context as
AIC(λ) = −2lλ(θ, β|y(t), ˆx′) + 2
m
X
j=1
dfj.
(17)
In practice, the minimun AIC for a grid of penalization parameters λ1, . . . , λk
should be used to select the optimal model. Note, however, that one can sim-
ply select a large value of λ to force the regularization approach to ﬁnd an exact
solution of the ODE model.
5.2. Variance of the parameter estimates and conﬁdence intervals
Conﬁdence intervals and standard errors of the parameter estimates can be
obtained from the Hessian matrix Hlλ(ˆθ, ˆβ), which is available as output of the
Conjugate Gradient algorithm [16] used to optimize lλ. The covariance matrix of
the parameter estimates is therefore obtained as ˆΣ = −Hlλ(ˆθ, ˆβ)−1 and its diag-
onal (variances of the parameters) used to estimate calculate the Wald conﬁdence
intervals.
6. Examples using synthetically generated data
6.1. Explicit ODE versus regularization approach
In this section we use a toy example to illustrate the advantages of using a
regularization approach to estimate the parameters of a dynamical system. We
consider the differential equation dx/dt −θx = 0 where D = d/dt. For ﬁxed
θ and initial condition x(0) the solution of the differential equation is given by
x(t) = x(0) exp{θt}. We ﬁx θ = −2, x(0) = −1 and we generate 500 samples of
9


## Page 10


10 equally spaced points in the interval [0, 2] using Gaussian noise with σ = 0.25.
For each sample we calculate the maximum likelihood estimator (MLE) of θ and
our RKHS based estimator for λ selected by means of the Akaike Information
Criteria (AIC) (see Section 5.1). The averaged absolute deviance to the true pa-
rameter of the MLE is 0.73 with a standard deviation of 1.03 whereas the averaged
error for the penalized approach is 0.53 with a standard deviation of 0.38. In Fig-
ure 1 we show the results for one run of the experiment. Figure 1 a) shows the
negative log likelihood and the penalized log-likelihood of the model for one of
the generated data sets. The penalized approach results in an ’improvement’ of
the original likelihood for parameter estimation with a minimum closer to the
true value of the parameter. Also note that the original negative log likelihood
becomes extremely ﬂat for small values of the parameters, which can produce
computational problems in the optimization step. Figure 1 b) shows the MLE and
RKHS solutions together with the true function x(t) = −exp{2t} for t ∈[0, 2].
Penalizing the likelihood improves the estimator in this example. The true func-
tion x is better approximated using the penalized approach due to the ﬁnite sample
bias of the MLE. Also the estimate of the parameter is closer to the true value of
θ in this particular realization (ˆθMLE = −2.55 vs. ˆθRKHS = −2.05).
6.2. Lotka volterra equations
In this experiment we work with the Lotka-Volterra system of differential
equations originally proposed in the theory of auto-catalytic chemical reaction
[13]. The formulation of the system is given by
dx1
dt = x1(θ1 −β1x2),
dx2
dt = −x2(θ1 −β2x2)
(18)
where θ = (θ1, θ2)T, β = (β1, β2)T are the parameters.
Our aim is to evaluate the accuracy and speed of our RKHS penalized ap-
proach in comparison with the classical MLE approach. To do so, we run a sim-
ulation study for ﬁxed θ1 = 0.2, β1 = 0.35 θ2 = 0.7, β2 = 0.40 and initial
conditions x1(0) = 1 and x2(0) = 2. We generate samples made up of n ﬁxed
and equally spaced independent noisy observations of the state variables x1 and
x2 in the interval T = [0, 30] that we perturb with zero mean Gaussian noise with
standard deviation σ. We generate data for the samples sizes n = 35, 70, 100 and
two noise scenarios σ = 0.1, 0.25. In Figure 2 a) we show the true solutions of
the model for the above mentioned parameters together with the data of one of the
simulations.
10


## Page 11


−3.5
−3.0
−2.5
−2.0
−1.5
−1.0
−0.5
5
10
15
20
Theta
Value
log−likelihood
penalized log−likelihood
−2.05
−2.55
(a) Negative log likelihood and the penalized
log-likelihood of the model for one of the gen-
erated data sets.
G
G
G
G
G
G
G
G
G
G
0.0
0.5
1.0
1.5
2.0
−1.0
−0.5
0.0
0.5
Time
Value
true solution
rkhs solution
mle solution
(b) Simulated data, true solution, and the two es-
timated solutions using the MLE and RKHS ap-
proaches.
Figure 1: Results obtained for the differential equation dx/dt −θx = 0
In order to apply the proposed approach we obtain the functions ˆx′
1 and ˆx′
2
using penalized splines and for ﬁx λ = 100. To perform the MLE estimation we
use an conjuate gradient algorith with 10 different initial values of the parameters
(randomly generated in the interval [0, 1]) and we use the likelihood value to select
the best candidate.
In Figure 2 b) we show a computational time comparative for the averaged
running times. The RKHS-based is 120.08, 24.06 and 14.41 times faster than the
explicit ODE approach for n = 35, 70 and 100 respectively. In Table 1 we show
the mean square errors of the estimates with respect to the true parameters for
100 runs of the experiment. For n = 35 the penalized RKHS approach performs
signiﬁcantly better than the explicit ODE estimates, which is explained by the
empirical bias suffered by the MLE approach illustrated in Section 6.1. For n =
75, 100 both methods work similarly in terms of precision. Notice that the noise
in the data is reﬂected in the precision of the estimates for both techniques; the
errors are larger in all cases for σ = 0.25.
11


## Page 12


0
5
10
15
20
25
30
0
1
2
3
4
Time
 
G
GG
G
G
GG
G
G
G
GG
G
GG
G
G
G
G
G
G
GG
GG
G
G
GG
GG
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
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
GG
G
GG
G
GGGG
GGG
G
G
G
G
GG
GG
G
G
GGG
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
GG
G
G
G
G
GG
G
G
G
G
G
G
GGG
G
GG
G
G
GG
G
G
G
G
G
G
GG
GG
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
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
(a) True solutions and the data in the Lotka-
Volterra experiment for n = 100 and σ = 0.25.
n=35
n=70
n=100
Explicit ODE
Time(Seconds)
0
20
40
60
80
100
120
n=35
n=70
n=100
Regularization
Time(Seconds)
0
20
40
60
80
100
120
(b) Computational cost comparison between the
explicit MLE approach and the proposed penal-
ized RKHS based approach.
Figure 2: Results obtained for the Lotka-Volterra equations.
7. Real example: Reconstruction of Transcription Factor activities in Strep-
tomyces coelicolor
A gene regulatory network consists of a gene encoding a transcription factor
(TF) together with the genes it regulates (genes whose activity can be activated
or repressed by binding to the DNA). In the absence of reliable technology to
measure the activity of the TF (number of TF-protein molecules in the cell), the
problem is to reconstruct it from gene expression data of its target genes.
In this experiment we work with a data set of genes expression levels in the
Streptomyces coelicolor bacterium. The goal is to reconstruct the activity of the
transcription factor (TF) cdaR using 10-points time-series gene expression data
of 17 genes. For each gene, two different series corresponding to a wild type
and mutant type bacterium (for which a transcriptional regulator cdaR has been
knocked out) are available. Measurements are available at time points (in mins.)
t = {16, 18, 20, 21, 22, 23, 24, 25, 39, 67}. The importance of understanding the
behaviour of the cdaR relies on the fact that it is partially responsible for the
production of a particular type of antibiotic.
Following Khanin et al. [11] we assume that changes in the expression levels
of the genes are caused by changes in the cdaR protein and the mRNA degrada-
12


## Page 13


Table 1: Mean square error for the inferred parameters in the Lotka-Volterra model. Standard
deviations shown in parenthesis. The true value of the parameters are ﬁxed to θ1 = 0.2, β1 = 0.35
θ2 = 0.7, β2 = 0.40
Lotka-Volterra ODE model
σ
n
Method
|θ1 −ˆθ1|
|β1 −ˆβ1|
|θ2 −ˆθ2|
|β2 −ˆβ2|
0.1
35
RKHS
0.0002 (0.0003)
0.0007 (0.0007)
0.0031 (0.0036)
0.0014 (0.0014)
MLE
0.0016 (0.0088)
0.0063 (0.0425)
0.0422 (0.1809)
0.0227 (0.1064)
70
RKHS
0.0001 (0.0001)
0.0002 (0.0002)
0.0009 (0.0011)
0.0003 (0.0004)
MLE
0.0000 (0.0001)
0.0001 (0.0006)
0.0017 (0.0034)
0.0005 (0.0010)
100
RKHS
0.0001 (0.0001)
0.0001 (0.0002)
0.0005 (0.0006)
0.0002 (0.0002)
MLE
0.0000 (0.0001)
0.0002 (0.0010)
0.0013 (0.0023)
0.0004 (0.0008)
0.25
35
RKHS
0.0010 (0.0013)
0.0017 (0.0024)
0.0111 (0.0205)
0.0038 (0.0059)
MLE
0.0029 (0.0180)
0.0081 (0.0392)
0.0173 (0.0487)
0.0078 (0.0359)
70
RKHS
0.0004 (0.0006)
0.0008 (0.0009)
0.0042 (0.0047)
0.0015 (0.0019)
MLE
0.0007 (0.0025)
0.0030 (0.0115)
0.0151 (0.0474)
0.0062 (0.0301)
100
RKHS
0.0003 (0.0004)
0.0005 (0.0006)
0.0034 (0.0043)
0.0011 (0.0016)
MLE
0.0008 (0.0032)
0.0028 (0.0116)
0.0174 (0.0603)
0.0083 (0.0387)
tion. We denote by η(t) the activity proﬁle of the regulator cdaR at time t and
by xj(t) the expression level of each gene j in time t. This regulatory system is
modelled by
d
dtxj(t) + θjxj(t) = β1j + β2j
η(t)
β3j + η(t),
(19)
where θj is the rate of mRNA degradation, β2j and β3j are gene-speciﬁc kinetic
parameters for the gene j and β1j is an additive constant that accounts for the basal
level of transcription and the nuisance effects from micro-arrays. The goal is to
use the available sample to reconstruct the levels of the activator η(t), which is
unobserved, and the gene proﬁles via the estimation of the parameters in (19). To
do so we apply the procedure described in Sections 3 and 4. We assume that the
variance is equal for all the genes. For each gene, we work with the average of the
two available time series. We model the activator η using a basis of cubic splines
with equally spaced nodes, that is η(t) = P15
j=1 ajφj where the φj’s are elements
of the basis and a1, . . . , a15 parameters to estimate. We apply the procedure de-
scribed in Section 5. We select the optimal penalization parameter λ by using the
AIC as model selection criterion.
Figure 3 a) shows the estimated proﬁle for the gene SCO3235, which ﬁts well
13


## Page 14


2
4
6
8
10
−1.0
−0.5
0.0
0.5
1.0
Gene SCO3235 inferred profile
Time order
Expression level
G
G
G
G
G
G
G
G
G
G
Reconstructed
Observed
(a) Gene SCO3235, reconstructed proﬁle. Cir-
cles and crosses represent the observed data and
lines the obtained proﬁles. The estimated vari-
ance and initial conditions are ˆσ2 = 0.016 and
ˆx(0) = −0.39. The estimated parameters for
this gene are β1 = 0.65 (stdev= 0.57), β2 =
1.07(0.51), β3 = 2.09 (0.26) and θ=1.06 (0.21).
2
4
6
8
10
0.0
0.2
0.4
0.6
0.8
1.0
cdaR TF inferred activity
Time order
Relative TF level
G
G
G
G
G
G
G
G
G
G
Reconstructed
Valildation
(b) Reconstructed activity of the master activator
cdaR scaled between 0 an 1. Circles and crosses
represent the data obtained in two independent
experiments not used in the estimation process.
Figure 3: Reconstructed genes proﬁles and master activator cdaR.
the observed data. The reconstructed genes proﬁles exhibit a similar ﬁt for the re-
maining genes. The reconstructed cdaR activator is shown in Figure 3 b) together
two independent replicates proﬁles obtained from a different experiment and that
were not used in the estimation process. The values are normalized between 0 and
1 since the activity of the cdaR protein is expressed in arbitrary units and can be
interpreted as relative levels. The estimated proﬁle ﬁts the observed data showing
two hills around time points 4 and 9 similarly to the genes proﬁles. This agrees
with the fact that cdaR is an activator of the genes activity. These result shows the
ability of the proposed approach to identify correctly unknown elements of the
ODE systems through a proper estimation of the parameters of the model. The
estimation of the parameters of this system takes around 15 mins in a personal
laptop. Further estimates of the baseline MLE estiamators are available in Khanin
et al. [11].
14


## Page 15


8. Conclusions and discussion
We have proposed a new method to estimate general systems of ordinary dif-
ferential equations measured with noise. Our proposal is based on the penaliza-
tion of the likelihood of the problem by means of the ODE. A reproducing kernel
Hilbert space approach has provided the theoretical framework to make this idea
feasible. The concept of Green’s function and the connection between linear dif-
ferential operators and Mercer kernels have been used to rewrite the penalized
likelihood of the problem in a particular manner easy to handle in practice.
The main merit of the method is its ability to perform in a single step the esti-
mation problem without solving the differential equation. In practice, our proposal
is specially competitive in small sample scenarios as it is shown via simulation. A
real example in system biology has been used to illustrate the utility of the method
in scenarios with hidden components.
In the future, we aim to focus on futher Bayesian extensions of this work, the
estimation of the regularization parameter λ and on the analysis of the theoretical
properties of the proposed method.
References
[1] Akaike, H., 1974. A new look at the statistical model identiﬁcation. IEEE
Transactions on Automatic Control 19(6), 716–723.
[2] Aronszajn, N., 1951. Green’s functions and reproducing kernels. Proceed-
ings of the Simposium on Spectral Theory and Differential Problems, Okla-
homa, 355–411.
[3] Aroszajn, N., 1950. Theory of reproducing kernels. Transactions of the
American Mathematical Society 68(3), 337–404.
[4] Berlinet, A., Thomas-Agnan, C., 2005. Reproducing kernel hilbert spaces in
probability and statistics. Srpinger.
[5] Calderhead, B., Girolami, M., Lawrence, N., 2008. Accelerating bayesian
inference over nonlinear differential equations with gaussian processes. In:
Neural Information Processing Systems. Vol. 22.
[6] Chkrebtii, O., Campbell, D. A., Girolami, M. A., Calderhead, B., Jun. 2013.
Bayesian Uncertainty Quantiﬁcation for Differential Equations. ArXiv e-
prints.
15


## Page 16


[7] Cucker, F., Smale, S., 2001. On the mathematical foundations of learning.
Bulletin of the American Mathematical Society 39(1), 1–49.
[8] Duffy, D. G., 2001. Green’s Functions with Applications. Chapman and
Hall/CRC.
[9] Green, P. J., Silverman, B. W., 1994. Nonparametric Regression and Gener-
alized Linear Models: A Roughness Penalty Approach. Vol. 58. Chapman &
Hall.
[10] Hofmann, T., Sch¨olkopf, B., J., S. A., 2008. Kernel methods in machine
learning. Annals of Statistics 36, 1171–1220.
[11] Khanin, R., Vinciotti, V., Mersinias, V., Smith, C., Wit, E., 2007. Statistical
reconstruction of transcription factor activity using michaelismenten kinetics
63 (3), 816823.
[12] Kimeldorf, G. S., Wahba, G., 1970. A correspondence between bayesian
estimation on stochastic processes and smoothing by splines. The Annals of
Mathematical Statistics 41(2), 495–502.
[13] Lotka, A. J., 1910. Contribution to the theory of periodic reaction. J. Phys.
Chem. 14 (3), 271274.
[14] Ma, X., Dai, B., Klein, R., Klein, B. E. K., Lee, K. E., Wahba, G., 2010. Pe-
nalized likelihood regression in reproducing kernel hilbert spaces with ran-
domized covariate data. Statistics 17 (1159), 46.
[15] Moguerza, J. M., Mu˜noz, A., 2006. Support vector machines with applica-
tions. Statistical Science 21(4), 322–336.
[16] Nocedal, J., Wright, S. J., 2006. Numerical Optimization, 2nd Edition.
Springer, New York.
[17] Parzen, E., 1970. Statistical inference on time series by rkhs methods. In
Proceedings 12th Biennial Seminar (R. Pyke, ed.) Canadian Mathematical
Congress, Montreal., 1–37.
[18] Poggio, T., Girosi, F., sep 1990. Networks for approximation and learning.
Proceedings of the IEEE 78 (9), 1481 –1497.
16


## Page 17


[19] Ramsay, J. O., Hooker, G., Campbell, D., Cao, J., 2007. Parameter estima-
tion for differential equations: a generalized smoothing approach. Journal
of the Royal Statistical Society: Series B (Statistical Methodology) 69 (5),
741–796.
[20] Ramsay, J. O., Silverman, B. W., 2006. Functional data analysis. Springer,
New York, 2nd ed.
[21] Steinke, F., Scholkopf, B., 2008. Kernels, regularization and differential
equations. Pattern Recognition 41 (11), 3271–3286.
[22] Vapnik, V., 1995. The nature of statistical learning theory. Springer, New
York.
[23] Wahba, G., 1990. Spline models for observational data. Series in Applied
Mathematics, SIAM. Philadelphia.
Appendix A.
Proof of Proposition 2
We prove the proposition by showing that lλ(θ, β|y(t), ˆx′) and gλ(θ, β|y(t), ˆx′)
are the same function. Consider the function
lλ(θ, β|y(t), ˆx′) = −
m
X
j=1
1
2σ2
j
∥yj −xj∥2 −λ
2
m
X
j=1
∥Pθjxj −fj(ˆx′(t), u(t), β)∥2.
Denote by fj = fj(u(t), ˆx′(t), β). We can rewrite the ﬁrst term as
m
X
j=1
1
2σ2
j
∥yj −xj∥2
=
m
X
j=1
1
2σ2
j
∥yj −P−1
θj fj + P−1
θj fj −xj∥2
=
m
X
j=1
1
2σ2
j
∥˜yj −˜xj∥2,
where ˜yj = yj −P−1
θj fj and ˜xj = xj −P−1
θj fj. Regarding the second term, we have
that
m
X
j=1
∥Pθjxj −fj∥2
=
m
X
j=1
∥Pθjxj −PθjP−1
θj fj∥2
17


## Page 18


=
m
X
j=1
∥Pθj(xj −P−1
θj fj)∥2
=
m
X
j=1
∥Pθj˜xj∥2.
Therefore, we can rewrite lλ(θ, β|y(t), ˆx′) as
lλ(θ, β|y(t), ˆx′) = −
m
X
j=1
1
2σ2
j
∥˜yj −˜xj∥2 −λ
2
m
X
j=1
∥Pθj˜xj∥2.
Using the properties of RKHSs detailed in Section 4, we can write
lλ(θ, β|y(t), ˆx′) = −
m
X
j=1
1
2σ2
j
∥˜yj −Kθjαj∥2 −λ
2
m
X
j=1
αT
j Kθjαj,
and expanding the ﬁrst terms we obtain
−
m
X
j=1
1
2σ2
j
h
˜yT
j ˜yj −2˜yT
j Kθjαj + αT
j KT
θjKθjαj + σ2λαT
j Kθjαj
i
.
For ﬁxed {θ, β} and σ2
j the maximum of lλ(θ, β|y(t), ˆx′) is given for the vec-
tors αj = (Kθj + σ2
jλI)−1˜yj. We set the derivative to zero to ﬁnd the point of
maximum. Substituting each αj and simplifying we obtain that
lλ(θ, β|y(t), ˆx′)
=
−
m
X
j=1
1
2σ2
j
h
˜yT
j ˜yj −2˜yT
j Kθj(Kθj + σ2
jλI)−1˜yj
+
˜yT
j (Kθj + σ2
jλI)−1(Kθj + σ2
jλI)Kθj(Kθj + σ2λI)−1˜yj
i
=
−
m
X
j=1
1
2σ2
h
˜yT
j ˜yj −˜yT
j Kθj(Kθj + σjλI)−1˜yj
i
=
−
m
X
j=1
1
2σ2
j
˜yT
j
h
I −(I + σ2
jλK−1
θj )−1i
˜yj
=
gλ(θ, β|y(t), ˆx′)
as we aimed to prove.
18

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
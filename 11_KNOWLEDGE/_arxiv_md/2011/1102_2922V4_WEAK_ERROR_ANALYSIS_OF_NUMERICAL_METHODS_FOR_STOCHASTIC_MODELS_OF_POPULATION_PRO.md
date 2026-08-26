---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1102.2922v4
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1102.2922v4_Weak_error_analysis_of_numerical_methods_for_stochastic_models_of_population_pro

> Source: 1102.2922v4_Weak_error_analysis_of_numerical_methods_for_stochastic_models_of_population_pro.pdf

> Pages: 32

---


## Page 1


Weak error analysis of numerical methods for stochastic models of
population processes
David F. Anderson∗and Masanori Koyama†
July 26, 2021
Abstract
The simplest, and most common, stochastic model for population processes, including those
from biochemistry and cell biology, are continuous time Markov chains.
Simulation of such
models is often relatively straightforward as there are easily implementable methods for the
generation of exact sample paths.
However, when using ensemble averages to approximate
expected values, the computational complexity can become prohibitive as the number of com-
putations per path scales linearly with the number of jumps of the process. When such methods
become computationally intractable, approximate methods, which introduce a bias, can become
advantageous. In this paper, we provide a general framework for understanding the weak error,
or bias, induced by diﬀerent numerical approximation techniques in the current setting. The
analysis takes into account both the natural scalings within a given system and the step-size
of the numerical method. Examples are provided to demonstrate the main analytical results as
well as the reduction in computational complexity achieved by the approximate methods.
1
Introduction
This paper provides a general framework for analyzing the weak error of numerical approximation
techniques for the continuous time Markov chain models typically found in the study of population
processes, including chemistry and cell biology. The main novelty of this work lies in how the
analysis takes account of both the natural multiple scalings of a given system and the step-size of
the numerical method, and is best viewed as an extension of the papers [3, 22, 23].
For k ∈{1, . . . , R}, let ζk ∈Rd denote the possible transition directions for a continuous time
Markov chain, and let λ′
k : Rd →R denote the respective intensity, or propensity functions.1 The
random time change representation for the model of interest is then
X(t) = X(0) +
R
X
k=1
Yk
Z t
0
λ′
k(X(s))ds

ζk,
(1.1)
∗Department of Mathematics, University of Wisconsin, Madison, Wi.
53706, anderson@math.wisc.edu, grant
support from NSF-DMS-1009275.
†Department of Mathematics, University of Wisconsin, Madison, Wi. 53706, koyama@math.wisc.edu, grant sup-
port from NSF-DMS-1009275 and NSF-DMS-0805793.
0AMS 2000 subject classiﬁcations: Primary 60H35, 65C99; Secondary 92C40
1In the language of probability, the functions are nearly universally termed intensity functions, whereas in the
language of chemistry and cell biology these functions are nearly universally termed propensity functions. We choose
the language of probability theory throughout the paper.
1
arXiv:1102.2922v4  [math.PR]  29 Feb 2012


## Page 2


where the Yk are independent, unit-rate Poisson processes. See, for example, [27], [14, Chapter 6 ],
or the recent survey [5]. The inﬁnitesimal generator for the model (1.1) is the operator A satisfying
(Af)(x) =
X
k
λ′
k(x)(f(x + ζk) −f(x)),
where f : Rd →R is chosen from a suﬃciently large class of functions.
The problem of simulating (1.1) (and particularly of approximating expected values) seems
deceivingly easy since we can simulate the continuous time Markov chains exactly.2 Letting f be
some function of the state of the system giving us some quantity of interest, we may estimate
Ef(X(T)) via an ensemble average,
bµn = 1
n
n
X
i=1
f(X[i](T)),
(1.2)
where X[i] is the ith independent copy of (1.1). The law of large numbers then ensures that
lim
n→∞bµn = Ef(X(T)),
(1.3)
with a probability of one. However, it is the computational work needed to achieve an accuracy
with a given tolerance, and not simply the fact that such a limit holds, that is of most interest to
us.
1.1
Scalings and computational cost
The main potential problem in trying to naively apply the limit (1.3) to a given system stems
from the fact that there is an expected computational cost to the generation of each independent
realization, which we denote by N for now, and explicitly quantify in (1.7) below.
Assuming
we wish to approximate Ef(X(T)) to an accuracy of ϵ > 0, in terms of conﬁdence intervals, we
must generate O(ϵ−2) paths yielding a total computational complexity of order O(Nϵ−2). This
computational complexity can be substantial when N is large and/or ϵ is small.
In many models of interest, including many from cell and population biology, we do, in fact,
have that N ≫1. It is therefore natural to consider how approximation schemes perform. Before
considering such schemes, however, it is important (from an analytical point of view) to modify (1.1)
by incorporating into the model a scaling parameter, N, that can eventually be used to quantify
N. The value N is usually taken to be the order of magnitude of maxi |Xi|. We then scale the
process by setting
XN
i
= N−αiXi,
where αi is chosen so that XN
i
is O(1). Deﬁning ζN
k
= N−αiζki, the general form of the scaled
model is then
XN(t) = XN(0) +
R
X
k=1
Yk

Nγ
Z t
0
Nckλk(XN(s))ds

ζN
k ,
(1.4)
where γ and ck are scalars such that
|ζN
k | = O(N−ck),
(1.5)
2This assumes the pseudo-random numbers generated by modern computers are “random enough” to be considered
truly random. We take this viewpoint throughout.
2


## Page 3


with |ζN
k | ≈N−ck for at least one k, and both XN and λk(XN(·)) are O(1). We explicitly note
that we are allowing for the possibility that |ζN
k | ≪N−ck for some of the k.
Also, note that
the models (1.1) and (1.4) are equivalent in that one is simply a scaled version of the other. For
concreteness, the scaling thus described will be carried out explicitly for the stochastic models
arising in biochemistry in Section 2.
The inﬁnitesimal generator AN for the model (1.4) is
(ANf)(x) = Nγ X
k
Nckλk(x)(f(x + ζN
k ) −f(x)),
(1.6)
where f : Rd →R is chosen from a suﬃciently large class of functions. Note that it is now natural
to take
N = Nγ X
k
Nck
(1.7)
as the order of magnitude for the number of steps required to generate a single path up to a time
of T > 0.
The parameter γ of (1.4) should be thought of as representing the natural time-scale of the
problem with γ > 0 implying a relevant time scale smaller than one. In this case of γ > 0, the
explicit numerical schemes considered in this paper are usually not a good choice and other methods,
such as averaging techniques, are usually required in conjunction with the methods described here
[5, 7, 9, 13, 25].
This fact is demonstrated by our main analytical results which provide error
bounds for the diﬀerent schemes that grow exponentially in Nγ. Therefore, our main results are
most useful when γ ≤0.
The model (1.4) is henceforth our main model of interest.
We make the following running
assumption, which in light of the fact that both XN and λk(XN(·)) are O(1), is a light one.
Running Assumption: The intensity functions λk for the scaled process XN satisfying (1.4),
together with all of their derivatives, are uniformly bounded.
The above running assumption can almost certainly be weakened to a local Lipschitz condition,
in which case analytical methods similar to those found in [24] and/or [28] can be applied. Proving
our main results in such generality, while possible and certainly worth doing in future work, will
be signiﬁcantly messier and we feel the main points of the analysis will be lost.
We return to our problem of interest and let f be a function of the state giving a quantity of
interest and consider how to approximate Ef(XN(T)). As already discussed, the computational
cost of approximating Ef(XN(T)) to an accuracy of ϵ, in the sense of conﬁdence intervals, using
the estimator (1.2) is O(Nϵ−2). Suppose now that ZN is an approximation of XN constructed
with a time-discretization step of size h > 0.3 Letting ZN
[i] denote independent copies of ZN, we
construct the estimator
bµn = 1
n
n
X
i=1
f(ZN
[i](T)).
(1.8)
Suppose that it can be shown that the approximation scheme has a weak error, or bias, of order
one. That is,
Ef(XN(T)) −Ef(ZN(T)) = O(h),
3As the approximate process explicitly depends upon the choice of h, we could denote it as ZN
h . However, for ease
of exposition we choose to drop the h dependence from the notation.
3


## Page 4


for a suitably large class of functions f. Then, noting that
Ef(XN(T)) −bµn =

Ef(XN(T)) −Ef(ZN(T))

+

Ef(ZN(T)) −bµn

,
we see that we must choose h = O(ϵ) to make the ﬁrst term on the right, the bias, O(ϵ), and
n = O(ϵ−2) to make the second term, the statistical error, have a variance of O(ϵ2), and a standard
deviation of O(ϵ). This gives a total computational complexity of O(ϵ−3). This will greatly lower the
computational complexity of the problem, as compared with using exact sample paths, if ϵ−1 ≪N.
If, instead, the method for generating ZN is second order accurate in a weak sense, that is if
Ef(XN(T)) −Ef(ZN(T)) = O(h2),
then we could choose h = O(ϵ1/2) to yield a bias of O(ϵ). This leads to a total computational
complexity of O(ϵ−2.5), which for small ϵ represents a substantial improvement over using an order
one method.
The above discussion points out that the key quantity to understand for a given approximation
method, and the focus of this paper, is the bias, or weak error, it induces for a given function f:
Bf(ZN, x, t)
def
= Exf(XN(t)) −Exf(ZN(t)).
(1.9)
Note that Bf(ZN, x, h) represents the local, one-step error of the method as the ﬁxed time-step is
of size h > 0. Analyzing the bias induced by diﬀerent numerical schemes is by now classical in the
study of stochastic processes, with nearly all the focus falling on how the bias scales with the size of
the time-step, h [26]. However, it is not suﬃcient in the current setting to simply understand how
the bias (1.9) scales with the time-discretization alone. Care must also be taken to quantify how
the leading order constants depend upon the natural scalings of a given system and given method,
here quantiﬁed by the parameter N > 0. For example, if
Ef(XN(T)) −Ef(ZN(T)) = O(cN
1 h + cN
2 h2),
then we wish to understand how cN
1 , cN
2 depend upon N since for a given choice of h we may have
that cN
1 h < cN
2 h2. In this case, the method will behave as if it is an order two method until h is
reduced to the point when cN
1 h > cN
2 h2, in which case it will behave like an order one method.
1.2
Notation and terminology
In this short subsection, we collect some necessary extra notation and terminology used throughout
the paper. We ﬁrst note that for f : Rd →R, and any t ≥0, Dynkin’s formula for the process (1.4)
is
Exf(XN(t)) = f(x) + Ex
Z t
0
ANf(X(s))ds,
(1.10)
which holds so long as the expectations exist. Similar expressions will hold for the approximate
methods under consideration. Dynkin’s formula will be our main analytical tool as it will allow us
to quantify the bias (1.9) for the diﬀerent methods and we therefore focus on developing compact
notation for the generators of our processes.
We deﬁne the operator ∇N
k for the kth possible transition, which we will typically call a “reac-
tion” in keeping with the motivating application of Section 2, via
∇N
k f(x)
def
= Nck(f(x + ζN
k ) −f(x)).
(1.11)
4


## Page 5


Note that if f is globally Lipschitz, then ∇N
k f(x) is uniformly bounded over k and x since |ζN
k | =
O(N−ck). We may now write (1.6) as
(ANf)(x) =
X
k
Nγλk(x)∇N
k f(x).
Deﬁning the vector valued operators
λ
def
= [λ1, . . . , λR],
∇N
def
= [∇N
1 , . . . , ∇N
R ],
(1.12)
where we recall that R is the number of reactions, we obtain
(ANf)(x) = (Nγλ · ∇N)f(x).
For i ∈{1, . . . , d} and k ∈{1, . . . , R}, we let mk satisfy
|ζN
k | = N−mk.
Note that, by construction, we have ck ≤mk, for all k. Finally, we denote the jth directional
derivative of f into the direction [v1, v2, ...vj] by f′[v1, ..., vj] and make the usual deﬁnition
∥f∥j
def
= sup
x {f′[v1, ...., vj](x), ∥v∥= 1}
(1.13)
1.3
Summary of main results.
The following list is a summary of our main results. Technical details and assumptions have been
omitted from the statements below for the sake of clarity.
1. In Theorem 4.1, we prove that for any explicit numerical scheme with a step-size of h > 0,
Bf(ZN, x, T) = O(Th−1 sup
z |Bf(ZN, z, h)|),
where Bf(ZN, x, t) is the bias deﬁned in (1.9). Thus, if the numerical scheme has a local, one-
step, error of O(hp+1), then the global error is O(hp). This result is standard and should be
compared to similar results in [6, 22]. It is included here since it is necessary to show that the
scalings do not alter the usual result.
2. In Theorem 5.5, we prove that if ZN
E is generated via Euler’s method, also known as explicit
τ-leaping in the setting of biochemistry, then
Bf(ZN
E , x, h) = O(ch2),
where c is independent of N. Thus, after applying Theorem 4.1, Euler’s method is proven to be
an order one method in that the leading order of the global error satisﬁes
Bf(ZN
E , x, T) = O(ch),
and decreases linearly with the step-size. This fact is formally stated in Theorem 6.4.
5


## Page 6


3. In Theorem 5.6, we prove that if ZN
M is generated via an approximate midpoint method, then
Bf(ZN
M, x, h) = O(cN
1 h2 + cN
2 h3),
where cN
1 , cN
2 depend upon the natural scalings of the system, quantiﬁed here by N > 0. The
term that dominates this error then depends upon the speciﬁc scalings of a system, encapsulated
in the constants cN
1 and cN
2 , and the size of the time discretization h. Theorem 4.1 then implies
Bf(ZN
M, x, T) = O(cN
1 h + cN
2 h2),
and the midpoint method will sometimes behave like a ﬁrst order method, and other times will
behave like a second order method. This fact is formally stated in Theorem 6.5. A transition
point, in terms of N and h, for this change in behavior is also provided.
4. In Theorem 5.8, we prove that if ZN
trap is generated via the weak trapezoidal method, which was
originally formulated in the diﬀusive setting [6] and is extended to the discrete setting in Section
3, then
Bf(ZN
trap, x, h) = O(ch3),
where c is independent of N. Thus, after applying Theorem 4.1, the Weak Trapezoidal method
is proven to be a second order method in that the leading order of the global error satisﬁes
Bf(ZN
trap, x, T) = O(ch2),
and decreases quadratically with the step-size. This fact is formally stated in Theorem 6.7.
1.4
Context
We attempt to put the present work in the correct historical context. In [3], Anderson, Ganguly,
and Kurtz provided the ﬁrst error analysis of diﬀerent approximation techniques that incorpo-
rated the natural scalings of the system (1.1) into the analysis. Speciﬁcally, they considered
models satisfying the “classical scaling,” which using our present terminology corresponds with
γ = 0, ck ≡1, and αi ≡1. They further coupled the time discretization to the scaling, thereby
ensuring h was always in a useful regime, and derived results for both the weak and strong error
of Euler’s method and the midpoint method. They proved that, in this speciﬁc setting, Euler’s
method is an order one method in both a weak and a strong (in the L1 norm) sense. They
proved that the strong error of the midpoint method falls between order one and two (see [3] for
precise statements), and that the leading order term of the weak error of the midpoint method
scales quadratically with the step-size.
In [22] it was shown by Hu, Li, and Min that the O(h2) weak convergence rate of the midpoint
method given in [3] depended intimately on the coupling between the time discretization and
the scaling parameter of the system. It was this particular observation that in a large part
motivates the present work as we wish to provide a general analytical rate of convergence for
the diﬀerent relevant methods in the most general possible scaling regime and in which the time
discretization parameter is independent of the natural scalings.
In [6] the weak trapezoidal algorithm was introduced in the context of SDEs driven by Brownian
motions. There, it was shown to be an easy to implement method that is second order accurate
in a weak sense. Further, it has the nice property that no costly derivatives need be computed
during the course of the simulation. In [23], it was pointed out that since the motivation for the
6


## Page 7


original weak trapezoidal algorithm comes from viewing SDEs as driven by space-time Wiener
processes, the exact same algorithm can work in the present jump setting by viewing the driving
forces as space-time Poisson processes. This observation was also made independently in an
earlier version of the present paper.
It is worth pointing out that there are at least two other trapezoidal type algorithms in the
literature pertaining to models of stochastic chemical kinetics. These are the implicit and explicit
trapezoidal methods of [11]. These method were explicitly developed to give better stability than
the usual methods, and so do not exhibit better convergence than does Euler’s method.
1.5
Paper outline
The remainder of the paper is organized as follows. In Section 2, we show how the basic models
considered in this paper, both (1.1) and (1.4), arise naturally in biochemistry, which is the main
area of motivation for this work. This section can safely be skipped by anyone not interested in
that application. In Section 3, we discuss numerical methods for the models under consideration,
including both exact and approximate schemes. In Section 4, we prove Theorem 4.1, as stated
loosely above, and relevant corollaries. In Section 5, we prove Theorems 5.5, 5.6, and 5.8, each
stated loosely above, providing the local, one-step errors induced by the approximate schemes
considered here. In Section 6, we provide bounds on the semigroup operator of the exact process
XN, yielding the ﬁnal piece to the global analysis of the weak error of the diﬀerent methods. We
also brieﬂy discuss stability concerns in Section 6. In Section 7, we provide relevant examples.
2
Motivating Systems: Biochemical Reaction Networks
This section builds the relevent models (1.1) and (1.4) used in the study of stochastically modeled
biochemical reaction networks. We feel it is worthwhile to include this section as this is the area
of main motivation for the present work. However, it can safely be skipped by those wishing to
simply see the mathematical analysis and not the areas of application.
2.1
The unscaled model
A chemical reaction network is a dynamical system involving multiple reactions and chemical
species. The simplest stochastic models of such networks treat the system as a continuous time
Markov chain with the state, X ∈Zd
≥0, giving the number of molecules of each species and with
reactions modeled as possible transitions of the chain.
An example of a chemical reaction is
2S1 + S2 →S3,
where we would interpret the above as saying two molecules of type S1 combine with a molecule
of type S2 to produce a molecule of type S3. The Si are called chemical species. Letting
ν1 =


2
1
0

,
ν′
1 =


0
0
1

,
and
ζ1 = ν′
1 −ν1 =


−2
−1
1

,
we see that every instance of the reaction changes the state of the system by addition of ζ1. Here
the subscript “1” is used to denote the ﬁrst (and in this case only) reaction of the system.
7


## Page 8


In the general setting we denote the number of species by d, and for i ∈{1, . . . , d} we denote
the ith species as Si. We then consider a ﬁnite set of R reactions, where the model for the kth
reaction is determined by
(i) a vector of inputs νk specifying the number of molecules of each chemical species that are
consumed in the reaction,
(ii) a vector of outputs ν′
k specifying the number of molecules of each chemical species that are
created in the reaction, and
(iii) a function of the state λ′
k that gives the transition intensity, rate, or propensity at which the
reaction occurs.
Speciﬁcally, if we denote the state of the system at time t by X(t) ∈Zd, and if the kth reaction
occurs at time t, we update the state by addition of the reaction vector
ξk
def
= ν′
k −νk
and the new state becomes X(t) = X(t−) + ξk. For the standard Markov chain model, the number
of times that the kth reaction occurs by time t can be represented by the counting process
Rk(t) = Yk
 Z t
0
λ′
k(X(s))ds

,
where the Yk are independent, unit-rate Poisson processes [27], [14, Chapter 6 ]. The state of the
system then satisﬁes
X(t) = X(0) +
X
k
Yk
Z t
0
λ′
k(X(s))ds

ξk,
which was (1.1) in the Introduction.
The above formulation is termed a random time change
representation and is equivalent to the chemical master equation representation found in much of
the biology and chemistry literature, where the master equation is Kolmogorov’s forward equation
in the terminology of probability.
A common choice of intensity function for chemical reaction systems is that of mass action
kinetics. Under mass action kinetics, the intensity function for the kth reaction is
λ′
k(x) = κ′
k
d
Y
i=1
xi!
(xi −νki)!,
(2.1)
where νki is the ith component of νk.
Example 1. To solidify notation, we consider the network
S1
κ1
⇄
κ2
S2,
2S2
κk
→S3,
where we have placed the rate constants κk above or below their respective reactions.
For this
example, equation (1.1) is
X(t) = X(0) + Y1
Z t
0
κ1X1(s)ds
 

−1
1
0

+ Y2
Z t
0
κ2X2(s)ds
 

1
−1
0


+ Y3
Z t
0
κ3X2(s)(X2(s) −1)ds
 

0
−2
1

.
8


## Page 9


Deﬁning ζ1 = [−1, 1, 0]T , ζ2 = [1, −1, 0]T , and ζ3 = [0, −2, 1]T , the generator A satisﬁes
(Af)(x) = κ1x1(f(x + ζ1) −f(x)) + κ2x2(f(x + ζ2) −f(x)) + κ3x2(x2 −1)(f(x + ζ3) −f(x)).
2.2
Scaled biochemical models
The scaling described below has been used previously in at least [4, 5, 7, 25]. We emphasize that the
scaling is an analytical tool used to understand the behavior of the diﬀerent processes, and that the
actual simulations using the diﬀerent methods make no use of, nor have need for, an understanding
of N, α, or the βk.
Let N ≫1 be a natural parameter of the system, perhaps the abundance of the species with
the highest number of molecules. Assume that the system satisﬁes (1.1) with λ′
k determined via
mass-action kinetics (2.1), and ζk ∈Zd representing the reaction vectors described in Section 2.1.
For each species i, deﬁne the normalized abundance (or simply, the abundance) by
XN
i (t) = N−αiXi(t),
where αi ≥0 should be selected so that XN
i
is O(1). Here XN
i
may be the species number (αi = 0)
or the species concentration, or something else.
Since the rate constants may also vary over several orders of magnitude, we write κ′
k = κkNβk
where the βk are selected so that κk = O(1) (recall that κ′
k is the original system parameter).
Note that while the αi are non-negative if N is chosen to be the abundance of the species with the
highest number of molecules, βk can be positive, negative, or zero.
Under the mass-action kinetics assumption, we always have that λ′
k(X(s)) = Nβk+νk·αλk(XN(s)),
where λk is deterministic mass-action kinetics with rate constants κk [5, 7, 25]. Our model has
therefore become
XN(t) = XN(0) +
X
k
Yk
Z t
0
Nβk+νk·αλk(XN(s))ds

ζN
k ,
i ∈{1, . . . , d},
(2.2)
where ζN
ki
def
= N−αiζki. To quantify the natural time-scale of the system, deﬁne γ ∈R via
γ =
max
{i,k : ζN
ki̸=0}{βk + νk · α −αi},
where we recall that νk is the source vector for the kth reaction. Letting
ck = βk + νk · α −γ,
for each k, the model (2.2) is seen to be exactly (1.4).
Remark 2.1. If βk + νk · α = αi = 1 for all i, k in (2.2), in which case γ = 0, then we have what is
typically called the classical scaling. It was speciﬁcally this scaling that was used in the analyses of
the Euler and midpoint methods found in [3, 22, 23]. In this case it is natural to consider XN as a
vector whose ith component gives the concentration, in moles per unit volume, of the ith species.
Example 2. As an instructive example, consider the system
S1
100
⇄
100
S2
9


## Page 10


with X1(0) = X2(0) = 10,000. In this case, it is natural to take N = 10,000 and α1 = α2 = 1. As
the rate constants are 100 = √10,000, we take β1 = β2 = 1/2 and ﬁnd that γ = 1/2. The equation
governing the normalized process XN
1 is
XN
1 (t) = XN
1 (0) −Y1

N1/2N
Z t
0
XN
1 (s)ds
 1
N + Y2

N1/2N
Z t
0
(2 −XN
1 (s))ds
 1
N
where we have used that XN
1 + XN
2 ≡2.
3
Numerical methods
3.1
Exact methods.
As already discussed in the introduction, because we are considering continuous time Markov chains,
there are a number of numerical methods available for the generation of exact sample paths for
the model (1.1), or the equivalent model (1.4). All are examples of discrete event simulation [21].
In the language of biochemistry these methods include the stochastic simulation algorithm, best
known as Gillespie’s algorithm in this setting [17, 18], the ﬁrst reaction method [17], and the next
reaction method [1, 16]. All such algorithms perform the same two basic steps multiple times until
a sample path is produced over a desired time interval: conditioned on the current state of the
system, both (i) the amount of time that passes until the next reaction takes place, ∆t, is computed
and (ii) the speciﬁc reaction that has taken place is found. Note that ∆t is an exponential random
variable with a parameter of P
k λk(X(t)). Therefore, if
X
k
λk(X(t)) ≈N ≫1
so that
E∆t =
1
P
k λk(X(t)) ≈1
N ≪1,
(3.1)
then the runtime needed to produce a single exact sample path may be prohibitive when coupled
with Monte Carlo techniques, and approximate methods may be desirable.
3.2
Approximate methods.
There will be times we will wish to discuss an arbitrary approximation to X or XN, and other times
we will wish to consider speciﬁc approximations. When we consider an arbitrary approximation
we will simply denote the approximation as Z or ZN. When we distinguish the Euler, midpoint,
and Weak Trapezoidal approximations, the main approximations under consideration here, we will
denote by ZE, ZM, and Ztrap the respective approximations to X, and by ZN
E , ZN
M, and ZN
trap the
respective approximations to XN. Throughout, our time-discretization parameter will be denoted
by h > 0.4
3.2.1
Euler’s method
The Euler approximation, ZE, to the model (1.1) is the solution to
ZE(t) = ZE(0) +
X
k
Yk
Z t
0
λ′
k(ZE ◦η(s))ds

ζk,
(3.2)
4Historically, the time discretization parameter for the methods described in this paper have been τ, thus giving
these methods the general name “τ-leaping methods.”
We choose to break from this tradition and denote our
time-step by h so as not to confuse τ with a stopping time.
10


## Page 11


where η(s)
def
=
j s
h
k
h, and all other notation is as before. Note that ZE(η(s)) = ZE(tn) if tn ≤s <
tn+1. The basic algorithm for the simulation of (3.2) up to a time of T > 0 is the following. For
x ≥0 we will write Poisson(x) for a Poisson random variable with a parameter of x.
Algorithm 1 (Euler’s method). Fix h > 0. Set ZE(0) = x0, t0 = 0, n = 0 and repeat the following
until tn+1 = T:
(i) Set tn+1 = tn + h. If tn+1 ≥T, set tn+1 = T and h = T −tn.
(ii) For k ∈{1, . . . , R}, let Λk = Poisson(λ′
k(ZE(tn))h) be independent of each other and all
previous random variables.
(iii) Set ZE(tn+1) = ZE(tn) + P
k Λkζk.
(iv) Set n ←n + 1.
The above algorithm is termed explicit tau-leaping in the biology and biochemistry literature
[19]. Several improvements and modiﬁcations have been made to the basic algorithm described
above over the years in the context of biochemical processes.
Many of the improvements are
concerned with how to choose the step-size adaptively [10, 20] and/or how to ensure that population
values do not go negative during the course of a simulation [2, 8, 12], which is a relevant issue as
population processes have a natural non-negativity constraint. For the simulations carried out in
Section 7, we choose to simply keep a ﬁxed step-size and set any species that goes negative in the
course of a jump to zero.
Deﬁning the operator
(Bzf)(x)
def
=
X
k
λ′
k(z)(f(x + ζk) −f(x)),
(3.3)
we see that for t > 0
Ef(ZE(t)) = Ef(ZE ◦η(t)) + E
Z t
η(t)
(BZE◦η(t)f)(ZE(s))ds,
(3.4)
so long as the expectations exist. The scaled version of (3.2), which is an approximation to XN
satisfying (1.4), is
ZN
E (t) = ZN
E (0) +
X
k
Yk

Nγ
Z t
0
Nckλk(ZN
E ◦η(s))ds

ζN
k ,
(3.5)
where all notation is as before. Deﬁne the operator BN
z by
BN
z f(x)
def
= (Nγλ(z) · ∇N)f(x).
(3.6)
If ZN
E satisﬁes (3.5), then for all t > 0
Ef(ZN
E (t)) = Ef(ZN
E (η(t))) + E
Z t
η(t)
(BN
ZN
E (η(t))f)(ZN
E (s))ds,
so long as the expectations exist.
11


## Page 12


3.2.2
Approximate midpoint method
A midpoint type method was ﬁrst described in [19]5 and analyzed in [3] and [22].
Deﬁne the
function
ρ(z)
def
= z + 1
2h
X
k
λ′
k(z)ζk,
which computes an approximate midpoint for the system (1.1) assuming the state of the system is
z and the time-step is h. Then deﬁne ZM to be the process that satisﬁes
ZM(t) = ZM(0) +
X
k
Yk
Z t
0
λ′
k ◦ρ(ZM ◦η(s))ds

ζk.
(3.7)
The basic algorithm for the simulation of (3.7) up to a time of T > 0 is the following. Note
that only step (ii) changes from Euler’s method.
Algorithm 2 (Midpoint method). Fix h > 0. Set ZM(0) = x0, t0 = 0, n = 0 and repeat the
following until tn+1 = T:
(i) Set tn+1 = tn + h. If tn+1 ≥T, set tn+1 = T and h = T −tn.
(ii) For k ∈{1, . . . , R}, let Λk = Poisson(λ′
k ◦ρ(ZM(tn))h) be independent of each other and all
previous random variables.
(iii) Set ZM(tn+1) = ZM(tn) + P
k Λkζk.
(iv) Set n ←n + 1.
For Bz deﬁned via (3.3), any t > 0, and ZM satisfying (3.7), we have
Ef(ZM(t)) = Ef(ZM ◦η(t)) + E
Z t
η(t)
(Bρ◦ZM◦η(t)f)(ZM(s))ds,
so long as the expectations exist. The scaled version of (3.7), which is an approximation to XN
satisfying (1.4), is
ZN
M(t) = ZN
M(0) +
X
k
Yk

Nγ
Z t
0
Nckλk ◦ρ(ZN
M ◦η(s))ds

ζN
k ,
(3.8)
where now
ρ(z) = z + 1
2hNγ X
k
Nckλk(z)ζN
k .
While we should write ρN in the above, we repress the “N” in this case for ease of notation. For
BN
z deﬁned via (3.6), and ZN
M satisfying (3.8), we have
Ef(ZN
M(t)) = Ef(ZN
M(η(t))) + E
Z t
η(t)
(BN
ρ(ZN
M◦η(t))f)(ZN
M(s))ds,
for all t > 0, so long as the expectations exist.
5The midpoint method detailed in [19] is actually a slight variant of the method described here.
In [19] the
approximate midpoint, called ρ(z) above, is rounded to the nearest integer value.
12


## Page 13


3.2.3
The weak trapezoidal method.
We will now describe a trapezoidal type algorithm to approximate the solutions of (1.1) and/or
(1.4). The method was originally introduced in the work of Anderson and Mattingly in the diﬀusive
setting, where it is best understood by using a path-wise representation that incorporates space-
time white noise processes, see [6]. It has independently been extended to the current jump setting
in [23] where it was studied in the classical scaling (γ = 0, αi ≡1, ck ≡1, with the step size coupled
to the system size similarly to the analysis in [3]).
In the algorithm below, which simulates a path up to a time T > 0, it is notationally convenient
to deﬁne [x]+ = x ∨0 = max{x, 0}.
Algorithm 3 (Weak trapezoidal method). Fix h > 0. Set Z(0) = x0, t0 = 0, and n = 0. Fixing a
θ ∈(0, 1), we deﬁne
ξ1
def
= 1
2
1
θ(1 −θ)
and
ξ2
def
= 1
2
(1 −θ)2 + θ2
θ(1 −θ)
.
(3.9)
We repeat the following steps until tn+1 = T, in which we ﬁrst compute a θ-midpoint y∗, and then
the new value Ztrap(tn+1):
(i) Set tn+1 = tn + h. If tn+1 ≥T, set tn+1 = T and h = T −tn.
(ii) For k ∈{1, . . . , R}, let Λk,1 = Poisson(λ′
k(Ztrap(tn))θh) be independent of each other and all
previous random variables.
(iii) Set y∗= Ztrap(tn) + P
k Λk,1ζk.
(iv) For k ∈{1, . . . , R}, let Λk,2 = Poisson([ξ1λ′
k(y∗) −ξ2λ′
k(tn)]+(1 −θ)h) be independent of each
other and all previous random variables.
(v) Set Ztrap(tn+1) = y∗+ P
k Λk,2ζk.
(vi) Set n ←n + 1.
Remark 3.1. Notice that on the (n + 1)st-step, y∗is the Euler approximation to X(nh + θh)
starting from Ztrap(tn) at time nh.
Remark 3.2. Notice that for all θ ∈(0, 1) one has ξ1 > ξ2 and ξ1 −ξ2 = 1.
We deﬁne the operator Bz1,z2 by
(Bz1,z2f)(x)
def
=
X
k
[ξ1λ′
k(z1) −ξ2λ′
k(z2)]+(f(x + ζk) −f(x)).
Then, for η(t) ≤t ≤η(t) + θh, the process Ztrap satisﬁes
Ef(Ztrap(t)) = Ef(Ztrap(η(t))) + E
Z t
η(t)
(BZtrap(η(t))f)(Ztrap(s))ds,
where we recall that Bz is deﬁned via (3.3), and for η(t) + θh ≤t ≤η(t) + h, the process Ztrap
satisﬁes
Ef(Ztrap(t)) = Ef(Ztrap(η(t) + θh)) + E
Z t
η(t)+θh
(BZtrap(η(t)+θh),Ztrap(η(t))f)(Ztrap(s))ds.
13


## Page 14


Finally, deﬁne the operator BN
z1,z2 by
(BN
z1,z2f)(x)
def
= (Nγ[ξ1λ(z1) −ξ2λ(z2)]+ · ∇N)f(x),
where for some θ ∈(0, 1), ξ1 and ξ2 satisfy (3.9), and for v ∈Rd the ith component of v+ is
[vi]+ = max{vi, 0}. Then, if ZN
trap represents the approximation to (1.4) via the weak trapezoidal
method, for η(t) ≤t < η(t) + θh
Ef(ZN
trap(t)) = Ef(ZN
trap(η(t))) + E
Z t
η(t)
(BN
ZN
trap(η(t))f)(ZN
trap(s))ds,
whereas for η(t) + θh ≤t < η(t) + h
Ef(ZN
trap(t)) = Ef(ZN
trap(η(t) + θh)) + E
Z t
η(t)+θh
(BN
ZN
trap(η(t)+θh),ZN
trap(η(t))f)(ZN
trap(s))ds.
4
Global Error from Local Error
Throughout the section, we will denote the vector valued process whose ith component satisﬁes
(1.4) by XN, and denote an arbitrary approximate process via ZN. Also, we deﬁne the following
semigroup operators acting on f ∈C0(Rd, R):
Ptf(x)
def
= Exf(XN(t))
(4.1)
Ptf(x)
def
= Exf(ZN(t)),
where for ease of notation we choose not to incorporate the notation N into either Pt or Pt.
Returning to the notation introduced in Section 1, we note that
Bf(ZN, x, t) = Exf(XN(t)) −Exf(ZN(t)) = (Pt −Pt)f(x).
We may therefore interpret the diﬀerence between the above two operators, for t ∈[0, T], as the
weak error, or bias, of the approximate process ZN on the interval [0, T]. As h > 0 is our time-step,
we note that Bf(ZN, x, h) = (Ph −Ph)f(x) is the one step local error.
Deﬁnition 1. Let n be an arbitrary non-negative integer, and M be a m dimensional vector of
C(Rd, R) valued operators on C(Rd, R), with its ℓth coordinate denoted by Mℓ. Then we deﬁne
∥f∥M
n = sup
(




 p
Y
i=1
Mℓi
!
f





∞
, 1 ≤ℓi ≤m, p ≤n
)
.
For example, if j, k, ℓ∈{1, ..., R} then
|(∇N
j ∇N
k ∇N
ℓf)(x)| ≤∥f∥∇N
3
,
where we recall that ∇N is deﬁned in (1.12). Note that, for any M,
∥f∥M
0
= ∥f∥0 = ∥f∥∞.
(4.2)
Also note that, by deﬁnition, for n ≥0
∥f∥M
n ≤∥f∥M
n+1.
14


## Page 15


Deﬁnition 2. Suppose M : C(Rd, R) →C(Rd, RR) and Q : C(Rd, R) →C(Rd, R) are operators.
Then deﬁne
∥Q∥M
j→ℓ
def
=
sup
f∈Cj,f̸=0
∥Qf∥M
ℓ
∥f∥M
j
.
Note that as stated in the Introduction, the purpose of this paper is to derive bounds for the
global weak error of the diﬀerent approximate processes, which, due to (4.2), consists of deriving
bounds for ∥(P n
h −Pnh)∥M
m→0, for an appropriately deﬁned M and a reasonable choice of m ≥0.
Theorem 4.1 below quantiﬁes how the global error ∥(P n
h −Pnh)∥M
m→0 can be bounded using the
one-step local error ∥Ph −Ph∥M
m→0. In Section 5, we will derive the requisite bounds for the local
error for each of the three methods.
Theorem 4.1. Let M be a C(Rd, RR) valued operator on C(Rd, R). Then for any n, m ≥0, and
h > 0
∥(P n
h −Pnh)∥M
m→0 = O(n ∥Ph −Ph∥M
m→0
max
ℓ∈{1,...,n}{∥Pℓh∥M
m→m})
Proof. Let f ∈C0(Rd, R). Note that, since ∥g∥0 = ∥g∥M
0
for any g,
∥P j−1
h
∥M
0→0∥Ph −Ph∥M
m→0 = ∥P j−1
h
∥0→0∥Ph −Ph∥M
m→0.
With this in mind
∥(P n
h −Pnh)f∥0 =


n
X
j=1
(P j
hPh(n−j) −P j−1
h
Ph(n−j+1))f


0
≤
n
X
j=1
∥P j−1
h
(Ph −Ph)Ph(n−j)f∥0
≤
n
X
j=1
∥P j−1
h
∥0→0∥Ph −Ph∥M
m→0∥Ph(n−j)∥M
m→m∥f∥M
m .
Since Ph is a contraction, i.e. ∥Ph∥0→0 ≤1, the result is shown.
The following result, where ∇N replaces M in Theorem 4.1, is now immediate.
Corollary 4.2. Under the same assumptions of Theorem 4.1 and with f ∈Cm
0 (Rd, R),
∥(P n
h −Pnh)f∥∇N
0
= O(n∥Ph −Ph∥∇N
m→0
max
ℓ∈{1,...,n}{∥Pℓhf∥∇N
m }).
The following generalization, which allows for variable step sizes, is straightforward.
Corollary 4.3. For f ∈Cm
0 (Rd, R)
∥Exf(Ztn) −Exf(Xtn)∥∞= O(n max
i=1,...,n{∥Phi −Phi∥∇N
m→0}
max
ℓ∈{1,...,n}{∥Ptℓf∥∇N
m }).
Thus, once we compute the local one step error ∥Ph −Ph∥∇N
m→0 for an approximate process, we
have a bound on the global weak error that depends only on the semigroup Pt of the original process.
We will delay discussion of ∥Ptf∥∇N
m
for now, as this term is independent of the approximate process.
Instead, in the next section we provide bounds for ∥Ph −Ph∥∇N
m→0 for each of the three methods
described in Section 3.
15


## Page 16


5
Local errors
Section 5.1 will present some necessary propositions and lemmas. Sections 5.2, 5.3, and 5.4 will
present the local analyses of the Euler, midpoint, and weak trapezoidal methods, respectively.
5.1
Analytical tools
Proposition 5.1. Let f ∈C1
0(Rd, RR). For any k ∈{1, . . . , R}
∇N
k f ∈O(Nck−mk∥f∥1) ⊂O(1).
In particular, N−ck∇N
k f is bounded.
Proof. The result follows from the fact that for any w ∈Rd
|f(x + w) −f(x)| ≤|w|∥f∥1.
Deﬁne, for any multi-subset I of {1, ..., R},
∇N
I f
def
=


(
|I|
Y
i=1
∇N
ℓi )f


,
so that,
∥f∥∇N
n
= sup
|I|≤n
∥∇N
I f∥∞.
Proposition 5.2. Let f ∈Cj
0(Rd, RR). Then,
∥f∥∇N
j
= O(∥f∥j).
Proof. The case j = 1 follows from Proposition 5.1. Now consider ∇N
I f(x) for a multi-set I of
{1, . . . , R}, with |I| = j ≥2. If mk > 0 for all k ∈I, the statement is clear. If on the other hand,
mk = 0 for some k ∈I, then for this speciﬁc k, we have ck ≤0 and
∥∇N
I f∥∞≤2Nck∥∇N
I\kf∥∞= O(∥f∥j−1) = O(∥f∥j),
where the second to last equality follows by an inductive hypothesis.
We make some deﬁnitions associated with ∇N. Let g : Rd →RR. For i, j ∈{1, . . . , R}
[DNg(x)]ij
def
= ∇N
j gi(x)
[(∇N)2]ij
def
= ∇N
i ∇N
j
diag(Nc)
def
= diag(Nc1, ..., NcR).
(5.1)
Also, we deﬁne 1R to be the R dimensional vector whose entries are all 1.
Lemma 5.3. (Product Rule) Let g, q : Rd →RR be vector valued functions. Then
∇N
k (g · q)(x) = (∇N
k g · q)(x) + (g · ∇N
k q)(x) + N−ck(∇N
k g · ∇N
k q)(x).
Also,
∇N(g · q)(x) = [DNg]T q(x) + [DNq]T g(x) + diag(Nc)−1([DNg]T × [DNq]T )(x)1Rf.
16


## Page 17


Proof. Note that, for any k,
∇N
k (g · q)(x) =Nck(g(x + ζN
k )q(x + ζN
k ) −g(x)q(x))
= Nck(g(x + ζN
k ) −g(x))q(x) + Nck(q(x + ζN
k ) −q(x))g(x)
+ N−ckNck(q(x + ζN
k ) −q(x))Nck(g(x + ζN
k ) −g(x))
= (∇N
k g) · q)(x) + (∇N
k q · g)(x) + N−ck(∇N
k g · ∇N
k q)(x),
verifying the ﬁrst statement. To verify the second, one simply notes that the above calculation
holds for every coordinate, and the result follows after simple bookkeeping.
Corollary 5.4. Let λ : Rd →RR be a vector valued function, and f : Rd →R. Then
∇N
k (λ · ∇Nf)(x) = (∇N
k λ · ∇N)f + λ · ∇N∇N
k f + N−ck∇N
k λ · ∇N∇N
k f.
Also,
∇N(λ · ∇Nf) = [DNλ]T ∇Nf + [(∇N)2f]λ + diag(Nc)−1([DNλ × (∇N)2]1Rf.
(5.2)
Proof. Simply put g = λ and q = ∇Nf, and note that ∇2 is symmetric.
5.2
Euler’s method
Throughout subsection 5.2, we let ZN
E be the Euler approximation to XN, and let
PE,hf(x)
def
= Exf(ZN
E (h)),
where h is the step-size taken in the algorithm. Below, we will assume h < N−γ, which is a natural
stability condition, and is discussed further in Section 6.2.
Theorem 5.5. Suppose that the step size h satisﬁes h < N−γ. Then
∥PE,h −Ph∥∇N
2→0 = O(N2γh2).
Proof. For Euler’s method with initial condition x0,
PE,hf(x0) = f(x0) + hBN
x0f(x0) + h2
2 (BN
x0)2f(x0) + O(N3γ∥f∥∇N
3
h3),
(5.3)
where, noting ∇Nλ(x0) = 0 and using the product rule in Lemma 5.3, we have
BN
x0f = Nγλ(x0) · ∇Nf
(BN
x0)2f = Nγλ(x0) · ∇N(Nγλ(x0) · ∇Nf)
= N2γλ(x0)T [(∇N)2f]λ(x0).
(5.4)
On the other hand, for the exact process (1.4),
Phf(x0) = f(x0) + hANf(x0) + h2
2 (AN)2f(x0) + O(N3γ∥f∥∇N
3
h3),
(5.5)
where, again,
ANf = Nγλ · ∇Nf.
17


## Page 18


Noting that,
(AN)2f(x) = N2γ(λ · ∇N(λ · ∇Nf(x)))
= N2γλT ([DNλ]T ∇Nf(x) + [(∇N)2f]λ(x) + N2γλT (diag(N−c)[DNλ × (∇)2]1Rf)
(5.6)
and deﬁning
a(x)
def
= N2γλT [DNλ]T ∇Nf(x)
b(x)
def
= N2γλT [(∇N)2f]λ(x)
c(x)
def
= N2γλT [diag(N−c)[DNλ × (∇N)2]1Rf(x)],
we can write
Phf(x0) = f(x0) + hANf(x0) + h2
2 (a(x0) + b(x0) + c(x0)) + O(N3γ∥f∥∇N
3
h3).
Note that BN
x0f(x0) = ANf(x0) and b(x0) = (BN
x0)2f(x0). We may then compare (5.3) and (5.5)
(PE,h −Ph)f(x0) = h2
2 ((BN
x0)2f(x0) −(a(x0) + b(x0) + c(x0))) + O(N3γ∥f∥∇N
3
h3)
= h2
2 (−a(x0) −c(x0)) + O(N3γ∥f∥∇N
3
h3).
The term a(x) + c(x) = O(N2γ∥f∥∇N
2
) is clearly non-zero in general, giving the desired result.
5.3
Approximate midpoint method
Throughout subsection 5.3, we let ZN
M be the midpoint method approximation to XN, and let
PM,hf(x)
def
= Exf(ZN
M(h)),
where h is the step-size taken in the algorithm. As before, we will assume h < N−γ, which is a
natural stability condition, and is discussed further in Section 6.2.
Theorem 5.6. Suppose that the step size h satisﬁes h < N−γ. Then
∥(PM,h −Ph)∥∇N
3→0 = O(N3γh3 + N2γ−min{mk}h2).
Remark 5.7. Theorem 5.6 predicts that the midpoint method behaves locally like a third order
method and globally like a second order method if h is in a regime satisfying Nγh ≫N−min{mk},
or equivalently if h ≫N−γ−min{mk}. This agrees with the result found in [3] pertaining to the
midpoint method, which had γ = 0, mk ≡1, and the running assumption that h ≫1/N. This
behavior is demonstrated via numerical example in Section 7.
Proof. (of Theorem 5.6) Let ζN denote the matrix with kth column ζN
k , i.e.
[ζN] = [ζN
1 , ζN
2 , ...., ζN
R ].
Recall that ρ is deﬁned via
ρ(z) = z + h
2Nγ X
k
λk(z)NckζN
k .
18


## Page 19


After some algebra, we have
BN
ρ(x0)f(x) = Nγ(λ(x0 + h
2Nγ X
k
λk(x0)NckζN
k )) · ∇Nf(x)
= Nγλ(x0) · ∇Nf(x) + w(x0) + O(N2γ∥f∥∇N
1
h2).
where
w(x)
def
= N2γ h
2[Dλ(x0)][ζN]diag(Nc)λ(x0) · ∇Nf(x).
Next, using the product rule (5.2), we see
(BN
ρ(x0))2f(x) = Nγλ(x0 + h
2[ζN]diag(Nc)λ(x0)) · ∇N(Nγλ(x0 + h
2[ζN]diag(Nc)λ(x0)) · ∇Nf)(x)
= N2γλ(x0 + h
2[ζN]diag(Nc)λ(x0))T [(∇N)2f]λ(x0 + h
2[ζN]diag(Nc)λ(x0)) · ∇Nf)(x)
= g(x0) + O(N2γ∥f∥∇N
2
h),
where
g(x0)
def
= N2γλ(x0)T [(∇N)2f(x)]λ(x0).
Therefore, since Nγλ(x0) · ∇Nf(x0) = ANf(x0), it follows that
PM,hf(x0) = f(x0) + hBN
ρ(x0)f(x0) + h2
2 (BN
ρ(x0))2f(x0) + O(N3γ∥f∥∇N
3
h3)
= f(x0) + h

ANf(x0) + w(x0) + O(N2γ∥f∥∇N
2
h2)

+ h2
2

g(x0) + O(N2γ∥f∥∇N
2
h)

+ O(N3γ∥f∥∇N
3
h3).
Recall that
(AN)2f(x) = a(x) + b(x) + c(x),
where
a(x) = N2γλT [DNλ]T ∇Nf(x),
b(x) = N2γλT [(∇N)2f]λ(x),
c(x) = N2γλT [diag(N−c)[DNλ × (∇N)2]1Rf(x)],
(5.7)
and
Phf(x0) = f(x0) + hANf(x0) + h2
2 (a(x0) + b(x0) + c(x0)) + O(N3γ∥f∥∇N
3
h3).
Noting that b(x0) = g(x0), we see
(PM,h −Ph)f(x0) = hw(x0) + h2
2 (g(x0) −(a(x0) + b(x0) + c(x0))) + O(N3γ∥f∥∇N
3
h3)
= (hw(x0) −h2
2 a(x0)) −h2
2 c(x0) + O(N3γ∥f∥∇N
3
h3).
(5.8)
We will now gain control over the terms (hw(x0) −h2
2 a(x0)) and h2
2 c(x0), separately.
19


## Page 20


Handling h2
2 c(x0) ﬁrst, we have that ∇Nλk ∈O(Nck−mk), and so
c(x0) = O(N2γ−min{mk}∥f∥∇N
2
).
Next, we will show that
hw(x0) −h2
2 a(x0) = O(N2γ−min{mk}∥f∥∇N
1
h2).
We have
hw(x0) −h2
2 a(x0) = h2
2 N2γ[Dλ(x0)][ζN]diag(Nc)λ(x0) · ∇Nf(x0) −h2
2 N2γλT [DNλ]T ∇Nf(x)
= h2
2 N2γ

[Dλ(x0)][ζN]diag(Nc) −[DNλ(x0)]

λ(x0) · ∇Nf(x0).
(5.9)
By Proposition 5.2, ∇Nf(x) is bounded by ∥f∥∇N
1
.
Therefore, we just need to show that the
diﬀerence between the two square matrices
[DNλ(x0)]
and
[Dλ(x0)][ζN]diag(Nc)
(5.10)
is O(N−min{mk}). Recalling the deﬁnitions in (5.1), the (i, j)th entry of the left side of (5.10) is
Ncj(λi(x0 + ζN
j ) −λi(x0))
whereas that of the right side of (5.10) is
Ncj∇λi · ζN
j .
Also, note that, for λ ∈C2
c (Rd, R),
((λ(x + v) −λ(x)) −∇λ(x) · v) ∈O(|v|2∥λ∥2).
where
∥λ∥2 = sup{∥λ∥∞, ∥∂xiλ∥∞, ∥∂xj∂xℓλ∥∞, i, j, k ≤d.}
Since ∥λk∥2 is bounded for any k, the diﬀerence between the (i, j)th entries of the two expressions
in (5.10) is
O(NcjN−2mj).
Also, recall that cj −mj ≤0. Thus the above is also
O(N−min{mk}).
Therefore (5.9) is of order
O(N2γ−min{mk}h2∥f∥∇N
1
),
as desired. Combining the above with (5.8) gives us
∥(Ph −PM,h)f∥0 = O(N2γ−min{mk}∥f∥∇N
1
h2 + N2γ−min{mk}∥f∥∇N
2
h2 + N3γ∥f∥∇N
3
h3)
= O(∥f∥∇N
3
[N3γh3 + N2γ−min{mk}h2]),
(5.11)
implying
∥PM,h −Ph∥∇N
3→0 = O(N3γh3 + N2γ−min{mk}h2),
as desired.
20


## Page 21


5.4
Weak trapezoidal method
Throughout subsection 5.4, we let ZN
trap be the weak trapezoidal approximation to XN, and let
Ptrap,hf(x)
def
= Exf(ZN
trap(h)),
where h is the size of the time discretization. We will again only consider the case h < N−γ, which
is a natural stability condition and is discussed further in Section 6.2.
We make the standing assumption that for all x in our state space of interest, and k, j ∈
{1, . . . , R}, we have
ξ1λk(x + ζN
j ) −ξ2λk(x) ≥0,
(5.12)
where ξ1 > ξ2 are deﬁned in (3.9) for some θ ∈(0, 1). Noting that ζN
j
will often be small, and that
ξ1 −ξ2 = 1, for most processes, including those arising from biochemistry, the requirement (5.12)
holds so long as the process is not directly at the boundary of the positive orthant. Weakening
(5.12) is almost certainly doable, for example by gaining control over the probability that a process
leaves a region in which the condition holds. This is an avenue for future work.
Theorem 5.8. Suppose that the step size h satisﬁes h < N−γ. Then
∥(Ptrap,h −Ph)∥∇N
3→0 = O(N3γh3).
Proof. Consider one step of the method with a step-size of size h and with initial value x0. Note
that the ﬁrst step of the algorithm produces a value y∗that is distributionally equivalent to one
produced by a Markov process with generator BN
1 given by
BN
1 f(x) = Nγλ(x0) · ∇Nf(x).
Next, given both x0 and y∗, step 2 produces a value which is distributionally equivalent to one
produced by a Markov process with generator
BN
2 f(x) = Nγ[ξ1λ(y∗) −ξ2λ(x0)]+ · ∇Nf(x).
(5.13)
Recall that for the exact process,
Phf(x0) = f(x0) + hANf(x0) + h2
2 (AN)2f(x0) + O(N3γ∥f∥∇N
3
h3).
For the approximate process we have,
Ptrap,hf(x0) = Ex0[Ex0[f(ZN
trap(h))|y∗]]
= Ex0f(y∗) + (1 −θ)hEx0[BN
2 f(y∗)] + (1 −θ)2h2
2
Ex0[(BN
2 )2f(y∗)] + O(N3γ∥f∥∇N
3
h3).
(5.14)
We will expand each piece of (5.14) in turn. Noting that BN
1 f(x0) = ANf(x0), the ﬁrst term is
Ex0f(y∗) = f(x0) + Ex0
Z θh
0
BN
1 f(Zs)ds

= f(x0) + θhANf(x0) + θ2h2
2
(BN
1 )2f(x0) + O(N3γ∥f∥∇N
3
h3).
21


## Page 22


We turn attention to the second term, (1 −θ)hEx0[BN
2 f(y∗)], and begin by making the following
deﬁnition:
g(y∗)
def
= BN
2 f(y∗) = Nγ[ξ1λ(y∗) −ξ2λ(x0)]+ · ∇Nf(y∗),
so that g(x) = Nγ([ξ1λ(x) −ξ2λ(x0)]+ · ∇N)f(x). Because ξ1 −ξ2 = 1, we have
g(x0) = Nγλ(x0) · ∇Nf(x0) = ANf(x0).
By our standing assumption (5.12)
g(x0 + ζk) −g(x0) = Nγ(ξ1λ(x0 + ζk) −ξ2λ(x0)) · ∇Nf(x0 + ζk) −Nγλ(x0) · ∇Nf(x0).
After some algebra
BN
1 g(x0) = Nγ(λ(x0) · ∇Ng)(x0) = Nγ X
k
Nckλk(x0)[g(x0 + ζk) −g(x0)]
= ξ1Nγλ(x0) · ∇N(Nγλ · f)(x0) −ξ2Nγλ(x0) · ∇N(λ(x0) · f)(x0)
= ξ1(BN
1 ANf(x0)) −ξ2((BN
1 )2f)(x0).
Thus,
Ex0[BN
2 f(y∗)] = Ex0[g(y∗)] = g(x0) + θhBN
1 g(x0) + O(N3γ∥f∥∇N
3
h2)
= ANf(x0) + θh

ξ1(BN
1 ANf)(x0) −ξ2(BN
1 )2f(x0)

+ O(N3γ∥f∥∇N
2
h2)
= ANf(x0) + θh

ξ1(AN)2f(x0) −ξ2(BN
1 )2f(x0)

+ O(N3γ∥f∥∇N
3
h2),
where the last line follows since BN
1 f(x0) = ANf(x0) for any f.
Finally, we turn the the last term in (5.14). Deﬁne
q(y∗)
def
= (BN
2 )2f(y∗)
= [ξ1λ(y∗) −ξ2λ(x0)]+ · ∇N([ξ1λ(y∗) −ξ2λ(x0)]+∇Nf)(y∗),
so that
q(x) = [ξ1λ −ξ2λ(x0)]+ · ∇N([ξ1λ −ξ2λ(x0)]+∇Nf)(x).
By our standing assumption (5.12) we have
Ex0[(BN
2 )2f(y∗)] = Ex0[q(y∗)]
= q(x0) + O(N3γ∥f∥∇N
3
h)
= (BN
1 )2f(x0) + O(N3γ∥f∥∇N
3
h).
(5.15)
Noting that
(1 −θ)θξ1 = 1
2
and
(1 −θ)θξ2 = (1 −θ)2 + θ2
2
,
22


## Page 23


we may conclude the following from the above calculations
Ex0[f(ZN
trap,h)] = Ex0f(y∗) + (1 −θ)hEx0[BN
2 f(y∗)] + (1 −θ)2h2
2
Ex0[(BN
2 )2f(y∗)]
+ O(N3γ∥f∥∇N
3
h3)
= f(x0) + θhANf(x0) + θ2h2
2
(BN
1 )2f(x0)
+ (1 −θ)hANf(x0) + h2
2 (AN)2f(x0) −h2
2 [(1 −θ)2 + θ2](BN
1 )2f(x0)
+ (1 −θ)2h2
2
(BN
1 )2f(x0) + O(N3γ∥f∥∇N
3
h3)
= f(x0) + ANf(x0) + h2
2 (AN)2f(x0) + O(N3γ∥f∥∇N
3
h3).
Thus
∥(Ptrap,h −Ph)f∥0 ∈O(N3γ∥f∥∇N
3
h3),
and the proof is complete.
6
Global Bounds and Stability
In Section 6.1 we bound ∥Ptf∥∇N
n
, which was the remaining piece to handle in Theorem 4.1 to give
us global bounds on the weak error induced by the diﬀerent methods. In Section 6.2, we brieﬂy
discuss some issues related to stability of the diﬀerent methods.
6.1
Bounds on ∥Ptf∥∇N
n
In this section we bound ∥Ptf∥∇N
n
, where n is a nonnegative integer and Pt is the semigroup
operator (4.1) of the scaled process (1.4). We point out, however, that for any process XN for
which Pt is well behaved, in that ∥Pt∥∇N
n→0 is bounded uniformly in N, the following results are not
needed, and, in fact, would most likely be a least optimal bound, as the bound grows exponentially
in Nγt. Note that any system satisfying the classical scaling has γ = 0. We also point out that
the arguments used below are quite similar to those used in [22] by Hu, Li, and Min, which were
extensions of those used in [3] by Anderson, Ganguly, and Kurtz.
For t ≥0 and any x ∈Rd, We deﬁne
v(t, x)
def
= Ptf(x) = Exf(XN
t ).
Theorem 6.1. If ∥f∥∇N
n
< ∞, then
∥v(t, ·)∥∇N
n
= ∥Ptf∥∇N
n
≤∥f∥∇N
n
eNγCnt
where
Cn = 2

∥λ∥∇N
1
n R + R(n −1)∥λ∥∇N
n

.
(6.1)
We delay the proof of Theorem 6.1 until the following Lemma is shown, the proof of which is
similar to that found in [22], which itself was an extension of the proof of Lemma 4.3 in [3].
23


## Page 24


Lemma 6.2. Given a multiset I of {1, · · · , R}, there exists a function qI(x) that is a linear function
of terms of the form ∇N
J v(t, x) with |J| < |I|, so that
∂t∇N
I v(t, x) = Nγ(λ · ∇N)∇N
I v(t, x) + Nγ
|I|
X
i=1
(βi · ∇N)∇I\ℓiv(t, x + ζℓi) + NγqI(x),
where βi = ∇N
ℓi λ. Further, qI consists of at most R(|I| −1) terms of the form ∇N
J v(t, x), each of
whose coeﬃcients are bounded above by ∥λ∥∇N
|I| .
Proof. This goes by induction. For |I| = 0, the statement follows because
∂tv(t, x) = Nγ(λ · ∇N)v(t, x).
(6.2)
Note that in this case, there are no βi or q terms. It is instructive to perform the |I| = 1 case. We
have
∂t∇N
k v(t, x) = ∇N
k ∂tv(t, x)
= ∇N
k (Nγλ · ∇Nv(t, x))
= Nγ(∇N
k λ · ∇N)v(t, x) + Nγλ · ∇N
k ∇Nv(t, x) + Nγ(N−ck∇N
k λ · ∇N
k ∇Nv(t, x)).
Note that for any g : Rd →R
(∇N
k λ · ∇N)g(x) + (N−ck∇N
k λ · ∇N)∇N
k g(x) = (∇N
k λ · ∇N)g(x + ζk).
(6.3)
Therefore, with g(x) = v(t, x) in the above, we have
∂t∇N
k v(t, x) = Nγ(λ(x) · ∇N)∇N
k v(t, x) + Nγ(∇N
k λ(x) · ∇N)v(t, x + ζk).
Now assume that it holds for a set of size ≤|I|. Then, using the inductive hypothesis, Lemma
5.2, and equation (6.3) yields
∂t∇N
k ∇N
I v(t, x)
= ∇N
k ∂t∇N
I v(t, x)
= Nγ∇N
k

(λ · ∇N)∇N
I v(t, x) +
|I|
X
i=1
(βi · ∇N)∇I\ℓiv(t, x + ζℓi) + qI(x)

= Nγ

(λ · ∇N)∇N
I∪kv(t, x) + (∇N
k λ · ∇N)∇N
I v(t, x + ζk)

+ Nγ
|I|
X
i=1

(βi · ∇N)∇N
k ∇N
I\ℓiv(t, x + ζℓi) + (∇N
k βi · ∇N)∇N
I\ℓiv(t, x + ζℓi + ζk)

+ Nγ∇N
k qI(x)
= Nγ(λ · ∇N)∇N
I∪kv(t, x) + Nγ

(∇N
k λ · ∇N)∇N
I∪k\kv(t, x + ζk) +
|I|
X
i=1
(βi · ∇N)∇N
I∪k\ℓiv(t, x + ζℓi)

+ Nγ

∇N
k qI(x) + (∇N
k βi · ∇N)∇N
I\ℓiv(t, x + ζℓi + ζk)

,
showing the result.
24


## Page 25


Proof. (of Theorem 6.1 )
Let n ≥0. Deﬁne
Un(t)
def
=
max
x,|I|≤n |∇N
I v(t, x)| = ∥v∥∇N
n
.
Each ∇N
I v(t, x) is a continuously diﬀerentiable function with respect to t. Therefore, the maximum
above is achieved at some (I∗, x∗) for all t ∈[0, t1] where t1 > 0. Fixing this choice of (I∗, x∗), we
have
Un(t) = ∇N
I∗v(t, x∗)
for all t < t1.
Note that
[(λ · ∇N)∇N
I∗v(t, x∗)]∇N
I∗v(t, x∗) =
X
k
λk(x)(∇N
k ∇N
I∗v(t, x∗))∇N
I∗v(t, x∗)
=
X
k
Nckλk(x)(∇N
I∗v(t, x∗+ ζk) −∇N
I∗v(t, x∗))∇N
I∗v(t, x∗)
≤0,
(6.4)
where the ﬁnal inequality holds by the speciﬁc choice of I∗and x∗. Also note that for any ℓi ∈I∗
and any choice of x
|∇N∇N
I∗\ℓiv(t, x)| ≤
R
X
k=1
|∇k∇N
I∗\ℓiv(t, x)| ≤R|∇N
I∗v(t, x∗)|.
(6.5)
From Lemma 6.2 and equations (6.4) and (6.5), we have
1
2∂t(∇N
I∗v(t, x∗))2 = (∂t∇N
I∗v(t, x∗))∇N
I∗v(t, x∗)
= Nγ

(λ · ∇N)∇N
I∗v(t, x∗) +
|I∗|
X
i=1
(βi · ∇N)∇I∗\ℓiv(t, x∗+ ζℓi) + qI∗(x∗)

∇N
I∗v(t, x∗)
(6.6)
≤Nγ

∥λ∥∇N
1
|I∗| R |∇N
I∗v(t, x∗)|2 + R(|I∗| −1)∥λ∥∇N
|I∗||∇N
I∗v(t, x∗)|2

,
where we have used the fact that each βi = ∇ℓiλ for ℓi ∈I∗. Setting
Cn = 2

∥λ∥∇N
1
n R + R(n −1)∥λ∥∇N
n

,
(6.7)
we see by an application of Gronwall’s inequality that the conclusion of the theorem holds for all
t < t1. That is, for t < t1
Un(t) ≤∥f∥∇N
n
eNγCnt.
To continue, repeat the above argument on the interval [t1, t2), with I∗, x∗again chosen to maximize
Un on that interval, and note that
Un(t1) ≤∥f∥∇N
n
eNγCnt1,
so that we may conclude that for t1 ≤t < t2,
Un(t) ≤∥f∥∇N
n
eNγCnt1eNγCn(t−t1) = ∥f∥∇N
n
eNγCnt.
Continuing on, we see that ti →∞as i →∞by the boundedness of the time derivatives of v(t, x),
thereby concluding the proof.
25


## Page 26


Remark 6.3. In the theorem above, Cn ∈∥λ∥∇N
n
.
Combining all of the previous results, we have the following theorems.
Theorem 6.4. (Global bound for the Euler method)
Suppose that the step size h satisﬁes h < N−γ, and T = nh. Then
∥(P n
E,h −Pnh)∥∇N
2→0 = O(N2γheC2NγT )
where C2 ∈O(∥λ∥∇N
2
) is deﬁned in (6.1).
Theorem 6.5. (Global bound for the midpoint method)
Suppose that the step size h satisﬁes h < N−γ, and T = nh. Then
∥(P n
M,h −Pnh)∥∇N
3→0 = O([N3γh2 + N2γ−min{mk}h]eC3NγT )
where C3 ∈O(∥λ∥∇N
3
) is deﬁned in (6.1).
The following immediate corollary to the theorem above recovers the result in [3].
Corollary 6.6. Under the additional condition h > N−γ−min{mk} in Theorem (6.5), the leading
order of the error of the midpoint method is O(h2).
Theorem 6.7. (Global bound for the weak trapezoidal method)
Suppose that the step size h satisﬁes h < N−γ, and T = nh. Then
∥P n
trap,h −Pnh∥∇N
3→0 = O(h2N3γeNγC3T )
where C3 ∈O(∥λ∥∇N
3
) is deﬁned in (6.1).
Thus, we see that the weak trapezoidal method detailed in Algorithm 3 is the only method that
boasts a global error of second order in the stepsize h in an “honest sense.” That is, it is a second
order method regardless of the relation of h with respect to N. This is in contrast to the midpoint
method which has second order accuracy only when the order of h is larger than N−γ−min{mk}.
6.2
Stability Concerns
The main results and proofs of our paper have incorporated stability concerns into the analysis.
This is seen in the statements of the theorems by the running condition that h < N−γ, where we
recall that Nγ should be interpreted as the time-scale of the system. Without this condition, the
methods are unstable. It is an interesting question, and the subject of future work, to determine
the stability properties of other methods in this setting.
As an instructive example, again consider the system
S1
100
⇄
100
S2
with X1(0) = X2(0) = 10,000. In this case, it is natural to take N = 10,000. As the rate constants
are 100 = √10,000, we take β1 = β2 = 1/2 and ﬁnd that γ = 1/2. The equation governing the
normalized process XN
1 is
XN
1 (t) = XN
1 (0) −Y1

N1/2N
Z t
0
XN
1 (s)ds
 1
N + Y2

N1/2N
Z t
0
(2 −XN
1 (s))ds
 1
N
where we have used that XN
1 + XN
2 ≡2. It is now clear that if the condition h < N−γ is violated
a path generated by any of the explicit methods discussed in this paper will behave quite poorly.
26


## Page 27


−2.5
−2
−1.5
−1
−0.5
−1
0
1
2
3
4
5
Log h
Log Error
 
 
Euler
Midptoint
Weak Trap
Figure 1: The log-log plot of |E[X2
3(2)] −E[Z2
3(2)]| against h for the three approximation methods.
The slope for Euler’s method is 1.21, whereas the slope for the weak trapezoidal solution with
θ = 1/2 is 3.06, which is better than expected. The curve governing the solution from the midpoint
method appears to not be linear; a behavior predicted by Theorem 5.6.
7
Examples
We provide two test systems. The ﬁrst is a simple linear system with three species that we will use
to demonstrate our main analytical results. The second is a gene-protien-mRNA model we will use
to demonstrate the capabilities of the diﬀerent methods on an actual test problem. We note that
in all simulations of the weak trapezoidal algorithm, we chose θ = 1/2.
Example 1. Consider the following ﬁrst order reaction network
A
κ1
⇄
κ2
B
κ3
⇄
κ4
C,
with κ1 = 0.03, κ2 = 1, κ3 = 0.1, and κ4 = 1. Starting from the initial state
X(0) = (XA(0), XB(0), XC(0)) = (13000, 100, 20),
where we make the obvious associations X1 = XA, X2 = XB, and X3 = XC. We approximate X(2)
using the three methods considered in this paper: Euler, midpoint, and weak trapezoidal with a
choice of θ = 1/2. For ﬁrst order systems, we may ﬁnd the ﬁrst moments and the covariances of
X(t) as solutions of linear ODEs using a Moment Generating function approach [15].
In Figure 1, we show a log-log plot of |E[X2
3(2)]−E[Z2
3(2)]| against h for the three approximation
methods. Each data point was found from either 106, 2.9 × 106, 3.9 × 106, 4.9 × 106, 8 × 106, or
107 independent simulations, with the number of simulations depending upon the size of h and
the method being used.
The slope for Euler’s method is 1.21, whereas the slope for the weak
trapezoidal solution is 3.06, which is better than expected. The curve governing the solution from
the midpoint method appears to not be linear; a behavior predicted by Theorem 5.6.
In Figure 2 we again consider the log-log plots of |E[X2
3(2)] −E[Z2
3(2)]| against h, but now only
for Euler’s method and the midpoint method so that we may see the change in behavior in the
midpoint method predicted in Theorem 5.6. In (a), we see that for larger h the slope generated via
the midpoint method is 2.03, whereas in (b) the slope is 1.12 when h is smaller. For reference, in
(a) the slope generated by Euler’s method is 1.366, whereas in (b) it is 1.09.
27


## Page 28


−1.4
−1.2
−1
−0.8
−0.6
2
2.5
3
3.5
4
4.5
5
Log h
Log Error
 
 
Euler
Midptoint
(a)
−2.6
−2.4
−2.2
−2
−1.8
−1.6
0.5
1
1.5
2
2.5
3
3.5
4
Log h
Log Error
 
 
Euler
Midptoint
(b)
Figure 2: The log-log plot of |E[X2
3(2)] −E[Z2
3(2)]| against h. The slope for generated via midpoint
tauleaping shifts from 2.03 in (a) to 1.12 in (b).
While the simulations make no use of the scalings inherent in the system, it is instructive
for us to quantify them in this example so that we are able to understand the behavior of the
midpoint method. We have N ≈104, α1 = 1, α2 = 1/2, α3 = 1/4, and mk = 1/4. Also, γ ≈0.
Therefore, Theorem 5.6 predicts the midpoint method will behave as an order two method if
h ≫N−1/4 ≈1/10, or if log(h) ≫−2.3, which roughly agrees with what is shown in Figures 1 and
2. Note that Theorem 5.6 will never provide a sharp estimate as to when the behavior will change
as it is a local result and the scalings in the system will change during the course of a simulation.
The fact that the trapezoidal method gave an order three convergence rate above does not hold
in general. This was demonstrated in the proof of Theorem 5.8, but it is helpful to also show this
via example. In Figure 3 we present a log-log plot of |EX2(2)−EZ2(2)| for the diﬀerent algorithms
on this same example. The approximate slopes are: 1.02 for Euler’s methods, 2.372 for midpoint
method, and 2.3 for the trapezoidal method. We point out that all of the plots above represent
results pertaining to the non-normalized processes as the simulation methods themselves make no
use of the scalings.
Example 2. Consider a model of gene transcription and translation:
G 25
→G + M,
M 1000
→M + P,
2P 0.001
→D,
M 0.1
→∅,
P
1→∅.
Here a single gene is being translated into mRNA, which is then being transcribed into proteins,
and ﬁnally the proteins produce stable dimers. The ﬁnal two reactions represent degradation of
mRNA and proteins, respectively. Suppose we start with one gene and no other molecules, and
want to estimate the expected number of dimers at time T = 1 to an accuracy of ± 1.0 with 95%
conﬁdence. Therefore, we want the variance of our estimator to be smaller than (1/1.96)2 = .2603.
While ϵ = 1 for the unscaled version of this problem, the simulation of just a few paths of the
system will show that there will be somewhere in the magnitude of 3,500 dimers at time T = 1.
Therefore, for the scaled system, we are asking for an accuracy of eϵ = 1/3500 ≈0.0002857. Also,
a few paths (100 is suﬃcient) shows that the order of magnitude of the variance of the normalized
number of dimers is approximately 0.11. Thus, the approximate number of exact sample paths we
will need to generate can be found by solving
1
nVar(normalized # dimers) = (eϵ/1.96)2 =⇒n = 5.18 × 106.
28


## Page 29


−2
−1.5
−1
−0.5
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
3
Log h
Log Error
 
 
Euler
Midptoint
Weak Trap
Figure 3: Log-log plot of |E[X3(2)] −E[Z3(2)]| against h for the three approximation methods.
The approximate slopes are: 1.02 for Euler’s methods, 2.372 for midpoint method, and 2.3 for the
trapezoidal method.
Approximation
# paths
CPU Time
Variance of estimator
# updates
3714.2 ± 1.0
4,740,000
149,000 CPU S
0.25995
8.27 ×1010
Table 1: Performance of Exact algorithm with crude Monte Carlo estimator (1.2).
Therefore, we will need approximately ﬁve million independent sample paths generated via an exact
algorithm. Implementing the modiﬁed next reaction method [1] on our machine (using Matlab),
each path takes approximately 0.03 CPU seconds to generate. Therefore, the approximate amount
of time to solve this particular problem will be 155,000 CPU S, which is about forty three hours.
The outcome of such a simulation is detailed in Table 1 where “# updates” refers to the total
number, over all paths, of updates to the system performed, and random variables generated,
and is used as a quantiﬁcation for the computational complexity of the diﬀerent methods under
consideration. In terms of software and hardware, the authors used Matlab for all computations,
which were performed on an Apple machine with a 2.2 GHz Intel i7 processor.
Next, we solved the problem using Euler’s method, the approximate midpoint method, and
the weak trapezoidal method with θ = 1/2. We note that for each of the three approximations,
we used the most naive implementation possible by simply setting the value of any component
that goes negative in the course of a step to zero, and by using a ﬁxed step size, h > 0. Thus,
improvements can be gained on the stated results by using a more sophisticated implementation
[2, 8]. However, we did produce our approximate paths in batches of 50,000, which greatly reduces
the cost of generating the Poisson random variables with the built in Matlab Poisson random
number generator.
In Table 2 we provide data on the performance of Euler’s method with various step-sizes,
combined with a crude Monte Carlo estimator (1.8).
Note that the bias in Euler’s method is
apparent even for very small h. In Table 3 we provide data on the performance of the midpoint
method with various step-sizes, combined with a crude Monte Carlo estimator (1.8). Note that
the solution has a much higher variance when h = 1/3, thereby necessitating signiﬁcantly more
paths to get a desired tolerance. This demonstrates the stability concerns discussed in Section 6.2.
This problem does not arise as much when using the weak trapezoidal method. In Table 4 we
provide data on the performance of the weak trapezoidal method with various step-sizes, combined
29


## Page 30


Step-size
Approximation
# paths
CPU Time
Variance of estimator
# updates
h = 3−7
3,712.3 ± 1.0
4,750,000
13,374.6 CPU S
0.25898
6.2 × 1010
h = 3−6
3,707.5 ± 1.0
4,750,000
6,207.9 CPU S
0.25839
2.1 × 1010
h = 3−5
3,693.4 ± 1.0
4,700,000
2,803.9 CPU S
0.26018
6.9 × 109
h = 3−4
3,654.6 ± 1.0
4,650,000
1,219 CPU S
0.25940
2.6 × 109
Table 2: Performance of Euler’s method with crude Monte Carlo.
Step-size
Approximation
# paths
CPU Time
Variance of estimator
# updates
h = 3−4
3,713.6 ± 1.0
4,650,000
1,269.1 CPU S
0.25996
2.3 × 109
h = 3−3
3,713.9 ± 1.0
4,500,000
497.5 CPU S
0.25860
7.6 × 108
h = 3−2
3,722.4 ± 1.0
4,050,000
177.6 CPU S
0.25972
2.2 × 108
h = 3−1
3,986.1 ± 1.0
18,500,000
376.0 CPU S
0.26020
3.3 × 108
Table 3: Performance of midpoint method with crude Monte Carlo.
with a crude Monte Carlo estimator (1.8). We see that for this example the midpoint method
and the weak trapezoidal method are, overall, comparable. However, the weak trapezoidal method
performs, in terms of bias and required CPU time, signiﬁcantly better than does the midpoint
method for h = 1/3.
It is worth noting that both the midpoint and weak trapezoidal methods compare decently on
this example with the multi-level Monte Carlo method developed recently for stochastic chemical
kinetic systems [4]. The choice of which method (an explicit solver discussed herein or a multi-level
Monte Carlo solver) a user wishes to implement will therefore often be problem, and user, speciﬁc.
We next used each of the methods above to estimate the probability that the number of dimers
at time 1 is greater than or equal to 6,000.
Note that this probability is the expected value
of the indicator function 1{XDimer(1)≥6,000}. The results are presented in Table 5, which provides
95% conﬁdence intervals for a few choices of h for each method.
Note that in computing this
approximation the weak trapezoidal method has signiﬁcantly less bias than does the midpoint
method for comparable step-sizes, making it the method of choice for this particular choice of
function f. The necessary CPU time for each of the methods is the same as those reported above.
References
[1] David F. Anderson, A modiﬁed next reaction method for simulating chemical systems with time
dependent propensities and delays, J. Chem. Phys. 127 (2007), no. 21, 214107.
[2]
, Incorporating postleap checks in tau-leaping, J. Chem. Phys. 128 (2008), no. 5, 054103.
Step-size
Approximation
# paths
CPU Time
Variance of estimator
# updates
h = 3−4
3,714.4 ± 1.0
4,750,000
2,120.5 CPU S
0.25940
4.6 × 109
h = 3−3
3,714.6 ± 1.0
4,750,000
898.2 CPU S
0.25940
1.6 × 109
h = 3−2
3,725.6 ± 1.0
4,800,000
349.8 CPU S
0.25965
5.2 × 108
h = 3−1
3,673.3 ± 1.0
8,850,000
238.2 CPU S
0.25944
3.2 × 108
Table 4: Performance of weak trapezoidal method with θ = 1/2, with crude Monte Carlo.
30


## Page 31


Method
Step-size
# paths
Approximation
Exact
N.A.
4,520,000
0.02843 ± 0.00015
Euler
h = 3−7
4,750,000
0.02818 ± 0.00015
Euler
h = 3−6
4,750,000
0.02782 ± 0.00015
Midpoint
h = 3−4
4,650,000
0.02718 ± 0.00015
Midpoint
h = 3−3
4,500,000
0.02537 ± 0.00015
Weak Trap, θ = 1/2
h = 3−4
4,750,000
0.02840 ± 0.00015
Weak Trap, θ = 1/2
h = 3−3
4,750,000
0.02838 ± 0.00015
Weak Trap, θ = 1/2
h = 3−2
4,800,000
0.02946 ± 0.00015
.
Table 5: Approximation of P{XDimer(1) ≥6, 000} using diﬀerent methods and diﬀerent step sizes.
As expected, the weak trapezoidal method demonstrates signiﬁcantly less bias than do the Euler
and midpoint methods.
[3] David F. Anderson, Arnab Ganguly, and Thomas G. Kurtz, Error analysis of tau-leap simu-
lation methods, Annals of Applied Probability 21 (2011), no. 6, 2226 – 2262.
[4] David F. Anderson and Desmond J. Higham, Multi-level Monte Carlo for stochastically modeled
chemical kinetic systems, to appear in SIAM: Multiscale Modeling and Simulation Available
on arxiv.org at arxiv.org:1107.2181.
[5] David F. Anderson and Thomas G. Kurtz, Continuous time markov chain models for chemical
reaction networks, Design and Analysis of Biomolecular Circuits: Engineering Approaches to
Systems and Synthetic Biology (H. Koeppl et al., ed.), Springer, 2011, pp. 3–42.
[6] David F. Anderson and Jonathan C. Mattingly, A weak trapezoidal method for a class of
stochastic diﬀerential equations, Comm. Math. Sci. 9 (2011), no. 1, 301 – 318.
[7] Karen Ball, Thomas G. Kurtz, Lea Popovic, and Greg Rempala, Asymptotic analysis of mul-
tiscale approximations to reaction networks, Ann. Appl. Prob. 16 (2006), no. 4, 1925–1961.
[8] Yang Cao, Daniel T. Gillespie, and Linda R. Petzold, Avoiding negative populations in explicit
poisson tau-leaping, J. Chem. Phys. 123 (2005), 054104.
[9]
, The slow-scale stochastic simulation aglorithm, J. Chem. Phys. 122 (2005), 014116.
[10]
, Eﬃcient step size selection for the tau-leaping simulation method, J. Chem. Phys. 124
(2006), 044109.
[11] Yang Cao and Linda R. Petzold, Trapezoidal tau-leaping formula for the stochastic simula-
tion of biochemical systems, proceedings of the FOSBE 2005, University of California Santa
Barbara, 2005.
[12] Abhijit Chatterjee and Dionisios G. Vlachos, Binomial distribution based τ-leap accelerated
stochastic simulation, J. Chem. Phys. 122 (2005), 024112.
[13] Weinan E, Di Liu, and Eric Vanden-Eijnden, Nested stochastic simulation algorithm for chem-
ical kinetic systems with disparate rates, J. Chem. Phys. 123 (2005), 194107.
[14] Stewart N. Ethier and Thomas G. Kurtz, Markov processes: Characterization and convergence,
John Wiley & Sons, New York, 1986.
31


## Page 32


[15] Chetan Gadgil, Chang Hyeong Lee, and Hans G. Othmer, A stochastic analysis of ﬁrst-order
reaction networks, Bull. Math. Bio. 67 (2005), 901–946.
[16] M.A. Gibson and J. Bruck, Eﬃcient exact stochastic simulation of chemical systems with many
species and many channels, J. Phys. Chem. A 105 (2000), 1876–1889.
[17] D. T. Gillespie, A general method for numerically simulating the stochastic time evolution of
coupled chemical reactions, J. Comput. Phys. 22 (1976), 403–434.
[18]
, Exact stochastic simulation of coupled chemical reactions, J. Phys. Chem. 81 (1977),
no. 25, 2340–2361.
[19]
, Approximate accelerated simulation of chemically reaction systems, J. Chem. Phys.
115 (2001), no. 4, 1716–1733.
[20] D. T. Gillespie and Linda R. Petzold, Improved leap-size selection for accelerated stochastic
simulation, J. Chem. Phys. 119 (2003), no. 16, 8229–8234.
[21] Peter W. Glynn, A GSMP formalism for discrete event systems, Proc. IEEE 77 (1989), no. 1,
14–23.
[22] Yucheng Hu, Tiejun Li, and Bin Min, The weak convergence analysis of tau-leaping methods:
revisited, Communications in Mathematical Sciences 9 (2011), no. 4, 965 – 996.
[23]
, A weak second order tau-leaping scheme for simulating chemical reaction systems,
Journal of Chemical Physics 135 (2011), 024113.
[24] Martin Hutzenthaler and Arnulf Jentzen, Convergence of the stochastic Euler scheme for locally
Lipschitz coeﬃcients, Foundations of Computational Mathematics 11 (2011), no. 6, 657 – 706.
[25] Hye-Won Kang and Thomas G. Kurtz, Separation of time-scales and model reduction for
stochastic reaction networks, to appear in Annals of Applied Probability.
[26] Peter E. Kloeden and Eckhard Platen, Numerical solution of stochastic diﬀerential equa-
tions, Applications of Mathematics (New York), vol. 23, Springer-Verlag, Berlin, 1992. MR
MR1214374 (94b:60069)
[27] Thomas G. Kurtz, Approximation of population processes, CBMS-NSF Reg. Conf. Series in
Appl. Math.: 36, SIAM, 1981.
[28] H. Lambda, Jonathan C. Mattingly, and Andrew M. Stuart, An adaptive Euler-Maruyama
scheme for SDEs: convergence and stability, IMA Journal of Numerical Analysis 27 (2007),
no. 3, 479–506.
32

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
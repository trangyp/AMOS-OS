---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0909.4790v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0909.4790v3_Error_analysis_of_tau-leap_simulation_methods

> Source: 0909.4790v3_Error_analysis_of_tau-leap_simulation_methods.pdf

> Pages: 38

---


## Page 1


arXiv:0909.4790v3  [math.PR]  14 Feb 2012
The Annals of Applied Probability
2011, Vol. 21, No. 6, 2226–2262
DOI: 10.1214/10-AAP756
c
⃝Institute of Mathematical Statistics, 2011
ERROR ANALYSIS OF TAU-LEAP SIMULATION METHODS
By David F. Anderson1, Arnab Ganguly2 and Thomas G. Kurtz2
University of Wisconsin, Madison
We perform an error analysis for numerical approximation meth-
ods of continuous time Markov chain models commonly found in the
chemistry and biochemistry literature. The motivation for the anal-
ysis is to be able to compare the accuracy of diﬀerent approxima-
tion methods and, speciﬁcally, Euler tau-leaping and midpoint tau-
leaping. We perform our analysis under a scaling in which the size of
the time discretization is inversely proportional to some (bounded)
power of the norm of the state of the system. We argue that this is
a more appropriate scaling than that found in previous error analyses
in which the size of the time discretization goes to zero independent
of the rest of the model. Under the present scaling, we show that
midpoint tau-leaping achieves a higher order of accuracy, in both
a weak and a strong sense, than Euler tau-leaping; a result that is in
contrast to previous analyses. We present examples that demonstrate
our ﬁndings.
1. Introduction.
This paper provides an error analysis for numerical ap-
proximation methods for continuous time Markov chain models that are
becoming increasingly common in the chemistry and biochemistry litera-
ture. Our goals of the paper are two-fold. First, we want to demonstrate the
importance of considering appropriate scalings in which to carry out error
analyses for the methods of interest. Second, we wish to provide such an er-
ror analysis in order to compare the accuracy of two diﬀerent approximation
methods. We perform our analysis on the Euler tau-leaping method ﬁrst pre-
sented in [11] and a midpoint tau-leaping method developed below, which
is only a slight variant of one presented in [11]. The midpoint tau-leaping
method will be demonstrated to be more accurate than Euler tau-leaping in
Received September 2009; revised July 2010.
1Supported by NSF Grants DMS-05-53687 and DMS-10-09275.
2Supported by NSF Grant DMS-05-53687.
AMS 2000 subject classiﬁcations. Primary 60H35, 65C99; secondary 92C40.
Key words and phrases. Tau-leaping, simulation, error analysis, reaction networks,
Markov chain, chemical master equation.
This is an electronic reprint of the original article published by the
Institute of Mathematical Statistics in The Annals of Applied Probability,
2011, Vol. 21, No. 6, 2226–2262. This reprint diﬀers from the original in
pagination and typographic detail.
1


## Page 2


2
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
both a strong and a weak sense, a result that is in contrast to previous error
analyses. We will discuss why previous error analyses made diﬀering predic-
tions than does ours and argue that the scaling provided here, or variants
thereof, is a more natural and appropriate choice for error analyses of such
methods. We also provide examples that demonstrate our ﬁndings.
1.1. The basic model.
The motivation for the class of mathematical mod-
els under consideration comes from chemistry and biochemistry, and more
generally from population processes (though we choose the language of
chemistry throughout the paper). We assume the existence of a chemical
reaction system consisting of (i) d chemical species {S1,S2,...,Sd} and (ii)
a ﬁnite set of possible reactions, which we index by k. Each reaction re-
quires some number of the species as inputs and provides some number of
the species as outputs. For example, the reaction S1 →2S2 would require
one molecule of S1 for the input and provide two molecules of S2 for the out-
put. If reaction k occurs at time t, then the state of the system X(t) ∈Zd
≥0
is updated via addition of the reaction vector νk ∈Zd, which represents the
net change in the abundances of the underlying species:
X(t) = X(t−) + νk.
Returning brieﬂy to the example S1 →2S2, the associated reaction vector for
this reaction would be [−1,2,0,... ,0]T . Finally, we denote by νs
k the vector
in Zd
≥0 representing the source of the kth reaction. Returning again to the
example S1 →2S2, the source vector for this reaction is νs
k = [1,0,...,0]T .
We assume that the waiting times for the k reactions are exponentially
distributed with intensity functions λk :Rd
≥0 →R≥0. We extend each λk to
all of Rd by setting it to zero outside Rd
≥0. This model is a continuous time
Markov chain in Zd
≥0 with generator
(Af)(x) =
X
k
λk(x)(f(x + νk) −f(x)),
(1.1)
where f :Zd →R is arbitrary. Kolmogorov’s forward equation for this model,
termed the “chemical master equation” in the chemistry and biology litera-
ture, is
d
dtP(x,t|π) =
X
k
P(x −νk,t|π)λk(x −νk) −
X
k
P(x,t|π)λk(x),
where for x ∈Zd
≥0 P(x,t|π) represents the probability that X(t) = x, con-
ditioned upon the initial distribution π. One representation for path-wise
solutions to this model uses a random time change of Poisson processes,
X(t) = X(0) +
X
k
Yk
Z t
0
λk(X(s))ds

νk,
(1.2)


## Page 3


ERROR ANALYSIS OF TAU-LEAP METHODS
3
where the Yk are independent, unit-rate Poisson processes (see, e.g., [16]).
Note that ˜X(t) def
= X(t)−P
k
R t
0 λk(X(s))dsνk is a martingale with quadratic
covariation matrix [X]t = P
k Yk(
R t
0 λk(X(s))ds)νkνT
k .
A common choice of intensity function for chemical reaction systems, and
the one we adopt throughout, is mass action kinetics. Under mass action
kinetics, the intensity function for the kth reaction is
λk(x) = ˜ck

x
x −νs
k

=
˜ck
Qd
ℓ=1 νs
kℓ!
d
Y
ℓ=1
xℓ!
(xℓ−νs
kℓ)!1{xℓ≥0}
(1.3)
def
= ck
d
Y
ℓ=1
xℓ!
(xℓ−νs
kℓ)!1{xℓ≥0},
where ˜ck is a positive constant and ck is deﬁned by the above equation. Mass
action kinetics arises by thinking of ˜ck∆t as the approximate probability
that a particular set of the molecules needed in the kth reaction will react
over a time-period of size ∆t, and then counting the number of ways such
a reaction could happen. Implicit in the assumption of mass action kinetics
is that the vessel under consideration is “well stirred.” For ease of notation,
we will henceforth drop the indicator functions from our representation of
mass action kinetics. More general rates will be discussed in the remark at
the top of page six.
1.2. Numerical methods.
There are a number of numerical methods that
produce statistically exact sample paths for the model described above.
These include the stochastic simulation algorithm, better known as Gille-
spie’s algorithm [9, 10], the ﬁrst reaction method [9] and the next reaction
method [1, 8]. All such algorithms perform the same two basic steps multiple
times until a sample path is produced over a desired time interval: ﬁrst, con-
ditioned on the current state of the system the amount of time that passes
until the next reaction takes place, ∆, is computed and second the speciﬁc
reaction that has taken place is found. If, however, P
k λk(X(t)) ≫0 then
∆≈(P
k λk(X(t)))−1 ≪1 and the time needed to produce a single exact
sample path over a time interval can be prohibitive.
The approximate algorithm “tau-leaping” was developed by Dan Gillespie
in [11] in an eﬀort to overcome the problem that ∆may be prohibitively
small. The basic idea of tau-leaping is to hold the intensity functions ﬁxed
over the time interval [tn,tn +h] at the values λk(X(tn)), where X(tn) is the
current state of the system, and, under this assumption, compute the number
of times each reaction takes place over this period. As the waiting times
for the reactions are exponentially distributed, this leads to the following
algorithm.


## Page 4


4
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
Algorithm 1 (Euler tau-leaping).
Set Z(0) = X(0), t0 = 0, n = 0 and
repeat the following until tn+1 > T.
(1) Set Z(tn+1) = Z(tn) + P
k Pk,n(λk(Z(tn))h)νk, set tn+1 = tn + h and
set n = n+1, where Pk,n(x) are independent Poisson random variables with
parameters x.
Several improvements and modiﬁcations have been made to the basic algo-
rithm described above over the years. However, they are mainly concerned
with how to choose the step-size adaptively [4, 12] and/or how to ensure
that population values do not go negative during the course of a simulation
[2, 3, 5], and are not explicitly relevant to the current discussion.
Similar to (1.2), a path-wise representation of Euler tau-leaping can be
given through a random time change of Poisson processes,
Z(t) = X(0) +
X
k
Yk
Z t
0
λk(Z ◦η(s)) ds

νk,
(1.4)
where η(s) = tn if tn ≤s < tn+1 and the Yk are as before. Noting that
R tn+1
0
λk(Z ◦η(s))ds = Pn
i=0 λk(Z(ti))(ti+1 −ti) explains our choice to call
this method “Euler tau-leaping.” Deﬁning the operator
(Bzf)(x) =
X
k
λk(z)(f(x + νk) −f(x)),
(1.5)
we see that for t > 0
Ef(Z(t)) = Ef(Z ◦η(t)) + E
Z t
η(t)
(BZ◦η(t)f)(Z(s))ds,
(1.6)
so long as the expectations exist. Further, we note that ˜Z(t) def
= Z(t) −
P
k
R t
0 λk(Z ◦η(s))dsνk is a martingale with quadratic covariation matrix
[ ˜Z]t =
X
k
Yk
Z t
0
λk(Z ◦η(s))ds

νkνT
k .
It is natural to believe that a midpoint type method would be more ac-
curate than an Euler type method in many situations. We therefore deﬁne
the function
ρ(z) def
= z + 1
2h
X
k
λk(z)νk,
which computes an approximate midpoint for the system assuming the state
of the system is z and the time-step is h.
Algorithm 2 (Midpoint tau-leaping).
Set Z(0) = X(0), t0 = 0, n = 0
and repeat the following until tn+1 > T.


## Page 5


ERROR ANALYSIS OF TAU-LEAP METHODS
5
(1) Set Z(tn+1) = Z(tn) + P
k Pk,n(λk ◦ρ ◦Z(tn)h)νk, set tn+1 = tn + h
and set n = n + 1, where Pk,n(x) are independent Poisson random variables
with parameters x.
Similar to (1.2) and (1.4), Z(t) can be represented via a random time
change of Poisson processes:
Z(t) = X(0) +
X
k
Yk
Z t
0
λk ◦ρ ◦Z ◦η(s)ds

νk,
where η(·) is as before. For Bz deﬁned via (1.5) and any 0 < t and any
function f
Ef(Z(t)) = Ef(Z ◦η(t)) + E
Z t
η(t)
(Bρ◦Z◦η(t)f)(Z(s))ds.
(1.7)
Finally,
˜Z(t) def
= Z(t) −P
k
R t
0 λk ◦ρ ◦Z ◦η(s)dsνk is a martingale with
quadratic covariation matrix [ ˜Z]t = P
k Yk(
R t
0 λk ◦ρ ◦Z ◦η(s)ds)νkνT
k . The
main goal of this paper is to show that the midpoint tau-leaping algorithm
is indeed more accurate than the Euler tau-leaping method under an appro-
priate, and natural, scaling described in Section 2.
Remark.
Historically, the time discretization parameter for tau-leaping
has been τ, thus giving the method its name. We choose to break from
this tradition and denote our time-step by h so as not to confuse τ with
a stopping time.
1.3. Previous error analyses.
Under the scaling h →0, Rathinam et
al. [18] performed a consistency check of Euler tau-leaping and found that
the local truncation error was O(h2) for all moments. They also showed that
under this same scaling Euler tau-leaping is ﬁrst order accurate in a weak
sense in the special case that the intensity functions λk are linear [18]. Li ex-
tended these results by showing that as h →0 Euler tau-leaping has a strong
error (in the L2 norm) of order 1/2 and a weak error of order one [17], which
agree with classical results pertaining to numerical analysis of SDEs driven
by Brownian motions (see, e.g., [13]).
Under the scaling h →0, it is readily seen that midpoint tau-leaping is
no more accurate than Euler tau-leaping. This follows since midpoint tau-
leaping consists of making an O(h2) correction to the intensity functions
used in Euler tau-leaping. As h →0, this correction becomes negligible as
Poisson processes “ignore” O(h2) corrections, and the accuracy of the two
methods will be the same.
We simply note that while the analyses performed in [18] and [17] and the
argument made in the previous paragraph are technically correct, performing


## Page 6


6
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
an analysis as h →0, independent of the rest of the model, is at odds with
the useful regime of tau-leaping. That is, tau-leaping would only be used in
a regime where h ≫∆, where ∆is the expected amount of time between
reactions, for otherwise an exact method would be performed. Therefore, we
should require that
h ≫
X
k
λk(Z(t))
−1
or
h
X
k
λk(Z(t)) ≫1,
(1.8)
where Z(t) is the state of the system. In Section 2, we will present a natural
scaling for the models under consideration that does satisfy (1.8) and under
which we will perform our analysis.
1.4. Paper outline.
The remainder of the paper is organized as follows.
In Section 2, we give some natural assumptions on the models considered
in this paper and introduce the scaling under which we perform our analy-
sis. In Section 3, we perform a strong error analysis for both the Euler and
midpoint tau-leaping methods and show that midpoint tau-leaping is the
more accurate of the two under our scaling. In Section 4, we perform a weak
error analysis of the diﬀerent methods and again conclude that the mid-
point method is more accurate. In Section 5, we present numerical examples
demonstrating our results.
2. Assumptions on the model.
2.1. Scalings of the model and the algorithms.
As discussed in the Intro-
duction, tau-leaping methods will only be of use if the time-discretization pa-
rameter h satisﬁes hP
k λk(Z(t)) ≫1 while (P
k λk(Z(t)))−1 ≪1, where Z(t)
is the state of the system at time t. There are a number of ways for the sec-
ond condition to hold and a modeling choice must be made. We make the
following natural assumptions:
(i) The initial abundance of each species scales with V for some V ≫1.
(ii) Each rate constant satisﬁes cV
k = O(V 1−νs
k·⃗1), where ⃗1 = [1,1,...,1]T .
In particular, cV
k = dk/V 1−νs
k·⃗1 for some dk > 0.
We will denote by XV the normalized process deﬁned as the vector of abun-
dances divided by V , and will denote by λV
k the intensity function deﬁned to
be mass action kinetics with rate constants cV
k . This scaling is the so called
“classical scaling” and arises naturally by thinking of V as the volume of the
vessel in which the reactions are taking place multiplied by Avogadro’s num-
ber [14]. In this case, XV gives the concentration of each species in moles per
unit volume. To understand the scaling for the rate constants, consider the
case of a reaction requiring as input two constituent molecules: S1 and S2.


## Page 7


ERROR ANALYSIS OF TAU-LEAP METHODS
7
Perhaps S1 + S2 →S3. It is reasonable to assume that the probability that
a particular pair of S1 and S2 molecules meet, and react, in a small time
interval is inversely proportional to the volume of the vessel. This same type
of logic holds for the cases in which more than two molecules are needed for
a reaction to take place (i.e., the probability that three particular molecules
meet and react is inversely proportional to the volume squared). For the case
that only one molecule is needed for a reaction to take place, it is reasonable
to assume that the probability of such a reaction taking place in the next
small interval of time for a particular molecule should not scale with the
volume. See also [19], Chapter 6.
Models that satisfy assumptions (i) and (ii) above have an important
property that we will detail here and make use of later. Let x(t) denote the
solution to the deterministic initial value problem
˙x(t) = F(x(t)) def
=
X
k
dkx(t)νs
kνk,
x(0) = x0 ∈Rd
≥0,
(2.1)
where dk is deﬁned in assumption (ii) above, and where for any two vectors
uv def
= uv1
1 ···uvd
d and we adopt the convention that 00 = 1. That is, x(t) is the
solution to the corresponding deterministically modeled chemical reaction
system with mass action kinetics. It was shown in [14, 15] that for any ε > 0
and any T > 0, if XV (0) = x(0) = x0, then
lim
V →∞P
n
sup
t∈[0,T]
|XV (t) −x(t)| ≥ε
o
→0.
(2.2)
Denoting λk as deterministic mass action kinetics with rate constant dk,
it is an exercise to check that for any reaction, that is, zeroth order, ﬁrst
order, second order, etc., and any x ∈Rd
≥0
λV
k (V x) = V λk(x) + ζV
k (x),
where ζV
k is uniformly bounded in V and is nonzero only if the reaction
requires more than one molecule of a particular species as an input. For
example, for the second order reaction S1 + S2 →S3 we have
λV
k (V x) = dk
V (V x1)(V x2) = V dkx1x2 = V λk(x),
whereas for the second order reaction 2S1 →S3 we have
λV
k (V x) = dk
V V x1(V x1 −1) = V dkx2
1 −dkx1 = V λk(x) + ζV
k (x)
with ζV
k (x) = −dkx1. The term ζV
k will have a true V dependence if three or
more molecules of a particular species are required as input. We now state
the deﬁnition AV
k (x) def
= 1
V λV
k (V x), and note that for all x ∈Rd
≥0
AV
k (x) = λk(x) + 1
V ζV
k (x)
(2.3)


## Page 8


8
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
and AV
k (x) ≡0 if x /∈Rd
≥0. Manipulating the deﬁnition of AV
k shows that for
all x ∈Rd
λV
k (V x) = V AV
k (x).
(2.4)
Remark.
The assumption of mass action kinetics is not critical to the
analysis carried out in this paper. Instead, what is critical to this particular
analysis is that our kinetics satisﬁes the scaling (2.4) for AV
k satisfying (2.3)
with λk suﬃciently smooth.
We now choose a discretization parameter for the approximate methods
that is dependent upon the assumptions of the model set out above. We let
hV def
= 1/V β,
(2.5)
where 0 < β < 1. We note that this scaling satisﬁes the necessary require-
ments detailed above as
X
k
λV
k (V x)
−1
= O(V −1) ≪1,
V −β
X
k
λV
k (V x)

= O(V 1−β) ≫1.
With this choice of time-step, we let ZV and ZV denote the processes gen-
erated by Euler and midpoint tau-leaping, respectively, normalized by V . We
can now state more clearly what the analysis of this paper will entail. We
will consider the case of V ≫0 by letting V →∞and consider the relation-
ship of the normalized approximate processes ZV and ZV to the original
process XV , normalized similarly. Note that all three processes converge to
the solution of (2.1). We will perform both weak and strong error analyses.
In the strong error analysis, we will consider L1 convergence as opposed to
the more standard (at least for systems driven by Brownian motions) L2
convergence. The reason for this is simple: the Itˆo isometry makes work-
ing with the L2-norm easier in the Brownian motion case, whereas Poisson
processes lend themselves naturally to analysis in the L1-norm.
We remark that it is clear that the choice of scaling laid out in this sec-
tion and assumed throughout the paper will not explicitly cover all cases
of interest. For example, one may choose to use approximation methods
when (i) the abundances of only a strict subset of the constituent species
are in an O(V ) scaling regime, or (ii) it is the rate constants themselves
that are O(V ) while the abundances are O(1), or (iii) there is a mixture of
the previous two cases with potentially more than two natural scales in the
system. Our analysis will not be directly applicable to such cases. However,


## Page 9


ERROR ANALYSIS OF TAU-LEAP METHODS
9
the purpose of this analysis is not to handle every conceivable case. Instead,
our purpose is to try and give a more accurate picture of how diﬀerent tau-
leaping methods approximate the exact solution, both strongly and weakly,
in at least one plausible setting and we believe that the analysis detailed
in this paper achieves this aim. Further, we believe that error analyses con-
ducted under diﬀerent modeling assumptions can be carried out in similar
fashion.
2.2. Redeﬁning the kinetics.
Before proceeding to the analysis, we allow
ourselves one change to the model detailed in the previous section. As we
will be considering approximation methods in which changes to the state of
the system are determined by Poisson random variables (which can produce
arbitrarily large values), there will always be a positive probability that solu-
tions will leave a region in which the scaling detailed above is valid. Multiple
options are available to handle such a situation. One option would be to de-
ﬁne a stopping time for when the process leaves a predetermined region in
which the scaling regime is valid and then only perform the analysis up to
that stopping time. Another option, and the one we choose, is to simply mod-
ify the kinetics by multiplying by a cutoﬀfunction that makes the intensity
functions zero outside such a region. This has the added beneﬁt of guar-
anteeing the existence of all moments of the processes involved. Note that
without this truncation or some other additional assumption guaranteeing
the existence of the necessary moments, some of the moment estimates that
follow may fail; however, the convergence in probability and convergence in
distribution results in Theorems 3.10 and 3.17 would still be valid.
Let γ ≥0 be C∞with compact support Ωγ ⊂Rd
>0, with γ(x) = 1 for all
x ∈Br(x(t)) for some r > 0, where x(t) satisﬁes (2.1). Now, we redeﬁne our
intensity functions by setting
λV
k (x) = γ(x/V )cV
k
d
Y
ℓ=1
xℓ!
(xℓ−νs
kℓ)!
for x ∈Rd,
(2.6)
where cV
k still satisﬁes the scaling detailed in the previous section. It is easy
to check that the redeﬁned kinetics still satisﬁes λV
k (V x) = V AV
k (x), where
now AV
k (x) has also been redeﬁned by multiplication by γ(x). Further, the
redeﬁned λV
k is identical to the previous function on the domain of interest
to us. That is, they only diﬀer if the process leaves the scaling regime of
interest. For the remainder of the paper, we assume our intensity functions
are given by (2.6). Finally, we note that for each k we have the existence of
an Lk > 0 such that
sup
x∈Rd,|α|<∞
|DαAV
k (x)| ≤Lk.
(2.7)


## Page 10


10
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
3. Strong error analysis for Euler and midpoint tau-leaping.
Through-
out this section, we assume a time discretization 0 = t0 < t1 < ··· < tN = T
with tn −tn−1 = hV = V −β for some 0 < β < 1. In Section 3.1 we give some
necessary technical results. In Section 3.2 we give bounds for supt≤T E|XV (t)−
ZV (t)| and supt≤T E|XV (t) −ZV (t)| in terms of V , where XV (t),ZV (t)
and ZV (t) are the normalized processes and satisfy the representations
XV (t) = XV (0) + 1
V
X
k
Yk

V
Z t
0
AV
k (XV (s))ds

νk,
(3.1)
ZV (t) = XV (0) + 1
V
X
k
Yk

V
Z t
0
AV
k (ZV ◦η(s)) ds

νk,
(3.2)
ZV (t) = XV (0) + 1
V
X
k
Yk

V
Z t
0
AV
k ◦ρV ◦ZV ◦η(s)ds

νk,
(3.3)
where
ρV (z) def
= z + 1
2V −β X
k
AV
k (z)νk
and η(s) = tn for s ∈[tn,tn+1). In Sections 3.3 and 3.4, we use diﬀerent
couplings of the processes than those above to provide the exact asymptotics
of the error processes XV −ZV and XV −ZV .
3.1. Preliminaries.
We present some technical, preliminary concepts that
will be used ubiquitously throughout the section. For a more thorough refer-
ence of the material presented here, see [6], Chapter 6. We begin by deﬁning
the following ﬁltrations that are generated by the Poisson processes Yk:
F˜u
def
= σ{Yk(sk):sk ≤uk},
Fi
u
def
= σ{Yk(r),Yi(s):k ̸= i,s ≤u,r ∈[0,∞)},
where ˜u is a multi-index and u is a scalar.
Lemma 3.1.
Suppose that X(t) satisﬁes (1.2) with nonnegative intensity
functions λk. For t ≥0 and a choice of k,
τk(t) =
Z t
0
λk(X(s))ds
(3.4)
is an {Fk
u}-stopping time.
Proof.
For u ≥0, let α(u) satisfy
Z α(u)
0
λk(X(s))ds = u,


## Page 11


ERROR ANALYSIS OF TAU-LEAP METHODS
11
where we take α(u) = ∞if
R ∞
0 λk(X(s))ds < u. Then α(u) is adapted to Fk
u
and {τk(t) ≤u} = {t ≤α(u)} ∈Fk
u.
□
Therefore, if the processes X(t) and Z(t) satisfy (1.2) with nonnegative
intensity functions λk,1 and λk,2, respectively, then for t,s ≥0 and a choice
of k,
E
Yk
Z t
0
λk,1(X(r))dr

−Yk
Z s
0
λk,2(Z(r))dr

(3.5)
= E

Z t
0
λk,1(X(r))dr −
Z s
0
λk,2(Z(r))dr
,
because (i) both the maximum and minimum of two stopping times are
stopping times, and (ii) Yk is monotone.
Similarly to above, one can show that τ(t) def
= (τ1(t),τ2(t),...), where τk(t)
is as in (3.4), is a multi-parameter {F˜u}-stopping time. We now deﬁne the
ﬁltration
Gt
def
= Fτ(t)
and note that by the conditions of Section 2.2 the centered process
˜Yk
Z t
0
λk(X(s))ds

def
= Yk
Z t
0
λk(X(s))ds

−
Z t
0
λk(X(s))ds
(3.6)
is a square integrable martingale, with respect to Gt, with quadratic variation
Yk(
R t
0 λk(X(s))ds). This fact will be used repeatedly throughout the paper.
3.2. Bounds on the strong error.
The following theorems give bounds on
the errors supt≤T E|XV (t) −ZV (t)| and supt≤T E|XV (t) −ZV (t)|.
Theorem 3.2.
Let XV (t) and ZV (t) satisfy (3.1) and (3.2), respec-
tively, for t ≤T. Then there exists a constant C = C(T) > 0 such that
sup
t≤T
E|XV (t) −ZV (t)| ≤CV −β = ChV .
Proof.
For t ∈[0,T], deﬁne E(t) def
= E|XV (t) −ZV (t)|. Using (3.5)
and (2.7),
E(t) ≤
X
k
|νk|Lk

E
Z t
0
|XV (s) −ZV ◦η(s)|ds
≤
X
k
|νk|Lk
Z t
0
E(s)ds +
X
k
|νk|Lk

E
Z t
0
|ZV (s) −ZV ◦η(s)|ds.


## Page 12


12
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
The second term on the right above can be bounded similarly,
E
Z t
0
|ZV (s) −ZV ◦η(s)|ds ≤
X
k
|νk|Lk

tV −β,
and the result holds via Gronwall’s inequality.
□
Theorem 3.3.
Let XV (t) and ZV (t) satisfy (3.1) and (3.3), respec-
tively, for t ≤T. Then there exists a constant C = C(T) > 0 such that
sup
t≤T
E|XV (t) −ZV (t)| ≤CV −κ(β)
where κ(β) = min
1 + β
2
,2β

.
Before proving Theorem 3.3, we present some preliminary material. Let
F V (x) def
= P
k AV
k (x)νk and deﬁne
U V,1(s) def
= ZV (s)−ρV ◦ZV ◦η(s) = ZV (s)−ZV ◦η(s)−1
2V −βF V (ZV ◦η(s))
and
˜U V,1(s) def
= (s −η(s) −1
2V −β)F V (ZV ◦η(s)).
Then
U V,1(s) −˜U V,1(s)
= ˜ZV (s) −˜ZV ◦η(s)
(3.7)
+ (s −η(s))(F V (ρV ◦ZV ◦η(s)) −F V (ZV ◦η(s))),
where ˜ZV (t) def
= ZV (t) −
R t
0 F V (ρV ◦ZV ◦η(s))ds is a martingale.
Lemma 3.4.
For all 0 < β < 1, there exists a C > 0 such that
sup
s≤∞
E|U V,1(s) −˜U V,1(s)| ≤CV −κ(β).
Proof.
Clearly, the third term on the right-hand side of (3.7) is O(V −2β)
uniformly in s. Thus,
E|U V,1(s) −˜U V,1(s)| ≤E| ˜ZV (s) −˜ZV ◦η(s)| + c1V −2β
≤
 1
V
X
k
|νk|2E
Z s
η(s)
AV
k (ρV ◦ZV ◦η(r))dr
1/2
+ c1V −2β
≤c2V −(1+β)/2 + c1V −2β
for constants c1 and c2 which do not depend upon s.
□
Lemma 3.5.
For all 0 < β < 1 and 0 < t, and for α ∈{2,3,4,...}
lim
V →∞V αβ sup
s≤t
E[|U V,1(s) −˜U V,1(s)|α] = 0.


## Page 13


ERROR ANALYSIS OF TAU-LEAP METHODS
13
Proof.
The third term on the right-hand side of (3.7) is O(V −2β), so
E|U V,1(s) −˜U V,1(s)|2 ≤C(E| ˜ZV (s) −˜ZV ◦η(s)|2 + V −4β)
≤C
V
X
k
|νk|2E
Z s
η(s)
AV
k (ρV ◦ZV ◦η(r)) dr + CV −4β
= O(V −((1+β)∧4β))
showing the α = 2 case.
It is simple to show that V αβ sups≤t E[|U V,1(s) −˜U V,1(s)|α] is uniformly
bounded in V for any α ∈Z≥0. The α = 2 case then gives the necessary
bounds for the arbitrary α case.
□
Note that by Lemmas 3.4 and 3.5
AV
k (ZV (s)) −AV
k (ρV ◦ZV ◦η(s))
= ∇AV
k (ρV ◦ZV ◦η(s)) · U V,1(s) + O(V −2β)
(3.8)
= ∇AV
k (ρV ◦ZV ◦η(s)) · ˜U V,1(s) + O(V −κ(β)).
We ﬁnally note that for any bounded function g and any n ≥0
Z tn+1
tn
g(η(s)) ˜U V,1(s)ds = 0
and so for any t > 0
Z t
0
g(η(s)) ˜U V,1(s)ds
= 1
8((2t −2η(t) −V −β)2 −V −2β)g(η(t))F V (ZV ◦η(t))
(3.9)
= O(V −2β).
Proof of Theorem 3.3.
For t ≤T deﬁne E(t) def
= E|XV (t) −ZV (t)|.
Letting ci denote constants
E(t) ≤
X
k
|νk|E

Z t
0
AV
k (XV (s))ds −
Z t
0
AV
k ◦ρV (ZV ◦η(s)) ds

≤c1
Z t
0
E(s)ds +
X
k
|νk|E

Z t
0
AV
k (ZV (s)) −AV
k ◦ρV (ZV ◦η(s)) ds

≤c1
Z t
0
E(s)ds + c2V −κ(β),
where the ﬁnal inequality used both (3.8) and (3.9). The result now follows
from Gronwall’s inequality.
□


## Page 14


14
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
3.3. Exact asymptotics for Euler tau-leaping.
Throughout this section
and the next, all convergences are understood to hold on bounded intervals.
More explicitly, we write XV →X if limV →∞P{supt≤T |XV (t) −X(t)| >
ε} = 0 for all ε > 0 and T > 0. Because of the simplifying assumptions made
on the kinetics in Section 2.2, it is not diﬃcult to show that XV →X also
implies limV →∞Esupt≤T |XV (t) −X(t)| = 0. In light of this, when we write
XV = ZV + O(V −p) for some p > 0 in this section and the next we mean
that for any T > 0 there exists a C(T) such that
lim
V →∞V pEsup
t≤T
|XV (t) −ZV (t)| ≤C(T).
Finally, recall that F V (x) = P
k AV
k (x)νk and note that the function F(x)
and the deterministic process x(s) used in the characterization of the error
processes are deﬁned via (2.1).
Theorem 3.2 suggests that XV −ZV scales like V −β. In this section, we
make this precise by characterizing the limiting behavior of V β(XV −ZV ),
as V →∞. To get the exact asymptotics for the Euler tau-leap method, we
will use the following coupling of the processes involved:
XV (t) = XV (0)
+ 1
V
X
k

Yk,1

V
Z t
0
AV
k (XV (s)) ∧AV
k (ZV ◦η(s)) ds

(3.10)
+ Yk,2

V
Z t
0
AV
k (XV (s))
−AV
k (XV (s)) ∧AV
k (ZV ◦η(s)) ds

νk,
ZV (t) = XV (0)
+ 1
V
X
k

Yk,1

V
Z t
0
AV
k (XV (s)) ∧AV
k (ZV ◦η(s)) ds

(3.11)
+ Yk,3

V
Z t
0
AV
k (ZV ◦η(s))
−AV
k (XV (s)) ∧AV
k (ZV ◦η(s))ds

νk.
It is important to note that the distributions of XV and ZV deﬁned via (3.10)
and (3.11) are the same as those for the processes deﬁned via (3.1) and (3.2).
The following lemma is easy to prove using Doob’s inequality.
Lemma 3.6.
For XV and ZV given by (3.10) and (3.11), XV −ZV →0.


## Page 15


ERROR ANALYSIS OF TAU-LEAP METHODS
15
Combining Lemma 3.6 and (2.2) shows that ZV −x →0, where x is the
solution to the associated ODE. Similarly, ZV ◦η −x →0. These facts will
be used throughout this section.
Centering the Poisson processes, we have
XV (t) −ZV (t) = MV (t) +
Z t
0
F V (XV (s)) −F V (ZV ◦η(s))ds
= MV (t) +
Z t
0
F V (XV (s)) −F V (ZV (s))ds
(3.12)
+
Z t
0
F V (ZV (s)) −F V (ZV ◦η(s)) ds,
where MV is a martingale.
To obtain the desired results, we must understand the behavior of the ﬁrst
and third terms on the right-hand side of (3.12). We begin by considering
the third term. We begin by deﬁning U V,2 and ˜U V,2 by
U V,2(s) def
= ZV (s) −ZV ◦η(s),
˜U V,2(s) def
= (s −η(s))F V (ZV ◦η(s)).
Then,
U V,2(s) −˜U V,2(s) = ˜ZV (s) −˜ZV ◦η(s),
where ˜ZV (t) def
= ZV (t) −
R t
0 F V (ZV ◦η(s))ds is a martingale. Thus,
F V (ZV (s)) −F V (ZV ◦η(s))
= DF V (ZV ◦η(s))U V,2(s) + O(V −2β)
(3.13)
= DF V (ZV ◦η(s)) ˜U V,2(s) + DF V (ZV ◦η(s))(U V,2(s) −˜U V,2(s))
+ O(V −2β).
Lemma 3.7.
For all 0 < β < 1, 0 < t, and α ∈{2,3,4,...}
lim
V →∞V αβ sup
s≤t
E[|U V,2(s) −˜U V,2(s)|α] = 0.
Proof.
The proof is similar to that of Lemma 3.5.
□
We may now characterize the limiting behavior of the third term of (3.12).
Lemma 3.8.
For 0 < β < 1 and any t > 0,
V β
Z t
0
F V (ZV (s)) −F V (ZV ◦η(s))ds →1
2
Z t
0
DF(x(s))F(x(s))ds.


## Page 16


16
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
Proof.
By (3.13) and Lemma 3.7
V β
Z t
0
F V (ZV (s)) −F V (ZV ◦η(s))ds
= V β
Z t
0
DF V (ZV ◦η(s))F V (ZV ◦η(s))(s −η(s)) ds + εV
1 (t),
where εV
1 →0 as V →∞. By Lemma 3.6 convergence results similar to (2.2)
hold for the process ZV ◦η, and because
R η(s)+V −β
η(s)
(r −η(s))dr = 1
2V −2β,
the lemma holds as stated.
□
Turning now to MV , we observe that the quadratic covariation is
[MV ]t = 1
V 2
X
k
(N V
k,2(t) + N V
k,3(t))νkνT
k ,
where
N V
k,2(t) def
= Yk

V
Z t
0
AV
k (XV (s)) −AV
k (XV (s)) ∧AV
k (ZV ◦η(s))

,
N V
k,3(t) def
= Yk

V
Z t
0
AV
k (ZV ◦η(s)) −AV
k (XV (s)) ∧AV
k (ZV ◦η(s))

,
which as V →∞is asymptotic to
1
V
X
k
Z t
0
|AV
k (XV (s)) −AV
k (ZV ◦η(s))|dsνkνT
k .
(3.14)
We have the following lemma.
Lemma 3.9.
For 0 < β < 1, V βMV →0, as V →∞.
Proof.
Multiplying (3.12) by V α, we see that V α(XV −ZV ) →0 pro-
vided α < β (so that the third term on the right goes to zero) and provided
V αMV →0. By the martingale central limit theorem, the latter convergence
holds provided V 2α[MV ] →0 (see Lemma A.2 in the Appendix). Let α0 =
sup{α:α ≤β,V 2α[MV ] →0}. Since α0 < 1, we have that 2α0 −1 < α0 ≤β,
which implies by the deﬁnition of α0 that V 2α0−1(XV −ZV ) →0. Therefore,
V 2α0[MV ]t
≈
X
k
Z t
0
V 2α0−1|AV
k (XV (s)) −AV
k (ZV ◦η(s))|dsνkνT
k
≈
X
k
Z t
0
V 2α0−1|∇AV
k (ZV ◦η(s)) · (ZV (s) −ZV ◦η(s))|dsνkνT
k
≈
X
k
Z t
0
V 2α0−1|∇AV
k (ZV ◦η(s)) · F V (ZV ◦η(s))|(s −η(s))dsνkνT
k ,


## Page 17


ERROR ANALYSIS OF TAU-LEAP METHODS
17
where in the second approximation we used that V 2α0−1(XV −ZV ) →0, in
the third approximation we substituted ˜U V,2(s) for U V,2(s), and by f ≈g
we mean f −g →0 as V →∞. The last expression goes to zero whenever
2α0 −1 < β, hence the convergence holds.
□
We now have the following theorem characterizing the behavior of
V β(XV −ZV ).
Theorem 3.10.
For XV and ZV given by (3.10) and (3.11) and for
0 < β < 1, V β(XV −ZV ) →E, where E is the solution to
E(t) =
Z t
0
DF(x(s))E(s)ds
(3.15)
+ 1
2
Z t
0
DF(x(s))F(x(s))ds,
E(0) = 0.
Proof.
Multiply (3.12) by V β and observe that
V β
Z t
0
F V (XV (s))−F V (ZV (s))ds ≈
Z t
0
DF V (ZV (s))V β(XV (s)−ZV (s))ds.
The theorem now follows directly from Lemmas 3.8 and 3.9.
□
3.4. Exact asymptotics for midpoint tau-leaping.
Throughout this sec-
tion, the Hessian matrix associated with a real valued function g will be
denoted by Hg. Also, for any vector U, we will denote by U T HF V (x)U the
vector whose ith component is U T HF V
i U, and similarly for F.
The goal of this section is to characterize the limiting behavior of
V κ(β)(XV (t) −ZV (t)),
where
κ(β) = min{2β,(1 + β)/2} =

2β,
β < 1/3,
(1 + β)/2,
β ≥1/3.
To get the exact asymptotics for the midpoint method, we will use the
following representation of the processes involved:
XV (t) = XV (0)
+ 1
V
X
k

Yk,1

V
Z t
0
AV
k (XV (s)) ∧AV
k (ρV ◦ZV ◦η(s))ds

(3.16)
+ Yk,2

V
Z t
0
AV
k (XV (s))
−AV
k (XV (s)) ∧AV
k (ρV ◦ZV ◦η(s)) ds

νk,


## Page 18


18
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
ZV (t) = XV (0)
+ 1
V
X
k

Yk,1

V
Z t
0
AV
k (XV (s)) ∧AV
k (ρV ◦ZV ◦η(s))ds

(3.17)
+ Yk,3

V
Z t
0
AV
k (ρV ◦ZV ◦η(s))
−AV
k (XV (s)) ∧AV
k (ρV ◦ZV ◦η(s)) ds

νk.
The following is similar to Lemma 3.6.
Lemma 3.11.
For XV and ZV given by (3.16) and (3.17), XV −ZV →0.
Combining Lemma 3.11 and (2.2) shows that ZV −x →0, where x is the
solution to the associated ODE. Similarly ZV ◦η −x →0. These facts will
be used throughout this section.
Centering the Poisson processes, we have
XV (t) −ZV (t) = MV (t) +
Z t
0
F V (XV (s)) −F V (ρV ◦ZV ◦η(s)) ds
= MV (t) +
Z t
0
F V (XV (s)) −F V (ZV (s))ds
(3.18)
+
Z t
0
F V (ZV (s)) −F V (ρV ◦ZV ◦η(s)) ds,
where MV is a martingale.
As before, we must understand the behavior of the ﬁrst and third terms
on the right-hand side of (3.18). We begin by considering the third term.
Proceeding as in the previous sections, we deﬁne U V,3 and ˜U V,3 as
U V,3(s) def
= ZV (s)−ρV ◦ZV ◦η(s) = ZV (s)−ZV ◦η(s)−1
2V −βF V (ZV ◦η(s))
and
˜U V,3(s) def
= (s −η(s) −1
2V −β)F V (ZV ◦η(s)).
Then
U V,3(s) −˜U V,3(s)
= ˜ZV (s) −˜ZV ◦η(s)
(3.19)
+ (s −η(s))(F V (ρV ◦ZV ◦η(s)) −F V (ZV ◦η(s))),


## Page 19


ERROR ANALYSIS OF TAU-LEAP METHODS
19
where ˜ZV (t) def
= ZV (t) −
R t
0 F V (ρV ◦ZV ◦η(s))ds is a martingale. Then
F V (ZV (s)) −F V (ρV ◦ZV ◦η(s))
= DF V (ρV ◦ZV ◦η(s))U V,3(s)
+ 1
2U V,3(s)T HF V (ρV ◦ZV ◦η(s))U V,3(s) + O(V −3β)
(3.20)
= DF V (ρV ◦ZV ◦η(s)) ˜U V,3(s)
+ 1
2U V,3(s)T HF V (ρV ◦ZV ◦η(s))U V,3(s)
+ DF V (ρV ◦ZV ◦η(s))(U V,3(s) −˜U V,3(s)) + O(V −3β).
Lemma 3.12.
For all 0 < β < 1, 0 < t, and α ∈{2,3,4,...}
lim
V →∞V αβ sup
s≤t
E[|U V,3(s) −˜U V,3(s)|α] = 0.
Proof.
The proof is similar to Lemma 3.5.
□
Let
κ1(β) = min{2β,β + 1/2} =

2β,
β < 1/2,
β + 1/2,
β ≥1/2.
Note that κ1(β) ≥κ(β) for all β ≥0.
Lemma 3.13.
For 0 < β < 1
2 and each t > 0,
V 2β
Z t
0
DF V (ρV ◦ZV ◦η(s))(U V,3(s) −˜U V,3(s))ds
(3.21)
→1
4
Z t
0
DF(x(s))2F(x(s))ds,
for β = 1
2
V
Z t
0
DF V (ρV ◦ZV ◦η(s))(U V,3(s) −˜U V,3(s))ds
(3.22)
⇒M1(t) + 1
4
Z t
0
DF(x(s))2F(x(s))ds,
and for 1
2 < β < 1,
V β+1/2
Z t
0
DF V (ρV ◦ZV ◦η(s))(U V,3(s) −˜U V,3(s)) ds ⇒M1(t),
(3.23)


## Page 20


20
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
where M1 is a mean zero Gaussian process with independent increments and
quadratic covariation
[M1]t = 1
3
Z t
0
X
k
Ak(x(s))DF(x(s))νkνT
k DF(x(s))T ds.
(3.24)
Proof.
By Lemma A.1 in the Appendix,
MV
1 (t) def
=
Z t
0
DF V (ρV ◦ZV ◦η(s))( ˜ZV (s) −˜ZV ◦η(s)) ds
+ DF V (ρV ◦ZV ◦η(t))( ˜ZV (t) −˜ZV ◦η(t))(η(t) + V −β −t)
is a martingale and its quadratic covariation matrix is
Z t
0
(η(s) + V −β −s)2DF V (ρV ◦ZV ◦η(s)) d[ ˜ZV ]sDF V (ρV ◦ZV ◦η(s))T .
Noting that
R η(s)+V −β
η(s)
(η(r) + V −β −r)2 dr = 1
3V −3β, it follows that
V 2β+1[MV
1 ]t →1
3
Z t
0
X
k
Ak(x(s))DF(x(s))νkνT
k DF(x(s))T ds,
so by the martingale central limit theorem V β+1/2MV
1 converges in distri-
bution to a mean zero Gaussian process with independent increments and
quadratic variation (3.24).
Since V 1/2( ˜ZV −˜ZV ◦η) →0, the integral on the left-hand side of (3.21),
(3.22) and (3.23) can be replaced by
MV
1 (t) +
Z t
0
DF V (ρV ◦ZV ◦η(s))(s −η(s))
(3.25)
× (F V (ρV ◦ZV ◦η(s)) −F V (ZV ◦η(s)))ds
without changing the limits. The second term in (3.25) multiplied by V 2β
converges to 1
4
R t
0 DF(x(s))2F(x(s))ds on bounded time intervals and the
three limits follow.
□
Lemma 3.14.
For 0 < β < 1,
V 2β 1
2
Z t
0
U V,3(s)T HF V (ρV ◦ZV ◦η(s))U V,3(s)ds
→1
24
Z t
0
F(x(s))T HF(x(s))F(x(s))ds.


## Page 21


ERROR ANALYSIS OF TAU-LEAP METHODS
21
Proof.
By Lemma 3.12, we can replace U V,3by ˜U V,3. Observing that
R η(s)+V −β
η(s)
(s −η(s) −1
2V −β)2 ds = 1
12V −3β,
V 2β 1
2
Z t
0

s −η(s) −1
2V −β
2
F V (ZV ◦η(s))T HF V (ρV ◦ZV ◦η(s))
× F V (ZV ◦η(s)) ds
converges as claimed.
□
We may now characterize the behavior of the third term of (3.18).
Lemma 3.15.
Let
RV (t) =
Z t
0

s −η(s) −1
2V −β

DF V (ρV ◦ZV ◦η(s))F V (Z ◦η(s)) ds.
Then for 0 < β < 1
2,
V 2β
Z t
0
(F V (ZV (s)) −F V (ρV ◦ZV ◦η(s)))ds −RV (t)

→1
4
Z t
0
DF(x(s))2F(x(s))ds + 1
24
Z t
0
F(x(s))T HF(x(s))F(x(s))ds,
for β = 1
2,
V
Z t
0
(F V (ZV (s)) −F V (ρV ◦ZV ◦η(s)))ds −RV (t)

⇒M1(t) + 1
4
Z t
0
DF(x(s))2F(x(s))ds
+ 1
24
Z t
0
F(x(s))T HF(x(s))F(x(s))ds
and for 1
2 < β < 1,
V β+1/2
Z t
0
(F V (ZV (s)) −F V (ρV ◦ZV ◦η(s)))ds ⇒M1(t).
Remark.
Note that V 2βRV is uniformly bounded, RV ◦η ≡0, and
RV (t) = 1
2[(t −η(t))2 −(t −η(t))V −β]DF V (ρV ◦ZV ◦η(t))F V (Z ◦η(t)).
Proof of Lemma 3.15.
The lemma follows from (3.20), the previous
lemmas, and by noting that
R t
0 DF V (ρV ◦ZV ◦η(s)) ˜U V,3(s)ds = RV (t).
□
We now turn to MV and observe that
[MV ]t = 1
V 2
X
k
(N V
k,2(t) + N V
k,3(t))νkνT
k ,


## Page 22


22
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
where
N V
k,2(t) def
= Yk

V
Z t
0
AV
k (XV (s)) −AV
k (XV (s)) ∧AV
k (ρV ◦ZV ◦η(s)) ds

,
N V
k,3(t) def
= Yk

V
Z t
0
AV
k (ρV ◦ZV ◦η(s))
−AV
k (XV (s)) ∧AV
k (ρV ◦ZV ◦η(s))ds

,
which as V →∞is asymptotic to
1
V
X
k
Z t
0
|AV
k (XV (s)) −AV
k (ρV ◦ZV ◦η(s))|dsνkνT
k .
Consequently, we have the following.
Lemma 3.16.
For 0 < β < 1, V (1+β)/2MV ⇒M where M is a mean-zero
Gaussian process with independent increments and quadratic covariation
[M]t =
X
k
1
4
Z t
0
|∇Ak(x(s)) · F(x(s))|dsνkνT
k .
Proof.
Multiplying (3.18) by V α, we see that V α(XV −ZV ) →0 pro-
vided α < κ1(β) (so that the third term on the right goes to zero) and
provided V αMV →0. By the martingale central limit theorem, the lat-
ter convergence holds provided V 2α[MV ] →0. Let α0 = sup{α:α ≤(β +
1)/2,V 2α[MV ] →0}. We make two observations. First, because α0 < 1,
we have that 2α0 −1 < α0. Second, because α0 ≤(β + 1)/2, we have that
2α0 −1 ≤β, and, in particular, 2α0 −1 < κ1(β) for all β ∈(0,1). Combining
these observations with the deﬁnition of α0 shows that V 2(2α0−1)[MV ]t →0
and hence V 2α0−1(XV −ZV ) →0. We now have
V 2α0[MV ]t ≈
X
k
Z t
0
V 2α0−1|Ak(XV (s)) −Ak(ρV ◦ZV ◦η(s))|dsνkνT
k
≈
X
k
Z t
0
V 2α0−1
s −η(s) −1
2V −β

× |∇Ak(ρV ◦ZV ◦η(s)) · F V (ZV ◦η(s))|dsνkνT
k ,
where in the second line we used that V 2α0−1(XV −ZV ) →0, and then
substituted ˜U V,3(s) for U V,3(s). Since the last expression would go to zero
if 2α0 −1 were less than β, we see that 2α0 −1 = β, that is, α0 = (β + 1)/2.
Furthermore, observing that
R η(s)+V −β
η(s)
|s−η(s)−1
2V −β|ds = 1
4V −2β, we see


## Page 23


ERROR ANALYSIS OF TAU-LEAP METHODS
23
that
V β+1[MV ]t = V 2α0[MV ]t →
X
k
1
4
Z t
0
|∇Ak(x(s)) · F(x(s))|dsνkνT
k ,
and the lemma follows by the martingale central limit theorem.
□
Collecting the results, we have the following theorem.
Theorem 3.17.
Let
H(t) = 1
6
Z t
0
DF(x(s))2F(x(s))ds + 1
24
Z t
0
F(x(s))T HF(x(s))F(x(s))ds.
For 0 < β < 1
3, V 2β(XV −ZV −RV ) →E1, where E1 is the solution of
E1(t) =
Z t
0
DF(x(s))E1(s)ds + H(t),
E1(0) = 0.
(3.26)
For β = 1
3, V 2β(XV −ZV −RV ) ⇒E2, where E2 is the solution of
E2(t) = M(t) +
Z t
0
DF(x(s))E2(s)ds + H(t),
E2(0) = 0.
(3.27)
For 1
3 < β < 1, V (1+β)/2(XV −ZV ) ⇒E3, where E3 is the solution of
E3(t) = M(t) +
Z t
0
DF(x(s))E3(s)ds,
E3(0) = 0.
(3.28)
Proof.
For β ≤1
3, RV is O(V −2β). Subtract RV from both sides of (3.18)
and observe that
Z t
0
F V (XV (s)) −F V (ZV (s))ds
≈
Z t
0
DF V (ZV (s))(XV (s) −ZV (s) −RV (s)) ds
+
Z t
0
DF V (ZV (s))RV (s)ds.
Since
V 2β
Z t
0
DF V (ZV (s))RV (s)ds →−1
12
Z t
0
DF(x(s))2F(x(s))ds,
the ﬁrst two parts follow from Lemmas 3.15 and 3.16.
For β > 1
3, (1 + β)/2 < 2β ∧κ1(β), so V (1+β)/2RV →0 and
V (1+β)/2
Z t
0
F V (ZV (s)) −F V (ρV ◦ZV ◦η(s))ds →0,
and the third part follows by Lemma 3.16.
□


## Page 24


24
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
4. Weak error analysis.
As in previous sections, we assume the existence
of a time discretization 0 = t0 < t1 < ··· < tN = T with tn −tn−1 = V −β for
some 0 < β < 1. We also recall that η(s) = tn for tn ≤s < tn+1 for each
n ≤N −1.
Let XV be a Markov process with generator
(AV f)(x) =
X
k
V AV
k (x)(f(x + νk/V ) −f(x)).
(4.1)
Deﬁning the operator
(BV
z f)(x) =
X
k
V AV
k (z)(f(x + νk/V ) −f(x)),
(4.2)
we suppose that ZV and ZV are processes that satisfy
Ef(Z(t)) = Ef(Z ◦η(t)) + E
Z t
η(t)
(BZ◦η(t)f)(Z(s))ds
(4.3)
and
Ef(Z(t)) = Ef(Z ◦η(t)) + E
Z t
η(t)
(BρV ◦Z◦η(t)f)(Z(s))ds
(4.4)
for all t > 0, respectively.
We begin with the weak error analysis of Euler tau-leaping, which is
immediate in light of Theorem 3.10.
Theorem 4.1.
Let XV (t) be a Markov process with generator (4.1) and
let ZV (t) be a process that satisﬁes (4.3) for the operator (4.2). Then, for
any continuously diﬀerentiable function f and any t ≤T,
lim
V →∞V β(Ef(XV (t)) −Ef(ZV (t))) = E(t) · ∇f(x(t)),
where E(t) satisﬁes (3.15).
Proof.
Without loss of generality, we may assume that XV (t) and ZV (t)
satisfy (3.10) and (3.11), respectively. The proof now follows immediately
from a combination of Taylor’s theorem and Theorem 3.10.
□
Remark.
Because the convergence in Theorem 4.1 is to a constant in-
dependent of the step-size of the method, we see that Richardson extrapo-
lation techniques can be carried out. However, we have not given bounds on
the next order correction, and so cannot say how much more accurate such
techniques would be.
We now consider the weak error analysis of the midpoint method.
Theorem 4.2.
Let XV (t) be a Markov process with generator (4.1) and
let ZV (t) be a process that satisﬁes (4.4) for the operator (4.2). Then, for
any two times continuously diﬀerentiable function f with compact support,


## Page 25


ERROR ANALYSIS OF TAU-LEAP METHODS
25
there exists a constant C = C(f,T) > 0 such that
V 2β|Ef(XV (T)) −Ef(ZV (T))| ≤C.
Before proving Theorem 4.2, some preliminary material is needed. Let
LV def
= {y :y = x/V,x ∈Zd}, and for x ∈LV and a given function f, let
v(t,x) = Exf(XV (t)),
(4.5)
where Ex represents the expectation conditioned upon XV (0) = x. Standard
results give that v(t,x) satisﬁes the following initial value problem (see,
e.g., [7], Proposition 1.5)
∂tv(t,x) = AV v(t,x)
=
X
k
V AV
k (x)(v(t,x + νk/V ) −v(t,x)),
(4.6)
v(0,x) = f(x),
x ∈LV .
The above equation can be viewed as a linear system by letting x enumerate
over LV and treating v(t,x) = vx(t) as functions in time only. It can even
be viewed as ﬁnite dimensional because of the conditions on the intensity
functions AV
k . That is, recall that AV
k (x) = 0 for all x outside the bounded
set Ωγ (see Section 2.2); thus, for any such x /∈Ωγ, v(t,x) = vx(t) ≡f(x),
for all t > 0.
For concreteness, we now let M denote the number of reactions for the
system under consideration. For k,ℓ∈[1,...,M] and x ∈LV , let
Dk(t,x) = V (v(t,x + νk/V ) −v(t,x)),
(4.7)
Dkℓ(t,x) = V (Dk(t,x + νℓ/V ) −Dk(t,x))
(4.8)
represent approximations to the ﬁrst and second spatial derivatives of v(t,x),
respectively. For notational ease, we have chosen not to explicitly note the V
dependence of the functions v(t,x), Dk(t,x) or Dkℓ(t,x).
The following lemma, which should be viewed as giving regularity condi-
tions for v(t,x) in the x variable, is instrumental in the proof of Theorem 4.2.
The proof is delayed until the end of the section.
Lemma 4.3.
Let v(t,x), Dk(t,x) and Dkℓ(t,x) be given by (4.5), (4.7)
and (4.8), respectively, and let T > 0. There exists K1 > 0 and K2 > 0 that
do not depend upon V such that
sup
t≤T
sup
k≤M
sup
x∈LV |Dk(t,x)| ≤K1,
(4.9)
sup
t≤T
sup
k,ℓ≤M
sup
x∈LV |Dkℓ(t,x)| ≤K2.
(4.10)
We will also need the following lemma, which gives regularity conditions
for Dk(t,x) in the t variable, and whose proof is also delayed.


## Page 26


26
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
Lemma 4.4.
Let Dk(t,x) be given by (4.7). There exists a K > 0 that
does not depend upon V such that
sup
t≤T
sup
k≤M
sup
x∈LV |Dk(t + h,x) −Dk(t,x)| ≤Kh
for all h > 0.
Proof of Theorem 4.2.
Deﬁne the function u(t,x):[0,T] × LV →R
by
u(t,x) def
= Exf(XV (T −t)),
(4.11)
and for any w(t,x):R × LV →R we deﬁne the operator L by
Lw(t,x) def
= ∂tw(t,x) + AV w(t,x)
= ∂tw(t,x) +
X
k
V AV
k (x)(w(t,x + νk/V ) −w(t,x)).
Note that u(t,x) = v(T −t,x), where v(t,x) is given by (4.5), and so by (4.6)
Lu(t,x) = 0 for t ∈[0,T] and x ∈LV . We also deﬁne the operator
Lzw(t,x) def
= ∂tw(t,x) + BV
z w(t,x)
= ∂tw(t,x) +
X
k
V AV
k (z)(w(t,x + νk/V ) −w(t,x)),
so that by virtue of equation (4.4), for t ≤T and any diﬀerentiable (in t)
function w(t,x)
Ew(t,ZV (t)) = Ew(η(t),ZV ◦η(t))
(4.12)
+
Z t
η(t)
ELρV ◦ZV ◦η(t)w(s,ZV (s))ds.
Recalling (4.11), we see that
Eu(T,ZV (T)) = Ef(ZV (T)),
Eu(T,XV (T)) = Eu(0,XV (0)) = Ef(XV (T)).
Therefore by (4.12), and using that XV (0) = ZV (0),
Ef(ZV (T)) −Ef(XV (T))
= Eu(T,ZV (T)) −Eu(0,ZV (0))
=
N−1
X
n=0
Eu(tn+1,ZV (tn+1)) −Eu(tn,ZV (tn))
=
N−1
X
n=0
E
Z tn+1
tn
LρV ◦ZV (tn)u(s,ZV (s))ds.


## Page 27


ERROR ANALYSIS OF TAU-LEAP METHODS
27
Because Lu(t,x) ≡0 for t ≤T and x ∈LV
E
Z tn+1
tn
LρV ◦ZV (tn)u(s,ZV (s))ds
= E
Z tn+1
tn
LρV ◦ZV (tn)u(s,ZV (s)) −Lu(s,ZV (s))ds
=
X
k
E
Z tn+1
tn
V [AV
k (ρV ◦ZV (tn)) −AV
k (ZV (s))]
(4.13)
× (u(s,ZV (s) + νk/V ) −u(s,ZV (s))) ds
=
X
k
E
Z tn+1
tn
[AV
k (ρV ◦ZV (tn)) −AV
k (ZV (s))]Dk(T −s,ZV (s)) ds.
Thus, it is suﬃcient to prove that each of the integrals in (4.13) are O(V −3β).
By Lemma 4.4, each integral term in (4.13) can be replaced by
IV
k (tn) def
= E
Z tn+1
tn
[AV
k (ρV ◦ZV (tn)) −AV
k (ZV (s))]
(4.14)
× Dk(T −tn,ZV (s))ds.
The remainder of the proof consists of proving that IV
k (tn) = O(V −3β).
Letting gV
n (x) def
= [AV
k (ρV ◦ZV (tn))−AV
k (x)]Dk(T −tn,x) and applying (4.4)
to the integrand in (4.14) yields
IV
k (tn) = E
Z tn+1
tn
[AV
k (ρV ◦ZV (tn)) −AV
k (ZV (tn))]Dk(T −tn,ZV (tn)) ds
+
X
j
E
Z tn+1
tn
Z s
tn
V AV
j (ρV ◦ZV (tn))
× (gV
n (ZV (r) + νj/V ) −gV (ZV (r)))dr ds.
We have
AV
k (ρV ◦ZV (tn)) = AV
k (ZV (tn))
+ ∇AV
k (ZV (tn)) · 1
2V −β X
j
AV
j (ZV (tn))νj
+ O(V −2β).
Thus,
IV
k (tn) =
X
j
1
2V −βE
Z tn+1
tn
∇AV
k (ZV (tn)) · νjAV
j (ZV (tn))


## Page 28


28
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
(4.15)
× Dk(T −tn,ZV (tn))ds + O(V −3β)
+
X
j
E
Z tn+1
tn
Z s
tn
V AV
j (ρV ◦ZV (tn))
(4.16)
× (gV
n (ZV (r) + νj/V ) −gV (ZV (r))) dr ds.
After some manipulation, the expected value term of (4.16) becomes
E
Z tn+1
tn
Z s
tn
V AV
j (ρV ◦ZV (tn))[AV
k (ZV (r)) −AV
k (ZV (r) + νj/V )]
× Dk(T −tn,ZV (r) + νj/V )dr ds
+ E
Z tn+1
tn
Z s
tn
AV
j (ρV ◦ZV (tn))[AV
k (ρV ◦ZV (tn)) −AV
k (ZV (r))]
× Dkj(T −tn,ZV (r))dr ds.
By Lemma 4.3 the last term above is O(V −3β). Taylor’s theorem and the
fact that AV
j (ρV ◦ZV (tn)) = AV
j (ZV (tn) + O(V −β) then shows us that the
expected value term of (4.16) is equal to
−E
Z tn+1
tn
Z s
tn
AV
j (ZV (tn))∇AV
k (ZV (r))
× νjDk(T −tn,ZV (r) + νj/V )dr ds + O(V −3β)
(4.17)
= −E
Z tn+1
tn
Z s
tn
AV
j (ZV (tn))∇AV
k (ZV (r)) · νjDk(T −tn,ZV (r))dr ds
+ O(V −3β),
where the second equality stems from an application of Lemma 4.3.
By Lemma 4.3, the function φ(x) = AV
j (ZV (tn))∇AV
k (x) · νjDk(T −tn,x)
satisﬁes supℓ|φ(x + νℓ/V ) −φ(x)| = O(V −1). Therefore, applying (4.4)
to (4.17) shows that (4.17) is equal to
−E
Z tn+1
tn
Z s
tn
AV
j (ZV (tn))∇AV
k (ZV (tn)) · νjDk(T −tn,ZV (tn))dr ds
+ O(V −3β).
Noting that the sum over j of the above is the negative of (4.15) plus
an O(V −3β) correction concludes the proof.
□
Theorem 4.2 can be strengthened in the case of β < 1/3.


## Page 29


ERROR ANALYSIS OF TAU-LEAP METHODS
29
Theorem 4.5.
Let XV (t) be a process with generator (4.1) and let ZV (t)
be a process that satisﬁes (4.4) for the operator (4.2). Suppose also that
β < 1/3. Then, for any continuously diﬀerentiable function f,
lim
V →∞V 2β(Ef(XV (T)) −Ef(ZV (T))) = E1(T) · ∇f(x(T)),
where E1(t) satisﬁes (3.26).
Proof.
Noting that RV (T) ≡0, this is an immediate consequence of
Theorem 3.17.
□
Remark.
In Theorem 4.1, we provided an explicit asymptotic value for
the scaled error of Euler tau-leaping in terms of a solution to a diﬀerential
equation for all scales, 0 < β < 1, of the leap step. However, Theorem 4.5
gives a similar result for the midpoint method only in the case 0 < β < 1/3.
For the case 1/3 ≤β < 1, Theorem 4.2 only shows that the error is asymp-
totically bounded by a constant. The reason for the discrepancy in results is
because in Section 3 we were able to show that the dominant component of
the pathwise error for Euler tau-leaping for all β ∈(0,1) and for midpoint
tau-leaping for β ∈(0,1/3) was a term that converged to a deterministic
process. However, in the case β ≥1/3 for midpoint tau-leaping, the dom-
inant term of the error is a nonzero Gaussian process. We note that this
random error process should not be viewed as “extra ﬂuctuations,” as they
are present in the other cases. In these other cases, they are just dominated
by the error that arises from the deterministic “drift” or “bias” of the er-
ror process. We leave the exact characterization of the weak error of the
midpoint method in the case β ≥1/3 as an open problem.
We now present the delayed proofs of Lemmas 4.3 and 4.4.
Proof of Lemma 4.3.
Let C1 > 0 be such that
sup
x∈LV sup
k
|Dk(0,x)| = sup
x∈LV sup
k
|V (f(x + νk/V ) −f(x))| ≤C1.
Using (4.6), a tedious reordering of terms shows that Dk(t,x) satisﬁes
∂tDk(t,x) =
X
j
AV
j (x)V [Dk(t,x + νj/V ) −Dk(t,x)]
(4.18)
+
X
j
(AV
j (x + νk/V ) −AV
j (x))V Dj(t,x + νk/V ).
Similarly to viewing v(t,x) = vx(t) as a ﬁnite-dimensional linear system,
(4.18) can be viewed as a linear system for the variables Dk(t,x) = D{k,x}(t),


## Page 30


30
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
for k ∈[1,...,M] and x ∈LV . Because AV
j (x) ≡0 for all x /∈Ωγ, we see that
∂tDk(t,x) ≡0 for all x such that x /∈Ωγ and x + νj/V /∈Ωγ for all j ∈
[1,... ,M]. Therefore, the system (4.18) can be viewed as ﬁnite dimensional
also.
Let Γ1 = [1,...,M] × LV . We enumerate the system (4.18) over b ∈Γ1.
That is, for b = {k,x} ∈Γ1 we let Db(t) = Dk(t,x) = Db1(t,b2). After some
ordering of the set Γ1, we let RΓ1 denote the set of (inﬁnite) vectors, v,
whose bth component is vb ∈R, and then denote D(t) ∈RΓ1 as the vector
whose bth component is Db(t). Next, for each b = {k,x} ∈Γ1, we let
Sb
def
=
X
j
AV
j (b2) =
X
j
AV
j (x)
and let rb,Rb ∈RΓ1 satisfy
Rb · v =
X
j
AV
j (b2)v{b1,b2+νj/V },
rb · v =
X
j
(AV
j (b2 + νb1/V ) −AV
j (b2))V v{j,b2+νb1/V }
for all v ∈RΓ1. It is readily seen that for any b both Rb and rb have at
most M nonzero components. Also, by the regularity conditions on the
functions AV
j ’s, the absolute value of the nonzero terms of rb are uniformly
bounded above by some K, which is independent of V . Finally, note that
Rb · 1 = Sb. Combining the previous few sentences shows that for any vector
v ∈RΓ1, we have the two inequalities
|Rb · v| =

X
j
AV
j (b2)v{b1,b2+νj/V }
 ≤Sb∥v∥∞,
(4.19)
|rb · v| ≤KM∥v∥∞,
(4.20)
where ∥v∥∞
def
= supb∈Γ1 |vb|. We now write (4.18) as
D′
b(t) = −V SbDb(t) + V Rb · D(t) + rb · D(t),
and so for each b ∈Γ1
d
dtDb(t)2 = −2V SbDb(t)2 + 2V Db(t)Rb · D(t) + 2Db(t)rb · D(t).
(4.21)
Only a ﬁnite number of the terms Db(t) are changing in time and so there is
a b1 and a t1 ∈(0,T] for which |Db1(t)| = ∥D(t)∥∞for t ∈[0,t1]. By (4.19),
we have that for this b1 and any t ∈[0,t1]
Z t
0
Db1(s)Rb1 · D(s)ds ≤
Z t
0
Sb1|Db1(s)|∥D(s)∥∞ds =
Z t
0
Sb1Db1(s)2 ds,


## Page 31


ERROR ANALYSIS OF TAU-LEAP METHODS
31
which, after integrating (4.21), yields
∥D(t)∥2
∞= Db1(t)2 ≤Db1(0)2 + 2
Z t
0
Db1(s)rb1 · D(s)ds
≤∥D(0)∥2
∞+ 2KM
Z t
0
∥D(s)∥2
∞ds,
where the ﬁnal inequality makes use of (4.20). An application of Gronwall’s
inequality now gives us that for t ∈[0,t1]
∥D(t)∥2
∞≤∥D(0)∥2
∞e2KMt.
To complete the proof, continue this process for i ≥2 by choosing the bi
for which |Dbi(t)| is maximal on the time interval ti −ti−1. We must have
limi→∞ti = T because (i) there are a ﬁnite number of time varying Db(t)’s
and (ii) each Db(t) is diﬀerentiable. After taking square roots, we ﬁnd
supt≤T ∥D(t)∥∞≤∥D(0)∥∞eKMT ≤C1eKMT , which is equivalent to (4.9).
We now turn our attention to showing (4.10), which we show in a similar
manner. There is a C2 > 0 such that for all x ∈LV and k,ℓ∈[1,...,M],
|Dkℓ(0,x)| = V 2|f(x + νℓ/V + νk/V ) −f(x + νℓ/V ) −f(x + νk/V ) + f(x)|
≤C2.
Another tedious reordering of terms, which makes use of (4.18), shows
that Dkℓ(t,x) satisﬁes
∂tDkℓ(t,x)
=
X
j
AV
j (x)V [Dkℓ(t,x + νj/V ) −Dkℓ(t,x)]
+
X
j
(AV
j (x + νℓ/V ) −AV
j (x))V Dkj(t,x + νℓ/V )
+
X
j
(AV
j (x + νk/V ) −AV
j (x))V Djℓ(t,x + νk/V ) + gkℓ(t,x),
where
gkℓ(t,x) def
=
X
j
V 2[AV
j (x + νℓ/V + νk/V )
−AV
j (x + νℓ/V ) −AV
j (x + νk/V ) + AV
j (x)]
× Dj(t,x + νℓ/V + νk/V ).
By (i) the fact that the second derivative of AV
j is uniformly (in j and x)
bounded and (ii) the bound (4.9), the absolute value of the last term is
uniformly (in t ≤T, x,k and ℓ) bounded by some C3 > 0.


## Page 32


32
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
As we did for both v(t,x) and Dk(t,x), we change perspective by view-
ing the above as a linear system with state space {k,ℓ,x} ∈[1,...,M] ×
[1,... ,M]×LV = Γ2, where we again put an ordering on Γ2 and consider RΓ2
deﬁned similarly to RΓ1. Also similarly to before, we note that only a ﬁnite
number of the Dk,ℓ(t,x) are changing in time. For b = {k,ℓ,x} ∈Γ2, we see
that Db(t) satisﬁes
D′
b(t) = −SbV Db(t) + V Rb · D(t) + rb · D(t) + gb(t),
(4.22)
where Db(t),D(t),Sb, Rb and rb are deﬁned similarly as before and where
we retain the necessary inequalities: for v ∈RΓ2,
|Rb · v| =

X
j
AV
j (b3)v{b1,b2,b3+νj/V }
 ≤Sb∥v∥∞,
(4.23)
|rb · v| ≤2KM∥v∥∞.
The rest of the proof is similar to the proof that the Dk(t,x) are uniformly
bounded. There is a b1 ∈Γ2 and a t1 ∈(0,T] for which |Db1(t)| = ∥D(t)∥∞for
all t ∈[0,t1]. Taking the derivative of Db1(t)2 while using (4.22), integrating,
and using the bounds (4.23), we have that for this b1 and any t ∈[0,t1],
Db1(t)2 = Db1(0)2 + 2
Z t
0
gb1(s)Db1(s)ds −2
Z t
0
Sb1V Db1(s)2 ds
+ 2
Z t
0
V Rb1 · D(s)Db1(s)ds + 2
Z t
0
rb1 · D(s)Db1(s)ds
≤Db(0)2 + 2C3t + (4KM + 2C3)
Z t
0
∥D(s)∥2
∞ds,
where we used the inequality x ≤1 + x2 on the term Db1(s) in the ﬁrst
integral above. Therefore, for t ≤t1
∥D(t)∥2
∞≤∥D(0)∥2
∞+ 2C3t + (4KM + 2C3)
Z t
0
∥D(s)∥2
∞ds.
We continue now by choosing a b2 ∈Γ2 such that |Db2(t)| = ∥D(t)∥∞for all
t ∈[t1,t2), with t1 < t2 ≤T. By similar arguments as above, we have that
for t ∈[t1,t2],
∥D(t)∥2 ≤∥D(t1)∥2
∞+ 2C3(t −t1) + (4KM + 2C3)
Z t
t1
∥D(s)∥2
∞ds
≤∥h(0)∥2
∞+ 2C3t + (4KM + 2C3)
Z t
0
∥h(s)∥2
∞ds.


## Page 33


ERROR ANALYSIS OF TAU-LEAP METHODS
33
Continuing in this manner shows that the above inequality holds for all
t ∈[0,T] and so a Gronwall inequality gives us that for all t ≤T,
∥D(t)∥2
∞≤

∥D(0)∥2
∞+
2C3
4KM + 2C3

e(4KM+2C3)T ,
which, after taking square roots, is equivalent to (4.10).
□
Proof of Lemma 4.4.
By (4.18), we have that for any k ∈[1,...,M]
and x ∈LV ,
Dk(t,x) = Dk(0,x) +
X
j
AV
j (x)
Z t
0
Dkj(s,x)ds
+
X
j
(AV
j (x + νk/V ) −AV
j (x))V
Z t
0
Dj(s,x + νk/v)ds.
The proof is now immediate in light of Lemma 4.3.
□
5. Examples.
Example 5.1.
Consider the case of an irreversible isomerization of one
molecule into another. We denote by A the molecule undergoing the iso-
merization and B the target molecule. We assume that the rate constant
associated with this reaction is 1. The pictorial representation for this sys-
tem is simply
A 1→B.
Letting X(t) denote the number of A molecules at time t ≥0, X(t) satisﬁes
X(t) = X(0) −Y
Z t
0
X(s)ds

.
Supposing that we start with V = 10,000 molecules, we approximate the
distribution of X(1) using 200,000 sample paths constructed using the Gille-
spie algorithm, which produces statistically exact sample paths, Euler tau-
leaping with a step-size of 1/20 and midpoint tau-leaping with a step-size of
1/20. Note that in this case 1/20 = 1/V 0.325, and so β = 0.325. The compu-
tational results are presented in Figure 1, which demonstrate the stronger
convergence rate of midpoint tau-leaping as compared to Euler tau-leaping.
It is simple to show that X(1) is a binomial(n,p) random variable with
parameters n = 10,000 and p = 1/e. Therefore, EX(1) = 10,000/e ≈3678.8.
The estimated means produced from the 200,000 sample paths of Euler
tau-leaping and midpoint tau-leaping were 3585.4 and 3681.4, respectively.


## Page 34


34
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
Fig. 1.
Relative frequency of X(1) from 200,000 sample paths constructed using (i) Gille-
spie’s algorithm, blue line ∇marker, (ii) Euler tau-leaping, green line, ⃝marker, and
(iii) midpoint tau-leaping, red line, ∗marker. The approximated distribution generated via
midpoint tau-leaping is clearly closer to the exact distribution than that of Euler tau-leap-
ing.
Solving for E(t) of (3.15) for this example yields E(t) = (1/2)e−tt. Theo-
rem 4.1 therefore estimates that Euler tau-leaping should produce a mean
(1/2)e−110,0001−0.325 ≈92.2 smaller than the actual mean, which is in agree-
ment with 3678.8−3585.4 = 93.4. Solving for E1(t) of (3.26) for this example
yields E1(t) = (1/6)te−t. Theorem 4.5 therefore estimates that midpoint tau-
leaping should produce a mean (1/6)e−110,0001−2∗0.325 = 4.62 smaller than
the actual mean, which is in agreement with 3678.8 −3681.4 = −2.6.
Example 5.2.
We now consider a simple Lotka–Volterra predator–prey
model. Letting A and B represent the prey and predators, respectively, in
a given environment we suppose (i) prey reproduce at a certain rate, (ii) in-
teractions between predators and prey beneﬁt the predator while hurting
the prey, and (iii) predators die at a certain rate. One possible model for
this system is
A 2→2A,
A + B 0.002
→2B,
B 2→∅,
where a choice of rate constants has been made. Letting X(t) ∈Z2
≥0 be such
that X1(t) and X2(t) represent the numbers of prey and predators at time
t > 0, respectively, X(t) satisﬁes
X(t) = X(0) + Y1
Z t
0
2X1(s)ds

1
0



## Page 35


ERROR ANALYSIS OF TAU-LEAP METHODS
35
Fig. 2.
Oscillations in a predator–prey model. In the left image we see the numbers of
predators versus the number of prey for a single realization of the system (5.1). In the right
image we see the time-series of the numbers of predators and prey for a single realization
of (5.1).
+ Y2
Z t
0
0.002X1(s)X2(s)ds

−1
1

(5.1)
+ Y3
Z t
0
2X2(s)ds

0
−1

.
We take X(0) = [1,000,1,000]T , and so V = 1,000 for our model. Lotka–
Volterra models are famous for producing periodic solutions; this behavior
is demonstrated in Figure 2.
We approximate the distribution of X2(10) using 30,000 sample paths
constructed using the Gillespie algorithm, Euler tau-leaping with a step-size
of 1/20 and midpoint tau-leaping with a step-size of 1/20. Note that in
this case 1/20 = 1/V 0.434, and so β = 0.434. The computational results are
presented in Figure 3, which again demonstrate the stronger convergence
rate of midpoint tau-leaping as compared to Euler tau-leaping.
APPENDIX
Lemma A.1.
Let M be a {Ft}-martingale, R be bounded and {Ft}-
adapted, and let h > 0. Then for η(t) ≡[t/h]h,
ˆ
M(t) =
Z t
0
R◦η(s)(M(s)−M ◦η(s)) ds+R◦η(t)(M(t)−M ◦η(t))(η(t)+h−t)
is an {Ft}-martingale and
[ ˆ
M]t =
Z t
0
(R ◦η(r))2(η(r) + h −r)2 d[M]r.
(A.1)


## Page 36


36
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
Fig. 3.
Relative frequency of X2(10) from 30,000 sample paths constructed using
(i) Gillespie’s algorithm, blue line ∇marker, (ii) Euler tau-leaping, green line, ⃝marker,
and (iii) midpoint tau-leaping, red line, ∗marker. The approximated distribution gener-
ated via midpoint tau-leaping is clearly closer to the exact distribution than that of Euler
tau-leaping.
If M is Rd-valued and R is Mm×d-valued, then the quadratic covariation
matrix is
[ ˆ
M]t =
Z t
0
(η(r) + h −r)2R ◦η(r)d[M]rRT ◦η(r).
Proof.
For t < T −h,
E[ ˆ
M(T)|Ft] = E
Z T
0
R ◦η(s)(M(s) −M ◦η(s)) ds|Ft

= E
Z η(t)+h
0
R ◦η(s)(M(s) −M ◦η(s)) ds|Ft

=
Z t
0
R ◦η(s)(M(s) −M ◦η(s)) ds
+ R ◦η(t)(M(t) −M ◦η(t))(η(t) + h −t).
The case of T −h ≤t < T is similar. [ ˆ
M] is just the quadratic variation of
the second term on the right, and noting that ˆ
M is continuous at t = kh for
all k = 0,1,2... , (A.1) follows.
□
For completeness, we include a statement of the martingale central limit
theorem (see [6] for more details).


## Page 37


ERROR ANALYSIS OF TAU-LEAP METHODS
37
Lemma A.2.
Let {Mn} be a sequence of Rd-valued martingales with
Mn(0) = 0. Suppose
lim
n→∞E
h
sup
s≤t
|Mn(s) −Mn(s−)|
i
= 0
and
[Mi
n,Mj
n]t →ci,j(t)
for all t>0 where C =((ci,j)) is deterministic and continuous. Then Mn ⇒M,
where M is Gaussian with independent increments and E[M(t)M(t)T ] = C(t).
REFERENCES
[1] Anderson, D. F. (2007). A modiﬁed next reaction method for simulating chemi-
cal systems with time dependent propensities and delays. J. Chem. Phys. 127
214107.
[2] Anderson, D. F. (2008). Incorporating postleap checks in tau-leaping. J. Chem.
Phys. 128 054103.
[3] Cao, Y., Gillespie, D. T. and Petzold, L. R. (2005). Avoiding negative popula-
tions in explicit Poisson tau-leaping. J. Chem. Phys. 123 054104.
[4] Cao, Y., Gillespie, D. T. and Petzold, L. R. (2006). Eﬃcient step size selection
for the tau-leaping simulation method. J. Chem. Phys. 124 044109.
[5] Chatterjee, A., Vlachos, D. G. and Katsoulakis, M. A. (2005). Binomial dis-
tribution based tau-leap accelerated stochastic simulation. J. Chem. Phys. 122
024112.
[6] Ethier, S. N. and Kurtz, T. G. (1986). Markov Processes: Characterization and
Convergence. Wiley, New York. MR0838085
[7] Ethier, S. N. and Kurtz, T. G. (2005). Markov Processes: Characterization and
Convergence, 2nd ed. Wiley, New York.
[8] Gibson, M. A. and Bruck, J. (2000). Eﬃcient exact stochastic simulation of chem-
ical systems with many species and many channels. J. Phys. Chem. A 105 1876–
1889.
[9] Gillespie, D. T. (1976). A general method for numerically simulating the stochastic
time evolution of coupled chemical reactions. J. Comput. Phys. 22 403–434.
MR0503370
[10] Gillespie, D. T. (1977). Exact stochastic simulation of coupled chemical reactions.
J. Phys. Chem. 81 2340–2361.
[11] Gillespie, D. T. (2001). Approximate accelerated simulation of chemically reaction
systems. J. Chem. Phys. 115 1716–1733.
[12] Gillespie, D. T. and Petzold, L. R. (2003). Improved leap-size selection for ac-
celerated stochastic simulation. J. Chem. Phys. 119 8229–8234.
[13] Kloeden, P. E. and Platen, E. (1992). Numerical Solution of Stochastic Diﬀer-
ential Equations. Applications of Mathematics (New York) 23. Springer, Berlin.
MR1214374
[14] Kurtz, T. G. (1972). The relationship between stochastic and deterministic models
for chemical reactions. J. Chem. Phys. 57 2976–2978.
[15] Kurtz, T. G. (1977/78). Strong approximation theorems for density dependent
Markov chains. Stochastic Processes Appl. 6 223–240. MR0464414


## Page 38


38
D. F. ANDERSON, A. GANGULY AND T. G. KURTZ
[16] Kurtz, T. G. (1981). Approximation of Population Processes. CBMS-NSF Re-
gional Conference Series in Applied Mathematics 36. SIAM, Philadelphia, PA.
MR0610982
[17] Li, T. (2007). Analysis of explicit tau-leaping schemes for simulating chemically
reacting systems. Multiscale Model. Simul. 6 417–436 (electronic). MR2338489
[18] Rathinam, M., Petzold, L. R., Cao, Y. and Gillespie, D. T. (2005). Consistency
and stability of tau-leaping schemes for chemical reaction systems. Multiscale
Model. Simul. 4 867–895 (electronic). MR2203944
[19] Wilkinson, D. J. (2006). Stochastic Modelling for Systems Biology. Chapman and
Hall/CRC, Boca Raton, FL. MR2222876
D. F. Anderson
T. G. Kurtz
Department of Mathematics
University of Wisconsin
480 Lincoln Drive
Madison, Wisconsin 53706
USA
E-mail: anderson@math.wisc.edu
kurtz@math.wisc.edu
URL: http://www.math.wisc.edu/˜anderson/
http://www.math.wisc.edu/˜kurtz/
A. Ganguly
Automatic Control Laboratory
Swiss Federal Institute of Technology
Physikstrasse 3, ETL I13
8092 Z¨urich
Switzerland
E-mail: gangulya@control.ee.ethz.ch
URL: http://control.ee.ethz.ch/˜gangulya/

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]